# Lazarus：窗口、组件、点击

**Versione 1.0** - 04/11/2026
*复习讲义 · 1INF 班 · 04/11/2026 · 实验课*

这份讲义帮你复习已经会的东西：Lazarus 的窗口长什么样，程序里放的零件（按钮、输入框、标签），以及点击时会发生什么。最后有一个 5 分钟的练习，马上就能成功。做错了没关系：所有程序员都会，连专业人士也一样。

## 1. Lazarus 地图
*示意图（不是照片）：你每次都会用到的 Lazarus 各部分。* (schema nel PDF)

1. **命令栏。**在最上面：菜单（File、Progetto、Esegui）和带三角形的绿色按钮 **Esegui**。按 `F9` 也能运行程序。
2. **组件面板（Palette）。**菜单下面一排现成的零件。在 **Standard** 标签里有按钮、输入框、标签。先点零件，再点窗口，零件就放上去了。
3. **对象检查器（Ispettore oggetti）。**在左边。显示选中的零件。**Proprietà**（属性）标签说明它的样子（文字、名字、大小）。**Eventi**（事件）标签说明它对什么有反应（比如点击）。
4. **Form1。**中间是你的程序窗口，像一张纸，你把零件放在上面。
5. **代码编辑器。**在右边（或在窗口后面）。在这里写指令。按 `F12` 在窗口和代码之间切换。
6. **Messaggi 窗口。**在下面。出错时会告诉你哪一行错了。

找不到某个窗口？点菜单 **Visualizza** 再打开。你不会弄坏任何东西。

## 2. 我们用过的组件
**组件**是现成的零件，像积木。从面板拿出来放进窗口。组件的类型名字以字母 **T** 开头。

| 组件 | 用来做什么 | 要记住的属性 |
|---|---|---|
| **TButton**（按钮） | 用来点击，让你的代码开始运行。 | `Caption` = 按钮上的字 ; `Name` = 代码里用的名字（Button1） |
| **TEdit**（输入框） | 用户在里面写（名字、数字）。 | `Text` = 里面写的内容 ; `Name` = Edit1 |
| **TLabel**（标签） | 显示一行字，程序可以改它。 | `Caption` = 看到的字 ; `Name` = Label1 |
| **TMemo**（多行文本） | 显示很多行（收银员的小票）。 | `Lines` = 各行 ; `Name` = Memo1 |

在单位换算器里：在输入框（TEdit）写 **5**，点按钮（TButton），标签（TLabel）显示 **5000 metri**。

## 3. OnClick 事件：让代码开始运行的点击
**事件**就是发生的事情，比如一次点击。Lazarus 等着点击，点击一来，就运行你的代码。你只要写它该做什么。

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  Label1.Caption := 'Ciao!';
end;
```

怎么做：在窗口里**双击按钮**。Lazarus 自己写好 `procedure`、`begin`、`end;`。你只写中间那一行。这样读：**“标签里的字变成 Ciao!”**。符号 `:=` 的意思是“变成”。`;` 结束这一行，像句子最后的句号。

最常见的错误：少了 `;`，把 `:=` 写成 `=`，或者少了一个 `'`。

## 4. 桥梁：从你已经知道的到 Lazarus
前面几节课你已经学了很多。这张表把它们放在一起。

| 你已经知道的 | 在 Lazarus 里叫 | 例子 |
|---|---|---|
| 程序的窗口 | **Form**（Form1） | 有按钮的窗口 |
| 窗口里的零件 | **Componenti**（组件） | TButton, TEdit, TLabel |
| 零件的特点 | **Proprietà**（属性） | Caption, Text, Name |
| 发生的事情 | **Evento**（事件） | OnClick（点击） |

### 小词典

| 词 | 意思 |
|---|---|
| Caption | 按钮或标签上**看得见**的字 |
| Text | 输入框**里面写的**字 |
| Name | 代码用的**内部**名字（Button1, Edit1） |
| Form | 程序的窗口 |
| Event | 发生的事情，比如点击 |
| Run (Esegui) | 运行程序（按 F9） |

## 5. 练习：5 分钟马上成功
一个按钮，点击后改变标签上的字。几乎不可能做错。

1. 打开 Lazarus。菜单 **Progetto**，再点 **Nuovo progetto**，再点 **Applicazione**。马上保存到 **Documenti\Lazarus** 里你自己的文件夹。
2. 在面板的 **Standard** 标签里点零件 **TButton**，再点窗口 Form1。
3. 点零件 **TLabel**，再点窗口里按钮的下面。
4. 点按钮。在对象检查器的 Proprietà 标签里，把 `Caption` 改成 **Premimi**。
5. **双击按钮**，代码打开了。在 `begin` 和 `end;` 中间自己抄下面这一行。
6. 按 `Ctrl` + `S` 保存，再按 `F9`。点按钮：字变了。成功！你做出了自己的程序。

```
Label1.Caption := 'Ciao, funziona!';
```

### 做成你自己的

1. 把 `Ciao, funziona!` 换成你自己的一句话（你的名字、你的球队、一句问候）。
2. 点 Form1，改属性 `Color`：选你最喜欢的颜色。
3. 把按钮的 `Caption` 改成你自己的词。让同学试一试你的程序。

### 抄在本子上

把这几行抄在本子上，然后用自己的话讲给同学听。

```
Form = la finestra
Componente = un pezzo (TButton, TEdit, TLabel)
Proprietà = come è fatto (Caption, Text, Name)
Evento = cosa succede (OnClick = il clic)
clic -> OnClick -> il mio codice
F9 = Esegui
```

## 6. 复习：给你的 5 个问题
先在本子上回答，再对照答案。

1. 点击用的那个零件叫什么？
2. 哪个属性改变按钮或标签上的字？
3. 按哪个键运行程序？
4. 双击按钮会怎样？
5. `Label1.Caption := 'Ciao';` 里的 `:=` 是什么意思？

### 答案

1. TButton（按钮）。
2. 属性 Caption。
3. F9 键（或绿色的 Esegui 按钮）。
4. 生成点击的过程（OnClick），并带你到代码里，写它该做什么。
5. 意思是“变成”：标签上的字变成 Ciao。

太棒了！这样复习就是记住东西的好办法。
