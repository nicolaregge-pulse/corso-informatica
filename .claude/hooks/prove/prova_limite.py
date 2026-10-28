"""Prove di limite-comandi.py (controlli per tutti: versioni, push pubblico, push riservato)."""
import importlib.util, io, json, os, subprocess, sys, tempfile, contextlib
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("lc", H + "/limite-comandi.py"); lc = importlib.util.module_from_spec(spec); spec.loader.exec_module(lc)
T = tempfile.mkdtemp()
def sh(*a, cwd=None): subprocess.run(a, cwd=cwd, check=True, capture_output=True)
pub, ris, bare = T + "/pub", T + "/ris", T + "/bare.git"
sh("git", "init", "-q", "--bare", bare); sh("git", "init", "-q", "-b", "main", pub)
os.makedirs(pub + "/docs/2inf-prova"); open(pub + "/docs/2inf-prova/index.html", "w").write("<p>ciao</p>")
sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "x", cwd=pub)
sh("git", "add", "-A", cwd=pub); sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "y", cwd=pub)
sh("git", "remote", "add", "origin", bare, cwd=pub); sh("git", "push", "-q", "origin", "main", cwd=pub); sh("git", "fetch", "-q", cwd=pub)
os.makedirs(ris + "/coda"); os.makedirs(ris + "/comandi"); os.makedirs(ris + "/config")
json.dump(["ROSSI MARIO", "BIANCHI ANNA"], open(ris + "/config/2inf-presenti-20261028.json", "w"))
open(ris + "/coda/a.json", "w").write('{"stato": "ok"}')
lc.PUB, lc.RIS = pub, ris
import controlli_pagine as cp; cp.RIS = ris; cp._NOMI = None

def esegui(cmd, cwd=None, agent="a1", sessione="prova"):
    d = {"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": cwd, "session_id": sessione, "scratchpad_dir": T}
    if agent: d["agent_id"] = agent
    sys.stdin = io.StringIO(json.dumps(d)); out = io.StringIO()
    with contextlib.redirect_stdout(out):
        try: lc.main()
        except Exception as e: print("ECCEZIONE", e)
    return "deny" in out.getvalue()

def scrivi(rel, testo, base=pub):
    os.makedirs(os.path.dirname(base + "/" + rel), exist_ok=True); open(base + "/" + rel, "w").write(testo)

casi = []
casi.append(("rm di un PDF versionato in docs", esegui("rm docs/1inf-x/dispensa-v1.0.pdf", pub, "a1"), True))
casi.append(("git rm con jolly in docs", esegui("cd /x && git rm docs/1inf/*.pdf", pub, "a1"), True))
casi.append(("rm di un file temporaneo", esegui("rm -rf /tmp/prova.txt", pub, "a1"), False))
casi.append(("git rm di una pagina html senza versione", esegui("git rm docs/1inf/index.html", pub, "a1"), False))
casi.append(("rm versione con PAGINE-OK", esegui("rm docs/a-v1.0.pdf # PAGINE-OK: doppione", pub, "a1"), False))
casi.append(("push pubblico pulito", esegui("git push origin HEAD:main", pub, "a1"), False))
scrivi("docs/2inf-prova/index.html", "<p>ciao 你好</p>")
casi.append(("push pubblico: cinese in pagina 2INF", esegui("git commit -am x && git push", pub, "a1"), True))
casi.append(("stesso push con PAGINE-OK", esegui("git push # PAGINE-OK: prova", pub, "a1"), False))
scrivi("docs/2inf-prova/index.html", "<p>ciao</p><pre>العربية</pre>")
casi.append(("push pubblico: arabo solo dentro <pre> (esempio di codice)", esegui("git push", pub), False))
scrivi("docs/2inf-prova/index.html", "<p>ripasso</p><a href='https://sites.google.com/piamarta.it/formazionesicurezzamilano/1-ora'>x</a>")
casi.append(("push pubblico: link alla Regione", esegui("git push", pub), True))
scrivi("docs/2inf-prova/index.html", "<p>ok</p><script>var a = 'l'account';</script>")
casi.append(("push pubblico: script con apostrofo che rompe", esegui("git push", pub), True))
scrivi("docs/2inf-prova/index.html", "<p>ok</p><script>var a = \"l'account\";</script>")
casi.append(("push pubblico: script corretto", esegui("git push", pub), False))
scrivi("docs/2inf-voti/voti.json", '{"righe":[{"n":"Rossi Mario","v":60}]}')
casi.append(("push pubblico con add: nome in chiaro in un JSON nuovo", esegui("git add -A && git push", pub), True))
casi.append(("push pubblico senza add: file non tracciato ignorato", esegui("git push", pub), False))
scrivi("docs/2inf-voti/voti.json", '{"righe":[{"n":"Mario R.","v":60}]}')
casi.append(("push pubblico con add: «Nome I.» ammesso", esegui("git add -A && git push", pub), False))
casi.append(("push riservato con JSON a posto", esegui("git push", ris), False))
scrivi("coda/b.json", '{"stato": "da-pubblicare",\n<<<<<<< HEAD\n}', base=ris)
casi.append(("push riservato con conflitto in coda", esegui("git push origin HEAD:main", ris), True))
casi.append(("riconosce il riservato dal percorso nel comando", lc.repo_del_push("cd /home/user/corso-informatica-riservato && git push", "/home/user") == lc.RIS, True))
casi.append(("riconosce il pubblico dal percorso nel comando", lc.repo_del_push("git -C /home/user/corso-informatica push", "/") == lc.PUB, True))
casi.append(("comando senza push con coda rotta", esegui("ls", ris), False))
# comportamento vecchio: subagente libero, comando lungo della sessione principale rifiutato
casi.append(("subagente con comando lungo", esegui("echo " + "x" * 700, "/tmp", "a1"), False))
casi.append(("sessione principale con comando lungo", esegui("echo " + "x" * 700, "/tmp", None, "sessione2"), True))
# input rotto: nessuna uscita, codice 0
r = subprocess.run([sys.executable, H + "/limite-comandi.py"], input="non json", capture_output=True, text=True)
casi.append(("input rotto: esce 0 senza output", r.returncode == 0 and not r.stdout, True))
ok = sum(1 for _, got, exp in casi if got == exp)
for n, got, exp in casi:
    if got != exp: print("SBAGLIATO:", n, "atteso", exp, "ottenuto", got)
print("%d/%d" % (ok, len(casi)))
