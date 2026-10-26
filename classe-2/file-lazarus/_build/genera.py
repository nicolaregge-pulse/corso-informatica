# -*- coding: utf-8 -*-
"""Dispensa 2INF «I file di un progetto Lazarus» (26/10/2026): una sola fonte -> MD, pagina online, PDF.
Uso: python3 classe-2/file-lazarus/_build/genera.py   (poi PDF con Playwright, vedi fondo)"""
import html, os, subprocess
VER = '1.0'; DATA = '26/10/2026'
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(QUI))
NOME_PDF = '20261026_Classe-2_v%s_File-di-Lazarus_IT.pdf' % VER
TITOLO = 'I file di un progetto Lazarus'

RIGHE = [  # estensione, nome, a che cosa serve, testo/binario, su GitHub
 ('.lpi', 'Lazarus Project Information', 'La scheda del progetto: le sue impostazioni. Con un doppio clic si apre il progetto in Lazarus.', 'testo', 'SÌ'),
 ('.lpr', 'Lazarus Program', 'Il programma principale: il punto da cui parte tutto.', 'testo', 'SÌ'),
 ('.pas', 'Pascal (unit)', 'Il codice che scrivi tu, per esempio unit1.pas.', 'testo', 'SÌ'),
 ('.lfm', 'Lazarus Form', 'Com\'è fatta la finestra: bottoni, caselle, posizioni, Caption.', 'testo', 'SÌ'),
 ('.ico', 'Icona', 'L\'icona del programma. Lazarus non la rifà da solo.', 'binario', 'SÌ'),
 ('.lps', 'Lazarus Project Session', 'Quali file avevi aperto e dove era il cursore. È solo tua.', 'testo', 'NO'),
 ('.res', 'Risorse', 'L\'icona e altre informazioni già «impacchettate». Lazarus la rifà.', 'binario', 'NO'),
 ('.o  .ppu', 'Pezzi compilati', 'Pezzi di programma già tradotti per il computer. Lazarus li rifà.', 'binario', 'NO'),
 ('.compiled', 'Nota di compilazione', 'Un appunto di Lazarus su come ha compilato.', 'testo', 'NO'),
 ('.exe', 'Programma pronto', 'Il programma finito. Lazarus lo rifà quando premi Esegui.', 'binario', 'NO'),
 ('backup/', 'Cartella', 'Copie vecchie dei tuoi file, fatte da Lazarus.', '—', 'NO'),
 ('lib/', 'Cartella', 'I pezzi compilati (.o, .ppu, .res, .compiled).', '—', 'NO'),
]

SEZ = [
 ('01 Che cosa crea Lazarus', [
  'Quando salvi un progetto, Lazarus mette nella cartella tanti file, non uno solo.',
  'Alcuni sono la RICETTA: li hai fatti tu (il codice, la finestra). Altri sono la TORTA già cotta: Lazarus li crea da solo quando premi Esegui.',
  'Su GitHub mettiamo solo la ricetta. Con la ricetta chiunque rifà la torta: apre il progetto e preme Esegui.']),
 ('02 File di testo e file binari', [
  'Un file di TESTO si apre con Blocco note e dentro leggi parole e codice.',
  'Un file BINARIO aperto con Blocco note mostra solo simboli strani: lo capisce solo il computer.',
  'Prova: clic destro sul file, poi «Apri con», poi «Blocco note». Se leggi parole è testo, se vedi simboli è binario. Chiudi senza salvare.']),
]
REGOLA = 'Su GitHub vanno solo 4 tipi di file: .lpi, .lpr, .pas, .lfm (e l\'icona .ico, se l\'hai scelta). Tutto il resto Lazarus lo rifà da solo.'
EXE = 'Perché niente .exe? GitHub serve per conservare la ricetta. Il .exe è la torta: pesa, cambia ogni volta che premi Esegui e non si può leggere. Chi vuole il programma apre il progetto e preme Esegui.'
ALBERO = 'lazarus/\n├── README.md\n├── primo-programma/\n│   ├── project1.lpi\n│   ├── project1.lpr\n│   ├── unit1.pas\n│   └── unit1.lfm\n└── salvadanaio/\n    ├── salvadanaio.lpi\n    ├── salvadanaio.lpr\n    ├── unit1.pas\n    └── unit1.lfm'
DOMANDE = ['In quale file c\'è il codice che hai scritto tu?', 'In quale file c\'è com\'è fatta la tua finestra?',
           'Come capisci se un file è di testo o binario?', 'Perché su GitHub non mettiamo il file .exe?']

