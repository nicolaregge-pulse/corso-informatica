// 2INF · Lazarus: il ciclo WHILE, «ripeti finché…» (20/10/2026). Dopo il FOR (15 e 19/10).
// Il gioco: lancia il dado finché esce il tuo numero magico, e conta i tiri. Ripasso, pratica passo per passo, verifica, recupero.
// Aree e peso nel giudizio: concetti 40%, il tuo programma (saperlo spiegare) 40%, la pratica fatta 20%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">' + t + '</pre>'; }
  var CODICE = "var dado, magico, tiri: integer;\nbegin\n  Randomize;\n  magico := StrToInt(Edit1.Text);\n  Memo1.Clear;\n  tiri := 0;\n  dado := 0;\n  while dado &lt;&gt; magico do\n  begin\n    dado := Random(6) + 1;\n    tiri := tiri + 1;\n    Memo1.Lines.Add('Tiro ' + IntToStr(tiri) + ': ' + IntToStr(dado));\n  end;\n  Memo1.Lines.Add('Uscito il ' + IntToStr(magico) + ' dopo ' + IntToStr(tiri) + ' tiri!');\nend;";

  window.BANCA = {
    id: "2inf-while-v1",
    classe: "2INF",
    titolo: "Il ciclo WHILE: lancia il dado finché…",
    sotto: "2INF · 20/10/2026 · Lazarus · ripasso, pratica, verifica e recupero",
    stato: "stato/2inf-while.json",
    risultati: "risultati.html?b=2inf-while",
    minuti: 30,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: while, condizione, ciclo infinito, Random", peso: 40 },
      programma: { nome: "Il tuo programma: saperlo spiegare (solo parole tue)", peso: 40 },
      pratica: { nome: "La pratica fatta", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO ---------- */
    schede_temi: { differenza: 1, forma: 2, infinito: 3, random: 4, programma: 5, pratica: 6, errori: 8 },
    schede: [
      { titolo: "1. Dal FOR al WHILE: quando non sai quante volte", testo: "Con il <b>for</b> sai prima quanti giri fai: <code>for x := 1 to 10 do</code> fa 10 giri, sempre.<br>Ma se lanci un dado finché esce il 6, <b>quante volte lo lanci?</b> Non lo sa nessuno: magari 1, magari 15.<br>Per questo c'è il <b>while</b>: «<b>finché</b> la condizione è vera, ripeti». Si ferma quando la condizione diventa falsa.<br>Nella vita: <i>finché</i> ho fame, mangio; <i>finché</i> il semaforo è rosso, aspetto." },
      { titolo: "2. Come si scrive", testo: K("while condizione do\nbegin\n  istruzioni da ripetere;\nend;") + "Si legge: <b>finché</b> la condizione è vera, <b>fai</b> quello che c'è tra begin ed end.<br>La condizione si controlla <b>prima</b> di ogni giro. Se è falsa già all'inizio, il while non fa <b>nessun</b> giro.<br>Le condizioni sono quelle dell'IF: <code>=</code> uguale, <code>&lt;&gt;</code> diverso, <code>&lt;</code> minore, <code>&gt;</code> maggiore, <code>&lt;=</code>, <code>&gt;=</code>.<br>Esempio: conta da 1 a 5 con il while:" + K("x := 1;\nwhile x &lt;= 5 do\nbegin\n  Memo1.Lines.Add(IntToStr(x));\n  x := x + 1;\nend;") + "Nel for il contatore aumenta da solo; nel while <b>lo fai aumentare tu</b> (<code>x := x + 1</code>)." },
      { titolo: "3. Il pericolo: il ciclo infinito", testo: "Se dentro il while niente cambia la condizione, il ciclo <b>non finisce mai</b>:" + K("x := 1;\nwhile x &lt;= 5 do\nbegin\n  Memo1.Lines.Add(IntToStr(x));\nend;") + "Qui manca <code>x := x + 1</code>: x resta 1 per sempre e il programma si <b>blocca</b>.<br>Se ti succede: in Lazarus menu <b>Esegui → Ferma</b> (oppure <b>Ctrl+F2</b>). Succede a tutti i programmatori, anche ai pro: si ferma e si corregge.<br>Regola: dentro il while deve sempre esserci qualcosa che <b>prima o poi</b> rende falsa la condizione." },
      { titolo: "4. Il dado: Random", testo: "Per tirare un dado il computer usa i <b>numeri a caso</b>:" + K("Randomize;\ndado := Random(6) + 1;") + "<b>Randomize</b> «mescola» i numeri: si scrive una volta all'inizio, altrimenti esce sempre la stessa sequenza.<br><b>Random(6)</b> dà un numero da <b>0 a 5</b>; con <b>+ 1</b> diventa da <b>1 a 6</b>, come un dado vero.<br>Per una moneta: <code>Random(2)</code> dà 0 o 1 (testa o croce)." },
      { titolo: "5. Il programma: lancia finché esce il numero magico", testo: "L'interfaccia: in alto <b>Numero magico (1-6)</b> [ 6 ], al centro un Memo grande, in basso un bottone <b>Lancia!</b>. Il codice del bottone, con i rientri giusti:" + K(CODICE) + "Leggilo: prendo il numero magico dalla casella; tiri parte da 0; <b>finché</b> il dado è <b>diverso</b> dal numero magico, tiro il dado, conto il tiro e lo scrivo nel Memo. Quando esce, scrivo dopo quanti tiri.<br>Perché <code>dado := 0</code> prima del while? Perché all'inizio il dado non è ancora uscito: 0 è diverso da qualsiasi numero magico, quindi il primo giro si fa sempre." },
      { titolo: "6. LA PRATICA, passi 1-5: il form", testo: "Un passo alla volta.<br>1) Apri Lazarus: <b>Progetto → Nuovo progetto → Applicazione → Ok</b>.<br>2) Metti un <b>TLabel</b> con Caption <b>Numero magico (1-6)</b>.<br>3) Accanto un <b>TEdit</b> (Edit1): nella proprietà <b>Text</b> scrivi <b>6</b>.<br>4) Al centro un <b>TMemo</b> grande con <b>ScrollBars = ssBoth</b>; cancella le righe di <b>Lines</b>.<br>5) In basso un <b>TButton</b> con Caption <b>Lancia!</b>." },
      { titolo: "7. LA PRATICA, passi 6-9: il codice e la prova", testo: "6) <b>Doppio clic</b> sul bottone: si apre <code>procedure TForm1.Button1Click</code>.<br>7) Scrivi il codice della scheda 5, riga per riga, con i rientri di 2 spazi. La riga <code>var dado, magico, tiri: integer;</code> va <b>sopra</b> il begin.<br>8) Premi <b>F9</b>.<br>9) Premi <b>Lancia!</b> più volte: ogni volta i tiri sono diversi. <b>FATTO!</b><br>Prova: scrivi <b>9</b> nella casella e premi Lancia!. Che cosa succede? (Scheda 3: Esegui → Ferma.)" },
      { titolo: "8. Fallo tuo, gli errori e la sfida", testo: "<b>Fallo tuo</b>: cambia le frasi nel Memo (per esempio <code>'Ce l''hai fatta in '</code>), il titolo della finestra (Caption del form) e il colore del form.<br><b>Tieni pronto il codice per la verifica</b>: seleziona dalla riga <code>var</code> all'ultimo <code>end;</code>, <b>Ctrl+C</b>; nella verifica c'è una domanda dove lo incolli.<br><b>Errori tipici</b>: manca <code>Randomize</code> (escono sempre gli stessi tiri); manca <code>tiri := tiri + 1</code> (dice sempre 0 tiri); <code>while dado = magico</code> invece di <code>&lt;&gt;</code> (non fa nessun giro); numero magico 9 (ciclo infinito).<br><b>Sfida</b>: due dadi, finché escono <b>due 6</b> insieme (<code>while (d1 &lt;&gt; 6) or (d2 &lt;&gt; 6) do</code>). Quanti tiri servono?" }
    ],
    strumenti: [{ t: 'Il monitor della lezione', u: '../2inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "Il while ripete…", ["finché la condizione è vera", "sempre 10 volte", "una volta sola"], "«Finché»: si ferma quando la condizione diventa falsa."),
    prepara: [
      { q: "Pensa a una cosa della tua giornata che fai «finché…» (finché ho sete bevo, finché non arriva il bus aspetto). Scrivila.", min: 6 }
    ],
    allenamento: [
      S(1, C("concetti", "Lancio un dado finché esce il 6. Quanti tiri faccio?", ["non si sa prima: per questo uso il while", "sempre 6", "sempre 1"], "Il for serve quando lo sai prima.")),
      S(2, C("concetti", "La condizione del while si controlla…", ["prima di ogni giro", "solo alla fine", "mai"], "Se è falsa subito, nessun giro.")),
      S(2, C("concetti", "<code>x := 10; while x &lt; 5 do …</code> quanti giri fa?", ["nessuno", "5", "10"], "10 non è minore di 5: falsa subito.")),
      S(2, C("concetti", "Nel while il contatore…", ["lo faccio aumentare io, con x := x + 1", "aumenta da solo come nel for", "non esiste"], "Nel for aumenta da solo; nel while no.")),
      S(3, C("concetti", "Il programma si è bloccato in un ciclo infinito. In Lazarus…", ["Esegui → Ferma (Ctrl+F2)", "spengo il PC", "premo F9 ancora"], "Si ferma e si corregge.")),
      S(4, C("concetti", "<code>Random(6) + 1</code> dà un numero…", ["da 1 a 6", "da 0 a 6", "sempre 6"], "Random(6) va da 0 a 5, più 1.")),
      S(4, C("concetti", "Randomize serve a…", ["mescolare i numeri a caso, una volta all'inizio", "tirare il dado", "fermare il ciclo"], "Senza, esce sempre la stessa sequenza.")),
      S(5, C("concetti", "<code>while dado &lt;&gt; magico do</code> si legge…", ["finché il dado è diverso dal numero magico", "finché il dado è uguale", "se il dado è maggiore"], "&lt;&gt; vuol dire diverso.")),
      S(7, C("pratica", "Passi 1-9 fatti? Premendo Lancia! nel Memo vedi…", ["i tiri uno per riga e alla fine «Uscito il … dopo … tiri!»", "un errore rosso", "niente"], "Se vedi un errore, guarda la scheda 8.")),
      S(8, C("pratica", "Hai provato la sfida dei due 6?", ["sì, funziona", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("concetti", "Quando conviene il while invece del for?", ["quando non so prima quante volte ripetere", "quando so che sono 10 volte", "mai"], "", "differenza"),
      C("concetti", "<code>x := 1; while x &lt;= 3 do begin Memo1.Lines.Add(IntToStr(x)); x := x + 1; end;</code> scrive…", ["1, 2, 3", "1, 2, 3, 4", "solo 1"], "", "forma"),
      C("concetti", "<code>x := 5; while x &gt; 0 do begin Memo1.Lines.Add(IntToStr(x)); x := x - 1; end;</code> scrive…", ["5, 4, 3, 2, 1", "0, 1, 2, 3, 4, 5", "niente"], "", "forma"),
      C("concetti", "<code>x := 0; while x &gt; 3 do x := x + 1;</code> quanti giri fa?", ["nessuno", "3", "infiniti"], "", "forma"),
      C("concetti", "<code>x := 1; while x &lt; 10 do Memo1.Lines.Add('ciao');</code> che cosa succede?", ["ciclo infinito: x non cambia mai", "scrive ciao 10 volte", "non scrive niente"], "", "infinito"),
      C("concetti", "Per non fare un ciclo infinito, dentro il while…", ["qualcosa deve cambiare la condizione", "metto un altro while", "tolgo begin ed end"], "", "infinito"),
      C("concetti", "<code>Random(10)</code> dà un numero…", ["da 0 a 9", "da 1 a 10", "sempre 10"], "", "random"),
      C("concetti", "Per un dado da 1 a 6 scrivo…", ["Random(6) + 1", "Random(6)", "Random(7)"], "", "random"),
      C("concetti", "Nel programma del dado, <code>tiri := tiri + 1</code> serve a…", ["contare quanti tiri ho fatto", "tirare il dado", "fermare il ciclo"], "", "programma"),
      C("concetti", "Nel programma del dado scrivo 9 come numero magico. Che cosa succede?", ["ciclo infinito: il dado non fa mai 9", "esce subito", "errore di compilazione"], "", "infinito"),
      C("concetti", "<code>&lt;&gt;</code> vuol dire…", ["diverso", "uguale", "minore o uguale"], "", "forma"),
      C("concetti", "Se tolgo <code>Randomize</code>, a ogni avvio del programma…", ["escono sempre gli stessi tiri", "il dado non funziona", "il ciclo diventa infinito"], "", "random")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di scrivere un while da solo?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti è piaciuto il gioco del dado?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "pratica", incolla: true, q: "Incolla qui il codice del tuo bottone Lancia! (dalla riga var fino all'ultimo end;). Qui l'incolla è permesso.", aiuto: "Nella finestra del codice di Lazarus: seleziona, Ctrl+C, poi qui Ctrl+V. Se non ce l'hai, scrivi: non fatto, e il motivo.", min_parole: 5,
        criteri: "codice vero: var integer, Randomize, StrToInt, tiri := 0, while … <> … do, Random(6) + 1, tiri := tiri + 1, Memo1.Lines.Add; rientri" },
      { area: "programma", tema: "programma", q: "Spiega con parole tue il codice che hai incollato: che cosa fanno Randomize, la riga del while, Random(6) + 1, tiri := tiri + 1, e perché il ciclo prima o poi finisce.", aiuto: "Almeno 30 parole. Scrivi tu, senza copiare.", min_parole: 30,
        criteri: "Randomize mescola; while ripete finché il dado è diverso dal magico; Random da 1 a 6; conta i tiri; finisce quando esce il numero; parole sue" },
      { area: "concetti", tema: "infinito", q: "Che cos'è un ciclo infinito? Fai un esempio (anche con il dado) e di' come si evita.", aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "ciclo che non finisce perché la condizione resta vera; esempio (x non aumenta, magico 9); si evita cambiando la condizione dentro il ciclo" },
      { area: "pratica", tema: "errori", q: "Racconta un errore che hai fatto oggi (o un compagno) e come l'avete risolto.", aiuto: "Almeno 15 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 15,
        criteri: "errore concreto e soluzione" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("concetti", "While vuol dire…", ["finché", "per", "se"], "", "differenza"),
      C("concetti", "Il while si ferma quando la condizione è…", ["falsa", "vera", "uguale a 10"], "", "forma"),
      C("concetti", "<code>x := 1; while x &lt;= 2 do begin Memo1.Lines.Add(IntToStr(x)); x := x + 1; end;</code> scrive…", ["1, 2", "1", "1, 2, 3"], "", "forma"),
      C("concetti", "Un ciclo che non finisce mai si chiama…", ["ciclo infinito", "ciclo for", "errore di sintassi"], "", "infinito"),
      C("concetti", "Il dado da 1 a 6 si scrive…", ["Random(6) + 1", "Random(1)", "Dado(6)"], "", "random"),
      C("concetti", "Per fermare un programma bloccato in Lazarus…", ["Esegui → Ferma", "F9", "Ctrl+C"], "", "infinito"),
      C("concetti", "Nel while, chi fa aumentare il contatore?", ["io, con x := x + 1", "Lazarus da solo", "nessuno"], "", "forma")
    ]
  };
})();
