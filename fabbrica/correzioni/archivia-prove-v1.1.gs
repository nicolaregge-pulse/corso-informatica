/**
 * ARCHIVIA PROVE - v1.1 (17/11/2026)  (la v1.0 resta: archivia-prove-v1.0.gs)
 * Apps Script per l'account PIAMARTA del docente. NON ATTIVATO: parte solo quando il docente lo lancia a mano.
 * Nessun cognome, nessuna password, nessun trigger. Non cambia mai i permessi di condivisione di nessun file o cartella.
 *
 * Novita della v1.1: ALBERO DELLE CARTELLE e FOGLIO INDICE (stessi campi di INDICE-PROVE-REGGE-v1.0.xlsx).
 *   Regge / <anno scolastico> / <classe> / <AAAA-MM-GG Ora N - titolo breve> /
 *   Dentro la cartella di ogni prova: collegamento al Moduli, PDF delle risposte (se l'elenco ha l'id), foglio dei risultati
 *   (solo se la cartella non e condivisa), come nella v1.0. Nella cartella «Regge» c'e il foglio «Indice prove Regge».
 *
 * Che cosa fa, a richiesta (si lancia a mano dal menu «Esegui»):
 *   1. apAnteprima()    : legge e basta, scrive nel Registro che cosa farebbe. Non crea e non cambia niente.
 *   2. archiviaProve()  : trova (o crea) «Regge» e l'albero anno/classe/prova, ci mette un COLLEGAMENTO a ogni Moduli
 *                         dell'elenco (il Moduli NON si sposta: il link dei ragazzi non cambia), copia il PDF delle risposte
 *                         se l'elenco ha l'id del PDF, crea o aggiorna il foglio dei risultati di ogni quiz e la riga
 *                         del foglio Indice (una riga per prova; se la riga esiste i link gia scritti dal docente restano).
 *   3. apAggiornaRisultati() : ricalcola solo i fogli dei risultati (da rilanciare quando si correggono le discorsive).
 *
 * FOGLIO INDICE «Indice prove Regge», scheda «Indice»: Anno scolastico, Classe, Data, Ora, Titolo, Tipo, Percorso cartella,
 * Link Moduli ragazzi, Link file risposte (PDF), Link foglio risultati, Scala voto, Punti totali, Stato, Note.
 * Nessun cognome e nessun voto di allievo nell'Indice. Dove il link non c'e: «da inserire».
 *
 * FOGLIO DEI RISULTATI (uno per quiz): scheda «Voti» (una riga per allievo: punti delle caselle, punti delle discorsive,
 * quante discorsive restano «da correggere», totale, voto proposto da 50 a 70 con il conto, stato PROVVISORIO o DEFINITIVO)
 * e scheda «Risposte» (copia dei valori della scheda «Risposte <id quiz>» del foglio Fabbrica, solo lettura dell'originale).
 * Voto proposto = 50 + 20 x punti / totale, arrotondato al mezzo voto (a meta, per eccesso). Le domande discorsive non
 * ricevono mai un punteggio da questo script: contano solo i punti scritti nelle colonne P del foglio Fabbrica.
 *
 * PRIVACY: il foglio dei risultati ha cognomi, email e voti. Se la cartella di archiviazione (o una cartella sopra di essa)
 * e condivisa con altre persone, lo script NON ci mette il foglio dei risultati: lo crea nella cartella riservata
 * AP_RISULTATI_RISERVATI_NOME (nella radice di Il mio Drive, non condivisa) e lo scrive nel Registro. Nella cartella
 * condivisa vanno solo i collegamenti ai Moduli, il PDF delle risposte e l'Indice (senza nomi di allievi).
 *
 * PERMESSI RICHIESTI (la prima volta Google chiede di autorizzare, account PIAMARTA):
 *   - https://www.googleapis.com/auth/drive          (DriveApp: cercare/creare cartelle, collegamenti, copia del PDF)
 *   - https://www.googleapis.com/auth/spreadsheets   (SpreadsheetApp: leggere Fabbrica, creare e scrivere Indice e risultati)
 *   Nessun UrlFetchApp, nessun trigger, nessuna Property. Il foglio Fabbrica viene SOLO letto.
 *
 * NON PROVATO (17/11/2026): lo script non e stato eseguito su Drive (nessun accesso Apps Script dal repository);
 * il calcolo (voto, tentativo migliore, discorsive da correggere, riga dell'Indice, nomi delle cartelle) e provato in locale
 * con dati finti; DriveApp/SpreadsheetApp, getTargetId dei collegamenti, il controllo della condivisione, la creazione
 * dell'albero e il foglio Indice non sono provati.
 *
 * Changelog:
 *   1.0 (17/11/2026): prima versione, 2INF e 4TI del 17/11/2026.
 *   1.1 (17/11/2026): albero Regge/anno/classe/prova, foglio Indice con gli stessi campi dell'Excel; elenco con data, ora,
 *                     titolo breve, tipo, link Moduli ragazzi e scala voto.
 */

