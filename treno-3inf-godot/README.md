# Il treno blindato della 3INF (Godot)

**Versione 2.6** — 14/10/2026 — motore Godot 4.7 — fork pulito della base del prof (`treno-3inf-godot` v1.0)

## 1 Cos'è

1. È il treno della classe 3INF rifatto partendo dalla **base del prof** su Godot (v1.0). La base resta intatta in `treno-prof-godot/`.
2. Perché 2.0: il treno della 3INF di prima (v1.0 … v1.11) era in HTML; è cambiato il motore, quindi versione «major».
3. Si gioca nel browser: `docs/giochi/treno-3inf-v2/`. Le versioni congelate sono in `docs/giochi/treno-3inf-v2/versioni/`.
4. Le richieste della classe (Noah, Andrea G., Ariel, David A., Tomas) sono state rifatte una alla volta, una versione ciascuna: vedi `CHANGELOG.md`.
5. Chiavi nuove del motore della 3INF: `aumento_per_livello` (regole.json), `rocce_varie` (ambienti), `tuta` e `pelle` (cattivi).

## 2 Come si apre con Godot portabile

1. Avviare Godot 4.7 portabile (doppio clic sul file `.exe`).
2. Nella finestra «Gestore dei progetti» premere «Importa».
3. Scegliere il file `project.godot` di questa cartella (`treno-3inf-godot`).
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
| `strumenti/indice_versioni.py` | strumento del prof: rifà la pagina di tutte le versioni da `versioni/versioni.json` |

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
2. Nel browser si usa la memoria del browser con i nomi `treno-3inf-v2-...`: record e facce della base sono separati da quelli del treno HTML della 2INF. Accanto a ogni punteggio c'è la versione del gioco (v0.31, v1.0...).

## 6 Come si fa una versione nuova

1. Si fa la modifica (dati o codice) e si prova con F5.
2. Si cambia il numero in `dati/versione.json` (MAJOR.MINOR.PATCH: cambio grosso . aggiunta . correzione).
3. Si esporta per il Web: in Godot, menu «Progetto» → «Esporta...» → preset «Web» → «Esporta progetto» (il percorso è già impostato: `../docs/giochi/treno-3inf-v2/index.html`), togliendo la spunta «Esporta con debug».
4. Si congela la versione, dalla radice del repository (lo fa il prof o Claude), e si aggiunge la riga in `docs/giochi/treno-3inf-v2/versioni/versioni.json`:

```
python3 strumenti/versione_treno_godot.py v2.7 treno-3inf-v2
python3 treno-3inf-godot/strumenti/indice_versioni.py
```

5. Si scrive la voce nel `CHANGELOG.md` (cosa cambia e perché).
6. Si fa il commit e il push: GitHub Pages pubblica la versione nuova; quella vecchia resta giocabile in `versioni/`.

Esportazione senza aprire l'editor (per Claude, dalla cartella `treno-3inf-godot`):

```
Godot_v4.7-stable_linux.x86_64 --headless --path . --export-release "Web" ../docs/giochi/treno-3inf-v2/index.html
```

## 7 Controllo automatico

1. Aggiungendo `?prova` all'indirizzo del gioco, la pagina scrive lo stato della partita in `window.__treno` (punti, vetro, posizione dei cattivi, posizione dei bottoni): serve ai controlli automatici con il browser.
2. Dal terminale: `Godot --headless --path . -- prova` fa partire una partita da sola (senza finestra) e stampa lo stato.
