// 2INF · Ripasso, verifica e recupero su: versioni e GitHub, il nostro sistema (portali, AI, informatica), l'esperienza personale, i dati del 12/10.
// Aree di competenza e peso nel giudizio: nozioni 30%, progetto e sistema 30%, esperienza personale 30%, dati 10%.
// Il voto è un giudizio complessivo del prof sulle risposte, non la somma dei punti. Solo italiano.
(function () {
  var VERSIONI = [
    ["v0.12", "La versione serale: il cielo del tramonto"], ["v0.13", "A ogni livello cambia lo scenario"],
    ["v0.14", "L'ultimo colpo quando il vetro si spacca"], ["v0.15", "La difficoltà cresce a ogni livello"],
    ["v0.16", "Il vetro regge 10 colpi"], ["v0.17", "I cattivi non nascono più troppo vicino"],
    ["v0.18", "BANG! e il cattivo cade a terra"], ["v0.19", "Il mirino rosso"],
    ["v0.20", "I cattivi si vedono sempre"], ["v0.21", "Le luci dei palazzi non lampeggiano più"],
    ["v0.22", "Il record accanto ai punti"], ["v0.23", "Il bottone Pausa"],
    ["v0.24", "Più avanti, più punti"], ["v0.25", "Colpo preciso in testa: punti bonus"],
    ["v0.26", "Pioggia e nebbia"], ["v0.27", "Binari gialli"],
    ["v0.28", "La barra del prossimo livello"], ["v0.29", "Le statistiche a fine partita"],
    ["v0.30", "La sfera d'oro: punti x2"], ["v0.31", "Gli uccelli nel cielo"]
  ];
  var GIOCA = "https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/versioni/";
  // Pull Request ricevute ogni quarto d'ora il 12/10 (dal backlog della giornata)
  var QUARTI = [["12:15", 3], ["12:30", 4], ["12:45", 22], ["13:00", 49], ["13:15", 23], ["13:30", 21], ["13:45", 7]];
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }

  window.BANCA = {
    id: "2inf-versioning-20261013",
    classe: "2INF",
    titolo: "Versioni, GitHub e il nostro treno",
    sotto: "2INF · 13/10/2026 · ripasso, verifica e recupero",
    stato: "stato/2inf-versioning.json",           // il prof apre la verifica e il recupero da qui
    risultati: "risultati.html?b=2inf-versioning",  // pagina pubblica della correzione
    backlog: "../2inf-backlog/backlog.json",        // per la parte personale: le Pull Request vere di lunedì
    modulo: "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform",
    minuti: 50,
    anteprima: "868848605",   // impronta del codice dell'anteprima del prof (il codice sta nel repository riservato)
    aree: {
      nozioni: { nome: "Nozioni: versioni, Git e GitHub", peso: 30 },
      sistema: { nome: "Il progetto: portali, intelligenza artificiale e informatica", peso: 30 },
      personale: { nome: "La tua esperienza del progetto (solo parole tue, senza intelligenza artificiale)", peso: 30 },
      dati: { nome: "Leggere i dati della lezione", peso: 10 },
      parere: { nome: "Il tuo parere su questa verifica (non conta per il voto)", peso: 0 }
    },
    quarti: QUARTI,

    /* ---------- RIPASSO ---------- */
    schede: [
      { titolo: "1. Le versioni", testo: "Una <b>versione</b> è un salvataggio del programma con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Se cambia il numero dopo il punto (v0.30 → v0.31) è un passo piccolo, <b>minor</b>. Se cambia il primo numero (v1.4 → v2.0) è un cambio grande, <b>major</b>: per esempio un motore nuovo, come Godot. Il <b>changelog</b> è il registro di tutte le modifiche, versione per versione." },
      { titolo: "2. Git e GitHub", testo: "<b>Git</b> è il programma che tiene tutte le versioni di un progetto. Ogni salvataggio si chiama <b>commit</b>. Il <b>repository</b> è la cartella del progetto con tutta la sua storia. <b>GitHub</b> è il sito che tiene i repository su Internet e li mostra a tutti: è lì che sta il nostro treno. Un <b>ramo</b> (branch) è una strada parallela di lavoro; un <b>fork</b> è una copia del progetto (la 3INF ha fatto il fork del nostro treno); il <b>merge</b> unisce un ramo dentro un altro." },
      { titolo: "3. La Pull Request e il backlog", testo: "Una <b>Pull Request</b> (PR) è una <b>richiesta di modifica scritta</b>: Titolo, Cosa cambia, Dove, Perché. Tutte le richieste vanno nel <b>backlog</b>, la coda dei lavori. Ognuna vale uno, chiunque la faccia; il <b>peso</b> dice quanto lavoro serve sul codice (1 colore, 2 numero, 3 personaggio, 5 ambiente, 8 regola nuova). Si fanno prima le più leggere; a parità di peso, chi è arrivato prima. È il metodo <b>Agile</b>: piccoli passi, sbagliare presto e correggere presto." },
      { titolo: "4. Il nostro sistema, pezzo per pezzo", testo: "1) Su <b>Google Classroom</b> c'è un solo compito con un link fisso. 2) La PR la mandi dal <b>Modulo «Consegna»</b> (Google Moduli). 3) Uno <b>script</b> (un piccolo programma di Google, Apps Script) ogni minuto porta le consegne nel <b>repository</b> del corso su <b>GitHub</b>. 4) <b>Claude</b>, l'intelligenza artificiale che lavora con il prof, legge la PR, le dà un peso nel backlog, <b>scrive il codice</b> della modifica, la prova nel browser e pubblica la versione nuova. 5) <b>GitHub Pages</b> mette il gioco e le pagine (backlog, voti, monitor, novità) sul sito, e si aggiornano da sole. 6) Il prof decide: sì o no alla PR, e il voto." },
      { titolo: "5. Chi fa cosa", testo: "<b>Tu</b> hai l'idea e la scrivi bene. <b>Il prof</b> decide cosa entra e dà il voto. <b>Claude</b> scrive il codice e lo prova. <b>GitHub</b> tiene tutte le versioni, così se una modifica rompe il gioco si torna indietro. Da oggi il treno passa su <b>Godot</b>: è un cambio major, e ogni classe avrà il suo <b>ramo</b> che parte dalla base del prof." }
    ],
    via: C("sistema", "Lunedì, come chiedevate una modifica al gioco?", ["con una Pull Request dal Modulo «Consegna»", "scrivendo il codice in Lazarus", "chiedendolo a voce al prof"], "Esatto: una richiesta di modifica scritta. Lunedì ne avete mandate 129, e sono nate 20 versioni del gioco."),
    prepara: [
      { q: "Lunedì: racconta una tua richiesta, con parole diverse da quelle che hai scritto, e perché l'hai fatta.", aiuto: "Guarda le tue richieste qui sopra per ricordartele.", min: 15 },
      { q: "Una cosa che ti è piaciuta del progetto o del gioco, e una che non ti è piaciuta. Perché?", min: 15 },
      { q: "Una cosa che hai imparato su di te: sul lavorare in squadra, sullo sbagliare e riprovare, sul fare le cose per bene.", min: 15 }
    ],
    allenamento: [
      S(1, C("nozioni", "Da v0.30 a v0.31 il cambio è…", ["piccolo (minor)", "grande (major)"], "Cambia il numero dopo il punto: passo piccolo.")),
      S(2, C("nozioni", "Ogni salvataggio in Git si chiama…", ["commit", "fork", "merge"], "Commit = salvataggio con una descrizione.")),
      S(2, C("nozioni", "La 3INF ha copiato il nostro treno per lavorarci senza toccare il nostro: è un…", ["fork", "merge", "changelog"], "Fork = copia del progetto.")),
      S(4, C("sistema", "Chi porta la tua PR dal Modulo a GitHub?", ["uno script, da solo, ogni minuto", "il prof, a mano", "Classroom"], "Lo script (Apps Script) gira ogni minuto.")),
      S(5, C("sistema", "Chi scrive il codice delle modifiche al treno?", ["Claude, l'intelligenza artificiale che lavora con il prof", "i ragazzi, in Lazarus", "GitHub, da solo"], "Claude scrive e prova il codice; il prof decide.")),
      S(5, C("sistema", "Perché nel gioco il cattivo colpito cade a terra e non c'è sangue?", ["è una regola della scuola: chi scrive il codice la rispetta", "perché il sangue non si può programmare"], "Le scelte del codice seguono le regole di chi decide.")),
      S(4, C("sistema", "A cosa serve GitHub Pages?", ["a mettere il gioco e le pagine sul sito, per tutti", "a scrivere le Pull Request", "a dare i voti"], "Pages pubblica il sito che vedi.")),
      S(3, C("nozioni", "Quale PR passa prima nel backlog?", ["binari gialli (peso 1)", "una regola nuova (peso 8)"], "Prima le più leggere."))
    ],

    /* ---------- VERIFICA ---------- */
    crocette: [
      C("nozioni", "Una versione del programma è…", ["un salvataggio con un numero e la descrizione di cosa cambia", "una copia di riserva senza nome", "un errore del programma"], "Ogni versione ha un numero e una riga che dice cosa cambia.", "versione"),
      C("nozioni", "Da v1.4 a v2.0 il cambio è…", ["grande (major)", "piccolo (minor)"], "Cambia il primo numero: cambio grande.", "numeri"),
      C("nozioni", "Il changelog è…", ["il registro delle modifiche di ogni versione", "l'elenco dei giocatori", "la lista dei voti"], "Change = cambio, log = registro.", "changelog"),
      C("nozioni", "Git e GitHub: qual è la differenza?", ["Git tiene le versioni; GitHub è il sito che tiene i repository su Internet", "sono la stessa cosa", "GitHub è un gioco, Git un sito"], "Git è il programma, GitHub il sito.", "git"),
      C("nozioni", "Un ramo (branch) è…", ["una strada parallela di lavoro sullo stesso progetto", "una versione cancellata", "un errore del codice"], "Ogni classe avrà il suo ramo che parte dalla base del prof.", "ramo"),
      C("nozioni", "merge vuol dire…", ["unire un ramo dentro un altro", "copiare il progetto", "tornare alla versione di prima"], "Merge = fondere.", "merge"),
      C("sistema", "Una Pull Request scritta bene ha quattro parti:", ["Titolo, Cosa cambia, Dove, Perché", "Nome, Cognome, Classe, Data", "Inizio, Svolgimento, Fine, Firma"], "Senza «Dove» e «Perché» chi scrive il codice non sa cosa fare.", "pr"),
      C("sistema", "Il peso di una richiesta nel backlog misura…", ["quanto lavoro sul codice serve", "quanto è importante chi la chiede", "quanto è bella l'idea"], "1 colore, 2 numero, 3 personaggio, 5 ambiente, 8 regola nuova.", "backlog"),
      C("sistema", "Che cosa fa lo script di Google nel nostro sistema?", ["ogni minuto porta le consegne dei Moduli nel repository su GitHub", "scrive il codice del treno", "corregge le verifiche"], "Lo script fa da ponte tra Google e GitHub.", "script"),
      C("sistema", "Nel nostro progetto, chi scrive il codice del treno?", ["Claude, l'intelligenza artificiale che lavora con il prof", "i ragazzi, in Lazarus", "GitHub, da solo"], "Claude scrive e prova il codice; il prof decide che cosa entra.", "ai"),
      C("sistema", "Nella v0.18 il cattivo colpito cade a terra e non c'è sangue. Perché Claude ha scelto così?", ["perché nei giochi di scuola niente sangue: segue le regole del prof e propone un'alternativa", "perché il sangue è troppo difficile da programmare", "per caso"], "Chi scrive il codice segue le regole di chi decide: qui, le regole della scuola.", "scelte"),
      C("sistema", "Arrivano insieme «binari gialli» (peso 1) e «un ambiente nuovo» (peso 5). Quale fa prima Claude, e perché?", ["i binari gialli: costano meno lavoro e il gioco migliora subito", "l'ambiente nuovo: è più bello", "quella del ragazzo con il voto più alto"], "È la regola del backlog: prima le più leggere, così si va avanti a piccoli passi.", "scelte")
    ],
    dati: [
      { tipo: "c", area: "dati", tema: "grafico", q: "Guarda il grafico: in quale quarto d'ora sono arrivate più Pull Request?", o: ["13:00", "12:45", "13:30"], a: 0, spiega: "Tra le 13:00 e le 13:15 ne sono arrivate 49.", grafico: true },
      { tipo: "n", area: "dati", tema: "grafico", q: "Sempre dal grafico: quante Pull Request in tutto tra le 12:45 e le 13:15 (somma delle due barre)?", giusto: 71, spiega: "22 + 49 = 71.", grafico: true }
    ],
    scale: [
      { area: "personale", q: "Quanto ti è piaciuto lavorare così, con le Pull Request, il backlog e le versioni?", basso: "per niente", alto: "moltissimo" },
      { area: "personale", q: "Quanto ti piace il gioco del treno, com'è adesso?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti è piaciuto fare la verifica così?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "sistema", tema: "sistema", q: "Spiega con parole tue il viaggio della tua Pull Request: dal Modulo fino alla versione nuova del gioco. Chi fa cosa (Modulo, script, GitHub, Claude, prof)? Chi scrive il codice, e perché a volte fa una scelta invece di un'altra?", aiuto: "Almeno 40 parole. Per le scelte puoi pensare all'ordine del backlog o alle regole della scuola.", min_parole: 40,
        criteri: "nomina i pezzi in ordine (Modulo, script, GitHub, Claude, prof, sito); dice chi decide e chi scrive il codice; spiega almeno una scelta (ordine del backlog, regole della scuola); parole sue." },
      { area: "personale", tema: "progetto", mostra_pr: true, q: "Il progetto: com'è stato per te lavorare come in un'azienda di software? Racconta un momento preciso di lunedì (una tua richiesta, quando l'hai vista nel gioco o respinta, i voti pubblici, la classifica). Cosa ti è piaciuto e cosa no?",
        aiuto: "Almeno 50 parole. Le tue richieste qui sopra servono solo per ricordare: non ricopiarle, racconta. Solo parole tue: qui non c'è una risposta giusta, c'è la tua esperienza.", min_parole: 50,
        criteri: "momento preciso e vero; cosa gli è piaciuto e cosa no, con il perché; parole sue." },
      { area: "personale", tema: "gioco", q: "Il gioco: cosa ti piace del treno e cosa cambieresti? Se fosse tuo, che cosa aggiungeresti per primo, e perché?",
        aiuto: "Almeno 40 parole. Pensa a quando ci hai giocato tu.", min_parole: 40,
        criteri: "giudizio personale motivato; idea concreta; collegata a quando ha giocato." },
      { area: "personale", tema: "imparato", q: "Cosa hai imparato sulla tua pelle in questo lavoro? Su di te, sul lavorare in squadra, sul fare le cose per bene, sullo sbagliare e riprovare.",
        aiuto: "Almeno 50 parole. Scrivi come parleresti a un amico.", min_parole: 50,
        criteri: "riflessione personale sincera; almeno un esempio vissuto; parole sue." }
    ,
      { area: "parere", tema: "parere", q: "Cosa ne pensi di questa verifica? Cosa ti è piaciuto, cosa cambieresti?", aiuto: "Non conta per il voto: serve al prof per migliorarla. Anche poche parole.", min_parole: 5 }
    ],

    /* ---------- RECUPERO: domande nuove sugli stessi temi ---------- */
    recupero: [
      C("nozioni", "Una versione che cambia solo il numero dopo il punto (v0.26 → v0.27) è…", ["minor: un passo piccolo", "major: un cambio grande"], "", "numeri"),
      C("nozioni", "Che cosa trovi scritto nel changelog della v0.26?", ["cosa è cambiato in quella versione (pioggia e nebbia) e chi l'ha chiesto", "il voto di chi l'ha chiesta", "il codice intero del gioco"], "", "changelog"),
      C("nozioni", "Che cos'è un repository?", ["la cartella del progetto con tutta la sua storia", "un errore", "un tipo di Pull Request"], "", "git"),
      C("nozioni", "La base del prof e il ramo della 2INF: la 2INF lavora…", ["sul suo ramo, che parte dalla base", "sulla base del prof, cambiandola", "su un altro sito"], "", "ramo"),
      C("nozioni", "Se una versione nuova rompe il gioco, grazie alle versioni si può…", ["tornare alla versione di prima", "solo ricominciare da zero", "niente"], "", "versione"),
      C("nozioni", "Unire le modifiche della base del prof nel ramo della classe si chiama…", ["merge", "fork", "commit"], "", "merge"),
      C("sistema", "Una PR dice «cambiate il treno». Che cosa manca?", ["Cosa cambia di preciso, Dove e Perché", "niente, va bene", "il nome del prof"], "", "pr"),
      C("sistema", "Una PR che aggiunge un ambiente nuovo pesa…", ["5", "1", "2"], "", "backlog"),
      C("sistema", "Senza lo script, che cosa succederebbe alla tua PR?", ["resterebbe nel Modulo e il prof dovrebbe copiarla a mano su GitHub", "andrebbe su GitHub lo stesso", "verrebbe cancellata"], "", "script"),
      C("sistema", "Chi decide se una PR entra nel gioco?", ["il prof", "Claude", "lo script"], "", "ai")
    ]
  };
})();
