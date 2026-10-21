// 3INF · 21/10/2026 — Il sito in ordine (struttura controllata), sfondo e animazioni in CSS, poi a coppie: ramo, Pull Request, merge, versione.
// Teoria + ripasso qui; il controllo della struttura è la pagina «L'albero del mio sito»; il quiz è su Google Moduli (link nel compito).
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  var ALB = "<a href=\"../3inf-albero/\" target=\"_blank\" rel=\"noopener\">L'albero del mio sito</a>";
  window.BANCA = {
    id: "3inf-grafica-pr-v1",
    classe: "3INF",
    titolo: "Il mio sito: in ordine, più bello, e lavoro in coppia",
    sotto: "3INF · 21/10/2026 · struttura, sfondo, animazioni, Pull Request e versioni",
    stato: "stato/3inf-grafica-pr.json",
    risultati: "risultati.html?b=3inf-grafica-pr",
    minuti: 15,
    anteprima: "868848605",
    aree: { web: { nome: "Sito, CSS e lavoro in coppia", peso: 100 }, parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 } },
    schede_temi: { albero: 1, sfondo: 3, anim: 4, pr: 5, versione: 6 },
    schede: [
      { titolo: "1. Prima di tutto: il sito in ordine", testo: "Un sito funziona solo se i file sono <b>nel posto giusto</b> e con il <b>nome giusto</b>. Nella cartella principale del repository servono:<br><code>index.html</code> · <code>style.css</code> · <code>competenze.html</code> · <code>passione.html</code> · la cartella <code>img</code> con le tue immagini.<br><br>Apri " + ALB + ", scrivi l'indirizzo del tuo sito e premi <b>Controlla</b>. Sistema le croci rosse <b>una alla volta</b> finché è tutto verde. Questo è il primo traguardo di oggi." },
      { titolo: "2. Le tre regole dei nomi", testo: "1) <b>Tutto minuscolo</b>: GitHub distingue <code>Index.html</code> da <code>index.html</code>: per lui sono due file diversi, e il link non funziona.<br>2) <b>Niente spazi</b>: <code>mia foto.jpg</code> no, <code>mia-foto.jpg</code> sì.<br>3) <b>Il collegamento uguale al nome, lettera per lettera</b>: se il file è <code>sfondo.jpeg</code>, nel CSS scrivi <code>sfondo.jpeg</code>, non <code>sfondo.jpg</code>.<br><br>Per rinominare su GitHub: apri il file, matita, cambia il nome in alto, <b>Commit changes</b>. Per spostarlo nella cartella img scrivi <code>img/</code> davanti al nome." },
      { titolo: "3. Un'immagine di sfondo", testo: "Carica la tua immagine: <b>Add file → Upload files</b>, poi rinominala in <code>img/sfondo.jpg</code>. Poi in <code>style.css</code>, dentro <code>body { }</code>, aggiungi:<pre>background-image: url(\"img/sfondo.jpg\");\nbackground-size: cover;\nbackground-attachment: fixed;</pre>Se il testo non si legge bene, metti il contenuto in un riquadro semitrasparente:<pre>main { background: rgba(255,255,255,0.85); padding: 20px; border-radius: 12px; }</pre>L'immagine la scegli tu: è il tuo sito." },
      { titolo: "4. Una piccola animazione", testo: "<b>Transition</b>: un cambiamento morbido quando passi sopra con il mouse.<pre>nav a { transition: transform 0.3s; }\nnav a:hover { transform: scale(1.15); }</pre><b>@keyframes</b>: un'animazione che parte da sola, per esempio il titolo che entra piano.<pre>@keyframes entra {\n  from { opacity: 0; transform: translateY(-20px); }\n  to   { opacity: 1; transform: translateY(0); }\n}\nh1 { animation: entra 1s ease; }</pre>Poche animazioni e leggere: un sito che si muove troppo stanca chi lo guarda." },
      { titolo: "5. A coppie: ramo, Pull Request, merge", testo: "Ora lavori sul sito del compagno, come in un'azienda.<br>1) Il compagno ti aggiunge come <b>collaboratore</b>: Settings → Collaborators → Add people.<br>2) Tu, nel suo repository, apri un file, matita, e in basso scegli <b>Create a new branch</b> (un ramo: la tua copia per provare). Aggiungi una sezione «Il mio compagno di lavoro»: tre righe su di lui e un consiglio per il suo sito.<br>3) Premi <b>Propose changes</b> e poi <b>Create pull request</b>.<br>4) Il compagno apre la Pull Request, guarda le modifiche e preme <b>Merge pull request</b>. Il suo sito ora ha la tua sezione!<br>Poi vi scambiate i ruoli." },
      { titolo: "6. Il numero di versione", testo: "Nel piè di pagina di <code>index.html</code> scrivi la versione: <code>&lt;footer&gt;Versione 1.0&lt;/footer&gt;</code>.<br>Ogni Pull Request accettata che aggiunge qualcosa fa salire il secondo numero: <b>1.0 → 1.1 → 1.2</b>. Il primo numero sale solo per un cambiamento grande (un sito tutto nuovo: 2.0).<br><b>Sfida finale</b>: tutti e due cambiate la <b>stessa riga</b> del titolo in due rami diversi. GitHub dice <b>conflitto</b>: scegliete insieme quale tenere (Resolve conflicts), poi merge. Avete risolto il vostro primo conflitto, come i programmatori veri." }
    ],
    via: C("web", "Su GitHub, Index.html e index.html sono…", ["due file diversi", "lo stesso file", "due cartelle"], "GitHub distingue maiuscole e minuscole."),
    prepara: [ { q: "Perché un file con il nome sbagliato rompe il sito?", min: 6 } ],
    allenamento: [
      S(1, C("web", "Dove deve stare index.html?", ["nella cartella principale del repository", "dentro la cartella img", "in una cartella chiamata sito"], "")),
      S(2, C("web", "Quale nome di file è giusto?", ["mia-foto.jpg", "Mia Foto.JPG", "mia foto.jpg"], "Minuscolo e senza spazi.")),
      S(3, C("web", "Per mettere un'immagine di sfondo uso…", ["background-image: url(\"img/sfondo.jpg\");", "<img background>", "color: sfondo;"], "")),
      S(4, C("web", "Un cambiamento morbido quando passo sopra con il mouse si fa con…", ["transition e :hover", "una nuova pagina html", "un commit"], "")),
      S(5, C("web", "Chi preme «Merge pull request»?", ["il proprietario del sito, dopo aver guardato le modifiche", "chi propone la modifica, subito", "nessuno"], "")),
      S(6, C("web", "Una Pull Request accettata aggiunge una sezione: la versione 1.1 diventa…", ["1.2", "2.0", "1.1 (non cambia)"], ""))
    ],
    crocette: [
      C("web", "Su GitHub, Index.html e index.html sono…", ["due file diversi", "lo stesso file", "due cartelle", "un errore di GitHub"], "", "albero"),
      C("web", "Il file si chiama sfondo.jpeg. Nel CSS scrivo…", ["url(\"img/sfondo.jpeg\")", "url(\"img/sfondo.jpg\")", "url(\"sfondo\")", "url(\"Sfondo.JPEG\")"], "", "sfondo"),
      C("web", "A che cosa serve un ramo (branch)?", ["a provare le modifiche senza toccare il sito vero", "a cancellare il repository", "a cambiare password", "a pubblicare su Classroom"], "", "pr"),
      C("web", "Due persone cambiano la stessa riga in due rami. Che cosa succede al merge?", ["un conflitto, da risolvere scegliendo cosa tenere", "GitHub cancella il repository", "vince sempre il più veloce", "niente, si sommano da sole"], "", "pr")
    ],
    scale: [ { area: "parere", q: "Quanto ti senti sicuro a lavorare sul sito di un altro?", basso: "per niente", alto: "moltissimo", ultima: true } ],
    aperte: [],
    recupero: []
  };
})();
