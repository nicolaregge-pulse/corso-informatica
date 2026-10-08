# Storia delle versioni

## v0.6 — 08/10/2026 10:30 — Il bosco bruciato (SCENARI) e la frase del cattivo (PERSONAGGI)

1. Richiesta della squadra SCENARI (Documento su Classroom): «nel bosco il cielo rosso cupo e vicino ai binari alberi bruciati e rottami, perché il treno è appena passato dopo un attacco».
2. Il primo ambiente ora è il «Bosco bruciato»: cielo rosso cupo, alberi neri, rottami fumanti con le braci vicino ai binari.
3. Richiesta della squadra PERSONAGGI: quando spara, il cattivo dice «Hahahahaha, perdente!».
4. Richiesta della squadra MOTORE FISICA (Documento su Classroom, con il link alla Pull Request #104): già nella versione 0.5.

## v0.5 — 08/10/2026 10:22 — Le regole della squadra MOTORE FISICA

1. Prima Pull Request VERA arrivata su GitHub: #104, del capo squadra MOTORE FISICA.
2. Velocità del treno 0,5 (confermata), i cattivi sparano dopo 3 secondi (prima 2,8), 100 punti per ogni cattivo colpito (prima 10).
3. Nella Pull Request c'era «0,5» con la virgola: in JSON i decimali si scrivono con il PUNTO (0.5). Il valore è stato messo giusto qui.

## v0.4 — 08/10/2026 10:16 — Audit degli investitori

1. Gli investitori: «treno troppo veloce, non si vedono le facce, le facce sono in un riquadro: doveva esserci il personaggio nascosto che esce».
2. Il cattivo ora è un personaggio intero (testa con la faccia, corpo, braccia e arma): sta NASCOSTO dietro l'albero, la casa o il barile e scivola fuori di lato.
3. Personaggi più grandi e più vicini; si colpiscono toccando la testa o il corpo.
4. Velocità del treno al minimo (0,5).
5. Tolte due foto in cui la faccia non si vedeva (solo capelli).

## v0.3 — 08/10/2026 10:08 — Più lento (richiesta della squadra TEST QUALITÀ)

1. Richiesta di modifica della Triade, consegnata su Classroom: «il gioco va troppo veloce».
2. Velocità del treno da 1 a 0,7: i cattivi restano a schermo più a lungo e si fa in tempo a colpirli.

## v0.2 — 08/10/2026 09:50 — I personaggi della squadra PERSONAGGI

1. Quattro personaggi disegnati con l'IA dalla squadra PERSONAGGI: tre agenti che difendono il treno e il Boss dei cattivi.
2. Nuovo bottone «I personaggi» nella schermata iniziale.
3. Le loro facce compaiono nel gioco, insieme a quelle della classe.

## v0.1 alfa — 08/10/2026 — La demo del prof

La versione di partenza, fatta dal prof (con Claude) sul progetto della lavagna. Da qui la classe corregge il tiro: regole, scenari, personaggi, testi. La v1.0 sarà la prima versione della classe.

### Cosa c'è

1. Vista dal vagone: paesaggio che scorre su tre piani, cinque ambienti (bosco, paese, città, montagna, mare).
2. I cattivi sbucano da dietro alberi, case e rocce o dal basso; si toccano per fermarli.
3. Il vetro antiproiettile regge 5 colpi, si crepa a ogni colpo, poi va in pezzi; audio del treno, degli spari e del vetro.
4. Il gioco legge i pezzi della classe da file separati e segnala i file sbagliati senza bloccarsi.
