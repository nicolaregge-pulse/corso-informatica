#!/usr/bin/env python3
"""Dati della vista «Sicurezza» del cruscotto (docs/cruscotto/dati/). Versione 1.0 (13/11/2026).

Da un file xlsx esportato dal foglio Fabbrica produce, per 1INF e 2INF:
    docs/cruscotto/dati/<CLASSE>-sicurezza.csv   una riga per allievo («Nome I.»), una colonna per ora di Sicurezza
    docs/cruscotto/dati/sicurezza-link.json      bottoni al Modulo di ogni quiz di Sicurezza (link per i ragazzi, da «Esiti»)
    docs/cruscotto/dati/meta.json                aggiunge, per ogni classe, ora del dato e ora dell'export (le altre voci restano)

Fonti (solo queste, nessun'altra):
  1. scheda «Sicurezza pubblica <CLASSE>»  (senza nomi: colonna Id = SHA-256 del nome in maiuscolo; ora del dato in riga 1)
  2. schede «Ris <id quiz>»                (ultimo invio, tentativi, punti: per «da quanto non consegna» e per le domande aperte)
  3. scheda «Esiti»                        (link per i ragazzi dei quiz)
  4. scheda «Elenco <CLASSE>»              (SOLO in memoria, per dare «Nome I.» all'Id e abbinare le email; non viene scritta)
  5. «Situazione pubblica <CLASSE>»        (controllo: ogni «Nome I.» deve esistere anche li')
  6. 2INF, ore 1-4: se la scheda dice «dato non importato», il registro dei quiz nel riservato
     (dati/verifiche/2inf-quiz-sicurezza{1,2,3,4}-*/_RISULTATI-QUIZ.csv, stesso abbinamento di strumenti/sicurezza_2inf.py;
     la data dell'ultimo invio di ogni ora e' nella riga «Fonti»). L'ora 5 della 2INF non ha un quiz in indice.json: resta «dato non importato» (non si presume).

DOMANDE APERTE (2INF 6A e 6B, decisione del docente: 8 chiuse da 1 punto + 2 aperte da 2 punti, totale 12, soglia 80% = 10 punti;
le aperte Moduli restano a 0 e le corregge Claude; fonte: SOLUZIONI-2INF-SICUREZZA-ORA6-v1.0.md, riservato):
  - «Migliore» del foglio = solo le chiuse. Finche' le aperte non sono corrette la cella dice «IN CORREZIONE chiuse X/8»
    (se anche con le aperte al massimo non si arriva a 10 punti: «DA RECUPERARE chiuse X/8», definitivo).
  - Correzioni nel riservato: dati/correzioni-aperte/<id quiz>.json  {"email": punti delle aperte da 0 a 4}. Con la correzione
    la cella diventa «NN% OK» oppure «NN% DA RECUPERARE» (punti/12).

CONTROLLO PRIVACY BLOCCANTE (R1), per ogni file prima di scriverlo: nessuna chiocciola; ogni Allievo e' «Nome I.»;
nessun cognome di allievo (generatori/privacy_nomi.py del riservato). Se non passa, il file NON viene scritto.

Uso:
    python3 -I strumenti/aggiorna_sicurezza_dati.py FABBRICA.xlsx [--esportato 2026-11-13T08:56:42+01:00]
Senza --esportato vale l'ora di modifica del file xlsx. L'xlsx NON va messo nel repository.
"""
import csv
import datetime
import glob
import hashlib
import io
import json
import os
import re
import sys
import unicodedata

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(QUI)
DEST = os.path.join(REPO, "docs", "cruscotto", "dati")
RIS = os.path.join(os.path.dirname(REPO), "corso-informatica-riservato")
CLASSI = ["1INF", "2INF"]
RE_ALLIEVO = re.compile(r"^[^\W\d_][\w'’-]*(?: [^\W\d_][\w'’-]*)* [^\W\d_]{1,2}\.(?: \(\d+\))?$")
# 2INF ore 6A e 6B: (punti delle chiuse, punti totali). Fonte: SOLUZIONI-2INF-SICUREZZA-ORA6-v1.0.md (riservato).
APERTE = {"quiz-2inf-sic6-mecc-1311": (8, 12), "quiz-2inf-sic6-elet-1311": (8, 12)}
SOGLIA = 80
# 2INF ore 1-4: cartelle del registro quiz nel riservato (come strumenti/sicurezza_2inf.py)
STORICO_2INF = {"Ora 1": "2inf-quiz-sicurezza1-20261001", "Ora 2": "2inf-quiz-sicurezza2-20261009",
                "Ora 3": "2inf-quiz-sicurezza3-20261021", "Ora 4": "2inf-quiz-sicurezza4-20261021"}


