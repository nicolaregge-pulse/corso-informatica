# Atlante del corso

**Versione 1.6** — 19/10/2026 · Il laboratorio di informatica secondo le idee di Nicola Regge. Area Docente.

*L'Atlante è la mappa unica del corso: che cosa c'è, dove sta, a che cosa serve, come si lavora in una giornata di lezione e quali parole dire a Claude. In cima c'è la mappa illustrata: ogni zona si clicca e porta alla pagina vera. Senza nomi di allievi.*

## 00 Come si usa

1. **È il punto da cui si parte per tutto:** le pagine del corso dalla mappa e dalle schede delle zone, i documenti del prof dalla scheda «I documenti del prof». Resta fuori solo il repository riservato (nomi, voti, presenze).
2. **Per andare in un posto:** si clicca la sua zona nella mappa, oppure il bottone nelle schede sotto la mappa. Funziona nella pagina HTML e nel PDF.
3. **Per capire come funziona una cosa:** si legge il capitolo che ne parla, qui sotto.
4. **Regola d'oro:** una cosa si scrive una volta sola, in una fonte unica, e da lì si genera ovunque serva.
5. **Prima di dire che cosa è stato fatto si guardano i dati**, mai a memoria.

## 01 Principi

1. **Qui provarci conviene e non fa male.** I ragazzi arrivano da molti «non ce l'hai fatta»: ogni pagina è costruita per farli riuscire.
2. **Autoregolazione:** ogni pagina per i ragazzi ha sempre i loro strumenti per regolarsi da soli: il monitor della lezione, il proprio andamento, i voti, il backlog. Il docente ha in più il suo cruscotto cifrato.
3. **Un solo bottone:** ogni consegna si fa con un bottone dentro la pagina, senza «copia, apri, incolla» (RIFERIMENTI §2.53, REGISTRO-ERRORI #61, #62, #68).
4. **Tre lingue** per tutto ciò che arriva ai ragazzi: italiano, arabo, cinese (in 2INF italiano e cinese).
5. **Privacy dei minori:** nomi, voti nominali e presenze mai sul pubblico. Sulle pagine pubbliche si usa «Nome I.» solo dove serve ai ragazzi per regolarsi; nei materiali per l'esterno nessun nome.
6. **Prima di proporre qualsiasi cosa ai ragazzi:** «Pubblico o vuoi vederlo prima?». Ordine fisso: teoria, compito, approvazione, pubblicazione.

## 02 I due repository e i due ambienti

1. **Due repository:**
   1. `corso-informatica` (pubblico): pagine, giochi, materiali. Il sito è pubblicato da `docs/` con GitHub Pages.
   2. `corso-informatica-riservato` (privato): nomi, voti, presenze, consegne, coda di Classroom, comandi per lo script, bobine.
2. **Due ambienti dentro il pubblico:** `main` è la cucina, dove si lavora; le **Release** (v1.0, v1.1…) sono il piatto servito, congelato per i ragazzi.
3. **I progetti di stage della 4TI** hanno un deposito ciascuno, con la chat nella Pull Request che resta aperta e l'archivio automatico in `storia/chat.md`.

## 03 La giornata di lezione

1. **Prima della lezione (Claude):** teoria e compito pronti come anteprima; il docente li guarda; si pubblica solo dopo «pubblica».
2. **Inizio:** il docente firma il programma previsto sul registro, **entro le 14:05**. Testo corto, al massimo 40 caratteri.
3. **Il compito arriva su Classroom** dallo script, con un solo link alla pagina della lezione.
4. **Durante:** il docente guarda il **monitor dal vivo** (capitolo 06): per ognuno scheda, percentuale, minuti che mancano, domande, verifica e voto, aggiornato ogni 5 secondi. Le domande dei ragazzi vanno all'assistente, che risponde nella pagina in 2-3 minuti. Il docente manda le schermate di Veyon; Claude le trascrive nel monitor pubblico dei ragazzi (solo fatti, fuori compito in rosso).
4b. **Il giro automatico** (Claude, ogni 2 minuti in lezione): legge il Foglio delle consegne, aggiorna il monitor, risponde alle domande, corregge, apre il recupero a chi è sotto 60, avvisa quando metà classe ha finito. Per la 3INF controlla anche il sito vero di ogni ragazzo e scrive a ognuno che cosa gli manca in «Il mio punto».
5. **Le proposte dei ragazzi** arrivano dal Modulo «Consegna»; Claude le mette nel backlog, le realizza nel gioco e pubblica le versioni nuove; i voti parziali si aggiornano.
6. **Fine:** argomenti realmente svolti nel registro degli argomenti; demo e prove del metodo aggiornate, senza nomi.

## 04 Le pagine di ogni classe: i sei bottoni

| Bottone | A che cosa serve | Chi lo vede |
|---|---|---|
| I voti | il proprio voto parziale e perché | tutti |
| Il backlog | la coda delle proposte, in ordine, con lo stato | tutti |
| Il monitor della lezione | che cosa c'era su ogni schermo, giro per giro | tutti |
| Cosa è cambiato oggi nel gioco | le versioni nuove nate dalle proposte | tutti |
| La classifica | chi ha portato più proposte nel gioco | tutti |
| Valutazione dei singoli | il giudizio del docente | solo il prof |

0. **Nel framework «codice in team»** (il gioco con le Pull Request) i sei bottoni ci sono sempre, aggiornati alla giornata.
1. Il docente ha in più il **cruscotto** della classe (cifrato, password dell'area docente): presenti, chi ha mandato, chi gioca ancora, una barra di avanzamento.
2. Nei voti, chi non ha ancora consegnato è **«in attesa»**, non 40.

## 05 Il gioco e le versioni

1. **Il Treno blindato** è il gioco della classe: nato in HTML in 2INF, copiato (fork) dalla 1INF e dalla 3INF, portato su Godot (versione 2.0).
2. **Ogni proposta accettata** fa nascere una versione nuova: cambio piccolo, sale il numero dopo il punto; cambio grande, sale il primo numero; correzione, sale il terzo.
3. **Il grafo delle versioni** mostra tutta la storia: rami, copie, unioni. Ogni pallino si gioca.
4. **Conflitto:** due proposte sulla stessa riga; vale chi è arrivato prima, e si spiega nel backlog.
5. **La base del prof** (`prof-nicola-regge`) è neutra; ogni classe ha il suo ramo o la sua copia.

## 06 I tre framework e il monitor dal vivo

1. **I tre framework** (MANIFESTO §9.8):
   1. **Codice in team (Agile):** il gioco della classe con Pull Request, backlog, merge, versioni, retrospettiva, e sempre i sei bottoni.
   2. **Lezione normale:** teoria → verifica → correzione → recupero → voto complessivo, in una sola pagina `verifica/?b=<lezione>`.
   3. **Questionario su Google Moduli**, allegato al compito su Classroom (traccia per la Regione).
2. **Com'è fatta una lezione tracciabile** (MANIFESTO §9.5): ripasso corto; la pratica spezzata in schede, ognuna con una domanda di controllo che dice al monitor a che punto è il ragazzo; verifica aperta dall'inizio con la scadenza all'ultima campanella; il lavoro pratico si consegna nella domanda «incolla qui» (l'unica dove si può incollare); la sfida per chi finisce prima nell'ultima scheda.
3. **Il monitor dal vivo del docente:** `avanzamento/?b=<lezione>-v1`, password dell'area docente. Legge lo script ogni 5 secondi; se lo script non risponde, ripiega sulla copia che Claude aggiorna ogni 1-2 minuti. Avvisa quando metà classe ha finito: il passo dopo deve essere già pronto.
4. **Prima di dare un link:** la prova automatica come un ragazzo (`strumenti/prova_verifica.js`) deve dire «Tutto a posto».
5. Come si rifà una verifica: `VERIFICA-COME-SI-FA.md`. Le regole fisse: `MANIFESTO.md`.

## 07 I progetti di stage della 4TI

1. Un deposito per ragazzo, il docente e Claude come collaboratori; la chat è una Pull Request che resta aperta.
2. Un passo e una domanda alla volta; prima capire, poi scrivere il codice (REGISTRO-ERRORI #65, #66).
3. Il **cruscotto dei progetti** legge GitHub dal vivo: rosso se il ragazzo aspetta una risposta. Nel cruscotto e nei file dei progetti si scrivono solo le iniziali (C.D.L., G.A.).
4. **Per chi sta fuori** c'è la pagina «Progetti della quarta», senza nomi né indirizzi: chi vuole vedere il progetto vero lo chiede al prof con un'email già scritta.

## 08 L'automazione

1. **Lo script «Consegne Classroom → Git»** (account di lavoro del docente) gira ogni 5 minuti: pubblica i compiti della coda, raccoglie le consegne, esegue i comandi del ponte.
2. **Coda** (`coda/` nel riservato): un file per compito, con stato «da-pubblicare».
3. **Ponte** (`comandi/` nel riservato): Moduli, Documenti, Drive, Fogli, letture delle risposte.
4. **Applicazione web dello script (v7.9, pubblicata il 18/10):** riceve consegne, segnali di avanzamento e domande con un clic, e risponde al monitor dal vivo con il codice `MONITOR_TOKEN` (proprietà dello script = password dell'area docente).
5. **Quando si cambia lo script:** si copia il codice dal link pubblico, si salva, poi «Esegui il deployment → Gestisci deployment → matita → Nuova versione». Da PC, 5 minuti: è l'unica cosa che fa solo il docente.

## 09 Materiali e nomi dei file

1. Albero: `classe / argomento / tipo-artefatto / NomeFile-datato-vX.Y`.
2. Sette tipi: materiale, consegne, valutazione, report, libri, presenze, lavagna. Materiale e lavagna senza nomi sono pubblici; gli altri riservati.
3. Il nome del PDF porta data, nome, area e versione, per esempio `20261013_Atlante_Docente_v1.0.pdf`.

## 10 I libri

1. **A, Manuale:** tutto, per argomento, su tre profondità (base, intermedio, avanzato).
2. **B, Libro di classe:** teoria ed esercitazioni per data, senza nomi (per la Classe 1: `libro-classe1.md`).
3. **C, Libro individuale:** il percorso del singolo ragazzo (riservato), complessivo, di oggi o della lezione.
4. **D, Libro parziale di classe:** una giornata o una lezione.
5. **Documenti del docente:** griglie, schede, valutazione complessiva della classe (riservati).

## 11 Le parole da dire a Claude

| Parola | Che cosa succede |
|---|---|
| PPP | annota e prepara in silenzio, non consegna |
| AVANTI | consegna quello che era parcheggiato |
| FIRMA | testi corti per il registro, entro le 14:05 |
| pubblica | quello che il docente ha visto va ai ragazzi |
| attiva verifica | apre la verifica della classe |
| SVOLTO | aggiorna gli argomenti realmente svolti |
| guarda | aggiorna subito il monitor leggendo il Foglio |
| CHIUDI classe | chiusura della giornata in cascata |
| VALUTAZIONE COMPLESSIVA classe | tutti i lavori fino a oggi, libri e voti |

## 12 Comunicazione e marketing

1. I materiali per chi sta fuori dall'aula: scuole e aziende, genitori, ragazzi, chi non capisce di informatica.
2. Una pagina raggiungibile solo con il link, con il racconto «Cinque giorni da azienda», la brochure, la demo e le guide.
3. Il test della mamma: un solo bottone, scritte grandi, una voce che legge.

## 13 Glossario

1. **Fork (copia):** una copia del progetto su cui lavorare senza toccare l'originale.
2. **Pull Request (proposta di modifica):** la richiesta di cambiare qualcosa; il docente dice sì o no.
3. **Merge (unione):** la proposta accettata entra nel progetto.
4. **Backlog (coda di lavoro):** l'elenco ordinato delle proposte da fare.
5. **Retrospettiva:** a fine argomento si guarda indietro: che cosa fare di più, di meno, che cosa cambiare.
6. **Cruscotto:** la pagina cifrata del docente con la situazione della classe.
7. **Fonte unica:** l'unico file dove un contenuto è scritto; il resto si genera da lì.

## 14 Registro delle versioni

1. **v1.6 (19/10/2026):** i tre framework e il monitor dal vivo (capitolo 06); il giro automatico e l'assistente nella giornata di lezione; l'applicazione web dello script v7.9; nella mappa le lezioni del 15-19/10 (assemblaggio 1INF, ciclo FOR 2INF, portfolio 3INF), il monitor dal vivo nella Sala di controllo, nuovi documenti del prof (MANIFESTO, audit del monitoraggio, regia del 19/10).
1. **v1.5 (13/10/2026):** nella zona della quarta, al posto dei link ai progetti dei ragazzi (con il loro nome nell'indirizzo), la pagina «Progetti della quarta» senza nomi; il link vero si chiede al prof.
1. **v1.4 (13/10/2026):** «I documenti del prof»: dall'Atlante si apre ogni documento del docente (modo di lavorare, guide, regole, registro degli errori, comunicazione); l'Atlante è il punto da cui si parte per tutto.
2. **v1.3 (13/10/2026):** pagina leggibile anche sul telefono; in alto il numero dell'edizione (vedi `comunicazione-marketing/EDIZIONI.md`).
2. **v1.2 (13/10/2026):** nelle zone niente nomi di prodotti di altre aziende; nasce «Il parco del corso», la versione con la sola mappa per la comunicazione.
2. **v1.1 (13/10/2026):** tolto il nome della scuola: l'Atlante porta il nome «Il laboratorio di informatica secondo le idee di Nicola Regge».
2. **v1.0 (13/10/2026):** mappa illustrata e cliccabile del corso, «come un parco»; Atlante riscritto con tutto quello che è nato dal 06/10 (giornata di lezione, i sei bottoni, gioco e versioni, verifica, progetti di stage, automazione, comunicazione); pagina HTML e PDF con i link cliccabili.
2. **v0.5 (06/10/2026):** Valutazione complessiva della classe e comando `VALUTAZIONE COMPLESSIVA classe`.
3. **v0.4 (01/10/2026):** `CHIUDI classe` con il monitoraggio.
4. **v0.3 (30/09/2026):** capitolo «se voglio X, dico Y».
5. **v0.2 (30/09/2026):** nome Atlante, due ambienti, tipi di artefatto, Manuale a due assi, comandi.
6. **v0.1 (30/09/2026):** prima stesura come «Topologia libri e metodologia».
