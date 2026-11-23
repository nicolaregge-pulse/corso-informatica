/* classroom_pubblica_prova5min v1.0 (23/11/2026): PROVA di 5 minuti, da lanciare dal docente nel progetto FABBRICA (account PIAMARTA). Scrive SOLO nel corso di prova. */
function PB_prova5minuti() {
  var NOME_CORSO = 'PROVA PUBBLICAZIONE';   // il corso di prova creato dal docente (nessun allievo)
  var MODELLO_DOC_ID = '';                  // facoltativo: id di un Documento Google qualsiasi; vuoto = quella prova resta «non provata»
  function r(p, v) { Logger.log((v ? 'PROVATO        ' : 'NON RIUSCITO   ') + p); }
  var sc = '';
  try { sc = JSON.parse(UrlFetchApp.fetch('https://oauth2.googleapis.com/tokeninfo?access_token=' + encodeURIComponent(ScriptApp.getOAuthToken())).getContentText()).scope || ''; } catch (e) { Logger.log('permessi non letti: ' + e); }
  r('permesso classroom.coursework.students (scrittura)', /classroom\.coursework\.students(\s|$)/.test(sc));
  r('permesso drive (scrittura)', /auth\/drive(\s|$)/.test(sc));
  var corsi = (Classroom.Courses.list({ courseStates: ['ACTIVE'] }).courses || []).filter(function (c) { return c.name === NOME_CORSO; });
  if (corsi.length !== 1) { Logger.log('STOP: il corso «' + NOME_CORSO + '» non e unico o non esiste (trovati ' + corsi.length + ')'); return; }
  var id = corsi[0].id, cw, mat = [{ link: { url: 'https://example.com/prova' } }], f = null, copia = null;
  try {
    f = DriveApp.createFile(Utilities.newBlob('%PDF-1.4\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF', 'application/pdf', 'prova-pubb.pdf'));
    mat.push({ driveFile: { driveFile: { id: f.getId() }, shareMode: 'VIEW' } });
    r('PDF creato in Drive', true);
    if (MODELLO_DOC_ID) { copia = DriveApp.getFileById(MODELLO_DOC_ID).makeCopy('prova-pubb-copia'); mat.push({ driveFile: { driveFile: { id: copia.getId() }, shareMode: 'STUDENT_COPY' } }); r('copia del Documento creata', true); }
  } catch (e) { r('Drive: ' + e, false); }
  try {
    var testo = 'Prova العربية 中文 italiano';
    cw = Classroom.Courses.CourseWork.create({ title: '1/1 Ora 1: prova pubblicazione', description: testo, workType: 'ASSIGNMENT', state: 'DRAFT', materials: mat }, id);
    r('compito creato in BOZZA con ' + mat.length + ' allegati (link, PDF' + (copia ? ', Documento copia per ogni studente' : '') + ')', true);
    var a = Classroom.Courses.CourseWork.get(id, cw.id);
    r('riletto: testo arabo e cinese identico', a.description === testo);
    r('riletto: ' + (a.materials || []).length + ' allegati su ' + mat.length + ', nessuna scadenza', (a.materials || []).length === mat.length && !a.dueDate);
    Classroom.Courses.CourseWork.patch({ state: 'PUBLISHED' }, id, cw.id, { updateMask: 'state' });
    r('stato letto da Classroom dopo la pubblica: ' + Classroom.Courses.CourseWork.get(id, cw.id).state, Classroom.Courses.CourseWork.get(id, cw.id).state === 'PUBLISHED');
  } catch (e) { r('Classroom: ' + e, false); }
  try { if (cw) { Classroom.Courses.CourseWork.remove(id, cw.id); r('compito di prova cancellato', true); } } catch (e) { r('cancellazione: ' + e + ' (cancellalo a mano nel corso di prova)', false); }
  try { if (f) f.setTrashed(true); if (copia) copia.setTrashed(true); } catch (e) { }
  Logger.log('FINE PROVA. Copia tutte le righe del registro e incollale nella chat.');
}
