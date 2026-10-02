# -*- coding: utf-8 -*-
# SCHEDA "La divisione per 2 con il resto" (02/10/2026): i ragazzi non sanno fare la divisione
# intera col resto, che è il pezzo che serve al metodo della lavagna. Solo DIVISIONE, niente altro:
# 1) dividere = fare 2 parti uguali (caramelle), 2) la regola pari/dispari per il resto,
# 3) tabella delle metà da consultare, 4) esercizi a gradini che finiscono con la catena del 37.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_decimale_binario import CSS, pdf, OUT

VER = "1.2"  # v1.2: Livello 3 riscritto riga per riga (niente tabella spezzata), primo passo già fatto

def pallini(n, pieni=True, scala=0.32):
    """n caramelle in coppie (colonne da 2); quella che avanza è ROSSA. pieni=False: cerchi vuoti."""
    coppie, resto = divmod(n, 2)
    R, G = 9, 24
    cols = coppie + resto
    W = max(1, cols) * G + 10; H = 2 * G + 10
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*scala:.0f}mm' height='{H*scala:.0f}mm' style='display:block;flex-shrink:0'>"]
    for c in range(coppie):
        x = 5 + c * G + G / 2
        if pieni:
            s.append(f"<rect x='{x-G/2+2}' y='3' width='{G-4}' height='{2*G}' rx='8' fill='none' stroke='#9cc0e4' stroke-dasharray='3 2'/>")
        for r in range(2):
            fill = "#2b7cc4" if pieni else "#fff"
            s.append(f"<circle cx='{x}' cy='{5 + r*G + G/2}' r='{R}' fill='{fill}' stroke='#2b7cc4' stroke-width='2'/>")
    if resto:
        x = 5 + coppie * G + G / 2
        s.append(f"<circle cx='{x}' cy='{5 + G/2}' r='{R}' fill='{'#d0392b' if pieni else '#fff'}' stroke='#d0392b' stroke-width='2'/>")
    s.append("</svg>")
    return "".join(s)

def tabella_meta(da, a):
    righe = "".join(f"<tr><td><b>{n}</b></td><td>{n//2}</td><td class='{'r1' if n%2 else ''}'>{n%2}</td></tr>" for n in range(da, a + 1))
    return righe

