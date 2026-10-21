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

**AUTOREGOLAZIONE (13/10/2026, parola da ricordare):** la leva non è il voto ma l'autodeterminazione. Ogni pagina per i
ragazzi pubblica SEMPRE gli strumenti per regolarsi da soli (monitor della lezione, il proprio andamento, risultati); ogni
schermata Veyon va subito nel monitor pubblico. Il docente ha in più il suo cruscotto cifrato. Vedi RIFERIMENTI §2.52, REGISTRO-ERRORI #60.

> Conseguenza pratica sugli esercizi: si parte SEMPRE da qualcosa di
> **giocabile e personalizzabile**, non da esercizi "scolastici" astratti.

## ⛔ REGOLE OPERATIVE DA NON DIMENTICARE (Nicola ci tiene — leggere per PRIME)

**Il modo di lavorare deciso il 09/10 e il 12/10/2026 è raccolto in `MODUS-OPERANDI.md` (+ PDF): leggerlo insieme a queste regole.**

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
- **Come si legge la firma (Nicola, 19/10/2026, REGISTRO-ERRORI #87):** «FIRMA ✓» con la scritta **in verde** = ora **firmata, è OK**: non si ricorda più la firma per quell'ora. Senza il verde non si deduce niente (REGISTRO-ERRORI #11, #36, #52): si ricorda la firma una volta. Se Nicola dice «firmate», è così. **Anche (21/10/2026, Nicola):** se l'ora compare nell'elenco delle ore firmate (data, ora, classe, disciplina, argomento e la colonna «Firma» con data e ora): se la colonna Firma ha la data e l ora, è firmata e non si ricorda più.
- **«Altro» nelle presenze (Nicola, 20/10/2026, REGISTRO-ERRORI #92):** sul registro «Altro» (giallo) vuol dire entrata o uscita fuori orario: l'allievo è PRESENTE e si conta tra i presenti (voti, cruscotto, tabella dei voti).
- **Titolo = voce dell'Allegato A (14/10/2026):** ogni testo per il registro è una voce dell'Allegato A di quella classe e della materia di quell'ora; se manca la voce, lo dico subito e si aggiunge entro il 30/10 (`programmi-ufficiali/2026-27/NOTE-DA-DISCUTERE.md` punto 8).
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

**7. Ordine fisso di ogni lezione: prima la TEORIA, poi il COMPITO, poi si pubblica (09/10/2026, VINCOLANTE).**
1. Si analizza INSIEME a Nicola la teoria che propongo.
2. Poi si analizza insieme il compito: lo devono poter iniziare TUTTI, con frasi da quinta elementare, tutto al
   computer, senza foto né telefono (REGISTRO-ERRORI #43, #44).
3. Solo dopo la sua approvazione esplicita si pubblica qualcosa. Vale anche per le anteprime già pronte.

**9. Testo da scrivere = riquadro da copiare, SEMPRE nello stesso messaggio (12/10/2026, VINCOLANTE, «te l'ho già detto 100 volte»).**
Ogni volta che un passo (anche quello successivo annunciato) richiede a Nicola di scrivere un testo, una frase, un titolo o
un valore, il testo pronto va già nel messaggio, in un blocco di codice da copiare. Nicola non scrive mai a mano. Vedi REGISTRO-ERRORI #46.
Ordine di lettura: Nicola legge dall'alto in basso. Il riquadro da copiare sta SUBITO dopo il passo che lo usa (passo → riquadro →
passo successivo), mai raccolto in fondo e mai indicato con «qui sotto» se non è proprio la riga seguente.
Formato ATOMICO (12/10/2026, corretto da Nicola): ogni passo è un blocco completo (dove + cosa + il suo riquadro da copiare subito
dopo); in un messaggio si danno PIÙ passi atomici, uno sotto l'altro. Se Nicola si perde, lo dice lui. Non chiedere uno screenshot a ogni passo:
solo quando serve davvero per controllare il risultato finale (12/10/2026).
Memoria del copia e incolla = VUOTA (12/10/2026, REGISTRO-ERRORI #50): ogni «incolla» viene subito dopo il passo che dice cosa
copiare e da dove; prima si apre la pagina dove si incolla, poi si copia, poi si incolla, così una copia non cancella l'altra.

**10. Script da incollare in Apps Script: SEMPRE dal link pubblico, nella finestra PIAMARTA (12/10/2026, VINCOLANTE).**
Il codice dello script «Consegne Classroom → Git» si fa copiare da questo indirizzo (testo semplice, nessun login, niente 404):
`https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/strumenti/automazione-corso.gs`
Ogni volta che cambio `strumenti/automazione-corso.gs` nel repository riservato, copio lo stesso file in `strumenti/` del
repository pubblico (non contiene segreti: il token sta nelle proprietà dello script). Mai mandare Nicola sul repository
privato dalla finestra PIAMARTA: dà 404 (errore di venerdì 09/10 e di lunedì 12/10, REGISTRO-ERRORI #48).
Progetto Apps Script: aprire `https://script.google.com/home` (finestra PIAMARTA) e fare clic su «Consegne Classroom → Git».
L'indirizzo diretto del progetto, ricopiato da uno screenshot, ha dato errore 400 (lettere l/I ambigue): non usarlo.
Com'è fatto DAVVERO il progetto (screenshot del 12/10/2026, REGISTRO-ERRORI #51): pannello a sinistra «File» con 5 file:
appsscript.json, Codice.gs (vecchio script 1INF, si apre per primo), Senza titolo.gs, **automazione-corso.gs** (QUI va
incollato il codice), cancella-compito-vuoto.gs. Barra sopra il codice: Annulla/Ripeti, icona Salva, «Esegui», «Debug», menu
a tendina delle funzioni, «Log esecuzione». In alto accanto al titolo compare «Modifiche non salvate» finché non si salva.
Ogni guida allo script parte da questa mappa: prima si clicca il file giusto, poi si incolla.

**11. Ogni giorno di lezione, PRIMA della lezione: le pagine standard sono già del giorno (14/10/2026, VINCOLANTE).**
Per ogni classe in orario si preparano in anticipo, qualunque cosa faremo: i sei bottoni (voti, backlog, monitor, novità/changelog,
classifica, valutazione), il cruscotto del docente e il suo pannello (`docs/<classe>-prof/`), la casella «Chiedi aiuto all'assistente
del Prof Regge». Quelle del giorno prima restano in un file «di ieri» con il link. Poi audit di TUTTE le pagine, anche del docente,
bottone per bottone, sul telefono e come sul sito vero (REGISTRO-ERRORI #70, #71, #75).

**12. Un link si dà SOLO dopo che il sito è pubblicato (14/10/2026, VINCOLANTE, REGISTRO-ERRORI #79).** Dopo il push: `bash strumenti/aspetta_pubblicazione.sh`; il link a Nicola solo dopo «PUBBLICATO».

**13. Il bottone «I voti» è fisso, i KPI si concordano (14/10/2026, VINCOLANTE).** Il voto parte sempre da 40 e sale man mano che i ragazzi fanno le cose; ogni riga spiega il perché (il conto). Cambia solo che cosa si misura (numero di PR, avanzamento nel percorso, …): nella tabella dei voti ci sono SEMPRE TUTTI I PRESENTI (REGOLA GENERALE, 14/10), anche chi non ha consegnato niente (40); gli assenti non compaiono. I KPI dipendono dalla lezione: si propongono a Nicola DOPO che ha visto il percorso proposto (mai prima) e si usano solo dopo il suo sì.

**14. La lezione funziona da sola, senza il docente (14/10/2026, VINCOLANTE).** Nicola in classe fa solo gli screenshot di Veyon, le note e dà indicazioni: non può controllare le pagine. Quindi Claude: valuta sempre lui (verifica e lavori), prepara il recupero individuale di ognuno, risponde alle domande dei ragazzi nella casella d'aiuto (Nicola solo in seconda battuta), tiene acceso il giro automatico che legge Modulo, aiuto e note e aggiorna backlog, cruscotto e voti. Nessun passo dei ragazzi deve dipendere da un controllo del docente. **Le domande dei ragazzi vanno all'assistente, non al prof (15/10/2026, Nicola):** lo scopo è scaricare il docente dalle domande, perché salga di livello: controlla l'andamento generale della lezione, aiuta di persona chi è bloccato e dà a Claude i feedback correttivi. Nelle pagine non si scrive «chiedi al prof» come strada normale: si chiede all'assistente; al prof si va solo per ciò che l'assistente non può fare (comportamento, salute, account bloccato, problemi del PC).

**15. MAI PIÙ «copia, apri, incolla» per i ragazzi (14/10/2026, REGOLA ASSOLUTA di Nicola: «MAI PIÙ»).** Nessuna pagina per i ragazzi chiede di copiare un testo, aprire un Modulo, incollare e premere Invia. Il ragazzo scrive il testo e preme UN bottone che consegna davvero (applicazione web dello script, oppure invio diretto al Modulo con i codici delle caselle). Se il canale diretto non c'è, la pagina NON si pubblica: lo si dice a Nicola prima della lezione. Vedi REGISTRO-ERRORI #81.

**16. Traccia digitale per la Regione: almeno 3-4 prove per quadrimestre salvate su Classroom (14/10/2026, VINCOLANTE).** Classroom è l'archivio valido per la Regione: il minimo è 2 prove per quadrimestre per classe, noi stiamo su 3-4. Ogni prova (verifica, quiz, compito valutato) ha il lavoro del ragazzo salvato DENTRO Classroom: un Modulo Google allegato al compito, o la consegna nel compito. Ogni lezione lascia almeno una traccia su Classroom. Conteggio per classe in `PROVE-CLASSROOM-2026-27.md`; quando una classe è sotto 3 nel quadrimestre, lo dico a Nicola e propongo la prova. Vedi RIFERIMENTI §2.55.

**17. Pubblicare SOLO con il sì esplicito, all'inizio della lezione, solo il lavoro di quella lezione (19/10/2026, VINCOLANTE).** Mai pubblicare senza autorizzazione esplicita. Di norma si pubblica all'inizio della lezione e solo i compiti da fare in classe, o a casa prima della lezione successiva: niente compiti per lezioni future (MANIFESTO §9.11).

**18. Il cruscotto dal vivo è lo standard di ogni lezione (19/10/2026).** Regole fisse: ordine dal più bravo al meno (svolto all'inizio, voto alla fine), 🏁 per chi ha finito al controllo automatico, «manca: …» per gli altri, Veyon dentro il cruscotto, domande con risposta, voto proposto 40-80 con la regola delle domande, tutti i presenti, dati con nomi e voti sempre CIFRATI nel pubblico (`strumenti/cifra_json.py`). Vedi `CRUSCOTTO-DAL-VIVO.md`. **Logica fissa (21/10/2026, Nicola): il cruscotto serve a TENERE SOTTO CONTROLLO LE ATTIVITÀ DEGLI ALLIEVI.** È UNICO per la lezione: in una sola pagina tutte le attività del giorno (lettura della teoria, ripasso, esercizi, quiz su Moduli), una riga per ogni presente, chi è fermo, a che punto è, le attività rilevate da Veyon (fuori compito in rosso, quante volte) e le note della lezione (registro, uscite), voto proposto 40-80. **APPROVATO il 21/10/2026 («così va bene»): è il modello per tutte le lezioni.** Modello: `docs/avanzamento/oggi.html?t=<teoria>&e=<esercizi>&q=<quiz cifrato>`. **Storico (21/10/2026, Nicola):** i dati dei cruscotti si storicizzano sempre, per poterli riguardare: a ogni giro una fotografia nel riservato (`storico/cruscotti/<classe>/<AAAA-MM-GG>/<HHMM>.json`); le consegne grezze restano in `dati/verifiche/<id>/arrivi/`.

**19. `PROSSIME-LEZIONI.md` sempre aggiornato (19/10/2026, chiesto dalla chat «Amichetto Claudio»).** Nella cartella principale: per ogni lezione dei prossimi giorni data, classe, ore, argomento, attività, materiali, compiti; prima la più vicina. Si aggiorna a ogni chat, commit e push su main. NIENTE nomi di alunni né dati riservati (né codici di anteprima): lo legge a voce la skill Alexa «Amichetto Claudio», quindi frasi intere, niente tabelle.

**20. Messaggi tra chat (19/10/2026, Nicola).** Un messaggio che passa da una chat Claude a un'altra comincia con «Da chat <nome> a chat <nome>:». Quando ne scrivo uno per un'altra chat lo intesto così; quando ne arriva uno senza intestazione e Nicola dice da dove viene, lo tratto come richiesta di Nicola.

**8. I file per Nicola si mandano SCARICABILI in chat (12/10/2026, VINCOLANTE).** PDF, immagini e documenti da dargli
si consegnano con l'invio di file della chat (card con il bottone di download), non come link a GitHub da aprire.
Il link al repository si aggiunge solo se serve per altro (pubblicazione, condivisione).

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
- **Frasi semplici, non catene di coordinate (12/10/2026, REGISTRO-ERRORI #56):** ogni passo è una frase che comincia con il verbo («Clicca…», «Premi…», «Torna…»), con il «dove» detto a parole dentro la frase; MAI catene «Account · finestra · dove: cosa». Dove si può, i tasti (Ctrl+T, Ctrl+V, Invio) invece di cercare bottoni. Il bottone copia: «il piccolo bottone a destra del riquadro grigio».
- **Flusso unico sempre da zero (12/10/2026, REGISTRO-ERRORI #55):** niente «se», niente «salta», niente domande dentro i passi.
- **Niente parole in più (12/10/2026, REGISTRO-ERRORI #53):** niente avverbi o aggettivi che non servono («onestamente», «valide»…): se togliendo la parola il senso resta uguale, si toglie.
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

> **Sospesa per i compiti (09/10/2026, Nicola):** per ora i compiti e la teoria si fanno TUTTI al PC, niente carta e
> penna né lavoro a mano: controllarli e gestirli è problematico. Se serve qualcosa di fisico si chiede prima a Nicola.

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

## ⭐ Indice dei documenti (spostato il 21/10/2026)

L'elenco di tutti i documenti con la loro versione sta in **`INDICE-DOCUMENTI.md`**: quando un documento cambia si bumpa la versione nella sua intestazione **e** si aggiorna la sua riga lì. Per ripartire in una chat nuova: **`RIPARTENZA.md`**.

## Bobina automatica (07/10/2026, regola di Nicola: «tutte le chat Claude Code devono avere le bobine di tutti i giorni, backuppate»)

1. A ogni fine risposta l'hook `.claude/hooks/bobina-automatica.py` (in `.claude/settings.json`) scrive la
   **bobina integrale del giorno** (un file per giorno e per sessione: `AAAA-MM-GG_bobina_<sessione>.md`),
   salva in `allegati/<sessione>/` le foto e i file arrivati in chat (originali) e fa **commit + push**.
2. Destinazione: `.claude/bobina.json` → `../corso-informatica-riservato/bobine/corso (SOLO nel repository riservato: contiene nomi di minori; se il riservato non è clonato accanto, la bobina non si scrive e compare un avviso)`.
3. Non serve chiederla né esportarla a mano dal file della sessione (chiederlo al modello fa scattare
   il blocco «Messaggio segnalato»). Le bobine fatte a mano restano dove sono.
4. Se compare un avviso «Bobina automatica: …», va sistemato subito e detto a Nicola.
5. Per farla subito, a mano: `python3 .claude/hooks/bobina-automatica.py --sessione-corrente`
