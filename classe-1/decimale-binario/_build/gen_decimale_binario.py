# -*- coding: utf-8 -*-
# Lezione 02/10/2026 Classe 1 — "Da DECIMALE a BINARIO" (come alla lavagna):
#   metodo delle DIVISIONI PER 2 (resti letti dal basso verso l'alto) + prova con le CASELLE
#   + BYTE (zeri davanti fino a 8 cifre).
# Genera: Dispensa IT/AR/ZH + Compito IT/AR/ZH (PDF) con grafica IDENTICA (§2.19): la tabella
# delle divisioni e la griglia del byte sono le STESSE immagini (SVG) in dispensa e compito.
# Il compito ha un NUCLEO BASE (per tutti) + SFIDE EXTRA (per chi finisce prima) (§2.24).
import os, subprocess, base64, json

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = "/home/user/corso-godot"
VER = "1.0"
DATA = "02/10/2026"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
POS = [128, 64, 32, 16, 8, 4, 2, 1]

def divisioni(n):
    r = []
    while n > 0:
        r.append((n, n % 2)); n //= 2
    return r
def binario(n): return format(n, 'b')
def byte(n): return format(n, '08b')

# ------------------------------------------------------------------ immagini (SVG)
def svg_div(n, piena=True, righe=8, lab=("÷ 2", "resto"), h=None):
    """Tabella delle divisioni come alla lavagna: numeri a sinistra, resti a destra,
    linea rossa in mezzo, freccia verde che sale (si legge dal basso verso l'alto)."""
    rows = divisioni(n) if piena else [(n, None)] + [(None, None)] * (righe - 1)
    if piena: righe = len(rows)
    RH, TOP, W = 30, 34, 190
    H = TOP + righe * RH + 8
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*0.22:.0f}mm' "
         f"height='{H*0.22:.0f}mm' class='svgdiv'>",
         f"<text x='55' y='20' font-size='13' fill='#1e8a6a' text-anchor='middle' font-weight='bold'>{lab[0]}</text>",
         f"<text x='130' y='20' font-size='13' fill='#1e8a6a' text-anchor='middle' font-weight='bold'>{lab[1]}</text>",
         f"<line x1='95' y1='6' x2='95' y2='{H-4}' stroke='#d0392b' stroke-width='2.2'/>"]
    for i, (q, r) in enumerate(rows):
        y = TOP + i * RH + 21
        if not piena:
            s.append(f"<line x1='18' y1='{y+6}' x2='160' y2='{y+6}' stroke='#c9d6e3' stroke-dasharray='3 3'/>")
        if q is not None:
            col = "#d0392b" if i == 0 else "#1f5fbf"
            s.append(f"<text x='55' y='{y}' font-size='19' fill='{col}' text-anchor='middle' font-weight='bold'>{q}</text>")
        if r is not None:
            s.append(f"<text x='130' y='{y}' font-size='19' fill='#1a2330' text-anchor='middle' font-weight='bold'>{r}</text>")
    # freccia verde verso l'alto
    y0, y1 = TOP + righe * RH - 4, TOP + 8
    s.append(f"<line x1='172' y1='{y0}' x2='172' y2='{y1+6}' stroke='#1e8a6a' stroke-width='2.5'/>"
             f"<polygon points='164,{y1+10} 180,{y1+10} 172,{y1-4}' fill='#1e8a6a'/>")
    s.append("</svg>")
    return "".join(s)