def carica_privacy():
    sys.path.insert(0, os.path.join(RIS, "generatori"))
    try:
        import privacy_nomi
    except Exception as e:  # noqa: BLE001
        print("STOP: controllo cognomi non possibile (riservato mancante: %s). Non pubblico nulla." % str(e)[:80])
        sys.exit(2)
    return privacy_nomi


def testo(v):
    if v is None:
        return ""
    if isinstance(v, float):
        return str(int(v)) if v == int(v) else repr(v)
    return str(v).strip()


def righe_foglio(ws):
    out = [[testo(c) for c in r] for r in ws.iter_rows(values_only=True)]
    while out and not any(out[-1]):
        out.pop()
    return out


def sha(s):
    return hashlib.sha256(s.upper().encode("utf-8")).hexdigest()


def norm(s):
    return "".join(c for c in unicodedata.normalize("NFKD", str(s)) if not unicodedata.combining(c)).upper()


def tok(s):
    return set(w for w in re.split(r"[^A-Z0-9]+", norm(s)) if len(w) > 2)


def nome_i_da_email(email):
    parti = [p for p in re.split(r"[._-]+", email.split("@")[0]) if p]
    if len(parti) < 2:
        return None
    return parti[0].capitalize(), parti[-1][0].upper()


def ora_riga1(riga0):
    m = re.search(r"(\d{1,2}):(\d{2}):(\d{2})", riga0)
    return "%02d:%s:%s" % (int(m.group(1)), m.group(2), m.group(3)) if m else None


