// Classe 2 — Sicurezza, 2ª ora del corso (D.Lgs. 81/08): prevenzione e protezione, allineato al PDF ufficiale «02_Prevenzione_Protezione» (italiano · cinese; la 2INF non usa l'arabo, §2.49)
function L(it, zh) { return { it: it, ar: "", zh: zh }; }
window.BANCA = {
  titolo: "Sicurezza 2 — Prevenzione e protezione",
  sotto: "Classe 2 · Sicurezza sul lavoro (D.Lgs. 81/08), 2ª ora · ognuno ha le sue domande · 每个人的题目都不一样",
  regola: L("Dal PDF ufficiale della 2ª ora. <b>ESPOSIZIONE</b> = quando una persona si trova vicino a un pericolo. <b>PERICOLO + ESPOSIZIONE = RISCHIO</b>. "
          + "<b>PREVENZIONE</b> = le misure per <b>evitare</b> o diminuire il rischio: prima domanda «si può <b>eliminare il pericolo</b>?»; se no, «si può eliminare l'<b>esposizione</b>?»; se no, si <b>riduce l'esposizione</b>. Il pericolo, per sua natura, non si diminuisce. "
          + "<b>Valutazione del rischio: R = P × D</b>. DANNO (D): 1 lieve, 2 modesto, 3 grave, 4 gravissimo. PROBABILITÀ (P): 1 improbabile, 2 possibile, 3 probabile, 4 molto probabile. "
          + "<b>PROTEZIONE</b> = misure e dispositivi, collettivi o individuali, che riducono la <b>gravità</b> del danno (la prevenzione riduce la <b>probabilità</b>). "
          + "Esempi: divieto di fumare = prevenzione (incendi); disco silenziato = prevenzione (rumore); maschera antipolvere, guanti = protezione; estintore = protezione dal fuoco. "
          + "<b>Gerarchia:</b> 1) eliminazione del rischio, 2) sostituzione con qualcosa di meno pericoloso, 3) riduzione dell'esposizione con misure tecniche e organizzative. "
          + "<b>INFORTUNIO</b> = causa violenta al lavoro con inabilità, invalidità o morte. <b>INCIDENTE</b> = danni materiali (o nessuno) ma si è rischiato di fare male alle persone: si chiama anche <b>evento sentinella</b>.",
          "来自第2小时的正式 PDF。暴露 = 一个人处在危险源附近。危险源 + 暴露 = 风险。预防 = 避免或降低风险的措施：先问「能消除危险源吗？」不能的话「能消除暴露吗？」再不能就减少暴露。危险源本身不能减少。"
          + "风险评估：R = P × D。伤害 D：1 轻微，2 中等，3 严重，4 非常严重。可能性 P：1 不太可能，2 可能，3 很可能，4 非常可能。"
          + "防护 = 降低伤害严重程度的集体或个人措施和装置（预防降低可能性）。例子：禁止吸烟 = 预防（火灾）；静音锯片 = 预防（噪音）；防尘口罩、手套 = 防护；灭火器 = 防火防护。"
          + "层级：1）消除风险，2）用不太危险的东西代替，3）用技术和组织措施减少暴露。工伤 = 工作中的暴力原因造成伤残或死亡。事故 = 有物质损失（或没有），但差点伤到人，也叫「哨兵事件」。"),
  quante: 10,
  domande: [
    { q: L("<b>PERICOLO + ESPOSIZIONE</b> = …", "<b>危险源 + 暴露</b> = ……"),
      o: [L("RISCHIO", "风险"), L("PROTEZIONE", "防护"), L("INFORTUNIO", "工伤"), L("DPI", "DPI")], a: 0 },
    { q: L("Cos'è l'<b>ESPOSIZIONE</b>?", "什么是<b>暴露</b>？"),
      o: [L("quando una persona si trova vicino a un pericolo", "一个人处在危险源附近"), L("un cartello giallo", "黄色标志"), L("il danno già successo", "已经发生的伤害"), L("un corso di formazione", "培训课程")], a: 0 },
    { q: L("Nella prevenzione, qual è la <b>prima domanda</b>?", "预防的<b>第一个问题</b>是什么？"),
      o: [L("Si può eliminare il pericolo?", "能消除危险源吗？"), L("Chi paga i danni?", "谁赔偿？"), L("Quanti DPI servono?", "需要几个 DPI？"), L("A che ora finisce il turno?", "几点下班？")], a: 0 },
    { q: L("Il <b>pericolo</b>, per sua natura…", "<b>危险源</b>本身……"),
      o: [L("non può essere diminuito: si elimina o si riduce l'esposizione", "不能减少：只能消除或减少暴露"), L("si diminuisce con i guanti", "戴手套就减少了"), L("diventa rischio da solo", "自己变成风险"), L("non esiste in laboratorio", "实验室里不存在")], a: 0 },
    { q: L("Un danno <b>GRAVISSIMO</b> vale…", "<b>非常严重</b>的伤害是几分？"),
      o: [L("4", "4"), L("1", "1"), L("2", "2"), L("10", "10")], a: 0 },
    { q: L("Una probabilità <b>IMPROBABILE</b> vale…", "<b>不太可能</b>的可能性是几分？"),
      o: [L("1", "1"), L("4", "4"), L("3", "3"), L("0", "0")], a: 0 },
    { q: L("Se P = 3 (probabile) e D = 2 (modesto), il rischio R vale…", "如果 P = 3（很可能），D = 2（中等），风险 R 是……"),
      o: [L("6", "6"), L("5", "5"), L("1", "1"), L("32", "32")], a: 0 },
    { q: L("Il <b>divieto di fumare</b> è un intervento di…", "<b>禁止吸烟</b>是……措施"),
      o: [L("prevenzione per il rischio incendi", "火灾风险的预防"), L("protezione individuale", "个人防护"), L("sostituzione", "代替"), L("primo soccorso", "急救")], a: 0 },
    { q: L("Una <b>maschera antipolvere</b> è un intervento di…", "<b>防尘口罩</b>是……措施"),
      o: [L("protezione delle vie respiratorie", "呼吸道的防护"), L("prevenzione del rumore", "噪音的预防"), L("eliminazione del pericolo", "消除危险源"), L("valutazione del rischio", "风险评估")], a: 0 },
    { q: L("La <b>gerarchia</b> delle misure di prevenzione è…", "预防措施的<b>层级</b>是……"),
      o: [L("eliminare, sostituire, ridurre l'esposizione", "消除、代替、减少暴露"), L("ridurre, sostituire, eliminare", "减少、代替、消除"), L("solo DPI", "只有 DPI"), L("prima l'estintore", "先灭火器")], a: 0 },
    { q: L("Un evento che ha fatto solo danni materiali ma poteva ferire qualcuno è…", "只造成物质损失、但差点伤到人的事件是……"),
      o: [L("un incidente (evento sentinella)", "事故（哨兵事件）"), L("un infortunio", "工伤"), L("una protezione", "防护"), L("un DPI", "DPI")], a: 0 },
    { q: L("Un <b>INFORTUNIO</b> è…", "<b>工伤</b>是……"),
      o: [L("una causa violenta al lavoro che porta inabilità, invalidità o morte", "工作中的暴力原因造成伤残或死亡"), L("un evento senza nessun danno", "没有任何伤害的事件"), L("un cartello", "标志"), L("una pausa", "休息")], a: 0 },
    { q: L("La <b>PREVENZIONE</b> serve a…", "<b>预防</b>的作用是……"),
      o: [L("far succedere il danno meno spesso", "让伤害更少发生"), L("rendere il danno meno grave", "让伤害不那么严重"), L("curare chi si è fatto male", "治疗受伤的人"), L("pagare l'assicurazione", "付保险")], a: 0 },
    { q: L("La <b>PROTEZIONE</b> serve a…", "<b>防护</b>的作用是……"),
      o: [L("rendere il danno meno grave", "让伤害不那么严重"), L("far succedere il danno meno spesso", "让伤害更少发生"), L("scrivere il DVR", "写 DVR"), L("chiamare il 112", "打112")], a: 0 },
    { q: L("Il <b>RISCHIO</b> si calcola come…", "<b>风险</b>怎么计算？"),
      o: [L("probabilità × danno", "可能性 × 伤害程度"), L("pericolo + danno", "危险源 + 伤害"), L("ore di lavoro × stipendio", "工作时间 × 工资"), L("numero di lavoratori", "工人的数量")], a: 0 },
    { q: L("Cosa sono i <b>DPI</b>?", "<b>DPI</b> 是什么？"),
      o: [L("Dispositivi di Protezione Individuale (casco, guanti…)", "个人防护装备（头盔、手套……）"), L("Documenti Per l'Impresa", "企业文件"), L("Divieti Per gli Impiegati", "职员禁令"), L("Dati Personali Informatici", "个人电脑数据")], a: 0 },
    { q: L("Qual è l'<b>ordine giusto</b> delle misure di sicurezza?", "安全措施的<b>正确顺序</b>是什么？"),
      o: [L("eliminare il rischio, poi protezione collettiva, poi DPI", "消除风险，然后集体防护，最后 DPI"), L("prima i DPI, poi il resto", "先 DPI，然后其他"), L("solo i DPI bastano", "只要 DPI 就够了"), L("non c'è un ordine", "没有顺序")], a: 0 },
    { q: L("Un <b>parapetto</b> su un balcone di lavoro è…", "工作阳台上的<b>护栏</b>是……"),
      o: [L("protezione collettiva", "集体防护"), L("un DPI", "个人防护装备 DPI"), L("prevenzione con la formazione", "通过培训的预防"), L("un cartello", "一个标志")], a: 0 },
    { q: L("Le <b>scarpe antinfortunistiche</b> sono…", "<b>安全鞋</b>是……"),
      o: [L("un DPI (protezione individuale)", "DPI（个人防护）"), L("protezione collettiva", "集体防护"), L("prevenzione", "预防"), L("vietate a scuola", "学校禁止")], a: 0 },
    { q: L("Un <b>corso di formazione</b> sulla sicurezza è…", "安全<b>培训课程</b>是……"),
      o: [L("prevenzione", "预防"), L("protezione individuale", "个人防护"), L("un danno", "伤害"), L("un pericolo", "危险源")], a: 0 },
    { q: L("Chi scrive la valutazione dei rischi (il <b>DVR</b>)?", "谁写风险评估（<b>DVR</b>）？"),
      o: [L("il datore di lavoro", "雇主"), L("lo studente", "学生"), L("il cliente", "客户"), L("nessuno, non serve", "没有人，不需要")], a: 0 },
    { q: L("Un cartello <b>BLU</b> rotondo indica…", "圆形<b>蓝色</b>标志表示……"),
      o: [L("un obbligo (per esempio: indossa i guanti)", "必须（例如：戴手套）"), L("un divieto", "禁止"), L("un'uscita di emergenza", "紧急出口"), L("attenzione, pericolo", "注意，危险")], a: 0 },
    { q: L("Un cartello <b>VERDE</b> indica…", "<b>绿色</b>标志表示……"),
      o: [L("salvataggio e uscite di emergenza", "救援和紧急出口"), L("un divieto", "禁止"), L("un obbligo", "必须"), L("materiale infiammabile", "易燃物品")], a: 0 },
    { q: L("Un cartello <b>ROSSO</b> con la barra indica…", "带斜杠的<b>红色</b>标志表示……"),
      o: [L("un divieto (per esempio: vietato fumare)", "禁止（例如：禁止吸烟）"), L("un obbligo", "必须"), L("un'uscita", "出口"), L("il pronto soccorso", "急救")], a: 0 },
    { q: L("Al videoterminale, quanta <b>pausa</b> serve?", "在电脑终端前需要多少<b>休息</b>？"),
      o: [L("15 minuti ogni 2 ore", "每2小时休息15分钟"), L("nessuna pausa", "不需要休息"), L("1 ora ogni 15 minuti", "每15分钟休息1小时"), L("solo a fine giornata", "只在一天结束时")], a: 0 },
    { q: L("In laboratorio uno <b>zaino nel passaggio</b> è…", "实验室里<b>通道上的书包</b>是……"),
      o: [L("un pericolo: lo sposto (prevenzione)", "危险源：我把它移开（预防）"), L("una protezione", "防护"), L("un DPI", "DPI"), L("normale, lo lascio", "正常，我不管它")], a: 0 },
    { q: L("Un <b>estintore</b> vicino alla porta è…", "门旁边的<b>灭火器</b>是……"),
      o: [L("protezione collettiva", "集体防护"), L("un DPI", "DPI"), L("un pericolo", "危险源"), L("un divieto", "禁止")], a: 0 },
    { q: L("Il <b>carter</b> che copre le parti in movimento di una macchina è…", "盖住机器运动部件的<b>防护罩</b>是……"),
      o: [L("protezione collettiva", "集体防护"), L("un DPI", "DPI"), L("un rischio", "风险"), L("un corso", "课程")], a: 0 },
    { q: L("Perché i DPI si usano <b>per ultimi</b>?", "为什么 DPI <b>最后</b>才用？"),
      o: [L("perché prima si prova a togliere il rischio alla fonte", "因为先要从源头消除风险"), L("perché costano poco", "因为便宜"), L("perché sono scomodi e non servono", "因为不舒服也没用"), L("perché li decide lo studente", "因为由学生决定")], a: 0 }
  ]
};
