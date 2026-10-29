# Verifica sul versioning

**Versione 1.0** — 29/10/2026
*Libro parziale della 2INF: la lezione del 13/10/2026. Fa parte del libro di testo della classe (libro-classe2). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 13/10/2026, Laboratorio.
2. **Argomenti:** Ripasso e verifica sul versioning; revisione delle versioni del treno.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Le versioni

<div class="scheda">Una <b>versione</b> è un salvataggio del programma con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Se cambia il numero dopo il punto (v0.30 → v0.31) è un passo piccolo, <b>minor</b>. Se cambia il primo numero (v1.4 → v2.0) è un cambio grande, <b>major</b>: per esempio un motore nuovo, come Godot. Il <b>changelog</b> è il registro di tutte le modifiche, versione per versione.</div>

#### 2. Git e GitHub

<div class="scheda"><b>Git</b> è il programma che tiene tutte le versioni di un progetto. Ogni salvataggio si chiama <b>commit</b>. Il <b>repository</b> è la cartella del progetto con tutta la sua storia. <b>GitHub</b> è il sito che tiene i repository su Internet e li mostra a tutti: è lì che sta il nostro treno. Un <b>ramo</b> (branch) è una strada parallela di lavoro; un <b>fork</b> è una copia del progetto (la 3INF ha fatto il fork del nostro treno); il <b>merge</b> unisce un ramo dentro un altro.</div>

#### 3. La Pull Request e il backlog

<div class="scheda">Una <b>Pull Request</b> (PR) è una <b>richiesta di modifica scritta</b>: Titolo, Cosa cambia, Dove, Perché. Tutte le richieste vanno nel <b>backlog</b>, la coda dei lavori. Ognuna vale uno, chiunque la faccia; il <b>peso</b> dice quanto lavoro serve sul codice (1 colore, 2 numero, 3 personaggio, 5 ambiente, 8 regola nuova). Si fanno prima le più leggere; a parità di peso, chi è arrivato prima. È il metodo <b>Agile</b>: piccoli passi, sbagliare presto e correggere presto.</div>

#### 4. Il nostro sistema, pezzo per pezzo

<div class="scheda">1) Su <b>Google Classroom</b> c'è un solo compito con un link fisso. 2) La PR la mandi dal <b>Modulo «Consegna»</b> (Google Moduli). 3) Uno <b>script</b> (un piccolo programma di Google, Apps Script) ogni minuto porta le consegne nel <b>repository</b> del corso su <b>GitHub</b>. 4) <b>Claude</b>, l'intelligenza artificiale che lavora con il prof, legge la PR, le dà un peso nel backlog, <b>scrive il codice</b> della modifica, la prova nel browser e pubblica la versione nuova. 5) <b>GitHub Pages</b> mette il gioco e le pagine (backlog, voti, monitor, novità) sul sito, e si aggiornano da sole. 6) Il prof decide: sì o no alla PR, e il voto.</div>

#### 5. Chi fa cosa

<div class="scheda"><b>Tu</b> hai l'idea e la scrivi bene. <b>Il prof</b> decide cosa entra e dà il voto. <b>Claude</b> scrive il codice e lo prova. <b>GitHub</b> tiene tutte le versioni, così se una modifica rompe il gioco si torna indietro. Da oggi il treno passa su <b>Godot</b>: è un cambio major, e ogni classe avrà il suo <b>ramo</b> che parte dalla base del prof.</div>


