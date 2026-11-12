#!/usr/bin/env python3
"""Aggiorna i dati di riserva del cruscotto (docs/cruscotto/dati/). Versione 1.0 (12/11/2026).

Da un file xlsx esportato dal foglio Fabbrica produce, per ogni classe:
    docs/cruscotto/dati/<CLASSE>-situazione.csv   da la scheda «Situazione pubblica <CLASSE>»
    docs/cruscotto/dati/<CLASSE>-consegne.csv     da la scheda «Consegne pubblica <CLASSE>» (se esiste)
    docs/cruscotto/dati/meta.json                 ora vera dell'export (Europe/Rome) e classi scritte

Si leggono SOLO le schede «... pubblica ...» (gia' solo «Nome I.»). Le schede con i cognomi
(«Situazione <CLASSE>», «Consegne <CLASSE>») non si aprono mai.

CONTROLLO PRIVACY BLOCCANTE (R1), per ogni file prima di scriverlo:
  1. nessuna email (nessuna chiocciola);
  2. ogni cella della colonna Allievo e' «Nome I.» (nome piu' una o due lettere con il punto) oppure «Allievo n»;
  3. nessun cognome di allievo, cercato con generatori/privacy_nomi.py del riservato su tutto il testo.
Se il riservato non e' clonato accanto il controllo non si puo' fare e lo script SI FERMA.
Un file che non passa NON viene scritto (e un vecchio file della stessa classe viene tolto): le altre classi vanno avanti.

Uso:
    python3 -I strumenti/aggiorna_cruscotto_dati.py FABBRICA.xlsx [--esportato 2026-11-12T10:43:48+01:00]
Senza --esportato vale l'ora di modifica del file xlsx (cioe' l'ora dell'export).
Il file xlsx NON va messo nel repository (e' un export con dati di tutta la scuola): si tiene fuori.
"""
import csv
import datetime
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(QUI)
DEST = os.path.join(REPO, "docs", "cruscotto", "dati")
RISERVATO = os.path.join(os.path.dirname(REPO), "corso-informatica-riservato", "generatori")
CLASSI = ["1INF", "2INF", "3INF", "4TI"]
RE_ALLIEVO = re.compile(r"^[^\W\d_][\w'’-]*(?: [^\W\d_][\w'’-]*)* [^\W\d_]{1,2}\.$")
RE_ALLIEVO_N = re.compile(r"^Allievo \d+$")


def carica_privacy():
    sys.path.insert(0, RISERVATO)
    try:
        import privacy_nomi
    except Exception as e:  # noqa: BLE001
        print("STOP: controllo cognomi non possibile (riservato mancante: %s). Non pubblico nulla." % str(e)[:80])
        sys.exit(2)
    return privacy_nomi


