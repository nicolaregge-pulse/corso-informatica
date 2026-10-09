# Changelog — Il treno blindato su Godot (1INF)

Ogni versione dice **cosa cambia e perché**. I numeri si leggono così: MAJOR.MINOR.PATCH
(cambio grosso . aggiunta . correzione di un errore). Ogni versione si gioca al suo link:
`https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-godot/versioni/<versione>/`
L'ultima versione è sempre a `https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-godot/`.

## v2.1.3 — 09/10/2026 — Il numero di versione si vede sempre (PATCH)

1. **Richiesta del prof**: in alto a sinistra, per tutta la partita, c'è scritto «Treno blindato v2.1.3». Così si vede subito quale versione si sta giocando: è il tema della lezione.
2. Il numero sta in un solo punto del codice (`const VERSIONE`), usato sia nella scritta in alto sia nella schermata iniziale.
3. Perché PATCH: piccola correzione dell'interfaccia, sale il terzo numero (2.1.2 → 2.1.3).

## v2.1.2 — 09/10/2026 — Facce rifatte (PATCH)

1. **Errore corretto**, segnalato dal prof: la faccia del prof non era centrata e quella di Subaru Natsuki mostrava anche il corpo.
2. **Come**: ogni faccia si prepara prima con lo strumento `strumenti/testa_personaggio.py`: si misura il riquadro della testa sull'originale, si ritaglia centrato, si ridimensiona tutto alla stessa misura (256 x 294) e si taglia la forma testa ovale + collo.
3. Perché PATCH: è una correzione, sale il terzo numero (2.1.1 → 2.1.2).

## v2.1.1 — 09/10/2026 — Correzione: il vetro si rompe (PATCH)

1. **Errore corretto**, segnalato dalla 1INF (Mathew F.: «anche se non spari il vetro non si rompe»). Il treno superava i cattivi prima che sparassero: il vetro non si rompeva mai e non si perdeva.
2. **Come**: il cattivo si nasconde più lontano e il suo tempo per sparare non supera il tempo in cui resta visibile. Provato in automatico: senza cliccare, 5 colpi e la partita finisce.
3. **Facce dei personaggi** ritagliate a forma di testa, con il collo, e ridimensionate tutte uguali.
4. Perché PATCH: è la correzione di un errore, sale il terzo numero (2.1 → 2.1.1).

## v2.1 — 09/10/2026 — I personaggi della 1INF (MINOR)

1. **Nuova funzione**: i cattivi possono avere la faccia di un personaggio scelto dai ragazzi (immagine presa dal web e consegnata con il Modulo «Consegna»), con il nome sopra la testa.
2. Primi personaggi: Prof. Regge e Subaru Natsuki (Wesley J.).
3. Perché MINOR: è un'aggiunta, sale il secondo numero (2.0 → 2.1).

## v2.0 — 09/10/2026 — Il treno su Godot (MAJOR)

1. Lo stesso gioco della 1INF v1.1 (cattivi Hidra, EI, Mister Bar Berry e i cieli della 1INF), rifatto con il motore Godot 4.7 ed esportato per il browser.
2. Perché MAJOR: è cambiato il motore, una cosa grossa, sale il primo numero (1.x → 2.0).
