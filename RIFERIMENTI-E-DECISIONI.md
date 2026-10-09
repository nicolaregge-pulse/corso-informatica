# Riferimenti rapidi e decisioni (Nicola ↔ Claude)

**Versione 2.31** — 08/10/2026

*File durevole su Git: raccoglie contatti, convenzioni e decisioni stabili, così non
si perdono quando la sessione viene compattata. Regola: qui NON entrano mai nomi di
allievi (minori) né voti nominali; quelli restano solo in scratchpad/PDF riservati.*

---

## 1. Contatti e riferimenti
1. **Assistenza tecnica (sysadmin):** `support.piamarta@piamarta.it`
2. **Email studenti:** `nome.cognome@studenti.piamarta.it`
3. **Email docenti:** `nome.cognome@piamarta.it` (Nicola: `NICOLA.REGGE@PIAMARTA.IT`)
4. **Scuola:** Piamarta · **Aula laboratorio:** 11
5. **Docente:** Regge Nicola · **Discipline:** Tecnologia professionale, Laboratorio
   professionale, Sicurezza professionale, Informatica.
6. **Classi:** 1INFspe (Classe 1), 2INFspe (Classe 2), 3INFspe (Classe 3), 4TI (Classe 4).
7. **Sicurezza = programma della REGIONE** (si fa ciò che dice la Regione, non ciò che
   decidiamo noi): quando si corregge, farlo sempre notare a Nicola.
8. **Sito Piamarta "Formazione sicurezza" (tutte le ore, 1ª→16ª)** — link che FUNZIONA
   (con i parametri di accesso):
   `https://sites.google.com/piamarta.it/formazionesicurezzamilano?pli=1&authuser=0`
   (senza `?pli=1&authuser=0` a Nicola non si apriva).
   **PROMEMORIA (da ricordare a Nicola ogni volta che serve questo link):** su alcune
   postazioni Nicola è loggato con l'**account PERSONALE** → il sito non si apre. Deve
   passare all'**account scuola** `@piamarta.it` (in alto a destra, scelta account). Idem
   per i ragazzi: devono essere su `@studenti.piamarta.it`.
