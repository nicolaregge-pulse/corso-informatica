/*
 * classroom_pubblica v1.0 — 23/11/2026 — PUBBLICO (nessun nome di allievo, nessuna password)
 * PROTOTIPO NON ATTIVATO, NON COLLEGATO A fabbrica/motore.js. Progetto: PUBBLICAZIONE-AUTOMATICA-PROGETTO-v1.0.md (riservato).
 *
 * Scopo: dopo il comando «PUBB n» (R2 di CLAUDE.md) creare su Classroom il compito di UNA ora e pubblicarlo, con prova letta da Classroom.
 *
 * Come funziona (in breve):
 *  - In git: fabbrica/post/<id>.json (la specifica del post) e fabbrica/post/coda.json (le richieste). Il comando PUBB n aggiunge UNA richiesta.
 *  - Questo file e' caricato come il motore: nel lancio una funzione pubb_ciclo() fa eval() del file e chiama PB_main_(); trigger a parte, ogni minuto.
 *  - Per ogni richiesta: controlli, anti-doppione, allegati (PDF, copia del Documento, link Moduli), compito creato in BOZZA, riletto da Classroom
 *    (titolo, testo identico, allegati, nessuna scadenza), solo allora patch a PUBLISHED e seconda lettura. Una sola «pubblica» per giro.
 *  - Esito nella scheda «Pubblicazioni» del foglio Fabbrica. Se qualcosa non va: stato NON_RIUSCITO e il motivo (la riga «PUBB n NON riuscito: pubblica a mano» la scrive Claude).
 *
 * Interruttori (Proprieta dello script): PB_STOP=1 ferma tutto · PB_ABILITA_REALE=1 permette i corsi veri (senza: solo corso di prova e solo bozza)
 *   PB_CORSO_PROVA = nome del corso di prova · PB_SEMPRE=1 ignora la fascia oraria · «attivo»:false nella coda spegne da git.
 *
 * Regole rispettate: R2 (solo su richiesta, una ora per volta, titolo «G/M Ora N: ...», senza scadenza, senza punti), R1 (nessun nome), R6 (avviso lingue).
 * Limiti di Classroom (dalla conoscenza dell'API, NON riletti dalla documentazione oggi): il progetto che ha creato un compito e' l'unico che lo puo modificare;
 * un compito PUBLISHED non torna in bozza (si cancella a mano). Tutto cio che tocca Classroom vero e' NON PROVATO: vedi il progetto, capitolo 2.
 * Permessi OAuth necessari in piu rispetto alla sola lettura: classroom.coursework.students (NON la versione .readonly) e drive (per creare il PDF e copiare il Documento).
 */
var PB_VERSIONE_ = '1.0';
var PB_TZ_ = 'Europe/Rome';
var PB_CLASSI_ = ['1INF', '2INF', '3INF', '4TI'];
var PB_BASE_ = (typeof FB_BASE !== 'undefined') ? FB_BASE : 'https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/fabbrica/';
var PB_MAX_TENTATIVI_ = 3;
var PB_BUDGET_MS_ = 50000;

/* ---------- utilita ---------- */
function PB_p_() { return PropertiesService.getScriptProperties(); }
function PB_json_(k) { try { return JSON.parse(PB_p_().getProperty(k) || '{}') || {}; } catch (e) { return {}; } }
function PB_salva_(k, v) { PB_p_().setProperty(k, JSON.stringify(v)); }
function PB_ora_(f) { return Utilities.formatDate(new Date(), PB_TZ_, f || 'dd/MM HH:mm:ss'); }
function PB_oggi_() { return PB_ora_('yyyy-MM-dd'); }
function PB_norm_(t) { return String(t || '').toLowerCase().replace(/\s+/g, ' ').trim(); }
function PB_testo_(t) { return String(t || '').replace(/\r\n/g, '\n').replace(/[ \t]+\n/g, '\n').trim(); }
function PB_hash_(s) { var h = 0x811c9dc5, i; s = String(s); for (i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = (h * 0x01000193) >>> 0; } return h.toString(16) + '-' + s.length; }
function PB_errore_(e) { return e && e.message ? e.message : String(e); }
function PB_transitorio_(msg) { return /\b50\d\b|too many times|timeout|timed out|temporar|rate limit|backend error|address unavailable|try again|quota/i.test(msg); }
function PB_conRetry_(fn) {
  var n = 0, e;
  for (;;) {
    try { return fn(); } catch (x) {
      e = x; n++;
      if (n >= 3 || !PB_transitorio_(PB_errore_(x))) throw e;
      Utilities.sleep(700 * n);
    }
  }
}
function PB_get_(percorso) {
  var r = PB_conRetry_(function () { return UrlFetchApp.fetch(PB_BASE_ + percorso + '?t=' + Date.now(), { muteHttpExceptions: true }); });
  if (r.getResponseCode() !== 200) throw new Error('HTTP ' + r.getResponseCode() + ' leggendo ' + percorso);
  return r;
}
function PB_leggiJson_(percorso) { return JSON.parse(PB_get_(percorso).getContentText('UTF-8')); }

