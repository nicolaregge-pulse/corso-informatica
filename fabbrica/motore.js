/**
 * FABBRICA - MOTORE v2.22 (13/11/2026)
 * Codice puro: lo scarica ed esegue (eval) il "lancio" a ogni giro. Usa le globali del lancio FB_BASE e UTENTI
 * ({ '3INF': [[pc, utenteGitHub, 'COGNOME Nome'], ...] }) e i servizi Google. Chiama FB_main_() dopo l'eval.
 * Properties usate: FB_FOGLIO, FB_FATTI, GITHUB_TOKEN (da v1), FB_FORMS, FB_NR, FB_ULTERR (nuove).
 * TIPOLOGIA LEZIONE (decisione del docente 11/11/2026, v2.8): le 4 tipologie sono Esercitazione Lazarus (schede Consegne <CLASSE> + progetto Lazarus nella scheda Git), Quiz su Moduli, Versioning su GitHub (schede Utenti e Git <CLASSE>), Teoria a schede (Moduli creato da una scheda). Nei lavori di indice.json il campo e "tipologia_lezione" ("quiz" o "teoria"; il vecchio nome "tipologia" o "tipo" e accettato; se manca: id che comincia per "scheda-" = teoria, altrimenti quiz). Il "tipo" delle domande (multi, singola, testo, paragrafo) e un'altra cosa e non cambia.
 * Changelog: 2.22 (13/11/2026; 'Stato' ha una riga 'Permessi' con i permessi che il progetto ha davvero e quelli che mancano, su richiesta del docente: «il cruscotto deve avere i dati che chiedo, senza condivisioni a mano») include la 2.21 e aggiunge DUE schede nuove, nessun dato e nessuna scheda esistente cambiano: (a) 'Risposte <id quiz>' per ogni Moduli (solo docente): una riga per invio con Ora invio, Allievo (COGNOME Nome da 'Elenco' e 'Abbinamenti'), Email, Tentativo, Punteggio, Su, Migliore, il TESTO della risposta a ogni domanda (D1..DN, comprese le aperte) e i punti per domanda (P1..PN; 'da correggere' per un'aperta con risposta e punteggio 0 o vuoto), con in fondo il blocco ERRORI RICORRENTI (per domanda: quanti allievi hanno sbagliato, quanti da correggere, quanti giusto); si scrive insieme a 'Ris <id>' e, per i Moduli gia letti, al primo giro dopo l'aggiornamento (al massimo 5 Moduli per giro); (b) 'Documenti <CLASSE>' (solo docente) e 'Documenti pubblica <CLASSE>' (solo 'Nome I.', senza email, link, titolo del file e testo) per ogni classe con corso Classroom: per ogni allievo e per ognuno degli ultimi 6 compiti di tipo Documento (assegnazione con un file Drive 'una copia per ogni allievo' o titolo 'G/M Ora N: ...') stato (ASSEGNATO, CONSEGNATO, IN RITARDO, RESTITUITO), ora di consegna, file allegato (titolo, id, link), ultima modifica, immagini totali, immagini del modello, immagini aggiunte, caratteri ed estratto di 300 caratteri del testo; il Documento si legge esportandolo in HTML con il token del progetto (nessun scope nuovo: serve quello di Drive che il lancio gia chiede con DriveApp), si rilegge solo se l'ultima modifica e cambiata, al massimo 24 esportazioni per giro, una classe per giro, ogni 5 minuti per classe; indice.json puo avere classroom.documenti = {attivo, ultimi, ogni_minuti, titolo, classi, max_letture}, senza il campo valgono questi valori; 'Stato' dice Motore 2.22. 2.21 (12/11/2026 sera, due correzioni, nessuna funzione nuova) (a) NOMI COMPOSTI 4TI: la scheda 'Situazione pubblica' (e ogni scheda pubblica che usa SM_brevi_) scriveva un secondo cognome nell'etichetta 'Nome I.' quando il nome del foglio e tutto maiuscolo con piu di due parole (per esempio 'ROSSI BIANCHI MARIO LUCA' dava 'Bianchi Mario Luca R.'); ora, se il confine cognome/nome non si puo sapere, si tiene come nome SOLO l'ultima parola (nel registro l'ordine e COGNOME(I) NOME(I)); (b) DOMANDE APERTE: la colonna 'Domande aperte da correggere' delle schede 'Ris' era 0 anche con aperte non corrette (il punteggio di una risposta libera non e null) e sommava i tentativi; ora conta le risposte non vuote alle domande aperte con punti il cui punteggio e null o 0, solo per il tentativo migliore. 2.20 VERSIONI DELLO STESSO QUIZ: campo opzionale `versioni: [id1, id2, ...]` sul lavoro attivo di indice.json (dal piu vecchio al piu recente; l'id attivo e sempre l'ultimo). Le schede 'Situazione <CLASSE>' (e la pubblica), 'Elenco <CLASSE>' (righe Moduli), gli abbinamenti e quindi il cruscotto contano UN solo quiz (una colonna, l'id attivo) e per ogni allievo prendono il risultato MIGLIORE tra le versioni (a parita il piu recente); se il migliore non e dell'ultima versione la cella aggiunge ' · fatto sulla versione precedente'. Le schede 'Ris <id>' delle versioni vecchie si leggono anche se nell'Indice sono 'Quiz (vecchio)' o nascoste; un id di versioni non creato (non in FB_FORMS) o di un'altra classe e ignorato; un lavoro elencato come versione di un altro non ha piu una colonna sua. MANCA vale solo se TUTTE le versioni create sono state lette (altrimenti 'dato non letto'); punteggi e significato di MANCA e NON ABBINATA invariati; senza il campo il comportamento e identico alla 2.19. 2.19 schede 'Consegne <CLASSE>' per i compiti di laboratorio (2INF; indice.json classroom.laboratorio): il motore legge da Classroom (id del corso dalla scheda Corsi) i compiti pubblicati con titolo 'G/M Ora N: argomento' del giorno piu recente (o del giorno fissato), e per ogni allievo scrive CONSEGNATO, RICONSEGNATO (restituito dal docente o consegnato di nuovo dopo la restituzione: conta come consegnato) oppure ASSEGNATO (da consegnare), conteggi Consegnati/Totali/Mancanti; nuova scheda 'Consegne pubblica <CLASSE>' con solo 'Nome I.' e nessuna email (stessa riga 1 con l'ora del dato); ogni classe Classroom ha il suo intervallo (laboratorio 2 minuti, le altre 10) e si leggono le classi dovute (al massimo 2 per giro) invece di una sola scelta dal minuto dell'ora (con il giro a minuti pari una classe poteva non avere mai il suo turno); il nome del corso si cerca anche senza badare a maiuscole e spazi e puo essere un elenco; se il corso di una classe di laboratorio non si trova, lo dice 'Ultimo errore' in Stato; le altre schede Consegne restano come prima; nessuna nuova tipologia lezione (il motore legge per classe e per titolo, non per tipologia); 2.18 abbinamento automatico email -> allievo nella scheda 'Situazione <CLASSE>' (per ogni classe con elenco di nomi): per ogni email che ha risposto a un quiz della classe e non e abbinata (scheda Email, Elenco Classroom o abbinamenti gia salvati) il motore prova prima la regola v2.15 (nome e cognome interi, qualunque ordine, qualunque dominio) poi, SOLO con dominio studenti.piamarta.it o piamarta.it, iniziale+cognome, nome+iniziale del cognome, cognome senza particella (De, El, Al, D'), primo nome di un nome composto, accenti e numeri finali ignorati; 'quasi uguale' (una lettera di differenza) e 'solo cognome' valgono solo come candidato; abbinamento SICURO = punteggio 85 o piu, un solo candidato ad almeno 15 punti sopra gli altri, e allievo libero (senza altra email) se il punteggio non e 100; gli abbinamenti sicuri si scrivono nella nuova scheda 'Abbinamenti <CLASSE>' (Email, Allievo, Fonte auto o docente, Aggiornato, Nota; mai cancellati; una riga con Allievo '-' = email da ignorare); i dubbi nella nuova scheda 'Abbinamenti da confermare <CLASSE>' (Email, Quiz, fino a 3 candidati, colonna Scelta dove il docente scrive OK = candidato 1, oppure 1, 2, 3, oppure NO = nessuno, oppure COGNOME Nome); al giro dopo il motore applica la scelta e la copia in 'Abbinamenti <CLASSE>' con Fonte docente; nella Situazione la cella e MANCA solo se l'allievo ha una email abbinata (nessuna risposta) oppure se per quel quiz non resta nessuna risposta da abbinare; altrimenti NON ABBINATA (risposte arrivate ma da abbinare, non contata come mancante ne come fatta); Stato ND per chi ha celle NON ABBINATA e nessun MANCA; riepilogo e riga 4 con i due conteggi separati; nuova colonna finale NON ABBINATA; la Situazione pubblica li copia senza email; 'Elenco <CLASSE>' (Moduli) e 'Sicurezza <CLASSE>' leggono 'Abbinamenti <CLASSE>'; 2.17 nuova scheda 'Situazione pubblica <CLASSE>' (1INF, 2INF, 3INF, 4TI) da pubblicare sul web per docs/cruscotto/: stesse colonne e stessa riga 1 (ora del dato) della scheda 'Situazione <CLASSE>', ma Allievo in formato 'Nome I.' (nome + iniziale del cognome, cognomi composti con particelle De, Di, El, Al ecc. gestiti, omonimi distinti con due lettere), SENZA email, SENZA note in fondo e SENZA altri dati personali (ogni email residua nei testi diventa '(email)'); se Allievo e un'email diventa 'Nome C.' dalla parte prima della chiocciola, altrimenti 'Allievo n'; la scheda 'Situazione <CLASSE>' con COGNOME Nome resta solo docente e invariata; la scheda pubblica in Indice come tipo Situazione (dopo quella docente), colore piu chiaro; 2.16 nuova scheda 'Elenco <CLASSE>' (colonne Email, Allievo COGNOME Nome come in Classroom, Fonte, Nota) per 1INF, 2INF, 3INF, 4TI: fonte primaria gli iscritti del corso Classroom (id dalla scheda Corsi, Courses.Students.list), fallback le email distinte delle schede 'Ris <id>' dei quiz attuali della classe (Allievo da 'Utenti <CLASSE>' per nome.cognome, abbinamento ambiguo = vuoto, Fonte 'Moduli'); una 'Email <CLASSE>' gia presente NON e mai sovrascritta (la scheda generata e separata); Situazione e Sicurezza leggono 'Email <CLASSE>' se c'e', altrimenti 'Elenco <CLASSE>' (solo righe Fonte Classroom); email con dominio diverso da studenti.piamarta.it e piamarta.it segnate 'dominio da controllare' in Nota (mai corrette); se l'API Classroom non risponde nessun errore: riga Avviso nella scheda e fallback; scheda Elenco in Indice come tipo Utenti; rilettura al massimo ogni 10 minuti; 2.15 scheda 'Situazione <CLASSE>': se mancano 'Email <CLASSE>' e 'Consegne <CLASSE>' l'elenco allievi viene dalla scheda 'Utenti <CLASSE>' (colonna C Allievo, COGNOME Nome), cosi chi non ha risposto a nessun quiz compare con MANCA; le email delle risposte si abbinano agli allievi per nome.cognome (riga 4: quanti abbinati e quanti no); avviso con il gesto preciso da fare (account PIAMARTA, un passo); 2.14 scheda 'Indice': righe 'Quiz' SOLO per gli id correnti di indice.json (una sola riga per id, Stato 'Attivo'); gli id vecchi di Esiti (Moduli sostituiti) diventano righe 'Quiz (vecchio)' con Stato 'Nascosta' e SENZA Link ragazzi, cosi il Pannello non li mostra; 2.13 FIX scheda 'Indice' e 'Quiz': niente piu formule HYPERLINK (il foglio e in italiano e rifiutava la virgola: #ERROR!); la colonna A di Indice e la colonna G di Quiz sono TESTO semplice (nome della scheda / 'Apri risultati'), il link cliccabile e messo con RichTextValue (setLinkUrl, indipendente dalla lingua) e, se non riesce, resta il testo; le righe 'Quiz' dell'Indice hanno Titolo e Link ragazzi da Esiti colonna D (mai link di modifica); 2.12 scheda 'Indice' con colonne in TESTO semplice per il Pannello (pagina docs/pannello/, che legge il CSV pubblicato): F = URL completo https://docs.google.com/spreadsheets/d/<id>/edit#gid=<gid> di ogni scheda, G = Titolo, H = Link ragazzi (solo viewform pubblico preso da Esiti colonna D, MAI il link di modifica), I = Tipologia lezione; una riga 'Quiz' per ogni lavoro di indice.json con link valido; nessun cognome, nessuna email; 2.11 scheda 'Indice' come prima scheda (una riga per scheda: nome con link HYPERLINK al gid, tipo, classe, ultimo aggiornamento, nascosta; raggruppata per tipo); ordine fisso delle schede a ogni giro (Indice, Situazione, Sicurezza, Esiti e Quiz, Tipologie lezione, Utenti/Consegne/Git/Email/Corsi, Altro, poi le 'Ris <id>' in fondo); le 'Ris <id>' ORFANE (id non piu in indice.json lavori) sono NASCOSTE con hideSheet e MAI cancellate (se l'id torna nell'indice si rimostrano); schede colorate (Ris per classe: 1INF blu, 2INF verde, 3INF arancio, 4TI viola, orfane grigie; Situazione e Sicurezza di un colore proprio); nessun dato e nessun id toccato; 2.10 intestazioni dei quiz nelle schede 'Situazione <CLASSE>' e 'Sicurezza <CLASSE>' in 3 righe (A = ora e argomento breve ricavati dal titolo del quiz, per esempio 'Sic. ora 5 \u00b7 infortuni'; B = data; C = id del quiz), mai troncate, testo a capo, larghezza colonna, riga intestazione alta, prime colonne congelate; se due intestazioni coincidono si aggiunge l'id alla riga A; id e Moduli invariati; 2.9 nuova scheda \'Situazione <CLASSE>\' (1INF, 2INF, 3INF, 4TI; solo docente, con COGNOME Nome): una riga per allievo, una colonna per ogni quiz della classe in indice.json (ordine di creazione, intestazione = titolo breve + data), cella = miglior % (punti/totale) o MANCA, riga \'Letto alle\' per ogni Moduli, colonne Fatti/totali, Media % dei fatti, NON HA FATTO, riepilogo in cima, colori verde >=80 / giallo <80 / rosso MANCA, (provv.) per le aperte non corrette; elenco allievi come Sicurezza (Email o Consegne), altrimenti email dalle schede Ris (dichiarato); schede e id esistenti invariati; 2.8 (a) controllo della richiesta PRIMA di creare il Moduli (titolo, domande, scelte, una sola giusta nelle singole): se non va, nessun Moduli e l'errore sta in Stato; (b) se la lettura o il controllo della richiesta falliscono, il lavoro NON e segnato come fatto e viene riprovato al giro dopo (prima restava perso per sempre); un Moduli gia creato non si ricrea mai; (c) avvisi lingua R6 non bloccanti nella colonna Controllo (1INF italiano+arabo+cinese; 2INF e 4TI solo italiano; 3INF niente arabo e cinese, il bangla e ammesso); (d) scheda 'Quiz' con colonna TIPOLOGIA LEZIONE; (e) nuova scheda 'Tipologie lezione' (classi x TIPOLOGIA LEZIONE, stato e ora del dato); (f) se manca 'Utenti <CLASSE>' la scheda vuota con l'intestazione viene creata (il docente incolla PC, utente GitHub, allievo); (g) Stato mostra la versione del motore; 2.7 Sicurezza per classe: indice.json "sicurezza" puo essere un elenco di classi (1INF, 2INF), ogni classe con le sue ore, ids e soglia; schede 'Email <CLASSE>', 'Consegne <CLASSE>', 'Sicurezza storico <CLASSE>' e 'Sicurezza <CLASSE>' (solo docente, COGNOME Nome); nuova scheda 'Sicurezza pubblica <CLASSE>' SENZA nomi (colonna Id = SHA-256 del nome in maiuscolo, il «Nome I.» lo mette la pagina docs/sicurezza-cruscotto/ da nomi.json) da pubblicare sul web per il cruscotto; 2.6 scheda 'Sicurezza 1INF' (solo docente, con COGNOME Nome): una riga per allievo, colonne ora 1-4 (da scheda 'Sicurezza storico 1INF'), 5, 6A, 6B (dalle schede 'Ris <id>' di indice.json "sicurezza") e Recupero, stato OK/DA RECUPERARE/MANCA/ASSENTE con soglia 80, colonne DA FARE ORA e DA RIFARE (sotto 80); elenco allievi ed email dalla scheda 'Email 1INF' oppure da 'Consegne 1INF'; 2.5 schede 'Ris <id>' con titolo del quiz in A1, riga A2 (Classe, id, data, ora, risposte), intestazione riga 4, dati dalla riga 5, colonna Domande aperte da correggere; nuova scheda 'Quiz' (prima dopo 'Esiti') con una riga per Modulo e link alla scheda dei risultati; 'Quiz migliori' legge dalla riga 5; 2.4 modulo GIT (scheda 'Git <CLASSE>' per ogni classe di indice.json "git", elenco dalla scheda 'Utenti <CLASSE>' A=PC B=Utente C=Allievo, una classe per giro, ogni classe al massimo ogni ogni_minuti, Progetto/README/Commit totali); 2.3 modulo CLASSROOM (schede 'Corsi' e 'Consegne <CLASSE>', una classe per giro, mappa in indice.json); 2.2 errori in una sola riga di 'Stato' (Ultimo errore), mai piu righe ERRORE in 'Esiti' (pulite a ogni giro); 2.1 elenco ragazzi letto dalla scheda 'Cruscotto Git <classe>' (UTENTI del lancio puo essere {}); 2.0 tutte le classi, registro Moduli, risultati (schede "Ris <id>"), scheda "Stato", cruscotti per classe.
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

/* v2.22: i permessi (scope OAuth) che il progetto ha davvero, letti dal token con tokeninfo di Google (nessun permesso in piu): scritti in 'Stato' riga 'Permessi' (ogni 30 minuti) */
var FB_SCOPE_RICHIESTI_ = [
  ['Moduli (forms)', ['https://www.googleapis.com/auth/forms']],
  ['Drive (DriveApp: lettura dei Documenti)', ['https://www.googleapis.com/auth/drive']],
  ['Fogli (spreadsheets)', ['https://www.googleapis.com/auth/spreadsheets']],
  ['Classroom: corsi', ['https://www.googleapis.com/auth/classroom.courses', 'https://www.googleapis.com/auth/classroom.courses.readonly']],
  ['Classroom: elenco allievi', ['https://www.googleapis.com/auth/classroom.rosters', 'https://www.googleapis.com/auth/classroom.rosters.readonly']],
  ['Classroom: consegne e allegati', ['https://www.googleapis.com/auth/classroom.coursework.students', 'https://www.googleapis.com/auth/classroom.coursework.students.readonly']],
  ['Classroom: email degli allievi', ['https://www.googleapis.com/auth/classroom.profile.emails']]
];
function FB_permessi_() {
  var p = FB_json_('FB_PERM'), ora = Date.now(), txt;
  if (p.t && ora - p.t < 1800000 && p.txt) return p.txt;
  try {
    var r = UrlFetchApp.fetch('https://oauth2.googleapis.com/tokeninfo?access_token=' + encodeURIComponent(ScriptApp.getOAuthToken()), { muteHttpExceptions: true });
    var j = {};
    try { j = JSON.parse(r.getContentText() || '{}') || {}; } catch (e1) { j = {}; }
    var sc = String(j.scope || '');
    if (!sc) txt = 'non letti (tokeninfo HTTP ' + r.getResponseCode() + ')';
    else {
      var have = sc.split(/\s+/), mancano = [];
      FB_SCOPE_RICHIESTI_.forEach(function (x) { if (!x[1].some(function (u) { return have.indexOf(u) >= 0; })) mancano.push(x[0]); });
      txt = mancano.length ? 'MANCANO: ' + mancano.join(', ') : 'OK (' + have.length + ' permessi, ci sono tutti quelli che servono)';
    }
  } catch (e) { txt = 'non letti: ' + String(e && e.message ? e.message : e).slice(0, 100); }
  FB_salva_('FB_PERM', { t: ora, txt: txt });
  return txt;
}

