#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2INF lunedì 02/11/2026 · pagine per i ragazzi (ANTEPRIMA, solo italiano): index, pratica, scheda, analizza, proietta, extra, config.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mails import MAILS, INDIZI
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../docs/anteprima/2inf-reti-02-11/')
PAG = '2inf-reti-02-11'
INVIO = json.load(open(os.path.join(OUT, '../1inf-lab-30-10/config.json')))['invio']
CSS = """:root{--bg:#f6f7f9;--fg:#1f2328;--mu:#5b6573;--card:#fff;--bd:#d5dbe3;--acc:#0b6e99;--ok:#1a7f37;--ko:#c0392b;--q:#fff4c2;--blu:#1f6feb}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--ko:#f85149;--q:#3b3200}}
:root[data-theme="dark"]{--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--ko:#f85149;--q:#3b3200}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.5 system-ui,"Segoe UI",sans-serif}
main{max-width:820px;margin:0 auto;padding:12px 16px 60px}h1{font-size:1.45em;margin:.4em 0}h2{font-size:1.2em;margin:.2em 0 .4em}h3{font-size:1.05em;margin:.8em 0 .3em}
.f5{background:var(--q);border-radius:10px;padding:8px 12px;font-size:.95em}.mu{color:var(--mu);font-size:.92em}
a.bt,button.bt{display:block;width:100%;text-align:center;background:var(--acc);color:#fff;font:inherit;font-weight:700;font-size:1.1em;padding:14px;border-radius:10px;text-decoration:none;margin:8px 0;border:0;cursor:pointer}
a.bt.v,button.bt.v{background:var(--ok)}a.bt.b{background:#fff0;color:var(--acc);border:2px solid var(--acc);font-weight:600;font-size:1em;padding:10px}button.bt[disabled]{opacity:.45;cursor:not-allowed}
.passo{border:3px solid var(--blu);border-radius:14px;padding:8px 14px 12px;margin:16px 0;background:var(--card)}
.passo .num{display:inline-flex;width:42px;height:42px;border-radius:50%;background:var(--blu);color:#fff;align-items:center;justify-content:center;font-weight:800;margin-right:8px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:10px 14px;margin:12px 0}
.vinci{border-color:var(--ok);background:rgba(26,127,55,.07)}.fatto{color:var(--ok);font-weight:800}
ol.pp{padding-left:1.3em}ol.pp li{margin:.5em 0}code,kbd{background:rgba(127,127,127,.18);border-radius:5px;padding:1px 6px;font-family:Consolas,monospace}
input[type=text],textarea,select{font:inherit;width:100%;padding:8px 10px;border:2px solid var(--acc);border-radius:10px;background:var(--card);color:var(--fg)}textarea{min-height:86px}
.msg{font-weight:700}.msg.ok{color:var(--ok)}.msg.ko{color:var(--ko)}
.ore{border-top:1px solid var(--bd);padding-top:8px;margin-top:8px}
.mailimg{width:100%;border:1px solid var(--bd);border-radius:8px;display:block}
.sc{display:flex;gap:10px;margin:10px 0}.sc label{flex:1;text-align:center;border:3px solid var(--bd);border-radius:12px;padding:12px 6px;font-weight:800;cursor:pointer;background:var(--card)}
.sc input{position:absolute;opacity:0;pointer-events:none}.sc label.sel{border-color:var(--blu);background:rgba(31,111,235,.12)}
.ind label{display:block;padding:6px 10px;border:1px solid var(--bd);border-radius:8px;margin:4px 0;cursor:pointer;background:var(--card)}.ind label.sel{border-color:var(--blu);background:rgba(31,111,235,.10)}
.ris{border-left:6px solid var(--ok);padding:6px 12px;margin:8px 0;background:var(--card);border-radius:8px}.ris.ko{border-color:var(--ko)}"""
HEAD0 = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>%s</title><style>' + CSS + '</style></head><body><main>'
class _H(str):
    def __mod__(self, t): return str(self).replace('%s', t, 1)
HEAD = _H(HEAD0)
F5 = '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>'
ASS = '<script src="../../assistente/assistente.js" data-pagina="' + PAG + '" data-lingue="it"></script>'
def scrivi(nome, h):
    open(OUT + nome, 'w', encoding='utf-8').write(h)
