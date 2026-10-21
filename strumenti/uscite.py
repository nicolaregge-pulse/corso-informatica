# -*- coding: utf-8 -*-
"""Uscite dall'aula (bagno) per classe e per allievo (21/10/2026, Nicola: «classifica del bagno, quante volte, date e ore»).
Legge i diari del riservato (righe «- HH:MM COGNOME NOME: bagno|uscita|rientro»; il rientro dà i minuti fuori) e scrive docs/avanzamento/uscite.json CIFRATO
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
    aperte = {}
    for r in open(f, encoding="utf-8"):
        m = re.match(r"-\s*(\d{1,2}:\d{2})\s+([^:]+):\s*(bagno|uscita|rientro)", r.strip(), re.I)
        if not m:
            continue
        ora, nome, tipo = m.group(1), m.group(2).strip(), m.group(3).lower()
        if tipo == "rientro":   # 21/10: chiude l'ultima uscita aperta dello stesso allievo
            u = aperte.pop(nome, None)
            if u:
                u["rientro"] = ora
                h1, m1 = map(int, u["ora"].split(":")); h2, m2 = map(int, ora.split(":"))
                u["minuti"] = (h2 * 60 + m2) - (h1 * 60 + m1)
            continue
        u = {"classe": classe, "data": data, "ora": ora, "nome": nome, "tipo": tipo}
        righe.append(u); aperte[nome] = u
    # 21/10/2026 (Nicola): se il rientro non è segnato, valgono 2 minuti (stimati)
    for u in aperte.values():
        u["minuti"] = 2; u["stimati"] = True
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "avanzamento", "uscite.json")
scrivi(out, {"uscite": righe})
print(len(righe), "uscite")
