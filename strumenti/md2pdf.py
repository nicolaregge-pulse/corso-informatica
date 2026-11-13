# -*- coding: utf-8 -*-
"""MD (fonte, per l'AI) -> PDF versionato (lettura). Stesso stile del manuale docenti: tabelle, liste numerate, box
(> **Nota:** giallo, > **Attenzione:** rosso, > **Da confermare:** blu). Il nome del PDF prende data, nome e «Versione X.Y» dal MD.
Uso: python3 strumenti/md2pdf.py FILE.md DATA_AAAAMMGG Nome-Del-Pdf
Opzioni facoltative: MD2PDF_ARIA=1 (font grande e spazi generosi, riquadro «> **FAI LO SCREENSHOT» verde); `<<PAGINA>>` = salto pagina."""
import html, os, re, subprocess, sys
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
src, data, nome = sys.argv[1], sys.argv[2], sys.argv[3]
md = open(src, encoding="utf-8").read()
vers = re.search(r"\*\*Versione (\d+\.\d+)\*\*", md).group(1)
e = html.escape
ARIOSO = os.environ.get("MD2PDF_ARIOSO") == "1"   # opzionale: dispense per i ragazzi, font grande, margini larghi, it/ar/zh con direzione giusta
AR_RE, ZH_RE = re.compile(r"[\u0600-\u06FF]"), re.compile(r"[\u4e00-\u9fff]")
LRI, PDI = "\u2066", "\u2069"
LAT_RE = re.compile(r"`[^`]*`|«[^«»\u0600-\u06FF]*[A-Za-z0-9][^«»\u0600-\u06FF]*»|[A-Za-z][A-Za-z0-9]*(?:[ \-+'\u2019.][A-Za-z0-9]+)*")
def isola_latino(t):
    """in una frase araba ogni pezzo latino (parole, tasti, codice, titoli tra «») diventa un blocco isolato sinistra-destra: la punteggiatura araba non si sposta"""
    def f(m):
        x = m.group(0)
        if x.startswith("«"): return "«" + LRI + x[1:-1] + PDI + "»"
        return LRI + x + PDI
    return LAT_RE.sub(f, t)
def para(t):
    if not ARIOSO: return f"<p dir='auto'>{inline(t)}</p>"
    if AR_RE.search(t): return f"<p class='ar' dir='rtl' lang='ar'>{inline(isola_latino(t))}</p>"
    if ZH_RE.search(t): return f"<p class='zh' lang='zh'>{inline(t)}</p>"
    return f"<p class='it'>{inline(t)}</p>"
def inline(t):
    t = e(t); t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t); t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t); return re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", t)
