/**
 * CRUSCOTTO WEB (tempo reale) - Apps Script v1.0 (20/11/2026)
 * File da incollare come file SEPARATO (nome: cruscotto_web) nello STESSO progetto Apps Script del motore Fabbrica
 * (account PIAMARTA, il progetto che ha le funzioni ciclo/installa del lancio). Non tocca motore.js ne il lancio.
 *
 * COSA FA (due parti)
 *  A) JOB LEGGERO live_giro(): trigger a tempo ogni 1 minuto (si crea una volta con live_installa()). Legge SOLO
 *     - i compiti di Classroom della classe con titolo «GG/MM Ora N» di OGGI (stato di ogni allievo) e
 *     - le risposte dei Moduli dei quiz di OGGI (chi ha risposto)
 *     e scrive una scheda piccola «Live <CLASSE>» nel foglio Fabbrica (solo «Nome I.», mai email, mai voti).
 *     Non legge storico, Documenti, Git, Situazione, ecc.: quelle restano al motore (giro lungo, ogni qualche minuto).
 *  B) WEB APP doGet(e): ?classe=1inf|2inf|3inf|4ti  -> JSON letto SOLO dalla scheda «Live <CLASSE>» (risponde in meno di 2 s).
 *     Con &callback=nome risponde in JSONP (riserva se il browser blocca il fetch tra domini).
 *
 * CALCOLO DEL TEMPO DEL JOB (stima, NON provata su Google: da verificare con live_prova(), il log dice la durata vera)
 *  per classe: elenco iscritti (1 chiamata, in cache 20 min) ~1 s + elenco compiti (1 chiamata) ~1 s
 *              + consegne di ogni compito di oggi (1 chiamata ciascuno, 3-4 compiti) ~1-2 s l'una = 4-8 s
 *              + per ogni quiz di oggi FormApp.openById + getResponses ~1-3 s (2-5 quiz) = 3-12 s
 *              + lettura Esiti/Corsi/Abbinamenti + scrittura della scheda Live ~2 s
 *       => circa 10-25 s per classe. Il job non INIZIA una classe dopo 30 s dall'avvio e si ferma a 50 s: sotto il minuto.
 *  Con 4 classi nello stesso giro si puo superare: si fa lavorare per prima la classe con il dato piu vecchio (nessuna resta indietro)
 *  e, per avere un dato ogni minuto sulla classe che il docente segue, si imposta la proprieta LV_CLASSI (vedi PASSI-DOCENTE).
 *
 * LIMITI NOTI
 *  - Quota Apps Script: il tempo totale dei trigger al giorno e limitato (di norma 90 min per account normali, 6 ore Workspace;
 *    NON provato quale vale per l'account PIAMARTA). Per questo il job esce subito fuori dall'orario (lun-ven 07:45-14:20, Roma).
 *  - I compiti non si leggono se il titolo non comincia con «GG/MM Ora N» (stessa regola del motore).
 *  - I quiz di oggi = lavori di fabbrica/indice.json (o Esiti) il cui id contiene GGMM di oggi (es. quiz-1inf-2011-ora4) o il cui
 *    titolo contiene GG/MM di oggi; le versioni dello stesso quiz si uniscono SOLO se indice.json ha il campo «versioni».
 *  - Usa LockService.getUserLock(): il motore usa getScriptLock(), quindi i due non si bloccano a vicenda.
 *
 * R1: nel JSON e nella scheda Live: solo «Nome I.» (stesso algoritmo del motore, SM_brevi_), mai email, cognomi, note, voti.
 * R7: se qualcosa non si legge, la scheda dice stato «non_letto» o «parziale» con il motivo; niente numeri inventati.
 * Nomi: tutte le funzioni e variabili globali hanno prefisso LV_ / live_ e doGet esiste solo qui (il motore non ha doGet;
 * il codice del motore gira dentro eval in ciclo(), quindi non ci sono conflitti di nomi).
 */

var LV_VERSIONE = '1.0';
var LV_CLASSI_TUTTE = ['1INF', '2INF', '3INF', '4TI'];
var LV_AVVIO_MAX_MS = 30000;   // dopo 30 s dall'avvio non si inizia un'altra classe
var LV_FINE_MS = 50000;        // a 50 s si smette di leggere e si scrive quello che c'e (stato «parziale»)
var LV_META = 8;               // righe prima dei dati: 1..7 intestazioni, 8 = testata colonne, dati dalla 9
var LV_BASE_DEFAULT = 'https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/fabbrica/';

