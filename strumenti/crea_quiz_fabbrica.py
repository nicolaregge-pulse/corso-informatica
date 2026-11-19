#!/usr/bin/env python3
"""crea_quiz_fabbrica.py v1.0 (19/11/2026)

Costruisce il file fabbrica/<id>.txt (JSON in base64, stesso formato dei quiz gia' in uso) e aggiunge la riga in
fabbrica/indice.json (lavori; con --sicurezza-ora anche sicurezza[classe].ore), poi con --commit/--push fa commit e push.
Il Moduli lo crea il motore della Fabbrica (foglio del docente) al giro successivo: il link si legge poi con
`bash strumenti/leggi_fabbrica.sh <id>` nel riservato (vedi PIANO-AUTONOMIA, passo 3).

Uso:
  python3 strumenti/crea_quiz_fabbrica.py SPEC.json --dry-run          # non scrive niente, stampa l'esito
  python3 strumenti/crea_quiz_fabbrica.py SPEC.json                    # scrive file e indice
  python3 strumenti/crea_quiz_fabbrica.py SPEC.json --commit --push    # scrive, commit e push (pull --rebase prima)
  python3 strumenti/crea_quiz_fabbrica.py --decodifica fabbrica/X.txt  # stampa la specifica JSON di un quiz esistente
Opzioni di prova: --fabbrica DIR (cartella al posto di fabbrica/), --verifica-uguale FILE (con --dry-run: il testo
prodotto deve essere identico a FILE, byte per byte).

SPECIFICA (JSON): {"id","titolo","descrizione","mescola":true,"conferma":"...","classe":"2INF",
 "tipologia_lezione":"quiz","sicurezza_ora":"7" (opzionale),
 "domande":[{"tipo":"singola|multi|paragrafo","t":"testo","s":[["risposta",true|false],...],"sp":"","punti":1}]}
Controlli bloccanti: id nuovo (mai riusato: ne' in indice.json ne' come file), formato id, singola = 1 giusta,
multi = almeno 2 giuste, paragrafo senza risposte, punti interi > 0, testi non vuoti, nessun cognome (R1: solo se
esiste il file elenco del riservato, via controllo_nomi.py: qui NON si cerca, lo fa l'hook del commit).
"""
import argparse, base64, json, os, re, subprocess, sys

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def codifica(spec):
    """Stesso formato di fabbrica/quiz-*.txt: JSON (ensure_ascii=False, separatori standard) in base64 + a capo."""
    corpo = {k: spec[k] for k in ("id", "titolo", "descrizione", "mescola", "conferma", "domande")}
    return base64.b64encode(json.dumps(corpo, ensure_ascii=False).encode("utf-8")).decode("ascii") + "\n"


def decodifica(testo):
    return json.loads(base64.b64decode(testo).decode("utf-8"))