JSCOMUNE = """
function $(i){return document.getElementById(i)}
function prendi(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(x){return d}}
function metti(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(x){}}
var CONF={};fetch('config.json?t='+Date.now()).then(function(r){return r.json()}).then(function(c){CONF=c||{}}).catch(function(){CONF={}});
function posta(d){return fetch(CONF.invio,{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'d='+encodeURIComponent(JSON.stringify(d))})}
function postaForm(d){var f=document.createElement('form');f.method='POST';f.action=CONF.invio;f.target='_blank';f.acceptCharset='UTF-8';var i=document.createElement('input');i.type='hidden';i.name='d';i.value=JSON.stringify(d);f.appendChild(i);document.body.appendChild(f);f.submit();f.remove()}
function parole(t){return String(t||'').trim().split(/\\s+/).filter(Boolean).length}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
"""

# ---------------- HUB ----------------
hub = HEAD % 'Laboratorio 2INF oggi' + """
<h1>OGGI 2/11 · Laboratorio 2INF: tutto qui</h1>
<p>Questa è l'unica pagina di oggi. Fai i passi in ordine, dall'alto in basso. Oggi vedi come parla il tuo PC in rete e impari a riconoscere le mail false.</p>
""" + F5 + """

<section class="passo"><h2><span class="num">1</span>PASSO 1 · La teoria: come parla il mio PC in rete</h2>
<p>6 schede piccole: rete, indirizzo IP, indirizzo MAC, gateway, DNS, DHCP. Leggile con calma. Poi fai il ripasso: ti dice subito se hai capito.</p>
<a class="bt v" href="../../verifica/?b=2inf-reti-ip" target="_blank" rel="noopener">Apri le 6 schede e il ripasso</a>
</section>

<section class="passo"><h2><span class="num">2</span>PASSO 2 · La pratica: la scheda d'identità del mio PC</h2>
<p>Leggi i numeri del tuo PC dalle Impostazioni di Windows (senza scrivere comandi) e compila il tuo Documento su Classroom. Il primo numero lo trovi in 2 minuti.</p>
<a class="bt" href="pratica.html">Apri i passi della pratica</a>
<div class="ore"><p><b>Quando hai finito il Documento:</b> il quiz di chiusura sulla rete. Si apre quando lo dice il Professore.</p>
<a class="bt b" href="../../verifica/?b=2inf-reti-ip&amp;modo=verifica" target="_blank" rel="noopener">Quiz di chiusura sulla rete</a></div>
</section>

<section class="passo"><h2><span class="num">3</span>PASSO 3 · Sicurezza: riconosco le mail false (phishing)</h2>
<p>Prima le schede (come si riconosce una truffa). Poi guardiamo insieme le mail sullo schermo grande. Poi analizzi tu 8 mail: sicura o phishing, e perché.</p>
<a class="bt v" href="../../verifica/?b=2inf-phishing" target="_blank" rel="noopener">Apri le schede sul phishing e il ripasso</a>
<a class="bt" href="analizza.html">Analizza le 8 mail</a>
</section>

<section class="passo"><h2><span class="num">4</span>PASSO 4 · Se hai finito: il mio budget in Fogli (extra)</h2>
<p>Solo quando hai finito i passi 1, 2 e 3. Costruisci un foglio di calcolo con le tue spese inventate: somma, media e un semaforo che diventa rosso.</p>
<a class="bt" href="extra.html">Apri l'extra: il mio budget</a>
</section>

<div class="aiutoprof" style="background:#fde8e8;border:3px solid #c0392b;border-radius:12px;padding:10px 12px;margin:16px 0;color:#000"><p style="font-size:1.25em;margin:0 0 6px"><b>Hai una domanda? Scrivila nella casella dell'assistente qui sotto.</b></p><p style="margin:0;font-size:.9em;color:#333">Al Professore ti rivolgi solo per cose del PC che non funziona, un account bloccato o un problema di comportamento.</p></div>

<section class="passo" style="border-color:var(--ok)"><h2>Il mio andamento</h2>
<p>Guarda a che punto sei e che cosa ti manca.</p>
<a class="bt v" href="cruscotto-ragazzi.html">Il mio andamento di oggi</a></section>
""" + F5 + """
<p class="mu" style="text-align:center"><a href="cruscotto.html">Cruscotto del Professore</a> (dati cifrati, solo per il docente) · <a href="proietta.html">Mail sullo schermo grande</a></p>
</main>""" + ASS + "</body></html>"
scrivi('index.html', hub)