/* ---------- logica pura (provata con node, servizi finti) ---------- */
function PB_prefisso_(giorno, ora) { var p = String(giorno).split('-'); return Number(p[2]) + '/' + Number(p[1]) + ' Ora ' + ora + ': '; }

/* Controlla una specifica. Ritorna {err:[], avv:[]}: err blocca, avv e' solo un avviso (R6). */
function PB_valida_(s, req) {
  var err = [], avv = [], i, a;
  if (!s || typeof s !== 'object') return { err: ['specifica non leggibile'], avv: [] };
  if (!/^[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9A-Za-z]+_ora[1-6][0-9A-Za-z\-]*$/.test(String(s.id || ''))) err.push('id non nel formato AAAA-MM-GG_CLASSE_oraN');
  if (PB_CLASSI_.indexOf(s.classe) < 0) err.push('classe non valida: ' + s.classe);
  if (!/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(String(s.giorno || ''))) err.push('giorno non valido');
  if (!(s.ora >= 1 && s.ora <= 6 && s.ora === Math.floor(s.ora))) err.push('ora non da 1 a 6');
  if (s.id && s.classe && s.giorno && s.ora && String(s.id).indexOf(s.giorno + '_' + s.classe + '_ora' + s.ora) !== 0) err.push('id, giorno, classe e ora non coincidono');
  var t = String(s.titolo || '');
  if (s.giorno && s.ora && t.indexOf(PB_prefisso_(s.giorno, s.ora)) !== 0) err.push('titolo non inizia con «' + PB_prefisso_(s.giorno, s.ora) + '»');
  else if (t.length < 14 || t.length > 90 || /\s{2,}/.test(t) || t !== t.trim()) err.push('titolo troppo corto/lungo o con spazi doppi');
  var d = String(s.descrizione || '');
  if (!d.trim()) err.push('testo vuoto');
  if (d.length > 29000) err.push('testo oltre 29000 caratteri');
  if (/�|\?\?\?\?/.test(d)) err.push('nel testo ci sono «????» o caratteri rotti (arabo/cinese perduti)');
  ['scadenza_iso', 'scadenza', 'punti', 'maxPoints', 'dueDate', 'programma_iso'].forEach(function (k) { if (s[k] !== undefined && s[k] !== null && s[k] !== '') err.push('il campo «' + k + '» non e ammesso (compito senza scadenza e senza punti)'); });
  if (s.classe && s.classe !== '1INF' && /[؀-ۿ一-鿿]/.test(d)) avv.push('arabo o cinese in ' + s.classe + ' (R6: solo la 1INF)');
  var al = s.allegati || [];
  if (!Array.isArray(al) || al.length > 8) err.push('allegati: elenco con al massimo 8 voci');
  else al.forEach(function (x, n) {
    a = 'allegato ' + (n + 1) + ': ';
    if (!x || ['pdf', 'documento', 'quiz', 'link'].indexOf(x.tipo) < 0) { err.push(a + 'tipo non previsto'); return; }
    if (x.tipo === 'pdf' && !/^post\/[0-9A-Za-z_\-\.\/]+\.pdf$/.test(String(x.file || ''))) err.push(a + 'pdf: percorso non valido');
    if (x.tipo === 'pdf' && !String(x.nome || '').trim()) err.push(a + 'pdf: manca il nome');
    if (x.tipo === 'documento' && !/^[0-9A-Za-z_\-]{20,}$/.test(String(x.modello_id || ''))) err.push(a + 'documento: modello_id non valido');
    if (x.tipo === 'documento' && !String(x.nome || '').trim()) err.push(a + 'documento: manca il nome');
    if (x.tipo === 'quiz' && !/^[0-9A-Za-z_\-]+$/.test(String(x.id || ''))) err.push(a + 'quiz: id non valido');
    if (x.tipo === 'link' && !/^https:\/\/[^\s]+$/.test(String(x.url || ''))) err.push(a + 'link: serve un indirizzo https');
  });
  if (req) {
    if (['bozza', 'pubblica'].indexOf(req.azione) < 0) err.push('azione non prevista: ' + req.azione);
    if (req.azione === 'pubblica' && Number(req.pubb) !== Number(s.ora)) err.push('PUBB ' + req.pubb + ' non coincide con l\'ora ' + s.ora + ' del post: una ora per volta');
    if (req.giorno && s.giorno && req.giorno !== s.giorno) err.push('giorno della richiesta diverso da quello del post');
  }
  return { err: err, avv: avv };
}

