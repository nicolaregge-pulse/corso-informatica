# -*- coding: utf-8 -*-
# Dispensa base "Bit, byte e numeri binari" v1.1 — SOLO binario->decimale (come la lavagna),
# con la FOTO della lavagna dentro la teoria. Teoria semplice ed estesa + 24 esempi.
# 3 documenti monolingui IT/AR/ZH. Per ragazzi che arrivano dalla 3a media.
import os, subprocess, base64
POS=[128,64,32,16,8,4,2,1]
def b8(n): return format(n,'08b')
def addends(n):
    return " + ".join(str(POS[i]) for i,c in enumerate(b8(n)) if c=='1') or "0"

LAVB64=base64.b64encode(open("/home/user/corso-godot/classe-1/lavagne/20261001-bit-e-byte.jpg","rb").read()).decode()
def lavfig(cap): return f'<div class="fig"><img src="data:image/jpeg;base64,{LAVB64}"><div class="cap">{cap}</div></div>'

# 24 esempi: dal BYTE al DECIMALE (la direzione della lezione)
NUMS=[3,5,10,13,19,27,42,50,64,78,85,100,120,127,130,150,170,200,210,225,240,250,255,99]
def ex_row(n):
    bitc="".join(f"<td class='{'one' if c=='1' else ''}'>{c}</td>" for c in b8(n))
    return (f"<div class='ex'><div class='exn'><code>{b8(n)}</code></div>"
            f"<table class='pos'><tr>{''.join(f'<td>{v}</td>' for v in POS)}</tr><tr>{bitc}</tr></table>"
            f"<div class='exb'>= {addends(n)} = <b>{n}</b></div></div>")
ESEMPI="".join(ex_row(n) for n in NUMS)

CSS="""@page{size:A4}*{box-sizing:border-box}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:11pt;line-height:1.55;margin:0}
.cover{background:linear-gradient(160deg,#134a6e,#2c86b8);color:#fff;border-radius:12px;padding:12mm;text-align:center;margin-bottom:5mm}
.cover h1{font-size:20pt;margin:0}.cover .s{font-size:12pt;opacity:.93;margin-top:2mm}
h2{color:#12467a;font-size:14.5pt;margin:6mm 0 2mm;border-bottom:2px solid #2b7cc4;padding-bottom:1mm}
p{margin:2mm 0}ol,ul{padding-left:7mm}li{margin:1.6mm 0}
.key{background:#eef4fb;border:1px solid #9cc0e4;border-left:5px solid #2b7cc4;border-radius:6px;padding:3mm 4mm;margin:3mm 0}
.vinci{background:#eafaf0;border:1px solid #bfe6cf;border-left:5px solid #2f9e57;border-radius:6px;padding:3mm 4mm;margin:3mm 0}.vinci b{color:#1e7a44}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px}
table.pos{border-collapse:collapse;margin:1mm 0;font-size:10pt;text-align:center}
table.pos td{border:1px solid #9cc0e4;padding:1mm 2mm}table.pos .one{background:#eafaf0;font-weight:bold;color:#1e7a44}
.fig{text-align:center;margin:3mm 0;border:1px solid #cfe0f0;border-radius:10px;padding:3mm;background:#fff}
.fig img{max-width:78%}.cap{font-size:9.5pt;color:#667;margin-top:1.5mm}
.grid{display:flex;flex-wrap:wrap;gap:4mm}
.ex{border:1px solid #d5e0ec;border-radius:7px;padding:2mm 3mm;background:#fafcff}
.flag{display:inline-block;background:#12467a;color:#fff;border-radius:5px;padding:1mm 4mm;font-size:11pt;margin-top:6mm}
.lang-ar{direction:rtl;text-align:right;font-family:"Amiri",serif;font-size:13pt}
.lang-ar ol,.lang-ar ul{padding-right:7mm;padding-left:0}
.lang-zh{font-family:"WenQuanYi Zen Hei",sans-serif;font-size:11.5pt}
"""

ESE78=("<table class='pos'><tr>"+"".join(f'<td>{v}</td>' for v in POS)+"</tr><tr>"
       +"".join(f"<td class='{'one' if c=='1' else ''}'>{c}</td>" for c in b8(78))+"</tr></table>")

