# Ora 3: gli Integer, il segnapunti con StrToInt e IntToStr

**Versione 1.0** — 29/10/2026 — ANTEPRIMA per il prof, non pubblicata

*1INF · Laboratorio · venerdì 30/10/2026, 13:00-14:00 · progetto `segnapunti` · si consegnano SEMPRE unit1.pas e lo screenshot*

الساعة 3: Integer، عدّاد النقاط مع StrToInt و IntToStr

第 3 节：Integer，用 StrToInt 和 IntToStr 做记分牌

## 01 Che cosa fai in quest'ora

Un programma nuovo: il <b>segnapunti</b> di una partita. Un numero grande al centro: <b>+1</b> aggiunge un punto, <b>Aggiungi</b> aggiunge i punti che scrivi nella casella, <b>Azzera</b> torna a 0. Per fare i conti serve un <b>Integer</b>.

برنامج جديد: عدّاد نقاط مباراة. رقم كبير في الوسط: +1 يضيف نقطة، Aggiungi يضيف النقاط التي تكتبها في الخانة، Azzera يرجع إلى 0. للحساب نحتاج Integer.

一个新程序：比赛的记分牌。中间一个大数字：+1 加一分，Aggiungi 加上你在输入框里写的分数，Azzera 回到 0。要算数就需要 Integer。

## 02 Ripasso in 1 minuto

<b>Ripasso in 1 minuto.</b> Un <b>Integer</b> è un numero intero, senza apici: <code>12</code>. Con gli Integer si fanno i conti: <code>12 + 3</code> = <code>15</code>. Ma la Caption e la casella hanno solo <b>String</b>. Servono i due traduttori: <code>StrToInt('12')</code> dà il numero 12, <code>IntToStr(15)</code> dà il testo '15'.

مراجعة في دقيقة. Integer هو عدد صحيح بلا علامات اقتباس: 12. بالأعداد نحسب: 12 + 3 = 15. لكن الـ Caption والخانة فيهما String فقط. نحتاج المترجمَين: StrToInt('12') يعطي الرقم 12، و IntToStr(15) يعطي النص '15'.

1 分钟复习。Integer 是整数，不加引号：12。整数可以算：12 + 3 = 15。可是 Caption 和输入框里只有 String。需要两个翻译：StrToInt('12') 得到数字 12，IntToStr(15) 得到文字 '15'。

## 03 Percorso facilitato (3 passi)

1. Progetto nuovo. Metti una scritta (A) con Caption 0 e un bottone (OK) con Caption +1.

    مشروع جديد. ضع كتابة (A) بـ Caption هو 0 وزراً (OK) بـ Caption هو +1.

    新项目。放一个文字（A），Caption 写 0；一个按钮（OK），Caption 写 +1。

2. Doppio clic sul bottone e scrivi questa riga sola tra begin e end;.

    انقر مرتين على الزر واكتب هذا السطر وحده بين begin و end;.

    双击按钮，在 begin 和 end; 之间只写这一行。

    ```
      Label1.Caption := IntToStr(StrToInt(Label1.Caption) + 1);
    ```

3. Premi F9 e clicca +1: il numero sale. Screenshot e consegna.

    اضغط F9 وانقر +1: الرقم يرتفع. لقطة شاشة وسلّم.

    按 F9，点 +1：数字增加。截图并提交。

## 04 L'esercitazione, passo per passo

1. **Progetto nuovo.** In alto clicca il menu <b>Progetto</b> → <b>Nuovo progetto…</b> → a sinistra <b>Applicazione</b> → <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.

    في الأعلى انقر القائمة Progetto ← Nuovo progetto… ← على اليسار Applicazione ← OK. في الوسط تظهر النافذة الفارغة Form1.

    点上方菜单 Progetto → Nuovo progetto… → 左边 Applicazione → OK。中间出现空窗口 Form1。

2. **Salva subito, nella cartella nuova.** Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Nella finestra clicca a sinistra <b>Documenti</b>, poi in alto <b>Nuova cartella</b>. Scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella per entrarci.

    القائمة Progetto ← Salva progetto con nome…. في النافذة انقر يساراً Documenti ثم في الأعلى Nuova cartella. اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد للدخول.

    菜单 Progetto → Salva progetto con nome…。在窗口左边点 Documenti，再点上方 Nuova cartella。写下面的名字，按回车，双击文件夹进去。

    ```
    segnapunti
    ```

