/**
 * Crea un TEST A RISPOSTA APERTA su Google Moduli — Sicurezza 1a ora (2INF).
 * Obiettivo: far scrivere con PAROLE LORO (anti copia / anti AI). Le domande chiedono
 * esempi personali e "questa aula": cose che la slide e l'AI non possono sapere, quindi
 * una risposta copiata/generica si riconosce subito.
 *
 * NON e' un quiz a punteggio automatico: le risposte aperte si leggono/valutano dopo
 * (l'export si da' all'assistente del corso per il controllo "parole loro").
 *
 * USO: Estensioni > Apps Script (o script.google.com) > incolla > Esegui
 *      creaTestApertoSicurezza > autorizza > nei Log trovi i 2 link (compilazione + modifica).
 */
function creaTestApertoSicurezza() {
  var form = FormApp.create('Test aperto — Sicurezza 1ª ora (2INF): con parole TUE')
    .setDescription(
      'Rispondi con PAROLE TUE e con ESEMPI TUOI. ' +
      'Non copiare dalla slide né da internet/AI: le risposte copiate si riconoscono ' +
      '(sono tutte uguali e generiche) e valgono MENO di una risposta semplice ma tua, ' +
      'anche con qualche errore. Meglio poco ma tuo.')
    .setCollectEmail(true)
    .setProgressBar(true);

  // Nome e Cognome (obbligatorio)
  form.addTextItem().setTitle('Nome e Cognome').setRequired(true);

  var domande = [
    '1) Con parole TUE: cos\'è la SALUTE? (non la definizione a memoria — cosa significa per te stare bene)',
    '2) Fai un ESEMPIO TUO (casa, scuola o sport) di un PERICOLO e del RISCHIO collegato. Spiega perché.',
    '3) Guarda QUESTA aula/laboratorio adesso: scrivi UN pericolo che vedi qui e come ridurresti il rischio.',
    '4) Spiega a un amico che non c\'era la differenza tra PERICOLO e RISCHIO, con parole tue.',
    '5) Perché NON si può dire subito se è più rischiosa una bombola di gas o una bottiglia di alcool?',
    '6) Inventa un ESEMPIO TUO di una misura di PREVENZIONE e una di PROTEZIONE (NON estintore e mascherina).',
    '7) Cos\'è un INFORTUNIO sul lavoro? Spiegalo con parole tue.',
    '8) Racconta un piccolo incidente o "quasi-incidente" che hai visto o vissuto: il rischio era alto? Perché?',
    '9) Perché a TE conviene imparare la sicurezza? Collegalo al lavoro/stage che vorresti fare.',
    '10) Scrivi UNA cosa della lezione che NON hai capito bene (va benissimo dirlo: serve a me per aiutarti).'
  ];

  domande.forEach(function(q) {
    form.addParagraphTextItem().setTitle(q).setRequired(q.indexOf('10)') !== 0);
  });

  Logger.log('LINK PER GLI ALLIEVI: ' + form.getPublishedUrl());
  Logger.log('LINK PER MODIFICARE: ' + form.getEditUrl());
}