function PB_impronta_(s) { return PB_hash_(JSON.stringify([s.titolo, s.descrizione, s.allegati || []])); }
function PB_impArralleg_(s) { return PB_hash_(JSON.stringify(s.allegati || [])); }

/* Stessa ora del giorno? fascia lun-ven 07:00-15:30 (la lezione e 8-14, la firma alle 14:05) */
function PB_inOrario_() {
  if (PB_p_().getProperty('PB_SEMPRE') === '1') return true;
  var g = Number(PB_ora_('u')), hm = Number(PB_ora_('HHmm'));
  return g >= 1 && g <= 5 && hm >= 700 && hm <= 1530;
}

/* Confronto del compito riletto da Classroom con la specifica. Ritorna elenco di differenze (vuoto = identico). */
function PB_differenze_(cw, s, nMateriali, atteso) {
  var d = [];
  if (!cw) return ['compito non letto'];
  if (cw.title !== s.titolo) d.push('titolo diverso');
  if (PB_testo_(cw.description) !== PB_testo_(s.descrizione)) d.push('testo diverso');
  if ((cw.materials || []).length !== nMateriali) d.push('allegati: ' + (cw.materials || []).length + ' invece di ' + nMateriali);
  if (cw.dueDate || cw.dueTime) d.push('ha una scadenza');
  if (cw.maxPoints) d.push('ha dei punti');
  if (atteso && cw.state !== atteso) d.push('stato ' + cw.state + ' invece di ' + atteso);
  return d;
}

/* ---------- Classroom e Drive (con servizi veri o finti) ---------- */
function PB_corsi_() {
  var out = [], tok;
  do {
    var r = PB_conRetry_(function () { return Classroom.Courses.list({ courseStates: ['ACTIVE'], pageSize: 100, pageToken: tok || undefined }); });
    (r.courses || []).forEach(function (c) { out.push(c); });
    tok = r.nextPageToken;
  } while (tok);
  return out;
}
function PB_nomeCorso_(classe, prova, indice) {
  if (prova) return PB_p_().getProperty('PB_CORSO_PROVA') || '';
  var m = indice && indice.classroom && indice.classroom.classi ? indice.classroom.classi[classe] : '';
  return m || '';
}
function PB_corso_(classe, prova, indice) {
  var nomi = PB_nomeCorso_(classe, prova, indice);
  if (!nomi) throw new Error(prova ? 'manca la proprieta PB_CORSO_PROVA' : 'in indice.json classroom.classi manca il corso di ' + classe);
  nomi = [].concat(nomi).map(PB_norm_);
  var trovati = PB_corsi_().filter(function (c) { return nomi.indexOf(PB_norm_(c.name)) >= 0; });
  if (trovati.length !== 1) throw new Error('corso «' + nomi.join('/') + '»: trovati ' + trovati.length + ' (ne serve uno)');
  return trovati[0];
}
function PB_cercaDoppione_(corsoId, titolo) {
  var tok, n = PB_norm_(titolo);
  do {
    var r = PB_conRetry_(function () { return Classroom.Courses.CourseWork.list(corsoId, { courseWorkStates: ['PUBLISHED', 'DRAFT'], pageSize: 100, pageToken: tok || undefined }); });
    var l = r.courseWork || [], i;
    for (i = 0; i < l.length; i++) if (PB_norm_(l[i].title) === n) return l[i];
    tok = r.nextPageToken;
  } while (tok);
  return null;
}
function PB_cartella_(nome) { var it = DriveApp.getFoldersByName(nome); return it.hasNext() ? it.next() : DriveApp.createFolder(nome); }

