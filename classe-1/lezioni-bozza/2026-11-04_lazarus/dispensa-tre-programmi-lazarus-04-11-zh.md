# Lazarus 里的三个程序

*单位换算器 · 四个按钮的计算器 · 收银员*

讲义 · 1INF 班 · 实验课 · 04/11/2026 · 版本 1.0

今天你做三个真正的程序。每个都能马上运行，可以给同学试玩。这里的代码和课堂页面上的完全一样。出错没关系：所有程序员都会出错，专业的也一样。

## 01 怎样运行程序

*示意图（不是截图）：在哪里按、程序出现在哪里。* (schema nel PDF)

1. 按 `Ctrl` + `S` 保存。
2. 按 `F9`，或者菜单下面带三角形的绿色按钮（**Esegui**）。
3. 等几秒钟：下面的 **Messaggi** 窗口里 Lazarus 在生成程序。如果出现红色的行，就是有错误（看每个程序的常见错误）。
4. 你的窗口会出现在 Lazarus **上面**，像真正的程序。看不到？在 Windows 底部的任务栏里找。
5. 试一试程序：在框里写数字，按按钮。
6. 停止：点你窗口右上角红色的 **X**。如果卡住了：在 Lazarus 里按 `Ctrl` + `F2`。
7. 回去修改：代码和窗口都还在。改一改，保存，再按 `F9`。

> **程序在哪里：** 按 `F9` 后，Lazarus 会在项目文件夹（例如 `Documenti\convertitore`）里生成一个和项目同名、以 `.exe` 结尾的文件，例如 `convertitore.exe`。这就是你的程序：双击它，不用 Lazarus 也能运行。看不到的话说明程序没有生成成功：看 Messaggi 窗口。

## 02 三个程序都一样的步骤

这六步每个程序都要做。下面的步骤里会有字母（A、B、C、D、E、F）：看相同字母的图。

1. **A**: 新项目：Progetto → Nuovo progetto… → Applicazione → OK
2. **B**: 保存：在 Documenti 新建文件夹，点两次 Salva
3. **C**: Standard 面板：点组件，再点窗体
4. **D**: Ispettore oggetti：改 Caption 或 Text
5. **E**: 双击按钮：代码打开
6. **F**: F9：程序开始运行

### 要知道的词

| 词 | 作用 | 例子 |
|---|---|---|
| `StrToInt('5')` | 文字变数字（不是数字就会停下） | `'5'` 变成 `5` |
| `StrToIntDef('ab', 0)` | 文字变数字；不行就用 0，不会停 | `'ab'` 变成 `0`；`'7'` 变成 `7` |
| `IntToStr(5000)` | 数字变文字 | `5000` 变成 `'5000'` |
| `div` | 不带小数的除法 | `17 div 5 = 3` |
| `mod` | 剩下的 | `17 mod 5 = 2` |
| `+` con testi | 连接两段文字 | `'Ciao ' + 'Anna'` |

> **文字和数字：** `'5' + '3'` 得 `'53'`（两段文字粘在一起）。`5 + 3` 得 `8`（两个数字）。所以总要转换：先把文字变数字来计算，再把数字变文字来显示结果。

## 03 程序 1：单位换算器

**有什么用。** 写一个数字，按一个按钮，程序就把它换算：公里变米、小时变分钟、欧元变分、摄氏变华氏、分钟变小时和分钟。**运行成功时**你会看到：

*示意图：做好的换算器。* (schema nel PDF)

*带编号的示意图：红色数字对应下面的表格。* (schema nel PDF)

