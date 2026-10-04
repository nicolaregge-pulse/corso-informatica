# -*- coding: utf-8 -*-
# Converte un MD del corso (titoli numerati, liste numerate/gerarchiche, > box, **bold**, `code`)
# in HTML impaginato + PDF. Uso: python md2pdf_doc.py input.md output.pdf
import re, sys, os, subprocess, html
SP=os.path.dirname(os.path.abspath(__file__))
src, out_pdf = sys.argv[1], sys.argv[2]
headerLeft = sys.argv[3] if len(sys.argv)>3 else "Corso Informatica"
headerRight = sys.argv[4] if len(sys.argv)>4 else "a.s. 2026/27"
footerLeft = sys.argv[5] if len(sys.argv)>5 else "Materiale del corso"
lines=open(src,encoding="utf-8").read().split("\n")

def inline(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s=re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', s)
    return s

htmlparts=[]
liststack=[]  # livelli ol aperti (per indent)
def close_lists(to=0):
    while len(liststack)>to:
        htmlparts.append("</ol>"); liststack.pop()

i=0
while i < len(lines):
    ln=lines[i].rstrip()
    if not ln.strip():
        close_lists(0); i+=1; continue
    if ln.strip()=="---":
        close_lists(0); i+=1; continue
    if ln.lstrip().startswith("```"):
        close_lists(0); i+=1; buf=[]
        while i<len(lines) and not lines[i].lstrip().startswith("```"):
            buf.append(html.escape(lines[i])); i+=1
        i+=1  # salta la chiusura ```
        htmlparts.append("<pre>"+"\n".join(buf)+"</pre>"); continue
    m=re.match(r'^(#{1,4})\s+(.*)$', ln)
    if m:
        close_lists(0); lv=len(m.group(1)); htmlparts.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>"); i+=1; continue
    if ln.lstrip().startswith("> "):
        close_lists(0); buf=[]
        while i<len(lines) and lines[i].lstrip().startswith(">"):
            buf.append(lines[i].lstrip()[1:].lstrip()); i+=1
        htmlparts.append('<div class="note">'+inline(" ".join(buf))+"</div>"); continue
    if ln.strip().startswith('|') and i+1<len(lines) and re.match(r'^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$', lines[i+1]):
        close_lists(0)
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            rows.append(lines[i].strip()); i+=1
        def cells(r): return [c.strip() for c in r.strip().strip('|').split('|')]
        head=cells(rows[0]); body=[cells(r) for r in rows[2:]]
        h='<table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in head)+'</tr></thead><tbody>'
        for r in body: h+='<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>'
        h+='</tbody></table>'
        htmlparts.append(h); continue
    lm=re.match(r'^(\s*)(\d+)\.\s+(.*)$', ln)
    if lm:
        indent=len(lm.group(1)); level=indent//3 + 1
        if level>len(liststack):
            while len(liststack)<level: htmlparts.append("<ol>"); liststack.append(level)
        elif level<len(liststack):
            close_lists(level)
        htmlparts.append(f"<li>{inline(lm.group(3))}</li>"); i+=1; continue
    # paragrafo normale
    close_lists(0); htmlparts.append(f"<p>{inline(ln.strip())}</p>"); i+=1
close_lists(0)

CSS='''@page{size:A4}*{box-sizing:border-box}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:10.6pt;line-height:1.5;margin:0}
h1{color:#12467a;font-size:19pt;margin:0 0 2mm;border-bottom:3px solid #2b7cc4;padding-bottom:2mm}
h2{color:#12467a;font-size:14pt;margin:7mm 0 2mm;background:#eef4fb;border-left:5px solid #2b7cc4;padding:2mm 3mm}
h3{color:#1a5a94;font-size:11.6pt;margin:5mm 0 1.5mm}
h1,h2,h3,h4{break-after:avoid;page-break-after:avoid}table,tr,blockquote,pre{break-inside:avoid;page-break-inside:avoid}
h4{color:#1a5a94;font-size:10.6pt;margin:4mm 0 1mm}
p{margin:1.5mm 0}
ol{margin:1mm 0 2mm;padding-left:7mm}li{margin:1.2mm 0}
ol ol{margin:1mm 0}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px;font-size:9pt}
.note{background:#eaf2fb;border:1px solid #b9d3ee;border-left:5px solid #2b7cc4;border-radius:5px;padding:3mm 4mm;margin:3mm 0;color:#22405e;font-style:italic}
em,i{color:#33475b}
table{border-collapse:collapse;width:100%;margin:3mm 0;font-size:9.4pt}
th{background:#12467a;color:#fff;text-align:left;padding:2mm 2.5mm;border:1px solid #12467a}
td{border:1px solid #cfdae6;padding:1.8mm 2.5mm;vertical-align:top}
tbody tr:nth-child(even) td{background:#f4f8fc}
'''
doc=f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(htmlparts)}</body></html>'
hp=out_pdf.replace(".pdf",".html"); open(hp,"w",encoding="utf-8").write(doc)
subprocess.run(["node",f"{SP}/render_doc.js",hp,out_pdf,headerLeft,headerRight,footerLeft],check=True)
print("OK",out_pdf)
