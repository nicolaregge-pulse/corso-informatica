# 00 Guida ai messaggi per il docente

**Versione 1.0** — 04/11/2026 — documento interno del docente e di Claude (nessun nome di allievi)

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
- **Formato a TABELLA (07/10/2026, Nicola):** i passi si danno in una tabella con le colonne N. · Account · Finestra/scheda · Dove · Cosa fare (una riga = una azione).

## 03 Registro delle versioni

1. v1.0 (04/11/2026): prima versione, con il testo spostato da `CLAUDE.md` (regole 8, 9, 20, 25, guida passo passo, regola copia).
