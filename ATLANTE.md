# Atlante del corso

**Versione 0.5** — 06/10/2026 · Corso Informatica (Piamarta)

*L'Atlante è la mappa unica del corso: come sono fatti i libri, come sono
organizzati i dati su Git, come cresce l'informazione senza rifare il lavoro, e
i comandi per generare la documentazione durante o a fine lezione. Documento del
docente, senza nomi di allievi. Sostituisce e amplia il vecchio "Topologia libri
e metodologia".*

---

## 00 Cos'è e come si usa

1. Se ci si chiede "che libri abbiamo, come si chiamano, dove stanno i dati, come
   aggiorno senza perdere tempo, e quale comando dico a Claude", la risposta è qui.
2. Regola d'oro: **una cosa si scrive una volta sola** (in una fonte unica) e da lì
   si **genera** ovunque serva.
3. **Prima di dire cosa è stato fatto, si legge la base dati** (`stato-dati`): mai
   a memoria. È la cura degli errori.

## 01 Principi

1. **Git è archivio e struttura**, non ripostiglio: fonti, generatori, indici,
   registro in una struttura logica riusabile.
2. **Fonti uniche + generazione**: i contenuti stanno in un posto; i documenti si
   costruiscono da lì.
3. **Le fonti si versionano, gli output si rigenerano**: su Git le sorgenti; i
   PDF/ZIP pesanti si ricreano e non si versionano.
4. **Nomi che spiegano la struttura** (regola 2.13, vedi 04).
5. **Privacy dei minori**: nomi e voti nominali mai sul pubblico.

## 02 I due repository e i due ambienti

1. **Due REPOSITORY** (chi può vedere):
   1. `corso-informatica` (pubblico, ex `corso-godot`, coi giochi Godot) — condivisibile.
   2. `corso-informatica-riservato` (privato) — nomi, voti, presenze, anti-plagio, personale.
2. **Due AMBIENTI** (quanto è pronto), dentro il pubblico:
   1. `main` = la cucina: si lavora e si migliora, sempre in evoluzione.
   2. **Release** (`v1.0`, `v1.1`…) = il piatto servito: versione congelata per i
      ragazzi, non cambia sotto i loro piedi. La crescita entra nella versione dopo.

## 03 Topologia dei materiali (per data)

1. **Assi dell'albero:** `classe / argomento-compito(slug) / tipo-artefatto / NomeFile-datato-vX.Y`.
2. **7 tipi-artefatto** (vocabolario chiuso):
   1. `materiale` — teoria, dispensa, testo del compito, giochi (pubblico).
   2. `consegne` — i lavori grezzi dei ragazzi (riservato).
   3. `valutazione` — griglie, schede, voti (riservato).
   4. `report` — report complessivo a 4 parti (riservato).
   5. `libri` — libri individuali (riservato).
   6. `presenze` — registri presenze (riservato).
   7. `lavagna` — foto della lavagna (di norma pubblico; riservato se si legge un nome).
3. **La visibilità è conseguenza del tipo:** `materiale` e `lavagna`-senza-nomi →
   pubblico; tutti gli altri → privato. Non si decide a mano ogni volta.
4. **Lo slug del compito** (`css-separato`, `git-ai`, `configura-pc`) è la **chiave**
   che lega materiale ↔ consegne ↔ valutazione ↔ report ↔ libri dello stesso compito.

## 04 I nomi spiegano la struttura (regola 2.13)

1. Il **percorso delle cartelle è scritto nel nome**, con `__` (doppio underscore) al
   posto di `/`. Dal nome si ricostruisce l'albero; dove sta il file ne giustifica il nome.
2. Esempi:
   1. `classe-3__css-separato__report__20260930_Report-Complessivo_v1.0.pdf`
   2. `classe-4__git-ai__libri__20260929_Libro-Individuale_Cutaia-Giuseppe_v1.0.pdf`
3. Dentro il `NomeFile` il singolo `_` separa i campi (data, descrizione, versione);
   `__` solo per le cartelle. Strumento: `strumenti/nome-albero.py` (espandi/collassa).
4. Effetto anti-errore: un file `classe-4__git-ai__valutazione__…` urla dove appartiene.

## 05 Il Manuale (libro totale): due assi a tre livelli

