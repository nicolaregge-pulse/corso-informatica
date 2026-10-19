// 1INF · Tecnologia: quanto pesa un file e quanto va veloce la rete (20/10/2026). Bit, byte, KB, MB, GB;
// la velocità in Mbps e la differenza tra b piccola (bit) e B grande (byte). Dopo il binario e il montaggio del PC.
// Frasi da quinta elementare, conti con numeri tondi. Italiano + una riga in arabo e in cinese sotto titoli e schede.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function L(it, ar, zh) { return it + '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">' + ar + '</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">' + zh + '</span>'; }
  function T(righe) { return '<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0">' + righe.map(function (r, i) { return '<tr>' + r.map(function (c) { return (i ? '<td' : '<th') + ' style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">' + c + (i ? '</td>' : '</th>'); }).join('') + '</tr>'; }).join('') + '</table>'; }

  window.BANCA = {
    id: "1inf-byte-velocita-v1",
    classe: "1INF",
    titolo: "Quanto pesa un file? Quanto va veloce la rete? · كم يزن الملف؟ · 文件有多大？",
    sotto: "1INF · 20/10/2026 · bit, byte, KB, MB, GB · velocità, streaming, Wi-Fi e cavi · ripasso, test e recupero",
    stato: "stato/1inf-byte-velocita.json",
    risultati: "risultati.html?b=1inf-byte-velocita",
    minuti: 20,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Bit, byte e unità di misura", peso: 50 },
      conti: { nome: "I conti con i tuoi numeri", peso: 30 },
      spiega: { nome: "Saperlo spiegare (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- 1. RIPASSO ---------- */
    schede_temi: { bit: 1, byte: 2, unita: 3, pesi: 4, conti: 5, velocita: 6, bB: 7, scaricare: 8, streaming: 9, wifi: 10, cavi: 11 },
    schede: [
      { titolo: L("1. Il bit: 0 oppure 1", "١. البِت: صفر أو واحد", "1. 比特：0 或 1"), testo: L(
        "Il computer capisce solo <b>due cose</b>: corrente <b>sì</b> o corrente <b>no</b>, come una lampadina accesa o spenta. Le scriviamo <b>1</b> e <b>0</b>.<br>Un solo 0 o 1 si chiama <b>bit</b>. È il pezzo più piccolo di informazione. Lo avete già visto con il <b>binario</b>: 1010 sono 4 bit.",
        "الحاسوب يفهم شيئين فقط: 1 أو 0، مثل مصباح مضاء أو مطفأ. الرقم الواحد اسمه «بِت».",
        "电脑只懂两种状态：1 或 0，就像灯开或关。一个 0 或 1 叫做“比特”（bit）。") },
      { titolo: L("2. Il byte: 8 bit insieme", "٢. البايت: ٨ بِت معًا", "2. 字节：8 个比特"), testo: L(
        "Un bit da solo dice poco. <b>8 bit insieme</b> fanno un <b>byte</b>. Con un byte il computer scrive <b>una lettera</b>: la A è 01000001.<br>Quindi: <b>1 byte = 8 bit = una lettera</b>.<br>Il bit si scrive con la <b>b piccola</b>, il byte con la <b>B grande</b>. Ricordatelo: serve dopo, per la velocità.",
        "٨ بِت = ١ بايت = حرف واحد. البِت يُكتب b صغيرة، والبايت B كبيرة.",
        "8 个比特 = 1 个字节 = 一个字母。比特写小写 b，字节写大写 B。") },
      { titolo: L("3. Le unità: KB, MB, GB, TB", "٣. الوحدات: KB، MB، GB، TB", "3. 单位：KB、MB、GB、TB"), testo: L(
        "I file sono fatti di tantissimi byte. Per non scrivere numeri lunghi usiamo i <b>multipli</b>, ogni gradino è <b>circa 1000 volte</b> più grande:" +
        T([["Nome", "Si scrive", "Quanto è"], ["kilobyte", "KB", "1000 byte"], ["megabyte", "MB", "1000 KB"], ["gigabyte", "GB", "1000 MB"], ["terabyte", "TB", "1000 GB"]]) +
        "Come i metri: 1000 metri = 1 chilometro. (Il computer, per essere precisi, usa 1024 invece di 1000: per i nostri conti va bene 1000.)",
        "كل درجة أكبر بنحو ١٠٠٠ مرة: ١٠٠٠ بايت = KB، ١٠٠٠ KB = MB، ١٠٠٠ MB = GB.",
        "每一级大约大 1000 倍：1000 字节 = 1 KB，1000 KB = 1 MB，1000 MB = 1 GB。") },
      { titolo: L("4. Quanto pesa?", "٤. كم يزن؟", "4. 有多大？"), testo: L(
        "Numeri tondi da ricordare:" +
        T([["Che cosa", "Quanto pesa (circa)"], ["un messaggio di testo", "1 KB"], ["una foto del telefono", "3 MB"], ["una canzone", "4 MB"], ["un video di 1 minuto", "100 MB"], ["un film", "2 GB"], ["la memoria di un telefono", "128 GB"], ["il disco del PC che avete montato", "500 GB o 1 TB"]]) +
        "La <b>RAM</b> si misura nello stesso modo: 8 GB, 16 GB.",
        "صورة ≈ ٣ MB، أغنية ≈ ٤ MB، فيلم ≈ ٢ GB، ذاكرة الهاتف ≈ ١٢٨ GB.",
        "一张照片约 3 MB，一首歌约 4 MB，一部电影约 2 GB，手机存储约 128 GB。") },
      { titolo: L("5. Il conto: quante foto ci stanno?", "٥. الحساب: كم صورة تتسع؟", "5. 计算：能放多少张照片？"), testo: L(
        "Il telefono ha <b>64 GB</b> liberi. Quante foto da 3 MB ci stanno?<br>1) Porto tutto in MB: 64 GB = 64 × 1000 = <b>64000 MB</b>.<br>2) Divido per il peso di una foto: 64000 : 3 = circa <b>21000 foto</b>.<br>Regola: <b>prima porto tutto nella stessa unità, poi divido</b>.",
        "أولًا نحوّل كل شيء إلى نفس الوحدة، ثم نقسم: ٦٤ GB = ٦٤٠٠٠ MB، ٦٤٠٠٠ ÷ ٣ ≈ ٢١٠٠٠ صورة.",
        "先换成同一个单位，再做除法：64 GB = 64000 MB，64000 ÷ 3 ≈ 21000 张照片。") },
      { titolo: L("6. La velocità della rete: bit al secondo", "٦. سرعة الشبكة: بِت في الثانية", "6. 网速：每秒多少比特"), testo: L(
        "La velocità di Internet si misura in <b>bit al secondo</b>. Si usa il <b>Mbps</b> = megabit al secondo (milioni di bit ogni secondo)." +
        T([["Connessione", "Velocità (circa)"], ["ADSL vecchia", "10 Mbps"], ["4G del telefono", "30 Mbps"], ["5G", "300 Mbps"], ["fibra", "1000 Mbps = 1 Gbps"]]) +
        "Più Mbps = scarichi più in fretta, i video non si bloccano, il gioco online non va a scatti.",
        "سرعة الإنترنت تُقاس بالبِت في الثانية: Mbps = ميغابِت في الثانية. الألياف ≈ ١٠٠٠ Mbps.",
        "网速用“每秒比特”来量：Mbps = 每秒兆比特。光纤约 1000 Mbps。") },
      { titolo: L("7. Attenzione: b piccola e B grande", "٧. انتبه: b صغيرة و B كبيرة", "7. 注意：小写 b 和大写 B"), testo: L(
        "La rete si misura in <b>Mb</b> (megabit, b piccola). I file si misurano in <b>MB</b> (megabyte, B grande).<br>Siccome 1 byte = 8 bit, per passare dalla velocità della rete ai MB al secondo <b>divido per 8</b>:<br>100 Mbps : 8 = <b>12,5 MB al secondo</b>.<br>Per questo, con una linea da 100 «mega», il download non va a 100 MB al secondo ma a circa 12.",
        "الشبكة بالميغابِت (b صغيرة) والملفات بالميغابايت (B كبيرة). نقسم على ٨: ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB في الثانية.",
        "网速用兆比特（小写 b），文件用兆字节（大写 B）。除以 8：100 Mbps ÷ 8 = 每秒 12.5 MB。") },
      { titolo: L("8. Quanto ci metto a scaricare?", "٨. كم أحتاج من الوقت للتنزيل؟", "8. 下载需要多长时间？"), testo: L(
        "Voglio scaricare un film da <b>2 GB</b> con una linea da <b>100 Mbps</b>.<br>1) Il film in MB: 2 GB = <b>2000 MB</b>.<br>2) La velocità in MB al secondo: 100 : 8 = <b>12,5 MB/s</b>.<br>3) Divido: 2000 : 12,5 = <b>160 secondi</b>, meno di 3 minuti.<br>Con il 4G a 30 Mbps: 30 : 8 ≈ 4 MB/s → 2000 : 4 = 500 secondi, più di 8 minuti.",
        "فيلم ٢ GB = ٢٠٠٠ MB. سرعة ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB/ث. ٢٠٠٠ ÷ ١٢٫٥ = ١٦٠ ثانية.",
        "电影 2 GB = 2000 MB。100 Mbps ÷ 8 = 每秒 12.5 MB。2000 ÷ 12.5 = 160 秒。") },
      { titolo: L("9. Lo streaming: quanta velocità serve?", "٩. البثّ المباشر: كم سرعة نحتاج؟", "9. 在线播放：需要多快的网速？"), testo: L(
        "<b>Streaming</b> vuol dire guardare o ascoltare <b>mentre scarica</b>, senza salvare il file (YouTube, Netflix, Spotify, le dirette). Servono almeno:" +
        T([["Che cosa", "Velocità minima (circa)"], ["musica", "0,3 Mbps"], ["videochiamata", "2 Mbps"], ["video HD", "5 Mbps"], ["video 4K", "25 Mbps"], ["gioco online", "10 Mbps, ma conta il <b>ping</b>: il tempo di risposta, sotto 50 ms"]]) +
        "Se in casa 3 persone guardano video HD insieme: 3 × 5 = 15 Mbps.",
        "البثّ = نشاهد أثناء التنزيل. فيديو HD ≈ ٥ Mbps، فيديو 4K ≈ ٢٥ Mbps.",
        "在线播放 = 边下载边看。高清视频约 5 Mbps，4K 视频约 25 Mbps。") },
      { titolo: L("10. Wi-Fi o cavo?", "١٠. واي فاي أم كابل؟", "10. 无线还是网线？"), testo: L(
        T([["", "Cavo", "Wi-Fi"], ["Velocità", "alta e sempre uguale", "cala con la distanza e i muri"], ["Stabilità", "ottima, ping basso", "dipende: microonde, tanti dispositivi"], ["Comodità", "devi stare vicino alla presa", "ti muovi dove vuoi"], ["Meglio per", "PC fisso, console, lavoro", "telefono, tablet, portatile"]]) +
        "<b>Tipi di Wi-Fi</b> (il numero più alto è il più nuovo):" +
        T([["Nome", "Anno", "Velocità massima (circa)"], ["Wi-Fi 4", "2009", "600 Mbps"], ["Wi-Fi 5", "2014", "3500 Mbps"], ["Wi-Fi 6 / 6E", "2019-2020", "9600 Mbps"], ["Wi-Fi 7", "2024", "oltre 40000 Mbps"]]) +
        "Due «strade» (bande): <b>2,4 GHz</b> arriva più lontano ma è più lenta; <b>5 GHz</b> è più veloce ma passa peggio i muri. Le velocità massime sono teoriche: a casa sono molto meno.",
        "الكابل أسرع وأكثر ثباتًا، والواي فاي أكثر راحة. الواي فاي ٤ و٥ و٦ و٧: الرقم الأكبر هو الأحدث. ٢٫٤ GHz يصل أبعد، ٥ GHz أسرع.",
        "网线更快更稳定，无线更方便。Wi-Fi 4、5、6、7：数字越大越新。2.4 GHz 传得更远，5 GHz 更快。") },
      { titolo: L("11. I tipi di cavo", "١١. أنواع الكابلات", "11. 网线的种类"), testo: L(
        T([["Cavo", "Com'è", "Velocità (circa)", "Dove si usa"], ["rame <b>Cat 5e</b>", "cavo di rete con la spina <b>RJ45</b>", "1000 Mbps", "casa, scuola"], ["rame <b>Cat 6 / 6A</b>", "come il 5e, più schermato", "fino a 10000 Mbps", "uffici, laboratori"], ["<b>fibra ottica</b>", "un filo di vetro: passa la <b>luce</b>", "migliaia di Mbps, anche chilometri", "dalla centrale a casa, tra palazzi"], ["coassiale", "il cavo dell'antenna TV", "basse", "TV, vecchie reti"]]) +
        "Il cavo di rete di rame arriva al massimo a <b>100 metri</b>; la fibra va molto più lontano e non sente i disturbi elettrici.<br>Nel laboratorio, il cavo che va dal PC alla presa nel muro è un <b>Cat 5e o Cat 6 con RJ45</b>.",
        "كابل النحاس (Cat 5e / Cat 6) بقابس RJ45 حتى ١٠٠ متر. الألياف البصرية تنقل الضوء وتصل إلى مسافات بعيدة جدًا.",
        "铜网线（Cat 5e / Cat 6）用 RJ45 插头，最长 100 米。光纤传输光，可以传很远。") }
    ],
    strumenti: [],
    via: C("nozioni", L("Un bit può valere…", "البِت يمكن أن يكون…", "一个比特可以是……"), ["0 oppure 1", "da 0 a 9", "una lettera"], "Acceso o spento."),
    prepara: [
      { q: L("Guarda il tuo telefono (Impostazioni → Memoria): quanti GB ha in tutto? Scrivi il numero e la marca del telefono. Se non lo sai, scrivi: non lo so.", "كم GB في هاتفك؟", "你的手机有多少 GB？"), min: 2 }
    ],
    allenamento: [
      S(1, C("nozioni", L("Il pezzo più piccolo di informazione è…", "أصغر قطعة معلومات هي…", "最小的信息单位是……"), ["il bit", "il byte", "il GB"], "Un solo 0 o 1.")),
      S(2, C("nozioni", L("1 byte è fatto di…", "البايت الواحد يتكون من…", "1 个字节等于……"), ["8 bit", "10 bit", "1000 bit"], "8 bit = una lettera.")),
      S(3, C("nozioni", L("1 GB è circa…", "١ GB تقريبًا…", "1 GB 大约是……"), ["1000 MB", "10 MB", "8 MB"], "Ogni gradino × 1000.")),
      S(3, C("nozioni", L("Qual è il più grande?", "أيها الأكبر؟", "哪个最大？"), ["1 TB", "1 GB", "1 MB"], "KB, MB, GB, TB.")),
      S(4, C("nozioni", L("Una foto del telefono pesa circa…", "صورة الهاتف تزن تقريبًا…", "一张手机照片大约……"), ["3 MB", "3 GB", "3 KB"], "Numeri tondi della scheda 4.")),
      S(5, C("conti", L("In 30 GB, quante foto da 3 MB ci stanno, circa?", "كم صورة ٣ MB في ٣٠ GB؟", "30 GB 能放多少张 3 MB 的照片？"), ["10000", "10", "90"], "30 GB = 30000 MB; 30000 : 3 = 10000.")),
      S(6, C("nozioni", L("La velocità di Internet si misura in…", "سرعة الإنترنت تُقاس بـ…", "网速的单位是……"), ["Mbps, megabit al secondo", "GB", "chilometri all'ora"], "Bit al secondo.")),
      S(7, C("conti", L("200 Mbps sono quanti MB al secondo?", "٢٠٠ Mbps كم MB في الثانية؟", "200 Mbps 等于每秒多少 MB？"), ["25", "200", "1600"], "Divido per 8.")),
      S(8, C("conti", L("Un file da 100 MB con una velocità di 10 MB al secondo: quanto ci metto?", "ملف ١٠٠ MB بسرعة ١٠ MB/ث: كم ثانية؟", "100 MB 的文件，每秒 10 MB，需要多久？"), ["10 secondi", "1000 secondi", "1 secondo"], "100 : 10 = 10.")),
      S(9, C("conti", L("Per un video HD servono circa…", "فيديو HD يحتاج تقريبًا…", "高清视频大约需要……"), ["5 Mbps", "500 Mbps", "0,3 Mbps"], "4K: 25 Mbps.")),
      S(10, C("nozioni", L("Per una console che gioca online è meglio…", "للعب عبر الإنترنت الأفضل…", "在线游戏机最好用……"), ["il cavo: più stabile, ping basso", "il Wi-Fi lontano dal router", "il Bluetooth"], "Il cavo non cala con i muri.")),
      S(10, C("nozioni", L("La banda Wi-Fi che arriva più lontano è…", "نطاق الواي فاي الذي يصل أبعد…", "传得更远的频段是……"), ["2,4 GHz", "5 GHz", "sono uguali"], "5 GHz è più veloce ma passa peggio i muri.")),
      S(11, C("nozioni", L("La spina del cavo di rete si chiama…", "قابس كابل الشبكة اسمه…", "网线插头叫……"), ["RJ45", "USB", "HDMI"], "Cat 5e o Cat 6 con RJ45."))
    ],

    /* ---------- 3. VERIFICA ---------- */
    crocette: [
      C("nozioni", L("Il bit vale…", "البِت قيمته…", "比特的值是……"), ["0 oppure 1", "da 1 a 10", "una parola"], "", "bit"),
      C("nozioni", L("8 bit fanno…", "٨ بِت تساوي…", "8 个比特等于……"), ["1 byte", "1 KB", "1 GB"], "", "byte"),
      C("nozioni", L("Una lettera, nel computer, occupa…", "الحرف الواحد يأخذ…", "一个字母占……"), ["1 byte", "1 GB", "1 bit"], "", "byte"),
      C("nozioni", L("1000 KB fanno circa…", "١٠٠٠ KB تساوي تقريبًا…", "1000 KB 大约是……"), ["1 MB", "1 GB", "1 TB"], "", "unita"),
      C("nozioni", L("In ordine dal più piccolo al più grande:", "من الأصغر إلى الأكبر:", "从小到大："), ["KB, MB, GB, TB", "GB, KB, TB, MB", "MB, KB, GB, TB"], "", "unita"),
      C("nozioni", L("Un film pesa circa…", "الفيلم يزن تقريبًا…", "一部电影大约……"), ["2 GB", "2 KB", "2 TB"], "", "pesi"),
      C("conti", L("Una chiavetta da 8 GB: quante canzoni da 4 MB ci stanno, circa?", "ذاكرة ٨ GB: كم أغنية ٤ MB؟", "8 GB 的 U 盘能放多少首 4 MB 的歌？"), ["2000", "32", "200000"], "", "conti"),
      C("nozioni", L("Mbps vuol dire…", "Mbps تعني…", "Mbps 的意思是……"), ["megabit al secondo", "megabyte al secondo", "mega per sempre"], "", "velocita"),
      C("nozioni", L("La b piccola indica…", "حرف b الصغير يعني…", "小写 b 表示……"), ["il bit", "il byte", "il gigabyte"], "", "bB"),
      C("conti", L("Una linea da 80 Mbps scarica circa quanti MB al secondo?", "خط ٨٠ Mbps كم MB في الثانية؟", "80 Mbps 每秒下载多少 MB？"), ["10", "80", "640"], "", "bB"),
      C("conti", L("Un file da 500 MB a 50 MB al secondo: quanti secondi?", "ملف ٥٠٠ MB بسرعة ٥٠ MB/ث: كم ثانية؟", "500 MB，每秒 50 MB，几秒？"), ["10", "25000", "550"], "", "scaricare"),
      C("nozioni", L("La connessione più veloce tra queste è…", "أسرع اتصال هو…", "下面哪个最快？"), ["la fibra", "l'ADSL vecchia", "il 4G"], "", "velocita"),
      C("conti", L("In casa 4 persone guardano video HD insieme (5 Mbps ciascuno). Servono almeno…", "٤ أشخاص يشاهدون فيديو HD معًا. نحتاج على الأقل…", "4 个人同时看高清视频，至少需要……"), ["20 Mbps", "5 Mbps", "4 Mbps"], "", "streaming"),
      C("nozioni", L("La fibra ottica trasporta…", "الألياف البصرية تنقل…", "光纤传输……"), ["la luce", "l'acqua", "il suono"], "", "cavi"),
      C("nozioni", L("Il cavo di rete di rame arriva al massimo a circa…", "كابل النحاس يصل إلى حوالي…", "铜网线最长约……"), ["100 metri", "10 chilometri", "1 metro"], "", "cavi"),
      C("nozioni", L("Tra Wi-Fi 4 e Wi-Fi 6, il più nuovo e veloce è…", "بين واي فاي ٤ و٦، الأحدث هو…", "Wi-Fi 4 和 Wi-Fi 6 哪个更新更快？"), ["Wi-Fi 6", "Wi-Fi 4", "sono uguali"], "", "wifi"),
      C("nozioni", L("Streaming vuol dire…", "البثّ يعني…", "在线播放的意思是……"), ["guardare o ascoltare mentre si scarica, senza salvare il file", "spegnere il Wi-Fi", "comprare un film"], "", "streaming")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti sicuro, adesso, con KB, MB e GB?", "ما مدى ثقتك الآن؟", "你现在有多大把握？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "conti", tema: "conti", q: L("IL TUO TELEFONO. Prendi i GB del tuo telefono (quelli che hai scritto all'inizio). Quante foto da 3 MB ci stanno? Scrivi i passaggi: prima porti in MB, poi dividi.", "خذ عدد GB في هاتفك: كم صورة ٣ MB تتسع؟ اكتب الخطوات.", "用你手机的 GB 数：能放多少张 3 MB 的照片？写出步骤。"), aiuto: "Se non sai i GB del tuo telefono, usa 64 GB. Scrivi i numeri e le parole, anche poche.", min_parole: 8,
        criteri: "GB × 1000 = MB; MB : 3 = numero di foto; i conti con il suo numero" },
      { area: "conti", tema: "scaricare", q: L("Vuoi scaricare un gioco da 4 GB. A casa hai 40 Mbps. Quanto ci metti? Scrivi i passaggi.", "تريد تنزيل لعبة ٤ GB بسرعة ٤٠ Mbps. كم تحتاج من الوقت؟ اكتب الخطوات.", "下载 4 GB 的游戏，网速 40 Mbps，要多久？写出步骤。"), aiuto: "Tre passi: il gioco in MB, la velocità in MB al secondo (dividi per 8), poi dividi.", min_parole: 8,
        criteri: "4000 MB; 40 : 8 = 5 MB/s; 4000 : 5 = 800 secondi, circa 13 minuti" },
      { area: "spiega", tema: "wifi", q: L("A casa tua: usi il Wi-Fi o il cavo? Per che cosa (video, giochi, compiti)? Secondo te, per il tuo uso, è meglio il Wi-Fi o il cavo, e perché?", "في بيتك: واي فاي أم كابل؟ لماذا؟", "在家你用无线还是网线？为什么？"), aiuto: "Almeno 15 parole. Puoi scrivere anche nella tua lingua.", min_parole: 15,
        criteri: "uso reale; scelta motivata con velocità, stabilità, comodità" },
      { area: "spiega", tema: "bB", q: L("Spiega con parole tue la differenza tra Mb (b piccola) e MB (B grande). Perché con una linea da 100 «mega» non scarico 100 MB al secondo?", "اشرح الفرق بين Mb و MB بكلماتك.", "用自己的话解释 Mb 和 MB 的区别。"), aiuto: "Almeno 15 parole. Puoi scrivere anche nella tua lingua.", min_parole: 15,
        criteri: "Mb = megabit, MB = megabyte; 1 byte = 8 bit; si divide per 8" }
    ],

    /* ---------- 4. RECUPERO ---------- */
    recupero: [
      C("nozioni", L("Il bit può essere…", "البِت يمكن أن يكون…", "比特可以是……"), ["0 o 1", "A o B", "1 o 2"], "", "bit"),
      C("nozioni", L("1 byte = ?", "١ بايت = ؟", "1 字节 = ？"), ["8 bit", "2 bit", "100 bit"], "", "byte"),
      C("nozioni", L("1 GB è più grande di 1 MB?", "هل ١ GB أكبر من ١ MB؟", "1 GB 比 1 MB 大吗？"), ["sì, circa 1000 volte", "no, è più piccolo", "sono uguali"], "", "unita"),
      C("nozioni", L("Le canzoni si misurano di solito in…", "الأغاني تُقاس عادة بـ…", "歌曲通常用……来量"), ["MB", "TB", "bit"], "", "pesi"),
      C("nozioni", L("La velocità della rete si misura in…", "سرعة الشبكة تُقاس بـ…", "网速的单位是……"), ["Mbps", "GB", "chili"], "", "velocita"),
      C("conti", L("16 Mbps sono quanti MB al secondo?", "١٦ Mbps كم MB في الثانية؟", "16 Mbps 等于每秒多少 MB？"), ["2", "16", "128"], "", "bB"),
      C("conti", L("In 6 GB, quante foto da 3 MB, circa?", "كم صورة ٣ MB في ٦ GB؟", "6 GB 能放多少张 3 MB 的照片？"), ["2000", "2", "18"], "", "conti")
    ]
  };
})();
