# Rete e gamer: ping, jitter, FPS e monitor

**Versione 1.0** — 29/10/2026
*Libro parziale della 1INF: la lezione del 23/10/2026. Fa parte del libro di testo della classe (libro-classe1). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 23/10/2026, 4 ore, Tecnologia e Laboratorio.
2. **Argomenti:** Ping, jitter, TCP e UDP, FPS e Hz, pannelli TN, VA e OLED, pixel e risoluzione; app «Le misure del mio PC» con le prove di ping, download e schermo; Documento personale; quiz su Moduli.

### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Nei giochi conta il ping (il tempo di risposta) più della velocità. Gli FPS sono le immagini al secondo, gli Hz quante volte il monitor si aggiorna.</p><p lang="ar" dir="rtl">في الألعاب يهمّ زمن الاستجابة (ping) أكثر من السرعة. FPS هي عدد الصور في الثانية، وHz عدد مرات تحديث الشاشة.</p><p lang="zh">玩游戏时 ping（响应时间）比网速更重要。FPS 是每秒画面数，Hz 是显示器每秒刷新的次数。</p></div>

### La teoria e l'esercitazione

Ping, jitter, TCP e UDP, FPS e Hz, pixel, monitor, scheda video, cavi video

Classe 1 · lezione del 23/10/2026 · Versione 1.0

Questa dispensa raccoglie la lezione: le slide, le foto della lavagna e tanti esempi con i conti fatti. In fondo trovi gli esercizi «Prova tu» con le soluzioni.

#### 01 Il ping

Il **ping** è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e a tornare indietro. Si misura in **millisecondi (ms)**: 1000 ms = 1 secondo.

| Ping | Come si gioca |
|---|---|
| sotto 30 ms | ottimo |
| 30-60 ms | buono |
| 60-100 ms | si sente un po' |
| oltre 150 ms | lag: i colpi arrivano in ritardo |

Il ping dipende soprattutto dalla **distanza** dal server, non dai Mbps.

> **Esempio.** Giochi su un server a Milano: ping 15 ms. Lo stesso gioco su un server in America: ping 120 ms. La tua linea è la stessa (100 Mbps): cambia solo la strada che fa il messaggio. Con 120 ms premi «spara» e il server lo riceve 60 ms dopo (metà del viaggio): intanto l'avversario si è già spostato.

![La lavagna della lezione](../../byte-velocita/immagini/lavagna-20261023/01_streaming-ftp-ping-jitter_doc.jpg)

*La lavagna della lezione: In alto: streaming senza ritrasmissione e FTP con ritrasmissione (capitolo 03). Al centro: il grafico del ping, con tempi di 23, 30 e 40 ms e un picco molto più alto. In basso: le onde del jitter.*

#### 02 Il jitter

Il **jitter** è quanto il ping **cambia** da un momento all'altro.

> **Esempio.** Ping misurati: 40, 41, 39, 40 ms. Cambiano di 1-2 ms: jitter **basso**, il gioco è regolare.  
> Ping misurati: 20, 120, 30, 110 ms. Cambiano di circa 100 ms: jitter **alto**, il personaggio salta e a volte si teletrasporta.

Sulla lavagna: le onde grandi sono una connessione a scatti (jitter alto); la riga quasi piatta in fondo è una connessione stabile (jitter basso).

> **Nota.** Meglio un ping di 50 ms sempre uguale che un ping che salta tra 20 e 120 ms.

#### 03 Con o senza ritrasmissione: TCP e UDP

In rete i dati viaggiano a **pacchetti**, cioè piccoli pezzi. A volte un pacchetto si perde per strada. Per spedire ci sono due regole, che si chiamano **protocolli**:

| Protocollo | Se un pacchetto si perde | Pregio | Si usa per |
|---|---|---|---|
| TCP | viene rimandato (con ritrasmissione, in inglese «retry») | arriva tutto, in ordine | file (FTP), pagine web, email, download |
| UDP | non viene rimandato (senza ritrasmissione) | più veloce, meno ritardo | streaming, videochiamate, giochi online |

> **Esempio.** Scarichi un file con FTP: se manca anche un solo pacchetto il file è rotto, quindi TCP lo rimanda. In una partita online un pacchetto perso diventa solo un piccolo scatto: aspettarlo bloccherebbe il gioco, quindi si usa UDP.

> **Nota.** Per ricordarlo: TCP è una raccomandata con ricevuta di ritorno; UDP è un volantino nella cassetta della posta: arriva prima, ma se si perde nessuno lo rimanda. TCP/IP è il nome di tutta la famiglia di regole di Internet.

#### 04 Lag, scatti e pacchetti persi

| Parola | Che cosa vuol dire | Da dove viene |
|---|---|---|
| lag | il gioco risponde in ritardo | ping alto |
| scatti di rete | movimenti a salti | jitter alto |
| pacchetti persi | pezzi di informazione che non arrivano | Wi-Fi debole, rete piena |
| scatti del PC | l'immagine va a scatti anche senza Internet | scheda video troppo lenta (FPS bassi) |

