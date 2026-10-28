#!/usr/bin/env python3
"""Hook Stop: controlla l'ultimo messaggio di Claude prima che arrivi al docente.

Se trova uno degli errori registrati, blocca la fine del turno con
{"decision": "block", "reason": ...}: Claude deve riscrivere il messaggio.
1. (a) Ordine copia/incolla sbagliato (#50, #138): dopo un «Ctrl+C» del
       contenuto di una pagina compare un riquadro da copiare (o un'altra
       copia) prima del «Ctrl+V».
2. (b) Cosa bloccante non in cima (#137): firma, scadenza, 14:05, uscita,
       PC rotto, non compila presenti ma non nelle prime 2 righe.
3. (c) «Fatto», «a posto», «funziona», «risolto» detti senza prova nello
       stesso messaggio (#63, #115, #128, #135).
4. (d) «pubblicat…», «è tutto pronto», «tutto a posto», «è online», «possono
       cominciare» riferiti a una classe senza la verifica sulla fonte vera:
       nel riservato serve dati/verifiche-lezione/<oggi>_<CLASSE>.json,
       VERDE e non più vecchio di 15 minuti (generatori/verifica_lezione.py;
       #63 #83 #104 #105 #115 #120 #127 #128 #135).
Contro i cicli: se stop_hook_active è true non blocca di nuovo.
Robusto: per qualunque errore interno esce 0 senza output.
"""
import datetime
import json
import os
import re
import sys
from zoneinfo import ZoneInfo

# ---------------------------------------------------------------- utilità

RE_RECINTO = re.compile(r"^\s*(```|~~~)")


def segmenta(testo):
    """Divide il messaggio in segmenti ('testo', righe) e ('riquadro', righe)."""
    segmenti = []
    corrente, tipo, chiusura = [], "testo", None
    for riga in testo.splitlines():
        m = RE_RECINTO.match(riga)
        if tipo == "testo" and m:
            if corrente:
                segmenti.append(("testo", corrente))
            corrente, tipo, chiusura = [], "riquadro", m.group(1)
            continue
        if tipo == "riquadro" and riga.strip().startswith(chiusura):
            segmenti.append(("riquadro", corrente))
            corrente, tipo = [], "testo"
            continue
        corrente.append(riga)
    if corrente:
        segmenti.append((tipo, corrente))
    return segmenti


def senza_riquadri(testo):
    return "\n".join("\n".join(r) for t, r in segmenta(testo) if t == "testo")


def senza_codice_in_linea(testo):
    return re.sub(r"`[^`\n]*`", " ", testo)


def senza_citazioni(testo):
    """Toglie le parole tra virgolette («fatto», "funziona"): sono citate, non dette."""
    testo = re.sub(r"«[^»\n]{0,200}»", " ", testo)
    testo = re.sub(r"“[^”\n]{0,200}”", " ", testo)
    testo = re.sub(r"\"[^\"\n]{0,200}\"", " ", testo)
    return testo


# ------------------------------------------------- (a) ordine copia/incolla

RE_COPIA_PAGINA = re.compile(
    r"ctrl\s*\+\s*c\b|\bcopia\s+(?:tutto|tutta|tutti|l['’]intero|l['’]intera)\b",
    re.I)
RE_INCOLLA_ESPLICITO = re.compile(r"ctrl\s*\+\s*v\b", re.I)
RE_INCOLLA_PAROLA = re.compile(r"\bincoll\w*", re.I)