function PB_linkQuiz_(id) {
  var ss = SpreadsheetApp.openById(PB_p_().getProperty('FB_FOGLIO')), sh = ss.getSheetByName('Esiti');
  if (!sh) throw new Error('scheda Esiti non trovata');
  var v = sh.getDataRange().getValues(), i, u = '';
  for (i = v.length - 1; i >= 1; i--) if (String(v[i][1]) === id) { u = String(v[i][3] || ''); break; }
  if (!/^https:\/\/docs\.google\.com\/forms\/.+\/viewform/.test(u)) throw new Error('quiz «' + id + '»: link ragazzi non trovato in Esiti (colonna D)');
  return u;
}

/* Costruisce l'elenco allegati. Ritorna {materiali, creati}. creati = id Drive creati (per la pulizia se serve). */
function PB_materiali_(s) {
  var mat = [], creati = [], cart = null;
  (s.allegati || []).forEach(function (x) {
    if (x.tipo === 'link') { mat.push({ link: { url: x.url } }); return; }
    if (x.tipo === 'quiz') { mat.push({ link: { url: PB_linkQuiz_(x.id) } }); return; }
    if (!cart) cart = PB_cartella_('PUBB ' + s.classe + ' ' + s.giorno);
    if (x.tipo === 'pdf') {
      var r = PB_get_(x.file), b = r.getBlob();
      var by = b.getBytes();
      if (by.length < 100 || by.length > 20 * 1024 * 1024) throw new Error('pdf ' + x.file + ': dimensione non plausibile (' + by.length + ' byte)');
      if (String.fromCharCode(by[0], by[1], by[2], by[3]) !== '%PDF') throw new Error('pdf ' + x.file + ': non e un PDF');
      var f = cart.createFile(b.setName(x.nome));
      creati.push(f.getId());
      mat.push({ driveFile: { driveFile: { id: f.getId() }, shareMode: 'VIEW' } });
    } else if (x.tipo === 'documento') {
      var c = DriveApp.getFileById(x.modello_id).makeCopy(x.nome, cart);
      creati.push(c.getId());
      mat.push({ driveFile: { driveFile: { id: c.getId() }, shareMode: 'STUDENT_COPY' } });
    }
  });
  return { materiali: mat, creati: creati };
}

function PB_registra_(es, spec) {
  try {
    var id = PB_p_().getProperty('FB_FOGLIO');
    if (!id) return;
    var ss = SpreadsheetApp.openById(id), sh = ss.getSheetByName('Pubblicazioni');
    if (!sh) {
      sh = ss.insertSheet('Pubblicazioni');
      sh.getRange(3, 1, 1, 12).setValues([['Ora esito', 'Post', 'Classe', 'Azione', 'PUBB', 'Esito', 'Stato letto da Classroom', 'Titolo', 'Allegati', 'Link', 'Motivo', 'Avvisi']]).setFontWeight('bold');
    }
    sh.appendRow([PB_ora_(), es.id, spec ? spec.classe : '', es.azione, es.pubb || '', es.stato, es.letto || '', spec ? spec.titolo : '', spec ? (spec.allegati || []).length : '', es.link || '', es.motivo || '', (es.avvisi || []).join('; ')]);
  } catch (e) { /* la registrazione non deve mai bloccare l'esito */ }
}
function PB_battito_(nota) {
  try {
    var id = PB_p_().getProperty('FB_FOGLIO');
    if (!id) return;
    var ss = SpreadsheetApp.openById(id), sh = ss.getSheetByName('Pubblicazioni');
    if (sh) sh.getRange(1, 1, 1, 3).setValues([['Ultimo giro PUBB', PB_ora_(), 'v' + PB_VERSIONE_ + ' ' + (nota || '')]]);
  } catch (e) { }
}

