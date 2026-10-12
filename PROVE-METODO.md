# Le prove che il metodo funziona

**Versione 0.1** — 12/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano. Area Docente.

Raccolta, lezione per lezione, dei dati che mostrano se il metodo «una scuola che lavora come un'azienda di software» funziona. Qui non ci sono nomi: ogni ragazzo è «Allievo NN», con lo stesso numero della demo. La versione con nome e iniziale sta nel repository riservato, in `prove-metodo/`. I dati si calcolano da soli con `strumenti/prove_metodo.py`, a partire dalle pagine della lezione (voti, backlog, monitor).

## 00 Cosa si misura

1. **Partecipazione:** quanti presenti mandano almeno una Pull Request (PR) e il Feedback sulla teoria.
2. **Produzione:** quante PR arrivano, quante entrano nel gioco, quante versioni nuove nascono.
3. **Ritmo:** quante PR arrivano ogni quarto d'ora, e prima e dopo la pubblicazione dei voti.
4. **Recuperi:** chi era sotto la sufficienza (meno di 5 PR) e la raggiunge dopo aver visto i voti pubblici.
5. **Attenzione:** quanti schermi sono sul compito durante i giri del docente con Veyon.
6. **Qualità:** quante PR sono scritte bene, con le quattro parti (Titolo, Cosa cambia, Dove, Perché).

> **Nota:** una sola lezione non è una prova. Le prove vere sono la stessa misura ripetuta per settimane e per classi diverse, con le stesse regole.

<!-- 20261012_2INF -->
## 20261012_2INF

| Indicatore | Valore |
|---|---|
| Presenti | 17 |
| Hanno mandato almeno una Pull Request (PR) | 17 su 17 |
| Hanno mandato il Feedback sulla teoria | 17 su 17 |
| PR ricevute | 129 |
| PR entrate nel gioco | 30 |
| PR rifiutate con il motivo | 12 |
| Versioni nuove del gioco nate dalle PR | 19 |
| PR scritte bene con le quattro parti | 9 |
| Schermi sul compito durante i giri del docente | 107 su 117 (91%) |

**PR ricevute ogni quarto d'ora:** 12:15 3, 12:30 4, 12:45 22, 13:00 49, 13:15 23, 13:30 21, 13:45 7.

**Prima e dopo i voti pubblici (ore 13:22), tutte le richieste inviate:** 93 in 59 minuti prima (1.6 al minuto), 36 in 32 minuti dopo (1.1 al minuto). Il ritmo della classe nel complesso cala verso la fine della lezione; l'effetto dei voti pubblici si vede su chi era indietro (qui sotto).

**Recuperi dopo i voti pubblici** (sotto le 5 PR prima delle 13:22, almeno 5 alla fine):

1. Allievo 09: 2 richieste prima, 9 richieste dopo; voto finale 80.
2. Allievo 17: 1 richiesta prima, 4 richieste dopo; voto finale 62.
<!-- fine 20261012_2INF -->

## 99 Registro delle versioni

1. **v0.1 (12/10/2026)**: prima versione, con la lezione della 2INF del 12/10/2026.
