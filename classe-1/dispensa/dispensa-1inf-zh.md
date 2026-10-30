# 1INF 课堂讲义：到 2026年10月30日 为止的课和练习

(Dispensa unica 1INF — lezioni ed esercizi fino al 30/10/2026)

**Versione 1.1** — 30/10/2026 · 简体中文版 (traduzione in cinese semplificato)

*1INF 班 · 信息技术、技术、实验室和安全 · 2026/2027 学年。只有一份讲义，每个人都一样：从 15/09 到 30/10/2026 的课，按日期排列。里面有简短的理论、黑板照片、要抄在本子上的句子，还有 Classroom 上的所有作业。PDF 用来阅读和打印；MD 文件可以给你自己的 AI（Gemini、NotebookLM），让它给你解释。*

*这一版先翻译了 30/10 的两章（第 25 章和第 26 章）。其他章节很快会在下一版里加上。*

---

## 00 怎么使用这份讲义

(Come si usa questa dispensa)

1. 每一章就是**一天的课**，按日期排列。每一章里面总是有这些部分：
   1.1 **时间**：日期、几点、什么课；
   1.2 **我们做了什么**；
   1.3 **理论**：简短但完整，有黑板照片；
   1.4 **抄在本子上**：有要抄的东西时才有；
   1.5 **练习和作业**：Classroom 上的标题、要做什么、链接、要交什么。
2. 最后有**所有作业的表格**（第 27 章）和**词汇表**（第 28 章）。
3. 你没来上课？先读那一天的章节，再打开 Classroom 上的作业，把它做完。作业一直开着，可以补做，除非老师另外说明。
4. 有一个词看不懂？把这个文件给你的 AI，问它：«用我的语言解释第 10 章，举一个例子。» AI 帮你**理解**，不是替你做作业。
5. Classroom 的链接只能用学校的账号打开。以 `nicolaregge-pulse.github.io` 开头的链接是课堂网页，任何浏览器都能打开。

> [GIALLO] 这门课的方法只有三句话：**马上赢**（几分钟就有第一个结果），**做成你自己的**（选你自己的东西：名字、颜色、游戏），**给别人看**（给同学看）。出错很正常：所有程序员都会出错，专业的也一样。

---

## 25 星期五 30/10/2026，8-9 点：Unicode 和 ASCII 码；字符串和整数

(Venerdì 30/10/2026, ora 8-9 — Unicode e codice ASCII; stringhe e interi)

### 25.1 时间
1. 星期五 30/10/2026，8-9 点，信息技术课（Informatica）。

### 25.2 我们做了什么
1. ASCII 码，一个字节（byte）里的 256 个字符，适合所有语言的 Unicode，十六进制数字，UTF-8；然后是第 2 部分：字符串和整数（String 和 Integer）。

### 25.3 理论：Unicode
1. 电脑只认识 0 和 1。
2. **ASCII 码：** 每个字母都有一个数字。**A** = 65 = `01000001`；**B** = 66 = `01000010`。最早的 ASCII 用 7 个比特（bit），也就是 128 个字符：只有拉丁字母、数字和符号。
3. **只有 256 个字符：** 8 个比特有 256 种组合，从 `00000000` 到 `11111111`。对世界上所有的语言来说，这不够：128 个或 256 个位置放不下阿拉伯字母、汉字和表情符号（emoji）。以前每个国家都有自己的表，文字常常会坏掉（出现奇怪的符号，比如 Ã© 或 ???）。
4. **Unicode** 是**一张**表，给**所有**语言用：有 150.000 多个字符，每个字符有自己的号码，在所有电脑和手机上都一样。前 128 个位置就是 ASCII：A 还是 65。
5. **Unicode 号码**的写法：U+ 加上 4 个十六进制数字：**A** = U+0041；阿拉伯字母 **ب** = U+0628；汉字 **中** = U+4E2D。
6. **十六进制数字**一共 16 个：0 1 2 3 4 5 6 7 8 9，然后 A = 10，B = 11，C = 12，D = 13，E = 14，F = 15。
7. **UTF-8：** 文件里这样保存号码：拉丁字母 1 个字节，阿拉伯字母 2 个字节，汉字 3 个字节，表情符号 4 个字节。
8. **用 30 秒给同学讲一讲：** «为什么我的手机上阿拉伯文和中文都能正常显示？»

![30/10 的黑板：Unicode、整数和字符串；ASCII 码（A = 65 = 01000001，B = 66 = 01000010）；红色字：只有 256 个字符](../unicode/immagini/20261030_lavagna-unicode-ascii.jpg)

![30/10 的黑板 2：A = U+0041，ب = U+0628，中 = U+4E2D，还有从 0 到 F 的十六进制数字](../unicode/immagini/20261030_lavagna-unicode-esadecimale.jpg)