# ---------------- PRATICA ----------------
prat = HEAD % 'Pratica: i numeri del mio PC' + """
<p class="mu"><a href="./">&larr; Torna alla pagina di oggi</a></p>
<h1>PASSO 2 · I numeri del mio PC</h1>
<p>Oggi non scrivi nessun comando: clicchi e leggi. Ogni passo è una cosa sola. Se ti sbagli, non succede niente: si torna indietro e si riprova (succede a tutti, anche ai professionisti).</p>
""" + F5 + """
<section class="card vinci"><h2>Vinci subito: il tuo indirizzo IP (2 minuti)</h2>
<ol class="pp">
<li>In basso a sinistra clicca il bottone <b>Start</b> (l'icona di Windows).</li>
<li>Clicca l'ingranaggio <b>Impostazioni</b>.</li>
<li>Clicca <b>Rete e Internet</b>.</li>
<li>Clicca <b>Ethernet</b> (se il PC ha il cavo) oppure <b>Wi-Fi</b>. Scegli quello con scritto «Connesso».</li>
<li>Clicca <b>Proprietà</b> (a volte si chiama <b>Proprietà hardware</b>).</li>
<li>Cerca la riga <b>Indirizzo IPv4</b>. Il numero a destra (quattro numeri con i punti) è il <b>tuo indirizzo IP</b>.</li>
</ol>
<p class="fatto">FATTO! Hai trovato l'indirizzo IP del tuo PC. Dillo al compagno: «Il mio PC è il 192.168...» (scrivi il tuo).</p></section>

<section class="card"><h2>Poi: MAC e DNS (nella stessa pagina)</h2>
<ol class="pp">
<li>Resta nella pagina delle Proprietà. Cerca <b>Indirizzo fisico (MAC)</b>: sono sei coppie di numeri e lettere. È il numero di serie della scheda di rete.</li>
<li>Cerca <b>Server DNS IPv4</b>: è l'indirizzo della «rubrica» che traduce i nomi dei siti.</li>
</ol><p class="fatto">FATTO! Hai trovato 3 numeri su 4.</p></section>

<section class="card"><h2>Il gateway (il quarto numero)</h2>
<ol class="pp">
<li>Premi il tasto <kbd>Windows</kbd> sulla tastiera.</li>
<li>Scrivi: <b>connessioni di rete</b> (scrivi solo queste parole, non è un comando).</li>
<li>Clicca <b>Visualizza connessioni di rete</b>.</li>
<li>Fai doppio clic sulla connessione accesa (quella a colori, non quella grigia).</li>
<li>Clicca il bottone <b>Dettagli…</b>.</li>
<li>Cerca <b>Gateway predefinito IPv4</b>: è l'indirizzo del <b>router</b>, la porta verso Internet.</li>
</ol>
<p class="mu">Piano B: questa finestra «Dettagli» ha tutti e quattro i numeri insieme (IP, MAC, gateway, DNS). Se nelle Impostazioni non trovi una riga, cercala qui.</p>
<p class="fatto">FATTO! Hai tutti e 4 i numeri.</p></section>

<section class="card"><h2>Fallo tuo: la scheda d'identità del mio PC</h2>
<ol class="pp">
<li>Torna su <b>Classroom</b> e apri il compito di oggi.</li>
<li>Apri il Documento <b>«La scheda d'identità del mio PC»</b> (è la tua copia).</li>
<li>Scegli un <b>nome simpatico</b> per il tuo PC e scrivilo in alto.</li>
<li>Scrivi nella tabella i 4 numeri e se la connessione è a cavo o Wi-Fi.</li>
<li>Scrivi le 4 righe «Con parole mie»: a cosa serve l'IP, il MAC, il gateway, il DNS. Con parole tue, non copiate.</li>
<li>Fai lo screenshot: premi insieme <kbd>Windows</kbd> + <kbd>Maiusc</kbd> + <kbd>S</kbd>, disegna un rettangolo sulla finestra dei numeri, poi nel Documento premi <kbd>Ctrl</kbd> + <kbd>V</kbd>.</li>
<li>Su Classroom premi <b>Consegna</b>.</li>
</ol>
<p class="mu">Questi numeri servono solo per la scheda di oggi: non pubblicarli fuori dalla classe.</p>
<p class="fatto">FATTO! La tua scheda è consegnata: è il tuo primo lavoro di oggi, mostralo al compagno.</p></section>

<section class="card"><h2>Il Documento non si apre? Piano B</h2>
<p>Se il Documento su Classroom non si apre, compila la scheda qui: un bottone la manda al Professore.</p>
<a class="bt b" href="scheda.html">Compila la scheda in questa pagina</a></section>
""" + F5 + "</main>" + ASS + "</body></html>"
scrivi('pratica.html', prat)

