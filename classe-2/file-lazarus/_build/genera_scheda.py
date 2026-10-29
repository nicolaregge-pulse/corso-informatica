# -*- coding: utf-8 -*-
"""Scheda 2INF «I file di un progetto Lazarus» (29/10/2026): da proiettare e da dare ai ragazzi.
Una sola fonte -> MD (per l'AI dei ragazzi) + HTML di stampa -> PDF versionato (header e footer, pag. N / Tot).
Riusa la dispensa del 26/10 (file-lazarus.md): stesse risposte su .ico (SÌ, se l'hai scelta) e .res (NO).
Uso: python3 classe-2/file-lazarus/_build/genera_scheda.py
Poi: python3 strumenti/solo_italiano.py <html>  e  node strumenti/render-pdf/render_doc.js <html> <pdf> ...
(NODE_PATH verso i moduli globali con playwright, PW_EXECUTABLE verso Chromium)."""
import html, os, sys
VER = '1.0'; DATA = '29/10/2026'
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOME_PDF = '20261029_Classe-2_v%s_Scheda-File-Lazarus_IT.pdf' % VER
TITOLO = 'I file di un progetto Lazarus'
HTML_OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/scheda-file-lazarus-stampa.html'

RIGHE = [  # estensione, che cos'è (parole semplici), va su GitHub?
 ('.lpi', 'Il progetto. Con un doppio clic lo apri in Lazarus.', 'SÌ'),
 ('.lpr', 'Il programma principale. Da qui parte tutto.', 'SÌ'),
 ('.pas', 'Il codice di una finestra. Qui scrivi tu.', 'SÌ'),
 ('.lfm', 'Il disegno della finestra: bottoni, caselle, scritte.', 'SÌ'),
 ('.ico', 'L\'icona del programma. Lazarus non la rifà da solo.', 'SÌ, se l\'hai scelta'),
 ('.res', 'Le risorse: l\'icona già «impacchettata». Lazarus la rifà.', 'NO'),
 ('.lps', 'Le tue impostazioni personali: quali file avevi aperto. Serve solo a te.', 'NO'),
 ('.exe', 'Il programma pronto. Si rifà con F9 (Esegui).', 'NO'),
 ('cartella lib', 'Pezzi già tradotti per il computer. Si rifà con F9.', 'NO'),
 ('cartella backup', 'Copie vecchie dei tuoi file, fatte da Lazarus.', 'NO'),
]
REGOLA = ['Su GitHub vanno i file che servono per RIFARE il programma.',
          'Quello che Lazarus rifà da solo resta sul PC.',
          'Ricorda i 4 file: .lpi, .lpr, .pas, .lfm (più l\'icona .ico, se l\'hai scelta).']
WINDOWS = ['Windows spesso nasconde la fine del nome: l\'estensione (.pas, .lfm, ...).',
           'Così vedi due file con lo stesso nome, per esempio «unit1» e «unit1». Non sono uguali!',
           'Guarda l\'icona: il file .lpi ha l\'icona di Lazarus. Il file .exe ha l\'icona del programma.',
           'Guarda la colonna «Tipo». Se non la vedi: in Esplora file clic su «Visualizza», poi su «Dettagli».',
           'Nella colonna «Tipo» c\'è il tipo del file, spesso con la sigla: per esempio «File LFM».',
           'Su GitHub il nome si vede sempre intero, con l\'estensione: lì controlli che sia giusto.']
CARTELLA = ['Ogni progetto ha la SUA cartella. Mai due progetti nella stessa cartella.',
            'Oggi rifacciamo la calcolatrice da zero: la cartella si chiama «calcolatrice».',
            'Quando salvi il progetto in Lazarus, scegli proprio quella cartella.']
ALBERO = [('calcolatrice/', ''), ('├── calcolatrice.lpi', 'SÌ'), ('├── calcolatrice.lpr', 'SÌ'), ('├── unit1.pas', 'SÌ'),
          ('├── unit1.lfm', 'SÌ'), ('├── calcolatrice.ico', 'SÌ, se l\'hai scelta'), ('├── calcolatrice.res', 'NO'),
          ('├── calcolatrice.lps', 'NO'), ('├── calcolatrice.exe', 'NO'), ('├── lib/', 'NO'), ('└── backup/', 'NO')]
SPIEGA = ['Su GitHub metto solo i file per rifare il programma: .lpi, .lpr, .pas e .lfm.',
          'Nel .pas c\'è il codice che scrivo io, nel .lfm c\'è il disegno della finestra.',
          'Il .exe, la cartella lib e la cartella backup no: Lazarus li rifà quando premo F9.']

def albero_txt():
    return '\n'.join(('%-24s %s' % (a, b)).rstrip() for a, b in ALBERO)

