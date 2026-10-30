# Ora 2: le caselle e le String, il generatore di soprannomi

**Versione 1.0** — 29/10/2026 — ANTEPRIMA per il prof, non pubblicata

*1INF · Laboratorio · venerdì 30/10/2026, 12:00-13:00 · progetto `soprannome` · si consegnano SEMPRE unit1.pas e lo screenshot*

الساعة 2: الخانات و String، مولّد الألقاب

第 2 节：输入框和 String，外号生成器

## 01 Che cosa fai in quest'ora

Un programma nuovo: scrivi il tuo nome e un animale, premi il bottone e il programma inventa il tuo soprannome: <b>Ahmed detto Leone!</b> Tutto quello che c'è in una casella è una <b>String</b>.

برنامج جديد: تكتب اسمك وحيواناً، تضغط الزر فيخترع البرنامج لقبك: Ahmed detto Leone! كل ما في الخانة هو String.

一个新程序：写你的名字和一种动物，按按钮，程序给你编一个外号：Ahmed detto Leone！输入框里的一切都是 String。

## 02 Ripasso in 1 minuto

<b>Ripasso in 1 minuto.</b> Una <b>String</b> è testo: sta tra apici, <code>'Ciao'</code>. Il <code>+</code> attacca due String: <code>'Ciao ' + 'Ahmed'</code> = <code>'Ciao Ahmed'</code>. Quello che l'utente scrive in <b>Edit1</b> si legge con <code>Edit1.Text</code>, ed è sempre una String. Una <b>variabile</b> è una scatola con un nome: <code>var nome: String;</code> prepara la scatola <i>nome</i> per il testo.

مراجعة في دقيقة. String هي نص: بين علامتي اقتباس 'Ciao'. علامة + تلصق نصين: 'Ciao ' + 'Ahmed' = 'Ciao Ahmed'. ما يكتبه المستخدم في Edit1 يُقرأ بـ Edit1.Text وهو دائماً String. المتغير صندوق له اسم: var nome: String; يجهّز الصندوق nome للنص.

1 分钟复习。String 是文字：放在单引号里 'Ciao'。+ 把两个 String 连起来：'Ciao ' + 'Ahmed' = 'Ciao Ahmed'。用户在 Edit1 里写的东西用 Edit1.Text 读取，它永远是 String。变量是一个有名字的盒子：var nome: String; 准备一个叫 nome 的盒子装文字。

## 03 Percorso facilitato (3 passi)

1. Progetto nuovo: menu Progetto → Nuovo progetto… → Applicazione → OK. Metti una casella (abc), un bottone (OK) e una scritta (A).

    مشروع جديد: Progetto ← Nuovo progetto… ← Applicazione ← OK. ضع خانة (abc) وزراً (OK) وكتابة (A).

    新项目：Progetto → Nuovo progetto… → Applicazione → OK。放一个输入框（abc）、一个按钮（OK）和一个文字（A）。

2. Doppio clic sul bottone e scrivi la riga tra begin e end;.

    انقر مرتين على الزر واكتب السطر بين begin و end;.

    双击按钮，在 begin 和 end; 之间写这一行。

    ```
      Label1.Caption := 'Ciao ' + Edit1.Text;
    ```

3. Premi F9, scrivi il tuo nome e premi il bottone: compare Ciao e il tuo nome. Screenshot e consegna.

    اضغط F9، اكتب اسمك واضغط الزر: يظهر Ciao واسمك. لقطة شاشة وسلّم.

    按 F9，写你的名字，按按钮：出现 Ciao 和你的名字。截图并提交。

## 04 L'esercitazione, passo per passo

1. **Progetto nuovo.** In alto clicca il menu <b>Progetto</b> → <b>Nuovo progetto…</b> → a sinistra <b>Applicazione</b> → <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.

    في الأعلى انقر القائمة Progetto ← Nuovo progetto… ← على اليسار Applicazione ← OK. في الوسط تظهر النافذة الفارغة Form1.

    点上方菜单 Progetto → Nuovo progetto… → 左边 Applicazione → OK。中间出现空窗口 Form1。

