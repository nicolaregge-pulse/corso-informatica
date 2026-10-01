# -*- coding: utf-8 -*-
# Compito "Da binario a decimale".
# Le griglie sono GESTITE COME IMMAGINI (PNG), identiche a quelle della dispensa (stessa
# griglia, stessi 1 in verde), così la grafica è IDENTICA ovunque. Sotto ogni griglia c'è
# lo SPAZIO per fare i conti a mano (carta e penna). 3 documenti monolingui IT/AR/ZH.
import os, subprocess, base64

POS=[128,64,32,16,8,4,2,1]
PART1=["00000011","00001010","00010001","00100000","01000001","01010101","01100100","11110000"]
PART2=["00000101","00011000","00100100","01000000","01111111","10000001","10101010","11000011"]
EX="01001110"  # esempio = 78, identico alla dispensa

OUT="/home/user/corso-godot/classe-1/bit-e-byte"
SP="/tmp/claude-0/-home-user-corso-godot/d65eff9d-e028-5dc2-8095-966645bd40b0/scratchpad"
RENDER="/home/user/corso-godot/strumenti/render-pdf/render_doc.js"
SHOT=f"{SP}/shot_grids.js"
IMGDIR=f"{SP}/grids_png"
os.makedirs(IMGDIR,exist_ok=True)
ENV=dict(os.environ); ENV["NODE_PATH"]=f"{SP}/node_modules"

# --- 1) foglio con tutte le griglie (stessa identica grafica della dispensa) ---
GRIDCSS="""*{box-sizing:border-box}body{margin:0;background:#fff}
.shot{display:inline-block;padding:3px;background:#fff}
table.pos{border-collapse:collapse;font-size:11pt;text-align:center;
 font-family:"DejaVu Sans",Arial,sans-serif}
table.pos td{border:1px solid #9cc0e4;padding:1.5mm 3mm;color:#1a2330}
table.pos .one{background:#eafaf0;font-weight:bold;color:#1e7a44}
"""
def grid_full(b):
    hdr="".join(f"<td>{v}</td>" for v in POS)
    row="".join(f"<td class='{'one' if c=='1' else ''}'>{c}</td>" for c in b)
    return f"<table class='pos'><tr>{hdr}</tr><tr>{row}</tr></table>"
def grid_empty():
    hdr="".join(f"<td>{v}</td>" for v in POS)
    row="".join("<td>&nbsp;</td>" for _ in POS)
    return f"<table class='pos'><tr>{hdr}</tr><tr>{row}</tr></table>"

sheet="<!DOCTYPE html><html><head><meta charset='utf-8'><style>"+GRIDCSS+"</style></head><body>"
sheet+=f"<div class='shot' id='ex'>{grid_full(EX)}</div>"
for i,b in enumerate(PART1): sheet+=f"<div class='shot' id='f{i}'>{grid_full(b)}</div>"
for i,b in enumerate(PART2): sheet+=f"<div class='shot' id='e{i}'>{grid_empty()}</div>"
sheet+="</body></html>"
shp=f"{SP}/grids_sheet.html"; open(shp,"w").write(sheet)
subprocess.run(["node",SHOT,shp,IMGDIR],env=ENV,check=True,capture_output=True)

def img(idn):
    data=base64.b64encode(open(f"{IMGDIR}/{idn}.png","rb").read()).decode()
    return f"<img class='grid' src='data:image/png;base64,{data}'>"

# --- 2) compito: immagine della griglia + spazio per i conti ---
CSS="""@page{size:A4}*{box-sizing:border-box}
body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:11pt;line-height:1.5;margin:0}
.cover{background:linear-gradient(160deg,#134a6e,#2c86b8);color:#fff;border-radius:12px;padding:12mm;text-align:center;margin-bottom:5mm}
.cover h1{font-size:19pt;margin:0}.cover .s{font-size:12pt;opacity:.93;margin-top:2mm}
h2{color:#12467a;font-size:14pt;margin:5mm 0 2mm;border-bottom:2px solid #2b7cc4;padding-bottom:1mm}
.attn{background:#fdecea;border:1px solid #e6b7b0;border-left:5px solid #c0392b;border-radius:6px;padding:3mm 4mm;margin:3mm 0}.attn b{color:#c0392b}
.key{background:#eef4fb;border:1px solid #9cc0e4;border-left:5px solid #2b7cc4;border-radius:6px;padding:3mm 4mm;margin:3mm 0}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px;font-size:12pt}
img.grid{height:15mm;display:block;margin:1.5mm 0}
.ex{border:1px solid #d5e0ec;border-radius:8px;padding:3mm 4mm;margin:3.5mm 0;background:#fafcff;page-break-inside:avoid}
.exn{font-weight:bold;color:#12467a}.byte{margin:1mm 0}
.conti{border:1px dashed #9cc0e4;border-radius:6px;background:#fff;height:22mm;margin-top:1.5mm;position:relative}
.conti .lab{position:absolute;top:1mm;left:2mm;font-size:9pt;color:#7a8aa0}
.res{margin-top:1.5mm;font-size:12pt}
.nome{margin:3mm 0}
.lang-ar{direction:rtl;text-align:right;font-family:"Amiri",serif;font-size:13pt}
.lang-ar img.grid{margin-left:auto;margin-right:0}
.lang-zh{font-family:"WenQuanYi Zen Hei",sans-serif;font-size:11.5pt}
"""

