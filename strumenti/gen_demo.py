# -*- coding: utf-8 -*-
"""Demo, ambiente 2: la giornata della 2INF del 12/10/2026, già finita, SENZA NOMI.

Copia le pagine pubbliche della lezione in docs/demo/giornata/, sostituisce ogni nome
(«Nome I.» e il nome da solo) con «Allievo NN», aggiunge a ogni pagina il tracciamento
della demo (docs/demo/traccia.js) e manda i link del gioco alla versione pubblica.
Se dopo la sostituzione resta anche un solo nome, si ferma e non scrive niente.

Uso:  python3 strumenti/gen_demo.py
"""
import json, os, re, shutil, sys

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
OUT = os.path.join(DOCS, "demo", "giornata")
GIOCO = "../gioco/"
GIOCO_PUBBLICO_VERSIONI = "#"
GRAFO = "https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/"
PAGINE = {  # cartella pubblica -> cartella nella demo
    "compito/2inf-20261012-documento": "compito",
    "2inf-backlog": "backlog",
    "2inf-voti": "voti",
    "2inf-monitor": "monitor",
    "2inf-novita": "novita",
    "2inf-top": "classifica",
}


def nomi():
    elenco = []
    for x in json.load(open(os.path.join(DOCS, "2inf-voti/voti.json"), encoding="utf-8"))["voti"]:
        elenco.append(x["alunno"])
    for x in json.load(open(os.path.join(DOCS, "2inf-backlog/backlog.json"), encoding="utf-8"))["voci"]:
        elenco.append(x["alunno"])
    for g in json.load(open(os.path.join(DOCS, "2inf-monitor/monitor.json"), encoding="utf-8"))["giri"]:
        for r in g["righe"]:
            elenco.append(r["alunno"])
    visti = []
    for n in elenco:
        n = (n or "").strip()
        if re.match(r"^[A-ZÀ-Ý][\w'À-ÿ]+ [A-ZÀ-Ý]\.$", n) and n not in visti:
            visti.append(n)
    return {n: "Allievo %02d" % (i + 1) for i, n in enumerate(visti)}


def anonimizza(testo, mappa):
    for n, a in sorted(mappa.items(), key=lambda x: -len(x[0])):
        testo = testo.replace(n, a)
    for n, a in mappa.items():
        testo = re.sub(r"(?<![\w'])%s(?![\w'])" % re.escape(n.split()[0]), a, testo, flags=re.I)
    return testo


SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
SPIEGA = {  # pagine che nella demo non si aprono davvero: al loro posto una pagina che spiega
    "modulo": ("Il Modulo Google", "Qui l'allievo apre il Modulo Google della lezione: il Feedback sulla teoria oppure la «Consegna» con la sua Pull Request (Titolo, Cosa cambia, Dove, Perché). Appena preme «Invia», lo script porta la risposta su Git entro un minuto e la PR compare nel backlog. Nella demo il Modulo vero non si apre, per non mescolare le prove con le consegne della classe."),
    "valutazione": ("Valutazione dei singoli (solo prof)", "Pagina cifrata, si apre solo con la password del docente: per ogni allievo, in ordine alfabetico del cognome, il voto proposto, le PR inviate e quelle entrate nel gioco, il Feedback e il motivo. Nella demo non si apre perché contiene i nomi veri."),
}


def percorsi(testo, cartella):
    testo = re.sub(r"https://docs\.google\.com/forms/[^\"']*", "../modulo/", testo)
    testo = testo.replace(SITO + "2inf-valutazione/", "../valutazione/")
    for src, dst in PAGINE.items():
        testo = testo.replace(SITO + src + "/", "../%s/" % dst)
    for src, dst in PAGINE.items():
        testo = testo.replace("../%s/" % src, "../%s/" % dst).replace("../" + src + "'", "../" + dst + "'")
    testo = re.sub(r"\.\./giochi/treno-blindato/versioni/versioni\.json", "versioni.json", testo)
    testo = re.sub(r"\.\./giochi/treno-blindato/versioni/(v[\w.-]*/?)?", GIOCO, testo)
    testo = testo.replace("../giochi/treno-blindato/", GIOCO).replace("../giochi/grafo/", GRAFO)
    if cartella == "compito":
        testo = testo.replace("../../2inf-", "../").replace("../../giochi/treno-blindato/", GIOCO)
    return testo


def main():
    mappa = nomi()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    scritti = []
    for src, dst in PAGINE.items():
        shutil.copytree(os.path.join(DOCS, src), os.path.join(OUT, dst))
    shutil.copy(os.path.join(DOCS, "giochi/treno-blindato/versioni/versioni.json"), os.path.join(OUT, "backlog", "versioni.json"))
    shutil.copytree(os.path.join(DOCS, "giochi/treno-blindato"), os.path.join(OUT, "gioco"),
                    ignore=shutil.ignore_patterns("versioni", "strumenti", "sw.js", "*.md"))
    from PIL import Image  # la foto della lavagna: in alto c'è un ragazzo riflesso nel vetro, si taglia sotto
    lj = os.path.join(OUT, "compito", "lavagna-versioni.jpg")
    im = Image.open(lj)
    w, h = im.size
    im.crop((0, int(h * 0.135), w, int(h * 0.80))).save(lj, quality=85)
    for radice, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith((".html", ".json", ".webmanifest")):
                continue
            p = os.path.join(radice, f)
            t = open(p, encoding="utf-8").read()
            t = percorsi(anonimizza(t, mappa), os.path.basename(radice))
            if os.path.basename(radice) == "gioco":
                t = re.sub(r"navigator\.serviceWorker\.register\([^)]*\)", "Promise.resolve()", t)
                t = t.replace("versioni/", GIOCO_PUBBLICO_VERSIONI)
            if f == "index.html" and "traccia.js" not in t:
                t = t.replace("</body>", '<script src="../../traccia.js"></script></body>', 1)
                t = t.replace("<head>", '<head><meta name="robots" content="noindex">', 1)
            open(p, "w", encoding="utf-8").write(t)
            scritti.append(p)
    stile = ("body{margin:0;background:#fbfaf7;color:#111;font:17px/1.5 system-ui,Segoe UI,Arial,sans-serif}"
             ".w{max-width:720px;margin:0 auto;padding:24px 16px}.box{background:#fff;border:1px solid #ddd;border-radius:12px;padding:16px}")
    for cart, (tit, testo) in SPIEGA.items():
        os.makedirs(os.path.join(OUT, cart), exist_ok=True)
        p = os.path.join(OUT, cart, "index.html")
        open(p, "w", encoding="utf-8").write(
            '<!doctype html><html lang="it"><head><meta name="robots" content="noindex"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head>'
            '<body><div class="w"><h1>%s</h1><div class="box">%s</div><p><a href="javascript:history.back()">Torna indietro</a></p></div>'
            '<script src="../../traccia.js"></script></body></html>' % (tit, stile, tit, testo))
        scritti.append(p)
    resti = []
    for p in scritti:
        t = open(p, encoding="utf-8").read()
        for n in mappa:
            for parola in (n, n.split()[0]):
                if re.search(r"(?<![\w'])%s(?![\w'])" % re.escape(parola), t, re.I):
                    resti.append((os.path.relpath(p, DOCS), parola))
    if resti:
        shutil.rmtree(OUT)
        sys.exit("FERMO: nomi rimasti %s" % resti[:10])
    print("demo/giornata: %d file, %d nomi sostituiti" % (len(scritti), len(mappa)))


if __name__ == "__main__":
    main()