def controlla(spec, indice, dirf):
    err = []
    for k in ("id", "titolo", "descrizione", "conferma", "domande", "classe"):
        if not spec.get(k):
            err.append("manca il campo '%s'" % k)
    spec.setdefault("mescola", True)
    spec.setdefault("tipologia_lezione", "quiz")
    qid = spec.get("id", "")
    if not re.fullmatch(r"(quiz|scheda)-(1inf|2inf|3inf|4ti)-[a-z0-9-]+", qid):
        err.append("id non valido (atteso quiz-<classe minuscola>-...): %r" % qid)
    if any(l.get("id") == qid for l in indice.get("lavori", [])):
        err.append("id gia' in indice.json: un lavoro gia' creato non si ricrea mai (scegli un id nuovo, es. suffisso b)")
    if os.path.exists(os.path.join(dirf, qid + ".txt")):
        err.append("il file %s.txt esiste gia' (mai riusare un id)" % qid)
    cl = str(spec.get("classe", "")).lower()
    if qid and cl and "-%s-" % cl not in qid:
        err.append("la classe %s non compare nell'id" % spec.get("classe"))
    for n, d in enumerate(spec.get("domande") or [], 1):
        p = "domanda %d: " % n
        if d.get("tipo") not in ("singola", "multi", "paragrafo"):
            err.append(p + "tipo %r non valido" % d.get("tipo")); continue
        if not str(d.get("t", "")).strip():
            err.append(p + "testo vuoto")
        d.setdefault("sp", "")
        if not isinstance(d.get("punti"), int) or d["punti"] < 1:
            err.append(p + "punti deve essere un intero >= 1")
        if d["tipo"] == "paragrafo":
            if d.get("s"):
                err.append(p + "una domanda aperta non ha risposte")
            d.pop("s", None)
            continue
        s = d.get("s") or []
        if len(s) < 2 or any(not (isinstance(x, list) and len(x) == 2 and str(x[0]).strip() and isinstance(x[1], bool)) for x in s):
            err.append(p + "risposte non valide (serve [[testo,true|false],...], almeno 2)"); continue
        g = sum(1 for x in s if x[1])
        if d["tipo"] == "singola" and g != 1:
            err.append(p + "singola: le risposte giuste sono %d, deve essere 1" % g)
        if d["tipo"] == "multi" and g < 2:
            err.append(p + "multi: le risposte giuste sono %d, devono essere almeno 2" % g)
        if len({x[0] for x in s}) != len(s):
            err.append(p + "due risposte uguali")
    return err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--commit", action="store_true")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--sicurezza-ora")
    ap.add_argument("--fabbrica", default=os.path.join(RADICE, "fabbrica"))
    ap.add_argument("--verifica-uguale")
    ap.add_argument("--decodifica")
    a = ap.parse_args()
    if a.decodifica:
        print(json.dumps(decodifica(open(a.decodifica, "rb").read()), ensure_ascii=False, indent=1)); return 0
    if not a.spec:
        ap.error("serve il file di specifica")
    spec = json.load(open(a.spec, encoding="utf-8"))
    pind = os.path.join(a.fabbrica, "indice.json")
    indice = json.load(open(pind, encoding="utf-8"))
    err = controlla(spec, indice, a.fabbrica)
    if err:
        print("NON CREATO:\n - " + "\n - ".join(err)); return 2
    testo = codifica(spec)
    if decodifica(testo)["domande"] != spec["domande"]:
        print("NON CREATO: la prova di decodifica non coincide"); return 2
    if a.verifica_uguale:
        uguale = testo.encode() == open(a.verifica_uguale, "rb").read()
        print("verifica byte per byte con %s: %s" % (a.verifica_uguale, "IDENTICO" if uguale else "DIVERSO"))
        if not uguale:
            return 3
    voce = {"id": spec["id"], "file": spec["id"] + ".txt", "tipologia_lezione": spec["tipologia_lezione"]}
    ora = a.sicurezza_ora or spec.get("sicurezza_ora")
    nuovo = json.loads(json.dumps(indice))
    nuovo["lavori"].append(voce)
    if ora:
        trovato = False
        for s in nuovo.get("sicurezza", []):
            if s.get("classe") == spec["classe"]:
                for o in s["ore"]:
                    if o.get("ora") == str(ora):
                        o.setdefault("ids", []).append(spec["id"]); trovato = True
        if not trovato:
            print("NON CREATO: sicurezza %s ora %s non trovata in indice.json" % (spec["classe"], ora)); return 2
    nuovo_testo = json.dumps(nuovo, indent=1, ensure_ascii=False)  # stesso formato del file attuale (senza a capo finale)
    print("OK controlli: %d domande, %d punti" % (len(spec["domande"]), sum(d["punti"] for d in spec["domande"])))
    print("file: %s (%d byte) · indice: +1 voce (%d lavori)%s" % (spec["id"] + ".txt", len(testo), len(nuovo["lavori"]),
          " · sicurezza ora %s" % ora if ora else ""))
    if a.dry_run:
        print("DRY-RUN: nessun file scritto."); return 0
    open(os.path.join(a.fabbrica, spec["id"] + ".txt"), "w", newline="").write(testo)
    open(pind, "w", encoding="utf-8", newline="").write(nuovo_testo)
    print("scritti file e indice.")
    if a.commit or a.push:
        g = lambda *c: subprocess.run(["git", "-C", RADICE] + list(c), capture_output=True, text=True)
        g("add", os.path.join(a.fabbrica, spec["id"] + ".txt"), pind)
        r = g("commit", "-m", "Fabbrica: quiz %s (%s)\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" % (spec["id"], spec["classe"]))
        print("commit:", (r.stdout + r.stderr).strip().splitlines()[0] if (r.stdout + r.stderr).strip() else r.returncode)
        if r.returncode:
            return 4
        if a.push:
            for t in range(3):
                g("pull", "--rebase")
                r = g("push")
                if r.returncode == 0:
                    print("push OK"); break
                print("push non riuscito, riprovo tra 5 s"); import time; time.sleep(5)
            else:
                return 5
    print("PROSSIMO PASSO: attendere il giro del motore, poi: bash strumenti/leggi_fabbrica.sh %s (riservato)" % spec["id"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
