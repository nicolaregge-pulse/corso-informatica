// Prova locale del motore v2.23-siti (sezione nuova: passo 'siti' = controllo dei siti dalla rete di Google). NOMI INVENTATI. Servizi Google FINTI:
// prova la LOGICA del codice (lettura scheda, HEAD poi GET, limiti di tempo, coda, Stato), NON le risposte vere di github.io ne i permessi veri di Apps Script (non provato).
// Modello: prova_motore_v2_22_3.js. Uso: node fabbrica/correzioni/prova_motore_v2_23_siti.js   (dalla radice del repository pubblico)
var fs = require('fs'), vm = require('vm'), path = require('path');
var D = Date, off = new D('2026-11-16T13:00:00Z').getTime() - D.now();     // orologio finto: 16/11/2026 14:00 a Roma, spostabile con avanza()
function FD(a, b, c, d, e, f, g) { if (!(this instanceof FD)) return new D(D.now() + off).toString(); if (arguments.length === 0) return new D(D.now() + off); if (arguments.length === 1) return new D(a); return new D(a, b, c || 1, d || 0, e || 0, f || 0, g || 0); }
FD.now = function () { return D.now() + off; }; FD.UTC = D.UTC; FD.parse = D.parse; FD.prototype = D.prototype;
global.Date = FD;
function avanza(ms) { off += ms; }
var fail = [], ok = 0;
function check(c, m) { if (c) ok++; else fail.push(m); }

/* ---- foglio finto (come nella prova 2.22.3) ---- */
function Sheet(nome, id) {
  var cells = {}, self = this;
  this.name = nome;
  function rng(r, c, nr, nc) {
    nr = nr || 1; nc = nc || 1;
    var o = {
      setValues: function (v) { for (var i = 0; i < v.length; i++) for (var j = 0; j < v[i].length; j++) cells[(r + i) + ',' + (c + j)] = v[i][j]; return o; },
      getValue: function () { var x = cells[r + ',' + c]; return x === undefined ? '' : x; },
      setValue: function (x) { cells[r + ',' + c] = x; return o; },
      getValues: function () { var out = []; for (var i = 0; i < nr; i++) { var row = []; for (var j = 0; j < nc; j++) { var x = cells[(r + i) + ',' + (c + j)]; row.push(x === undefined ? '' : x); } out.push(row); } return out; }
    };
    ['setNumberFormat', 'setFontWeight', 'setBackground', 'setWrap', 'setFontStyle', 'setFontColor'].forEach(function (m) { o[m] = function () { return o; }; });
    return o;
  }
  this.getRange = rng;
  this.getDataRange = function () { var mr = 0, mc = 0; Object.keys(cells).forEach(function (k) { var p = k.split(','); mr = Math.max(mr, +p[0]); mc = Math.max(mc, +p[1]); }); return rng(1, 1, mr, mc); };
  this.clear = function () { cells = {}; };
  this.setFrozenRows = this.setFrozenColumns = this.setTabColor = function () { };
  this.getName = function () { return nome; };
  this.getSheetId = function () { return id; };
  this.isSheetHidden = function () { return false; };
  this.rows = function () { return self.getDataRange().getValues(); };
}
function Foglio() {
  var sh = {}, n = 1, ordine = [];
  this.getSheetByName = function (x) { return sh[x] || null; };
  this.insertSheet = function (x) { sh[x] = new Sheet(x, n++); ordine.push(x); return sh[x]; };
  this.getSheets = function () { return ordine.map(function (k) { return sh[k]; }); };
  this.getId = function () { return 'FOGLIO'; };
}
function pad(x) { return ('0' + x).slice(-2); }
var Utilities = { formatDate: function (d, tz, f) {
  var t = new Date(d.getTime() + 3600000);
  return f.replace('yyyy', t.getUTCFullYear()).replace('dd', pad(t.getUTCDate())).replace('MM', pad(t.getUTCMonth() + 1)).replace('HH', pad(t.getUTCHours())).replace('mm', pad(t.getUTCMinutes())).replace('ss', pad(t.getUTCSeconds()));
} };
var props = {};
var PropertiesService = { getScriptProperties: function () { return { getProperty: function (k) { return props[k] || null; }, setProperty: function (k, v) { props[k] = v; } }; } };

