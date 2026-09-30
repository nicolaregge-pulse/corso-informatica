# -*- coding: utf-8 -*-
"""
Generatore del LIBRO INDIVIDUALE complessivo di un allievo (Classe 1).

Unisce le UNITA' condivise (su Git: teoria + testo compito + criteri) con i DATI
RISERVATI del singolo allievo (fuori da Git: lavoro svolto + valutazione +
riflessione), producendo un PDF completo che cresce a ogni lezione.

Uso:
  python3 genera_libro_individuale.py --dati <dati_riservati.json> --allievo <slug> \
      [--out <file.pdf>] [--render <percorso render_generic.js>]

- Il generatore e i file 'unita/' NON contengono nomi (stanno su Git).
- I dati riservati (con i nomi) restano nello scratchpad, MAI su Git.
"""
import os, re, json, argparse, html, subprocess, sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # cartella libro-individuale

def leggi_manifesto():
    txt=open(os.path.join(BASE,"manifesto.md"),encoding="utf-8").read()
    unita=[]
    for m in re.finditer(r'^\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*([\d-]+)\s*\|\s*(unita/[^\s|]+)\s*\|',txt,re.M):
        sl=os.path.splitext(os.path.basename(m.group(4)))[0]
        sl=re.sub(r'^\d+-','',sl)
        unita.append(dict(id=m.group(1),titolo=m.group(2),data=m.group(3),file=m.group(4),slug=sl))
    return unita

def leggi_unita(relpath):
    txt=open(os.path.join(BASE,relpath),encoding="utf-8").read()
    fm={}
    fmatch=re.match(r'^---\n(.*?)\n---\n',txt,re.S)
    body=txt
    if fmatch:
        for line in fmatch.group(1).splitlines():
            if ':' in line:
                k,v=line.split(':',1); fm[k.strip()]=v.strip()
        body=txt[fmatch.end():]
    sez={}
    parts=re.split(r'^##\s+(.+)$',body,flags=re.M)
    # parts: [pre, titolo1, corpo1, titolo2, corpo2, ...]
    for i in range(1,len(parts),2):
        sez[parts[i].strip()]=parts[i+1].strip()
    return fm, sez

def _unisci_continuazioni(md):
    """Unisce le righe 'a capo' (continuazioni) alla voce di lista precedente,
    così un elenco spezzato su piu righe resta un unico <li> numerato bene."""
    res=[]
    for ln in md.splitlines():
        if re.match(r'^\s*\d+\.\s', ln) or ln.strip()=='':
            res.append(ln)
        else:
            if res and res[-1].strip()!='' and re.match(r'^\s*\d+\.\s', res[-1]):
                res[-1]=res[-1].rstrip()+' '+ln.strip()
            else:
                res.append(ln)
    return res

def md_liste_to_html(md):
    """Converte le liste numerate (anche annidate con indentazione) in <ol>."""
    lines=_unisci_continuazioni(md)
    out=[]; stack=[]  # stack di (indent)
    def close_to(indent):
        while stack and stack[-1]>indent:
            out.append('</ol>'); stack.pop()
    for ln in lines:
        m=re.match(r'^(\s*)\d+\.\s+(.*)$',ln)
        if m:
            indent=len(m.group(1))
            if not stack or indent>stack[-1]:
                out.append('<ol>'); stack.append(indent)
            elif indent<stack[-1]:
                close_to(indent)
            txt=html.escape(m.group(2))
            txt=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',txt)
            txt=re.sub(r'`(.+?)`',r'<span class="key">\1</span>',txt)
            out.append(f'<li>{txt}</li>')
        else:
            close_to(-1)
            if ln.strip():
                t=html.escape(ln.strip()); t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
                out.append(f'<p>{t}</p>')
    close_to(-1)
    return "\n".join(out)

LIV_COL={"Ottimo":"#2f9e57","Buono":"#3f7fbf","Sufficiente":"#d0a516","Da rivedere":"#c0392b"}
MARK={"ok":("●","#2f9e57","Soddisfatto"),"parz":("◑","#d0a516","Parziale"),"no":("○","#c0392b","Mancante")}