| N. | Name | 类型 | 要改什么 |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` 清空 |
| 2 | `Label1` | TLabel | 不用改（代码会填） |
| 3 | `Button1` | TButton | `Caption` = `Km in metri` |
| 4 | `Button2` | TButton | `Caption` = `Ore in minuti` |
| 5 | `Button3` | TButton | `Caption` = `Euro in centesimi` |
| 6 | `Button4` | TButton | `Caption` = `Celsius in Fahrenheit` |
| 7 | `Button5` | TButton | `Caption` = `Minuti in ore e minuti` |

### 步骤，每行一个动作

1. [A] 打开 Lazarus：菜单 `Progetto`，`Nuovo progetto…`，`Applicazione`，`OK`。
2. [B] 菜单 `Progetto`，`Salva progetto con nome…`：在 `Documenti` 里新建文件夹 `convertitore`，文件名写 `convertitore`，点 `Salva`（再点一次 `Salva` 保存 `unit1.pas`）。
3. [C] `Standard` 面板：点 `TEdit`，再点窗体上方。
4. [C] 点 `TLabel`，再点输入框下面的窗体。
5. [C] 点 `TButton`，再点标签下面的窗体。
6. [D] 点 `Button1`。在 Ispettore oggetti 的 `Caption` 里写：`Km in metri`。
7. [D] 点 `Edit1`。在 Ispettore 里删掉 `Text` 的内容：要留空。
8. [E] 双击 `Button1`：代码打开。
9. `begin` 和 `end;` 的开头 Lazarus 已经写好了。把处理程序补完整（完整代码在下面）：

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

10. [F] 按 `F9`，在框里写 `5`，按按钮。

> **马上成功（5 分钟）：** 写 `5`，应该出现 **5000 metri**。成功了！你做出了第一个程序。

**另外四个按钮：** 方法一样（放按钮，写 `Caption`，双击，抄代码）。只有计算部分不同。

小时变分钟（`Button2`）。试 `2`：**120 minuti**。

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

欧元变分（`Button3`）。试 `3`：**300 centesimi**。

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

摄氏变华氏（`Button4`）。`c * 9 div 5 + 32`。试 `100`：**212**。

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

分钟变小时和分钟（`Button5`）：`div` 得整小时，`mod` 得剩下的。试 `135`：**2 小时 15 分钟**。

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

### 新指令的作用

`StrToInt(Edit1.Text)` 读取输入框里的文字并变成数字：写 `5` 就得到 `5`。`IntToStr(metri)` 相反：`5000` 变成文字 `'5000'`，才能放进标签。`135 div 60` = `2`，`135 mod 60` = `15`。

### 最常见的 3 个错误

| 你看到什么 | 意思是 | 解决办法 |
|---|---|---|
| `Identifier not found "Edit1"` | 缺少组件，或者代码里的名字和 Ispettore 里的 `Name` 不一样。 | 检查窗体上有没有 `Edit1`、`Label1`、`Button1`。名字要写得完全一样（包括大小写）。 |
| `Incompatible types` | 在需要数字的地方放了文字，或在需要文字的地方放了数字。 | 计算用 `StrToInt(...)`。写进标签用 `IntToStr(...)`。 |
| 程序关闭，或弹出写着 `"5a" is an invalid integer` 的窗口 | 输入框里的数字写得不对：有字母、空格、逗号，或者是空的。 | 只写整数数字（写 `5`，不要写 `5,5` 或 `5 km`）。然后再按按钮。 |

> **做成你自己的：** 改按钮上的字、窗口标题（Form 的 `Caption`）和颜色（`Color`）。再加一个你喜欢的换算按钮（比如米变厘米：`* 100`）。

## 04 程序 2：四个按钮的计算器

**有什么用。** 写两个数字，按 `+`、`-`、`*` 或 `/`，程序写出带结果的句子。**运行成功时**你会看到：

*示意图：做好的计算器。* (schema nel PDF)

*带编号的示意图：红色数字对应下面的表格。* (schema nel PDF)

| N. | Name | 类型 | 要改什么 |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` 清空 |
| 2 | `Edit2` | TEdit | `Text` 清空 |
| 3 | `Button1` | TButton | `Caption` = `+` |
| 4 | `Button2` | TButton | `Caption` = `-` |
| 5 | `Button3` | TButton | `Caption` = `*` |
| 6 | `Button4` | TButton | `Caption` = `/` |
| 7 | `Label1` | TLabel | 不用改（代码会填） |

