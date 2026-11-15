"""Fascia al posto del numero (v1.0, 15/11/2026; decisione del docente, R1): nel PUBBLICO per ogni «Nome I.» restano lo stato
(fatto / manca / in correzione) e una fascia «OK» (miglior tentativo a 80% o piu) o «DA RIVEDERE» (sotto 80%), SENZA numero:
niente percentuale, niente punti, niente voto proposto, niente punti per domanda. I numeri per allievo stanno solo nel RISERVATO
(dati/cruscotto-pieno/, usato dalla versione docente con i COGNOME).

Funzioni:
    pubblica_situazione(righe)  -> righe della «Situazione pubblica» senza numeri per allievo (celle quiz -> OK / DA RIVEDERE, colonna Media tolta)
    pubblica_sicurezza(righe)   -> righe della Sicurezza: «71% DA RECUPERARE» -> «DA RECUPERARE», «IN CORREZIONE chiuse 8/8» -> «IN CORREZIONE»
    fascia_da_pct(p)            -> «OK» / «DA RIVEDERE»
    scrivi_pieno(nome_file, testo) scrive la copia con i numeri nel riservato (se c'e')
"""
import os
import re

SOGLIA = 80
QUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(QUI)
PIENO = os.path.join(os.path.dirname(REPO), "corso-informatica-riservato", "dati", "cruscotto-pieno")
RE_Q = re.compile(r"^(\d+)%\s*\((\d+)/(\d+)\)(.*)$")
RE_STATI = ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO")


def fascia_da_pct(p):
    return "OK" if p >= SOGLIA else "DA RIVEDERE"


def _coda(t):
    """di cio' che segue «NN% (x/y)» tiene solo le parole (provv., versione precedente), mai cifre"""
    return re.sub(r"[\d%/]+", "", t or "").replace("()", "").rstrip()


def cella_quiz(c):
    m = RE_Q.match((c or "").strip())
    if not m:
        return c
    return fascia_da_pct(int(m.group(1))) + _coda(m.group(4))


def _testa(righe):
    return next((i for i, r in enumerate(righe) if len(r) > 1 and r[0].strip() == "Stato" and r[1].strip() == "Allievo"), None)


def pubblica_situazione(righe):
    righe = [list(r) for r in righe]
    hi = _testa(righe)
    if hi is None:
        raise ValueError("intestazione «Stato / Allievo» non trovata")
    head = righe[hi]
    fi = next((i for i, h in enumerate(head) if re.match(r"^Fatti\s*/\s*totali", h)), len(head))
    mi = next((i for i, h in enumerate(head) if h.strip().startswith("Media")), None)
    for r in righe[hi + 1:]:
        if r[0].strip() not in RE_STATI:
            break
        for j in range(2, min(fi, len(r))):
            r[j] = cella_quiz(r[j])
    if mi is not None:                       # la media per allievo e' un numero per allievo: fuori dal pubblico
        for r in righe:
            if len(r) > mi and (r is head or (r[0].strip() in RE_STATI)):
                del r[mi]
    for r in righe[:hi]:                     # legenda: niente piu' «miglior punteggio in %»
        if r and r[0].startswith("Cella = miglior punteggio"):
            t = r[0]
            t = t.replace("Cella = miglior punteggio in % (punti/totale) di tutti i tentativi.",
                          "Cella = fascia del miglior tentativo: OK = 80% o più, DA RIVEDERE = sotto 80%. Nessun numero per allievo: i punteggi stanno solo nella versione riservata del docente.")
            t = t.replace("Verde = 80% o più, giallo = sotto 80%, ", "")
            t = re.sub(r"\(provv\.\) = ci sono domande aperte non ancora corrette: la percentuale può cambiare\. Media = solo sui quiz fatti\.",
                       "(provv.) = ci sono domande aperte non ancora corrette: la fascia può cambiare.", t)
            r[0] = t
        if r and r[0].startswith("Cella = fascia"):
            r[0] = re.sub(r"Media = solo sui quiz fatti\.\s*", "", r[0])
    return righe


def pubblica_sicurezza(righe):
    righe = [list(r) for r in righe]
    hi = _testa(righe)
    if hi is None:
        raise ValueError("intestazione Sicurezza non trovata")
    for r in righe[hi + 1:]:
        if r[0].strip() not in RE_STATI:
            break
        for j in range(2, len(r)):
            x = r[j].strip()
            m = re.match(r"^\d+%\s+(OK|DA RECUPERARE)\b", x)
            if m:
                r[j] = m.group(1)
            elif re.match(r"^IN CORREZIONE", x):
                r[j] = "IN CORREZIONE"
            elif re.match(r"^DA RECUPERARE chiuse", x):
                r[j] = "DA RECUPERARE"
    for r in righe[:hi]:
        if r and r[0].startswith("Soglia "):
            r[0] = ("Soglia 80% sul miglior tentativo. OK = 80% o più · DA RECUPERARE = sotto · MANCA = nessuna risposta · "
                    "IN CORREZIONE = ci sono domande aperte non ancora corrette · dato non importato = ora senza dato nel foglio. "
                    "Nessun numero per allievo: i punteggi stanno solo nella versione riservata del docente.")
    return righe


def scrivi_pieno(nome_file, testo):
    """copia CON i numeri, solo nel riservato (se non e' clonato accanto non fa niente)"""
    try:
        if not os.path.isdir(os.path.dirname(PIENO)):
            return False
        os.makedirs(PIENO, exist_ok=True)
        with open(os.path.join(PIENO, nome_file), "w", encoding="utf-8", newline="") as f:
            f.write(testo)
        return True
    except OSError:
        return False
