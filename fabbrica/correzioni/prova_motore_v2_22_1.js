// Prova locale del motore v2.22.1 (schede 'Risposte <id>' e 'Documenti <CLASSE>'). NOMI INVENTATI. Servizi Google FINTI (non e Google):
// prova la LOGICA del codice, non le API vere (permessi, forme esatte delle risposte di Classroom e di Moduli: non provato).
// Uso: node fabbrica/correzioni/prova_motore_v2_22.js   (dalla radice del repository)
var fs = require('fs'), vm = require('vm'), path = require('path');
var fail = [];
function check(c, m) { if (!c) fail.push(m); }

/* ---- foglio finto ---- */
function Sheet(nome, id) {
  var self = this, cells = {}, nascosta = false;
  this.name = nome; this.id = id;
  function rng(r, c, nr, nc) {
    nr = nr || 1; nc = nc || 1;
    var o = {
      setValues: function (v) { for (var i = 0; i < v.length; i++) for (var j = 0; j < v[i].length; j++) cells[(r + i) + ',' + (c + j)] = v[i][j]; return o; },
      getValue: function () { var x = cells[r + ',' + c]; return x === undefined ? '' : x; },
      setValue: function (x) { cells[r + ',' + c] = x; return o; },
      getValues: function () { var out = []; for (var i = 0; i < nr; i++) { var row = []; for (var j = 0; j < nc; j++) { var x = cells[(r + i) + ',' + (c + j)]; row.push(x === undefined ? '' : x); } out.push(row); } return out; }
    };
    ['setFontWeight', 'setBackground', 'setWrap', 'setFontStyle', 'setFontColor', 'setNumberFormat'].forEach(function (m) { o[m] = function () { return o; }; });
    return o;
  }
  this.getRange = rng;
  this.getDataRange = function () {
    var mr = 0, mc = 0; Object.keys(cells).forEach(function (k) { var p = k.split(','); mr = Math.max(mr, +p[0]); mc = Math.max(mc, +p[1]); });
    return rng(1, 1, mr, mc);
  };
  this.clear = function () { cells = {}; };
  this.setFrozenRows = this.setFrozenColumns = this.setTabColor = function () { };
  this.getSheetId = function () { return id; };
  this.getName = function () { return nome; };
  this.isSheetHidden = function () { return nascosta; };
  this.rows = function () { var d = self.getDataRange().getValues(); return d; };
}
function Foglio() {
  var sh = {}, n = 1;
  this.getSheetByName = function (x) { return sh[x] || null; };
  this.insertSheet = function (x) { sh[x] = new Sheet(x, n++); return sh[x]; };
  this.getSheets = function () { return Object.keys(sh).map(function (k) { return sh[k]; }); };
  this.getId = function () { return 'FOGLIO'; };
}
/* ---- formattazione data: Roma = UTC+1 (novembre) ---- */
function pad(x) { return ('0' + x).slice(-2); }
var Utilities = { formatDate: function (d, tz, f) {
  var t = new Date(d.getTime() + 3600000), Y = t.getUTCFullYear(), M = pad(t.getUTCMonth() + 1), D = pad(t.getUTCDate()), h = pad(t.getUTCHours()), m = pad(t.getUTCMinutes()), s = pad(t.getUTCSeconds());
  return f.replace('yyyy', Y).replace('dd', D).replace('MM', M).replace('HH', h).replace('mm', m).replace('ss', s);
} };
var props = {};
var PropertiesService = { getScriptProperties: function () { return { getProperty: function (k) { return props[k] || null; }, setProperty: function (k, v) { props[k] = v; } }; } };

