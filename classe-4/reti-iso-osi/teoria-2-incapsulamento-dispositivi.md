# Teoria 2 di 3 — Incapsulamento e dispositivi di rete

**Versione 2.0** — 06/10/2026 — Classe 4, Reti.

## 1. L'incapsulamento: le buste

Chi spedisce, scendendo dal 7 all'1, **aggiunge** a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le **toglie** nell'ordine inverso.

MAC

IP

TCP

Ciao prof!

coda MAC

Il frame che viaggia sul cavo: il messaggio dentro tre buste

## 2. Come si chiama il pezzo di dati (PDU)

| Livello | Nome del pezzo (PDU) |
| 7 · 6 · 5 | dati |
| 4 Trasporto | segmento |
| 3 Rete | pacchetto |
| 2 Collegamento | frame (trama) |
| 1 Fisico | bit |

**PDU** = Protocol Data Unit, unità di dati del protocollo: il nome del pezzo di dati a quel livello.

## 3. Due indirizzi diversi: MAC e IP

|  | Indirizzo MAC (livello 2) | Indirizzo IP (livello 3) |
| Cos'è | il «nome e cognome» della scheda di rete, scritto in fabbrica | l'«indirizzo di casa», dato dalla rete in cui sei |
| Esempio | `3C:52:82:1A:7F:09` | `192.168.1.23` |
| Dove vale | solo dentro la rete locale | anche tra reti diverse, fino a Internet |
| Chi lo usa | lo switch | il router |

## 4. I dispositivi e il loro livello

| Dispositivo | Livello | Cosa fa |
| cavo, antenna, hub | 1 | trasporta i bit; l'hub ripete tutto a tutte le porte |
| scheda di rete | 1-2 | trasforma i dati in segnali; ha il MAC |
| switch, access point Wi-Fi | 2 | consegna il frame solo al dispositivo giusto, usando il MAC |
| router | 3 | collega reti diverse e sceglie la strada, usando l'IP |
| firewall | 3-4 e oltre | decide cosa può passare (indirizzi, porte) |

Il «modem» di casa di solito è **più dispositivi in uno**: router + switch + access point Wi-Fi.

## 5. Trasporto: TCP o UDP

| TCP | UDP |
| come una **raccomandata con ricevuta**: controlla che arrivi tutto, in ordine | come una **cartolina**: veloce, ma se un pezzo si perde va avanti |
| download, siti web, email | videochiamate, giochi online, dirette |

Le **porte** dicono a quale programma va il segmento: 80 = web (HTTP), 443 = web sicuro (HTTPS), 53 = DNS.

**Carta e penna:** disegna le buste di un messaggio (MAC · IP · TCP · dati · coda) e scrivi sotto ogni busta il suo livello.
