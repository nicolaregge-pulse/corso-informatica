# -*- coding: utf-8 -*-
# Lezione 02/10/2026 Classe 1, 6a ora (13:05-14:00): "Il tuo NOME in binario (ASCII) e i COLORI (RGB)".
# Continua il METODO DELLE MONETE (stessa griglia del byte, §2.19). Trucco chiave: ogni lettera
# MAIUSCOLA = 64 + posizione nell'alfabeto -> il byte comincia sempre con 010.
# Genera Dispensa + Compito IT/AR/ZH (PDF) + coda per l'automazione (Doc da compilare).
import os, sys, json
sys.path.insert(0, "/home/user/corso-godot/classe-1/decimale-binario/_build")
from gen_decimale_binario import CSS, POS, byte, pdf
from gen_facili_v11 import tabella, otto, divs, XCSS as XCSS11

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = "1.1"  # v1.1: tolto il metodo delle monete, solo divisioni per 2 (metodo di Nicola)
LETTERE = [chr(c) for c in range(65, 91)]
def somma(n): return " + ".join(str(v) for v, c in zip(POS, byte(n)) if c == "1")

def tab_ascii():
    r1 = "".join(f"<td><b>{l}</b></td>" for l in LETTERE[:13]); r2 = "".join(f"<td>{ord(l)}</td>" for l in LETTERE[:13])
    r3 = "".join(f"<td><b>{l}</b></td>" for l in LETTERE[13:]); r4 = "".join(f"<td>{ord(l)}</td>" for l in LETTERE[13:])
    return f"<table class='asc'><tr>{r1}</tr><tr>{r2}</tr><tr>{r3}</tr><tr>{r4}</tr></table>"

COLORI = [("255,0,0", "#ff0000"), ("0,255,0", "#00ff00"), ("0,0,255", "#0000ff"),
          ("255,255,0", "#ffff00"), ("255,255,255", "#ffffff"), ("0,0,0", "#000000")]
NOMI_COL = {"IT": ["rosso", "verde", "blu", "giallo", "bianco", "nero"],
            "AR": ["أحمر", "أخضر", "أزرق", "أصفر", "أبيض", "أسود"],
            "ZH": ["红", "绿", "蓝", "黄", "白", "黑"]}

def tab_colori(L):
    rows = "".join(f"<tr><td><span class='sw' style='background:{h}'></span></td><td>{NOMI_COL[L][i]}</td>"
                   f"<td><code>{rgb}</code></td></tr>" for i, (rgb, h) in enumerate(COLORI))
    return f"<table class='col'>{rows}</table>"

