#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove di controlla_leggibilita.py (v1.0, 13/11/2026). Uso: python3 strumenti/prova_controlla_leggibilita.py
Ogni caso: testo MD piccolo, codice atteso presente/assente. Esce 1 se un caso fallisce."""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controlla_leggibilita as c

LUOGHI = c.LUOGHI


def esegui(testo, ext=".md"):
    with tempfile.NamedTemporaryFile("w", suffix=ext, delete=False, encoding="utf-8") as f:
        f.write(testo)
    try:
        righe = c.leggi_file(f.name)
    finally:
        os.unlink(f.name)
    return c.controlla(righe, 14, 25, LUOGHI)


def ha(av, codice, gravita=None):
    return any(a[3] == codice and (gravita is None or a[2] == gravita) for a in av)


CASI = [
    ("01 frase corta: nessun avviso LUNGA", "Apri il Blocco note.\n", lambda a: not ha(a, "LUNGA")),
    ("02 frase di 16 parole: AVVISO LUNGA", "Nel Blocco note scrivi il nome della tua cartella e poi premi il tasto Invio sulla tastiera del computer.\n",
     lambda a: ha(a, "LUNGA", "AVVISO") and not ha(a, "LUNGA", "GRAVE")),
    ("03 frase di 30 parole: GRAVE LUNGA", " ".join(["parola"] * 30) + ".\n", lambda a: ha(a, "LUNGA", "GRAVE")),
    ("04 esercizio con «Per esempio»: ok", "Nel Blocco note scrivi 3 righe (per esempio: telefono, televisione, console).\n",
     lambda a: not ha(a, "SENZAESEMPIO")),
    ("05 esercizio con testo già dato: ok", "Nel Blocco note scrivi `ciao` e premi Invio.\n", lambda a: not ha(a, "SENZAESEMPIO")),
    ("06 esercizio senza esempio: GRAVE", "Nel Blocco note scrivi 4 righe, una per ogni regola. Dopo i due punti scrivi con parole tue.\n",
     lambda a: ha(a, "SENZAESEMPIO", "GRAVE")),
    ("07 parola astratta senza spiegazione: AVVISO", "La privacy è importante.\n\nApri il Blocco note.\n", lambda a: ha(a, "ASTRATTA")),
    ("08 parola astratta con spiegazione: ok", "La privacy (cioè i tuoi dati personali) è importante.\n", lambda a: not ha(a, "ASTRATTA")),
    ("09 passo senza luogo: AVVISO DOVE", "Scegli UNA storia.\n", lambda a: ha(a, "DOVE")),
    ("10 passo con luogo: ok", "Apri la cartella Documenti.\n", lambda a: not ha(a, "DOVE")),
    ("11 arabo e cinese saltati", "Apri il Blocco note.\n\nافتح المفكرة وافتح المفكرة وافتح المفكرة وافتح المفكرة وافتح المفكرة وافتح المفكرة.\n\n打开记事本。" * 1 + "\n",
     lambda a: not ha(a, "LUNGA")),
    ("12 codice, tabelle e commenti saltati", "```\n" + " ".join(["x"] * 40) + "\n```\n| " + " ".join(["y"] * 40) + " |\n<!-- " + " ".join(["z"] * 40) + " -->\n",
     lambda a: not a),
    ("13 [regola PPP] pronome vago: AVVISO VAGO", "Nel Blocco note scrivi quello, poi premi Invio.\n", lambda a: ha(a, "VAGO")),
    ("14 [regola PPP] «ciò che hai visto» vago", "Nel Blocco note scrivi ciò che hai visto.\n", lambda a: ha(a, "VAGO")),
    ("15 [regola PPP] questo + nome non è vago", "Nel Blocco note scrivi il nome di questo file.\n", lambda a: not ha(a, "VAGO")),
    ("16 [regola PPP] consegna impersonale: SOGGETTO", "Nel Blocco note si scrive il proprio nome.\n", lambda a: ha(a, "SOGGETTO")),
    ("17 [regola PPP] consegna senza oggetto: COSA", "Nel Blocco note scrivi e premi Invio.\n", lambda a: ha(a, "COSA")),
    ("18 [regola PPP] consegna completa: nessun VAGO/SOGGETTO/COSA/COMPLETA",
     "Nel Blocco note scrivi il nome del tuo animale preferito. Per esempio: `gatto`.\n",
     lambda a: not any(ha(a, x) for x in ("VAGO", "SOGGETTO", "COSA", "COMPLETA"))),
    ("19 [regola PPP] scrivi senza dove né esempio: COMPLETA", "Scrivi in una riga la tua regola con parole tue.\n", lambda a: ha(a, "COMPLETA")),
    ("20 allineamento: `1 PASSWORD` non nel titolo", "### 1) Le regole del laboratorio\n\nLa password è tua.\n\nNel Blocco note scrivi `1 PASSWORD`.\n",
     lambda a: ha(a, "ALLINEA")),
    ("21 HTML: salta lang=ar e tabelle", "<html><body><p>Apri il Blocco note.</p><p lang='ar'>" + "كلمة " * 30 + "</p><table><tr><td>" + "a " * 40 + "</td></tr></table></body></html>",
     lambda a: not ha(a, "LUNGA")),
]

if __name__ == "__main__":
    ko = 0
    for nome, testo, ok in CASI:
        av = esegui(testo, ".html" if nome.startswith("21") else ".md")
        esito = ok(av)
        ko += (not esito)
        print(("OK   " if esito else "FALLITO ") + nome + ("" if esito else "  -> " + str([(x[3], x[2]) for x in av])))
    print(f"{len(CASI) - ko}/{len(CASI)} casi superati")
    sys.exit(1 if ko else 0)
