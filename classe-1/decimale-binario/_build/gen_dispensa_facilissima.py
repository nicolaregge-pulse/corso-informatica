# -*- coding: utf-8 -*-
# DISPENSA FACILISSIMA (02/10/2026, chiesta in classe): 2 pagine, caratteri GRANDI, pochissime
# parole, il 37 spiegato "a fumetto": la griglia del byte si riempie passo dopo passo.
# Stessa griglia (stessi colori) di dispensa, compito e scheda facile (§2.19).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_decimale_binario import CSS, POS, pdf, OUT, VER

def griglia(bits, scala=0.42, evid=None):
    """bits: stringa di 8 caratteri tra '0','1','_' (vuota). evid = indici da evidenziare (giallo)."""
    CW, CH, W = 34, 26, 8 * 34 + 2
    H = CH * 2 + 2
    evid = evid or []
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*scala:.0f}mm' height='{H*scala:.0f}mm' style='display:block'>"]
    for i, v in enumerate(POS):
        x = 1 + i * CW
        hf = "#ffe58a" if i in evid else "#f3f7fb"
        s.append(f"<rect x='{x}' y='1' width='{CW}' height='{CH}' fill='{hf}' stroke='#9cc0e4'/>"
                 f"<text x='{x+CW/2}' y='18' font-size='12' text-anchor='middle' fill='#12467a' font-weight='bold'>{v}</text>")
        c = bits[i]
        fill, col, txt = "#ffffff", "#1a2330", ""
        if c == "1": fill, col, txt = "#eafaf0", "#1e7a44", "1"
        elif c == "0": col, txt = "#d0392b", "0"
        s.append(f"<rect x='{x}' y='{CH+1}' width='{CW}' height='{CH}' fill='{fill}' stroke='#9cc0e4'/>"
                 f"<text x='{x+CW/2}' y='{CH+19}' font-size='16' text-anchor='middle' fill='{col}' font-weight='bold'>{txt}</text>")
    s.append("</svg>")
    return "".join(s)

# il 37 a fumetto: (bits dopo il passo, caselle evidenziate, chiave del testo)
PASSI = [("00______", [0, 1], "p1"), ("001_____", [2], "p2"), ("00100___", [3, 4], "p3"),
         ("001001__", [5], "p4"), ("00100101", [6, 7], "p5")]

T = {
"IT": dict(
 titolo="Il binario facile", sub="Classe 1 · da decimale a binario · italiano",
 a="Il byte ha <b>8 caselle</b>. Ogni casella è una <b>moneta</b>:",
 b="In ogni casella scrivi: <b>1</b> = uso la moneta · <b>0</b> = non la uso.<br><b>Tutte le 8 caselle hanno un numero.</b> Mai vuote.",
 h_es="Esempio: 37 (passo per passo)",
 p1="128 ci sta in 37? <b>NO → 0</b>. 64? <b>NO → 0</b>.",
 p2="32 ci sta in 37? <b>SÌ → 1</b>. Restano 37 − 32 = <b>5</b>.",
 p3="16 ci sta in 5? <b>NO → 0</b>. 8? <b>NO → 0</b>.",
 p4="4 ci sta in 5? <b>SÌ → 1</b>. Resta 5 − 4 = <b>1</b>.",
 p5="2 ci sta in 1? <b>NO → 0</b>. 1? <b>SÌ → 1</b>. Resta <b>0</b>. Finito!",
 fine="37 = <b>00100101</b> · prova: 32 + 4 + 1 = 37",
 h_ric="Ricorda: 3 domande", r1="La moneta <b>ci sta</b>?", r2="Sì → <b>1</b> e la tolgo. No → <b>0</b>.", r3="Vado alla moneta <b>dopo</b>, fino alla fine.",
 h_prova="Prova tu (sul foglio)", pr=["6 = 4 + 2", "9 = 8 + 1", "12 = 8 + 4"],
 bravo="Se ci riesci: BRAVO! Hai capito il binario."),
"AR": dict(
 titolo="الثنائي السهل", sub="الصف الأول · من العشري إلى الثنائي · العربية",
 a="للبايت <b>8 خانات</b>. كل خانة هي <b>عملة</b>:",
 b="في كل خانة اكتب: <b>1</b> = أستعمل العملة · <b>0</b> = لا أستعملها.<br><b>كل الخانات الثماني فيها رقم.</b> لا تبقى فارغة أبدًا.",
 h_es="مثال: 37 (خطوة بخطوة)",
 p1="هل 128 تدخل في 37؟ <b>لا ← 0</b>. 64؟ <b>لا ← 0</b>.",
 p2="هل 32 تدخل في 37؟ <b>نعم ← 1</b>. الباقي 37 − 32 = <b>5</b>.",
 p3="هل 16 تدخل في 5؟ <b>لا ← 0</b>. 8؟ <b>لا ← 0</b>.",
 p4="هل 4 تدخل في 5؟ <b>نعم ← 1</b>. الباقي 5 − 4 = <b>1</b>.",
 p5="هل 2 تدخل في 1؟ <b>لا ← 0</b>. 1؟ <b>نعم ← 1</b>. الباقي <b>0</b>. انتهينا!",
 fine="37 = <b>00100101</b> · التحقق: 32 + 4 + 1 = 37",
 h_ric="تذكّر: 3 أسئلة", r1="هل العملة <b>تدخل</b>؟", r2="نعم ← <b>1</b> وأطرحها. لا ← <b>0</b>.", r3="أنتقل إلى العملة <b>التالية</b> حتى النهاية.",
 h_prova="جرّب أنت (على الورقة)", pr=["6 = 4 + 2", "9 = 8 + 1", "12 = 8 + 4"],
 bravo="إذا نجحت: أحسنت! لقد فهمت الثنائي."),
"ZH": dict(
 titolo="简单的二进制", sub="一年级 · 从十进制到二进制 · 中文",
 a="一个字节有 <b>8 个格子</b>。每个格子是一个<b>硬币</b>:",
 b="每个格子写:<b>1</b> = 用这个硬币 · <b>0</b> = 不用。<br><b>8 个格子都要写数字。</b>不能空着。",
 h_es="例子:37(一步一步)",
 p1="128 放得进 37 吗?<b>不能 → 0</b>。64?<b>不能 → 0</b>。",
 p2="32 放得进 37 吗?<b>能 → 1</b>。剩下 37 − 32 = <b>5</b>。",
 p3="16 放得进 5 吗?<b>不能 → 0</b>。8?<b>不能 → 0</b>。",
 p4="4 放得进 5 吗?<b>能 → 1</b>。剩下 5 − 4 = <b>1</b>。",
 p5="2 放得进 1 吗?<b>不能 → 0</b>。1?<b>能 → 1</b>。剩下 <b>0</b>。完成!",
 fine="37 = <b>00100101</b> · 检查:32 + 4 + 1 = 37",
 h_ric="记住:3 个问题", r1="硬币<b>放得进</b>吗?", r2="能 → <b>1</b>,减掉它。不能 → <b>0</b>。", r3="去<b>下一个</b>硬币,直到最后。",
 h_prova="你来试试(在纸上)", pr=["6 = 4 + 2", "9 = 8 + 1", "12 = 8 + 4"],
 bravo="做到了:太棒了!你懂二进制了。"),
}

