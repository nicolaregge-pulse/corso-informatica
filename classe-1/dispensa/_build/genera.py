#!/usr/bin/env python3
"""Dispensa unica 1INF: sorgente (_build/sorgente-dispensa-1inf.md) -> dispensa-1inf.md -> dispensa-1inf-vX.Y.html.
Uso: python3 classe-1/dispensa/_build/genera.py ; poi node classe-1/dispensa/_build/pdf.js
Il numero di versione si legge dalla riga «**Versione X.Y**» del sorgente. Le immagini sono incorporate nell'HTML
(ridotte a 1400 px) così il file è unico; nell'MD restano i percorsi relativi ai file del repository."""
import base64, io, os, re, html
import markdown
from PIL import Image

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(B)
CR = 'https://classroom.google.com/c/ODc3MDA4ODA3MzM2/a/'
LINK = {  # id del compito su Classroom -> parte finale del link (elenco dei compiti della 1INF, 30/10/2026)
 '896633156753': 'ODk2NjMzMTU2NzUz', '25512772563': 'MjU1MTI3NzI1NjNa', '162798419144': 'MTYyNzk4NDE5MTQ0',
 '896264751640': 'ODk2MjY0NzUxNjQw', '25508838506': 'MjU1MDg4Mzg1MDZa', '25501074817': 'MjU1MDEwNzQ4MTda',
 '25499238525': 'MjU0OTkyMzg1MjVa', '25497518252': 'MjU0OTc1MTgyNTJa', '25491537064': 'MjU0OTE1MzcwNjRa',
 '162785194824': 'MTYyNzg1MTk0ODI0', '162780501663': 'MTYyNzgwNTAxNjYz', '162780530434': 'MTYyNzgwNTMwNDM0',
 '162772834692': 'MTYyNzcyODM0Njky', '25479109134': 'MjU0NzkxMDkxMzRa', '162772427606': 'MTYyNzcyNDI3NjA2',
 '25470195861': 'MjU0NzAxOTU4NjFa', '25470143620': 'MjU0NzAxNDM2MjBa', '162766226696': 'MTYyNzY2MjI2Njk2',
 '25468157252': 'MjU0NjgxNTcyNTJa', '890168279073': 'ODkwMTY4Mjc5MDcz', '25456481000': 'MjU0NTY0ODEwMDBa',
 '25456492719': 'MjU0NTY0OTI3MTla', '162758014051': 'MTYyNzU4MDE0MDUx', '162758007983': 'MTYyNzU4MDA3OTgz',
 '162751969558': 'MTYyNzUxOTY5NTU4', '162744859457': 'MTYyNzQ0ODU5NDU3', '25435420216': 'MjU0MzU0MjAyMTZa',
 '25435321522': 'MjU0MzUzMjE1MjJa', '25435145858': 'MjU0MzUxNDU4NTha', '25434650395': 'MjU0MzQ2NTAzOTVa',
 '25430126069': 'MjU0MzAxMjYwNjla', '162740680247': 'MTYyNzQwNjgwMjQ3', '162736042009': 'MTYyNzM2MDQyMDA5',
 '25424338372': 'MjU0MjQzMzgzNzJa', '25423836765': 'MjU0MjM4MzY3NjVa', '162720697037': 'MTYyNzIwNjk3MDM3',
 '162718828033': 'MTYyNzE4ODI4MDMz', '25399922586': 'MjUzOTk5MjI1ODZa', '162715816693': 'MTYyNzE1ODE2Njkz',
 '25387925389': 'MjUzODc5MjUzODla', '25387467575': 'MjUzODc0Njc1NzVa', '162706061942': 'MTYyNzA2MDYxOTQy',
 '25379757538': 'MjUzNzk3NTc1Mzha', '25379076643': 'MjUzNzkwNzY2NDNa', '25373823679': 'MjUzNzM4MjM2Nzla',
}

