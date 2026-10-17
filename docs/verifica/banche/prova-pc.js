// PROVA assemblaggio PC — test 1-a-1 (teoria breve + simulatore + verifica + recupero).
// Framework 2 (lezione normale) su una persona. Riusa il motore verifica e il simulatore monta-pc-v3.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  window.BANCA = {
    id: "prova-pc-v1",
    classe: "PROVA",
    titolo: "Prova: monta il PC e i suoi pezzi",
    sotto: "Test · teoria breve, simulatore, verifica e recupero",
    stato: "stato/prova-pc.json",
    risultati: "risultati.html?b=prova-pc",
    minuti: 12,
    anteprima: "999001",
    strumenti: [
      { t: "🔧 Prova il simulatore «Monta il PC»", u: "../monta-pc-v3/", c: "#2ea043" }
    ],
    aree: {
      pc: { nome: "I pezzi del computer", peso: 100 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { pezzi: 1, raffredda: 2, collega: 3 },
    schede: [
      { titolo: "1. Il cervello e la memoria", testo: "La <b>CPU</b> (processore) è il <b>cervello</b>: fa i calcoli. La <b>RAM</b> è la <b>memoria veloce di lavoro</b>, si infila negli slot lunghi della scheda madre. L'<b>hard disk</b> (o SSD) <b>conserva i file</b> (foto, giochi) anche a PC spento." },
      { titolo: "2. Corrente e raffreddamento", testo: "L'<b>alimentatore</b> dà la <b>corrente</b> a tutti i pezzi. La CPU scalda, quindi sopra ha <b>dissipatore + ventola</b> che la <b>raffreddano</b> buttando fuori l'aria calda." },
      { titolo: "3. Dove si monta e come si collega", testo: "La <b>scheda madre</b> è la base dove si <b>montano tutti i pezzi</b>. Il <b>lettore DVD</b> e l'<b>hard disk</b> stanno sulla <b>slitta</b> e si collegano con il <b>cavo SATA</b>." },
      { titolo: "4. Prova il simulatore", testo: "Prima della verifica, apri il bottone verde <b>«Prova il simulatore Monta il PC»</b> qui sopra e monta almeno un computer: trascina i pezzi al loro posto fino a «FATTO»." }
    ],
    via: C("pc", "Qual è il «cervello» del computer?", ["La CPU (processore)", "La ventola", "Il cavo"], "Fa tutti i calcoli."),
    prepara: [
      { q: "Scrivi, con parole tue, cosa hai montato nel simulatore e in che ordine.", min: 6 },
      { q: "A cosa serve la RAM? E l'hard disk? Spiega la differenza.", min: 6 }
    ],
    allenamento: [
      S(1, C("pc", "La RAM si infila…", ["negli slot lunghi della scheda madre", "nel lettore DVD", "nell'alimentatore"], "È la memoria di lavoro.")),
      S(2, C("pc", "Cosa conserva i file anche a PC spento?", ["l'hard disk / SSD", "la RAM", "la ventola"], "La RAM si svuota.")),
      S(3, C("pc", "Cosa raffredda la CPU?", ["dissipatore + ventola", "l'hard disk", "il cavo SATA"], "")),
      S(4, C("pc", "Chi dà la corrente a tutti i pezzi?", ["l'alimentatore", "la CPU", "la RAM"], ""))
    ],
    crocette: [
      C("pc", "Devi togliere la memoria di lavoro dal PC. Quale pezzo prendi?", ["La RAM, dagli slot lunghi", "L'hard disk", "La ventola", "L'alimentatore"], "", "pezzi"),
      C("pc", "Il PC scalda e si spegne da solo. Quale pezzo controlli?", ["Il dissipatore e la ventola della CPU", "Il lettore DVD", "Il cavo di rete", "La tastiera"], "", "raffredda"),
      C("pc", "Qual è il «cervello» che fa i calcoli?", ["La CPU (processore)", "La RAM", "L'hard disk", "La ventola"], "", "pezzi"),
      C("pc", "Dove si montano TUTTI i pezzi?", ["Sulla scheda madre", "Nel DVD", "Sullo schermo", "Nel muro"], "", "pezzi"),
      C("pc", "Il lettore DVD e l'hard disk si collegano con quale cavo?", ["Il cavo SATA", "Il cavo della corrente del muro", "Il cavo HDMI", "Nessun cavo"], "", "collega"),
      C("pc", "Cosa conserva i file anche a PC spento?", ["L'hard disk / SSD", "La RAM", "La ventola", "L'alimentatore"], "", "pezzi")
    ],
    scale: [
      { area: "parere", q: "Quanto ti sei sentita sicura sui pezzi del PC?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [],
    recupero: [
      C("pc", "La CPU è…", ["il cervello che fa i calcoli", "un cavo", "la ventola"], "", "pezzi"),
      C("pc", "La RAM è…", ["la memoria veloce di lavoro", "dove salvi i file per sempre", "l'alimentatore"], "", "pezzi"),
      C("pc", "L'hard disk…", ["conserva i file anche a PC spento", "raffredda la CPU", "dà la corrente"], "", "pezzi"),
      C("pc", "L'alimentatore…", ["dà la corrente a tutti i pezzi", "legge i DVD", "fa i calcoli"], "", "pezzi"),
      C("pc", "Tutti i pezzi si montano…", ["sulla scheda madre", "nel lettore DVD", "nella ventola"], "", "pezzi")
    ]
  };
})();
