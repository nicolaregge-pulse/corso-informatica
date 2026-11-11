# Il Framework QUIZ: la pagina-lezione con percorso a passi e quiz a metà ora

**Versione 1.1** — 11/11/2026 (v1.1: capitolo 10 Ore di Sicurezza, schema fisso) — prima: 1.0, 04/11/2026 — Prof. Nicola Regge, Laboratorio di Informatica. Area Docente, documento interno (non per i ragazzi).

Nome dato dal docente il 04/11/2026 al tipo di pagina usato per la 1INF in `docs/anteprima/1inf-lazarus-04-11/modulo-1.html` (ora 1, convertitore di misure in Lazarus). Questo documento descrive la pagina com'è, dice quando usarla e come se ne crea una nuova copiando il modello in `docs/modelli/framework-quiz/`. Formato secondo `REGOLE-FORMATTAZIONE.md`. Le sigle: PR (Pull Request, proposta di modifica su GitHub), F5 (tasto che ricarica la pagina), KPI (Key Performance Indicator, indicatore da misurare).

> [GIALLO] **Come si collega a FRAMEWORK-LEZIONE.md:** `FRAMEWORK-LEZIONE.md` è lo scheletro della GIORNATA (prima, durante, dopo, valutazione, registro) e vale sempre. Il Framework QUIZ è un tipo di PAGINA dentro quello scheletro: realizza i punti 02 (la pagina della lezione) e 04 (valutazione) di `FRAMEWORK-LEZIONE.md` per le ore di laboratorio guidato con un quiz. Non lo sostituisce e non cambia nessuna sua regola. Dove i due documenti sembrano dire cose diverse, vale `FRAMEWORK-LEZIONE.md` e `CLAUDE.md`.

## 01 Definizione

1. **Framework QUIZ:** una pagina per ORA di lezione, con un solo indirizzo, che porta il ragazzo da zero a un programma funzionante con passi a una azione per volta, un quiz su Moduli Google a metà ora, la parte «Fallo tuo», il quaderno da ricopiare e la consegna con un bottone.
2. **Perché si chiama QUIZ:** il quiz a metà ora è il momento che misura se il ragazzo ha capito quello che ha appena visto funzionare (motore «Vinci subito, Fallo tuo, Mostralo» e prova del nove). È anche la traccia su Classroom per la Regione (regola 16, regola 33).
3. **Una pagina = una ora.** Più ore dello stesso giorno sono più pagine (`modulo-1.html`, `modulo-2.html`, …) dentro la stessa cartella; le ore successive restano bloccate (capitolo 03, blocco 9).

## 02 Quando si usa

1. Laboratorio guidato in cui i ragazzi producono qualcosa che gira sul PC (per esempio un programma Lazarus) e c'è un concetto da verificare con un quiz.
2. Lezione in cui il docente in aula fa screenshot di Veyon e note e non può controllare le pagine (regola 14): tutto sta sulla pagina e sul cruscotto.
3. Non si usa per la sola teoria a schede (modalità 3 della regola 29 senza lavoro pratico) né per il lavoro con versioning su GitHub (modalità 1): per quelli valgono `REGOLE-COSTRUZIONE-TEORIA.md` e `GIRO-PULL-REQUEST.md`. Il Framework QUIZ si può combinare con un percorso facilitato (massimo 3 passi, regola 29) per chi è in difficoltà.

## 03 Struttura della pagina, blocco per blocco

Nell'ordine in cui compaiono dall'alto. Ogni testo per i ragazzi segue le lingue della classe (capitolo 05).

1. **Riga di contesto.** Una riga piccola in grigio: classe, materia, giorno e data, e la regola di consegna. Esempio reale: «1INF · Laboratorio · mercoledì 04/11/2026 · si consegnano SEMPRE unit1.pas e lo screenshot» (CHECKLIST-LEZIONE §01 punto 10).
2. **Titolo dell'ora** in italiano (h1), arabo (a destra) e cinese, uno sotto l'altro. Esempio: «Ora 1 · Convertitore di misure».
3. **Riquadro giallo F5** (classe `f5`): «La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova», con arabo e cinese. La stessa frase si ripete in fondo alla pagina.
4. **Riquadro azzurro con i 4 bottoni** (`#barra-link`), ognuno con la scritta nelle tre lingue della classe:
   1. «A che punto sono»: il cruscotto dei ragazzi (`cruscotto-ragazzi.html`), con il proprio andamento e quello della classe;
   2. «Monitor della lezione»: la pagina pubblica dei giri Veyon;
   3. «Quiz», in verde (`bt v`): il Modulo Google del quiz; resta spento con il messaggio «Il quiz si apre tra poco: premi F5» finché il suo indirizzo non è in `config.json`;
   4. «Chiedi all'assistente»: porta alla casella in fondo alla pagina.
