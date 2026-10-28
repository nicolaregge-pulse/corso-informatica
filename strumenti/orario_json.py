#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Orario delle lezioni in JSON per le pagine del sito (28/10/2026, richiesta del docente).

Legge tutte le tabelle orario/settimana-AAAA-MM-GG.md (righe «| Mer 28/10 | 08-11 (3 h) | 1INF | Disciplina |»)
e scrive docs/avanzamento/orario-lezioni.json: per ogni giorno l'elenco delle ore di ogni classe.
Lo usano:
  1. il cruscotto unico (docs/cruscotto/), per il link al giorno di lezione successivo nella linguetta «Piano del giorno»;
  2. le pagine di monitoraggio (docs/avanzamento/orario-lezione.js), per mostrare l'allarme «il dato ha N minuti»
     solo durante la lezione della classe e fino a 15 minuti dopo.
Niente nomi di allievi: solo giorni, ore, classi e discipline.
Uso (una riga, dalla cartella del repository pubblico):
    python3 strumenti/orario_json.py
Va rilanciato ogni volta che si aggiunge o si cambia un file orario/settimana-*.md (passi notturni).
"""
import glob, json, os, re, sys

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PUB, "docs", "avanzamento", "orario-lezioni.json")
RIGA = re.compile(r"^\|\s*\w{3}\s+(\d{1,2})/(\d{1,2})\s*\|\s*(\d{1,2})(?::(\d\d))?\s*-\s*(\d{1,2})(?::(\d\d))?[^|]*\|\s*([0-9][A-Z]+)\s*\|\s*([^|]*)\|")


def main():
    lezioni = {}
    fonti = []
    for f in sorted(glob.glob(os.path.join(PUB, "orario", "settimana-*.md"))):
        m = re.search(r"settimana-(\d{4})-(\d\d)-(\d\d)\.md$", f)
        if not m:
            continue
        anno, mese_inizio = int(m.group(1)), int(m.group(2))
        n = 0
        for riga in open(f, encoding="utf-8"):
            r = RIGA.match(riga.strip())
            if not r:
                continue
            g, mese = int(r.group(1)), int(r.group(2))
            a = anno + (1 if mese < mese_inizio else 0)   # settimana a cavallo di dicembre e gennaio
            giorno = "%04d-%02d-%02d" % (a, mese, g)
            voce = {"classe": r.group(7), "da": "%02d:%s" % (int(r.group(3)), r.group(4) or "00"),
                    "a": "%02d:%s" % (int(r.group(5)), r.group(6) or "00"), "disciplina": r.group(8).strip()}
            elenco = lezioni.setdefault(giorno, [])
            if voce not in elenco:
                elenco.append(voce)
                n += 1
        fonti.append("%s (%d ore)" % (os.path.relpath(f, PUB), n))
    for g in lezioni:
        lezioni[g].sort(key=lambda v: (v["da"], v["classe"]))
    dati = {"fonte": fonti, "lezioni": dict(sorted(lezioni.items()))}
    vecchio = None
    try:
        vecchio = json.load(open(OUT, encoding="utf-8"))
    except Exception:
        pass
    if vecchio != dati:
        with open(OUT, "w", encoding="utf-8") as fh:
            json.dump(dati, fh, ensure_ascii=False, indent=1)
    print("orario-lezioni.json: %d giorni da %d settimane" % (len(lezioni), len(fonti)))
    return 0 if lezioni else 1


if __name__ == "__main__":
    sys.exit(main())
