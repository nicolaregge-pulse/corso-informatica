#!/usr/bin/env python3
"""Hook PreToolUse (matcher Bash): limita i comandi della sessione PRINCIPALE.

Errore #132: comandi e risultati lunghi riempiono la chat e il docente non
riesce a leggere. Regole:
1. Al massimo 3 comandi Bash per turno (un turno = dall'ultimo messaggio
   arrivato nella sessione: docente, messaggio programmato, resoconto di un
   subagente). Dal 4° in poi il comando viene rifiutato.
2. Un singolo comando più lungo di 600 caratteri viene rifiutato.
Le chiamate dei subagenti (campo agent_id nell'input) non si contano e non si
bloccano: il lavoro lungo va proprio lì.

Robusto: per qualunque errore interno esce 0 senza output (comando permesso).
"""
import fcntl
import json
import os
import sys
import tempfile

MAX_COMANDI = 3
MAX_CARATTERI = 600
MAX_BYTE_LETTI = 40 * 1024 * 1024  # il transcript può superare i 100 MB

MOTIVO_TROPPI = ("Più di 3 comandi in questo turno: passa il lavoro a un subagente "
                 "(Agent) così il docente non vede la chat piena (REGISTRO-ERRORI #132).")
MOTIVO_LUNGO = ("Comando Bash più lungo di 600 caratteri: metti il codice in un file "
                "nello scratchpad (Write) e lancialo con un comando di una riga che "
                "stampa solo «ok», oppure passa il lavoro a un subagente (Agent) "
                "(REGISTRO-ERRORI #132).")


def righe_dal_fondo(path, max_byte=MAX_BYTE_LETTI, blocco=1024 * 1024):
    """Restituisce le righe del file dalla fine verso l'inizio."""
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        pos = f.tell()
        letti = 0
        resto = b""
        while pos > 0 and letti < max_byte:
            n = min(blocco, pos)
            pos -= n
            f.seek(pos)
            pezzo = f.read(n) + resto
            letti += n
            parti = pezzo.split(b"\n")
            resto = parti[0]
            for r in reversed(parti[1:]):
                if r.strip():
                    yield r
        if pos == 0 and resto.strip():
            yield resto


def inizio_turno(d):
    """True se la riga del transcript è un messaggio che apre un turno."""
    if d.get("type") != "user" or d.get("isSidechain"):
        return False
    contenuto = (d.get("message") or {}).get("content")
    if isinstance(contenuto, list):
        tipi = {x.get("type") for x in contenuto if isinstance(x, dict)}
        if not tipi or tipi <= {"tool_result"}:
            return False
    elif not isinstance(contenuto, str):
        return False
    if d.get("origin"):
        return True  # docente, messaggio programmato, resoconto, notifica
    return not d.get("isMeta")  # escluse immagini espanse e «Stop hook feedback»


def bash_del_turno(transcript_path):
    """(chiave del turno, insieme degli id dei Bash del turno) dal transcript."""
    ids = set()
    chiave = None
    for r in righe_dal_fondo(transcript_path):
        try:
            d = json.loads(r)
        except Exception:
            continue
        if d.get("isSidechain"):
            continue
        if d.get("type") == "assistant":
            for x in (d.get("message") or {}).get("content") or []:
                if isinstance(x, dict) and x.get("type") == "tool_use" and x.get("name") == "Bash":
                    if x.get("id"):
                        ids.add(x["id"])
        elif inizio_turno(d):
            chiave = d.get("promptId") or d.get("uuid")
            break
    return chiave, ids


def file_stato(data):
    base = data.get("scratchpad_dir") or tempfile.gettempdir()
    cartella = os.path.join(base, "controlli-hook")
    os.makedirs(cartella, exist_ok=True)
    sid = "".join(c for c in str(data.get("session_id") or "sessione") if c.isalnum() or c in "-_")
    return os.path.join(cartella, "limite-comandi-%s.json" % (sid or "sessione"))


def nega(motivo):
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": motivo,
        }
    }
    sys.stdout.write(json.dumps(out, ensure_ascii=False))


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    if data.get("agent_id"):
        return  # chiamata di un subagente: libera
    if data.get("tool_name") != "Bash":
        return
    comando = str((data.get("tool_input") or {}).get("command") or "")
    tid = data.get("tool_use_id") or ""

    chiave_tr, ids_tr = None, set()
    tp = data.get("transcript_path")
    if tp:
        try:
            chiave_tr, ids_tr = bash_del_turno(os.path.expanduser(tp))
        except Exception:
            chiave_tr, ids_tr = None, set()
    chiave = data.get("prompt_id") or chiave_tr or "senza-turno"

    percorso = file_stato(data)
    with open(percorso, "a+", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            stato = json.loads(f.read() or "{}")
        except Exception:
            stato = {}
        turno = stato.setdefault(chiave, {"permessi": [], "bloccati": []})
        permessi = set(turno["permessi"])
        bloccati = set(turno["bloccati"])
        gia_contati = (ids_tr - bloccati - {tid}) | (permessi - {tid})

        motivo = None
        if len(comando) > MAX_CARATTERI:
            motivo = MOTIVO_LUNGO
        elif len(gia_contati) >= MAX_COMANDI:
            motivo = MOTIVO_TROPPI

        if motivo:
            if tid:
                bloccati.add(tid)
        else:
            permessi.add(tid or "senza-id-%d" % len(permessi))
        turno["permessi"] = sorted(permessi)
        turno["bloccati"] = sorted(bloccati)
        # tiene solo gli ultimi 30 turni
        if len(stato) > 30:
            for k in list(stato)[:-30]:
                stato.pop(k, None)
        f.seek(0)
        f.truncate()
        f.write(json.dumps(stato))
        fcntl.flock(f, fcntl.LOCK_UN)

    if motivo:
        nega(motivo)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
