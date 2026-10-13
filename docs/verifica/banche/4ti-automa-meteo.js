// 4TI · progetto di stage «Automa meteo» · percorso guidato: teoria, pratica, verifica, recupero (aggiustamento del voto).
// Aree e peso nel giudizio: concetti 30%, il tuo codice (saperlo spiegare) 40%, il lavoro fatto (tappe e commit) 30%.
// Il voto è un giudizio complessivo del prof. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  var REPO = "https://github.com/chasedeleon/automa-meteo-python";
  var PERCORSO = REPO + "/blob/main/documenti/PERCORSO.md";

  window.BANCA = {
    id: "4ti-automa-meteo-v1",
    classe: "4TI",
    titolo: "Automa meteo: costruiscilo, capiscilo, spiegalo",
    sotto: "4TI · progetto di stage · teoria, pratica, verifica e recupero",
    stato: "stato/4ti-automa-meteo.json",
    risultati: "risultati.html?b=4ti-automa-meteo",
    modulo: "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform",
    minuti: 50,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: API, dati, file, automi, web", peso: 30 },
      codice: { nome: "Il tuo codice: saperlo spiegare (solo parole tue)", peso: 40 },
      lavoro: { nome: "Il lavoro fatto: tappe e commit", peso: 30 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. TEORIA ---------- */
    schede: [
      { titolo: "1. Che cos'è un automa", testo: "Un <b>automa</b> è un programma che fa da solo un lavoro che si ripete: legge un dato, lo salva, lo mostra, poi aspetta e ricomincia. I sistemi di controllo delle fabbriche e dei laboratori (come <b>EPICS</b>) sono fatti così, in grande: <b>sorgente dei dati → automa → storico → pannello di controllo</b>. Il tuo progetto ha gli stessi quattro blocchi." },
      { titolo: "2. API REST e JSON", testo: "Una <b>API REST</b> è un indirizzo web che invece di una pagina restituisce <b>dati</b>. Open-Meteo risponde in <b>JSON</b>: testo con parentesi graffe, fatto di coppie <i>nome: valore</i>, una dentro l'altra come cassetti in un armadio. In Python <code>json.loads()</code> trasforma quel testo in un dizionario, e <code>dati[\"current_weather\"][\"temperature\"]</code> apre il cassetto «current_weather» e prende «temperature»." },
      { titolo: "3. Funzioni, return e None", testo: "Una <b>funzione</b> (<code>def</code>) è un pezzo di programma con un nome, che si richiama quando serve. Con <code>return</code> restituisce un risultato a chi l'ha chiamata. I <b>parametri</b>, tra le parentesi, sono i dati che riceve: <code>vento=None</code> vuol dire «se non me lo dai, vale None». <b>None</b> vuol dire «niente»: lo si usa quando un dato manca, per esempio se Internet non risponde (<code>try</code> / <code>except</code>)." },
      { titolo: "4. Lo storico: file CSV", testo: "Un <b>CSV</b> è un file di testo a tabella: una riga per lettura, le colonne separate da <code>;</code>. Si apre con Excel. Aprendo il file in modalità <code>\"a\"</code> (append) si aggiunge in fondo senza cancellare. In Excel italiano i decimali vogliono la <b>virgola</b>: con il punto, 18.9 diventa testo e non si può fare la media." },
      { titolo: "5. Il ciclo e il tempo", testo: "<code>while True:</code> ripete per sempre; <code>time.sleep(60)</code> aspetta 60 secondi. Il computer che esegue il programma può avere un altro fuso orario: con <code>ZoneInfo(\"Europe/Rome\")</code> si usa l'ora italiana." },
      { titolo: "6. La dashboard: Python scrive una pagina web", testo: "Una pagina web è solo testo HTML. Python la costruisce con una <b>f-string</b> (<code>f\"...{temperatura}...\"</code>), che mette i valori al posto giusto, e la scrive in <code>index.html</code>. <code>&lt;meta charset=\"utf-8\"&gt;</code> serve perché simboli come «°» si vedano bene." },
      { titolo: "7. GitHub Actions e Pages", testo: "<b>GitHub Actions</b> esegue il tuo programma da solo, agli orari scritti nel file <code>.github/workflows/automa.yml</code> (ogni 30 minuti), anche a computer spento, e salva i risultati con un commit. <b>GitHub Pages</b> pubblica la cartella <code>docs</code> come sito: la dashboard si apre anche dal telefono." },
      { titolo: "8. LA PRATICA: costruisci il tuo automa", testo: "La pratica è il <b>percorso a tappe</b> nel tuo deposito: scrivi l'automa da zero, nella cartella <code>mio-automa/</code>, un pezzo alla volta, con gli aiuti a livelli e senza codice da copiare. Ogni tappa: funziona + commit + la sai spiegare nella chat del progetto.<br><a href=\"" + PERCORSO + "\" target=\"_blank\"><b>Apri il percorso a tappe</b></a> · <a href=\"https://colab.research.google.com\" target=\"_blank\">Apri Google Colab</a> · <a href=\"" + REPO + "/pulls\" target=\"_blank\">La chat del progetto</a>" }
    ],
    strumenti: [{ t: 'Il tuo deposito', u: REPO, c: '#1f6feb' }, { t: 'La tua dashboard', u: 'https://chasedeleon.github.io/automa-meteo-python/', c: '#1a7f37' }],
    via: C("concetti", "Il tuo automa prende la temperatura da…", ["un servizio su Internet (API REST Open-Meteo)", "un termometro attaccato al PC", "un file scritto a mano"], "Esatto: una API REST, che risponde con dati invece che con una pagina."),
    prepara: [
      { q: "Racconta con parole tue che cosa fa il tuo automa, dall'inizio alla fine, come lo spiegheresti a un amico.", min: 25 },
      { q: "Qual è la parte del progetto che hai capito meglio, e quale ti è ancora poco chiara?", min: 15 }
    ],
    allenamento: [
      S(1, C("concetti", "I quattro blocchi del tuo progetto sono…", ["sorgente dei dati, automa, storico, dashboard", "tastiera, mouse, schermo, stampante", "Word, Excel, PowerPoint, Outlook"], "Come nei sistemi di controllo veri.")),
      S(2, C("concetti", "In <code>dati[\"current_weather\"][\"windspeed\"]</code>, che cosa fa <code>[\"windspeed\"]</code>?", ["prende il vento dentro current_weather", "cancella il vento", "manda il vento al server"], "Si apre il cassetto e si prende quel valore.")),
      S(2, C("concetti", "<code>json.loads(testo)</code> serve a…", ["trasformare il testo JSON in dati di Python", "scrivere un file", "aprire una pagina web"], "loads = carica da una stringa.")),
      S(3, C("concetti", "Se Internet non risponde, la tua funzione restituisce…", ["None, grazie a try/except", "un errore che ferma tutto per sempre", "zero gradi"], "except cattura l'errore e restituisce None.")),
      S(3, C("concetti", "<code>def genera_dashboard(vento=None)</code>: che cosa vuol dire <code>vento=None</code>?", ["se il vento non viene passato, vale None", "il vento è sempre zero", "il vento è vietato"], "È il valore predefinito del parametro.")),
      S(4, C("concetti", "Perché nello storico si scrive 18,9 e non 18.9?", ["perché Excel in italiano legge i decimali con la virgola", "perché è più corto", "perché Python lo vuole"], "Con il punto Excel lo tratta come testo.")),
      S(5, C("concetti", "<code>time.sleep(60)</code>…", ["fa aspettare il programma 60 secondi", "spegne il computer per 60 secondi", "legge 60 temperature"], "sleep = dormi.")),
      S(7, C("concetti", "La lettura delle 12:44 nessuno l'ha cliccata. Chi l'ha fatta?", ["GitHub Actions, seguendo l'orario in automa.yml", "il prof, di nascosto", "il telefono"], "schedule = ogni 30 minuti, da solo."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("concetti", "Una API REST è…", ["un indirizzo web che restituisce dati invece di una pagina", "un tipo di computer", "un file di Excel"], "Open-Meteo è una API REST.", "api"),
      C("concetti", "JSON è…", ["un formato di testo per i dati, con coppie nome: valore", "un linguaggio per disegnare", "un antivirus"], "Parentesi graffe, nomi e valori.", "json"),
      C("concetti", "<code>return</code> in una funzione…", ["restituisce il risultato a chi l'ha chiamata", "ricomincia il programma", "stampa sullo schermo"], "", "funzioni"),
      C("concetti", "Aprire un file con <code>\"a\"</code> invece che con <code>\"w\"</code>…", ["aggiunge in fondo senza cancellare", "cancella tutto e riscrive", "apre solo in lettura"], "", "file"),
      C("concetti", "<code>while True:</code> con <code>time.sleep(60)</code> dentro…", ["ripete per sempre, una volta al minuto", "fa una sola lettura", "si ferma dopo 60 letture"], "", "ciclo"),
      C("concetti", "Una f-string come <code>f\"{temperatura} °C\"</code>…", ["mette il valore della variabile dentro il testo", "scrive la parola temperatura", "è un errore"], "", "html"),
      C("concetti", "Il file <code>.github/workflows/automa.yml</code>…", ["dice a GitHub quale programma eseguire e ogni quanto", "contiene le temperature", "è la pagina della dashboard"], "", "actions"),
      C("concetti", "GitHub Pages…", ["pubblica la cartella docs come sito, visibile anche dal telefono", "esegue il programma ogni 30 minuti", "corregge il codice"], "", "actions")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di spiegare il tuo codice?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti è piaciuto costruire l'automa?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "codice", tema: "funzione", q: "Spiega con parole tue che cosa fa la tua funzione che legge il meteo: che cosa chiede, a chi, che cosa restituisce e che cosa succede se Internet non risponde.", aiuto: "Almeno 40 parole. Come lo spiegheresti a un collega.", min_parole: 40,
        criteri: "nomina la API Open-Meteo; dice che restituisce i numeri (temperatura, vento); spiega try/except e None; parole sue" },
      { area: "codice", tema: "parametro", q: "Perché nella dashboard c'è <code>vento=None</code>? Che cosa succede se il vento non arriva?", aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "parametro con valore predefinito; la pagina mostra «-» invece di bloccarsi" },
      { area: "codice", tema: "automa", q: "Chi esegue il tuo programma ogni 30 minuti, dove è scritto, e che differenza c'è con il ciclo <code>while True</code> su Colab?", aiuto: "Almeno 40 parole.", min_parole: 40,
        criteri: "GitHub Actions; automa.yml con l'orario; su GitHub una lettura sola, su Colab il ciclo con sleep" },
      { area: "lavoro", tema: "tappe", q: "Elenca le tappe che hai fatto e, per ognuna, il messaggio del commit e una cosa che hai imparato.", aiuto: "Una riga per tappa. Il prof controlla i commit nel tuo deposito.", min_parole: 30,
        criteri: "tappe vere con commit veri nel deposito; una cosa imparata per tappa" },
      { area: "lavoro", tema: "errore", q: "Racconta un errore che hai fatto durante il progetto e come l'hai risolto.", aiuto: "Almeno 30 parole. Sbagliare è normale: conta come ne sei uscito.", min_parole: 30,
        criteri: "errore concreto; come l'ha trovato; come l'ha risolto" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più in questo percorso, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO: aggiustamento del voto ---------- */
    recupero: [
      C("concetti", "Nella risposta di Open-Meteo la temperatura sta…", ["dentro current_weather, alla voce temperature", "nel titolo della pagina", "in un file sul PC"], "", "json"),
      C("concetti", "Che cosa restituisce <code>json.loads</code>?", ["un dizionario di Python", "un file CSV", "una pagina HTML"], "", "json"),
      C("concetti", "Un indirizzo che finisce con <code>?latitude=45.46&longitude=9.19</code> sta chiedendo…", ["i dati per quel punto della Terra (Milano)", "una password", "un file da scaricare"], "", "api"),
      C("concetti", "Se tolgo <code>return</code> dalla funzione…", ["chi la chiama riceve None", "la funzione va più veloce", "non cambia niente"], "", "funzioni"),
      C("concetti", "Per scrivere l'intestazione dello storico una volta sola si controlla…", ["se il file esiste già", "l'ora del giorno", "la temperatura"], "", "file"),
      C("concetti", "Per fermare il ciclo su Colab…", ["si clicca il quadrato di stop", "si aspetta che finisca da solo", "si spegne Internet"], "", "ciclo"),
      C("concetti", "Senza <code>&lt;meta charset=\"utf-8\"&gt;</code> il simbolo «°»…", ["può comparire storto", "diventa più grande", "sparisce la pagina"], "", "html"),
      C("concetti", "Se cambio l'orario in automa.yml da 30 a 60 minuti…", ["l'automa legge ogni ora", "l'automa si ferma", "la dashboard sparisce"], "", "actions")
    ]
  };
})();
