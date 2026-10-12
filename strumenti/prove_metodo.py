# -*- coding: utf-8 -*-
"""Raccolta delle prove che il metodo funziona, lezione per lezione.

Legge i dati pubblici di una lezione (voti, backlog, monitor) e scrive:
1. nel repository RISERVATO, prove-metodo/<id>.json e <id>.md, con nome e iniziale;
2. nel repository pubblico, la parte della lezione dentro PROVE-METODO.md, SENZA nomi (Allievo NN).

Uso:  python3 strumenti/prove_metodo.py 20261012_2INF 2inf 13:22
      (id della lezione, prefisso delle pagine in docs/, ora in cui i voti sono diventati pubblici)
"""
import collections, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
RIS = os.path.join(os.path.dirname(ROOT), "corso-informatica-riservato", "prove-metodo")


def minuti(ora):
    h, m = ora.strip()[-5:].split(":")
    return int(h) * 60 + int(m)


def calcola(pref, ora_voti):
    voti = json.load(open(os.path.join(DOCS, pref + "-voti/voti.json"), encoding="utf-8"))["voti"]
    back = json.load(open(os.path.join(DOCS, pref + "-backlog/backlog.json"), encoding="utf-8"))["voci"]
    giri = json.load(open(os.path.join(DOCS, pref + "-monitor/monitor.json"), encoding="utf-8"))["giri"]
    tv = minuti(ora_voti)
    quarti = collections.Counter()
    for x in back:
        t = minuti(x["ora"])
        quarti["%02d:%02d" % (t // 60, t // 15 % 4 * 15)] += 1
    allievi = []
    for x in voti:
        ore = [minuti(e["ora"]) for e in x.get("elenco", [])]
        prima = sum(1 for t in ore if t < tv)
        bene = re.search(r"(\d+) scritte bene", x.get("perche", ""))
        allievi.append({"alunno": x["alunno"], "pr": x["pr"], "fatte": x["fatte"], "voto": x["voto"], "feedback": x["feedback"],
                        "prima": prima, "dopo": len(ore) - prima, "bene": int(bene.group(1)) if bene else 0})
    osservazioni = sum(len(g["righe"]) for g in giri)
    fuori = sum(1 for g in giri for r in g["righe"] if r.get("fuori"))
    pesi = collections.Counter(x.get("peso") for x in back if x.get("peso"))
    versioni = sorted({x["fatto"].split()[0] for x in back if x.get("fatto", "").startswith("v")})
    return {
        "presenti": len(allievi),
        "con_pr": sum(1 for a in allievi if a["pr"] > 0),
        "feedback": sum(1 for a in allievi if a["feedback"]),
        "pr": len(back),
        "nel_gioco": sum(1 for x in back if x.get("fatto")),
        "rifiutate": sum(1 for x in back if x.get("no")),
        "versioni": len(versioni),
        "scritte_bene": sum(a["bene"] for a in allievi),
        "quarti": dict(sorted(quarti.items())),
        "ora_voti": ora_voti,
        "pr_prima_voti": sum(a["prima"] for a in allievi),
        "pr_dopo_voti": sum(a["dopo"] for a in allievi),
        "minuti_prima": tv - min(minuti(x["ora"]) for x in back),
        "minuti_dopo": max(minuti(x["ora"]) for x in back) - tv,
        "recuperi": [a for a in allievi if a["prima"] < 5 and a["prima"] + a["dopo"] >= 5 and a["dopo"] > 0],
        "osservazioni": osservazioni,
        "fuori": fuori,
        "giri": len(giri),
        "pesi": dict(sorted(pesi.items())),
        "allievi": allievi,
    }


def quante(n):
    return "1 richiesta" if n == 1 else "%d richieste" % n


def testo(lid, d, nome):
    r = ["## %s" % lid, "",
         "| Indicatore | Valore |", "|---|---|",
         "| Presenti | %d |" % d["presenti"],
         "| Hanno mandato almeno una Pull Request (PR) | %d su %d |" % (d["con_pr"], d["presenti"]),
         "| Hanno mandato il Feedback sulla teoria | %d su %d |" % (d["feedback"], d["presenti"]),
         "| PR ricevute | %d |" % d["pr"],
         "| PR entrate nel gioco | %d |" % d["nel_gioco"],
         "| PR rifiutate con il motivo | %d |" % d["rifiutate"],
         "| Versioni nuove del gioco nate dalle PR | %d |" % d["versioni"],
         "| PR scritte bene con le quattro parti | %d |" % d["scritte_bene"],
         "| Schermi sul compito durante i giri del docente | %d su %d (%d%%) |" % (
             d["osservazioni"] - d["fuori"], d["osservazioni"], round(100 * (d["osservazioni"] - d["fuori"]) / max(1, d["osservazioni"]))),
         "", "**PR ricevute ogni quarto d'ora:** " + ", ".join("%s %d" % kv for kv in d["quarti"].items()) + ".", "",
         "**Prima e dopo i voti pubblici (ore %s), tutte le richieste inviate:** %d in %d minuti prima (%.1f al minuto), %d in %d minuti dopo (%.1f al minuto). Il ritmo della classe nel complesso cala verso la fine della lezione; l'effetto dei voti pubblici si vede su chi era indietro (qui sotto)." % (
             d["ora_voti"], d["pr_prima_voti"], d["minuti_prima"], d["pr_prima_voti"] / max(1, d["minuti_prima"]),
             d["pr_dopo_voti"], d["minuti_dopo"], d["pr_dopo_voti"] / max(1, d["minuti_dopo"])), ""]
    if d["recuperi"]:
        r += ["**Recuperi dopo i voti pubblici** (sotto le 5 PR prima delle %s, almeno 5 alla fine):" % d["ora_voti"], ""]
        for i, a in enumerate(d["recuperi"]):
            r.append("%d. %s: %s prima, %s dopo; voto finale %d." % (i + 1, nome(a["alunno"]), quante(a["prima"]), quante(a["dopo"]), a["voto"]))
        r.append("")
    return r


def main():
    lid, pref, ora_voti = sys.argv[1], sys.argv[2], sys.argv[3]
    d = calcola(pref, ora_voti)
    os.makedirs(RIS, exist_ok=True)
    json.dump(d, open(os.path.join(RIS, lid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    righe = testo(lid, d, lambda n: n)
    righe += ["**Tutti gli allievi**", "", "| Allievo | PR valide | nel gioco | richieste prima delle %s | dopo | scritte bene | Feedback | voto |" % ora_voti, "|---|---|---|---|---|---|---|---|"]
    righe += ["| %s | %d | %d | %d | %d | %d | %s | %d |" % (a["alunno"], a["pr"], a["fatte"], a["prima"], a["dopo"], a["bene"], "sì" if a["feedback"] else "no", a["voto"]) for a in d["allievi"]]
    open(os.path.join(RIS, lid + ".md"), "w", encoding="utf-8").write("# Prove del metodo — %s (RISERVATO, con i nomi)\n\n" % lid + "\n".join(righe) + "\n")
    anon = {a["alunno"]: "Allievo %02d" % (i + 1) for i, a in enumerate(d["allievi"])}
    pub = os.path.join(ROOT, "PROVE-METODO.md")
    s = open(pub, encoding="utf-8").read() if os.path.exists(pub) else ""
    blocco = "<!-- %s -->\n" % lid + "\n".join(testo(lid, d, lambda n: anon.get(n, "Allievo"))) + "<!-- fine %s -->\n" % lid
    if "<!-- %s -->" % lid in s:
        s = re.sub(r"<!-- %s -->.*?<!-- fine %s -->\n" % (lid, lid), lambda _: blocco, s, flags=re.S)
    else:
        s = s.replace("## 99 Registro delle versioni", blocco + "\n## 99 Registro delle versioni")
    open(pub, "w", encoding="utf-8").write(s)
    print("prove:", lid, "| riservato:", os.path.join(RIS, lid + ".md"), "| pubblico: PROVE-METODO.md")


if __name__ == "__main__":
    main()
