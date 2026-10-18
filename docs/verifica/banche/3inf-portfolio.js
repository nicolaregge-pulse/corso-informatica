// 3INF · Il mio sito diventa il mio portfolio (19/10/2026). Ripasso HTML/CSS/GitHub Pages, pratica sul proprio sito,
// verifica e recupero. Riparte dalla Dispensa 5 dell'8/10 (classe-3/sito-github), rimandata allora.
// Aree e peso nel giudizio: nozioni 40%, il tuo portfolio (saperlo raccontare) 40%, la pratica 20%.
// Lingua: italiano semplice con una riga di aiuto in bengalese (বাংলা) sotto schede e domande.
(function () {
  function L(it, bn) { return it + ' <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">' + bn + '</span>'; }
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">' + t.replace(/</g, '&lt;') + '</pre>'; }
  var PAG = '<!DOCTYPE html>\n<html lang="it">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>Cosa so fare</title>\n  <link rel="stylesheet" href="style.css">\n</head>\n<body>\n  <nav class="menu">\n    <a href="index.html">Home</a>\n    <a href="competenze.html">Cosa so fare</a>\n  </nav>\n  <h1>Cosa so fare</h1>\n  <div class="scheda">\n    <h2>Le mie competenze tecniche</h2>\n    <ul>\n      <li>Scrivo una pagina web in HTML</li>\n      <li>Cambio colori e stile con il CSS</li>\n      <li>Pubblico il mio sito su Internet con GitHub</li>\n      <li>Salvo ogni modifica con un commit</li>\n    </ul>\n    <h2>Le mie competenze personali</h2>\n    <ul>\n      <li>Quando mi blocco, chiedo aiuto</li>\n      <li>Se sbaglio, riprovo</li>\n      <li>Aiuto un compagno quando posso</li>\n    </ul>\n    <h2>Cosa ho imparato in questa scuola</h2>\n    <p>Qui ho imparato a ...</p>\n    <h2>La mia frase per un\'azienda</h2>\n    <p>Studio informatica. So creare e pubblicare un sito web. Imparo in fretta e non mi arrendo.</p>\n  </div>\n  <p class="piede">Sito creato da me - 2026</p>\n</body>\n</html>';
  var MENU = '  <nav class="menu">\n    <a href="index.html">Home</a>\n    <a href="competenze.html">Cosa so fare</a>\n  </nav>';
  var CSS = '.menu {\n  background: darkblue;\n  padding: 10px;\n  border-radius: 10px;\n}\n.menu a {\n  color: white;\n  text-decoration: none;\n  font-weight: bold;\n  margin: 0 12px;\n}\n.menu a:hover {\n  color: orange;\n}';

  window.BANCA = {
    id: "3inf-portfolio-v1",
    classe: "3INF",
    titolo: "Il mio sito diventa il mio portfolio",
    sotto: "3INF · 19/10/2026 · HTML, CSS, GitHub Pages · ripasso, pratica, verifica e recupero",
    stato: "stato/3inf-portfolio.json",
    risultati: "risultati.html?b=3inf-portfolio",
    minuti: 30,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Nozioni: HTML, CSS, GitHub Pages", peso: 40 },
      portfolio: { nome: "Il tuo portfolio: saperlo raccontare (solo parole tue)", peso: 40 },
      pratica: { nome: "La pratica sul tuo sito", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO ---------- */
    schede_temi: { sito: 1, html: 2, css: 3, pages: 4, portfolio: 5, codice: 6, menu: 7, pratica: 8, errori: 10 },
    schede: [
      { titolo: "1. Dove siamo: il tuo sito · ১. আমরা কোথায় আছি", testo: L(
        "Hai già un <b>sito pubblico</b> su Internet: lo hai fatto tu, dall'8 ottobre. Sta in un <b>repository</b> su GitHub (quasi tutti lo hanno chiamato <b>mio-sito</b>) e ha dentro almeno due file: <b>index.html</b> (la pagina) e <b>style.css</b> (i colori e lo stile). Chi ha fatto la Dispensa 4 ha anche una <b>seconda pagina</b> e un <b>menu</b> per passare da una pagina all'altra. L'indirizzo è <b>https://tuonome.github.io/mio-sito/</b>. Oggi il sito diventa il tuo <b>portfolio</b>: una pagina che dice <b>cosa sai fare</b>, da mostrare a un'azienda per lo stage.",
        "তোমার একটি ওয়েবসাইট আছে, GitHub-এ <b>mio-sito</b> নামে। আজ এটি তোমার <b>portfolio</b> হবে: কী কী পারো, কোম্পানিকে দেখানোর জন্য।") },
      { titolo: "2. Ripasso HTML: i mattoni della pagina · ২. HTML", testo: L(
        "<b>HTML</b> è la lingua delle pagine web. Ogni pezzo sta tra due <b>tag</b>: uno apre <code>&lt;p&gt;</code>, uno chiude <code>&lt;/p&gt;</code>. Quelli che usi tu:<br>" +
        "<code>&lt;h1&gt;</code> titolo grande · <code>&lt;h2&gt;</code> titolo piccolo · <code>&lt;p&gt;</code> paragrafo (un pezzo di testo) · <code>&lt;ul&gt;</code> elenco, con dentro un <code>&lt;li&gt;</code> per ogni riga · <code>&lt;a href=\"pagina.html\"&gt;Testo&lt;/a&gt;</code> link, cioè un collegamento a un'altra pagina · <code>&lt;div class=\"scheda\"&gt;</code> una scatola che raggruppa.<br>" +
        "La pagina ha una <b>testa</b> <code>&lt;head&gt;</code> (il titolo della scheda del browser e il collegamento al CSS) e un <b>corpo</b> <code>&lt;body&gt;</code> (tutto quello che si vede).",
        "HTML-এ প্রতিটি অংশ দুটি <b>tag</b>-এর মাঝে থাকে: <code>&lt;p&gt;</code> খোলে, <code>&lt;/p&gt;</code> বন্ধ করে। h1 বড় শিরোনাম, ul/li তালিকা, a href লিংক।") },
      { titolo: "3. Ripasso CSS: i colori e lo stile · ৩. CSS", testo: L(
        "Il <b>CSS</b> decide com'è fatta la pagina: colori, bordi, spazi. Sta nel file <b>style.css</b>, collegato alla pagina con la riga <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code> dentro head. Una regola CSS è fatta così:" + K('.menu {\n  background: darkblue;\n  padding: 10px;\n}') +
        "<b>.menu</b> è il <b>selettore</b>: dice <i>a chi</i> si applica (qui: a tutto quello che ha <code>class=\"menu\"</code>). Tra le graffe ci sono le <b>proprietà</b>: <code>background</code> il colore di sfondo, <code>padding</code> lo spazio interno, <code>color</code> il colore del testo, <code>border-radius</code> gli angoli arrotondati. Ogni proprietà finisce con <b>;</b>. Il punto davanti (<code>.menu</code>) vuol dire «classe».",
        "<b>CSS</b> পাতার রং আর স্টাইল ঠিক করে, ফাইল <b>style.css</b>-এ। <b>.menu</b> হলো selector (কাকে প্রযোজ্য), গোল বন্ধনীর ভিতরে property: background, padding, color।") },
      { titolo: "4. Ripasso GitHub Pages: come si pubblica · ৪. GitHub Pages", testo: L(
        "Il sito vive nel <b>repository</b> su github.com. Per cambiare un file: apri il file, clicca la <b>matita</b> (in alto a destra), scrivi, poi <b>Commit changes</b> due volte. Il <b>commit</b> è il salvataggio con la data e un messaggio: GitHub tiene tutta la storia. Per un file nuovo: <b>Add file → Create new file</b>, scrivi il nome, incolla, commit.<br>" +
        "Dopo il commit, <b>GitHub Pages</b> ricostruisce il sito: aspetta <b>1 minuto</b>, poi nel sito premi <b>Ctrl+F5</b> (ricarica senza memoria). Se vedi <b>404</b>, il nome del file non è quello che c'è scritto nel link: controlla maiuscole e minuscole, <b>competenze.html</b> tutto minuscolo.",
        "GitHub-এ ফাইল বদলাতে: ফাইল খোলো, <b>pencil</b> চাপো, লেখো, <b>Commit changes</b> দুইবার। ১ মিনিট পর সাইটে <b>Ctrl+F5</b>। <b>404</b> মানে ফাইলের নাম ভুল।") },
      { titolo: "5. Il portfolio: a cosa serve, e la regola d'oro · ৫. Portfolio", testo: L(
        "Un <b>portfolio</b> è la pagina che racconta <b>cosa sai fare</b>: le competenze <b>tecniche</b> (HTML, CSS, GitHub, Lazarus, montare un PC…) e quelle <b>personali</b> (chiedo aiuto quando mi blocco, se sbaglio riprovo, aiuto un compagno). È il tuo <b>biglietto da visita</b> per lo stage e per un colloquio: un'azienda lo apre e in 30 secondi capisce chi sei.<br>" +
        "<b>Regola d'oro (privacy):</b> la pagina è <b>pubblica</b>, la vede chiunque. Scrivi <b>solo cose vere e solo cose positive</b>, e solo il tuo <b>nome o soprannome</b>: niente cognome, telefono, indirizzo, classe, scuola, foto di altri. Le cose personali (difficoltà, famiglia, da dove vieni) <b>non</b> vanno sul sito: le scrivi nella verifica, che legge solo il prof.",
        "<b>Portfolio</b> = কী পারো তার পাতা: technical আর personal দক্ষতা। স্টেজ আর ইন্টারভিউর জন্য। <b>নিয়ম:</b> পাতা সবাই দেখে, তাই শুধু সত্য আর ভালো কথা, শুধু নাম বা ডাকনাম; ফোন, ঠিকানা, পরিবারের কথা নয়।") },
      { titolo: "6. Il codice: la pagina competenze.html · ৬. কোড", testo: L(
        "Questa è la pagina intera. Oggi la copi <b>da qui</b> dentro GitHub (il bottone in alto a destra del riquadro, oppure seleziona tutto e Ctrl+C). Poi la cambi con le <b>tue</b> cose vere." + K(PAG) +
        "Guarda com'è fatta: il <b>menu</b> in alto (nav) con due link, un <b>h1</b>, una <b>scheda</b> (div) con quattro <b>h2</b> e gli elenchi. La riga <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code> le dà gli stessi colori della tua Home.",
        "এই পুরো পাতাটি কপি করে GitHub-এ বসাও, তারপর নিজের সত্য কথা দিয়ে বদলাও।") },
      { titolo: "7. Il menu nella Home e i suoi colori · ৭. মেনু", testo: L(
        "Perché dalla Home si arrivi al portfolio, anche <b>index.html</b> deve avere il menu. Si mette <b>subito dopo</b> la riga <code>&lt;body&gt;</code>:" + K(MENU) +
        "Se hai già il menu della Dispensa 4, aggiungi solo la riga di <b>competenze.html</b>. Se hai anche <b>passione.html</b>, lascia anche quella.<br>Se il menu resta senza colori, in fondo a <b>style.css</b> ci va questo:" + K(CSS),
        "<b>index.html</b>-এও মেনু লাগবে, <code>&lt;body&gt;</code>-এর ঠিক পরে। মেনুতে রং না থাকলে <b>style.css</b>-এর শেষে এই কোড।") },
      { titolo: "8. LA PRATICA, passi 1-3: la pagina nuova su GitHub · ৮. অনুশীলন ১-৩", testo: L(
        "Un passo alla volta. Ogni passo è una cosa sola.<br>" +
        "1) Vai su <b>github.com</b>, entra, apri il tuo repository <b>mio-sito</b>.<br>" +
        "2) Clicca il bottone grigio <b>Add file</b> (in alto a destra, vicino al verde), poi <b>Create new file</b>. Nella casella del nome scrivi esattamente <b>competenze.html</b> (tutto minuscolo).<br>" +
        "3) Nel riquadro grande incolla la pagina della scheda 6 (Ctrl+V). Poi il bottone verde <b>Commit changes...</b>, poi di nuovo <b>Commit changes</b>. <b>FATTO!</b> Il file esiste.<br>" +
        "Rispondi alla domanda qui sotto: così il monitor sa che sei a questo punto.",
        "১) github.com → <b>mio-sito</b>। ২) <b>Add file → Create new file</b>, নাম <b>competenze.html</b>। ৩) কোড পেস্ট, <b>Commit changes</b> দুইবার।") },
      { titolo: "9. LA PRATICA, passi 4-6: fallo tuo e collega la Home · ৯. অনুশীলন ৪-৬", testo: L(
        "4) <b>Fallo tuo, solo cose vere.</b> Apri <b>competenze.html</b>, clicca la <b>matita</b>. Cambia gli elenchi: lascia solo le competenze che hai davvero, aggiungine di tue (una cosa che sai fare al PC, in Lazarus, con le mani…). Scrivi la frase «Qui ho imparato a …» e la <b>tua frase per un'azienda</b>. Commit.<br>" +
        "5) Apri <b>index.html</b>, matita. Subito dopo la riga <code>&lt;body&gt;</code> incolla il menu della scheda 7 (se c'è già, aggiungi solo la riga di competenze.html). Commit.<br>" +
        "6) Aspetta 1 minuto. Apri il tuo sito, <b>Ctrl+F5</b>. Clicca <b>Cosa so fare</b>, poi <b>Home</b>. <b>FATTO!</b> Il tuo portfolio è online. Copia l'indirizzo della pagina dalla barra del browser: ti serve per la verifica.",
        "৪) <b>competenze.html</b> → pencil → নিজের সত্য দক্ষতা লেখো → Commit। ৫) <b>index.html</b>-এ <code>&lt;body&gt;</code>-এর পরে মেনু → Commit। ৬) ১ মিনিট পর সাইট খোলো, <b>Ctrl+F5</b>। ঠিকানাটি কপি করো।") },
      { titolo: "10. Se qualcosa non va, e la sfida per chi ha finito · ১০. সমস্যা ও চ্যালেঞ্জ", testo: L(
        "<b>Vedo 404</b> cliccando «Cosa so fare»: il file deve chiamarsi esattamente <b>competenze.html</b>, minuscolo, come nel menu. <b>Il menu è senza colori</b>: in fondo a style.css incolla il CSS della scheda 7, aspetta un minuto, Ctrl+F5. <b>La scheda bianca non ha il bordo</b>: ti manca il CSS della Dispensa 3 (.scheda), lo trovi nella pagina della classe. <b>Non vedo le modifiche</b>: hai fatto il commit? Hai aspettato un minuto? Ctrl+F5?<br>" +
        "<b>Mostralo:</b> leggi al compagno la tua frase per un'azienda, come a un colloquio, 30 secondi.<br>" +
        "<b>Sfida per chi ha finito:</b> 1) una terza pagina <b>passione.html</b> (la cosa che ti piace di più) con la sua riga nel menu; 2) cambia un colore del menu e lo sfondo della scheda; 3) nella Home metti un link al portfolio anche in fondo alla pagina.<br>" +
        "Ti blocchi? Scrivi la domanda all'assistente, in fondo alla pagina: ti risponde.",
        "<b>404</b>: ফাইলের নাম <b>competenze.html</b> ছোট হাতের। মেনুতে রং নেই: style.css-এর শেষে CSS। শেষ করলে: <b>passione.html</b> তৃতীয় পাতা, রং বদলাও। আটকে গেলে নিচে সহকারীকে প্রশ্ন করো।") }
    ],
    strumenti: [{ t: 'Il mio punto: cosa mi manca (password del libro)', u: '../3inf-mio-punto/', c: '#d4a017' }, { t: 'La pagina della classe: i siti di tutti', u: '../3inf-sito/', c: '#1f6feb' }, { t: 'Il monitor della lezione', u: '../3inf-monitor/', c: '#6e40c9' }],
    via: C("nozioni", L("Il tuo sito su Internet ha l'indirizzo che comincia con…", "তোমার সাইটের ঠিকানা শুরু হয়…"), ["https://tuonome.github.io/", "https://classroom.google.com/", "https://lazarus.it/"], "Il sito pubblico sta su GitHub Pages."),
    prepara: [
      { q: L("Prima e dopo: scrivi almeno 3 cose che oggi sai fare e a settembre no (per esempio: ho un account GitHub, il mio sito è su Internet, so cos'è un commit…).", "আগে আর এখন: ৩টি জিনিস যা এখন পারো, সেপ্টেম্বরে পারতে না।"), min: 15 },
      { q: L("Una cosa che hai imparato in questa scuola e che, secondo te, da un'altra parte non avresti imparato. Anche non di informatica.", "এই স্কুলে শেখা একটি জিনিস, যা অন্য কোথাও শিখতে না।"), min: 12 }
    ],
    allenamento: [
      S(1, C("nozioni", L("Il file con la pagina principale del tuo sito si chiama…", "প্রধান পাতার ফাইল…"), ["index.html", "style.css", "pagina.txt"], "index = la pagina d'ingresso.")),
      S(2, C("nozioni", L("Per fare un elenco con tante righe si usa…", "তালিকার জন্য…"), ["<ul> con dentro un <li> per riga", "<h1> per ogni riga", "<p> con le virgole"], "ul = elenco, li = riga.")),
      S(2, C("nozioni", L("<code>&lt;a href=\"competenze.html\"&gt;Cosa so fare&lt;/a&gt;</code> è…", "এটি কী?"), ["un link alla pagina competenze.html", "un titolo", "un colore"], "a = link, href = dove porta.")),
      S(3, C("nozioni", L("In <code>.menu { background: darkblue; }</code>, <b>.menu</b> è…", "<b>.menu</b> কী?"), ["il selettore: a chi si applica la regola", "il colore", "il nome del file"], "Il punto davanti vuol dire classe.")),
      S(3, C("nozioni", L("La riga che collega la pagina al file dei colori è…", "CSS যুক্ত করার লাইন…"), ["<link rel=\"stylesheet\" href=\"style.css\">", "<a href=\"style.css\">", "<p>style.css</p>"], "Sta dentro head.")),
      S(4, C("nozioni", L("Dopo il commit, per vedere la modifica sul sito…", "Commit-এর পর…"), ["aspetto 1 minuto e premo Ctrl+F5", "spengo il PC", "faccio un altro repository"], "GitHub Pages ricostruisce il sito.")),
      S(4, C("nozioni", L("Clicco «Cosa so fare» e vedo 404. Il motivo più probabile:", "404 কেন?"), ["il nome del file non è esattamente competenze.html", "Internet è spento", "manca il CSS"], "404 = pagina non trovata.")),
      S(5, C("nozioni", L("Nel portfolio, che è pubblico, scrivo…", "Portfolio-তে লিখি…"), ["solo cose vere e positive, solo nome o soprannome", "il mio telefono così mi chiamano", "le mie difficoltà in famiglia"], "La pagina la vede chiunque.")),
      S(8, C("pratica", L("Passi 1-3 fatti? Dopo il commit, nel repository mio-sito vedi…", "ধাপ ১-৩ শেষ? Repository-তে দেখো…"), ["il file competenze.html nell'elenco dei file", "una pagina 404", "il file style.css cancellato"], "Se non lo vedi, rifai il passo 2.")),
      S(9, C("pratica", L("Passi 4-6 fatti? Sul sito, cliccando «Cosa so fare» vedi…", "ধাপ ৪-৬ শেষ? সাইটে দেখো…"), ["la pagina con le mie competenze, con il menu in alto", "ancora la pagina di esempio del prof, uguale", "niente, il sito non si apre"], "Se è ancora l'esempio: passo 4, fallo tuo.")),
      S(10, C("pratica", L("Hai fatto la sfida? Che cosa hai aggiunto?", "চ্যালেঞ্জ করেছো?"), ["una terza pagina o un colore nuovo", "niente, ho finito ai passi 1-6", "ho cancellato il sito"], "Tutte le risposte vanno bene: serve al monitor."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("nozioni", L("Il tag che apre un paragrafo di testo è…", "অনুচ্ছেদের tag…"), ["<p>", "<ul>", "<link>"], "", "html"),
      C("nozioni", L("<code>&lt;h2&gt;Le mie competenze&lt;/h2&gt;</code> mostra…", "এটি দেখায়…"), ["un titolo piccolo", "un link", "un elenco"], "", "html"),
      C("nozioni", L("In un elenco, ogni riga sta in un…", "তালিকার প্রতিটি লাইন…"), ["<li>", "<h1>", "<div>"], "", "html"),
      C("nozioni", L("<code>href</code> dentro un link dice…", "href বলে…"), ["dove porta il link", "il colore del link", "la grandezza del testo"], "", "html"),
      C("nozioni", L("Le regole CSS del tuo sito stanno nel file…", "CSS নিয়ম থাকে…"), ["style.css", "index.html", "competenze.html"], "", "css"),
      C("nozioni", L("<code>.menu a:hover { color: orange; }</code> fa diventare arancione…", "এটি কমলা করে…"), ["il link del menu quando il mouse ci passa sopra", "tutto lo sfondo", "il titolo h1"], "", "css"),
      C("nozioni", L("Ogni proprietà CSS finisce con…", "প্রতিটি property শেষ হয়…"), [";", ".", "!"], "", "css"),
      C("nozioni", L("Il commit è…", "Commit হলো…"), ["il salvataggio di una modifica, con data e messaggio", "la cancellazione del sito", "un colore"], "", "pages"),
      C("nozioni", L("Per creare un file nuovo nel repository si usa…", "নতুন ফাইল…"), ["Add file → Create new file", "la matita su index.html", "Ctrl+F5"], "", "pages"),
      C("nozioni", L("Dopo una modifica non vedo niente di nuovo sul sito. Prima cosa da fare:", "পরিবর্তন দেখছি না। প্রথমে…"), ["aspettare un minuto e premere Ctrl+F5", "cancellare il repository", "cambiare browser"], "", "pages"),
      C("nozioni", L("Sul portfolio pubblico NON scrivo…", "পাবলিক পাতায় লিখি না…"), ["il mio telefono e il mio indirizzo", "le mie competenze tecniche", "la mia frase per un'azienda"], "", "portfolio"),
      C("nozioni", L("Il portfolio serve a…", "Portfolio-র কাজ…"), ["far vedere a un'azienda cosa so fare", "giocare", "scrivere i voti"], "", "portfolio")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti capace, adesso, di aggiungere una pagina al tuo sito da solo?", "এখন একা একটি পাতা যোগ করতে কতটা পারো?"), basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: L("Quanto sei fiero della tua pagina «Cosa so fare»?", "নিজের পাতা নিয়ে কতটা গর্বিত?"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "pratica", tema: "pratica", incolla: true, q: L("Incolla qui l'indirizzo della tua pagina «Cosa so fare» (comincia con https:// e finisce con competenze.html).", "তোমার পাতার ঠিকানা এখানে পেস্ট করো।"), aiuto: "Copialo dalla barra del browser e incolla (Ctrl+V). Se la pagina non è ancora online, scrivi: non ancora online, e il motivo.", min_parole: 1,
        criteri: "indirizzo https://<utente>.github.io/<repo>/competenze.html; se manca, il motivo" },
      { area: "portfolio", tema: "portfolio", q: L("Racconta il tuo portfolio: quali competenze hai scritto (tecniche e personali) e perché proprio quelle. Qual è la tua frase per un'azienda?", "তোমার portfolio বলো: কোন দক্ষতা লিখেছো আর কেন। কোম্পানির জন্য তোমার বাক্য কী?"), aiuto: "Almeno 30 parole. Scrivi tu, senza copiare.", min_parole: 30,
        criteri: "competenze vere, tecniche e personali, con un perché; la frase per l'azienda; parole sue" },
      { area: "portfolio", tema: "scuola", q: L("Che cosa hai imparato in questa scuola che da un'altra parte non avresti imparato? Qui lo legge solo il prof: puoi scrivere anche le cose personali.", "এই স্কুলে কী শিখেছো যা অন্য কোথাও শিখতে না? এটি শুধু শিক্ষক পড়েন।"), aiuto: "Almeno 20 parole, sincere.", min_parole: 20,
        criteri: "risposta personale e sincera; non si valuta il contenuto, si valuta che ci sia" },
      { area: "nozioni", tema: "html", q: L("Spiega con parole tue che cosa fanno queste tre righe: <code>&lt;nav class=\"menu\"&gt;</code>, <code>&lt;a href=\"index.html\"&gt;Home&lt;/a&gt;</code>, <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code>.", "এই তিন লাইন কী করে, নিজের ভাষায় বলো।"), aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "nav = la scatola del menu con la classe menu; a href = link alla Home; link stylesheet = collega il CSS" },
      { area: "pratica", tema: "errori", q: L("Racconta un problema che hai avuto oggi (o un compagno) e come l'avete risolto. Se non ne hai avuti, racconta che cosa controlleresti se vedessi 404.", "আজ কী সমস্যা হয়েছিল, কীভাবে সমাধান করেছো?"), aiuto: "Almeno 15 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 15,
        criteri: "problema concreto (404, menu senza colori, commit dimenticato, Ctrl+F5) e la soluzione" },
      { area: "parere", tema: "retro", q: L("Che cosa ti è servito di più oggi, e che cosa cambieresti?", "আজ কী সবচেয়ে কাজে লেগেছে, কী বদলাতে?"), aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("nozioni", L("Il tag per un titolo grande è…", "বড় শিরোনাম…"), ["<h1>", "<li>", "<css>"], "", "html"),
      C("nozioni", L("Un elenco si fa con…", "তালিকা…"), ["<ul> e <li>", "<p> e <a>", "<head> e <body>"], "", "html"),
      C("nozioni", L("<code>&lt;a href=\"index.html\"&gt;Home&lt;/a&gt;</code> porta…", "এটি নিয়ে যায়…"), ["alla pagina index.html", "a Google", "al file CSS"], "", "html"),
      C("nozioni", L("I colori del sito stanno in…", "রং থাকে…"), ["style.css", "index.html", "GitHub"], "", "css"),
      C("nozioni", L("<code>background: darkblue;</code> cambia…", "এটি বদলায়…"), ["il colore di sfondo", "la grandezza del testo", "il nome del file"], "", "css"),
      C("nozioni", L("Per salvare una modifica su GitHub premo…", "সেভ করতে…"), ["Commit changes", "Ctrl+F5", "404"], "", "pages"),
      C("nozioni", L("Ctrl+F5 serve a…", "Ctrl+F5…"), ["ricaricare la pagina senza memoria, per vedere le novità", "cancellare il sito", "fare il commit"], "", "pages"),
      C("nozioni", L("Nel portfolio pubblico metto…", "পাবলিক portfolio-তে…"), ["solo cose vere e positive", "il numero di telefono", "la foto di un compagno"], "", "portfolio"),
      C("nozioni", L("Il nome giusto del file del portfolio è…", "ফাইলের সঠিক নাম…"), ["competenze.html", "Competenze.HTML", "competenze"], "", "pages")
    ]
  };
})();
