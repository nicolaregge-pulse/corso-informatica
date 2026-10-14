// 1INF · Ripasso, verifica e recupero sul gioco della talpa (14/10/2026): un'app condivisa, Pull Request, merge, versioni,
// backlog e changelog; gestione delle foto (ritagliare, copiare, incollare, salvare, caricare); l'esperienza personale.
// Aree e peso nel giudizio: nozioni 40%, pratica 30%, esperienza personale 20%, dati 10%. Italiano, arabo, cinese.
(function () {
  function L(it, ar, zh) { return it + '<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em">' + ar + '</div><div style="color:#5d6878">' + zh + '</div>'; }
  function S(n, q) { q.scheda = n; return q; }
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  var QUARTI = [["09:00", 0], ["09:15", 10], ["09:30", 1], ["09:45", 12]];   // personaggi entrati nel gioco per quarto d'ora

  window.BANCA = {
    id: "1inf-talpa-20261014",
    classe: "1INF",
    titolo: "Il gioco della talpa: un'app di tutta la classe",
    sotto: "1INF · 14/10/2026 · ripasso, verifica e recupero",
    stato: "stato/1inf-talpa.json",
    risultati: "risultati.html?b=1inf-talpa",
    backlog: "../1inf-backlog/backlog.json",
    modulo: "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform",
    minuti: 30,
    anteprima: "868848605",
    aree: {
      nozioni: { nome: "Nozioni: app condivisa, Pull Request, merge, versioni", peso: 40 },
      pratica: { nome: "Pratica: le foto (ritagliare, copiare, incollare, salvare, caricare)", peso: 30 },
      personale: { nome: "La tua esperienza (solo parole tue)", peso: 20 },
      dati: { nome: "Leggere i dati della lezione", peso: 10 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    quarti: QUARTI,

    /* ---------- RIPASSO ---------- */
    schede_temi: { app: 1, pr: 2, merge: 2, versione: 3, changelog: 3, backlog: 3, ritaglio: 4, copia: 4, salva: 5, carica: 5 },
    schede: [
      { titolo: "1. Un'app di tutta la classe", testo: L("Tutta la classe lavora su <b>un solo programma</b>: il gioco della talpa. Ognuno porta un pezzo: il suo personaggio. Regola: <b>si aggiunge, non si cancella</b> il lavoro degli altri.", "كل الصف يعمل على <b>برنامج واحد</b>: لعبة الخُلد. كل واحد يجلب قطعة: شخصيته. القاعدة: <b>نضيف ولا نمسح</b> عمل الآخرين.", "全班一起做<b>同一个程序</b>：打地鼠游戏。每个人带来一部分：自己的角色。规则：<b>只添加，不删除</b>别人的成果。") },
      { titolo: "2. Pull Request e Merge", testo: L("La <b>Pull Request</b> è una <b>richiesta</b>: «ecco il mio personaggio, mettilo nel gioco». Il prof la controlla e la unisce al gioco: questo si chiama <b>merge</b> (unione).", "<b>Pull Request</b> هو <b>طلب</b>: «هذه شخصيتي، ضعها في اللعبة». الأستاذ يتحقق ويدمجها في اللعبة: اسمه <b>merge</b> (دمج).", "<b>Pull Request</b> 是一个<b>请求</b>：「这是我的角色，把它放进游戏」。老师检查后把它合并进游戏：这叫 <b>merge</b>（合并）。") },
      { titolo: "3. Versioni, backlog, changelog", testo: L("Ogni modifica fa nascere una <b>versione nuova</b>: v1.1, v1.2… Il <b>backlog</b> è la fila delle richieste. Il <b>changelog</b> è il diario: che cosa è cambiato in ogni versione e chi l'ha chiesto.", "كل تعديل يصنع <b>نسخة جديدة</b>: v1.1، v1.2… <b>backlog</b> هو قائمة الطلبات. <b>changelog</b> هو المذكرة: ما الذي تغيّر في كل نسخة ومن طلبه.", "每个修改产生一个<b>新版本</b>：v1.1、v1.2……<b>backlog</b> 是请求的队列。<b>changelog</b> 是日记：每个版本改了什么、是谁要求的。") },
      { titolo: "4. Ritagliare e copiare una foto", testo: L("<b>Ritagliare</b> = tenere solo la parte che serve (la testa). Sul PC: <b>Windows + Maiusc + S</b> e disegni un quadrato. <b>Copiare</b> un'immagine: tasto destro → «Copia immagine». <b>Incollare</b>: <b>Ctrl + V</b>.", "<b>القص</b> = نحتفظ بالجزء المهم فقط (الرأس). في الحاسوب: <b>Windows + Shift + S</b> وترسم مربعًا. <b>نسخ</b> صورة: الزر الأيمن ← «Copia immagine». <b>اللصق</b>: <b>Ctrl + V</b>.", "<b>裁剪</b>＝只留下需要的部分（头）。在电脑上：<b>Windows + Shift + S</b>，然后画一个方框。<b>复制</b>图片：右键 →「Copia immagine」。<b>粘贴</b>：<b>Ctrl + V</b>。") },
      { titolo: "5. Salvare e caricare", testo: L("<b>Salvare con nome</b>: scegli la cartella (Immagini) e un nome chiaro, senza spazi: 1INF_cognome-nome_foto.png. <b>Caricare</b> sul Modulo: «Aggiungi file» → «Sfoglia» → scegli il file → «Apri» → «Invia».", "<b>الحفظ باسم</b>: اختر المجلد (الصور) واسمًا واضحًا بدون فراغات: 1INF_cognome-nome_foto.png. <b>الرفع</b> إلى النموذج: «Aggiungi file» ← «Sfoglia» ← اختر الملف ← «Apri» ← «Invia».", "<b>另存为</b>：选文件夹（图片）和一个清楚、没有空格的名字：1INF_cognome-nome_foto.png。<b>上传</b>到表单：「Aggiungi file」→「Sfoglia」→ 选文件 →「Apri」→「Invia」。") }
    ],
    strumenti: [{ t: 'Il monitor della lezione', u: 'https://nicolaregge-pulse.github.io/corso-informatica/1inf-monitor/', c: '#6e40c9' }, { t: 'Il gioco', u: 'https://nicolaregge-pulse.github.io/corso-informatica/giochi/talpa-1inf/', c: '#1a7f37' }],
    via: C("nozioni", L("Oggi, come avete chiesto di mettere il vostro personaggio nel gioco?", "اليوم، كيف طلبتم وضع شخصيتكم في اللعبة؟", "今天你们是怎么要求把角色放进游戏的？"), ["con una richiesta (Pull Request)", "scrivendo il codice da soli", "senza chiedere niente"], "Esatto: una richiesta, una Pull Request."),
    prepara: [
      { q: L("Racconta con parole tue che cosa hai fatto oggi, dall'inizio alla fine.", "احكِ بكلماتك ماذا فعلت اليوم، من البداية إلى النهاية.", "用你自己的话说说今天从头到尾做了什么。"), min: 15 }
    ],
    allenamento: [
      S(1, C("nozioni", L("Nell'app di tutta la classe, il lavoro degli altri…", "في تطبيق كل الصف، عمل الآخرين…", "在全班的应用里，别人的成果……"), ["non si cancella: si aggiunge il proprio", "si può cancellare", "si cambia come si vuole"], "Aggiungere sì, cancellare no.")),
      S(2, C("nozioni", L("«Ecco il mio personaggio, mettilo nel gioco» è…", "«هذه شخصيتي، ضعها في اللعبة» هو…", "「这是我的角色，把它放进游戏」是……"), ["una Pull Request", "un merge", "un changelog"], "La richiesta si chiama Pull Request.")),
      S(2, C("nozioni", L("Il prof unisce la richiesta al gioco: si chiama…", "الأستاذ يدمج الطلب في اللعبة: اسمه…", "老师把请求合并进游戏：这叫……"), ["merge", "backlog", "versione"], "Merge = unione.")),
      S(3, C("nozioni", L("Dove leggi che cosa è cambiato in ogni versione?", "أين تقرأ ما الذي تغيّر في كل نسخة؟", "在哪里看每个版本改了什么？"), ["nel changelog", "nel backlog", "su Classroom"], "Il changelog è il diario delle versioni.")),
      S(4, C("pratica", L("Per incollare un'immagine premi…", "للصق صورة تضغط…", "粘贴图片要按……"), ["Ctrl + V", "Ctrl + C", "Ctrl + P"], "Ctrl + C copia, Ctrl + V incolla.")),
      S(5, C("pratica", L("Quale nome di file è giusto?", "أي اسم ملف صحيح؟", "哪个文件名是对的？"), ["1INF_rossi-mario_foto.png", "foto di Mario.png", "IMG 2026 10 14.png"], "Classe, cognome-nome, che cosa è: senza spazi."))
    ],

    /* ---------- VERIFICA ---------- */
    crocette: [
      C("nozioni", L("Che cos'è un'app condivisa?", "ما هو التطبيق المشترك؟", "什么是共享的应用？"), ["un solo programma a cui lavorano in tanti, ognuno con il suo pezzo", "un programma di una sola persona", "un gioco già finito"], "Tutta la classe lavora sullo stesso gioco.", "app"),
      C("nozioni", L("La regola del lavoro in squadra sul codice è…", "قاعدة العمل الجماعي على الكود هي…", "团队一起写代码的规则是……"), ["aggiungere il proprio pezzo, senza cancellare quello degli altri", "cancellare quello che non piace", "rifare tutto da capo"], "Aggiungere sì, cancellare no.", "app"),
      C("nozioni", L("Una Pull Request è…", "Pull Request هو…", "Pull Request 是……"), ["una richiesta di modifica", "una versione del gioco", "una password"], "Pull Request = richiesta di unire il tuo pezzo.", "pr"),
      C("nozioni", L("Il merge è…", "merge هو…", "merge 是……"), ["l'unione della modifica al gioco, dopo il controllo del prof", "la cancellazione del gioco", "il nome del gioco"], "Merge = unione.", "merge"),
      C("nozioni", L("Dopo ogni modifica entrata nel gioco…", "بعد كل تعديل يدخل اللعبة…", "每个修改进入游戏之后……"), ["nasce una versione nuova (v1.1, v1.2…)", "il gioco ricomincia da zero", "non cambia niente"], "Ogni modifica, una versione.", "versione"),
      C("nozioni", L("Il backlog è…", "backlog هو…", "backlog 是……"), ["la fila delle richieste, con chi e quando", "il diario delle versioni", "il gioco finito"], "Backlog = coda dei lavori.", "backlog"),
      C("nozioni", L("Il changelog è…", "changelog هو…", "changelog 是……"), ["il diario di che cosa è cambiato in ogni versione", "la fila delle richieste", "la classifica"], "Change = cambio, log = diario.", "changelog"),
      C("pratica", L("Ritagliare una foto vuol dire…", "قص الصورة يعني…", "裁剪照片的意思是……"), ["tenere solo la parte che serve, per esempio la testa", "cancellarla", "colorarla"], "Si tiene solo la parte utile.", "ritaglio"),
      C("pratica", L("Per copiare un'immagine da internet…", "لنسخ صورة من الإنترنت…", "从网上复制一张图片……"), ["tasto destro sull'immagine → «Copia immagine»", "doppio clic sull'immagine", "Ctrl + S"], "Tasto destro, Copia immagine.", "copia"),
      C("pratica", L("Ctrl + C e Ctrl + V servono a…", "Ctrl + C و Ctrl + V تستعمل لـ…", "Ctrl + C 和 Ctrl + V 用来……"), ["copiare e incollare", "salvare e chiudere", "stampare e cancellare"], "C = copia, V = incolla.", "copia"),
      C("pratica", L("Sul PC della scuola, per ritagliare un pezzo di schermo premi…", "في حاسوب المدرسة، لقص جزء من الشاشة تضغط…", "在学校电脑上，要截取屏幕的一部分，按……"), ["Windows + Maiusc + S", "Ctrl + Z", "Alt + F4"], "Poi disegni un quadrato.", "ritaglio"),
      C("pratica", L("Per mandare la foto con il Modulo «Consegna»…", "لإرسال الصورة بنموذج «Consegna»…", "用「Consegna」表单发送照片……"), ["«Aggiungi file» → «Sfoglia» → scegli il file → «Apri» → «Invia»", "la scrivi a mano", "la stampi"], "Si carica il file e poi Invia.", "carica")
    ],
    dati: [
      { tipo: "c", area: "dati", tema: "grafico", q: L("Guarda il grafico: in quale quarto d'ora sono entrati più personaggi nel gioco?", "انظر إلى الرسم: في أي ربع ساعة دخلت شخصيات أكثر؟", "看图：哪一刻钟进入游戏的角色最多？"), o: ["09:45", "09:15", "09:30"], a: 0, spiega: "Alle 09:45 ne sono entrati 12.", grafico: true },
      { tipo: "n", area: "dati", tema: "grafico", q: L("Quanti personaggi in tutto dalle 09:15 alle 09:45 (somma delle tre barre)?", "كم شخصية في المجموع من 09:15 إلى 09:45 (مجموع الأعمدة الثلاثة)؟", "从 09:15 到 09:45 一共多少个角色（三根柱子的和）？"), giusto: 23, spiega: "10 + 1 + 12 = 23.", grafico: true }
    ],
    scale: [
      { area: "personale", q: L("Quanto ti è piaciuto mettere il tuo personaggio nel gioco?", "كم أعجبك وضع شخصيتك في اللعبة؟", "把你的角色放进游戏，你有多喜欢？"), basso: "per niente", alto: "moltissimo" },
      { area: "parere", q: L("Quanto ti è piaciuta questa verifica?", "كم أعجبك هذا الاختبار؟", "你有多喜欢这次测验？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "nozioni", tema: "app", q: L("Spiega con parole tue, come al direttore: che cosa avete fatto oggi con il gioco della talpa? Usa le parole richiesta (Pull Request), merge e versione.", "اشرح بكلماتك، كأنك تتكلم مع المدير: ماذا فعلتم اليوم بلعبة الخُلد؟ استعمل الكلمات: طلب (Pull Request)، merge، نسخة.", "用你自己的话，像对校长那样说：今天你们用打地鼠游戏做了什么？要用到这些词：请求（Pull Request）、merge、版本。"),
        aiuto: "Almeno 30 parole. Puoi scrivere anche nella tua lingua.", min_parole: 30,
        criteri: "un solo programma di tutta la classe; la richiesta; il controllo e il merge; la versione nuova; parole sue." },
      { area: "personale", tema: "personale", mostra_pr: true, q: L("Il tuo personaggio: com'è, ti piace? Che cosa cambieresti nella prossima Pull Request?", "شخصيتك: كيف هي، هل تعجبك؟ ماذا ستغيّر في الطلب القادم؟", "你的角色：是什么样子？你喜欢吗？下一个请求你想改什么？"),
        aiuto: "Almeno 20 parole.", min_parole: 20, criteri: "descrive il suo personaggio; un'idea concreta di modifica; parole sue." },
      { area: "parere", tema: "retro", q: L("Una cosa da fare di più e una da fare di meno nelle lezioni.", "شيء نفعله أكثر وشيء نفعله أقل في الدروس.", "上课时要多做的一件事和要少做的一件事。"), aiuto: "Anche poche parole, ma sincere.", min_parole: 3 }
    ],

    /* ---------- RECUPERO ---------- */
    recupero: [
      C("nozioni", L("Nel gioco ci sono i personaggi di tutti. Tu aggiungi il tuo. Che cosa NON devi fare?", "في اللعبة شخصيات الجميع. أنت تضيف شخصيتك. ماذا لا يجب أن تفعل؟", "游戏里有所有人的角色。你加上你的。你不能做什么？"), ["cancellare i personaggi degli altri", "aggiungere il tuo", "giocare"], "", "app"),
      C("nozioni", L("Chi controlla una Pull Request prima del merge?", "من يتحقق من Pull Request قبل الدمج؟", "merge 之前谁检查 Pull Request？"), ["il prof", "nessuno", "il gioco da solo"], "", "merge"),
      C("nozioni", L("Da v1.10 a v1.11 è entrato…", "من v1.10 إلى v1.11 دخل…", "从 v1.10 到 v1.11 进入了……"), ["un cambiamento nuovo (una modifica)", "niente", "un errore"], "", "versione"),
      C("nozioni", L("La seconda Pull Request, senza foto, chiede…", "الطلب الثاني، بدون صورة، يطلب…", "第二个请求不需要照片，它要求……"), ["di cambiare il personaggio, con una descrizione", "una foto nuova", "di cancellare il gioco"], "", "pr"),
      C("pratica", L("Hai copiato un'immagine. Per metterla nella pagina premi…", "نسخت صورة. لوضعها في الصفحة تضغط…", "你复制了一张图片。要把它放进页面，按……"), ["Ctrl + V", "Ctrl + C", "Esc"], "", "copia"),
      C("pratica", L("La foto è troppo grande, con altre persone. Che cosa fai?", "الصورة كبيرة، فيها أشخاص آخرون. ماذا تفعل؟", "照片太大，里面还有别人。你怎么办？"), ["la ritaglio: tengo solo la mia testa", "la mando così", "la cancello"], "", "ritaglio"),
      C("pratica", L("Dove salvi la foto per ritrovarla subito?", "أين تحفظ الصورة لتجدها بسرعة؟", "照片存在哪里能马上找到？"), ["nella cartella Immagini, con un nome chiaro", "dove capita", "non la salvo"], "", "salva"),
      C("pratica", L("Nel Modulo, dopo aver scelto il file, l'ultimo bottone è…", "في النموذج، بعد اختيار الملف، آخر زر هو…", "在表单里选好文件后，最后一个按钮是……"), ["«Invia»", "«Annulla»", "«Esci»"], "", "carica")
    ]
  };
})();
