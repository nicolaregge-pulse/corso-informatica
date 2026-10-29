# Ora 1: String e Integer, poi il cartello APERTO / CHIUSO

**Versione 1.0** — 29/10/2026 — ANTEPRIMA per il prof, non pubblicata

*1INF · Laboratorio · venerdì 30/10/2026, 11:00-12:00 · progetto `cartello` · si consegnano SEMPRE unit1.pas e lo screenshot*

الساعة 1: String و Integer، ثم لافتة APERTO / CHIUSO

第 1 节：String 和 Integer，然后做 APERTO / CHIUSO 牌子

## 01 Che cosa fai in quest'ora

Prima mezz'ora: la teoria in 6 schede, con una domanda dopo ogni scheda, e il quiz. Poi il programma: un cartello per il tuo negozio inventato. Premi <b>Apri</b> e compare APERTO in verde, premi <b>Chiudi</b> e compare CHIUSO in rosso.

النصف ساعة الأولى: النظرية في 6 بطاقات، مع سؤال بعد كل بطاقة، ثم الاختبار. بعدها البرنامج: لافتة لمتجرك المتخيَّل. تضغط Apri فيظهر APERTO بالأخضر، وتضغط Chiudi فيظهر CHIUSO بالأحمر.

前半小时：6 张理论卡片，每张后面一个问题，然后做测验。之后写程序：给你想象的商店做一个牌子。按 Apri 出现绿色的 APERTO，按 Chiudi 出现红色的 CHIUSO。

## 02 Fase 1: teoria e quiz

1. Teoria in 6 schede con le domande di ripasso: pagina `docs/verifica/?b=1inf-lab3010-tipi`.
2. Quiz di 22 domande su String e Integer: su Moduli Google (piano A) oppure nella stessa pagina, modo verifica (piano B).

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

## 03 Percorso facilitato (3 passi)

1. Leggi le schede 2 e 3 (String e Integer) e rispondi alle loro domande.

    اقرأ البطاقتين 2 و3 (String و Integer) وأجب عن أسئلتهما.

    读第 2、3 张卡片（String 和 Integer），回答它们的问题。

2. Nella Form1 metti una Label (la A) e un bottone (OK). Doppio clic sul bottone e scrivi la riga.

    في Form1 ضع Label (الحرف A) وزراً (OK). انقر مرتين على الزر واكتب السطر.

    在 Form1 放一个 Label（A）和一个按钮（OK）。双击按钮，写这一行。

    ```
      Label1.Caption := 'APERTO';
    ```

3. Premi F9 e clicca il bottone: compare APERTO. Fai lo screenshot e consegnalo.

    اضغط F9 وانقر الزر: يظهر APERTO. خذ لقطة شاشة وسلّمها.

    按 F9，点按钮：出现 APERTO。截图并提交。

## 04 L'esercitazione, passo per passo

1. **Progetto nuovo.** In alto clicca il menu <b>Progetto</b> → <b>Nuovo progetto…</b> → a sinistra <b>Applicazione</b> → <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.

    في الأعلى انقر القائمة Progetto ← Nuovo progetto… ← على اليسار Applicazione ← OK. في الوسط تظهر النافذة الفارغة Form1.

    点上方菜单 Progetto → Nuovo progetto… → 左边 Applicazione → OK。中间出现空窗口 Form1。

2. **Salva subito, nella cartella nuova.** Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Nella finestra clicca a sinistra <b>Documenti</b>, poi in alto <b>Nuova cartella</b>. Scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella per entrarci.

    القائمة Progetto ← Salva progetto con nome…. في النافذة انقر يساراً Documenti ثم في الأعلى Nuova cartella. اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد للدخول.

    菜单 Progetto → Salva progetto con nome…。在窗口左边点 Documenti，再点上方 Nuova cartella。写下面的名字，按回车，双击文件夹进去。

    ```
    cartello
    ```

