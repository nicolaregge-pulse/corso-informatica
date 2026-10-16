/*
  crea-quiz-modulo2.gs — crea AUTOMATICAMENTE un Quiz su Google Moduli
  Classe 2 INF · SICUREZZA Modulo 2: "I soggetti della sicurezza e i diritti/doveri"
  (Datore, dirigente, preposto, RSPP, medico competente, RLS, lavoratore; diritti/doveri;
   organi di vigilanza — Accordo Stato-Regioni / D.Lgs 81/2008) · SOLO ITALIANO
  14 domande x 3 punti = 42 (punteggio automatico). Ordine domande mescolato per ogni ragazzo.

  ANTI-AI (come chiesto):
  - Domande PERSONALI e a SCENARIO ("Tu sei in stage...", "Nel tuo reparto...").
  - La risposta che un'AI sceglie "a occhio" (la più generica/comoda) è messa come TRAPPOLA:
    serve leggere il caso e applicare la regola, non ripetere la definizione.
  - setShuffleQuestions(true).
  - Onesto: Moduli NON blocca l'incolla. Il blocco vero dell'incolla + tempo di scrittura
    misurato ce l'ha il nostro motore "verifica" (docs/verifica). Qui l'anti-AI è nel COME
    sono scritte le domande + farlo in classe con Veyon e tempo corto.

  COME SI USA:
  1. script.google.com -> Nuovo progetto. 2. Incolla tutto questo file.
  3. Scegli creaQuiz e premi Esegui. 4. Autorizza con l'account SCUOLA.
  5. In "Esecuzioni" trovi il LINK: allegalo come Compito su Classroom.

  CHIAVE (per il docente) — la risposta GIUSTA è quella segnata true (posizione variabile):
  1 DPI gratis dall'azienda · 2 cavo scoperto: non toccare e segnalare · 3 collega senza occhiali:
  segnalare (è dovere di tutti) · 4 attrezzo senza istruzioni: fermarsi e chiedere formazione ·
  5 primo responsabile: datore · 6 preposto: controlla sul campo · 7 RSPP: esperto che consiglia ·
  8 medico competente: visite mediche · 9 RLS: eletto dai colleghi · 10 controllo esterno: ASL/Ispettorato ·
  11 INAIL: assicura in caso di infortunio · 12 sedia rotta/mal di schiena: segnalare (preposto/RLS) ·
  13 saltare la formazione: no, è un diritto/dovere · 14 cliente senza scarpe in area pericolosa: va fermato.
*/