5. **Riquadro «Chi sei?».** Una casella per nome e cognome. Serve al cruscotto per riconoscere il ragazzo: la pagina manda a ogni passo fatto un segnale con nome, classe, passo, numero di passi fatti, quaderno e quiz. Si memorizza nel browser; nella pagina pubblica compare solo «Nome I.».
6. **Riquadro introduttivo** con la frase di partenza («Non devi scegliere niente: parti dal passo 1»), la barra di avanzamento (`#barra`) e il contatore «Passi fatti: k su N». Eventuali pagine facoltative (per esempio un recupero) si linkano qui e si dichiarano facoltative.
7. **Riquadro rosso «Sei bloccato?».** Dice di scrivere la domanda nella casella dell'assistente in fondo alla pagina e di alzare la mano solo se il PC non funziona (regola 14, controllo `alza_la_mano`).
8. **I passi**, uno per riquadro (classe `passo`), con il bollo «da fare», «ADESSO» (bordo blu) o «FATTO» (bordo verde) e il bottone «Ho fatto!». Regole di ogni passo:
   1. una sola azione che si vede sullo schermo, frase da quinta elementare;
   2. il componente, il menu o il tasto è NOMINATO per intero nel passo (per esempio «nella palette Standard clicca TEdit», non «metti la casella»);
   3. accanto c'è sempre uno schema o uno screenshot (regola 32), con la didascalia «Schema disegnato (non è uno screenshot)» quando è uno schema;
   4. il codice da copiare sta in un riquadro scuro con il bottone «Copia»;
   5. ordine dei passi: 1, **Vinci subito** (poche mosse, quasi impossibile sbagliare, risultato a schermo entro 10 minuti: nel modello è il convertitore km in metri provato con F9); 2, i passi di costruzione, uno per azione; 3, il **quiz** (passo con il bottone verde, 8 domande, 4 minuti, soglia 6 giuste); 4, i passi di allargamento (percorso B); 5, **Fallo tuo** (colore, titolo, una conversione a scelta: scelgono qualcosa di loro); 6, **quaderno da ricopiare** (poche righe in un riquadro giallo `quad`, regola 23); 7, **Salva tutto** (Ctrl+S); 8, screenshot del programma che gira; 9, **consegna** con il bottone «Manda al prof».
9. **Consegna.** Un solo bottone che consegna davvero (pagina `consegna.html?ora=N`, regola 15): mai «copia, apri, incolla». Si consegnano i file dichiarati nella riga di contesto (per Lazarus SEMPRE `unit1.pas` e lo screenshot, MODUS-OPERANDI 03.3).
10. **Ore successive bloccate.** In `<head>` c'è `ore.js` con `data-ora="N"`: la pagina legge `config.json` e si apre solo se `ore_sbloccate` è almeno N; altrimenti mostra «Questa ora non è ancora aperta» e si apre da sola appena il docente alza il numero (30 secondi). Il docente alza UNA ora alla volta con `strumenti/sblocca_ora.py <cartella> N` (regola 31).
11. **Casella dell'assistente** in fondo (`assistente.js`, lingue della classe), con un solo bottone «Manda».
12. **Percorsi.** Ogni passo dichiara per quale percorso vale (`data-perc="A"`, `"B"` o `"AB"`): il percorso A può essere un recupero più breve, il B il percorso pieno. Il cruscotto riceve il percorso scelto.

## 04 Cosa deve avere il cruscotto collegato

1. Un file `cruscotto-ragazzi.html` con il suo `cruscotto-ragazzi.json` nella stessa cartella della lezione, nome e iniziale, senza note riservate (regola 28, CRUSCOTTO-DAL-VIVO.md).
2. Per ogni presente: a che punto è (passo, passi fatti su totale), quiz fatto sì o no e punteggio, consegna ricevuta con i file dentro (letti davvero), da quanto è fermo, che cosa mostra Veyon (fuori compito in rosso), note e uscite, voto proposto 40-80 con il conto (regola 18, regola 13).
3. Colonne dei KPI del giorno proposti a Nicola e confermati (regola 13): per esempio «.pas», «screenshot», «quiz 6 su 8», con ✔ o ✘.
4. Il segnale di avanzamento della pagina (`modo: avanzamento`) deve arrivare al cruscotto: prova con un nome finto prima della lezione.
5. Il cruscotto non mostra MAI dati vecchi senza dirlo: se l'ultimo dato è più vecchio di qualche minuto lo scrive in rosso con l'ora (regola 28). Un cruscotto con tutti i dati «vecchi» in rosso a lezione cominciata è un errore di configurazione, non di lezione (capitolo 08, punto 3).
6. Dati con nomi cifrati nel pubblico (`strumenti/cifra_json.py`, regola 18) e storico a ogni giro nel riservato.

