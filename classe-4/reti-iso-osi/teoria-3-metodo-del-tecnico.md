# Teoria 3 di 3 — Il metodo del tecnico di rete

**Versione 2.0** — 06/10/2026 — Classe 4, Reti.

## 1. ISO/OSI e TCP/IP

ISO/OSI è il modello per **ragionare**; Internet usa il modello **TCP/IP**, che ha 4 livelli e raggruppa quelli OSI così:

| TCP/IP (4 livelli) | Livelli ISO/OSI |
| Applicazione | 7 · 6 · 5 |
| Trasporto | 4 |
| Internet | 3 |
| Accesso alla rete | 2 · 1 |

## 2. Il metodo: dal basso verso l'alto

Quando «Internet non va», il tecnico controlla **prima i livelli bassi**: se il cavo è staccato, è inutile cercare il problema nel browser.

| Livello | Cosa controllo | Come |
| 1 Fisico | cavo collegato, lucine accese, Wi-Fi attivo | guardo e tocco: lucina della scheda di rete, icona della rete |
| 2 Collegamento | switch o access point acceso, porta funzionante | cambio porta o cavo; mi ricollego al Wi-Fi |
| 3 Rete | il PC ha un IP giusto? il router risponde? | `ipconfig`: se l'IP inizia con 169.254 non l'ha ricevuto; `ping` al router |
| 4-7 | il servizio e il nome del sito funzionano? | `ping 8.8.8.8` va ma il sito no → problema di DNS |

**ipconfig** mostra l'indirizzo IP del PC; **ping** manda un piccolo messaggio e aspetta la risposta (protocollo ICMP, livello 3). **DNS** traduce il nome del sito (www.google.it) in un indirizzo IP.

## 3. Tre casi svolti

| Sintomo | Livello | Cosa faccio |
| L'icona della rete ha una X: «cavo di rete scollegato» | 1 | ricollego il cavo o lo cambio |
| `ipconfig` mostra 169.254.10.5 | 3 | il PC non ha ricevuto l'IP dal router: riavvio la scheda di rete, controllo il router |
| `ping 8.8.8.8` risponde ma www.google.it non si apre | 7 (DNS) | il collegamento c'è, manca la traduzione dei nomi: controllo il DNS |

**Carta e penna:** scrivi i 4 controlli in ordine, dal livello 1 in su. È la scaletta che userai anche in Packet Tracer.
