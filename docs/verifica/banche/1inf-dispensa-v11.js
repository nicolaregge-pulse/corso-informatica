// 1INF · quiz su tutta la dispensa v1.1 (classe-1/dispensa/dispensa-1inf.md). PIANO B del quiz su Moduli. Preparata il 30/10/2026, APERTA il 30/10 alle ~11:30 («apri quiz» di Nicola) con stato/1inf-dispensa-v11.json. Dopo la consegna: bottone verso Lazarus Ora 1 (campo «dopo»).
window.BANCA = {
 "id": "1inf-dispensa-v11-v1",
 "classe": "1INF",
 "titolo": "Quiz sulla dispensa · اختبار الملزمة · 讲义测验",
 "sotto": "1INF · dispensa v1.1 · lezioni dal 15/09 al 30/10/2026 · 15 crocette e 5 domande scritte",
 "stato": "stato/1inf-dispensa-v11.json",
 "minuti": 30,
 "dopo": {"t": "Finito il quiz: Lazarus, Ora 1 · Il pasticcio dei numeri", "u": "https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lab-30-10/modulo-1.html", "nota": "Se ti blocchi a creare il progetto, alza la mano: arriva il Professore."},
 "anteprima": "4195422281",
 "aree": {
  "dispensa": {
   "nome": "La dispensa",
   "peso": 75
  },
  "mia": {
   "nome": "Il mio lavoro (parole tue)",
   "peso": 25
  }
 },
 "strumenti": [
  {
   "t": "La mia giornata: voto, fatto e da fare",
   "u": "../1inf-oggi/",
   "c": "#b45309"
  }
 ],
 "schede": [
  {
   "titolo": "Come è fatto il quiz · كيف هو الاختبار · 测验是什么样的",
   "testo": "<div style=\"border:3px solid #b45309;background:#fff3cd;color:#000;border-radius:12px;padding:10px\"><p style=\"color:#000\">1. Il quiz è su <b>tutta la dispensa</b>: le lezioni dal 15/09 al 30/10.</p><span lang=\"ar\" dir=\"rtl\" style=\"display:block;color:#333\">١. الاختبار عن كل الملزمة: الدروس من 15/09 إلى 30/10.</span><span lang=\"zh\" style=\"display:block;color:#333\">1. 测验包括整本讲义：9月15日到10月30日的课。</span><p style=\"color:#000\">2. 15 domande a crocette e 5 domande da scrivere con parole tue, sul TUO lavoro.</p><span lang=\"ar\" dir=\"rtl\" style=\"display:block;color:#333\">٢. ‏15 سؤال اختيار و5 أسئلة تكتب فيها بكلماتك عن عملك أنت.</span><span lang=\"zh\" style=\"display:block;color:#333\">2. 15 道选择题和 5 道写作题，用你自己的话写你自己的作品。</span><p style=\"color:#000\">3. Ripassa dalla dispensa: i capitoli 10, 11, 23, 25 e 26 sono i più importanti.</p><span lang=\"ar\" dir=\"rtl\" style=\"display:block;color:#333\">٣. راجع من الملزمة: الفصول 10 و11 و23 و25 و26 هي الأهم.</span><span lang=\"zh\" style=\"display:block;color:#333\">3. 用讲义复习：第 10、11、23、25、26 章最重要。</span></div>"
  }
 ],
 "allenamento": [],
 "crocette": [
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "binario",
   "q": "Alla lavagna del 01/10 il prof ha convertito il byte <code>01001110</code> con il metodo delle caselle. Quale conto è giusto?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">على السبورة يوم 01/10 حوّل الأستاذ البايت 01001110 بطريقة الخانات. أيّ حساب صحيح؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">10月1日黑板上，老师用格子法换算了字节 01001110。哪个算式是对的？</span>",
   "o": [
    "64 + 8 + 4 + 2 = 78",
    "64 + 8 + 4 + 1 = 77",
    "128 + 8 + 4 + 2 = 142",
    "64 + 16 + 4 + 2 = 86"
   ],
   "a": 0,
   "spiega": "Gli 1 stanno nelle caselle 64, 8, 4 e 2: 64 + 8 + 4 + 2 = 78."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "binario",
   "q": "Con il metodo delle divisioni per 2 (lavagna del 02/10) converti 22 e scrivilo in un byte da 8 cifre. Che cosa ottieni?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">بطريقة القسمة على 2 (سبورة 02/10) حوّل 22 واكتبه في بايت من 8 أرقام. ماذا تحصل؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">用除以 2 的方法（10月2日黑板）把 22 换算，写成 8 位的字节。结果是什么？</span>",
   "o": [
    "00010110",
    "00001101",
    "10110000",
    "00010111"
   ],
   "a": 0,
   "spiega": "22→11 resto 0; 11→5 resto 1; 5→2 resto 1; 2→1 resto 0; ultimo 1. Dal basso 10110, zeri a sinistra: 00010110."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "unicode",
   "q": "Alla lavagna del 30/10: A = 65 = <code>01000001</code> e B = 66 = <code>01000010</code>. Con la stessa regola, che byte è la C (67)?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">على سبورة 30/10: A = 65 = 01000001 و B = 66 = 01000010. بنفس القاعدة، ما هو بايت الحرف C (67)؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">10月30日黑板：A = 65 = 01000001，B = 66 = 01000010。按同样的规则，C（67）是哪个字节？</span>",
   "o": [
    "01000011",
    "01000100",
    "01000010",
    "11000001"
   ],
   "a": 0,
   "spiega": "67 = 64 + 2 + 1: caselle 64, 2 e 1."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "unicode",
   "q": "Scrivi il nome Ahmed in arabo: أحمد (4 lettere arabe). Quanti byte occupa in UTF-8?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">اكتب اسم أحمد بالعربية: 4 حروف عربية. كم بايتاً يشغل في UTF-8؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">用阿拉伯文写名字 Ahmed：أحمد（4 个阿拉伯字母）。用 UTF-8 占多少字节？</span>",
   "o": [
    "8 byte",
    "4 byte",
    "12 byte",
    "16 byte"
   ],
   "a": 0,
   "spiega": "In UTF-8 ogni lettera araba occupa 2 byte: 4 × 2 = 8."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "tipi",
   "q": "Lavagna 3 del 30/10: a sinistra le STRINGHE, a destra gli INTERI. Che cosa compare con questa riga?<br><code>Label1.Caption := '12' + '15';</code><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">سبورة 3 يوم 30/10: على اليسار النصوص (String) وعلى اليمين الأعداد الصحيحة (Integer). ماذا يظهر مع هذا السطر؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">10月30日第3块黑板：左边是字符串，右边是整数。这一行会显示什么？</span>",
   "o": [
    "1215",
    "27",
    "12 + 15",
    "errore quando premi F9"
   ],
   "a": 0,
   "spiega": "Sono due String (hanno gli apici): il + le attacca."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "tipi",
   "q": "Che cosa mostra la Label alla fine?<br><code>var a, b: Integer; s: String;</code><br><code>a := 4;</code><br><code>b := 6;</code><br><code>s := IntToStr(a) + IntToStr(b);</code><br><code>Label1.Caption := s + IntToStr(a + b);</code><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تُظهر Label في النهاية؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">最后 Label 显示什么？</span>",
   "o": [
    "4610",
    "20",
    "1010",
    "46"
   ],
   "a": 0,
   "spiega": "s = '46' (due String attaccate); a + b = 10, IntToStr dà '10'; '46' + '10' = '4610'."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "errori",
   "q": "Quale di queste righe dà errore (Incompatible types) quando premi F9?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ سطر من هذه يعطي خطأ (Incompatible types) عندما تضغط F9؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">按 F9 时，下面哪一行会出错（Incompatible types）？</span>",
   "o": [
    "Label1.Caption := 5 + 3;",
    "Label1.Caption := IntToStr(5 + 3);",
    "Label1.Caption := '5' + '3';",
    "Label1.Caption := Edit1.Text + '!';"
   ],
   "a": 0,
   "spiega": "La Caption è una String; 5 + 3 è un Integer: serve IntToStr."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "errori",
   "q": "Nel segnapunti (ora 3) c'è <code>var punti: Integer;</code>. Quale riga dà errore quando premi F9?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">في عدّاد النقاط (الساعة 3) يوجد var punti: Integer;. أيّ سطر يعطي خطأ عندما تضغط F9؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">在记分牌程序里（第 3 节）有 var punti: Integer;。按 F9 时哪一行会出错？</span>",
   "o": [
    "punti := Label1.Caption;",
    "punti := StrToInt(Label1.Caption);",
    "Label1.Caption := IntToStr(punti);",
    "punti := punti + 1;"
   ],
   "a": 0,
   "spiega": "La Caption è una String e punti è un Integer: serve StrToInt."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "tipi",
   "q": "Generatore di soprannomi (ora 2). Nella casella Edit1 scrivi Ahmed e premi il bottone. Che cosa compare?<br><code>nome := Edit1.Text;</code><br><code>Label1.Caption := 'nome' + ' detto ' + nome;</code><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">مولّد الألقاب (الساعة 2). تكتب Ahmed في الخانة Edit1 وتضغط الزر. ماذا يظهر؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">起外号程序（第 2 节）。在输入框 Edit1 里写 Ahmed，然后按按钮。会显示什么？</span>",
   "o": [
    "nome detto Ahmed",
    "Ahmed detto Ahmed",
    "nome detto nome",
    "errore quando premi F9"
   ],
   "a": 0,
   "spiega": "'nome' con gli apici è la PAROLA nome; nome senza apici è la SCATOLA, che contiene Ahmed."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "lazarus",
   "q": "Lavagna del 28/10: il progetto si chiama PIPPO. Quali sono i 4 file da tenere (da consegnare e da mettere su GitHub)?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">سبورة 28/10: اسم المشروع PIPPO. ما هي الملفات الأربعة التي يجب الاحتفاظ بها (للتسليم ولـ GitHub)؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">10月28日黑板：项目叫 PIPPO。要保留的 4 个文件（交作业、放到 GitHub 上）是哪些？</span>",
   "o": [
    "PIPPO.lpi, PIPPO.lpr, unit1.pas, unit1.lfm",
    "PIPPO.exe, PIPPO.lpi, unit1.pas, unit1.lfm",
    "PIPPO.lps, PIPPO.res, unit1.pas, unit1.o",
    "PIPPO.lpi, PIPPO.exe, PIPPO.ico, la cartella lib"
   ],
   "a": 0,
   "spiega": "Il resto (.exe, .lps, .res, .ico, lib, backup) Lazarus lo rifà da solo."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "rete",
   "q": "Un gioco pesa 3 GB e la tua linea va a 80 Mbps. Con i conti della lezione (1 GB = 1000 MB; da Mbps a MB al secondo dividi per 8), quanto ci mette a scaricarsi?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">لعبة حجمها 3 GB وسرعة خطك 80 Mbps. بحسابات الدرس (1 GB = 1000 MB؛ من Mbps إلى MB في الثانية اقسم على 8)، كم تحتاج لتنزيلها؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">一个游戏 3 GB，你的网速是 80 Mbps。按课上的算法（1 GB = 1000 MB；Mbps 换成每秒 MB 要除以 8），下载要多久？</span>",
   "o": [
    "300 secondi, cioè 5 minuti",
    "37,5 secondi",
    "2400 secondi, cioè 40 minuti",
    "30 secondi"
   ],
   "a": 0,
   "spiega": "80 : 8 = 10 MB al secondo; 3000 MB : 10 = 300 secondi."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "gamer",
   "q": "Lavagna del 23/10: 30 FPS su un monitor a 120 Hz = ogni immagine mostrata 4 volte. Il tuo gioco fa 48 FPS su un monitor a 144 Hz: quante volte viene mostrata ogni immagine?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">سبورة 23/10: ‏30 FPS على شاشة 120 Hz = كل صورة تُعرض 4 مرات. لعبتك تعطي 48 FPS على شاشة 144 Hz: كم مرة تُعرض كل صورة؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">10月23日黑板：30 FPS 配 120 Hz 显示器 = 每张画面显示 4 次。你的游戏是 48 FPS，显示器 144 Hz：每张画面显示几次？</span>",
   "o": [
    "3 volte",
    "4 volte",
    "96 volte",
    "una volta sola"
   ],
   "a": 0,
   "spiega": "144 : 48 = 3."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "versioni",
   "q": "Il tuo gioco è alla v1.9. Lo rifate tutto con il motore Godot, come il Treno blindato. Che numero ha la versione nuova?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">لعبتك في الإصدار v1.9. تعيدون صنعها كلها بمحرك Godot، مثل القطار المصفّح. ما رقم الإصدار الجديد؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你的游戏是 v1.9。你们用 Godot 引擎把它全部重做，就像装甲列车一样。新版本号是多少？</span>",
   "o": [
    "v2.0",
    "v1.10",
    "v1.9.1",
    "v2.9"
   ],
   "a": 0,
   "spiega": "Cambio grande = major: sale il primo numero e si riparte da .0."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "hardware",
   "q": "Hai un processore AMD Ryzen 5 con socket AM5 e due banchi di RAM DDR5. Quale scheda madre scegli?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">عندك معالج AMD Ryzen 5 بمقبس AM5 وشريحتا ذاكرة RAM من نوع DDR5. أيّ لوحة أم تختار؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你有一个 AMD Ryzen 5 处理器（插座 AM5）和两条 DDR5 内存。你选哪块主板？</span>",
   "o": [
    "socket AM5 e slot RAM DDR5",
    "socket LGA1700 e slot RAM DDR5",
    "socket AM4 e slot RAM DDR4",
    "socket AM5 e slot RAM DDR4"
   ],
   "a": 0,
   "spiega": "CPU e scheda madre con lo stesso socket; la RAM con la stessa DDR (la tacca è in un punto diverso)."
  },
  {
   "tipo": "c",
   "area": "dispensa",
   "tema": "sicurezza",
   "q": "In cucina giri il manico della padella verso dentro e prendi la pentola con i guanti da forno. Che cosa sono queste due cose?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">في المطبخ تدير مقبض المقلاة إلى الداخل وتمسك القدر بقفازات الفرن. ما هما هذان الأمران؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">在厨房里你把平底锅的把手转向里面，并戴隔热手套拿锅。这两件事分别是什么？</span>",
   "o": [
    "il manico girato è prevenzione, i guanti sono protezione",
    "il manico girato è protezione, i guanti sono prevenzione",
    "tutte e due prevenzione",
    "tutte e due protezione"
   ],
   "a": 0,
   "spiega": "Prevenzione: il danno succede meno spesso. Protezione: se succede, fa meno male."
  }
 ],
 "aperte": [
  {
   "area": "mia",
   "tema": "lazarus",
   "q": "Descrivi il programma Lazarus che hai fatto TU oggi in laboratorio (il pasticcio dei numeri, il soprannome o il segnapunti): che cosa c'è nella tua finestra e che cosa fa il bottone quando lo premi. Poi copia, scrivendola tu, UNA riga del TUO codice e spiega con parole tue che cosa fa.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">صِف برنامج Lazarus الذي صنعته أنت اليوم في المختبر (فوضى الأرقام، أو اللقب، أو عدّاد النقاط): ماذا يوجد في نافذتك وماذا يفعل الزر عندما تضغطه. ثم اكتب بنفسك سطراً واحداً من كودك واشرح بكلماتك ماذا يفعل.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">描述你今天在实验课上自己做的 Lazarus 程序（数字大杂烩、起外号或记分牌）：你的窗口里有什么，按下按钮时会发生什么。然后亲手写出你代码中的一行，用你自己的话解释它做什么。</span>",
   "aiuto": "Almeno 25 parole, con parole tue. Puoi scrivere anche nella tua lingua. Racconta il TUO lavoro: l'AI non lo conosce.",
   "min_parole": 25,
   "criteri": "nomina il proprio programma; descrive i pezzi della finestra (Label, Edit, Button) e che cosa compare al clic; una riga vera del codice (IntToStr, StrToInt o + tra String) spiegata con le parole String e Integer; coerente con la consegna dell'ora"
  },
  {
   "area": "mia",
   "tema": "hardware",
   "q": "Il PC che hai configurato TU (compiti del 24/09 e del 30/09): scrivi due pezzi che hai scelto, con il nome o il modello, e spiega perché devono andare d'accordo (socket, RAM DDR, slot PCIe o form factor).<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">الحاسوب الذي جهّزته أنت (واجبات 24/09 و30/09): اكتب قطعتين اخترتهما، مع الاسم أو الطراز، واشرح لماذا يجب أن تتوافقا (المقبس، ذاكرة DDR، منفذ PCIe أو حجم اللوحة).</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你自己配置的电脑（9月24日和9月30日的作业）：写出你选的两个配件（名称或型号），并解释它们为什么必须匹配（插座、DDR 内存、PCIe 插槽或主板尺寸）。</span>",
   "aiuto": "Almeno 25 parole, con parole tue. Puoi scrivere anche nella tua lingua. Racconta il TUO lavoro: l'AI non lo conosce.",
   "min_parole": 25,
   "criteri": "due pezzi reali della propria configurazione (modello); la compatibilità giusta: CPU-scheda madre stesso socket, RAM stessa DDR, scheda video slot PCIe x16, case e form factor; confronto con il Documento consegnato"
  },
  {
   "area": "mia",
   "tema": "versioni",
   "q": "La TUA Pull Request (il Treno blindato del 08/10 o del 13/10, oppure la talpa del 14/10): che cosa hai chiesto di cambiare, con quale valore o disegno nuovo, e perché? Poi spiega con parole tue che cos'è il merge.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">طلب الدمج (Pull Request) الخاص بك (القطار المصفّح يوم 08/10 أو 13/10، أو لعبة الخلد يوم 14/10): ماذا طلبت أن يتغيّر، بأي قيمة أو رسم جديد، ولماذا؟ ثم اشرح بكلماتك ما هو الدمج (merge).</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你自己的 Pull Request（10月8日或10月13日的装甲列车，或10月14日的打地鼠）：你请求改什么、新的数值或图画是什么、为什么？然后用你自己的话解释什么是 merge（合并）。</span>",
   "aiuto": "Almeno 25 parole, con parole tue. Puoi scrivere anche nella tua lingua. Racconta il TUO lavoro: l'AI non lo conosce.",
   "min_parole": 25,
   "criteri": "la propria richiesta (riga o pezzo, valore nuovo, perché), coerente con quella consegnata; merge = la richiesta accettata entra nel ramo principale e nasce una versione nuova"
  },
  {
   "area": "mia",
   "tema": "gamer",
   "q": "Il TUO documento «Rete e gamer» (23/10): che ping hai misurato con l'app «Le misure del mio PC» e che cosa vuol dire per il gioco a cui giochi tu? Poi fai un esempio della TUA giornata in cui si usa TCP e uno in cui si usa UDP.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">مستندك «الشبكة واللاعب» (23/10): ما قيمة ping التي قستها بتطبيق «قياسات حاسوبي» وماذا تعني للعبة التي تلعبها أنت؟ ثم أعطِ مثالاً من يومك يُستعمل فيه TCP ومثالاً يُستعمل فيه UDP.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你的文档《网络与玩家》（10月23日）：你用「我的电脑测量」应用测到的 ping 是多少？这对你玩的游戏意味着什么？再举一个你一天中用到 TCP 的例子和一个用到 UDP 的例子。</span>",
   "aiuto": "Almeno 25 parole, con parole tue. Puoi scrivere anche nella tua lingua. Racconta il TUO lavoro: l'AI non lo conosce.",
   "min_parole": 25,
   "criteri": "un ping in ms con il giudizio della tabella (sotto 30 ottimo … oltre 150 lag); il proprio gioco; TCP = arriva tutto (download, pagine, email); UDP = veloce, niente ritrasmissione (voce, videochiamata, gioco online)"
  },
  {
   "area": "mia",
   "tema": "sicurezza",
   "q": "Pensa a un pericolo VERO che c'è a casa tua, in laboratorio o sulla strada che fai per venire a scuola. Descrivilo, poi scrivi una cosa di PREVENZIONE e una di PROTEZIONE per quel pericolo, spiegando la differenza con parole tue.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">فكّر في خطر حقيقي موجود في بيتك أو في المختبر أو في الطريق التي تسلكها إلى المدرسة. صِفه، ثم اكتب شيئاً للوقاية وشيئاً للحماية من هذا الخطر، واشرح الفرق بكلماتك.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">想一个真实的危险：在你家里、在实验室，或在你上学的路上。描述它，然后写一个「预防」措施和一个「防护」措施，并用你自己的话解释两者的区别。</span>",
   "aiuto": "Almeno 25 parole, con parole tue. Puoi scrivere anche nella tua lingua. Racconta il TUO lavoro: l'AI non lo conosce.",
   "min_parole": 25,
   "criteri": "un pericolo concreto e personale; prevenzione = il danno succede meno spesso (agisci prima); protezione = se succede fa meno male (casco, guanti, DPI); la regola d'oro"
  }
 ],
 "recupero": []
};