# ---------- MD ----------
md = ['# 00 %s' % TITOLO, '', '**Versione %s** — %s — Classe 2INF' % (VER, DATA), '']
for t, ps in SEZ:
    md += ['## ' + t, ''] + ['%d. %s' % (i + 1, p) for i, p in enumerate(ps)] + ['']
md += ['## 03 Tutti i file, uno per uno', '', '| Estensione | Nome | A che cosa serve | Testo o binario | Su GitHub |', '|---|---|---|---|---|']
md += ['| %s | %s | %s | %s | %s |' % r for r in RIGHE] + ['']
md += ['## 04 La regola facile', '', '1. ' + REGOLA, '2. ' + EXE, '']
md += ['## 05 Come deve essere il tuo repository', '', '```', ALBERO, '```', '']
md += ['## 06 Sai spiegarlo?', '', 'Rispondi a voce, con parole tue:', ''] + ['%d. %s' % (i + 1, d) for i, d in enumerate(DOMANDE)] + ['']
md += ['## Changelog', '', '1. v1.0 (26/10/2026): prima versione, dalla lezione «Il mio GitHub in ordine».', '']
open(os.path.join(QUI, 'file-lazarus.md'), 'w').write('\n'.join(md))

# ---------- HTML (pagina online e base del PDF) ----------
e = html.escape
def corpo(online):
    h = ['<h1>%s</h1><p class="ver">Versione %s — %s — Classe 2INF</p>' % (e(TITOLO), VER, DATA)]
    if online: h.append('<p class="pdf"><a href="%s" download>Scarica il PDF</a></p>' % NOME_PDF)
    for t, ps in SEZ:
        h.append('<h2>%s</h2><ol>%s</ol>' % (e(t), ''.join('<li>%s</li>' % e(p) for p in ps)))
    h.append('<h2>03 Tutti i file, uno per uno</h2><table><tr><th>Estensione</th><th>Nome</th><th>A che cosa serve</th><th>Testo o binario</th><th>Su GitHub</th></tr>')
    for r in RIGHE:
        h.append('<tr class="%s"><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td><b>%s</b></td></tr>' % ('si' if r[4] == 'SÌ' else 'no', e(r[0]), e(r[1]), e(r[2]), e(r[3]), r[4]))
    h.append('</table>')
    h.append('<h2>04 La regola facile</h2><div class="box giallo">%s</div><div class="box blu">%s</div>' % (e(REGOLA), e(EXE)))
    h.append('<h2>05 Come deve essere il tuo repository</h2><pre>%s</pre>' % e(ALBERO))
    h.append('<h2>06 Sai spiegarlo?</h2><p>Rispondi a voce, con parole tue:</p><ol>%s</ol>' % ''.join('<li>%s</li>' % e(d) for d in DOMANDE))
    return '\n'.join(h)
CSS = '''body{font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:16px;line-height:1.5;color:#1b1f24;background:#fff}
h1{font-size:28px;margin:8px 0 0}h2{font-size:21px;margin:26px 0 8px;break-after:avoid}.ver{color:#555;margin:2px 0 12px}
table{width:100%;border-collapse:collapse;font-size:15px}th,td{border:1px solid #ccd;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#eef2f7}tr.si td:last-child{color:#11663a}tr.no td:last-child{color:#b3261e}tr{break-inside:avoid}
.box{border-radius:8px;padding:10px 14px;margin:10px 0}.giallo{background:#fff6d6;border-left:6px solid #e0b400}.blu{background:#e6f0ff;border-left:6px solid #2f6fdb}
pre{background:#f4f6f8;padding:12px;border-radius:8px;overflow-x:auto;font-size:15px}.pdf a{display:inline-block;background:#1f6feb;color:#fff;padding:8px 14px;border-radius:8px;text-decoration:none}
@media (max-width:600px){table{font-size:13px}th,td{padding:4px}}'''
pag = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>File di Lazarus</title><style>%s</style></head><body>%s\n<script src="../assistente/assistente.js" data-pagina="2inf-file-lazarus" data-lingue="it"></script></body></html>' % (CSS, corpo(True))
out = os.path.join(ROOT, 'docs', '2inf-file-lazarus'); os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w').write(pag)
stampa = '<!doctype html><html lang="it"><head><meta charset="utf-8"><style>%s @page{size:A4;margin:16mm}</style></head><body>%s</body></html>' % (CSS, corpo(False))
open('/tmp/claude-0/file-lazarus-stampa.html', 'w').write(stampa)
print('MD, pagina e HTML di stampa scritti;', NOME_PDF)
