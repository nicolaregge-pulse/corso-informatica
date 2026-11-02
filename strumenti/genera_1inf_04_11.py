#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1INF mercoledì 04/11/2026, Laboratorio 8-11, tre ore: esercizi Lazarus UTILI con stringhe e interi.
# Ora 1 Convertitore di misure · Ora 2 Calcolatrice a 4 bottoni (StrToIntDef) · Ora 3 Il cassiere (div, mod, stringhe).
# Voce Allegato A (PFP_1, Comp. 15, I anno): «Programmazione a eventi con Lazarus (Free Pascal): form, componenti, proprietà, gestori di evento».
# Scrive docs/anteprima/1inf-lab-04-11/ (tutto CHIUSO: ore_sbloccate 0). Nessun nome di ragazzi.
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_pagine_lezione import *

SLUG = '1inf-lab-04-11'
D = SLUGDIR + SLUG + '/'
os.makedirs(D + 'img', exist_ok=True); os.makedirs(D + 'codice', exist_ok=True)

# ---------- codice di riferimento (serve anche per provare il controllo automatico) ----------
def unit(comps, handlers, uses_extra=''):
    campi = ''.join('    %s: %s;\n' % (n, t) for n, t in comps)
    procs = ''.join('    procedure %sClick(Sender: TObject);\n' % h for h, _ in handlers)
    corpi = ''.join('procedure TForm1.%sClick(Sender: TObject);\n%s\n' % (h, b.strip('\n') + '\n') for h, b in handlers)
    return ('unit Unit1;\n\n{$mode objfpc}{$H+}\n\ninterface\n\nuses\n  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;\n\ntype\n\n  { TForm1 }\n\n  TForm1 = class(TForm)\n'
            + campi + procs + '  private\n\n  public\n\n  end;\n\nvar\n  Form1: TForm1;\n\nimplementation\n\n{$R *.lfm}\n\n{ TForm1 }\n\n' + corpi + '\nend.\n')

def pr(h, b):
    return 'procedure TForm1.%sClick(Sender: TObject);\n' % h + b

def blocco(var, corpo):
    return 'var\n  %s\nbegin\n%s\nend;\n' % (var, corpo)

B1 = blocco('km, metri: Integer;', "  km := StrToInt(Edit1.Text);\n  metri := km * 1000;\n  Label1.Caption := IntToStr(metri) + ' metri';")
B2 = blocco('ore, minuti: Integer;', "  ore := StrToInt(Edit1.Text);\n  minuti := ore * 60;\n  Label1.Caption := IntToStr(minuti) + ' minuti';")
B3 = blocco('euro, centesimi: Integer;', "  euro := StrToInt(Edit1.Text);\n  centesimi := euro * 100;\n  Label1.Caption := IntToStr(centesimi) + ' centesimi';")
B4 = blocco('c, f: Integer;', "  c := StrToInt(Edit1.Text);\n  f := c * 9 div 5 + 32;\n  Label1.Caption := IntToStr(c) + ' gradi C sono ' + IntToStr(f) + ' gradi F';")
B5 = blocco('minuti, ore, resto: Integer;', "  minuti := StrToInt(Edit1.Text);\n  ore := minuti div 60;\n  resto := minuti mod 60;\n  Label1.Caption := IntToStr(minuti) + ' minuti sono ' + IntToStr(ore) + ' ore e ' + IntToStr(resto) + ' minuti';")
COMP1 = [('Button1', 'TButton'), ('Button2', 'TButton'), ('Button3', 'TButton'), ('Button4', 'TButton'), ('Button5', 'TButton'), ('Edit1', 'TEdit'), ('Label1', 'TLabel')]
open(D + 'codice/ora1_unit1.pas', 'w', encoding='utf-8').write(unit(COMP1, [('Button1', B1), ('Button2', B2), ('Button3', B3), ('Button4', B4), ('Button5', B5)]))

def ab(var, corpo_frase):
    return blocco('a, b: Integer;', "  a := StrToIntDef(Edit1.Text, 0);\n  b := StrToIntDef(Edit2.Text, 0);\n" + corpo_frase)
C_PIU = "  Label1.Caption := IntToStr(a) + ' più ' + IntToStr(b) + ' fa ' + IntToStr(a + b);"
C_MENO = "  Label1.Caption := IntToStr(a) + ' meno ' + IntToStr(b) + ' fa ' + IntToStr(a - b);"
C_PER = "  Label1.Caption := IntToStr(a) + ' per ' + IntToStr(b) + ' fa ' + IntToStr(a * b);"
C_DIV = ("  if b = 0 then\n    Label1.Caption := 'Non si può dividere per zero'\n  else\n"
         "    Label1.Caption := IntToStr(a) + ' diviso ' + IntToStr(b) + ' fa ' + IntToStr(a div b);")
COMP2 = [('Button1', 'TButton'), ('Button2', 'TButton'), ('Button3', 'TButton'), ('Button4', 'TButton'), ('Edit1', 'TEdit'), ('Edit2', 'TEdit'), ('Label1', 'TLabel')]
open(D + 'codice/ora2_unit1.pas', 'w', encoding='utf-8').write(unit(COMP2, [('Button1', ab('', C_PIU)), ('Button2', ab('', C_MENO)), ('Button3', ab('', C_PER)), ('Button4', ab('', C_DIV))]))

B_CASS = blocco('prezzo, dati, resto, b10, b5, m2, m1: Integer;',
    "  prezzo := StrToIntDef(Edit2.Text, 0);\n  dati := StrToIntDef(Edit3.Text, 0);\n  resto := dati - prezzo;\n"
    "  b10 := resto div 10;\n  resto := resto mod 10;\n  b5 := resto div 5;\n  resto := resto mod 5;\n  m2 := resto div 2;\n  m1 := resto mod 2;\n"
    "  Memo1.Clear;\n  Memo1.Lines.Add('SCONTRINO');\n  Memo1.Lines.Add('Cliente: ' + Edit1.Text);\n  Memo1.Lines.Add('Prezzo: ' + IntToStr(prezzo) + ' euro');\n"
    "  Memo1.Lines.Add('Dati: ' + IntToStr(dati) + ' euro');\n  Memo1.Lines.Add('Resto: ' + IntToStr(dati - prezzo) + ' euro');\n"
    "  Memo1.Lines.Add(IntToStr(b10) + ' banconote da 10, ' + IntToStr(b5) + ' da 5');\n  Memo1.Lines.Add(IntToStr(m2) + ' monete da 2, ' + IntToStr(m1) + ' da 1');")
