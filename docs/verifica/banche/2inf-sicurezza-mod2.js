// 2INF · Sicurezza sul lavoro — Modulo 2: i soggetti e i doveri (16/10/2026).
// Verifica obbligatoria (Regione): teoria + verifica. Casi a scenario, anti-IA. Incolla bloccato, tempo e uscite misurati.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  window.BANCA = {
    id: "2inf-sicurezza-mod2-v1",
    classe: "2INF",
    titolo: "Sicurezza sul lavoro — Modulo 2: i soggetti e i doveri",
    sotto: "2INF · 16/10/2026 · ripasso, verifica e recupero",
    stato: "stato/2inf-sicurezza-mod2.json",
    risultati: "risultati.html?b=2inf-sicurezza-mod2",
    minuti: 15,
    anteprima: "868848605",
    aree: {
      sic: { nome: "Sicurezza: chi fa cosa e i tuoi doveri", peso: 100 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { soggetti: 1, doveri: 2, organi: 3 },
    schede: [
      { titolo: "1. Chi si occupa della sicurezza", testo: "Il <b>datore di lavoro</b> è il primo responsabile. Il <b>dirigente</b> organizza; il <b>preposto</b> (capo-reparto) controlla sul campo. Il <b>RSPP</b> è l'esperto che studia i rischi. Il <b>medico competente</b> fa le visite. Il <b>RLS</b> è eletto dai colleghi ed è la loro voce." },
      { titolo: "2. I tuoi diritti e doveri", testo: "<b>Diritti</b> del lavoratore (anche in stage): formazione, informazione, <b>DPI gratis</b>, visita medica. <b>Doveri</b>: rispettare le regole, non togliere le protezioni, usare i DPI, <b>segnalare i pericoli</b>." },
      { titolo: "3. Chi controlla da fuori", testo: "Gli <b>organi di vigilanza</b> (ASL/ATS, Ispettorato del lavoro) controllano dall'esterno. L'<b>INAIL</b> assicura: se ti fai male sul lavoro, ti aiuta economicamente." }
    ],
    via: C("sic", "Chi è il PRIMO responsabile della sicurezza?", ["Il datore di lavoro", "Lo studente in stage", "Il cliente"], "Chi comanda e decide."),
    prepara: [
      { q: "Scrivi due doveri del lavoratore, con parole tue.", min: 6 },
      { q: "A cosa serve l'INAIL?", min: 5 }
    ],
    allenamento: [
      S(1, C("sic", "Il preposto…", ["controlla sul campo e corregge subito", "fa le visite mediche", "assicura i lavoratori"], "È il capo-reparto.")),
      S(2, C("sic", "I DPI (guanti, scarpe…)…", ["li dà l'azienda, gratis", "li paga il lavoratore", "non servono"], "È un diritto.")),
      S(3, C("sic", "L'INAIL…", ["assicura se ti fai male sul lavoro", "fa le visite", "vende i DPI"], ""))
    ],
    crocette: [
      C("sic", "Primo giorno di stage. Il capo: «guanti e scarpe compratele tu». Che pensi?", ["No: i DPI me li deve dare l'azienda, gratis (è un mio diritto)", "Va bene, i DPI li paga il lavoratore", "Li compro solo se mi fanno male le mani", "Non servono, basta stare attenti"], "", "doveri"),
      C("sic", "Nel reparto c'è un cavo elettrico scoperto per terra. Qual è la cosa GIUSTA?", ["Non toccarlo e segnalarlo subito al preposto", "Aggiustarlo da solo in fretta", "Coprirlo con lo scotch e continuare", "Lasciar stare, non è un problema mio"], "", "doveri"),
      C("sic", "Un collega usa il trapano SENZA occhiali. Tu sei studente in stage. Che fai?", ["Lo dico al preposto o avviso il collega: segnalare è un dovere di tutti", "Niente: sono in stage, non è compito mio", "Prendo gli occhiali e li metto io al posto suo", "Filmo la scena col telefono"], "", "doveri"),
      C("sic", "Il preposto ti dà un attrezzo nuovo senza spiegarti come si usa e dice «sbrigati». Tu…", ["Mi fermo e chiedo le istruzioni/formazione: ho diritto a lavorare sicuro", "Lo uso comunque per non fare brutta figura", "Mi rifiuto e me ne vado a casa", "Chiedo a un compagno di usarlo al posto mio"], "", "doveri"),
      C("sic", "Chi è il PRIMO responsabile della sicurezza in azienda?", ["Il datore di lavoro", "Lo studente in stage", "Il cliente", "Nessuno: è facoltativa"], "", "soggetti"),
      C("sic", "Il capo-reparto che ti controlla sul campo e corregge subito: che ruolo ha?", ["Preposto", "Medico competente", "RSPP", "RLS"], "", "soggetti"),
      C("sic", "Un esperto studia i rischi e consiglia come difendersi, ma non comanda. Chi è?", ["Il RSPP", "Il datore di lavoro", "Il medico competente", "Un cliente"], "", "soggetti"),
      C("sic", "Ti chiamano per una visita per controllare la tua salute al lavoro. Chi la fa?", ["Il medico competente", "Il preposto", "L'RLS", "L'INAIL"], "", "soggetti"),
      C("sic", "I colleghi votano uno di voi per parlare con l'azienda dei problemi di sicurezza. È…", ["Il RLS (rappresentante dei lavoratori per la sicurezza)", "Il titolare", "Un medico esterno", "Un ispettore dello Stato"], "", "soggetti"),
      C("sic", "Chi può venire DA FUORI a controllare che l'azienda rispetti la sicurezza?", ["Gli organi di vigilanza: ASL/ATS e Ispettorato del lavoro", "Nessuno: dentro decide solo il titolare", "I clienti", "I fornitori"], "", "organi"),
      C("sic", "Ti fai male a una mano con una macchina al lavoro. Quale ente ti aiuta economicamente?", ["L'INAIL", "L'RLS", "Il medico competente", "Il negozio dei DPI"], "", "organi"),
      C("sic", "La sedia è rotta e ti viene mal di schiena. Che cosa fai PER PRIMO?", ["Lo segnalo al preposto (e posso rivolgermi all'RLS)", "Niente: il mal di schiena è normale", "Cambio lavoro", "Aspetto che se ne accorgano gli altri"], "", "doveri"),
      C("sic", "Il capo: «Salta la formazione sulla sicurezza, così iniziamo prima». Tu…", ["La formazione è un mio diritto e un dovere: non si salta", "Va bene, decide lui", "La faccio un'altra volta, non è importante", "La faccio solo se mi pagano di più"], "", "doveri"),
      C("sic", "Un cliente entra in area pericolosa senza scarpe antinfortunistiche. Che cosa è giusto?", ["Va avvisato e fermato: la sicurezza vale anche per chi entra", "I clienti non c'entrano con la sicurezza", "Non è un problema, sta poco", "Gli presto le mie scarpe"], "", "doveri")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti sicuro su chi fa cosa e sui tuoi doveri?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [],
    recupero: [
      C("sic", "Il datore di lavoro è…", ["il primo responsabile della sicurezza", "un cliente", "un ispettore"], "", "soggetti"),
      C("sic", "I DPI li dà…", ["l'azienda, gratis", "il lavoratore, pagandoli", "nessuno"], "", "doveri"),
      C("sic", "Se vedi un pericolo, come lavoratore devi…", ["segnalarlo subito", "far finta di niente", "aspettare"], "", "doveri"),
      C("sic", "Il RLS è…", ["eletto dai colleghi, la loro voce", "il titolare", "un medico"], "", "soggetti"),
      C("sic", "L'INAIL…", ["assicura in caso di infortunio", "fa le visite", "vende i DPI"], "", "organi")
    ]
  };
})();