## 05 Cosa deve avere il post su Classroom

1. **Un solo post per l'ora e un solo indirizzo** (regola #164 del registro errori: «i ragazzi fanno casino se diamo URL diversi»): il link della pagina dell'ora. Gli altri indirizzi (cruscotto, monitor, quiz, assistente, consegna) stanno DENTRO la pagina, nei 4 bottoni.
2. **Titolo nel formato «G/M Ora N: argomento breve»**, con N l'ora della classe (CHECKLIST-LEZIONE §06 punto 12). Esempio: «4/11 Ora 1: Convertitore di misure».
3. **La frase F5:** «La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova».
4. **Senza scadenza** (regola 27), un'ora per volta (regola 31): nel post c'è solo il lavoro dell'ora e il testo lo dice.
5. **Lingue per classe:** 1INF italiano, arabo e cinese; 2INF solo italiano (la pagina passa da `strumenti/solo_italiano.py`); 3INF italiano più la riga in bangla solo per il PC 14; 4TI solo italiano (regola 21).
6. **Il Modulo del quiz** è allegato o linkato nel compito se serve come prova (regola 33): il link sta anche nel `config.json` della pagina.
7. Prima di creare il post: `bash strumenti/prima_di_pubblicare.sh "<titolo>"` e lettura di `classroom.compiti`; se il post esiste già si modifica (regola 34).

## 06 Il quiz a metà ora

1. **Dove:** dopo il primo risultato visibile («ora che hai visto che il bottone funziona»), non prima: il ragazzo ha già qualcosa su cui ragionare.
2. **Che cosa:** un Modulo Google in modalità quiz creato col ponte (`forms.crea_quiz`), mai un quiz solo sul sito (regola 33). La copia sul sito serve solo come ripasso.
3. **Quanto e soglia:** 8 domande, 4 minuti, servono 6 giuste. Il numero può cambiare, ma la soglia si scrive sempre nel passo e nel Modulo.
4. **Chi non fa in tempo:** lo fa all'inizio dell'ora dopo; il cruscotto lo mostra come «quiz da fare», non come errore.
5. **Chiave nel `config.json`:** `quiz_<argomento>` con l'indirizzo `viewform` del Modulo; la pagina attiva da sola i bottoni verdi (uno nei 4 bottoni, uno nel passo).
6. La lettura delle risposte entra nella situazione quiz della classe (regola 18, `situazione_quiz.py`) e nel voto proposto.

## 07 Controlli prima di dare il via

Si aggiungono a `CHECKLIST-LEZIONE.md` (controllo nuovo §06 punto 14: «la pagina rispetta il Framework QUIZ») e a `FRAMEWORK-LEZIONE.md` capitolo 07.

