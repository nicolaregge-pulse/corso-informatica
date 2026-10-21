# Catalogo del corso

**Versione 1.2** — 21/10/2026 · Area Docente · senza nomi di allievi

*Il catalogo è l'elenco completo di tutto quello che abbiamo prodotto: ogni pagina del sito, gioco, strumento, script e cartella, con a che cosa serve e dove sta. L'Atlante con la mappa illustrata resta la parte da mostrare (experience, comunicazione, prova e simulazione); il catalogo è il magazzino del docente. I documenti con la loro versione sono elencati in `INDICE-DOCUMENTI.md`.*

## 00 Come si usa

1. **Indirizzo del sito:** tutte le pagine stanno sotto `https://nicolaregge-pulse.github.io/corso-informatica/`. Il percorso scritto nel catalogo (per esempio `docs/1inf-gamer/`) diventa l'indirizzo togliendo `docs/` (per esempio `.../corso-informatica/1inf-gamer/`).
2. **Due repository:** il pubblico `nicolaregge-pulse/corso-informatica` (ex `corso-godot`, stesso repository) e il riservato `nicolaregge-pulse/corso-informatica-riservato`. Dove non è scritto, si parla del pubblico.
3. **Quando nasce una cosa nuova** (pagina, gioco, script) si aggiunge la sua riga qui, nella sezione giusta, e si bumpa la versione.
4. **Differenza con gli altri elenchi:**
   1. `ATLANTE.md`: la mappa da mostrare e il racconto di come funziona il corso.
   2. `INDICE-DOCUMENTI.md`: i documenti (MD e PDF) con il numero di versione.
   3. `CATALOGO.md` (questo): tutte le cose prodotte, una per riga.

## 01 I tre framework

*La parte più importante del corso. Ogni lezione usa uno dei tre framework: si sceglie il framework, poi si riempie con il contenuto della lezione. In tutti e tre ci sono il monitor o il cruscotto dal vivo e il voto per ognuno con il conto (MANIFESTO §9.8).*

**Regole comuni a tutti e tre (Nicola, 21/10/2026):**

1. **L'assistente che aiuta:** in ogni pagina dei ragazzi c'è la casella «Chiedi aiuto all'assistente del Prof Regge» (`docs/assistente/`). Le domande vanno all'assistente, non al prof.
2. **L'avanzamento si vede:** ogni framework fa vedere a che punto si è. I ragazzi hanno il monitor della classe e il proprio andamento, per regolarsi da soli; il docente ha il cruscotto dal vivo cifrato.
3. **Il quadro generale della classe:** ogni ragazzo vede la situazione di tutta la classe (monitor e classifica), così capisce se è indietro o alla pari con i compagni.
4. **Il voto per ognuno con il conto:** parte da 40 e sale con le cose fatte, fino a 80; nella tabella ci sono tutti i presenti.

### 01a Framework 1: il codice in team con le Pull Request

1. **Che cos'è:** il gioco o il sito della classe cresce con le Pull Request dei ragazzi. Ogni Pull Request accettata diventa una versione nuova.
2. **Che cosa fa:**
   1. tiene traccia di tutto: chi ha proposto che cosa, quando, che cosa è entrato;
   2. ha sempre i sei bottoni della classe: voti, backlog, monitor, novità, classifica, valutazione;
   3. mostra le versioni, dice che cosa cambia da una all'altra e le lascia aprire e provare tutte, per sempre.
3. **I pezzi:**
   1. pagine: i sei bottoni `docs/<classe>-voti/`, `-backlog/`, `-monitor/`, `-novita/`, `-top/`, `-valutazione/`; le versioni giocabili `docs/giochi/<gioco>/versioni/`; il grafo `docs/giochi/grafo/`; `docs/lezione-versioni/`, `docs/2inf-revisione/`, `docs/3inf-gioco/`, `docs/3inf-pr/`;
   2. strumenti: `rilascia_versione_pr.py` (una Pull Request in produzione come versione nuova), `pubblica_versione_*.py`, `versione_treno_godot.py`, `gen_novita.py`, `gen_revisione_2inf.py`, `talpa_versione.py`, `talpa_voti.py`;
   3. GitHub: `.github/workflows/giochi-controllo.yml` controlla che una Pull Request dei ragazzi tocchi solo i file del gioco;
   4. riservato: `generatori/` per backlog, voti delle Pull Request e cruscotti (per esempio `giro_backlog_3inf.py`, `voti_pr_2inf.py`, `cruscotto_1inf_pr.py`).
