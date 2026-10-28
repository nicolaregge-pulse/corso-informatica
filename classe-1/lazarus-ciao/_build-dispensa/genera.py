#!/usr/bin/env python3
# Dispensa «Lazarus: il mio primo programma» (1INF, 28/10/2026): 3 documenti monolingui (IT, AR, ZH), MD + HTML.
# Uso: python3 _build-dispensa/genera.py   poi   node _build-dispensa/pdf.js   (PDF con Playwright)
# Il libro di testo prende il capitolo con: python3 _build-dispensa/genera.py libro  (stampa il capitolo MD per il libro)
import html, importlib.util, os, re, sys
QUI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(QUI); sys.path.insert(0, QUI)
VER, DATA = '1.0', '28/10/2026'
FONT = '/home/user/corso-informatica/strumenti/render-pdf/fonts/'

def carica(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(QUI, n + '.py')); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def nome(L): return '20261028_Classe-1_v%s_Lazarus-Primo-Programma_%s' % (VER, L['sigla'])

# ---------- testo in linea ----------
def h(t):
    """markup -> HTML: `codice`, [[menu]], **grassetto**, *corsivo*, \\n -> <br>."""
    st = []
    def stash(x): st.append(x); return '\x00%d\x00' % (len(st) - 1)
    t = re.sub(r'`([^`]+)`', lambda m: stash('<code>%s</code>' % html.escape(m.group(1), quote=False)), t)
    t = re.sub(r'\[\[(.+?)\]\]', lambda m: stash('<span class="ui">«%s»</span>' % html.escape(m.group(1), quote=False)), t)
    t = html.escape(t, quote=False)
    t = t.replace('{{', '<span class="ltr">').replace('}}', '</span>')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t); t = re.sub(r'\*([^*\n]+)\*', r'<i>\1</i>', t)
    t = t.replace('\n', '<br>')
    return re.sub(r'\x00(\d+)\x00', lambda m: st[int(m.group(1))], t)
def m(t, cella=False):
    """markup -> Markdown."""
    t = re.sub(r'\[\[(.+?)\]\]', r'«\1»', t).replace('{{', '').replace('}}', '')
    if cella:
        t = t.replace('|', '\\|').replace('\n', '<br>')
    return t

