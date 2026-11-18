# -*- coding: utf-8 -*-
"""Pagina del docente docs/3inf/verifica-trasferimento/index.html (18/11/2026).
Legge gli elenchi dal RISERVATO (config/3inf-github.json, 3inf-pc-github.json) e li cifra nel file pubblico
(AES-GCM/PBKDF2 di cifra_json.py): nel pubblico non resta nessun cognome né utente in chiaro.
Uso: python3 strumenti/genera_verifica_trasferimento_3inf.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cifra_json import cifra
RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIS = "/home/user/corso-informatica-riservato/config/"

def dati():
    g = json.load(open(RIS + "3inf-github.json", encoding="utf-8"))["allievi"]
    pc = json.load(open(RIS + "3inf-pc-github.json", encoding="utf-8"))["pc"]
    al = []
    for r in g:
        nome, p, login, repo = r[0], r[1], r[2], r[3]
        cogn = " ".join(t for t in nome.split() if t.isupper())
        us = [login.lower()] if login and login != "-" else []
        al.append({"n": nome, "pc": p, "u": us, "r": [repo.lower()] if repo else [], "c": cogn.lower().replace(" ", "-")})
    noti = {u for a in al for u in a["u"]}
    for n, login in pc.items():   # login della mappa PC che non sta nell'altro elenco
        if login.lower() in noti: continue
        cand = [a for a in al if str(a["pc"]) == n]
        if len(cand) == 1: cand[0]["u"].append(login.lower()); noti.add(login.lower())
    for a in al: del a["pc"]
    return {"allievi": al}

if __name__ == "__main__":
    modello = open(os.path.join(RADICE, "strumenti/verifica-trasferimento-3inf-modello.html"), encoding="utf-8").read()
    h = modello.replace("__BLOB__", json.dumps(cifra(dati())))
    dest = os.path.join(RADICE, "docs/3inf/verifica-trasferimento/index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(h)
    print(dest, len(h), "byte")
