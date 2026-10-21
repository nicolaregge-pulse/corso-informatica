/* Banca del test di orientamento — Versione 1.0 — 21/10/2026. Bilingue: italiano e arabo.
   Test per ragazzi di terza media (un'ora). Una versione nuova = un file nuovo (banca-orientamento-v1.1.js …)
   e il numero in index.html. Un testo è "uguale nelle due lingue" oppure ["italiano", "arabo"].
   Domanda: { q: testo, g: risposta giusta, s: [sbagliate] }. Nessun dato raccolto. */
window.BANCA_ORIENTAMENTO = {
  versione: "1.0",
  blocchi: [
    { id: "logica", titolo: ["Logica", "المنطق"], minuti: 10,
      intro: ["Ragiona con calma. Non servono calcoli difficili: guarda bene e trova la regola.", "فكّر بهدوء. لا تحتاج إلى حسابات صعبة: انظر جيدًا واكتشف القاعدة."],
      domande: [
        { q: ["Che numero viene dopo? 2, 4, 8, 16, …", "ما الرقم التالي؟ 2، 4، 8، 16، …"], g: "32", s: ["24", "20", "18"] },
        { q: ["Che lettera viene dopo? A, C, E, G, …", "ما الحرف التالي؟ A، C، E، G، … (حروف لاتينية)"], g: "I", s: ["H", "L", "J"] },
        { q: ["Quale parola non c'entra con le altre?", "أي كلمة لا تنتمي إلى المجموعة؟"], g: ["rosa", "وردة"], s: [["cane", "كلب"], ["gatto", "قطة"], ["cavallo", "حصان"]] },
        { q: ["Tutti i gatti sono animali. Fufi è un gatto. Allora…", "كل القطط حيوانات. فوفي قطة. إذن…"], g: ["Fufi è un animale", "فوفي حيوان"],
          s: [["Fufi non è un animale", "فوفي ليست حيوانًا"], ["Tutti gli animali sono gatti", "كل الحيوانات قطط"], ["Non si può sapere", "لا يمكن أن نعرف"]] },
        { q: ["Marco è più alto di Luca. Luca è più alto di Anna. Chi è il più basso?", "ماركو أطول من لوكا. لوكا أطول من آنا. من الأقصر؟"], g: ["Anna", "آنا"],
          s: [["Marco", "ماركو"], ["Luca", "لوكا"], ["Non si può sapere", "لا يمكن أن نعرف"]] },
        { q: ["Oggi è lunedì. Che giorno sarà tra 10 giorni?", "اليوم هو الاثنين. أي يوم سيكون بعد 10 أيام؟"], g: ["giovedì", "الخميس"],
          s: [["mercoledì", "الأربعاء"], ["venerdì", "الجمعة"], ["lunedì", "الاثنين"]] },
        { q: ["Che numero viene dopo? 1, 1, 2, 3, 5, 8, …", "ما الرقم التالي؟ 1، 1، 2، 3، 5، 8، …"], g: "13", s: ["11", "12", "16"] }
      ] },
    { id: "matematica", titolo: ["Matematica", "الرياضيات"], minuti: 15,
      intro: ["Rispondi qui al computer. Non usare la calcolatrice.", "أجب هنا على الحاسوب. لا تستخدم الآلة الحاسبة."],
      domande: [
        { q: ["Quanto fa 7 × 8?", "كم يساوي 7 × 8؟"], g: "56", s: ["54", "48", "64"] },
        { q: ["Quanto è il 25% di 80?", "كم تساوي 25% من 80؟"], g: "20", s: ["25", "40", "16"] },
        { q: ["Un telefono costa 200 €. Con lo sconto del 10% quanto costa?", "هاتف ثمنه 200 يورو. مع خصم 10% كم يصبح ثمنه؟"], g: "180 €", s: ["190 €", "100 €", "20 €"] },
        { q: ["3 quaderni costano 6 €. Quanto costano 5 quaderni?", "3 دفاتر ثمنها 6 يورو. كم ثمن 5 دفاتر؟"], g: "10 €", s: ["8 €", "11 €", "15 €"] },
        { q: ["Risolvi: 3x + 5 = 20. Quanto vale x?", "حلّ المعادلة: 3x + 5 = 20. كم تساوي x؟"], g: "5", s: ["15", "8", "3"] },
        { q: ["Un rettangolo è lungo 6 cm e largo 4 cm. Quanto è la sua area?", "مستطيل طوله 6 سم وعرضه 4 سم. كم مساحته؟"], g: "24 cm²", s: ["20 cm²", "10 cm²", "48 cm²"] },
        { q: ["Qual è la media di 4, 6 e 8?", "ما متوسط الأعداد 4 و6 و8؟"], g: "6", s: ["5", "18", "7"] },
        { q: ["Un film dura 1 ora e 45 minuti. Inizia alle 20:30. A che ora finisce?", "فيلم مدته ساعة و45 دقيقة. يبدأ الساعة 20:30. متى ينتهي؟"], g: "22:15", s: ["21:75", "22:05", "21:45"] }
      ] },
    { id: "informatica", titolo: ["Informatica pratica", "المعلوماتية العملية"], minuti: 20,
      intro: ["Prima porti il robot alla bandiera con i blocchi, poi rispondi a poche domande.", "أولًا أوصل الروبوت إلى العلم باستخدام المكعبات، ثم أجب عن بعض الأسئلة."],
      robot: [
        { righe: ["R...B"] },
        { righe: ["R....", ".....", "....B"] },
        { righe: ["R.#..", "..#..", "....B"] },
        { righe: ["R#...", ".#.#.", ".#.#.", "...#B"] }
      ],
      domande: [
        { q: ["Un programma dice: «ripeti 3 volte: fai un passo avanti». Quanti passi fa il robot?", "برنامج يقول: «كرّر 3 مرات: خطوة إلى الأمام». كم خطوة يخطو الروبوت؟"], g: "3", s: ["1", "4", "6"] },
        { q: ["Che cos'è un algoritmo?", "ما هي الخوارزمية؟"], g: ["una serie di passi in ordine per risolvere un problema", "سلسلة من الخطوات بالترتيب لحل مشكلة"],
          s: [["un tipo di computer", "نوع من الحواسيب"], ["un virus", "فيروس"], ["un sito internet", "موقع إنترنت"]] },
        { q: ["Quale di questi serve per mettere dati DENTRO il computer?", "أي من هذه يُستخدم لإدخال البيانات إلى الحاسوب؟"], g: ["la tastiera", "لوحة المفاتيح"],
          s: [["il monitor", "الشاشة"], ["la stampante", "الطابعة"], ["le casse", "مكبرات الصوت"]] },
        { q: ["Nel sistema binario si usano solo le cifre…", "في النظام الثنائي نستخدم فقط الأرقام…"], g: ["0 e 1", "0 و 1"], s: [["da 0 a 9", "من 0 إلى 9"], ["1 e 2", "1 و 2"], ["A e B", "A و B"]] },
        { q: ["Il numero binario 101 vale, in decimale…", "العدد الثنائي 101 يساوي في النظام العشري…"], g: "5", s: ["101", "3", "6"] },
        { q: ["Una foto pesa 2 MB. Quante ne stanno in 10 MB?", "صورة حجمها 2 ميغابايت. كم صورة تتسع في 10 ميغابايت؟"], g: "5", s: ["20", "8", "12"] }
      ] },
    { id: "motivazione", titolo: ["Motivazione e autovalutazione", "الدافع والتقييم الذاتي"], minuti: 10,
      intro: ["Qui non ci sono risposte giuste o sbagliate. Rispondi sinceramente: serve solo a te.", "هنا لا توجد إجابات صحيحة أو خاطئة. أجب بصدق: هذا لك فقط."],
      scala: [["per niente", "أبدًا"], ["poco", "قليلًا"], ["abbastanza", "إلى حد ما"], ["molto", "كثيرًا"], ["moltissimo", "كثيرًا جدًا"]],
      frasi: [
        ["Mi piace capire come funzionano le cose (un'app, un gioco, un computer).", "أحب أن أفهم كيف تعمل الأشياء (تطبيق، لعبة، حاسوب)."],
        ["Mi piace usare il computer per CREARE qualcosa, non solo per giocare o guardare video.", "أحب أن أستخدم الحاسوب لأصنع شيئًا، وليس فقط للعب أو مشاهدة الفيديو."],
        ["Quando un problema è difficile, provo ancora invece di lasciar perdere.", "عندما تكون المشكلة صعبة، أحاول مرة أخرى بدلًا من الاستسلام."],
        ["Mi piacerebbe creare un videogioco, un sito o un'app.", "أود أن أصنع لعبة فيديو أو موقعًا أو تطبيقًا."],
        ["Mi piace montare, smontare o aggiustare oggetti e dispositivi.", "أحب تركيب الأشياء والأجهزة أو تفكيكها أو إصلاحها."],
        ["Mi piace lavorare in gruppo con i compagni.", "أحب العمل في مجموعة مع زملائي."],
        ["Mi piacerebbe fare un lavoro con i computer da grande.", "أود أن أعمل في مجال الحاسوب عندما أكبر."]
      ] }
  ]
};
