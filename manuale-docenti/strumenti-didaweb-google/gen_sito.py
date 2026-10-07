# -*- coding: utf-8 -*-
"""Manuale docenti «Strumenti automatici: DIDAweb e Google» → sito (docs/docenti/: home con indice + una pagina per capitolo,
caselle con il bottone Copia) e PDF versionato. Fonte unica: strumenti-didaweb-google.md (+ i file codice-*.txt dei segnalibri).
Le righe ```CODICE:file.txt``` vengono sostituite dal contenuto del file. Uso: python3 gen_sito.py"""
import html, os, re, subprocess
QUI = os.path.dirname(os.path.abspath(__file__))
SITO = os.path.join(QUI, "..", "..", "docs", "docenti")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
md = open(os.path.join(QUI, "strumenti-didaweb-google.md"), encoding="utf-8").read()
VERS = re.search(r"\*\*Versione (\d+\.\d+)\*\*", md).group(1)
e = html.escape
CSS = """:root{--blu:#12467a;--bg:#f6f8fb;--txt:#1a2330;--bordo:#d5dde8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font-family:"Segoe UI",Arial,sans-serif;line-height:1.5}
.w{max-width:960px;margin:0 auto;padding:16px 16px 60px}a{color:var(--blu)}
h1{color:var(--blu);font-size:28px;margin:8px 0}h2{color:var(--blu);font-size:22px;margin:28px 0 8px;border-bottom:2px solid var(--bordo);padding-bottom:4px;break-after:avoid}
h3{font-size:18px;margin:20px 0 6px;break-after:avoid}table{border-collapse:collapse;width:100%;margin:8px 0;background:#fff;font-size:14px}
th,td{border:1px solid var(--bordo);padding:6px 8px;vertical-align:top;text-align:left}th{background:#e9f0f8}
.box{border-radius:8px;padding:10px 12px;margin:10px 0}.nota{background:#fff8d6;border-left:6px solid #e0b400}
.att{background:#fdecea;border-left:6px solid #c0392b}.conf{background:#e8f1fb;border-left:6px solid #2f6db5}
.cod{background:#fff;border:1px solid var(--bordo);border-radius:8px;margin:8px 0}.cod pre{margin:0;padding:10px;white-space:pre-wrap;word-break:break-all;font-size:12px;max-height:160px;overflow:auto}
.cod button{display:block;width:100%;border:0;background:#ffd23f;font-weight:800;font-size:16px;padding:8px;border-radius:8px 8px 0 0;cursor:pointer}
nav.indice{background:#fff;border:1px solid var(--bordo);border-radius:10px;padding:10px 16px}nav.indice li{margin:4px 0}
.top{display:flex;gap:12px;flex-wrap:wrap;font-size:14px;margin-bottom:8px}.ver{color:#778;font-size:12px;margin-top:24px}
code{background:#eef2f7;padding:1px 4px;border-radius:4px}
@media print{.cod button,.top{display:none}.cod pre{max-height:none}body{background:#fff}}"""
JS = """<script>document.querySelectorAll('.cod button').forEach(function(b){b.onclick=function(){var t=b.nextElementSibling.textContent;
function ok(){b.textContent='Copiato! Ora Ctrl + V';setTimeout(function(){b.textContent='Copia'},2500)}
if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){fb(t);ok()})}else{fb(t);ok()}}});
function fb(t){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}</script>"""

def inline(t):
    t = e(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)

