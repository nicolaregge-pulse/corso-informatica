#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Traccia degli argomenti degli Allegati A: cosa e' fatto, cosa resta, cronologia.

Versione 1.0 (20/11/2026). PUBBLICO: nessun dato di allievi nel codice.
I dati (stato, cronologia, xlsx, pdf) vivono nel RISERVATO:
  <riservato>/dati/allegato-a-traccia/stato-traccia.json   (stato machine-readable, cronologia append-only)
  <riservato>/registro-allievi/ARGOMENTI-ALLEGATO-A-TRACCIA-2026-27-vX.Y.{xlsx,pdf}

Comandi:
  inizializza                  crea lo stato dalle fonti (solo se non esiste; --forza per rifarlo) e le versioni 1.0 di xlsx e pdf
  segna <classe> <materia> <n voce> <data> <ora> <durata> [titolo]   segna una voce come svolta; nuova versione di xlsx e pdf
  lista-da-fare <classe> [materia]
  cronologia [classe]
  rigenera                     nuova versione di xlsx e pdf dallo stato attuale (senza cambiare i dati)

Opzioni comuni: --riservato DIR (default /home/user/corso-informatica-riservato, o variabile ARGOMENTI_RISERVATO),
                --pubblico DIR (default: il repository di questo script).
Regole: R5.2 (nessuna voce aggiunta all'Allegato A), R7 (ogni voce con fonte; abbinamento dubbio = «da confermare dal docente»).
"""
import argparse
import datetime as D
import difflib
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

CLASSI = ["1INF", "2INF", "3INF", "4TI"]
NOME_CLASSE = {"1INF": "1INFspe", "2INF": "2INFspe", "3INF": "3INFspe", "4TI": "4TI"}
DA_ASSEGNARE = "da assegnare (docente)"
MATERIE = {
    "1INF": ["Impresa simulata (lab)", "Laboratorio professionale", "Tecnologia professionale", "Sicurezza professionale"],
    "2INF": ["Informatica", "Laboratorio professionale", "Sicurezza professionale"],
    "3INF": ["Laboratorio professionale"],
    "4TI": ["Laboratorio professionale"],
}
# ore previste (dati/docente/ORE-DOCENZA-2026-27-v1.0.md, dal PDF dell'incarico, non provato sul contratto)
ORE_PREVISTE = {
    ("1INF", "Impresa simulata (lab)"): (198, "150 + 48 come scritto nel PDF; il significato del 48 e' da confermare dal docente (la somma 343 della 1INF lo conta)"),
    ("1INF", "Laboratorio professionale"): (61, ""),
    ("1INF", "Tecnologia professionale"): (51, ""),
    ("1INF", "Sicurezza professionale"): (33, ""),
    ("2INF", "Informatica"): (48, ""),
    ("2INF", "Laboratorio professionale"): (135, ""),
    ("2INF", "Sicurezza professionale"): (16, ""),
    ("3INF", "Laboratorio professionale"): (143, ""),
    ("4TI", "Laboratorio professionale"): (99, ""),
}
# scala del tempo dal grafico «ORE DI DOCENZA 2026/27» del 19/11/2026 (ipotesi modificabile del docente)
PERIODI = [
    {"nome": "23/11/2026 - 18/02/2027", "dal": "2026-11-23", "al": "2027-02-18",
     "ore_sett": {"1INF": 9.1, "2INF": 10.1, "3INF": 0, "4TI": 2.5}, "nota": "3INFspe in stage dal 23/11 al 18/02 (nel grafico «-»)"},
    {"nome": "19/02/2027 - 21/05/2027", "dal": "2027-02-19", "al": "2027-05-21",
     "ore_sett": {"1INF": 12.1, "2INF": 0, "3INF": 6.3, "4TI": 3.4}, "nota": "2INFspe in stage dal 19/02 al 21/05 (nel grafico «-»); 3INFspe rientra il 19/02"},
    {"nome": "24/05/2027 - 04/06/2027", "dal": "2027-05-24", "al": "2027-06-04",
     "ore_sett": {"1INF": 7.5, "2INF": 8.3, "3INF": 3.9, "4TI": 2.1}, "nota": "tutte le classi presenti"},
]
FESTIVI = [("2026-12-07", "2026-12-08", "festivi 7-8/12"), ("2026-12-24", "2027-01-06", "ferie di Natale 24/12-06/01"),
           ("2027-03-25", "2027-03-29", "Pasqua 25-29/03/2027"), ("2027-06-02", "2027-06-02", "festivo 2/06")]
ORE_SETT_TOTALE = 21.8
ORE_FATTE_SETT = 25.7
ORE_FATTE_GRAFICO = 239
TOTALE_INCARICO = 784

STOP = set("di del della dei delle e ed il lo la le un una in con per su da al alla ai alle nel nella che a o come ora ore".split())


def sn(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def toks(s):
    return {t for t in re.findall(r"[a-z0-9]+", sn(s)) if len(t) >= 4 and t not in STOP}


def fmt_data(iso):
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


def parse_data(s):
    s = s.strip()
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})(?:/(\d{4}))?", s)
    if m:
        y = int(m.group(3)) if m.group(3) else D.date.today().year
        return D.date(y, int(m.group(2)), int(m.group(1))).isoformat()
    D.date.fromisoformat(s)
    return s


def ora_h(a, b):
    """ore del registro (h1..h6) da un intervallo di orologio 'a-b' (8-9 = h1)."""
    return list(range(a - 7, b - 7))


# ------------------------------------------------------------------ percorsi
def percorsi(args):
    ris = Path(args.riservato or os.environ.get("ARGOMENTI_RISERVATO", "/home/user/corso-informatica-riservato"))
    pub = Path(args.pubblico) if args.pubblico else Path(__file__).resolve().parents[1]
    return pub, ris, ris / "dati" / "allegato-a-traccia" / "stato-traccia.json", ris / "registro-allievi"


def carica(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def salva(p, d):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ inizializzazione
def costruisci_stato(pub, ris):
    stato_a = carica(pub / "allegato-a-stato" / "stato-allegato-a.json")
    cop = carica(pub / "programmi-ufficiali" / "2026-27" / "copertura-allegato-a.json")
    did = carica(ris / "report" / "2026-11-19" / "ARGOMENTI-DIDAWEB-LETTI-19-11-v1.0.json")

    # 1) lezioni = una riga per ora del registro DIDAweb (letto il 19/11/2026)
    lez, per_chiave = [], {}
    for mat_key, righe in did["materie"].items():
        cl, mat = mat_key.split(" ", 1)
        mat = {"Impresa simulata (LAB)": "Impresa simulata (lab)"}.get(mat, mat)
        for r in righe:
            L = {"id": f"{cl}-{r['data']}-h{r['ora']}", "classe": cl, "materia": mat, "data": r["data"], "ora": r["ora"],
                 "durata": 1, "titolo_registro": r["argomento"] or "(vuoto sul registro: lo mette la direzione)",
                 "fonte": "DIDAweb letto il 19/11/2026 (ARGOMENTI-DIDAWEB-LETTI-19-11-v1.0.json)",
                 "voci": [], "voci_dubbie": [], "voci_candidate": []}
            lez.append(L)
            per_chiave[(cl, r["data"], r["ora"])] = L
    lez.sort(key=lambda x: (x["data"], x["classe"], x["ora"]))

    # 2) lezioni di copertura -> righe DIDAweb (certe se c'e' l'orario, altrimenti da confermare)
    cop_lez = {}
    for l in cop["lezioni"]:
        cl, data = l["classe"], l["data"]
        righe_giorno = [x for x in lez if x["classe"] == cl and x["data"] == data]
        certe, candidate = [], []
        if l.get("ora"):
            a, b = [int(x) for x in l["ora"].split("-")]
            certe = [per_chiave[(cl, data, h)]["id"] for h in ora_h(a, b) if (cl, data, h) in per_chiave]
        else:
            tt = toks(l["titolo"])
            for x in righe_giorno:
                if tt & toks(x["titolo_registro"]) or ("sicurezza" in sn(l["titolo"]) and x["materia"] == "Sicurezza professionale"):
                    candidate.append(x["id"])
            if len(candidate) == 1:
                certe, candidate = candidate, []
        cop_lez[l["id"]] = {"titolo": l["titolo"], "data": data, "fonte": l["fonte"], "certe": certe, "candidate": candidate}

    cop_voce = {}
    for c in cop["copertura"]:
        cop_voce[(c["classe"], c["voce"])] = c

    # 3) voci dall'Allegato A (parte «Regge»), una riga per occorrenza, nell'ordine del file
    classi = {}
    for cl in CLASSI:
        voci, n = [], 0
        for comp in stato_a["voci"][cl]:
            modulo, mi = "", 0
            for v in comp["voci"]:
                if v["liv"] == 0:
                    modulo, mi = v["testo"], mi + 1
                    continue
                n += 1
                c = cop_voce.get((cl, v["testo"]))
                lids = c["lezioni"] if c else []
                certe, dubbie_ora, dub = [], [], False
                for lid in lids:
                    certe += cop_lez[lid]["certe"]
                    dubbie_ora += cop_lez[lid]["candidate"]
                nota = v.get("nota", "")
                if v["stato"] == "FATTO":
                    stato = "FATTO"
                elif nota.startswith("parziale") or lids:
                    stato = "PARZIALE"
                else:
                    stato = "DA FARE"
                dc = stato != "FATTO" and bool(nota or lids)
                dc_nota = nota if dc else ""
                if stato == "FATTO" and not lids:
                    dc, dc_nota = True, "data, ora e lezione del registro non indicate nella fonte (confermato dal docente): abbinamento da confermare dal docente"
                if stato == "FATTO" and dubbie_ora and not certe:
                    dc, dc_nota = True, "data certa, ora non indicata: abbinamento all'ora da confermare dal docente"
                voci.append({"n": n, "comp": comp["comp"], "comp_titolo": comp["titolo"], "modulo": modulo,
                             "testo": v["testo"], "stato": stato, "stato_allegato": v["stato"],
                             "materia": DA_ASSEGNARE, "materia_fonte": "", "fonte": v.get("fonte", ""),
                             "nota": nota, "da_confermare": dc, "da_confermare_nota": dc_nota,
                             "lezioni": sorted(set(certe)), "lezioni_dubbie": sorted(set(dubbie_ora)),
                             "settimana_prevista": ""})
        classi[cl] = voci

    # 4) abbinamenti voce <-> riga del registro
    for cl, voci in classi.items():
        for v in voci:
            dub = v["da_confermare"] and v["stato"] != "FATTO"
            for lid in v["lezioni"]:
                r = next(x for x in lez if x["id"] == lid)
                (r["voci_dubbie"] if dub else r["voci"]).append(f"{cl}:{v['n']}")
            for lid in v["lezioni_dubbie"]:
                r = next(x for x in lez if x["id"] == lid)
                r["voci_candidate"].append(f"{cl}:{v['n']}")

    # 5) materia di ogni voce, con la fonte (mai indovinata)
    idx = {x["id"]: x for x in lez}
    for cl, voci in classi.items():
        for v in voci:
            mats = sorted({idx[i]["materia"] for i in v["lezioni"]})
            if len(mats) == 1:
                v["materia"], v["materia_fonte"] = mats[0], "materia della lezione sul registro DIDAweb"
            elif len(mats) > 1:
                v["materia_fonte"] = "lezioni di piu' materie (" + ", ".join(mats) + "): da assegnare dal docente"
            elif re.match(r"\d+ª ora:", v["testo"]) and cl in ("1INF", "2INF"):
                v["materia"], v["materia_fonte"] = "Sicurezza professionale", "voce numerata del modulo «Sicurezza sul lavoro: le 16 lezioni» (Comp. 14)"
            elif len(MATERIE[cl]) == 1:
                v["materia"], v["materia_fonte"] = MATERIE[cl][0], "unica materia della classe nell'incarico"
            else:
                v["materia_fonte"] = "nessuna lezione abbinata: materia da assegnare dal docente"

    # 6) candidati per titolo (solo suggerimento, non cambia lo stato) per le ore senza voce
    for r in lez:
        if r["voci"] or r["voci_dubbie"]:
            continue
        best = []
        for v in classi[r["classe"]]:
            a, b = sn(r["titolo_registro"]), sn(v["testo"])
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if r["materia"] == "Sicurezza professionale":
                continue  # Sicurezza: il titolo lo mette la direzione (R5.2bis), nessun suggerimento
            if a and (ratio >= 0.72 or (len(toks(r["titolo_registro"]) & toks(v["testo"])) >= 2)):
                best.append((ratio, v["n"]))
        best.sort(reverse=True)
        r["voci_candidate"] = sorted(set(r["voci_candidate"] + [f"{r['classe']}:{n}" for _, n in best[:2]]))

    stato = {
        "versione_dati": "1.0",
        "creato": datetime_now(),
        "fonti": {
            "voci": "allegato-a-stato/stato-allegato-a.json v" + stato_a["versione"] + " (pubblico; parte «Regge» dell'Allegato A del 02/11/2026)",
            "abbinamenti": "programmi-ufficiali/2026-27/copertura-allegato-a.json v" + cop["versione"] + " e svolto-2026-27.json",
            "registro": "report/2026-11-19/ARGOMENTI-DIDAWEB-LETTI-19-11-v1.0.json (DIDAweb letto il 19/11/2026 ore 10:22-10:25)",
            "ore_previste": "dati/docente/ORE-DOCENZA-2026-27-v1.0.md (PDF dell'incarico, non provato sul contratto)",
            "scala_tempo": "dati/ore-docenza/GRAFICO-ORE-DOCENZA-19-11-2026.png (ipotesi modificabile del docente)",
        },
        "classi": classi,
        "lezioni": lez,
        "ore_previste": [{"classe": c, "materia": m, "ore": o, "nota": n} for (c, m), (o, n) in ORE_PREVISTE.items()],
        "periodi": PERIODI,
        "festivi": [{"dal": a, "al": b, "nome": n} for a, b, n in FESTIVI],
        "eventi": [{"ts": datetime_now(), "tipo": "inizializza", "testo": "stato creato dalle fonti"}],
    }
    return stato


def datetime_now():
    return D.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


# ------------------------------------------------------------------ calcoli
def lezioni_voce(stato, v):
    idx = {x["id"]: x for x in stato["lezioni"]}
    return [idx[i] for i in v["lezioni"] if i in idx]


def descr_lezioni(stato, v):
    """(data/ora/durata, titolo registro)"""
    ls = sorted(lezioni_voce(stato, v), key=lambda x: (x["data"], x["ora"]))
    if not ls:
        dub = [x for x in stato["lezioni"] if x["id"] in v.get("lezioni_dubbie", [])]
        if dub:
            d = sorted({x["data"] for x in dub})
            return (", ".join(fmt_data(x) for x in d) + ": ora da confermare dal docente (possibili " + ", ".join(f"h{x['ora']}" for x in sorted(dub, key=lambda z: z['ora'])) + ")",
                    " | ".join(x["titolo_registro"] for x in dub))
        extra = v.get("eventi_segna", [])
        return ("", "")
    gruppi = {}
    for x in ls:
        gruppi.setdefault(x["data"], []).append(x)
    parti, titoli = [], []
    for d, xs in gruppi.items():
        hs = [x["ora"] for x in xs]
        ore = sum(x["durata"] for x in xs)
        h = f"h{min(hs)}" if len(hs) == 1 else f"h{min(hs)}-h{max(hs)}"
        parti.append(f"{fmt_data(d)} {h}, {ore:g} h")
        titoli += [x["titolo_registro"] for x in xs]
    tot = sum(x["durata"] for x in ls)
    s = "; ".join(parti) + (f" (totale {tot:g} h)" if len(gruppi) > 1 else "")
    return s, " | ".join(dict.fromkeys(titoli))


def giorni_lavorativi(dal, al, festivi):
    hol = set()
    for f in festivi:
        d = D.date.fromisoformat(f["dal"])
        while d <= D.date.fromisoformat(f["al"]):
            hol.add(d)
            d += D.timedelta(1)
    n, d = 0, D.date.fromisoformat(dal)
    while d <= D.date.fromisoformat(al):
        if d.weekday() < 5 and d not in hol:
            n += 1
        d += D.timedelta(1)
    return n


def ore_fatte(stato, cl, mat=None):
    return sum(x["durata"] for x in stato["lezioni"] if x["classe"] == cl and (mat is None or x["materia"] == mat))


# ------------------------------------------------------------------ versioni dei file di uscita
def prossima_versione(cartella):
    mx = (1, -1)
    for p in Path(cartella).glob("ARGOMENTI-ALLEGATO-A-TRACCIA-2026-27-v*.*"):
        m = re.search(r"-v(\d+)\.(\d+)\.(xlsx|pdf)$", p.name)
        if m:
            mx = max(mx, (int(m.group(1)), int(m.group(2))))
    return f"{mx[0]}.{mx[1] + 1}" if mx[1] >= 0 else "1.0"


def genera_uscite(stato, cartella, versione):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import argomenti_allegato_a_uscite as U
    cartella = Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    nx = cartella / f"ARGOMENTI-ALLEGATO-A-TRACCIA-2026-27-v{versione}.xlsx"
    npdf = cartella / f"ARGOMENTI-ALLEGATO-A-TRACCIA-2026-27-v{versione}.pdf"
    U.scrivi_xlsx(stato, nx, versione)
    U.scrivi_pdf(stato, npdf, versione)
    return nx, npdf


# ------------------------------------------------------------------ comandi
def cmd_inizializza(a):
    pub, ris, sp, out = percorsi(a)
    if sp.exists() and not a.forza:
        sys.exit(f"Esiste gia' {sp}: non lo rifaccio (usa --forza per ricostruirlo dalle fonti, perdendo i 'segna').")
    st = costruisci_stato(pub, ris)
    v = prossima_versione(out)
    st["versione_output"] = v
    salva(sp, st)
    nx, npdf = genera_uscite(st, out, v)
    print(f"Stato: {sp}\nCreati: {nx}\n        {npdf}")


def trova_materia(cl, testo):
    t = sn(testo).strip()
    c = [m for m in MATERIE[cl] if sn(m) == t] or [m for m in MATERIE[cl] if sn(m).startswith(t) or t in sn(m)]
    if len(c) != 1:
        sys.exit(f"Materia «{testo}» non valida o ambigua per {cl}. Materie: " + "; ".join(MATERIE[cl]))
    return c[0]


def cmd_segna(a):
    pub, ris, sp, out = percorsi(a)
    st = carica(sp)
    cl = a.classe.upper()
    if cl not in CLASSI:
        sys.exit("Classe non valida: " + ", ".join(CLASSI))
    mat = trova_materia(cl, a.materia)
    voce = next((v for v in st["classi"][cl] if v["n"] == a.n_voce), None)
    if not voce:
        sys.exit(f"Voce {a.n_voce} non trovata in {cl} (n da 1 a {len(st['classi'][cl])}).")
    data = parse_data(a.data)
    m = re.fullmatch(r"h?(\d)(?:-h?(\d))?", a.ora.strip().lower())
    if not m:
        sys.exit("Ora non valida: usa 3, h3 oppure 3-4 (1 = 8-9 ... 6 = 13-14).")
    h1 = int(m.group(1))
    h2 = int(m.group(2)) if m.group(2) else h1
    durata = float(a.durata.replace(",", "."))
    if not (1 <= h1 <= h2 <= 6):
        sys.exit("Ora fuori da 1-6.")
    if voce["materia"] not in (DA_ASSEGNARE, mat) and not a.forza:
        sys.exit(f"La voce e' assegnata a «{voce['materia']}», non a «{mat}». Usa --forza per cambiare.")
    titolo = a.titolo or "(titolo del registro non indicato)"
    ore_righe = list(range(h1, h2 + 1))
    per_riga = durata / len(ore_righe)
    nuove = 0
    ids = []
    for h in ore_righe:
        lid = f"{cl}-{data}-h{h}"
        ids.append(lid)
        r = next((x for x in st["lezioni"] if x["id"] == lid), None)
        if r is None:
            r = {"id": lid, "classe": cl, "materia": mat, "data": data, "ora": h, "durata": per_riga,
                 "titolo_registro": titolo, "fonte": f"segnato il {D.date.today().isoformat()} con argomenti_allegato_a.py",
                 "voci": [], "voci_dubbie": [], "voci_candidate": []}
            st["lezioni"].append(r)
            nuove += per_riga
        elif r["materia"] != mat and not a.forza:
            sys.exit(f"L'ora {lid} e' gia' registrata come «{r['materia']}»: usa --forza se e' un errore.")
        if f"{cl}:{voce['n']}" not in r["voci"]:
            r["voci"].append(f"{cl}:{voce['n']}")
        if f"{cl}:{voce['n']}" in r["voci_dubbie"]:
            r["voci_dubbie"].remove(f"{cl}:{voce['n']}")
    voce["lezioni"] = sorted(set(voce["lezioni"] + ids))
    voce["lezioni_dubbie"] = []
    voce["stato"] = "PARZIALE" if a.parziale else "FATTO"
    voce["materia"], voce["materia_fonte"] = mat, "indicata dal docente con 'segna'"
    voce["da_confermare"], voce["da_confermare_nota"] = False, ""
    voce["fonte"] = f"segnato dal docente il {D.date.today().strftime('%d/%m/%Y')} (argomenti_allegato_a.py)"
    st["lezioni"].sort(key=lambda x: (x["data"], x["classe"], x["ora"]))
    st["eventi"].append({"ts": datetime_now(), "tipo": "segna", "classe": cl, "materia": mat, "n_voce": voce["n"],
                         "voce": voce["testo"], "data": data, "ora": a.ora, "durata": durata, "titolo": titolo,
                         "stato": voce["stato"], "ore_nuove": nuove})
    v = prossima_versione(out)
    st["versione_output"] = v
    salva(sp, st)
    nx, npdf = genera_uscite(st, out, v)
    resta = [x for x in st["classi"][cl] if x["stato"] != "FATTO"]
    print(f"{'Parziale' if a.parziale else 'Fatto'}: «{voce['testo']}» ({cl}, {mat}, {fmt_data(data)} h{a.ora}, {durata:g} h); "
          f"voci rimaste in {cl}: {sum(1 for x in resta if x['stato']=='DA FARE')} da fare, {sum(1 for x in resta if x['stato']=='PARZIALE')} parziali. "
          f"Traccia v{v}: {nx.name}")


def cmd_lista(a):
    pub, ris, sp, out = percorsi(a)
    st = carica(sp)
    cl = a.classe.upper()
    mat = trova_materia(cl, a.materia) if a.materia and sn(a.materia) not in ("da assegnare", "tutte") else None
    for v in st["classi"][cl]:
        if v["stato"] == "FATTO":
            continue
        if mat and v["materia"] != mat:
            continue
        if a.materia and sn(a.materia) == "da assegnare" and v["materia"] != DA_ASSEGNARE:
            continue
        dc = "  [da confermare dal docente]" if v["da_confermare"] else ""
        print(f"{cl} n.{v['n']:>3}  Comp.{v['comp']:<2} {v['stato']:<8} {v['materia'][:26]:<26} {v['testo']}{dc}")


def cmd_cronologia(a):
    pub, ris, sp, out = percorsi(a)
    st = carica(sp)
    for r in st["lezioni"]:
        if a.classe and r["classe"] != a.classe.upper():
            continue
        vv = ", ".join(r["voci"]) or ("(da confermare: " + ", ".join(r["voci_dubbie"]) + ")" if r["voci_dubbie"] else "-")
        print(f"{fmt_data(r['data'])} h{r['ora']} {r['classe']:<4} {r['materia'][:24]:<24} {r['durata']:g}h  {r['titolo_registro'][:60]:<60}  voce: {vv}")


def cmd_rigenera(a):
    pub, ris, sp, out = percorsi(a)
    st = carica(sp)
    v = prossima_versione(out)
    st["versione_output"] = v
    st["eventi"].append({"ts": datetime_now(), "tipo": "rigenera", "testo": "nuova versione dei file dallo stato"})
    salva(sp, st)
    print(*genera_uscite(st, out, v), sep="\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--riservato")
    p.add_argument("--pubblico")
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("inizializza"); s.add_argument("--forza", action="store_true"); s.set_defaults(f=cmd_inizializza)
    s = sp.add_parser("segna")
    s.add_argument("classe"); s.add_argument("materia"); s.add_argument("n_voce", type=int); s.add_argument("data")
    s.add_argument("ora"); s.add_argument("durata"); s.add_argument("titolo", nargs="?")
    s.add_argument("--parziale", action="store_true"); s.add_argument("--forza", action="store_true"); s.set_defaults(f=cmd_segna)
    s = sp.add_parser("lista-da-fare"); s.add_argument("classe"); s.add_argument("materia", nargs="?"); s.set_defaults(f=cmd_lista)
    s = sp.add_parser("cronologia"); s.add_argument("classe", nargs="?"); s.set_defaults(f=cmd_cronologia)
    s = sp.add_parser("rigenera"); s.set_defaults(f=cmd_rigenera)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
