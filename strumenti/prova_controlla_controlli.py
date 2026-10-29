#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove del controllo «lavoro del giorno» e della notte di oggi in controlla_controlli.py (29/10/2026, REGISTRO-ERRORI #139).
Uso: python3 strumenti/prova_controlla_controlli.py   (ultima riga «N/N»)"""
import datetime, importlib.util, json, os, sys, tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cc", os.path.join(QUI, "controlla_controlli.py"))
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
ok = tot = 0


def prova(nome, cond):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(("OK   " if cond else "NO   ") + nome)


def pub_finto(orario, piani, proposte_oggi):
    d = tempfile.mkdtemp()
    os.makedirs(d + "/docs/avanzamento"); os.makedirs(d + "/docs/cruscotto/piano")
    json.dump({"lezioni": orario}, open(d + "/docs/avanzamento/orario-lezioni.json", "w"))
    for nome, n in piani.items():
        json.dump({"proposte": [{"n": i + 1} for i in range(n)]}, open(d + "/docs/cruscotto/piano/" + nome, "w"))
    if proposte_oggi is not None:
        open(d + "/PROPOSTE-OGGI.md", "w").write(proposte_oggi)
    return d


def esegui(giorno, pub):
    cc.righe.clear()
    frase = cc.controlla_lavoro_del_giorno(giorno, pub)
    return frase, list(cc.righe)


G = "2026-10-29"
ORARIO = {G: [{"classe": "2INF", "disciplina": "Laboratorio professionale"},
              {"classe": "3INF", "disciplina": "Laboratorio professionale"},
              {"classe": "1INF", "disciplina": "Sicurezza professionale"}]}

# 1. piano presente
pub = pub_finto(ORARIO, {"2inf-%s.json" % G: 3, "3inf-%s.json" % G: 4, "1inf-%s.json" % G: 1}, "# Proposte di oggi, 29/10/2026\n")
frase, r = esegui(G, pub)
prova("piano presente: VERDE", r and r[-1][0] == "VERDE" and frase == "")

# 2. piano mancante
pub = pub_finto(ORARIO, {"1inf-%s.json" % G: 1}, None)
frase, r = esegui(G, pub)
prova("piano mancante: ROSSO", r and r[-1][0] == "ROSSO")
prova("piano mancante: nomina 2INF e 3INF", "Mancano le proposte di oggi per 2INF, 3INF" in frase)
prova("piano mancante: PROPOSTE-OGGI.md segnalato", "PROPOSTE-OGGI.md" in frase)

# 3. poche proposte e PROPOSTE-OGGI.md di ieri
pub = pub_finto(ORARIO, {"2inf-%s.json" % G: 1, "3inf-%s.json" % G: 3, "1inf-%s.json" % G: 1}, "# Proposte del 28/10/2026\n")
frase, r = esegui(G, pub)
prova("una proposta per un laboratorio: ROSSO", r[-1][0] == "ROSSO" and "2INF (1 su 3)" in frase)
prova("PROPOSTE-OGGI.md con la data vecchia: segnalato", "non ha la data di oggi" in frase)

# 4. giorno senza lezioni (sabato, e un feriale coperto dall'orario senza ore)
pub = pub_finto(ORARIO, {}, None)
frase, r = esegui("2026-10-31", pub)
prova("sabato: VERDE oggi niente lezioni", r[-1][0] == "VERDE" and "niente lezioni" in r[-1][1] and frase == "")
pub = pub_finto(dict(ORARIO, **{"2026-11-03": []}), {}, None)
frase, r = esegui("2026-11-02", pub)
prova("feriale senza ore nell'orario: VERDE", r[-1][0] == "VERDE")

# 5. notte di oggi in ora di Roma: alle 6:20 del 29 si controlla il 29, non il 28
adesso = datetime.datetime(2026, 10, 29, 6, 20, tzinfo=cc.ROMA)
prova("notte attesa alle 6:20 del 29/10 = 2026-10-29", cc.notte_attesa(adesso) == G)
utc = datetime.datetime(2026, 10, 28, 23, 30, tzinfo=datetime.timezone.utc)   # 0:30 a Roma
prova("23:30 UTC del 28 = notte del 29 a Roma", cc.notte_attesa(utc) == G)

# 6. notte mancante = frase per il docente; prima riga dell'esito con DA SAPERE SUBITO
ris = tempfile.mkdtemp()
cc.righe.clear()
f = cc.controlla_notte(G, ris)
prova("notte mancante: ROSSO e frase", cc.righe[-1][0] == "ROSSO" and "non risulta finita" in f)
import io, contextlib
out = io.StringIO()
with contextlib.redirect_stdout(out):
    cc.stampa([f, "Mancano le proposte di oggi per 2INF"])
prima = out.getvalue().splitlines()[0]
prova("prima riga: ESITO con DA SAPERE SUBITO", prima.startswith("ESITO: ROSSO") and "DA SAPERE SUBITO" in prima and "2INF" in prima)

print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