def controllo_copia_incolla(testo):
    segmenti = segmenta(testo)
    # righe di testo che introducono un riquadro: l'ultima riga non vuota
    # prima di un riquadro parla di QUEL riquadro («incolla questo:»)
    eventi = []  # (tipo, riga)
    for i, (tipo, righe) in enumerate(segmenti):
        if tipo == "riquadro":
            eventi.append(("RIQUADRO", (righe[0] if righe else "").strip()[:80]))
            continue
        prossimo_riquadro = i + 1 < len(segmenti) and segmenti[i + 1][0] == "riquadro"
        idx_intro = None
        if prossimo_riquadro:
            for j in range(len(righe) - 1, -1, -1):
                if righe[j].strip():
                    idx_intro = j
                    break
        for j, riga in enumerate(righe):
            pulita = senza_codice_in_linea(riga)
            trovati = []
            for m in RE_COPIA_PAGINA.finditer(pulita):
                trovati.append((m.start(), "COPIA"))
            for m in RE_INCOLLA_ESPLICITO.finditer(pulita):
                trovati.append((m.start(), "INCOLLA"))
            if j != idx_intro:
                for m in RE_INCOLLA_PAROLA.finditer(pulita):
                    trovati.append((m.start(), "INCOLLA"))
            trovati.sort()
            ultimo = None
            for _, t in trovati:
                if t == ultimo:
                    continue  # «copia tutto (Ctrl+A e Ctrl+C)» = una copia sola
                eventi.append((t, riga.strip()[:120]))
                ultimo = t

    in_attesa = None  # riga della copia non ancora incollata
    for tipo, riga in eventi:
        if tipo == "COPIA":
            if in_attesa is not None:
                return ("Ordine copia/incolla sbagliato (#50, #138): dopo «%s» chiedi una "
                        "seconda copia («%s») prima del Ctrl+V: la seconda copia cancella "
                        "la prima dagli appunti." % (in_attesa, riga))
            in_attesa = riga
        elif tipo == "INCOLLA":
            in_attesa = None
        elif tipo == "RIQUADRO" and in_attesa is not None:
            return ("Ordine copia/incolla sbagliato (#50, #138): dopo «%s» c'è un riquadro "
                    "da copiare prima del Ctrl+V; copiare il riquadro cancella dagli appunti "
                    "il testo copiato dalla pagina. Riscrivi i passi in quest'ordine: "
                    "1) apri la pagina dove si incolla e incolla lì gli indirizzi o i "
                    "riquadri che servono; 2) apri la pagina da copiare e premi Ctrl+A e "
                    "Ctrl+C; 3) torna sulla prima pagina e premi Ctrl+V. Nessun riquadro "
                    "tra il Ctrl+C e il Ctrl+V." % in_attesa)
    return None


# --------------------------------------------- (b) bloccante in prima riga

PAROLE_BLOCCANTI = [
    ("firma", re.compile(r"\bfirm(?:a|are|ate|arle|ala)\b|non\s+firmat\w*", re.I)),
    ("scadenza", re.compile(r"scadenz\w*", re.I)),
    ("14:05", re.compile(r"14[:.]05")),
    ("uscita", re.compile(r"\buscit\w*", re.I)),
    ("PC rotto", re.compile(r"\bPC\s+rott\w*", re.I)),
    ("non compila", re.compile(r"non\s+compila", re.I)),
]


def controllo_bloccanti(testo):
    righe = [r for r in senza_citazioni(senza_riquadri(testo)).splitlines() if r.strip()]
    if not righe:
        return None
    cima = "\n".join(righe[:2])
    resto = "\n".join(righe[2:])
    mancanti = []
    for nome, rx in PAROLE_BLOCCANTI:
        m = rx.search(resto)
        if m and not rx.search(cima):
            riga = next((r for r in righe[2:] if rx.search(r)), "")
            mancanti.append("«%s» (riga: «%s»)" % (nome, riga.strip()[:100]))
    if not mancanti:
        return None
    return ("Cosa bloccante non in cima (#137): nel messaggio c'è %s ma non nelle prime 2 "
            "righe. Riscrivi il messaggio mettendo la cosa bloccante da sola nella PRIMA "
            "riga, prima di tutto il resto (es. «FIRMA: ...», «USCITA: ...»); se non è "
            "bloccante, togli la parola o spostala in cima." % "; ".join(mancanti))


# ------------------------------------------------- (c) «fatto» senza prova