9. **Portale AFGP Piamarta:** `https://piamarta.afgp.it/`
10. **CAMPANELLE (date da Nicola, salvate il 02/10/2026):**
    **08:00 · 08:55 · 09:55 · 10:50 · [intervallo] · 11:10 · 12:05 · 13:05 · 14:00**.
    Ore reali: 1ª 08:00-08:55 · 2ª 08:55-09:55 · 3ª 09:55-10:50 · intervallo 10:50-11:10 ·
    4ª 11:10-12:05 · 5ª 12:05-13:05 · 6ª 13:05-14:00. Registri inviati alle **14:05** (firma entro
    quell'ora). Nel registro elettronico le ore risultano a blocchi da 60 minuti (08-09 … 13-14).
    Ogni scadenza di compito e ogni promemoria si fissano su queste campanelle, mai a caso.
    **Nulla dopo le 14:00** (fine lezioni): raccolta finale delle consegne alle **13:55** e report
    a Nicola PRIMA delle 14:00; ciò che arriva dopo si riprende in automatico senza chiedere niente.

## 2. Convenzioni durature
1. **PPP** = "parcheggia": annota, prepara in silenzio, **non consegnare** finché
   Nicola non dice **"avanti"**. Eccezione: se dentro il PPP c'è un'azione concreta
   esplicita, quella si fa subito.
2. **Riflessione obbligatoria:** ogni compito finisce con "cosa NON ho fatto e perché"
   + "cosa NON ho capito". È la parte più importante da leggere.
3. **Un foglio = una cosa sola.** Coordinate complete (app → scheda → area → azione).
   Cose da copiare sempre in **blocco di codice** (bottone copia).
4. **Lingue materiali ragazzi:** versione **italiana per tutti** + **bilingue** solo
   per chi serve. Classe 1 = IT/AR/ZH; Classe 3 = IT + bangla. Materiali docente = IT.
5. **Git — DUE repo:** il **pubblico** `corso-informatica` (ex `corso-godot`, che
   resta come redirect; contiene anche i **giochi Godot**) tiene solo materiale
   **condivisibile** (didattica, esperimenti/giochi/siti dei ragazzi): **mai** nomi
   di minori, voti nominali o dati personali. Tutto ciò che è
   **riservato/strategico/personale** (nomi, voti nominali, presenze, anti-plagio,
   dati di rete, cedolini) va nel repo **PRIVATO** `corso-informatica-riservato`
   (le **fonti** versionate stanno lì). I **PDF/ZIP pesanti intermedi** sono **rigenerabili**:
   NON si versionano (scratchpad + consegna a Nicola). **ECCEZIONE:** il **deliverable finale
   di chiusura** (lo ZIP di `CHIUDI classe`) si **archivia nel repo PRIVATO**
   (`dati/chiusure/<CLASSE>/`, force oltre il `.gitignore`) perché contiene nomi — così resta
   conservato com'è stato consegnato. Mai nel pubblico.
6. **Consegne ragazzi:** preferire **un solo Documento Google** (screenshot + testo/codice
   + riflessione), non file .html/ZIP da raccogliere.
7. **Metodo:** "Vinci subito · Fallo tuo · Mostralo"; passi piccoli, micro-vittorie ogni
   15-20 min; niente 3 ore di fila sullo stesso compito (spezzare, "mostralo" al compagno).
8. **GIT come archivio e struttura (regola):** usare Git per **archiviare i materiali** e
   costruire **strutture logiche riusabili** (fonti uniche `argomenti/`, generatori, indici,
   registro, file di riferimento) così da **non perdere lavoro** col compattamento e
   **ottimizzare i tempi di Claude**. Preferire sempre strutture Git-backed a file effimeri;
   i dati **riservati** (nomi di minori) restano comunque fuori da Git (scratchpad + PDF).
9. **Due griglie a ogni compito (per il docente):** (a) **griglia completa** del lavoro —
   tutte le note + cosa NON ha fatto in **neretto** + voto; (b) **griglia incrementale** —
   solo info principali, **una colonna per compito** che si accumula nel tempo. Vale per
   tutte le classi. Entrambe RISERVATE (nomi) → PDF a Nicola, mai su Git.
10. **REPORT COMPLESSIVO del compito (regola, 30/09/2026).** Per ogni compito, oltre alle
    due griglie, si produce un **report complessivo** (RISERVATO → PDF) che contiene SEMPRE,
    in un unico documento, queste 4 parti:
    1. **Dettaglio per allievo** = tutto ciò che è stato dato al ragazzo (il suo lavoro +
       la sua valutazione con le note).
    2. **Le mie impressioni** (di Claude): lettura d'insieme della classe, chi va bene, chi
       recuperare, segnali.
    3. **Anti-plagio:** copiature, uso dichiarato/sospetto di IA, account condivisi,
       tentativi di pilotare il voto.
    4. **Indicazioni dei ragazzi:** sintesi analizzata delle loro riflessioni — temi svolti
       poco o **non capiti**, richieste, difficoltà ricorrenti (dove intervenire).
    5. **Segnalazioni:** anomalie viste nel **monitoraggio** o in classe — presenza di un
       allievo **non di quella classe**, comportamenti, problemi tecnici — da riportare nel report.
11. **Doc già su Classroom = congelati (regola, 01/10/2026).** Se Nicola dice cose che
    modificherebbero un documento **già pubblicato/consegnato su Classroom**, Claude **NON
    lo rifà in automatico**: ne tiene solo **traccia** nell'elenco "Correzioni in sospeso"
    (§7) e lo aggiorna **solo quando Nicola lo dice esplicitamente** (poi bump di versione).
    Vale per i doc già in mano agli allievi; i doc non ancora pubblicati si correggono subito.
    **Eccezione — questione GRAVE:** se l'errore blocca o fuorvia davvero, si aggiorna il doc
    su Classroom. Ma costa: **perdita di tempo, confusione, e i ragazzi fragili si perdono.**
    Quindi si fa **solo se davvero necessario**, e si **avvisa la classe** del cambiamento.

12. **Parola chiave "monito" (regola, 01/10/2026):** quando Nicola scrive **"monito"**
    (o manda uno screenshot di monitoraggio Veyon), significa: **osserva cosa fanno i
    ragazzi** e **aggiungi le osservazioni** al **Report andamento classe** (uno per classe,
    RISERVATO → repo privato `dati/andamento/report-andamento-classe-<CLASSE>.md`). È un
    documento **che cresce nel tempo** (storia dell'andamento: chi lavora, chi è fuori
    task, difficoltà ricorrenti, progressi). Le segnalazioni gravi/ripetute confluiscono
    anche nel report del compito (§2.10 punto 5). I nomi stanno solo nel repo privato.
    **Precisazione (01/10/2026):** uno **screenshot Veyon inviato SENZA testo** vale di per sé
    come comando **"monitora e registra"** (stessa cosa di scrivere "monito"): Claude osserva la
    schermata e annota l'osservazione con l'orario nel report andamento, senza bisogno di altre
    parole.

13. **Griglie totali ⇒ SEMPRE anche il Report di monitoraggio allievi (regola, 01/10/2026).**
    Quando Nicola chiede le **griglie totali** (le griglie complete del lavoro), si produce
    **sempre anche** il **Report di monitoraggio allievi** di quella giornata/ora: fa parte
    dell'**andamento dell'ora**. Fonte = il Report andamento classe (§2.12). Quindi le griglie
    totali consegnate sono accompagnate dal quadro di chi ha lavorato / chi era fuori task /
    difficoltà viste al monitoraggio. Tutto RISERVATO (nomi) → repo privato / PDF a Nicola.

14. **CHIUDI — impacchettamento a prova di privacy (regola, 01/10/2026).** La cascata CHIUDI
    produce due insiemi SEPARATI: (a) **file PER GLI ALLIEVI** = i **libri individuali, uno per
    file**, ciascuno col **solo** lavoro del singolo (nessun nome/voto altrui) → si consegnano
    **uno a uno** (ognuno riceve solo il suo); (b) file **SOLO DOCENTE** = griglia completa,
    report monitoraggio con nomi, incrementale. **MAI** un unico ZIP con tutti gli allievi
    insieme destinato alla consegna, e **MAI** mettere i documenti docente nello stesso
    pacchetto che può arrivare ai ragazzi. "Libro individuale" = del singolo, per lui.

15. **Valutazione = "dell'AI", mai spacciata per quella del docente (regola, 01/10/2026,
    corretta).** L'AI (Claude/"SBIRRO") **DÀ** voto, giudizio e tutto ciò che è utile dire al
    ragazzo, **ma** la sezione va intitolata **"Valutazione dell'AI"** (o "dell'assistente"),
    **mai** "Valutazione del docente": Nicola non li ha valutati lui. La valutazione dell'AI è
    uno **strumento di supporto** che il docente può confermare, correggere o sovrascrivere
    quando vuole. Nel libro dell'allievo quindi **ci sono** voto e giudizio, chiaramente marcati
    come dell'AI. (Prima avevo tolto la valutazione: era sbagliato; va messa, solo attribuita
    correttamente.)

16. **Report "lezioni precedenti" SEMPRE prima di proporre argomenti (regola, 01/10/2026).**
    Quando Nicola chiede cosa fare o degli argomenti da trattare (inizio lezione), Claude dà
    **sempre per primo** il **report di cosa è stato fatto nelle lezioni precedenti** di quella
    classe (dal registro `ARGOMENTI-SVOLTI-2026-27.md` + consegne/materiali), e **solo dopo**
    propone i prossimi argomenti (coerenti col calendario/moduli). Se il registro è indietro,
    lo si segnala e si chiede conferma per aggiornarlo.

