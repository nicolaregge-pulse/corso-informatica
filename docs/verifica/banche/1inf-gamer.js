// 1INF · Il laboratorio del gamer (21/10/2026): ping, jitter, lag, FPS, Hz, monitor, schede video, banda dei cavi.
// Seguito della lezione del 20/10 (bit, byte, velocità della rete). Prove dal vivo nella pagina ../1inf-gamer/.
// Italiano semplice + titoli in arabo e cinese.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function T(righe) { return '<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0">' + righe.map(function (r, i) { return '<tr>' + r.map(function (c) { return (i ? '<td' : '<th') + ' style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">' + c + (i ? '</td>' : '</th>'); }).join('') + '</tr>'; }).join('') + '</table>'; }
  var LAB = '<a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>';

  window.BANCA = {
    id: "1inf-gamer-v1",
    classe: "1INF",
    titolo: "Il laboratorio del gamer · مختبر اللاعب · 玩家实验室",
    sotto: "1INF · 21/10/2026 · ping, jitter, lag, FPS, Hz, monitor, schede video, cavi",
    stato: "stato/1inf-gamer.json",
    risultati: "risultati.html?b=1inf-gamer",
    minuti: 20,
    anteprima: "868848605",
    ripasso_n: 1,
    aree: {
      nozioni: { nome: "Rete e video: le parole del gamer", peso: 50 },
      prove: { nome: "Le tue prove nel laboratorio", peso: 30 },
      spiega: { nome: "Saperlo spiegare (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: { ripasso: 1, ping: 2, jitter: 3, lag: 4, fps: 5, hz: 6, monitor: 7, scheda: 8, cavi: 9, setup: 10 },
    schede: [
      { titolo: "1. Ripasso: Mbps e MB · مراجعة · 复习", testo: "La rete si misura in <b>Mbps</b> (megabit al secondo). 1 byte = 8 bit, quindi 100 Mbps = 12,5 MB al secondo. Per i giochi però la velocità non basta: conta anche <b>quanto in fretta</b> arriva la risposta." },
      { titolo: "2. Il ping · البينغ · 延迟(ping)", testo: "Il <b>ping</b> è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in <b>millisecondi (ms)</b>: 1000 ms = 1 secondo." + T([["Ping", "Come si gioca"], ["sotto 30 ms", "ottimo"], ["30-60 ms", "buono"], ["60-100 ms", "si sente un po'"], ["oltre 150 ms", "lag: i colpi arrivano in ritardo"]]) + "Il ping dipende soprattutto dalla <b>distanza</b> dal server, non dai Mbps. " + LAB + ": prova il gioco dei bersagli con ping 20 e con ping 200." },
      { titolo: "3. Il jitter · التذبذب · 抖动", testo: "Il <b>jitter</b> è quanto il ping <b>cambia</b> da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping." },
      { titolo: "4. Lag, scatti e pacchetti persi · التأخير والتقطع · 卡顿和丢包", testo: T([["Parola", "Che cosa vuol dire", "Da dove viene"], ["<b>lag</b>", "il gioco risponde in ritardo", "ping alto"], ["<b>scatti</b> di rete", "movimenti a salti", "jitter alto"], ["<b>pacchetti persi</b> (packet loss)", "pezzi di informazione che non arrivano", "Wi-Fi debole, rete piena"], ["<b>scatti</b> del PC (FPS bassi)", "l'immagine va a scatti anche offline", "scheda video troppo lenta"]]) + "Il cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo." },
      { titolo: "5. Gli FPS · الإطارات في الثانية · 帧率(FPS)", testo: "Un video o un gioco è fatto di tante <b>immagini ferme</b> mostrate una dopo l'altra. <b>FPS</b> = frame per second, immagini al secondo." + T([["FPS", "Come appare"], ["15", "a scatti"], ["30", "accettabile, film e console vecchie"], ["60", "fluido"], ["144 e più", "molto fluido, giochi veloci"]]) + "Gli FPS li produce la <b>scheda video</b>. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS." },
      { titolo: "6. Gli Hz del monitor · الهرتز · 刷新率(Hz)", testo: "Gli <b>Hz</b> (hertz) dicono quante volte al secondo il <b>monitor</b> ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.<br>Regola: <b>FPS della scheda video e Hz del monitor devono andare d'accordo</b>. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando." },
      { titolo: "7. I tipi di monitor · أنواع الشاشات · 显示器类型", testo: T([["Tipo", "Pregio", "Difetto"], ["<b>TN</b>", "velocissimo, economico", "colori spenti, angolo di visione stretto"], ["<b>IPS</b>", "colori belli, si vede bene di lato", "un po' più lento"], ["<b>VA</b>", "neri profondi, buon contrasto", "a volte scie nelle scene veloci"], ["<b>OLED</b>", "neri perfetti, velocissimo", "costoso"]]) + "Il <b>tempo di risposta</b> (1-5 ms) dice quanto in fretta un pixel cambia colore: più basso, meno scie." },
      { titolo: "8. La scheda video · بطاقة الرسوميات · 显卡", testo: "La <b>scheda video</b> (GPU) disegna le immagini del gioco.<br><b>Integrata</b>: dentro il processore, consuma poco, va bene per scuola e video.<br><b>Dedicata</b>: una scheda a parte con la sua memoria (<b>VRAM</b>, per esempio 8 GB), serve per i giochi pesanti.<br>Più la risoluzione è alta (4K) e più gli FPS che vuoi, più la scheda video deve essere potente." },
      { titolo: "9. Il cavo video e la banda · كابل الفيديو · 视频线", testo: "Dalla scheda video al monitor passano tantissimi dati. Il conto: <b>pixel × 3 byte di colore × Hz</b>. Full HD a 60 Hz: 1920 × 1080 × 24 bit × 60 ≈ <b>3 Gbit al secondo</b>." + T([["Cavo", "Banda massima (circa)"], ["HDMI 1.4", "10 Gbit/s"], ["HDMI 2.0", "18 Gbit/s"], ["DisplayPort 1.4", "32 Gbit/s"], ["HDMI 2.1", "48 Gbit/s"]]) + "Per un monitor 4K a 144 Hz serve un cavo nuovo. " + LAB + ", parte 3: calcola la banda del tuo monitor ideale." },
      { titolo: "10. Il mio setup da gamer · إعدادي · 我的游戏设备", testo: "Ultima prova: scegli il tuo <b>gioco preferito</b> e il setup giusto per giocarlo: cavo o Wi-Fi, quanti Hz, che monitor, che scheda video, che cavo video. Lo scrivi nella verifica con le tue parole e i tuoi numeri." }
    ],
    strumenti: [{ t: 'Il laboratorio del gamer (prove dal vivo)', u: '../1inf-gamer/', c: '#d4a017' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
    via: C("nozioni", "Il ping si misura in…", ["millisecondi (ms)", "gigabyte (GB)", "hertz (Hz)"], "1000 ms = 1 secondo."),
    prepara: [{ q: "Qual è il tuo gioco preferito? Su che cosa ci giochi (telefono, console, PC)?", min: 4 }],
    allenamento: [
      S(1, C("nozioni", "100 Mbps sono circa…", ["12,5 MB al secondo", "100 MB al secondo", "800 MB al secondo"], "Si divide per 8.")),
      S(2, C("nozioni", "Il ping è…", ["il tempo di andata e ritorno di un messaggio fino al server", "la velocità di download", "il numero di immagini al secondo"], "Andata e ritorno, in ms.")),
      S(2, C("prove", "Nel laboratorio, con ping 200 rispetto a ping 20, hai colpito…", ["meno bersagli", "più bersagli", "gli stessi"], "Il ritardo ti fa mancare i bersagli che si spostano.")),
      S(3, C("nozioni", "Il jitter è…", ["quanto il ping cambia da un momento all'altro", "il ping sempre uguale", "la luminosità del monitor"], "Ping che salta = jitter alto.")),
      S(4, C("nozioni", "Per giocare online è meglio…", ["il cavo: ping e jitter più bassi", "il Wi-Fi lontano dal router", "spegnere il router"], "Il cavo è più stabile.")),
      S(5, C("nozioni", "FPS vuol dire…", ["immagini al secondo", "file per secondo", "velocità del mouse"], "Frame per second.")),
      S(6, C("nozioni", "Monitor da 60 Hz, scheda video a 200 FPS: quante immagini vedi al secondo?", ["60", "200", "260"], "Il monitor ne mostra al massimo quanti sono i suoi Hz.")),
      S(7, C("nozioni", "Il monitor con i neri perfetti ma costoso è…", ["OLED", "TN", "VA"], "OLED.")),
      S(8, C("nozioni", "La memoria della scheda video si chiama…", ["VRAM", "ROM", "SSD"], "Video RAM.")),
      S(9, C("nozioni", "Per un monitor 4K a 144 Hz serve…", ["un cavo con tanta banda, come HDMI 2.1", "un cavo qualsiasi", "il Wi-Fi"], "Tanti pixel e tanti Hz = tanti dati."))
    ],
    crocette: [
      C("nozioni", "Ping 25 ms: com'è?", ["ottimo", "lag forte", "il gioco non parte"], "", "ping"),
      C("nozioni", "Il ping dipende soprattutto…", ["dalla distanza dal server", "dalla grandezza del monitor", "dal colore del PC"], "", "ping"),
      C("nozioni", "Il personaggio salta e si teletrasporta: il problema più probabile è…", ["jitter alto o pacchetti persi", "monitor IPS", "troppa VRAM"], "", "jitter"),
      C("nozioni", "Il gioco va a scatti anche senza Internet: colpa…", ["della scheda video (FPS bassi)", "del ping", "del router"], "", "lag"),
      C("nozioni", "Un film al cinema ha circa…", ["24-30 FPS", "500 FPS", "1 FPS"], "", "fps"),
      C("nozioni", "Hz del monitor =", ["quante volte al secondo il monitor ridisegna l'immagine", "la grandezza dello schermo", "la velocità della rete"], "", "hz"),
      C("nozioni", "Per giochi veloci il monitor ideale ha…", ["144 Hz o più", "30 Hz", "1 Hz"], "", "hz"),
      C("nozioni", "Il monitor con i colori più belli visti anche di lato, tra TN e IPS, è…", ["IPS", "TN", "sono uguali"], "", "monitor"),
      C("nozioni", "Una scheda video integrata…", ["sta dentro il processore", "ha sempre 24 GB di VRAM", "si collega con il Wi-Fi"], "", "scheda"),
      C("nozioni", "Full HD a 60 Hz ha bisogno di circa…", ["3 Gbit/s", "3 Mbit/s", "300 Gbit/s"], "", "cavi"),
      C("nozioni", "Tra questi cavi, quello con più banda è…", ["HDMI 2.1", "HDMI 1.4", "HDMI 2.0"], "", "cavi"),
      C("nozioni", "Tempo di risposta del monitor 1 ms rispetto a 5 ms…", ["meno scie nelle scene veloci", "più scie", "nessuna differenza"], "", "monitor")
    ],
    scale: [{ area: "parere", q: "Quanto ti è piaciuto il laboratorio del gamer?", basso: "per niente", alto: "moltissimo", ultima: true }],
    aperte: [
      { area: "prove", tema: "ping", q: "LE TUE PROVE. Nel laboratorio: quanti bersagli hai colpito con ping 20 e quanti con ping 200? E con jitter 150? Che differenza hai sentito?", aiuto: "Scrivi i tuoi numeri e una frase. Almeno 12 parole.", min_parole: 12, criteri: "numeri veri delle prove; meno punti con ping e jitter alti; spiegazione" },
      { area: "spiega", tema: "setup", q: "IL MIO SETUP DA GAMER. Il tuo gioco preferito: con che connessione (cavo o Wi-Fi), quanti Hz, che tipo di monitor, che scheda video e che cavo video ci giocheresti? Spiega perché.", aiuto: "Almeno 25 parole. Puoi scrivere anche nella tua lingua.", min_parole: 25, criteri: "scelte coerenti col gioco; usa ping, Hz/FPS, monitor, scheda video, cavo" },
      { area: "spiega", tema: "hz", q: "Spiega con parole tue la differenza tra FPS e Hz.", aiuto: "Almeno 15 parole.", min_parole: 15, criteri: "FPS = immagini prodotte dalla scheda video; Hz = immagini mostrate dal monitor; si vede il minimo tra i due" }
    ],
    recupero: [
      C("nozioni", "Il ping si misura in…", ["ms", "GB", "Hz"], "", "ping"),
      C("nozioni", "Ping alto vuol dire…", ["lag", "immagine più bella", "più memoria"], "", "ping"),
      C("nozioni", "FPS =", ["immagini al secondo", "byte al secondo", "giocatori al secondo"], "", "fps"),
      C("nozioni", "Gli Hz sono del…", ["monitor", "mouse", "router"], "", "hz"),
      C("nozioni", "Per giocare online è meglio…", ["il cavo", "il Wi-Fi in un'altra stanza", "il Bluetooth"], "", "lag"),
      C("nozioni", "La VRAM è la memoria…", ["della scheda video", "del telefono", "del router"], "", "scheda")
    ]
  };
})();
