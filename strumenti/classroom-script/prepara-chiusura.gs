/**
 * PREPARA CHIUSURA (parte meccanica di "CHIUDI CLASSE").
 * In un clic: crea un FOGLIO di stato consegne (+ voti quiz se presenti) e una ZIP delle
 * consegne nel tuo Drive. La VALUTAZIONE (voti, giudizi, anti-plagio, libri, report) la fa
 * poi l'AI dalla ZIP: lo script NON corregge e NON giudica.
 *
 * SETUP: account @piamarta.it; "Servizi" (+) > "Google Classroom API". Autorizza alla 1ª esecuzione.
 * USO: 1) elencaCompiti() -> ID del compito;  2) incollalo in COURSEWORK_ID;  3) preparaChiusura().
 */
var CONFIG = {
  COURSE_ID: '162656105584',            // NUOVO 2 INFO 26/27 (metti il corso giusto)
  COURSEWORK_ID: 'INCOLLA_ID_COMPITO'   // da elencaCompiti()
};

function elencaCompiti() {
  var res = Classroom.Courses.CourseWork.list(CONFIG.COURSE_ID, { orderBy: 'updateTime desc' });
  (res.courseWork || []).forEach(function(w){ Logger.log('COMPITO: "' + w.title + '"  →  ID: ' + w.id); });
}

var _nomi = {};
function nomeAllievo(id){ if(_nomi[id])return _nomi[id]; try{_nomi[id]=Classroom.UserProfiles.get(id).name.fullName;}catch(e){_nomi[id]=id;} return _nomi[id]; }
function _blobDi(id){ var f=DriveApp.getFileById(id),mt=f.getMimeType(); return mt.indexOf('application/vnd.google-apps')===0 ? f.getAs('application/pdf') : f.getBlob(); }

function preparaChiusura() {
  var titolo = Classroom.Courses.CourseWork.get(CONFIG.COURSE_ID, CONFIG.COURSEWORK_ID).title;
  var subs = (Classroom.Courses.CourseWork.StudentSubmissions
             .list(CONFIG.COURSE_ID, CONFIG.COURSEWORK_ID).studentSubmissions) || [];

  // cartella di lavoro
  var cart = DriveApp.createFolder('CHIUSURA ' + titolo + ' ' + new Date().toISOString().slice(0,10));

  // 1) FOGLIO di stato
  var ss = SpreadsheetApp.create('Chiusura - ' + titolo);
  DriveApp.getFileById(ss.getId()).moveTo(cart);
  var sh = ss.getActiveSheet();
  sh.appendRow(['Allievo', 'Stato', 'Voto quiz', 'Ultima consegna', 'N. allegati']);
  sh.getRange(1,1,1,5).setFontWeight('bold').setBackground('#12467a').setFontColor('#ffffff');

  var blobs = [], consegnati = 0;
  subs.forEach(function(s){
    var nome = nomeAllievo(s.userId);
    var stato = {NEW:'non iniziato', CREATED:'assegnato (non consegnato)',
                 TURNED_IN:'CONSEGNATO', RETURNED:'riconsegnato'}[s.state] || s.state;
    var atts = (s.assignmentSubmission && s.assignmentSubmission.attachments) || [];
    var data = s.updateTime ? s.updateTime.slice(0,16).replace('T',' ') : '';
    sh.appendRow([nome, stato, (s.assignedGrade!=null?s.assignedGrade:''), data, atts.length]);

    if (s.state === 'TURNED_IN' || s.state === 'RETURNED') {
      consegnati++;
      var safe = nome.replace(/[\\\/:*?"<>|]/g,'_');
      atts.forEach(function(a,i){
        try { if (a.driveFile && a.driveFile.id) {
          var b = _blobDi(a.driveFile.id);
          b.setName(safe + (atts.length>1?('_'+(i+1)):'') + ' - ' + b.getName());
          blobs.push(b);
        }} catch(e){ Logger.log('Saltato allegato di '+nome+': '+e); }
      });
    }
  });
  // riga riepilogo
  sh.appendRow([]);
  sh.appendRow(['CONSEGNATI', consegnati + ' / ' + subs.length]);

  // 2) ZIP delle consegne
  var zipUrl = '(nessun allegato)';
  if (blobs.length) {
    var zip = Utilities.zip(blobs, 'Consegne - ' + titolo.replace(/[\\\/:*?"<>|]/g,'_') + '.zip');
    var zf = cart.createFile(zip);
    zipUrl = zf.getUrl();
  }

  Logger.log('— PREPARA CHIUSURA: ' + titolo + ' —');
  Logger.log('Cartella: ' + cart.getUrl());
  Logger.log('Foglio stato: ' + ss.getUrl());
  Logger.log('ZIP consegne: ' + zipUrl + '  (file: ' + blobs.length + ')');
  Logger.log('Consegnati: ' + consegnati + ' / ' + subs.length);
  Logger.log('>> Ora passa la ZIP all\'AI per la valutazione (comando CHIUDI).');
}