2. **Salva subito, nella cartella nuova.** Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Nella finestra clicca a sinistra <b>Documenti</b>, poi in alto <b>Nuova cartella</b>. Scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella per entrarci.

    القائمة Progetto ← Salva progetto con nome…. في النافذة انقر يساراً Documenti ثم في الأعلى Nuova cartella. اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد للدخول.

    菜单 Progetto → Salva progetto con nome…。在窗口左边点 Documenti，再点上方 Nuova cartella。写下面的名字，按回车，双击文件夹进去。

    ```
    soprannome
    ```

3. **Il nome del progetto.** In basso, nella casella <b>Nome file</b>, scrivi il nome qui sotto e clicca <b>Salva</b>. Lazarus chiede il nome della unit: lascia <code>unit1.pas</code> e clicca <b>Salva</b>. In alto, nel titolo di Lazarus, c'è scritto <b>soprannome</b>: FATTO!

    في الأسفل، في خانة Nome file، اكتب الاسم أدناه وانقر Salva. يسأل Lazarus عن اسم الـ unit: اترك unit1.pas وانقر Salva. في عنوان Lazarus مكتوب soprannome: تم!

    在下面 Nome file 框里写下面的名字，点 Salva。Lazarus 问 unit 的名字：保留 unit1.pas，点 Salva。Lazarus 标题里写着 soprannome：完成！

    ```
    soprannome.lpi
    ```

4. **La casella del nome.** Nella palette <b>Standard</b> clicca la casella con <b>abc</b> (è la <b>TEdit</b>) e clicca nella Form1, in alto: compare <b>Edit1</b>. Nell'Ispettore oggetti trova <b>Text</b> e cancella la scritta: la casella resta vuota.

    في لوحة Standard انقر الخانة التي فيها abc (هي TEdit) وانقر في Form1 في الأعلى: يظهر Edit1. في Ispettore oggetti ابحث عن Text وامسح الكتابة: تبقى الخانة فارغة.

    在 Standard 组件面板点带 abc 的输入框（就是 TEdit），再点 Form1 上方：出现 Edit1。在 Ispettore oggetti 找到 Text，删掉文字：输入框变空。

5. **Il suggerimento grigio.** Sempre per Edit1, nell'Ispettore oggetti trova <b>TextHint</b> e scrivi il testo qui sotto. Quando la casella è vuota, si vede in grigio.

    لـ Edit1 أيضاً، في Ispettore oggetti ابحث عن TextHint واكتب النص أدناه. عندما تكون الخانة فارغة يظهر بالرمادي.

    还是 Edit1，在 Ispettore oggetti 找到 TextHint，写下面的文字。输入框空的时候，它显示成灰色。

    ```
    Il tuo nome
    ```

6. **La casella dell'animale.** Metti una seconda TEdit sotto la prima: compare <b>Edit2</b>. Cancella il suo <b>Text</b> e in <b>TextHint</b> scrivi:

    ضع TEdit ثانية تحت الأولى: يظهر Edit2. امسح Text الخاص بها وفي TextHint اكتب:

    在第一个下面再放一个 TEdit：出现 Edit2。删掉它的 Text，在 TextHint 里写：

    ```
    Un animale
    ```

7. **Il bottone.** Metti un <b>TButton</b> (il bottone OK) sotto le caselle: compare <b>Button1</b>. Nell'Ispettore oggetti cambia <b>Caption</b> in:

    ضع TButton (الزر OK) تحت الخانات: يظهر Button1. في Ispettore oggetti غيّر Caption إلى:

    在输入框下面放一个 TButton（OK 按钮）：出现 Button1。在 Ispettore oggetti 把 Caption 改成：

    ```
    Crea il soprannome
    ```

8. **La scritta del risultato.** Metti una <b>TLabel</b> (la A) sotto il bottone: compare <b>Label1</b>. Cambia <b>Caption</b> in tre puntini e, in <b>Font</b> → <b>Size</b>, scrivi 24.

    ضع TLabel (الحرف A) تحت الزر: يظهر Label1. غيّر Caption إلى ثلاث نقاط وفي Font ← Size اكتب 24.

    在按钮下面放一个 TLabel（A）：出现 Label1。把 Caption 改成三个点，在 Font → Size 里写 24。

    ```
    ...
    ```

