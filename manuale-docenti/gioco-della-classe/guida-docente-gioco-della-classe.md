# Il gioco della classe: guida del docente

**Versione 1.1** — 08/10/2026 · Area Docente · Prof. Nicola Regge, Centro Padre Piamarta, Milano

Come condurre una lezione di ingegneria del software con la classe: un gioco per il telefono costruito da tutti, con fork, Pull Request (proposta di modifica), revisione, merge (unione), release (versioni numerate) e il grafico delle versioni. Prima applicazione: 3INF, giovedì 08/10/2026, «Assalto dei mostri». Nessun nome di allievo in questo documento.

## 00 L'idea in breve

1. Il gioco è diviso in **pezzi**, ognuno in un file separato: un mostro per ogni PC (`mostri/pc07.json`) e un file per ogni squadra (regole, grafica, testi, suoni). Ognuno lavora sul suo file: niente conflitti per sbaglio.
2. I ragazzi **non scrivono** nel repository del corso: fanno la loro copia (fork) e propongono la modifica con una Pull Request, tutto dal browser. Il controllo automatico rifiuta le Pull Request che toccano file fuori da `docs/giochi/`.
3. Un **controllo automatico** guarda ogni Pull Request: spunta verde se il file è giusto, X rossa con la spiegazione se c'è un errore (di solito una virgola).
4. Il docente fa il **merge** e pubblica le **release** del gioco: assalto-v1.0 il motore, assalto-v1.1 i mostri della classe, assalto-v1.2 il lavoro delle squadre (il prefisso «assalto-» le tiene separate dalle release del corso).
5. Alla fine si guarda insieme il **grafico** (Insights → Network): ogni fork, ogni commit, ogni merge.

| Cosa | Dove |
|---|---|
| Cartella del gioco su GitHub (repository del corso) | `https://github.com/nicolaregge-pulse/corso-informatica/tree/main/docs/giochi/assalto-dei-mostri` |
| Il gioco online | `https://nicolaregge-pulse.github.io/corso-informatica/giochi/assalto-dei-mostri/` |
| Pagina della classe (dispensa, «scegli il tuo PC», compito) | `https://nicolaregge-pulse.github.io/corso-informatica/3inf-sito/` |
| Tutti i giochi del corso | `https://nicolaregge-pulse.github.io/corso-informatica/giochi/` |

## 01 Scaletta della lezione (2 ore)

| Ora | Cosa | Ruolo del docente |
|---|---|---|
| 0-10 min | Presentazione: «oggi siete un'azienda di software». Ruoli: product owner (il docente), project manager (uno per squadra, a turno), sviluppatori, revisori | mostra il gioco v1.0 sul proiettore |
| 10-35 min | Tutti: il proprio mostro con una Pull Request | gira tra i banchi; fa i primi merge al proiettore |
| 35-40 min | Release v1.1: i mostri della classe entrano nel gioco | pubblica la release, tutti giocano dal telefono |
| 40-75 min | Squadre REGOLE, GRAFICA, TESTI, SUONI: backlog su carta (chi fa cosa), decisione su carta, Pull Request del project manager, revisione di un compagno di un'altra squadra | fa vedere un conflitto vero e lo risolve con la classe |
| 75-85 min | Release v1.2 e grafico delle versioni (Insights → Network); i ragazzi lo disegnano a mano | commenta il grafico |
| 85-105 min | Documento su Classroom: lavoro di squadra (5 competenze, voto 1-4 con esempio vero) e «cosa ho imparato qui che altrove non avrei imparato» | raccoglie |
| 105-120 min | Gara con i telefoni: chi fa il record | celebra |

> **Nota:** carta e penna sul banco: le squadre decidono i valori su carta prima di toccare il file, e ognuno disegna il grafico delle versioni.

## 02 Le squadre

| Squadra | File | Cosa decide |
|---|---|---|
| Tutti | `mostri/pcNN.json` | il proprio mostro (nome, colore, occhi, corna, bocca, velocità, frase) |
| REGOLE | `regole.json` | colpi che regge il vetro, secondi prima che i mostri sparino, mostri per livello, punti |
| GRAFICA | `grafica.json` | colori di cielo, luna, palazzi, finestre e strada |
| TESTI | `testi.json` | titolo, sottotitolo, frasi di fine partita (anche nelle lingue dei ragazzi) |
| SUONI | `suoni.json` | volume e note della musica di vittoria |

