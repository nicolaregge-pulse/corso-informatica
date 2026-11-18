#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllo dei budget del materiale 1INF di mercoledi 18/11/2026 (v1.0, 18/11/2026).

Nato da un errore (REGISTRO-ERRORI-CLAUDE.md, #357): i budget dei tre preventivi (ufficio 450, studio 600, gaming 900 euro)
erano stati cambiati per errore in 500/600/1000 in alcuni file e non in altri; i ragazzi vedevano valori diversi in posti
diversi. Un errore nuovo corregge uno strumento (CLAUDE.md 00.2): questo.

UNICA FONTE dei valori: config/budget-1inf-1811.json (ufficio, studio, gaming). Il controllo FALLISCE se nelle VERSIONI
CORRENTI del materiale (la versione piu' alta di ogni famiglia di file) compare, vicino a «euro», «€» o «budget» (anche in arabo
e cinese), un numero che pare un budget (multiplo di 50 da 300 a 2000) e non e' uno dei valori della fonte. Gli indirizzi
internet e i percorsi (testo con una barra) non si leggono: un sito esterno puo' avere nel suo indirizzo un'altra cifra.
Le versioni vecchie (superate) non si controllano: restano come storia (R11.3).

DECISIONE 18/11 ore 09:5x: budget 500/600/1000 (v2.0 della fonte); le versioni 450/600/900 sono in config «non_usare_oggi» e non si guardano.
Che cosa guarda (versioni correnti = la piu' alta di ogni famiglia, tolte quelle «da non usare oggi»):
  riservato report/2026-11-18/*.md, *.pdf (dispense, pacchetti, piano, soluzioni, ricerca, siti di riserva) e
  report/2026-11-18/pdf-ragazzi/*.pdf e *.docx;  pubblico docs/dispense/mercoledi/*.html e modelli/*.docx,
  fabbrica/quiz-1inf-1811-ora6-confronto.txt, PROSSIME-LEZIONI.md, PROPOSTE-OGGI.md, docs/cruscotto/piano/1inf-2026-11-18.json.
Se il riservato manca, i file del riservato sono «non controllati» (GIALLO) e non contano come errore.

Uso: python3 strumenti/controlla_budget_1inf.py [--prova]
Uscita: 0 se nessun problema, 1 altrimenti. Non scrive niente. Nessun nome di allievo."""
import glob, json, os, re, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.dirname(QUI)
RIS = os.path.join(os.path.dirname(PUB), "corso-informatica-riservato")
CONFIG = os.path.join(PUB, "config", "budget-1inf-1811.json")
GIORNO = "2026-11-18"

PAROLA = re.compile(r"euro|€|\beur\b|budget|يورو|ميزانية|欧元|预算", re.I)
NUMERO = re.compile(r"(?<![A-Za-z0-9_.,/-])(\d{1,2}[.\s]\d{3}|\d{3,4})(?![A-Za-z0-9_/-]|[.,]\d)")   # solo lettere latine: «1000欧元» si legge
FINESTRA = 60   # caratteri di distanza dalla parola «euro» / «budget» (una frase come «un ufficio da 500 euro, uno studio da 600 e un gaming da 1000»)


def frammenti_esclusi(config=CONFIG):
    """nomi (frammenti, minuscoli) delle versioni «DA NON USARE oggi» (450/600/900): il controllo non le guarda"""
    d = json.load(open(config, encoding="utf-8"))
    return [x.lower() for x in d.get("non_usare_oggi", {}).get("frammenti", [])]


def valori_ammessi(config=CONFIG):
    d = json.load(open(config, encoding="utf-8"))
    b = d["budget"]
    assert set(b) == {"ufficio", "studio", "gaming"}, "la fonte deve avere ufficio, studio e gaming"
    return {int(v) for v in b.values()}


def senza_storia(riga):
    """toglie le note di storia «prima 450/600/900»: non sono un budget attuale"""
    if re.match(r"\s*\d+\.\s+v\d+\.\d+\s*\(", riga):   # riga del registro delle versioni (storia)
        return " "
    riga = re.sub(r"build da \d+ e \d+", " ", riga, flags=re.I)   # descrizione di pagine di un sito esterno
    return re.sub(r"prima\s+\d{3,4}(?:\s*[/,e]\s*\d{3,4})*", " ", riga, flags=re.I)


def senza_indirizzi(riga):
    """toglie indirizzi internet e percorsi (parole con una barra): non sono budget"""
    riga = re.sub(r"https?://\S+", " ", riga)
    return " ".join(p for p in riga.split(" ") if "/" not in p)


def sospetti_nel_testo(testo, ammessi):
    """[(numero_riga, numero, riga)] dei numeri che paiono un budget e non sono tra gli ammessi"""
    trovati = []
    for n, riga in enumerate(testo.splitlines(), 1):
        r = senza_indirizzi(senza_storia(riga))
        if not PAROLA.search(r):
            continue
        for m in NUMERO.finditer(r):
            v = int(re.sub(r"[.\s]", "", m.group(1)))
            if v in ammessi or v < 300 or v > 2000 or v % 50:
                continue
            vicino = r[max(0, m.start() - FINESTRA):m.end() + FINESTRA]
            if PAROLA.search(vicino):
                trovati.append((n, v, riga.strip()[:90]))
    return trovati


def _famiglia(percorso):
    """(nome della famiglia, versione come tupla): «X-v1.2.md» -> («X», (1, 2)); «x-v1-2.docx» -> («x», (1, 2)); None se senza versione"""
    nome = os.path.basename(percorso)
    m = re.match(r"^(?:\d{8}_)?(.*?)[-_]v(\d+)[.-](\d+)\.[A-Za-z]+$", nome)
    if not m:
        return None
    return (os.path.dirname(percorso) + "/" + m.group(1).lower(), (int(m.group(2)), int(m.group(3))))


def versioni_correnti(file_):
    """la versione piu' alta di ogni famiglia; i file senza versione restano tutti"""
    migliori, senza = {}, []
    for f in file_:
        k = _famiglia(f)
        if k is None:
            senza.append(f)
        elif k[0] not in migliori or k[1] > migliori[k[0]][0]:
            migliori[k[0]] = (k[1], f)
    return sorted(senza + [v[1] for v in migliori.values()])


def testo_di(f):
    if f.endswith(".pdf"):
        r = subprocess.run(["pdftotext", "-layout", f, "-"], capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            raise RuntimeError("pdftotext")
        return r.stdout
    if f.endswith(".docx"):
        from docx import Document
        d = Document(f)
        parti = [p.text for p in d.paragraphs]
        for t in d.tables:
            for riga in t.rows:
                parti += [c.text.replace("\n", " ") for c in riga.cells]
        return "\n".join(parti)
    return open(f, encoding="utf-8", errors="replace").read()


def file_da_controllare(pub=PUB, ris=RIS, config=CONFIG):
    rep = os.path.join(ris, "report", GIORNO)
    riservato = []
    for pat in ("*.md", "*.pdf", "pdf-ragazzi/*.pdf", "pdf-ragazzi/*.docx"):
        riservato += glob.glob(os.path.join(rep, pat))
    # solo le dispense e i modelli del 18/11 e i documenti del piano: i PDF dei ragazzi di altre cose non ci sono in questa cartella
    pubblico = (glob.glob(os.path.join(pub, "docs", "dispense", "mercoledi", "*.html")) +
                glob.glob(os.path.join(pub, "docs", "dispense", "mercoledi", "modelli", "*.docx")))
    fissi = [os.path.join(pub, "fabbrica", "quiz-1inf-1811-ora6-confronto.txt"), os.path.join(pub, "PROSSIME-LEZIONI.md"),
             os.path.join(pub, "PROPOSTE-OGGI.md"), os.path.join(pub, "docs", "cruscotto", "piano", "1inf-%s.json" % GIORNO)]
    esclusi = frammenti_esclusi(config)
    nuovo = lambda lista: [f for f in lista if not any(x in os.path.basename(f).lower() for x in esclusi)]
    return versioni_correnti(nuovo(riservato)), versioni_correnti(nuovo(pubblico)) + [f for f in fissi if os.path.isfile(f)]


def controlla(pub=PUB, ris=RIS, config=CONFIG):
    """(problemi, non_controllati, n_file): problemi = [«file:riga: numero»]"""
    ammessi = valori_ammessi(config)
    ris_f, pub_f = file_da_controllare(pub, ris, config)
    problemi, non_controllati = [], []
    if not os.path.isdir(os.path.join(ris, "report")):
        non_controllati.append("riservato non trovato accanto: file del riservato non controllati")
        ris_f = []
    for f in ris_f + pub_f:
        try:
            testo = testo_di(f)
        except Exception as e:
            non_controllati.append("%s (%s)" % (os.path.basename(f), type(e).__name__))
            continue
        for n, v, riga in sospetti_nel_testo(testo, ammessi):
            base = f.replace(ris + "/", "riservato/").replace(pub + "/", "")
            problemi.append("%s riga %d: %d euro non e' uno dei budget %s" % (base, n, v, "/".join(str(x) for x in sorted(ammessi))))
    return problemi, non_controllati, len(ris_f) + len(pub_f)


def prova():
    """prove dello strumento su testo finto: deve trovare gli errori messi apposta e non dare falsi allarmi"""
    am = {500, 600, 1000}
    ok = tot = 0

    def p(nome, cond):
        nonlocal ok, tot
        tot += 1; ok += bool(cond); print(("OK   " if cond else "NO   ") + nome)
    p("450 euro trovato", len(sospetti_nel_testo("Il cliente ufficio ha 450 euro.", am)) == 1)
    p("budget 900 trovato", len(sospetti_nel_testo("Il budget del gaming e' 900.", am)) == 1)
    p("arabo: 450 يورو trovato", len(sospetti_nel_testo("الميزانية: 450 يورو", am)) == 1)
    p("cinese: 预算：900欧元 trovato", len(sospetti_nel_testo("预算：900欧元", am)) == 1)
    p("500/600/1000 euro ammessi", not sospetti_nel_testo("Budget: 500 euro, studio 600 euro, gaming 1.000 euro", am))
    p("nota di storia «prima 450/600/900» ammessa", not sospetti_nel_testo("budget decisi (prima 450/600/900, proposta mia)", am))
    p("prezzo di un pezzo (80 euro, 358,90 euro) ammesso", not sospetti_nel_testo("Costa 80 euro. Un Ryzen a 358,90 euro.", am))
    p("totale d'esempio 540 euro ammesso", not sospetti_nel_testo("es. 540 euro", am))
    p("indirizzo con 900 ammesso", not sospetti_nel_testo("Apri https://x.it/pc-gaming-900-euro", am))
    p("indirizzo con 1000 ammesso", not sospetti_nel_testo("Apri https://configmon.it/configurazioni/pc-gaming-1000-euro e `/configurazioni/pc-gaming-1000-euro`", am))
    p("numero lontano da euro ammesso", not sospetti_nel_testo("Punteggio 19.600 e 1000 pagine; poi un testo molto lungo che non finisce mai e non parla di niente, scritto per fare distanza, e infine euro", am))
    p("riga senza euro e senza budget ammessa", not sospetti_nel_testo("Il PC ha 500 GB di disco", am))
    p("versione esclusa dalla lista «da non usare»", frammenti_esclusi() and "ora2-v1.2" in frammenti_esclusi())
    p("versione corrente: v1.3 batte v1.2", versioni_correnti(["/x/A-v1.2.md", "/x/A-v1.3.md", "/x/B-v1.0.md"]) == ["/x/A-v1.3.md", "/x/B-v1.0.md"])
    p("versione corrente nei nomi dei modelli (v1-2 contro v1-10)", versioni_correnti(["/x/m-v1-2.docx", "/x/m-v1-10.docx"]) == ["/x/m-v1-10.docx"])
    p("prefisso data del PDF ignorato", versioni_correnti(["/x/20261117_P_v1.1.pdf", "/x/20261118_P_v1.2.pdf"]) == ["/x/20261118_P_v1.2.pdf"])
    print("%d/%d" % (ok, tot))
    return 0 if ok == tot else 1


def main():
    if "--prova" in sys.argv:
        return prova()
    problemi, nc, n = controlla()
    for x in nc:
        print("GIALLO: " + x)
    for x in problemi:
        print("ROSSO: " + x)
    if problemi:
        print("ESITO: ROSSO (%d) su %d file" % (len(problemi), n))
        return 1
    print("ESITO: VERDE: %d file controllati, nessun budget diverso da %s" % (n, "/".join(str(x) for x in sorted(valori_ammessi()))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