3. **Il nome del progetto.** In basso, nella casella <b>Nome file</b>, scrivi il nome qui sotto e clicca <b>Salva</b>. Lazarus chiede il nome della unit: lascia <code>unit1.pas</code> e clicca <b>Salva</b>. In alto, nel titolo di Lazarus, c'è scritto <b>segnapunti</b>: FATTO!

    في الأسفل، في خانة Nome file، اكتب الاسم أدناه وانقر Salva. يسأل Lazarus عن اسم الـ unit: اترك unit1.pas وانقر Salva. في عنوان Lazarus مكتوب segnapunti: تم!

    在下面 Nome file 框里写下面的名字，点 Salva。Lazarus 问 unit 的名字：保留 unit1.pas，点 Salva。Lazarus 标题里写着 segnapunti：完成！

    ```
    segnapunti.lpi
    ```

4. **Il numero grande.** Metti una <b>TLabel</b> (la A) al centro della Form1: compare <b>Label1</b>. Nell'Ispettore oggetti cambia <b>Caption</b> in <b>0</b> (zero) e in <b>Font</b> → <b>Size</b> scrivi 48.

    ضع TLabel (الحرف A) في وسط Form1: يظهر Label1. في Ispettore oggetti غيّر Caption إلى 0 (صفر) وفي Font ← Size اكتب 48.

    在 Form1 中间放一个 TLabel（A）：出现 Label1。在 Ispettore oggetti 把 Caption 改成 0（零），在 Font → Size 写 48。

    ```
    0
    ```

5. **Il bottone +1.** Metti un <b>TButton</b> sotto il numero: compare <b>Button1</b>. Cambia <b>Caption</b> in:

    ضع TButton تحت الرقم: يظهر Button1. غيّر Caption إلى:

    在数字下面放一个 TButton：出现 Button1。把 Caption 改成：

    ```
    +1
    ```

6. **La scatola per il numero.** Doppio clic su <b>+1</b>: si apre <code>Button1Click</code>. Clicca alla fine della riga <code>procedure</code>, premi Invio e scrivi prima di <code>begin</code>: una scatola di tipo <b>Integer</b>.

    انقر مرتين على +1: يفتح Button1Click. انقر في نهاية سطر procedure، اضغط Invio واكتب قبل begin: صندوق من نوع Integer.

    双击 +1：打开 Button1Click。点 procedure 那一行的末尾，按回车，在 begin 前面写：一个 Integer 类型的盒子。

    ```
    var
      punti: Integer;
    ```

7. **Tre righe: traduci, conta, traduci.** Tra <code>begin</code> e <code>end;</code> scrivi: 1) <code>StrToInt</code> trasforma la scritta '0' nel numero 0; 2) aggiungi 1; 3) <code>IntToStr</code> trasforma il numero in scritta per la Caption.

    بين begin و end; اكتب: 1) StrToInt يحوّل الكتابة '0' إلى الرقم 0؛ 2) أضف 1؛ 3) IntToStr يحوّل الرقم إلى كتابة للـ Caption.

    在 begin 和 end; 之间写：1）StrToInt 把文字 '0' 变成数字 0；2）加 1；3）IntToStr 把数字变回文字给 Caption。

    ```
      punti := StrToInt(Label1.Caption);
      punti := punti + 1;
      Label1.Caption := IntToStr(punti);
    ```

8. **Fai partire: F9.** Premi <b>F9</b> e clicca <b>+1</b> tante volte: 1, 2, 3, 4… FATTO! Sfida il compagno: chi arriva prima a 30?

    اضغط F9 وانقر +1 مرات كثيرة: 1، 2، 3، 4… تم! تحدَّ زميلك: من يصل أولاً إلى 30؟

    按 F9，多次点 +1：1、2、3、4…… 完成！和同桌比赛：谁先到 30？

9. **La casella dei punti.** Chiudi il programma e premi <b>F12</b> per tornare alla Form1. Metti una <b>TEdit</b> (abc): compare <b>Edit1</b>. Nell'Ispettore oggetti cambia <b>Text</b> in:

    أغلق البرنامج واضغط F12 للعودة إلى Form1. ضع TEdit (abc): يظهر Edit1. في Ispettore oggetti غيّر Text إلى:

    关掉程序，按 F12 回到 Form1。放一个 TEdit（abc）：出现 Edit1。在 Ispettore oggetti 把 Text 改成：

    ```
    3
    ```

