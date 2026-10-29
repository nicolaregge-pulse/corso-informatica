#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDIT END-TO-END del flusso del corso (29/10/2026, REGISTRO-ERRORI #133-#146).

Percorre il flusso VERO dall'inizio alla fine e per ogni anello dice VERDE / ROSSO / ROSSO-NON-VERIFICABILE con la
PROVA (che cosa ha visto, ora del dato). Mai «verde» perché un file esiste soltanto.

Uso (una riga):
    python3 /home/user/corso-informatica/strumenti/audit_e2e.py [AAAA-MM-GG]
Senza data: il giorno di lezione di oggi se la lezione non è finita, altrimenti il prossimo giorno di lezione.

Anelli:
  1 Preparazione: docs/cruscotto/piano/<classe>-<data>.json su origin/main per ogni classe in orario, >=3 proposte
    (1 se la classe quel giorno ha solo Sicurezza); 4TI il martedì.
  2 Sito: l'ultimo giro «Pages» riuscito contiene l'ultimo commit che tocca docs/; download di github.io.
  3 Rendering: Playwright (strumenti/audit_e2e_pagina.js) sul cruscotto servito dai file del commit pubblicato,
    390 px, modalità Docente con il codice vero: piano con proposte e «Scelgo questa», ora e giorno del dato delle
    altre linguette, nessun errore JS.
  4 Canale docente: «scelta» vera via doPost sul canale docente-prova, arrivo nel riservato entro 10 minuti,
    riconosciuta da strumenti/aspetta_scelta.sh.
  5 Classroom: comando del ponte (classroom.compiti, classroom.annunci, classroom.consegne: SOLA LETTURA) per ogni
    classe; compito del giorno PUBLISHED e senza scadenza (regola 27); generatori/verifica_lezione.py VERDE
    (sul risultato dello stesso comando, --da-file); comandi del ponte «da-eseguire» da più di 10 minuti = ROSSO.
  6 Dati dei ragazzi: per 2 allievi per classe la consegna su Classroom = quello che mostra il cruscotto (JSON
    cifrato decifrato con strumenti/cifra_json.py).
  7 Domande: domanda di prova all'assistente (pagina cruscotto-<classe>-prova), arrivo nel riservato e presenza
    nella linguetta «Domande dei ragazzi» dopo generatori/domande_cruscotto.py.