def elenco_e_nomi(wb, c):
    """Ritorna (id_sha -> 'Nome I.', email_minuscola -> id_sha). Elenco e' privato: resta in memoria."""
    sit = righe_foglio(wb["Situazione pubblica " + c])
    hi = next(i for i, r in enumerate(sit) if len(r) > 1 and r[0] == "Stato" and r[1] == "Allievo")
    pubblici = [r[1] for r in sit[hi + 1:] if r and r[0] in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO")]
    el = righe_foglio(wb["Elenco " + c])[1:]
    id_nome, email_id, usati = {}, {}, set()
    for r in el:
        if len(r) < 2 or not r[0] or not r[1]:
            continue
        email, alli = r[0].lower(), r[1]
        ni = nome_i_da_email(email)
        cand = []
        if ni:
            cand = [p for p in pubblici if p.split(" (")[0].rsplit(" ", 1)[0].lower() == ni[0].lower()
                    and p.split(" (")[0].rsplit(" ", 1)[1].rstrip(".").upper().startswith(ni[1])]
        scelto = next((p for p in cand if p not in usati), None)
        if scelto is None:
            scelto = "%s %s." % ni if ni else "Allievo %d" % (len(id_nome) + 1)
        usati.add(scelto)
        id_nome[sha(alli)] = scelto
        email_id[email] = sha(alli)
    return id_nome, email_id, pubblici


def leggi_ris(wb, qid):
    """{email: {migliore, su, tentativi, ultimo, aperte}} dalla scheda «Ris <id>»; {} se manca."""
    nome = "Ris " + qid
    if nome not in wb.sheetnames:
        return {}, ""
    righe = righe_foglio(wb[nome])
    letto = ora_riga1(righe[1][0]) if len(righe) > 1 and righe[1] else ""
    hi = next((i for i, r in enumerate(righe) if r and r[0] == "Email"), None)
    out = {}
    if hi is None:
        return out, letto
    for r in righe[hi + 1:]:
        if not r or not r[0] or "@" not in r[0]:
            continue
        r = r + [""] * (6 - len(r))
        try:
            out[r[0].lower()] = dict(migliore=float(r[1]), su=float(r[2]), tentativi=int(float(r[3] or 0)), ultimo=r[4], aperte=float(r[5] or 0))
        except ValueError:
            continue
    return out, letto


def ultimo_key(s):
    m = re.match(r"^(\d{1,2})/(\d{1,2}) (\d{1,2}):(\d{2})$", s or "")
    return (int(m.group(2)), int(m.group(1)), int(m.group(3)), int(m.group(4))) if m else None


def correzioni(qid):
    f = os.path.join(RIS, "dati", "correzioni-aperte", qid + ".json")
    try:
        return {k.lower(): float(v) for k, v in json.load(open(f, encoding="utf-8")).items()}
    except (OSError, ValueError):
        return {}


def cella_aperte(qid, ris, corr):
    """Cella di un quiz con domande aperte (2INF 6A/6B). ris = riga Ris dell'allievo o None."""
    chiuse_max, tot = APERTE[qid]
    if not ris:
        return "MANCA"
    ch = ris["migliore"]
    if corr is not None:
        pts = ch + max(0.0, min(4.0, corr))
        pct = round(100 * pts / tot)
        return "%d%% %s" % (pct, "OK" if pct >= SOGLIA else "DA RECUPERARE")
    ap_max = tot - chiuse_max
    if (ch + ap_max) * 100 / tot >= SOGLIA:
        return "IN CORREZIONE chiuse %d/%d" % (round(ch), chiuse_max)
    return "DA RECUPERARE chiuse %d/%d (anche con le aperte al massimo non arriva a 10)" % (round(ch), chiuse_max)


def storico_2inf(email_id, id_nome, el_alli):
    """({id_sha: {'Ora k': pct}}, {'Ora k': 'gg/mm ultimo invio nel registro'}) dal registro quiz del riservato; email, poi nome per parole in comune."""
    out = {i: {} for i in id_nome}
    date = {}
    for ora, cart in STORICO_2INF.items():
        f = os.path.join(RIS, "dati", "verifiche", cart, "_RISULTATI-QUIZ.csv")
        if not os.path.exists(f):
            continue
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter=";"):
            if (r.get("ora") or "")[:10] > date.get(ora, ""):
                date[ora] = r["ora"][:10]
            sid = email_id.get((r.get("email") or "").lower())
            if sid is None:
                t = tok(r.get("nome", "") + " " + (r.get("email") or "").split("@")[0])
                best, bn = 0, None
                for i, alli in el_alli.items():
                    k = len(t & tok(alli))
                    if k > best:
                        best, bn = k, i
                sid = bn if best >= 2 else None
            if sid is None:
                continue
            try:
                pct = round(100 * int(r["punteggio"]) / int(r["massimo"]))
            except (ValueError, ZeroDivisionError):
                continue
            out[sid][ora] = max(out[sid].get(ora, -1), pct)
    return out, {k: "%s/%s" % (v[8:10], v[5:7]) for k, v in date.items()}


def controllo_privacy(righe, pn):
    guai = []
    t = "\n".join(c for r in righe for c in r)
    if "@" in t:
        guai.append("c'e' una chiocciola (email)")
    hi = next((i for i, r in enumerate(righe) if r and r[0] == "Stato"), None)
    for k, r in enumerate(righe[hi + 1:], start=hi + 2):
        if not RE_ALLIEVO.match(r[1]) and not re.match(r"^Allievo \d+$", r[1]):
            guai.append("riga %d: Allievo non e' in forma «Nome I.»" % k)
    trovati = pn.trova(t)
    if trovati:
        guai.append("cognome di un allievo nel testo (%s)" % ", ".join(sorted(set(trovati))))
    return guai


def scrivi_csv(percorso, righe):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    larg = max(len(r) for r in righe)
    for r in righe:
        w.writerow(r + [""] * (larg - len(r)))
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())


