/*
  crea-verifica-for.gs — crea su Google Moduli la VERIFICA sul ciclo FOR in Lazarus (2INF, ottobre 2026).
  Versione 1.0 — 19/10/2026 · solo italiano (2INF, RIFERIMENTI §2.49)
  24 domande: crocette con una o PIÙ risposte giuste (punteggio automatico), codice giusto/sbagliato,
  «che cosa scrive il Memo», e 4 domande dove si SCRIVE un pezzo di codice (le corregge il docente o Claude).
  Il Modulo raccoglie anche l'email (traccia per la Regione: si allega al compito su Classroom).

  COME SI USA (finestra PIAMARTA):
  1. script.google.com → «Nuovo progetto».
  2. Cancella il codice di esempio e incolla questo file.
  3. In alto scegli la funzione  creaVerificaFor  e premi «Esegui»; autorizza con l'account della scuola.
  4. In «Log esecuzione» trovi i due link: quello da dare ai ragazzi e quello per modificare.
*/

function creaVerificaFor() {
  var form = FormApp.create('Verifica — Il ciclo FOR in Lazarus (2INF)')
    .setIsQuiz(true)
    .setCollectEmail(true)
    .setLimitOneResponsePerUser(true)
    .setShuffleQuestions(false)
    .setDescription(
      'Verifica sul ciclo FOR (il programma Contatore e la tabellina).\n' +
      'Leggi bene: in alcune domande le risposte giuste sono PIÙ DI UNA (c\'è scritto «una o più»).\n' +
      'Nelle ultime domande scrivi tu il codice: va bene anche se non è perfetto, conta l\'idea giusta.\n' +
      'Puoi aprire Lazarus e provare il codice. Non puoi copiare da un compagno.');

  form.addTextItem().setTitle('Cognome e nome').setRequired(true);

  // ---------- helper ----------
  function una(titolo, opzioni, punti, aiuto) {          // una sola giusta
    var it = form.addMultipleChoiceItem().setTitle(titolo).setPoints(punti || 2).setRequired(true);
    if (aiuto) it.setHelpText(aiuto);
    it.setChoices(opzioni.map(function (o) { return it.createChoice(o[0], o[1]); }));
  }
  function piu(titolo, opzioni, punti, aiuto) {          // una o più giuste
    var it = form.addCheckboxItem().setTitle(titolo + '  (una o più risposte giuste)').setPoints(punti || 3).setRequired(true);
    if (aiuto) it.setHelpText(aiuto);
    it.setChoices(opzioni.map(function (o) { return it.createChoice(o[0], o[1]); }));
  }
  function scrivi(titolo, aiuto) {                       // codice da scrivere: lo corregge il docente
    form.addParagraphTextItem().setTitle(titolo).setHelpText(aiuto).setRequired(true);
  }

  // ---------- PARTE 1: che cos'è il FOR ----------
  form.addSectionHeaderItem().setTitle('Parte 1 — Che cos\'è il ciclo FOR');

  una('1) Il ciclo FOR serve a…', [
    ['ripetere delle istruzioni un numero di volte che si conosce prima', true],
    ['fare una scelta tra due strade, come l\'IF', false],
    ['chiudere il programma', false],
    ['scrivere un testo in un Edit', false]]);

  una('2) In  for x := 1 to 10 do  la variabile x si chiama…', [
    ['contatore (variabile di controllo)', true],
    ['costante', false],
    ['bottone', false],
    ['procedura', false]]);

  piu('3) Quali righe scrivono un ciclo FOR CORRETTO in Lazarus?', [
    ['for i := 1 to 5 do', true],
    ['for i := 5 downto 1 do', true],
    ['for i = 1 to 5 do', false],
    ['for i := 1 to 5', false],
    ['for (i := 1; i <= 5) do', false]],
    3, 'Attenzione ai due punti prima dell\'uguale e al «do» finale.');

  una('4) Che tipo deve avere la variabile del ciclo FOR?', [
    ['integer (un numero intero)', true],
    ['string (un testo)', false],
    ['real (un numero con la virgola)', false]]);

  una('5) Dove si dichiara la variabile del ciclo, per esempio  x: integer;  ?', [
    ['nella parte  var  prima di  begin', true],
    ['dentro il ciclo, dopo  do', false],
    ['nell\'Ispettore oggetti', false]]);

  piu('6) Quando dentro il ciclo ci sono DUE o più istruzioni, che cosa serve?', [
    ['begin all\'inizio delle istruzioni', true],
    ['end; alla fine delle istruzioni', true],
    ['niente: Lazarus le capisce da solo', false],
    ['un secondo  do', false]]);

  // ---------- PARTE 2: quante volte? che cosa scrive? ----------
  form.addSectionHeaderItem().setTitle('Parte 2 — Quante volte? Che cosa scrive il Memo?');

  una('7) Quante volte gira  for i := 1 to 10 do ?', [
    ['10', true], ['9', false], ['11', false], ['1', false]]);

  una('8) Quante volte gira  for i := 3 to 7 do ?', [
    ['5', true], ['4', false], ['7', false], ['3', false]]);

  una('9) Quante volte gira  for i := 5 to 1 do ?', [
    ['0: non parte, perché 5 è più grande di 1 (serve downto)', true],
    ['5', false], ['4', false], ['va avanti per sempre', false]]);

  una('10) Che cosa scrive nel Memo questo codice?\nfor i := 1 to 3 do\n  Memo1.Lines.Add(IntToStr(i));', [
    ['1, 2, 3 (uno per riga)', true],
    ['3, 2, 1', false],
    ['solo 3', false],
    ['1, 2', false]]);

  una('11) Che cosa scrive nel Memo?\nfor i := 4 downto 2 do\n  Memo1.Lines.Add(IntToStr(i));', [
    ['4, 3, 2', true], ['2, 3, 4', false], ['4, 2', false], ['niente', false]]);

  una('12) Che cosa scrive nel Memo?\nfor i := 1 to 3 do\n  Memo1.Lines.Add(IntToStr(i * 2));', [
    ['2, 4, 6', true], ['1, 2, 3', false], ['3, 6, 9', false], ['2, 3, 4', false]]);

  una('13) Nel programma Contatore, l\'Edit «da» contiene 3 e l\'Edit «a» contiene 6.\nfor x := StrToInt(Edit1.Text) to StrToInt(Edit2.Text) do\n  Memo1.Lines.Add(IntToStr(x));\nQuante righe compaiono nel Memo?', [
    ['4 (3, 4, 5, 6)', true], ['3', false], ['6', false], ['36', false]]);

  una('14) Che cosa fa  sleep(1000)  dentro il ciclo del Contatore?', [
    ['aspetta 1 secondo prima di continuare, così si vede contare', true],
    ['conta fino a 1000', false],
    ['spegne il computer', false],
    ['scrive 1000 nel Memo', false]]);

  una('15) Che cosa scrive nel Memo?\ns := 0;\nfor i := 1 to 4 do\n  s := s + i;\nMemo1.Lines.Add(IntToStr(s));', [
    ['10', true], ['4', false], ['1234', false], ['0', false]],
    3, 'Fai il conto passo per passo: s parte da 0 e ogni giro aggiunge i.');

  // ---------- PARTE 3: codice giusto o sbagliato ----------
  form.addSectionHeaderItem().setTitle('Parte 3 — Codice giusto o sbagliato');

  piu('16) Vogliamo scrivere nel Memo i numeri da 1 a 5. Quali pezzi di codice FUNZIONANO?', [
    ['for i := 1 to 5 do\n  Memo1.Lines.Add(IntToStr(i));', true],
    ['for i := 1 to 5 do\nbegin\n  Memo1.Lines.Add(IntToStr(i));\nend;', true],
    ['for i := 1 to 5 do\n  Memo1.Lines.Add(i);', false],
    ['for i := 1 to 5 do;\n  Memo1.Lines.Add(IntToStr(i));', false]],
    4, 'Guarda bene: IntToStr, il punto e virgola dopo do, begin/end.');

  piu('17) Quali sono ERRORI in questo codice?\nfor x = 1 to 10\n  Memo1.Lines.Add(x);', [
    ['manca  :=  (si scrive  x := 1)', true],
    ['manca  do  alla fine della prima riga', true],
    ['manca  IntToStr  (il Memo vuole un testo)', true],
    ['10 è troppo grande per un ciclo', false]], 4);

  una('18) Questo codice dovrebbe scrivere nel Memo la tabellina del 3 (3, 6, 9 … 30), ma scrive solo 30. Perché?\nfor i := 1 to 10 do\n  r := 3 * i;\nMemo1.Lines.Add(IntToStr(r));', [
    ['manca begin … end: dentro il ciclo c\'è solo  r := 3 * i , la riga del Memo viene eseguita una volta sola alla fine', true],
    ['manca sleep', false],
    ['la tabellina del 3 non si può fare con il FOR', false],
    ['bisogna scrivere  to 30', false]], 3);

  piu('19) Vogliamo il conto alla rovescia da 10 a 1. Quali righe vanno bene?', [
    ['for i := 10 downto 1 do', true],
    ['for i := 1 to 10 do  e nel Memo si scrive  IntToStr(11 - i)', true],
    ['for i := 10 to 1 do', false],
    ['for i := -10 to 1 do', false]], 4, 'Ci sono due strade giuste.');

  piu('20) Nel Contatore l\'utente scrive i numeri negli Edit. Che cosa serve per usarli nel FOR?', [
    ['StrToInt(Edit1.Text)', true],
    ['StrToInt(Edit2.Text)', true],
    ['Edit1.Text da solo, senza StrToInt', false],
    ['IntToStr(Edit1.Text)', false]], 3);

  // ---------- PARTE 4: scrivi tu il codice ----------
  form.addSectionHeaderItem().setTitle('Parte 4 — Scrivi tu il codice')
    .setHelpText('Scrivi solo le righe del ciclo (non serve tutto il programma). Puoi provarlo in Lazarus e incollarlo qui.');

  scrivi('21) Scrivi il ciclo FOR che mette nel Memo i numeri da 1 a 20.',
         'Esempio di come comincia: for i := …');
  scrivi('22) Scrivi il ciclo che mette nel Memo la tabellina del numero scritto in Edit1, da 1 a 10, così: 7 x 1 = 7',
         'Ti servono StrToInt(Edit1.Text), IntToStr e il simbolo + per unire i testi.');
  scrivi('23) Scrivi il ciclo che mette nel Memo SOLO i numeri pari da 2 a 20.',
         'Ci sono almeno due modi: moltiplicare il contatore per 2, oppure usare un IF con  mod 2 = 0 .');
  scrivi('24) Scrivi il codice che somma i numeri da 1 a 100 e scrive il risultato nel Memo (deve venire 5050).',
         'Serve una variabile in più, che parte da 0 prima del ciclo.');

  form.addParagraphTextItem().setTitle('25) Con parole tue: che differenza c\'è tra  to  e  downto ? Fai un esempio.')
    .setRequired(true);

  Logger.log('Link per i ragazzi: ' + form.getPublishedUrl());
  Logger.log('Link per modificare: ' + form.getEditUrl());
}