out, righe, i = [], md.split("\n"), 0
while i < len(righe):
    r = righe[i]
    if r.startswith("<!--"):   # riga di commento (versione, changelog, note per il docente): resta nel MD, non va nel PDF
        while "-->" not in righe[i]: i += 1
        i += 1; continue
    if r.startswith("```"):
        j = i + 1; c = []
        while not righe[j].startswith("```"): c.append(righe[j]); j += 1
        out.append(f"<pre>{e(chr(10).join(c))}</pre>"); i = j + 1; continue
    if r.startswith("|"):
        t = []
        while i < len(righe) and righe[i].startswith("|"): t.append(righe[i]); i += 1
        cel = [[x.strip() for x in l.strip("|").split("|")] for l in t if not re.match(r"^\|[-| ]+\|$", l)]
        out.append("<table><tr>" + "".join(f"<th>{inline(x)}</th>" for x in cel[0]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{inline(x)}</td>" for x in rr) + "</tr>" for rr in cel[1:]) + "</table>"); continue
    if r.startswith("> **FAI LO SCREENSHOT"):  # riquadro verde ben visibile; le righe "> " consecutive stanno nello stesso riquadro
        blk = []
        while i < len(righe) and righe[i].startswith("> "): blk.append(inline(righe[i][2:])); i += 1
        out.append("<div class='box shot'>" + "".join("<div dir='auto' style='margin:3px 0'>" + b + "</div>" for b in blk) + "</div>"); continue
    if ARIOSO and (r.startswith("> ") or r == ">"):
        gruppo = []
        while i < len(righe) and (righe[i].startswith("> ") or righe[i] == ">"): gruppo.append(righe[i][2:]); i += 1
        cls = "shot" if "FAI LO SCREENSHOT" in gruppo[0] else ("att" if "Attenzione" in gruppo[0] else ("conf" if "Da confermare" in gruppo[0] else "nota"))
        out.append(f"<div class='box {cls}'>" + "".join(para(g) if g.strip() else "<div class='sp'></div>" for g in gruppo) + "</div>"); continue
    if r.startswith("> "):
        cls = "att" if "Attenzione" in r else ("conf" if "Da confermare" in r else "nota")
        out.append(f"<div class='box {cls}'>{inline(r[2:])}</div>"); i += 1; continue
    if re.match(r"^\d+\. ", r):
        # liste numerate anche annidate (3 spazi per livello): numeri gerarchici 1, 1.1, 1.1.1
        voci = []
        while i < len(righe) and re.match(r"^( {3})*\d+\. ", righe[i]):
            m = re.match(r"^((?: {3})*)\d+\. (.*)$", righe[i]); voci.append((len(m.group(1)) // 3, m.group(2))); i += 1
        cont, html_l = [0, 0, 0, 0], []
        primo = re.match(r"^\d+", righe[i - len(voci)].strip()) if voci else None
        if primo and voci and voci[0][0] == 0: cont[0] = int(primo.group(0)) - 1   # la lista riparte dal numero scritto (dopo un blocco di codice)
        for liv, testo in voci:
            cont[liv] += 1
            for k in range(liv + 1, len(cont)): cont[k] = 0
            num = ".".join(str(cont[k]) for k in range(liv + 1))
            html_l.append(f"<div class='li l{liv}'><span class='n'>{num}</span><span>{inline(testo)}</span></div>")
        out.append("<div class='ol'>" + "".join(html_l) + "</div>"); continue
    m = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", r)
    if m:  # immagine su riga propria: ![didascalia](percorso relativo al MD), incorporata nel PDF
        import base64
        pimg = os.path.join(os.path.dirname(os.path.abspath(src)), m.group(2))
        alt, _, larg = m.group(1).partition("|")   # facoltativo: ![didascalia|420](img.png) = larghezza massima 420 px
        stile = "max-width:" + (larg + "px" if larg.strip().isdigit() else "100%") + (";max-height:430px;border-radius:8px;border:1px solid #c9d3e0" if ARIOSO else ";max-height:560px")
        if os.path.exists(pimg):
            out.append("<p style='text-align:center;break-inside:avoid'><img style='" + stile + "' src='data:image/png;base64," + base64.b64encode(open(pimg, "rb").read()).decode() + "' alt='" + e(alt) + "'></p>")
        else:
            out.append("<p>[immagine mancante: " + e(m.group(2)) + "]</p>")
        i += 1; continue
    if r.strip()=="<<PAGINA>>":
        out.append("<div style='break-before:page'></div>"); i += 1; continue
    for k, tag in ((4, "h3"), (3, "h2"), (2, "h1")):
        if r.startswith("#" * (k - 1) + " "): out.append(f"<{tag}>{inline(r[k:])}</{tag}>"); break
    else:
        if r.strip(): out.append(para(r))
    i += 1
CSS = """body{font-family:"Segoe UI",Arial,sans-serif;color:#1a2330;font-size:12.5px;line-height:1.45;margin:18px 26px}h1{color:#12467a;font-size:22px}
h2{color:#12467a;font-size:17px;border-bottom:2px solid #d5dde8;padding-bottom:3px;margin-top:20px;break-after:avoid}h3{font-size:14px;break-after:avoid}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:11.5px}th,td{border:1px solid #c9d3e0;padding:4px 6px;vertical-align:top;text-align:left}th{background:#e9f0f8}
.box{border-radius:6px;padding:7px 10px;margin:8px 0}.nota{background:#fff8d6;border-left:5px solid #e0b400}.att{background:#fdecea;border-left:5px solid #c0392b}.conf{background:#e8f1fb;border-left:5px solid #2f6db5}
.ol{margin:4px 0 8px}.li{display:flex;gap:6px;margin:2px 0;break-inside:avoid}.li .n{min-width:2.2em;font-weight:600;color:#12467a}.l1{margin-left:1.6em}.l2{margin-left:3.2em}.l3{margin-left:4.8em}
pre{background:#f3f5f8;padding:6px;white-space:pre-wrap;word-break:break-all;font-size:10px}code{background:#eef2f7;padding:0 3px}"""
if ARIOSO:  # font grande, margini larghi, poco testo per pagina (le pagine si spezzano con <<PAGINA>>)
    CSS = """@page{size:A4;margin:13mm 20mm}body{font-family:"DejaVu Sans","Segoe UI",Arial,sans-serif;color:#1a2330;font-size:19px;line-height:1.5;margin:0}
h1{color:#12467a;font-size:31px;line-height:1.25;margin:0 0 12px}h2{color:#12467a;font-size:27px;line-height:1.3;border-bottom:3px solid #d5dde8;padding-bottom:6px;margin:0 0 16px;break-after:avoid}
h3{color:#12467a;font-size:23px;margin:0 0 12px;break-after:avoid}p{margin:0}p.it{margin-top:14px}p.ar,p.zh{margin-top:5px}
p.ar{font-family:Amiri,"DejaVu Sans",serif;font-size:22px;line-height:1.55;color:#14456b}p.zh{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif;font-size:19px;color:#14456b}
code{direction:ltr;unicode-bidi:isolate;font-family:"DejaVu Sans Mono",monospace;background:#eef2f7;padding:1px 6px;border-radius:4px;font-size:17px}
.ol{margin:14px 0 0}.li{display:flex;gap:14px;margin:0;break-inside:avoid;font-size:21px}.li .n{flex:0 0 38px;height:38px;border-radius:50%;background:#12467a;color:#fff;text-align:center;line-height:38px;font-weight:700;min-width:0}
.box{border-radius:12px;padding:14px 22px 18px;margin:22px 0 0;break-inside:avoid}.box p:first-child{margin-top:0}.sp{height:10px}
.shot{border:5px solid #d62828;background:#fff4f4}.shot p.it:first-child{font-size:27px;font-weight:700;color:#c0392b}.nota{background:#fff8d6;border:3px solid #e0b400}.att{background:#fdecea;border:3px solid #c0392b}.conf{background:#e8f1fb;border:3px solid #2f6db5}
pre{background:#f3f5f8;padding:10px;white-space:pre-wrap;word-break:break-all;font-size:15px}"""
if os.environ.get("MD2PDF_ORIZZONTALE") == "1":  # opzionale: A4 orizzontale per tabelle larghe
    CSS += "\n@page{size:A4 landscape;margin:9mm}body{margin:4px 6px;font-size:11px}table{font-size:9.5px}th,td{padding:2px 4px}h1{font-size:19px}h2{font-size:15px}"
if os.environ.get("MD2PDF_ARIA") == "1":  # opzionale: dispense «con più aria» (font grande, margini larghi, pagine A4 con spazi generosi)
    CSS += """
@page{size:A4;margin:16mm 17mm}body{font-size:18px;line-height:1.75;margin:0}h1{font-size:30px;line-height:1.25}h2{font-size:25px;margin-top:6px}h3{font-size:21px;margin:22px 0 6px}
p{margin:0 0 15px}table{font-size:16px}th,td{padding:9px 10px}.box{font-size:18px;padding:12px 16px;margin:16px 0}.ol{margin:8px 0 6px}.li{margin:4px 0;gap:10px}.li .n{min-width:2.4em}
.shot{background:#e7f7ec;border:4px solid #1e8a4c;border-radius:12px;padding:16px 20px;margin:22px 0;break-inside:avoid;font-size:19px}"""
else:
    CSS += """
.shot{background:#e7f7ec;border:3px solid #1e8a4c;border-radius:10px;padding:10px 14px;margin:12px 0;break-inside:avoid}"""
base = os.path.splitext(src)[0]
h = base + ".tmp.html"
open(h, "w", encoding="utf-8").write(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>" + "\n".join(out))
pdf = os.path.join(os.path.dirname(os.path.abspath(src)), f"{data}_{nome}_v{vers}.pdf")
subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + pdf, "file://" + os.path.abspath(h)], capture_output=True)
os.remove(h); print(pdf, os.path.getsize(pdf) // 1024, "KB")