1. Squadre di 3-4, composte dal docente; il project manager cambia a ogni progetto.
2. Negli `autori` dei file di squadra si scrive solo il numero del PC (per esempio `"PC 14"`), mai nomi e cognomi.

## 03 Fare il merge di una Pull Request

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PERSONALE | Chrome gialla, repository corso-informatica | in alto, scheda «Pull requests» | clic |
| 2 | PERSONALE | elenco delle Pull Request | il titolo della Pull Request | clic |
| 3 | PERSONALE | pagina della Pull Request | in basso, riquadro dei controlli | deve esserci la spunta verde «All checks have passed» |
| 4 | PERSONALE | stessa pagina | scheda «Files changed» | guarda il file: solo il file del suo PC, niente dati personali |
| 5 | PERSONALE | scheda «Conversation» | bottone verde «Merge pull request» | clic |
| 6 | PERSONALE | stessa pagina | bottone verde «Confirm merge» | clic: la Pull Request diventa viola, «Merged» |

> **Attenzione:** con la X rossa non si fa il merge: il ragazzo apre «Details», legge cosa sistemare e corregge il file nella sua copia; la Pull Request si aggiorna da sola.

## 04 Un conflitto, da far vedere alla classe

Succede quando due Pull Request cambiano la stessa riga dello stesso file (di solito nei file di squadra).

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PERSONALE | pagina della Pull Request in conflitto | in basso, bottone «Resolve conflicts» | clic |
| 2 | PERSONALE | editor dei conflitti | righe tra `<<<<<<<` e `>>>>>>>` | si sceglie con la classe quale versione tenere e si cancellano i segni `<<<<<<<`, `=======`, `>>>>>>>` |
| 3 | PERSONALE | stessa pagina | in alto a destra, «Mark as resolved» | clic |
| 4 | PERSONALE | stessa pagina | bottone verde «Commit merge» | clic, poi il merge come al capitolo 03 |

## 05 Pubblicare una release (versione)

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PERSONALE | repository corso-informatica | colonna a destra, «Releases» → «Create a new release» | clic |
| 2 | PERSONALE | pagina della release | «Choose a tag» | scrivi il numero (per esempio assalto-v1.1) e scegli «Create new tag» |
| 3 | PERSONALE | stessa pagina | «Release title» e descrizione | per esempio «Assalto dei mostri v1.1 — I mostri della classe» |
| 4 | PERSONALE | in fondo | bottone verde «Publish release» | clic |

> **Nota:** il numero che si vede nel gioco (in basso a destra) sta nel file `versione.json`: Claude lo aggiorna insieme alla storia delle versioni (`CHANGELOG.md`) a ogni release.

## 06 Il grafico delle versioni

1. Nel repository del corso: scheda «Insights» → a sinistra «Network». Si vedono la linea principale (main), le copie dei ragazzi, i loro commit e le frecce dei merge.
2. In alternativa: «Commits» per l'elenco in ordine di tempo, con chi ha fatto cosa.

## 07 Cosa fa Claude in automatico

1. Prepara il gioco, i pezzi, il controllo automatico, la dispensa, il compito su Classroom e la pagina della classe.
2. Su comando del docente («controlla le Pull Request») legge le Pull Request, segnala quelle con errori o con dati personali e, se il docente lo chiede, fa i merge di quelle con la spunta verde.
3. Aggiorna `versione.json` e `CHANGELOG.md` a ogni release e tiene allineata la copia nel repository del corso.

## 08 Changelog

1. **v1.1 (08/10/2026)** — il gioco sta nel repository del corso, in `docs/giochi/` (decisione di Nicola): indirizzi aggiornati, release con prefisso «assalto-».
2. **v1.0 (08/10/2026)** — prima versione: idea, scaletta, squadre, merge, conflitto, release, grafico, cosa fa Claude.
