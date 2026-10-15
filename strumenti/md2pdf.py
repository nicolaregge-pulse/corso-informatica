# -*- coding: utf-8 -*-
"""MD (fonte, per l'AI) -> PDF versionato (lettura). Stesso stile del manuale docenti: tabelle, liste numerate, box
(> **Nota:** giallo, > **Attenzione:** rosso, > **Da confermare:** blu). Il nome del PDF prende data, nome e «Versione X.Y» dal MD.
Uso: python3 strumenti/md2pdf.py FILE.md DATA_AAAAMMGG Nome-Del-Pdf"""
import html, os, re, subprocess, sys
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
src, data, nome = sys.argv[1], sys.argv[2], sys.argv[3]
md = open(src, encoding="utf-8").read()
vers = re.search(r"\*\*Versione (\d+\.\d+)\*\*", md).group(1)
e = html.escape
def inline(t):
    t = e(t); t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t); return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
out, righe, i = [], md.split("\n"), 0
while i < len(righe):
    r = righe[i]
    if r.startswith("```"):
        j = i + 1; c = []
        while not righe[j].startswith("```"): c.append(righe[j]); j += 1
        out.append(f"<pre>{e(chr(10).join(c))}</pre>"); i = j + 1; continue
    if r.startswith("|"):
        t = []
        while i < len(righe) and righe[i].startswith("|"): t.append(righe[i]); i += 1
        cel = [[x.strip() for x in l.strip("|").split("|")] for l in t if not re.match(r"^\|[-| ]+\|$", l)]
        out.append("<table><tr>" + "".join(f"<th>{inline(x)}</th>" for x in cel[0]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{inline(x)}</td>" for x in rr) + "</tr>" for rr in cel[1:]) + "</table>"); continue
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
            html_l.append(f"<div class='li l{liv}'><span class='n'>{num}</span>{inline(testo)}</div>")
        out.append("<div class='ol'>" + "".join(html_l) + "</div>"); continue
    for k, tag in ((4, "h3"), (3, "h2"), (2, "h1")):
        if r.startswith("#" * (k - 1) + " "): out.append(f"<{tag}>{inline(r[k:])}</{tag}>"); break
    else:
        if r.strip(): out.append(f"<p>{inline(r)}</p>")
    i += 1
CSS = """body{font-family:"Segoe UI",Arial,sans-serif;color:#1a2330;font-size:12.5px;line-height:1.45;margin:18px 26px}h1{color:#12467a;font-size:22px}
h2{color:#12467a;font-size:17px;border-bottom:2px solid #d5dde8;padding-bottom:3px;margin-top:20px;break-after:avoid}h3{font-size:14px;break-after:avoid}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:11.5px}th,td{border:1px solid #c9d3e0;padding:4px 6px;vertical-align:top;text-align:left}th{background:#e9f0f8}
.box{border-radius:6px;padding:7px 10px;margin:8px 0}.nota{background:#fff8d6;border-left:5px solid #e0b400}.att{background:#fdecea;border-left:5px solid #c0392b}.conf{background:#e8f1fb;border-left:5px solid #2f6db5}
.ol{margin:4px 0 8px}.li{display:flex;gap:6px;margin:2px 0;break-inside:avoid}.li .n{min-width:2.2em;font-weight:600;color:#12467a}.l1{margin-left:1.6em}.l2{margin-left:3.2em}.l3{margin-left:4.8em}
pre{background:#f3f5f8;padding:6px;white-space:pre-wrap;word-break:break-all;font-size:10px}code{background:#eef2f7;padding:0 3px}"""
base = os.path.splitext(src)[0]
h = base + ".tmp.html"
open(h, "w", encoding="utf-8").write(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>" + "\n".join(out))
pdf = os.path.join(os.path.dirname(os.path.abspath(src)), f"{data}_{nome}_v{vers}.pdf")
subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + pdf, "file://" + os.path.abspath(h)], capture_output=True)
os.remove(h); print(pdf, os.path.getsize(pdf) // 1024, "KB")
