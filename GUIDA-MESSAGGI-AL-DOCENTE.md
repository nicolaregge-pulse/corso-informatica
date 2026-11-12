# 00 Guida ai messaggi per il docente

**Versione 1.5** — 12/11/2026 (prima: 1.4, 1.3, 1.2, 1.1 del 06/11/2026) — documento interno del docente e di Claude (nessun nome di allievi)

Dettaglio della regola R4 di `CLAUDE.md` (messaggi al docente). La regola breve sta lì; qui c'è il testo completo da cui nasce.

<div class="box giallo" markdown="1">
**Testo spostato da `CLAUDE.md` il 04/11/2026, senza cambiarlo** (archivio completo: `archivio/CLAUDE-fino-al-2026-11-04.md`). Dove questo testo dice una cosa diversa dalle regole R1-R11 del nuovo `CLAUDE.md` (per esempio prefissi, pubblicazione, tabelle di passi, carta e penna), valgono le regole R1-R11.
</div>

## 01 La regola R4 in breve

1. Prima riga: la cosa bloccante, da sola (firma, uscita, «PUBB n NON riuscito», PC rotto).
2. Poche righe: in ora di lezione il blocco, il link o il riquadro, il prossimo passo. Il resto va in un file.
3. Ogni passo è una frase che comincia con il verbo e dice il «dove» a parole: niente tabelle di passi e niente catene di coordinate (questo supera il «formato a tabella» del 07/10/2026 riportato sotto).
4. Ogni testo da scrivere sta in un riquadro da copiare subito dopo il passo; prima si apre la pagina dove si incolla, poi si copia, poi si incolla.
5. Niente log, JSON o output lunghi in chat; i file si mandano scaricabili.

## 02 Testo completo spostato da CLAUDE.md

