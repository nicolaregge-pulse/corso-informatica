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
casi.append(("git mv di un PDF versionato fuori da docs", esegui("git mv docs/1inf-x/Dispensa-AR-v1.2.pdf classe-1/x/Dispensa-AR-v1.3.pdf", pub, "a1"), True))
casi.append(("mv di una versione dentro docs", esegui("mv docs/1inf-x/a-v1.1.pdf docs/1inf-x/a-v1.2.pdf", pub, "a1"), True))
casi.append(("cp di una versione nuova accanto alla vecchia", esegui("cp classe-1/x/a-v1.2.pdf docs/1inf-x/", pub, "a1"), False))
casi.append(("mv di un file verso docs", esegui("mv /tmp/x/a-v1.2.pdf docs/1inf-x/", pub, "a1"), False))
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
# R1 (04/11/2026): cognomi degli allievi nei commit del pubblico
import controllo_nomi as cn; cn._CACHE.clear()
casi.append(("commit pubblico con cognome nel messaggio", esegui('git commit -m "Cruscotto: Rossi ha finito"', pub), True))
casi.append(("commit pubblico con cognome, anche con PAGINE-OK", esegui('git commit -m "Rossi ok" # PAGINE-OK: x', pub), True))
casi.append(("commit pubblico con «Mario R.»", esegui('git commit -m "Cruscotto: Mario R. ha finito"', pub), False))
casi.append(("commit pubblico con heredoc e cognome", esegui("git commit -F - <<'EOF'\nVoti di BIANCHI\nEOF", pub), True))
open(T + "/msg.txt", "w").write("Pagina di Bianchi")
casi.append(("commit pubblico con -F file e cognome", esegui("git commit -F %s/msg.txt" % T, pub), True))
# #319 (12/11/2026): cognome dentro un file fuori da docs/ (qui fabbrica/)
scrivi("fabbrica/correzioni/nota.js", "// esempio: ROSSI MARIO dava Mario R.")
casi.append(("push pubblico con add: cognome in un file di fabbrica/", esegui("git add -A && git push", pub), True))
casi.append(("push pubblico con add: cognome in fabbrica/, anche con PAGINE-OK", esegui("git add -A && git push # PAGINE-OK: x", pub), True))
scrivi("fabbrica/correzioni/nota.js", "// esempio: nomi inventati, Mario R.")
casi.append(("push pubblico con add: file di fabbrica/ senza cognomi", esegui("git add -A && git push", pub), False))
os.remove(pub + "/fabbrica/correzioni/nota.js")
casi.append(("commit RISERVATO con cognome (ammesso)", esegui('git commit -m "Voti di Rossi Mario"', ris), False))
casi.append(("commit pubblico senza nomi", esegui('git commit -m "Cruscotto 1INF aggiornato"', pub), False))
sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "nota su Rossi", cwd=pub)
casi.append(("push pubblico con cognome in un commit da pushare", esegui("git push", pub), True))
sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--amend", "--allow-empty", "-m", "nota", cwd=pub)
casi.append(("push pubblico dopo aver corretto il messaggio", esegui("git push # PAGINE-OK: prova", pub), False))
cn._CACHE.clear()
json.dump({"nomi": [], "parole_comuni": ["rossi"]}, open(ris + "/config/nomi-controllo.json", "w"))
casi.append(("parola comune esclusa", esegui('git commit -m "Rossi è un colore"', pub), False))
r = subprocess.run([sys.executable, H + "/controllo_nomi.py", T + "/msg.txt"], capture_output=True, text=True, env=dict(os.environ))
casi.append(("commit-msg: modulo da riga di comando non si rompe", r.returncode in (0, 1), True))
# limite: 8 comandi per turno nella sessione principale
for i in range(8):
    esegui("ls", "/tmp", None, "sessione8")
casi.append(("9° comando dello stesso turno rifiutato", esegui("ls", "/tmp", None, "sessione8"), True))
# input rotto: nessuna uscita, codice 0
r = subprocess.run([sys.executable, H + "/limite-comandi.py"], input="non json", capture_output=True, text=True)
casi.append(("input rotto: esce 0 senza output", r.returncode == 0 and not r.stdout, True))
ok = sum(1 for _, got, exp in casi if got == exp)
for n, got, exp in casi:
    if got != exp: print("SBAGLIATO:", n, "atteso", exp, "ottenuto", got)
print("%d/%d" % (ok, len(casi)))
