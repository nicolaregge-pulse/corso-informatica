// 1INF laboratorio 30/10/2026: controllo automatico del file unit1.pas (piano A della consegna).
// Legge il testo del file e dice, con parole semplici, se dentro ci sono i pezzi giusti per quell'ora.
// NON blocca mai la consegna: è solo un aiuto. Lo stesso controllo, in Python, lo fa il cruscotto del prof
// (riservato: generatori/cruscotto_1inf_lab3010.py). Uso: ControllaPas(testo, ora) -> {ok, voci:[{ok, it, ar, zh}], ora_trovata}
(function (g) {
  function pulisci(t) {   // toglie i commenti { … }, (* … *), // … e le scritte tra apici (per cercare il codice vero)
    return String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/\(\*[\s\S]*?\*\)/g, ' ').replace(/\/\/[^\n]*/g, ' ');
  }
  function senzaScritte(t) { return t.replace(/'[^'\n]*'/g, "''"); }
  function scritte(t) { var m = t.match(/'[^'\n]*'/g) || []; return m.map(function (s) { return s.slice(1, -1); }); }
  function voce(ok, it, ar, zh, solo_avviso) { return { ok: !!ok, avviso: !!solo_avviso, it: it, ar: ar, zh: zh }; }
  function oraTrovata(c) {   // quale esercitazione è (serve al cruscotto quando i file arrivano senza nome)
    if (/\bStrToInt\s*\(/i.test(c)) return 3;
    if (/\bEdit\d+\s*\.\s*Text\b/i.test(c)) return 2;
    if (/\bCaption\s*:=/i.test(c)) return 1;
    return 0;
  }
  function ControllaPas(testo, ora) {
    var grezzo = String(testo || ''), c0 = pulisci(grezzo), c = senzaScritte(c0), S = scritte(c0), V = [];
    var unita = /\bunit\s+\w+\s*;/i.test(c) && /\bimplementation\b/i.test(c) && /\bend\s*\.\s*$/i.test(c.trim());
    V.push(voce(unita, 'È un file di Lazarus (una unit in Pascal).', 'هذا ملف Lazarus (وحدة Pascal).', '这是 Lazarus 文件（Pascal 单元）。'));
    if (!unita) {
      V.push(voce(false, 'Hai scelto il file giusto? Deve essere unit1.pas, nella cartella del progetto.', 'هل اخترت الملف الصحيح؟ يجب أن يكون unit1.pas في مجلد المشروع.', '选对文件了吗？必须是项目文件夹里的 unit1.pas。'));
      return { ok: false, voci: V, ora_trovata: 0 };
    }
    var clic = /procedure\s+TForm1\s*\.\s*Button1Click\s*\(/i.test(c);
    V.push(voce(clic, 'C\'è il clic del bottone: Button1Click.', 'يوجد نقر الزر: Button1Click.', '有按钮的点击：Button1Click。'));
    if (ora === 1) {
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=\s*'[^']*'\s*\+\s*'/i.test(c0), 'Testo: due String attaccate con +, per esempio \'5\' + \'3\'.', 'Testo: نصّان ملصوقان بـ +، مثلاً \'5\' + \'3\'.', 'Testo：两个 String 用 + 连起来，比如 \'5\' + \'3\'。'));
      V.push(voce(/\bvar\b[\s\S]*?:\s*Integer\s*;[\s\S]*?\bbegin\b/i.test(c), 'Numeri: ci sono variabili Integer: var a, b: Integer;', 'Numeri: توجد متغيرات Integer: var a, b: Integer;', 'Numeri：有 Integer 变量：var a, b: Integer;'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=\s*IntToStr\s*\(/i.test(c), 'Numeri: il risultato va nella Caption con IntToStr( … ).', 'Numeri: النتيجة تذهب إلى الـ Caption بـ IntToStr( … ).', 'Numeri：结果用 IntToStr( … ) 放进 Caption。'));
      var nums = (c.match(/:=\s*-?\d+\s*;/g) || []).map(function (x) { return x.replace(/\D/g, ''); }), lett = S.filter(function (s) { return /^\s*-?\d+\s*$/.test(s); });
      V.push(voce(nums.concat(lett).some(function (x) { return x.trim() !== '5' && x.trim() !== '3'; }), 'Ci sono numeri tuoi (non solo 5 e 3).', 'توجد أرقام خاصة بك (ليس فقط 5 و3).', '有你自己的数字（不只是 5 和 3）。', true));
    } else if (ora === 2) {
      V.push(voce(/\bvar\b[\s\S]*?:\s*String\s*;[\s\S]*?\bbegin\b/i.test(c), 'C\'è una variabile String: var nome: String;', 'يوجد متغير String: var nome: String;', '有一个 String 变量：var nome: String;'));
      V.push(voce(/:=\s*Edit1\s*\.\s*Text\s*;/i.test(c), 'Il programma legge la casella: … := Edit1.Text;', 'البرنامج يقرأ الخانة: … := Edit1.Text;', '程序读取输入框：… := Edit1.Text;'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=[^;]*\+/i.test(c), 'La frase si attacca con +: Label1.Caption := … + …;', 'الجملة تُلصق بـ +: Label1.Caption := … + …;', '句子用 + 连起来：Label1.Caption := … + …;'));
      var frasi = S.filter(function (s) { return s.trim().length > 1 && s.trim() !== '...' && s.trim() !== 'detto' && s !== '!'; });
      V.push(voce(frasi.length > 0, 'C\'è una frase tua (non solo «detto»).', 'توجد جملة خاصة بك (ليس فقط «detto»).', '有你自己的句子（不只是 «detto»）。', true));
    } else if (ora === 3) {
      V.push(voce(/\bvar\b[\s\S]*?:\s*Integer\s*;[\s\S]*?\bbegin\b/i.test(c), 'C\'è una variabile Integer: var punti: Integer;', 'يوجد متغير Integer: var punti: Integer;', '有一个 Integer 变量：var punti: Integer;'));
      V.push(voce(/\bStrToInt\s*\(/i.test(c), 'C\'è StrToInt: il testo diventa un numero.', 'يوجد StrToInt: النص يصبح رقماً.', '有 StrToInt：文字变成数字。'));
      V.push(voce(/\bIntToStr\s*\(/i.test(c), 'C\'è IntToStr: il numero torna testo per la Caption.', 'يوجد IntToStr: الرقم يعود نصاً للـ Caption.', '有 IntToStr：数字变回文字给 Caption。'));
      V.push(voce(/\bStrToInt\s*\(\s*Edit1\s*\.\s*Text\s*\)/i.test(c), 'Il bottone Aggiungi legge la casella: StrToInt(Edit1.Text).', 'زر Aggiungi يقرأ الخانة: StrToInt(Edit1.Text).', 'Aggiungi 按钮读取输入框：StrToInt(Edit1.Text)。', true));
    }
    var errori = V.filter(function (v) { return !v.ok && !v.avviso; }).length;
    return { ok: errori === 0, voci: V, ora_trovata: oraTrovata(c) };
  }
  g.ControllaPas = ControllaPas;
  if (typeof module !== 'undefined') module.exports = ControllaPas;
})(typeof window !== 'undefined' ? window : globalThis);
