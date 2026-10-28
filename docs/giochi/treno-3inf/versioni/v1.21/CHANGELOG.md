# Il treno blindato della 3INF — storia delle versioni


















## v1.21 — 14/10/2026 13:05 — Più nuvole in montagna (sprint 3)

1. PR1 di Denis A. (Titolo: Nuvole; Cosa cambia: più nuvole; Dove: livello montagna; Perché: così è più bello): fatto, in montagna le nuvole sono 12 invece di 6. Nel motore è nata la regola «nuvole». Una richiesta scritta bene, con le 4 parti.

## v1.20 — 14/10/2026 13:05 — Case chiare, tetti scuri (sprint 3)

1. PR1 di Ariel D.: «nel paese case con toni chiari e tetti con toni scuri, per dare più varietà». Fatto: case color crema, tetti marrone scuro e grigio antracite. Nel motore è nata la regola «tetti».

## v1.19 — 14/10/2026 13:05 — Il primo livello più facile (sprint 3)

1. PR3 di Ariel D.: «nel primo livello i nemici sono lenti e facili da colpire». Fatto: i nemici aspettano 4 secondi prima di sparare (prima 3); a ogni livello aspettano un po' meno, quindi il gioco resta difficile più avanti.

## v1.18 — 14/10/2026 13:01 — Il cielo lo scegli tu (sprint 2)

1. PR di Kelvin P.: «sarebbe bello avere la possibilità di cambiare il colore del cielo come vuole il giocatore». Fatto: in basso a sinistra c'è «Cielo» con una tavolozza di colori; il bottone «come prima» rimette il cielo dell'ambiente.

## v1.17 — 14/10/2026 13:01 — Il cielo nuvoloso nel bosco (sprint 2)

1. PR di Samuele U.: «metti il cielo nuvoloso e abbassa la velocità; aumenta la potenza delle armi». Fatto il cielo nuvoloso nel bosco (grigio chiaro). La velocità è già bassa dalla v1.12. Le armi più potenti sono una regola nuova: restano nel backlog per il prossimo sprint.

## v1.16 — 14/10/2026 13:01 — Le montagne viola (sprint 2)

1. PR di Dani S.: «metti le montagne di colore viola». Fatto: in montagna le montagne lontane sono viola. Il resto della sua richiesta (35 km/h e cavalli che corrono) resta nel backlog: la velocità è già 30 km/h dalla v1.12, i cavalli vanno disegnati (peso 5).

## v1.15 — 14/10/2026 12:43 — L'alieno verde più veloce (sprint 1)

1. Revisione di Simone G.: «la v1.8 con l'alieno è giusta, ma vorrei che andasse più veloce». Fatto: l'Alieno verde ha la velocità massima (3).

## v1.14 — 14/10/2026 12:43 — Colori più vivi (sprint 1)

1. PR1 di Simone G.: «aumenta la saturazione di 100 in tutto il gioco, così è più come un gioco vero». Fatto: saturazione al 200% (cioè +100%) su tutto il gioco. Nel motore è nata la regola «saturazione».

## v1.13 — 14/10/2026 12:43 — Niente case e rocce sui binari (sprint 1)

1. Revisione di Noah V.: «alcune case e rocce occupano il binario». Era un difetto (bug): gli oggetti grandi, come le rocce più grosse, finivano sopra i binari. Sistemato: ogni oggetto sta sempre a lato dei binari. Noah ha anche scritto che il treno partiva a 80 km/h: dalla v1.12 parte a 30 km/h.

## v1.12 — 14/10/2026 12:39 — Si parte a 30 km/h (sprint 1)

1. Revisione di Alessandro A.: «il treno è troppo veloce: dovrebbe partire a 30 km/h e salire di 3 km/h a ogni livello». Fatto: velocità 0,5 (sul tachimetro 30 km/h) e a ogni livello il 10% in più, cioè 3 km/h. È nata dalla revisione: anche una revisione può diventare una Pull Request.

## v1.11 — 14/10/2026 12:37 — Il treno rallentato