def classe(wb, c, indice, pn, esiti):
    sp = righe_foglio(wb["Sicurezza pubblica " + c])
    hi = next(i for i, r in enumerate(sp) if r and r[0] == "Stato" and r[1] == "Id")
    testa, corpo = sp[hi], [r + [""] * (len(sp[hi]) - len(r)) for r in sp[hi + 1:] if r and r[0]]
    dato = ora_riga1(sp[0][0]) or "?"
    id_nome, email_id, pubblici = elenco_e_nomi(wb, c)
    el_alli = {sha(r[1]): r[1] for r in righe_foglio(wb["Elenco " + c])[1:] if len(r) > 1 and r[1]}
    ore_idx = [i for i, h in enumerate(testa) if re.match(r"^Ora\s", h) or h.startswith("Recupero")]
    blocco = next((b for b in indice["sicurezza"] if b["classe"] == c), {"ore": [], "recupero": {}})
    ids_ora = {("Ora " + o["ora"]): o.get("ids", []) for o in blocco["ore"]}
    ids_ora["Recupero ore 1-5"] = blocco.get("recupero", {}).get("ids", [])
    # Moduli: risposte per allievo (ultimo invio) e domande aperte
    ris, letture, ultimo = {}, [], {}
    for h, ids in ids_ora.items():
        for qid in ids:
            d, letto = leggi_ris(wb, qid)
            ris[qid] = d
            if letto:
                letture.append("%s %s" % (h.replace("Ora ", ""), letto))
            for em, x in d.items():
                sid = email_id.get(em)
                k = ultimo_key(x["ultimo"])
                if sid and k and (sid not in ultimo or k > ultimo_key(ultimo[sid])):
                    ultimo[sid] = x["ultimo"]
    storico, date_st = storico_2inf(email_id, id_nome, el_alli) if c == "2INF" else ({}, {})
    righe_out, sconosciuti, n_storico = [], 0, 0
    for r in corpo:
        sid = r[1]
        nome = id_nome.get(sid)
        if nome is None:
            sconosciuti += 1
            nome = "Allievo %d" % (len(righe_out) + 1)
        celle = []
        for i in ore_idx:
            h, v = testa[i], r[i]
            qids = ids_ora.get(h, [])
            if c == "2INF" and len(qids) == 1 and qids[0] in APERTE:
                em = next((e for e, s in email_id.items() if s == sid), None)
                # vale la scheda Ris (letta dopo la scheda pubblica); senza riga Ris e' MANCA
                v = cella_aperte(qids[0], ris[qids[0]].get(em), correzioni(qids[0]).get(em))
            elif c == "2INF" and h in STORICO_2INF and v.lower().startswith("dato non importato"):
                p = storico.get(sid, {}).get(h)
                n_storico += 1
                v = ("%d%% %s" % (p, "OK" if p >= SOGLIA else "DA RECUPERARE")) if p is not None else "MANCA"
            celle.append(v)
        righe_out.append((nome, celle, ultimo.get(sid, "")))
    # ordine stabile: per nome
    righe_out.sort(key=lambda x: x[0].lower())
    # stato riassuntivo
    def stato(celle):
        if any(x.startswith("MANCA") or x.startswith("DA RECUPERARE") or re.match(r"^\d+% DA RECUPERARE", x) for x in celle):
            return "ROSSO"
        if any(x.startswith("IN CORREZIONE") or x.lower().startswith("dato non") for x in celle):
            return "ND"
        return "VERDE"
    intest = ["Stato", "Allievo"] + [testa[i] for i in ore_idx] + ["Ultimo invio"]
    out = [["%s · Sicurezza (pubblica, solo Nome I.) · dati letti alle %s · %s" % (c, dato, "esportati dal foglio Fabbrica")],
           ["Soglia %d%% sul miglior tentativo. «NN%% OK» = %d%% o piu · «NN%% DA RECUPERARE» = sotto · MANCA = nessuna risposta · IN CORREZIONE = ci sono domande aperte non ancora corrette, la percentuale e provvisoria · dato non importato = ora senza dato nel foglio." % (SOGLIA, SOGLIA)],
           ["Fonti: scheda «Sicurezza pubblica %s» (motore, %s) · schede Ris dei Moduli (%s)%s" % (
               c, dato, "; ".join(letture) or "nessuna", (" · ore 1-4: registro dei quiz del docente nel riservato, ultimo invio per ora: %s (%d celle)" % (", ".join("%s %s" % (k.replace("Ora ", ""), v) for k, v in sorted(date_st.items())), n_storico)) if n_storico else "")],
           intest]
    for nome, celle, ult in righe_out:
        out.append([stato(celle), nome] + celle + [ult])
    return out, dato, sconosciuti, letture, n_storico


