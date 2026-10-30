# Ora 1: String e Integer, il pasticcio dei numeri

**Versione 1.1** — 29/10/2026 — pubblicata il 30/10/2026; aggiornata alle 12:40 (passo «Salva» nel percorso facilitato)

*1INF · Laboratorio · venerdì 30/10/2026, 11:00-12:00 · progetto `pasticcio` · si consegnano SEMPRE unit1.pas e lo screenshot*

الساعة 1: String و Integer، لخبطة الأرقام

第 1 节：String 和 Integer，数字的混乱

## 01 Che cosa fai in quest'ora

Tutta l'ora parla di <b>String</b> e <b>Integer</b>. La teoria e il quiz li hai fatti stamattina. Adesso un programma piccolo che mostra la differenza: il bottone <b>Testo</b> fa <code>'5' + '3'</code> e compare <b>53</b>; il bottone <b>Numeri</b> fa 5 + 3 con due Integer e compare <b>8</b>.

الساعة كلها عن String و Integer. النظرية والاختبار تمّا هذا الصباح. الآن برنامج صغير يُظهر الفرق: الزر Testo يفعل '5' + '3' فيظهر 53؛ والزر Numeri يفعل 5 + 3 بعددين Integer فيظهر 8.

这一节课都讲 String 和 Integer。理论和测验今天早上已经做完。现在写一个小程序来看区别：Testo 按钮做 '5' + '3'，出现 53；Numeri 按钮用两个 Integer 做 5 + 3，出现 8。

## 02 Teoria e quiz già fatti stamattina → vai alla Fase 2

النظرية والاختبار تمّا هذا الصباح ← انتقل إلى المرحلة 2

理论和测验今天早上已经做完 → 去第 2 阶段

1. Chi stamattina non li ha fatti: torna alla pagina del laboratorio (`docs/anteprima/1inf-lab-30-10/`) e fai il passo 3.
2. Le 6 schede qui sotto restano per ripassare: pagina `docs/verifica/?b=1inf-lab3010-tipi`.

### 02.1 1. La variabile: una scatola con un nome

Una <b>variabile</b> è una <b>scatola</b> con un'etichetta. Sull'etichetta c'è il nome (per esempio <code>nome</code> o <code>eta</code>), dentro c'è un valore. Il segno <code>:=</code> vuol dire «metti dentro».

المتغير صندوق عليه ملصق. على الملصق الاسم (مثلاً nome أو eta)، وفي الداخل قيمة. العلامة := تعني «ضع داخل».

变量是一个贴了标签的盒子。标签上是名字（比如 nome 或 eta），里面是一个值。:= 的意思是“放进去”。

Ogni scatola ha un <b>tipo</b>: dice che cosa ci può stare dentro. Oggi ne impariamo due: <b>String</b> (testo) e <b>Integer</b> (numero intero).

لكل صندوق نوع: يقول ماذا يمكن أن يوضع فيه. اليوم نتعلم نوعين: String (نص) و Integer (عدد صحيح).

每个盒子都有一个类型：说明里面能装什么。今天学两种：String（文字）和 Integer（整数）。

```
var
  nome: String;     { scatola per il testo }
  eta: Integer;     { scatola per un numero intero }
begin
  nome := 'Ahmed';
  eta := 12;
```

### 02.2 2. String: il testo tra apici

Una <b>String</b> è un <b>testo</b>: lettere, spazi, simboli e anche cifre. In Pascal si scrive sempre tra <b>apici</b> (la virgoletta alta): <code>'Ciao'</code>, <code>'Milano'</code>, <code>'007'</code>.

String هي نص: حروف ومسافات ورموز وحتى أرقام. في Pascal تُكتب دائماً بين علامتي اقتباس مفردتين: 'Ciao'، 'Milano'، '007'.

String 是文字：字母、空格、符号，也可以是数字。在 Pascal 里总是写在单引号里：'Ciao'、'Milano'、'007'。

Attenzione: <code>'007'</code> ha gli apici, quindi è una String, anche se dentro ci sono cifre. Il <code>+</code> tra due String le <b>attacca</b>: <code>'Ciao ' + 'Ahmed'</code> fa <code>'Ciao Ahmed'</code>.

انتبه: '007' لها علامتا اقتباس، إذن هي String حتى لو كان فيها أرقام. علامة + بين نصّين تلصقهما: 'Ciao ' + 'Ahmed' تعطي 'Ciao Ahmed'.

