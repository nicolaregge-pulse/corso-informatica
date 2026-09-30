# -*- coding: utf-8 -*-
"""
Genera il LIBRO GENERALE della classe (senza nomi): tutte le unità con
teoria + compito + criteri, in ordine di data. È il "libro di testo" condiviso,
pubblicabile su Git. Riusa gli stessi mattoni del generatore individuale.

Uso: python3 genera_libro_generale.py [--out <file.pdf>] [--render <render_libro.js>]
"""
import os, html, argparse, subprocess
from genera_libro_individuale import leggi_manifesto, leggi_unita, md_liste_to_html, CSS

def genera(out_pdf, render_js=None):
    parts=[]
    for u in leggi_manifesto():
        fm,sez=leggi_unita(u["file"])
        teoria=md_liste_to_html(sez.get("Teoria",""))
        compito=md_liste_to_html(sez.get("Il compito",""))
        criteri=md_liste_to_html(sez.get("Criteri di valutazione",""))
        macro=html.escape(fm.get("macro","")); materia=html.escape(fm.get("materia",""))
        orario=html.escape(fm.get("orario","")); contenuto=html.escape(fm.get("contenuto",""))
        band=f'''<div class="unit-band">
<div class="macro">{macro}</div>
<div class="titolo">Unità {u["id"]} — {html.escape(u["titolo"])}</div>
<div class="meta"><b>Materia:</b> {materia} &nbsp;·&nbsp; <b>Data lezione:</b> {u["data"]} &nbsp;·&nbsp; <b>Orario:</b> {orario}</div>
<div class="cont">Contenuto: {contenuto}</div>
</div>'''
        parts.append(f'''{band}
<h3>La teoria</h3><div class="box">{teoria}</div>
<h3>Il compito</h3><div class="box">{compito}</div>
<h3>Criteri di valutazione</h3><div class="box">{criteri}</div>''')
    doc=f'''<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><h1>Libro di Classe — Informatica</h1><div style="font-size:12pt;opacity:.9">Classe 1 INF · Anno 2026/27</div>
<div class="who">Il libro della classe</div><div class="meta">Teoria e compiti di tutte le lezioni, in ordine di data</div></div>
<div class="intro"><b>Questo è il libro condiviso della classe:</b> per ogni lezione trovi la <b>teoria</b>, il <b>testo del compito</b> e i <b>criteri di valutazione</b>. Ogni allievo ne ha poi una copia <b>personale</b> con anche il proprio lavoro e la valutazione. Cresce a ogni lezione.</div>
{''.join(parts)}
</body></html>'''
    html_path=os.path.splitext(out_pdf)[0]+".html"
    open(html_path,"w",encoding="utf-8").write(doc)
    if render_js:
        subprocess.run(["node",render_js,html_path,out_pdf,"Classe 1 INF",
                        "Corso di Informatica — Classe 1","Libro di Classe — Informatica"],check=True)
        print("PDF:",out_pdf)
    else:
        print("HTML:",html_path)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default="/tmp/libro-classe1-generale.pdf")
    ap.add_argument("--render",default=None)
    a=ap.parse_args()
    genera(a.out,a.render)
