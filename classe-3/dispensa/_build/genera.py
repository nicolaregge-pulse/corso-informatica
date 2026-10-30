#!/usr/bin/env python3
"""Dispensa unica 3INF: sorgente (_build/sorgente-dispensa-3inf.md) -> dispensa-3inf.md -> dispensa-3inf-vX.Y.html.
Uso: python3 classe-3/dispensa/_build/genera.py ; poi node classe-3/dispensa/_build/pdf.js
Il numero di versione si legge dalla riga «**Versione X.Y**» del sorgente. Le immagini sono incorporate nell'HTML
(ridotte a 1400 px) così il file è unico; nell'MD restano i percorsi relativi ai file del repository."""
import base64, io, os, re, html
import markdown
from PIL import Image

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(B)
CLASSE = '3INF'
SIGLA = '3inf'
CORSO = 'MjUzMjQ1NzQ2NDBa'  # corso 3INF su Classroom
LINK = {  # id del compito su Classroom -> parte finale del link (elenco dei compiti della 3INF, 29/10/2026)
 '25512303811': 'MjU1MTIzMDM4MTFa', '25510294360': 'MjU1MTAyOTQzNjBa', '162789417641': 'MTYyNzg5NDE3NjQx',
 '893472573800': 'ODkzNDcyNTczODAw', '25484011501': 'MjU0ODQwMTE1MDFa', '162769881324': 'MTYyNzY5ODgxMzI0',
 '162767767346': 'MTYyNzY3NzY3MzQ2', '162767661128': 'MTYyNzY3NjYxMTI4', '162767331950': 'MTYyNzY3MzMxOTUw',
 '162761743140': 'MTYyNzYxNzQzMTQw', '25456074794': 'MjU0NTYwNzQ3OTRa', '889534649060': 'ODg5NTM0NjQ5MDYw',
 '162748281843': 'MTYyNzQ4MjgxODQz', '162737024883': 'MTYyNzM3MDI0ODgz', '25425883714': 'MjU0MjU4ODM3MTRa',
 '25425684246': 'MjU0MjU2ODQyNDZa', '25413864707': 'MjU0MTM4NjQ3MDda', '162722983699': 'MTYyNzIyOTgzNjk5',
}

# Riepilogo: data, titolo come su Classroom, che cosa si consegna, capitolo
COMPITI = [
 ('25/09', 'GitHub', 'Documento «Git e Versioning» con le 3 parti', '02'),
 ('28/09', 'I tipi di file', 'Documento «I tipi di file» con le 5 parti', '03'),
 ('30/09', 'Esercitazione pagina HTML', 'Documento: screenshot, codice e riflessione', '04'),
 ('30/09', 'CSS in un file separato', 'il Documento aggiornato con HTML e stile.css', '04'),
 ('02/10', 'Pagina HTML', 'la pagina «Mi presento» con i due file', '05'),
 ('05/10', 'Pagina personale HTML', 'Documento: link, HTML, CSS, screenshot, spiegazione', '06'),
 ('07/10', 'Compito 3 — Il sito migliorato', 'Documento con le 5 parti e la riflessione', '07'),
 ('08/10', 'Compito 4 — Il treno blindato della 3INF: le mie Pull Request', 'Documento con PR-1, PR-2, PR-3, PR-4 e che cosa ho imparato', '08'),
 ('12/10', "Versioning: il tuo Documento nell'albero delle versioni", 'il lavoro della pagina, fase 1 e fase 2', '09'),
 ('14/10', 'Il merge: le vostre richieste entrano nel gioco', 'almeno 3 richieste (PR1, PR2, PR3)', '10'),
 ('14/10', 'Ripasso e verifica: versioni, Pull Request, Agile', 'ripasso e verifica sulla pagina', '10'),
 ('14/10', 'VERIFICA: clicca qui', 'verifica su Moduli inviata', '10'),
 ('15/10', 'Sei il Product Manager: un team Agile al lavoro', 'v3.0, v3.1 e 3 risposte con «Consegna al prof»', '11'),
 ('19/10', 'Il mio sito diventa il mio portfolio', 'la pagina competenze.html online e la verifica', '12'),
 ('21/10', 'OGGI: il mio sito in ordine, più bello, e lavoro in coppia', 'sito in ordine, Pull Request in coppia, quiz su Moduli', '13'),
 ('22/10', 'OGGI: recupero — il mio sito personale funziona', 'il sito di 3 pagine e il quiz', '14'),
 ('28/10', 'Hello World in Lazarus e in Java', 'Documento: codici, screenshot, tabella del confronto, frasi', '16'),
 ('29/10', 'NON SONO RIUSCITO AD ESEGUIRE HELLO WORLD JAVA', 'Documento con le perplessità e il confronto', '17'),
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
