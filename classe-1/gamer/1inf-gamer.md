# Il laboratorio del gamer · مختبر اللاعب · 玩家实验室

**Versione 1.0** — 21/10/2026 · 1INF · 21/10/2026 · bit e byte di immagini e film, ping, lag, FPS, Hz, monitor, schede video, cavi VGA e HDMI

La pagina della lezione, con il ripasso: https://nicolaregge-pulse.github.io/corso-informatica/verifica/?b=1inf-gamer

## 01 Ripasso: Mbps e MB

La rete si misura in **Mbps** (megabit al secondo). 1 byte = 8 bit, quindi 100 Mbps = 12,5 MB al secondo. Per i giochi però la velocità non basta: conta anche **quanto in fretta** arriva la risposta.

## 02 Il ping

Il **ping** è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in **millisecondi (ms)**: 1000 ms = 1 secondo.PingCome si giocasotto 30 msottimo30-60 msbuono60-100 mssi sente un po'oltre 150 mslag: i colpi arrivano in ritardoIl ping dipende soprattutto dalla **distanza** dal server, non dai Mbps. **Apri il Laboratorio del gamer** (../1inf-gamer/): prova il gioco dei bersagli con ping 20 e con ping 200.

## 03 Il jitter

Il **jitter** è quanto il ping **cambia** da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping.

## 04 Lag, scatti e pacchetti persi

ParolaChe cosa vuol direDa dove viene**lag**il gioco risponde in ritardoping alto**scatti** di retemovimenti a saltijitter alto**pacchetti persi** (packet loss)pezzi di informazione che non arrivanoWi-Fi debole, rete piena**scatti** del PC (FPS bassi)l'immagine va a scatti anche offlinescheda video troppo lentaIl cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo.

## 05 Gli FPS

Un video o un gioco è fatto di tante **immagini ferme** mostrate una dopo l'altra. **FPS** = frame per second, immagini al secondo.FPSCome appare15a scatti30accettabile, film e console vecchie60fluido144 e piùmolto fluido, giochi velociGli FPS li produce la **scheda video**. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS.

## 06 Gli Hz del monitor

Gli **Hz** (hertz) dicono quante volte al secondo il **monitor** ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.
Regola: **FPS della scheda video e Hz del monitor devono andare d'accordo**. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando.

## 07 I tipi di monitor

TipoPregioDifetto**TN**velocissimo, economicocolori spenti, angolo di visione stretto**IPS**colori belli, si vede bene di latoun po' più lento**VA**neri profondi, buon contrastoa volte scie nelle scene veloci**OLED**neri perfetti, velocissimocostosoIl **tempo di risposta** (1-5 ms) dice quanto in fretta un pixel cambia colore: più basso, meno scie.

## 08 La scheda video

La **scheda video** (GPU) disegna le immagini del gioco.
**Integrata**: dentro il processore, consuma poco, va bene per scuola e video.
**Dedicata**: una scheda a parte con la sua memoria (**VRAM**, per esempio 8 GB), serve per i giochi pesanti.
Più la risoluzione è alta (4K) e più gli FPS che vuoi, più la scheda video deve essere potente.

## 09 Quanto pesano immagini e film

Un'immagine è fatta di **pixel**; ogni pixel ha un colore di **3 byte** (rosso, verde, blu). Una foto Full HD: 1920 × 1080 pixel × 3 byte ≈ **6 MB** senza compressione. Il formato **JPG** la comprime a circa 0,5-1 MB.
Un **film** è un'immagine ripetuta 24-30 volte al secondo: 2 ore senza compressione sarebbero più di 1000 GB! Grazie alla compressione (MP4) diventa circa 2 GB. Per questo lo streaming funziona anche con pochi Mbps.

## 10 Il cavo video e la banda

Il PC si collega al monitor con un cavo video: **VGA** (vecchio, analogico, connettore blu a 15 piedini, immagine meno nitida), **DVI** (digitale, bianco), **HDMI** (digitale, porta anche l'audio, il più diffuso), **DisplayPort** (digitale, per i monitor da gaming). Dalla scheda video al monitor passano tantissimi dati. Il conto: **pixel × 3 byte di colore × Hz**. Full HD a 60 Hz: 1920 × 1080 × 24 bit × 60 ≈ **3 Gbit al secondo**.CavoBanda massima (circa)HDMI 1.410 Gbit/sHDMI 2.018 Gbit/sDisplayPort 1.432 Gbit/sHDMI 2.148 Gbit/sPer un monitor 4K a 144 Hz serve un cavo nuovo. **Apri il Laboratorio del gamer** (../1inf-gamer/), parte 3: calcola la banda del tuo monitor ideale.

## 11 Il mio setup da gamer

Ultima prova: scegli il tuo **gioco preferito** e il setup giusto per giocarlo: cavo o Wi-Fi, quanti Hz, che monitor, che scheda video, che cavo video. Lo scrivi nella verifica con le tue parole e i tuoi numeri.

## 12 Che cosa fare oggi

1. Studia nel PDF delle slide le pagine da 7 a 12 e le pagine 23 e 24.
2. Leggi la teoria e fai il ripasso sulla pagina della lezione.
3. Prova il laboratorio: https://nicolaregge-pulse.github.io/corso-informatica/1inf-gamer/
4. Fai il quiz su Google Moduli (link su Classroom) e premi Invia.