function creaQuiz() {
  var form = FormApp.create('Quiz — Sicurezza Modulo 2: i soggetti e i doveri (Classe 2)')
    .setIsQuiz(true)
    .setDescription('Casi veri di officina/azienda. Leggi bene OGNI situazione: la risposta "facile" non è sempre quella giusta. Rispondi come se fossi tu nella scena.');
  form.setCollectEmail(true);
  form.setShuffleQuestions(true);

  form.addTextItem().setTitle('Nome e Cognome').setHelpText('Obbligatorio.').setRequired(true);

  // In ogni domanda la risposta giusta è segnata con true, ma in posizione VARIABILE.
  var domande = [
    { t: '1) Primo giorno di stage. Il tuo capo ti dice: «I guanti e le scarpe antinfortunistiche compratele tu». Che cosa pensi?',
      o: [['«Va bene, i DPI li paga sempre il lavoratore»', false],
          ['«No: i DPI me li deve dare l\'azienda, gratis. È un mio diritto»', true],
          ['«Li compro solo se mi fanno male le mani»', false],
          ['«Non servono, basta stare attenti»', false]] },
    { t: '2) Nel tuo reparto vedi un cavo elettrico scoperto per terra. Qual è la cosa GIUSTA?',
      o: [['Aggiustarlo da solo in fretta, così nessuno inciampa', false],
          ['Coprirlo con lo scotch e continuare', false],
          ['Non toccarlo e segnalarlo subito al preposto', true],
          ['Lasciar stare: non è un problema mio', false]] },
    { t: '3) Un collega usa il trapano SENZA occhiali di protezione. Tu sei solo uno studente in stage. Che fai?',
      o: [['Niente: sono in stage, non è compito mio', false],
          ['Lo dico al preposto o avviso il collega: segnalare i pericoli è un dovere di tutti', true],
          ['Prendo gli occhiali e li metto io al posto suo', false],
          ['Filmo la scena col telefono', false]] },
    { t: '4) Il preposto ti dà un attrezzo nuovo senza spiegarti come si usa e dice «sbrigati». Tu…',
      o: [['Lo uso comunque, per non fare brutta figura', false],
          ['Mi rifiuto e me ne vado a casa', false],
          ['Mi fermo e chiedo la formazione/le istruzioni: ho diritto a lavorare in sicurezza', true],
          ['Chiedo a un compagno di usarlo al posto mio', false]] },
    { t: '5) Nella tua azienda, chi è il PRIMO responsabile della sicurezza?',
      o: [['Il datore di lavoro (chi comanda e decide)', true],
          ['Lo studente in stage', false],
          ['Il cliente', false],
          ['Nessuno: è facoltativa', false]] },
    { t: '6) Il tuo capo-reparto che ti controlla mentre lavori e ti corregge subito: che ruolo ha?',
      o: [['Medico competente', false],
          ['RSPP', false],
          ['Preposto', true],
          ['RLS', false]] },
    { t: '7) In azienda arriva un esperto che studia i rischi e scrive come difendersi, ma non comanda nessuno. Chi è?',
      o: [['Il RSPP', true],
          ['Il datore di lavoro', false],
          ['Il medico competente', false],
          ['Un cliente', false]] },
    { t: '8) Ti chiamano per una visita per controllare la tua salute al lavoro. Chi la fa?',
      o: [['Il preposto', false],
          ['Il medico competente', true],
          ['L\'RLS', false],
          ['L\'INAIL', false]] },
    { t: '9) I tuoi colleghi votano uno di voi perché parli con l\'azienda dei problemi di sicurezza. Quel collega è…',
      o: [['Il titolare', false],
          ['Un medico esterno', false],
          ['Il RLS (Rappresentante dei Lavoratori per la Sicurezza)', true],
          ['Un ispettore dello Stato', false]] },
    { t: '10) Chi può venire DA FUORI a controllare che la tua azienda rispetti la sicurezza?',
      o: [['Nessuno: dentro decide solo il titolare', false],
          ['Gli organi di vigilanza: ASL/ATS e Ispettorato del lavoro', true],
          ['I clienti', false],
          ['I fornitori', false]] },
    { t: '11) Ti fai male a una mano con una macchina al lavoro. Quale ente ti aiuta economicamente?',
      o: [['L\'INAIL', true],
          ['L\'RLS', false],
          ['Il medico competente', false],
          ['Il negozio dei DPI', false]] },
    { t: '12) La tua sedia è rotta e ti viene mal di schiena. Che cosa fai PER PRIMO?',
      o: [['Niente: il mal di schiena è normale al lavoro', false],
          ['Lo segnalo al preposto (e posso rivolgermi all\'RLS)', true],
          ['Cambio lavoro', false],
          ['Aspetto che se ne accorgano gli altri', false]] },
    { t: '13) Il capo dice: «Salta la formazione sulla sicurezza, così iniziamo prima». Tu…',
      o: [['«Va bene, decide lui»', false],
          ['«La formazione è un mio diritto e un dovere: non si salta»', true],
          ['«La faccio un\'altra volta, non è importante»', false],
          ['«La faccio solo se mi pagano di più»', false]] },
    { t: '14) Un cliente entra in area pericolosa dell\'officina senza scarpe antinfortunistiche. Che cosa è giusto?',
      o: [['I clienti non c\'entrano con la sicurezza', false],
          ['Va avvisato e fermato: la sicurezza vale anche per chi entra', true],
          ['Non è un problema, tanto sta poco', false],
          ['Gli presto le mie scarpe', false]] }
  ];

  domande.forEach(function(d) {
    var item = form.addMultipleChoiceItem();
    item.setTitle(d.t).setPoints(3).setRequired(true);
    item.setChoices(d.o.map(function(c){ return item.createChoice(c[0], c[1]); }));
  });

  Logger.log('FATTO. Link per te (modifica): ' + form.getEditUrl());
  Logger.log('Link per gli allievi: ' + form.getPublishedUrl());
}