4. **Dove l'abbiamo usato:** il treno blindato della 2INF, la talpa e il treno della 1INF, il gioco e i siti in coppia della 3INF.
5. **Documenti:** `GIRO-PULL-REQUEST.md`, `AGILE-CERIMONIE.md`, `ORGANIZZAZIONE-RAMI-CLASSI.md`.

### 01b Framework 2: Classroom, quiz o verifica, recupero, nuovo quiz e cruscotto

1. **Che cos'è:** la lezione normale tracciata dall'inizio alla fine. Il modello è la 1INF del 21/10.
2. **Il giro:**
   1. su Classroom un solo compito e un solo annuncio, «OGGI FATE SOLO QUESTE COSE, IN QUESTO ORDINE», con i link diretti;
   2. teoria e ripasso sulla pagina `verifica/?b=<banca>`;
   3. quiz o verifica su Google Moduli, creato dal ponte con `forms.crea_quiz` (traccia per la Regione);
   4. correzione automatica e recupero per chi è sotto;
   5. nuovo quiz per chi ha fatto il recupero;
   6. il cruscotto unico segue tutto dal vivo, una riga per presente, con il voto proposto 40-80.
3. **I pezzi:**
   1. pagine: `docs/verifica/` con le banche in `docs/verifica/banche/`; `docs/recupero/`; `docs/verifica-moduli/`; il cruscotto `docs/avanzamento/oggi.html?t=…&e=…&g=…&q=…&v=…`; uscite e fuori compito in `docs/avanzamento/`;
   2. strumenti: `banca2md.py` (documento della lezione), `prova_verifica.js` (prova come un ragazzo), `gen_recupero.py`, `cifra_json.py`, `giro_veyon.py`, `uscite.py`, `fuori_compito.py`, `gen_pianob.py`;
   3. script di Google: `automazione-corso.gs` con la coda (`coda/`) e il ponte (`comandi/`) nel riservato;
   4. riservato: `generatori/moduli_live.py`, `giro_compito_unico.py`, `correggi_verifica.py`, `recupero.py`, `crusc_1inf_cifrato.py`.
4. **Dove l'abbiamo usato:** 1INF del 21/10 (bit, byte, velocità e gamer), il portfolio della 3INF del 19/10, il ciclo FOR e il WHILE della 2INF.
5. **Documenti:** `FRAMEWORK-LEZIONE.md`, `VERIFICA-COME-SI-FA.md`, `CRUSCOTTO-DAL-VIVO.md`.

### 01c Framework 3: il quiz

1. **Che cos'è:** la lezione che si chiude con un questionario su Google Moduli allegato al compito su Classroom. Il lavoro del ragazzo resta dentro Classroom, valido per la Regione.
2. **Il giro:** si studia il materiale (pagina della lezione o sito ufficiale), poi il quiz su Moduli; le risposte arrivano con il ponte `forms.risposte` e vanno nel cruscotto e nei voti.
3. **I pezzi:**
   1. script di Google: `automazione-corso.gs`, azioni `forms.crea_quiz`, `forms.risposte`, `classroom.compiti`, `classroom.annuncio`;
   2. pagine: `docs/verifica-moduli/` e il cruscotto `docs/avanzamento/oggi.html` con il quiz cifrato;
   3. riservato: `generatori/moduli_live.py`, `dati/quiz-sicurezza-2INF/`, il conteggio delle prove in `PROVE-CLASSROOM-2026-27.md` (pubblico).
4. **Dove l'abbiamo usato:** il corso sulla sicurezza della Regione in 2INF (ore 1-4).

## 02 Registro DIDAweb e pubblicazione su Classroom

*Gli attrezzi che lavorano fuori dal sito: il registro elettronico DIDAweb e Google Classroom, nella finestra dell'account PIAMARTA.*

