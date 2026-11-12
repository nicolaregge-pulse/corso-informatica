/**
 * FABBRICA - MOTORE v2.17 (12/11/2026)
 * Codice puro: lo scarica ed esegue (eval) il "lancio" a ogni giro. Usa le globali del lancio FB_BASE e UTENTI
 * ({ '3INF': [[pc, utenteGitHub, 'COGNOME Nome'], ...] }) e i servizi Google. Chiama FB_main_() dopo l'eval.
 * Properties usate: FB_FOGLIO, FB_FATTI, GITHUB_TOKEN (da v1), FB_FORMS, FB_NR, FB_ULTERR (nuove).
 * TIPOLOGIA LEZIONE (decisione del docente 11/11/2026, v2.8): le 4 tipologie sono Esercitazione Lazarus (schede Consegne <CLASSE> + progetto Lazarus nella scheda Git), Quiz su Moduli, Versioning su GitHub (schede Utenti e Git <CLASSE>), Teoria a schede (Moduli creato da una scheda). Nei lavori di indice.json il campo e "tipologia_lezione" ("quiz" o "teoria"; il vecchio nome "tipologia" o "tipo" e accettato; se manca: id che comincia per "scheda-" = teoria, altrimenti quiz). Il "tipo" delle domande (multi, singola, testo, paragrafo) e un'altra cosa e non cambia.
 * Changelog: 2.17 nuova scheda 'Situazione pubblica <CLASSE>' (1INF, 2INF, 3INF, 4TI) da pubblicare sul web per docs/cruscotto/: stesse colonne e stessa riga 1 (ora del dato) della scheda 'Situazione <CLASSE>', ma Allievo in formato 'Nome I.' (nome + iniziale del cognome, cognomi composti con particelle De, Di, El, Al ecc. gestiti, omonimi distinti con due lettere), SENZA email, SENZA note in fondo e SENZA altri dati personali (ogni email residua nei testi diventa '(email)'); se Allievo e un'email diventa 'Nome C.' dalla parte prima della chiocciola, altrimenti 'Allievo n'; la scheda 'Situazione <CLASSE>' con COGNOME Nome resta solo docente e invariata; la scheda pubblica in Indice come tipo Situazione (dopo quella docente), colore piu chiaro; 2.16 nuova scheda 'Elenco <CLASSE>' (colonne Email, Allievo COGNOME Nome come in Classroom, Fonte, Nota) per 1INF, 2INF, 3INF, 4TI: fonte primaria gli iscritti del corso Classroom (id dalla scheda Corsi, Courses.Students.list), fallback le email distinte delle schede 'Ris <id>' dei quiz attuali della classe (Allievo da 'Utenti <CLASSE>' per nome.cognome, abbinamento ambiguo = vuoto, Fonte 'Moduli'); una 'Email <CLASSE>' gia presente NON e mai sovrascritta (la scheda generata e separata); Situazione e Sicurezza leggono 'Email <CLASSE>' se c'e', altrimenti 'Elenco <CLASSE>' (solo righe Fonte Classroom); email con dominio diverso da studenti.piamarta.it e piamarta.it segnate 'dominio da controllare' in Nota (mai corrette); se l'API Classroom non risponde nessun errore: riga Avviso nella scheda e fallback; scheda Elenco in Indice come tipo Utenti; rilettura al massimo ogni 10 minuti; 2.15 scheda 'Situazione <CLASSE>': se mancano 'Email <CLASSE>' e 'Consegne <CLASSE>' l'elenco allievi viene dalla scheda 'Utenti <CLASSE>' (colonna C Allievo, COGNOME Nome), cosi chi non ha risposto a nessun quiz compare con MANCA; le email delle risposte si abbinano agli allievi per nome.cognome (riga 4: quanti abbinati e quanti no); avviso con il gesto preciso da fare (account PIAMARTA, un passo); 2.14 scheda 'Indice': righe 'Quiz' SOLO per gli id correnti di indice.json (una sola riga per id, Stato 'Attivo'); gli id vecchi di Esiti (Moduli sostituiti) diventano righe 'Quiz (vecchio)' con Stato 'Nascosta' e SENZA Link ragazzi, cosi il Pannello non li mostra; 2.13 FIX scheda 'Indice' e 'Quiz': niente piu formule HYPERLINK (il foglio e in italiano e rifiutava la virgola: #ERROR!); la colonna A di Indice e la colonna G di Quiz sono TESTO semplice (nome della scheda / 'Apri risultati'), il link cliccabile e messo con RichTextValue (setLinkUrl, indipendente dalla lingua) e, se non riesce, resta il testo; le righe 'Quiz' dell'Indice hanno Titolo e Link ragazzi da Esiti colonna D (mai link di modifica); 2.12 scheda 'Indice' con colonne in TESTO semplice per il Pannello (pagina docs/pannello/, che legge il CSV pubblicato): F = URL completo https://docs.google.com/spreadsheets/d/<id>/edit#gid=<gid> di ogni scheda, G = Titolo, H = Link ragazzi (solo viewform pubblico preso da Esiti colonna D, MAI il link di modifica), I = Tipologia lezione; una riga 'Quiz' per ogni lavoro di indice.json con link valido; nessun cognome, nessuna email; 2.11 scheda 'Indice' come prima scheda (una riga per scheda: nome con link HYPERLINK al gid, tipo, classe, ultimo aggiornamento, nascosta; raggruppata per tipo); ordine fisso delle schede a ogni giro (Indice, Situazione, Sicurezza, Esiti e Quiz, Tipologie lezione, Utenti/Consegne/Git/Email/Corsi, Altro, poi le 'Ris <id>' in fondo); le 'Ris <id>' ORFANE (id non piu in indice.json lavori) sono NASCOSTE con hideSheet e MAI cancellate (se l'id torna nell'indice si rimostrano); schede colorate (Ris per classe: 1INF blu, 2INF verde, 3INF arancio, 4TI viola, orfane grigie; Situazione e Sicurezza di un colore proprio); nessun dato e nessun id toccato; 2.10 intestazioni dei quiz nelle schede 'Situazione <CLASSE>' e 'Sicurezza <CLASSE>' in 3 righe (A = ora e argomento breve ricavati dal titolo del quiz, per esempio 'Sic. ora 5 \u00b7 infortuni'; B = data; C = id del quiz), mai troncate, testo a capo, larghezza colonna, riga intestazione alta, prime colonne congelate; se due intestazioni coincidono si aggiunge l'id alla riga A; id e Moduli invariati; 2.9 nuova scheda \'Situazione <CLASSE>\' (1INF, 2INF, 3INF, 4TI; solo docente, con COGNOME Nome): una riga per allievo, una colonna per ogni quiz della classe in indice.json (ordine di creazione, intestazione = titolo breve + data), cella = miglior % (punti/totale) o MANCA, riga \'Letto alle\' per ogni Moduli, colonne Fatti/totali, Media % dei fatti, NON HA FATTO, riepilogo in cima, colori verde >=80 / giallo <80 / rosso MANCA, (provv.) per le aperte non corrette; elenco allievi come Sicurezza (Email o Consegne), altrimenti email dalle schede Ris (dichiarato); schede e id esistenti invariati; 2.8 (a) controllo della richiesta PRIMA di creare il Moduli (titolo, domande, scelte, una sola giusta nelle singole): se non va, nessun Moduli e l'errore sta in Stato; (b) se la lettura o il controllo della richiesta falliscono, il lavoro NON e segnato come fatto e viene riprovato al giro dopo (prima restava perso per sempre); un Moduli gia creato non si ricrea mai; (c) avvisi lingua R6 non bloccanti nella colonna Controllo (1INF italiano+arabo+cinese; 2INF e 4TI solo italiano; 3INF niente arabo e cinese, il bangla e ammesso); (d) scheda 'Quiz' con colonna TIPOLOGIA LEZIONE; (e) nuova scheda 'Tipologie lezione' (classi x TIPOLOGIA LEZIONE, stato e ora del dato); (f) se manca 'Utenti <CLASSE>' la scheda vuota con l'intestazione viene creata (il docente incolla PC, utente GitHub, allievo); (g) Stato mostra la versione del motore; 2.7 Sicurezza per classe: indice.json "sicurezza" puo essere un elenco di classi (1INF, 2INF), ogni classe con le sue ore, ids e soglia; schede 'Email <CLASSE>', 'Consegne <CLASSE>', 'Sicurezza storico <CLASSE>' e 'Sicurezza <CLASSE>' (solo docente, COGNOME Nome); nuova scheda 'Sicurezza pubblica <CLASSE>' SENZA nomi (colonna Id = SHA-256 del nome in maiuscolo, il «Nome I.» lo mette la pagina docs/sicurezza-cruscotto/ da nomi.json) da pubblicare sul web per il cruscotto; 2.6 scheda 'Sicurezza 1INF' (solo docente, con COGNOME Nome): una riga per allievo, colonne ora 1-4 (da scheda 'Sicurezza storico 1INF'), 5, 6A, 6B (dalle schede 'Ris <id>' di indice.json "sicurezza") e Recupero, stato OK/DA RECUPERARE/MANCA/ASSENTE con soglia 80, colonne DA FARE ORA e DA RIFARE (sotto 80); elenco allievi ed email dalla scheda 'Email 1INF' oppure da 'Consegne 1INF'; 2.5 schede 'Ris <id>' con titolo del quiz in A1, riga A2 (Classe, id, data, ora, risposte), intestazione riga 4, dati dalla riga 5, colonna Domande aperte da correggere; nuova scheda 'Quiz' (prima dopo 'Esiti') con una riga per Modulo e link alla scheda dei risultati; 'Quiz migliori' legge dalla riga 5; 2.4 modulo GIT (scheda 'Git <CLASSE>' per ogni classe di indice.json "git", elenco dalla scheda 'Utenti <CLASSE>' A=PC B=Utente C=Allievo, una classe per giro, ogni classe al massimo ogni ogni_minuti, Progetto/README/Commit totali); 2.3 modulo CLASSROOM (schede 'Corsi' e 'Consegne <CLASSE>', una classe per giro, mappa in indice.json); 2.2 errori in una sola riga di 'Stato' (Ultimo errore), mai piu righe ERRORE in 'Esiti' (pulite a ogni giro); 2.1 elenco ragazzi letto dalla scheda 'Cruscotto Git <classe>' (UTENTI del lancio puo essere {}); 2.0 tutte le classi, registro Moduli, risultati (schede "Ris <id>"), scheda "Stato", cruscotti per classe.
 */

function FB_p_() { return PropertiesService.getScriptProperties(); }
function FB_json_(k) { try { return JSON.parse(FB_p_().getProperty(k) || '{}') || {}; } catch (e) { return {}; } }
function FB_salva_(k, o) { FB_p_().setProperty(k, JSON.stringify(o)); }
function FB_ora_(f) { return Utilities.formatDate(new Date(), 'Europe/Rome', f || 'dd/MM HH:mm:ss'); }

