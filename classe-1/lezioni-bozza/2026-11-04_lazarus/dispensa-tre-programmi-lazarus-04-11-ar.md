# ثلاثة برامج في Lazarus

*محوّل القياسات · آلة حاسبة بأربعة أزرار · أمين الصندوق*

مذكرة · الصف 1INF · المختبر · 04/11/2026 · الإصدار 1.0

اليوم تصنع ثلاثة برامج حقيقية. كل برنامج يعمل فوراً ويمكنك أن تجرّبه مع زميل. الكود هنا هو نفسه الموجود في صفحات الدرس. إذا أخطأت فلا مشكلة: يحدث هذا لكل المبرمجين، حتى المحترفين.

## 01 كيف تشغّل البرنامج

*رسم توضيحي (ليس لقطة شاشة): أين تضغط وأين يظهر البرنامج.* (schema nel PDF)

1. احفظ بـ `Ctrl` + `S`.
2. اضغط `F9` أو الزر الأخضر ذا المثلث (**Esegui**) تحت القوائم.
3. انتظر بضع ثوانٍ: في الأسفل، في نافذة **Messaggi**، يبني Lazarus البرنامج. إذا ظهر سطر أحمر فهناك خطأ (انظر الأخطاء الشائعة في كل برنامج).
4. نافذتك تفتح **فوق** Lazarus مثل برنامج حقيقي. لا تراها؟ ابحث عنها في شريط Windows السفلي.
5. جرّب البرنامج: اكتب الأرقام في الخانات واضغط الأزرار.
6. لإيقافه: اضغط **X** الحمراء أعلى يمين نافذتك. إذا تجمّد: اضغط `Ctrl` + `F2` داخل Lazarus.
7. ارجع وعدّل: الكود والنافذة ما زالا هناك. غيّر واحفظ واضغط `F9` من جديد.

> **أين يوجد البرنامج:** عند الضغط على `F9` ينشئ Lazarus في مجلد المشروع (مثلاً `Documenti\convertitore`) ملفاً باسم المشروع وينتهي بـ `.exe`، مثل `convertitore.exe`. هذا هو برنامجك: بنقرة مزدوجة يعمل حتى بدون Lazarus. إذا لم تجده فلم يُبنَ البرنامج: انظر نافذة Messaggi.

## 02 الخطوات المتكررة (للبرامج الثلاثة)

هذه الخطوات الست تكررها في كل برنامج. في الوصفات أدناه ستجد الحرف (A…F): انظر إلى الرسم الذي يحمل نفس الحرف.

1. **A**: مشروع جديد: Progetto ← Nuovo progetto… ← Applicazione ← OK
2. **B**: احفظ: مجلد جديد في Documenti ثم Salva مرتين
3. **C**: لوحة Standard: اضغط المكوّن ثم النافذة
4. **D**: Ispettore oggetti: غيّر Caption أو Text
5. **E**: نقرة مزدوجة على الزر: يفتح الكود
6. **F**: F9: يبدأ البرنامج

### كلمات يجب معرفتها

| الكلمة | ماذا تفعل | مثال |
|---|---|---|
| `StrToInt('5')` | من نص إلى رقم (يتوقف إذا لم يكن رقماً) | `'5'` تصبح `5` |
| `StrToIntDef('ab', 0)` | من نص إلى رقم؛ وإن لم يصلح يستعمل 0 ولا يتوقف | `'ab'` تصبح `0`؛ `'7'` تصبح `7` |
| `IntToStr(5000)` | من رقم إلى نص | `5000` تصبح `'5000'` |
| `div` | قسمة بدون فاصلة | `17 div 5 = 3` |
| `mod` | الباقي | `17 mod 5 = 2` |
| `+` con testi | يلصق نصين | `'Ciao ' + 'Anna'` |

> **نص مقابل رقم:** `'5' + '3'` تعطي `'53'` (نصان ملصوقان). `5 + 3` تعطي `8` (رقمان). لذلك نحوّل دائماً: من نص إلى رقم لنحسب، ثم من رقم إلى نص لنكتب النتيجة.

## 03 البرنامج 1: محوّل القياسات

**فائدته.** تكتب رقماً وتضغط زراً فيحوّله البرنامج: كيلومترات إلى أمتار، ساعات إلى دقائق، يورو إلى سنتات، سيلسيوس إلى فهرنهايت، دقائق إلى ساعات ودقائق. **عندما يعمل** ترى هذا:

*رسم توضيحي: المحوّل بعد الانتهاء.* (schema nel PDF)

*رسم بأرقام: الأرقام الحمراء هي أرقام الجدول.* (schema nel PDF)

