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

# 7. controlli del 29/10/2026 pomeriggio (#147-#150, #152)
import subprocess


def git_repo():
    d = tempfile.mkdtemp()
    subprocess.run(["git", "init", "-q", d], check=True)
    return d


def commit(d, msg, quando=None):
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    if quando:
        env["GIT_COMMITTER_DATE"] = env["GIT_AUTHOR_DATE"] = quando
    subprocess.run(["git", "-C", d, "add", "-A"], check=True, env=env)
    subprocess.run(["git", "-C", d, "commit", "-q", "--allow-empty", "-m", msg], check=True, env=env)


# 7.1 #147 formato: un campo tolto è ROSSO, con l'alias no
pubf = git_repo(); os.makedirs(pubf + "/docs/avanzamento")
fq = pubf + "/docs/avanzamento/x-quiz.json"
json.dump({"righe": [{"nome": "a", "o1": 1}]}, open(fq, "w")); commit(pubf, "v1")
json.dump({"righe": [{"nome": "a", "q": [1]}]}, open(fq, "w")); commit(pubf, "v2")
cc.righe.clear()
prova("#147: campo o1 tolto = problema", any("o1" in p for p in cc.controlla_formato_json(pubf, file_=[fq])))
json.dump({"righe": [{"nome": "a", "q": [1], "o1": 1}]}, open(fq, "w")); commit(pubf, "v3")
prova("#147: con l'alias o1 nessun problema", cc.controlla_formato_json(pubf, file_=[fq]) == [])

# 7.2 #148 docente e ragazzi con lo stesso «generato»
pubc, risc = tempfile.mkdtemp(), tempfile.mkdtemp()
os.makedirs(pubc + "/docs/avanzamento"); os.makedirs(pubc + "/docs/x-rag"); os.makedirs(risc + "/config/situazione-quiz")
cfg = risc + "/config/situazione-quiz/x.json"
json.dump({"pubblico": "x-quiz.json", "ragazzi": "x-rag"}, open(cfg, "w"))
json.dump({"generato": "2026-10-29T13:50"}, open(pubc + "/docs/avanzamento/x-quiz.json", "w"))
json.dump({"generato": "2026-10-29T13:55"}, open(pubc + "/docs/x-rag/dati.json", "w"))
prova("#148: docente 13:50, ragazzi 13:55 = problema", len(cc.controlla_coppie_docente_ragazzi(pubc, risc, [cfg])) == 1)
json.dump({"generato": "2026-10-29T13:55"}, open(pubc + "/docs/avanzamento/x-quiz.json", "w"))
prova("#148: stesso generato = nessun problema", cc.controlla_coppie_docente_ragazzi(pubc, risc, [cfg]) == [])

# 7.3 #149 ponte: colonna del giorno senza comando; quiz letti a turno
risp = git_repo(); os.makedirs(risp + "/config/situazione-quiz"); os.makedirs(risp + "/comandi")
cfgp = risp + "/config/situazione-quiz/y.json"
col = {"tipo": "moduli", "corta": "5ª", "dir": "dati/verifiche/q5-20261030"}
json.dump({"colonne": [col], "ponte": []}, open(cfgp, "w"))
prova("#149: quiz del 30/10 senza comando di lettura = problema", len(cc.controlla_ponte_quiz(risp, [cfgp], "2026-10-30")) == 1)
po = [{"comando": "comandi/a.json", "salva_in": "dati/verifiche/q5-20261030"}, {"comando": "comandi/b.json", "salva_in": "dati/verifiche/q4"}]
json.dump({"colonne": [col], "ponte": po}, open(cfgp, "w"))
for nome, quando in (("a", "2026-10-30T13:30:00+01:00"), ("b", "2026-10-30T13:45:00+01:00")):
    json.dump({"stato": "eseguito"}, open(risp + "/comandi/%s.json" % nome, "w")); commit(risp, "Ponte Google: %s.json (eseguito)" % nome, quando)
prova("#149: quiz letti a 15 minuti di distanza = problema", any("a turno" in p for p in cc.controlla_ponte_quiz(risp, [cfgp], "2026-10-30")))
json.dump({"stato": "eseguito", "n": 2}, open(risp + "/comandi/a.json", "w")); commit(risp, "Ponte Google: a.json (eseguito)", "2026-10-30T13:44:00+01:00")
prova("#149: quiz letti insieme = nessun problema", cc.controlla_ponte_quiz(risp, [cfgp], "2026-10-30") == [])

# 7.4 #150 Sicurezza: compito con quiz in coda e ora dopo pronta
G2 = "2026-10-30"
pubs = pub_finto({G2: [{"classe": "2INF", "disciplina": "Sicurezza"}, {"classe": "2INF", "disciplina": "Sicurezza"}]}, {}, None)
riss = tempfile.mkdtemp(); os.makedirs(riss + "/coda"); os.makedirs(pubs + "/docs/verifica/banche")
prova("#150: niente compito in coda = problema", len(cc.controlla_sicurezza_pronta(G2, pubs, riss)) == 1)
json.dump({"quiz": {"domande": []}}, open(riss + "/coda/%s_2INF_sicurezza-5ora.json" % G2, "w"))
prova("#150: 2 ore e la 7ª non pronta = problema", any("7ª" in p for p in cc.controlla_sicurezza_pronta(G2, pubs, riss)))
open(pubs + "/docs/verifica/banche/2inf-sicurezza-7ora.js", "w").write("x")
prova("#150: ora dopo pronta = nessun problema", cc.controlla_sicurezza_pronta(G2, pubs, riss) == [])

# 7.5 #152 la notte finita alle 6:50 non ha girato da sola
risn = tempfile.mkdtemp(); os.makedirs(risn + "/stato")
base_n = {"regole_rilette": [], "classi_preparate": [], "problemi": []}
json.dump(dict(base_n, ora="06:50", controlla_controlli=["non eseguito"]), open(risn + "/stato/notte-%s.json" % G, "w"))
cc.righe.clear()
prova("#152: notte delle 6:50 = frase per il docente", "non ha girato da sola" in cc.controlla_notte(G, risn))
json.dump(dict(base_n, ora="00:40", controlla_controlli=["ESITO: VERDE"]), open(risn + "/stato/notte-%s.json" % G, "w"))
prova("#152: notte delle 0:40 con il controllore = a posto", cc.controlla_notte(G, risn) == "")

print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
