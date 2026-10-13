# Ripasso, verifica e recupero: come si rifà

**Versione 1.0** — 13/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano. Area Docente.

Questo documento rende ripetibile il percorso provato con la 2INF il 13/10/2026 (chiusura del Treno e del versioning). Vale per tutte le classi. Nasce dalla retrospettiva di quel giorno e dagli errori #60, #61 e #62 del registro.

## 00 Le pagine

| Pagina | Indirizzo | Chi la vede |
|---|---|---|
| Percorso dei ragazzi | `docs/verifica/?b=<banca>` | tutti |
| Risultati della classe | `docs/verifica/risultati.html?b=<banca>` | tutti |
| Monitor della lezione | `docs/<classe>-monitor/` | tutti |
| Cruscotto del prof | `docs/<classe>-cruscotto/` | solo il prof (password dell'area docente) |
| Anteprima con le risposte giuste | `docs/verifica/?b=<banca>&anteprima=<codice>` | solo il prof (codice nel riservato) |

## 01 Prima della lezione (lo fa Claude)

1. Scrive la banca delle domande in `docs/verifica/banche/<banca>.js`: schede, allenamento, crocette con il tema, dati, scale, domande scritte, retrospettiva, recupero, `schede_temi` (tema sbagliato → scheda da ripassare), `strumenti` (bottone del monitor).
2. Mette lo stato chiuso in `docs/verifica/stato/<banca>.json`.
3. **Prova come un ragazzo, fino in fondo**, con lo script di prova:
   1. ripasso, verifica, ricarica a metà, scheda chiusa e riaperta, consegna con un clic, risultato dopo la ricarica, recupero con la teoria mirata;
   2. si apre la verifica solo se la prova finisce con «Tutto a posto».
```
NODE_PATH=$(npm root -g) node strumenti/prova_verifica.js <banca>
```
4. Prepara il monitor della classe vuoto e il cruscotto (`generatori/cruscotto.py` nel riservato).
5. Dà al docente il link dell'anteprima e chiede: «Pubblico o vuoi vederlo prima?».

## 02 In classe

1. **Ripasso.** I ragazzi aprono il percorso dal compito o dall'annuncio di Classroom. La prima domanda è facile, per vincere subito.
2. **Il docente manda le schermate di Veyon in chat.** Claude le trascrive nel monitor (solo fatti, fuori compito in rosso) e aggiorna il cruscotto.
3. **Quando si apre la verifica:** quando più della metà è in fondo al ripasso e la classe comincia a parlare. Il docente scrive «attiva». Claude apre la verifica con l'ora di consegna (tempo dato meno 5 minuti per mandare).
4. **Durante la verifica la pagina parla da sola:** salva ogni 2 secondi, negli ultimi 5 minuti mostra il promemoria della consegna, sotto ogni domanda c'è «Ho un problema con questa domanda». Il docente non deve spiegare passi a voce.
5. **Consegna con un clic.** Il ragazzo clicca «Consegna»: il risultato va da solo al docente e si apre una scheda con scritto «Consegna arrivata al prof». Se la scheda non si apre, nella pagina c'è un solo bottone: «Manda al prof».

## 03 Correzione e voti

1. Claude legge le consegne con `generatori/correggi_verifica.py` (riservato): crocette per area, risposte scritte, tempi, antiplagio.
2. Il docente dà una **fascia** per i casi da decidere (per esempio 55-65). Claude propone il voto come giudizio complessivo, con i pesi della banca.
3. Gli assenti nei giorni del progetto: la parte personale non si valuta.
4. Le misure compensative stanno solo nel riservato (`config/misure-compensative-<classe>.md`).
5. Claude chiede «Pubblico i voti o vuoi vederli prima?» e solo dopo il sì scrive `docs/verifica/risultati/<banca>.json`.

## 04 Recupero personale

1. Si apre ragazzo per ragazzo, dopo il voto: `recupero` aperto e il nome in `recupero_per`.
2. Il recupero ha due passi: prima la teoria mirata (i propri errori con la risposta giusta e le schede che servono), poi la riverifica (crocette sui temi sbagliati e le risposte scritte lasciate vuote).

## 05 Retrospettiva e storia

1. Le quattro domande (di più, di meno, cominciare, smettere) sono alla fine della verifica.
2. Claude ne fa il riassunto senza nomi in `RETROSPETTIVE.md`, insieme alla revisione e alla retrospettiva fra docente e Claude (`AGILE-CERIMONIE.md`).
3. La giornata entra nella demo, senza nomi (`strumenti/gen_demo_13.py` come modello).
4. I tempi per domanda del cruscotto servono per tarare la verifica successiva.

## 06 Da fare una volta sola: la consegna con un clic

Si fa il lunedì o il mercoledì pomeriggio, a scuola senza classe. Finché non è fatto, la pagina usa la riserva del Modulo «Consegna».

1. Apri la finestra PIAMARTA e premi Ctrl+T per una scheda nuova.
2. Incolla nella barra in alto questo indirizzo e premi Invio:
```
https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/strumenti/automazione-corso.gs
```
3. Premi Ctrl+A e poi Ctrl+C per copiare tutto il codice.
4. Apri una scheda nuova con Ctrl+T, incolla questo indirizzo e premi Invio:
```
https://script.google.com/home
```
5. Clicca il progetto «Consegne Classroom → Git».
6. Nel pannello «File» a sinistra clicca «automazione-corso.gs».
7. Clicca dentro il codice, premi Ctrl+A e poi Ctrl+V.
8. Premi Ctrl+S per salvare.
9. In alto a destra clicca il bottone blu «Distribuisci», poi «Nuova distribuzione».
10. Accanto a «Seleziona tipo» clicca l'ingranaggio e scegli «Applicazione web».
11. In «Esegui come» scegli «Me»; in «Chi ha accesso» scegli la voce con il nome della scuola.
12. Clicca «Distribuisci» e poi «Autorizza accesso» con l'account PIAMARTA.
13. Copia l'indirizzo che finisce con «/exec» e incollalo in chat: Claude lo mette in `docs/verifica/config.json` e rifà la prova del capitolo 01.

## 07 Registro delle versioni

1. **v1.0 (13/10/2026):** prima versione, dopo la verifica della 2INF: consegna con un clic, prova come un ragazzo, cruscotto per ogni classe con i tempi per domanda, recupero con teoria mirata.
