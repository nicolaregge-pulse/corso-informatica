#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera le dispense riepilogative PER I RAGAZZI (1INF, 2INF, 3INF, 3INF-PC14, 4TI): MD + PDF in docs/dispense/riepilogo/.

Versione 1.0 (12/11/2026). PUBBLICO: nessun cognome, nessun voto. Dati in strumenti/dispense_riepilogo_dati.py.
Uso: python3 strumenti/genera_dispense_riepilogo.py [--versione 1.0] [--solo 1INF,4TI] [--senza-pdf]
     (--solo: nomi dei file, come 1INF, 2INF, 3INF, 3INF-PC14, 4TI; una versione già pubblicata non si riusa: nuovo numero)
PDF: python3 strumenti/md2pdf.py FILE.md 20261112 Dispensa-Riepilogo-<CLASSE>  ->  YYYYMMDD_Nome_vX.Y.pdf nella stessa cartella.
R6: 1INF italiano+arabo+cinese; 2INF e 4TI solo italiano; 3INF italiano e, solo nel file «-PC14», una riga in bangla sotto ogni frase.
"""
import os
import subprocess
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import dispense_riepilogo_dati as D  # noqa: E402

REPO = os.path.dirname(QUI)
OUT = os.path.join(REPO, "docs", "dispense", "riepilogo")


def righe_lingue(testi, lingue):
    return [testi[l] for l in lingue if l in testi]


def costruisci(classe, lingue, versione, nota_file):
    c = D.CLASSI[classe]
    L = []
    A = L.append
    A("# " + c["titolo"]["it"])
    A("")
    A("**Versione %s** — 12/11/2026 — dispensa per i ragazzi%s" % (versione, nota_file))
    A("")
    for t in righe_lingue(c["titolo"], lingue)[1:]:
        A(t)
        A("")
    for t in righe_lingue(c["intro"], lingue):
        A(t)
        A("")
    A("## 1. Quello che abbiamo fatto")
    A("")
    for num, (_, tit, voci) in enumerate(c["blocchi"], 1):
        A("### %s. %s" % (num, tit["it"]))
        A("")
        for t in righe_lingue(tit, lingue)[1:]:
            A(t)
            A("")
        for data, frasi in voci:
            primo = True
            for t in righe_lingue(frasi, lingue):
                A(("**%s** — " % data if primo else "") + t)
                A("")
                primo = False
    A("## 2. Lavori su Classroom")
    A("")
    for t in righe_lingue(c["compiti_intro"], lingue):
        A(t)
        A("")
    for i, x in enumerate(c["compiti"], 1):
        A("%d. %s" % (i, x))
    if c["compiti"]:
        A("")
    A("## 3. Quiz")
    A("")
    for t in righe_lingue(c["quiz_intro"], lingue):
        A(t)
        A("")
    for i, x in enumerate(c["quiz"], 1):
        A("%d. %s" % (i, x))
    A("")
    A("## 4. Parole da ricordare")
    A("")
    A("| Parola | Che cosa vuol dire |")
    A("|---|---|")
    for parola, sig in c["parole"]:
        A("| **%s** | %s |" % (parola, " · ".join(righe_lingue(sig, lingue))))
    A("")
    A("## 5. Se ti manca un lavoro")
    A("")
    fine = {"it": "Apri Classroom, cerca il lavoro che ti manca e consegnalo. Vai con calma, dal lavoro più vecchio al più nuovo. Tutti devono fare tutto.",
            "ar": "افتح Classroom وابحث عن العمل الناقص وسلّمه. اعمل بهدوء، من الأقدم إلى الأحدث. الجميع يجب أن يفعل كل شيء.",
            "zh": "打开 Classroom，找到你缺的作业并提交。慢慢来，从最旧的作业做到最新的。每个人都要完成所有作业。",
            "bn": "Classroom খোলো, যে কাজটি বাকি আছে সেটি খুঁজে জমা দাও। ধীরে ধীরে করো, পুরনো কাজ থেকে নতুন কাজের দিকে। সবাইকে সব কাজ করতে হবে।"}
    for t in righe_lingue(fine, lingue):
        A(t)
        A("")
    A("## Cronologia")
    A("")
    A("1. v%s (12/11/2026): da ARGOMENTI-SVOLTI-2026-27 v1.6, dal registro firmato e dai titoli dei compiti e dei quiz (1INF: compiti letti da Classroom alle 14:14 del 12/11). Il testo in arabo, cinese e bangla è scritto da Claude e non è stato riletto da un madrelingua." % versione)
    A("")
    return "\n".join(L)


def main():
    versione = "1.0"
    if "--versione" in sys.argv:
        versione = sys.argv[sys.argv.index("--versione") + 1]
    solo = sys.argv[sys.argv.index("--solo") + 1].split(",") if "--solo" in sys.argv else None
    os.makedirs(OUT, exist_ok=True)
    lavori = [("1INF", ["it", "ar", "zh"], "1INF", ""),
              ("2INF", ["it"], "2INF", ""),
              ("3INF", ["it"], "3INF", ""),
              ("3INF", ["it", "bn"], "3INF-PC14", " (con la riga in bangla, solo per il PC 14)"),
              ("4TI", ["it"], "4TI", "")]
    for classe, lingue, nome, nota in lavori:
        if solo and nome not in solo:
            continue
        md = costruisci(classe, lingue, versione, nota)
        path = os.path.join(OUT, "DISPENSA-RIEPILOGO-%s-v%s.md" % (nome, versione))
        open(path, "w", encoding="utf-8").write(md)
        print(path)
        if "--senza-pdf" not in sys.argv:
            r = subprocess.run([sys.executable, os.path.join(QUI, "md2pdf.py"), path, "20261112", "Dispensa-Riepilogo-" + nome], capture_output=True, text=True)
            print(r.stdout.strip() or r.stderr.strip())


if __name__ == "__main__":
    main()