### 02a I segnalibri di DIDAweb

| Segnalibro | Codice (riservato `strumenti/`) | Che cosa fa |
|---|---|---|
| Voti DIDAweb (automatico) | `didaweb-auto.js` | Dal pacchetto preparato da Claude (data e ora, argomento, «Cognome Nome;voto» per ognuno) crea la colonna, scrive voti e argomento, chiede conferma e salva |
| Voti DIDAweb (a mano) | `didaweb-segnalibro.js` | Scrive i voti in una colonna già creata; non salva |
| Firma | `didaweb-firma.js` | Scrive l'argomento delle ore del docente e le firma, un'ora per clic |
| Diagnosi | `didaweb-diagnosi.js` | Legge la struttura della pagina, senza nomi né voti, per aggiornare i segnalibri |
| Copia HTML | — | Copia la pagina per costruire un segnalibro nuovo |

1. Gli indirizzi da incollare nei preferiti sono nei file `*-URL.txt` accanto al codice; stanno nella cartella «DidaWeb» della barra dei preferiti.
2. La guida passo per passo è `docs/docenti/02-didaweb-i-segnalibri-che-scrivono-i-voti.html`.

### 02b Lo script «Consegne Classroom → Git»

1. **Dove sta:** progetto Apps Script nell'account PIAMARTA, file `automazione-corso.gs`. Il codice da incollare si copia dal link pubblico `strumenti/automazione-corso.gs` (raw.githubusercontent).
2. **Come lavora:** gira da solo ogni minuto (lun-ven 7-15). Legge la coda (`coda/*.json`, compiti da pubblicare) e il ponte (`comandi/*.json`, azioni su Google) nel riservato.
3. **Che cosa fa su Classroom:**
   1. pubblica i compiti con PDF, Documento per ogni allievo e quiz su Moduli;
   2. chiude alla scadenza e porta le consegne su Git;
   3. aggiorna il testo delle istruzioni;
   4. mette i voti (in bozza o restituiti);
   5. pubblica, modifica e cancella gli annunci.
4. **Dietro le quinte (v8.2, 21/10/2026):**
   1. **bozza:** un compito o un annuncio si prepara in bozza; il docente lo vede in Classroom, i ragazzi no;
   2. **mostra:** con un comando la bozza diventa visibile ai ragazzi;
   3. **programmato:** la bozza si pubblica da sola all'ora scelta (per esempio alla prima campanella);
   4. **modifica:** titolo, istruzioni, scadenza e punti di un compito;
   5. **cancella:** solo con la conferma scritta «CANCELLA» e solo se nessuno ha ancora consegnato.
5. **Limite di Google:** lo script modifica, mostra e cancella solo le cose create da lui; un compito già pubblicato non torna in bozza.
6. **Piano B:** se lo script è fermo, `docs/prof-pubblica/` (generatore `strumenti/gen_pianob.py`).
7. **Guide:** `docs/docenti/03-google-lo-script-automatico-consegne-classroom-git.html`, `strumenti/classroom-script/VISIONE-AUTOMAZIONE.md`.

## 03 Pagine della 1INF

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| Oggi | `docs/1inf/` | La pagina del giorno: che cosa si fa oggi, in ordine |
| I sei bottoni | `docs/1inf-voti/`, `docs/1inf-backlog/`, `docs/1inf-monitor/`, `docs/1inf-novita/`, `docs/1inf-top/`, `docs/1inf-valutazione/` | Voti, backlog, monitor, novità del gioco, classifica, situazione |
| Quante ce ne stanno? | `docs/1inf-quante/` | Percorso guidato: quanto pesa un file e quanti ne stanno nel telefono |
| Giochi dei byte | `docs/1inf-byte-giochi/` | Peso di un'immagine, gara dei download, streaming, sfida delle unità |
| Slide bit, byte e velocità | `docs/1inf-byte/` | Le slide in PDF della lezione su bit, byte e velocità della rete |
| Laboratorio del gamer | `docs/1inf-gamer/` | Ping, jitter, lag, FPS e Hz, monitor, schede video e cavi video |
| Decimale e binario | `docs/1inf-decimale-binario/`, `docs/1inf-conversione/`, `docs/1inf-divisioni/`, `docs/1inf-divisione-resto/` | Divisione per 2, resto e conversione da decimale a binario |
| Il tuo nome in binario e i colori | `docs/1inf-nome-colori/` | Spiegazione e compito: il nome in binario e i codici dei colori |
| Foto e personaggi | `docs/1inf-foto-personaggi/` | Le facce dei personaggi del gioco della classe |
| Talpa: richieste per il prof | `docs/1inf-talpa-prof/` | Le proposte dei ragazzi per il gioco della talpa |
| Cruscotti | `docs/1inf-cruscotto/`, `docs/1inf-prof/`, `docs/1inf-prof-live/`, `docs/1inf-test/` | Cruscotto, pannello del prof, cruscotto dal vivo, cruscotto del test |