| N. | Name | النوع | ماذا تغيّر |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` فارغ |
| 2 | `Label1` | TLabel | لا شيء (يملؤها الكود) |
| 3 | `Button1` | TButton | `Caption` = `Km in metri` |
| 4 | `Button2` | TButton | `Caption` = `Ore in minuti` |
| 5 | `Button3` | TButton | `Caption` = `Euro in centesimi` |
| 6 | `Button4` | TButton | `Caption` = `Celsius in Fahrenheit` |
| 7 | `Button5` | TButton | `Caption` = `Minuti in ore e minuti` |

### الوصفة، خطوة واحدة في كل سطر

1. [A] افتح Lazarus: القائمة `Progetto` ثم `Nuovo progetto…` ثم `Applicazione` ثم `OK`.
2. [B] القائمة `Progetto` ثم `Salva progetto con nome…`: في `Documenti` أنشئ مجلداً باسم `convertitore` واكتب `convertitore` كاسم للملف واضغط `Salva` (ثم `Salva` مرة أخرى لـ `unit1.pas`).
3. [C] لوحة `Standard`: اضغط `TEdit` ثم اضغط على النافذة في الأعلى.
4. [C] اضغط `TLabel` ثم اضغط على النافذة تحت الخانة.
5. [C] اضغط `TButton` ثم اضغط على النافذة تحت الملصق.
6. [D] اضغط `Button1`. في Ispettore oggetti اكتب في `Caption`: `Km in metri`.
7. [D] اضغط `Edit1`. في Ispettore احذف قيمة `Text`: يجب أن تبقى فارغة.
8. [E] انقر مرتين على `Button1`: يفتح الكود.
9. بين `begin` و `end;` كتب Lazarus البداية. أكمل المعالج هكذا (الكود الكامل أدناه):

```
procedure TForm1.Button1Click(Sender: TObject);
var
  km, metri: Integer;
begin
  km := StrToInt(Edit1.Text);
  metri := km * 1000;
  Label1.Caption := IntToStr(metri) + ' metri';
end;
```

10. [F] اضغط `F9` واكتب `5` في الخانة واضغط الزر.

> **انتصار سريع (5 دقائق):** مع `5` يجب أن يظهر **5000 metri**. تمّ! لقد صنعت أول برنامج لك.

**الأزرار الأربعة الأخرى:** بنفس الطريقة (ضع الزر، اكتب `Caption`، انقر مرتين، انسخ الكود). يتغير الكود في العملية الحسابية فقط.

ساعات إلى دقائق (`Button2`). جرّب `2`: **120 minuti**.

```
procedure TForm1.Button2Click(Sender: TObject);
var
  ore, minuti: Integer;
begin
  ore := StrToInt(Edit1.Text);
  minuti := ore * 60;
  Label1.Caption := IntToStr(minuti) + ' minuti';
end;
```

يورو إلى سنتات (`Button3`). جرّب `3`: **300 centesimi**.

```
procedure TForm1.Button3Click(Sender: TObject);
var
  euro, centesimi: Integer;
begin
  euro := StrToInt(Edit1.Text);
  centesimi := euro * 100;
  Label1.Caption := IntToStr(centesimi) + ' centesimi';
end;
```

سيلسيوس إلى فهرنهايت (`Button4`). `c * 9 div 5 + 32`. جرّب `100`: **212**.

```
procedure TForm1.Button4Click(Sender: TObject);
var
  c, f: Integer;
begin
  c := StrToInt(Edit1.Text);
  f := c * 9 div 5 + 32;
  Label1.Caption := IntToStr(c) + ' gradi C sono ' + IntToStr(f) + ' gradi F';
end;
```

دقائق إلى ساعات ودقائق (`Button5`): `div` تعطي الساعات الكاملة و`mod` الباقي. جرّب `135`: **ساعتان و15 دقيقة**.

```
procedure TForm1.Button5Click(Sender: TObject);
var
  minuti, ore, resto: Integer;
begin
  minuti := StrToInt(Edit1.Text);
  ore := minuti div 60;
  resto := minuti mod 60;
  Label1.Caption := IntToStr(minuti) + ' minuti sono ' + IntToStr(ore) + ' ore e ' + IntToStr(resto) + ' minuti';
