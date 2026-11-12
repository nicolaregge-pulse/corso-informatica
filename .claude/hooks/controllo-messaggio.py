#!/usr/bin/env python3
"""Hook Stop: controlla l'ultimo messaggio di Claude prima che arrivi al docente.

Versione ridotta del 04/11/2026 (decisioni del docente su REGOLE-DA-DECIDERE.md): da 35
controlli ai controlli essenziali. Se ne trova uno, blocca la fine del turno con
{"decision": "block", "reason": ...}: Claude deve riscrivere il messaggio.
1. (a) Ordine copia/incolla sbagliato (#50, #138): dopo un «Ctrl+C» del contenuto di una
       pagina compare un riquadro da copiare (o un'altra copia) prima del «Ctrl+V». (R4)
2. (b) Cosa bloccante non in prima riga (#137): firma, scadenza, 14:05, uscita, PC rotto,
       non compila, PUBB n non riuscito, fuori dalle prime 2 righe. Il promemoria della firma
       non vale se FIRME-REGISTRO dice che oggi è tutto firmato (ex controllo m). (R4, R5)
3. (d) «pubblicat…», «è tutto pronto», «è online», «possono cominciare» riferiti a una classe
       senza dati/verifiche-lezione/<oggi>_<CLASSE>.json VERDE e di meno di 15 minuti. (R2, R7)
4. (e) Link al sito senza «PUBBLICATO» delle ultime modifiche di docs/ (#79); link al
       riservato senza la finestra PERSONALE, script copiato dal riservato (ex o, #48). (R7)
5. (gg) Il docente ha nominato un'ora della giornata («prima ora», «3ª ora», «PUBB 2») e la
       risposta non scrive l'orario (8-9…) (#159). Vale SOLO se il docente ha davvero parlato
       di un'ora: le cifre senza «ª» («tra 1 ora») e i quiz di Sicurezza non contano. (R2)
6. (ff) Formato dei kit e dei documenti (12/11/2026, chiude la famiglia #282, #285-#289, #293,
       #309, #311): legge l'ultimo turno dell'assistente dalla trascrizione (blocchi text e
       tool_use in ordine, dall'ultimo messaggio del docente) e controlla R-A cornice blu intorno
       a ogni SendUserFile di documento, R-B un solo PDF per risposta con i kit, R-C kit in turno
       pulito, R-D kit Classroom (rosso, TITOLO e OGGETTO in riquadri, chiusura rossa), R-E frase
       vietata nell'oggetto, R-F cornice verde nei messaggi che non sono kit. (GUIDA-MESSAGGI 03octies)
Controlli tolti il 04/11/2026 (elenco completo in LEGGIMI-controlli.md, capitolo 05):
c, f, g, h, i, j, k, l, n, p, q, r, s, t, u, v, w, x, y, z, aa, bb, cc, dd, ee, ff, hh, ii.
Il controllo dei nomi degli allievi NON sta qui (in chat COGNOME Nome è richiesto, R7): sta
in limite-comandi.py + controllo_nomi.py, sui commit e sui push del repository pubblico (R1).
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
    ("PUBB non riuscito", re.compile(r"PUBB\s*[1-6]?\s+NON\s+riuscit\w*", re.I)),
]


def controllo_bloccanti(testo):
    righe = [r for r in senza_citazioni(senza_riquadri(testo)).splitlines() if r.strip()]
    if not righe:
        return None
    cima = "\n".join(righe[:2])
    resto = "\n".join(righe[2:])
    mancanti = []
    firmato = ore_di_oggi_tutte_firmate(datetime.datetime.now(TZ_ROMA))
    for nome, rx in PAROLE_BLOCCANTI:
        if nome == "firma" and firmato:
            continue  # ore di oggi tutte firmate: la firma non è più bloccante (ex controllo m)
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


PUB = "/home/user/corso-informatica"
TZ_ROMA = ZoneInfo("Europe/Rome")


def _git(*arg):
    import subprocess
    r = subprocess.run(["git", "-C", PUB] + list(arg), capture_output=True, text=True, timeout=5)
    return r.returncode, r.stdout.strip()


# (e) link al sito (assorbe il vecchio controllo o, link al riservato)
# (e) link al sito senza «PUBBLICATO» (#79, #78)
RE_LINK_SITO = re.compile(r"nicolaregge-pulse\.github\.io/corso-informatica", re.I)


def controllo_link_senza_pubblicato(testo):
    if not RE_LINK_SITO.search(testo) or not os.path.isdir(PUB):
        return None
    consiglio = ("Prima: bash /home/user/corso-informatica/strumenti/aspetta_pubblicazione.sh (dalla "
                 "cartella del pubblico) e il link solo dopo «PUBBLICATO» (#79).")
    rc, sporchi = _git("status", "--porcelain", "--", "docs")
    if rc == 0 and sporchi:
        return "Link al sito con pagine di docs/ non ancora committate e pushate (#79). " + consiglio
    rc, avanti = _git("diff", "--name-only", "origin/main", "HEAD", "--", "docs")
    if rc == 0 and avanti:
        return "Link al sito con pagine di docs/ non ancora pushate (#79). " + consiglio
    rc, ultimo = _git("log", "-1", "--format=%ct", "--", "docs")
    if rc != 0 or not ultimo:
        return None
    if datetime.datetime.now().timestamp() - int(ultimo) > 2 * 3600:
        return None  # nessuna modifica alle pagine nelle ultime 2 ore
    rc, cartella_git = _git("rev-parse", "--absolute-git-dir")
    timbro = os.path.join(cartella_git, "ultimo-pubblicato") if rc == 0 else ""
    sha = open(timbro).read().strip() if timbro and os.path.exists(timbro) else ""
    if sha:
        rc, dopo = _git("diff", "--name-only", sha, "HEAD", "--", "docs")
        if rc == 0 and not dopo:
            return None
    return ("Link al sito dato senza «PUBBLICATO» per le ultime modifiche alle pagine (#79): il docente "
            "vedrebbe la versione vecchia. " + consiglio)


# (o) link al riservato senza profilo personale; script dal riservato (#48; 07/10 n. 29)
RE_LINK_RISERVATO = re.compile(r"github\.com/nicolaregge-pulse/corso-informatica-riservato\S*", re.I)


def controllo_link_riservato(testo):
    m = RE_LINK_RISERVATO.search(testo)
    if not m:
        return None
    if "automazione-corso.gs" in m.group(0):
        return ("Script da copiare dal repository riservato (#48): nella finestra PIAMARTA dà 404. Si "
                "copia dal link pubblico https://raw.githubusercontent.com/nicolaregge-pulse/"
                "corso-informatica/main/strumenti/automazione-corso.gs (regola 10).")
    if not re.search(r"personale", testo, re.I):
        return ("Link al repository riservato senza il passo «apri la finestra Chrome dell'account "
                "PERSONALE» prima (07/10 n. 29, #48): nella finestra PIAMARTA dà 404.")
    return None


# (m) firma ricordata per ore già firmate (#36, #52, #87, #96; 05/10 n. 11)
RE_RICORDA_FIRMA = re.compile(
    r"(?:ricorda(?:ti)?\s+(?:di\s+)?|devi\s+|vanno\s+|va\s+)firm\w*|firma\s+(?:le|l['’]|la)\s*or|"
    r"non\s+(?:risulta|risultano|sono|è)\s+(?:ancora\s+)?firmat\w*|firmare\s+entro|(?<!niente )da\s+firmare",
    re.I)


def ore_di_oggi_tutte_firmate(adesso):
    f = os.path.join(PUB, "FIRME-REGISTRO-2026-27.md")
    if not os.path.exists(f):
        return False
    data = adesso.strftime("%d/%m/%Y")
    righe, dentro = [], False
    for r in open(f, encoding="utf-8"):
        if r.startswith("## "):
            dentro = data in r
            continue
        if dentro and re.search(r"\bor[ae]\b", r, re.I):
            righe.append(r)
    if not righe:
        return False
    return all(re.search(r"firmat", r, re.I) and not re.search(r"non\s+firmat|da\s+firmare|manca", r, re.I)
               for r in righe)


def ultimo_messaggio_docente(transcript_path, max_byte=8 * 1024 * 1024):
    try:
        with open(os.path.expanduser(transcript_path), "rb") as f:
            f.seek(0, os.SEEK_END)
            dim = f.tell()
            f.seek(max(0, dim - max_byte))
            righe = f.read().split(b"\n")
    except Exception:
        return ""
    for r in reversed(righe):
        try:
            d = json.loads(r)
        except Exception:
            continue
        if d.get("type") != "user" or d.get("isSidechain") or d.get("isMeta"):
            continue
        c = (d.get("message") or {}).get("content")
        if isinstance(c, str):
            return c
        if isinstance(c, list):
            testi = [x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text"]
            if testi:
                return "\n".join(testi)
    return ""


# (gg) «prima ora» del docente: si dice l'orario (#159)
# 04/11/2026: solo ordinali veri («prima ora», «3ª ora») e il comando «PUBB n»; «tra 1 ora» non conta.
RE_ORA_ORDINALE = re.compile(r"\b(?:prima|seconda|terza|quarta|quinta|sesta)\s+ora\b|\b[1-6]\s*[ª°]\s*ora\b|"
                             r"\b[1-6]a\s+ora\b|^\s*PUBB\s+[1-6]\b", re.I | re.M)
RE_ORARIO = re.compile(r"\b(?:[01]?\d|2[0-3])(?::\d{2})?\s*[-–]\s*(?:[01]?\d|2[0-3])(?::\d{2})?\b|\bdalle\s+\d{1,2}\b|\balle\s+\d{1,2}\b")


def controllo_ora_ordinale(testo, data):
    richiesta = ultimo_messaggio_docente(data.get("transcript_path") or "")
    m = RE_ORA_ORDINALE.search(richiesta or "")
    if not m or re.search(r"sicurezza|quiz\s+della|[1-5]ª\s+ora\s+di\s+sicurezza", richiesta, re.I):
        return None
    if RE_ORARIO.search(senza_riquadri(testo)):
        return None
    return ("Il docente ha detto «%s» (#159): «prima ora» è l'ora della GIORNATA. Nella risposta si scrive l'orario "
            "(per esempio «8-9») così l'equivoco si vede subito; nel dubbio si fa in entrambe." % m.group(0))



# ------------------------------------- (ff) formato kit e documenti (12/11/2026)
# Chiude la famiglia di errori sul formato: #282, #285-#289, #293, #309, #311 (GUIDA-MESSAGGI 03sexies-03octies).
# Il controllo vede solo i blocchi (text, tool_use) della trascrizione, NON come l'app li mostra.
import hashlib
import tempfile

STATO_FORMATO = os.environ.get("CORSO_STATO_FORMATO",
                               os.path.join(tempfile.gettempdir(), "corso-controllo-formato-stato.json"))  # "" = nessuna memoria
EST_DOCUMENTO = (".pdf", ".docx", ".xlsx", ".csv", ".zip")


def _riga_di(simbolo, riga):
    return re.match(r"^\s*(?:%s\s*){3,}$" % simbolo, riga) is not None


def _righe(testo):
    return [r for r in testo.splitlines() if r.strip()]


def e_kit(testo):
    """Testo di un kit: righe rosse 🟥🟥 e TITOLO, OGGETTO o un link in un riquadro."""
    if "🟥🟥" not in testo:
        return False
    if re.search(r"\bTITOLO\b|\bOGGETTO\b", testo):
        return True
    return any(t == "riquadro" and any(re.search(r"https?://", r) for r in righe)
               for t, righe in segmenta(testo))


def e_kit_classroom(testo):
    """Kit Classroom: TITOLO e OGGETTO (maiuscoli) con righe rosse o almeno due riquadri."""
    if not (re.search(r"\bTITOLO\b", testo) and re.search(r"\bOGGETTO\b", testo)):
        return False
    return "🟥🟥" in testo or sum(1 for t, _ in segmenta(testo) if t == "riquadro") >= 2


def etichetta_in_riquadro(testo, etichetta):
    righe = testo.splitlines()
    dentro, chiusura = False, None
    for i, r in enumerate(righe):
        m = RE_RECINTO.match(r)
        if not dentro and m:
            dentro, chiusura = True, m.group(1)
            continue
        if dentro and r.strip().startswith(chiusura):
            dentro = False
            continue
        if re.search(r"\b%s\b" % etichetta, r):
            if dentro:
                return True
            for s in righe[i + 1:]:
                if s.strip():
                    if RE_RECINTO.match(s):
                        return True
                    break
    return False


def file_del_comando(inp):
    """Percorsi passati a SendUserFile (file_path, files: elenco di stringhe o di oggetti)."""
    if not isinstance(inp, dict):
        return []
    out = []
    for k in ("file_path", "path"):
        if isinstance(inp.get(k), str):
            out.append(inp[k])
    f = inp.get("files")
    if isinstance(f, str):
        out.append(f)
    elif isinstance(f, list):
        for x in f:
            if isinstance(x, str):
                out.append(x)
            elif isinstance(x, dict):
                v = x.get("path") or x.get("file_path")
                if isinstance(v, str):
                    out.append(v)
    return out


def documenti_del_comando(inp):
    return [f for f in file_del_comando(inp) if f.lower().endswith(EST_DOCUMENTO)]


def _tail_righe(path, n):
    with open(os.path.expanduser(path), "rb") as f:
        f.seek(0, os.SEEK_END)
        dim = f.tell()
        f.seek(max(0, dim - n))
        righe = f.read().split(b"\n")
    return righe[1:] if dim > n else righe  # la prima riga può essere tagliata


def e_messaggio_docente(d):
    """True per un messaggio vero del docente (non risultato di strumento, notifica, feedback di hook)."""
    if d.get("type") != "user" or d.get("isSidechain") or d.get("isMeta"):
        return False
    c = (d.get("message") or {}).get("content")
    if isinstance(c, str):
        testo = c
    elif isinstance(c, list):
        if any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
            return False
        testo = "\n".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
    else:
        return False
    origine = d.get("origin")
    genere = origine.get("kind") if isinstance(origine, dict) else None
    if genere:
        return genere == "human"
    t = testo.lstrip()
    return bool(t) and not t.startswith(("Stop hook feedback", "<task-notification", "<system-reminder",
                                         "<command-", "[Image:"))


def eventi_ultimo_turno(transcript_path):
    """([eventi], chiave_turno): i blocchi dell'assistente dall'ultimo messaggio del docente, in ordine.
    Evento = ('text', testo, chiave) oppure ('tool', nome, input, id). Mai un errore: in caso di problemi ([], '')."""
    if not transcript_path:
        return [], ""
    try:
        for n in (1024 * 1024, 8 * 1024 * 1024):
            eventi, chiave, trovato = [], "", False
            for r in reversed(_tail_righe(transcript_path, n)):
                try:
                    d = json.loads(r)
                except Exception:
                    continue
                if d.get("isSidechain"):
                    continue
                if d.get("type") == "assistant":
                    blocchi = (d.get("message") or {}).get("content") or []
                    if isinstance(blocchi, list):
                        for j in range(len(blocchi) - 1, -1, -1):
                            x = blocchi[j]
                            if not isinstance(x, dict):
                                continue
                            if x.get("type") == "text" and (x.get("text") or "").strip():
                                eventi.append(("text", x["text"], "%s/%d" % (d.get("uuid", len(eventi)), j)))
                            elif x.get("type") == "tool_use":
                                eventi.append(("tool", x.get("name", ""), x.get("input") or {},
                                               x.get("id") or "%s/%d" % (d.get("uuid", len(eventi)), j)))
                elif e_messaggio_docente(d):
                    c = (d.get("message") or {}).get("content")
                    testo = c if isinstance(c, str) else json.dumps(c, ensure_ascii=False)[:500]
                    chiave = str(d.get("uuid") or hashlib.sha1(testo.encode("utf-8")).hexdigest()[:12])
                    trovato = True
                    break
            if trovato:
                break
        eventi.reverse()
        return eventi, chiave
    except Exception:
        return [], ""


def _allinea_finale(eventi, finale):
    """Il messaggio finale (last_assistant_message) può non essere ancora scritto nella trascrizione."""
    eventi = list(eventi)
    if finale.strip() and not (eventi and eventi[-1][0] == "text" and eventi[-1][1].strip() == finale.strip()):
        eventi.append(("text", finale, "finale"))
    return eventi


def _h(testo):
    return hashlib.sha1(testo.encode("utf-8")).hexdigest()[:10]


def analizza_formato(eventi, finale):
    """Lista di (codice, chiave, messaggio) per l'ultimo turno. Regole R-A..R-F (GUIDA-MESSAGGI 03octies)."""
    ev = _allinea_finale(eventi, finale)
    testi = [e for e in ev if e[0] == "text"]
    errori = []

    # R-A: ogni documento ha la cornice blu (testo con 🟦 e 📄 prima, testo con 🟦 dopo) (#309, #285)
    for i, e in enumerate(ev):
        if e[0] != "tool" or e[1] != "SendUserFile":
            continue
        docs = documenti_del_comando(e[2])
        if not docs:
            continue  # immagini e altri file: fuori dalla regola
        prima = ev[i - 1] if i > 0 else None
        dopo = ev[i + 1] if i + 1 < len(ev) else None
        mancano = []
        if prima is None or prima[0] != "text":
            mancano.append("subito prima del file non c'è un testo (c'è uno strumento o niente)")
        else:
            r = _righe(prima[1])
            if not (len(r) >= 2 and _riga_di("🟦", r[-2]) and re.match(r"^[\s*_>#\-]*📄", r[-1])):
                mancano.append("il testo prima del file non finisce con una riga di quadratini blu 🟦 seguita da una riga "
                               "che comincia con 📄")
        if dopo is None or dopo[0] != "text":
            mancano.append("subito dopo il file non c'è un testo (c'è uno strumento o niente)")
        else:
            r = _righe(dopo[1])
            if not (r and _riga_di("🟦", r[0])):
                mancano.append("il testo dopo il file non comincia con una riga di quadratini blu 🟦")
        if mancano:
            errori.append(("A", e[3], "Documento senza cornice blu (#309, #285): per «%s» %s. Formato: testo che FINISCE "
                           "con una riga 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 e una riga «📄 NOME DEL DOCUMENTO ⬇️»; subito dopo "
                           "SendUserFile (stesso file, nessun altro strumento in mezzo); subito dopo un testo che COMINCIA con "
                           "una riga 🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦. Rimanda il file così, mai una scheda da sola."
                           % (os.path.basename(docs[0]), "; ".join(mancano))))

    # R-B: un solo PDF per risposta quando ci sono i kit rossi (#311)
    n_pdf = sum(1 for e in ev if e[0] == "tool" and e[1] == "SendUserFile"
                for f in file_del_comando(e[2]) if f.lower().endswith(".pdf"))
    if n_pdf >= 2 and any("🟥🟥" in t[1] for t in testi):
        errori.append(("B", "turno", "Due kit/due PDF nella stessa risposta (il testo sparisce) (#311): nel turno ci sono %d "
                       "PDF mandati con SendUserFile e righe rosse 🟥🟥: l'app sostituisce con un riassunto il testo scritto "
                       "prima di ogni scheda e il kit non si vede. Un solo kit e un solo PDF per risposta: manda ora il "
                       "primo kit nel formato giusto e il secondo nel messaggio dopo." % n_pdf))

    # R-C: il kit si consegna in un turno pulito (#293)
    for i, e in enumerate(ev):
        if e[0] == "text" and e_kit(e[1]):
            sporchi = []
            for x in ev[:i]:
                if x[0] == "tool" and x[1] != "SendUserFile" and x[1] not in sporchi:
                    sporchi.append(x[1])
            if sporchi:
                errori.append(("C", "turno", "Kit in turno sporco (#293, GUIDA-MESSAGGI 03octies «turno pulito»): prima del "
                               "kit, in questo turno, ci sono stati strumenti (%s) e l'app non mostra il testo del kit. "
                               "NON mandare il kit adesso e NON usare le cornici colorate: rispondi in testo semplice, una "
                               "riga, dicendo che il kit arriva nel prossimo messaggio; nel turno pulito successivo "
                               "consegnalo senza nessuno strumento prima (comandi, controlli, agenti si fanno prima)."
                               % ", ".join(sporchi[:6])))
            break

    # R-D: kit Classroom nello standard 03sexies (#287-#289)
    for i, e in enumerate(ev):
        if e[0] == "text" and e_kit_classroom(e[1]):
            k = _h(e[1])
            r = _righe(e[1])
            if not (r and _riga_di("🟥", r[0])):
                errori.append(("D1", k, "Kit Classroom senza cornice rossa in testa (#289): il primo blocco deve cominciare "
                               "con una riga di quadratini rossi 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥, poi TITOLO e OGGETTO."))
            if not (etichetta_in_riquadro(e[1], "TITOLO") and etichetta_in_riquadro(e[1], "OGGETTO")):
                errori.append(("D2", k, "Kit Classroom con TITOLO e OGGETTO fuori dai riquadri (#282, #289): ognuno va in un "
                               "riquadro di codice (tre apici ```) da copiare, uno per valore, subito dopo la sua etichetta."))
            ultimo = testi[-1][1]
            rf = _righe(ultimo)
            if not (rf and _riga_di("🟥", rf[-1])):
                errori.append(("D3", k, "Kit Classroom con testo dopo la riga rossa finale, o senza (#288, #289, #293): l'ultimo "
                               "testo del kit (quello dopo il PDF) deve avere come ULTIMA cosa una riga di quadratini rossi "
                               "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥; niente registro, quiz o «Non provato» dopo (solo righe vuote)."))
            break

    # R-E: frase vietata nell'oggetto (#289, 03octies)
    for t in testi:
        if (e_kit(t[1]) or e_kit_classroom(t[1])) and re.search(r"lo\s+facciamo\s+quando\s+lo\s+dico\s+io", t[1], re.I):
            errori.append(("E", _h(t[1]), "Frase vietata nell'oggetto (03octies): togli «lo facciamo quando lo dico io». Al "
                           "massimo «Seguirà il quiz.», oppure niente."))
            break

    # R-F: ogni messaggio che non è un kit ha la cornice verde (#291)
    e_un_kit = any(e_kit(t[1]) or e_kit_classroom(t[1]) for t in testi)
    f = finale.strip()
    rf = _righe(f)
    if (not e_un_kit and len(f) >= 60 and len(rf) >= 2 and not f.startswith(("🔴", "🟥", "🟦"))
            and "🟩🟩🟩" not in f):
        errori.append(("F", _h(f), "Messaggio senza cornice verde (#291): ogni messaggio per il docente che non è un kit "
                       "sta in una cornice verde, con una riga di quadratini verdi 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 sopra e "
                       "una sotto (la prima riga resta la cosa bloccante, R4). Eccezioni: risposte che cominciano con 🔴 o "
                       "con una riga 🟥/🟦, e risposte brevi (sotto i 60 caratteri)."))
    return errori


