// Classe 1 — Sicurezza, 1ª ora: pericolo, danno, rischio, prevenzione, protezione (trilingue IT · AR · ZH)
// Versione semplificata del quiz della Classe 2 (crea-quiz-sicurezza-1ora-2inf.gs), con frasi brevi.
function L(it, ar, zh) { return { it: it, ar: ar, zh: zh }; }
window.BANCA = {
  titolo: "Sicurezza 1 — Pericolo, danno, rischio",
  sotto: "Classe 1 · Sicurezza sul lavoro · ognuno ha le sue domande · لكل واحد أسئلته · 每个人的题目都不一样",
  regola: L("<b>PERICOLO</b> = una cosa che <b>può</b> fare male (il coltello, il gas). "
          + "<b>DANNO</b> = il male che ti fai (un taglio, una frattura). "
          + "<b>RISCHIO</b> = <b>quanto è probabile</b> che il danno succeda davvero. "
          + "<b>PREVENZIONE</b> = fa succedere il danno <b>meno spesso</b> (divieto di fumare). "
          + "<b>PROTEZIONE</b> = fa il danno <b>meno grave</b> (casco, guanti, estintore).",
          "الخطر = شيء يمكن أن يؤذي (السكين، الغاز). الضرر = الأذى الذي يحدث (جرح، كسر). المخاطرة = مدى احتمال حدوث الضرر فعلاً. "
          + "الوقاية = تجعل الضرر يحدث أقل (منع التدخين). الحماية = تجعل الضرر أقل خطورة (الخوذة، القفازات، طفاية الحريق).",
          "危险源 = 可能伤人的东西(刀、煤气)。伤害 = 受到的伤(割伤、骨折)。风险 = 伤害真的发生的可能性有多大。"
          + "预防 = 让伤害更少发生(禁止吸烟)。防护 = 让伤害不那么严重(头盔、手套、灭火器)。"),
  quante: 10,
  domande: [
    { q: L("Che cos'è il <b>PERICOLO</b>?", "ما هو <b>الخطر</b>؟", "什么是<b>危险源</b>?"),
      o: [L("Una cosa che può fare male", "شيء يمكن أن يؤذي", "可能伤人的东西"), L("Il male che ti sei già fatto", "الأذى الذي حدث بالفعل", "已经受到的伤"),
          L("Un cartello verde", "لافتة خضراء", "一个绿色的标志"), L("Un corso di formazione", "دورة تدريبية", "一个培训课程")], a: 0 },
    { q: L("Che cos'è il <b>DANNO</b>?", "ما هو <b>الضرر</b>؟", "什么是<b>伤害</b>?"),
      o: [L("Il male che ti fai (un taglio, una frattura)", "الأذى الذي يحدث لك (جرح، كسر)", "受到的伤(割伤、骨折)"), L("Una cosa che può fare male", "شيء يمكن أن يؤذي", "可能伤人的东西"),
          L("Un estintore", "طفاية حريق", "灭火器"), L("Una regola della scuola", "قاعدة المدرسة", "学校的规定")], a: 0 },
    { q: L("Che cos'è il <b>RISCHIO</b>?", "ما هي <b>المخاطرة</b>؟", "什么是<b>风险</b>?"),
      o: [L("Quanto è probabile che il danno succeda davvero", "مدى احتمال حدوث الضرر فعلاً", "伤害真的发生的可能性"), L("La stessa cosa del pericolo", "نفس الشيء مثل الخطر", "和危险源一样"),
          L("Un paio di guanti", "زوج من القفازات", "一副手套"), L("Una malattia", "مرض", "一种病")], a: 0 },
    { q: L("Il <b>coltello</b> in cucina è…", "<b>السكين</b> في المطبخ هو…", "厨房里的<b>刀</b>是……"),
      o: [L("un pericolo", "خطر", "危险源"), L("un danno", "ضرر", "伤害"), L("una protezione", "حماية", "防护"), L("una prevenzione", "وقاية", "预防")], a: 0 },
    { q: L("Ti tagli un dito con il coltello. Il taglio è…", "جرحت إصبعك بالسكين. الجرح هو…", "你用刀割伤了手指。这个伤口是……"),
      o: [L("un danno", "ضرر", "伤害"), L("un pericolo", "خطر", "危险源"), L("una prevenzione", "وقاية", "预防"), L("un rischio zero", "مخاطرة صفر", "零风险")], a: 0 },
    { q: L("Il <b>divieto di fumare</b> (contro gli incendi) è…", "<b>منع التدخين</b> (ضد الحرائق) هو…", "<b>禁止吸烟</b>(防火灾)是……"),
      o: [L("prevenzione: l'incendio succede meno spesso", "وقاية: الحريق يحدث أقل", "预防:火灾更少发生"), L("protezione", "حماية", "防护"),
          L("un danno", "ضرر", "伤害"), L("un pericolo", "خطر", "危险源")], a: 0 },
    { q: L("Il <b>casco</b> in cantiere è…", "<b>الخوذة</b> في موقع البناء هي…", "工地上的<b>安全帽</b>是……"),
      o: [L("protezione: il danno è meno grave", "حماية: الضرر أقل خطورة", "防护:伤害不那么严重"), L("prevenzione", "وقاية", "预防"),
          L("un pericolo", "خطر", "危险源"), L("un danno", "ضرر", "伤害")], a: 0 },
    { q: L("L'<b>estintore</b> è…", "<b>طفاية الحريق</b> هي…", "<b>灭火器</b>是……"),
      o: [L("un dispositivo di protezione dal fuoco", "أداة حماية من النار", "防火的防护设备"), L("un pericolo", "خطر", "危险源"),
          L("un danno", "ضرر", "伤害"), L("una malattia", "مرض", "一种病")], a: 0 },
    { q: L("La <b>mascherina antipolvere</b> è…", "<b>كمامة الغبار</b> هي…", "<b>防尘口罩</b>是……"),
      o: [L("protezione", "حماية", "防护"), L("prevenzione", "وقاية", "预防"), L("un pericolo", "خطر", "危险源"), L("un danno", "ضرر", "伤害")], a: 0 },
    { q: L("Prevenzione e protezione insieme…", "الوقاية والحماية معاً…", "预防和防护一起……"),
      o: [L("abbassano il rischio", "تقللان المخاطرة", "降低风险"), L("aumentano il pericolo", "تزيدان الخطر", "增加危险"),
          L("servono solo dopo l'incidente", "تفيدان فقط بعد الحادث", "只在事故以后有用"), L("non servono a niente", "لا تفيدان", "没有用")], a: 0 },
    { q: L("Che cos'è la <b>SALUTE</b>?", "ما هي <b>الصحة</b>؟", "什么是<b>健康</b>?"),
      o: [L("Stare bene nel corpo, nella mente e con gli altri", "أن تكون بخير في الجسم والعقل ومع الآخرين", "身体、心理和与人相处都好"),
          L("Solo non avere la febbre", "فقط عدم وجود حمى", "只是不发烧"), L("Essere molto forti", "أن تكون قوياً جداً", "非常强壮"), L("Non andare mai dal medico", "عدم الذهاب إلى الطبيب أبداً", "从来不看医生")], a: 0 },
    { q: L("Uno <b>zaino per terra</b> in mezzo alla classe è…", "<b>حقيبة على الأرض</b> وسط الصف هي…", "教室中间地上的<b>书包</b>是……"),
      o: [L("un pericolo: qualcuno può inciampare", "خطر: قد يتعثر أحد", "危险源:有人可能会绊倒"), L("una protezione", "حماية", "防护"),
          L("una prevenzione", "وقاية", "预防"), L("niente di importante", "لا شيء مهم", "不重要")], a: 0 },
    { q: L("Cosa fai per <b>prevenire</b> il pericolo dello zaino per terra?", "ماذا تفعل <b>لتجنّب</b> خطر الحقيبة على الأرض؟", "怎样<b>预防</b>书包在地上的危险?"),
      o: [L("Metto lo zaino sotto il banco o appeso", "أضع الحقيبة تحت الطاولة أو أعلّقها", "把书包放在桌子下面或挂起来"), L("Lo lascio lì", "أتركها هناك", "就放在那里"),
          L("Metto il casco", "ألبس الخوذة", "戴安全帽"), L("Chiamo l'ambulanza", "أتصل بالإسعاف", "叫救护车")], a: 0 },
    { q: L("Perché a scuola facciamo il corso sulla sicurezza?", "لماذا نأخذ دورة السلامة في المدرسة؟", "为什么在学校上安全课?"),
      o: [L("Lo chiede la legge: serve per lo stage e per il lavoro", "القانون يطلبه: ضروري للتدريب والعمل", "法律要求:实习和工作需要"), L("Per riempire le ore vuote", "لملء الساعات الفارغة", "为了填满空的课时"),
          L("È facoltativo", "اختياري", "是自愿的"), L("Per giocare", "للعب", "为了玩")], a: 0 },
    { q: L("Il <b>cavo della corrente</b> rovinato del PC è…", "<b>سلك الكهرباء</b> التالف للحاسوب هو…", "电脑坏了的<b>电线</b>是……"),
      o: [L("un pericolo: lo dico subito al docente", "خطر: أخبر المعلم فوراً", "危险源:马上告诉老师"), L("una protezione", "حماية", "防护"),
          L("un danno già successo", "ضرر حدث بالفعل", "已经发生的伤害"), L("normale, lo uso lo stesso", "عادي، أستعمله", "正常,照样用")], a: 0 }
  ]
};
