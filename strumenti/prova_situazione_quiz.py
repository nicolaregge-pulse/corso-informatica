#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove dell'abbinamento dei nomi della situazione quiz (29/10/2026, audit: la 2INF contava un quiz in meno per ora
rispetto a strumenti/sicurezza_2inf.py per un cognome composto scritto unito nel Modulo).
Legge le funzioni tok/con_attaccati/stesso da generatori/situazione_quiz.py del riservato (senza eseguirlo).
Nomi di prova inventati. Uso: python3 strumenti/prova_situazione_quiz.py   (ultima riga «N/N»)"""
import os, re, sys, unicodedata
F = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                 "corso-informatica-riservato", "generatori", "situazione_quiz.py")
src = open(F, encoding="utf-8").read()
ns = {}
exec("import re, unicodedata\n" + src[src.index("def tok("):src.index("def quando(")], ns)
stesso = ns["stesso"]
ok = tot = 0


def prova(nome, cond):
    global ok, tot
    tot += 1; ok += bool(cond)
    print(("OK   " if cond else "NO   ") + nome)


prova("cognome composto scritto unito nel nome", stesso("DEL MONTE ANNA", "Anna Delmonte"))
prova("cognome composto scritto unito nell'email", stesso("DEL MONTE ANNA", "anna delmmonte", "anna.delmonte@scuola.it"))
prova("nome e cognome normali", stesso("ROSSI LUCA", "Luca Rossi"))
prova("persona diversa con lo stesso nome", not stesso("ROSSI LUCA", "Luca Bianchi"))
prova("solo il nome non basta", not stesso("ROSSI LUCA", "Luca Verdi", "luca.verdi@scuola.it"))
prova("cognome unito di un altro non abbina", not stesso("DEL MONTE ANNA", "Anna Delvalle"))
print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
