#!/usr/bin/env python3
"""Dispensa unica 2INF: sorgente (_build/sorgente-dispensa-2inf.md) -> dispensa-2inf.md -> dispensa-2inf-vX.Y.html.
Uso: python3 classe-2/dispensa/_build/genera.py ; poi node classe-2/dispensa/_build/pdf.js
Il numero di versione si legge dalla riga «**Versione X.Y**» del sorgente. Le immagini sono incorporate nell'HTML
(ridotte a 1400 px) così il file è unico; nell'MD restano i percorsi relativi ai file del repository."""
import base64, io, os, re, html
import markdown
from PIL import Image

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(B)
CLASSE = '2INF'
SIGLA = '2inf'
CORSO = 'MTYyNjU2MTA1NTg0'  # corso 2INF su Classroom
LINK = {  # id del compito su Classroom -> parte finale del link (elenco dei compiti della 2INF, 30/10/2026)
 '896634449458': 'ODk2NjM0NDQ5NDU4', '25511638244': 'MjU1MTE2MzgyNDRa', '896284901573': 'ODk2Mjg0OTAxNTcz',
 '896023720194': 'ODk2MDIzNzIwMTk0', '162796820407': 'MTYyNzk2ODIwNDA3', '162796509546': 'MTYyNzk2NTA5NTQ2',
 '162789012695': 'MTYyNzg5MDEyNjk1', '25496012521': 'MjU0OTYwMTI1MjFa', '25495514593': 'MjU0OTU1MTQ1OTNa',
 '25492948477': 'MjU0OTI5NDg0Nzda', '893468669864': 'ODkzNDY4NjY5ODY0', '25488710499': 'MjU0ODg3MTA0OTla',
 '25486684311': 'MjU0ODY2ODQzMTFa', '25485799458': 'MjU0ODU3OTk0NTha', '25474464847': 'MjU0NzQ0NjQ4NDda',
 '25473573008': 'MjU0NzM1NzMwMDha', '162762591641': 'MTYyNzYyNTkxNjQx', '890150006923': 'ODkwMTUwMDA2OTIz',
 '25457861580': 'MjU0NTc4NjE1ODBa', '889901173020': 'ODg5OTAxMTczMDIw', '25455229956': 'MjU0NTUyMjk5NTZa',
 '889536175690': 'ODg5NTM2MTc1Njkw', '162749600266': 'MTYyNzQ5NjAwMjY2', '162749480822': 'MTYyNzQ5NDgwODIy',
 '162749445767': 'MTYyNzQ5NDQ1NzY3', '25428535293': 'MjU0Mjg1MzUyOTNa', '162729930003': 'MTYyNzI5OTMwMDAz',
 '25406885800': 'MjU0MDY4ODU4MDBa',
}

