// 2INF · Reti: IP, MAC, gateway, DNS, DHCP (02/11/2026).
// Generata da classe-2/phishing-0211/_build/gen_banche.py. Solo italiano (2INF). Marchi e domini inventati (.example).
window.BANCA = {
 "id": "2inf-reti-ip-v1",
 "classe": "2INF",
 "titolo": "Come parla il mio PC in rete: IP, MAC, gateway, DNS",
 "sotto": "2INF · 02/11/2026 · prima le 6 schede, poi il ripasso, poi il quiz di chiusura",
 "stato": "stato/2inf-reti-ip.json",
 "risultati": "risultati.html?b=2inf-reti-ip",
 "minuti": 15,
 "anteprima": "1166576373",
 "aree": {
  "rete": {
   "nome": "Come parla il PC in rete",
   "peso": 80
  },
  "mia": {
   "nome": "Con parole tue",
   "peso": 20
  },
  "parere": {
   "nome": "Il tuo parere (non conta per il voto)",
   "peso": 0
  }
 },
 "schede_temi": {
  "rete": 1,
  "ip": 2,
  "mac": 3,
  "gateway": 4,
  "dns": 5,
  "dhcp": 6
 },
 "schede": [
  {
   "titolo": "1. Che cos'è una rete",
   "testo": "Una <b>rete</b> è un gruppo di dispositivi collegati per parlarsi: PC, telefoni, stampanti.<br>Si collegano con un <b>cavo</b> o con il <b>Wi-Fi</b> (la rete senza fili).<br><br>Una rete piccola, come quella del laboratorio o di casa tua, si chiama <b>LAN</b> (in inglese «Local Area Network», cioè rete locale).<br><br><b>Per parlarsi, ogni dispositivo ha bisogno di un nome che gli altri capiscono: un indirizzo.</b>"
  },
  {
   "titolo": "2. L'indirizzo IP: l'indirizzo di casa del PC",
   "testo": "L'<b>indirizzo IP</b> è l'indirizzo di casa del tuo PC nella rete. Per esempio: <b>192.168.1.25</b>.<br><br>Sono <b>quattro numeri</b> separati da punti. Ogni numero va da 0 a 255.<br>Due PC nella stessa rete <b>non possono avere lo stesso IP</b>, come due case non possono avere lo stesso numero civico nella stessa via.<br><br>L'IP può <b>cambiare</b>: se porti il telefono da casa a scuola, ha un IP diverso."
  },
  {
   "titolo": "3. L'indirizzo MAC: il numero di serie della scheda di rete",
   "testo": "Il <b>MAC</b> è il numero di serie della <b>scheda di rete</b> (la parte del PC che si collega alla rete). Per esempio: <b>5C-BA-EF-12-34-56</b>.<br><br>Sono <b>sei coppie</b> di numeri e lettere. Lo scrive la fabbrica e <b>non cambia</b>.<br><br><b>IP = indirizzo di casa (può cambiare). MAC = numero di serie (resta sempre quello).</b>"
  },
  {
   "titolo": "4. Il gateway: la porta di casa verso Internet",
   "testo": "Il <b>gateway</b> (in italiano «porta d'uscita») è la <b>porta della rete verso Internet</b>. Di solito è il <b>router</b>, quella scatola con le lucine. Il suo indirizzo è spesso come <b>192.168.1.1</b>.<br><br>Quando il tuo PC vuole parlare con qualcuno <b>fuori dalla rete</b> (un sito, per esempio), manda tutto al gateway, e il gateway lo porta fuori.<br><br>Senza gateway puoi parlare con i PC vicini, ma <b>non vai su Internet</b>."
  },
  {
   "titolo": "5. Il DNS: la rubrica di Internet",
   "testo": "Per i computer un sito è un numero (un IP), ma per noi è più facile ricordare un nome, come <b>example.org</b>.<br><br>Il <b>DNS</b> è la <b>rubrica</b> che traduce il nome in numero: il tuo PC chiede «qual è il numero di questo nome?» e il DNS risponde.<br><br>Se il DNS non funziona, i siti non si aprono con il nome, anche se la rete c'è."
  },
  {
   "titolo": "6. Il DHCP: chi distribuisce gli indirizzi",
   "testo": "Chi dà un indirizzo IP al tuo PC? Di solito <b>lo fa il router da solo</b>, con un servizio che si chiama <b>DHCP</b>.<br><br>Appena ti colleghi, il DHCP ti dà in un attimo: l'<b>IP</b>, il <b>gateway</b> e il <b>DNS</b>. Come il portiere di un albergo che ti consegna la chiave e ti dice dov'è l'uscita.<br><br>Per questo di solito non devi scrivere niente a mano: è tutto <b>automatico</b>."
  }
 ],
 "strumenti": [
  {
   "t": "Il mio andamento di oggi",
   "u": "../anteprima/2inf-reti-02-11/cruscotto-ragazzi.html",
   "c": "#b45309"
  },
  {
   "t": "Torna alla pagina di oggi",
   "u": "../anteprima/2inf-reti-02-11/",
   "c": "#0b6e99"
  }
 ],
 "via": {
  "tipo": "c",
  "area": "rete",
  "tema": "rete",
  "q": "Quale di questi si può collegare a una rete?",
  "o": [
   "un telefono, un PC e una stampante",
   "solo i PC",
   "solo i telefoni"
  ],
  "a": 0,
  "spiega": "Anche telefoni e stampanti."
 },
 "prepara": [
  {
   "q": "Prova a dire con parole tue: a cosa serve l'indirizzo IP? Scrivi una frase.",
   "aiuto": "Pensa all'indirizzo di casa."
  },
  {
   "q": "Che cosa è più facile ricordare: un nome come example.org o un numero? Perché serve il DNS?",
   "aiuto": "Pensa alla rubrica del telefono."
  }
 ],
 "allenamento": [
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "LAN vuol dire…",
   "o": [
    "rete locale (piccola, come quella del laboratorio)",
    "il nome di un sito",
    "un tipo di cavo elettrico"
   ],
   "a": 0,
   "spiega": "Local Area Network: rete locale.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Quale di questi si può collegare a una rete?",
   "o": [
    "un telefono, un PC e una stampante",
    "solo i PC",
    "solo i telefoni"
   ],
   "a": 0,
   "spiega": "Anche telefoni e stampanti.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Un indirizzo IP come 192.168.1.25 è fatto da…",
   "o": [
    "quattro numeri separati da punti",
    "sei coppie di lettere e numeri",
    "una sola parola"
   ],
   "a": 0,
   "spiega": "Quattro numeri con i punti.",
   "scheda": 2
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Due PC nella stessa rete possono avere lo stesso IP?",
   "o": [
    "no, ognuno ha il suo",
    "sì, sempre",
    "solo se sono dello stesso colore"
   ],
   "a": 0,
   "spiega": "Come due case con lo stesso numero civico: non va.",
   "scheda": 2
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Il MAC è…",
   "o": [
    "il numero di serie della scheda di rete",
    "l'indirizzo di casa del PC",
    "il nome del router"
   ],
   "a": 0,
   "spiega": "Numero di serie: lo scrive la fabbrica.",
   "scheda": 3
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Quale tra IP e MAC può cambiare quando cambi rete?",
   "o": [
    "l'IP",
    "il MAC",
    "tutti e due non cambiano mai"
   ],
   "a": 0,
   "spiega": "L'IP cambia, il MAC resta.",
   "scheda": 3
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Il gateway serve per…",
   "o": [
    "uscire dalla rete e andare su Internet",
    "stampare",
    "dare l'IP ai telefoni"
   ],
   "a": 0,
   "spiega": "È la porta verso Internet.",
   "scheda": 4
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Il DNS fa…",
   "o": [
    "da rubrica: traduce un nome in un numero",
    "da stampante",
    "da antivirus"
   ],
   "a": 0,
   "spiega": "Nome → numero.",
   "scheda": 5
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "",
   "q": "Il DHCP serve a…",
   "o": [
    "dare in automatico l'IP, il gateway e il DNS",
    "spegnere il router",
    "scaricare i giochi"
   ],
   "a": 0,
   "spiega": "Distribuisce gli indirizzi da solo.",
   "scheda": 6
  }
 ],
 "crocette": [
  {
   "tipo": "c",
   "area": "rete",
   "tema": "rete",
   "q": "Una rete piccola, come quella di casa o del laboratorio, si chiama…",
   "o": [
    "LAN",
    "WAN",
    "USB",
    "HDMI"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "ip",
   "q": "Il tuo PC ha l'indirizzo 192.168.1.25. Questo numero è…",
   "o": [
    "un indirizzo IP",
    "un indirizzo MAC",
    "un numero di telefono",
    "il nome di un sito"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "ip",
   "q": "Quale di questi può essere un indirizzo IP?",
   "o": [
    "192.168.1.40",
    "5C-BA-EF-12-34-56",
    "www.example.org",
    "192.168"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "ip",
   "q": "Perché due PC non possono avere lo stesso IP nella stessa rete?",
   "o": [
    "perché la rete non saprebbe a quale dei due mandare i messaggi",
    "perché si rompono",
    "perché si spegne il router",
    "non è vero: possono"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "mac",
   "q": "Il numero 5C-BA-EF-12-34-56 è…",
   "o": [
    "un indirizzo MAC",
    "un indirizzo IP",
    "un gateway",
    "un DNS"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "mac",
   "q": "Il MAC lo decide…",
   "o": [
    "la fabbrica che ha costruito la scheda di rete",
    "il router ogni volta",
    "il professore",
    "il sito che visiti"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "mac",
   "q": "Quale frase è giusta?",
   "o": [
    "l'IP può cambiare, il MAC di solito resta quello",
    "il MAC cambia ogni giorno",
    "l'IP e il MAC sono la stessa cosa",
    "l'IP non cambia mai"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "gateway",
   "q": "Il gateway di una rete di casa è di solito…",
   "o": [
    "il router",
    "la stampante",
    "il monitor",
    "la tastiera"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "gateway",
   "q": "Se il gateway non funziona, che cosa succede?",
   "o": [
    "puoi parlare con i PC vicini ma non vai su Internet",
    "il PC si spegne",
    "non puoi più scrivere",
    "si cancellano i file"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "dns",
   "q": "Scrivi «example.org» e il sito si apre. Chi ha tradotto il nome in numero?",
   "o": [
    "il DNS",
    "il DHCP",
    "il MAC",
    "la stampante"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "dns",
   "q": "Hai la rete ma nessun sito si apre con il nome. Quale servizio sospetti?",
   "o": [
    "il DNS",
    "il MAC",
    "la tastiera",
    "lo schermo"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "dhcp",
   "q": "Chi dà l'IP al PC in automatico quando ti colleghi?",
   "o": [
    "il DHCP",
    "il DNS",
    "il MAC",
    "il monitor"
   ],
   "a": 0,
   "spiega": ""
  }
 ],
 "dati": [
  {
   "tipo": "n",
   "area": "rete",
   "tema": "ip",
   "q": "Da quanti numeri è fatto un indirizzo IP come 192.168.1.25? Scrivi solo il numero.",
   "giusto": 4,
   "spiega": "Quattro numeri con i punti."
  },
  {
   "tipo": "n",
   "area": "rete",
   "tema": "mac",
   "q": "Quante coppie di numeri e lettere ha un indirizzo MAC come 5C-BA-EF-12-34-56? Scrivi solo il numero.",
   "giusto": 6,
   "spiega": "Sei coppie."
  }
 ],
 "scale": [
  {
   "area": "parere",
   "q": "Quanto ti senti sicuro a leggere l'IP del tuo PC da solo?",
   "basso": "per niente",
   "alto": "moltissimo",
   "ultima": true
  }
 ],
 "aperte": [
  {
   "area": "mia",
   "tema": "gateway",
   "q": "A COSA SERVE IL GATEWAY. Spiega con parole tue, come a un compagno, a cosa serve il gateway. Puoi fare un esempio con la porta di casa.",
   "criteri": "porta verso Internet, router, senza gateway niente Internet"
  },
  {
   "area": "mia",
   "tema": "dns",
   "q": "A COSA SERVE IL DNS. Spiega con parole tue che cosa fa il DNS e che cosa succede se non funziona.",
   "criteri": "traduce i nomi in numeri (rubrica); senza DNS i siti non si aprono con il nome"
  }
 ],
 "recupero": [
  {
   "tipo": "c",
   "area": "rete",
   "tema": "rete",
   "q": "LAN vuol dire…",
   "o": [
    "rete locale (piccola, come quella del laboratorio)",
    "il nome di un sito",
    "un tipo di cavo elettrico"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "rete",
   "q": "Quale di questi si può collegare a una rete?",
   "o": [
    "un telefono, un PC e una stampante",
    "solo i PC",
    "solo i telefoni"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "ip",
   "q": "Un indirizzo IP come 192.168.1.25 è fatto da…",
   "o": [
    "quattro numeri separati da punti",
    "sei coppie di lettere e numeri",
    "una sola parola"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "ip",
   "q": "Due PC nella stessa rete possono avere lo stesso IP?",
   "o": [
    "no, ognuno ha il suo",
    "sì, sempre",
    "solo se sono dello stesso colore"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "mac",
   "q": "Il MAC è…",
   "o": [
    "il numero di serie della scheda di rete",
    "l'indirizzo di casa del PC",
    "il nome del router"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "mac",
   "q": "Quale tra IP e MAC può cambiare quando cambi rete?",
   "o": [
    "l'IP",
    "il MAC",
    "tutti e due non cambiano mai"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "gateway",
   "q": "Il gateway serve per…",
   "o": [
    "uscire dalla rete e andare su Internet",
    "stampare",
    "dare l'IP ai telefoni"
   ],
   "a": 0,
   "spiega": ""
  },
  {
   "tipo": "c",
   "area": "rete",
   "tema": "dns",
   "q": "Il DNS fa…",
   "o": [
    "da rubrica: traduce un nome in un numero",
    "da stampante",
    "da antivirus"
   ],
   "a": 0,
   "spiega": ""
  }
 ]
};
