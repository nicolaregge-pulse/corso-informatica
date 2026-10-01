# -*- coding: utf-8 -*-
# Compito "Da binario a decimale" (SOLO questa direzione, come la lezione).
# 3 documenti monolingui IT/AR/ZH. Da consegnare su Classroom. Separato dalla dispensa.
import os, subprocess
POS=[128,64,32,16,8,4,2,1]
BYTES=["00000011","00001010","00010001","00100000","01000001","01010101","01100100","10000000","11110000","11111111"]
def postab():
    return "<table class='pos'><tr>"+"".join(f"<td>{v}</td>" for v in POS)+"</tr></table>"
def listbytes():
    return "".join(f"<li><code>{b}</code> = ______</li>" for b in BYTES)

CSS="""@page{size:A4}*{box-sizing:border-box}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:11pt;line-height:1.55;margin:0}
.cover{background:linear-gradient(160deg,#134a6e,#2c86b8);color:#fff;border-radius:12px;padding:12mm;text-align:center;margin-bottom:5mm}
.cover h1{font-size:19pt;margin:0}.cover .s{font-size:12pt;opacity:.93;margin-top:2mm}
h2{color:#12467a;font-size:14pt;margin:5mm 0 2mm;border-bottom:2px solid #2b7cc4;padding-bottom:1mm}
ol{padding-left:7mm}li{margin:2mm 0}
.attn{background:#fdecea;border:1px solid #e6b7b0;border-left:5px solid #c0392b;border-radius:6px;padding:3mm 4mm;margin:3mm 0}.attn b{color:#c0392b}
.es{background:#eef4fb;border:1px solid #9cc0e4;border-left:5px solid #2b7cc4;border-radius:6px;padding:3mm 4mm;margin:3mm 0}
.tuo{background:#f2ebf7;border:1px solid #d8c6ec;border-left:5px solid #8e44ad;border-radius:6px;padding:3mm 4mm;margin:3mm 0}.tuo b{color:#7030a0}
.consegna{background:#fff8e6;border:1px solid #e6cf7a;border-left:5px solid #d0a516;border-radius:6px;padding:3mm 4mm;margin:3mm 0}
table.pos{border-collapse:collapse;margin:2mm auto;font-size:11pt;text-align:center}
table.pos td{border:1px solid #2b7cc4;padding:1.5mm 4mm;background:#12467a;color:#fff}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px}
.lang-ar{direction:rtl;text-align:right;font-family:"Amiri",serif;font-size:13pt}
.lang-ar ol{padding-right:7mm;padding-left:0}
.lang-zh{font-family:"WenQuanYi Zen Hei",sans-serif;font-size:11.5pt}
"""