**9. Testo da scrivere = riquadro da copiare, SEMPRE nello stesso messaggio (12/10/2026, VINCOLANTE, «te l'ho già detto 100 volte»).**
Ogni volta che un passo (anche quello successivo annunciato) richiede a Nicola di scrivere un testo, una frase, un titolo o
un valore, il testo pronto va già nel messaggio, in un blocco di codice da copiare. Nicola non scrive mai a mano. Vedi REGISTRO-ERRORI #46.
Ordine di lettura: Nicola legge dall'alto in basso. Il riquadro da copiare sta SUBITO dopo il passo che lo usa (passo → riquadro →
passo successivo), mai raccolto in fondo e mai indicato con «qui sotto» se non è proprio la riga seguente.
Formato ATOMICO (12/10/2026, corretto da Nicola): ogni passo è un blocco completo (dove + cosa + il suo riquadro da copiare subito
dopo); in un messaggio si danno PIÙ passi atomici, uno sotto l'altro. Se Nicola si perde, lo dice lui. Non chiedere uno screenshot a ogni passo:
solo quando serve davvero per controllare il risultato finale (12/10/2026).
Memoria del copia e incolla = VUOTA (12/10/2026, REGISTRO-ERRORI #50): ogni «incolla» viene subito dopo il passo che dice cosa
copiare e da dove; prima si apre la pagina dove si incolla, poi si copia, poi si incolla, così una copia non cancella l'altra.

**8. I file per Nicola si mandano SCARICABILI in chat (12/10/2026, VINCOLANTE).** PDF, immagini e documenti da dargli
si consegnano con l'invio di file della chat (card con il bottone di download), non come link a GitHub da aprire.
Il link al repository si aggiunge solo se serve per altro (pubblicazione, condivisione).

**25. Niente output lungo nella chat (28/10/2026, Nicola).** Non stampare mai su terminale/chat blocchi di testo lunghi, log completi o payload JSON. Quando esegui comandi o chiamate, reindirizza sempre l output su file temporanei o usa parametri silenziosi. Mostra all utente solo brevi sintesi discorsive in italiano.

**20. Messaggi tra chat (19/10/2026, Nicola).** Un messaggio che passa da una chat Claude a un'altra comincia con «Da chat <nome> a chat <nome>:». Quando ne scrivo uno per un'altra chat lo intesto così; quando ne arriva uno senza intestazione e Nicola dice da dove viene, lo tratto come richiesta di Nicola.

### Guida passo-passo — coordinate SEMPRE complete (regola VINCOLANTE)

> **Nota 06/11/2026:** dove questo testo dice «più passi in un messaggio» (formato atomico, sopra) vale R4.3: si dà SOLO il prossimo passo. Dove dice «account → finestra → app → dove → cosa» come catena, vale la frase con il verbo davanti e il «dove» in parole, preceduta da account e finestra (R4.3; riga «SOLO IL PROSSIMO PASSO» e «Frasi semplici» sotto).

Quando chiedo a Nicola di fare **qualsiasi** azione (un comando, un clic, un
valore da inserire), devo **SEMPRE** premettere le coordinate complete, così sa
esattamente dove agire. Prima dell'azione indico, in quest'ordine:

0. **Quale ACCOUNT** (07/10/2026, VINCOLANTE) — si chiamano così: **account PERSONALE** = nicolaregge@gmail.com
   (finestra Chrome con le schede gialle e la foto in alto a destra, dove c'è GitHub) e **account PIAMARTA** =
   nicola.regge@piamarta.it (finestra Chrome con le schede arancioni e il bottone «Scuola», dove ci sono DIDAweb,
   Classroom e lo script).
   Ordine fisso di ogni riga: **account → finestra → app → dove → cosa**, con le **caselle da copiare**
   sempre nello stesso messaggio.
1. **Quale APPLICAZIONE** — es. `[APP — GitHub Desktop]`, `[APP — Godot]`,
   `[APP — Esplora file]`, `[BROWSER]`.
2. **Quale FINESTRA / SCHEDA** — se ce ne sono più aperte, dirlo esplicitamente
   (es. `[BROWSER — scheda "corso-godot"]`).
3. **Quale MENU → voce → sotto-voce**.
4. **In quale AREA della finestra/applicazione** — pannello a sinistra, barra in
   alto a destra, riquadro in basso, ecc.
5. **L'AZIONE esatta**, **una alla volta**.

**Mai** dare un comando "nudo" senza dire **dove** va messo. Un passo alla volta;
se è terreno nuovo per lui, massima precisione.

**REGOLA COPIA (VINCOLANTE, chiesta da Nicola — non violarla mai):** qualunque
cosa Nicola debba **copiare** (un nome file, un valore, un comando, un pezzo di
testo) va **SEMPRE** in un **blocco di codice recintato** — cioè su una riga a
parte, tra ` ``` ` e ` ``` ` — così compare il **bottone "copia"** e lui NON deve
selezionare col mouse. Regole precise:
- **NON basta** il codice "in linea" con un solo apice (`` `così` ``): NON ha il
  bottone copia → vietato per le cose da copiare.
- **NON** metterlo come testo normale nella frase, né nel blockquote `>`.
- **Un valore per blocco:** un solo riquadro = una sola cosa da copiare, così un
  clic copia esattamente quella e nient'altro.
- Vale anche per **nomi di file**: es. il nome da dare a uno screenshot va nel suo
  riquadro, da solo.
- Il testo dentro il riquadro dev'essere **esattamente** ciò che serve, pronto da
  incollare (nessuna barra `/` nei nomi file di Windows, ecc.).

**Rinforzo (chiesto da Nicola, vale SEMPRE — è più importante di andare veloci):**
- **Una sola azione per riga numerata.** Mai due clic nella stessa riga.
- **Ogni riga dice DOVE prima di dire COSA:** applicazione → scheda/finestra →
  area della pagina (es. "in alto a destra", "nel menu a sinistra") → il nome
  **esatto** del bottone/voce (tra apici) → l'azione.
- **Se Nicola manda uno screenshot, indico il punto ESATTO** su *quella*
  schermata (dove si trova, com'è scritto), non un'istruzione generica.
- **Non dare mai per scontato** che sappia dov'è un bottone o cosa fa un termine.
  Nel dubbio, essere più precisi, non meno.
- Meglio **lento e chiaro** che veloce e confuso: la fretta qui è un errore.
- **SOLO IL PROSSIMO PASSO (07/10/2026, Nicola):** non ripetere mai i passi che ha già fatto; dire il prossimo passo e basta, aspettare che lo faccia, poi il successivo.
- **Frasi semplici, non catene di coordinate (12/10/2026, REGISTRO-ERRORI #56):** ogni passo è una frase che comincia con il verbo («Clicca…», «Premi…», «Torna…»), con il «dove» detto a parole dentro la frase; MAI catene «Account · finestra · dove: cosa». Dove si può, i tasti (Ctrl+T, Ctrl+V, Invio) invece di cercare bottoni. Il bottone copia: «il piccolo bottone a destra del riquadro grigio».
- **Flusso unico sempre da zero (12/10/2026, REGISTRO-ERRORI #55):** niente «se», niente «salta», niente domande dentro i passi.
- **Niente parole in più (12/10/2026, REGISTRO-ERRORI #53):** niente avverbi o aggettivi che non servono («onestamente», «valide»…): se togliendo la parola il senso resta uguale, si toglie.
- **SUPERATO (R4.3, 04/11/2026) — Formato a TABELLA (07/10/2026, Nicola):** i passi si danno in una tabella con le colonne N. · Account · Finestra/scheda · Dove · Cosa fare (una riga = una azione).

## 03 Formato dei messaggi in classe (decisione del docente, 11/11/2026)

Il docente ha detto «PERFETTO» a questo formato. Dettaglio di R4 (R4.2, 3bis, 3ter).

1. Tutte le informazioni per il docente stanno in UN riquadro ROSSO, fatto con righe di quadratini rossi (🟥) sopra e sotto.
2. Dispense e PDF stanno in un riquadro BLU (righe di 🟦); il file vero viene mandato con SendUserFile subito prima del riquadro.
3. Il pacchetto per Classroom è UN SOLO riquadro rosso con: il titolo (in un riquadro di codice), l'oggetto (il testo del post)
   e una fascia blu con «FILE DA ALLEGARE: nome.pdf». La scheda del PDF si manda nel mezzo del riquadro: testo, SendUserFile,
   testo di chiusura.
4. Nel riquadro compaiono il nome del file e la riga «Non provato:» (R7.5).
5. Niente codice o spiegazioni lunghe in chat mentre il docente è in classe (dettaglio in R4: file .txt con SendUserFile).
6. In classe il docente deve capire a colpo d'occhio: la prima riga è la cosa bloccante.

## 03bis I colori delle cornici (decisione del docente, 11/11/2026)

1. **Verde** (🟩): i comunicati per il docente, messi in cornice (stato, domande, passi da fare).
2. **Rosso** (🟥): solo le pubblicazioni su Classroom (titolo, oggetto, testo da incollare, registro).
3. **Blu** (🟦): solo i documenti (PDF e altri file mandati con SendUserFile: il file va subito sotto la riga della cornice).
4. La prima riga di ogni messaggio resta la cosa bloccante, da sola; la cornice viene dopo.

## 03ter Il PDF si manda SEMPRE come scheda da scaricare (decisione del docente, 12/11/2026)

1. Ogni volta che nel messaggio c'è un PDF o un altro file per il docente, la **scheda del file va mandata con SendUserFile in quel messaggio**, anche se il file era già stato mandato prima. Scrivere solo il nome del file in un riquadro blu NON basta: il docente non lo trova («mettilo nelle note, MAI PIÙ»).
2. Questo vale più della vecchia regola «non rimandare lo stesso file» (errore #273): un doppione «(1)» costa meno di un file che non si trova. Se il file non è cambiato si rimanda con lo stesso nome.
3. **Schema esatto del pacchetto Classroom (approvato dal docente il 11/11, riconfermato il 12/11):** un solo messaggio. Prima riga: la cosa bloccante. Poi riga di quadratini rossi; titolo, oggetto e registro, ciascuno in un riquadro di codice; riga di quadratini **blu** e «📄 FILE DA ALLEGARE: la dispensa è qui sotto ⬇️»; **la scheda del PDF mandata con SendUserFile**; riga di quadratini **blu** (il blu sta SOLO intorno al file); poi nel rosso il quiz o altre note brevi; riga di quadratini rossi; riga «Non provato:». Il blu non si usa per testo, solo per incorniciare il file.
4. Se il docente ha un PDF solo per sé (dispensa frontale), la sua scheda sta in un riquadro blu a parte, con il file mandato subito prima.

## 03quater L'ORDINE di ogni ora (decisione del docente, 11/11 e 12/11/2026)

1. **Dispensa docente (frontale):** si manda PER PRIMA, all'inizio dell'ora, con la scheda del PDF dentro una cornice blu. Il docente spiega alla lavagna.
2. **Foto della lavagna:** le manda il docente. Fino a quel momento NON si danno titolo e oggetto.
3. **Pacchetto per Classroom:** dopo le foto, un solo riquadro rosso (titolo, oggetto, registro) con la dispensa dei ragazzi dentro la cornice blu (sezione 03ter).
4. **Quiz su Moduli:** verso la fine dell'ora, quando lo dice il docente, con domande aperte sul proprio PC e alcune a scelta (FRAMEWORK-QUIZ.md, capitolo «Quiz anti-AI»). Mai nel post iniziale.

## 04 Registro delle versioni

3. v1.2 (11/11/2026): nuova sezione 03, formato dei messaggi in classe (riquadro rosso, riquadro blu, pacchetto Classroom), decisione del docente.
2. v1.1 (06/11/2026): note di allineamento a R4.3 (solo il prossimo passo, niente catene né tabelle).
1. v1.0 (04/11/2026): prima versione, con il testo spostato da `CLAUDE.md` (regole 8, 9, 20, 25, guida passo passo, regola copia).
4. v1.3 (11/11/2026): nuova sezione 03bis, colori delle cornici: verde per i comunicati, rosso per Classroom, blu per i documenti, decisione del docente.
5. v1.4 (12/11/2026): nuova sezione 03ter, il PDF si manda sempre come scheda da scaricare nello stesso messaggio, anche se già mandato; errore #285.
6. v1.5 (12/11/2026): nuova sezione 03quater, ordine fisso di ogni ora: dispensa docente, foto, pacchetto Classroom, quiz a fine ora; errore #286.
7. v1.6 (12/11/2026): formato del pacchetto Classroom corretto dal docente: nel riquadro rosso solo TITOLO e OGGETTO, e dentro il rosso il riquadro blu con la dispensa dei ragazzi; registro, quiz e «Non provato» fuori dal rosso; la scheda PDF si manda con SendUserFile PRIMA del testo finale (il docente vede solo il testo dopo l'ultima chiamata di strumento); errore #287.
