# -*- coding: utf-8 -*-
# v1.1 (02/10/2026) delle DUE cose facili, SOLO con il METODO DI NICOLA (quello della lavagna):
# DIVISIONI PER 2, resto a destra, si legge DAL BASSO VERSO L'ALTO, poi ZERI DAVANTI fino a 8.
# Sostituisce le v1.0 col "metodo delle monete" (ritirate: hanno confuso i ragazzi, regola §2.26).
#   - Dispensa facilissima: il 37 a fumetto, la tabella delle divisioni che cresce riga per riga.
#   - Scheda facile: esercizi a gradini (prima scrivi solo i resti, poi completi, poi da solo).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_decimale_binario import CSS, pdf, OUT, binario, byte

VER = "1.1"

def divs(n):
    r = []
    while n > 0: r.append((n, n % 2)); n //= 2
    return r

def tabella(rows, righe=None, lab=("÷ 2", "resto"), freccia=False, scala=0.30, evid=None):
    """Tabella delle divisioni come alla lavagna. rows: lista (numero o None, resto o None).
    righe: righe totali (le mancanti sono vuote, tratteggiate). evid: indice riga in giallo."""
    righe = righe or len(rows)
    rows = rows + [(None, None)] * (righe - len(rows))
    RH, TOP, W = 30, 34, 190
    H = TOP + righe * RH + 8
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*scala:.0f}mm' height='{H*scala:.0f}mm' style='display:block;flex-shrink:0'>",
         f"<text x='55' y='20' font-size='13' fill='#1e8a6a' text-anchor='middle' font-weight='bold'>{lab[0]}</text>",
         f"<text x='130' y='20' font-size='13' fill='#1e8a6a' text-anchor='middle' font-weight='bold'>{lab[1]}</text>",
         f"<line x1='95' y1='6' x2='95' y2='{H-4}' stroke='#d0392b' stroke-width='2.2'/>"]
    for i, (q, r) in enumerate(rows):
        y = TOP + i * RH + 21
        if evid == i:
            s.append(f"<rect x='10' y='{y-20}' width='160' height='27' fill='#ffe58a' rx='4'/>")
        s.append(f"<line x1='18' y1='{y+6}' x2='160' y2='{y+6}' stroke='#d5e0ec' stroke-dasharray='3 3'/>")
        if q is not None:
            s.append(f"<text x='55' y='{y}' font-size='19' fill='{'#d0392b' if i == 0 else '#1f5fbf'}' text-anchor='middle' font-weight='bold'>{q}</text>")
        if r is not None:
            s.append(f"<text x='130' y='{y}' font-size='19' fill='#1a2330' text-anchor='middle' font-weight='bold'>{r}</text>")
    if freccia:
        y0, y1 = TOP + righe * RH - 4, TOP + 8
        s.append(f"<line x1='172' y1='{y0}' x2='172' y2='{y1+6}' stroke='#1e8a6a' stroke-width='2.5'/>"
                 f"<polygon points='164,{y1+10} 180,{y1+10} 172,{y1-4}' fill='#1e8a6a'/>")
    s.append("</svg>")
    return "".join(s)