/* ---- rete finta: pagine, immagini, errori ---- */
var log = [];
function resp(code, body) { return { getResponseCode: function () { return code; }, getContentText: function () { return body || ''; } }; }
var PAG = {
  'https://ok.github.io/mio-sito/': [200, '<!DOCTYPE html><html><head><title>  Chi   sono &amp; cosa faccio </title></head><body>' +
    '<img src="foto1.jpg"><img src=\'./foto2.jpg\' alt="x"><IMG SRC="/mio-sito/foto3.jpg"><img src="https://ext.example/x.png"><img src="data:image/png;base64,AAAA"><img src="foto 4.jpg"><img src="foto1.jpg"><img src="sub/../foto5.jpg"></body></html>'],
  'https://rotte.github.io/mio-sito/': [200, '<html><head><title>Rotte</title></head><body><img src="a.jpg"><img src="b.jpg"><img src="c.jpg"><img></body></html>'],
  'https://nopages.github.io/mio-sito/': [404, '<h1>404</h1>'],
  'https://notitle.github.io/x/': [200, '<html><body><p>niente titolo</p></body></html>'],
  'https://doc.github.io/mio-sito/': [200, '<html><head><title>Dal Documento</title></head><body></body></html>'],
  'https://atteso.github.io/mio-sito/': [404, ''],
  'https://deriv.github.io/mio-sito/': [200, '<html><head><title>Derivato</title></head><body><img src="a.png"></body></html>']
};
var IMG = {   // url -> {head, get}
  'https://ok.github.io/mio-sito/foto1.jpg': { head: 200, get: 200 }, 'https://ok.github.io/mio-sito/foto2.jpg': { head: 200, get: 200 }, 'https://ok.github.io/mio-sito/foto3.jpg': { head: 200, get: 200 },
  'https://ext.example/x.png': { head: 200, get: 200 }, 'https://ok.github.io/mio-sito/foto%204.jpg': { head: 200, get: 200 }, 'https://ok.github.io/mio-sito/foto5.jpg': { head: 200, get: 200 },
  'https://rotte.github.io/mio-sito/a.jpg': { head: 405, get: 200 },     // HEAD non permesso, GET si: deve risultare OK con metodo GET
  'https://rotte.github.io/mio-sito/b.jpg': { head: 404, get: 404 },     // rotta
  'https://rotte.github.io/mio-sito/c.jpg': { head: 200, get: 200 },
  'https://deriv.github.io/mio-sito/a.png': { head: 200, get: 200 }
};
function una(r) {
  log.push({ url: r.url, method: (r.method || 'get').toLowerCase() });
  if (/invalido/.test(r.url)) throw new Error('Indirizzo non valido: ' + r.url);
  if (/giu\.github\.io/.test(r.url)) throw new Error('DNS error: giu.github.io');
  var m = (r.method || 'get').toLowerCase();
  if (PAG[r.url]) return resp(PAG[r.url][0], PAG[r.url][1]);
  if (IMG[r.url]) return resp(IMG[r.url][m === 'head' ? 'head' : 'get'], '');
  return resp(404, '');
}
var UrlFetchApp = {
  fetch: function (u, opt) { if (typeof u === 'object') return una(u); return una(Object.assign({ url: u }, opt || {})); },
  fetchAll: function (reqs) { return reqs.map(una); }
};
var ctx = { Utilities: Utilities, PropertiesService: PropertiesService, UrlFetchApp: UrlFetchApp, Logger: { log: function () { } }, console: console, Date: Date, JSON: JSON, Math: Math, RegExp: RegExp, Object: Object, Array: Array, String: String, Number: Number, Error: Error, parseInt: parseInt, isNaN: isNaN };
vm.createContext(ctx);
var src = fs.readFileSync(path.join(__dirname, 'motore-v2.23-siti.js'), 'utf8');
vm.runInContext(src, ctx);
function ru(code) { return vm.runInContext(code, ctx); }
function nFetch(metodo) { return log.filter(function (x) { return !metodo || x.method === metodo; }).length; }
function riga(sh, cognome) { return sh.rows().filter(function (r) { return r[0] === cognome; })[0]; }

