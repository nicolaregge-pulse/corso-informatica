#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prova di strumenti/controlla_coerenza_materiale.py (16/11/2026): parte dal materiale VERO letto in memoria, controlla che la base non abbia
errori e poi introduce 14 errori, uno alla volta, controllando che lo strumento li trovi (e nel punto giusto). Non scrive nulla su disco.
Uso: python3 strumenti/prova_controlla_coerenza_materiale.py   (oppure controlla_coerenza_materiale.py --prova)"""
import json, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import controlla_coerenza_materiale as C

RIS = os.environ.get("RISERVATO", C.RIS0)
PUB = os.path.dirname(QUI)


def carica():
    """materiale vero in un dizionario: testo per i file di testo, 'PDF' / 'DOCX' per i file binari"""
    f = {}
    def leggi_cartella(base, rel, estensioni_testo, ricorsivo=False):
        d = os.path.join(base, rel)
        if not os.path.isdir(d): return
        for nome in os.listdir(d):
            p = os.path.join(d, nome)
            if os.path.isdir(p):
                if ricorsivo: leggi_cartella(base, rel + "/" + nome, estensioni_testo, ricorsivo)
                continue
            chiave = ("R/" if base == RIS else "P/") + rel + "/" + nome
            if nome.endswith(".pdf"): f[chiave] = "PDF"
            elif nome.endswith(".docx") or nome.endswith(".zip"): f[chiave] = "DOCX"
            elif nome.endswith(estensioni_testo):
                try: f[chiave] = open(p, encoding="utf-8").read()
                except Exception: pass
    leggi_cartella(RIS, C.REPORT, (".md", ".json"))
    leggi_cartella(RIS, C.REPORT + "/pdf-ragazzi", (".json",))
    leggi_cartella(RIS, "generatori", ("cruscotto_lezione.py",))
    leggi_cartella(PUB, "docs/lunedi", (".html",))
    leggi_cartella(PUB, C.DISPENSE, (".md",))
    leggi_cartella(PUB, C.DISPENSE + "/modelli", (".md",))
    leggi_cartella(PUB, "fabbrica", (".json", ".txt"))
    leggi_cartella(PUB, "strumenti", ("coerenza_materiale_spec.json",))
    # pagine e file che index.html e link.html linkano fuori da docs/lunedi (cartella docs/stage e i suoi file)
    f["P/docs/stage"] = "DIR"
    for nome in os.listdir(os.path.join(PUB, "docs/stage")): f["P/docs/stage/" + nome] = "FILE"
    return f


def esegui(finto):
    m = C.Mat(finto=finto)
    return C.controlla(m)


def trova_ultimo(finto, base):
    pref = "R/" + C.REPORT + "/" + base + "-v"
    v = []
    for k in finto:
        m = re.match(r"^" + re.escape(pref) + r"(\d+)\.(\d+)\.md$", k)
        if m: v.append((int(m.group(1)), int(m.group(2)), k))
    return sorted(v)[-1][2]


def main():
    if not os.path.isdir(RIS):
        print("prova non eseguibile: repository riservato non trovato (%s)" % RIS); return 2
    base = carica()
    ok = True; n = 0
    def prova(nome, mutazione, check_atteso):
        nonlocal ok, n
        f = dict(base); mutazione(f)
        E = esegui(f)
        trovati = [r for r in E.errori if r[1].startswith(check_atteso)]
        n += 1
        if trovati: print("OK     %-62s -> trovato: %s" % (nome, trovati[0][2][:90]))
        else:
            ok = False; print("FALLITA %-61s -> lo strumento NON ha trovato l'errore (%s)" % (nome, check_atteso))
    # base
    E0 = esegui(dict(base)); n += 1
    if E0.errori:
        ok = False; print("FALLITA base: il materiale vero ha %d errori:" % len(E0.errori))
        for r in E0.errori[:6]: print("   ", r[1], r[2][:110])
    else: print("OK     base: nessun errore sul materiale vero (%d controlli OK)" % sum(1 for r in E0.righe if r[0] == "OK"))
    R = "R/" + C.REPORT + "/"
    def edit(chiave_o_base, vecchio, nuovo, ultimo=True):
        def f(d):
            k = trova_ultimo(d, chiave_o_base) if ultimo else chiave_o_base
            assert vecchio in d[k], (k, vecchio)
            d[k] = d[k].replace(vecchio, nuovo, 1)
        return f
    prova("dispensa ora 1: «ultimo commit» al posto di «URL del sito»", edit(C.DISP[1], "`URL del sito:`", "`Ultimo commit:`"), "04 cima")
    prova("semplificato ora 2: rimando a una pagina", edit(C.SEMPL[2][0], "Dubbio? Dispensa Ora 2, capitolo 6 · Presenze stage.", "Dubbio? Dispensa Ora 2, pagine 32-43."), "06 semplificati")
    prova("semplificato ora 1: capitolo che non esiste", edit(C.SEMPL[1][0], "capitolo 6 · Consegna", "capitolo 9 · Consegna"), "06 semplificati")
    prova("pacchetto ora 3: 3 screenshot invece di 4", edit(C.PACC[3], "4 screenshot, con una riga", "3 screenshot, con una riga"), "02 screenshot")
    prova("pacchetto ora 2: elenco file senza presenze.html", edit(C.PACC[2], "style.css, presenze.html, CHANGELOG.md; 4)", "style.css, CHANGELOG.md; 4)"), "03 file")
    def senza_slot(d):
        k = [x for x in d if "modelli/3inf-modello-documento-ora2-v" in x and x.endswith(".md")]
        k = sorted(k)[-1]; d[k] = d[k].replace("### presenze.html\n\n(Incolla qui il codice del file.)\n\n", "")
    prova("modello ora 2: manca il file presenze.html", senza_slot, "03 file")
    def quiz_diverso(d):
        k = "P/docs/lunedi/index.html"; d[k] = d[k].replace("1FAIpQLSeCJhPRl8AGm1xYded6kjQp4k", "1FAIpQLSeCJhPRl8AGm1xYded6kjQp4X", 1)
    prova("pagina index.html: link del quiz ora 1 sbagliato", quiz_diverso, "07 quiz")
    prova("dispensa ora 2: repository fisso `sito-personale`", edit(C.DISP[2], "Apri il tuo repository su GitHub.", "Apri il tuo repository `sito-personale` su GitHub."), "05 repository")
    def senza_pdf(d): del d["P/docs/dispense/lunedi/3inf-ora3-dispensa-v1-4.pdf"]
    prova("sito: manca il PDF dell'ultima dispensa ora 3", senza_pdf, "01 versioni")
    def vecchio_semplificato(d):
        for p in C.PAGINE:
            d["P/" + p] = d["P/" + p].replace("3inf-ora1-semplificato-v1-1.pdf", "3inf-ora1-semplificato-v1-0.pdf")
    prova("pagine: citano il semplificato v1.0 invece della v1.1", vecchio_semplificato, "01 versioni")
    def font_piccolo(d):
        k = [x for x in d if x.endswith("semplificati-v1.1-font.json")][0]
        j = json.loads(d[k]); j["3inf-ora3-semplificato-v1.1.pdf"]["font_px"] = 9.5; d[k] = json.dumps(j)
    prova("semplificato ora 3: font 9,5 px", font_piccolo, "06 semplificati")
    prova("pacchetto ora 1: titolo cambiato", edit(C.PACC[1], "```\n16/11 Ora 1: Il mio sito su GitHub\n```", "```\n16/11 Ora 1-2: Il mio sito su GitHub\n```"), "08 titoli")
    prova("dispensa ora 3: primo giorno dello stage 24/11", edit(C.DISP[3], "Primo giorno dello stage: lunedì 23/11/2026", "Primo giorno dello stage: lunedì 24/11/2026"), "09 date")
    def cruscotto_vecchio(d):
        k = "R/generatori/cruscotto_lezione.py"; d[k] = d[k] + "\n# chiedi al docente se va bene o se creare sito-personale\n"
    prova("cruscotto di lezione: chiede di ricreare il repository", cruscotto_vecchio, "05 repository")
    print("%s: %d prove" % ("TUTTE SUPERATE" if ok else "ALCUNE FALLITE", n))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
