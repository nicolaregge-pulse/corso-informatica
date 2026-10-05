# Riferimenti rapidi e decisioni (Nicola ↔ Claude)

**Versione 2.12** — 05/10/2026

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