/* ---------- S1 unita ---------- */
check(ru("SITI_base_('https://a.github.io/mio-sito')") === 'https://a.github.io/mio-sito/', 'S1 base senza barra');
check(ru("SITI_base_('https://a.github.io/mio-sito/pagina.html?x=1#y')") === 'https://a.github.io/mio-sito/', 'S1 base con pagina');
check(ru("SITI_base_('https://a.github.io')") === 'https://a.github.io/', 'S1 base dominio');
var B = 'https://u.github.io/mio-sito/';
check(ru("SITI_assoluto_('foto.jpg', '" + B + "')") === B + 'foto.jpg', 'S1 relativo');
check(ru("SITI_assoluto_('./img/a.png', '" + B + "')") === B + 'img/a.png', 'S1 ./');
check(ru("SITI_assoluto_('../x.png', '" + B + "sub/')") === B + 'x.png', 'S1 ..');
check(ru("SITI_assoluto_('/foto.jpg', '" + B + "')") === 'https://u.github.io/foto.jpg', 'S1 radice: nei siti di progetto punta FUORI dal repository (e il bug tipico)');
check(ru("SITI_assoluto_('//cdn.x.it/a.png', '" + B + "')") === 'https://cdn.x.it/a.png', 'S1 //host');
check(ru("SITI_assoluto_('a b.png?v=1#z', '" + B + "')") === B + 'a%20b.png?v=1', 'S1 spazio, query, ancora');
check(ru("SITI_assoluto_('data:image/png;base64,AA', '" + B + "')") === 'data:' && ru("SITI_assoluto_('', '" + B + "')") === null, 'S1 data e vuoto');
check(ru("SITI_titolo_('<TITLE>\\n  Ciao &amp;  mondo </TITLE>')") === 'Ciao & mondo' && ru("SITI_titolo_('<p>x</p>')") === '', 'S1 titolo');
var im = ru("SITI_immagini_('<img src=\"a.png\"><img src=a.png><img><img src=\"\"><IMG SRC=\\'b.png\\'>', '" + B + "')");
check(im.n === 5 && im.urls.length === 2 && im.vuote === 2, 'S1 immagini: ' + JSON.stringify(im));
ru("var tanti = ''; for (var q = 0; q < 40; q++) tanti += '<img src=\"i' + q + '.png\">'");
var im2 = ru("SITI_immagini_(tanti, '" + B + "')");
check(im2.n === 40 && im2.urls.length === 30 && im2.oltre === 10, 'S1 limite 30 immagini: ' + JSON.stringify([im2.n, im2.urls.length, im2.oltre]));

/* ---------- S2 passo con scheda in entrata ---------- */
var ss = new Foglio();
ru('FB_NOTE_ = []');
ctx.ss = ss;
var r0 = ru("FB_siti_(ss, Date.now())");
check(r0.totale === 0 && ss.getSheetByName('Siti da controllare') && ss.getSheetByName('Siti da controllare').rows()[0].join('|') === 'COGNOME|URL sito|URL repository|Classe', 'S2 scheda in entrata creata con intestazione');
var st0 = ss.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Siti'; })[0];
check(st0 && /nessun sito da controllare/.test(st0[1]) && /scheda creata ora/.test(st0[1]), 'S2 Stato senza siti: ' + JSON.stringify(st0));
var sin = ss.getSheetByName('Siti da controllare');
sin.getRange(2, 1, 6, 4).setValues([
  ['ROSSI Mario', 'https://ok.github.io/mio-sito/', 'https://github.com/ok/mio-sito', '2INF'],
  ['VERDI Anna', 'https://rotte.github.io/mio-sito/', 'https://github.com/rotte/mio-sito', '2INF'],
  ['NERI Luca', 'https://nopages.github.io/mio-sito/', '', '2INF'],
  ['BIANCHI Sara', 'https://giu.github.io/mio-sito/', '', '2INF'],
  ['GIALLI Ugo', '', 'https://github.com/deriv/mio-sito', '2INF'],
  ['MORI Elia', 'https://notitle.github.io/x/', '', '3INF']]);