def _nuovi_errori(chiave_turno, errori):
    """Toglie gli errori già segnalati in questo turno (un SendUserFile vecchio non fa bloccare per sempre)."""
    if not STATO_FORMATO or not chiave_turno:
        return errori
    try:
        try:
            stato = json.load(open(STATO_FORMATO, encoding="utf-8"))
        except Exception:
            stato = {}
        visti = set(stato.get(chiave_turno, []))
        nuovi = [e for e in errori if "%s|%s" % (e[0], e[1]) not in visti]
        if nuovi:
            stato[chiave_turno] = sorted(visti | {"%s|%s" % (e[0], e[1]) for e in nuovi})
            for k in list(stato)[:-30]:
                del stato[k]
            json.dump(stato, open(STATO_FORMATO, "w", encoding="utf-8"))
        return nuovi
    except Exception:
        return errori


def controllo_formato(testo, data):
    if "last_assistant_message" in data and not (data.get("last_assistant_message") or "").strip():
        return None  # turno senza testo per il docente (per esempio notifica di un agente): niente da controllare
    eventi, chiave = eventi_ultimo_turno(data.get("transcript_path") or "")
    errori = _nuovi_errori(chiave, analizza_formato(eventi, testo))
    if not errori:
        return None
    return ("Formato dei kit e dei documenti sbagliato (GUIDA-MESSAGGI 03sexies-03octies; famiglia #282, #285-#289, #293, "
            "#309, #311). Tu non vedi come l'app mostra la risposta: segui questo schema.\n"
            + "\n".join("   - [%s] %s" % (e[0], e[2]) for e in errori))


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


def controllo_link(testo):
    return controllo_link_senza_pubblicato(testo) or controllo_link_riservato(testo)


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
    for controllo in (controllo_bloccanti, controllo_copia_incolla, controllo_pronto_senza_verifica,
                      controllo_link, lambda t: controllo_ora_ordinale(t, data),
                      lambda t: controllo_formato(t, data)):
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
