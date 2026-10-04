// Classe 4 — Il modello ISO/OSI (quiz personale: domande e ordine diversi per ognuno)
var LIV = ["1 Fisico", "2 Collegamento dati", "3 Rete", "4 Trasporto", "5 Sessione", "6 Presentazione", "7 Applicazione"];
function quale(testo, giusto) { return { q: "A quale livello ISO/OSI appartiene: <b>" + testo + "</b>?", o: LIV, a: giusto - 1, fisse: true }; }
window.BANCA = {
  titolo: "Il modello ISO/OSI",
  sotto: "Classe 4 · Reti · ognuno ha le sue domande · ripassa con la pagina <a href='../4ti-iso-osi/'>Il viaggio di un pacchetto</a>",
  regola: "Dall'alto in basso: <b>7 Applicazione · 6 Presentazione · 5 Sessione · 4 Trasporto · 3 Rete · 2 Collegamento dati · 1 Fisico</b>. "
        + "Chi spedisce <b>aggiunge</b> le buste scendendo (incapsulamento), chi riceve le <b>toglie</b> salendo.",
  quante: 12,
  domande: [
    quale("il cavo di rete e il segnale Wi-Fi", 1),
    quale("lo switch", 2),
    quale("l'indirizzo MAC", 2),
    quale("il router", 3),
    quale("l'indirizzo IP", 3),
    quale("il comando ping (protocollo ICMP)", 3),
    quale("TCP e UDP", 4),
    quale("le porte (es. 80 per il web, 443 per HTTPS)", 4),
    quale("aprire e chiudere la 'conversazione' tra due computer", 5),
    quale("la cifratura dei dati e i formati (JPEG, ASCII)", 6),
    quale("HTTP, DNS, SMTP (posta)", 7),
    quale("il browser e il programma di posta che usi", 7),
    { q: "Quanti livelli ha il modello ISO/OSI?", o: ["7", "4", "5", "8"], a: 0 },
    { q: "Che cos'è l'<b>incapsulamento</b>?", o: ["Scendendo nei livelli, ogni livello aggiunge la sua intestazione (una 'busta') ai dati",
        "Il router cancella i pacchetti sbagliati", "Il cavo protegge i bit dai disturbi", "Il messaggio viene compresso in un file .zip"], a: 0 },
    { q: "Chi riceve il messaggio, in che ordine toglie le buste?", o: ["Dal livello 1 verso il livello 7 (salendo)", "Dal livello 7 verso il livello 1 (scendendo)", "In ordine casuale", "Non toglie niente"], a: 0 },
    { q: "Differenza tra <b>TCP</b> e <b>UDP</b>?", o: ["TCP controlla che arrivino tutti i pezzi in ordine; UDP è più veloce ma non controlla",
        "TCP è per il Wi-Fi, UDP per il cavo", "UDP è più sicuro di TCP", "Sono la stessa cosa"], a: 0 },
    { q: "Lo <b>switch</b> consegna i dati al PC giusto usando…", o: ["l'indirizzo MAC", "l'indirizzo IP", "il nome del sito", "la porta 80"], a: 0 },
    { q: "Il <b>router</b> sceglie la strada tra reti diverse usando…", o: ["l'indirizzo IP", "l'indirizzo MAC", "il colore del cavo", "la password del Wi-Fi"], a: 0 },
    { q: "Il modello <b>TCP/IP</b> (quello usato da Internet) quanti livelli ha?", o: ["4", "7", "2", "10"], a: 0 },
    { q: "Al livello Trasporto il pezzo di dati si chiama…", o: ["segmento", "frame (trama)", "bit", "pacchetto IP"], a: 0 },
    { q: "Al livello Collegamento dati il pezzo di dati si chiama…", o: ["frame (trama)", "segmento", "messaggio", "porta"], a: 0 },
    { q: "Scrivi <b>https://</b> e compare il lucchetto: i dati sono cifrati. A quale livello avviene la cifratura (nel modello OSI)?", o: ["6 Presentazione", "1 Fisico", "3 Rete", "2 Collegamento dati"], a: 0 },
    { q: "Il PC non vede la rete e la lucina della scheda di rete è spenta. Da quale livello parti a cercare il guasto?", o: ["1 Fisico: controllo il cavo", "7 Applicazione: reinstallo il browser", "6 Presentazione", "5 Sessione"], a: 0 },
    { q: "Il <b>DNS</b> a cosa serve?", o: ["Traduce un nome (es. google.it) in un indirizzo IP", "Dà la corrente al router", "Cifra la password del Wi-Fi", "Collega i cavi tra loro"], a: 0 }
  ]
};
