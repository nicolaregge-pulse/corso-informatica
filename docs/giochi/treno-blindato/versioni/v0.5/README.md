# Il treno blindato

Il gioco della classe 2INF (Centro Padre Piamarta, Milano). Sei dentro un vagone: il treno attraversa boschi, paesi, città, montagne e mare; i cattivi saltano fuori da dietro alberi e case. Li tocchi prima che sparino: il vetro antiproiettile regge 5 colpi.

**Il progetto della classe (lavagna dell'08/10):** si guarda avanti dalla cabina, lungo i binari; i cattivi spuntano dalle finestre delle case, da dietro gli alberi e dai barili. Tre cose da curare: dinamica, UI (cosa si vede), UX (come ci si sente a giocare).

**Gioca:** https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/

## Come lavoriamo (come una vera azienda di software)

1. Il prodotto è il gioco; il product owner è il prof.
2. Il lavoro è diviso in pezzi: ogni pezzo è un file separato.
3. Ognuno lavora sulla sua copia (fork) e propone la modifica con una Pull Request.
4. Il controllo automatico guarda ogni Pull Request; il prof fa la revisione e il merge.
5. Quando una versione è pronta si fa una release (treno-v1.0, treno-v1.1...). La storia si vede in Insights → Network.

## I pezzi del gioco

| File | Squadra | Cosa contiene |
|---|---|---|
| `cattivi/pc01.json` ... `pc40.json` | CATTIVI: tutti, uno a testa | il tuo cattivo (il file ha il numero del tuo PC) |
| `ambienti/bosco.json`, `case.json`, `citta.json`, `montagna.json`, `mare.json` | AMBIENTI: uno per ambiente | colori del cielo e della terra, che oggetti ci sono (alberi, case, palazzi, rocce, onde), quanti |
| `percorso.json` | PERCORSO e REGOLE | l'ordine degli ambienti e quanti secondi dura ognuno |
| `regole.json` | PERCORSO e REGOLE | colpi del vetro, velocità del treno, tempo dei cattivi, punti |
| `facce.json` + cartella `facce/` | PERSONAGGI | le facce dei compagni che hanno dato la foto (maggiorenni, foto date da loro): ritagliate sul viso |
| `protagonista.json` | PROTAGONISTA e TESTI | nome e colori del protagonista |
| `testi.json` | PROTAGONISTA e TESTI | titolo, frasi di fine partita (anche nelle vostre lingue) |
| `suoni.json` | SUONI | volume e note della vittoria |
| `index.html` | MOTORE (il prof) | il programma che legge tutti i pezzi |

## Il tuo cattivo

| Campo | Cosa puoi mettere |
|---|---|
| `nome` | il nome del cattivo (massimo 24 caratteri) |
| `colore` | un colore come `#8a8f98` |
| `occhi` | 1, 2 oppure 3 |
| `cappello` | 0 = niente, 1 = cappello, 2 = bandana sul viso |
| `bocca` | 0 = denti, 1 = bocca aperta, 2 = zig-zag |
| `velocita` | 1 = normale, 2 = veloce, 3 = velocissimo |
| `frase` | cosa grida quando spara (massimo 40 caratteri) |
| `immagine` | `true` se carichi anche `cattivi/pcNN.png` (inventato con l'IA), altrimenti `false` |

**Regole:** nei file dei cattivi niente nomi veri, email, link, numeri di telefono o parolacce. Le foto vere vanno solo nella cartella `facce/`, solo di chi è maggiorenne e ha dato la sua foto; chi non vuole la sua faccia nel gioco lo dice e la si toglie subito.