end;
```

### ماذا تفعل التعليمات الجديدة

`StrToInt(Edit1.Text)` يقرأ نص الخانة ويحوّله إلى رقم: إذا كتبت `5` يصبح `5`. `IntToStr(metri)` يفعل العكس: `5000` تصبح النص `'5000'` الذي نضعه في الملصق. `135 div 60` = `2` و `135 mod 60` = `15`.

### الأخطاء الثلاثة الأكثر شيوعاً

| ماذا ترى | ماذا يعني | الحل |
|---|---|---|
| `Identifier not found "Edit1"` | المكوّن مفقود أو أن الاسم في الكود يختلف عن `Name` في Ispettore. | تأكد أن على النافذة `Edit1` و`Label1` و`Button1`. اكتب الاسم مطابقاً تماماً (مع الأحرف الكبيرة). |
| `Incompatible types` | وضعت نصاً حيث يلزم رقم أو رقماً حيث يلزم نص. | للحساب: `StrToInt(...)`. للكتابة في الملصق: `IntToStr(...)`. |
| يُغلق البرنامج أو تظهر نافذة فيها `"5a" is an invalid integer` | الرقم في الخانة غير مكتوب جيداً: حروف أو فراغات أو فاصلة أو أن الخانة فارغة. | اكتب أرقاماً صحيحة فقط (`5` وليس `5,5` ولا `5 km`). ثم اضغط الزر من جديد. |

> **اجعله لك:** غيّر كتابة الزر وعنوان النافذة (`Caption` الخاصة بـ Form) واللون (`Color`). أضف زراً واحداً بتحويل تحبه (مثلاً أمتار إلى سنتيمترات: `* 100`).

## 04 البرنامج 2: آلة حاسبة بأربعة أزرار

**فائدته.** تكتب رقمين وتضغط `+` أو `-` أو `*` أو `/` فيكتب البرنامج جملة فيها النتيجة. **عندما يعمل** ترى هذا:

*رسم توضيحي: الآلة الحاسبة بعد الانتهاء.* (schema nel PDF)

*رسم بأرقام: الأرقام الحمراء هي أرقام الجدول.* (schema nel PDF)

| N. | Name | النوع | ماذا تغيّر |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` فارغ |
| 2 | `Edit2` | TEdit | `Text` فارغ |
| 3 | `Button1` | TButton | `Caption` = `+` |
| 4 | `Button2` | TButton | `Caption` = `-` |
| 5 | `Button3` | TButton | `Caption` = `*` |
| 6 | `Button4` | TButton | `Caption` = `/` |
| 7 | `Label1` | TLabel | لا شيء (يملؤها الكود) |

### الوصفة، خطوة واحدة في كل سطر

1. [A] القائمة `Progetto` ثم `Nuovo progetto…` ثم `Applicazione` ثم `OK`.
2. [B] `Progetto` ثم `Salva progetto con nome…`: مجلد `calcolatrice` في `Documenti` واسم الملف `calcolatrice` ثم `Salva` مرتين.
3. [C] لوحة `Standard`: اضغط `TEdit` ثم النافذة. ثم `TEdit` ثانية تحت الأولى.
4. [C] اضغط `TButton` ثم النافذة. كرر أربع مرات في صف.
5. [C] اضغط `TLabel` ثم النافذة تحت الأزرار.
6. [D] اضغط كل زر واكتب `Caption`: `+` ثم `-` ثم `*` ثم `/`.
7. [D] اضغط `Edit1` وأفرغ `Text`. افعل نفس الشيء مع `Edit2`.
8. [E] انقر مرتين على الزر `+` (`Button1`). أكمل المعالج هكذا:

```
procedure TForm1.Button1Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' più ' + IntToStr(b) + ' fa ' + IntToStr(a + b);
end;
```

9. [F] اضغط `F9` واكتب `7` و`5` ثم اضغط `+`.

> **انتصار سريع (5 دقائق):** يجب أن تظهر الجملة **7 più 5 fa 12**.

**الأزرار الثلاثة الأخرى:** انقر مرتين على `-` ثم `*` ثم `/` وانسخ. تتغير العملية والكلمة فقط. جرّب `7` و`5`: **7 meno 5 fa 2** و**7 per 5 fa 35**.

```
procedure TForm1.Button2Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' meno ' + IntToStr(b) + ' fa ' + IntToStr(a - b);
end;
```

```
procedure TForm1.Button3Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' per ' + IntToStr(b) + ' fa ' + IntToStr(a * b);
end;
```

زر `/` يفحص الصفر بـ `if`: لا يمكن القسمة على صفر. جرّب `8` و`0`: **Non si può dividere per zero**. مع `8` و`2`: **8 diviso 2 fa 4**.

```
procedure TForm1.Button4Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  if b = 0 then
    Label1.Caption := 'Non si può dividere per zero'
  else
    Label1.Caption := IntToStr(a) + ' diviso ' + IntToStr(b) + ' fa ' + IntToStr(a div b);
end;
```