9. **Le scatole per il testo.** Fai doppio clic sul bottone: si apre <code>procedure TForm1.Button1Click</code>. Clicca alla fine di quella riga, premi Invio e scrivi le tre righe <b>prima</b> di <code>begin</code>. Sono due scatole (variabili) di tipo <b>String</b>.

    انقر مرتين على الزر: يفتح procedure TForm1.Button1Click. انقر في نهاية ذلك السطر، اضغط Invio واكتب الأسطر الثلاثة قبل begin. هما صندوقان (متغيران) من نوع String.

    双击按钮：打开 procedure TForm1.Button1Click。点那一行的末尾，按回车，在 begin 前面写这三行。这是两个 String 类型的盒子（变量）。

    ```
    var
      nome: String;
      animale: String;
    ```

10. **Il codice del soprannome.** Tra <code>begin</code> e <code>end;</code> scrivi le tre righe. Prima metti il testo delle caselle nelle scatole, poi attacchi tutto con <code>+</code>. Attenzione agli spazi dentro <code>' detto '</code>.

    بين begin و end; اكتب الأسطر الثلاثة. أولاً تضع نص الخانات في الصناديق، ثم تلصق كل شيء بـ +. انتبه للمسافات داخل ' detto '.

    在 begin 和 end; 之间写这三行。先把输入框里的文字放进盒子，再用 + 全部连起来。注意 ' detto ' 里面的空格。

    ```
      nome := Edit1.Text;
      animale := Edit2.Text;
      Label1.Caption := nome + ' detto ' + animale + '!';
    ```

11. **Fai partire: F9.** Premi <b>F9</b>. Scrivi il tuo nome e un animale, clicca <b>Crea il soprannome</b>: compare per esempio <b>Ahmed detto Leone!</b> FATTO! Fallo provare al compagno con il suo nome.

    اضغط F9. اكتب اسمك وحيواناً وانقر Crea il soprannome: يظهر مثلاً Ahmed detto Leone! تم! دع زميلك يجرّب باسمه.

    按 F9。写你的名字和一种动物，点 Crea il soprannome：出现比如 Ahmed detto Leone！完成！让同桌用他的名字试试。

12. **La trappola degli apici.** Chiudi il programma. Nell'ultima riga metti gli apici intorno a nome: <code>'nome'</code>. Premi F9 e prova: compare <b>nome detto Leone!</b> Perché? Con gli apici è la PAROLA nome, senza apici è la SCATOLA nome. Togli gli apici.

    أغلق البرنامج. في السطر الأخير ضع علامتي اقتباس حول nome: 'nome'. اضغط F9 وجرّب: يظهر nome detto Leone! لماذا؟ مع علامات الاقتباس هي الكلمة nome، وبدونها هي الصندوق nome. أزل علامات الاقتباس.

    关掉程序。在最后一行给 nome 加上引号：'nome'。按 F9 试试：出现 nome detto Leone！为什么？有引号是“nome”这个词，没有引号是叫 nome 的盒子。把引号去掉。

    ```
      Label1.Caption := 'nome' + ' detto ' + animale + '!';
    ```

13. **Fallo tuo: la tua frase.** Cambia <code>' detto '</code> con parole tue, per esempio <code>' il re dei '</code> o <code>' il super '</code> (con uno spazio prima e dopo). Cambia il colore della scritta (<b>Font</b> → <b>Color</b>). Chi ha finito: <b>Button2</b> con Caption <b>Cancella</b> e questo codice:

    غيّر ' detto ' بكلماتك، مثلاً ' il re dei ' أو ' il super ' (مع مسافة قبل وبعد). غيّر لون الكتابة (Font ← Color). من أنهى: Button2 بـ Caption هو Cancella وهذا الكود:

    把 ' detto ' 换成你自己的话，比如 ' il re dei ' 或 ' il super '（前后各有一个空格）。改文字的颜色（Font → Color）。做完的同学：Button2，Caption 写 Cancella，代码如下：

    ```
      Edit1.Text := '';
      Edit2.Text := '';
      Label1.Caption := '...';
    ```

## 05 Tre aiuti

