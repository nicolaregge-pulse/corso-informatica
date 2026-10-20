# Scarica testi da Genius (PC personale di Nicola, Windows 11)

Uso personale. Non mettere i testi nel repository e non darli ai ragazzi.

1. Installare Python da python.org (spuntare "Add Python to PATH").
2. Aprire il Prompt dei comandi e scrivere: pip install lyricsgenius
3. Creare un token gratuito su genius.com/api-clients ("New API Client", poi "Generate Access Token").
4. Impostare il token: setx GENIUS_TOKEN "IL_TUO_TOKEN"  (poi chiudere e riaprire il Prompt).
5. Mettere in questa cartella un file canzoni.txt, una riga per canzone: Titolo - Artista
6. Eseguire: python scarica_testi.py