COMP3 = [('Button1', 'TButton'), ('Edit1', 'TEdit'), ('Edit2', 'TEdit'), ('Edit3', 'TEdit'), ('Label1', 'TLabel'), ('Memo1', 'TMemo')]
open(D + 'codice/ora3_unit1.pas', 'w', encoding='utf-8').write(unit(COMP3, [('Button1', B_CASS)]))

# ---------- schemi (regola 32) ----------
def S(n, titolo, items, hl=(), nota=''): svg(D + 'img/' + n, titolo, items, hl, nota)
S('nuovo-progetto.svg', 'Lazarus: nuovo progetto', [('menu', ['File', 'Progetto  ▸', 'Esegui'], 40, 70), ('menu', ['Nuovo progetto…', 'Salva progetto con nome…'], 360, 70), ('box', 'Scegli: Applicazione\npoi OK', 360, 200, 380, 90)], (1, 2), 'Progetto → Nuovo progetto… → Applicazione → OK')
S('salva-progetto.svg', 'Salva progetto con nome', [('lbl', 'Cartella: Documenti ▸ convertitore', 40, 90), ('edit', 'convertitore', 40, 140, 420), ('btn', 'Salva', 500, 140, 160), ('box', 'Prima: Documenti → Nuova cartella\nPoi: nome file e Salva (2 volte)', 40, 230, 620, 100)], (1, 2), 'Il nome della cartella è scritto sul passo')
S('palette.svg', 'Lazarus: palette Standard', [('box', 'Standard | Additional | Common', 40, 70, 700, 50), ('btn', 'Button', 60, 150, 140), ('edit', 'Edit', 240, 150, 140), ('lbl', 'Label', 420, 180), ('box', 'Clic sul componente,\npoi clic sulla Form', 40, 260, 460, 90)], (1, 2, 3), 'Clicca il componente, poi clicca sulla finestra grigia')
S('ispettore.svg', 'Ispettore oggetti: Caption', [('box', 'Button1\nCaption  [ Km in metri ]\nName  Button1', 40, 70, 360, 130), ('btn', 'Km in metri', 480, 110, 240), ('arrow', 400, 135, 470, 135)], (0,), 'Cambia Caption: il bottone cambia scritta')
S('doppio-clic.svg', 'Doppio clic sul bottone', [('btn', 'Km in metri', 280, 150, 240), ('arrow', 400, 300, 400, 205), ('box', 'DOPPIO CLIC sul bottone:\nsi apre il codice', 180, 310, 440, 90)], (0, 2), 'Doppio clic = si apre la procedura')
S('prova-f9.svg', 'Premi F9: il programma parte', [('edit', '5', 40, 90, 300), ('btn', 'Km in metri', 360, 90, 220), ('lbl', '5000 metri', 40, 220), ('box', 'Scrivi 5 e premi il bottone:\ncompare 5000 metri', 40, 300, 560, 90)], (3, 2), 'FATTO! Se vedi 5000 metri, funziona')
S('ris-ora1.svg', 'Il convertitore finito', [('edit', '135', 40, 80, 200), ('btn', 'Km in metri', 40, 140, 200), ('btn', 'Ore in minuti', 260, 140, 200), ('btn', 'Euro in centesimi', 480, 140, 240), ('btn', 'Celsius in Fahrenheit', 40, 200, 280), ('btn', 'Minuti in ore', 340, 200, 220), ('lbl', '135 minuti sono 2 ore e 15 minuti', 40, 320)], (5,), 'Cinque bottoni, un risultato')
S('form-calc.svg', 'La calcolatrice: i componenti', [('edit', '', 40, 80, 220), ('edit', '', 290, 80, 220), ('btn', '+', 40, 150, 100), ('btn', '-', 160, 150, 100), ('btn', '*', 280, 150, 100), ('btn', '/', 400, 150, 100), ('lbl', 'Label1', 40, 260)], (0, 1), '2 Edit, 4 Button, 1 Label')
S('ris-ora2.svg', 'La calcolatrice finita', [('edit', '7', 40, 80, 220), ('edit', '5', 290, 80, 220), ('btn', '+', 40, 150, 100), ('btn', '-', 160, 150, 100), ('btn', '*', 280, 150, 100), ('btn', '/', 400, 150, 100), ('lbl', '7 più 5 fa 12', 40, 270)], (6,), 'Il risultato è una frase')
S('div-zero.svg', 'Divisione per zero', [('edit', '8', 40, 80, 220), ('edit', '0', 290, 80, 220), ('btn', '/', 400, 150, 100), ('lbl', 'Non si può dividere per zero', 40, 260)], (3,), 'Con if il programma non si blocca')
S('form-cass.svg', 'Il cassiere: i componenti', [('edit', 'nome cliente', 40, 80, 280), ('edit', 'prezzo', 340, 80, 180), ('edit', 'soldi dati', 540, 80, 180), ('btn', 'Calcola il resto', 40, 140, 280), ('memo', '', 40, 210, 680, 190)], (4,), '3 Edit, 1 Button, 1 Memo')
S('ris-ora3.svg', 'Lo scontrino finito', [('memo', 'SCONTRINO\nCliente: Maria\nPrezzo: 13 euro\nDati: 50 euro\nResto: 37 euro\n3 banconote da 10, 1 da 5\n1 monete da 2, 0 da 1', 40, 70, 680, 250)], (0,), 'Lo scontrino con il TUO nome')
S('salva.svg', 'Salva con Ctrl + S', [('box', 'Ctrl + S\n(tieni premuto Ctrl, premi S)', 160, 120, 480, 100), ('box', 'Vale per tutti i file del progetto', 160, 250, 480, 60)], (0,), 'Salva SEMPRE prima di consegnare')
S('screenshot.svg', 'Screenshot: Win + Shift + S', [('box', 'Win + Shift + S\ntrascina sul programma che gira', 120, 100, 560, 100), ('box', 'Poi incolla in Paint (Ctrl+V)\ne salva nella cartella del progetto', 120, 230, 560, 100)], (0,), 'Nome file: oraN_screenshot.png')
S('consegna.svg', 'Consegna', [('box', 'Premi il bottone verde\nManda al prof', 120, 90, 560, 100), ('btn', 'Manda al prof', 160, 230, 480)], (1,), 'Scegli unit1.pas e lo screenshot')
S('quiz.svg', 'Quiz su Google Moduli', [('box', 'Quiz breve: testo contro numero\n8 domande · 3 minuti', 120, 90, 560, 100), ('btn', 'Apri il quiz', 160, 230, 480)], (1,), 'Rispondi e premi Invia')
S('quaderno.svg', 'Il quaderno', [('box', 'Ricopia sul quaderno\nle righe del riquadro nero', 120, 100, 560, 100), ('box', 'Scrivi a mano: ti aiuta a ricordare', 120, 230, 560, 70)], (0,), 'Carta e penna sul banco')
S('fallo-tuo.svg', 'Fallo tuo', [('box', 'Cambia la scritta del bottone,\nil titolo della finestra,\nil colore dello sfondo', 100, 90, 600, 130), ('box', 'Aggiungi UN bottone con la tua idea', 100, 250, 600, 70)], (0,), 'Questo è il tuo programma')
for n in (1, 2, 3):
    codesvg(D + 'img/codice-%d.svg' % n, 'Il codice dell\'ora %d' % n, open(D + 'codice/ora%d_unit1.pas' % n, encoding='utf-8').read().split('{ TForm1 }')[2].split('\nend.')[0].strip(), 'Esempio del codice di un bottone')