1. Richiesta del prof: il gioco era troppo veloce. Velocità di partenza 0,6 (prima 1,2) e a ogni livello solo il 6% in più (prima il 15%). La regola di Noah (lento all'inizio, poi più veloce) resta, ma più dolce.

## v1.10 — 14/10/2026 11:33 — Arriva Tuta

1. PR di Tomas (12/10), PERSONAGGI: il nuovo nemico Tuta, con la tuta arancione, esce a metà percorso da dietro palazzi e tombini. I gatti della stessa richiesta non ci sono ancora: il motore non sa disegnare animali che si muovono, restano nel backlog per una prossima versione.

## v1.9 — 14/10/2026 11:33 — Paesaggio meno vuoto

1. PR di David A. (12/10), SCENARI: «il paesaggio è troppo vuoto e spoglio». In montagna ora ci sono più rocce, cespugli e greggi intorno ai binari (densità 3, il massimo).

## v1.8 — 14/10/2026 11:33 — Arrivano gli alieni verdi

1. PR di Ariel (12/10), PERSONAGGI: tra i nemici compare l'Alieno verde, tutto verde, con tre occhi; quando spara dice «BLIP BLOP!».

## v1.7 — 14/10/2026 11:33 — Rocce di grandezze e colori diversi

1. PR di Ariel (12/10), SCENARI: le rocce ai lati dei binari hanno grandezze e toni di colore diversi, non sono più tutte uguali. Nel motore è nata la regola «rocce_varie».

## v1.6 — 14/10/2026 11:33 — Cielo grigio in città

1. PR1 di Andrea G. (12/10): il cielo diventa grigio, «così il gioco sembra più un gioco d'azione». MERGE CON UN CONFLITTO: in montagna Dani e Ale (v1.2) avevano chiesto il cielo sereno. Per non cancellare il loro lavoro, il cielo grigio va in città: aggiungere sì, cancellare no.

## v1.5 — 14/10/2026 11:33 — Treno più lento all'inizio, poi sempre più veloce

1. PR1 di Noah (12/10), MOTORE FISICA: il treno parte più lento (velocità 1,2 invece di 2) e a ogni livello va il 15% più veloce, così il gioco diventa più difficile man mano. Nel motore è nata una regola nuova: «aumento_per_livello».

## v1.4 — 08/10/2026 12:55 — Treno più veloce, Nash, Dylan, il cielo che cambia subito

1. PR #17 di Noah (PC 35), MOTORE FISICA: velocità del treno 2, «più intenso e più difficile».
2. PR #15 di Ariel D. (PC 13), PERSONAGGI: Nash ha la giacca blu e nera e quando vince dice «Bella partita… ma il migliore resta uno solo».
3. PR #19 di Emmanuel (PC 22), TEST QUALITÀ: il cattivo Dylan, mimetica grigio scuro, esce da dietro un vagone blindato e grida «GAAA!!».
4. PR #18 di Eric (PC 23): Franciscos ha la mimetica azzurra e bianca.
5. DIFETTO trovato da Dani (PR #20) e Ale (PR #21), SCENARI: al livello 2 il cielo cambiava in ritardo. Sistemato: quando sali di livello cambia subito anche l'ambiente.

## v1.3 — 08/10/2026 12:42 — Cespugli, greggi, armi diverse, nuovi cattivi

1. PR #8 di Mirko (PC 16), SCENARI: cespugli vicino ai binari da cui escono i banditi, con armi diverse (fucile d'assalto, revolver, pistola).
2. PR #13 di Dani (PC 18) e #14 di Ale (PC 17), SCENARI: in montagna greggi di mucche e pecore che pascolano senza intralciare la strada.
3. PR #10 di Ariel D. (PC 13) e #11 di Tomas (PC 15), PERSONAGGI: Travor esce da palazzi, tombini e cespugli e dice «Tutto qui quello che sai fare?»; il protagonista si chiama Nash.
4. PR #12 di Eric (PC 23), TEST QUALITÀ: il cattivo Franciscos, mimetica azzurra, esce da un cespuglio con il revolver e grida «ARGENTINAA!».

## v1.2 — 08/10/2026 12:30 — Montagna, tempo che peggiora, Travor

1. PR #4 di Dani (PC 18) e PR #5 di Ale (PC 17), SCENARI: il viaggio parte dalla strada che percorre la montagna, cielo sereno; a ogni livello il tempo cambia e diventa più difficile giocare (livello 2 foschia, livello 3 pioggia, livello 4 pioggia e nebbia). Le curve della strada: in arrivo.
2. PR #6 di Tomas (PC 15), PERSONAGGI: il cattivo «Travor» con la mimetica grigio scuro (manca ancora la frase).
3. Nuova mimetica «grigia».

## v1.1 — 08/10/2026 12:24 — Black Panter (Pull Request #1 e #2, squadra SCENARI)

1. PR #1 di Dani (PC 18) e PR #2 di Ale (PC 17), consegnate su Classroom: il cattivo «Black Panter», mimetica nera con i dettagli argento, esce da dietro una porta e quando spara dice «Yahuu!».
2. Il motore ora sa fare mimetiche di colori diversi: nuova mimetica «nera» con macchie argento.

## v1.0 — 08/10/2026 12:10 — Il fork della 3INF

1. La 3INF fa la SUA copia (fork) del gioco della 2INF, versione 0.11.
2. Traversine di legno vero: colore sfumato, venature e nodi del legno, ombra sotto (indicazione del prof).
3. Nuvole che scorrono nel cielo (indicazione del prof).
4. Da qui in avanti: le Pull Request consegnate su Classroom dalla 3INF.