def svg_byte(n=None, mostra_valori=True):
    """Griglia del byte (8 caselle, valori 128..1) — stessa grafica di ieri.
    1 in verde; gli ZERI AGGIUNTI DAVANTI in rosso (come alla lavagna)."""
    CW, CH, W = 34, 26, 8 * 34 + 2
    H = CH * 2 + 2
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*0.26:.0f}mm' height='{H*0.26:.0f}mm' class='svgbyte'>"]
    bits = byte(n) if n is not None else None
    lead = (8 - len(binario(n))) if n is not None else 0
    for i, v in enumerate(POS):
        x = 1 + i * CW
        s.append(f"<rect x='{x}' y='1' width='{CW}' height='{CH}' fill='#f3f7fb' stroke='#9cc0e4'/>"
                 f"<text x='{x+CW/2}' y='18' font-size='12' text-anchor='middle' fill='#12467a'>{v}</text>")
        fill, txt, col, fw = "#ffffff", "", "#1a2330", "normal"
        if bits:
            txt = bits[i]
            if txt == "1": fill, col, fw = "#eafaf0", "#1e7a44", "bold"
            elif i < lead: col = "#d0392b"
        s.append(f"<rect x='{x}' y='{CH+1}' width='{CW}' height='{CH}' fill='{fill}' stroke='#9cc0e4'/>"
                 f"<text x='{x+CW/2}' y='{CH+19}' font-size='15' text-anchor='middle' fill='{col}' font-weight='{fw}'>{txt}</text>")
    s.append("</svg>")
    return "".join(s)

def somma(n): return " + ".join(str(POS[i]) for i, c in enumerate(byte(n)) if c == "1")

# ------------------------------------------------------------------ dati
ESEMPIO = 37
ESEMPI_SVOLTI = [6, 13, 25, 50, 100, 200]
BASE = [5, 6, 9, 12, 20, 25, 31, 44]           # nucleo base: tutti
EXTRA = [50, 77, 100, 128, 150, 200, 255]      # sfide per chi finisce prima

LAV = base64.b64encode(open(f"{ROOT}/classe-1/lavagne/20261002-decimale-binario.jpg", "rb").read()).decode()
LAV2 = base64.b64encode(open(f"{ROOT}/classe-1/lavagne/20261002-decimale-binario-17.jpg", "rb").read()).decode()
FONT = {w: base64.b64encode(open(f"{ROOT}/strumenti/render-pdf/fonts/amiri-arabic-{w}-normal.woff2", "rb").read()).decode()
        for w in (400, 700)}

CSS = """@page{size:A4;margin:14mm 14mm 16mm}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@font-face{font-family:"Amiri";font-weight:400;src:url(data:font/woff2;base64,%s) format("woff2")}
@font-face{font-family:"Amiri";font-weight:700;src:url(data:font/woff2;base64,%s) format("woff2")}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:11pt;line-height:1.5;margin:0}
.cover{background:linear-gradient(160deg,#134a6e,#2c86b8);color:#fff;border-radius:12px;padding:9mm;text-align:center;margin-bottom:5mm}
.cover h1{font-size:20pt;margin:0}.cover .s{font-size:11.5pt;opacity:.93;margin-top:2mm}
h2{color:#12467a;font-size:14pt;margin:5mm 0 2mm;border-bottom:2px solid #2b7cc4;padding-bottom:1mm;page-break-after:avoid}
p{margin:2mm 0}ol{padding-left:7mm;margin:2mm 0}li{margin:1.4mm 0}
.key{background:#eef4fb;border:1px solid #9cc0e4;border-left:5px solid #2b7cc4;border-radius:6px;padding:3mm 4mm;margin:3mm 0;page-break-inside:avoid}
.vinci{background:#eafaf0;border:1px solid #bfe6cf;border-left:5px solid #2f9e57;border-radius:6px;padding:3mm 4mm;margin:3mm 0;page-break-inside:avoid}.vinci b{color:#1e7a44}
.attn{background:#fdecea;border:1px solid #e6b7b0;border-left:5px solid #c0392b;border-radius:6px;padding:3mm 4mm;margin:3mm 0;page-break-inside:avoid}.attn b{color:#c0392b}
.nota{background:#fff8e1;border:1px solid #f0d78c;border-left:5px solid #e0a800;border-radius:6px;padding:3mm 4mm;margin:3mm 0;page-break-inside:avoid}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px;font-size:11.5pt;direction:ltr;unicode-bidi:embed}
.fig{text-align:center;margin:3mm 0;border:1px solid #cfe0f0;border-radius:10px;padding:3mm;page-break-inside:avoid}
.fig img{max-width:62%%}.cap{font-size:9.5pt;color:#667;margin-top:1.5mm}
.esempio{display:flex;gap:6mm;align-items:flex-start;page-break-inside:avoid;direction:ltr}
.esempio .dx{flex:1}.dx p{margin:1.5mm 0}
.grid{display:flex;flex-wrap:wrap;gap:3mm;direction:ltr}
.card{border:1px solid #d5e0ec;border-radius:8px;padding:2.5mm 4mm;background:#fafcff;page-break-inside:avoid;width:100%%;display:flex;gap:6mm}
.card .t{font-weight:bold;color:#12467a;margin-bottom:1mm}
.card .dx{flex:1;font-size:10.5pt}
.svgdiv,.svgbyte{display:block;flex-shrink:0}
.riga{margin:2mm 0;font-size:11pt}
.conti{border:1px dashed #9cc0e4;border-radius:6px;height:16mm;margin-top:1.5mm;font-size:8.5pt;color:#7a8aa0;padding:1mm 2mm}
.nome{margin:3mm 0}
.lang-ar .testo{direction:rtl;text-align:right;font-family:"Amiri",serif;font-size:13.5pt}
.lang-ar .testo ol{padding-right:7mm;padding-left:0}
.lang-ar .lbl{font-family:"Amiri",serif;font-size:12pt}
.lang-zh{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif}
.foot{font-size:8.5pt;color:#8a9bb0;border-top:1px solid #dce5ef;margin-top:6mm;padding-top:1.5mm}
""" % (FONT[400], FONT[700])