function FB_get_(url) {
  var r = UrlFetchApp.fetch(url + (url.indexOf('?') < 0 ? '?' : '&') + 't=' + Date.now(), { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('HTTP ' + r.getResponseCode() + ' ' + url);
  return r.getContentText();
}

var FB_TESTA_ = ['Ora', 'Id', 'Titolo', 'Link per i ragazzi', 'Link di modifica', 'Controllo', 'Classe', 'FormId'];

function FB_foglio_() {
  var id = FB_p_().getProperty('FB_FOGLIO'), ss;
  if (id) ss = SpreadsheetApp.openById(id);
  else {
    ss = SpreadsheetApp.create('Fabbrica (10/11/2026)');
    FB_p_().setProperty('FB_FOGLIO', ss.getId());
    ss.getSheets()[0].setName('Esiti');
  }
  var sh = ss.getSheetByName('Esiti') || ss.insertSheet('Esiti');
  sh.getRange(1, 1, 1, FB_TESTA_.length).setValues([FB_TESTA_]).setFontWeight('bold');
  return ss;
}

function FB_classe_(q, id) {
  if (q && q.classe) return String(q.classe).toUpperCase();
  var m = /^[A-Za-z]+-(\d+[A-Za-z]+)-/.exec(id || '');
  return m ? m[1].toUpperCase() : '';
}

/* ---------- TIPOLOGIA LEZIONE (v2.8) ---------- */
var FB_TL_ = { esercitazione: 'Esercitazione Lazarus', quiz: 'Quiz su Moduli', versioning: 'Versioning su GitHub', teoria: 'Teoria a schede' };
function FB_tl_(l, id) {
  var v = String((l && (l.tipologia_lezione || l.tipologia || l.tipo)) || '').toLowerCase();
  if (v.indexOf('teor') === 0 || v.indexOf('schede') >= 0) return 'teoria';
  if (v.indexOf('quiz') === 0) return 'quiz';
  return /^scheda-/i.test(String(id || (l && l.id) || '')) ? 'teoria' : 'quiz';
}

function FB_valida_(q) {
  var e = [];
  if (!q || typeof q !== 'object') return ['richiesta vuota'];
  if (!String(q.titolo || '').trim()) e.push('manca il titolo');
  if (!q.domande || !q.domande.length) { e.push('nessuna domanda'); return e; }
  q.domande.forEach(function (d, i) {
    var n = 'domanda ' + (i + 1);
    if (['multi', 'singola', 'testo', 'paragrafo'].indexOf(d.tipo) < 0) { e.push(n + ': tipo di domanda sconosciuto (' + d.tipo + ')'); return; }
    if (!String(d.t || '').trim()) e.push(n + ': manca il testo');
    if (d.tipo === 'multi' || d.tipo === 'singola') {
      if (!d.s || d.s.length < 2) { e.push(n + ': servono almeno 2 scelte'); return; }
      var g = d.s.filter(function (x) { return x && x[1]; }).length;
      if (d.s.some(function (x) { return !x || !String(x[0] || '').trim(); })) e.push(n + ': scelta vuota');
      if (d.tipo === 'singola' && g !== 1) e.push(n + ': la singola deve avere 1 giusta, ne ha ' + g);
      if (d.tipo === 'multi' && g < 1) e.push(n + ': nessuna scelta giusta');
    }
  });
  return e;
}

function FB_lingue_(q, classe) {
  var t = JSON.stringify(q), ar = /[\u0600-\u06FF]/.test(t), zh = /[\u4E00-\u9FFF]/.test(t), bn = /[\u0980-\u09FF]/.test(t), a = [];
  if (classe === '1INF') { if (!ar) a.push('manca l\'arabo'); if (!zh) a.push('manca il cinese'); }
  else if (classe === '2INF' || classe === '4TI') { if (ar || zh || bn) a.push('solo italiano'); }
  else if (classe === '3INF') { if (ar || zh) a.push('niente arabo e cinese (solo bangla per il PC 14)'); }
  return a;
}

/* ---------- Moduli ---------- */
function FB_attese_(q) {
  return q.domande.map(function (d) {
    if (d.tipo === 'multi') return { tipo: 'multi', scelte: d.s.length, giuste: d.s.filter(function (x) { return x[1]; }).length, titolo: d.t };
    if (d.tipo === 'singola') return { tipo: 'singola', scelte: d.s.length, giuste: 1, titolo: d.t };
    return { tipo: d.tipo, titolo: d.t };
  });
}

function FB_verifica_(form, attese) {
  var items = form.getItems(), err = [], ok = 0;
  if (items.length !== attese.length) err.push('ci sono ' + items.length + ' domande invece di ' + attese.length);
  for (var i = 0; i < Math.min(items.length, attese.length); i++) {
    var a = attese[i], it = items[i], p = [];
    try {
      if (it.getTitle() !== a.titolo) p.push('titolo diverso');
      if (a.tipo === 'multi' || a.tipo === 'singola') {
        var tipo = a.tipo === 'multi' ? FormApp.ItemType.CHECKBOX : FormApp.ItemType.MULTIPLE_CHOICE;
        if (it.getType() !== tipo) p.push('tipo sbagliato (' + it.getType() + ')');
        else {
          var x = a.tipo === 'multi' ? it.asCheckboxItem() : it.asMultipleChoiceItem();
          var sc = x.getChoices();
          var g = sc.filter(function (c) { return c.isCorrectAnswer(); }).length;
          if (sc.length !== a.scelte) p.push(sc.length + ' scelte invece di ' + a.scelte);
          if (g !== a.giuste) p.push(g + ' giuste invece di ' + a.giuste);
        }
      } else {
        var t2 = a.tipo === 'testo' ? FormApp.ItemType.TEXT : FormApp.ItemType.PARAGRAPH_TEXT;
        if (it.getType() !== t2) p.push('tipo sbagliato (' + it.getType() + ')');
      }
    } catch (e) { p.push('lettura: ' + e); }
    if (p.length) err.push('domanda ' + (i + 1) + ': ' + p.join(', ')); else ok++;
  }
  return { ok: ok, tot: attese.length, err: err };
}

function FB_crea_(q) {
  var f = FormApp.create(q.titolo);
  f.setDescription(q.descrizione || '');
  f.setIsQuiz(true);
  if (q.mescola) f.setShuffleQuestions(true);
  f.setCollectEmail(true);
  f.setLimitOneResponsePerUser(false);
  try { f.setRequireLogin(true); } catch (e) { Logger.log('setRequireLogin: ' + e); }
  f.setConfirmationMessage(q.conferma || 'Fatto!');
  q.domande.forEach(function (d) {
    var it;
    if (d.tipo === 'multi' || d.tipo === 'singola') {
      it = d.tipo === 'multi' ? f.addCheckboxItem() : f.addMultipleChoiceItem();
      it.setTitle(d.t);
      it.setChoices(d.s.map(function (x) { return it.createChoice(x[0], x[1]); }));
      it.setPoints(d.punti || 1);
      if (d.sp) {
        it.setFeedbackForCorrect(FormApp.createFeedback().setText('Giusto! ' + d.sp).build());
        it.setFeedbackForIncorrect(FormApp.createFeedback().setText('Non ancora. ' + d.sp).build());
      }
    } else {
      it = d.tipo === 'testo' ? f.addTextItem() : f.addParagraphTextItem();
      it.setTitle(d.t);
      if (d.punti && typeof it.setPoints === 'function') it.setPoints(d.punti);
      it.setHelpText('Domanda aperta: la corregge il docente a mano.');
    }
    it.setRequired(true);
  });
  var v = FB_verifica_(f, FB_attese_(q));
  return { ragazzi: f.getPublishedUrl(), modifica: f.getEditUrl(), formId: f.getId(), v: v };
}

/* ---------- Errori e stato ---------- */
var FB_ERRS = [];
function FB_errore_(ss, passo, e) {
  FB_ERRS.push(passo + ': ' + (e && e.message ? e.message : e));
}

function FB_pulisci_(ss) {
  var sh = ss.getSheetByName('Esiti');
  if (!sh) return;
  var v = sh.getDataRange().getValues(), i = v.length - 1, fine;
  while (i >= 1) {
    if (v[i][1] !== 'ERRORE') { i--; continue; }
    fine = i;
    while (i >= 1 && v[i][1] === 'ERRORE') i--;
    sh.deleteRows(i + 2, fine - i);
  }
}

function FB_ultimoErrore_() {
  if (!FB_ERRS.length) return 'nessuno';
  var t = FB_ERRS.join(' | ');
  if (t.indexOf('autorizzazioni') >= 0) return "Manca un'autorizzazione Google: eseguire installa e consentire";
  return FB_ora_() + ' ' + t;
}

function FB_stato_(ss) {
  var sh = ss.getSheetByName('Stato') || ss.insertSheet('Stato');
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), tot = 0, k, n = 0;
  for (k in forms) n++;
  for (k in nr) tot += Number(nr[k]) || 0;
  sh.getRange(1, 1, 5, 2).setValues([
    ['Fabbrica v2', FB_ora_('dd/MM/yyyy HH:mm:ss')],
    ['Moduli', n],
    ['Risposte totali', tot],
    ['Ultimo errore', FB_ultimoErrore_()],
    ['Motore', '2.17']
  ]);
  sh.getRange(1, 1).setFontWeight('bold');
}

/* ---------- Passi ---------- */
function FB_nuovi_(ss, indice) {
  var fatti = FB_json_('FB_FATTI'), forms = FB_json_('FB_FORMS'), sh = ss.getSheetByName('Esiti');
  (indice.lavori || []).forEach(function (l) {
    if (fatti[l.id]) return;
    var ora = FB_ora_(), q, cl;
    try {
      var testo = Utilities.newBlob(Utilities.base64Decode(FB_get_(FB_BASE + l.file).trim())).getDataAsString('UTF-8');
      q = JSON.parse(testo);
      var ev = FB_valida_(q);
      if (ev.length) throw new Error('richiesta non valida: ' + ev.join('; '));
      cl = FB_classe_(q, l.id);
    } catch (e0) {
      /* nessun Moduli creato: non si segna come fatto, si riprova al giro dopo */
      FB_errore_(ss, 'lavoro ' + l.id, e0);
      return;
    }
    try {
      var r = FB_crea_(q);
      var ctrl = r.v.err.length ? 'ERRORE: ' + r.v.err.join('; ') + ' (NON darlo ai ragazzi)' : 'OK ' + r.v.ok + '/' + r.v.tot;
      var av = FB_lingue_(q, cl);
      if (av.length && !r.v.err.length) ctrl += ' \u00b7 AVVISO R6 (non blocca): ' + av.join(', ');
      sh.appendRow([ora, l.id, q.titolo, r.ragazzi, r.modifica, ctrl, cl, r.formId]);
      forms[l.id] = { formId: r.formId, classe: cl, titolo: q.titolo };
      FB_salva_('FB_FORMS', forms);
    } catch (e) {
      sh.appendRow([ora, l.id, '', '', '', 'ERRORE: ' + e, FB_classe_(null, l.id), '']);
    }
    fatti[l.id] = 1;
    FB_salva_('FB_FATTI', fatti);
  });
}

function FB_ripara_(ss) {
  var sh = ss.getSheetByName('Esiti'), forms = FB_json_('FB_FORMS'), cambiato = false;
  var dati = sh.getDataRange().getValues();
  for (var i = 1; i < dati.length; i++) {
    var r = dati[i], id = String(r[1] || ''), link = String(r[4] || '');
    if (!id || id === 'ERRORE' || !link || forms[id]) continue;
    try {
      var fid = r[7] ? String(r[7]) : FormApp.openByUrl(link).getId();
      var cl = r[6] ? String(r[6]) : FB_classe_(null, id);
      forms[id] = { formId: fid, classe: cl, titolo: String(r[2] || '') };
      cambiato = true;
      sh.getRange(i + 1, 7, 1, 2).setValues([[cl, fid]]);
    } catch (e) { FB_errore_(ss, 'ripara ' + id, e); }
  }
  if (cambiato) FB_salva_('FB_FORMS', forms);
}

function FB_puntiTotali_(form) {
  var tot = 0;
  form.getItems().forEach(function (it) {
    try {
      var t = it.getType(), x = null, T = FormApp.ItemType;
      if (t === T.CHECKBOX) x = it.asCheckboxItem();
      else if (t === T.MULTIPLE_CHOICE) x = it.asMultipleChoiceItem();
      else if (t === T.TEXT) x = it.asTextItem();
      else if (t === T.PARAGRAPH_TEXT) x = it.asParagraphTextItem();
      if (x) tot += Number(x.getPoints()) || 0;
    } catch (e) { }
  });
  return tot;
}

function FB_creato_(ss, id) {
  var v = ss.getSheetByName('Esiti').getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][1] === id) return String(v[i][0]).slice(0, 5);
  return '';
}