log.length = 0;
var r1 = ru("FB_siti_(ss, Date.now())");
check(r1.controllati === 6 && r1.totale === 6, 'S2 controllati 6/6: ' + JSON.stringify(r1));
var S = ss.getSheetByName('Siti');
check(S.rows()[0].join('|') === 'COGNOME|Classe|URL sito|URL repository|Origine|HTTP|Titolo|N. immagini|Immagini OK|Immagini non raggiungibili|Dettaglio immagini|Esito|Controllato alle|Epoca (ms)', 'S2 intestazione Siti: ' + S.rows()[0].join('|'));
var ro = riga(S, 'ROSSI Mario');
check(ro[5] === 200 && ro[6] === 'Chi sono & cosa faccio' && ro[11] === 'OK', 'S2 ROSSI: http/titolo/esito: ' + JSON.stringify(ro));
check(ro[7] === 8 && ro[8] === 7 && ro[9] === '', 'S2 ROSSI: 8 <img> nella pagina, 7 URL unici (foto1 doppia; compresa la data: incorporata), tutte ok: ' + JSON.stringify([ro[7], ro[8], ro[9]]));
check(/200 HEAD foto1\.jpg/.test(ro[10]) && /200 HEAD foto2\.jpg/.test(ro[10]) && /200 HEAD foto3\.jpg/.test(ro[10]) && /200 HEAD foto%204\.jpg/.test(ro[10]) && /200 HEAD foto5\.jpg/.test(ro[10]) && /data/.test(ro[10]) && /200 HEAD x\.png/.test(ro[10]), 'S2 ROSSI: dettaglio per ogni img (URL assoluto risolto, ../ semplificato): ' + ro[10]);
check(/^\d\d\/\d\d\/\d{4} 14:00:\d\d$/.test(ro[12]) && ro[13] > 0, 'S2 ora del controllo (Roma 14:00): ' + ro[12]);
var ve = riga(S, 'VERDI Anna');
check(ve[11] === 'IMMAGINI ROTTE (2)' && /b\.jpg \(404\)/.test(ve[9]) && /src vuoto/.test(ve[9]) && /200 GET a\.jpg/.test(ve[10]) && /404 GET b\.jpg/.test(ve[10]) && /200 HEAD c\.jpg/.test(ve[10]) && ve[8] === 2, 'S2 VERDI: HEAD 405 -> GET 200 (ok), b rotta, src vuoto: ' + JSON.stringify(ve.slice(7, 12)));
var ne = riga(S, 'NERI Luca');
check(ne[5] === 404 && /^PAGINA NON TROVATA \(404\)/.test(ne[11]) && ne[7] === 0, 'S2 NERI 404: ' + JSON.stringify(ne));
var bi = riga(S, 'BIANCHI Sara');
check(bi[5] === 0 && /^NON RAGGIUNGIBILE: DNS error/.test(bi[11]), 'S2 BIANCHI DNS: ' + JSON.stringify(bi));
var gi = riga(S, 'GIALLI Ugo');
check(gi[2] === 'https://deriv.github.io/mio-sito/' && /derivato/.test(gi[4]) && gi[11] === 'OK' && gi[6] === 'Derivato', 'S2 GIALLI: sito derivato dall\'URL del repository: ' + JSON.stringify(gi));
var mo = riga(S, 'MORI Elia');
check(mo[11] === 'SENZA TITOLO' && mo[1] === '3INF', 'S2 MORI senza titolo');
var st1 = ss.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Siti'; });
check(st1.length === 1 && /controllati 6 di 6 · OK 2 · con problemi 4/.test(st1[0][1]) && /alle 14:00:/.test(st1[0][1]) && !/IN CODA/.test(st1[0][1]), 'S2 riga Stato: ' + JSON.stringify(st1));
check(nFetch('head') > 0 && nFetch('get') > 0, 'S2 HEAD e GET usate');
check(!S.rows().some(function (r) { return r[0] === 'ROSSI Mario' && r.length < 14; }), 'S2 14 colonne');