T = {
"IT": dict(
 t="La divisione per 2 con il resto", sub="Classe 1 · scheda di aiuto · sul foglio · italiano",
 h1="1. Dividere per 2 = fare 2 parti uguali",
 p1="Hai delle caramelle e le dividi tra <b>2 amici</b>: ognuno ne prende lo stesso numero. Quella che <b>avanza</b> (in rosso) è il <b>RESTO</b>.",
 e6="6 caramelle → 3 a testa, non avanza niente.", e6r="6 : 2 = 3 resto 0",
 e7="7 caramelle → 3 a testa, ne avanza 1.", e7r="7 : 2 = 3 resto 1",
 h2="2. La regola (una riga sola)",
 regola="<b>Numero PARI</b> (finisce con 0, 2, 4, 6, 8) → fai la <b>metà</b>, resto <b>0</b>.<br><b>Numero DISPARI</b> (finisce con 1, 3, 5, 7, 9) → <b>togli 1</b> (è il resto), poi fai la <b>metà</b>.",
 es37="Esempio: <b>37</b> è dispari → tolgo 1 → 36 → metà = <b>18</b>. Quindi <b>37 : 2 = 18 resto 1</b>.",
 h3="3. La tabella delle metà (guardala quando serve)", col=("numero", "risultato (: 2)", "resto"),
 h4="4. Esercizi", l1="Livello 1 — dividi le caramelle in coppie (colora quella che avanza)",
 l2="Livello 2 — pari o dispari? poi dividi", l3="Livello 3 — divisioni a catena",
 l3t="La prima riga è già fatta: 37 : 2 = 18 resto 1. Il <b>18</b> passa nella riga sotto e lo dividi. Fai così ogni volta: il risultato va nella riga sotto. Ti fermi quando il risultato è <b>0</b>.",
 resto="resto", fatto="FATTO! Ora sai fare la divisione per 2 con il resto."),
"AR": dict(
 t="القسمة على 2 مع الباقي", sub="الصف الأول · ورقة مساعدة · على الورقة · العربية",
 h1="1. القسمة على 2 = جزءان متساويان",
 p1="لديك حلوى وتقسمها بين <b>صديقين</b>: كل واحد يأخذ العدد نفسه. التي <b>تبقى</b> (بالأحمر) هي <b>الباقي</b>.",
 e6="6 حلوى ← 3 لكل واحد، لا يبقى شيء.", e6r="6 : 2 = 3 والباقي 0",
 e7="7 حلوى ← 3 لكل واحد، تبقى 1.", e7r="7 : 2 = 3 والباقي 1",
 h2="2. القاعدة (سطر واحد)",
 regola="<b>عدد زوجي</b> (ينتهي بـ 0، 2، 4، 6، 8) ← خذ <b>النصف</b>، الباقي <b>0</b>.<br><b>عدد فردي</b> (ينتهي بـ 1، 3، 5، 7، 9) ← <b>اطرح 1</b> (هو الباقي)، ثم خذ <b>النصف</b>.",
 es37="مثال: <b>37</b> فردي ← أطرح 1 ← 36 ← النصف = <b>18</b>. إذن <b>37 : 2 = 18 والباقي 1</b>.",
 h3="3. جدول الأنصاف (انظر إليه عند الحاجة)", col=("العدد", "الناتج (: 2)", "الباقي"),
 h4="4. تمارين", l1="المستوى 1 — قسّم الحلوى أزواجًا (لوّن التي تبقى)",
 l2="المستوى 2 — زوجي أم فردي؟ ثم اقسم", l3="المستوى 3 — قسمة متتالية",
 l3t="السطر الأول محلول: 37 : 2 = 18 والباقي 1. العدد <b>18</b> ينتقل إلى السطر التالي وتقسمه. افعل هكذا كل مرة: الناتج يذهب إلى السطر التالي. تتوقف عندما يصبح الناتج <b>0</b>.",
 resto="الباقي", fatto="أحسنت! الآن تعرف القسمة على 2 مع الباقي."),
"ZH": dict(
 t="除以 2 和余数", sub="一年级 · 帮助练习 · 在纸上做 · 中文",
 h1="1. 除以 2 = 分成 2 份一样多",
 p1="你有一些糖,分给 <b>2 个朋友</b>:每人拿一样多。<b>剩下</b>的那颗(红色)就是<b>余数</b>。",
 e6="6 颗糖 → 每人 3 颗,没有剩下。", e6r="6 : 2 = 3 余 0",
 e7="7 颗糖 → 每人 3 颗,剩下 1 颗。", e7r="7 : 2 = 3 余 1",
 h2="2. 规则(只有一行)",
 regola="<b>偶数</b>(个位是 0、2、4、6、8)→ 取<b>一半</b>,余数 <b>0</b>。<br><b>奇数</b>(个位是 1、3、5、7、9)→ <b>先减 1</b>(这就是余数),再取<b>一半</b>。",
 es37="例子:<b>37</b> 是奇数 → 减 1 → 36 → 一半 = <b>18</b>。所以 <b>37 : 2 = 18 余 1</b>。",
 h3="3. 一半表(需要时看)", col=("数字", "结果(: 2)", "余数"),
 h4="4. 练习", l1="第 1 级 — 把糖两个两个分(剩下的涂颜色)",
 l2="第 2 级 — 偶数还是奇数?然后除", l3="第 3 级 — 连续除法",
 l3t="第一行已经做好:37 : 2 = 18 余 1。<b>18</b> 写到下一行,再除以 2。每次都这样:结果写到下一行。结果是 <b>0</b> 时就停。",
 resto="余", fatto="做到了!现在你会除以 2 和余数了。"),
}

