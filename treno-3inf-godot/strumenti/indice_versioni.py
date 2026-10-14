#!/usr/bin/env python3
"""Rifà la pagina docs/giochi/treno-3inf-v2/versioni/index.html da versioni/versioni.json.

Uso (dalla radice del repository):  python3 treno-3inf-godot/strumenti/indice_versioni.py
"""
import html
import json
import pathlib

WEB = pathlib.Path(__file__).resolve().parent.parent.parent / "docs" / "giochi" / "treno-3inf-v2" / "versioni"
TITOLO = "Il treno blindato della 3INF su Godot — tutte le versioni"
CSS = """body{margin:0;background:#1a1410;color:#fff;font-family:system-ui,Segoe UI,Arial,sans-serif}
.w{max-width:820px;margin:0 auto;padding:16px}h1{color:#ffd34d}.v{background:#2c2119;border:1px solid #6b5440;border-radius:14px;padding:12px 16px;margin:12px 0}
.v h2{margin:0;color:#ffd34d;font-size:21px}.d{opacity:.7;margin:2px 0}a{color:#9fd3ff}.bt{display:inline-block;background:#2f9e57;color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:8px 14px;margin-right:8px}
.nota{background:#3a2c20;border-left:5px solid #ffd34d;padding:10px 12px;border-radius:8px;margin:10px 0}"""


def main() -> None:
    righe = json.loads((WEB / "versioni.json").read_text(encoding="utf-8"))
    blocchi = []
    for r in reversed(righe):
        v = html.escape(r["versione"])
        if r.get("commit"):
            codice = f"<a href='https://github.com/nicolaregge-pulse/corso-informatica/tree/{r['commit']}/docs/giochi/treno-3inf-v2'>il codice di questa versione su GitHub (commit {r['commit'][:7]})</a>"
        else:
            codice = "commit in arrivo"
        blocchi.append(f"<div class='v'><h2>{v} — {html.escape(r['nome'])}</h2><p class='d'>{html.escape(r['data'])}</p>"
                       f"<p>{html.escape(r['cambi'])}</p><p><a class='bt' href='{v}/'>Gioca questa versione</a> {codice}</p></div>")
    pagina = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITOLO}</title><style>{CSS}</style></head><body><div class="w">
<h1>{TITOLO}</h1>
<p>Ogni versione resta giocabile per sempre: è una «fotografia» del gioco in quel momento. <a href="../">Versione attuale</a></p>
<div class="nota"><b>Da dove viene:</b> questo treno è un <b>fork</b> (una copia tutta nostra) della <b>base del prof</b> su Godot (v1.0). Si parte da <b>v2.0</b>: è una versione <b>major</b> perché il gioco ha cambiato motore (il treno della 3INF di prima, v1.0 … v1.11, era in HTML ed è ancora giocabile in <a href="../../treno-3inf/versioni/">un'altra pagina</a>). Poi le richieste della classe sono arrivate una alla volta, ognuna come una versione nuova.</div>
<div class="nota"><b>Come si riprende una versione vecchia (Git):</b> 1) su GitHub, nel repository del corso, apri <b>Commits</b> (la storia) oppure <b>Insights → Network</b> (il grafo); 2) clicca il commit della versione; 3) <b>Browse files</b> mostra tutti i file com'erano; 4) per tornare indietro un file: apri il file a quel commit, copia, e incollalo con la matita nella versione attuale (oppure il prof fa un «revert» del commit).</div>
{''.join(blocchi)}</div></body></html>
"""
    (WEB / "index.html").write_text(pagina, encoding="utf-8")
    print("scritto", WEB / "index.html")


if __name__ == "__main__":
    main()