/* ---------- S3 rilettura entro 5 minuti: nessuna richiesta nuova, risultati conservati ---------- */
log.length = 0; avanza(2 * 60000);
var r2 = ru("FB_siti_(ss, Date.now())");
check(nFetch() === 0 && r2.controllati === 0, 'S3 dopo 2 minuti nessun sito riaperto: richieste ' + nFetch());
check(riga(ss.getSheetByName('Siti'), 'ROSSI Mario')[11] === 'OK' && riga(ss.getSheetByName('Siti'), 'VERDI Anna')[11] === 'IMMAGINI ROTTE (2)', 'S3 risultati conservati');
var st2 = ss.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Siti'; })[0][1];
check(/controllati 0 di 6/.test(st2) && /6 controllati meno di 5 minuti fa/.test(st2), 'S3 Stato: ' + st2);
// dopo 6 minuti si riapre: l'allievo ha sistemato l'immagine b.jpg
IMG['https://rotte.github.io/mio-sito/b.jpg'] = { head: 200, get: 200 };
avanza(4 * 60000 + 1000); log.length = 0;
var r3 = ru("FB_siti_(ss, Date.now())");
check(r3.controllati === 6 && riga(ss.getSheetByName('Siti'), 'VERDI Anna')[11] !== 'OK' && /1 src vuoto|src vuoto/.test(riga(ss.getSheetByName('Siti'), 'VERDI Anna')[9]) && !/b\.jpg/.test(riga(ss.getSheetByName('Siti'), 'VERDI Anna')[9]), 'S3 dopo 6 minuti: b.jpg ora raggiungibile (resta solo il src vuoto): ' + JSON.stringify(riga(ss.getSheetByName('Siti'), 'VERDI Anna').slice(8, 12)));

/* ---------- S4 limite di tempo: si smette, i non fatti restano in coda, i vecchi risultati restano ---------- */
avanza(10 * 60000); log.length = 0;
var rr = ru("SITI_passo_(ss, Date.now(), 0, 270000)");     // budget zero: nessun gruppo
check(rr.controllati === 0 && rr.inCoda === 6 && nFetch() === 0, 'S4 budget zero: nessuna richiesta, 6 in coda: ' + JSON.stringify(rr));
var st4 = ss.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Siti'; })[0][1];
check(/IN CODA per il tempo: 6/.test(st4) && /riprendono al giro dopo/.test(st4), 'S4 Stato dice IN CODA: ' + st4);
check(riga(ss.getSheetByName('Siti'), 'ROSSI Mario')[11] === 'OK', 'S4 i risultati vecchi restano visibili');
// 12 siti, 5 per gruppo, budget che basta per un gruppo solo: i piu vecchi per primi
ru("SITI_BATCH_ = 2");
var sin2 = ss.getSheetByName('Siti da controllare');
sin2.getRange(8, 1, 1, 4).setValues([['NUOVO Zeno', 'https://doc.github.io/mio-sito/', '', '2INF']]);
ru("var ORIG_fuori = Date.now");
avanza(10 * 60000); log.length = 0;
// il simulatore del tempo: ogni gruppo costa 50 s di orologio finto -> con budget 60 s ne passano 2 (il controllo e prima di ogni gruppo)
var orig = ctx.UrlFetchApp.fetchAll;
ctx.UrlFetchApp.fetchAll = function (reqs) { if (reqs[0].method === 'get' && /github\.io\/[^ ]*\/$/.test(reqs[0].url)) avanza(50000); return orig(reqs); };
var r5 = ru("SITI_passo_(ss, Date.now(), 60000, 270000)");
check(r5.controllati === 4 && r5.inCoda === 3, 'S4 budget 60 s con gruppi da 2 e 50 s ciascuno: 2 gruppi, 4 siti, 3 in coda: ' + JSON.stringify(r5));
ctx.UrlFetchApp.fetchAll = orig;
ru("SITI_BATCH_ = 10");
// limite totale del giro (270 s) gia superato: nessun sito
avanza(10 * 60000); log.length = 0;
var r6 = ru("SITI_passo_(ss, Date.now() - 300000, 60000, 270000)");
check(r6.controllati === 0 && nFetch() === 0, 'S4 limite del giro superato: nessun sito aperto');

