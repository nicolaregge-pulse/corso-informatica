# Sito 3INF: Gite e Presenze stage — nota per il docente

**Versione 1.0** — 17/11/2026 · documento interno (non per i ragazzi)

## 01 Che cosa c'è

1. Tutorial guidato (17 passi a bottoni «Ho fatto», bangla solo con `?pc=14`): `docs/3inf/sito-gite-stage/index.html` (generato da `strumenti/genera_tutorial_sito_3inf.py`).
2. PDF del tutorial: `classe-3/sito-gite-stage/20261117_Classe-3_Tutorial-Sito-Gite-Stage_IT_v1.0.pdf` e `..._IT-BN_v1.0.pdf` (con la riga in bangla).
3. Modello completo e funzionante: `docs/3inf/sito-gite-stage/modello/` (index, passione, competenze, diario, presenze, gite, style.css, dati-gite.js, img/). Il tutorial fa costruire proprio questi file: i riquadri sono letti da qui.
4. Il sito è una cartella di file sul PC (Blocco note e browser). Niente Git né GitHub (decisione del 17/11).

## 02 Struttura uguale per tutti

1. `index.html` (Chi sono), `passione.html` (Hobby), `competenze.html`, `diario.html` (Il mio stage: descrizione), `presenze.html` (calendario con nota per ogni giorno), `gite.html`, `style.css`, `dati-gite.js`, cartella `img/`. Stessi nomi già usati dalla classe il 16/11. Il tutorial dice agli allievi di ricopiare questi file nella cartella `sito-personale`.
2. Calendario presenze: la pagina che già c'era (`docs/stage/presenze-allievo.html`, 23/11/2026-18/02/2027, lunedì-sabato, 76 giorni). La pagina «Copia la pagina Presenze stage» (`docs/stage/copia.html`) ora fa SCARICARE il file `presenze.html` (prima parlava di GitHub).
3. Gite: nei documenti non c'è nessuna gita (cercato in entrambi i repository). `dati-gite.js` è vuoto e la pagina lo dice. Le gite le scrive il docente in quel file (una riga per gita: titolo, data, meta, ritrovo, ora, rientro, costo, cosa portare, note). Gli allievi lo scaricano dal tutorial.

## 03 Dove vanno i dati (la tua domanda: «database e file?»), scelto io

1. Livello 1, condiviso: Google Foglio del docente via Apps Script (`docs/stage/presenze-stage-servizio.gs`, già pronto, una riga per allievo e per giorno con stato, ore e nota). Oggi NON ATTIVO (`docs/stage/config.json`, endpoint vuoto).
2. Livello 2, sicurezza: i giorni restano nel browser (localStorage) e il bottone «Scarica i dati (file)» crea `presenze-stage.json`. Nuovo in v2.2 della pagina: bottone «Carica il mio file» che li rimette (solo il proprio file, solo in modalità modifica).
3. Per attivare il livello 1: i 5 passi del capitolo 04 di `REGISTRO-STAGE-v2.0.md` (riservato, `report/2026-11-16/`): account PIAMARTA, script.google.com, incolla il `.gs`, esegui `prepara`, Implementa come app web («Chiunque»), poi dammi l'indirizzo `/exec` e lo metto in `docs/stage/config.json`. Nessuna pagina dei ragazzi si rifà. Non provato sul servizio reale.

## 04 Da confermare o da dirmi

1. **Privacy del servizio:** `doGet` del `.gs` restituisce a chiunque conosca l'indirizzo tutti i giorni e le note di tutti gli allievi (nome «Nome I.»). Per la nota «che cosa ho fatto» non l'ho cambiato (era già così dal 16/11, serve ai tutor). Se vuoi che gli allievi non si vedano tra loro, `doGet` deve rispondere solo con la chiave: lo faccio dopo il tuo via.
2. **Dove sta la cartella** `sito-personale` sul PC: nel tutorial dice «dove salvi i tuoi lavori, il prof ti dice quale». Dimmi il percorso vero (Documenti? un'unità?).
3. **Come consegnano il sito:** ZIP della cartella nel compito Classroom che crei tu (non l'ho pubblicato). Titolo del compito: da dirmi.
4. **Date e gite:** lo stage è 23/11/2026-18/02/2027 (dai tuoi documenti). Le gite non ci sono: dimmi titolo, data, meta, ritrovo, ora, costo e cosa portare.

## 05 Provato e non provato (Playwright, Chromium, file://)

1. Provato (`generatori/prove_sito_3inf/` nel riservato): modello 57 su 57 (menu, nessun errore JS, gite vuote e con dati di prova, presenze su file:// con password e nota, ricarica, file scaricato, ricarica da file su un altro browser, file di un altro allievo rifiutato, in sola lettura niente import); tutorial 16 su 16 (percorso, copia negli appunti, bangla PC 14, controllo cartella giusta e cartella rotta). Test esistente della pagina presenze: 23 su 23 fino al passo che chiede la password del docente (non salvata).
2. NON provato: servizio Apps Script reale, `copia.html` con il download su un PC aula, Blocco note e «Salva con nome» sui PC dell'aula (le immagini di quei passi sono schemi disegnati, non screenshot veri), telefono vero, Classroom.

## 06 Changelog

1. v1.0 (17/11/2026): prima versione.