# ---------- passi per ora ----------
def T(it, ar, zh): return it, {'ar': ar, 'zh': zh}
def P(t, x, img, alt='', code=None, extra=None):
    ti, tl = t; xi, xl = x
    return dict(t=ti, tl=tl, x=xi, xl=xl, img=img, alt=alt, code=code, extra=extra)

Q_QUAD = lambda righe: '<div class="quad"><b>QUADERNO · ricopia a mano · انسخ في الدفتر · 抄在本子上</b><pre><span class="t">%s</span></pre></div>' % E(righe)
NOTA_FAC = ('<details class="card"><summary>Percorso facilitato (se sei indietro): solo %s</summary><p>%s</p><p class="ar" lang="ar" dir="rtl">%s</p><p class="zh" lang="zh">%s</p></details>')

SALVA_SHOT = lambda n: [
    P(T('Salva tutto', 'احفظ كل شيء', '保存全部'), T('Premi <b>Ctrl + S</b>. FATTO!', 'اضغط Ctrl + S. تمّ!', '按 Ctrl + S。完成！'), 'salva.svg', 'Ctrl + S'),
    P(T('Fai lo screenshot', 'التقط لقطة الشاشة', '截图'), T('Con il programma che gira premi <b>Win + Shift + S</b>, trascina sul programma, incolla in Paint e salva nella cartella del progetto con il nome <code>ora%d_screenshot.png</code>.' % n, 'والبرنامج يعمل اضغط Win + Shift + S، ثم الصقها في Paint واحفظها في مجلد المشروع باسم ora%d_screenshot.png.' % n, '程序运行时按 Win + Shift + S，在 Paint 里粘贴，保存到项目文件夹，文件名 ora%d_screenshot.png。' % n), 'screenshot.svg', 'Win Shift S'),
    P(T('Manda al prof', 'أرسل إلى الأستاذ', '发给老师'), T('Premi il bottone: scegli <code>unit1.pas</code> e lo screenshot e premi «Manda al prof». FATTO!', 'اضغط الزر: اختر unit1.pas ولقطة الشاشة ثم «Manda al prof».', '按按钮：选择 unit1.pas 和截图，再按「Manda al prof」。'), 'consegna.svg', 'Consegna',
      extra='<a class="bt v" href="consegna.html?ora=%d">Manda al prof ora %d · أرسل · 发送</a>' % (n, n))]

NUOVO = lambda cart, nome: [
    P(T('Crea il progetto', 'أنشئ المشروع', '新建项目'), T('In Lazarus: menu <b>Progetto</b> → <b>Nuovo progetto…</b> → <b>Applicazione</b> → <b>OK</b>. Compare una finestra grigia (<b>Form1</b>). FATTO!', 'في Lazarus: Progetto ← Nuovo progetto… ← Applicazione ← OK. تظهر نافذة رمادية (Form1).', '在 Lazarus 里：Progetto → Nuovo progetto… → Applicazione → OK。出现灰色窗口（Form1）。'), 'nuovo-progetto.svg', 'Nuovo progetto'),
    P(T('Salva il progetto in Documenti', 'احفظ المشروع في Documenti', '把项目保存到 Documenti'), T('Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Clicca <b>Documenti</b>, poi <b>Nuova cartella</b> e dai alla cartella il nome <code>%s</code>. Entra nella cartella e scrivi <code>%s</code> in <b>Nome file</b>, poi <b>Salva</b>; per <code>unit1.pas</code> clicca ancora <b>Salva</b>.' % (cart, nome), 'Progetto ← Salva progetto con nome… . اضغط Documenti ثم مجلد جديد باسم %s. ادخل المجلد واكتب %s ثم Salva (مرتين).' % (cart, nome), 'Progetto → Salva progetto con nome…。点 Documenti，新建文件夹，名字 %s。进入文件夹，文件名写 %s，点 Salva（两次）。' % (cart, nome)), 'salva-progetto.svg', 'Salva progetto')]

