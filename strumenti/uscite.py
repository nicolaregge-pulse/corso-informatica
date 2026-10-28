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
# 28/10/2026: anche le note del riservato config/<classe>-note-AAAAMMGG.json
# ({"COGNOME NOME": ["HH:MM uscita (bagno)", "HH:MM rientrato", ...]}); un'uscita già nel diario non si conta due volte.
import json
viste = {(u["classe"], u["data"], u["nome"].upper(), u["ora"]) for u in righe}
for f in sorted(glob.glob("/home/user/corso-informatica-riservato/config/*-note-*.json")):
    m = re.match(r"(\w+)-note-(\d{4})(\d{2})(\d{2})\.json$", os.path.basename(f))
    if not m:
        continue
    classe, data = m.group(1).upper(), "%s-%s-%s" % m.group(2, 3, 4)
    try:
        note = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print("salto", f, e); continue
    for nome, voci in note.items():
        nome = nome.strip().upper(); aperta = None
        for v in sorted(voci if isinstance(voci, list) else [voci]):
            mm = re.match(r"\s*(\d{1,2}:\d{2})\s+(.*)", str(v))
            if not mm:
                continue
            ora, testo = mm.group(1), mm.group(2).lower()
            if re.match(r"(rientrat[oa]|rientro)\b", testo):
                if aperta and "rientro" not in aperta:
                    aperta["rientro"] = ora
                    h1, m1 = map(int, aperta["ora"].split(":")); h2, m2 = map(int, ora.split(":"))
                    aperta["minuti"] = (h2 * 60 + m2) - (h1 * 60 + m1); aperta.pop("stimati", None)
                continue
            if re.match(r"(uscit[oa]|bagno)\b", testo):
                if (classe, data, nome, ora) in viste:
                    aperta = None; continue
                aperta = {"classe": classe, "data": data, "ora": ora, "nome": nome,
                          "tipo": "bagno" if "bagno" in testo else "uscita", "minuti": 2, "stimati": True}
                righe.append(aperta); viste.add((classe, data, nome, ora))
righe.sort(key=lambda u: (u["data"], u["ora"]))
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "avanzamento", "uscite.json")
scrivi(out, {"uscite": righe})
print(len(righe), "uscite")
