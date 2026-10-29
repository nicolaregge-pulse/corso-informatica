#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1INF 30/10/2026: due pagine della giornata, italiano + arabo + cinese (regola 21), una riga da ricopiare sul quaderno (regola 23).
#   docs/1inf-unicode/        Tecnologia 8-9: «Il computer scrive in tutte le lingue» (da ASCII, 02/10, a Unicode), con la casella prova-lettere.
#   docs/1inf-lazarus-label/  Laboratorio 11-14: Lazarus «Ciao 2»: Label, Caption, colori e il bottone Cancella.
# Nessun dato del ragazzo esce dalla pagina: la consegna è su Classroom (quiz su Moduli per la Tecnologia, Documento per il Laboratorio).
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../docs/')

CSS = """:root{--bg:#f6f7f9;--fg:#1f2328;--mu:#5b6573;--card:#fff;--bd:#d5dbe3;--acc:#0b6e99;--ok:#1a7f37;--q:#fff4c2}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--mu:#9aa5b1;--card:#161b22;--bd:#30363d;--acc:#4ea8de;--ok:#3fb950;--q:#3b3200}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.5 system-ui,sans-serif}
main{max-width:820px;margin:0 auto;padding:12px 16px 60px}h1{font-size:1.5em;margin:.4em 0}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 14px;margin:12px 0}
.ar{direction:rtl;color:var(--mu);font-size:.95em;margin:4px 0}.zh{color:var(--mu);font-size:.95em;margin:4px 0}
pre{background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;overflow-x:auto;font-size:16px;white-space:pre-wrap}
.quad{background:var(--q);border:2px solid #d4a017;border-radius:10px;padding:10px 12px}
.f5{background:var(--q);border-radius:10px;padding:8px 12px;font-size:.95em}
a.bt{display:block;text-align:center;background:var(--acc);color:#fff;font-weight:700;padding:12px;border-radius:10px;text-decoration:none;margin:8px 0}
input{font-size:22px;width:100%;padding:10px;border:2px solid var(--acc);border-radius:10px;background:var(--card);color:var(--fg)}
table{border-collapse:collapse;width:100%}td,th{border:1px solid var(--bd);padding:6px;text-align:center}
.tw{overflow-x:auto;max-width:100%}.big{font-size:28px}code{background:rgba(127,127,127,.15);border-radius:5px;padding:1px 5px}
.fatto{color:var(--ok);font-weight:700}"""

def L(it, ar, zh):
    return '<p>' + it + '</p><p class="ar" lang="ar" dir="rtl">' + ar + '</p><p class="zh" lang="zh">' + zh + '</p>'

def card(t, body):
    return '<section class="card"><h2>' + t + '</h2>' + body + '</section>'

def pagina(titolo, h1, sotto, corpo, js=''):
    return ('<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>' + titolo + '</title><style>' + CSS + '</style></head><body><main><h1>' + h1 + '</h1><p class="zh">' + sotto + '</p>'
            '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova. · اضغط F5 لرؤية النسخة الجديدة. · 按 F5 查看新版本。</p>'
            '<a class="bt" href="../1inf-oggi/" target="_blank" rel="noopener">La mia giornata · يومي · 我的一天</a>'
            + corpo + '</main>' + ('<script>' + js + '</script>' if js else '') + '</body></html>')

# ---------------- Tecnologia: Unicode ----------------
U = []
U.append(card('1. Ripasso: il tuo nome in ASCII', L(
    'Il 2 ottobre hai scritto il tuo nome in binario: ogni lettera ha un <b>numero</b>. La <b>A</b> è 65, la <b>B</b> è 66… Questa tabella si chiama <b>ASCII</b>: 128 caratteri, solo lettere latine, cifre e segni.',
    'في 2 أكتوبر كتبت اسمك بالثنائي: لكل حرف رقم. A هو 65، B هو 66… هذا الجدول اسمه ASCII: 128 رمزاً فقط، حروف لاتينية وأرقام وعلامات.',
    '10月2日你把名字写成了二进制：每个字母都有一个数字。A 是 65，B 是 66……这个表叫 ASCII：只有 128 个字符，只有拉丁字母、数字和符号。')))