/* Elabora UNA richiesta. Ritorna l'esito {stato: PUBBLICATO|BOZZA_PRONTA|GIA_PUBBLICATO|NON_RIUSCITO, motivo, link, ...}; puo lanciare (errore transitorio). */
function PB_elabora_(req, indice) {
  var es = { id: req.post, azione: req.azione, pubb: req.pubb || null, stato: '', motivo: '', link: '', cwId: '', letto: '', avvisi: [] };
  var spec = PB_leggiJson_('post/' + req.post + '.json');
  var v = PB_valida_(spec, req);
  es.avvisi = v.avv;
  if (v.err.length) { es.stato = 'NON_RIUSCITO'; es.motivo = 'controllo: ' + v.err.join('; '); es.spec = spec; return es; }
  es.spec = spec;
  var azione = req.azione;
  if (!req.prova && PB_p_().getProperty('PB_ABILITA_REALE') !== '1') {
    if (azione === 'pubblica') { azione = 'bozza'; es.avvisi.push('PB_ABILITA_REALE spento: solo bozza, la pubblica il docente con un clic'); }
  }
  var corso = PB_corso_(spec.classe, !!req.prova, indice);
  var mem = PB_json_('PB_POST'), m = mem[spec.id] || null, cw = null;
  if (m && m.cwId && m.corso === corso.id) {
    try { cw = PB_conRetry_(function () { return Classroom.Courses.CourseWork.get(corso.id, m.cwId); }); } catch (e) { if (!/404|not found/i.test(PB_errore_(e))) throw e; cw = null; m = null; }
  } else m = null;
  if (cw && cw.state === 'DELETED') { cw = null; m = null; }
  if (!cw) {
    var dup = PB_cercaDoppione_(corso.id, spec.titolo);
    if (dup) {
      es.stato = 'NON_RIUSCITO'; es.link = dup.alternateLink || ''; es.cwId = dup.id;
      es.motivo = 'esiste gia un compito con questo titolo (' + dup.state + ') che non e del motore: non lo tocco (il progetto che lo ha creato e l\'unico che lo puo modificare). Si completa a mano.';
      return es;
    }
  }
  var imp = PB_impronta_(spec), impA = PB_impArralleg_(spec), nMat = (spec.allegati || []).length;
  if (cw && cw.state === 'PUBLISHED') {
    es.stato = 'GIA_PUBBLICATO'; es.link = cw.alternateLink || ''; es.cwId = cw.id; es.letto = 'PUBLISHED';
    es.motivo = m && m.imp !== imp ? 'il post e gia pubblicato: la specifica e cambiata dopo, NON ho modificato nulla (modifica a mano)' : 'gia pubblicato dal motore';
    return es;
  }
  if (cw && cw.state === 'DRAFT' && m.imp !== imp) {
    if (m.impA === impA) {
      cw = PB_conRetry_(function () { return Classroom.Courses.CourseWork.patch({ title: spec.titolo, description: spec.descrizione }, corso.id, cw.id, { updateMask: 'title,description' }); });
      m.imp = imp; mem[spec.id] = m; PB_salva_('PB_POST', mem);
    } else {   /* allegati cambiati: la bozza si butta (mai un compito pubblicato) e si rifa */
      PB_conRetry_(function () { return Classroom.Courses.CourseWork.remove(corso.id, cw.id); });
      delete mem[spec.id]; PB_salva_('PB_POST', mem); cw = null; m = null;
    }
  }
  if (!cw) {
    var mt = PB_materiali_(spec);
    nMat = mt.materiali.length;
    cw = PB_conRetry_(function () { return Classroom.Courses.CourseWork.create({ title: spec.titolo, description: spec.descrizione, workType: 'ASSIGNMENT', state: 'DRAFT', materials: mt.materiali }, corso.id); });
    mem[spec.id] = { cwId: cw.id, corso: corso.id, imp: imp, impA: impA, creato: PB_ora_(), drive: mt.creati };
    PB_salva_('PB_POST', mem);
  }
  es.cwId = cw.id; es.link = cw.alternateLink || '';
  var l1 = PB_conRetry_(function () { return Classroom.Courses.CourseWork.get(corso.id, cw.id); });
  var dif = PB_differenze_(l1, spec, nMat, 'DRAFT');
  if (dif.length) { es.stato = 'NON_RIUSCITO'; es.letto = 'DRAFT'; es.motivo = 'la bozza riletta da Classroom non coincide (' + dif.join(', ') + '): NON pubblicata'; return es; }
  if (azione === 'bozza') { es.stato = 'BOZZA_PRONTA'; es.letto = 'DRAFT'; es.motivo = req.azione === 'pubblica' ? 'bozza pronta, da pubblicare con un clic (interruttore reale spento)' : ''; return es; }
  PB_conRetry_(function () { return Classroom.Courses.CourseWork.patch({ state: 'PUBLISHED' }, corso.id, cw.id, { updateMask: 'state' }); });
  var l2 = PB_conRetry_(function () { return Classroom.Courses.CourseWork.get(corso.id, cw.id); });
  var dif2 = PB_differenze_(l2, spec, nMat, 'PUBLISHED');
  es.letto = l2.state; es.link = l2.alternateLink || es.link;
  if (dif2.length) { es.stato = 'NON_RIUSCITO'; es.motivo = 'dopo la pubblicazione Classroom dice: ' + dif2.join(', '); return es; }
  es.stato = 'PUBBLICATO'; es.letto = 'PUBLISHED alle ' + PB_ora_('HH:mm:ss');
  return es;
}

