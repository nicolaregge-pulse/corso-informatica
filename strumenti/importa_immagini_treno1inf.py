# -*- coding: utf-8 -*-
"""Importa nel «Treno blindato della 1INF» le immagini allegate ai compiti PR-1…PR-4 su Classroom.

Le consegne arrivano dal ponte di Google nel repository riservato: ../corso-informatica-riservato/dati/consegne/1INF/treno-prN/<Nome Cognome>.<ext>
Lo script le ridimensiona (lato massimo 600 px, JPG), le mette nell'albero docs/giochi/treno-1inf/immagini/<tipo>/<nome>-<iniziale>.jpg,
aggiorna immagini.json (galleria) e, per i cattivi (PR-1), le aggiunge anche alle facce del gioco (facce/ + facce.json).
Nelle pagine pubbliche si scrive solo il nome di battesimo e l'iniziale del cognome.
Uso: python3 strumenti/importa_immagini_treno1inf.py
"""
import json, os, re, unicodedata
from PIL import Image, ImageOps
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIOCO = os.path.join(ROOT, "docs", "giochi", "treno-1inf")
DEST = os.path.join(GIOCO, "immagini")
CONS = os.path.join(os.path.dirname(ROOT), "corso-informatica-riservato", "dati", "consegne", "1INF")
TIPI = {"treno-pr1": "cattivi", "treno-pr2": "paesaggi", "treno-pr3": "difetti", "treno-pr4": "revisioni"}
EST = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp")


def slug(s):
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def chi(nome_file):
    base = re.sub(r"_\d+$", "", os.path.splitext(nome_file)[0])
    p = [x for x in re.split(r"[\s_]+", base) if x]
    nome = p[0].capitalize() if p else "?"
    ini = (p[-1][0].upper() + ".") if len(p) > 1 else ""
    return (nome + " " + ini).strip(), slug(nome + "-" + ini)


def main():
    idx_p = os.path.join(DEST, "immagini.json")
    idx = json.load(open(idx_p, encoding="utf-8")) if os.path.exists(idx_p) else {"immagini": []}
    gia = {(x["tipo"], x["file"]) for x in idx["immagini"]}
    facce_p = os.path.join(GIOCO, "facce.json")
    F = json.load(open(facce_p, encoding="utf-8"))
    nuove = 0
    for cart, tipo in TIPI.items():
        src = os.path.join(CONS, cart)
        if not os.path.isdir(src):
            continue
        for f in sorted(os.listdir(src)):
            if not f.lower().endswith(EST):
                continue
            nome, s = chi(f)
            n = 1
            out = s + ".jpg"
            while (tipo, out) in gia and not any(x["file"] == out and x["origine"] == f for x in idx["immagini"]):
                n += 1; out = "%s-%d.jpg" % (s, n)
            if any(x["origine"] == f and x["tipo"] == tipo for x in idx["immagini"]):
                continue
            im = ImageOps.exif_transpose(Image.open(os.path.join(src, f))).convert("RGB")
            im.thumbnail((600, 600))
            im.save(os.path.join(DEST, tipo, out), "JPEG", quality=82)
            idx["immagini"].append({"tipo": tipo, "file": out, "chi": nome, "origine": f})
            gia.add((tipo, out)); nuove += 1
            if tipo == "cattivi":
                faccia = "1inf-" + out
                f2 = im.copy(); f2.thumbnail((240, 240)); f2.save(os.path.join(GIOCO, "facce", faccia), "JPEG", quality=82)
                if faccia not in F["facce"]:
                    F["facce"].insert(0, faccia)
                    F.setdefault("autori", []).append("Cattivo disegnato da " + nome + " (1INF, PR-1)")
    json.dump(idx, open(idx_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(F, open(facce_p, "w", encoding="utf-8"), ensure_ascii=False)
    print("immagini nuove:", nuove, "· totale:", len(idx["immagini"]))


if __name__ == "__main__":
    main()