# ---------- MD (fonte versionata, per l'AI dei ragazzi) ----------
md = ['# 00 %s' % TITOLO, '', '**Versione %s** — %s — Classe 2INF — Scheda' % (VER, DATA), '']
md += ['## 01 Ogni file, che cosa è', '', '| Estensione | Che cos\'è | Va su GitHub? |', '|---|---|---|']
md += ['| %s | %s | %s |' % r for r in RIGHE] + ['']
md += ['## 02 La regola d\'oro', ''] + ['> [GIALLO] ' + ' '.join(REGOLA), '']
md += ['## 03 Attenzione: Windows nasconde le estensioni', ''] + ['%d. %s' % (i + 1, p) for i, p in enumerate(WINDOWS)] + ['']
md += ['## 04 Una cartella per ogni progetto', ''] + ['%d. %s' % (i + 1, p) for i, p in enumerate(CARTELLA)] + ['']
md += ['```', albero_txt(), '```', '']
md += ['## 05 Spiegalo in 30 secondi', '', 'Dillo al compagno, con queste 3 frasi:', ''] + ['%d. %s' % (i + 1, p) for i, p in enumerate(SPIEGA)] + ['']
md += ['## Changelog', '', '1. v1.0 (29/10/2026): prima versione, scheda da proiettare per la lezione della calcolatrice da zero.', '']
open(os.path.join(QUI, 'scheda-file-lazarus.md'), 'w', encoding='utf-8').write('\n'.join(md))

# ---------- HTML di stampa ----------
e = html.escape
def ol(v): return '<ol>%s</ol>' % ''.join('<li><span class="n">%d</span><span>%s</span></li>' % (i + 1, e(p)) for i, p in enumerate(v))
h = ['<h1>%s</h1><p class="ver">Versione %s — %s — Classe 2INF — Scheda</p>' % (e(TITOLO), VER, DATA)]
h.append('<section><h2>01 Ogni file, che cosa è</h2><table><tr><th>Estensione</th><th>Che cos\'è</th><th>Va su GitHub?</th></tr>')
for a, b, c in RIGHE:
    h.append('<tr class="%s"><td class="est">%s</td><td>%s</td><td class="gh">%s</td></tr>' % ('si' if c.startswith('SÌ') else 'no', e(a), e(b), e(c)))
h.append('</table></section>')
h.append('<section><h2>02 La regola d\'oro</h2><div class="box giallo oro">%s</div></section>' % ''.join('<p>%s</p>' % e(p) for p in REGOLA))
h.append('<section><h2>03 Attenzione: Windows nasconde le estensioni</h2>%s</section>' % ol(WINDOWS))
alb = ''.join('<div class="r"><span class="f">%s</span><span class="%s">%s</span></div>' % (e(a), 'si' if b.startswith('SÌ') else 'no', e(b)) for a, b in ALBERO)
h.append('<section><h2>04 Una cartella per ogni progetto</h2>%s<div class="albero">%s</div></section>' % (ol(CARTELLA), alb))
h.append('<section><h2>05 Spiegalo in 30 secondi</h2><div class="box giallo"><p><b>Dillo al compagno, con queste 3 frasi:</b></p>%s</div></section>' % ol(SPIEGA))
CSS = '''body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1b1f24;font-size:14px;line-height:1.4;margin:0}
h1{font-size:26px;color:#12467a;margin:0}.ver{color:#555;margin:2px 0 8px;font-size:12px}
h2{font-size:18px;color:#12467a;border-bottom:2px solid #d5dde8;padding-bottom:2px;margin:12px 0 6px;break-after:avoid}
section{break-inside:avoid}
table{width:100%;border-collapse:collapse;font-size:14px}th,td{border:1px solid #c9d3e0;padding:5px 8px;text-align:left;vertical-align:top}
th{background:#e9f0f8}tr{break-inside:avoid}td.est{font-weight:700;font-family:"DejaVu Sans Mono",monospace;white-space:nowrap}
td.gh{font-weight:700;white-space:nowrap}tr.si td.gh{color:#11663a}tr.no td.gh{color:#b3261e}
.box{border-radius:6px;padding:8px 12px;margin:6px 0}.giallo{background:#fff8d6;border-left:6px solid #e0b400}.box p{margin:2px 0}
.oro{font-size:16px}.oro p:first-child{font-weight:700}
ol{list-style:none;padding:0;margin:4px 0}ol li{display:flex;gap:8px;margin:3px 0;break-inside:avoid}ol li .n{min-width:1.4em;font-weight:700;color:#12467a}
.albero{background:#f3f5f8;border-radius:6px;padding:8px 12px;margin-top:6px;font-family:"DejaVu Sans Mono",monospace;font-size:13px}
.albero .r{display:flex}.albero .f{width:17em;white-space:pre}.albero .si{color:#11663a;font-weight:700}.albero .no{color:#b3261e;font-weight:700}'''
open(HTML_OUT, 'w', encoding='utf-8').write('<!doctype html><html lang="it"><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (CSS, '\n'.join(h)))
print('MD e HTML di stampa scritti;', NOME_PDF)
