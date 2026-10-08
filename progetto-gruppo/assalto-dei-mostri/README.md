# Assalto dei Mostri

Il gioco della classe 3INF (Centro Padre Piamarta, Milano). Si gioca sul telefono: i mostri sbucano da tutte le parti, li tocchi prima che sparino al tuo vetro.

**Giocalo qui:** https://nicolaregge-pulse.github.io/assalto-dei-mostri/

## Come lavoriamo: come una vera azienda di software

1. **Il prodotto** è il gioco. Il **product owner** (il prof) decide cosa entra in ogni versione.
2. **Il lavoro è diviso in pezzi**: ogni pezzo è un file separato, così ognuno lavora sul suo senza rompere quello degli altri.
3. **Il backlog** (la lista dei lavori da fare) sta nelle **Issues** del repository. Ogni Issue è un lavoro: lo prendi, lo fai, lo chiudi.
4. **Nessuno scrive direttamente qui.** Ognuno lavora sulla sua copia (**fork**) e propone la modifica con una **Pull Request**.
5. Un **controllo automatico** guarda ogni Pull Request: se c'è un errore compare una X rossa e c'è scritto cosa sistemare.
6. Il prof fa la **revisione** e il **merge** (unisce la modifica al gioco).
7. Quando una versione è pronta si fa una **release** (v1.0, v1.1, v1.2...). La storia di tutti i lavori si vede in **Insights → Network**.

## I pezzi del gioco

| File | Squadra | Cosa contiene |
|---|---|---|
| `mostri/pc01.json` ... `mostri/pc40.json` | tutti, uno a testa | il tuo mostro: il file ha il numero del tuo PC |
| `mostri/pc01.png` ... | chi vuole | l'immagine del tuo mostro (facoltativa) |
| `regole.json` | REGOLE | quanti colpi regge il vetro, quanto in fretta sparano i mostri, i punti |
| `grafica.json` | GRAFICA | i colori della città: cielo, luna, palazzi, finestre, strada |
| `testi.json` | TESTI | il titolo, le frasi di fine partita, i messaggi |
| `suoni.json` | SUONI | il volume e le note della musica di vittoria |
| `index.html` | MOTORE (il prof) | il programma che legge tutti i pezzi |

## Il tuo mostro (il primo lavoro di tutti)

Il file si chiama come il tuo PC, con due cifre: PC 7 → `mostri/pc07.json`. Copia l'esempio `mostri/pc00-ESEMPIO.json` e cambia i valori:

| Campo | Cosa puoi mettere |
|---|---|
| `nome` | il nome del mostro (massimo 24 caratteri) |
| `colore` | un colore come `#ff6fb1` (cerca «color picker» su Google) |
| `occhi` | 1, 2 oppure 3 |
| `corna` | 0 = senza, 1 = con le corna |
| `bocca` | 0 = denti, 1 = lingua, 2 = zig-zag |
| `velocita` | 1 = normale, 2 = veloce, 3 = velocissimo |
| `frase` | cosa grida quando ti spara (massimo 40 caratteri) |
| `immagine` | `true` se carichi anche `mostri/pcNN.png`, altrimenti `false` |

**Regole:** niente nomi e cognomi veri, niente email, link o numeri di telefono, niente parolacce. Negli `autori` dei file di squadra si scrive solo il numero del PC, per esempio `"PC 14"`.

## Le versioni

| Versione | Cosa contiene | Stato |
|---|---|---|
| v1.0 | Il motore: mostri casuali, vetro, livelli, audio | fatta |
| v1.1 | I mostri della classe (un mostro per ogni PC) | in lavorazione |
| v1.2 | Il lavoro delle squadre: regole, grafica, testi, suoni | in lavorazione |
| v2.0 | Il gioco rifatto in Godot | da progettare |

La storia delle modifiche è in `CHANGELOG.md`.
