// 1INF 06/11/2026: controllo automatico di unit1.pas («Il convertitore che parla» e, se avanza tempo, «Lo scontrino che parla»).
// Solo un aiuto: NON blocca mai la consegna. Uso: ControllaPas(testo, 'conv' | 'scontrino') -> {ok, livello, punti, voci:[{ok,avviso,it,ar,zh}]}
// punti (0-20) = la parte Lazarus del voto proposto (config/lezione/1inf-2026-11-06.json): livello 1 = 8, livello 2 = +6, livello 3 o Fallo tuo = +6.
(function (g) {
  function pulisci(t) { return String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/\(\*[\s\S]*?\*\)/g, ' ').replace(/\/\/[^\n]*/g, ' '); }
  function voce(ok, it, ar, zh, avviso) { return { ok: !!ok, avviso: !!avviso, it: it, ar: ar, zh: zh }; }
  function ControllaPas(testo, quale) {
    var c = pulisci(testo), V = [], punti = 0, livello = 0;
    var unita = /\bunit\s+\w+\s*;/i.test(c) && /\bimplementation\b/i.test(c) && /\bend\s*\.\s*$/i.test(c.trim());
    V.push(voce(unita, 'È un file di Lazarus (una unit in Pascal).', 'هذا ملف Lazarus (وحدة Pascal).', '这是 Lazarus 文件（Pascal 单元）。'));
    if (!unita) {
      V.push(voce(false, 'Hai scelto il file giusto? Deve essere unit1.pas, nella cartella del progetto.', 'هل اخترت الملف الصحيح؟ يجب أن يكون unit1.pas في مجلد المشروع.', '选对文件了吗？必须是项目文件夹里的 unit1.pas。'));
      return { ok: false, livello: 0, punti: 0, voci: V };
    }
    var nb = (c.match(/procedure\s+TForm1\s*\.\s*Button\d+Click\s*\(/gi) || []).length;
    var s2i = /\bStrToInt(Def)?\s*\(\s*Edit1\s*\.\s*Text/i.test(c), cap = /Label1\s*\.\s*Caption\s*:=[^;]*IntToStr\s*\(/i.test(c);
    var testoUnito = /Label1\s*\.\s*Caption\s*:=[^;]*'[^']*'\s*\+|\+\s*'[^']*'[^;]*;/i.test(c);
    var aggiunge = /Label1\s*\.\s*Caption\s*:=\s*Label1\s*\.\s*Caption\s*\+/i.test(c);
    var cicli = /\b(for|while|repeat)\b/i.test(c);
    V.push(voce(/procedure\s+TForm1\s*\.\s*Button1Click\s*\(/i.test(c), 'C\'è il clic del bottone: Button1Click.', 'يوجد نقر الزر: Button1Click.', '有按钮的点击：Button1Click。'));
    if (quale !== 'scontrino') V.push(voce(s2i, 'Il bottone legge la casella: StrToInt(Edit1.Text).', 'الزر يقرأ الخانة: StrToInt(Edit1.Text).', '按钮读取输入框：StrToInt(Edit1.Text)。'));
    if (quale !== 'scontrino') V.push(voce(cap, 'Il numero va nella frase con IntToStr( … ).', 'الرقم يدخل في الجملة بـ IntToStr( … ).', '数字用 IntToStr( … ) 放进句子。'));
    V.push(voce(testoUnito, 'La frase unisce pezzi di testo con il + (per esempio \' km in metri sono \').', 'الجملة تجمع قطع النص بـ +.', '句子用 + 把文字连起来。'));
    if (quale === 'scontrino') {
      var memo = /Memo1\s*\.\s*Lines\s*\.\s*Add\s*\(/i.test(c);
      var l1 = memo && /Edit1\s*\.\s*Text/i.test(c) && /Edit2\s*\.\s*Text/i.test(c) && /'[^']*'\s*\+|\+\s*'[^']*'/.test(c);
      var l2 = /\bStrToInt(Def)?\s*\(\s*Edit2\s*\.\s*Text/i.test(c) && /\bStrToInt(Def)?\s*\(\s*Edit3\s*\.\s*Text/i.test(c) && /\bif\b[^;]*\bthen\b/i.test(c) && /\belse\b/i.test(c) && /IntToStr\s*\(/i.test(c) && /'\s*x\s*'/i.test(c);
      var l3 = /StrToInt\s*\(\s*Label2\s*\.\s*Caption\s*\)/i.test(c) && /Label2\s*\.\s*Caption\s*:=\s*IntToStr/i.test(c) && /Edit3\s*\.\s*Text\s*:=\s*'1'/i.test(c);
      V.push(voce(memo, 'Lo scontrino si scrive nella Memo: Memo1.Lines.Add( … ); una riga per volta.', 'الإيصال يُكتب في Memo: Memo1.Lines.Add( … );', '小票写在 Memo 里：Memo1.Lines.Add( … );'));
      V.push(voce(l1, 'Livello 1: una riga semplice con il + (per esempio prodotto, spazio, prezzo, euro).', 'المستوى 1: سطر بسيط بـ +.', '第 1 级：用 + 写一行简单的。'));
      V.push(voce(l2, 'Livello 2: if quanti > 1 then … else …, con la x: «3 x pizze da 5 euro: 15 euro».', 'المستوى 2: if مع x.', '第 2 级：用 if 加 x。', true));
      V.push(voce(l3, 'Livello 3: il totale in Label2 (StrToInt e IntToStr) e Edit3.Text := \'1\' dopo ogni riga.', 'المستوى 3: المجموع في Label2 وإعادة Edit3 إلى 1.', '第 3 级：总数放在 Label2，每行之后 Edit3 变回 1。', true));
      V.push(voce(/Edit1\s*\.\s*SetFocus/i.test(c), 'Comodo: Edit1.Clear; Edit2.Clear; Edit1.SetFocus; (caselle pulite, cursore sul prodotto).', 'مريح: تنظيف الخانات والمؤشر على المنتج.', '方便：清空输入框，光标回到商品。', true));
      if (l1) { livello = 1; punti = 8; }
      if (l1 && l2) { livello = 2; punti = 14; }
      if (livello === 2 && l3) { livello = 3; punti = 20; }
    } else {
      var km = /\*\s*1000\b/.test(c), cm = /\*\s*100\b(?!0)/.test(c), min = /\*\s*60\b/.test(c);
      var l1 = s2i && cap && testoUnito && km;
      V.push(voce(km, 'Livello 1: km in metri (* 1000) con la frase «7 km in metri sono 7000 metri».', 'المستوى 1: كم إلى متر (* 1000).', '第 1 级：公里变米（* 1000）。'));
      V.push(voce(cm && min && nb >= 4, 'Livello 2: almeno 4 bottoni (m→cm * 100, ore→minuti * 60, euro→centesimi * 100).', 'المستوى 2: 4 أزرار على الأقل.', '第 2 级：至少 4 个按钮。', true));
      V.push(voce(aggiunge || /Edit2\s*\.\s*Text/i.test(c), 'Livello 3: la frase composta (Label1.Caption := Label1.Caption + … o il tuo nome da Edit2).', 'المستوى 3: الجملة المركّبة.', '第 3 级：组合句子。', true));
      V.push(voce(nb >= 6 || (nb >= 5 && aggiunge), 'Fallo tuo: un bottone in più con la tua conversione e la frase scherzosa.', 'اصنعه بنفسك: زر إضافي بتحويلك.', '自己做：多一个按钮，用你的换算。', true));
      if (l1) { livello = 1; punti = 8; }
      if (l1 && cm && min && nb >= 4) { livello = 2; punti = 14; }
      if (livello === 2 && (aggiunge || /Edit2\s*\.\s*Text/i.test(c) || nb >= 5)) { livello = 3; punti = 20; }
    }
    if (cicli) V.push(voce(false, 'Oggi niente cicli (for, while): solo somme di stringhe.', 'اليوم بدون حلقات: فقط جمع النصوص.', '今天不用循环：只把文字加起来。', true));
    var errori = V.filter(function (v) { return !v.ok && !v.avviso; }).length;
    return { ok: errori === 0, livello: livello, punti: punti, voci: V };
  }
  g.ControllaPas = ControllaPas;
  if (typeof module !== 'undefined') module.exports = ControllaPas;
})(typeof window !== 'undefined' ? window : globalThis);
