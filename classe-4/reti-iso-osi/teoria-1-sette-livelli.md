# Teoria 1 di 3 — I sette livelli ISO/OSI

**Versione 2.0** — 06/10/2026 — Classe 4, Reti.

**Perché ci serve:** ogni messaggio che parte dal tuo PC attraversa **7 livelli**. Se sai a quale livello sta un problema, sai **dove cercare il guasto**: è il lavoro del tecnico di rete ed è la base dell'esame con **Packet Tracer**.

## 1. L'idea: come spedire un pacco

Tu scrivi il biglietto, lo metti in una scatola, il negozio scrive l'indirizzo, il corriere sceglie la strada, il furgone lo porta. Ognuno fa **un solo lavoro** e si fida di quello sotto. Una rete funziona allo stesso modo: **7 livelli**, ognuno con il suo compito.

## 2. La tabella dei 7 livelli

| Livello | Cosa fa | Esempi |
| 
7 Applicazione
 | i programmi che usi: dove nasce il messaggio | HTTP, HTTPS, DNS, SMTP |
| 
6 Presentazione
 | traduce in un formato comune, cifra e comprime | TLS (lucchetto), JPEG, ASCII |
| 
5 Sessione
 | apre, tiene aperta e chiude la conversazione | sessioni, login |
| 
4 Trasporto
 | spezza in pezzi, numera, controlla che arrivino tutti | TCP, UDP, porte (80, 443) |
| 
3 Rete
 | indirizzo IP e scelta della strada tra reti | IP, ICMP (ping) |
| 
2 Collegamento dati
 | indirizzo MAC, consegna nella rete locale | Ethernet, Wi-Fi (MAC) |
| 
1 Fisico
 | i bit come segnali: corrente, luce, onde radio | RJ45, fibra, Wi-Fi |

## 3. Come ricordarli

1. Dal basso (1) all'alto (7): **F**isico, **C**ollegamento, **R**ete, **T**rasporto, **S**essione, **P**resentazione, **A**pplicazione.
1. Frase per ricordare le iniziali F-C-R-T-S-P-A: **«Fiori Colorati Rendono Tutti Sereni, Perfino gli Arrabbiati»**.
1. In inglese (Physical, Data link, Network, Transport, Session, Presentation, Application): «Please Do Not Throw Sausage Pizza Away».

## 4. Guarda il viaggio

Apri la pagina interattiva **Il viaggio di un pacchetto** (è nella pagina della classe): fai scendere il messaggio dal 7 all'1 e guardalo risalire dall'altra parte.

**Carta e penna:** disegna la pila dei 7 livelli, dal 7 in alto all'1 in basso, ognuno con il suo colore. Ti serve per l'Esercitazione 1.
