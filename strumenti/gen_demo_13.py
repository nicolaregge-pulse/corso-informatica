# -*- coding: utf-8 -*-
"""Demo, la giornata della 2INF del 13/10/2026, SENZA NOMI: chiusura dell'argomento con ripasso, verifica, recupero.

Pagine in docs/demo/giornata-13/:
  percorso/   il motore della verifica (docs/verifica) con la banca della 2INF; nella demo verifica e recupero sono aperti
              e il Modulo «Consegna» è sostituito da una pagina che spiega
  monitor/    il monitor della lezione (giri Veyon), con i nomi sostituiti
  cruscotto/  il cruscotto del prof (nel corso è cifrato; qui si vede aperto, senza nomi)
  modulo/     al posto del Modulo vero
Stessa numerazione «Allievo NN» della giornata del 12/10 (strumenti/gen_demo.py); i nomi nuovi prendono i numeri dopo.
Se dopo la sostituzione resta anche un solo nome, si ferma e non scrive niente.
Uso: python3 strumenti/gen_demo_13.py   (si rilancia a fine lezione, con risultati e retrospettiva)
"""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_demo as G

DOCS = G.DOCS
PRIV = os.path.join(os.path.dirname(DOCS), "..", "corso-informatica-riservato")
OUT = os.path.join(DOCS, "demo", "giornata-13")
BANCA = "2inf-versioning"


def mappa_nomi():
    m = G.nomi()
    altri = []
    for g in json.load(open(os.path.join(DOCS, "2inf-monitor", "monitor.json"), encoding="utf-8"))["giri"]:
        altri += [r["alunno"] for r in g["righe"]]
    try:
        altri += [a["allievo"] for a in json.load(open(os.path.join(DOCS, "verifica", "risultati", BANCA + ".json"), encoding="utf-8")).get("allievi", [])]
    except Exception:
        pass
    for n in altri:
        n = (n or "").strip()
        if re.match(r"^[A-ZÀ-Ý][\w'À-ÿ]+ [A-ZÀ-Ý]\.$", n) and n not in m:
            m[n] = "Allievo %02d" % (len(m) + 1)
    return m


def pagina(tit, corpo, stile=""):
    return ('<!doctype html><html lang="it"><head><meta name="robots" content="noindex"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>'
            'body{margin:0;background:#fbfaf7;color:#111;font:16px/1.5 system-ui,Segoe UI,Arial,sans-serif}.w{max-width:1100px;margin:0 auto;padding:20px 16px}'
            '.box{background:#fff;border:1px solid #ddd;border-radius:12px;padding:16px}%s</style></head><body><div class="w">%s</div>'
            '<script src="../../traccia.js"></script></body></html>' % (tit, stile, corpo))


def main():
    m = mappa_nomi()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    scritti = []
    # 1. il percorso
    P = os.path.join(OUT, "percorso")
    shutil.copytree(os.path.join(DOCS, "verifica"), P)
    json.dump({"verifica": "aperta", "recupero": "aperto", "recupero_per": "tutti"}, open(os.path.join(P, "stato", BANCA + ".json"), "w"))
    os.makedirs(os.path.join(OUT, "backlog"), exist_ok=True)
    shutil.copy(os.path.join(DOCS, "demo", "giornata", "backlog", "backlog.json"), os.path.join(OUT, "backlog", "backlog.json"))
    b = os.path.join(P, "banche", BANCA + ".js")
    t = open(b, encoding="utf-8").read()
    t = t.replace('"../2inf-backlog/backlog.json"', '"../backlog/backlog.json"')
    t = re.sub(r'https://docs\.google\.com/forms/[^"\']*', "../modulo/", t)
    t = t.replace("https://nicolaregge-pulse.github.io/corso-informatica/2inf-monitor/", "../monitor/")
    t = t.replace("id: '2inf-versioning-", "id: 'demo-2inf-versioning-").replace('id: "2inf-versioning-', 'id: "demo-2inf-versioning-')
    open(b, "w", encoding="utf-8").write(t)
    # 2. il monitor
    shutil.copytree(os.path.join(DOCS, "2inf-monitor"), os.path.join(OUT, "monitor"))
    for f in os.listdir(os.path.join(OUT, "monitor")):
        if f.startswith("monitor-"):
            os.remove(os.path.join(OUT, "monitor", f))
    mi = os.path.join(OUT, "monitor", "index.html")
    open(mi, "w", encoding="utf-8").write(open(mi, encoding="utf-8").read().replace('href="../2inf-voti/"', 'href="../../giornata/voti/"').replace('href="../2inf-backlog/"', 'href="../../giornata/backlog/"'))
    # 3. il cruscotto del prof, aperto e senza nomi
    c = json.load(open(os.path.join(PRIV, "dati", "cruscotto", "2inf-13-10-2026.json"), encoding="utf-8"))
    os.makedirs(os.path.join(OUT, "cruscotto"), exist_ok=True)
    open(os.path.join(OUT, "cruscotto", "index.html"), "w", encoding="utf-8").write(pagina(
        "Cruscotto del prof", "<h1>Il cruscotto del prof — 2INF · 13/10/2026</h1><p class='mu'>Nel corso questa pagina è cifrata: si apre solo con la password del docente e si aggiorna da sola ogni minuto. Dice quanti hanno finito, chi, e che cosa stanno facendo, per decidere quando aprire la verifica.</p>" + c["corpo"], c["stile"]))
    # 4. al posto del Modulo vero
    os.makedirs(os.path.join(OUT, "modulo"), exist_ok=True)
    open(os.path.join(OUT, "modulo", "index.html"), "w", encoding="utf-8").write(pagina(
        "Il Modulo «Consegna»", "<h1>Il Modulo «Consegna»</h1><div class='box'>Alla fine della verifica l'allievo preme «Copia il risultato e apri il Modulo»: il risultato è già copiato, nel Modulo Google sceglie «testo», preme Ctrl+V e Invia. Lo script porta la consegna su Git entro un minuto e il docente corregge; il voto compare nella pagina dei risultati. Nella demo il Modulo vero non si apre, per non mescolare le prove con le consegne della classe.</div><p><a href='javascript:history.back()'>Torna indietro</a></p>"))
    for radice, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith((".html", ".json", ".js")):
                continue
            p = os.path.join(radice, f)
            t = open(p, encoding="utf-8").read()
            t = G.anonimizza(t, m)
            if f == "index.html" and "traccia.js" not in t:
                t = t.replace("</body>", '<script src="../../traccia.js"></script></body>', 1)
                t = t.replace("<head>", '<head><meta name="robots" content="noindex">', 1)
            if f == "risultati.html" and "traccia.js" not in t:
                t = t.replace("</body>", '<script src="../../traccia.js"></script></body>', 1)
            open(p, "w", encoding="utf-8").write(t)
            scritti.append(p)
    resti = []
    for p in scritti:
        t = open(p, encoding="utf-8").read()
        for n in m:
            for parola in (n, n.split()[0]):
                if re.search(r"(?<![\w'])%s(?![\w'])" % re.escape(parola), t, re.I):
                    resti.append((os.path.relpath(p, DOCS), parola))
    if resti:
        shutil.rmtree(OUT)
        sys.exit("FERMO: nomi rimasti %s" % resti[:10])
    print("demo/giornata-13: %d file, %d nomi sostituiti" % (len(scritti), len(m)))


if __name__ == "__main__":
    main()