def blocchi(testo):
    out, righe, i = [], testo.split("\n"), 0
    while i < len(righe):
        r = righe[i]
        if r.startswith("```"):
            j = i + 1; corpo = []
            while not righe[j].startswith("```"): corpo.append(righe[j]); j += 1
            c = "\n".join(corpo)
            m = re.match(r"CODICE:(\S+)", c)
            if m: c = open(os.path.join(QUI, m.group(1)), encoding="utf-8").read().strip()
            out.append(f"<div class='cod'><button>Copia</button><pre>{e(c)}</pre></div>"); i = j + 1; continue
        if r.startswith("|"):
            t = []
            while i < len(righe) and righe[i].startswith("|"): t.append(righe[i]); i += 1
            cel = [[x.strip() for x in l.strip("|").split("|")] for l in t if not re.match(r"^\|[-| ]+\|$", l)]
            out.append("<table><tr>" + "".join(f"<th>{inline(x)}</th>" for x in cel[0]) + "</tr>" +
                       "".join("<tr>" + "".join(f"<td>{inline(x)}</td>" for x in rr) + "</tr>" for rr in cel[1:]) + "</table>"); continue
        if r.startswith("> "):
            cls = "att" if "Attenzione" in r else ("conf" if "Da confermare" in r else "nota")
            out.append(f"<div class='box {cls}'>{inline(r[2:])}</div>"); i += 1; continue
        if re.match(r"^\d+\. ", r):
            l = []
            while i < len(righe) and re.match(r"^\d+\. ", righe[i]): l.append(re.sub(r"^\d+\. ", "", righe[i])); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in l) + "</ol>"); continue
        if r.startswith("### "): out.append(f"<h3 id='{slug(r[4:])}'>{inline(r[4:])}</h3>")
        elif r.strip(): out.append(f"<p>{inline(r)}</p>")
        i += 1
    return "\n".join(out)

def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def pagina(titolo, corpo, nav=""):
    return (f"<!doctype html><html lang='it'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<meta http-equiv='Cache-Control' content='no-cache'><title>{e(titolo)}</title><style>{CSS}</style></head><body><div class='w'>"
            f"{nav}{corpo}<div class='ver'>Strumenti automatici del docente · Versione {VERS} · generato da manuale-docenti/strumenti-didaweb-google/</div></div>{JS}</body></html>")

testa, *capitoli = re.split(r"^## ", md, flags=re.M)
titolo = testa.split("\n")[0].lstrip("# ").strip()
intro = blocchi("\n".join(testa.split("\n")[1:]))
os.makedirs(SITO, exist_ok=True)
voci, tutto = [], []
for c in capitoli:
    tit, corpo = c.split("\n", 1)
    s = slug(tit); voci.append((tit, s))
    sub = re.findall(r"^### (.+)$", corpo, flags=re.M)
    tutto.append(f"<h2 id='{s}'>{inline(tit)}</h2>" + blocchi(corpo))
for k, (c, (tit, s)) in enumerate(zip(capitoli, voci)):
    corpo = c.split("\n", 1)[1]
    prev = f"<a href='{voci[k-1][1]}.html'>← {e(voci[k-1][0])}</a>" if k else ""
    nxt = f"<a href='{voci[k+1][1]}.html'>{e(voci[k+1][0])} →</a>" if k + 1 < len(voci) else ""
    nav = f"<div class='top'><a href='index.html'>Home</a>{prev}{nxt}</div>"
    open(os.path.join(SITO, s + ".html"), "w", encoding="utf-8").write(pagina(tit, f"<h1>{inline(tit)}</h1>" + blocchi(corpo), nav))
ind = "<nav class='indice'><ol>" + "".join(
    f"<li><a href='{s}.html'>{e(t)}</a>" + ("<ol>" + "".join(f"<li><a href='{s}.html#{slug(x)}'>{e(x)}</a></li>" for x in re.findall(r'^### (.+)$', c.split(chr(10), 1)[1], flags=re.M)) + "</ol>" if re.search(r'^### ', c, flags=re.M) else "") + "</li>"
    for (t, s), c in zip(voci, capitoli)) + "</ol></nav>"
pdfnome = f"20261007_Strumenti-DIDAweb-Google_Docente_v{VERS}.pdf"
home = (f"<h1>{e(titolo)}</h1>" + intro + "<h2>Indice</h2>" + ind +
        f"<p>Tutto in una pagina sola (da stampare): <a href='tutto.html'>versione completa</a> · PDF: <a href='{pdfnome}'>{pdfnome}</a></p>")
open(os.path.join(SITO, "index.html"), "w", encoding="utf-8").write(pagina(titolo, home))
open(os.path.join(SITO, "tutto.html"), "w", encoding="utf-8").write(pagina(titolo, f"<h1>{e(titolo)}</h1>" + intro + "".join(tutto), "<div class='top'><a href='index.html'>Home</a></div>"))
pdf = os.path.join(QUI, pdfnome)
subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + pdf, "file://" + os.path.abspath(os.path.join(SITO, "tutto.html"))], capture_output=True)
import shutil; shutil.copy(pdf, os.path.join(SITO, pdfnome))
print("pagine:", len(voci) + 2, "· PDF:", pdfnome, os.path.getsize(pdf) // 1024, "KB")
