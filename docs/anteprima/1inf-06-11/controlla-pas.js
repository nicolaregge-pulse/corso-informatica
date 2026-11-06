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
    V.push(voce(cap, 'Il numero va nella frase con IntToStr( … ).', 'الرقم يدخل في الجملة بـ IntToStr( … ).', '数字用 IntToStr( … ) 放进句子。'));
    V.push(voce(testoUnito, 'La frase unisce pezzi di testo con il + (per esempio \' km in metri sono \').', 'الجملة تجمع قطع النص بـ +.', '句子用 + 把文字连起来。'));
    if (quale === 'scontrino') {
      var l1 = /\bStrToInt(Def)?\s*\(\s*Edit2\s*\.\s*Text/i.test(c) && /\bStrToInt(Def)?\s*\(\s*Edit3\s*\.\s*Text/i.test(c);
      V.push(voce(l1, 'Leggi prezzo e quantità: StrToInt(Edit2.Text) e StrToInt(Edit3.Text).', 'تقرأ السعر والكمية.', '读取价格和数量。'));
      V.push(voce(/'\s*euro fanno\s*'|fanno/i.test(c), 'La riga dice «… da … euro fanno … euro».', 'السطر يقول «… بـ … يورو = … يورو».', '这一行写「… 每个 … 欧元，一共 … 欧元」。'));
      V.push(voce(aggiunge, 'Livello 2: le righe si aggiungono: Label1.Caption := Label1.Caption + …', 'المستوى 2: الأسطر تُضاف.', '第 2 级：一行一行加上去。', true));
      V.push(voce(/StrToInt\s*\(\s*Label2\s*\.\s*Caption\s*\)/i.test(c) && /Label2\s*\.\s*Caption\s*:=\s*IntToStr/i.test(c), 'Livello 3: il totale in Label2 con StrToInt e IntToStr.', 'المستوى 3: المجموع في Label2.', '第 3 级：总数放在 Label2。', true));
      if (l1 && cap) { livello = 1; punti = 8; }
      if (livello && aggiunge) { livello = 2; punti = 14; }
      if (livello === 2 && /StrToInt\s*\(\s*Label2/i.test(c)) { livello = 3; punti = 20; }
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