/* ---- Moduli finto ---- */
var T = { CHECKBOX: 'CB', MULTIPLE_CHOICE: 'MC', LIST: 'LI', TEXT: 'TX', PARAGRAPH_TEXT: 'PX', PAGE_BREAK: 'PB', SECTION_HEADER: 'SH', IMAGE: 'IM', VIDEO: 'VI' };
function item(id, tipo, titolo, punti) {
  var o = { getId: function () { return id; }, getType: function () { return tipo; }, getTitle: function () { return titolo; } };
  var as = { getPoints: function () { return punti; } };
  ['asCheckboxItem', 'asMultipleChoiceItem', 'asListItem', 'asTextItem', 'asParagraphTextItem'].forEach(function (m) { o[m] = function () { return as; }; });
  return o;
}
function risp(email, ts, voci) {   // voci: [[item, risposta, punteggio|null]]
  var irs = voci.map(function (v) { return { getItem: function () { return v[0]; }, getResponse: function () { return v[1]; }, getScore: function () { return v[2]; } }; });
  return { getRespondentEmail: function () { return email; }, getTimestamp: function () { return new Date(ts); }, getItemResponses: function () { return irs; },
    getGradableItemResponses: function () { return irs.filter(function (x) { return x.getScore() !== null; }); } };
}
var q1 = item(11, T.MULTIPLE_CHOICE, 'Quale estensione ha un documento di testo?', 1), q2 = item(12, T.CHECKBOX, 'Quali sono cartelle?', 2), q3 = item(13, T.PARAGRAPH_TEXT, 'Spiega che cosa e un percorso.', 3), q4 = item(14, T.TEXT, 'Una parola per file.', 1), sez = item(15, T.SECTION_HEADER, 'Parte B', 0);
var form = { getItems: function () { return [q1, q2, sez, q3, q4]; }, getTitle: function () { return 'Quiz di prova'; } };
var ris = [
  risp('mario.rossi@studenti.piamarta.it', '2026-11-13T10:50:00Z', [[q1, '.txt', 1], [q2, ['Documenti', 'Immagini'], 2], [q3, '=SOMMA(1;2) un percorso e la strada', 0], [q4, 'file', 1]]),
  risp('mario.rossi@studenti.piamarta.it', '2026-11-13T11:10:00Z', [[q1, '.exe', 0], [q2, ['Documenti'], 1], [q3, 'Il percorso e dove sta il file.', 0], [q4, 'file', 1]]),
  risp('anna.verdi@studenti.piamarta.it', '2026-11-13T10:55:00Z', [[q1, '.txt', 1], [q2, ['Documenti', 'Immagini'], 2], [q3, 'Un posto.', 2], [q4, '', 0]]),
  risp('ignoto@gmail.com', '2026-11-13T10:56:00Z', [[q1, '.txt', 1]])
];

