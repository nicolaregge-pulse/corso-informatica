/**
 * AUTOMAZIONE CORSO v7.7 (16/10/2026) — gira DA SOLA ogni minuto (timer di Google) sull'account SCUOLA.
 * v7.7: SI RIPARA DA SOLO. Il timer di Google a volte si spegne: ora ogni contatto del web app (doGet/doPost)
 *       chiama AUTO_assicuraTimer() che lo ricrea se manca. In piu' l'azione «classroom.annuncio_cancella»
 *       permette di cancellare un annuncio (test e pulizia; mai il lavoro degli allievi).
 * v7.6: RETE DI SICUREZZA. Ogni consegna va sempre nel Foglio di riserva; la pagina del ragazzo dice «arrivata»
 *       solo se la consegna e' al sicuro (Git o riserva), mai a vuoto. AUTO_recuperaArrivi() ripesca dalla
 *       riserva e carica su Git le consegne cadute (ramo occupato): si lancia a mano, riusabile all'infinito.
 * Git e' la zona di scambio con l'AI (repo privato corso-informatica-riservato):
 *
 *   1. PUBBLICA: l'AI mette in coda/ un file .json con stato "da-pubblicare" (titolo, PDF,
 *      Google Doc del compito, scadenza). Lo script crea cartella Drive + PDF + Doc (copia per
 *      ogni allievo) e pubblica il compito su Classroom. Stato -> "pubblicato".
 *   2. CHIUDE: passata la scadenza (+10 minuti) deposita le consegne (PDF + TXT) in
 *      dati/consegne/<CLASSE>/<cartella>/ . Stato -> "chiuso". Poi l'AI genera libri e griglie.
 *   3. TESTO SEMPRE AGGIORNATO (v2): se nel .json l'AI alza "testo_rev" e cambia "testo", lo script
 *      aggiorna le Istruzioni del compito. Se il compito e' stato creato A MANO (Classroom non lo
 *      lascia modificare allo script) pubblica invece un ANNUNCIO con il testo nuovo.
 *   4. RACCOLTE IN PIU' (v2): "raccolte": ["2026-10-05T12:00:00Z", ...] -> a ogni ora passata
 *      ri-deposita le consegne (chi consegna in ritardo entra lo stesso), anche dopo "chiuso".
 *   5. SITUAZIONE (v2): per i compiti aperti scrive dati/situazione/<CLASSE>_<cartella>.md con chi
 *      ha consegnato e chi no (solo quando cambia qualcosa).
 *   6. VOTI (v3): se nel .json l'AI mette "voti": {"Cognome Nome": 75, ...} e alza "voti_rev", lo
 *      script scrive i voti su Classroom come BOZZA (il docente li controlla e preme "Restituisci").
 *      "voti_su": 100 porta prima il punteggio massimo del compito a 100 (centesimi).
 *      Solo con "voti_restituisci": true li restituisce anche ai ragazzi.
 *      FUNZIONA SOLO sui compiti creati dallo script: quelli creati a mano Classroom non li lascia toccare.
 *   7. QUIZ SU MODULI (v4): se nel .json c'e' "quiz": {versioni, domande, punti, descrizione}, lo script
 *      crea da solo i Moduli-quiz (una versione per lettera, domande mescolate per ogni ragazzo,
 *      punteggio automatico), li mette nella cartella Drive del compito, li allega al compito su
 *      Classroom e scrive i link al posto di {A} {B} {C} nel testo. Alla chiusura (e a ogni raccolta
 *      in piu') deposita i risultati in dati/consegne/<CLASSE>/<cartella>/_RISULTATI-QUIZ.csv e .json.
 *   8. PONTE GOOGLE (v5): l'AI mette in comandi/ un .json con "stato": "da-eseguire" e una lista di
 *      "azioni" su Drive, Moduli, Fogli, Documenti, Classroom e Gmail (solo BOZZE). Lo script le esegue,
 *      scrive i risultati nello stesso file (stato "eseguito" o "errore") e salva gli export nel repo.
 *      Cosi' l'AI legge e scrive su tutta la suite Google in tutte e due le direzioni.
 *  10. PERCORSO A SCHERMATE (v7): azione "forms.crea_percorso" (una domanda per pagina, crocette corrette da sole,
 *      domanda scritta finale, immagine facoltativa).
 *  11. CONSEGNA DELLA VERIFICA CON UN CLIC (v7.4): lo script è anche una piccola pagina web (Distribuisci ->
 *      Applicazione web). La verifica HTML, quando il ragazzo clicca «Consegna», manda il risultato a questa pagina,
 *      che lo salva su Git in dati/verifiche/<id>/arrivi/ e risponde «Consegna arrivata al prof». Niente copia, incolla e Modulo.
 *   9. MODULI CON RISPOSTE SCRITTE (v6): azioni "forms.crea_modulo" (domande a testo, email della scuola
 *      raccolta da Google, una sola risposta per account: es. «Scegli la password del tuo libro») e
 *      "forms.risposte_testo" (salva le risposte grezze nel repo riservato, abbinate all'email).
 *      PER SICUREZZA il ponte NON cancella niente, NON condivide fuori dalla scuola e NON invia mail
 *      (crea solo bozze in Gmail: le invia il docente).
 *
 * SETUP (UNA VOLTA SOLA): incolla questo file nel progetto "Consegne Classroom → Git"
 * (che ha gia' il servizio Classroom e GITHUB_TOKEN), poi Esegui -> attivaAutomatico.
 * Tutto ha il prefisso AUTO_ per non pestare le funzioni degli altri file del progetto.
 */
var AUTO = {
  REPO: 'nicolaregge-pulse/corso-informatica-riservato',
  BRANCH: 'main',
  CODA: 'coda',
  DIZIONARIO: 'config/classi.json',
  MINUTI_DOPO_SCADENZA: 10
};

/* ====================== DA ESEGUIRE UNA VOLTA ====================== */
function attivaAutomatico() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'autoCiclo') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('autoCiclo').timeBased().everyMinutes(1).create();  // v7.1: ogni minuto
  Logger.log('Timer ATTIVO: autoCiclo ogni minuto. Ora faccio subito il primo giro...');
  autoCiclo();
}

function disattivaAutomatico() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'autoCiclo') ScriptApp.deleteTrigger(t);
  });
  Logger.log('Timer DISATTIVATO.');
}

/* v7.7 — SI RIPARA DA SOLO: se il timer di autoCiclo non c'e' piu' (Google a volte lo spegne),
   lo ricrea. Viene chiamato a ogni contatto del web app (doGet/doPost): cosi' qualunque
   attivita' (una consegna, una visita alla pagina) tiene vivo il ponte. Idempotente. */
function AUTO_assicuraTimer() {
  try {
    var c = ScriptApp.getProjectTriggers().filter(function (t) { return t.getHandlerFunction() === 'autoCiclo'; });
    if (c.length === 0) { ScriptApp.newTrigger('autoCiclo').timeBased().everyMinutes(1).create(); Logger.log('Timer RI-CREATO (self-healing).'); }
    else if (c.length > 1) { c.slice(1).forEach(function (t) { ScriptApp.deleteTrigger(t); }); }  // niente doppioni
  } catch (e) { Logger.log('AUTO_assicuraTimer: ' + e); }
}


