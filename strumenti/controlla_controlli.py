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
  8. fine giornata (29/10/2026 sera, #141 #144 #145 #146 #155 #156): per ogni classe del giorno precedente compito
     uscito entro la campanella, verifica VERDE, presenze nel diario, cruscotto con una riga per presente e senza
     «null», nessun 40 a chi ha finito, report PDF di ogni ora, domande con risposta, non-andato.md scritto.
Opzioni: --notte AAAA-MM-GG controlla quella notte (predefinito: oggi, ora di Roma);
         --fine-giornata AAAA-MM-GG fa solo il punto 8 per quel giorno;
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



def _uscita_dopo(uscita, da, giorno):
    """True se il compito è uscito DOPO la campanella del giorno. «18:18 del 29/10» = giorno prima: va bene.
    (30/10/2026, controllore di fine giornata: prima si confrontavano solo le ore e la sera prima risultava «dopo».)"""
    m = re.match(r"\s*(\d{1,2})[:.](\d{2})(?:\s+del\s+(\d{1,2})/(\d{1,2}))?", uscita)
    if not m:
        return True
    if m.group(3):
        gg, mm = int(m.group(3)), int(m.group(4))
        y, mo, d = (int(x) for x in giorno.split("-"))
        if (mm, gg) < (mo, d):
            return False
        if (mm, gg) > (mo, d):
            return True
    return "%02d:%02d" % (int(m.group(1)), int(m.group(2))) > da

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
        # 29/10/2026 (audit): le immagini incorporate (data:...;base64,...) non sono testo: un cognome corto può
        # comparire per caso dentro i caratteri base64 (falso rosso nei libri di testo HTML del 29/10).
        testo = re.sub(r"data:[a-z0-9.+/-]+;base64,[A-Za-z0-9+/=\s]+", " ", testo, flags=re.I)
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
    for extra in ("prova_controlla_controlli.py", "prova_situazione_quiz.py"):   # 29/10/2026 (#147-#152)
        if os.path.isfile(os.path.join(PUB, "strumenti", extra)):
            prove.append(os.path.join(PUB, "strumenti", extra))
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
    # #152 (29/10/2026): la notte vale solo se ha girato DA SOLA prima delle 6:30 e ha eseguito il controllore
    cc_txt = json.dumps(d.get("controlla_controlli", ""), ensure_ascii=False).lower()
    tardi = str(d.get("ora", "")) > "06:30"
    non_eseguito = "non eseguito" in cc_txt or "fallit" in cc_txt
    esito(not (tardi or non_eseguito), "notte del %s girata da sola (#152)" % giorno +
          ((": " + ", ".join(x for x, s in (("finita alle %s, dopo le 6:30" % d.get("ora"), tardi),
                                             ("controllore non eseguito o notte fallita", non_eseguito)) if s)) if (tardi or non_eseguito) else ""))
    if tardi or non_eseguito:
        return "La preparazione della notte del %s non ha girato da sola (%s)" % (giorno, "finita alle %s" % d.get("ora") if tardi else "controllore non eseguito")
    if d.get("problemi"):
        return "La notte del %s ha lasciato problemi aperti: %s" % (giorno, "; ".join(map(str, d["problemi"]))[:300])
    return ""


# ----------------------------------------------- controlli aggiunti il 29/10/2026 pomeriggio (#147-#150, #152)

def _git(cwd, *a):
    try:
        return subprocess.run(["git", "-C", cwd] + list(a), capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return ""


def _leggi_json_testo(t):
    try:
        d = json.loads(t)
    except Exception:
        return None
    if isinstance(d, dict) and d.get("cifrato"):
        try:
            sys.path.insert(0, os.path.join(PUB, "strumenti"))
            import cifra_json
            d = cifra_json.decifra(d)
        except Exception:
            return None
    return d


def firma_campi(d):
    """Campi che una pagina può leggere: chiavi in cima e chiavi delle righe (d['righe'] o lista)."""
    if not isinstance(d, (dict, list)):
        return set()
    out = set(d.keys()) if isinstance(d, dict) else set()
    righe_d = d.get("righe") if isinstance(d, dict) else d
    if isinstance(righe_d, list):
        for r in righe_d[:50]:
            if isinstance(r, dict):
                out |= {"righe." + k for k in r.keys()}
    return out


def controlla_formato_json(pub=None, ore=24, file_=None):
    """#147: un JSON letto dalle pagine non perde campi rispetto alle versioni delle ultime 24 ore: una pagina rimasta
    nella cache del browser legge ancora i campi vecchi (29/10 13:30, monitor quiz 1INF tutto «MANCA»).
    Restituisce l'elenco dei problemi."""
    pub = pub or PUB
    if file_ is None:
        file_ = sorted(glob.glob(os.path.join(pub, "docs", "avanzamento", "*-quiz.json")) +
                       glob.glob(os.path.join(pub, "docs", "*", "dati.json")))
    problemi = []
    for f in file_:
        rel = os.path.relpath(f, pub)
        shas = _git(pub, "log", "--since=%d hours ago" % ore, "--format=%h", "--", rel).split()
        if not shas:
            continue
        try:
            ora_d = _leggi_json_testo(open(f, encoding="utf-8").read())
        except Exception:
            continue
        adesso_c = firma_campi(ora_d)
        if not adesso_c:
            continue
        persi = set()
        for s in shas[:: max(1, len(shas) // 12)][:12] + shas[-1:]:
            vecchio = _leggi_json_testo(_git(pub, "show", "%s:%s" % (s, rel)))
            persi |= firma_campi(vecchio) - adesso_c
        persi = {p for p in persi if p not in ("generato",)}
        if persi:
            problemi.append("%s ha perso i campi %s" % (rel, ", ".join(sorted(persi)[:6])))
    esito(not problemi, "formato dei JSON delle pagine compatibile con le versioni delle ultime %d ore (#147)" % ore +
          (": " + "; ".join(problemi) + " (rimetterli come alias)" if problemi else ""))
    return problemi


def controlla_coppie_docente_ragazzi(pub=None, ris=None, configs=None):
    """#148: la pagina del docente (JSON cifrato) e quella dei ragazzi (dati.json) mostrano gli stessi dati: stesso
    «generato». Restituisce l'elenco dei problemi."""
    pub, ris = pub or PUB, ris or RIS
    if configs is None:
        configs = sorted(glob.glob(os.path.join(ris, "config", "situazione-quiz", "*.json")))
    problemi = []
    for c in configs:
        try:
            cfg = json.load(open(c, encoding="utf-8"))
        except Exception:
            continue
        if not cfg.get("ragazzi") or not cfg.get("pubblico"):
            continue
        fd = os.path.join(pub, "docs", "avanzamento", cfg["pubblico"])
        fr = os.path.join(pub, "docs", cfg["ragazzi"], "dati.json")
        if not (os.path.exists(fd) and os.path.exists(fr)):
            continue
        dd = _leggi_json_testo(open(fd, encoding="utf-8").read())
        dr = _leggi_json_testo(open(fr, encoding="utf-8").read())
        if dd is None:
            giallo("coppia docente/ragazzi %s: JSON del docente non decifrabile qui" % os.path.basename(c))
            continue
        gd, gr = (dd or {}).get("generato", ""), (dr or {}).get("generato", "")
        if gd != gr:
            problemi.append("%s: docente %s, ragazzi %s" % (os.path.basename(c), gd or "?", gr or "?"))
    esito(not problemi, "pagina del docente e dei ragazzi con gli stessi dati (#148)" +
          (": " + "; ".join(problemi) if problemi else ""))
    return problemi


def controlla_ponte_quiz(ris=None, configs=None, giorno=None, scarto_min=6):
    """#149: i quiz del giorno si leggono TUTTI a ogni giro (dati della stessa ora, scarto massimo 6 minuti tra
    l'ultima lettura di un quiz e quella di un altro). Una colonna «moduli» del giorno (cartella con la data di oggi o
    successiva) deve avere il suo comando di lettura nel «ponte». Restituisce l'elenco dei problemi."""
    ris = ris or RIS
    giorno = giorno or (datetime.datetime.now(ROMA) if ROMA else datetime.datetime.now()).strftime("%Y-%m-%d")
    g8 = giorno.replace("-", "")
    if configs is None:
        configs = sorted(glob.glob(os.path.join(ris, "config", "situazione-quiz", "*.json")))
    problemi = []
    for c in configs:
        try:
            cfg = json.load(open(c, encoding="utf-8"))
        except Exception:
            continue
        po = cfg.get("ponte") or []
        po = [po] if isinstance(po, dict) else po
        salva = {os.path.normpath(p.get("salva_in", "")) for p in po}
        for col in cfg.get("colonne", []):
            m = re.search(r"(\d{8})$", col.get("dir", ""))
            if col.get("tipo") == "moduli" and m and m.group(1) >= g8 and os.path.normpath(col["dir"]) not in salva:
                problemi.append("%s: «%s» senza comando di lettura nel ponte" % (os.path.basename(c), col.get("corta", col.get("etichetta"))))
        ore_l = []
        for p in po:
            base = os.path.splitext(os.path.basename(p.get("comando", "")))[0]
            if not base:
                continue
            t = _git(ris, "log", "-1", "--format=%ct", "--grep=Ponte Google: " + base, "--", p["comando"]).strip()
            if t.isdigit():
                ore_l.append(int(t))
        oggi_l = [t for t in ore_l if datetime.datetime.fromtimestamp(t, ROMA).strftime("%Y-%m-%d") == giorno] if ROMA else ore_l
        if len(oggi_l) >= 2 and (max(oggi_l) - min(oggi_l)) > scarto_min * 60:
            problemi.append("%s: quiz letti a turno, scarto di %d minuti" % (os.path.basename(c), (max(oggi_l) - min(oggi_l)) // 60))
    esito(not problemi, "quiz del giorno letti tutti insieme dal ponte (#149)" + (": " + "; ".join(problemi) if problemi else ""))
    return problemi


def controlla_sicurezza_pronta(giorno, pub=None, ris=None):
    """#150 (ripete #129): per ogni classe con Sicurezza nel giorno, il compito con il quiz è già in coda prima della
    lezione e la pagina dell'ora DOPO è già pronta (docs/verifica/banche/<classe>-sicurezza-<N+1>ora.js), così se il
    docente chiede un'altra ora non si lavora a lezione iniziata. Restituisce l'elenco dei problemi."""
    pub, ris = pub or PUB, ris or RIS
    ore, _ = lezioni_di(giorno, pub)
    classi = {}
    for classe, disc in ore:
        if "sicurezza" in (disc or "").lower():
            classi[classe] = classi.get(classe, 0) + 1
    problemi, gialli = [], []
    for classe, n_ore in sorted(classi.items()):
        coda = [f for f in glob.glob(os.path.join(ris, "coda", "%s_%s_*sicurezza*.json" % (giorno, classe))) +
                glob.glob(os.path.join(ris, "coda", "archivio", "%s_%s_*sicurezza*.json" % (giorno, classe)))]
        con_quiz = []
        for f in coda:
            try:
                d = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            if d.get("quiz") or d.get("moduli") or "docs.google.com/forms" in (d.get("descrizione") or ""):
                con_quiz.append(os.path.basename(f))
        if not con_quiz:
            problemi.append("%s: nessun compito di Sicurezza con il quiz in coda per il %s" % (classe, giorno))
            continue
        m = re.search(r"sicurezza-(\d+)ora", " ".join(con_quiz))
        if not m:
            continue
        dopo = int(m.group(1)) + n_ore
        banca = os.path.join(pub, "docs", "verifica", "banche", "%s-sicurezza-%dora.js" % (classe.lower(), dopo))
        if not os.path.exists(banca):
            (problemi if n_ore >= 2 else gialli).append("%s: l'ora dopo (%dª) non è pronta (%s)" % (
                classe, dopo, os.path.relpath(banca, pub)))
    for x in gialli:
        giallo("Sicurezza %s: %s (#150)" % (giorno, x))
    esito(not problemi, "Sicurezza del %s preparata prima della lezione (#150)" % giorno +
          (": " + "; ".join(problemi) if problemi else ""))
    return problemi


# ----------------------------------------------- fine giornata (29/10/2026 sera: #141 #144 #145 #146 #155 #156, regole 22 e 24)

def _ora_roma(iso):
    try:
        d = datetime.datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
        return d.astimezone(ROMA).strftime("%H:%M") if ROMA else d.strftime("%H:%M")
    except Exception:
        return ""


def _presenti_diario(ris, classe, giorno):
    """Numero dei presenti dal diario della classe (ultimo numero detto: entrate in ritardo comprese)."""
    f = os.path.join(ris, "diario", classe.upper(), "%s.md" % giorno)
    try:
        t = open(f, encoding="utf-8").read()
    except Exception:
        return None
    m = re.findall(r"presenti(?:\s+sono)?\s*\(?(\d+)|(\d+)\s+presenti", t, re.I)
    vals = [int(a or b) for a, b in m]
    return vals[-1] if vals else None


def _ultimo_cruscotto(ris, classe, giorno):
    for c in (classe.lower(), classe.upper()):
        d = os.path.join(ris, "storico", "cruscotti", c, giorno)
        if os.path.isdir(d):
            fs = sorted(os.listdir(d), key=lambda x: re.sub(r"\D", "", x))
            if fs:
                return os.path.join(d, fs[-1])
    return None



def _hhmm_min(x):
    m = re.search(r"(\d{2})(\d{2})(?!.*\d{4})", x)
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None



def _quiz_lavoro_futuro(classe, giorno, pub, ris, testi=None):
    """#160: le banche dei quiz della classe toccate nel giorno non devono chiedere i lavori del laboratorio dello
    stesso giorno (titoli «Ora N · Titolo» delle voci di coda) né «il programma che hai fatto oggi in laboratorio»,
    salvo il segno «dopo_il_lavoro» nella banca (quiz fatto DOPO il lavoro). testi = {nome: testo} per le prove."""
    titoli = []
    for f in glob.glob(os.path.join(ris, "coda", "%s_%s_*.json" % (giorno, classe.upper()))):
        try:
            t = json.load(open(f, encoding="utf-8")).get("titolo", "")
        except Exception:
            continue
        m = re.search(r"\bOra\s+\d\s*·\s*([^·]+)", t)
        if m:
            parola = [w for w in re.findall(r"[a-zà-ù]{5,}", m.group(1).lower()) if w not in ("numeri", "della", "delle")]
            titoli.extend(parola[:1])
    if testi is None:
        testi = {}
        try:
            r = subprocess.run(["git", "-C", pub, "log", "--since", giorno + " 00:00", "--until", giorno + " 23:59",
                                "--name-only", "--format=", "--", "docs/verifica/banche/"], capture_output=True, text=True, timeout=60)
            for f in set(r.stdout.split()):
                if os.path.basename(f).lower().startswith(classe.lower()) and os.path.exists(os.path.join(pub, f)):
                    testi[f] = open(os.path.join(pub, f), encoding="utf-8").read()
        except Exception:
            pass
    out = []
    for f, t in testi.items():
        if f == "_prova" or "dopo_il_lavoro" in t:
            continue
        # le domande della verifica le vedono solo se la verifica o il recupero sono stati aperti nel giorno
        ms = re.search(r'"stato"\s*:\s*"([^"]+)"', t)
        if ms and not testi.get("_prova"):
            st = os.path.join("docs", "verifica", ms.group(1))
            try:
                r = subprocess.run(["git", "-C", pub, "log", "-p", "--since", giorno + " 00:00", "--until", giorno + " 23:59",
                                    "--", st], capture_output=True, text=True, timeout=60).stdout
                r += open(os.path.join(pub, st), encoding="utf-8").read()
            except Exception:
                r = '"verifica": "aperta"'
            if not re.search(r'"verifica"\s*:\s*"aperta"|"recupero"\s*:\s*"aperto"', r):
                continue
        low = t.lower()
        trovate = [w for w in titoli if w in low]
        if re.search(r"(?:hai\s+fatto|fatto\s+tu)\s+oggi\s+in\s+laboratorio", low):
            trovate.append("«fatto oggi in laboratorio»")
        if trovate:
            out.append("%s: il quiz %s chiede il lavoro di oggi non ancora fatto (%s) (#160)"
                       % (classe, os.path.basename(f), ", ".join(trovate)))
    return out

def _controlli_30_10(classe, ore, giorno, pub, ris, piano):
    """Controlli nati il 30/10/2026 (REGISTRO-ERRORI #162-#170), sul dato vero.
    1. #168: voci di coda del giorno senza id Classroom e non sospese (lo script non le ha create, e niente piano B).
    2. #169: buchi di più di 12 minuti tra due fotografie del cruscotto durante le ore di lezione (giri morti).
    3. #170: colonna «pratica» (allenamenti) vuota per tutti i presenti nell'ultima fotografia dei quiz.
    4. #164: più compiti «OGGI» del giorno su Classroom che blocchi di lezione della classe (un solo posto per i ragazzi).
    5. #163: 1INF, dispensa o pagina del piano senza arabo e cinese.
    6. #162: piano del laboratorio (2 ore o più) senza una proposta divisa ora per ora."""
    out = []
    g8 = giorno.replace("-", "")
    # 1. coda
    for f in glob.glob(os.path.join(ris, "coda", "%s_%s_*.json" % (giorno, classe.upper()))):
        try:
            q = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        st = str(q.get("stato", ""))
        if not q.get("coursework_id") and not st.startswith(("sospeso", "annullato", "superato", "in-attesa")):
            out.append("%s: %s in coda senza id Classroom e non sospeso (#168: script che non crea, piano B mancante)"
                       % (classe, os.path.basename(f)))
    # 2. giri del cruscotto
    for c in (classe.lower(), classe.upper()):
        d = os.path.join(ris, "storico", "cruscotti", c, giorno)
        if not os.path.isdir(d):
            continue
        tempi = sorted({t for t in (_hhmm_min(x) for x in os.listdir(d)) if t is not None})
        for l in ore:
            a, b = int(l["da"][:2]) * 60 + int(l["da"][3:5]), int(l["a"][:2]) * 60 + int(l["a"][3:5])
            dentro = [t for t in tempi if a <= t <= b]
            punti = [a + 5] + dentro + [b - 5]
            buchi = ["%02d:%02d-%02d:%02d" % (x // 60, x % 60, y // 60, y % 60)
                     for x, y in zip(punti, punti[1:]) if y - x > 12]
            if buchi:
                out.append("%s: giri del cruscotto fermi %s (#169)" % (classe, ", ".join(buchi)))
        break
    # 3. allenamenti vuoti
    for f in sorted(glob.glob(os.path.join(ris, "storico", "cruscotti", classe.lower(), giorno, "quiz-*.json")))[-1:]:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for i, col in enumerate(d.get("colonne", [])):
            if col.get("tipo") == "pratica" and d.get("righe") and \
                    not any((r.get("q") or [None] * (i + 1))[i] for r in d["righe"]):
                out.append("%s: colonna «%s» vuota per tutti i %d presenti: la consegna del ripasso non arriva (#170)"
                           % (classe, col.get("corta", col.get("etichetta")), len(d["righe"])))
    # 4. compiti «OGGI» del giorno
    try:
        v = json.load(open(os.path.join(ris, "dati", "verifiche-lezione", "%s_%s.json" % (giorno, classe)), encoding="utf-8"))
        gg = "%s/%s" % (giorno[8:10], giorno[5:7])
        oggi = [p for p in v.get("pezzi", []) if p.get("pezzo", "").startswith("compito «OGGI") and gg in p.get("pezzo", "")
                and p.get("dettaglio") == "PUBLISHED"]
        if len(oggi) > len(ore):
            out.append("%s: %d compiti «OGGI %s» pubblicati per %d blocchi di lezione: ai ragazzi un solo posto (#164)"
                       % (classe, len(oggi), gg, len(ore)))
    except Exception:
        pass
    # 5. tre lingue in 1INF
    if classe.upper() == "1INF":
        ar, zh = re.compile("[\u0600-\u06ff]"), re.compile("[\u4e00-\u9fff]")
        disp = glob.glob(os.path.join(pub, "docs", "dispense", "dispensa-1inf-v*.pdf"))
        for f in disp:
            ver = re.search(r"-v([\d.]+)\.pdf$", f).group(1)
            for lg in ("ar", "zh"):
                if not glob.glob(os.path.join(pub, "docs", "dispense", "dispensa-1inf-%s-v*.pdf" % lg)):
                    out.append("1INF: dispensa v%s senza la versione %s (#163)" % (ver, lg))
        for l in piano.get("link", []) if isinstance(piano, dict) else []:
            u = str(l.get("u", "")).split("?")[0]
            if not u.startswith("1inf") or any(x in u for x in ("oggi", "monitor", "prof", "avanzamento")):
                continue
            pg = os.path.join(pub, "docs", u, "index.html") if u.endswith("/") else os.path.join(pub, "docs", u)
            try:
                t = open(pg, encoding="utf-8").read()
            except Exception:
                continue
            if not ar.search(t) or not zh.search(t):
                out.append("1INF: pagina %s senza arabo o cinese (#163)" % u)
    # 7. #160: quiz del giorno che chiede il lavoro del laboratorio di oggi (non ancora fatto quando si fa il quiz)
    out.extend(_quiz_lavoro_futuro(classe, giorno, pub, ris))
    # 6. laboratorio diviso ora per ora
    for l in ore:
        if int(l["a"][:2]) - int(l["da"][:2]) >= 2 and isinstance(piano, dict):
            prop = [p for p in piano.get("proposte", []) if str(p.get("preferita")) == "True"
                    and re.search(r"laborat", str(p.get("titolo", "")), re.I)]
            for p in prop:
                if len(re.findall(r"\b[1-3]ª\s+ora\b", str(p.get("descrizione", "")))) < 2:
                    out.append("%s: proposta «%s» del laboratorio di %s-%s non divisa ora per ora (#162)"
                               % (classe, str(p.get("titolo", ""))[:50], l["da"], l["a"]))
    return out

def controlla_fine_giornata(giorno, pub=None, ris=None):
    """Controllore di fine giornata: per ogni classe in orario il giorno indicato, sul dato vero.
    1. compito su Classroom uscito entro la prima campanella (piano «pubblicata», #141) e piano senza bottoni dopo
       la pubblicazione (#144); 2. ultimo cruscotto: una riga per presente, nessun «null»/«None» nel testo, nessun 40 a
       chi ha finito o consegnato (#146, #156); 3. diario con le presenze; 4. report PDF di ogni ora (regola 24);
    5. domande all'assistente del giorno con risposta (regola 22, #145); 6. elenco di fine giornata
       report/<giorno>/non-andato.md scritto (#155). Restituisce l'elenco dei problemi."""
    pub, ris = pub or PUB, ris or RIS
    if not os.path.isdir(ris):
        giallo("fine giornata %s: riservato assente, controllo saltato" % giorno)
        return []
    try:
        lez = json.load(open(os.path.join(pub, "docs", "avanzamento", "orario-lezioni.json"), encoding="utf-8"))["lezioni"].get(giorno) or []
    except Exception:
        lez = []
    if not lez:
        esito(True, "fine giornata %s: nessuna lezione" % giorno)
        return []
    problemi = []
    classi = {}
    for l in lez:
        classi.setdefault(l["classe"], []).append(l)
    rep = os.path.join(ris, "report", giorno)
    rep_files = os.listdir(rep) if os.path.isdir(rep) else []
    g8 = giorno.replace("-", "")
    for classe, ore in classi.items():
        da = min(l["da"] for l in ore)
        try:
            piano = json.load(open(os.path.join(pub, "docs", "cruscotto", "piano", "%s-%s.json" % (classe.lower(), giorno)), encoding="utf-8"))
        except Exception:
            piano = {}
        uscita = str(piano.get("pubblicata") or "")
        if not uscita:
            problemi.append("%s: il piano non dice quando il compito è uscito su Classroom (#144)" % classe)
        elif _uscita_dopo(uscita, da, giorno):
            problemi.append("%s: compito uscito su Classroom alle %s, dopo la campanella delle %s (#141)" % (classe, uscita, da))
        try:
            v = json.load(open(os.path.join(ris, "dati", "verifiche-lezione", "%s_%s.json" % (giorno, classe)), encoding="utf-8"))
            if v.get("esito") != "VERDE":
                problemi.append("%s: verifica della lezione %s" % (classe, v.get("esito")))
        except Exception:
            problemi.append("%s: manca dati/verifiche-lezione/%s_%s.json" % (classe, giorno, classe))
        n_pres = _presenti_diario(ris, classe, giorno)
        if n_pres is None:
            problemi.append("%s: presenze assenti in diario/%s/%s.md" % (classe, classe, giorno))
        cr = _ultimo_cruscotto(ris, classe, giorno)
        if not cr:
            problemi.append("%s: nessuna fotografia del cruscotto in storico/cruscotti" % classe)
        else:
            try:
                d = json.load(open(cr, encoding="utf-8"))
                righe_c = d.get("righe") if isinstance(d, dict) else d
                righe_c = righe_c if isinstance(righe_c, list) else []
                if n_pres is not None and len(righe_c) != n_pres:
                    problemi.append("%s: cruscotto con %d righe, presenti %d (%s)" % (classe, len(righe_c), n_pres, os.path.basename(cr)))
                testi = re.findall(r'"((?:[^"\\]|\\.)*)"', json.dumps(d, ensure_ascii=False))
                if any(re.search(r"\bnull\b|\bNone\b|undefined|NaN", s) for s in testi):
                    problemi.append("%s: «null» o «None» scritto nel cruscotto (#146)" % classe)
                quaranta = 0
                for r in righe_c:
                    s = json.dumps(r, ensure_ascii=False)
                    if isinstance(r, dict) and r.get("voto") == 40 and ('"finito": true' in s or "CONSEGNATO" in s):
                        quaranta += 1
                if quaranta:
                    problemi.append("%s: %d allievi con voto 40 pur avendo finito o consegnato (#156)" % (classe, quaranta))
            except Exception as e:
                problemi.append("%s: cruscotto %s illeggibile (%s)" % (classe, os.path.basename(cr), e))
        mancano_pdf = []
        for l in ore:
            h0, h1 = int(l["da"][:2]), int(l["a"][:2])
            for h in range(h0, h1):
                nome = "%s_%s_ore-%02d-%02d_report.pdf" % (g8, classe, h, h + 1)
                if nome not in rep_files:
                    mancano_pdf.append("%02d-%02d" % (h, h + 1))
        if mancano_pdf:
            problemi.append("%s: report PDF dell'ora mancante (regola 24): %s" % (classe, ", ".join(mancano_pdf)))
        # 30/10/2026 (controllore di fine giornata, #162-#170): controlli nati dagli errori del 30/10
        problemi.extend(_controlli_30_10(classe, ore, giorno, pub, ris, piano))
    # domande all'assistente del giorno (regola 22)
    senza = 0
    tot = 0
    for f in glob.glob(os.path.join(ris, "dati", "verifiche", "assistente-*", "arrivi", "*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if d.get("modo") != "domanda":
            continue
        o = d.get("ora") or d.get("_arrivo") or ""
        try:
            t0 = datetime.datetime.fromisoformat(o.replace("Z", "+00:00"))
            t0 = t0.astimezone(ROMA) if ROMA else t0
        except Exception:
            continue
        if t0.date().isoformat() != giorno:
            continue
        tot += 1
        pag = str(d.get("id", "")).replace("assistente-", "")
        try:
            risp = json.load(open(os.path.join(pub, "docs", "assistente", "risposte", pag + ".json"), encoding="utf-8"))
        except Exception:
            risp = []
        nome = (d.get("nome") or "").strip().lower().split(" ")[0]
        q = (d.get("domanda") or "").strip()[:30].lower()
        ok = any((r.get("risposta") or "").strip() and (
                 (q and (r.get("domanda") or "").strip()[:30].lower() == q) or
                 (nome and (r.get("nome") or "").strip().lower().startswith(nome))) for r in risp if isinstance(r, dict))
        if not ok:
            senza += 1
    if senza:
        problemi.append("domande all'assistente del %s senza risposta: %d su %d (regola 22)" % (giorno, senza, tot))
    if not os.path.isfile(os.path.join(rep, "non-andato.md")):
        problemi.append("manca report/%s/non-andato.md: il controllo di fine giornata non è stato fatto (#155)" % giorno)
    esito(not problemi, "fine giornata %s (%s)" % (giorno, ", ".join(classi)) + (": " + "; ".join(problemi) if problemi else ""))
    return problemi


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
    a.add_argument("--fine-giornata", default=None, help="AAAA-MM-GG: fa solo il controllo di fine giornata")
    args = a.parse_args()
    adesso = datetime.datetime.now(ROMA) if ROMA else datetime.datetime.now()
    if args.fine_giornata:
        controlla_fine_giornata(args.fine_giornata)
        return stampa([])
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
    controlla_formato_json()
    controlla_coppie_docente_ragazzi()
    controlla_ponte_quiz(giorno=oggi)
    controlla_sicurezza_pronta(oggi)
    ieri = (datetime.date.fromisoformat(oggi) - datetime.timedelta(days=1)).isoformat()
    controlla_fine_giornata(ieri)   # 29/10/2026 sera: la giornata precedente, sul dato vero
    controlla_privacy()
    return stampa(da_sapere)


if __name__ == "__main__":
    sys.exit(main())