T = {
"IT": dict(
 titolo="Il tuo nome in binario e i colori", sub="Classe 1 · ASCII e RGB · italiano · 02/10/2026",
 ctitolo="Compito — Il tuo nome in binario e i colori", csub="Classe 1 · da consegnare · 02/10/2026",
 s1="1. Anche le lettere sono numeri", s1t="Nel computer ogni lettera ha un <b>numero</b> (si chiama codice <b>ASCII</b>). Ecco le maiuscole:",
 trucco="<b>Come stamattina:</b> prendi il numero della lettera, <b>dividi per 2</b> (pari → 0, dispari → 1), leggi i resti <b>dal basso</b> e metti gli <b>zeri davanti</b> fino a 8.",
 s2="2. Dalla lettera al byte (divisioni per 2)", s2t="Lettera → numero (tabella) → divisioni per 2 → byte.",
 es="A = 65:", es2="La parola CIAO:",
 s3="3. I colori sono 3 numeri", s3t="Ogni colore dello schermo è fatto di 3 numeri: <b>R</b>osso, <b>G</b> verde, <b>B</b>lu. Ognuno va da <b>0 a 255</b> = <b>1 byte</b>. Un colore = 3 byte.",
 t255="<b>Facile:</b> 255 = <code>11111111</code> (tutti 1) e 0 = <code>00000000</code> (tutti 0). Facilissimo!",
 rosso="Rosso (255,0,0) in binario:",
 tuo="<b>Fallo tuo:</b> scrivi su Google <b>selettore colori</b>: scegli il tuo colore preferito e leggi i 3 numeri RGB.",
 attn="<b>Come si fa:</b> i conti sul FOGLIO. Poi apri il documento del compito (è già il TUO) e scrivi le risposte DOPO I DUE PUNTI. Alla fine premi il bottone blu <b>Consegna</b>.",
 p1="Parte 1 — Le lettere (per tutti)", p1t="Scrivi il byte di ogni lettera.",
 p2="Parte 2 — Il tuo nome", p2t="Scrivi il tuo nome in MAIUSCOLO, una lettera per riga, con il suo byte.",
 p3="Parte 3 — I colori", p3t="Scrivi i 3 byte di ogni colore.",
 p4="Sfide (solo se hai finito)", p4t="Minuscola: a = 97 (= A + 32). Spazio = 32. Arancione = 255,165,0: scrivi 165 in binario.",
 foot="Corso Informatica — Classe 1 · Il tuo nome in binario e i colori"),
"AR": dict(
 titolo="اسمك بالثنائي والألوان", sub="الصف الأول · ASCII و RGB · العربية · 02/10/2026",
 ctitolo="واجب — اسمك بالثنائي والألوان", csub="الصف الأول · يُسلَّم · 02/10/2026",
 s1="1. الحروف أيضًا أرقام", s1t="في الحاسوب لكل حرف <b>رقم</b> (اسمه رمز <b>ASCII</b>). هذه الحروف الكبيرة:",
 trucco="<b>مثل الصباح:</b> خذ رقم الحرف، <b>اقسم على 2</b> (زوجي ← 0، فردي ← 1)، اقرأ البواقي <b>من الأسفل</b> وضع <b>أصفارًا في البداية</b> حتى 8.",
 s2="2. من الحرف إلى البايت (القسمة على 2)", s2t="الحرف ← الرقم (الجدول) ← القسمة على 2 ← البايت.",
 es="A = 65:", es2="كلمة CIAO:",
 s3="3. الألوان هي 3 أرقام", s3t="كل لون على الشاشة مصنوع من 3 أرقام: <b>R</b> أحمر، <b>G</b> أخضر، <b>B</b> أزرق. كل رقم من <b>0 إلى 255</b> = <b>بايت واحد</b>. اللون = 3 بايت.",
 t255="<b>سهل:</b> 255 = <code>11111111</code> (كلها 1) و 0 = <code>00000000</code> (كلها 0). سهل جدًا!",
 rosso="الأحمر (255,0,0) بالثنائي:",
 tuo="<b>اجعله لك:</b> اكتب في Google <b>selettore colori</b> (منتقي الألوان): اختر لونك المفضل واقرأ أرقام RGB الثلاثة.",
 attn="<b>كيف تعمل:</b> الحساب على الورقة. ثم افتح مستند الواجب (هو نسختك) واكتب الأجوبة بعد النقطتين. في النهاية اضغط الزر الأزرق في الأعلى على اليمين (\"Consegna\" = تسليم).",
 p1="الجزء 1 — الحروف (للجميع)", p1t="اكتب بايت كل حرف.",
 p2="الجزء 2 — اسمك", p2t="اكتب اسمك بالحروف اللاتينية الكبيرة، حرف في كل سطر، مع البايت.",
 p3="الجزء 3 — الألوان", p3t="اكتب البايتات الثلاثة لكل لون.",
 p4="تحديات (إذا أنهيت فقط)", p4t="حرف صغير: a = 97 (= A + 32). المسافة = 32. البرتقالي = 255,165,0: اكتب 165 بالثنائي.",
 foot="Corso Informatica — Classe 1 · اسمك بالثنائي والألوان"),
"ZH": dict(
 titolo="你的名字和颜色的二进制", sub="一年级 · ASCII 和 RGB · 中文 · 02/10/2026",
 ctitolo="作业 — 你的名字和颜色的二进制", csub="一年级 · 要交 · 02/10/2026",
 s1="1. 字母也是数字", s1t="在计算机里每个字母都有一个<b>数字</b>(叫 <b>ASCII</b> 码)。这是大写字母:",
 trucco="<b>和上午一样:</b>拿字母的数字,<b>除以 2</b>(偶数 → 0,奇数 → 1),<b>从下往上</b>读余数,<b>前面补 0</b> 到 8 位。",
 s2="2. 从字母到字节(除以 2)", s2t="字母 → 数字(查表)→ 除以 2 → 字节。",
 es="A = 65:", es2="单词 CIAO:",
 s3="3. 颜色是 3 个数字", s3t="屏幕上的每个颜色由 3 个数字组成:<b>R</b> 红、<b>G</b> 绿、<b>B</b> 蓝。每个从 <b>0 到 255</b> = <b>1 个字节</b>。一个颜色 = 3 个字节。",
 t255="<b>很简单:</b>255 = <code>11111111</code>(全是 1),0 = <code>00000000</code>(全是 0)。很简单!",
 rosso="红色 (255,0,0) 的二进制:",
 tuo="<b>做你自己的:</b>在 Google 里写 <b>selettore colori</b>(取色器):选你最喜欢的颜色,读出 3 个 RGB 数字。",
 attn="<b>怎么做:</b>在纸上计算。然后打开作业文档(是你自己的副本),把答案写在冒号后面。最后点右上方的蓝色按钮(\"Consegna\" = 提交)。",
 p1="第一部分 — 字母(所有人)", p1t="写出每个字母的字节。",
 p2="第二部分 — 你的名字", p2t="用拉丁大写字母写你的名字,每行一个字母,加上它的字节。",
 p3="第三部分 — 颜色", p3t="写出每个颜色的 3 个字节。",
 p4="挑战(做完了才做)", p4t="小写:a = 97(= A + 32)。空格 = 32。橙色 = 255,165,0:把 165 写成二进制。",
 foot="Corso Informatica — Classe 1 · 你的名字和颜色的二进制"),
}

