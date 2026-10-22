// 2INF · Lazarus: «Il mio salvadanaio» (22/10/2026). Mette insieme il FOR (15 e 19/10) e il WHILE (20/10) in un programma nuovo.
// Il ragazzo sceglie che cosa vuole comprare e quanto costa; il FOR conta una settimana di risparmi, il WHILE i giorni che servono.
// Sfida: la paghetta del sabato (mod 7). Durata reale: circa 2 ore di laboratorio (form 15', FOR 20', WHILE 25', settimane 10',
// sfida 20', domande ~30' a 1' l'una, spiegazione e consegna 10'). Aree: concetti 40%, programma (saperlo spiegare) 40%, pratica 20%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">' + t + '</pre>'; }
  function F(t) { return '<div style="background:#dafbe1;border:2px solid #1a7f37;border-radius:8px;padding:8px 12px;margin:8px 0;font-weight:700">FATTO! ' + t + '</div>'; }

  var INCIPIT_FOR = "procedure TForm1.Button1Click(Sender: TObject);\nvar giorno, euro, totale: integer;\nbegin\n  Randomize;\n  Memo1.Clear;\n  totale := 0;\n  // QUI il ciclo FOR: giorno da 1 a 7\n  //   QUI euro a caso da 1 a 5\n  //   QUI aggiungi euro al totale\n  //   QUI scrivi nel Memo: Giorno 1: +3 euro\n  // QUI, dopo il ciclo, scrivi il totale della settimana\nend;";
  var INCIPIT_WHILE = "procedure TForm1.Button2Click(Sender: TObject);\nvar giorni, euro, totale, prezzo: integer;\nbegin\n  Randomize;\n  prezzo := StrToInt(Edit2.Text);\n  Memo1.Clear;\n  totale := 0;\n  giorni := 0;\n  // QUI il ciclo WHILE: finché il totale è minore del prezzo\n  //   QUI euro a caso da 1 a 5\n  //   QUI aggiungi euro al totale\n  //   QUI conta un giorno in più\n  // QUI, dopo il ciclo, scrivi quanti giorni servono\nend;";

  window.BANCA = {
    id: "2inf-salvadanaio-v1",
    classe: "2INF",
    controllo: "../2inf-monitor/lazarus.json",
    titolo: "Il mio salvadanaio: FOR e WHILE insieme",
    sotto: "2INF · 22/10/2026 · Lazarus · un programma tuo con il FOR e il WHILE (circa 2 ore)",
    stato: "stato/2inf-salvadanaio.json",
    risultati: "risultati.html?b=2inf-salvadanaio",
    minuti: 120,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: for, while, condizione di uscita, contatore, Random, mod", peso: 40 },
      programma: { nome: "Il tuo programma: saperlo spiegare (solo parole tue)", peso: 40 },
      pratica: { nome: "La pratica in Lazarus", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO E PRATICA ---------- */
    schede_temi: { progetto: 1, differenza: 2, for: 2, while: 2, form: 3, somma: 4, random: 4, contatore: 5, uscita: 5, settimane: 6, mod: 7, errori: 8, pratica: 8 },
    schede: [
      { titolo: "1. Il mio salvadanaio: che cosa facciamo oggi", testo: "Oggi fai un programma <b>tuo</b>: un salvadanaio.<br>Tu scegli <b>che cosa vuoi comprare</b> (delle scarpe, una cuffia, un gioco) e <b>quanto costa</b>.<br>Ogni giorno metti nel salvadanaio da <b>1 a 5 euro</b>, a caso.<br>Il programma ha <b>tre bottoni</b>:<br>1) <b>Una settimana</b>: quanto risparmi in 7 giorni. Qui usi il <b>FOR</b>.<br>2) <b>Quanti giorni mi servono?</b>: quanti giorni servono per arrivare al prezzo. Qui usi il <b>WHILE</b>.<br>3) <b>Con la paghetta</b> (sfida): il sabato arrivano 10 euro in più.<br>Un pezzo alla volta. Ogni pezzo finisce con un <b>FATTO!</b> verde." },
      { titolo: "2. FOR o WHILE? Ripasso lampo", testo: "<b>FOR</b> = so <b>prima</b> quante volte. Una settimana ha sempre 7 giorni:" + K("for giorno := 1 to 7 do") + "<b>WHILE</b> = <b>non so</b> quante volte. Ripeto <b>finché</b> la condizione è vera:" + K("while totale &lt; prezzo do") + "Si legge: <b>finché</b> il totale è <b>minore</b> del prezzo, metto altri soldi.<br>Nel FOR il contatore aumenta <b>da solo</b>. Nel WHILE lo fai aumentare <b>tu</b>: <code>giorni := giorni + 1</code>.<br>Nel WHILE qualcosa deve cambiare la condizione, se no il ciclo <b>non finisce mai</b> (ciclo infinito: <b>Esegui → Ferma</b>, oppure <b>Ctrl+F2</b>)." },
      { titolo: "3. PEZZO 1: la Form (circa 15 minuti)", testo: "1) Apri Lazarus: <b>Progetto → Nuovo progetto → Applicazione → Ok</b>.<br>2) Metti un <b>TLabel</b>. Caption: <b>Che cosa vuoi comprare?</b><br>3) Accanto metti un <b>TEdit</b> (si chiama <b>Edit1</b>). Nella proprietà <b>Text</b> scrivi la cosa che vuoi tu, per esempio <b>scarpe</b>.<br>4) Sotto metti un altro <b>TLabel</b>. Caption: <b>Quanto costa (euro)?</b><br>5) Accanto metti un <b>TEdit</b> (<b>Edit2</b>). Text: il prezzo, per esempio <b>80</b>. Solo il numero, senza €.<br>6) Metti tre <b>TButton</b>, uno sotto l'altro. Caption: <b>Una settimana</b> (Button1), <b>Quanti giorni mi servono?</b> (Button2), <b>Con la paghetta</b> (Button3).<br>7) Metti un <b>TMemo</b> grande (Memo1). <b>ScrollBars = ssVertical</b>. Cancella le righe di <b>Lines</b>.<br>8) <b>Fallo tuo</b>: Caption del form = <b>Il salvadanaio di</b> e il tuo nome. Cambia il colore (Color) del form.<br>9) Premi <b>F9</b>: si apre la tua finestra." + F("La finestra si apre e vedi le due caselle, i tre bottoni e il Memo.") },
      { titolo: "4. PEZZO 2: il bottone «Una settimana», con il FOR (circa 20 minuti)", testo: "1) Chiudi la finestra. Fai <b>doppio clic</b> sul bottone <b>Una settimana</b>.<br>2) Lazarus scrive la procedura. Completala così: le righe con <code>// QUI</code> dicono che cosa scrivere al loro posto." + K(INCIPIT_FOR) + "<b>Indizi</b>, se ti servono:<br>Il ciclo: <code>for giorno := 1 to 7 do</code> poi <code>begin</code> … <code>end;</code><br>Il soldo del giorno: <code>euro := Random(5) + 1;</code> (da 1 a 5)<br>Nel salvadanaio: <code>totale := totale + euro;</code><br>La riga nel Memo: <code>Memo1.Lines.Add('Giorno ' + IntToStr(giorno) + ': +' + IntToStr(euro) + ' euro');</code><br>Il totale, <b>dopo</b> l'<code>end;</code> del ciclo: <code>Memo1.Lines.Add('In una settimana: ' + IntToStr(totale) + ' euro');</code><br>3) Premi <b>F9</b> e poi il bottone <b>Una settimana</b>, più volte." + F("Nel Memo vedi 7 righe, da Giorno 1 a Giorno 7, e sotto il totale. Ogni volta i numeri cambiano.") },
      { titolo: "5. PEZZO 3: il bottone «Quanti giorni mi servono?», con il WHILE (circa 25 minuti)", testo: "1) Doppio clic sul bottone <b>Quanti giorni mi servono?</b> e completa:" + K(INCIPIT_WHILE) + "<b>Indizi</b>:<br>Il ciclo: <code>while totale &lt; prezzo do</code> poi <code>begin</code> … <code>end;</code><br>Dentro: <code>euro := Random(5) + 1;</code> poi <code>totale := totale + euro;</code> poi <code>giorni := giorni + 1;</code><br>Se vuoi vedere i giorni nel Memo: <code>Memo1.Lines.Add('Giorno ' + IntToStr(giorni) + ': ho ' + IntToStr(totale) + ' euro');</code><br>Dopo il ciclo: <code>Memo1.Lines.Add('Per ' + Edit1.Text + ' ti servono ' + IntToStr(giorni) + ' giorni');</code><br><b>Perché si ferma?</b> Ogni giro il totale cresce. Quando arriva al prezzo (o lo supera), <code>totale &lt; prezzo</code> diventa <b>falso</b> e il ciclo finisce. Questa è la <b>condizione di uscita</b>.<br>2) F9, scrivi 80 nella casella del prezzo, premi il bottone." + F("Il Memo dice: Per scarpe ti servono … giorni (con la tua cosa e il tuo prezzo).") },
      { titolo: "6. PEZZO 4: quante settimane? (circa 10 minuti)", testo: "In Pascal ci sono due operazioni per le divisioni <b>senza virgola</b>:<br><b>div</b> = quante volte ci sta. <code>23 div 7</code> = <b>3</b> (3 settimane intere).<br><b>mod</b> = quanto avanza. <code>23 mod 7</code> = <b>2</b> (avanzano 2 giorni).<br>Aggiungi alla fine del bottone <b>Quanti giorni mi servono?</b>, dopo l'altra riga:" + K("Memo1.Lines.Add('Cioè ' + IntToStr(giorni div 7) + ' settimane e ' + IntToStr(giorni mod 7) + ' giorni');") + "Prova con un prezzo grande, per esempio <b>150</b>." + F("Il Memo dice anche: Cioè … settimane e … giorni.") },
      { titolo: "7. SFIDA: il bottone «Con la paghetta» (circa 20 minuti)", testo: "Il <b>sabato</b> arriva la paghetta: <b>10 euro in più</b>. Facciamo finta che il giorno 7, il 14, il 21… siano i sabati.<br>Come si riconosce? Il giorno è un sabato quando <code>giorni mod 7 = 0</code> (7, 14, 21 divisi per 7 non hanno resto).<br>1) Doppio clic sul bottone <b>Con la paghetta</b>.<br>2) Copia dentro tutto il codice del bottone «Quanti giorni mi servono?» (le var e le righe tra begin ed end).<br>3) Dentro il while, <b>dopo</b> <code>giorni := giorni + 1;</code>, aggiungi:" + K("if giorni mod 7 = 0 then\nbegin\n  totale := totale + 10;\n  Memo1.Lines.Add('Sabato: paghetta +10 euro!');\nend;") + "4) F9 e premi i due bottoni con lo stesso prezzo. Con la paghetta servono <b>meno giorni</b>?" + F("Nel Memo compare «Sabato: paghetta +10 euro!» e i giorni sono meno di prima.") },
      { titolo: "8. Errori tipici e la consegna", testo: "<b>Errori tipici</b> (succede a tutti, anche ai pro):<br>1) <b>Identifier not found</b>: manca la variabile nella riga <code>var</code>.<br>2) Il totale è sempre 0 o sbagliato: manca <code>totale := 0;</code> prima del ciclo, o <code>totale := totale + euro;</code> dentro.<br>3) Dice sempre 0 giorni: manca <code>giorni := giorni + 1;</code>.<br>4) Il programma si blocca: ciclo infinito. Il totale non cresce dentro il while. <b>Esegui → Ferma</b> e controlla.<br>5) Errore quando premi il bottone: la casella del prezzo è vuota o ha lettere (o il simbolo €). Scrivi solo il numero.<br>6) Il totale della settimana compare 7 volte: la riga del totale è <b>dentro</b> il ciclo. Spostala dopo l'<code>end;</code>.<br><b>La consegna</b>: nella verifica c'è una domanda dove incolli <b>tutto il tuo codice</b>. In Lazarus, nella finestra del codice, seleziona dalla prima <code>procedure TForm1.Button1Click</code> fino all'ultimo <code>end;</code> dei bottoni e premi <b>Ctrl+C</b>. Poi nella domanda premi <b>Ctrl+V</b>. Poi scrivi con parole tue che cosa fa." + F("Hai il codice copiato e sai dire a voce che cosa fa ogni bottone.") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../2inf-oggi/', c: '#1f7a3f' }, { t: 'Il monitor della lezione', u: '../2inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "Una settimana ha sempre 7 giorni. Per contare i risparmi di una settimana uso…", ["il FOR, da 1 a 7", "il WHILE", "un IF"], "So prima quante volte: 7. Allora FOR."),
    prepara: [
      { q: "Che cosa vorresti comprare con i tuoi risparmi, e quanto costa più o meno? Scrivilo: lo userai nel programma.", min: 5 }
    ],
    allenamento: [
      S(1, C("pratica", "Nel salvadanaio, quanti euro metti ogni giorno?", ["da 1 a 5, a caso", "sempre 5", "sempre 10"], "Ogni giorno una cifra a caso da 1 a 5.")),
      S(2, C("concetti", "Per sapere <b>quanti giorni</b> servono ad arrivare al prezzo uso…", ["il WHILE: non so prima quante volte", "il FOR da 1 a 7", "niente ciclo"], "Non lo sai prima: dipende dai soldi a caso.")),
      S(2, C("concetti", "<code>while totale &lt; prezzo do</code> si legge…", ["finché il totale è minore del prezzo", "se il totale è uguale al prezzo", "per totale da 1 a prezzo"], "&lt; vuol dire minore.")),
      S(3, C("pratica", "Pezzo 1 fatto? Premendo F9 vedi…", ["la finestra con 2 caselle, 3 bottoni e il Memo", "un errore rosso", "non ho ancora finito la Form"], "Tutte le risposte vanno bene: serve al monitor.")),
      S(4, C("concetti", "<code>Random(5) + 1</code> dà un numero…", ["da 1 a 5", "da 0 a 5", "sempre 5"], "Random(5) va da 0 a 4, più 1.")),
      S(4, C("concetti", "<code>totale := totale + euro;</code> vuol dire…", ["al totale di prima aggiungo gli euro di oggi", "il totale diventa uguale a euro", "confronto totale ed euro"], "Come mettere monete nel salvadanaio.")),
      S(4, C("concetti", "La riga con il totale della settimana va…", ["dopo l'end; del ciclo, così si scrive una volta", "dentro il ciclo", "prima del for"], "Dentro il ciclo si scriverebbe 7 volte.")),
      S(4, C("pratica", "Pezzo 2 fatto? Premendo «Una settimana» nel Memo vedi…", ["7 righe Giorno 1… Giorno 7 e il totale", "un errore rosso", "non ho ancora finito"], "Se vedi un errore, guarda la scheda 8.")),
      S(5, C("concetti", "Perché si scrive <code>totale := 0;</code> e <code>giorni := 0;</code> prima del while?", ["il salvadanaio parte vuoto e i giorni da zero", "per fermare il ciclo", "non serve a niente"], "Si parte da zero, poi si aggiunge.")),
      S(5, C("concetti", "Il while si ferma quando…", ["il totale arriva al prezzo o lo supera", "sono passati 7 giorni", "mai"], "totale &lt; prezzo diventa falso.")),
      S(5, C("pratica", "Pezzo 3 fatto? Premendo «Quanti giorni mi servono?»…", ["il Memo dice quanti giorni servono per la mia cosa", "il programma si blocca", "non ho ancora finito"], "Si blocca? Ciclo infinito: scheda 8.")),
      S(6, C("concetti", "<code>23 div 7</code> fa…", ["3", "2", "3,28"], "Quante volte 7 ci sta in 23: 3.")),
      S(6, C("concetti", "<code>23 mod 7</code> fa…", ["2", "3", "0"], "7 × 3 = 21, avanzano 2.")),
      S(7, C("concetti", "Il giorno 14 è un sabato perché…", ["14 mod 7 = 0", "14 div 7 = 0", "14 è pari"], "14 diviso 7 non ha resto.")),
      S(7, C("pratica", "Hai provato la sfida della paghetta?", ["sì, funziona", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("concetti", "Quando uso il FOR invece del WHILE?", ["quando so prima quante volte ripetere", "quando non lo so", "mai"], "", "differenza"),
      C("concetti", "<code>for giorno := 1 to 7 do</code> quanti giri fa?", ["7", "6", "8"], "", "for"),
      C("concetti", "Nel FOR il contatore <code>giorno</code>…", ["aumenta da solo a ogni giro", "lo devo aumentare io", "resta sempre 1"], "", "for"),
      C("concetti", "Nel WHILE dei giorni, chi fa aumentare <code>giorni</code>?", ["io, con giorni := giorni + 1", "Lazarus da solo", "nessuno"], "", "contatore"),
      C("concetti", "<code>totale := 0; for i := 1 to 3 do totale := totale + 2;</code> alla fine totale vale…", ["6", "2", "3"], "", "somma"),
      C("concetti", "<code>while totale &lt; prezzo do</code> con totale = 50 e prezzo = 40: quanti giri fa?", ["nessuno: la condizione è falsa subito", "40", "infiniti"], "", "uscita"),
      C("concetti", "Se dentro il while dimentico <code>totale := totale + euro;</code>…", ["ciclo infinito: il totale non arriva mai al prezzo", "finisce subito", "funziona uguale"], "", "uscita"),
      C("concetti", "Il prezzo scritto dal ragazzo si legge con…", ["prezzo := StrToInt(Edit2.Text);", "prezzo := Edit2.Text;", "prezzo := IntToStr(Edit2.Text);"], "", "form"),
      C("concetti", "Il nome della cosa da comprare va nel Memo con…", ["Edit1.Text, che è già testo", "IntToStr(Edit1.Text)", "StrToInt(Edit1.Text)"], "", "form"),
      C("concetti", "<code>Random(5) + 1</code> può dare 0?", ["no: dà da 1 a 5", "sì", "solo il primo giorno"], "", "random"),
      C("concetti", "<code>30 div 7</code> e <code>30 mod 7</code> fanno…", ["4 e 2", "4 e 4", "2 e 4"], "", "mod"),
      C("concetti", "Quale giorno è un sabato con la regola <code>giorni mod 7 = 0</code>?", ["21", "20", "22"], "", "mod"),
      C("concetti", "La riga del totale della settimana è dentro il ciclo FOR. Che cosa succede?", ["il totale si scrive 7 volte", "non si scrive mai", "errore di compilazione"], "", "errori")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di scegliere tra FOR e WHILE da solo?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto sei fiero del tuo salvadanaio?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "pratica", incolla: true, q: "Incolla qui TUTTO il codice del tuo salvadanaio (dalla prima procedure TForm1.Button1Click fino all'ultimo end; dei bottoni). Qui l'incolla è permesso.", aiuto: "In Lazarus, nella finestra del codice: seleziona, Ctrl+C, poi qui Ctrl+V. Se non ce l'hai, scrivi: non fatto, e il motivo.", min_parole: 5,
        criteri: "codice vero: Button1Click con for giorno := 1 to 7, Random(5) + 1, totale := totale + euro, totale scritto dopo il ciclo; Button2Click con prezzo := StrToInt(Edit2.Text), totale e giorni a 0, while totale < prezzo, giorni := giorni + 1, uso di Edit1.Text; sfida: Button3Click con if giorni mod 7 = 0; rientri" },
      { area: "programma", tema: "uscita", q: "Spiega in due righe, con parole tue, che cosa fa il tuo programma: che cosa fa il bottone con il FOR e che cosa fa il bottone con il WHILE.", aiuto: "Almeno 20 parole. Scrivi tu, senza copiare: è la prova del «saperlo spiegare».", min_parole: 20,
        criteri: "FOR: 7 giorni, soldi a caso, somma e totale della settimana; WHILE: ripete finché il totale è minore del prezzo, conta i giorni; parole sue" },
      { area: "programma", tema: "uscita", q: "Perché il tuo ciclo WHILE prima o poi si ferma? Che cosa succederebbe se il totale non crescesse?", aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "a ogni giro il totale cresce; quando arriva al prezzo la condizione totale < prezzo diventa falsa; senza crescita: ciclo infinito" },
      { area: "pratica", tema: "errori", q: "Racconta un errore che hai fatto oggi (o un compagno) e come l'avete risolto.", aiuto: "Almeno 15 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 15,
        criteri: "errore concreto e soluzione" },
      { area: "parere", tema: "retro", q: "Che cosa ti è piaciuto di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("concetti", "Una settimana ha 7 giorni: per contarli uso…", ["il FOR", "il WHILE", "il mod"], "", "differenza"),
      C("concetti", "While vuol dire…", ["finché", "per", "se"], "", "while"),
      C("concetti", "<code>totale := totale + 3;</code> con totale = 10: dopo vale…", ["13", "3", "10"], "", "somma"),
      C("concetti", "Il while si ferma quando la condizione è…", ["falsa", "vera", "uguale a 7"], "", "uscita"),
      C("concetti", "Un ciclo che non finisce mai si chiama…", ["ciclo infinito", "ciclo for", "paghetta"], "", "uscita"),
      C("concetti", "<code>14 mod 7</code> fa…", ["0", "2", "7"], "", "mod"),
      C("concetti", "Il prezzo dalla casella Edit2 si legge con…", ["StrToInt(Edit2.Text)", "IntToStr(Edit2.Text)", "Edit2.Caption"], "", "form")
    ]
  };
})();
