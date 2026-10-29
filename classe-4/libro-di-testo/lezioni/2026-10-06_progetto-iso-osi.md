# Il progetto individuale e il modello ISO/OSI

**Versione 1.0** — 29/10/2026
*Libro parziale della 4TI: la lezione del 06/10/2026. Fa parte del libro di testo della classe (libro-classe4). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 06/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Progetto individuale (idea di gioco o applicazione, prima versione); modello ISO/OSI con quiz.

### La teoria e l'esercitazione

**Perché ci serve:** ogni messaggio che parte dal tuo PC attraversa **7 livelli**. Se sai a quale livello sta un problema, sai **dove cercare il guasto**: è il lavoro del tecnico di rete ed è la base dell'esame con **Packet Tracer**.

#### 1. L'idea: come spedire un pacco

Tu scrivi il biglietto, lo metti in una scatola, il negozio scrive l'indirizzo, il corriere sceglie la strada, il furgone lo porta. Ognuno fa **un solo lavoro** e si fida di quello sotto. Una rete funziona allo stesso modo: **7 livelli**, ognuno con il suo compito.

#### 2. La tabella dei 7 livelli

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

#### 3. Come ricordarli

1. Dal basso (1) all'alto (7): **F**isico, **C**ollegamento, **R**ete, **T**rasporto, **S**essione, **P**resentazione, **A**pplicazione.
1. Frase per ricordare le iniziali F-C-R-T-S-P-A: **«Fiori Colorati Rendono Tutti Sereni, Perfino gli Arrabbiati»**.
1. In inglese (Physical, Data link, Network, Transport, Session, Presentation, Application): «Please Do Not Throw Sausage Pizza Away».

#### 4. Guarda il viaggio

Apri la pagina interattiva **Il viaggio di un pacchetto** (è nella pagina della classe): fai scendere il messaggio dal 7 all'1 e guardalo risalire dall'altra parte.

**Carta e penna:** disegna la pila dei 7 livelli, dal 7 in alto all'1 in basso, ognuno con il suo colore. Ti serve per l'Esercitazione 1.

#### 1. L'incapsulamento: le buste

Chi spedisce, scendendo dal 7 all'1, **aggiunge** a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le **toglie** nell'ordine inverso.

MAC

IP

TCP

Ciao prof!

coda MAC

Il frame che viaggia sul cavo: il messaggio dentro tre buste

#### 2. Come si chiama il pezzo di dati (PDU)

| Livello | Nome del pezzo (PDU) |
| 7 · 6 · 5 | dati |
| 4 Trasporto | segmento |
| 3 Rete | pacchetto |
| 2 Collegamento | frame (trama) |
| 1 Fisico | bit |

**PDU** = Protocol Data Unit, unità di dati del protocollo: il nome del pezzo di dati a quel livello.

#### 3. Due indirizzi diversi: MAC e IP

|  | Indirizzo MAC (livello 2) | Indirizzo IP (livello 3) |
| Cos'è | il «nome e cognome» della scheda di rete, scritto in fabbrica | l'«indirizzo di casa», dato dalla rete in cui sei |
| Esempio | `3C:52:82:1A:7F:09` | `192.168.1.23` |
| Dove vale | solo dentro la rete locale | anche tra reti diverse, fino a Internet |
| Chi lo usa | lo switch | il router |

#### 4. I dispositivi e il loro livello

| Dispositivo | Livello | Cosa fa |
| cavo, antenna, hub | 1 | trasporta i bit; l'hub ripete tutto a tutte le porte |
| scheda di rete | 1-2 | trasforma i dati in segnali; ha il MAC |
| switch, access point Wi-Fi | 2 | consegna il frame solo al dispositivo giusto, usando il MAC |
| router | 3 | collega reti diverse e sceglie la strada, usando l'IP |
| firewall | 3-4 e oltre | decide cosa può passare (indirizzi, porte) |

Il «modem» di casa di solito è **più dispositivi in uno**: router + switch + access point Wi-Fi.

#### 5. Trasporto: TCP o UDP

| TCP | UDP |
| come una **raccomandata con ricevuta**: controlla che arrivi tutto, in ordine | come una **cartolina**: veloce, ma se un pezzo si perde va avanti |
| download, siti web, email | videochiamate, giochi online, dirette |

Le **porte** dicono a quale programma va il segmento: 80 = web (HTTP), 443 = web sicuro (HTTPS), 53 = DNS.

**Carta e penna:** disegna le buste di un messaggio (MAC · IP · TCP · dati · coda) e scrivi sotto ogni busta il suo livello.

#### 1. ISO/OSI e TCP/IP

ISO/OSI è il modello per **ragionare**; Internet usa il modello **TCP/IP**, che ha 4 livelli e raggruppa quelli OSI così:

| TCP/IP (4 livelli) | Livelli ISO/OSI |
| Applicazione | 7 · 6 · 5 |
| Trasporto | 4 |
| Internet | 3 |
| Accesso alla rete | 2 · 1 |

#### 2. Il metodo: dal basso verso l'alto

Quando «Internet non va», il tecnico controlla **prima i livelli bassi**: se il cavo è staccato, è inutile cercare il problema nel browser.

| Livello | Cosa controllo | Come |
| 1 Fisico | cavo collegato, lucine accese, Wi-Fi attivo | guardo e tocco: lucina della scheda di rete, icona della rete |
| 2 Collegamento | switch o access point acceso, porta funzionante | cambio porta o cavo; mi ricollego al Wi-Fi |
| 3 Rete | il PC ha un IP giusto? il router risponde? | `ipconfig`: se l'IP inizia con 169.254 non l'ha ricevuto; `ping` al router |
| 4-7 | il servizio e il nome del sito funzionano? | `ping 8.8.8.8` va ma il sito no → problema di DNS |

**ipconfig** mostra l'indirizzo IP del PC; **ping** manda un piccolo messaggio e aspetta la risposta (protocollo ICMP, livello 3). **DNS** traduce il nome del sito (www.google.it) in un indirizzo IP.

#### 3. Tre casi svolti

| Sintomo | Livello | Cosa faccio |
| L'icona della rete ha una X: «cavo di rete scollegato» | 1 | ricollego il cavo o lo cambio |
| `ipconfig` mostra 169.254.10.5 | 3 | il PC non ha ricevuto l'IP dal router: riavvio la scheda di rete, controllo il router |
| `ping 8.8.8.8` risponde ma www.google.it non si apre | 7 (DNS) | il collegamento c'è, manca la traduzione dei nomi: controllo il DNS |

**Carta e penna:** scrivi i 4 controlli in ordine, dal livello 1 in su. È la scaletta che userai anche in Packet Tracer.

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
