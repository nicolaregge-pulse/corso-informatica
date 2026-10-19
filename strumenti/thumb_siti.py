#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Miniature (thumbnail) delle pagine dei siti dei ragazzi per il cruscotto del docente (19/10/2026, Nicola).
Legge docs/avanzamento/<banca>-siti.json (url del portfolio e del sito di ognuno), scarica da raw.githubusercontent.com
index.html, style.css, competenze.html, passione.html, li rende in locale con Playwright e salva le miniature in
docs/avanzamento/thumb/<banca>/<utente>-<pagina>.png. Nel cruscotto compaiono come immagini cliccabili (link al sito vero).
Uso: python3 strumenti/thumb_siti.py <banca>      (es. 3inf-portfolio-v1)
"""
import json, os, re, sys, subprocess, tempfile, urllib.request
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = sys.argv[1]
SITI = json.load(open(f"{R}/docs/avanzamento/{B}-siti.json", encoding="utf-8"))
OUT = f"{R}/docs/avanzamento/thumb/{B}"; os.makedirs(OUT, exist_ok=True)
PAG = ["index.html", "competenze.html", "passione.html"]


def raw(u, repo, f):
    for br in ("main", "master"):
        try:
            with urllib.request.urlopen(f"https://raw.githubusercontent.com/{u}/{repo}/{br}/{f}", timeout=15) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            pass
    return None


lavori = []
with tempfile.TemporaryDirectory() as tmp:
    for nome, s in SITI.items():
        m = re.match(r"https://([^.]+)\.github\.io/([^/]+)/", s.get("sito", ""))
        if not m or s.get("home_ok") is False:
            continue
        u, repo = m.group(1), m.group(2)
        d = os.path.join(tmp, u); os.makedirs(d, exist_ok=True)
        css = raw(u, repo, "style.css")
        if css: open(os.path.join(d, "style.css"), "w", encoding="utf-8").write(css)
        for p in PAG:
            h = raw(u, repo, p)
            if h is None:
                continue
            open(os.path.join(d, p), "w", encoding="utf-8").write(h)
            lavori.append({"file": os.path.join(d, p), "out": f"{OUT}/{u}-{p[:-5]}.png", "pagina": p[:-5], "nome": nome})
    job = os.path.join(tmp, "job.json"); json.dump(lavori, open(job, "w"))
    js = r"""
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const L=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:960,height:600},deviceScaleFactor:0.5});
for(const l of L){try{await p.goto('file://'+l.file,{waitUntil:'load',timeout:8000});await p.waitForTimeout(150);await p.screenshot({path:l.out});}catch(e){console.log('KO',l.file,e.message.slice(0,80));}}
await b.close();})();"""
    jsf = os.path.join(tmp, "shot.js"); open(jsf, "w").write(js)
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", jsf, job], env=env, timeout=240)
# indice per il cruscotto: nome -> {pagina: file}
idx = {}
for l in lavori:
    if os.path.exists(l["out"]):
        idx.setdefault(l["nome"], {})[l["pagina"]] = os.path.relpath(l["out"], f"{R}/docs/avanzamento")
json.dump(idx, open(f"{OUT}/indice.json", "w"), ensure_ascii=False, indent=1)
print(f"miniature: {sum(len(v) for v in idx.values())} pagine di {len(idx)} ragazzi")
