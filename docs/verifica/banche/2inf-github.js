// 2INF · GitHub: «Il mio repository lazarus in ordine» (22/10/2026, Nicola: «ognuno ha gestito i file su git in modo diverso…
// creare una cartella root e poi ogni progetto sotto… almeno poi siamo tutti allineati»). Lezione pratica, passo a passo, ~45 minuti.
// Alla fine il PC e GitHub hanno lo STESSO albero: lazarus/ con primo-programma, salvadanaio, esercizio-3, esercizio-4.
// Controllo automatico: riservato generatori/ordine_github_2inf.py → ../2inf-monitor/ordine.json. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">' + t + '</pre>'; }
  function F(t) { return '<div style="background:#dafbe1;border:2px solid #1a7f37;border-radius:8px;padding:8px 12px;margin:8px 0;font-weight:700">FATTO! ' + t + '</div>'; }
  var ALBERO = "lazarus\n├── primo-programma\n├── salvadanaio\n├── esercizio-3\n├── esercizio-4\n└── README.md   (solo su GitHub)";
  var README = "# I miei progetti Lazarus\n\nSono (il tuo nome), classe 2INF.\n\n1. primo-programma: il mio primo programma\n2. salvadanaio: FOR e WHILE, quanti giorni per comprare (la tua cosa)\n3. esercizio-3: in arrivo\n4. esercizio-4: in arrivo";

  window.BANCA = {
    id: "2inf-github-v1",
    classe: "2INF",
    controllo: "../2inf-monitor/ordine.json",
    titolo: "Il mio repository «lazarus» in ordine",
    sotto: "2INF · 22/10/2026 · GitHub · una cartella per ogni progetto, uguale sul PC e su GitHub (circa 45 minuti)",
    stato: "stato/2inf-github.json",
    risultati: "risultati.html?b=2inf-github",
    minuti: 45,
    aree: {
      concetti: { nome: "Concetti: repository, cartella, commit, caricare", peso: 40 },
      pratica: { nome: "La pratica: il tuo repository in ordine", peso: 60 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { ordine: 1, parole: 2, pc: 3, github: 5, pulire: 6, readme: 9, nomi: 10, carica: 11 },
    schede: [
      { titolo: "1. Che cosa facciamo oggi: tutti uguali, tutto in ordine", testo: "Oggi metti in ordine i tuoi progetti, come fa un programmatore vero.<br>Un datore di lavoro guarda il tuo GitHub: deve trovare <b>ogni progetto nella sua cartella</b>, non file sparsi.<br>La regola è una sola: <b>una cartella grande «lazarus»</b> e dentro <b>una cartella per ogni progetto</b>.<br>Sul tuo PC e su GitHub l'albero è <b>uguale</b>:" + K(ALBERO) + "Le cartelle «esercizio-3» e «esercizio-4» sono per i prossimi esercizi: oggi le prepari vuote, poi il prof ti dice il nome vero.<br>Un passo alla volta. Ogni passo finisce con un <b>FATTO!</b> verde." },
      { titolo: "2. Le parole di oggi", testo: "<b>Repository</b> = la cartella grande del tuo progetto su GitHub. Il tuo si chiama <b>lazarus</b>.<br><b>Cartella</b> (in inglese <i>folder</i>) = una scatola dentro il repository. Una per progetto.<br><b>Caricare</b> (in inglese <i>upload</i>) = mandare i file dal PC a GitHub.<br><b>Commit</b> = il salvataggio su GitHub, con una frase che dice che cosa hai fatto.<br><b>README</b> = la pagina di presentazione del repository: chi sei e che cosa c'è dentro.<br>Il sito è in inglese: <b>Add file</b> = aggiungi file, <b>New Folder</b> = nuova cartella, <b>Delete</b> = cancella, <b>Move</b> = sposta." },
      { titolo: "3. PASSO 1 e 2: la cartella «lazarus» sul PC", testo: "1) <b>Chiudi Lazarus</b> (la X in alto a destra). Se chiede di salvare, premi <b>Sì</b>. Con Lazarus aperto le cartelle non si spostano.<br>2) Apri <b>Esplora file</b> (la cartella gialla in basso) e clicca <b>Documenti</b> a sinistra.<br>3) In alto clicca <b>Nuova cartella</b> e scrivi il nome, tutto minuscolo:" + K("lazarus") + "4) Premi <b>Invio</b>." + F("In Documenti c'è la cartella «lazarus».") },
      { titolo: "4. PASSO 3 e 4: dentro «lazarus», le cartelle dei progetti", testo: "1) Trova la cartella del tuo <b>salvadanaio</b> (in Documenti, o dove l'hai salvata: in Lazarus il percorso era scritto in alto, tra parentesi).<br>2) <b>Trascinala</b> sopra la cartella <b>lazarus</b> e lascia andare: adesso è dentro.<br>3) Se si chiama in un altro modo (salvadanio, for e while…), tasto destro → <b>Rinomina</b> e scrivi:" + K("salvadanaio") + "4) Entra in <b>lazarus</b> (doppio clic) e crea due cartelle nuove con <b>Nuova cartella</b>:" + K("esercizio-3") + K("esercizio-4") + F("Dentro Documenti\\lazarus ci sono salvadanaio, esercizio-3 ed esercizio-4.") },
      { titolo: "5. PASSO 5: apri il tuo repository nell'editor di GitHub", testo: "1) In Chrome apri <b>github.com</b> e il tuo repository <b>lazarus</b> (in alto a destra la tua foto → <b>Your repositories</b> → <b>lazarus</b>).<br>2) Clicca una volta in un punto vuoto della pagina e premi il tasto <b>.</b> (il punto).<br>3) Si apre <b>github.dev</b>: è come un programma, ma nel browser. A sinistra vedi i file del repository.<br>4) A sinistra, sotto l'ultimo file, clicca con il tasto <b>destro</b> nello spazio vuoto → <b>New Folder…</b> e scrivi:" + K("primo-programma") + "e premi Invio." + F("A sinistra c'è la cartella «primo-programma».") },
      { titolo: "6. PASSO 6: i file sparsi vanno in «primo-programma»", testo: "I file nella pagina principale (project1, unit1, …) sono il tuo progetto vecchio. Mettiamoli nella sua cartella.<br>1) A sinistra clicca il <b>primo file</b> sotto le cartelle.<br>2) Tieni premuto <b>Maiusc</b> e clicca l'<b>ultimo file</b>: si colorano tutti.<br>3) Tieni premuto <b>Ctrl</b> e clicca <b>README.md</b>: il README <b>non</b> si sposta.<br>4) <b>Trascina</b> i file colorati sopra la cartella <b>primo-programma</b> e clicca <b>Move</b>.<br>Nessun file sparso, solo il README? Questo passo è già fatto: vai al passo 7." + F("A sinistra restano solo le cartelle e README.md.") },
      { titolo: "7. PASSO 7: via i file .exe", testo: "Il file <b>.exe</b> è il programma già pronto: pesa tanto e non serve, perché il progetto si ricrea da Lazarus con F9.<br>1) Apri le cartelle a sinistra (clic sulla freccina) e cerca i file che finiscono con <b>.exe</b>.<br>2) Clicca il file .exe e premi <b>Canc</b>, poi <b>Delete</b>.<br>3) Fallo per ogni .exe. Le cartelle <b>lib</b> e <b>backup</b> puoi cancellarle allo stesso modo: le rifà Lazarus." + F("Nel repository non ci sono più file .exe.") },
      { titolo: "8. PASSO 8: le cartelle dei prossimi esercizi", testo: "GitHub non tiene le cartelle vuote: dentro ci mettiamo un piccolo README.<br>1) A sinistra, tasto destro nello spazio vuoto → <b>New File…</b> e scrivi, con la barra <b>/</b>:" + K("esercizio-3/README.md") + "La barra crea la cartella e il file dentro. Premi Invio.<br>2) Nel file che si apre scrivi:" + K("Qui andrà l'esercizio 3") + "3) Rifai per il 4:" + K("esercizio-4/README.md") + K("Qui andrà l'esercizio 4") + F("A sinistra ci sono esercizio-3 ed esercizio-4.") },
      { titolo: "9. PASSO 9: il tuo README (Fallo tuo) e il commit", testo: "1) A sinistra clicca <b>README.md</b> (quello fuori dalle cartelle).<br>2) Cancella tutto (<b>Ctrl+A</b>, <b>Canc</b>) e scrivi la tua presentazione. Puoi partire da questo e cambiarlo come vuoi tu:" + K(README) + "3) Nella barra delle icone tutta a sinistra clicca la <b>terza icona</b> (quella con il pallino blu e un numero).<br>4) Nella casella <b>Message</b> scrivi:" + K("Metto in ordine i miei progetti") + "5) Clicca il bottone verde <b>Commit &amp; Push</b>." + F("Il commit è partito: sul tuo repository vedi le cartelle e il README nuovo.") },
      { titolo: "10. Errori tipici (succede a tutti, anche ai pro)", testo: "1) <b>La cartella ha un nome sbagliato</b> (salvadanio, for e while, salvadanio2): in github.dev tasto destro sulla cartella → <b>Rename</b> e scrivi il nome giusto, poi commit.<br>2) <b>Ho spostato anche il README</b> dentro primo-programma: trascinalo fuori, sopra lo spazio vuoto in basso.<br>3) <b>Commit &amp; Push è grigio</b>: non hai scritto il messaggio nella casella <b>Message</b>.<br>4) <b>Non vedo le cartelle su github.com</b>: ricarica la pagina (<b>F5</b>). Hai premuto Commit &amp; Push?<br>5) <b>Ho due repository</b> (lazarus e lazarus-): ne tieni uno solo e si chiama <b>lazarus</b>. Chiedi all'assistente." + F("Hai risolto il tuo errore da solo, o con l'assistente.") },
      { titolo: "11. PASSO 10 e 11: il salvadanaio su GitHub", testo: "1) Torna su <b>github.com</b>, nel tuo repository <b>lazarus</b>, e ricarica la pagina (F5).<br>2) Clicca <b>Add file</b> (a sinistra del bottone verde Code) → <b>Upload files</b>.<br>3) Apri <b>Esplora file</b> → <b>Documenti</b> → <b>lazarus</b>.<br>4) <b>Trascina la cartella salvadanaio</b> dentro la pagina di GitHub (porta il mouse sull'icona di Chrome in basso e aspetta un secondo, poi lascia al centro della pagina).<br>5) Aspetta la barra verde piena e clicca <b>Commit changes</b>.<br>6) Guarda la tabella in alto in questa pagina: entro 5 minuti la tua riga diventa verde." + F("Il tuo GitHub è uguale alla cartella lazarus del tuo PC. Fallo vedere al compagno!") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../2inf-oggi/', c: '#1f7a3f' }, { t: 'Il monitor della lezione', u: '../2inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "Dove va un progetto nuovo di Lazarus su GitHub?", ["in una sua cartella dentro il repository «lazarus»", "sparso nella pagina principale", "in un repository nuovo ogni volta"], "Una cartella per progetto, tutte dentro lazarus."),
    prepara: [],
    allenamento: [
      S(1, C("concetti", "Che cosa c'è nella pagina principale del repository «lazarus», quando è in ordine?", ["solo le cartelle dei progetti e il README", "tutti i file di tutti i progetti", "solo il file .exe"], "File sparsi = disordine.")),
      S(2, C("concetti", "Un commit è…", ["un salvataggio su GitHub con una frase che dice che cosa ho fatto", "un errore", "una password"], "Commit = salvataggio con messaggio.")),
      S(3, C("pratica", "Passo 1 e 2: in Documenti c'è la cartella «lazarus»?", ["sì", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor.")),
      S(4, C("pratica", "Passo 3 e 4: dentro lazarus ci sono salvadanaio, esercizio-3, esercizio-4?", ["sì", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor.")),
      S(6, C("concetti", "Per selezionare tanti file di fila in github.dev…", ["clicco il primo, tengo Maiusc e clicco l'ultimo", "clicco solo il primo", "premo F9"], "Maiusc = dal primo all'ultimo; Ctrl = uno alla volta.")),
      S(7, C("concetti", "Perché togliamo il file .exe?", ["è il programma già pronto: pesa e non serve, basta il progetto", "è un virus", "GitHub non lo legge"], "Il progetto si ricrea con F9.")),
      S(8, C("concetti", "Scrivendo «esercizio-3/README.md» come nome del file nuovo…", ["la barra crea la cartella esercizio-3 e dentro il file", "il file si chiama con la barra", "dà errore"], "La barra / separa cartella e file.")),
      S(9, C("pratica", "Passo 9: hai fatto Commit & Push?", ["sì", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor."))
    ],
    crocette: [
      C("concetti", "Il repository di Lazarus di ognuno di noi si chiama…", ["lazarus", "lazarus-", "progetto1"], "", "ordine"),
      C("concetti", "Sul PC la cartella dei progetti Lazarus è…", ["Documenti\\lazarus, con una cartella per progetto", "il Desktop, con i file sparsi", "C:\\ con un nome a caso"], "", "pc"),
      C("concetti", "Caricare (upload) vuol dire…", ["mandare i file dal PC a GitHub", "cancellare i file", "far partire il programma"], "", "parole"),
      C("concetti", "Il README serve a…", ["presentare chi sei e che cosa c'è nel repository", "far partire Lazarus", "cancellare i file vecchi"], "", "readme"),
      C("concetti", "GitHub tiene una cartella vuota?", ["no: per tenerla ci metto dentro un file, come un README", "sì, sempre", "solo se è grande"], "", "github"),
      C("concetti", "Per spostare un file in una cartella in github.dev…", ["lo trascino sopra la cartella e clicco Move", "lo cancello", "premo F9"], "", "pulire")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di mettere un progetto nuovo nella sua cartella su GitHub da solo?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "ordine", q: "Scrivi l'indirizzo del tuo repository (github.com/…/lazarus) e, con parole tue, dove va il prossimo esercizio di Lazarus sul PC e su GitHub.", aiuto: "Almeno 15 parole. Scrivi tu, senza copiare: è la prova del «saperlo spiegare».", min_parole: 15,
        criteri: "indirizzo github.com/<utente>/lazarus; il prossimo esercizio va in Documenti\\lazarus\\esercizio-3 sul PC e nella cartella esercizio-3 del repository; parole sue" }
    ],
    recupero: [
      C("concetti", "Una cartella per ogni…", ["progetto", "file", "giorno"], "", "ordine"),
      C("concetti", "Commit vuol dire…", ["salvataggio su GitHub", "cancella", "apri"], "", "parole"),
      C("concetti", "Il file .exe nel repository…", ["non serve", "è obbligatorio", "è il README"], "", "pulire")
    ]
  };
})();
