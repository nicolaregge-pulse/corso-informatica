# -*- coding: utf-8 -*-
"""Dati delle dispense riepilogative (12/11/2026): tutto lo svolto finora e i lavori assegnati, per classe.

Versione 1.0. PUBBLICO: nessun cognome, nessun voto, nessuna presenza. Fonti: ARGOMENTI-SVOLTI-2026-27.md (v1.6),
FIRME-REGISTRO-2026-27.md (v2.7), PROVE-CLASSROOM-2026-27.md, fabbrica/indice.json e i titoli dei quiz in fabbrica/*.txt,
PROSSIME-LEZIONI.md. I titoli dei compiti Classroom del 1INF vengono dall'elenco di Fabbrica delle 13:19 del 12/11 (titoli
troncati a 28 caratteri: finiscono con «…»). Lingue (R6): 1INF it+ar+zh; 2INF e 4TI solo it; 3INF it (+ bn solo per il PC 14).
Arabo, cinese e bangla sono scritti da Claude e NON riletti da un madrelingua.
Ogni voce: (data, {it, ar, zh, bn}). Frasi corte, una cosa per frase.
"""

DATA = "12 novembre 2026"

# ----------------------------------------------------------------------------------------------- 1INF
UNO = {
    "classe": "1INF",
    "titolo": {"it": "Riepilogo del corso 1INF", "ar": "ملخص دورة 1INF", "zh": "1INF 课程总结"},
    "intro": {
        "it": "Questa pagina racconta tutto quello che abbiamo fatto da settembre a oggi (12 novembre 2026) e i lavori che ti sono stati chiesti. Se ti manca un lavoro, fallo: tutti devono fare tutto.",
        "ar": "تحكي هذه الصفحة كل ما فعلناه من سبتمبر حتى اليوم (12 نوفمبر 2026) والأعمال المطلوبة منك. إذا ينقصك عمل، قم به: الجميع يجب أن يفعل كل شيء.",
        "zh": "这一页讲述从九月到今天（2026年11月12日）我们做过的所有事情，以及要求你完成的作业。如果你缺了某个作业，请补上：每个人都要完成所有作业。",
    },
    "blocchi": [
        ("1", {"it": "I primi giorni (settembre)", "ar": "الأيام الأولى (سبتمبر)", "zh": "最初几天（九月）"}, [
            ("15-17/09", {"it": "Abbiamo imparato a entrare nel computer e in Google con il nostro account, a usare Drive e Classroom e a fare ordine nelle cartelle.",
                          "ar": "تعلمنا الدخول إلى الحاسوب وإلى Google بحسابنا، واستخدام Drive وClassroom وترتيب المجلدات.",
                          "zh": "我们学会了用自己的账号登录电脑和 Google，使用 Drive 和 Classroom，并把文件夹整理好。"}),
            ("16/09", {"it": "Abbiamo letto le regole per usare computer, internet e intelligenza artificiale a scuola.",
                       "ar": "قرأنا قواعد استخدام الحاسوب والإنترنت والذكاء الاصطناعي في المدرسة.",
                       "zh": "我们读了在学校使用电脑、网络和人工智能的规则。"}),
            ("17/09", {"it": "Primo lavoro: un documento Google su «Io e la mia famiglia», consegnato su Classroom.",
                       "ar": "العمل الأول: مستند Google عن «أنا وعائلتي» وتسليمه على Classroom.",
                       "zh": "第一个作业：用 Google 文档写“我和我的家人”，并在 Classroom 提交。"}),
        ]),
        ("2", {"it": "Il computer da dentro", "ar": "الحاسوب من الداخل", "zh": "电脑的内部"}, [
            ("24/09", {"it": "Come è fatto un PC: scheda madre, processore (CPU), RAM, slot e prese. Lavoro: un documento con teoria e immagini, consegnato su Classroom.",
                       "ar": "كيف يتكوّن الحاسوب: اللوحة الأم، المعالج (CPU)، الذاكرة RAM، الفتحات والمقابس. العمل: مستند فيه شرح وصور وتسليمه على Classroom.",
                       "zh": "电脑是怎样组成的：主板、处理器（CPU）、内存 RAM、插槽和接口。作业：一个有说明和图片的文档，在 Classroom 提交。"}),
            ("12/11", {"it": "ICT e hardware: che cos'è un computer e il modello di Von Neumann (CPU, RAM, memorie di massa, scheda madre). Lavoro su Classroom e quiz di 12 domande.",
                       "ar": "تكنولوجيا المعلومات والعتاد: ما هو الحاسوب ونموذج فون نيومان (CPU وRAM وذاكرة التخزين واللوحة الأم). عمل على Classroom واختبار من 12 سؤالاً.",
                       "zh": "信息技术与硬件：什么是计算机，以及冯·诺依曼模型（CPU、RAM、大容量存储、主板）。在 Classroom 的作业和 12 道题的测验。"}),
        ]),
        ("3", {"it": "Bit, byte e velocità della rete", "ar": "البت والبايت وسرعة الشبكة", "zh": "比特、字节和网络速度"}, [
            ("01/10", {"it": "Bit e byte: il sistema binario e come passare da binario a decimale con la tabella dei valori (128, 64, 32 … 1). Esercizio con 16 conversioni su Classroom.",
                       "ar": "البت والبايت: النظام الثنائي وكيف ننتقل من الثنائي إلى العشري بجدول القيم (128، 64، 32 … 1). تمرين من 16 تحويلاً على Classroom.",
                       "zh": "比特和字节：二进制，以及用数值表（128、64、32 … 1）把二进制换成十进制。在 Classroom 的 16 道转换练习。"}),
            ("20-21/10", {"it": "Quanto pesa un file e quanto va veloce la rete: KB, MB, GB, TB, bit e byte, Mbps, tempo di download. Giochi dei byte e quiz.",
                          "ar": "كم يزن الملف وما سرعة الشبكة: KB وMB وGB وTB، البت والبايت، Mbps، وقت التنزيل. ألعاب البايت واختبار.",
                          "zh": "文件有多重、网络有多快：KB、MB、GB、TB，比特和字节，Mbps，下载时间。字节游戏和测验。"}),
            ("23/10", {"it": "Rete e gamer: ping, jitter, TCP e UDP, FPS e Hz, pixel e risoluzione. App «Le misure del mio PC» e quiz.",
                       "ar": "الشبكة واللاعب: ping وjitter وTCP وUDP وFPS وHz، البكسل والدقة. تطبيق «قياسات حاسوبي» واختبار.",
                       "zh": "网络与游戏玩家：ping、jitter、TCP 和 UDP、FPS 和 Hz、像素和分辨率。应用“我电脑的测量”和测验。"}),
        ]),
        ("4", {"it": "Programmare con Lazarus", "ar": "البرمجة مع Lazarus", "zh": "用 Lazarus 编程"}, [
            ("28/10", {"it": "Il primo programma in Lazarus: un bottone che scrive «Ciao». Progetto nuovo in una cartella, palette dei componenti, Edit e Button.",
                       "ar": "أول برنامج في Lazarus: زر يكتب «Ciao». مشروع جديد في مجلد، لوحة المكوّنات، Edit وButton.",
                       "zh": "Lazarus 的第一个程序：一个会显示“Ciao”的按钮。在文件夹里新建项目，组件面板，Edit 和 Button。"}),
            ("30/10", {"it": "Variabili String (testo) e Integer (numero intero). StrToInt e IntToStr per passare da testo a numero e da numero a testo. Unicode e codice ASCII: il computer scrive in tutte le lingue.",
                       "ar": "المتغيرات String (نص) وInteger (عدد صحيح). StrToInt وIntToStr للتحويل من نص إلى رقم ومن رقم إلى نص. Unicode وASCII: الحاسوب يكتب بكل اللغات.",
                       "zh": "变量 String（文本）和 Integer（整数）。用 StrToInt 和 IntToStr 在文本和数字之间转换。Unicode 和 ASCII 码：电脑能写所有语言。"}),
            ("04/11", {"it": "Far girare un programma (Esegui, F9) e il file .exe nella cartella del progetto. Tre programmi: convertitore di misure, calcolatrice a quattro bottoni, cassiere con div e mod.",
                       "ar": "تشغيل البرنامج (Esegui وF9) وملف .exe في مجلد المشروع. ثلاثة برامج: محوّل القياسات، آلة حاسبة بأربعة أزرار، أمين الصندوق مع div وmod.",
                       "zh": "运行程序（Esegui，F9）和项目文件夹里的 .exe 文件。三个程序：单位转换器、四个按钮的计算器、带 div 和 mod 的收银员。"}),
            ("05-06/11", {"it": "Stringhe e interi, conversioni. Il Convertitore. «Lo scontrino che parla». Ripasso di stringhe e interi.",
                          "ar": "النصوص والأعداد الصحيحة والتحويلات. المحوّل. «الإيصال الناطق». مراجعة النصوص والأعداد الصحيحة.",
                          "zh": "字符串和整数、转换。转换器。“会说话的小票”。字符串和整数的复习。"}),
            ("11/11", {"it": "Operazioni con String e Integer, poi i numeri reali (con la virgola) e la divisione. Due quiz e un lavoro su Classroom per ogni ora.",
                       "ar": "عمليات مع String وInteger، ثم الأعداد الحقيقية (بفاصلة) والقسمة. اختباران وعمل على Classroom لكل ساعة.",
                       "zh": "String 和 Integer 的运算，然后是实数（带小数点）和除法。两个测验，每节课在 Classroom 有一个作业。"}),
        ]),
        ("5", {"it": "Internet e sicurezza", "ar": "الإنترنت والأمان", "zh": "网络与安全"}, [
            ("03/11", {"it": "Deepfake: foto, voce e video falsi, e come difendersi. Lavoro su Classroom.",
                       "ar": "التزييف العميق: صور وأصوات وفيديوهات مزيفة، وكيف نحمي أنفسنا. عمل على Classroom.",
                       "zh": "深度伪造：假照片、假声音和假视频，以及如何保护自己。在 Classroom 的作业。"}),
            ("22/10-11/11", {"it": "Corso di Sicurezza sul lavoro: rischio e danno (22/10), prevenzione e protezione (29/10), organi di vigilanza (04/11), rischi meccanici ed elettrici (11/11). Dopo ogni ora c'è un quiz su Moduli.",
                             "ar": "دورة السلامة في العمل: الخطر والضرر (22/10)، الوقاية والحماية (29/10)، هيئات الرقابة (04/11)، المخاطر الميكانيكية والكهربائية (11/11). بعد كل ساعة هناك اختبار على Moduli.",
                             "zh": "工作安全课程：风险和伤害（10月22日），预防和防护（10月29日），监管机构（11月4日），机械和电气风险（11月11日）。每节课后有一个 Moduli 测验。"}),
        ]),
    ],
    "compiti_intro": {
        "it": "Apri Classroom e controlla che questi lavori siano consegnati. I titoli lunghi sono tagliati con «…».",
        "ar": "افتح Classroom وتأكد أن هذه الأعمال مسلّمة. العناوين الطويلة مقطوعة بعلامة «…».",
        "zh": "打开 Classroom，检查这些作业是否都已提交。太长的标题用“…”截断。",
    },
    "compiti": [
        "29/10 · OGGI 29/10: Sicurezza 2, prevenzione e protezione",
        "30/10 · OGGI 30/10: il computer scrive in tutte le lingue",
        "03/11 · 3/11 Ora 1: deepfake, foto, voce e video falsi",
        "05/11 · 5/11 Ora 6: Testo o numero?",
        "05/11 · 5/11 Ora 6: Bonus, trova l'e…",
        "06/11 · 6/11 Ora 4: Il convertitore…",
        "06/11 · 6/11 Ora 5: Lo scontrino che…",
        "11/11 · 11/11 Ora 1: String e Intege…",
        "11/11 · 11/11 Ora 2: Numeri reali e…",
        "11/11 · 11/11 Ora 6: Rischi meccanic…",
        "12/11 · 12/11 Ora 6: ICT e hardware del computer",
    ],
    "quiz_intro": {
        "it": "Quiz su Moduli Google (si possono rifare, vale il risultato migliore):",
        "ar": "اختبارات على Google Moduli (يمكن إعادتها، وتُحسب أفضل نتيجة):",
        "zh": "Google Moduli 测验（可以重做，取最好的成绩）：",
    },
    "quiz": [
        "11/11 · Quiz ora 1 FINALE: tipi di dati, begin/end e punto e virgola",
        "11/11 · Quiz ora 2 FINALE: numeri reali e divisione",
        "11/11 · Quiz Sicurezza quinta ora: rischio infortuni",
        "11/11 · Quiz Sicurezza ora 6A: rischi meccanici generali",
        "11/11 · Quiz Sicurezza ora 6B: rischi elettrici generali",
        "11/11 · Quiz Sicurezza RECUPERO ore 1-5",
        "12/11 · Quiz 12/11 Ora 6: ICT e hardware (1INF)",
    ],
    "parole": [
        ("bit", {"it": "la più piccola unità: 0 oppure 1", "ar": "أصغر وحدة: 0 أو 1", "zh": "最小的单位：0 或 1"}),
        ("byte", {"it": "8 bit insieme", "ar": "8 بتات معاً", "zh": "8 个比特在一起"}),
        ("CPU", {"it": "il processore: il cervello del computer", "ar": "المعالج: عقل الحاسوب", "zh": "处理器：电脑的大脑"}),
        ("RAM", {"it": "la memoria veloce: tiene quello che usi adesso", "ar": "الذاكرة السريعة: تحفظ ما تستخدمه الآن", "zh": "快速内存：保存你现在在用的东西"}),
        ("memoria di massa", {"it": "il disco: tiene tutti i file anche a computer spento", "ar": "القرص: يحفظ كل الملفات حتى والحاسوب مطفأ", "zh": "硬盘：电脑关机后也保存所有文件"}),
        ("String", {"it": "in Lazarus: un testo", "ar": "في Lazarus: نص", "zh": "在 Lazarus 中：一段文字"}),
        ("Integer", {"it": "in Lazarus: un numero intero", "ar": "في Lazarus: عدد صحيح", "zh": "在 Lazarus 中：一个整数"}),
        ("Unicode", {"it": "la tabella che dà un numero a ogni lettera di ogni lingua", "ar": "الجدول الذي يعطي رقماً لكل حرف في كل لغة", "zh": "给每种语言的每个字母一个编号的表"}),
    ],
}