17. **Integrare sì, introdurre argomenti nuovi solo dopo confronto (regola, 01/10/2026).**
    Distinzione chiave: **integrare/arricchire** ciò che Nicola ha spiegato (esempi in più,
    chiarimenti, immagini) è **apprezzato** e si fa. **Introdurre argomenti o direzioni NUOVI**
    non trattati (es. decimale→binario quando in classe si è fatto solo binario→decimale) **NON**
    si fa di propria iniziativa: ci si **confronta prima** con Nicola. La **lavagna** è il
    riferimento di cosa è stato spiegato. Regola generale: **nel dubbio, chiedi.**

18. **La foto della lavagna va DENTRO la dispensa di teoria (regola, 01/10/2026).** La teoria
    deve contenere la **foto della lavagna** della lezione: è la lezione vera, con le parole e i
    disegni del docente, e aiuta i ragazzi a fissare e a riconoscere ciò che hanno visto in
    classe. Vale per ogni dispensa/scheda (foto ritagliata senza nomi se pubblica).

19. **Stesse cose = stesso layout IDENTICO (regola, 01/10/2026).** Materiali dello stesso tipo
    che i ragazzi vedono in sequenza (es. **dispensa** e poi **compito/esercitazione** sullo
    stesso argomento) devono avere la **grafica identica**, non solo "simile". Se la dispensa usa
    una certa griglia (colori, bordi, evidenziazioni), il compito usa **quella stessa griglia**,
    pixel per pixel. Modo pratico: **gestire gli elementi grafici come IMMAGINI** (PNG dalla
    stessa fonte) + **spazio per i conti a mano** sotto. Vale per ogni coppia teoria↔esercizio.

20. **Solo COPIA-INCOLLA, passo per passo (regola, 02/10/2026).** Quando guido Nicola in una
    procedura, deve dover **solo copiare e incollare**, **mai scrivere/digitare** nulla a mano
    (né editare codice). Quindi: ogni valore/comando in un **blocco di codice** col bottone copia
    (già regola COPIA); **un passo alla volta**, numerato, con le coordinate complete (app →
    scheda → area → azione); i valori da inserire si danno **già pronti** (es. ID, nomi, percorsi)
    e, dove serve configurare, si usano **Proprietà dello script / caselle** in cui si incolla,
    non modifiche al codice. Se un dato deve venire da lui (es. un ID dal log), glielo faccio
    **copiare** da dove appare e **incollare** dove serve — mai riscrivere.

21. **Nomi sensati agli script/progetti (regola, 02/10/2026).** Niente "Progetto senza titolo":
    ogni progetto Apps Script (e file script) ha un **nome chiaro** che dice cosa fa, es.
    "Consegne Classroom → Git", "Crea compito Classroom", "Quiz Sicurezza". Si rinominano anche
    quelli vecchi senza nome quando si aprono.

22. **Scheda sintetica per la lezione frontale del docente (regola, 02/10/2026).** Per OGNI
    nuovo argomento/lezione, Claude dà SEMPRE a Nicola — per primo — una **scheda sintetica**
    (1 pagina, per il DOCENTE) con cui **iniziare la lezione frontale**: concetto in breve, i
    passi del metodo, 2-3 esempi svolti, gli agganci "Vinci subito · Fallo tuo · Mostralo", gli
    errori tipici da prevenire. È il "canovaccio" della spiegazione alla lavagna. Viene PRIMA di
    dispensa/compito (che poi seguono la lavagna reale, §2.17-2.18). È materiale docente
    (in italiano), separato dai materiali per i ragazzi (trilingui).

23. **Flusso standard di una lezione/argomento (regola, 02/10/2026 — richiesta da Nicola).**
    L'ordine di ogni nuovo argomento è: **(1)** Claude propone **3-4 argomenti**, preceduti dal
    **report dello svolto** della classe (§2.16); **(2)** Nicola ne sceglie **uno o più**;
    **(3)** Claude dà la **scheda sintetica** per la lezione frontale (§2.22); **(4)** Nicola fa
    la lezione e manda le **immagini della lavagna**; **(5)** Claude crea il lavoro su
    **Classroom** — **dispensa (teoria)** + **compito con scadenza** — tramite lo script/ponte;
    **(6)** dopo la **scadenza**, dalle consegne Claude genera **libro individuale + griglie +
    report docente**. La scadenza serve proprio a chiudere e generare i libri.

24. **Sovradimensionare + gestire il divario (fast/slow) (regola, 02/10/2026).** Meglio
    **preparare PIÙ lavoro del necessario** e non finirlo, che avere ragazzi **fermi a non far
    niente** (il fermo diventa off-task). Inoltre, dare "molti lavori" rischia di allargare un
    **digital divide interno**: alcuni finiscono molto prima della media, gli ultimi faticano
    perfino a consegnare. Quindi ogni lezione/compito si progetta **a più livelli**:
    - un **NUCLEO base** (pavimento basso) che **tutti** riescono a fare e **consegnare** (con
      scaffolding/aiuti per gli ultimi);
    - **ESTRA/sfide** (soffitto alto) per chi finisce prima, così **non resta mai fermo**;
    - materiale **abbondante** (sovradimensionato), così non si esaurisce mai.
    Si lega ai **4 livelli di aiuto** dell'eserciziario e alla "scatola flessibile".

25. **Argomenti del REGISTRO: CORTI (regola, 02/10/2026 — richiesta da Nicola).** La casella
    "Argomento" del registro elettronico mostra poco testo e taglia il resto (visto con "...metodo d").
    Quindi il testo per il registro è **una frase breve, massimo ~40 caratteri**, senza parentesi
    né spiegazioni (es. "Conversione da decimale a binario"). **Uno per ora**, ciascuno nel suo
    blocco da copiare. I dettagli vanno in `ARGOMENTI-SVOLTI-2026-27.md`, non nel registro.

