"""Privacy dei nomi (28/10/2026): importare questo modulo in ogni script che scrive pagine o dati pubblici.

Se il repository riservato è clonato accanto, carica il suo generatori/privacy_nomi.py: da quel momento ogni
file scritto dentro questo repository (tranne i cifrati, il codice e .git) esce con i ragazzi come «Nome C.»
(link e nomi utente GitHub restano intatti, 28/10/2026). Se il riservato manca non fa niente (i cognomi
non sono in questo repository, quindi non c'è niente da togliere).

Uso, nella prima riga degli import:
    import privacy_pubblico  # noqa: F401
"""
import os
import sys

RISERVATO = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                         "corso-informatica-riservato", "generatori")
ATTIVO = False
try:
    if os.path.exists(os.path.join(RISERVATO, "privacy_nomi.py")):
        if RISERVATO not in sys.path:
            sys.path.append(RISERVATO)
        import privacy_nomi  # noqa: F401
        ATTIVO = True
except Exception as e:   # la privacy non deve mai fermare un generatore: lo dice e va avanti
    print("privacy_pubblico: controllo dei nomi non attivo (" + str(e)[:80] + ")", file=sys.stderr)


# ---------------------------------------------------------------------------------------------------------------------------
# CONTROLLO «NESSUN NUMERO PER ALLIEVO» (15/11/2026, decisione del docente, R1). Si lancia da riga di comando:
#     python3 -I strumenti/privacy_pubblico.py          esito 0 = nessun numero per allievo nei file pubblici del cruscotto; esito 1 = trovati (elencati)
# Controlla docs/cruscotto/dati/*.csv e *.json, docs/cruscotto/completo/*.html: una riga/oggetto di un «Nome I.» non deve avere
# percentuali, punti (x/y), «chiuse x/y», colonne «Media», voti, punti per domanda. I conteggi (fatti 4/11) e le fasce (OK / DA RIVEDERE) restano.
# ---------------------------------------------------------------------------------------------------------------------------
import csv as _csv
import json as _json
import re as _re

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CRU = os.path.join(_REPO, "docs", "cruscotto")
_RE_ALL = _re.compile(r"^[^\W\d_][\w'’-]*(?: [^\W\d_][\w'’-]*)* [^\W\d_]{1,2}\.(?: \(\d+\))?$")
_RE_NUM = _re.compile(r"^\s*\d+\s*%|chiuse\s+\d+\s*/\s*\d+|\d+\s*/\s*\d+\s*(?:pt|punti)\b", _re.I)   # cella che INIZIA con una percentuale, «chiuse x/y», «x/y punti»; le date dei titoli «(11/11)» e i conteggi «4/11» non contano
_CHIAVI_JSON = {"pct", "mg", "su", "domande", "media", "voto_proposto", "punti", "punteggio"}


def _csv_numeri(percorso):
    guai = []
    with open(percorso, encoding="utf-8", newline="") as f:
        righe = list(_csv.reader(f))
    for i, r in enumerate(righe, 1):
        if len(r) > 1 and r[0].strip() in ("Stato",) and r[1].strip() == "Allievo":
            for h in r:
                if h.strip().lower().startswith(("media", "voto")):
                    guai.append("%s: colonna «%s» (numero per allievo)" % (os.path.basename(percorso), h.strip()[:30]))
        elif len(r) > 1 and _RE_ALL.match(r[1].strip()):
            for c in r[2:]:
                if _RE_NUM.search(c):
                    guai.append("%s riga %d: cella con un numero («%s»)" % (os.path.basename(percorso), i, c.strip()[:30]))
                    break
    return guai


def _json_numeri(percorso):
    guai = []
    d = _json.load(open(percorso, encoding="utf-8"))

    def giu(x, dentro_allievo):
        if isinstance(x, dict):
            for k, v in x.items():
                if dentro_allievo and k in _CHIAVI_JSON:
                    guai.append("%s: chiave «%s» per allievo" % (os.path.basename(percorso), k))
                if k == "voto" and isinstance(v, (int, float)) and not isinstance(v, bool):
                    guai.append("%s: un voto numerico" % os.path.basename(percorso))
                giu(v, dentro_allievo or k == "allievi")
        elif isinstance(x, list):
            for v in x:
                giu(v, dentro_allievo)
    giu(d, False)
    return sorted(set(guai))


def _html_numeri(percorso):
    guai = []
    t = open(percorso, encoding="utf-8").read()
    for riga in _re.findall(r"<tr[^>]*>.*?</tr>", t, _re.S):
        celle = [_re.sub(r"<[^>]+>", " ", c).strip() for c in _re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", riga, _re.S)]
        if celle and _RE_ALL.match(celle[0]) and any(_RE_NUM.search(c) for c in celle[1:]):
            guai.append("%s: riga di «%s» con un numero" % (os.path.basename(percorso), celle[0][:20]))
    return guai


def controlla_numeri():
    guai = []
    for sotto, fn, est in (("dati", _csv_numeri, ".csv"), ("dati", _json_numeri, ".json"), ("completo", _html_numeri, ".html"), ("lezione-16-11", _html_numeri, ".html")):
        cart = os.path.join(_CRU, sotto)
        if not os.path.isdir(cart):
            continue
        for nome in sorted(os.listdir(cart)):
            if nome.endswith(est):
                try:
                    guai += fn(os.path.join(cart, nome))
                except Exception as e:  # noqa: BLE001
                    guai.append("%s: illeggibile (%s)" % (nome, str(e)[:60]))
    return guai


if __name__ == "__main__":
    _g = controlla_numeri()
    if _g:
        print("privacy_pubblico: TROVATI numeri per allievo nei file pubblici (%d):" % len(_g))
        for _x in _g[:30]:
            print("  - " + _x)
        sys.exit(1)
    print("privacy_pubblico: OK, nessun numero per allievo nei file pubblici del cruscotto (dati/*.csv, dati/*.json, completo/*.html).")
    sys.exit(0)
