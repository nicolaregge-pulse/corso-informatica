# Atlante del corso

**Versione 1.1** — 13/10/2026 · Il laboratorio di informatica secondo le idee di Nicola Regge. Area Docente.

*L'Atlante è la mappa unica del corso: che cosa c'è, dove sta, a che cosa serve, come si lavora in una giornata di lezione e quali parole dire a Claude. In cima c'è la mappa illustrata: ogni zona si clicca e porta alla pagina vera. Senza nomi di allievi.*

## 00 Come si usa

1. **Per andare in un posto:** si clicca la sua zona nella mappa, oppure il bottone nelle schede sotto la mappa. Funziona nella pagina HTML e nel PDF.
2. **Per capire come funziona una cosa:** si legge il capitolo che ne parla, qui sotto.
3. **Regola d'oro:** una cosa si scrive una volta sola, in una fonte unica, e da lì si genera ovunque serva.
4. **Prima di dire che cosa è stato fatto si guardano i dati**, mai a memoria.

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
4. **Durante:** il docente manda le schermate di Veyon; Claude le trascrive nel monitor pubblico (solo fatti, fuori compito in rosso) e aggiorna il cruscotto.
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

1. Il docente ha in più il **cruscotto** della classe (cifrato, password dell'area docente): presenti, chi ha mandato, chi gioca ancora, una barra di avanzamento.
2. Nei voti, chi non ha ancora consegnato è **«in attesa»**, non 40.

## 05 Il gioco e le versioni

1. **Il Treno blindato** è il gioco della classe: nato in HTML in 2INF, copiato (fork) dalla 1INF e dalla 3INF, portato su Godot (versione 2.0).
2. **Ogni proposta accettata** fa nascere una versione nuova: cambio piccolo, sale il numero dopo il punto; cambio grande, sale il primo numero; correzione, sale il terzo.
3. **Il grafo delle versioni** mostra tutta la storia: rami, copie, unioni. Ogni pallino si gioca.
4. **Conflitto:** due proposte sulla stessa riga; vale chi è arrivato prima, e si spiega nel backlog.
5. **La base del prof** (`prof-nicola-regge`) è neutra; ogni classe ha il suo ramo o la sua copia.

## 06 Ripasso, verifica, recupero

1. Un solo motore per tutte le classi: ripasso con risposta subito, verifica che si apre quando più di metà ha finito il ripasso, recupero fatto sui propri errori.
2. Come si rifà: `VERIFICA-COME-SI-FA.md`.

## 07 I progetti di stage della 4TI

1. Un deposito per ragazzo, il docente e Claude come collaboratori; la chat è una Pull Request che resta aperta.
2. Un passo e una domanda alla volta; prima capire, poi scrivere il codice (REGISTRO-ERRORI #65, #66).
3. Il **cruscotto dei progetti** legge GitHub dal vivo: rosso se il ragazzo aspetta una risposta.

## 08 L'automazione

1. **Lo script «Consegne Classroom → Git»** (account di lavoro del docente) gira ogni 5 minuti: pubblica i compiti della coda, raccoglie le consegne, esegue i comandi del ponte.
2. **Coda** (`coda/` nel riservato): un file per compito, con stato «da-pubblicare».
3. **Ponte** (`comandi/` nel riservato): Moduli, Documenti, Drive, Fogli, letture delle risposte.
4. **Da attivare:** l'applicazione web dello script (13 passi una tantum) per la consegna con un clic e la casella «Chiedi aiuto all'assistente del Prof Regge».

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

1. **v1.1 (13/10/2026):** tolto il nome della scuola: l'Atlante porta il nome «Il laboratorio di informatica secondo le idee di Nicola Regge».
2. **v1.0 (13/10/2026):** mappa illustrata e cliccabile del corso, «come un parco»; Atlante riscritto con tutto quello che è nato dal 06/10 (giornata di lezione, i sei bottoni, gioco e versioni, verifica, progetti di stage, automazione, comunicazione); pagina HTML e PDF con i link cliccabili.
2. **v0.5 (06/10/2026):** Valutazione complessiva della classe e comando `VALUTAZIONE COMPLESSIVA classe`.
3. **v0.4 (01/10/2026):** `CHIUDI classe` con il monitoraggio.
4. **v0.3 (30/09/2026):** capitolo «se voglio X, dico Y».
5. **v0.2 (30/09/2026):** nome Atlante, due ambienti, tipi di artefatto, Manuale a due assi, comandi.
6. **v0.1 (30/09/2026):** prima stesura come «Topologia libri e metodologia».