# ---------------- SCHEDA (piano B della consegna) ----------------
sched = HEAD % 'La scheda del mio PC' + """
<p class="mu"><a href="pratica.html">&larr; Torna ai passi della pratica</a></p>
<h1>La scheda d'identità del mio PC</h1>
<p>Piano B: usa questa pagina solo se il Documento su Classroom non funziona. Scrivi con parole tue.</p>
<section class="card"><h2>1. Chi sei?</h2><input type="text" id="nome" placeholder="Nome Cognome" autocomplete="name"></section>
<section class="card"><h2>2. Il nome del mio PC (scegli tu)</h2><input type="text" id="pc" placeholder="Per esempio: Il Razzo"></section>
<section class="card"><h2>3. I miei numeri</h2>
<p>Indirizzo IP</p><input type="text" id="ip" placeholder="Per esempio 192.168.1.25">
<p>Indirizzo MAC</p><input type="text" id="mac" placeholder="Per esempio 5C-BA-EF-12-34-56">
<p>Gateway</p><input type="text" id="gw" placeholder="Per esempio 192.168.1.1">
<p>DNS</p><input type="text" id="dns" placeholder="Per esempio 192.168.1.1">
<p>Connessione</p><select id="conn"><option value="">Scegli…</option><option>Cavo (Ethernet)</option><option>Wi-Fi</option></select></section>
<section class="card"><h2>4. Con parole mie</h2>
<p>A cosa serve l'IP?</p><textarea id="p_ip"></textarea><p>A cosa serve il MAC?</p><textarea id="p_mac"></textarea>
<p>A cosa serve il gateway?</p><textarea id="p_gw"></textarea><p>A cosa serve il DNS?</p><textarea id="p_dns"></textarea></section>
<section class="card"><h2>5. Il mio screenshot (facoltativo)</h2><p class="mu">Scegli l'immagine che hai salvato con Windows + Maiusc + S.</p><input type="file" id="img" accept="image/*"><div id="anteprima"></div></section>
<section class="card"><h2>6. Manda al prof</h2><button class="bt v" id="manda" disabled>Manda al prof</button><p class="msg" id="msg"></p></section>
""" + F5 + "</main>" + ASS + """<script>""" + JSCOMUNE + """
var IMG=null,CH=['nome','pc','ip','mac','gw','dns','conn','p_ip','p_mac','p_gw','p_dns'],SALVA=prendi('scheda-0211',{});
CH.forEach(function(k){if(SALVA[k])$(k).value=SALVA[k];$(k).addEventListener('input',function(){SALVA[k]=$(k).value;metti('scheda-0211',SALVA);pronto()})});
function pronto(){var ok=$('nome').value.trim().split(/\\s+/).length>=2&&$('ip').value.trim()&&$('mac').value.trim()&&$('gw').value.trim()&&$('dns').value.trim()&&$('conn').value&&['p_ip','p_mac','p_gw','p_dns'].every(function(k){return parole($(k).value)>=4});$('manda').disabled=!ok}
$('img').onchange=function(){var f=$('img').files[0];IMG=null;$('anteprima').innerHTML='';if(!f)return;var r=new FileReader();r.onload=function(){var url=String(r.result),im=new Image();im.onload=function(){$('anteprima').innerHTML='<img alt="il tuo screenshot" style="max-width:100%;max-height:240px;border-radius:8px" src="'+url+'">';try{var w=Math.min(1400,im.naturalWidth),h=Math.round(im.naturalHeight*w/im.naturalWidth),c=document.createElement('canvas');c.width=w;c.height=h;c.getContext('2d').drawImage(im,0,0,w,h);IMG={nome:'scheda_pc_screenshot.jpg',tipo:'image/jpeg',b64:c.toDataURL('image/jpeg',0.7).split(',')[1],originale:f.name}}catch(x){IMG={nome:f.name,tipo:f.type,b64:url.split(',')[1],originale:f.name}}};im.src=url};r.readAsDataURL(f)};
function costruisci(){var base={id:'2inf-reti-0211-scheda',modo:'verifica',classe:'2INF',nome:$('nome').value.trim().replace(/\\s+/g,' ')},out=[],P=200000;
 if(IMG){var parti=Math.max(1,Math.ceil(IMG.b64.length/P));for(var k=0;k<parti;k++)out.push(Object.assign({},base,{cosa:'screenshot',file:IMG.nome,parte:k+1,parti:parti,base64:IMG.b64.slice(k*P,(k+1)*P),quando:new Date().toISOString()}))}
 out.push(Object.assign({},base,{cosa:'scheda',pc:$('pc').value.trim(),ip:$('ip').value.trim(),mac:$('mac').value.trim(),gateway:$('gw').value.trim(),dns:$('dns').value.trim(),connessione:$('conn').value,
  parole_mie:{ip:$('p_ip').value,mac:$('p_mac').value,gateway:$('p_gw').value,dns:$('p_dns').value},screenshot:IMG?{file:IMG.nome}:null,consegnata:true,quando:new Date().toISOString()}));return out}
window.costruisci=costruisci;
$('manda').onclick=async function(){pronto();if($('manda').disabled)return;var inv=costruisci();
 if(!CONF.attivo||!CONF.invio){$('msg').className='msg ko';$('msg').textContent='ANTEPRIMA: invio spento. Partirebbero '+inv.length+' invii.';return}
 $('manda').disabled=true;$('msg').className='msg';$('msg').textContent='Sto mandando…';
 try{for(var i=0;i<inv.length-1;i++){await posta(inv[i]);await new Promise(function(o){setTimeout(o,1300)})}
  await posta(inv[inv.length-1]);postaForm(inv[inv.length-1]);$('msg').className='msg ok';$('msg').textContent='Mandato! Si è aperta una scheda con scritto «Consegna arrivata al prof». Se non la vedi, consegna anche su Classroom.';metti('scheda-0211-fatta',new Date().toISOString())}
 catch(x){$('msg').className='msg ko';$('msg').textContent='Non è partito. Premi di nuovo «Manda al prof».';$('manda').disabled=false}};
pronto();
</script></body></html>"""
scrivi('scheda.html', sched)

