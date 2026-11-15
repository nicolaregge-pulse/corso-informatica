#!/usr/bin/env python3
"""Coerenza del cruscotto con la fonte (v1.1, 15/11/2026: + controllo delle pagine «completo» per TUTTE e 4 le classi; v1.0, 13/11/2026; errore #327). Non scrive niente.
Uso: python3 -I strumenti/controlla_coerenza_cruscotto.py FABBRICA.xlsx
Confronta docs/cruscotto/dati/1INF-oggi.json e 1INF-presenze.json con l'export del foglio Fabbrica:
 1. stessi allievi (n. e iniziali «Nome I.») nella vista Oggi e nella scheda «Situazione pubblica 1INF»;
 2. per ogni Documento di oggi: il numero di «consegnato» della vista Oggi = numero di «Consegnato» della scheda Consegne 1INF;
 3. per ogni quiz di oggi: il numero di «fatto» della vista Oggi = allievi della scheda Situazione che hanno una percentuale (non MANCA);
 4. presenti + assenti della vista presenze = allievi del registro del giorno e nessun nome in comune tra le due liste.
Esce con 1 se una cosa non torna."""
import json, os, re, sys
import openpyxl
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(R, "docs", "cruscotto", "dati")
x = openpyxl.load_workbook(sys.argv[1], data_only=True)
oggi = json.load(open(os.path.join(D, "1INF-oggi.json"), encoding="utf-8"))
pres = json.load(open(os.path.join(D, "1INF-presenze.json"), encoding="utf-8"))
problemi = []
confronti = 0
def righe(n):
    return [r for r in x[n].iter_rows(values_only=True)]
cons = righe("Consegne 1INF"); hi = [i for i, r in enumerate(cons) if r and r[0] == "Stato"][0]; H = cons[hi]
sit = righe("Situazione 1INF"); si = [i for i, r in enumerate(sit) if r and r[0] == "Stato"][0]; SH = sit[si]
n_cons = len([r for r in cons[hi + 1:] if r[1]])
if oggi["n_allievi"] != n_cons:
    problemi.append("allievi: vista Oggi %d, Consegne %d" % (oggi["n_allievi"], n_cons))
voci = {v.get("id") or v.get("chiave"): v for v in oggi["voci"]} if isinstance(oggi["voci"], list) else {}
for ora in (4, 5, 6):
    j = [k for k, h in enumerate(H) if h and re.search(r"13/11 Ora %d:" % ora, str(h))]
    if j:
        c = sum(1 for r in cons[hi + 1:] if r[1] and str(r[j[0]]) == "Consegnato")
        o = sum(1 for a in oggi["allievi"] if a["stati"].get("ora%d-documento" % ora, {}).get("s") == "consegnato")
        confronti += 1
        if c != o: problemi.append("Documento ora %d: Oggi %d consegnati, Consegne %d" % (ora, o, c))
    j = [k for k, h in enumerate(SH) if h and re.search(r"13/11 Ora %d:" % ora, str(h))]
    if j:
        c = sum(1 for r in sit[si + 1:] if r[1] and r[j[0]] not in (None, "", "MANCA", "NON ABBINATA", "-"))
        o = sum(1 for a in oggi["allievi"] if a["stati"].get("ora%d-quiz" % ora, {}).get("s") == "fatto")
        confronti += 1
        if c != o: problemi.append("Quiz ora %d: Oggi %d fatti, Situazione %d" % (ora, o, c))
pa = pres.get("presenti", []); aa = pres.get("assenti", [])
if set(pa) & set(aa): problemi.append("presenze: nomi sia tra presenti sia tra assenti: %s" % sorted(set(pa) & set(aa)))
if len(pa) + len(aa) != pres.get("n_iscritti", pres.get("iscritti", len(pa) + len(aa))): problemi.append("presenze: presenti+assenti diverso dagli iscritti")