XCSS = """
body{font-size:14pt}
.big{font-size:15pt;margin:3mm 0}
.monete{display:flex;gap:3mm;justify-content:center;margin:3mm 0 4mm;direction:ltr}
.moneta{width:17mm;height:17mm;border-radius:50%;background:#f5c542;border:2px solid #c99a12;display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:14pt;color:#5a4200}
.passo{display:flex;align-items:center;gap:5mm;border:1px solid #d5e0ec;border-radius:10px;padding:2.5mm 4mm;margin:2.5mm 0;background:#fafcff;page-break-inside:avoid}
.passo .n{min-width:10mm;height:10mm;border-radius:50%;background:#2b7cc4;color:#fff;font-weight:bold;display:flex;align-items:center;justify-content:center;font-size:13pt}
.passo .g{direction:ltr}
.passo .tx{flex:1;font-size:13pt}
.fine{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:3mm;text-align:center;font-size:16pt;color:#1e7a44;margin:3mm 0}
.ric{display:flex;gap:4mm;margin:2mm 0}
.ric div{flex:1;background:#eef4fb;border-radius:10px;padding:3mm;text-align:center;font-size:13pt}
.prova{display:flex;flex-direction:column;gap:3mm;direction:ltr}
.prova .pv{display:flex;align-items:center;gap:6mm;font-size:15pt;font-weight:bold;color:#12467a}
.lang-ar .passo{flex-direction:row-reverse}
"""

def main():
    for L, t in T.items():
        monete = "".join(f"<div class='moneta'>{v}</div>" for v in POS)
        passi = "".join(f"<div class='passo'><div class='n'>{i+1}</div><div class='g'>{griglia(b, 0.36, e)}</div>"
                        f"<div class='tx testo'>{t[k]}</div></div>" for i, (b, e, k) in enumerate(PASSI))
        prova = "".join(f"<div class='pv'><span style='min-width:40mm'>{p}</span>{griglia('________', 0.36)}</div>" for p in t["pr"])
        body = (f"<div class='cover'><h1>{t['titolo']}</h1><div class='s'>{t['sub']}</div></div>"
                f"<p class='big testo'>{t['a']}</p><div class='monete'>{monete}</div>"
                f"<div class='attn big testo'>{t['b']}</div>"
                f"<h2 class='testo'>{t['h_es']}</h2>{passi}"
                f"<div class='fine testo'>{t['fine']}</div>"
                f"<div style='page-break-before:always'></div>"
                f"<h2 class='testo'>{t['h_ric']}</h2>"
                f"<div class='ric testo'><div>1. {t['r1']}</div><div>2. {t['r2']}</div><div>3. {t['r3']}</div></div>"
                f"<h2 class='testo'>{t['h_prova']}</h2><div class='prova'>{prova}</div>"
                f"<div class='fine testo'>{t['bravo']}</div>")
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head><body class='{cls}'>{body}</body></html>"
        hp = f"{OUT}/dispensa-facilissima-{L}.html"; open(hp, "w").write(html)
        pdf(hp, f"{OUT}/Dispensa-Facilissima-Binario-{L}-v{VER}.pdf")
        print("OK", L)

if __name__ == "__main__":
    main()
