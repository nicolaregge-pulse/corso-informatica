# -*- coding: utf-8 -*-
"""Audit degli investitori per «Il treno blindato» (2INF): calcola l'investimento da 100.000 a 2.000.000 $.

Legge i dati veri del lavoro della classe e scrive docs/2inf-treno/investitori/audit.json, che la pagina
docs/2inf-treno/investitori/ mostra come una visita di investitori. Ogni volta che si rilancia nasce un nuovo
audit (audit-v1, v2, ...): gli audit vecchi restano, così i ragazzi vedono se l'azienda cresce.

Cosa guarda (punti su 100):
  1. richieste di modifica consegnate dalle squadre (stato.json → punteggi.*.richieste)   max 30
  2. variazioni di codice su Git dopo la demo del prof (commit 10e2cdf..HEAD sul gioco)  max 20
  3. versioni della classe (versioni.json, esclusi v0.0 e v0.1-alfa)                    max 15
  4. squadre attive (almeno una richiesta, un file o un lavoro fatto)                      max 15
  5. disciplina: −2 per ogni PC visto a fare altro (punteggi.*.fuori)                     max 10
  6. presentazione e verbale della CEO (voto del prof, --ceo 0-10)                         max 10
Uso:
  python3 strumenti/audit_investitori_treno.py [--ceo N] [--nota "testo"]
"""
import datetime, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQ = os.path.join(ROOT, "docs", "2inf-treno", "squadre", "stato.json")
VER = os.path.join(ROOT, "docs", "giochi", "treno-blindato", "versioni", "versioni.json")
OUT = os.path.join(ROOT, "docs", "2inf-treno", "investitori", "audit.json")
MIN, MAX = 100_000, 2_000_000


def arg(nome, default=None):
    return sys.argv[sys.argv.index(nome) + 1] if nome in sys.argv else default


def commit_oggi():
    # contano solo le modifiche nate dal lavoro della classe: dopo la demo del prof (commit 10e2cdf, v0.1-alfa)
    out = subprocess.run(["git", "-C", ROOT, "log", "10e2cdf..HEAD", "--format=%h|%s", "--",
                          "docs/giochi/treno-blindato"], capture_output=True, text=True).stdout.strip()
    return [r.split("|", 1) for r in out.splitlines() if r]


def main():
    sq = json.load(open(SQ, encoding="utf-8"))
    ver = [v for v in json.load(open(VER, encoding="utf-8")) if v["versione"] not in ("v0.0", "v0.1-alfa")]  # solo le versioni della classe
    P = sq.get("punteggi", {})
    vecchio = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {"audit": []}
    ceo = max(0, min(10, int(arg("--ceo", vecchio["audit"][-1]["ceo"] if vecchio["audit"] else 3))))

    richieste = sum(p.get("richieste", 0) for p in P.values())
    commit = commit_oggi()
    fuori = sum(p.get("fuori", 0) for p in P.values()) + sq.get("fuori_da_assegnare", 0)
    squadre = []
    for k, s in sq["squadre"].items():
        p = P.get(k, {})
        fatti = sum(1 for l in s["lavori"] if l.get("stato") == "fatto")
        attiva = bool(p.get("richieste") or p.get("file") or p.get("nel_gioco") or fatti)
        squadre.append({"chiave": k, "nome": s["nome"], "colore": s["colore"], "richieste": p.get("richieste", 0),
                        "file": p.get("file", 0), "lavori_fatti": fatti, "fuori": p.get("fuori", 0), "attiva": attiva})
    attive = sum(1 for s in squadre if s["attiva"])

    voci = [
        {"cosa": "Richieste di modifica consegnate dalle squadre", "valore": richieste, "punti": min(30, 2 * richieste), "max": 30,
         "giudizio": "Le idee scritte sono il prodotto dell'azienda: senza richieste gli sviluppatori non sanno cosa fare."},
        {"cosa": "Variazioni di codice su Git nate dalle vostre richieste (commit dopo la demo)", "valore": len(commit), "punti": min(20, 2 * len(commit)), "max": 20,
         "giudizio": "Ogni commit è una modifica vera del gioco, con data e descrizione: gli investitori la possono controllare."},
        {"cosa": "Versioni del gioco uscite dal lavoro della classe", "valore": len(ver), "punti": min(15, 5 * len(ver)), "max": 15,
         "giudizio": "Un'azienda seria fa uscire versioni spesso e le tiene tutte."},
        {"cosa": "Squadre al lavoro (su 5)", "valore": attive, "punti": 3 * attive, "max": 15,
         "giudizio": "Gli investitori vogliono un'azienda dove lavorano tutti i reparti, non solo uno."},
        {"cosa": "Disciplina: PC visti a fare altro", "valore": fuori, "punti": max(0, 10 - 2 * fuori), "max": 10,
         "giudizio": "Chi gioca durante il lavoro fa scappare gli investitori."},
        {"cosa": "Presentazione e verbale della CEO (voto del prof)", "valore": ceo, "punti": ceo, "max": 10,
         "giudizio": "La CEO deve saper raccontare cosa fa l'azienda e cosa farà."},
    ]
    punti = sum(v["punti"] for v in voci)
    totale = round((MIN + (MAX - MIN) * punti / 100) / 10_000) * 10_000
    quote = [("Navigli Ventures", "Milano", 0.4), ("Long River Capital", "Shanghai", 0.35), ("Al-Nahr Investments", "Il Cairo", 0.25)]
    investitori = [{"nome": n, "citta": c, "dollari": round(totale * q / 1000) * 1000} for n, c, q in quote]
    investitori[0]["dollari"] += totale - sum(i["dollari"] for i in investitori)

    consigli = []
    for s in squadre:
        if s["chiave"] == "ceo":
            continue
        if not s["richieste"]:
            consigli.append("Squadra " + s["nome"] + ": nessuna richiesta di modifica. Una richiesta chiara vale +2 punti e una nuova versione del gioco.")
    if fuori:
        consigli.append("PC visti a fare altro: " + str(fuori) + ". Ognuno costa 2 punti: circa 38.000 $ di investimento perso.")
    if ceo < 7:
        consigli.append("La CEO prepari 3 frasi: cosa fa il gioco, cosa ha fatto ogni squadra, cosa uscirà nella prossima versione.")

    n = len(vecchio["audit"]) + 1
    adesso = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).strftime("%d/%m/%Y %H:%M")
    vecchio["audit"].append({"versione": "audit-v%d" % n, "ora": adesso, "punti": punti, "investimento": totale, "ceo": ceo,
                             "voci": voci, "squadre": squadre, "investitori": investitori, "consigli": consigli,
                             "ultimi_commit": [{"id": c[0], "msg": c[1][:110]} for c in commit[:6]],
                             "nota": arg("--nota", "")})
    vecchio["aggiornato"] = adesso
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(vecchio, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("audit-v%d: %d punti → %s $" % (n, punti, format(totale, ",").replace(",", ".")))


if __name__ == "__main__":
    main()