PASSI1 = [
    P(T('Quiz breve: testo contro numero (3 minuti)', 'اختبار قصير: نص أم رقم (3 دقائق)', '小测验：文字还是数字（3 分钟）'), T('Prima di cominciare: 8 domande su <code>\'5\' + \'3\'</code> contro <code>5 + 3</code>. Premi il bottone verde, rispondi e premi <b>Invia</b>. FATTO!', 'قبل أن نبدأ: 8 أسئلة عن \'5\' + \'3\' مقابل 5 + 3. اضغط الزر الأخضر وأجب ثم Invia.', '开始前：8 道题，比较 \'5\' + \'3\' 和 5 + 3。按绿色按钮，回答后按 Invia。'), 'quiz.svg', 'Quiz Moduli',
      extra='<a class="bt v" href="__QUIZ1__" target="_blank" rel="noopener">Apri il quiz · افتح الاختبار · 打开测验</a>')] + NUOVO('convertitore', 'convertitore') + [
    P(T('Metti i componenti: Edit, Label e UN bottone', 'ضع المكونات: Edit و Label وزر واحد', '放组件：Edit、Label 和一个按钮'), T('Nella palette <b>Standard</b> clicca <b>TEdit</b> e poi sulla Form; poi <b>TLabel</b>; poi <b>TButton</b>. FATTO!', 'من لوحة Standard اضغط TEdit ثم على النافذة؛ ثم TLabel؛ ثم TButton.', '在 Standard 面板点 TEdit 再点窗口；然后 TLabel；然后 TButton。'), 'palette.svg', 'Palette'),
    P(T('Cambia la scritta del bottone', 'غيّر كتابة الزر', '改按钮上的字'), T('Clicca il bottone. A sinistra, nell\'<b>Ispettore oggetti</b>, trova <b>Caption</b> e scrivi <code>Km in metri</code>. Cancella il testo di <b>Edit1</b> (proprietà <b>Text</b>). FATTO!', 'اضغط الزر. في Ispettore oggetti ابحث عن Caption واكتب Km in metri. امسح نص Edit1 (Text).', '点按钮。在左边「Ispettore oggetti」找到 Caption，写 Km in metri。清空 Edit1 的 Text。'), 'ispettore.svg', 'Caption'),
    P(T('Apri il codice del bottone', 'افتح كود الزر', '打开按钮的代码'), T('Fai <b>doppio clic</b> sul bottone: si apre il codice. FATTO!', 'انقر مرتين على الزر: يفتح الكود.', '双击按钮：打开代码。'), 'doppio-clic.svg', 'Doppio clic'),
    P(T('Scrivi il primo convertitore: km in metri', 'اكتب أول محوّل: كم إلى متر', '写第一个换算：公里变米'), T('Lazarus ha già scritto la riga <code>procedure…</code>, <code>begin</code> e <code>end;</code>: tu completa così. <code>StrToInt</code> trasforma il testo in numero, <code>IntToStr</code> il numero in testo.', 'StrToInt يحوّل النص إلى رقم، و IntToStr يحوّل الرقم إلى نص.', 'StrToInt 把文字变成数字，IntToStr 把数字变回文字。'), 'codice-1.svg', 'Codice km', code=pr('Button1', B1)),
    P(T('Provalo con F9', 'جرّبه بـ F9', '按 F9 试试'), T('Premi <b>F9</b>. Scrivi <code>5</code> e premi il bottone: deve comparire <b>5000 metri</b>. FATTO! Prima vittoria!', 'اضغط F9. اكتب 5 واضغط الزر: يجب أن يظهر 5000 metri. أول انتصار!', '按 F9。写 5，按按钮：应出现 5000 metri。第一次胜利！'), 'prova-f9.svg', 'F9 5000 metri'),
    P(T('Secondo e terzo bottone: ore e euro', 'الزر الثاني والثالث: ساعات ويورو', '第二、三个按钮：小时和欧元'), T('Aggiungi due bottoni (<code>Ore in minuti</code>, <code>Euro in centesimi</code>) con lo stesso metodo. Il codice di <b>Ore in minuti</b>:', 'أضف زرين بنفس الطريقة. كود الساعات:', '用同样的方法加两个按钮。小时的代码：'), 'codice-1.svg', 'Codice ore', code=pr('Button2', B2) + '\n// Euro in centesimi: stessa cosa con  * 100'),
    P(T('Quarto bottone: Celsius in Fahrenheit', 'الزر الرابع: سيلسيوس إلى فهرنهايت', '第四个按钮：摄氏变华氏'), T('<code>div</code> è la divisione <b>senza virgola</b>. La formula è <code>C * 9 div 5 + 32</code>. Prova con 100: deve fare 212.', 'div هي القسمة بدون فاصلة. الصيغة: C * 9 div 5 + 32. جرّب 100: النتيجة 212.', 'div 是不带小数的除法。公式：C * 9 div 5 + 32。试 100：得 212。'), 'codice-1.svg', 'Codice Celsius', code=pr('Button4', B4)),
    P(T('Quinto bottone: minuti in ore e minuti', 'الزر الخامس: دقائق إلى ساعات ودقائق', '第五个按钮：分钟变小时和分钟'), T('<code>div</code> dà le ore intere, <code>mod</code> dà quello che avanza. Prova con 135: <b>2 ore e 15 minuti</b>.', 'div تعطي الساعات الكاملة و mod تعطي الباقي. جرّب 135: ساعتان و15 دقيقة.', 'div 得到整小时，mod 得到剩下的。试 135：2 小时 15 分钟。'), 'ris-ora1.svg', 'Cinque bottoni', code=pr('Button5', B5)),
    P(T('Fallo tuo', 'اجعله لك', '做成你自己的'), T('Cambia la scritta del bottone e il titolo della finestra (proprietà <b>Caption</b> della Form), scegli un colore (<b>Color</b>) e aggiungi UN bottone con una conversione che piace a te. FATTO!', 'غيّر كتابة الزر وعنوان النافذة واختر لوناً وأضف زراً بتحويل تحبه.', '改按钮文字和窗口标题，选一个颜色，再加一个你喜欢的换算按钮。'), 'fallo-tuo.svg', 'Fallo tuo'),
    P(T('Sul quaderno', 'في الدفتر', '写在本子上'), T('Ricopia sul quaderno il riquadro giallo.', 'انسخ المربع الأصفر في الدفتر.', '把黄色框抄在本子上。'), 'quaderno.svg', 'Quaderno',
      extra=Q_QUAD("String = testo  '53'\nInteger = numero  53\ndiv = divisione senza virgola   17 div 5 = 3\nmod = quello che avanza    17 mod 5 = 2\nC * 9 div 5 + 32 = Fahrenheit")),
] + SALVA_SHOT(1)

