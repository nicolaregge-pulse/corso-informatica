# -*- coding: utf-8 -*-
"""Banca di una lezione (docs/verifica/banche/<banca>.js) -> documento MD della lezione (fonte per l'AI dei ragazzi) + PDF.
Un solo posto da cui nasce tutto: la pagina della lezione e il suo documento restano uguali.
Uso: python3 strumenti/banca2md.py <banca> <cartella-di-uscita> <AAAAMMGG> <Nome-Pdf> [riga «Compito» ...]"""
import html, json, os, re, subprocess, sys

banca, out, data, nome = sys.argv[1:5]
compito = sys.argv[5:]
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
js = "global.window={};require(%s);console.log(JSON.stringify(window.BANCA))" % json.dumps(R + "/docs/verifica/banche/" + banca + ".js")
B = json.loads(subprocess.check_output(["node", "-e", js]))


def testo(h):
    h = re.sub(r"<pre[^>]*>(.*?)</pre>", lambda m: "\n```\n" + html.unescape(m.group(1)) + "\n```\n", h, flags=re.S)
    h = re.sub(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"\2 (\1)", h)
    h = re.sub(r"<span lang=\"(ar|zh)\"[^>]*>", "\n\n", h)   # righe in arabo e cinese (L() delle banche 1INF): paragrafo a parte
    h = re.sub(r"<br\s*/?>", "\n", h)
    h = re.sub(r"<div[^>]*>(.*?)</div>", r"\n\n\1\n", h, flags=re.S)
    h = re.sub(r"</?b>", "**", h)
    h = re.sub(r"</?code>", "`", h)
    h = re.sub(r"<[^>]+>", "", h)
    return html.unescape(h).strip()


sito = "https://nicolaregge-pulse.github.io/corso-informatica/verifica/?b=" + banca
md = ["# " + B["titolo"], "", "**Versione 1.0** — " + data[6:] + "/" + data[4:6] + "/" + data[:4] + " · " + B.get("sotto", ""), "",
      "La pagina della lezione, con il ripasso: " + sito, ""]
for i, s in enumerate(B["schede"]):
    md += ["## %02d %s" % (i + 1, re.sub(r"^\d+\.\s*", "", s["titolo"].split(" · ")[0])), "", testo(s["testo"]), ""]
if compito:
    md += ["## %02d Che cosa fare oggi" % (len(B["schede"]) + 1), ""] + ["%d. %s" % (i + 1, c) for i, c in enumerate(compito)] + [""]
os.makedirs(out, exist_ok=True)
f = os.path.join(out, banca + ".md")
open(f, "w", encoding="utf-8").write("\n".join(md))
subprocess.run([sys.executable, os.path.join(R, "strumenti", "md2pdf.py"), f, data, nome], check=True)
print(f)