26. **Si usa SOLO il metodo del docente (regola, 02/10/2026 — richiesta da Nicola).** Il metodo
    è quello che Nicola fa alla lavagna (es. decimale → binario = divisioni per 2, resti dal basso,
    zeri davanti). Se i ragazzi faticano si spiega **lo stesso metodo più semplice** (più passi,
    più disegni, esercizi a gradini), **mai** introdurre un metodo alternativo: confonde. (Errore del
    02/10: "metodo delle monete" ritirato.)

27. **Indentazione del codice Lazarus/Pascal (regola, 04/10/2026 — richiesta da Nicola).** In tutti
    gli esempi e le soluzioni: `if` ed `else` **sullo stesso rientro**; `begin` ed `end` **sullo
    stesso rientro**; tutto ciò che sta dentro è **indentato** di un livello (2 spazi). Negli if
    annidati ogni livello aggiunge un rientro, così si vede a colpo d'occhio chi sta dentro a chi.

28. **Ogni correzione di Nicola diventa regola (05/10/2026 — richiesta da Nicola).** TUTTO ciò che Nicola
    segnala come sbagliato (anche con PPP) si registra **subito** in due posti: 1) `REGISTRO-ERRORI-CLAUDE.md`
    (cosa è successo, data, classe); 2) una **regola qui** (o in `REGOLE-NOSTRE-CLAUDE-NICOLA.md`) che dice
    come non rifarlo. Prima di ogni consegna si rileggono le regole 2.25-2.29.

29. **Testi da incollare su Classroom: già impaginati (05/10/2026).** Istruzioni di compiti/annunci: titoletti
    in MAIUSCOLO, **una riga per passo** numerata (1. 2. 3.), elenchi una voce per riga, riga vuota tra i
    blocchi, il link su una riga sua. **Mai** un paragrafo unico con 1) 2) 3) in linea. Il testo intero sta
    in **un solo** blocco da copiare, pronto da incollare (con il link dentro, se va sostituito tutto).

30. **Comando "Chiudi classe <CLASSE>" (es. "Chiudi classe 3 INF") — 05/10/2026, richiesto da Nicola.** Quando Nicola
    lo dice, si chiude il lavoro della classe e si producono, MD + PDF versionati:
    1. **Per ogni allievo — il libro individuale**: tutta la teoria dal primo giorno di scuola, tutti gli esercizi,
       tutti i lavori consegnati con voto e indicazioni personali (nel repo riservato; copia per l'allievo protetta).
    2. **Per Nicola**: tutte le griglie (voti per lavoro + **griglia incrementale** lezione dopo lezione), consigli
       per allievo, valutazioni, cosa NON hanno capito e cosa NON hanno fatto, il **report di monitoraggio** (Veyon,
       fuori compito, problemi di account, presenze).
    3. Fonti: `dati/consegne/<CLASSE>/`, `dati/presenze/`, `dati/valutazioni/`, anagrafica Excel, note di monitoraggio,
       materiali del repo pubblico della classe. Tutto con i nomi resta SOLO nel repo riservato.
    4. **Consultazione con un clic (05/10/2026, chiesto da Nicola):** su richiesta, i PDF della chiusura (libri individuali e
       documento del docente) si mettono anche in una **pagina privata Artifact** di claude.ai: Nicola clicca e il PDF si apre
       nel riquadro a destra, senza scaricare. Contiene nomi e voti di minori: si pubblica solo dopo il suo "pubblica" esplicito,
       resta privata e non si condivide.
    5. **Ordine fisso:** si aspetta la raccolta automatica delle consegne (scadenza + 10 minuti), si rilegge GitHub (codice e
       README di ognuno), poi un solo comando: `generatori/chiudi_3inf_sito.py` (per la 3INF del 05/10).

31. **In `docs/` i PDF già usati in classe non si cancellano (05/10/2026).** Quando esce una versione nuova, la pagina
    unica punta alla nuova, ma la vecchia **resta** nella cartella: chi ha la pagina vecchia in memoria nel browser
    deve poter aprire il link. Si fa pulizia solo a fine settimana, mai durante le lezioni.

32. **Monitoraggio Veyon: dalla miniatura solo fatti, mai giudizi (05/10/2026).** Si scrive "PC N sulla pagina X alle
    HH:MM", non "non ha fatto niente". Prima di dire che un allievo è fermo si guardano le schede aperte e lo stato del
    sito (pagina dei siti): la miniatura mostra solo la finestra in primo piano.
33. **In classe risposte cortissime (05/10/2026).** Durante la lezione rispondo SOLO con: il testo aggiornato e completo del compito da incollare su Classroom (un blocco copia) e il link per il docente (un blocco copia). Niente tabelle o spiegazioni se Nicola non le chiede.
34. **Lavori su GitHub: la consegna la genera Claude (05/10/2026).** Il ragazzo pubblica il sito e su Classroom preme solo "Consegna". Link, codice, screenshot, controlli e domande personali li genera Claude dal repository (`generatori/siti_3inf.py`, elenco unico `config/3inf-github.json` nel repo riservato). Il docente interroga.
35. **Gli assenti si escludono sempre (05/10/2026).** Da liste, link del docente, pagine di controllo, conteggi e "chi manca" si tolgono gli assenti del giorno; restano solo nel registro presenze (repo riservato) e nei recuperi.
36. **Fuori compito: se ne tiene sempre traccia (05/10/2026).** A ogni monitoraggio Veyon si annota nel repo riservato (`dati/andamento/<CLASSE>-fuori-compito-<data>.md`) chi, a che ora e cosa si vede (solo fatti, §2.32). Serve per la valutazione del comportamento e per la chiusura della classe.
37. **Controlli dei siti senza API di GitHub (05/10/2026).** L'API si blocca dopo circa 60 controlli all'ora dalla rete della scuola. Le pagine aprono direttamente il sito (`docs/3inf-sito/online.js`) e leggono utenti e repository da `pc.json` e `repo.json`, generati in automatico.
38. **Su Classroom e sulle pagine della classe SOLO il lavoro del giorno (05/10/2026, VINCOLANTE).** Mai pubblicare su Classroom, né mostrare nella pagina linkata, materiale di un giorno diverso da quello della lezione. I lavori dei giorni dopo si preparano in coda (`in-attesa-ok-docente`) e nascosti nelle pagine; si attivano solo il loro giorno, con l'OK di Nicola. Lo script `automazione-corso.gs` rifiuta da solo un compito la cui data nel nome del file non è oggi.
39. **Un solo compito aperto alla volta (05/10/2026, VINCOLANTE).** Se nella stessa lezione ci sono due lavori, su Classroom si pubblica solo il primo; il secondo resta in coda e si pubblica quando Nicola dice che la classe ha finito il primo. Titoli con l'ordine ("1 di 2", "2 di 2") e nomi descrittivi, mai "Compito 1".
40. **Come si controllano i lavori su GitHub (05/10/2026, dopo gli errori del mattino).** 1) I repository si TROVANO con la ricerca GitHub dei repository creati oggi (es. `lazarus in:name created:>=OGGI`), non indovinando nomi utente e nomi di repository (i ragazzi usano nomi diversi: `lazarus-`, `mio-sito12`...). 2) I file si LEGGONO con `git clone` (elenca tutti i file, nessuna cache), non con raw. 3) Si accettano nomi di file diversi (project1, primo_programma, progetto1): conta il contenuto di `unit1.pas`. 4) Prima di dire "non ha caricato" si verifica con il clone. Generatore: `generatori/monitor_2inf.py` (repo riservato).
41. **Solo strumenti provati e approvati da Nicola (05/10/2026, sera).** Il flusso completo per tutte le classi è: Nicola dà il compito → Claude prepara la pagina HTML delle spiegazioni e il file per lo script → lo script lo pubblica su Classroom → raccoglie le consegne → Claude corregge, fa libri e chiusura → lo script mette i voti su Classroom → le consegne restano su Classroom e la prova va nell'archivio per la Regione. Regola: in classe si usa SOLO ciò che Nicola ha provato e approvato; ogni pezzo nuovo si prova prima con lui e solo dopo diventa standard. Stato al 05/10:
    1. **Approvati (provati in classe):** pubblicazione del compito con lo script; raccolta automatica delle consegne; una pagina per i ragazzi + un link per il docente; caricamento su GitHub con Add file → Upload files; chiusura classe con libri individuali protetti, zip docente senza password, voti in centesimi.
    2. **Da provare con Nicola:** voti in bozza su Classroom (script v3, solo compiti creati dallo script; Nicola controlla e preme Restituisci); archivio delle prove (`archivio-prove/` nel repo riservato, generatore `generatori/archivio_prove.py`: scheda della prova MD+PDF, pagina del compito fotografata, chiusura, registro delle prove per classe); pagina del compito unica a 3 versioni (normale, semplificata, lingue); correttore unico con la griglia scritta nel compito.
    3. **Compiti creati a mano:** lo script non può né modificarli né metterci i voti. Per questo i compiti li crea sempre lo script.