1. **Asse ARGOMENTI** (il *cosa*): `argomento / sottoargomento / paragrafo` (albero a 3 livelli).
2. **Asse PROFONDITÀ** (il *quanto*): `Base / Intermedio / Avanzato` (3 livelli).
3. **I 3 livelli di profondità stanno nello STESSO file** del paragrafo (vicini), così
   leggere un argomento è facile e non si salta da un posto all'altro.
4. **Fonte unica del Manuale:** `manuale/<argomento>/<sottoargomento>/<paragrafo>.md`,
   con dentro `## Base`, `## Intermedio`, `## Avanzato`.
5. **Generazione:** si percorre l'albero (indice arg→sottoarg→par) e, per ogni paragrafo,
   si impaginano le 3 profondità in box colorati (base=verde, interm=blu, avanz=viola).

## 06 Accrescimento e aggiornamento (il punto difficile)

1. **Separare CONTENUTO da DOVE-APPARE.** Il contenuto vive una volta sola nella fonte
   del Manuale (per argomento); i libri per data lo **richiamano per chiave** (`git/repository`).
2. **Il totale cresce sempre;** il libro di una classe cresce **solo quando quella
   classe fa l'argomento** — ma sempre col testo migliore, perché è la stessa fonte.
3. **Due modi in cui un libro di classe cresce:**
   1. **Nuovo argomento**: la classe fa qualcosa di nuovo → entra come *core*.
   2. **Aggiornamento**: la fonte di un argomento già presente migliora → nasce un
      **aggiornamento** che propaga (nuova versione del libro).
4. **Matrice di copertura** (dentro `stato-dati`): *paragrafo × classe → fatto? quando?
   con quale versione*. Decide, in ogni libro di classe, cosa è **core** (fatto da quella
   classe) e cosa **approfondimento** (fatto meglio altrove, in un riquadro distinto).
5. **Esempio:** spiego `case` oggi in Classe 3 → lo scrivo una volta nella fonte →
   il **Manuale cresce**; **Classe 3** lo mostra come core (con la data di oggi);
   **Classe 1** (non l'ha fatto) NON riscrive la sua storia: `case` compare da loro solo
   come *approfondimento*, o niente, finché non lo fanno.
6. **Sicurezza:** Manuale versionato (bump + changelog a ogni aggiunta); le copie
   **congelate** (Release) non cambiano: la crescita entra nella versione successiva.

## 07 Le foto della lavagna

1. Sono il tipo `lavagna`: **per classe e per giorno** (la data sta nel nome).
2. **Fissano argomenti e tempi:** vanno **in cima** a ogni sezione-lezione dei libri
   per data (classe e individuale); l'allievo vede subito *cosa* e *quando*.
3. **Le mette Nicola** (Claude non vede le foto): tu carichi il file col nome-albero,
   Claude lo impagina nei libri.
4. Nel Manuale (per argomento) non entrano: lì conta l'argomento, non il giorno.

## 08 I tipi di libro

1. **A — Manuale / libro totale**: **tutto**, diviso su **3 livelli d'albero** (argomento /
   sottoargomento / paragrafo) **× 3 profondità** (Base / Intermedio / Avanzato). Uno solo,
   per argomento, cresce sempre (vedi 05).
2. **B — Libro di classe** (senza nomi, **per data**): tutta la teoria e l'esercitazione,
   lezione per lezione, di quella classe. È il libro di testo comune della classe.
3. **C — Libro individuale** (riservato): il percorso personale dell'allievo — teoria +
   esercizi realmente fatti + valutazione + riflessione + foto lavagna. Ha **tre tagli**
   per ampiezza:
   1. **C complessivo** — *tutte* le lezioni e *tutti* gli esercizi dell'allievo (tutto
      l'anno); cresce a ogni lezione. È il suo libro di testo personale.
   2. **C di oggi** (giornata) — tutta la teoria e *tutti* gli esercizi **di oggi** (una
      giornata, anche più esercizi).
   3. **C di lezione** — *solo* la teoria e l'esercitazione **in oggetto** (un singolo
      esercizio); lo "sfilato" da dare subito a fine ora.
4. **D — Libro parziale di classe** (senza nomi): una giornata o una lezione del Tipo B.

## 08b Documenti del docente (valutazione)