# ----------------------------------------------------------------------------------------------- 2INF
DUE = {
    "classe": "2INF",
    "titolo": {"it": "Riepilogo del corso 2INF"},
    "intro": {"it": "Questa pagina racconta tutto quello che abbiamo fatto da settembre a oggi (12 novembre 2026) e i lavori che ti sono stati chiesti. Se ti manca un lavoro, fallo: tutti devono fare tutto."},
    "blocchi": [
        ("1", {"it": "Programmare con Lazarus"}, [
            ("01/10", {"it": "Il convertitore di temperature (Celsius e Fahrenheit): if, then, else, begin e end, il bottone Reset e le finestre di scelta."}),
            ("07/10", {"it": "Quiz «Cosa scrive il programma?» sulle istruzioni if, then, else."}),
            ("19/10", {"it": "Il ciclo FOR, seconda parte: il programma Contatore con due caselle (da… a…), un bottone e un Memo. Verifica sul ciclo FOR su Moduli."}),
            ("20/10", {"it": "Il ciclo WHILE («ripeti finché»): il gioco del dado, il ciclo infinito e come fermarlo. Verifica con il codice spiegato."}),
            ("22/10", {"it": "Interrogazioni sul ciclo WHILE. FOR e WHILE nel programma «Salvadanaio»."}),
        ]),
        ("2", {"it": "GitHub, versioni e metodo Agile"}, [
            ("12/10", {"it": "Versioni e Agile: il Manifesto e le 10 regole, la Pull Request sul gioco della classe, il backlog con i numeri di Fibonacci."}),
            ("22-26/10", {"it": "GitHub: un repository per i progetti Lazarus e uno per i progetti HTML, una cartella per ogni progetto, i file spostati con la matita di GitHub."}),
            ("29/10", {"it": "La calcolatrice in Lazarus in due versioni (v1.0 e v1.2) caricate su GitHub con commit e release, e un documento con gli screenshot."}),
        ]),
        ("3", {"it": "Sicurezza sul lavoro (corso della Regione)"}, [
            ("01/10-06/11", {"it": "Un'ora alla volta: rischio e danno, prevenzione e protezione, organizzazione della prevenzione, diritti, doveri e organi di vigilanza, rischio infortuni. Dopo ogni ora c'è un quiz su Moduli; chi ha perso un quiz lo recupera."}),
        ]),
        ("4", {"it": "Reti e sicurezza informatica"}, [
            ("02/11", {"it": "La rete del mio PC: indirizzo IP, MAC, gateway e DNS con il comando ipconfig; la scheda d'identità del PC. DHCP e DNS in quattro schede, con un quiz di 8 domande."}),
            ("02-03/11", {"it": "Social engineering e phishing: come si riconosce una mail falsa, la regola d'oro, il quiz. Il 3 novembre anche la verifica in due passaggi (2FA) di GitHub."}),
        ]),
        ("5", {"it": "Il PC e Windows 10"}, [
            ("05/11", {"it": "Smontaggio del PC: sicurezza e componenti. Assemblaggio, BIOS e avvio da USB. Installazione di Windows 10, utenti e IP."}),
            ("09/11", {"it": "Windows 10 come amministratore («Win10 Admin»)."}),
            ("10/11", {"it": "Configurazione e scelta dei componenti di un PC. Preventivo di un PC con il foglio di calcolo e quiz."}),
            ("12/11", {"it": "Tre ore su Windows 10: ora 1 utenti e gruppi (e recupero dei quiz), ora 2 Visualizzatore eventi e Gestione dispositivi, ora 3 Gestione attività e risorse. Per ogni ora: il documento della giornata, il compito su Classroom e il quiz di fine ora."}),
        ]),
    ],
    "compiti_intro": {"it": "Apri Classroom e controlla che questi lavori siano consegnati:"},
    "compiti": [
        "19/10 · VERIFICA: il ciclo FOR",
        "20/10 · Lazarus: il ciclo WHILE, lancia il dado finché…",
        "29/10 · OGGI 29/10: la calcolatrice Lazarus su GitHub",
        "30/10 · OGGI 30/10: Sicurezza, 5ª ora: il rischio infortuni",
        "12/11 · 12/11 Ora 1: Win10 utenti e recupero quiz",
        "12/11 · 12/11 Ora 2: Win10 eventi e Gestione dispositivi",
        "12/11 · 12/11 Ora 3: Win10 Gestione attività",
    ],
    "quiz_intro": {"it": "Quiz su Moduli Google (si possono rifare, vale il risultato migliore):"},
    "quiz": [
        "10/11 · Quiz Preventivo di un computer con il foglio di calcolo",
        "12/11 · Quiz fine ora 1: utenti e gruppi",
        "12/11 · Quiz fine ora 2: eventi e dispositivi",
        "12/11 · Quiz fine ora 3: attività e risorse",
    ],
    "parole": [
        ("utente e gruppo", {"it": "chi usa il PC e l'insieme di utenti con gli stessi permessi"}),
        ("amministratore", {"it": "l'utente che può cambiare tutto nel PC"}),
        ("privilegio minimo", {"it": "dare a ognuno solo i permessi che servono"}),
        ("Visualizzatore eventi", {"it": "il registro dove Windows scrive quello che succede"}),
        ("Gestione dispositivi", {"it": "l'elenco dei componenti del PC e dei loro driver"}),
        ("Gestione attività", {"it": "mostra i programmi in uso e quanta CPU e memoria usano"}),
        ("ciclo FOR e WHILE", {"it": "ripetere istruzioni: FOR un numero di volte noto, WHILE finché una condizione è vera"}),
        ("commit e release", {"it": "salvare una versione del progetto su GitHub e darle un numero"}),
    ],
}