/* ---------- S5 completamenti automatici: dal Documento e dall'indirizzo atteso; la scheda a mano ha la precedenza ---------- */
var ss2 = new Foglio();
ctx.ss2 = ss2;
var doc = ss2.insertSheet('Documenti 2INF');
doc.getRange(1, 1, 6, 16).setValues([['2INF · Documenti · dati letti il 16/11/2026 12:41:43'], [''], [''],
  ['Allievo', 'Email', 'Compito', 'Id', 'Stato', 'Ora', 'File', 'File ID', 'Link', 'Tipo', 'Mod', 'Imm', 'Mod', 'Agg', 'Caratteri', 'Estratto del testo'],
  ['ROSSI Mario', 'm@x', 'Ora 4', '1', 'CONSEGNATO', '', '', '', '', '', '', '', '', '', '', 'Nome: Mario URL del repository: https://github.com/ok/mio-sito URL del sito: https://ok.github.io/mio-sito/ (Al posto'],
  ['DOCU Dario', 'd@x', 'Ora 4', '1', 'CONSEGNATO', '', '', '', '', '', '', '', '', '', '', 'URL del repository: https://github.com/doc/mio-sito (niente sito)']]);
var dp = ss2.insertSheet('Documenti pubblica 2INF');
dp.getRange(1, 1, 4, 16).setValues([[''], [''], [''], ['Allievo', 'x', 'x', 'x', 'x', 'x', 'Estratto del testo'], ['Dario D.', '', '', '', '', '', 'https://github.com/pubblico/non-deve-comparire']]);
var ut = ss2.insertSheet('Utenti 2INF');
ut.getRange(1, 1, 4, 3).setValues([['PC', 'Utente GitHub', 'Allievo'], [11, 'atteso', 'ATTESI Anna'], [12, 'ok', 'ROSSI Mario'], [13, '-', 'SENZA Utente']]);
var sin3 = ss2.insertSheet('Siti da controllare');
sin3.getRange(1, 1, 2, 4).setValues([['COGNOME', 'URL sito', 'URL repository', 'Classe'], ['rossi mario', 'https://rotte.github.io/mio-sito/', '', '2INF']]);
log.length = 0;
var r7 = ru("SITI_passo_(ss2, Date.now(), 60000, 270000)");
var S2 = ss2.getSheetByName('Siti').rows().slice(1);
check(r7.totale === 3 && S2.length === 3, 'S5 totale 3 (1 a mano + Documento DOCU + atteso ATTESI; ROSSI non duplicato, SENZA senza utente, scheda pubblica ignorata): ' + JSON.stringify(S2.map(function (r) { return r[0]; })));
check(riga(ss2.getSheetByName('Siti'), 'rossi mario')[2] === 'https://rotte.github.io/mio-sito/' && riga(ss2.getSheetByName('Siti'), 'rossi mario')[4] === 'scheda', 'S5 la scheda a mano vince');
var dd = riga(ss2.getSheetByName('Siti'), 'DOCU Dario');
check(dd && dd[2] === 'https://doc.github.io/mio-sito/' && /scritto nel Documento \(Documenti 2INF\)/.test(dd[4]) && dd[11] === 'OK', 'S5 DOCU: sito derivato dal repository scritto nel Documento: ' + JSON.stringify(dd));
var at = riga(ss2.getSheetByName('Siti'), 'ATTESI Anna');
check(at && at[2] === 'https://atteso.github.io/mio-sito/' && /^ATTESO \(utente da Utenti 2INF/.test(at[4]) && /404/.test(at[11]), 'S5 ATTESI: indirizzo atteso, origine dichiarata, 404: ' + JSON.stringify(at));
check(!ss2.getSheetByName('Siti').rows().some(function (r) { return /pubblico/.test(r.join('')); }), 'S5 nessun dato dalla scheda pubblica');
check(/di cui 2 completati da soli/.test(ss2.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Siti'; })[0][1]), 'S5 Stato conta i completamenti automatici');

/* ---------- S6 un indirizzo non valido non ferma il gruppo ---------- */
var ss3 = new Foglio(); ctx.ss3 = ss3;
var s3 = ss3.insertSheet('Siti da controllare');
s3.getRange(1, 1, 3, 4).setValues([['COGNOME', 'URL sito', 'URL repository', 'Classe'], ['UNO Primo', 'https://ok.github.io/mio-sito/', '', '2INF'], ['DUE Secondo', 'https://invalido.github.io/x/', '', '2INF']]);
ru("SITI_AUTO_ATTESO_ = false; SITI_AUTO_DOCUMENTI_ = false");
var r8 = ru("SITI_passo_(ss3, Date.now(), 60000, 270000)");
var S3 = ss3.getSheetByName('Siti');
check(r8.controllati === 2 && riga(S3, 'UNO Primo')[11] === 'OK' && /^NON RAGGIUNGIBILE: Indirizzo non valido/.test(riga(S3, 'DUE Secondo')[11]), 'S6 indirizzo non valido: gli altri si controllano lo stesso: ' + JSON.stringify([riga(S3, 'UNO Primo')[11], riga(S3, 'DUE Secondo')[11]]));
ru("SITI_AUTO_ATTESO_ = true; SITI_AUTO_DOCUMENTI_ = true");

/* ---------- S7 integrazione nel giro del motore ---------- */
check(/passo\('siti', function \(\) \{ FB_siti_\(ss, t0\); \}\);/.test(src) && src.indexOf("passo('ripara'") < src.indexOf("passo('siti', function") && src.indexOf("passo('siti', function") < src.indexOf("passo('risultati'"), 'S7 passo siti dopo ripara e prima di risultati');
check((src.match(/\['Motore', '2\.23-siti'\]/g) || []).length === 2 && !/\['Motore', '2\.22\.3'\]/.test(src), 'S7 versione 2.23-siti in Stato (2 punti)');
check(/^\/\*\*\n \* FABBRICA - MOTORE v2\.23-siti/.test(src) && /Changelog: 2\.23-siti/.test(src.split('\n').slice(0, 8).join('\n')), 'S7 intestazione e changelog');
ctx.SpreadsheetApp = { openById: function () { return ss4; } };
ctx.LockService = { getScriptLock: function () { return { tryLock: function () { return true; }, releaseLock: function () { } }; } };
var ss4 = new Foglio(); ctx.ss4 = ss4;
ss4.insertSheet('Esiti'); ss4.insertSheet('Stato');
var s4 = ss4.insertSheet('Siti da controllare');
s4.getRange(1, 1, 2, 4).setValues([['COGNOME', 'URL sito', 'URL repository', 'Classe'], ['UNO Primo', 'https://ok.github.io/mio-sito/', '', '2INF']]);
ru("FB_p_().setProperty('FB_FOGLIO', 'X')");
ctx.ClassroomFinto = 1;
ru("FB_main_()");
var g = ss4.getSheetByName('Stato').rows();
check(g.some(function (r) { return r[0] === 'Motore' && r[1] === '2.23-siti'; }), 'S7 Stato: Motore 2.23-siti');
check(g.some(function (r) { return r[0] === 'Siti' && /controllati 1 di 1 · OK 1/.test(r[1]); }), 'S7 giro del motore: riga Siti in Stato: ' + JSON.stringify(g.filter(function (r) { return r[0] === 'Siti'; })));
check(g.some(function (r) { return r[0] === 'Giro' && /durata/.test(r[1]); }), 'S7 riga Giro presente');
// con il limite del giro gia superato il passo 'siti' e saltato e dichiarato come gli altri
ru("FB_MAX_GIRO_ = -1; FB_main_()");
var g2 = ss4.getSheetByName('Stato').rows().filter(function (r) { return r[0] === 'Giro'; })[0][1];
check(/SALTATI per il tempo: .*siti/.test(g2), 'S7 limite superato: siti saltato e dichiarato: ' + g2);
ru("FB_MAX_GIRO_ = 270000");

console.log('Controlli riusciti: ' + ok + ', falliti: ' + fail.length);
if (fail.length) { console.log('PROVA FALLITA:\n- ' + fail.join('\n- ')); process.exit(1); }
console.log('PROVA OK (passo siti: lettura scheda, HEAD poi GET, titolo, immagini, esiti, Stato, coda per il tempo, rilettura dopo 5 minuti, completamenti da Documenti e Utenti, giro del motore; con servizi FINTI: github.io vero e permessi di Apps Script non provati)');
