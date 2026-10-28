#!/usr/bin/env python3
"""Hook UserPromptSubmit: a ogni messaggio del docente aggiunge come contesto
per Claude il promemoria breve .claude/promemoria-errori.md (errori che si
ripetono di più, dal REGISTRO-ERRORI-CLAUDE.md).

Robusto: se qualcosa va storto esce 0 senza output (la sessione non si rompe).
"""
import json
import os
import sys


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
