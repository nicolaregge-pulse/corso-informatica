# -*- coding: utf-8 -*-
"""Gioco della talpa 1INF: dà il nome vero a «Personaggio N» (elenco, versioni, backlog).
Uso: python3 strumenti/talpa_nome.py 5 "Muhammad N." """
import sys as _sp, os as _op; _sp.path.append(_op.path.dirname(_op.path.abspath(__file__))); import privacy_pubblico  # noqa: E401,F401 privacy 28/10/2026: nel pubblico i ragazzi solo come «Nome C.»
import json, os, re, sys, unicodedata
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n, nome = sys.argv[1], sys.argv[2]
def slug(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn"); return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
for f in ["docs/giochi/talpa-1inf/talpe/elenco.json", "docs/giochi/talpa-1inf/versioni/versioni.json", "docs/1inf-backlog/backlog.json"]:
    p = os.path.join(QUI, f); t = open(p, encoding="utf-8").read()
    t = t.replace(f"personaggio-personaggio-{n}", f"personaggio-{slug(nome)}")
    t = re.sub(rf"Personaggio {n}(?!\d)", nome, t)
    d = json.loads(t)
    def pulisci(x):
        if isinstance(x, dict):
            if nome in json.dumps(x, ensure_ascii=False) and ("chi" in x or "autore" in x or "alunno" in x):
                return json.loads(json.dumps(x, ensure_ascii=False).replace(" (nome in arrivo)", ""))
            return {k: pulisci(v) for k, v in x.items()}
        if isinstance(x, list): return [pulisci(v) for v in x]
        return x
    json.dump(pulisci(d), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("Personaggio", n, "->", nome)
