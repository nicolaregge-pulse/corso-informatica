#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""docente_live.py v1.0 (20/11/2026) - scrive docs/live/docente-<classe>.json CIFRATO (stesso formato di strumenti/cifra_json.py, R1.2).
Contenuto (in chiaro SOLO nel riservato): mappa «Nome I.» -> COGNOME Nome, note con ora h N, link agli screenshot (https), motivi del voto.
La pagina docs/live/ lo decifra nel browser con il codice del docente; senza codice mostra solo la parte pubblica. NON e' in tempo reale:
la pagina scrive l'ora di aggiornamento di questo file ("aggiornato").
Uso:
  python3 strumenti/docente_live.py 1INF                 # parte dall'ultimo cruscotto docente del riservato (cruscotti/cruscotto-<CLASSE>-*.html)
  python3 strumenti/docente_live.py 1INF --da-file F.json  # oppure da un JSON in chiaro del riservato con la stessa forma (vedi sotto)
Forma del JSON in chiaro: {"aggiornato": ISO, "giorno": "AAAA-MM-GG", "nomi": {"Nome I.": "COGNOME Nome"},
  "note": {"Nome I.": [{"ora": 4, "testo": "...", "quando": "HH:MM"}]}, "screenshot": {"Nome I.": [{"ora": 4, "testo": "", "link": "https://..."}]},
  "motivi": {"Nome I.": "testo"}}
Il JSON in chiaro (con i cognomi) si salva SOLO nel riservato: cruscotti/docente-live-<CLASSE>.json. Nel pubblico va solo il file cifrato.
"""
import argparse, glob, json, os, re, sys
from datetime import datetime, timedelta, timezone

RIS = "/home/user/corso-informatica-riservato"
PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cifra_json import scrivi  # noqa: E402


def da_cruscotto(classe):
    files = sorted(glob.glob(os.path.join(RIS, "cruscotti", "cruscotto-%s-*.html" % classe)))
    if not files:
        sys.exit("nessun cruscotto docente per %s nel riservato" % classe)
    t = open(files[-1], encoding="utf-8").read()
    d = json.loads(re.search(r'<script id="dati"[^>]*>(.*?)</script>', t, re.S).group(1))
    nomi, note = {}, {}
    for p in d["presenti"] + d["assenti"]:
        q = p.get("docente") or {}
        if q.get("cognome_nome"):
            nomi[p["nome"]] = q["cognome_nome"]
        nn = [{"ora": 0, "testo": n.get("testo", ""), "quando": n.get("data", "")} for n in (q.get("note") or [])[-5:]]
        if nn:
            note[p["nome"]] = nn
    roma = timezone(timedelta(hours=1))
    return {"aggiornato": datetime.now(roma).strftime("%Y-%m-%dT%H:%M:%S+01:00"), "giorno": d["lezione"]["giorno"], "nomi": nomi, "note": note,
            "screenshot": {}, "motivi": {}, "fonte": os.path.relpath(files[-1], RIS)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classe")
    ap.add_argument("--da-file")
    a = ap.parse_args()
    classe = a.classe.upper()
    obj = json.load(open(a.da_file, encoding="utf-8")) if a.da_file else da_cruscotto(classe)
    chiaro = os.path.join(RIS, "cruscotti", "docente-live-%s.json" % classe)
    json.dump(obj, open(chiaro, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    out = os.path.join(PUB, "docs", "live", "docente-%s.json" % classe.lower())
    scrivi(out, obj)
    print("scritto", os.path.relpath(out, PUB), "(cifrato);", len(obj["nomi"]), "nomi; in chiaro solo nel riservato:", os.path.relpath(chiaro, RIS))


if __name__ == "__main__":
    main()