// ---------------------------------------------------------------- CONFIGURAZIONE (qui si cambia, niente altro)
var AP_CARTELLA_PADRE_ID = '15i5CWtuJfETRrtHMACelzfS7XtGa360t'; // INFORMATICA > ARCHIVIAZIONE PROVE
var AP_CARTELLA_NOME = 'Regge';                                  // cartella creata dal docente dentro il padre
var AP_CARTELLA_ID = '';                                         // se noto, l'id della cartella «Regge» (ha la precedenza sul nome)
var AP_RISULTATI_RISERVATI_NOME = 'Regge - risultati riservati (solo docente)';
var AP_FOGLIO_FABBRICA_ID = '1EUUhdhJl7QG6CCcN-a2h1Nd6xkQiv1r1mk3QeUUi2r4'; // Fabbrica (10/11/2026), solo lettura

var AP_ANNO = '2026-27';                                        // anno scolastico (primo livello sotto «Regge»)
var AP_INDICE_NOME = 'Indice prove Regge';                       // foglio indice nella cartella «Regge»
var AP_ND = 'da inserire';

// Elenco dei quiz da archiviare. nChiuse = domande a caselle (corrette dal Moduli); totale = punti massimi del quiz.
// data = AAAA-MM-GG; ora = «1-2» o «3»; breve = titolo breve per il nome della cartella; moduliUrl = link dei ragazzi.
// pdfId = id Drive del PDF «risposte e spiegazioni» (senza nomi di allievi) gia caricato dal docente; vuoto = da caricare a mano.
var AP_ELENCO = [
  { classe: '2INF', id: 'quiz-2inf-1711-teoria', titolo: '17/11 Quiz di teoria: web, HTML e CSS',
    data: '2026-11-17', ora: '1-2', breve: 'Quiz teoria web HTML CSS', tipo: 'Quiz', titoloIndice: 'Quiz di teoria: web, HTML e CSS',
    moduliUrl: 'https://docs.google.com/forms/d/e/1FAIpQLSd5Jf81CM4cGrt0FMxZ1e_O5cDtVdSkFCz3cYCJEgtjFWI9TA/viewform',
    formId: '1H5NXMMOoNDIkzfpTL28qTOTlorG4TBsEFOTm111Eado', nChiuse: 10, totale: 40, pdfId: '' },
  { classe: '4TI', id: 'quiz-4ti-1711-ora3-teoria', titolo: '17/11 Ora 3: Quiz di teoria di rete',
    data: '2026-11-17', ora: '3', breve: 'Quiz teoria rete', tipo: 'Quiz', titoloIndice: 'Quiz di teoria di rete',
    moduliUrl: 'https://docs.google.com/forms/d/e/1FAIpQLSe0phmn0IYVaRk66PJg7sHs8GpTVg_v_p0s6jSwgOcxepCznA/viewform',
    formId: '1TRdbXCRKqFHGuMtL13j35ULjoAlxorIa5lHPqNGDpLc', nChiuse: 14, totale: 60, pdfId: '' }
];

// ---------------------------------------------------------------- punti di ingresso
function apAnteprima() { apGiro_(false, true); }
function archiviaProve() { apGiro_(true, true); }
function apAggiornaRisultati() { apGiro_(true, false); }