Esito: dati/audit-e2e/<AAAA-MM-GG>_<HHMM>.json nel riservato (commit e push). Prima riga: «AUDIT E2E: VERDE» solo se
TUTTI gli anelli sono VERDI, altrimenti «AUDIT E2E: ROSSO (n): ...». Nessun nome di allievo sullo schermo.
Non crea né modifica compiti; scrive solo sui canali di PROVA.
"""
import base64, datetime, glob, hashlib, http.server, json, os, re, shutil, socket, ssl, subprocess, sys
import tempfile, threading, time, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

os.environ["TZ"] = "Europe/Rome"   # date dei commit (format-local) in ora di Roma
time.tzset()

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIS = os.path.join(os.path.dirname(PUB), "corso-informatica-riservato")
REPO = "nicolaregge-pulse/corso-informatica"
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
TZ = ZoneInfo("Europe/Rome")
V, R, NV = "VERDE", "ROSSO", "ROSSO-NON-VERIFICABILE"
ALIAS = {"4TI": "4INF"}
ATTESA = 10 * 60
sys.path.insert(0, os.path.join(PUB, "strumenti"))
import cifra_json  # noqa: E402

ADESSO = datetime.datetime.now(TZ)
OGGI = ADESSO.strftime("%Y-%m-%d")
TMP = tempfile.mkdtemp(prefix="audit-e2e-")
RUN = "audit-e2e-" + ADESSO.strftime("%Y%m%d-%H%M%S")


def sh(cmd, cwd=PUB, timeout=180, env=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str), capture_output=True, text=True, timeout=timeout, env=env)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "timeout"


def ora():
    return datetime.datetime.now(TZ).strftime("%H:%M:%S")


def peggiore(es):
    return R if R in es else NV if NV in es else V


def anello(n, nome, prove, esiti, extra=None):
    d = {"n": n, "nome": nome, "esito": peggiore(esiti) if esiti else R, "prove": prove, "ora": ora()}
    if not esiti:
        prove.append("nessun controllo eseguito")
    if extra:
        d.update(extra)
    return d


def ctx_ssl():
    for f in (os.environ.get("SSL_CERT_FILE"), "/root/.ccr/ca-bundle.crt"):
        if f and os.path.exists(f):
            return ssl.create_default_context(cafile=f)
    return ssl.create_default_context()


def scarica(url, dati=None, timeout=25):
    """(codice, corpo, errore). L'errore è il testo esatto (es. proxy 403)."""
    try:
        req = urllib.request.Request(url, data=dati, method="POST" if dati else "GET",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"} if dati else {})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx_ssl()) as r:
            return r.status, r.read(2_000_000), None
    except urllib.error.HTTPError as e:
        return e.code, b"", "HTTP %s %s" % (e.code, e.reason)
    except Exception as e:
        return None, b"", "%s: %s" % (type(e).__name__, e)


def bloccato(err):
    return bool(err) and bool(re.search(r"Tunnel connection failed|403|407|CONNECT|Forbidden|Name or service|timed out|refused", err))


def git_show(rev, path):
    rc, out = sh(["git", "show", "%s:%s" % (rev, path)])
    return out if rc == 0 else None


def pull_ris():
    return sh(["git", "pull", "-q", "--rebase", "--autostash"], cwd=RIS, timeout=120)[0] == 0


def push_ris(files, msg):
    sh(["git", "add"] + files, cwd=RIS)
    sh(["git", "commit", "-q", "-m", msg, "--"] + files, cwd=RIS)
    for _ in range(4):
        if sh(["git", "push", "-q"], cwd=RIS, timeout=120)[0] == 0:
            return True
        time.sleep(3)
        pull_ris()
    return False


# ------------------------------------------------------------------ orario

def orario():
    sh(["git", "fetch", "-q", "origin", "main"])
    t = git_show("origin/main", "docs/avanzamento/orario-lezioni.json")
    try:
        return json.loads(t)["lezioni"]
    except Exception:
        return json.load(open(os.path.join(PUB, "docs/avanzamento/orario-lezioni.json"), encoding="utf-8"))["lezioni"]


def giorno_predefinito(lez):
    oggi = lez.get(OGGI) or []
    if oggi and ADESSO.strftime("%H:%M") < max(v.get("a", "14:00") for v in oggi):
        return OGGI
    dopo = sorted(g for g in lez if g > OGGI)
    return dopo[0] if dopo else OGGI


def classi_del_giorno(lez, data):
    c = {}
    for v in lez.get(data) or []:
        c.setdefault(v["classe"], []).append(v.get("disciplina", ""))
    return c


# ------------------------------------------------------------------ anello 1

def anello1(data, classi):
    prove, es = [], []
    if not classi:
        return anello(1, "Preparazione", ["l'orario non ha lezioni il %s" % data], [R])
    if datetime.date.fromisoformat(data).weekday() == 1 and "4TI" not in classi:
        prove.append("martedì %s: l'orario non ha la 4TI" % data); es.append(R)
    _, ls = sh(["git", "ls-tree", "--name-only", "origin/main", "docs/cruscotto/piano/"])
    su_main = set(ls.split())
    for c, disc in classi.items():
        minimo = 1 if all("sicurezza" in (x or "").lower() for x in disc) else 3
        f = "docs/cruscotto/piano/%s-%s.json" % (c.lower(), data)
        if f not in su_main:
            locale = os.path.exists(os.path.join(PUB, f))
            prove.append("%s: %s assente su origin/main%s" % (c, os.path.basename(f), " (c'è solo in locale, non pushato)" if locale else ""))
            es.append(R); continue
        try:
            p = json.loads(git_show("origin/main", f))
        except Exception as e:
            prove.append("%s: piano illeggibile (%s)" % (c, e)); es.append(R); continue
        n = len(p.get("proposte") or [])
        _, quando = sh(["git", "log", "-1", "--format=%h %cd", "--date=format-local:%d/%m %H:%M", "origin/main", "--", f])
        ok = n >= minimo and p.get("giorno") == data and str(p.get("classe", "")).upper() == c
        prove.append("%s: %d proposte (minimo %d), giorno %s, commit %s" % (c, n, minimo, p.get("giorno"), quando.strip()))
        es.append(V if ok else R)
    return anello(1, "Preparazione", prove, es, {"classi": list(classi)})


# ------------------------------------------------------------------ anello 2

def anello2(data, classi):
    prove, es = [], []
    _, docs_sha = sh(["git", "log", "-1", "--format=%H", "origin/main", "--", "docs"])
    docs_sha = docs_sha.strip()
    _, docs_t = sh(["git", "log", "-1", "--format=%cd", "--date=format-local:%d/%m %H:%M", docs_sha])
    rc, b = sh(["gh", "api", "repos/%s/pages/builds/latest" % REPO], timeout=60)
    pub_sha = None
    if rc == 0:
        try:
            j = json.loads(b); pub_sha = j.get("commit") if j.get("status") == "built" else None
            prove.append("pages/builds/latest: %s commit %s" % (j.get("status"), (j.get("commit") or "")[:7]))
        except Exception:
            pass
    else:
        prove.append("pages/builds/latest non leggibile: %s" % re.sub(r"\s+", " ", b)[:90])
    rc, b = sh(["gh", "api", "repos/%s/actions/runs?per_page=40" % REPO], timeout=60)
    try:
        runs = [r for r in json.loads(b)["workflow_runs"] if "Pages" in r.get("name", "")]
    except Exception:
        runs = []
    ok_runs = [r for r in runs if r["status"] == "completed" and r["conclusion"] == "success"]
    if not pub_sha and ok_runs:
        pub_sha = ok_runs[0]["head_sha"]
        t = datetime.datetime.fromisoformat(ok_runs[0]["updated_at"].replace("Z", "+00:00")).astimezone(TZ)
        prove.append("ultimo giro Pages riuscito (actions/runs): %s alle %s" % (pub_sha[:7], t.strftime("%d/%m %H:%M")))
    if not pub_sha:
        prove.append("stato di GitHub Pages non leggibile"); es.append(NV)
    else:
        if docs_sha and sh(["git", "merge-base", "--is-ancestor", docs_sha, pub_sha])[0] == 0:
            prove.append("ultimo commit su docs/ %s (%s) è pubblicato" % (docs_sha[:7], docs_t.strip())); es.append(V)
        else:
            corso = [r for r in runs if r["head_sha"] == docs_sha]
            prove.append("ultimo commit su docs/ %s (%s) NON pubblicato (giro: %s)" % (
                docs_sha[:7], docs_t.strip(), (corso[0]["status"] + " " + (corso[0]["conclusion"] or "")) if corso else "nessuno"))
            es.append(R)
    # download dal sito vero
    piani = [("cruscotto/piano/%s-%s.json" % (c.lower(), data)) for c in classi] or ["cruscotto/chiave.json"]
    for rel in ["cruscotto/", piani[0]]:
        code, corpo, err = scarica(SITO + rel)
        if err:
            prove.append("%s%s: %s" % (SITO, rel, err)); es.append(NV if bloccato(err) and code is None else R)
        else:
            atteso = git_show(pub_sha or "origin/main", "docs/" + (rel + "index.html" if rel.endswith("/") else rel))
            uguale = atteso is not None and corpo.decode("utf-8", "replace").strip() == atteso.strip()
            prove.append("%s: HTTP %s, %s" % (rel, code, "uguale al commit pubblicato" if uguale else "DIVERSO dal commit pubblicato"))
            es.append(V if uguale else R)
    return anello(2, "Sito", prove, es), pub_sha


# ------------------------------------------------------------------ anello 3

def tok_docente():
    try:
        t = json.load(open(os.path.join(RIS, "config/compito-unico-docente.json"), encoding="utf-8"))["password"]
        return t if cifra_json.decifra(json.load(open(os.path.join(PUB, "docs/cruscotto/chiave.json")))).get("ok") == 1 else ""
    except Exception:
        return ""


def server(cartella):
    s = socket.socket(); s.bind(("127.0.0.1", 0)); porta = s.getsockname()[1]; s.close()

    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=cartella, **k)

        def log_message(self, *a):
            pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", porta), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, "http://127.0.0.1:%d/" % porta