/* v2.13: link cliccabile senza formule (RichTextValue): items = [{t: testo, u: url}] in colonna c da riga r; il testo e gia scritto, se il rich text non funziona resta il testo */
function FB_linkCelle_(sh, r, c, items) {
  try {
    var v = items.map(function (x) { return [x.u ? SpreadsheetApp.newRichTextValue().setText(x.t).setLinkUrl(x.u).build() : SpreadsheetApp.newRichTextValue().setText(x.t).build()]; });
    sh.getRange(r, c, v.length, 1).setRichTextValues(v);
  } catch (e) { }
}
var FB_lavoroIndice_ = {};
function FB_quiz_(ss) {
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), medie = FB_json_('FB_MEDIE');
  var es = ss.getSheetByName('Esiti').getDataRange().getValues(), righe = [], i;
  var FB_lq_ = [];
  for (i = 1; i < es.length; i++) {
    var id = es[i][1], f = forms[id];
    if (!id || !f) continue;
    var ris = ss.getSheetByName('Ris ' + id);
    var link = ris ? 'Apri risultati' : '';
    FB_lq_.push({ t: link, u: ris ? '#gid=' + ris.getSheetId() : '' });
    righe.push([i, [f.classe || FB_classe_(null, id), f.titolo || es[i][2] || id, id, nr[id] === undefined ? '' : nr[id], medie[id] === undefined ? '' : medie[id], es[i][3] || '', link, FB_TL_[FB_tl_(FB_lavoroIndice_[id], id)]]]);
  }
  righe.forEach(function (r, n) { r.push(FB_lq_[n]); });
  righe.sort(function (a, b) { return b[0] - a[0]; });
  var lqs = righe.map(function (r) { return r[2]; });
  var sh = ss.getSheetByName('Quiz');
  if (!sh) { var pos = ss.getSheetByName('Esiti'); sh = pos.getIndex ? ss.insertSheet('Quiz', pos.getIndex()) : ss.insertSheet('Quiz'); }
  sh.clear();
  sh.getRange(1, 1, 1, 8).setValues([['Classe', 'Titolo', 'Id', 'Risposte', 'Media del migliore', 'Link per i ragazzi', 'Link alla scheda dei risultati', 'TIPOLOGIA LEZIONE']]).setFontWeight('bold');
  if (righe.length) sh.getRange(2, 1, righe.length, 8).setValues(righe.map(function (r) { return r[1]; }));
  if (righe.length) FB_linkCelle_(sh, 2, 7, lqs);
}

function FB_risultati_(ss, t0) {
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), fatte = 0, id;
  for (id in forms) {
    if (fatte >= 5 || Date.now() - t0 > 270000) break;
    try {
      var form = FormApp.openById(forms[id].formId);
      var ris = form.getResponses(), n = ris.length;
      var g0 = ss.getSheetByName('Ris ' + id);
      if (nr[id] === n && g0 && g0.getRange(4, 1).getValues()[0][0] === 'Email') continue;
      var su = FB_puntiTotali_(form), per = {};
      ris.forEach(function (r) {
        var em = r.getRespondentEmail() || '(senza email)', s = 0, p0 = per[em] || (per[em] = { max: 0, t: 0, ult: null, aperte: 0 });
        (r.getGradableItemResponses() || []).forEach(function (g) { var sc = g.getScore(); if (sc === null || sc === undefined) p0.aperte++; s += Number(sc) || 0; });
        var ts = r.getTimestamp(), p = p0;
        if (s > p.max) p.max = s;
        p.t++;
        if (!p.ult || ts > p.ult) p.ult = ts;
      });
      var righe = Object.keys(per).map(function (em) {
        var p = per[em];
        return [em, p.max, su, p.t, p.ult ? Utilities.formatDate(p.ult, 'Europe/Rome', 'dd/MM HH:mm') : '', p.aperte];
      });
      righe.sort(function (a, b) { return b[1] - a[1]; });
      var tot = 0;
      righe.forEach(function (r) { tot += r[1]; });
      var medie = FB_json_('FB_MEDIE');
      medie[id] = righe.length ? Math.round(tot / righe.length * 10) / 10 : '';
      FB_salva_('FB_MEDIE', medie);
      var sh = ss.getSheetByName('Ris ' + id) || ss.insertSheet('Ris ' + id);
      sh.clear();
      var cr = FB_creato_(ss, id);
      sh.getRange(1, 1).setValue(form.getTitle() || forms[id].titolo || id).setFontWeight('bold');
      sh.getRange(2, 1).setValue('Classe ' + (forms[id].classe || FB_classe_(null, id)) + ' \u00b7 id ' + id + ' \u00b7 creato il ' + cr + ' \u00b7 dati letti alle ' + FB_ora_('HH:mm:ss') + ' \u00b7 ' + n + ' risposte');
      sh.getRange(4, 1, 1, 6).setValues([['Email', 'Migliore', 'Su', 'Tentativi', 'Ultimo invio', 'Domande aperte da correggere']]).setFontWeight('bold');
      if (righe.length) sh.getRange(5, 1, righe.length, 6).setValues(righe);
      nr[id] = n;
      FB_salva_('FB_NR', nr);
      fatte++;
    } catch (e) { FB_errore_(ss, 'risultati ' + id, e); }
  }
}

/* ---------- Cruscotto Git per classe ---------- */
function CG_get_(path) {
  var tok = FB_p_().getProperty('GITHUB_TOKEN');
  var h = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'fabbrica' };
  if (tok) h['Authorization'] = 'Bearer ' + tok;
  try {
    var r = UrlFetchApp.fetch('https://api.github.com/' + path, { headers: h, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null;
    return JSON.parse(r.getContentText());
  } catch (e) { return null; }
}

function CG_riga_(pc, utente, nome, oggi) {
  var repos = CG_get_('users/' + utente + '/repos?per_page=100&sort=pushed') || [];
  var sc = null, i;
  for (i = 0; i < repos.length; i++) { if (/master/i.test(repos[i].name)) { sc = repos[i]; break; } }
  if (!sc) for (i = 0; i < repos.length; i++) { if ((repos[i].pushed_at || '').slice(0, 10) === oggi) { sc = repos[i]; break; } }
  if (!sc && repos.length) sc = repos[0];
  var d = { repo: '-', push: '-', oggi: 0, ult: '-', tag: '-', rel: '-', chg: 'no', st: 'ROSSO' };
  if (sc) {
    var full = sc.full_name;
    d.repo = sc.name;
    d.push = (sc.pushed_at || '').replace('T', ' ').slice(11, 16) + ' UTC';
    var com = CG_get_('repos/' + full + '/commits?per_page=30') || [];
    for (i = 0; i < com.length; i++) { if (com[i].commit.author.date.slice(0, 10) === oggi) d.oggi++; }
    if (com.length) d.ult = String(com[0].commit.message).split('\n')[0].slice(0, 60);
    var tags = CG_get_('repos/' + full + '/tags?per_page=5') || [];
    if (tags.length) d.tag = tags.map(function (t) { return t.name; }).join(', ');
    var rel = CG_get_('repos/' + full + '/releases?per_page=5') || [], bozza = false;
    if (rel.length) { d.rel = (rel[0].name || rel[0].tag_name || 'senza nome') + (rel[0].draft ? ' (bozza)' : ''); bozza = !!rel[0].draft; }
    var cont = CG_get_('repos/' + full + '/contents/') || [];
    for (i = 0; i < cont.length; i++) { if (/changelog/i.test(cont[i].name)) d.chg = 'sì'; }
    if (rel.length && !bozza && tags.length) d.st = 'VERDE';
    else if (rel.length || tags.length) d.st = 'GIALLO';
    else if (d.oggi > 0) d.st = 'ARANCIO';
  }
  return [d.st, 'PC ' + pc, nome, utente, d.repo, d.push, d.oggi, d.tag, d.rel, d.chg, d.ult];
}

function CG_aggiorna_(ss, classe, utenti) {
  var nomeSh = 'Cruscotto Git ' + classe;
  var sh = ss.getSheetByName(nomeSh) || ss.insertSheet(nomeSh);
  var oggi = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd');
  var righe = utenti.map(function (u) { return CG_riga_(u[0], u[1], u[2], oggi); });
  var ord = { VERDE: 0, GIALLO: 1, ARANCIO: 2, ROSSO: 3 };
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]]; });
  sh.clear();
  var ora = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Git e Mastermind · release 1.0 · dati letti alle ' + ora).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = release pubblicata con tag · GIALLO = tag o bozza · ARANCIO = commit di oggi · ROSSO = nessuna attività. Solo repository pubblici.');
  var testa = ['Stato', 'PC', 'Allievo', 'Utente GitHub', 'Repository', 'Ultimo push', 'Commit oggi', 'Tag', 'Release', 'CHANGELOG', 'Ultimo commit'];
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (var i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}

function CG_leggiElenco_(ss, classe) {
  var sh = ss.getSheetByName('Cruscotto Git ' + classe), out = [];
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 4; i < v.length; i++) {
    var n = parseInt(String(v[i][1]).replace(/\D/g, ''), 10), nome = String(v[i][2] || '').trim(), ut = String(v[i][3] || '').trim();
    if (!ut || !nome || isNaN(n)) continue;
    out.push([n, ut, nome]);
  }
  return out;
}

function FB_cruscotti_(ss, indice) {
  var lista = indice.cruscotti;
  if (!lista && indice.cruscotto && indice.cruscotto.attivo) lista = [{ classe: '3INF', attivo: true }];
  if (new Date().getMinutes() % 2 !== 0) return;
  (lista || []).forEach(function (c) {
    if (c.attivo === false) return;
    var u = (typeof UTENTI !== 'undefined' && UTENTI) ? UTENTI[c.classe] : null;
    if (!u || !u.length) u = CG_leggiElenco_(ss, c.classe);
    if (!u.length) {
      var es = ss.getSheetByName('Esiti'), msg = 'Cruscotto ' + c.classe + ': nessun elenco';
      var rr = es ? es.getDataRange().getValues() : [];
      if (!rr.length || String(rr[rr.length - 1][5]) !== msg) if (es) es.appendRow([FB_ora_(), 'AVVISO', '', '', '', msg, '', '']);
      return;
    }
    try { CG_aggiorna_(ss, c.classe, u); } catch (e) { FB_errore_(ss, 'cruscotto ' + c.classe, e); }
  });
}

/* ---------- Git e progetti per classe (v2.4) ---------- */
function GT_get_(path) {
  var tok = FB_p_().getProperty('GITHUB_TOKEN');
  var h = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'fabbrica' };
  if (tok) h['Authorization'] = 'Bearer ' + tok;
  try {
    var r = UrlFetchApp.fetch('https://api.github.com/' + path, { headers: h, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null;
    var lk = '';
    try { var hh = r.getHeaders ? r.getHeaders() : {}; lk = String(hh.Link || hh.link || ''); } catch (e1) { lk = ''; }
    return { body: JSON.parse(r.getContentText()), link: lk };
  } catch (e) { return null; }
}
function GT_lista_(path) { var r = GT_get_(path); return r && r.body && r.body.length !== undefined ? r.body : []; }

function GT_riga_(pc, utente, nome, oggi) {
  var repos = GT_lista_('users/' + utente + '/repos?per_page=100&sort=pushed'), sc = null, i;
  for (i = 0; i < repos.length; i++) { if (/master|mastermind/i.test(repos[i].name)) { sc = repos[i]; break; } }
  if (!sc) for (i = 0; i < repos.length; i++) { if ((repos[i].pushed_at || '').slice(0, 10) === oggi) { sc = repos[i]; break; } }
  if (!sc && repos.length) sc = repos[0];
  var d = { repo: '-', push: '-', oggi: 0, tot: 0, prog: 'no', rd: 'no', tag: '-', rel: '-', ult: '-', st: 'ROSSO' };
  if (sc) {
    var full = sc.full_name, bozza = false, hasTag = false, hasRel = false;
    d.repo = sc.name;
    d.push = (sc.pushed_at || '').replace('T', ' ').slice(0, 16) + ' UTC';
    var c = GT_get_('repos/' + full + '/commits?per_page=30'), com = c ? c.body : [];
    for (i = 0; i < com.length; i++) { if (String((com[i].commit.author || {}).date).slice(0, 10) === oggi) d.oggi++; }
    if (com.length) d.ult = String(com[0].commit.message).split('\n')[0].slice(0, 60);
    d.tot = com.length;
    var m = c && /[?&]page=(\d+)>;\s*rel="last"/.exec(c.link);
    if (m) d.tot = '~' + (Number(m[1]) * 30);
    var cont = GT_lista_('repos/' + full + '/contents/'), lz = false, altro = false;
    for (i = 0; i < cont.length; i++) {
      if (/\.(lpi|lpr)$/i.test(cont[i].name)) lz = true;
      if (/^readme/i.test(cont[i].name)) d.rd = 'si';
      altro = true;
    }
    d.prog = lz ? 'Lazarus' : (altro ? 'altro' : 'no');
    if (/master|mastermind/i.test(sc.name)) {
      var tags = GT_lista_('repos/' + full + '/tags?per_page=5'), rel = GT_lista_('repos/' + full + '/releases?per_page=5');
      if (tags.length) { d.tag = tags.map(function (t) { return t.name; }).join(', '); hasTag = true; }
      if (rel.length) { d.rel = (rel[0].name || rel[0].tag_name || 'senza nome') + (rel[0].draft ? ' (bozza)' : ''); bozza = !!rel[0].draft; hasRel = true; }
      if (hasRel && !bozza && hasTag) d.st = 'VERDE';
      else if (hasRel || hasTag) d.st = 'GIALLO';
      else if (d.oggi > 0) d.st = 'ARANCIO';
    } else if (d.oggi > 0) d.st = 'ARANCIO';
  }
  return [d.st, 'PC ' + pc, nome, utente, d.repo, d.push, d.oggi, d.tot, d.prog, d.rd, d.tag, d.rel, d.ult];
}

function GT_elenco_(ss, classe) {
  var sh = ss.getSheetByName('Utenti ' + classe), out = [];
  if (sh) {
    var v = sh.getDataRange().getValues();
    for (var i = 0; i < v.length; i++) {
      var ut = String(v[i][1] || '').trim();
      if (!ut || /^utente/i.test(ut)) continue;
      out.push([String(v[i][0]).replace(/\D/g, '') || '-', ut, String(v[i][2] || '').trim() || '-']);
    }
    return out;
  }
  if (classe === '3INF') return CG_leggiElenco_(ss, classe);
  return null;
}

function GT_scheda_(ss, classe, utenti, t0) {
  var oggi = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd'), righe = [], errori = 0, i;
  for (i = 0; i < utenti.length; i++) {
    if (Date.now() - t0 > 270000) { FB_errore_(ss, 'Git ' + classe, 'tempo quasi finito, righe parziali'); break; }
    try { righe.push(GT_riga_(utenti[i][0], utenti[i][1], utenti[i][2], oggi)); }
    catch (e) { errori++; righe.push(['ROSSO', 'PC ' + utenti[i][0], utenti[i][2], utenti[i][1], '-', '-', 0, 0, 'no', 'no', '-', '-', 'errore lettura']); }
  }
  if (errori) FB_errore_(ss, 'Git ' + classe, errori + ' righe con errore di lettura');
  var ord = { VERDE: 0, GIALLO: 1, ARANCIO: 2, ROSSO: 3 };
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]]; });
  var sh = ss.getSheetByName('Git ' + classe) || ss.insertSheet('Git ' + classe);
  sh.clear();
  var ora = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Git e progetti · dati letti alle ' + ora).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = release pubblicata con tag · GIALLO = tag o bozza · ARANCIO = commit di oggi · ROSSO = nessuna attività. Tag e release solo per i repository Mastermind. Solo repository pubblici. Commit totali approssimati.');
  var testa = ['Stato', 'PC', 'Allievo', 'Utente GitHub', 'Repository', 'Ultimo push', 'Commit oggi', 'Commit totali', 'Progetto', 'README', 'Tag', 'Release', 'Ultimo commit'];
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}

