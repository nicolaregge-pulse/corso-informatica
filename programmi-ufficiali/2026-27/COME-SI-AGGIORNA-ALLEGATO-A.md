# 00 Come si aggiorna l'Allegato A senza pasticci

**Versione 1.0** — 14/10/2026 — Area Docente. Il modo per modificare l'Allegato A in due (o in tanti) senza cancellare il lavoro degli altri.

## 01 L'idea

1. Il file Word vero è uno solo: quello della scuola, che toccano anche gli altri docenti.
2. La parte di Regge non si scrive a mano nel Word: vive nel programma `PROGRAMMI-DI-MASSIMA-2026-27.md`.
3. Ogni volta si parte dal file più recente della scuola, Claude ci rimette dentro la parte di Regge in verde e il file torna subito a scuola.
4. Così non esistono due copie che vanno avanti per conto loro.

## 02 I passi di Nicola

1. Scarica dalla scuola il file più recente dell'Allegato A, un attimo prima.
2. Lo manda a Claude in chat.
3. Claude glielo ridà in un paio di minuti, con la parte di Regge aggiornata.
4. Nicola lo ricarica subito a scuola, senza aprirlo per modificarlo.
5. Le modifiche alla parte di Regge si dicono a Claude in chat: Claude cambia il programma e rifà il file.

## 03 Che cosa controlla lo script da solo

1. Riconosce la classe dalla tabella delle annualità.
2. Nella riga di quest'anno toglie il vecchio blocco «Regge» verde e ci rimette quello aggiornato. Si può rilanciare quante volte si vuole: il risultato è sempre lo stesso.
3. Se qualcuno ha cambiato a mano il blocco verde nel Word, si ferma e mostra la differenza, senza sovrascrivere niente.
4. Dice che cosa hanno cambiato gli altri docenti dall'ultima volta.
5. Riapre il file salvato e controlla che il testo degli altri sia identico a prima; se non lo è, butta il file.

> **Nota:** script `programmi-ufficiali/_build/aggiorna_allegati.py`; file pronti in `programmi-ufficiali/2026-27/consegna/` con data e ora nel nome; memoria dell'ultima volta in `programmi-ufficiali/2026-27/registro-allegati.json`. Provato il 14/10 con un collega che aggiunge una riga (segnalata) e con una modifica a mano del verde (fermato).

## 04 Registro delle versioni
1. **v1.0 (14/10/2026)**: prima versione.
