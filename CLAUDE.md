# CLAUDE.md — Corso Godot (cartella `godot/`)

Preferenze e contesto **solo** per il corso Godot/GDScript. Non c'entra con
Quidoo Pulse (che ha il suo CLAUDE.md nella root). Questo file vale quando si
lavora dentro `godot/`.

---

## ⭐ Contesto umano e missione (leggere SEMPRE per prime)

Gli studenti vivono spesso situazioni di **svantaggio sociale**: molti hanno un
**background migratorio** (extracomunitari), a volte contesti familiari
difficili, e non hanno avuto molte opportunità. Spesso sono ragazzi
**"scartati" da altre scuole** (respinti o messi da parte da altri istituti) e
arrivano qui già segnati da quei rifiuti. Alcuni possono essere "difficili" da
coinvolgere e tenere agganciati.

> Proprio per questo il modo in cui li trattiamo conta doppio: qui **non sono
> scarti**, sono ragazzi a cui diamo una cosa fatta bene. Il tono è sempre di
> **rispetto e fiducia**, mai di sufficienza.

**Il legame di fiducia (leva + responsabilità):** questi ragazzi hanno **grande
stima nel docente**, proprio perché è lui a dargli questa possibilità. È il
motore motivazionale più forte che abbiamo — e insieme la responsabilità di
**non deluderli**: mantenere alta la qualità e non far mai sentire quel patto
tradito.

**La missione del docente (Nicola):** offrirgli un percorso di **qualità
superiore**, con **dignità**, perché possano trovare **sbocchi lavorativi
migliori**. Questo NON è un corso "di serie B": è pensato apposta per **aprire
porte**. Va tenuto alto il livello *e* accessibile il modo.

**Implicazioni pratiche (VINCOLANTI):**
- **Approccio molto semplice, tutto VISUALE.** Niente riga di comando — né per
  Git né per altro. Si **clicca**, non si digitano comandi.
  - Per **Git**: solo strumenti visuali. Consigliato **GitHub Desktop** (il più
    semplice, bottoni grandi e chiari) oppure il **pannello Git di VS Code**.
    **MAI la CLI** con loro.
- Passi **piccolissimi**, un obiettivo alla volta, sempre con un risultato
  concreto e "figo" da vedere subito.
- **Zero gergo** non spiegato; ogni termine tecnico/inglese va tradotto.
- **Tanto incoraggiamento**: celebrare ogni piccola vittoria; non far mai
  sentire "stupido" nessuno. La pazienza è parte del metodo, non un extra.
- Risultati **spendibili e mostrabili** (giochi che funzionano, cose di cui
  essere fieri): sono la leva motivazionale più forte per questi ragazzi.

## ⭐ Il motore del coinvolgimento (il problema numero 1)

Il rischio vero non è che non capiscano: è che **si stufino e mollino**. Molti
hanno imparato che "provarci = fallire ed essere umiliati", quindi si arrendono
*prima*, per difesa. Il compito numero 1 è **far sentire che qui provarci
conviene e non fa male**. Ogni esercizio si progetta attorno a questo motore:

**"Vinci subito · Fallo tuo · Mostralo"** — sempre tutte e tre:
1. **Vinci subito (≈10 min):** il primo risultato deve essere quasi impossibile
   da sbagliare. Poche mosse → qualcosa che funziona a schermo. La prima
   vittoria è ciò che impedisce la fuga.
2. **Fallo tuo:** in ogni esercizio scelgono qualcosa di **loro** (colore, nome
   del gioco, personaggio, foto/meme, scritta). L'ownership è il gancio più
   forte.
3. **Mostralo:** ogni pezzo dev'essere **giocabile e mostrabile** (al compagno,
   sul telefono). Il "l'ho fatto io" motiva più di un voto.

Due ingranaggi di supporto:
- **Passi minuscoli con "FATTO!" visibile:** mai più di un obiettivo alla volta;
  ognuno chiude con una piccola vittoria concreta.