function FB_git_(ss, indice, t0) {
  var cfg = indice.git;
  if (!cfg || cfg.attivo === false) return;
  var classi = cfg.classi || ['3INF', '4TI', '2INF', '1INF'], ogni = (cfg.ogni_minuti || 10) * 60000;
  var T = FB_json_('GT_T'), ora = Date.now(), fatta = false;
  var dovute = classi.filter(function (c) { return !T[c] || ora - T[c] >= ogni; });
  dovute.sort(function (a, b) { return (T[a] || 0) - (T[b] || 0); });
  dovute.forEach(function (c) {
    try {
      var u = GT_elenco_(ss, c);
      if (!u || !u.length) {
        if (!ss.getSheetByName('Utenti ' + c)) ss.insertSheet('Utenti ' + c).getRange(1, 1, 1, 3).setValues([['PC', 'Utente GitHub', 'Allievo']]).setFontWeight('bold');
        FB_ERRS.push('Git ' + c + ': compilare la scheda Utenti ' + c + ' (PC, Utente GitHub, Allievo)'); return;
      }
      if (fatta || Date.now() - t0 > 240000) return;
      GT_scheda_(ss, c, u, t0);
      T[c] = ora; fatta = true; FB_salva_('GT_T', T);
    } catch (e) { FB_errore_(ss, 'Git ' + c, e); }
  });
}

/* ---------- Classroom: consegne per classe (v2.3) ---------- */
function CR_corsi_() {
  var out = [], tok = null, r;
  do {
    r = Classroom.Courses.list({ courseStates: ['ACTIVE'], pageSize: 100, pageToken: tok || undefined });
    out = out.concat(r.courses || []);
    tok = r.nextPageToken || null;
  } while (tok);
  return out;
}
function CR_classe_(nome, mappa) {
  for (var c in mappa) { if (mappa[c] && String(nome).indexOf(mappa[c]) >= 0) return c; }
  return '-';
}
function CR_nome_(s) {
  var n = (s.profile && s.profile.name) || {};
  if (n.familyName && n.givenName) return String(n.familyName).toUpperCase() + ' ' + n.givenName;
  return n.fullName || '(senza nome)';
}
function CR_quiz_(ss, classe, email) {
  var parti = [], c = String(classe).toLowerCase();
  ss.getSheets().forEach(function (sh) {
    var m = /^Ris (.+)$/.exec(sh.getName ? sh.getName() : sh.name);
    if (!m || m[1].toLowerCase().indexOf(c) < 0) return;
    var v = sh.getDataRange().getValues();
    for (var i = 4; i < v.length; i++) {
      if (String(v[i][0]).toLowerCase() === String(email).toLowerCase()) { parti.push(v[i][1] + '/' + v[i][2]); break; }
    }
  });
  return parti.length ? parti.join(' · ') : '-';
}
function CR_scheda_(ss, classe, corso, cfg) {
  var N = cfg.ultimi || 8, id = corso.id, i, j;
  var studenti = [], tok = null, r;
  do {
    r = Classroom.Courses.Students.list(id, { pageSize: 100, pageToken: tok || undefined });
    studenti = studenti.concat(r.students || []); tok = r.nextPageToken || null;
  } while (tok);
  var lavori = [];
  tok = null;
  do {
    r = Classroom.Courses.CourseWork.list(id, { courseWorkStates: ['PUBLISHED'], pageSize: 100, pageToken: tok || undefined });
    lavori = lavori.concat(r.courseWork || []); tok = r.nextPageToken || null;
  } while (tok);
  lavori = lavori.filter(function (w) { return w.workType === 'ASSIGNMENT'; });
  lavori.sort(function (a, b) { return String(b.creationTime) < String(a.creationTime) ? -1 : 1; });
  lavori = lavori.slice(0, N);
  var cons = {};
  lavori.forEach(function (w) {
    var t = null; tok = null;
    do {
      r = Classroom.Courses.CourseWork.StudentSubmissions.list(id, w.id, { pageSize: 100, pageToken: tok || undefined });
      (r.studentSubmissions || []).forEach(function (s) {
        if (s.state === 'TURNED_IN' || s.state === 'RETURNED') (cons[w.id] = cons[w.id] || {})[s.userId] = 1;
      });
      tok = r.nextPageToken || null;
    } while (tok);
  });
  var ord = { ROSSO: 0, ARANCIO: 1, GIALLO: 2, VERDE: 3 };
  var righe = studenti.map(function (s) {
    var m = 0, celle = lavori.map(function (w) {
      if ((cons[w.id] || {})[s.userId]) return 'Consegnato';
      m++; return 'Mancante';
    });
    var st = m === 0 ? 'VERDE' : m === 1 ? 'GIALLO' : m <= 3 ? 'ARANCIO' : 'ROSSO';
    var em = (s.profile && s.profile.emailAddress) || '';
    return [st, CR_nome_(s), em].concat(celle, [lavori.length - m, m, em ? CR_quiz_(ss, classe, em) : '-']);
  });
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]] || (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0); });
  var nomeSh = 'Consegne ' + classe;
  var sh = ss.getSheetByName(nomeSh) || ss.insertSheet(nomeSh);
  sh.clear();
  sh.getRange(1, 1).setValue(classe + ' · Consegne · dati letti alle ' + Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss')).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = nessun compito mancante · GIALLO = ne manca 1 · ARANCIO = ne mancano 2-3 · ROSSO = 4 o più. Ultimi compiti pubblicati; Consegnato = consegnato o restituito.');
  var testa = ['Stato', 'Allievo', 'Email'];
  lavori.forEach(function (w) {
    var d = String(w.creationTime || '').slice(0, 10).split('-');
    testa.push(String(w.title || '').slice(0, 28) + ' ' + (d.length === 3 ? d[2] + '/' + d[1] : ''));
  });
  testa = testa.concat(['Consegnati', 'Mancanti', 'Quiz migliori']);
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}
function FB_classroom_(ss, indice, t0) {
  var cfg = indice.classroom;
  if (!cfg || cfg.attivo === false) return;
  if (typeof Classroom === 'undefined') { FB_ERRS.push('Classroom non abilitato: aggiungere il servizio Classroom API in Apps Script'); return; }
  if (Date.now() - t0 > 240000) return;
  var corsi = CR_corsi_(), mappa = cfg.classi || {}, trovati = {}, ordine = [];
  var ts = Number(FB_p_().getProperty('FB_CORSI_T') || 0);
  if (Date.now() - ts >= 600000 || !ss.getSheetByName('Corsi')) {
    var sc = ss.getSheetByName('Corsi') || ss.insertSheet('Corsi');
    sc.clear();
    sc.getRange(1, 1, 1, 3).setValues([['Nome', 'Id', 'Classe']]).setFontWeight('bold');
    var rr = corsi.map(function (c) { return [c.name, c.id, CR_classe_(c.name, mappa)]; });
    if (rr.length) sc.getRange(2, 1, rr.length, 3).setValues(rr);
    FB_p_().setProperty('FB_CORSI_T', String(Date.now()));
  }
  corsi.forEach(function (c) { var k = CR_classe_(c.name, mappa); if (k !== '-' && !trovati[k]) trovati[k] = c; });
  for (var k in mappa) if (trovati[k]) ordine.push(k);
  if (!ordine.length) return;
  var cl = ordine[Math.floor(new Date().getMinutes() / 1) % ordine.length];
  CR_scheda_(ss, cl, trovati[cl], cfg);
}

/* ---------- Sicurezza 1INF per allievo (v2.6, solo docente) ---------- */
function SI_norm_(s) { return String(s || '').toUpperCase().replace(/\s+/g, ' ').trim(); }
function SI_ora_(s) { return String(s || '').toUpperCase().replace(/^ORA\s*/, '').trim(); }

function SI_elenco_(ss, classe) {
  var e2n = {}, nomi = [], visti = {}, sh = ss.getSheetByName('Email ' + classe), v, i, fonte = '';
  function aggNome(n) { if (n && !visti[n]) { visti[n] = 1; nomi.push(n); } }
  if (sh) {
    fonte = "scheda 'Email " + classe + "'";
    v = sh.getDataRange().getValues();
    for (i = 0; i < v.length; i++) {
      var em = String(v[i][0] || '').trim().toLowerCase(), n = SI_norm_(v[i][1]);
      if (!n || /^allievo$/i.test(n)) continue;
      if (em.indexOf('@') > 0) e2n[em] = n;
      aggNome(n);
    }
    return { e2n: e2n, nomi: nomi, fonte: fonte };
  }
  /* v2.16: 'Elenco <CLASSE>' generata dal motore, solo righe con Fonte Classroom */
  if ((sh = ss.getSheetByName('Elenco ' + classe))) {
    v = sh.getDataRange().getValues();
    for (i = 1; i < v.length; i++) {
      var em3 = String(v[i][0] || '').trim().toLowerCase(), n3 = SI_norm_(v[i][1]);
      if (!n3 || String(v[i][2]) !== 'Classroom') continue;
      if (em3.indexOf('@') > 0) e2n[em3] = n3;
      aggNome(n3);
    }
    if (nomi.length) return { e2n: e2n, nomi: nomi, fonte: "scheda 'Elenco " + classe + "' (Classroom)" };
    e2n = {};
  }
  if ((sh = ss.getSheetByName('Consegne ' + classe))) {
    fonte = "scheda 'Consegne " + classe + "' (Classroom)";
    v = sh.getDataRange().getValues();
    for (i = 4; i < v.length; i++) {
      var em2 = String(v[i][2] || '').trim().toLowerCase(), n2 = SI_norm_(v[i][1]);
      if (!n2) continue;
      if (em2.indexOf('@') > 0) e2n[em2] = n2;
      aggNome(n2);
    }
  }
  return { e2n: e2n, nomi: nomi, fonte: fonte };
}

