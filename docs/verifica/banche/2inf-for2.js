// 2INF · Lazarus: il ciclo FOR, seconda parte (19/10/2026). Riparte dalla lezione del 15/10 (banca 2inf-for):
// ripasso corto, la pratica «da … a …» passo per passo con i punti di controllo, verifica (con il proprio codice incollato) e recupero.
// Aree e peso nel giudizio: concetti 40%, il tuo programma (saperlo spiegare) 40%, la pratica fatta 20%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">' + t + '</pre>'; }
  var CODICE = "var giro, inizio, fine: integer;\nbegin\n  inizio := StrToInt(Edit1.Text);\n  fine := StrToInt(Edit2.Text);\n  Memo1.Clear;\n  for giro := inizio to fine do\n  begin\n    Memo1.Lines.Add(IntToStr(giro));\n  end;\nend;";

  window.BANCA = {
    id: "2inf-for2-v1",
    classe: "2INF",
    titolo: "Il ciclo FOR, seconda parte: la tua app funziona",
    sotto: "2INF · 19/10/2026 · Lazarus · ripasso, pratica, verifica e recupero",
    stato: "stato/2inf-for2.json",
    risultati: "risultati.html?b=2inf-for2",
    minuti: 35,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: il ciclo for, il contatore, begin/end, IntToStr, StrToInt", peso: 40 },
      programma: { nome: "Il tuo programma: saperlo spiegare (solo parole tue)", peso: 40 },
      pratica: { nome: "La pratica in Lazarus", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO (corto: è la seconda volta) ---------- */
    schede_temi: { ciclo: 1, contatore: 1, giri: 2, inttostr: 2, strtoint: 3, memo: 3, errori: 4, ui: 5, pratica: 6 },
    schede: [
      { titolo: "1. Giovedì: il ciclo for in una riga", testo: "Giovedì abbiamo visto il <b>ciclo for</b>: fa ripetere al computer la stessa cosa tante volte. Alla lavagna:" + K("for x := 1 to 10 do\nbegin\n  writeln('CIAO');\nend;") + "Si legge: <b>per</b> x che va <b>da 1 a 10, fai</b> quello che c'è tra <b>begin</b> ed <b>end</b>. <b>x</b> è il <b>contatore</b>: una variabile <b>intera</b> (<code>integer</code>), dichiarata prima con <code>var x: integer;</code>, che a ogni giro aumenta di 1. <b>:=</b> dà il valore di partenza, <b>to</b> dice dove arriva, <b>do</b> vuol dire «fai».<br>Oggi lo scopo è uno: <b>la tua app «da … a …» funziona</b> e la sai spiegare. Giovedì l'hanno finita in 7 su 20: oggi tutti." },
      { titolo: "2. Quanti giri, e il numero nel Memo", testo: K("for giro := 7 to 12 do\nbegin\n  Memo1.Lines.Add(IntToStr(giro));\nend;") + "I giri si contano <b>fine − inizio + 1</b>: 12 − 7 + 1 = <b>6</b> giri, e nel Memo compaiono 7, 8, 9, 10, 11, 12, uno per riga.<br>In un programma con il form, <b>writeln</b> non si vede: si scrive nel <b>Memo</b> con <b>Memo1.Lines.Add</b> («al Memo1, alle sue righe, aggiungi»). Il Memo vuole <b>testo</b>, quindi il numero del giro passa da <b>IntToStr</b> (Int = intero, Str = testo). Per attaccare un testo al numero si usa il <b>+</b>: <code>IntToStr(giro) + ' - CIAO'</code>." },
      { titolo: "3. Le caselle: StrToInt e Memo1.Clear", testo: "Nell'app «da … a …» i numeri di partenza e di arrivo li scrive chi usa il programma, in due caselle <b>TEdit</b>. Il testo della casella diventa numero con <b>StrToInt</b> (il contrario di IntToStr):" + K("inizio := StrToInt(Edit1.Text);\nfine := StrToInt(Edit2.Text);") + "<b>Memo1.Clear</b> svuota il Memo prima di ricominciare, così a ogni clic non si accumulano le righe vecchie.<br>Quando i numeri sono tanti (da 1 a 100) non ci stanno: con <b>ScrollBars = ssBoth</b> nel Memo compaiono le <b>barre di scorrimento</b>." },
      { titolo: "4. Gli errori di giovedì (sono normali, ma oggi li evitiamo)", testo: "1) <b>Identifier not found</b> sul contatore: manca <code>var giro: integer;</code> sopra il begin del bottone.<br>2) Il <b>punto e virgola dopo do</b>: <code>for giro := 1 to 10 do;</code> ripete 10 volte… niente.<br>3) <b>begin</b> senza <b>end;</b>: non compila. Conta i begin e gli end: devono essere pari.<br>4) <code>Memo1.Lines.Add(giro)</code> senza <b>IntToStr</b>: errore, il Memo vuole testo.<br>5) Casella vuota e premi il bottone: StrToInt di niente dà errore. Scrivi prima i due numeri.<br>6) I <b>rientri</b> (regola del prof): begin ed end sullo stesso rientro, quello che sta dentro 2 spazi più a destra. In Lazarus selezioni le righe e premi <b>Ctrl+Shift+I</b> (a destra) o <b>Ctrl+Shift+U</b> (a sinistra). Codice tutto a sinistra = codice che nessuno legge: in un'azienda non passa." },
      { titolo: "5. Il programma intero (quello che oggi fai girare)", testo: "L'interfaccia: in alto <b>da</b> [ 5 ] <b>a</b> [ 12 ], al centro un Memo grande, in basso un bottone <b>Conta!</b>. Il codice del bottone, con i rientri giusti:" + K(CODICE) + "Leggilo riga per riga: dichiaro tre variabili intere; prendo i due numeri dalle caselle; pulisco il Memo; per giro da inizio a fine, aggiungo al Memo il numero del giro come testo. Fine." },
      { titolo: "6. LA PRATICA, passi 1-5: il form", testo: "Un passo alla volta. Ogni passo è una cosa sola.<br>1) Apri Lazarus: <b>Progetto → Nuovo progetto → Applicazione → Ok</b>. (Se hai il progetto di giovedì, aprilo e vai al passo 7.)<br>2) Dalla scheda <b>Standard</b> metti sul form un <b>TLabel</b>; nell'Ispettore oggetti la sua <b>Caption</b> diventa <b>da</b>.<br>3) Metti accanto un <b>TEdit</b> (Edit1) e cancella il contenuto della proprietà <b>Text</b>.<br>4) Metti un altro <b>TLabel</b> con Caption <b>a</b>, e accanto un altro <b>TEdit</b> (Edit2) con Text vuoto.<br>5) Metti al centro un <b>TMemo</b> grande; nell'Ispettore metti <b>ScrollBars</b> a <b>ssBoth</b>. Metti in basso un <b>TButton</b> con Caption <b>Conta!</b>.<br>Rispondi alla domanda qui sotto: così il monitor sa che sei a questo punto." },
      { titolo: "7. LA PRATICA, passi 6-9: il codice e la prova", testo: "6) Fai <b>doppio clic</b> sul bottone: si apre <code>procedure TForm1.Button1Click</code>.<br>7) Scrivi il codice della scheda 5, riga per riga, <b>con i rientri di 2 spazi</b>. La riga <code>var giro, inizio, fine: integer;</code> va <b>sopra</b> il begin della procedura.<br>8) Premi <b>F9</b>. Se Lazarus segna un errore in rosso, leggi la riga: quasi sempre è uno dei 6 errori della scheda 4.<br>9) Scrivi 5 e 12 nelle caselle, premi <b>Conta!</b>: compaiono i numeri da 5 a 12. <b>FATTO!</b> Prova anche da 1 a 100 e usa la barra di scorrimento.<br>Rispondi alla domanda qui sotto." },
      { titolo: "8. LA PRATICA, passi 10-12: fallo tuo, e la sfida", testo: "10) <b>Fallo tuo</b>: accanto al numero metti una frase tua, per esempio <code>IntToStr(giro) + ' - forza!'</code>; cambia la <b>Caption del form</b> (il titolo della finestra) con un nome tuo.<br>11) <b>Tieni pronto il codice per la verifica</b>: nella finestra del codice seleziona dalla riga <code>var</code> fino all'ultimo <code>end;</code> del bottone e premi <b>Ctrl+C</b>. Nella verifica c'è una domanda dove lo incolli (lì l'incolla è permesso; nelle altre no).<br>12) <b>Sfida</b> per chi ha finito: una terza casella con un numero, e nel Memo la sua tabellina: <code>IntToStr(giro) + ' x 7 = ' + IntToStr(giro * 7)</code>, con il 7 preso dalla terza casella. Sfida 2: un bottone <b>Pulisci</b> che fa solo <code>Memo1.Clear;</code>.<br>Ti blocchi? Scrivi la domanda all'assistente, in fondo alla pagina: ti risponde." }
    ],
    strumenti: [{ t: 'Il monitor della lezione', u: '../2inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "<code>for x := 1 to 10 do</code> ripete quello che c'è tra begin ed end…", ["10 volte", "1 volta", "per sempre"], "Da 1 a 10: 10 giri."),
    prepara: [
      { q: "Racconta con parole tue che cosa fa un ciclo for, come lo spiegheresti a un amico che non sa programmare.", min: 20 },
      { q: "Giovedì a che punto eri arrivato con l'app «da … a …»? Che cosa ti mancava?", min: 10 }
    ],
    allenamento: [
      S(1, C("concetti", "Nel for, il contatore deve essere una variabile…", ["intera (integer)", "di testo (string)", "con la virgola"], "Conta i giri: 1, 2, 3…")),
      S(1, C("concetti", "Che cosa fa <code>:=</code> nella riga del for?", ["dà al contatore il valore di partenza", "confronta due numeri", "chiude il ciclo"], "Come sempre in Pascal.")),
      S(2, C("concetti", "Quante volte gira <code>for giro := 7 to 12 do</code>?", ["6", "5", "12"], "12 − 7 + 1 = 6.")),
      S(2, C("concetti", "<code>IntToStr(giro)</code> serve a…", ["trasformare il numero in testo", "trasformare il testo in numero", "contare i giri"], "Int = intero, Str = testo.")),
      S(3, C("concetti", "Per leggere il numero scritto in Edit1 si usa…", ["StrToInt(Edit1.Text)", "IntToStr(Edit1.Text)", "Edit1.Caption"], "Testo → numero: StrToInt.")),
      S(3, C("concetti", "<code>Memo1.Clear</code> serve a…", ["svuotare il Memo prima di ricominciare", "chiudere il programma", "contare le righe"], "Così le righe vecchie non si accumulano.")),
      S(4, C("concetti", "Lazarus dice «Identifier not found: giro». Che cosa manca?", ["var giro: integer; sopra il begin", "un end in più", "un bottone"], "Il contatore va dichiarato.")),
      S(4, C("concetti", "<code>for giro := 1 to 10 do;</code> con il punto e virgola dopo do…", ["ripete 10 volte niente", "funziona uguale", "ripete 11 volte"], "Il ; chiude il ciclo subito.")),
      S(5, C("concetti", "Con da 5 a 12 nelle caselle, quante righe compaiono nel Memo?", ["8", "7", "12"], "12 − 5 + 1 = 8.")),
      S(6, C("pratica", "Passi 1-5 fatti? Sul tuo form adesso ci sono…", ["2 Label, 2 Edit, 1 Memo, 1 Button", "solo un bottone", "niente, non ho ancora aperto Lazarus"], "Se manca qualcosa, torna al passo che manca.")),
      S(7, C("pratica", "Passi 6-9 fatti? Premendo Conta! con 5 e 12…", ["compaiono i numeri da 5 a 12 nel Memo", "Lazarus dà un errore rosso", "non succede niente"], "Errore rosso: scheda 4. Niente: hai scritto i numeri nelle caselle?")),
      S(8, C("pratica", "Passi 10-12: che cosa hai fatto?", ["l'ho fatto mio (frase e titolo) e ho copiato il codice", "anche la sfida della tabellina", "sono ancora ai passi 6-9"], "Tutte le risposte vanno bene: serve al monitor."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("concetti", "<code>for i := 1 to 5 do Memo1.Lines.Add('OK');</code> quante righe scrive?", ["5", "1", "6"], "", "giri"),
      C("concetti", "<code>for i := 3 to 8 do</code> quanti giri fa?", ["6", "5", "8"], "8 − 3 + 1 = 6", "giri"),
      C("concetti", "Il contatore del for si dichiara…", ["con var, sopra il begin, come integer", "non si dichiara mai", "nella Caption del bottone"], "", "contatore"),
      C("concetti", "<code>Memo1.Lines.Add(IntToStr(i));</code> con i da 1 a 3 scrive…", ["1, 2, 3, uno per riga", "i, i, i", "123 su una riga sola"], "", "inttostr"),
      C("concetti", "Tra begin ed end del for ci va…", ["quello che si deve ripetere a ogni giro", "la dichiarazione delle variabili", "il nome del form"], "", "ciclo"),
      C("concetti", "<code>inizio := StrToInt(Edit1.Text);</code> serve a…", ["prendere il numero scritto nella casella", "scrivere un numero nella casella", "pulire la casella"], "", "strtoint"),
      C("concetti", "<code>Memo1.Lines.Add(i);</code> senza IntToStr…", ["dà errore, perché il Memo vuole testo", "scrive il numero lo stesso", "scrive la lettera i"], "", "inttostr"),
      C("concetti", "Perché le righe dentro il ciclo si spostano a destra di 2 spazi?", ["per vedere subito che cosa si ripete: il codice si legge", "perché se no Lazarus non compila", "per far andare il programma più veloce"], "", "errori"),
      C("concetti", "Premo Conta! con le caselle vuote e il programma dà errore. Perché?", ["StrToInt non può trasformare un testo vuoto in numero", "il Memo è troppo piccolo", "manca il bottone"], "", "strtoint"),
      C("concetti", "<code>IntToStr(giro * 7)</code> con giro = 3 dà…", ["il testo 21", "il numero 37", "il testo giro*7"], "", "inttostr")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di scrivere un ciclo for da solo?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto sei fiero della tua app «da … a …»?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "pratica", incolla: true, q: "Incolla qui il codice del tuo bottone Conta! (dalla riga var fino all'ultimo end;). Qui l'incolla è permesso.", aiuto: "Nella finestra del codice di Lazarus: seleziona, Ctrl+C, poi qui Ctrl+V. Se non ce l'hai, scrivi: non fatto, e il motivo.", min_parole: 5,
        criteri: "codice vero del ragazzo: var con integer, StrToInt dalle caselle, Memo1.Clear, for … to … do, begin/end, Memo1.Lines.Add(IntToStr(...)); rientri" },
      { area: "programma", tema: "ciclo", q: "Spiega con parole tue il codice che hai incollato, riga per riga: che cosa fa var, che cosa fanno le due StrToInt, Memo1.Clear, il for, e che cosa c'è tra begin ed end.", aiuto: "Almeno 30 parole. Scrivi tu, senza copiare.", min_parole: 30,
        criteri: "dichiara le variabili intere; prende i numeri dalle caselle; pulisce il Memo; ripete da inizio a fine; aggiunge il numero come testo; parole sue" },
      { area: "concetti", tema: "giri", q: "Nelle caselle scrivo da 20 a 25. Quante righe compaiono nel Memo e quali? Se scrivessi da 25 a 20, che cosa succede secondo te?", aiuto: "Almeno 15 parole.", min_parole: 15,
        criteri: "6 righe: 20, 21, 22, 23, 24, 25; da 25 a 20 il for non fa nessun giro (il Memo resta vuoto)" },
      { area: "pratica", tema: "errori", q: "Racconta un errore che hai fatto oggi o giovedì (o un compagno) e come l'avete risolto.", aiuto: "Almeno 20 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 20,
        criteri: "errore concreto (var mancante, ; dopo do, IntToStr, begin/end, casella vuota); come l'ha risolto" },
      { area: "pratica", tema: "pratica", q: "Che cosa hai cambiato per fare tua l'app (la frase, il titolo)? Se hai fatto la sfida della tabellina o del bottone Pulisci, raccontala.", aiuto: "Almeno 12 parole.", min_parole: 12,
        criteri: "scelta personale vera; eventuale sfida descritta con il codice giusto (giro * n, Memo1.Clear)" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("concetti", "<code>for i := 1 to 4 do</code> quanti giri fa?", ["4", "3", "5"], "", "giri"),
      C("concetti", "<code>for i := 10 to 15 do</code> quanti giri fa?", ["6", "5", "15"], "15 − 10 + 1", "giri"),
      C("concetti", "Il contatore del for è…", ["una variabile intera che aumenta di 1 a ogni giro", "un bottone", "un testo fisso"], "", "contatore"),
      C("concetti", "Per mettere il numero del giro nel Memo si scrive…", ["Memo1.Lines.Add(IntToStr(i))", "Memo1.Lines.Add(i)", "writeln(Memo1)"], "", "inttostr"),
      C("concetti", "Il ciclo for serve quando…", ["sai quante volte ripetere", "non vuoi ripetere niente", "vuoi chiudere il programma"], "", "ciclo"),
      C("concetti", "Dopo <code>do</code> il punto e virgola…", ["non ci va", "ci va sempre", "ci vanno due punti e virgola"], "", "errori"),
      C("concetti", "StrToInt e IntToStr: che differenza c'è?", ["StrToInt: testo → numero; IntToStr: numero → testo", "sono uguali", "StrToInt scrive nel Memo"], "", "strtoint"),
      C("concetti", "<code>Memo1.Clear;</code> serve a…", ["svuotare il Memo", "chiudere Lazarus", "aggiungere una riga"], "", "memo"),
      C("concetti", "Per far partire il programma in Lazarus premo…", ["F9", "F1", "Ctrl+C"], "", "ui")
    ]
  };
})();