# ---------------- ANALIZZA (phishing) ----------------
MJ = [dict(n=m['n'], ok=m['ok'], ind=m['indizi'], sp=m['spiega']) for m in MAILS]
card = ''
for m in MAILS:
    card += ('<section class="card" id="m%d"><h2>Mail %d di 8</h2><img class="mailimg" src="mail/mail-%d.png" alt="Mail %d">'
             '<h3>Che cosa pensi?</h3><div class="sc" data-n="%d"><label><input type="radio" name="d%d" value="sicura">Sicura</label><label><input type="radio" name="d%d" value="phishing">Phishing</label></div>'
             '<h3>Quali indizi vedi? (scegli quelli che trovi)</h3><div class="ind" data-n="%d">%s</div></section>'
             % (m['n'], m['n'], m['n'], m['n'], m['n'], m['n'], m['n'], m['n'],
                ''.join('<label><input type="checkbox" value="%s"> %s</label>' % (k, v) for k, v in INDIZI.items())))
anal = HEAD % 'Analizza le 8 mail' + """
<p class="mu"><a href="./">&larr; Torna alla pagina di oggi</a></p>
<h1>PASSO 3 · Analizza le 8 mail</h1>
<p>Sono mail finte, fatte per la lezione: nessun marchio è vero. Per ogni mail: scegli <b>Sicura</b> o <b>Phishing</b>, poi segna gli indizi che vedi. Alla fine due domande con parole tue e un bottone per consegnare. Tre mail sono sicure e cinque sono phishing.</p>
<p class="mu">Non c'è fretta e nessuno ti giudica: sbagliare qui serve a imparare. Il risultato lo vedi subito dopo la consegna.</p>
""" + F5 + """
<section class="card"><h2>Chi sei?</h2><input type="text" id="nome" placeholder="Nome Cognome" autocomplete="name"></section>
<p class="mu" id="conta">Mail fatte: 0 su 8</p>
""" + card + """
<section class="card"><h2>Due domande con parole tue</h2>
<p><b>1. Che cosa fai se ricevi una mail così?</b></p><textarea id="q1" placeholder="Scrivi qui, con parole tue."></textarea>
<p><b>2. Come controlli il mittente?</b></p><textarea id="q2" placeholder="Scrivi qui, con parole tue."></textarea>
<p class="mu" id="cp"></p></section>
<section class="card"><h2>Consegna</h2><button class="bt v" id="manda" disabled>Consegna al prof</button><p class="msg" id="msg"></p><div id="ris"></div></section>
""" + F5 + "</main>" + ASS + """<script>""" + JSCOMUNE + """
var M=""" + json.dumps(MJ, ensure_ascii=False) + """,IND=""" + json.dumps(INDIZI, ensure_ascii=False) + """,ST=prendi('analizza-0211',{nome:'',d:{},i:{},q1:'',q2:'',fatto:null});
function salva(){metti('analizza-0211',ST)}
function conta(){var n=Object.keys(ST.d).length;$('conta').textContent='Mail fatte: '+n+' su 8';var a=parole(ST.q1),b=parole(ST.q2);$('cp').textContent='Parole scritte: domanda 1 = '+a+', domanda 2 = '+b+' (ne servono almeno 6 per ognuna).';
 $('manda').disabled=!(ST.nome.trim().split(/\\s+/).length>=2&&n===8&&a>=6&&b>=6)}
function disegna(){document.querySelectorAll('.sc').forEach(function(s){var n=s.dataset.n;s.querySelectorAll('label').forEach(function(l){var v=l.querySelector('input').value;l.className=ST.d[n]===v?'sel':'';l.querySelector('input').checked=ST.d[n]===v})});
 document.querySelectorAll('.ind').forEach(function(s){var n=s.dataset.n,sel=ST.i[n]||[];s.querySelectorAll('label').forEach(function(l){var c=l.querySelector('input');c.checked=sel.indexOf(c.value)>=0;l.className=c.checked?'sel':''})});conta()}
document.querySelectorAll('.sc input').forEach(function(r){r.addEventListener('change',function(){ST.d[r.closest('.sc').dataset.n]=r.value;salva();disegna()})});
document.querySelectorAll('.ind input').forEach(function(c){c.addEventListener('change',function(){var n=c.closest('.ind').dataset.n,s=(ST.i[n]||[]).filter(function(x){return x!==c.value});if(c.checked)s.push(c.value);ST.i[n]=s;salva();disegna()})});
$('nome').value=ST.nome;$('nome').addEventListener('input',function(){ST.nome=$('nome').value;salva();conta()});
$('q1').value=ST.q1;$('q2').value=ST.q2;$('q1').addEventListener('input',function(){ST.q1=$('q1').value;salva();conta()});$('q2').addEventListener('input',function(){ST.q2=$('q2').value;salva();conta()});
function costruisci(st){var cr=M.map(function(m){var data=st.d[m.n]||'(nessuna)',giusta=m.ok?'sicura':'phishing',sc=(st.i[m.n]||[]).slice().sort().join(''),gi=m.ind.split('').sort().join('');
 return{area:'ph',tema:'mail'+m.n,q:'Mail '+m.n,data:data,giusta:giusta,ok:data===giusta,indizi_scelti:sc,indizi_giusti:gi,indizi_ok:sc===gi}});
 var g=cr.filter(function(c){return c.ok}).length;
 return{id:'2inf-phishing-analisi',modo:'verifica',classe:'2INF',nome:st.nome.trim().replace(/\\s+/g,' '),quando:new Date().toLocaleString('it-IT'),consegnata:true,punteggio:g,su:8,
  crocette:cr,aperte:[{area:'mia',tema:'cosa',q:'Che cosa fai se ricevi una mail così?',testo:st.q1,parole:parole(st.q1)},{area:'mia',tema:'mittente',q:'Come controlli il mittente?',testo:st.q2,parole:parole(st.q2)}]}}
window.costruisci=costruisci;
function mostra(R){var h='<div class="ris'+(R.punteggio>=6?'':' ko')+'"><b style="font-size:1.3em">Hai indovinato '+R.punteggio+' mail su 8</b><br>'+(R.punteggio>=7?'Bravissimo: occhio da esperto.':R.punteggio>=5?'Bene! Guarda qui sotto i casi sbagliati: è così che si impara.':'Capita: i truffatori sono bravi. Rileggi le spiegazioni, la prossima volta andrà meglio.')+'</div>';
 R.crocette.forEach(function(c,i){var m=M[i],sc=c.indizi_scelti.split(''),gi=m.ind.split(''),buoni=sc.filter(function(x){return gi.indexOf(x)>=0}),mancati=gi.filter(function(x){return sc.indexOf(x)<0}),extra=sc.filter(function(x){return gi.indexOf(x)<0});
  h+='<div class="ris'+(c.ok?'':' ko')+'"><b>Mail '+m.n+': '+(c.ok?'giusto':'sbagliato')+'</b> · era <b>'+(m.ok?'sicura':'phishing')+'</b> (tu: '+esc(c.data)+')<br>'+esc(m.sp)+
   '<br><span class="mu">Indizi che hai trovato giusti: '+buoni.length+' su '+gi.length+(mancati.length?' · ti sono sfuggiti: '+mancati.map(function(x){return esc(IND[x])}).join('; '):'')+(extra.length?' · non c\\'erano: '+extra.map(function(x){return esc(IND[x])}).join('; '):'')+'</span></div>'});
 $('ris').innerHTML=h}
function blocca(){document.querySelectorAll('input,textarea').forEach(function(x){x.disabled=true});$('manda').disabled=true}
if(ST.fatto){blocca();$('msg').className='msg ok';$('msg').textContent='Consegnato alle '+ST.fatto.ora+'.';mostra(ST.fatto.R)}
$('manda').onclick=async function(){conta();if($('manda').disabled)return;var R=costruisci(ST);
 if(!CONF.attivo||!CONF.invio){$('msg').className='msg ko';$('msg').textContent='ANTEPRIMA: invio spento. Il risultato si vede lo stesso qui sotto.';mostra(R);return}
 $('manda').disabled=true;$('msg').className='msg';$('msg').textContent='Sto mandando…';
 try{await posta(R);postaForm(R);ST.fatto={ora:new Date().toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'}),R:R};salva();blocca();$('msg').className='msg ok';$('msg').textContent='Mandato! Si è aperta una scheda con scritto «Consegna arrivata al prof». Ecco il tuo risultato.';mostra(R)}
 catch(x){$('msg').className='msg ko';$('msg').textContent='Non è partito. Premi di nuovo «Consegna al prof».';$('manda').disabled=false}};
disegna();
</script></body></html>"""
scrivi('analizza.html', anal)