# ----------------------------------------------------------------------------------------------- 3INF
TRE = {
    "classe": "3INF",
    "titolo": {"it": "Riepilogo del corso 3INF", "bn": "3INF কোর্সের সারসংক্ষেপ"},
    "intro": {"it": "Questa pagina racconta tutto quello che abbiamo fatto da settembre a oggi (12 novembre 2026) e i lavori che ti sono stati chiesti. Se ti manca un lavoro, fallo: tutti devono fare tutto.",
              "bn": "এই পাতায় সেপ্টেম্বর থেকে আজ (১২ নভেম্বর ২০২৬) পর্যন্ত আমরা যা যা করেছি এবং তোমার কাছে যে কাজগুলো চাওয়া হয়েছে তা আছে। কোনো কাজ বাকি থাকলে করে ফেলো: সবাইকে সব কাজ করতে হবে।"},
    "blocchi": [
        ("1", {"it": "Siti web", "bn": "ওয়েবসাইট"}, [
            ("05/10", {"it": "Pagina personale in HTML: la prima pagina web di ognuno, consegnata su Classroom.",
                       "bn": "এইচটিএমএল দিয়ে ব্যক্তিগত পেজ: প্রত্যেকের প্রথম ওয়েব পেজ, Classroom-এ জমা দেওয়া।"}),
            ("19/10", {"it": "Il sito diventa un portfolio: HTML5, CSS3 e GitHub Pages; la pagina «Cosa so fare» con il menu; verifica.",
                       "bn": "সাইট থেকে পোর্টফোলিও: HTML5, CSS3 ও GitHub Pages; মেনুসহ «আমি কী পারি» পেজ; যাচাই।"}),
            ("21/10", {"it": "Struttura del sito e CSS: cartelle e nomi giusti, immagine di sfondo, animazioni. Lavoro a squadre con ramo e Pull Request.",
                       "bn": "সাইটের কাঠামো ও CSS: সঠিক ফোল্ডার ও নাম, ব্যাকগ্রাউন্ড ছবি, অ্যানিমেশন। ব্রাঞ্চ ও Pull Request সহ দলগত কাজ।"}),
        ]),
        ("2", {"it": "Versioni, GitHub e metodo Agile", "bn": "সংস্করণ, GitHub ও Agile পদ্ধতি"}, [
            ("12/10", {"it": "Versioni, rami e Pull Request: come si chiede una modifica a un progetto di gruppo. Manifesto Agile e 10 regole, backlog.",
                       "bn": "সংস্করণ, ব্রাঞ্চ ও Pull Request: দলের প্রজেক্টে কীভাবে পরিবর্তনের অনুরোধ করতে হয়। Agile ম্যানিফেস্টো ও ১০টি নিয়ম, ব্যাকলগ।"}),
            ("14/10", {"it": "Verifica su Moduli: versioni, Pull Request e Agile.",
                       "bn": "Moduli-তে পরীক্ষা: সংস্করণ, Pull Request ও Agile।"}),
            ("10/11", {"it": "Sviluppo collaborativo: release e changelog. Quiz sulla Release 1.0 del Mastermind.",
                       "bn": "দলগত ডেভেলপমেন্ট: রিলিজ ও চেঞ্জলগ। Mastermind-এর Release 1.0 নিয়ে কুইজ।"}),
        ]),
        ("3", {"it": "Lazarus e Java", "bn": "Lazarus ও Java"}, [
            ("28-29/10", {"it": "Java senza installare niente: Eclipse portabile, Hello World con finestra e bottone, differenze tra Lazarus e Java.",
                          "bn": "কিছু ইনস্টল না করে Java: পোর্টেবল Eclipse, জানালা ও বোতামসহ Hello World, Lazarus ও Java-র পার্থক্য।"}),
        ]),
        ("4", {"it": "Il Mastermind in rete", "bn": "নেটওয়ার্কে Mastermind"}, [
            ("02/11", {"it": "Mastermind in Lazarus: codice con numeri casuali (Random), schede e punteggio. Poi client e server in rete (porta 5050).",
                       "bn": "Lazarus-এ Mastermind: র‍্যান্ডম সংখ্যার কোড, কার্ড ও স্কোর। তারপর নেটওয়ার্কে ক্লায়েন্ট ও সার্ভার (পোর্ট ৫০৫০)।"}),
            ("04/11", {"it": "Mastermind in rete: il protocollo dei messaggi, il client collegato al server, gara di classe.",
                       "bn": "নেটওয়ার্কে Mastermind: বার্তার প্রোটোকল, সার্ভারের সঙ্গে যুক্ত ক্লায়েন্ট, ক্লাসের প্রতিযোগিতা।"}),
            ("11/11", {"it": "Comunicazione tra client e server e chat in Lazarus. Quiz su protocollo e chat.",
                       "bn": "ক্লায়েন্ট ও সার্ভারের যোগাযোগ এবং Lazarus-এ চ্যাট। প্রোটোকল ও চ্যাট নিয়ে কুইজ।"}),
        ]),
        ("5", {"it": "Il PC", "bn": "পিসি"}, [
            ("05/11", {"it": "Smontaggio e assemblaggio di un PC: componenti, BIOS e ordine di avvio.",
                       "bn": "পিসি খোলা ও জোড়া লাগানো: যন্ত্রাংশ, BIOS ও বুট ক্রম।"}),
            ("09/11", {"it": "Installazione di Windows 10.",
                       "bn": "Windows 10 ইনস্টল করা।"}),
        ]),
    ],
    "compiti_intro": {"it": "Apri Classroom e controlla che questi lavori siano consegnati:",
                      "bn": "Classroom খুলে দেখো এই কাজগুলো জমা দেওয়া হয়েছে কিনা:"},
    "compiti": [
        "19/10 · Il mio sito diventa il mio portfolio",
        "28/10 · Hello World in Lazarus e in Java",
        "02/11 · Mastermind in rete: il tuo CLIENT",
        "04/11 · 4/11 Ora 2: partita di classe, GitHub e quiz (Mastermind in rete)",
    ],
    "quiz_intro": {"it": "Quiz su Moduli Google (si possono rifare, vale il risultato migliore):",
                   "bn": "Google Moduli কুইজ (আবার দেওয়া যায়, সেরা ফলাফল ধরা হয়):"},
    "quiz": [
        "14/10 · Verifica su versioni, Pull Request e Agile",
        "10/11 · Quiz Release 1.0 del Mastermind",
        "11/11 · Quiz ore 4-5: protocollo e chat",
    ],
    "parole": [
        ("repository", {"it": "la cartella del progetto su GitHub", "bn": "GitHub-এ প্রজেক্টের ফোল্ডার"}),
        ("ramo (branch)", {"it": "una copia del progetto dove lavori senza rompere l'originale", "bn": "প্রজেক্টের একটি কপি, যেখানে মূলটি নষ্ট না করে কাজ করা যায়"}),
        ("Pull Request", {"it": "la richiesta di unire le tue modifiche al progetto", "bn": "তোমার পরিবর্তন প্রজেক্টে যুক্ত করার অনুরোধ"}),
        ("client e server", {"it": "il client chiede, il server risponde", "bn": "ক্লায়েন্ট চায়, সার্ভার উত্তর দেয়"}),
        ("protocollo", {"it": "le regole con cui due programmi si scrivono", "bn": "যে নিয়মে দুটি প্রোগ্রাম একে অপরকে বার্তা পাঠায়"}),
        ("release", {"it": "una versione del programma con un numero, pronta da usare", "bn": "নম্বরসহ প্রোগ্রামের একটি সংস্করণ, ব্যবহারের জন্য তৈরি"}),
    ],
}