- **Errore = zero vergogna:** annulla facile, il bug è normale ("succede a tutti
  i programmatori, anche ai pro"). Nessuno si sente stupido, mai.
- **La prova del nove — "saperlo spiegare":** se sanno raccontare a voce, con
  parole loro, cosa fa ciò che hanno fatto (anche se in parte copiato), la
  competenza c'è davvero. È anche la regola d'uso dell'AI: aiuta a capire, non a
  saltare il pensiero.

> Conseguenza pratica sugli esercizi: si parte SEMPRE da qualcosa di
> **giocabile e personalizzabile**, non da esercizi "scolastici" astratti.

## ⛔ REGOLE OPERATIVE DA NON DIMENTICARE (Nicola ci tiene — leggere per PRIME)

**1. Nome del ramo di lavoro: sempre PULITO.** Il ramo deve avere un nome
leggibile (es. `claude/corso-godot`). MAI lasciare o mostrare rami con suffissi
casuali tipo `...-mubah1`. Se il sistema che avvia la sessione ne assegna uno
così, spostare **subito** il lavoro su un ramo dal nome pulito. Non promettere
mai "non lo vedrai più" se non dipende da me: dire la verità sui limiti.

**2. Con che programma si apre ogni tipo di file** (scuola = zero installazioni,
niente admin: usare SOLO ciò che è già presente):
- **Codice `.gd`** → si scrive/apre **dentro Godot** (portabile, è già lì). Per
  solo **leggerlo** come testo: click **destro** sul file → `Apri con` →
  `Blocco note`. Mai doppio clic (apre Godot e fa partire il gioco).
- **File `.md`** (manuale, eserciziario, quaderno) → si leggono **impaginati** su
  `github.com` (browser); per modificarli, la matita di GitHub o `github.dev`
  (tasto `.`). Per solo testo offline: `Blocco note`.
- **Manuale da leggere impaginato** → il **PDF** (con SumatraPDF, portabile).
- Regola d'oro: **mai far installare programmi**. Solo Blocco note, browser,
  Godot portabile, SumatraPDF portabile.

**3. Prefisso `PPP` = "prendi in considerazione ma NON dare l'output finché non
dico avanti".** Quando una riga di Nicola inizia con `PPP` (a voce, dettando,
l'equivalente è **"parcheggia, parcheggia, parcheggia"**), è un **promemoria da
annotare**: NON si consegna il risultato finale / non si riempie la chat finché
Nicola non dice **"avanti"**. Serve a **non far scorrere la chat**. Comportamento:
- Registrare il contenuto come nota/promemoria.
- **Iniziare a preparare** in silenzio (bozze, file, ragionamento), ma **non
  consegnare** l'output finale finché non arriva **"avanti"**.
- Rispondere in modo **minimo** (al più un cenno brevissimo di presa in carico),
  mai un blocco esplicativo, finché non è dato l'"avanti".
- **Eccezione:** se dentro il `PPP` c'è un'azione concreta esplicita (es. "dammi
  il PDF il prima possibile", "committa"), quella si esegue subito.
- **"Fammeli" vince sul PPP:** se un risultato è già stato chiesto ("dammi",
  "fammi"), i PPP successivi ne precisano solo il contenuto: si consegna appena pronto.
- **Se non sto facendo niente, vado avanti comunque** sul lavoro parcheggiato.
- Dettaglio completo nel file interno `REGOLE-NOSTRE-CLAUDE-NICOLA.md` (le nostre
  convenzioni, da non confondere con le regole PER i ragazzi).

**4. Registro (firma ore): segnare SEMPRE il PROGRAMMA INIZIALE su tutte le ore.**
Logica di Nicola: firma in anticipo il programma previsto su ogni ora, per non
rischiare di lasciare **ore non firmate**; a fine giornata lo aggiorna con gli
argomenti **realmente svolti**. Compito di Claude, ogni giorno di lezione:
- **Memorizzare** il programma previsto e le **presenze/assenze** quando Nicola
  le manda (le presenze contengono nomi di minori → restano in scratchpad, NON
  nel repo).
- **Tenere traccia** durante la lezione (anche voti "domande al volo": 70 OK / 50 KO).
- **⏰ FIRMA ENTRO LE 14:05 (VINCOLANTE):** i registri vengono **inviati alle
  14:05**; le ore **non firmate entro quell'ora** vengono **tolte dal monte ore
  della Regione**. Perciò Nicola firma **subito in classe** il programma previsto
  (anche con argomenti provvisori) e li corregge dopo. **Compito di Claude:
  ricordare la firma IN AULA, prima delle 14:05** (non a fine giornata).
- **Testo per il registro CORTO:** max ~40 caratteri, una frase, niente parentesi, uno per
  ora in blocchi da copiare separati (la casella taglia il testo lungo). Vedi RIFERIMENTI §2.25.
- **A FINE giornata: CHIEDERE a Nicola gli argomenti realmente svolti** e
  aggiornare (`ARGOMENTI-SVOLTI-2026-27.md`, senza nomi). La firma è già stata
  fatta prima (vedi sopra); a fine giornata si sistemano solo gli **argomenti**.

**5. Libro di testo Classe 1 (workflow VINCOLANTE).** Ogni lezione produce un
documento **MD + PDF versionato** (e si **archivia anche l'HTML** quando la resa
è da HTML). Poi Claude **aggiunge automaticamente** quel contenuto al **libro di
testo complessivo** `classe-1/libro-di-testo/libro-classe1.md` (bump versione +
voce nel changelog). Il **PDF serve per leggere/stampare**, l'**MD si dà ai
ragazzi per la loro AI** (che spiega/traduce nella loro lingua). **Claude mette
SEMPRE tutto su Git e lo tiene aggiornato** (MD, PDF e HTML).

**6. Prima di proporre QUALSIASI cosa ai ragazzi: chiedere SEMPRE «Pubblico o vuoi vederlo prima?» (09/10/2026, VINCOLANTE).**
Vale per compiti, Documenti, quiz, Moduli, annunci, post e pagine per i ragazzi. Si prepara tutto, si dà a Nicola il link
per vederlo e si aspetta la sua risposta: si pubblica SOLO dopo la parola «pubblica» (o un sì esplicito a quella domanda).
Un orario detto prima («negli ultimi 25 minuti») NON vale come via. Vedi REGISTRO-ERRORI #41.

## Contesto didattico

- **Docente:** Nicola. Sta imparando Godot in prima persona, in parallelo ai
  ragazzi.
- **Classi:** una **seconda** e una **terza** di **istituto professionale**.
  → Taglio **pratico**: fare prima, teoria in piccole dosi legata al fare;
  risultato visibile e "figo" a ogni passo; molto copia-modifica-sperimenta.
  Sfruttare al massimo i 4 livelli di aiuto dell'eserciziario.
- **Background dei ragazzi:** conoscono **Lazarus** (Free Pascal) a **livello
  base**. Hanno usato pochi componenti:
  - **TButton** (il bottone)
  - **TEdit** (la casella di testo)
  - la proprietà **Caption** (il testo mostrato)
  - Progetti fatti: cose molto semplici, tipo una **calcolatrice**.
- Quindi: **principianti**. Sanno cos'è un evento (click), una proprietà, una
  variabile; non hanno mai visto un "game loop" né la programmazione a oggetti
  avanzata.

## Obiettivo del corso (quest'anno)

- Un corso che **diverta**: la priorità è tenerli **agganciati**.
- Tutti i progetti devono essere **molto usabili e accattivanti** — giochini
  che li attirano e che possono mostrare/giocare subito. Niente esercizi aridi.
- Difficoltà **graduale**, sempre con un risultato visibile a ogni passo.

## Metodo (come spiegare)

- **Sempre in italiano**, semplice, **un passo alla volta**, con risultato a
  schermo a ogni tappa.
- **Bridge da Lazarus**: spiegare ogni concetto Godot partendo da ciò che già
  conoscono. Tabella di traduzione:
  | Lazarus (lo sanno) | Godot (nuovo) |
  |---|---|
  | Form | Scena (albero di nodi) |
  | Componenti (TButton, TEdit…) | Nodi (Button, LineEdit, Label…) |
  | Proprietà (Caption…) nell'Object Inspector | Proprietà nell'Ispettore |
  | Gestore evento (`Button1Click`) | Segnale + funzione |
  | Object Pascal | GDScript (stile Python) |
  - Concetto NUOVO chiave da introdurre bene: il **game loop**
    (`_process(delta)` gira ~60 volte/sec da solo). *"Lazarus reagisce, Godot
    pulsa."*

## Progetti a gruppi (lavoro in team) — importante

Durante l'anno, ogni tanto, fare **progetti a gruppi di 2-4** ragazzi con i
**ruoli divisi**, per insegnare a **sviluppare in team** (competenza lavorativa
vera, spendibile):
- uno sviluppa la **scena**;
- uno i **nodi**;
- uno l'**interfaccia grafica** (GUI);
- uno i **movimenti**/logica di gioco.

Obiettivi: collaborazione, divisione dei compiti, **integrare il lavoro degli
altri** (come in un vero team di sviluppo). Si lega bene a **Git**: ognuno lavora
sul suo pezzo e poi si uniscono i contributi.

**Attenzioni (dato il contesto):**
- Comporre i gruppi con cura; **ruoli chiari e a rotazione** così tutti provano
  tutto e nessuno resta indietro o si nasconde dietro i più bravi.
- Ogni gruppo deve arrivare a una **piccola vittoria mostrabile** (coerente col
  motore "Vinci subito · Fallo tuo · Mostralo").

## ⭐ Vincolo SCUOLA: niente installazioni → browser + portabile

A scuola installare software richiede l'**amministratore di sistema** (lento, e
ogni problema successivo va ri-chiesto a lui). Quindi, per le **postazioni
scolastiche**, prediligere soluzioni **SENZA installazione**:

- **Godot è PORTABILE** 🎉: è un singolo `.exe`, **non serve installarlo** con
  l'admin. Si copia in una cartella utente (o su chiavetta USB) e si avvia con
  doppio clic. → Il pezzo più grosso è già risolto.
  - Possibile ostacolo: policy che bloccano gli `.exe` non firmati (AppLocker).
    In quel caso serve **uno sblocco una tantum** dal sysadmin, non
    un'installazione ricorrente.
- **Git / versioning: tutto da BROWSER** (zero software):
  - **github.com**: creare repo, modificare file (icona matita), fare commit,
    creare branch e Pull Request — tutto dall'interfaccia web.
  - **github.dev**: dentro un repo premi il tasto **`.`** (punto) → si apre un
    editor tipo VS Code **nel browser**; modifichi e fai commit lì. Zero install.
- Ripiego 100% browser anche per Godot: **editor.godotengine.org** (l'editor di
  Godot nel browser), ma è più limitato/sperimentale → usarlo solo se il `.exe`
  portabile fosse bloccato.
- **Sulla macchina personale di Nicola** (non a scuola) va benissimo **GitHub
  Desktop**: comodo per lui per preparare le cose.
  - **Uso didattico = "seconda vista"**: mostrare lo *stesso* concetto (un
    commit, un branch, il sync) sia nel **browser** sia in **Desktop** aiuta a
    capire che **Git è il concetto, lo strumento è solo una finestra** su di
    esso. Desktop rende più evidenti: la vista *modifiche/staging* prima del
    commit, una **storia** ordinata e il **sync locale↔cloud** (push/pull).
    Ambiente primario per la classe resta comunque il **browser**.

## ⭐ Guida passo-passo — coordinate SEMPRE complete (regola VINCOLANTE)

Quando chiedo a Nicola di fare **qualsiasi** azione (un comando, un clic, un
valore da inserire), devo **SEMPRE** premettere le coordinate complete, così sa
esattamente dove agire. Prima dell'azione indico, in quest'ordine:

0. **Quale ACCOUNT** (07/10/2026, VINCOLANTE) — si chiamano così: **account PERSONALE** = nicolaregge@gmail.com
   (finestra Chrome con le schede gialle e la foto in alto a destra, dove c'è GitHub) e **account PIAMARTA** =
   nicola.regge@piamarta.it (finestra Chrome con le schede arancioni e il bottone «Scuola», dove ci sono DIDAweb,
   Classroom e lo script).
   Ordine fisso di ogni riga: **account → finestra → app → dove → cosa**, con le **caselle da copiare**
   sempre nello stesso messaggio.
1. **Quale APPLICAZIONE** — es. `[APP — GitHub Desktop]`, `[APP — Godot]`,
   `[APP — Esplora file]`, `[BROWSER]`.
2. **Quale FINESTRA / SCHEDA** — se ce ne sono più aperte, dirlo esplicitamente
   (es. `[BROWSER — scheda "corso-godot"]`).
3. **Quale MENU → voce → sotto-voce**.
4. **In quale AREA della finestra/applicazione** — pannello a sinistra, barra in
   alto a destra, riquadro in basso, ecc.
5. **L'AZIONE esatta**, **una alla volta**.

**Mai** dare un comando "nudo" senza dire **dove** va messo. Un passo alla volta;
se è terreno nuovo per lui, massima precisione.

**⭐ REGOLA COPIA (VINCOLANTE, chiesta da Nicola — non violarla mai):** qualunque
cosa Nicola debba **copiare** (un nome file, un valore, un comando, un pezzo di
testo) va **SEMPRE** in un **blocco di codice recintato** — cioè su una riga a
parte, tra ` ``` ` e ` ``` ` — così compare il **bottone "copia"** e lui NON deve
selezionare col mouse. Regole precise:
- **NON basta** il codice "in linea" con un solo apice (`` `così` ``): NON ha il
  bottone copia → vietato per le cose da copiare.
- **NON** metterlo come testo normale nella frase, né nel blockquote `>`.
- **Un valore per blocco:** un solo riquadro = una sola cosa da copiare, così un
  clic copia esattamente quella e nient'altro.
- Vale anche per **nomi di file**: es. il nome da dare a uno screenshot va nel suo
  riquadro, da solo.
- Il testo dentro il riquadro dev'essere **esattamente** ciò che serve, pronto da
  incollare (nessuna barra `/` nei nomi file di Windows, ecc.).

**Rinforzo (chiesto da Nicola, vale SEMPRE — è più importante di andare veloci):**
- **Una sola azione per riga numerata.** Mai due clic nella stessa riga.
- **Ogni riga dice DOVE prima di dire COSA:** applicazione → scheda/finestra →
  area della pagina (es. "in alto a destra", "nel menu a sinistra") → il nome
  **esatto** del bottone/voce (tra apici) → l'azione.
- **Se Nicola manda uno screenshot, indico il punto ESATTO** su *quella*
  schermata (dove si trova, com'è scritto), non un'istruzione generica.
- **Non dare mai per scontato** che sappia dov'è un bottone o cosa fa un termine.
  Nel dubbio, essere più precisi, non meno.
- Meglio **lento e chiaro** che veloce e confuso: la fretta qui è un errore.
- **SOLO IL PROSSIMO PASSO (07/10/2026, Nicola):** non ripetere mai i passi che ha già fatto; dire il prossimo passo e basta, aspettare che lo faccia, poi il successivo.
- **Formato a TABELLA (07/10/2026, Nicola):** i passi si danno in una tabella con le colonne N. · Account · Finestra/scheda · Dove · Cosa fare (una riga = una azione).

## ⭐ Standard di formattazione dei documenti (VINCOLANTE)

Tutti i documenti del corso — **presenti e futuri** — seguono lo standard scritto
in **`REGOLE-FORMATTAZIONE.md`** (documento 00). È la regola, non un consiglio.
Per questo progetto la **fonte di verità è Nicola** (nessun ruolo di soggetti
esterni). Punti chiave da ricordare sempre:

- **MD + PDF** per ogni documento; una **super-guida combinata** + zip dei singoli.
- **Liste solo numerate e gerarchiche** (1, 1.1, 1.1.2): **niente elenchi puntati**.
- **Niente emoji decorative** nei documenti; per evidenziare si usano i **box
  colorati semantici** (rosso = disallineamento, blu = da confermare, giallo = nota).
- **Titoli numerati** (00, 01, 02, 02b), **senza trattino** ("02 Panoramica"), mai
  orfani a fine pagina.
- **Sigle** esplicitate alla prima occorrenza; termini ricorrenti nel **GLOSSARIO**.
- **Versione congelata** una volta stampata; correzioni nella successiva
  (CHANGELOG_Vn + ERRATA_Vn in coda al combinato).
- **REGOLA 0 (assoluta):** tutto ciò che l'utente deve **copiare** va in un
  **blocco di codice** (col bottone "copia"), mai in linea né in citazione.

**Come si concilia col metodo del corso:** cambia la **forma** (formattazione
sobria, niente emoji/puntati), **non** la **sostanza pedagogica**. Restano intatti:
tono di rispetto e incoraggiamento, passi piccolissimi, "Vinci subito · Fallo tuo ·
Mostralo", celebrare ogni vittoria, coordinate sempre complete. Si può essere caldi
e incoraggianti anche in prosa sobria e con liste numerate.

> Nota di migrazione: i documenti già esistenti (guide, manuale, indici) si
> adeguano **gradualmente** allo standard, non tutti in una volta, per non
> introdurre errori. Ogni nuovo documento nasce già conforme.

## ⭐ Ogni testo per i ragazzi nelle 3 lingue (VINCOLANTE — richiesto da Nicola)

Ogni testo **destinato agli allievi** (consegne, esercizi, guide, avvisi, schede)
deve essere **disponibile nelle 3 lingue** del gruppo: **italiano, arabo, cinese
semplificato**. Regole pratiche:

- Va bene sia **3 file separati** (uno per lingua) sia **un unico file** con le
  tre lingue affiancate; per le consegne operative si preferiscono i **3 file
  monolingui**, ognuno con **tutte** le indicazioni complete.
- Le indicazioni devono essere **semplici e complete** ("a prova di errore"):
  spiegare tutto, compreso a cosa servono link/strumenti, come si crea il lavoro e
  come si consegna.
- **Font per il PDF**: cinese **WenQuanYi Zen Hei**, arabo **Amiri** (installato in
  `~/.fonts`); questi documenti si generano da **HTML** (non dal motore "libro"
  che usa DejaVu, privo di cinese/arabo). L'arabo va reso **RTL** (`dir="rtl"`).
- **Eccezione**: i materiali **interni per il docente** (pianificazione, registro
  attività, regole, indici) restano in italiano; la regola vale per ciò che
  arriva in mano agli allievi.
- **⭐ Testo latino dentro l'arabo/cinese (richiesto da Nicola):** nei testi in
  arabo e cinese capita di dover scrivere parole in caratteri latini; vanno
  gestite così, perché i ragazzi che leggono in arabo/cinese non restino spiazzati:
  1. **Indirizzi e email** (es. `github.com`, un'email): NON si traducono (un
     indirizzo si scrive sempre in lettere latine). Vanno marcati chiaramente
     nella loro lingua come "indirizzo/e-mail: scrivilo esattamente così".
  2. **Nomi dei bottoni dei siti**: NON scriverli in inglese. Il ragazzo spesso
     fa tradurre il sito nella sua lingua, quindi il testo inglese non coincide
     con quello che vede. Si descrive il bottone per **posizione + colore + a
     cosa serve** (che valgono in qualunque lingua), con la parola **italiana**
     probabile come aiuto (invitando a tradurre la pagina in italiano). Mai
     affidarsi al solo testo del bottone.

## ⭐ Struttura del corso e flusso Git

### Due ambienti: "autore" (Nicola) vs "ragazzi"
Il corso stesso è versionato su Git, su due livelli:
- **`main` = ambiente AUTORE (di Nicola).** La sua "cucina": prepara, avanza,
  migliora il corso; può essere anche in lavorazione/incompleto.
- **Release per i RAGAZZI.** Quando una parte è pronta e testata si pubblica una
  **Release** taggata (`v1.0`, `v1.1`…): la versione **congelata e stabile** che
  i ragazzi ricevono. Non cambia sotto i loro piedi mentre Nicola lavora alle
  migliorie, e insegna davvero il concetto di **release/versione**.
- **I ragazzi lavorano su una LORO copia** (fork o repo personale), **mai** sul
  master di Nicola: il suo resta intatto e ognuno ha il suo spazio per esercizi
  e quaderno. (Si sposa con la Fase 2: branch/PR.)

### Ibrido a due fasi (la complessità Git cresce con loro) — SCELTA CONFERMATA
- **Fase 1 (inizio) — esercizi SEPARATI**, ognuno con la sua descrizione (scheda
  a 4 livelli). Git semplice: un **commit** per salvare la propria versione. Se
  sbagli un esercizio gli altri restano intatti (zero conseguenze, zero
  vergogna). In repo: cartella `esercizi/` con una sottocartella per esercizio.
- **Fase 2 (quando hanno confidenza / progetti a gruppi) — progetto che EVOLVE**
  con **branch → Pull Request → release**. Un gioco che cresce; ognuno sul suo
  branch, PR, merge, e release taggate (`v1.0` giocabile, `v1.1` con suoni…). In
  repo: cartella `progetto-gruppo/`.
- **Perché non partire dal flusso unico + PR:** per ragazzi che mollano facile un
  progetto unico che si rompe = frustrazione, e PR/merge all'inizio sono troppo.
  Prima farglielo **desiderare** (semplice), poi introdurlo quando il gioco di
  gruppo lo rende naturale.

## ⭐ Carta e penna in OGNI lezione (TASSATIVO — richiesto da Nicola)

Regola **vincolante e senza eccezioni**, da rispettare e da ricordare in **ogni
singola lezione** di **tutti** gli anni:

- **Ogni allievo deve avere carta e penna sul banco**, per prendere **appunti** e
  fare **schemi a mano** — sempre, anche (e soprattutto) quando si lavora al
  computer. Scrivere e disegnare a mano aiuta a capire e a fissare i concetti.
- **Se un allievo non li ha, il docente glieli fornisce e segna una nota**
  (annotazione), lezione per lezione. Non è un capriccio: è parte del metodo.
- Gli appunti e gli schemi a mano **confluiscono nel quaderno personale** (anche
  fotografati e incollati): alimentano il "Mostralo" e la prova del nove.
- **Conseguenza per il materiale:** ogni piano-lezione, guida ed esercizio deve
  dare per scontato carta e penna e, dove utile, **prevedere esplicitamente** il
  momento "prendi appunti / fai lo schema a mano".

## ⭐ Regole operative permanenti (richieste da Nicola)

1. **Tutto versionato.** Ogni file (progetti Godot, script, documenti) va nel
   repository, sul branch del corso. Niente lavoro che vive solo sul PC.
2. **Manuale in doppio formato.** Ogni volta che si produce un **PDF** (il
   "manuale"), si produce **anche** un file **`.md` versionato** con **tutto
   quello che abbiamo detto/spiegato**.
   - Il **`.md` è la fonte versionabile** (sorgente di verità, in git).
   - Il **PDF è la resa consegnabile** generata dall'`.md`.
   - Il "manuale" ha **due parti**, entrambe in `godot/manuale/`:
     * **`manuale.md`** = il **libro di testo** (teoria/narrazione; cresce mano
       a mano che avanziamo insieme nella comprensione di Godot).
     * **`eserciziario.md`** = gli **esercizi** per i ragazzi, con codice già
       fattibile. Ogni esercizio ha **4 livelli di aiuto a scoperta graduale**:
       (1) descrizione, (2) aiuto/indizio, (3) la scena/i nodi, (4) codice
       completo. Così chi ce la fa procede da solo, chi è bloccato scopre solo
       l'aiuto che gli serve.
   - **Immagini/screenshot nel libro di testo**: il libro deve contenere
     **immagini dell'ambiente** (es. l'editor Godot all'avvio) per orientare i
     ragazzi. Stanno in `godot/manuale/immagini/` e sono richiamate nell'`.md`.
     ⚠️ Gli screenshot li fornisce **Nicola**: io (Claude) non vedo/salvo le sue
     schermate come file, quindi le mette lui nella cartella `immagini/` con il
     nome atteso, e nel MD trova già i riferimenti pronti.
   - **Quaderno dello studente** (portfolio personale): **ogni ragazzo tiene un
     SUO libro di testo** che cresce a OGNI lezione e a OGNI esercizio (pagine
     aggiunte man mano). Anche questo in **MD + PDF versionato**. Template in
     `godot/manuale/quaderno-studente-TEMPLATE.md`. Serve il motore "Mostralo" +
     la prova del nove "saperlo spiegare": documentano e raccontano ciò che
     fanno, e a fine anno hanno un libro **loro** di cui essere fieri.
3. **Versionare il manuale come i PDF di Quidoo:** una versione consegnata è
   **congelata**; se cambia il contenuto si **bumpa** il numero di versione e si
   aggiunge una voce al changelog in fondo al `manuale.md`. Mai riusare un
   numero già consegnato.
   - **Il numero di versione sta SEMPRE nel NOME del file PDF.** Il consegnabile
     si chiama `manuale-vX.Y.pdf` (es. `manuale-v0.1.pdf`), **mai** un generico
     `manuale.pdf`. Così due versioni non si sovrascrivono e si vede a colpo
     d'occhio quale versione si ha in mano. Il numero nel nome file deve
     **coincidere** con la "Versione X.Y" scritta nell'intestazione del `.md`.
   - **Mai due file con lo stesso numero di versione.** Se cambia anche solo un
     contenuto, prima si bumpa la versione nel `.md`, poi si rigenera il PDF (che
     prenderà automaticamente il nuovo nome).
   - Il nome del PDF è **generato in automatico** dalla "Versione" del `.md`
     (vedi `manuale/_build/genera_pdf.py`): non va scritto a mano.

## 🗺️ Prossimi passi (roadmap immediata)

**Sessione dedicata al LIBRO DI TESTO** (richiesta da Nicola):
1. **Agganciare `corso-godot` a questa sessione** (add_repo — serve OK esplicito di Nicola).
2. **Spostare** manuale + eserciziario + template + `immagini/` dentro `corso-godot`.
3. **Nicola carica le immagini** in `manuale/immagini/` e fa push (GitHub Desktop
   o upload da browser). Divisione: Nicola droppa i file, **Claude impagina**.
4. **Claude genera il PDF impaginato definitivo** con le immagini incluse.

**Poi:** invitare la classe · primo giro **branch → Pull Request** (browser) ·
prima **Release** per i ragazzi.

## Struttura cartella `godot/`

```
godot/   (spazio di authoring dentro shiftmanager-web → poi migra nel repo corso-godot)
├── CLAUDE.md                 ← questo file (preferenze corso)
├── README.md                 ← panoramica + concetti base
├── manuale/
│   ├── manuale.md            ← LIBRO DI TESTO (teoria; fonte versionata → PDF)
│   ├── eserciziario.md       ← ESERCIZI a 4 livelli (fonte versionata → PDF)
│   ├── quaderno-studente-TEMPLATE.md ← portfolio personale dei ragazzi (MD+PDF)
│   └── immagini/             ← screenshot richiamati dal manuale
├── chirurgo-pasticcione/     ← primo gioco (backup del progetto vivo)
└── acchiappa-le-stelle/      ← mini-esempio di riferimento

Repo del corso (nicolaregge-pulse/corso-godot) — layout OBIETTIVO:
  main = area autore  ·  Release vX.Y = versione stabile per i ragazzi
  ├── manuale/           (libro di testo + eserciziario + immagini + quaderno template)
  ├── esercizi/          (Fase 1: una sottocartella per esercizio)
  └── progetto-gruppo/   (Fase 2: progetto che evolve con branch/PR/release)
```

## ⭐ Elenco documenti e versioni (indice, aggiornato 04/10/2026)

Ogni documento del corso porta un **numero di versione** nella propria
intestazione (`**Versione X.Y**`). Questo è l'indice di riferimento: quando un
documento cambia si bumpa la versione nella sua intestazione **e** si aggiorna la
riga qui sotto. La fonte di verità della singola versione resta sempre
l'intestazione del file.

### 1. Riferimento e stato
1. `00-STATO-DEL-CORSO.md` — v2.3 (fonte di verità: decisioni e stato)
2. `CORSO-INFORMATICA.md` — v1.17 (super-guida / indice generale)
3. `PROMEMORIA-NICOLA.md` — v0.7 (+ PDF v0.7; cose da fare di Nicola + roadmap cose da sviluppare con Claude)
4. `01-GLOSSARIO.md` — v1.1
5. `REGOLE-NOSTRE-CLAUDE-NICOLA.md` — v2.5 (v2.5 = PPP: «fammeli» vince, se fermo vado avanti; PDF `20261004_Docente_v2.4_...`; v2.4 = tolti i nomi veri di allievi; convenzioni interne Nicola↔Claude: PPP, schema nomi file cronologia/cosa/chi + aree Comune/Docente/Regione, nome deterministico col percorso, conservazione integrale; NON sono le regole per i ragazzi)
5c. `sbobinature/README.md` (+ `TEMPLATE-sbobinatura.md`) — v0.1 (trascrizioni lezioni: conservazione integrale + versione lavorata; alimenta libro di testo, argomenti svolti e note dei ragazzi; nomi solo in scratchpad)
5d. `strumenti/nome-albero.py` (+ `README.md`) — v0.1 (script: nomi file deterministici col percorso nel nome, espandi/collassa l'albero — regola 2.13)
5e. `ATLANTE.md` (+ `ATLANTE-v0.5.pdf`) — v0.5 (v0.5: Valutazione complessiva della classe; mappa unica del corso: tipi di libro A/B/C(3 tagli)/D, Manuale 3 livelli × 3 profondità, 7 tipi-artefatto + nomi 2.13, accrescimento con matrice di copertura e aggiornamenti, due repo/main-Release, documenti del docente, comandi/parole chiave con tabella. Ex "Topologia libri", rimosso)
5g. `METODOLOGIA-CORSO.md` (→ `METODOLOGIA-CORSO-v1.1.pdf`, generatore `strumenti/gen_metodologia.py`) — v1.1 (sintesi da stampare: missione, motore, come si scrive per i ragazzi, giornata di lezione, compito, valutazione, Chiudi classe, documentazione Regione, automazione Git↔script↔Classroom, comandi, dove sta cosa, approvato/da provare)
5f. `RIFERIMENTI-E-DECISIONI.md` — v2.30 (§2.50 prima di proporre ai ragazzi: «Pubblico o vuoi vederlo prima?»; §2.49 lingue 2INF: IT e ZH, niente arabo; §2.48 modo di lavorare: pubblica, istruzioni personalizzate «Il mio punto», segui, traccia Veyon; §2.46 chi ha finito: altre materie o informatica; §2.47 media tecnica separata, non consegnati a 40; §2.45 tutta la suite Google in automatico: coda + ponte `comandi/`, automazione v5; §2.44 voti DIDAweb: materia per argomento trattato, minimo 40; §2.43 lista standard valutazioni per il docente / Valutazione complessiva della classe; §2.42 recupero a fianco: pagine semplificate docs/recupero + elenco docente riservato; §2.41 solo strumenti provati e approvati da Nicola + flusso completo fino all'archivio prove; §2.40 controllo GitHub con ricerca + git clone; §2.39 un solo compito aperto alla volta; §2.38 su Classroom solo il lavoro del giorno; §2.30.4-5 chiusura in pagina privata con un clic, ordine fisso; §2.35 assenti esclusi, §2.36 fuori compito tracciato, §2.37 controlli senza API; §2.34 consegna dei lavori GitHub generata da Claude; §2.33 in classe solo testo compito + link docente; §2.32 Veyon: solo fatti; §2.31 non cancellare PDF in docs/ durante le lezioni; §2.30 comando "Chiudi classe"; §2.28 ogni correzione → registro errori + regola, §2.29 testi Classroom impaginati; §1.10 campanelle, §2.25 registro corto, §2.26 solo il metodo del docente, §2.27 rientri Lazarus; contatti, convenzioni durature, tassonomia libri, dove stanno le cose, aperte; anti-compattamento; NIENTE nomi)

### 2. Pianificazione didattica
1. `MAPPA-ARGOMENTI.md` — v1.5 (aggiunto Google Takeout in Produttività digitale)
2. `MENU-CONTENITORI.md` — v0.1 (menu dei contenitori per i ragazzi: cosa possiamo fare + percorso a imbuto sui 4 anni)
3. `GRIGLIA-ARGOMENTI.md` — v1.17 (argomenti per anno + colonna competenze; Godot: assaggio dopo Lazarus 1ª/2ª, sviluppo 3ª-4ª)
4. `PIANO-ORE-LEZIONE.md` — v0.4 (piano ora-per-ora, 4 anni)

### 3. Regole, standard e organizzazione
1. `REGOLE-FORMATTAZIONE.md` — v1.4
2. `REGOLE-LABORATORIO.md` — v0.1
3. `REGOLAMENTO-STRUMENTI-DIGITALI-IA.md` — v0.2 (v0.2: vietato registrare la voce senza permesso e fare deepfake di voce/volto; regolamento + modulo presa visione/accettazione: strumenti informatici, servizi digitali, IA generativa)
4. `RUOLI-CLASSE.md` — v0.4
5. `STRUTTURA-REPOSITORY.md` — v1.2
5b. `STRUTTURA-REGISTRI-CLASSI.md` — v0.1 (struttura logica delle 4 classi: un Excel per classe con Allievi/Registro voti/Assenze/Allegato A; dati coi nomi solo fuori dal repo; flusso Allegato A)
6. `ORGANIZZAZIONE-GIT-ALLIEVI.md` — v0.4 (repository allievi via Classroom 50)
7. `GUIDA-NOTEBOOKLM-CLASSROOM.md` (→ `GUIDA-NOTEBOOKLM-CLASSROOM-v0.1.pdf`) — v0.1 (guida operativa docente: NotebookLM + creare un compito su Classroom, passo-passo; cosa caricare, cosa far abilitare)
8. `SCHEDA-NOTEBOOKLM-SUBITO.md` (→ `SCHEDA-NOTEBOOKLM-SUBITO-v0.1.pdf`) — v0.1 (scheda pronta "ricetta": solo i passi, la prima volta con NotebookLM, senza spiegazioni)
9. `SCHEDA-DUE-MONDI-CLASSROOM-GITHUB.md` (→ `SCHEDA-DUE-MONDI-CLASSROOM-GITHUB-v0.1.pdf`) — v0.1 (scheda chiara: Classroom vs GitHub vs NotebookLM, chi mette cosa, l'unico ponte a mano)
10. `SCHEDA-TRIADE-NOTEBOOKLM-CLASSROOM-GIT.md` (→ `SCHEDA-TRIADE-NOTEBOOKLM-CLASSROOM-GIT-v0.1.pdf`) — v0.1 (scheda triade: come gestire e lavorare al meglio con i tre; giro completo + esempio concreto)
11. `guida-docenti-alunni-non-italofoni/GUIDA-DOCENTI-ALUNNI-NON-ITALOFONI.md` (+ `guida-docenti.html` → `Guida-Docenti-Alunni-Non-Italofoni-v0.1.pdf`) — v0.1 (guida per gli altri docenti: come gestire le lezioni con alunni che non parlano italiano; principi + pratiche concrete che stiamo facendo + strumenti; esempio del quiz trilingue su Moduli con lo script e come si gestisce)
12. `manuale-docenti/generazione-modulo-google-via-script.md` (+ `.html` → `20260923_Generazione-Modulo-Google-via-Script_IT_v0.2.pdf`) — v0.2 (capitolo manuale docenti: creare un quiz su Google Moduli con uno script Apps Script; esecuzione passo-passo provata in classe, allega su Classroom, come cambiare le domande, errori da evitare)
13. `manuale-docenti/strumenti-didaweb-google/strumenti-didaweb-google.md` (sito `docs/docenti/` con indice e caselle Copia, generatore `gen_sito.py` → `20261007_Strumenti-DIDAweb-Google_Docente_v1.3.pdf`) — v1.3 (segnalibri DIDAweb: Copia HTML, Copia funzioni, Voti v1, Voti AUTO v2, Firma registro v1.2; script «Consegne Classroom → Git»: coda, raccolta, ponte, moduli, voti; pagine collegate; giro della lezione)
14. `INVENTARIO-STRUMENTI-AUTOMAZIONE.md` (→ `20261007_Inventario-Strumenti-e-Automazione_Docente_v1.0.pdf`, con `strumenti/md2pdf.py`) — v1.0 (piattaforme, modalità di lavoro, giro della lezione, automatico / semiautomatico / a mano, lezioni imparate, prossimi passi)
15. `manuale-docenti/gioco-della-classe/guida-docente-gioco-della-classe.md` (→ `20261008_Gioco-Della-Classe_Guida-Docente_v1.1.pdf`) — v1.1 (lezione di ingegneria del software: gioco «Assalto dei mostri» a pezzi, fork, Pull Request, controllo automatico, merge, conflitto, release, grafico Network; il gioco sta in `docs/giochi/assalto-dei-mostri/` del repository del corso)

### 4. Programmi per classe e documenti per la Regione
1. `classe-1/programma.md` — v0.4
2. `classe-2/programma.md` — v0.3
3. `classe-3/programma.md` — v0.2
4. `classe-4/programma.md` — v0.2
5. `PROGRAMMA-PREVENTIVO-2026-27.md` — v0.4 (parti da incollare in Allegato A)
6. `MIE-PARTI-ALLEGATO-A.md` — v0.2 (parti di Regge estratte dai PFP)
7. `ARGOMENTI-SVOLTI.md` — v0.3 (svolto 2025/26, nomenclatura 26/27)
7b. `ARGOMENTI-SVOLTI-2026-27.md` — v0.3 (registro attività svolte 2026/27, agganciato all'Allegato A; si aggiorna a ogni lezione)
7c. `allegato-a-stato/allegato-a-stato.md` (+ `allegato-a-stato.html` → `Allegato-A-Stato-v0.3.pdf`) — v0.3 (Allegato A stato fatto/da fare, da fare in giallo; Classi 1-4; 2/3/4 generate da MIE-PARTI con build_allegato.py)
7d. `allegato-a-2026-27/allegato-a-classe-{1,2,3,4}.md` (→ `allegato-a-classe-N-v0.1.pdf`) — v0.1 (le mie parti Regge mappate per competenza/area, pronte da incollare negli Argomenti del PFP ufficiale; sorgente per compilare poi il docx ufficiale in `programmi-ufficiali/`; generati da `gen_allegati.py`)
8. `programma-svolto/README.md` — v1.0
9. `programma-svolto/_fonti-registro-2025-26/README.md` — v1.0
10. `programmi-ufficiali/README.md` — v0.6

### 5. Manuale (libro di testo + eserciziario)
1. `manuale/manuale.md` — v0.20 (libro di testo)
2. `manuale/eserciziario.md` — v0.15 (esercizi a 4 livelli)
3. `manuale/quaderno-studente-TEMPLATE.md` — v1.0
4. `manuale/immagini/README.md` — v1.0
5. `manuale/_build/README.md` — v1.0

### 6. Materiali della Classe 1
1. `classe-1/README.md` — v1.0
2. `classe-1/MATERIALE-PRONTO.md` — v1.5 (aggiornato con i materiali di settembre 2026)
3. `classe-1/scheda-configuratore-pc.md` — v0.3
4. `classe-1/bussola-mondo-del-lavoro.md` — v0.2
5. `classe-1/da-far-fare-assolutamente.md` — v0.2
6. `classe-1/laboratorio-01-utenze-e-aree.md` — v0.1 (primo lab: login Windows + cartella in rete e account Google + Drive, prova password)
7. `classe-1/laboratorio-02-area-logica-google-classroom.md` — v0.1 (secondo lab: area logica/cartelle ad albero, giro Google Suite, iscrizione a Classroom; ripasso sicurezza)
8. `classe-1/glossario-l2/glossario-l2.md` (+ `glossario.html` → `Glossario-L2-v1.0.pdf`) — v1.0 (glossario multilingue IT · EN · cinese semplificato caratteri+pinyin · arabo; PDF da HTML per i font CJK/arabo)
8b. `classe-1/attivita-blocchi/attivita-blocchi.md` (+ `attivita-blocchi.html` → `attivita-blocchi-v0.1.pdf`) — v0.1 (attività jolly "tempo libero": primo gioco con i blocchi / Ora del Codice; trilingue IT/AR/ZH, a prova di errore, browser)
8c. `classe-1/github-crea-account/github-crea-account.md` (+ `github-crea-account.html` → `20260917_Classe-1-PerTutti_v0.2_Crea-Account-GitHub_multilingua.pdf`) — v0.2 (prima lezione Git: crea account GitHub con email scuola ed entra; trilingue IT/AR/ZH; bottoni per posizione/colore, indirizzi marcati; nota "provare prima i permessi/posta esterna")
8d. `classe-1/consegna-senza-tastiera/consegna-senza-tastiera.md` (+ `.html` → `consegna-senza-tastiera-v0.1.pdf`) — v0.1 (supporto per allievo senza tastiera / che non scrive in italiano: via sicura foglio+foto, via digitale scrittura a mano col mouse; cinese+italiano con disegni; nessun nome di allievo per privacy)
8e. `classe-1/ricerca-github/ricerca-github.md` (+ HTML IT/AR/ZH → `Ricerca-GitHub-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna: piccola ricerca "cos'è GitHub e cos'è un repository", guardando il sito e cercando in rete; si scrive in Google Documenti e si consegna su Classroom; attività di avvicinamento prima di creare gli account; niente login necessario; 3 file monolingui)
8f. `classe-1/costruisci-pc/costruisci-pc.md` (+ HTML IT/AR/ZH → `Costruisci-PC-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna: montare un PC con it.pcpartpicker.com in modalità Builder, componenti compatibili a budget; lista+prezzo in Google Documenti, consegna su Classroom; 3 file monolingui)
8g. `classe-1/componenti-pc-compito/componenti-pc.md` (+ HTML IT/AR/ZH → `Componenti-PC-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna dopo i componenti fisici: spiegare a cosa serve ogni pezzo con parole proprie + domande personali anti copia/AI; consegna su Classroom o foto; 3 file monolingui)
8h. `classe-1/regole-fine-lavoro/regole-fine.md` (+ HTML IT/AR/ZH → `Regole-Fine-Lavoro-IT/AR/ZH-v1.0.pdf`) — v1.0 (regole di laboratorio 'quando hai finito o non hai niente da fare': no giochi/YouTube/rumore, resti al posto, blocca/esci col Ctrl+Alt+Canc, + cosa fare di utile; 3 file monolingui da caricare su Classroom)
8i. `classe-1/libro-di-testo/libro-classe1.md` (+ `_build/libro-classe1.html` → `libro-classe1-v0.6.pdf`) — v0.6 (v0.6: 5.2 lavagna del 09/10, numeri major.minor.patch.build; v0.5: 5.1 versioni, rami, fork, merge del Treno blindato; LIBRO DI TESTO Classe 1: raccoglie appunti/teoria/esercitazioni; cresce a ogni lezione; PDF per leggere, MD per l'AI dei ragazzi)
8i2. `classe-1/utenze-password/utenze-password.html` (→ `20260923_Le-Mie-Utenze-Password_Classe-1-PerTutti_multilingua_v1.0.pdf`) — v1.0 (scheda da compilare a penna: utenze e password di computer scuola/Google/GitHub; trilingue IT/AR/ZH, una pagina, con nota di sicurezza "tienila al sicuro")
8j. `classe-1/accesso-blocco-schermo/accesso-blocco-schermo.md` (+ `.html` → `Accesso-Blocco-Schermo-v1.0.pdf`) — v1.0 (scheda UNICA trilingue: Ctrl+Alt+Canc — login/logout, blocca/sblocca schermo; spiega tutte le voci del menu; con disegno della schermata; separata dalle Regole)
8k. `classe-1/regole-classe/regole-classe.md` (+ `.html` → `Regole-Classe-v1.1.pdf`) — v1.1 (scheda UNICA trilingue: regole di comportamento in classe — alzare la mano ben alta + cenno del docente; attenzione/lavoro con l orologio sulla lavagna, niente YouTube, si aspetta l esercitazione su Classroom)
8l. `classe-1/versioning/versioning.md` (+ `.html` → `Versioning-v2.3.pdf`) — v2.3 (scheda UNICA trilingue: flusso completo delle versioni, major/minor, ripartenza da .0 con nuova linea a ogni release principale; pagine con alberi eterogenei; grafo complesso stile Git a 4 rami paralleli con branch/merge, che termina in 2 versioni principali v1.x e v2.0)
8m. `classe-1/quiz-regole-versioning/` — v1.1 (md v1.1, PDF ancora v1.0; quiz per Google Moduli su Regole della classe + Versioning; `crea-modulo.gs` = script Apps Script che crea il Modulo-quiz in 1 clic, 12 domande trilingui IT/AR/ZH con punteggio automatico; `quiz-regole-versioning.md` + `.html` → `Quiz-Regole-Versioning-v1.0.pdf` = istruzioni passo-passo + chiave risposte per il docente; si allega come Compito su Classroom)
8n. `classe-1/lezione-versioni-treno/lezione-versioni-treno.md` (generatore `_build/gen_lezione_versioni.py` → pagina `docs/lezione-versioni/` + `20261009_Lezione-Versioni-Treno_Classe-1-2-PerTutti_multilingua_v1.0.pdf`) — v1.0 (09/10, 1INF e 2INF: la storia del Treno blindato nel grafo di Git — versione, ramo, fork, Pull Request, merge, minor/major, release; trilingue IT/AR/ZH; la storia si legge dai versioni.json dei giochi)
8o. `treno-blindato-godot/` (export web `docs/giochi/treno-godot/`, ramo Git `treno-godot`) — v2.0 (il Treno della 1INF v1.1 rifatto con Godot 4.7: versione major; dati in `dati/*.json`; grafo `docs/giochi/grafo/` con fork, ramo «immagini» + merge e v2.0)
9. `classe-1/esercizio-presentazione-famiglia/` — v1.2 (esercizio "Io e la mia famiglia": presentazione di sé/famiglia con Google Documenti + consegna su Classroom; passo-passo "a prova di errore" con spiegazione dei 2 link + nota su indirizzi/bottoni nelle 3 lingue. Fonte `esercizio-presentazione-famiglia.md`; **3 file monolingui** `...-IT/AR/ZH-v1.2.pdf` + versione unica trilingue `...-v1.2.pdf` + **versione ILLUSTRATA** `...-IMMAGINI-v1.2.pdf` (disegni con frecce + QR per Classroom, per chi non legge italiano; `esercizio-immagini.html`))
10. `classe-1/negozio-online/GUIDA-RAGAZZI.md` — v1.5
11. `classe-1/negozio-online/PIANO-LEZIONE.md` — v1.1
12. `classe-1/negozio-online/README.md` — v1.0

### 6b. Materiali della Classe 2
1. `classe-2/condizioni-if-then.md` — v0.1 (condizioni SE/ALLORA: IFTTT, funzione SE di Google Fogli, social, Lazarus if/then/else)
2. `classe-2/if-annidati/` (generatori `_build/gen_if_annidati.py`, `gen_cinema.py`; pagina unica `docs/2inf-if/`) — v1.0 (05/10: dispensa if/then/else e if annidati con la regola dei rientri §2.27, riscaldamento R1-R4, gioco Indovina il numero a 4 livelli + compito; 08/10: Il cassiere del cinema, 3 if annidati, or, CheckBox, tabella di prova + compito)
3. `classe-2/lazarus-convertitore/` — v1.0-2.2 (convertitori mph/km/h e temperature, 29/09-01/10) · `classe-2/sicurezza-1ora-rischio-danno/quiz/` — v1.0 · `classe-2/sicurezza-phishing/` — v1.0 (Email sicura o truffa)

### 6c. Materiale trasversale (tutti gli anni)
1. `INTELLIGENZA-ARTIFICIALE.md` — v0.1 (IA: Gem vs Agenti autonomi; con Gemini)
1b. `corso-docente-ai/corso-agenti-gem.md` (→ `20260923_Corso-Agenti-e-GEM_Docente_v1.0.pdf`) — v1.0 (CORSO PER IL DOCENTE su Agenti e GEM: i tre livelli chat/GEM/agente, creare un Gem in Gemini passo-passo, "simulare un professionista", ricettario di 5 Gem pronti da copiare, cenni sugli agenti, regole/privacy, piano in 3 passi; area Docente)
2. `INVALSI-GRADO10-2025-26.md` — v1.1 (analisi dati INVALSI grado 10 2INFSPE; area Sicurezza = solo 4.1/4.2 + mappa 22 quesiti)
3. `RECUPERO-INVALSI.md` — v0.2 (piano recupero lacune DigComp: sicurezza 4.1/4.2 sui 5 temi misurati + comunicazione area 2)
4. `RECUPERO-INVALSI-esercizi.md` — v0.1 (schede + esercizi a scenario + laboratorio pratico: finta mail phishing, wi-fi non sicuro, cookie)
6. `sicurezza-deepfake/` (generatore `_build/gen_deepfake.py`; pagina `docs/sicurezza-deepfake/`, quiz `docs/quiz/?b=sicurezza-deepfake`; PDF IT/AR/ZH; `SCHEDA-DOCENTE-deepfake-v1.0.pdf`; modello di compito Classroom nel riservato `coda/modelli/`) — v1.0 (voci e volti falsi: cos'è, segnali d'allarme, parola d'ordine di famiglia, regole della scuola, cosa fare; tutte le classi)
5. `quiz-recupero-invalsi/index.html` + `README.md` — v1.0 (quiz HTML autocorreggente, 18 scenari; pubblicabile su GitHub Pages)

### 7. Materiali della Classe 3
1. `classe-3/reti-teoria.md` — v0.2
2. `classe-3/esercizi/01-cablaggio-rj45.md` — v0.1
3. `classe-3/troubleshooting-guasti.md` — v0.1 (kit diagnosi guasti: teoria a crocette + guasti fisici) — Panaccione
4. `classe-3/corso-html-css.md` — v0.1 (corso base HTML5/CSS, con pubblicazione su Pages) — Panaccione
5. `classe-3/comunicazione-digitale/comunicazione-digitale.md` (+ `.html` → `Comunicazione-Digitale-v0.1.pdf`) — v0.1 (contenitore "Addetto alla comunicazione digitale" per la terza, nato dai bisogni delle aziende di stage: contenuti/siti/social/Facebook; profilo + competenze + 6 moduli + progetto finale, strumenti browser, legami con e-commerce/HTML-CSS/stage; bozza da confermare)
6. `classe-3/sito-github/` (generatori `_build/gen_sito_github.py` e `gen_sito_github_2.py` → PDF IT e IT-BN; la chiave DOCENTE va nel repo riservato `materiale-docente/`; pagina unica `docs/3inf-sito/` con bottoni Copia ed esempio vivo) — v1.0 (05/10: Dispensa 1 pagina web da zero con index.html + style.css separati, Dispensa 2 pubblicazione su GitHub Pages, Compito primo sito pubblico; 07/10: Dispensa 3 modifica su GitHub, commit e History + Compito 3; 08/10: Dispensa 4 seconda pagina e menu + Compito 4)
7. `classe-3/pagina-html-locale/` — v1.0 (30/09: pagina HTML locale, CSS separato, mini-compiti, sfida finale; IT e IT-BN) · `classe-3/cosa-e-git/` — v1.0-2.1 (Git, versioning; il file IT-BN è `20260925_Classe-3-PerTutti_v1.3_Compito-Git-Versioning_IT-BN.pdf`)
8. `classe-3/sito-github/` 08/10 (generatori `_build/gen_competenze_3inf.py`, `gen_squadra_3inf.py`) — v1.0 (Dispensa 5 + Compito «Il mio portfolio: cosa so fare», rimandato; Dispensa 6 + Compito 4 «Lavoriamo come un'azienda»: il gioco della classe con fork, Pull Request, merge, versioni; IT e IT-BN)

### 7b. Materiali della Classe 4
1. `classe-4/reti-iso-osi/` (generatore `_build/gen_iso_osi.py`; pagina unica `docs/4ti-iso-osi/` con la pagina interattiva Il viaggio di un pacchetto) — v1.0 (06/10: scheda dei 7 livelli + compito Il viaggio del mio messaggio + quiz personale)
2. `classe-4/git-ai-notebooklm/` — v1.0-1.1 (29/09: Git e AI con NotebookLM; la chiave del quiz versioning sta nel repo riservato)
3. `docs/4ti-app/` — v1.0 (06/10: pagina «App di reti» con elenco estendibile; prima app `viaggio-iso-osi.html` «Il viaggio di un messaggio»: teoria dei 7 livelli, simulazione PC A → switch → router → server con byte reali (Ethernet, IP, TCP, FCS calcolati), vista per livello con comunicazione virtuale e percorso reale; un solo file, nessuna libreria; l'esempio usa l'indirizzo vero del sito del corso)

### 7c. Settimana, quiz e pagine del sito
1. `orario/settimana-2026-10-05.md` — v1.0 (orario 5-9/10) · `orario/piano-settimana-2026-10-05.md` (→ `Piano-Settimana-2026-10-05-v1.0.pdf`) — v1.0 (lezione per lezione: materiali, compiti in coda, testi registro ≤40 caratteri)
2. `docs/quiz/` — v1.0 (motore unico del quiz personale: `?b=banca&n=compito&timer=1`; banche in `docs/quiz/banche/`: `4ti-iso-osi`, `2inf-if`, `1inf-sicurezza-1`; uscita da incollare nel Documento, raccolta automatica)
2b. `docs/recupero/` (generatore `strumenti/gen_recupero.py`) — v1.0 (recupero a fianco: pagine semplificate un'azione per passo per 2inf-github, 2inf-indovina, 3inf-sito; senza nomi)
3. `docs/1inf-conversione/` — v1.0 (decimale → binario interattivo, numeri personali, timer) · `docs/1inf-divisioni/` — v1.0 · `docs/1inf-decimale-binario/` (teoria e compiti v1.2-1.4, trilingue)
4. `REGISTRO-ERRORI-CLAUDE.md` — v2.17 · `REGISTRO-ORE-2026-27.md` — v1.1 · `INDICE-GENERALE.md` — v1.0 · `AUDIT-REPOSITORY-2026-10-02.md` — v1.0 · `RETROSPETTIVA-25-09-2026.md` — v1.0 · `SCHEMA-CLASSI-TIPOLOGIE.md` — v1.1 (4TI = classe articolata di 2 gruppi; il gruppo 4INF di Nicola è di 9)

### 8. Altri materiali e prototipi
1. `README.md` (radice) — v1.0
2. `battaglia-navale-3d/README.md` — v1.0

### 9. Libro combinato (generato)
1. `LIBRO-COMPLETO.md` / `LIBRO-COMPLETO-vX.Y.pdf` — v1.74 (assemblato in automatico da `classe-1/_build/`; la versione è `LIBRO_VERSION`; copertina/footer "classi 1,2,3,4" + frontespizio per ogni Parte-classe; include ora il Libro di Testo Classe 1).

### 10. Attestati (non testuali)
1. `attestati/ATTESTATO-RUOLI.html` → `ATTESTATO-RUOLI-v0.4.pdf` (unico PDF, 4 pagine, con logo Piamarta).

## Bobina automatica (07/10/2026, regola di Nicola: «tutte le chat Claude Code devono avere le bobine di tutti i giorni, backuppate»)

1. A ogni fine risposta l'hook `.claude/hooks/bobina-automatica.py` (in `.claude/settings.json`) scrive la
   **bobina integrale del giorno** (un file per giorno e per sessione: `AAAA-MM-GG_bobina_<sessione>.md`),
   salva in `allegati/<sessione>/` le foto e i file arrivati in chat (originali) e fa **commit + push**.
2. Destinazione: `.claude/bobina.json` → `../corso-informatica-riservato/bobine/corso (SOLO nel repository riservato: contiene nomi di minori; se il riservato non è clonato accanto, la bobina non si scrive e compare un avviso)`.
3. Non serve chiederla né esportarla a mano dal file della sessione (chiederlo al modello fa scattare
   il blocco «Messaggio segnalato»). Le bobine fatte a mano restano dove sono.
4. Se compare un avviso «Bobina automatica: …», va sistemato subito e detto a Nicola.
5. Per farla subito, a mano: `python3 .claude/hooks/bobina-automatica.py --sessione-corrente`
