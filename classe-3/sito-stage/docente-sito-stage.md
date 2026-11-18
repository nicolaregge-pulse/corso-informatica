# Sito 3INF: Stage e Presenze — nota per il docente

**Versione 1.1** — 18/11/2026 · documento interno (non per i ragazzi)

## 01 Che cosa c'è

1. Tutorial guidato (15 passi a bottoni «Ho fatto», bangla solo con `?pc=14`): `docs/3inf/sito-stage/index.html` (generato da `strumenti/genera_tutorial_sito_3inf.py`).
2. PDF del tutorial: `classe-3/sito-stage/20261118_Classe-3_Tutorial-Sito-Stage_IT_v1.1.pdf` e `..._IT-BN_v1.1.pdf` (con la riga in bangla).
3. Modello completo e funzionante: `docs/3inf/sito-stage/modello/` (index, passione, competenze, diario, presenze, style.css, img/). Il tutorial fa costruire proprio questi file: i riquadri sono letti da qui.
4. Il sito è una cartella di file sul PC (Blocco note e browser). Niente Git né GitHub per gli allievi (decisione del 17/11).
5. Questa versione sostituisce la v1.0 del 17/11 (cartella `docs/3inf/sito-gite-stage/`, lasciata dov'è perché già data; in cima ha il rimando a questa).

## 02 Struttura uguale per tutti

1. `index.html` (Chi sono), `passione.html` (Hobby), `competenze.html` (Le mie competenze), `diario.html` (Il mio stage: che cosa fa allo stage), `presenze.html` (calendario con nota per ogni giorno), `style.css`, cartella `img/`. Menu a cinque bottoni. Il tutorial dice agli allievi di ricopiare questi file nella cartella `sito-personale`.
2. Calendario presenze: la pagina `docs/stage/presenze-allievo.html`, 23/11/2026-18/02/2027, lunedì-sabato, 76 giorni. La pagina «Copia la pagina Presenze stage» (`docs/stage/copia.html`) fa SCARICARE il file `presenze.html`.

## 03 Dove vanno i dati

1. Livello 1, condiviso: Google Foglio del docente via Apps Script (`docs/stage/presenze-stage-servizio.gs`). Oggi NON ATTIVO (`docs/stage/config.json`, endpoint vuoto).
2. Livello 2, sicurezza: i giorni restano nel browser (localStorage) e il bottone «Scarica i dati (file)» crea `presenze-stage.json`; il bottone «Carica il mio file» li rimette (solo il proprio file, solo in modalità modifica).
3. Per attivare il livello 1: i 5 passi del capitolo 04 di `REGISTRO-STAGE-v2.0.md` (riservato, `report/2026-11-16/`). Non provato sul servizio reale.

## 04 Da confermare o da dirmi

1. **Privacy del servizio:** `doGet` del `.gs` restituisce a chiunque conosca l'indirizzo tutti i giorni e le note di tutti gli allievi («Nome I.»). Non cambiato: lo faccio dopo il tuo via.
2. **Dove sta la cartella** `sito-personale` sul PC: nel tutorial dice «dove salvi i tuoi lavori, il prof ti dice quale». Dimmi il percorso vero.
3. **Come consegnano il sito:** ZIP della cartella nel compito Classroom che crei tu (non pubblicato). Titolo del compito: da dirmi.

## 05 Provato e non provato (Playwright, Chromium, file://)

1. Provato (`generatori/prove_sito_3inf/` nel riservato): modello 41 su 41 (menu a 5 voci, nessun errore JS, presenze su file:// con password e nota, ricarica, file scaricato, ricarica da file su un altro browser, file di un altro allievo rifiutato, in sola lettura niente import); tutorial 16 su 16 (15 passi, copia negli appunti, bangla PC 14, controllo cartella giusta e cartella rotta).
2. NON provato: servizio Apps Script reale, `copia.html` con il download su un PC aula, Blocco note e «Salva con nome» sui PC dell'aula (le immagini di quei passi sono schemi disegnati), telefono vero, Classroom.

## 06 Changelog

1. v1.1 (18/11/2026): nuovo percorso `sito-stage`, sito di 5 pagine (Chi sono, Hobby, Competenze, Il mio stage, Presenze); tutorial da 17 a 15 passi; correzione dell'errore di interpretazione di una parola dettata.
2. v1.0 (17/11/2026): prima versione (cartella `sito-gite-stage`).