# ---------------- PROIETTA (per il docente: mail sullo schermo grande, SENZA risposte) ----------------
pro = _H(HEAD.replace('main{max-width:820px', 'main{max-width:1100px')) % 'Mail sullo schermo' + """
<p class="mu"><a href="./">&larr; Torna alla pagina di oggi</a> · Frecce destra e sinistra per cambiare mail · premi <b>F</b> per lo schermo intero</p>
<div style="display:flex;gap:8px;align-items:center;justify-content:space-between"><button class="bt b" id="pr" style="width:auto;padding:8px 18px">&larr; Prima</button><h1 id="tit" style="margin:0">Mail 1 di 8</h1><button class="bt b" id="su" style="width:auto;padding:8px 18px">Dopo &rarr;</button></div>
<img id="im" class="mailimg" alt="Mail" src="mail/mail-1.png" style="margin-top:10px">
<p class="mu">Domande per la classe: chi scrive? Che dominio ha? Mette fretta? Dove porta il bottone? Sicura o phishing?</p>
<script>var N=1;function vai(n){N=Math.max(1,Math.min(8,n));document.getElementById('im').src='mail/mail-'+N+'.png';document.getElementById('im').alt='Mail '+N;document.getElementById('tit').textContent='Mail '+N+' di 8';try{history.replaceState(null,'','#'+N)}catch(x){}}
document.getElementById('pr').onclick=function(){vai(N-1)};document.getElementById('su').onclick=function(){vai(N+1)};
document.addEventListener('keydown',function(e){if(e.key==='ArrowRight')vai(N+1);if(e.key==='ArrowLeft')vai(N-1);if(e.key==='f'||e.key==='F'){if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen()}});
if(/^#[1-8]$/.test(location.hash))vai(+location.hash.slice(1));</script></main></body></html>"""
scrivi('proietta.html', pro)

