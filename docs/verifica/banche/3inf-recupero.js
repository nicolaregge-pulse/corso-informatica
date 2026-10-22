// 3INF · Recupero: «Il mio sito personale funziona» (22/10/2026, Nicola: «lezione di recupero per tutti, facile, che faccia arrivare
// tutti ad avere un sito personale; poi vedremo pull request e lavoro congiunto»). Solo github.com, file pronti da copiare.
// Lezione da 2INF del mattino (REGISTRO-ERRORI): prima vittoria subito visibile, pochi passi, la tabella in alto dice a ognuno
// SOLO i passi che gli mancano. Controllo: riservato generatori/sito_3inf_recupero.py → ../3inf-recupero/controllo.json. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">' + t + '</pre>'; }
  function F(t) { return '<div style="background:#dafbe1;border:2px solid #1a7f37;border-radius:8px;padding:8px 12px;margin:8px 0;font-weight:700">FATTO! ' + t + '</div>'; }
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  var COME = "<b>Come si mette un file su GitHub</b> (sempre uguale):<br>" +
    "• Il file <b>non c'è</b>: nel repository clicca <b>Add file</b> → <b>Create new file</b>, scrivi il nome, incolla il testo, poi <b>Commit changes…</b> → <b>Commit changes</b>.<br>" +
    "• Il file <b>c'è già</b> ma la tabella dice di rifarlo: aprilo, clicca la <b>matita</b>, <b>Ctrl+A</b>, incolla il testo nuovo, poi <b>Commit changes…</b> → <b>Commit changes</b>.<br>" +
    "Il testo lo copi da <b>La pagina dei file pronti</b> (bottone verde in alto): lì ogni file ha il suo bottone <b>Copia</b>.";

  window.BANCA = {
    id: "3inf-recupero-v1",
    classe: "3INF",
    controllo: "../3inf-recupero/controllo.json",
    titolo: "Recupero: il mio sito personale funziona",
    sotto: "3INF · 22/10/2026 · un sito di 3 pagine con sfondo, animazione e versione, uguale per tutti (circa 1 ora)",
    stato: "stato/3inf-recupero.json",
    risultati: "risultati.html?b=3inf-recupero",
    minuti: 60,
    aree: {
      concetti: { nome: "Concetti: file, cartelle, link, CSS, GitHub Pages", peso: 40 },
      pratica: { nome: "La pratica: il tuo sito funziona", peso: 60 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { obiettivo: 1, index: 2, css: 3, pagine: 4, foto: 5, pages: 6, errori: 7 },
    schede: [
      { titolo: "1. Oggi: il tuo sito funziona, per tutti", testo: "Oggi ognuno arriva ad avere il suo <b>sito personale</b> che funziona: 3 pagine con il menu, una foto di sfondo, un'animazione e il numero di versione.<br>Si lavora <b>solo su github.com</b>, nel tuo repository del sito. Niente programmi da aprire.<br><b>Guarda la tabella in alto</b>: per ognuno dice <b>che cosa ti manca</b>. Fai <b>solo</b> i passi che ti mancano. Quello che c'è già e funziona non lo tocchi.<br>Il sito ha questi file, tutti nella cartella principale (la foto nella cartella <b>img</b>):" + K("index.html        la Home\nstyle.css         i colori, lo sfondo, l'animazione\ncompetenze.html   che cosa so fare\npassione.html     la mia passione\nimg/sfondo.jpg    la foto di sfondo") + COME },
      { titolo: "2. PASSO 1: la Home (index.html)", testo: "La Home è la prima pagina che si apre. Si chiama sempre <b>index.html</b>, tutto minuscolo.<br>1) Copia il file <b>index.html</b> dalla pagina dei file pronti (bottone verde in alto).<br>2) Mettilo nel repository come spiegato nella scheda 1.<br>3) <b>Fallo tuo</b>: al posto di <b>IL TUO NOME</b> scrivi il tuo nome, e completa le frasi con le tue parole." + F("Nel repository c'è index.html con il tuo nome.") },
      { titolo: "3. PASSO 2: lo stile (style.css)", testo: "Il file <b>style.css</b> dà i colori, la foto di sfondo e l'animazione a tutte le pagine.<br>1) Copia <b>style.css</b> dalla pagina dei file pronti e mettilo nel repository.<br>2) <b>Fallo tuo</b>: cambia il colore del menu: la riga <code>background: #1f6feb;</code> dentro <code>nav</code>. Prova per esempio <code>#e11d48</code> (rosso), <code>#16a34a</code> (verde), <code>#9333ea</code> (viola).<br>Dentro ci sono già lo <b>sfondo</b> (<code>background-image</code>) e l'<b>animazione</b> (<code>@keyframes</code>): il riquadro bianco entra piano dal basso." + F("Nel repository c'è style.css.") },
      { titolo: "4. PASSO 3 e 4: le pagine competenze e passione", testo: "Le altre due pagine si chiamano esattamente <b>competenze.html</b> e <b>passione.html</b> (tutto minuscolo, senza spazi). Se il nome è diverso, il menu non le trova.<br>1) Copia <b>competenze.html</b> dai file pronti, mettila nel repository, scrivi 3 cose che sai fare.<br>2) Copia <b>passione.html</b>, mettila nel repository, scrivi la tua passione (sport, musica, giochi, cucina…).<br>Hai già una pagina con un nome sbagliato (comp.html, passioni.html)? Crea quella con il nome giusto e copia dentro il tuo testo." + F("Nel repository ci sono competenze.html e passione.html.") },
      { titolo: "5. PASSO 5: la foto di sfondo nella cartella img", testo: "1) Cerca una foto che ti piace (Google Immagini, oppure una tua). Salvala sul PC con il nome:" + K("sfondo.jpg") + "Attenzione: deve finire con <b>.jpg</b>. Se Windows la salva come .jfif o .webp, nella finestra di salvataggio scrivi il nome <b>sfondo.jpg</b> per intero.<br>2) Nel repository crea la cartella img: <b>Add file</b> → <b>Create new file</b>, come nome scrivi" + K("img/LEGGIMI.md") + "e nel testo scrivi una parola qualsiasi, poi <b>Commit changes</b>. La barra / crea la cartella.<br>3) Clicca la cartella <b>img</b>, poi <b>Add file</b> → <b>Upload files</b>, trascina dentro <b>sfondo.jpg</b> e clicca <b>Commit changes</b>." + F("Nel repository c'è img/sfondo.jpg.") },
      { titolo: "6. PASSO 6: guarda il tuo sito su internet", testo: "1) Nel repository clicca <b>Settings</b> (in alto a destra, con l'ingranaggio) → a sinistra <b>Pages</b>.<br>2) In <b>Branch</b> deve esserci <b>main</b> e <b>/ (root)</b>. Se c'è scritto None, scegli <b>main</b> e clicca <b>Save</b>.<br>3) In alto nella stessa pagina compare l'indirizzo del sito, così:" + K("https://tuonome.github.io/nome-del-repository/") + "4) Aprilo. Le modifiche arrivano dopo 1 o 2 minuti: premi <b>Ctrl+F5</b> per ricaricare.<br>5) Clicca il menu: Home, Competenze, Passione. Si aprono tutte?" + F("Il tuo sito si apre su internet, con la foto di sfondo e il menu che funziona. Fallo vedere al compagno!") },
      { titolo: "7. Se qualcosa non va (succede a tutti, anche ai pro)", testo: "1) <b>Pagina bianca o errore 404</b> quando clicco il menu: il nome del file è sbagliato. Deve essere esattamente competenze.html o passione.html.<br>2) <b>Non vedo lo sfondo</b>: la foto non si chiama sfondo.jpg, oppure non è nella cartella img. Guarda la tabella in alto.<br>3) <b>Il sito non cambia</b>: aspetta 2 minuti e premi Ctrl+F5.<br>4) <b>Il sito è tutto senza colori</b>: manca style.css, oppure si chiama in un altro modo (Style.css, stile.css).<br>5) <b>I miei file sono in una sottocartella</b> (Mio-sito/…): il sito li cerca nella cartella principale. Dillo all'assistente: ti aiuta a spostarli." + F("Hai risolto da solo o con l'assistente.") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../3inf-oggi/', c: '#b45309' }, { t: 'I FILE PRONTI DA COPIARE', u: '../3inf-recupero/file.html', c: '#1a7f37' }, { t: 'HAI FINITO? Lezione di ieri: collaborazione e Pull Request', u: '?b=3inf-grafica-pr', c: '#6e40c9' }, { t: 'La pagina della classe: i siti di tutti', u: '../3inf-sito/', c: '#1f6feb' }, { t: 'Il monitor della lezione', u: '../3inf-monitor/', c: '#6e40c9' }],
    via: C("concetti", "Come si deve chiamare la Home del sito?", ["index.html", "home.html", "Index.HTML"], "Il browser apre da solo index.html."),
    prepara: [],
    allenamento: [
      S(1, C("concetti", "Che cosa fai oggi?", ["solo i passi che la tabella dice che mi mancano", "rifaccio tutto da capo", "niente"], "Quello che funziona non si tocca.")),
      S(2, C("pratica", "Passo 1: nel repository c'è index.html con il tuo nome?", ["sì", "ci sto lavorando", "non ancora"], "Tutte le risposte vanno bene: serve al monitor.")),
      S(3, C("concetti", "A che cosa serve style.css?", ["colori, sfondo e animazione di tutte le pagine", "a scrivere il testo", "a pubblicare il sito"], "HTML = il contenuto, CSS = l'aspetto.")),
      S(4, C("concetti", "Il menu porta a passione.html, ma il file si chiama passioni.html. Che cosa succede?", ["pagina bianca o errore 404", "funziona lo stesso", "il sito si cancella"], "Il nome deve essere identico.")),
      S(5, C("concetti", "Dove va la foto di sfondo?", ["nella cartella img, con il nome sfondo.jpg", "dove capita", "dentro index.html"], "Lo style.css la cerca in img/sfondo.jpg.")),
      S(6, C("pratica", "Passo 6: il tuo sito si apre su internet con lo sfondo?", ["sì", "si apre ma senza sfondo", "non ancora"], "Tutte le risposte vanno bene: serve al monitor."))
    ],
    crocette: [
      C("concetti", "La Home di un sito si chiama…", ["index.html", "home.html", "sito.html"], "", "index"),
      C("concetti", "Il file che dà i colori a tutte le pagine è…", ["style.css", "index.html", "img"], "", "css"),
      C("concetti", "Nel menu c'è il link a competenze.html. Il file si chiama comp.html. Che cosa succede?", ["errore 404: il file non viene trovato", "funziona", "si apre la Home"], "", "pagine"),
      C("concetti", "Nel CSS lo sfondo si mette con…", ["background-image: url(\"img/sfondo.jpg\")", "color: sfondo", "<img src=sfondo>"], "", "foto"),
      C("concetti", "Un'animazione nel CSS si scrive con…", ["@keyframes", "<animazione>", "background"], "", "css"),
      C("concetti", "Ho cambiato il sito ma su internet non vedo niente di nuovo. Che cosa faccio?", ["aspetto 1-2 minuti e premo Ctrl+F5", "cancello il repository", "rifaccio tutto"], "", "pages"),
      C("concetti", "Dove si accende GitHub Pages?", ["Settings → Pages → Branch main → Save", "Add file → Upload", "Code → Download"], "", "pages"),
      C("concetti", "Perché si scrive «Versione 1.0» in fondo alla Home?", ["per sapere quale versione del sito si sta guardando", "perché il browser lo chiede", "non serve"], "", "index")
    ],
    scale: [
      { area: "parere", q: "Quanto sei fiero, adesso, del tuo sito?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "pages", q: "Scrivi l'indirizzo del tuo sito (https://…github.io/…) e, con parole tue, che cosa hai sistemato oggi.", aiuto: "Almeno 15 parole. Scrivi tu, senza copiare.", min_parole: 15,
        criteri: "indirizzo github.io del proprio sito; descrizione con parole sue di cosa ha sistemato (file, nomi, foto, sfondo, Pages)" }
    ],
    recupero: [
      C("concetti", "La Home si chiama…", ["index.html", "home.html", "uno.html"], "", "index"),
      C("concetti", "La foto di sfondo va in…", ["img/sfondo.jpg", "il Desktop", "index.html"], "", "foto"),
      C("concetti", "Per vedere le modifiche premo…", ["Ctrl+F5", "Canc", "F9"], "", "pages")
    ]
  };
})();
