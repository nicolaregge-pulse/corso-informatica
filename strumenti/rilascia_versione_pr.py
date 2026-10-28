# -*- coding: utf-8 -*-
"""Mette IN PRODUZIONE una Pull Request come versione nuova del gioco della classe (metodo approvato il 12/10/2026).
Fa tutto il giro, sempre uguale:
  1. versione.json e CHANGELOG.md del gioco (chi l'ha chiesta, cosa cambia, peso, dove nel codice);
  2. controllo automatico del gioco (strumenti/controlla.py): se fallisce, si ferma e non pubblica niente;
  3. cartella ferma della versione (giocabile per sempre) con lo script di pubblicazione del gioco;
  4. backlog: la PR diventa FATTO con il numero della versione (file dei pesi nel repository riservato);
  5. pagina «Cosa è cambiato oggi» (strumenti/gen_novita.py) e grafo (legge da solo versioni.json);
  6. commit + push dei due repository, poi il numero del commit nella pagina delle versioni.
Le impostazioni della lezione (gioco, pagine, file dei pesi) stanno nel repository riservato: config/lezioni/<id>.json.
Prima di lanciarlo si modifica il codice del gioco (index.html, regole.json…) e si prova nel browser.
Uso: python3 strumenti/rilascia_versione_pr.py <id-lezione> <versione> "<nome>" "<riassunto>" '<righe del changelog in JSON>' '<pesi da aggiornare in JSON>'
Esempio: python3 strumenti/rilascia_versione_pr.py 20261012_2INF v0.27 "Binari gialli" "PR di Katherine A." '["riga 1","riga 2"]' '{"email|ora":{"fatto":"v0.27"}}'
"""
import sys as _sp, os as _op; _sp.path.append(_op.path.dirname(_op.path.abspath(__file__))); import privacy_pubblico  # noqa: E401,F401 privacy 28/10/2026: nel pubblico i ragazzi solo come «Nome C.»
import json, sys, subprocess, datetime, os, time
PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIV = os.path.join(os.path.dirname(PUB), "corso-informatica-riservato")
lid, ver, nome, cambi, righe, pesi = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], json.loads(sys.argv[5]), json.loads(sys.argv[6])
C = json.load(open(os.path.join(PRIV, "config", "lezioni", lid + ".json"), encoding="utf-8"))
G = os.path.join(PUB, "docs", "giochi", C["gioco"]["cartella"])
PG = C["pagine"]
TR = "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01JTpsyuF8gaZ4AW6QqesUQ2"
ora = (datetime.datetime.utcnow() + datetime.timedelta(hours=2)).strftime("%d/%m/%Y %H:%M")
r = subprocess.run(["python3", "strumenti/controlla.py"], cwd=G, capture_output=True, text=True)
if "Tutto a posto" not in r.stdout:
    sys.exit("CONTROLLO FALLITO, niente pubblicato:\n" + r.stdout[-500:] + r.stderr[-500:])
json.dump({"versione": ver.lstrip("v"), "nome": nome}, open(G + "/versione.json", "w"), ensure_ascii=False, indent=2)
s = open(G + "/CHANGELOG.md", encoding="utf-8").read()
blocco = f"## {ver} — {ora} — {nome}\n\n" + "".join(f"{i+1}. {x}\n" for i, x in enumerate(righe)) + "\n"
s = s.replace("# Storia delle versioni\n\n", "# Storia delle versioni\n\n" + blocco, 1)
open(G + "/CHANGELOG.md", "w", encoding="utf-8").write(s)
subprocess.run(["python3", C["gioco"]["pubblica"], ver, nome, cambi], cwd=PUB, check=True)
p = os.path.join(PRIV, C["pesi"]); d = json.load(open(p, encoding="utf-8"))
for k, v in pesi.items():
    d.setdefault(k, {}).update(v)
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
subprocess.run(["python3", "generatori/lezione_pr.py", lid, "backlog"], cwd=PRIV)
subprocess.run(["python3", "strumenti/gen_novita.py", C["gioco"]["cartella"], PG["novita"], C["data"], C["classe"]], cwd=PUB)
def push(repo, paths, msg):
    subprocess.run(["git", "-C", repo, "add", "-f"] + paths)
    subprocess.run(["git", "-C", repo, "commit", "-q", "-m", msg + TR])
    for _ in range(8):
        if subprocess.run(["git", "-C", repo, "pull", "-q", "--rebase", "origin", "main"], capture_output=True).returncode:
            subprocess.run(["git", "-C", repo, "rebase", "--abort"], capture_output=True)
        if subprocess.run(["git", "-C", repo, "push", "-q", "origin", "HEAD:main"], capture_output=True).returncode == 0: return True
        time.sleep(2)
    print("PUSH FALLITO", repo)
push(PRIV, [C["pesi"]], f"Backlog {C['classe']}: FATTO {ver}")
push(PUB, [f"docs/giochi/{C['gioco']['cartella']}", f"docs/{PG['backlog']}", f"docs/{PG['novita']}"], f"{C['gioco']['titolo']} {C['classe']} {ver}: {nome}")
subprocess.run(["python3", C["gioco"]["pubblica"], "--commit-di", ver], cwd=PUB)
push(PUB, [f"docs/giochi/{C['gioco']['cartella']}/versioni"], f"{C['classe']}: commit della {ver} nella pagina delle versioni")
print("RILASCIATA", ver, ora)
