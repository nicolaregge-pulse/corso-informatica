/**
 * CONTROLLA le consegne di un compito su Google Classroom e ne fa una ZIP.
 *
 * SETUP (una volta): account @piamarta.it; nell'editor Apps Script, "Servizi" (+) >
 *   aggiungi "Google Classroom API". Poi autorizza alla prima esecuzione.
 *
 * USO:
 *   1) elencaCompiti()          → trova l'ID del compito (nel Registro di esecuzione).
 *   2) statoConsegne()          → chi ha consegnato / assegnato / il voto.
 *   3) scaricaEZippaConsegne()  → crea una ZIP nel tuo Drive con tutte le consegne
 *                                 (un file per allievo, già nominato). Nel log trovi il link.
 */

var CONFIG = {
  COURSE_ID: '162656105584',    // NUOVO 2 INFO 26/27 (metti il corso giusto)
  COURSEWORK_ID: 'INCOLLA_ID_COMPITO'  // da elencaCompiti()
};

// ---- 1) elenco compiti del corso ----
function elencaCompiti() {
  var res = Classroom.Courses.CourseWork.list(CONFIG.COURSE_ID, { orderBy: 'updateTime desc' });
  (res.courseWork || []).forEach(function(w) {
    Logger.log('COMPITO: "' + w.title + '"  →  ID: ' + w.id);
  });
}

// nome allievo da userId (cache per non ripetere chiamate)
var _nomi = {};
function nomeAllievo(userId) {
  if (_nomi[userId]) return _nomi[userId];
  try { var p = Classroom.UserProfiles.get(userId); _nomi[userId] = p.name.fullName; }
  catch (e) { _nomi[userId] = userId; }
  return _nomi[userId];
}

// ---- 2) stato delle consegne ----
function statoConsegne() {
  var subs = (Classroom.Courses.CourseWork.StudentSubmissions
             .list(CONFIG.COURSE_ID, CONFIG.COURSEWORK_ID).studentSubmissions) || [];
  var consegnati = 0;
  subs.forEach(function(s) {
    var stato = {NEW:'non iniziato', CREATED:'assegnato (non consegnato)',
                 TURNED_IN:'CONSEGNATO', RETURNED:'riconsegnato'}[s.state] || s.state;
    if (s.state === 'TURNED_IN' || s.state === 'RETURNED') consegnati++;
    var voto = (s.assignedGrade != null) ? (' · voto ' + s.assignedGrade) : '';
    Logger.log(nomeAllievo(s.userId) + '  →  ' + stato + voto);
  });
  Logger.log('--- Consegnati: ' + consegnati + ' / ' + subs.length + ' ---');
}

// esporta un file Drive in blob (Google Docs/Slides/Sheets -> PDF; altri -> così com'è)
function _blobDi(fileId) {
  var f = DriveApp.getFileById(fileId);
  var mt = f.getMimeType();
  if (mt.indexOf('application/vnd.google-apps') === 0) {
    return f.getAs('application/pdf');
  }
  return f.getBlob();
}

// ---- 3) scarica e zippa tutte le consegne ----
function scaricaEZippaConsegne() {
  var titolo = Classroom.Courses.CourseWork.get(CONFIG.COURSE_ID, CONFIG.COURSEWORK_ID).title;
  var subs = (Classroom.Courses.CourseWork.StudentSubmissions
             .list(CONFIG.COURSE_ID, CONFIG.COURSEWORK_ID).studentSubmissions) || [];
  var blobs = [];
  subs.forEach(function(s) {
    if (s.state !== 'TURNED_IN' && s.state !== 'RETURNED') return; // solo chi ha consegnato
    var nome = nomeAllievo(s.userId).replace(/[\\\/:*?"<>|]/g, '_');
    var atts = (s.assignmentSubmission && s.assignmentSubmission.attachments) || [];
    atts.forEach(function(a, i) {
      try {
        if (a.driveFile && a.driveFile.id) {
          var b = _blobDi(a.driveFile.id);
          var suffisso = (atts.length > 1) ? ('_' + (i + 1)) : '';
          b.setName(nome + suffisso + ' - ' + b.getName());
          blobs.push(b);
        }
      } catch (e) {
        Logger.log('Saltato un allegato di ' + nome + ': ' + e);
      }
    });
  });
  if (!blobs.length) { Logger.log('Nessuna consegna con allegati da zippare.'); return; }
  var nomeZip = 'Consegne - ' + titolo.replace(/[\\\/:*?"<>|]/g, '_') + '.zip';
  var zip = Utilities.zip(blobs, nomeZip);
  // cartella di destinazione nel Drive
  var cartella = DriveApp.createFolder('CONSEGNE ' + titolo + ' ' + new Date().toISOString().slice(0,10));
  var file = cartella.createFile(zip);
  Logger.log('ZIP creata: ' + file.getUrl());
  Logger.log('File nella ZIP: ' + blobs.length);
}