U.append(card('2. Il problema: e l\'arabo? E il cinese?', L(
    'In 128 posti non ci stanno le lettere arabe, i caratteri cinesi, le emoji. Ogni paese faceva la sua tabella e i testi si rompevano: comparivano simboli strani come <code>Ã©</code> o <code>???</code>.',
    'في 128 مكاناً لا تتسع الحروف العربية ولا الرموز الصينية ولا الإيموجي. كل بلد صنع جدوله والنصوص كانت تفسد: تظهر رموز غريبة مثل ??? .',
    '128 个位置放不下阿拉伯字母、汉字和表情符号。每个国家做自己的表，文字经常乱码：出现 ??? 这样的怪符号。')))
U.append(card('3. La soluzione: Unicode', L(
    '<b>Unicode</b> è UNA tabella per TUTTE le lingue del mondo: più di 150.000 caratteri. Ogni carattere ha il suo numero, uguale in tutti i computer e telefoni. Le prime 128 posizioni sono proprio l\'ASCII: la A resta 65.',
    'Unicode جدول واحد لكل لغات العالم: أكثر من 150000 رمز. لكل رمز رقمه، نفسه في كل الحواسيب والهواتف. أول 128 مكاناً هي ASCII: الحرف A يبقى 65.',
    'Unicode 是一张给世界上所有语言用的表：超过 15 万个字符。每个字符都有自己的数字，在所有电脑和手机上都一样。前 128 个位置就是 ASCII：A 还是 65。')))
U.append(card('4. Prova tu: scrivi il tuo nome nella tua lingua', L(
    'Scrivi qui il tuo nome, anche in arabo o in cinese, o una emoji. Sotto vedi il numero Unicode di ogni carattere. Prima vittoria: trova il numero della prima lettera del tuo nome.',
    'اكتب اسمك هنا، بالعربية أيضاً، أو إيموجي. ترى تحته رقم Unicode لكل حرف. أول فوز: اعثر على رقم أول حرف من اسمك.',
    '在这里写你的名字，也可以用中文，或者一个表情。下面会显示每个字符的 Unicode 数字。第一个胜利：找到你名字第一个字的数字。')
    + '<input id="t" value="Ciao سلام 你好" autocomplete="off" aria-label="testo"><div class="tw"><table id="tb"></table></div><p id="n" class="fatto"></p>'))
U.append(card('5. Quanti byte? UTF-8', L(
    'Nel file il numero si salva con <b>UTF-8</b>: le lettere latine usano <b>1 byte</b>, le lettere arabe <b>2 byte</b>, i caratteri cinesi <b>3 byte</b>, le emoji <b>4 byte</b>. Guarda la colonna «byte» nella tabella qui sopra.',
    'في الملف يُحفظ الرقم بـ UTF-8: الحروف اللاتينية بايت واحد، العربية 2 بايت، الصينية 3 بايت، الإيموجي 4 بايت. انظر عمود «byte» في الجدول.',
    '在文件里数字用 UTF-8 保存：拉丁字母 1 个字节，阿拉伯字母 2 个字节，汉字 3 个字节，表情 4 个字节。看上面表里的“byte”一列。')))
U.append(card('6. Spiegalo in 30 secondi', L(
    'Al compagno di banco, a voce: «Perché sul mio telefono vedo bene sia l\'arabo sia il cinese?»',
    'لزميلك بصوتك: «لماذا أرى العربية والصينية جيداً على هاتفي؟»',
    '对同桌说：“为什么我的手机上阿拉伯文和中文都能正常显示？”')))
U.append(card('7. Da ricopiare sul quaderno', '<div class="quad"><pre>ASCII = 128 caratteri, solo lettere latine. A = 65.\nUNICODE = una tabella per TUTTE le lingue.\nUTF-8 = latino 1 byte, arabo 2, cinese 3, emoji 4.</pre></div>'))
U.append(card('8. Il quiz', L('Il quiz su Google Moduli è nel compito di oggi su Classroom: 15 domande, premi «Invia» alla fine.',
    'الاختبار على Google Moduli موجود في واجب اليوم على Classroom: 15 سؤالاً، اضغط «إرسال» في النهاية.',
    'Google Moduli 上的测验在今天 Classroom 的作业里：15 道题，最后点“提交”。')))
