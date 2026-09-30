# -*- coding: utf-8 -*-
"""
Genera il MANUALE / LIBRO COMPLETO (per argomento, 3 livelli) dagli argomenti.
Fonte unica: i file argomenti/<slug>.md. Riusa i mattoni del generatore libri.

Uso: python3 genera_manuale.py [--out <file.pdf>] [--livelli 1,2,3] [--render <render_libro.js>]
"""
import os, re, html, base64, argparse, subprocess, sys, glob

HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.path.dirname(os.path.dirname(HERE))
ARG=os.path.join(REPO,"argomenti")
LIBRO_BUILD=os.path.join(REPO,"classe-1","libro-individuale","_build")
sys.path.insert(0,LIBRO_BUILD)
from genera_libro_individuale import md_liste_to_html, CSS  # riuso: niente duplicazione

LIV=[("Livello 1 (base)","L1 · Base","#2f9e57","#eaf6ef"),
     ("Livello 2 (intermedio)","L2 · Intermedio","#2b7cc4","#e8f1fb"),
     ("Livello 3 (avanzato)","L3 · Avanzato","#8e44ad","#f2ebf7")]

def leggi_argomento(path):
    txt=open(path,encoding="utf-8").read()
    fm={}; body=txt
    m=re.match(r'^---\n(.*?)\n---\n',txt,re.S)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line: k,v=line.split(':',1); fm[k.strip()]=v.strip()
        body=txt[m.end():]
    sez={}
    parts=re.split(r'^##\s+(.+)$',body,flags=re.M)
    for i in range(1,len(parts),2): sez[parts[i].strip()]=parts[i+1].strip()
    return fm,sez

def img_html(fm):
    out=[]
    for rel in [x.strip() for x in fm.get("immagini","").split("|") if x.strip()]:
        p=os.path.join(REPO,rel)
        if os.path.exists(p):
            b=base64.b64encode(open(p,"rb").read()).decode()
            out.append(f'<div class="fig"><img src="data:image/png;base64,{b}"></div>')
    return "".join(out)

EXTRA_CSS=('.lev{border-radius:8px;padding:0.5mm 4mm 3mm;margin:2mm 0 4mm}'
 '.lev .tag{display:inline-block;color:#fff;font-size:9pt;font-weight:bold;padding:1mm 3.5mm;border-radius:0 0 6px 6px;margin-bottom:2mm}'
 '.fig{text-align:center;margin:3mm 0}.fig img{max-width:70%;border:1px solid #e0e6ec;border-radius:6px}')

def genera(out_pdf, livelli, render_js=None):
    files=sorted(f for f in glob.glob(os.path.join(ARG,"*.md")) if os.path.basename(f)!="README.md")
    blocchi=[]
    for f in files:
        fm,sez=leggi_argomento(f)
        titolo=html.escape(fm.get("titolo",os.path.basename(f)))
        macro=html.escape(fm.get("macro","")); ver=html.escape(fm.get("versione",""))
        band=(f'<div class="unit-band"><div class="macro">{macro}</div>'
              f'<div class="titolo">{titolo}</div>'
              f'<div class="meta"><b>Argomento</b> · versione {ver}</div></div>')
        levhtml=[]
        for key,tag,col,bg in LIV:
            n=key.split()[1]  # "1","2","3"
            if n not in livelli: continue
            if key not in sez: continue
            levhtml.append(f'<div class="lev" style="background:{bg};border:1px solid {col}55">'
                           f'<div class="tag" style="background:{col}">{tag}</div>'
                           f'{md_liste_to_html(sez[key])}</div>')
        imgs=img_html(fm)
        blocchi.append(band+imgs+"".join(levhtml))
    indice="".join(f'<li>{html.escape(leggi_argomento(f)[0].get("titolo",""))}</li>' for f in files)
    doc=(f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}{EXTRA_CSS}</style></head><body>'
     '<div class="cover"><h1>Manuale di Informatica</h1>'
     '<div style="font-size:12pt;opacity:.9">Corso Operatore Informatico · a.s. 2026/27</div>'
     '<div class="who">Il libro completo</div>'
     '<div class="meta">Tutti gli argomenti, in 3 livelli di profondità — fonte unica che cresce e migliora</div></div>'
     '<div class="intro"><b>Come è organizzato:</b> ogni <b>argomento</b> è spiegato in <b>3 livelli</b> '
     '(base, intermedio, avanzato). È la fonte unica: da qui si generano i libri di classe e individuali. '
     f'Argomenti in questa edizione:<ol>{indice}</ol></div>'
     f'{"".join(blocchi)}</body></html>')
    html_path=os.path.splitext(out_pdf)[0]+".html"
    open(html_path,"w",encoding="utf-8").write(doc)
    if render_js:
        subprocess.run(["node",render_js,html_path,out_pdf,"Corso di Informatica",
                        "Manuale di Informatica — a.s. 2026/27","Manuale di Informatica"],check=True)
        print("PDF:",out_pdf)
    else:
        print("HTML:",html_path)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="/tmp/manuale-informatica.pdf")
    ap.add_argument("--livelli",default="1,2,3")
    ap.add_argument("--render",default=None)
    a=ap.parse_args()
    genera(a.out,[x.strip() for x in a.livelli.split(",")],a.render)
