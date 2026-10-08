# Controllo automatico dei file del «Treno blindato» (gira da solo a ogni Pull Request).
import json, os, re, sys
ERR = []
COLORE = re.compile(r"^#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$")
VIETATI = re.compile(r"@|https?://|\b\d{6,}\b")
def leggi(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception as e:
        ERR.append(f"{p}: non è JSON valido ({e}). Controlla virgole e virgolette."); return None
def numero(p, d, k, a, b):
    if k in d and not (isinstance(d[k], (int, float)) and a <= d[k] <= b):
        ERR.append(f"{p}: «{k}» deve essere un numero da {a} a {b}.")
def colori(p, d, chiavi):
    for k in chiavi:
        if k in d and not COLORE.match(str(d[k])):
            ERR.append(f"{p}: «{k}» deve essere un colore come #ffd34d")
for f in sorted(os.listdir("cattivi")):
    p = os.path.join("cattivi", f)
    if f.startswith("pc00") or f.endswith(".md"): continue
    if f.endswith(".png"):
        if not re.fullmatch(r"pc(0[1-9]|[1-3]\d|40)\.png", f): ERR.append(f"{p}: l'immagine si chiama come il tuo PC, per esempio pc14.png")
        continue
    if not re.fullmatch(r"pc(0[1-9]|[1-3]\d|40)\.json", f):
        ERR.append(f"{p}: il nome del file è pc + numero del PC a due cifre, per esempio pc07.json"); continue
    d = leggi(p)
    if d is None: continue
    for k in ("nome", "colore", "occhi", "cappello", "bocca", "velocita", "frase"):
        if k not in d: ERR.append(f"{p}: manca «{k}».")
    colori(p, d, ["colore"]); numero(p, d, "occhi", 1, 3); numero(p, d, "cappello", 0, 2); numero(p, d, "bocca", 0, 2); numero(p, d, "velocita", 1, 3)
    for k in ("nome", "frase"):
        if VIETATI.search(str(d.get(k, ""))): ERR.append(f"{p}: in «{k}» niente email, link o numeri di telefono.")
    if len(str(d.get("nome", ""))) > 24: ERR.append(f"{p}: «nome» al massimo 24 caratteri.")
    if len(str(d.get("frase", ""))) > 40: ERR.append(f"{p}: «frase» al massimo 40 caratteri.")
for f in sorted(os.listdir("ambienti")):
    if not f.endswith(".json"): continue
    p = os.path.join("ambienti", f)
    if f[:-5] not in ("bosco", "case", "citta", "montagna", "mare"): ERR.append(f"{p}: gli ambienti sono bosco, case, citta, montagna, mare"); continue
    d = leggi(p)
    if d is None: continue
    colori(p, d, ["cielo_alto", "cielo_basso", "lontano", "terra", "colore_oggetti"]); numero(p, d, "densita", 1, 3)
    if d.get("oggetti") not in ("alberi", "case", "palazzi", "rocce", "onde"): ERR.append(f"{p}: «oggetti» è alberi, case, palazzi, rocce oppure onde")
if os.path.exists("facce.json"):
    d = leggi("facce.json")
    for n in (d or {}).get("facce", []):
        if not re.fullmatch(r"[a-z0-9-]+\.(jpg|png)", str(n)) or not os.path.exists(os.path.join("facce", str(n))):
            ERR.append(f"facce.json: «{n}» non è un file della cartella facce")
for f in ("versione.json", "regole.json", "percorso.json", "protagonista.json", "testi.json", "suoni.json"):
    d = leggi(f)
    if d is None: continue
    if f == "regole.json":
        numero(f, d, "vetro", 1, 9); numero(f, d, "velocita_treno", 0.5, 3); numero(f, d, "secondi_prima_di_sparare", 0.8, 5); numero(f, d, "cattivi_per_livello", 3, 50); numero(f, d, "punti_per_cattivo", 1, 1000)
    if f == "percorso.json":
        if any(a not in ("bosco", "case", "citta", "montagna", "mare") for a in d.get("ambienti", [])): ERR.append("percorso.json: gli ambienti sono bosco, case, citta, montagna, mare")
        numero(f, d, "secondi_per_ambiente", 5, 120)
    if f == "protagonista.json": colori(f, d, ["giacca", "capelli"])
    if f == "suoni.json": numero(f, d, "volume", 0, 1)
    for a in d.get("autori", []) if isinstance(d, dict) else []:
        if VIETATI.search(str(a)): ERR.append(f"{f}: negli autori solo PC o soprannome.")
if ERR:
    print("DA SISTEMARE:"); [print(" -", e) for e in ERR]; sys.exit(1)
print("Tutto a posto: il gioco può leggere tutti i file.")
