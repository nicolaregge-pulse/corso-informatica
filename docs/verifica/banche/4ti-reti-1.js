// Generato da classe-4/reti-dispositivi/_build/parti.js (27/10/2026): parte 1 di 4 della lezione 4ti-reti-dispositivi.
window.BANCA = {
 "id": "4ti-reti-1-v1",
 "classe": "4TI",
 "titolo": "Le reti, parte 1 di 4: i livelli, le reti, i protocolli",
 "sotto": "4TI · 27/10/2026 · leggi le schede, fai il ripasso, poi il quiz su Moduli in fondo all'ultima scheda",
 "stato": "stato/4ti-reti-1.json",
 "risultati": "risultati.html?b=4ti-reti-1",
 "minuti": 10,
 "anteprima": "868848605",
 "aree": {
  "nozioni": {
   "nome": "Nozioni sulle reti",
   "peso": 50
  },
  "spiega": {
   "nome": "Saperlo spiegare (solo parole tue)",
   "peso": 25
  },
  "progetto": {
   "nome": "Il mio progetto",
   "peso": 25
  },
  "parere": {
   "nome": "Il tuo parere (non conta per il voto)",
   "peso": 0
  }
 },
 "ripasso_n": 0,
 "schede_temi": {
  "osi": 1,
  "lan": 2,
  "protocolli": 3
 },
 "schede": [
  {
   "titolo": "1. Ripasso: i 7 livelli in una pagina",
   "testo": "Lo hai già studiato: un messaggio viaggia attraverso <b>sette livelli</b>, come un pacco in una ditta di spedizioni. Chi spedisce scende dal 7 all'1, chi riceve sale dall'1 al 7. Ogni livello mette una <b>busta</b> (incapsulamento).<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">N.</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Livello</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Parola chiave</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Chi ci lavora</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">7</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Applicazione</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">il programma</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">browser, HTTP, DNS</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">4</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Trasporto</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">pezzi e porte</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">TCP, UDP</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Rete</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">indirizzo IP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">router</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">2</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Collegamento</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">indirizzo MAC</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">switch, access point</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Fisico</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">i bit</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">cavo, onde del Wi-Fi</td></tr></table>Oggi usiamo questa tabella come una <b>mappa</b>: per ogni dispositivo nuovo ci chiediamo «a che livello lavora?»."
  },
  {
   "titolo": "2. La rete di casa, la rete della scuola, Internet",
   "testo": "Una <b>rete</b> è un gruppo di dispositivi collegati che si parlano. Ce ne sono di grandezze diverse, come le strade:<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Nome</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Che cos'è</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Paragone</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">LAN (rete locale)</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">i dispositivi di una casa, di un'aula, di un ufficio</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">le strade dentro il tuo quartiere</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">WAN (rete geografica)</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">collega reti lontane: città, sedi di un'azienda</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'autostrada tra due città</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Internet</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">la rete di tutte le reti del mondo</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">tutte le strade del mondo insieme</td></tr></table><b>A casa:</b> telefono, PC e TV sono una piccola LAN; il modem-router la collega a Internet.<br><b>A scuola:</b> i PC del laboratorio sono una LAN più grande, con molti switch e access point; un router la collega a Internet."
  },
  {
   "titolo": "3. I protocolli: le lingue comuni",
   "testo": "Un <b>protocollo</b> è un insieme di regole per parlarsi, come una lingua comune. Se due dispositivi usano lo stesso protocollo, si capiscono, anche se sono di marche diverse.<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Protocollo</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">A che cosa serve</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Livello</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Nella vita reale</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">IP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">dà un indirizzo e trova la strada</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3 Rete</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'indirizzo sulla busta</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">TCP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">consegna sicura, in ordine</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">4 Trasporto</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">la raccomandata con ricevuta</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">UDP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">consegna veloce, senza controllo</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">4 Trasporto</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">il volantino nella cassetta</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">HTTP / HTTPS</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">apre le pagine web (HTTPS è cifrato, col lucchetto)</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">7 Applicazione</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">chiedere un libro in biblioteca</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">DNS</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">traduce il nome (google.it) in indirizzo IP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">7 Applicazione</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">la rubrica del telefono</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">DHCP</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">dà in automatico l'IP a chi entra nella rete</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">7 Applicazione</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">la reception dell'hotel che ti dà la stanza</td></tr></table><div style=\"margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px\"><p style=\"margin:0 0 8px\"><b>FINE DELLA PARTE 1.</b> Adesso il quiz: domande su quello che hai appena letto. Rispondi da solo, senza AI.</p><a href=\"https://docs.google.com/forms/d/e/1FAIpQLSddSJQHApVPK0GFPBTapANXVqGEgY3kIDzrudrvVncHxon4xw/viewform\" target=\"_blank\" rel=\"noopener\" style=\"display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px\">Fai il QUIZ della parte 1</a><p style=\"margin:10px 0 0\">Poi aspetta il via del prof per la parte 2.</p></div>"
  }
 ],
 "strumenti": [
  {
   "t": "Il viaggio di un pacchetto (animazione)",
   "u": "../4ti-iso-osi/viaggio.html",
   "c": "#1f6feb"
  },
  {
   "t": "I progetti della classe",
   "u": "../4ti-progetti/",
   "c": "#d4a017"
  }
 ],
 "via": {
  "tipo": "c",
  "area": "nozioni",
  "tema": "",
  "q": "Il dispositivo che collega la rete della scuola a Internet è…",
  "o": [
   "il router",
   "il mouse",
   "il monitor"
  ],
  "a": 0,
  "spiega": "Il router collega reti diverse."
 },
 "allenamento": [
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "Lo switch lavora al livello…",
   "o": [
    "2 Collegamento",
    "7 Applicazione",
    "1 Fisico"
   ],
   "a": 0,
   "spiega": "Guarda l'indirizzo MAC.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "I PC di un'aula collegati tra loro formano una…",
   "o": [
    "LAN (rete locale)",
    "WAN",
    "stampante"
   ],
   "a": 0,
   "spiega": "Rete piccola, in un solo posto.",
   "scheda": 2
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "Il protocollo che traduce il nome di un sito in indirizzo IP è…",
   "o": [
    "DNS",
    "UDP",
    "HTTP"
   ],
   "a": 0,
   "spiega": "Come la rubrica del telefono.",
   "scheda": 3
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "Il protocollo che dà in automatico l'IP al tuo PC è…",
   "o": [
    "DHCP",
    "DNS",
    "TCP"
   ],
   "a": 0,
   "spiega": "Come la reception dell'hotel.",
   "scheda": 3
  }
 ],
 "crocette": [
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "osi",
   "q": "Il router lavora al livello…",
   "o": [
    "3 Rete",
    "2 Collegamento",
    "7 Applicazione"
   ],
   "a": 0,
   "spiega": "Il router guarda l'indirizzo IP: livello 3."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "lan",
   "q": "La rete di tutte le reti del mondo si chiama…",
   "o": [
    "Internet",
    "LAN",
    "switch"
   ],
   "a": 0,
   "spiega": "Internet unisce tutte le reti."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "lan",
   "q": "Una rete che collega le sedi di un'azienda in due città diverse è una…",
   "o": [
    "WAN (rete geografica)",
    "LAN (rete locale)",
    "rete Bluetooth"
   ],
   "a": 0,
   "spiega": "WAN = rete grande, tra posti lontani."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "protocolli",
   "q": "Un protocollo è…",
   "o": [
    "un insieme di regole per parlarsi, come una lingua comune",
    "un tipo di cavo",
    "un programma antivirus"
   ],
   "a": 0,
   "spiega": "Se due dispositivi usano lo stesso protocollo si capiscono."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "protocolli",
   "q": "HTTPS è il protocollo per…",
   "o": [
    "aprire le pagine web in modo cifrato (col lucchetto)",
    "dare l'IP ai PC",
    "stampare"
   ],
   "a": 0,
   "spiega": "Livello 7, la S vuol dire sicuro."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "protocolli",
   "q": "Scrivi google.it nel browser. Chi lo trasforma in un indirizzo IP?",
   "o": [
    "il DNS",
    "il DHCP",
    "lo switch"
   ],
   "a": 0,
   "spiega": "Il DNS è la rubrica della rete."
  }
 ],
 "scale": [
  {
   "area": "parere",
   "q": "Quanto ti senti sicuro, adesso, su switch, router, access point e firewall?",
   "basso": "per niente",
   "alto": "moltissimo"
  },
  {
   "area": "parere",
   "q": "Quanto ti interessa il programma di quest'anno (cavi, Packet Tracer, configurare la rete)?",
   "basso": "per niente",
   "alto": "moltissimo",
   "ultima": true
  }
 ],
 "aperte": [],
 "recupero": [
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "lan",
   "q": "La rete di un'aula si chiama…",
   "o": [
    "LAN",
    "WAN",
    "Internet"
   ],
   "a": 0,
   "spiega": "Rete locale."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "protocolli",
   "q": "Il DNS serve a…",
   "o": [
    "tradurre i nomi dei siti in indirizzi IP",
    "dare la corrente ai PC",
    "bloccare i virus"
   ],
   "a": 0,
   "spiega": "È la rubrica della rete."
  }
 ]
};
