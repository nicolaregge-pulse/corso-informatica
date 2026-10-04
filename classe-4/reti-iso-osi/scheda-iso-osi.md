<!-- generato da scheda-iso-osi.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Il modello ISO/OSI — i 7 livelli di una rete

Classe 4 · Reti · 06/10/2026 · scheda di teoria

**Perché ci serve:** ogni volta che un messaggio parte dal tuo PC attraversa **7 livelli**. Se sai a quale livello sta un problema, sai **dove cercare il guasto** : è il lavoro del tecnico di rete, ed è la base dell'esame con **Packet Tracer**. Prima di leggere apri la pagina interattiva **Il viaggio di un pacchetto** (link su Classroom).

## 1\. La tabella dei 7 livelli

Livello| Cosa fa| Il pezzo di dati (PDU)| Dispositivo| Esempi| TCP/IP  
---|---|---|---|---|---  
7 Applicazione| i programmi che usi: dove nasce il messaggio| dati| —| HTTP, HTTPS, DNS, SMTP| Applicazione  
6 Presentazione| traduce in un formato comune, cifra e comprime| dati| —| TLS (lucchetto), JPEG, ASCII| Applicazione  
5 Sessione| apre, tiene aperta e chiude la conversazione| dati| —| sessioni, login| Applicazione  
4 Trasporto| spezza in pezzi, numera, controlla che arrivino tutti| segmento| —| TCP, UDP, porte (80, 443)| Trasporto  
3 Rete| indirizzo IP e scelta della strada tra reti| pacchetto| router| IP, ICMP (ping)| Internet  
2 Collegamento dati| indirizzo MAC, consegna nella rete locale| frame (trama)| switch, scheda di rete| Ethernet, Wi-Fi (MAC)| Accesso alla rete  
1 Fisico| i bit come segnali: corrente, luce, onde radio| bit| cavi, hub, antenne| RJ45, fibra, Wi-Fi| Accesso alla rete  
  
**PDU** (Protocol Data Unit, unità di dati del protocollo) = come si chiama il pezzo di dati a quel livello. **TCP/IP** = il modello usato davvero da Internet: ha **4 livelli** e raggruppa i livelli OSI come nell'ultima colonna.

## 2\. L'incapsulamento: le buste

Chi spedisce, scendendo dal 7 all'1, **aggiunge** a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le **toglie** nell'ordine inverso.

MACIPTCPCiao prof!coda MAC

Il frame che viaggia sul cavo: il messaggio dentro tre buste

## 3\. Il metodo del tecnico: dal basso verso l'alto

  1. **1 Fisico:** il cavo è collegato? La lucina della scheda di rete è accesa? Il Wi-Fi è attivo?
  2. **2 Collegamento:** lo switch è acceso? La porta funziona?
  3. **3 Rete:** il PC ha un indirizzo IP corretto? Il router risponde al `ping`?
  4. **4-7:** il servizio funziona? Il nome del sito si traduce (DNS)? Il programma è configurato bene?

**Carta e penna:** disegna la pila dei 7 livelli con i colori, e accanto a ogni livello il suo dispositivo e la sua PDU. Poi disegna le buste del punto 2.

Classe 4 · Scheda ISO/OSI · v1.0
