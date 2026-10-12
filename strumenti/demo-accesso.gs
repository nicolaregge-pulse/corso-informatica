/**
 * DEMO CON ACCESSO VIA EMAIL — v1.0 (12/10/2026) — account PERSONALE di Nicola Regge.
 * Chi apre il link della demo scrive la sua email, riceve un codice di 6 cifre (vale 15 minuti) e, scritto il codice,
 * entra nella demo per 24 ore. Ogni richiesta, ogni accesso e ogni pagina aperta finiscono nel Foglio «Demo — accessi»
 * e ti arriva una email di notifica.
 * Una volta sola: 1) Esegui «setup». 2) Esegui il deployment come «App web»: esegui come «Me», accesso «Chiunque».
 * Nessun segreto qui dentro: la chiave per firmare gli accessi la crea «setup» nelle proprietà dello script.
 */
var DEMO_URL = 'https://nicolaregge-pulse.github.io/corso-informatica/demo/';
var DURATA_ORE = 24;

function setup() {
  var p = PropertiesService.getScriptProperties();
  if (!p.getProperty('SEGRETO')) p.setProperty('SEGRETO', Utilities.getUuid() + Utilities.getUuid());
  if (!p.getProperty('FOGLIO')) {
    var ss = SpreadsheetApp.create('Demo — accessi');
    ss.getSheets()[0].setName('Registro').appendRow(['Data e ora', 'Email', 'Evento', 'Dettaglio']);
    p.setProperty('FOGLIO', ss.getId());
  }
  MailApp.getRemainingDailyQuota();
  Logger.log('Pronto. Foglio degli accessi: ' + SpreadsheetApp.openById(p.getProperty('FOGLIO')).getUrl());
}

function registra_(email, evento, dettaglio, notifica) {
  var p = PropertiesService.getScriptProperties();
  SpreadsheetApp.openById(p.getProperty('FOGLIO')).getSheetByName('Registro').appendRow([new Date(), email, evento, dettaglio || '']);
  if (notifica) {
    MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'Demo: ' + evento + ' — ' + email,
      'Chi: ' + email + '\nCosa: ' + evento + '\nDettaglio: ' + (dettaglio || '-') + '\nQuando: ' + new Date());
  }
}

function firma_(s) {
  return Utilities.base64EncodeWebSafe(Utilities.computeHmacSha256Signature(s, PropertiesService.getScriptProperties().getProperty('SEGRETO')));
}
function token_(email) {
  var s = email + '|' + (Date.now() + DURATA_ORE * 3600 * 1000);
  return Utilities.base64EncodeWebSafe(s) + '.' + firma_(s);
}
function leggiToken_(t) {
  try {
    var a = String(t || '').split('.');
    var s = Utilities.newBlob(Utilities.base64DecodeWebSafe(a[0])).getDataAsString();
    if (firma_(s) !== a[1]) return null;
    var x = s.split('|');
    if (Number(x[1]) < Date.now()) return null;
    return { email: x[0], scade: Number(x[1]) };
  } catch (e) { return null; }
}

