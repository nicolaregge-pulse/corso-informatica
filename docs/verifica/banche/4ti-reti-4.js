// Generato da classe-4/reti-dispositivi/_build/parti.js (27/10/2026): parte 4 di 4 della lezione 4ti-reti-dispositivi.
window.BANCA = {
 "id": "4ti-reti-4-v1",
 "classe": "4TI",
 "titolo": "Le reti, parte 4 di 4: il tuo indirizzo IP e il programma dell'anno",
 "sotto": "4TI · 27/10/2026 · leggi le schede, fai il ripasso, poi il quiz su Moduli in fondo all'ultima scheda",
 "stato": "stato/4ti-reti-4.json",
 "risultati": "risultati.html?b=4ti-reti-4",
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
  "ipconfig": 1,
  "anno": 2
 },
 "schede": [
  {
   "titolo": "8. Leggere la configurazione del tuo PC: ipconfig",
   "testo": "Ora guardi i numeri veri del tuo PC. <b>Non servono diritti di amministratore.</b><br>1. Premi il tasto <b>Windows</b> sulla tastiera.<br>2. Scrivi <b>cmd</b> e premi <b>Invio</b>: si apre una finestra nera (il Prompt dei comandi).<br>3. Scrivi <b>ipconfig</b> e premi <b>Invio</b>.<br>4. Cerca il blocco della tua scheda (Ethernet se hai il cavo, Wi-Fi se sei senza fili). Vedi qualcosa così:<pre style=\"background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap\">Scheda Ethernet Ethernet:\n\n   Indirizzo IPv4. . . . . . . . . : 192.168.10.37\n   Subnet mask . . . . . . . . . . : 255.255.255.0\n   Gateway predefinito . . . . . . : 192.168.10.1</pre><table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Riga</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Che cosa vuol dire</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Indirizzo IPv4</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">il numero del tuo PC nella rete (l'indirizzo di casa)</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Subnet mask (maschera)</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">dice quanto è grande il «quartiere»: chi è nella tua stessa rete</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Gateway predefinito</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'indirizzo del router, la porta d'uscita</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Server DNS</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">chi traduce i nomi in IP; lo vedi con <b>ipconfig /all</b></td></tr></table>Se l'IP comincia con <b>169.254</b>, il PC non ha ricevuto l'indirizzo dal DHCP: guarda il cavo e chiedi all'assistente."
  },
  {
   "titolo": "9. Che cosa faremo quest'anno",
   "testo": "Questa è la strada del laboratorio di quest'anno. Sono competenze che chiedono davvero le aziende:<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Tappa</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Che cosa fai</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Che cosa sai fare alla fine</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1. Cablaggio</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">prepari un cavo di rete e lo provi</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">collegare una postazione</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">2. Packet Tracer</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">costruisci una rete al computer, con PC, switch e router</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">progettare una rete senza comprare niente</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3. Configurare</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">dai gli indirizzi, configuri switch, router e access point</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">far parlare due reti</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">4. Sicurezza</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">password Wi-Fi, regole del firewall, aggiornamenti</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">proteggere una piccola rete</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">5. Progetto</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">il tuo progetto, che mostri alla classe e allo stage</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">un lavoro da mettere nel curriculum</td></tr></table>Packet Tracer è un programma gratuito che simula la rete: puoi sbagliare quanto vuoi, non si rompe niente.<div style=\"margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px\"><p style=\"margin:0 0 8px\"><b>FINE DELLA PARTE 4.</b> Adesso il quiz: domande su quello che hai appena letto. Rispondi da solo, senza AI.</p><b>Il quiz della parte 4 arriva tra poco: premi F5.</b><p style=\"margin:10px 0 0\">Poi l'ultima ora: il tuo progetto.</p></div>"
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
   "q": "Per vedere il tuo indirizzo IP scrivi nel Prompt dei comandi…",
   "o": [
    "ipconfig",
    "format",
    "shutdown"
   ],
   "a": 0,
   "spiega": "Non servono diritti di amministratore.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "Packet Tracer serve a…",
   "o": [
    "costruire una rete al computer, senza rompere niente",
    "giocare online",
    "scrivere documenti"
   ],
   "a": 0,
   "spiega": "È un simulatore di reti.",
   "scheda": 2
  }
 ],
 "crocette": [
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "ipconfig",
   "q": "Nel risultato di ipconfig, la riga «Gateway predefinito» ti dice…",
   "o": [
    "l'indirizzo del router della tua rete",
    "il nome del tuo PC",
    "la velocità del cavo"
   ],
   "a": 0,
   "spiega": "È la porta d'uscita verso le altre reti."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "ipconfig",
   "q": "ipconfig dice che il tuo IP è 169.254.8.20. Vuol dire che…",
   "o": [
    "il PC non ha ricevuto l'IP dal DHCP",
    "va tutto benissimo",
    "sei collegato al 5 GHz"
   ],
   "a": 0,
   "spiega": "Controlla il cavo e il livello 3."
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
   "tema": "ipconfig",
   "q": "Il comando per vedere il tuo IP è…",
   "o": [
    "ipconfig",
    "print",
    "save"
   ],
   "a": 0,
   "spiega": "Lo scrivi nel Prompt dei comandi."
  }
 ]
};