PASSI2 = NUOVO('calcolatrice', 'calcolatrice') + [
    P(T('Metti i componenti: 2 Edit, 4 bottoni, 1 Label', 'ضع المكونات: خانتا Edit و4 أزرار وLabel', '放组件：2 个 Edit、4 个按钮、1 个 Label'), T('Dalla palette <b>Standard</b>: due <b>TEdit</b>, quattro <b>TButton</b> e una <b>TLabel</b>. Cambia le <b>Caption</b> dei bottoni in <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>. Cancella il <b>Text</b> dei due Edit. FATTO!', 'من لوحة Standard: خانتا TEdit وأربعة TButton وTLabel. غيّر Caption الأزرار إلى + - * /. امسح Text في الخانتين.', '从 Standard 面板放：两个 TEdit、四个 TButton、一个 TLabel。按钮的 Caption 改成 + - * /。清空两个 Edit 的 Text。'), 'form-calc.svg', 'Componenti'),
    P(T('Il bottone più: StrToIntDef', 'زر الجمع: StrToIntDef', '加号按钮：StrToIntDef'), T('Doppio clic sul bottone <b>+</b>. <code>StrToIntDef(testo, 0)</code> legge il numero e, se la casella è vuota o ci sono lettere, usa <b>0</b> invece di bloccarsi.', 'StrToIntDef يقرأ الرقم وإذا كانت الخانة فارغة أو فيها حروف يستعمل 0 بدل أن يتوقف.', 'StrToIntDef 读取数字；如果框是空的或有字母，就用 0，不会卡住。'), 'codice-2.svg', 'Codice più', code=pr('Button1', ab('', C_PIU))),
    P(T('Provalo: 7 più 5', 'جرّبه: 7 زائد 5', '试试：7 加 5'), T('Premi <b>F9</b>, scrivi <code>7</code> e <code>5</code>, premi <b>+</b>: compare la frase <b>7 più 5 fa 12</b>. FATTO!', 'اضغط F9 واكتب 7 و5 ثم +: تظهر الجملة 7 più 5 fa 12.', '按 F9，写 7 和 5，按 +：出现句子 7 più 5 fa 12。'), 'ris-ora2.svg', '7 più 5 fa 12'),
    P(T('Il bottone meno', 'زر الطرح', '减号按钮'), T('Stesso metodo: cambia solo l\'operazione e la parola.', 'نفس الطريقة: غيّر العملية والكلمة فقط.', '同样的方法：只改运算和单词。'), 'codice-2.svg', 'Codice meno', code=pr('Button1', ab('', C_MENO))),
    P(T('Il bottone per', 'زر الضرب', '乘号按钮'), T('Stesso metodo con <code>*</code>.', 'نفس الطريقة مع *.', '同样的方法，用 *。'), 'codice-2.svg', 'Codice per', code=pr('Button1', ab('', C_PER))),
    P(T('Il bottone diviso (bonus: zero)', 'زر القسمة (إضافي: الصفر)', '除号按钮（加分：零）'), T('Con i numeri interi si usa <code>div</code>. Con <code>if</code> controlli lo <b>zero</b>: non si può dividere per zero. Prova <code>8</code> e <code>0</code>.', 'مع الأعداد الصحيحة نستعمل div. مع if نفحص الصفر: لا يمكن القسمة على صفر.', '整数用 div。用 if 检查零：不能除以零。试 8 和 0。'), 'div-zero.svg', 'Divisione per zero', code=pr('Button1', ab('', C_DIV))),
    P(T('Fallo tuo', 'اجعله لك', '做成你自己的'), T('Cambia titolo della finestra, colori e le frasi (per esempio «sommato a»). FATTO!', 'غيّر عنوان النافذة والألوان والجمل.', '改窗口标题、颜色和句子。'), 'fallo-tuo.svg', 'Fallo tuo'),
    P(T('Sul quaderno', 'في الدفتر', '写在本子上'), T('Ricopia sul quaderno il riquadro giallo.', 'انسخ المربع الأصفر في الدفتر.', '把黄色框抄在本子上。'), 'quaderno.svg', 'Quaderno',
      extra=Q_QUAD("StrToIntDef(Edit1.Text, 0)  = numero, se non va usa 0\nIntToStr(a + b)  = numero che diventa testo\nif b = 0 then ... else ...  = se... altrimenti...")),
] + SALVA_SHOT(2)

PASSI3 = NUOVO('cassiere', 'cassiere') + [
    P(T('Metti i componenti: 3 Edit, 1 bottone, 1 Memo', 'ضع المكونات: 3 Edit وزر وMemo', '放组件：3 个 Edit、1 个按钮、1 个 Memo'), T('Dalla palette <b>Standard</b>: tre <b>TEdit</b> (nome cliente, prezzo, soldi dati), un <b>TButton</b> con Caption <code>Calcola il resto</code>, un <b>TMemo</b> grande per lo scontrino (nel Memo svuota la proprietà <b>Lines</b>). FATTO!', 'من Standard: ثلاث خانات TEdit (اسم الزبون والسعر والمبلغ المدفوع) وزر Calcola il resto وTMemo كبير للإيصال.', '从 Standard 放：三个 TEdit（顾客名字、价格、给的钱）、一个按钮 Calcola il resto、一个大 TMemo 当小票。'), 'form-cass.svg', 'Componenti'),
    P(T('Prima il resto: soldi dati meno prezzo', 'أولاً الباقي: المبلغ ناقص السعر', '先算找零：给的钱减价格'), T('Doppio clic sul bottone. Scrivi solo le prime righe: leggi i due numeri con <code>StrToIntDef</code> e calcola <code>dati - prezzo</code>.', 'انقر مرتين على الزر. اكتب الأسطر الأولى فقط: اقرأ الرقمين واحسب dati - prezzo.', '双击按钮。先只写前几行：读两个数字，计算 dati - prezzo。'), 'codice-3.svg', 'Resto', code=blocco('prezzo, dati, resto: Integer;', "  prezzo := StrToIntDef(Edit2.Text, 0);\n  dati := StrToIntDef(Edit3.Text, 0);\n  resto := dati - prezzo;\n  Label1.Caption := 'Resto: ' + IntToStr(resto) + ' euro';")),
    P(T('Banconote e monete con div e mod', 'الأوراق والعملات بـ div و mod', '用 div 和 mod 算钞票和硬币'), T('<code>div</code> conta quante banconote, <code>mod</code> dice quanto avanza. Si fa a gradini: prima da 10, poi da 5, poi da 2, poi da 1. Con resto 37: 3 da 10, 1 da 5, 1 da 2, 0 da 1.', 'div تعدّ كم ورقة، و mod تقول كم يتبقى. نبدأ من 10 ثم 5 ثم 2 ثم 1.', 'div 数有几张，mod 说还剩多少。先 10，再 5，再 2，再 1。'), 'codice-3.svg', 'Banconote', code=B_CASS.split("  Memo1.Clear;")[0]),
    P(T('Lo scontrino con il nome del cliente', 'الإيصال مع اسم الزبون', '带顾客名字的小票'), T('Con <code>+</code> unisci le <b>stringhe</b>: <code>\'Cliente: \' + Edit1.Text</code>. Ogni <code>Memo1.Lines.Add</code> aggiunge una riga. Prova: Maria, 13, 50.', 'بعلامة + نلصق النصوص. كل Memo1.Lines.Add يضيف سطراً. جرّب: Maria و13 و50.', '用 + 连接字符串。每个 Memo1.Lines.Add 加一行。试：Maria、13、50。'), 'ris-ora3.svg', 'Scontrino', code=B_CASS.split("  b10 := resto div 10;")[0].replace("  resto := dati - prezzo;\n", "") + "...\n  Memo1.Clear;\n  Memo1.Lines.Add('SCONTRINO');\n  Memo1.Lines.Add('Cliente: ' + Edit1.Text);\n  Memo1.Lines.Add('Prezzo: ' + IntToStr(prezzo) + ' euro');"),
    P(T('Fallo tuo', 'اجعله لك', '做成你自己的'), T('Dai un nome al tuo negozio e scrivilo in cima allo scontrino (<code>Memo1.Lines.Add(\'NEGOZIO DI ...\')</code>). FATTO!', 'أعط اسماً لمتجرك واكتبه أعلى الإيصال.', '给你的商店起个名字，写在小票最上面。'), 'fallo-tuo.svg', 'Fallo tuo'),
    P(T('Sul quaderno', 'في الدفتر', '写在本子上'), T('Ricopia sul quaderno il riquadro giallo.', 'انسخ المربع الأصفر في الدفتر.', '把黄色框抄在本子上。'), 'quaderno.svg', 'Quaderno',
      extra=Q_QUAD("resto = dati - prezzo\nbanconote = resto div 10      avanza = resto mod 10\n'Cliente: ' + Edit1.Text   = il + unisce due testi")),
] + SALVA_SHOT(3)