def otto(bits=None, rosso=0, scala=0.42):
    """Le 8 caselle del byte (come in fondo alla lavagna): zeri aggiunti in ROSSO."""
    CW, CH = 30, 30
    W = 8 * CW + 2
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {CH+2}' width='{W*scala:.0f}mm' height='{(CH+2)*scala:.0f}mm' style='display:block;flex-shrink:0'>"]
    for i in range(8):
        x = 1 + i * CW
        c = bits[i] if bits else ""
        col = "#d0392b" if (bits and i < rosso) else ("#1e7a44" if c == "1" else "#1a2330")
        s.append(f"<rect x='{x}' y='1' width='{CW}' height='{CH}' fill='#fff' stroke='#5a6b80' stroke-width='1.5'/>"
                 f"<text x='{x+CW/2}' y='22' font-size='18' text-anchor='middle' fill='{col}' font-weight='bold'>{c}</text>")
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------- testi
T = {
"IT": dict(lab=("÷ 2", "resto"),
 ft="Il binario facile", fsub="Classe 1 · da decimale a binario · il metodo della lavagna · italiano",
 regola="<b>Il resto è facile:</b> numero <b>PARI → resto 0</b> · numero <b>DISPARI → resto 1</b>.",
 h37="Il 37, passo per passo (come alla lavagna)",
 s=["Scrivo <b>37</b>. È dispari → resto <b>1</b>. Poi 37 : 2 = <b>18</b> (va sotto).",
    "<b>18</b> è pari → resto <b>0</b>. Poi 18 : 2 = <b>9</b>.",
    "<b>9</b> è dispari → resto <b>1</b>. Poi 9 : 2 = <b>4</b>.",
    "<b>4</b> pari → <b>0</b>, poi <b>2</b>. <b>2</b> pari → <b>0</b>, poi <b>1</b>.",
    "<b>1</b> → resto <b>1</b>. Finito!",
    "Leggo i resti <b>DAL BASSO VERSO L'ALTO</b>: <b>100101</b>."],
 hbyte="Il byte: sempre 8 caselle",
 byt="100101 ha <b>6</b> cifre. Il byte ne ha <b>8</b>. Mancano 2 → metto <b>2 zeri DAVANTI</b> (in rosso):",
 byt2="Gli zeri davanti non cambiano il numero (come 007 = 7).",
 h3="Ricorda: 3 cose", r=["Dividi per 2: resto a destra (pari 0, dispari 1).", "Leggi i resti dal BASSO verso l'ALTO.", "Zeri DAVANTI fino a 8 caselle."],
 bravo="Se ci riesci: BRAVO! Hai capito il binario.",
 st="Scheda facile — da decimale a binario", ssub="Classe 1 · esercizi a gradini · sul foglio · italiano",
 l1="Livello 1 — scrivi SOLO i resti", l1t="I numeri a sinistra ci sono già. Tu scrivi a destra il resto: pari → 0, dispari → 1. Poi leggi dal basso.",
 l2="Livello 2 — completa la tabella", l2t="La prima riga c'è già. Continua tu a dividere per 2.",
 l3="Livello 3 — da solo", l3t="Fai tutta la tabella da solo.",
 l4="Livello 4 — completa il byte", l4t="Hai il numero binario. Mettilo nelle 8 caselle: <b>zeri davanti</b>, fino a 8.",
 bin="binario (dal basso):", byte="byte (8 caselle):", fatto="FATTO! Ora sai trasformare un numero in byte."),
"AR": dict(lab=("÷ 2", "الباقي"),
 ft="الثنائي السهل", fsub="الصف الأول · من العشري إلى الثنائي · طريقة اللوحة · العربية",
 regola="<b>الباقي سهل:</b> عدد <b>زوجي ← الباقي 0</b> · عدد <b>فردي ← الباقي 1</b>.",
 h37="العدد 37 خطوة بخطوة (كما على اللوحة)",
 s=["أكتب <b>37</b>. فردي ← الباقي <b>1</b>. ثم 37 : 2 = <b>18</b> (يُكتب تحته).",
    "<b>18</b> زوجي ← الباقي <b>0</b>. ثم 18 : 2 = <b>9</b>.",
    "<b>9</b> فردي ← الباقي <b>1</b>. ثم 9 : 2 = <b>4</b>.",
    "<b>4</b> زوجي ← <b>0</b>، ثم <b>2</b>. <b>2</b> زوجي ← <b>0</b>، ثم <b>1</b>.",
    "<b>1</b> ← الباقي <b>1</b>. انتهينا!",
    "أقرأ البواقي <b>من الأسفل إلى الأعلى</b>: <b>100101</b>."],
 hbyte="البايت: دائمًا 8 خانات",
 byt="العدد 100101 فيه <b>6</b> أرقام. البايت فيه <b>8</b>. ينقص 2 ← أضع <b>صفرين في البداية</b> (بالأحمر):",
 byt2="الأصفار في البداية لا تغيّر العدد (مثل 007 = 7).",
 h3="تذكّر: 3 أشياء", r=["اقسم على 2: الباقي على اليمين (زوجي 0، فردي 1).", "اقرأ البواقي من الأسفل إلى الأعلى.", "أصفار في البداية حتى 8 خانات."],
 bravo="إذا نجحت: أحسنت! لقد فهمت الثنائي.",
 st="ورقة سهلة — من العشري إلى الثنائي", ssub="الصف الأول · تمارين متدرجة · على الورقة · العربية",
 l1="المستوى 1 — اكتب البواقي فقط", l1t="الأعداد على اليسار موجودة. اكتب أنت الباقي على اليمين: زوجي ← 0، فردي ← 1. ثم اقرأ من الأسفل.",
 l2="المستوى 2 — أكمل الجدول", l2t="السطر الأول موجود. أكمل القسمة على 2.",
 l3="المستوى 3 — وحدك", l3t="املأ الجدول كله وحدك.",
 l4="المستوى 4 — أكمل البايت", l4t="لديك العدد الثنائي. ضعه في الخانات الثماني: <b>أصفار في البداية</b> حتى 8.",
 bin="الثنائي (من الأسفل):", byte="البايت (8 خانات):", fatto="أحسنت! الآن تعرف كيف تحوّل العدد إلى بايت."),
"ZH": dict(lab=("÷ 2", "余数"),
 ft="简单的二进制", fsub="一年级 · 从十进制到二进制 · 白板上的方法 · 中文",
 regola="<b>余数很简单:</b><b>偶数 → 余数 0</b> · <b>奇数 → 余数 1</b>。",
 h37="37,一步一步(和白板一样)",
 s=["写 <b>37</b>。奇数 → 余数 <b>1</b>。然后 37 : 2 = <b>18</b>(写在下面)。",
    "<b>18</b> 是偶数 → 余数 <b>0</b>。然后 18 : 2 = <b>9</b>。",
    "<b>9</b> 是奇数 → 余数 <b>1</b>。然后 9 : 2 = <b>4</b>。",
    "<b>4</b> 偶数 → <b>0</b>,然后 <b>2</b>。<b>2</b> 偶数 → <b>0</b>,然后 <b>1</b>。",
    "<b>1</b> → 余数 <b>1</b>。完成!",
    "<b>从下往上</b>读余数:<b>100101</b>。"],
 hbyte="字节:永远是 8 个格子",
 byt="100101 有 <b>6</b> 位。字节有 <b>8</b> 位。少 2 位 → 在<b>前面补 2 个 0</b>(红色):",
 byt2="前面的 0 不改变数字(就像 007 = 7)。",
 h3="记住:3 件事", r=["除以 2:余数写右边(偶数 0,奇数 1)。", "从下往上读余数。", "前面补 0,补到 8 个格子。"],
 bravo="做到了:太棒了!你懂二进制了。",
 st="简单练习 — 从十进制到二进制", ssub="一年级 · 分级练习 · 在纸上做 · 中文",
 l1="第 1 级 — 只写余数", l1t="左边的数字已经写好了。你在右边写余数:偶数 → 0,奇数 → 1。然后从下往上读。",
 l2="第 2 级 — 把表格写完", l2t="第一行已经写好了。你继续除以 2。",
 l3="第 3 级 — 自己做", l3t="整个表格自己做。",
 l4="第 4 级 — 把字节补完整", l4t="你有二进制数。把它放进 8 个格子:<b>前面补 0</b>,补到 8 个。",
 bin="二进制(从下往上):", byte="字节(8 个格子):", fatto="做到了!现在你会把数字变成字节了。"),
}

