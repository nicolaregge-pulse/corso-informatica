# 00 Come si aggiorna l'Allegato A senza pasticci

**Versione 1.2** — 14/10/2026 — Area Docente. Il modo per modificare l'Allegato A in due (o in tanti) senza cancellare il lavoro degli altri.

## 01 L'idea

1. Il file Word vero è uno solo: quello della scuola, che toccano anche gli altri docenti.
2. La parte di Regge non si scrive a mano nel Word: vive nel programma `PROGRAMMI-DI-MASSIMA-2026-27.md`.
3. Ogni volta si parte dal file più recente della scuola, Claude ci rimette dentro la parte di Regge e il file torna subito a scuola.
4. Così non esistono due copie che vanno avanti per conto loro.
5. I colori: **rosa** = la parte di Regge prevista per il 2026/27; **verde** = la parte di Regge degli anni scorsi, già consegnata; **giallo o bianco** = gli altri docenti.

## 02 I passi di Nicola

1. Scarica dalla scuola il file più recente e guarda l'ora dell'ultima modifica del file a scuola.
2. Lo manda a Claude in chat.
3. Claude glielo ridà in un paio di minuti, con la parte di Regge aggiornata.
4. Prima di ricaricarlo, guarda di nuovo l'ora dell'ultima modifica a scuola.
   1. Se è la stessa del passo 1, nessuno l'ha toccato nel frattempo: lo ricarica.
   2. Se è cambiata, qualcuno ci ha lavorato: non lo ricarica, scarica di nuovo il file e ricomincia dal passo 2.
5. Dopo averlo ricaricato, lo scarica ancora una volta dalla scuola e lo manda a Claude: Claude risponde «TUTTO A POSTO» oppure dice che cosa non va.
6. Le modifiche alla parte di Regge si dicono a Claude in chat: Claude cambia il programma e rifà il file.

> **Attenzione:** lo script garantisce che il file ridato contiene tutto quello che c'era nel file mandato. Non può vedere che cosa succede a scuola tra il passo 1 e il passo 4: per questo servono il controllo dell'ora (passo 4) e il controllo finale (passo 5).

## 03 Che cosa controlla lo script da solo

1. Riconosce la classe dalla tabella delle annualità.
2. Nella riga di quest'anno toglie il vecchio blocco «Regge» e ci rimette quello aggiornato, in rosa; nelle righe degli anni scorsi colora di verde la parte di Regge (da «Regge» fino all'etichetta di un altro docente: Meles, Panaccione, Erba) e toglie il verde dalle etichette degli altri. Si può rilanciare quante volte si vuole: il risultato è sempre lo stesso.
3. Se qualcuno ha cambiato a mano il blocco rosa nel Word, si ferma e mostra la differenza, senza sovrascrivere niente.
4. Dice che cosa hanno cambiato gli altri docenti dall'ultima volta.
5. Riapre il file salvato e controlla che il testo degli altri sia identico a prima; se non lo è, butta il file.
6. Con `--verifica` controlla il file che sta a scuola dopo il caricamento: la parte di Regge è quella preparata e il testo degli altri è identico.

> **Nota:** script `programmi-ufficiali/_build/aggiorna_allegati.py`; file pronti in `programmi-ufficiali/2026-27/consegna/` con data e ora nel nome; memoria dell'ultima volta in `programmi-ufficiali/2026-27/registro-allegati.json`. Provato il 14/10 con un collega che aggiunge una riga (segnalata) e con una modifica a mano del verde (fermato).

## 04 Registro delle versioni
3. **v1.2 (14/10/2026)**: consolidata: un solo script (`aggiorna_allegati.py` con `allegati_comune.py`), colori rosa/verde/giallo, file v1.0.
2. **v1.1 (14/10/2026)**: controllo dell'ora dell'ultima modifica prima di ricaricare e controllo finale dopo («TUTTO A POSTO»).
1. **v1.0 (14/10/2026)**: prima versione.
