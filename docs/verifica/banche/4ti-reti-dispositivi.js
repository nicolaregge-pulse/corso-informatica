// 4TI · Le reti e i loro dispositivi: switch, router, access point, firewall + il mio progetto (27/10/2026).
// Laboratorio professionale 10-13. Ripassa in una scheda la teoria ISO/OSI del 06/10 e del 20/10
// (classe-4/reti-iso-osi), poi va avanti: LAN, WAN e Internet, i protocolli, switch, router, access point,
// firewall, ipconfig senza diritti di amministratore, il programma dell'anno e la definizione del progetto.
// Aree e peso nel giudizio: nozioni sulle reti 50%, saperlo spiegare 25%, il mio progetto 25%. Solo italiano.
(function () {
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function T(righe) { return '<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0">' + righe.map(function (r, i) { return '<tr>' + r.map(function (c) { return (i ? '<td' : '<th') + ' style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">' + c + (i ? '</td>' : '</th>'); }).join('') + '</tr>'; }).join('') + '</table>'; }
  function K(t) { return '<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap">' + t.replace(/</g, '&lt;') + '</pre>'; }
  var IPCONFIG = "Scheda Ethernet Ethernet:\n\n   Indirizzo IPv4. . . . . . . . . : 192.168.10.37\n   Subnet mask . . . . . . . . . . : 255.255.255.0\n   Gateway predefinito . . . . . . : 192.168.10.1";
  var README = "# Nome del mio progetto\n\n## Che cosa fa\nDue o tre frasi: che cosa fa il mio programma, gioco o rete.\n\n## Per chi è\nChi lo usa: un'azienda, un giocatore, un tecnico, la mia classe.\n\n## Come si usa\nI passi di chi lo usa: apro, clicco, scrivo, vedo.\n\n## Con che cosa lo faccio\nGodot, Lazarus, Python, Packet Tracer, GitHub…\n\n## Che cosa c'entra la rete\nQuali dispositivi o protocolli usa (o potrebbe usare): switch, router, Wi-Fi, HTTP, DNS…\n\n## La prima versione (v0.1)\nLa cosa più piccola che funziona e che posso mostrare.\n\n## Le versioni dopo\nv0.2: …  v0.3: …\n\n## Chi sono\nNome (o soprannome), classe 4ª, indirizzo informatico.";

  window.BANCA = {
    id: "4ti-reti-dispositivi-v1",
    classe: "4TI",
    titolo: "Le reti e i loro dispositivi: switch, router, access point, firewall",
    sotto: "4TI · 27/10/2026 · LAN e Internet, i protocolli, i dispositivi della rete · poi il tuo progetto dell'anno",
    stato: "stato/4ti-reti-dispositivi.json",
    risultati: "risultati.html?b=4ti-reti-dispositivi",
    minuti: 30,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Nozioni sulle reti", peso: 50 },
      spiega: { nome: "Saperlo spiegare (solo parole tue)", peso: 25 },
      progetto: { nome: "Il mio progetto", peso: 25 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO + TEORIA NUOVA ---------- */
    ripasso_n: 1,
    schede_temi: { osi: 1, lan: 2, protocolli: 3, switch: 4, router: 5, wifi: 6, firewall: 7, ipconfig: 8, anno: 9, progetto: 10 },
    schede: [
      { titolo: "1. Ripasso: i 7 livelli in una pagina", testo:
        "Lo hai già studiato: un messaggio viaggia attraverso <b>sette livelli</b>, come un pacco in una ditta di spedizioni. Chi spedisce scende dal 7 all'1, chi riceve sale dall'1 al 7. Ogni livello mette una <b>busta</b> (incapsulamento)." +
        T([["N.", "Livello", "Parola chiave", "Chi ci lavora"],
           ["7", "Applicazione", "il programma", "browser, HTTP, DNS"],
           ["4", "Trasporto", "pezzi e porte", "TCP, UDP"],
           ["3", "Rete", "indirizzo IP", "router"],
           ["2", "Collegamento", "indirizzo MAC", "switch, access point"],
           ["1", "Fisico", "i bit", "cavo, onde del Wi-Fi"]]) +
        "Oggi usiamo questa tabella come una <b>mappa</b>: per ogni dispositivo nuovo ci chiediamo «a che livello lavora?»." },
      { titolo: "2. La rete di casa, la rete della scuola, Internet", testo:
        "Una <b>rete</b> è un gruppo di dispositivi collegati che si parlano. Ce ne sono di grandezze diverse, come le strade:" +
        T([["Nome", "Che cos'è", "Paragone"],
           ["LAN (rete locale)", "i dispositivi di una casa, di un'aula, di un ufficio", "le strade dentro il tuo quartiere"],
           ["WAN (rete geografica)", "collega reti lontane: città, sedi di un'azienda", "l'autostrada tra due città"],
           ["Internet", "la rete di tutte le reti del mondo", "tutte le strade del mondo insieme"]]) +
        "<b>A casa:</b> telefono, PC e TV sono una piccola LAN; il modem-router la collega a Internet.<br><b>A scuola:</b> i PC del laboratorio sono una LAN più grande, con molti switch e access point; un router la collega a Internet." },
      { titolo: "3. I protocolli: le lingue comuni", testo:
        "Un <b>protocollo</b> è un insieme di regole per parlarsi, come una lingua comune. Se due dispositivi usano lo stesso protocollo, si capiscono, anche se sono di marche diverse." +
        T([["Protocollo", "A che cosa serve", "Livello", "Nella vita reale"],
           ["IP", "dà un indirizzo e trova la strada", "3 Rete", "l'indirizzo sulla busta"],
           ["TCP", "consegna sicura, in ordine", "4 Trasporto", "la raccomandata con ricevuta"],
           ["UDP", "consegna veloce, senza controllo", "4 Trasporto", "il volantino nella cassetta"],
           ["HTTP / HTTPS", "apre le pagine web (HTTPS è cifrato, col lucchetto)", "7 Applicazione", "chiedere un libro in biblioteca"],
           ["DNS", "traduce il nome (google.it) in indirizzo IP", "7 Applicazione", "la rubrica del telefono"],
           ["DHCP", "dà in automatico l'IP a chi entra nella rete", "7 Applicazione", "la reception dell'hotel che ti dà la stanza"]]) },
      { titolo: "4. Lo switch (e il vecchio hub)", testo:
        "Lo <b>switch</b> è la «ciabatta» della rete: ha tante prese (porte) dove infili i cavi dei PC. Lavora al <b>livello 2</b> e guarda l'<b>indirizzo MAC</b>.<br><br>Lo switch impara chi è collegato a ogni porta e lo scrive nella sua <b>tabella degli indirizzi MAC</b>:" +
        T([["Porta", "Indirizzo MAC che ha visto"], ["1", "3C-52-82-1A-7F-09 (PC del prof)"], ["2", "A4-BB-6D-10-22-3E (PC 2)"], ["3", "F0-1F-AF-55-90-0C (stampante)"]]) +
        "Così manda ogni frame <b>solo</b> al PC giusto.<br><br>L'<b>hub</b> (livello 1) invece non capisce gli indirizzi: ripete tutto a tutti.<br><b>Paragone:</b> l'hub è chi grida in corridoio; lo switch è il postino che porta la lettera alla porta giusta." },
      { titolo: "5. Il router: la porta verso le altre reti", testo:
        "Il <b>router</b> lavora al <b>livello 3</b> e guarda l'<b>indirizzo IP</b>. Collega reti diverse e sceglie la strada, come un navigatore.<br><br>Il <b>gateway predefinito</b> è l'indirizzo del router della tua rete: è la «porta d'uscita». Quando il PC deve parlare con qualcuno fuori dalla LAN, manda il pacchetto lì." +
        T([["", "Switch", "Router"],
           ["Livello", "2 Collegamento", "3 Rete"],
           ["Guarda", "l'indirizzo MAC", "l'indirizzo IP"],
           ["Lavora", "dentro la stessa rete", "tra reti diverse"],
           ["Paragone", "il postino del condominio", "l'ufficio postale che smista tra città"]]) +
        "<b>NAT in parole semplici:</b> a casa tutti i dispositivi hanno un IP privato (192.168…). Verso Internet il router li fa uscire tutti con <b>un solo</b> IP pubblico, e poi ricorda a chi riportare le risposte. Come il centralino di un'azienda: un solo numero fuori, tanti interni dentro." },
      { titolo: "6. L'access point e il Wi-Fi", testo:
        "L'<b>access point</b> (punto di accesso) collega i dispositivi senza fili alla rete con il cavo. È come uno switch, ma via radio: lavora ai livelli <b>1 e 2</b>." +
        T([["Parola", "Che cosa vuol dire"],
           ["SSID", "il nome della rete Wi-Fi che vedi sul telefono"],
           ["Password WPA2 / WPA3", "la chiave che cifra il Wi-Fi; WPA3 è la più nuova e sicura"],
           ["2,4 GHz", "arriva più lontano e passa meglio i muri, ma è più lento"],
           ["5 GHz", "più veloce, ma arriva meno lontano"]]) +
        "<b>Access point o router di casa?</b> Il «router» di casa è in realtà <b>tante scatole in una</b>: router + switch + access point + modem (+ firewall). A scuola invece sono apparecchi separati: tanti access point sui soffitti, collegati a switch, e un router solo." },
      { titolo: "7. Il firewall: il buttafuori della rete", testo:
        "Il <b>firewall</b> controlla tutto quello che entra ed esce e decide chi passa, seguendo delle <b>regole</b>. È come il buttafuori di una discoteca con la lista." +
        T([["Regola (esempio)", "Che cosa succede"],
           ["porta 443 (HTTPS): aperta", "i siti web sicuri funzionano"],
           ["porta 80 (HTTP): aperta", "i siti web normali funzionano"],
           ["porte dei giochi online: chiuse", "a scuola il gioco non si collega"],
           ["siti di scommesse o violenti: bloccati", "il browser mostra «pagina bloccata»"]]) +
        "Una <b>porta</b> è come il numero dell'interno di un ufficio: dice a quale programma va il messaggio. <b>Aperta</b> = si può entrare; <b>chiusa</b> = non si passa.<br>La scuola usa un firewall per proteggere i PC dai virus e per bloccare certi siti: non è un dispetto, è sicurezza." },
      { titolo: "8. Leggere la configurazione del tuo PC: ipconfig", testo:
        "Ora guardi i numeri veri del tuo PC. <b>Non servono diritti di amministratore.</b><br>1. Premi il tasto <b>Windows</b> sulla tastiera.<br>2. Scrivi <b>cmd</b> e premi <b>Invio</b>: si apre una finestra nera (il Prompt dei comandi).<br>3. Scrivi <b>ipconfig</b> e premi <b>Invio</b>.<br>4. Cerca il blocco della tua scheda (Ethernet se hai il cavo, Wi-Fi se sei senza fili). Vedi qualcosa così:" + K(IPCONFIG) +
        T([["Riga", "Che cosa vuol dire"],
           ["Indirizzo IPv4", "il numero del tuo PC nella rete (l'indirizzo di casa)"],
           ["Subnet mask (maschera)", "dice quanto è grande il «quartiere»: chi è nella tua stessa rete"],
           ["Gateway predefinito", "l'indirizzo del router, la porta d'uscita"],
           ["Server DNS", "chi traduce i nomi in IP; lo vedi con <b>ipconfig /all</b>"]]) +
        "Se l'IP comincia con <b>169.254</b>, il PC non ha ricevuto l'indirizzo dal DHCP: guarda il cavo e chiedi all'assistente." },
      { titolo: "9. Che cosa faremo quest'anno", testo:
        "Questa è la strada del laboratorio di quest'anno. Sono competenze che chiedono davvero le aziende:" +
        T([["Tappa", "Che cosa fai", "Che cosa sai fare alla fine"],
           ["1. Cablaggio", "prepari un cavo di rete e lo provi", "collegare una postazione"],
           ["2. Packet Tracer", "costruisci una rete al computer, con PC, switch e router", "progettare una rete senza comprare niente"],
           ["3. Configurare", "dai gli indirizzi, configuri switch, router e access point", "far parlare due reti"],
           ["4. Sicurezza", "password Wi-Fi, regole del firewall, aggiornamenti", "proteggere una piccola rete"],
           ["5. Progetto", "il tuo progetto, che mostri alla classe e allo stage", "un lavoro da mettere nel curriculum"]]) +
        "Packet Tracer è un programma gratuito che simula la rete: puoi sbagliare quanto vuoi, non si rompe niente." },
      { titolo: "10. Il mio progetto: definirlo bene", testo:
        "Il 20/10 hai scritto la prima descrizione del tuo progetto. Oggi la <b>aggiorni</b> con quello che hai imparato sulle reti. In un'azienda vera la descrizione sta nel file <b>README.md</b>, la prima pagina del repository. Lo schema:" + K(README) +
        "Regola d'oro: la <b>prima versione (v0.1)</b> è la cosa più piccola che funziona. Meglio piccola e finita che grande e a metà.<br>Il nuovo punto «Che cosa c'entra la rete» ti aiuta a collegare il tuo progetto a quello che faremo quest'anno." }
    ],
    strumenti: [{ t: 'Il viaggio di un pacchetto (animazione)', u: '../4ti-iso-osi/viaggio.html', c: '#1f6feb' }, { t: 'I progetti della classe', u: '../4ti-progetti/', c: '#d4a017' }],
    via: C("nozioni", "Il dispositivo che collega la rete della scuola a Internet è…", ["il router", "il mouse", "il monitor"], "Il router collega reti diverse."),
    prepara: [
      { q: "Pensa al tuo progetto: in una frase, che cosa c'entra la rete (per esempio: è un gioco online, è una rete per un negozio, usa il Wi-Fi)?", min: 10 }
    ],
    allenamento: [
      S(1, C("nozioni", "Lo switch lavora al livello…", ["2 Collegamento", "7 Applicazione", "1 Fisico"], "Guarda l'indirizzo MAC.")),
      S(2, C("nozioni", "I PC di un'aula collegati tra loro formano una…", ["LAN (rete locale)", "WAN", "stampante"], "Rete piccola, in un solo posto.")),
      S(3, C("nozioni", "Il protocollo che traduce il nome di un sito in indirizzo IP è…", ["DNS", "UDP", "HTTP"], "Come la rubrica del telefono.")),
      S(3, C("nozioni", "Il protocollo che dà in automatico l'IP al tuo PC è…", ["DHCP", "DNS", "TCP"], "Come la reception dell'hotel.")),
      S(4, C("nozioni", "Lo switch manda il frame…", ["solo al PC giusto, grazie alla tabella dei MAC", "a tutti i PC", "a Internet"], "L'hub invece lo manda a tutti.")),
      S(5, C("nozioni", "Il gateway predefinito è…", ["l'indirizzo del router, la porta d'uscita della rete", "il nome del Wi-Fi", "la password del PC"], "Lì vanno i pacchetti diretti fuori dalla LAN.")),
      S(6, C("nozioni", "L'SSID è…", ["il nome della rete Wi-Fi", "la password del Wi-Fi", "un cavo"], "È il nome che vedi nella lista delle reti.")),
      S(7, C("nozioni", "Il firewall assomiglia a…", ["un buttafuori con la lista", "un postino", "una rubrica"], "Decide chi passa, con delle regole.")),
      S(8, C("nozioni", "Per vedere il tuo indirizzo IP scrivi nel Prompt dei comandi…", ["ipconfig", "format", "shutdown"], "Non servono diritti di amministratore.")),
      S(9, C("nozioni", "Packet Tracer serve a…", ["costruire una rete al computer, senza rompere niente", "giocare online", "scrivere documenti"], "È un simulatore di reti.")),
      S(10, C("progetto", "La prima versione (v0.1) del progetto deve essere…", ["la cosa più piccola che funziona", "il progetto finito", "solo un'idea scritta"], "Piccola e finita."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("nozioni", "Il router lavora al livello…", ["3 Rete", "2 Collegamento", "7 Applicazione"], "Il router guarda l'indirizzo IP: livello 3.", "osi"),
      C("nozioni", "La rete di tutte le reti del mondo si chiama…", ["Internet", "LAN", "switch"], "Internet unisce tutte le reti.", "lan"),
      C("nozioni", "Una rete che collega le sedi di un'azienda in due città diverse è una…", ["WAN (rete geografica)", "LAN (rete locale)", "rete Bluetooth"], "WAN = rete grande, tra posti lontani.", "lan"),
      C("nozioni", "Un protocollo è…", ["un insieme di regole per parlarsi, come una lingua comune", "un tipo di cavo", "un programma antivirus"], "Se due dispositivi usano lo stesso protocollo si capiscono.", "protocolli"),
      C("nozioni", "HTTPS è il protocollo per…", ["aprire le pagine web in modo cifrato (col lucchetto)", "dare l'IP ai PC", "stampare"], "Livello 7, la S vuol dire sicuro.", "protocolli"),
      C("nozioni", "Scrivi google.it nel browser. Chi lo trasforma in un indirizzo IP?", ["il DNS", "il DHCP", "lo switch"], "Il DNS è la rubrica della rete.", "protocolli"),
      C("nozioni", "La differenza tra switch e hub è che lo switch…", ["manda i dati solo al PC giusto", "è più colorato", "funziona senza corrente"], "L'hub ripete tutto a tutti.", "switch"),
      C("nozioni", "Nella sua tabella lo switch scrive…", ["quale indirizzo MAC c'è su ogni porta", "le password degli utenti", "i siti visitati"], "Così sa dove mandare ogni frame.", "switch"),
      C("nozioni", "Il router di casa usa il NAT per…", ["far uscire tutti i dispositivi con un solo IP pubblico", "cambiare il nome del Wi-Fi", "rendere più veloce il cavo"], "Come il centralino: un numero fuori, tanti interni dentro.", "router"),
      C("nozioni", "Il PC vuole aprire un sito fuori dalla scuola. A chi manda il pacchetto per primo?", ["al gateway predefinito (il router)", "alla stampante", "all'hub"], "Il gateway è la porta d'uscita della LAN.", "router"),
      C("nozioni", "Vuoi più velocità e sei vicino all'access point. Scegli il Wi-Fi a…", ["5 GHz", "2,4 GHz", "non cambia niente"], "5 GHz è più veloce ma arriva meno lontano.", "wifi"),
      C("nozioni", "La password più sicura per il Wi-Fi oggi usa…", ["WPA3", "nessuna password", "il nome della rete"], "WPA3 è la protezione più nuova.", "wifi"),
      C("nozioni", "A scuola il gioco online non si collega, ma i siti web sì. Probabilmente…", ["il firewall tiene chiuse le porte del gioco", "il cavo è rotto", "il monitor è spento"], "Le porte 80 e 443 sono aperte, quelle del gioco no.", "firewall"),
      C("nozioni", "Nel risultato di ipconfig, la riga «Gateway predefinito» ti dice…", ["l'indirizzo del router della tua rete", "il nome del tuo PC", "la velocità del cavo"], "È la porta d'uscita verso le altre reti.", "ipconfig"),
      C("nozioni", "ipconfig dice che il tuo IP è 169.254.8.20. Vuol dire che…", ["il PC non ha ricevuto l'IP dal DHCP", "va tutto benissimo", "sei collegato al 5 GHz"], "Controlla il cavo e il livello 3.", "ipconfig")
    ],
    scale: [
      { area: "parere", q: "Quanto ti senti sicuro, adesso, su switch, router, access point e firewall?", basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: "Quanto ti interessa il programma di quest'anno (cavi, Packet Tracer, configurare la rete)?", basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "spiega", tema: "router", q: "Spiega con parole tue la differenza tra uno switch e un router. Usa un esempio: la rete del laboratorio della scuola.", aiuto: "Almeno 30 parole: a che livello lavora ognuno, che indirizzo guarda, dove lavora (dentro la rete o tra reti).", min_parole: 30,
        criteri: "switch livello 2, indirizzo MAC, dentro la stessa LAN; router livello 3, indirizzo IP, collega reti diverse (gateway verso Internet); esempio del laboratorio usato; parole sue" },
      { area: "spiega", tema: "firewall", q: "A che cosa serve un firewall? Spiegalo a un amico che non sa niente di computer, con un esempio della scuola.", aiuto: "Almeno 30 parole. Pensa al buttafuori, alle regole e alle porte aperte o chiuse.", min_parole: 30,
        criteri: "controlla cosa entra ed esce; decide con regole; porte aperte e chiuse o siti bloccati; scopo di protezione; esempio concreto; parole sue" },
      { area: "spiega", tema: "wifi", q: "Il router di casa e gli access point della scuola: che differenza c'è? Perché a scuola sono apparecchi separati?", aiuto: "Almeno 20 parole.", min_parole: 20,
        criteri: "il router di casa contiene più apparecchi (router, switch, access point, modem); a scuola servono tanti access point per coprire tutto l'edificio e un solo router; access point ai livelli 1-2" },
      { area: "progetto", tema: "progetto", q: "IL TUO PROGETTO, VERSIONE AGGIORNATA. Riscrivi la descrizione seguendo lo schema della scheda 10: nome, che cosa fa, per chi è, come si usa, con che cosa lo fai, che cosa c'entra la rete, la prima versione v0.1, le versioni dopo.", aiuto: "Almeno 80 parole, parole tue. Diventerà il README del tuo repository: scrivila come se la leggesse un'azienda.", min_parole: 80,
        criteri: "tutte le sezioni dello schema, compresa «Che cosa c'entra la rete» con almeno un dispositivo o protocollo nominato in modo corretto; v0.1 piccola e realizzabile; chiara per chi non sa niente; parole sue" },
      { area: "parere", tema: "retro", q: "Che cosa ti è servito di più oggi, e che cosa cambieresti?", aiuto: "Anche poche parole, ma sincere.", min_parole: 5 }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("nozioni", "Lo switch guarda l'indirizzo…", ["MAC", "IP", "e-mail"], "Livello 2.", "switch"),
      C("nozioni", "Il router guarda l'indirizzo…", ["IP", "MAC", "del sito"], "Livello 3.", "router"),
      C("nozioni", "La rete di un'aula si chiama…", ["LAN", "WAN", "Internet"], "Rete locale.", "lan"),
      C("nozioni", "Il DNS serve a…", ["tradurre i nomi dei siti in indirizzi IP", "dare la corrente ai PC", "bloccare i virus"], "È la rubrica della rete.", "protocolli"),
      C("nozioni", "Il nome della rete Wi-Fi si chiama…", ["SSID", "IP", "porta"], "Lo vedi nella lista delle reti.", "wifi"),
      C("nozioni", "Il firewall…", ["decide chi passa con delle regole", "ripete i dati a tutti", "stampa i documenti"], "Il buttafuori della rete.", "firewall"),
      C("nozioni", "Il comando per vedere il tuo IP è…", ["ipconfig", "print", "save"], "Lo scrivi nel Prompt dei comandi.", "ipconfig"),
      C("nozioni", "L'hub…", ["ripete i bit a tutti, senza capire gli indirizzi", "sceglie la strada con l'IP", "è un firewall"], "Livello 1.", "switch")
    ]
  };
})();
