# Registro degli errori di Claude ("SBIRRO") — Corso Informatica

**Versione 2.15** — 08/10/2026

*Registro onesto degli errori che Claude commette, giorno per giorno, con la correzione
adottata e la regola nata di conseguenza. Serve a non ripeterli e a migliorare. Lo tiene
aggiornato Claude su richiesta di Nicola: a ogni nuovo problema si aggiunge una voce con la
data. NON contiene nomi di allievi (quelli restano nel repo privato).*

---

## 01/10/2026 — Chiusura compito Classe 2INF (Convertitore temperature)

1. **Pacchetto unico con i dati di tutti (privacy).**
   - Cosa: ho consegnato un solo ZIP con dentro i libri di tutti gli allievi + la griglia con
     tutti i voti + il monitoraggio, **senza protezione**. Aperto lo ZIP, si vedevano tutti i
     file di tutti e i documenti riservati del docente.
   - Perché è sbagliato: i dati di un allievo non devono mai stare in un file accessibile agli
     altri; i documenti del docente non vanno mescolati a ciò che può arrivare ai ragazzi.
   - Correzione: ZIP unico **ma** con i libri **cifrati, una password per allievo**, e i
     documenti docente cifrati con una password docente. → RIFERIMENTI §2.14.

2. **"Valutazione del docente" non autorizzata.**
   - Cosa: nei libri degli allievi avevo messo una sezione "Valutazione del docente", mentre
     Nicola non li aveva valutati lui.
   - Perché è sbagliato: non si attribuisce al docente un giudizio che non ha dato.
   - Correzione: la valutazione la dà l'AI, intitolata **"Valutazione dell'AI"**. → RIFERIMENTI §2.15.

3. **Sovra-correzione: avevo tolto del tutto la valutazione.**
   - Cosa: dopo l'errore 2, avevo tolto voto e giudizio dai libri.
   - Perché è sbagliato: il ragazzo deve avere voto e giudizio (utili), solo attribuiti all'AI.
   - Correzione: rimessa la valutazione come "dell'AI". → RIFERIMENTI §2.15 (v1.9).