42. **Recupero a fianco (06/10/2026, richiesto da Nicola).** Ogni tanto chi è andato male rifà l'esercizio in versione semplificata con Nicola seduto accanto, così si recupera anche chi non ce la fa. Regole: 1) entra chi ha voto sotto 60 o lavoro non svolto (assenti esclusi); prima chi è sotto 60 (A FIANCO), poi i "non svolto" che possono fare da soli con la pagina; 2) la pagina semplificata è pubblica e senza nomi (`docs/recupero/<esercizio>/`, generatore `strumenti/gen_recupero.py`): un'azione per passo, il programma in alto, "adesso devi vedere", "non mi torna", numero del passo grande per Veyon, elenco completo per il docente; 3) l'elenco con i nomi, il punto da cui partire e le 3 domande della prova del nove sta nel repo riservato (`generatori/recupero.py` → `dati/recupero/`), e si rigenera dopo ogni "Chiudi classe"; 4) voto di recupero (proposta, da confermare): stessa griglia, voto NUOVO sul registro, il precedente resta; se non sa rispondere alle domande non supera 60. Stato: da provare con Nicola (§2.41).
43. **Lista standard valutazioni per il docente e «Valutazione complessiva della classe» (06/10/2026, nome deciso da Nicola).** Ogni volta che si valuta una classe si producono SEMPRE: 1) per ogni allievo presente il libro (tutti i lavori con voto e indicazioni, cosa recuperare, consegne in coda), protetto da password per il ragazzo e senza password per il docente; 2) per il docente: voti per il registro in ordine alfabetico (O = proposta AI, C = valutazione ponderata del docente), griglia completa, situazione e indicazioni per allievo (comprese le cose non capite), lista di recupero (i tre con la media più bassa vengono interrogati), monitoraggio e fuori compito, password, Excel della classe aggiornato; 3) due zip, LIBRI-PROTETTI e DOCENTE, assenti fuori dagli zip, divisi se superano 30 MB. Il punto su tutti i lavori fino a una data si chiama **Valutazione complessiva della classe** (comando `VALUTAZIONE COMPLESSIVA classe`, ATLANTE 08b punto 5).
44. **Voti su DIDAweb: materia scelta per ARGOMENTO, voto minimo 40 (06/10/2026, Nicola).** Quando un voto va sul registro, la disciplina (Tecnologia, Laboratorio, Sicurezza professionale) si sceglie in base all'**argomento realmente trattato** nel lavoro, non solo all'ora in cui è stato fatto: **Sicurezza professionale in modo rigoroso: SOLO le 16 lezioni online di sicurezza + la Ricerca GitHub del 18/09 (motivazione: gestire il repository in modo sicuro)**; regole di classe, versioning e uso pratico degli strumenti → **Laboratorio**; hardware, configurazione del PC, sistema binario e calcolo → **Tecnologia**. Si guarda anche la macro-area del lavoro. Si cerca di avere almeno un voto per materia. Data e ora: quelle della lezione in cui il lavoro è stato svolto (ore da 1 a 6). Descrizione corta, con il riferimento al compito su Classroom. **Il voto minimo è 40**: i voti più bassi si portano a 40. I voti si danno un lavoro per volta, in tabella N. · Alunno · Voto, nell'ordine del registro (23 righe, vuoto per chi non ha voto).
45. **Tutta la suite Google in automatico, in tutte e due le direzioni (06/10/2026, priorità assoluta per Nicola).** Ogni passaggio su Google (Moduli, Fogli, Documenti, Drive, Classroom, Gmail) si fa con lo script automatico dell'account della scuola, mai a mano: i compiti e i quiz con la coda `coda/` (quiz su Moduli dalla v4), tutto il resto con il **ponte Google** `comandi/` (v5): cercare, leggere, esportare, creare, scrivere su Drive, Moduli, Fogli, Documenti e Classroom, e preparare **bozze** in Gmail. Per sicurezza il ponte non cancella, non condivide fuori dalla scuola e non invia mail; gli annunci su Classroom partono solo con l'OK del docente.