XCSS = """
body{font-size:13pt}
.regola{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:3mm 4mm;font-size:14pt;text-align:center;margin:3mm 0}
.passo{display:flex;align-items:center;gap:6mm;border:1px solid #d5e0ec;border-radius:10px;padding:2mm 4mm;margin:2mm 0;background:#fafcff;page-break-inside:avoid}
.passo .n{min-width:10mm;height:10mm;border-radius:50%;background:#2b7cc4;color:#fff;font-weight:bold;display:flex;align-items:center;justify-content:center}
.passo .tx{flex:1;font-size:13pt}
.lang-ar .passo{flex-direction:row-reverse}
.bytebox{display:flex;align-items:center;gap:6mm;margin:3mm 0;direction:ltr}
.fine{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:3mm;text-align:center;font-size:15pt;color:#1e7a44;margin:4mm 0;font-weight:bold}
.ric{display:flex;gap:4mm;margin:2mm 0}.ric div{flex:1;background:#eef4fb;border-radius:10px;padding:3mm;text-align:center}
.ese{display:flex;gap:6mm;align-items:flex-start;border:1px solid #d5e0ec;border-radius:10px;padding:3mm 4mm;margin:3mm 0;background:#fafcff;page-break-inside:avoid;direction:ltr}
.ese .t{font-weight:bold;color:#12467a;font-size:14pt;margin-bottom:2mm}
.ese .dx p{margin:2mm 0}
.linea{display:inline-block;border-bottom:1.5px solid #5a6b80;min-width:40mm;height:6mm}
"""