3. **Il nome del progetto.** In basso, nella casella <b>Nome file</b>, scrivi il nome qui sotto e clicca <b>Salva</b>. Lazarus chiede il nome della unit: lascia <code>unit1.pas</code> e clicca <b>Salva</b>. In alto, nel titolo di Lazarus, c'è scritto <b>cartello</b>: FATTO!

    في الأسفل، في خانة Nome file، اكتب الاسم أدناه وانقر Salva. يسأل Lazarus عن اسم الـ unit: اترك unit1.pas وانقر Salva. في عنوان Lazarus مكتوب cartello: تم!

    在下面 Nome file 框里写下面的名字，点 Salva。Lazarus 问 unit 的名字：保留 unit1.pas，点 Salva。Lazarus 标题里写着 cartello：完成！

    ```
    cartello.lpi
    ```

4. **Il cartello: la Label.** Nella palette <b>Standard</b> clicca la <b>A</b> (è la <b>TLabel</b>, la scritta) e poi clicca nella Form1, in alto. Compare <b>Label1</b>.

    في لوحة Standard انقر A (هي TLabel، الكتابة) ثم انقر في Form1 في الأعلى. يظهر Label1.

    在 Standard 组件面板点 A（就是 TLabel，文字），再点 Form1 上方。出现 Label1。

5. **Fallo tuo: il nome del negozio.** Con Label1 selezionata, a sinistra nell'<b>Ispettore oggetti</b> trova <b>Caption</b> e scrivi il nome del tuo negozio inventato (per esempio <i>Pizzeria da Ahmed</i>). La scritta cambia SUBITO nella Form1: prima vittoria!

    مع تحديد Label1، يساراً في Ispettore oggetti ابحث عن Caption واكتب اسم متجرك المتخيَّل (مثلاً Pizzeria da Ahmed). الكتابة تتغير فوراً في Form1: أول فوز!

    选中 Label1，在左边 Ispettore oggetti 找到 Caption，写你想象的商店名字（比如 Pizzeria da Ahmed）。Form1 里的文字马上变了：第一个胜利！

6. **Scritta grande.** Sempre nell'Ispettore oggetti, clicca il piccolo segno a sinistra di <b>Font</b>: si apre l'elenco. Trova <b>Size</b> e scrivi <b>28</b>, poi premi Invio.

    في Ispettore oggetti انقر العلامة الصغيرة على يسار Font: تفتح القائمة. ابحث عن Size واكتب 28 ثم اضغط Invio.

    还是在 Ispettore oggetti，点 Font 左边的小符号：展开列表。找到 Size，写 28，按回车。

    ```
    28
    ```

7. **Due bottoni.** Nella palette clicca il bottone <b>OK</b> (è il <b>TButton</b>) e clicca nella Form1 sotto la scritta: compare <b>Button1</b>. Nell'Ispettore oggetti cambia <b>Caption</b> in <b>Apri</b>. Rifai: secondo bottone <b>Button2</b> con Caption <b>Chiudi</b>.

    في اللوحة انقر الزر OK (هو TButton) وانقر في Form1 تحت الكتابة: يظهر Button1. في Ispettore oggetti غيّر Caption إلى Apri. كرّر: زر ثانٍ Button2 بـ Caption هو Chiudi.

    在组件面板点 OK 按钮（就是 TButton），再点 Form1 文字下面：出现 Button1。在 Ispettore oggetti 把 Caption 改成 Apri。再做一次：第二个按钮 Button2，Caption 写 Chiudi。

8. **Il codice di Apri.** Fai <b>doppio clic</b> sul bottone <b>Apri</b>: si apre il codice con <code>procedure TForm1.Button1Click</code>. Tra <code>begin</code> e <code>end;</code> scrivi le due righe. <code>'APERTO'</code> è una <b>String</b>: va tra apici.

    انقر مرتين على الزر Apri: يفتح الكود مع procedure TForm1.Button1Click. بين begin و end; اكتب السطرين. 'APERTO' هي String: توضع بين علامتي اقتباس.

    双击 Apri 按钮：打开代码，有 procedure TForm1.Button1Click。在 begin 和 end; 之间写这两行。'APERTO' 是 String：要放在单引号里。

    ```
      Label1.Caption := 'APERTO';
      Label1.Font.Color := clGreen;
    ```