function doGet(e) {
  var q = (e && e.parameter) || {};
  if (q.azione === 'traccia') {   // chiamata dalle pagine della demo (JSONP)
    var t = leggiToken_(q.t), out = { ok: !!t, scade: t ? t.scade : 0 };
    if (t) registra_(t.email, q.evento === 'apertura' ? 'pagina aperta' : 'attività', (q.pagina || '') + ' ' + (q.dettaglio || ''), q.evento === 'apertura');
    var cb = /^[A-Za-z_][A-Za-z0-9_]*$/.test(q.callback || '') ? q.callback : 'cb';
    return ContentService.createTextOutput(cb + '(' + JSON.stringify(out) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return HtmlService.createHtmlOutput(PAGINA_).setTitle('Demo — accesso').addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

function richiediCodice(email) {
  email = String(email || '').trim().toLowerCase();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return 'Email non valida.';
  var c = CacheService.getScriptCache(), n = Number(c.get('n_' + email) || 0);
  if (n >= 5) return 'Troppe richieste: riprova fra un\'ora.';
  var codice = String(Math.floor(100000 + Math.random() * 900000));
  c.put('cod_' + email, codice, 900);
  c.put('n_' + email, String(n + 1), 3600);
  MailApp.sendEmail(email, 'Il tuo codice per la demo',
    'Il tuo codice è: ' + codice + '\n\nVale 15 minuti. Dopo l\'accesso la demo resta aperta per ' + DURATA_ORE + ' ore.\n\nSe non hai chiesto tu il codice, ignora questa email.');
  registra_(email, 'richiesta codice', '', true);
  return 'ok';
}

function verificaCodice(email, codice) {
  email = String(email || '').trim().toLowerCase();
  var c = CacheService.getScriptCache();
  if (!codice || c.get('cod_' + email) !== String(codice).trim()) { registra_(email, 'codice sbagliato', '', false); return { ok: false }; }
  c.remove('cod_' + email);
  registra_(email, 'accesso', 'valido ' + DURATA_ORE + ' ore', true);
  return { ok: true, link: DEMO_URL + '?t=' + encodeURIComponent(token_(email)) };
}

var PAGINA_ = '<!doctype html><html lang="it"><head><meta charset="utf-8"><style>' +
  'body{margin:0;background:#fbfaf7;color:#111;font:17px/1.5 system-ui,Segoe UI,Arial,sans-serif}.w{max-width:520px;margin:0 auto;padding:24px 16px}' +
  'h1{font-size:26px;margin:0 0 6px}.box{background:#fff;border:2px solid #1f6feb;border-radius:14px;padding:18px}' +
  'input{font:inherit;width:100%;box-sizing:border-box;padding:12px;border:1px solid #bbb;border-radius:10px;margin:8px 0}' +
  'button,a.bt{display:inline-block;font:inherit;font-weight:800;background:#1f6feb;color:#fff;border:0;border-radius:10px;padding:12px 20px;text-decoration:none;cursor:pointer}' +
  '.mu{color:#555;font-size:14px}#msg{color:#c0392b;min-height:1.4em}</style></head><body><div class="w">' +
  '<h1>Una scuola che lavora come un\'azienda di software</h1><p class="mu">Demo del sistema di laboratorio del prof. Nicola Regge: compito unico, Pull Request, backlog, versioni del gioco, voti e classifica che si aggiornano da soli.</p>' +
  '<div class="box" id="passo1"><p><b>1.</b> Scrivi la tua email: ti mandiamo un codice di 6 cifre.</p><input id="email" type="email" autocomplete="email" placeholder="nome@esempio.it"><button id="b1">Mandami il codice</button></div>' +
  '<div class="box" id="passo2" style="display:none"><p><b>2.</b> Scrivi il codice che hai ricevuto per email.</p><input id="codice" inputmode="numeric" maxlength="6" placeholder="6 cifre"><button id="b2">Entra nella demo</button></div>' +
  '<div class="box" id="passo3" style="display:none"><p><b>Fatto.</b> La demo resta aperta per 24 ore.</p><a class="bt" id="vai" target="_top" href="#">Apri la demo</a></div>' +
  '<p id="msg"></p><p class="mu">Informativa: usiamo la tua email solo per mandarti il codice e per sapere chi ha visto la demo e quali pagine ha aperto. Titolare: Nicola Regge. Per farla cancellare, rispondi all\'email del codice.</p>' +
  '</div><script>' +
  'function $(i){return document.getElementById(i)}' +
  '$("b1").onclick=function(){$("msg").textContent="Invio in corso…";google.script.run.withSuccessHandler(function(r){if(r==="ok"){$("passo1").style.display="none";$("passo2").style.display="block";$("msg").textContent="Codice mandato: guarda la tua email."}else $("msg").textContent=r}).richiediCodice($("email").value)};' +
  '$("b2").onclick=function(){google.script.run.withSuccessHandler(function(r){if(r.ok){$("passo2").style.display="none";$("passo3").style.display="block";$("vai").href=r.link;$("msg").textContent=""}else $("msg").textContent="Codice sbagliato o scaduto."}).verificaCodice($("email").value,$("codice").value)};' +
  '</script></body></html>';
