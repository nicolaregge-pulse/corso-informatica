#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""3INF mercoledì 04/11/2026, 12-14: «Il protocollo del Mastermind» (v4.0). Trasforma la bozza classe-3/lezioni-bozza/2026-11-04_protocollo-rete/
in docs/anteprima/3inf-protocollo-04-11/ (cartella NON linkata). Ora 1 = index.html, ora 2 = ora2.html (ore_sbloccate: 1 = solo ora 1 aperta, regola 31).
Nessun nome di ragazzi. Quiz: segnaposto __QUIZ3__ sostituito col link del Modulo creato dal ponte (strumenti/riempi_link_protocollo_04_11.py o a mano)."""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_pagine_lezione import svg, SLUGDIR, INVIO
SLUG = '3inf-protocollo-04-11'; D = SLUGDIR + SLUG + '/'; os.makedirs(D + 'img', exist_ok=True)
B = '/home/user/corso-informatica/classe-3/lezioni-bozza/2026-11-04_protocollo-rete/'
SRC = SLUGDIR + '1inf-deepfake-03-11/'
QUIZ = os.environ.get('QUIZ3', '__QUIZ3__')

# ---- immagini dei passi nuovi (schemi, dichiarati come schemi)
svg(D + 'img/zip.svg', 'Scarica e apri lo zip', [('btn', 'Scarica il progetto (zip)', 80, 90, 640), ('box', 'Esplora file ▸ Download ▸ clic destro sul file\n▸ Estrai tutto ▸ Estrai', 80, 200, 640, 110)], (0, 1), 'Poi apri la cartella che si è creata')
svg(D + 'img/collegato.svg', 'Sei collegato', [('lbl', 'Collegato! Ciao …', 80, 120), ('btn', 'Sono collegato', 80, 160, 420), ('box', 'Premilo solo se in basso nel client\nvedi «Collegato!»', 80, 250, 640, 100)], (0, 1), 'Il Prof controlla anche sul suo server')
svg(D + 'img/link-commit.svg', 'Il link del commit', [('box', 'Nel tuo repository clicca il commit\n(la riga con il tuo messaggio)', 40, 70, 720, 90), ('edit', 'https://github.com/…/commit/…', 40, 190, 720), ('btn', 'Manda al prof', 40, 260, 300)], (0, 2), 'Incolla il link e premi il bottone: arriva da solo')
svg(D + 'img/quiz.svg', 'Quiz su Google Moduli', [('box', '12 domande sulla rete\nalmeno 8 giuste per un buon voto', 80, 90, 640, 100), ('btn', 'Apri il quiz', 160, 240, 480)], (1,), 'Il quiz è la prova: lavoro tuo')
def img(f, alt): return '<figure style="margin:8px 0"><img src="img/%s" alt="%s" style="width:100%%;border:1px solid var(--bd);border-radius:8px"><figcaption class="small">Schema (non è uno screenshot esatto)</figcaption></figure>' % (f, alt)

# ---- blocchi comuni
EXTRA_CSS = ('.bn{display:none}body.pc14 .bn{display:block}.f5{font-weight:700}.barra{background:var(--bd);border-radius:8px;height:14px}.barra i{display:block;height:14px;border-radius:8px;background:var(--ok);width:0}'
             '.ok2{background:var(--bn);border:2px solid var(--ok);border-radius:10px;padding:8px 12px}#ore-chiuso{color:#111}')
F5 = '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>'
def alto(ora):
    return (F5 + '<section class="card"><h2>Chi sei?</h2><p>Scrivi nome e cognome: serve al cruscotto per vedere a che punto sei.</p>'
            '<input type="text" id="chisei" autocomplete="name" placeholder="Nome Cognome" style="font:inherit;padding:8px;border:2px solid var(--bd);border-radius:8px;width:100%;max-width:420px;background:var(--card);color:var(--fg)">'
            '<p class="small" id="chiseiok"></p></section>'
            '<section class="card"><h2>Il tuo andamento e gli aiuti</h2><a class="bt" href="cruscotto-ragazzi.html">Come sto andando</a> <a class="bt alt" href="../../3inf-monitor/">Il monitor della lezione</a>'
            + ('<a class="bt alt" href="animazione-protocollo.html" target="_blank" rel="noopener">L\'animazione (si apre in una scheda)</a>' if ora == 1 else '<a class="bt alt" href="./">Torna all\'ora 1</a>')
            + '<p class="small">Sei bloccato? Scrivi la domanda nella casella dell\'assistente in fondo alla pagina: ti risponde subito. Alza la mano solo se il PC non funziona.</p></section>')
BASSO = ('<div id="aiuto"></div></main><script src="../../assistente/assistente.js" data-pagina="' + SLUG + '" data-lingue="it" data-dove="aiuto"></script>')
COMMON_JS = r"""<script>(function(){
function $(i){return document.getElementById(i)}function pr(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(x){return d}}function me(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(x){}}
try{if(/[?&]pc=14\b/.test(location.search))localStorage.setItem('pc14','1');if(localStorage.getItem('pc14')==='1')document.body.classList.add('pc14')}catch(x){}
var C={},NOME=pr('nome-0411','');$('chisei').value=NOME;
$('chisei').addEventListener('change',function(){var v=$('chisei').value.trim().replace(/\s+/g,' ');if(v.split(' ').length<2){$('chiseiok').textContent='Scrivi nome e cognome.';return}NOME=v;me('nome-0411',v);$('chiseiok').textContent='Ciao '+v+'!'});
function conf(cb){fetch('config.json?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.json()}).then(function(c){C=c||{};if(cb)cb()}).catch(function(){})}
window.INV=function(d,msg){d.classe='3INF';d.nome=NOME;d.quando=new Date().toISOString();if(!NOME||NOME.split(' ').length<2){msg.textContent='Scrivi prima nome e cognome nella casella «Chi sei?» in alto.';return}
 if(!C.attivo||!C.invio){msg.textContent='ANTEPRIMA: invio spento.';return}
 var f=document.createElement('form');f.method='POST';f.action=C.invio;f.target='_blank';f.acceptCharset='UTF-8';var i=document.createElement('input');i.type='hidden';i.name='d';i.value=JSON.stringify(d);f.appendChild(i);document.body.appendChild(f);f.submit();f.remove();
 msg.textContent='Mandato! Si è aperta una scheda con scritto «Consegna arrivata al prof».'};
var ult=-1;function ping(){if(!C.attivo||!C.invio||!NOME)return;var k=window.AVZ?window.AVZ():{s:0,r:0};var key=k.s+'/'+k.r;if(key===ult)return;ult=key;
 var d={id:'avz-3inf-protocollo-0411',modo:'avanzamento',classe:'3INF',nome:NOME,scheda:k.s,totale:k.t,risposte:k.r,titolo:k.n||'',quando:new Date().toISOString()};
 try{fetch(C.invio,{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'d='+encodeURIComponent(JSON.stringify(d))})}catch(x){}}
conf(function(){if(window.DOPO)window.DOPO(C)});setInterval(function(){conf(function(){if(window.DOPO)window.DOPO(C)})},30000);setInterval(ping,20000);
})();</script>"""

def pulisci_testa(s, ora, titolo):
    s = re.sub(r'<div class="bozza">.*?</div>', '', s, count=1, flags=re.S)
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex"><script src="ore.js" data-ora="%d"></script>' % ora, 1)
    s = s.replace('</style></head>', EXTRA_CSS + '</style></head>', 1)
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % titolo, s, count=1)
    return s

# ================= ORA 1
s = open(B + 'lezione.html', encoding='utf-8').read()
s = pulisci_testa(s, 1, 'Il protocollo del Mastermind')
s = re.sub(r'(<h1>.*?</h1><p class="small">.*?</p>)', lambda m: m.group(1) + alto(1), s, count=1, flags=re.S) if '<p class="small">' in s else s
s = s.replace('Ora 1 di 2 (le ore successive sono bloccate). ', 'Ora 1 di 2 (le ore successive sono bloccate). ')
# blocco ora 2: si apre da config
s = s.replace('<p id="ora2link" style="display:none">', '<p id="ora2link" style="display:none">')
cnt = ('<script>window.AVZ=function(){var n=0;var t=document.getElementById("conta");if(t)n=parseInt(t.textContent)||0;return{s:n,t:5,r:n,n:"Prof finto: risposte scoperte"}};'
       'window.DOPO=function(c){var ok=(c.ore_sbloccate||0)>=2;var m=document.getElementById("lockmsg"),l=document.getElementById("ora2link");if(l)l.style.display=ok?"block":"none";if(m)m.style.display=ok?"none":"block"};</script>')
s = s.replace('</main><script>', '</main>' + cnt + '<script>', 1) if '</main><script>' in s else s
s = s.replace('</main>', BASSO.replace('</main>', '') + '</main>', 1) if False else s
# assistente + comuni prima della chiusura body
s = s.replace('</main>', '<div id="aiuto"></div></main><script src="../../assistente/assistente.js" data-pagina="%s" data-lingue="it" data-dove="aiuto"></script>' % SLUG, 1)
s = s.replace('</body>', COMMON_JS + '</body>')
open(D + 'index.html', 'w', encoding='utf-8').write(s)

# ================= ORA 2
o = open(B + 'ora2.html', encoding='utf-8').read()
o = pulisci_testa(o, 2, 'Ora 2 - il client collegato')
o = re.sub(r'(<h1>.*?</h1><p class="small">.*?</p>)', lambda m: m.group(1) + alto(2), o, count=1, flags=re.S)
passo0 = ('<section class="card"><h2>0. Scarica il progetto</h2><p>Premi il bottone: si scarica la cartella compressa con il Mastermind versione 4. Poi apri <b>Esplora file</b>, vai in <b>Download</b>, clic destro sul file e scegli <b>Estrai tutto</b>.</p>'
          '<a class="bt" href="mastermind-bello-v4.0.zip" download>Scarica il progetto (zip)</a>' + img('zip.svg', 'Schema: scarica e apri lo zip') + '</section>')
o = o.replace('<section class="card"><h2>1. Apri il client versione 4</h2>', passo0 + '<section class="card"><h2>1. Apri il client versione 4</h2>', 1)
# passo 4: segnale collegato
o = o.replace('Questo è il momento che conta per il voto: client collegato.</p>', 'Questo è il momento che conta per il voto: client collegato.</p><button type="button" class="bt" id="bcoll">Sono collegato</button> <span class="small" id="mcoll"></span>' + img('collegato.svg', 'Schema: sono collegato'), 1)
# commit: niente "copia": esempio + invio diretto
o = o.replace('Per il messaggio del commit puoi copiare questo (oppure scrivere uno tuo, più bello):', 'Esempio di messaggio chiaro (scrivi il tuo, con parole tue):')
form = ('<section class="card"><h2>10b. Manda il link del commit</h2><p>Nel repository clicca il commit (la riga con il tuo messaggio). Scrivi qui sotto l\'indirizzo che vedi nella barra del browser e premi il bottone: arriva da solo al Prof.</p>'
        '<input type="text" id="urlcommit" placeholder="https://github.com/…/commit/…" style="font:inherit;padding:8px;border:2px solid var(--bd);border-radius:8px;width:100%;background:var(--card);color:var(--fg)"> '
        '<button type="button" class="bt" id="mcommit">Manda al prof</button><p class="small" id="msgcommit"></p>' + img('link-commit.svg', 'Schema: il link del commit') + '</section>')
o = o.replace('<section class="card"><h2>11. Il quiz sulla rete</h2>', form + '<section class="card"><h2>11. Il quiz sulla rete</h2>', 1)
o = re.sub(r'(<h2>11\. Il quiz sulla rete</h2><p>.*?</p>)', lambda m: m.group(1).replace('Il link del quiz compare qui quando il Prof lo apre (Modulo).', 'Premi il bottone verde: si apre il Modulo Google.') + '<a class="bt" style="background:var(--ok);border-color:var(--ok)" href="%s" target="_blank" rel="noopener">Apri il quiz</a>' % QUIZ + img('quiz.svg', 'Schema: il quiz'), o, count=1, flags=re.S)
o = o.replace('</main>', '<div id="aiuto"></div></main><script src="../../assistente/assistente.js" data-pagina="%s-ora2" data-lingue="it" data-dove="aiuto"></script>' % SLUG, 1)
agg = ('<script>(function(){function $(i){return document.getElementById(i)}var fatto={};'
       '$("bcoll").onclick=function(){fatto.coll=1;INV({id:"3inf-collegato-0411",modo:"verifica",cosa:"collegato"},$("mcoll"))};'
       '$("mcommit").onclick=function(){var u=$("urlcommit").value.trim();if(!/^https:\\/\\/github\\.com\\/.+\\/commit\\/[0-9a-f]{7,}/i.test(u)){$("msgcommit").textContent="Il link deve cominciare con https://github.com/ e contenere /commit/. Controlla di aver cliccato il commit.";return}fatto.com=1;INV({id:"3inf-commit-0411",modo:"verifica",cosa:"commit",url:u},$("msgcommit"))};'
       'window.AVZ=function(){var r=(fatto.coll?1:0)+(fatto.com?1:0);return{s:r,t:2,r:r,n:"Ora 2: collegato e commit"}}})();</script>')
o = o.replace('</body>', agg + COMMON_JS + '</body>')
open(D + 'ora2.html', 'w', encoding='utf-8').write(o)

# ---- file e cartella
shutil.copy(SRC + 'ore.js', D + 'ore.js'); shutil.copy(SRC + 'cruscotto.css', D + 'cruscotto.css')
for f in ('mastermind-bello-v4.0.zip', 'animazione-protocollo.html'): shutil.copy(B + f, D + f)
json.dump({"invio": INVIO, "attivo": True, "ore_sbloccate": 1, "_nota": "3INF 04/11/2026, Il protocollo del Mastermind (v4.0). ore_sbloccate 1 = solo ora 1 aperta; ora 2 (ora2.html) si apre alzando a 2 (regola 31, strumenti/sblocca_ora.py). NON LINKATA, NON PUBBLICATA.",
           "server_ip": ""}, open(D + 'config.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', D)