46. **Chi ha finito il lavoro (07/10/2026, Nicola).** Chi ha finito il compito del giorno può fare **lavori di altre materie** oppure **cose di informatica** (esercizi, Tinkercad, programmazione, dispense). Non si gioca e non si guardano video. Nel monitoraggio Veyon: lavoro di un'altra materia o attività di informatica dopo aver finito = **sul pezzo**; giochi, video, social, siti non di studio = fuori compito. Quando la classe aspetta (per esempio durante le interrogazioni) si assegna sempre un lavoro breve già pronto, come il quiz personale del giorno, aperto a tutti con Veyon («Apri sito web») e con un annuncio su Classroom per chi non riesce ad aprirlo.
47. **Parte tecnica separata dalla teoria nella valutazione (07/10/2026, Nicola).** Nei report si leggono due medie: la **media tecnica** (programmi e pubblicazione su GitHub) e la **media di teoria** (ricerche scritte e quiz). Nella media tecnica un lavoro **non consegnato vale 40**; gli assenti restano fuori. Il voto proposto dall'AI va sempre confrontato con quello che il ragazzo ha consegnato davvero (codice suo o copiato dalla dispensa, programma che gira, spiegazione con parole sue): a parità di consegna, stesso voto.
48. **Il modo di lavorare in classe: pubblica, personalizza, segui (07/10/2026, VINCOLANTE, Nicola: «il modo di lavorare deve essere questo»).** A ogni lezione con un lavoro: 1) **si pubblica** il lavoro su Classroom con lo script (compito o annuncio, una volta sola, §2.39); 2) **istruzioni personalizzate** per ogni ragazzo, basate su quello che ha già fatto: pagina «Il mio punto» della classe (`docs/<classe>-mio-punto/`, generatore `generatori/mio_punto_<classe>.py` nel repo riservato), che si apre con la password del libro e mostra lavori fatti/da recuperare, il sito o il programma, i commit di oggi e «cosa devo fare adesso» con i link alle pagine passo-passo; nel repo pubblico solo testo cifrato, niente nomi né voti in chiaro; 3) **si seguono** durante l'ora: controlli ripetuti (consegne su Classroom con il ponte, commit su GitHub con git clone), la pagina «Il mio punto» si rigenera da sola, e a Nicola si dice chi non ha fatto cosa e come finirlo; 4) **si tiene traccia degli screenshot di Veyon** per chi non lavora bene: solo fatti, con ora e numero di PC, in `dati/andamento/<CLASSE>-fuori-compito-<data>.md` (repo riservato, §2.32, §2.36). Prima di nominare ai ragazzi un materiale (libro, pagina) si controlla che lo abbiano e si dice dove trovarlo.
49. **Lingue della 2INF (08/10/2026, Nicola: «non serviva arabo, ma ok lascialo»).** Nei testi per la 2INF l'arabo non serve: si scrivono in italiano e cinese. Quello già pubblicato con l'arabo resta com'è.

## 3. Tassonomia dei libri (decisa)
1. **A — Manuale / Libro totale:** per ARGOMENTO, **3 livelli** (base/intermedio/avanzato).
   Fonte unica = `argomenti/`.
2. **B — Libro complessivo di classe:** teoria + compiti di tutte le lezioni (senza nomi).
3. **C — Libro individuale:** B + il lavoro del singolo **valutato** + indicazioni +
   **riflessione** + (foto della lavagna, fornite da Nicola). Riservato.
4. **D — Libro parziale:** una giornata o una lezione (sottoinsieme).
5. **Core vs Approfondimento:** core = ciò che ha fatto QUELLA classe; il meglio fatto
   nelle altre classi = **"Approfondimento"** in un riquadro distinto.
6. **Naming:** `Libro-Classe-N_COMPLESSIVO_vX.Y` · `Manuale-Informatica_vX.Y` ·
   `Libro-Individuale_Cognome-Nome_Classe-N_..._RISERVATO`.
7. **Header/footer:** standard vincolante (vedi `REGOLE-FORMATTAZIONE.md` §12): banda per
   unità (macro-argomento · materia · data · orario · contenuto) + footer di pagina.

## 4. Dove stanno le cose (repo)
1. `argomenti/` — la **fonte unica** a 3 livelli + `_build/genera_manuale.py` (Manuale).
2. `classe-1/libro-individuale/` — `unita/`, `manifesto.md`, generatori (`_build/`:
   individuale, generale, `render_libro.js`).
