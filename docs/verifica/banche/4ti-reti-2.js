// Generato da classe-4/reti-dispositivi/_build/parti.js (27/10/2026): parte 2 di 4 della lezione 4ti-reti-dispositivi.
window.BANCA = {
 "id": "4ti-reti-2-v1",
 "classe": "4TI",
 "titolo": "Le reti, parte 2 di 4: lo switch e il router",
 "sotto": "4TI · 27/10/2026 · leggi le schede, fai il ripasso, poi il quiz su Moduli in fondo all'ultima scheda",
 "stato": "stato/4ti-reti-2.json",
 "risultati": "risultati.html?b=4ti-reti-2",
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
  "switch": 1,
  "router": 2
 },
 "schede": [
  {
   "titolo": "4. Lo switch (e il vecchio hub)",
   "testo": "Lo <b>switch</b> è la «ciabatta» della rete: ha tante prese (porte) dove infili i cavi dei PC. Lavora al <b>livello 2</b> e guarda l'<b>indirizzo MAC</b>.<br><br>Lo switch impara chi è collegato a ogni porta e lo scrive nella sua <b>tabella degli indirizzi MAC</b>:<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Porta</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Indirizzo MAC che ha visto</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3C-52-82-1A-7F-09 (PC del prof)</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">2</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">A4-BB-6D-10-22-3E (PC 2)</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">F0-1F-AF-55-90-0C (stampante)</td></tr></table>Così manda ogni frame <b>solo</b> al PC giusto.<br><br>L'<b>hub</b> (livello 1) invece non capisce gli indirizzi: ripete tutto a tutti.<br><b>Paragone:</b> l'hub è chi grida in corridoio; lo switch è il postino che porta la lettera alla porta giusta."
  },
  {
   "titolo": "5. Il router: la porta verso le altre reti",
   "testo": "Il <b>router</b> lavora al <b>livello 3</b> e guarda l'<b>indirizzo IP</b>. Collega reti diverse e sceglie la strada, come un navigatore.<br><br>Il <b>gateway predefinito</b> è l'indirizzo del router della tua rete: è la «porta d'uscita». Quando il PC deve parlare con qualcuno fuori dalla LAN, manda il pacchetto lì.<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\"></th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Switch</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Router</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Livello</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">2 Collegamento</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">3 Rete</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Guarda</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'indirizzo MAC</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'indirizzo IP</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Lavora</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">dentro la stessa rete</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">tra reti diverse</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Paragone</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">il postino del condominio</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">l'ufficio postale che smista tra città</td></tr></table><b>NAT in parole semplici:</b> a casa tutti i dispositivi hanno un IP privato (192.168…). Verso Internet il router li fa uscire tutti con <b>un solo</b> IP pubblico, e poi ricorda a chi riportare le risposte. Come il centralino di un'azienda: un solo numero fuori, tanti interni dentro.<div style=\"margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px\"><p style=\"margin:0 0 8px\"><b>FINE DELLA PARTE 2.</b> Adesso il quiz: domande su quello che hai appena letto. Rispondi da solo, senza AI.</p><b>Il quiz della parte 2 arriva tra poco: premi F5.</b><p style=\"margin:10px 0 0\">Poi aspetta il via del prof per la parte 3.</p></div>"
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
   "q": "Lo switch manda il frame…",
   "o": [
    "solo al PC giusto, grazie alla tabella dei MAC",
    "a tutti i PC",
    "a Internet"
   ],
   "a": 0,
   "spiega": "L'hub invece lo manda a tutti.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "",
   "q": "Il gateway predefinito è…",
   "o": [
    "l'indirizzo del router, la porta d'uscita della rete",
    "il nome del Wi-Fi",
    "la password del PC"
   ],
   "a": 0,
   "spiega": "Lì vanno i pacchetti diretti fuori dalla LAN.",
   "scheda": 2
  }
 ],
 "crocette": [
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "switch",
   "q": "La differenza tra switch e hub è che lo switch…",
   "o": [
    "manda i dati solo al PC giusto",
    "è più colorato",
    "funziona senza corrente"
   ],
   "a": 0,
   "spiega": "L'hub ripete tutto a tutti."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "switch",
   "q": "Nella sua tabella lo switch scrive…",
   "o": [
    "quale indirizzo MAC c'è su ogni porta",
    "le password degli utenti",
    "i siti visitati"
   ],
   "a": 0,
   "spiega": "Così sa dove mandare ogni frame."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "router",
   "q": "Il router di casa usa il NAT per…",
   "o": [
    "far uscire tutti i dispositivi con un solo IP pubblico",
    "cambiare il nome del Wi-Fi",
    "rendere più veloce il cavo"
   ],
   "a": 0,
   "spiega": "Come il centralino: un numero fuori, tanti interni dentro."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "router",
   "q": "Il PC vuole aprire un sito fuori dalla scuola. A chi manda il pacchetto per primo?",
   "o": [
    "al gateway predefinito (il router)",
    "alla stampante",
    "all'hub"
   ],
   "a": 0,
   "spiega": "Il gateway è la porta d'uscita della LAN."
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
   "tema": "switch",
   "q": "Lo switch guarda l'indirizzo…",
   "o": [
    "MAC",
    "IP",
    "e-mail"
   ],
   "a": 0,
   "spiega": "Livello 2."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "router",
   "q": "Il router guarda l'indirizzo…",
   "o": [
    "IP",
    "MAC",
    "del sito"
   ],
   "a": 0,
   "spiega": "Livello 3."
  },
  {
   "tipo": "c",
   "area": "nozioni",
   "tema": "switch",
   "q": "L'hub…",
   "o": [
    "ripete i bit a tutti, senza capire gli indirizzi",
    "sceglie la strada con l'IP",
    "è un firewall"
   ],
   "a": 0,
   "spiega": "Livello 1."
  }
 ]
};