# Riepilogo: data, titolo come su Classroom, che cosa si consegna, capitolo
COMPITI = [
 ('25/09', 'GitHub', 'Documento «Git e Versioning» con le 3 parti', '03'),
 ('28/09', 'Tipi di file', 'Documento «I tipi di file» con le 5 parti', '04'),
 ('01/10', 'LAZARUS: applicazione conversione temperatura', '2 screenshot, 3 risposte e la prova con Gemini', '06'),
 ('05/10', 'LAZARUS IF THEN', 'il lavoro sugli if della lezione', '07'),
 ('05/10', 'Lazarus — Il mio primo programma pubblicato su GitHub', 'il programma nel repository «lazarus» e il README', '07'),
 ('05/10', 'Lazarus — Indovina il numero con gli if annidati', 'Documento: 3 screenshot, codice, spiegazione, riflessione', '07'),
 ('07/10', 'Quiz 1 — Cosa scrive il programma?', 'il risultato del quiz nel Documento', '08'),
 ('08/10', 'Il treno blindato — il lavoro della mia squadra', 'Documento con le Pull Request', '09'),
 ('08/10', 'Il treno blindato — la mia idea e il mio difetto (versione 0.7)', 'Documento con 1 idea e 1 difetto', '09'),
 ('09/10', 'Sicurezza — 2ª ora (Regione): Prevenzione e protezione — quiz e domande', 'Documento: risultato del quiz e 5 risposte', '10'),
 ('09/10', 'Versioni e Git: la storia del nostro Treno blindato', 'Documento: una frase per ognuna delle 10 parole', '10'),
 ('12/10', "Versioning: il tuo Documento nell'albero delle versioni", 'Feedback e PR1 dai bottoni della pagina', '11'),
 ('15/10', 'Verifica rapida: versioni, Pull Request, Agile', 'verifica su Moduli inviata', '13'),
 ('15/10', 'Lazarus: il ciclo FOR, la tua app «da … a …»', "l'app «da … a …» in Lazarus", '13'),
 ('19/10', 'Contatore', "l'app che funziona e la verifica con il codice", '15'),
 ('19/10', 'VERIFICA: il ciclo FOR', 'quiz su Moduli inviato', '15'),
 ('20/10', 'Lazarus: il ciclo WHILE, lancia il dado finché…', 'il gioco del dado e la verifica con il codice', '16'),
 ('21/10', "OGGI: Sicurezza 3ª ora — l'organizzazione della prevenzione", 'ripasso sulla pagina e quiz su Moduli', '17'),
 ('21/10', 'OGGI: Sicurezza 4ª ora — diritti, doveri, sanzioni e vigilanza', 'quiz su Moduli inviato', '17'),
 ('22/10', 'OGGI: Lazarus FOR e WHILE — Il mio salvadanaio', 'il codice incollato nella pagina', '18'),
 ('22/10', 'QUIZ: cicli FOR e WHILE, Lazarus e GitHub', 'quiz su Moduli inviato', '18'),
 ('22/10', 'OGGI: GitHub — il mio repository «lazarus» in ordine', 'il repository «lazarus» in ordine', '18'),
 ('26/10', 'OGGI: il mio GitHub in ordine (repository «lazarus»)', 'il repository «lazarus» in ordine', '19'),
 ('26/10', 'ULTIMO LAVORO DI OGGI: il report del mio repository', 'Documento con 3 foto e 3 frasi', '19'),
 ('27/10', 'OGGI: il mio repository «lazarus» uguale per tutti', 'la cartella «calcolatrice» nel repository', '20'),
 ('28/10', 'SICUREZZA: ripasso delle 4 ore e i quiz che ti mancano', 'i quiz mancanti su Moduli', '21'),
 ('29/10', 'OGGI 29/10: la calcolatrice Lazarus su GitHub', 'Documento con gli screenshot', '22'),
 ('30/10', 'OGGI 30/10: Sicurezza, 5ª ora: il rischio infortuni', 'ripasso sulla pagina e quiz su Moduli', '23'),
]


def tabella():
    r = ['| N. | Data | Compito | Che cosa si consegna | Capitolo |', '|---|---|---|---|---|']
    for i, (d, t, c, cap) in enumerate(COMPITI, 1):
        r.append(f'| {i} | {d} | {t} | {c} | {cap} |')
    return '\n'.join(r)


def sorgente_a_md():
    s = open(os.path.join(B, f'sorgente-dispensa-{SIGLA}.md'), encoding='utf8').read()
    s = re.sub(r'\{\{CR:(\d+)\}\}', lambda m: 'https://classroom.google.com/c/' + CORSO + '/a/' + LINK[m.group(1)] + '/details', s)
    s = s.replace('{{TABELLA}}', f'La tabella elenca i {len(COMPITI)} compiti dati su Classroom alla {CLASSE} fino al 30/10/2026, in ordine di data. '
                  'Il capitolo dice dove trovare la teoria e le istruzioni.\n\n' + tabella())
    return s


def img_data(rel):
    p = os.path.normpath(os.path.join(OUT, rel))
    im = Image.open(p)
    im = im.convert('RGB')
    im.thumbnail((1400, 1400))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=78, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