> Riservati (nomi + voti) → PDF, mai sul Git pubblico.

1. **Griglia completa** (per compito): tutte le note del lavoro + cosa NON ha fatto in
   **neretto** + voto. Il dettaglio di quel singolo compito.
2. **Scheda complessiva del lavoro** (per compito; detta anche *report complessivo*): il
   documento unico che raccoglie **tutto** su quel compito — tutte le **indicazioni date al
   ragazzo** (il suo lavoro + la sua valutazione), **più** le note **per il docente**
   (impressioni), la **nota anti-plagio**, le **problematiche**, e le **cose non fatte / non
   capite** (le indicazioni dei ragazzi, analizzate).
3. **Scheda incrementale insegnante** (per classe, **cumulativa**): **tutte le lezioni ×
   tutti i voti** della classe (righe = allievi, colonne = lezioni/compiti), che si accumula
   nel tempo, con **qualche nota di alta visibilità** — i pochi segnali importanti da vedere
   subito (chi recuperare, anti-plagio, assenze che pesano) — **e le cose poco chiare o non
   capite** (accumulate dalle riflessioni dei ragazzi), così il docente vede a colpo d'occhio,
   a livello di classe, cosa resta da chiarire. È il "quadro d'insieme" del docente.
4. **Scheda complessiva per giornata**: l'**insieme delle schede complessive del lavoro**
   (punto 2) di **tutti** i compiti svolti quel giorno — il riepilogo completo della giornata
   per il docente (se il giorno ha un solo compito, coincide con la sua scheda del lavoro).
5. **Valutazione complessiva della classe** (per classe, a una data; nome deciso da Nicola il
   06/10/2026): il punto su **tutti i lavori fatti fino a quel giorno**, con la **lista standard
   valutazioni per il docente** (RIFERIMENTI §2.43). Contiene:
   1. per ogni allievo presente il **libro della valutazione complessiva** (tutti i lavori con
      voto e indicazioni, cosa recuperare, le sue consegne in coda), **protetto** da password per
      il ragazzo e **senza** password per il docente;
   2. per il docente: **voti per il registro** in ordine alfabetico (O = proposta AI, C =
      valutazione ponderata del docente), **griglia completa**, **situazione e indicazioni** per
      allievo, **lista di recupero** (i tre con la media più bassa vengono interrogati),
      **monitoraggio**, **password**, **Excel** della classe aggiornato;
   3. due zip: **LIBRI-PROTETTI** (ragazzi) e **DOCENTE** (tutto, senza password); assenti fuori
      dagli zip. Prima volta: 1INF, 06/10/2026 (`generatori/valutazione_complessiva_1inf.py`).

## 09 Comandi / parole chiave (durante o a fine ore)

> Parole brevi da dire (anche dettando) per far generare la documentazione. Come `PPP`,
> sono convenzioni: si scrivono in maiuscolo all'inizio della richiesta.

### 09.1 Durante l'ora
1. **PPP** — "parcheggia": annota e prepara in silenzio, non consegnare finché non dico "avanti".
2. **AVANTI** — consegna quello che era parcheggiato.
3. **FIRMA** — prepara/ricorda la firma ore col programma previsto (entro le 14:05).
4. **VOLO** `nome 70|50` — voto "domanda al volo" da annotare (70 = OK, 50 = KO).
5. **LAVAGNA** `classe` — ho caricato la foto della lavagna: catalogala e mettila nei libri per data.
6. **PARCHEGGIATI** — mostrami la lista dei PPP ancora in sospeso.