def facilissima(L, t):
    r = divs(37)
    passi_rows = [r[:1], r[:2], r[:3], r[:5], r[:6], r[:6]]
    evid = [0, 1, 2, 4, 5, None]
    passi = "".join(
        f"<div class='passo'><div class='n'>{i+1}</div>{tabella(passi_rows[i], 6, t['lab'], freccia=(i == 5), scala=0.26, evid=evid[i])}"
        f"<div class='tx testo'>{t['s'][i]}</div></div>" for i in range(6))
    ric = "".join(f"<div>{i+1}. {x}</div>" for i, x in enumerate(t["r"]))
    prova = "".join(f"<div class='ese'>{tabella([(n, None)], len(divs(n)), t['lab'], scala=0.26)}<div class='dx'>"
                    f"<div class='t'>{n}</div><p class='lbl'>{t['bin']} <span class='linea'></span></p>"
                    f"<p class='lbl'>{t['byte']}</p>{otto()}</div></div>" for n in (6, 9, 12))
    return (f"<div class='cover'><h1>{t['ft']}</h1><div class='s'>{t['fsub']}</div></div>"
            f"<div class='regola testo'>{t['regola']}</div>"
            f"<h2 class='testo'>{t['h37']}</h2>{passi}"
            f"<h2 class='testo'>{t['hbyte']}</h2><p class='testo'>{t['byt']}</p>"
            f"<div class='bytebox'>{otto('00100101', rosso=2)}</div><p class='testo'>{t['byt2']}</p>"
            f"<div style='page-break-before:always'></div>"
            f"<h2 class='testo'>{t['h3']}</h2><div class='ric testo'>{ric}</div>"
            f"<div class='testo'><h2>{'Prova tu' if L=='IT' else ('جرّب أنت' if L=='AR' else '你来试试')}</h2></div>{prova}"
            f"<div class='fine testo'>{t['bravo']}</div>")

def facile(L, t):
    k = 0; out = []
    def ese(n, rows, righe):
        nonlocal k; k += 1
        return (f"<div class='ese'>{tabella(rows, righe, t['lab'], scala=0.26)}<div class='dx'>"
                f"<div class='t'>{k}. {n}</div><p class='lbl'>{t['bin']} <span class='linea'></span></p>"
                f"<p class='lbl'>{t['byte']}</p>{otto()}</div></div>")
    out.append(f"<div class='cover'><h1>{t['st']}</h1><div class='s'>{t['ssub']}</div></div>")
    out.append(f"<div class='regola testo'>{t['regola']}</div>")
    out.append(f"<div class='testo'><h2>{t['l1']}</h2><p>{t['l1t']}</p></div>")
    for n in (2, 3, 5, 6):
        out.append(ese(n, [(q, None) for q, _ in divs(n)], len(divs(n))))
    out.append(f"<div class='testo'><h2>{t['l2']}</h2><p>{t['l2t']}</p></div>")
    for n in (9, 10, 12, 13):
        out.append(ese(n, [(n, None)], len(divs(n))))
    out.append(f"<div class='testo'><h2>{t['l3']}</h2><p>{t['l3t']}</p></div>")
    for n in (17, 20, 25):
        out.append(ese(n, [(n, None)], len(divs(n))))
    out.append(f"<div class='testo'><h2>{t['l4']}</h2><p>{t['l4t']}</p></div>")
    out.append(f"<div class='bytebox'><code>100101</code> → {otto('00100101', rosso=2)}</div>")
    for b in ("101", "11", "1001", "110", "10010"):
        k += 1
        out.append(f"<div class='ese'><div class='dx'><div class='t'>{k}. <code>{b}</code></div>{otto()}</div></div>")
    out.append(f"<div class='fine testo'>{t['fatto']}</div>")
    return "".join(out)

def main():
    for L, t in T.items():
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        for fn, html_name, pdf_name in ((facilissima, f"dispensa-facilissima-{L}", f"Dispensa-Facilissima-Binario-{L}-v{VER}.pdf"),
                                        (facile, f"scheda-facile-{L}", f"Scheda-Facile-Binario-{L}-v{VER}.pdf")):
            html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head><body class='{cls}'>{fn(L, t)}</body></html>"
            hp = f"{OUT}/{html_name}.html"; open(hp, "w").write(html)
            pdf(hp, f"{OUT}/{pdf_name}")
        print("OK", L)

if __name__ == "__main__":
    main()
