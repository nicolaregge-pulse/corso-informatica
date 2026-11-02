#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Libreria per le pagine dei ragazzi (04/11/2026): schemi SVG (regola 32) e scheletro della pagina a passi.
# Nessun nome di ragazzi qui dentro. Usata da strumenti/genera_pagine_04_11.py.
import html, os

SLUGDIR = '/home/user/corso-informatica/docs/anteprima/'
INVIO = 'https://script.google.com/macros/s/AKfycbzJ-4JRlTsSRSL77wXNG6ysffGURuDwyFVLin681obuwaw51a5Iso9KHqlUVLcig4_m/exec'
E = html.escape


def _t(x, y, s, size=20, bold=False, fill='#1f2328', anchor='start', mono=False):
    n_ = len(s) - len(s.lstrip(' ')); s = '\u00a0' * n_ + s.lstrip(' ')
    fam = 'Consolas,Menlo,monospace' if mono else 'Arial,Helvetica,sans-serif'
    return '<text x="%d" y="%d" font-size="%d" fill="%s" font-weight="%s" text-anchor="%s" font-family="%s">%s</text>' % (
        x, y, size, fill, 'bold' if bold else 'normal', anchor, fam, E(s))


def svg(path, titolo, items, hl=(), nota=''):
    """items: ('lbl',testo,x,y) ('edit',testo,x,y,w) ('btn',testo,x,y,w) ('memo',testo,x,y,w,h)
    ('menu',[voci],x,y) ('box',testo,x,y,w,h) ('code',[righe],x,y,w) ('arrow',x1,y1,x2,y2)
    hl: indici degli items da cerchiare in rosso. Scrive il file SVG in path."""
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 470" role="img" aria-label="%s">' % E(titolo),
         '<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#d1242f"/></marker></defs>',
         '<rect width="800" height="470" fill="#eef1f4"/>',
         '<rect x="10" y="10" width="780" height="450" rx="10" fill="#fff" stroke="#57606a" stroke-width="3"/>',
         '<rect x="10" y="10" width="780" height="34" rx="10" fill="#d0d7de" stroke="#57606a" stroke-width="3"/>',
         _t(24, 35, titolo, 20, True)]
    boxes = []
    for it in items:
        k = it[0]
        if k == 'lbl':
            o.append(_t(it[2], it[3], it[1], 24, True)); boxes.append((it[2] - 6, it[3] - 24, len(it[1]) * 13 + 12, 34))
        elif k == 'edit':
            x, y, w = it[2], it[3], it[4]
            o.append('<rect x="%d" y="%d" width="%d" height="40" fill="#fff" stroke="#57606a" stroke-width="2"/>' % (x, y, w))
            o.append(_t(x + 10, y + 28, it[1], 22)); boxes.append((x, y, w, 40))
        elif k == 'btn':
            x, y, w = it[2], it[3], it[4]
            o.append('<rect x="%d" y="%d" width="%d" height="44" rx="6" fill="#e1e1e1" stroke="#57606a" stroke-width="2"/>' % (x, y, w))
            o.append(_t(x + w // 2, y + 30, it[1], 21, True, anchor='middle')); boxes.append((x, y, w, 44))
        elif k == 'memo':
            x, y, w, h = it[2], it[3], it[4], it[5]
            o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#fff" stroke="#57606a" stroke-width="2"/>' % (x, y, w, h))
            for i, r in enumerate(it[1].split('\n')):
                o.append(_t(x + 10, y + 28 + i * 26, r, 19, mono=True))
            boxes.append((x, y, w, h))
        elif k == 'box':
            x, y, w, h = it[2], it[3], it[4], it[5]
            o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="#fff8d6" stroke="#57606a" stroke-width="2"/>' % (x, y, w, h))
            for i, r in enumerate(it[1].split('\n')):
                o.append(_t(x + 14, y + 32 + i * 28, r, 20, i == 0))
            boxes.append((x, y, w, h))
        elif k == 'menu':
            x, y = it[2], it[3]
            o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#f6f8fa" stroke="#57606a" stroke-width="2"/>' % (x, y, 300, 36 * len(it[1]) + 8))
            for i, r in enumerate(it[1]):
                o.append(_t(x + 14, y + 32 + i * 36, r, 21))
            boxes.append((x, y, 300, 36 * len(it[1]) + 8))
        elif k == 'code':
            x, y, w = it[2], it[3], it[4]
            h = 28 * len(it[1]) + 20
            o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="#0d1117" stroke="#57606a" stroke-width="2"/>' % (x, y, w, h))
            for i, r in enumerate(it[1]):
                o.append(_t(x + 14, y + 30 + i * 28, r, 18, fill='#e6edf3', mono=True))
            boxes.append((x, y, w, h))
        elif k == 'arrow':
            o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d1242f" stroke-width="5" marker-end="url(#ar)"/>' % it[1:5]); boxes.append(None)
    for i in hl:
        b = boxes[i]
        if b:
            o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="none" stroke="#d1242f" stroke-width="5"/>' % (b[0] - 5, b[1] - 5, b[2] + 10, b[3] + 10))
    if nota:
        for i, r in enumerate(nota.split('\n')):
            o.append(_t(30, 420 + i * 26 - 26 * (nota.count('\n')), r, 20, True, '#d1242f'))
    o.append('</svg>')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(''.join(o))


def codesvg(path, titolo, codice, nota=''):
    righe = codice.strip('\n').split('\n\n')[0].split('\n')[:11]
    svg(path, titolo, [('code', righe, 40, 70, 720)], (), nota or 'Il codice da scrivere (esempio)')


CSS = """:root{--bg:#f6f7f9;--fg:#1f2328;--mu:#5b6573;--card:#fff;--bd:#d5dbe3;--acc:#0b6e99;--ok:#1a7f37;--q:#fff4c2;--ante:#fde8e8;--blu:#1f6feb}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--q:#3b3200;--ante:#3a1616}}
:root[data-theme="dark"]{--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--q:#3b3200;--ante:#3a1616}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.5 system-ui,"Segoe UI",sans-serif}
main{max-width:820px;margin:0 auto;padding:12px 16px 60px}h1{font-size:1.45em;margin:.4em 0}h2{font-size:1.15em;margin:.2em 0 .4em}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 14px;margin:12px 0}
.ar{direction:rtl;text-align:right;color:var(--mu);font-size:.95em;margin:4px 0;font-family:"Amiri","Noto Naskh Arabic","Segoe UI",serif}.zh{color:var(--mu);font-size:.95em;margin:4px 0;font-family:"WenQuanYi Zen Hei","Microsoft YaHei",sans-serif}
pre{background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;overflow-x:auto;font-size:16px;white-space:pre-wrap;margin:8px 0;position:relative}pre .t{display:block}
.quad{background:var(--q);border:2px solid #d4a017;border-radius:10px;padding:10px 12px}.f5{background:var(--q);border-radius:10px;padding:8px 12px;font-size:.95em}
.ante{background:var(--ante);border:2px solid #c0392b;border-radius:10px;padding:8px 12px;font-size:.95em}
a.bt,button.bt{display:block;width:100%;text-align:center;background:var(--acc);color:#fff;font:inherit;font-weight:700;padding:12px;border-radius:10px;text-decoration:none;margin:8px 0;border:0;cursor:pointer}
a.bt.v,button.bt.v{background:var(--ok)}a.bt.b{background:#fff0;color:var(--acc);border:2px solid var(--acc);font-weight:600}
code{background:rgba(127,127,127,.15);border-radius:5px;padding:1px 5px}
.barra{height:14px;background:var(--bd);border-radius:7px;overflow:hidden;margin:6px 0}.barra i{display:block;height:100%;background:var(--ok);width:0}
.passo{border:3px solid var(--bd);border-radius:14px;padding:6px 14px 10px;margin:14px 0;background:var(--card)}
.passo .num{display:inline-flex;width:38px;height:38px;border-radius:50%;background:#6e7781;color:#fff;align-items:center;justify-content:center;font-weight:800;margin-right:6px}
.passo .bollo{float:right;font-size:14px;padding:3px 10px;border-radius:8px;color:#fff;background:#6e7781}
.passo.fatto{border-color:var(--ok)}.passo.fatto .num,.passo.fatto .bollo{background:var(--ok)}
.passo.ora{border:4px solid var(--blu)}.passo.ora .num,.passo.ora .bollo{background:var(--blu)}
.passo button.fb{font:inherit;font-weight:700;background:var(--ok);color:#fff;border:0;border-radius:10px;padding:9px 16px;cursor:pointer;margin-top:6px}
.passo.fatto button.fb{background:#6e7781}
details{margin:8px 0}details summary{cursor:pointer;font-weight:700;color:var(--blu)}
input[type=text]{font:inherit;width:100%;padding:8px 10px;border:2px solid var(--acc);border-radius:10px;background:var(--card);color:var(--fg)}
.mu{color:var(--mu);font-size:.92em}
.cp{position:absolute;right:6px;top:6px;font:inherit;font-size:13px;padding:3px 9px;border-radius:7px;border:0;background:#30363d;color:#fff;cursor:pointer}
.bn{display:none;background:#eef7ee;border-left:4px solid var(--ok);padding:4px 10px;margin:4px 0;color:#111;font-family:"Noto Sans Bengali","Vrinda","Nirmala UI",sans-serif}
body.pc14 .bn{display:block}.aiutoprof p{margin:0 0 6px}
.err{border:2px solid #c0392b;border-radius:12px;padding:8px 14px;margin:10px 0;background:var(--card)}
#ip{border:4px solid var(--blu);border-radius:14px;padding:12px 14px;margin:12px 0;background:var(--card);text-align:center}
#ip .g{font-size:1.5em;font-weight:800;margin:4px 0;word-break:break-all}#ip.vuoto{border-color:#d4a017;background:var(--q)}
.sx-img{width:100%;max-width:720px;height:auto;border:2px solid #8c959f;border-radius:10px;display:block}
@media (max-width:480px){main{padding:10px 16px 60px}h1{font-size:1.25em}pre{font-size:14px}}"""


def L(d, k='x'):
    """Righe nelle altre lingue: d = {'ar':..,'zh':..,'bn':..}"""
    o = ''
    if d.get('ar'): o += '<p class="ar" lang="ar" dir="rtl">%s</p>' % d['ar']
    if d.get('zh'): o += '<p class="zh" lang="zh">%s</p>' % d['zh']
    if d.get('bn'): o += '<p class="bn" lang="bn">%s</p>' % d['bn']
    return o


def passo_html(n, p):
    """p: dict(t=titolo it, tl={ar,zh,bn}, x=testo it (html), xl={...}, code=str, img=file, alt=str, extra=html)"""
    h = '<div class="passo" data-p="%d"><span class="bollo">da fare</span><h2><span class="num">%d</span>%s</h2>' % (n, n, p['t'])
    h += L(p.get('tl', {}))
    if p.get('x'): h += '<p>%s</p>' % p['x']
    h += L(p.get('xl', {}))
    if p.get('code'): h += '<pre><span class="t">%s</span></pre>' % E(p['code'].strip('\n'))
    if p.get('extra'): h += p['extra']
    if p.get('img'):
        h += '<figure style="margin:8px 0"><img class="sx-img" src="img/%s" alt="%s" loading="lazy"><figcaption class="mu" style="font-size:15px">Schema (non è uno screenshot esatto)</figcaption></figure>' % (p['img'], E(p.get('alt', '')))
    h += '<button class="fb">Ho fatto!</button></div>\n'
    return h


JS = r"""
(function(){
var SLUG='__SLUG__', ORA=__ORA__, K='st-'+SLUG, KN='nome-0411', CONF={}, NS=__NS__;
function prendi(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(x){return d}}
function metti(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(x){}}
try{if(/[?&]pc=14\b/.test(location.search))localStorage.setItem('pc14','1');if(localStorage.getItem('pc14')==='1')document.body.classList.add('pc14')}catch(x){}
var S=prendi(K,{}), NOME=prendi(KN,'')||'', P=[].slice.call(document.querySelectorAll('.passo'));
var inp=document.getElementById('nome'); inp.value=NOME;
inp.addEventListener('change',function(){var v=inp.value.trim().replace(/\s+/g,' ');if(v.split(' ').length<2){document.getElementById('nomeok').textContent='Scrivi nome e cognome.';return}NOME=v;metti(KN,v);document.getElementById('nomeok').textContent='Ciao '+v+'!';ping(true)});
var ultimo=-1;
function ping(forza){
  if(!CONF.attivo||!CONF.invio||!NOME)return; var fatti=P.filter(function(p){return S[p.dataset.p]}).length; if(fatti===ultimo&&!forza)return; ultimo=fatti;
  var max=0;P.forEach(function(p){if(S[p.dataset.p])max=Math.max(max,+p.dataset.p)});
  var tit=max?P[max-1].querySelector('h2').textContent.replace(/^\d+/,''):'';
  var d={id:'avz-'+SLUG,modo:'avanzamento',classe:'__CLASSE__',nome:NOME,scheda:max,totale:NS,risposte:fatti,titolo:tit,quando:new Date().toISOString()};
  try{fetch(CONF.invio,{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'d='+encodeURIComponent(JSON.stringify(d))})}catch(x){}
}
function disegna(){
  var prossimo=null; P.forEach(function(p){var f=!!S[p.dataset.p];p.classList.toggle('fatto',f);p.classList.remove('ora');p.querySelector('.bollo').textContent=f?'FATTO':'da fare';p.querySelector('.fb').textContent=f?'Fatto ✓ (clic per togliere)':'Ho fatto!';if(!f&&!prossimo)prossimo=p});
  if(prossimo){prossimo.classList.add('ora');prossimo.querySelector('.bollo').textContent='ADESSO'}
  var n=P.filter(function(p){return S[p.dataset.p]}).length;document.getElementById('barra').style.width=Math.round(100*n/P.length)+'%';
  document.getElementById('conta').textContent='Passi fatti: '+n+' su '+P.length+(n===P.length?' — BRAVO, hai finito!':'');
}
P.forEach(function(p){p.querySelector('.fb').onclick=function(){S[p.dataset.p]=!S[p.dataset.p];metti(K,S);disegna();ping(false)}});
[].forEach.call(document.querySelectorAll('pre'),function(pr){var b=document.createElement('button');b.className='cp';b.type='button';b.textContent='Copia';b.onclick=function(){var t=(pr.querySelector('.t')||pr).textContent;try{navigator.clipboard.writeText(t).then(function(){b.textContent='Copiato!'},function(){b.textContent='Seleziona a mano'})}catch(x){b.textContent='Seleziona a mano'}setTimeout(function(){b.textContent='Copia'},1800)};pr.appendChild(b)});
function mostraIP(){var box=document.getElementById('ip'); if(!box)return; var ip=(CONF.server_ip||'').trim(), g=document.getElementById('ipg'); box.classList.toggle('vuoto',!ip); g.textContent=ip?ip:'lo scrive il Prof alla lavagna'}
function giro(){fetch('config.json?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.json()}).then(function(c){CONF=c||{};mostraIP()}).catch(function(){})}
disegna(); giro(); setInterval(giro,30000); setInterval(function(){ping(true)},120000);
})();
"""


def pagina(slug, classe, titolo, sotto, ora, passi, lingue, assist_lingue, extra_top='', extra_mid='', extra_bottom='', h1l=None, ore_gate=None, ip=False, avz=None):
    """Scrive docs/anteprima/<slug>/<nome file> non qui: restituisce l'HTML della pagina a passi."""
    gate = ore_gate if ore_gate is not None else ora
    h = ['<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">',
         '<title>%s</title><script src="ore.js" data-ora="%d"></script><style>%s</style></head><body><main>' % (E(titolo), gate, CSS),
         '<p class="mu">%s</p><h1>%s</h1>%s' % (sotto, titolo, L(h1l or {})),
         '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.' + (' · <span lang="ar">اضغط F5 لرؤية النسخة الجديدة.</span> · <span lang="zh">按 F5 查看新版本。</span>' if 'ar' in lingue else '') + '</p>']
    if ip:
        h.append('<div id="ip" class="vuoto"><b>IP del server (la porta c\'è già)</b><div class="g" id="ipg">lo scrive il Prof alla lavagna</div>'
                 '<p class="bn" lang="bn">সার্ভারের IP ঠিকানা: প্রফেসর বোর্ডে লিখবেন।</p><p class="mu">Si aggiorna da solo ogni 30 secondi.</p></div>')
    h.append(extra_top)
    h.append('<section class="card"><h2>Chi sei?</h2><p>Scrivi nome e cognome: serve al cruscotto per vedere a che punto sei.</p><input type="text" id="nome" autocomplete="name" placeholder="Nome Cognome"><p class="mu" id="nomeok"></p><div class="barra"><i id="barra"></i></div><p id="conta" class="mu"></p></section>')
    h.append(extra_mid)
    h.append('<div class="aiutoprof" style="background:#fde8e8;border:3px solid #c0392b;border-radius:12px;padding:10px 12px;margin:12px 0;color:#000"><p style="font-size:1.1em"><b>Sei bloccato? Scrivi la domanda nella casella dell\'assistente in fondo alla pagina: ti risponde subito. Alza la mano solo se il PC non funziona (non si accende, niente rete, Lazarus non si apre).</b></p>'
             + ('<p class="ar" lang="ar" dir="rtl">إذا علقت، اكتب سؤالك في خانة المساعد أسفل الصفحة: يجيبك فوراً. ارفع يدك فقط إذا كان الحاسوب لا يعمل.</p><p class="zh" lang="zh">卡住了就在页面底部的助手框里写问题，它马上回答。只有电脑坏了才举手。</p>' if 'ar' in lingue else '')
             + ('<p class="bn" lang="bn">আটকে গেলে পেজের নিচে সহকারীর বক্সে প্রশ্ন লেখো। শুধু PC কাজ না করলে হাত তোলো।</p>' if 'bn' in lingue else '') + '</div>')
    for i, p in enumerate(passi, 1):
        h.append(passo_html(i, p))
    h.append(extra_bottom)
    h.append('<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p><div id="aiuto"></div></main>')
    h.append('<script src="../../assistente/assistente.js" data-pagina="%s" data-lingue="%s" data-dove="aiuto"></script>' % (slug, assist_lingue))
    h.append('<script>' + JS.replace('__SLUG__', avz or slug).replace('__ORA__', str(ora)).replace('__NS__', str(len(passi))).replace('__CLASSE__', classe) + '</script></body></html>')
    return '\n'.join(h)
