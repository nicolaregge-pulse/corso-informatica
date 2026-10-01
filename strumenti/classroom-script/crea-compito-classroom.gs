/**
 * Crea COMPITI su Google Classroom con Apps Script (API Classroom).
 *
 * PRIMA DI USARLO (una volta sola):
 *  1) Usa l'ACCOUNT SCOLASTICO @piamarta.it (devi essere docente del corso).
 *  2) Nell'editor Apps Script, a sinistra: "Servizi" (icona +) > aggiungi "Google Classroom API".
 *  3) Esegui prima elencaCorsi() per trovare l'ID del corso giusto (lo trovi nel Registro di esecuzione).
 *
 * POI:
 *  4) Incolla l'ID in CONFIG.COURSE_ID qui sotto e personalizza titolo/descrizione/link/scadenza.
 *  5) Esegui creaCompito(). Alla prima esecuzione autorizza i permessi.
 *
 * Nota: state 'DRAFT' = crea la bozza (la pubblichi tu a mano dopo aver controllato);
 *       'PUBLISHED' = lo pubblica subito agli allievi.
 */

// ---------------- 1) Trova l'ID del corso ----------------
function elencaCorsi() {
  var res = Classroom.Courses.list({ courseStates: ['ACTIVE'] });
  if (!res.courses || !res.courses.length) { Logger.log('Nessun corso attivo.'); return; }
  res.courses.forEach(function(c) {
    Logger.log('CORSO: "' + c.name + '"  →  ID: ' + c.id);
  });
}

// ---------------- 2) Configura e crea il compito ----------------
var CONFIG = {
  COURSE_ID: 'INCOLLA_QUI_ID_CORSO',                 // da elencaCorsi()
  TITOLO: 'Test aperto — Sicurezza 1ª ora (parole tue)',
  DESCRIZIONE: 'Rispondi con PAROLE TUE ed ESEMPI TUOI. Le risposte copiate dalla slide o da '
             + 'internet/AI si riconoscono e valgono meno di una risposta semplice ma tua.',
  LINK: '',          // opzionale: URL del Modulo/materiale (vuoto = nessun allegato)
  PUNTI: 100,        // metti 0 per "nessun voto numerico"
  PUBBLICA_SUBITO: false,   // false = bozza (consigliato: controlli e pubblichi tu); true = pubblica agli allievi
  // Scadenza (opzionale): lascia null per nessuna scadenza
  SCADENZA: null     // es. {anno:2026, mese:10, giorno:3, ora:14, minuti:0}
};

function creaCompito() {
  var work = {
    title: CONFIG.TITOLO,
    description: CONFIG.DESCRIZIONE,
    workType: 'ASSIGNMENT',
    state: CONFIG.PUBBLICA_SUBITO ? 'PUBLISHED' : 'DRAFT'
  };
  if (CONFIG.PUNTI && CONFIG.PUNTI > 0) work.maxPoints = CONFIG.PUNTI;
  if (CONFIG.LINK) work.materials = [{ link: { url: CONFIG.LINK } }];
  if (CONFIG.SCADENZA) {
    work.dueDate = { year: CONFIG.SCADENZA.anno, month: CONFIG.SCADENZA.mese, day: CONFIG.SCADENZA.giorno };
    work.dueTime = { hours: CONFIG.SCADENZA.ora, minutes: CONFIG.SCADENZA.minuti };
  }
  var creato = Classroom.Courses.CourseWork.create(work, CONFIG.COURSE_ID);
  Logger.log('Compito creato (' + work.state + '): ' + creato.title);
  Logger.log('Link al compito: ' + creato.alternateLink);
}

// ---------------- (opzionale) crea più compiti in una volta ----------------
function creaPiuCompiti() {
  var LISTA = [
    { titolo: 'Compito 1', descrizione: 'Testo...', link: '' },
    { titolo: 'Compito 2', descrizione: 'Testo...', link: '' }
  ];
  LISTA.forEach(function(c) {
    var w = { title: c.titolo, description: c.descrizione, workType: 'ASSIGNMENT', state: 'DRAFT' };
    if (c.link) w.materials = [{ link: { url: c.link } }];
    var r = Classroom.Courses.CourseWork.create(w, CONFIG.COURSE_ID);
    Logger.log('Creato (bozza): ' + r.title + ' → ' + r.alternateLink);
  });
}