JSU = """var t=document.getElementById('t'),tb=document.getElementById('tb'),n=document.getElementById('n');
function f(){var r='<tr><th>car.</th><th>numero</th><th>byte</th></tr>',c=0;for(var ch of t.value){if(ch===' ')continue;c++;var cp=ch.codePointAt(0),b=new TextEncoder().encode(ch).length;
r+='<tr><td class="big">'+ch.replace(/</g,'&lt;')+'</td><td>'+cp+'</td><td>'+b+'</td></tr>';}tb.innerHTML=r;n.textContent=c?'FATTO! '+c+' caratteri · ✔':'';}
t.addEventListener('input',f);f();"""

# ---------------- Laboratorio: Lazarus Ciao 2 ----------------
PASSI = [
 ('Apri il progetto Ciao di mercoledì: menu <b>Progetto</b> → <b>Apri progetto…</b> → cartella <b>Documenti\\Lazarus\\Ciao</b> → file <b>.lpi</b> → <b>Apri</b>.',
  'افتح مشروع Ciao: قائمة Progetto ← Apri progetto… ← المجلد Documenti\\Lazarus\\Ciao ← الملف .lpi ← Apri.',
  '打开周三的 Ciao 项目：菜单 Progetto → Apri progetto… → 文件夹 Documenti\\Lazarus\\Ciao → .lpi 文件 → Apri。'),
 ('Salva una copia nuova: menu <b>Progetto</b> → <b>Salva progetto come…</b> → crea la cartella <b>Ciao2</b> dentro <b>Documenti\\Lazarus</b> e salva lì.',
  'احفظ نسخة جديدة: Progetto ← Salva progetto come… ← أنشئ المجلد Ciao2 داخل Documenti\\Lazarus واحفظ هناك.',
  '另存一份新的：Progetto → Salva progetto come… → 在 Documenti\\Lazarus 里新建文件夹 Ciao2，保存在那里。'),
 ('Nella palette <b>Standard</b> clicca la <b>A</b> (è la <b>TLabel</b>, l\'etichetta) e poi clicca sulla finestra Form1. Compare <b>Label1</b>.',
  'في لوحة Standard انقر على A (هي TLabel، اللافتة) ثم انقر على النافذة Form1. يظهر Label1.',
  '在 Standard 组件面板点 A（就是 TLabel，标签），再点 Form1 窗口。出现 Label1。'),
 ('Doppio clic sul bottone <b>Button1</b>. Cambia la riga di mercoledì così: il saluto va nella Label, non più nella casella.',
  'انقر مرتين على Button1. غيّر السطر هكذا: التحية تذهب إلى الـ Label وليس إلى الخانة.',
  '双击 Button1。把周三的那行改成这样：问候写到 Label 里，不再写到输入框里。'),
 ('Premi <b>F9</b>: scrivi il tuo nome, premi il bottone. Sotto compare <b>Ciao</b> e il tuo nome. <b>FATTO!</b> Fai lo screenshot (Win + Shift + S).',
  'اضغط F9: اكتب اسمك واضغط الزر. يظهر تحته Ciao واسمك. تم! خذ لقطة شاشة (Win + Shift + S).',
  '按 F9：写你的名字，按按钮。下面出现 Ciao 和你的名字。完成！截图（Win + Shift + S）。'),
 ('Fallo tuo: clicca <b>Label1</b>, nell\'<b>Ispettore oggetti</b> (a sinistra) cambia <b>Font</b> → grandezza 24 e <b>Font.Color</b> con il tuo colore; cambia <b>Color</b> di <b>Form1</b>.',
  'اجعله لك: انقر Label1، في Ispettore oggetti (يساراً) غيّر Font ← الحجم 24 و Font.Color بلونك؛ غيّر Color لـ Form1.',
  '做成你自己的：点 Label1，在左边的 Ispettore oggetti 里把 Font 大小改成 24，Font.Color 改成你喜欢的颜色；再改 Form1 的 Color。'),
 ('Chi ha finito: aggiungi <b>Button2</b> con Caption <b>Cancella</b>. Doppio clic e scrivi le due righe del riquadro: svuota la casella e la Label.',
  'من أنهى: أضف Button2 بعنوان Cancella. انقر مرتين واكتب السطرين: يفرغ الخانة والـ Label.',
  '做完的同学：加一个 Button2，Caption 写 Cancella。双击，写下框里的两行：清空输入框和标签。'),
 ('Consegna: apri il <b>Documento</b> del compito di oggi su Classroom, metti il codice, lo screenshot e una frase con parole tue, poi premi <b>Consegna</b>.',
  'التسليم: افتح المستند في واجب اليوم على Classroom، ضع الكود ولقطة الشاشة وجملة بكلماتك، ثم اضغط Consegna.',
  '提交：打开今天 Classroom 作业里的文档，放上代码、截图和一句你自己的话，然后点 Consegna。'),
]
CODICE = {4: "procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  Label1.Caption := 'Ciao ' + Edit1.Text;\nend;",
          7: "  Edit1.Text := '';\n  Label1.Caption := '';"}