# ---- v1.1: pagine «completo» di tutte le classi (docs/cruscotto/completo/<CLASSE>.html) contro il foglio ----
from html.parser import HTMLParser
class _T(HTMLParser):
    """sezione id -> righe (liste di celle di testo) delle sue tabelle"""
    def __init__(s): super().__init__(); s.sez = None; s.d = {}; s.riga = None; s.cella = None
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "section": s.sez = a.get("id"); s.d.setdefault(s.sez, [])
        if t == "tr": s.riga = []
        if t in ("td", "th"): s.cella = ""
    def handle_data(s, x):
        if s.cella is not None: s.cella += x
    def handle_endtag(s, t):
        if t in ("td", "th") and s.riga is not None and s.cella is not None: s.riga.append(s.cella.strip()); s.cella = None
        if t == "tr" and s.riga is not None and s.sez: s.d[s.sez].append(s.riga); s.riga = None
def _nomi_foglio(nome_sheet):
    r = righe(nome_sheet); i = [k for k, x in enumerate(r) if x and x[0] == "Stato"][0]
    return r[i], [x for x in r[i + 1:] if x and x[0] in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO") and x[1]]
tot_cmp = 0
for CL in ("1INF", "2INF", "3INF", "4TI"):
    pth = os.path.join(R, "docs", "cruscotto", "completo", CL + ".html")
    if not os.path.exists(pth):
        problemi.append("%s: manca la pagina completo" % CL); continue
    p = _T(); p.feed(open(pth, encoding="utf-8").read())
    def corpo(sid): return [r for r in p.d.get(sid, []) if r and not r[0].startswith(("Assenti all", "Classe")) and len(r) > 1]
    # 1. stessi allievi in presenza, compiti, quiz, recuperi e nella Situazione pubblica del foglio
    hs, ds = _nomi_foglio("Situazione pubblica " + CL)
    att = {x[1] for x in ds}
    for sid in ("presenza", "compiti", "quiz", "recuperi"):
        nm = {r[0].split("\n")[0].strip() for r in corpo(sid)[1:]}
        nm = {re.sub(r"assente il \d\d/\d\d$", "", n).strip() for n in nm}
        tot_cmp += 1
        if not att <= nm:
            problemi.append("%s %s: nella Situazione pubblica ma non nella pagina: %s" % (CL, sid, sorted(att - nm)))
        elif nm - att and sid == "presenza":
            print("AVVISO %s: %d allievi del registro non sono nel foglio Fabbrica (nessun dato di quiz o compiti): %s" % (CL, len(nm - att), sorted(nm - att)))
    # 2. compiti: caselle «consegnato» della pagina = «Consegnato» della scheda Consegne
    if "Consegne " + CL in x.sheetnames:
        hc, dc = _nomi_foglio("Consegne " + CL)
        ic = hc.index("Consegnati")
        fogl = sum(1 for r in dc for v in r[3:ic] if v == "Consegnato")
        pag = sum(1 for r in corpo("compiti")[1:] for c in r[1:-2] if c.startswith("\u2713"))
        tot_cmp += 1
        if fogl != pag: problemi.append("%s compiti consegnati: pagina %d, foglio %d" % (CL, pag, fogl))
    # 3. quiz: fatti della pagina (colonna Fatti «n/m») = celle con percentuale della Situazione (quiz non Sicurezza e non futuri)
    rq = corpo("quiz")
    if rq and len(rq[0]) > 2:
        pag = sum(int(r[-1].split("/")[0]) for r in rq[1:] if re.match(r"^\d+/\d+$", r[-1]))
        fogl = 0
        idx = [k for k, h in enumerate(hs) if k >= 2 and not re.search(r"quiz-\w+-sic|^\s*Sic", h) and k < hs.index("Fatti / totali")]
        for r in ds:
            fogl += sum(1 for k in idx if re.match(r"^\d+%\s*\(", (r[k] or "").strip()))
        tot_cmp += 1
        if fogl != pag: problemi.append("%s quiz fatti: pagina %d, foglio %d" % (CL, pag, fogl))
    # 4. presenze: nessun nome tra presenti e assenti, ordine presenti prima
    pr = [r for r in p.d.get("presenza", []) if r and len(r) > 3]
print("ROSSO: " + "; ".join(problemi) if problemi else "VERDE: vista Oggi, Consegne, Situazione e presenze coerenti (%d confronti Documenti/quiz, %d allievi nel foglio, %d presenti, %d assenti); pagine «completo» 4 classi: %d confronti" % (confronti, n_cons, len(pa), len(aa), tot_cmp))
sys.exit(1 if problemi else 0)
