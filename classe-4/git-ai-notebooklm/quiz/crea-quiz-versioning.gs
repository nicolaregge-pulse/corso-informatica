/*
  crea-quiz-versioning.gs — crea AUTOMATICAMENTE un Quiz su Google Moduli
  Argomento: Git e versioning · Lingua: italiano
  Il quiz assegna il PUNTEGGIO da solo (12 domande x 5 punti = 60).

  COME SI USA:
  1. Vai su  script.google.com  e crea un "Nuovo progetto".
  2. Cancella il codice di esempio e INCOLLA tutto questo file.
  3. In alto scegli la funzione  creaQuiz  e premi "Esegui".
  4. Autorizza con l'account SCUOLA quando lo chiede.
  5. In "Esecuzioni" (in basso) trovi il LINK del Modulo: allegalo come Compito su Classroom.
*/

function creaQuiz() {
  var form = FormApp.create('Quiz — Git e versioning (Classe 4)')
    .setIsQuiz(true)
    .setDescription('Verifica su Git, GitHub e il versioning. Una sola risposta giusta per domanda.');
  form.setCollectEmail(true);
  form.setShuffleQuestions(false);

  // OBBLIGATORIO: Nome e Cognome
  form.addTextItem().setTitle('Nome e Cognome').setRequired(true);

  var domande = [
    { t: 'Che differenza c\'e tra Git e GitHub?',
      o: [['Git e lo strumento che tiene la storia del progetto; GitHub e il servizio online dove i progetti vivono e si condividono', true],
          ['Sono la stessa identica cosa con due nomi', false],
          ['Git e un sito web; GitHub e un programma da installare', false],
          ['Git serve per le foto; GitHub per i video', false]] },
    { t: 'Che cos\'e un commit?',
      o: [['Un salvataggio del progetto (una "fotografia") con un messaggio', true],
          ['La cancellazione di tutti i file', false],
          ['Il nome del proprietario del progetto', false],
          ['Un errore di sistema', false]] },
    { t: 'Che cos\'e un branch (ramo)?',
      o: [['Una strada di lavoro parallela per provare senza rovinare la versione principale', true],
          ['Il cestino del progetto', false],
          ['Il pulsante per stampare', false],
          ['Un tipo di immagine', false]] },
    { t: 'Cosa propone una Pull Request?',
      o: [['Di unire il proprio ramo alla versione principale, dopo una revisione', true],
          ['Di cancellare il repository', false],
          ['Di cambiare la password', false],
          ['Di spegnere il computer', false]] },
    { t: 'Nel numero 1.2.3, la prima cifra (major) aumenta quando…',
      o: [['si fa un cambiamento grosso, magari incompatibile con il vecchio', true],
          ['si corregge un piccolo errore', false],
          ['si cambia il colore dell\'icona', false],
          ['non aumenta mai', false]] },
    { t: 'Nel numero 1.2.3, la terza cifra (patch) aumenta quando…',
      o: [['si corregge solo un bug, senza novita', true],
          ['si riscrive tutto da capo', false],
          ['si aggiunge una grande funzione nuova', false],
          ['si cancella il progetto', false]] },
    { t: 'Qual e la regola d\'oro del versioning?',
      o: [['Una versione gia pubblicata non si riusa: prima si aumenta il numero, poi si pubblica', true],
          ['Si puo cambiare una versione pubblicata quando si vuole', false],
          ['Il numero di versione si sceglie a caso', false],
          ['Le versioni non servono a niente', false]] },
    { t: 'Che cos\'e un merge?',
      o: [['Unire un ramo con quello principale (main)', true],
          ['Spegnere il progetto', false],
          ['Un tipo di file audio', false],
          ['La cancellazione della storia', false]] },
    { t: 'Che cos\'e un revert?',
      o: [['Un nuovo commit che annulla uno sbagliato, senza cancellare la storia', true],
          ['La formattazione del disco', false],
          ['Il ripristino della password', false],
          ['Un ramo abbandonato', false]] },
    { t: 'Quando avviene un conflitto di merge?',
      o: [['Quando due rami hanno cambiato la stessa riga in modo diverso', true],
          ['Quando il computer e spento', false],
          ['Quando manca la corrente', false],
          ['Quando il file e troppo grande', false]] },
    { t: 'Che tipo di servizio e GitHub?',
      o: [['PaaS (una piattaforma online gia pronta)', true],
          ['Un videogioco', false],
          ['Un programma di disegno', false],
          ['Un antivirus', false]] },
    { t: 'Con quale modello si paga GitHub?',
      o: [['Freemium: base gratis, funzioni avanzate a pagamento', true],
          ['Solo a pagamento, sempre', false],
          ['Non esiste, e vietato', false],
          ['Si paga a ore', false]] }
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
