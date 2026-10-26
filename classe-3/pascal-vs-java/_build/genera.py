#!/usr/bin/env python3
# Teoria «Object Pascal e Java» (3INF, 26/10/2026): 3 documenti monolingui (IT, AR, ZH), MD + HTML + PDF. Copia del generatore della dispensa 1INF, con il blocco 'code'.
# Uso: python3 _build/genera.py   (poi il PDF lo fa _build/pdf.js)
import importlib.util, os, re, sys, html
QUI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(QUI)
VER = '1.0'; IMG = ''
FONT = '/home/user/corso-informatica/strumenti/render-pdf/fonts/'
def carica(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(QUI, n + '.py')); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def nome(L): return (L.get('file', '20261023_Classe-1-Dispensa_v%s_Rete-Gamer') % VER) + '_' + L['lang'].upper()
def md_testo(t): return re.sub(r'<br>', '  \n', re.sub(r'</?b>', '**', t))
def tab_html(r): return '<table><tr>' + ''.join('<th>%s</th>' % c for c in r[0]) + '</tr>' + ''.join('<tr>' + ''.join('<td>%s</td>' % c for c in x) + '</tr>' for x in r[1:]) + '</table>'
CSS = '''@font-face{font-family:Amiri;src:url(file://%samiri-arabic-400-normal.woff2)}@font-face{font-family:Amiri;font-weight:700;src:url(file://%samiri-arabic-700-normal.woff2)}
@page{size:A4;margin:16mm 16mm 18mm}body{font-family:"DejaVu Sans",Arial,sans-serif;font-size:11.5pt;line-height:1.5;color:#1b2430}
body.ar{font-family:Amiri,serif;font-size:14pt;line-height:1.7}body.zh{font-family:"WenQuanYi Zen Hei",sans-serif}
h1{font-size:26pt;margin:0 0 4mm;color:#1f6feb}h2{font-size:16pt;margin:7mm 0 3mm;border-bottom:2px solid #1f6feb;padding-bottom:1mm;break-after:avoid}
.sec{break-inside:auto}table{border-collapse:collapse;width:100%%;margin:3mm 0;break-inside:avoid}th,td{border:1px solid #b9c2cc;padding:4px 8px;text-align:start;vertical-align:top}th{background:#e8f0fe}
.box{border-radius:3mm;padding:3mm 4mm;margin:3mm 0;break-inside:avoid}.es{background:#e8f5e9;border-inline-start:5px solid #2e7d32}.nota{background:#fff8e1;border-inline-start:5px solid #f9a825}.sol{background:#e3f2fd;border-inline-start:5px solid #1565c0}
.box b.t{display:block;margin-bottom:1mm}figure{margin:3mm 0;text-align:center;break-inside:avoid}figure img{max-height:105mm;max-width:100%%;border-radius:2mm}figcaption{font-size:.9em;color:#5c6672}
pre{background:#0d1117;color:#e6edf3;padding:3mm 4mm;border-radius:2mm;font:10pt/1.4 'DejaVu Sans Mono',monospace;direction:ltr;text-align:left;white-space:pre;overflow:hidden;break-inside:avoid}.lab{font-weight:700;margin:3mm 0 1mm}
.cop{text-align:center;padding-top:50mm;break-after:page}.cop .s{font-size:14pt;color:#5c6672}ol{margin:2mm 0}'''
# Uso: python3 _build/genera.py [prefisso=testi] (linee = linee guida del compito)
PRE = sys.argv[1] if len(sys.argv) > 1 else 'teoria'
for n in (PRE + '_it', PRE + '_ar', PRE + '_zh'):
    m = carica(n); L = m.L; f = nome(L)
    h = ['<!doctype html><html lang="%s" dir="%s"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body class="%s">' % (L['lang'], L['dir'], L['titolo'], CSS % (FONT, FONT), L['lang'])]
    h.append('<div class="cop"><h1>%s</h1><p class="s">%s</p><p>%s · v%s</p><p>%s</p></div>' % (L['titolo'], L['sotto'], L['classe'], VER, L['intro']))
    md = ['# %s' % L['titolo'], '', L['sotto'], '', '%s · Versione %s' % (L['classe'], VER), '', L['intro'], '']
    for tit, blocchi in m.S:
        h.append('<div class="sec"><h2>%s</h2>' % tit); md += ['## ' + tit, '']
        for b in blocchi:
            k = b[0]
            if k == 'p': h.append('<p>%s</p>' % b[1]); md += [md_testo(b[1]), '']
            elif k == 'tab': h.append(tab_html(b[1])); md += ['| ' + ' | '.join(b[1][0]) + ' |', '|' + '---|' * len(b[1][0])] + ['| ' + ' | '.join(x) + ' |' for x in b[1][1:]] + ['']
            elif k in ('es', 'nota'): h.append('<div class="box %s"><b class="t">%s</b>%s</div>' % (k, L[k], b[1])); md += ['> **%s.** %s' % (L[k], md_testo(b[1]).replace('  \n', '  \n> ')), '']
            elif k == 'img': h.append('<figure><img src="%s%s"><figcaption>%s: %s</figcaption></figure>' % (IMG, b[1], L['foto'], b[2])); md += ['![%s](%s%s)' % (L['foto'], IMG, b[1]), '', '*%s: %s*' % (L['foto'], b[2]), '']
            elif k == 'code': h.append('<div class="lab">%s</div><pre>%s</pre>' % (b[1], html.escape(b[2]))); md += ['**' + re.sub(r'<[^>]+>', '', b[1]) + '**', '', '```', b[2], '```', '']
            elif k == 'ol': h.append('<ol>' + ''.join('<li>%s</li>' % x for x in b[1]) + '</ol>'); md += ['%d. %s' % (i + 1, x) for i, x in enumerate(b[1])] + ['']
            elif k == 'sol': h.append('<div class="box sol"><b class="t">%s</b><ol>%s</ol></div>' % (L['sol'], ''.join('<li>%s</li>' % x for x in b[1]))); md += ['### ' + L['sol'], ''] + ['%d. %s' % (i + 1, x) for i, x in enumerate(b[1])] + ['']
        h.append('</div>')
    h.append('</body></html>')
    open(os.path.join(OUT, f + '.html'), 'w').write('\n'.join(h)); open(os.path.join(OUT, f + '.md'), 'w').write('\n'.join(md))
    print(f)
