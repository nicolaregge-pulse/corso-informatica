# -*- coding: utf-8 -*-
"""MD -> PDF A4 (testo grande, per la lettura al volo in classe). Uso: python3 genera.py
Genera i tre PDF singoli e il combinato con indice. Stesso parser di strumenti/md2pdf.py (liste numerate gerarchiche, tabelle, box)."""
import html, os, re, subprocess
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
QUI = os.path.dirname(os.path.abspath(__file__)); DIR = os.path.dirname(QUI)
GUIDE = [("guida-1inf-lazarus-04-11", "1INF Lazarus, 8:00-11:00"), ("guida-3inf-mastermind-04-11", "3INF Mastermind in rete, 11:00-13:00"), ("guida-1inf-sicurezza-04-11", "1INF Sicurezza 4ª ora, 13:00-14:00")]
e = html.escape
def inline(t):
    t = e(t); t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t); t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", t)
def md2html(md):
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
            out.append("<table><tr>" + "".join(f"<th>{inline(x)}</th>" for x in cel[0]) + "</tr>" + "".join("<tr>" + "".join((f"<td style='white-space:nowrap'>{inline(x)}</td>" if re.match(r"^\d+:\d+(-\d+:\d+)?$", x) else f"<td>{inline(x)}</td>") for x in rr) + "</tr>" for rr in cel[1:]) + "</table>"); continue
        if r.startswith("> "):
            cls = "att" if "Attenzione" in r else ("conf" if "Da confermare" in r else "nota")
            out.append(f"<div class='box {cls}'>{inline(r[2:])}</div>"); i += 1; continue
        if re.match(r"^( {3})*\d+\. ", r):
            voci = []
            while i < len(righe) and (re.match(r"^( {3})*\d+\. ", righe[i]) or re.match(r"^ {3,}> ", righe[i])):
                if righe[i].lstrip().startswith("> "):
                    voci.append((voci[-1][0] + 1 if voci else 0, "@@" + righe[i].lstrip()[2:])); i += 1; continue
                m = re.match(r"^((?: {3})*)\d+\. (.*)$", righe[i]); voci.append((len(m.group(1)) // 3, m.group(2))); i += 1
            cont, hl = [0, 0, 0, 0, 0], []
            primo = re.match(r"^\d+", righe[i - len(voci)].strip())
            if primo and voci[0][0] == 0: cont[0] = int(primo.group(0)) - 1
            for liv, testo in voci:
                if testo.startswith("@@"):
                    cls = "att" if "Attenzione" in testo else ("conf" if "Da confermare" in testo else "nota")
                    hl.append(f"<div class='box {cls} l{liv}'>{inline(testo[2:])}</div>"); continue
                cont[liv] += 1
                for k in range(liv + 1, len(cont)): cont[k] = 0
                num = ".".join(str(cont[k]) for k in range(liv + 1))
                hl.append(f"<div class='li l{liv}'><span class='n'>{num}</span><span>{inline(testo)}</span></div>")
            out.append("<div class='ol'>" + "".join(hl) + "</div>"); continue
        for k, tag in ((4, "h3"), (3, "h2"), (2, "h1")):
            if r.startswith("#" * (k - 1) + " "): out.append(f"<{tag}>{inline(r[k:])}</{tag}>"); break
        else:
            if r.strip(): out.append(f"<p>{inline(r)}</p>")
        i += 1
    return "\n".join(out)
CSS = """@page{size:A4;margin:12mm}body{font-family:"Segoe UI","DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:13.5px;line-height:1.5;margin:0}
h1{color:#12467a;font-size:27px;line-height:1.2;margin:0 0 6px}h2{color:#fff;background:#12467a;font-size:20px;padding:6px 10px;border-radius:6px;margin:22px 0 8px;break-after:avoid}
h3{font-size:16px}p{margin:6px 0}table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13px;break-inside:auto}tr{break-inside:avoid}th,td{border:1px solid #9fb0c6;padding:5px 7px;vertical-align:top;text-align:left}th{background:#dfe9f5}
.box{border-radius:6px;padding:8px 11px;margin:9px 0;break-inside:avoid}.nota{background:#fff8d6;border-left:6px solid #e0b400}.att{background:#fdecea;border-left:6px solid #c0392b}.conf{background:#e8f1fb;border-left:6px solid #2f6db5}
.ol{margin:6px 0 10px}.li{display:flex;gap:7px;margin:4px 0;break-inside:avoid}.li .n{min-width:2.6em;font-weight:700;color:#12467a}.l1{margin-left:1.8em}.l2{margin-left:3.6em}.l3{margin-left:5.4em}.l4{margin-left:7em}
pre{background:#f3f5f8;border:1px solid #c9d3e0;padding:8px;white-space:pre-wrap;word-break:break-word;font-size:13px;break-inside:avoid}code{background:#eef2f7;padding:0 3px;font-size:12px;word-break:break-all}
.cop{text-align:center;padding-top:60mm}.cop h1{font-size:40px}.pg{break-before:page}.ind li{margin:8px 0;font-size:16px}"""
def pdf(htmltxt, nome):
    h = os.path.join(QUI, nome + ".tmp.html"); p = os.path.join(DIR, nome + ".pdf")
    open(h, "w", encoding="utf-8").write(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>{htmltxt}")
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + p, "file://" + h], capture_output=True)
    os.remove(h); return p
corpi = {}
for n, t in GUIDE:
    md = open(os.path.join(DIR, n + ".md"), encoding="utf-8").read(); corpi[n] = md2html(md); pdf(corpi[n], n)
cop = "<div class='cop'><h1>Guida del docente 04/11</h1><p style='font-size:20px'>Mercoledì 04 novembre 2026</p><p style='font-size:16px'>Tre lezioni frontali, copione a minuti</p></div>"
ind = "<div class='pg'><h1>Indice</h1><ol class='ind'>" + "".join(f"<li>{t} <span style='color:#667'>(guida {k+1})</span></li>" for k, (n, t) in enumerate(GUIDE)) + "</ol><div class='box nota'>Orario: 08:00-11:00 1INF Laboratorio, 11:00-13:00 3INF Laboratorio, 13:00-14:00 1INF Sicurezza. Firma del registro entro le 14:05. Nessun nome di allievo in questa guida.</div></div>"
corpo = "".join(f"<div class='pg'>{corpi[n]}</div>" for n, t in GUIDE)
print(pdf(cop + ind + corpo, "guida-del-docente-04-11"))
