#!/usr/bin/env python3
"""Hook UserPromptSubmit: a ogni messaggio del docente aggiunge come contesto
per Claude il promemoria breve .claude/promemoria-errori.md (errori che si
ripetono di più, dal REGISTRO-ERRORI-CLAUDE.md).

Robusto: se qualcosa va storto esce 0 senza output (la sessione non si rompe).
"""
import glob
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from zoneinfo import ZoneInfo

# v1.3 (18/11/2026 sera): al primo messaggio umano del giorno si ordina anche di seguire, PRIMA di rispondere nel merito,
# report/PROCEDURA-MATTINA-<ultima versione>.md del riservato (percorso completo, versione più alta trovata sul disco;
# CORSO_RISERVATO sposta la cartella per le prove). Nessuna scrittura, nessun trigger.
# v1.8 (19/11/2026): punta a INFO-PIU-USATE-v1.7.md (sezione 15, il kit comprende anche il PDF lavagna).
# v1.6 (19/11/2026): punta a INFO-PIU-USATE-v1.5.md (sezione 11, ora della nota). v1.7 (19/11/2026): punta a INFO-PIU-USATE-v1.6.md (quiz in autonomia, bobina).
# v1.5 (19/11/2026): punta a INFO-PIU-USATE-v1.4.md (sezione 11, 5 dati per ora).
# v1.4 (19/11/2026): punta a INFO-PIU-USATE-v1.3.md (sezione «Prima di consegnare un kit», errore #376).
# v1.3 (19/11/2026): punta a INFO-PIU-USATE-v1.3.md (voce «Come si crea un quiz», errore #375).
# v1.2 (18/11/2026): il segnale «primo messaggio del giorno» lo consuma solo un messaggio UMANO (non i prompt di
# trigger/routine, es. la notte delle 00:09); i file BOZZA sono esclusi; percorso completo di didaweb-auto.js.
# v1.1 (18/11/2026): aggiunte INFO-PIU-USATE e COSE-DA-FARE del giorno (audit del meccanismo sera/mattino).
# Rilettura del mattino (errore #350, 17/11/2026): al primo messaggio di ogni giornata si chiede di rileggere
# i documenti prima di lavorare. Stato: un file per giorno nella cartella temporanea (CORSO_STATO_RILETTURA="" la spegne).
RILETTURA = (
    "RILETTURA DEL MATTINO (primo messaggio di oggi, %s; regola del docente, errore #350): prima di fare QUALSIASI "
    "cosa rileggi per intero: CLAUDE.md, GUIDA-MESSAGGI-AL-DOCENTE.md, CHECKLIST-LEZIONE.md e la guida dei segnalibri "
    "DIDAweb (docs/docenti/02-didaweb-i-segnalibri-che-scrivono-i-voti.html, con /home/user/corso-informatica-riservato/strumenti/didaweb-auto.js). Le "
    "modalità già decise dal docente (per esempio i voti DIDAweb col segnalibro «Voti DIDAweb AUTO» e il pacchetto; "
    "il codice da copiare in UN riquadro da solo in FONDO, R4 3ter) NON si cambiano: se un metodo esiste già, si usa "
    "quello. PRIMA di dare passi al docente leggi anche /home/user/corso-informatica-riservato/report/INFO-PIU-USATE-v1.7.md "
    "(o l'ultima versione presente in report/) e, se esiste, il file delle cose da fare di oggi: il più recente tra "
    "/home/user/corso-informatica-riservato/report/*/COSE-DA-FARE-<GG-MM di oggi>*.md, ESCLUSI i file con BOZZA nel nome, versione più alta (-vN.N; senza versione = v1.0) o, a parità, la più recente per data (lo scrive la sera prima il "
    "controllore di fine giornata; se manca, dillo nella riga). Poi dici in una riga di averle rilette e quante cose "
    "bloccanti ci sono oggi."
)


RISERVATO = "/home/user/corso-informatica-riservato"

PROCEDURA = (
    " PROCEDURA DEL MATTINO (v1.3): PRIMA di rispondere nel merito esegui, passo per passo (A rilettura, B ultimi 3 giorni, "
    "C orario di oggi, D file PROPOSTE-CLASSROOM, E una sola schermata al docente), la procedura scritta in %s. "
    "Usi solo Read, Grep e Write; non pubblichi nulla (R2) e non sviluppi finché il docente non sceglie."
)
PROCEDURA_MANCA = (
    " PROCEDURA DEL MATTINO: il file report/PROCEDURA-MATTINA-v*.md non si trova in %s/report/: dillo in una riga "
    "e rileggi i documenti come sopra."
)


def ultima_procedura(base=None):
    """Percorso completo dell'ultima versione di report/PROCEDURA-MATTINA-vN.N.md (versione più alta), o None."""
    base = base if base is not None else (os.environ.get("CORSO_RISERVATO") or RISERVATO)
    migliore = None
    for f in glob.glob(os.path.join(base, "report", "PROCEDURA-MATTINA-v*.md")):
        m = re.search(r"-v(\d+)\.(\d+)\.md$", f)
        if m:
            v = (int(m.group(1)), int(m.group(2)))
            if migliore is None or v > migliore[0]:
                migliore = (v, f)
    return migliore[1] if migliore else None


def frase_procedura():
    p = ultima_procedura()
    if p:
        return PROCEDURA % p
    return PROCEDURA_MANCA % (os.environ.get("CORSO_RISERVATO") or RISERVATO)


# Segni dei prompt NON umani (trigger, routine, notifiche, sub-agenti), visti nelle bobine reali del 18/11:
# il trigger arriva come «<task-notification> ... scheduled trigger ... ReadNotifications».
SEGNI_AUTOMATICI = (
    "<task-notification", "queued-remote-notifications", "scheduled trigger", "fired by routine",
    "<wake", "<child-session-event", "<webhook-payload", "<event source=",
)
PREFISSI_AUTOMATICI = (
    "promemoria", "controllo di fine giornata", "preparazione notturna",
)


def messaggio_automatico(prompt):
    """True se il prompt viene da un trigger/routine e non dal docente."""
    if not isinstance(prompt, str):
        return False
    p = prompt.strip().lower()
    if p.startswith(PREFISSI_AUTOMATICI):
        return True
    return any(x in p[:2000] for x in SEGNI_AUTOMATICI)


def prima_volta_oggi():
    stato = os.environ.get("CORSO_STATO_RILETTURA")
    if stato == "":
        return None
    oggi = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d")
    path = stato or os.path.join(tempfile.gettempdir(), "corso-rilettura-mattino.txt")
    try:
        with open(path, encoding="utf-8") as f:
            if f.read().strip() == oggi:
                return None
    except Exception:
        pass
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(oggi)
    except Exception:
        return None
    return oggi


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    base = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or ""
    candidati = [
        os.path.join(base, ".claude", "promemoria-errori.md"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "promemoria-errori.md"),
    ]
    testo = ""
    for p in candidati:
        try:
            with open(p, encoding="utf-8") as f:
                testo = f.read().strip()
            if testo:
                break
        except Exception:
            continue
    try:
        oggi = None if messaggio_automatico(data.get("prompt")) else prima_volta_oggi()
        if oggi:
            testo = (RILETTURA % oggi) + frase_procedura() + "\n\n" + testo
    except Exception:
        pass
    if not testo:
        return
    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": testo,
        }
    }
    sys.stdout.write(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
