// 4TI · Ripasso ISO/OSI + verifica + la descrizione del mio progetto (20/10/2026).
// Riprende la teoria del 06/10 (classe-4/reti-iso-osi): 7 livelli, incapsulamento e PDU, MAC e IP, dispositivi,
// TCP e UDP, il metodo del tecnico dal basso verso l'alto. Poi ognuno scrive la descrizione del suo progetto di stage.
// Aree e peso nel giudizio: nozioni ISO/OSI 50%, saperlo spiegare 25%, la descrizione del mio progetto 25%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function T(righe) { return '<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0">' + righe.map(function (r, i) { return '<tr>' + r.map(function (c) { return (i ? '<td' : '<th') + ' style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">' + c + (i ? '</td>' : '</th>'); }).join('') + '</tr>'; }).join('') + '</table>'; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap">' + t.replace(/</g, '&lt;') + '</pre>'; }
  var README = "# Nome del mio progetto\n\n## Che cosa fa\nDue o tre frasi: che cosa fa il mio programma, gioco o rete.\n\n## Per chi è\nChi lo usa: un'azienda, un giocatore, un tecnico, la mia classe.\n\n## Come si usa\nI passi di chi lo usa: apro, clicco, scrivo, vedo.\n\n## Con che cosa lo faccio\nGodot, Lazarus, Python, Packet Tracer, GitHub…\n\n## La prima versione (v0.1)\nLa cosa più piccola che funziona e che posso mostrare.\n\n## Le versioni dopo\nv0.2: …  v0.3: …\n\n## Chi sono\nNome (o soprannome), classe 4ª, indirizzo informatico.";

  window.BANCA = {
    id: "4ti-iso-osi-ripasso-v1",
    classe: "4TI",
    titolo: "ISO/OSI: ripasso, verifica e la descrizione del mio progetto",
    sotto: "4TI · 20/10/2026 · i 7 livelli, l'incapsulamento, i dispositivi · poi il tuo progetto di stage",
    stato: "stato/4ti-iso-osi-ripasso.json",
    risultati: "risultati.html?b=4ti-iso-osi-ripasso",
    minuti: 25,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Nozioni ISO/OSI", peso: 50 },
      spiega: { nome: "Saperlo spiegare (solo parole tue)", peso: 25 },
      progetto: { nome: "La descrizione del mio progetto", peso: 25 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO ---------- */
    schede_temi: { livelli: 1, ricordare: 2, buste: 3, indirizzi: 4, dispositivi: 5, trasporto: 6, tecnico: 7, progetto: 8, readme: 9, ponte: 10 },
    schede: [
      { titolo: "1. I sette livelli: come spedire un pacco", testo:
        "Quando mandi un messaggio, non lo fa un solo programma: lo fanno <b>sette livelli</b>, uno sopra l'altro, come in una ditta di spedizioni. Ognuno fa il suo lavoro e passa il pacco al livello sotto." +
        T([["N.", "Livello", "Che cosa fa", "Esempio"],
           ["7", "Applicazione", "il programma che usi", "browser, WhatsApp, e-mail"],
           ["6", "Presentazione", "traduce, comprime, cifra", "JPG, MP3, HTTPS"],
           ["5", "Sessione", "apre e chiude la conversazione", "login, videochiamata"],
           ["4", "Trasporto", "divide in pezzi e controlla che arrivino", "TCP, UDP, porte"],
           ["3", "Rete", "sceglie la strada tra reti diverse", "indirizzo IP, router"],
           ["2", "Collegamento", "consegna dentro la stessa rete", "indirizzo MAC, switch"],
           ["1", "Fisico", "manda i bit sul mezzo", "cavo, Wi-Fi, fibra"]]) },
      { titolo: "2. Come ricordarli", testo:
        "Dal basso verso l'alto: <b>F</b>isico, <b>C</b>ollegamento, <b>R</b>ete, <b>T</b>rasporto, <b>S</b>essione, <b>P</b>resentazione, <b>A</b>pplicazione.<br><br>Una frase per ricordare le iniziali F-C-R-T-S-P-A: <b>«Fate Come Ragazzi Tranquilli: Studiate Prima, Applicatevi»</b>.<br><br>Due regole d'oro:<br>1. <b>In basso</b> ci sono le cose che tocchi (cavi, schede, switch); <b>in alto</b> i programmi che usi.<br>2. Chi spedisce scende dal 7 all'1; chi riceve sale dall'1 al 7." },
      { titolo: "3. L'incapsulamento: le buste", testo:
        "Scendendo, ogni livello mette i dati dentro una <b>busta</b> e ci scrive sopra le sue informazioni (l'<b>intestazione</b>). Chi riceve apre le buste al contrario.<br><br>Il pezzo di dati cambia nome a ogni livello (si chiama <b>PDU</b>):" +
        T([["Livello", "Nome del pezzo"], ["7, 6, 5", "dati"], ["4 Trasporto", "segmento"], ["3 Rete", "pacchetto"], ["2 Collegamento", "frame (trama)"], ["1 Fisico", "bit"]]) +
        "Per ricordarlo: <b>D-S-P-F-B</b>, «Dati Spediti Per Fare Bene»." },
      { titolo: "4. Due indirizzi: MAC e IP", testo:
        T([["", "MAC", "IP"],
           ["Livello", "2 Collegamento", "3 Rete"],
           ["Che cos'è", "il «numero di telaio» della scheda di rete, scritto in fabbrica", "l'«indirizzo di casa», dato dalla rete in cui sei"],
           ["Cambia?", "no, resta sempre lo stesso", "sì, se cambi rete cambia"],
           ["Esempio", "3C-52-82-1A-7F-09", "192.168.1.25"],
           ["Chi lo usa", "lo switch", "il router"]]) +
        "Il MAC serve per l'ultimo tratto, dentro la stessa rete. L'IP serve per trovare la strada da una rete all'altra." },
      { titolo: "5. I dispositivi e il loro livello", testo:
        T([["Dispositivo", "Livello", "Che cosa guarda"],
           ["cavo, hub, ripetitore", "1", "solo i bit, non capisce niente"],
           ["switch, access point", "2", "l'indirizzo MAC: manda il frame solo al PC giusto"],
           ["router", "3", "l'indirizzo IP: sceglie la strada tra reti diverse"],
           ["firewall", "3-4 (e oltre)", "IP e porte: decide chi passa e chi no"],
           ["PC, server", "da 1 a 7", "tutti i livelli"]]) +
        "Trucco: più il dispositivo «capisce», più sta in alto." },
      { titolo: "6. Trasporto: TCP o UDP", testo:
        T([["", "TCP", "UDP"],
           ["Come lavora", "controlla che tutto arrivi, in ordine; se manca un pezzo lo rimanda", "manda e basta, senza controllare"],
           ["Pregio", "affidabile", "veloce"],
           ["Si usa per", "pagine web, e-mail, file", "videochiamate, giochi online, dirette"],
           ["Paragone", "raccomandata con ricevuta", "volantino nella cassetta"]]) +
        "La <b>porta</b> dice a quale programma va il segmento: 80 e 443 sito web, 53 DNS, 25 e-mail." },
      { titolo: "7. Il metodo del tecnico: dal basso verso l'alto", testo:
        "Quando «Internet non va», il tecnico controlla i livelli <b>dal basso</b>, uno alla volta:" +
        T([["Livello", "Che cosa controllo"],
           ["1 Fisico", "cavo collegato, lucine accese, Wi-Fi attivo"],
           ["2 Collegamento", "switch o access point acceso, porta che funziona"],
           ["3 Rete", "il PC ha un IP giusto? se comincia con 169.254 non l'ha ricevuto; il router risponde?"],
           ["4-7", "il servizio funziona? se l'IP 8.8.8.8 risponde ma il sito no, è il DNS"]]) +
        "È il metodo che userai in stage: prima i cavi, poi i programmi." },
      { titolo: "8. Il mio progetto: perché scrivere la descrizione", testo:
        "Ognuno di voi ha un progetto di stage (un gioco, un programma, una rete). In un'azienda vera, prima di scrivere codice si scrive <b>la descrizione</b>: due minuti di lettura che spiegano a chiunque che cosa farai.<br><br>Serve a tre cose:<br>1. a <b>te</b>, per avere chiaro dove vai;<br>2. al <b>prof</b> e al <b>tutor dello stage</b>, per aiutarti;<br>3. a <b>un'azienda</b>, che la legge come un biglietto da visita.<br><br>Regola d'oro: la <b>prima versione (v0.1)</b> è la cosa più piccola che funziona. Meglio piccola e finita che grande e a metà." },
      { titolo: "9. Com'è fatta una descrizione (il README)", testo:
        "Su GitHub la descrizione sta nel file <b>README.md</b>, la prima pagina del repository. Oggi la scrivi qui nella verifica; poi diventa il README del tuo progetto. Lo schema:" + K(README) +
        "Scrivila con parole tue: non serve che sia lunga, serve che sia vera e chiara." },
      { titolo: "10. Il ponte verso la prossima lezione: l'indirizzo IP", testo:
        "Al livello 3 c'è l'<b>indirizzo IP</b>. La prossima volta impariamo a leggerlo davvero: indirizzo, maschera, gateway e DNS.<br><br>Prova già adesso, senza riga di comando: <b>Impostazioni → Rete e Internet → Ethernet</b> (o Wi-Fi) <b>→ Proprietà</b>. Cerca la riga «Indirizzo IPv4»: è il numero del tuo PC nella rete della scuola." }
    ],
    strumenti: [{ t: 'Il viaggio di un pacchetto (animazione)', u: '../4ti-iso-osi/viaggio.html', c: '#1f6feb' }, { t: 'I progetti della classe', u: '../4ti-progetti/', c: '#d4a017' }],
    via: C("nozioni", "Quanti sono i livelli del modello ISO/OSI?", ["7", "4", "10"], "Sette, dal Fisico all'Applicazione."),
    prepara: [
      { q: "Pensa al tuo progetto di stage: in una frase, che cosa vuoi costruire?", min: 8 }
    ],
    allenamento: [
      S(1, C("nozioni", "Il livello 1 si chiama…", ["Fisico", "Applicazione", "Rete"], "Il più in basso: i bit sul cavo.")),
      S(1, C("nozioni", "Il browser lavora al livello…", ["7 Applicazione", "1 Fisico", "3 Rete"], "È il programma che usi.")),
      S(2, C("nozioni", "Chi spedisce un messaggio, attraversa i livelli…", ["dal 7 all'1", "dall'1 al 7", "solo il 3"], "Scende; chi riceve sale.")),
      S(3, C("nozioni", "Al livello 3 il pezzo di dati si chiama…", ["pacchetto", "frame", "bit"], "D-S-P-F-B: dati, segmento, pacchetto, frame, bit.")),
      S(3, C("nozioni", "Incapsulamento vuol dire…", ["ogni livello mette i dati in una busta con la sua intestazione", "cancellare i dati", "comprimere un file"], "Le buste una dentro l'altra.")),
      S(4, C("nozioni", "L'indirizzo che resta sempre uguale, scritto in fabbrica, è…", ["il MAC", "l'IP", "la porta"], "Il MAC è il numero di telaio.")),
      S(5, C("nozioni", "Lo switch guarda…", ["l'indirizzo MAC", "l'indirizzo IP", "niente"], "Livello 2.")),
      S(5, C("nozioni", "Il dispositivo che collega reti diverse è…", ["il router", "l'hub", "il cavo"], "Livello 3, guarda l'IP.")),
      S(6, C("nozioni", "Per una videochiamata, dove conta la velocità, si usa…", ["UDP", "TCP", "HTTP"], "Meglio perdere un fotogramma che aspettare.")),
      S(7, C("nozioni", "«Internet non va». Il tecnico controlla per primo…", ["il cavo e le lucine", "il sito web", "l'antivirus"], "Dal basso verso l'alto.")),
      S(9, C("progetto", "La prima versione (v0.1) del progetto deve essere…", ["la cosa più piccola che funziona", "il progetto finito", "solo un'idea scritta"], "Piccola e finita.")),
      S(10, C("nozioni", "Il tuo IP l'hai trovato in Impostazioni → Rete. Comincia con…", ["192.168. oppure 10. oppure 172.", "169.254.", "non l'ho trovato"], "Se comincia con 169.254 il PC non ha ricevuto l'IP: chiedi all'assistente."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("nozioni", "Il livello 4 si chiama…", ["Trasporto", "Rete", "Sessione"], "", "livelli"),
      C("nozioni", "Il livello che sceglie la strada tra reti diverse è…", ["3 Rete", "2 Collegamento", "6 Presentazione"], "", "livelli"),
      C("nozioni", "HTTPS, JPG e MP3 (formati e cifratura) sono del livello…", ["6 Presentazione", "1 Fisico", "4 Trasporto"], "", "livelli"),
      C("nozioni", "L'ordine giusto dal basso è…", ["Fisico, Collegamento, Rete, Trasporto, Sessione, Presentazione, Applicazione", "Applicazione, Rete, Fisico, Trasporto, Sessione, Collegamento, Presentazione", "Rete, Fisico, Trasporto, Collegamento, Applicazione, Sessione, Presentazione"], "", "ricordare"),
      C("nozioni", "Al livello 2 il pezzo di dati si chiama…", ["frame (trama)", "segmento", "pacchetto"], "", "buste"),
      C("nozioni", "Al livello 4 il pezzo di dati si chiama…", ["segmento", "bit", "frame"], "", "buste"),
      C("nozioni", "Chi riceve il messaggio…", ["apre le buste dal livello 1 al 7", "aggiunge altre buste", "legge solo il livello 7"], "", "buste"),
      C("nozioni", "192.168.1.25 è un indirizzo…", ["IP", "MAC", "di porta"], "", "indirizzi"),
      C("nozioni", "Se porto il portatile da scuola a casa, cambia…", ["l'indirizzo IP", "l'indirizzo MAC", "nessuno dei due"], "", "indirizzi"),
      C("nozioni", "L'access point del Wi-Fi lavora soprattutto al livello…", ["2 Collegamento", "7 Applicazione", "4 Trasporto"], "", "dispositivi"),
      C("nozioni", "L'hub…", ["ripete i bit a tutti, senza capire gli indirizzi", "sceglie la strada con l'IP", "blocca i virus"], "", "dispositivi"),
      C("nozioni", "Per scaricare un file senza perdere pezzi si usa…", ["TCP", "UDP", "un hub"], "", "trasporto"),
      C("nozioni", "La porta 443 serve a…", ["i siti web sicuri (HTTPS)", "l'e-mail", "il cavo di rete"], "", "trasporto"),
      C("nozioni", "Il PC ha l'IP 169.254.10.3. Che cosa vuol dire?", ["non ha ricevuto l'IP dalla rete: guardo il livello 3", "va tutto bene", "il monitor è rotto"], "", "tecnico"),
      C("nozioni", "L'IP 8.8.8.8 risponde ma il sito con il nome non si apre. Il problema è…", ["il DNS, che traduce il nome in IP", "il cavo", "la scheda video"], "", "tecnico")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti sicuro, adesso, sui 7 livelli ISO/OSI?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti piace il tuo progetto di stage?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "spiega", tema: "buste", q: "Spiega con parole tue l'incapsulamento. Usa l'esempio di un messaggio che mandi con WhatsApp a un amico.", aiuto: "Almeno 30 parole: chi mette le buste, chi le apre, perché.", min_parole: 30,
        criteri: "scendendo ogni livello aggiunge un'intestazione (busta); chi riceve le apre al contrario; l'esempio è usato" },
      { area: "spiega", tema: "tecnico", q: "Un cliente ti chiama: «Internet non va». Racconta, passo per passo, che cosa controlli e in che ordine. Di' il livello di ogni passo.", aiuto: "Almeno 30 parole. Pensa al metodo dal basso verso l'alto.", min_parole: 30,
        criteri: "ordine dal basso: fisico (cavo, lucine), collegamento (switch, Wi-Fi), rete (IP, 169.254, router), poi DNS e servizio" },
      { area: "progetto", tema: "readme", q: "LA DESCRIZIONE DEL TUO PROGETTO. Scrivila seguendo lo schema della scheda 9: nome del progetto, che cosa fa, per chi è, come si usa, con che cosa lo fai, la prima versione v0.1, le versioni dopo.", aiuto: "Almeno 80 parole, parole tue. Diventerà il README del tuo repository: scrivila come se la leggesse un'azienda.", min_parole: 80,
        criteri: "tutte le sezioni dello schema; v0.1 piccola e realizzabile; chiara per chi non sa niente; parole sue" },
      { area: "progetto", tema: "progetto", q: "Il tuo progetto usa la rete? Se sì, a quali livelli ISO/OSI lavora (per esempio: un gioco online usa UDP al livello 4)? Se no, come potrebbe usarla in una versione futura?", aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "collegamento sensato tra il proprio progetto e almeno un livello" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("nozioni", "Il livello più in basso è…", ["1 Fisico", "7 Applicazione", "3 Rete"], "", "livelli"),
      C("nozioni", "WhatsApp e il browser sono al livello…", ["7 Applicazione", "2 Collegamento", "1 Fisico"], "", "livelli"),
      C("nozioni", "Il router lavora al livello…", ["3 Rete", "1 Fisico", "7 Applicazione"], "", "dispositivi"),
      C("nozioni", "Lo switch usa l'indirizzo…", ["MAC", "IP", "e-mail"], "", "dispositivi"),
      C("nozioni", "L'indirizzo scritto in fabbrica nella scheda di rete è…", ["il MAC", "l'IP", "il DNS"], "", "indirizzi"),
      C("nozioni", "Al livello 3 il pezzo di dati si chiama…", ["pacchetto", "frame", "bit"], "", "buste"),
      C("nozioni", "UDP è…", ["veloce ma senza controllo", "lento ma sicuro", "un cavo"], "", "trasporto"),
      C("nozioni", "Quando la rete non va, si comincia a controllare…", ["dal livello 1, il cavo", "dal livello 7, il programma", "a caso"], "", "tecnico")
    ]
  };
})();