> **Esempio.** Il gioco va a scatti anche quando giochi senza Internet: la colpa non è della rete ma della scheda video. Se invece va a scatti solo online, controlla ping e jitter e prova il cavo al posto del Wi-Fi.

> **Nota.** Il cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo.

#### 05 Gli FPS

Un video o un gioco è fatto di tante **immagini ferme** mostrate una dopo l'altra, come un cartone animato. **FPS** vuol dire «frame per second», cioè immagini al secondo. Gli FPS li prepara la **scheda video**.

| FPS | Come appare |
|---|---|
| 15 | a scatti |
| 30 | accettabile: film e console vecchie |
| 60 | fluido |
| 144 e più | molto fluido, per i giochi veloci |

> **Esempio.** A 60 FPS ogni immagine resta sullo schermo 1000 : 60 ≈ 17 ms. A 30 FPS resta 1000 : 30 ≈ 33 ms, il doppio: si vede meno fluido. A 144 FPS resta circa 7 ms.

#### 06 Gli Hz del monitor

Gli **Hz** (hertz) dicono quante volte al secondo il **monitor** ridisegna lo schermo. In inglese si dice «refresh rate», frequenza di aggiornamento.

> **Nota.** Regola: gli FPS della scheda video e gli Hz del monitor devono andare d'accordo.

> **Esempio.** Scheda video a 30 FPS, monitor a 120 Hz: il monitor ridisegna 120 volte al secondo ma ha solo 30 immagini nuove. Ogni immagine viene mostrata 4 volte (120 : 30 = 4): il monitor veloce è sprecato.  
> Scheda video a 200 FPS, monitor a 60 Hz: vedi comunque solo 60 immagini al secondo: la scheda video è sprecata.  
> Scheda video a 144 FPS, monitor a 144 Hz: tutto d'accordo, massima fluidità.

![La lavagna della lezione](../../byte-velocita/immagini/lavagna-20261023/02_tcp-udp-fps-hz_doc.jpg)

*La lavagna della lezione: In alto: TCP/IP e UDP. Al centro: le immagini in fila (da 15 a 240 al secondo). In basso: 30 FPS su un monitor a 120 Hz, ogni immagine ripetuta 4 volte.*

#### 07 Pixel e risoluzione

Lo schermo è una griglia di quadratini colorati: ogni quadratino è un **pixel**. La **risoluzione** dice quanti pixel ci sono in larghezza e in altezza.

| Nome | Larghezza × altezza | Pixel in tutto (circa) |
|---|---|---|
| HD | 1280 × 720 | 0,9 milioni |
| Full HD | 1920 × 1080 | 2 milioni |
| 2K (QHD) | 2560 × 1440 | 3,7 milioni |
| 4K | 3840 × 2160 | 8,3 milioni |

> **Esempio.** 1920 × 1080 = 2.073.600, cioè circa 2 milioni di pixel.  
> Il 4K ha il doppio dei pixel in larghezza e il doppio in altezza: 2 × 2 = 4 volte il Full HD. Per questo serve una scheda video più potente.

![La lavagna della lezione](../../byte-velocita/immagini/lavagna-20261023/04_pixel-risoluzione_doc.jpg)

*La lavagna della lezione: La griglia dei pixel e il conto 1920 × 1080 ≈ 2 milioni.*

#### 08 I tipi di monitor

Lo schermo può essere fatto in modi diversi: si chiamano **pannelli**. L'**angolo di visione** dice da quanto di lato vedi ancora bene i colori.

| Pannello | Angolo (lavagna) | Pregio | Difetto |
|---|---|---|---|
| TN | circa 90° | velocissimo (tanti Hz), economico | colori spenti, angolo stretto |
| IPS | 120° | colori belli, si vede bene di lato | un po' più lento |
| VA | 160° | neri profondi, buon contrasto | scia dietro le cose che si muovono |
| OLED | molto ampio | neri perfetti, velocissimo | costa tanto |

Sul VA la pallina che si muove lascia una scia, soprattutto nelle scene scure: si chiama **ghosting**, «immagine fantasma». Il **tempo di risposta** (1-5 ms) dice quanto in fretta un pixel cambia colore: più è basso, meno scie.

> **Esempio.** Chi gioca a sparatutto veloci e ha pochi soldi: TN o IPS veloce. Chi guarda film al buio: VA o OLED. Chi vuole il massimo e può spendere: OLED.

> **Nota.** Oggi i pannelli IPS e VA arrivano quasi a 178° e ci sono anche IPS a 144-240 Hz: i numeri della lavagna servono a capire la differenza tra i pannelli.

![La lavagna della lezione](../../byte-velocita/immagini/lavagna-20261023/03_pannelli-tn-va-oled_doc.jpg)

*La lavagna della lezione: Gli angoli di visione (90°, 120°, 160°), la scia del VA, l'OLED che costa tanto.*