/* v7.1 — SUBITO, senza aspettare il timer: quando un ragazzo preme «Invia» in un Modulo, le risposte vanno su Git all'istante.
   Da eseguire UNA volta: Esegui -> attivaInvioModuli. Moduli e cartelle in AUTO_MODULI_LIVE. */
var AUTO_MODULI_LIVE = {
  '1p8YarftHXjSEObPFbo7WlOxzX-EBpEF5Xx-WqKo5ixI': 'dati/consegne/_modulo-consegna/risposte.json',
  '1JVn38PZHdEKSA7LpUpWLiyUi0_72TMRehtFEYpAnz4o': 'dati/consegne/3INF/2026-10/20261012_parere-teoria/risposte.json',
  '1FVAspj6QiC_8cnvSq1xWQE_gBKbz8RTsb51srR2wc3M': 'dati/consegne/2INF/2026-10/20261012_parere-teoria/risposte.json'
};
/* v7.3 — l'elenco dei Moduli «live» sta anche su Git: config/moduli-live.json ({"id del Modulo": "percorso delle risposte"}).
   Lo script lo legge e, ogni 10 minuti, attiva da solo l'invio immediato per i Moduli nuovi e lo toglie a quelli tolti
   dall'elenco: per aggiungere un Modulo NON serve più ricopiare lo script né premere «Esegui». */
function AUTO_moduliLive() {
  var m = {};
  Object.keys(AUTO_MODULI_LIVE).forEach(function (k) { m[k] = AUTO_MODULI_LIVE[k]; });
  try {
    var j = AUTO_leggiJson('config/moduli-live.json').json;
    Object.keys(j).forEach(function (k) { if (k.charAt(0) !== '_') { if (j[k]) m[k] = j[k]; else delete m[k]; } });
  } catch (e) { Logger.log('config/moduli-live.json non letto: ' + e); }
  return m;
}
function AUTO_allineaInvio(subito) {
  var p = PropertiesService.getScriptProperties(), ora = Date.now();
  if (!subito && ora - Number(p.getProperty('ULTIMO_ALLINEA') || 0) < 10 * 60 * 1000) return 0;
  p.setProperty('ULTIMO_ALLINEA', String(ora));
  var m = AUTO_moduliLive(), gia = {}, n = 0, tolti = 0;
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() !== 'AUTO_suInvio') return;
    var id = t.getTriggerSourceId();
    if (!m[id] || gia[id]) { ScriptApp.deleteTrigger(t); tolti++; } else gia[id] = true;
  });
  Object.keys(m).forEach(function (id) {
    if (gia[id]) return;
    try { ScriptApp.newTrigger('AUTO_suInvio').forForm(id).onFormSubmit().create(); n++; }
    catch (e) { Logger.log('Invio immediato NON attivato per ' + id + ': ' + e); }
  });
  Logger.log('Invio immediato: ' + Object.keys(m).length + ' moduli nell\'elenco, ' + n + ' attivati ora, ' + tolti + ' tolti.');
  return n;
}
function attivaInvioModuli() { AUTO_allineaInvio(true); }
function AUTO_suInvio(e) {
  var fr = e.source, id = fr.getId(), dove = AUTO_moduliLive()[id];
  if (!dove) return;
  var righe = fr.getResponses().map(function (r) {
    var o = { email: r.getRespondentEmail(), ora: r.getTimestamp().toISOString(), risposte: {} };
    r.getItemResponses().forEach(function (ir) { o.risposte[ir.getItem().getTitle()] = String(ir.getResponse()); });
    return o; });
  AUTO_commit(dove, Utilities.newBlob(JSON.stringify(righe, null, 1), 'application/json', 'risposte.json'), 'Invio immediato: ' + fr.getTitle());
}

/* ====================== IL GIRO AUTOMATICO ====================== */
function autoCiclo() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(2000)) { Logger.log('Giro precedente ancora in corso: salto.'); return; }
  try {
    var r = AUTO_gh('get', '/contents/' + AUTO.CODA + '?ref=' + AUTO.BRANCH);
    if (r.getResponseCode() === 404) { Logger.log('Coda vuota.'); return; }
    if (r.getResponseCode() !== 200) { Logger.log('GitHub risponde ' + r.getResponseCode() + ': ' + r.getContentText().slice(0, 300)); return; }   // v7.2
    var files = JSON.parse(r.getContentText()).filter(function (f) { return /\.json$/.test(f.name); });
    var adesso = new Date(), fatto = 0;
    files.forEach(function (f) {
      var item = AUTO_leggiJson(f.path);
      var job = item.json;
      try {
        if (job.stato === 'pubblicato' || job.stato === 'chiuso') {
          var cambi = AUTO_extra(job, adesso);
          if (cambi) { AUTO_scriviJson(f.path, job, item.sha, cambi + ': ' + job.titolo); item = AUTO_leggiJson(f.path); job = item.json; fatto++; }
        }
        if (job.stato === 'da-pubblicare') {
          // REGOLA §2.38: si pubblica SOLO il lavoro del giorno (data in testa al nome del file)
          var oggi = Utilities.formatDate(adesso, 'Europe/Rome', 'yyyy-MM-dd');
          if (f.name.indexOf(oggi) !== 0) { Logger.log('NON pubblico ' + f.name + ': non e\' un lavoro di oggi (' + oggi + ').'); return; }
          AUTO_pubblica(job);
          job.stato = 'pubblicato'; job.pubblicato_il = adesso.toISOString();
          AUTO_scriviJson(f.path, job, item.sha, 'Pubblicato su Classroom: ' + job.titolo); fatto++;
        } else if (job.stato === 'pubblicato' &&
                   adesso.getTime() > new Date(job.scadenza_iso).getTime() + AUTO.MINUTI_DOPO_SCADENZA * 60000) {
          var esito = AUTO_chiudi(job);
          job.stato = 'chiuso'; job.chiuso_il = adesso.toISOString(); job.esito_chiusura = esito;
          AUTO_scriviJson(f.path, job, item.sha, 'Chiuso e depositato: ' + job.titolo); fatto++;
        }
      } catch (e) {
        Logger.log('ERRORE su ' + f.name + ': ' + e);
      }
    });
    try { fatto += AUTO_comandi(); } catch (e) { Logger.log('ERRORE ponte Google: ' + e); }   // v5
    try { AUTO_allineaInvio(false); } catch (e) { Logger.log('ERRORE invio immediato: ' + e); }   // v7.3
    Logger.log('Giro finito. Azioni fatte: ' + fatto + ' (file in coda: ' + files.length + ')');
  } finally { lock.releaseLock(); }
}

