// 2INF · Lazarus: il ciclo FOR (15/10/2026). Teoria dalla lavagna del prof, pratica in Lazarus, verifica, recupero.
// Aree e peso nel giudizio: concetti 40%, il tuo programma (saperlo spiegare) 40%, la pratica fatta 20%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">' + t + '</pre>'; }

  window.BANCA = {
    id: "2inf-for-v1",
    classe: "2INF",
    titolo: "Il ciclo FOR: il computer ripete per te",
    sotto: "2INF · 15/10/2026 · Lazarus · teoria, pratica, verifica e recupero",
    stato: "stato/2inf-for.json",
    risultati: "risultati.html?b=2inf-for",
    minuti: 40,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: il ciclo for, il contatore, begin/end, IntToStr", peso: 40 },
      programma: { nome: "Il tuo programma: saperlo spiegare (solo parole tue)", peso: 40 },
      pratica: { nome: "La pratica in Lazarus", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. TEORIA (la lavagna del prof) ---------- */
    schede_temi: { ciclo: 1, contatore: 2, giri: 3, inttostr: 3, memo: 4, errori: 5, strtoint: 6, ui: 6, pratica: 7 },
    schede: [
      { titolo: "1. Che cos'è un ciclo", testo: "Un <b>ciclo</b> fa ripetere al computer la stessa cosa tante volte, senza riscriverla. Per scrivere CIAO 10 volte, senza ciclo servono 10 righe uguali; con il ciclo <b>for</b> ne bastano 3. In Lazarus finora il programma <b>reagiva</b> a un clic e faceva una cosa sola; con il for, dentro lo stesso clic, il programma <b>ripete</b>." },
      { titolo: "2. La lavagna: FOR X := 1 TO 10 DO", testo: K("for x := 1 to 10 do\nbegin\n   writeln('CIAO');\nend;") + "Si legge così: <b>per</b> x che va <b>da 1 a 10, fai</b> quello che c'è tra <b>begin</b> ed <b>end</b>.<br><b>x</b> è il <b>contatore</b>: una variabile <b>intera</b> (<code>integer</code>) che a ogni giro aumenta di 1. Va dichiarata prima, come tutte le variabili: <code>var x: integer;</code><br><b>:=</b> dà il valore di partenza (come sempre in Pascal). <b>to</b> dice dove arriva. <b>do</b> vuol dire «fai».<br><b>writeln</b> scrive e va a capo (<b>ln</b> = line, riga); <b>write</b> invece scrive e resta sulla stessa riga." },
      { titolo: "3. Il contatore cambia a ogni giro", testo: K("for giro := 7 to 12 do\nbegin\n   writeln(IntToStr(giro));\nend;") + "Il nome del contatore lo scegli tu: alla lavagna il prof ha usato il nome di un compagno. Qui si chiama <b>giro</b>.<br>Il ciclo parte da 7 e arriva a 12: scrive <b>7, 8, 9, 10, 11, 12</b>, uno per riga. I giri sono <b>6</b>: si contano così, <b>fine − inizio + 1</b> (12 − 7 + 1 = 6).<br><b>IntToStr</b> trasforma un numero intero in testo (Int = intero, Str = stringa, testo), come facevate nella calcolatrice per mettere un numero nella Caption." },
      { titolo: "4. In Lazarus, con il form: si scrive nel Memo", testo: "Alla lavagna c'è <b>writeln</b>, che scrive in una finestra di solo testo. In un programma con il <b>form</b> (bottoni e caselle) writeln non si vede: si usa un <b>Memo</b> (TMemo, una casella di testo con tante righe). Ogni giro aggiunge una riga:" + K("for giro := 1 to 10 do\nbegin\n   Memo1.Lines.Add('CIAO');\nend;") + "<b>Memo1.Lines.Add</b> = «al Memo1, alle sue righe, aggiungi». Con il numero del giro:" + K("Memo1.Lines.Add(IntToStr(giro) + ' - CIAO');") + "Il <b>+</b> tra due testi li attacca uno all'altro." },
      { titolo: "5. Gli errori di tutti (anche dei programmatori veri)", testo: "1) Il contatore <b>non dichiarato</b>: manca <code>var giro: integer;</code> sopra il begin del bottone. Lazarus dice «Identifier not found».<br>2) Il <b>punto e virgola dopo do</b>: <code>for giro := 1 to 10 do;</code> ripete 10 volte… niente, e la riga sotto la fa una volta sola.<br>3) <b>begin</b> senza <b>end;</b>: Lazarus non compila.<br>4) Il numero nel Memo <b>senza IntToStr</b>: errore, perché il Memo vuole testo.<br>5) I <b>rientri</b>: quello che sta dentro il ciclo si sposta a destra di 3 spazi, così si vede subito che cosa si ripete." },
      { titolo: "6. Il programma della lavagna: da … a …", testo: "L'<b>interfaccia</b> (UI, quello che si vede) disegnata alla lavagna: in alto <b>da</b> [ 5 ] <b>a</b> [ 12 ], al centro un Memo grande, in basso un bottone. Premi il bottone e nel Memo compaiono i numeri da 5 a 12, uno per riga.<br>I componenti: <b>TLabel</b> per le scritte «da» e «a», <b>TEdit</b> per le due caselle dei numeri, <b>TMemo</b> per l'elenco, <b>TButton</b> per partire. Nel Memo la proprietà <b>ScrollBars</b> va messa a <b>ssBoth</b>: compaiono le barre per scorrere quando i numeri sono tanti.<br>Il codice del bottone:" + K("var giro, inizio, fine: integer;\nbegin\n   inizio := StrToInt(Edit1.Text);\n   fine := StrToInt(Edit2.Text);\n   Memo1.Clear;\n   for giro := inizio to fine do\n   begin\n      Memo1.Lines.Add(IntToStr(giro));\n   end;\nend;") + "<b>StrToInt</b> fa il contrario di IntToStr: trasforma il testo della casella in un numero. <b>Memo1.Clear</b> pulisce il Memo prima di ricominciare." },
      { titolo: "7. LA PRATICA: il tuo «da … a …» in Lazarus", testo: "Un passo alla volta, in Lazarus. Ogni passo è una cosa sola.<br>1) Apri Lazarus e scegli <b>Progetto → Nuovo progetto → Applicazione</b>, poi <b>Ok</b>.<br>2) Dalla scheda <b>Standard</b> metti sul form un <b>TLabel</b>; nell'Ispettore la sua <b>Caption</b> diventa <b>da</b>.<br>3) Metti accanto un <b>TEdit</b> (Edit1) e cancella il testo della proprietà <b>Text</b>.<br>4) Metti un altro <b>TLabel</b> con Caption <b>a</b>.<br>5) Metti accanto un altro <b>TEdit</b> (Edit2), con Text vuoto.<br>6) Metti al centro un <b>TMemo</b> grande; nell'Ispettore metti <b>ScrollBars</b> a <b>ssBoth</b>.<br>7) Metti in basso un <b>TButton</b> con Caption <b>Conta!</b><br>8) Fai <b>doppio clic</b> sul bottone: si apre <code>Button1Click</code>.<br>9) Scrivi il codice della scheda 6, riga per riga, con i rientri.<br>10) Premi <b>F9</b>, scrivi 5 e 12 nelle caselle, premi <b>Conta!</b>: compaiono i numeri da 5 a 12. <b>FATTO!</b><br>11) <b>Fallo tuo</b>: accanto al numero metti una frase tua, per esempio <code>IntToStr(giro) + ' - forza!'</code>, e cambia il titolo del form (Caption del form) con un nome tuo.<br>12) <b>Sfida</b>: una terza casella con un numero e nel Memo la sua tabellina: <code>IntToStr(giro) + ' x 7 = ' + IntToStr(giro * 7)</code><br>Ti blocchi? Scrivi la domanda all'assistente, qui sotto: ti risponde." }
    ],
    strumenti: [{ t: 'Il monitor della lezione', u: 'https://nicolaregge-pulse.github.io/corso-informatica/2inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "<code>for x := 1 to 10 do</code> ripete quello che c'è tra begin ed end…", ["10 volte", "1 volta", "per sempre"], "Da 1 a 10: 10 giri."),
    prepara: [
      { q: "Racconta con parole tue che cosa fa un ciclo for, come lo spiegheresti a un amico che non sa programmare.", min: 20 },
      { q: "Nel tuo programma in Lazarus, che cosa hai scelto di far ripetere e quante volte?", min: 12 }
    ],
    allenamento: [
      S(1, C("concetti", "Un ciclo serve a…", ["far ripetere al computer la stessa cosa tante volte", "cancellare il programma", "aprire una finestra nuova"], "Ripetere senza riscrivere.")),
      S(2, C("concetti", "Nel for, il contatore deve essere una variabile…", ["intera (integer)", "di testo (string)", "con la virgola"], "Conta i giri: 1, 2, 3…")),
      S(2, C("concetti", "<code>writeln</code> e <code>write</code>: che differenza c'è?", ["writeln va a capo dopo aver scritto, write no", "write va a capo, writeln no", "nessuna"], "ln = line, riga.")),
      S(3, C("concetti", "Quante volte gira <code>for giro := 7 to 12 do</code>?", ["6", "5", "12"], "12 − 7 + 1 = 6.")),
      S(3, C("concetti", "<code>IntToStr(giro)</code> serve a…", ["trasformare il numero in testo", "trasformare il testo in numero", "contare i giri"], "Int = intero, Str = testo.")),
      S(4, C("concetti", "In un programma con il form, per scrivere una riga a ogni giro si usa…", ["Memo1.Lines.Add(...)", "writeln(...)", "Button1.Caption"], "writeln nel form non si vede.")),
      S(5, C("concetti", "<code>for giro := 1 to 10 do;</code> con il punto e virgola dopo do…", ["ripete 10 volte niente, e la riga dopo la fa una volta", "funziona uguale", "ripete 11 volte"], "Il ; chiude il ciclo subito.")),
      S(6, C("concetti", "Per leggere il numero che il ragazzo scrive in Edit1 si usa…", ["StrToInt(Edit1.Text)", "IntToStr(Edit1.Text)", "Edit1.Caption"], "Testo → numero: StrToInt.")),
      S(6, C("concetti", "Con da 5 a 12 nelle caselle, quante righe compaiono nel Memo?", ["8", "7", "12"], "12 − 5 + 1 = 8.")),
      S(5, C("concetti", "Lazarus dice «Identifier not found» sul contatore. Che cosa manca?", ["var giro: integer; sopra il begin", "un end in più", "un bottone"], "Il contatore va dichiarato."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("concetti", "<code>for i := 1 to 5 do Memo1.Lines.Add('OK');</code> quante righe scrive?", ["5", "1", "6"], "", "giri"),
      C("concetti", "<code>for i := 3 to 8 do</code> quanti giri fa?", ["6", "5", "8"], "8 − 3 + 1 = 6", "giri"),
      C("concetti", "Il contatore del for si dichiara…", ["con var, sopra il begin, come integer", "non si dichiara mai", "nella Caption del bottone"], "", "contatore"),
      C("concetti", "<code>Memo1.Lines.Add(IntToStr(i));</code> con i da 1 a 3 scrive…", ["1, 2, 3, uno per riga", "i, i, i", "123 su una riga sola"], "", "inttostr"),
      C("concetti", "Che cosa fa <code>:=</code> nella riga del for?", ["dà al contatore il valore di partenza", "confronta due numeri", "chiude il ciclo"], "", "contatore"),
      C("concetti", "Tra begin ed end del for ci va…", ["quello che si deve ripetere a ogni giro", "la dichiarazione delle variabili", "il nome del form"], "", "ciclo"),
      C("concetti", "Perché le righe dentro il ciclo si spostano a destra?", ["per vedere subito che cosa si ripete", "perché Lazarus lo vuole, se no non compila", "per far andare il programma più veloce"], "", "errori"),
      C("concetti", "<code>Memo1.Lines.Add(i);</code> senza IntToStr…", ["dà errore, perché il Memo vuole testo", "scrive il numero lo stesso", "scrive la lettera i"], "", "inttostr"),
      C("concetti", "<code>inizio := StrToInt(Edit1.Text);</code> serve a…", ["prendere il numero scritto nella casella", "scrivere un numero nella casella", "pulire la casella"], "", "strtoint"),
      C("concetti", "Nel Memo, ScrollBars = ssBoth…", ["fa comparire le barre per scorrere", "colora il Memo", "blocca il Memo"], "", "ui")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di scrivere un ciclo for da solo?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti è piaciuto fare il contatore in Lazarus?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "programma", tema: "ciclo", q: "Scrivi un ciclo for che mette nel Memo il tuo nome 5 volte. Poi spiega con parole tue che cosa fa ogni pezzo: for, il contatore, to, do, begin/end.", aiuto: "Almeno 30 parole. Scrivi tu, senza copiare.", min_parole: 30,
        criteri: "ciclo giusto da 1 a 5 con Memo1.Lines.Add e il nome; spiega contatore, partenza e arrivo, do, begin/end; parole sue" },
      { area: "concetti", tema: "giri", q: "<code>for giro := 7 to 12 do Memo1.Lines.Add(IntToStr(giro));</code> Quante righe compaiono nel Memo, e quali? Perché serve IntToStr?", aiuto: "Almeno 15 parole.", min_parole: 15,
        criteri: "6 righe: 7, 8, 9, 10, 11, 12; IntToStr trasforma il numero in testo perché il Memo vuole testo" },
      { area: "pratica", tema: "pratica", q: "Racconta il programma «da … a …» che hai fatto oggi in Lazarus: quali componenti hai messo, che cosa fa il bottone, che cosa hai cambiato per farlo tuo. Se hai fatto la sfida della tabellina, dillo.", aiuto: "Almeno 25 parole.", min_parole: 25,
        criteri: "programma vero: TLabel, TEdit, TMemo, TButton; StrToInt dalle caselle; ciclo; scelta personale; eventuale tabellina" },
      { area: "pratica", tema: "errori", q: "Racconta un errore che hai fatto oggi (o che ha fatto un compagno) e come l'avete risolto.", aiuto: "Almeno 20 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 20,
        criteri: "errore concreto (var mancante, ; dopo do, IntToStr, begin/end); come l'ha risolto" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("concetti", "<code>for i := 1 to 4 do</code> quanti giri fa?", ["4", "3", "5"], "", "giri"),
      C("concetti", "<code>for i := 10 to 15 do</code> quanti giri fa?", ["6", "5", "15"], "15 − 10 + 1", "giri"),
      C("concetti", "Il contatore del for è…", ["una variabile intera che aumenta di 1 a ogni giro", "un bottone", "un testo fisso"], "", "contatore"),
      C("concetti", "Per mettere il numero del giro nel Memo si scrive…", ["Memo1.Lines.Add(IntToStr(i))", "Memo1.Lines.Add(i)", "writeln(Memo1)"], "", "inttostr"),
      C("concetti", "Il ciclo for serve quando…", ["sai quante volte ripetere", "non vuoi ripetere niente", "vuoi chiudere il programma"], "", "ciclo"),
      C("concetti", "In un programma con il form, writeln…", ["non si vede: si usa il Memo", "scrive nella Caption", "apre una finestra nuova"], "", "memo"),
      C("concetti", "Dopo <code>do</code> il punto e virgola…", ["non ci va", "ci va sempre", "ci vanno due punti e virgola"], "", "errori"),
      C("concetti", "StrToInt e IntToStr: che differenza c'è?", ["StrToInt: testo → numero; IntToStr: numero → testo", "sono uguali", "StrToInt scrive nel Memo"], "", "strtoint"),
      C("concetti", "<code>IntToStr(giro * 7)</code> con giro = 3 dà…", ["il testo 21", "il numero 37", "il testo giro*7"], "", "inttostr")
    ]
  };
})();
