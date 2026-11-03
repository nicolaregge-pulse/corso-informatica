// 1INF 04/11/2026: controllo automatico di unit1.pas (convertitore, calcolatrice, cassiere).
// Solo un aiuto: NON blocca mai la consegna. Uso: ControllaPas(testo, ora) -> {ok, facile, voci:[{ok,avviso,it,ar,zh}], ora_trovata}
(function (g) {
  function pulisci(t) { return String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/\(\*[\s\S]*?\*\)/g, ' ').replace(/\/\/[^\n]*/g, ' '); }
  function senzaScritte(t) { return t.replace(/'[^'\n]*'/g, "''"); }
  function voce(ok, it, ar, zh, avviso) { return { ok: !!ok, avviso: !!avviso, it: it, ar: ar, zh: zh }; }
  function oraTrovata(c) {
    if (/\bmod\b/i.test(c) && /\bMemo1\b/i.test(c)) return 3;
    if (/StrToIntDef\s*\(\s*Edit2/i.test(c)) return 2;
    if (/\bdiv\b|\*\s*1000|\*\s*60\b/i.test(c)) return 1;
    return 0;
  }
  var FACILE = {
    1: /\bLabel1\s*\.\s*Caption\s*:=[^;]*\*\s*1000/i,
    2: /\bLabel1\s*\.\s*Caption\s*:=[^;]*StrToInt(Def)?\s*\(\s*Edit1[^;]*\+/i,
    3: /resto\s*:=\s*\w+\s*-\s*\w+/i
  };
  function ControllaPas(testo, ora) {
    var c0 = pulisci(testo), c = senzaScritte(c0), V = [];
    var unita = /\bunit\s+\w+\s*;/i.test(c) && /\bimplementation\b/i.test(c) && /\bend\s*\.\s*$/i.test(c.trim());
    V.push(voce(unita, 'È un file di Lazarus (una unit in Pascal).', 'هذا ملف Lazarus (وحدة Pascal).', '这是 Lazarus 文件（Pascal 单元）。'));
    if (!unita) {
      V.push(voce(false, 'Hai scelto il file giusto? Deve essere unit1.pas, nella cartella del progetto.', 'هل اخترت الملف الصحيح؟ يجب أن يكون unit1.pas في مجلد المشروع.', '选对文件了吗？必须是项目文件夹里的 unit1.pas。'));
      return { ok: false, voci: V, ora_trovata: 0 };
    }
    var clic = /procedure\s+TForm1\s*\.\s*Button1Click\s*\(/i.test(c);
    V.push(voce(clic, 'C\'è il clic del bottone: Button1Click.', 'يوجد نقر الزر: Button1Click.', '有按钮的点击：Button1Click。'));
    var nb = (c.match(/procedure\s+TForm1\s*\.\s*Button\d+Click\s*\(/gi) || []).length;
    if (ora === 1) {
      V.push(voce(/\bvar\b[\s\S]*?:\s*Integer\s*;[\s\S]*?\bbegin\b/i.test(c), 'Ci sono variabili Integer: var km, metri: Integer;', 'توجد متغيرات Integer.', '有 Integer 变量。'));
      V.push(voce(/\bStrToInt(Def)?\s*\(\s*Edit1\s*\.\s*Text/i.test(c), 'Il bottone legge la casella: StrToInt(Edit1.Text).', 'الزر يقرأ الخانة: StrToInt(Edit1.Text).', '按钮读取输入框：StrToInt(Edit1.Text)。'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=[^;]*IntToStr\s*\(/i.test(c), 'Il risultato va nella Caption con IntToStr( … ).', 'النتيجة تذهب إلى Caption بـ IntToStr( … ).', '结果用 IntToStr( … ) 放进 Caption。'));
      V.push(voce(/\*\s*1000\b/.test(c), 'Km in metri: * 1000.', 'كم إلى متر: * 1000.', '公里变米：* 1000。'));
      V.push(voce(/\*\s*60\b/.test(c), 'Ore in minuti: * 60.', 'ساعات إلى دقائق: * 60.', '小时变分钟：* 60。', true));
      V.push(voce(/\*\s*100\b(?!0)/.test(c), 'Euro in centesimi: * 100.', 'يورو إلى سنت: * 100.', '欧元变分：* 100。', true));
      V.push(voce(/9\s*\)?\s*div\s*5\s*\)?\s*\+\s*32/i.test(c), 'Celsius in Fahrenheit: C * 9 div 5 + 32.', 'سيلسيوس إلى فهرنهايت: C * 9 div 5 + 32.', '摄氏变华氏：C * 9 div 5 + 32。', true));
      V.push(voce(/\bdiv\s+60\b/i.test(c) && /\bmod\s+60\b/i.test(c), 'Minuti in ore e minuti: div 60 e mod 60.', 'دقائق إلى ساعات ودقائق: div 60 و mod 60.', '分钟变小时和分钟：div 60 和 mod 60。', true));
      V.push(voce(nb >= 3, 'Hai almeno 3 bottoni con il loro codice.', 'لديك 3 أزرار على الأقل بكودها.', '至少有 3 个按钮和它们的代码。', true));
    } else if (ora === 2) {
      V.push(voce(/\bStrToIntDef\s*\(\s*Edit1\s*\.\s*Text\s*,/i.test(c) && /\bStrToIntDef\s*\(\s*Edit2\s*\.\s*Text\s*,/i.test(c), 'Leggi le due caselle con StrToIntDef(Edit1.Text, 0) e StrToIntDef(Edit2.Text, 0).', 'تقرأ الخانتين بـ StrToIntDef.', '用 StrToIntDef 读取两个输入框。'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=[^;]*'[^']*'[^;]*IntToStr\s*\(/i.test(c0) || /\bLabel1\s*\.\s*Caption\s*:=[^;]*IntToStr[^;]*\+\s*''/i.test(c), 'Il risultato è una frase: IntToStr(a) + \' più \' + …', 'النتيجة جملة.', '结果是一句话。'));
      V.push(voce(/IntToStr\s*\(\s*a\s*\+\s*b\s*\)/i.test(c), 'Il bottone + : IntToStr(a + b).', 'زر الجمع.', '加号按钮。'));
      V.push(voce(/IntToStr\s*\(\s*a\s*-\s*b\s*\)/i.test(c), 'Il bottone − : IntToStr(a - b).', 'زر الطرح.', '减号按钮。', true));
      V.push(voce(/IntToStr\s*\(\s*a\s*\*\s*b\s*\)/i.test(c), 'Il bottone × : IntToStr(a * b).', 'زر الضرب.', '乘号按钮。', true));
      V.push(voce(/IntToStr\s*\(\s*a\s+div\s+b\s*\)/i.test(c), 'Il bottone ÷ : IntToStr(a div b).', 'زر القسمة.', '除号按钮。', true));
      V.push(voce(/\bif\s+b\s*=\s*0\s+then\b/i.test(c), 'Bonus: if b = 0 then … (niente divisione per zero).', 'إضافي: if b = 0 then …', '加分：if b = 0 then …', true));
    } else if (ora === 3) {
      V.push(voce(/\bStrToInt(Def)?\s*\(\s*Edit2\s*\.\s*Text/i.test(c) && /\bStrToInt(Def)?\s*\(\s*Edit3\s*\.\s*Text/i.test(c), 'Leggi prezzo e soldi dati: StrToIntDef(Edit2.Text, 0) e StrToIntDef(Edit3.Text, 0).', 'تقرأ السعر والمبلغ.', '读取价格和给的钱。'));
      V.push(voce(/\w+\s*:=\s*\w+\s*-\s*\w+\s*;/.test(c), 'Calcoli il resto: dati - prezzo.', 'تحسب الباقي.', '计算找零。'));
      V.push(voce(/\bdiv\s+10\b/i.test(c) && /\bmod\s+10\b/i.test(c), 'Banconote da 10 con div 10 e mod 10.', 'أوراق 10 بـ div و mod.', '用 div 10 和 mod 10 算 10 元钞票。', true));
      V.push(voce(/\bMemo1\s*\.\s*Lines\s*\.\s*Add\s*\(/i.test(c), 'Lo scontrino usa Memo1.Lines.Add( … ).', 'الإيصال يستعمل Memo1.Lines.Add.', '小票用 Memo1.Lines.Add。'));
      V.push(voce(/'[^']*'\s*\+\s*Edit1\s*\.\s*Text/i.test(c0), 'Il nome del cliente è unito con +: \'Cliente: \' + Edit1.Text.', 'اسم الزبون ملصق بـ +.', '顾客名字用 + 连接。'));
    }
    var errori = V.filter(function (v) { return !v.ok && !v.avviso; }).length, fac = false;
    if (errori > 0 && clic && FACILE[ora] && FACILE[ora].test(c)) {
      fac = true; V.forEach(function (v) { if (!v.ok) v.avviso = true; });
      V.push(voce(true, 'Percorso facilitato: il codice è giusto. Bravo! Le righe gialle sono per chi fa il percorso completo.', 'المسار الميسّر: الكود صحيح. أحسنت!', '简单路线：代码正确。真棒！'));
      errori = 0;
    }
    return { ok: errori === 0, facile: fac, voci: V, ora_trovata: oraTrovata(c) };
  }
  g.ControllaPas = ControllaPas;
  if (typeof module !== 'undefined') module.exports = ControllaPas;
})(typeof window !== 'undefined' ? window : globalThis);
