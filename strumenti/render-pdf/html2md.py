# -*- coding: utf-8 -*-
"""Crea la versione Markdown (.md) di una scheda HTML del corso, accanto all'HTML.
Serve la regola MD + PDF: il PDF si legge e si stampa, l'MD si dà ai ragazzi per la loro AI.
Uso: python3 strumenti/render-pdf/html2md.py file1.html [file2.html ...]
"""
import re, sys, os
import html2text

for p in sys.argv[1:]:
    h = open(p, encoding="utf-8").read()
    h = re.sub(r"<style.*?</style>", "", h, flags=re.S)
    h = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    h = re.sub(r"<i style='background:[^']*'>\d+</i>", "", h)   # i numeri colorati delle coppie begin/end
    c = html2text.HTML2Text()
    c.body_width = 0
    c.ignore_images = True
    md = c.handle(h).strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    out = os.path.splitext(p)[0] + ".md"
    open(out, "w", encoding="utf-8").write("<!-- generato da %s con html2md.py: non modificare a mano, si rigenera -->\n\n%s\n" % (os.path.basename(p), md))
    print(out)