### 步骤，每行一个动作

1. [A] 菜单 `Progetto`，`Nuovo progetto…`，`Applicazione`，`OK`。
2. [B] `Progetto`，`Salva progetto con nome…`：在 `Documenti` 里建文件夹 `calcolatrice`，文件名 `calcolatrice`，点两次 `Salva`。
3. [C] `Standard` 面板：点 `TEdit`，再点窗体。然后在第一个下面再放一个 `TEdit`。
4. [C] 点 `TButton`，再点窗体。重复四次，排成一行。
5. [C] 点 `TLabel`，再点按钮下面的窗体。
6. [D] 依次点每个按钮，写 `Caption`：`+`、`-`、`*`、`/`。
7. [D] 点 `Edit1`，清空 `Text`。`Edit2` 也一样。
8. [E] 双击 `+` 按钮（`Button1`）。把处理程序补成这样：

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

9. [F] 按 `F9`，写 `7` 和 `5`，按 `+`。

> **马上成功（5 分钟）：** 应该出现句子 **7 più 5 fa 12**。

**另外三个按钮：** 依次双击 `-`、`*`、`/` 并抄代码。只改运算和单词。试 `7` 和 `5`：**7 meno 5 fa 2**，**7 per 5 fa 35**。

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

`/` 按钮用 `if` 检查零：不能除以零。试 `8` 和 `0`：**Non si può dividere per zero**。试 `8` 和 `2`：**8 diviso 2 fa 4**。

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

### 新指令的作用

`StrToIntDef(Edit1.Text, 0)` 读取数字；框是空的或有字母时用 `0`，不会卡住：`'7'` 得 `7`，`'ab'` 得 `0`。`if b = 0 then … else …` 的意思：**如果** b 是零就做第一件事，**否则**做第二件事。`8 div 2` 得 `4`。

### 最常见的 3 个错误

| 你看到什么 | 意思是 | 解决办法 |
|---|---|---|
| `Identifier not found "Edit2"` | 缺少第二个 `Edit`，或名字不一样。 | 在窗体上放第二个 `TEdit`，检查它叫 `Edit2`。 |
| `Incompatible types` | 文字和数字搞混：你写了 `Label1.Caption := a + b`。 | 写进标签需要文字：`IntToStr(a + b)`。 |
| 程序关闭并出现 `Division by zero` | 你除以了零，而且缺少 `if b = 0` 的检查。 | 照抄 `/` 按钮带 `if` 的代码。试 `8` 和 `0`。 |

> **做成你自己的：** 改窗口标题、颜色和句子（比如把 `più` 改成 `sommato a`）。

## 05 程序 3：收银员

**有什么用。** 写顾客名字、价格和给的钱：程序算出找零，说明需要几张钞票和几枚硬币，并写出带名字的小票。**运行成功时**你会看到：

*示意图：做好的小票。* (schema nel PDF)

*带编号的示意图：红色数字对应下面的表格。* (schema nel PDF)

| N. | Name | 类型 | 用途 |
|---|---|---|---|
| 1 | `Edit1` | TEdit | 顾客名字（`Text` 清空） |
| 2 | `Edit2` | TEdit | 价格（`Text` 清空） |
| 3 | `Edit3` | TEdit | 给的钱（`Text` 清空） |
| 4 | `Button1` | TButton | `Caption` = `Calcola il resto` |
| 5 | `Label1` | TLabel | 写找零 |
| 6 | `Memo1` | TMemo | 小票（内容清空） |

### 步骤，每行一个动作