### 25.4 理论：字符串和整数（String 和 Integer）
1. **变量**（variabile）是一个有名字的盒子，盒子里有一个值。`:=` 的意思是«放进去»。每个盒子都有一个**类型**。
2. **String**（字符串）= **文字**，总是写在**单引号**里：`'Ciao'`、`'Milano'`、`'007'`（有单引号就是文字，就算里面是数字）。两个 String 之间的 `+` 会把它们**连起来**：`'Ciao ' + 'Ahmed'` = `'Ciao Ahmed'`。
3. **Integer**（整数）= **整数数字**，没有单引号，没有小数点，也可以是负数：`0`、`7`、`2026`、`-5`。用 Integer 可以做计算；`3.5` 不是 Integer。
4. **陷阱：** `'5' + '3'` = `'53'`（String，连起来）；`5 + 3` = `8`（Integer，相加）。黑板上：`'12' + '15'` = `'1215'`，`12 + 15` = `27`。
5. **在 Lazarus 里，框里的内容是 String：** `Edit1.Text`、`Label1.Caption` 和 `Button1.Caption` 都是 String。`Label1.Caption := 7;` 会出错（Incompatible types，类型不兼容）；`Label1.Caption := '7';` 是对的。
6. **两个翻译员：** `StrToInt('7')` 给出数字 7；`IntToStr(7)` 给出文字 `'7'`。一个数字的旅程：输入框 → StrToInt → 计算 → IntToStr → Caption。如果框里写的是 *ciao*，StrToInt 翻译不了，程序会因为错误停下来。

![30/10 的黑板 3：左边是字符串（STRINGHE），右边是整数（INTERI）；'12' + '15' = '1215'，12 + 15 = 27](../unicode/immagini/20261030_lavagna-stringhe-interi.jpg)

### 25.5 抄在本子上

本子上抄意大利语原文（和黑板上一样）；下面是中文意思。

```
ASCII = 128 caratteri, solo lettere latine. A = 65.
UNICODE = una tabella per TUTTE le lingue.
UTF-8 = latino 1 byte, arabo 2, cinese 3, emoji 4.
String = testo, tra apici: 'Mario'
Integer = numero intero, senza apici: 15
StrToInt = da testo a numero. IntToStr = da numero a testo.
```

1. ASCII = 128 个字符，只有拉丁字母。A = 65。
2. UNICODE = 一张表，给所有语言用。
3. UTF-8 = 拉丁字母 1 个字节，阿拉伯字母 2 个，汉字 3 个，表情符号 4 个。
4. String = 文字，写在单引号里：'Mario'
5. Integer = 整数，没有单引号：15
6. StrToInt = 从文字变成数字。IntToStr = 从数字变成文字。

### 25.6 练习和作业
1. **OGGI 30/10: il computer scrive in tutte le lingue**（今天 30/10：电脑会写所有的语言）
   1.1 要做什么：打开这节课的网页，读卡片，在框里写你的名字（也可以用阿拉伯文或中文）：你会看到每个字符的 Unicode 号码。把第 7 张卡片的句子抄在本子上。做 Moduli 上的测验（15 道题）。然后是第 2 部分：读 6 张关于 String 和 Integer 的卡片，做复习，再做 Moduli 上的测验（22 道题）。把第 2 部分的句子抄在本子上。
   1.2 Unicode 网页：https://nicolaregge-pulse.github.io/corso-informatica/1inf-unicode/
   1.3 Unicode 测验：https://docs.google.com/forms/d/e/1FAIpQLSegqxhNi56-IiLTOvWmIYDvC3rFf8KJm3AOg-HneFKDinwIxg/viewform
   1.4 String 和 Integer：https://nicolaregge-pulse.github.io/corso-informatica/verifica/?b=1inf-lab3010-tipi
   1.5 String 和 Integer 测验：https://docs.google.com/forms/d/e/1FAIpQLScEmtd4AdC2KLC60oQ2nxhUpiOLmzQ8PSmuUmwNTSFAl8XhBg/viewform
   1.6 链接：https://classroom.google.com/c/ODc3MDA4ODA3MzM2/a/ODk2NjMzMTU2NzUz/details
   1.7 要交什么：网页上的复习，和 Moduli 上已经提交的两个测验。

---

## 26 星期五 30/10/2026，11-14 点：实验室：在 Lazarus 里用字符串和整数

(Venerdì 30/10/2026, ore 11-14 — Laboratorio: stringhe e interi in Lazarus)

### 26.1 时间
1. 星期五 30/10/2026，11-14 点，实验室课（Laboratorio），3 个小时，每小时一个程序。

### 26.2 要做什么
1. 在 Lazarus 里做三个程序，每小时一个，练习用 String 和 Integer：数字的乱子、外号、记分牌。每个小时都有一条 3 步的简单路线，给有困难的同学。
2. **Lazarus 帮助：** 如果你不会建 Lazarus 项目，就举手请老师帮忙：老师会到你的座位来。别的问题请用助手的输入框问。

### 26.3 理论
1. 理论就是第 25.4 章的内容：变量、String、Integer、`+` 的陷阱、StrToInt 和 IntToStr。
2. **`var` 这几行**（盒子）要写在 `begin` 的**前面**。
3. **带单引号的 `'nome'`** 是«nome»这个**词**；**不带单引号的 `nome`** 是叫 nome 的**盒子**。
4. **要用 Caption 来计算：** 先用 `StrToInt` 把它变成 Integer，再计算，然后用 `IntToStr` 变回文字。