# ---------------- EXTRA: il mio budget ----------------
ext = HEAD % 'Extra: il mio budget' + """
<p class="mu"><a href="./">&larr; Torna alla pagina di oggi</a></p>
<h1>PASSO 4 · Extra: il mio budget in Fogli</h1>
<p>Solo se hai finito i passi 1, 2 e 3. Costruisci un foglio di calcolo con le <b>tue spese inventate</b> del mese (non scrivere i soldi veri di casa tua). Alla fine il foglio ti dice da solo se spendi troppo.</p>
""" + F5 + """
<section class="card vinci"><h2>Vinci subito: la somma (5 minuti)</h2>
<ol class="pp">
<li>Su Classroom apri il compito <b>«Il mio budget»</b> e clicca <b>Crea</b>, poi <b>Fogli</b>. Dai al foglio il nome: <b>Il mio budget - Cognome Nome</b>.</li>
<li>Nella cella <b>A1</b> scrivi <b>Spesa</b> e nella cella <b>B1</b> scrivi <b>Euro</b>.</li>
<li>Da <b>A2</b> a <b>A6</b> scrivi 5 spese <b>tue</b> (per esempio: snack, ricarica del telefono, cinema, musica, un regalo).</li>
<li>Da <b>B2</b> a <b>B6</b> scrivi quanto costa ognuna (numeri inventati, per esempio 3, 10, 8, 5, 12).</li>
<li>Nella cella <b>A7</b> scrivi <b>Totale</b>. Nella cella <b>B7</b> scrivi questa formula e premi Invio:<br><code>=SOMMA(B2:B6)</code></li>
</ol><p class="fatto">FATTO! Il foglio ha fatto la somma da solo.</p></section>

<section class="card"><h2>Passo 2: media, spesa più alta e più bassa</h2>
<ol class="pp">
<li>In <b>A8</b> scrivi <b>Media</b>. In <b>B8</b> scrivi: <code>=MEDIA(B2:B6)</code></li>
<li>In <b>A9</b> scrivi <b>Spesa più alta</b>. In <b>B9</b> scrivi: <code>=MAX(B2:B6)</code></li>
<li>In <b>A10</b> scrivi <b>Spesa più bassa</b>. In <b>B10</b> scrivi: <code>=MIN(B2:B6)</code></li>
<li>Cambia un numero in B2:B6 e guarda: tutto si aggiorna da solo.</li>
</ol><p class="fatto">FATTO! Sai usare SOMMA, MEDIA, MAX e MIN.</p></section>

<section class="card"><h2>Passo 3: quanto mi avanza</h2>
<ol class="pp">
<li>In <b>A12</b> scrivi <b>Budget del mese</b>. In <b>B12</b> scrivi un numero inventato, per esempio 40.</li>
<li>In <b>A13</b> scrivi <b>Mi avanza</b>. In <b>B13</b> scrivi: <code>=B12-B7</code></li>
</ol><p class="fatto">FATTO! Se spendi più del budget il numero diventa negativo.</p></section>

<section class="card"><h2>Passo 4: il semaforo (formattazione condizionale)</h2>
<ol class="pp">
<li>Clicca la cella <b>B13</b>.</li>
<li>In alto clicca il menu <b>Formato</b>, poi <b>Formattazione condizionale</b>.</li>
<li>Nella finestra a destra, sotto «Formatta le celle se…», scegli <b>È minore di</b> e scrivi <b>0</b>.</li>
<li>Sotto «Stile di formattazione» scegli lo sfondo <b>rosso</b>. Clicca <b>Fine</b>.</li>
<li>Cambia il budget in B12 con un numero piccolo (per esempio 10): la cella B13 diventa rossa da sola.</li>
</ol><p class="fatto">FATTO! Il tuo foglio ora «ragiona»: avvisa da solo.</p></section>

<section class="card"><h2>Bonus: un grafico a torta</h2>
<ol class="pp"><li>Seleziona le celle da <b>A1</b> a <b>B6</b> con il mouse.</li><li>In alto clicca <b>Inserisci</b>, poi <b>Grafico</b>.</li><li>Nella finestra a destra scegli il tipo <b>Grafico a torta</b>.</li></ol></section>

<section class="card"><h2>Con parole mie e consegna</h2>
<ol class="pp"><li>Sotto la tabella, in <b>A16</b>, scrivi una frase con parole tue: che cosa fanno SOMMA e MEDIA?</li>
<li>In <b>A17</b> scrivi una frase: che cosa fa il rosso nella cella B13?</li>
<li>Su Classroom premi <b>Consegna</b>.</li></ol>
<p class="fatto">FATTO! Hai un foglio di calcolo tuo, mostralo al compagno.</p></section>
""" + F5 + "</main>" + ASS + "</body></html>"
scrivi('extra.html', ext)
json.dump({"invio": INVIO, "attivo": True, "_nota": "2INF 02/11/2026. Anteprima: nessuna pagina è collegata da Classroom o dal sito finché il prof non dice «pubblica». Piano A: le pagine mandano le consegne allo script (dati/verifiche/2inf-*)."},
          open(OUT + 'config.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('pagine ok')
