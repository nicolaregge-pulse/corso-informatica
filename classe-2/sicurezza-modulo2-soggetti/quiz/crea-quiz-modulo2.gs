/*
  crea-quiz-modulo2.gs — crea AUTOMATICAMENTE un Quiz su Google Moduli
  Classe 2 INF · SICUREZZA Modulo 2: "I soggetti della sicurezza e i diritti/doveri"
  (Datore di lavoro, dirigente, preposto, RSPP, medico competente, RLS, lavoratore;
   diritti e doveri del lavoratore; organi di vigilanza — Accordo Stato-Regioni / D.Lgs 81/2008) · SOLO ITALIANO
  Il quiz assegna il PUNTEGGIO da solo (8 domande x 5 punti = 40).

  COME SI USA:
  1. Vai su  script.google.com  e crea un "Nuovo progetto".
  2. Cancella il codice di esempio e INCOLLA tutto questo file.
  3. In alto scegli la funzione  creaQuiz  e premi "Esegui".
  4. Autorizza con l'account SCUOLA quando lo chiede.
  5. In "Esecuzioni" (in basso) trovi il LINK del Modulo: allegalo come Compito su Classroom.

  QUANDO: DOPO aver visto la teoria del Modulo 2 (chi fa cosa + diritti/doveri del lavoratore).

  CHIAVE DELLE RISPOSTE (per il docente) — la risposta corretta è SEMPRE la prima scritta nel codice:
  1) Datore di lavoro = primo responsabile della sicurezza
  2) Preposto = controlla sul campo (il capo-reparto)
  3) RSPP = l'esperto che studia i rischi e consiglia
  4) Medico competente = fa le visite mediche
  5) RLS = eletto dai colleghi, è la voce dei lavoratori
  6) Diritto del lavoratore = ricevere i DPI gratis
  7) Dovere del lavoratore = NON togliere le protezioni + segnalare i pericoli
  8) INAIL = assicura il lavoratore se si fa male sul lavoro
*/

function creaQuiz() {
  var form = FormApp.create('Quiz — Sicurezza Modulo 2: i soggetti e i diritti/doveri (Classe 2)')
    .setIsQuiz(true)
    .setDescription('Verifica sul Modulo 2 di sicurezza: chi si occupa della sicurezza in azienda (datore di lavoro, preposto, RSPP, medico competente, RLS, lavoratore) e i diritti/doveri del lavoratore. Leggi con calma e scegli la risposta giusta. Puoi riguardare la teoria.');
  form.setCollectEmail(true);
  form.setShuffleQuestions(false);

  // OBBLIGATORIO: Nome e Cognome (regola: ogni quiz/Modulo deve chiederli)
  form.addTextItem()
    .setTitle('Nome e Cognome')
    .setHelpText('Scrivi il tuo nome e cognome (obbligatorio).')
    .setRequired(true);

  var domande = [
    { t: '1) Chi è il PRIMO responsabile della sicurezza in un\'azienda?',
      o: [['Il datore di lavoro (chi comanda e decide)', true],
          ['Il lavoratore appena assunto', false],
          ['Il cliente che entra in azienda', false],
          ['Nessuno, la sicurezza è facoltativa', false]] },
    { t: '2) Chi è il PREPOSTO?',
      o: [['Il capo-reparto che controlla sul campo e corregge subito chi sbaglia', true],
          ['Il medico che fa le visite', false],
          ['L\'esperto che scrive il documento dei rischi', false],
          ['Il controllore che viene da fuori', false]] },
    { t: '3) Che cosa fa il RSPP (Responsabile del Servizio di Prevenzione e Protezione)?',
      o: [['È l\'esperto: studia i rischi dell\'azienda e consiglia come difendersi', true],
          ['Comanda l\'azienda al posto del datore di lavoro', false],
          ['Fa le visite mediche ai lavoratori', false],
          ['Viene eletto dai colleghi per parlare al posto loro', false]] },
    { t: '4) Che cosa fa il MEDICO COMPETENTE?',
      o: [['Fa le visite mediche ai lavoratori per controllare la loro salute', true],
          ['Decide quali macchine comprare', false],
          ['Controlla che tutti usino i guanti sul campo', false],
          ['Assicura i lavoratori in caso di infortunio', false]] },
    { t: '5) Chi è il RLS (Rappresentante dei Lavoratori per la Sicurezza)?',
      o: [['Un lavoratore eletto dai colleghi, che è la loro voce con l\'azienda', true],
          ['Il titolare dell\'azienda', false],
          ['Un medico esterno', false],
          ['Un controllore dell\'Ispettorato del lavoro', false]] },
    { t: '6) Qual è un DIRITTO del lavoratore (anche dello studente in stage)?',
      o: [['Ricevere i DPI (guanti, occhiali, scarpe...) gratis, senza pagarli', true],
          ['Decidere lui da solo quali rischi correre', false],
          ['Togliere le protezioni quando ha fretta', false],
          ['Non fare mai la formazione sulla sicurezza', false]] },
    { t: '7) Qual è un DOVERE del lavoratore?',
      o: [['Non togliere le protezioni e segnalare subito i pericoli che vede', true],
          ['Nascondere i guasti per non fare brutta figura', false],
          ['Usare le macchine come gli pare, senza istruzioni', false],
          ['Lasciare che pensino alla sicurezza solo gli altri', false]] },
    { t: '8) A che cosa serve l\'INAIL?',
      o: [['Assicura i lavoratori: se ti fai male sul lavoro, ti aiuta economicamente', true],
          ['Fa le visite mediche in azienda', false],
          ['Vende i dispositivi di protezione', false],
          ['Elegge il rappresentante dei lavoratori', false]] }
  ];

  domande.forEach(function(d) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(d.t).setPoints(5).setRequired(true);
    var choices = d.o.map(function(c){ return item.createChoice(c[0], c[1]); });
    item.setChoices(choices);
  });

  Logger.log('FATTO. Link da modificare (per te): ' + form.getEditUrl());
  Logger.log('Link da dare/allegare (per gli allievi): ' + form.getPublishedUrl());
}
