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

Controlli che valgono per TUTTI (anche i subagenti), nel momento dell'azione:
3. Cancellare una versione in docs/ (PDF o file «vN.N») con rm / git rm, o spostarla con mv / git mv: rifiutato
   (errori del 01/10 n. 13 e del 05/10 n. 4: le versioni si tengono, si bumpa).
4. «git push» del repository PUBBLICO: prima si controllano i file di docs/ cambiati
   rispetto a origin/main (controlli_pagine.py: lingue della classe #49 #82 #119,
   link alla Regione #136, nomi in chiaro #85, sintassi degli script #118).
5. «git push» del RISERVATO: coda/*.json e comandi/*.json devono leggersi (05/10 n. 12).
Per un falso allarme si aggiunge al comando il commento «# PAGINE-OK: <motivo>».

Robusto: per qualunque errore interno esce 0 senza output (comando permesso).
"""
import fcntl
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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


# ------------------------------------------- controlli per tutti (anche subagenti)

PUB = "/home/user/corso-informatica"
RIS = "/home/user/corso-informatica-riservato"
RX_RM = re.compile(r"(?:^|[;&|(]\s*|\s)(?:git\s+rm|rm)((?:\s+[^\s;&|)]+)+)")
RX_MV = re.compile(r"(?:^|[;&|(]\s*|\s)(?:git\s+mv|mv)((?:\s+[^\s;&|)]+)+)")
RX_PUSH = re.compile(r"\bgit\b[^;&|\n]*\bpush\b")


def cancella_versioni(comando):
    for m in RX_RM.finditer(comando):
        for arg in m.group(1).split():
            if arg.startswith("-"):
                continue
            a = arg.strip("'\"")
            if "docs/" in a and (a.endswith(".pdf") or "*" in a or re.search(r"v\d+[._]\d+", a)):
                return ("Non si cancella una versione in docs/ («%s»): le versioni già date restano, si "
                        "bumpa e la pagina punta alla nuova (REGISTRO-ERRORI 01/10 n. 13, 05/10 n. 4)." % a)
    # audit 28/10/2026: anche spostare o rinominare una versione (mv / git mv) la toglie da docs/
    for m in RX_MV.finditer(comando):
        arg = [x.strip("'\"") for x in m.group(1).split() if not x.startswith("-")]
        for a in arg[:-1]:
            if "docs/" in a and (a.endswith(".pdf") or "*" in a or re.search(r"v\d+[._]\d+", a)):
                return ("Non si sposta né si rinomina una versione in docs/ («%s»): si copia (cp) la nuova "
                        "versione accanto alla vecchia, che resta (REGISTRO-ERRORI 01/10 n. 13, 05/10 n. 4)." % a)
    return None


def repo_del_push(comando, cwd):
    if "corso-informatica-riservato" in comando:
        return RIS
    if re.search(r"/home/user/corso-informatica(?![-\w])", comando):
        return PUB
    cwd = cwd or ""
    if cwd.startswith(RIS):
        return RIS
    if cwd.startswith(PUB):
        return PUB
    return None


def git(cartella, *arg):
    r = subprocess.run(["git", "-C", cartella] + list(arg), capture_output=True, text=True, timeout=8)
    return r.stdout if r.returncode == 0 else ""


def controlla_push_pubblico(comando):
    import controlli_pagine as cp
    inizio = time.time()
    nomi = set(git(PUB, "diff", "--name-only", "origin/main", "--", "docs").split())
    if re.search(r"\bgit\b[^;&|]*\badd\b", comando):
        nomi |= set(git(PUB, "ls-files", "--others", "--exclude-standard", "--", "docs").split())
    problemi = []
    for nome in sorted(nomi)[:40]:
        if time.time() - inizio > 12:
            break
        if not cp.da_controllare(nome):
            continue
        f = os.path.join(PUB, nome)
        if not os.path.isfile(f) or os.path.getsize(f) > 3_000_000:
            continue
        try:
            testo = open(f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        problemi.extend(cp.controlla(nome, testo, cp.SICURI))
    if not problemi:
        return None
    return ("Push del sito fermato: %d problemi nelle pagine (controlli_pagine.py).\n%s\nCorreggi e "
            "rilancia il push. Solo se è un falso allarme, aggiungi al comando il commento "
            "«# PAGINE-OK: <motivo>» e dillo al docente." % (len(problemi), "\n".join(problemi[:6])))


def controlla_push_riservato():
    rotti = []
    for f in glob.glob(os.path.join(RIS, "coda", "*.json")) + glob.glob(os.path.join(RIS, "comandi", "*.json")):
        try:
            testo = open(f, encoding="utf-8").read()
            if "<<<<<<<" in testo or ">>>>>>>" in testo:
                raise ValueError("conflitto")
            json.loads(testo)
        except Exception:
            rotti.append(os.path.relpath(f, RIS))
    if not rotti:
        return None
    return ("Push del riservato fermato: questi file della coda o del ponte non si leggono (JSON rotto o "
            "segni di conflitto): %s. Riscrivi il file intero, non prendere un lato a caso "
            "(REGISTRO-ERRORI 05/10 n. 12)." % ", ".join(rotti[:5]))


def controllo_comando(data, comando):
    if "PAGINE-OK" in comando:
        return None
    m = cancella_versioni(comando)
    if m:
        return m
    if not RX_PUSH.search(comando):
        return None
    repo = repo_del_push(comando, data.get("cwd"))
    if repo == PUB and os.path.isdir(PUB):
        return controlla_push_pubblico(comando)
    if repo == RIS and os.path.isdir(RIS):
        return controlla_push_riservato()
    return None


def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    if data.get("tool_name") != "Bash":
        return
    comando = str((data.get("tool_input") or {}).get("command") or "")
    try:
        motivo = controllo_comando(data, comando)
    except Exception:
        motivo = None
    if motivo:
        nega(motivo)
        return
    if data.get("agent_id"):
        return  # chiamata di un subagente: libera dal limite dei comandi
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