## 04 Pagine della 2INF

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| I sei bottoni | `docs/2inf-voti/`, `docs/2inf-backlog/`, `docs/2inf-monitor/`, `docs/2inf-novita/`, `docs/2inf-top/`, `docs/2inf-valutazione/` | Voti, backlog, monitor, novità del gioco, classifica, valutazione |
| Il treno blindato | `docs/2inf-treno/` | Il gioco della classe: versioni, investitori, organigramma |
| Le decisioni: if | `docs/2inf-if/` | Lezione e compito sull'IF in Lazarus |
| Slide del ciclo WHILE | `docs/2inf-while/` | Le slide in PDF del ciclo WHILE |
| Versioni e Git | `docs/2inf-versioning/` | Lezione sul versioning |
| Revisione delle versioni | `docs/2inf-revisione/` | Una riga positiva e una da migliorare per ogni versione del treno |
| Consegna e controllo | `docs/2inf-consegna/`, `docs/2inf-controlla/` | Consegna del gioco «Indovina» e controllo di chi ha fatto giusto |
| Cruscotto | `docs/2inf-cruscotto/` | Cruscotto della classe |

## 05 Pagine della 3INF

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| I sei bottoni | `docs/3inf-voti/`, `docs/3inf-backlog/`, `docs/3inf-monitor/`, `docs/3inf-top/`, `docs/3inf-valutazione/`, `docs/3inf-sprint/` | Voti, backlog, monitor, classifica, situazione, sprint |
| Il mio primo sito | `docs/3inf-sito/`, `docs/3inf-base/` | Corso HTML e CSS e modello di partenza del sito personale |
| L'albero del mio sito | `docs/3inf-albero/` | Legge i file del sito da GitHub e segna in rosso quello che manca |
| La Pull Request in coppia | `docs/3inf-pr/` | Percorso: collaboratore, ramo, Pull Request e merge sul sito del compagno |
| Pull Request in tempo reale | `docs/3inf-gioco/` | Il gioco della classe che cresce a colpi di Pull Request |
| Il mio punto | `docs/3inf-mio-punto/` | Per ognuno: che cosa gli manca, aggiornato dal giro automatico |
| Agile | `docs/3inf-agile/`, `docs/teoria/agile/`, `docs/teoria/agile-it/`, `docs/teoria/3inf-agile-lavoro/` | Cruscotto del Product Manager e teoria Agile |
| Cruscotti | `docs/3inf-cruscotto/`, `docs/3inf-prof-live/` | Cruscotto della classe e cruscotto dal vivo del docente |

## 06 Pagine della 4TI

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| ISO/OSI | `docs/4ti-iso-osi/` | Lezione sui sette livelli, con l'animazione del viaggio di un pacchetto |
| App di reti | `docs/4ti-app/` | Strumenti pratici sulle reti |
| Cruscotto dei progetti | `docs/4ti-progetti/` | Avanzamento dei progetti di stage |

