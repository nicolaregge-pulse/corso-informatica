# -*- coding: utf-8 -*-
# SCHEDA FACILE (recupero in classe, 02/10/2026): "Il byte con le monete".
# Nata perché i ragazzi faticavano su DUE cose: (1) generare il numero binario, (2) riempire
# con gli 0 fino a 8 bit. Metodo delle MONETE sulla griglia di 8 caselle (la stessa di ieri e
# della dispensa, §2.19): gli zeri davanti vengono DA SOLI, perché ogni casella va riempita.
# Gradini bassissimi: 1 moneta -> 2 monete (con aiuto) -> 3 monete -> "completa il byte".
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_decimale_binario import CSS, POS, svg_byte, byte, binario, pdf, OUT, VER

def monete(n): return [v for v, c in zip(POS, byte(n)) if c == "1"]

def svg_aiuto(n):
    """Griglia vuota con le MONETE da usare evidenziate in giallo (aiuto del livello 2)."""
    CW, CH, W = 34, 26, 8 * 34 + 2
    H = CH * 2 + 2
    usa = set(monete(n))
    s = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' width='{W*0.26:.0f}mm' height='{H*0.26:.0f}mm' class='svgbyte'>"]
    for i, v in enumerate(POS):
        x = 1 + i * CW
        fill = "#ffe58a" if v in usa else "#f3f7fb"
        s.append(f"<rect x='{x}' y='1' width='{CW}' height='{CH}' fill='{fill}' stroke='#9cc0e4'/>"
                 f"<text x='{x+CW/2}' y='18' font-size='12' text-anchor='middle' fill='#12467a' font-weight='{'bold' if v in usa else 'normal'}'>{v}</text>"
                 f"<rect x='{x}' y='{CH+1}' width='{CW}' height='{CH}' fill='#ffffff' stroke='#9cc0e4'/>")
    s.append("</svg>")
    return "".join(s)

L1 = [1, 2, 4, 8, 16, 32]          # una sola moneta
L2 = [3, 5, 6, 10, 12, 20]         # due monete (con aiuto giallo)
L3 = [7, 11, 13, 21, 37]           # tre monete
L4 = ["101", "11", "1001", "110", "10010"]   # completa il byte (zeri davanti)

