#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla che le domande APERTE di un quiz non chiedano ciò che la dispensa dà solo in un passo «facoltativo».

Versione 1.0 (12/11/2026). Nasce dall'errore #316: il quiz 1INF ora 6 chiedeva, alla domanda 12, «processore e RAM del
TUO PC», ma la dispensa dava il comando `msinfo32` in un passo «facoltativo»: 10 allievi su 21 a zero.
Uso:   python3 strumenti/controlla_quiz_dispensa.py fabbrica/<quiz>.txt <dispensa>.md [altra_dispensa.md ...]
Esito: 0 = nessun avviso; 1 = almeno un avviso (stampato). Non blocca niente da solo: va lanciato prima di dire che
       il quiz è pronto (CHECKLIST-LEZIONE). Legge solo il testo italiano (prima riga di ogni domanda).
Come funziona: per ogni domanda aperta (tipo paragrafo o testo) prende le parole significative della domanda; per ogni
blocco «facoltativo» della dispensa (un titolo o una riga con la parola «facoltativ», con le righe che seguono fino al
titolo dopo) conta quante parole significative ha in comune; con 3 o più parole in comune (o 2 se la domanda chiede un
dato del proprio PC: «del TUO PC») e un'azione nel blocco (comando tra apici inversi, «premi», «apri», «scrivi»)
segnala la domanda.
Limite: euristica, può dare falsi avvisi (si leggono a mano) e non vede i blocchi senza la parola «facoltativ».
"""
import base64
import json
import re
import sys

STOP = set("""scrivi scrivere cosa vedi vederli vedere riesci riescono tuo tua tuoi tue del della dei delle con che per come sono
fai fare esempio parole tue tra una uno gli loro anche solo dici dire prima dopo sul sulla nel nella alla alle degli
non quale quali dove quando perche questo questa quello quella fatto passo solo guarda guardare""".split())
AZIONE = re.compile(r"`[^`]+`|\bpremi\b|\bapri\b|\bscrivi\b|\bclicca\b", re.I)
PERSONALE = re.compile(r"\b(?:del|nel|sul|dal|il|al)\s+tuo\b|\bTUO\b|\bTUA\b|\bTUOI\b", re.I)


def parole(testo):
    return {w for w in re.findall(r"[a-zà-ù0-9]{3,}", testo.lower()) if w not in STOP}


def carica_quiz(path):
    raw = open(path, encoding="utf-8").read().strip()
    try:
        return json.loads(base64.b64decode(raw).decode("utf-8"))
    except Exception:
        return json.loads(raw)


def blocchi_facoltativi(md):
    righe = md.split("\n")
    out, i = [], 0
    while i < len(righe):
        r = righe[i]
        if re.search(r"facoltativ", r, re.I):
            if r.lstrip().startswith("#"):
                liv = len(r) - len(r.lstrip("#"))
                j = i + 1
                while j < len(righe) and not (righe[j].startswith("#") and (len(righe[j]) - len(righe[j].lstrip("#"))) <= liv):
                    j += 1
            else:
                j = i + 1
                while j < len(righe) and (righe[j].startswith((" ", "\t")) or not righe[j].strip() and j + 1 < len(righe) and righe[j + 1].startswith((" ", "\t"))):
                    j += 1
            out.append((i + 1, "\n".join(righe[i:j])))
            i = j
        else:
            i += 1
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    quiz = carica_quiz(sys.argv[1])
    avvisi = []
    blocchi = []
    for d in sys.argv[2:]:
        for riga, testo in blocchi_facoltativi(open(d, encoding="utf-8").read()):
            blocchi.append((d, riga, testo))
    for n, dom in enumerate(quiz.get("domande", []), 1):
        if dom.get("tipo") not in ("paragrafo", "testo"):
            continue
        it = (dom.get("t") or "").split("\n")[0]
        pq = parole(it)
        for d, riga, testo in blocchi:
            comuni = pq & parole(testo)
            if AZIONE.search(testo) and (len(comuni) >= 3 or (len(comuni) >= 2 and PERSONALE.search(it))):
                avvisi.append("domanda %d (aperta): «%s» chiede cose (%s) che %s dà nel passo facoltativo alla riga %d" % (
                    n, it[:70], ", ".join(sorted(comuni)), d.split("/")[-1], riga))
    if avvisi:
        print("AVVISO (#316): una domanda aperta dipende da un passo facoltativo. O il passo diventa obbligatorio nella dispensa, o la domanda si toglie/riscrive.")
        for a in avvisi:
            print("-", a)
        return 1
    print("nessun avviso: le domande aperte non dipendono da passi facoltativi (controllo euristico)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