DATA_RE = re.compile(r"\b(\d{1,2})/(\d{1,2})(?:/(\d{4}))?\b")
ORA_RE = re.compile(r"(aggiornat\w*|dati letti|letti il|letto alle|dati da|conteggio delle|controllo delle|ultimo dato|ultimo alle)\D{0,30}?(?:(\d{1,2}/\d{1,2}(?:/\d{4})?)\D{0,6}?)?(\d{1,2}[:.]\d{2})", re.I)


def freschezza(testo, file_oggi):
    """(esito, prova): ora del dato e giorno del dato."""
    if not testo.strip():
        return R, "linguetta vuota"
    if re.search(r"Scrivi il codice|Codice sbagliato|codice del monitor", testo):
        return R, "chiede di nuovo il codice del docente: «%s»" % testo[:70]
    m = ORA_RE.search(testo)
    if not m:
        return R, "nessuna ora del dato nella linguetta («%s»)" % testo[:70]
    snippet = testo[m.start(): m.end()].strip()
    oggi_dm = (int(OGGI[8:10]), int(OGGI[5:7]))
    if m.group(2):
        d = DATA_RE.match(m.group(2))
        di_oggi = (int(d.group(1)), int(d.group(2))) == oggi_dm
        return (V if di_oggi else R), "«%s»%s" % (snippet, "" if di_oggi else ": il dato NON è di oggi")
    if re.search(r"\boggi\b", testo[max(0, m.start() - 60): m.end()], re.I):
        return V, "«%s» (detto «oggi»)" % snippet
    if file_oggi:
        return V, "«%s» senza giorno; il file del dato (%s) è del commit di oggi" % (snippet, file_oggi)
    return R, "«%s»: l'ora non dice il giorno e il file del dato non è di oggi" % snippet