IT=f"""
<div class="key"><b>In questa lezione facciamo UNA direzione: dal BINARIO al DECIMALE</b> (da 0 e 1 al numero di tutti i giorni).</div>
<h2>1. I numeri di tutti i giorni</h2>
<p>Noi contiamo con <b>dieci cifre</b>: 0 1 2 3 4 5 6 7 8 9. Con queste dieci cifre scriviamo
<b>qualsiasi</b> numero. Questo si chiama <b>sistema decimale</b> («deci» vuol dire dieci).</p>
<h2>2. Dentro il computer: acceso o spento</h2>
<p>Il computer è fatto di <b>tantissimi piccoli interruttori</b>. Un interruttore può stare solo
in <b>due modi</b>: acceso o spento. Il computer usa questi due stati: <b>acceso = 1</b>, <b>spento = 0</b>.</p>
<h2>3. Il bit</h2>
<div class="key">Un <b>bit</b> è la cosa più piccola: <b>una sola cifra, 0 oppure 1</b>. La parola "bit"
viene dall'inglese <b>Binary Digit</b> = <b>cifra binaria</b>. Tutto, dentro il computer, è fatto di bit.</div>
<h2>4. Contare con solo 0 e 1 (il binario)</h2>
<p>Con due cifre si conta così: 0, 1… poi le cifre finiscono, quindi si scrive <b>10, 11, 100, 101,
110, 111…</b> È come il <b>contachilometri</b> dell'auto: quando una rotella arriva in fondo, gira quella accanto.</p>
<h2>5. Il byte</h2>
<p>Mettiamo insieme <b>8 bit</b>: questo si chiama <b>byte</b>. Un byte ha <b>8 caselle</b>, ognuna
con uno 0 o un 1. Una <b>lettera</b> scritta nel computer occupa <b>1 byte</b>.</p>
<h2>6. Da binario a decimale (il metodo delle caselle)</h2>
<p>Ogni casella ha un <b>valore</b>. Da destra verso sinistra: <b>1, 2, 4, 8, 16, 32, 64, 128</b>
(ogni volta il doppio). Per trovare il numero: guarda dove c'è un <b>1</b> e <b>somma</b> i valori.</p>
<div class="key"><b>Esempio (come alla lavagna):</b>{ESE78}
<p>Ci sono gli <b>1</b> sotto 64, 8, 4, 2 → <b>64 + 8 + 4 + 2 = 78</b>. Quindi <code>01001110 = 78</code>.</p></div>
{lavfig("La lavagna della nostra lezione: BIT, Byte = 8 bit e la conversione 01001110 = 64+8+4+2 = 78.")}
<div class="vinci"><b>Trucco con le dita:</b> ogni dito è un bit (alzato = 1, abbassato = 0). Con
<b>una mano</b> conti fino a <b>31</b>, con <b>due mani</b> fino a <b>1023</b>!</div>
<h2>7. Quanto «pesa» (i multipli)</h2>
<p>1 byte = 8 bit. Poi: <b>1 KB = 1024 byte</b>, <b>1 MB = 1024 KB</b>, <b>1 GB = 1024 MB</b>.
Una foto pesa qualche <b>MB</b>; un film qualche <b>GB</b>.</p>
"""

AR=f"""
<div class="key"><b>في هذا الدرس نعمل في اتجاه واحد: من الثنائي إلى العشري</b> (من 0 و 1 إلى الرقم العادي).</div>
<h2>1. أرقام كل يوم</h2>
<p>نحن نعدّ بعشرة أرقام: 0 1 2 3 4 5 6 7 8 9. بهذه الأرقام نكتب <b>أي</b> عدد. هذا هو <b>النظام العشري</b>.</p>
<h2>2. داخل الحاسوب: مُشغّل أو مُطفأ</h2>
<p>الحاسوب مصنوع من <b>ملايين المفاتيح الصغيرة</b>. المفتاح له حالتان فقط: <b>مُشغّل = 1</b>، <b>مُطفأ = 0</b>.</p>
<h2>3. البِت</h2>
<div class="key">البِت هو أصغر شيء: <b>رقم واحد فقط، 0 أو 1</b>. كلمة "bit" من الإنجليزية <b>Binary Digit</b> = رقم ثنائي. كل شيء داخل الحاسوب مصنوع من بتات.</div>
<h2>4. العدّ بـ 0 و 1 فقط (الثنائي)</h2>
<p>برقمين نعدّ هكذا: 0، 1… ثم تنتهي الأرقام، فنكتب <b>10، 11، 100، 101، 110، 111…</b> تمامًا مثل عدّاد السيارة.</p>
<h2>5. البايت</h2>
<p>نجمع <b>8 بتات</b> معًا: هذا هو <b>البايت</b>. للبايت <b>8 خانات</b>. الحرف الواحد = <b>1 بايت</b>.</p>
<h2>6. من الثنائي إلى العشري (طريقة الخانات)</h2>
<p>كل خانة لها <b>قيمة</b>، من اليمين إلى اليسار: <b>1، 2، 4، 8، 16، 32، 64، 128</b>. اجمع القيم حيث يوجد <b>1</b>.</p>
<div class="key"><b>مثال (كما على اللوحة):</b>{ESE78}
<p>توجد 1 تحت 64 و8 و4 و2 ← <b>64 + 8 + 4 + 2 = 78</b>. إذن <code>01001110 = 78</code>.</p></div>
{lavfig("لوحة درسنا: BIT، Byte = 8 بت، والتحويل 01001110 = 64+8+4+2 = 78.")}
<div class="vinci"><b>حيلة الأصابع:</b> كل إصبع بِت (مرفوع = 1). بيد واحدة تصل إلى 31، وبيدين إلى 1023!</div>
<h2>7. كم «يزن» (المضاعفات)</h2>
<p>1 بايت = 8 بت. ثم: 1 KB = 1024 بايت، 1 MB = 1024 KB، 1 GB = 1024 MB. الصورة بضعة MB، الفيلم بضعة GB.</p>
"""