TXT={
"IT":("Compito — Da binario a decimale","Classe 1 · da consegnare",
  "<div class='attn'><b>Attenzione:</b> questo è il <b>compito da consegnare</b>. Per ogni griglia, somma i valori (riga sopra) dove sotto c'è un <b>1</b>; nello spazio bianco <b>fai i conti a mano</b> e scrivi il risultato, come nell'esempio.</div>",
  "<div class='nome'><b>Nome e Cognome:</b> ______________________________</div>",
  "Parte 1 — la griglia è già fatta: trova il numero","Parte 2 — la griglia è vuota: scrivi tu gli 0 e 1 nella griglia, poi fai i conti",
  "Fai i conti qui","risultato (numero)","numero binario"),
"AR":("واجب — من الثنائي إلى العشري","الصف الأول · يُسلَّم",
  "<div class='attn'><b>انتبه:</b> هذا هو <b>الواجب الذي يُسلَّم</b>. لكل جدول، اجمع القيم (الصف العلوي) حيث يوجد تحتها <b>1</b>؛ في المساحة البيضاء <b>احسب بخط اليد</b> واكتب الناتج، كما في المثال.</div>",
  "<div class='nome'><b>الاسم واللقب:</b> ______________________________</div>",
  "الجزء 1 — الجدول ممتلئ: جد العدد","الجزء 2 — الجدول فارغ: اكتب أنت الأصفار والواحدات في الجدول ثم احسب",
  "احسب هنا","الناتج (العدد)","العدد الثنائي"),
"ZH":("作业 — 从二进制到十进制","一年级 · 要交",
  "<div class='attn'><b>注意:</b>这是<b>要交的作业</b>。每个格子,把下面有 <b>1</b> 的位置上方的数值相加;在空白处<b>用手算</b>并写出结果,和例子一样。</div>",
  "<div class='nome'><b>姓名:</b> ______________________________</div>",
  "第一部分 — 格子已填好:找出数字","第二部分 — 格子是空的:自己在格子里写 0 和 1,然后计算",
  "在这里算","结果(数字)","二进制数"),
}

for code,(title,sub,attn,nome,h1,h2,clab,reslab,binlab) in TXT.items():
    lc={"IT":"","AR":"lang-ar","ZH":"lang-zh"}[code]
    def ex_full(n,idn):
        return (f"<div class='ex'><div class='exn'>{('Esercizio' if code=='IT' else ('تمرين' if code=='AR' else '练习'))} {n}</div>"
                f"{img(idn)}<div class='conti'><span class='lab'>{clab}</span></div>"
                f"<div class='res'>= __________________________  →  {reslab}: __________</div></div>")
    def ex_empty(n,idn,b):
        return (f"<div class='ex'><div class='exn'>{('Esercizio' if code=='IT' else ('تمرين' if code=='AR' else '练习'))} {n}</div>"
                f"<div class='byte'>{binlab}: <code>{b}</code></div>"
                f"{img(idn)}<div class='conti'><span class='lab'>{clab}</span></div>"
                f"<div class='res'>= __________________________  →  {reslab}: __________</div></div>")
    EX78=(f"<div class='key'><b>{'Esempio' if code=='IT' else ('مثال' if code=='AR' else '例子')}:</b>"
          f"{img('ex')}<div class='res'>= 128 + 64 + 32 + 16 = <b>78</b></div></div>")
    P1="".join(ex_full(i+1,f"f{i}") for i in range(8))
    P2="".join(ex_empty(i+9,f"e{i}",b) for i,b in enumerate(PART2))
    body=f"""<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><style>{CSS}</style></head>
<body class='{lc}'>
<div class='cover'><h1>{title}</h1><div class='s'>{sub}</div></div>
{attn}{nome}{EX78}
<h2>{h1}</h2>{P1}
<h2>{h2}</h2>{P2}
</body></html>"""
    hp=f"{OUT}/compito-bit-byte-{code}.html"; open(hp,"w").write(body)
    pdf=f"{OUT}/Compito-Bit-Byte-{code}-v3.0.pdf"
    subprocess.run(["node",RENDER,hp,pdf,title,"Classe 1 · 01/10/2026","Corso Informatica — Classe 1"],env=ENV,check=True,capture_output=True)
    print("OK",code)
print("Parte1:",len(PART1),"Parte2:",len(PART2))