# ------------------------------------------------------------------ testi
T = {
"IT": dict(
  lab=("÷ 2", "resto"),
  titolo="Da decimale a binario", sub=f"Classe 1 · spiegazione · italiano · {DATA}",
  ctitolo="Compito — Da decimale a binario", csub=f"Classe 1 · da consegnare · {DATA}",
  bin="binario", byte="byte (8 cifre)", prova="prova con le caselle",
  teoria=f"""
<div class="key"><b>Ieri</b> abbiamo fatto la strada da 0 e 1 al numero (binario → decimale).
<b>Oggi facciamo la strada al contrario:</b> dal numero di tutti i giorni a 0 e 1 (decimale → binario).</div>
<h2>1. Ripasso in 30 secondi</h2>
<ol><li>Un <b>bit</b> è una sola cifra: <b>0</b> oppure <b>1</b>.</li>
<li>Un <b>byte</b> sono <b>8 bit</b>: 8 caselle.</li>
<li>Le caselle valgono, da destra: <b>1, 2, 4, 8, 16, 32, 64, 128</b> (ogni volta il doppio).</li></ol>
<h2>2. Il metodo delle divisioni per 2 (come alla lavagna)</h2>
<ol><li>Scrivi il <b>numero</b> in alto a sinistra e tira una <b>linea</b> verticale.</li>
<li><b>Dividi per 2</b>: il <b>risultato</b> va sotto, a sinistra; il <b>resto</b> (0 oppure 1) va a destra della linea.</li>
<li><b>Continua</b> a dividere il nuovo numero, finché arrivi a <b>1</b>. L'ultimo 1 passa a destra così com'è.</li>
<li><b>Leggi i resti dal basso verso l'alto</b>: quello è il numero in binario.</li></ol>
<div class="vinci"><b>Trucco:</b> il resto è facilissimo. <b>Numero pari → resto 0</b>, <b>numero dispari → resto 1</b>.
Non serve nemmeno fare la divisione col resto: basta guardare se il numero è pari o dispari.</div>
<h2>3. L'esempio della lavagna: 37</h2>
@@ESEMPIO@@
<h2>4. Il byte: gli zeri davanti</h2>
<p>Un byte ha sempre <b>8 caselle</b>. Se il numero binario ha meno cifre, si aggiungono degli
<b>zeri a SINISTRA</b> (davanti). Gli zeri davanti <b>non cambiano il valore</b>, come <code>007</code> che vale 7.</p>
<p><code>100101</code> ha 6 cifre → aggiungo 2 zeri davanti → <code>00100101</code> (gli zeri aggiunti sono in rosso).</p>
@@LAVAGNA@@
<h2>5. Errori da evitare</h2>
<ol><li><b>Leggere i resti dall'alto in basso.</b> Per 37 verrebbe <code>101001</code> = 41: sbagliato. Si legge <b>dal basso</b>.</li>
<li><b>Dimenticare l'ultimo 1</b> (quello in fondo alla tabella).</li>
<li><b>Mettere gli zeri a destra</b> invece che a sinistra: <code>10010100</code> = 148, un altro numero.</li></ol>
<div class="nota"><b>Carta e penna:</b> rifai a mano la tabella del 37 sul tuo foglio, senza guardare. Se ti torna 100101, hai capito il metodo.</div>
<h2>6. Il riassunto in 4 parole</h2>
<p><b>Dividi</b> per 2 · scrivi il <b>resto</b> · leggi <b>dal basso</b> · metti gli <b>zeri davanti</b> fino a 8.</p>
""",
  esempio_txt=lambda: f"""<p>37 diviso 2 fa 18, resto <b>1</b>. 18 diviso 2 fa 9, resto <b>0</b>. 9 diviso 2 fa 4, resto <b>1</b>.
4 diviso 2 fa 2, resto <b>0</b>. 2 diviso 2 fa 1, resto <b>0</b>. Il 1 finale passa a destra: <b>1</b>.</p>
<p>Leggo i resti <b>dal basso verso l'alto</b>: <code>100101</code>.</p>
<p><b>La prova con le caselle:</b> dove c'è un 1 sommo il valore: <b>{somma(37)} = 37</b>. Giusto!</p>""",
  lav2cap="La prova della classe alla lavagna: 17 diviso 2 più volte; i resti letti dal basso danno 10001. Nel byte diventa 00010001.",
  lavcap="La lavagna della nostra lezione: 37 diviso per 2 più volte, i resti letti dal basso verso l'alto (100101), la prova 32 + 4 + 1 = 37 e il byte 00100101.",
  svolti="7. Altri esempi svolti", svolti_intro="Guarda come si fa con altri numeri. Copre la parte destra con la mano e prova da solo!",
  sfida="""<div class="vinci"><b>Sfida per chi va veloce:</b> scrivi in binario la <b>tua età</b> e il <b>giorno</b> in cui sei nato.
Poi prova 255: viene <code>11111111</code>, tutto pieno. È il numero più grande che sta in un byte!</div>""",
  attn="""<div class="attn"><b>Questo è il compito da consegnare.</b> Per ogni numero: <b>1)</b> fai le divisioni per 2
nella tabella (resto a destra); <b>2)</b> leggi i resti <b>dal basso verso l'alto</b> e scrivi il numero binario;
<b>3)</b> scrivi il <b>byte</b> con 8 cifre (zeri davanti); <b>4)</b> fai la prova con le caselle.
I conti a mano li fai sul tuo foglio o nello spazio tratteggiato.</div>""",
  nome="<b>Nome e Cognome:</b> ______________________________",
  es="Esempio", ex="Esercizio", numero="numero",
  p1="Parte 1 — Nucleo base (per tutti)", p2="Parte 2 — Sfide extra (per chi finisce prima)",
  conti="conti / prova",
  tuo="Il tuo numero (età, giorno di nascita, numero di maglia…): ______  →  byte: ____________",
  spiega="Spiega con parole tue: perché i resti si leggono dal basso verso l'alto? ______________________________________________",
  foot="Corso Informatica — Classe 1 · Da decimale a binario",
),
"AR": dict(
  lab=("÷ 2", "الباقي"),
  titolo="من العشري إلى الثنائي", sub=f"الصف الأول · شرح · العربية · {DATA}",
  ctitolo="واجب — من العشري إلى الثنائي", csub=f"الصف الأول · يُسلَّم · {DATA}",
  bin="الثنائي", byte="البايت (8 أرقام)", prova="التحقق بالخانات",
  teoria=f"""
<div class="key"><b>بالأمس</b> ذهبنا من 0 و 1 إلى العدد (ثنائي ← عشري).
<b>اليوم نسير في الطريق المعاكس:</b> من العدد العادي إلى 0 و 1 (عشري ← ثنائي).</div>
<h2>1. مراجعة في 30 ثانية</h2>
<ol><li><b>البِت</b> رقم واحد فقط: <b>0</b> أو <b>1</b>.</li>
<li><b>البايت</b> = <b>8 بتات</b>: 8 خانات.</li>
<li>قيم الخانات من اليمين: <b>1، 2، 4، 8، 16، 32، 64، 128</b> (كل مرة الضعف).</li></ol>
<h2>2. طريقة القسمة على 2 (كما على اللوحة)</h2>
<ol><li>اكتب <b>العدد</b> في الأعلى وارسم <b>خطًا</b> عموديًا.</li>
<li><b>اقسم على 2</b>: <b>الناتج</b> يُكتب تحته، و<b>الباقي</b> (0 أو 1) يُكتب بجانب الخط.</li>
<li><b>استمر</b> في القسمة حتى تصل إلى <b>1</b>. آخر 1 ينتقل إلى عمود الباقي كما هو.</li>
<li><b>اقرأ البواقي من الأسفل إلى الأعلى</b>: هذا هو العدد الثنائي.</li></ol>
<div class="vinci"><b>حيلة:</b> الباقي سهل جدًا. <b>عدد زوجي ← الباقي 0</b>، <b>عدد فردي ← الباقي 1</b>.</div>
<h2>3. مثال اللوحة: 37</h2>
@@ESEMPIO@@
<h2>4. البايت: الأصفار في البداية</h2>
<p>للبايت دائمًا <b>8 خانات</b>. إذا كان العدد الثنائي أقصر، نضيف <b>أصفارًا على اليسار</b> (في البداية).
الأصفار في البداية <b>لا تغيّر القيمة</b>، مثل <code>007</code> = 7.</p>
<p><code>100101</code> فيه 6 أرقام ← نضيف صفرين في البداية ← <code>00100101</code> (الأصفار المضافة باللون الأحمر).</p>
@@LAVAGNA@@
<h2>5. أخطاء يجب تجنّبها</h2>
<ol><li><b>قراءة البواقي من الأعلى إلى الأسفل.</b> للعدد 37 ينتج <code>101001</code> = 41: خطأ. نقرأ <b>من الأسفل</b>.</li>
<li><b>نسيان آخر 1</b> في أسفل الجدول.</li>
<li><b>وضع الأصفار على اليمين</b> بدل اليسار: <code>10010100</code> = 148، عدد آخر.</li></ol>
<div class="nota"><b>ورقة وقلم:</b> أعد رسم جدول العدد 37 بخط يدك دون أن تنظر. إذا حصلت على 100101 فقد فهمت الطريقة.</div>
<h2>6. الملخّص في 4 كلمات</h2>
<p><b>اقسم</b> على 2 · اكتب <b>الباقي</b> · اقرأ <b>من الأسفل</b> · ضع <b>الأصفار في البداية</b> حتى 8.</p>
""",
  esempio_txt=lambda: f"""<p class="lbl">37 ÷ 2 = 18 والباقي <b>1</b>. 18 ÷ 2 = 9 والباقي <b>0</b>. 9 ÷ 2 = 4 والباقي <b>1</b>.
4 ÷ 2 = 2 والباقي <b>0</b>. 2 ÷ 2 = 1 والباقي <b>0</b>. آخر 1 ينتقل إلى اليمين: <b>1</b>.</p>
<p class="lbl">أقرأ البواقي <b>من الأسفل إلى الأعلى</b>: <code>100101</code>.</p>
<p class="lbl"><b>التحقق بالخانات:</b> <b>{somma(37)} = 37</b>. صحيح!</p>""",
  lav2cap="تجربة الصف على اللوحة: 17 مقسومًا على 2 عدة مرات؛ البواقي من الأسفل تعطي 10001. في البايت تصبح 00010001.",
  lavcap="لوحة درسنا: 37 مقسومًا على 2 عدة مرات، البواقي تُقرأ من الأسفل إلى الأعلى (100101)، التحقق 32 + 4 + 1 = 37 والبايت 00100101.",
  svolti="7. أمثلة أخرى محلولة", svolti_intro="انظر كيف نعمل مع أعداد أخرى. غطِّ الجزء الأيمن بيدك وجرّب وحدك!",
  sfida="""<div class="vinci"><b>تحدٍّ للسريعين:</b> اكتب بالثنائي <b>عمرك</b> و<b>يوم</b> ميلادك.
ثم جرّب 255: النتيجة <code>11111111</code>، كلها ممتلئة. إنه أكبر عدد يتّسع له البايت!</div>""",
  attn="""<div class="attn"><b>هذا هو الواجب الذي يُسلَّم.</b> لكل عدد: <b>1)</b> اقسم على 2 في الجدول (الباقي على اليمين)؛
<b>2)</b> اقرأ البواقي <b>من الأسفل إلى الأعلى</b> واكتب العدد الثنائي؛ <b>3)</b> اكتب <b>البايت</b> بـ 8 أرقام (أصفار في البداية)؛
<b>4)</b> تحقّق بالخانات. الحسابات اليدوية على ورقتك أو في المساحة المنقّطة.</div>""",
  nome="<b>الاسم واللقب:</b> ______________________________",
  es="مثال", ex="تمرين", numero="العدد",
  p1="الجزء 1 — الأساس (للجميع)", p2="الجزء 2 — تحديات إضافية (لمن ينهي أولًا)",
  conti="الحساب / التحقق",
  tuo="عددك (العمر، يوم الميلاد، رقم القميص…): ______  ←  البايت: ____________",
  spiega="اشرح بكلماتك: لماذا نقرأ البواقي من الأسفل إلى الأعلى؟ ______________________________",
  foot="Corso Informatica — Classe 1 · من العشري إلى الثنائي",
),
"ZH": dict(
  lab=("÷ 2", "余数"),
  titolo="从十进制到二进制", sub=f"一年级 · 讲解 · 中文 · {DATA}",
  ctitolo="作业 — 从十进制到二进制", csub=f"一年级 · 要交 · {DATA}",
  bin="二进制", byte="字节(8 位)", prova="用格子检查",
  teoria=f"""
<div class="key"><b>昨天</b>我们从 0 和 1 走到数字(二进制 → 十进制)。
<b>今天走相反的路:</b>从平常的数字到 0 和 1(十进制 → 二进制)。</div>
<h2>1. 30 秒复习</h2>
<ol><li><b>位(bit)</b>只有一个数字:<b>0</b> 或 <b>1</b>。</li>
<li><b>字节(byte)</b>= <b>8 位</b>:8 个格子。</li>
<li>格子的数值,从右开始:<b>1、2、4、8、16、32、64、128</b>(每次翻倍)。</li></ol>
<h2>2. 除以 2 的方法(和白板一样)</h2>
<ol><li>在左上方写下<b>数字</b>,画一条<b>竖线</b>。</li>
<li><b>除以 2</b>:<b>商</b>写在下面(左边);<b>余数</b>(0 或 1)写在竖线右边。</li>
<li>一直<b>继续</b>除,直到得到 <b>1</b>。最后的 1 直接写到右边。</li>
<li><b>从下往上读余数</b>:这就是二进制数。</li></ol>
<div class="vinci"><b>技巧:</b>余数非常简单。<b>偶数 → 余数 0</b>,<b>奇数 → 余数 1</b>。只要看数字是偶数还是奇数就行!</div>
<h2>3. 白板上的例子:37</h2>
@@ESEMPIO@@
<h2>4. 字节:前面补 0</h2>
<p>一个字节总是有 <b>8 个格子</b>。如果二进制数位数不够,就在<b>左边(前面)补 0</b>。
前面的 0 <b>不改变数值</b>,就像 <code>007</code> 还是 7。</p>
<p><code>100101</code> 有 6 位 → 前面补 2 个 0 → <code>00100101</code>(补上的 0 是红色)。</p>
@@LAVAGNA@@
<h2>5. 要避免的错误</h2>
<ol><li><b>从上往下读余数。</b>37 会变成 <code>101001</code> = 41:错了。要<b>从下往上</b>读。</li>
<li><b>忘了最后的 1</b>(表格最下面那个)。</li>
<li><b>把 0 补在右边</b>而不是左边:<code>10010100</code> = 148,是另一个数。</li></ol>
<div class="nota"><b>纸和笔:</b>不看书,在你的纸上自己画一遍 37 的表格。如果得到 100101,你就懂了。</div>
<h2>6. 四个词总结</h2>
<p><b>除以</b> 2 · 写<b>余数</b> · <b>从下往上</b>读 · <b>前面补 0</b> 到 8 位。</p>
""",
  esempio_txt=lambda: f"""<p>37 ÷ 2 = 18,余 <b>1</b>。18 ÷ 2 = 9,余 <b>0</b>。9 ÷ 2 = 4,余 <b>1</b>。
4 ÷ 2 = 2,余 <b>0</b>。2 ÷ 2 = 1,余 <b>0</b>。最后的 1 写到右边:<b>1</b>。</p>
<p><b>从下往上</b>读余数:<code>100101</code>。</p>
<p><b>用格子检查:</b>有 1 的地方把数值相加:<b>{somma(37)} = 37</b>。对了!</p>""",
  lav2cap="全班在白板上的练习:17 多次除以 2;余数从下往上读得到 10001。写成字节是 00010001。",
  lavcap="我们这节课的白板:37 多次除以 2,余数从下往上读(100101),检查 32 + 4 + 1 = 37,以及字节 00100101。",
  svolti="7. 更多例题", svolti_intro="看看其他数字怎么做。用手挡住右边,自己试一试!",
  sfida="""<div class="vinci"><b>给快的同学的挑战:</b>用二进制写出<b>你的年龄</b>和你出生的<b>日子</b>。
再试 255:结果是 <code>11111111</code>,全满了。这是一个字节能放下的最大的数!</div>""",
  attn="""<div class="attn"><b>这是要交的作业。</b>每个数字:<b>1)</b>在表格里除以 2(余数写右边);
<b>2)</b><b>从下往上</b>读余数,写出二进制数;<b>3)</b>写出 8 位的<b>字节</b>(前面补 0);<b>4)</b>用格子检查。
手算写在你的纸上或虚线框里。</div>""",
  nome="<b>姓名:</b> ______________________________",
  es="例子", ex="练习", numero="数字",
  p1="第一部分 — 基础(所有人)", p2="第二部分 — 额外挑战(先做完的同学)",
  conti="计算 / 检查",
  tuo="你的数字(年龄、出生日、球衣号码……):______  →  字节:____________",
  spiega="用你自己的话解释:为什么余数要从下往上读?______________________________",
  foot="Corso Informatica — Classe 1 · 从十进制到二进制",
),
}

