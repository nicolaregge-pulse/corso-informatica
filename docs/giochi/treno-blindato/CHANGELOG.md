# Storia delle versioni

## v0.27 — 12/10/2026 13:22 — Binari gialli

1. Pull Request di Katherine A. (13:19): «Cambiare colore ai binari: gialli invece che grigi, in tutta la partita, così si vedono meglio».
2. I due binari sono gialli in tutti gli scenari.
3. Peso 1 nel backlog: si cambia un colore in index.html. PR scritta bene, con le 4 parti.

## v0.26 — 12/10/2026 13:19 — Pioggia e nebbia

1. Pull Request di Lina A. (13:10), «Condizioni meteo dinamiche (pioggia e nebbia)»; la stessa idea è arrivata da Youssef A. (13:11), Riccardo B. (13:12, «Il meteo variabile») e Oscar F. (13:13, «nebbia che rende i nemici meno visibili»).
2. Dal livello 2 il cielo diventa grigio, dal livello 3 piove, dal livello 4 arriva anche la nebbia: i cattivi si vedono meno, quindi il gioco diventa più difficile.
3. Il codice viene dal fork della 3INF (la loro versione 1.2): un esempio vero di come un lavoro fatto su un ramo si può riprendere in un altro.
4. Peso 5 nel backlog: un effetto nuovo sul paesaggio, in index.html.

## v0.25 — 12/10/2026 13:18 — Colpo preciso

1. Pull Request di Giorgio A. (13:16): «se il giocatore colpisce un cattivo con un colpo preciso, riceve punti bonus, così conviene mirare bene».
2. Se colpisci il cattivo proprio sulla testa compare «COLPO PRECISO +50» e prendi 50 punti in più; se lo colpisci sul corpo, i punti sono quelli normali.
3. Peso 2 nel backlog: una regola piccola in index.html, dove si spara e dove si contano i punti.

## v0.24 — 12/10/2026 13:17 — Più avanti, più punti

1. Pull Request di Luciano C. (13:14): «più vai avanti nel gioco e i nemici ti danno più punti».
2. Ogni cattivo colpito vale il 50% in più a ogni livello: 100 punti al livello 1, 150 al livello 2, 200 al livello 3, e così via (più il bonus della combo).
3. Peso 2 nel backlog: si cambia un calcolo in index.html, dove si contano i punti.

## v0.23 — 12/10/2026 13:07 — Il bottone Pausa

1. Pull Request di Lina A. (13:03): «Aggiunta del pulsante Pausa: un tasto in alto per mettere in pausa il gioco e riprenderlo quando si vuole, nell’interfaccia e nel codice di controllo, per fermare la partita senza perdere i progressi».
2. Durante la partita, in alto a destra, c’è il bottone blu «Pausa»: il gioco si ferma e compare la scritta PAUSA; il bottone diventa «Riprendi». Funziona anche con il tasto P o Esc.
3. In pausa non si spara e i cattivi non si muovono: punti, vetro e livello restano come sono.
4. Peso 3 nel backlog: un bottone nuovo e una regola nel ciclo del gioco, in index.html.

## v0.22 — 12/10/2026 13:05 — Il record accanto ai punti

1. Pull Request di Youssef A. (13:04): «Punteggio migliore salvato: salvare il record e mostrarlo accanto al contatore, così resta anche dopo aver ricaricato la pagina».
2. In alto, accanto a «Punti», c’è la scritta gialla «Record» con il punteggio migliore fatto su questo computer. Si salva nel browser, quindi resta anche se ricarichi la pagina; se lo superi, il record sale mentre giochi.
3. Peso 2 nel backlog: una riga in index.html, dove si scrivono i punti.

## v0.21 — 12/10/2026 13:03 — Le luci dei palazzi non lampeggiano più