B = [card('Che cosa fai oggi', L(
    'Mercoledì il saluto andava nella casella. Oggi lo mettiamo in una <b>Label</b> (l\'etichetta, come la Caption che già conosci), lo facciamo <b>grande e colorato</b> e aggiungiamo il bottone <b>Cancella</b>.',
    'يوم الأربعاء كانت التحية في الخانة. اليوم نضعها في Label (اللافتة)، نجعلها كبيرة وملوّنة ونضيف زر Cancella.',
    '周三问候写在输入框里。今天我们把它放进 Label（标签），把它变大、变彩色，再加一个 Cancella 按钮。')
    + '<p><b>Versione facile (3 passi):</b> passi 3, 4 e 5. · <span lang="ar">النسخة السهلة: الخطوات 3 و4 و5.</span> · <span lang="zh">简单版：第 3、4、5 步。</span></p>'
    + '<p>Chi non ha consegnato il «Ciao» di mercoledì: prima quello. · <span lang="ar">من لم يسلّم Ciao يوم الأربعاء: أولاً هو.</span> · <span lang="zh">周三的 Ciao 没交的同学：先做那个。</span></p>'
    + '<a class="bt" href="../verifica/?b=1inf-lazarus-ciao" target="_blank" rel="noopener">Il «Ciao» di mercoledì · Ciao الأربعاء · 周三的 Ciao</a>')]
for i, (it, ar, zh) in enumerate(PASSI, 1):
    B.append(card('Passo %d' % i, L(it, ar, zh) + ('<pre>' + CODICE[i] + '</pre>' if i in CODICE else '')))
B.append(card('Spiegalo in 30 secondi', L('Al compagno: che differenza c\'è tra <code>Edit1.Text</code> e <code>Label1.Caption</code>?',
    'لزميلك: ما الفرق بين Edit1.Text و Label1.Caption؟', '对同桌说：Edit1.Text 和 Label1.Caption 有什么区别？')))
B.append(card('Da ricopiare sul quaderno', '<div class="quad"><pre>EDIT = la casella dove SCRIVE l\'utente (proprietà Text).\nLABEL = la scritta che MOSTRA il programma (proprietà Caption).\n:=  vuol dire «metti dentro».\nLabel1.Caption := \'Ciao \' + Edit1.Text;</pre></div>'))

os.makedirs(P + '1inf-unicode', exist_ok=True); os.makedirs(P + '1inf-lazarus-label', exist_ok=True)
open(P + '1inf-unicode/index.html', 'w', encoding='utf-8').write(pagina('Tutte le lingue', 'Il computer scrive in tutte le lingue', 'الحاسوب يكتب بكل اللغات · 电脑会写所有语言 · 1INF 30/10/2026', ''.join(U), JSU))
open(P + '1inf-lazarus-label/index.html', 'w', encoding='utf-8').write(pagina('Lazarus Ciao 2', 'Lazarus, Ciao 2: la Label e i colori', 'Lazarus: اللافتة والألوان · Lazarus：标签和颜色 · 1INF 30/10/2026', ''.join(B)))
print('ok')
