# -*- coding: utf-8 -*-
import subprocess, os
SP=os.path.dirname(os.path.abspath(__file__))
GREEN="#2f9e57"; BLUE="#2b7cc4"; PURP="#8e44ad"; GH="#dff2e6"; BH="#dbe9f8"; PH="#ece3f5"; OR="#e08a1a"; OH="#fdeccf"

def keyboard_svg():
    W=720; fy=8; fh=30; y0=fy+fh+9; w=42; h=34; gap=5; x0=8
    svg=[f'<svg width="{W}" height="256" viewBox="0 0 {W} 256" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans,Arial">']
    fkeys=['Esc','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','Stamp']
    fw=(W-16-13*4)/14
    fx=8
    for k in fkeys:
        fill="#fff";stroke="#8aa0b4";tcol="#5a6b7b";sw=1;fs=9
        if k=='Stamp':
            fill=PH;stroke=PURP;tcol="#5b2d82";sw=2.5;fs=9
        svg.append(f'<rect x="{fx:.1f}" y="{fy}" width="{fw:.1f}" height="{fh}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        svg.append(f'<text x="{fx+fw/2:.1f}" y="{fy+fh/2+3}" text-anchor="middle" font-size="{fs}" font-weight="{"bold" if k=="Stamp" else "normal"}" fill="{tcol}">{k}</text>')
        fx+=fw+4
    rows=[
     ['`','1','2','3','4','5','6','7','8','9','0','-','=',('Backspace',2)],
     [('Tab',1.5),'Q','W','E','R','T','Y','U','I','O','P','[',']'],
     [('Bloc Maiusc',1.8),'A','S','D','F','G','H','J','K','L',';',"'",('Invio',1.7)],
     [('Maiusc',2.2),'Z','X','C','V','B','N','M',',','.','/',('Maiusc',2.2)],
     [('Ctrl',1.3),('Win',1.1),('Alt',1.1),('Spazio',6),('Alt',1.1),('Ctrl',1.3)],
    ]
    GK={'Win','S'}; BK={'C','V'}; seen={}
    for r,row in enumerate(rows):
        x=x0; y=y0+r*(h+gap)
        for key in row:
            lab,units=(key if isinstance(key,tuple) else (key,1)); kw=units*w+(units-1)*gap
            fill="#fff";stroke="#8aa0b4";tcol="#33475b";sw=1
            ig=lab in GK or (lab=='Maiusc' and seen.get('Maiusc',0)==0)
            ib=lab in BK or (lab=='Ctrl' and seen.get('Ctrl',0)==0)
            if ig: fill=GH;stroke=GREEN;tcol="#1f7a43";sw=2.5
            elif ib: fill=BH;stroke=BLUE;tcol="#1b3a5c";sw=2.5
            seen[lab]=seen.get(lab,0)+1
            svg.append(f'<rect x="{x}" y="{y}" width="{kw}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
            if lab=='Win':
                cx=x+kw/2
                svg.append(f'<g transform="translate({cx-7},{y+6})"><rect x="0" y="0" width="6" height="6" fill="{GREEN}"/><rect x="8" y="0" width="6" height="6" fill="{GREEN}"/><rect x="0" y="8" width="6" height="6" fill="{GREEN}"/><rect x="8" y="8" width="6" height="6" fill="{GREEN}"/></g>')
                svg.append(f'<text x="{cx}" y="{y+30}" text-anchor="middle" font-size="9" fill="{tcol}">Win</text>')
            else:
                fs=10 if len(lab)>3 else 13
                svg.append(f'<text x="{x+kw/2}" y="{y+h/2+4}" text-anchor="middle" font-size="{fs}" font-weight="{"bold" if (ig or ib) else "normal"}" fill="{tcol}">{lab}</text>')
            x+=kw+gap
    svg.append('</svg>')
    return "".join(svg)

def mouse_svg():
    return ('<svg width="230" height="180" viewBox="0 0 230 180" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans,Arial">'
     '<rect x="45" y="12" width="80" height="150" rx="38" fill="#fff" stroke="#8aa0b4" stroke-width="2"/>'
     f'<path d="M85 13 L87 13 A38 38 0 0 1 123 51 L123 78 L85 78 Z" fill="{OH}" stroke="{OR}" stroke-width="2.5"/>'
     '<line x1="85" y1="13" x2="85" y2="78" stroke="#8aa0b4" stroke-width="1.4"/>'
     '<line x1="47" y1="78" x2="123" y2="78" stroke="#8aa0b4" stroke-width="1.2"/>'
     '<rect x="79" y="20" width="12" height="26" rx="6" fill="#dfe6ee" stroke="#8aa0b4"/>'
     f'<text x="150" y="42" font-size="13" font-weight="bold" fill="{OR}">DESTRO</text>'
     f'<path d="M148 40 C138 42 132 44 126 46" fill="none" stroke="{OR}" stroke-width="2" marker-end="url(#a)"/>'
     f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="{OR}"/></marker></defs>'
     '</svg>')

KB=keyboard_svg(); MOUSE=mouse_svg()

# Legende trilingui compatte (una sola figura per tutti)
LEG_KB=('<div class="leg">'
 '<b style="color:#1f7a43">IT</b> — Verde = una PARTE (Windows+Maiusc+S) · Viola = TUTTO lo schermo (Windows+Stamp, tasto in alto a destra) · Blu = copia/incolla (Ctrl+C, Ctrl+V).<br>'
 '<b style="color:#1f7a43">AR</b> — <span class="ar">أخضر = جزء من الشاشة (Windows+Maiusc+S) · بنفسجي = كل الشاشة (Windows+Stamp، الزر أعلى اليمين) · أزرق = نسخ/لصق (Ctrl+C، Ctrl+V).</span><br>'
 '<b style="color:#1f7a43">ZH</b> — <span class="zh">绿色 = 屏幕的一部分 (Windows+Maiusc+S) · 紫色 = 整个屏幕 (Windows+Stamp，右上角的键) · 蓝色 = 复制/粘贴 (Ctrl+C、Ctrl+V)。</span>'
 '</div>')
LEG_MOUSE=('<div class="leg">'
 '<b style="color:#c9761a">IT</b> — Clic destro = premi il tasto DESTRO del mouse (in arancione). &nbsp; '
 '<b style="color:#c9761a">AR</b> <span class="ar">النقر بالزر الأيمن = اضغط الزر الأيمن للفأرة (البرتقالي).</span> &nbsp; '
 '<b style="color:#c9761a">ZH</b> <span class="zh">右键点击 = 按鼠标右键（橙色）。</span>'
 '</div>')

FIG_KB=f'<div class="fig">{KB}{LEG_KB}</div>'
FIG_MOUSE=f'<div class="fig">{MOUSE}{LEG_MOUSE}</div>'

def K(t): return f'<span class="key">{t}</span>'

IT=f'''
<div class="flag it">ITALIANO</div>
<div class="it">
<h3>1. Che cos'è uno screenshot</h3>
<ol>
<li>Uno <b>screenshot</b> è una <b>"foto" di quello che vedi sullo schermo</b>. Serve per salvare o mostrare una parte dello schermo.</li>
</ol>
<h3>2. Come si fa uno screenshot</h3>
<ol>
<li><b>Solo una parte:</b> premi INSIEME {K("Windows")} + {K("Maiusc")} + {K("S")}. Lo schermo diventa scuro, con il mouse <b>trascini un riquadro</b> sulla parte che vuoi. Quando lasci, l'immagine è <b>già copiata</b>.</li>
<li><b>Tutto lo schermo:</b> premi INSIEME {K("Windows")} + {K("Stamp")} (il tasto <b>Stamp</b>, scritto anche <b>PrtSc</b>, è <b>in alto a destra</b>). L'immagine si salva da sola in <b>Immagini &rarr; Screenshot</b>.</li>
</ol>
<h3>3. Copiare e incollare</h3>
<ol>
<li><b>Copiare</b> del testo selezionato: {K("Ctrl")} + {K("C")}.</li>
<li><b>Incollare</b> (immagine o testo): clicca nel punto giusto e premi {K("Ctrl")} + {K("V")}.</li>
<li><b>In Gemini:</b> clicca nella <b>casella del messaggio in basso</b> e fai {K("Ctrl")} + {K("V")}.</li>
</ol>
<h3>4. Usare Gemini per trascrivere (da immagine a testo)</h3>
<ol>
<li>Vai con l'account della scuola a questo indirizzo (scrivilo esattamente così): {K("gemini.google.com")}</li>
<li><b>Incolla</b> lo screenshot ({K("Ctrl")} + {K("V")}) e scrivi la richiesta: <span class="cmd">Trascrivi il testo di questa immagine.</span></li>
<li>Gemini ti dà il <b>testo scritto</b>: lo <b>copi</b> ({K("Ctrl")} + {K("C")}) e lo <b>incolli</b> nel documento ({K("Ctrl")} + {K("V")}).</li>
</ol>
<h3>5. Cenni di Google Lens</h3>
<ol>
<li>Nel browser Chrome: <b>clic destro</b> su un'immagine &rarr; <b>"Cerca immagine con Google"</b>; si apre Lens a destra, scegli <b>Testo</b>, seleziona e copia ({K("Ctrl")} + {K("C")}).</li>
</ol>
<h3>6. Prova tu (esercizio)</h3>
<ol>
<li>Fai uno <b>screenshot</b> di una pagina.</li>
<li><b>Incollalo in Gemini</b> e fatti <b>trascrivere</b> il testo.</li>
<li><b>Copia</b> il testo e <b>incollalo</b> in un documento di <b>Google Documenti</b>.</li>
</ol>
<h3>7. Cosa devi consegnare</h3>
<ol>
<li>Un <b>documento di Google Documenti</b>, caricato nel <b>compito su Classroom</b>, con dentro lo <b>screenshot</b>, il <b>testo trascritto</b> e la parte 8.</li>
</ol>
<h3>8. Alla fine scrivi sempre (OBBLIGATORIO)</h3>
<ol>
<li><b>Cosa NON sono riuscito/a a fare</b>, e <b>perché</b>.</li>
<li><b>Cosa NON ho capito</b> (le parti difficili). Non c'è vergogna: serve a te e al prof.</li>
</ol>
</div>
'''

AR=f'''
<div class="flag ar">العربية</div>
<div class="ar">
<h3>1. ما هي لقطة الشاشة (screenshot)</h3>
<ol>
<li><b>لقطة الشاشة</b> هي <b>«صورة» لما تراه على الشاشة</b>. تُستعمَل لحفظ أو إظهار جزء من الشاشة.</li>
</ol>
<h3>2. كيف تأخذ لقطة الشاشة</h3>
<ol>
<li><b>جزء فقط:</b> اضغط معًا {K("Windows")} + {K("Maiusc")} + {K("S")}. تصبح الشاشة داكنة، وبالفأرة <b>تسحب مستطيلًا</b> على الجزء الذي تريده. عند الإفلات تكون الصورة <b>منسوخة</b> مباشرة.</li>
<li><b>كل الشاشة:</b> اضغط معًا {K("Windows")} + {K("Stamp")} (زرّ <b>Stamp</b>، ويُكتب أيضًا <b>PrtSc</b>، موجود <b>أعلى اليمين</b>). تُحفَظ الصورة تلقائيًا في <b>الصور &larr; Screenshot</b>.</li>
</ol>
<h3>3. النسخ واللصق</h3>
<ol>
<li><b>نسخ</b> نصّ محدَّد: {K("Ctrl")} + {K("C")}.</li>
<li><b>لصق</b> (صورة أو نص): انقر في المكان المناسب واضغط {K("Ctrl")} + {K("V")}.</li>
<li><b>داخل Gemini:</b> انقر في <b>خانة الرسالة بالأسفل</b> واضغط {K("Ctrl")} + {K("V")}.</li>
</ol>
<h3>4. استخدام Gemini لتحويل الصورة إلى نصّ</h3>
<ol>
<li>ادخل بحساب المدرسة إلى هذا العنوان (اكتبه هكذا تمامًا): {K("gemini.google.com")}</li>
<li><b>الصق</b> لقطة الشاشة ({K("Ctrl")} + {K("V")}) واكتب الطلب: <span class="cmd">انسخ النصّ الموجود في هذه الصورة.</span></li>
<li>يعطيك Gemini <b>النصّ مكتوبًا</b>: <b>تنسخه</b> ({K("Ctrl")} + {K("C")}) و<b>تلصقه</b> في المستند ({K("Ctrl")} + {K("V")}).</li>
</ol>
<h3>5. لمحة عن Google Lens</h3>
<ol>
<li>في متصفّح Chrome: <b>انقر بالزر الأيمن</b> على صورة &larr; <b>«البحث عن الصورة باستخدام Google»</b>؛ يفتح Lens على اليمين، اختر <b>نص</b>، حدِّده وانسخه ({K("Ctrl")} + {K("C")}).</li>
</ol>
<h3>6. جرّب بنفسك (تمرين)</h3>
<ol>
<li>خذ <b>لقطة شاشة</b> لصفحة.</li>
<li><b>الصقها في Gemini</b> واطلب <b>تحويلها إلى نصّ</b>.</li>
<li><b>انسخ</b> النصّ و<b>الصقه</b> في مستند <b>Google Documenti</b>.</li>
</ol>
<h3>7. ما الذي تسلّمه</h3>
<ol>
<li>مستند <b>Google Documenti</b> واحد، مرفوعًا في <b>الواجب على Classroom</b>، يحتوي على <b>لقطة الشاشة</b> و<b>النصّ المكتوب</b> والجزء 8.</li>
</ol>
<h3>8. في النهاية اكتب دائمًا (إلزامي)</h3>
<ol>
<li><b>ما الذي لم أستطع فعله</b>، و<b>لماذا</b>.</li>
<li><b>ما الذي لم أفهمه</b> (الأجزاء الصعبة). لا عيب في ذلك: هذا يفيدك ويفيد الأستاذ.</li>
</ol>
</div>
'''

ZH=f'''
<div class="flag zh">中文</div>
<div class="zh">
<h3>1. 什么是屏幕截图（screenshot）</h3>
<ol>
<li><b>屏幕截图</b>就是<b>把你在屏幕上看到的内容「拍成一张照片」</b>。用来保存或展示屏幕的一部分。</li>
</ol>
<h3>2. 怎么截图</h3>
<ol>
<li><b>只截一部分：</b>同时按 {K("Windows")} + {K("Maiusc")} + {K("S")}。屏幕变暗，用鼠标<b>拖出一个方框</b>框住你要的部分。松开鼠标后，图片<b>已经被复制</b>。</li>
<li><b>整个屏幕：</b>同时按 {K("Windows")} + {K("Stamp")}（<b>Stamp</b> 键，也写作 <b>PrtSc</b>，在键盘<b>右上角</b>）。图片会自动保存到 <b>图片 &rarr; Screenshot</b>。</li>
</ol>
<h3>3. 复制和粘贴</h3>
<ol>
<li><b>复制</b>选中的文字：{K("Ctrl")} + {K("C")}。</li>
<li><b>粘贴</b>（图片或文字）：点到要放的位置，按 {K("Ctrl")} + {K("V")}。</li>
<li><b>在 Gemini 里：</b>点<b>下方的消息框</b>，按 {K("Ctrl")} + {K("V")}。</li>
</ol>
<h3>4. 用 Gemini 把图片转成文字</h3>
<ol>
<li>用学校账号打开这个网址（照着一模一样写）：{K("gemini.google.com")}</li>
<li><b>粘贴</b>截图（{K("Ctrl")} + {K("V")}），写下请求：<span class="cmd">转写这张图片里的文字。</span></li>
<li>Gemini 给你<b>写好的文字</b>：<b>复制</b>（{K("Ctrl")} + {K("C")}）再<b>粘贴</b>到文档里（{K("Ctrl")} + {K("V")}）。</li>
</ol>
<h3>5. Google Lens 简介</h3>
<ol>
<li>在 Chrome 浏览器里：在图片上<b>点右键</b> &rarr; <b>「用 Google 搜索图片」</b>；右侧打开 Lens，选<b>文字</b>，选中并复制（{K("Ctrl")} + {K("C")}）。</li>
</ol>
<h3>6. 你来试试（练习）</h3>
<ol>
<li>对一个页面<b>截图</b>。</li>
<li><b>粘贴到 Gemini</b>，让它<b>转写</b>文字。</li>
<li><b>复制</b>文字，<b>粘贴</b>到 <b>Google Documenti</b> 文档里。</li>
</ol>
<h3>7. 你要交什么</h3>
<ol>
<li>一个 <b>Google Documenti 文档</b>，上传到 <b>Classroom 的作业</b>里，里面要有<b>截图</b>、<b>转写的文字</b>和第 8 部分。</li>
</ol>
<h3>8. 最后一定要写（必做）</h3>
<ol>
<li><b>我没能做到什么</b>，以及<b>为什么</b>。</li>
<li><b>我没听懂什么</b>（难的部分）。这不丢人：对你和老师都有用。</li>
</ol>
</div>
'''

CSS='''
@page{size:A4;margin:14mm}*{box-sizing:border-box}
body{margin:0;color:#1a1a1a;line-height:1.6;font-size:11pt}
.it{font-family:"DejaVu Sans",Arial,sans-serif}
.zh{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif}
.ar{font-family:"Amiri","DejaVu Sans",serif;direction:rtl;text-align:right;font-size:13pt;line-height:1.95}
.cover{background:linear-gradient(160deg,#eef4fb,#f0ecfb);padding:10mm;border-radius:8px;text-align:center;margin-bottom:5mm}
.cover h1{color:#12467a;font-size:19pt;margin:0 0 2mm}.cover .s{color:#444;font-size:12pt}
.cover .d{color:#5a6b7b;font-size:10pt;margin-top:2mm}
.flag{font-size:15pt;font-weight:bold;color:#12467a;margin:6mm 0 2mm;border-bottom:3px solid #cfe0f0;padding-bottom:1.5mm}
.flag.ar{text-align:right}
h3{color:#12467a;font-size:12pt;margin:4mm 0 1.5mm;page-break-after:avoid}
.ar h3{text-align:right}
ol{margin:0 0 2mm;padding-left:7mm}.ar ol{padding-left:0;padding-right:7mm}
li{margin:1.6mm 0}
.key{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #cddae8;padding:0 6px;border-radius:4px;direction:ltr;display:inline-block;font-size:10.5pt;white-space:nowrap}
.cmd{font-family:"DejaVu Sans Mono",monospace;background:#f5f7fa;border-left:4px solid #2b7cc4;padding:1mm 3mm;border-radius:3px;display:block;margin:1.5mm 0;direction:ltr;text-align:left}
.ar .cmd{direction:rtl;text-align:right;border-left:none;border-right:4px solid #2b7cc4;font-family:"Amiri",serif}
.zh .cmd{font-family:"WenQuanYi Zen Hei",monospace}
.fig{text-align:center;margin:3mm 0 5mm;page-break-inside:avoid}
.fig svg{max-width:100%}
.leg{font-size:9pt;color:#33475b;margin-top:2mm;text-align:left;line-height:1.7}
.leg .ar{font-size:10pt;display:inline}
.leg .zh{display:inline}
.pagebreak{page-break-before:always}
'''

html=f'''<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover it">
<h1>Cattura schermo · Copia-incolla · Trascrivi con l'AI</h1>
<div class="s">التقاط الشاشة · نسخ ولصق · التحويل إلى نص بالذكاء الاصطناعي &nbsp;·&nbsp; 屏幕截图 · 复制粘贴 · 用 AI 转写文字</div>
<div class="d">Classe 1 · Informatica · 30/09/2026 · IT / العربية / 中文</div>
</div>

<div class="fig-title it" style="text-align:center;color:#12467a;font-weight:bold;font-size:12pt;margin-bottom:1mm">La tastiera — i tasti da usare / لوحة المفاتيح / 键盘</div>
{FIG_KB}
<div class="fig-title it" style="text-align:center;color:#12467a;font-weight:bold;font-size:12pt;margin:4mm 0 1mm">Il mouse — il clic destro / الفأرة / 鼠标</div>
{FIG_MOUSE}

{IT}
<div class="pagebreak"></div>
{AR}
<div class="pagebreak"></div>
{ZH}
</body></html>'''

open(f"{SP}/cattura-copia-trascrivi-tri.html","w",encoding="utf-8").write(html)
subprocess.run(["node",f"{SP}/render_generic.js",f"{SP}/cattura-copia-trascrivi-tri.html",f"{SP}/20260930_Classe-1_Cattura-Copia-Trascrivi_TRILINGUE_v1.pdf"],check=True)
print("FATTO trilingue")