注意：'007' 有引号，所以它是 String，即使里面是数字。两个 String 之间的 + 是把它们连起来：'Ciao ' + 'Ahmed' 得到 'Ciao Ahmed'。

```
'Ciao'      String
'007'       String (ha gli apici!)
'Ciao ' + 'Ahmed'  ->  'Ciao Ahmed'
```

### 02.3 3. Integer: il numero intero

Un <b>Integer</b> è un <b>numero intero</b>: senza virgola, senza apici. Può essere anche negativo: <code>0</code>, <code>7</code>, <code>2026</code>, <code>-5</code>.

Integer هو عدد صحيح: بلا فاصلة وبلا علامات اقتباس. يمكن أن يكون سالباً: 0، 7، 2026، -5.

Integer 是整数：没有小数点，没有引号。也可以是负数：0、7、2026、-5。

Con gli Integer si fanno i <b>conti</b>: <code>+</code> <code>-</code> <code>*</code>. <code>3.5</code> NON è un Integer: ha la virgola (in Pascal si scrive con il punto).

بالأعداد الصحيحة نحسب: + - *. العدد 3.5 ليس Integer: فيه فاصلة (في Pascal تُكتب بنقطة).

整数可以计算：+ - *。3.5 不是 Integer：它有小数点（Pascal 里用点来写）。

```
12          Integer
-5          Integer
3.5         NON e' un Integer (ha la virgola)
12 + 3  ->  15
```

### 02.4 4. La trappola: '5' + '3' oppure 5 + 3?

Lo stesso segno <code>+</code> fa due cose diverse. Tra due <b>String</b> le attacca: <code>'5' + '3'</code> = <code>'53'</code>. Tra due <b>Integer</b> fa la somma: <code>5 + 3</code> = <code>8</code>.

نفس العلامة + تفعل شيئين مختلفين. بين نصّين تلصقهما: '5' + '3' = '53'. بين عددين تجمعهما: 5 + 3 = 8.

同一个 + 做两件不同的事。两个 String 之间是连起来：'5' + '3' = '53'。两个 Integer 之间是相加：5 + 3 = 8。

Per questo bisogna sempre guardare il <b>tipo</b>: gli apici ti dicono che è testo.

لهذا يجب دائماً النظر إلى النوع: علامات الاقتباس تقول لك إنه نص.

所以一定要看类型：引号告诉你它是文字。

```
'5' + '3'   ->  '53'   (String: attacca)
 5  +  3   ->   8     (Integer: somma)
```

### 02.5 5. In Lazarus le caselle hanno String