/* ---- Classroom, Drive, UrlFetch finti ---- */
var fetchCount = 0, metaCount = 0;
var DOC = 'application/vnd.google-apps.document';
var files = {
  MODELLO: { nome: 'Documento con gli screenshot', mime: DOC, mod: new Date('2026-11-13T09:00:00Z'), html: '<html><head><style>p{color:red}</style></head><body><p>Istruzioni: incolla qui gli screenshot.</p><img src="x"></body></html>' },
  CP1: { nome: 'Copia di Documento - Rossi Mario', mime: DOC, mod: new Date('2026-11-13T11:20:00Z'), html: '<body><p>Istruzioni: incolla qui gli screenshot.</p><img src="x"><p>Ho fatto la cartella &amp; il file.</p><img src="a"><img src="b"></body>' },
  CP2: { nome: 'Copia di Documento - Verdi Anna', mime: DOC, mod: new Date('2026-11-13T11:21:00Z'), html: '<body><p>Istruzioni: incolla qui gli screenshot.</p><img src="x"></body>' },
  PDF1: { nome: 'foto.png', mime: 'image/png', mod: new Date('2026-11-13T11:22:00Z'), html: '' }
};
var DriveApp = { getFileById: function (id) {
  metaCount++;
  if (id === 'NEGATO') throw new Error('Nessun accesso: file negato');
  var f = files[id]; if (!f) throw new Error('non trovato ' + id);
  return { getName: function () { return f.nome; }, getMimeType: function () { return f.mime; }, getLastUpdated: function () { return f.mod; } };
} };
var tokenScope = 'https://www.googleapis.com/auth/forms https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/classroom.courses.readonly https://www.googleapis.com/auth/classroom.rosters.readonly https://www.googleapis.com/auth/classroom.coursework.students.readonly https://www.googleapis.com/auth/classroom.profile.emails';
var fetchSingoli = [];
var UrlFetchApp = { fetch: function (url) {
  fetchSingoli.push(url);
  if (/tokeninfo/.test(url)) return { getResponseCode: function () { return 200; }, getContentText: function () { return JSON.stringify({ scope: tokenScope }); } };
  var m = /files\/([^\/]+)\/export/.exec(url), f = m && files[m[1]];
  return { getResponseCode: function () { return f ? 200 : 404; }, getContentText: function () { return f ? f.html : ''; } };
}, fetchAll: function (reqs) {
  return reqs.map(function (r) {
    fetchCount++;
    var id = /document\/d\/([^\/]+)\//.exec(r.url)[1];
    check(/^Bearer /.test(r.headers.Authorization), 'manca il token');
    return { getResponseCode: function () { return files[id] ? 200 : 404; }, getContentText: function () { return files[id] ? files[id].html : ''; } };
  });
} };
var ScriptApp = { getOAuthToken: function () { return 'TOKEN'; } };
var corso = { id: 'C1', name: '1 INF 26/27' };
var studenti = [
  { userId: 'u1', profile: { name: { familyName: 'Rossi', givenName: 'Mario', fullName: 'Mario Rossi' }, emailAddress: 'mario.rossi@studenti.piamarta.it' } },
  { userId: 'u2', profile: { name: { familyName: 'Verdi', givenName: 'Anna', fullName: 'Anna Verdi' }, emailAddress: 'anna.verdi@studenti.piamarta.it' } },
  { userId: 'u3', profile: { name: { familyName: 'Neri', givenName: 'Luca', fullName: 'Luca Neri' }, emailAddress: 'luca.neri@studenti.piamarta.it' } },
  { userId: 'u4', profile: { name: { familyName: 'Bianchi', givenName: 'Sara', fullName: 'Sara Bianchi' }, emailAddress: 'sara.bianchi@studenti.piamarta.it' } }
];
var lavori = [
  { id: 'W1', title: '13/11 Ora 4: File e cartelle', workType: 'ASSIGNMENT', creationTime: '2026-11-13T10:38:00Z', materials: [{ driveFile: { shareMode: 'STUDENT_COPY', driveFile: { id: 'MODELLO' } } }] },
  { id: 'W2', title: 'Compito senza Documento', workType: 'ASSIGNMENT', creationTime: '2026-11-12T10:38:00Z', materials: [] },
  { id: 'W3', title: 'Domanda', workType: 'SHORT_ANSWER_QUESTION', creationTime: '2026-11-12T10:38:00Z' }
];
var sottoW1 = [
  { userId: 'u1', state: 'TURNED_IN', late: false, updateTime: '2026-11-13T11:25:00Z', submissionHistory: [{ stateHistory: { state: 'CREATED', stateTimestamp: '2026-11-13T10:40:00Z' } }, { stateHistory: { state: 'TURNED_IN', stateTimestamp: '2026-11-13T11:24:30Z' } }], assignmentSubmission: { attachments: [{ driveFile: { id: 'CP1', title: 'Copia di Documento - Rossi Mario', alternateLink: 'https://docs.google.com/document/d/CP1/edit' } }] } },
  { userId: 'u2', state: 'CREATED', assignmentSubmission: { attachments: [{ driveFile: { id: 'CP2', title: 'Copia di Documento - Verdi Anna', alternateLink: 'https://docs.google.com/document/d/CP2/edit' } }] } },
  { userId: 'u3', state: 'TURNED_IN', late: true, updateTime: '2026-11-13T12:40:00Z', assignmentSubmission: { attachments: [{ driveFile: { id: 'NEGATO', title: 'Copia negata' } }, { driveFile: { id: 'PDF1', title: 'foto.png' } }] } },
  { userId: 'u4', state: 'NEW' }
];
var Classroom = { Courses: {
  list: function () { return { courses: [corso] }; },
  Students: { list: function () { return { students: studenti }; } },
  CourseWork: { list: function () { return { courseWork: lavori }; }, StudentSubmissions: { list: function (c, w) { return { studentSubmissions: w === 'W1' ? sottoW1 : [] }; } } }
} };