10. **Il bottone Aggiungi.** Metti un secondo <b>TButton</b> accanto alla casella: compare <b>Button2</b>. Cambia <b>Caption</b> in <b>Aggiungi</b>. Fai doppio clic su Aggiungi: si apre <code>Button2Click</code>. Prima di <code>begin</code> scrivi due scatole Integer:

    ضع TButton ثانياً بجانب الخانة: يظهر Button2. غيّر Caption إلى Aggiungi. انقر مرتين على Aggiungi: يفتح Button2Click. قبل begin اكتب صندوقين Integer:

    在输入框旁边放第二个 TButton：出现 Button2。把 Caption 改成 Aggiungi。双击 Aggiungi：打开 Button2Click。在 begin 前面写两个 Integer 盒子：

    ```
    var
      punti: Integer;
      aggiunta: Integer;
    ```

11. **Il codice di Aggiungi.** Tra <code>begin</code> e <code>end;</code> scrivi le quattro righe: anche la casella ha una String, quindi anche lì serve <code>StrToInt</code>.

    بين begin و end; اكتب الأسطر الأربعة: الخانة أيضاً فيها String، لذلك نحتاج هناك أيضاً StrToInt.

    在 begin 和 end; 之间写这四行：输入框里也是 String，所以那里也要用 StrToInt。

    ```
      punti := StrToInt(Label1.Caption);
      aggiunta := StrToInt(Edit1.Text);
      punti := punti + aggiunta;
      Label1.Caption := IntToStr(punti);
    ```

12. **Prova Aggiungi.** Premi <b>F9</b>. Clicca <b>Aggiungi</b>: il numero sale di 3. Scrivi 10 nella casella e clicca ancora: sale di 10. FATTO! Fai lo screenshot.

    اضغط F9. انقر Aggiungi: يرتفع الرقم 3. اكتب 10 في الخانة وانقر مجدداً: يرتفع 10. تم! خذ لقطة شاشة.

    按 F9。点 Aggiungi：数字加 3。在输入框写 10，再点：加 10。完成！截图。

13. **Il bottone Azzera.** Chiudi il programma, F12. Metti un terzo <b>TButton</b>: <b>Button3</b>, Caption <b>Azzera</b>. Doppio clic e scrivi la riga. '0' ha gli apici: la Caption vuole una String.

    أغلق البرنامج، F12. ضع TButton ثالثاً: Button3، Caption هو Azzera. انقر مرتين واكتب السطر. '0' لها علامتا اقتباس: الـ Caption تريد String.

    关掉程序，F12。放第三个 TButton：Button3，Caption 写 Azzera。双击，写这一行。'0' 有引号：Caption 要的是 String。

    ```
      Label1.Caption := '0';
    ```

14. **La trappola del 53.** Prova a capire senza scriverlo: se in Aggiungi ci fosse <code>Label1.Caption := Label1.Caption + Edit1.Text;</code>, con 5 sul display e 3 nella casella, comparirebbe <b>53</b>, non 8. Perché? Due String si ATTACCANO, due Integer si SOMMANO. Scrivilo nel quaderno.

    حاول أن تفهم دون أن تكتبه: لو كان في Aggiungi السطر Label1.Caption := Label1.Caption + Edit1.Text; مع 5 على الشاشة و3 في الخانة، لظهر 53 وليس 8. لماذا؟ نصّان يُلصقان، وعددان يُجمعان. اكتبه في الدفتر.

    不写代码，想一想：如果 Aggiungi 里写的是 Label1.Caption := Label1.Caption + Edit1.Text;，显示 5，输入框写 3，会出现 53，而不是 8。为什么？两个 String 是连起来，两个 Integer 是相加。写进本子里。

15. **Fallo tuo.** Una scritta con il tuo nome sopra il numero (una Label con Caption <i>Segnapunti di Ahmed</i>), i tuoi colori, e il bottone <b>+1</b> che diventa <b>+2</b> (cambia <code>punti + 1</code> e la Caption). Chi ha finito: un bottone <b>-1</b>.

    كتابة باسمك فوق الرقم (Label بـ Caption هو Segnapunti di Ahmed)، ألوانك، والزر +1 يصبح +2 (غيّر punti + 1 والـ Caption). من أنهى: زر -1.

    数字上方加一行写着你名字的文字（一个 Label，Caption 写 Segnapunti di Ahmed），你的颜色，再把 +1 按钮变成 +2（改 punti + 1 和 Caption）。做完的同学：加一个 -1 按钮。

