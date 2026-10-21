# -*- coding: utf-8 -*-
"""Uscite dall'aula (bagno) per classe e per allievo (21/10/2026, Nicola: «classifica del bagno, quante volte, date e ore»).
Legge i diari del riservato (righe «- HH:MM COGNOME NOME: bagno») e scrive docs/avanzamento/uscite.json CIFRATO
(nomi di minori): la pagina docs/avanzamento/uscite.html lo apre con il codice del docente.
Uso: python3 strumenti/uscite.py"""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from cifra_json import scrivi
RIS = "/home/user/corso-informatica-riservato/diario"
righe = []
for f in sorted(glob.glob(RIS + "/*/*.md")):
    classe, data = f.split("/")[-2], os.path.basename(f)[:10]
    if not re.match(r"\d{4}-\d{2}-\d{2}$", data):
        continue
    for r in open(f, encoding="utf-8"):
        m = re.match(r"-\s*(\d{1,2}:\d{2})\s+([^:]+):\s*bagno", r.strip(), re.I)
        if m:
            righe.append({"classe": classe, "data": data, "ora": m.group(1), "nome": m.group(2).strip()})
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "avanzamento", "uscite.json")
scrivi(out, {"uscite": righe})
print(len(righe), "uscite")