FAC = {
    1: ('il bottone Km in metri', 'Fai solo i passi 1-7 e 12-14: un solo bottone (km in metri), screenshot e consegna.', 'افعل الخطوات 1-7 و12-14 فقط: زر واحد ثم اللقطة والتسليم.', '只做第 1-7 步和 12-14 步：一个按钮，截图并提交。'),
    2: ('il bottone +', 'Fai solo il bottone <b>+</b>: componenti, codice, prova 7 più 5, screenshot e consegna.', 'افعل زر + فقط: المكونات والكود والتجربة ثم اللقطة والتسليم.', '只做 + 按钮：组件、代码、试 7 加 5、截图和提交。'),
    3: ('il resto', 'Fai solo il <b>resto</b> (soldi dati meno prezzo): niente banconote, screenshot e consegna.', 'افعل الباقي فقط (المبلغ ناقص السعر)، ثم اللقطة والتسليم.', '只做找零（给的钱减价格）：不算钞票，截图并提交。'),
}
TIT = {1: ('Convertitore di misure', 'محوّل القياسات', '单位换算器'), 2: ('Calcolatrice a 4 bottoni', 'آلة حاسبة بأربعة أزرار', '四个按钮的计算器'), 3: ('Il cassiere', 'أمين الصندوق', '收银员')}
for n, passi in ((1, PASSI1), (2, PASSI2), (3, PASSI3)):
    f = FAC[n]
    fac = NOTA_FAC % (f[0], f[1], f[2], f[3])
    h = pagina(SLUG, '1INF', 'Ora %d · %s' % (n, TIT[n][0]), '1INF · Laboratorio · mercoledì 04/11/2026 · si consegnano SEMPRE unit1.pas e lo screenshot', n, passi, ('ar', 'zh'), 'it,ar,zh',
               h1l={'ar': 'الساعة %d · %s' % (n, TIT[n][1]), 'zh': '第 %d 节 · %s' % (n, TIT[n][2])}, extra_mid=fac, avz='1inf-lab0411-ora%d' % n)
    h = h.replace('id="nome"', 'id="nome"')  # (campo nome comune)
    open(D + 'modulo-%d.html' % n, 'w', encoding='utf-8').write(h)

# ---------- pagina dell'indice (gated sull'ora 1) ----------
IDX = ['<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">',
       '<title>Laboratorio 1INF 04/11</title><script src="ore.js" data-ora="1"></script><style>%s</style></head><body><main>' % CSS,
       '<h1>OGGI 04/11 · Laboratorio 1INF</h1><p class="ar" lang="ar" dir="rtl">اليوم 04/11 · مختبر 1INF</p><p class="zh" lang="zh">今天 04/11 · 1INF 实验课</p>',
       '<p>Oggi fai programmi <b>utili</b> in Lazarus con testo (String) e numeri (Integer). Un percorso per ogni ora; a ogni ora manda <code>unit1.pas</code> e lo screenshot. Ricopia sul quaderno il riquadro giallo.</p>',
       '<p class="ar" lang="ar" dir="rtl">اليوم تصنع برامج مفيدة في Lazarus بالنصوص (String) والأرقام (Integer). مسار لكل ساعة؛ في كل ساعة أرسل unit1.pas ولقطة الشاشة.</p><p class="zh" lang="zh">今天用 Lazarus 做有用的程序，用到文字（String）和数字（Integer）。每节课一条路线；每节课提交 unit1.pas 和截图。</p>',
       '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova. · <span lang="ar">اضغط F5 لرؤية النسخة الجديدة.</span> · <span lang="zh">按 F5 查看新版本。</span></p>',
       '<section class="card"><h2>Ora 1 · Convertitore di misure · محوّل القياسات · 单位换算器</h2><a class="bt" href="modulo-1.html">Apri l\'ora 1</a></section>',
       '<section class="card"><h2>Ora 2 · Calcolatrice a 4 bottoni · آلة حاسبة · 计算器</h2><a class="bt" href="modulo-2.html">Apri l\'ora 2 (si apre quando il Prof la sblocca)</a></section>',
       '<section class="card"><h2>Ora 3 · Il cassiere · أمين الصندوق · 收银员</h2><a class="bt" href="modulo-3.html">Apri l\'ora 3 (si apre quando il Prof la sblocca)</a></section>',
       '<section class="card" style="border-color:var(--ok)"><h2>Il mio andamento · تقدّمي · 我的进度</h2><a class="bt v" href="cruscotto-ragazzi.html">Il mio andamento · تقدّمي · 我的进度</a></section>',
       '<div id="aiuto"></div></main><script src="../../assistente/assistente.js" data-pagina="1inf-lab-04-11" data-lingue="it,ar,zh" data-dove="aiuto"></script></body></html>']
