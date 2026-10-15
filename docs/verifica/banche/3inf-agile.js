// 3INF · Verifica Agile / Product Manager (15/10/2026). Meno IA possibile: le aperte sono sul lavoro di OGGI del ragazzo.
// Il motore blocca l'incolla, misura il tempo di scrittura e segna le uscite dalla pagina. Aree e peso: concetti 30%, il tuo planning 40%, esperienza 30%.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }

  window.BANCA = {
    id: "3inf-agile-v1",
    classe: "3INF",
    titolo: "Verifica: un team Agile al lavoro",
    sotto: "3INF · 15/10/2026 · versioni, sprint, planning · ripasso, verifica e recupero",
    stato: "stato/3inf-agile.json",
    risultati: "risultati.html?b=3inf-agile",
    minuti: 20,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: sprint, backlog, peso, rischio, cerimonie", peso: 30 },
      planning: { nome: "Il tuo planning: le tue scelte di oggi (solo parole tue)", peso: 40 },
      esperienza: { nome: "La tua esperienza del gioco", peso: 30 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- RIPASSO ---------- */
    schede_temi: { sprint: 1, cerimonie: 1, backlog: 2, peso: 2, rischio: 2, planning: 3, clienti: 3 },
    schede: [
      { titolo: "1. Lo sprint e le cerimonie", testo: "Lo <b>sprint</b> è l'unità di tempo dell'Agile (in azienda una settimana, lun-ven; nel gioco 15 minuti). Ha una <b>capacità</b> fissa: il team fa al massimo <b>8 punti</b> di lavoro. Ogni sprint gira in 4 <b>cerimonie</b>: <b>Planning</b> (si sceglie), <b>Daily</b> (ogni giorno, cosa ho fatto/faccio/mi blocca), <b>Review</b> (si mostra la versione ai clienti), <b>Retrospettiva</b> (il team migliora il suo modo di lavorare)." },
      { titolo: "2. Backlog, peso e rischio", testo: "Il <b>backlog</b> è la lista ordinata delle richieste. Ogni richiesta ha un <b>peso</b> (quanto lavoro serve: 1, 2, 3, 5, 8) e un <b>rischio</b> sul software (quanto può rompere le altre parti: 1, 2, 3). Il <b>valore</b> dice quanto serve ai clienti." },
      { titolo: "3. Il planning: mettere insieme i pezzetti", testo: "Il <b>planning</b> è <b>mettere insieme i pezzetti</b> nell'ordine giusto: non si fa tutto e non a caso, si scelgono le richieste che danno il risultato più grande dentro gli 8 punti. Il filo è la <b>priorità</b> = <b>valore ÷ (peso + rischio)</b>: prima quelle che valgono tanto e costano poco. I clienti non pesano uguale: <b>TrenoCity conta 3</b>, la <b>Ludoteca conta 1</b>." }
    ],
    strumenti: [{ t: 'Il gioco', u: 'https://nicolaregge-pulse.github.io/corso-informatica/compito/3inf-20261015-agile/', c: '#1f6feb' }, { t: 'Il cruscotto', u: 'https://nicolaregge-pulse.github.io/corso-informatica/3inf-agile/', c: '#0b7285' }],
    via: C("concetti", "Lo sprint è…", ["un tempo fisso di lavoro con una capacità di 8 punti", "un cliente", "un bug del gioco"], "Unità di tempo dell'Agile."),
    prepara: [
      { q: "Che cos'è il planning, con l'idea di oggi («mettere insieme i pezzetti»)?", min: 12 },
      { q: "Nel tuo sprint, che cosa hai scelto per prima e perché?", min: 10 }
    ],
    allenamento: [
      S(1, C("concetti", "La capacità dello sprint è 8 punti: vuol dire…", ["al massimo 8 punti di peso per sprint", "sempre 8 richieste", "8 minuti di gioco"], "Si riempie fino a 8.")),
      S(1, C("concetti", "Le 4 cerimonie dello sprint sono…", ["planning, daily, review, retrospettiva", "nome, azienda, voto, fine", "lunedì, martedì, mercoledì, giovedì"], "Il cerchio della lavagna.")),
      S(2, C("concetti", "Il peso di una richiesta dice…", ["quanto lavoro serve", "quanto piace al prof", "il colore"], "1, 2, 3, 5, 8.")),
      S(2, C("concetti", "Il rischio sul software dice…", ["quanto la modifica può rompere le altre parti", "quanto è bella", "quanto costa in euro"], "1 basso, 3 alto.")),
      S(3, C("planning", "La priorità si calcola…", ["valore ÷ (peso + rischio)", "peso × rischio", "a caso"], "Prima valore alto e costo basso.")),
      S(3, C("planning", "TrenoCity conta 3 e la Ludoteca conta 1: vuol dire…", ["rendere felice TrenoCity vale di più", "sono uguali", "la Ludoteca vale di più"], "Il cliente grande pesa di più."))
    ],

    /* ---------- VERIFICA ---------- */
    crocette: [
      C("concetti", "Lo sprint è…", ["un tempo fisso di lavoro, con capacità 8 punti", "un tipo di bug", "il nome di un cliente"], "", "sprint"),
      C("concetti", "La priorità di una richiesta è…", ["valore ÷ (peso + rischio)", "peso + valore", "il numero di parole"], "", "planning"),
      C("concetti", "Le quattro cerimonie sono…", ["planning, daily, review, retrospettiva", "fork, branch, merge, release", "nome, azienda, voto, fine"], "", "cerimonie"),
      C("concetti", "Il peso di una richiesta misura…", ["quanto lavoro serve a farla", "quanto è bella", "quanti clienti la vogliono"], "", "peso"),
      C("concetti", "Il Product Manager…", ["decide l'ordine del backlog e che cosa entra nello sprint", "scrive tutto il codice da solo", "prova il gioco e trova i bug"], "", "backlog"),
      C("concetti", "TrenoCity conta 3 e la Ludoteca conta 1: nel planning…", ["conviene accontentare prima TrenoCity", "contano uguale", "si ignora TrenoCity"], "", "clienti")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti capace, adesso, di fare il planning di uno sprint?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti è piaciuto fare il Product Manager?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "planning", tema: "scelte", q: "Scrivi il nome della TUA azienda e le richieste che hai scelto nel tuo sprint. Perché proprio quelle?", aiuto: "Al massimo 3 righe, parole tue. È il tuo lavoro: lo sai solo tu.", min_parole: 12,
        criteri: "nome azienda + richieste reali del suo gioco; una ragione (valore/peso/rischio/cliente)" },
      { area: "planning", tema: "planning", q: "Oggi è uscito che il planning è «mettere insieme i pezzetti». Spiega con parole tue che cosa vuol dire fare il planning.", aiuto: "Al massimo 3 righe.", min_parole: 12,
        criteri: "scegliere e ordinare dentro gli 8 punti; priorità = valore ÷ (peso+rischio); non si fa tutto" },
      { area: "esperienza", tema: "clienti", q: "Perché il cliente TrenoCity conta più della Ludoteca quando scegli? Fai un esempio tuo.", aiuto: "Al massimo 3 righe.", min_parole: 10,
        criteri: "TrenoCity pesa 3, Ludoteca 1; un esempio concreto di scelta" },
      { area: "parere", tema: "retro", q: "Una cosa che hai imparato oggi e una che cambieresti.", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- RECUPERO ---------- */
    recupero: [
      C("concetti", "Lo sprint ha una capacità di…", ["8 punti di peso", "8 euro", "8 clienti"], "", "sprint"),
      C("concetti", "Il planning vuol dire…", ["scegliere e ordinare le richieste dentro gli 8 punti", "cancellare il gioco", "scrivere il codice"], "", "planning"),
      C("concetti", "La priorità più alta ce l'ha una richiesta con…", ["valore alto e peso+rischio bassi", "tante parole", "un bel titolo"], "", "planning"),
      C("concetti", "La review serve a…", ["mostrare la versione nuova ai clienti", "scegliere le richieste", "spegnere i PC"], "", "cerimonie"),
      C("concetti", "La retrospettiva serve a…", ["decidere come lavorare meglio il prossimo sprint", "dare i voti", "trovare i clienti"], "", "cerimonie"),
      C("concetti", "Il rischio alto in uno sprint può…", ["far uscire un bug nella versione", "far guadagnare punti", "rendere tutti felici"], "", "peso")
    ]
  };
})();