def blocco_personale(u_id, dati_unita, tipo="compito"):
    """Genera Il mio lavoro + Valutazione + Riflessione, o un segnaposto se mancano."""
    if not dati_unita:
        if tipo in ("aula","laboratorio"):
            return ('<div class="mancante">Attività svolta in classe (senza una '
                    'consegna individuale su Classroom).</div>')
        return ('<div class="mancante">Consegna di questa lezione non ancora inserita '
                '(da recuperare da Classroom).</div>')
    h=[]
    svolto=dati_unita.get("svolto")
    if svolto:
        h.append('<h4>Il mio lavoro — quello che ho consegnato</h4>')
        h.append(f'<div class="svolto">{html.escape(svolto).strip().replace(chr(10),"<br>")}</div>')
    v=dati_unita.get("valutazione")
    if v:
        lc=LIV_COL.get(v["livello"],"#3f7fbf")
        h.append('<h4>La valutazione del prof</h4>')
        h.append(f'<div class="valu"><div class="vhead"><span>Livello: {v["livello"]}</span><span>Voto: {v["voto"]}/10</span></div><table class="crit">')
        etich={"comp":"Completezza","prezzi":"Prezzi e totale","senso":"Scelte sensate","cura":"Cura e ordine","plagio":"Originalità (anti-plagio)","screen":"Screenshot","trascr":"Trascrizione","copia":"Copia-incolla","consegna":"Consegna","rifl":"Riflessione"}
        for k,val in v.get("crit",{}).items():
            ch=MARK[val[0]]
            h.append(f'<tr><td class="cl">{etich.get(k,k)}</td><td class="cm" style="color:{ch[1]}">{ch[0]} {ch[2]}</td><td>{html.escape(val[1])}</td></tr>')
        h.append('</table></div>')
        if v.get("sintesi"): h.append(f'<p><b>In sintesi:</b> {html.escape(v["sintesi"])}</p>')
        if v.get("migliora"):
            h.append('<p><b>Cosa posso migliorare:</b></p><ul>'+''.join(f'<li>{html.escape(x)}</li>' for x in v["migliora"])+'</ul>')
    r=dati_unita.get("riflessione")
    h.append('<div class="rifl"><h4>La mia riflessione — la parte più importante</h4>')
    if r and (r.get("non_fatto") or r.get("non_capito")):
        h.append(f'<div class="q">Cosa NON sono riuscito a fare, e perché:</div><div class="a">{html.escape(r.get("non_fatto","—")) or "—"}</div>')
        h.append(f'<div class="q">Cosa NON ho capito:</div><div class="a">{html.escape(r.get("non_capito","—")) or "—"}</div>')
    else:
        h.append('<div class="empty">— riflessione non presente in questa consegna —</div>')
    h.append('</div>')
    return "\n".join(h)

CSS='''
@page{size:A4;margin:15mm}
*{box-sizing:border-box}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a1a1a;font-size:11pt;line-height:1.55;margin:0}
.cover{background:linear-gradient(160deg,#12467a,#2b7cc4);color:#fff;border-radius:10px;padding:22mm 12mm;text-align:center;margin-bottom:7mm}
.cover h1{font-size:24pt;margin:0 0 3mm}.cover .who{font-size:17pt;font-weight:bold;margin:6mm 0 1mm}.cover .meta{font-size:12pt;opacity:.92}
.riserv{background:#fdecea;border:1px solid #e0b4ae;color:#8a2a1c;padding:1.5mm 3mm;border-radius:4px;font-size:8.5pt;margin-bottom:5mm;text-align:center}
.intro{background:#eef4fb;border:1px solid #cfe0f0;border-radius:6px;padding:4mm 5mm;font-size:10pt;color:#33475b;margin-bottom:6mm}
.unit-band{page-break-before:always;margin:0 0 4mm;border:1px solid #cfe0f0;border-radius:8px;overflow:hidden}
.unit-band:first-of-type{page-break-before:avoid}
.unit-band .macro{background:#12467a;color:#fff;font-size:9pt;letter-spacing:.5px;padding:1.5mm 4mm;text-transform:uppercase}
.unit-band .titolo{font-size:15pt;font-weight:bold;color:#12467a;padding:3mm 4mm 1mm}
.unit-band .meta{padding:0 4mm 1mm;color:#33475b;font-size:9.5pt}
.unit-band .meta b{color:#12467a}
.unit-band .cont{padding:0 4mm 3mm;color:#5a6b7b;font-size:9.5pt;font-style:italic}
h3{color:#12467a;font-size:12.5pt;margin:6mm 0 2mm;padding-left:3mm;border-left:5px solid #2b7cc4}
h4{color:#12467a;font-size:12pt;margin:5mm 0 2mm}
.tag{display:inline-block;background:#2b7cc4;color:#fff;font-size:8.5pt;padding:0.5mm 3mm;border-radius:10px;vertical-align:middle;margin-left:3mm}
p{margin:0 0 2.5mm}ol,ul{margin:0 0 3mm;padding-left:7mm}li{margin:1.2mm 0}
ol ol{margin:1mm 0}
.box{border:1px solid #d6e0ea;border-radius:6px;padding:3mm 4mm;margin:2mm 0 4mm;background:#fafcfe}
.key{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #cddae8;padding:0 4px;border-radius:3px;font-size:9.6pt}
.svolto{font-size:9.4pt;background:#f5f7fa;border-left:4px solid #8aa0b4;padding:3mm 4mm;border-radius:4px;line-height:1.4}
.valu{border:1px solid #cfdae6;border-radius:8px;overflow:hidden;margin:2mm 0}
.vhead{background:#12467a;color:#fff;padding:2.5mm 4mm;font-weight:bold;font-size:12pt;display:flex;justify-content:space-between}
table.crit{border-collapse:collapse;width:100%}
table.crit td{border-top:1px solid #e5edf4;padding:2mm 4mm;font-size:10pt;vertical-align:top}
td.cl{width:26%;font-weight:bold;color:#12467a}td.cm{width:24%;font-weight:bold}
.rifl{background:#fff8e6;border:1.5px solid #e6cf7a;border-radius:8px;padding:4mm 5mm;margin:3mm 0}
.rifl h4{color:#a6810a;margin:0 0 2mm}.rifl .q{font-weight:bold;color:#7a5c00;margin-top:2mm}
.rifl .a{margin:0 0 2mm}.rifl .empty{color:#b08a1a;font-style:italic}
.mancante{background:#f4f6f8;border:1px dashed #b7c4d0;color:#6a7a88;border-radius:6px;padding:3mm 4mm;font-style:italic}
'''

