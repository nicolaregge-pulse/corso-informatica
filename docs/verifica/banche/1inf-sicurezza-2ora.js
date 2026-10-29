// 1INF · Sicurezza sul lavoro, 2ª lezione (29/10/2026, 13:00-14:00): PREVENZIONE e PROTEZIONE con casi della loro vita.
// Preparata la mattina del 29/10 dall'ossatura classe-1/sicurezza-1ora/ossatura-2a-lezione.md (generatore: gen_sic2.py).
// Come la 1ª: niente leggi né regolamento, nessun link a siti esterni; italiano semplicissimo + una riga in arabo e in cinese.
// Tempi (errore #102): 8 schede ~12 min, ripasso 13 domande ~13 min, «prepara» ~4 min, verifica 20 casi ~20 min (= quiz su Moduli).
(function () {
  function C(area, q, o, spiega, tema) { return { tipo: "c", area: area, tema: tema || "", q: q, o: o, a: 0, spiega: spiega }; }
  function S(n, q) { q.scheda = n; return q; }
  function L(it, ar, zh) { return it + '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">' + ar + '</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">' + zh + '</span>'; }
  window.BANCA = {
    id: "1inf-sicurezza-2ora-v1",
    classe: "1INF",
    titolo: "Sicurezza 2: prevenzione e protezione · الوقاية والحماية · 预防和防护",
    sotto: "1INF · 29/10/2026 · sicurezza, 2ª lezione · casi veri: aula, casa, strada, sport, lavoretti · teoria, ripasso e quiz",
    stato: "stato/1inf-sicurezza-2ora.json",
    risultati: "risultati.html?b=1inf-sicurezza-2ora",
    minuti: 25,
    anteprima: "868848605",
    aree: {
      sic: { nome: "Prevenzione e protezione", peso: 80 },
      mia: { nome: "Nella mia vita (parole tue)", peso: 20 },
      parere: { nome: "Il tuo parere (non conta per il voto)", peso: 0 }
    },
    schede_temi: {"ripasso": 1, "due": 2, "casa": 3, "strada": 4, "protezione": 5, "tutti": 6, "prima": 7, "schermo": 8},
    schede: [
      { titolo: "1. Ripasso in un minuto · ١. مراجعة في دقيقة · 1. 一分钟复习", testo: L("Ripasso della volta scorsa:<br><b>PERICOLO</b> = una cosa che <b>può</b> fare male.<br><b>DANNO</b> = il male che <b>succede davvero</b>.<br><b>RISCHIO</b> = <b>quanto è facile</b> che il danno succeda e <b>quanto è grave</b>.<br>Oggi impari come si <b>abbassa</b> il rischio.", "مراجعة: الخطر = شيء يمكن أن يؤذي. الضرر = الأذى الذي يحدث فعلاً. المخاطرة = مدى سهولة حدوث الضرر ومدى خطورته. اليوم نتعلم كيف نخفّض المخاطرة.", "复习：危险源 = 可能伤人的东西。伤害 = 真的发生的伤。风险 = 伤害发生的可能性有多大、有多严重。今天学习怎样降低风险。") },
      { titolo: "2. Due modi: prevenzione e protezione · ٢. طريقتان: الوقاية والحماية · 2. 两种方法：预防和防护", testo: L("Ci sono <b>due modi</b> per abbassare il rischio.<br><b>PREVENZIONE</b>: il danno succede <b>meno spesso</b> (o mai). Agisci <b>prima</b>.<br><b>PROTEZIONE</b>: se il danno succede, fa <b>meno male</b>. Ti difende <b>durante</b>.<br>Esempio, il motorino: andare <b>piano</b> è prevenzione (cadi meno spesso); il <b>casco</b> è protezione (se cadi, ti fai meno male).", "هناك طريقتان لتخفيض المخاطرة. الوقاية: الضرر يحدث أقل (أو لا يحدث أبداً)، نعمل قبل. الحماية: إذا حدث الضرر يكون أقل أذى. مثال الدراجة النارية: القيادة ببطء = وقاية؛ الخوذة = حماية.", "降低风险有两种方法。预防：让伤害少发生（或不发生），在事前行动。防护：如果伤害发生了，伤得轻一些。例如摩托车：开慢一点 = 预防；头盔 = 防护。") },
      { titolo: "3. La prevenzione a casa e in aula · ٣. الوقاية في البيت وفي القاعة · 3. 家里和教室里的预防", testo: L("<b>A casa:</b> il manico della padella girato <b>verso dentro</b>; il telefono in carica <b>sul tavolo</b>, non sotto il cuscino; il pavimento bagnato asciugato <b>subito</b>.<br><b>In aula:</b> i cavi <b>lungo il muro</b>, gli zaini <b>sotto il banco</b>, la sedia con <b>quattro gambe a terra</b>, una presa rotta <b>detta subito</b> al prof.<br>Sono tutte <b>prevenzione</b>: il pericolo non arriva a farti male.", "في البيت: مقبض المقلاة نحو الداخل؛ الهاتف يُشحن على الطاولة لا تحت الوسادة؛ نجفف الأرض المبللة فوراً. في القاعة: الأسلاك بجانب الحائط، الحقائب تحت الطاولة، الكرسي على أرجله الأربع، نخبر المعلم فوراً عن المقبس المكسور. كل هذا وقاية.", "在家：锅柄朝里；手机放在桌上充电，不放在枕头下；湿地板马上擦干。在教室：电线沿着墙，书包放在桌子下面，椅子四条腿着地，插座坏了马上告诉老师。这些都是预防。") },
      { titolo: "4. La prevenzione in strada e nello sport · ٤. الوقاية في الشارع وفي الرياضة · 4. 马路上和运动中的预防", testo: L("<b>In strada:</b> le <b>luci</b> della bici accese di sera, <b>rallentare</b> sul bagnato, il telefono <b>in tasca</b> mentre guidi o attraversi.<br><b>Nello sport:</b> il <b>riscaldamento</b> prima della partita, il pavimento della palestra <b>asciutto</b>, il pallone <b>rimesso a posto</b>.<br>Anche queste sono <b>prevenzione</b>: il danno succede meno spesso.", "في الشارع: أضواء الدراجة مضاءة في المساء، نبطئ على الأرض المبللة، الهاتف في الجيب أثناء القيادة أو عبور الطريق. في الرياضة: الإحماء قبل المباراة، أرض الصالة جافة، نعيد الكرة إلى مكانها. هذه أيضاً وقاية.", "在马路上：晚上开自行车灯，路湿时减速，骑车或过马路时手机放口袋里。运动时：比赛前热身，体育馆地板保持干燥，球放回原处。这些也是预防。") },
      { titolo: "5. La protezione · ٥. الحماية · 5. 防护", testo: L("La <b>protezione</b> non toglie il pericolo: fa sì che il danno sia <b>meno grave</b>.<br>Esempi: il <b>casco</b> del motorino e della bici, i <b>guanti da forno</b>, i <b>parastinchi</b> nel calcio, le <b>ginocchiere</b>, gli <b>occhiali</b> quando usi il trapano, le <b>scarpe antinfortunistiche</b> al lavoro.<br>Al lavoro queste cose si chiamano <b>DPI</b>: dispositivi di protezione individuale.", "الحماية لا تزيل الخطر: تجعل الضرر أقل خطورة. أمثلة: خوذة الدراجة النارية والدراجة، قفازات الفرن، واقي الساق في كرة القدم، واقي الركبة، النظارات عند استعمال المثقاب، أحذية السلامة في العمل. في العمل تُسمّى معدات الحماية الشخصية (DPI).", "防护不能去掉危险源：它让伤害不那么严重。例如：摩托车和自行车的头盔、烤箱手套、踢足球的护腿板、护膝、用电钻时戴的护目镜、工作时穿的安全鞋。在工作中这些叫个人防护装备（DPI）。") },
      { titolo: "6. Protezione per tutti, protezione per me · ٦. حماية للجميع، حماية لي · 6. 保护所有人，保护我自己", testo: L("Alcune protezioni proteggono <b>tutti</b>: il <b>salvavita</b> di casa (stacca la corrente se c'è un guasto), la <b>ciabatta con l'interruttore</b>, la <b>ringhiera</b> delle scale.<br>Altre proteggono <b>solo chi le indossa</b>: il casco, i guanti, gli occhiali.<br>Quelle per tutti funzionano anche se qualcuno si dimentica; quelle per me funzionano <b>solo se le metto</b>.", "بعض وسائل الحماية تحمي الجميع: قاطع الكهرباء الآلي في البيت (يقطع الكهرباء عند العطل)، المشترك الكهربائي بزر، درابزين الدرج. وبعضها يحمي فقط من يلبسها: الخوذة، القفازات، النظارات. الحماية للجميع تعمل حتى لو نسي أحد؛ الحماية الشخصية تعمل فقط إذا لبستها.", "有些防护保护所有人：家里的漏电保护开关（出故障时自动断电）、带开关的插线板、楼梯扶手。有些只保护戴着它的人：头盔、手套、护目镜。保护所有人的防护即使有人忘了也有效；个人防护只有戴上才有效。") },
      { titolo: "7. Prima la prevenzione, poi la protezione · ٧. أولاً الوقاية، ثم الحماية · 7. 先预防，再防护", testo: L("La regola d'oro: <b>prima</b> provo a <b>togliere</b> il pericolo (prevenzione). Se <b>non posso</b> toglierlo, <b>mi proteggo</b> (protezione).<br>Esempio: il cavo per terra in aula. Prima lo <b>sposto lungo il muro</b>: il pericolo sparisce.<br>Esempio: l'olio bollente. Non posso cucinare senza: allora giro il manico verso dentro e uso i <b>guanti da forno</b>.", "القاعدة الذهبية: أولاً أحاول إزالة الخطر (وقاية). إذا لم أستطع إزالته، أحمي نفسي (حماية). مثال: السلك على أرض القاعة: أولاً أنقله بجانب الحائط فيختفي الخطر. مثال: الزيت المغلي: لا أستطيع الطبخ بدونه، فأدير المقبض نحو الداخل وأستعمل قفازات الفرن.", "黄金法则：先想办法去掉危险源（预防）。如果去不掉，就保护自己（防护）。例如：教室地上的电线，先把它移到墙边，危险就没了。例如：热油，做饭离不开它，那就把锅柄朝里，并戴烤箱手套。") },
      { titolo: "8. Lo schermo e la sedia · ٨. الشاشة والكرسي · 8. 屏幕和椅子", testo: L("Al computer il pericolo è <b>piccolo ma tutti i giorni</b>: occhi stanchi, mal di schiena, mal di collo.<br>Prevenzione facile: una <b>pausa</b> breve ogni ora (guarda lontano), lo schermo alla <b>distanza di un braccio</b>, la <b>schiena appoggiata</b>, i piedi a terra, la sedia con <b>quattro gambe a terra</b>.<br>Lo puoi fare <b>adesso</b>, qui in aula.", "أمام الحاسوب الخطر صغير لكنه كل يوم: تعب العينين، ألم الظهر، ألم الرقبة. وقاية سهلة: استراحة قصيرة كل ساعة (انظر بعيداً)، الشاشة على بعد ذراع، الظهر مسنود، القدمان على الأرض، الكرسي على أرجله الأربع. تستطيع أن تفعل هذا الآن هنا في القاعة.", "在电脑前，危险很小但每天都有：眼睛累、腰疼、脖子疼。简单的预防：每小时短暂休息一下（看远处），屏幕离你一臂远，后背靠着椅背，双脚着地，椅子四条腿着地。你现在就可以在教室里做到。") }
    ],
    strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../1inf-oggi/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
    via: C("sic", L("Il casco del motorino è…", "خوذة الدراجة النارية هي…", "摩托车头盔是……"), ["protezione", "prevenzione", "un pericolo"], "Se cadi, ti fai meno male: è protezione.", "protezione"),
    prepara: [
      { q: L("Guardati intorno, qui in aula. Scrivi UNA cosa di prevenzione che vedi (o che manca).", "انظر حولك في القاعة. اكتب شيئاً واحداً من الوقاية تراه (أو ينقص).", "看看教室四周，写一个你看到的（或缺少的）预防措施。"), aiuto: "Anche nella tua lingua. Esempio: «i cavi sono lungo il muro».", min: 4 },
      { q: L("Scrivi UNA protezione che usi (o che dovresti usare) nello sport o in strada.", "اكتب وسيلة حماية واحدة تستعملها (أو يجب أن تستعملها) في الرياضة أو في الشارع.", "写一个你在运动或马路上使用（或应该使用）的防护。"), aiuto: "Anche nella tua lingua. Esempio: «il casco quando vado in bici».", min: 4 }
    ],
    allenamento: [
      S(1, C("sic", L("Il male che succede DAVVERO si chiama…", "الأذى الذي يحدث فعلاً اسمه…", "真的发生的伤叫……"), ["danno", "pericolo", "rischio"], "Il danno è già successo.", "")),
      S(2, C("sic", L("PREVENZIONE vuol dire…", "الوقاية تعني…", "预防的意思是……"), ["il danno succede meno spesso", "il danno fa meno male", "il danno è già successo"], "Prevenzione: agisci prima.", "")),
      S(2, C("sic", L("PROTEZIONE vuol dire…", "الحماية تعني…", "防护的意思是……"), ["se il danno succede, fa meno male", "il danno non succede mai", "non serve fare niente"], "Protezione: ti difende durante.", "")),
      S(3, C("sic", L("Il manico della padella girato verso dentro è…", "مقبض المقلاة نحو الداخل هو…", "锅柄朝里是……"), ["prevenzione", "protezione", "un danno"], "Nessuno lo urta: il danno succede meno spesso.", "")),
      S(3, C("sic", L("Il telefono in carica: dove lo metti di notte?", "الهاتف في الشحن: أين تضعه في الليل؟", "晚上手机充电放在哪里？"), ["sul tavolo", "sotto il cuscino", "nel letto vicino alla faccia"], "Sul tavolo non si scalda troppo.", "")),
      S(4, C("sic", L("Le luci della bici accese di sera sono…", "أضواء الدراجة مضاءة في المساء هي…", "晚上开着的自行车灯是……"), ["prevenzione", "protezione", "un pericolo"], "Ti vedono: è più difficile che ti investano.", "")),
      S(4, C("sic", L("Il riscaldamento prima della partita serve a…", "الإحماء قبل المباراة يفيد في…", "比赛前热身是为了……"), ["farsi male meno spesso", "vincere sicuro", "stancarsi prima"], "È prevenzione.", "")),
      S(5, C("sic", L("I guanti da forno sono…", "قفازات الفرن هي…", "烤箱手套是……"), ["protezione", "prevenzione", "un danno"], "Se tocchi la teglia calda, non ti bruci.", "")),
      S(5, C("sic", L("Usi il trapano. Che cosa metti?", "تستعمل المثقاب. ماذا تلبس؟", "你用电钻。你戴什么？"), ["gli occhiali di protezione", "le cuffie della musica", "niente"], "Le schegge non ti entrano negli occhi.", "")),
      S(6, C("sic", L("Il salvavita di casa protegge…", "قاطع الكهرباء الآلي في البيت يحمي…", "家里的漏电保护开关保护……"), ["tutti quelli in casa", "solo chi lo tocca", "nessuno"], "Stacca la corrente per tutti.", "")),
      S(6, C("sic", L("Il casco protegge…", "الخوذة تحمي…", "头盔保护……"), ["solo chi lo indossa", "tutti quelli in strada", "nessuno"], "Funziona solo se lo metti.", "")),
      S(7, C("sic", L("Cavo per terra in aula. Che cosa fai PRIMA?", "سلك على أرض القاعة. ماذا تفعل أولاً؟", "教室地上有电线。你先做什么？"), ["lo sposto lungo il muro", "metto le scarpe speciali", "non faccio niente"], "Prima togli il pericolo.", "")),
      S(8, C("sic", L("Lo schermo del computer: a che distanza?", "شاشة الحاسوب: على أي مسافة؟", "电脑屏幕：离多远？"), ["un braccio", "dieci centimetri", "tre metri"], "Un braccio: gli occhi si stancano meno.", ""))
    ],
    /* ---------- VERIFICA (chiusa: la apre il prof; gli stessi 20 casi sono il quiz su Moduli) ---------- */
    crocette: [
      C("sic", L("Il casco allacciato in motorino è…", "الخوذة المربوطة على الدراجة النارية هي…", "骑摩托车时系好的头盔是……"), ["protezione: se cadi ti fai meno male", "prevenzione: così non cadi mai", "un pericolo", "un danno"], "", "protezione"),
      C("sic", L("Giri il manico della padella verso dentro. Questo è…", "تدير مقبض المقلاة نحو الداخل. هذا…", "你把锅柄转向里面。这是……"), ["prevenzione: è più difficile urtarla", "protezione: se ti bruci fa meno male", "un danno", "un pericolo"], "", "casa"),
      C("sic", L("In aula fissi i cavi lungo il muro. Questo è…", "في القاعة تثبّت الأسلاك بجانب الحائط. هذا…", "在教室里你把电线固定在墙边。这是……"), ["prevenzione", "protezione", "un danno", "un quasi incidente"], "", "casa"),
      C("sic", L("Metti i guanti da forno per prendere la teglia calda. Questo è…", "تلبس قفازات الفرن لتأخذ الصينية الساخنة. هذا…", "你戴烤箱手套去拿热烤盘。这是……"), ["protezione", "prevenzione", "un pericolo", "un danno"], "", "protezione"),
      C("sic", L("Di sera accendi le luci della bici. Questo è…", "في المساء تشغّل أضواء الدراجة. هذا…", "晚上你打开自行车灯。这是……"), ["prevenzione", "protezione", "un danno", "niente di utile"], "", "strada"),
      C("sic", L("A pallavolo metti le ginocchiere. Questo è…", "في الكرة الطائرة تلبس واقي الركبة. هذا…", "打排球时你戴护膝。这是……"), ["protezione", "prevenzione", "un pericolo", "un danno"], "", "protezione"),
      C("sic", L("Che differenza c'è tra prevenzione e protezione?", "ما الفرق بين الوقاية والحماية؟", "预防和防护有什么区别？"), ["la prevenzione fa succedere il danno meno spesso, la protezione lo rende meno grave", "sono la stessa cosa", "la protezione si fa prima, la prevenzione dopo", "la prevenzione serve solo al lavoro"], "", "due"),
      C("sic", L("Un cavo passa per terra tra i banchi. Qual è la cosa MIGLIORE?", "سلك على الأرض بين الطاولات. ما الأفضل؟", "桌子之间的地上有电线。最好的做法是什么？"), ["spostarlo lungo il muro: il pericolo sparisce", "camminare piano e sperare", "lasciarlo lì e non pensarci", "mettere le scarpe da ginnastica"], "", "prima"),
      C("sic", L("Due modi di tagliare il pane. Quale abbassa di più il rischio?", "طريقتان لتقطيع الخبز. أيّهما يخفّض المخاطرة أكثر؟", "两种切面包的方法。哪种更能降低风险？"), ["sul tagliere, con la lama lontana dalle dita", "in mano, tagliando verso la mano", "di corsa, parlando al telefono", "con un coltello che non taglia, schiacciando forte"], "", "casa"),
      C("sic", L("Telefono in carica. Dove il rischio è più BASSO?", "الهاتف في الشحن. أين المخاطرة أقل؟", "手机充电。放在哪里风险最低？"), ["sul tavolo, con il caricatore originale", "sotto il cuscino, tutta la notte", "sul letto, con il filo spellato", "sul divano, sotto la coperta"], "", "casa"),
      C("sic", L("In aula vedi una presa rotta con i fili fuori. Che cosa fai?", "في القاعة ترى مقبساً مكسوراً والأسلاك خارجة. ماذا تفعل؟", "在教室里你看到一个坏插座，电线露在外面。你怎么做？"), ["non la tocco e lo dico subito al prof", "la aggiusto io con lo scotch", "ci attacco il caricatore lo stesso", "faccio finta di niente"], "", "casa"),
      C("sic", L("In palestra il pavimento è bagnato. Che cosa fai?", "في الصالة الرياضية الأرض مبللة. ماذا تفعل؟", "体育馆地板是湿的。你怎么做？"), ["lo dico, e si asciuga prima di giocare", "gioco lo stesso, più veloce", "gioco con più forza nelle gambe", "non dico niente"], "", "strada"),
      C("sic", L("Il telefono in tasca scotta tanto. Che cosa fai?", "الهاتف في جيبك ساخن جداً. ماذا تفعل؟", "口袋里的手机很烫。你怎么做？"), ["lo tolgo dalla tasca, lo spengo e lo lascio raffreddare", "lo metto sotto il cuscino", "continuo a giocare", "lo metto in carica"], "", "casa"),
      C("sic", L("Lavoretto: devi prendere una scatola in alto e la scala traballa. Che cosa fai?", "عمل صغير: يجب أن تأخذ علبة من الأعلى والسلم يهتز. ماذا تفعل؟", "打零工：你要拿高处的箱子，梯子在晃。你怎么做？"), ["cerco una scala che sta ferma o chiedo a qualcuno di tenerla", "salgo lo stesso, veloce", "salgo su una sedia con le ruote", "salto per prenderla"], "", "prima"),
      C("sic", L("Il salvavita di casa protegge…", "قاطع الكهرباء الآلي في البيت يحمي…", "家里的漏电保护开关保护……"), ["tutti quelli che sono in casa", "solo chi lo tocca", "solo il frigorifero", "nessuno"], "", "tutti"),
      C("sic", L("Il casco protegge…", "الخوذة تحمي…", "头盔保护……"), ["solo chi lo indossa", "tutti quelli in strada", "anche se resta appeso in garage", "solo di notte"], "", "tutti"),
      C("sic", L("La regola d'oro della sicurezza è…", "القاعدة الذهبية للسلامة هي…", "安全的黄金法则是……"), ["prima tolgo il pericolo; se non posso, mi proteggo", "prima mi proteggo, poi non faccio altro", "basta stare attenti", "la protezione basta sempre"], "", "prima"),
      C("sic", L("Al computer, per non stancare gli occhi…", "أمام الحاسوب، حتى لا تتعب عيناك…", "在电脑前，为了不让眼睛累……"), ["ogni ora faccio una pausa breve e guardo lontano", "avvicino lo schermo al naso", "gioco 4 ore senza fermarmi", "abbasso la luce dello schermo al minimo"], "", "schermo"),
      C("sic", L("Come stai seduto al computer?", "كيف تجلس أمام الحاسوب؟", "你在电脑前怎么坐？"), ["schiena appoggiata, piedi a terra, quattro gambe della sedia a terra", "dondolando sulla sedia", "sdraiato con il collo piegato", "in piedi sulla sedia"], "", "schermo"),
      C("sic", L("Usi il trapano per un lavoretto. Prevenzione E protezione insieme sono…", "تستعمل المثقاب في عمل صغير. الوقاية والحماية معاً هما…", "你打零工时用电钻。预防加防护一起是……"), ["pezzo fermato bene + occhiali di protezione", "nessuna delle due: si fa veloce", "solo i guanti da forno", "solo la musica nelle cuffie"], "", "protezione")
    ],
    scale: [
      { area: "parere", q: L("Quanto ti senti sicuro, adesso, con prevenzione e protezione?", "ما مدى ثقتك الآن بالوقاية والحماية؟", "你现在对预防和防护有多大把握？"), basso: "per niente", alto: "moltissimo", ultima: true }
    ],
    aperte: [
      { area: "mia", tema: "casa", q: L("LA TUA CASA. Scrivi UNA cosa di PREVENZIONE che fai già a casa (o che dovresti fare). Quale pericolo toglie?", "بيتك. اكتب شيئاً واحداً من الوقاية تفعله في البيت (أو يجب أن تفعله). أيّ خطر يزيل؟", "你的家。写一个你在家已经做的（或应该做的）预防措施。它去掉了什么危险源？"),
        criteri: "azione concreta di prevenzione a casa; pericolo collegato coerente" },
      { area: "mia", tema: "protezione", q: L("LO SPORT O LA STRADA. Scrivi UNA protezione che usi (o che dovresti usare). Da quale danno ti protegge?", "الرياضة أو الشارع. اكتب وسيلة حماية واحدة تستعملها (أو يجب أن تستعملها). من أيّ ضرر تحميك؟", "运动或马路。写一个你使用（或应该使用）的防护。它保护你免受什么伤害？"),
        criteri: "protezione concreta (casco, parastinchi, guanti…) e danno che rende meno grave" }
    ],
    /* ---------- RECUPERO ---------- */
    recupero: [
      C("sic", L("Il casco è…", "الخوذة هي…", "头盔是……"), ["protezione", "prevenzione", "un pericolo"], "", "protezione"),
      C("sic", L("Il manico girato verso dentro è…", "المقبض نحو الداخل هو…", "锅柄朝里是……"), ["prevenzione", "protezione", "un danno"], "", "casa"),
      C("sic", L("Prevenzione: il danno succede…", "الوقاية: الضرر يحدث…", "预防：伤害发生得……"), ["meno spesso", "più spesso", "sempre"], "", "due"),
      C("sic", L("Protezione: il danno è…", "الحماية: الضرر يكون…", "防护：伤害……"), ["meno grave", "più grave", "già successo"], "", "due"),
      C("sic", L("Cavo per terra: per prima cosa…", "سلك على الأرض: أولاً…", "地上有电线：首先……"), ["lo sposto", "metto il casco", "niente"], "", "prima"),
      C("sic", L("Il salvavita protegge…", "قاطع الكهرباء الآلي يحمي…", "漏电保护开关保护……"), ["tutti", "solo me", "nessuno"], "", "tutti"),
      C("sic", L("Lo schermo sta a…", "الشاشة على بعد…", "屏幕离你……"), ["un braccio", "un dito", "tre metri"], "", "schermo"),
      C("sic", L("Le luci della bici di sera sono…", "أضواء الدراجة في المساء هي…", "晚上的自行车灯是……"), ["prevenzione", "protezione", "un danno"], "", "strada")
    ]
  };
})();