3. `REGISTRO-ORE-2026-27.md` — tutte le ore (navigabile per giorno / classe / materia).
4. `manuale-informatica/` — il Manuale generato.
5. **Dati riservati** (voti + nomi, anti-plagio, presenze, strategico, personale):
   nel repo **PRIVATO** `corso-informatica-riservato`, clonato in
   `/home/user/corso-informatica-riservato`. Struttura: `dati/` (fonte di verità,
   con `libro-dati-riservato.json` + `anagrafiche/` + `presenze/`), `generatori/`
   (script che producono output coi nomi), `antiplagio/`, `strategico/` (+ `personale/`,
   `password/`). I PDF/ZIP si **rigenerano**, non si versionano (`.gitignore`).
6. **Libri individuali:** generatore **pubblico**
   `classe-1/libro-individuale/_build/genera_libro_individuale.py` con i dati passati
   dal privato: `--dati /home/user/corso-informatica-riservato/dati/libro-dati-riservato.json`.
   La teoria/descrizione compiti (pubblica, senza nomi) viene **infrapposta** al lavoro
   valutato del singolo (dal privato). Output = PDF in scratchpad, consegnati a Nicola.

## 5. Aperte (da completare)
1. **Atlante del corso** — FATTO: `ATLANTE.md` (v0.3) + `ATLANTE-v0.3.pdf`. Mappa unica:
   tipi di libro A/B/C(3 tagli)/D, Manuale 3 livelli × 3 profondità, 7 tipi-artefatto + nomi
   2.13, accrescimento (fonte unica + matrice copertura + aggiornamenti), due repo/main-Release,
   documenti del docente (griglia, scheda del lavoro, per giornata, incrementale) e i
   **comandi/parole chiave** con la tabella "documento → comando". (Ex "Topologia libri", rimosso.)
2. **Programma Sicurezza (Regione)** — atteso da Nicola.
3. **"Io e la mia famiglia" 17/09** — manca lo ZIP per l'ultima colonna della griglia.
4. **Lezione HTML Classe 3 → nei libri** (dopo il PDF tassonomia): diventa argomento + unità.

## 6. Changelog
1. **v1.0 (30/09/2026)**: prima versione, per non perdere i riferimenti al compattamento.
2. **v1.1 (30/09/2026)**: modello a **due repo** (pubblico `corso-informatica`, ex `corso-godot` + privato
   `corso-informatica-riservato`). I dati riservati (nomi, voti, presenze, anti-plagio,
   strategico, personale) non stanno più solo in scratchpad ma nel repo privato; i
   PDF/ZIP restano rigenerabili. Aggiornati §2.5, §4.5 e §4.6.
3. **v1.2 (01/10/2026)**: §2.11 — i doc **già su Classroom** non si rifanno in automatico
   (solo traccia in §7, correzioni su richiesta; eccezione se grave, col suo costo). Aggiunta
   la sezione §7 "Correzioni in sospeso".
4. **v1.3 (01/10/2026)**: §2.10 punto 5 — **Segnalazioni**: le anomalie viste nel
   monitoraggio o in classe (allievo non di quella classe, comportamenti, problemi tecnici)
   entrano sempre nel **report complessivo** del compito.
5. **v1.4 (01/10/2026)**: §1 punti 8-9 — salvato il **link Piamarta "Formazione sicurezza"**
   che funziona (coi parametri `?pli=1&authuser=0`) + portale AFGP, per non perderli.
6. **v1.5 (01/10/2026)**: §1 punto 8 — promemoria **account personale vs scuola**: su alcune
   postazioni Nicola è loggato col personale e il sito sicurezza non si apre; ricordargli di
   passare all'account `@piamarta.it` (ragazzi: `@studenti.piamarta.it`).
7. **v1.6 (01/10/2026)**: §2 punto 12 — parola chiave **"monito"**: monitora i ragazzi e
   aggiungi le osservazioni al **Report andamento classe** (uno per classe, RISERVATO, repo
   privato, documento che cresce nel tempo).
8. **v1.7 (01/10/2026)**: §2 punto 13 — **griglie totali ⇒ sempre anche il Report di
   monitoraggio allievi** (fa parte dell'andamento dell'ora).
9. **v1.8 (01/10/2026)**: §2 punti 14-15 (dopo errori su CHIUDI 2INF): **14** CHIUDI impacchetta
   a prova di privacy (file per allievo separati + documenti docente a parte, mai tutto in un
   unico pacchetto consegnabile); **15** mai attribuire al docente valutazioni/voti/"prima
   lettura" che non ha dato — nei libri degli allievi niente "Valutazione del docente", lo
   spazio voto resta vuoto finché non lo compila Nicola.
10. **v1.9 (01/10/2026)**: §2 punto 15 **corretto** — l'AI **DÀ** voto e giudizio (utili al
    ragazzo), ma la sezione si intitola **"Valutazione dell'AI"**, mai "del docente". Prima
    avevo tolto la valutazione: era sbagliato; va messa, solo attribuita all'AI. Standard del
    compito allineato alla Classe 3: 5 documenti docente (scheda valutazione, dossier evidenze
    col testo reale, report complessivo con anti-plagio + indicazioni ragazzi + segnalazioni,
    griglia, incrementale), voti in **scala /10** come proposta dell'AI.
11. **v2.0 (01/10/2026)**: §2.5 — **eccezione**: il deliverable finale di `CHIUDI classe` (lo
    ZIP) si **versiona nel repo privato** (`dati/chiusure/<CLASSE>/`). Fissato dopo l'errore di
    non aver versionato lo ZIP di chiusura 2INF (vedi `REGISTRO-ERRORI-CLAUDE.md`).
12. **v2.1 (01/10/2026)**: §2 punto 16 — **report "lezioni precedenti" sempre prima di proporre
    argomenti** (dal registro svolti). Fissato dopo l'errore di aver proposto argomenti senza
    prima dare il quadro dello svolto (vedi REGISTRO-ERRORI).
13. **v2.2 (01/10/2026)**: §2 punti 17-18 + §7 — **17** integrare sì, introdurre argomenti nuovi
    solo dopo confronto ("nel dubbio chiedi"); **18** la **foto della lavagna va dentro la
    dispensa di teoria**; §7 — corr. in sospeso sulla dispensa bit/byte (due direzioni, da
    separare). Dopo i rilievi di Nicola sulla dispensa bit/byte.