XCSS = """
.nota2{color:#7a8aa0;font-size:11pt;margin-left:auto}
body{font-size:13pt}
.duo{display:flex;gap:8mm;align-items:center;margin:2mm 0;page-break-inside:avoid}
.duo .tx p{margin:1mm 0}
.big{font-size:15pt;font-weight:bold;color:#12467a;direction:ltr;unicode-bidi:embed}
.regola{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:3mm 5mm;font-size:13.5pt;margin:3mm 0;line-height:1.7}
.tabs{display:flex;gap:3mm;direction:ltr;justify-content:center;page-break-inside:avoid}
table.meta{border-collapse:collapse;font-size:10pt}
table.meta td,table.meta th{border:1px solid #9cc0e4;padding:0.5mm 1.8mm;text-align:center}
table.meta th{background:#eef4fb;color:#12467a;font-size:8.5pt;white-space:nowrap}
table.meta .r1{background:#fdecea;color:#d0392b;font-weight:bold}
.ese{display:flex;gap:6mm;align-items:center;border:1px solid #d5e0ec;border-radius:10px;padding:3mm 4mm;margin:2.5mm 0;background:#fafcff;page-break-inside:avoid;direction:ltr}
.ese .k{font-weight:bold;color:#12467a;min-width:8mm}
.cat{border-collapse:collapse;margin:3mm 0;direction:ltr;font-size:15pt}
.cat td{border:1px solid #9cc0e4;padding:2mm 4mm;min-width:22mm;height:11mm;text-align:center}
.cat .q{color:#d0392b;font-weight:bold}
.fine{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:3mm;text-align:center;font-size:14pt;color:#1e7a44;margin:4mm 0;font-weight:bold}
"""


SOPRA = {"IT": "← il risultato della riga sopra", "AR": "← ناتج السطر السابق", "ZH": "← 上一行的结果"}
ESEMPIO = {"IT": "già fatto", "AR": "محلول", "ZH": "已做好"}

def catena(L, t):
    r = f"<bdi>{t['resto']}</bdi>"
    righe = (f"<div class='ese' style='background:#eafaf0'><span class='k'>1.</span><span class='big'>37 : 2 = 18 {r} 1</span>"
             f"<span class='nota2'>({ESEMPIO[L]})</span></div>"
             f"<div class='ese'><span class='k'>2.</span><span class='big'><span style='color:#d0392b'>18</span> : 2 = ____ {r} ____</span>"
             f"<span class='nota2'>{SOPRA[L]}</span></div>")
    for k in range(3, 7):
        righe += (f"<div class='ese'><span class='k'>{k}.</span><span class='big'>____ : 2 = ____ {r} ____</span>"
                  f"<span class='nota2'>{SOPRA[L]}</span></div>")
    return f"<div style='page-break-inside:avoid'>{righe}</div>"

def scheda(L, t):
    h = "".join(f"<th>{c}</th>" for c in t["col"])
    tabs = "".join(f"<table class='meta'><tr>{h}</tr>{tabella_meta(a, b)}</tr></table>" for a, b in ((1, 10), (11, 20), (21, 30), (31, 40)))
    k = 0; l1 = l2 = ""
    for n in (4, 5, 8, 9):
        k += 1
        l1 += f"<div class='ese'><span class='k'>{k}.</span>{pallini(n, pieni=False)}<span class='big'>{n} : 2 = ____ <bdi>{t['resto']}</bdi> ____</span></div>"
    for n in (10, 11, 14, 15, 20, 21):
        k += 1
        l2 += f"<div class='ese'><span class='k'>{k}.</span><span class='big'>{n} : 2 = ____ <bdi>{t['resto']}</bdi> ____</span></div>"
    cat = catena(L, t)
    return (f"<div class='cover'><h1>{t['t']}</h1><div class='s'>{t['sub']}</div></div>"
            f"<h2 class='testo'>{t['h1']}</h2><p class='testo'>{t['p1']}</p>"
            f"<div class='duo'>{pallini(6)}<div class='tx testo'><p>{t['e6']}</p><p class='big'>{t['e6r']}</p></div></div>"
            f"<div class='duo'>{pallini(7)}<div class='tx testo'><p>{t['e7']}</p><p class='big'>{t['e7r']}</p></div></div>"
            f"<h2 class='testo'>{t['h2']}</h2><div class='regola testo'>{t['regola']}</div><p class='testo'>{t['es37']}</p>"
            f"<h2 class='testo'>{t['h3']}</h2><div class='tabs'>{tabs}</div>"
            f"<div style='page-break-before:always'></div><h2 class='testo'>{t['h4']}</h2>"
            f"<h2 class='testo' style='font-size:12.5pt'>{t['l1']}</h2>{l1}"
            f"<h2 class='testo' style='font-size:12.5pt'>{t['l2']}</h2>{l2}"
            f"<div style='page-break-inside:avoid'><h2 class='testo' style='font-size:12.5pt'>{t['l3']}</h2><p class='testo'>{t['l3t']}</p>{cat}</div>"
            f"<div class='fine testo'>{t['fatto']}</div>")

