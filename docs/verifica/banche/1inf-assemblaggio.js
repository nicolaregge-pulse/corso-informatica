// 1INF · Montiamo il computer — ripasso + test sui pezzi del PC (16/10/2026).
// Dopo il lab di assemblaggio: ripasso, verifica (test), recupero. Frasi semplici, anti-IA sulle aperte.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  window.BANCA = {
    id: "1inf-assemblaggio-v1",
    classe: "1INF",
    titolo: "Montiamo il computer — i pezzi del PC",
    sotto: "1INF · 16/10/2026 · ripasso, test e recupero",
    stato: "stato/1inf-assemblaggio.json",
    risultati: "risultati.html?b=1inf-assemblaggio",
    minuti: 12,
    anteprima: "116101316",
    aree: {
      pc: { nome: "I pezzi del computer", peso: 100 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { pezzi: 1, raffredda: 2, collega: 3 },
    schede: [
      { titolo: "1. Il cervello e la memoria", testo: "La <b>CPU</b> (processore) è il <b>cervello</b>: fa i calcoli. La <b>RAM</b> è la <b>memoria veloce di lavoro</b>: si infila negli slot lunghi della scheda madre. L'<b>hard disk</b> (o SSD) <b>conserva i tuoi file</b> (foto, giochi): non si cancella quando spegni." },
      { titolo: "2. Corrente e raffreddamento", testo: "L'<b>alimentatore</b> dà la <b>corrente</b> a tutti i pezzi. La CPU si scalda, quindi sopra ha il <b>dissipatore</b> + la <b>ventola</b> che la <b>raffreddano</b> buttando fuori l'aria calda." },
      { titolo: "3. Dove si monta e come si collega", testo: "La <b>scheda madre</b> è la base dove si <b>montano tutti i pezzi</b>. Il <b>lettore DVD</b> e l'<b>hard disk</b> stanno sulla <b>slitta</b> e si collegano alla scheda madre col <b>cavo SATA</b>." }
    ],
    via: C("pc", "Qual è il «cervello» del computer?", ["La CPU (processore)", "La ventola", "Il cavo"], "Fa tutti i calcoli."),
    prepara: [
      { q: "Scrivi, con parole tue, cosa hai smontato e rimontato oggi al banco.", min: 8 },
      { q: "A cosa serve la RAM? E l'hard disk? Spiega la differenza con parole tue.", min: 8 }
    ],
    allenamento: [
      S(1, C("pc", "La RAM si infila…", ["negli slot lunghi della scheda madre", "nel lettore DVD", "nell'alimentatore"], "È la memoria di lavoro.")),
      S(2, C("pc", "Cosa conserva i tuoi file anche a PC spento?", ["l'hard disk / SSD", "la RAM", "la ventola"], "La RAM invece si svuota.")),
      S(3, C("pc", "Cosa raffredda la CPU?", ["dissipatore + ventola", "l'hard disk", "il cavo SATA"], "")),
      S(4, C("pc", "Chi dà la corrente a tutti i pezzi?", ["l'alimentatore", "la CPU", "la RAM"], ""))
    ],
    crocette: [
      C("pc", "Apri il PC e devi togliere la memoria di lavoro. Quale pezzo prendi?", ["La RAM, dagli slot lunghi", "L'hard disk", "La ventola", "L'alimentatore"], "", "pezzi"),
      C("pc", "Il PC si spegne da solo quando lavora tanto e scalda. Quale pezzo controlli?", ["Il dissipatore e la ventola della CPU", "Il lettore DVD", "Il cavo di rete", "La tastiera"], "", "raffredda"),
      C("pc", "Vuoi aggiungere spazio per salvare tanti file e giochi. Cosa cambi/aggiungi?", ["Un hard disk o SSD più grande", "Più ventole", "Un alimentatore più piccolo", "Un cavo più lungo"], "", "pezzi"),
      C("pc", "Hai in mano la scheda madre. A cosa serve?", ["È la base dove si montano tutti i pezzi", "Conserva i file", "Dà la corrente", "Raffredda la CPU"], "", "pezzi"),
      C("pc", "Il lettore DVD e l'hard disk si collegano alla scheda madre con quale cavo?", ["Il cavo SATA", "Il cavo della corrente del muro", "Il cavo HDMI dello schermo", "Nessun cavo"], "", "collega"),
      C("pc", "Qual è il «cervello» che fa i calcoli?", ["La CPU (processore)", "La RAM", "L'hard disk", "La ventola"], "", "pezzi"),
      C("pc", "La ventola serve a…", ["buttare fuori l'aria calda e raffreddare", "salvare le foto", "dare la corrente", "leggere i DVD"], "", "raffredda"),
      C("pc", "Quando spegni il PC, cosa si CANCELLA perché è solo memoria di lavoro?", ["La RAM", "L'hard disk", "La scheda madre", "L'alimentatore"], "", "pezzi")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti sicuro sui pezzi del computer dopo averlo montato?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [],
    recupero: [
      C("pc", "La CPU è…", ["il cervello che fa i calcoli", "un cavo", "la ventola"], "", "pezzi"),
      C("pc", "La RAM è…", ["la memoria veloce di lavoro", "dove salvi i file per sempre", "l'alimentatore"], "", "pezzi"),
      C("pc", "L'hard disk…", ["conserva i file anche a PC spento", "raffredda la CPU", "dà la corrente"], "", "pezzi"),
      C("pc", "L'alimentatore…", ["dà la corrente a tutti i pezzi", "legge i DVD", "fa i calcoli"], "", "pezzi"),
      C("pc", "Tutti i pezzi si montano…", ["sulla scheda madre", "dentro il lettore DVD", "nella ventola"], "", "pezzi")
    ]
  };
})();
