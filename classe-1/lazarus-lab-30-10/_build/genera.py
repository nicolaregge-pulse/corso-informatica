#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1INF, laboratorio di venerdì 30/10/2026 (11-14): tre percorsi, tre esercitazioni Lazarus, tre codici.
ANTEPRIMA per il prof: le pagine stanno in docs/anteprima/1inf-lab-30-10/ e non sono collegate da nessuna pagina dei ragazzi.

Scrive:
  docs/anteprima/1inf-lab-30-10/modulo-1.html, modulo-2.html, modulo-3.html (+ i sorgenti .md)
  docs/verifica/banche/1inf-lab3010-tipi.js   (teoria String e Integer + quiz: piano B del quiz, motore del corso)
  docs/verifica/stato/1inf-lab3010-tipi.json  (verifica CHIUSA: nessuno la fa finché il prof non la apre)
  docs/anteprima/1inf-lab-30-10/quiz-moduli.json (le stesse domande per il comando forms.crea_quiz: piano A del quiz)
Uso: python3 classe-1/lazarus-lab-30-10/_build/genera.py
"""
import html, json, os

PUB = '/home/user/corso-informatica'
OUT = PUB + '/docs/anteprima/1inf-lab-30-10'
BANCA_ID = '1inf-lab3010-tipi'
VERIFICA = '../../verifica/?b=' + BANCA_ID


def T(it, ar, zh): return (it, ar, zh)


# ------------------------------------------------------------------ pezzi comuni
def progetto(cartella):
    return [
        (T('Progetto nuovo', 'مشروع جديد', '新项目'),
         T('In alto clicca il menu <b>Progetto</b> → <b>Nuovo progetto…</b> → a sinistra <b>Applicazione</b> → <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.',
           'في الأعلى انقر القائمة Progetto ← Nuovo progetto… ← على اليسار Applicazione ← OK. في الوسط تظهر النافذة الفارغة Form1.',
           '点上方菜单 Progetto → Nuovo progetto… → 左边 Applicazione → OK。中间出现空窗口 Form1。'), None),
        (T('Salva subito, nella cartella nuova', 'احفظ فوراً في مجلد جديد', '马上保存到新文件夹'),
         T('Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Nella finestra clicca a sinistra <b>Documenti</b>, poi in alto <b>Nuova cartella</b>. Scrivi il nome qui sotto, premi Invio e fai doppio clic sulla cartella per entrarci.',
           'القائمة Progetto ← Salva progetto con nome…. في النافذة انقر يساراً Documenti ثم في الأعلى Nuova cartella. اكتب الاسم أدناه، اضغط Invio وانقر مرتين على المجلد للدخول.',
           '菜单 Progetto → Salva progetto con nome…。在窗口左边点 Documenti，再点上方 Nuova cartella。写下面的名字，按回车，双击文件夹进去。'), cartella),
        (T('Il nome del progetto', 'اسم المشروع', '项目的名字'),
         T('In basso, nella casella <b>Nome file</b>, scrivi il nome qui sotto e clicca <b>Salva</b>. Lazarus chiede il nome della unit: lascia <code>unit1.pas</code> e clicca <b>Salva</b>. In alto, nel titolo di Lazarus, c\'è scritto <b>' + cartella + '</b>: FATTO!',
           'في الأسفل، في خانة Nome file، اكتب الاسم أدناه وانقر Salva. يسأل Lazarus عن اسم الـ unit: اترك unit1.pas وانقر Salva. في عنوان Lazarus مكتوب ' + cartella + ': تم!',
           '在下面 Nome file 框里写下面的名字，点 Salva。Lazarus 问 unit 的名字：保留 unit1.pas，点 Salva。Lazarus 标题里写着 ' + cartella + '：完成！'), cartella + '.lpi'),
    ]


def consegna_b(n, cartella, compito):
    f_pas, f_png = 'ora%d_unit1.pas' % n, 'ora%d_screenshot.png' % n
    return [
        (T('Lo screenshot del programma che gira', 'لقطة شاشة للبرنامج وهو يعمل', '程序运行时的截图'),
         T('Premi <b>F9</b>: il tuo programma è aperto. Premi insieme <b>Win + Shift + S</b> e con il mouse disegna un rettangolo intorno alla tua finestra. In basso a destra clicca l\'avviso <b>Ritaglio</b>: si apre lo Strumento di cattura. Premi <b>Ctrl + S</b>, a sinistra clicca <b>Documenti</b>, doppio clic sulla cartella <b>' + cartella + '</b>, in <b>Nome file</b> scrivi il nome qui sotto e clicca <b>Salva</b>.',
           'اضغط F9: برنامجك مفتوح. اضغط معاً Win + Shift + S وارسم بالفأرة مستطيلاً حول نافذتك. في الأسفل يميناً انقر الإشعار: تفتح أداة القص. اضغط Ctrl + S، يساراً انقر Documenti، انقر مرتين على المجلد ' + cartella + '، في Nome file اكتب الاسم أدناه وانقر Salva.',
           '按 F9：你的程序打开了。同时按 Win + Shift + S，用鼠标在你的窗口周围画一个方框。点右下角的截图通知：打开截图工具。按 Ctrl + S，左边点 Documenti，双击文件夹 ' + cartella + '，在 Nome file 写下面的名字，点 Salva。'), f_png),
        (T('Trova unit1.pas', 'اعثر على unit1.pas', '找到 unit1.pas'),
         T('Premi <b>Win + E</b> (Esplora file). A sinistra clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>' + cartella + '</b>. In alto clicca <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>: ora vedi le lettere dopo il punto. Il file del tuo codice è <code>unit1.pas</code>.',
           'اضغط Win + E. يساراً انقر Documenti وانقر مرتين على المجلد ' + cartella + '. في الأعلى Visualizza ← Mostra ← Estensioni nomi file: الآن ترى الحروف بعد النقطة. ملف الكود هو unit1.pas.',
           '按 Win + E（文件资源管理器）。左边点 Documenti，双击文件夹 ' + cartella + '。上方点 Visualizza → Mostra → Estensioni nomi file：现在能看到点后面的字母。你的代码文件是 unit1.pas。'), None),
        (T('Fai la copia da consegnare', 'اصنع نسخة للتسليم', '做一个要提交的副本'),
         T('Clicca una volta <code>unit1.pas</code>. Premi <b>Ctrl + C</b> e poi <b>Ctrl + V</b>: compare <code>unit1 - Copia.pas</code>. Cliccala una volta, premi <b>F2</b>, scrivi il nome qui sotto e premi Invio. (L\'originale <code>unit1.pas</code> resta lì: il progetto funziona ancora.)',
           'انقر مرة على unit1.pas. اضغط Ctrl + C ثم Ctrl + V: يظهر unit1 - Copia.pas. انقر عليه مرة، اضغط F2، اكتب الاسم أدناه واضغط Invio. (الأصلي unit1.pas يبقى: المشروع يعمل.)',
           '点一下 unit1.pas。按 Ctrl + C，再按 Ctrl + V：出现 unit1 - Copia.pas。点它一下，按 F2，写下面的名字，按回车。（原来的 unit1.pas 还在：项目照样能用。）'), f_pas),
        (T('Su Classroom: aggiungi i due file', 'على Classroom: أضف الملفين', '在 Classroom：添加两个文件'),
         T('Apri il compito <b>' + compito + '</b> su Classroom. A destra, nel riquadro <b>Il tuo lavoro</b>, clicca <b>+ Aggiungi o crea</b> → <b>File</b> → <b>Sfoglia</b>. Vai in <b>Documenti</b> → <b>' + cartella + '</b>, scegli <code>' + f_pas + '</code> e clicca <b>Apri</b>. Rifai lo stesso per <code>' + f_png + '</code>.',
           'افتح الواجب ' + compito + ' على Classroom. يميناً في مربع Il tuo lavoro انقر + Aggiungi o crea ← File ← Sfoglia. اذهب إلى Documenti ← ' + cartella + '، اختر ' + f_pas + ' وانقر Apri. كرّر نفس الشيء لـ ' + f_png + '.',
           '在 Classroom 打开作业 ' + compito + '。右边 Il tuo lavoro 框里点 + Aggiungi o crea → File → Sfoglia。进入 Documenti → ' + cartella + '，选 ' + f_pas + '，点 Apri。对 ' + f_png + ' 再做一次。'), None),
        (T('Consegna', 'سلّم', '提交'),
         T('Nel riquadro <b>Il tuo lavoro</b> vedi i due file: <code>' + f_pas + '</code> e <code>' + f_png + '</code>. Clicca <b>Consegna</b> e poi ancora <b>Consegna</b>. FATTO!',
           'في مربع Il tuo lavoro ترى الملفين. انقر Consegna ثم Consegna مرة أخرى. تم!',
           '在 Il tuo lavoro 框里看到两个文件。点 Consegna，再点一次 Consegna。完成！'), None),
    ]


# ------------------------------------------------------------------ i tre moduli
M = {}

M[1] = dict(
    n=1, ora='11:00-12:00', cartella='pasticcio', compito='Ora 1 · Il pasticcio dei numeri',
    titolo=T('Ora 1: String e Integer, il pasticcio dei numeri', 'الساعة 1: String و Integer، لخبطة الأرقام', '第 1 节：String 和 Integer，数字的混乱'),
    intro=T('Tutta l\'ora parla di <b>String</b> e <b>Integer</b>. Prima mezz\'ora: la teoria in 6 schede, con una domanda dopo ogni scheda, e il quiz. Poi un programma piccolo che mostra la differenza: il bottone <b>Testo</b> fa <code>\'5\' + \'3\'</code> e compare <b>53</b>; il bottone <b>Numeri</b> fa 5 + 3 con due Integer e compare <b>8</b>.',
            'الساعة كلها عن String و Integer. النصف ساعة الأولى: النظرية في 6 بطاقات، مع سؤال بعد كل بطاقة، ثم الاختبار. بعدها برنامج صغير يُظهر الفرق: الزر Testo يفعل \'5\' + \'3\' فيظهر 53؛ والزر Numeri يفعل 5 + 3 بعددين Integer فيظهر 8.',
            '这一节课都讲 String 和 Integer。前半小时：6 张理论卡片，每张后面一个问题，然后做测验。之后写一个小程序来看区别：Testo 按钮做 \'5\' + \'3\'，出现 53；Numeri 按钮用两个 Integer 做 5 + 3，出现 8。'),
    finestra=dict(titolo='Form1', label='53   8', colore='#0b6e99', bottoni=['Testo', 'Numeri'], edits=[]),
    teoria=True,
    passi=progetto('pasticcio') + [
        (T('La scritta del risultato', 'كتابة النتيجة', '结果的文字'),
         T('Nella palette <b>Standard</b> clicca la <b>A</b> (è la <b>TLabel</b>) e poi clicca nella Form1, in alto: compare <b>Label1</b>. Nell\'Ispettore oggetti cambia <b>Caption</b> in <b>?</b> e, nel piccolo segno a sinistra di <b>Font</b> → <b>Size</b>, scrivi 36.',
           'في لوحة Standard انقر A (هي TLabel) ثم انقر في Form1 في الأعلى: يظهر Label1. في Ispettore oggetti غيّر Caption إلى ? وفي العلامة الصغيرة يسار Font ← Size اكتب 36.',
           '在 Standard 组件面板点 A（就是 TLabel），再点 Form1 上方：出现 Label1。在 Ispettore oggetti 把 Caption 改成 ?，点 Font 左边的小符号 → Size，写 36。'), '36'),
        (T('Due bottoni', 'زرّان', '两个按钮'),
         T('Nella palette clicca il bottone <b>OK</b> (è il <b>TButton</b>) e clicca nella Form1 sotto la scritta: compare <b>Button1</b>, cambia <b>Caption</b> in <b>Testo</b>. Rifai: secondo bottone <b>Button2</b> con Caption <b>Numeri</b>.',
           'في اللوحة انقر الزر OK (هو TButton) وانقر في Form1 تحت الكتابة: يظهر Button1، غيّر Caption إلى Testo. كرّر: زر ثانٍ Button2 بـ Caption هو Numeri.',
           '在组件面板点 OK 按钮（就是 TButton），再点 Form1 文字下面：出现 Button1，把 Caption 改成 Testo。再做一次：第二个按钮 Button2，Caption 写 Numeri。'), None),
        (T('Il bottone Testo: due String', 'الزر Testo: نصّان', 'Testo 按钮：两个 String'),
         T('Fai <b>doppio clic</b> sul bottone <b>Testo</b>: si apre <code>procedure TForm1.Button1Click</code>. Tra <code>begin</code> e <code>end;</code> scrivi la riga. <code>\'5\'</code> e <code>\'3\'</code> hanno gli apici: sono due <b>String</b>.',
           'انقر مرتين على الزر Testo: يفتح procedure TForm1.Button1Click. بين begin و end; اكتب السطر. \'5\' و\'3\' لهما علامات اقتباس: هما نصّان String.',
           '双击 Testo 按钮：打开 procedure TForm1.Button1Click。在 begin 和 end; 之间写这一行。\'5\' 和 \'3\' 有引号：是两个 String。'),
         "  Label1.Caption := '5' + '3';"),
        (T('Fai partire: F9', 'شغّل: F9', '运行：F9'),
         T('Premi <b>F9</b>. Clicca <b>Testo</b>: compare <b>53</b>, non 8! Due String si ATTACCANO. FATTO: prima vittoria. Fallo vedere al compagno.',
           'اضغط F9. انقر Testo: يظهر 53 وليس 8! النصّان يُلصقان. تم: أول فوز. أرِه لزميلك.',
           '按 F9。点 Testo：出现 53，不是 8！两个 String 是连起来。完成：第一个胜利。给同桌看看。'), None),
        (T('Il bottone Numeri: le scatole Integer', 'الزر Numeri: صناديق Integer', 'Numeri 按钮：Integer 盒子'),
         T('Chiudi il programma e premi <b>F12</b>: torni alla Form1. Fai doppio clic su <b>Numeri</b>: si apre <code>Button2Click</code>. Clicca alla fine della riga <code>procedure</code>, premi Invio e scrivi PRIMA di <code>begin</code>: due scatole di tipo <b>Integer</b>.',
           'أغلق البرنامج واضغط F12: تعود إلى Form1. انقر مرتين على Numeri: يفتح Button2Click. انقر في نهاية سطر procedure، اضغط Invio واكتب قبل begin: صندوقان من نوع Integer.',
           '关掉程序，按 F12：回到 Form1。双击 Numeri：打开 Button2Click。点 procedure 那一行的末尾，按回车，在 begin 前面写：两个 Integer 类型的盒子。'),
         "var\n  a, b: Integer;"),
        (T('L\'errore che insegna (succede a tutti)', 'الخطأ الذي يعلّم (يحدث للجميع)', '能教你东西的错误（谁都会遇到）'),
         T('Tra <code>begin</code> e <code>end;</code> scrivi le tre righe e premi <b>F9</b>. In basso, in <b>Messaggi</b>, compare l\'errore <b>Incompatible types</b>: la Caption vuole una <b>String</b> e <code>a + b</code> è un <b>Integer</b>. È normale: lo correggi nel passo dopo.',
           'بين begin و end; اكتب الأسطر الثلاثة واضغط F9. في الأسفل في Messaggi يظهر الخطأ Incompatible types: الـ Caption تريد String و a + b هو Integer. هذا طبيعي: تصحّحه في الخطوة التالية.',
           '在 begin 和 end; 之间写这三行，按 F9。下面 Messaggi 里出现错误 Incompatible types：Caption 要的是 String，a + b 是 Integer。这很正常：下一步就改好。'),
         "  a := 5;\n  b := 3;\n  Label1.Caption := a + b;"),
        (T('Il traduttore IntToStr', 'المترجم IntToStr', '翻译 IntToStr'),
         T('Cambia l\'ultima riga così: <code>IntToStr</code> trasforma il numero 8 nel testo \'8\'. Premi <b>F9</b>. Clicca <b>Testo</b>: 53. Clicca <b>Numeri</b>: 8. FATTO! Lo stesso 5 e 3, due risultati diversi.',
           'غيّر السطر الأخير هكذا: IntToStr يحوّل الرقم 8 إلى النص \'8\'. اضغط F9. انقر Testo: 53. انقر Numeri: 8. تم! نفس 5 و3، ونتيجتان مختلفتان.',
           '把最后一行改成这样：IntToStr 把数字 8 变成文字 \'8\'。按 F9。点 Testo：53。点 Numeri：8。完成！同样的 5 和 3，两个不同的结果。'),
         "  Label1.Caption := IntToStr(a + b);"),
        (T('Fallo tuo: i tuoi numeri', 'اجعله لك: أرقامك', '做成你自己的：你的数字'),
         T('Scegli due numeri tuoi (per esempio la tua età e il tuo numero di maglia): cambiali in tutti e due i bottoni, nel Testo tra apici e nei Numeri senza apici. Prima di F9 scrivi sul quaderno che cosa ti aspetti, poi controlla. Chi ha finito: <b>Button3</b> con Caption <b>Tutti e due</b> e questa riga:',
           'اختر رقمين خاصين بك (مثلاً عمرك ورقم قميصك): غيّرهما في الزرين، في Testo بين علامات اقتباس وفي Numeri بلا علامات. قبل F9 اكتب في الدفتر ما تتوقعه، ثم تحقّق. من أنهى: Button3 بـ Caption هو Tutti e due وهذا السطر:',
           '选两个你自己的数字（比如你的年龄和你的球衣号码）：在两个按钮里都改掉，Testo 里加引号，Numeri 里不加引号。按 F9 之前先在本子上写下你预计的结果，再检查。做完的同学：Button3，Caption 写 Tutti e due，写这一行：'),
         "  Label1.Caption := '5' + '3' + ' oppure ' + IntToStr(5 + 3);"),
    ],
    facile=[
        (T('Leggi le schede 2 e 3 (String e Integer) e rispondi alle loro domande.', 'اقرأ البطاقتين 2 و3 (String و Integer) وأجب عن أسئلتهما.', '读第 2、3 张卡片（String 和 Integer），回答它们的问题。'), None),
        (T('Nella Form1 metti una Label (la A) e un bottone (OK). Doppio clic sul bottone e scrivi la riga.', 'في Form1 ضع Label (الحرف A) وزراً (OK). انقر مرتين على الزر واكتب السطر.', '在 Form1 放一个 Label（A）和一个按钮（OK）。双击按钮，写这一行。'), "  Label1.Caption := '5' + '3';"),
        (T('Premi F9 e clicca il bottone: compare 53. Fai lo screenshot e consegnalo.', 'اضغط F9 وانقر الزر: يظهر 53. خذ لقطة شاشة وسلّمها.', '按 F9，点按钮：出现 53。截图并提交。'), None),
    ],
    indizio=T('Testo: i numeri tra apici sono String e il + li attacca. Numeri: le righe <code>var</code> vanno prima di <code>begin</code>; la Caption vuole una String, quindi <code>IntToStr(a + b)</code>.',
              'Testo: الأرقام بين علامات اقتباس هي String والـ + يلصقها. Numeri: أسطر var قبل begin؛ الـ Caption تريد String، لذلك IntToStr(a + b).',
              'Testo：引号里的数字是 String，+ 把它们连起来。Numeri：var 那几行写在 begin 前面；Caption 要 String，所以写 IntToStr(a + b)。'),
    pezzo="procedure TForm1.Button2Click(Sender: TObject);\nvar\n  a, b: Integer;\nbegin\n  a := 5;\n  b := 3;\n  Label1.Caption := IntToStr(a + b);\nend;",
    spiega=T('Al compagno: perché lo stesso 5 e 3 dà 53 con <b>Testo</b> e 8 con <b>Numeri</b>? A che cosa serve <code>IntToStr</code>?', 'لزميلك: لماذا نفس 5 و3 يعطيان 53 مع Testo و8 مع Numeri؟ لماذا نحتاج IntToStr؟', '对同桌说：为什么同样的 5 和 3，按 Testo 是 53，按 Numeri 是 8？IntToStr 有什么用？'),
    controllo=[
        T('So dire che cos\'è una String e che cos\'è un Integer, con un esempio.', 'أعرف أن أقول ما هي String وما هو Integer، مع مثال.', '我能说出什么是 String、什么是 Integer，并举例。'),
        T('Il mio programma mostra 53 con Testo e 8 con Numeri (o i risultati dei miei numeri).', 'برنامجي يُظهر 53 مع Testo و8 مع Numeri (أو نتائج أرقامي).', '我的程序按 Testo 显示 53，按 Numeri 显示 8（或我自己数字的结果）。'),
        T('So perché Label1.Caption := a + b; dà errore e come si corregge.', 'أعرف لماذا Label1.Caption := a + b; يعطي خطأ وكيف يُصحَّح.', '我知道为什么 Label1.Caption := a + b; 会出错，以及怎么改。'),
        T('Ho consegnato ora1_unit1.pas e ora1_screenshot.png.', 'سلّمت ora1_unit1.pas و ora1_screenshot.png.', '我提交了 ora1_unit1.pas 和 ora1_screenshot.png。'),
    ],
    quaderno="VARIABILE = una scatola con un nome dentro c'e' un valore\nSTRING  = testo, sempre tra apici:   'Ciao'   '5'\nINTEGER = numero intero, senza apici:  5   12   -3\n'5' + '3' = '53'  (attacca)      5 + 3 = 8  (somma)\nLabel1.Caption := a + b;            ERRORE: la Caption vuole una String\nLabel1.Caption := IntToStr(a + b);  giusto: 8\nStrToInt: da String a Integer    '7' -> 7\nIntToStr: da Integer a String     7 -> '7'",
)

M[2] = dict(
    n=2, ora='12:00-13:00', cartella='soprannome', compito='Ora 2 · Il soprannome',
    titolo=T('Ora 2: le caselle e le String, il generatore di soprannomi', 'الساعة 2: الخانات و String، مولّد الألقاب', '第 2 节：输入框和 String，外号生成器'),
    intro=T('Un programma nuovo: scrivi il tuo nome e un animale, premi il bottone e il programma inventa il tuo soprannome: <b>Ahmed detto Leone!</b> Tutto quello che c\'è in una casella è una <b>String</b>.',
            'برنامج جديد: تكتب اسمك وحيواناً، تضغط الزر فيخترع البرنامج لقبك: Ahmed detto Leone! كل ما في الخانة هو String.',
            '一个新程序：写你的名字和一种动物，按按钮，程序给你编一个外号：Ahmed detto Leone！输入框里的一切都是 String。'),
    finestra=dict(titolo='Form1', label='Ahmed detto Leone!', colore='#6e40c9', bottoni=['Crea il soprannome', 'Cancella'], edits=['Ahmed', 'Leone']),
    ripasso=T('<b>Ripasso in 1 minuto.</b> Una <b>String</b> è testo: sta tra apici, <code>\'Ciao\'</code>. Il <code>+</code> attacca due String: <code>\'Ciao \' + \'Ahmed\'</code> = <code>\'Ciao Ahmed\'</code>. Quello che l\'utente scrive in <b>Edit1</b> si legge con <code>Edit1.Text</code>, ed è sempre una String. Una <b>variabile</b> è una scatola con un nome: <code>var nome: String;</code> prepara la scatola <i>nome</i> per il testo.',
              'مراجعة في دقيقة. String هي نص: بين علامتي اقتباس \'Ciao\'. علامة + تلصق نصين: \'Ciao \' + \'Ahmed\' = \'Ciao Ahmed\'. ما يكتبه المستخدم في Edit1 يُقرأ بـ Edit1.Text وهو دائماً String. المتغير صندوق له اسم: var nome: String; يجهّز الصندوق nome للنص.',
              '1 分钟复习。String 是文字：放在单引号里 \'Ciao\'。+ 把两个 String 连起来：\'Ciao \' + \'Ahmed\' = \'Ciao Ahmed\'。用户在 Edit1 里写的东西用 Edit1.Text 读取，它永远是 String。变量是一个有名字的盒子：var nome: String; 准备一个叫 nome 的盒子装文字。'),
    passi=progetto('soprannome') + [
        (T('La casella del nome', 'خانة الاسم', '名字的输入框'),
         T('Nella palette <b>Standard</b> clicca la casella con <b>abc</b> (è la <b>TEdit</b>) e clicca nella Form1, in alto: compare <b>Edit1</b>. Nell\'Ispettore oggetti trova <b>Text</b> e cancella la scritta: la casella resta vuota.',
           'في لوحة Standard انقر الخانة التي فيها abc (هي TEdit) وانقر في Form1 في الأعلى: يظهر Edit1. في Ispettore oggetti ابحث عن Text وامسح الكتابة: تبقى الخانة فارغة.',
           '在 Standard 组件面板点带 abc 的输入框（就是 TEdit），再点 Form1 上方：出现 Edit1。在 Ispettore oggetti 找到 Text，删掉文字：输入框变空。'), None),
        (T('Il suggerimento grigio', 'التلميح الرمادي', '灰色提示'),
         T('Sempre per Edit1, nell\'Ispettore oggetti trova <b>TextHint</b> e scrivi il testo qui sotto. Quando la casella è vuota, si vede in grigio.',
           'لـ Edit1 أيضاً، في Ispettore oggetti ابحث عن TextHint واكتب النص أدناه. عندما تكون الخانة فارغة يظهر بالرمادي.',
           '还是 Edit1，在 Ispettore oggetti 找到 TextHint，写下面的文字。输入框空的时候，它显示成灰色。'), 'Il tuo nome'),
        (T('La casella dell\'animale', 'خانة الحيوان', '动物的输入框'),
         T('Metti una seconda TEdit sotto la prima: compare <b>Edit2</b>. Cancella il suo <b>Text</b> e in <b>TextHint</b> scrivi:',
           'ضع TEdit ثانية تحت الأولى: يظهر Edit2. امسح Text الخاص بها وفي TextHint اكتب:',
           '在第一个下面再放一个 TEdit：出现 Edit2。删掉它的 Text，在 TextHint 里写：'), 'Un animale'),
        (T('Il bottone', 'الزر', '按钮'),
         T('Metti un <b>TButton</b> (il bottone OK) sotto le caselle: compare <b>Button1</b>. Nell\'Ispettore oggetti cambia <b>Caption</b> in:',
           'ضع TButton (الزر OK) تحت الخانات: يظهر Button1. في Ispettore oggetti غيّر Caption إلى:',
           '在输入框下面放一个 TButton（OK 按钮）：出现 Button1。在 Ispettore oggetti 把 Caption 改成：'), 'Crea il soprannome'),
        (T('La scritta del risultato', 'كتابة النتيجة', '结果的文字'),
         T('Metti una <b>TLabel</b> (la A) sotto il bottone: compare <b>Label1</b>. Cambia <b>Caption</b> in tre puntini e, in <b>Font</b> → <b>Size</b>, scrivi 24.',
           'ضع TLabel (الحرف A) تحت الزر: يظهر Label1. غيّر Caption إلى ثلاث نقاط وفي Font ← Size اكتب 24.',
           '在按钮下面放一个 TLabel（A）：出现 Label1。把 Caption 改成三个点，在 Font → Size 里写 24。'), '...'),
        (T('Le scatole per il testo', 'الصناديق للنص', '装文字的盒子'),
         T('Fai doppio clic sul bottone: si apre <code>procedure TForm1.Button1Click</code>. Clicca alla fine di quella riga, premi Invio e scrivi le tre righe <b>prima</b> di <code>begin</code>. Sono due scatole (variabili) di tipo <b>String</b>.',
           'انقر مرتين على الزر: يفتح procedure TForm1.Button1Click. انقر في نهاية ذلك السطر، اضغط Invio واكتب الأسطر الثلاثة قبل begin. هما صندوقان (متغيران) من نوع String.',
           '双击按钮：打开 procedure TForm1.Button1Click。点那一行的末尾，按回车，在 begin 前面写这三行。这是两个 String 类型的盒子（变量）。'),
         "var\n  nome: String;\n  animale: String;"),
        (T('Il codice del soprannome', 'كود اللقب', '外号的代码'),
         T('Tra <code>begin</code> e <code>end;</code> scrivi le tre righe. Prima metti il testo delle caselle nelle scatole, poi attacchi tutto con <code>+</code>. Attenzione agli spazi dentro <code>\' detto \'</code>.',
           'بين begin و end; اكتب الأسطر الثلاثة. أولاً تضع نص الخانات في الصناديق، ثم تلصق كل شيء بـ +. انتبه للمسافات داخل \' detto \'.',
           '在 begin 和 end; 之间写这三行。先把输入框里的文字放进盒子，再用 + 全部连起来。注意 \' detto \' 里面的空格。'),
         "  nome := Edit1.Text;\n  animale := Edit2.Text;\n  Label1.Caption := nome + ' detto ' + animale + '!';"),
        (T('Fai partire: F9', 'شغّل: F9', '运行：F9'),
         T('Premi <b>F9</b>. Scrivi il tuo nome e un animale, clicca <b>Crea il soprannome</b>: compare per esempio <b>Ahmed detto Leone!</b> FATTO! Fallo provare al compagno con il suo nome.',
           'اضغط F9. اكتب اسمك وحيواناً وانقر Crea il soprannome: يظهر مثلاً Ahmed detto Leone! تم! دع زميلك يجرّب باسمه.',
           '按 F9。写你的名字和一种动物，点 Crea il soprannome：出现比如 Ahmed detto Leone！完成！让同桌用他的名字试试。'), None),
        (T('La trappola degli apici', 'فخ علامات الاقتباس', '引号的陷阱'),
         T('Chiudi il programma. Nell\'ultima riga metti gli apici intorno a nome: <code>\'nome\'</code>. Premi F9 e prova: compare <b>nome detto Leone!</b> Perché? Con gli apici è la PAROLA nome, senza apici è la SCATOLA nome. Togli gli apici.',
           'أغلق البرنامج. في السطر الأخير ضع علامتي اقتباس حول nome: \'nome\'. اضغط F9 وجرّب: يظهر nome detto Leone! لماذا؟ مع علامات الاقتباس هي الكلمة nome، وبدونها هي الصندوق nome. أزل علامات الاقتباس.',
           '关掉程序。在最后一行给 nome 加上引号：\'nome\'。按 F9 试试：出现 nome detto Leone！为什么？有引号是“nome”这个词，没有引号是叫 nome 的盒子。把引号去掉。'),
         "  Label1.Caption := 'nome' + ' detto ' + animale + '!';"),
        (T('Fallo tuo: la tua frase', 'اجعله لك: جملتك', '做成你自己的：你的句子'),
         T('Cambia <code>\' detto \'</code> con parole tue, per esempio <code>\' il re dei \'</code> o <code>\' il super \'</code> (con uno spazio prima e dopo). Cambia il colore della scritta (<b>Font</b> → <b>Color</b>). Chi ha finito: <b>Button2</b> con Caption <b>Cancella</b> e questo codice:',
           'غيّر \' detto \' بكلماتك، مثلاً \' il re dei \' أو \' il super \' (مع مسافة قبل وبعد). غيّر لون الكتابة (Font ← Color). من أنهى: Button2 بـ Caption هو Cancella وهذا الكود:',
           '把 \' detto \' 换成你自己的话，比如 \' il re dei \' 或 \' il super \'（前后各有一个空格）。改文字的颜色（Font → Color）。做完的同学：Button2，Caption 写 Cancella，代码如下：'),
         "  Edit1.Text := '';\n  Edit2.Text := '';\n  Label1.Caption := '...';"),
    ],
    facile=[
        (T('Progetto nuovo: menu Progetto → Nuovo progetto… → Applicazione → OK. Metti una casella (abc), un bottone (OK) e una scritta (A).', 'مشروع جديد: Progetto ← Nuovo progetto… ← Applicazione ← OK. ضع خانة (abc) وزراً (OK) وكتابة (A).', '新项目：Progetto → Nuovo progetto… → Applicazione → OK。放一个输入框（abc）、一个按钮（OK）和一个文字（A）。'), None),
        (T('Doppio clic sul bottone e scrivi la riga tra begin e end;.', 'انقر مرتين على الزر واكتب السطر بين begin و end;.', '双击按钮，在 begin 和 end; 之间写这一行。'), "  Label1.Caption := 'Ciao ' + Edit1.Text;"),
        (T('Premi F9, scrivi il tuo nome e premi il bottone: compare Ciao e il tuo nome. Screenshot e consegna.', 'اضغط F9، اكتب اسمك واضغط الزر: يظهر Ciao واسمك. لقطة شاشة وسلّم.', '按 F9，写你的名字，按按钮：出现 Ciao 和你的名字。截图并提交。'), None),
    ],
    indizio=T('Le righe <code>var</code> vanno PRIMA di <code>begin</code>. Le scatole si riempiono con <code>:=</code>. Le parole fisse vanno tra apici, le scatole no.',
              'أسطر var تأتي قبل begin. الصناديق تُملأ بـ :=. الكلمات الثابتة بين علامات اقتباس، والصناديق لا.',
              'var 那几行写在 begin 前面。盒子用 := 装东西。固定的字放在引号里，盒子不用。'),
    pezzo="procedure TForm1.Button1Click(Sender: TObject);\nvar\n  nome: String;\n  animale: String;\nbegin\n  nome := Edit1.Text;\n  animale := Edit2.Text;\n  Label1.Caption := nome + ' detto ' + animale + '!';\nend;",
    spiega=T('Al compagno: che differenza c\'è tra <code>\'nome\'</code> e <code>nome</code> nel tuo programma?', 'لزميلك: ما الفرق بين \'nome\' و nome في برنامجك؟', '对同桌说：在你的程序里，\'nome\' 和 nome 有什么区别？'),
    controllo=[
        T('Il mio programma legge le due caselle e scrive il soprannome.', 'برنامجي يقرأ الخانتين ويكتب اللقب.', '我的程序读取两个输入框，写出外号。'),
        T('So dove vanno le righe var (prima di begin).', 'أعرف أين توضع أسطر var (قبل begin).', '我知道 var 那几行写在哪里（begin 前面）。'),
        T('So spiegare perché \'nome\' con gli apici scrive la parola nome.', 'أعرف أن أشرح لماذا \'nome\' مع علامات الاقتباس تكتب كلمة nome.', '我能解释为什么带引号的 \'nome\' 写出的是 nome 这个词。'),
        T('Ho consegnato ora2_unit1.pas e ora2_screenshot.png.', 'سلّمت ora2_unit1.pas و ora2_screenshot.png.', '我提交了 ora2_unit1.pas 和 ora2_screenshot.png。'),
    ],
    quaderno="var nome: String;          preparo la scatola per il testo\nnome := Edit1.Text;        metto nella scatola il testo della casella\nLabel1.Caption := nome + ' detto ' + animale;   + attacca le String\n'nome' con gli apici = la PAROLA nome\nnome  senza apici    = la SCATOLA nome",
)

M[3] = dict(
    n=3, ora='13:00-14:00', cartella='segnapunti', compito='Ora 3 · Il segnapunti',
    titolo=T('Ora 3: gli Integer, il segnapunti con StrToInt e IntToStr', 'الساعة 3: Integer، عدّاد النقاط مع StrToInt و IntToStr', '第 3 节：Integer，用 StrToInt 和 IntToStr 做记分牌'),
    intro=T('Un programma nuovo: il <b>segnapunti</b> di una partita. Un numero grande al centro: <b>+1</b> aggiunge un punto, <b>Aggiungi</b> aggiunge i punti che scrivi nella casella, <b>Azzera</b> torna a 0. Per fare i conti serve un <b>Integer</b>.',
            'برنامج جديد: عدّاد نقاط مباراة. رقم كبير في الوسط: +1 يضيف نقطة، Aggiungi يضيف النقاط التي تكتبها في الخانة، Azzera يرجع إلى 0. للحساب نحتاج Integer.',
            '一个新程序：比赛的记分牌。中间一个大数字：+1 加一分，Aggiungi 加上你在输入框里写的分数，Azzera 回到 0。要算数就需要 Integer。'),
    finestra=dict(titolo='Form1', label='12', colore='#0b6e99', bottoni=['+1', 'Aggiungi', 'Azzera'], edits=['3']),
    ripasso=T('<b>Ripasso in 1 minuto.</b> Un <b>Integer</b> è un numero intero, senza apici: <code>12</code>. Con gli Integer si fanno i conti: <code>12 + 3</code> = <code>15</code>. Ma la Caption e la casella hanno solo <b>String</b>. Servono i due traduttori: <code>StrToInt(\'12\')</code> dà il numero 12, <code>IntToStr(15)</code> dà il testo \'15\'.',
              'مراجعة في دقيقة. Integer هو عدد صحيح بلا علامات اقتباس: 12. بالأعداد نحسب: 12 + 3 = 15. لكن الـ Caption والخانة فيهما String فقط. نحتاج المترجمَين: StrToInt(\'12\') يعطي الرقم 12، و IntToStr(15) يعطي النص \'15\'.',
              '1 分钟复习。Integer 是整数，不加引号：12。整数可以算：12 + 3 = 15。可是 Caption 和输入框里只有 String。需要两个翻译：StrToInt(\'12\') 得到数字 12，IntToStr(15) 得到文字 \'15\'。'),
    passi=progetto('segnapunti') + [
        (T('Il numero grande', 'الرقم الكبير', '大数字'),
         T('Metti una <b>TLabel</b> (la A) al centro della Form1: compare <b>Label1</b>. Nell\'Ispettore oggetti cambia <b>Caption</b> in <b>0</b> (zero) e in <b>Font</b> → <b>Size</b> scrivi 48.',
           'ضع TLabel (الحرف A) في وسط Form1: يظهر Label1. في Ispettore oggetti غيّر Caption إلى 0 (صفر) وفي Font ← Size اكتب 48.',
           '在 Form1 中间放一个 TLabel（A）：出现 Label1。在 Ispettore oggetti 把 Caption 改成 0（零），在 Font → Size 写 48。'), '0'),
        (T('Il bottone +1', 'الزر +1', '+1 按钮'),
         T('Metti un <b>TButton</b> sotto il numero: compare <b>Button1</b>. Cambia <b>Caption</b> in:',
           'ضع TButton تحت الرقم: يظهر Button1. غيّر Caption إلى:',
           '在数字下面放一个 TButton：出现 Button1。把 Caption 改成：'), '+1'),
        (T('La scatola per il numero', 'الصندوق للرقم', '装数字的盒子'),
         T('Doppio clic su <b>+1</b>: si apre <code>Button1Click</code>. Clicca alla fine della riga <code>procedure</code>, premi Invio e scrivi prima di <code>begin</code>: una scatola di tipo <b>Integer</b>.',
           'انقر مرتين على +1: يفتح Button1Click. انقر في نهاية سطر procedure، اضغط Invio واكتب قبل begin: صندوق من نوع Integer.',
           '双击 +1：打开 Button1Click。点 procedure 那一行的末尾，按回车，在 begin 前面写：一个 Integer 类型的盒子。'),
         "var\n  punti: Integer;"),
        (T('Tre righe: traduci, conta, traduci', 'ثلاثة أسطر: ترجم، احسب، ترجم', '三行：翻译、计算、翻译'),
         T('Tra <code>begin</code> e <code>end;</code> scrivi: 1) <code>StrToInt</code> trasforma la scritta \'0\' nel numero 0; 2) aggiungi 1; 3) <code>IntToStr</code> trasforma il numero in scritta per la Caption.',
           'بين begin و end; اكتب: 1) StrToInt يحوّل الكتابة \'0\' إلى الرقم 0؛ 2) أضف 1؛ 3) IntToStr يحوّل الرقم إلى كتابة للـ Caption.',
           '在 begin 和 end; 之间写：1）StrToInt 把文字 \'0\' 变成数字 0；2）加 1；3）IntToStr 把数字变回文字给 Caption。'),
         "  punti := StrToInt(Label1.Caption);\n  punti := punti + 1;\n  Label1.Caption := IntToStr(punti);"),
        (T('Fai partire: F9', 'شغّل: F9', '运行：F9'),
         T('Premi <b>F9</b> e clicca <b>+1</b> tante volte: 1, 2, 3, 4… FATTO! Sfida il compagno: chi arriva prima a 30?',
           'اضغط F9 وانقر +1 مرات كثيرة: 1، 2، 3، 4… تم! تحدَّ زميلك: من يصل أولاً إلى 30؟',
           '按 F9，多次点 +1：1、2、3、4…… 完成！和同桌比赛：谁先到 30？'), None),
        (T('La casella dei punti', 'خانة النقاط', '分数的输入框'),
         T('Chiudi il programma e premi <b>F12</b> per tornare alla Form1. Metti una <b>TEdit</b> (abc): compare <b>Edit1</b>. Nell\'Ispettore oggetti cambia <b>Text</b> in:',
           'أغلق البرنامج واضغط F12 للعودة إلى Form1. ضع TEdit (abc): يظهر Edit1. في Ispettore oggetti غيّر Text إلى:',
           '关掉程序，按 F12 回到 Form1。放一个 TEdit（abc）：出现 Edit1。在 Ispettore oggetti 把 Text 改成：'), '3'),
        (T('Il bottone Aggiungi', 'الزر Aggiungi', 'Aggiungi 按钮'),
         T('Metti un secondo <b>TButton</b> accanto alla casella: compare <b>Button2</b>. Cambia <b>Caption</b> in <b>Aggiungi</b>. Fai doppio clic su Aggiungi: si apre <code>Button2Click</code>. Prima di <code>begin</code> scrivi due scatole Integer:',
           'ضع TButton ثانياً بجانب الخانة: يظهر Button2. غيّر Caption إلى Aggiungi. انقر مرتين على Aggiungi: يفتح Button2Click. قبل begin اكتب صندوقين Integer:',
           '在输入框旁边放第二个 TButton：出现 Button2。把 Caption 改成 Aggiungi。双击 Aggiungi：打开 Button2Click。在 begin 前面写两个 Integer 盒子：'),
         "var\n  punti: Integer;\n  aggiunta: Integer;"),
        (T('Il codice di Aggiungi', 'كود Aggiungi', 'Aggiungi 的代码'),
         T('Tra <code>begin</code> e <code>end;</code> scrivi le quattro righe: anche la casella ha una String, quindi anche lì serve <code>StrToInt</code>.',
           'بين begin و end; اكتب الأسطر الأربعة: الخانة أيضاً فيها String، لذلك نحتاج هناك أيضاً StrToInt.',
           '在 begin 和 end; 之间写这四行：输入框里也是 String，所以那里也要用 StrToInt。'),
         "  punti := StrToInt(Label1.Caption);\n  aggiunta := StrToInt(Edit1.Text);\n  punti := punti + aggiunta;\n  Label1.Caption := IntToStr(punti);"),
        (T('Prova Aggiungi', 'جرّب Aggiungi', '试试 Aggiungi'),
         T('Premi <b>F9</b>. Clicca <b>Aggiungi</b>: il numero sale di 3. Scrivi 10 nella casella e clicca ancora: sale di 10. FATTO! Fai lo screenshot.',
           'اضغط F9. انقر Aggiungi: يرتفع الرقم 3. اكتب 10 في الخانة وانقر مجدداً: يرتفع 10. تم! خذ لقطة شاشة.',
           '按 F9。点 Aggiungi：数字加 3。在输入框写 10，再点：加 10。完成！截图。'), None),
        (T('Il bottone Azzera', 'الزر Azzera', 'Azzera 按钮'),
         T('Chiudi il programma, F12. Metti un terzo <b>TButton</b>: <b>Button3</b>, Caption <b>Azzera</b>. Doppio clic e scrivi la riga. \'0\' ha gli apici: la Caption vuole una String.',
           'أغلق البرنامج، F12. ضع TButton ثالثاً: Button3، Caption هو Azzera. انقر مرتين واكتب السطر. \'0\' لها علامتا اقتباس: الـ Caption تريد String.',
           '关掉程序，F12。放第三个 TButton：Button3，Caption 写 Azzera。双击，写这一行。\'0\' 有引号：Caption 要的是 String。'),
         "  Label1.Caption := '0';"),
        (T('La trappola del 53', 'فخ الـ 53', '53 的陷阱'),
         T('Prova a capire senza scriverlo: se in Aggiungi ci fosse <code>Label1.Caption := Label1.Caption + Edit1.Text;</code>, con 5 sul display e 3 nella casella, comparirebbe <b>53</b>, non 8. Perché? Due String si ATTACCANO, due Integer si SOMMANO. Scrivilo nel quaderno.',
           'حاول أن تفهم دون أن تكتبه: لو كان في Aggiungi السطر Label1.Caption := Label1.Caption + Edit1.Text; مع 5 على الشاشة و3 في الخانة، لظهر 53 وليس 8. لماذا؟ نصّان يُلصقان، وعددان يُجمعان. اكتبه في الدفتر.',
           '不写代码，想一想：如果 Aggiungi 里写的是 Label1.Caption := Label1.Caption + Edit1.Text;，显示 5，输入框写 3，会出现 53，而不是 8。为什么？两个 String 是连起来，两个 Integer 是相加。写进本子里。'), None),
        (T('Fallo tuo', 'اجعله لك', '做成你自己的'),
         T('Una scritta con il tuo nome sopra il numero (una Label con Caption <i>Segnapunti di Ahmed</i>), i tuoi colori, e il bottone <b>+1</b> che diventa <b>+2</b> (cambia <code>punti + 1</code> e la Caption). Chi ha finito: un bottone <b>-1</b>.',
           'كتابة باسمك فوق الرقم (Label بـ Caption هو Segnapunti di Ahmed)، ألوانك، والزر +1 يصبح +2 (غيّر punti + 1 والـ Caption). من أنهى: زر -1.',
           '数字上方加一行写着你名字的文字（一个 Label，Caption 写 Segnapunti di Ahmed），你的颜色，再把 +1 按钮变成 +2（改 punti + 1 和 Caption）。做完的同学：加一个 -1 按钮。'), None),
    ],
    facile=[
        (T('Progetto nuovo. Metti una scritta (A) con Caption 0 e un bottone (OK) con Caption +1.', 'مشروع جديد. ضع كتابة (A) بـ Caption هو 0 وزراً (OK) بـ Caption هو +1.', '新项目。放一个文字（A），Caption 写 0；一个按钮（OK），Caption 写 +1。'), None),
        (T('Doppio clic sul bottone e scrivi questa riga sola tra begin e end;.', 'انقر مرتين على الزر واكتب هذا السطر وحده بين begin و end;.', '双击按钮，在 begin 和 end; 之间只写这一行。'), "  Label1.Caption := IntToStr(StrToInt(Label1.Caption) + 1);"),
        (T('Premi F9 e clicca +1: il numero sale. Screenshot e consegna.', 'اضغط F9 وانقر +1: الرقم يرتفع. لقطة شاشة وسلّم.', '按 F9，点 +1：数字增加。截图并提交。'), None),
    ],
    indizio=T('La Caption è una String: per contare la traduci in Integer con <code>StrToInt</code>, fai il conto, e la ritraduci con <code>IntToStr</code>. Le righe <code>var</code> vanno prima di <code>begin</code>.',
              'الـ Caption هي String: للحساب تترجمها إلى Integer بـ StrToInt، تحسب، ثم تعيدها بـ IntToStr. أسطر var قبل begin.',
              'Caption 是 String：要计算就先用 StrToInt 翻译成 Integer，算完再用 IntToStr 翻译回来。var 那几行写在 begin 前面。'),
    pezzo="procedure TForm1.Button2Click(Sender: TObject);\nvar\n  punti: Integer;\n  aggiunta: Integer;\nbegin\n  punti := StrToInt(Label1.Caption);\n  aggiunta := StrToInt(Edit1.Text);\n  punti := punti + aggiunta;\n  Label1.Caption := IntToStr(punti);\nend;",
    spiega=T('Al compagno: nel tuo segnapunti, che cosa fa <code>StrToInt</code> e che cosa fa <code>IntToStr</code>? Perché servono tutti e due?', 'لزميلك: في عدّاد نقاطك، ماذا يفعل StrToInt وماذا يفعل IntToStr؟ لماذا نحتاج الاثنين؟', '对同桌说：在你的记分牌里，StrToInt 做什么，IntToStr 做什么？为什么两个都需要？'),
    controllo=[
        T('Il mio segnapunti sale con +1 e con Aggiungi, e torna a 0 con Azzera.', 'عدّاد نقاطي يرتفع بـ +1 وبـ Aggiungi ويعود إلى 0 بـ Azzera.', '我的记分牌用 +1 和 Aggiungi 增加，用 Azzera 回到 0。'),
        T('So dire perché serve StrToInt prima del conto e IntToStr dopo.', 'أعرف أن أقول لماذا نحتاج StrToInt قبل الحساب و IntToStr بعده.', '我能说出为什么计算前要 StrToInt，计算后要 IntToStr。'),
        T('So spiegare perché \'5\' + \'3\' darebbe 53.', 'أعرف أن أشرح لماذا \'5\' + \'3\' تعطي 53.', '我能解释为什么 \'5\' + \'3\' 会得到 53。'),
        T('Ho consegnato ora3_unit1.pas e ora3_screenshot.png.', 'سلّمت ora3_unit1.pas و ora3_screenshot.png.', '我提交了 ora3_unit1.pas 和 ora3_screenshot.png。'),
    ],
    quaderno="var punti: Integer;                  scatola per un numero intero\npunti := StrToInt(Label1.Caption);   testo -> numero   '5' -> 5\npunti := punti + 1;                  il conto (solo con gli Integer)\nLabel1.Caption := IntToStr(punti);   numero -> testo   6 -> '6'\n'5' + '3' = '53'          5 + 3 = 8",
)

# ------------------------------------------------------------------ teoria e quiz (banca del corso)
SPAN_AR = '<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">%s</span>'
SPAN_ZH = '<span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">%s</span>'


def q3(t): return t[0] + SPAN_AR % t[1] + SPAN_ZH % t[2]


def par(t): return '<p>%s</p><p lang="ar" dir="rtl" style="color:#5b6573">%s</p><p lang="zh" style="color:#5b6573">%s</p>' % t


def pre(c): return '<pre style="background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap">' + html.escape(c) + '</pre>'


SCHEDE = [
    (T('1. La variabile: una scatola con un nome', '١. المتغير: صندوق له اسم', '1. 变量：一个有名字的盒子'),
     [T('Una <b>variabile</b> è una <b>scatola</b> con un\'etichetta. Sull\'etichetta c\'è il nome (per esempio <code>nome</code> o <code>eta</code>), dentro c\'è un valore. Il segno <code>:=</code> vuol dire «metti dentro».',
        'المتغير صندوق عليه ملصق. على الملصق الاسم (مثلاً nome أو eta)، وفي الداخل قيمة. العلامة := تعني «ضع داخل».',
        '变量是一个贴了标签的盒子。标签上是名字（比如 nome 或 eta），里面是一个值。:= 的意思是“放进去”。'),
      T('Ogni scatola ha un <b>tipo</b>: dice che cosa ci può stare dentro. Oggi ne impariamo due: <b>String</b> (testo) e <b>Integer</b> (numero intero).',
        'لكل صندوق نوع: يقول ماذا يمكن أن يوضع فيه. اليوم نتعلم نوعين: String (نص) و Integer (عدد صحيح).',
        '每个盒子都有一个类型：说明里面能装什么。今天学两种：String（文字）和 Integer（整数）。')],
     "var\n  nome: String;     { scatola per il testo }\n  eta: Integer;     { scatola per un numero intero }\nbegin\n  nome := 'Ahmed';\n  eta := 12;"),
    (T('2. String: il testo tra apici', '٢. String: النص بين علامتي اقتباس', '2. String：引号里的文字'),
     [T('Una <b>String</b> è un <b>testo</b>: lettere, spazi, simboli e anche cifre. In Pascal si scrive sempre tra <b>apici</b> (la virgoletta alta): <code>\'Ciao\'</code>, <code>\'Milano\'</code>, <code>\'007\'</code>.',
        'String هي نص: حروف ومسافات ورموز وحتى أرقام. في Pascal تُكتب دائماً بين علامتي اقتباس مفردتين: \'Ciao\'، \'Milano\'، \'007\'.',
        'String 是文字：字母、空格、符号，也可以是数字。在 Pascal 里总是写在单引号里：\'Ciao\'、\'Milano\'、\'007\'。'),
      T('Attenzione: <code>\'007\'</code> ha gli apici, quindi è una String, anche se dentro ci sono cifre. Il <code>+</code> tra due String le <b>attacca</b>: <code>\'Ciao \' + \'Ahmed\'</code> fa <code>\'Ciao Ahmed\'</code>.',
        'انتبه: \'007\' لها علامتا اقتباس، إذن هي String حتى لو كان فيها أرقام. علامة + بين نصّين تلصقهما: \'Ciao \' + \'Ahmed\' تعطي \'Ciao Ahmed\'.',
        '注意：\'007\' 有引号，所以它是 String，即使里面是数字。两个 String 之间的 + 是把它们连起来：\'Ciao \' + \'Ahmed\' 得到 \'Ciao Ahmed\'。')],
     "'Ciao'      String\n'007'       String (ha gli apici!)\n'Ciao ' + 'Ahmed'  ->  'Ciao Ahmed'"),
    (T('3. Integer: il numero intero', '٣. Integer: العدد الصحيح', '3. Integer：整数'),
     [T('Un <b>Integer</b> è un <b>numero intero</b>: senza virgola, senza apici. Può essere anche negativo: <code>0</code>, <code>7</code>, <code>2026</code>, <code>-5</code>.',
        'Integer هو عدد صحيح: بلا فاصلة وبلا علامات اقتباس. يمكن أن يكون سالباً: 0، 7، 2026، -5.',
        'Integer 是整数：没有小数点，没有引号。也可以是负数：0、7、2026、-5。'),
      T('Con gli Integer si fanno i <b>conti</b>: <code>+</code> <code>-</code> <code>*</code>. <code>3.5</code> NON è un Integer: ha la virgola (in Pascal si scrive con il punto).',
        'بالأعداد الصحيحة نحسب: + - *. العدد 3.5 ليس Integer: فيه فاصلة (في Pascal تُكتب بنقطة).',
        '整数可以计算：+ - *。3.5 不是 Integer：它有小数点（Pascal 里用点来写）。')],
     "12          Integer\n-5          Integer\n3.5         NON e' un Integer (ha la virgola)\n12 + 3  ->  15"),
    (T('4. La trappola: \'5\' + \'3\' oppure 5 + 3?', '٤. الفخ: \'5\' + \'3\' أم 5 + 3؟', '4. 陷阱：\'5\' + \'3\' 还是 5 + 3？'),
     [T('Lo stesso segno <code>+</code> fa due cose diverse. Tra due <b>String</b> le attacca: <code>\'5\' + \'3\'</code> = <code>\'53\'</code>. Tra due <b>Integer</b> fa la somma: <code>5 + 3</code> = <code>8</code>.',
        'نفس العلامة + تفعل شيئين مختلفين. بين نصّين تلصقهما: \'5\' + \'3\' = \'53\'. بين عددين تجمعهما: 5 + 3 = 8.',
        '同一个 + 做两件不同的事。两个 String 之间是连起来：\'5\' + \'3\' = \'53\'。两个 Integer 之间是相加：5 + 3 = 8。'),
      T('Per questo bisogna sempre guardare il <b>tipo</b>: gli apici ti dicono che è testo.',
        'لهذا يجب دائماً النظر إلى النوع: علامات الاقتباس تقول لك إنه نص.',
        '所以一定要看类型：引号告诉你它是文字。')],
     "'5' + '3'   ->  '53'   (String: attacca)\n 5  +  3   ->   8     (Integer: somma)"),
    (T('5. In Lazarus le caselle hanno String', '٥. في Lazarus الخانات فيها String', '5. 在 Lazarus 里，输入框里是 String'),
     [T('<code>Edit1.Text</code> (quello che l\'utente scrive nella casella) è una <b>String</b>. Anche se scrivi 15, dentro c\'è <code>\'15\'</code>, il testo. Anche <code>Label1.Caption</code> e <code>Button1.Caption</code> sono String.',
        'Edit1.Text (ما يكتبه المستخدم في الخانة) هو String. حتى لو كتبت 15، في الداخل \'15\'، النص. و Label1.Caption و Button1.Caption أيضاً String.',
        'Edit1.Text（用户在输入框里写的）是 String。即使你写 15，里面也是 \'15\'，是文字。Label1.Caption 和 Button1.Caption 也是 String。'),
      T('Per questo <code>Label1.Caption := 7;</code> dà errore quando premi F9: la Caption vuole una String e 7 è un Integer.',
        'لهذا Label1.Caption := 7; يعطي خطأ عندما تضغط F9: الـ Caption تريد String و7 هو Integer.',
        '所以按 F9 时 Label1.Caption := 7; 会出错：Caption 要的是 String，7 是 Integer。')],
     "Edit1.Text       String  (scrivo 15 -> '15')\nLabel1.Caption   String\nLabel1.Caption := 7;     ERRORE: Incompatible types\nLabel1.Caption := '7';   giusto"),
    (T('6. I due traduttori: StrToInt e IntToStr', '٦. المترجمان: StrToInt و IntToStr', '6. 两个翻译：StrToInt 和 IntToStr'),
     [T('<code>StrToInt</code> si legge «da String a Integer»: <code>StrToInt(\'7\')</code> dà il numero 7. <code>IntToStr</code> si legge «da Integer a String»: <code>IntToStr(7)</code> dà il testo <code>\'7\'</code>.',
        'StrToInt تُقرأ «من String إلى Integer»: StrToInt(\'7\') يعطي الرقم 7. و IntToStr تُقرأ «من Integer إلى String»: IntToStr(7) يعطي النص \'7\'.',
        'StrToInt 读作“从 String 到 Integer”：StrToInt(\'7\') 得到数字 7。IntToStr 读作“从 Integer 到 String”：IntToStr(7) 得到文字 \'7\'。'),
      T('Il viaggio di un numero: casella → <code>StrToInt</code> → conto → <code>IntToStr</code> → Caption. Se la casella contiene <i>ciao</i>, <code>StrToInt</code> non sa tradurre: il programma si ferma con un errore.',
        'رحلة الرقم: الخانة ← StrToInt ← الحساب ← IntToStr ← Caption. إذا كانت الخانة فيها ciao، لا يعرف StrToInt الترجمة: يتوقف البرنامج بخطأ.',
        '一个数字的旅程：输入框 → StrToInt → 计算 → IntToStr → Caption。如果输入框里是 ciao，StrToInt 翻译不了：程序会报错停下。')],
     "Edit1.Text   '7'  --StrToInt-->  7  --(+1)-->  8  --IntToStr-->  '8'   Label1.Caption"),
]

ALLENA = [   # una domanda facile dopo ogni scheda (ripasso)
    (1, T('Che cos\'è una variabile?', 'ما هو المتغير؟', '什么是变量？'), ['una scatola con un nome, con dentro un valore', 'un bottone della Form', 'un errore di Lazarus'], 'Ha un nome e un tipo; := ci mette dentro un valore.'),
    (2, T('Quale di questi è una String?', 'أيّ من هذه هو String؟', '下面哪个是 String？'), ["'Milano'", '25', 'Milano senza apici'], 'Le String stanno tra apici.'),
    (3, T('Quale di questi è un Integer?', 'أيّ من هذه هو Integer؟', '下面哪个是 Integer？'), ['15', "'15'", '3.5'], 'Numero intero, senza apici e senza virgola.'),
    (4, T("Che cosa dà '2' + '2'?", "ماذا تعطي '2' + '2'؟", "'2' + '2' 得到什么？"), ["'22'", '4', "'4'"], 'Due String si attaccano.'),
    (5, T('L\'utente scrive 10 in Edit1. Che cos\'è Edit1.Text?', 'المستخدم يكتب 10 في Edit1. ما هو Edit1.Text؟', '用户在 Edit1 里写 10。Edit1.Text 是什么？'), ["la String '10'", "l'Integer 10", "l'Integer 0"], 'Quello che c\'è in una casella è sempre testo.'),
    (6, T('Vuoi mostrare il numero 8 in Label1.Caption. Che cosa usi?', 'تريد أن تُظهر الرقم 8 في Label1.Caption. ماذا تستعمل؟', '你想在 Label1.Caption 里显示数字 8。用什么？'), ['IntToStr(8)', 'StrToInt(8)', 'niente: Label1.Caption := 8;'], 'IntToStr: da Integer a String.'),
]

# Le 22 crocette: OGNI risposta verificata con il compilatore Free Pascal (fpc 3.2, {$mode objfpc}{$H+}) il 29/10/2026.
CROCETTE = [
    ('tipo', T("Che tipo è <code>'42'</code>?", "ما نوع <code>'42'</code>؟", "<code>'42'</code> 是什么类型？"), ['String', 'Integer', 'nessuno dei due'], "Ha gli apici: è testo."),
    ('tipo', T('Che tipo è <code>42</code> (senza apici)?', 'ما نوع <code>42</code> (بلا علامات اقتباس)؟', '<code>42</code>（不带引号）是什么类型？'), ['Integer', 'String', 'nessuno dei due'], 'Numero intero senza apici.'),
    ('tipo', T("Che tipo è <code>'007'</code>?", "ما نوع <code>'007'</code>؟", "<code>'007'</code> 是什么类型？"), ['String', 'Integer, perché sono cifre', 'Integer: vale 7'], 'Gli apici decidono: è testo, anche se ci sono cifre.'),
    ('tipo', T("Che tipo è <code>' 12'</code> (con uno spazio prima del 12)?", "ما نوع <code>' 12'</code> (مع مسافة قبل 12)؟", "<code>' 12'</code>（12 前面有一个空格）是什么类型？"), ['String', 'Integer', 'nessuno: è un errore'], 'Ha gli apici: è testo, lo spazio fa parte del testo.'),
    ('tipo', T('Che tipo è <code>-5</code>?', 'ما نوع <code>-5</code>؟', '<code>-5</code> 是什么类型？'), ['Integer', 'String', 'non è un numero'], 'Gli Integer possono essere negativi.'),
    ('tipo', T('<code>3.5</code> è un Integer?', 'هل <code>3.5</code> هو Integer؟', '<code>3.5</code> 是 Integer 吗？'), ['no: ha la virgola, non è un numero intero', 'sì', 'no: è una String'], 'Integer = solo numeri interi. 3.5 è un numero con la virgola (senza apici non è una String).'),
    ('lazarus', T("L'utente scrive <b>15</b> nella casella Edit1. Che cos'è <code>Edit1.Text</code>?", "يكتب المستخدم 15 في الخانة Edit1. ما هو <code>Edit1.Text</code>؟", "用户在输入框 Edit1 里写 15。<code>Edit1.Text</code> 是什么？"), ["la String '15'", "l'Integer 15", "l'Integer 0"], 'Il testo di una casella è sempre una String.'),
    ('lazarus', T("<code>var anno: String;</code> e poi <code>anno := '2026';</code>. Di che tipo è <code>anno</code>?", "<code>var anno: String;</code> ثم <code>anno := '2026';</code>. ما نوع <code>anno</code>؟", "<code>var anno: String;</code> 然后 <code>anno := '2026';</code>。<code>anno</code> 是什么类型？"), ['String, anche se dentro ci sono cifre', 'Integer, perché 2026 è un numero', 'cambia tipo da solo'], 'Il tipo lo decide la riga var: la scatola anno è per il testo.'),
    ('conto', T("Che cosa dà <code>IntToStr(5) + '5'</code>?", "ماذا يعطي <code>IntToStr(5) + '5'</code>؟", "<code>IntToStr(5) + '5'</code> 得到什么？"), ["la String '55'", "l'Integer 10", "la String '10'", 'un errore'], "IntToStr(5) è '5'; due String si attaccano."),
    ('conto', T("Che cosa dà <code>StrToInt('3') + 2</code>?", "ماذا يعطي <code>StrToInt('3') + 2</code>؟", "<code>StrToInt('3') + 2</code> 得到什么？"), ["l'Integer 5", "la String '32'", "la String '5'", 'un errore'], "StrToInt('3') è il numero 3; 3 + 2 = 5."),
    ('conto', T("Che cosa dà <code>'3' + '4'</code>?", "ماذا يعطي <code>'3' + '4'</code>؟", "<code>'3' + '4'</code> 得到什么？"), ["'34'", '7', "'7'"], 'Due String si attaccano.'),
    ('conto', T('<code>a</code> e <code>b</code> sono Integer: <code>a := 2; b := 3;</code>. Che cosa mostra <code>Label1.Caption := IntToStr(a + b);</code>?', 'a و b من نوع Integer: <code>a := 2; b := 3;</code>. ماذا يُظهر <code>Label1.Caption := IntToStr(a + b);</code>؟', 'a 和 b 是 Integer：<code>a := 2; b := 3;</code>。<code>Label1.Caption := IntToStr(a + b);</code> 显示什么？'), ['5', '23', 'un errore'], 'Prima la somma (5), poi la traduzione in testo.'),
    ('conto', T('Stessi <code>a := 2; b := 3;</code>. Che cosa mostra <code>Label1.Caption := IntToStr(a) + IntToStr(b);</code>?', 'نفس <code>a := 2; b := 3;</code>. ماذا يُظهر <code>Label1.Caption := IntToStr(a) + IntToStr(b);</code>؟', '同样 <code>a := 2; b := 3;</code>。<code>Label1.Caption := IntToStr(a) + IntToStr(b);</code> 显示什么？'), ['23', '5', 'un errore'], "Prima diventano testo ('2' e '3'), poi si attaccano."),
    ('conto', T("Che cosa dà <code>'Ciao' + 5</code>?", "ماذا يعطي <code>'Ciao' + 5</code>؟", "<code>'Ciao' + 5</code> 得到什么？"), ['errore quando premi F9: non si attacca un Integer a una String', "'Ciao5'", "'Ciao 5'"], "Serve IntToStr: 'Ciao' + IntToStr(5)."),
    ('errore', T('Quale riga dà errore quando premi F9 (Lazarus non la compila)?', 'أيّ سطر يعطي خطأ عندما تضغط F9 (لا يترجمه Lazarus)؟', '按 F9 时哪一行会出错（Lazarus 编译不了）？'), ['Label1.Caption := 7;', "Label1.Caption := '7';", 'Label1.Caption := IntToStr(7);', "Label1.Caption := '7' + '7';"], 'La Caption vuole una String: 7 senza apici è un Integer.'),
    ('errore', T('<code>n</code> è un Integer. Quale riga è GIUSTA?', '<code>n</code> من نوع Integer. أيّ سطر صحيح؟', '<code>n</code> 是 Integer。哪一行是对的？'), ['n := StrToInt(Edit1.Text);', 'n := Edit1.Text;', "n := 'Edit1.Text';", 'n := IntToStr(Edit1.Text);'], 'Edit1.Text è una String: per metterla in un Integer serve StrToInt.'),
    ('errore', T("Il programma esegue <code>n := StrToInt('ciao');</code>. Che cosa succede?", "البرنامج ينفّذ <code>n := StrToInt('ciao');</code>. ماذا يحدث؟", "程序执行 <code>n := StrToInt('ciao');</code>。会发生什么？"), ["parte, ma quando arriva a questa riga si ferma con un errore: 'ciao' non è un numero", 'n vale 0', 'n vale 4 (le lettere)', "n vale 'ciao'"], 'StrToInt sa tradurre solo testo fatto di cifre.'),
    ('traccia', T("Che cosa mostra la Label alla fine?" + pre("var s: String;\nbegin\n  s := '1';\n  s := s + '1';\n  s := s + '1';\n  Label1.Caption := s;"), 'ماذا تُظهر الـ Label في النهاية؟', '最后 Label 显示什么？'), ['111', '3', '1'], "s è una String: '1', poi '11', poi '111'."),
    ('traccia', T("Che cosa mostra la Label alla fine?" + pre("var n: Integer;\nbegin\n  n := 1;\n  n := n + n;\n  n := n + n;\n  Label1.Caption := IntToStr(n);"), 'ماذا تُظهر الـ Label في النهاية؟', '最后 Label 显示什么？'), ['4', '2', '11', '1111'], 'n è un Integer: 1, poi 2, poi 4.'),
    ('traccia', T("Nella casella Edit1 c'è scritto <b>7</b>. Che cosa mostra la Label?" + pre("var n: Integer;\nbegin\n  n := StrToInt(Edit1.Text) + 3;\n  Label1.Caption := Edit1.Text + IntToStr(n);"), 'في الخانة Edit1 مكتوب 7. ماذا تُظهر الـ Label؟', '输入框 Edit1 里写着 7。Label 显示什么？'), ['710', '10', '17', '73'], "n = 7 + 3 = 10; poi si attaccano '7' e '10'."),
    ('traccia', T("Che cosa mostra la Label alla fine?" + pre("var x: Integer; s: String;\nbegin\n  x := 4;\n  s := IntToStr(x) + IntToStr(x);\n  x := StrToInt(s) + 1;\n  Label1.Caption := IntToStr(x);"), 'ماذا تُظهر الـ Label في النهاية؟', '最后 Label 显示什么？'), ['45', '9', '441', '8'], "s = '44'; StrToInt('44') + 1 = 45."),
    ('traccia', T("Che cosa mostra la Label alla fine?" + pre("var nome: String;\nbegin\n  nome := 'Sara';\n  Label1.Caption := 'nome' + ' ' + nome;"), 'ماذا تُظهر الـ Label في النهاية؟', '最后 Label 显示什么？'), ['nome Sara', 'Sara Sara', 'nome nome'], "'nome' tra apici è la parola; nome senza apici è la scatola che contiene Sara."),
]

APERTE = [
    T('IL TUO SEGNAPUNTI (ora 3). Copia QUI SOTTO, scrivendola tu, la riga del TUO programma che trasforma il testo della casella Edit1 in un numero. Poi spiega con parole tue che cosa succederebbe se togliessi StrToInt.',
      'عدّاد نقاطك (الساعة 3). اكتب هنا بنفسك سطر برنامجك الذي يحوّل نص الخانة Edit1 إلى رقم. ثم اشرح بكلماتك ماذا يحدث لو حذفت StrToInt.',
      '你的记分牌（第 3 节）。在下面亲手写出你程序里把输入框 Edit1 的文字变成数字的那一行。再用你自己的话解释：如果去掉 StrToInt 会怎样。'),
    T('Sul tuo segnapunti c\'è 12 e nella casella scrivi 5. Che numero vedi dopo Aggiungi? E che cosa vedresti se la riga fosse Label1.Caption := Label1.Caption + Edit1.Text; ? Spiega il perché con le parole String e Integer.',
      'على عدّاد نقاطك 12 وفي الخانة تكتب 5. أيّ رقم ترى بعد Aggiungi؟ وماذا سترى لو كان السطر Label1.Caption := Label1.Caption + Edit1.Text; ؟ اشرح السبب بكلمتي String و Integer.',
      '你的记分牌上是 12，输入框里写 5。按 Aggiungi 后看到几？如果那一行是 Label1.Caption := Label1.Caption + Edit1.Text; 会看到什么？用 String 和 Integer 这两个词解释原因。'),
    T('IL TUO SOPRANNOME (ora 2). Scrivi che cosa hai messo nelle due caselle e che cosa è comparso. Perché in quel programma NON serve StrToInt?',
      'لقبك (الساعة 2). اكتب ماذا وضعت في الخانتين وماذا ظهر. لماذا لا نحتاج StrToInt في ذلك البرنامج؟',
      '你的外号（第 2 节）。写出你在两个输入框里填了什么、出现了什么。为什么那个程序不需要 StrToInt？'),
]
CRITERI = ['riga vera con StrToInt(Edit1.Text) e il nome della propria variabile; senza StrToInt: errore Incompatible types, la casella è una String',
           '17; con la riga sbagliata 125: le String si attaccano, gli Integer si sommano',
           'valori propri delle caselle e frase comparsa; solo testo attaccato con +, nessun conto, quindi niente Integer']


# Foto della lavagna dentro le schede (30/10/2026, Nicola: «Integra le foto nella teoria"). Percorso visto da docs/verifica/.
FOTO_SCHEDE = {
    3: ('../1inf-unicode/immagini/lavagna-2026-10-30-3.jpg',
        "La lavagna del 30/10: stringhe e interi, '12' + '15' = '1215' e 12 + 15 = 27",
        T("La lavagna di oggi: con gli apici <code>'12' + '15' = '1215'</code> (String, attacca); senza apici <code>12 + 15 = 27</code> (Integer, somma).",
          "سبورة اليوم: مع علامات الاقتباس '12' + '15' = '1215' (String، تلصق)؛ بدون علامات الاقتباس 12 + 15 = 27 (Integer، تجمع).",
          "今天的白板：有引号 '12' + '15' = '1215'（String，连起来）；没有引号 12 + 15 = 27（Integer，相加）。")),
}


def foto(f):
    if not f:
        return ''
    src, alt, cap = f
    return ('<img src="%s" alt="%s" style="display:block;width:100%%;max-width:520px;height:auto;margin:10px auto 4px;border-radius:10px;border:1px solid #d5dbe3" loading="lazy">' % (src, html.escape(alt))) + par(cap)

def banca():
    B = {
        'id': BANCA_ID + '-v1', 'classe': '1INF',
        'titolo': 'String e Integer · String و Integer · String 和 Integer',
        'sotto': '1INF · 30/10/2026 · laboratorio, 1ª ora · variabili, String, Integer, StrToInt, IntToStr · teoria, ripasso e quiz',
        'stato': 'stato/' + BANCA_ID + '.json', 'minuti': 20, 'anteprima': '868848605',
        'aree': {'tipi': {'nome': 'String e Integer', 'peso': 85}, 'mia': {'nome': 'Nel mio programma (parole tue)', 'peso': 15}},
        'strumenti': [{'t': 'La mia giornata: voto, fatto e da fare', 'u': '../1inf-oggi/', 'c': '#b45309'}],
        'schede': [], 'allenamento': [], 'crocette': [], 'aperte': [], 'recupero': [],
    }
    for i, (tit, testi, cod) in enumerate(SCHEDE):
        B['schede'].append({'titolo': ' · '.join(tit), 'testo': ''.join(par(t) for t in testi) + pre(cod) + foto(FOTO_SCHEDE.get(i))})
    for sc, q, o, sp in ALLENA:
        B['allenamento'].append({'tipo': 'c', 'area': 'tipi', 'tema': '', 'q': q3(q), 'o': o, 'a': 0, 'spiega': sp, 'scheda': sc})
    for tema, q, o, sp in CROCETTE:
        B['crocette'].append({'tipo': 'c', 'area': 'tipi', 'tema': tema, 'q': q3(q), 'o': o, 'a': 0, 'spiega': sp})
    for i, q in enumerate(APERTE):
        B['aperte'].append({'area': 'mia', 'tema': 'mio', 'q': q3(q), 'aiuto': 'Almeno 15 parole. Puoi scrivere anche nella tua lingua.', 'min_parole': 15, 'criteri': CRITERI[i]})
    for sc, q, o, sp in ALLENA:
        B['recupero'].append({'tipo': 'c', 'area': 'tipi', 'tema': '', 'q': q3(q), 'o': o, 'a': 0, 'spiega': sp})
    return B


def moduli_quiz():   # piano A: le stesse crocette per forms.crea_quiz (testo semplice, tre lingue per riga)
    dom = []
    for k, (tema, q, o, sp) in enumerate(CROCETTE, 1):
        it = q[0]
        it = it.replace('<pre style="background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap">', '\n').replace('</pre>', '')
        import re
        it = html.unescape(re.sub(r'<[^>]+>', '', it))
        ar = html.unescape(re.sub(r'<[^>]+>', '', q[1])); zh = html.unescape(re.sub(r'<[^>]+>', '', q[2]))
        dom.append({'A': ['%d) %s\n%s\n%s' % (k, it, ar, zh), o[0], o[1:]]})
    return {'titolo': 'Quiz — String e Integer (1INF, laboratorio 30/10)',
            'descrizione': '22 domande su String e Integer. Ogni risposta giusta vale 1 punto. Leggi BENE il codice: un apice cambia tutto.\n٢٢ سؤالاً عن String و Integer. اقرأ الكود جيداً: علامة اقتباس واحدة تغيّر كل شيء.\n22 道关于 String 和 Integer 的题。仔细读代码：一个引号就能改变一切。',
            'punti': 1, 'mescola': True, 'versioni': ['A'], 'domande': dom}


# ------------------------------------------------------------------ pagina HTML del modulo
CSS = """:root{--bg:#f6f7f9;--fg:#1f2328;--mu:#5b6573;--card:#fff;--bd:#d5dbe3;--acc:#0b6e99;--ok:#1a7f37;--q:#fff4c2;--ante:#fde8e8;--blu:#1f6feb}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--q:#3b3200;--ante:#3a1616}}
:root[data-theme="dark"]{--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--q:#3b3200;--ante:#3a1616}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.5 system-ui,"Segoe UI",sans-serif}
main{max-width:820px;margin:0 auto;padding:12px 16px 60px}h1{font-size:1.45em;margin:.4em 0}h2{font-size:1.15em;margin:.2em 0 .4em}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 14px;margin:12px 0}
.ar{direction:rtl;text-align:right;color:var(--mu);font-size:.95em;margin:4px 0;font-family:"Amiri","Noto Naskh Arabic","Segoe UI",serif}.zh{color:var(--mu);font-size:.95em;margin:4px 0;font-family:"WenQuanYi Zen Hei","Microsoft YaHei",sans-serif}
pre{background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;overflow-x:auto;font-size:16px;white-space:pre-wrap;margin:8px 0}
.quad{background:var(--q);border:2px solid #d4a017;border-radius:10px;padding:10px 12px}.f5{background:var(--q);border-radius:10px;padding:8px 12px;font-size:.95em}
.ante{background:var(--ante);border:2px solid #c0392b;border-radius:10px;padding:8px 12px;font-size:.95em}
a.bt,button.bt{display:block;width:100%;text-align:center;background:var(--acc);color:#fff;font:inherit;font-weight:700;padding:12px;border-radius:10px;text-decoration:none;margin:8px 0;border:0;cursor:pointer}
a.bt.v,button.bt.v{background:var(--ok)}a.bt.b{background:#fff0;color:var(--acc);border:2px solid var(--acc);font-weight:600}
code{background:rgba(127,127,127,.15);border-radius:5px;padding:1px 5px}
.barra{height:14px;background:var(--bd);border-radius:7px;overflow:hidden;margin:6px 0}.barra i{display:block;height:100%;background:var(--ok);width:0}
.passo{border:3px solid var(--bd);border-radius:14px;padding:6px 14px 10px;margin:14px 0;background:var(--card)}
.passo .num{display:inline-flex;width:38px;height:38px;border-radius:50%;background:#6e7781;color:#fff;align-items:center;justify-content:center;font-weight:800;margin-right:6px}
.passo .bollo{float:right;font-size:14px;padding:3px 10px;border-radius:8px;color:#fff;background:#6e7781}
.passo.fatto{border-color:var(--ok)}.passo.fatto .num,.passo.fatto .bollo{background:var(--ok)}
.passo.ora{border:4px solid var(--blu)}.passo.ora .num,.passo.ora .bollo{background:var(--blu)}
.passo button.fb{font:inherit;font-weight:700;background:var(--ok);color:#fff;border:0;border-radius:10px;padding:9px 16px;cursor:pointer;margin-top:6px}
.passo.fatto button.fb{background:#6e7781}
.win{max-width:360px;border:2px solid #6e7781;border-radius:8px;overflow:hidden;margin:8px auto;background:#f0f0f0;color:#111}
.win .tb{background:#dfe3e8;padding:4px 8px;font-size:14px;display:flex;justify-content:space-between}.win .co{padding:14px;text-align:center}
.win .lb{font-size:28px;font-weight:800;margin:6px 0}.win .ed{display:block;background:#fff;border:1px solid #8a8a8a;text-align:left;padding:3px 6px;margin:6px auto;width:80%;font-size:16px}
.win .bu{display:inline-block;background:#e1e1e1;border:1px solid #8a8a8a;border-radius:3px;padding:4px 10px;margin:3px;font-size:15px}
details{margin:8px 0}details summary{cursor:pointer;font-weight:700;color:var(--blu)}
.chk label{display:flex;gap:10px;align-items:flex-start;margin:8px 0}.chk input{width:22px;height:22px;flex:0 0 22px;margin-top:3px}
input[type=text]{font:inherit;width:100%;padding:8px 10px;border:2px solid var(--acc);border-radius:10px;background:var(--card);color:var(--fg)}
.mu{color:var(--mu);font-size:.92em}"""


def tri(t, tag='p'):
    return '<%s>%s</%s><%s class="ar" lang="ar" dir="rtl">%s</%s><%s class="zh" lang="zh">%s</%s>' % (tag, t[0], tag, tag, t[1], tag, tag, t[2], tag)


def finestra(f):
    ed = ''.join('<span class="ed">%s</span>' % html.escape(x) for x in f['edits'])
    bu = ''.join('<span class="bu">%s</span>' % html.escape(x) for x in f['bottoni'])
    return ('<div class="win" aria-label="Come sarà il tuo programma"><div class="tb"><span>%s</span><span>_ □ ×</span></div><div class="co">%s'
            '<div class="lb" style="color:%s">%s</div>%s</div></div>') % (html.escape(f['titolo']), ed if f['edits'] and len(f['edits']) > 1 else '', f['colore'], html.escape(f['label']), (ed if len(f['edits']) == 1 else '') + bu)


def pagina(m):
    n = m['n']; P = m['passi']; consegna = consegna_b(n, m['cartella'], m['compito'])
    h = ['<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">',
         '<title>Lazarus ora %d</title><style>%s</style></head><body><main>' % (n, CSS)]
    h.append('<p class="ante"><b>ANTEPRIMA PER IL PROF, non pubblicata.</b> Nessuna pagina dei ragazzi porta qui. Percorso %d di 3 · <a href="./">indice dell\'anteprima</a></p>' % n)
    h.append('<h1>%s</h1><p class="ar" lang="ar" dir="rtl">%s</p><p class="zh" lang="zh">%s</p>' % m['titolo'])
    h.append('<p class="mu">1INF · venerdì 30/10/2026 · %s · progetto <code>%s</code></p>' % (m['ora'], m['cartella']))
    h.append('<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova. · <span lang="ar">اضغط F5 لرؤية النسخة الجديدة.</span> · <span lang="zh">按 F5 查看新版本。</span></p>')
    h.append('<a class="bt b" href="../../1inf-oggi/" target="_blank" rel="noopener">La mia giornata · يومي · 我的一天</a>')
    # nome e avanzamento
    h.append('<section class="card"><h2>Chi sei? · من أنت؟ · 你是谁？</h2><p>Scrivi nome e cognome: serve al cruscotto per vedere a che punto sei.</p>'
             '<p class="ar" lang="ar" dir="rtl">اكتب الاسم واللقب: يحتاجه لوح المتابعة ليعرف أين وصلت.</p><p class="zh" lang="zh">写你的名字和姓：看板用它来知道你做到哪里了。</p>'
             '<input type="text" id="nome" autocomplete="name" placeholder="Nome Cognome"><p class="mu" id="nomeok"></p>'
             '<div class="barra"><i id="barra"></i></div><p id="conta" class="mu"></p></section>')
    h.append('<section class="card"><h2>Che cosa fai in quest\'ora</h2>%s%s</section>' % (tri(m['intro']), finestra(m['finestra'])))
    # facilitato
    fac = '<section class="card" style="border:2px solid #b45309"><h2>Percorso facilitato: 3 passi · المسار الميسّر · 简单路线</h2>'
    fac += tri(T('Per chi oggi fa fatica: fai solo questi 3 passi. Va bene così: è un programma vero.', 'لمن يجد صعوبة اليوم: افعل هذه الخطوات الثلاث فقط. هذا جيد: إنه برنامج حقيقي.', '今天觉得难的同学：只做这 3 步。这样就很好：这是一个真正的程序。'))
    for k, (t, c) in enumerate(m['facile'], 1):
        fac += '<div class="passo" data-p="F%d"><span class="bollo">da fare</span><h2><span class="num">%d</span>Facile %d</h2>%s%s<button class="fb">Fatto! · تم · 完成</button></div>' % (k, k, k, tri(t), pre(c) if c else '')
    fac += '<p class="mu">Per consegnare bastano lo screenshot e unit1.pas: passi C1-C5 in fondo.</p></section>'
    h.append(fac)
    # teoria
    if m.get('teoria'):
        h.append('<section class="card" style="border:3px solid var(--blu)"><h2>Fase 1: teoria e quiz (30 minuti)</h2>')
        h.append(tri(T('Apri la teoria: 6 schede corte, con una domanda dopo ogni scheda. Poi il prof apre il quiz su String e Integer: leggi BENE il codice, un apice cambia tutto.',
                       'افتح النظرية: 6 بطاقات قصيرة، مع سؤال بعد كل بطاقة. ثم يفتح الأستاذ الاختبار عن String و Integer: اقرأ الكود جيداً، علامة اقتباس واحدة تغيّر كل شيء.',
                       '打开理论：6 张短卡片，每张后面一个问题。然后老师打开关于 String 和 Integer 的测验：仔细读代码，一个引号就能改变一切。')))
        h.append('<a class="bt" href="%s" target="_blank" rel="noopener">Teoria e quiz: String e Integer · النظرية والاختبار · 理论和测验</a>' % VERIFICA)
        h.append('<p class="mu" id="moduli-riga">Se il prof vi dà il quiz su Moduli Google, il link arriva su Classroom. · <span lang="ar">إذا أعطاكم الأستاذ الاختبار على Google Moduli، يصل الرابط على Classroom.</span> · <span lang="zh">如果老师用 Google 表单测验，链接会发在 Classroom 上。</span></p></section>')
        h.append('<h2 style="margin-top:22px">Fase 2: l\'esercitazione</h2>')
    else:
        h.append('<section class="card quad">%s</section>' % tri(m['ripasso']))
    for k, (tit, t, c) in enumerate(P, 1):
        h.append('<div class="passo" data-p="%d"><span class="bollo">da fare</span><h2><span class="num">%d</span>%s</h2><p class="ar" lang="ar" dir="rtl">%s</p><p class="zh" lang="zh">%s</p>%s%s<button class="fb">Fatto! · تم · 完成</button></div>'
                 % (k, k, tit[0], tit[1], tit[2], tri(t), pre(c) if c else ''))
    # aiuti
    h.append('<section class="card"><h2>Sei bloccato? Tre aiuti, uno alla volta · ثلاث مساعدات · 三个提示</h2>')
    h.append('<details><summary>Aiuto 1: un indizio</summary>%s</details>' % tri(m['indizio']))
    h.append('<details><summary>Aiuto 2: il pezzo di codice</summary>%s</details>' % pre(m['pezzo']))
    full = open(OUT + '/codice/ora%d_unit1.pas' % n, encoding='utf-8').read()
    h.append('<details><summary>Aiuto 3: tutto unit1.pas</summary>%s%s</details>' % (
        tri(T('Non copiare tutto: le righe in alto le scrive Lazarus da solo quando metti i pezzi nella Form. Tu scrivi solo le righe dentro le procedure.', 'لا تنسخ كل شيء: الأسطر في الأعلى يكتبها Lazarus وحده عندما تضع القطع في الـ Form. أنت تكتب فقط الأسطر داخل الإجراءات.', '不要全部照抄：上面那些行是你往 Form 里放组件时 Lazarus 自己写的。你只写过程里面的那几行。')), pre(full)))
    h.append('</section>')
    h.append('<section class="card"><h2>Spiegalo in 30 secondi</h2>%s</section>' % tri(m['spiega']))
    # consegna
    h.append('<h2 style="margin-top:22px">Consegna: unit1.pas + screenshot · التسليم · 提交</h2>')
    h.append('<section class="card" style="border:3px solid var(--ok)">%s<a class="bt v" href="consegna.html?ora=%d" target="_blank" rel="noopener">Consegna con un bottone · سلّم بزر واحد · 一键提交</a>'
             % (tri(T('Si consegnano SEMPRE due file: <code>unit1.pas</code> (il tuo codice) e lo screenshot del programma che gira. Prima fai lo screenshot (passo C1), poi apri la pagina di consegna: scegli i due file e premi un bottone.',
                      'نسلّم دائماً ملفين: unit1.pas (الكود) ولقطة شاشة للبرنامج وهو يعمل. أولاً خذ لقطة الشاشة (الخطوة C1)، ثم افتح صفحة التسليم: اختر الملفين واضغط زراً واحداً.',
                      '永远提交两个文件：unit1.pas（你的代码）和程序运行时的截图。先截图（C1 步），再打开提交页面：选两个文件，按一个按钮。')), n))
    h.append('<p><b>Se il bottone non funziona:</b> consegna su Classroom con i passi C2-C5 qui sotto. · <span lang="ar">إذا لم يعمل الزر: سلّم على Classroom بالخطوات C2-C5.</span> · <span lang="zh">如果按钮不能用：按下面 C2-C5 步在 Classroom 提交。</span></p></section>')
    for k, (tit, t, c) in enumerate(consegna, 1):
        h.append('<div class="passo" data-p="C%d"><span class="bollo">da fare</span><h2><span class="num">C%d</span>%s</h2><p class="ar" lang="ar" dir="rtl">%s</p><p class="zh" lang="zh">%s</p>%s%s<button class="fb">Fatto! · تم · 完成</button></div>'
                 % (k, k, tit[0], tit[1], tit[2], tri(t), pre(c) if c else ''))
    h.append('<section class="card chk"><h2>Controllo finale: lo so fare? · هل أعرف؟ · 我会了吗？</h2>')
    for k, t in enumerate(m['controllo']):
        h.append('<label><input type="checkbox" data-k="%d"><span>%s<br><span class="ar" lang="ar" dir="rtl" style="display:block">%s</span><span class="zh" lang="zh" style="display:block">%s</span></span></label>' % (k, t[0], t[1], t[2]))
    h.append('</section>')
    h.append('<section class="card"><h2>Da ricopiare sul quaderno · انسخ في الدفتر · 抄在本子上</h2><div class="quad">%s</div></section>' % pre(m['quaderno']))
    h.append(SCRIPT % {'n': n})
    h.append('</main></body></html>')
    return '\n'.join(h)


SCRIPT = """<script>
(function(){
var ORA=%(n)d, K='lab3010-ora'+ORA, KN='lab3010-nome', CONF={};
function prendi(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(x){return d}}
function metti(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(x){}}
var S=prendi(K,{}), NOME=prendi(KN,'')||'', P=[].slice.call(document.querySelectorAll('.passo')), principali=P.filter(function(p){return /^\\d+$/.test(p.dataset.p)});
var inp=document.getElementById('nome'); inp.value=NOME;
inp.addEventListener('change',function(){var v=inp.value.trim().replace(/\\s+/g,' ');if(v.split(' ').length<2){document.getElementById('nomeok').textContent='Scrivi nome e cognome.';return}NOME=v;metti(KN,v);document.getElementById('nomeok').textContent='Ciao '+v+'!';ping(true)});
fetch('config.json?t='+Date.now()).then(function(r){return r.json()}).then(function(c){CONF=c||{}}).catch(function(){});
var ultimo=-1;
function ping(forza){   // stesso segnale di avanzamento delle pagine di teoria (modo «avanzamento», va nel Foglio di riserva)
  if(!CONF.attivo||!CONF.invio||!NOME)return; var fatti=principali.filter(function(p){return S[p.dataset.p]}).length; if(fatti===ultimo&&!forza)return; ultimo=fatti;
  var max=0;principali.forEach(function(p){if(S[p.dataset.p])max=Math.max(max,+p.dataset.p)});
  var tit=max?principali[max-1].querySelector('h2').textContent.replace(/^\\d+/,''):'';
  var facili=['F1','F2','F3'].filter(function(k){return S[k]}).length, cons=['C1','C2','C3','C4','C5'].filter(function(k){return S[k]}).length;
  var d={id:'avz-1inf-lab3010-ora'+ORA,modo:'avanzamento',classe:'1INF',nome:NOME,scheda:max,totale:principali.length,risposte:fatti,titolo:tit,facile:facili,consegna:cons,quando:new Date().toISOString()};
  try{fetch(CONF.invio,{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:'d='+encodeURIComponent(JSON.stringify(d))})}catch(x){}
}
function disegna(){
  var prossimo=null; P.forEach(function(p){var f=!!S[p.dataset.p];p.classList.toggle('fatto',f);p.classList.remove('ora');p.querySelector('.bollo').textContent=f?'FATTO':'da fare';p.querySelector('.fb').textContent=f?'Fatto ✓ (clic per togliere)':'Fatto! · تم · 完成';if(!f&&!prossimo&&/^\\d+$/.test(p.dataset.p))prossimo=p});
  if(prossimo){prossimo.classList.add('ora');prossimo.querySelector('.bollo').textContent='ADESSO'}
  var n=principali.filter(function(p){return S[p.dataset.p]}).length;document.getElementById('barra').style.width=Math.round(100*n/principali.length)+'%%';
  document.getElementById('conta').textContent='Passi fatti: '+n+' su '+principali.length;
}
P.forEach(function(p){p.querySelector('.fb').onclick=function(){S[p.dataset.p]=!S[p.dataset.p];metti(K,S);disegna();ping(false)}});
var C=prendi(K+'-chk',{});[].forEach.call(document.querySelectorAll('.chk input'),function(c){c.checked=!!C[c.dataset.k];c.onchange=function(){C[c.dataset.k]=c.checked;metti(K+'-chk',C)}});
disegna();setInterval(function(){ping(true)},120000);
})();
</script>"""


def md(m):
    n = m['n']; L = ['# %s' % m['titolo'][0], '', '**Versione 1.0** — 29/10/2026 — ANTEPRIMA per il prof, non pubblicata', '',
                     '*1INF · Laboratorio · venerdì 30/10/2026, %s · progetto `%s` · si consegnano SEMPRE unit1.pas e lo screenshot*' % (m['ora'], m['cartella']), '',
                     m['titolo'][1], '', m['titolo'][2], '', '## 01 Che cosa fai in quest\'ora', '']
    def t3(t): return [t[0], '', t[1], '', t[2], '']
    L += t3(m['intro'])
    if m.get('teoria'):
        L += ['## 02 Fase 1: teoria e quiz', '', '1. Teoria in 6 schede con le domande di ripasso: pagina `docs/verifica/?b=%s`.' % BANCA_ID,
              '2. Quiz di 22 domande su String e Integer: su Moduli Google (piano A) oppure nella stessa pagina, modo verifica (piano B).', '']
        for k, (tit, testi, cod) in enumerate(SCHEDE, 1):
            L += ['### 02.%d %s' % (k, tit[0]), '']
            for t in testi: L += t3(t)
            L += ['```', cod, '```', '']
    else:
        L += ['## 02 Ripasso in 1 minuto', ''] + t3(m['ripasso'])
    L += ['## 03 Percorso facilitato (3 passi)', '']
    for k, (t, c) in enumerate(m['facile'], 1):
        L += ['%d. %s' % (k, t[0]), '', '    ' + t[1], '', '    ' + t[2], '']
        if c: L += ['    ```', '\n'.join('    ' + x for x in c.split('\n')), '    ```', '']
    L += ['## 04 L\'esercitazione, passo per passo', '']
    for k, (tit, t, c) in enumerate(m['passi'], 1):
        L += ['%d. **%s.** %s' % (k, tit[0], t[0]), '', '    ' + t[1], '', '    ' + t[2], '']
        if c: L += ['    ```', '\n'.join('    ' + x for x in c.split('\n')), '    ```', '']
    L += ['## 05 Tre aiuti', '', '1. Indizio: ' + m['indizio'][0], '2. Il pezzo di codice:', '', '    ```', '\n'.join('    ' + x for x in m['pezzo'].split('\n')), '    ```', '',
          '3. Tutto unit1.pas: `codice/ora%d_unit1.pas`.' % n, '', '## 06 Spiegalo in 30 secondi', ''] + t3(m['spiega'])
    L += ['## 07 Consegna: unit1.pas + screenshot', '', '1. Piano A: pagina `consegna.html?ora=%d`: scegli unit1.pas e lo screenshot, il controllo automatico dice subito se il codice va bene, un bottone manda tutto.' % n,
          '2. Piano B, se il bottone non funziona: Classroom, passi C1-C5.', '']
    for k, (tit, t, c) in enumerate(consegna_b(n, m['cartella'], m['compito']), 1):
        L += ['    %d. **C%d %s.** %s' % (k, k, tit[0], t[0]), '']
        if c: L += ['        ```', '        ' + c, '        ```', '']
    L += ['## 08 Controllo finale', ''] + ['%d. %s' % (k, t[0]) for k, t in enumerate(m['controllo'], 1)] + ['', '## 09 Da ricopiare sul quaderno', '', '```', m['quaderno'], '```', '']
    return '\n'.join(L)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for n, m in M.items():
        open(OUT + '/modulo-%d.html' % n, 'w', encoding='utf-8').write(pagina(m))
        open(OUT + '/modulo-%d.md' % n, 'w', encoding='utf-8').write(md(m))
    B = banca()
    open(PUB + '/docs/verifica/banche/' + BANCA_ID + '.js', 'w', encoding='utf-8').write(
        '// 1INF · 30/10/2026: String e Integer. APERTA ai ragazzi alle 06:45 (Tecnologia 8-9, parte 2 della lezione Unicode, e laboratorio): teoria e ripasso; il quiz è su Moduli. Generato da classe-1/lazarus-lab-30-10/_build/genera.py\nwindow.BANCA = ' + json.dumps(B, ensure_ascii=False, indent=1) + ';\n')
    st = PUB + '/docs/verifica/stato/' + BANCA_ID + '.json'
    if not os.path.exists(st):
        json.dump({'verifica': 'chiusa', 'recupero': 'chiuso', 'recupero_per': [], '_nota': '29/10: anteprima per il prof. La verifica (22 crocette + 3 aperte) si apre solo con il suo via.'}, open(st, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(moduli_quiz(), open(OUT + '/quiz-moduli.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok: 3 moduli, banca', BANCA_ID, 'crocette', len(CROCETTE), 'aperte', len(APERTE))