1. Indizio: Le righe <code>var</code> vanno PRIMA di <code>begin</code>. Le scatole si riempiono con <code>:=</code>. Le parole fisse vanno tra apici, le scatole no.
2. Il pezzo di codice:

    ```
    procedure TForm1.Button1Click(Sender: TObject);
    var
      nome: String;
      animale: String;
    begin
      nome := Edit1.Text;
      animale := Edit2.Text;
      Label1.Caption := nome + ' detto ' + animale + '!';
    end;
    ```

3. Tutto unit1.pas: `codice/ora2_unit1.pas`.

## 06 Spiegalo in 30 secondi

Al compagno: che differenza c'è tra <code>'nome'</code> e <code>nome</code> nel tuo programma?

لزميلك: ما الفرق بين 'nome' و nome في برنامجك؟

对同桌说：在你的程序里，'nome' 和 nome 有什么区别？

## 07 Consegna: unit1.pas + screenshot

1. Piano A: pagina `consegna.html?ora=2`: scegli unit1.pas e lo screenshot, il controllo automatico dice subito se il codice va bene, un bottone manda tutto.
2. Piano B, se il bottone non funziona: Classroom, passi C1-C5.

    1. **C1 Lo screenshot del programma che gira.** Premi <b>F9</b>: il tuo programma è aperto. Premi insieme <b>Win + Shift + S</b> e con il mouse disegna un rettangolo intorno alla tua finestra. In basso a destra clicca l'avviso <b>Ritaglio</b>: si apre lo Strumento di cattura. Premi <b>Ctrl + S</b>, a sinistra clicca <b>Documenti</b>, doppio clic sulla cartella <b>soprannome</b>, in <b>Nome file</b> scrivi il nome qui sotto e clicca <b>Salva</b>.

        ```
        ora2_screenshot.png
        ```

    2. **C2 Trova unit1.pas.** Premi <b>Win + E</b> (Esplora file). A sinistra clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>soprannome</b>. In alto clicca <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>: ora vedi le lettere dopo il punto. Il file del tuo codice è <code>unit1.pas</code>.

    3. **C3 Fai la copia da consegnare.** Clicca una volta <code>unit1.pas</code>. Premi <b>Ctrl + C</b> e poi <b>Ctrl + V</b>: compare <code>unit1 - Copia.pas</code>. Cliccala una volta, premi <b>F2</b>, scrivi il nome qui sotto e premi Invio. (L'originale <code>unit1.pas</code> resta lì: il progetto funziona ancora.)

        ```
        ora2_unit1.pas
        ```

    4. **C4 Su Classroom: aggiungi i due file.** Apri il compito <b>Laboratorio 11-14: stringhe e interi in Lazarus</b> su Classroom (è uno solo per le tre ore). Se vedi il bottone <b>Annulla consegna</b>, cliccalo prima: i file delle ore prima restano lì. A destra, nel riquadro <b>Il tuo lavoro</b>, clicca <b>+ Aggiungi o crea</b> → <b>File</b> → <b>Sfoglia</b>. Vai in <b>Documenti</b> → <b>soprannome</b>, scegli <code>ora2_unit1.pas</code> e clicca <b>Apri</b>. Rifai lo stesso per <code>ora2_screenshot.png</code>.

    5. **C5 Consegna.** Nel riquadro <b>Il tuo lavoro</b> vedi i due file: <code>ora2_unit1.pas</code> e <code>ora2_screenshot.png</code>. Clicca <b>Consegna</b> e poi ancora <b>Consegna</b>. FATTO!

## 08 Controllo finale

1. Il mio programma legge le due caselle e scrive il soprannome.
2. So dove vanno le righe var (prima di begin).
3. So spiegare perché 'nome' con gli apici scrive la parola nome.
4. Ho consegnato ora2_unit1.pas e ora2_screenshot.png.

## 09 Da ricopiare sul quaderno

```
var nome: String;          preparo la scatola per il testo
nome := Edit1.Text;        metto nella scatola il testo della casella
Label1.Caption := nome + ' detto ' + animale;   + attacca le String
'nome' con gli apici = la PAROLA nome
nome  senza apici    = la SCATOLA nome
```
