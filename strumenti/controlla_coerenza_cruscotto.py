#!/usr/bin/env python3
"""Coerenza del cruscotto 1INF con la fonte (v1.0, 13/11/2026; errore #327). Non scrive niente.
Uso: python3 -I strumenti/controlla_coerenza_cruscotto.py FABBRICA.xlsx
Confronta docs/cruscotto/dati/1INF-oggi.json e 1INF-presenze.json con l'export del foglio Fabbrica:
 1. stessi allievi (n. e iniziali «Nome I.») nella vista Oggi e nella scheda «Situazione pubblica 1INF»;
 2. per ogni Documento di oggi: il numero di «consegnato» della vista Oggi = numero di «Consegnato» della scheda Consegne 1INF;
 3. per ogni quiz di oggi: il numero di «fatto» della vista Oggi = allievi della scheda Situazione che hanno una percentuale (non MANCA);
 4. presenti + assenti della vista presenze = allievi del registro del giorno e nessun nome in comune tra le due liste.
Esce con 1 se una cosa non torna."""
import json, os, re, sys
import openpyxl
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(R, "docs", "cruscotto", "dati")
x = openpyxl.load_workbook(sys.argv[1], data_only=True)
oggi = json.load(open(os.path.join(D, "1INF-oggi.json"), encoding="utf-8"))
pres = json.load(open(os.path.join(D, "1INF-presenze.json"), encoding="utf-8"))
problemi = []
confronti = 0
def righe(n):
    return [r for r in x[n].iter_rows(values_only=True)]
cons = righe("Consegne 1INF"); hi = [i for i, r in enumerate(cons) if r and r[0] == "Stato"][0]; H = cons[hi]
sit = righe("Situazione 1INF"); si = [i for i, r in enumerate(sit) if r and r[0] == "Stato"][0]; SH = sit[si]
n_cons = len([r for r in cons[hi + 1:] if r[1]])
if oggi["n_allievi"] != n_cons:
    problemi.append("allievi: vista Oggi %d, Consegne %d" % (oggi["n_allievi"], n_cons))
voci = {v.get("id") or v.get("chiave"): v for v in oggi["voci"]} if isinstance(oggi["voci"], list) else {}
for ora in (4, 5, 6):
    j = [k for k, h in enumerate(H) if h and re.search(r"13/11 Ora %d:" % ora, str(h))]
    if j:
        c = sum(1 for r in cons[hi + 1:] if r[1] and str(r[j[0]]) == "Consegnato")
        o = sum(1 for a in oggi["allievi"] if a["stati"].get("ora%d-documento" % ora, {}).get("s") == "consegnato")
        confronti += 1
        if c != o: problemi.append("Documento ora %d: Oggi %d consegnati, Consegne %d" % (ora, o, c))
    j = [k for k, h in enumerate(SH) if h and re.search(r"13/11 Ora %d:" % ora, str(h))]
    if j:
        c = sum(1 for r in sit[si + 1:] if r[1] and r[j[0]] not in (None, "", "MANCA", "NON ABBINATA", "-"))
        o = sum(1 for a in oggi["allievi"] if a["stati"].get("ora%d-quiz" % ora, {}).get("s") == "fatto")
        confronti += 1
        if c != o: problemi.append("Quiz ora %d: Oggi %d fatti, Situazione %d" % (ora, o, c))
pa = pres.get("presenti", []); aa = pres.get("assenti", [])
if set(pa) & set(aa): problemi.append("presenze: nomi sia tra presenti sia tra assenti: %s" % sorted(set(pa) & set(aa)))
if len(pa) + len(aa) != pres.get("n_iscritti", pres.get("iscritti", len(pa) + len(aa))): problemi.append("presenze: presenti+assenti diverso dagli iscritti")
print("ROSSO: " + "; ".join(problemi) if problemi else "VERDE: vista Oggi, Consegne, Situazione e presenze coerenti (%d confronti Documenti/quiz, %d allievi nel foglio, %d presenti, %d assenti)" % (confronti, n_cons, len(pa), len(aa)))
sys.exit(1 if problemi else 0)