IT=f"""
<div class="attn"><b>Attenzione:</b> questo è il <b>compito da consegnare</b> su Classroom. La <b>dispensa</b> "Bit, byte e numeri binari" serve per studiare e <b>non</b> si consegna. Si fa <b>solo</b> da binario a decimale.</div>
<p><b>Ricorda i valori delle caselle</b> (da destra, ognuna il doppio):</p>{postab()}
<div class="es"><b>Esercizio 1 — converti ogni byte in decimale</b> (somma i valori dove c'è un 1):
<ol>{listbytes()}</ol></div>
<div class="tuo"><b>Esercizio 2 — Fallo tuo:</b> inventa <b>un byte</b> a piacere (8 cifre tra 0 e 1), scrivilo e <b>convertilo</b> in decimale. Poi: quanti <b>byte</b> pesa il tuo <b>nome</b>? (una lettera = 1 byte).</div>
<div class="consegna"><b>Che cosa consegni</b> (un solo Documento Google su Classroom):
<ol>
<li>Le risposte degli esercizi 1 e 2 (puoi anche fare una <b>foto</b> del lavoro a mano).</li>
<li><b>Riflessione</b>: 1) cosa <b>non sei riuscito</b> a fare e perché; 2) cosa <b>non hai capito</b>; 3) <b>note per il formatore</b> (un dubbio, una richiesta, un'idea).</li>
</ol></div>
"""
AR=f"""
<div class="attn"><b>انتبه:</b> هذا هو <b>الواجب الذي تُسلّمه</b> على Classroom. الورقة «البت والبايت» للدراسة فقط، لا تُسلَّم. نعمل <b>فقط</b> من الثنائي إلى العشري.</div>
<p><b>تذكّر قيم الخانات</b> (من اليمين، كل واحدة ضعف السابقة):</p>{postab()}
<div class="es"><b>التمرين 1 — حوّل كل بايت إلى العشري</b> (اجمع القيم حيث يوجد 1):
<ol>{listbytes()}</ol></div>
<div class="tuo"><b>التمرين 2 — اجعله لك:</b> اخترع <b>بايت</b> من عندك (8 أرقام بين 0 و1)، اكتبه و<b>حوّله</b> إلى العشري. ثم: كم <b>بايت</b> يزن <b>اسمك</b>؟ (حرف = 1 بايت).</div>
<div class="consegna"><b>ماذا تُسلّم</b> (مستند Google واحد على Classroom):
<ol>
<li>إجابات التمرينين 1 و2 (يمكن أيضًا <b>صورة</b> للعمل بخط اليد).</li>
<li><b>تأمّل</b>: 1) ما الذي <b>لم تستطع</b> فعله ولماذا؛ 2) ما الذي <b>لم تفهمه</b>؛ 3) <b>ملاحظات للمدرّب</b>.</li>
</ol></div>
"""
ZH=f"""
<div class="attn"><b>注意:</b>这是要交到 Classroom 的<b>作业</b>。“位和字节”那份讲义只用来学习,不用交。我们<b>只</b>做从二进制到十进制。</div>
<p><b>记住格子的数值</b>(从右边开始,每个是前一个的两倍):</p>{postab()}
<div class="es"><b>练习 1 — 把每个字节转换成十进制</b>(把有 1 的位置上的数值相加):
<ol>{listbytes()}</ol></div>
<div class="tuo"><b>练习 2 — 做成你自己的:</b>自己编一个<b>字节</b>(8 个 0 或 1),写下来并<b>转换</b>成十进制。然后:你的<b>名字</b>有多少<b>字节</b>?(一个字母 = 1 字节)。</div>
<div class="consegna"><b>要交什么</b>(一个 Google 文档,交到 Classroom):
<ol>
<li>练习 1 和 2 的答案(也可以<b>拍照</b>手写的作业)。</li>
<li><b>反思</b>:1)你<b>没能</b>做到什么,为什么;2)你<b>没理解</b>什么;3)<b>给老师的话</b>。</li>
</ol></div>
"""

OUT="/home/user/corso-godot/classe-1/bit-e-byte"
SP="/tmp/claude-0/-home-user-corso-godot/d65eff9d-e028-5dc2-8095-966645bd40b0/scratchpad"
RENDER="/home/user/corso-godot/strumenti/render-pdf/render_doc.js"
ENV=dict(os.environ); ENV["NODE_PATH"]=f"{SP}/node_modules"
LANGS=[("IT","Compito — da binario a decimale","Classe 1 · da consegnare su Classroom",IT,"lang-it",""),
 ("AR","واجب — من الثنائي إلى العشري","الصف الأول · يُسلَّم على Classroom",AR,"lang-ar","lang-ar"),
 ("ZH","作业 — 从二进制到十进制","一年级 · 交到 Classroom",ZH,"lang-zh","lang-zh")]
for code,title,sub,corpo,lc,bodycls in LANGS:
    body=f"""<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><style>{CSS}</style></head>
<body class='{bodycls}'><div class='cover'><h1>{title}</h1><div class='s'>{sub}</div></div>
<div class='{lc}'>{corpo}</div></body></html>"""
    hp=f"{OUT}/compito-bit-byte-{code}.html"; open(hp,"w").write(body)
    pdf=f"{OUT}/Compito-Bit-Byte-{code}-v1.0.pdf"
    subprocess.run(["node",RENDER,hp,pdf,title,"Classe 1 · 01/10/2026","Corso Informatica — Classe 1"],env=ENV,check=True,capture_output=True)
    print("OK",code)
print("bytes:",len(BYTES))