#### 09 La scheda video

La **scheda video** (in inglese GPU) disegna le immagini del gioco. **Integrata**: è dentro il processore, consuma poco, va bene per la scuola e i video. **Dedicata**: è una scheda a parte con la sua memoria (**VRAM**, per esempio 8 GB) e serve per i giochi pesanti.

> **Esempio.** Per scuola, video e Classroom basta la scheda integrata. Per un gioco 3D in Full HD a 144 FPS serve una scheda dedicata con almeno 8 GB di VRAM.

#### 10 Quanto pesano immagini e film

Ogni pixel ha un colore fatto di **3 byte**: rosso, verde, blu.

> **Esempio.** Una foto Full HD: 2.073.600 pixel × 3 byte = 6.220.800 byte, circa **6 MB**. Il formato JPG la comprime (la rende più piccola) a circa 0,5-1 MB.  
> Un film di 2 ore mostra 24 immagini al secondo: 6 MB × 24 = 144 MB ogni secondo; 2 ore sono 7200 secondi; 144 × 7200 = 1.036.800 MB, circa **1000 GB**. Con la compressione MP4 diventa circa 2 GB: 500 volte più piccolo. Per questo lo streaming funziona anche con pochi Mbps.

#### 11 Il cavo video e la banda

Il PC si collega al monitor con un **cavo video**: **VGA** (vecchio, connettore blu a 15 piedini, immagine meno nitida), **DVI** (digitale, bianco), **HDMI** (digitale, porta anche l'audio, il più diffuso), **DisplayPort** (digitale, per i monitor da gaming). La **banda** è quanti dati passano nel cavo ogni secondo: pixel × 24 bit di colore × Hz.

| Cavo | Banda massima (circa) |
|---|---|
| HDMI 1.4 | 10 Gbit/s |
| HDMI 2.0 | 18 Gbit/s |
| DisplayPort 1.4 | 32 Gbit/s |
| HDMI 2.1 | 48 Gbit/s |

> **Esempio.** Full HD a 60 Hz: 1920 × 1080 × 24 × 60 = 2.985.984.000 bit al secondo, circa **3 Gbit/s**: va bene anche HDMI 1.4.  
> 4K a 144 Hz: 3840 × 2160 × 24 × 144 = circa **28,7 Gbit/s**: HDMI 2.0 (18) non basta, serve DisplayPort 1.4 (32) o HDMI 2.1 (48).

#### 12 Esempio completo: il mio setup da gamer

Ecco un setup scelto per un gioco veloce, con i conti. Poi tocca a te, con il tuo gioco preferito.

| Che cosa | Scelta | Perché |
|---|---|---|
| gioco | uno sparatutto online | serve rapidità |
| rete | cavo, ping sotto 30 ms | ping e jitter bassi |
| monitor | IPS, Full HD, 144 Hz | veloce e con bei colori |
| scheda video | dedicata, 8 GB di VRAM | fa 144 FPS in Full HD |
| cavo video | DisplayPort 1.4 | 1920 × 1080 × 24 × 144 ≈ 7,2 Gbit/s: basta anche HDMI 2.0 |

#### 13 Prova tu

1. Ping misurati: 35, 36, 34, 35 ms. Il jitter è alto o basso?
2. Scheda video a 60 FPS, monitor a 240 Hz: quante volte viene mostrata ogni immagine?
3. Quanti pixel ha uno schermo 1280 × 720?
4. Scarichi un aggiornamento del gioco: TCP o UDP? E per la voce nella chat della squadra?
5. Il gioco va a scatti anche senza Internet: colpa della rete o della scheda video?
6. Un monitor 2K (2560 × 1440) a 60 Hz: basta un cavo HDMI 1.4?

##### Soluzioni

1. Basso: cambia solo di 1-2 ms.
2. 4 volte: 240 : 60 = 4.
3. 1280 × 720 = 921.600 pixel.
4. L'aggiornamento con TCP: il file deve arrivare intero. La voce con UDP: meglio un piccolo salto che un ritardo.
5. Della scheda video (FPS bassi).
6. 2560 × 1440 × 24 × 60 ≈ 5,3 Gbit/s: sì, HDMI 1.4 arriva a 10.

#### 14 Parole nuove

| Parola | Che cosa vuol dire |
|---|---|
| ping | tempo di andata e ritorno di un messaggio, in ms |
| jitter | quanto cambia il ping |
| lag | ritardo nel gioco |
| pacchetto | piccolo pezzo di dati che viaggia in rete |
| protocollo | regola per spedire i dati (TCP, UDP) |
| FPS | immagini al secondo preparate dalla scheda video |
| Hz | volte al secondo che il monitor ridisegna lo schermo |
| pixel | quadratino colorato dello schermo |
| risoluzione | pixel in larghezza × pixel in altezza |
| pannello | il tipo di schermo: TN, IPS, VA, OLED |
| VRAM | la memoria della scheda video |
| banda | quanti dati passano ogni secondo |

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
