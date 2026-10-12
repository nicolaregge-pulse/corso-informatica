# Storia delle versioni

## v0.15 — 12/10/2026 12:56 — La difficoltà cresce a ogni livello

1. Pull Request di Antonio M. (12:38): «la difficoltà non aumenta: a ogni livello la difficoltà aumenta».
2. A ogni livello i cattivi sparano 0,3 secondi prima (prima era 0,12) e arrivano più spesso: al livello 1 il gioco è uguale, dal livello 2 si sente la differenza.
3. La seconda parte della sua richiesta, «un’arma nuova a ogni livello», resta nel backlog: è un lavoro più grande (peso 8).
4. Peso 2 nel backlog: si cambiano due numeri in index.html.

## v0.14 — 12/10/2026 12:54 — Ultimo colpo

1. Pull Request di Egor M. (12:31): «dopo che si spacca il vetro si muore subito: farlo diventare che si ha comunque 1 colpo tankabile».
2. Quando il vetro arriva a zero compare la scritta «VETRO ROTTO! ULTIMO COLPO!»: si può ancora giocare. La partita finisce al colpo dopo.
3. Peso 2 nel backlog: una regola piccola in index.html, nella funzione spara.

## v0.13 — 12/10/2026 12:54 — Nuovo livello, nuovo scenario

1. Pull Request di Ney V. (12:29): «cambiare lo scenario quando si cambia di livello». La stessa richiesta è arrivata da Alejandro G. (12:45): «quando cambia livello cambi la mappa».
2. Prima lo scenario cambiava solo ogni 20 secondi. Ora, appena passi di livello, il treno entra subito nello scenario dopo e compare il suo nome in grande.
3. Peso 2 nel backlog: una riga di codice in index.html, dove si passa di livello.

## v0.12 — 12/10/2026 12:30 — La versione serale (PR di Mahammed M.)

1. Pull Request del 12/10 alle 12:23, dal Modulo «Consegna»: «vorrei una versione serale».
2. Il Paese, la Montagna e il Mare hanno il cielo del tramonto: viola in alto, arancione verso l'orizzonte; colline e terra più scure, come di sera.
3. La Città era già di notte e il Bosco resta rosso cupo (scelta della squadra SCENARI): non cambiano.
4. Peso 1 nel backlog: si cambiano solo colori, nei file dentro la cartella `ambienti/`.

## v0.11 — 08/10/2026 10:58 — I punteggi si salvano sempre (difetto segnalato dal prof)

1. Difetto: «non chiede il nome e non salva i punteggi».
2. Il punteggio ora si salva da solo appena finisce la partita (come «Anonimo»); il soprannome si può scrivere dopo e si conferma anche con il tasto Invio. Il soprannome viene ricordato per la partita dopo.
3. Il telefono teneva in memoria la versione vecchia del gioco: ora il gioco chiede sempre la versione nuova alla rete.

## v0.10 — 08/10/2026 10:52 — I migliori punteggi (indicazione del prof)

1. A fine partita, se il punteggio entra nei primi 10, si scrive un soprannome (mai nome e cognome) e si salva.
2. Nella schermata iniziale: «I migliori punteggi su questo dispositivo» (i primi 10, con la versione del gioco).
3. «Record della classe»: file record-classe.json, lo aggiorna il prof con i record consegnati (solo squadra o soprannome).

## v0.9 — 08/10/2026 10:48 — Teste in proporzione (indicazione del prof)

1. «Una faccia è troppo grossa e sproporzionata»: la testa aveva una misura minima fissa, quindi gli omini lontani avevano la testa enorme. Ora la testa è sempre in proporzione al corpo.

## v0.8 — 08/10/2026 10:45 — Mimetica, facce senza cerchio, fucile d'assalto (indicazioni del prof)

1. Le facce non hanno più il cerchio bianco: si vede solo la faccia, ritagliata a forma di testa.
2. Il tempo prima dello sparo è una barretta sopra la testa (gialla, poi rossa).
3. Tutti gli omini sono vestiti con la mimetica.
4. Il personaggio «Agente Speciale» imbraccia un fucile d'assalto (calcio e paramano di legno, caricatore curvo).

## v0.7 — 08/10/2026 10:36 — Omini che escono dal nascondiglio (indicazione del prof)

1. Indicazione del product owner (il prof): «metti gli omini, non i cerchietti, e che escano dal nascondiglio».
2. Ogni cattivo è un omino intero: testa (con la faccia della classe o con la maschera da bandito), busto, braccia, gambe e arma puntata verso il treno.
3. Esce dal nascondiglio: è accucciato dietro l'albero, la casa o il rottame, si alza e fa un passo fuori di lato, con un «!» rosso.
4. Quando lo colpisci cade all'indietro.

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