### 26.4 第 1 小时（11-12）：数字的乱子
1. 新建项目，保存在 Documenti（文档）里的新文件夹 `pasticcio` 中（`pasticcio.lpi`、`unit1.pas`）。
2. 一个 Label，Caption 是 `?`，还有两个按钮：**Testo**（文字）和 **Numeri**（数字）。
3. Testo 按钮：`Label1.Caption := '5' + '3';` → 显示 **53**：两个 String 连在一起。
4. Numeri 按钮：两个 Integer 盒子，`a := 5; b := 3;`。`Label1.Caption := a + b;` 会出错 **Incompatible types**（每个人都会遇到）；改成 `IntToStr(a + b)` → 显示 **8**。
5. 做成你自己的：用你自己的两个数字（比如你的年龄和你的球衣号码）。

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

### 26.5 第 2 小时（12-13）：外号生成器
1. 新项目 `soprannome`：两个 TEdit（TextHint 写 «Il tuo nome»（你的名字）和 «Un animale»（一种动物）），一个按钮 «Crea il soprannome»（生成外号），一个大的 Label。
2. 程序把框里的文字放进 String 盒子，再用 `+` 连起来：比如会显示 «Ahmed detto Leone!»（叫做狮子的 Ahmed！）。
3. 单引号的陷阱：如果写 `'nome'`，显示的是 «nome» 这个词，不是你的名字。
4. 做成你自己的：把 « detto » 换成你自己的话，换文字的颜色。

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

### 26.6 第 3 小时（13-14）：记分牌
1. 新项目 `segnapunti`：一个大的 Label，Caption 是 `0`，按钮 **+1**、**Aggiungi**（加上，旁边有一个 TEdit 写分数）和 **Azzera**（清零）。
2. +1：翻译、计算、再翻译（`StrToInt`、`+ 1`、`IntToStr`）。Aggiungi：输入框里的也是 String，所以要 `StrToInt(Edit1.Text)`。Azzera：`Label1.Caption := '0';`。
3. 53 的陷阱：`Label1.Caption + Edit1.Text`，如果是 5 和 3，会得到 53，不是 8。
4. 做成你自己的：在数字上面加一行写你的名字，用你的颜色，再加一个 +2 按钮。

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

### 26.7 抄在本子上

本子上抄意大利语原文；下面是中文意思。

```
VARIABILE = una scatola con un nome, dentro c'e' un valore
STRING  = testo, sempre tra apici:   'Ciao'   '5'
INTEGER = numero intero, senza apici:  5   12   -3
'5' + '3' = '53'  (attacca)      5 + 3 = 8  (somma)
Label1.Caption := IntToStr(a + b);  giusto: 8
var nome: String;          preparo la scatola per il testo
nome := Edit1.Text;        metto nella scatola il testo della casella
'nome' con gli apici = la PAROLA nome
nome  senza apici    = la SCATOLA nome
punti := StrToInt(Label1.Caption);   testo -> numero   '5' -> 5
Label1.Caption := IntToStr(punti);   numero -> testo   6 -> '6'
```

1. 变量 = 一个有名字的盒子，里面有一个值。
2. STRING = 文字，总是在单引号里：'Ciao' '5'
3. INTEGER = 整数，没有单引号：5 12 -3
4. '5' + '3' = '53'（连起来）；5 + 3 = 8（相加）
5. `Label1.Caption := IntToStr(a + b);` 正确：8
6. `var nome: String;` 准备一个放文字的盒子
7. `nome := Edit1.Text;` 把输入框里的文字放进盒子
8. 带单引号的 'nome' = nome 这个词；不带单引号的 nome = 叫 nome 的盒子
9. `punti := StrToInt(Label1.Caption);` 文字 → 数字，'5' → 5
10. `Label1.Caption := IntToStr(punti);` 数字 → 文字，6 → '6'

### 26.8 练习和作业
1. **OGGI 30/10: Laboratorio 11-14: stringhe e interi in Lazarus (3 programmi)**（今天 30/10：11-14 点实验室，Lazarus 里的字符串和整数，3 个程序）
   1.1 要做什么：每个小时打开路线网页，一步一步做，然后提交。
   1.2 第 1 小时：https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lab-30-10/modulo-1.html
   1.3 第 2 小时：https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lab-30-10/modulo-2.html
   1.4 第 3 小时：https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lab-30-10/modulo-3.html
   1.5 提交：https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lab-30-10/consegna.html （加上 `?ora=1`、`?ora=2`、`?ora=3`）
   1.6 要交什么：每个小时交 `unit1.pas` 和程序运行时的截图，用提交网页上的按钮。B 计划，如果按钮不能用：在 Classroom 的作业里附上这个小时的两个文件（比如 `ora1_unit1.pas` 和 `ora1_screenshot.png`），然后按 «Consegna»（提交）。

---

