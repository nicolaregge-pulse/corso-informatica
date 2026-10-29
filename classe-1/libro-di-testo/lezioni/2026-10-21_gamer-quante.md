# Il laboratorio del gamer: quante ce ne stanno?

**Versione 1.0** — 29/10/2026
*Libro parziale della 1INF: la lezione del 21/10/2026. Fa parte del libro di testo della classe (libro-classe1). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 21/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Quanto pesa un file e quante ne stanno, tempo di download, streaming e buffering; percorso «Quante ce ne stanno?», giochi dei byte, quiz su Moduli, domande orali.

### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Calcoliamo quante foto e film stanno in una memoria e quanto tempo serve a scaricarli.</p><p lang="ar" dir="rtl">نحسب كم صورة وفيلمًا تتسع لها الذاكرة وكم من الوقت يلزم لتنزيلها.</p><p lang="zh">计算一个存储器能放多少照片和电影，以及下载需要多长时间。</p></div>

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Ripasso: Mbps e MB · مراجعة · 复习

<div class="scheda">La rete si misura in <b>Mbps</b> (megabit al secondo). 1 byte = 8 bit, quindi 100 Mbps = 12,5 MB al secondo. Per i giochi però la velocità non basta: conta anche <b>quanto in fretta</b> arriva la risposta.</div>

#### 2. Il ping · البينغ · 延迟(ping)

<div class="scheda">Il <b>ping</b> è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in <b>millisecondi (ms)</b>: 1000 ms = 1 secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Ping</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come si gioca</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sotto 30 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ottimo</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30-60 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">buono</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60-100 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">si sente un po'</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">oltre 150 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">lag: i colpi arrivano in ritardo</td></tr></table>Il ping dipende soprattutto dalla <b>distanza</b> dal server, non dai Mbps. <a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>: prova il gioco dei bersagli con ping 20 e con ping 200.</div>

#### 3. Il jitter · التذبذب · 抖动

<div class="scheda">Il <b>jitter</b> è quanto il ping <b>cambia</b> da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping.</div>

#### 4. Lag, scatti e pacchetti persi · التأخير والتقطع · 卡顿和丢包

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Parola</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa vuol dire</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Da dove viene</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>lag</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il gioco risponde in ritardo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ping alto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>scatti</b> di rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">movimenti a salti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">jitter alto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>pacchetti persi</b> (packet loss)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">pezzi di informazione che non arrivano</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi debole, rete piena</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>scatti</b> del PC (FPS bassi)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'immagine va a scatti anche offline</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">scheda video troppo lenta</td></tr></table>Il cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo.</div>

#### 5. Gli FPS · الإطارات في الثانية · 帧率(FPS)

<div class="scheda">Un video o un gioco è fatto di tante <b>immagini ferme</b> mostrate una dopo l'altra. <b>FPS</b> = frame per second, immagini al secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">FPS</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come appare</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">15</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a scatti</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">accettabile, film e console vecchie</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fluido</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">144 e più</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">molto fluido, giochi veloci</td></tr></table>Gli FPS li produce la <b>scheda video</b>. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS.</div>

#### 6. Gli Hz del monitor · الهرتز · 刷新率(Hz)

<div class="scheda">Gli <b>Hz</b> (hertz) dicono quante volte al secondo il <b>monitor</b> ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.<br>Regola: <b>FPS della scheda video e Hz del monitor devono andare d'accordo</b>. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando.</div>

#### 7. I tipi di monitor · أنواع الشاشات · 显示器类型

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Tipo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Pregio</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Difetto</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>TN</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">velocissimo, economico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">colori spenti, angolo di visione stretto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>IPS</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">colori belli, si vede bene di lato</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un po' più lento</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>VA</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">neri profondi, buon contrasto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a volte scie nelle scene veloci</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>OLED</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">neri perfetti, velocissimo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">costoso</td></tr></table>Il <b>tempo di risposta</b> (1-5 ms) dice quanto in fretta un pixel cambia colore: più basso, meno scie.</div>

#### 8. La scheda video · بطاقة الرسوميات · 显卡

<div class="scheda">La <b>scheda video</b> (GPU) disegna le immagini del gioco.<br><b>Integrata</b>: dentro il processore, consuma poco, va bene per scuola e video.<br><b>Dedicata</b>: una scheda a parte con la sua memoria (<b>VRAM</b>, per esempio 8 GB), serve per i giochi pesanti.<br>Più la risoluzione è alta (4K) e più gli FPS che vuoi, più la scheda video deve essere potente.</div>

#### 9. Quanto pesano immagini e film · حجم الصور والأفلام · 图片和电影有多大

<div class="scheda">Un'immagine è fatta di <b>pixel</b>; ogni pixel ha un colore di <b>3 byte</b> (rosso, verde, blu). Una foto Full HD: 1920 × 1080 pixel × 3 byte ≈ <b>6 MB</b> senza compressione. Il formato <b>JPG</b> la comprime a circa 0,5-1 MB.<br>Un <b>film</b> è un'immagine ripetuta 24-30 volte al secondo: 2 ore senza compressione sarebbero più di 1000 GB! Grazie alla compressione (MP4) diventa circa 2 GB. Per questo lo streaming funziona anche con pochi Mbps.</div>

#### 10. Il cavo video e la banda · كابل الفيديو · 视频线

<div class="scheda">Il PC si collega al monitor con un cavo video: <b>VGA</b> (vecchio, analogico, connettore blu a 15 piedini, immagine meno nitida), <b>DVI</b> (digitale, bianco), <b>HDMI</b> (digitale, porta anche l'audio, il più diffuso), <b>DisplayPort</b> (digitale, per i monitor da gaming). Dalla scheda video al monitor passano tantissimi dati. Il conto: <b>pixel × 3 byte di colore × Hz</b>. Full HD a 60 Hz: 1920 × 1080 × 24 bit × 60 ≈ <b>3 Gbit al secondo</b>.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cavo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Banda massima (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 1.4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">10 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 2.0</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">18 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DisplayPort 1.4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">32 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 2.1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">48 Gbit/s</td></tr></table>Per un monitor 4K a 144 Hz serve un cavo nuovo. <a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>, parte 3: calcola la banda del tuo monitor ideale.</div>

#### 11. Il mio setup da gamer · إعدادي · 我的游戏设备

<div class="scheda">Ultima prova: scegli il tuo <b>gioco preferito</b> e il setup giusto per giocarlo: cavo o Wi-Fi, quanti Hz, che monitor, che scheda video, che cavo video. Lo scrivi nella verifica con le tue parole e i tuoi numeri.</div>


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
