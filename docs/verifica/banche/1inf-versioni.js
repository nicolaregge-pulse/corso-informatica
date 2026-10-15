// 1INF · Versioni del software e changelog (15/10/2026). Ripasso + verifica corta. Incolla bloccato, tempo e uscite misurati.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  window.BANCA = {
    id: "1inf-versioni-v1",
    classe: "1INF",
    titolo: "Versioni del software e changelog",
    sotto: "1INF · 15/10/2026 · ripasso, verifica e recupero",
    stato: "stato/1inf-versioni.json",
    risultati: "risultati.html?b=1inf-versioni",
    minuti: 15,
    anteprima: "868848605",
    aree: {
      concetti: { nome: "Concetti: versione, major/minor, changelog", peso: 60 },
      tuo: { nome: "Il tuo esempio (parole tue)", peso: 40 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { versione: 1, numeri: 2, changelog: 3 },
    schede: [
      { titolo: "1. Che cos'è una versione", testo: "Una <b>versione</b> è un salvataggio del programma con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Così si sa sempre quale versione si sta usando, e se una modifica rompe tutto si può tornare a una versione di prima." },
      { titolo: "2. Major e minor", testo: "Se cambia il numero <b>dopo il punto</b> (v0.30 → v0.31, oppure v1.4 → v1.5) è un passo <b>piccolo</b>: <b>minor</b>. Se cambia il <b>primo numero</b> (v1.9 → v2.0) è un cambio <b>grande</b>: <b>major</b>, per esempio un motore nuovo. Dopo un major si riparte dallo zero (v2.0, v2.1…)." },
      { titolo: "3. Il changelog", testo: "Il <b>changelog</b> è il <b>registro di tutte le modifiche</b>, versione per versione: per ognuna c'è il numero e cosa è cambiato. Serve a ricordare la storia del programma e a far capire agli altri cosa è stato fatto." }
    ],
    via: C("concetti", "Una versione è…", ["un salvataggio con un numero e cosa cambia", "un gioco", "un errore del computer"], "Numero + descrizione."),
    prepara: [
      { q: "Scrivi una versione nuova del treno: il numero e cosa cambia.", min: 6 },
      { q: "Perché conviene scrivere il changelog?", min: 6 }
    ],
    allenamento: [
      S(1, C("concetti", "Una versione serve a…", ["salvare il programma e sapere cosa cambia", "cancellare il gioco", "spegnere il PC"], "")),
      S(2, C("concetti", "Da v0.30 a v0.31 è un cambio…", ["piccolo (minor)", "grande (major)", "niente"], "Cambia il numero dopo il punto.")),
      S(2, C("concetti", "Da v1.9 a v2.0 è un cambio…", ["grande (major)", "piccolo (minor)", "un errore"], "Cambia il primo numero.")),
      S(3, C("concetti", "Il changelog è…", ["l'elenco delle modifiche di ogni versione", "il nome del gioco", "un bug"], ""))
    ],
    crocette: [
      C("concetti", "Una versione del programma è…", ["un salvataggio con un numero e la descrizione di cosa cambia", "un tipo di computer", "un gioco online"], "", "versione"),
      C("concetti", "Da v0.30 a v0.31 il cambio è…", ["piccolo (minor)", "grande (major)", "non è un cambio"], "", "numeri"),
      C("concetti", "Da v1.4 a v2.0 il cambio è…", ["grande (major)", "piccolo (minor)", "uguale"], "", "numeri"),
      C("concetti", "Il changelog è…", ["l'elenco di tutte le modifiche, versione per versione", "il nome del programma", "una password"], "", "changelog"),
      C("concetti", "Perché conviene usare le versioni?", ["se una modifica rompe tutto, si torna a una versione di prima", "per fare il gioco più lungo", "per spegnere il PC"], "", "versione"),
      C("concetti", "Dopo una versione major (v2.0) il numero dopo il punto…", ["riparte da zero (v2.0, v2.1, v2.2)", "continua da v2.31", "sparisce"], "", "numeri")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti sicuro sulle versioni e il changelog?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "tuo", tema: "versione", q: "Scrivi una versione nuova del treno: il numero (es. v1.6) e in una riga cosa cambia.", aiuto: "Parole tue. Es: v1.6 — il cielo diventa rosso al tramonto.", min_parole: 6,
        criteri: "un numero di versione coerente + una modifica descritta" },
      { area: "concetti", tema: "changelog", q: "Che cos'è il changelog e perché è utile? Rispondi con parole tue.", aiuto: "Al massimo 3 righe.", min_parole: 8,
        criteri: "elenco delle modifiche per versione; utile per ricordare/capire la storia" }
    ],
    recupero: [
      C("concetti", "Una versione ha…", ["un numero e la descrizione di cosa cambia", "solo un colore", "solo un nome"], "", "versione"),
      C("concetti", "Il numero dopo il punto che aumenta (v0.30→v0.31) vuol dire…", ["cambio piccolo (minor)", "cambio grande", "errore"], "", "numeri"),
      C("concetti", "Il primo numero che aumenta (v1.x→v2.0) vuol dire…", ["cambio grande (major)", "cambio piccolo", "niente"], "", "numeri"),
      C("concetti", "Il changelog serve a…", ["ricordare tutte le modifiche fatte", "giocare", "accendere il PC"], "", "changelog")
    ]
  };
})();
