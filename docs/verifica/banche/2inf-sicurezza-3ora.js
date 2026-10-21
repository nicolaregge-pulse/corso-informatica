// 2INF · Sicurezza sul lavoro — 3ª ora (Regione): organizzazione della prevenzione aziendale (21/10/2026).
// Teoria ufficiale sul sito della formazione (3ª ora); qui ripasso + verifica di 20 casi a scenario, anti-IA:
// incolla bloccato, ordine personale, tempo e uscite misurati, due domande sulla PROPRIA aula. Solo italiano (2INF).
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  window.BANCA = {
    id: "2inf-sicurezza-3ora-v1",
    classe: "2INF",
    titolo: "Sicurezza sul lavoro — 3ª ora: l'organizzazione della prevenzione in azienda",
    sotto: "2INF · 21/10/2026 · prima la teoria ufficiale, poi il ripasso e la verifica",
    stato: "stato/2inf-sicurezza-3ora.json",
    risultati: "risultati.html?b=2inf-sicurezza-3ora",
    minuti: 20,
    anteprima: "868848605",
    aree: {
      sic: { nome: "Sicurezza: come si organizza la prevenzione", peso: 80 },
      mia: { nome: "La sicurezza nella mia aula (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { spp: 1, dvr: 2, emergenze: 3, formazione: 4 },
    schede: [
      { titolo: "1. La squadra della prevenzione", testo: "Prima studia la <b>3ª ora</b> sul sito ufficiale della formazione: <a href=\"https://sites.google.com/piamarta.it/formazionesicurezzamilano/3-ora\" target=\"_blank\" rel=\"noopener\">apri la teoria (si apre in una scheda nuova)</a>.<br><br>In azienda la sicurezza è organizzata come una squadra. Il <b>datore di lavoro</b> decide e risponde. Il <b>Servizio di Prevenzione e Protezione</b> (SPP), guidato dal <b>RSPP</b>, studia i rischi e propone le soluzioni. Il <b>medico competente</b> controlla la salute. Il <b>RLS</b> parla a nome dei lavoratori. I <b>preposti</b> controllano sul campo." },
      { titolo: "2. Il DVR: la mappa dei rischi", testo: "Il <b>DVR</b> (Documento di Valutazione dei Rischi) è il documento dove l'azienda scrive <b>tutti i rischi</b> di ogni lavoro e <b>che cosa fa</b> per ridurli. Lo firma il datore di lavoro, con l'RSPP e il medico competente, sentito l'RLS. Il datore di lavoro <b>non può delegarlo</b> a nessuno. Si aggiorna quando cambia qualcosa: una macchina nuova, un reparto nuovo, dopo un infortunio. Almeno <b>una volta l'anno</b> c'è la <b>riunione periodica</b> della squadra della sicurezza." },
      { titolo: "3. Le emergenze: chi interviene", testo: "Ogni azienda ha gli <b>addetti alle emergenze</b>: gli <b>addetti antincendio</b> (usano gli estintori e guidano l'evacuazione) e gli <b>addetti al primo soccorso</b> (aiutano chi si fa male e chiamano il <b>112</b>). C'è un <b>piano di emergenza</b>: vie di fuga, <b>uscite di emergenza</b> con il cartello verde, <b>punto di raccolta</b> fuori dall'edificio. Durante l'evacuazione: niente ascensore, niente corsa, non si torna indietro a prendere le cose." },
      { titolo: "4. Formazione, informazione, addestramento", testo: "<b>Informazione</b>: ti dicono quali rischi ci sono e chi sono le persone della sicurezza. <b>Formazione</b>: un corso per capire (come questo: 4 ore generali + le ore specifiche). <b>Addestramento</b>: provi davvero, con le mani, l'attrezzo o il DPI, con qualcuno che ti guarda. Si fanno <b>durante l'orario di lavoro</b> e <b>non costano niente al lavoratore</b>. Valgono anche per lo <b>studente in stage</b>." }
    ],
    via: C("sic", "Il documento dove l'azienda scrive tutti i rischi si chiama…", ["DVR", "INAIL", "DPI"], "Documento di Valutazione dei Rischi."),
    prepara: [
      { q: "Con parole tue: che cos'è il DVR?", min: 6 },
      { q: "Chi sono gli addetti alle emergenze?", min: 6 }
    ],
    allenamento: [
      S(1, C("sic", "Il SPP è guidato da…", ["l'RSPP", "il medico competente", "il cliente"], "Il Responsabile del Servizio di Prevenzione e Protezione.")),
      S(2, C("sic", "Il DVR lo può delegare il datore di lavoro?", ["No, mai: è un suo obbligo", "Sì, al lavoratore più giovane", "Sì, a un cliente"], "")),
      S(3, C("sic", "Durante un'evacuazione l'ascensore…", ["non si usa", "si usa, è più veloce", "si usa solo al primo piano"], "")),
      S(4, C("sic", "Provare davvero un attrezzo con qualcuno che ti guarda è…", ["addestramento", "informazione", "una sanzione"], ""))
    ],
    crocette: [
      C("sic", "Primo giorno di stage. Nessuno ti ha detto dove sono le uscite di emergenza. Che cosa fai?", ["Chiedo al tutor o al preposto: ho diritto all'informazione", "Niente, se succede qualcosa seguo gli altri", "Me le cerco quando c'è l'allarme", "Esco dalla finestra se serve"], "", "formazione"),
      C("sic", "Suona l'allarme antincendio mentre sei al computer. Qual è la cosa GIUSTA?", ["Lascio tutto, seguo la via di fuga e vado al punto di raccolta", "Finisco di salvare il lavoro e poi esco", "Prendo l'ascensore per fare prima", "Resto al posto e aspetto"], "", "emergenze"),
      C("sic", "Arrivato al punto di raccolta ti accorgi di aver lasciato il telefono in aula. Che fai?", ["Resto al punto di raccolta: non si torna mai indietro", "Torno a prenderlo di corsa", "Mando un compagno a prenderlo", "Rientro dall'uscita di emergenza"], "", "emergenze"),
      C("sic", "Un collega si taglia una mano e perde sangue. Chi deve intervenire per primo?", ["L'addetto al primo soccorso, che se serve chiama il 112", "Il cliente più vicino", "L'RLS, perché è eletto dai colleghi", "Nessuno: si aspetta la fine del turno"], "", "emergenze"),
      C("sic", "Esce un po' di fumo da una ciabatta elettrica. Chi usa l'estintore?", ["L'addetto antincendio, che è formato a farlo", "Chiunque, anche senza aver mai provato", "Il primo che passa, con l'acqua", "Nessuno: si aspetta che si spenga"], "", "emergenze"),
      C("sic", "Il numero unico per le emergenze in Italia e in Europa è…", ["112", "118 solo per gli incendi", "1500", "Il numero del capo"], "", "emergenze"),
      C("sic", "L'azienda compra una macchina nuova, più pericolosa. Che cosa deve fare con il DVR?", ["Aggiornarlo, valutando i nuovi rischi", "Niente: il DVR si scrive una volta sola", "Buttarlo e non rifarlo", "Aspettare il primo infortunio"], "", "dvr"),
      C("sic", "Chi FIRMA il DVR e ne risponde?", ["Il datore di lavoro", "Lo studente in stage", "L'INAIL", "Il fornitore della macchina"], "", "dvr"),
      C("sic", "Il titolare dice: «Il DVR lo scrive il ragazzo nuovo, io non ho tempo». È giusto?", ["No: il datore di lavoro non può delegare la valutazione dei rischi", "Sì, lo può scrivere chiunque", "Sì, se il ragazzo è bravo con il computer", "Sì, basta che lo firmi il cliente"], "", "dvr"),
      C("sic", "A che cosa serve il DVR?", ["A scrivere i rischi di ogni lavoro e le misure per ridurli", "A segnare gli orari di entrata e uscita", "A elencare gli stipendi", "A fare la pubblicità all'azienda"], "", "dvr"),
      C("sic", "Almeno una volta all'anno la squadra della sicurezza si incontra. Come si chiama?", ["Riunione periodica", "Festa aziendale", "Colloquio di lavoro", "Ispezione dell'INAIL"], "", "dvr"),
      C("sic", "Chi guida il Servizio di Prevenzione e Protezione?", ["L'RSPP", "Il medico competente", "L'RLS", "Il preposto"], "", "spp"),
      C("sic", "L'RSPP ti propone di cambiare il modo in cui sposti i PC pesanti. Che ruolo ha?", ["Studia i rischi e consiglia le soluzioni, ma non comanda", "Comanda l'azienda", "Fa le visite mediche", "Controlla l'azienda da fuori, per lo Stato"], "", "spp"),
      C("sic", "Vuoi segnalare un problema di sicurezza senza esporti da solo con il capo. A chi ti rivolgi?", ["All'RLS, il rappresentante eletto dai lavoratori", "Al cliente", "All'addetto antincendio", "A nessuno: non si può"], "", "spp"),
      C("sic", "Ti spiegano a voce quali rischi ci sono nel reparto e chi è l'addetto al primo soccorso. Questa è…", ["Informazione", "Addestramento", "Una sanzione", "La riunione periodica"], "", "formazione"),
      C("sic", "Il tutor ti fa provare a montare un PC con il braccialetto antistatico e ti guarda mentre lo fai. Questo è…", ["Addestramento", "Informazione", "Il DVR", "Il punto di raccolta"], "", "formazione"),
      C("sic", "Il capo: «Il corso sulla sicurezza lo fai sabato, gratis per noi, pagato da te». È giusto?", ["No: la formazione si fa in orario di lavoro e non costa niente al lavoratore", "Sì, la formazione la paga sempre il lavoratore", "Sì, se il corso è di sabato", "Sì, ma solo per gli studenti in stage"], "", "formazione"),
      C("sic", "Lo studente in stage deve ricevere formazione e informazione sulla sicurezza?", ["Sì: per la sicurezza è trattato come un lavoratore", "No: è solo uno studente", "Solo se lo chiede la famiglia", "Solo dopo un mese di stage"], "", "formazione"),
      C("sic", "Davanti all'uscita di emergenza ci sono degli scatoloni. Che cosa fai?", ["Lo segnalo subito al preposto: le vie di fuga devono restare libere", "Niente, tanto c'è un'altra porta", "Li sposto sopra l'estintore", "Ci metto anche i miei"], "", "emergenze"),
      C("sic", "Il cartello delle uscite di emergenza e del primo soccorso è di colore…", ["Verde", "Rosso", "Giallo", "Blu"], "", "emergenze")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti pronto se domani suona un allarme al lavoro?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "mia", tema: "aula", q: "Guarda la TUA aula di adesso. Dov'è l'uscita di emergenza più vicina al tuo posto? Che strada fai per arrivarci? Descrivila con parole tue.", aiuto: "Almeno 20 parole: da dove parti, dove giri, che cosa vedi.", min_parole: 20,
        criteri: "descrive un percorso concreto dalla propria postazione; cita l'uscita o il cartello verde" },
      { area: "mia", tema: "pericolo", q: "Scrivi UN pericolo che vedi nella tua aula (cavi, prese, sedie, zaini…) e a chi lo segnaleresti in un'azienda. Perché proprio a lui?", aiuto: "Almeno 20 parole: il pericolo, la persona (preposto, RLS…), il perché.", min_parole: 20,
        criteri: "pericolo concreto dell'aula; persona corretta (preposto o RLS); motivazione" }
    ],
    recupero: [
      C("sic", "Il DVR è…", ["il documento con i rischi e le misure", "un tipo di estintore", "un ente che assicura"], "", "dvr"),
      C("sic", "Durante l'evacuazione si va…", ["al punto di raccolta, senza ascensore", "in ascensore", "a casa"], "", "emergenze"),
      C("sic", "Chi interviene se qualcuno si fa male?", ["l'addetto al primo soccorso", "il cliente", "nessuno"], "", "emergenze"),
      C("sic", "La formazione sulla sicurezza…", ["è gratis e in orario di lavoro", "la paga il lavoratore", "non serve agli stagisti"], "", "formazione"),
      C("sic", "L'RSPP…", ["studia i rischi e consiglia", "comanda l'azienda", "fa le visite"], "", "spp")
    ]
  };
})();