ZH=f"""
<div class="key"><b>这节课我们只做一个方向:从二进制到十进制</b>(从 0 和 1 到平常用的数字)。</div>
<h2>1. 每天用的数字</h2>
<p>我们用<b>十个数字</b>来数数:0 1 2 3 4 5 6 7 8 9。用这十个数字可以写出<b>任何</b>数。这叫<b>十进制</b>。</p>
<h2>2. 计算机内部:开或关</h2>
<p>计算机由<b>数十亿个小开关</b>组成。开关只有两种状态:<b>开 = 1</b>,<b>关 = 0</b>。</p>
<h2>3. 位(bit)</h2>
<div class="key">位是最小的东西:<b>只有一个数字,0 或 1</b>。“bit” 来自英文 <b>Binary Digit</b> = 二进制数字。计算机里的一切都由位组成。</div>
<h2>4. 只用 0 和 1 数数(二进制)</h2>
<p>用两个数字这样数:0、1……数字用完了,就写 <b>10、11、100、101、110、111……</b> 就像汽车的里程表。</p>
<h2>5. 字节(byte)</h2>
<p>把 <b>8 个位</b>放在一起:这叫<b>字节</b>。一个字节有 <b>8 个格子</b>。一个字母 = <b>1 字节</b>。</p>
<h2>6. 从二进制到十进制(格子法)</h2>
<p>每个格子有一个<b>数值</b>,从右到左:<b>1、2、4、8、16、32、64、128</b>。把有 <b>1</b> 的位置上的数值<b>相加</b>。</p>
<div class="key"><b>例子(和白板一样):</b>{ESE78}
<p>在 64、8、4、2 下面有 1 ← <b>64 + 8 + 4 + 2 = 78</b>。所以 <code>01001110 = 78</code>。</p></div>
{lavfig("我们这节课的白板:BIT、Byte = 8 位,以及换算 01001110 = 64+8+4+2 = 78。")}
<div class="vinci"><b>手指技巧:</b>每个手指是一个位(竖起 = 1)。一只手数到 31,两只手数到 1023!</div>
<h2>7. 有多“重”(倍数)</h2>
<p>1 字节 = 8 位。然后:1 KB = 1024 字节,1 MB = 1024 KB,1 GB = 1024 MB。一张照片几 MB,一部电影几 GB。</p>
"""

OUT="/home/user/corso-godot/classe-1/bit-e-byte"
SP="/tmp/claude-0/-home-user-corso-godot/d65eff9d-e028-5dc2-8095-966645bd40b0/scratchpad"
RENDER="/home/user/corso-godot/strumenti/render-pdf/render_doc.js"
ENV=dict(os.environ); ENV["NODE_PATH"]=f"{SP}/node_modules"
LANGS=[
 ("IT","Bit, byte e numeri binari","Classe 1 · spiegazione base · italiano", IT, "lang-it",
   "Tanti esempi: byte → decimale","Dato il byte, somma i valori dove c'è un 1: trovi il numero. Gli 1 sono evidenziati.", ""),
 ("AR","البت والبايت والأعداد الثنائية","الصف الأول · شرح أساسي · العربية", AR, "lang-ar",
   "أمثلة كثيرة: بايت ← عدد عشري","من البايت، اجمع القيم حيث يوجد 1 فتجد العدد. الأرقام 1 مميّزة.", "lang-ar"),
 ("ZH","位、字节和二进制数","一年级 · 基础讲解 · 中文", ZH, "lang-zh",
   "很多例子:字节 → 十进制","给出字节,把有 1 的位置上的数值相加,就得到数字。标出了所有的 1。", "lang-zh"),
]
for code,title,sub,teoria,lc,exh,exintro,bodycls in LANGS:
    body=f"""<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><style>{CSS}</style></head>
<body class='{bodycls}'>
<div class='cover'><h1>{title}</h1><div class='s'>{sub} · solo binario→decimale</div></div>
<div class='{lc}'>{teoria}</div>
<h2>{exh}</h2><p>{exintro}</p>
<div class='grid'>{ESEMPI}</div>
</body></html>"""
    hp=f"{OUT}/dispensa-bit-byte-{code}.html"; open(hp,"w").write(body)
    pdf=f"{OUT}/Dispensa-Bit-Byte-{code}-v1.1.pdf"
    subprocess.run(["node",RENDER,hp,pdf,title,"Classe 1 · 01/10/2026","Corso Informatica — Classe 1"],env=ENV,check=True,capture_output=True)
    print("OK",code,"->",os.path.basename(pdf))
print("esempi:",len(NUMS))