function SI_storico_(ss, classe) {
  var out = {}, sh = ss.getSheetByName('Sicurezza storico ' + classe);
  if (!sh) return { dati: out, presente: false };
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) {
    var n = SI_norm_(v[i][0]), o = SI_ora_(v[i][1]);
    if (!n || !o) continue;
    var voto = v[i][2] === '' || v[i][2] === null || v[i][2] === undefined ? null : Number(v[i][2]);
    if (voto !== null && isNaN(voto)) voto = null;
    var st = SI_norm_(v[i][3]);
    out[n + '|' + o] = { voto: voto, stato: st, fonte: String(v[i][4] || '') };
  }
  return { dati: out, presente: true };
}

function SI_ris_(ss, ids, e2n, ora, nonAbb, letture) {
  var per = {}, disp = false;
  (ids || []).forEach(function (id) {
    var sh = ss.getSheetByName('Ris ' + id);
    if (!sh) return;
    disp = true;
    var v = sh.getDataRange().getValues();
    var m = /dati letti alle (\d\d:\d\d)/.exec(String(v[1] && v[1][0] || ''));
    letture.push(ora + ' (' + id + '): ' + (m ? m[1] : 'ora non leggibile'));
    for (var i = 4; i < v.length; i++) {
      var em = String(v[i][0] || '').trim().toLowerCase(), su = Number(v[i][2]), mg = Number(v[i][1]);
      if (!em || !su) continue;
      var pct = Math.round(mg / su * 100), aperte = Number(v[i][5]) || 0, nome = e2n[em];
      if (!nome) { nonAbb.push(em + ' · ora ' + ora + ' · ' + pct + '%'); continue; }
      if (!per[nome] || pct > per[nome].pct) per[nome] = { pct: pct, aperte: aperte };
    }
  });
  return { per: per, disp: disp };
}

function SI_cella_(nome, ora, ris, sto, soglia) {
  var r = ris.per[nome], s = sto.dati[nome + '|' + ora];
  var pct = null, da = '', aperte = 0;
  if (r) { pct = r.pct; da = 'F'; aperte = r.aperte; }
  if (s && s.voto !== null && (pct === null || s.voto > pct)) { pct = s.voto; da = 'r'; aperte = 0; }
  if (pct !== null) {
    var ok = pct >= soglia;
    return { st: ok ? 'OK' : 'REC', pct: pct, txt: pct + '% ' + (ok ? 'OK' : 'DA RECUPERARE') + (da === 'r' ? ' (r)' : '') + (aperte > 0 ? ' (provv.: ' + aperte + ' aperte da correggere)' : '') };
  }
  if (s && s.stato === 'ASSENTE') return { st: 'ASSENTE', pct: null, txt: 'ASSENTE (r)' };
  if (s && s.stato === 'MANCA') return { st: 'MANCA', pct: null, txt: 'MANCA (r)' };
  if (ris.disp) return { st: 'MANCA', pct: null, txt: 'MANCA' };
  return { st: 'ND', pct: null, txt: 'dato non importato' };
}

function SI_classe_(ss, cfg) {
  if (!cfg || cfg.attivo === false) return;
  var classe = String(cfg.classe || '1INF').toUpperCase(), soglia = Number(cfg.soglia) || 80, ore = cfg.ore || [];
  var nomeSh = 'Sicurezza ' + classe;
  var el = SI_elenco_(ss, classe), sto = SI_storico_(ss, classe), nonAbb = [], letture = [];
  var sh = ss.getSheetByName(nomeSh) || ss.insertSheet(nomeSh);
  sh.clear();
  var ora0 = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Sicurezza per allievo (solo docente) · dati letti alle ' + ora0).setFontWeight('bold');
  if (!el.nomi.length) {
    sh.getRange(2, 1).setValue("Manca l'elenco degli allievi: serve la scheda 'Email " + classe + "' (A=Email, B=Allievo) oppure la scheda 'Consegne " + classe + "'.");
    return;
  }
  var risOre = ore.map(function (o) { return SI_ris_(ss, o.ids, el.e2n, o.ora, nonAbb, letture); });
  var rec = SI_ris_(ss, (cfg.recupero && cfg.recupero.ids) || [], el.e2n, 'Recupero', nonAbb, letture);
  sh.getRange(2, 1).setValue('Soglia ' + soglia + '/100 sul miglior tentativo. OK = ' + soglia + '% o più · DA RECUPERARE = sotto ' + soglia + '% · MANCA = nessuna risposta · ASSENTE = segnato assente nella scheda storico. (r) = dato dalla scheda \u0027Sicurezza storico ' + classe + '\u0027 (report del riservato, fonte e ora nella colonna Fonte). (provv.) = ci sono domande aperte non ancora corrette, la percentuale è provvisoria. 6A e 6B sono colonne separate: come si combinano non è deciso.');
  sh.getRange(3, 1).setValue('Elenco da ' + el.fonte + ' · storico ' + (sto.presente ? 'presente' : "assente (scheda 'Sicurezza storico " + classe + "' non trovata)") + ' · letture Moduli: ' + (letture.join(' · ') || 'nessuna scheda Ris trovata'));
  var testa = ['Stato', 'Allievo'].concat(ore.map(function (o) { return 'Ora ' + o.ora; }), ['Recupero ore 1-5', 'DA FARE ORA', 'DA RIFARE (sotto ' + soglia + ')', 'Dato non importato']);
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  try {
    var fSic = FB_json_('FB_FORMS'), dSic = {}, shE = ss.getSheetByName('Esiti');
    if (shE) shE.getDataRange().getValues().forEach(function (r) { dSic[r[1]] = String(r[0]).slice(0, 5); });
    var tSic = ore.map(function (o) {
      var id0 = (o.ids || [])[0], f0 = id0 && fSic[id0], th = SM_testa_(f0 ? f0.titolo : 'Sicurezza ora ' + o.ora, id0 || 'storico', dSic[id0] || '');
      if (!/ora\s+\w+/i.test(th.a)) th.a = 'Sic. ora ' + o.ora + ' \u00b7 ' + th.a.replace(/^Sic\.\s*/, '');
      th.a = th.a.replace(/^Sic\. ora \w+/i, 'Sic. ora ' + o.ora);
      return th;
    });
    SM_applica_(sh, 4, 3, tSic);
  } catch (eT) { Logger.log('intestazioni sicurezza: ' + eT); }
  var righe = el.nomi.map(function (nome) {
    var celle = ore.map(function (o, k) { return SI_cella_(nome, SI_ora_(o.ora), risOre[k], sto, soglia); });
    var fare = [], rifare = [], nd = [];
    celle.forEach(function (c, k) {
      var o = ore[k].ora;
      if (c.st === 'MANCA') fare.push('ora ' + o);
      else if (c.st === 'ASSENTE') fare.push('ora ' + o + ' (assente)');
      else if (c.st === 'REC') rifare.push('ora ' + o + ' (' + c.pct + '%)');
      else if (c.st === 'ND') nd.push('ora ' + o);
    });
    var cr = rec.per[nome] ? rec.per[nome].pct + '%' : (rec.disp ? 'MANCA' : 'dato non importato');
    var st = (fare.length) ? 'ROSSO' : rifare.length ? 'ARANCIO' : nd.length ? 'GIALLO' : 'VERDE';
    return [st, nome].concat(celle.map(function (c) { return c.txt; }), [cr, fare.join(', ') || '-', rifare.join(', ') || '-', nd.join(', ') || '-']);
  });
  var ord = { ROSSO: 0, ARANCIO: 1, GIALLO: 2, VERDE: 3 };
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]] || (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0); });
  sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  SI_pubblica_(ss, classe, soglia, ora0, testa, righe, letture);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (var i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
  var fondo = 6 + righe.length, note = [];
  var visti = {}; el.nomi.forEach(function (n) { visti[n] = 1; });
  var estranei = {};
  for (var k in sto.dati) { var nn = k.split('|')[0]; if (!visti[nn]) estranei[nn] = 1; }
  Object.keys(estranei).forEach(function (n) { note.push(['Nome nello storico non trovato nell\u0027elenco: ' + n]); });
  nonAbb.forEach(function (e) { note.push(['Email non abbinata a un allievo: ' + e]); });
  if (note.length) sh.getRange(fondo, 1, note.length, 1).setValues(note);
}

function SI_hash_(nome) {
  var b = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, SI_norm_(nome), Utilities.Charset.UTF_8), h = '';
  for (var i = 0; i < b.length; i++) h += ('0' + ((b[i] + 256) % 256).toString(16)).slice(-2);
  return h;
}

/* scheda pubblica SENZA nomi: Id = SHA-256 del nome in maiuscolo; il «Nome I.» sta in docs/sicurezza-cruscotto/nomi.json */
function SI_pubblica_(ss, classe, soglia, ora0, testa, righe, letture) {
  var sh = ss.getSheetByName('Sicurezza pubblica ' + classe) || ss.insertSheet('Sicurezza pubblica ' + classe);
  sh.clear();
  sh.getRange(1, 1).setValue(classe + ' · Sicurezza (pubblica, senza nomi) · dati letti alle ' + ora0).setFontWeight('bold');
  sh.getRange(2, 1).setValue('Soglia ' + soglia + '/100 sul miglior tentativo. OK = ' + soglia + '% o più · DA RECUPERARE = sotto ' + soglia + '% · MANCA = nessuna risposta · ASSENTE = segnato assente. (provv.) = domande aperte non ancora corrette.');
  sh.getRange(3, 1).setValue('Letture Moduli: ' + (letture.join(' · ') || 'nessuna scheda Ris trovata'));
  var t = testa.slice(); t[1] = 'Id';
  sh.getRange(4, 1, 1, t.length).setValues([t]).setFontWeight('bold');
  var pub = righe.map(function (r) { var q = r.slice(); q[1] = SI_hash_(r[1]); return q; });
  if (pub.length) sh.getRange(5, 1, pub.length, t.length).setValues(pub);
}

function FB_sicurezza_(ss, indice) {
  var l = indice.sicurezza;
  if (!l) return;
  if (!Array.isArray(l)) l = [l];
  l.forEach(function (cfg) {
    try { SI_classe_(ss, cfg); } catch (e) { FB_errore_(ss, 'sicurezza ' + (cfg && cfg.classe || ''), e); }
  });
}

/* ---------- Situazione per classe: tutti i quiz, tutti i voti, chi non ha fatto (v2.9, solo docente) ---------- */
function SM_corto_(t, id) {
  var s = String(t || id || '').replace(/\s*\([^)]*\)\s*$/, '').replace(/\s+/g, ' ').trim();
  return s.length > 45 ? s.slice(0, 44) + '\u2026' : s;
}

/* v2.10: intestazione quiz in 3 righe. A = ora e argomento breve (dal titolo), B = data, C = id */
function SM_testa_(titolo, id, dataEsiti) {
  var t = String(titolo || id || ''), data = String(dataEsiti || ''), m;
  t = t.split(' \u00b7 ')[0];
  m = /\((?:[0-9A-Za-z]+),\s*(\d\d\/\d\d)\)\s*$/.exec(t);
  if (m) data = m[1];
  t = t.replace(/\s*\([^)]*\)\s*$/, '').replace(/^Quiz\s+/i, '').replace(/\s+/g, ' ').trim();
  var a = t, sic = /^Sicurezza\s+/i.test(t), r;
  if (sic) {
    t = t.replace(/^Sicurezza\s+/i, '');
    if ((r = /^RECUPERO\s+(ore\s+[\d-]+)/i.exec(t))) a = 'Sic. RECUPERO ' + r[1];
    else {
      var o = /^(?:ora\s+(\w+)|quinta ora)\s*(?::\s*(.*))?$/i.exec(t);
      if (o) a = 'Sic. ora ' + (o[1] || '5') + (o[2] ? ' \u00b7 ' + o[2].replace(/^rischio\s+/i, '').replace(/\s+generali$/i, '') : '');
      else a = 'Sic. ' + t;
    }
  } else if ((r = /^(or[ae]\s+[\d-]+(?:\s+FINALE)?)\s*:\s*(.*)$/i.exec(t))) a = r[1] + ' \u00b7 ' + r[2];
  return { a: a, data: data, id: id };
}

/* applica le intestazioni a 3 righe a una riga di intestazione gia scritta (colonne c0.., una per quiz) */
function SM_applica_(sh, riga, c0, teste, largTot) {
  var n = teste.length, seen = {}, k, dup = {};
  teste.forEach(function (x) { dup[x.a] = (dup[x.a] || 0) + 1; });
  teste.forEach(function (x) { if (dup[x.a] > 1) x.a = x.a + ' (' + x.id + ')'; x.cella = x.a + '\n' + x.data + '\n' + x.id; });
  if (!n) return;
  sh.getRange(riga, c0, 1, n).setValues([teste.map(function (x) { return x.cella; })]).setWrap(true).setVerticalAlignment('top');
  for (k = 0; k < n; k++) sh.setColumnWidth(c0 + k, 190);
  sh.setRowHeight(riga, 78);
  sh.setColumnWidth(1, 80); sh.setColumnWidth(2, 190);
  sh.setFrozenColumns(2);
}

