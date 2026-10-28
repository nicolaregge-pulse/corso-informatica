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
Aggiunti il 28/10/2026 sera (MAPPA-REGOLE-CONTROLLI.md):
5. (e) link al sito senza «PUBBLICATO» delle ultime modifiche di docs/ (#79, #78);
6. (f) tempi promessi per ciò che fa lo script, senza piano B (#129, #130);
7. (g) stringa dei voti DIDAweb senza «Disciplina» (#98, #117);
8. (h) «nessuna AI» senza aver visto tutte le finestre (#90);
9. (i) «utente non indicato» invece di chiedere chi c'è (#100);
10. (j) «onestamente», «sinceramente»… (#53);
11. (k) passi come catene di coordinate con « · » (#56);
12. (l) istruzioni con «salta al passo» / «se la scheda è già aperta» (#55);
13. (m) firma ricordata quando FIRME-REGISTRO dice che oggi è tutto firmato (#36 #52 #87 #96);
14. (n) il docente chiede di registrare un errore e il messaggio non ha il numero #NNN (#113);
15. (o) link al riservato senza «personale»; script copiato dal riservato (#48; 07/10 n. 29);
16. (p) indirizzo diretto del progetto Apps Script (regola 10, #51);
17. (q) più di 30 righe di testo nelle ore di lezione (05/10 n. 6, #132);
18. (r) «non ha consegnato», «non risulta» senza dire dove si è controllato (#83 #95);
19. (s) «ha copiato» detto come certo (01/10 n. 6);
20. (t) «al tuo avanti» quando il docente ha chiesto «dammi/fammi» (05/10 n. 21);
21. (u) rimando a riquadri di messaggi precedenti (05/10 n. 31);
22. (v) «incolla» in Apps Script senza il file automazione-corso.gs (#51);
e in (g) anche i voti sotto 40 nella stringa DIDAweb (05/10 n. 23).
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


# ------------------------------------------- controlli aggiunti il 28/10/2026 sera
# (MAPPA-REGOLE-CONTROLLI.md: voci del registro che erano scoperte)

PUB = "/home/user/corso-informatica"
TZ_ROMA = ZoneInfo("Europe/Rome")


def _git(*arg):
    import subprocess
    r = subprocess.run(["git", "-C", PUB] + list(arg), capture_output=True, text=True, timeout=5)
    return r.returncode, r.stdout.strip()


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


# (f) tempi promessi che dipendono dallo script (#129, #130)
RE_PROMESSA = re.compile(
    r"entro\s+(?:pochi|qualche|un\s+paio\s+di|\d+)\s+minut\w*|"
    r"dovrebbe(?:ro)?\s+(?:arrivare|uscire|comparire|partire|essere\s+pubblicat\w*)|"
    r"arriv\w*\s+(?:tra|fra)\s+poco|(?:tra|fra)\s+(?:pochi|qualche)\s+minuti\s+(?:arriv|esc|compar)\w*", re.I)


RE_DIPENDE_DA_SCRIPT = re.compile(r"\bscript\b|\bponte\b|\bgiro\b|\bcoda\b|\btimer\b", re.I)
RE_COSE_ATTESE = re.compile(r"pubblic\w*|classroom|\bquiz\b|compit\w*|annunc\w*|modul\w*", re.I)


def controllo_promessa_tempi(testo):
    """Solo quando la promessa riguarda una cosa che il docente aspetta e che fa lo script."""
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_PROMESSA.search(base)
    if not m or re.search(r"piano\s+B", testo, re.I):
        return None
    if not (RE_DIPENDE_DA_SCRIPT.search(base) and RE_COSE_ATTESE.search(base)):
        return None
    return ("Tempo promesso senza piano B (#129, #130): «%s». Non si promettono tempi per ciò che fa lo "
            "script: dai la strada che il docente può fare subito (piano B: docs/prof-pubblica/ o il "
            "testo dell'annuncio da copiare) e scrivi che intanto controlli lo script." % m.group(0))


# (g) stringa dei voti per DIDAweb senza la Disciplina (#98, #117)
RE_STRINGA_VOTI = re.compile(r"\b\d{2}/\d{2}/\d{4}\s+h\s*\d")


def controllo_voti_senza_disciplina(testo):
    for riga in testo.splitlines():
        if RE_STRINGA_VOTI.search(riga):
            bassi = [v for v in re.findall(r";\s*(\d{1,3})\b", riga) if int(v) < 40]
            if bassi:
                return ("Voto sotto 40 nella stringa per DIDAweb (%s) (05/10 n. 23, regola 13): il voto "
                        "minimo è 40." % ", ".join(bassi))
    if RE_STRINGA_VOTI.search(testo) and not re.search(r"disciplin", testo, re.I):
        return ("Stringa dei voti per DIDAweb senza la Disciplina (#98, #117): sopra la stringa, in "
                "grassetto, «Disciplina da scegliere: …» (la materia firmata in quell'ora, da orario/), "
                "e il primo passo della tabella è sceglierla.")
    return None


# (h) «nessuna AI» da una vista remota (#90)
RE_NESSUNA_AI = re.compile(
    r"\b(?:nessun[ao]?|niente)\s+(?:uso\s+(?:di\s+|dell['’]\s*)?)?(?:AI|IA|intelligenza\s+artificiale|"
    r"chatgpt|gemini)\b", re.I)


def controllo_nessuna_ai(testo):
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_NESSUNA_AI.search(base)
    if not m or re.search(r"tutte\s+le\s+finestre|primo\s+piano", testo, re.I):
        return None
    return ("«%s» senza aver visto tutte le finestre (#90): scrivi «nella finestra in primo piano non si "
            "vede AI; le altre finestre non le ho viste», oppure di' che hai visto tutte le finestre e "
            "le schede." % m.group(0))


# (i) PC senza nome lasciato come «utente non indicato» (#100)
RE_SENZA_UTENTE = re.compile(r"utente\s+(?:non\s+indicato|sconosciuto|non\s+visibile|ignoto)", re.I)


def controllo_utente_non_indicato(testo):
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_SENZA_UTENTE.search(base)
    if not m or re.search(r"chi\s+c['’]è|chi\s+è\s+(?:al|sul)\s+PC", testo, re.I):
        return None
    return ("«%s» (#100): se un riquadro di Veyon non mostra il nome, chiedi subito al docente chi c'è "
            "a quel PC (una domanda, in cima)." % m.group(0))


# (j) parole che non servono (#53)
RE_PAROLE_INUTILI = re.compile(r"\b(onestamente|sinceramente|francamente|a\s+dire\s+il\s+vero)\b", re.I)


def controllo_parole_inutili(testo):
    m = RE_PAROLE_INUTILI.search(senza_citazioni(senza_riquadri(testo)))
    if m:
        return ("Parola che non serve (#53): «%s» fa pensare che altre volte non sia così. Toglila."
                % m.group(0))
    return None


# (k) passi scritti come catene di coordinate (#56)
RE_VERBO_PASSO = re.compile(r"\b(?:clicca|premi|apri|scrivi|incolla|copia|vai|torna|scegli)\b", re.I)


def controllo_catene_coordinate(testo):
    for riga in senza_riquadri(testo).splitlines():
        if riga.count(" · ") >= 2 and RE_VERBO_PASSO.search(riga):
            return ("Passo scritto come catena di coordinate (#56): «%s». Ogni passo è una frase che "
                    "comincia con il verbo («Clicca…», «Premi…»), con il «dove» detto a parole."
                    % riga.strip()[:100])
    return None


# (l) istruzioni con «se» e «salta» (#55)
RE_SALTA = re.compile(r"\bsalta\s+(?:al|alla|ai|alle|il|la)\s+(?:passo|parte|punto|sezione)|"
                      r"\bse\s+(?:la\s+scheda|la\s+pagina|il\s+file|la\s+finestra)\s+(?:è|e')\s+già\s+apert",
                      re.I)


def controllo_se_salta(testo):
    m = RE_SALTA.search(senza_citazioni(senza_riquadri(testo)))
    if m:
        return ("Istruzioni con condizioni (#55): «%s». Le istruzioni sono un flusso unico che parte da "
                "zero: niente «se», niente «salta»." % m.group(0))
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


def controllo_firma_gia_fatta(testo):
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_RICORDA_FIRMA.search(base)
    if not m:
        return None
    if not ore_di_oggi_tutte_firmate(datetime.datetime.now(TZ_ROMA)):
        return None
    return ("Firma ricordata, ma in FIRME-REGISTRO-2026-27.md tutte le ore di oggi risultano firmate "
            "(#36, #52, #87, #96): togli il promemoria della firma.")


# (n) errore da registrare rimandato (#113)
RE_CHIEDE_ERRORE = re.compile(
    r"(?:registr|scriv|segn|annot|aggiung|mett)\w*\b[^.?!\n]{0,60}\berror|sbirro", re.I)


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


def controllo_errore_rimandato(testo, data):
    richiesta = ultimo_messaggio_docente(data.get("transcript_path") or "")
    if not richiesta or not RE_CHIEDE_ERRORE.search(richiesta):
        return None
    if re.search(r"#\d{2,3}\b", testo):
        return None
    return ("Il docente ha chiesto di registrare un errore (#113): si scrive SUBITO in "
            "REGISTRO-ERRORI-CLAUDE.md, prima di ogni altro lavoro, e nel messaggio si dà il numero "
            "della voce (es. «registrato come #139»).")


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


# (p) indirizzo diretto del progetto Apps Script (regola 10, #51)
RE_SCRIPT_DIRETTO = re.compile(r"script\.google\.com/(?:d/|home/projects/)", re.I)


def controllo_script_diretto(testo):
    if RE_SCRIPT_DIRETTO.search(testo):
        return ("Indirizzo diretto del progetto Apps Script (regola 10): ha dato errore 400. Si apre "
                "https://script.google.com/home e si clicca «Consegne Classroom → Git», poi il file "
                "«automazione-corso.gs».")
    return None


# (q) messaggio lungo durante le ore di lezione (05/10 n. 6, #132, regola 3quinquies)
MAX_RIGHE_IN_LEZIONE = 30


def controllo_lungo_in_lezione(testo, adesso=None):
    adesso = adesso or datetime.datetime.now(TZ_ROMA)
    if adesso.weekday() > 4:
        return None
    minuti = adesso.hour * 60 + adesso.minute
    if not (7 * 60 + 50 <= minuti <= 14 * 60 + 10):
        return None
    righe = [r for r in senza_riquadri(testo).splitlines() if r.strip()]
    if len(righe) <= MAX_RIGHE_IN_LEZIONE:
        return None
    return ("Messaggio di %d righe durante la lezione (05/10 n. 6, #132): il docente è in classe e non "
            "riesce a leggerlo. Tieni solo le cose bloccanti e i riquadri da copiare (massimo %d righe); "
            "il resto va in un file." % (len(righe), MAX_RIGHE_IN_LEZIONE))


# (r) «non ha consegnato», «non risulta» senza aver guardato le fonti (#83, #95; 05/10 n. 5 e 16)
RE_NON_RISULTA = re.compile(
    r"\bnon\s+(?:ha|hanno)\s+(?:ancora\s+)?(?:caricato|consegnato|iniziato|fatto\s+(?:niente|nulla))|"
    r"\bnessuno\s+ha\s+(?:ancora\s+)?(?:caricato|consegnato)|\bnon\s+(?:gli\s+|le\s+)?risulta(?:no)?\b", re.I)
RE_FONTI = re.compile(r"ho\s+controllato|ho\s+verificato|controllat[oaie]|verificat[oaie]|clon\w*|"
                      r"tutt[ie]\s+(?:i|le|e)\s+(?:quiz|fonti|moduli|consegne|repository)|schermat\w*|"
                      r"cruscotto|classroom|\bmodul\w*|veyon|repository|\bfoglio\b", re.I)


def controllo_non_risulta(testo):
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_NON_RISULTA.search(base)
    if not m or RE_FONTI.search(testo):
        return None
    return ("«%s» senza dire dove hai controllato (#83, #95; 05/10 n. 16): prima si guardano tutte le "
            "fonti (tutti i quiz e i Moduli del giorno, Classroom, il clone del repository e l'account di "
            "oggi), poi si scrive «ho controllato …: non c'è»." % m.group(0))


# (s) «ha copiato» detto come certo (01/10 n. 6)
RE_COPIATO = re.compile(r"\b(?:ha|hanno)\s+(?:copiato|plagiato)\b", re.I)


def controllo_copiato(testo):
    base = senza_citazioni(senza_riquadri(testo))
    m = RE_COPIATO.search(base)
    if not m or re.search(r"da\s+verificare|potrebbe|potrebbero|sembra|forse|stesso\s+account", base, re.I):
        return None
    if not re.search(r"plagi|compagn|verific|compit|consegn|risposte|\bPC\s*\d", base, re.I):
        return None  # «ha copiato i file» detto di Windows, non di un allievo
    return ("«%s» detto come certo (01/10 n. 6): può essere lo stesso account su due PC. Si scrive al "
            "condizionale, «da verificare», finché non è confermato." % m.group(0))


# (t) risultato chiesto e trattenuto «al tuo avanti» (05/10 n. 21)
RE_ASPETTO_AVANTI = re.compile(r"(?:al\s+tuo|quando\s+(?:mi\s+)?dici)\s+[«\"]?avanti", re.I)
RE_DAMMI = re.compile(r"\b(?:dammi|fammi|fammel[aoie]|mandami)\b", re.I)


def controllo_avanti(testo, data):
    if not RE_ASPETTO_AVANTI.search(testo):
        return None
    richiesta = ultimo_messaggio_docente(data.get("transcript_path") or "")
    if not RE_DAMMI.search(richiesta or ""):
        return None
    return ("Il docente ha chiesto il risultato («dammi», «fammi»): si consegna appena è pronto, non «al tuo "
            "avanti» (05/10 n. 21; CLAUDE.md regola 3, «Fammeli» vince sul PPP).")


# (u) rimando a riquadri o testi di messaggi precedenti (05/10 n. 31)
RE_RIMANDO = re.compile(r"riquadr\w*\s+(?:di\s+prima|precedent\w*|che\s+ti\s+ho\s+(?:dato|mandato))|"
                        r"(?:link|testo|codice)\s+(?:di\s+prima|che\s+ti\s+ho\s+(?:dato|mandato)\s+prima)|"
                        r"\bvedi\s+(?:sopra|il\s+messaggio\s+precedente)", re.I)


def controllo_rimando_riquadri(testo):
    m = RE_RIMANDO.search(senza_citazioni(senza_riquadri(testo)))
    if m:
        return ("«%s» (05/10 n. 31): ogni messaggio con passi contiene TUTTI i riquadri da copiare che "
                "servono, anche se già dati prima." % m.group(0))
    return None


# (v) incollare in Apps Script senza dire in quale file (#51)
def controllo_file_apps_script(testo):
    if re.search(r"script\.google\.com|apps\s+script", testo, re.I) and \
            re.search(r"ctrl\s*\+\s*v", testo, re.I) and "automazione-corso.gs" not in testo:
        return ("Passi per Apps Script con «incolla» senza il file (#51): prima si clicca il file "
                "«automazione-corso.gs» nel pannello «File» a sinistra (il progetto si apre su «Codice.gs»).")
    return None


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
                      controllo_pronto_senza_verifica, controllo_link_senza_pubblicato,
                      controllo_promessa_tempi, controllo_voti_senza_disciplina, controllo_nessuna_ai,
                      controllo_utente_non_indicato, controllo_parole_inutili,
                      controllo_catene_coordinate, controllo_se_salta, controllo_firma_gia_fatta,
                      lambda t: controllo_errore_rimandato(t, data), controllo_link_riservato,
                      controllo_script_diretto, controllo_lungo_in_lezione, controllo_non_risulta,
                      controllo_copiato, lambda t: controllo_avanti(t, data), controllo_rimando_riquadri,
                      controllo_file_apps_script):
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
