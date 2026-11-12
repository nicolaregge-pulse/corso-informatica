/**
 * LAVAGNA - web app Google Apps Script v1.0 (12/11/2026)
 * Riceve i lavori della pagina docs/lavagna/ (disegni dei ragazzi), li salva in Drive e scrive una riga nel foglio Fabbrica.
 *
 * NON ATTIVA finche il docente non la pubblica (vedi riservato report/2026-11-12/LAVAGNA-ATTIVAZIONE-v1.0.md).
 * Si pubblica come WEB APP: «Esegui come: me» (account PIAMARTA), «Chi ha accesso: chiunque nel dominio piamarta».
 * Cosi Session.getActiveUser().getEmail() riconosce il ragazzo (se il browser manda i cookie dell'account scuola).
 *
 * Che cosa fa
 *  - doPost(e): corpo «d=<JSON>» con {specId, versione, nonce, ora, durata, lingue, ordine, passi, esiti, png (base64)}.
 *      Controlla i limiti, legge l'email dalla sessione (mai dal corpo), salva in Drive «Lavagna/<specId>/<email>_<data>.png»
 *      e il risultato (senza PNG) in «<email>_<data>.json», aggiunge una riga alla scheda «Lavagna» del foglio Fabbrica.
 *      Lo stesso nonce non si salva due volte (un nuovo invio dello stesso lavoro dice «gia arrivato»).
 *  - doGet(e): ?azione=seme&specId=...    -> {ok, seme}  seme fisso per ragazzo e compito (hash, niente email): ordine dei passi
 *              ?azione=ricevuta&specId=...&nonce=... -> {ok, trovata, ora, riconosciuto}  prova che il lavoro e arrivato
 *              (vale solo per chi ha spedito; mai l'email nella risposta). Con &callback=nome risponde in JSONP.
 *  - LAV_prepara(): si lancia UNA volta a mano: crea la cartella «Lavagna», la scheda «Lavagna», il sale del seme.
 *  - LAV_autotest(): prova senza pagina: salva un lavoro finto «test-autotest» e scrive l'esito nel registro.
 *
 * Limiti: PNG al massimo 2,5 MB, risultato JSON al massimo 400 KB, al massimo 30 lavori per ragazzo e compito.
 * Nessun cognome e nessuna password nel codice. L'id del foglio non e scritto qui: si trova per nome o sta in FOGLIO_FABBRICA.
 */

var LAV_VERSIONE = '1.0';
var LAV_MAX_PNG = 2500000;
var LAV_MAX_JSON = 400000;
var LAV_MAX_PER_UTENTE = 30;
var LAV_SCHEDA = 'Lavagna';
var LAV_CARTELLA = 'Lavagna';
var LAV_TESTA = ['Arrivo', 'specId', 'Email', 'Ora del ragazzo', 'Esito automatico', 'Da guardare', 'File PNG', 'File JSON', 'Nonce', 'Riconosciuto', 'Durata (s)', 'Ordine dei passi'];
var LAV_COL_NONCE = 9;

/* ------------------------------------------------------------------ proprieta e cartelle */
function LAV_p_() { return PropertiesService.getScriptProperties(); }

function LAV_sale_() {
  var p = LAV_p_(), s = p.getProperty('LAV_SALE');
  if (!s) { s = Utilities.getUuid() + Utilities.getUuid(); p.setProperty('LAV_SALE', s); }
  return s;
}

function LAV_foglio_() {
  var p = LAV_p_(), id = p.getProperty('FOGLIO_FABBRICA');
  if (id) return SpreadsheetApp.openById(id);
  var it = DriveApp.searchFiles("title contains 'Fabbrica' and mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false");
  var trovati = [];
  while (it.hasNext()) { var f = it.next(); if (/^Fabbrica\b/.test(f.getName())) trovati.push(f); }
  if (trovati.length !== 1) {
    throw new Error('Foglio Fabbrica non trovato o ambiguo (' + trovati.length + ' file). Aggiungi la proprieta di script FOGLIO_FABBRICA con l\'id del foglio.');
  }
  p.setProperty('FOGLIO_FABBRICA', trovati[0].getId());
  return SpreadsheetApp.openById(trovati[0].getId());
}