RE_AFFERMAZIONI = [
    re.compile(r"\b(?:è|e'|é)\s+(?:tutto\s+)?a\s+posto\b", re.I),
    re.compile(r"\btutto\s+a\s+posto\b", re.I),
    re.compile(r"(?<!come )(?<!non )(?<!se )\bfunzion(?:a|ano)\b(?=\s*(?:ora|adesso|già|di nuovo|bene|tutto)?\s*(?:[.!]|$))", re.I | re.M),
    re.compile(r"\b(?:ora|adesso|già|tutto)\s+funzion(?:a|ano)\b", re.I),
    re.compile(r"\bho\s+(?:già\s+)?risolto\b", re.I),
    re.compile(r"(?:^|[.!?]\s+)\W{0,4}risolt[oaie]\b", re.I | re.M),
    re.compile(r"(?<!non )(?<!da )\brisolt[oaie]\s*(?:[.!]|$)", re.I | re.M),
    re.compile(r"(?:^|[.!?]\s+)\W{0,4}fatt[oaie]\b\s*(?:[.!:,]|$)", re.I | re.M),
    re.compile(r"\b(?:è|sono)\s+(?:già\s+)?(?:stat[oaie]\s+)?fatt[oaie]\b(?!\s+(?:da|di|in|con|per|così|come))", re.I),
    re.compile(r"\btutto\s+fatto\b|\bfatto\s+tutto\b", re.I),
]

RE_PROVE = re.compile(
    r"ho\s+visto|\bvist[oa]\s+(?:che|lo|la|il)\b|\brisult[ae]\b|\brisultano\b|PUBBLICATO|"
    r"PUBLISHED|schermat\w*|controllat\w*|verificat\w*|ho\s+provato|ho\s+controllato|"
    r"ho\s+verificato|\bprov[ae]\b",
    re.I)


def controllo_fatto_senza_prova(testo):
    base = senza_citazioni(senza_codice_in_linea(senza_riquadri(testo)))
    trovate = []
    for rx in RE_AFFERMAZIONI:
        for m in rx.finditer(base):
            trovate.append(m.group(0).strip(" .!:,\n"))
    if not trovate:
        return None
    if RE_PROVE.search(testo):  # la prova può stare anche in un riquadro
        return None
    return ("Affermazione senza prova (#63, #115, #128, #135): hai scritto «%s» ma nel "
            "messaggio non c'è la prova. Riscrivi dicendo che cosa hai visto o controllato "
            "(es. «ho visto PUBBLICATO», «Classroom risulta PUBLISHED», «compilato con F9 "
            "senza errori», «ho controllato nel repository»); se non l'hai verificato, "
            "togli «%s» e scrivi che cosa manca da verificare."
            % (trovate[0], trovate[0]))


# ------------------------------- (d) «pubblicato» senza verifica_lezione.py

RIS = "/home/user/corso-informatica-riservato"
RE_PRONTO = re.compile(
    r"pubblicat\w*|(?:è|e')\s+tutto\s+pronto|tutto\s+a\s+posto|(?:è|sono)\s+online|"
    r"possono\s+(?:cominciare|iniziare)", re.I)
RE_NEGAZIONE = re.compile(r"\b(?:non|ancora\s+da|da)\s+(?:\w+\s+){0,2}$", re.I)
RE_CLASSE = re.compile(r"\b([1-4])\s*(INF|INFO|TI)\b", re.I)


def classi_in(testo):
    out = []
    for m in RE_CLASSE.finditer(testo):
        c = m.group(1) + ("TI" if m.group(2).upper() == "TI" else "INF")
        if c not in out:
            out.append(c)
    return out