def anello3(data, classi, pub_sha, piani):
    prove, es, extra = [], [], {}
    rev = pub_sha or "origin/main"
    sito = os.path.join(TMP, "sito")
    os.makedirs(sito, exist_ok=True)
    rc, out = sh("git archive %s docs | tar -x -C %s" % (rev, sito))
    if rc != 0:
        return anello(3, "Rendering", ["git archive non riuscito: %s" % out[:200]], [R]), {}
    docs = os.path.join(sito, "docs")
    srv, base = server(docs)
    tok = tok_docente()
    cfg = {"base": base, "sito_dir": docs, "tok": tok, "prova": not tok, "data": data, "oggi": OGGI,
           "classi": [{"classe": c, "titoli": [x.get("titolo", "") for x in (piani.get(c) or {}).get("proposte", [])]} for c in classi]}
    prove.append("cruscotto servito dai file del commit %s, 390 px, modalità Docente, %s" % (
        rev[:7], "codice del docente vero (dal riservato)" if tok else "SENZA codice: ?prova=1"))
    if not tok:
        es.append(R)
    fc, fo = os.path.join(TMP, "pagina-cfg.json"), os.path.join(TMP, "pagina-out.json")
    json.dump(cfg, open(fc, "w"))
    env = dict(os.environ, NODE_PATH=os.environ.get("NODE_PATH", "/opt/node22/lib/node_modules"))
    rc, out = sh(["node", os.path.join(PUB, "strumenti/audit_e2e_pagina.js"), fc, fo], timeout=600, env=env)
    srv.shutdown()
    if rc != 0 or not os.path.exists(fo):
        return anello(3, "Rendering", prove + ["Playwright non è partito: %s" % out.strip()[-200:]], [R]), {}
    ris = json.load(open(fo))
    extra["pagina"] = ris
    bloccati = set()
    for r in ris["classi"]:
        c = r["classe"]
        if r.get("errore"):
            prove.append("%s: eccezione nel browser: %s" % (c, r["errore"][:150])); es.append(R); continue
        if tok and not r.get("codice_docente_accettato"):
            prove.append("%s: il codice del docente non è stato accettato (TOK_OK vuoto)" % c); es.append(R)
        p = r["schede"].get("piano", {})
        props = (piani.get(c) or {}).get("proposte") or []
        if not props:
            prove.append("%s Piano %s: «%s»" % (c, data, p.get("testo", "")[:110])); es.append(R)
        else:
            pubbl = "PUBBLICATA alle" in p.get("testo", "")
            visti = len(p.get("titoli_visti") or [])
            ok = visti == len(props) and (p.get("scelgo", 0) >= 1 or pubbl)
            prove.append("%s Piano %s: %d/%d proposte visibili, «Scelgo questa» %d, «Pubblica» %d%s" % (
                c, data, visti, len(props), p.get("scelgo", 0), p.get("pubblica", 0), ", PUBBLICATA" if pubbl else ""))
            es.append(V if ok else R)
        # file JSON del dato caricati: sono del commit di oggi?
        file_oggi = ""
        for j in r.get("json") or []:
            u = j["url"]
            rel = None
            if u.startswith(base):
                rel = "docs/" + u[len(base):]
            elif "/main/" in u:
                rel = u.split("/main/", 1)[1]
            if not rel or not rel.startswith("docs/avanzamento/") or re.search(r"orario|indice|domande|uscite|riepilogo|criticita", rel):
                continue
            _, t = sh(["git", "log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d %H:%M", rev, "--", rel])
            if t.strip().startswith(OGGI):
                file_oggi = "%s, %s" % (os.path.basename(rel), t.strip()[11:])
        for t in ("oggi", "domande", "uscite", "script", "riepilogo"):
            s = r["schede"].get(t) or {}
            testo = s.get("testo", "")
            if t == "oggi" and re.search(r"NON di oggi", s.get("nota", "")):
                e, pr = R, "nota in rosso: «%s»" % s["nota"][:90]
            else:
                e, pr = freschezza(testo, file_oggi if t == "oggi" else "")
            if t == "script" and "non risponde" in testo:
                pr += "; lo script Google «non risponde» (script.google.com non raggiungibile da qui)"
            prove.append("%s %s: %s" % (c, t, pr)); es.append(e)
        if r.get("errori_js"):
            prove.append("%s: %d errori JS: %s" % (c, len(r["errori_js"]), r["errori_js"][0][:120])); es.append(R)
        else:
            prove.append("%s: nessun errore JS" % c)
        if (r.get("larghezza") or 0) > 400:
            prove.append("%s: pagina larga %d px a 390 px (scorre di lato)" % (c, r["larghezza"])); es.append(R)
        bloccati |= {re.sub(r"^https?://([^/]+).*", r"\1", u) for u in r.get("bloccati") or []}
    if bloccati:
        prove.append("host esterni non raggiungibili dal browser di prova (bloccati): %s" % ", ".join(sorted(bloccati)))
    return anello(3, "Rendering", prove, es), ris


# ------------------------------------------------------------------ anelli 4 e 7 (doPost)

def indirizzo_invio(rev):
    try:
        return json.loads(git_show(rev, "docs/verifica/config.json"))["invio"]
    except Exception:
        return ""


def manda(invio, d):
    return scarica(invio, ("d=" + urllib.parse.quote(json.dumps(d, ensure_ascii=False))).encode())


def aspetta_file(cartella, segno, minuti=10, tira=True):
    fine = time.time() + minuti * 60
    while time.time() < fine:
        if tira:
            pull_ris()
        for f in sorted(glob.glob(os.path.join(RIS, cartella, "*.json"))):
            try:
                if segno in open(f, encoding="utf-8").read():
                    return f
            except Exception:
                pass
        time.sleep(30)
    return None


