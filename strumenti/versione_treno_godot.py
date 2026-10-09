"""Congela la versione attuale del Treno su Godot in docs/giochi/treno-godot/versioni/<v>/.

Uso: python3 strumenti/versione_treno_godot.py v2.1
La cartella della versione contiene solo la pagina e il pacchetto del gioco (index.pck):
il motore (index.js + index.wasm, 38 MB) è lo stesso per tutte le versioni e resta nella cartella principale.
"""
import os, re, shutil, sys

v = sys.argv[1]
base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "giochi", "treno-godot")
dst = os.path.join(base, "versioni", v)
os.makedirs(dst, exist_ok=True)
for f in os.listdir(dst):
    os.remove(os.path.join(dst, f))
shutil.copy(os.path.join(base, "index.pck"), os.path.join(dst, "index.pck"))
h = open(os.path.join(base, "index.html"), encoding="utf-8").read()
h = h.replace('src="index.js"', 'src="../../index.js"')
h = h.replace('"executable":"index"', '"executable":"../../index","mainPack":"index.pck"')
h = re.sub(r'(href|src)="index\.(png|icon\.png|apple-touch-icon\.png)"', r'\1="../../index.\2"', h)
h = h.replace("<title>", "<title>" + v + " · ", 1)
open(os.path.join(dst, "index.html"), "w", encoding="utf-8").write(h)
print("versione congelata:", dst)
