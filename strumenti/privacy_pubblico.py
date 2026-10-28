"""Privacy dei nomi (28/10/2026): importare questo modulo in ogni script che scrive pagine o dati pubblici.

Se il repository riservato è clonato accanto, carica il suo generatori/privacy_nomi.py: da quel momento ogni
file scritto dentro questo repository (tranne i cifrati, il codice e .git) esce con i ragazzi come «Nome C.»
e senza link o nomi utente con il cognome attaccato. Se il riservato manca non fa niente (i cognomi
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
