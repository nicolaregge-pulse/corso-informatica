#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllore dei controlli (28/10/2026): in un colpo dice se i controlli automatici sono VIVI.

Nicola, 28/10/2026: niente promesse, servono meccanismi; e serve sapere che i meccanismi funzionano davvero.
Controlla:
  1. gli hook registrati nelle impostazioni di Claude Code, sia del repository (.claude/settings.json) sia della
     cartella /home/user (/home/user/.claude/settings.json, per le sessioni che partono da lì): promemoria-errori.py
     (UserPromptSubmit), limite-comandi.py (PreToolUse sui comandi Bash), versiona-tutto.sh e controllo-messaggio.py
     (Stop); i file degli hook esistono e si compilano (python3 -m py_compile, bash -n);
  2. attiva-controlli-home.py è idempotente (girato due volte su una copia vuota dà lo stesso file);
  3. le prove degli hook (.claude/hooks/prove/prova_*.py, più generatori/prova_audit_regole.py del riservato)
     stampano tutte «N/N»;
  4. .claude/passi-notturni.md si legge, ha la versione, l'ultimo passo «stato della notte» e i comandi che cita
     puntano a file che esistono;
  5. la notte di OGGI (ora di Roma) ha lasciato nel riservato stato/notte-<giorno>.json (scritto dall'ultimo passo dei passi
     notturni) e il file si legge;
  6. privacy del pubblico (28/10/2026): nei file tracciati di questo repository (tranne i JSON cifrati e
     .claude/hooks/prove/) non c'è nessun cognome dei ragazzi scritto come testo (nome e cognome visibili).
     Link e nomi utente GitHub dei ragazzi («nomecognome.github.io», «github.com/nomecognome…») NON si segnalano
     (28/10/2026, Nicola: sono i loro account pubblici e servono alle pagine). L'elenco dei cognomi viene dalle anagrafiche del
     riservato (generatori/privacy_nomi.py); se il riservato manca il controllo è GIALLO e non conta come errore.
     Il rosso dice solo i file e quanti cognomi, mai i cognomi.
  7. lavoro del giorno (29/10/2026): per ogni classe in orario oggi c'è docs/cruscotto/piano/<classe>-<oggi>.json con
     almeno 3 proposte (1 per le classi che oggi hanno solo Sicurezza) e PROPOSTE-OGGI.md ha la data di oggi; nei giorni
     senza lezione è VERDE «oggi niente lezioni».
La PRIMA riga è l'esito con «DA SAPERE SUBITO» (lavoro del giorno mancante, notte fallita); l'ultima ripete l'esito.
Stampa una riga per controllo, «VERDE: <cosa>», «GIALLO: <cosa>» o «ROSSO: <cosa>», e in fondo «ESITO: VERDE» o
«ESITO: ROSSO (N)».
Esce con 0 se tutto è VERDE, 1 altrimenti. Non scrive niente nei repository. Nessun segreto: legge solo impostazioni,
prove e nomi di file.
Uso (una riga):
    python3 /home/user/corso-informatica/strumenti/controlla_controlli.py
    python3 /home/user/corso-informatica/strumenti/controlla_controlli.py --notte 2026-10-29
Opzioni: --notte AAAA-MM-GG controlla quella notte (predefinito: oggi, ora di Roma);
         --senza-prove salta il punto 3 (più veloce); --solo-privacy fa solo il punto 6.
