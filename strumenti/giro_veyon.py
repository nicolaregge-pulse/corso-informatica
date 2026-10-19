#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Giro Veyon → monitor della classe + cruscotto del docente (19/10/2026).
Da uno screenshot di Veyon l'assistente scrive un file JSON con le righe
  [{"pc":"PC 21","nome":"NOME COGNOME","cosa":"Google vuoto","fuori":true}, ...]
e questo script lo mette in DUE posti:
  1. docs/<classe>-monitor/monitor.json  (pubblico: nome abbreviato «Nome C.»)
  2. docs/avanzamento/<banca>-schermi.json (cruscotto del docente: ultimo giro, nome intero come nel Foglio)
Uso: python3 strumenti/giro_veyon.py <classe es. 3inf> <banca es. 3inf-portfolio-v1> <ora HH:MM> <righe.json> [sintesi]
"""
import cifra_json, json, sys, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
classe, banca, ora, frighe = sys.argv[1:5]
sintesi = sys.argv[5] if len(sys.argv) > 5 else ""
righe = json.load(open(frighe, encoding="utf-8"))


def abbrevia(n):
    t = n.split()
    return t[0].capitalize() + (" " + t[-1][0].upper() + "." if len(t) > 1 else "")


fuori = [r for r in righe if r.get("fuori")]
if not sintesi:
    sintesi = f"{len(righe)} PC accesi: {len(righe) - len(fuori)} lavorano, {len(fuori)} fuori" + (
        " (" + ", ".join(r["pc"] for r in fuori) + ")." if fuori else ".")

pm = f"{R}/docs/{classe}-monitor/monitor.json"
d = json.load(open(pm, encoding="utf-8"))
d["giri"].append({"ora": ora, "righe": [{"pc": r["pc"], "alunno": abbrevia(r["nome"]), "cosa": r["cosa"], "fuori": bool(r.get("fuori"))} for r in righe], "sintesi": sintesi})
json.dump(d, open(pm, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ps = f"{R}/docs/avanzamento/{banca}-schermi.json"
cifra_json.scrivi(ps, {"ora": ora, "sintesi": sintesi, "righe": righe})   # nomi interi: cifrato
print(f"giro {ora}: {sintesi}")