function FB_stato_(ss) {
  var sh = ss.getSheetByName('Stato') || ss.insertSheet('Stato');
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), tot = 0, k, n = 0;
  for (k in forms) n++;
  for (k in nr) tot += Number(nr[k]) || 0;
  sh.getRange(1, 1, 6, 2).setValues([
    ['Fabbrica v2', FB_ora_('dd/MM/yyyy HH:mm:ss')],
    ['Moduli', n],
    ['Risposte totali', tot],
    ['Ultimo errore', FB_ultimoErrore_()],
    ['Motore', '2.22'],
    ['Permessi', FB_permessi_()]
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

/* v2.21: le domande aperte (testo breve o paragrafo) con punti > 0 del Modulo */
function FB_aperteItems_(form) {
  var out = [];
  form.getItems().forEach(function (it) {
    try {
      var t = it.getType(), T = FormApp.ItemType, x = null;
      if (t === T.TEXT) x = it.asTextItem();
      else if (t === T.PARAGRAPH_TEXT) x = it.asParagraphTextItem();
      if (x && (Number(x.getPoints()) || 0) > 0) out.push(it);
    } catch (e) { }
  });
  return out;
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
      if (nr[id] === n && g0 && g0.getRange(4, 1).getValues()[0][0] === 'Email' && ss.getSheetByName('Risposte ' + id)) continue;
      var su = FB_puntiTotali_(form), per = {}, apItems = FB_aperteItems_(form);
      ris.forEach(function (r) {
        var em = r.getRespondentEmail() || '(senza email)', s = 0, ap = 0, p0 = per[em] || (per[em] = { max: -1, t: 0, ult: null, aperte: 0 });
        (r.getGradableItemResponses() || []).forEach(function (g) { s += Number(g.getScore()) || 0; });
        /* v2.21: aperte da correggere dalla struttura del Modulo: risposta non vuota a una domanda aperta con punti e punteggio null o 0 (uno 0 dato dal docente conta ancora: provvisorio, mai il contrario) */
        apItems.forEach(function (it) {
          try {
            var ir = r.getResponseForItem(it);
            if (!ir) return;
            var v = ir.getResponse();
            if (v === null || v === undefined || String(v).replace(/\s+/g, '') === '') return;
            var sc2 = ir.getScore ? ir.getScore() : null;
            if (sc2 === null || sc2 === undefined || Number(sc2) === 0) ap++;
          } catch (e) { }
        });
        var ts = r.getTimestamp(), p = p0;
        if (s > p.max || (s === p.max && (!p.ult || ts >= p.ult))) { p.max = s; p.aperte = ap; }
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
      /* v2.22: scheda 'Risposte <id>' (risposte per domanda); un errore qui non blocca 'Ris <id>' */
      try { RS_risposte_(ss, id, form, forms[id], ris, su); } catch (e2) { FB_errore_(ss, 'risposte ' + id, e2); }
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
function CR_norm_(t) { return String(t || '').toLowerCase().replace(/\s+/g, ' ').trim(); }
function CR_classe_(nome, mappa) {
  for (var c in mappa) { if (mappa[c] && String(nome).indexOf(mappa[c]) >= 0) return c; }
  /* v2.19: seconda prova senza maiuscole e con spazi uguali; il valore puo essere anche un elenco di nomi */
  for (var c2 in mappa) {
    var v = mappa[c2], l = Object.prototype.toString.call(v) === '[object Array]' ? v : [v];
    for (var i = 0; i < l.length; i++) { if (l[i] && CR_norm_(nome).indexOf(CR_norm_(l[i])) >= 0) return c2; }
  }
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
  var lab = CR_lab_(cfg, classe);
  if (lab) { CR_labScheda_(ss, classe, id, studenti, lavori, lab); return; }
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
  for (var k in mappa) {
    if (trovati[k]) ordine.push(k);
    else if (CR_lab_(cfg, k)) FB_ERRS.push("Consegne " + k + ": corso Classroom non trovato (cerco un corso attivo il cui nome contiene '" + (Object.prototype.toString.call(mappa[k]) === '[object Array]' ? mappa[k].join("' o '") : mappa[k]) + "'; nomi dei corsi nella scheda Corsi)");
  }
  if (!ordine.length) return;
  /* v2.19: ogni classe ha il suo intervallo (laboratorio: 2 minuti, le altre: ogni_minuti, 10) e si leggono le classi dovute, la piu vecchia prima, al massimo 2 per giro; prima si leggeva una classe sola in base al minuto dell'ora e una classe poteva non toccare mai il suo turno */
  var T = FB_json_('FB_CR_T'), ora = Date.now(), dovute = [];
  ordine.forEach(function (c) {
    var lb = CR_lab_(cfg, c), mx = (lb ? lb.ogni : (Number(cfg.ogni_minuti) || 10)) * 60000 - 20000;
    var nome = 'Consegne ' + c;
    if (!ss.getSheetByName(nome) || ora - Number(T[c] || 0) >= mx) dovute.push(c);
  });
  dovute.sort(function (a, b) {
    var la = CR_lab_(cfg, a) ? 0 : 1, lb2 = CR_lab_(cfg, b) ? 0 : 1;
    return la - lb2 || Number(T[a] || 0) - Number(T[b] || 0);
  });
  dovute.slice(0, 2).forEach(function (cl) {
    if (Date.now() - t0 > 200000) return;
    try { CR_scheda_(ss, cl, trovati[cl], cfg); T[cl] = Date.now(); FB_salva_('FB_CR_T', T); }
    catch (e) { FB_errore_(ss, 'Consegne ' + cl, e); }
  });
}

/* ---------- v2.19: Consegne dei compiti di laboratorio per classe (2INF): un compito di Classroom «G/M Ora N: argomento» ---------- */
function CR_lab_(cfg, classe) {
  var l = cfg && cfg.laboratorio && cfg.laboratorio[classe];
  if (!l) return null;
  if (l === true) l = {};
  return { titolo: l.titolo || '^\\s*\\d{1,2}\\s*/\\s*\\d{1,2}\\s+Ora\\s*\\d', giorno: String(l.giorno || ''), ogni: Number(l.ogni_minuti) || 2 };
}
function CR_giorno_(t) {
  var m = /^\s*(\d{1,2})\s*\/\s*(\d{1,2})/.exec(String(t || ''));
  return m ? ('0' + m[1]).slice(-2) + '/' + ('0' + m[2]).slice(-2) : '';
}
function CR_oraN_(t) { var m = /Ora\s*(\d+)/i.exec(String(t || '')); return m ? Number(m[1]) : 99; }
/* stato di una consegna: CONSEGNATO (consegnato), RICONSEGNATO (restituito dal docente, oppure consegnato di nuovo dopo la restituzione: conta come consegnato), ASSEGNATO (ancora da consegnare, anche se la consegna e stata annullata) */
function CR_statoSub_(s) {
  if (s.state === 'RETURNED') return 'RICONSEGNATO';
  if (s.state === 'TURNED_IN') {
    var h = s.submissionHistory || [];
    for (var i = 0; i < h.length; i++) if (h[i] && h[i].stateHistory && h[i].stateHistory.state === 'RETURNED') return 'RICONSEGNATO';
    return 'CONSEGNATO';
  }
  return 'ASSEGNATO';
}
function CR_labScheda_(ss, classe, id, studenti, lavori, lab) {
  var re = new RegExp(lab.titolo, 'i'), i, j, tok, r;
  var cand = lavori.filter(function (w) { return re.test(String(w.title || '')); });
  var giorno = lab.giorno ? CR_giorno_(lab.giorno) : '';
  if (!giorno && cand.length) {
    cand.sort(function (a, b) { return String(b.creationTime) < String(a.creationTime) ? -1 : 1; });
    giorno = CR_giorno_(cand[0].title);
  }
  var comp = cand.filter(function (w) { return CR_giorno_(w.title) === giorno; });
  comp.sort(function (a, b) { return CR_oraN_(a.title) - CR_oraN_(b.title) || (String(a.creationTime) < String(b.creationTime) ? -1 : 1); });
  var stato = {};
  comp.forEach(function (w) {
    tok = null; stato[w.id] = {};
    do {
      r = Classroom.Courses.CourseWork.StudentSubmissions.list(id, w.id, { pageSize: 100, pageToken: tok || undefined });
      (r.studentSubmissions || []).forEach(function (s) { stato[w.id][s.userId] = CR_statoSub_(s); });
      tok = r.nextPageToken || null;
    } while (tok);
  });
  var T = comp.length, ord = { ROSSO: 0, ARANCIO: 1, GIALLO: 2, VERDE: 3, ND: 4 };
  var righe = studenti.map(function (s) {
    var cons = 0, ass = 0, celle = comp.map(function (w) {
      var x = stato[w.id][s.userId];
      if (!x) return '-';
      if (x === 'ASSEGNATO') ass++; else cons++;
      return x;
    });
    var st = T === 0 ? 'ND' : ass === 0 ? 'VERDE' : ass === 1 ? 'GIALLO' : ass <= 3 ? 'ARANCIO' : 'ROSSO';
    var em = (s.profile && s.profile.emailAddress) || '';
    return { st: st, nome: CR_nome_(s), em: em, celle: celle, cons: cons, tot: cons + ass, ass: ass };
  });
  righe.sort(function (a, b) { return ord[a.st] - ord[b.st] || (a.nome < b.nome ? -1 : a.nome > b.nome ? 1 : 0); });
  var ora = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  var testaT = comp.map(function (w) { return String(w.title || '').slice(0, 60); });
  var tuttiT = righe.filter(function (x) { return T > 0 && x.ass === 0 && x.tot === T; }).length;
  var almenoUno = righe.filter(function (x) { return x.cons > 0; }).length;
  var rie = T === 0
    ? "RIEPILOGO: nessun compito di Classroom con titolo «G/M Ora N: argomento» trovato in " + classe + " (compiti pubblicati, tipo Compito). " + righe.length + " allievi nel corso."
    : 'RIEPILOGO: ' + righe.length + ' allievi · compiti del ' + giorno + ': ' + T + ' · ' + tuttiT + ' hanno consegnato tutti i ' + T + ' · ' + almenoUno + ' ne hanno consegnato almeno uno · ' + (righe.length - almenoUno) + ' non ne hanno consegnato nessuno';
  var leg = 'CONSEGNATO = consegnato · RICONSEGNATO = restituito dal docente o consegnato di nuovo dopo la restituzione (conta come consegnato) · ASSEGNATO = ancora da consegnare (anche consegna annullata) · - = compito non assegnato a questo allievo. VERDE = tutto consegnato · GIALLO = ne manca 1 · ARANCIO = ne mancano 2-3 · ROSSO = 4 o piu · ND = nessun compito letto. Compiti letti (pubblicati): ' + (T ? comp.map(function (w) { return String(w.title || '').slice(0, 60); }).join(' | ') : 'nessuno') + '.';
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a', ND: '#e0e0e0' };
  function scrivi(nome, testa, dati, riga1, riga2, riga3) {
    var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
    sh.clear();
    sh.getRange(1, 1).setValue(riga1).setFontWeight('bold');
    sh.getRange(2, 1).setValue(riga2);
    sh.getRange(3, 1).setValue(riga3);
    sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
    if (dati.length) sh.getRange(5, 1, dati.length, testa.length).setValues(dati);
    for (var k = 0; k < dati.length; k++) sh.getRange(5 + k, 1).setBackground(col[dati[k][0]] || '#fff').setFontWeight('bold');
  }
  /* scheda docente: Stato, Allievo (COGNOME Nome), Email, un compito per colonna, conteggi, Quiz migliori */
  var testa = ['Stato', 'Allievo', 'Email'].concat(testaT, ['Consegnati', 'Totali', 'Mancanti', 'Quiz migliori']);
  var dati = righe.map(function (x) { return [x.st, x.nome, x.em].concat(x.celle, [x.cons, x.tot, x.ass, x.em ? CR_quiz_(ss, classe, x.em) : '-']); });
  scrivi('Consegne ' + classe, testa, dati, classe + ' · Consegne · dati letti alle ' + ora, leg, rie);
  /* scheda pubblica: solo «Nome I.», nessuna email (v2.19) */
  var lab2 = SM_brevi_(righe.map(function (x) { return x.nome; }));
  var testaP = ['Stato', 'Allievo'].concat(testaT, ['Consegnati', 'Totali', 'Mancanti']);
  var datiP = righe.map(function (x, k) { return [x.st, lab2[k]].concat(x.celle, [x.cons, x.tot, x.ass]); });
  scrivi('Consegne pubblica ' + classe, testaP, datiP, classe + ' · Consegne (pubblica, solo Nome I.) · dati letti alle ' + ora, leg, rie);
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
  try { AB_unisci_(ss, classe, el); } catch (e) { }
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

/* v2.20: versioni dello stesso quiz. Dal piu vecchio al piu recente; l'id attivo e sempre l'ultimo; solo id creati (in FB_FORMS) della stessa classe */
function VQ_ids_(l, id, forms, classe) {
  var out = [], vis = {};
  ((l && l.versioni) || []).forEach(function (v) {
    v = String(v || '').trim();
    if (!v || v === id || vis[v] || !forms[v]) return;
    if (classe && String(forms[v].classe || FB_classe_(null, v) || '').toUpperCase() !== classe) return;
    vis[v] = 1; out.push(v);
  });
  out.push(id);
  return out;
}
/* lavori che sono versioni vecchie di un altro lavoro: nessuna colonna loro */
function VQ_assorbiti_(indice) {
  var ass = {}, abs = {};
  (indice.lavori || []).forEach(function (l) {
    if (abs[l.id]) return;
    ass[l.id] = 1;
    ((l && l.versioni) || []).forEach(function (v) { if (v && v !== l.id && !ass[v]) abs[v] = 1; });
  });
  return abs;
}
function SM_quiz_(ss, indice, classe) {
  var forms = FB_json_('FB_FORMS'), es = ss.getSheetByName('Esiti').getDataRange().getValues(), out = [], i;
  var lavori = {}, assorbiti = VQ_assorbiti_(indice);
  (indice.lavori || []).forEach(function (l) { lavori[l.id] = l; });
  for (i = 1; i < es.length; i++) {
    var id = es[i][1], f = forms[id];
    if (!id || !f || !lavori[id] || assorbiti[id]) continue;
    if ((f.classe || FB_classe_(null, id)) !== classe) continue;
    if (FB_tl_(lavori[id], id) !== 'quiz') continue;
    var th = SM_testa_(f.titolo || es[i][2], id, String(es[i][0]).slice(0, 5));
    out.push({ id: id, riga: i, data: th.data, titolo: th.a, th: th, ver: VQ_ids_(lavori[id], id, forms, classe) });
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

/* v2.20: legge tutte le versioni di un quiz (ids dal piu vecchio al piu recente): per ogni email il risultato migliore, a parita il piu recente; vecchia = il migliore non e dell'ultima versione.
   disp = tutte le versioni elencate hanno la scheda Ris (altrimenti non si puo provare MANCA) */
function SM_leggiGruppo_(ss, ids) {
  var per = {}, ora = '', disp = true, n = ids.length;
  ids.forEach(function (id, k) {
    var L = SM_leggi_(ss, id);
    if (!L.disp) { disp = false; return; }
    if (/^\d/.test(L.ora) && (!ora || L.ora < ora)) ora = L.ora;
    else if (!ora) ora = L.ora;
    Object.keys(L.per).forEach(function (em) {
      var r = L.per[em], p = per[em];
      if (!p || r.pct >= p.pct) per[em] = { pct: r.pct, mg: r.mg, su: r.su, aperte: r.aperte, vecchia: k < n - 1 };
    });
  });
  return { disp: disp, ora: ora, per: per };
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
  return "GESTO (account PIAMARTA, un passo): apri il foglio Fabbrica, vai alla scheda 'Abbinamenti da confermare " + classe + "' e nella colonna Scelta scrivi OK (e' il candidato 1) oppure il numero del candidato giusto, oppure NO se l'email non e' di un allievo.";
}

/* ---------- v2.18: abbinamento email -> allievo in piu forme; schede 'Abbinamenti <CLASSE>' (confermati) e 'Abbinamenti da confermare <CLASSE>' ---------- */
function AB_part_(t) { return t.length === 1 || !!SM_PART_[String(t).toUpperCase()]; }
function AB_senzaPart_(tk) { var i = 0; while (i < tk.length - 1 && AB_part_(tk[i])) i++; return tk.slice(i); }
/* vero se a e b differiscono per una sola lettera (sostituita, tolta, aggiunta o scambiata con la vicina) */
function AB_dist1_(a, b) {
  if (a === b) return false;
  var la = a.length, lb = b.length, i = 0;
  if (Math.abs(la - lb) > 1) return false;
  while (i < la && i < lb && a.charAt(i) === b.charAt(i)) i++;
  if (la === lb) return a.slice(i + 1) === b.slice(i + 1) || (a.charAt(i) === b.charAt(i + 1) && a.charAt(i + 1) === b.charAt(i) && a.slice(i + 2) === b.slice(i + 2));
  if (la > lb) return a.slice(i + 1) === b.slice(i);
  return b.slice(i + 1) === a.slice(i);
}
/* nome dell'elenco (COGNOME Nome, anche tutto maiuscolo) -> tabella delle forme di email con il punteggio (100 nome e cognome interi, 92 senza particella o con il primo nome, 85 con iniziale) */
function AB_prep_(nome, orig) {
  var tk = SM_tok_(nome), p = SM_parti_(orig || nome, 0), cog = SM_tok_(p.cog), nom = SM_tok_(p.nome), i;
  if (tk.length < 2) return null;
  if (!cog.length || !nom.length) { cog = [tk[0]]; nom = tk.slice(1); }
  var f = {}, c = cog.join(''), n = nom.join(''), cp = AB_senzaPart_(cog).join(''), n1 = nom[0], ni = n1.charAt(0), ci = c.charAt(0);
  function add(x, v) { if (x && (!f[x] || f[x] < v)) f[x] = v; }
  for (i = 1; i < tk.length; i++) { var a = tk.slice(0, i).join(''), b = tk.slice(i).join(''); add(a + b, 100); add(b + a, 100); }
  add(c + n, 100); add(n + c, 100);
  if (cp.length >= 3 && cp !== c) { add(cp + n, 92); add(n + cp, 92); }
  if (n1.length >= 3 && n1 !== n) { add(c + n1, 92); add(n1 + c, 92); if (cp.length >= 3) { add(cp + n1, 92); add(n1 + cp, 92); } }
  if (c.length >= 3) { add(ni + c, 85); add(c + ni, 85); }
  if (cp.length >= 3) { add(ni + cp, 85); add(cp + ni, 85); }
  if (n1.length >= 3) { add(ci + n1, 85); add(n1 + ci, 85); add(ci + n, 85); add(n + ci, 85); }
  return { n: nome, f: f, c: c, cp: cp, n1: n1 };
}
function AB_punti_(j, P) {
  var s = P.f[j] || 0, k;
  if (s) return s;
  if (j.length >= 8) for (k in P.f) if (P.f[k] === 100 && k.length >= 8 && AB_dist1_(k, j)) return 75;
  if (P.cp.length >= 4 && (j === P.c || j === P.cp)) return 60;
  if (P.cp.length >= 4 && j.length > P.cp.length && (j.indexOf(P.cp) === 0 || j.lastIndexOf(P.cp) === j.length - P.cp.length)) return 55;
  if (P.n1.length >= 4 && j === P.n1) return 45;
  if (P.n1.length >= 4 && j.indexOf(P.n1) === 0) return 40;
  return 0;
}
function AB_forma_(s) {
  return s >= 100 ? 'nome e cognome' : s >= 92 ? 'nome e cognome (senza particella o con il primo nome)' : s >= 85 ? 'iniziale e cognome' : s >= 75 ? 'quasi uguale (una lettera diversa)' : s >= 55 ? 'solo il cognome' : 'solo il nome';
}
/* candidati per una email: [{n, s}] con punteggio 40 o piu, dal migliore */
function AB_cand_(em, pool) {
  var loc = String(em || '').split('@')[0].split('+')[0], j = SM_tok_(loc).join(''), out = [];
  if (!j) return out;
  pool.forEach(function (P) { var s = AB_punti_(j, P); if (s >= 40) out.push({ n: P.n, s: s }); });
  out.sort(function (a, b) { return b.s - a.s || (a.n < b.n ? -1 : a.n > b.n ? 1 : 0); });
  return out;
}
function AB_riga_(v) { for (var i = v.length - 1; i >= 0; i--) if (String(v[i][0] || '').trim() !== '') return i + 1; return 0; }
/* scheda 'Abbinamenti <CLASSE>': Email, Allievo, Fonte, Aggiornato, Nota. Ritorna { map: email -> NOME (o '-'), fonte: email -> fonte } */
function AB_salvati_(ss, classe) {
  var sh = ss.getSheetByName('Abbinamenti ' + classe), map = {}, fonte = {};
  if (!sh) return { map: map, fonte: fonte, esiste: false };
  var v = sh.getDataRange().getValues();
  for (var i = 0; i < v.length; i++) {
    var em = String(v[i][0] || '').trim().toLowerCase();
    if (em.indexOf('@') < 1 || map[em] !== undefined) continue;
    var n = String(v[i][1] || '').trim();
    map[em] = n === '-' ? '-' : SI_norm_(n);
    fonte[em] = String(v[i][2] || '').trim().toLowerCase();
  }
  return { map: map, fonte: fonte, esiste: true };
}
/* Sicurezza: unisce gli abbinamenti salvati a quelli dell'elenco (solo per nomi che ci sono) */
function AB_unisci_(ss, classe, el) {
  var sv = AB_salvati_(ss, classe), ok = {};
  el.nomi.forEach(function (n) { ok[n] = 1; });
  Object.keys(sv.map).forEach(function (em) { if (!el.e2n[em] && sv.map[em] !== '-' && ok[sv.map[em]]) el.e2n[em] = sv.map[em]; });
}
function AB_aggiungi_(ss, classe, righe) {
  if (!righe.length) return;
  var sh = ss.getSheetByName('Abbinamenti ' + classe) || ss.insertSheet('Abbinamenti ' + classe), v = sh.getDataRange().getValues(), n = AB_riga_(v);
  if (!n) { sh.getRange(1, 1, 1, 5).setValues([['Email', 'Allievo', 'Fonte', 'Aggiornato', 'Nota']]).setFontWeight('bold').setBackground('#e8eef9'); n = 1; }
  sh.getRange(n + 1, 1, righe.length, 5).setValues(righe);
}
/* ogni giro: applica le Scelte del docente, abbina in automatico i sicuri, riscrive i dubbi. e2n e modificata (email -> NOME o '-'). */
function AB_processa_(ss, classe, elenco, e2n, perEmail, orig) {
  var ok = {}, ora = FB_ora_('dd/MM HH:mm'), nuove = [], emails = Object.keys(perEmail).filter(function (e) { return e.indexOf('@') > 0; }).sort(), i;
  elenco.forEach(function (n) { ok[n] = 1; });
  var nomeDub = 'Abbinamenti da confermare ' + classe, shD = ss.getSheetByName(nomeDub), scelte = {}, esiti = {};
  var sv = AB_salvati_(ss, classe);
  /* 1) scelte del docente dal giro prima */
  if (shD) {
    var vd = shD.getDataRange().getValues();
    for (i = 4; i < vd.length; i++) {
      var em = String(vd[i][0] || '').trim().toLowerCase(), sc = String(vd[i][5] || '').trim();
      if (em.indexOf('@') < 1 || !sc) continue;
      var u = SI_norm_(sc), nome = null;
      if (u === 'OK') nome = SI_norm_(String(vd[i][1] || '').split(' · ')[0]);
      else if (/^[123]$/.test(u)) nome = SI_norm_(String(vd[i][Number(u)] || '').split(' · ')[0]);
      else if (u === 'NO') nome = '-';
      else if (ok[u]) nome = u;
      if (nome === '-' || (nome && ok[nome])) {
        if (sv.map[em] === undefined) { nuove.push([em, nome, 'docente', ora, 'scelta ' + sc]); sv.map[em] = nome; sv.fonte[em] = 'docente'; }
      } else esiti[em] = 'Scelta non valida (' + sc + '): scrivi OK, 1, 2, 3, NO oppure COGNOME Nome come nell\'elenco';
      if (nome && !esiti[em]) delete scelte[em]; else scelte[em] = sc;
    }
  }
  /* 2) abbinamenti salvati; 3) regola v2.15 */
  var pend = [], nAuto = 0;
  emails.forEach(function (e) {
    if (e2n[e] !== undefined) return;
    var s = sv.map[e];
    if (s === '-') { e2n[e] = '-'; return; }
    if (s && ok[s]) { e2n[e] = s; return; }
    var n = SM_abbina_(e, elenco);
    if (n) { e2n[e] = n; nuove.push([e, n, 'auto', ora, 'nome e cognome']); nAuto++; sv.map[e] = n; sv.fonte[e] = 'auto'; return; }
    pend.push(e);
  });
  /* 4) forme nuove, solo per i non ancora abbinati */
  var pool = [], occ = {}, dubbi = [];
  elenco.forEach(function (n) { var P = AB_prep_(n, orig[n]); if (P) pool.push(P); });
  Object.keys(e2n).forEach(function (e) { if (e2n[e] && e2n[e] !== '-') occ[e2n[e]] = 1; });
  var lista = pend.map(function (e) { var c = AB_cand_(e, pool); return { e: e, c: c, b: c.length ? c[0].s : 0 }; });
  lista.sort(function (a, b) { return b.b - a.b || (a.e < b.e ? -1 : 1); });
  lista.forEach(function (x) {
    var c = x.c, b = c[0], scuola = EL_DOMINI_.test(x.e);
    var sicuro = b && b.s >= 85 && (b.s === 100 || scuola) && (c.length < 2 || c[1].s <= b.s - 15) && (b.s === 100 || !occ[b.n]);
    if (sicuro) { e2n[x.e] = b.n; occ[b.n] = 1; nuove.push([x.e, b.n, 'auto', ora, AB_forma_(b.s)]); nAuto++; sv.map[x.e] = b.n; sv.fonte[x.e] = 'auto'; }
    else dubbi.push(x);
  });
  AB_aggiungi_(ss, classe, nuove);
  /* 5) scheda dei dubbi */
  if (dubbi.length || shD) {
    var sh = shD || ss.insertSheet(nomeDub);
    sh.clear();
    sh.getRange(1, 1).setValue(classe + ' · Abbinamenti da confermare (solo docente, con COGNOME Nome ed email, mai da pubblicare) · dati letti il ' + FB_ora_('dd/MM/yyyy HH:mm:ss')).setFontWeight('bold');
    sh.getRange(2, 1).setValue("Email che hanno risposto a un quiz della classe e non sono abbinate a un allievo. Nella colonna Scelta scrivi OK (= candidato 1), oppure 1, 2 o 3 (il candidato giusto), oppure NO (non e' un allievo), oppure COGNOME Nome come nell'elenco. Al giro dopo il motore applica la scelta e la copia nella scheda 'Abbinamenti " + classe + "'.");
    sh.getRange(4, 1, 1, 7).setValues([['Email', 'Candidato 1', 'Candidato 2', 'Candidato 3', 'Quiz con risposte', 'Scelta', 'Esito']]).setFontWeight('bold').setBackground('#e8eef9');
    var rr = dubbi.map(function (x) {
      var cc = [0, 1, 2].map(function (k) { var y = x.c[k]; return y ? y.n + ' · ' + AB_forma_(y.s) + (occ[y.n] ? " · ha gia' un'email" : '') : ''; });
      return [x.e, cc[0], cc[1], cc[2], perEmail[x.e].join(' · '), scelte[x.e] || '', esiti[x.e] || (x.c.length ? '' : 'nessun candidato: scrivi COGNOME Nome oppure NO')];
    });
    if (rr.length) sh.getRange(5, 1, rr.length, 7).setValues(rr);
    else sh.getRange(5, 1).setValue('Nessun abbinamento da confermare.');
  }
  var nAutoTot = 0, nDoc = 0;
  Object.keys(sv.map).forEach(function (e) { if (sv.map[e] === '-' || perEmail[e] === undefined) return; if (sv.fonte[e] === 'auto') nAutoTot++; else if (sv.fonte[e] === 'docente') nDoc++; });
  return { auto: nAutoTot, doc: nDoc, dubbi: dubbi.length, nuoviAuto: nAuto };
}

function SM_classe_(ss, indice, classe) {
  var quiz = SM_quiz_(ss, indice, classe), nome = 'Situazione ' + classe;
  var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  sh.clear();
  var ora0 = FB_ora_('dd/MM/yyyy HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Situazione quiz e voti (solo docente, con COGNOME Nome) · dati letti il ' + ora0).setFontWeight('bold');
  if (!quiz.length) { sh.getRange(2, 1).setValue('Nessun quiz della classe ' + classe + ' in indice.json.'); return; }
  var el = SI_elenco_(ss, classe), nonAbb = [], nonAbbEm = {}, dichiara = '', fonteTxt = '', usaUtenti = false;
  var lett = quiz.map(function (q) { return SM_leggiGruppo_(ss, q.ver); });
  var elenco = el.nomi.slice(), e2n = {}, k0;
  for (k0 in el.e2n) e2n[k0] = el.e2n[k0];
  var orig = {}, shU0 = ss.getSheetByName('Utenti ' + classe);
  if (shU0) shU0.getDataRange().getValues().forEach(function (r) { var o = String(r[2] || '').trim(); if (o) orig[SI_norm_(o)] = o; });
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
  /* v2.18: abbinamento delle email con risposte (scheda Email/Elenco, abbinamenti salvati, regola v2.15, forme nuove) */
  var abbN = 0, senzaEmail = [], ab = { auto: 0, doc: 0, dubbi: 0 };
  if (!dichiara) {
    var perEmail = {};
    lett.forEach(function (L, k) { Object.keys(L.per).forEach(function (em) { (perEmail[em] = perEmail[em] || []).push(quiz[k].titolo); }); });
    ab = AB_processa_(ss, classe, elenco, e2n, perEmail, orig);
    var trov = {};
    Object.keys(e2n).forEach(function (em) { if (e2n[em] && e2n[em] !== '-') trov[e2n[em]] = 1; });
    elenco.forEach(function (n) { if (trov[n]) abbN++; else senzaEmail.push(n); });
  }
  var hasEm = {};
  Object.keys(e2n).forEach(function (em) { if (e2n[em] && e2n[em] !== '-') hasEm[e2n[em]] = 1; });
  var celle = {}, disp = lett.map(function (L) { return L.disp; }), uk = quiz.map(function () { return 0; });
  elenco.forEach(function (n) { celle[n] = quiz.map(function () { return null; }); });
  lett.forEach(function (L, k) {
    Object.keys(L.per).forEach(function (em) {
      var n = e2n[em], r = L.per[em];
      if (n === '-') return;
      if (!n) { nonAbb.push(em + ' · ' + quiz[k].titolo + ' · ' + r.pct + '%'); nonAbbEm[em] = 1; uk[k]++; return; }
      var c = celle[n][k];
      if (!c || r.pct > c.pct) celle[n][k] = r;
    });
  });
  var tot = disp.filter(function (d) { return d; }).length, nd = quiz.length - tot;
  var testa = ['Stato', 'Allievo'].concat(quiz.map(function (q) { return q.titolo; }), ['Fatti / totali', 'Media % dei fatti', 'NON HA FATTO', 'NON ABBINATA']);
  var righe = elenco.map(function (n) {
    var fatti = 0, somma = 0, manca = [], nab = [], txt = quiz.map(function (q, k) {
      var c = celle[n][k];
      if (c) { if (disp[k]) { fatti++; somma += c.pct; } return { t: c.pct + '% (' + c.mg + '/' + c.su + ')' + (c.aperte > 0 ? ' (provv.: ' + c.aperte + ' aperte da correggere)' : '') + (c.vecchia ? ' \u00b7 fatto sulla versione precedente' : ''), p: c.pct }; }
      if (disp[k]) {
        /* MANCA solo con la prova: email abbinata (e nessuna risposta) oppure nessuna risposta del quiz resta da abbinare */
        if (hasEm[n] || !uk[k]) { manca.push(q.titolo + ' (' + q.data + ')'); return { t: 'MANCA', p: -1 }; }
        nab.push(q.titolo + ' (' + q.data + ')'); return { t: 'NON ABBINATA', p: -3 };
      }
      return { t: 'dato non letto', p: -2 };
    });
    var st = !tot ? 'ND' : manca.length ? 'ROSSO' : nab.length ? 'ND' : 'VERDE';
    return { st: st, n: n, txt: txt, riga: [st, n].concat(txt.map(function (x) { return x.t; }), [fatti + '/' + tot, fatti ? Math.round(somma / fatti) + '%' : '-', manca.length ? manca.join(' · ') : '-', nab.length ? nab.join(' · ') : '-']), m: manca.length, na: nab.length };
  });
  righe.sort(function (a, b) { return b.m - a.m || b.na - a.na || (a.n < b.n ? -1 : a.n > b.n ? 1 : 0); });
  var tutto = righe.filter(function (r) { return tot && r.m === 0 && r.na === 0; }).length;
  var conM = righe.filter(function (r) { return r.m > 0; }).length, conNA = righe.filter(function (r) { return r.na > 0; }).length;
  sh.getRange(2, 1).setValue('Cella = miglior punteggio in % (punti/totale) di tutti i tentativi. MANCA = nessuna risposta, con la prova: l’allievo ha una email abbinata e non ha risposto, oppure per quel quiz non resta nessuna risposta da abbinare. NON ABBINATA = per quel quiz ci sono risposte arrivate ma da abbinare a un allievo: non si sa se questo allievo ha risposto (non e MANCA e non e fatto). Verde = 80% o più, giallo = sotto 80%, rosso = MANCA, ambra = NON ABBINATA. Stato ND = ci sono celle NON ABBINATA e nessun MANCA. (provv.) = ci sono domande aperte non ancora corrette: la percentuale può cambiare. Media = solo sui quiz fatti. Quiz = Moduli di indice.json con TIPOLOGIA LEZIONE Quiz su Moduli (le schede di teoria non sono contate). Se un quiz e stato rigenerato (campo versioni di indice.json) le versioni contano come UN quiz: vale il risultato migliore, a parita il piu recente, con la nota «fatto sulla versione precedente» se non e dell\u2019ultima.');
  sh.getRange(3, 1).setValue('RIEPILOGO: ' + righe.length + ' allievi · ' + tutto + ' hanno fatto tutti i ' + tot + ' quiz letti · ' + (righe.length - tutto) + ' ne hanno almeno uno non fatto (MANCA provato: ' + conM + ' · NON ABBINATA, risposte da abbinare: ' + conNA + ')' + (nd ? ' · ' + nd + ' quiz non ancora letti (scheda Ris assente), non contati' : ''));
  var abbTxt = '', nE = Object.keys(nonAbbEm).length;
  if (usaUtenti) abbTxt = ' · Abbinamento email (nome e cognome in piu forme): ' + abbN + ' allievi abbinati, ' + senzaEmail.length + ' senza email abbinata' + (senzaEmail.length ? ' (per questi MANCA vale solo se per il quiz non resta nessuna risposta da abbinare, altrimenti NON ABBINATA)' : '');
  if (ab.auto || ab.doc) abbTxt += ' · ' + ab.auto + ' email abbinate in automatico e ' + ab.doc + " confermate dal docente (scheda 'Abbinamenti " + classe + "')";
  if (nonAbb.length) abbTxt += ' · ' + nonAbb.length + ' risposte con email non abbinata (' + nE + " email, elenco in fondo e nella scheda 'Abbinamenti da confermare " + classe + "') · ATTENZIONE: " + SM_gesto_(classe, 'abb');
  var verTxt = quiz.filter(function (q) { return q.ver.length > 1; }).map(function (q) { return q.id + ' = ' + q.ver.join(' + '); }).join(' ; ');
  if (verTxt) abbTxt += ' · Versioni dello stesso quiz contate come uno (migliore risultato): ' + verTxt;
  sh.getRange(4, 1).setValue('Elenco allievi da ' + (el.nomi.length ? el.fonte : fonteTxt || 'schede Ris (vedi avviso)') + abbTxt + (dichiara ? ' · ATTENZIONE: ' + dichiara : ''));
  var lr = ['Letto alle', ''].concat(lett.map(function (L) { return L.disp ? L.ora : 'non letto'; }), ['', '', '', '']);
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
      sh.getRange(7 + i, 3 + k).setBackground(x.p === -3 ? '#ffe082' : x.p < 0 ? '#ef9a9a' : x.p >= 80 ? '#a5d6a7' : '#fff59d');
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
    /* v2.21: con due o piu parole dopo il cognome presunto non si sa dove finisce il cognome (doppio cognome): si tiene come nome solo l'ultima parola */
    if (p.length - nc >= 2) nc = p.length - 1;
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
  var rg = src.getDataRange(), vals = SM_pubValori_(rg.getValues()), nc = 1, i;
  vals.forEach(function (r) { if (r.length > nc) nc = r.length; });
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
  var forms = FB_json_('FB_FORMS'), vis = {}, em = [], ut = SM_utenti_(ss, classe), orig = {}, sv = AB_salvati_(ss, classe).map;
  var shU = ss.getSheetByName('Utenti ' + classe);
  if (shU) shU.getDataRange().getValues().forEach(function (r) { var o = String(r[2] || '').trim(); if (o) orig[SI_norm_(o)] = o; });
  (indice.lavori || []).forEach(function (l) {
    var cl = String((forms[l.id] && forms[l.id].classe) || FB_classe_(l, l.id) || '').toUpperCase();
    if (cl !== classe) return;
    VQ_ids_(l, l.id, forms, classe).forEach(function (vid) {
      var sh = ss.getSheetByName('Ris ' + vid);
      if (!sh) return;
      var v = sh.getDataRange().getValues();
      for (var i = 4; i < v.length; i++) {
        var e = String(v[i][0] || '').trim().toLowerCase();
        if (e.indexOf('@') > 0 && !vis[e]) { vis[e] = 1; em.push(e); }
      }
    });
  });
  return em.map(function (e) {
    var n = (sv[e] && sv[e] !== '-' ? sv[e] : null) || (ut.nomi.length ? SM_abbina_(e, ut.nomi) : null);
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
  if (/^Consegne pubblica /.test(nome)) return { g: 5, tipo: 'Consegne', classe: c, k: '2' + c + 'z' };
  if (/^Consegne /.test(nome)) return { g: 5, tipo: 'Consegne', classe: c, k: '2' + c };
  if (/^(Cruscotto )?Git /.test(nome)) return { g: 5, tipo: 'Git', classe: c, k: '3' + c };
  if (/^Abbinamenti da confermare /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c + 'zy' };
  if (/^Abbinamenti /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c + 'zx' };
  if (/^Email /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c };
  if (/^Elenco /.test(nome)) return { g: 5, tipo: 'Utenti', classe: c, k: '4' + c + 'z' };
  if (nome === 'Corsi') return { g: 5, tipo: 'Consegne', classe: '', k: '5' };
  if (/^Documenti pubblica /.test(nome)) return { g: 5, tipo: 'Consegne', classe: c, k: '2' + c + 'zz' };
  if (/^Documenti /.test(nome)) return { g: 5, tipo: 'Consegne', classe: c, k: '2' + c + 'y' };
  if (m = /^Risposte (.+)$/.exec(nome)) {
    var id2 = m[1], cl2 = (forms[id2] && forms[id2].classe) || FB_classe_(null, id2) || '';
    return { g: 7, tipo: 'Risposte quiz', classe: String(cl2).toUpperCase(), k: id2 + '~', id: id2 };
  }
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

/* ---------- v2.22: schede 'Risposte <id quiz>' (risposte per domanda, solo docente) ---------- */
var RS_NC_ = {};
/* email (minuscola) -> 'COGNOME Nome' dalle schede Elenco e Abbinamenti della classe (i confermati valgono piu dell'elenco) */
function RS_nomi_(ss, classe) {
  if (RS_NC_[classe]) return RS_NC_[classe];
  var out = {};
  ['Elenco ', 'Abbinamenti '].forEach(function (p) {
    var sh = ss.getSheetByName(p + classe);
    if (!sh) return;
    var v = sh.getDataRange().getValues();
    for (var i = 1; i < v.length; i++) {
      var em = String(v[i][0] || '').trim().toLowerCase(), n = String(v[i][1] || '').trim();
      if (em.indexOf('@') > 0 && n && n !== '-') out[em] = n;
    }
  });
  RS_NC_[classe] = out;
  return out;
}
/* le domande del Modulo in ordine: { id, testo, max, aperta } (niente intestazioni di sezione, immagini, video, interruzioni di pagina) */
function RS_domande_(form) {
  var out = [], T = FormApp.ItemType;
  var skip = [T.PAGE_BREAK, T.SECTION_HEADER, T.IMAGE, T.VIDEO];
  form.getItems().forEach(function (it) {
    var t = it.getType(), x = null, mx = 0;
    if (skip.indexOf(t) >= 0) return;
    try {
      if (t === T.CHECKBOX) x = it.asCheckboxItem();
      else if (t === T.MULTIPLE_CHOICE) x = it.asMultipleChoiceItem();
      else if (t === T.LIST) x = it.asListItem();
      else if (t === T.TEXT) x = it.asTextItem();
      else if (t === T.PARAGRAPH_TEXT) x = it.asParagraphTextItem();
      if (x && x.getPoints) mx = Number(x.getPoints()) || 0;
    } catch (e) { mx = 0; }
    out.push({ id: it.getId(), testo: String(it.getTitle() || ''), max: mx, aperta: t === T.TEXT || t === T.PARAGRAPH_TEXT });
  });
  return out;
}
function RS_txt_(x) {
  if (x === null || x === undefined) return '';
  if (Object.prototype.toString.call(x) === '[object Array]') return x.map(RS_txt_).filter(function (s) { return s !== ''; }).join(' | ');
  return String(x);
}
/* una cella di testo: mai una formula (la risposta di un allievo potrebbe cominciare con = + - @), al massimo 1500 caratteri */
function RS_cella_(s) {
  s = String(s);
  if (s.length > 1500) s = s.slice(0, 1500) + '…';
  return /^[=+\-@]/.test(s) ? ' ' + s : s;
}
function RS_risposte_(ss, id, form, f, ris, su) {
  var nome = 'Risposte ' + id, classe = String((f && f.classe) || FB_classe_(null, id) || '').toUpperCase();
  var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  sh.clear();
  var dom = RS_domande_(form), nomi = RS_nomi_(ss, classe), nd = dom.length, byId = {}, righe = [], per = {}, conta = {}, i;
  dom.forEach(function (d, k) { byId[d.id] = k; });
  var lista = ris.slice().sort(function (a, b) { return a.getTimestamp() - b.getTimestamp(); });
  lista.forEach(function (r) {
    var em = r.getRespondentEmail() || '(senza email)', key = em.toLowerCase(), s = 0;
    (r.getGradableItemResponses() || []).forEach(function (g) { s += Number(g.getScore()) || 0; });
    conta[key] = (conta[key] || 0) + 1;
    var ans = [], pts = [], dc = [];
    for (i = 0; i < nd; i++) { ans.push(''); pts.push(''); dc.push(false); }
    (r.getItemResponses() || []).forEach(function (ir) {
      var k = byId[ir.getItem().getId()];
      if (k === undefined) return;
      var testo = RS_txt_(ir.getResponse()), sc = ir.getScore ? ir.getScore() : null;
      ans[k] = RS_cella_(testo);
      if (dom[k].aperta && dom[k].max > 0 && testo.replace(/\s+/g, '') !== '' && (sc === null || sc === undefined || Number(sc) === 0)) { pts[k] = 'da correggere'; dc[k] = true; }
      else pts[k] = (sc === null || sc === undefined) ? '' : Number(sc);
    });
    for (i = 0; i < nd; i++) if (pts[i] === '' && dom[i].max > 0 && ans[i] === '') pts[i] = 0;   /* nessuna risposta a una domanda con punti = 0 punti */
    var riga = { ts: r.getTimestamp(), em: em, key: key, tent: conta[key], s: s, ans: ans, pts: pts, dc: dc };
    righe.push(riga);
    var p = per[key];
    if (!p || s > p.s || (s === p.s && riga.ts >= p.ts)) per[key] = riga;
  });
  var nome2 = function (em) { return nomi[String(em).toLowerCase()] || '(non abbinato)'; };
  var testa = ['Ora invio', 'Allievo', 'Email', 'Tentativo', 'Punteggio', 'Su', 'Migliore'], r3 = ['Domanda →', '', '', '', '', '', ''];
  dom.forEach(function (d, k) { testa.push('D' + (k + 1)); r3.push(d.testo + (d.max ? ' (' + d.max + ' pt)' : '')); });
  dom.forEach(function (d, k) { testa.push('P' + (k + 1)); r3.push(d.max ? 'max ' + d.max : 'senza punti'); });
  var col = testa.length;
  var dati = righe.map(function (x) {
    var mig = per[x.key] === x ? 'Sì' : '';
    return [Utilities.formatDate(x.ts, 'Europe/Rome', 'dd/MM HH:mm:ss'), nome2(x.em), x.em, x.tent, x.s, su, mig].concat(x.ans, x.pts);
  });
  dati.sort(function (a, b) { return a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : a[3] - b[3]; });
  sh.getRange(1, 1).setValue('Risposte per domanda · ' + (form.getTitle() || (f && f.titolo) || id)).setFontWeight('bold');
  sh.getRange(2, 1).setValue('Classe ' + classe + ' · id ' + id + ' · dati letti il ' + FB_ora_('dd/MM/yyyy HH:mm:ss') + ' · ' + ris.length + ' risposte · SOLO DOCENTE (cognomi, email e testo delle risposte)');
  sh.getRange(3, 1, 1, col).setValues([r3]).setWrap(true).setFontStyle('italic');
  sh.getRange(4, 1, 1, col).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (dati.length) sh.getRange(5, 1, dati.length, col).setValues(dati);
  /* errori ricorrenti: tentativo migliore di ogni allievo; sbagliata = punteggio sotto il massimo; da correggere = aperta con risposta e punteggio 0 o vuoto */
  var best = Object.keys(per).map(function (k) { return per[k]; }), sum = [];
  dom.forEach(function (d, k) {
    if (!(d.max > 0)) return;
    var sb = 0, dc = 0, ok = 0;
    best.forEach(function (b) {
      if (b.dc[k]) dc++;
      else if (typeof b.pts[k] === 'number' && b.pts[k] >= d.max) ok++;
      else sb++;
    });
    sum.push([k, sb, dc, ok]);
  });
  sum.sort(function (a, b) { return b[1] - a[1] || a[0] - b[0]; });
  var r0 = 5 + dati.length + 2;
  sh.getRange(r0, 1).setValue('ERRORI RICORRENTI (tentativo migliore di ogni allievo, ' + best.length + ' allievi; sbagliata = sotto il punteggio massimo; chi non ha risposto conta sbagliata)').setFontWeight('bold');
  sh.getRange(r0 + 1, 1, 1, 6).setValues([['Domanda', 'Testo', 'Sbagliata da', 'Da correggere', 'Giusta da', 'Punti max']]).setFontWeight('bold').setBackground('#e8eef9');
  if (sum.length) sh.getRange(r0 + 2, 1, sum.length, 6).setValues(sum.map(function (s) { return ['D' + (s[0] + 1), RS_cella_(dom[s[0]].testo.slice(0, 200)), s[1], s[2], s[3], dom[s[0]].max]; }));
  sh.setFrozenRows(4);
  sh.setFrozenColumns(3);
  return ris.length;
}

/* ---------- v2.22: schede 'Documenti <CLASSE>' (docente) e 'Documenti pubblica <CLASSE>' (solo Nome I.) ----------
   Per ogni allievo e per ogni compito di Classroom di tipo Documento (assegnazione con un file Drive «una copia per ogni allievo», oppure titolo «G/M Ora N: ...»):
   stato, ora di consegna, file allegato (titolo, id, link), ultima modifica del file, immagini, caratteri, estratto del testo.
   Permessi: nessuno nuovo rispetto al lancio (Classroom: le stesse chiamate di 'Consegne'; Drive: DriveApp e il token del progetto per esportare il Documento in HTML). */
var DC_RE_ORA_ = /^\s*\d{1,2}\s*\/\s*\d{1,2}\s+Ora\s*\d/i;
function DC_cfg_(indice, classe) {
  var c = (indice && indice.classroom) || {}, d = c.documenti;
  if (d === false || (d && d.attivo === false)) return null;
  d = d && typeof d === 'object' ? d : {};
  if (d.classi && d.classi.indexOf(classe) < 0) return null;
  return { ultimi: Number(d.ultimi) || 6, ogni: Number(d.ogni_minuti) || 5, titolo: d.titolo || '', max_letture: Number(d.max_letture) || 24 };
}
function DC_isDoc_(w, cfg) {
  if (w.workType !== 'ASSIGNMENT') return false;
  if (cfg.titolo && new RegExp(cfg.titolo, 'i').test(String(w.title || ''))) return true;
  if (DC_RE_ORA_.test(String(w.title || ''))) return true;
  return (w.materials || []).some(function (m) { return m.driveFile && m.driveFile.shareMode === 'STUDENT_COPY'; });
}
/* il file Drive del modello (la copia per ogni allievo), se c'e */
function DC_modello_(w) {
  var ms = w.materials || [];
  for (var i = 0; i < ms.length; i++) {
    var d = ms[i].driveFile;
    if (d && d.shareMode === 'STUDENT_COPY' && d.driveFile && d.driveFile.id) return d.driveFile.id;
  }
  return '';
}
function DC_stato_(s) {
  if (s.state === 'RETURNED') return 'RESTITUITO';
  if (s.state === 'TURNED_IN') return s.late ? 'IN RITARDO' : 'CONSEGNATO';
  return 'ASSEGNATO';
}
function DC_oraCons_(s) {
  if (s.state !== 'TURNED_IN' && s.state !== 'RETURNED') return '';
  var h = s.submissionHistory || [], t = '', i;
  for (i = 0; i < h.length; i++) if (h[i] && h[i].stateHistory && h[i].stateHistory.state === 'TURNED_IN' && h[i].stateHistory.stateTimestamp) t = h[i].stateHistory.stateTimestamp;
  if (!t) t = s.updateTime || '';
  if (!t) return '';
  var d = new Date(t);
  return isNaN(d.getTime()) ? '' : Utilities.formatDate(d, 'Europe/Rome', 'dd/MM HH:mm');
}
function DC_testo_(h) {
  return String(h || '').replace(/<head[\s\S]*?<\/head>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ').replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<\/(p|div|h[1-6]|li|tr)>|<br\s*\/?>/gi, ' ').replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&')
    .replace(/&#(\d+);/g, function (m, n) { return String.fromCharCode(Number(n)); }).replace(/\s+/g, ' ').trim();
}
function DC_imm_(h) { return (String(h || '').match(/<img\b/gi) || []).length; }
/* metadati di un file con DriveApp (titolo, tipo, ultima modifica con i secondi) */
function DC_meta_(id) {
  try {
    var f = DriveApp.getFileById(id);
    return { ok: true, nome: f.getName(), mime: f.getMimeType(), mod: Utilities.formatDate(f.getLastUpdated(), 'Europe/Rome', 'yyyy-MM-dd HH:mm:ss') };
  } catch (e) { return { ok: false, err: String(e && e.message ? e.message : e).slice(0, 120) }; }
}
/* legge i file indicati (id -> info), riusando la cache se l'ultima modifica non e cambiata; al massimo `max` esportazioni per giro e solo prima di `tmax` (ms) */
function DC_leggi_(ids, cache, max, tmax) {
  var out = {}, daLeggere = [], DOC = 'application/vnd.google-apps.document', i;
  ids.forEach(function (id) {
    var m = DC_meta_(id), c = cache[id];
    if (!m.ok) { out[id] = { err: 'file non apribile: ' + m.err, tent: ((c && c.tent) || 0) + 1, img: 'n.d.', car: 'n.d.', estr: '', mod: '', nome: '', mime: '' }; return; }
    var info = { nome: m.nome, mime: m.mime, mod: m.mod, img: 'n.d.', car: 'n.d.', estr: '', err: '', tent: 0 };
    if (m.mime.indexOf('image/') === 0) { info.img = 1; info.car = 0; info.estr = '(file immagine)'; out[id] = info; return; }
    if (m.mime !== DOC) { info.estr = '(non e un Documento Google: contenuto non letto)'; out[id] = info; return; }
    if (c && c.mod === m.mod && !c.err) { info.img = c.img; info.car = c.car; info.estr = c.estr; out[id] = info; return; }
    if (c && c.mod === m.mod && c.err && (c.tent || 0) >= 3) { info.err = c.err; info.tent = c.tent; out[id] = info; return; }
    info.tent = (c && c.mod === m.mod) ? (c.tent || 0) : 0;
    info.err = 'in attesa di lettura';
    out[id] = info; daLeggere.push(id);
  });
  daLeggere = daLeggere.slice(0, max);
  var tok = ScriptApp.getOAuthToken(), k;
  for (k = 0; k < daLeggere.length; k += 10) {
    if (Date.now() > tmax) break;
    var blocco = daLeggere.slice(k, k + 10);
    var reqs = blocco.map(function (id) { return { url: 'https://docs.google.com/document/d/' + id + '/export?format=html', headers: { Authorization: 'Bearer ' + tok }, muteHttpExceptions: true, followRedirects: true }; });
    var rs;
    try { rs = UrlFetchApp.fetchAll(reqs); } catch (e) { rs = blocco.map(function () { return null; }); }
    blocco.forEach(function (id, n) {
      var r = rs[n], info = out[id];
      if (r && r.getResponseCode() !== 200) {   /* seconda strada: esportazione con l'API di Drive */
        try { r = UrlFetchApp.fetch('https://www.googleapis.com/drive/v3/files/' + id + '/export?mimeType=text%2Fhtml', { headers: { Authorization: 'Bearer ' + tok }, muteHttpExceptions: true }); } catch (e3) { }
      }
      if (!r || r.getResponseCode() !== 200) { info.err = 'esportazione del Documento non riuscita (' + (r ? 'HTTP ' + r.getResponseCode() : 'nessuna risposta') + ')'; info.tent++; return; }
      var h = r.getContentText(), t = DC_testo_(h);
      info.img = DC_imm_(h); info.car = t.length; info.estr = t.slice(0, 300); info.err = '';
    });
  }
  return out;
}
function DC_cella_(s) { s = String(s === null || s === undefined ? '' : s); return /^[=+\-@]/.test(s) ? ' ' + s : s; }
function DC_scheda_(ss, classe, corsoId, cfg, t0) {
  var i, tok, r, studenti = [], lavori = [];
  tok = null;
  do {
    r = Classroom.Courses.Students.list(corsoId, { pageSize: 100, pageToken: tok || undefined });
    studenti = studenti.concat(r.students || []); tok = r.nextPageToken || null;
  } while (tok);
  tok = null;
  do {
    r = Classroom.Courses.CourseWork.list(corsoId, { courseWorkStates: ['PUBLISHED'], pageSize: 100, pageToken: tok || undefined });
    lavori = lavori.concat(r.courseWork || []); tok = r.nextPageToken || null;
  } while (tok);
  lavori = lavori.filter(function (w) { return DC_isDoc_(w, cfg); });
  lavori.sort(function (a, b) { return String(b.creationTime) < String(a.creationTime) ? -1 : 1; });
  lavori = lavori.slice(0, cfg.ultimi);
  lavori.sort(function (a, b) { return String(a.creationTime) < String(b.creationTime) ? -1 : 1; });
  var sub = {};   /* workId -> userId -> submission */
  lavori.forEach(function (w) {
    sub[w.id] = {}; tok = null;
    do {
      r = Classroom.Courses.CourseWork.StudentSubmissions.list(corsoId, w.id, { pageSize: 100, pageToken: tok || undefined });
      (r.studentSubmissions || []).forEach(function (s) { sub[w.id][s.userId] = s; });
      tok = r.nextPageToken || null;
    } while (tok);
  });
  /* cache: la scheda di prima (id file -> ultima modifica, immagini, caratteri, estratto) */
  var nomeSh = 'Documenti ' + classe, cache = {}, vecchia = ss.getSheetByName(nomeSh);
  if (vecchia) {
    var vv = vecchia.getDataRange().getValues();
    for (i = 4; i < vv.length; i++) {
      var fid = String(vv[i][7] || '');
      if (fid && !cache[fid]) cache[fid] = { mod: String(vv[i][10] || ''), img: vv[i][11], car: vv[i][14], estr: String(vv[i][15] || ''), err: String(vv[i][17] || ''), tent: Number(vv[i][18]) || 0 };
    }
  }
  /* i modelli non stanno nella scheda: la loro ultima modifica e le immagini si tengono nelle proprieta dello script (al massimo 40) */
  var pm = FB_json_('FB_DOC_MOD'), ids = [], visti = {}, modelli = {};
  Object.keys(pm).forEach(function (k) { if (!cache[k]) cache[k] = { mod: pm[k].mod, img: pm[k].img, car: 0, estr: '', err: '', tent: 0 }; });
  lavori.forEach(function (w) {
    var m = DC_modello_(w); if (m) { modelli[w.id] = m; if (!visti[m]) { visti[m] = 1; ids.push(m); } }
    studenti.forEach(function (s) {
      var x = sub[w.id][s.userId], at = (x && x.assignmentSubmission && x.assignmentSubmission.attachments) || [];
      at.forEach(function (a) { if (a.driveFile && a.driveFile.id && !visti[a.driveFile.id]) { visti[a.driveFile.id] = 1; ids.push(a.driveFile.id); } });
    });
  });
  var info = DC_leggi_(ids, cache, cfg.max_letture, t0 + 240000);
  var pm2 = {}, nm = 0;
  Object.keys(modelli).forEach(function (w) { var m = modelli[w], x = info[m]; if (x && !x.err && typeof x.img === 'number') pm2[m] = { mod: x.mod, img: x.img }; });
  Object.keys(pm).forEach(function (k) { if (!pm2[k] && Object.keys(pm2).length + nm < 40) { pm2[k] = pm[k]; nm++; } });
  FB_salva_('FB_DOC_MOD', pm2);
  var adesso = FB_ora_('dd/MM/yyyy HH:mm:ss'), righe = [], consegnati = 0, letti = 0, nonLetti = 0;
  var stOrd = studenti.map(function (s) { return { s: s, nome: CR_nome_(s), em: (s.profile && s.profile.emailAddress) || '' }; });
  stOrd.sort(function (a, b) { return a.nome < b.nome ? -1 : a.nome > b.nome ? 1 : 0; });
  stOrd.forEach(function (st) {
    lavori.forEach(function (w) {
      var x = sub[w.id][st.s.userId];
      if (!x) return;   /* compito non assegnato a questo allievo */
      var stato = DC_stato_(x), ora = DC_oraCons_(x), at = ((x.assignmentSubmission && x.assignmentSubmission.attachments) || []).filter(function (a) { return a.driveFile && a.driveFile.id; });
      if (stato !== 'ASSEGNATO') consegnati++;
      var mod = modelli[w.id] && info[modelli[w.id]], imM = mod && typeof mod.img === 'number' ? mod.img : 'n.d.';
      var base = [st.nome, st.em, String(w.title || ''), w.id, stato, ora];
      if (!at.length) { righe.push(base.concat(['', '', '', '', '', '', imM, 'n.d.', '', '', adesso, 'nessun file allegato', 0])); return; }
      at.forEach(function (a) {
        var d = info[a.driveFile.id] || { img: 'n.d.', car: 'n.d.', estr: '', err: 'file non letto in questo giro', tent: 0, nome: '', mime: '', mod: '' };
        var agg = (typeof d.img === 'number') ? ((typeof imM === 'number' && String(d.mime).indexOf('image/') !== 0) ? Math.max(0, d.img - imM) : d.img) : 'n.d.';
        if (d.err) nonLetti++; else letti++;
        righe.push(base.concat([String(a.driveFile.title || d.nome || ''), a.driveFile.id, String(a.driveFile.alternateLink || ''), d.mime || '', d.mod || '', d.img, imM, agg, d.car, DC_cella_(d.estr), adesso, d.err || '', d.tent || 0]));
      });
    });
  });
  var testa = ['Allievo', 'Email', 'Compito', 'Id compito', 'Stato', 'Ora consegna', 'File', 'File ID', 'Link', 'Tipo file', 'Ultima modifica file', 'Immagini totali', 'Immagini del modello', 'Immagini aggiunte', 'Caratteri', 'Estratto del testo', 'Letto alle', 'Errore di lettura', 'Tentativi'];
  var leg = 'Stato: ASSEGNATO = da consegnare (anche consegna annullata) · CONSEGNATO · IN RITARDO (consegnato dopo la scadenza di Classroom; se il compito non ha scadenza non compare) · RESTITUITO. Immagini aggiunte = immagini del Documento dell\'allievo meno quelle gia presenti nel modello; n.d. = non letto. Compiti letti: ' + (lavori.length ? lavori.map(function (w) { return String(w.title || '').slice(0, 60); }).join(' | ') : 'nessuno') + '.';
  var rie = 'RIEPILOGO: ' + studenti.length + ' allievi · ' + lavori.length + ' compiti di tipo Documento (gli ultimi ' + cfg.ultimi + ') · consegne ' + consegnati + ' · file letti ' + letti + ' · file non letti ' + nonLetti + '. SOLO DOCENTE: cognomi, email, link e testo dei Documenti.';
  var sh = vecchia || ss.insertSheet(nomeSh);
  sh.clear();
  sh.getRange(1, 1).setValue(classe + ' · Documenti · dati letti il ' + adesso).setFontWeight('bold');
  sh.getRange(2, 1).setValue(leg);
  sh.getRange(3, 1).setValue(rie);
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  sh.setFrozenRows(4);
  /* scheda pubblica: solo Nome I., stato, ora, immagini si/no/n.d.; niente email, link, titolo del file ne testo */
  var nomiU = [], vis = {};
  stOrd.forEach(function (st) { if (!vis[st.nome]) { vis[st.nome] = 1; nomiU.push(st.nome); } });
  var brevi = SM_brevi_(nomiU), mapB = {};
  nomiU.forEach(function (n, k) { mapB[n] = brevi[k]; });
  var testaP = ['Allievo', 'Compito', 'Stato', 'Ora consegna', 'Immagini presenti', 'Immagini aggiunte', 'Caratteri'];
  var datiP = righe.map(function (x) {
    var agg = x[13], pres = typeof agg === 'number' ? (agg > 0 ? 'sì' : 'no') : 'n.d.';
    return [mapB[x[0]] || 'Allievo', x[2], x[4], x[5], pres, agg, x[14]];
  });
  var shp = ss.getSheetByName('Documenti pubblica ' + classe) || ss.insertSheet('Documenti pubblica ' + classe);
  shp.clear();
  shp.getRange(1, 1).setValue(classe + ' · Documenti (pubblica, solo Nome I.) · dati letti il ' + adesso).setFontWeight('bold');
  shp.getRange(2, 1).setValue(leg);
  shp.getRange(3, 1).setValue(rie.replace(/ SOLO DOCENTE.*$/, ''));
  shp.getRange(4, 1, 1, testaP.length).setValues([testaP]).setFontWeight('bold').setBackground('#e8eef9');
  if (datiP.length) shp.getRange(5, 1, datiP.length, testaP.length).setValues(datiP);
  shp.setFrozenRows(4);
}
function FB_documenti_(ss, indice, t0) {
  var cfg0 = indice.classroom;
  if (!cfg0 || cfg0.attivo === false) return;
  if (typeof Classroom === 'undefined') return;   /* lo dice gia FB_classroom_ */
  if (Date.now() - t0 > 170000) return;
  var T = FB_json_('FB_DOC_T'), ora = Date.now(), dovute = [], corsi = null;
  IX_CLASSI_.forEach(function (c) {
    if (!(cfg0.classi || {})[c]) return;
    var cfg = DC_cfg_(indice, c);
    if (!cfg) return;
    if (!ss.getSheetByName('Documenti ' + c) || ora - Number(T[c] || 0) >= cfg.ogni * 60000 - 20000) dovute.push({ c: c, cfg: cfg });
  });
  if (!dovute.length) return;
  dovute.sort(function (a, b) { return Number(T[a.c] || 0) - Number(T[b.c] || 0); });
  var d = dovute[0], id = '';
  var sc = ss.getSheetByName('Corsi');
  if (sc) {
    var v = sc.getDataRange().getValues();
    for (var i = 1; i < v.length; i++) if (v[i][2] === d.c && v[i][1]) { id = String(v[i][1]); break; }
  }
  if (!id) {
    var corsiApi = CR_corsi_(), mappa = cfg0.classi || {};
    for (var j = 0; j < corsiApi.length; j++) if (CR_classe_(corsiApi[j].name, mappa) === d.c) { id = corsiApi[j].id; break; }
  }
  if (!id) { FB_ERRS.push('Documenti ' + d.c + ': corso Classroom non trovato (scheda Corsi)'); T[d.c] = ora; FB_salva_('FB_DOC_T', T); return; }
  try { DC_scheda_(ss, d.c, id, d.cfg, t0); T[d.c] = Date.now(); FB_salva_('FB_DOC_T', T); }
  catch (e) { T[d.c] = Date.now(); FB_salva_('FB_DOC_T', T); FB_errore_(ss, 'Documenti ' + d.c, e); }
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
    RS_NC_ = {};
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
      try { FB_documenti_(ss, indice, t0); } catch (e) { FB_errore_(ss, 'documenti', e); }
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