def esempio_html(L, n=ESEMPIO):
    t = T[L]
    return (f"<div class='esempio'>{svg_div(n, True, lab=t['lab'])}<div class='dx testo'>{t['esempio_txt']()}"
            f"<p class='lbl'><b>{t['byte']}:</b></p>{svg_byte(n)}</div></div>")

def card_svolto(L, n):
    t = T[L]
    return (f"<div class='card'>{svg_div(n, True, lab=t['lab'])}<div class='dx'>"
            f"<div class='t'>{n}</div><div class='lbl'>{t['bin']}:</div><p><code>{binario(n)}</code></p>"
            f"<div class='lbl'>{t['byte']}:</div>{svg_byte(n)}"
            f"<p style='font-size:9pt'>{t['prova']}: {somma(n)} = {n}</p></div></div>")

def card_compito(L, k, n):
    t = T[L]
    return (f"<div class='card'>{svg_div(n, False, lab=t['lab'])}<div class='dx'>"
            f"<div class='t lbl'>{t['ex']} {k} — {t['numero']} {n}</div>"
            f"<div class='riga'><span class='lbl'>{t['bin']}:</span> ________________</div>"
            f"<div class='lbl'>{t['byte']}:</div>{svg_byte(None)}"
            f"<div class='conti lbl'>{t['conti']}</div></div></div>")