XCSS = """
table.asc{border-collapse:collapse;margin:2mm auto;direction:ltr;font-size:11pt}
table.asc td{border:1px solid #9cc0e4;padding:1mm 2.2mm;text-align:center}
table.asc tr:nth-child(odd){background:#eef4fb}
table.col{border-collapse:collapse;margin:2mm 0;direction:ltr}
table.col td{border:1px solid #d5e0ec;padding:1.5mm 4mm;font-size:12pt}
.sw{display:inline-block;width:12mm;height:7mm;border:1px solid #888;border-radius:3px;vertical-align:middle}
.riga{display:flex;align-items:center;gap:5mm;margin:2mm 0;direction:ltr;page-break-inside:avoid}
.riga .l{min-width:30mm;font-weight:bold;font-size:12.5pt;color:#12467a}
.vuota{border-bottom:1px solid #9cc0e4;min-width:60mm;height:7mm}
"""

LET_BASE = ["B", "D", "H", "I", "P"]
COL_BASE = [("rosso", "255,0,0"), ("bianco", "255,255,255"), ("nero", "0,0,0"), ("giallo", "255,255,0")]

def dispensa(L, t):
    ciao = "".join(f"<div class='riga'><span class='l'>{c} = {ord(c)}</span>{otto(byte(ord(c)), rosso=8-len(format(ord(c),'b')), scala=0.34)}</div>" for c in "CIAO")
    return (f"<div class='cover'><h1>{t['titolo']}</h1><div class='s'>{t['sub']}</div></div>"
            f"<div class='testo'><h2>{t['s1']}</h2><p>{t['s1t']}</p></div>{tab_ascii()}"
            f"<div class='vinci testo'>{t['trucco']}</div>"
            f"<div class='testo'><h2>{t['s2']}</h2><p>{t['s2t']}</p></div>"
            f"<div class='riga'><span class='l testo'>{t['es']}</span>{tabella(divs(65), lab=('÷ 2', {'IT':'resto','AR':'الباقي','ZH':'余数'}[L]), freccia=True, scala=0.24)}<span>→ <code>1000001</code> →</span>{otto(byte(65), rosso=1, scala=0.34)}</div>"
            f"<p class='testo'><b>{t['es2']}</b></p>{ciao}"
            f"<div class='testo'><h2>{t['s3']}</h2><p>{t['s3t']}</p></div>{tab_colori(L)}"
            f"<div class='vinci testo'>{t['t255']}</div>"
            f"<p class='testo'><b>{t['rosso']}</b></p>"
            f"<div class='riga'>{otto(byte(255), scala=0.3)}{otto(byte(0), scala=0.3)}{otto(byte(0), scala=0.3)}</div>"
            f"<div class='nota testo'>{t['tuo']}</div><div class='foot'>{t['foot']} · v{VER}</div>")

def compito(L, t):
    lett = "".join(f"<div class='riga'><span class='l'>{c} = {ord(c)}</span>{otto(scala=0.34)}</div>" for c in LET_BASE)
    nome = "".join(f"<div class='riga'><span class='l'>___ = ___</span>{otto(scala=0.34)}</div>" for _ in range(6))
    col = "".join(f"<div class='riga'><span class='l'><span class='sw' style='background:{dict(COLORI)[rgb]}'></span> {rgb}</span>"
                  f"<span class='vuota'></span></div>" for _, rgb in COL_BASE)
    return (f"<div class='cover'><h1>{t['ctitolo']}</h1><div class='s'>{t['csub']}</div></div>"
            f"<div class='attn testo'>{t['attn']}</div>"
            f"<div class='testo'><h2>{t['p1']}</h2><p>{t['p1t']}</p></div>"
            f"<div class='riga'><span class='l'>A = 65</span>{otto(byte(65), rosso=1, scala=0.34)}</div>{lett}"
            f"<div class='testo'><h2>{t['p2']}</h2><p>{t['p2t']}</p></div>{nome}"
            f"<div class='testo'><h2>{t['p3']}</h2><p>{t['p3t']}</p></div>{col}"
            f"<div class='testo'><h2>{t['p4']}</h2><p>{t['p4t']}</p></div><div class='foot'>{t['foot']} · v{VER}</div>")

def main():
    for L, t in T.items():
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        for kind, fn, name in (("dispensa", dispensa, "Dispensa"), ("compito", compito, "Compito")):
            html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head>"
                    f"<body class='{cls}'>{fn(L, t)}</body></html>")
            hp = f"{OUT}/{kind}-nome-colori-{L}.html"; open(hp, "w").write(html)
            pdf(hp, f"{OUT}/{name}-Nome-Colori-{L}-v{VER}.pdf")
        print("OK", L)
    # chiave di correzione (privato)
    key = {"compito": "Compito — Il tuo nome in binario e i colori", "classe": "1INF", "data": "2026-10-02",
           "lettere": {c: byte(ord(c)) for c in ["A"] + LET_BASE},
           "colori": {n: " ".join(byte(int(x)) for x in rgb.split(",")) for n, rgb in COL_BASE},
           "regola_nome": "ogni maiuscola = byte(ord(lettera)); minuscola = +32", "sfida_165": byte(165)}
    json.dump(key, open("/home/user/corso-informatica-riservato/materiale-esami/chiavi/1INF-nome-e-colori.json", "w"),
              ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