def stato_verifica(classe, oggi, adesso):
    """None se la verifica c'è, è VERDE e ha meno di 15 minuti; altrimenti il problema."""
    nomi = [classe] + (["4TI", "4INF"] if classe in ("4TI", "4INF") else [])
    for nome in nomi:
        f = os.path.join(RIS, "dati", "verifiche-lezione", "%s_%s.json" % (oggi, nome))
        if not os.path.exists(f):
            continue
        d = json.load(open(f, encoding="utf-8"))
        ora = datetime.datetime.fromisoformat(d["ora"])
        eta = (adesso - ora).total_seconds() / 60
        if eta > 15:
            return "la verifica della %s è di %d minuti fa (massimo 15)" % (classe, eta)
        if d.get("esito") != "VERDE":
            return "la verifica della %s non è VERDE: %s" % (classe, d.get("riga", d.get("esito")))
        return None
    return "manca dati/verifiche-lezione/%s_%s.json nel riservato" % (oggi, classe)


def controllo_pronto_senza_verifica(testo):
    if not os.path.isdir(RIS):
        return None
    base = senza_citazioni(senza_codice_in_linea(senza_riquadri(testo)))
    classi_messaggio = classi_in(base)
    if not classi_messaggio:
        return None
    da_verificare, frase = [], None
    for riga in base.splitlines():
        for m in RE_PRONTO.finditer(riga):
            if RE_NEGAZIONE.search(riga[max(0, m.start() - 25):m.start()]):
                continue
            frase = frase or m.group(0)
            for c in (classi_in(riga) or classi_messaggio):
                if c not in da_verificare:
                    da_verificare.append(c)
    if not da_verificare:
        return None
    adesso = datetime.datetime.now(ZoneInfo("Europe/Rome"))
    oggi = adesso.strftime("%Y-%m-%d")
    problemi = []
    for c in da_verificare:
        p = stato_verifica(c, oggi, adesso)
        if p:
            problemi.append(p)
    if not problemi:
        return None
    return ("Pubblicazione non verificata (#63 #83 #104 #105 #115 #120 #127 #128 #135): hai scritto "
            "«%s» per la %s, ma %s. Prima lancia (una riga per classe):\n"
            "python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py %s\n"
            "e scrivi «pubblicato» / «è tutto pronto» solo se stampa VERDE; con GIALLO o ROSSO "
            "riscrivi il messaggio dicendo che cosa manca."
            % (frase, ", ".join(da_verificare), "; ".join(problemi), da_verificare[0]))


# ------------------------------------------------------------- transcript

def ultimo_testo_assistente(transcript_path, max_righe=4000):
    try:
        with open(os.path.expanduser(transcript_path), "rb") as f:
            f.seek(0, os.SEEK_END)
            dim = f.tell()
            f.seek(max(0, dim - 8 * 1024 * 1024))
            righe = f.read().split(b"\n")[-max_righe:]
    except Exception:
        return ""
    for r in reversed(righe):
        try:
            d = json.loads(r)
        except Exception:
            continue
        if d.get("isSidechain") or d.get("type") != "assistant":
            continue
        parti = [x.get("text", "") for x in (d.get("message") or {}).get("content") or []
                 if isinstance(x, dict) and x.get("type") == "text"]
        testo = "\n".join(p for p in parti if p)
        if testo.strip():
            return testo
    return ""


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    if data.get("stop_hook_active"):
        return
    if data.get("agent_id"):
        return
    testo = data.get("last_assistant_message")
    if not isinstance(testo, str) or not testo.strip():
        testo = ultimo_testo_assistente(data.get("transcript_path") or "")
    if not testo.strip():
        return
    motivi = []
    for controllo in (controllo_bloccanti, controllo_copia_incolla, controllo_fatto_senza_prova,
                      controllo_pronto_senza_verifica):
        try:
            m = controllo(testo)
        except Exception:
            m = None
        if m:
            motivi.append(m)
    if motivi:
        reason = ("CONTROLLO AUTOMATICO DEL MESSAGGIO (hook controllo-messaggio.py): "
                  "riscrivi la risposta al docente correggendo questi punti.\n"
                  + "\n".join("%d. %s" % (i + 1, m) for i, m in enumerate(motivi)))
        sys.stdout.write(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
