# -*- coding: utf-8 -*-
"""Controlla un'EDIZIONE della comunicazione e dell'Atlante (comunicazione-marketing/EDIZIONE.json).
Dice «TUTTO A POSTO» solo se:
  1. ogni parte ha la versione scritta nel suo sorgente uguale a quella dell'edizione, e i suoi file esistono;
  2. tutti i link partendo dall'Atlante, dal parco, dalla pagina e dal racconto portano a un file che esiste;
  3. tutti i link dentro i PDF portano a un file che esiste;
  4. nelle parti pubbliche non ci sono nomi di ragazzi, nome della scuola o della città, marchi di altri;
  5. l'impronta delle parti è uguale a quella scritta nell'edizione (se no: qualcosa è cambiato, si sale di edizione).
Con --browser apre anche ogni pagina in Chromium (telefono e computer) e fa correre il racconto con una voce simulata.
Uso: python3 strumenti/controlla_edizione.py [--browser] [--fissa]   (--fissa scrive l'impronta nell'edizione)"""
import glob, hashlib, json, os, re, subprocess, sys

QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://nicolaregge-pulse.github.io/corso-informatica/"
MARCHI = r"gardaland|mikrotik|winbox|routeros|google|github|gemini|claude|godot|classroom|veyon|subaru|didaweb|notebooklm|piamarta|milano"
ESTERNI_NOTI = {"mailto:nicola.regge@gmail.com", "https://chasedeleon.github.io/automa-meteo-python/", "https://nicolaregge-pulse.github.io/firewall-virtuale/"}
os.chdir(QUI)
E = json.load(open("comunicazione-marketing/EDIZIONE.json", encoding="utf-8"))
problemi, avvisi = [], []

def versione_sorgente(fonte):
    f, tipo = fonte
    s = open(f, encoding="utf-8").read()
    pat = {"md": r"\*\*Versione (\d+\.\d+)\*\*", "meta": r'<meta name="versione" content="(\d+\.\d+)">',
           "VER": r'^VER = "(\d+\.\d+)"', "VERS_PARCO": r'^VERS_PARCO = "(\d+\.\d+)"'}[tipo]
    m = re.search(pat, s, re.M)
    return m.group(1) if m else None

def file_parte(p):
    out = []
    for f in p["file"]:
        out += sorted(glob.glob(f.replace("{v}", p["versione"]))) or [f.replace("{v}", p["versione"]) + " (MANCA)"]
    return out

# 1. versioni e file
for p in E["parti"]:
    v = versione_sorgente(p["fonte"])
    if v != p["versione"]:
        problemi.append(f"{p['nome']}: nel sorgente c'è la versione {v}, nell'edizione {p['versione']}")
    for f in file_parte(p):
        if f.endswith("(MANCA)"): problemi.append(f"{p['nome']}: manca il file {f[:-8]}")

# 2. link dalle pagine
GH = "https://github.com/nicolaregge-pulse/corso-informatica/blob/main/"
def locale(h, da):
    if h.startswith(GH): return h[len(GH):]          # documenti del prof: il file deve esistere nel repository
    if h.startswith(BASE): loc = "docs/" + h[len(BASE):]
    elif h.startswith(("http", "mailto:")): return None
    else: loc = os.path.normpath(os.path.join(os.path.dirname(da), h))
    loc = loc.split("?")[0]
    if loc.endswith("/") or os.path.isdir(loc): loc = os.path.join(loc, "index.html")
    return loc
PAGINE = ["docs/atlante-k4x9w2/index.html", "docs/cm-qma7yay4q5/index.html", "docs/cm-qma7yay4q5/progetti/index.html", "docs/cm-qma7yay4q5/parco/index.html", "docs/cm-qma7yay4q5/racconto/index.html"]
esterni, n_link, interne = set(), 0, set()
for pg in PAGINE:
    s = open(pg, encoding="utf-8").read()
    for h in re.findall(r'(?:href|src)="([^"#]+)"', s) + re.findall(r"img: '([^']+)'", s):
        if "' +" in h: continue
        n_link += 1
        loc = locale(h, pg)
        if loc is None: esterni.add(h); continue
        if not os.path.exists(loc): problemi.append(f"link rotto in {pg}: {h}")
        elif loc.endswith(".html"): interne.add(loc[5:].replace("index.html", "") + ("?" + h.split("?")[1] if "?" in h else ""))

# 3. link nei PDF
try:
    from pypdf import PdfReader
    for p in E["parti"]:
        for f in file_parte(p):
            if not f.endswith(".pdf") or not os.path.exists(f): continue
            for pagina in PdfReader(f).pages:
                for a in pagina.get("/Annots") or []:
                    A = a.get_object().get("/A")
                    if A and A.get("/URI"):
                        h = str(A["/URI"]); n_link += 1; loc = locale(h, f)
                        if loc is None: esterni.add(h)
                        elif not os.path.exists(loc): problemi.append(f"link rotto nel PDF {os.path.basename(f)}: {h}")