function apGiro_(scrivi, archivia) {
  var log = function (s) { Logger.log((scrivi ? '' : '[ANTEPRIMA] ') + s); };
  var cartella = apCartella_(scrivi, log);
  var condivisa = cartella ? apCondivisa_(cartella) : true;
  log('Cartella di archiviazione: ' + (cartella ? cartella.getName() + ' (' + cartella.getUrl() + ')' : 'non trovata') +
      ' - condivisa con altri: ' + (condivisa ? 'SI o non verificabile' : 'no'));
  var ris = null, indice = [];
  AP_ELENCO.forEach(function (q) {
    var prova = null, linkPdf = '', linkRis = '';
    if (archivia && cartella) {
      prova = apAlbero_(cartella, q, scrivi, log);
      if (prova) {
        apCollega_(prova, q.formId, 'Moduli ' + q.classe, scrivi, log);
        if (q.pdfId) linkPdf = apCopiaPdf_(prova, q.pdfId, scrivi, log);
        else {
          var pi = prova.getFilesByType(MimeType.PDF);
          if (pi.hasNext()) { linkPdf = pi.next().getUrl(); log('PDF delle risposte di ' + q.classe + ': trovato nella cartella della prova.'); }
          else log('PDF delle risposte di ' + q.classe + ': id non in elenco e nessun PDF nella cartella, da caricare a mano.');
        }
      }
    }
    var dove = condivisa ? (ris = ris || apCartellaRiservata_(scrivi, log)) : prova;
    var u = apRisultati_(q, dove, scrivi, log);
    if (u) linkRis = u;
    indice.push({ q: q, linkPdf: linkPdf, linkRis: linkRis });
  });
  if (archivia && cartella) apIndice_(cartella, indice, scrivi, log);
}

// ---------------------------------------------------------------- Drive
function apCartella_(scrivi, log) {
  if (AP_CARTELLA_ID) return DriveApp.getFolderById(AP_CARTELLA_ID);
  var padre = DriveApp.getFolderById(AP_CARTELLA_PADRE_ID);
  var it = padre.getFoldersByName(AP_CARTELLA_NOME);
  if (it.hasNext()) return it.next();
  if (!scrivi) { log('La cartella «' + AP_CARTELLA_NOME + '» non esiste: la creerei dentro ' + padre.getName() + '.'); return null; }
  log('Creo la cartella «' + AP_CARTELLA_NOME + '» dentro ' + padre.getName() + '.');
  return padre.createFolder(AP_CARTELLA_NOME);
}

// Vero se la cartella o una cartella sopra di essa e condivisa con altri (non cambia nulla, legge soltanto).
function apCondivisa_(cartella) {
  var f = cartella, giri = 0;
  while (f && giri++ < 10) {
    if (f.getSharingAccessType() !== DriveApp.Access.PRIVATE) return true;
    if (f.getViewers().length > 0 || f.getEditors().length > 0) return true;
    var p = f.getParents();
    f = p.hasNext() ? p.next() : null;
  }
  return false;
}

function apCartellaRiservata_(scrivi, log) {
  var radice = DriveApp.getRootFolder();
  var it = radice.getFoldersByName(AP_RISULTATI_RISERVATI_NOME);
  if (it.hasNext()) return it.next();
  if (!scrivi) { log('Creerei la cartella riservata «' + AP_RISULTATI_RISERVATI_NOME + '» nella radice di Il mio Drive.'); return null; }
  log('Creo la cartella riservata «' + AP_RISULTATI_RISERVATI_NOME + '» nella radice di Il mio Drive.');
  return radice.createFolder(AP_RISULTATI_RISERVATI_NOME);
}

// Collegamento (shortcut) al file: il file non si sposta e il suo indirizzo non cambia.
function apCollega_(cartella, fileId, etichetta, scrivi, log) {
  var it = cartella.getFiles();
  while (it.hasNext()) {
    var f = it.next();
    if (f.getMimeType() === 'application/vnd.google-apps.shortcut' && f.getTargetId() === fileId) {
      log(etichetta + ': collegamento gia presente (' + f.getName() + ').'); return;
    }
  }
  if (!scrivi) { log(etichetta + ': creerei un collegamento al Moduli ' + fileId + '.'); return; }
  var s = cartella.createShortcut(fileId);
  log(etichetta + ': collegamento creato (' + s.getName() + ', ' + s.getUrl() + ').');
}

