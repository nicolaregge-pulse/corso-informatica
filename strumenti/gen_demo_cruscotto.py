#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DEMO del cruscotto dal vivo, SENZA NOMI (19/10/2026), per la comunicazione e l'Atlante.
Prende i dati veri cifrati della lezione (docs/avanzamento/<banca>*), li decifra, sostituisce ogni nome con «Allievo NN»,
toglie indirizzi dei siti (contengono il nome utente), miniature (mostrano il nome) e i nomi dentro i testi; scrive
docs/demo/cruscotto/dati/ in chiaro e la pagina docs/demo/cruscotto/index.html, che si apre senza codice.
Uso: python3 strumenti/gen_demo_cruscotto.py 3inf-portfolio-v1
"""
import sys as _sp, os as _op; _sp.path.append(_op.path.dirname(_op.path.abspath(__file__))); import privacy_pubblico  # noqa: E401,F401 privacy 28/10/2026: nel pubblico i ragazzi solo come «Nome C.»
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cifra_json
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = sys.argv[1]; BANCA = re.sub(r"-v\d+$", "", B); AV = f"{R}/docs/avanzamento"; OUT = f"{R}/docs/demo/cruscotto"; D = f"{OUT}/dati"
os.makedirs(D, exist_ok=True)
A = cifra_json.leggi(f"{AV}/{B}.json"); S = cifra_json.leggi(f"{AV}/{B}-siti.json") or {}
V = cifra_json.leggi(f"{AV}/{B}-voti.json") or {}; SC = cifra_json.leggi(f"{AV}/{B}-schermi.json") or {}
toks = lambda n: set(t.lower() for t in re.split(r"[^\wà-ú']+", n) if len(t) >= 3)
NATO = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Whiskey", "Xray", "Yankee", "Zulu"]
alias, tutti = {}, []
for n in [x["nome"] for x in A["righe"]] + list(S) + list(V.get("voti", {})) + [r["nome"] for r in SC.get("righe", [])]:
    k = next((k for k in alias if toks(k) & toks(n)), None)
    alias[n] = alias[k] if k else NATO[len(set(alias.values()))]
    tutti += list(toks(n))
def pulisci(t):
    t = str(t)
    for w in sorted(set(tutti), key=len, reverse=True):
        t = re.sub(r"\b" + re.escape(w) + r"\b", "…", t, flags=re.I)
    return re.sub(r"https?://\S+", "(indirizzo)", t)
for x in A["righe"]:
    x["nome"] = alias[x["nome"]]; x.pop("inizio", None)   # demo ferma: niente stima dei minuti
    if x.get("aiuto"): x["aiuto"]["domanda"] = pulisci(x["aiuto"]["domanda"])
A["aggiornato"] = "demo"
json.dump(A, open(f"{D}/{B}.json", "w"), ensure_ascii=False)
json.dump({alias[k]: dict(v, url="#", sito="#", comp_ok=v.get("su", 1) > 1) for k, v in S.items()}, open(f"{D}/{B}-siti.json", "w"), ensure_ascii=False)
V["voti"] = {alias[k]: dict(v, conto=pulisci(v["conto"])) for k, v in V.get("voti", {}).items()}
json.dump(V, open(f"{D}/{B}-voti.json", "w"), ensure_ascii=False)
SC["righe"] = [dict(r, nome=alias[r["nome"]], cosa=pulisci(r["cosa"])) for r in SC.get("righe", [])]; SC["sintesi"] = pulisci(SC.get("sintesi", ""))
json.dump(SC, open(f"{D}/{B}-schermi.json", "w"), ensure_ascii=False)
ris = json.load(open(f"{R}/docs/assistente/risposte/verifica-{BANCA}.json"))
json.dump([dict(r, nome=alias.get(r["nome"]) or next((alias[k] for k in alias if toks(k) & toks(r["nome"])), "Anonimo"), domanda=pulisci(r["domanda"]), risposta=pulisci(r["risposta"])) for r in ris], open(f"{D}/risposte.json", "w"), ensure_ascii=False)
st = json.load(open(f"{R}/docs/verifica/stato/{BANCA}.json")); json.dump({"inizio": st.get("inizio"), "scadenza": st.get("scadenza")}, open(f"{D}/stato.json", "w"))
json.dump({"invio": ""}, open(f"{D}/config.json", "w"))
# la pagina: stessa del cruscotto, dati locali, senza codice, senza miniature
h = open(f"{AV}/index.html", encoding="utf-8").read()
h = h.replace("'../avanzamento/thumb/'+B+'/indice.json'", "'dati/nessuna.json'").replace("'../avanzamento/'+B", "'dati/'+B")
h = h.replace("'../verifica/stato/'+B.replace(/-v\\d+$/,'')+'.json?t='", "'dati/stato.json?t='")
h = h.replace("'../assistente/risposte/verifica-'+B.replace(/-v\\d+$/,'')+'.json?t='", "'dati/risposte.json?t='")
h = h.replace("fetch('../verifica/config.json?t='", "fetch('dati/config.json?t='")
h = h.replace("<h1>📖 Monitor dal vivo</h1>", "<h1>📖 Monitor dal vivo · DEMO</h1><p class=\"sub\"><b>Demo senza nomi:</b> la lezione vera della terza del 19/10/2026, con nomi in codice (Alfa, Bravo, Charlie…). Nella versione per il docente qui ci sono i nomi, le miniature dei siti e i link.</p>")
h = h.replace("</body>", "<script>document.getElementById('tok').value='demo';document.getElementById('ok').click();</script></body>")
open(f"{OUT}/index.html", "w", encoding="utf-8").write(h)
print("demo:", len(A["righe"]), "allievi →", OUT)
