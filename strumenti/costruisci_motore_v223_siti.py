#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""costruisci_motore_v223_siti.py v1.0 (16/11/2026): costruisce fabbrica/correzioni/motore-v2.23-siti.js dal motore v2.22.3 + strumenti/controlla_siti_live.gs.
NON attiva nulla e NON tocca fabbrica/motore.js (errore #335: l'attivazione e un gesto del docente, «via»). Nessun nome di allievo.
Cambia rispetto alla v2.22.3 SOLO: intestazione e changelog, numero di versione, il blocco SITI_* (copiato dal .gs) prima di FB_main_, e il passo
passo('siti', ...) dopo 'ripara' (budget proprio di 60 s; se la scheda 'Siti da controllare' e vuota costa solo una lettura).
Uso: python3 strumenti/costruisci_motore_v223_siti.py   (dalla radice del repository pubblico)"""
import os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = open(os.path.join(R, "fabbrica/correzioni/motore-v2.22.3.js"), encoding="utf-8").read()
gs = open(os.path.join(R, "strumenti/controlla_siti_live.gs"), encoding="utf-8").read()


def una_volta(testo, cosa, nuovo):
    n = testo.count(cosa)
    if n != 1:
        sys.exit("ancora non trovato esattamente una volta (%d): %r" % (n, cosa[:60]))
    return testo.replace(cosa, nuovo)


s = una_volta(base, " * FABBRICA - MOTORE v2.22.3 (15/11/2026)", " * FABBRICA - MOTORE v2.23-siti (16/11/2026)")
s = una_volta(s, " * Changelog: 2.22.3 (15/11/2026,",
              " * Changelog: 2.23-siti (16/11/2026, base 2.22.3, NON ATTIVATO: serve il «via» del docente; nessun permesso nuovo: UrlFetchApp c'e gia): passo nuovo 'siti' (FB_siti_) che legge la scheda 'Siti da controllare' (COGNOME, URL sito, URL repository), la completa dai Documenti e da 'Utenti <CLASSE>', apre ogni sito DALLA RETE DI GOOGLE (github.io dal sandbox non si raggiunge), e scrive la scheda 'Siti' (HTTP, <title>, numero di <img>, per ogni <img> codice HEAD/GET dell'URL assoluto, esito, ora) e la riga 'Siti' in 'Stato'; budget 60 s per giro, stesso limite FB_MAX_GIRO_ (270 s) della 2.22.3, i siti non fatti restano in coda e si riprendono dai piu vecchi. Le schede 'Siti da controllare' e 'Siti' sono solo docente (COGNOME): mai da pubblicare. Tutto il resto e identico alla 2.22.3. 2.22.3 (15/11/2026,")
assert s.count("['Motore', '2.22.3']") == 2     # FB_stato_ e la scrittura a inizio giro di FB_main_
s = s.replace("['Motore', '2.22.3']", "['Motore', '2.23-siti']")
blocco = "/* ---------- v2.23-siti: controllo dei siti dei ragazzi dalla rete di Google (copiato da strumenti/controlla_siti_live.gs) ---------- */\n" + gs.rstrip("\n") + "\n\n"
s = una_volta(s, "function FB_main_() {", blocco + "function FB_main_() {")
s = una_volta(s, "    passo('ripara', function () { FB_ripara_(ss); });\n",
              "    passo('ripara', function () { FB_ripara_(ss); });\n    passo('siti', function () { FB_siti_(ss, t0); });\n")
out = os.path.join(R, "fabbrica/correzioni/motore-v2.23-siti.js")
open(out, "w", encoding="utf-8").write(s)
print("scritto", out, len(s), "byte")
