# Changelog — Il treno blindato su Godot (base del prof. Nicola Regge)

Ogni versione dice **cosa cambia e perché**. I numeri si leggono così: MAJOR.MINOR.PATCH
(cambio grosso . aggiunta . correzione di un errore). Ogni versione si gioca al suo link:
`https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-prof/versioni/<versione>/`
L'ultima versione è sempre a `https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-prof/`.

## v1.0 — 12/10/2026 — Il treno blindato su Godot, base del prof (MAJOR)

### 1 Il porting su Godot 4.7

1. Il gioco della classe 2INF (versione HTML **0.31**, «Gli uccelli nel cielo») è stato rifatto con il motore **Godot 4.7** ed esportato per il browser (PC e telefono).
2. Perché MAJOR: è cambiato il motore, una cosa grossa. Il numero riparte da 1.0.
3. I dati restano in file `.json` con gli stessi nomi della versione HTML, nella cartella `dati/`.

### 2 Il vetro si crepa dal bordo verso il centro (richiesta del prof)

1. Nella versione HTML la crepa partiva vicino al cattivo, spesso in mezzo al vetro, e copriva subito la vista.
2. Ora il primo colpo crepa un angolo del vetro, vicino alla cornice (con qualche scheggia saltata via); ogni colpo dopo arriva un po' più vicino al centro. Il centro resta pulito il più a lungo possibile; solo gli ultimi colpi arrivano in mezzo.
3. Le crepe sono linee bianche sottili con piccoli rami, anelli intorno al punto colpito e il foro al centro; le crepe che andrebbero verso il centro sono più corte.
4. Il numero di colpi è sempre quello di `dati/regole.json` (10), più l'ultimo colpo della v0.14.

### 3 Base neutra per tutte le classi (richiesta del prof)

1. Nome: «Il treno blindato — base del prof. Nicola Regge»; in basso a destra: «versione 1.0 · base del prof · su Godot».
2. Le funzioni «Facce della classe» e «I personaggi» funzionano, ma le liste della base sono vuote (`dati/facce.json`, `dati/img/personaggi/personaggi.json`): ogni classe aggiunge le sue.
3. Cattivi disegnati (bandito con la maschera, tuta mimetica); i cattivi della classe arrivano con i file `dati/cattivi/pcNN.json`.
4. La copertina della 2INF non c'è: dietro al titolo corre il treno. Una classe può mettere la sua `dati/img/copertina.jpg`.
5. «Chi l'ha fatto» racconta da dove viene la base (gioco della 2INF, versione 0.31) senza nomi di studenti; i campi «autori» dei dati sono vuoti.

### 4 Cosa è stato portato dalla versione HTML 0.31

1. La cabina che guarda avanti lungo i binari, in prospettiva; cinque ambienti (Bosco bruciato con i rottami fumanti, Paese, Città, Montagna, Mare) con i colori serali della v0.12; colline, traversine, binari gialli (v0.27).
2. I cattivi interi in mimetica che sbucano dal nascondiglio (alberi, case, palazzi, rocce, barili) con il «!» rosso, la barretta del tempo gialla e poi rossa, l'arma puntata verso il treno; il fucile d'assalto per le facce con `"ak"` in `facce.json` (v0.7, v0.8, v0.9).
3. I cattivi nascono lontano (v0.17) e, appena usciti, si disegnano sopra a tutti gli oggetti (v0.20); le luci dei palazzi non lampeggiano (v0.21).
4. Si spara toccando o cliccando la testa o il corpo; mirino rosso del mouse (v0.19); BANG!, lampo rosso, il cattivo cade a terra e sparisce, scintille grigie e gialle (v0.18).
5. Punti: 100 per cattivo +50% a ogni livello (v0.24), bonus combo, COLPO PRECISO +50 sulla testa (v0.25), sfera d'oro rara che dà punti x2 per 10 secondi (v0.30).
6. Il vetro regge 10 colpi (v0.16) più l'ultimo colpo con la scritta «VETRO ROTTO! ULTIMO COLPO!» (v0.14); scossone, crepe, vetro che va in pezzi.
7. Livelli: ogni 10 cattivi si sale di livello e cambia scenario (v0.13), la difficoltà cresce (v0.15), dal livello 4 arrivano anche due cattivi insieme; barra «prossimo livello» in alto (v0.28).
8. Meteo: dal livello 2 cielo grigio, dal 3 pioggia, dal 4 nebbia (v0.26); uccelli che passano nel cielo e si fermano in pausa (v0.31).
9. Cruscotto: tachimetro in km/h, quadrante del vetro, il macchinista; in alto Punti, Record (v0.22), ambiente, livello e km; quadratini del vetro.
10. Pausa: bottone blu in alto a destra, tasti P ed Esc, scritta PAUSA (v0.23).
11. Schermate: inizio (PARTI!, Chi l'ha fatto, I personaggi, Facce della classe, il tuo record, migliori punteggi, cattivi della classe, controllo dei file, link «Tutte le versioni del gioco»); fine partita con punti, NUOVO RECORD, lodi, statistiche (cattivi colpiti, colpi a vuoto, precisione, v0.29), soprannome e migliori punteggi salvati subito (v0.10, v0.11), RIPARTI e Menu.
12. Suoni costruiti con la matematica come nell'HTML: colpo, pop, sparo, crepa, vetro rotto, fischio del treno, sferragliare, note della vittoria da `suoni.json`.
13. Controllo dei file: un file scritto male non blocca il gioco e viene segnalato nella schermata iniziale (anche la virgola in più prima di `}`).

### 5 Piccoli miglioramenti per il telefono

1. Telefono in verticale: la grandezza delle cose segue anche l'altezza del vetro, così i cattivi non sono minuscoli; la riga «ambiente · livello · km» va sotto la barra del livello.
2. Il tocco ha almeno 22 punti di tolleranza intorno alla testa (il dito è meno preciso del mouse).
3. Le scritte grandi si rimpiccioliscono se non stanno nello schermo.
4. Le schermate lunghe si scorrono con il dito.
5. Il sottotitolo dice il numero vero di colpi del vetro (`{vetro}` in `testi.json`): nell'HTML diceva ancora 5.

### 6 Cosa NON è uguale alla versione HTML, e perché

1. Il bottone «Installa il gioco» e il gioco senza rete (service worker) non ci sono: l'esportazione Web di Godot è fatta senza «app installabile», come il treno Godot della 1INF.
2. I dati sono dentro il pacchetto del gioco (`index.pck`): dopo aver cambiato un file in `dati/` bisogna esportare di nuovo. Nell'HTML il browser leggeva i file a ogni avvio (anche `record-classe.json`).
3. Il carattere è quello di Godot (Open Sans) e non quello del sistema; la freccia «→» dei crediti è «›», perché nel carattere di Godot la freccia non c'è.
4. I suoni sono calcolati all'avvio con la stessa ricetta: il timbro è molto simile ma non identico; i suoni casuali (crepa, vetro rotto) hanno 2-3 varianti fisse.
5. «Facce della classe» nel browser usa la finestra dei file del browser (come l'HTML); sul PC, dentro Godot, usa la finestra «Apri» di Godot e salva le foto nella cartella dell'utente.
6. Godot nel browser pesa di più della pagina HTML (il motore è un file di 39 MB, che si scarica la prima volta) e chiede più lavoro alla scheda grafica: su computer molto vecchi può essere meno fluido.
