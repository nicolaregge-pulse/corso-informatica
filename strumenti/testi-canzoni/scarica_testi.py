"""Scarica i testi delle canzoni da Genius (uso personale, PC di Nicola).

Uso: python scarica_testi.py
Legge  canzoni.txt  (una canzone per riga: Titolo - Artista)
Scrive un file .txt per canzone nella cartella  testi/
Il token Genius sta nella variabile d'ambiente GENIUS_TOKEN (mai nel repository).
I testi NON vanno nel repository: la cartella testi/ e' esclusa da .gitignore.
"""
import os
import re
import sys
import time

import lyricsgenius

PAUSA_SECONDI = 5  # pausa tra una canzone e l'altra, per non farsi bloccare


def nome_sicuro(testo):
    return re.sub(r'[\\/:*?"<>|]', "_", testo).strip()


def main():
    token = os.environ.get("GENIUS_TOKEN")
    if not token:
        sys.exit("Manca GENIUS_TOKEN (vedi LEGGIMI.md).")
    if not os.path.exists("canzoni.txt"):
        sys.exit("Manca il file canzoni.txt nella cartella.")

    os.makedirs("testi", exist_ok=True)
    genius = lyricsgenius.Genius(token, remove_section_headers=False,
                                 skip_non_songs=True, verbose=False)

    with open("canzoni.txt", encoding="utf-8") as f:
        righe = [r.strip() for r in f if r.strip() and not r.startswith("#")]

    for riga in righe:
        titolo, _, artista = riga.partition(" - ")
        song = genius.search_song(titolo.strip(), artista.strip() or None)
        if song is None:
            print(f"NON TROVATA: {riga}")
            continue
        percorso = os.path.join("testi", nome_sicuro(f"{song.artist} - {song.title}") + ".txt")
        with open(percorso, "w", encoding="utf-8") as out:
            out.write(f"{song.title} - {song.artist}\n\n{song.lyrics}\n")
        print(f"OK: {percorso}")
        time.sleep(PAUSA_SECONDI)


if __name__ == "__main__":
    main()