### 09.2 A fine ora o fine giornata
1. **SVOLTO** — registra gli argomenti realmente svolti (aggiorna argomenti-svolti + matrice di copertura).
2. **VOTA** `slug-compito` — valuta le consegne (dallo zip) → le due griglie (completa + incrementale).
3. **REPORT** `slug-compito` — genera il report complessivo (impressioni + anti-plagio + indicazioni ragazzi + dettaglio).
4. **LIBRI** `classe` `complessivo|oggi|lezione <slug>` — (ri)genera i libri individuali
   della classe nel taglio scelto (tutto l'anno · la giornata di oggi · una sola esercitazione).
5. **CLASSE** `classe` `[data]` — (ri)genera il libro di classe (tipo B), tutto o per una data.
6. **MANUALE** `argomento/paragrafo` — aggiungi o migliora un paragrafo nella fonte unica → rigenera il libro totale (bump versione).
7. **INCREMENTALE** `classe` — aggiorna/genera la scheda incrementale insegnante (tutte le lezioni × voti + note + cose non capite).
8. **GIORNATA** `classe` — genera la scheda complessiva per giornata (unione delle schede di ogni lavoro del giorno).
9. **CHIUDI** `classe` — la **chiusura del lavoro di una classe**: fa **tutto in cascata** —
   SVOLTO → VOTA (griglia completa) → REPORT → **MONITORAGGIO** (report di monitoraggio
   allievi / andamento dell'ora, RISERVATO) → **CLASSE** (libro di classe aggiornato) →
   **LIBRI oggi** (libri individuali della giornata) → GIORNATA → **INCREMENTALE** (scheda
   insegnante) → STATO. Un comando solo a fine ora. (Le griglie totali portano sempre con sé
   il report di monitoraggio — vedi RIFERIMENTI §2.13.)
10. **STATO** — mostrami la base dati ad albero aggiornata (cosa c'è, cosa manca, coperture).
11. **VALUTAZIONE COMPLESSIVA** `classe` — genera la **Valutazione complessiva della classe**
    (08b punto 5): tutti i lavori fino a oggi, libri protetti per i ragazzi, documenti del docente,
    due zip. Prima dice cosa genera; i voti C li mette il docente.

### 09.2b Tabella: quale documento → quale comando

| Documento | Comando | Cosa contiene | Visibilità |
|---|---|---|---|
| Manuale / libro totale (A) | `MANUALE argomento/paragrafo` | tutto: 3 livelli d'albero × 3 profondità | pubblico |
| Libro di classe (B) | `CLASSE classe [data]` | teoria + esercitazione per data, senza nomi | pubblico |
| Libro individuale complessivo (C) | `LIBRI classe complessivo` | tutte le lezioni ed esercizi dell'allievo | riservato |
| Libro individuale di oggi (C) | `LIBRI classe oggi` | teoria + esercizi di oggi dell'allievo | riservato |
| Libro individuale di lezione (C) | `LIBRI classe lezione <slug>` | teoria + l'esercitazione in oggetto | riservato |
| Griglia completa (per compito) | `VOTA <slug>` | note + cosa non fatto (neretto) + voto | riservato |
| Scheda complessiva del lavoro (report) | `REPORT <slug>` | indicazioni al ragazzo + note docente + anti-plagio + non fatto/non capito | riservato |
| Scheda complessiva per giornata | `GIORNATA classe` | unione delle schede del lavoro del giorno | riservato |
| Scheda incrementale insegnante | `INCREMENTALE classe` | tutte le lezioni × voti + note alta visibilità + cose non capite | riservato |
| Foto lavagna nei libri | `LAVAGNA classe` | cataloga la foto e la inserisce nei libri per data | pubblico* |
| Argomenti svolti + firma ore | `SVOLTO` / `FIRMA` | registro svolto + firma programma | misto |
| Valutazione complessiva della classe | `VALUTAZIONE COMPLESSIVA classe` | tutti i lavori fino a oggi: libri protetti, voti O/C, griglia, situazione, recupero, zip | riservato |
| Chiusura giornata (cascata) | `CHIUDI classe` | genera in automatico tutto il necessario del giorno | — |

*Lavagna: pubblico se non si leggono nomi, altrimenti riservato.

### 09.3 Regole comuni ai comandi
1. Ogni output riservato (coi nomi) esce in **PDF** e non va su Git pubblico.
2. Ogni PDF esce con **header e footer** (titolo, contesto, "RISERVATO" dove serve, numero di pagina).
3. Dopo un comando che cambia i dati, aggiorno **`stato-dati`** così l'albero resta vero.

## 09c How-to ed esempi (se voglio X, dico Y)

> Gli scenari più frequenti, nel formato **se voglio … → dico … → ottengo …**.

1. **Chiudere il lavoro di una classe a fine ora** → `CHIUDI 3INF` → in un colpo: libro di
   classe aggiornato + libri individuali della giornata + griglia completa + scheda
   incrementale insegnante. (È lo scenario tipico di fine ora.)
2. **Valutare un compito appena raccolto** → `VOTA css-separato` → la **griglia completa**
   del compito e l'aggiornamento della scheda incrementale.
3. **Il quadro completo di un compito** (per me docente) → `REPORT css-separato` → la scheda
   complessiva del lavoro: mie impressioni + anti-plagio + indicazioni dei ragazzi + dettaglio.
4. **Dare all'allievo solo la lezione di oggi** → `LIBRI 3INF oggi` → il suo libro individuale
   della giornata (teoria + esercizi di oggi + valutazione).
5. **Dare all'allievo tutto il suo percorso** → `LIBRI 3INF complessivo` → il suo libro
   individuale completo (tutto l'anno).
6. **Aggiungere o migliorare una spiegazione** → `MANUALE lazarus/case` → aggiorno la fonte
   unica: il Manuale cresce e **tutti i libri che la richiamano** si aggiornano alla rigenerazione.
7. **Ho caricato la foto della lavagna** → `LAVAGNA 3INF` → la catalogo e la metto in cima ai
   libri per data (fissa argomenti e tempi).
8. **Firmare le ore a inizio giornata** → `FIRMA` → il programma previsto pronto da firmare
   entro le 14:05.
9. **A fine giornata, registrare cosa si è fatto** → `SVOLTO` → aggiorno gli argomenti svolti
   e la matrice di copertura.
10. **Voto "domanda al volo"** → `VOLO cognome 70` → lo annoto (70 = OK, 50 = KO).
11. **Non consegnare finché non dico "avanti"** → `PPP ...` → parcheggio, preparo in silenzio.
12. **Vedere cosa c'è e cosa manca** → `STATO` → l'albero della base dati aggiornato.

## 10 Operatività di ogni lezione

1. **Inizio:** `FIRMA` (programma previsto). La teoria nuova entra come argomento nel Manuale.
2. **Durante:** `PPP` per parcheggiare; `VOLO` per i voti al volo; `LAVAGNA` quando carichi le foto.
3. **Fine:** `SVOLTO`; poi `VOTA` / `REPORT` / `LIBRI` / `CLASSE` secondo cosa serve; `STATO` per verificare.
4. **Manutenzione:** se una spiegazione migliora, `MANUALE` sull'argomento → si aggiorna ovunque.

## 11 Glossario

1. **Fonte unica:** l'unico file dove un contenuto è scritto; il resto si genera da lì.
2. **Rigenerabile:** file che si ricrea dalle fonti (per questo non si versiona).
3. **Slug:** nome corto e stabile del compito/argomento, usato come chiave.
4. **Matrice di copertura:** tabella paragrafo × classe (fatto? quando? quale versione).
5. **Core / Approfondimento:** core = fatto da quella classe; approfondimento = fatto meglio altrove.
6. **Aggiornamento:** miglioria di un contenuto già presente, che propaga ai libri come nuova versione.

## 12 Changelog

1. **v0.5 (06/10/2026):** nuovo output **Valutazione complessiva della classe** (08b punto 5) e comando
   `VALUTAZIONE COMPLESSIVA classe`, con la lista standard valutazioni per il docente (RIFERIMENTI §2.43).
1. **v0.4 (01/10/2026):** la cascata **CHIUDI classe** ora include lo step **MONITORAGGIO**
   (report di monitoraggio allievi / andamento dell'ora): le griglie totali portano sempre
   con sé il report di monitoraggio (RIFERIMENTI §2.12-2.13).
2. **v0.3 (30/09/2026):** aggiunto il capitolo **09c How-to ed esempi** ("se voglio X, dico Y")
   con gli scenari frequenti; `CHIUDI classe` ora include anche il **libro di classe** e le
   griglie (completa + incrementale) — la "chiusura del lavoro di una classe".
2. **v0.2 (30/09/2026):** rinominato **Atlante**; aggiunti i due ambienti (main/Release),
   la topologia a 7 tipi-artefatto con nomi 2.13, il Manuale a due assi 3+3, l'accrescimento
   con matrice di copertura e aggiornamenti, le foto della lavagna e i **comandi/parole chiave**.
2. **v0.1 (30/09/2026):** prima stesura come "Topologia libri e metodologia".
