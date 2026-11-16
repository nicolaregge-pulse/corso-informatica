/**
 * CONTROLLA SITI LIVE v1.0 (16/11/2026) - Google Apps Script. Nessun nome di allievo in questo file (R1): i nomi stanno solo nel foglio del docente.
 *
 * A che cosa serve: dal sandbox di Claude github.io NON si raggiunge (proxy). La rete di Google si': questa funzione apre i siti dei
 * ragazzi dalla rete di Google e scrive il risultato in una scheda del foglio Fabbrica (account PIAMARTA).
 *
 * SCHEDA IN ENTRATA 'Siti da controllare' (una riga per allievo; intestazione: COGNOME | URL sito | URL repository | Classe (facoltativa)).
 *   Si compila a mano (incolla il CSV di strumenti/prepara_siti_da_controllare.py nel riservato) e, in piu, si completa da sola con
 *   l'ultimo URL che l'allievo ha scritto nel Documento (schede 'Documenti <CLASSE>') e, in mancanza, con l'indirizzo atteso
 *   https://<utente>.github.io/<SITI_REPO_ATTESO_>/ dalle schede 'Utenti <CLASSE>' (colonna Origine lo dice: mai confusa con quello scritto).
 * SCHEDA IN USCITA 'Siti' (solo docente, con COGNOME: MAI da pubblicare): COGNOME, Classe, URL sito, URL repository, Origine, HTTP, Titolo,
 *   N. immagini, Immagini OK, Immagini non raggiungibili, Dettaglio immagini (per ogni <img>: codice HTTP, HEAD o GET, nome file),
 *   Esito, Controllato alle, Epoca (ms; serve a rileggere per primi i siti piu vecchi).
 * RIGA 'Siti' nella scheda 'Stato': quanti controllati, OK, con problemi, in coda per il tempo, durata.
 *
 * LIMITI DI TEMPO (come il motore v2.22.3: FB_MAX_GIRO_ = 270 s): si smette di aprire siti allo scadere; quelli rimasti restano in coda e
 * si controllano al giro dopo (si parte dai piu vecchi); la scheda 'Siti' e la riga 'Stato' si scrivono SEMPRE.
 * Dentro il motore (v2.23-siti) il passo ha un budget proprio (SITI_BUDGET_MS_ = 60 s) per non allungare il giro.
 *
 * USO:  dentro il motore: chiamata FB_siti_(ss, t0) da FB_main_ (gia fatta nel motore-v2.23-siti.js).
 *       da solo: incolla questo file in un progetto Apps Script legato al foglio Fabbrica ed esegui SITI_main() (una volta, per provare);
 *       SITI_installaTrigger() la fa ripartire ogni 5 minuti, SITI_togliTrigger() la ferma.
 * Permessi: servono solo UrlFetchApp (script.external_request) e il foglio: gli stessi che il motore Fabbrica ha gia.
 * Non tocca Classroom, Moduli, Drive: legge soltanto fogli e pagine web pubbliche.
 */
var SITI_IN_ = 'Siti da controllare';
var SITI_OUT_ = 'Siti';
var SITI_MAX_MS_ = 270000;      // limite totale (uso da solo)
var SITI_BUDGET_MS_ = 60000;    // budget del passo dentro il motore
var SITI_OGNI_MIN_ = 5;         // un sito si riapre al massimo ogni 5 minuti
var SITI_MAX_IMG_ = 30;         // immagini controllate per sito
var SITI_BATCH_ = 10;           // siti per gruppo (fetchAll in parallelo)
var SITI_REPO_ATTESO_ = 'mio-sito';
var SITI_AUTO_DOCUMENTI_ = true;
var SITI_AUTO_ATTESO_ = true;
var SITI_TESTA_IN_ = ['COGNOME', 'URL sito', 'URL repository', 'Classe'];
var SITI_TESTA_OUT_ = ['COGNOME', 'Classe', 'URL sito', 'URL repository', 'Origine', 'HTTP', 'Titolo', 'N. immagini', 'Immagini OK', 'Immagini non raggiungibili', 'Dettaglio immagini', 'Esito', 'Controllato alle', 'Epoca (ms)'];