T = {
"IT": dict(
 titolo="Scheda facile — Il byte con le monete", sub="Classe 1 · da fare sul foglio · italiano",
 idea="""<h2>1. Il byte è una fila di 8 caselle</h2>
<p>Ogni casella vale una <b>moneta</b>: <b>128, 64, 32, 16, 8, 4, 2, 1</b>.
In ogni casella scrivi <b>1</b> se usi quella moneta, <b>0</b> se non la usi.</p>
<div class="attn"><b>Regola d'oro:</b> le caselle sono <b>sempre 8</b> e <b>nessuna resta vuota</b>.
Se una moneta non serve, scrivi <b>0</b>. Ecco perché davanti compaiono gli zeri!</div>""",
 metodo="""<h2>2. Il metodo delle monete</h2>
<ol><li>Parti dalla moneta più <b>grande</b> (128) e vai verso destra.</li>
<li>Chiediti: <b>ci sta nel mio numero?</b> Sì → scrivi <b>1</b> e <b>togli</b> la moneta. No → scrivi <b>0</b>.</li>
<li>Continua con quello che <b>resta</b>, fino all'ultima casella (1).</li></ol>""",
 es_h="Esempio: 5", col=("moneta", "ci sta?", "scrivo", "resta"), si="sì", no="no",
 es_fine="Il byte di 5 è <code>00000101</code>. Controllo: 4 + 1 = 5. Giusto!",
 h1="Livello 1 — una sola moneta (facilissimo)", h2="Livello 2 — due monete (le monete giuste sono in giallo)",
 h3="Livello 3 — tre monete", h4="Livello 4 — completa il byte",
 h4_txt="Hai un numero binario corto. Scrivilo nelle caselle <b>partendo da DESTRA</b>, poi riempi con <b>0</b> le caselle vuote a sinistra.",
 es4="Esempio: <code>101</code> → <code>00000101</code>",
 numero="numero", controllo="controllo", fatto="FATTO! Ora sai fare il byte di qualsiasi numero fino a 255."),
"AR": dict(
 titolo="ورقة سهلة — البايت بالعملات", sub="الصف الأول · تُحلّ على الورقة · العربية",
 idea="""<h2>1. البايت صفّ من 8 خانات</h2>
<p>كل خانة تساوي <b>عملة</b>: <b>128، 64، 32، 16، 8، 4، 2، 1</b>.
في كل خانة اكتب <b>1</b> إذا استعملت العملة، و<b>0</b> إذا لم تستعملها.</p>
<div class="attn"><b>القاعدة الذهبية:</b> الخانات <b>دائمًا 8</b> و<b>لا تبقى أي خانة فارغة</b>.
إذا لم تحتج العملة اكتب <b>0</b>. لهذا تظهر الأصفار في البداية!</div>""",
 metodo="""<h2>2. طريقة العملات</h2>
<ol><li>ابدأ من أكبر عملة (128) واتجه نحو اليمين.</li>
<li>اسأل نفسك: <b>هل تدخل في عددي؟</b> نعم ← اكتب <b>1</b> واطرح العملة. لا ← اكتب <b>0</b>.</li>
<li>استمر مع <b>الباقي</b> حتى آخر خانة (1).</li></ol>""",
 es_h="مثال: 5", col=("العملة", "تدخل؟", "أكتب", "الباقي"), si="نعم", no="لا",
 es_fine="بايت العدد 5 هو <code>00000101</code>. التحقق: 4 + 1 = 5. صحيح!",
 h1="المستوى 1 — عملة واحدة (سهل جدًا)", h2="المستوى 2 — عملتان (العملات الصحيحة باللون الأصفر)",
 h3="المستوى 3 — ثلاث عملات", h4="المستوى 4 — أكمل البايت",
 h4_txt="لديك عدد ثنائي قصير. اكتبه في الخانات <b>بدءًا من اليمين</b>، ثم املأ الخانات الفارغة على اليسار بـ <b>0</b>.",
 es4="مثال: <code>101</code> ← <code>00000101</code>",
 numero="العدد", controllo="التحقق", fatto="أحسنت! الآن تعرف كيف تكتب بايت أي عدد حتى 255."),
"ZH": dict(
 titolo="简单练习 — 用硬币做字节", sub="一年级 · 在纸上做 · 中文",
 idea="""<h2>1. 字节是一排 8 个格子</h2>
<p>每个格子是一个<b>硬币</b>:<b>128、64、32、16、8、4、2、1</b>。
用到这个硬币就写 <b>1</b>,不用就写 <b>0</b>。</p>
<div class="attn"><b>黄金规则:</b>格子<b>永远是 8 个</b>,<b>一个都不能空着</b>。
不用的硬币写 <b>0</b>。所以前面会出现 0!</div>""",
 metodo="""<h2>2. 硬币法</h2>
<ol><li>从<b>最大</b>的硬币(128)开始,往右走。</li>
<li>问自己:<b>放得下吗?</b>能 → 写 <b>1</b>,并<b>减掉</b>这个硬币。不能 → 写 <b>0</b>。</li>
<li>用<b>剩下的</b>继续,一直到最后一个格子(1)。</li></ol>""",
 es_h="例子:5", col=("硬币", "放得下?", "写", "剩下"), si="能", no="不能",
 es_fine="5 的字节是 <code>00000101</code>。检查:4 + 1 = 5。对了!",
 h1="第 1 级 — 只有一个硬币(非常简单)", h2="第 2 级 — 两个硬币(要用的硬币是黄色的)",
 h3="第 3 级 — 三个硬币", h4="第 4 级 — 把字节补完整",
 h4_txt="给你一个短的二进制数。<b>从右边开始</b>写进格子,然后在左边空的格子里写 <b>0</b>。",
 es4="例子:<code>101</code> → <code>00000101</code>",
 numero="数字", controllo="检查", fatto="做到了!现在你会写 255 以内任何数字的字节了。"),
}

