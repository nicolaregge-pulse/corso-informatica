# Object Pascal 和 Java 的比较

为什么用 Object Pascal（Lazarus）学得更快：代码更少，变量不用 “new”，窗口用鼠标画

三年级 · 2026年10月26日 · Versione 1.0

同一个程序用两种语言来写。看看需要几行、要学多少新词：你就会明白为什么我们先用 Lazarus。代码保留英文字母。

## 01 两种语言

**Object Pascal** 是 **Lazarus**（和 Delphi）的语言。**Java** 在公司和 Android 应用里用得很多。

|  | Object Pascal (Lazarus) | Java |
|---|---|---|
| 怎样变成程序 | 编译：变成一个 .exe 文件 | 先编译成 “bytecode”，再由 Java 虚拟机解释执行 |
| 电脑上需要什么 | 什么都不需要：.exe 自己就能运行 | 要安装 Java（虚拟机） |
| 窗口 | 用鼠标画 | 用代码写 |

## 02 Hello World

**Object Pascal**

```
begin
  writeln('Hello World');
end.
```

**Java**

```
public class Ciao {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

在 Java 里，只写一句话就需要一个 **class** 和 **main** 方法，还有 **public**、**static**、**void**、**String[] args** 这些词。在 Object Pascal 里只要 **begin** 和 **end**。

## 03 变量：不用 “new”

在 Object Pascal 里，变量在 **var** 部分写上名字和类型，然后马上就能用。数组（array）也已经准备好了。

**Object Pascal**

```
var
  nome: string;
  eta: integer;
  voti: array[1..5] of integer;
begin
  nome := 'Ali';
  eta := 16;
  voti[1] := 8;
  readln(nome);        // leggo dalla tastiera
end.
```

在 Java 里，简单类型（int、double）没问题，但数组或从键盘读取，就必须用 **new** 来**创建一个对象**。

**Java**

```
String nome = "Ali";
int eta = 16;
int[] voti = new int[5];          // serve new
voti[0] = 8;                       // si parte da 0
Scanner tastiera = new Scanner(System.in);   // serve new
nome = tastiera.nextLine();
```

> **要知道.** Java 的数组从 0 开始；Pascal 由你决定从哪里开始（这里从 1）。在 Java 里每个 “大” 东西都要先用 new 创建才能用。

## 04 有一个按钮的窗口

用 Lazarus，把按钮拖到窗体（Form）上，双击，写**一行**：

**Object Pascal (Lazarus)**

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello World');
end;
```

在 Java（Swing）里，窗口和按钮全部要用代码写，每一个都要用 **new** 创建：

**Java**

```
JFrame finestra = new JFrame("Ciao");
JButton bottone = new JButton("Premi");
bottone.addActionListener(e ->
    JOptionPane.showMessageDialog(null, "Hello World"));
finestra.add(bottone);
finestra.setSize(300, 200);
finestra.setVisible(true);
```

## 05 总结

| 什么 | Object Pascal | Java |
|---|---|---|
| Hello World | begin…end 里一行 | 5 行，有 class 和 main |
| 变量和数组 | 在 var 部分，马上能用 | 数组和很多对象要用 new |
| 从键盘读取 | readln | new Scanner(System.in) |
| 窗口和按钮 | 用鼠标画 | 用代码和 new 写 |
| 做好的程序 | 一个到处都能运行的 .exe | 需要安装 Java |

## 06 说实话

在 Object Pascal 里，比较复杂的**类**也要先创建（**Create**），用完再释放（**Free**）。Java 会自己释放内存。而且 Java 在工作中用得非常多：所以知道它是好的。

**Object Pascal**

```
var lista: TStringList;
begin
  lista := TStringList.Create;   // anche qui si crea
  lista.Add('Ali');
  lista.Free;                    // e si libera
end;
```

> **要知道.** 但是要学编程、马上看到结果，用 Lazarus 的 Object Pascal 是最简单的路：要学的词更少，窗口用鼠标画，.exe 到处都能运行。

## 07 你来试试

1. Hello World 在 Object Pascal 里要几行？在 Java 里要几行？
2. 在 Java 里，创建一个有 5 个数字的数组需要什么？
3. 为什么用 Lazarus 做的程序不用安装任何东西就能在每台 Windows 电脑上运行？

### 答案

1. Object Pascal：1 行（在 begin…end 里）。Java：5 行，有 class 和 main。
2. 要用 new：int[] voti = new int[5];
3. 因为它被编译成 .exe 文件；而 Java 需要安装它的虚拟机。
