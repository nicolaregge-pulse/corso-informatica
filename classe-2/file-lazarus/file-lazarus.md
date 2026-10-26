# 00 I file di un progetto Lazarus

**Versione 1.0** — 26/10/2026 — Classe 2INF

## 01 Che cosa crea Lazarus

1. Quando salvi un progetto, Lazarus mette nella cartella tanti file, non uno solo.
2. Alcuni sono la RICETTA: li hai fatti tu (il codice, la finestra). Altri sono la TORTA già cotta: Lazarus li crea da solo quando premi Esegui.
3. Su GitHub mettiamo solo la ricetta. Con la ricetta chiunque rifà la torta: apre il progetto e preme Esegui.

## 02 File di testo e file binari

1. Un file di TESTO si apre con Blocco note e dentro leggi parole e codice.
2. Un file BINARIO aperto con Blocco note mostra solo simboli strani: lo capisce solo il computer.
3. Prova: clic destro sul file, poi «Apri con», poi «Blocco note». Se leggi parole è testo, se vedi simboli è binario. Chiudi senza salvare.

## 03 Tutti i file, uno per uno

| Estensione | Nome | A che cosa serve | Testo o binario | Su GitHub |
|---|---|---|---|---|
| .lpi | Lazarus Project Information | La scheda del progetto: le sue impostazioni. Con un doppio clic si apre il progetto in Lazarus. | testo | SÌ |
| .lpr | Lazarus Program | Il programma principale: il punto da cui parte tutto. | testo | SÌ |
| .pas | Pascal (unit) | Il codice che scrivi tu, per esempio unit1.pas. | testo | SÌ |
| .lfm | Lazarus Form | Com'è fatta la finestra: bottoni, caselle, posizioni, Caption. | testo | SÌ |
| .ico | Icona | L'icona del programma. Lazarus non la rifà da solo. | binario | SÌ |
| .lps | Lazarus Project Session | Quali file avevi aperto e dove era il cursore. È solo tua. | testo | NO |
| .res | Risorse | L'icona e altre informazioni già «impacchettate». Lazarus la rifà. | binario | NO |
| .o  .ppu | Pezzi compilati | Pezzi di programma già tradotti per il computer. Lazarus li rifà. | binario | NO |
| .compiled | Nota di compilazione | Un appunto di Lazarus su come ha compilato. | testo | NO |
| .exe | Programma pronto | Il programma finito. Lazarus lo rifà quando premi Esegui. | binario | NO |
| backup/ | Cartella | Copie vecchie dei tuoi file, fatte da Lazarus. | — | NO |
| lib/ | Cartella | I pezzi compilati (.o, .ppu, .res, .compiled). | — | NO |

## 04 La regola facile

1. Su GitHub vanno solo 4 tipi di file: .lpi, .lpr, .pas, .lfm (e l'icona .ico, se l'hai scelta). Tutto il resto Lazarus lo rifà da solo.
2. Perché niente .exe? GitHub serve per conservare la ricetta. Il .exe è la torta: pesa, cambia ogni volta che premi Esegui e non si può leggere. Chi vuole il programma apre il progetto e preme Esegui.

## 05 Come deve essere il tuo repository

```
lazarus/
├── README.md
├── primo-programma/
│   ├── project1.lpi
│   ├── project1.lpr
│   ├── unit1.pas
│   └── unit1.lfm
└── salvadanaio/
    ├── salvadanaio.lpi
    ├── salvadanaio.lpr
    ├── unit1.pas
    └── unit1.lfm
```

## 06 Sai spiegarlo?

Rispondi a voce, con parole tue:

1. In quale file c'è il codice che hai scritto tu?
2. In quale file c'è com'è fatta la tua finestra?
3. Come capisci se un file è di testo o binario?
4. Perché su GitHub non mettiamo il file .exe?

## Changelog

1. v1.0 (26/10/2026): prima versione, dalla lezione «Il mio GitHub in ordine».
