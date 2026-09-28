/*
  crea-quiz-tipi-di-file-2inf.gs — crea AUTOMATICAMENTE un Quiz su Google Moduli
  Classe 2 INF · Argomento: I TIPI DI FILE · Lingua: SOLO ITALIANO
  Il quiz assegna il PUNTEGGIO da solo (20 domande x 5 punti = 100).

  COME SI USA:
  1. Vai su  script.google.com  e crea un "Nuovo progetto".
  2. Cancella il codice di esempio e INCOLLA tutto questo file.
  3. In alto scegli la funzione  creaQuiz  e premi "Esegui".
  4. Autorizza con l'account SCUOLA quando lo chiede.
  5. In "Esecuzioni" (in basso) trovi il LINK del Modulo: allegalo come Compito su Classroom.
*/

function creaQuiz() {
  var form = FormApp.create('Quiz — I tipi di file (Classe 2)')
    .setIsQuiz(true)
    .setDescription('Verifica su: i tipi di file (estensioni, testo/binario, formati, file a tag, compressione, percorso, Markdown). Leggi con calma e scegli la risposta giusta. Puoi usare la dispensa.');
  form.setCollectEmail(true);
  form.setShuffleQuestions(false);

  var domande = [
    { t: '1) Che cos\'è un file?',
      o: [['Un contenitore di informazioni salvato nel computer (testo, foto, video…)', true],
          ['Solo una fotografia', false],
          ['Un programma che pulisce il computer', false],
          ['Una cartella vuota', false]] },
    { t: '2) A cosa serve l\'estensione (le lettere dopo il punto, es. .jpg)?',
      o: [['A dire di che tipo è il file e con quale programma aprirlo', true],
          ['A rendere il file più pesante', false],
          ['A cancellare il file', false],
          ['A colorare l\'icona', false]] },
    { t: '3) Se rinomino "foto.jpg" in "foto.txt", cosa succede?',
      o: [['Resta una foto: cambia solo l\'etichetta, non il contenuto', true],
          ['Diventa un vero file di testo', false],
          ['La foto si cancella', false],
          ['Il computer si blocca', false]] },
    { t: '4) Come capisci se un file è di TESTO o BINARIO?',
      o: [['Lo apro col Blocco note: se lo leggo è testo, se vedo simboli strani è binario', true],
          ['Guardo il colore dell\'icona', false],
          ['Dalla grandezza in MB', false],
          ['Non si può capire', false]] },
    { t: '5) Quale di questi è un file di TESTO (leggibile col Blocco note)?',
      o: [['.txt', true], ['.mp3', false], ['.jpg', false], ['.exe', false]] },
    { t: '6) Quale di questi è un file BINARIO?',
      o: [['.png', true], ['.txt', false], ['.md', false], ['.csv', false]] },
    { t: '7) Il formato .txt serve per…',
      o: [['Scrivere testo semplice, senza colori né grassetto', true],
          ['Salvare video ad alta qualità', false],
          ['Comprimere tanti file insieme', false],
          ['Fare fotografie', false]] },
    { t: '8) Il formato PDF serve soprattutto per…',
      o: [['Un documento impaginato che si vede uguale ovunque e si stampa bene', true],
          ['Registrare l\'audio', false],
          ['Programmare un gioco', false],
          ['Comprimere una cartella', false]] },
    { t: '9) A cosa serve il formato ZIP?',
      o: [['A mettere più file in uno solo e comprimerli (pesano meno)', true],
          ['A scrivere una canzone', false],
          ['A creare un sito web', false],
          ['A stampare un documento', false]] },
    { t: '10) Differenza tra PNG e JPG?',
      o: [['PNG senza perdita e con sfondo trasparente; JPG più compresso per le foto', true],
          ['Sono la stessa identica cosa', false],
          ['PNG è un video, JPG è un suono', false],
          ['JPG non si apre mai', false]] },
    { t: '11) Il formato MP4 è…',
      o: [['Un video (immagini in movimento + audio insieme)', true],
          ['Un foglio di calcolo', false],
          ['Un\'immagine fissa', false],
          ['Un archivio compresso', false]] },
    { t: '12) Che cos\'è un file CSV?',
      o: [['Una tabella scritta come testo, con le colonne separate da virgole', true],
          ['Un video compresso', false],
          ['Un programma da installare', false],
          ['Una foto con sfondo trasparente', false]] },
    { t: '13) Quali di questi sono file "a TAG" (con etichette)?',
      o: [['HTML, XML, MD', true],
          ['JPG, MP3, EXE', false],
          ['ZIP, RAR, 7Z', false],
          ['TXT, CSV, WAV', false]] },
    { t: '14) In HTML, cosa fa il tag <b>…</b>?',
      o: [['Mette la parola in grassetto', true],
          ['Crea un titolo grande', false],
          ['Inserisce un\'immagine', false],
          ['Crea un link', false]] },
    { t: '15) In HTML, cosa fa il tag <h1>…</h1>?',
      o: [['Crea il titolo principale (grande)', true],
          ['Mette in corsivo', false],
          ['Crea un paragrafo piccolo', false],
          ['Cancella il testo', false]] },
    { t: '16) In Markdown (MD), il simbolo # all\'inizio della riga serve a…',
      o: [['Fare un titolo', true],
          ['Mettere in grassetto', false],
          ['Andare a capo', false],
          ['Cancellare la riga', false]] },
    { t: '17) La compressione SENZA perdita (lossless): quale esempio è giusto?',
      o: [['ZIP o PNG: il file torna identico all\'originale', true],
          ['JPG: butta via dei dettagli', false],
          ['MP3: perde un po\' di qualità', false],
          ['MP4: perde dei fotogrammi', false]] },
    { t: '18) La compressione CON perdita (lossy): quale esempio è giusto?',
      o: [['JPG o MP3: si butta un po\' di dettaglio e il file pesa molto meno', true],
          ['ZIP: torna tutto identico', false],
          ['PNG: non perde nulla', false],
          ['TXT: è solo testo', false]] },
    { t: '19) Che cos\'è il "percorso" (path) di un file?',
      o: [['L\'indirizzo del file nel computer (le cartelle per arrivarci)', true],
          ['Il peso del file in MB', false],
          ['Il colore dell\'icona', false],
          ['Il nome del programma che l\'ha creato', false]] },
    { t: '20) Perché diamo le dispense anche in Markdown (.md) per usarle con l\'intelligenza artificiale?',
      o: [['Perché è testo puro e pulito: l\'AI lo legge bene per spiegare/tradurre', true],
          ['Perché è un video', false],
          ['Perché pesa più di un PDF', false],
          ['Perché non si può leggere', false]] }
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
