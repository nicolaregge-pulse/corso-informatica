// 3INF · Ripasso, verifica e recupero su: versioni e numeri, fork, ramo, Pull Request, merge, changelog, backlog con i pesi,
// Agile (Manifesto, sprint, retrospettiva), perché un programma cambia, rispetto del lavoro degli altri, privacy.
// Il gioco: «Il treno blindato della 3INF» (fork del 08/10, v1.0-v1.4 dalle PR #1-#21; dal 14/10 v1.5+ dalle 14 richieste del 12/10).
// Aree e peso nel giudizio: nozioni 30%, metodo e regole 30%, esperienza personale 30%, dati 10%.
// Lingua: italiano semplice con una riga di aiuto in bengalese (বাংলা) sotto domande, schede e istruzioni.
// Le opzioni delle crocette e le spiegazioni restano solo in italiano: il motore le mostra come testo semplice.
(function () {
  // riga di aiuto in bengalese: sotto il testo italiano, sinistra-destra, colore attenuato
  function L(it, bn) { return it + ' <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">' + bn + '</span>'; }
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  // richieste (Pull Request) arrivate ogni quarto d'ora lunedì 12/10 (dal backlog della 3INF: 14 in tutto)
  var QUARTI = [["10:15", 2], ["10:30", 11], ["10:45", 1]];

  window.BANCA = {
    id: "3inf-versioning-20261014",
    classe: "3INF",
    titolo: "Versioni, Pull Request e il treno della 3INF",
    sotto: "3INF · 14/10/2026 · ripasso, verifica e recupero",
    stato: "stato/3inf-versioning.json",
    risultati: "risultati.html?b=3inf-versioning",
    backlog: "../3inf-backlog/backlog.json",        // per la parte personale: le richieste vere di lunedì 12/10
    modulo: "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform",
    minuti: 30,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Nozioni: versioni, fork, ramo, Pull Request, merge, changelog", peso: 30 },
      sistema: { nome: "Il metodo: backlog, Agile, regole della squadra e privacy", peso: 30 },
      personale: { nome: "La tua esperienza (solo parole tue)", peso: 30 },
      dati: { nome: "Leggere i dati della lezione", peso: 10 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    quarti: QUARTI,

    /* ---------- RIPASSO ---------- */
    schede_temi: { versione: 1, numeri: 1, changelog: 1, cambia: 1, fork: 2, ramo: 2, merge: 2, pr: 3, backlog: 4, agile: 5, regole: 6, privacy: 6 },
    schede: [
      { titolo: "1. Le versioni e il changelog · ১. সংস্করণ ও changelog", testo: L(
        "Una <b>versione</b> è un salvataggio del gioco con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Il numero ha due parti: <b>major.minor</b>. Da v1.4 a v1.5 cambia il numero dopo il punto: è un passo piccolo, <b>minor</b>. Da v1.5 a v2.0 cambia il primo numero: è un cambio grande, <b>major</b> (per esempio un motore nuovo). Il <b>changelog</b> è il registro di tutte le modifiche, versione per versione: che cosa è cambiato e da quale richiesta. Un programma <b>cambia</b> perché chi lo usa chiede cose nuove e perché si trovano <b>difetti</b> da sistemare: nella v1.4 Dani e Ale hanno trovato che il cielo cambiava in ritardo, ed è stato sistemato.",
        "<b>সংস্করণ</b> মানে খেলার একটি সেভ: একটি <b>নম্বর</b> আর কী বদলেছে তার একটি লাইন। নম্বরের দুই অংশ: <b>major.minor</b>। v1.4 থেকে v1.5: ছোট পরিবর্তন (<b>minor</b>)। v1.5 থেকে v2.0: বড় পরিবর্তন (<b>major</b>)। <b>changelog</b> হলো সব পরিবর্তনের তালিকা। প্রোগ্রাম বদলায়, কারণ মানুষ নতুন জিনিস চায় আর ভুল ঠিক করতে হয়।") },
      { titolo: "2. Fork, ramo e merge · ২. fork, শাখা ও merge", testo: L(
        "L'08/10 la 3INF ha fatto il suo <b>fork</b>: una <b>copia</b> del treno della 2INF (versione v0.11), per lavorarci senza toccare il gioco della 2INF. Da lì è partita la v1.0 della 3INF. Un <b>ramo</b> (branch) è una strada di lavoro parallela nello stesso progetto. Il <b>merge</b> unisce una modifica (o un ramo) dentro il gioco: lo fa il prof quando accetta una Pull Request.",
        "০৮/১০ তারিখে 3INF <b>fork</b> করেছে: 2INF-এর ট্রেন খেলার একটি <b>কপি</b> (v0.11), যাতে ওদের খেলা না বদলায়। <b>শাখা</b> (branch) মানে একই প্রজেক্টে পাশাপাশি আরেকটি কাজের রাস্তা। <b>merge</b> মানে একটি পরিবর্তন খেলার সাথে যোগ করা: শিক্ষক Pull Request গ্রহণ করলে এটা করেন।") },
      { titolo: "3. La Pull Request · ৩. Pull Request", testo: L(
        "Una <b>Pull Request</b> (PR) è una <b>richiesta di modifica scritta</b>. Ha quattro parti: <b>Titolo</b>, <b>Cosa cambia</b>, <b>Dove</b> (in quale punto del gioco), <b>Perché</b>. L'08/10 le squadre SCENARI, PERSONAGGI, MOTORE FISICA e TEST QUALITÀ hanno mandato le PR dalla #1 alla #21: da quelle sono nate le versioni dalla v1.1 alla v1.4. Lunedì 12/10 sono arrivate 14 richieste: da queste nascono oggi le versioni nuove, dalla v1.5 in poi.",
        "<b>Pull Request</b> (PR) মানে লিখিত একটি পরিবর্তনের অনুরোধ। এর চারটি অংশ: <b>শিরোনাম</b>, <b>কী বদলাবে</b>, <b>কোথায়</b>, <b>কেন</b>। ০৮/১০-এ দলগুলো PR #1 থেকে #21 পাঠিয়েছে: তা থেকে v1.1 থেকে v1.4 হয়েছে। ১২/১০-এ ১৪টি অনুরোধ এসেছে: আজ তা থেকে v1.5 আর পরের সংস্করণ হচ্ছে।") },
      { titolo: "4. Il backlog e i pesi · ৪. backlog ও ওজন", testo: L(
        "Il <b>backlog</b> è la coda dei lavori: tutte le richieste, in ordine. Ogni richiesta ha un <b>peso</b>: quanto lavoro serve sul codice. I pesi sono i numeri di <b>Fibonacci</b>: 1, 2, 3, 5, 8 (ogni numero è la somma dei due prima). 1 = un colore, 2 = un numero nelle regole, 3 = un personaggio, 5 = un ambiente, 8 = due cose insieme o una regola nuova. Si fanno prima le richieste più leggere; a parità di peso, chi è arrivato prima.",
        "<b>backlog</b> মানে কাজের সারি: সব অনুরোধ, ক্রম অনুযায়ী। প্রতিটি অনুরোধের একটি <b>ওজন</b> আছে: কোডে কত কাজ লাগবে। ওজন হলো Fibonacci সংখ্যা: ১, ২, ৩, ৫, ৮ (প্রতিটি আগের দুইটির যোগফল)। ১ = একটি রং, ২ = একটি সংখ্যা, ৩ = একটি চরিত্র, ৫ = একটি পরিবেশ, ৮ = দুইটি জিনিস একসাথে। আগে হালকা কাজ হয়।") },
      { titolo: "5. Agile: sprint e retrospettiva · ৫. Agile: sprint ও retrospettiva", testo: L(
        "<b>Agile</b> è un modo di lavorare delle aziende di software. Il <b>Manifesto Agile</b> dice, per esempio: un programma che <b>funziona</b> conta più di tanti documenti; <b>rispondere ai cambiamenti</b> conta più che seguire un piano fisso; le <b>persone</b> e il parlarsi contano più degli strumenti. Si lavora a <b>sprint</b>: giri di lavoro brevi, con un obiettivo, alla fine dei quali esce una versione che funziona. Alla fine dello sprint c'è la <b>retrospettiva</b>: la squadra dice che cosa è andato bene e che cosa migliorare.",
        "<b>Agile</b> হলো সফটওয়্যার কোম্পানির কাজের একটি পদ্ধতি। <b>Agile Manifesto</b> বলে: চালু প্রোগ্রাম অনেক কাগজের চেয়ে বেশি জরুরি; পরিবর্তনে সাড়া দেওয়া নির্দিষ্ট পরিকল্পনার চেয়ে বেশি জরুরি; মানুষ আর কথা বলা যন্ত্রের চেয়ে বেশি জরুরি। কাজ হয় <b>sprint</b>-এ: ছোট কাজের পালা, একটি লক্ষ্য, শেষে একটি চালু সংস্করণ। শেষে <b>retrospettiva</b>: দল বলে কী ভালো হয়েছে আর কী ভালো করা যায়।") },
      { titolo: "6. Le regole della squadra · ৬. দলের নিয়ম", testo: L(
        "Il gioco è di <b>tutta la classe</b>. Regola: <b>aggiungere sì, cancellare no</b>. Il cattivo Travor l'ha chiesto Tomas: se hai un'idea, aggiungi un personaggio tuo, non cancelli quello di un compagno. Il gioco è <b>pubblico</b>: lo vede chiunque su Internet. Per questo <b>niente foto di persone vere</b> (privacy): lunedì 3 richieste sono state respinte per questo motivo. Si possono rimandare con un personaggio disegnato o di un videogioco.",
        "খেলাটি <b>পুরো ক্লাসের</b>। নিয়ম: <b>যোগ করা যায়, মুছে ফেলা যায় না</b>। Travor চরিত্রটি Tomas চেয়েছিল: তোমার নতুন ধারণা থাকলে নিজের চরিত্র যোগ করো, বন্ধুরটা মুছে ফেলো না। খেলাটি ইন্টারনেটে <b>সবাই দেখতে পায়</b>। তাই <b>আসল মানুষের ছবি নয়</b> (গোপনীয়তা): সোমবার এই কারণে ৩টি অনুরোধ বাতিল হয়েছে। আঁকা চরিত্র বা ভিডিও গেমের চরিত্র দিয়ে আবার পাঠানো যায়।") }
    ],
    strumenti: [
      { t: 'Il treno della 3INF', u: '../giochi/treno-3inf/', c: '#1a7f37' },
      { t: 'Le versioni del treno', u: '../giochi/treno-3inf/versioni/', c: '#1f6feb' },
      { t: 'Il backlog della 3INF', u: '../3inf-backlog/', c: '#6e40c9' }
    ],
    via: C("nozioni", L("Come chiedevate una modifica al treno della 3INF?", "3INF-এর ট্রেনে পরিবর্তন কীভাবে চাইতে?"),
      ["con una Pull Request scritta", "scrivendo il codice da soli", "chiedendolo a voce al prof"],
      "Esatto: una richiesta di modifica scritta. Dalle vostre Pull Request sono nate le versioni del treno."),
    prepara: [
      { q: L("Racconta una tua richiesta (dell'08/10 o di lunedì 12/10) con parole diverse da quelle che hai scritto, e perché l'hai fatta.", "তোমার একটি অনুরোধের কথা বলো (০৮/১০ বা ১২/১০), নতুন কথায়, আর কেন চেয়েছিলে।"),
        aiuto: L("Le richieste di lunedì le vedi qui sopra; quelle dell'08/10 sono nel changelog del treno.", "সোমবারের অনুরোধ উপরে আছে; ০৮/১০-এরগুলো ট্রেনের changelog-এ।"), min: 15 },
      { q: L("Una cosa che hai imparato lavorando come in un'azienda di software: squadre, Pull Request, versioni.", "সফটওয়্যার কোম্পানির মতো কাজ করে তুমি কী শিখেছ: দল, Pull Request, সংস্করণ।"), min: 15 }
    ],
    allenamento: [
      S(1, C("nozioni", L("Se il treno passasse a un motore nuovo, il numero diventerebbe v2.0. È un cambio…", "নতুন ইঞ্জিনে গেলে নম্বর হবে v2.0। এটা কোন পরিবর্তন?"),
        ["grande (major)", "piccolo (minor)"], "Cambia il primo numero: cambio grande.")),
      S(2, C("nozioni", L("Chi fa il merge di una Pull Request nel treno?", "ট্রেনে Pull Request-এর merge কে করে?"),
        ["il prof, quando accetta la Pull Request", "chiunque, senza chiedere", "il gioco, da solo"], "Il prof controlla e unisce la modifica al gioco.")),
      S(3, C("sistema", L("Una PR dice solo «cambiate il treno». Che cosa manca?", "একটি PR-এ শুধু লেখা «ট্রেন বদলাও»। কী নেই?"),
        ["Cosa cambia di preciso, Dove e Perché", "niente, va bene così", "il nome del prof"], "Senza «Dove» e «Perché» chi scrive il codice non sa cosa fare.")),
      S(4, C("sistema", L("Nel backlog ci sono «cielo grigio» (peso 1) e «lo stadio con un personaggio» (peso 8). Quale si fa prima?", "backlog-এ আছে «ধূসর আকাশ» (ওজন ১) আর «স্টেডিয়াম ও চরিত্র» (ওজন ৮)। কোনটা আগে হবে?"),
        ["il cielo grigio: pesa meno", "lo stadio: è più bello", "tutte e due insieme"], "Prima le richieste più leggere: il gioco migliora subito.")),
      S(5, C("sistema", L("Alla fine dello sprint la squadra dice che cosa è andato bene e che cosa migliorare. Come si chiama?", "sprint-এর শেষে দল বলে কী ভালো হয়েছে আর কী ভালো করা যায়। এর নাম কী?"),
        ["retrospettiva", "fork", "changelog"], "Retrospettiva = guardarsi indietro per migliorare.")),
      S(6, C("sistema", L("Vuoi usare la foto di un tuo amico per un personaggio. Va bene nel gioco pubblico?", "বন্ধুর ছবি দিয়ে চরিত্র বানাতে চাও। সবার খেলায় এটা চলবে?"),
        ["no: niente foto di persone vere, uso un personaggio disegnato", "sì, sempre", "sì, se la foto è bella"], "Il gioco lo vede chiunque: i volti veri restano fuori (privacy)."))
    ],

    /* ---------- VERIFICA ---------- */
    crocette: [
      C("nozioni", L("Una versione del gioco è…", "খেলার একটি সংস্করণ হলো…"),
        ["un salvataggio con un numero e la riga di cosa cambia", "una copia di riserva senza nome", "un errore del gioco"], "Ogni versione ha un numero e una riga che dice cosa cambia.", "versione"),
      C("nozioni", L("Da v1.4 a v1.5 il cambio è…", "v1.4 থেকে v1.5: পরিবর্তনটি…"),
        ["piccolo (minor)", "grande (major)"], "Cambia il numero dopo il punto: passo piccolo.", "numeri"),
      C("nozioni", L("Nel changelog della v1.3 c'è scritto: «PR #12 di Eric: il cattivo Franciscos». Che cosa ti dice questa riga?", "v1.3-এর changelog-এ লেখা: «PR #12, Eric: খলনায়ক Franciscos»। এই লাইন কী বলে?"),
        ["quale modifica è entrata, in quale versione e da quale richiesta", "il voto di Eric", "il codice intero del gioco"], "Il changelog è il registro delle modifiche, versione per versione.", "changelog"),
      C("nozioni", L("L'08/10 la 3INF ha fatto una copia del treno della 2INF, per lavorarci senza toccare il loro. Come si chiama questa copia?", "০৮/১০-এ 3INF 2INF-এর ট্রেনের একটি কপি বানিয়েছে, ওদের খেলা না বদলে কাজ করতে। এই কপির নাম কী?"),
        ["fork", "merge", "changelog"], "Fork = copia di un progetto, per lavorarci per conto proprio.", "fork"),
      C("nozioni", L("Un ramo (branch) è…", "শাখা (branch) হলো…"),
        ["una strada di lavoro parallela nello stesso progetto", "una versione cancellata", "un errore del codice"], "Sul ramo si lavora senza rompere il gioco principale.", "ramo"),
      C("nozioni", L("Il prof accetta la tua Pull Request e unisce la modifica al gioco. Come si chiama?", "শিক্ষক তোমার Pull Request গ্রহণ করে পরিবর্তনটি খেলার সাথে যোগ করেন। এর নাম কী?"),
        ["merge", "fork", "backlog"], "Merge = unire.", "merge"),
      C("nozioni", L("Una Pull Request scritta bene ha quattro parti:", "ভালোভাবে লেখা Pull Request-এর চারটি অংশ:"),
        ["Titolo, Cosa cambia, Dove, Perché", "Nome, Cognome, Classe, Data", "Inizio, Svolgimento, Fine, Firma"], "Senza «Dove» e «Perché» chi scrive il codice non sa cosa fare.", "pr"),
      C("nozioni", L("Nella v1.4 Dani e Ale hanno trovato un difetto: il cielo cambiava in ritardo. Che cosa è successo dopo?", "v1.4-এ Dani আর Ale একটি ভুল খুঁজে পেয়েছে: আকাশ দেরিতে বদলাত। তারপর কী হয়েছে?"),
        ["il difetto è stato sistemato ed è entrato in una versione", "hanno ricominciato il gioco da zero", "niente: i difetti non si sistemano"], "Un programma cambia per le idee nuove e per sistemare i difetti.", "cambia"),
      C("sistema", L("Lunedì una richiesta chiedeva due cose insieme: un personaggio nuovo (peso 3) e lo stadio come ambiente nuovo (peso 5). Quanto pesa nel backlog?", "সোমবার একটি অনুরোধে দুইটি জিনিস ছিল: নতুন চরিত্র (ওজন ৩) আর নতুন পরিবেশ স্টেডিয়াম (ওজন ৫)। backlog-এ এর ওজন কত?"),
        ["8", "5", "3"], "3 + 5 = 8: è anche il numero di Fibonacci che viene dopo il 5.", "backlog"),
      C("sistema", L("Il Manifesto Agile dice che conta di più…", "Agile Manifesto অনুযায়ী বেশি জরুরি…"),
        ["un programma che funziona, più di tanti documenti", "seguire il piano senza cambiarlo mai", "scrivere tutto prima di cominciare"], "Software che funziona più della documentazione; rispondere ai cambiamenti più che seguire un piano.", "agile"),
      C("sistema", L("Vuoi cambiare il cattivo Travor, che ha chiesto Tomas. Che cosa fai?", "তুমি Travor (Tomas-এর চাওয়া চরিত্র) বদলাতে চাও। কী করবে?"),
        ["chiedo un personaggio nuovo mio e lascio Travor com'è", "cancello Travor e metto il mio", "cambio Travor senza dirlo a nessuno"], "Aggiungere sì, cancellare no: si rispetta il lavoro degli altri.", "regole"),
      C("sistema", L("Lunedì 3 richieste sono state respinte. Perché?", "সোমবার ৩টি অনুরোধ বাতিল হয়েছে। কেন?"),
        ["avevano la foto di una persona vera, e il gioco è pubblico (privacy)", "erano scritte male", "erano arrivate tardi"], "Nel gioco pubblico niente volti veri: si rimanda con un personaggio disegnato o di un videogioco.", "privacy")
    ],
    dati: [
      { tipo: "c", area: "dati", tema: "grafico", q: L("Guarda il grafico: in quale quarto d'ora sono arrivate più richieste lunedì?", "গ্রাফ দেখো: সোমবার কোন পনেরো মিনিটে সবচেয়ে বেশি অনুরোধ এসেছে?"),
        o: ["10:30", "10:15", "10:45"], a: 0, spiega: "Tra le 10:30 e le 10:45 ne sono arrivate 11.", grafico: true },
      { tipo: "n", area: "dati", tema: "grafico", q: L("Sempre dal grafico: quante richieste in tutto lunedì (somma delle tre barre)?", "গ্রাফ থেকে: সোমবার মোট কতটি অনুরোধ (তিনটি দাগের যোগফল)?"),
        giusto: 14, spiega: "2 + 11 + 1 = 14.", grafico: true }
    ],
    scale: [
      { area: "personale", q: L("Quanto ti è piaciuto lavorare così, con Pull Request, backlog e versioni?", "Pull Request, backlog আর সংস্করণ দিয়ে কাজ তোমার কতটা ভালো লেগেছে?"), basso: "per niente · একদম না", alto: "moltissimo · খুব বেশি" },
      { area: "personale", q: L("Quanto ti piace il treno della 3INF, com'è adesso?", "3INF-এর ট্রেন এখন যেমন আছে, তোমার কতটা ভালো লাগে?"), basso: "per niente · একদম না", alto: "moltissimo · খুব বেশি" },
      { area: "parere", q: L("Quanto ti è piaciuta questa verifica?", "এই পরীক্ষা তোমার কতটা ভালো লেগেছে?"), basso: "per niente · একদম না", alto: "moltissimo · খুব বেশি", ultima: true }
    ],
    aperte: [
      { area: "sistema", tema: "direttore", q: L("Spiega come al direttore della scuola che cosa ha fatto la 3INF con il treno, dal fork alle versioni nuove. Usa le parole fork, Pull Request, backlog, merge, versione e changelog.", "স্কুলের পরিচালককে বোঝাও 3INF ট্রেন খেলা দিয়ে কী করেছে, fork থেকে নতুন সংস্করণ পর্যন্ত। এই শব্দগুলো ব্যবহার করো: fork, Pull Request, backlog, merge, সংস্করণ, changelog।"),
        aiuto: L("Almeno 40 parole. Frasi semplici, in ordine: prima, poi, alla fine.", "কমপক্ষে ৪০টি শব্দ। সহজ বাক্য, ক্রম অনুযায়ী: প্রথমে, তারপর, শেষে।"), min_parole: 40,
        criteri: "in ordine: fork dal treno della 2INF, PR con Titolo/Cosa/Dove/Perché, backlog con i pesi, merge del prof, versione nuova, changelog; usa le parole giuste; parole sue." },
      { area: "personale", tema: "mia-pr", mostra_pr: true, q: L("La tua Pull Request: che cosa chiedevi, dove e perché? È entrata nel gioco o è stata respinta? Se la riscrivessi oggi, come la scriveresti meglio?", "তোমার Pull Request: কী চেয়েছিলে, কোথায় আর কেন? খেলায় যোগ হয়েছে না বাতিল হয়েছে? আজ আবার লিখলে কীভাবে আরও ভালো লিখবে?"),
        aiuto: L("Almeno 40 parole. Le richieste qui sopra servono solo per ricordare: non ricopiarle, racconta. Se la tua è dell'08/10, pensa al changelog del treno. Se non ne hai mandata una, racconta quella che manderesti.", "কমপক্ষে ৪০টি শব্দ। উপরের অনুরোধগুলো শুধু মনে করার জন্য: কপি কোরো না, নিজের কথায় বলো। অনুরোধ না পাঠিয়ে থাকলে, কোনটা পাঠাতে চাও সেটা বলো।"), min_parole: 40,
        criteri: "richiesta precisa e vera (cosa, dove, perché); sa se è entrata o respinta e perché; un miglioramento concreto (le quattro parti, privacy, peso); parole sue." },
      { area: "parere", tema: "retro", q: L("Retrospettiva: una cosa da fare di più, una da fare di meno, una da cominciare e una da smettere, nelle lezioni e nel gioco.", "Retrospettiva: ক্লাসে আর খেলায় কী বেশি করব, কী কম করব, কী শুরু করব, কী বন্ধ করব।"),
        aiuto: L("Non conta per il voto: serve al prof per migliorare. Anche poche parole, ma sincere.", "নম্বরের জন্য নয়: শিক্ষককে ভালো করতে সাহায্য করে। অল্প কথা, কিন্তু সত্যি।"), min_parole: 8 }
    ],

    /* ---------- RECUPERO: domande nuove sugli stessi temi ---------- */
    recupero: [
      C("nozioni", L("Da v1.3 a v1.4 il cambio è…", "v1.3 থেকে v1.4: পরিবর্তনটি…"), ["minor: un passo piccolo", "major: un cambio grande"], "", "numeri"),
      C("nozioni", L("Dove leggi che cosa è cambiato nella v1.2 e da quale Pull Request?", "v1.2-এ কী বদলেছে আর কোন Pull Request থেকে, কোথায় পড়বে?"), ["nel changelog", "nel backlog", "su Classroom"], "", "changelog"),
      C("nozioni", L("A che cosa serve un ramo (branch)?", "শাখা (branch) কী কাজে লাগে?"), ["a lavorare su una strada parallela, senza rompere il gioco principale", "a cancellare il gioco", "a dare il voto"], "", "ramo"),
      C("nozioni", L("Prima del merge, chi controlla la Pull Request?", "merge-এর আগে Pull Request কে দেখে?"), ["il prof", "nessuno", "il gioco, da solo"], "", "merge"),
      C("nozioni", L("Quale di queste è una Pull Request scritta bene?", "কোনটা ভালোভাবে লেখা Pull Request?"), ["«Cielo grigio: il colore del cielo diventa grigio, nello sfondo, così il gioco sembra più d'azione»", "«cambiate il treno»", "«una cosa bella»"], "", "pr"),
      C("sistema", L("I pesi del backlog sono 1, 2, 3, 5, 8. Che numero viene dopo l'8?", "backlog-এর ওজন ১, ২, ৩, ৫, ৮। ৮-এর পরে কোন সংখ্যা?"), ["13", "9", "10"], "", "backlog"),
      C("sistema", L("Uno sprint finisce con…", "একটি sprint শেষ হয়…"), ["una versione che funziona e la retrospettiva", "un voto e basta", "la cancellazione del gioco"], "", "agile"),
      C("sistema", L("Una richiesta con la foto di una persona vera viene respinta. Come la rimandi?", "আসল মানুষের ছবিসহ অনুরোধ বাতিল হয়েছে। কীভাবে আবার পাঠাবে?"), ["con un personaggio disegnato o di un videogioco", "con la foto di un'altra persona vera", "non si può più mandare"], "", "privacy")
    ]
  };
})();
