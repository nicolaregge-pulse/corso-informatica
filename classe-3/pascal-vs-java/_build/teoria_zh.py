from codici import *
L = dict(lang='zh', dir='ltr', file='20261026_Classe-3-Teoria_v%s_Object-Pascal-e-Java', titolo='Object Pascal 和 Java 的比较',
         sotto='为什么用 Object Pascal（Lazarus）学得更快：代码更少，变量不用 “new”，窗口用鼠标画',
         classe='三年级 · 2026年10月26日', es='例子', nota='要知道', sol='答案', foto='', pag='页',
         intro='同一个程序用两种语言来写。看看需要几行、要学多少新词：你就会明白为什么我们先用 Lazarus。代码保留英文字母。')
S = [
('01 两种语言', [
 ('p', '<b>Object Pascal</b> 是 <b>Lazarus</b>（和 Delphi）的语言。<b>Java</b> 在公司和 Android 应用里用得很多。'),
 ('tab', [['', 'Object Pascal (Lazarus)', 'Java'], ['怎样变成程序', '编译：变成一个 .exe 文件', '先编译成 “bytecode”，再由 Java 虚拟机解释执行'], ['电脑上需要什么', '什么都不需要：.exe 自己就能运行', '要安装 Java（虚拟机）'], ['窗口', '用鼠标画', '用代码写']])]),
('02 Hello World', [
 ('code', 'Object Pascal', HP), ('code', 'Java', HJ),
 ('p', '在 Java 里，只写一句话就需要一个 <b>class</b> 和 <b>main</b> 方法，还有 <b>public</b>、<b>static</b>、<b>void</b>、<b>String[] args</b> 这些词。在 Object Pascal 里只要 <b>begin</b> 和 <b>end</b>。')]),
('03 变量：不用 “new”', [
 ('p', '在 Object Pascal 里，变量在 <b>var</b> 部分写上名字和类型，然后马上就能用。数组（array）也已经准备好了。'),
 ('code', 'Object Pascal', VP),
 ('p', '在 Java 里，简单类型（int、double）没问题，但数组或从键盘读取，就必须用 <b>new</b> 来<b>创建一个对象</b>。'),
 ('code', 'Java', VJ),
 ('nota', 'Java 的数组从 0 开始；Pascal 由你决定从哪里开始（这里从 1）。在 Java 里每个 “大” 东西都要先用 new 创建才能用。')]),
('04 有一个按钮的窗口', [
 ('p', '用 Lazarus，把按钮拖到窗体（Form）上，双击，写<b>一行</b>：'),
 ('code', 'Object Pascal (Lazarus)', FP),
 ('p', '在 Java（Swing）里，窗口和按钮全部要用代码写，每一个都要用 <b>new</b> 创建：'),
 ('code', 'Java', FJ)]),
('05 总结', [
 ('tab', [['什么', 'Object Pascal', 'Java'], ['Hello World', 'begin…end 里一行', '5 行，有 class 和 main'], ['变量和数组', '在 var 部分，马上能用', '数组和很多对象要用 new'], ['从键盘读取', 'readln', 'new Scanner(System.in)'], ['窗口和按钮', '用鼠标画', '用代码和 new 写'], ['做好的程序', '一个到处都能运行的 .exe', '需要安装 Java']])]),
('06 说实话', [
 ('p', '在 Object Pascal 里，比较复杂的<b>类</b>也要先创建（<b>Create</b>），用完再释放（<b>Free</b>）。Java 会自己释放内存。而且 Java 在工作中用得非常多：所以知道它是好的。'),
 ('code', 'Object Pascal', CP),
 ('nota', '但是要学编程、马上看到结果，用 Lazarus 的 Object Pascal 是最简单的路：要学的词更少，窗口用鼠标画，.exe 到处都能运行。')]),
('07 你来试试', [
 ('ol', ['Hello World 在 Object Pascal 里要几行？在 Java 里要几行？', '在 Java 里，创建一个有 5 个数字的数组需要什么？', '为什么用 Lazarus 做的程序不用安装任何东西就能在每台 Windows 电脑上运行？']),
 ('sol', ['Object Pascal：1 行（在 begin…end 里）。Java：5 行，有 class 和 main。', '要用 new：int[] voti = new int[5];', '因为它被编译成 .exe 文件；而 Java 需要安装它的虚拟机。'])]),
]