function SM_quiz_(ss, indice, classe) {
  var forms = FB_json_('FB_FORMS'), es = ss.getSheetByName('Esiti').getDataRange().getValues(), out = [], i;
  var lavori = {};
  (indice.lavori || []).forEach(function (l) { lavori[l.id] = l; });
  for (i = 1; i < es.length; i++) {
    var id = es[i][1], f = forms[id];
    if (!id || !f || !lavori[id]) continue;
    if ((f.classe || FB_classe_(null, id)) !== classe) continue;
    if (FB_tl_(lavori[id], id) !== 'quiz') continue;
    var th = SM_testa_(f.titolo || es[i][2], id, String(es[i][0]).slice(0, 5));
    out.push({ id: id, riga: i, data: th.data, titolo: th.a, th: th });
  }
  return out;
}

function SM_leggi_(ss, id) {
  var sh = ss.getSheetByName('Ris ' + id);
  if (!sh) return { disp: false, ora: '', per: {} };
  var v = sh.getDataRange().getValues(), per = {};
  var m = /dati letti alle (\d\d:\d\d(?::\d\d)?)/.exec(String(v[1] && v[1][0] || ''));
  for (var i = 4; i < v.length; i++) {
    var em = String(v[i][0] || '').trim().toLowerCase(), mg = Number(v[i][1]), su = Number(v[i][2]);
    if (!em || !su) continue;
    var pct = Math.round(mg / su * 100), ap = Number(v[i][5]) || 0;
    if (!per[em] || pct > per[em].pct) per[em] = { pct: pct, mg: mg, su: su, aperte: ap };
  }
  return { disp: true, ora: m ? m[1] : 'ora non leggibile', per: per };
}

/* ---------- v2.15: elenco allievi per Situazione anche da 'Utenti <CLASSE>' e abbinamento email per nome.cognome ---------- */
function SM_tok_(s) {
  var t = String(s || '').toLowerCase();
  try { t = t.normalize('NFD').replace(/[̀-ͯ]/g, ''); } catch (e) { }
  return t.split(/[^a-z]+/).filter(function (x) { return x; });
}
function SM_abbina_(email, nomi) {
  var loc = String(email || '').split('@')[0], tk = SM_tok_(loc), j = tk.join(''), trovati = [];
  if (!j) return null;
  nomi.forEach(function (n) {
    var nt = SM_tok_(n);
    if (nt.length < 2) return;
    var a = nt.slice().sort().join('|'), b = tk.slice().sort().join('|'), ok = a === b;
    if (!ok && tk.length === 1) { /* cognomenome senza separatore: cognome+nome o nome+cognome */
      var cog = nt[0], nom = nt.slice(1).join(''), cogAll = nt.slice(0, -1).join(''), nomUlt = nt[nt.length - 1];
      ok = j === cog + nom || j === nom + cog || j === cogAll + nomUlt || j === nomUlt + cogAll;
    }
    if (ok) trovati.push(n);
  });
  return trovati.length === 1 ? trovati[0] : null;
}
function SM_utenti_(ss, classe) {
  var sh = ss.getSheetByName('Utenti ' + classe), nomi = [], vis = {};
  if (!sh) return { esiste: false, nomi: nomi };
  var v = sh.getDataRange().getValues();
  for (var i = 0; i < v.length; i++) {
    var n = SI_norm_(v[i][2]);
    if (!n || /^ALLIEVO$/.test(n) || /^-$/.test(n)) continue;
    if (!vis[n]) { vis[n] = 1; nomi.push(n); }
  }
  return { esiste: true, nomi: nomi };
}
function SM_gesto_(classe, caso) {
  if (caso === 'manca') return "GESTO (account PIAMARTA, un passo): apri il foglio Fabbrica, vai alla scheda 'Utenti " + classe + "' (se non c'e' la crea il motore al prossimo giro) e incolla le righe PC, Utente GitHub, Allievo (COGNOME Nome), una per allievo.";
  return "GESTO (account PIAMARTA, un passo): apri il foglio Fabbrica, crea la scheda 'Email " + classe + "' e scrivi nella colonna A l'email e nella colonna B l'allievo (COGNOME Nome) degli allievi non abbinati.";
}