var ctx = { Utilities: Utilities, PropertiesService: PropertiesService, FormApp: { ItemType: T }, DriveApp: DriveApp, UrlFetchApp: UrlFetchApp, ScriptApp: ScriptApp, Classroom: Classroom, Logger: { log: function () { } }, console: console, Date: Date, JSON: JSON, Object: Object, Math: Math, Number: Number, String: String, RegExp: RegExp, Array: Array, isNaN: isNaN, Error: Error };
vm.createContext(ctx);
var src = fs.readFileSync(path.join(__dirname, 'motore-v2.22.1.js'), 'utf8');
vm.runInContext(src, ctx);
vm.runInContext('FB_ERRS = []; FB_lavoroIndice_ = {};', ctx);

var ss = new Foglio();
ctx.ss = ss; ctx.form = form; ctx.ris = ris;
// Elenco con i nomi (COGNOME Nome) e una scheda Corsi
var el = ss.insertSheet('Elenco 1INF'); el.getRange(1, 1, 1, 2).setValues([['Email', 'Allievo']]);
el.getRange(2, 1, 3, 2).setValues([['mario.rossi@studenti.piamarta.it', 'ROSSI Mario'], ['anna.verdi@studenti.piamarta.it', 'VERDI Anna'], ['luca.neri@studenti.piamarta.it', 'NERI Luca']]);
var co = ss.insertSheet('Corsi'); co.getRange(1, 1, 2, 3).setValues([['Nome', 'Id', 'Classe'], ['1 INF 26/27', 'C1', '1INF']]);

// ---------- Risposte ----------
vm.runInContext("RS_risposte_(ss, 'quiz-1inf-prova', form, { classe: '1INF', titolo: 'Quiz di prova' }, ris, 7)", ctx);
var R = ss.getSheetByName('Risposte quiz-1inf-prova').rows();
check(R[3].join('|') === 'Ora invio|Allievo|Email|Tentativo|Punteggio|Su|Migliore|D1|D2|D3|D4|P1|P2|P3|P4', 'intestazione Risposte: ' + R[3].join('|'));
var righe = R.slice(4, 8);
check(righe.length === 4, 'attese 4 righe di risposte, trovate ' + righe.length);
var rossi1 = righe.filter(function (r) { return r[1] === 'ROSSI Mario' && r[3] === 1; })[0], rossi2 = righe.filter(function (r) { return r[1] === 'ROSSI Mario' && r[3] === 2; })[0];
check(rossi1 && rossi2, 'due tentativi di ROSSI Mario');
check(rossi1[4] === 4 && rossi1[6] === 'S\u00ec' && rossi2[6] === '', 'tentativo migliore: ' + JSON.stringify([rossi1[4], rossi1[6], rossi2[6]]));
check(rossi1[0] === '13/11 11:50:00', 'ora in ora di Roma: ' + rossi1[0]);
check(rossi1[7] === '.txt' && rossi1[8] === 'Documenti | Immagini', 'testo risposte: ' + rossi1[7] + ' / ' + rossi1[8]);
check(/^ =SOMMA/.test(rossi1[9]), 'una risposta che comincia con = non deve essere una formula: ' + rossi1[9]);
check(rossi1[13] === 'da correggere' && rossi1[12] === 2 && rossi1[11] === 1, 'punti per domanda / aperta da correggere: ' + rossi1.slice(11).join(','));
var verdi = righe.filter(function (r) { return r[1] === 'VERDI Anna'; })[0];
check(verdi[13] === 2 && verdi[14] === 0, 'aperta corretta (2 punti) e non risposta (0 punti): ' + verdi.slice(11).join(','));
var ign = righe.filter(function (r) { return r[2] === 'ignoto@gmail.com'; })[0];
check(ign[1] === '(non abbinato)' && ign[8] === '' && ign[12] === 0, 'email non abbinata e domande senza risposta a 0: ' + JSON.stringify(ign));
var tutto = R.map(function (r) { return r.join('|'); }).join('\n');
var iE = R.map(function (r) { return r[0]; }).indexOf('Domanda');
check(iE > 0, 'blocco errori ricorrenti mancante');
var err = R.slice(iE + 1, iE + 5).filter(function (r) { return r[0]; });
check(err.length === 4, 'quattro domande con punti nel blocco errori: ' + err.length);
var e3 = err.filter(function (r) { return r[0] === 'D3'; })[0];
check(e3 && e3[2] === 2 && e3[3] === 1 && e3[4] === 0, 'D3: 2 sbagliate (VERDI 2/3, ignoto 0), 1 da correggere (ROSSI): ' + JSON.stringify(e3));
// la scheda Risposte nella classificazione delle schede
var info = vm.runInContext("IX_info_('Risposte quiz-1inf-prova', { 'quiz-1inf-prova': { classe: '1INF' } })", ctx);
check(info.g === 7 && info.id === 'quiz-1inf-prova' && info.classe === '1INF', 'IX_info_ Risposte: ' + JSON.stringify(info));
var info2 = vm.runInContext("IX_info_('Ris quiz-1inf-prova', {})", ctx);
check(info2.g === 7 && info2.id === 'quiz-1inf-prova', 'IX_info_ Ris invariata');
check(vm.runInContext("IX_info_('Documenti pubblica 1INF', {}).k", ctx) > vm.runInContext("IX_info_('Documenti 1INF', {}).k", ctx), 'ordine Documenti / pubblica');