def link_quiz(wb, indice):
    es = righe_foglio(wb["Esiti"])
    url = {r[1]: r[3] for r in es[1:] if len(r) > 3 and r[3].startswith("https://docs.google.com/forms/")}
    tit = {r[1]: r[2] for r in es[1:] if len(r) > 2}
    out = {}
    for b in indice["sicurezza"]:
        c = b["classe"]
        out[c] = {}
        for o in b["ore"]:
            ids = o.get("ids", [])
            vivi = [i for i in ids if i in url]
            if len(vivi) == 1:      # con due versioni non si presume quale sia quella data ai ragazzi (R7.6)
                out[c]["Ora " + o["ora"]] = {"id": vivi[0], "titolo": tit.get(vivi[0], ""), "url": url[vivi[0]]}
    return out


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 1
    xlsx = argv[1]
    if "--esportato" in argv:
        esportato = datetime.datetime.fromisoformat(argv[argv.index("--esportato") + 1])
    else:
        esportato = datetime.datetime.fromtimestamp(os.path.getmtime(xlsx)).astimezone()
    pn = carica_privacy()
    import openpyxl
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    indice = json.load(open(os.path.join(REPO, "fabbrica", "indice.json"), encoding="utf-8"))
    os.makedirs(DEST, exist_ok=True)
    mp = os.path.join(DEST, "meta.json")
    meta = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {"classi": {}}
    brutto = 0
    for c in CLASSI:
        f = os.path.join(DEST, "%s-sicurezza.csv" % c)
        if "Sicurezza pubblica " + c not in wb.sheetnames:
            print("ATTENZIONE %s: scheda «Sicurezza pubblica %s» non trovata" % (c, c))
            continue
        righe, dato, sconosciuti, letture, n_st = classe(wb, c, indice, pn, None)
        guai = controllo_privacy(righe, pn)
        if sconosciuti:
            guai.append("%d Id senza nome in elenco" % sconosciuti)
        if guai:
            print("ATTENZIONE %s sicurezza: NON pubblicato, %s" % (c, "; ".join(guai)))
            if os.path.exists(f):
                os.remove(f)
            meta.setdefault("classi", {}).setdefault(c, {})["sicurezza"] = False
            brutto = 3
            continue
        scrivi_csv(f, righe)
        # ora del dato = riga 1 della scheda (data = giorno dell'export in ora italiana)
        giorno = esportato.astimezone(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat()
        meta.setdefault("classi", {}).setdefault(c, {})["sicurezza"] = True
        meta["classi"][c]["sicurezza_dato"] = "%sT%s+01:00" % (giorno, dato)
        print("%s sicurezza: scritto (%d allievi, dato del motore %s, storico %d celle)" % (c, len(righe) - 4, dato, n_st))
    lk = link_quiz(wb, indice)
    t = json.dumps(lk, ensure_ascii=False, indent=1)
    if "@" in t or pn.trova(t):
        print("ATTENZIONE link: NON scritti (privacy)")
        brutto = 3
    else:
        with open(os.path.join(DEST, "sicurezza-link.json"), "w", encoding="utf-8") as fh:
            fh.write(t + "\n")
    meta["esportato"] = esportato.isoformat(timespec="seconds")
    with open(mp, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("meta.json: esportato %s" % meta["esportato"])
    return brutto


if __name__ == "__main__":
    sys.exit(main(sys.argv))