## 07 Pagine comuni a tutte le classi

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| Ripasso e verifica | `docs/verifica/?b=<banca>` | Motore unico di teoria, ripasso e verifica; le banche stanno in `docs/verifica/banche/` |
| Banche presenti | `docs/verifica/banche/` | 1inf-assemblaggio, 1inf-byte-velocita, 1inf-gamer, 1inf-talpa, 1inf-versioni, 2inf-for, 2inf-for2, 2inf-sicurezza-3ora, 2inf-sicurezza-mod2, 2inf-versioning, 2inf-while, 3inf-agile, 3inf-grafica-pr, 3inf-portfolio, 3inf-versioning, 4ti-automa-meteo, 4ti-iso-osi-ripasso, prova-pc |
| Compiti | `docs/compito/<classe>-<data>-<nome>/` | Le pagine dei compiti, una cartella per compito |
| Quiz personale | `docs/quiz/` | Quiz individuale |
| Recupero a fianco | `docs/recupero/` | Pagine semplificate per rifare un esercizio con il docente accanto |
| Assistente | `docs/assistente/` | La casella «Chiedi aiuto all'assistente del Prof Regge» e le risposte |
| Controlla | `docs/controlla/` | Controlla chi ha fatto giusto |
| I siti della classe | `docs/siti-classe/` | Elenco dei siti dei ragazzi |
| Test di rete | `docs/test-rete/` | Prova della velocità e della rete |
| La password del mio libro | `docs/password-libro/` | Per aprire il proprio libro personale cifrato |
| Carica il tuo file | `docs/carica/` | Un ragazzo manda al prof un PDF o una foto (anche grande, a pezzi) con lo script delle consegne; arriva nel riservato in `dati/verifiche/caricamenti-<data>/` |
| Test di orientamento | `docs/orientamento/` | Per i ragazzi di terza media: logica, matematica, robot a blocchi e motivazione, con profilo finale; banca `banca-orientamento-v1.0.js`, scheda del docente nel riservato |
| Deepfake | `docs/sicurezza-deepfake/` | Voci e volti falsi, in tre lingue |
| Monta il PC | `docs/monta-pc/`, `docs/monta-pc-v2/`, `docs/monta-pc-v3/`, `docs/sfida-pc/`, `docs/classifica/`, `docs/monta-pc-cruscotto/` | Gioco di assemblaggio del PC, sfida lampo e classifica |

## 08 Pagine del docente

| Pagina | Percorso | A che cosa serve |
|---|---|---|
| Cruscotto della lezione | `docs/avanzamento/oggi.html?t=…&e=…&g=…&q=…&v=…` | Il cruscotto unico approvato il 21/10: una riga per presente, voto proposto 40-80 |
| Cruscotto della 3INF | `docs/avanzamento/3inf-oggi.html` | I siti dei ragazzi controllati a ogni giro |
| Ufficio informazioni | `docs/avanzamento/registri.html` | Tutti i registri che crescono a ogni lezione |
| Uscite dall'aula | `docs/avanzamento/uscite.html` | Uscite e rientri per classe |
| Fuori compito | `docs/avanzamento/fuori-compito.html` | Fuori compito rilevati da Veyon, con le foto dei giri |
| Monitor dal vivo | `docs/avanzamento/` | Pagina di partenza del monitor |
| Cruscotto della verifica | `docs/verifica-moduli/` | Arrivi del quiz su Google Moduli |
| Piano B | `docs/prof-pubblica/` | Pubblicare senza lo script, quando lo script è fermo |
| Strumenti DIDAweb e Google | `docs/docenti/` | Guida in sei capitoli: account, segnalibri DIDAweb, script, pagine collegate, giro completo |
| Voti per DIDAweb | `docs/strumenti/voti-didaweb.js` | Il segnalibro che scrive i voti nel registro |

I dati con i nomi in queste pagine sono sempre cifrati con `strumenti/cifra_json.py`.

## 09 Giochi