/* ---------- servizi di base ---------- */
function LV_roma_(d, f) { return Utilities.formatDate(d || new Date(), 'Europe/Rome', f); }
function LV_iso_(d) { return LV_roma_(d, "yyyy-MM-dd'T'HH:mm:ssXXX"); }

function LV_foglio_() {
  var p = PropertiesService.getScriptProperties(), id = p.getProperty('FB_FOGLIO');
  if (id) return SpreadsheetApp.openById(id);
  try { var a = SpreadsheetApp.getActive(); if (a) return a; } catch (e) { }
  var it = DriveApp.getFilesByName('Fabbrica (10/11/2026)');
  if (it.hasNext()) return SpreadsheetApp.open(it.next());
  throw new Error('foglio Fabbrica non trovato (manca la proprieta FB_FOGLIO)');
}

/* ---------- «Nome I.»: stesso algoritmo del motore (SM_brevi_), copiato qui perche il motore gira in eval ---------- */
var LV_PART_ = { DE: 1, DI: 1, DA: 1, DEL: 1, DELLA: 1, DEI: 1, DEGLI: 1, DAL: 1, DALLA: 1, DALL: 1, DELLE: 1, LO: 1, LA: 1, LE: 1, EL: 1, AL: 1, BEN: 1, BIN: 1, BEL: 1, ABD: 1, ABDEL: 1, ABDUL: 1, ABU: 1, ABOU: 1, OULD: 1, VAN: 1, VON: 1, DOS: 1, DAS: 1, DU: 1, SAN: 1, SANTA: 1, MAC: 1, MC: 1 };
function LV_cap_(w) { return String(w || '').toLowerCase().replace(/(^|[-'’\s])([a-zà-ÿ])/g, function (m, a, b) { return a + b.toUpperCase(); }); }
function LV_tuttoMai_(t) { return t === t.toUpperCase() && t !== t.toLowerCase(); }
function LV_parti_(s, k) {
  s = String(s || '').replace(/\s+/g, ' ').trim();
  if (s.indexOf('@') > 0) return { nome: 'Allievo ' + (k + 1), cog: '' };   // mai un'email in uscita
  var p = s.split(' ').filter(function (x) { return x; });
  if (p.length < 2) return { nome: p.length ? LV_cap_(p[0]) : 'Allievo ' + (k + 1), cog: '' };
  var nc = 0;
  while (nc < p.length && LV_tuttoMai_(p[nc])) nc++;
  if (nc === 0 || nc === p.length) {
    nc = 0;
    while (nc < p.length - 2 && LV_PART_[p[nc].toUpperCase().replace(/[.']/g, '')]) nc++;
    nc++;
    if (p.length - nc >= 2) nc = p.length - 1;
  }
  return { nome: p.slice(nc).map(LV_cap_).join(' '), cog: p.slice(0, nc).join(' ').toUpperCase() };
}
function LV_brevi_(nomi) {
  var pt = nomi.map(function (n, k) { return LV_parti_(n, k); }), lab = [], i, L;
  function etichetta(p, n) {
    var sl = String(p.cog || '').toUpperCase().replace(/[^A-ZÀ-Ý]/g, '');
    if (!sl) return p.nome;
    return p.nome + ' ' + sl.charAt(0) + sl.slice(1, n).toLowerCase() + '.';
  }
  for (i = 0; i < pt.length; i++) lab.push(etichetta(pt[i], 1));
  for (L = 2; L <= 4; L++) {
    var conta = {};
    lab.forEach(function (x) { conta[x.toUpperCase()] = (conta[x.toUpperCase()] || 0) + 1; });
    for (i = 0; i < lab.length; i++) if (conta[lab[i].toUpperCase()] > 1) lab[i] = etichetta(pt[i], L);
  }
  var vis = {};
  for (i = 0; i < lab.length; i++) {
    var u = lab[i].toUpperCase();
    if (vis[u]) { vis[u]++; lab[i] = lab[i] + ' (' + vis[u] + ')'; } else vis[u] = 1;
  }
  return lab;
}

/* ---------- Classroom ---------- */
function LV_corsoId_(ss, classe) {
  var sh = ss.getSheetByName('Corsi');
  if (!sh) return '';
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (String(v[i][2]).toUpperCase() === classe && v[i][1] !== '') return String(v[i][1]).replace(/\.0+$/, '');
  return '';
}
function LV_iscritti_(corsoId, classe) {
  var cache = CacheService.getScriptCache(), k = 'LV_R_' + classe + '_' + corsoId, c = cache.get(k);
  if (c) { try { return JSON.parse(c); } catch (e) { } }
  var out = [], tok = null, r;
  do {
    r = Classroom.Courses.Students.list(corsoId, { pageSize: 100, pageToken: tok || undefined });
    (r.students || []).forEach(function (s) {
      var n = (s.profile && s.profile.name) || {};
      out.push({ u: s.userId, e: String((s.profile && s.profile.emailAddress) || '').toLowerCase(), c: n.familyName || '', n: n.givenName || '', f: n.fullName || '' });
    });
    tok = r.nextPageToken || null;
  } while (tok);
  try { cache.put(k, JSON.stringify(out), 1200); } catch (e) { }
  return out;
}
function LV_nomeCR_(s) { return (s.c && s.n) ? String(s.c).toUpperCase() + ' ' + s.n : (s.f || '(senza nome)'); }
function LV_statoSub_(s) {   // come CR_statoSub_ del motore
  if (s.state === 'RETURNED') return 'RICONSEGNATO';
  if (s.state === 'TURNED_IN') {
    var h = s.submissionHistory || [];
    for (var i = 0; i < h.length; i++) if (h[i] && h[i].stateHistory && h[i].stateHistory.state === 'RETURNED') return 'RICONSEGNATO';
    return 'CONSEGNATO';
  }
  return 'ASSEGNATO';
}
function LV_compitiOggi_(corsoId, gg, mm) {
  var r = Classroom.Courses.CourseWork.list(corsoId, { courseWorkStates: ['PUBLISHED'], orderBy: 'updateTime desc', pageSize: 30 });
  var out = [];
  (r.courseWork || []).forEach(function (w) {
    var m = /^\s*(\d{1,2})\s*\/\s*(\d{1,2})\s+Ora\s*(\d+)/i.exec(String(w.title || ''));
    if (m && Number(m[1]) === gg && Number(m[2]) === mm) out.push({ id: w.id, titolo: String(w.title), ora: Number(m[3]), link: w.alternateLink || '' });
  });
  out.sort(function (a, b) { return a.ora - b.ora; });
  return out;
}
function LV_consegne_(corsoId, wid) {
  var out = {}, tok = null, r;
  do {
    r = Classroom.Courses.CourseWork.StudentSubmissions.list(corsoId, wid, { pageSize: 100, pageToken: tok || undefined });
    (r.studentSubmissions || []).forEach(function (s) { out[s.userId] = { stato: LV_statoSub_(s), t: s.updateTime || '' }; });
    tok = r.nextPageToken || null;
  } while (tok);
  return out;
}

/* ---------- quiz di oggi ---------- */
function LV_indice_() {
  var cache = CacheService.getScriptCache(), c = cache.get('LV_INDICE');
  if (c) { try { return JSON.parse(c); } catch (e) { } }
  var base = (typeof FB_BASE !== 'undefined') ? FB_BASE : LV_BASE_DEFAULT;
  var r = UrlFetchApp.fetch(base + 'indice.json?t=' + Date.now(), { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('indice.json HTTP ' + r.getResponseCode());
  var t = r.getContentText();
  var d = JSON.parse(t), min = { lavori: (d.lavori || []).map(function (l) { return { id: l.id, versioni: l.versioni || [] }; }) };
  try { cache.put('LV_INDICE', JSON.stringify(min), 300); } catch (e) { }
  return min;
}
function LV_esiti_(ss) {   // id -> {titolo, link, classe, formId}
  var sh = ss.getSheetByName('Esiti'), out = {};
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][1]) out[String(v[i][1])] = { titolo: String(v[i][2] || ''), link: String(v[i][3] || ''), classe: String(v[i][6] || '').toUpperCase(), formId: String(v[i][7] || '') };
  return out;
}
/* quiz attivi di oggi per la classe: [{id, titolo, link, ids:[id attivo + versioni con Moduli creato]}] */
function LV_quizOggi_(ss, classe, gg, mm) {
  var esiti = LV_esiti_(ss), ind = LV_indice_(), gm = (gg < 10 ? '0' : '') + gg + (mm < 10 ? '0' : '') + mm;
  var reId = new RegExp('(^|-)' + gm + '(-|$)'), reTit = new RegExp('(^|\\D)0?' + gg + '\\s*/\\s*0?' + mm + '(\\D|$)');
  var assorbiti = {};
  ind.lavori.forEach(function (l) { (l.versioni || []).forEach(function (v) { if (v !== l.id) assorbiti[v] = 1; }); });
  var out = [];
  ind.lavori.forEach(function (l) {
    var e = esiti[l.id];
    if (!e || e.classe !== classe || assorbiti[l.id]) return;
    if (!(reId.test(l.id) || reTit.test(e.titolo))) return;
    var ids = (l.versioni && l.versioni.length ? l.versioni.slice() : []);
    if (ids.indexOf(l.id) < 0) ids.push(l.id);
    ids = ids.filter(function (x) { return esiti[x] && esiti[x].formId; });
    if (ids.length) out.push({ id: l.id, titolo: e.titolo, link: e.link, ids: ids, forms: ids.map(function (x) { return esiti[x].formId; }) });
  });
  return out;
}
function LV_abbinamenti_(ss, classe) {   // email -> 'COGNOME Nome' (scheda Abbinamenti, solo uso interno)
  var sh = ss.getSheetByName('Abbinamenti ' + classe), out = {};
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][0] && v[i][1] && String(v[i][1]) !== '-') out[String(v[i][0]).toLowerCase()] = String(v[i][1]).toUpperCase();
  return out;
}

/* ---------- una classe ---------- */
function LV_classe_(ss, classe, t0) {
  var ora = new Date(), gg = Number(LV_roma_(ora, 'd')), mm = Number(LV_roma_(ora, 'M')), giorno = LV_roma_(ora, 'yyyy-MM-dd');
  var avvisi = [], stato = 'ok', motivo = '';
  var corso = LV_corsoId_(ss, classe);
  if (!corso) { LV_scriviErrore_(ss, classe, 'corso Classroom non trovato nella scheda Corsi'); return; }
  var isc = LV_iscritti_(corso, classe);
  if (!isc.length) { LV_scriviErrore_(ss, classe, 'nessun iscritto letto dal corso Classroom'); return; }
  isc.sort(function (a, b) { var x = LV_nomeCR_(a), y = LV_nomeCR_(b); return x < y ? -1 : (x > y ? 1 : 0); });
  var etich = LV_brevi_(isc.map(LV_nomeCR_)), perUtente = {}, perEmail = {}, perNome = {};
  isc.forEach(function (s, i) { perUtente[s.u] = i; if (s.e) perEmail[s.e] = i; perNome[LV_nomeCR_(s).toUpperCase()] = i; });
  var ab = LV_abbinamenti_(ss, classe);
  Object.keys(ab).forEach(function (em) { if (perEmail[em] === undefined && perNome[ab[em]] !== undefined) perEmail[em] = perNome[ab[em]]; });
  var ultimo = isc.map(function () { return ''; });
  function agg(i, iso) { var ms = Date.parse(iso); if (isNaN(ms)) return; var cur = ultimo[i] ? Date.parse(ultimo[i]) : 0; if (ms > cur) ultimo[i] = LV_iso_(new Date(ms)); }
  var colonne = [], dati = isc.map(function () { return []; });
  // compiti di oggi
  var compiti = LV_compitiOggi_(corso, gg, mm);
  for (var c = 0; c < compiti.length; c++) {
    if (Date.now() - t0 > LV_FINE_MS) { stato = 'parziale'; motivo = 'tempo del giro finito: compiti ' + compiti.slice(c).map(function (x) { return 'Ora ' + x.ora; }).join(', ') + ' non letti'; break; }
    var cons = LV_consegne_(corso, compiti[c].id);
    colonne.push({ k: 'C', titolo: compiti[c].titolo, link: compiti[c].link, ora: compiti[c].ora });
    isc.forEach(function (s, i) {
      var x = cons[s.u];
      dati[i].push(x ? x.stato : '-');
      if (x && x.stato !== 'ASSEGNATO') agg(i, x.t);
    });
  }
  // quiz di oggi
  var quiz = [], nonAbb = 0;
  try { quiz = LV_quizOggi_(ss, classe, gg, mm); } catch (e) { avvisi.push('quiz di oggi non letti: ' + String(e.message || e).slice(0, 120)); stato = 'parziale'; }
  for (var q = 0; q < quiz.length; q++) {
    if (Date.now() - t0 > LV_FINE_MS) { stato = 'parziale'; motivo = (motivo ? motivo + '; ' : '') + 'tempo del giro finito: quiz ' + quiz.slice(q).map(function (x) { return x.id; }).join(', ') + ' non letti'; break; }
    var fatti = {};
    quiz[q].forms.forEach(function (fid) {
      var ris = FormApp.openById(fid).getResponses();
      ris.forEach(function (r) {
        var em = String(r.getRespondentEmail() || '').toLowerCase(), i = perEmail[em];
        if (i === undefined) { nonAbb++; return; }
        fatti[i] = 1; agg(i, LV_iso_(r.getTimestamp()));
      });
    });
    colonne.push({ k: 'Q', id: quiz[q].id, titolo: quiz[q].titolo, link: quiz[q].link });
    isc.forEach(function (s, i) { dati[i].push(fatti[i] ? 'FATTO' : 'MANCA'); });
  }
  if (nonAbb) avvisi.push(nonAbb + ' risposte ai quiz di oggi con email non abbinata (non contate)');
  if (!compiti.length) avvisi.push('nessun compito «GG/MM Ora N» di oggi pubblicato su Classroom');
  if (!quiz.length) avvisi.push('nessun quiz di oggi trovato');
  LV_scrivi_(ss, classe, { dato: new Date(t0),   /* ora di INIZIO del giro: tutto cio che e scritto e stato letto dopo questo istante, quindi il dato e fresco almeno quanto dichiarato */ giorno: giorno, stato: stato, motivo: motivo, durata: Math.round((Date.now() - t0) / 1000), nonAbb: nonAbb, avvisi: avvisi, colonne: colonne, nomi: etich, dati: dati, ultimo: ultimo });
}

/* ---------- la scheda «Live <CLASSE>» ---------- */
function LV_scheda_(ss, classe) { return ss.getSheetByName('Live ' + classe) || ss.insertSheet('Live ' + classe); }
function LV_scrivi_(ss, classe, o) {
  var sh = LV_scheda_(ss, classe), nc = o.colonne.length, larg = Math.max(3, nc + 2), righe = [], i, j;
  function riga(a, b, c) { var r = [a, b, c || '']; while (r.length < larg) r.push(''); return r; }
  righe.push(riga('Live ' + classe, LV_iso_(o.dato), 'dati letti alle ' + LV_roma_(o.dato, 'HH:mm:ss')));
  righe.push(riga('lezione', o.giorno));
  righe.push(riga('stato', o.stato, o.motivo));
  righe.push(riga('durata_s', o.durata));
  righe.push(riga('non_abbinate', o.nonAbb));
  righe.push(riga('versione', LV_VERSIONE, o.avvisi.join(' | ')));
  righe.push(riga('lavori', JSON.stringify(o.colonne)));
  var testa = ['Allievo'];
  o.colonne.forEach(function (c) { testa.push((c.k === 'C' ? 'C|' : 'Q|') + c.titolo); });
  testa.push('ULTIMO'); while (testa.length < larg) testa.push('');
  righe.push(testa);
  for (i = 0; i < o.nomi.length; i++) {
    var r = [o.nomi[i]];
    for (j = 0; j < nc; j++) r.push(o.dati[i][j]);
    r.push(o.ultimo[i]); while (r.length < larg) r.push('');
    righe.push(r);
  }
  sh.clearContents();
  var rg = sh.getRange(1, 1, righe.length, larg);
  rg.setNumberFormat('@');             // tutto testo: l'ora ISO non deve diventare una data
  rg.setValues(righe);
  SpreadsheetApp.flush();
}
function LV_scriviErrore_(ss, classe, msg) {   // non cancella i dati vecchi: cambia solo lo stato (l'ora del dato resta quella vecchia)
  var sh = LV_scheda_(ss, classe);
  if (sh.getLastRow() < 3) {
    sh.getRange(1, 1, 3, 3).setNumberFormat('@').setValues([['Live ' + classe, '', ''], ['lezione', LV_roma_(new Date(), 'yyyy-MM-dd'), ''], ['stato', 'non_letto', String(msg).slice(0, 300)]]);
  } else {
    sh.getRange(3, 1, 1, 3).setNumberFormat('@').setValues([['stato', 'non_letto', String(msg).slice(0, 300)]]);
  }
}

/* ---------- il job ---------- */
function LV_classiDaFare_(ss) {
  var p = PropertiesService.getScriptProperties().getProperty('LV_CLASSI');
  var lista = p ? String(p).split(/[\s,;]+/).map(function (x) { return x.toUpperCase(); }).filter(function (x) { return LV_CLASSI_TUTTE.indexOf(x) >= 0; }) : LV_CLASSI_TUTTE.slice();
  var eta = {};
  lista.forEach(function (c) { var sh = ss.getSheetByName('Live ' + c); eta[c] = sh && sh.getLastRow() >= 1 ? String(sh.getRange(1, 2).getValue() || '') : ''; });
  lista.sort(function (a, b) { return eta[a] < eta[b] ? -1 : (eta[a] > eta[b] ? 1 : 0); });   // prima il dato piu vecchio (ISO si ordina come testo)
  return lista;
}
function LV_inOrario_() {
  var n = new Date(), g = Number(LV_roma_(n, 'u')), hm = LV_roma_(n, 'HH:mm');   // u: 1 = lunedi ... 7 = domenica
  return g >= 1 && g <= 5 && hm >= '07:45' && hm <= '14:20';
}
function LV_esegui_(forza) {
  var t0 = Date.now(), lock = LockService.getUserLock();
  if (!lock.tryLock(2000)) { Logger.log('live: un altro giro e in corso, salto'); return; }
  try {
    if (!forza && !LV_inOrario_()) return;
    var ss = LV_foglio_(), classi = LV_classiDaFare_(ss);
    for (var i = 0; i < classi.length; i++) {
      if (Date.now() - t0 > LV_AVVIO_MAX_MS) { Logger.log('live: saltate per il tempo ' + classi.slice(i).join(', ')); break; }
      try { LV_classe_(ss, classi[i], t0); }
      catch (e) { Logger.log('live ' + classi[i] + ': ' + e); try { LV_scriviErrore_(ss, classi[i], String(e.message || e).slice(0, 200)); } catch (e2) { } }
      Logger.log('live ' + classi[i] + ' fatto dopo ' + Math.round((Date.now() - t0) / 1000) + ' s');
    }
  } finally { lock.releaseLock(); }
}
/** Funzione del trigger a tempo (ogni minuto). */
function live_giro() { LV_esegui_(false); }
/** Prova a mano, fuori orario: legge, scrive la scheda Live e nel log (Visualizza, Log di esecuzione) c'e la durata. */
function live_prova() { LV_esegui_(true); }
/** Si lancia UNA volta: crea il trigger a tempo ogni minuto per live_giro (toglie quelli vecchi). */
function live_installa() {
  live_spegni();
  ScriptApp.newTrigger('live_giro').timeBased().everyMinutes(1).create();
  Logger.log('CRUSCOTTO LIVE ATTIVO: live_giro ogni minuto, lun-ven 07:45-14:20.');
}
function live_spegni() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'live_giro') ScriptApp.deleteTrigger(t); });
}

/* ---------- WEB APP ---------- */
function LV_pulisciNome_(s, k) {
  s = String(s || '').trim();
  if (/@/.test(s) || !/^[^\s\d@]+( [^\s\d@]+)* [A-ZÀ-Ý][a-zà-ÿ]{0,3}\.( \(\d+\))?$/.test(s)) return 'Allievo ' + (k + 1);
  return s;
}
function LV_leggi_(classe) {
  var ss = LV_foglio_(), sh = ss.getSheetByName('Live ' + classe), adesso = new Date();
  var base = { versione: LV_VERSIONE, classe: classe, generato_il: LV_iso_(adesso), dato_il: null, secondi_dal_dato: null, lezione: null, stato: 'non_letto', non_letto: null, criticita: [], lavori: { compiti: [], quiz: [] }, allievi: [] };
  if (!sh || sh.getLastRow() < 3) { base.non_letto = 'scheda Live ' + classe + ' non ancora scritta dal job'; base.criticita.push(base.non_letto); return base; }
  var v = sh.getDataRange().getDisplayValues(), i, j;
  var iso = String(v[0][1] || '');
  var ms = Date.parse(iso);
  base.dato_il = iso || null;
  base.secondi_dal_dato = isNaN(ms) ? null : Math.max(0, Math.round((adesso.getTime() - ms) / 1000));
  base.lezione = String(v[1][1] || '') || null;
  base.stato = String(v[2][1] || 'non_letto');
  var motivo = String(v[2][2] || '');
  if (base.stato !== 'ok') { base.non_letto = motivo || base.stato; base.criticita.push((base.stato === 'parziale' ? 'Dato parziale: ' : 'Dato non letto: ') + (motivo || base.stato)); }
  var durata = Number(v[3] && v[3][1]), nonAbb = Number(v[4] && v[4][1]);
  base.durata_job_s = isNaN(durata) ? null : durata;
  if (nonAbb > 0) base.criticita.push(nonAbb + ' risposte ai quiz di oggi con email non abbinata (non contate)');
  var avv = String((v[5] && v[5][2]) || ''); if (avv) avv.split(' | ').forEach(function (a) { if (a && a.indexOf('email non abbinata') < 0) base.criticita.push(a); });
  var meta = []; try { meta = JSON.parse(String((v[6] && v[6][1]) || '[]')); } catch (e) { meta = []; }
  meta.forEach(function (m) { if (m.k === 'C') base.lavori.compiti.push({ titolo: m.titolo, link: m.link || '', ora: m.ora }); else base.lavori.quiz.push({ id: m.id, titolo: m.titolo, link: m.link || '' }); });
  for (i = LV_META; i < v.length; i++) {
    var nome = LV_pulisciNome_(v[i][0], i - LV_META);
    if (!String(v[i][0] || '').trim()) continue;
    var al = { nome: nome, compiti: [], quiz: [], ultimo: null };
    for (j = 0; j < meta.length; j++) {
      var cella = String(v[i][1 + j] || '');
      if (meta[j].k === 'C') al.compiti.push({ titolo: meta[j].titolo, stato: cella });
      else al.quiz.push({ id: meta[j].id, fatto: cella === 'FATTO' });
    }
    var u = String(v[i][1 + meta.length] || ''); al.ultimo = u && !isNaN(Date.parse(u)) ? u : null;
    base.allievi.push(al);
  }
  return base;
}
function doGet(e) {
  var p = (e && e.parameter) || {}, classe = String(p.classe || '').toUpperCase(), out;
  if (LV_CLASSI_TUTTE.indexOf(classe) < 0) out = { versione: LV_VERSIONE, errore: 'parametro classe mancante o sconosciuto (1inf, 2inf, 3inf, 4ti)', allievi: [], criticita: [] };
  else { try { out = LV_leggi_(classe); } catch (x) { out = { versione: LV_VERSIONE, classe: classe, generato_il: LV_iso_(new Date()), stato: 'non_letto', non_letto: 'errore del web app: ' + String(x.message || x).slice(0, 150), allievi: [], criticita: ['errore del web app'] }; } }
  var testo = JSON.stringify(out), cb = String(p.callback || '');
  if (/^[A-Za-z_][A-Za-z0-9_.]{0,40}$/.test(cb)) return ContentService.createTextOutput(cb + '(' + testo + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
  return ContentService.createTextOutput(testo).setMimeType(ContentService.MimeType.JSON);
}
/** Prova a mano del web app: scrive nel log il JSON della 1INF (solo Nome I.). */
function live_provaWeb() { Logger.log(JSON.stringify(LV_leggi_('1INF')).slice(0, 3000)); }
