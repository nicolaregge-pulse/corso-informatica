# -*- coding: utf-8 -*-
"""Gioco della talpa 1INF (14/10/2026): voti parziali dei presenti, calcolati da backlog, versioni e premio.
Regole: «in attesa» finché il personaggio non è nel gioco; personaggio nel gioco (prima PR) = 70;
ogni altra PR entrata nel gioco (seconda, terza: modifiche) +10; personaggio fra i primi tre del premio +10; massimo 100.
Scrive docs/1inf-voti/voti.json (pagina dei voti e classifica) e docs/compito/1inf-20261014-talpa/voti.json («Il mio punto»).
Uso: python3 strumenti/talpa_voti.py"""
import datetime, json, os
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def j(p, d):
    try: return json.load(open(os.path.join(QUI, p), encoding="utf-8"))
    except Exception: return d
PRESENTI = ["Moaaz A.", "Christian A.", "Matteo A.", "Giexther A.", "Anthony A.", "Aya B.", "Alessio C.", "Cristian C.", "Nehara F.", "Sara F.",
            "Wesley J.", "Yinlin L.", "Moaaz M.", "Abdel N.", "Muhammad N.", "Thomas R.", "Andrea S.", "Giovanni S.", "Shanzay S.", "Enea Z."]
B = j("docs/1inf-backlog/backlog.json", {"voci": []})["voci"]
E = j("docs/giochi/talpa-1inf/talpe/elenco.json", {"talpe": []})["talpe"]
C = j("docs/giochi/talpa-1inf/premi/voti.json", {}).get("conteggi", {})
punti = sorted({v for v in C.values() if v > 0}, reverse=True)[:3]
podio = {t["chi"] for t in E if C.get(t["file"], 0) in punti and C.get(t["file"], 0) > 0}
V, P = [], []
for a in PRESENTI:
    mie = [v for v in B if v["alunno"] == a]
    fatte = [v for v in mie if v.get("fatto")]
    if not fatte:
        voto, perche = None, ("richiesta arrivata, il personaggio è in preparazione" if mie else "in attesa della foto")
    else:
        voto = min(100, 70 + 10 * (len(fatte) - 1) + (10 if a in podio else 0))
        perche = f"personaggio nel gioco ({fatte[0]['fatto']})" + (f", {len(fatte) - 1} modifiche nel gioco" if len(fatte) > 1 else "") + (", premio dei personaggi migliori" if a in podio else "")
    el = [{"ora": v["ora"][-5:], "richiesta": v["richiesta"], "stato": v.get("fatto") or "da fare", "conta": True} for v in mie]
    V.append({"alunno": a, "pr": len(mie), "fatte": len(fatte), "feedback": True, "voto": voto if voto is not None else "in attesa", "perche": perche, "elenco": el})
    P.append({"alunno": a, "proposti": len(mie), "pubblicati": len(fatte), "voto": voto if voto is not None else "in attesa", "perche": perche})
ora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).strftime("%d/%m/%Y %H:%M")
json.dump({"aggiornato": ora + " (parziali)", "voti": V}, open(os.path.join(QUI, "docs/1inf-voti/voti.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"aggiornato": ora, "voti": P}, open(os.path.join(QUI, "docs/compito/1inf-20261014-talpa/voti.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(sum(1 for v in V if v["voto"] != "in attesa"), "voti su", len(V))