open(D + 'index.html', 'w', encoding='utf-8').write('\n'.join(IDX))

# ---------- file di supporto copiati dai modelli ----------
M = SLUGDIR + '1inf-lab-30-10/'
shutil.copy(SLUGDIR + '1inf-deepfake-03-11/ore.js', D + 'ore.js')
for f in ('cruscotto.css', 'cruscotto-vista.js'):
    shutil.copy(SLUGDIR + '1inf-deepfake-03-11/' + f, D + f)
r = open(SLUGDIR + '1inf-deepfake-03-11/cruscotto-ragazzi.html', encoding='utf-8').read().replace('03/11', '04/11')
open(D + 'cruscotto-ragazzi.html', 'w', encoding='utf-8').write(r)
(not os.path.exists(D + 'cruscotto-ragazzi.json')) and open(D + 'cruscotto-ragazzi.json', 'w', encoding='utf-8').write(json.dumps({"titolo": "1INF 04/11", "generato": "", "ora": "-", "fonte": "dati non ancora letti: il docente preme LEGGI I DATI quando serve", "righe": []}, ensure_ascii=False, indent=1))
json.dump({"invio": INVIO, "attivo": True, "ore_sbloccate": 0,
           "_nota": "1INF 04/11/2026, Laboratorio 8-11: convertitore, calcolatrice, cassiere (Allegato A PFP_1 Comp. 15, I anno). Pagina CHIUSA finche il docente non sblocca (regola 31).",
           "_ore": "0 = tutta chiusa; il docente alza di UNA ora alla volta con strumenti/sblocca_ora.py 1inf-lab-04-11 N."},
          open(D + 'config.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = open(M + 'consegna.html', encoding='utf-8').read()
c = c.replace("['', 'pasticcio', 'soprannome', 'segnapunti']", "['', 'convertitore', 'calcolatrice', 'cassiere']").replace('1inf-lab3010-ora', '1inf-lab0411-ora').replace('lab3010-', 'lab0411-')
c = c.replace("'modulo-' + ORA + '.html#C2'", "'modulo-' + ORA + '.html'")
c = c.replace('consegna i due file su Classroom con i passi C2-C5 della <a id="torna" href="#">pagina del percorso</a>', 'consegna i due file su Classroom nel compito di oggi (sono nella cartella del progetto). <a id="torna" href="#">Torna ai passi</a>')
assert '1inf-lab0411-ora' in c and 'convertitore' in c
open(D + 'consegna.html', 'w', encoding='utf-8').write(c)

# ---------- controllo automatico di unit1.pas ----------
JSC = r"""// 1INF 04/11/2026: controllo automatico di unit1.pas (convertitore, calcolatrice, cassiere).
// Solo un aiuto: NON blocca mai la consegna. Uso: ControllaPas(testo, ora) -> {ok, facile, voci:[{ok,avviso,it,ar,zh}], ora_trovata}
(function (g) {
  function pulisci(t) { return String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/\(\*[\s\S]*?\*\)/g, ' ').replace(/\/\/[^\n]*/g, ' '); }
  function senzaScritte(t) { return t.replace(/'[^'\n]*'/g, "''"); }
  function voce(ok, it, ar, zh, avviso) { return { ok: !!ok, avviso: !!avviso, it: it, ar: ar, zh: zh }; }
  function oraTrovata(c) {
    if (/\bmod\b/i.test(c) && /\bMemo1\b/i.test(c)) return 3;
    if (/StrToIntDef\s*\(\s*Edit2/i.test(c)) return 2;
    if (/\bdiv\b|\*\s*1000|\*\s*60\b/i.test(c)) return 1;
    return 0;
  }
  var FACILE = {
    1: /\bLabel1\s*\.\s*Caption\s*:=[^;]*\*\s*1000/i,
    2: /\bLabel1\s*\.\s*Caption\s*:=[^;]*StrToInt(Def)?\s*\(\s*Edit1[^;]*\+/i,
    3: /resto\s*:=\s*\w+\s*-\s*\w+/i
  };
  function ControllaPas(testo, ora) {
    var c0 = pulisci(testo), c = senzaScritte(c0), V = [];
    var unita = /\bunit\s+\w+\s*;/i.test(c) && /\bimplementation\b/i.test(c) && /\bend\s*\.\s*$/i.test(c.trim());
    V.push(voce(unita, 'È un file di Lazarus (una unit in Pascal).', 'هذا ملف Lazarus (وحدة Pascal).', '这是 Lazarus 文件（Pascal 单元）。'));
    if (!unita) {
      V.push(voce(false, 'Hai scelto il file giusto? Deve essere unit1.pas, nella cartella del progetto.', 'هل اخترت الملف الصحيح؟ يجب أن يكون unit1.pas في مجلد المشروع.', '选对文件了吗？必须是项目文件夹里的 unit1.pas。'));
      return { ok: false, voci: V, ora_trovata: 0 };
    }
    var clic = /procedure\s+TForm1\s*\.\s*Button1Click\s*\(/i.test(c);
    V.push(voce(clic, 'C\'è il clic del bottone: Button1Click.', 'يوجد نقر الزر: Button1Click.', '有按钮的点击：Button1Click。'));
    var nb = (c.match(/procedure\s+TForm1\s*\.\s*Button\d+Click\s*\(/gi) || []).length;
    if (ora === 1) {
      V.push(voce(/\bvar\b[\s\S]*?:\s*Integer\s*;[\s\S]*?\bbegin\b/i.test(c), 'Ci sono variabili Integer: var km, metri: Integer;', 'توجد متغيرات Integer.', '有 Integer 变量。'));
      V.push(voce(/\bStrToInt(Def)?\s*\(\s*Edit1\s*\.\s*Text/i.test(c), 'Il bottone legge la casella: StrToInt(Edit1.Text).', 'الزر يقرأ الخانة: StrToInt(Edit1.Text).', '按钮读取输入框：StrToInt(Edit1.Text)。'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=[^;]*IntToStr\s*\(/i.test(c), 'Il risultato va nella Caption con IntToStr( … ).', 'النتيجة تذهب إلى Caption بـ IntToStr( … ).', '结果用 IntToStr( … ) 放进 Caption。'));
      V.push(voce(/\*\s*1000\b/.test(c), 'Km in metri: * 1000.', 'كم إلى متر: * 1000.', '公里变米：* 1000。'));
      V.push(voce(/\*\s*60\b/.test(c), 'Ore in minuti: * 60.', 'ساعات إلى دقائق: * 60.', '小时变分钟：* 60。', true));
      V.push(voce(/\*\s*100\b(?!0)/.test(c), 'Euro in centesimi: * 100.', 'يورو إلى سنت: * 100.', '欧元变分：* 100。', true));
      V.push(voce(/9\s*\)?\s*div\s*5\s*\)?\s*\+\s*32/i.test(c), 'Celsius in Fahrenheit: C * 9 div 5 + 32.', 'سيلسيوس إلى فهرنهايت: C * 9 div 5 + 32.', '摄氏变华氏：C * 9 div 5 + 32。', true));
      V.push(voce(/\bdiv\s+60\b/i.test(c) && /\bmod\s+60\b/i.test(c), 'Minuti in ore e minuti: div 60 e mod 60.', 'دقائق إلى ساعات ودقائق: div 60 و mod 60.', '分钟变小时和分钟：div 60 和 mod 60。', true));
      V.push(voce(nb >= 3, 'Hai almeno 3 bottoni con il loro codice.', 'لديك 3 أزرار على الأقل بكودها.', '至少有 3 个按钮和它们的代码。', true));
    } else if (ora === 2) {
      V.push(voce(/\bStrToIntDef\s*\(\s*Edit1\s*\.\s*Text\s*,/i.test(c) && /\bStrToIntDef\s*\(\s*Edit2\s*\.\s*Text\s*,/i.test(c), 'Leggi le due caselle con StrToIntDef(Edit1.Text, 0) e StrToIntDef(Edit2.Text, 0).', 'تقرأ الخانتين بـ StrToIntDef.', '用 StrToIntDef 读取两个输入框。'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=[^;]*'[^']*'[^;]*IntToStr\s*\(/i.test(c0) || /\bLabel1\s*\.\s*Caption\s*:=[^;]*IntToStr[^;]*\+\s*''/i.test(c), 'Il risultato è una frase: IntToStr(a) + \' più \' + …', 'النتيجة جملة.', '结果是一句话。'));
      V.push(voce(/IntToStr\s*\(\s*a\s*\+\s*b\s*\)/i.test(c), 'Il bottone + : IntToStr(a + b).', 'زر الجمع.', '加号按钮。'));
      V.push(voce(/IntToStr\s*\(\s*a\s*-\s*b\s*\)/i.test(c), 'Il bottone − : IntToStr(a - b).', 'زر الطرح.', '减号按钮。', true));
      V.push(voce(/IntToStr\s*\(\s*a\s*\*\s*b\s*\)/i.test(c), 'Il bottone × : IntToStr(a * b).', 'زر الضرب.', '乘号按钮。', true));
      V.push(voce(/IntToStr\s*\(\s*a\s+div\s+b\s*\)/i.test(c), 'Il bottone ÷ : IntToStr(a div b).', 'زر القسمة.', '除号按钮。', true));
      V.push(voce(/\bif\s+b\s*=\s*0\s+then\b/i.test(c), 'Bonus: if b = 0 then … (niente divisione per zero).', 'إضافي: if b = 0 then …', '加分：if b = 0 then …', true));
    } else if (ora === 3) {
      V.push(voce(/\bStrToInt(Def)?\s*\(\s*Edit2\s*\.\s*Text/i.test(c) && /\bStrToInt(Def)?\s*\(\s*Edit3\s*\.\s*Text/i.test(c), 'Leggi prezzo e soldi dati: StrToIntDef(Edit2.Text, 0) e StrToIntDef(Edit3.Text, 0).', 'تقرأ السعر والمبلغ.', '读取价格和给的钱。'));
      V.push(voce(/\w+\s*:=\s*\w+\s*-\s*\w+\s*;/.test(c), 'Calcoli il resto: dati - prezzo.', 'تحسب الباقي.', '计算找零。'));
      V.push(voce(/\bdiv\s+10\b/i.test(c) && /\bmod\s+10\b/i.test(c), 'Banconote da 10 con div 10 e mod 10.', 'أوراق 10 بـ div و mod.', '用 div 10 和 mod 10 算 10 元钞票。', true));
      V.push(voce(/\bMemo1\s*\.\s*Lines\s*\.\s*Add\s*\(/i.test(c), 'Lo scontrino usa Memo1.Lines.Add( … ).', 'الإيصال يستعمل Memo1.Lines.Add.', '小票用 Memo1.Lines.Add。'));
      V.push(voce(/'[^']*'\s*\+\s*Edit1\s*\.\s*Text/i.test(c0), 'Il nome del cliente è unito con +: \'Cliente: \' + Edit1.Text.', 'اسم الزبون ملصق بـ +.', '顾客名字用 + 连接。'));
    }
    var errori = V.filter(function (v) { return !v.ok && !v.avviso; }).length, fac = false;
    if (errori > 0 && clic && FACILE[ora] && FACILE[ora].test(c)) {
      fac = true; V.forEach(function (v) { if (!v.ok) v.avviso = true; });
      V.push(voce(true, 'Percorso facilitato: il codice è giusto. Bravo! Le righe gialle sono per chi fa il percorso completo.', 'المسار الميسّر: الكود صحيح. أحسنت!', '简单路线：代码正确。真棒！'));
      errori = 0;
    }
    return { ok: errori === 0, facile: fac, voci: V, ora_trovata: oraTrovata(c) };
  }
  g.ControllaPas = ControllaPas;
  if (typeof module !== 'undefined') module.exports = ControllaPas;
})(typeof window !== 'undefined' ? window : globalThis);
"""
open(D + 'controlla-pas.js', 'w', encoding='utf-8').write(JSC)
print('1inf ok', len(os.listdir(D)), 'file;', len(os.listdir(D + 'img')), 'schemi')
