/*
  crea-quiz-sicurezza-1ora-2inf.gs — crea AUTOMATICAMENTE un Quiz su Google Moduli
  Classe 2 INF · SICUREZZA 1ª ORA: "Concetti di rischio e danno"
  (Rischio, Danno, Prevenzione, Protezione — protocollo scuola / D.Lgs 81/2008) · SOLO ITALIANO
  Il quiz assegna il PUNTEGGIO da solo (20 domande x 5 punti = 100).

  COME SI USA:
  1. Vai su  script.google.com  e crea un "Nuovo progetto".
  2. Cancella il codice di esempio e INCOLLA tutto questo file.
  3. In alto scegli la funzione  creaQuiz  e premi "Esegui".
  4. Autorizza con l'account SCUOLA quando lo chiede.
  5. In "Esecuzioni" (in basso) trovi il LINK del Modulo: allegalo come Compito su Classroom.

  QUANDO: in 6ª ora, DOPO aver visto la videolezione e le slide della 1ª ora.
*/

function creaQuiz() {
  var form = FormApp.create('Quiz — Sicurezza 1ª ora: Rischio e Danno (Classe 2)')
    .setIsQuiz(true)
    .setDescription('Verifica sulla 1ª ora di sicurezza: salute, pericolo, danno, rischio, prevenzione e protezione. Leggi con calma e scegli la risposta giusta. Puoi riguardare le slide.');
  form.setCollectEmail(true);
  form.setShuffleQuestions(false);

  // OBBLIGATORIO: Nome e Cognome (regola: ogni quiz/Modulo deve chiederli)
  form.addTextItem()
    .setTitle('Nome e Cognome')
    .setHelpText('Scrivi il tuo nome e cognome (obbligatorio).')
    .setRequired(true);

  var domande = [
    { t: '1) Che cos\'è la SALUTE (secondo l\'OMS e il D.Lgs 81/2008)?',
      o: [['Uno stato di completo benessere fisico, mentale e sociale, non solo assenza di malattia', true],
          ['Soltanto non avere la febbre', false],
          ['Essere forti e muscolosi', false],
          ['Non andare mai dal medico', false]] },
    { t: '2) Perché a scuola si fa la formazione obbligatoria sulla sicurezza?',
      o: [['Perché è richiesta per legge per poter fare stage/alternanza e dà crediti utili al lavoro', true],
          ['Per riempire le ore vuote', false],
          ['Perché lo decide ogni insegnante a piacere', false],
          ['Non è obbligatoria, è facoltativa', false]] },
    { t: '3) Che cos\'è il PERICOLO?',
      o: [['La proprietà o qualità intrinseca di qualcosa, che ha la potenzialità di causare danni', true],
          ['La probabilità che succeda un danno', false],
          ['Un infortunio già avvenuto', false],
          ['La paura di farsi male', false]] },
    { t: '4) Che cos\'è il DANNO?',
      o: [['Un\'alterazione, transitoria o permanente, dell\'organismo o di una sua funzione', true],
          ['La qualità intrinseca di una sostanza', false],
          ['Un cartello di divieto', false],
          ['Una misura di protezione', false]] },
    { t: '5) Che cos\'è il RISCHIO?',
      o: [['La probabilità che il danno si verifichi davvero', true],
          ['La stessa cosa del pericolo', false],
          ['Un dispositivo di protezione', false],
          ['Il nome di una malattia', false]] },
    { t: '6) Qual è la differenza tra PERICOLO e RISCHIO?',
      o: [['Il pericolo è una qualità intrinseca; il rischio è la probabilità che quel pericolo causi un danno', true],
          ['Sono esattamente la stessa cosa', false],
          ['Il pericolo riguarda le macchine, il rischio solo le persone', false],
          ['Il rischio esiste solo in fabbrica, il pericolo solo a scuola', false]] },
    { t: '7) "È più rischiosa una bombola di gas o una bottiglia di alcool?" Perché non si può rispondere subito?',
      o: [['Perché conosciamo solo i pericoli, ma non il contesto (chi, dove, per fare cosa): mancano dati per quantificare il rischio', true],
          ['Perché la bombola è sempre più pericolosa, punto', false],
          ['Perché l\'alcool non è mai pericoloso', false],
          ['Perché il rischio non si può mai valutare', false]] },
    { t: '8) Il magazziniere col carrello in scarsa visibilità investe un collega (frattura). Lo "zaino per terra" su cui inciampa il docente. Cosa sono le condizioni che hanno elevato il rischio?',
      o: [['Sono i PERICOLI (diversi) presenti nelle due situazioni', true],
          ['Sono le protezioni', false],
          ['Sono le malattie professionali', false],
          ['Sono i dispositivi di prevenzione', false]] },
    { t: '9) Che cos\'è una LESIONE?',
      o: [['Una modificazione in senso patologico della struttura o funzione di un tessuto o organo', true],
          ['Un cartello di sicurezza', false],
          ['La probabilità di un infortunio', false],
          ['Un corso di formazione', false]] },
    { t: '10) Che cos\'è la PREVENZIONE?',
      o: [['L\'insieme di misure per ridurre la PROBABILITÀ che il danno si verifichi', true],
          ['Le misure per ridurre la gravità del danno', false],
          ['Curare chi si è già fatto male', false],
          ['Un tipo di infortunio', false]] },
    { t: '11) Che cos\'è la PROTEZIONE?',
      o: [['L\'insieme di misure e dispositivi (collettivi o individuali) per ridurre la GRAVITÀ di un evento dannoso', true],
          ['Le misure per ridurre la probabilità del danno', false],
          ['La qualità intrinseca di una sostanza', false],
          ['Il diritto alla salute', false]] },
    { t: '12) In sintesi: prevenzione e protezione...',
      o: [['La prevenzione riduce la probabilità del danno, la protezione ne riduce la gravità: insieme diminuiscono il rischio', true],
          ['Sono la stessa identica cosa', false],
          ['Servono solo dopo l\'infortunio', false],
          ['Riguardano solo i vigili del fuoco', false]] },
    { t: '13) Il DIVIETO DI FUMARE contro il rischio incendi è un intervento di...',
      o: [['Prevenzione (riduce la probabilità che scoppi l\'incendio)', true],
          ['Protezione', false],
          ['Cura', false],
          ['Nessuno dei due', false]] },
    { t: '14) Una MASCHERA ANTIPOLVERE per le vie respiratorie è un intervento di...',
      o: [['Protezione (riduce la gravità del danno sulla persona)', true],
          ['Prevenzione', false],
          ['Formazione', false],
          ['Valutazione del rischio', false]] },
    { t: '15) Un ESTINTORE è...',
      o: [['Un dispositivo di protezione dal fuoco', true],
          ['Una misura di prevenzione', false],
          ['Un pericolo', false],
          ['Una malattia professionale', false]] },
    { t: '16) Qual è l\'ordine giusto della gerarchia delle misure di prevenzione?',
      o: [['1) eliminare il rischio, 2) sostituire ciò che è pericoloso con qualcosa di meno pericoloso, 3) ridurre l\'esposizione', true],
          ['1) dare i guanti, 2) mettere cartelli, 3) sperare che vada bene', false],
          ['1) ridurre l\'esposizione, 2) curare, 3) eliminare', false],
          ['Non esiste un ordine', false]] },
    { t: '17) Perché "il pericolo per sua natura non può essere diminuito"?',
      o: [['Perché è una qualità intrinseca: su di esso si agisce eliminandolo o riducendo l\'esposizione, non "abbassandolo"', true],
          ['Perché il pericolo non esiste davvero', false],
          ['Perché basta ignorarlo', false],
          ['Perché lo decide il datore di lavoro', false]] },
    { t: '18) Come si ricava l\'entità del RISCHIO nella valutazione?',
      o: [['Combinando la PROBABILITÀ (P, da 1 a 4) e la GRAVITÀ del DANNO (D, da 1 a 4)', true],
          ['Solo dal numero di lavoratori', false],
          ['Solo dal costo delle macchine', false],
          ['A caso', false]] },
    { t: '19) Che cos\'è un INFORTUNIO sul lavoro?',
      o: [['Un incidente da causa violenta in occasione di lavoro, da cui deriva inabilità, invalidità o morte', true],
          ['Una malattia che arriva lentamente negli anni', false],
          ['Un cartello di divieto', false],
          ['Un dispositivo di protezione', false]] },
    { t: '20) La piramide "1 - 29 - 300": cosa rappresentano i 300 alla base?',
      o: [['Gli incidenti / quasi-infortuni (infortuni mancati): tanti segnali di una situazione a forte rischio', true],
          ['300 infortuni gravi al giorno', false],
          ['300 lavoratori per azienda', false],
          ['300 cartelli di sicurezza', false]] }
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