/* ====================== 1. PUBBLICA ====================== */
function AUTO_pubblica(job) {
  var courseId = AUTO_courseId(job.classe);
  // sicurezza anti-doppione: se un compito con lo stesso titolo c'e' gia', lo adotto
  var esist = (Classroom.Courses.CourseWork.list(courseId, { pageSize: 50 }).courseWork || [])
              .filter(function (w) { return w.title === job.titolo; });
  if (esist.length) {
    job.course_id = courseId; job.coursework_id = esist[0].id; job.link = esist[0].alternateLink;
    Logger.log('Gia\' presente su Classroom, lo adotto: ' + job.titolo); return;
  }
  var cart = AUTO_cartella(job.cartella_drive || job.titolo);
  var materiali = [];
  (job.pdf || []).forEach(function (n) {
    var r = UrlFetchApp.fetch(job.base_url + n, { muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) throw new Error('PDF non scaricato: ' + n + ' (' + r.getResponseCode() + ')');
    var f = cart.createFile(r.getBlob().setName(n));
    materiali.push({ driveFile: { driveFile: { id: f.getId() }, shareMode: 'VIEW' } });
  });
  if (job.doc) {
    var doc = AUTO_creaDoc(job.titolo, job.doc);
    DriveApp.getFileById(doc.getId()).moveTo(cart);
    materiali.unshift({ driveFile: { driveFile: { id: doc.getId() }, shareMode: 'STUDENT_COPY' } });
  }
  if (job.quiz && !job.moduli) {                       // v4: quiz su Moduli creati in automatico
    job.moduli = AUTO_creaQuiz(job, cart);
    var testo = job.descrizione || '';
    job.moduli.forEach(function (m) {
      testo = testo.split('{' + m.versione + '}').join(m.compila);
      materiali.push({ link: { url: m.compila } });
    });
    job.descrizione = testo;
  }
  var s = new Date(job.scadenza_iso);
  var work = {
    title: job.titolo, description: job.descrizione || '', workType: 'ASSIGNMENT', state: 'PUBLISHED',
    materials: materiali,
    dueDate: { year: s.getUTCFullYear(), month: s.getUTCMonth() + 1, day: s.getUTCDate() },
    dueTime: { hours: s.getUTCHours(), minutes: s.getUTCMinutes() }
  };
  if (job.punti) work.maxPoints = job.punti;
  var c = Classroom.Courses.CourseWork.create(work, courseId);
  job.course_id = courseId; job.coursework_id = c.id; job.link = c.alternateLink;
  Logger.log('PUBBLICATO ' + job.classe + ': ' + c.title + ' -> ' + c.alternateLink);
}

function AUTO_creaDoc(titolo, blocchi) {
  var doc = DocumentApp.create(titolo), b = doc.getBody();
  var H = { h1: DocumentApp.ParagraphHeading.HEADING1, h2: DocumentApp.ParagraphHeading.HEADING2,
            h3: DocumentApp.ParagraphHeading.HEADING3 };
  blocchi.forEach(function (k) {
    if (k.t === 'tab') {
      var t = b.appendTable(k.rows);
      (k.w || []).forEach(function (w, i) { t.setColumnWidth(i, w); });
      t.getRow(0).editAsText().setBold(true);
    } else {
      var p = b.appendParagraph(k.x);
      if (H[k.t]) p.setHeading(H[k.t]);
    }
  });
  doc.saveAndClose();
  return doc;
}

function AUTO_cartella(nome) {
  var it = DriveApp.getFoldersByName(nome);
  return it.hasNext() ? it.next() : DriveApp.createFolder(nome);
}

/* ====================== 3-4-5. TESTO, RACCOLTE IN PIU', SITUAZIONE ====================== */
function AUTO_extra(job, adesso) {
  var cosa = [];
  if (job.testo && (job.testo_rev || 0) > (job.testo_applicato_rev || 0)) {
    try {
      Classroom.Courses.CourseWork.patch({ description: job.testo }, job.course_id, job.coursework_id, { updateMask: 'description' });
      job.testo_modo = 'istruzioni';
    } catch (e) {
      Classroom.Courses.Announcements.create({ text: job.titolo.toUpperCase() + ' - ISTRUZIONI AGGIORNATE\n\n' + job.testo, state: 'PUBLISHED' }, job.course_id);
      job.testo_modo = 'annuncio';
    }
    job.testo_applicato_rev = job.testo_rev; job.testo_applicato_il = adesso.toISOString(); cosa.push('Testo aggiornato');
  }
  var fatte = job.raccolte_fatte || [];
  (job.raccolte || []).forEach(function (t) {
    if (fatte.indexOf(t) < 0 && adesso.getTime() > new Date(t).getTime()) {
      job.esito_ultima_raccolta = AUTO_chiudi(job); fatte.push(t); cosa.push('Raccolta in piu');
    }
  });
  job.raccolte_fatte = fatte;
  if (job.voti && (job.voti_rev || 0) > (job.voti_applicati_rev || 0)) {
    job.esito_voti = AUTO_voti(job);
    job.voti_applicati_rev = job.voti_rev; job.voti_applicati_il = adesso.toISOString(); cosa.push('Voti in bozza');
  }
  if (job.stato === 'pubblicato' && job.situazione !== false) AUTO_situazione(job);
  return cosa.join(' + ');
}

function AUTO_situazione(job) {
  var subs = (Classroom.Courses.CourseWork.StudentSubmissions.list(job.course_id, job.coursework_id).studentSubmissions) || [];
  var righe = subs.map(function (s) {
    var st = { TURNED_IN: 'CONSEGNATO', RETURNED: 'RESTITUITO', CREATED: 'non consegnato', NEW: 'non consegnato', RECLAIMED_BY_STUDENT: 'ritirato' }[s.state] || s.state;
    var n = ((s.assignmentSubmission && s.assignmentSubmission.attachments) || []).length;
    return '| ' + AUTO_nome(s.userId) + ' | ' + st + ' | ' + n + ' |';
  }).sort();
  var ok = righe.filter(function (r) { return r.indexOf('CONSEGNATO') >= 0 || r.indexOf('RESTITUITO') >= 0; }).length;
  var md = '# ' + job.classe + ' - ' + job.titolo + ' (RISERVATO)\n\nConsegnati: ' + ok + ' / ' + subs.length +
           '\n\n| Allievo | Stato | Allegati |\n|---|---|---|\n' + righe.join('\n') + '\n';
  var path = 'dati/situazione/' + job.classe + '_' + (job.cartella || AUTO_slug(job.titolo)) + '.md';
  var enc = path.split('/').map(encodeURIComponent).join('/');
  var get = AUTO_gh('get', '/contents/' + enc + '?ref=' + AUTO.BRANCH);
  if (get.getResponseCode() === 200) {
    var vecchio = Utilities.newBlob(Utilities.base64Decode(JSON.parse(get.getContentText()).content.replace(/\s/g, ''))).getDataAsString('UTF-8');
    if (vecchio === md) return;
  }
  AUTO_commit(path, Utilities.newBlob(md, 'text/markdown'), 'Situazione ' + job.classe + ': ' + ok + '/' + subs.length);
}

/* ====================== 6. VOTI (bozza su Classroom) ====================== */
function AUTO_voti(job) {
  var W = Classroom.Courses.CourseWork, S = W.StudentSubmissions;
  if (job.voti_su && W.get(job.course_id, job.coursework_id).maxPoints !== job.voti_su) {
    W.patch({ maxPoints: job.voti_su }, job.course_id, job.coursework_id, { updateMask: 'maxPoints' });
  }
  var subs = (S.list(job.course_id, job.coursework_id, { pageSize: 100 }).studentSubmissions) || [];
  var esito = { messi: 0, non_trovati: [], doppi: [] };
  Object.keys(job.voti).forEach(function (nome) {
    var voto = job.voti[nome];
    if (voto === null || voto === '') return;
    var miei = AUTO_parole(nome);
    var trovati = subs.filter(function (s) {
      var suoi = AUTO_parole(AUTO_nome(s.userId));
      return miei.every(function (p) { return suoi.indexOf(p) >= 0; });
    });
    if (trovati.length === 0) { esito.non_trovati.push(nome); return; }
    if (trovati.length > 1) { esito.doppi.push(nome); return; }
    var sub = trovati[0], campi = { draftGrade: voto }, mask = 'draftGrade';
    if (job.voti_restituisci) { campi.assignedGrade = voto; mask += ',assignedGrade'; }
    S.patch(campi, job.course_id, job.coursework_id, sub.id, { updateMask: mask });
    if (job.voti_restituisci) S['return']({}, job.course_id, job.coursework_id, sub.id);
    esito.messi++;
  });
  Logger.log('VOTI ' + job.classe + ' - ' + job.titolo + ': messi ' + esito.messi + ', non trovati ' + esito.non_trovati.join(', '));
  return esito;
}

function AUTO_parole(nome) {
  return AUTO_slug(nome).split('-').filter(function (p) { return p.length > 1; });
}

/* ====================== 2. CHIUDE (deposita le consegne) ====================== */
function AUTO_chiudi(job) {
  var subs = (Classroom.Courses.CourseWork.StudentSubmissions
              .list(job.course_id, job.coursework_id).studentSubmissions) || [];
  var base = 'dati/consegne/' + job.classe + '/' + (job.cartella || AUTO_slug(job.titolo));
  var nFile = 0, consegnati = 0;
  subs.forEach(function (s) {
    if (s.state !== 'TURNED_IN' && s.state !== 'RETURNED') return;
    consegnati++;
    var nome = AUTO_nome(s.userId).replace(/[\\\/:*?"<>|]/g, '_');
    var atts = (s.assignmentSubmission && s.assignmentSubmission.attachments) || [];
    atts.forEach(function (a, i) {
      try {
        if (!(a.driveFile && a.driveFile.id)) return;
        var id = a.driveFile.id, f = DriveApp.getFileById(id), mt = f.getMimeType();
        var suff = (atts.length > 1 ? ('_' + (i + 1)) : '');
        if (mt.indexOf('application/vnd.google-apps.document') === 0) {
          AUTO_commit(base + '/' + nome + suff + '.pdf', f.getAs('application/pdf'), 'Consegna ' + job.classe + ' - ' + nome);
          var txt = DocumentApp.openById(id).getBody().getText();
          AUTO_commit(base + '/' + nome + suff + '.txt', Utilities.newBlob(txt, 'text/plain', nome + '.txt'), 'Testo consegna ' + job.classe + ' - ' + nome);
          nFile += 2;
        } else if (mt.indexOf('application/vnd.google-apps') === 0) {
          AUTO_commit(base + '/' + nome + suff + '.pdf', f.getAs('application/pdf'), 'Consegna ' + job.classe + ' - ' + nome); nFile++;
        } else {
          var ext = (f.getName().indexOf('.') >= 0 ? f.getName().split('.').pop() : 'bin');
          AUTO_commit(base + '/' + nome + suff + '.' + ext, f.getBlob(), 'Consegna ' + job.classe + ' - ' + nome); nFile++;
        }
      } catch (e) { Logger.log('Errore su ' + nome + ': ' + e); }
    });
  });
  var idx = 'Classe: ' + job.classe + '\nCompito: ' + job.titolo + '\nCOURSEWORK_ID: ' + job.coursework_id +
            '\nConsegnati: ' + consegnati + ' / ' + subs.length + '\nData: ' + new Date().toISOString();
  AUTO_commit(base + '/_INDICE.txt', Utilities.newBlob(idx, 'text/plain', '_INDICE.txt'), 'Indice consegne ' + job.classe + ' - ' + job.titolo);
  var quiz = job.moduli ? AUTO_risultatiQuiz(job, base) : null;   // v4
  Logger.log('CHIUSO ' + job.classe + ': ' + job.titolo + ' | consegnati ' + consegnati + '/' + subs.length);
  return { consegnati: consegnati, iscritti: subs.length, file: nFile, cartella: base, quiz: quiz };
}

/* ====================== QUIZ SU MODULI (v4) ====================== */
function AUTO_mescola(arr, seme) {
  var a = arr.slice(), s = seme;
  for (var i = a.length - 1; i > 0; i--) {
    s = (s * 9301 + 49297) % 233280;
    var j = Math.floor(s / 233280 * (i + 1));
    var t = a[i]; a[i] = a[j]; a[j] = t;
  }
  return a;
}

function AUTO_creaQuiz(job, cart) {
  var q = job.quiz, vers = q.versioni || ['A'], out = [];
  vers.forEach(function (v, iv) {
    var form = FormApp.create((q.titolo || job.titolo) + (vers.length > 1 ? ' — Versione ' + v : ''))
      .setIsQuiz(true)
      .setShuffleQuestions(q.mescola !== false)
      .setCollectEmail(true)
      .setLimitOneResponsePerUser(true)
      .setDescription((q.descrizione || '') + (vers.length > 1 ? ' Versione ' + v + '.' : ''));
    form.addTextItem().setTitle('Nome e cognome').setRequired(true);
    q.domande.forEach(function (d, n) {
      var r = d[v] || d.A, item = form.addMultipleChoiceItem();
      var scelte = AUTO_mescola([[r[1], true]].concat(r[2].map(function (x) { return [x, false]; })), (n + 1) * 31 + iv * 977);
      item.setTitle(r[0]).setPoints(q.punti || 5).setRequired(true)
          .setChoices(scelte.map(function (c) { return item.createChoice(c[0], c[1]); }));
    });
    DriveApp.getFileById(form.getId()).moveTo(cart);
    out.push({ versione: v, id: form.getId(), compila: form.getPublishedUrl(), modifica: form.getEditUrl() });
    Logger.log('QUIZ ' + v + ' creato: ' + form.getPublishedUrl());
  });
  return out;
}

function AUTO_risultatiQuiz(job, base) {
  var righe = ['versione;email;nome;punteggio;massimo;ora'], det = [];
  job.moduli.forEach(function (m) {
    var f = FormApp.openById(m.id), max = 0;
    f.getItems().forEach(function (it) {
      if (it.getType() === FormApp.ItemType.MULTIPLE_CHOICE) max += it.asMultipleChoiceItem().getPoints();
    });
    f.getResponses().forEach(function (r) {
      var nome = '', tot = 0, sbagliate = [];
      r.getItemResponses().forEach(function (ir) {
        if (ir.getItem().getType() === FormApp.ItemType.TEXT) nome = String(ir.getResponse());
      });
      r.getGradableItemResponses().forEach(function (g) {
        var sc = g.getScore() || 0; tot += sc;
        if (!sc) sbagliate.push(g.getItem().getTitle());
      });
      righe.push([m.versione, r.getRespondentEmail(), nome.replace(/;/g, ','), tot, max, r.getTimestamp().toISOString()].join(';'));
      det.push({ versione: m.versione, email: r.getRespondentEmail(), nome: nome, punteggio: tot, massimo: max, sbagliate: sbagliate });
    });
  });
  AUTO_commit(base + '/_RISULTATI-QUIZ.csv', Utilities.newBlob(righe.join('\n'), 'text/plain', '_RISULTATI-QUIZ.csv'), 'Risultati quiz ' + job.classe + ' - ' + job.titolo);
  AUTO_commit(base + '/_RISULTATI-QUIZ.json', Utilities.newBlob(JSON.stringify(det, null, 1), 'application/json', '_RISULTATI-QUIZ.json'), 'Dettaglio quiz ' + job.classe + ' - ' + job.titolo);
  return { risposte: det.length };
}

/* ====================== 8. PONTE GOOGLE (v5) ====================== */
function AUTO_comandi() {
  var r = AUTO_gh('get', '/contents/comandi?ref=' + AUTO.BRANCH);
  if (r.getResponseCode() !== 200) return 0;
  var n = 0;
  JSON.parse(r.getContentText()).filter(function (f) { return /\.json$/.test(f.name); }).forEach(function (f) {
    var item = AUTO_leggiJson(f.path), cmd = item.json;
    if (cmd.stato !== 'da-eseguire') return;
    var ris = [], errori = 0;
    (cmd.azioni || []).forEach(function (a, i) {
      try { ris.push({ n: i + 1, tipo: a.tipo, ok: true, dati: AUTO_azione(a) }); }
      catch (e) { errori++; ris.push({ n: i + 1, tipo: a.tipo, ok: false, errore: String(e) }); }
    });
    cmd.risultati = ris; cmd.stato = errori ? 'errore' : 'eseguito'; cmd.eseguito_il = new Date().toISOString();
    AUTO_scriviJson(f.path, cmd, item.sha, 'Ponte Google: ' + f.name + ' (' + cmd.stato + ')'); n++;
  });
  return n;
}

function AUTO_azione(a) {
  switch (a.tipo) {
    /* ---- Drive ---- */
    case 'drive.cerca': {           // a.query = sintassi di ricerca di Drive, es: "title contains 'Quiz'"
      var it = DriveApp.searchFiles(a.query), out = [];
      while (it.hasNext() && out.length < (a.max || 50)) { var f = it.next();
        out.push({ id: f.getId(), nome: f.getName(), tipo: f.getMimeType(), url: f.getUrl(), modificato: f.getLastUpdated() }); }
      return out; }
    case 'drive.elenca': {          // a.cartella_id
      var c = DriveApp.getFolderById(a.cartella_id), out2 = [], fi = c.getFiles();
      while (fi.hasNext()) { var g = fi.next(); out2.push({ id: g.getId(), nome: g.getName(), tipo: g.getMimeType(), url: g.getUrl(), modificato: g.getLastUpdated() }); }
      var sub = c.getFolders(); while (sub.hasNext()) { var d = sub.next(); out2.push({ id: d.getId(), nome: d.getName(), tipo: 'cartella', url: d.getUrl() }); }
      return out2; }
    case 'drive.esporta': {         // a.id, a.formato (pdf, txt, csv, xlsx, docx), a.salva_in (percorso nel repo)
      var file = DriveApp.getFileById(a.id), mt = file.getMimeType(), blob;
      if (mt.indexOf('application/vnd.google-apps') === 0) {
        var fm = { pdf: 'application/pdf', txt: 'text/plain', csv: 'text/csv',
                   xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                   docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' }[a.formato || 'pdf'];
        if (a.formato === 'csv') blob = Utilities.newBlob(AUTO_csv(SpreadsheetApp.openById(a.id).getSheets()[0].getDataRange().getDisplayValues()), 'text/csv');
        else if (a.formato === 'txt' && mt === 'application/vnd.google-apps.document') blob = Utilities.newBlob(DocumentApp.openById(a.id).getBody().getText(), 'text/plain');
        else blob = file.getAs(fm);
      } else blob = file.getBlob();
      AUTO_commit(a.salva_in, blob, 'Ponte Google: export ' + file.getName());
      return { salvato_in: a.salva_in, nome: file.getName() }; }
    case 'drive.copia': {           // a.id, a.nome, a.cartella_id (facoltativa)
      var orig = DriveApp.getFileById(a.id), cop = a.cartella_id ? orig.makeCopy(a.nome || orig.getName(), DriveApp.getFolderById(a.cartella_id)) : orig.makeCopy(a.nome || orig.getName());
      return { id: cop.getId(), url: cop.getUrl() }; }
    case 'drive.cartella': {        // a.nome, a.padre_id (facoltativa)
      var nuova = a.padre_id ? DriveApp.getFolderById(a.padre_id).createFolder(a.nome) : DriveApp.createFolder(a.nome);
      return { id: nuova.getId(), url: nuova.getUrl() }; }
    /* ---- Moduli ---- */
    case 'forms.crea_quiz': {       // a.quiz come nei job (versioni, domande, punti, descrizione), a.cartella_id facoltativa
      var cart = a.cartella_id ? DriveApp.getFolderById(a.cartella_id) : DriveApp.getRootFolder();
      return AUTO_creaQuiz({ quiz: a.quiz, titolo: a.quiz.titolo || 'Quiz' }, cart); }
    case 'forms.leggi': {           // a.id: struttura del modulo con le risposte giuste
      var fo = FormApp.openById(a.id);
      return { titolo: fo.getTitle(), compila: fo.getPublishedUrl(), modifica: fo.getEditUrl(), quiz: fo.isQuiz(),
        domande: fo.getItems().map(function (x) {
          var o = { titolo: x.getTitle(), tipo: String(x.getType()) };
          if (x.getType() === FormApp.ItemType.MULTIPLE_CHOICE) { var mc = x.asMultipleChoiceItem(); o.punti = mc.getPoints();
            o.scelte = mc.getChoices().map(function (c) { return { testo: c.getValue(), giusta: c.isCorrectAnswer() }; }); }
          return o; }) }; }
    case 'forms.risposte': {        // a.id, a.salva_in (cartella nel repo): risultati con punteggio e risposte sbagliate
      AUTO_risultatiQuiz({ moduli: [{ versione: a.versione || 'A', id: a.id }], classe: a.classe || '', titolo: a.titolo || a.id }, a.salva_in);
      return { salvato_in: a.salva_in + '/_RISULTATI-QUIZ.json' }; }
    case 'forms.crea_modulo': {     // v6: a.titolo, a.descrizione, a.domande [{titolo, aiuto, obbligatoria, min, max}], a.cartella_id
      var fm = FormApp.create(a.titolo).setDescription(a.descrizione || '')
        .setCollectEmail(true).setLimitOneResponsePerUser(a.piu_risposte ? false : true).setAllowResponseEdits(true)
        .setConfirmationMessage(a.conferma || 'Fatto! Ricordati la tua password: non dirla a nessuno.');
      try { fm.setRequireLogin(true); } catch (e) {}
      var pre = [];
      (a.domande || []).forEach(function (d) {
        // v7.1: d.paragrafo = casella grande (come un documento); d.precompila = testo già scritto nel link precompilato
        var it = (d.paragrafo ? fm.addParagraphTextItem() : fm.addTextItem()).setTitle(d.titolo).setHelpText(d.aiuto || '').setRequired(d.obbligatoria !== false);
        if (d.precompila) pre.push(it.createResponse(d.precompila));   // v7.4: addTextItem/addParagraphTextItem danno già l'oggetto giusto (prima: «asTextItem is not a function»)
        if (d.min || d.max) {
          var v = FormApp.createTextValidation().setHelpText(d.errore || 'Lunghezza non valida')
            .requireTextLengthGreaterThanOrEqualTo(d.min || 1).build();
          it.setValidation(v);
        }
      });
      if (a.cartella_id) DriveApp.getFileById(fm.getId()).moveTo(DriveApp.getFolderById(a.cartella_id));
      var out = { id: fm.getId(), compila: fm.getPublishedUrl(), modifica: fm.getEditUrl() };
      if (pre.length) { var fr0 = fm.createResponse(); pre.forEach(function (r) { fr0.withItemResponse(r); }); out.precompilato = fr0.toPrefilledUrl(); }
      return out; }
    case 'forms.crea_percorso': {   // v7: quiz a schermate (una domanda per pagina), a crocette con risposta giusta + domande scritte
      // a.titolo, a.descrizione, a.conferma, a.cartella_id, a.domande [{titolo, aiuto, immagine_url, scelte:[testo...], giusta: indice, punti} | {titolo, aiuto, testo:true}]
      var fp = FormApp.create(a.titolo).setDescription(a.descrizione || '').setIsQuiz(true)
        .setCollectEmail(true).setLimitOneResponsePerUser(true).setShuffleQuestions(false).setProgressBar(true)
        .setConfirmationMessage(a.conferma || 'Fatto!');
      try { fp.setRequireLogin(true); } catch (e) {}
      (a.domande || []).forEach(function (d, n) {
        if (n > 0) fp.addPageBreakItem().setTitle('Domanda ' + (n + 1) + ' di ' + a.domande.length);
        if (d.immagine_url) fp.addImageItem().setImage(UrlFetchApp.fetch(d.immagine_url).getBlob());
        if (d.testo) { fp.addTextItem().setTitle(d.titolo).setHelpText(d.aiuto || '').setRequired(true); return; }
        var mi = fp.addMultipleChoiceItem();
        mi.setTitle(d.titolo).setHelpText(d.aiuto || '').setPoints(d.punti || 6).setRequired(true)
          .setChoices(d.scelte.map(function (c, k) { return mi.createChoice(c, k === d.giusta); }));
      });
      if (a.cartella_id) DriveApp.getFileById(fp.getId()).moveTo(DriveApp.getFolderById(a.cartella_id));
      return { id: fp.getId(), compila: fp.getPublishedUrl(), modifica: fp.getEditUrl() }; }
    case 'forms.modifica': {        // v7.1: a.id; a.descrizione, a.conferma (facoltative); a.aiuti {titolo domanda: nuovo aiuto}
      var fx = FormApp.openById(a.id), cambiati = 0;
      if (a.descrizione !== undefined) fx.setDescription(a.descrizione);
      if (a.conferma !== undefined) fx.setConfirmationMessage(a.conferma);
      fx.getItems().forEach(function (it) {
        if (a.aiuti && a.aiuti.hasOwnProperty(it.getTitle())) { it.setHelpText(a.aiuti[it.getTitle()]); cambiati++; } });
      return { id: a.id, domande_cambiate: cambiati }; }
    case 'forms.risposte_testo': {  // v6: a.id, a.salva_in (file .json nel repo riservato)
      var fr = FormApp.openById(a.id), righe = fr.getResponses().map(function (r) {
        var o = { email: r.getRespondentEmail(), ora: r.getTimestamp().toISOString(), risposte: {} };
        r.getItemResponses().forEach(function (ir) { o.risposte[ir.getItem().getTitle()] = String(ir.getResponse()); });
        return o; });
      AUTO_commit(a.salva_in, Utilities.newBlob(JSON.stringify(righe, null, 1), 'application/json', 'risposte.json'), 'Risposte modulo: ' + fr.getTitle());
      return { risposte: righe.length, salvato_in: a.salva_in }; }
    case 'forms.collega_foglio': {  // a.id: crea il Foglio delle risposte
      var fq = FormApp.openById(a.id), ss = SpreadsheetApp.create(fq.getTitle() + ' (risposte)');
      fq.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
      return { foglio_id: ss.getId(), url: ss.getUrl() }; }
    /* ---- Fogli ---- */
    case 'sheets.leggi': {          // a.id, a.intervallo facoltativo (es. "Foglio1!A1:F30")
      var sp = SpreadsheetApp.openById(a.id), rg = a.intervallo ? sp.getRange(a.intervallo) : sp.getSheets()[0].getDataRange();
      return rg.getDisplayValues(); }
    case 'sheets.scrivi': {         // a.id, a.intervallo (cella di partenza), a.valori (righe)
      var sp2 = SpreadsheetApp.openById(a.id), cella = sp2.getRange(a.intervallo);
      cella.getSheet().getRange(cella.getRow(), cella.getColumn(), a.valori.length, a.valori[0].length).setValues(a.valori);
      return { righe: a.valori.length }; }
    case 'sheets.crea': {           // a.titolo, a.valori (righe), a.cartella_id facoltativa
      var nuovo = SpreadsheetApp.create(a.titolo);
      if (a.valori && a.valori.length) nuovo.getSheets()[0].getRange(1, 1, a.valori.length, a.valori[0].length).setValues(a.valori);
      if (a.cartella_id) DriveApp.getFileById(nuovo.getId()).moveTo(DriveApp.getFolderById(a.cartella_id));
      return { id: nuovo.getId(), url: nuovo.getUrl() }; }
    /* ---- Documenti ---- */
    case 'docs.leggi':              // a.id
      return DocumentApp.openById(a.id).getBody().getText();
    case 'docs.crea': {             // a.titolo, a.blocchi (come "doc" nei job), a.cartella_id facoltativa
      var dc = AUTO_creaDoc(a.titolo, a.blocchi || []);
      if (a.cartella_id) DriveApp.getFileById(dc.getId()).moveTo(DriveApp.getFolderById(a.cartella_id));
      return { id: dc.getId(), url: dc.getUrl() }; }
    case 'docs.sostituisci': {      // a.id, a.cerca, a.sostituisci
      var body = DocumentApp.openById(a.id).getBody(); body.replaceText(a.cerca, a.sostituisci); return { fatto: true }; }
    /* ---- Classroom ---- */
    case 'classroom.corsi':
      return (Classroom.Courses.list({ teacherId: 'me', courseStates: ['ACTIVE'] }).courses || []).map(function (c) { return { id: c.id, nome: c.name, link: c.alternateLink }; });
    case 'classroom.compiti': {     // a.classe
      var cid = AUTO_courseId(a.classe);
      return (Classroom.Courses.CourseWork.list(cid, { pageSize: 50 }).courseWork || []).map(function (w) {
        return { id: w.id, titolo: w.title, stato: w.state, scadenza: w.dueDate ? [w.dueDate.day, w.dueDate.month, w.dueDate.year].join('/') : '', link: w.alternateLink }; }); }
    case 'classroom.consegne': {    // a.classe, a.coursework_id: chi ha consegnato e chi no
      var cid2 = AUTO_courseId(a.classe);
      return ((Classroom.Courses.CourseWork.StudentSubmissions.list(cid2, a.coursework_id).studentSubmissions) || []).map(function (s) {
        return { nome: AUTO_nome(s.userId), stato: s.state, voto_bozza: s.draftGrade, voto: s.assignedGrade, in_ritardo: !!s.late }; }); }
    case 'classroom.annuncio': {    // a.classe, a.testo (solo con l'OK del docente scritto nel file)
      var an = Classroom.Courses.Announcements.create({ text: a.testo, state: 'PUBLISHED' }, AUTO_courseId(a.classe));
      return { id: an.id, link: an.alternateLink }; }
    case 'classroom.annuncio_cancella': {   // v7.7: a.classe, a.annuncio_id — cancella SOLO un annuncio (mai il lavoro degli allievi). Per test e pulizia.
      Classroom.Courses.Announcements.remove(AUTO_courseId(a.classe), a.annuncio_id);
      return { cancellato: a.annuncio_id }; }
    /* ---- Gmail: SOLO bozze ---- */
    case 'gmail.bozza': {           // a.a, a.oggetto, a.testo
      var bz = GmailApp.createDraft(a.a, a.oggetto, a.testo); return { bozza_id: bz.getId() }; }
    default:
      throw new Error('Azione non prevista: ' + a.tipo);
  }
}

function AUTO_csv(righe) {
  return righe.map(function (r) { return r.map(function (v) { v = String(v); return /[",;\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }).join(','); }).join('\n');
}

var AUTO_nomi = {};
function AUTO_nome(id) {
  if (AUTO_nomi[id]) return AUTO_nomi[id];
  try { AUTO_nomi[id] = Classroom.UserProfiles.get(id).name.fullName; } catch (e) { AUTO_nomi[id] = id; }
  return AUTO_nomi[id];
}

function AUTO_slug(t) {
  var s = (t || '').toLowerCase();
  s = s.replace(/[àáâä]/g, 'a').replace(/[èéêë]/g, 'e').replace(/[ìíîï]/g, 'i')
       .replace(/[òóôö]/g, 'o').replace(/[ùúûü]/g, 'u').replace(/[ç]/g, 'c').replace(/[–—]/g, ' ');
  s = s.replace(/^\s*compito\b/, '').replace(/[^a-z0-9]+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
  return s || 'compito';
}

/* ====================== GIT (zona di scambio) ====================== */
function AUTO_courseId(classe) {
  var diz = AUTO_leggiJson(AUTO.DIZIONARIO).json;
  var c = diz.classi && diz.classi[classe];
  if (!c || !c.course_id) throw new Error('Classe ' + classe + ' assente nel dizionario');
  return c.course_id;
}

function AUTO_leggiJson(path) {
  var r = AUTO_gh('get', '/contents/' + path + '?ref=' + AUTO.BRANCH);
  if (r.getResponseCode() !== 200) throw new Error('Non letto ' + path + ' (' + r.getResponseCode() + ')');
  var j = JSON.parse(r.getContentText());
  var testo = Utilities.newBlob(Utilities.base64Decode(j.content.replace(/\s/g, ''))).getDataAsString('UTF-8');
  return { json: JSON.parse(testo), sha: j.sha };
}

function AUTO_scriviJson(path, obj, sha, msg) {
  var blob = Utilities.newBlob(JSON.stringify(obj, null, 1), 'application/json');
  var payload = { message: msg, content: Utilities.base64Encode(blob.getBytes()), branch: AUTO.BRANCH, sha: sha };
  var code = AUTO_gh('put', '/contents/' + path, payload).getResponseCode();
  if (code !== 200 && code !== 201) throw new Error('Stato non salvato su ' + path + ' (' + code + ')');
}

function AUTO_commit(repoPath, blob, msg) {
  var enc = repoPath.split('/').map(encodeURIComponent).join('/');
  var get = AUTO_gh('get', '/contents/' + enc + '?ref=' + AUTO.BRANCH);
  var sha = (get.getResponseCode() === 200) ? JSON.parse(get.getContentText()).sha : null;
  var payload = { message: msg, content: Utilities.base64Encode(blob.getBytes()), branch: AUTO.BRANCH };
  if (sha) payload.sha = sha;
  return AUTO_gh('put', '/contents/' + enc, payload).getResponseCode();
}

function AUTO_gh(method, path, payload) {
  var token = PropertiesService.getScriptProperties().getProperty('GITHUB_TOKEN');
  if (!token) throw new Error('Manca GITHUB_TOKEN nelle Proprieta dello script.');
  return UrlFetchApp.fetch('https://api.github.com/repos/' + AUTO.REPO + path, {
    method: method,
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
    contentType: 'application/json',
    payload: payload ? JSON.stringify(payload) : null,
    muteHttpExceptions: true
  });
}


/* ====================== v7.4 — CONSEGNA DELLA VERIFICA CON UN CLIC (applicazione web) ======================
   La pagina docs/verifica/ manda il risultato con un modulo HTML (POST, campo «d» = JSON) in una scheda nuova.
   Qui si controlla, si salva su Git (dati/verifiche/<id>/arrivi/) e si risponde con una pagina chiara per il ragazzo.
   Se Git non risponde, il risultato resta comunque nel Foglio «Arrivi verifiche» (riserva) e si recupera dopo.
   Messa in funzione (una volta): Distribuisci -> Nuova distribuzione -> Applicazione web -> Esegui come: me ->
   Chi ha accesso: chiunque nella scuola (o chiunque) -> Distribuisci -> copia l'URL che finisce con /exec. */
function doGet(e) {
  AUTO_assicuraTimer();   // v7.7: ogni visita tiene vivo il ponte
  return AUTO_paginaArrivo('Pagina pronta', 'Da qui arrivano le consegne delle verifiche del corso.', '#1f6feb');
}
function doPost(e) {
  AUTO_assicuraTimer();   // v7.7: ogni consegna tiene vivo il ponte
  var d;
  try { d = JSON.parse((e && e.parameter && e.parameter.d) || (e && e.postData && e.postData.contents) || '{}'); }
  catch (x) { return AUTO_paginaArrivo('Non arrivata', 'Il risultato non si legge. Torna alla verifica e clicca di nuovo «Manda al prof».', '#c0392b'); }
  var id = String(d.id || '').replace(/[^a-z0-9-]/gi, '').slice(0, 80);
  var nome = String(d.nome || '').slice(0, 60);
  var modo = d.modo === 'recupero' ? 'recupero' : d.modo === 'domanda' ? 'domanda' : d.modo === 'proposta' ? 'proposta' : 'verifica';   // v7.5: «proposta» (la talpa della 1INF, 14/10)
  if (!id || !nome) return AUTO_paginaArrivo('Non arrivata', 'Manca il nome o la verifica. Torna alla verifica e clicca di nuovo «Manda al prof».', '#c0392b');
  var testo = JSON.stringify(d, null, 1);
  if (testo.length > 300000) testo = testo.slice(0, 300000);
  var adesso = new Date(), email = '';
  try { email = Session.getActiveUser().getEmail() || ''; } catch (x) {}
  d._arrivo = adesso.toISOString(); d._email = email;
  testo = JSON.stringify(d, null, 1);
  var file = 'dati/verifiche/' + id + '/arrivi/' + Utilities.formatDate(adesso, 'Europe/Rome', 'HHmmss') + '_' + modo + '_' + AUTO_slug(nome) + '.json';
  var ok = false, okFoglio = false, lock = LockService.getScriptLock();
  try {
    lock.waitLock(25000);
    for (var i = 0; i < 3 && !ok; i++) {
      var c = AUTO_commit(file, Utilities.newBlob(testo, 'application/json'), 'Consegna ' + modo + ': ' + id + ' · ' + nome);
      ok = (c === 200 || c === 201);
      if (!ok) Utilities.sleep(1500);
    }
  } catch (x) { Logger.log('Consegna su Git non riuscita: ' + x); }
  finally { try { lock.releaseLock(); } catch (x) {} }
  try { AUTO_foglioArrivi().appendRow([adesso, id, modo, nome, email, ok ? 'su Git' : 'SOLO QUI', testo.slice(0, 45000)]); okFoglio = true; } catch (x) { Logger.log('Foglio di riserva: ' + x); }
  var ora = Utilities.formatDate(adesso, 'Europe/Rome', 'HH:mm');
  // v7.6: mai piu' «arrivata» a vuoto. La consegna e' al sicuro se sta su Git O nella riserva (Foglio).
  // Se non e' ne' sull'uno ne' sull'altra, si chiede di riprovare invece di dare per fatto.
  if (!ok && !okFoglio)
    return AUTO_paginaArrivo('Non arrivata', nome + ', la connessione ha fatto i capricci. Clicca di nuovo «Manda al prof» tra un momento.', '#c0392b');
  return AUTO_paginaArrivo(modo === 'proposta' ? 'Arrivata! · وصلت! · 收到了！' : 'Consegna arrivata al prof', nome + ', la tua ' + modo + ' è arrivata alle ' + ora + '. Hai finito: puoi chiudere questa scheda.', '#1a7f37');
}

/* ====================== v7.6 — RETE DI SICUREZZA: RECUPERA LE CONSEGNE DALLA RISERVA ======================
   Ogni consegna finisce sempre nel Foglio «Arrivi verifiche» (riserva), anche quando la scrittura su Git
   cade (ramo occupato). Questa funzione rilegge il Foglio e carica su Git ogni consegna segnata «SOLO QUI».
   Si lancia A MANO dal progetto: scegli AUTO_recuperaArrivi nel menu a tendina delle funzioni e premi «Esegui».
   E' riusabile all'infinito: le consegne gia' su Git si saltano, quelle recuperate si segnano «recuperato». */
function AUTO_recuperaArrivi() {
  var foglio = AUTO_foglioArrivi();
  var dati = foglio.getDataRange().getValues();
  var fatti = 0, saltati = 0, errori = 0;
  for (var r = 1; r < dati.length; r++) {
    var riga = dati[r];
    var quando = riga[0];
    var id = String(riga[1] || '').replace(/[^a-z0-9-]/gi, '').slice(0, 80);
    var modo = String(riga[2] || 'verifica');
    var nome = String(riga[3] || '');
    var git = String(riga[5] || '');
    var testo = String(riga[6] || '');
    if (!id || !nome || !testo) { saltati++; continue; }
    if (git === 'su Git' || git === 'recuperato') { saltati++; continue; }
    var d = (quando instanceof Date) ? quando : new Date(quando);
    var file = 'dati/verifiche/' + id + '/arrivi/' + Utilities.formatDate(d, 'Europe/Rome', 'HHmmss') + '_' + modo + '_' + AUTO_slug(nome) + '.json';
    var c = 0;
    for (var k = 0; k < 3; k++) {
      try { c = AUTO_commit(file, Utilities.newBlob(testo, 'application/json'), 'Recupero dalla riserva: ' + id + ' · ' + nome); }
      catch (x) { c = 0; Logger.log('Recupero fallito su ' + file + ': ' + x); }
      if (c === 200 || c === 201) break;
      Utilities.sleep(1200);
    }
    if (c === 200 || c === 201) { foglio.getRange(r + 1, 6).setValue('recuperato'); fatti++; }
    else errori++;
    Utilities.sleep(400);
  }
  var msg = 'Recupero finito. Caricate ora: ' + fatti + ' · gia a posto o saltate: ' + saltati + ' · errori: ' + errori + '.';
  Logger.log(msg);
  return msg;
}
function AUTO_foglioArrivi() {
  var p = PropertiesService.getScriptProperties(), id = p.getProperty('FOGLIO_ARRIVI');
  if (id) { try { return SpreadsheetApp.openById(id).getSheets()[0]; } catch (x) {} }
  var ss = SpreadsheetApp.create('Arrivi verifiche (riserva dello script)');
  ss.getSheets()[0].appendRow(['Arrivo', 'Verifica', 'Modo', 'Nome', 'Email', 'Git', 'Risultato']);
  p.setProperty('FOGLIO_ARRIVI', ss.getId());
  return ss.getSheets()[0];
}
function AUTO_paginaArrivo(titolo, testo, colore) {
  var h = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>' +
    '<body style="margin:0;font:20px/1.5 system-ui,Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1a2330">' +
    '<div style="max-width:640px;margin:60px auto;padding:24px;background:#fff;border:4px solid ' + colore + ';border-radius:16px">' +
    '<h1 style="color:' + colore + ';margin-top:0">' + titolo + '</h1><p>' + testo.replace(/</g, '&lt;') + '</p></div></body></html>';
  return HtmlService.createHtmlOutput(h).setTitle(titolo).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