### ماذا تفعل التعليمات الجديدة

`StrToIntDef(Edit1.Text, 0)` يقرأ الرقم، وإذا كانت الخانة فارغة أو فيها حروف يستعمل `0` بدل أن يتوقف: `'7'` تعطي `7` و`'ab'` تعطي `0`. `if b = 0 then … else …` تعني: **إذا** كان b صفراً افعل الأول و**وإلا** افعل الثاني. `8 div 2` تعطي `4`.

### الأخطاء الثلاثة الأكثر شيوعاً

| ماذا ترى | ماذا يعني | الحل |
|---|---|---|
| `Identifier not found "Edit2"` | الخانة الثانية `Edit` مفقودة أو الاسم مختلف. | ضع `TEdit` ثانية على النافذة وتأكد أن اسمها `Edit2`. |
| `Incompatible types` | نص مقابل رقم: كتبت `Label1.Caption := a + b`. | للكتابة في الملصق يلزم نص: `IntToStr(a + b)`. |
| يُغلق البرنامج مع `Division by zero` | قسمت على صفر وينقص الفحص `if b = 0`. | انسخ كود زر `/` مع `if`. جرّب `8` و`0`. |

> **اجعله لك:** غيّر عنوان النافذة والألوان والجمل (مثلاً بدل `più` اكتب `sommato a`).

## 05 البرنامج 3: أمين الصندوق

**فائدته.** تكتب اسم الزبون والسعر والمبلغ المدفوع فيحسب البرنامج الباقي ويقول كم ورقة وعملة معدنية يلزم ويكتب الإيصال باسم الزبون. **عندما يعمل** ترى هذا:

*رسم توضيحي: الإيصال بعد الانتهاء.* (schema nel PDF)

*رسم بأرقام: الأرقام الحمراء هي أرقام الجدول.* (schema nel PDF)

| N. | Name | النوع | فائدته |
|---|---|---|---|
| 1 | `Edit1` | TEdit | اسم الزبون (`Text` فارغ) |
| 2 | `Edit2` | TEdit | السعر (`Text` فارغ) |
| 3 | `Edit3` | TEdit | المبلغ المدفوع (`Text` فارغ) |
| 4 | `Button1` | TButton | `Caption` = `Calcola il resto` |
| 5 | `Label1` | TLabel | تكتب الباقي |
| 6 | `Memo1` | TMemo | الإيصال (أسطر فارغة) |

### الوصفة، خطوة واحدة في كل سطر

1. [A] القائمة `Progetto` ثم `Nuovo progetto…` ثم `Applicazione` ثم `OK`.
2. [B] `Progetto` ثم `Salva progetto con nome…`: مجلد `cassiere` في `Documenti` واسم الملف `cassiere` ثم `Salva` مرتين.
3. [C] لوحة `Standard`: ثلاث مرات `TEdit` (اضغط المكوّن ثم النافذة) واحدة تحت الأخرى.
4. [C] `TButton` تحت الخانات ثم `TLabel` بجانب الزر.
5. [C] `TMemo` كبيرة في أسفل النافذة.
6. [D] اضغط `Button1` واكتب `Caption`: `Calcola il resto`.
7. [D] أفرغ `Text` في `Edit1` و`Edit2` و`Edit3`.
8. [D] اضغط `Memo1`: في Ispettore، يمين `Lines`، اضغط النقاط الثلاث، احذف النص ثم `OK`.
9. [E] انقر مرتين على الزر. لتنتصر بسرعة اكتب الباقي فقط (المبلغ المدفوع ناقص السعر):

```
procedure TForm1.Button1Click(Sender: TObject);
var
  prezzo, dati, resto: Integer;
begin
  prezzo := StrToIntDef(Edit2.Text, 0);
  dati := StrToIntDef(Edit3.Text, 0);
  resto := dati - prezzo;
  Label1.Caption := 'Resto: ' + IntToStr(resto) + ' euro';
end;
```

10. [F] اضغط `F9` واكتب السعر `13` والمبلغ المدفوع `50` ثم اضغط الزر.

> **انتصار سريع (5 دقائق):** يجب أن يظهر **Resto: 37 euro**.

11. أوقف البرنامج (`X` الحمراء). احذف كل الكود بين `begin` و`end;` واستعمل الكود الكامل أدناه: يضيف الأوراق والعملات والإيصال.