def page(L, body):
    cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
    return (f"<!DOCTYPE html><html lang='{L.lower()}'><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body class='{cls}'>{body}</body></html>")

def pdf(html_path, pdf_path):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", "file://" + html_path], check=True, capture_output=True)

def main():
    for L, t in T.items():
        lav = (f"<div class='fig'><img src='data:image/jpeg;base64,{LAV}'><div class='cap testo'>{t['lavcap']}</div></div>"
               f"<div class='fig'><img style='max-width:38%' src='data:image/jpeg;base64,{LAV2}'><div class='cap testo'>{t['lav2cap']}</div></div>")
        teoria = t["teoria"].replace("@@ESEMPIO@@", esempio_html(L)).replace("@@LAVAGNA@@", lav)
        disp = (f"<div class='cover'><h1>{t['titolo']}</h1><div class='s'>{t['sub']}</div></div>"
                f"<div class='testo'>{teoria}<h2>{t['svolti']}</h2><p>{t['svolti_intro']}</p></div>"
                f"<div class='grid'>{''.join(card_svolto(L, n) for n in ESEMPI_SVOLTI)}</div>"
                f"<div class='testo'>{t['sfida']}</div><div class='foot'>{t['foot']} · v{VER}</div>")
        hp = f"{OUT}/dispensa-decimale-binario-{L}.html"; open(hp, "w").write(page(L, disp))
        pdf(hp, f"{OUT}/Dispensa-Decimale-Binario-{L}-v{VER}.pdf")

        comp = (f"<div class='cover'><h1>{t['ctitolo']}</h1><div class='s'>{t['csub']}</div></div>"
                f"<div class='testo'>{t['attn']}<div class='nome'>{t['nome']}</div>"
                f"<h2>{t['es']}: 37</h2></div>{esempio_html(L)}"
                f"<div class='testo'><h2>{t['p1']}</h2></div>"
                f"<div class='grid'>{''.join(card_compito(L, i+1, n) for i, n in enumerate(BASE))}</div>"
                f"<div class='testo'><h2>{t['p2']}</h2></div>"
                f"<div class='grid'>{''.join(card_compito(L, i+1+len(BASE), n) for i, n in enumerate(EXTRA))}</div>"
                f"<div class='testo'><p class='riga'>{t['tuo']}</p><p class='riga'>{t['spiega']}</p></div>"
                f"<div class='foot'>{t['foot']} · v{VER}</div>")
        hp = f"{OUT}/compito-decimale-binario-{L}.html"; open(hp, "w").write(page(L, comp))
        pdf(hp, f"{OUT}/Compito-Decimale-Binario-{L}-v{VER}.pdf")
        print("OK", L)
    # chiave di correzione (per l'AI alla chiusura) — va nel repo PRIVATO
    key = {"compito": "Compito — Da decimale a binario", "classe": "1INF", "data": "2026-10-02",
           "esempio": {"n": ESEMPIO, "binario": binario(ESEMPIO), "byte": byte(ESEMPIO)},
           "esercizi": [{"k": i+1, "n": n, "livello": "base" if i < len(BASE) else "extra",
                         "binario": binario(n), "byte": byte(n)} for i, n in enumerate(BASE + EXTRA)]}
    kp = "/home/user/corso-informatica-riservato/materiale-esami/chiavi/1INF-da-decimale-a-binario.json"
    os.makedirs(os.path.dirname(kp), exist_ok=True); json.dump(key, open(kp, "w"), ensure_ascii=False, indent=1)
    print("chiave ->", kp)

if __name__ == "__main__":
    main()