9. **Il codice di Chiudi.** Premi <b>F12</b>: torni alla Form1. Fai doppio clic sul bottone <b>Chiudi</b> (si apre <code>Button2Click</code>) e scrivi:

    اضغط F12: تعود إلى Form1. انقر مرتين على الزر Chiudi (يفتح Button2Click) واكتب:

    按 F12：回到 Form1。双击 Chiudi 按钮（打开 Button2Click），写：

    ```
      Label1.Caption := 'CHIUSO';
      Label1.Font.Color := clRed;
    ```

10. **Fai partire: F9.** Premi <b>F9</b>. Si apre il TUO programma. Clicca <b>Apri</b>: APERTO in verde. Clicca <b>Chiudi</b>: CHIUSO in rosso. FATTO! Fallo vedere al compagno.

    اضغط F9. يفتح برنامجك. انقر Apri: APERTO بالأخضر. انقر Chiudi: CHIUSO بالأحمر. تم! أرِه لزميلك.

    按 F9。打开你的程序。点 Apri：绿色的 APERTO。点 Chiudi：红色的 CHIUSO。完成！给同桌看看。

11. **L'errore che insegna (succede a tutti).** Chiudi il tuo programma. Nella riga di Apri cambia <code>'APERTO'</code> in <code>7</code> (senza apici) e premi F9. In basso, in <b>Messaggi</b>, compare l'errore <b>Incompatible types</b>: la Caption vuole una <b>String</b>, 7 è un <b>Integer</b>. Correggi così e premi F9: compare 7. Poi rimetti <code>'APERTO'</code>.

    أغلق برنامجك. في سطر Apri غيّر 'APERTO' إلى 7 (بلا علامات اقتباس) واضغط F9. في الأسفل في Messaggi يظهر الخطأ Incompatible types: الـ Caption تريد String، و7 هو Integer. صحّح هكذا واضغط F9: يظهر 7. ثم أرجع 'APERTO'.

    关掉你的程序。在 Apri 那行把 'APERTO' 改成 7（不加引号），按 F9。下面 Messaggi 里出现错误 Incompatible types：Caption 要的是 String，7 是 Integer。照下面改正，按 F9：出现 7。然后改回 'APERTO'。

    ```
      Label1.Caption := IntToStr(7);
    ```

12. **Fallo tuo: i tuoi colori.** Cambia <code>clGreen</code> e <code>clRed</code> con i colori che vuoi: <code>clBlue</code>, <code>clPurple</code>, <code>clFuchsia</code>, <code>clNavy</code>, <code>clOlive</code>, <code>clTeal</code>. Poi clicca un punto vuoto della Form1 e nell'Ispettore oggetti cambia <b>Color</b> (lo sfondo). Chi ha finito: terzo bottone <b>Pausa</b> che scrive <i>TORNO SUBITO</i>.

    غيّر clGreen و clRed بالألوان التي تريدها: clBlue، clPurple، clFuchsia، clNavy، clOlive، clTeal. ثم انقر مكاناً فارغاً في Form1 وفي Ispettore oggetti غيّر Color (الخلفية). من أنهى: زر ثالث Pausa يكتب TORNO SUBITO.

    把 clGreen 和 clRed 换成你喜欢的颜色：clBlue、clPurple、clFuchsia、clNavy、clOlive、clTeal。再点 Form1 的空白处，在 Ispettore oggetti 改 Color（背景）。做完的同学：第三个按钮 Pausa，写出 TORNO SUBITO。

## 05 Tre aiuti

1. Indizio: Ogni riga va tra <code>begin</code> e <code>end;</code> e finisce con <code>;</code>. La scritta va tra apici: <code>'APERTO'</code>. Il colore comincia con <code>cl</code>.
2. Il pezzo di codice:

    ```
    procedure TForm1.Button1Click(Sender: TObject);
    begin
      Label1.Caption := 'APERTO';
      Label1.Font.Color := clGreen;
    end;
    ```