| Gioco | Sorgente Godot | Pubblicato in |
|---|---|---|
| Il treno blindato (2INF) | `treno-blindato-godot/` | `docs/giochi/treno-blindato/`, `docs/giochi/treno-godot/` |
| Il treno della 1INF (fork) | `treno-1inf-fork/` | `docs/giochi/treno-1inf/`, `docs/giochi/treno-1inf-fork/` |
| Il treno della 3INF | `treno-3inf-godot/` | `docs/giochi/treno-3inf/`, `docs/giochi/treno-3inf-v2/` |
| Il treno Luna | `treno-luna-godot/` | `docs/giochi/treno-luna/` |
| Il treno del prof | `treno-prof-godot/` | `docs/giochi/treno-prof/` |
| Assalto dei mostri (3INF) | — | `docs/giochi/assalto-dei-mostri/`, `docs/giochi/assalto-dei-mostri-avatar/` |
| Acchiappa la talpa | `acchiappa-la-talpa/`, `talpa-1inf/` | `docs/talpa/`, `docs/giochi/talpa-1inf/` |
| Schiva gli asteroidi | `schiva-gli-asteroidi/` | `docs/asteroidi/` |
| Rompi i mattoni | `rompi-i-mattoni/` | `docs/mattoni/` |
| Torta in faccia | `torta-in-faccia/`, `torta-panaccione/` | `docs/torta/`, `docs/torta-panaccione/` |
| Gioco del Quindici | `gioco-del-quindici/` | `docs/quindici/` |
| Battaglia navale 3D | `battaglia-navale-3d/` | — |
| Acchiappa le stelle, Chirurgo pasticcione | `acchiappa-le-stelle/`, `chirurgo-pasticcione/` | — |
| Esercizi di Godot | `esercizi/01-…` fino a `esercizi/04-…` | — |
| Elenco e grafo dei giochi | — | `docs/giochi/`, `docs/giochi/grafo/`, `docs/gioco/`, `docs/lezione-versioni/` |

Ogni versione pubblicata resta giocabile per sempre; la pubblicano gli script `strumenti/pubblica_versione_*.py`.

## 10 Vetrina (vedi l'Atlante)

| Cosa | Percorso | A che cosa serve |
|---|---|---|
| Atlante con la mappa | `docs/atlante-k4x9w2/`, `ATLANTE.md` | La mappa illustrata e cliccabile del corso |
| Il laboratorio raccontato | `docs/cm-qma7yay4q5/` | Racconto, parco, mattina della terza, progetti, PDF |
| Demo del laboratorio | `docs/demo/` | Giornate della 2INF già finite, cruscotto e prova, senza nomi |
| L'azienda dei videogiochi | `docs/azienda/` | La classe come un'azienda, con il report |
| Comunicazione e marketing | `comunicazione-marketing/`, `brochure/`, `presentazione-demo/` | Edizioni della comunicazione, brochure e presentazioni |
| Cassaforte | `docs/cassaforte/` | Proteggere i file con una password |

## 11 Strumenti (script del repository pubblico)

| Gruppo | Script | A che cosa serve |
|---|---|---|
| Pubblicazione | `aspetta_pubblicazione.sh`, `controlla_classe.py`, `controlla_edizione.py`, `controlla_edizione.js`, `installa_controlli.sh` | Aspettare il sito pubblicato e controllare le pagine prima di darle |
| Lezioni | `banca2md.py`, `prova_verifica.js`, `gen_pianob.py`, `gen_recupero.py`, `md2pdf.py`, `render-pdf/` | Documento della lezione dalla banca, prova come un ragazzo, piano B, recupero, PDF |
| Cruscotti | `cifra_json.py`, `giro_veyon.py`, `lavori_monitor.py`, `uscite.py`, `fuori_compito.py`, `thumb_siti.py` | Dati cifrati, Veyon, lavori fatti, uscite, fuori compito, miniature dei siti |
| Giochi | `pubblica_versione_treno*.py`, `pubblica_versione_assalto.py`, `rilascia_versione_pr.py`, `versione_treno_godot.py`, `talpa_*.py`, `testa_personaggio.py`, `importa_immagini_treno1inf.py`, `luna_password.py`, `audit_investitori_treno.py`, `esporta_talpa.sh` | Versioni dei giochi, personaggi, voti della talpa, investitori del treno |
| Generatori | `gen_atlante.py`, `gen_demo*.py`, `gen_metodologia.py`, `gen_novita.py`, `gen_revisione_2inf.py`, `prove_metodo.py`, `nome-albero.py`, `solo_italiano.py`, `sicurezza_2inf.py` | Atlante, demo, metodologia, novità, revisione, prove del metodo, nomi dei file |
| Script di Google | `automazione-corso.gs`, `demo-accesso.gs`, `classroom-script/` | Lo script «Consegne Classroom → Git» (coda e ponte) e gli script di Classroom |
| Dati delle classi | `schede-classi.json` | Le schede delle classi usate dalle pagine |