4. **Standard del compito incompleto (mancava l'anti-plagio e il report completo).**
   - Cosa: la prima chiusura non seguiva lo standard della Classe 3 (mancavano anti-plagio,
     dossier evidenze col testo reale, report complessivo a più sezioni) e usava voti /100.
   - Correzione: 5 documenti docente (scheda valutazione, dossier evidenze, report complessivo
     con anti-plagio + indicazioni ragazzi + segnalazioni, griglia, incrementale), voti **/10**.

5. **Frainteso il problema di privacy segnalato.**
   - Cosa: alla segnalazione "senza password tutti vedono tutto" ho risposto con opzioni
     tecniche invece di capire subito l'accordo mancato (separazione + attribuzione corretta).
   - Correzione: prima capire la regola mancata, poi agire.

6. **Anti-plagio troppo assertivo all'inizio.**
   - Cosa: avevo scritto "ha copiato" per screenshot/testi simili.
   - Perché è sbagliato: possono essere lo **stesso account su 2 PC**; va verificato.
   - Correzione: sempre al condizionale ("da verificare") finché non confermato.

7. **Contenuto del libro dell'allievo da delimitare.**
   - Cosa: rischio di mettere nel libro del ragazzo indicazioni pensate per il docente.
   - Correzione: nel libro va tutto ciò che riguarda **lui** (lavoro, valutazione AI, come ha
     lavorato/monitoraggio su di lui, anti-plagio su di lui), **tranne** le indicazioni
     specifiche per il docente (prossimo passo, strategia di recupero).

8. **Password casuali che cambiano a ogni rigenerazione.**
   - Cosa: avevo generato le password dei libri in modo **casuale**; rigenerando lo zip (per
     un'altra correzione) sono cambiate, diverse da quelle già consegnate agli allievi.
   - Perché è sbagliato: una password consegnata deve restare **stabile** per sempre.
   - Correzione: password **fisse** (hardcoded) nel generatore; non cambiano più a nessuna
     rigenerazione.

9. **Password messa anche sui documenti del docente.**
   - Cosa: avevo cifrato anche griglie/report del docente. Nicola non deve sbloccare i propri
     documenti.
   - Perché è sbagliato: la password serve solo a separare i libri tra allievi; i documenti del
     docente li legge lui, devono essere **aperti**.
   - Correzione: cifratura **solo** sui libri degli allievi; documenti docente aperti (incluso
     il foglio riepilogo password).

10. **Non ho versionato lo ZIP finale di chiusura.**
    - Cosa: ho generato il deliverable finale (lo ZIP di CHIUDI CLASSE 2INF) e l'ho consegnato
      senza metterlo su Git.
    - Perché è sbagliato: regola di Nicola "tutto versionato"; il deliverable finale va
      conservato com'è stato consegnato.
    - Correzione: lo ZIP di chiusura si **archivia nel repo PRIVATO** (`dati/chiusure/<CLASSE>/`,
      force oltre il `.gitignore`), perché contiene nomi → mai nel pubblico. → RIFERIMENTI §2.5.

11. **Proposto argomenti senza il report delle lezioni precedenti.**
    - Cosa: ho suggerito argomenti per la Classe 1 senza prima dare il quadro di **cosa era
      stato fatto** nelle lezioni precedenti.
    - Perché è sbagliato: le proposte vanno ancorate allo svolto; Nicola deve vedere prima il
      report del fatto.
    - Correzione: **sempre** prima il report "lezioni precedenti" (dal registro svolti), poi le
      proposte. → RIFERIMENTI §2.16.

12. **Introdotto un argomento NON spiegato in classe (direzione inversa).**
    - Cosa: nella dispensa bit/byte ho aggiunto **decimale→binario**, mentre in classe (lavagna)
      si era fatto **solo binario→decimale**. Può confondere i ragazzi.
    - Perché è sbagliato: il materiale deve seguire la lezione reale; introdurre argomenti nuovi
      di mia iniziativa non va bene ("se Nicola avesse voluto, lo avrebbe fatto alla lavagna").
    - Correzione: **integrare** sì, **introdurre argomenti nuovi** solo dopo **confronto**; nel
      dubbio chiedo. Inoltre: la **foto della lavagna** va dentro la dispensa di teoria.
      → RIFERIMENTI §2.17, §2.18, §7.

13. **Cancellato una versione invece di tenerla.**
    - Cosa: rifacendo la dispensa bit/byte, ho **rimosso** i PDF v1.0 sostituendoli con la v1.1.
    - Perché è sbagliato: le versioni sono **congelate** e si **tengono**; si **bumpa sempre**,
      non si cancella la precedente (regola di Nicola "aumenta sempre versione").
    - Correzione: ripristinata la v1.0; d'ora in poi le versioni si accumulano, non si eliminano.

## 01/10/2026 — Compito bit/byte (grafica diversa dalla dispensa)

14. **Grafica del compito DIVERSA dalla dispensa → ragazzi persi.**
    - Cosa: la dispensa usava la griglia a valori posizionali con gli 1 in verde; il compito
      l'avevo fatto con una **tabella diversa** (prima come Google Doc semplice, poi con una
      griglia solo "simile"). I ragazzi non hanno riconosciuto la stessa cosa e si sono persi.
    - Perché è sbagliato: materiali dello stesso argomento che i ragazzi vedono in sequenza devono
      avere la grafica **identica**, non "simile". Il cambio di grafica li confonde.
    - Correzione: compito rifatto con la griglia **identica** alla dispensa, **gestita come
      immagine** (PNG dalla stessa fonte → identica ovunque: PDF/Classroom/stampa), con **sotto lo
      spazio per i conti a mano**. Nasce la regola → RIFERIMENTI §2.19.

---

## 02/10/2026 — 1INF, pubblicazione del compito in classe

1. **Automazione spiegata a metà, scoperta in classe (GRAVE).** Il ponte provato era solo
   Classroom → Git; per PUBBLICARE (Git → Classroom) serve comunque uno script che parte
   dall'account scuola (un Esegui o un timer). Non l'ho detto quando abbiamo progettato il ponte:
   Nicola l'ha scoperto con 20 ragazzi in attesa, che hanno aspettato oltre 10 minuti.
   **Correzione:** (a) dire SUBITO i limiti di ciò che costruisco (cosa resta a Nicola); (b) il
   setup una tantum (timer) si fa FUORI dalla lezione, mai in classe; (c) in classe serve sempre
   una **via rapida pronta** (link/caselle per creare il compito a mano in 1 minuto), consegnata
   insieme ai materiali.
2. **Passi non "solo copia-incolla".** Il passo "apri il progetto Apps Script" era senza link.
   **Correzione:** ogni passo che apre un sito parte da un **link in una casella da copiare**.
3. **Via rapida senza il documento da compilare.** Nella pubblicazione a mano ho messo solo PDF
   (da leggere) e non il **Google Doc da compilare** ("una copia per ogni studente"), che invece c'era
   nello script automatico. I ragazzi non avevano dove scrivere. **Correzione:** ogni compito ha
   SEMPRE il documento da compilare allegato come copia per ogni allievo, in qualunque via di
   pubblicazione (automatica o a mano).
4. **Metodo alternativo introdotto ("metodo delle monete").** Per aiutare chi faticava ho proposto
   un secondo metodo invece di semplificare quello della lavagna: ha confuso i ragazzi. **Correzione:**
   ritirato (v1.0 tolte dal sito), rifatte facilissima / scheda facile / nome-colori v1.1 solo con le
   divisioni per 2. Regola → RIFERIMENTI §2.26.
5. **Orari delle campanelle persi.** Nicola li aveva dati in una sessione precedente; non li avevo
   salvati in un file, quindi ho fissato scadenze "a caso" (14:00, 13:00) e ho dovuto chiederli di
   nuovo in classe. **Correzione:** salvati in RIFERIMENTI §1.10 + `orario/Orario-Campanelle-v1.0.pdf`;
   ogni dato operativo che Nicola mi dà va scritto SUBITO in un file del repo.
6. **Troppe modifiche ai materiali DURANTE la lezione.** In un'ora: monete → divisioni, pagina
   con 4 → 2 → 6 → 12 → 4 bottoni, PDF v1.0 → v1.1 → v1.2 → v1.3 → v1.4. Ogni cambio ha spostato
   il terreno sotto i piedi dei ragazzi e di Nicola ("li hai confusi"). **Correzione:** durante la
   lezione si CONGELA ciò che è pubblicato; si corregge solo un errore bloccante, con UNA modifica
   ragionata, non a tentativi.
7. **Argomenti mescolati.** La scheda sulla divisione (Livello 3) parlava già di binario; ho poi
   proposto un compito unico "dalla divisione al binario". Nicola: "tieni distinti gli argomenti".
   **Correzione:** un argomento = una teoria + un compito; il ponte tra due argomenti è un compito
   a sé, dopo.
8. **Impaginazione non controllata prima di consegnare.** Tabella delle metà tagliata ai bordi,
   tabella del Livello 3 spezzata su due pagine, titoli orfani a fine pagina, "37" senza spiegazione
   di cosa fare. Nicola l'ha visto prima di me. **Correzione:** prima di pubblicare guardo OGNI
   pagina di OGNI lingua (render a immagine), non solo la prima.
9. **Link rotti nelle istruzioni di Classroom.** Ho tolto dal sito i PDF v1.0 che erano linkati
   direttamente nelle istruzioni del compito → link non funzionanti. **Correzione:** nelle istruzioni
   di Classroom SOLO il link unico della pagina (che non cambia mai); mai link diretti ai PDF versionati.
10. **Pagina vecchia rimasta nel browser.** Dopo le modifiche Nicola vedeva ancora la versione
    precedente (cache): ho dato per scontato che "ricaricare" bastasse. **Correzione:** versione
    scritta in copertina (riquadro bianco) + pagina senza cache + avviso esplicito "Ctrl+F5".
11. **Compiti vuoti pubblicati dallo script (GRAVE).** Ho messo in coda "aggancia il compito che
    creerà Nicola" PRIMA che lui lo creasse: lo script non lo ha trovato e ha pubblicato da solo
    "Compito 1" e "Compito 2" VUOTI, visibili ai ragazzi e non eliminabili dalla vista Stream.
    **Correzione:** si aggancia un compito manuale solo DOPO che Nicola conferma "creato"; lo script
    va dotato di uno stato "solo-aggancia" che non pubblica mai.
12. **Consiglio sbagliato: modificare un compito durante la lezione.** Sono stato IO a consigliare di
    trasformare i compiti vuoti modificandoli mentre i ragazzi lavoravano. Classroom ha spostato il
    Compito 2 in cima, sopra il Compito 1: i ragazzi hanno perso l'ordine. Non era da fare: bastava
    lasciarli stare e usarli DOPO, a fine lavoro sul Compito 1. **Correzione:** prima di
    far modificare un compito già pubblicato, avvisare che sale in cima e dare subito "Sposta in alto"
    per rimettere l'ordine (o usare un Argomento ordinato).
13. **Indicazioni imprecise su schermate e account.** "Elimina" dato per possibile dove non c'era
    (Stream), passaggi multipli in un solo messaggio quando Nicola chiedeva "una cosa per volta",
    dubbio sull'account (scuola/personale) gestito male. **Correzione:** UNA azione per messaggio
    quando la situazione è nuova; leggere lo screenshot e indicare il punto ESATTO di quella schermata.
14. **Chiave di correzione sovrascritta.** Rigenerando il compito v1.1 ho sovrascritto la chiave
    della v1.0 che i ragazzi stavano consegnando (rimessa a posto subito). **Correzione:** ogni chiave
    porta la versione nel nome del file; mai sovrascrivere la chiave di un compito in corso.
15. **Compito bit/byte v3.0 di ieri con esempio sbagliato** (griglia di 78, somma scritta
    "128+64+32+16 = 78"). Visto solo oggi. **Correzione:** controllo aritmetico automatico degli
    esempi (somma ricalcolata) prima di generare il PDF.

**Causa comune di oggi:** ho privilegiato la velocità e i tentativi rispetto alla verifica, e ho
cambiato materiale già in mano ai ragazzi. **Regola d'oro da qui in avanti:** *in classe niente
esperimenti: si pubblica una volta, verificato pagina per pagina; le migliorie si fanno dopo la
lezione.*

---

*(Le prossime giornate si aggiungono qui sotto con la loro data.)*

## 05/10/2026 — 3INF, istruzioni del compito su Classroom

1. **Errore:** ho dato a Nicola il testo delle istruzioni del compito come **un unico paragrafo lungo** (tutte le 5 parti in una riga). Su Classroom risulta un blocco illeggibile per i ragazzi ("formattazione pessima").
2. **Regola:** i testi da incollare su Classroom vanno **già impaginati**: titoletti in maiuscolo, una riga per passo, numeri 1. 2. 3., le parti del Documento una per riga, riga vuota tra i blocchi. Mai frasi lunghe con 1) 2) 3) in linea.
3. **Regola generale (chiesta da Nicola):** tutto ciò che Nicola segnala va qui **e** in una regola (RIFERIMENTI §2.28-2.29), per non rifarlo più.
4. **05/10, 08:45 — link rotto "2. Su internet" (scheda facile 2).** Passando alla v1.1 ho cancellato da `docs/` il PDF v1.0: chi aveva la pagina vecchia nel browser cliccava un link che non esisteva più. **Regola (RIFERIMENTI §2.31):** in `docs/` le versioni già usate in classe **non si cancellano mai** durante la giornata; la pagina punta alla nuova, la vecchia resta raggiungibile.
5. **05/10, 09:15 — allievo giudicato "fermo" dalla sola miniatura di Veyon.** Del PC 26 avevo detto "non ha iniziato" perché la miniatura mostrava la pagina del compito; in realtà il suo sito era già online. **Regola (RIFERIMENTI §2.32):** dalla miniatura si dice solo "sulla pagina X alle HH:MM", mai "non ha fatto niente"; prima di un giudizio si controllano le schede aperte e la pagina dei siti.
6. **05/10, 10:00 — risposte troppo lunghe durante la lezione.** Nicola deve seguire i ragazzi e non riesce a leggere tabelle e spiegazioni. **Regola (RIFERIMENTI §2.33):** in classe la risposta è SOLO (a) il testo aggiornato e completo del compito da incollare su Classroom, in un unico blocco copia, e (b) il link per il docente in un blocco copia. Niente tabelle o spiegazioni se non chieste.
7. **05/10, 10:05 — ho fatto preparare il Documento ai ragazzi.** Era deciso che la consegna (link, codice, screenshot) la preparo io leggendo il sito da GitHub. Io invece ho continuato a scrivere "metti nel Documento il link e il codice". **Regola (RIFERIMENTI §2.34):** quando un lavoro è su GitHub, la consegna la genera Claude (`generatori/siti_3inf.py`). Il ragazzo pubblica il sito, preme solo "Consegna" su Classroom e poi viene interrogato. Chi non ha il sito online deve arrivarci, oppure il docente detta il suo nome utente.
8. **05/10, 10:10 — bangla mostrato a tutti.** Il bangla serve solo all'allievo del PC 14; mostrarlo a tutti confonde gli altri. **Regola:** le traduzioni si mostrano solo a chi servono (pagina per PC: bangla solo sul PC 14). Per gli altri, la pagina resta solo in italiano.
9. **05/10, 10:05-10:02 — pagina "Controlla" rotta per un apostrofo.** Ho scritto "l'account" dentro una stringa JavaScript tra apici singoli: lo script non partiva e la lista restava vuota. Poi la cache del browser ha continuato a mostrare la versione rotta. **Regola:** dopo ogni modifica a una pagina con script, controllo la sintassi (`node --check`) e la provo nel browser prima di pubblicare. Al docente do il link con `?v=` e l'ora, così il browser non usa la pagina vecchia.
10. **05/10, 11:00 — nella pagina della 2INF c'erano anche i lavori dei giorni dopo.** La pagina linkata nel compito di oggi mostrava anche il quiz del 07/10 e il cassiere del cinema dell'08/10: troppa roba, i ragazzi si confondono. **Regola:** la pagina della classe mostra SOLO il lavoro del giorno. I materiali dei giorni dopo si preparano ma restano nascosti e compaiono solo il loro giorno.
11. **05/10, 11:36 — firma data per mancante.** Dallo screenshot del registro ho scambiato il bottone "FIRMA ✓" per una firma ancora da fare; Nicola aveva già firmato. **Regola:** su DIDAweb la prova è la casella "Visualizza tutte le firme arretrate": se il calendario non mostra giorni evidenziati, non manca nessuna firma. Prima di dire "manca la firma" chiedo di guardare lì, non deduco dal colore del bottone.
12. **05/10, 11:45 — file della coda rotto da un conflitto di Git.** Mentre lo script di Classroom salvava il suo stato, io ho riscritto lo stesso file: nel rebase sono rimasti i segni del conflitto e il JSON non si leggeva più, bloccando il giro dello script. Riparato in pochi minuti. **Regola:** dopo ogni rebase nel repo riservato controllo che tutti i `coda/*.json` si leggano (`json.load`) prima di pushare; nei conflitti sui file della coda riscrivo il file intero, non prendo un lato a caso.
13. **05/10, 11:50 — due compiti pubblicati insieme.** Ho messo su Classroom subito sia il primo lavoro (programma su GitHub) sia il secondo (Indovina il numero): i ragazzi non hanno capito quale fare per primo. **Regola (RIFERIMENTI §2.39):** su Classroom c'è UN solo compito aperto alla volta. Il secondo si prepara in coda e si pubblica solo quando Nicola dice che la classe ha finito il primo. Il titolo dice sempre l'ordine ("1 di 2", "2 di 2") e le istruzioni del secondo iniziano con "PRIMA finisci ...".
14. **05/10, 12:00 — istruzioni GitHub poco chiare e pagina rigenerata male.** Per pubblicare il programma Lazarus avevo scelto il copia-incolla del codice (Ctrl + A, Ctrl + C, Create new file): né Nicola né i ragazzi l'hanno capito; Nicola si aspettava il caricamento dei file da GitHub web. In più, rigenerando la pagina, il generatore ha rimesso in vista dispensa e compito degli if, che dovevano restare nascosti. **Regole:** 1) per caricare file su GitHub si usa il metodo standard **Add file → Upload files → choose your files**, salvo diversa indicazione di Nicola; nel dubbio si chiede PRIMA di scrivere i passi. 2) Dopo ogni rigenerazione di una pagina della classe si apre la pagina nel browser di prova e si controlla che si veda SOLO il lavoro di oggi (numero di riquadri) prima di pubblicare.
15. **05/10, 12:08 — istruzione "seleziona unit1.pas, unit1.lfm…" impossibile da seguire.** Sui PC della scuola Windows nasconde le estensioni: i ragazzi vedono due "unit1" e due "project1" e non sanno quali prendere. **Regola:** mai chiedere di riconoscere un file dall'estensione. Per scegliere più file si dà un bottone COPIA con i nomi tra virgolette (es. "unit1.pas" "unit1.lfm"), da incollare nella casella "Nome file" della finestra di Windows.
16. **05/10, 12:15 — "nessuno ha caricato" detto senza verificare bene.** Cercavo i lavori indovinando nomi utente e il nome esatto `lazarus`, e leggendo con raw (con cache): Picco aveva caricato in `lazarus-`, Castelletta e Moussa avevano caricato dopo il mio controllo. **Regola (RIFERIMENTI §2.40):** ricerca GitHub dei repository creati oggi + `git clone`; mai dire "non ha caricato" senza il clone.
17. **05/10, sera — file da scaricare poco chiari.** Ho mandato lo zip dei libri protetti intero (troppo grande, 31 MB) e poi le 2 parti: Nicola si è trovato 4 file senza sapere quali scaricare. **Regola:** se un file supera il limite, lo divido PRIMA e mando solo le parti; nel messaggio dico esattamente quali file scaricare e quanti sono.
18. **05/10, sera — voti di Indovina calcolati prima della raccolta dei Documenti e due errori nel correttore.** Ho chiuso la classe alle 13:51, prima della raccolta delle 13:56: mancavano i punti del Documento. In più il correttore abbinava il Documento per pezzo di cognome ("abdel" trovava anche Abdelfattah) e contava le domande del modello vuoto come risposte. **Regole:** 1) la chiusura si fa DOPO l'ultima raccolta delle consegne; 2) gli abbinamenti allievo ↔ file si fanno su parole intere di tutto il cognome; 3) dal Documento si conta solo il testo scritto dal ragazzo, tolte le righe del modello.
19. **06/10, 08:30 — «nessun guasto segnalato prima» detto senza la fonte giusta.** Per il PC 33 ho detto che non c'erano segnalazioni precedenti: in realtà era già nella segnalazione all'assistenza del 28-29/09, che non era salvata nel repository. **Regola:** tutte le segnalazioni all'assistenza si salvano nel repo riservato (`dati/manutenzione/`, con il registro dei guasti); prima di dire «mai segnalato» si controlla lì e, se manca qualcosa, si chiede al docente. A ogni lezione si verifica se i guasti aperti esistono ancora.
20. **06/10, 08:10-09:10 — lista «Cose da fare» pubblicata rotta.** Aggiungendo una voce ho sostituito il blocco dei dati con una ricerca automatica che ha preso anche il codice della pagina: la pagina non partiva più. **Regola:** quando si ripubblica una pagina che si salva da sola, il blocco dei dati si sostituisce una volta sola e in un punto preciso; prima di pubblicare si controlla il codice e si apre la pagina in un browser di prova.
21. **06/10, mattina — report dei voti trattenuto per un PPP.** Nicola aveva chiesto «dammi il report con tutte le valutazioni»; i messaggi PPP successivi ne precisavano il contenuto, ma io ho risposto «te lo do al tuo avanti». Nicola: «smettila con avanti, se ti dico di farmeli fammeli». **Regola (Regole nostre, PPP punti 5-6):** se un risultato è stato chiesto, il PPP successivo ne cambia solo il contenuto e il risultato si consegna appena è pronto; e un PPP non mi tiene mai fermo: se non sto facendo niente, vado avanti.
22. **06/10, mattina — doppioni nella griglia 1INF del 03/10.** Tre colonne erano lo stesso voto contato due volte (GitHub e repository = Ricerca GitHub, Il versioning = Quiz Regole + Versioning, Config. PC teoria = Esercizio Hardware) e mancava «Configurare un PC» del 24/09; il voto complessivo comunicato stamattina ne risente di qualche punto. **Regola:** prima di fare una media si controlla che ogni colonna sia un lavoro diverso (stesse cifre su tutta la classe = doppione) e si confronta l'elenco delle colonne con l'elenco dei compiti su Classroom.
23. **06/10, 09:30 — materia del voto scelta solo dall'ora.** Per DIDAweb ho assegnato il Quiz Regole + Versioning a Laboratorio perché era l'ora di Laboratorio; l'argomento (regole) è Sicurezza. Inoltre davo voti sotto 40. **Regola (RIFERIMENTI §2.44):** la materia si sceglie in base all'argomento realmente trattato; il voto minimo è 40.
24. **06/10, 12:20 — quiz su Moduli ancora da far partire a mano.** Nicola mi aveva chiesto giorni fa che anche i quiz su Moduli si creassero in automatico, come i compiti su Classroom; non l'avevo fatto e gli ho dato di nuovo uno script da eseguire. **Regola:** quando Nicola chiede di automatizzare un passaggio, l'automazione si costruisce subito nello script automatico (oggi: versione 4, quiz su Moduli con risultati depositati nel repo riservato) e si segna nell'elenco delle cose da fare; mai più passaggi a mano che si possono fare da soli.
25. **07/10, 08:50 — password dei libri 2INF diverse tra una chiusura e l'altra.** Per la 2INF esistevano due liste di password (quella del 25/09 e quella fissa del 01/10): i libri del 05/10 e la prima versione di quelli del 07/10 usavano la lista del 25/09, mentre l'elenco dato a Nicola era quello del 01/10, che in più non aveva 3 allievi. Nicola se n'è accorto perché un allievo risultava senza password. **Regole:** 1) per ogni classe c'è UNA sola lista di password, nel repo riservato (`strategico/password/`, file «Password-UNICA»), e tutti i generatori leggono solo quella; 2) prima di consegnare uno zip protetto si prova ad aprire OGNI libro con la password dell'elenco che ha Nicola; 3) a chi non ha ancora una password si prepara il bigliettino.
26. **07/10, 09:10 — nomi dei file dei libri che iniziano con la descrizione.** I libri si chiamavano «Libro-Tutti-i-Lavori_Cognome…»: su Classroom si vede solo l'inizio del nome del file, quindi i ragazzi vedevano tutti lo stesso «Libro-Tutti-i-Lavori_A…» senza capire quale fosse il loro. Nicola l'aveva già chiesto. **Regola:** ogni file personale di un ragazzo inizia con **Cognome-Nome**, poi classe, poi descrizione e data (es. «Cognome-Nome_2INF_Tutti-i-miei-lavori_07-10-2026.pdf»); vale per tutti i generatori.
27. **07/10, 12:15 — PDF delle password vuoto mandato senza controllo.** Il PDF dei bigliettini della 3INF conteneva solo la pagina di errore di Chrome (percorso del file sbagliato), e l'ho mandato senza aprirlo. **Regola:** ogni PDF si apre e si controlla il contenuto (testo atteso presente) PRIMA di mandarlo; il generatore dei PDF usa sempre percorsi assoluti.
28. **07/10, 12:00 — segnalibro DIDAweb provato solo su una pagina finta.** Due errori scoperti solo in classe: la finestrella di Chrome accetta una riga sola (la lista su più righe non funzionava) e su DIDAweb i nomi e le caselle stanno in tabelle separate. **Regola:** uno strumento per un sito esterno si costruisce partendo dall'HTML VERO della pagina (fatto copiare dal docente, salvato solo nel repo riservato) e si prova su quella copia prima di darlo a Nicola.
29. **07/10, 12:35 — link al repository riservato dato per il profilo «Scuola».** Lo stesso 404 del 06/10: nel profilo Chrome della scuola GitHub non è collegato. **Regola:** i link al repository riservato si danno SEMPRE con il passo «apri il profilo personale di Chrome» prima; mai un link nudo.
30. **07/10, 12:20 — lo stesso lavoro contato due volte (3INF).** «Pagina HTML» ed «Esercitazione pagina HTML» erano lo stesso lavoro in due caselle di Classroom: chi l'aveva consegnato in una risultava «non consegnato» (40) nell'altra. **Regola:** prima di una griglia si confrontano i compiti di Classroom tra loro (stesso argomento, stessa data, consegne complementari = stesso lavoro, una colonna sola con il voto migliore) e, per ogni «non consegnato», si controlla anche GitHub.
31. **07/10 — riferimenti a messaggi precedenti invece delle caselle da copiare.** Nicola: «devi darmi tutte le caselle per il copia e incolla senza farmele cercare». **Regola:** ogni messaggio con passi da fare contiene TUTTE le caselle da copiare che servono a quei passi, anche se già date prima.
32. **07/10, 12:40-12:55 — aggiornamento dello script con un flusso inutilizzabile (15 minuti persi).** Ho dato passi che facevano passare da un account all'altro e copiare un indirizzo DOPO aver copiato lo script (così gli appunti si perdevano); poi ho rimesso in chat tutto lo script (550 righe) invece di dire che era già negli appunti. **Regole:** 1) mai far copiare due cose in sequenza se la seconda cancella la prima: gli indirizzi si scrivono a mano o si aprono PRIMA di copiare; 2) prima di dare i passi si controlla cosa Nicola ha già (appunti, schede aperte) e si parte da lì; 3) lo script automatico si aggiorna da solo da GitHub (caricatore): Nicola non incolla più codice, dopo l'ultima volta.
33. **07/10, 13:00 — «la password del tuo libro» senza dire dove sta il libro (3INF).** L'annuncio e la pagina della password parlavano del «libro dei voti», ma i libri con le indicazioni personali erano solo nello zip del docente: non erano mai stati dati ai ragazzi, che hanno chiesto «dove sono le istruzioni personalizzate?». In più il «consiglio del prof» era una frase uguale per livello, non davvero personale. **Regole:** 1) prima di nominare un materiale in un testo per i ragazzi, si controlla che i ragazzi lo abbiano già e si scrive DOVE trovarlo (Classroom, quale compito o materiale); 2) la consegna dei libri ai ragazzi fa parte della chiusura (zip → Classroom) e va indicata a Nicola come passo esplicito; 3) le indicazioni «personalizzate» citano almeno una cosa concreta di quel ragazzo (un lavoro, un errore, un passo successivo).
34. **07/10, 12:55-13:00 — annuncio pubblicato DUE volte su Classroom (3INF).** Lo script ha pubblicato l'annuncio alle 12:55 ma non è riuscito a segnare «eseguito» nel repository, perché nello stesso momento io avevo spinto un altro file (lettura delle risposte): al giro dopo lo ha ripubblicato. **Regole:** 1) mentre un comando che PUBBLICA (annuncio, compito) è in attesa, non si spinge nient'altro nel repository riservato finché non risulta «eseguito»; 2) la sorveglianza automatica si ferma prima di un annuncio e riparte dopo; 3) da fare nello script: prima di pubblicare un annuncio, controllare se ce n'è già uno con lo stesso testo (come già fa per i compiti).
35. **07/10, 13:52-14:01 — zip per i ragazzi non consegnato prima della campanella (3INF).** Nicola ha chiesto lo zip alle 13:52; io ho aspettato bloccato fino a 9 minuti la raccolta automatica dello script per avere gli screenshot, senza dare niente nel frattempo e senza leggere i suoi messaggi («sono 13:57», «2 minuti»). Risultato: classe finita senza zip. **Regole:** 1) a fine ora si consegna SUBITO quello che c'è (bozza con i dati disponibili, segnata come bozza) e si aggiorna dopo; 2) mai attese bloccanti di più di 1 minuto durante la lezione: le attese vanno in background; 3) lo zip per i ragazzi è pronto 10 minuti prima della campanella (per l'ultima ora: alle 13:50), con i dati di quel momento.
36. **07/10, 16:30 — RIPETIZIONE dell'errore 11: firma data per mancante dal bottone «FIRMA ✓» (3INF).** Leggendo l'HTML del Registro di corso ho scritto a Nicola che le ore 5 e 6 «non risultavano firmate» perché c'era il bottone «Firma ✔»; Nicola le aveva firmate in classe. Il bottone resta anche sulle ore firmate (serve a rifirmare dopo aver cambiato l'argomento). In più il segnalibro «Firma registro» v1.0 usava proprio la presenza del bottone per capire se un'ora era firmata. **Regole:** 1) prima di dire qualcosa sulle firme si rilegge la regola 11: la prova è «Visualizza tutte le firme arretrate» o «Da firmare», mai il bottone; 2) uno strumento che deve riconoscere uno stato (firmato / non firmato) si costruisce con un esempio VERO di ENTRAMBI gli stati, chiesto al docente prima di consegnarlo; 3) il segnalibro non decide da solo che un'ora è «da firmare»: mostra lo stato che legge e chiede conferma.
37. **08/10, 09:21 — «lo script è fermo» detto senza prova (2INF).** Nessun commit dello script da ieri alle 14:02 e il compito non ancora su Classroom: ho concluso che lo script era fermo e ho fatto segnare il compito «da creare a mano», togliendolo alla coda. In realtà lo script non aveva niente da fare (i compiti di oggi erano in attesa dell'OK) e il compito era in coda da meno di un giro (5 minuti); rimesso in coda, è uscito alle 09:25. Risultato: 5 minuti persi e rischio di compito doppio. **Regole:** 1) prima di dire che lo script è fermo si manda un comando di prova (`classroom.compiti`) e si aspetta un giro intero (5-6 minuti); 2) un compito in coda non si toglie dalla coda finché la prova non dice che lo script è fermo; 3) al docente si dice subito «esce entro 5 minuti», non «non funziona».

## 08/10/2026 — 2INF, «Il treno blindato»: per un'ora e mezza quasi nessuno ha consegnato (#38)

1. **Cosa è successo.** Fino alle 10:10 le consegne erano zero; la prima consegna vera è arrivata dopo l'annuncio degli investitori, quasi tutti hanno consegnato solo con il compito «idea e difetto» delle 10:35.
2. **Errori miei.**
   1. Ho mescolato due canali: le pagine spiegavano fork e Pull Request vere su GitHub, il compito chiedeva le consegne su Classroom. I ragazzi non sapevano dove consegnare.
   2. Ho fatto consegnare solo il capo squadra: tutti gli altri non avevano un lavoro da consegnare e si sono fermati.
   3. Il primo lavoro obbligatorio con un orario è arrivato tardi; prima c'erano solo «lavori da fare» senza scadenza.
   4. Ho aperto troppi canali (due moduli, pagine, annunci): i moduli hanno avuto zero risposte.
   5. Ho letto i Documenti tardi: all'inizio aspettavo il bottone «Consegna».
3. **Regola (vale da oggi, per tutte le classi).** In un progetto di squadra: (1) un solo canale, il Documento del compito su Classroom; (2) ogni punto del Documento è una Pull Request che Claude legge, integra e pubblica come versione nuova; (3) TUTTI consegnano, ognuno nel suo Documento, con fasi a orario (una ogni 20-25 minuti) e una frase da completare già scritta; (4) la prima fase scade entro 20 minuti dall'inizio; (5) Claude legge i Documenti ogni 5 minuti fin dall'inizio, anche senza «Consegna», e pubblica i numeri di PC che non hanno ancora consegnato; (6) niente GitHub per i ragazzi se non è il lavoro del giorno.

## 08/10/2026 — 3INF, «Il treno blindato della 3INF»: errori in classe (#39)

1. **Orari sbagliati.** Ho scritto le fasi a partire dalle 11:20 senza controllare l'ora vera (erano le 12:00): ho dovuto rifare gli orari tre volte (12:05-13:50, poi fino alle 13:30, poi fino alle 13:05). Regola: prima di scrivere un orario per i ragazzi si chiede l'ora di fine al docente e si parte dall'ora di adesso.
2. **Istruzioni troppo lunghe e poco chiare.** La prima versione spiegava tutto (Pull Request, fasi, voto) ma non diceva COSA fare e COME in un passo solo: i team non hanno capito. Regola: la pagina per i ragazzi mostra una sola cosa da fare adesso, con passi numerati da ragazzi delle medie, la riga già pronta e il bottone COPIA.
3. **La PR-3 non era spiegata.** «Un difetto nella versione nuova» non diceva cosa fare: tutti hanno chiesto. Regola: ogni fase ha un esempio completo e il link a quello che serve (qui: apri il gioco, fai 1 partita, scrivi UNA cosa che non va).
4. **Lavori per PC con i numeri vecchi.** Ho diviso il lavoro per numero di PC usando la foto Veyon delle 12:08; alle 12:26 molti avevano cambiato PC. Regola: prima di assegnare un lavoro per PC si controlla l'ultima foto Veyon; meglio assegnare per nome (nel Documento personale) e usare il PC solo come aiuto.
5. **Modifiche alla pagina non verificate.** Due sostituzioni nel codice della pagina non sono andate a segno (il testo da sostituire non c'era) e me ne sono accorto dopo. Regola: dopo ogni modifica si controlla che il cambiamento ci sia (ricerca nel file o schermata) prima di dire che è fatto.
6. **«Consegna» non spiegata all'inizio.** Due ragazzi hanno premuto «Consegna» e il Documento si è bloccato. Regola: nel testo del compito, fin dall'inizio, «non premere Consegna fino alla fine; se l'hai premuto, premi Annulla consegna».
7. **Pull Request copiate tra compagni.** Tre ragazzi della stessa squadra hanno consegnato lo stesso cattivo. Regola: ogni PR-1 deve essere diversa; le copie si accettano una volta sola e si segnalano.
8. **Nomi nei report.** La regola del corso vieta i nomi dei minori nelle pagine pubbliche; il docente li ha chiesti. Soluzione adottata: report pubblico per numero di PC, nomi visibili solo con la password della classe (cifrati nel repository).

## 08/10/2026 — 3INF, report pubblicato senza nomi leggibili (#40)

1. **Cosa è successo.** Il report della 3INF mostrava «scrivi la password» al posto del nome: il docente non poteva capire a colpo d'occhio di chi fosse ogni riga, quindi il report non serviva in classe.
2. **Correzione.** Nel report ora si vede subito il nome di battesimo; il cognome resta nel report completo del repository privato.
3. **Regola (vale da oggi, per tutte le classi).** Non si pubblica MAI un report, un elenco o una pagina di valutazione che il docente non possa attribuire in modo semplice e immediato a ogni allievo: ogni riga porta almeno il nome di battesimo visibile (mai solo il numero di PC, mai nomi nascosti dietro una password).
