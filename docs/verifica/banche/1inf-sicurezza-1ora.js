// 1INF · Sicurezza sul lavoro, 1ª lezione (22/10/2026, 13:05-14:00): PERICOLO, DANNO, RISCHIO con casi della loro vita.
// Correzione del docente (22/10): niente leggi e niente regolamento; solo casi reali e concreti (aula di informatica,
// cavi e prese, sedia e schermo, cucina di casa, motorino e bici, lavoretti, sport, telefono che si scalda).
// La 2ª lezione (prevenzione e protezione) è a parte: classe-1/sicurezza-1ora/ossatura-2a-lezione.md.
// Italiano semplicissimo + una riga in arabo e in cinese sotto titoli, schede e domande (come 1inf-byte-velocita).
// Tempi (errore #102): 8 schede ~12 min, ripasso 13 domande ~13 min, «prepara» ~4 min, quiz Moduli 20 domande ~20 min.
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function L(it, ar, zh) { return it + '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">' + ar + '</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">' + zh + '</span>'; }

  window.BANCA = {
    id: "1inf-sicurezza-1ora-v1",
    classe: "1INF",
    titolo: "Sicurezza 1: pericolo, danno, rischio · الخطر، الضرر، المخاطرة · 危险源、伤害、风险",
    sotto: "1INF · 22/10/2026 · sicurezza, 1ª lezione · casi veri: aula, casa, strada, sport, lavoretti · teoria, ripasso e quiz",
    stato: "stato/1inf-sicurezza-1ora.json",
    risultati: "risultati.html?b=1inf-sicurezza-1ora",
    minuti: 25,
    anteprima: "868848605",
    aree: {
      sic: { nome: "Pericolo, danno e rischio", peso: 80 },
      mia: { nome: "Nella mia vita (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },

    /* ---------- TEORIA E RIPASSO ---------- */
    schede_temi: { tre: 1, pericolo: 2, dove: 3, danno: 4, rischio: 5, altobasso: 6, insieme: 7, pelo: 8 },
    schede: [
      { titolo: "1. Oggi: tre parole · ١. اليوم: ثلاث كلمات · 1. 今天：三个词", testo: L(
        "Oggi comincia il corso sulla <b>sicurezza</b>. Serve a una cosa sola: <b>non farsi male</b>, a scuola, a casa, per strada e al lavoro.<br>Oggi impari tre parole:<br><b>PERICOLO</b>: una cosa che <b>può</b> fare male.<br><b>DANNO</b>: il male che <b>succede davvero</b>.<br><b>RISCHIO</b>: <b>quanto è facile</b> che il danno succeda, e <b>quanto è grave</b>.",
        "اليوم نتعلم ثلاث كلمات: الخطر = شيء يمكن أن يؤذي. الضرر = الأذى الذي يحدث فعلاً. المخاطرة = مدى سهولة حدوث الضرر ومدى خطورته.",
        "今天学三个词：危险源 = 可能伤人的东西。伤害 = 真的发生的伤。风险 = 伤害发生的可能性有多大、有多严重。") },
      { titolo: "2. Il pericolo · ٢. الخطر · 2. 危险源", testo: L(
        "Il <b>pericolo</b> è una cosa (o una situazione) che <b>può</b> fare male. Non ti ha ancora fatto niente: <b>potrebbe</b>.<br>Esempi: il <b>coltello</b>, l'<b>olio bollente</b> nella padella, la <b>presa</b> con i fili che si vedono, il <b>pavimento bagnato</b>, la <b>strada</b> piena di macchine.<br>Domanda magica: <b>«Che cosa qui mi può fare male?»</b> La risposta è il pericolo.",
        "الخطر = شيء يمكن أن يؤذي، لكنه لم يؤذك بعد. أمثلة: السكين، الزيت المغلي، المقبس بأسلاك ظاهرة، الأرض المبللة، الشارع.",
        "危险源 = 可能伤人的东西，但还没有伤到你。例如：刀、热油、露出电线的插座、湿的地板、马路。") },
      { titolo: "3. I pericoli sono dappertutto · ٣. الأخطار في كل مكان · 3. 危险源到处都有", testo: L(
        "<b>In aula di informatica:</b> cavi per terra, zaini nel passaggio, una presa rotta, la sedia che dondola, lo schermo troppo vicino.<br><b>A casa, in cucina:</b> il fornello acceso, la pentola che bolle, il coltello, il ferro da stiro.<br><b>In strada:</b> il motorino, la bici di sera senza luci, il telefono in mano mentre attraversi.<br><b>Nello sport e in palestra:</b> il pallone lasciato a terra, il pavimento bagnato, gli attrezzi.<br><b>Nei lavoretti:</b> la scala, il trapano, la sedia con le ruote usata come scala.",
        "في قاعة الحاسوب: أسلاك على الأرض، حقائب في الممر، مقبس مكسور. في المطبخ: الموقد، القدر الذي يغلي، السكين. في الشارع: الدراجة النارية، الدراجة بلا أضواء. في الرياضة: كرة على الأرض، أرض مبللة. في الأعمال الصغيرة: السلّم، المثقاب.",
        "电脑教室：地上的电线、过道里的书包、坏插座。厨房：炉子、开水锅、刀。马路：摩托车、晚上没灯的自行车。运动：地上的球、湿地板。打零工：梯子、电钻。") },
      { titolo: "4. Il danno · ٤. الضرر · 4. 伤害", testo: L(
        "Il <b>danno</b> è il male che <b>succede davvero</b>.<br>Esempi: un <b>taglio</b> al dito, una <b>bruciatura</b> alla mano, una <b>caviglia storta</b>, una <b>frattura</b> (un osso rotto), la <b>scossa</b> elettrica, il <b>mal di schiena</b>, gli <b>occhi stanchi</b> e il mal di testa dopo ore di schermo.<br>Il danno può essere piccolo (un graffio) o grande (un osso rotto). Si può rompere anche una cosa: il telefono, il PC.",
        "الضرر = الأذى الذي يحدث فعلاً: جرح، حرق، التواء الكاحل، كسر، صدمة كهربائية، ألم الظهر، تعب العينين. يمكن أن يكون صغيراً أو كبيراً.",
        "伤害 = 真的发生的伤：割伤、烫伤、扭伤脚踝、骨折、触电、腰疼、眼睛累。伤害可以小，也可以大。") },
      { titolo: "5. Il rischio · ٥. المخاطرة · 5. 风险", testo: L(
        "Il <b>rischio</b> risponde a due domande:<br>1) <b>Succede facilmente?</b> (spesso o quasi mai)<br>2) <b>Quanto male fa?</b> (poco o tanto)<br>Lo stesso pericolo può avere un rischio diverso. Il <b>coltello</b>: se tagli sul tagliere con le dita lontane, il rischio è <b>basso</b>. Se tagli il pane tenendolo in mano, verso la mano, il rischio è <b>alto</b>.<br>Il pericolo è la cosa. Il rischio dipende da <b>come</b> la usi.",
        "المخاطرة تجيب عن سؤالين: هل يحدث الضرر بسهولة؟ وكم يؤذي؟ نفس السكين: على لوح التقطيع والأصابع بعيدة = مخاطرة منخفضة؛ نحو اليد = مخاطرة عالية.",
        "风险回答两个问题：伤害容易发生吗？伤得有多重？同一把刀：在砧板上、手指离得远 = 低风险；朝着手切 = 高风险。") },
      { titolo: "6. Rischio alto, rischio basso · ٦. مخاطرة عالية، مخاطرة منخفضة · 6. 高风险、低风险", testo: L(
        "Guardiamo il <b>motorino</b>:<br><b>Rischio basso:</b> casco allacciato, piano, strada che conosci, di giorno.<br><b>Rischio alto:</b> senza casco, veloce, di notte, con il telefono in mano.<br>Guardiamo il <b>telefono in carica</b>:<br><b>Rischio basso:</b> caricatore originale, sul tavolo, di giorno.<br><b>Rischio alto:</b> caricatore con il filo spellato, sotto il cuscino, tutta la notte: si scalda tanto e può prendere fuoco.<br>Il rischio è più alto quando il danno è <b>più facile</b> e <b>più grave</b>.",
        "الدراجة النارية: خوذة مربوطة وسرعة بطيئة = مخاطرة منخفضة؛ بلا خوذة وبسرعة ومع الهاتف في اليد = مخاطرة عالية. الهاتف في الشحن تحت الوسادة طوال الليل = مخاطرة عالية: يسخن وقد يحترق.",
        "摩托车：系好头盔、慢慢开 = 低风险；不戴头盔、开得快、手拿手机 = 高风险。手机整夜在枕头下充电 = 高风险：会很烫，可能着火。") },
      { titolo: "7. Tutte e tre insieme · ٧. الثلاثة معاً · 7. 三个词一起看", testo: L(
        "<b>La padella in cucina.</b><br>Pericolo: l'<b>olio bollente</b>.<br>Danno: una <b>bruciatura</b> alla mano o al braccio.<br>Rischio: <b>alto</b> se il manico sporge fuori dal fornello e passa un bambino; <b>basso</b> se il manico è girato verso dentro e stai attento.<br><b>La sedia in aula.</b><br>Pericolo: la sedia che <b>dondola</b> su due gambe.<br>Danno: cadi all'indietro e <b>batti la testa</b>.<br>Rischio: <b>alto</b> se ti dondoli spesso; <b>basso</b> se stai seduto con quattro gambe a terra.",
        "المقلاة: الخطر = الزيت المغلي؛ الضرر = حرق؛ المخاطرة عالية إذا كان المقبض خارج الموقد. الكرسي: الخطر = التأرجح؛ الضرر = السقوط وضرب الرأس.",
        "平底锅：危险源 = 热油；伤害 = 烫伤；锅柄朝外时风险高。椅子：危险源 = 摇椅子；伤害 = 向后摔倒、撞到头。") },
      { titolo: "8. «Per un pelo!» · ٨. «نجوت بأعجوبة!» · 8. “差一点！”", testo: L(
        "Scivoli sul pavimento bagnato ma ti tieni al banco: <b>non ti fai niente</b>. Questo è un <b>quasi incidente</b>: il danno non c'è stato, ma il pericolo c'era davvero.<br>Che cosa fai? <b>Lo dici subito</b> (al prof, in palestra all'allenatore, al lavoro al capo), così la prossima persona non cade.<br>Chi fa sicurezza dice: <b>prima di un incidente vero ci sono tanti «per un pelo»</b>. Se li ascolti, eviti il danno.",
        "تنزلق على الأرض المبللة لكنك تمسك بالطاولة ولا تتأذى: هذا «حادث وشيك». أخبر فوراً المعلم أو المدرب أو المسؤول، حتى لا يسقط الشخص التالي.",
        "在湿地板上滑了一下，但扶住了桌子，没受伤：这是“险些发生的事故”。马上告诉老师、教练或老板，这样下一个人就不会摔倒。") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../1inf-oggi/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
    via: C("sic", L("Una cosa che PUÒ fare male si chiama…", "الشيء الذي يمكن أن يؤذي اسمه…", "可能伤人的东西叫……"), ["pericolo", "danno", "rischio"], "Il pericolo: non ha ancora fatto male, ma potrebbe."),
    prepara: [
      { q: L("Guardati intorno, qui in aula. Scrivi UNA cosa che può fare male.", "انظر حولك في القاعة. اكتب شيئاً واحداً يمكن أن يؤذي.", "看看教室四周，写一个可能伤人的东西。"), aiuto: "Anche nella tua lingua. Esempio: «il cavo sotto il mio banco».", min: 5 },
      { q: L("Pensa a casa tua, allo sport o alla strada. Scrivi un pericolo e il danno che può fare.", "فكّر في بيتك أو الرياضة أو الشارع. اكتب خطراً والضرر الذي قد يسببه.", "想想家里、运动或马路。写一个危险源和它可能造成的伤害。"), aiuto: "Anche nella tua lingua. Esempio: «l'olio bollente: una bruciatura».", min: 6 }
    ],
    allenamento: [
      S(1, C("sic", L("Il male che succede DAVVERO si chiama…", "الأذى الذي يحدث فعلاً اسمه…", "真的发生的伤叫……"), ["danno", "pericolo", "rischio"], "Il danno è già successo.")),
      S(1, C("sic", L("«Quanto è facile e quanto è grave» si chiama…", "«مدى السهولة ومدى الخطورة» اسمه…", "“有多容易发生、有多严重”叫……"), ["rischio", "danno", "pericolo"], "Il rischio.")),
      S(2, C("sic", L("Il ferro da stiro acceso è…", "المكواة المشتعلة هي…", "开着的电熨斗是……"), ["un pericolo", "un danno", "una bruciatura"], "Può bruciare: è un pericolo.")),
      S(2, C("sic", L("Domanda magica per trovare un pericolo:", "السؤال السحري لإيجاد الخطر:", "找危险源的神奇问题："), ["«Che cosa qui mi può fare male?»", "«Che ore sono?»", "«Chi ha vinto?»"], "")),
      S(3, C("sic", L("In aula di informatica, quale di questi è un pericolo?", "في قاعة الحاسوب، أيّ هذه خطر؟", "在电脑教室，哪个是危险源？"), ["un cavo per terra nel passaggio", "il mouse sul tappetino", "il libro sul banco"], "Qualcuno ci inciampa.")),
      S(3, C("sic", L("In palestra, quale di questi è un pericolo?", "في الصالة الرياضية، أيّ هذه خطر؟", "在体育馆，哪个是危险源？"), ["il pallone lasciato a terra", "la panchina al suo posto", "la porta chiusa"], "Ci metti il piede sopra e cadi.")),
      S(4, C("sic", L("Una caviglia storta è…", "التواء الكاحل هو…", "扭伤脚踝是……"), ["un danno", "un pericolo", "un rischio"], "È il male che è successo.")),
      S(4, C("sic", L("Ore e ore davanti allo schermo, senza pause. Il danno possibile è…", "ساعات أمام الشاشة بلا استراحة. الضرر الممكن هو…", "长时间看屏幕不休息，可能的伤害是……"), ["occhi stanchi e mal di testa", "una gamba rotta", "una bruciatura"], "")),
      S(5, C("sic", L("Il rischio risponde a due domande: succede facilmente? e…", "المخاطرة تجيب عن سؤالين: هل يحدث بسهولة؟ و…", "风险回答两个问题：容易发生吗？还有……"), ["quanto male fa?", "quanto costa?", "chi è stato?"], "")),
      S(6, C("sic", L("Motorino: dove il rischio è più ALTO?", "الدراجة النارية: أين المخاطرة أعلى؟", "摩托车：哪种风险更高？"), ["senza casco, veloce, di notte", "casco allacciato, piano, di giorno", "motorino fermo in garage"], "Danno più facile e più grave.")),
      S(7, C("sic", L("Padella: il manico sporge fuori dal fornello e passa un bambino. Il rischio è…", "المقلاة: المقبض خارج الموقد ويمرّ طفل. المخاطرة…", "锅柄伸出灶台，有小孩经过。风险……"), ["alto", "zero", "basso"], "Basta un urto e l'olio cade.")),
      S(8, C("sic", L("Scivoli ma non ti fai niente. Che cosa fai?", "تنزلق لكنك لا تتأذى. ماذا تفعل؟", "滑了一下但没受伤，你怎么做？"), ["lo dico subito, così il prossimo non cade", "niente, tanto non mi sono fatto male", "rido e vado via"], "È un «per un pelo»: va detto."))
    ],

    /* ---------- VERIFICA (chiusa: la apre il prof; gli stessi 20 casi sono il quiz su Moduli) ---------- */
    crocette: [
      C("sic", L("In aula, un cavo della corrente passa per terra tra i banchi. Il cavo è…", "في القاعة، سلك كهرباء على الأرض بين الطاولات. السلك هو…", "教室里，一根电线从桌子之间的地上穿过。这根电线是……"), ["un pericolo: qualcuno può inciampare", "un danno", "niente di importante", "una protezione"], "", "pericolo"),
      C("sic", L("Un compagno inciampa nel cavo e si sbuccia il ginocchio. Il ginocchio sbucciato è…", "زميل يتعثر بالسلك ويجرح ركبته. الركبة المجروحة هي…", "同学被电线绊倒，膝盖擦破了。擦破的膝盖是……"), ["il danno", "il pericolo", "il rischio", "un quasi incidente"], "", "danno"),
      C("sic", L("A casa, la padella con l'olio bollente sul fuoco è…", "في البيت، المقلاة بالزيت المغلي على النار هي…", "家里，火上装着热油的锅是……"), ["un pericolo", "un danno", "una bruciatura", "un rischio zero"], "", "pericolo"),
      C("sic", L("Ti cade un po' di olio bollente sulla mano. La bruciatura è…", "يسقط زيت مغلي على يدك. الحرق هو…", "热油溅到你手上，烫伤是……"), ["un danno", "un pericolo", "un rischio", "una cosa che può succedere"], "", "danno"),
      C("sic", L("Che cosa vuol dire «rischio ALTO»?", "ماذا تعني «مخاطرة عالية»؟", "“高风险”是什么意思？"), ["il danno è facile che succeda, e può essere grave", "la cosa è in alto, su uno scaffale", "il danno è già successo", "non succede mai niente"], "", "rischio"),
      C("sic", L("Tre ragazzi in motorino. Chi ha il rischio più ALTO?", "ثلاثة شباب على دراجات نارية. من مخاطرته أعلى؟", "三个骑摩托车的年轻人，谁的风险最高？"), ["senza casco, veloce, con il telefono in mano", "casco allacciato, piano, di giorno", "casco allacciato, si ferma al rosso", "motorino spento, a piedi accanto"], "", "altobasso"),
      C("sic", L("Il telefono è in carica sotto il cuscino tutta la notte e diventa caldissimo. Il rischio è…", "الهاتف يُشحن تحت الوسادة طوال الليل ويصبح ساخناً جداً. المخاطرة…", "手机整夜在枕头下充电，变得很烫。风险……"), ["alto: si può bruciare o prendere fuoco", "zero: il telefono non fa male", "basso: è solo caldo", "non c'entra la sicurezza"], "", "altobasso"),
      C("sic", L("In palestra il pavimento è bagnato. Qual è il pericolo?", "في الصالة الرياضية الأرض مبللة. ما الخطر؟", "体育馆地板是湿的。危险源是什么？"), ["scivolare e cadere", "avere sete", "perdere la partita", "sporcare le scarpe"], "", "pericolo"),
      C("sic", L("Lo stesso coltello. Quando il rischio è più BASSO?", "نفس السكين. متى تكون المخاطرة أقل؟", "同一把刀，什么时候风险最低？"), ["taglio sul tagliere, con le dita lontane dalla lama", "taglio il pane tenendolo in mano, verso la mano", "corro in cucina con il coltello in mano", "lo lascio sul bordo del tavolo"], "", "rischio"),
      C("sic", L("In aula ti dondoli sulla sedia, sulle due gambe dietro. Quale danno può succedere?", "تتأرجح على الكرسي على الرجلين الخلفيتين. ما الضرر الممكن؟", "你在教室里摇椅子，只用后面两条腿。可能发生什么伤害？"), ["cadi all'indietro e batti la testa", "si scarica il PC", "ti viene fame", "nessuno, mai"], "", "insieme"),
      C("sic", L("Nel laboratorio vedi una presa rotta con i fili che si vedono. Che cosa fai?", "في المختبر ترى مقبساً مكسوراً والأسلاك ظاهرة. ماذا تفعل؟", "在机房里你看到一个坏插座，电线露出来了。你怎么做？"), ["non la tocco e lo dico subito al prof", "provo a ripararla con le mani", "ci attacco lo stesso il caricatore", "faccio finta di niente"], "", "pericolo"),
      C("sic", L("Giochi al PC per 4 ore senza mai alzare gli occhi. Quale danno è possibile?", "تلعب على الحاسوب ٤ ساعات دون أن ترفع عينيك. ما الضرر الممكن؟", "你玩电脑 4 个小时，眼睛从不离开屏幕。可能有什么伤害？"), ["occhi stanchi, mal di testa e mal di schiena", "una scossa elettrica", "un taglio al dito", "nessun danno, mai"], "", "danno"),
      C("sic", L("Vai in bici di sera, senza luci e vestito di nero. Qual è il pericolo più grande?", "تركب الدراجة مساءً بلا أضواء وبملابس سوداء. ما الخطر الأكبر؟", "晚上骑自行车，没有灯，穿黑衣服。最大的危险源是什么？"), ["le macchine non ti vedono", "si sgonfia la gomma", "fa freddo", "arrivi in ritardo"], "", "pericolo"),
      C("sic", L("Lavoretto: aiuti a dipingere una parete e sali su una sedia con le ruote. Il rischio è…", "عمل صغير: تساعد في طلاء حائط وتصعد على كرسي بعجلات. المخاطرة…", "打零工：你帮忙刷墙，站在带轮子的椅子上。风险……"), ["alto: la sedia scappa e cadi", "basso: le ruote tengono ferma la sedia", "zero: è solo una sedia", "uguale a stare con i piedi per terra"], "", "altobasso"),
      C("sic", L("Scivoli sul bagnato ma ti tieni al banco e non ti fai niente. Questo è…", "تنزلق على الأرض المبللة لكنك تمسك بالطاولة ولا تتأذى. هذا…", "你在湿地上滑了一下，但扶住桌子，没受伤。这是……"), ["un quasi incidente: il pericolo c'era, lo dico", "niente: non è successo niente", "un danno grave", "una protezione"], "", "pelo"),
      C("sic", L("Pericolo e rischio sono la stessa cosa?", "هل الخطر والمخاطرة نفس الشيء؟", "危险源和风险是一样的吗？"), ["No: il pericolo è la cosa, il rischio è quanto è facile e grave il danno", "Sì, sono due parole uguali", "No: il rischio è il male già successo", "Sì, ma solo al lavoro"], "", "rischio"),
      C("sic", L("Dopo la partita qualcuno lascia il pallone in mezzo al campo. Il pallone a terra è…", "بعد المباراة يترك أحدهم الكرة وسط الملعب. الكرة على الأرض هي…", "比赛后有人把球留在场地中间。地上的球是……"), ["un pericolo: qualcuno ci mette il piede e cade", "un danno", "una protezione", "niente: è solo un pallone"], "", "pericolo"),
      C("sic", L("Due caricatori: A) originale, sul tavolo. B) filo spellato, sul letto. Dove il rischio è più ALTO?", "شاحنان: أ) أصلي على الطاولة. ب) سلك مقشور على السرير. أين المخاطرة أعلى؟", "两个充电器：A）原装，放在桌上。B）电线破皮，放在床上。哪个风险更高？"), ["B: filo spellato sul letto", "A: originale sul tavolo", "sono uguali", "nessuno dei due"], "", "altobasso"),
      C("sic", L("Lo stesso danno, la caviglia storta. Dove è più FACILE che succeda?", "نفس الضرر، التواء الكاحل. أين يحدث بسهولة أكبر؟", "同样的伤害，扭伤脚踝。在哪里更容易发生？"), ["correndo in aula tra zaini e cavi per terra", "camminando in un corridoio libero", "stando seduto al banco", "leggendo un libro"], "", "rischio"),
      C("sic", L("Ti fai male al dito con la porta e ti esce un po' di sangue. Che cosa è il dito che sanguina?", "تؤذي إصبعك بالباب ويخرج قليل من الدم. ما هو الإصبع النازف؟", "你的手指被门夹了，流了一点血。流血的手指是……"), ["il danno", "il pericolo", "il rischio", "un quasi incidente"], "", "danno")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti sicuro, adesso, con pericolo, danno e rischio?", "ما مدى ثقتك الآن بالخطر والضرر والمخاطرة؟", "你现在对危险源、伤害和风险有多大把握？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "mia", tema: "dove", q: L("LA TUA AULA, ADESSO. Guardati intorno. Scrivi UN pericolo che vedi (che cosa è e dove è) e il danno che può fare.", "قاعتك الآن. انظر حولك. اكتب خطراً واحداً تراه (ما هو وأين هو) والضرر الذي قد يسببه.", "你的教室，现在。看看四周。写一个你看到的危险源（是什么、在哪里）和它可能造成的伤害。"), aiuto: "Almeno 12 parole. Puoi scrivere anche nella tua lingua.", min_parole: 12,
        criteri: "pericolo concreto e reale della propria aula, con il posto; danno coerente" },
      { area: "mia", tema: "altobasso", q: L("LA TUA VITA. Pensa a casa, allo sport, alla strada o a un lavoretto. Scrivi un pericolo, il danno che può fare e se il rischio è alto o basso. Perché?", "حياتك. فكّر في البيت أو الرياضة أو الشارع أو عمل صغير. اكتب خطراً والضرر الممكن، وهل المخاطرة عالية أم منخفضة، ولماذا؟", "你的生活。想想家里、运动、马路或打零工。写一个危险源、可能的伤害，风险高还是低，为什么？"), aiuto: "Almeno 15 parole. Puoi scrivere anche nella tua lingua.", min_parole: 15,
        criteri: "situazione propria; pericolo e danno distinti; rischio alto o basso motivato con «facile» e «grave»" }
    ],

    /* ---------- RECUPERO ---------- */
    recupero: [
      C("sic", L("Il coltello sul tavolo è…", "السكين على الطاولة هو…", "桌上的刀是……"), ["un pericolo", "un danno", "un taglio"], "", "pericolo"),
      C("sic", L("Il taglio al dito è…", "الجرح في الإصبع هو…", "手指上的伤口是……"), ["un danno", "un pericolo", "un rischio"], "", "danno"),
      C("sic", L("Il rischio è…", "المخاطرة هي…", "风险是……"), ["quanto è facile e grave il danno", "il male già successo", "un attrezzo"], "", "rischio"),
      C("sic", L("Quale ha il rischio più alto?", "أيّها مخاطرته أعلى؟", "哪个风险更高？"), ["bici di notte senza luci", "bici di giorno con le luci", "bici ferma in cortile"], "", "altobasso"),
      C("sic", L("Uno zaino in mezzo al passaggio è…", "حقيبة وسط الممر هي…", "过道中间的书包是……"), ["un pericolo", "un danno", "una protezione"], "", "dove"),
      C("sic", L("Pericolo: olio bollente. Il danno è…", "الخطر: زيت مغلي. الضرر هو…", "危险源：热油。伤害是……"), ["una bruciatura", "una gamba rotta", "la fame"], "", "insieme"),
      C("sic", L("«Per un pelo», non ti sei fatto niente. Che cosa fai?", "«نجوت بأعجوبة» ولم تتأذَّ. ماذا تفعل؟", "“差一点”，你没受伤。你怎么做？"), ["lo dico subito", "niente", "lo rifaccio"], "", "pelo"),
      C("sic", L("Pericolo, danno, rischio: per oggi le parole sono…", "الخطر، الضرر، المخاطرة: كلمات اليوم…", "危险源、伤害、风险：今天的词是……"), ["tre", "una", "dieci"], "", "tre")
    ]
  };
})();