```
procedure TForm1.Button1Click(Sender: TObject);
var
  prezzo, dati, resto, b10, b5, m2, m1: Integer;
begin
  prezzo := StrToIntDef(Edit2.Text, 0);
  dati := StrToIntDef(Edit3.Text, 0);
  resto := dati - prezzo;
  b10 := resto div 10;
  resto := resto mod 10;
  b5 := resto div 5;
  resto := resto mod 5;
  m2 := resto div 2;
  m1 := resto mod 2;
  Memo1.Clear;
  Memo1.Lines.Add('SCONTRINO');
  Memo1.Lines.Add('Cliente: ' + Edit1.Text);
  Memo1.Lines.Add('Prezzo: ' + IntToStr(prezzo) + ' euro');
  Memo1.Lines.Add('Dati: ' + IntToStr(dati) + ' euro');
  Memo1.Lines.Add('Resto: ' + IntToStr(dati - prezzo) + ' euro');
  Memo1.Lines.Add(IntToStr(b10) + ' banconote da 10, ' + IntToStr(b5) + ' da 5');
  Memo1.Lines.Add(IntToStr(m2) + ' monete da 2, ' + IntToStr(m1) + ' da 1');
end;
```

12. [F] اضغط `F9` واكتب `Maria` و`13` و`50` ثم اضغط الزر.

> **النتيجة المتوقعة:** يظهر الإيصال في Memo: `SCONTRINO` و`Cliente: Maria` و`Prezzo: 13 euro` و`Dati: 50 euro` و`Resto: 37 euro` و`3 banconote da 10, 1 da 5` و`1 monete da 2, 0 da 1`.

### ماذا تفعل التعليمات الجديدة

الباقي `37`: `37 div 10` = `3` أوراق من 10 و`37 mod 10` = `7` يتبقى. `7 div 5` = `1` ورقة من 5 ويتبقى `2`. `2 div 2` = `1` عملة من 2 ويتبقى `0`. `'Cliente: ' + Edit1.Text` يلصق نصين. `Memo1.Lines.Add(...)` يضيف سطراً إلى الإيصال و`Memo1.Clear` يفرغه قبل الكتابة.

### الأخطاء الثلاثة الأكثر شيوعاً

| ماذا ترى | ماذا يعني | الحل |
|---|---|---|
| `Identifier not found "Memo1"` | `TMemo` مفقودة أو اسمها مختلف. | ضع `TMemo` على النافذة وتأكد أن `Name` هو `Memo1`. وكذلك `Edit1` و`Edit2` و`Edit3`. |
| `Incompatible types` | نص مقابل رقم: كتبت `Memo1.Lines.Add(resto)` دون تحويل. | اكتب `IntToStr(resto)` داخل `Add(...)`. |
| الباقي أو الأوراق غريبة (أرقام سالبة أو `0`) | المبلغ المدفوع أقل من السعر أو كتبت السنتات بفاصلة (`13,50` تُحسب `0`). | اكتب يورو صحيحة (`13`). يجب أن يكون المبلغ المدفوع على الأقل مساوياً للسعر. |

> **اجعله لك:** أعط اسماً لمتجرك واكتبه أعلى الإيصال: بعد `Memo1.Clear;` أضف `Memo1.Lines.Add('NEGOZIO DI ...');` بالاسم الذي تريده.

## 06 ملخص البرامج الثلاثة

| البرنامج | المكونات | الجديد | التجربة | النتيجة |
|---|---|---|---|---|
| 1. المحوّل | `Edit1`, `Label1`, 5 `Button` | `StrToInt`, `IntToStr`, `div`, `mod` | `5` | `5000 metri` |
| 2. الحاسبة | `Edit1`, `Edit2`, 4 `Button`, `Label1` | `StrToIntDef`, `if … else` | `7` e `5` / `8` e `0` | `7 più 5 fa 12` / `Non si può dividere per zero` |
| 3. أمين الصندوق | `Edit1`, `Edit2`, `Edit3`, `Label1`, `Button1`, `Memo1` | `div`, `mod`, `+` sui testi, `Memo1.Lines.Add` | `Maria`, `13`, `50` | `Resto: 37 euro` |

### انسخ في الدفتر

```
String = testo  '53'
Integer = numero  53
StrToInt = da testo a numero
IntToStr = da numero a testo
StrToIntDef(testo, 0) = se non va, usa 0
div = divisione senza virgola   17 div 5 = 3
mod = quello che avanza    17 mod 5 = 2
resto = dati - prezzo
```

ثم احكِ لزميل بكلماتك ماذا يفعل برنامجك المفضل.

لقد صنعت ثلاثة برامج حقيقية. أرِها لزميل: اسمك على عملك.