1. Tutti i blocchi del capitolo 03 ci sono, nell'ordine. Nessun segnaposto `{{...}}` rimasto nel file.
2. **Ogni bottone si apre davvero**: cruscotto, monitor, quiz, assistente, consegna, recupero. Si prova clic per clic sul sito vero dopo «PUBBLICATO» (regola 12), non solo in locale, e dopo Ctrl+F5 (#75, #118).
3. Il quiz è un Modulo vero, con il suo indirizzo in `config.json` e il bottone verde attivo (#173).
4. Lingue della classe controllate (regola 21); per la 2INF `solo_italiano.py` passa.
5. `node --check` sugli script e prova in Chromium senza errori JS (#80, #118).
6. `ore_sbloccate` vale 1: le ore dopo sono chiuse (regola 31).
7. Il post Classroom ha un solo indirizzo, il titolo nel formato giusto e nessun doppione (#164, #174, #194).
8. Il codice dei passi è provato come lo fanno i ragazzi, nella stessa sequenza, su un Lazarus vero; se non è provato lo si dice (#175).
9. Il cruscotto riceve il segnale di un nome finto e mostra i dati con l'ora di oggi.
10. Piano B pronto: «Se il bottone non funziona: …» sulla pagina (CHECKLIST §01 punto 11).
11. Verifica finale con `verifica_lezione.py <CLASSE>`: solo con VERDE si dice «pubblicato» (CHECKLIST §02 punto 6).

## 08 Errori già visti il 04/11/2026, da non ripetere

1. **Bottoni senza verifica dei link.** I 4 bottoni sono stati messi nella pagina senza aprirli uno per uno: un indirizzo sbagliato o un Modulo non ancora creato lascia il ragazzo con un bottone morto. Regola: si aprono tutti, dalla pagina pubblicata, prima del via (capitolo 07 punto 2).
2. **Componente non nominato nel passo.** Un passo che dice «metti il bottone» senza scrivere TButton e la palette Standard fa perdere chi non sa dove cercare. Regola: nel passo si scrive il nome esatto del componente, della palette, della proprietà (Caption, Text) e dove si trova nell'Ispettore oggetti.
3. **Dati del cruscotto «vecchi» in rosso.** Il cruscotto dei ragazzi mostrava tutto come dato vecchio perché il giro automatico non aveva ancora scritto il JSON di quell'ora (campo `generato` e `ora` fermi alle 09:43 mentre la lezione era già in corso). Regola: prima della campanella un giro di prova vero, e `generato` aggiornato a ogni giro (#152, #153).
4. **Errore del debugger di Lazarus a 64 bit con F9.** Premendo F9 compare una finestra di errore del debugger e il programma non parte. Non è un errore del ragazzo. Soluzione, da mettere sulla pagina nel passo F9 e da dire all'assistente: premere Ctrl+S (Salva tutto), poi aprire a mano il programma dalla cartella del progetto con doppio clic sul file `.exe` (per esempio `project1.exe`). Il programma gira lo stesso e lo screenshot si fa uguale.
5. **Consegna incompleta.** In una esercitazione Lazarus si consegnano SEMPRE `unit1.pas` e lo screenshot; la riga di contesto in alto lo ripete per non dimenticarlo.

> [BLU] **Da confermare:** il punto 4 è stato scritto dal rapporto del docente del 04/11/2026. Non c'è ancora una voce nel registro degli errori: da aprire quando il docente conferma la soluzione.

## 09 Come si crea una nuova lezione copiando il modello

1. Copiare la cartella `docs/modelli/framework-quiz/` in `docs/anteprima/<classe>-<argomento>-<GG-MM>/` (stessa convenzione delle anteprime); rinominare `modello.html` in `modulo-1.html` (uno per ora).
2. Sostituire tutti i segnaposto `{{...}}` (elenco nel file `docs/modelli/framework-quiz/README.md`). Cercare con `grep -n "{{" modulo-1.html`: deve restare zero.
3. Disegnare o inserire lo schema di ogni passo in `img/` (il modello contiene solo schemi segnaposto) e togliere i passi che non servono: ogni passo deve avere la sua immagine.
4. Creare il Modulo del quiz col ponte e scrivere il suo indirizzo in `config.json` sotto la chiave scelta (`{{CHIAVE_QUIZ}}`).
5. Preparare `cruscotto-ragazzi.html` e `cruscotto-ragazzi.json` per la classe e mettere in `config.json` l'indirizzo `invio` del segnale di avanzamento e `attivo: true`.
6. Eliminare il file `README.md` e togliere `modello.html` dalla copia: la pagina pubblicata ha `noindex` e non porta il nome del modello.
7. Per la 2INF e la 4TI togliere arabo e cinese e passare da `strumenti/solo_italiano.py`; per la 3INF mettere la riga in bangla solo per il PC 14.
8. Eseguire il capitolo 07, poi pubblicare (regola 27, 31), `bash strumenti/aspetta_pubblicazione.sh`, link ai ragazzi solo dopo «PUBBLICATO».

## 10 Ore di Sicurezza: schema fisso

Regola data dal docente l'11/11/2026, per la Sicurezza di 1INF e delle altre classi che la fanno.

1. **Sempre la stessa storia:** un'ora nuova più il recupero delle ore precedenti, per assenza o per voto sotto l'80%.
2. **Domande:** ogni ora ha un banco di domande più largo del quiz; si fanno due versioni, A e B, e ogni tanto si alternano o si cambiano.
3. **Moduli sempre aperti a più tentativi** della stessa prova, anche quando sarebbe il caso di cambiare le domande. La Fabbrica lo impone già (`setLimitOneResponsePerUser(false)` in `fabbrica/motore.js`). Vale il tentativo migliore.
4. **Titoli del registro:** li mette la direzione e fa fede il registro; Allegato A in doppia modalità, «Dichiarato» e «Registro» (R5.2bis, `ARGOMENTI-SVOLTI-2026-27.md` capitolo 4b).
5. **Recuperi:** l'elenco per allievo sta nel riservato (`report/AAAA-MM-GG/recuperi-sicurezza-<classe>.md`); nel pubblico mai nomi.

## 11 Registro delle versioni

1. **v1.0 (04/11/2026):** prima versione, dal tipo di pagina usato in 1INF il 04/11/2026 (ora 1, convertitore di misure) e battezzato «Framework QUIZ» dal docente. Modello in `docs/modelli/framework-quiz/`.
2. **v1.1 (11/11/2026):** capitolo 10 «Ore di Sicurezza: schema fisso», su regola del docente.