function SITI_ora_(f) { return Utilities.formatDate(new Date(), 'Europe/Rome', f || 'dd/MM/yyyy HH:mm:ss'); }
function SITI_norm_(s) { var t = String(s === null || s === undefined ? '' : s); if (t.normalize) t = t.normalize('NFD'); return t.toLowerCase().replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]/g, ''); }
function SITI_sn_(s) { return String(s === null || s === undefined ? '' : s).replace(/^\s+|\s+$/g, ''); }

/* ---------- URL ---------- */
function SITI_base_(url) {          // cartella della pagina, con la barra finale
  var u = String(url).split('#')[0].split('?')[0];
  if (/\/$/.test(u)) return u;
  var ult = u.split('/').pop();
  if (/^https?:$/.test(u.split('/')[0]) && u.split('/').length <= 3) return u + '/';    // solo il dominio
  return ult.indexOf('.') >= 0 ? u.substring(0, u.lastIndexOf('/') + 1) : u + '/';      // pagina.html -> cartella; /repo -> /repo/
}
function SITI_assoluto_(src, base) {
  var s = SITI_sn_(src).split('#')[0];
  if (!s) return null;
  if (/^data:/i.test(s)) return 'data:';
  var out;
  if (/^https?:\/\//i.test(s)) out = s;
  else if (/^\/\//.test(s)) out = 'https:' + s;
  else {
    var m = /^(https?:\/\/[^\/]+)(\/.*)?$/.exec(base), origine = m[1], path = m[2] || '/';
    var dir = path.charAt(0) === '/' && s.charAt(0) === '/' ? '' : path.substring(0, path.lastIndexOf('/') + 1);
    var pieces = (s.charAt(0) === '/' ? s : dir + s).split('?')[0].split('/'), res = [], i;
    for (i = 0; i < pieces.length; i++) {
      if (pieces[i] === '..') { if (res.length > 1) res.pop(); } else if (pieces[i] !== '.') res.push(pieces[i]);
    }
    var q = s.indexOf('?') >= 0 ? s.substring(s.indexOf('?')) : '';
    out = origine + res.join('/') + q;
  }
  return out.replace(/ /g, '%20');
}
function SITI_nomeFile_(url) { var p = String(url).split('?')[0].split('/'); return p[p.length - 1] || url; }
function SITI_decodifica_(t) {
  return String(t).replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ').replace(/&middot;/g, '\u00b7');
}
function SITI_titolo_(html) {
  var m = /<title[^>]*>([\s\S]*?)<\/title>/i.exec(html || '');
  return m ? SITI_decodifica_(m[1]).replace(/\s+/g, ' ').replace(/^\s+|\s+$/g, '').substring(0, 120) : '';
}
function SITI_immagini_(html, base) {   // -> { n: numero di <img> nella pagina, urls: assoluti unici (max SITI_MAX_IMG_), vuote: <img> senza src }
  var tags = (html || '').match(/<img\b[^>]*>/gi) || [], urls = [], vuote = 0, visti = {}, i, m, a;
  for (i = 0; i < tags.length; i++) {
    m = /\bsrc\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/i.exec(tags[i]);
    var src = m ? (m[1] !== undefined ? m[1] : (m[2] !== undefined ? m[2] : m[3])) : '';
    a = SITI_assoluto_(src, base);
    if (!a) { vuote++; continue; }
    if (!visti[a]) { visti[a] = 1; urls.push(a); }
  }
  return { n: tags.length, urls: urls.slice(0, SITI_MAX_IMG_), vuote: vuote, oltre: Math.max(0, urls.length - SITI_MAX_IMG_) };
}

/* ---------- rete ---------- */
function SITI_fetchTutti_(reqs, leggiCorpo) {
  var out = [], i;
  if (!reqs.length) return out;
  try {
    var r = UrlFetchApp.fetchAll(reqs);
    for (i = 0; i < r.length; i++) out.push({ code: r[i].getResponseCode(), body: leggiCorpo ? r[i].getContentText() : '' });
    return out;
  } catch (e) {            // un indirizzo non valido fa fallire tutto il gruppo: si rifa uno per uno
    for (i = 0; i < reqs.length; i++) {
      try { var x = UrlFetchApp.fetch(reqs[i].url, reqs[i]); out.push({ code: x.getResponseCode(), body: leggiCorpo ? x.getContentText() : '' }); }
      catch (e2) { out.push({ code: 0, body: '', err: String(e2 && e2.message ? e2.message : e2).substring(0, 80) }); }
    }
    return out;
  }
}
function SITI_req_(url, metodo) { return { url: url, method: metodo, muteHttpExceptions: true, followRedirects: true, headers: { 'Cache-Control': 'no-cache' } }; }

/* controlla un gruppo di righe: pagina (GET), poi per ogni <img> HEAD e, se non e 2xx, GET */
function SITI_controllaGruppo_(righe) {
  var pagine = SITI_fetchTutti_(righe.map(function (r) { return SITI_req_(r.sito, 'get'); }), true), tutte = [], mappa = {}, k, i, j;
  var info = pagine.map(function (p, idx) {
    var r = righe[idx], base = SITI_base_(r.sito), im = (p.code >= 200 && p.code < 300) ? SITI_immagini_(p.body, base) : { n: 0, urls: [], vuote: 0, oltre: 0 };
    im.urls.forEach(function (u) { if (u !== 'data:' && !mappa[u]) { mappa[u] = { esito: null }; tutte.push(u); } });
    return { riga: r, http: p.code, err: p.err || '', titolo: (p.code >= 200 && p.code < 300) ? SITI_titolo_(p.body) : '', im: im };
  });
  // HEAD in gruppi da 20, poi GET per quelle non 2xx
  for (i = 0; i < tutte.length; i += 20) {
    var ch = tutte.slice(i, i + 20), rh = SITI_fetchTutti_(ch.map(function (u) { return SITI_req_(u, 'head'); }), false), daRifare = [];
    for (j = 0; j < ch.length; j++) {
      if (rh[j].code >= 200 && rh[j].code < 300) mappa[ch[j]] = { code: rh[j].code, metodo: 'HEAD' };
      else daRifare.push(ch[j]);
    }
    if (daRifare.length) {
      var rg = SITI_fetchTutti_(daRifare.map(function (u) { return SITI_req_(u, 'get'); }), false);
      for (j = 0; j < daRifare.length; j++) mappa[daRifare[j]] = { code: rg[j].code, metodo: 'GET' };
    }
  }
  return info.map(function (x) {
    var det = [], rotte = [], ok = 0;
    x.im.urls.forEach(function (u) {
      if (u === 'data:') { det.push('data (immagine nel codice) incorporata'); ok++; return; }
      var m = mappa[u] || { code: 0, metodo: 'GET' }, bene = m.code >= 200 && m.code < 300;
      det.push(m.code + ' ' + m.metodo + ' ' + SITI_nomeFile_(u));
      if (bene) ok++; else rotte.push(SITI_nomeFile_(u) + ' (' + m.code + ')');
    });
    if (x.im.vuote) { det.push('0 <img> con src vuoto: ' + x.im.vuote); rotte.push('src vuoto (' + x.im.vuote + ')'); }
    if (x.im.oltre) det.push('altre ' + x.im.oltre + ' immagini non controllate (limite ' + SITI_MAX_IMG_ + ')');
    var esito;
    if (x.http === 0) esito = 'NON RAGGIUNGIBILE' + (x.err ? ': ' + x.err : '');
    else if (x.http === 404) esito = 'PAGINA NON TROVATA (404): GitHub Pages non attivo o indirizzo sbagliato';
    else if (x.http < 200 || x.http >= 300) esito = 'ERRORE HTTP ' + x.http;
    else if (rotte.length) esito = 'IMMAGINI ROTTE (' + rotte.length + ')';
    else if (!x.titolo) esito = 'SENZA TITOLO';
    else esito = 'OK';
    return { http: x.http, titolo: x.titolo, n: x.im.n, ok: ok, rotte: rotte.join(', '), dettaglio: det.join('\n'), esito: esito };
  });
}

/* ---------- schede ---------- */
function SITI_leggiIn_(ss) {
  var sh = ss.getSheetByName(SITI_IN_);
  if (!sh) { sh = ss.insertSheet(SITI_IN_); sh.getRange(1, 1, 1, SITI_TESTA_IN_.length).setValues([SITI_TESTA_IN_]).setFontWeight('bold'); return { righe: [], creata: true }; }
  var v = sh.getDataRange().getValues(), righe = [], i;
  if (!v.length) return { righe: [], creata: false };
  var h = v[0].map(SITI_norm_), cC = h.indexOf('cognome'), cS = -1, cR = -1, cK = h.indexOf('classe');
  for (i = 0; i < h.length; i++) { if (cS < 0 && /sito/.test(h[i]) && !/repo/.test(h[i])) cS = i; if (cR < 0 && /repo/.test(h[i])) cR = i; }
  if (cC < 0) cC = 0; if (cS < 0) cS = 1; if (cR < 0) cR = 2;
  for (i = 1; i < v.length; i++) {
    var cog = SITI_sn_(v[i][cC]), sito = SITI_sn_(v[i][cS]), repo = SITI_sn_(v[i][cR]), cl = cK >= 0 ? SITI_sn_(v[i][cK]) : '', orig = 'scheda';
    if (!cog || (!sito && !repo)) continue;
    if (!sito && repo) { var d = SITI_daRepo_(repo); if (d) { sito = d; orig = 'derivato dall\'URL del repository'; } }
    if (!sito) continue;
    righe.push({ cognome: cog, sito: sito, repo: repo, classe: cl, origine: orig });
  }
  return { righe: righe, creata: false };
}
function SITI_daRepo_(repo) {
  var m = /^https?:\/\/(?:www\.)?github\.com\/([^\/\s]+)\/([^\/\s?#]+)/i.exec(repo || '');
  return m ? 'https://' + m[1].toLowerCase() + '.github.io/' + m[2].replace(/\.git$/, '') + '/' : null;
}
/* completamenti automatici: dal Documento (URL scritto dall'allievo) e dall'indirizzo atteso (utente da 'Utenti <CLASSE>') */
function SITI_auto_(ss, esistenti) {
  var presenti = {}, nuovi = [], sheets = ss.getSheets(), i, j;
  esistenti.forEach(function (r) { presenti[SITI_norm_(r.cognome)] = 1; });
  if (SITI_AUTO_DOCUMENTI_) {
    for (i = 0; i < sheets.length; i++) {
      var nome = sheets[i].getName(), m = /^Documenti (\S+)$/.exec(nome);
      if (!m || /pubblica/i.test(nome)) continue;
      var v = sheets[i].getDataRange().getValues(), hi = -1, cA = 0, cE = -1;
      for (j = 0; j < Math.min(v.length, 8); j++) { if (SITI_norm_(v[j][0]) === 'allievo') { hi = j; break; } }
      if (hi < 0) continue;
      for (j = 0; j < v[hi].length; j++) { if (SITI_norm_(v[hi][j]) === 'estrattodeltesto') cE = j; }
      if (cE < 0) continue;
      var perAllievo = {};
      for (j = hi + 1; j < v.length; j++) {
        var testo = String(v[j][cE] || ''), cog = SITI_sn_(v[j][cA]);
        if (!cog || !testo) continue;
        var s = /https?:\/\/[A-Za-z0-9-]+\.github\.io\/[^\s<>"')]+/i.exec(testo), r = /https?:\/\/(?:www\.)?github\.com\/[A-Za-z0-9-]+\/[^\s\/<>"')?#]+/i.exec(testo);
        if (!s && !r) continue;
        perAllievo[SITI_norm_(cog)] = { cognome: cog, sito: s ? s[0] : (SITI_daRepo_(r[0]) || ''), repo: r ? r[0] : '', classe: m[1], origine: 'scritto nel Documento (' + nome + ')' };
      }
      Object.keys(perAllievo).forEach(function (k) { if (!presenti[k] && perAllievo[k].sito) { presenti[k] = 1; nuovi.push(perAllievo[k]); } });
    }
  }
  if (SITI_AUTO_ATTESO_) {
    for (i = 0; i < sheets.length; i++) {
      var n2 = sheets[i].getName(), m2 = /^Utenti (\S+)$/.exec(n2);
      if (!m2) continue;
      var u = sheets[i].getDataRange().getValues();
      for (j = 1; j < u.length; j++) {
        var ut = SITI_sn_(u[j][1]), al = SITI_sn_(u[j][2]);
        if (!ut || ut === '-' || !al || presenti[SITI_norm_(al)]) continue;
        presenti[SITI_norm_(al)] = 1;
        nuovi.push({ cognome: al, sito: 'https://' + ut.toLowerCase() + '.github.io/' + SITI_REPO_ATTESO_ + '/', repo: 'https://github.com/' + ut + '/' + SITI_REPO_ATTESO_, classe: m2[1], origine: 'ATTESO (utente da ' + n2 + ', repository ' + SITI_REPO_ATTESO_ + ': l\'allievo non l\'ha scritto)' });
      }
    }
  }
  return nuovi;
}
function SITI_vecchi_(ss) {         // risultati gia scritti: chiave -> riga
  var sh = ss.getSheetByName(SITI_OUT_), out = {};
  if (!sh) return out;
  var v = sh.getDataRange().getValues(), i;
  for (i = 1; i < v.length; i++) {
    if (!v[i][0] || !v[i][2]) continue;
    out[SITI_norm_(v[i][0]) + '|' + SITI_sn_(v[i][2])] = v[i];
  }
  return out;
}
function SITI_riga_Stato_(ss, testo) {
  var sh = ss.getSheetByName('Stato') || ss.insertSheet('Stato'), v = sh.getDataRange().getValues(), i, riga = -1;
  for (i = 0; i < v.length; i++) { if (v[i][0] === 'Siti') { riga = i + 1; break; } }
  if (riga < 0) riga = Math.max(v.length, 8) + 1;
  sh.getRange(riga, 1, 1, 2).setValues([['Siti', testo]]);
}

/**
 * Passo completo. ss = foglio Fabbrica; t0 = inizio del giro del motore (o di questa esecuzione); budget = ms massimi per i siti.
 * -> { controllati, ok, problemi, inCoda, totale }
 */
function SITI_passo_(ss, t0, budget, limiteTotale) {
  var tS = Date.now(), inp = SITI_leggiIn_(ss), righe = inp.righe, i;
  var auto = SITI_auto_(ss, righe);
  righe = righe.concat(auto);
  var testata = SITI_TESTA_OUT_;
  if (!righe.length) {
    var vuoto = ss.getSheetByName(SITI_OUT_) || ss.insertSheet(SITI_OUT_);
    if (!vuoto.getDataRange().getValues().length || vuoto.getRange(1, 1).getValue() !== 'COGNOME') vuoto.getRange(1, 1, 1, testata.length).setValues([testata]).setFontWeight('bold');
    SITI_riga_Stato_(ss, 'nessun sito da controllare: compila la scheda \'' + SITI_IN_ + '\' (COGNOME, URL sito, URL repository)' + (inp.creata ? ' (scheda creata ora)' : '') + ' · ' + SITI_ora_('HH:mm:ss'));
    return { controllati: 0, ok: 0, problemi: 0, inCoda: 0, totale: 0 };
  }
  var vecchi = SITI_vecchi_(ss), ora = Date.now(), scaduto = SITI_OGNI_MIN_ * 60000;
  righe.forEach(function (r) {
    var v = vecchi[SITI_norm_(r.cognome) + '|' + r.sito];
    r.epoca = v ? Number(v[13]) || 0 : 0;
    r.prec = v || null;
  });
  var dovute = righe.filter(function (r) { return !r.epoca || ora - r.epoca >= scaduto; }).sort(function (a, b) { return a.epoca - b.epoca; });
  var fatte = 0, risultati = {};
  function fuori() { return (Date.now() - tS >= budget) || (Date.now() - t0 >= limiteTotale); }
  for (i = 0; i < dovute.length; i += SITI_BATCH_) {
    if (fuori()) break;
    var gruppo = dovute.slice(i, i + SITI_BATCH_), esiti;
    try { esiti = SITI_controllaGruppo_(gruppo); } catch (e) { esiti = gruppo.map(function () { return { http: 0, titolo: '', n: 0, ok: 0, rotte: '', dettaglio: '', esito: 'ERRORE DEL CONTROLLO: ' + String(e && e.message ? e.message : e).substring(0, 80) }; }); }
    gruppo.forEach(function (r, k) { risultati[SITI_norm_(r.cognome) + '|' + r.sito] = esiti[k]; fatte++; });
  }
  var adesso = Date.now(), out = [], ok = 0, problemi = 0;
  righe.forEach(function (r) {
    var k = SITI_norm_(r.cognome) + '|' + r.sito, e = risultati[k];
    if (e) { out.push([r.cognome, r.classe, r.sito, r.repo, r.origine, e.http, e.titolo, e.n, e.ok, e.rotte, e.dettaglio, e.esito, SITI_ora_(), adesso]); if (e.esito === 'OK') ok++; else problemi++; }
    else if (r.prec) { var p = r.prec.slice(0, 14); p[1] = r.classe || p[1]; p[3] = r.repo || p[3]; p[4] = r.origine; out.push(p); if (p[11] === 'OK') ok++; else problemi++; }
    else out.push([r.cognome, r.classe, r.sito, r.repo, r.origine, '', '', '', '', '', '', 'DA CONTROLLARE (in coda)', '', 0]);
  });
  out.sort(function (a, b) { return String(a[0]).localeCompare(String(b[0])); });
  var sh = ss.getSheetByName(SITI_OUT_) || ss.insertSheet(SITI_OUT_);
  sh.clear();
  sh.getRange(1, 1, 1, testata.length).setValues([testata]).setFontWeight('bold');
  sh.getRange(2, 1, out.length, testata.length).setValues(out);
  sh.setFrozenRows(1);
  var inCoda = dovute.length - fatte;
  SITI_riga_Stato_(ss, 'controllati ' + fatte + ' di ' + righe.length + ' · OK ' + ok + ' · con problemi ' + problemi + (inCoda ? ' · IN CODA per il tempo: ' + inCoda + ' (riprendono al giro dopo)' : '') +
    (righe.length - dovute.length ? ' · ' + (righe.length - dovute.length) + ' controllati meno di ' + SITI_OGNI_MIN_ + ' minuti fa' : '') +
    ' · di cui ' + auto.length + ' completati da soli (Documento o indirizzo atteso) · durata ' + Math.round((Date.now() - tS) / 1000) + ' s · alle ' + SITI_ora_('HH:mm:ss'));
  return { controllati: fatte, ok: ok, problemi: problemi, inCoda: inCoda, totale: righe.length };
}

/* chiamata dal motore: FB_siti_(ss, t0) dentro passo('siti', ...) */
function FB_siti_(ss, t0) {
  return SITI_passo_(ss, t0 || Date.now(), SITI_BUDGET_MS_, (typeof FB_MAX_GIRO_ !== 'undefined' ? FB_MAX_GIRO_ : SITI_MAX_MS_));
}

/* uso da solo */
function SITI_foglio_() {
  var ss = null;
  try { ss = SpreadsheetApp.getActiveSpreadsheet(); } catch (e) { ss = null; }
  if (!ss) { var id = PropertiesService.getScriptProperties().getProperty('FB_FOGLIO'); if (id) ss = SpreadsheetApp.openById(id); }
  return ss;
}
function SITI_main() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var ss = SITI_foglio_();
    if (!ss) throw new Error('foglio non trovato: apri lo script dal foglio Fabbrica (Estensioni, Apps Script) oppure imposta FB_FOGLIO');
    var t0 = Date.now(), r;
    try { r = SITI_passo_(ss, t0, SITI_MAX_MS_, SITI_MAX_MS_); }
    catch (e) { SITI_riga_Stato_(ss, 'ERRORE: ' + String(e && e.message ? e.message : e).substring(0, 160) + ' · alle ' + SITI_ora_('HH:mm:ss')); throw e; }
    return r;
  } finally { lock.releaseLock(); }
}
function SITI_installaTrigger() {
  SITI_togliTrigger();
  ScriptApp.newTrigger('SITI_main').timeBased().everyMinutes(5).create();
}
function SITI_togliTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'SITI_main') ScriptApp.deleteTrigger(t); });
}