except ImportError:
    avvisi.append("pypdf non c'è: i link dentro i PDF non sono stati controllati")
for h in sorted(h for h in esterni - ESTERNI_NOTI if not h.startswith("mailto:nicola.regge@gmail.com")):
    avvisi.append(f"link esterno da provare a mano (dal container non si raggiunge): {h[:80]}")

# 4. contenuti delle parti pubbliche: nomi dei ragazzi, scuola, città, marchi
def testo(f):
    if f.endswith(".pdf"):
        from pypdf import PdfReader
        return " ".join((x.extract_text() or "") for x in PdfReader(f).pages)
    if re.search(r"\.(jpg|png|webp)$", f): return ""
    return open(f, encoding="utf-8").read()
nomi = set()
riservato = os.path.join(os.path.dirname(QUI), "corso-informatica-riservato", "generatori", "build_chiudi_1inf_full.py")
if os.path.exists(riservato):
    src = open(riservato, encoding="utf-8").read(); ns = {}
    exec(re.search(r"ROSTER=\{.*?\n\}", src, re.S).group(0), ns)
    for v in ns["ROSTER"].values():
        nomi |= {t.lower() for t in v[0].split() if len(t) > 3}
    nomi |= {"chase", "giulian", "deleon", "alvarez", "bettinelli", "acevedo"}
else:
    avvisi.append("elenco delle classi non trovato (repository riservato): i nomi dei ragazzi non sono stati cercati")
for p in E["parti"]:
    for f in file_parte(p):
        if not os.path.exists(f): continue
        t = re.sub(r"https?://\S+", "", testo(f)).lower()
        t = re.sub(r"<script.*?</script>", "", t, flags=re.S) if f.endswith(".html") and p["id"] != "racconto" else t
        if p["pubblica"]:
            m = sorted(set(re.findall(MARCHI, t)))
            if p["id"] == "racconto":      # nel codice della voce si cerca una voce italiana per nome (Google, Alice…): non è testo
                m = [x for x in m if x != "google"]
            if m: problemi.append(f"{p['nome']} ({os.path.basename(f)}): nomi da togliere {m}")
        t2 = re.sub(r"sala di controllo|sala giochi", "", t)   # «sala» è anche una parola comune
        hit = sorted(n for n in nomi if re.search(r"\b" + re.escape(n) + r"\b", t2))
        if hit and p["pubblica"]: problemi.append(f"{p['nome']} ({os.path.basename(f)}): possibili nomi di ragazzi {hit}")

# 5. impronta
h = hashlib.sha256()
for p in E["parti"]:
    for f in file_parte(p):
        if os.path.exists(f): h.update(f.encode()); h.update(open(f, "rb").read())
impronta = h.hexdigest()[:10]

# 6. prova nel browser
if "--browser" in sys.argv:
    elenco = "/tmp/pagine-edizione.txt"; open(elenco, "w").write("\n".join(sorted(interne)))
    server = subprocess.Popen([sys.executable, "-m", "http.server", "8799"], cwd=os.path.join(QUI, "docs"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import time; time.sleep(1)
    r = subprocess.run(["node", os.path.join(QUI, "strumenti", "controlla_edizione.js"), elenco], capture_output=True, text=True,
                       env=dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()))
    for riga in r.stdout.splitlines():
        if riga.startswith("KO"): problemi.append("browser: " + riga[3:])
    server.terminate()
    if r.returncode: problemi.append("browser: prova non riuscita " + r.stderr[-200:])
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "browser: nessuna uscita")

print(f"Edizione {E['edizione']} del {E['data']} · {len(E['parti'])} parti · {n_link} link controllati · impronta {impronta}")
for p in E["parti"]: print(f"   {p['nome']}: versione {p['versione']}")
for a in avvisi: print("   avviso:", a)
if "--fissa" in sys.argv and not problemi:
    E["impronta"] = impronta
    json.dump(E, open("comunicazione-marketing/EDIZIONE.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Impronta scritta nell'edizione.")
elif E.get("impronta") and E["impronta"] != impronta:
    problemi.append(f"le parti sono cambiate dopo l'edizione {E['edizione']} (impronta {E['impronta']} → {impronta}): sali di edizione")
if problemi:
    print("DA SISTEMARE:"); [print("   " + x) for x in problemi]; sys.exit(1)
print(f"TUTTO A POSTO · edizione {E['edizione']} · impronta {impronta}")