function LAV_scheda_(ss) {
  var sh = ss.getSheetByName(LAV_SCHEDA);
  if (!sh) sh = ss.insertSheet(LAV_SCHEDA);
  if (sh.getLastRow() < 1) {
    sh.getRange(1, 1, 1, LAV_TESTA.length).setValues([LAV_TESTA]).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function LAV_radice_() {
  var p = LAV_p_(), id = p.getProperty('LAV_CARTELLA_ID');
  if (id) { try { return DriveApp.getFolderById(id); } catch (x) {} }
  var it = DriveApp.getFoldersByName(LAV_CARTELLA), f = it.hasNext() ? it.next() : DriveApp.createFolder(LAV_CARTELLA);
  p.setProperty('LAV_CARTELLA_ID', f.getId());
  return f;
}

function LAV_sotto_(padre, nome) {
  var it = padre.getFoldersByName(nome);
  return it.hasNext() ? it.next() : padre.createFolder(nome);
}

/* ------------------------------------------------------------------ utilita */
function LAV_email_() {
  var e = '';
  try { e = Session.getActiveUser().getEmail() || ''; } catch (x) {}
  return String(e).toLowerCase();
}

function LAV_slug_(s) { return String(s).replace(/[^a-z0-9@._-]/gi, '_').slice(0, 80); }

function LAV_risposta_(obj, e) {
  var json = JSON.stringify(obj);
  var cb = e && e.parameter && e.parameter.callback;
  if (cb && /^[\w$.]{1,60}$/.test(cb)) {
    return ContentService.createTextOutput(cb + '(' + json + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(json).setMimeType(ContentService.MimeType.JSON);
}

function LAV_riga_(sh, nonce) {
  var n = sh.getLastRow();
  if (n < 2) return 0;
  var r = sh.getRange(2, LAV_COL_NONCE, n - 1, 1).createTextFinder(nonce).matchEntireCell(true).findNext();
  return r ? r.getRow() : 0;
}

function LAV_seme_(email, specId) {
  var raw = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, email + '|' + LAV_sale_() + '|' + specId, Utilities.Charset.UTF_8);
  return raw.slice(0, 8).map(function (b) { return ('0' + (b & 255).toString(16)).slice(-2); }).join('');
}

/* ------------------------------------------------------------------ salvataggio */
function LAV_salva_(d, email, bytes) {
  var specId = String(d.specId || ''), nonce = String(d.nonce || '');
  var ss = LAV_foglio_(), sh = LAV_scheda_(ss);
  var riga = LAV_riga_(sh, nonce);
  if (riga) {
    var a = sh.getRange(riga, 1).getValue();
    return { ok: true, gia: true, nonce: nonce, ora: (a && a.toISOString) ? a.toISOString() : new Date().toISOString(), riconosciuto: !!email };
  }
  if (email && sh.getLastRow() > 1) {
    var v = sh.getRange(2, 2, sh.getLastRow() - 1, 2).getValues(), k = 0;
    for (var i = 0; i < v.length; i++) { if (v[i][0] === specId && String(v[i][1]).toLowerCase() === email) k++; }
    if (k >= LAV_MAX_PER_UTENTE) return { ok: false, errore: 'troppi_invii' };
  }
  var ora = new Date();
  var stamp = Utilities.formatDate(ora, 'Europe/Rome', 'yyyyMMdd-HHmmss');
  var nome = (email ? LAV_slug_(email) : 'anonimo-' + nonce) + '_' + stamp;
  var cart = LAV_sotto_(LAV_radice_(), specId);
  var png = cart.createFile(Utilities.newBlob(bytes, 'image/png', nome + '.png'));
  var ris = JSON.parse(JSON.stringify(d)); delete ris.png;
  ris.arrivo = ora.toISOString(); ris.riconosciuto = !!email;
  var js = cart.createFile(Utilities.newBlob(JSON.stringify(ris), 'application/json', nome + '.json'));
  var esiti = d.esiti || {};
  var guardare = (esiti.da_valutare || 0);
  sh.appendRow([ora, specId, email, String(d.ora || ''), String(esiti.automatico || ''), guardare, png.getUrl(), js.getUrl(), nonce,
    email ? 'SI' : 'NO', Number(d.durata) || 0, (d.ordine || []).join(',')]);
  return { ok: true, gia: false, nonce: nonce, ora: ora.toISOString(), riconosciuto: !!email };
}

/* ------------------------------------------------------------------ web app */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    var corpo = (e && e.parameter && e.parameter.d) || (e && e.postData && e.postData.contents) || '';
    if (!corpo) return LAV_risposta_({ ok: false, errore: 'vuoto' }, e);
    var d;
    try { d = JSON.parse(corpo); } catch (x) { return LAV_risposta_({ ok: false, errore: 'json' }, e); }
    var specId = String(d.specId || ''), nonce = String(d.nonce || '');
    if (!/^[a-z0-9-]{1,80}$/.test(specId)) return LAV_risposta_({ ok: false, errore: 'specId' }, e);
    if (!/^[0-9a-f]{16}$/.test(nonce)) return LAV_risposta_({ ok: false, errore: 'nonce' }, e);
    var b64 = String(d.png || '');
    if (!b64 || b64.length > Math.ceil(LAV_MAX_PNG * 4 / 3) + 8) return LAV_risposta_({ ok: false, errore: 'png_dimensione' }, e);
    var senza = JSON.parse(JSON.stringify(d)); delete senza.png;
    if (JSON.stringify(senza).length > LAV_MAX_JSON) return LAV_risposta_({ ok: false, errore: 'json_dimensione' }, e);
    var bytes = Utilities.base64Decode(b64);
    if (bytes.length > LAV_MAX_PNG || bytes.length < 8 || bytes[0] !== -119 || bytes[1] !== 80 || bytes[2] !== 78 || bytes[3] !== 71) {
      return LAV_risposta_({ ok: false, errore: 'png' }, e);
    }
    lock.waitLock(25000);
    return LAV_risposta_(LAV_salva_(d, LAV_email_(), bytes), e);
  } catch (x) {
    Logger.log('Lavagna doPost: ' + x);
    return LAV_risposta_({ ok: false, errore: 'interno' }, e);
  } finally {
    try { lock.releaseLock(); } catch (y) {}
  }
}

function doGet(e) {
  try {
    var p = (e && e.parameter) || {}, az = p.azione || '';
    var specId = String(p.specId || '');
    if (az === 'seme') {
      if (!/^[a-z0-9-]{1,80}$/.test(specId)) return LAV_risposta_({ ok: false, errore: 'specId' }, e);
      var em = LAV_email_();
      return LAV_risposta_({ ok: true, seme: em ? LAV_seme_(em, specId) : '' }, e);
    }
    if (az === 'ricevuta') {
      var nonce = String(p.nonce || '');
      if (!/^[a-z0-9-]{1,80}$/.test(specId) || !/^[0-9a-f]{16}$/.test(nonce)) return LAV_risposta_({ ok: false, errore: 'parametri' }, e);
      var sh = LAV_scheda_(LAV_foglio_()), riga = LAV_riga_(sh, nonce);
      if (!riga) return LAV_risposta_({ ok: true, trovata: false }, e);
      var v = sh.getRange(riga, 1, 1, LAV_COL_NONCE + 1).getValues()[0];
      var chi = LAV_email_();
      if (v[1] !== specId || String(v[2]).toLowerCase() !== chi) return LAV_risposta_({ ok: true, trovata: false }, e);
      var a = v[0];
      return LAV_risposta_({ ok: true, trovata: true, ora: (a && a.toISOString) ? a.toISOString() : null, riconosciuto: v[LAV_COL_NONCE] === 'SI' }, e);
    }
    return LAV_risposta_({ ok: true, servizio: 'lavagna', versione: LAV_VERSIONE }, e);
  } catch (x) {
    Logger.log('Lavagna doGet: ' + x);
    return LAV_risposta_({ ok: false, errore: 'interno' }, e);
  }
}

/* ------------------------------------------------------------------ da lanciare a mano */
function LAV_prepara() {
  LAV_sale_();
  var ss = LAV_foglio_(), sh = LAV_scheda_(ss), radice = LAV_radice_();
  var msg = 'Lavagna pronta. Foglio: ' + ss.getName() + ' (scheda «' + sh.getName() + '»). Cartella Drive: ' + radice.getName() + ' ' + radice.getUrl();
  Logger.log(msg);
  return msg;
}

function LAV_autotest() {
  var png1 = Utilities.base64Decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==');
  var d = { specId: 'test-autotest', versione: '0', nonce: Utilities.getUuid().replace(/-/g, '').slice(0, 16), ora: new Date().toISOString(), durata: 1, ordine: ['t1'],
    passi: [], esiti: { automatico: '0 su 0', da_valutare: 0 } };
  var r = LAV_salva_(d, LAV_email_() || 'autotest@locale', png1);
  var msg = 'Autotest: ' + JSON.stringify(r) + '. Cancella a mano la riga «test-autotest» della scheda Lavagna e la cartella Lavagna/test-autotest.';
  Logger.log(msg);
  return msg;
}