CSS = """
@page{size:A4;margin:16mm 16mm 18mm 16mm}
:root{--ink:#1d2430;--mu:#5c6672;--ln:#cfd6de;--acc:#1f5f8b}
body{font-family:"DejaVu Sans","Amiri","WenQuanYi Zen Hei",sans-serif;font-size:10.2pt;line-height:1.45;color:var(--ink);background:#fff;margin:0}
h1{font-size:21pt;color:var(--acc);margin:0 0 6px}
h2{font-size:14.5pt;color:#fff;background:var(--acc);padding:6px 10px;border-radius:4px;margin:20px 0 8px;break-after:avoid;page-break-after:avoid}
h2.cap{break-before:page;page-break-before:always}
h3{font-size:11.5pt;color:var(--acc);border-bottom:1px solid var(--ln);padding-bottom:2px;margin:14px 0 6px;break-after:avoid;page-break-after:avoid}
p{margin:5px 0}
ol{margin:4px 0 6px 0;padding-left:22px}
li{margin:2px 0}
code{font-family:"DejaVu Sans Mono","WenQuanYi Zen Hei",monospace;font-size:9pt;background:#f1f4f7;padding:0 3px;border-radius:3px}
pre{background:#f1f4f7;border:1px solid var(--ln);border-radius:4px;padding:7px 9px;white-space:pre-wrap;break-inside:avoid;page-break-inside:avoid}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:9.3pt;break-inside:auto}
tr{break-inside:avoid;page-break-inside:avoid}
th,td{border:1px solid var(--ln);padding:3px 6px;text-align:left;vertical-align:top}
th{background:#e7eef5}
figure{margin:8px 0;text-align:center;break-inside:avoid;page-break-inside:avoid}
figure img{max-width:100%;max-height:118mm;border:1px solid var(--ln);border-radius:4px}
figcaption{font-size:8.8pt;color:var(--mu);margin-top:3px}
.box{border-left:5px solid;padding:6px 10px;margin:8px 0;border-radius:3px;break-inside:avoid}
.box.giallo{background:#fff8dc;border-color:#d9a400}.box.blu{background:#eaf3fb;border-color:#2a74b5}.box.rosso{background:#fdecec;border-color:#c0392b}
hr{border:0;border-top:1px solid var(--ln);margin:14px 0}
.sotto{color:var(--mu);font-style:italic}
a{color:var(--acc);word-break:break-all}
"""


def md_a_html(md):
    t = md.split('\n')
    # le righe «1.1 …» dentro le liste vanno a capo (interruzione di riga markdown)
    for i in range(1, len(t)):
        if re.match(r'^\s{2,}\d+(\.\d+)+ ', t[i]) and t[i - 1].strip():
            t[i - 1] = t[i - 1].rstrip() + '  '
    md = '\n'.join(t)
    # blockquote con [GIALLO]/[BLU]/[ROSSO] -> riquadri colorati
    def box(m):
        col = m.group(1).lower()
        testo = re.sub(r'^>\s?', '', m.group(0), flags=re.M).replace(f'[{m.group(1)}]', '', 1).strip()
        return f'<div class="box {col}" markdown="1">\n{testo}\n</div>'
    md = re.sub(r'^> \[(GIALLO|BLU|ROSSO)\][^\n]*(?:\n>[^\n]*)*', box, md, flags=re.M)
    corpo = markdown.markdown(md, extensions=['tables', 'fenced_code', 'md_in_html', 'sane_lists'])
    # immagini -> figure con didascalia, incorporate
    def fig(m):
        alt, src = html.unescape(m.group(1)), html.unescape(m.group(2))
        return f'<figure><img src="{img_data(src)}" alt="{html.escape(alt)}"><figcaption>{html.escape(alt)}</figcaption></figure>'
    corpo = re.sub(r'<p><img alt="([^"]*)" src="([^"]*)" ?/?></p>', fig, corpo)
    # ogni capitolo di lezione comincia su una pagina nuova
    corpo = re.sub(r'<h2>(\d\d) ', lambda m: f'<h2 class="cap">{m.group(1)} ' if m.group(1) != '00' else m.group(0), corpo)
    # niente riga orizzontale prima di un capitolo che comincia su pagina nuova (evita pagine vuote)
    corpo = re.sub(r'<hr ?/?>\s*(?=<h2 class="cap">)', '', corpo)
    # link cliccabili
    corpo = re.sub(r'(?<!["=>])(https://[^\s<)]+)', r'<a href="\1">\1</a>', corpo)
    return corpo


def main():
    md = sorgente_a_md()
    ver = re.search(r'\*\*Versione (\d+\.\d+)\*\*', md).group(1)
    open(os.path.join(OUT, f'dispensa-{SIGLA}.md'), 'w', encoding='utf8').write(md)
    corpo = md_a_html(md)
    doc = f'<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dispensa {CLASSE} v{ver}</title><style>{CSS}</style></head><body>{corpo}</body></html>'
    out = os.path.join(OUT, f'dispensa-{SIGLA}-v{ver}.html')
    open(out, 'w', encoding='utf8').write(doc)
    print(out, len(doc) // 1024, 'KB', len(COMPITI), 'compiti')


if __name__ == '__main__':
    main()