## 12 Automatismi di GitHub

| Automatismo | File | A che cosa serve |
|---|---|---|
| Pubblicazione del sito | `.github/workflows/deploy-pages.yml` | Pubblica `docs/` su GitHub Pages a ogni push |
| Controllo dei giochi | `.github/workflows/giochi-controllo.yml` | Controlla che una Pull Request dei ragazzi tocchi solo `docs/giochi/` |
| Bobina automatica | `.claude/hooks/bobina-automatica.py` | A ogni risposta di Claude scrive la bobina del giorno nel riservato |

## 13 Repository riservato

Qui si elencano solo le cartelle e i tipi di script: i contenuti hanno nomi di minori e restano nel riservato.

| Cartella | A che cosa serve |
|---|---|
| `dati/` | Fonte di verità: anagrafiche, presenze, voti, verifiche, Veyon, situazione, cruscotti |
| `diario/<classe>/` | Il diario di ogni lezione, con presenze, domande orali e report |
| `coda/` | Compiti da pubblicare su Classroom con lo script |
| `comandi/` | Il ponte con lo script: quiz su Moduli, risposte, esportazioni, annunci |
| `generatori/` | Gli script con i nomi: cruscotti cifrati, voti, report, libri individuali, chiusure, giri automatici |
| `config/` | Utenti GitHub delle classi, classi, prove, Moduli dal vivo |
| `strumenti/` | Segnalibri di DIDAweb (voti, firma, diagnosi) e gli script di Google |
| `storico/cruscotti/` | La fotografia dei cruscotti a ogni giro |
| `bobine/corso/` | Le bobine integrali delle chat, una per giorno |
| `archivio-prove/`, `prove-metodo/` | Le prove per la Regione e le prove che il metodo funziona |
| `antiplagio/`, `materiale-esami/`, `materiale-docente/` | Controllo dei lavori, esami e materiali del docente |
| `strategico/` | Dati della rete della scuola e dati personali del docente |
| `backup/` | Due copie zip della cartella di lavoro di inizio ottobre (02/10 e 05/10) |

## 14 Materiali e documenti

| Cartella | Contenuto |
|---|---|
| `classe-1/`, `classe-2/`, `classe-3/`, `classe-4/` | Materiali delle lezioni per classe, libri di testo, programmi |
| `manuale/`, `manuale-docenti/`, `manuale-informatica/` | Manuale ed eserciziario di Godot, guide per i docenti, manuale di informatica |
| `allegato-a-2026-27/`, `allegato-a-stato/`, `programmi-ufficiali/`, `piano-di-studio-2026-27/`, `programma-svolto/` | Allegato A, programmi ufficiali, piani di studio, programma svolto |
| `consegne/`, `attestati/`, `orario/`, `mappe/`, `argomenti/`, `sbobinature/` | Consegne, attestati dei ruoli, orario e campanelle, mappe, schede di argomento, sbobinature |
| `guida-docenti-alunni-non-italofoni/`, `guida-md-con-gemini/`, `corso-docente-ai/`, `quiz-recupero-invalsi/`, `libro-paganini/` | Guide, corso sull'AI per docenti, recupero INVALSI, confronto con il libro di testo |
| Documenti nella cartella principale | Elencati con la versione in `INDICE-DOCUMENTI.md` |

## 15 Registro delle versioni

1. **v1.2 (21/10/2026)**: nuovo capitolo 02 «Registro DIDAweb e pubblicazione su Classroom», con lo script v8.2 (bozze, mostra, pubblicazione programmata, modifica e cancellazione).
2. **v1.1 (21/10/2026)**: nuovo capitolo 01 «I tre framework», la parte più importante, dettata da Nicola; gli altri capitoli scalano di un numero.
3. **v1.0 (21/10/2026)**: prima versione, chiesta da Nicola: tutto quello che è stato prodotto, separato dall'Atlante (la vetrina).