## 05 Tre aiuti

1. Indizio: La Caption è una String: per contare la traduci in Integer con <code>StrToInt</code>, fai il conto, e la ritraduci con <code>IntToStr</code>. Le righe <code>var</code> vanno prima di <code>begin</code>.
2. Il pezzo di codice:

    ```
    procedure TForm1.Button2Click(Sender: TObject);
    var
      punti: Integer;
      aggiunta: Integer;
    begin
      punti := StrToInt(Label1.Caption);
      aggiunta := StrToInt(Edit1.Text);
      punti := punti + aggiunta;
      Label1.Caption := IntToStr(punti);
    end;
    ```

3. Tutto unit1.pas: `codice/ora3_unit1.pas`.

## 06 Spiegalo in 30 secondi

Al compagno: nel tuo segnapunti, che cosa fa <code>StrToInt</code> e che cosa fa <code>IntToStr</code>? Perché servono tutti e due?

لزميلك: في عدّاد نقاطك، ماذا يفعل StrToInt وماذا يفعل IntToStr؟ لماذا نحتاج الاثنين؟

对同桌说：在你的记分牌里，StrToInt 做什么，IntToStr 做什么？为什么两个都需要？

## 07 Consegna: unit1.pas + screenshot

1. Piano A: pagina `consegna.html?ora=3`: scegli unit1.pas e lo screenshot, il controllo automatico dice subito se il codice va bene, un bottone manda tutto.
2. Piano B, se il bottone non funziona: Classroom, passi C1-C5.

    1. **C1 Lo screenshot del programma che gira.** Premi <b>F9</b>: il tuo programma è aperto. Premi insieme <b>Win + Shift + S</b> e con il mouse disegna un rettangolo intorno alla tua finestra. In basso a destra clicca l'avviso <b>Ritaglio</b>: si apre lo Strumento di cattura. Premi <b>Ctrl + S</b>, a sinistra clicca <b>Documenti</b>, doppio clic sulla cartella <b>segnapunti</b>, in <b>Nome file</b> scrivi il nome qui sotto e clicca <b>Salva</b>.

        ```
        ora3_screenshot.png
        ```

    2. **C2 Trova unit1.pas.** Premi <b>Win + E</b> (Esplora file). A sinistra clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>segnapunti</b>. In alto clicca <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>: ora vedi le lettere dopo il punto. Il file del tuo codice è <code>unit1.pas</code>.

    3. **C3 Fai la copia da consegnare.** Clicca una volta <code>unit1.pas</code>. Premi <b>Ctrl + C</b> e poi <b>Ctrl + V</b>: compare <code>unit1 - Copia.pas</code>. Cliccala una volta, premi <b>F2</b>, scrivi il nome qui sotto e premi Invio. (L'originale <code>unit1.pas</code> resta lì: il progetto funziona ancora.)

        ```
        ora3_unit1.pas
        ```

    4. **C4 Su Classroom: aggiungi i due file.** Apri il compito <b>Ora 3 · Il segnapunti</b> su Classroom. A destra, nel riquadro <b>Il tuo lavoro</b>, clicca <b>+ Aggiungi o crea</b> → <b>File</b> → <b>Sfoglia</b>. Vai in <b>Documenti</b> → <b>segnapunti</b>, scegli <code>ora3_unit1.pas</code> e clicca <b>Apri</b>. Rifai lo stesso per <code>ora3_screenshot.png</code>.

    5. **C5 Consegna.** Nel riquadro <b>Il tuo lavoro</b> vedi i due file: <code>ora3_unit1.pas</code> e <code>ora3_screenshot.png</code>. Clicca <b>Consegna</b> e poi ancora <b>Consegna</b>. FATTO!

## 08 Controllo finale

1. Il mio segnapunti sale con +1 e con Aggiungi, e torna a 0 con Azzera.
2. So dire perché serve StrToInt prima del conto e IntToStr dopo.
3. So spiegare perché '5' + '3' darebbe 53.
4. Ho consegnato ora3_unit1.pas e ora3_screenshot.png.

## 09 Da ricopiare sul quaderno

```
var punti: Integer;                  scatola per un numero intero
punti := StrToInt(Label1.Caption);   testo -> numero   '5' -> 5
punti := punti + 1;                  il conto (solo con gli Integer)
Label1.Caption := IntToStr(punti);   numero -> testo   6 -> '6'
'5' + '3' = '53'          5 + 3 = 8
```