"""
import argparse, datetime, glob, json, os, re, subprocess, sys, tempfile

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIS = os.path.join(os.path.dirname(PUB), "corso-informatica-riservato")
HOOKS = os.path.join(PUB, ".claude", "hooks")
IMPOSTAZIONI = {"repository": os.path.join(PUB, ".claude", "settings.json"),
                "/home/user": "/home/user/.claude/settings.json"}
ATTESI = [("UserPromptSubmit", None, "promemoria-errori.py"),
          ("PreToolUse", "Bash", "limite-comandi.py"),
          ("Stop", None, "versiona-tutto.sh"),
          ("Stop", None, "controllo-messaggio.py")]
try:
    from zoneinfo import ZoneInfo
    ROMA = ZoneInfo("Europe/Rome")
except Exception:  # pragma: no cover
    ROMA = None

righe = []


def esito(ok, cosa):
    righe.append(("VERDE" if ok else "ROSSO", cosa))


def giallo(cosa):
    righe.append(("GIALLO", cosa))


BINARI = re.compile(r"\.(png|jpe?g|webp|gif|ico|pdf|zip|7z|woff2?|ttf|otf|mp3|mp4|wav|ogg|xlsx|docx|pptx|pck|wasm|import|exe)$", re.I)
CODICE = (".py", ".js", ".mjs", ".gd", ".sh", ".gs")


def controlla_privacy():
    gen = os.path.join(RIS, "generatori")
    if not os.path.isfile(os.path.join(gen, "privacy_nomi.py")):
        giallo("privacy del pubblico: repository riservato non trovato accanto, cognomi non cercati")
        return
    try:
        if gen not in sys.path:
            sys.path.append(gen)
        import privacy_nomi
        privacy_nomi.disattiva()   # qui si legge soltanto
        n_cognomi = len(privacy_nomi.cognomi())
    except Exception as e:
        giallo("privacy del pubblico: elenco dei cognomi non leggibile (%s)" % str(e)[:80])
        return
    if not n_cognomi:
        giallo("privacy del pubblico: nessun cognome nelle anagrafiche del riservato")
        return
    file_git = subprocess.run(["git", "-C", PUB, "ls-files"], capture_output=True, text=True).stdout.splitlines()
    trovati, letti = [], 0
    for rel in file_git:
        if rel.startswith(".claude/hooks/prove/") or BINARI.search(rel):
            continue
        try:
            testo = open(os.path.join(PUB, rel), encoding="utf-8").read()
        except Exception:
            continue
        if privacy_nomi._CIFRATO.match(testo):   # JSON cifrati (cifra_json e i formati più vecchi salt/iv/ct)
            continue
        letti += 1
        h = privacy_nomi.trova(testo, codice=rel.endswith(CODICE))
        if h:
            trovati.append("%s (%d)" % (rel, len(h)))
    esito(not trovati, "privacy del pubblico: %d file letti, %d cognomi cercati nel testo (link e nomi utente GitHub esclusi)" % (letti, n_cognomi)
          + (": cognomi in " + ", ".join(trovati[:15]) + (" e altri %d" % (len(trovati) - 15) if len(trovati) > 15 else "") if trovati else ""))


def notte_attesa(adesso):
    """Notte da controllare = OGGI in ora di Roma (29/10/2026, REGISTRO-ERRORI #139). La Chat del giorno parte alle
    0:00 (regola 26) e prepara il giorno stesso: stato/notte-<oggi>.json deve esserci già alle 6:20. Prima si
    cercava il giorno precedente fino alle 8:00, e il 29/10 alle 6:20 il controllo ha guardato il 28 invece del 29."""
    if ROMA is not None and adesso.tzinfo is not None:
        adesso = adesso.astimezone(ROMA)
    return adesso.date().isoformat()


MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre",
        "novembre", "dicembre"]
CLASSI_PAROLE = {"prima informatica": "1INF", "seconda informatica": "2INF", "terza informatica": "3INF",
                 "quarta": "4TI"}


def lezioni_di(giorno, pub=None):
    """Ore di lezione del giorno: [(classe, disciplina)], e se l'orario copre quel giorno (None = orario ignoto).
    Fonte 1: docs/avanzamento/orario-lezioni.json (strumenti/orario_json.py); fonte 2: PROSSIME-LEZIONI.md."""
    pub = pub or PUB
    try:
        d = json.load(open(os.path.join(pub, "docs", "avanzamento", "orario-lezioni.json"), encoding="utf-8"))
        lez = d.get("lezioni") or {}
        if giorno in lez:
            return [(v.get("classe", ""), v.get("disciplina", "")) for v in lez[giorno]], True
        coperto = any(k >= giorno for k in lez)
    except Exception:
        coperto = False
    g = datetime.date.fromisoformat(giorno)
    try:
        testo = open(os.path.join(pub, "PROSSIME-LEZIONI.md"), encoding="utf-8").read()
    except Exception:
        testo = ""
    titolo = re.compile(r"^##\s+\S+\s+%d\s+%s\b" % (g.day, MESI[g.month - 1]), re.I | re.M)
    m = titolo.search(testo)
    if m:
        sezione = re.split(r"^## ", testo[m.end():], maxsplit=1, flags=re.M)[0]
        ore = []
        for h in re.findall(r"^###\s+(.+)$", sezione, re.M):
            parti = [x.strip() for x in h.split(",")]
            classe = CLASSI_PAROLE.get(parti[0].lower(), parti[0])
            ore.append((classe, parti[2] if len(parti) > 2 else ""))
        return ore, True
    if coperto or re.search(r"^##\s+\S+\s+\d+\s+%s" % MESI[g.month - 1], testo, re.M | re.I):
        return [], True
    return [], None


def controlla_lavoro_del_giorno(giorno, pub=None):
    """Regola 26: per ogni classe in orario oggi docs/cruscotto/piano/<classe>-<oggi>.json con almeno 3 proposte
    (1 se la classe ha solo Sicurezza) e PROPOSTE-OGGI.md con la data di oggi. Restituisce la frase per il docente
    (vuota se è tutto a posto)."""
    pub = pub or PUB
    g = datetime.date.fromisoformat(giorno)
    ore, noto = lezioni_di(giorno, pub)
    if not ore:
        if g.weekday() >= 5 or noto:
            esito(True, "lavoro del giorno %s: oggi niente lezioni" % giorno)
            return ""
        frase = "Non so quali classi hanno lezione oggi %s: orario e PROSSIME-LEZIONI.md non hanno questo giorno" % giorno
        esito(False, "lavoro del giorno: " + frase)
        return frase
    classi = {}
    for classe, disc in ore:
        classi.setdefault(classe, []).append(disc)
    mancano, poche = [], []
    for classe, discipline in classi.items():
        minimo = 1 if all("sicurezza" in (x or "").lower() for x in discipline) else 3
        f = os.path.join(pub, "docs", "cruscotto", "piano", "%s-%s.json" % (classe.lower(), giorno))
        try:
            n = len(json.load(open(f, encoding="utf-8")).get("proposte") or [])
        except Exception:
            mancano.append(classe)
            continue
        if n < minimo:
            poche.append("%s (%d su %d)" % (classe, n, minimo))
    problemi = []
    if mancano:
        problemi.append("Mancano le proposte di oggi per " + ", ".join(mancano))
    if poche:
        problemi.append("Troppo poche proposte per " + ", ".join(poche))
    try:
        p = open(os.path.join(pub, "PROPOSTE-OGGI.md"), encoding="utf-8").read()
    except Exception:
        p = None
    date_ok = (giorno, g.strftime("%d/%m/%Y"), "%d %s" % (g.day, MESI[g.month - 1]))
    if p is None:
        problemi.append("PROPOSTE-OGGI.md non esiste")
    elif not any(x in p for x in date_ok):
        problemi.append("PROPOSTE-OGGI.md non ha la data di oggi")
    frase = "; ".join(problemi)
    esito(not problemi, "lavoro del giorno %s (%s): " % (giorno, ", ".join(classi)) +
          (frase + ": la preparazione della notte non è finita" if problemi else "piani e PROPOSTE-OGGI.md presenti"))
    return frase + (": la preparazione della notte non è finita" if frase else "")


def controlla_impostazioni():
    for dove, f in IMPOSTAZIONI.items():
        try:
            cfg = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            esito(False, "impostazioni %s (%s) non leggibili: %s" % (dove, f, e))
            continue
        hooks = cfg.get("hooks") or {}
        mancano = []
        for evento, matcher, script in ATTESI:
            trovato = False
            for gruppo in hooks.get(evento) or []:
                if matcher and gruppo.get("matcher") != matcher:
                    continue
                if any(script in (h.get("command") or "") for h in gruppo.get("hooks") or []):
                    trovato = True
            if not trovato:
                mancano.append("%s %s" % (evento, script))
        esito(not mancano, "hook registrati nelle impostazioni %s" % dove + (": mancano " + ", ".join(mancano) if mancano else " (4 su 4)"))


def controlla_file_hook():
    rotti = []
    for _, _, script in ATTESI:
        p = os.path.join(HOOKS, script)
        if not os.path.isfile(p):
            rotti.append(script + " non esiste")
            continue
        cmd = ["bash", "-n", p] if p.endswith(".sh") else [sys.executable, "-c", "import ast,sys; ast.parse(open(sys.argv[1]).read())", p]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            rotti.append(script + " non si compila")
    esito(not rotti, "file degli hook presenti e senza errori di sintassi" + (": " + "; ".join(rotti) if rotti else ""))


def controlla_attiva_home():
    src = os.path.join(HOOKS, "attiva-controlli-home.py")
    try:
        testo = open(src, encoding="utf-8").read()
    except Exception as e:
        esito(False, "attiva-controlli-home.py non leggibile: %s" % e)
        return
    with tempfile.TemporaryDirectory() as t:
        dest = os.path.join(t, "settings.json")
        prova = os.path.join(t, "attiva.py")
        nuovo = re.sub(r'DEST = "[^"]*"', 'DEST = %r' % dest, testo, count=1)
        open(prova, "w", encoding="utf-8").write(nuovo)
        uscite, copie = [], []
        for _ in range(2):
            r = subprocess.run([sys.executable, prova], capture_output=True, text=True)
            uscite.append(r.stdout.strip())
            copie.append(open(dest, encoding="utf-8").read() if os.path.exists(dest) else "")
        ok = uscite == ["ok", "ok"] and copie[0] and copie[0] == copie[1]
        n = 0
        try:
            n = sum(len(g.get("hooks") or []) for v in json.loads(copie[1]).get("hooks", {}).values() for g in v)
        except Exception:
            ok = False
        esito(ok and n == 4, "attiva-controlli-home.py idempotente (due giri, %d hook, file identico)" % n)


def controlla_prove():
    prove = sorted(glob.glob(os.path.join(HOOKS, "prove", "prova_*.py")))
    extra = os.path.join(RIS, "generatori", "prova_audit_regole.py")
    if os.path.isfile(extra):
        prove.append(extra)
    if not prove:
        esito(False, "prove degli hook: nessun file in .claude/hooks/prove/")
        return
    for p in prove:
        try:
            r = subprocess.run([sys.executable, p], capture_output=True, text=True, timeout=300, cwd=os.path.dirname(p))
            ultima = (r.stdout.strip().splitlines() or [""])[-1]
        except subprocess.TimeoutExpired:
            ultima, r = "tempo scaduto", None
        m = re.match(r"^(\d+)/(\d+)$", ultima)
        ok = bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 0 and r is not None and r.returncode == 0
        esito(ok, "prove %s: %s" % (os.path.basename(p), ultima or "nessun risultato"))


def controlla_passi():
    f = os.path.join(PUB, ".claude", "passi-notturni.md")
    try:
        t = open(f, encoding="utf-8").read()
    except Exception as e:
        esito(False, "passi-notturni.md non leggibile: %s" % e)
        return
    problemi = []
    if not re.search(r"\*\*Versione \d+\.\d+\*\*", t):
        problemi.append("manca la versione")
    if "stato/notte-" not in t or "controlla_controlli.py" not in t:
        problemi.append("manca l'ultimo passo «stato della notte»")
    for cmd in re.findall(r"(?:python3|bash)\s+((?:/home/user/|strumenti/|generatori/)[^\s`]+\.(?:py|sh))", t):
        base = PUB if cmd.startswith("strumenti/") else (RIS if cmd.startswith("generatori/") else "")
        p = os.path.join(base, cmd) if base else cmd
        if not os.path.isfile(p):
            problemi.append("comando citato senza file: " + cmd)
    esito(not problemi, "passi-notturni.md leggibile" + (": " + "; ".join(sorted(set(problemi))) if problemi else ""))


def controlla_notte(giorno, ris=None):
    """Restituisce la frase per il docente se la notte è fallita (vuota se è a posto)."""
    f = os.path.join(ris or RIS, "stato", "notte-%s.json" % giorno)
    rel = "stato/notte-%s.json" % giorno
    if not os.path.isfile(f):
        frase = "La preparazione della notte del %s non risulta finita: nel riservato manca %s" % (giorno, rel)
        esito(False, frase + " (lo scrive l'ultimo passo di passi-notturni.md)")
        return frase
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        esito(False, "notte del %s: %s non si legge (%s)" % (giorno, rel, e))
        return "La notte del %s ha lasciato %s illeggibile" % (giorno, rel)
    mancano = [k for k in ("ora", "regole_rilette", "controlla_controlli", "classi_preparate", "problemi") if k not in d]
    esito(not mancano, "notte del %s: %s presente" % (giorno, rel) + (", mancano i campi " + ", ".join(mancano) if mancano else ""))
    if d.get("problemi"):
        return "La notte del %s ha lasciato problemi aperti: %s" % (giorno, "; ".join(map(str, d["problemi"]))[:300])
    return ""


def stampa(da_sapere):
    """Prima riga = l'esito con le cose che il docente deve sapere subito (29/10/2026, REGISTRO-ERRORI #139)."""
    rossi = sum(1 for e, _ in righe if e == "ROSSO")
    finale = "ESITO: VERDE" if not rossi else "ESITO: ROSSO (%d)" % rossi
    da_sapere = [x for x in da_sapere if x]
    print(finale + ((". DA SAPERE SUBITO: " + " | ".join(da_sapere)) if da_sapere else ""))
    for e, cosa in righe:
        print("%s: %s" % (e, cosa))
    print(finale)
    return 0 if not rossi else 1


def main():
    a = argparse.ArgumentParser(description="Controllore dei controlli automatici")
    a.add_argument("--notte", default=None, help="AAAA-MM-GG della notte da controllare")
    a.add_argument("--senza-prove", action="store_true")
    a.add_argument("--solo-privacy", action="store_true")
    args = a.parse_args()
    adesso = datetime.datetime.now(ROMA) if ROMA else datetime.datetime.now()
    if args.solo_privacy:
        controlla_privacy()
        for e, cosa in righe:
            print("%s: %s" % (e, cosa))
        rossi = sum(1 for e, _ in righe if e == "ROSSO")
        print("ESITO: VERDE" if not rossi else "ESITO: ROSSO (%d)" % rossi)
        return 0 if not rossi else 1
    controlla_impostazioni()
    controlla_file_hook()
    controlla_attiva_home()
    if not args.senza_prove:
        controlla_prove()
    controlla_passi()
    oggi = args.notte or notte_attesa(adesso)
    da_sapere = [controlla_lavoro_del_giorno(oggi), controlla_notte(oggi)]
    controlla_privacy()
    return stampa(da_sapere)


if __name__ == "__main__":
    sys.exit(main())