def anello4(rev, data):
    prove, es = [], []
    invio = indirizzo_invio(rev)
    if not invio:
        return anello(4, "Canale docente", ["docs/verifica/config.json senza «invio»"], [R])
    tok = tok_docente()
    ora_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()[:23] + "Z"
    testo = "Scelgo la proposta 1: AUDIT E2E %s" % RUN
    d = {"id": "docente-prova", "nome": "Docente", "modo": "domanda", "classe": "PROVA", "giorno": data, "ora": ora_iso,
         "pagina": SITO + "cruscotto/?audit=" + RUN, "tipo": "scelta", "proposta": 1, "titolo": "AUDIT E2E " + RUN,
         "testo": testo, "domanda": testo, "firma": hashlib.sha256((tok + "|" + ora_iso).encode()).hexdigest()}
    # aspetta_scelta.sh parte PRIMA dell'invio (guarda i file più nuovi del suo avvio) e fa lui i git pull
    asp = subprocess.Popen(["bash", os.path.join(RIS, "strumenti/aspetta_scelta.sh"), "11"], cwd=RIS,
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    time.sleep(5)
    code, corpo, err = manda(invio, d)
    if err and code is None:
        asp.kill()
        prove.append("POST %s…: %s" % (invio[:45], err))
        return anello(4, "Canale docente", prove, [NV if bloccato(err) else R])
    prove.append("POST della scelta: HTTP %s %s" % (code, "Consegna arrivata" if b"arrivat" in corpo else (err or "")))
    t0 = time.time()
    f = aspetta_file("dati/verifiche/docente-prova/arrivi", RUN, 10, tira=False)
    if f:
        prove.append("arrivata nel riservato in %d s: %s" % (time.time() - t0, os.path.relpath(f, RIS))); es.append(V)
    else:
        prove.append("NON arrivata in dati/verifiche/docente-prova/arrivi/ entro 10 minuti"); es.append(R)
    try:
        out, _ = asp.communicate(timeout=60 * 12)
    except subprocess.TimeoutExpired:
        asp.kill(); out = ""
    out = (out or "").strip()
    if out.startswith("SCELTA") and RUN in out:
        prove.append("aspetta_scelta.sh: «%s»" % out[:80]); es.append(V)
    else:
        prove.append("aspetta_scelta.sh NON l'ha riconosciuta: «%s»" % out[:80]); es.append(R)
    return anello(4, "Canale docente", prove, es)


def domande_generate(classe, prova):
    """Esegue generatori/domande_cruscotto.py (genera) scrivendo in una cartella temporanea, non nel sito."""
    sys.path.insert(0, os.path.join(RIS, "generatori"))
    import importlib
    m = importlib.import_module("domande_cruscotto")
    preso = {}
    m.scrivi_cifrato = lambda dest, obj: preso.update({"dest": dest, "obj": obj})
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        m.genera(classe, 14)
    return preso


def anello7(rev, classi):
    prove, es = [], []
    c = (list(classi) or ["1INF"])[0].lower()
    pagina = "cruscotto-%s-prova" % c
    invio = indirizzo_invio(rev)
    d = {"id": "assistente-" + pagina, "nome": "Audit E2E", "modo": "domanda", "domanda": "Domanda di prova %s: funziona?" % RUN,
         "pagina": SITO + "cruscotto/?prova=1&audit=" + RUN, "ora": datetime.datetime.now(datetime.timezone.utc).isoformat()[:23] + "Z"}
    code, corpo, err = manda(invio, d) if invio else (None, b"", "nessun indirizzo invio")
    arrivata = None
    if err and code is None:
        prove.append("POST della domanda (pagina %s): %s" % (pagina, err)); es.append(NV if bloccato(err) else R)
    else:
        prove.append("POST della domanda: HTTP %s" % code)
        arrivata = aspetta_file("dati/verifiche/assistente-%s/arrivi" % pagina, RUN, 10)
        if arrivata:
            prove.append("arrivata: %s" % os.path.relpath(arrivata, RIS)); es.append(V)
        else:
            prove.append("NON arrivata in dati/verifiche/assistente-%s/arrivi/ entro 10 minuti" % pagina); es.append(R)
    # che cosa farebbe domande_cruscotto.py con una domanda di PROVA (anche se l'invio non è possibile da qui)
    try:
        g = domande_generate(c, True)
        dest = os.path.relpath(g.get("dest", "?"), PUB)
        L = (g.get("obj") or {}).get("domande") or []
        con_prova = [x for x in L if str(x.get("pagina", "")).endswith("-prova")]
        mia = [x for x in L if RUN in str(x.get("domanda", ""))]
        prove.append("domande_cruscotto.py (%s): scrive %s con %d domande, %d da pagine -prova%s" % (
            c.upper(), dest, len(L), len(con_prova), ", c'è quella dell'audit" if mia else ""))
        if not os.path.basename(dest).endswith("-prova.json"):
            prove.append("la linguetta in prova legge avanzamento/domande-%s-prova.json, che domande_cruscotto.py non scrive; "
                         "le caselle «-prova» vengono saltate: una domanda di prova non arriva mai nella linguetta" % c)
            es.append(R)
        elif arrivata and not mia:
            es.append(R)
    except Exception as e:
        prove.append("domande_cruscotto.py non eseguibile: %s" % e); es.append(R)
    _, t = sh(["git", "log", "-1", "--format=%cd", "--date=format-local:%d/%m %H:%M", rev or "origin/main", "--",
               "docs/avanzamento/domande-%s-prova.json" % c])
    prove.append("domande-%s-prova.json nel sito: ultimo commit %s" % (c, t.strip() or "mai"))
    return anello(7, "Domande", prove, es)


# ------------------------------------------------------------------ anelli 5 e 6 (ponte)

def coda_del(classe, giorno):
    out = []
    for f in sorted(glob.glob(os.path.join(RIS, "coda", "%s_%s_*.json" % (giorno, classe))) +
                    glob.glob(os.path.join(RIS, "coda", "archivio", "%s_%s_*.json" % (giorno, classe)))):
        try:
            d = json.load(open(f, encoding="utf-8"))
            if d.get("coursework_id"):
                out.append(d)
        except Exception:
            pass
    return out


def manda_comandi(classi):
    pull_ris()
    inviati = {}
    for c in classi:
        cl = ALIAS.get(c, c)
        coda = coda_del(c, OGGI)
        azioni = [{"tipo": "classroom.compiti", "classe": cl}, {"tipo": "classroom.annunci", "classe": cl}]
        if coda:
            azioni.append({"tipo": "classroom.consegne", "classe": cl, "coursework_id": str(coda[-1]["coursework_id"])})
        nome = "%s_%s-%s.json" % (OGGI, RUN, c.lower())
        rel = os.path.join("comandi", nome)
        json.dump({"stato": "da-eseguire", "nota": "%s audit_e2e.py %s: SOLA LETTURA (compiti, annunci, consegne)" % (
            ADESSO.strftime("%d/%m %H:%M"), c), "azioni": azioni}, open(os.path.join(RIS, rel), "w", encoding="utf-8"),
            ensure_ascii=False, indent=1)
        inviati[c] = {"file": rel, "coursework": coda[-1]["coursework_id"] if coda else "", "titolo": coda[-1].get("titolo", "") if coda else ""}
    ok = push_ris([v["file"] for v in inviati.values()], "Audit E2E: comandi del ponte in sola lettura (%s)" % ", ".join(classi))
    return inviati, time.time(), ok


def aspetta_comandi(inviati, t0):
    risultati = {}
    while time.time() < t0 + ATTESA:
        pull_ris()
        for c, v in inviati.items():
            if c in risultati:
                continue
            for p in (v["file"], os.path.join("comandi", "archivio", os.path.basename(v["file"]))):
                try:
                    d = json.load(open(os.path.join(RIS, p), encoding="utf-8"))
                except Exception:
                    continue
                if d.get("stato") in ("eseguito", "errore"):
                    risultati[c] = (p, d)
        if len(risultati) == len(inviati):
            break
        time.sleep(30)
    return risultati


def dati_ris(d, tipo):
    for r in d.get("risultati") or []:
        if r.get("tipo") == tipo:
            return r.get("dati") if r.get("ok") else {"_errore": r.get("errore")}
    return None


def comandi_fermi():
    fermi = []
    for f in glob.glob(os.path.join(RIS, "comandi", "*.json")):
        try:
            if json.load(open(f, encoding="utf-8")).get("stato") != "da-eseguire":
                continue
        except Exception:
            continue
        _, t = sh(["git", "log", "--diff-filter=A", "--format=%ct", "-1", "--", os.path.relpath(f, RIS)], cwd=RIS)
        eta = (time.time() - int(t.strip())) / 60 if t.strip().isdigit() else None
        if eta is None or eta > 10:
            fermi.append("%s (%s)" % (os.path.basename(f), "mai committato" if eta is None else "da %d min" % eta))
    return fermi


def anello5(data, classi, inviati, ok_push, risultati):
    prove, es = [], []
    if not ok_push:
        prove.append("push dei comandi del ponte non riuscito"); es.append(R)
    for c in classi:
        v = inviati.get(c)
        if c not in risultati:
            prove.append("%s: comando %s ancora «da-eseguire» dopo 10 minuti" % (c, os.path.basename(v["file"]) if v else "?"))
            es.append(R); continue
        p, d = risultati[c]
        t = ((lambda x: x.astimezone(TZ).strftime("%H:%M"))(datetime.datetime.fromisoformat(d["eseguito_il"].replace("Z", "+00:00"))) if d.get("eseguito_il") else "?")
        compiti = dati_ris(d, "classroom.compiti")
        if not isinstance(compiti, list):
            prove.append("%s: classroom.compiti in errore: %s" % (c, str(compiti)[:120])); es.append(R); continue
        coda_ids = {str(x["coursework_id"]) for x in coda_del(c, data)}
        del_giorno = [w for w in compiti if str(w.get("id")) in coda_ids or
                      (w.get("programmato") or "")[:10] == data or
                      (lambda s: len(s) == 3 and "%04d-%02d-%02d" % (int(s[2]), int(s[1]), int(s[0])) == data)((w.get("scadenza") or "").split("/"))]
        prove.append("%s: ponte eseguito alle %s, %d compiti letti" % (c, t, len(compiti)))
        if not del_giorno:
            prove.append("%s: nessun compito del %s su Classroom (né in coda, né programmato, né con scadenza quel giorno)" % (c, data))
            es.append(R)
        for w in del_giorno:
            ok = w.get("stato") == "PUBLISHED" and not w.get("scadenza")
            prove.append("%s: «%s» %s, scadenza %s" % (c, str(w.get("titolo", ""))[:40], w.get("stato"), w.get("scadenza") or "nessuna"))
            es.append(V if ok else R)
        # verifica_lezione.py sullo stesso risultato del ponte (sola lettura, nessun nuovo comando)
        rc, out = sh(["python3", os.path.join(RIS, "generatori/verifica_lezione.py"), c, "--giorno", data,
                      "--da-file", os.path.join(RIS, p)], cwd=RIS, timeout=300)
        riga = (out.strip().splitlines() or ["(nessuna uscita)"])[-1]
        prove.append("%s: verifica_lezione.py → %s" % (c, riga[:160])); es.append(V if riga.startswith("VERDE") else R)
    fermi = comandi_fermi()
    if fermi:
        prove.append("comandi del ponte «da-eseguire» da più di 10 minuti: %s" % ", ".join(fermi[:5])); es.append(R)
    else:
        prove.append("nessun comando del ponte fermo da più di 10 minuti")
    return anello(5, "Classroom", prove, es)


def norm(n):
    return set(re.sub(r"[^a-zà-ü ]", " ", str(n).lower()).split())


def consegnato_cruscotto(cella):
    if isinstance(cella, dict):
        if "consegnato" in (cella.get("fatti") or []):
            return True
        if "consegnato" in (cella.get("manca") or []):
            return False
        if isinstance(cella.get("ok"), bool) and re.search(r"consegn", str(cella.get("t", "")), re.I):
            return cella["ok"]
    s = json.dumps(cella, ensure_ascii=False).lower()
    if re.search(r"non (ancora )?consegn|○", s):
        return False
    if re.search(r"consegnat|✔", s):
        return True
    return None


def anello6(classi, inviati, risultati, pagina, rev):
    prove, es, dettagli = [], [], []
    per_classe = {x["classe"]: x for x in (pagina or {}).get("classi", [])}
    for c in classi:
        v = inviati.get(c) or {}
        if c not in risultati:
            prove.append("%s: consegne non lette (ponte senza risposta)" % c); es.append(R); continue
        if not v.get("coursework"):
            prove.append("%s: nessun compito di oggi in coda: non so quale consegna confrontare" % c); es.append(R); continue
        cons = dati_ris(risultati[c][1], "classroom.consegne")
        if not isinstance(cons, list):
            prove.append("%s: classroom.consegne in errore: %s" % (c, str(cons)[:120])); es.append(R); continue
        # il file del cruscotto che la linguetta «Oggi dal vivo» ha caricato
        fonte, dati = None, None
        for j in (per_classe.get(c) or {}).get("json", []):
            u = j["url"]
            rel = ("docs/avanzamento/" + u.split("/avanzamento/", 1)[1]) if "/avanzamento/" in u else None
            if not rel or "orario" in rel or "indice" in rel or "domande" in rel or "uscite" in rel:
                continue
            try:
                d = json.loads(git_show(rev, rel) or "null")
                d = cifra_json.decifra(d) if isinstance(d, dict) and d.get("cifrato") else d
            except Exception:
                continue
            if isinstance(d, dict) and d.get("righe"):
                fonte, dati = rel, d
        if not dati:
            prove.append("%s: il cruscotto non ha caricato un file con le righe degli allievi" % c); es.append(R); continue
        col = dati.get("colonne") or []
        idx = max([i for i, t in enumerate(col) if re.search(r"document|quiz|consegn|compito", str(t), re.I)] or [-1])
        if idx < 0:
            prove.append("%s: nel cruscotto (%s) nessuna colonna della consegna su Classroom: %s" % (c, os.path.basename(fonte), col))
            es.append(R); continue
        righe = dati["righe"]
        classroom_si = [x for x in cons if x.get("stato") in ("TURNED_IN", "RETURNED")]
        classroom_no = [x for x in cons if x not in classroom_si]
        scelti = (classroom_si[:1] + classroom_no[:1]) if classroom_si and classroom_no else (classroom_si or classroom_no)[:2]
        prove.append("%s: compito «%s» su Classroom %d consegnati su %d; cruscotto %s colonna «%s» (ora del dato %s)" % (
            c, v.get("titolo", "")[:30], len(classroom_si), len(cons), os.path.basename(fonte), col[idx], dati.get("ora", "?")))
        for k, x in enumerate(scelti, 1):
            riga = next((r for r in righe if len(norm(r.get("nome")) & norm(x.get("nome"))) >= 2 or norm(r.get("nome")) == norm(x.get("nome"))), None)
            cr = x.get("stato") in ("TURNED_IN", "RETURNED")
            if not riga:
                prove.append("%s allievo %d: su Classroom %s, nel cruscotto NON c'è" % (c, k, x.get("stato"))); es.append(R)
                dettagli.append({"classe": c, "nome": x.get("nome"), "classroom": x.get("stato"), "cruscotto": None}); continue
            celle = riga.get("celle") or riga.get("col") or []
            cella = celle[idx] if idx < len(celle) else None
            cc = consegnato_cruscotto(cella)
            uguale = cc is not None and cc == cr
            prove.append("%s allievo %d: Classroom %s, cruscotto %s → %s" % (
                c, k, x.get("stato"), {True: "consegnato", False: "non consegnato", None: "non lo dice"}[cc], "coincide" if uguale else "NON coincide"))
            es.append(V if uguale else R)
            dettagli.append({"classe": c, "nome": x.get("nome"), "classroom": x.get("stato"), "cruscotto": cella})
        ultimo = sorted(glob.glob(os.path.join(RIS, "dati", "%s-*-%s.json" % (c.lower(), OGGI.replace("-", "")))), key=os.path.getmtime)
        if ultimo:
            prove.append("%s: ultimo file in dati/: %s" % (c, os.path.basename(ultimo[-1])))
    return anello(6, "Dati dei ragazzi", prove, es, {"dettagli": dettagli})


# ------------------------------------------------------------------ main

def main():
    lez = orario()
    data = sys.argv[1] if len(sys.argv) > 1 and re.fullmatch(r"\d{4}-\d\d-\d\d", sys.argv[1]) else giorno_predefinito(lez)
    classi = classi_del_giorno(lez, data)
    ris = []
    inviati, t0, ok_push = manda_comandi(list(classi))          # il ponte lavora mentre girano gli altri anelli
    piani = {}
    for c in classi:
        try:
            piani[c] = json.loads(git_show("origin/main", "docs/cruscotto/piano/%s-%s.json" % (c.lower(), data)) or "null") or {}
        except Exception:
            piani[c] = {}
    passi = []

    def prova(n, nome, f):
        try:
            return f()
        except Exception as e:
            import traceback
            return anello(n, nome, ["eccezione dell'audit: %s" % traceback.format_exc().strip().splitlines()[-1][:200]], [R])

    ris.append(prova(1, "Preparazione", lambda: anello1(data, classi)))
    a2 = prova(2, "Sito", lambda: anello2(data, classi))
    a2, pub = a2 if isinstance(a2, tuple) else (a2, None)
    ris.append(a2)
    a3 = prova(3, "Rendering", lambda: anello3(data, classi, pub, piani))
    a3, pagina = a3 if isinstance(a3, tuple) else (a3, {})
    ris.append(a3)
    rev = pub or "origin/main"
    a4 = prova(4, "Canale docente", lambda: anello4(rev, data))
    a7 = prova(7, "Domande", lambda: anello7(rev, classi))
    risultati = aspetta_comandi(inviati, t0)
    ris.append(prova(5, "Classroom", lambda: anello5(data, classi, inviati, ok_push, risultati)))
    ris.append(prova(6, "Dati dei ragazzi", lambda: anello6(classi, inviati, risultati, pagina, rev)))
    ris.insert(3, a4)
    ris.append(a7)
    ris.sort(key=lambda x: x["n"])
    rossi = [x for x in ris if x["esito"] != V]
    prima = "AUDIT E2E: VERDE" if not rossi else "AUDIT E2E: ROSSO (%d): %s" % (
        len(rossi), "; ".join("%d %s%s" % (x["n"], x["nome"], " NON VERIFICABILE" if x["esito"] == NV else "") for x in rossi))
    out = {"run": RUN, "data": data, "classi": list(classi), "ora": datetime.datetime.now(TZ).isoformat(timespec="seconds"),
           "esito": "VERDE" if not rossi else "ROSSO", "riga": prima, "commit_pubblicato": pub, "anelli": ris}
    rel = os.path.join("dati", "audit-e2e", "%s_%s.json" % (OGGI, ADESSO.strftime("%H%M")))
    pull_ris()
    os.makedirs(os.path.join(RIS, os.path.dirname(rel)), exist_ok=True)
    json.dump(out, open(os.path.join(RIS, rel), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    extra = [os.path.join("dati", "verifiche-lezione", "%s_%s.json" % (data, c)) for c in classi]
    extra = [x for x in extra if os.path.exists(os.path.join(RIS, x))]
    pushed = push_ris([rel] + extra, "Audit E2E %s (%s): %s" % (data, ADESSO.strftime("%H:%M"), out["esito"]))
    print(prima)
    for x in ris:
        print("%d %s: %s — %s" % (x["n"], x["nome"], x["esito"], " | ".join(x["prove"])[:600]))
    print("esito: %s%s" % (rel, "" if pushed else " (push NON riuscito)"))
    shutil.rmtree(TMP, ignore_errors=True)
    return 0 if not rossi else 2


if __name__ == "__main__":
    sys.exit(main())