3. Tutto unit1.pas: `codice/ora1_unit1.pas`.

## 06 Spiegalo in 30 secondi

Al compagno: perché <code>'APERTO'</code> ha gli apici e <code>7</code> no? Che cosa vuole la Caption?

لزميلك: لماذا 'APERTO' لها علامات اقتباس و7 لا؟ ماذا تريد الـ Caption؟

对同桌说：为什么 'APERTO' 有引号而 7 没有？Caption 要的是什么？

## 07 Consegna: unit1.pas + screenshot

1. Piano A: pagina `consegna.html?ora=1`: scegli unit1.pas e lo screenshot, il controllo automatico dice subito se il codice va bene, un bottone manda tutto.
2. Piano B, se il bottone non funziona: Classroom, passi C1-C5.

    1. **C1 Lo screenshot del programma che gira.** Premi <b>F9</b>: il tuo programma è aperto. Premi insieme <b>Win + Shift + S</b> e con il mouse disegna un rettangolo intorno alla tua finestra. In basso a destra clicca l'avviso <b>Ritaglio</b>: si apre lo Strumento di cattura. Premi <b>Ctrl + S</b>, a sinistra clicca <b>Documenti</b>, doppio clic sulla cartella <b>cartello</b>, in <b>Nome file</b> scrivi il nome qui sotto e clicca <b>Salva</b>.

        ```
        ora1_screenshot.png
        ```

    2. **C2 Trova unit1.pas.** Premi <b>Win + E</b> (Esplora file). A sinistra clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>cartello</b>. In alto clicca <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>: ora vedi le lettere dopo il punto. Il file del tuo codice è <code>unit1.pas</code>.

    3. **C3 Fai la copia da consegnare.** Clicca una volta <code>unit1.pas</code>. Premi <b>Ctrl + C</b> e poi <b>Ctrl + V</b>: compare <code>unit1 - Copia.pas</code>. Cliccala una volta, premi <b>F2</b>, scrivi il nome qui sotto e premi Invio. (L'originale <code>unit1.pas</code> resta lì: il progetto funziona ancora.)

        ```
        ora1_unit1.pas
        ```

    4. **C4 Su Classroom: aggiungi i due file.** Apri il compito <b>Ora 1 · Il cartello</b> su Classroom. A destra, nel riquadro <b>Il tuo lavoro</b>, clicca <b>+ Aggiungi o crea</b> → <b>File</b> → <b>Sfoglia</b>. Vai in <b>Documenti</b> → <b>cartello</b>, scegli <code>ora1_unit1.pas</code> e clicca <b>Apri</b>. Rifai lo stesso per <code>ora1_screenshot.png</code>.

    5. **C5 Consegna.** Nel riquadro <b>Il tuo lavoro</b> vedi i due file: <code>ora1_unit1.pas</code> e <code>ora1_screenshot.png</code>. Clicca <b>Consegna</b> e poi ancora <b>Consegna</b>. FATTO!

## 08 Controllo finale

1. So dire che cos'è una String e che cos'è un Integer, con un esempio.
2. So perché '5' + '3' fa '53' e 5 + 3 fa 8.
3. Il mio cartello cambia scritta e colore quando premo i bottoni.
4. Ho consegnato ora1_unit1.pas e ora1_screenshot.png.

## 09 Da ricopiare sul quaderno

```
VARIABILE = una scatola con un nome dentro c'e' un valore
STRING  = testo, sempre tra apici:   'Ciao'   '5'
INTEGER = numero intero, senza apici:  5   12   -3
'5' + '3' = '53'  (attacca)      5 + 3 = 8  (somma)
Edit1.Text e Label1.Caption sono STRING
StrToInt: da String a Integer    '7' -> 7
IntToStr: da Integer a String     7 -> '7'
```