# ---------- HTML ----------
CSS = '''@font-face{font-family:Amiri;src:url(file://%(f)sAmiri-Regular.ttf)}@font-face{font-family:Amiri;font-weight:700;src:url(file://%(f)sAmiri-Bold.ttf)}
@page{size:A4;margin:20mm 16mm 18mm}
body{font-family:"DejaVu Sans",Arial,sans-serif;font-size:11pt;line-height:1.5;color:#1b2430;margin:0}
body.ar{font-family:Amiri,"DejaVu Sans",serif;font-size:13.5pt;line-height:1.75}
body.zh{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif;font-size:11pt;line-height:1.7}
h1{font-size:24pt;margin:0 0 2mm;color:#1f4e8c}.ver{font-weight:bold;margin:0 0 4mm;direction:ltr;unicode-bidi:isolate}
h2{font-size:15.5pt;margin:7mm 0 3mm;color:#1f4e8c;border-bottom:2px solid #1f4e8c;padding-bottom:1mm;break-after:avoid}
.sotto{font-size:13pt;color:#4a5562;margin:0 0 2mm}.intro{margin:4mm 0}
table{border-collapse:collapse;width:100%%;margin:3mm 0}tr{break-inside:avoid}th,td{border:1px solid #b9c2cc;padding:4px 7px;text-align:start;vertical-align:top}th{background:#e8f0fe}
table.banda td:first-child{background:#f3f5f8;font-weight:bold;width:32%%}
code{font-family:"DejaVu Sans Mono",monospace;font-size:.88em;background:#eef2f7;border:1px solid #d5dbe3;border-radius:3px;padding:0 3px;direction:ltr;unicode-bidi:isolate;white-space:nowrap}
body.ar code{font-size:.72em}body.ar .ui{font-family:"DejaVu Sans",sans-serif;font-size:.8em}
.ltr{direction:ltr;unicode-bidi:isolate;white-space:nowrap;font-family:"DejaVu Sans",sans-serif;font-size:.72em}.keep{break-after:avoid}td code{white-space:normal}
.ui{direction:ltr;unicode-bidi:isolate;font-weight:bold;color:#1f4e8c}
pre{font-family:"DejaVu Sans Mono",monospace;font-size:9.6pt;line-height:1.35;background:#f5f7fa;border:1px solid #c9d1db;border-radius:2mm;padding:3mm 4mm;margin:2mm 0 3mm;direction:ltr;text-align:left;unicode-bidi:isolate;white-space:pre;break-inside:avoid;overflow:hidden}
ol.passi{margin:2mm 0;padding-inline-start:8mm}ol.passi li{margin:1.2mm 0}ol.passi li pre{margin-top:1.5mm}
.box{border-radius:2mm;padding:3mm 4mm;margin:3mm 0;break-inside:avoid;background:#fff8e1;border-inline-start:5px solid #f9a825}
.quad{margin:3mm 0;break-inside:avoid}.quad .t{font-weight:bold;color:#2e7d32}.quad .leg{font-size:.92em;color:#3b4552}
figure{margin:4mm 0;text-align:center;break-inside:avoid}figure img{max-height:95mm;max-width:100%%;border-radius:2mm;border:1px solid #c9d1db}figcaption{font-size:.9em;color:#4a5562;margin-top:1.5mm;text-align:start}
'''
def html_doc(L, S):
    o = ['<!doctype html><html lang="%s" dir="%s"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body class="%s">' % (L['lang'], L['dir'], html.escape(L['titolo']), CSS % {'f': FONT}, L['lang'])]
    o.append('<h1>%s</h1><p class="sotto">%s</p><p class="ver">Versione %s — %s</p>' % (h(L['titolo']), h(L['sotto']), VER, DATA))
    o.append('<table class="banda">' + ''.join('<tr><td>%s</td><td>%s</td></tr>' % (h(a), h(b)) for a, b in L['banda']) + '</table>')
    o.append('<p class="intro">%s</p>' % h(L['intro']))
    for tit, blocchi in S:
        o.append('<h2>%s</h2>' % h(tit))
        for i, b in enumerate(blocchi):
            k = b[0]; dopo = blocchi[i + 1][0] if i + 1 < len(blocchi) else ''
            if k == 'p': o.append('<p%s>%s</p>' % (' class="keep"' if dopo in ('tab', 'steps', 'quaderno') else '', h(b[1])))
            elif k == 'steps':
                o.append('<ol class="passi">' + ''.join('<li>%s%s</li>' % (h(s[0]), ('<pre>%s</pre>' % html.escape(s[1], quote=False)) if len(s) > 1 else '') for s in b[1]) + '</ol>')
            elif k == 'tab':
                r = b[1]; o.append('<table><thead><tr>' + ''.join('<th>%s</th>' % h(c) for c in r[0]) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>%s</td>' % h(c) for c in x) + '</tr>' for x in r[1:]) + '</tbody></table>')
            elif k == 'quaderno':
                o.append('<div class="quad"><p class="t">%s</p><pre>%s</pre>%s</div>' % (h(L['quaderno']), html.escape(b[1], quote=False), ('<p class="leg"><b>%s:</b> %s</p>' % (h(L['legenda']), h(b[2]))) if b[2] else ''))
            elif k == 'nota': o.append('<div class="box">%s</div>' % h(b[1]))
            elif k == 'img': o.append('<figure><img src="%s" alt="%s"><figcaption><b>%s:</b> %s</figcaption></figure>' % (b[1], html.escape(L['foto']), h(L['foto']), h(b[2])))
    o.append('</body></html>')
    return '\n'.join(o)

# ---------- Markdown ----------
def md_blocchi(L, S, liv='##', num=None):
    """Markdown dei capitoli. num=None: titoli come nella dispensa; num='8': sottotitoli 8.1, 8.2 per il libro."""
    o = []
    for i, (tit, blocchi) in enumerate(S, 1):
        if num: o += ['%s %s.%d %s' % (liv, num, i, re.sub(r'^\d+ ', '', tit)), '']
        else: o += ['%s %s' % (liv, tit), '']
        for b in blocchi:
            k = b[0]
            if k == 'p': o += [m(b[1]), '']
            elif k == 'steps' and num and any(len(s) > 1 for s in b[1]):
                # libro: python-markdown non regge il codice dentro le liste -> passi come paragrafi numerati
                for j, s in enumerate(b[1], 1):
                    o += ['**%d.** %s' % (j, m(s[0])), '']
                    if len(s) > 1: o += ['```', s[1], '```', '']
            elif k == 'steps':
                for j, s in enumerate(b[1], 1):
                    o.append('%d. %s' % (j, m(s[0])))
                    if len(s) > 1:
                        pad = ' ' * (len('%d. ' % j))
                        if num:  # libro: blocco di codice indentato (python-markdown non legge i ``` dentro le liste)
                            o += [''] + [pad + '    ' + r for r in s[1].split('\n')] + ['']
                        else:
                            o += ['', pad + '```'] + [pad + r for r in s[1].split('\n')] + [pad + '```', '']
                o.append('')
            elif k == 'tab':
                r = b[1]; o += ['| ' + ' | '.join(m(c, True) for c in r[0]) + ' |', '|' + '---|' * len(r[0])] + ['| ' + ' | '.join(m(c, True) for c in x) + ' |' for x in r[1:]] + ['']
            elif k == 'quaderno':
                o += ['**%s**' % L['quaderno'], '', '```', b[1], '```', '']
                if b[2]: o += ['*%s:* %s' % (L['legenda'], m(b[2])), '']
            elif k == 'nota': o += ['> [GIALLO] ' + m(b[1]), '']
            elif k == 'img':
                src = b[1] if not num else 'immagini/' + os.path.basename(b[1])
                o += ['![%s: %s](%s)' % (L['foto'], m(b[2]).replace('[', '(').replace(']', ')'), src), '']
    return o
def md_doc(L, S):
    o = ['# ' + L['titolo'], '', '**Versione %s** — %s' % (VER, DATA), '', '*%s · %s*' % (L['classe'], L['sotto']), '',
         '| | |', '|---|---|'] + ['| %s | %s |' % (m(a, True), m(b, True)) for a, b in L['banda']] + ['', L['intro'], '']
    return '\n'.join(o + md_blocchi(L, S)).rstrip() + '\n'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'libro':
        t = carica('testi_it'); print('\n'.join(md_blocchi(t.L, t.S, '###', sys.argv[2] if len(sys.argv) > 2 else '8')).rstrip()); sys.exit()
    for n in ('testi_it', 'testi_ar', 'testi_zh'):
        t = carica(n); f = nome(t.L)
        open(os.path.join(OUT, f + '.html'), 'w').write(html_doc(t.L, t.S))
        md = md_doc(t.L, t.S)
        open(os.path.join(OUT, f + '.md'), 'w').write(md)
        print(f)
