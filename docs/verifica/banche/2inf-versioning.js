// 2INF · Verifica su versioni, Pull Request, backlog e metodo Agile (13/10/2026). Solo italiano.
// Le crocette sono uguali per tutti (in ordine diverso). Le prime due domande scritte cambiano da ragazzo a ragazzo:
// ognuno ragiona su una versione diversa del treno, così non si può copiare dal compagno.
(function () {
  var VERSIONI = [
    ["v0.12", "La versione serale: il cielo del tramonto"], ["v0.13", "A ogni livello cambia lo scenario"],
    ["v0.14", "L'ultimo colpo quando il vetro si spacca"], ["v0.15", "La difficoltà cresce a ogni livello"],
    ["v0.16", "Il vetro regge 10 colpi"], ["v0.17", "I cattivi non nascono più troppo vicino"],
    ["v0.18", "BANG! e il cattivo cade a terra"], ["v0.19", "Il mirino rosso"],
    ["v0.20", "I cattivi si vedono sempre"], ["v0.21", "Le luci dei palazzi non lampeggiano più"],
    ["v0.22", "Il record accanto ai punti"], ["v0.23", "Il bottone Pausa"],
    ["v0.24", "Più avanti, più punti"], ["v0.25", "Colpo preciso in testa: punti bonus"],
    ["v0.26", "Pioggia e nebbia"], ["v0.27", "Binari gialli"],
    ["v0.28", "La barra del prossimo livello"], ["v0.29", "Le statistiche a fine partita"],
    ["v0.30", "La sfera d'oro: punti x2"], ["v0.31", "Gli uccelli nel cielo"]
  ];
  var GIOCA = "https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/versioni/";
  function C(q, o, spiega) { return { q: q, o: o, a: 0, spiega: spiega }; }
  window.BANCA = {
    id: "2inf-versioning-20261013",
    classe: "2INF",
    titolo: "Verifica: versioni, Pull Request e backlog",
    sotto: "2INF · 13/10/2026 · 12 domande a crocetta e 3 da scrivere con parole tue",
    intro: "È la verifica sul lavoro di lunedì: le versioni del treno, le Pull Request e il backlog. Hai tempo fino alla fine dell'ora. Puoi tenere aperta la pagina «Revisione delle versioni» solo per la domanda scritta 1, se il prof lo dice.",
    minuti: 50,
    punti_crocette: 60,
    voto_min: 40,
    modulo: "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform",   // Modulo «Consegna» generico
    crocette: [
      C("Una versione del programma è…", ["un salvataggio con un numero e la descrizione di cosa cambia", "una copia di riserva senza nome", "un errore del programma"], "Ogni versione ha un numero (per esempio v0.26) e una riga che dice cosa cambia."),
      C("Da v0.30 a v0.31 il cambio è…", ["piccolo (minor)", "grande (major)"], "Cambia solo il numero dopo il punto: è un passo piccolo."),
      C("Da v1.4 a v2.0 il cambio è…", ["grande (major)", "piccolo (minor)"], "Cambia il primo numero: è un cambio grande, per esempio un motore nuovo come Godot."),
      C("Il changelog è…", ["il registro delle modifiche di ogni versione", "l'elenco dei giocatori", "la lista dei voti"], "Change = cambio, log = registro: dice cosa è cambiato in ogni versione."),
      C("Una Pull Request è…", ["una richiesta di modifica scritta", "un messaggio al prof per chiedere il voto", "una copia del gioco"], "Si chiede di cambiare il programma; chi lo cura decide se accettarla."),
      C("Una Pull Request scritta bene ha quattro parti:", ["Titolo, Cosa cambia, Dove, Perché", "Nome, Cognome, Classe, Data", "Inizio, Svolgimento, Fine, Firma"], "Senza «Dove» e «Perché» chi scrive il codice non sa cosa fare."),
      C("Il peso di una richiesta nel backlog misura…", ["quanto lavoro sul codice serve", "quanto è importante chi la chiede", "quanto è bella l'idea"], "1 un testo o un colore, 2 un numero, 3 un personaggio, 5 un ambiente, 8 una regola nuova."),
      C("Quale richiesta passa per prima?", ["i binari gialli (peso 1)", "un ambiente nuovo (peso 5)", "una regola nuova del gioco (peso 8)"], "Prima le richieste più leggere: escono subito e il gioco migliora a piccoli passi."),
      C("Due richieste hanno lo stesso peso: quale passa prima?", ["quella arrivata prima", "quella di chi ha il voto più alto", "una a caso"], "Ogni richiesta vale uno, chiunque la faccia: a parità di peso conta l'ordine di arrivo."),
      C("fork vuol dire…", ["una copia del progetto per lavorarci senza toccare l'originale", "unire due rami", "cancellare una versione"], "La 3INF ha fatto un fork del treno della 2INF."),
      C("merge vuol dire…", ["unire un ramo dentro un altro", "copiare il progetto", "tornare alla versione di prima"], "Merge = fondere: le modifiche di un ramo entrano nell'altro."),
      C("«Sbagliare presto, correggere presto» (metodo Agile) vuol dire…", ["fare piccoli passi, farli vedere e correggere subito", "pubblicare solo quando è tutto perfetto", "non correggere mai gli errori"], "Per questo lunedì i voti e il backlog erano pubblici durante la lezione.")
    ],
    aperte: [
      function (r) {
        var v = VERSIONI[Math.floor(r() * VERSIONI.length)];
        return { q: "La tua versione è la <b>" + v[0] + "</b> «" + v[1] + "». Giocala (<a href='" + GIOCA + v[0] + "/' target='_blank'>apri la " + v[0] + "</a>). Scrivi: che cosa è cambiato rispetto alla versione prima, e perché il gioco è migliorato o peggiorato.",
          aiuto: "Almeno 30 parole. Racconta cosa hai visto tu giocando: non esiste una risposta uguale per tutti.", min_parole: 30, punti: 14,
          criteri: "descrive il cambio vero della versione (5); dice cosa ha visto giocando (5); dà un giudizio motivato (4)." };
      },
      function (r) {
        var v = VERSIONI[Math.floor(r() * VERSIONI.length)];
        return { q: "Scrivi una Pull Request per migliorare la <b>" + v[0] + "</b> «" + v[1] + "», con le quattro parti: <b>Titolo · Cosa cambia · Dove · Perché</b>.",
          aiuto: "Almeno 25 parole. Una riga per ogni parte. Il «Dove» deve dire in che punto del gioco (schermata, livello, scenario).", min_parole: 25, punti: 13,
          criteri: "quattro parti presenti (4); cosa cambia chiaro e realizzabile (4); dove preciso (3); perché motivato (2)." };
      },
      { q: "Con parole tue: perché un'azienda di software lavora a versioni e con le Pull Request, invece di cambiare il programma e basta? Fai un esempio preso da lunedì.",
        aiuto: "Almeno 30 parole. Usa un esempio vero: una tua richiesta, una versione, il backlog.", min_parole: 30, punti: 13,
        criteri: "spiega a cosa servono le versioni (tornare indietro, sapere chi ha cambiato cosa) (5); spiega a cosa serve la PR (decidere prima di cambiare) (4); esempio vero di lunedì (4)." }
    ]
  };
})();