def main():
    for L, t in T.items():
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head><body class='{cls}'>{scheda(L, t)}</body></html>"
        hp = f"{OUT}/divisione-per-2-{L}.html"; open(hp, "w").write(html)
        pdf(hp, f"{OUT}/Divisione-per-2-{L}-v{VER}.pdf")
        print("OK", L)

if __name__ == "__main__":
    main()

# ---- COMPITO (stesse righe del documento da compilare su Classroom) ----
TC = {"IT": ("Compito — La divisione per 2 con il resto", "Classe 1 · da consegnare · 02/10/2026",
             "Scrivi il risultato e il resto. I conti sul foglio.", "Livello 3 — divisioni a catena: il risultato va nella riga sotto come numero nuovo.",
             ""),
      "AR": ("واجب — القسمة على 2 مع الباقي", "الصف الأول · يُسلَّم · 02/10/2026",
             "اكتب الناتج والباقي. الحساب على الورقة.", "المستوى 3 — قسمة متتالية: الناتج يُكتب في السطر التالي كعدد جديد.",
             ""),
      "ZH": ("作业 — 除以 2 和余数", "一年级 · 要交 · 02/10/2026",
             "写出结果和余数。在纸上算。", "第 3 级 — 连续除法:结果写到下一行当作新数字。",
             "")}

def compito(L, t):
    ti, su, istr, l3, sf = TC[L]
    k = 0; righe = ""
    for n in (4, 5, 8, 9, 10, 11, 14, 15, 20, 21):
        k += 1
        righe += f"<div class='ese'><span class='k'>{k}.</span><span class='big'>{n} : 2 = ____ <bdi>{t['resto']}</bdi> ____</span></div>"
    cat = catena(L, t)
    return (f"<div class='cover'><h1>{ti}</h1><div class='s'>{su}</div></div><p class='testo'>{istr}</p>"
            f"<p class='big'>{ {'IT':'Esempio','AR':'مثال','ZH':'例子'}[L] }: 7 : 2 = 3 <bdi>{t['resto']}</bdi> 1</p>{righe}"
            f"<div style='page-break-inside:avoid'><h2 class='testo'>{l3}</h2>{cat}</div>"
            f"<div style='page-break-inside:avoid'><h2 class='testo'>{ {'IT':'Sfide (solo se hai finito)','AR':'تحديات (إذا أنهيت فقط)','ZH':'挑战(做完了才做)'}[L] }</h2>"
            + ''.join(f"<div class='ese'><span class='k'>{11+i}.</span><span class='big'>{n} : 2 = ____ <bdi>{t['resto']}</bdi> ____</span></div>" for i, n in enumerate((33, 45, 58, 67))) + "</div>")

def main_compito():
    for L, t in T.items():
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head><body class='{cls}'>{compito(L, t)}</body></html>"
        hp = f"{OUT}/compito-divisione-per-2-{L}.html"; open(hp, "w").write(html)
        pdf(hp, f"{OUT}/Compito-Divisione-per-2-{L}-v{VER}.pdf")
        print("OK compito", L)

if __name__ == "__main__":
    main_compito()