14. **v2.3 (01/10/2026)**: §2 punto 19 — **stesse cose = stesso layout IDENTICO**: dispensa e
    compito sullo stesso argomento devono avere la grafica identica (gestita come immagini), con
    spazio per i conti a mano sotto. Dopo che il compito bit/byte usava una griglia diversa dalla
    dispensa e i ragazzi si erano persi.
15. **v2.4 (01/10/2026)**: §2 punto 12 — **screenshot Veyon senza testo = comando monitor**
    (osserva e registra con l'orario, senza altre parole).
16. **v2.5 (02/10/2026)**: §2 punti 20-21 — **solo copia-incolla passo per passo** (mai far
    scrivere/editare a Nicola) e **nomi sensati agli script**. + visione pipeline automazione
    (file dedicato) e scelta ponte: Git come scambio (opzione B).
17. **v2.6 (02/10/2026)**: §2 punto 22 — **scheda sintetica per la lezione frontale** del
    docente, sempre e per prima, per ogni nuovo argomento.
18. **v2.9 (02/10/2026)**: §2 punto 25 — **argomenti del registro CORTI** (max ~40 caratteri,
    uno per ora): la casella del registro taglia il testo lungo.
19. **v2.10 (04/10/2026)**: §2 punto 27 — **indentazione Lazarus**: if/else allineati, begin/end allineati, il resto indentato.
20. **v2.11 (05/10/2026)**: §2.28 ogni correzione di Nicola → registro errori + regola; §2.29 testi Classroom già impaginati.
21. **v2.12 (05/10/2026)**: §2.30 comando "Chiudi classe" (libro individuale per allievo + griglie e report per il docente).
22. **v2.13 (05/10/2026)**: §2.31 in docs/ i PDF già usati non si cancellano durante le lezioni.
23. **v2.14 (05/10/2026)**: §2.32 monitoraggio Veyon: dalla miniatura solo fatti, mai giudizi.
24. **v2.15 (05/10/2026)**: §2.33 in classe solo testo del compito + link docente.
25. **v2.16 (05/10/2026)**: §2.34 lavori su GitHub: la consegna la genera Claude.
26. **v2.17 (05/10/2026)**: §2.35 assenti esclusi sempre; §2.36 traccia del fuori compito; §2.37 controlli senza API.
35. **v2.26 (06/10/2026)**: §2.45 tutta la suite Google in automatico (coda e ponte Google, automazione v5).
38. **v2.29 (08/10/2026)**: §2.49 lingue della 2INF: italiano e cinese, l'arabo non serve.
37. **v2.28 (07/10/2026)**: §2.48 il modo di lavorare in classe: pubblica, istruzioni personalizzate («Il mio punto»), segui, traccia gli screenshot.
36. **v2.27 (07/10/2026)**: §2.46 chi ha finito può fare lavori di altre materie o di informatica; §2.47 parte tecnica separata dalla teoria, non consegnati a 40 nella media tecnica.
34. **v2.25 (06/10/2026)**: §2.44 voti su DIDAweb: materia per argomento, minimo 40, un lavoro per volta.
33. **v2.24 (06/10/2026)**: §2.43 lista standard valutazioni per il docente e Valutazione complessiva della classe.
32. **v2.23 (06/10/2026)**: §2.42 recupero a fianco (pagine semplificate + elenco del docente).
31. **v2.22 (05/10/2026)**: §2.41 solo strumenti provati e approvati da Nicola; flusso completo compito → Classroom → voti → archivio prove.
30. **v2.21 (05/10/2026)**: §2.40 controllo dei lavori su GitHub: ricerca + git clone.
29. **v2.20 (05/10/2026)**: §2.39 un solo compito aperto alla volta, titoli descrittivi con l'ordine.
28. **v2.19 (05/10/2026)**: §2.38 su Classroom e nelle pagine solo il lavoro del giorno.
27. **v2.18 (05/10/2026)**: §2.30 punti 4-5: chiusura consultabile con un clic in una pagina privata (dopo "pubblica"); ordine fisso della chiusura.

## 7. Correzioni in sospeso (doc già su Classroom)
*Qui si annotano le modifiche a documenti GIÀ pubblicati su Classroom (regola §2.11): NON si
applicano in automatico. Si applicano solo quando Nicola lo dice; poi si tolgono da qui e si
bumpa la versione del doc.*
1. **Dispensa "Bit, byte e numeri binari" (Classe 1, 01/10/2026):** contiene **tutte e due le
   direzioni** (binario→decimale e decimale→binario, sez. 7). Scelta didattica di Nicola: fare
   **prima solo binario→decimale**, l'altra direzione dopo → avere entrambe nello stesso foglio
   può confondere. **NON si rifà ora** (il file è già in mano ai ragazzi). Alla **prossima
   versione**: separare — dispensa A solo binario→decimale, dispensa B decimale→binario.
   Il **compito** (non ancora pubblicato) si fa invece **su una sola direzione: binario→decimale**.

### 2.50 Prima di proporre ai ragazzi: «Pubblico o vuoi vederlo prima?» (09/10/2026)

1. Prima di proporre qualsiasi cosa agli allievi (compito, Documento, quiz, Modulo, annuncio, pagina) Claude chiede SEMPRE a Nicola: «Pubblico o vuoi vederlo prima?».
2. Si pubblica solo dopo «pubblica» o un sì esplicito; un orario detto prima non vale come via (REGISTRO-ERRORI #41).

### 2.51 Ordine fisso: teoria, poi compito, poi approvazione (09/10/2026)

1. La prima cosa di ogni lezione è analizzare con Nicola la teoria proposta da Claude.
2. Poi si analizza il compito: lo devono poter iniziare tutti, un passo piccolo alla volta, tutto al computer, senza foto né telefono.
3. Si pubblica solo dopo l'approvazione esplicita di Nicola.
