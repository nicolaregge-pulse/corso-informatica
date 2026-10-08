# -*- coding: utf-8 -*-
"""Pubblica una VERSIONE del «Treno blindato» della 3INF (fork della 2INF) e la lascia giocabile per sempre.

Ogni versione diventa una cartella ferma: docs/giochi/treno-3inf/versioni/<versione>/ (copia di tutti i file del gioco
in quel momento) e una riga in versioni/versioni.json; la pagina versioni/index.html elenca tutte le versioni con il link
per giocarle e il link al codice su GitHub di quel commit (così si vede come «riprendere» una versione).
Uso:
  python3 strumenti/pubblica_versione_treno3inf.py v0.1-alfa "Demo del prof" "cosa è cambiato"          (dal gioco attuale)
  python3 strumenti/pubblica_versione_treno3inf.py v0.0 "Prima idea" "cosa..." --da-commit d729f5e         (da un commit vecchio)
Dopo: commit + push; poi si rilancia con --commit-di <versione> per scrivere il commit nella pagina.
"""
import html, json, os, shutil, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIOCO = os.path.join(ROOT, "docs", "giochi", "treno-3inf")
VER = os.path.join(GIOCO, "versioni")
REPO = "https://github.com/nicolaregge-pulse/corso-informatica"
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf/"


def elenco():
    p = os.path.join(VER, "versioni.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []


def salva(v):
    os.makedirs(VER, exist_ok=True)
    json.dump(v, open(os.path.join(VER, "versioni.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    e = html.escape
    righe = ""
    for x in reversed(v):
        cod = (f"<a href='{REPO}/tree/{x['commit']}/docs/giochi/treno-3inf'>il codice di questa versione su GitHub (commit {x['commit'][:7]})</a>"
               if x.get("commit") else "commit in arrivo")
        righe += (f"<div class='v'><h2>{e(x['versione'])} — {e(x['nome'])}</h2><p class='d'>{e(x['data'])}</p><p>{e(x['cambi'])}</p>"
                  f"<p><a class='bt' href='{e(x['versione'])}/'>Gioca questa versione</a> {cod}</p></div>")
    pagina = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Il treno blindato della 3INF — tutte le versioni</title><style>body{{margin:0;background:#1a1410;color:#fff;font-family:system-ui,Segoe UI,Arial,sans-serif}}
.w{{max-width:820px;margin:0 auto;padding:16px}}h1{{color:#ffd34d}}.v{{background:#2c2119;border:1px solid #6b5440;border-radius:14px;padding:12px 16px;margin:12px 0}}
.v h2{{margin:0;color:#ffd34d;font-size:21px}}.d{{opacity:.7;margin:2px 0}}a{{color:#9fd3ff}}.bt{{display:inline-block;background:#2f9e57;color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:8px 14px;margin-right:8px}}
.nota{{background:#3a2c20;border-left:5px solid #ffd34d;padding:10px 12px;border-radius:8px}}</style></head><body><div class="w">
<h1>Il treno blindato della 3INF — tutte le versioni</h1>
<p>Ogni versione resta giocabile per sempre: è una «fotografia» del gioco in quel momento. <a href="../">Versione attuale</a></p>
<div class="nota"><b>Come si riprende una versione vecchia (Git):</b> 1) su GitHub, nel repository del corso, apri <b>Commits</b> (la storia) oppure <b>Insights → Network</b> (il grafo); 2) clicca il commit della versione; 3) <b>Browse files</b> mostra tutti i file com'erano; 4) per tornare indietro un file: apri il file a quel commit, copia, e incollalo con la matita nella versione attuale (oppure il prof fa un «revert» del commit).</div>
{righe}</div></body></html>"""
    open(os.path.join(VER, "index.html"), "w", encoding="utf-8").write(pagina)


def main():
    a = sys.argv[1:]
    v = elenco()
    if a and a[0] == "--commit-di":
        sha = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%H", "--", f"docs/giochi/treno-3inf/versioni/{a[1]}"], capture_output=True, text=True).stdout.strip()
        for x in v:
            if x["versione"] == a[1] and not x.get("commit"):
                x["commit"] = x.get("commit_sorgente") or sha
        salva(v); print("commit scritto:", a[1]); return
    ver, nome, cambi = a[0], a[1], a[2]
    dest = os.path.join(VER, ver)
    if os.path.exists(dest):
        sys.exit("Questa versione esiste già: le versioni pubblicate non si cambiano. Usa un numero nuovo.")
    os.makedirs(dest)
    if "--da-commit" in a:
        c = a[a.index("--da-commit") + 1]
        tar = subprocess.run(["git", "-C", ROOT, "archive", c, "docs/giochi/treno-3inf"], capture_output=True).stdout
        tmp = os.path.join(VER, ".tmp"); os.makedirs(tmp, exist_ok=True)
        subprocess.run(["tar", "-x", "-C", tmp], input=tar, check=True)
        src = os.path.join(tmp, "docs", "giochi", "treno-3inf")
        for f in os.listdir(src):
            if f != "versioni":
                (shutil.copytree if os.path.isdir(os.path.join(src, f)) else shutil.copy)(os.path.join(src, f), os.path.join(dest, f))
        shutil.rmtree(tmp)
        sorg = subprocess.run(["git", "-C", ROOT, "rev-parse", c], capture_output=True, text=True).stdout.strip()
    else:
        for f in os.listdir(GIOCO):
            if f != "versioni":
                (shutil.copytree if os.path.isdir(os.path.join(GIOCO, f)) else shutil.copy)(os.path.join(GIOCO, f), os.path.join(dest, f))
        sorg = ""
    sw = os.path.join(dest, "sw.js")
    if os.path.exists(sw):
        os.remove(sw)   # le versioni ferme non installano un service worker loro
    import datetime
    v.append({"versione": ver, "nome": nome, "cambi": cambi, "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), "commit": "", "commit_sorgente": sorg})
    salva(v); print("pubblicata:", dest)


if __name__ == "__main__":
    main()