EXTRA_CSS = """
table.passi{border-collapse:collapse;margin:2mm 0;font-size:11pt;direction:ltr}
table.passi td,table.passi th{border:1px solid #9cc0e4;padding:1mm 4mm;text-align:center}
table.passi th{background:#eef4fb;color:#12467a}
table.passi .si{background:#eafaf0;color:#1e7a44;font-weight:bold}
.ese{border:1px solid #d5e0ec;border-radius:8px;padding:2.5mm 4mm;margin:2.5mm 0;background:#fafcff;page-break-inside:avoid;direction:ltr}
.ese .t{font-weight:bold;color:#12467a;margin-bottom:1mm}
.ese .r{margin-top:1.5mm;font-size:10.5pt}
.fatto{background:#eafaf0;border:2px solid #2f9e57;border-radius:10px;padding:4mm;text-align:center;font-size:13pt;color:#1e7a44;font-weight:bold;margin-top:5mm}
"""

def passi(L, n):
    t = T[L]; resta = n; rows = []
    for v in POS:
        ok = v <= resta
        if ok: resta -= v
        rows.append(f"<tr><td>{v}</td><td class='{'si' if ok else ''}'>{t['si'] if ok else t['no']}</td>"
                    f"<td class='{'si' if ok else ''}'>{1 if ok else 0}</td><td>{resta}</td></tr>")
    h = "".join(f"<th>{c}</th>" for c in t["col"])
    return f"<table class='passi'><tr>{h}</tr>{''.join(rows)}</table>"

def ese(L, k, n, aiuto=False):
    t = T[L]
    g = svg_aiuto(n) if aiuto else svg_byte(None)
    return (f"<div class='ese'><div class='t'>{k}. {t['numero']} {n}</div>{g}"
            f"<div class='r'>{t['controllo']}: ______ + ______ + ______ = {n}</div></div>")

def ese4(L, k, b):
    return (f"<div class='ese'><div class='t'>{k}. <code>{b}</code> → ________</div>{svg_byte(None)}</div>")

def main():
    for L, t in T.items():
        body = (f"<div class='cover'><h1>{t['titolo']}</h1><div class='s'>{t['sub']}</div></div>"
                f"<div class='testo'>{t['idea']}{t['metodo']}<h2>{t['es_h']}</h2></div>"
                f"<div style='display:flex;gap:8mm;align-items:center;direction:ltr'>{passi(L, 5)}<div>{svg_byte(5)}</div></div>"
                f"<div class='testo'><p>{t['es_fine']}</p><h2>{t['h1']}</h2></div>")
        k = 0
        for n in L1: k += 1; body += ese(L, k, n)
        body += f"<div class='testo'><h2>{t['h2']}</h2></div>"
        for n in L2: k += 1; body += ese(L, k, n, aiuto=True)
        body += f"<div class='testo'><h2>{t['h3']}</h2></div>"
        for n in L3: k += 1; body += ese(L, k, n)
        body += (f"<div class='testo'><h2>{t['h4']}</h2><p>{t['h4_txt']}</p><p>{t['es4']}</p></div>"
                 f"<div style='direction:ltr'>{svg_byte(5)}</div>")
        for b in L4: k += 1; body += ese4(L, k, b)
        body += f"<div class='fatto testo'>{t['fatto']}</div>"
        cls = {"IT": "lang-it", "AR": "lang-ar", "ZH": "lang-zh"}[L]
        html = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}{EXTRA_CSS}</style></head>"
                f"<body class='{cls}'>{body}</body></html>")
        hp = f"{OUT}/scheda-facile-{L}.html"; open(hp, "w").write(html)
        pdf(hp, f"{OUT}/Scheda-Facile-Byte-Monete-{L}-v{VER}.pdf")
        print("OK", L)

if __name__ == "__main__":
    main()