function PB_chiave_(r) { return r.post + ':' + r.azione + ':' + (r.richiesta || ''); }   /* una nuova richiesta (nuovo «richiesta») permette di riprovare dopo un NON_RIUSCITO */

/* Giro: legge la coda, elabora al massimo UNA «pubblica» e fino a 2 «bozza». Ritorna un riassunto (per i test e per il log). */
function PB_main_() {
  var lock = LockService.getUserLock();   /* il motore usa getScriptLock: i due non si bloccano a vicenda */
  if (!lock.tryLock(5000)) return { saltato: 'lock' };
  var t0 = Date.now(), fatti, riass = { fatte: [], saltato: '' };
  try {
    if (PB_p_().getProperty('PB_STOP') === '1') { riass.saltato = 'PB_STOP'; return riass; }
    if (!PB_inOrario_()) { riass.saltato = 'fuori orario'; return riass; }
    var coda = PB_leggiJson_('post/coda.json');
    var indice = {}; try { indice = PB_leggiJson_('indice.json'); } catch (e0) { indice = {}; }
    PB_battito_('letta la coda');
    if (!coda || coda.attivo !== true) { riass.saltato = 'coda spenta'; return riass; }
    fatti = PB_json_('PB_FATTI');
    var oggi = PB_oggi_(), npub = 0, nboz = 0;
    var todo = (coda.richieste || []).filter(function (r) { return r && r.post && ['bozza', 'pubblica'].indexOf(r.azione) >= 0; })
      .sort(function (a, b) { return (a.azione === 'pubblica' ? 0 : 1) - (b.azione === 'pubblica' ? 0 : 1) || (a.pubb || 0) - (b.pubb || 0); });
    todo.forEach(function (r) {
      var k = PB_chiave_(r), f = fatti[k];
      if (Date.now() - t0 > PB_BUDGET_MS_) return;
      if (f && f.finale) return;
      if (r.giorno && r.giorno > oggi && r.azione === 'pubblica') return;   /* non e ancora il giorno */
      if (r.azione === 'pubblica' && r.giorno && r.giorno < oggi) { fatti[k] = { finale: true, stato: 'SCADUTA', ts: PB_ora_(), tms: Date.now() }; riass.fatte.push({ id: r.post, stato: 'SCADUTA' }); return; }
      if (r.azione === 'pubblica') { if (npub >= 1) return; npub++; } else { if (nboz >= 2) return; nboz++; }
      var es, tent = ((f && f.tent) || 0) + 1;
      try { es = PB_elabora_(r, indice); }
      catch (e) {
        var msg = PB_errore_(e);
        if (PB_transitorio_(msg) && tent < PB_MAX_TENTATIVI_) { fatti[k] = { tent: tent, ts: PB_ora_(), ultimo: msg.slice(0, 150) }; riass.fatte.push({ id: r.post, stato: 'RIPROVO', motivo: msg }); return; }
        es = { id: r.post, azione: r.azione, pubb: r.pubb || null, stato: 'NON_RIUSCITO', motivo: msg + (PB_transitorio_(msg) ? ' (dopo ' + tent + ' tentativi)' : ''), avvisi: [] };
      }
      fatti[k] = { finale: true, stato: es.stato, ts: PB_ora_(), tms: Date.now(), link: es.link || '' };
      PB_registra_(es, es.spec);
      delete es.spec;
      riass.fatte.push(es);
    });
    var tagli = Date.now() - 3 * 86400000;
    Object.keys(fatti).forEach(function (k) { if (fatti[k].finale && fatti[k].tms && fatti[k].tms < tagli) delete fatti[k]; });
    PB_salva_('PB_FATTI', fatti);
    return riass;
  } finally { lock.releaseLock(); }
}

/* Per il lancio (UNA volta, dal docente, DOPO le prove): trigger separato ogni minuto. NON attivato da questo file. */
function PB_installaTrigger_() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'pubb_ciclo') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('pubb_ciclo').timeBased().everyMinutes(1).create();
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PB_valida_: PB_valida_, PB_differenze_: PB_differenze_, PB_main_: PB_main_, PB_elabora_: PB_elabora_, PB_prefisso_: PB_prefisso_, PB_hash_: PB_hash_, PB_inOrario_: PB_inOrario_ };
}