| Versione | Cosa è entrato | Cosa funziona | Cosa si può migliorare |
|---|---|---|---|
| v0.12 | La versione serale | Con una sola idea il gioco cambia atmosfera: il tramonto lo rende più bello da guardare. | Al tramonto i cattivi scuri si staccano meno dallo sfondo: vanno provati con colori più chiari. |
| v0.13 | Nuovo livello, nuovo scenario | Ogni livello è un posto nuovo: chi gioca sente che sta andando avanti. | Il cambio di scenario arriva di colpo: una scritta o un attimo di pausa lo annuncerebbe meglio. |
| v0.14 | Ultimo colpo | L'ultimo colpo dà ancora una possibilità e crea tensione. | Con il vetro tutto crepato l'ultimo colpo si gioca quasi alla cieca: per questo nella base del prof le crepe partono dai bordi. |
| v0.15 | La difficoltà cresce a ogni livello | Il gioco resta interessante anche per chi è bravo. | Nessuno ha ancora misurato quanto diventa difficile dopo il livello 5: serve un collaudo. |
| v0.16 | Vetro da 10 colpi | Partite più lunghe e meno frustrazione per chi comincia. | Con 10 colpi i primi livelli diventano facili: la difficoltà va bilanciata insieme al vetro. |
| v0.17 | I cattivi non nascono più troppo vicino | Difetto vero, trovato giocando: è il lavoro di chi fa il collaudo. | Ora i cattivi sono più lontani: sul telefono vanno controllati, potrebbero essere piccoli da toccare. |
| v0.18 | BANG! e il cattivo cade a terra | Il colpo si sente e si vede: soddisfazione immediata. | Tre richieste sulla stessa cosa: prima di mandarla, conviene guardare il backlog e unirsi a quella che c'è già. |
| v0.19 | Il mirino rosso | Il mirino rosso rende la mira più precisa e il gioco più «da gioco». | Sul telefono il mirino non c'è, perché si tocca con il dito: l'idea vale solo per il PC. |
| v0.20 | I cattivi si vedono sempre | Corregge un difetto che rovinava la partita. | Il difetto era nato da una versione precedente: ogni modifica va provata giocando prima di pubblicarla. |
| v0.21 | Le luci dei palazzi non lampeggiano più | Tolto un lampeggio fastidioso, che può anche dare fastidio agli occhi. | Con le luci ferme il paese sembra meno vivo: si potrebbero accendere piano piano. |
| v0.22 | Il record accanto ai punti | La sfida continua contro se stessi: il record è sempre lì accanto ai punti. | Il record resta solo su quel computer: su un altro PC si riparte da zero. |
| v0.23 | Il bottone Pausa | Indispensabile in classe: si può fermare la partita (anche con il tasto P o Esc) e riprenderla. | Il bottone è piccolo: sul telefono va provato che si tocchi bene. |
| v0.24 | Più avanti, più punti | Premia chi resiste di più: andare avanti conviene. | I punti crescono in fretta: i record dei primi giorni diventano impossibili da battere? |
| v0.25 | Colpo preciso | Premia la precisione, non solo la velocità. | Non si capisce subito quando un colpo è «preciso»: serve una scritta che lo dica. |
| v0.26 | Pioggia e nebbia | Quattro richieste sulla stessa idea diventano una versione sola: lavoro di squadra vero. | Con pioggia e nebbia si vede poco: va bene per i livelli alti, ma all'inizio potrebbe scoraggiare. |
| v0.27 | Binari gialli | I binari gialli si vedono meglio: modifica piccola, effetto grande. | Il giallo non c'entra molto con il bosco bruciato: un colore più scuro potrebbe stare meglio. |
| v0.28 | La barra del prossimo livello | Si vede quanto manca al prossimo livello: dà un obiettivo vicino. | La barra è in alto al centro, vicino ad altre scritte: va controllato che non copra i cattivi. |
| v0.29 | Le statistiche a fine partita | A fine partita si vede cosa si è fatto bene: precisione e colpi sbagliati. | Le statistiche spariscono con la partita dopo: si potrebbero tenere le migliori. |
| v0.30 | La sfera d'oro: punti x2 | La sfera d'oro dà un momento di sorpresa e cambia il ritmo. | Quando si colpisce la sfera, non si vede bene quanto resta dei 10 secondi: serve un contatore. |
| v0.31 | Gli uccelli nel cielo | Gli uccelli rendono il cielo vivo: un dettaglio che fa sembrare il mondo vero. | Gli uccelli possono distrarre: non devono sembrare cattivi da colpire. |

#### Domande per l'analisi in classe

1. Quale versione ha migliorato di più il gioco? Perché?
2. Quale miglioramento proposto qui sopra faresti per primo? Scrivilo come Pull Request: Titolo, Cosa cambia, Dove, Perché.
3. Trovi un difetto che qui non c'è? Provalo giocando e scrivilo come Pull Request.

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