function apCopiaPdf_(cartella, pdfId, scrivi, log) {
  var src = DriveApp.getFileById(pdfId), nome = src.getName();
  var it = cartella.getFilesByName(nome);
  if (it.hasNext()) { log('PDF ' + nome + ': gia presente.'); return it.next().getUrl(); }
  if (!scrivi) { log('PDF ' + nome + ': lo copierei nella cartella.'); return ''; }
  var copia = src.makeCopy(nome, cartella);
  log('PDF ' + nome + ': copiato nella cartella.');
  return copia.getUrl();
}

// ---------------------------------------------------------------- albero Regge / anno / classe / prova
function apNomeProva_(q) { return q.data + ' Ora ' + q.ora + ' - ' + q.breve; }
function apPercorso_(q) { return 'Regge/' + AP_ANNO + '/' + q.classe + '/' + apNomeProva_(q); }

function apSotto_(padre, nome, scrivi, log) {
  var it = padre.getFoldersByName(nome);
  if (it.hasNext()) return it.next();
  if (!scrivi) { log('Creerei la cartella «' + nome + '» dentro «' + padre.getName() + '».'); return null; }
  log('Creo la cartella «' + nome + '» dentro «' + padre.getName() + '».');
  return padre.createFolder(nome);
}

// Ritorna la cartella della prova (la crea se manca); in anteprima ritorna null se manca un livello.
function apAlbero_(regge, q, scrivi, log) {
  var f = regge, livelli = [AP_ANNO, q.classe, apNomeProva_(q)];
  for (var i = 0; i < livelli.length && f; i++) f = apSotto_(f, livelli[i], scrivi, log);
  return f;
}

// ---------------------------------------------------------------- foglio Indice (nessun nome di allievo)
var AP_INDICE_TESTA = ['Anno scolastico', 'Classe', 'Data', 'Ora', 'Titolo', 'Tipo', 'Percorso cartella', 'Link Moduli ragazzi',
  'Link file risposte (PDF)', 'Link foglio risultati', 'Scala voto', 'Punti totali', 'Stato', 'Note'];

// Funzione pura (provata in locale). Colonne 8, 9, 10 (indici 7, 8, 9) = link.
function apRigaIndice_(q, linkPdf, linkRis) {
  var stato = (linkPdf && linkRis) ? 'Archiviata' : 'Da archiviare (PDF e risultati da inserire)';
  return [AP_ANNO, q.classe, q.data, q.ora, q.titoloIndice || q.titolo, q.tipo || 'Quiz', apPercorso_(q),
    q.moduliUrl || AP_ND, linkPdf || AP_ND, linkRis || AP_ND,
    '50-70 lineare: 50 + 20 x punti / ' + q.totale, q.totale, stato,
    'Riga scritta dallo script archivia-prove v1.1; link del Moduli dal pacchetto Classroom, non provato aperto come allievo.'];
}

