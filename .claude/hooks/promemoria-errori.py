#!/usr/bin/env python3
"""Hook UserPromptSubmit: a ogni messaggio del docente aggiunge come contesto
per Claude il promemoria breve .claude/promemoria-errori.md (errori che si
ripetono di più, dal REGISTRO-ERRORI-CLAUDE.md).

Robusto: se qualcosa va storto esce 0 senza output (la sessione non si rompe).
"""
import json
import os
import sys
import tempfile
from datetime import datetime
from zoneinfo import ZoneInfo

# v1.1 (18/11/2026): aggiunte INFO-PIU-USATE e COSE-DA-FARE del giorno (audit del meccanismo sera/mattino).
# Rilettura del mattino (errore #350, 17/11/2026): al primo messaggio di ogni giornata si chiede di rileggere
# i documenti prima di lavorare. Stato: un file per giorno nella cartella temporanea (CORSO_STATO_RILETTURA="" la spegne).
RILETTURA = (
    "RILETTURA DEL MATTINO (primo messaggio di oggi, %s; regola del docente, errore #350): prima di fare QUALSIASI "
    "cosa rileggi per intero: CLAUDE.md, GUIDA-MESSAGGI-AL-DOCENTE.md, CHECKLIST-LEZIONE.md e la guida dei segnalibri "
    "DIDAweb (docs/docenti/02-didaweb-i-segnalibri-che-scrivono-i-voti.html, con strumenti/didaweb-auto.js). Le "
    "modalità già decise dal docente (per esempio i voti DIDAweb col segnalibro «Voti DIDAweb AUTO» e il pacchetto; "
    "il codice da copiare in UN riquadro da solo in FONDO, R4 3ter) NON si cambiano: se un metodo esiste già, si usa "
    "quello. PRIMA di dare passi al docente leggi anche /home/user/corso-informatica-riservato/report/INFO-PIU-USATE-v1.0.md "
    "(o l'ultima versione presente in report/) e, se esiste, il file delle cose da fare di oggi: il più recente tra "
    "/home/user/corso-informatica-riservato/report/*/COSE-DA-FARE-<GG-MM di oggi>*.md (lo scrive la sera prima il "
    "controllore di fine giornata; se manca, dillo nella riga). Poi dici in una riga di averle rilette e quante cose "
    "bloccanti ci sono oggi."
)


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
        oggi = prima_volta_oggi()
        if oggi:
            testo = (RILETTURA % oggi) + "\n\n" + testo
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