function SM_classe_(ss, indice, classe) {
  var quiz = SM_quiz_(ss, indice, classe), nome = 'Situazione ' + classe;
  var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  sh.clear();
  var ora0 = FB_ora_('dd/MM/yyyy HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' \u00b7 Situazione quiz e voti (solo docente, con COGNOME Nome) \u00b7 dati letti il ' + ora0).setFontWeight('bold');
  if (!quiz.length) { sh.getRange(2, 1).setValue('Nessun quiz della classe ' + classe + ' in indice.json.'); return; }
  var el = SI_elenco_(ss, classe), nonAbb = [], dichiara = '', fonteTxt = '', usaUtenti = false;
  var lett = quiz.map(function (q) { return SM_leggi_(ss, q.id); });
  var elenco = el.nomi.slice(), e2n = {}, k0;
  for (k0 in el.e2n) e2n[k0] = el.e2n[k0];
  if (!elenco.length) {
    var ut = SM_utenti_(ss, classe);
    if (ut.nomi.length) {
      usaUtenti = true; elenco = ut.nomi.slice();
      fonteTxt = "scheda 'Utenti " + classe + "' (" + ut.nomi.length + " allievi, colonna Allievo)";
    } else {
      e2n = {}; var vis = {};
      lett.forEach(function (L) { Object.keys(L.per).forEach(function (em) { if (!vis[em]) { vis[em] = 1; e2n[em] = em; elenco.push(em); } }); });
      dichiara = "Nessun elenco allievi per " + classe + ": manca la scheda 'Email " + classe + "' o 'Consegne " + classe + "' e la scheda 'Utenti " + classe + "' " + (ut.esiste ? "e' vuota (colonna Allievo senza nomi)" : "non c'e'") + ". Uso le email presenti nelle schede Ris; chi non ha mai risposto a nessun quiz NON compare. " + SM_gesto_(classe, 'manca');
    }
  }
  var abbN = 0, senzaEmail = [];
  if (usaUtenti) {
    var viste = {}, trov = {};
    lett.forEach(function (L) { Object.keys(L.per).forEach(function (em) {
      if (viste[em]) return; viste[em] = 1;
      var n = SM_abbina_(em, elenco);
      if (n) { e2n[em] = n; trov[n] = 1; }
    }); });
    abbN = Object.keys(trov).length;
    elenco.forEach(function (n) { if (!trov[n]) senzaEmail.push(n); });
  }
  var celle = {}, disp = lett.map(function (L) { return L.disp; });
  elenco.forEach(function (n) { celle[n] = quiz.map(function () { return null; }); });
  lett.forEach(function (L, k) {
    Object.keys(L.per).forEach(function (em) {
      var n = e2n[em], r = L.per[em];
      if (!n) { nonAbb.push(em + ' \u00b7 ' + quiz[k].titolo + ' \u00b7 ' + r.pct + '%'); return; }
      var c = celle[n][k];
      if (!c || r.pct > c.pct) celle[n][k] = r;
    });
  });
  var tot = disp.filter(function (d) { return d; }).length, nd = quiz.length - tot;
  var testa = ['Stato', 'Allievo'].concat(quiz.map(function (q) { return q.titolo; }), ['Fatti / totali', 'Media % dei fatti', 'NON HA FATTO']);
  var righe = elenco.map(function (n) {
    var fatti = 0, somma = 0, manca = [], txt = quiz.map(function (q, k) {
      var c = celle[n][k];
      if (c) { fatti++; somma += c.pct; return { t: c.pct + '% (' + c.mg + '/' + c.su + ')' + (c.aperte > 0 ? ' (provv.: ' + c.aperte + ' aperte da correggere)' : ''), p: c.pct }; }
      if (disp[k]) { manca.push(q.titolo + ' (' + q.data + ')'); return { t: 'MANCA', p: -1 }; }
      return { t: 'dato non letto', p: -2 };
    });
    var st = !tot ? 'ND' : manca.length ? 'ROSSO' : 'VERDE';
    return { st: st, n: n, txt: txt, riga: [st, n].concat(txt.map(function (x) { return x.t; }), [fatti + '/' + tot, fatti ? Math.round(somma / fatti) + '%' : '-', manca.length ? manca.join(' \u00b7 ') : '-']), m: manca.length };
  });
  righe.sort(function (a, b) { return b.m - a.m || (a.n < b.n ? -1 : a.n > b.n ? 1 : 0); });
  var tutto = righe.filter(function (r) { return tot && r.m === 0; }).length;
  sh.getRange(2, 1).setValue('Cella = miglior punteggio in % (punti/totale) di tutti i tentativi. MANCA = nessuna risposta. Verde = 80% o pi\u00f9, giallo = sotto 80%, rosso = MANCA. (provv.) = ci sono domande aperte non ancora corrette: la percentuale pu\u00f2 cambiare. Media = solo sui quiz fatti. Quiz = Moduli di indice.json con TIPOLOGIA LEZIONE Quiz su Moduli (le schede di teoria non sono contate).');
  sh.getRange(3, 1).setValue('RIEPILOGO: ' + righe.length + ' allievi \u00b7 ' + tutto + ' hanno fatto tutti i ' + tot + ' quiz letti \u00b7 ' + (righe.length - tutto) + ' ne hanno almeno uno mancante' + (nd ? ' \u00b7 ' + nd + ' quiz non ancora letti (scheda Ris assente), non contati' : ''));
  var abbTxt = '';
  if (usaUtenti) abbTxt = ' \u00b7 Abbinamento email per nome.cognome: ' + abbN + ' allievi abbinati, ' + senzaEmail.length + ' senza email abbinata (' + (senzaEmail.length ? senzaEmail.length + ' risultano MANCA anche se potrebbero aver risposto' : 'nessuno') + ')' + (nonAbb.length ? ' \u00b7 ' + nonAbb.length + ' risposte con email non abbinata (elenco in fondo)' : '') + (senzaEmail.length || nonAbb.length ? ' \u00b7 ATTENZIONE: ' + SM_gesto_(classe, 'abb') : '');
  sh.getRange(4, 1).setValue('Elenco allievi da ' + (el.nomi.length ? el.fonte : fonteTxt || 'schede Ris (vedi avviso)') + abbTxt + (dichiara ? ' \u00b7 ATTENZIONE: ' + dichiara : ''));
  var lr = ['Letto alle', ''].concat(lett.map(function (L) { return L.disp ? L.ora : 'non letto'; }), ['', '', '']);
  sh.getRange(5, 1, 1, lr.length).setValues([lr]).setFontWeight('bold');
  sh.getRange(6, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  sh.getRange(7, 1, righe.length, testa.length).setValues(righe.map(function (r) { return r.riga; }));
  SM_applica_(sh, 6, 3, quiz.map(function (q) { return q.th; }));
  quiz.forEach(function (q) { q.titolo = q.th.a; });
  var colSt = { VERDE: '#a5d6a7', ROSSO: '#ef9a9a', ND: '#eeeeee' };
  righe.forEach(function (r, i) {
    sh.getRange(7 + i, 1).setBackground(colSt[r.st]).setFontWeight('bold');
    r.txt.forEach(function (x, k) {
      if (x.p === -2) return;
      sh.getRange(7 + i, 3 + k).setBackground(x.p < 0 ? '#ef9a9a' : x.p >= 80 ? '#a5d6a7' : '#fff59d');
    });
  });
  var note = [];
  nonAbb.forEach(function (e) { note.push(['Email non abbinata a un allievo: ' + e]); });
  if (note.length) sh.getRange(8 + righe.length, 1, note.length, 1).setValues(note);
}

/* ---------- v2.17: scheda 'Situazione pubblica <CLASSE>': stesse colonne, Allievo = «Nome I.», nessuna email ---------- */
var SM_PART_ = { DE: 1, DI: 1, DA: 1, DEL: 1, DELLA: 1, DEI: 1, DEGLI: 1, DAL: 1, DALLA: 1, DALL: 1, DELLE: 1, LO: 1, LA: 1, LE: 1, EL: 1, AL: 1, BEN: 1, BIN: 1, BEL: 1, ABD: 1, ABDEL: 1, ABDUL: 1, ABU: 1, ABOU: 1, OULD: 1, VAN: 1, VON: 1, DOS: 1, DAS: 1, DU: 1, SAN: 1, SANTA: 1, MAC: 1, MC: 1 };
function SM_cap_(w) { return String(w || '').toLowerCase().replace(/(^|[-'\u2019\s])([a-z\u00e0-\u00ff])/g, function (m, a, b) { return a + b.toUpperCase(); }); }
function SM_tuttoMai_(t) { return t === t.toUpperCase() && t !== t.toLowerCase(); }
/* 'ROSSI Mario', 'DE LUCA Mario', 'EL AMRANI SARA' -> { nome: 'Mario', cog: 'ROSSI' } (cog serve solo per iniziale e omonimi, mai in uscita intera) */
function SM_parti_(s, k) {
  s = String(s || '').replace(/\s+/g, ' ').trim();
  if (s.indexOf('@') > 0) {
    var t = s.split('@')[0].split(/[._-]+/).filter(function (x) { return x; });
    return t.length >= 2 ? { nome: SM_cap_(t[0]), cog: t[t.length - 1].toUpperCase() } : { nome: 'Allievo ' + (k + 1), cog: '' };
  }
  var p = s.split(' ').filter(function (x) { return x; });
  if (p.length < 2) return { nome: p.length ? SM_cap_(p[0]) : 'Allievo ' + (k + 1), cog: '' };
  var nc = 0;
  while (nc < p.length && SM_tuttoMai_(p[nc])) nc++;
  if (nc === 0 || nc === p.length) {
    /* tutto maiuscolo (o senza maiuscole): il cognome e la prima parola piu le particelle che la precedono */
    nc = 0;
    while (nc < p.length - 2 && SM_PART_[p[nc].toUpperCase().replace(/[.']/g, '')]) nc++;
    nc++;
  }
  return { nome: p.slice(nc).map(SM_cap_).join(' '), cog: p.slice(0, nc).join(' ').toUpperCase() };
}
function SM_iniz_(cog) { var m = /[A-Z\u00c0-\u00dd]/.exec(String(cog || '').toUpperCase()); return m ? m[0] : ''; }
/* elenco di nomi del foglio -> elenco di etichette «Nome I.» (omonimi: «Nome Ro.», poi tre lettere, poi numero) */
function SM_brevi_(nomi) {
  var pt = nomi.map(function (n, k) { return SM_parti_(n, k); }), lab = [], i, L;
  function etichetta(p, n) {
    var sl = String(p.cog || '').toUpperCase().replace(/[^A-Z\u00c0-\u00dd]/g, '');
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
/* valori della scheda docente -> valori della scheda pubblica (stessa forma, stessa riga 1, nomi brevi, niente email, niente note in fondo) */
function SM_pubValori_(v) {
  var out = [], hi = -1, i, j, nonAbb = 0;
  function pulisci(x) { return typeof x === 'string' ? x.replace(/[^\s,;()<>]+@[^\s,;()<>]+/g, '(email)') : x; }
  for (i = 0; i < v.length; i++) if (String(v[i][0] || '').trim() === 'Stato' && String(v[i][1] || '').trim() === 'Allievo') { hi = i; break; }
  var fine = hi < 0 ? v.length : hi + 1, nomi = [], ult = hi;
  if (hi >= 0) {
    for (i = hi + 1; i < v.length; i++) {
      var st = String(v[i][0] || '').trim();
      if (st !== 'VERDE' && st !== 'ROSSO' && st !== 'ND') break;
      nomi.push(v[i][1]); ult = i;
    }
    for (i = ult + 1; i < v.length; i++) if (/^Email non abbinata/i.test(String(v[i][0] || ''))) nonAbb++;
  }
  var lab = SM_brevi_(nomi);
  for (i = 0; i < fine; i++) {
    var r = v[i].map(pulisci);
    if (i === 0) r[0] = String(r[0]).replace(/\(solo docente, con COGNOME Nome\)/, '(pubblica, solo Nome I.)');
    out.push(r);
  }
  for (i = 0; i < nomi.length; i++) {
    var q = v[hi + 1 + i].map(pulisci);
    q[1] = lab[i];
    out.push(q);
  }
  if (hi >= 0 && nonAbb) { var w = []; for (j = 0; j < v[0].length; j++) w.push(''); w[0] = 'Risposte con email non abbinata: ' + nonAbb + ' (dettaglio nella scheda docente)'; out.push(w); }
  return out;
}
function SM_pubblica_(ss, classe) {
  var src = ss.getSheetByName('Situazione ' + classe);
  if (!src) return;
  var nome = 'Situazione pubblica ' + classe, sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  var rg = src.getDataRange(), vals = SM_pubValori_(rg.getValues()), nc = rg.getNumColumns(), i;
  sh.clear();
  vals = vals.map(function (r) { while (r.length < nc) r.push(''); return r.slice(0, nc); });
  sh.getRange(1, 1, vals.length, nc).setValues(vals);
  try { rg.copyTo(sh.getRange(1, 1), SpreadsheetApp.CopyPasteType.PASTE_FORMAT, false); } catch (e) { }
  try {
    sh.getRange(1, 1).setFontWeight('bold');
    for (i = 1; i <= nc; i++) sh.setColumnWidth(i, src.getColumnWidth(i));
    sh.setFrozenColumns(src.getFrozenColumns());
  } catch (e) { }
}

function FB_situazione_(ss, indice) {
  ['1INF', '2INF', '3INF', '4TI'].forEach(function (c) {
    try { SM_classe_(ss, indice, c); } catch (e) { FB_errore_(ss, 'situazione ' + c, e); }
    try { SM_pubblica_(ss, c); } catch (e) { FB_errore_(ss, 'situazione pubblica ' + c, e); }
  });
}

/* ---------- v2.16: scheda 'Elenco <CLASSE>' (Email, Allievo, Fonte, Nota): iscritti Classroom, altrimenti email dalle schede Ris ---------- */
var EL_DOMINI_ = /@(studenti\.)?piamarta\.it$/i;
function EL_corso_(ss, classe, cfg) {
  var mappa = (cfg && cfg.classi) || {};
  if (!mappa[classe]) return { id: null, av: "in indice.json classroom.classi manca il nome del corso di " + classe };
  var sc = ss.getSheetByName('Corsi'), v, i;
  if (sc) { v = sc.getDataRange().getValues(); for (i = 1; i < v.length; i++) { if (String(v[i][2]) === classe && v[i][1]) return { id: String(v[i][1]) }; } }
  if (typeof Classroom === 'undefined') return { id: null, av: 'Classroom non abilitato (servizio Classroom API da aggiungere in Apps Script)' };
  var corsi = CR_corsi_();
  for (i = 0; i < corsi.length; i++) { if (CR_classe_(corsi[i].name, mappa) === classe) return { id: String(corsi[i].id) }; }
  return { id: null, av: "id del corso Classroom di " + classe + " non trovato (scheda Corsi vuota per questa classe)" };
}
function EL_classroom_(id) {
  var out = [], tok = null, r;
  do {
    r = Classroom.Courses.Students.list(id, { pageSize: 100, pageToken: tok || undefined });
    out = out.concat(r.students || []); tok = r.nextPageToken || null;
  } while (tok);
  return out.map(function (s) {
    var em = String((s.profile && s.profile.emailAddress) || '').trim().toLowerCase(), nota = [];
    if (!em) nota.push('email non visibile (permessi Classroom)');
    else if (!EL_DOMINI_.test(em)) nota.push('dominio da controllare');
    return [em, CR_nome_(s), 'Classroom', nota.join('; ')];
  });
}
function EL_moduli_(ss, indice, classe) {
  var forms = FB_json_('FB_FORMS'), vis = {}, em = [], ut = SM_utenti_(ss, classe), orig = {};
  var shU = ss.getSheetByName('Utenti ' + classe);
  if (shU) shU.getDataRange().getValues().forEach(function (r) { var o = String(r[2] || '').trim(); if (o) orig[SI_norm_(o)] = o; });
  (indice.lavori || []).forEach(function (l) {
    var cl = String((forms[l.id] && forms[l.id].classe) || FB_classe_(l, l.id) || '').toUpperCase();
    if (cl !== classe) return;
    var sh = ss.getSheetByName('Ris ' + l.id);
    if (!sh) return;
    var v = sh.getDataRange().getValues();
    for (var i = 4; i < v.length; i++) {
      var e = String(v[i][0] || '').trim().toLowerCase();
      if (e.indexOf('@') > 0 && !vis[e]) { vis[e] = 1; em.push(e); }
    }
  });
  return em.map(function (e) {
    var n = ut.nomi.length ? SM_abbina_(e, ut.nomi) : null;
    return [e, n ? (orig[n] || n) : '', 'Moduli', EL_DOMINI_.test(e) ? '' : 'dominio da controllare'];
  });
}
function EL_classe_(ss, indice, classe) {
  var cfg = indice.classroom, avvisi = [], righe = null;
  try {
    var co = EL_corso_(ss, classe, cfg);
    if (co.id) {
      righe = EL_classroom_(co.id);
      if (!righe.length) { avvisi.push('Il corso Classroom di ' + classe + ' non ha iscritti visibili: uso le email dei Moduli'); righe = null; }
    } else avvisi.push(co.av + ': uso le email dei Moduli');
  } catch (e) { avvisi.push('Classroom non risponde (' + String(e && e.message || e).slice(0, 120) + '): uso le email dei Moduli'); righe = null; }
  if (!righe) righe = EL_moduli_(ss, indice, classe);
  righe.sort(function (a, b) { var x = (a[1] || '￿') + a[0], y = (b[1] || '￿') + b[0]; return x < y ? -1 : x > y ? 1 : 0; });
  var sh = ss.getSheetByName('Elenco ' + classe) || ss.insertSheet('Elenco ' + classe);
  sh.clear();
  var tutte = [['Email', 'Allievo', 'Fonte', 'Nota']].concat(righe);
  avvisi.forEach(function (a) { tutte.push(['', '', 'Avviso', a]); });
  sh.getRange(1, 1, tutte.length, 4).setValues(tutte);
  sh.getRange(1, 1, 1, 4).setFontWeight('bold').setBackground('#e8eef9');
}
function FB_elenco_(ss, indice) {
  var tab = FB_json_('FB_ELENCO_T'), ora = Date.now(), cambiato = false;
  IX_CLASSI_.forEach(function (c) {
    if (ss.getSheetByName('Elenco ' + c) && ora - Number(tab[c] || 0) < 600000) return;
    try { EL_classe_(ss, indice, c); tab[c] = ora; cambiato = true; } catch (e) { Logger.log('elenco ' + c + ': ' + e); }
  });
  if (cambiato) FB_salva_('FB_ELENCO_T', tab);
}

/* ---------- Indice, ordine e colori delle schede (v2.11) ---------- */
var IX_CLASSI_ = ['1INF', '2INF', '3INF', '4TI'];
var IX_COL_ = { '1INF': '#1e88e5', '2INF': '#43a047', '3INF': '#fb8c00', '4TI': '#8e24aa' };
function IX_classe_(nome) { var m = /(1INF|2INF|3INF|4TI)$/.exec(nome); return m ? m[1] : ''; }
function IX_info_(nome, forms) {
  var c = IX_classe_(nome), m;
  if (nome === 'Indice') return { g: 0, tipo: 'Altro', classe: '', k: '' };
  if (/^Situazione /.test(nome)) return { g: 1, tipo: 'Situazione', classe: c, k: c + (/^Situazione pubblica /.test(nome) ? '2' : '1') };
  if (/^Sicurezza /.test(nome)) return { g: 2, tipo: 'Sicurezza', classe: c, k: c + (/^Sicurezza pubblica /.test(nome) ? '3' : /^Sicurezza storico /.test(nome) ? '2' : '1') };
  if (nome === 'Esiti') return { g: 3, tipo: 'Esiti', classe: '', k: '1' };
  if (nome === 'Quiz') return { g: 3, tipo: 'Esiti', classe: '', k: '2' };
  if (nome === 'Quiz migliori') return { g: 3, tipo: 'Esiti', classe: '', k: '3' };
  if (nome === 'Tipologie lezione') return { g: 4, tipo: 'Esiti', classe: '', k: '' };
  if (/^Utenti /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '1' + c };
  if (/^Consegne /.test(nome)) return { g: 5, tipo: 'Consegne', classe: c, k: '2' + c };
  if (/^(Cruscotto )?Git /.test(nome)) return { g: 5, tipo: 'Git', classe: c, k: '3' + c };
  if (/^Email /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c };
  if (/^Elenco /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c + 'z' };
  if (nome === 'Corsi') return { g: 5, tipo: 'Consegne', classe: '', k: '5' };
  if (m = /^Ris (.+)$/.exec(nome)) {
    var id = m[1], cl = (forms[id] && forms[id].classe) || FB_classe_(null, id) || '';
    return { g: 7, tipo: 'Risposte quiz', classe: String(cl).toUpperCase(), k: id, id: id };
  }
  return { g: 6, tipo: 'Altro', classe: c, k: nome };
}
function IX_agg_(sh) {
  try {
    for (var r = 1; r <= 2; r++) {
      var m = /dati letti (?:alle|il) ([^\u00b7]+)/.exec(String(sh.getRange(r, 1).getValues()[0][0] || ''));
      if (m) return m[1].trim();
    }
    if (sh.getName() === 'Stato') { var v = String(sh.getRange(1, 2).getValues()[0][0] || ''); if (v) return v; }
  } catch (e) { }
  return 'non scritto';
}
function FB_schede_(ss, indice) {
  var forms = FB_json_('FB_FORMS'), attuali = {}, hide = !!indice;
  if (indice) (indice.lavori || []).forEach(function (l) { attuali[l.id] = true; });
  if (!ss.getSheetByName('Stato')) ss.insertSheet('Stato');
  var ix = ss.getSheetByName('Indice') || ss.insertSheet('Indice');
  /* 1) orfane nascoste (mai cancellate), attuali rimostrate, colori */
  ss.getSheets().forEach(function (sh) {
    var nome = sh.getName(), i = IX_info_(nome, forms), col = null;
    try {
      if (i.g === 7 && hide) {
        if (attuali[i.id]) { if (sh.isSheetHidden()) sh.showSheet(); col = IX_COL_[i.classe] || null; }
        else { if (!sh.isSheetHidden()) sh.hideSheet(); col = '#9e9e9e'; }
      } else if (i.g === 7) col = IX_COL_[i.classe] || null;
      else if (i.g === 1) col = /^Situazione pubblica /.test(nome) ? '#80cbc4' : '#00897b';
      else if (i.g === 2) col = '#c62828';
      else if (i.g === 0) col = '#616161';
      if (col) sh.setTabColor(col);
    } catch (e) { FB_errore_(ss, 'scheda ' + nome, e); }
  });
  /* 2) ordine fisso */
  var tutte = ss.getSheets().map(function (sh) { var i = IX_info_(sh.getName(), forms); return { sh: sh, nome: sh.getName(), g: i.g, k: i.k, c: IX_CLASSI_.indexOf(i.classe) < 0 ? 9 : IX_CLASSI_.indexOf(i.classe) }; });
  tutte.sort(function (a, b) {
    if (a.g !== b.g) return a.g - b.g;
    if (a.g === 7) { if (a.c !== b.c) return a.c - b.c; }
    if (a.g === 1) { if (a.c !== b.c) return a.c - b.c; }
    if (a.g === 2) { if (a.c !== b.c) return a.c - b.c; }
    return a.k < b.k ? -1 : a.k > b.k ? 1 : 0;
  });
  var cur = ss.getSheets().map(function (sh) { return sh.getName(); });
  tutte.forEach(function (t, p) {
    if (cur[p] === t.nome) return;
    try { ss.setActiveSheet(t.sh); ss.moveActiveSheet(p + 1); cur.splice(cur.indexOf(t.nome), 1); cur.splice(p, 0, t.nome); } catch (e) { FB_errore_(ss, 'ordine ' + t.nome, e); }
  });
  /* 3) scheda Indice (solo link e testo, nessun dato altrui) */
  var righe = [], forme = [];
  tutte.forEach(function (t) {
    var i = IX_info_(t.nome, forms), nasc = false;
    try { nasc = t.sh.isSheetHidden(); } catch (e) { }
    righe.push([t.nome, i.tipo, i.classe || '-', IX_agg_(t.sh), nasc ? 'Nascosta' : 'Visibile']);
    forme.push({ t: t.nome, u: '#gid=' + t.sh.getSheetId() });
  });
  ix.clear();
  ix.getRange(1, 1).setValue('Indice delle schede (' + righe.length + ') \u00b7 aggiornato alle ' + FB_ora_('HH:mm:ss') + ' \u00b7 clicca il nome per aprire; le schede Nascosta si rimostrano da Visualizza > Fogli nascosti').setFontWeight('bold');
  /* v2.12: colonne di TESTO per il Pannello (il CSV pubblicato non porta gli URL delle formule) */
  var base = 'https://docs.google.com/spreadsheets/d/' + ss.getId() + '/edit#gid=';
  var TLS = { 'Git': FB_TL_.versioning, 'Consegne': FB_TL_.esercitazione, 'Risposte quiz': FB_TL_.quiz };
  var rs = righe.length;
  righe = righe.map(function (r, n) { return r.concat([base + tutte[n].sh.getSheetId(), '', '', TLS[r[1]] || '']); });
  var ids = {}, qr = [];
  try {
    var es = ss.getSheetByName('Esiti').getDataRange().getValues();
    for (var q = 1; q < es.length; q++) ids[es[q][1]] = { t: es[q][2], l: String(es[q][3] || '') };
  } catch (e) { FB_errore_(ss, 'indice quiz', e); }
  var vistiQ = {}, correnti = {};
  if (indice) (indice.lavori || []).forEach(function (l) { correnti[l.id] = 1; });
  if (indice) (indice.lavori || []).forEach(function (l) {
    var x = ids[l.id], f = forms[l.id];
    if (!x || !/^https:\/\/docs\.google\.com\/forms\/d\/e\/[^\/\s]+\/viewform/.test(x.l)) return;
    if (vistiQ[l.id]) return; vistiQ[l.id] = 1;
    qr.push([l.id, 'Quiz', String((f && f.classe) || FB_classe_(null, l.id) || '-').toUpperCase(), '-', 'Attivo', '', (f && f.titolo) || x.t || l.id, x.l.split('#')[0], FB_TL_[FB_tl_(l, l.id)]]);
  });
  /* v2.14: id di Esiti non piu in indice.json = Moduli sostituiti: riga nascosta, senza link */
  if (indice) Object.keys(ids).forEach(function (k) {
    if (!k || correnti[k]) return;
    qr.push([k, 'Quiz (vecchio)', String(FB_classe_(null, k) || '-').toUpperCase(), '-', 'Nascosta', '', ids[k].t || k, '', '']);
  });
  var tot = righe.concat(qr);
  ix.getRange(3, 1, 1, 9).setValues([['Scheda', 'Tipo', 'Classe', 'Ultimo aggiornamento', 'Stato', 'URL', 'Titolo', 'Link ragazzi', 'Tipologia lezione']]).setFontWeight('bold');
  ix.getRange(4, 1, tot.length, 9).setValues(tot);
  FB_linkCelle_(ix, 4, 1, forme);
  ix.setColumnWidth(1, 260);
  ix.setFrozenRows(3);
}

/* ---------- Giro principale ---------- */
/* ---------- Tipologie lezione per classe (v2.8) ---------- */
function FB_matrice_(ss, indice) {
  var classi = ['1INF', '2INF', '3INF', '4TI'], forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR');
  var lavori = {};
  (indice.lavori || []).forEach(function (l) { lavori[l.id] = l; });
  function ora_(nome) {
    var sh = ss.getSheetByName(nome);
    if (!sh) return null;
    var m = /dati letti alle (\d\d:\d\d:\d\d)/.exec(String(sh.getRange(1, 1).getValues()[0][0] || ''));
    var v = sh.getDataRange().getValues(), n = 0, i;
    for (i = 4; i < v.length; i++) if (v[i] && String(v[i][1] || '').trim()) n++;
    return { ora: m ? m[1] : 'ora non scritta', n: n };
  }
  var righe = classi.map(function (c) {
    var cr = ora_('Consegne ' + c), gt = ora_('Git ' + c), uso = ss.getSheetByName('Utenti ' + c);
    var nq = 0, ns = 0, rq = 0, rs = 0, id;
    for (id in forms) {
      if ((forms[id].classe || FB_classe_(null, id)) !== c) continue;
      if (FB_tl_(lavori[id], id) === 'teoria') { ns++; rs += Number(nr[id]) || 0; } else { nq++; rq += Number(nr[id]) || 0; }
    }
    var lazarus = cr ? 'OK: Consegne ' + c + ', ' + cr.n + ' allievi, dati alle ' + cr.ora + (gt ? ' · progetto Lazarus nella scheda Git' : ' · manca la scheda Git') : 'MANCA: scheda Consegne ' + c + ' (corso Classroom non trovato o servizio Classroom non abilitato)';
    var vers = gt ? 'OK: Git ' + c + ', ' + gt.n + ' allievi, dati alle ' + gt.ora : (uso && uso.getDataRange().getValues().length > 1 ? 'IN ATTESA: scheda Git ' + c + ' al prossimo giro' : 'MANCA: scheda Utenti ' + c + ' da compilare (PC, Utente GitHub, Allievo)');
    return [c, lazarus, nq ? 'OK: ' + nq + ' Moduli, ' + rq + ' risposte' : 'MANCA: nessun Moduli quiz in indice.json', vers, ns ? 'OK: ' + ns + ' schede, ' + rs + ' risposte' : 'MANCA: nessuna scheda in indice.json'];
  });
  var sh = ss.getSheetByName('Tipologie lezione') || ss.insertSheet('Tipologie lezione');
  sh.clear();
  sh.getRange(1, 1).setValue('Classi x TIPOLOGIA LEZIONE (nessun nome di allievo) · dati letti alle ' + FB_ora_('HH:mm:ss')).setFontWeight('bold');
  sh.getRange(3, 1, 1, 5).setValues([['Classe \\ TIPOLOGIA LEZIONE', FB_TL_.esercitazione, FB_TL_.quiz, FB_TL_.versioning, FB_TL_.teoria]]).setFontWeight('bold');
  sh.getRange(4, 1, righe.length, 5).setValues(righe);
}

function FB_main_() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var t0 = Date.now();
    FB_ERRS = [];
    FB_lavoroIndice_ = {};
    var ss = FB_foglio_(), indice = { lavori: [] };
    try { FB_pulisci_(ss); } catch (e) { FB_errore_(ss, 'pulizia', e); }
    try { indice = JSON.parse(FB_get_(FB_BASE + 'indice.json')); } catch (e) { FB_errore_(ss, 'indice', e); indice = null; }
    if (indice) {
      (indice.lavori || []).forEach(function (l) { FB_lavoroIndice_[l.id] = l; });
      try { FB_nuovi_(ss, indice); } catch (e) { FB_errore_(ss, 'nuovi', e); }
    }
    try { FB_ripara_(ss); } catch (e) { FB_errore_(ss, 'ripara', e); }
    try { FB_risultati_(ss, t0); } catch (e) { FB_errore_(ss, 'risultati', e); }
    try { FB_quiz_(ss); } catch (e) { FB_errore_(ss, 'quiz', e); }
    if (indice) {
      try { FB_cruscotti_(ss, indice); } catch (e) { FB_errore_(ss, 'cruscotti', e); }
    }
    if (indice) {
      try { FB_classroom_(ss, indice, t0); } catch (e) { FB_errore_(ss, 'classroom', e); }
    }
    if (indice) {
      try { FB_elenco_(ss, indice); } catch (e) { FB_errore_(ss, 'elenco', e); }
    }
    if (indice) {
      try { FB_git_(ss, indice, t0); } catch (e) { FB_errore_(ss, 'git', e); }
    }
    if (indice) {
      try { FB_sicurezza_(ss, indice); } catch (e) { FB_errore_(ss, 'sicurezza', e); }
    }
    if (indice) {
      try { FB_matrice_(ss, indice); } catch (e) { FB_errore_(ss, 'tipologie lezione', e); }
    }
    if (indice) {
      try { FB_situazione_(ss, indice); } catch (e) { FB_errore_(ss, 'situazione', e); }
    }
    try { FB_schede_(ss, indice); } catch (e) { FB_errore_(ss, 'schede', e); }
    try { FB_stato_(ss); } catch (e) { Logger.log('stato: ' + e); }
  } finally {
    lock.releaseLock();
  }
}