1. Pull Request di Luca B. (13:01): «sistemare le luci che lampeggiano di continuo nelle case e nei palazzi»; dove: case e palazzi; perché: è un difetto.
2. Causa: le finestre accese dei palazzi erano scelte in base alla posizione sullo schermo; il palazzo si muove, quindi a ogni istante si accendevano finestre diverse.
3. Correzione: ogni palazzo ha le sue finestre accese, sempre le stesse, mentre si avvicina.
4. Peso 2 nel backlog: un difetto piccolo, una riga di index.html.

## v0.20 — 12/10/2026 13:02 — I cattivi si vedono sempre

1. Pull Request di Egor M. (12:57): «migliorare gli ostacoli dove si nascondono i nemici (case, palazzi…): a volte escono male e il nemico non si vede».
2. Causa: il cattivo veniva disegnato insieme al suo nascondiglio, quindi le case e i palazzi più vicini al treno gli finivano davanti e lo coprivano.
3. Correzione: mentre esce, il cattivo resta dietro al suo nascondiglio (si vede che sbuca); appena è fuori, viene disegnato sopra a tutti gli oggetti, quindi si vede sempre e si può colpire.
4. Peso 3 nel backlog: un difetto vero, nel punto di index.html dove si disegna il paesaggio.

## v0.19 — 12/10/2026 13:02 — Il mirino rosso

1. Pull Request di Ney V. (12:59): «Cursore a forma di mirino: cambia il puntatore del mouse con la grafica di un mirino rosso, per dare subito l’idea di uno sparatutto arcade».
2. Sopra il gioco il puntatore del mouse è un mirino rosso (cerchio, punto al centro e quattro tacche); il centro del mirino è il punto dove si spara.
3. Peso 1 nel backlog: una riga di stile in index.html, il mirino è disegnato lì dentro.

## v0.18 — 12/10/2026 13:00 — BANG! e il cattivo cade a terra

1. Pull Request di Ney V. (12:57): «quando clicchi un nemico, non farlo sparire all’improvviso: scritta BANG!, flash rosso o piccola animazione di caduta».
2. Pull Request di Egor M. (12:59): «effetti sugli spari, per esempio bang o qualche altro effetto figo».
3. Pull Request di Luca B. (12:51): «sembra un gioco di paintball». Il sangue no (gioco di scuola, sito pubblico): al suo posto il cattivo cade a terra.
4. Ora quando colpisci un cattivo compare BANG!, lo schermo fa un piccolo lampo rosso, il cattivo cade a terra piano e poi sparisce; le scintille sono grigie e gialle, non più coriandoli colorati.
5. Peso 3 nel backlog: animazione e scritte in index.html.

## v0.17 — 12/10/2026 12:57 — I cattivi non nascono più troppo vicino

1. Pull Request di Luca B. (12:55), «sistemare bug»: i nemici nascono dietro o troppo vicino, non vengono contati e sparano da dove non si riesce a cliccarli.
2. Causa: i cattivi nascevano dietro oggetti già vicini al treno e potevano sparare solo quando erano quasi passati, ai bordi del finestrino.
3. Correzione: i cattivi nascono più lontano (dietro gli oggetti che stanno arrivando) e sparano al più tardi quando sono ancora ben visibili nel finestrino, dove si possono colpire.
4. Peso 3 nel backlog: un difetto vero, tre numeri in index.html. PR scritta bene, con titolo, dove e perché.

## v0.16 — 12/10/2026 12:56 — Vetro da 10 colpi

1. Pull Request PR1 di Katherine A. (12:53): «Più munizioni per il giocatore: aumentare i colpi da 5 a 10, perché 5 colpi finiscono troppo in fretta nei momenti affollati».
2. Nel gioco i «colpi» che si possono prendere sono quelli del vetro: ora il vetro regge 10 colpi (prima 5), più l’ultimo colpo della v0.14.
3. Il file regole.json accettava al massimo 9: il limite ora è 12 (anche nel controllo automatico).
4. Peso 2 nel backlog: si cambia un numero in regole.json (e il limite in index.html).

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
