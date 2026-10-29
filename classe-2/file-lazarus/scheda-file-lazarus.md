# 00 I file di un progetto Lazarus

**Versione 1.0** — 29/10/2026 — Classe 2INF — Scheda

## 01 Ogni file, che cosa è

| Estensione | Che cos'è | Va su GitHub? |
|---|---|---|
| .lpi | Il progetto. Con un doppio clic lo apri in Lazarus. | SÌ |
| .lpr | Il programma principale. Da qui parte tutto. | SÌ |
| .pas | Il codice di una finestra. Qui scrivi tu. | SÌ |
| .lfm | Il disegno della finestra: bottoni, caselle, scritte. | SÌ |
| .ico | L'icona del programma. Lazarus non la rifà da solo. | SÌ, se l'hai scelta |
| .res | Le risorse: l'icona già «impacchettata». Lazarus la rifà. | NO |
| .lps | Le tue impostazioni personali: quali file avevi aperto. Serve solo a te. | NO |
| .exe | Il programma pronto. Si rifà con F9 (Esegui). | NO |
| cartella lib | Pezzi già tradotti per il computer. Si rifà con F9. | NO |
| cartella backup | Copie vecchie dei tuoi file, fatte da Lazarus. | NO |

## 02 La regola d'oro

> [GIALLO] Su GitHub vanno i file che servono per RIFARE il programma. Quello che Lazarus rifà da solo resta sul PC. Ricorda i 4 file: .lpi, .lpr, .pas, .lfm (più l'icona .ico, se l'hai scelta).

## 03 Attenzione: Windows nasconde le estensioni

1. Windows spesso nasconde la fine del nome: l'estensione (.pas, .lfm, ...).
2. Così vedi due file con lo stesso nome, per esempio «unit1» e «unit1». Non sono uguali!
3. Guarda l'icona: il file .lpi ha l'icona di Lazarus. Il file .exe ha l'icona del programma.
4. Guarda la colonna «Tipo». Se non la vedi: in Esplora file clic su «Visualizza», poi su «Dettagli».
5. Nella colonna «Tipo» c'è il tipo del file, spesso con la sigla: per esempio «File LFM».
6. Su GitHub il nome si vede sempre intero, con l'estensione: lì controlli che sia giusto.

## 04 Una cartella per ogni progetto

1. Ogni progetto ha la SUA cartella. Mai due progetti nella stessa cartella.
2. Oggi rifacciamo la calcolatrice da zero: la cartella si chiama «calcolatrice».
3. Quando salvi il progetto in Lazarus, scegli proprio quella cartella.

```
calcolatrice/
├── calcolatrice.lpi     SÌ
├── calcolatrice.lpr     SÌ
├── unit1.pas            SÌ
├── unit1.lfm            SÌ
├── calcolatrice.ico     SÌ, se l'hai scelta
├── calcolatrice.res     NO
├── calcolatrice.lps     NO
├── calcolatrice.exe     NO
├── lib/                 NO
└── backup/              NO
```

## 05 Spiegalo in 30 secondi

Dillo al compagno, con queste 3 frasi:

1. Su GitHub metto solo i file per rifare il programma: .lpi, .lpr, .pas e .lfm.
2. Nel .pas c'è il codice che scrivo io, nel .lfm c'è il disegno della finestra.
3. Il .exe, la cartella lib e la cartella backup no: Lazarus li rifà quando premo F9.

## Changelog

1. v1.0 (29/10/2026): prima versione, scheda da proiettare per la lezione della calcolatrice da zero.
