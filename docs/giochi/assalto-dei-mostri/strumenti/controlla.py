# Controllo automatico dei file del gioco (gira da solo a ogni Pull Request: è la «revisione del codice» automatica).
# Se qualcosa non va, la Pull Request mostra una X rossa e qui sotto c'è scritto cosa sistemare.
import json, os, re, sys

ERR = []
COLORE = re.compile(r"^#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$")
VIETATI = re.compile(r"@|https?://|\b\d{6,}\b")          # niente email, link o numeri di telefono


def leggi(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception as e:
        ERR.append(f"{p}: non è JSON valido ({e}). Controlla virgole e virgolette.")
        return None


def numero(p, d, k, a, b):
    if k in d and not (isinstance(d[k], (int, float)) and a <= d[k] <= b):
        ERR.append(f"{p}: «{k}» deve essere un numero da {a} a {b}.")


for f in sorted(os.listdir("mostri")):
    p = os.path.join("mostri", f)
    if f.startswith("pc00") or f.endswith(".md"):
        continue
    if f.endswith(".png"):
        if not re.fullmatch(r"pc(0[1-9]|[1-3]\d|40)\.png", f):
            ERR.append(f"{p}: l'immagine deve chiamarsi come il tuo PC, per esempio pc14.png")
        continue
    if not re.fullmatch(r"pc(0[1-9]|[1-3]\d|40)\.json", f):
        ERR.append(f"{p}: il nome del file deve essere pc + numero del PC a due cifre, per esempio pc07.json")
        continue
    d = leggi(p)
    if d is None:
        continue
    for k in ("nome", "colore", "occhi", "corna", "bocca", "velocita", "frase"):
        if k not in d:
            ERR.append(f"{p}: manca «{k}».")
    if "colore" in d and not COLORE.match(str(d["colore"])):
        ERR.append(f"{p}: «colore» deve essere come #ff6fb1")
    numero(p, d, "occhi", 1, 3); numero(p, d, "corna", 0, 1); numero(p, d, "bocca", 0, 2); numero(p, d, "velocita", 1, 3)
    for k in ("nome", "frase"):
        if VIETATI.search(str(d.get(k, ""))):
            ERR.append(f"{p}: in «{k}» niente email, link o numeri di telefono.")
    if len(str(d.get("nome", ""))) > 24:
        ERR.append(f"{p}: «nome» al massimo 24 caratteri.")
    if len(str(d.get("frase", ""))) > 40:
        ERR.append(f"{p}: «frase» al massimo 40 caratteri.")

for f in ("versione.json", "regole.json", "grafica.json", "testi.json", "suoni.json"):
    d = leggi(f)
    if d is None:
        continue
    if f == "regole.json":
        numero(f, d, "vetro_minimo", 1, 9); numero(f, d, "vetro_massimo", 1, 9); numero(f, d, "secondi_prima_di_sparare", 0.8, 5)
        numero(f, d, "mostri_per_livello", 3, 50); numero(f, d, "punti_per_mostro", 1, 1000)
        if d.get("vetro_minimo", 0) > d.get("vetro_massimo", 9):
            ERR.append("regole.json: vetro_minimo non può essere più grande di vetro_massimo.")
    if f == "grafica.json":
        for k, v in d.items():
            if k == "autori":
                continue
            for x in (v if isinstance(v, list) else [v]):
                if not COLORE.match(str(x)):
                    ERR.append(f"grafica.json: «{k}» deve essere un colore come #ffd34d")
    if f == "suoni.json":
        numero(f, d, "volume", 0, 1)
    for a in d.get("autori", []) if isinstance(d, dict) else []:
        if VIETATI.search(str(a)):
            ERR.append(f"{f}: negli autori solo PC o soprannome.")

if ERR:
    print("DA SISTEMARE:")
    for e in ERR:
        print(" -", e)
    sys.exit(1)
print("Tutto a posto: il gioco può leggere tutti i file.")
