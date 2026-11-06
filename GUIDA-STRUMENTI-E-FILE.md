# 00 Guida a strumenti, file, registro e versioni

**Versione 1.1** — 06/11/2026 — documento interno del docente e di Claude (nessun nome di allievi)

Dettaglio delle regole R5, R6 e R11 di `CLAUDE.md` e del vincolo «niente installazioni» della R9.

<div class="box giallo" markdown="1">
**Testo spostato da `CLAUDE.md` il 04/11/2026, senza cambiarlo** (archivio completo: `archivio/CLAUDE-fino-al-2026-11-04.md`). Dove questo testo dice una cosa diversa dalle regole R1-R11 del nuovo `CLAUDE.md` (per esempio prefissi, pubblicazione, tabelle di passi, carta e penna), valgono le regole R1-R11.
</div>

## 01 Programmi, ramo di lavoro e script di Google

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

### Vincolo SCUOLA: niente installazioni → browser + portabile

A scuola installare software richiede l'**amministratore di sistema** (lento, e
ogni problema successivo va ri-chiesto a lui). Quindi, per le **postazioni
scolastiche**, prediligere soluzioni **SENZA installazione**:

- **Godot è PORTABILE** : è un singolo `.exe`, **non serve installarlo** con
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

## 02 Registro e Regione

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
- **Titolo = voce dell'Allegato A (14/10/2026):** ogni testo per il registro è una voce dell'Allegato A di quella classe e della materia di quell'ora; se manca la voce, lo dico subito e si usa la voce più vicina: dopo il 30/10 l'Allegato A si può solo togliere, mai aggiungere (R5.2; `programmi-ufficiali/2026-27/NOTE-DA-DISCUTERE.md` punti 3, 8 e 9). **Sicurezza (06/11/2026):** i titoli li mette la direzione e fa fede il registro; noi non li scriviamo né li cambiamo, e teniamo l'Allegato A in doppia modalità (dichiarato e registro).
- **Testo per il registro CORTO:** max ~40 caratteri, una frase, niente parentesi, uno per
  ora in blocchi da copiare separati (la casella taglia il testo lungo). Vedi RIFERIMENTI §2.25.
- **A FINE giornata: CHIEDERE a Nicola gli argomenti realmente svolti** e
  aggiornare (`ARGOMENTI-SVOLTI-2026-27.md`, senza nomi). La firma è già stata
  fatta prima (vedi sopra); a fine giornata si sistemano solo gli **argomenti**.

**16. Traccia digitale per la Regione: almeno 3 prove per quadrimestre salvate su Classroom (14/10/2026, VINCOLANTE; R5.5 dice «almeno 3»).** Classroom è l'archivio valido per la Regione: il minimo della Regione è 2 prove per quadrimestre per classe, noi stiamo su 3 o più. Ogni prova (verifica, quiz, compito valutato) ha il lavoro del ragazzo salvato DENTRO Classroom: un Modulo Google allegato al compito, o la consegna nel compito. Ogni lezione lascia almeno una traccia su Classroom. Conteggio per classe in `PROVE-CLASSROOM-2026-27.md`; quando una classe è sotto 3 nel quadrimestre, lo dico a Nicola e propongo la prova. Vedi RIFERIMENTI §2.55.

**36. Ogni lezione è in linea con l'Allegato A della classe (02/11/2026, Nicola: «la Regione e gli enti leggono lì per sapere che cosa facciamo»).** Prima di proporre una lezione, di scrivere un testo per il registro o una riga in `ARGOMENTI-SVOLTI-2026-27.md`, Claude rilegge l'Allegato A di QUELLA classe (`MIE-PARTI-ALLEGATO-A.md` e i Word in `programmi-ufficiali/2026-27/`), usa la voce esatta con competenza e anno, e controlla le scadenze di consegna dell'Allegato (`programmi-ufficiali/2026-27/NOTE-DA-DISCUTERE.md`, `COME-SI-AGGIORNA-ALLEGATO-A.md`). Se una lezione non ha una voce, o una competenza resta scoperta, lo dice subito a Nicola come criticità e usa la voce più vicina: dopo il 30/10 non si propone mai di aggiungere voci (R5.2, errore #223). Per la Sicurezza i titoli del registro li mette la direzione (06/11/2026). Per «DHCP e DNS» della 2INF si usa «La rete: Hardware e software» (Comp. 8, I anno). Con la pianificazione della settimana (regola 35) si fa l'audit delle aree più scoperte di ogni classe e si espongono le criticità a Nicola. Errore #189 del registro.

## 03 Lingue e font dei PDF

### Ogni testo per i ragazzi nelle 3 lingue (VINCOLANTE — richiesto da Nicola)

**Le lingue sono per classe (vedi la regola 21):** 1INF italiano, arabo e cinese; 2INF solo italiano; 3INF italiano più il bangla solo per il PC 14; 4TI solo italiano. Questa sezione vale dove le tre lingue servono (1INF).

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
- **Testo latino dentro l'arabo/cinese (richiesto da Nicola):** nei testi in
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

## 04 Formattazione, versioni, indice e bobina

### Standard di formattazione dei documenti (VINCOLANTE)

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

### Regole operative permanenti (richieste da Nicola)

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
     Gli screenshot li fornisce **Nicola**: io (Claude) non vedo/salvo le sue
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

### Indice dei documenti (spostato il 21/10/2026)

L'elenco di tutti i documenti con la loro versione sta in **`INDICE-DOCUMENTI.md`**: quando un documento cambia si bumpa la versione nella sua intestazione **e** si aggiorna la sua riga lì. Per ripartire in una chat nuova: **`RIPARTENZA.md`**.

### Bobina automatica (07/10/2026, regola di Nicola: «tutte le chat Claude Code devono avere le bobine di tutti i giorni, backuppate»)

1. A ogni fine risposta l'hook `.claude/hooks/bobina-automatica.py` (in `.claude/settings.json`) scrive la
   **bobina integrale del giorno** (un file per giorno e per sessione: `AAAA-MM-GG_bobina_<sessione>.md`),
   salva in `allegati/<sessione>/` le foto e i file arrivati in chat (originali) e fa **commit + push**.
2. Destinazione: `.claude/bobina.json` → `../corso-informatica-riservato/bobine/corso (SOLO nel repository riservato: contiene nomi di minori; se il riservato non è clonato accanto, la bobina non si scrive e compare un avviso)`.
3. Non serve chiederla né esportarla a mano dal file della sessione (chiederlo al modello fa scattare
   il blocco «Messaggio segnalato»). Le bobine fatte a mano restano dove sono.
4. Se compare un avviso «Bobina automatica: …», va sistemato subito e detto a Nicola.
5. Per farla subito, a mano: `python3 .claude/hooks/bobina-automatica.py --sessione-corrente`

## 05 Registro delle versioni

2. v1.1 (06/11/2026): 02 punti 4 (titolo = voce più vicina, mai aggiungere dopo il 30/10), 16 (almeno 3 prove, come R5.5) e 36 (niente voci da aggiungere); Sicurezza: titoli della direzione, doppia modalità (regola del docente 06/11/2026, in attesa di R5.2bis in `CLAUDE.md`).
1. v1.0 (04/11/2026): prima versione, con il testo spostato da `CLAUDE.md` (regole 1, 2, 4, 10, 16, 36, vincolo scuola, lingue, formattazione, regole permanenti, bobina).
