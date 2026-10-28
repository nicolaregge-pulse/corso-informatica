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
  5. la notte precedente ha lasciato nel riservato stato/notte-<giorno>.json (scritto dall'ultimo passo dei passi
     notturni) e il file si legge;
  6. privacy del pubblico (28/10/2026): nei file tracciati di questo repository (tranne i JSON cifrati e
     .claude/hooks/prove/) non c'è nessun cognome dei ragazzi scritto come testo (nome e cognome visibili).
     Link e nomi utente GitHub dei ragazzi («nomecognome.github.io», «github.com/nomecognome…») NON si segnalano
     (28/10/2026, Nicola: sono i loro account pubblici e servono alle pagine). L'elenco dei cognomi viene dalle anagrafiche del
     riservato (generatori/privacy_nomi.py); se il riservato manca il controllo è GIALLO e non conta come errore.
     Il rosso dice solo i file e quanti cognomi, mai i cognomi.
Stampa una riga per controllo, «VERDE: <cosa>», «GIALLO: <cosa>» o «ROSSO: <cosa>», e in fondo «ESITO: VERDE» o
«ESITO: ROSSO (N)».
Esce con 0 se tutto è VERDE, 1 altrimenti. Non scrive niente nei repository. Nessun segreto: legge solo impostazioni,
prove e nomi di file.
Uso (una riga):
    python3 /home/user/corso-informatica/strumenti/controlla_controlli.py
    python3 /home/user/corso-informatica/strumenti/controlla_controlli.py --notte 2026-10-29
Opzioni: --notte AAAA-MM-GG controlla quella notte (predefinito: l'ultima notte di lavoro attesa, vedi notte_attesa);
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
    """Ultima notte di lavoro che deve già esserci: la Chat del giorno parte lunedì-venerdì alle 6:47 (e alle 0:00,
    regola 26) e lavora per il giorno stesso. Dalle 8:00 di un giorno feriale si aspetta il file di quel giorno;
    prima delle 8:00, o di sabato e domenica, quello dell'ultimo giorno feriale precedente."""
    g = adesso.date()
    if not (g.weekday() < 5 and adesso.hour >= 8):
        g -= datetime.timedelta(days=1)
        while g.weekday() >= 5:
            g -= datetime.timedelta(days=1)
    return g.isoformat()


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


def controlla_notte(giorno):
    f = os.path.join(RIS, "stato", "notte-%s.json" % giorno)
    rel = "stato/notte-%s.json" % giorno
    if not os.path.isfile(f):
        esito(False, "notte del %s: nel riservato manca %s (lo scrive l'ultimo passo di passi-notturni.md)" % (giorno, rel))
        return
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        esito(False, "notte del %s: %s non si legge (%s)" % (giorno, rel, e))
        return
    mancano = [k for k in ("ora", "regole_rilette", "controlla_controlli", "classi_preparate", "problemi") if k not in d]
    esito(not mancano, "notte del %s: %s presente" % (giorno, rel) + (", mancano i campi " + ", ".join(mancano) if mancano else ""))


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
    controlla_notte(args.notte or notte_attesa(adesso))
    controlla_privacy()
    for e, cosa in righe:
        print("%s: %s" % (e, cosa))
    rossi = sum(1 for e, _ in righe if e == "ROSSO")
    print("ESITO: VERDE" if not rossi else "ESITO: ROSSO (%d)" % rossi)
    return 0 if not rossi else 1


if __name__ == "__main__":
    sys.exit(main())
