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
      { t: "🔧 Verifica 1 — monta il PC nel simulatore", u: "../monta-pc-v3/?id=prova-sim", c: "#2ea043" }
    ],
    aree: {
      pc: { nome: "I pezzi del computer", peso: 100 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { pezzi: 1, raffredda: 2, collega: 3 },
    schede: [
      { titolo: "0. Partiamo da zero: cos'è un computer", testo: "Un computer fisso è una <b>scatola</b> (si chiama <b>case</b> o cabinet) che contiene tanti pezzi collegati tra loro. Ogni pezzo fa una cosa precisa. In questa prova impari <b>a cosa serve ogni pezzo</b> e <b>come si montano</b>. Non devi sapere niente prima: leggi con calma, qui c'è tutto." },
      { titolo: "1. La scheda madre — la base di tutto", testo: "La <b>scheda madre</b> (in inglese <i>motherboard</i>) è la <b>grande piastra</b> su cui si <b>attaccano tutti gli altri pezzi</b>. È come il banco di lavoro: CPU, RAM, dischi e cavi finiscono tutti lì sopra o collegati a lei. Senza scheda madre i pezzi non si parlano." },
      { titolo: "2. La CPU — il cervello", testo: "La <b>CPU</b> (si dice «ci-pi-u», in italiano <b>processore</b>) è il <b>cervello</b>: fa tutti i <b>calcoli</b>, cioè fa funzionare i programmi. Si incastra in uno zoccolo quadrato al centro della scheda madre. È il pezzo più importante per la velocità." },
      { titolo: "3. Dissipatore e ventola — il raffreddamento", testo: "La CPU lavorando <b>si scalda</b> molto. Per non bruciarsi, sopra ci mettiamo il <b>dissipatore</b> (un blocco di metallo che toglie il calore) e una <b>ventola</b> che <b>soffia via l'aria calda</b>. Se il raffreddamento manca, il PC si spegne da solo per protezione." },
      { titolo: "4. La RAM — la memoria di lavoro", testo: "La <b>RAM</b> è la <b>memoria veloce di lavoro</b>: tiene i dati di quello che stai facendo <b>in questo momento</b>. Sono barrette lunghe che si infilano negli <b>slot lunghi</b> della scheda madre. Attenzione: quando <b>spegni</b> il PC, la RAM <b>si svuota</b> (non conserva niente)." },
      { titolo: "5. Hard disk / SSD — dove si conservano i file", testo: "L'<b>hard disk</b> (o il più moderno <b>SSD</b>) è la memoria che <b>conserva i tuoi file</b> — foto, musica, giochi, programmi — <b>anche a PC spento</b>. È la differenza con la RAM: la RAM è il tavolo di lavoro (si sgombra), il disco è l'armadio (resta)." },
      { titolo: "6. L'alimentatore — la corrente", testo: "L'<b>alimentatore</b> (in inglese <i>PSU</i>) prende la corrente dalla presa del muro e la <b>distribuisce a tutti i pezzi</b> nella giusta quantità. È la scatola con la ventola e tanti cavi. Senza di lui niente si accende." },
      { titolo: "7. Scheda video, DVD, slitta e cavo SATA", testo: "La <b>scheda video</b> (o <i>GPU</i>) serve a mostrare <b>immagini e giochi</b> sullo schermo. Il <b>lettore DVD</b> legge i dischi. DVD e hard disk stanno su una <b>slitta</b> (un supporto che scorre) e si collegano alla scheda madre con il <b>cavo SATA</b> (un cavetto piatto)." },
      { titolo: "8. Come si monta (l'ordine)", testo: "In pratica: 1) si fissa la <b>scheda madre</b> nel case; 2) si mette la <b>CPU</b> nello zoccolo e sopra <b>dissipatore + ventola</b>; 3) si infila la <b>RAM</b> negli slot; 4) si montano <b>dischi e DVD</b> sulla slitta; 5) si mette l'<b>alimentatore</b> e si <b>collegano i cavi</b> (corrente e SATA). Alla fine si accende." },
      { titolo: "9. Adesso le due verifiche", testo: "Ora tocca a te, in due passi: <b>① Verifica 1 — l'assemblaggio:</b> apri il bottone verde qui sopra e <b>monta il PC nel simulatore</b> (trascina i pezzi fino a «FATTO», montane almeno 3). <b>② Verifica 2 — il quiz:</b> poi vai su «2. Verifica» e rispondi alle domande. Se sbagli parecchio, il prof ti apre un <b>recupero</b>. Coraggio: hai appena letto tutto il necessario!" }
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
