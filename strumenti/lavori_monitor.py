#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lavori fatti per il monitor dal vivo (20/10/2026, Nicola: «dal cruscotto un link alle cose fatte, per verificarle tutte»).
Legge il CSV del Foglio «Arrivi verifiche» (riservato) e, se c'è, il CSV del quiz Moduli; per ogni allievo tiene
l'ultima verifica e l'ultimo recupero (domande, risposte date, giuste, testi scritti) e il quiz.
Scrive docs/avanzamento/<banca>-lavori.json CIFRATO (nomi e risposte di minori): il monitor lo apre con il codice del docente.
Uso: python3 strumenti/lavori_monitor.py <banca-vN> <arrivi.csv> [quiz.csv]
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cifra_json import scrivi

csv.field_size_limit(10 ** 9)
banca, arrivi = sys.argv[1], sys.argv[2]
quiz = sys.argv[3] if len(sys.argv) > 3 else None
lav = {}
for r in list(csv.reader(open(arrivi, encoding="utf-8")))[1:]:
    try:
        d = json.loads(r[-1])
    except Exception:
        continue
    if d.get("id") != banca or d.get("modo") not in ("verifica", "recupero"):
        continue
    nome = d.get("nome") or d.get("_email") or "?"
    lav.setdefault(nome, {})[d["modo"]] = {
        "quando": d.get("quando"), "minuti": d.get("minuti"), "in_ritardo": d.get("in_ritardo"),
        "crocette": [{"q": c.get("q"), "data": c.get("data"), "giusta": c.get("giusta"), "ok": c.get("ok") is True} for c in d.get("crocette") or []],
        "aperte": [{"q": a.get("q"), "testo": a.get("testo"), "parole": a.get("parole"), "min": a.get("min")} for a in d.get("aperte") or []],
        "antiplagio": d.get("antiplagio")}
if quiz and os.path.exists(quiz):
    for q in csv.DictReader(open(quiz, encoding="utf-8"), delimiter=";"):
        lav.setdefault(q["nome"], {})["quiz"] = {"punteggio": q["punteggio"], "massimo": q["massimo"], "ora": q["ora"]}
out = os.path.join(os.path.dirname(__file__), "..", "docs", "avanzamento", banca + "-lavori.json")
scrivi(out, {"banca": banca, "lavori": lav})
print(len(lav), "allievi ->", os.path.normpath(out))