def genera(dati_path, slug, out_pdf, render_js=None):
    dati=json.load(open(dati_path,encoding="utf-8"))
    if slug not in dati: sys.exit(f"Allievo '{slug}' non trovato nei dati riservati.")
    allievo=dati[slug]; nome=allievo["nome"]; per_unita=allievo.get("unita",{})
    unita_list=leggi_manifesto()
    parts=[]
    for u in unita_list:
        fm,sez=leggi_unita(u["file"])
        teoria=md_liste_to_html(sez.get("Teoria",""))
        compito=md_liste_to_html(sez.get("Il compito",""))
        pers=blocco_personale(u["id"], per_unita.get(u["slug"]), fm.get("tipo","compito"))
        macro=html.escape(fm.get("macro","")); materia=html.escape(fm.get("materia",""))
        orario=html.escape(fm.get("orario","")); contenuto=html.escape(fm.get("contenuto",""))
        band=f'''<div class="unit-band">
<div class="macro">{macro}</div>
<div class="titolo">Unità {u["id"]} — {html.escape(u["titolo"])}</div>
<div class="meta"><b>Materia:</b> {materia} &nbsp;·&nbsp; <b>Data lezione:</b> {u["data"]} &nbsp;·&nbsp; <b>Orario:</b> {orario}</div>
<div class="cont">Contenuto: {contenuto}</div>
</div>'''
        parts.append(f'''{band}
<h3>La teoria — cosa abbiamo imparato</h3><div class="box">{teoria}</div>
<h3>Il compito — la consegna</h3><div class="box">{compito}</div>
<h3>Il mio lavoro e la valutazione</h3>{pers}''')
    doc=f'''<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><h1>Il mio libro di Informatica</h1><div style="font-size:12pt;opacity:.9">Classe 1 INF · Anno 2026/27</div>
<div class="who">{html.escape(nome)}</div><div class="meta">Il quaderno personale che cresce a ogni lezione</div></div>
<div class="riserv">RISERVATO — contiene il nome di un allievo (minore). Non su Git. Solo per il docente e l'allievo.</div>
<div class="intro"><b>Questo libro raccoglie tutto il tuo lavoro</b> — la teoria, il testo di ogni compito e il tuo compito svolto con la valutazione e la tua riflessione — di tutte le lezioni, in ordine di data. Cresce a ogni lezione.</div>
{''.join(parts)}
</body></html>'''
    html_path=os.path.splitext(out_pdf)[0]+".html"
    open(html_path,"w",encoding="utf-8").write(doc)
    if render_js:
        subprocess.run(["node",render_js,html_path,out_pdf,nome],check=True)
        print("PDF:",out_pdf)
    else:
        print("HTML:",html_path,"(render con render_generic.js per il PDF)")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--dati",required=True); ap.add_argument("--allievo",required=True)
    ap.add_argument("--out",default=None); ap.add_argument("--render",default=None)
    a=ap.parse_args()
    out=a.out or f"/tmp/{a.allievo}_libro-individuale.pdf"
    genera(a.dati,a.allievo,out,a.render)