# Riepilogo: data, titolo come su Classroom, che cosa si consegna, capitolo
COMPITI = [
 ('17/09', 'Io e la mia famiglia: documento di presentazione (origini, provenienza, storia)', 'Documento Google su Classroom', '03'),
 ('18/09', 'Ricerca: cos\'è GitHub e cos\'è un repository', 'Documento con la ricerca; account GitHub', '04'),
 ('21/09', 'Parti del PC', 'il lavoro sui componenti, su Classroom', '05'),
 ('21/09', 'CTRL + ALT + CANC', 'quello che chiede il compito', '05'),
 ('21/09', 'VERSIONING', 'lettura della scheda delle versioni', '05'),
 ('21/09', 'QUIZ (Regole + Versioning)', 'quiz completato', '05'),
 ('23/09', 'Esercizio Hardware', 'il lavoro sui componenti, su Classroom', '07'),
 ('23/09', 'Quiz (componenti del PC)', 'quiz completato', '07'),
 ('24/09', 'Configurare un PC', 'Documento con i 5 standard e le immagini', '08'),
 ('24/09', 'Crea il PC dei tuoi sogni', 'lista dei pezzi compatibili con il totale', '08'),
 ('30/09', 'Configura un PC', 'Documento con 8 componenti, prezzi e totale', '09'),
 ('30/09', 'USARE CATTURA SCHERMO', 'Documento con screenshot, testo trascritto e riflessione', '09'),
 ('30/09', 'L\'inizio di quest\'anno scolastico', 'come indicato nel compito', '09'),
 ('01/10', 'Bit e Byte TEORIA', 'lettura della dispensa', '10'),
 ('01/10', 'Compito — Da binario a decimale', '16 esercizi svolti', '10'),
 ('02/10', 'Compito — Da decimale a binario', 'esercizi di conversione', '11'),
 ('02/10', 'Compito — Dalla divisione per 2 al binario', 'divisioni a catena', '11'),
 ('02/10', 'Compito 1 — Divisioni per 2', 'risultato della pagina degli esercizi', '11'),
 ('02/10', 'Compito 2 — Divisioni per 2 con il timer', 'risultato della pagina degli esercizi', '11'),
 ('02/10', 'Compito 3 — Divisioni per 2 con il timer', 'risultato della pagina degli esercizi', '11'),
 ('06/10', 'Cacciaviti per il laboratorio — come li compro', 'come indicato nel compito', '17'),
 ('08/10', 'PR-1 — Il mio cattivo', 'Documento con la richiesta e la foto del disegno', '12'),
 ('08/10', 'PR-2 — Il mio paesaggio', 'Documento con la richiesta', '12'),
 ('08/10', 'PR-3 — Un difetto', 'Documento con il difetto', '12'),
 ('08/10', 'PR-4 — Revisione e cosa ho imparato', 'Documento con la revisione', '12'),
 ('09/10', 'Versioni e Git: la storia del nostro Treno blindato', 'compito unico con il quiz', '13'),
 ('13/10', 'La mia prima Pull Request', 'la Pull Request: riga, valore nuovo, perché', '14'),
 ('14/10', 'La mia talpa', 'la foto ritagliata e la frase sul personaggio', '15'),
 ('14/10', 'La mia talpa: il percorso', 'ripasso e verifica sulla pagina', '15'),
 ('14/10', 'Com\'è andata oggi?', 'poche righe sulla lezione', '15'),
 ('15/10', 'Versioni del software e changelog (annuncio)', 'verifica sulla pagina', '16'),
 ('16/10', 'Lab — Monta il PC (gara di assemblaggio)', 'il PC rimontato', '17'),
 ('16/10', 'Sfida lampo — conosci i pezzi del PC?', 'la sfida completata', '17'),
 ('16/10', 'Ripassa e fai il Test — i pezzi del PC', 'ripasso e test sulla pagina', '17'),
 ('20/10', 'Quanto pesa un file? Quanto va veloce la rete?', 'ripasso sulla pagina', '18'),
 ('20/10', 'QUIZ: bit, byte e velocità della rete', 'quiz su Moduli inviato', '18'),
 ('21/10', 'OGGI: il laboratorio del gamer', 'percorso «Quante ce ne stanno?» e giochi dei byte', '19'),
 ('21/10', 'QUIZ: velocità della rete, download, streaming e cavi', 'quiz su Moduli inviato', '19'),
 ('22/10', 'OGGI: Sicurezza 1 — pericolo, rischio e infortunio', 'ripasso sulla pagina e quiz su Moduli', '20'),
 ('23/10', 'Dimensioni e unità di misura dell\'informatica', 'Documento «Rete e gamer», 13 capitoli, almeno 1500 parole', '21'),
 ('23/10', 'QUIZ dimensioni', 'quiz su Moduli inviato', '21'),
 ('27/10', 'OGGI: ripasso, poi la scheda video e i cavi', 'i due quiz', '22'),
 ('28/10', 'Il mio primo programma: Ciao in Lazarus', 'Documento con codice, screenshot e una frase', '23'),
 ('29/10', 'OGGI 29/10: Sicurezza 2, prevenzione e protezione (e Sicurezza 3)', 'ripasso sulla pagina e quiz su Moduli', '24'),
 ('29/10', 'Recuperi quiz', 'i quiz mancanti', '24'),
 ('30/10', 'OGGI 30/10: il computer scrive in tutte le lingue', 'ripasso e due quiz su Moduli', '25'),
 ('30/10', 'OGGI 30/10: Laboratorio 11-14: stringhe e interi in Lazarus', 'per ogni ora unit1.pas e lo screenshot', '26'),
]


def tabella():
    r = ['| N. | Data | Compito | Che cosa si consegna | Capitolo |', '|---|---|---|---|---|']
    for i, (d, t, c, cap) in enumerate(COMPITI, 1):
        r.append(f'| {i} | {d} | {t} | {c} | {cap} |')
    return '\n'.join(r)


def sorgente_a_md():
    s = open(os.path.join(B, 'sorgente-dispensa-1inf.md'), encoding='utf8').read()
    s = re.sub(r'\{\{CR:(\d+)\}\}', lambda m: CR + LINK[m.group(1)] + '/details', s)
    s = s.replace('{{TABELLA}}', f'La tabella elenca i {len(COMPITI)} compiti dati su Classroom alla 1INF fino al 30/10/2026, in ordine di data. '
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
    # ogni capitolo di lezione (01-27) comincia su una pagina nuova
    corpo = re.sub(r'<h2>(\d\d) ', lambda m: f'<h2 class="cap">{m.group(1)} ' if m.group(1) != '00' else m.group(0), corpo)
    # link cliccabili
    corpo = re.sub(r'(?<!["=>])(https://[^\s<)]+)', r'<a href="\1">\1</a>', corpo)
    return corpo


def main():
    md = sorgente_a_md()
    ver = re.search(r'\*\*Versione (\d+\.\d+)\*\*', md).group(1)
    open(os.path.join(OUT, 'dispensa-1inf.md'), 'w', encoding='utf8').write(md)
    corpo = md_a_html(md)
    doc = f'<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dispensa 1INF v{ver}</title><style>{CSS}</style></head><body>{corpo}</body></html>'
    out = os.path.join(OUT, f'dispensa-1inf-v{ver}.html')
    open(out, 'w', encoding='utf8').write(doc)
    print(out, len(doc) // 1024, 'KB', len(COMPITI), 'compiti')


if __name__ == '__main__':
    main()