1. [A] 菜单 `Progetto`，`Nuovo progetto…`，`Applicazione`，`OK`。
2. [B] `Progetto`，`Salva progetto con nome…`：在 `Documenti` 里建文件夹 `cassiere`，文件名 `cassiere`，点两次 `Salva`。
3. [C] `Standard` 面板：放三次 `TEdit`（点组件，再点窗体），一个在另一个下面。
4. [C] 输入框下面放一个 `TButton`，按钮旁边放一个 `TLabel`。
5. [C] 窗体底部放一个大的 `TMemo`。
6. [D] 点 `Button1`，`Caption` 写 `Calcola il resto`。
7. [D] 清空 `Edit1`、`Edit2`、`Edit3` 的 `Text`。
8. [D] 点 `Memo1`：在 Ispettore 里 `Lines` 的右边点三个点，删掉文字，点 `OK`。
9. [E] 双击按钮。要**马上成功**，先只写找零（给的钱减价格）：

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

10. [F] 按 `F9`，价格写 `13`，给的钱写 `50`，按按钮。

> **马上成功（5 分钟）：** 应该出现 **Resto: 37 euro**。

11. 停止程序（红色 `X`）。删掉 `begin` 和 `end;` 之间的所有代码，换成下面的完整代码：加上钞票、硬币和小票。

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

12. [F] 按 `F9`，写 `Maria`、`13`、`50`，按按钮。

> **预期结果：** Memo 里出现小票：`SCONTRINO`、`Cliente: Maria`、`Prezzo: 13 euro`、`Dati: 50 euro`、`Resto: 37 euro`、`3 banconote da 10, 1 da 5`、`1 monete da 2, 0 da 1`。

### 新指令的作用

找零 `37`：`37 div 10` = `3` 张 10，`37 mod 10` = `7` 剩下。`7 div 5` = `1` 张 5，剩 `2`。`2 div 2` = `1` 枚 2，剩 `0`。`'Cliente: ' + Edit1.Text` 把两段文字连起来。`Memo1.Lines.Add(...)` 给小票加一行，`Memo1.Clear` 在写之前清空小票。

### 最常见的 3 个错误

| 你看到什么 | 意思是 | 解决办法 |
|---|---|---|
| `Identifier not found "Memo1"` | 缺少 `TMemo`，或名字不同。 | 把 `TMemo` 放到窗体上，检查 `Name` 是 `Memo1`。`Edit1`、`Edit2`、`Edit3` 也一样。 |
| `Incompatible types` | 文字和数字搞混：你写了 `Memo1.Lines.Add(resto)`，没有转换。 | 在 `Add(...)` 里写 `IntToStr(resto)`。 |
| 找零或钞票数很奇怪（负数或 `0`） | 给的钱比价格少，或者用逗号写了分（`13,50` 会算成 `0`）。 | 只写整欧元（`13`）。给的钱至少要和价格一样多。 |

> **做成你自己的：** 给你的商店起个名字，写在小票最上面：在 `Memo1.Clear;` 后面加上 `Memo1.Lines.Add('NEGOZIO DI ...');`，名字自己定。

## 06 三个程序总结

| 程序 | 组件 | 新东西 | 试一试 | 应得到 |
|---|---|---|---|---|
| 1. 换算器 | `Edit1`, `Label1`, 5 `Button` | `StrToInt`, `IntToStr`, `div`, `mod` | `5` | `5000 metri` |
| 2. 计算器 | `Edit1`, `Edit2`, 4 `Button`, `Label1` | `StrToIntDef`, `if … else` | `7` e `5` / `8` e `0` | `7 più 5 fa 12` / `Non si può dividere per zero` |
| 3. 收银员 | `Edit1`, `Edit2`, `Edit3`, `Label1`, `Button1`, `Memo1` | `div`, `mod`, `+` sui testi, `Memo1.Lines.Add` | `Maria`, `13`, `50` | `Resto: 37 euro` |

### 抄在本子上

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

然后用自己的话给同学讲讲你最喜欢的程序是做什么的。

你做了三个真正的程序。给同学看看：你的名字就在你的作品上。
