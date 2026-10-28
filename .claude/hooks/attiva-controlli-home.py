#!/usr/bin/env python3
"""Attiva i controlli automatici anche quando la sessione Claude Code parte
dalla cartella /home/user (e non da /home/user/corso-informatica).

Claude Code legge .claude/settings.json della cartella da cui parte la
sessione: se parte da /home/user, i controlli di questo repository non
valgono. Questo script aggiunge (una volta sola, senza doppioni) i tre
controlli a /home/user/.claude/settings.json, con i percorsi assoluti.
Uso: python3 /home/user/corso-informatica/.claude/hooks/attiva-controlli-home.py
Stampa solo «ok».
"""
import json
import os

HOOKS = "/home/user/corso-informatica/.claude/hooks"
DEST = "/home/user/.claude/settings.json"

VOCI = {
    "UserPromptSubmit": (None, "python3 %s/promemoria-errori.py" % HOOKS, 10),
    "PreToolUse": ("Bash", "python3 %s/limite-comandi.py" % HOOKS, 20),
    "Stop": (None, "python3 %s/controllo-messaggio.py" % HOOKS, 20),
}

os.makedirs(os.path.dirname(DEST), exist_ok=True)
try:
    with open(DEST, encoding="utf-8") as f:
        cfg = json.load(f)
except Exception:
    cfg = {}
hooks = cfg.setdefault("hooks", {})
for evento, (matcher, comando, timeout) in VOCI.items():
    gruppi = hooks.setdefault(evento, [])
    if any(h.get("command") == comando for g in gruppi for h in g.get("hooks", [])):
        continue
    gruppo = {"hooks": [{"type": "command", "command": comando, "timeout": timeout}]}
    if matcher:
        gruppo["matcher"] = matcher
    gruppi.append(gruppo)
with open(DEST, "w", encoding="utf-8") as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)
print("ok")
