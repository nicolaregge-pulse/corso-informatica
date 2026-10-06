# -*- coding: utf-8 -*-
"""Genera METODOLOGIA-CORSO-vX.Y.pdf da METODOLOGIA-CORSO.md (la versione si legge dall'intestazione).
Uso: python3 strumenti/gen_metodologia.py"""
import os, re, subprocess, markdown
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
md = open(os.path.join(R, "METODOLOGIA-CORSO.md"), encoding="utf-8").read()
ver = re.search(r"\*\*Versione (\d+\.\d+)\*\*", md).group(1)
# liste annidate: nel sorgente il rientro è di 3 spazi, Markdown ne vuole 4
md = "\n".join((" " * (4 * (len(l) - len(l.lstrip(" "))) // 3) + l.lstrip(" ")) if (len(l) - len(l.lstrip(" "))) % 3 == 0 else l for l in md.split("\n"))
corpo = markdown.markdown(md, extensions=["tables", "md_in_html", "sane_lists"])
css = """@page{size:A4;margin:16mm 15mm 18mm;@bottom-left{content:"Metodologia del corso — Versione %s";font:8.5pt 'DejaVu Sans';color:#667}
@bottom-right{content:"pagina " counter(page) " di " counter(pages);font:8.5pt 'DejaVu Sans';color:#667}}
body{font-family:'DejaVu Sans',Arial,sans-serif;font-size:10.3pt;line-height:1.45;color:#1a2330}
h1{color:#12467a;font-size:20pt;margin:0 0 4px}h2{color:#12467a;font-size:13.5pt;border-bottom:2px solid #c9d8ea;padding-bottom:2px;margin:18px 0 6px;break-after:avoid}
h3{color:#1f6fa5;font-size:11.5pt;margin:12px 0 4px;break-after:avoid}p{margin:5px 0}ol{margin:4px 0 6px;padding-left:22px}li{margin:2px 0}
table{border-collapse:collapse;width:100%%;font-size:9pt;margin:6px 0;break-inside:auto}th,td{border:1px solid #9fb3c8;padding:3px 5px;vertical-align:top;text-align:left}
th{background:#e3ecf6}tr{break-inside:avoid}code{font-family:'DejaVu Sans Mono',monospace;font-size:8.8pt;background:#f1f4f8;padding:0 2px}
hr{border:0;border-top:1px solid #c9d8ea}.box{border-left:6px solid;border-radius:6px;padding:6px 12px;margin:8px 0;break-inside:avoid}
.blu{background:#e8f1fb;border-color:#1f6fa5}.giallo{background:#fff8dc;border-color:#d4a017}.rosso{background:#fdecea;border-color:#c0392b}""" % ver
html = "<!doctype html><html lang='it'><meta charset='utf-8'><title>Metodologia del corso v%s</title><style>%s</style><body>%s</body></html>" % (ver, css, corpo)
hp = os.path.join(R, "strumenti", "_metodologia.tmp.html")
open(hp, "w", encoding="utf-8").write(html)
out = os.path.join(R, "METODOLOGIA-CORSO-v%s.pdf" % ver)
subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + out, "file://" + hp], capture_output=True)
os.remove(hp)
print(out)