<code>Edit1.Text</code> (quello che l'utente scrive nella casella) è una <b>String</b>. Anche se scrivi 15, dentro c'è <code>'15'</code>, il testo. Anche <code>Label1.Caption</code> e <code>Button1.Caption</code> sono String.

Edit1.Text (ما يكتبه المستخدم في الخانة) هو String. حتى لو كتبت 15، في الداخل '15'، النص. و Label1.Caption و Button1.Caption أيضاً String.

Edit1.Text（用户在输入框里写的）是 String。即使你写 15，里面也是 '15'，是文字。Label1.Caption 和 Button1.Caption 也是 String。

Per questo <code>Label1.Caption := 7;</code> dà errore quando premi F9: la Caption vuole una String e 7 è un Integer.

لهذا Label1.Caption := 7; يعطي خطأ عندما تضغط F9: الـ Caption تريد String و7 هو Integer.

所以按 F9 时 Label1.Caption := 7; 会出错：Caption 要的是 String，7 是 Integer。

```
Edit1.Text       String  (scrivo 15 -> '15')
Label1.Caption   String
Label1.Caption := 7;     ERRORE: Incompatible types
Label1.Caption := '7';   giusto
```

### 02.6 6. I due traduttori: StrToInt e IntToStr

<code>StrToInt</code> si legge «da String a Integer»: <code>StrToInt('7')</code> dà il numero 7. <code>IntToStr</code> si legge «da Integer a String»: <code>IntToStr(7)</code> dà il testo <code>'7'</code>.

StrToInt تُقرأ «من String إلى Integer»: StrToInt('7') يعطي الرقم 7. و IntToStr تُقرأ «من Integer إلى String»: IntToStr(7) يعطي النص '7'.

StrToInt 读作“从 String 到 Integer”：StrToInt('7') 得到数字 7。IntToStr 读作“从 Integer 到 String”：IntToStr(7) 得到文字 '7'。

Il viaggio di un numero: casella → <code>StrToInt</code> → conto → <code>IntToStr</code> → Caption. Se la casella contiene <i>ciao</i>, <code>StrToInt</code> non sa tradurre: il programma si ferma con un errore.

رحلة الرقم: الخانة ← StrToInt ← الحساب ← IntToStr ← Caption. إذا كانت الخانة فيها ciao، لا يعرف StrToInt الترجمة: يتوقف البرنامج بخطأ.

一个数字的旅程：输入框 → StrToInt → 计算 → IntToStr → Caption。如果输入框里是 ciao，StrToInt 翻译不了：程序会报错停下。

```
Edit1.Text   '7'  --StrToInt-->  7  --(+1)-->  8  --IntToStr-->  '8'   Label1.Caption
```

## 03 Percorso facilitato (4 passi)

> **AIUTO LAZARUS: se sei in difficoltà a creare il progetto Lazarus, alza la mano e chiedi aiuto al Professore: viene lui al tuo posto.**
>
> إذا وجدت صعوبة في إنشاء مشروع Lazarus، ارفع يدك واطلب المساعدة من الأستاذ: سيأتي هو إلى مكانك.
>
> 如果你创建 Lazarus 项目有困难，请举手请老师帮忙：老师会到你的座位来。
>
> Per le altre domande usa la casella dell'assistente.

1. Leggi le schede 2 e 3 (String e Integer) e rispondi alle loro domande.

    اقرأ البطاقتين 2 و3 (String و Integer) وأجب عن أسئلتهما.

    读第 2、3 张卡片（String 和 Integer），回答它们的问题。

2. **Salva subito, nella cartella nuova.** Prima il progetto nuovo: menu Progetto → Nuovo progetto… → Applicazione → OK. Menu Progetto → Salva progetto con nome…. A sinistra clicca Documenti, in alto Nuova cartella, scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella. In Nome file scrivi lo stesso nome e clicca Salva; per unit1.pas clicca ancora Salva.

    أولاً مشروع جديد: القائمة Progetto ← Nuovo progetto… ← Applicazione ← OK. القائمة Progetto ← Salva progetto con nome…. انقر يساراً Documenti، ثم في الأعلى Nuova cartella، اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد. في Nome file اكتب نفس الاسم وانقر Salva؛ ولـ unit1.pas انقر Salva مرة أخرى.

    先建新项目：菜单 Progetto → Nuovo progetto… → Applicazione → OK。菜单 Progetto → Salva progetto con nome…。左边点 Documenti，上方点 Nuova cartella，写下面的名字，按回车，双击文件夹进去。在 Nome file 里写同样的名字，点 Salva；unit1.pas 再点一次 Salva。

    ```
    pasticcio
    ```

3. Nella Form1 metti una Label (la A) e un bottone (OK). Doppio clic sul bottone e scrivi la riga.

    في Form1 ضع Label (الحرف A) وزراً (OK). انقر مرتين على الزر واكتب السطر.

    在 Form1 放一个 Label（A）和一个按钮（OK）。双击按钮，写这一行。

    ```
      Label1.Caption := '5' + '3';
    ```

4. Premi F9 e clicca il bottone: compare 53. Fai lo screenshot e consegnalo.

    اضغط F9 وانقر الزر: يظهر 53. خذ لقطة شاشة وسلّمها.

    按 F9，点按钮：出现 53。截图并提交。

## 04 L'esercitazione, passo per passo

> **AIUTO LAZARUS: se sei in difficoltà a creare il progetto Lazarus, alza la mano e chiedi aiuto al Professore: viene lui al tuo posto.**
>
> إذا وجدت صعوبة في إنشاء مشروع Lazarus، ارفع يدك واطلب المساعدة من الأستاذ: سيأتي هو إلى مكانك.
>
> 如果你创建 Lazarus 项目有困难，请举手请老师帮忙：老师会到你的座位来。
>
> Per le altre domande usa la casella dell'assistente.

1. **Progetto nuovo.** In alto clicca il menu <b>Progetto</b> → <b>Nuovo progetto…</b> → a sinistra <b>Applicazione</b> → <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.

    في الأعلى انقر القائمة Progetto ← Nuovo progetto… ← على اليسار Applicazione ← OK. في الوسط تظهر النافذة الفارغة Form1.

    点上方菜单 Progetto → Nuovo progetto… → 左边 Applicazione → OK。中间出现空窗口 Form1。

2. **Salva subito, nella cartella nuova.** Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Nella finestra clicca a sinistra <b>Documenti</b>, poi in alto <b>Nuova cartella</b>. Scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella per entrarci.

    القائمة Progetto ← Salva progetto con nome…. في النافذة انقر يساراً Documenti ثم في الأعلى Nuova cartella. اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد للدخول.

    菜单 Progetto → Salva progetto con nome…。在窗口左边点 Documenti，再点上方 Nuova cartella。写下面的名字，按回车，双击文件夹进去。

    ```
    pasticcio
    ```

3. **Il nome del progetto.** In basso, nella casella <b>Nome file</b>, scrivi il nome qui sotto e clicca <b>Salva</b>. Lazarus chiede il nome della unit: lascia <code>unit1.pas</code> e clicca <b>Salva</b>. In alto, nel titolo di Lazarus, c'è scritto <b>pasticcio</b>: FATTO!

    في الأسفل، في خانة Nome file، اكتب الاسم أدناه وانقر Salva. يسأل Lazarus عن اسم الـ unit: اترك unit1.pas وانقر Salva. في عنوان Lazarus مكتوب pasticcio: تم!

    在下面 Nome file 框里写下面的名字，点 Salva。Lazarus 问 unit 的名字：保留 unit1.pas，点 Salva。Lazarus 标题里写着 pasticcio：完成！

    ```
    pasticcio.lpi
    ```

4. **La scritta del risultato.** Nella palette <b>Standard</b> clicca la <b>A</b> (è la <b>TLabel</b>) e poi clicca nella Form1, in alto: compare <b>Label1</b>. Nell'Ispettore oggetti cambia <b>Caption</b> in <b>?</b> e, nel piccolo segno a sinistra di <b>Font</b> → <b>Size</b>, scrivi 36.

    في لوحة Standard انقر A (هي TLabel) ثم انقر في Form1 في الأعلى: يظهر Label1. في Ispettore oggetti غيّر Caption إلى ? وفي العلامة الصغيرة يسار Font ← Size اكتب 36.

    在 Standard 组件面板点 A（就是 TLabel），再点 Form1 上方：出现 Label1。在 Ispettore oggetti 把 Caption 改成 ?，点 Font 左边的小符号 → Size，写 36。

    ```
    36
    ```

5. **Due bottoni.** Nella palette clicca il bottone <b>OK</b> (è il <b>TButton</b>) e clicca nella Form1 sotto la scritta: compare <b>Button1</b>, cambia <b>Caption</b> in <b>Testo</b>. Rifai: secondo bottone <b>Button2</b> con Caption <b>Numeri</b>.

    في اللوحة انقر الزر OK (هو TButton) وانقر في Form1 تحت الكتابة: يظهر Button1، غيّر Caption إلى Testo. كرّر: زر ثانٍ Button2 بـ Caption هو Numeri.

    在组件面板点 OK 按钮（就是 TButton），再点 Form1 文字下面：出现 Button1，把 Caption 改成 Testo。再做一次：第二个按钮 Button2，Caption 写 Numeri。

6. **Il bottone Testo: due String.** Fai <b>doppio clic</b> sul bottone <b>Testo</b>: si apre <code>procedure TForm1.Button1Click</code>. Tra <code>begin</code> e <code>end;</code> scrivi la riga. <code>'5'</code> e <code>'3'</code> hanno gli apici: sono due <b>String</b>.

    انقر مرتين على الزر Testo: يفتح procedure TForm1.Button1Click. بين begin و end; اكتب السطر. '5' و'3' لهما علامات اقتباس: هما نصّان String.

    双击 Testo 按钮：打开 procedure TForm1.Button1Click。在 begin 和 end; 之间写这一行。'5' 和 '3' 有引号：是两个 String。

    ```
      Label1.Caption := '5' + '3';
    ```

7. **Fai partire: F9.** Premi <b>F9</b>. Clicca <b>Testo</b>: compare <b>53</b>, non 8! Due String si ATTACCANO. FATTO: prima vittoria. Fallo vedere al compagno.

    اضغط F9. انقر Testo: يظهر 53 وليس 8! النصّان يُلصقان. تم: أول فوز. أرِه لزميلك.

    按 F9。点 Testo：出现 53，不是 8！两个 String 是连起来。完成：第一个胜利。给同桌看看。

8. **Il bottone Numeri: le scatole Integer.** Chiudi il programma e premi <b>F12</b>: torni alla Form1. Fai doppio clic su <b>Numeri</b>: si apre <code>Button2Click</code>. Clicca alla fine della riga <code>procedure</code>, premi Invio e scrivi PRIMA di <code>begin</code>: due scatole di tipo <b>Integer</b>.

    أغلق البرنامج واضغط F12: تعود إلى Form1. انقر مرتين على Numeri: يفتح Button2Click. انقر في نهاية سطر procedure، اضغط Invio واكتب قبل begin: صندوقان من نوع Integer.

    关掉程序，按 F12：回到 Form1。双击 Numeri：打开 Button2Click。点 procedure 那一行的末尾，按回车，在 begin 前面写：两个 Integer 类型的盒子。

    ```
    var
      a, b: Integer;
    ```

9. **L'errore che insegna (succede a tutti).** Tra <code>begin</code> e <code>end;</code> scrivi le tre righe e premi <b>F9</b>. In basso, in <b>Messaggi</b>, compare l'errore <b>Incompatible types</b>: la Caption vuole una <b>String</b> e <code>a + b</code> è un <b>Integer</b>. È normale: lo correggi nel passo dopo.

    بين begin و end; اكتب الأسطر الثلاثة واضغط F9. في الأسفل في Messaggi يظهر الخطأ Incompatible types: الـ Caption تريد String و a + b هو Integer. هذا طبيعي: تصحّحه في الخطوة التالية.

    在 begin 和 end; 之间写这三行，按 F9。下面 Messaggi 里出现错误 Incompatible types：Caption 要的是 String，a + b 是 Integer。这很正常：下一步就改好。

    ```
      a := 5;
      b := 3;
      Label1.Caption := a + b;
    ```

10. **Il traduttore IntToStr.** Cambia l'ultima riga così: <code>IntToStr</code> trasforma il numero 8 nel testo '8'. Premi <b>F9</b>. Clicca <b>Testo</b>: 53. Clicca <b>Numeri</b>: 8. FATTO! Lo stesso 5 e 3, due risultati diversi.

    غيّر السطر الأخير هكذا: IntToStr يحوّل الرقم 8 إلى النص '8'. اضغط F9. انقر Testo: 53. انقر Numeri: 8. تم! نفس 5 و3، ونتيجتان مختلفتان.

    把最后一行改成这样：IntToStr 把数字 8 变成文字 '8'。按 F9。点 Testo：53。点 Numeri：8。完成！同样的 5 和 3，两个不同的结果。

    ```
      Label1.Caption := IntToStr(a + b);
    ```

11. **Fallo tuo: i tuoi numeri.** Scegli due numeri tuoi (per esempio la tua età e il tuo numero di maglia): cambiali in tutti e due i bottoni, nel Testo tra apici e nei Numeri senza apici. Prima di F9 scrivi sul quaderno che cosa ti aspetti, poi controlla. Chi ha finito: <b>Button3</b> con Caption <b>Tutti e due</b> e questa riga:

    اختر رقمين خاصين بك (مثلاً عمرك ورقم قميصك): غيّرهما في الزرين، في Testo بين علامات اقتباس وفي Numeri بلا علامات. قبل F9 اكتب في الدفتر ما تتوقعه، ثم تحقّق. من أنهى: Button3 بـ Caption هو Tutti e due وهذا السطر:

    选两个你自己的数字（比如你的年龄和你的球衣号码）：在两个按钮里都改掉，Testo 里加引号，Numeri 里不加引号。按 F9 之前先在本子上写下你预计的结果，再检查。做完的同学：Button3，Caption 写 Tutti e due，写这一行：

    ```
      Label1.Caption := '5' + '3' + ' oppure ' + IntToStr(5 + 3);
    ```

## 05 Tre aiuti

1. Indizio: Testo: i numeri tra apici sono String e il + li attacca. Numeri: le righe <code>var</code> vanno prima di <code>begin</code>; la Caption vuole una String, quindi <code>IntToStr(a + b)</code>.
2. Il pezzo di codice:

    ```
    procedure TForm1.Button2Click(Sender: TObject);
    var
      a, b: Integer;
    begin
      a := 5;
      b := 3;
      Label1.Caption := IntToStr(a + b);
    end;
    ```

3. Tutto unit1.pas: `codice/ora1_unit1.pas`.

## 06 Spiegalo in 30 secondi

Al compagno: perché lo stesso 5 e 3 dà 53 con <b>Testo</b> e 8 con <b>Numeri</b>? A che cosa serve <code>IntToStr</code>?

لزميلك: لماذا نفس 5 و3 يعطيان 53 مع Testo و8 مع Numeri؟ لماذا نحتاج IntToStr؟

对同桌说：为什么同样的 5 和 3，按 Testo 是 53，按 Numeri 是 8？IntToStr 有什么用？

## 07 Consegna: unit1.pas + screenshot

1. Piano A: pagina `consegna.html?ora=1`: scegli unit1.pas e lo screenshot, il controllo automatico dice subito se il codice va bene, un bottone manda tutto.
2. Piano B, se il bottone non funziona: Classroom, passi C1-C5.

    1. **C1 Lo screenshot del programma che gira.** Premi <b>F9</b>: il tuo programma è aperto. Premi insieme <b>Win + Shift + S</b> e con il mouse disegna un rettangolo intorno alla tua finestra. In basso a destra clicca l'avviso <b>Ritaglio</b>: si apre lo Strumento di cattura. Premi <b>Ctrl + S</b>, a sinistra clicca <b>Documenti</b>, doppio clic sulla cartella <b>pasticcio</b>, in <b>Nome file</b> scrivi il nome qui sotto e clicca <b>Salva</b>.

        ```
        ora1_screenshot.png
        ```

    2. **C2 Trova unit1.pas.** Premi <b>Win + E</b> (Esplora file). A sinistra clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>pasticcio</b>. In alto clicca <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>: ora vedi le lettere dopo il punto. Il file del tuo codice è <code>unit1.pas</code>.

    3. **C3 Fai la copia da consegnare.** Clicca una volta <code>unit1.pas</code>. Premi <b>Ctrl + C</b> e poi <b>Ctrl + V</b>: compare <code>unit1 - Copia.pas</code>. Cliccala una volta, premi <b>F2</b>, scrivi il nome qui sotto e premi Invio. (L'originale <code>unit1.pas</code> resta lì: il progetto funziona ancora.)

        ```
        ora1_unit1.pas
        ```

    4. **C4 Su Classroom: aggiungi i due file.** Apri il compito <b>Laboratorio 11-14: stringhe e interi in Lazarus</b> su Classroom (è uno solo per le tre ore). Se vedi il bottone <b>Annulla consegna</b>, cliccalo prima: i file delle ore prima restano lì. A destra, nel riquadro <b>Il tuo lavoro</b>, clicca <b>+ Aggiungi o crea</b> → <b>File</b> → <b>Sfoglia</b>. Vai in <b>Documenti</b> → <b>pasticcio</b>, scegli <code>ora1_unit1.pas</code> e clicca <b>Apri</b>. Rifai lo stesso per <code>ora1_screenshot.png</code>.

    5. **C5 Consegna.** Nel riquadro <b>Il tuo lavoro</b> vedi i due file: <code>ora1_unit1.pas</code> e <code>ora1_screenshot.png</code>. Clicca <b>Consegna</b> e poi ancora <b>Consegna</b>. FATTO!

## 08 Controllo finale

1. So dire che cos'è una String e che cos'è un Integer, con un esempio.
2. Il mio programma mostra 53 con Testo e 8 con Numeri (o i risultati dei miei numeri).
3. So perché Label1.Caption := a + b; dà errore e come si corregge.
4. Ho consegnato ora1_unit1.pas e ora1_screenshot.png.

## 09 Da ricopiare sul quaderno

```
VARIABILE = una scatola con un nome dentro c'e' un valore
STRING  = testo, sempre tra apici:   'Ciao'   '5'
INTEGER = numero intero, senza apici:  5   12   -3
'5' + '3' = '53'  (attacca)      5 + 3 = 8  (somma)
Label1.Caption := a + b;            ERRORE: la Caption vuole una String
Label1.Caption := IntToStr(a + b);  giusto: 8
StrToInt: da String a Integer    '7' -> 7
IntToStr: da Integer a String     7 -> '7'
```
