# Il treno blindato — base del prof. Nicola Regge (Godot)

**Versione 1.0** — 12/10/2026 — motore Godot 4.7

## 1 Cos'è

1. È il gioco della classe 2INF «Il treno blindato» (versione HTML 0.31, «Gli uccelli nel cielo») rifatto con il motore **Godot 4.7** ed esportato per il browser.
2. È la **base del prof**: da qui ogni classe parte con un suo ramo e aggiunge i suoi pezzi (cattivi, ambienti, facce, personaggi). Per questo la base è **neutra**: niente facce né personaggi di una classe, solo cattivi disegnati.
3. Perché 1.0: è cambiato il motore, una cosa grossa, quindi è una versione «major».
4. Si gioca nel browser (PC e telefono, in verticale e in orizzontale): `docs/giochi/treno-2inf-godot/` del sito del corso. Le versioni congelate sono in `docs/giochi/treno-2inf-godot/versioni/`.
5. Ponte da Lazarus: Lazarus **reagisce** (aspetta un clic, come `Button1Click`), Godot **pulsa** (`_process(delta)` gira da solo circa 60 volte al secondo e muove il treno, i cattivi, la pioggia).

## 2 Come si apre con Godot portabile

1. Avviare Godot 4.7 portabile (doppio clic sul file `.exe`).
2. Nella finestra «Gestore dei progetti» premere «Importa».
3. Scegliere il file `project.godot` di questa cartella (`treno-2inf-godot`).
4. Premere «Importa e modifica».
5. Premere F5 (oppure il triangolo «Esegui» in alto a destra): il gioco parte in una finestra.

## 3 I file del progetto

| File | Cosa contiene |
|---|---|
| `treno.gd` | il MOTORE: legge i dati, fa avanzare il treno, i cattivi, i colpi, il vetro, e disegna tutto (commenti in italiano) |
| `schermate.gd` | le SCHERMATE: inizio, fine partita, «Chi l'ha fatto», «I personaggi», «Facce della classe», bottone Pausa, scritta della versione |
| `suoni.gd` | i SUONI, costruiti con la matematica (nessun file audio), come nella versione HTML |
| `memoria.gd` | la MEMORIA: record, migliori punteggi, soprannome, facce scelte sul dispositivo |
| `strato.gd` | un «foglio» su cui il motore dipinge (paesaggio, cabina, scritte in alto) |
| `main.tscn` | la scena: un solo nodo con lo script `treno.gd` |
| `icon.png` | l'icona del gioco (binari e mirino) |
| `export_presets.cfg` | le impostazioni per esportare il gioco per il Web |
| `strumenti/congela_versione.py` | strumento del prof: copia la versione esportata in `versioni/vX.Y/` |

## 4 I dati (si cambia il gioco senza toccare il codice)

Tutti i dati stanno nella cartella `dati/`, con gli stessi nomi della versione HTML: un file della versione HTML si può copiare qui così com'è.

| File | Squadra | Cosa contiene |
|---|---|---|
| `dati/regole.json` | PERCORSO e REGOLE | colpi del vetro, velocità del treno, secondi prima che un cattivo spari, cattivi per livello, punti |
| `dati/percorso.json` | PERCORSO e REGOLE | l'ordine degli ambienti e quanti secondi dura ognuno |
| `dati/ambienti/*.json` | AMBIENTI | colori del cielo e della terra, oggetti (alberi, case, palazzi, rocce, onde), quanti, rottami |
| `dati/cattivi/pc01.json` ... `pc40.json` | CATTIVI | un cattivo per ogni PC (modello: `pc00-ESEMPIO.json`, che non entra nel gioco) |
| `dati/facce.json` + `dati/facce/` | PERSONAGGI | le facce della classe che compaiono sui cattivi (lista vuota nella base) |
| `dati/img/personaggi/personaggi.json` | PERSONAGGI | la galleria «I personaggi» (vuota nella base) |
| `dati/img/copertina.jpg` | PERSONAGGI | facoltativa: se c'è, diventa lo sfondo della schermata iniziale |
| `dati/protagonista.json` | PROTAGONISTA e TESTI | nome e colore della giacca del macchinista |
| `dati/testi.json` | PROTAGONISTA e TESTI | titolo, sottotitolo, frasi dei cattivi, frasi di fine partita (`{vetro}` diventa il numero di colpi) |
| `dati/suoni.json` | SUONI | volume e note della vittoria |
| `dati/record-classe.json` | il prof | i record della classe (solo squadra o soprannome, mai nomi e cognomi) |
| `dati/versione.json` | il prof | numero e nome della versione (si vede in basso a destra) |

1. Un file scritto male non blocca il gioco: nella schermata iniziale compare «Controllo dei file» con il nome del file e la riga da sistemare.
2. Le immagini (facce, personaggi, cattivi `pcNN.png`) si mettono nella loro cartella; Godot le prepara da solo quando si apre il progetto.
3. Dopo aver cambiato un dato bisogna **esportare di nuovo** il gioco per il Web (punto 6): il browser legge i dati dal pacchetto esportato.

## 5 La memoria del giocatore (privacy)

1. Record, migliori punteggi, soprannome e «Facce della classe» restano **solo sul dispositivo** di chi gioca: niente va in rete né su GitHub.
2. Nel browser si usa la stessa memoria (e gli stessi nomi, `treno-2inf-...`) della versione HTML: sullo stesso sito record e facce sono in comune con il treno HTML. Accanto a ogni punteggio c'è la versione del gioco (v0.31, v1.0...).

## 6 Come si fa una versione nuova

1. Si fa la modifica (dati o codice) e si prova con F5.
2. Si cambia il numero in `dati/versione.json` (MAJOR.MINOR.PATCH: cambio grosso . aggiunta . correzione).
3. Si esporta per il Web: in Godot, menu «Progetto» → «Esporta...» → preset «Web» → «Esporta progetto» (il percorso è già impostato: `../docs/giochi/treno-2inf-godot/index.html`), togliendo la spunta «Esporta con debug».
4. Si congela la versione (lo fa il prof o Claude):

```
python3 strumenti/congela_versione.py 1.1 "Nome della versione" "Cosa cambia"
```

5. Si scrive la voce nel `CHANGELOG.md` (cosa cambia e perché).
6. Si fa il commit e il push: GitHub Pages pubblica la versione nuova; quella vecchia resta giocabile in `versioni/`.

Esportazione senza aprire l'editor (per Claude, dalla cartella `treno-2inf-godot`):

```
Godot_v4.7-stable_linux.x86_64 --headless --path . --export-release "Web" ../docs/giochi/treno-2inf-godot/index.html
```

## 7 Controllo automatico

1. Aggiungendo `?prova` all'indirizzo del gioco, la pagina scrive lo stato della partita in `window.__treno` (punti, vetro, posizione dei cattivi, posizione dei bottoni): serve ai controlli automatici con il browser.
2. Dal terminale: `Godot --headless --path . -- prova` fa partire una partita da sola (senza finestra) e stampa lo stato.