def testo_cella(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        return str(int(v)) if v == int(v) else repr(v)
    if isinstance(v, (datetime.datetime, datetime.date)):
        return "%d/%d" % (v.day, v.month)   # Excel ha letto «1/4» come 1 aprile: si ricalcola dopo
    return str(v)


def righe_foglio(ws):
    out = [[testo_cella(c) for c in r] for r in ws.iter_rows(values_only=True)]
    while out and not any(x.strip() for x in out[-1]):
        out.pop()
    for r in out:
        while r and not r[-1].strip():
            r.pop()
    return out


def ripara_situazione(righe):
    """Fatti / totali (data scambiata da Excel) e Media (numero 0-1) come li da Google: «3/4» e «88%»."""
    hi = next((i for i, r in enumerate(righe) if len(r) > 1 and r[0].strip() == "Stato" and r[1].strip() == "Allievo"), None)
    if hi is None:
        raise ValueError("intestazione «Stato / Allievo» non trovata")
    head = righe[hi]
    fi = next((i for i, h in enumerate(head) if re.match(r"^Fatti\s*/\s*totali", h)), None)
    if fi is None:
        return righe, 0
    mi = next((i for i, h in enumerate(head) if h.startswith("Media")), None)
    ntot = fi - 2
    toccate = 0
    for r in righe[hi + 1:]:
        if r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        r += [""] * (len(head) - len(r))
        fatti = sum(1 for x in r[2:fi] if re.match(r"^\d+%\s*\(", x.strip()))
        nuovo = "%d/%d" % (fatti, ntot)
        if r[fi] != nuovo:
            toccate += 1
        r[fi] = nuovo
        if mi is not None and re.match(r"^\d*\.?\d+$", r[mi].strip()) and r[mi].strip() not in ("0", ""):
            v = float(r[mi])
            if 0 < v <= 1:
                r[mi] = "%d%%" % round(v * 100)
    return righe, toccate


def controllo_privacy(nome_file, righe, pn):
    """Ritorna l'elenco dei problemi (vuoto = passa). Non stampa mai i cognomi nei file."""
    guai = []
    testo = "\n".join(c for r in righe for c in r)
    if "@" in testo:
        guai.append("c'e' una chiocciola (email)")
    hi = next((i for i, r in enumerate(righe) if len(r) > 1 and r[0].strip() == "Stato" and r[1].strip() == "Allievo"), None)
    if hi is None:
        guai.append("intestazione Stato/Allievo non trovata")
        return guai
    if any(h.strip().lower() == "email" for h in righe[hi]):
        guai.append("c'e' una colonna Email")
    for k, r in enumerate(righe[hi + 1:], start=hi + 2):
        if r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        a = (r[1] if len(r) > 1 else "").strip()
        if not (RE_ALLIEVO.match(a) or RE_ALLIEVO_N.match(a)):
            guai.append("riga %d: Allievo non e' in forma «Nome I.»" % k)
    trovati = pn.trova(testo)
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


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 1
    xlsx = argv[1]
    esportato = None
    if "--esportato" in argv:
        esportato = datetime.datetime.fromisoformat(argv[argv.index("--esportato") + 1])
    else:
        esportato = datetime.datetime.fromtimestamp(os.path.getmtime(xlsx)).astimezone()
    pn = carica_privacy()
    import openpyxl
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    os.makedirs(DEST, exist_ok=True)
    scritti, saltati = {}, []
    for c in CLASSI:
        scritti[c] = {"situazione": False, "consegne": False}
        for tipo, scheda in (("situazione", "Situazione pubblica " + c), ("consegne", "Consegne pubblica " + c)):
            file_csv = os.path.join(DEST, "%s-%s.csv" % (c, tipo))
            if scheda not in wb.sheetnames:
                if tipo == "situazione":
                    saltati.append("%s: scheda «%s» non trovata" % (c, scheda))
                if os.path.exists(file_csv):
                    os.remove(file_csv)
                continue
            righe = righe_foglio(wb[scheda])
            if tipo == "situazione":
                righe, n = ripara_situazione(righe)
                if n:
                    print("%s: ricalcolato «Fatti / totali» in %d righe (Excel lo leggeva come data)" % (c, n))
            guai = controllo_privacy(scheda, righe, pn)
            if guai:
                saltati.append("%s %s: NON pubblicato, %s" % (c, tipo, "; ".join(guai)))
                if os.path.exists(file_csv):
                    os.remove(file_csv)
                continue
            scrivi_csv(file_csv, righe)
            scritti[c][tipo] = True
            print("%s %s: scritto (%d righe)" % (c, tipo, len(righe)))
    meta = {"esportato": esportato.isoformat(timespec="seconds"),
            "fonte": "foglio Fabbrica, schede pubbliche, esportato dall'assistente",
            "classi": scritti}
    with open(os.path.join(DEST, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
        f.write("\n")
    for s in saltati:
        print("ATTENZIONE " + s)
    print("meta.json: esportato %s" % meta["esportato"])
    return 3 if saltati else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