// ---------- Documenti ----------
var indice = { classroom: { attivo: true, classi: { '1INF': '1 INF 26/27' } } };
ctx.indice = indice;
vm.runInContext("FB_documenti_(ss, indice, Date.now())", ctx);
var errs = vm.runInContext('FB_ERRS', ctx);
check(errs.length === 0, 'errori nel giro Documenti: ' + errs.join(' | '));
var D = ss.getSheetByName('Documenti 1INF'), P = ss.getSheetByName('Documenti pubblica 1INF');
check(D && P, 'schede Documenti create');
var d = D.rows(), p = P.rows();
check(/^1INF . Documenti . dati letti il \d\d\/\d\d\/\d{4} \d\d:\d\d:\d\d$/.test(d[0][0].replace(/\u00b7/g, '.')), 'riga 1: ' + d[0][0]);
check(d[3][0] === 'Allievo' && d[3][13] === 'Immagini aggiunte', 'intestazione Documenti');
var dr = d.slice(4);
check(dr.length === 5, 'righe: BIANCHI(1) + NERI(2 file) + ROSSI(1) + VERDI(1) = 5, trovate ' + dr.length + ' ' + JSON.stringify(dr.map(function (r) { return r[0]; })));
var rossi = dr.filter(function (r) { return r[0] === 'ROSSI Mario'; })[0];
check(rossi && rossi[4] === 'CONSEGNATO' && rossi[5] === '13/11 12:24', 'ROSSI consegnato 12:24 (11:24:30Z + 1h): ' + JSON.stringify(rossi && rossi.slice(0, 6)));
check(rossi[11] === 3 && rossi[12] === 1 && rossi[13] === 2, 'immagini ROSSI: totali 3, modello 1, aggiunte 2: ' + rossi.slice(11, 14));
check(/Ho fatto la cartella & il file/.test(rossi[15]) && rossi[14] > 20, 'estratto e caratteri: ' + rossi[15]);
var verdi2 = dr.filter(function (r) { return r[0] === 'VERDI Anna'; })[0];
check(verdi2[4] === 'ASSEGNATO' && verdi2[5] === '' && verdi2[13] === 0, 'VERDI assegnato, nessuna immagine aggiunta: ' + JSON.stringify(verdi2.slice(0, 14)));
var neri = dr.filter(function (r) { return r[0] === 'NERI Luca'; });
check(neri.length === 2 && neri[0][4] === 'IN RITARDO', 'NERI in ritardo, 2 file: ' + neri.length);
var negato = neri.filter(function (r) { return r[7] === 'NEGATO'; })[0], foto = neri.filter(function (r) { return r[7] === 'PDF1'; })[0];
check(negato && /non apribile/.test(negato[17]) && negato[13] === 'n.d.', 'file negato: n.d. con motivo: ' + JSON.stringify(negato && negato.slice(11, 19)));
check(foto && foto[11] === 1 && foto[13] === 1, 'file immagine: 1 immagine: ' + JSON.stringify(foto && foto.slice(11, 15)));
var bianchi = dr.filter(function (r) { return r[0] === 'BIANCHI Sara'; })[0];
check(bianchi && bianchi[4] === 'ASSEGNATO' && /nessun file/.test(bianchi[17]), 'BIANCHI senza file');
check(!dr.some(function (r) { return r[2] === 'Compito senza Documento' || r[2] === 'Domanda'; }), 'solo compiti di tipo Documento');
// scheda pubblica: nessuna email, link, titolo file, testo, cognome intero
var pubTxt = p.map(function (r) { return r.join('|'); }).join('\n');
check(p[3].join('|') === 'Allievo|Compito|Stato|Ora consegna|Immagini presenti|Immagini aggiunte|Caratteri', 'intestazione pubblica: ' + p[3].join('|'));
check(pubTxt.indexOf('@') < 0 && pubTxt.indexOf('docs.google') < 0 && pubTxt.indexOf('Ho fatto') < 0 && pubTxt.indexOf('Copia di') < 0, 'la scheda pubblica contiene dati non pubblici');
check(!/Rossi|Verdi|Neri|Bianchi/.test(pubTxt.replace(/Documenti pubblica/g, '')), 'cognome intero nella scheda pubblica: ' + pubTxt.slice(0, 600));
var pr = p.slice(4);
check(pr.some(function (r) { return r[0] === 'Mario R.' && r[4] === 's\u00ec' && r[5] === 2; }), 'Mario R.: immagini si, 2 aggiunte');
check(pr.some(function (r) { return r[0] === 'Anna V.' && r[4] === 'no'; }), 'Anna V.: immagini no');
// cache: secondo giro (dopo l'intervallo) non riesporta i file invariati
var f1 = fetchCount, m1 = metaCount;
vm.runInContext("FB_p_().setProperty('FB_DOC_T', '{}')", ctx);
vm.runInContext("FB_documenti_(ss, indice, Date.now())", ctx);
check(fetchCount - f1 === 0, 'secondo giro: nessuna esportazione se l ultima modifica non e cambiata (ne ha fatte ' + (fetchCount - f1) + ')');
check(metaCount > m1, 'secondo giro: i metadati si rileggono');
var d2 = ss.getSheetByName('Documenti 1INF').rows().slice(4), rossiB = d2.filter(function (r) { return r[0] === 'ROSSI Mario'; })[0];
check(rossiB[13] === 2 && /Ho fatto/.test(rossiB[15]), 'dalla cache: stesse immagini e stesso estratto');
// il Documento cambia: si rilegge
files.CP2.mod = new Date('2026-11-13T12:30:00Z'); files.CP2.html = '<body><img src="1"><img src="2"></body>';
f1 = fetchCount;
vm.runInContext("FB_p_().setProperty('FB_DOC_T', '{}')", ctx);
vm.runInContext("FB_documenti_(ss, indice, Date.now())", ctx);
check(fetchCount - f1 === 1, 'file cambiato: una sola esportazione (' + (fetchCount - f1) + ')');
var d3 = ss.getSheetByName('Documenti 1INF').rows().slice(4), v3 = d3.filter(function (r) { return r[0] === 'VERDI Anna'; })[0];
check(v3[11] === 2 && v3[13] === 1, 'Documento cambiato: 2 immagini, 1 aggiunta: ' + v3.slice(11, 14));
// documenti spento
vm.runInContext("indice.classroom.documenti = { attivo: false }; ss.getSheetByName('Documenti 1INF').clear(); FB_p_().setProperty('FB_DOC_T', '{}'); FB_documenti_(ss, indice, Date.now())", ctx);
check(ss.getSheetByName('Documenti 1INF').rows()[0][0] === '', 'classroom.documenti.attivo=false non scrive');

