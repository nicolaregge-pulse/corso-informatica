// 1INF · Sicurezza sul lavoro, 3ª ora (formazione generale): Sicurezza 3: prevenzione aziendale.
// Generata il 29/10/2026 da gen.py (contenuti come la 2INF, adattati alla 1INF: casi di vita, niente leggi, italiano + arabo + cinese).
// Nessun link a siti esterni tranne il nostro quiz su Google Moduli (#136).
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function L(it, ar, zh) { return it + '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">' + ar + '</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">' + zh + '</span>'; }
  window.BANCA = {
    id: "1inf-sicurezza-3ora-v1",
    classe: "1INF",
    titolo: "Sicurezza 3: prevenzione aziendale · الوقاية في الشركة · 企业中的预防",
    sotto: "1INF · 30/10/2026 · sicurezza, 3ª lezione · chi si occupa della sicurezza al lavoro · teoria, ripasso e quiz",
    stato: "stato/1inf-sicurezza-3ora.json",
    risultati: "risultati.html?b=1inf-sicurezza-3ora",
    minuti: 25,
    anteprima: "868848605",
    aree: {
      sic: { nome: "Organizzazione della prevenzione", peso: 80 },
      mia: { nome: "Nella mia vita (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: {"ripasso": 1, "squadra": 2, "capo": 3, "esperti": 4, "rls": 5, "dvr": 6, "emergenze": 7, "formazione": 8},
    schede: [
      { titolo: "1. Ripasso in un minuto · مراجعة في دقيقة · 1. 一分钟复习", testo: L("Ripasso della volta scorsa:<br><b>PREVENZIONE</b> = il danno succede <b>meno spesso</b>.<br><b>PROTEZIONE</b> = se il danno succede, fa <b>meno male</b>.<br>Regola d'oro: <b>prima</b> togli il pericolo, <b>poi</b> proteggiti.<br>Oggi impari <b>chi</b> si occupa della sicurezza al lavoro.", "مراجعة: الوقاية = الضرر يحدث أقل. الحماية = إذا حدث الضرر يؤذي أقل. القاعدة الذهبية: أزل الخطر أولاً، ثم احمِ نفسك. اليوم تتعلم من يهتم بالسلامة في العمل.", "复习：预防 = 伤害发生得更少。防护 = 伤害发生时伤得更轻。黄金法则：先去掉危险，再保护自己。今天学习：在工作中谁负责安全。") },
      { titolo: "2. La sicurezza è una squadra · السلامة فريق · 2. 安全是一个团队", testo: L("In una squadra di calcio ognuno ha il suo <b>ruolo</b>: l'allenatore, il capitano, il medico, i giocatori.<br>Al lavoro è uguale: la sicurezza la fa una <b>squadra</b>, e ognuno ha il suo compito.<br>Anche <b>tu</b>, lavoratore o studente in <b>stage</b>, fai parte della squadra.", "في فريق كرة القدم لكل واحد دوره: المدرب، القائد، الطبيب، اللاعبون. في العمل الأمر نفسه: السلامة يصنعها فريق، ولكل واحد مهمته. وأنت أيضاً، عاملاً أو طالباً في التدريب، جزء من الفريق.", "足球队里每个人都有自己的角色：教练、队长、队医、球员。工作中也一样：安全由一个团队来做，每个人都有自己的任务。你也是团队的一员，不管你是工人还是实习学生。") },
      { titolo: "3. Il datore di lavoro e il preposto · صاحب العمل والمشرف · 3. 雇主和班组长", testo: L("Il <b>DATORE DI LAVORO</b> è il capo dell'azienda: <b>decide</b>, paga le cose per la sicurezza e <b>risponde</b> se qualcosa va male.<br>Il <b>PREPOSTO</b> è il capo-reparto: sta <b>sul campo</b> con i lavoratori e <b>controlla</b> che usino le protezioni. Se vede un pericolo, ferma il lavoro.<br>In laboratorio, a scuola, il prof fa un po' da preposto.", "صاحب العمل هو رئيس الشركة: يقرّر، ويدفع ثمن أشياء السلامة، ويتحمّل المسؤولية إذا حدث خطأ. المشرف (preposto) هو رئيس القسم: يكون في الميدان مع العمال ويراقب أنهم يستعملون وسائل الحماية. إذا رأى خطراً يوقف العمل. في مختبر المدرسة، المعلم يقوم قليلاً بدور المشرف.", "雇主（datore di lavoro）是公司的老板：他做决定，为安全花钱，出了问题要负责。班组长（preposto）是部门负责人：他在现场和工人在一起，检查大家是否使用防护。看到危险时，他会停止工作。在学校实验室里，老师有点像班组长。") },
      { titolo: "4. Gli esperti: RSPP e medico · الخبراء: RSPP والطبيب · 4. 专家：RSPP 和医生", testo: L("L'<b>RSPP</b> è l'<b>esperto</b> della sicurezza: studia i rischi di ogni lavoro e <b>propone</b> le soluzioni al capo.<br>Il <b>MEDICO COMPETENTE</b> è il medico dell'azienda: fa le <b>visite</b> ai lavoratori e dice se uno può fare quel lavoro.<br>La visita è <b>gratis</b> e si fa in orario di lavoro.", "الـ RSPP هو خبير السلامة: يدرس مخاطر كل عمل ويقترح الحلول على صاحب العمل. الطبيب المختص هو طبيب الشركة: يفحص العمال ويقول إن كان الشخص يستطيع القيام بذلك العمل. الفحص مجاني ويتم في وقت العمل.", "RSPP 是安全专家：他研究每项工作的风险，并向老板提出解决办法。职业医生（medico competente）是公司的医生：他给工人做体检，并判断一个人能不能做这项工作。体检免费，在工作时间内进行。") },
      { titolo: "5. L'RLS: la voce dei lavoratori · الـ RLS: صوت العمال · 5. RLS：工人的声音", testo: L("L'<b>RLS</b> è un <b>lavoratore</b> come gli altri, <b>eletto dai colleghi</b>.<br>È la loro <b>voce</b>: porta al capo i problemi di sicurezza, controlla e fa domande.<br>Se vedi un pericolo e hai paura di dirlo al capo, puoi dirlo all'<b>RLS</b>.<br>A scuola è come il <b>rappresentante di classe</b>.", "الـ RLS عامل مثل الآخرين، ينتخبه زملاؤه. هو صوتهم: ينقل إلى صاحب العمل مشاكل السلامة، يراقب ويسأل. إذا رأيت خطراً وخفت أن تقوله للرئيس، تستطيع أن تقوله للـ RLS. في المدرسة هو مثل ممثّل الصف.", "RLS 是一名普通工人，由同事选出来。他是工人们的声音：把安全问题告诉老板，检查并提问。如果你看到危险，又不敢告诉老板，可以告诉 RLS。在学校里，他就像班级代表。") },
      { titolo: "6. Il DVR: il quaderno dei rischi · الـ DVR: دفتر المخاطر · 6. DVR：风险本子", testo: L("Il <b>DVR</b> (Documento di Valutazione dei Rischi) è il <b>quaderno dei rischi</b> dell'azienda.<br>Dentro c'è scritto <b>quali rischi</b> ci sono in ogni lavoro e <b>che cosa si fa</b> per abbassarli.<br>Lo fa il datore di lavoro, con l'RSPP e il medico. Si <b>aggiorna</b> quando cambia qualcosa: una macchina nuova, un reparto nuovo, dopo un infortunio.", "الـ DVR (وثيقة تقييم المخاطر) هو دفتر المخاطر في الشركة. مكتوب فيه ما هي المخاطر في كل عمل وماذا نفعل لتخفيضها. يكتبه صاحب العمل مع الـ RSPP والطبيب. يُحدَّث عندما يتغير شيء: آلة جديدة، قسم جديد، بعد إصابة.", "DVR（风险评估文件）是公司的“风险本子”。里面写着每项工作有哪些风险，以及做什么来降低风险。由雇主和 RSPP、医生一起完成。有变化时要更新：新机器、新部门、发生工伤以后。") },
      { titolo: "7. Le emergenze · حالات الطوارئ · 7. 紧急情况", testo: L("In ogni azienda (e a scuola) ci sono gli <b>addetti alle emergenze</b>: quelli dell'<b>antincendio</b> (usano l'estintore) e quelli del <b>primo soccorso</b> (aiutano chi si fa male e chiamano il <b>112</b>).<br>Se suona l'allarme: segui il cartello <b>verde</b> dell'uscita e vai al <b>punto di raccolta</b>.<br><b>Niente ascensore, non correre, non tornare indietro</b> a prendere le cose.", "في كل شركة (وفي المدرسة) يوجد مسؤولو الطوارئ: مسؤولو مكافحة الحريق (يستعملون طفاية الحريق) ومسؤولو الإسعافات الأولية (يساعدون المصاب ويتصلون بالرقم 112). إذا رنّ الإنذار: اتبع اللافتة الخضراء للمخرج واذهب إلى نقطة التجمع. لا مصعد، لا ركض، لا تعد إلى الخلف لتأخذ أغراضك.", "每个公司（和学校）都有应急人员：消防员（会用灭火器）和急救员（帮助受伤的人，并拨打 112）。警报响了：跟着绿色的出口标志走，到集合点去。不坐电梯，不跑，不回去拿东西。") },
      { titolo: "8. Informazione, formazione, addestramento · الإعلام، التكوين، التدريب العملي · 8. 告知、培训、实操训练", testo: L("<b>INFORMAZIONE</b>: ti dicono quali rischi ci sono e chi sono le persone della sicurezza.<br><b>FORMAZIONE</b>: un corso per capire, come questo.<br><b>ADDESTRAMENTO</b>: provi davvero, con le mani, l'attrezzo o il DPI, con qualcuno che ti guarda.<br>Sono <b>gratis</b>, in orario di lavoro, anche per lo studente in <b>stage</b>.", "الإعلام: يقولون لك ما هي المخاطر ومن هم أشخاص السلامة. التكوين: دورة لتفهم، مثل هذه. التدريب العملي: تجرّب فعلاً بيديك الأداة أو وسيلة الحماية، وشخص يراقبك. كلها مجانية، في وقت العمل، وأيضاً للطالب في التدريب.", "告知：告诉你有哪些风险，谁是负责安全的人。培训：一门帮你理解的课，就像这门课。实操训练：在别人看着的情况下，你亲手试用工具或防护装备。这些都免费，在工作时间内进行，实习学生也一样。") + "<!--QUIZNUOVO--><div style=\"margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px\"><p><b>FINE DELLE SCHEDE · نهاية البطاقات · 卡片结束</b></p><p>Fai il ripasso qui sotto. · راجِع. · 做复习。</p><p><b>Sul quaderno ricopia:</b> RLS = il lavoratore eletto dai colleghi: è la loro voce. DVR = il documento con tutti i rischi e che cosa si fa per abbassarli. REGOLA D'ORO: allarme = niente ascensore, non correre, vai al punto di raccolta.</p><p lang=\"ar\" dir=\"rtl\">انسخ في الدفتر: RLS = العامل الذي ينتخبه زملاؤه، هو صوتهم. DVR = الوثيقة التي فيها كل المخاطر وما نفعله لتخفيضها. القاعدة الذهبية: إنذار = لا مصعد، لا ركض، اذهب إلى نقطة التجمع.</p><p lang=\"zh\">抄在本子上：RLS = 同事选出的工人，是大家的声音。DVR = 写着所有风险以及如何降低风险的文件。黄金法则：警报 = 不坐电梯，不跑，去集合点。</p></div><!--/QUIZNUOVO-->" }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../1inf-oggi/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
    via: C("sic", L("Al lavoro, chi fa le visite ai lavoratori?", "في العمل، من يفحص العمال؟", "在工作中，谁给工人做体检？"), ["il medico competente", "il preposto", "il cliente"], "Il medico competente fa le visite.", "esperti"),
    prepara: [
      { q: L("Pensa alla scuola. Scrivi UNA persona che si occupa della sicurezza qui e che cosa fa.", "فكّر في المدرسة. اكتب شخصاً واحداً يهتم بالسلامة هنا وماذا يفعل.", "想想学校。写一个在这里负责安全的人，以及他做什么。"), aiuto: "Anche nella tua lingua. Esempio: «il prof di laboratorio controlla che i cavi siano a posto».", min: 4 },
      { q: L("Se suona l'allarme in aula, che cosa fai? Scrivi 2 cose.", "إذا رنّ الإنذار في القاعة، ماذا تفعل؟ اكتب شيئين.", "如果教室里警报响了，你怎么做？写两件事。"), aiuto: "Anche nella tua lingua. Esempio: «esco senza correre, vado al punto di raccolta».", min: 4 }
    ],
    allenamento: [
      S(1, C("sic", L("PROTEZIONE vuol dire…", "الحماية تعني…", "防护的意思是……"), ["se il danno succede, fa meno male", "il danno succede meno spesso", "il danno è già successo"], "Protezione: il danno è meno grave.", "")),
      S(2, C("sic", L("Al lavoro la sicurezza la fa…", "في العمل السلامة يصنعها…", "在工作中，安全由谁来做？"), ["una squadra, dove ognuno ha il suo compito", "solo il capo", "nessuno"], "È un lavoro di squadra.", "")),
      S(3, C("sic", L("Chi decide e risponde della sicurezza in azienda?", "من يقرّر ويتحمّل مسؤولية السلامة في الشركة؟", "在公司里谁对安全做决定并负责？"), ["il datore di lavoro", "il cliente", "il nuovo arrivato"], "Il datore di lavoro è il primo responsabile.", "")),
      S(3, C("sic", L("Il preposto è…", "المشرف (preposto) هو…", "班组长（preposto）是……"), ["il capo-reparto che controlla sul campo", "il medico", "il cliente"], "Sta con i lavoratori e controlla.", "")),
      S(4, C("sic", L("L'RSPP…", "الـ RSPP…", "RSPP……"), ["studia i rischi e propone le soluzioni", "fa le visite mediche", "ripara le macchine"], "È l'esperto della sicurezza.", "")),
      S(4, C("sic", L("Chi fa le visite ai lavoratori?", "من يفحص العمال؟", "谁给工人做体检？"), ["il medico competente", "l'RLS", "il preposto"], "Il medico dell'azienda.", "")),
      S(5, C("sic", L("L'RLS è…", "الـ RLS هو…", "RLS 是……"), ["un lavoratore eletto dai colleghi", "il capo dell'azienda", "un ispettore"], "È la voce dei lavoratori.", "")),
      S(5, C("sic", L("Hai paura di dire un pericolo al capo. A chi lo puoi dire?", "تخاف أن تقول خطراً للرئيس. لمن تستطيع أن تقوله؟", "你不敢把危险告诉老板。你可以告诉谁？"), ["all'RLS", "a nessuno", "al cliente"], "L'RLS porta il problema al capo.", "")),
      S(6, C("sic", L("Il DVR è…", "الـ DVR هو…", "DVR 是……"), ["il documento con tutti i rischi e che cosa si fa", "il contratto di lavoro", "la busta paga"], "È il quaderno dei rischi.", "")),
      S(6, C("sic", L("Il DVR si aggiorna quando…", "يُحدَّث الـ DVR عندما…", "DVR 什么时候更新？"), ["arriva una macchina nuova", "mai", "solo a Natale"], "Cambia qualcosa: si aggiorna.", "")),
      S(7, C("sic", L("Suona l'allarme antincendio. Che cosa fai?", "رنّ إنذار الحريق. ماذا تفعل؟", "火警响了。你怎么做？"), ["scendo dalle scale e vado al punto di raccolta", "prendo l'ascensore", "torno a prendere lo zaino"], "Niente ascensore, niente cose.", "")),
      S(7, C("sic", L("Il numero per le emergenze è…", "رقم الطوارئ هو…", "紧急电话是……"), ["112", "000", "1234"], "112: il numero unico.", "")),
      S(8, C("sic", L("Provi davvero l'attrezzo, con qualcuno che ti guarda. Questo è…", "تجرّب الأداة فعلاً وشخص يراقبك. هذا…", "你在别人看着下亲手试用工具。这是……"), ["addestramento", "informazione", "una vacanza"], "Addestramento: provi con le mani.", ""))
    ],
    /* ---------- VERIFICA (chiusa: gli stessi 20 casi sono il quiz su Moduli) ---------- */
    crocette: [
      C("sic", L("In azienda, chi è il primo responsabile della sicurezza?", "في الشركة، من هو المسؤول الأول عن السلامة؟", "在公司里，谁是安全的第一责任人？"), ["il datore di lavoro", "il lavoratore più giovane", "il cliente", "il fornitore"], "", "squadra"),
      C("sic", L("Il preposto vede un operaio alla mola senza occhiali. Che cosa fa?", "المشرف يرى عاملاً عند آلة الجلخ بلا نظارات. ماذا يفعل؟", "班组长看到一个工人在砂轮机旁没戴护目镜。他怎么做？"), ["lo ferma e gli fa mettere gli occhiali", "fa finta di niente", "lo lascia lavorare più in fretta", "se ne va a casa"], "", "capo"),
      C("sic", L("Chi studia i rischi di ogni lavoro e propone le soluzioni al capo?", "من يدرس مخاطر كل عمل ويقترح الحلول على الرئيس؟", "谁研究每项工作的风险，并向老板提出解决办法？"), ["l'RSPP", "il medico competente", "il cliente", "il nuovo arrivato"], "", "esperti"),
      C("sic", L("Prima di lavorare in un magazzino fai una visita. Chi la fa?", "قبل العمل في مستودع تقوم بفحص طبي. من يقوم به؟", "在仓库工作前你要做体检。谁来做？"), ["il medico competente", "l'RLS", "il preposto", "un collega"], "", "esperti"),
      C("sic", L("La visita del medico competente…", "فحص الطبيب المختص…", "职业医生的体检……"), ["è gratis e si fa in orario di lavoro", "la paga il lavoratore", "si fa la domenica", "serve solo ai capi"], "", "esperti"),
      C("sic", L("Chi elegge l'RLS?", "من ينتخب الـ RLS؟", "谁选出 RLS？"), ["i lavoratori, cioè i colleghi", "il datore di lavoro", "il medico", "i clienti"], "", "rls"),
      C("sic", L("Vedi una scala rotta in magazzino e il capo non ti ascolta. A chi puoi dirlo?", "ترى سلّماً مكسوراً في المستودع والرئيس لا يسمعك. لمن تستطيع أن تقول؟", "你看到仓库里的梯子坏了，老板不听你说。你可以告诉谁？"), ["all'RLS", "a nessuno", "a un cliente", "lo scrivo sui social"], "", "rls"),
      C("sic", L("A scuola, chi assomiglia di più all'RLS?", "في المدرسة، من يشبه الـ RLS أكثر؟", "在学校里，谁最像 RLS？"), ["il rappresentante di classe", "il preside", "il prof di matematica", "il compagno nuovo"], "", "rls"),
      C("sic", L("Che cosa c'è scritto nel DVR?", "ماذا مكتوب في الـ DVR؟", "DVR 里写着什么？"), ["i rischi di ogni lavoro e che cosa si fa per abbassarli", "gli stipendi", "gli orari del bar", "le ferie"], "", "dvr"),
      C("sic", L("L'azienda compra una macchina nuova. Il DVR…", "الشركة تشتري آلة جديدة. الـ DVR…", "公司买了一台新机器。DVR……"), ["si aggiorna", "resta uguale per sempre", "si butta via", "lo scrive il cliente"], "", "dvr"),
      C("sic", L("Chi fa il DVR?", "من يكتب الـ DVR؟", "谁来做 DVR？"), ["il datore di lavoro, con l'RSPP e il medico", "il lavoratore nuovo, da solo", "il cliente", "nessuno"], "", "dvr"),
      C("sic", L("Suona l'allarme antincendio a scuola. Che cosa fai?", "رنّ إنذار الحريق في المدرسة. ماذا تفعل؟", "学校火警响了。你怎么做？"), ["esco con calma, seguo il cartello verde, vado al punto di raccolta", "prendo l'ascensore", "corro e spingo gli altri", "torno in aula a prendere il telefono"], "", "emergenze"),
      C("sic", L("Il cartello dell'uscita di emergenza è di colore…", "لافتة مخرج الطوارئ لونها…", "紧急出口标志是什么颜色？"), ["verde", "rosso", "giallo", "viola"], "", "emergenze"),
      C("sic", L("Un compagno cade e batte forte la testa. Che cosa fai?", "زميل يسقط ويضرب رأسه بقوة. ماذا تفعل؟", "一个同学摔倒，头撞得很重。你怎么做？"), ["chiamo subito un adulto o l'addetto al primo soccorso (o il 112)", "lo tiro su di forza", "gli faccio una foto", "me ne vado"], "", "emergenze"),
      C("sic", L("In azienda, chi usa l'estintore?", "في الشركة، من يستعمل طفاية الحريق؟", "在公司里，谁使用灭火器？"), ["l'addetto antincendio, che ha fatto il corso", "il cliente", "il fornitore", "nessuno, mai"], "", "emergenze"),
      C("sic", L("Dopo che siete usciti, dove si aspetta?", "بعد الخروج، أين ننتظر؟", "大家出来以后，在哪里等？"), ["al punto di raccolta, fuori dall'edificio", "in bagno", "in ascensore", "sulle scale"], "", "emergenze"),
      C("sic", L("Questo corso sulla sicurezza è…", "هذه الدورة عن السلامة هي…", "这门安全课是……"), ["formazione", "addestramento", "una multa", "una vacanza"], "", "formazione"),
      C("sic", L("Ti spiegano quali rischi ci sono e chi sono le persone della sicurezza. Questo è…", "يشرحون لك ما هي المخاطر ومن هم أشخاص السلامة. هذا…", "有人告诉你有哪些风险、谁负责安全。这是……"), ["informazione", "addestramento", "una sanzione", "il DVR"], "", "formazione"),
      C("sic", L("Chi paga la formazione sulla sicurezza?", "من يدفع ثمن التكوين في السلامة؟", "谁支付安全培训的费用？"), ["l'azienda: per il lavoratore è gratis", "il lavoratore", "i genitori", "il cliente"], "", "formazione"),
      C("sic", L("Sei in stage in un'officina. La formazione sulla sicurezza…", "أنت في تدريب في ورشة. التكوين في السلامة…", "你在一个车间实习。安全培训……"), ["vale anche per te", "è solo per i dipendenti", "non serve agli studenti", "la fai quando vuoi tu"], "", "formazione")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti sicuro, adesso, con le persone della sicurezza?", "ما مدى ثقتك الآن بأشخاص السلامة؟", "你现在对负责安全的人了解多少？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "mia", tema: "squadra", q: L("LA SQUADRA. Scegli UNA persona della squadra della sicurezza (datore di lavoro, preposto, RSPP, medico, RLS). Scrivi con parole tue che cosa fa.", "الفريق. اختر شخصاً واحداً من فريق السلامة (صاحب العمل، المشرف، RSPP، الطبيب، RLS). اكتب بكلماتك ماذا يفعل.", "团队。从安全团队中选一个人（雇主、班组长、RSPP、医生、RLS）。用你自己的话写他做什么。"),
        criteri: "ruolo della squadra corretto e compito coerente" },
      { area: "mia", tema: "emergenze", q: L("L'EMERGENZA. Suona l'allarme mentre sei in laboratorio. Scrivi che cosa fai, passo per passo.", "الطوارئ. يرنّ الإنذار وأنت في المختبر. اكتب ماذا تفعل خطوة بخطوة.", "紧急情况。你在实验室时警报响了。一步一步写你怎么做。"),
        criteri: "uscita con calma, niente ascensore, cartello verde, punto di raccolta, non tornare indietro" }
    ],
    /* ---------- RECUPERO ---------- */
    recupero: [
      C("sic", L("Il primo responsabile della sicurezza è…", "المسؤول الأول عن السلامة هو…", "安全的第一责任人是……"), ["il datore di lavoro", "il cliente", "nessuno"], "", "squadra"),
      C("sic", L("Chi controlla sul campo?", "من يراقب في الميدان؟", "谁在现场检查？"), ["il preposto", "il medico", "il cliente"], "", "capo"),
      C("sic", L("Le visite le fa…", "الفحوص يقوم بها…", "体检由谁做？"), ["il medico competente", "l'RLS", "il preposto"], "", "esperti"),
      C("sic", L("L'RLS è eletto da…", "الـ RLS ينتخبه…", "RLS 由谁选出？"), ["i colleghi", "il capo", "i clienti"], "", "rls"),
      C("sic", L("Nel DVR ci sono…", "في الـ DVR يوجد…", "DVR 里有……"), ["i rischi e che cosa si fa", "gli stipendi", "le ferie"], "", "dvr"),
      C("sic", L("Allarme: l'ascensore…", "إنذار: المصعد…", "警报：电梯……"), ["non si prende", "si prende", "si aspetta"], "", "emergenze"),
      C("sic", L("Il numero delle emergenze è…", "رقم الطوارئ هو…", "紧急电话是……"), ["112", "000", "1234"], "", "emergenze"),
      C("sic", L("La formazione sulla sicurezza è…", "التكوين في السلامة…", "安全培训……"), ["gratis", "a pagamento", "vietata"], "", "formazione")
    ]
  };
})();
