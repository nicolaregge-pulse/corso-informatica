// 1INF · Tecnologia: la scheda video e i cavi video (27/10/2026, 1 ora, 13-14). Seguito del laboratorio del gamer (21/10):
// là FPS, Hz, monitor e VGA/HDMI di base; qui più a fondo: GPU integrata e dedicata, VRAM, corrente, uscite riconosciute a vista,
// VGA, DVI, HDMI, DisplayPort, USB-C, adattatori, il cavo giusto. Frasi da quinta elementare, numeri tondi.
// Italiano + una riga in arabo e in cinese sotto titoli e schede. Il quiz finale su Moduli è a parte (ripasso + cose nuove).
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function L(it, ar, zh) { return it + '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">' + ar + '</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">' + zh + '</span>'; }
  function T(righe) { return '<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0">' + righe.map(function (r, i) { return '<tr>' + r.map(function (c) { return (i ? '<td' : '<th') + ' style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">' + c + (i ? '</td>' : '</th>'); }).join('') + '</tr>'; }).join('') + '</table>'; }

  window.BANCA = {
    id: "1inf-video-cavi-v1",
    classe: "1INF",
    titolo: "La scheda video e i cavi video · بطاقة الرسوميات وكابلات الفيديو · 显卡和视频线",
    sotto: "1INF · 27/10/2026 · GPU integrata e dedicata, VRAM, uscite video, VGA, DVI, HDMI, DisplayPort, USB-C, adattatori · ripasso, test e recupero",
    stato: "stato/1inf-video-cavi.json",
    risultati: "risultati.html?b=1inf-video-cavi",
    minuti: 15,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Scheda video e cavi: le parole giuste", peso: 50 },
      scelta: { nome: "Scegli il cavo giusto", peso: 30 },
      spiega: { nome: "Saperlo spiegare (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO ---------- */
    schede_temi: { gpu: 1, vram: 2, uscite: 3, cavi: 4, adattatori: 5, pratica: 6, spiega: 7 },
    schede: [
      { titolo: "1. La GPU: il cervello delle immagini · ١. معالج الرسوميات: عقل الصور · 1. GPU：图像的大脑", testo: L(
        "Il 21/10 avete visto che gli <b>FPS</b> (immagini al secondo) li prepara la <b>scheda video</b>. Oggi la guardiamo da vicino.<br>Dentro la scheda video c'è la <b>GPU</b>: è il <b>cervello delle immagini</b>. Il processore (CPU) pensa a tutto il resto; la GPU disegna lo schermo, migliaia di pixel insieme.<br>Ci sono due tipi:" +
        T([["", "Integrata", "Dedicata"], ["Dove sta", "dentro il processore", "una scheda a parte, infilata nello <b>slot PCIe</b> della scheda madre"], ["Com'è", "non si vede", "grande, con <b>1, 2 o 3 ventole</b>"], ["Potenza", "bassa: scuola, video, Internet", "alta: giochi, montaggio video, 3D"], ["Prezzo", "compresa nel processore", "da 150 a oltre 1000 euro"]]) +
        "I PC del laboratorio di solito hanno la scheda video <b>integrata</b>.",
        "GPU هو عقل الصور. المدمجة داخل المعالج، والمنفصلة بطاقة مستقلة في منفذ PCIe ولها مراوح.",
        "GPU 是图像的大脑。集成显卡在处理器里面；独立显卡是单独的一块卡，插在 PCIe 插槽上，有风扇。") },
      { titolo: "2. La VRAM e la corrente · ٢. ذاكرة الفيديو والكهرباء · 2. 显存和电源", testo: L(
        "La scheda dedicata ha una <b>sua memoria</b>: la <b>VRAM</b> (video RAM). Lì tiene le immagini, i colori e i disegni del gioco. Si misura in <b>GB</b>, come la RAM:" +
        T([["VRAM", "Va bene per"], ["4 GB", "giochi leggeri in Full HD"], ["8 GB", "quasi tutti i giochi in Full HD"], ["12-16 GB", "giochi in 2K e 4K, montaggio video 4K"], ["24 GB", "4K al massimo, grafica 3D, intelligenza artificiale"]]) +
        "La scheda integrata non ha VRAM sua: <b>prende in prestito un pezzo della RAM</b> del PC.<br>La scheda dedicata <b>consuma tanta corrente</b>: da 75 a 450 watt (una lampadina LED ne consuma 10). Per questo ha un cavo che arriva <b>direttamente dall'alimentatore</b>, e serve un alimentatore più forte (600-850 watt). Scalda tanto: per questo ha le ventole.",
        "VRAM هي ذاكرة بطاقة الرسوميات وتُقاس بـ GB (مثلًا ٨ GB). البطاقة المنفصلة تستهلك كهرباء كثيرة (٧٥-٤٥٠ واط) وتحتاج كابلًا من مزوّد الطاقة.",
        "VRAM 是显卡自己的内存，用 GB 来量（比如 8 GB）。独立显卡很耗电（75-450 瓦），需要电源直接接线。") },
      { titolo: "3. Le uscite video: riconoscerle a vista · ٣. منافذ الفيديو: كيف نعرفها بالنظر · 3. 视频接口：一眼认出来", testo: L(
        "Dietro al PC ci sono tante <b>prese</b> (uscite). Quelle per il monitor si riconoscono da <b>forma</b>, <b>colore</b> e <b>piedini</b> (i pin, i contatti di metallo):" +
        T([["Uscita", "Forma", "Colore", "Piedini"], ["<b>VGA</b>", "trapezio con 2 viti", "blu", "15 buchini in 3 file"], ["<b>DVI</b>", "rettangolo lungo con 2 viti", "bianco", "fino a 24 buchini + una crocetta"], ["<b>HDMI</b>", "trapezio piatto, senza viti", "nero", "19 contatti dentro"], ["<b>DisplayPort</b>", "rettangolo con <b>un angolo tagliato</b>", "nero", "20 contatti dentro"], ["<b>USB-C</b>", "piccolo ovale, entra nei due versi", "nero o grigio", "24 contatti dentro"]]) +
        "Attenzione: se il PC ha una scheda <b>dedicata</b>, le sue uscite sono <b>più in basso</b>, in fila orizzontale. Il monitor va attaccato <b>lì</b>, non alle uscite in alto vicino alle USB (quelle sono della scheda integrata).",
        "نعرف المنافذ من الشكل واللون وعدد الدبابيس: VGA أزرق ١٥ ثقبًا، DVI أبيض كبير، HDMI مسطّح، DisplayPort له زاوية مقطوعة، USB-C صغير بيضاوي.",
        "看形状、颜色和针脚就能认出：VGA 蓝色 15 孔，DVI 白色很大，HDMI 扁平，DisplayPort 有一个切角，USB-C 小小的椭圆形。") },
      { titolo: "4. I cavi video a confronto · ٤. مقارنة كابلات الفيديو · 4. 视频线比较", testo: L(
        "Ogni uscita ha il suo cavo. Ecco la tabella da ricordare (numeri tondi):" +
        T([["Cavo", "Com'è", "Audio", "Massimo (circa)", "Dove si trova"], ["<b>VGA</b>", "vecchio, <b>analogico</b>, blu", "no, solo immagine", "Full HD a 60 Hz, meno nitido", "PC e proiettori vecchi"], ["<b>DVI</b>", "digitale, bianco, grande", "di solito no", "2560 × 1600 a 60 Hz", "PC e monitor di 10-15 anni fa"], ["<b>HDMI 1.4</b>", "digitale, il più comune", "sì", "4K a 30 Hz", "TV, PC, proiettori"], ["<b>HDMI 2.0</b>", "uguale fuori", "sì", "4K a 60 Hz", "TV, console, PC"], ["<b>HDMI 2.1</b>", "uguale fuori", "sì", "4K a 120 Hz, 8K a 60 Hz", "console nuove, TV nuove"], ["<b>DisplayPort 1.4</b>", "digitale, angolo tagliato", "sì", "4K a 120 Hz e oltre", "PC e monitor da gioco"], ["<b>USB-C</b>", "piccolo, entra nei due versi", "sì", "di solito 4K a 60 Hz", "telefoni, portatili, tablet"]]) +
        "<b>Analogico</b> = il segnale è un'onda, si rovina un po'. <b>Digitale</b> = il segnale è fatto di 0 e 1, arriva pulito.<br>I cavi HDMI fuori sono tutti uguali: la versione (2.0, 2.1) è scritta sulla confezione o sul cavo.",
        "VGA قديم وتناظري، بدون صوت. HDMI الأكثر انتشارًا، صورة وصوت. DisplayPort لشاشات الألعاب. USB-C للهواتف والحواسيب المحمولة. HDMI 2.0: 4K بـ ٦٠ Hz. HDMI 2.1 و DisplayPort 1.4: 4K بـ ١٢٠ Hz.",
        "VGA 是旧的模拟线，没有声音。HDMI 最常见，有图像和声音。DisplayPort 用于游戏显示器。USB-C 用于手机和笔记本。HDMI 2.0：4K 60 Hz。HDMI 2.1 和 DisplayPort 1.4：4K 120 Hz。") },
      { titolo: "5. Gli adattatori e il cavo giusto · ٥. المحوّلات والكابل المناسب · 5. 转接头和合适的线", testo: L(
        "Se il PC e il monitor hanno prese diverse si usa un <b>adattatore</b> (un pezzo che cambia la forma della spina):" +
        T([["Adattatore", "Funziona?", "Attenzione"], ["HDMI → VGA", "sì", "trasforma il digitale in analogico; l'<b>audio si perde</b>"], ["DVI → HDMI", "sì, facile", "di solito senza audio"], ["DisplayPort → HDMI", "sì, facile", "va bene per i PC con solo DisplayPort"], ["USB-C → HDMI", "sì", "solo se il telefono o il portatile manda il video dalla USB-C"]]) +
        "<b>Il cavo giusto:</b><br>Per una <b>console</b> (PlayStation, Xbox, Switch): sempre <b>HDMI</b>, perché porta immagine e audio alla TV.<br>Per il <b>monitor della scuola</b>: guardi le prese dietro al PC e dietro al monitor e scegli quella <b>uguale e più nuova</b> (meglio HDMI o DisplayPort che VGA).<br>Per un <b>monitor da gioco a 144 Hz</b>: DisplayPort, o HDMI 2.1.",
        "المحوّل يغيّر شكل القابس: HDMI إلى VGA (يضيع الصوت). للكونسول نستعمل دائمًا HDMI. لشاشة المدرسة نختار المنفذ المتشابه والأحدث.",
        "转接头改变插头的形状：HDMI 转 VGA（没有声音）。游戏机永远用 HDMI。学校的显示器：选两边都有的、最新的接口。") },
      { titolo: "6. Prova al banco: che uscite vedi? · ٦. تجربة على الطاولة: ما المنافذ التي تراها؟ · 6. 动手看看：你看到哪些接口？", testo: L(
        "Adesso tocca a te, al tuo posto, senza smontare niente e senza staccare cavi.<br>1) Guarda <b>dietro al PC</b> del laboratorio. Cerca le prese della tabella della scheda 3. Conta: quante VGA? quante HDMI? quante DisplayPort? quante DVI?<br>2) Guarda <b>dietro al monitor</b>. Che prese ha?<br>3) Segui il cavo che va dal PC al monitor: <b>che cavo è</b>? Di che colore è la spina?<br>4) Il PC ha una scheda <b>dedicata</b> (uscite in basso, in fila) o solo <b>integrata</b> (uscite in alto, vicino alle USB)?<br>Scrivi quello che vedi nella casella «Prepara la tua storia» qui sotto: servirà nella verifica.",
        "انظر خلف الحاسوب وخلف الشاشة، بدون فصل أي كابل. عُدّ المنافذ: VGA، HDMI، DisplayPort، DVI. أي كابل يصل الحاسوب بالشاشة؟ اكتب ما تراه.",
        "看看电脑和显示器的背面，不要拔线。数一数：VGA、HDMI、DisplayPort、DVI 各有几个？电脑和显示器用的是哪种线？把你看到的写下来。") },
      { titolo: "7. Spiegalo in 30 secondi · ٧. اشرحه في ٣٠ ثانية · 7. 30 秒讲清楚", testo: L(
        "Girati verso il compagno e digli queste frasi con parole tue. Se le sai dire, hai capito davvero:<br>1) «La <b>GPU</b> è il cervello che disegna le immagini; la VRAM è la sua memoria.»<br>2) «La scheda <b>integrata</b> sta nel processore; quella <b>dedicata</b> è una scheda a parte, con le ventole, per i giochi.»<br>3) «<b>VGA</b> è vecchio e porta solo l'immagine; <b>HDMI</b> porta immagine e audio; <b>DisplayPort</b> è per i monitor da gioco.»<br>4) «Se le prese sono diverse, uso un <b>adattatore</b>.»<br>Poi scambiatevi: adesso spiega lui a te.",
        "قل لزميلك: GPU عقل الصور. المدمجة في المعالج والمنفصلة بطاقة بمراوح. VGA قديم، HDMI صورة وصوت، DisplayPort لشاشات الألعاب.",
        "对同学说：GPU 是图像的大脑。集成显卡在处理器里，独立显卡是带风扇的卡。VGA 很旧，HDMI 有图像和声音，DisplayPort 用于游戏显示器。") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../1inf-oggi/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
    via: C("nozioni", L("La GPU è…", "معالج الرسوميات (GPU) هو…", "GPU 是……"), ["il cervello che disegna le immagini", "la memoria del telefono", "il cavo del monitor"], "Graphics Processing Unit: disegna lo schermo."),
    /* 26/10: «prepara» tolto, la prova al banco è nella scheda 6 */
    allenamento: [
      S(1, C("nozioni", L("La scheda video integrata sta…", "بطاقة الرسوميات المدمجة موجودة…", "集成显卡在……"), ["dentro il processore", "in una scheda a parte con le ventole", "dentro il monitor"], "Integrata = dentro la CPU.")),
      S(1, C("nozioni", L("La scheda video dedicata si infila…", "بطاقة الرسوميات المنفصلة تُركَّب…", "独立显卡插在……"), ["nello slot PCIe della scheda madre", "nella presa USB", "nella presa di rete"], "Lo slot lungo PCIe.")),
      S(2, C("nozioni", L("La VRAM è…", "VRAM هي…", "VRAM 是……"), ["la memoria della scheda video", "la velocità del monitor", "un tipo di cavo"], "Video RAM, in GB.")),
      S(2, C("nozioni", L("Perché la scheda dedicata ha un cavo che arriva dall'alimentatore?", "لماذا تحتاج البطاقة المنفصلة كابلًا من مزوّد الطاقة؟", "为什么独立显卡要接电源线？"), ["perché consuma tanta corrente", "per portare Internet", "per l'audio"], "Da 75 a 450 watt.")),
      S(3, C("nozioni", L("La presa con un angolo tagliato è…", "المنفذ ذو الزاوية المقطوعة هو…", "有一个切角的接口是……"), ["DisplayPort", "VGA", "DVI"], "Un solo angolo storto.")),
      S(3, C("nozioni", L("La presa bianca, grande, con tanti buchini e due viti è…", "المنفذ الأبيض الكبير بثقوب كثيرة وبرغيين هو…", "白色、很大、很多孔、两个螺丝的接口是……"), ["DVI", "HDMI", "USB-C"], "Bianco e grande: DVI.")),
      S(4, C("nozioni", L("Quale cavo porta solo l'immagine, senza audio?", "أي كابل ينقل الصورة فقط بدون صوت؟", "哪种线只传图像，没有声音？"), ["VGA", "HDMI", "DisplayPort"], "VGA: vecchio, analogico.")),
      S(4, C("scelta", L("HDMI 2.0 arriva al massimo a…", "HDMI 2.0 يصل إلى…", "HDMI 2.0 最高是……"), ["4K a 60 Hz", "4K a 240 Hz", "Full HD a 30 Hz"], "Per 4K a 120 Hz serve HDMI 2.1 o DisplayPort 1.4.")),
      S(5, C("scelta", L("Il PC ha solo HDMI, il vecchio proiettore solo VGA. Che cosa serve?", "الحاسوب فيه HDMI فقط والجهاز القديم VGA فقط. ماذا نحتاج؟", "电脑只有 HDMI，旧投影仪只有 VGA。需要什么？"), ["un adattatore HDMI → VGA", "un cavo di rete", "niente, si collegano da soli"], "L'audio però si perde.")),
      S(5, C("scelta", L("Per collegare una console alla TV si usa…", "لتوصيل جهاز الألعاب بالتلفاز نستعمل…", "游戏机接电视用……"), ["HDMI", "VGA", "DVI"], "Immagine e audio in un cavo solo."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("nozioni", L("La GPU serve a…", "GPU يُستعمل لـ…", "GPU 用来……"), ["disegnare le immagini sullo schermo", "salvare i file", "collegarsi al Wi-Fi"], "", "gpu"),
      C("nozioni", L("Una scheda video con 2 o 3 ventole è di solito…", "بطاقة رسوميات بمروحتين أو ثلاث هي عادة…", "有 2 或 3 个风扇的显卡通常是……"), ["dedicata", "integrata", "una scheda di rete"], "", "gpu"),
      C("nozioni", L("La scheda integrata, per le immagini, usa…", "البطاقة المدمجة تستعمل للصور…", "集成显卡用什么存图像？"), ["un pezzo della RAM del PC", "8 GB di VRAM sua", "la memoria del monitor"], "", "vram"),
      C("nozioni", L("Per montare video in 4K è meglio una scheda con…", "لمونتاج فيديو 4K الأفضل بطاقة بـ…", "剪辑 4K 视频最好用……"), ["tanta VRAM, per esempio 12-16 GB", "1 GB di VRAM", "nessuna VRAM"], "", "vram"),
      C("nozioni", L("La presa blu, a trapezio, con 15 buchini in 3 file è…", "المنفذ الأزرق بـ ١٥ ثقبًا في ٣ صفوف هو…", "蓝色、梯形、3 排 15 个孔的接口是……"), ["VGA", "HDMI", "DisplayPort"], "", "uscite"),
      C("nozioni", L("La presa piccola e ovale che entra nei due versi è…", "المنفذ الصغير البيضاوي الذي يدخل من الجهتين هو…", "小小的椭圆形、两面都能插的接口是……"), ["USB-C", "DVI", "VGA"], "", "uscite"),
      C("nozioni", L("Analogico vuol dire…", "تناظري يعني…", "模拟信号的意思是……"), ["il segnale è un'onda e si può rovinare un po'", "il segnale è fatto di 0 e 1", "il cavo è senza fili"], "", "cavi"),
      C("scelta", L("Monitor da gioco 4K a 120 Hz: quale cavo?", "شاشة ألعاب 4K بـ ١٢٠ Hz: أي كابل؟", "4K 120 Hz 游戏显示器：用哪种线？"), ["DisplayPort 1.4 o HDMI 2.1", "VGA", "HDMI 1.4"], "", "cavi"),
      C("scelta", L("Attacchi il PC alla TV con HDMI → VGA. Che cosa si perde?", "توصل الحاسوب بـ HDMI إلى VGA. ماذا يضيع؟", "用 HDMI 转 VGA 接电视，会失去什么？"), ["l'audio", "l'immagine", "la corrente"], "", "adattatori"),
      C("scelta", L("Il PC ha una scheda dedicata. Il monitor va attaccato…", "الحاسوب فيه بطاقة منفصلة. نوصل الشاشة…", "电脑有独立显卡，显示器应该接在……"), ["alle uscite della scheda dedicata, più in basso", "alle uscite in alto vicino alle USB", "alla presa di rete"], "", "uscite")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti sicuro, adesso, a riconoscere i cavi video?", "ما مدى ثقتك الآن في معرفة كابلات الفيديو؟", "你现在有多大把握认出视频线？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "scelta", tema: "adattatori", q: L("IL CAVO GIUSTO. Un amico ha una PlayStation e un monitor da PC con le prese VGA e HDMI. Quale cavo gli consigli e perché? E se il monitor avesse solo VGA?", "صديقك عنده PlayStation وشاشة فيها VGA و HDMI. أي كابل تنصحه به ولماذا؟ وإذا كانت الشاشة VGA فقط؟", "朋友有 PlayStation 和一台有 VGA 和 HDMI 的显示器。你建议用哪种线？为什么？如果显示器只有 VGA 呢？"), aiuto: "Almeno 15 parole. Puoi scrivere anche nella tua lingua.", min_parole: 15,
        criteri: "HDMI perché la console ha solo HDMI e porta immagine e audio; con solo VGA serve un adattatore HDMI → VGA e l'audio si perde" },
      { area: "spiega", tema: "pratica", q: L("IL TUO PC DEL LABORATORIO. Che prese video hai visto dietro al PC e dietro al monitor? Con che cavo sono collegati? La scheda video è integrata o dedicata? Come lo hai capito?", "ما المنافذ التي رأيتها خلف الحاسوب والشاشة؟ بأي كابل هما موصولان؟ البطاقة مدمجة أم منفصلة؟", "你在电脑和显示器背面看到了哪些接口？用什么线连接？显卡是集成的还是独立的？"), aiuto: "Usa quello che hai scritto all'inizio. Almeno 15 parole.", min_parole: 15,
        criteri: "nomina le prese viste (VGA, HDMI, DisplayPort, DVI) con colore o forma; il cavo usato; integrata o dedicata con il motivo (posizione delle uscite, ventole)" }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("nozioni", L("La GPU disegna…", "GPU يرسم…", "GPU 画……"), ["le immagini", "i file di testo", "la rete"], "", "gpu"),
      C("nozioni", L("La VRAM si misura in…", "VRAM تُقاس بـ…", "VRAM 的单位是……"), ["GB", "Hz", "metri"], "", "vram"),
      C("nozioni", L("Il cavo VGA è di colore…", "كابل VGA لونه…", "VGA 线是什么颜色？"), ["blu", "rosso", "verde"], "", "uscite"),
      C("nozioni", L("Il cavo più comune, con immagine e audio, è…", "الكابل الأكثر انتشارًا بالصورة والصوت هو…", "最常见、有图像和声音的线是……"), ["HDMI", "VGA", "DVI"], "", "cavi"),
      C("scelta", L("Il telefono si collega alla TV con…", "الهاتف يتصل بالتلفاز بـ…", "手机接电视用……"), ["USB-C → HDMI", "VGA → DVI", "il cavo di rete"], "", "adattatori"),
      C("scelta", L("Per un monitor da gioco a 144 Hz è meglio…", "لشاشة ألعاب ١٤٤ Hz الأفضل…", "144 Hz 游戏显示器最好用……"), ["DisplayPort", "VGA", "DVI"], "", "cavi")
    ]
  };
})();
