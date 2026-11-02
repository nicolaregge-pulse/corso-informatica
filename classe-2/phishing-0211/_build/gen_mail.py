# -*- coding: utf-8 -*-
# Scrive docs/anteprima/2inf-reti-02-11/mail/mail-N.html (finto programma di posta) e le fa fotografare a playwright (mail-N.png).
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from mails import MAILS
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../docs/anteprima/2inf-reti-02-11/mail/')
CSS = """*{box-sizing:border-box}body{margin:0;background:#e9edf2;font:17px/1.5 'Segoe UI',system-ui,Arial,sans-serif;color:#1f2328}
#mail{width:860px;max-width:100%;background:#fff;border:1px solid #c9d1da;margin:0}
.top{background:#2b4a6f;color:#fff;padding:9px 18px;font-weight:700;display:flex;justify-content:space-between;font-size:15px}
.top span:last-child{font-weight:400;opacity:.85}
.ogg{font-size:25px;font-weight:700;padding:16px 22px 8px}
.da{flex-wrap:wrap;display:flex;gap:12px;padding:6px 22px 14px;border-bottom:1px solid #e3e7ec;align-items:center}
.av{width:44px;height:44px;border-radius:50%;background:#6b7c93;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;flex:none}
.da b{font-size:17px}.da .ind{color:#4a5563;font-size:15px}.da .dt{margin-left:auto;color:#6b7684;font-size:14px;text-align:right}
.corpo{padding:18px 22px 10px}.corpo p{margin:0 0 12px}
.btn{display:inline-block;background:#1a73e8;color:#fff;padding:11px 22px;border-radius:6px;font-weight:700;margin:6px 0 14px;font-size:16px}
.all{margin:4px 22px 14px;display:inline-flex;gap:8px;border:1px solid #c9d1da;border-radius:8px;padding:7px 12px;background:#f4f6f9;font-size:15px}
.stato{word-break:break-all;background:#2d2f33;color:#e8eaed;font:14px/1.3 Consolas,Menlo,monospace;padding:7px 14px;border-top:3px solid #888}
.stato small{display:block;font:12px 'Segoe UI',Arial,sans-serif;color:#aab;margin-bottom:2px}"""
os.makedirs(OUT, exist_ok=True)
for m in MAILS:
    corpo = ''.join('<p>%s</p>' % r if '<br>' in r else '<p>%s</p>' % html.escape(r) for r in m['righe'])
    ini = html.escape(m['mitt'][0])
    allegato = '<div class="all">&#128206; %s</div>' % html.escape(m['allegato']) if m['allegato'] else ''
    h = ('<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Mail %d</title><style>%s</style></head><body>'
         '<div id="mail"><div class="top"><span>Posta · Esempio</span><span>Posta in arrivo</span></div>'
         '<div class="ogg">%s</div>'
         '<div class="da"><div class="av">%s</div><div><b>%s</b><div class="ind">&lt;%s&gt;</div><div class="ind">A: me</div></div><div class="dt">%s</div></div>'
         '<div class="corpo">%s<span class="btn">%s</span></div>%s'
         '<div class="stato"><small>Se passi il mouse sul bottone, in basso a sinistra il programma mostra dove porta davvero:</small>%s</div></div></body></html>'
         % (m['n'], CSS, html.escape(m['ogg']), ini, html.escape(m['mitt']), html.escape(m['ind']), html.escape(m['data']), corpo, html.escape(m['bottone']), allegato, html.escape(m['link'])))
    open(OUT + 'mail-%d.html' % m['n'], 'w', encoding='utf-8').write(h)
print('html ok', len(MAILS))