// ---------- FB_risultati_ (giro completo dei risultati, Moduli finto) ----------
form.getResponses = function () { return ris; };
ctx.FormApp.openById = function () { return form; };
var es = ss.insertSheet('Esiti'); es.getRange(1, 1, 2, 4).setValues([['Data', 'Id', 'Titolo', 'Link'], ['13/11', 'quiz-1inf-prova2', 'Quiz di prova', '']]);
vm.runInContext("FB_salva_('FB_FORMS', { 'quiz-1inf-prova2': { formId: 'F', classe: '1INF', titolo: 'Quiz di prova' } }); FB_ERRS = []; FB_risultati_(ss, Date.now())", ctx);
check(vm.runInContext('FB_ERRS', ctx).length === 0, 'errori in FB_risultati_: ' + vm.runInContext('FB_ERRS', ctx).join(' | '));
check(ss.getSheetByName('Ris quiz-1inf-prova2') && ss.getSheetByName('Risposte quiz-1inf-prova2'), 'FB_risultati_ scrive Ris e Risposte');
var ris2 = ss.getSheetByName('Ris quiz-1inf-prova2').rows();
check(ris2[3][0] === 'Email' && ris2[4][0] !== '', 'Ris invariata (Email, Migliore, Su, ...)');
vm.runInContext("ss.getSheetByName('Ris quiz-1inf-prova2').clear(); ss.getSheetByName('Risposte quiz-1inf-prova2').clear()", ctx);
vm.runInContext("FB_risultati_(ss, Date.now())", ctx);
check(ss.getSheetByName('Risposte quiz-1inf-prova2').rows()[3][0] === 'Ora invio', 'Ris cancellata = si riscrive anche Risposte');
// stesso numero di risposte e Risposte presente: non si rilegge
var cnt = 0; form.getTitle = function () { cnt++; return 'Quiz di prova'; };
vm.runInContext("FB_risultati_(ss, Date.now())", ctx);
check(cnt === 0, 'quiz invariato: nessuna rilettura');
// ---------- permessi (tokeninfo) ----------
vm.runInContext("FB_p_().setProperty('FB_PERM', '{}')", ctx);
var perm = vm.runInContext('FB_permessi_()', ctx);
check(/^OK/.test(perm), 'permessi: ' + perm);
tokenScope = tokenScope.replace('https://www.googleapis.com/auth/drive ', '').replace(' https://www.googleapis.com/auth/classroom.profile.emails', '');
vm.runInContext("FB_p_().setProperty('FB_PERM', '{}')", ctx);
perm = vm.runInContext('FB_permessi_()', ctx);
check(/^MANCANO: Drive .*Classroom: email/.test(perm), 'permessi mancanti: ' + perm);
var nf = fetchSingoli.length; vm.runInContext('FB_permessi_()', ctx);
check(fetchSingoli.length === nf, 'i permessi si rileggono al massimo ogni 30 minuti');
var st = new Foglio().insertSheet('Stato'); ctx.st = st; ctx.ss2 = { getSheetByName: function () { return st; }, insertSheet: function () { return st; } };
vm.runInContext("FB_stato_(ss2)", ctx);
var stv = st.rows(); check(stv[4][0] === 'Motore' && stv[4][1] === "2.22.1" && stv[5][0] === 'Permessi', 'riga Permessi in Stato: ' + JSON.stringify(stv.slice(4)));
// seconda strada di esportazione: la prima (docs.google.com) risponde 403, la seconda (API Drive) 200
var primaFetchAll = UrlFetchApp.fetchAll;
UrlFetchApp.fetchAll = function (reqs) { return reqs.map(function () { return { getResponseCode: function () { return 403; }, getContentText: function () { return ''; } }; }); };
var inf = vm.runInContext("DC_leggi_(['CP1'], {}, 5, Date.now() + 60000)", ctx);
check(inf.CP1.img === 3 && inf.CP1.err === '', 'fallback API Drive: ' + JSON.stringify(inf.CP1));
UrlFetchApp.fetchAll = primaFetchAll;

