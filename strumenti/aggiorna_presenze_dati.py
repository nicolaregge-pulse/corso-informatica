#!/usr/bin/env python3
"""Presenze del giorno per il cruscotto (docs/cruscotto/dati/<CLASSE>-presenze.json). Versione 1.0 (13/11/2026).

Decisione del docente (13/11/2026): la presenza o l'assenza di una lezione e' un dato PUBBLICO, come «Nome I.».
Restano nel riservato: nomi completi, voti dettagliati, note e MOTIVI delle assenze.

Legge dal riservato il file piu' recente  dati/<classe>-presenze-AAAAMMGG-HHMM.json  (COGNOME Nome, fonte, ora; vedi il file di esempio)
e scrive nel pubblico SOLO:  classe, giorno, ora del dato, fonte, ordine alfabetico del registro (per cognome) come «Nome I.»,
elenco presenti e assenti come «Nome I.». Nessun cognome, nessun motivo, nessuna nota.

CONTROLLO PRIVACY BLOCCANTE (R1) prima di scrivere: ogni voce in forma «Nome I.», nessuna chiocciola, nessun cognome noto
(generatori/privacy_nomi.py del riservato). Un file che non passa NON viene scritto (esito 3).

I COGNOME Nome NON escono mai da qui: la versione con i cognomi e' un file HTML del solo riservato (generatori/cruscotto_docente.py).

Uso (dalla cartella del repository pubblico):
    python3 -I strumenti/aggiorna_presenze_dati.py [CLASSE ...] [--file /percorso/del/riservato.json]
Senza argomenti: tutte le classi per cui nel riservato c'e' un file di presenze. Esiti: 0 ok (anche «niente da fare»), 2 errore, 3 file non passato.
"""
import glob
import json
import os
import re
import sys
import unicodedata

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import aggiorna_cruscotto_dati as base  # noqa: E402

DEST = os.environ.get("CRUSCOTTO_DEST") or base.DEST
RIS_DATI = os.path.normpath(os.path.join(os.path.dirname(base.RISERVATO), "dati"))


def chiave(s):
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c)).upper().split()


def piu_recente(classe):
    fs = sorted(glob.glob(os.path.join(RIS_DATI, "%s-presenze-[0-9]*-[0-9]*.json" % classe.lower())))
    return fs[-1] if fs else None


def scrivi_classe(classe, percorso, pn):
    d = json.load(open(percorso, encoding="utf-8"))
    pres, ass = d.get("presenti") or [], d.get("assenti") or []
    if not pres and not ass:
        print("%s: file senza presenti e senza assenti: salto." % classe)
        return 2
    registro = sorted(pres + ass, key=chiave)          # ordine del registro: per COGNOME (il cognome e' la prima parola)
    nb = {x: pn.nome_c(x) for x in registro}
    ora = str(d.get("ora_dato") or "")
    giorno = str(d.get("giorno") or "")
    out = {
        "versione": "1.0",
        "classe": classe,
        "giorno": giorno,
        "ora_dato": ora,
        "dato": "%sT%s:00+01:00" % (giorno, ora) if re.fullmatch(r"\d{2}:\d{2}", ora) and giorno else None,
        "fonte": "registro DIDAweb, letto dal docente (presenza = dato pubblico come Nome I.)",
        "n_iscritti": len(registro),
        "ordine": [nb[x] for x in registro],
        "presenti": [nb[x] for x in sorted(pres, key=chiave)],
        "assenti": [nb[x] for x in sorted(ass, key=chiave)],
    }
    testo = json.dumps(out, ensure_ascii=False, indent=1)
    guai = []
    if "@" in testo:
        guai.append("chiocciola")
    for v in out["ordine"]:
        if not base.RE_ALLIEVO.match(v):
            guai.append("voce non in forma «Nome I.»")
    if len(set(out["ordine"])) != len(out["ordine"]):
        guai.append("due allievi con lo stesso «Nome I.»: serve un'iniziale in piu'")
    if pn.trova(testo):
        guai.append("cognome di un allievo nel testo")
    if guai:
        print("%s: NON scritto, controllo privacy: %s" % (classe, "; ".join(sorted(set(guai)))))
        return 3
    os.makedirs(DEST, exist_ok=True)
    dest = os.path.join(DEST, "%s-presenze.json" % classe)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(testo + "\n")
    print("%s: scritto %s (presenti %d, assenti %d, dato %s %s)" % (classe, os.path.relpath(dest), len(pres), len(ass), giorno, ora))
    return 0


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    forzato = argv[argv.index("--file") + 1] if "--file" in argv else None
    if forzato:
        args = [a for a in args if a != forzato]
    classi = [a.upper() for a in args] or list(base.CLASSI)
    pn = base.carica_privacy()
    esito = 0
    for c in classi:
        p = forzato or piu_recente(c)
        if not p:
            print("%s: nessun file di presenze nel riservato: niente da fare." % c)
            continue
        esito = max(esito, scrivi_classe(c, p, pn))
    return esito


if __name__ == "__main__":
    sys.exit(main(sys.argv))
