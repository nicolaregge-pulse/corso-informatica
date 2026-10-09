// Classe 2 — Sicurezza, 2ª ora del corso (D.Lgs. 81/08): prevenzione e protezione (italiano · cinese; la 2INF non usa l'arabo, §2.49)
function L(it, zh) { return { it: it, ar: "", zh: zh }; }
window.BANCA = {
  titolo: "Sicurezza 2 — Prevenzione e protezione",
  sotto: "Classe 2 · Sicurezza sul lavoro (D.Lgs. 81/08), 2ª ora · ognuno ha le sue domande · 每个人的题目都不一样",
  regola: L("<b>RISCHIO = PROBABILITÀ × DANNO</b>: quanto è facile che succeda, per quanto è grave. "
          + "<b>PREVENZIONE</b> = abbassa la <b>probabilità</b>: formazione, manutenzione, ordine, procedure, segnaletica. "
          + "<b>PROTEZIONE</b> = abbassa la <b>gravità</b> del danno: <b>collettiva</b> (parapetti, carter delle macchine, estintori, uscite di emergenza) "
          + "e <b>individuale</b> = i <b>DPI</b>, Dispositivi di Protezione Individuale (casco, guanti, occhiali, scarpe antinfortunistiche, cuffie). "
          + "<b>Ordine giusto:</b> 1) eliminare il rischio alla fonte, 2) protezione collettiva, 3) DPI per ultimi. "
          + "Il <b>datore di lavoro</b> scrive la valutazione dei rischi nel <b>DVR</b> (Documento di Valutazione dei Rischi). "
          + "<b>Colori dei cartelli:</b> rosso = divieto e antincendio, giallo = attenzione, blu = obbligo, verde = salvataggio e uscite. "
          + "<b>Al computer:</b> 15 minuti di pausa ogni 2 ore al videoterminale, schiena dritta, cavi e zaini fuori dai passaggi, niente liquidi vicino al PC.",
          "风险 = 可能性 × 伤害程度。预防 = 降低发生的可能性（培训、维修、整齐、程序、标志）。"
          + "防护 = 降低伤害的严重程度：集体防护（护栏、机器防护罩、灭火器、紧急出口）和个人防护装备 DPI（头盔、手套、眼镜、安全鞋、耳罩）。"
          + "正确顺序：1）从源头消除风险，2）集体防护，3）最后才是 DPI。雇主把风险评估写在 DVR（风险评估文件）里。"
          + "标志颜色：红色 = 禁止和消防，黄色 = 注意，蓝色 = 必须，绿色 = 救援和出口。电脑前：每2小时休息15分钟，背挺直，电线和书包不放在通道上，电脑旁不放饮料。"),
  quante: 10,
  domande: [
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