// ---------- v2.22.1: Risposte solo per Moduli con risposte recenti, max 2 per giro, scheda vuota rifatta ----------
var oldBuild = form.getResponses;
vm.runInContext("FB_salva_('FB_NR', {}); ss.getSheetByName('Risposte quiz-1inf-prova2') && ss.deleteSheet && 0", ctx);
// (a) Modulo senza risposte: nessuna scheda Risposte
var vuoti = { getResponses: function () { return []; }, getTitle: function () { return 'Vuoto'; }, getItems: function () { return []; } };
var forms3 = { 'q-vuoto': vuoti };
ctx.FormApp.openById = function (fid) { return forms3[fid] || form; };
vm.runInContext("FB_salva_('FB_FORMS', { 'q-vuoto': { formId: 'q-vuoto', classe: '1INF', titolo: 'Vuoto' } }); FB_salva_('FB_NR', {}); FB_ERRS = []; FB_risultati_(ss, Date.now())", ctx);
check(!ss.getSheetByName('Risposte q-vuoto'), 'Modulo senza risposte: nessuna scheda Risposte');
// (b) scheda Risposte vuota (giro interrotto): si rifa
var shV = ss.insertSheet('Risposte quiz-1inf-prova2'); shV.clear();
vm.runInContext("FB_salva_('FB_FORMS', { 'quiz-1inf-prova2': { formId: 'F', classe: '1INF', titolo: 'Quiz di prova' } }); FB_salva_('FB_NR', { 'quiz-1inf-prova2': " + ris.length + " }); FB_risultati_(ss, Date.now())", ctx);
check(ss.getSheetByName('Risposte quiz-1inf-prova2').rows()[3][0] === 'Ora invio', 'scheda Risposte vuota: si rifa al giro dopo');
// (c) risposte vecchie (oltre 4 giorni): nessuna scheda Risposte
var vecchio = { getResponses: function () { return [{ getTimestamp: function () { return new Date(Date.now() - 6 * 86400000); }, getRespondentEmail: function () { return 'a@b.it'; }, getGradableItemResponses: function () { return []; }, getItemResponses: function () { return []; }, getResponseForItem: function () { return null; } }]; }, getTitle: function () { return 'Vecchio'; }, getItems: function () { return []; } };
forms3['q-vecchio'] = vecchio;
vm.runInContext("FB_salva_('FB_FORMS', { 'q-vecchio': { formId: 'q-vecchio', classe: '1INF', titolo: 'Vecchio' } }); FB_salva_('FB_NR', {}); FB_risultati_(ss, Date.now())", ctx);
check(!ss.getSheetByName('Risposte q-vecchio'), 'Modulo con risposte di oltre 4 giorni: nessuna scheda Risposte');
// (d) al massimo 2 Risposte per giro
var base = form;
['r1', 'r2', 'r3', 'r4'].forEach(function (k) { forms3[k] = base; });
vm.runInContext("FB_salva_('FB_FORMS', { r1: { formId: 'r1', classe: '1INF', titolo: 'R1' }, r2: { formId: 'r2', classe: '1INF', titolo: 'R2' }, r3: { formId: 'r3', classe: '1INF', titolo: 'R3' }, r4: { formId: 'r4', classe: '1INF', titolo: 'R4' } }); FB_salva_('FB_NR', {}); FB_risultati_(ss, Date.now())", ctx);
var nR = ['r1', 'r2', 'r3', 'r4'].filter(function (k) { return ss.getSheetByName('Risposte ' + k); }).length;
check(nR === 2, 'al massimo 2 schede Risposte per giro (' + nR + ')');
vm.runInContext("FB_risultati_(ss, Date.now())", ctx);
nR = ['r1', 'r2', 'r3', 'r4'].filter(function (k) { return ss.getSheetByName('Risposte ' + k); }).length;
check(nR === 4, 'al giro dopo le altre 2 (' + nR + ')');
if (fail.length) { console.log('PROVA FALLITA:\n- ' + fail.join('\n- ')); process.exit(1); }
console.log('PROVA OK (Risposte, Documenti, cache, privacy scheda pubblica; con servizi finti: API vere di Moduli, Classroom, Drive non provate)');
