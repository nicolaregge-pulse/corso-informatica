#!/usr/bin/env python3
"""Controllo dei PDF per i ragazzi e della loro copia scaricabile (v1.0, 13/11/2026; errori #330 e #331).

Uso: python3 strumenti/controlla_pdf_ragazzi.py <file.pdf> [altro.pdf ...]
Controlla (nessun controllo e' bloccante da solo: esce con 1 se c'e' un GRAVE):
 1. NOME del file: solo lettere minuscole latine, cifre, trattini e punto; niente spazi, accenti o maiuscole (un nome
    strano non si scaricava da Classroom, #330). GRAVE.
 2. NOTE TECNICHE dentro il PDF dei ragazzi (versione, changelog, «da confermare», «non provato», nomi di file o di
    regole, «Claude», «docente»): il PDF per i ragazzi ha solo passi, screenshot e consegna (#331). GRAVE.
 3. FITTEZZA: parole per pagina oltre la soglia (150: scelta di Claude, da confermare dal docente). AVVISO.
 4. COPIA SCARICABILE: se il file sta in docs/dispense/oggi/ deve essere un PDF vero (intestazione %PDF) e il commit
    deve essere gia su origin/main (altrimenti il link non funziona ancora). GRAVE.
"""
import os, re, subprocess, sys

SOGLIA_PAROLE_PAGINA = 150
TECNICHE = [r"\bversione\s*\d", r"\bv\d+\.\d+\b", r"changelog", r"da confermare", r"non provato", r"\bR\d{1,2}\b",
            r"\bclaude\b", r"\bdocente\b", r"\.md\b", r"report/", r"strumenti/", r"\bPUBB\b", r"\bfonte:"]


def testo_pagine(pdf):
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        raise RuntimeError("pdftotext: " + out.stderr[:100])
    return out.stdout.split("\f")


def controlla(pdf, pub=None):
    gravi, avvisi = [], []
    nome = os.path.basename(pdf)
    if not re.fullmatch(r"[a-z0-9][a-z0-9.\-]*\.pdf", nome):
        gravi.append("nome del file non sicuro per il download (solo minuscole latine, cifre, trattini): " + nome)
    with open(pdf, "rb") as f:
        if f.read(5) != b"%PDF-":
            gravi.append("non e' un PDF vero (manca l'intestazione %PDF)")
            return gravi, avvisi
    try:
        pagine = [p for p in testo_pagine(pdf) if p.strip()]
    except Exception as e:
        return gravi + ["testo non leggibile: %s" % e], avvisi
    for n, p in enumerate(pagine, 1):
        for rx in TECNICHE:
            m = re.search(rx, p, re.I)
            if m:
                gravi.append("pagina %d: nota tecnica nel PDF dei ragazzi: «%s»" % (n, m.group(0)))
                break
        parole = len(p.split())
        if parole > SOGLIA_PAROLE_PAGINA:
            avvisi.append("pagina %d: %d parole (oltre %d, pagina fitta)" % (n, parole, SOGLIA_PAROLE_PAGINA))
    ap = os.path.abspath(pdf)
    if "/docs/dispense/oggi/" in ap:
        repo = ap.split("/docs/dispense/oggi/")[0]
        rel = os.path.relpath(ap, repo)
        try:
            subprocess.run(["git", "-C", repo, "fetch", "-q"], timeout=60)
            r = subprocess.run(["git", "-C", repo, "cat-file", "-e", "origin/main:" + rel], capture_output=True)
            if r.returncode != 0:
                gravi.append("la copia scaricabile NON e' ancora su origin/main: il link non funziona")
        except Exception as e:
            avvisi.append("push non verificato: %s" % e)
    return gravi, avvisi


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    esito = 0
    for f in sys.argv[1:]:
        g, a = controlla(f)
        print(("ROSSO" if g else "VERDE" if not a else "GIALLO") + ": " + os.path.basename(f))
        for x in g: print("  GRAVE:", x)
        for x in a: print("  avviso:", x)
        if g: esito = 1
    sys.exit(esito)