function apLink_(url) { return (url && url !== AP_ND) ? '=HYPERLINK("' + String(url).replace(/"/g, '""') + '","Apri")' : AP_ND; }

function apIndice_(regge, indice, scrivi, log) {
  var it = regge.getFilesByName(AP_INDICE_NOME), ss = null;
  if (it.hasNext()) ss = SpreadsheetApp.open(it.next());
  else if (!scrivi) { log('Creerei il foglio «' + AP_INDICE_NOME + '» nella cartella «' + regge.getName() + '».'); }
  else { ss = SpreadsheetApp.create(AP_INDICE_NOME); DriveApp.getFileById(ss.getId()).moveTo(regge); log('Creato il foglio «' + AP_INDICE_NOME + '»: ' + ss.getUrl()); }
  if (!ss) return;
  var sh = ss.getSheetByName('Indice') || ss.insertSheet('Indice');
  if (sh.getRange(1, 1).getValue() !== AP_INDICE_TESTA[0]) {
    sh.getRange(1, 1, 1, AP_INDICE_TESTA.length).setValues([AP_INDICE_TESTA]);
    sh.getRange(1, 1, 1, AP_INDICE_TESTA.length).setFontWeight('bold').setBackground('#1F3864').setFontColor('#FFFFFF');
    sh.setFrozenRows(1); sh.setFrozenColumns(5);
    [14, 9, 12, 7, 36, 12, 62, 24, 24, 24, 34, 11, 22, 60].forEach(function (w, i) { sh.setColumnWidth(i + 1, w * 7); });
  }
  var perc = sh.getLastRow() > 1 ? sh.getRange(2, 7, sh.getLastRow() - 1, 1).getValues().map(function (r) { return r[0]; }) : [];
  indice.forEach(function (x) {
    var riga = apRigaIndice_(x.q, x.linkPdf, x.linkRis), n = perc.indexOf(riga[6]);
    var r = n >= 0 ? n + 2 : sh.getLastRow() + 1;
    if (n >= 0) {
      // riga gia presente: i link gia scritti dal docente restano (si riempie solo dove c'e «da inserire» o vuoto)
      for (var c = 8; c <= 10; c++) {
        var cella = sh.getRange(r, c), f = cella.getFormula(), v = String(cella.getValue() || '');
        if (f || (v && v !== AP_ND)) riga[c - 1] = f || v;
      }
    }
    sh.getRange(r, 1, 1, riga.length).setValues([riga]);
    [8, 9, 10].forEach(function (c) { var v = riga[c - 1]; if (String(v).charAt(0) === '=') return; var l = apLink_(v); if (l === AP_ND) sh.getRange(r, c).setValue(AP_ND); else sh.getRange(r, c).setFormula(l); });
    sh.getRange(r, 3).setNumberFormat('yyyy-mm-dd'); sh.getRange(r, 4).setNumberFormat('@');
    log('Indice: riga ' + r + ' ' + (n >= 0 ? 'aggiornata' : 'aggiunta') + ' per ' + apPercorso_(x.q) + '.');
    if (n < 0) perc.push(riga[6]);
  });
  if (!sh.getFilter()) sh.getRange(1, 1, Math.max(sh.getLastRow(), 2), AP_INDICE_TESTA.length).createFilter();
}

// ---------------------------------------------------------------- foglio dei risultati
function apRisultati_(q, cartella, scrivi, log) {
  var fab = SpreadsheetApp.openById(AP_FOGLIO_FABBRICA_ID);
  var sh = fab.getSheetByName('Risposte ' + q.id);
  if (!sh) { log(q.classe + ': la scheda «Risposte ' + q.id + '» non c\'e ancora nel foglio Fabbrica (nessuna risposta arrivata o giro del motore non fatto).'); return ''; }
  var valori = sh.getDataRange().getValues();
  var r = apAggrega_(valori, q);
  log(q.classe + ': ' + r.righe.length + ' allievi con almeno un invio, ' + r.provvisori + ' con discorsive da correggere (fonte: scheda «Risposte ' + q.id + '», letta ' + Utilities.formatDate(new Date(), 'Europe/Rome', 'dd/MM/yyyy HH:mm') + ').');
  if (!scrivi || !cartella) return '';
  var nome = 'Risultati ' + q.classe + ' - ' + q.titolo;
  var it = cartella.getFilesByName(nome), ss;
  if (it.hasNext()) ss = SpreadsheetApp.open(it.next());
  else { ss = SpreadsheetApp.create(nome); DriveApp.getFileById(ss.getId()).moveTo(cartella); }
  apScrivi_(ss, 'Voti', r.testa, r.righe);
  apScrivi_(ss, 'Risposte', null, valori);
  var primo = ss.getSheetByName('Foglio1') || ss.getSheetByName('Sheet1');
  if (primo && ss.getSheets().length > 1) ss.deleteSheet(primo); // solo il foglio vuoto creato da SpreadsheetApp.create
  log(q.classe + ': foglio dei risultati aggiornato: ' + ss.getUrl());
  return ss.getUrl();
}

function apScrivi_(ss, nome, testa, righe) {
  var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  sh.clearContents();
  var tutte = testa ? [testa].concat(righe) : righe;
  if (!tutte.length) return;
  var colonne = 0; tutte.forEach(function (r) { if (r.length > colonne) colonne = r.length; });
  tutte = tutte.map(function (r) { var c = r.slice(); while (c.length < colonne) c.push(''); return c; });
  sh.getRange(1, 1, tutte.length, colonne).setValues(tutte);
  if (testa) sh.getRange(1, 1, 1, testa.length).setFontWeight('bold');
  sh.setFrozenRows(testa ? 1 : 0);
}

// ---------------------------------------------------------------- calcolo (funzioni pure, provate in locale)
function apVoto_(tot, totale) { return Math.floor((50 + 20 * tot / totale) * 2 + 0.5) / 2; }
function apNum_(x) { return (typeof x === 'number' && isFinite(x)) ? x : null; }
function apFmt_(x) { return String(x).replace('.', ','); }

// valori = getValues() della scheda «Risposte <id>»: riga di intestazione con «Ora invio», colonne Allievo, Email, P1..Pn.
// Ritorna { testa, righe, provvisori }. Una riga per allievo: conta l'invio con piu punti (a pari punti, l'ultimo).
function apAggrega_(valori, q) {
  var h = -1, i, k;
  for (i = 0; i < valori.length; i++) if (String(valori[i][0]) === 'Ora invio') { h = i; break; }
  var testa = ['Allievo', 'Email', 'Invii', 'Punti caselle (su ' + 0 + ')', 'Punti discorsive', 'Discorsive da correggere', 'Totale (su ' + q.totale + ')', 'Voto proposto 50-70', 'Stato', 'Conto del voto'];
  var maxCh = 0;
  if (h < 0) return { testa: testa, righe: [], provvisori: 0 };
  var inte = valori[h].map(String), cA = inte.indexOf('Allievo'), cE = inte.indexOf('Email'), cP = inte.indexOf('P1');
  var nTot = 0; while (inte.indexOf('P' + (nTot + 1)) >= 0) nTot++;
  if (cA < 0 || cE < 0 || cP < 0 || nTot < q.nChiuse) throw new Error('Intestazione della scheda Risposte <' + q.id + '> inattesa: servono Allievo, Email, P1..P' + q.nChiuse + '.');
  var rigaMax = h > 0 ? valori[h - 1] : [];
  for (k = 0; k < q.nChiuse; k++) { var m = /max\s+([\d.,]+)/.exec(String(rigaMax[cP + k] || '')); maxCh += m ? parseFloat(m[1].replace(',', '.')) : 0; }
  testa[3] = 'Punti caselle' + (maxCh ? ' (su ' + maxCh + ')' : '');
  var per = {};
  for (i = h + 1; i < valori.length; i++) {
    var r = valori[i];
    if (!String(r[cE] || '').trim() && !String(r[cA] || '').trim()) continue;
    var ch = 0, di = 0, pend = 0;
    for (k = 0; k < nTot; k++) {
      var p = apNum_(r[cP + k]);
      if (k < q.nChiuse) { if (p !== null) ch += p; }
      else if (p !== null) di += p; else pend++;
    }
    var chiave = String(r[cE] || '').trim().toLowerCase() || String(r[cA]).trim();
    var d = per[chiave] || (per[chiave] = { nome: String(r[cA] || '').trim(), email: String(r[cE] || '').trim(), invii: 0, best: null });
    d.invii++;
    if (!d.nome && String(r[cA] || '').trim()) d.nome = String(r[cA]).trim();
    if (!d.best || ch + di >= d.best.ch + d.best.di) d.best = { ch: ch, di: di, pend: pend };
  }
  var righe = [], prov = 0;
  Object.keys(per).forEach(function (c) {
    var d = per[c], tot = d.best.ch + d.best.di, v = apVoto_(tot, q.totale), pr = d.best.pend > 0;
    if (pr) prov++;
    righe.push([d.nome || 'NON ABBINATA', d.email, d.invii, d.best.ch, d.best.di, d.best.pend, tot, v, pr ? 'PROVVISORIO' : 'DEFINITIVO',
      '50 + 20 x ' + apFmt_(tot) + ' / ' + q.totale + ' = ' + apFmt_(50 + 20 * tot / q.totale) + ' -> ' + apFmt_(v)]);
  });
  righe.sort(function (a, b) { return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0; });
  return { testa: testa, righe: righe, provvisori: prov };
}

if (typeof module !== 'undefined') module.exports = { apAggrega_: apAggrega_, apVoto_: apVoto_, apRigaIndice_: apRigaIndice_, apPercorso_: apPercorso_, apNomeProva_: apNomeProva_, apLink_: apLink_, AP_ELENCO: AP_ELENCO, AP_INDICE_TESTA: AP_INDICE_TESTA };