# ----------------------------------------------------------------------------------------------- 4TI
QUATTRO = {
    "classe": "4TI",
    "titolo": {"it": "Riepilogo del corso 4TI"},
    "intro": {"it": "Questa pagina racconta quello che abbiamo fatto da settembre a oggi (12 novembre 2026) nel laboratorio di reti e i lavori che ti sono stati chiesti. Se ti manca un lavoro, fallo: tutti devono fare tutto."},
    "blocchi": [
        ("1", {"it": "I sette livelli ISO/OSI"}, [
            ("06/10", {"it": "La pila dei sette livelli, l'incapsulamento, i dispositivi di rete (a che livello lavora ognuno), il metodo del tecnico di rete e il viaggio di un messaggio da un PC all'altro. Quiz ISO/OSI di 20 domande su Moduli."}),
            ("20/10", {"it": "Ripasso ISO/OSI, verifica e quiz su Moduli."}),
        ]),
        ("2", {"it": "Protocolli di rete"}, [
            ("27/10", {"it": "Protocolli di rete (titolo del registro: «Protocolli di rete»)."}),
        ]),
        ("3", {"it": "Indirizzi IPv4 e subnetting"}, [
            ("03/11", {"it": "L'indirizzo IPv4, la maschera, il gateway, DHCP e DNS. Esercizi su coppie di PC, una scheda sugli indirizzi e un quiz su Moduli."}),
            ("10/11", {"it": "Subnetting a passi: calcolare maschera, rete e host di 3 reti. Quiz «Subnetting a passi» e scheda «Leggere il piano di rete»."}),
        ]),
    ],
    "compiti_intro": {"it": "Controlla su Classroom di avere consegnato i lavori delle lezioni del 3 e del 10 novembre e le prove di ottobre."},
    "compiti": [],
    "quiz_intro": {"it": "Quiz su Moduli Google (si possono rifare, vale il risultato migliore):"},
    "quiz": [
        "06/10 · Quiz ISO/OSI, 20 domande",
        "10/11 · Quiz Subnetting a passi",
    ],
    "parole": [
        ("livello ISO/OSI", {"it": "uno dei sette strati del modello che spiega come viaggiano i dati"}),
        ("incapsulamento", {"it": "ogni livello aggiunge la sua intestazione al messaggio"}),
        ("indirizzo IPv4", {"it": "quattro numeri da 0 a 255 che dicono dove sta un PC nella rete"}),
        ("maschera di sottorete", {"it": "dice quale parte dell'indirizzo è la rete e quale è il PC"}),
        ("gateway", {"it": "la porta verso un'altra rete, di solito il router"}),
        ("DHCP e DNS", {"it": "DHCP dà l'indirizzo al PC; DNS trasforma un nome in un indirizzo"}),
    ],
}

CLASSI = {"1INF": UNO, "2INF": DUE, "3INF": TRE, "4TI": QUATTRO}
