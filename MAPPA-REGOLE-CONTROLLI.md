# 00 Mappa regole e controlli

**Versione 1.33** — 23/11/2026 (sezione 08 nuova: controlli rimessi; le righe rimesse o risolte altrove sono corrette nella tabella) · prima v1.32 (23/11/2026, sezione 07: banco di prova degli errori) · prima v1.31 (23/11/2026, righe #386-#389: controlli costruiti, da D ad A) · prima v1.30 (20/11/2026, righe #384-#389) · prima v1.29, 19/11/2026 — documento interno del docente e di Claude

Nicola, 28/10/2026: Claude conosce le regole ma non le applica nel momento dell'azione. Rimedio: ogni regola nata da un errore diventa un controllo che scatta da solo nel momento giusto, senza dipendere dalla memoria di Claude. Questa mappa prende TUTTE le voci di `REGISTRO-ERRORI-CLAUDE.md` (v2.86: le voci antiche del 01/10 e del 02/10 numerate per giorno, poi dal #1 al #138, con il #82 usato due volte) e dice, per ognuna, quale controllo la copre.

## 01 Conteggio

1. Voci del registro contate qui: 200 (le 13 dal #158 al #170 aggiunte dal controllore di fine giornata del 30/10/2026, tutte A; prima: 187, 14 del 01/10, 15 del 02/10, 139 numerate dal #1 al #138 con il #82 doppio, le 8 voci dal #139 al #146 e le 8 dal #147 al #154 del 29/10/2026, le 3 dal #155 al #157 del controllore di fine giornata del 29/10/2026).
2. Copertura dopo i controlli aggiunti il 28/10/2026 sera, e prima:

| Copertura | Ora | Prima |
|---|---|---|
| A controllo automatico | 83 | 21 |
| B passo obbligatorio notturno | 46 | 13 |
| C superata | 4 | 4 |
| D scoperta | 54 | 149 |
| Totale | 187 | 187 |

3. Voci per schema dell'errore, con la copertura di adesso:

| Schema | Voci | A | B | C | D |
|---|---|---|---|---|---|
| 1 non applica la regola sapendola | 46 | 31 | 8 | 0 | 7 |
| 2 dichiara senza verificare | 39 | 22 | 8 | 0 | 9 |
| 3 promette invece di costruire | 5 | 2 | 1 | 1 | 1 |
| 4 prepara in ritardo | 27 | 6 | 16 | 0 | 5 |
| 5 scrive per sé e non per chi legge | 24 | 10 | 5 | 0 | 9 |
| 6 altro | 46 | 12 | 8 | 3 | 23 |

4. Lettura: lo schema 1 (la regola c'era e non l'ho applicata) è coperto da A o B in 38 voci su 45, lo schema 2 (ho dichiarato senza verificare) in 23 su 32. Le voci scoperte sono soprattutto giudizi didattici o di progetto (schema 6) e lavori fatti in lezione che non passano da un file, da un comando o da un messaggio.

## 02 Legenda

1. Schema dell'errore.
   1.1. 1: non applica la regola sapendola.
   1.2. 2: dichiara senza verificare.
   1.3. 3: promette invece di costruire.
   1.4. 4: prepara in ritardo.
   1.5. 5: scrive per sé e non per chi legge.
   1.6. 6: altro.
2. Copertura.
   2.1. A: controllo automatico già attivo (hook di Claude Code, script che si ferma da solo, oppure rimedio nel codice che rende l'errore impossibile).
   2.2. B: passo obbligatorio dell'attività notturna «Chat del giorno» (o dell'audit pre-lezione delle 06:50), con un comando o una domanda sì/no.
   2.3. C: regola superata da una decisione successiva.
   2.4. D: scoperta; nella sezione 05 il perché e che cosa servirebbe.

## 03 I controlli

1. `.claude/hooks/controllo-messaggio.py` (prima che il messaggio arrivi al docente; blocca una volta e Claude riscrive).
   1.1. (a) ordine copia/incolla (#50 #138).
   1.2. (b) cosa bloccante nelle prime 2 righe (#137).
   1.3. (c) «fatto», «a posto», «funziona», «risolto» senza prova (#63 #115 #135).
   1.4. (d) «pubblicato», «tutto pronto» per una classe senza verifica_lezione.py VERDE (#105 #128).
   1.5. (e) link al sito senza «PUBBLICATO» delle ultime modifiche di docs/ (#79), nuovo.
   1.6. (f) tempi promessi per ciò che fa lo script, senza piano B (#129 #130), nuovo.
   1.7. (g) stringa DIDAweb senza «Disciplina» o con voti sotto 40 (#98 #117; 05/10 n. 23), nuovo.
   1.8. (h) «nessuna AI» senza aver visto tutte le finestre (#90), nuovo.
   1.9. (i) «utente non indicato» invece di chiedere chi c'è (#100), nuovo.
   1.10. (j) «onestamente», «sinceramente» (#53), nuovo.
   1.11. (k) passi come catene di coordinate (#56), nuovo.
   1.12. (l) istruzioni con «salta al passo» o «se è già aperta» (#55), nuovo.
   1.13. (m) firma ricordata quando FIRME-REGISTRO dice tutto firmato (#36 #52 #87 #96), nuovo.
   1.14. (n) richiesta di registrare un errore senza il numero della voce (#113), nuovo.
   1.15. (o) link al riservato senza «personale»; script copiato dal riservato (#48), nuovo.
   1.16. (p) indirizzo diretto del progetto Apps Script (regola 10), nuovo.
   1.17. (q) più di 30 righe di testo nelle ore di lezione (05/10 n. 6), nuovo.
   1.18. (r) «non ha consegnato», «non risulta» senza dire dove si è controllato (#83 #95), nuovo.
   1.19. (s) «ha copiato» detto come certo (01/10 n. 6), nuovo.
   1.20. (t) «al tuo avanti» quando il docente ha chiesto «dammi», «fammi» (05/10 n. 21), nuovo.
   1.21. (u) rimando a riquadri di messaggi precedenti (05/10 n. 31), nuovo.
   1.22. (v) Ctrl+V in Apps Script senza il file automazione-corso.gs (#51), nuovo.
   1.23. (w) «N consegnati su M» senza fonte e ora della lettura (#151), 29/10/2026.
   1.24. (x) attività automatica o notturna dichiarata pronta senza giro di prova (#152), 29/10/2026.
   1.25. (y) pagina provata solo con dati simulati «?prova=1» (#153), 29/10/2026.
   1.26. (z) domanda al docente su presenze o voti già nei file del giorno (#154), 29/10/2026.
   1.27. (aa) release «della cartella» o «del progetto» senza dire che vale per tutto il repository (#157), 29/10/2026 sera.
   1.28. (bb) più di 2 aiutanti accesi insieme (#143), 29/10/2026 sera.
   1.29. (ff) formato dei kit e dei documenti, 12/11/2026 (#282, #285-#289, #291, #293, #309, #311, #312): legge l'ultimo turno dalla trascrizione e controlla R-A cornice blu intorno a ogni SendUserFile (.pdf, .docx, .xlsx, .csv, .zip), R-B al massimo un PDF con le righe rosse, R-C nessuno strumento prima del kit, R-D kit Classroom (rosso in testa, TITOLO e OGGETTO in riquadri, rosso come ultima riga), R-E frase vietata nell'oggetto, R-F cornice verde nei messaggi che non sono kit. Prove: `.claude/hooks/prove/prova_formato_kit.py`.
2. `.claude/hooks/limite-comandi.py` (prima di ogni comando Bash).
   2.1. Massimo 3 comandi per turno e 600 caratteri, solo sessione principale (#132).
   2.2. Cancellare una versione in docs/ (PDF o «vN.N») con rm o git rm: rifiutato, per tutti (01/10 n. 13, #4), nuovo.
   2.3. Push del pubblico: le pagine cambiate passano da `controlli_pagine.py` (lingue della classe, link alla Regione, nomi in chiaro, sintassi degli script; #49 #82 #85 #118 #119 #136), per tutti, nuovo.
   2.4. Push del riservato: coda/ e comandi/ devono leggersi (#12), per tutti, nuovo.
   2.5. `controlli_pagine.py`, controllo `valore_nudo` (29/10/2026 sera): un voto o un PC scritto nella pagina senza controllo del vuoto (mostra «null») blocca il push (#146, #156).
3. `generatori/verifica_lezione.py` del riservato: compito PUBLISHED, pagina pubblicata e, nuovo, annuncio più recente con «OGGI…» (#94); l'hook (d) lo esige prima di «pubblicato».
4. `generatori/audit_regole.py` del riservato (passi notturni 01.1), nuovo: pagine cambiate (lingue, Regione, «arriva tra poco», nomi, sintassi, Modulo con incolla, foto e telefono, link a file mancanti), un compito e un annuncio per classe al giorno, scadenze sulle campanelle, istruzioni impaginate, comandi del ponte (fermi, troppo grandi, non archiviati, più di 40 al giorno), versioni cancellate, sezione del giorno in FIRME-REGISTRO.
5. `.claude/passi-notturni.md`, nuovo: i comandi notturni, 15 domande sì/no sulla lezione del giorno (dalla v1.1 anche la regola 28) e 4 promemoria a orario (firma alle 13:30, piano B 10 minuti prima, fine classe, argomenti svolti alle 14:10); dalla v1.1 l'ultimo passo scrive `stato/notte-<giorno>.json` nel riservato e `strumenti/controlla_controlli.py` controlla che i controlli siano vivi (controllore del controllore).
6. Già attivi: Chat del giorno, passo 5 (pagina, compito in bozza, quiz, cruscotto con le consegne, piano B, battito, 2 allievi confrontati con la fonte); audit pre-lezione delle 06:50 (comandi fermi, pubblicazione, sei bottoni, consegne «SOLO QUI»); `versiona-tutto.sh`.
7. Prove: `.claude/hooks/prove/prova_messaggio.py` (74 casi dal 29/10/2026), `.claude/hooks/prove/prova_limite.py` (27 casi dalla v1.1: anche mv e git mv di una versione), `generatori/prova_audit_regole.py` del riservato (11 casi): tutti superati il 28/10/2026. Ogni controllo, se si rompe, esce con 0 e non blocca.
8. Regola 30 di CLAUDE.md (29/10/2026), nuovo: le criticità per il docente stanno in `docs/cruscotto/criticita.json` e nel bottone rosso «Serve te (N)» del cruscotto, riletto ogni minuto; i «Fatto» del docente arrivano in `dati/verifiche/docente-<classe>/arrivi/` (tipo «fatto») e `strumenti/aspetta_scelta.sh` del riservato li stampa come «FATTO …». A ogni giro Claude toglie le voci risolte; quello che può fare da solo non ci va.
9. `strumenti/controlla_controlli.py`, controlli aggiunti il 29/10/2026 pomeriggio: formato dei JSON delle pagine compatibile con le versioni delle ultime 24 ore (#147); pagina del docente e dei ragazzi con lo stesso «generato» (#148); quiz del giorno letti tutti insieme dal ponte e ogni quiz del giorno con il suo comando di lettura (#149); Sicurezza preparata prima della lezione, con l'ora dopo pronta (#150); notte ROSSA se finita dopo le 6:30 o con il controllore non eseguito (#152). Prove: `strumenti/prova_controlla_controlli.py` (24 casi) e `strumenti/prova_situazione_quiz.py` (6 casi, abbinamento dei cognomi composti), lanciate anche da `controlla_controlli.py`.

10. `strumenti/controlla_controlli.py --fine-giornata AAAA-MM-GG` (29/10/2026 sera; gira anche ogni mattina sul giorno prima): compito uscito su Classroom entro la campanella (#141), piano con «pubblicata» (#140, #144), verifica della lezione VERDE, presenze nel diario, ultimo cruscotto con una riga per presente, senza «null» e senza 40 a chi ha finito (#142, #146, #156), report PDF di ogni ora (regola 24), domande del giorno con risposta (regola 22, #145), `report/<giorno>/non-andato.md` scritto (#155).

## 04 Tabella delle voci

| Voce | Regola | Schema | Prima | Ora | Dove scatta |
|---|---|---|---|---|---|
| 01/10-1 | I libri degli allievi si consegnano cifrati, una password per allievo | 6 | A | A | rimedio nel codice: generatori di chiusura build_chiudi_*_full.py |
| 01/10-2 | La valutazione nei libri si intitola «Valutazione dell'AI», mai del docente | 6 | A | A | rimedio nel codice: build_chiudi_*_full.py scrivono «Valutazione dell'AI» |
| 01/10-3 | Voto e giudizio restano nel libro, attribuiti all'AI | 6 | D | A | come 01/10-2 |
| 01/10-4 | La chiusura segue lo standard completo (anti-plagio, dossier, report, voti /10) | 4 | D | D | procedura rara di fine compito: servirebbe una lista di controllo dentro il generatore di chiusura |
| 01/10-5 | Prima si capisce l'accordo mancato, poi si agisce | 5 | D | D | comprensione: non si controlla con parole o file |
| 01/10-6 | Anti-plagio sempre al condizionale, «da verificare» | 2 | D | A | avviso `controlli_ripristinati.avviso_ha_copiato`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (s), «ha copiato» detto come certo) |
| 01/10-7 | Nel libro dell'allievo solo ciò che riguarda lui, niente indicazioni per il docente | 6 | D | D | contenuto dei libri: servirebbe un controllo nel generatore di chiusura |
| 01/10-8 | Le password consegnate restano fisse a ogni rigenerazione | 6 | A | A | rimedio nel codice: password fisse nei generatori |
| 01/10-9 | Password solo sui libri degli allievi, documenti del docente aperti | 6 | A | A | rimedio nel codice: generatori di chiusura |
| 01/10-10 | Lo ZIP finale di chiusura si archivia nel riservato | 1 | A | A | hook Stop versiona-tutto.sh (blocca se qualcosa non è committato e pushato) |
| 01/10-11 | Prima delle proposte, il report delle lezioni precedenti | 4 | D | B | passi-notturni.md 02.1, storia della classe |
| 01/10-12 | Niente argomenti nuovi non spiegati in classe senza confronto | 6 | D | D | giudizio didattico: servirebbe la foto della lavagna nel diario |
| 01/10-13 | Le versioni non si cancellano: si bumpa e si tengono | 1 | D | A | hook limite-comandi.py (cancellazione di versioni in docs/ rifiutata) + audit_regole.py (passi notturni 01.1) 07 |
| 01/10-14 | Compito e dispensa dello stesso argomento con grafica identica | 6 | D | D | giudizio visivo: servirebbe generare le due cose dalla stessa immagine |
| 02/10-1 | Dire subito i limiti di ciò che si costruisce; via rapida (piano B) sempre pronta | 3 | B | B | Chat del giorno, passo 5 (piano B) + passi-notturni.md 03.2 |
| 02/10-2 | Ogni passo che apre un sito parte da un link in una casella da copiare | 5 | D | D | non si riconosce in automatico quale passo apre un sito |
| 02/10-3 | Ogni compito ha il Documento da compilare, in ogni via di pubblicazione | 4 | D | D | servirebbe un controllo del piano B (gen_pianob.py) sul Documento allegato |
| 02/10-4 | Non introdurre un metodo alternativo: si semplifica quello della lavagna | 6 | D | D | giudizio didattico |
| 02/10-5 | Ogni dato operativo del docente (campanelle) va subito in un file | 4 | D | B | audit_regole.py (passi notturni 01.1) 04, scadenze sulle campanelle di RIFERIMENTI §1.10 |
| 02/10-6 | In classe si congela ciò che è pubblicato; si corregge solo un errore bloccante | 1 | D | D | bloccare i push in lezione fermerebbe anche le correzioni urgenti |
| 02/10-7 | Un argomento = una teoria + un compito | 6 | D | D | giudizio didattico |
| 02/10-8 | Prima di pubblicare si guarda ogni pagina di ogni lingua (render a immagine) | 2 | D | D | servirebbe un controllo automatico dei PDF (titoli orfani, tabelle tagliate) |
| 02/10-9 | Nelle istruzioni di Classroom solo il link unico della pagina, mai PDF versionati | 6 | D | C | regola superata: oggi i PDF dei ragazzi vanno come Allegato del post (kit di `report/2026-11-20/KIT-CLASSROOM-*.md`, formato PDF #388) e li controlla `controlla_kit.py`; il link unico non è più l'unica forma. Fonte: kit del 20/11/2026, CLAUDE.md R2.3 (23/11/2026: era A, controllo (m) tolto il 04/11) |
| 02/10-10 | Versione in copertina, pagina senza cache, Ctrl+F5 | 6 | D | D | la memoria del browser del docente non si vede da qui |
| 02/10-11 | Mai agganciare un compito manuale prima che il docente lo crei | 6 | C | C | superata: dal 21/10 i compiti nascono solo dalla coda, in bozza (script v8.2) |
| 02/10-12 | Non far modificare un compito durante la lezione (sale in cima) | 6 | D | D | consiglio dato in chat: nessuna parola sicura da cercare |
| 02/10-13 | Una azione per messaggio quando la situazione è nuova; punto esatto dello screenshot | 5 | D | A | hook controllo-messaggio.py (q) messaggi lunghi in lezione, (k) catene di coordinate |
| 02/10-14 | Ogni chiave di correzione ha la versione nel nome, mai sovrascritta | 6 | D | D | servirebbe il divieto di sovrascrivere chiavi nei generatori |
| 02/10-15 | Controllo aritmetico automatico degli esempi prima del PDF | 3 | D | D | promesso e mai costruito: servirebbe nel generatore delle dispense |
| #1 | I testi per Classroom vanno impaginati (una riga per passo) | 5 | D | B | audit_regole.py (passi notturni 01.1) 04 (righe più lunghe di 300 caratteri) |
| #2 | Titoletti in maiuscolo, numeri, righe vuote tra i blocchi | 5 | D | B | come #1 |
| #3 | Tutto ciò che il docente segnala va nel registro e in una regola | 1 | D | A | avviso `controlli_ripristinati.avviso_con_docente` (registrazione senza il numero #NNN). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (n) richiesta di registrare un errore senza numero) |
| #4 | In docs/ le versioni già usate in classe non si cancellano | 1 | D | A | hook limite-comandi.py (cancellazione di versioni rifiutata) + audit_regole.py (passi notturni 01.1) 07 |
| #5 | Dalla miniatura Veyon solo «sulla pagina X alle HH:MM», mai «non ha fatto niente» | 2 | D | A | BLOCCO `controlli_ripristinati.non_caricato_senza_ricerca` («non ha caricato» / «non ha fatto niente» da Veyon / «ha già» da uno screenshot senza la ricerca). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (r) «non ha iniziato / non ha fatto niente» senza fonte) |
| #6 | In classe risposte corte: solo testo da incollare e link | 5 | D | A | hook controllo-messaggio.py (q) più di 30 righe nelle ore di lezione |
| #7 | Quando il lavoro è su GitHub, la consegna la genera Claude | 6 | D | D | scelta di progetto della lezione |
| #8 | Le traduzioni si mostrano solo a chi servono (bangla solo PC 14) | 1 | D | D | la pagina per PC non si distingue in automatico dalla pagina per tutti |
| #9 | Dopo ogni modifica a una pagina con script: node --check e prova | 1 | D | A | hook limite-comandi.py (prima del push: sintassi di tutti gli script) + audit_regole.py (passi notturni 01.1) 01 |
| #10 | La pagina della classe mostra solo il lavoro del giorno | 4 | D | B | passi-notturni.md 02.9 |
| #11 | La firma non si deduce dal bottone «FIRMA ✓» | 2 | D | C | R5.1 di CLAUDE.md v2.0 (04/11/2026): «FIRMA ✓» in verde = firmata; la vecchia regola «la firma non si deduce dal bottone» è abrogata. Fonte: CLAUDE.md R5.1, REGOLE-DA-DECIDERE.md (23/11/2026: era A, controllo (m) tolto il 04/11) |
| #12 | Dopo un rebase i coda/*.json si devono leggere prima del push | 1 | D | A | hook limite-comandi.py (push del riservato fermato con JSON rotti) + audit_regole.py (passi notturni 01.1) 03 |
| #13 | Un solo compito aperto alla volta su Classroom | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 (un compito per classe al giorno) |
| #14 | Caricare file su GitHub con Add file → Upload files; dopo una rigenerazione si contano i riquadri | 6 | D | D | scelta di metodo; la rigenerazione è coperta in parte da passi-notturni.md 02.9 |
| #15 | Mai chiedere di riconoscere un file dall'estensione | 5 | D | D | i nomi di file nelle pagine sono spesso leciti: troppi falsi allarmi |
| #16 | Mai «non ha caricato» senza la ricerca e il clone | 2 | D | A | BLOCCO `controlli_ripristinati.non_caricato_senza_ricerca` («non ha caricato» / «non ha fatto niente» da Veyon / «ha già» da uno screenshot senza la ricerca). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (r)) |
| #17 | File grandi divisi prima; dire quali scaricare e quanti | 5 | D | D | l'invio dei file in chat non passa da un hook |
| #18 | Chiusura dopo l'ultima raccolta; abbinamenti sul cognome intero | 6 | D | D | servirebbe un controllo nei correttori |
| #19 | Segnalazioni di guasti salvate nel riservato; prima di «mai segnalato» si guarda lì | 2 | D | D | servirebbe un elenco dei guasti letto dall'audit |
| #20 | Ripubblicando una pagina che si salva da sola, il blocco dati si sostituisce una volta | 1 | D | A | hook limite-comandi.py (sintassi degli script prima del push) |
| #21 | Se un risultato è stato chiesto, si consegna appena pronto (il PPP non lo ferma) | 1 | D | A | avviso `controlli_ripristinati.avviso_con_docente` («al tuo avanti» dopo «dammi/fammi»). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (t) «al tuo avanti» dopo «dammi/fammi») |
| #22 | Prima di una media, ogni colonna è un lavoro diverso | 6 | D | D | servirebbe un controllo nel generatore delle griglie |
| #23 | Materia del voto dall'argomento; voto minimo 40 | 1 | D | A | avviso `controlli_ripristinati.avviso_didaweb` (Disciplina da scegliere, voti da 40). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (g) voti sotto 40 e Disciplina nella stringa DIDAweb) |
| #24 | I passaggi che si possono automatizzare si automatizzano subito | 3 | C | C | superata: i quiz su Moduli li crea il ponte (forms.crea_quiz) |
| #25 | Una sola lista di password per classe; prova di apertura di ogni libro | 1 | D | D | servirebbe la prova di apertura dentro il generatore dello zip |
| #26 | Ogni file personale comincia con Cognome-Nome | 5 | D | D | servirebbe un controllo nei generatori dei libri |
| #27 | Ogni PDF si apre e si controlla prima di mandarlo | 2 | D | D | l'invio dei file in chat non passa da un hook |
| #28 | Uno strumento per un sito esterno si prova sull'HTML vero | 2 | D | D | giudizio di progetto |
| #29 | Link al riservato sempre con «apri il profilo personale» | 1 | D | A | hook controllo-messaggio.py (o) |
| #30 | Lavori uguali in due caselle = una colonna sola | 6 | D | D | come #22 |
| #31 | Ogni messaggio con passi ha TUTTE le caselle da copiare | 5 | D | A | BLOCCO `controlli_ripristinati.rimando_a_riquadri_di_prima`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (u) rimando a riquadri di prima) |
| #32 | Mai due copie in fila: la seconda cancella la prima | 1 | A | A | hook controllo-messaggio.py (a) ordine copia/incolla |
| #33 | Prima di nominare un materiale, si dice dove trovarlo | 5 | D | D | non si sa in automatico se i ragazzi hanno un materiale |
| #34 | Mentre un comando che pubblica è in attesa non si spinge altro; un annuncio solo | 1 | D | B | audit_regole.py (passi notturni 01.1) 05 (un annuncio per classe al giorno) |
| #35 | A fine ora si consegna quello che c'è; zip pronto 10 minuti prima | 4 | D | B | passi-notturni.md 03.3 (promemoria 10 minuti prima della fine) |
| #36 | La firma non si deduce dal bottone (ripetizione di #11) | 1 | D | C | R5.1 di CLAUDE.md v2.0 (04/11/2026): «FIRMA ✓» in verde = firmata; regola abrogata. Fonte: CLAUDE.md R5.1 (23/11/2026: era A, controllo (m) tolto il 04/11) |
| #37 | «Script fermo» solo dopo una prova del ponte | 2 | B | B | Chat del giorno, passo 5 (battito con un comando del ponte); la frase «esce entro 5 minuti» è superata da #130 |
| #38 | Progetto di squadra: un canale, tutti consegnano, prima fase entro 20 minuti | 4 | D | B | passi-notturni.md 02.4 e 02.7 |
| #39 | Orari dall'ora vera; una cosa da fare per volta; modifiche verificate | 2 | D | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: lezione in corsa; solo «modifiche verificate» è coperta da hook controllo-messaggio.py (c)) |
| #40 | Ogni riga di un report porta almeno il nome visibile | 5 | D | D | servirebbe un controllo sulle pagine del docente (cifrate) |
| #41 | Pubblicare solo con il via; formato riscritto e confermato; lingue della classe | 6 | C | C | superata dalla regola 17 (21/10: Claude pubblica da solo); le lingue sono coperte da hook limite-comandi.py |
| #42 | Consegne da un canale che accetta invii ripetuti | 6 | C | C | superata da #68 e #81 (una sola strada, UN bottone) |
| #43 | In 1INF un solo compito che possono iniziare TUTTI | 5 | D | B | passi-notturni.md 02.2 |
| #44 | In laboratorio tutto al computer: niente foto né telefono | 6 | D | B | audit_regole.py (passi notturni 01.1) 01 (foto e telefono nelle pagine) + passi-notturni.md 02.2 |
| #45 | Niente attività a mano se il docente non le chiede | 6 | D | B | passi-notturni.md 02.2 |
| #46 | Il testo da scrivere è già nel messaggio, in un riquadro | 1 | D | D | non si sa in automatico quale testo il docente dovrà scrivere |
| #47 | Campi indicati per posizione; ogni passo finisce con «Dopo devi vedere» | 5 | D | D | giudizio di scrittura |
| #48 | Lo script si copia dal link pubblico, mai dal riservato | 1 | D | A | hook controllo-messaggio.py (o) |
| #49 | 2INF solo italiano: ogni pagina passa dal controllo delle lingue | 1 | D | A | hook limite-comandi.py (prima del push: lingue della classe) + audit_regole.py (passi notturni 01.1) 01 |
| #50 | Memoria del copia e incolla vuota; prima la pagina d'arrivo | 1 | A | A | hook controllo-messaggio.py (a) |
| #51 | Prima di incollare in Apps Script si clicca automazione-corso.gs | 5 | D | A | avviso `controlli_ripristinati.avviso_apps_script`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (v) e (p)) |
| #52 | Firma: mai dedotta dallo screenshot (terza volta) | 1 | D | C | R5.1 di CLAUDE.md v2.0 (04/11/2026): «FIRMA ✓» in verde = firmata; regola abrogata. Fonte: CLAUDE.md R5.1 (23/11/2026: era A, controllo (m) tolto il 04/11) |
| #53 | Niente avverbi e aggettivi che non servono | 5 | D | A | avviso `controlli_ripristinati.avviso_stile`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (j)) |
| #54 | Le considerazioni del docente non si interpretano: una domanda sola | 6 | D | D | intenzione del docente: non controllabile |
| #55 | Istruzioni senza «se», «salta», domande | 5 | D | A | avviso `controlli_ripristinati.avviso_stile`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (l)) |
| #56 | Passi come frasi che cominciano con il verbo, non catene di coordinate | 5 | D | A | avviso `controlli_ripristinati.avviso_stile`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (k)) |
| #57 | Ripetizione di #50 | 1 | A | A | hook controllo-messaggio.py (a) |
| #58 | Comandi eseguiti archiviati; dopo un comando controllo entro 2 minuti | 6 | D | B | audit_regole.py (passi notturni 01.1) 06 (comandi non archiviati e fermi) |
| #59 | Ogni richiesta del docente va subito nell'elenco dei lavori aperti | 4 | D | D | non si riconosce in automatico una richiesta dentro un PPP |
| #60 | Ogni pagina dei ragazzi ha i bottoni per autoregolarsi | 1 | B | B | audit pre-lezione delle 06:50 punto 3 + passi-notturni.md 02.10 |
| #61 | Verifica provata con ricarica, chiusura, bottoni e consegna fino all'arrivo | 2 | A | A | rimedio nel codice del motore della verifica (salvataggio ogni 2 secondi, ripresa) + prova_verifica.js |
| #62 | Ai ragazzi una azione per frase; la consegna è UN bottone | 5 | D | B | audit_regole.py (passi notturni 01.1) 01 (Modulo + incolla) + passi-notturni.md 02.7 |
| #63 | «Fatto» o «non serve più» solo dopo la prova | 2 | A | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (c) e (d)) |
| #64 | Mai chiedere una risposta nella pagina che quel passo chiude | 6 | D | D | chat con i ragazzi su GitHub: non passa dagli hook |
| #65 | Con i ragazzi un messaggio = un'azione + una domanda chiusa | 5 | D | D | come #64 |
| #66 | Con il codice prima capire, poi incollare | 6 | D | D | giudizio didattico |
| #67 | Prima di proporre una strada si guarda lo schermo vero del ragazzo | 6 | D | D | giudizio in lezione |
| #68 | Una sola strada di consegna, letta in tempo reale, provata come un ragazzo | 4 | D | B | passi-notturni.md 02.7 |
| #69 | Anche per i maggiorenni solo le iniziali | 1 | D | D | manca l'elenco della 4TI nel config: aggiunto quello, lo coprirebbe hook limite-comandi.py |
| #70 | Un gioco si prova sul sito vero, file compressi, senza memoria | 2 | D | D | github.io non è raggiungibile da qui (proxy) |
| #71 | Le pagine dei sei bottoni passano al giorno nuovo prima del compito | 4 | B | B | passi-notturni.md 02.10 + audit pre-lezione delle 06:50 punto 3 |
| #72 | Prima di un percorso si controlla che cosa c'è davvero in aula | 6 | D | D | giudizio di progetto |
| #73 | Ogni schermata Veyon va subito nel monitor e nel cruscotto | 4 | D | D | in lezione: servirebbe un giro che segnali le schermate non ancora nel monitor |
| #74 | Per ciò che sa solo il docente, la strada più corta per lui (la chat) | 6 | D | D | giudizio di progetto |
| #75 | L'audit comprende le pagine del docente, bottone per bottone | 2 | D | B | passi-notturni.md 02.10 |
| #76 | Ogni lezione ha il riquadro «Spiegalo in 30 secondi» | 4 | D | B | passi-notturni.md 02.6 |
| #77 | Nessun bottone porta a una pagina vuota | 2 | D | B | passi-notturni.md 02.10 |
| #78 | Lezione pronta e provata prima; percorso dall'alto in basso; pubblicata 3 minuti prima del link | 4 | B | B | Chat del giorno, passo 5 (pagina pronta) + hook controllo-messaggio.py (e) |
| #79 | Il link si dà solo dopo «PUBBLICATO» | 1 | D | A | hook controllo-messaggio.py (e) link al sito senza PUBBLICATO |
| #80 | Nell'audit si controlla il CONTENUTO, non solo che la pagina si apra | 2 | B | B | Chat del giorno, passo 5 (confronto di 2 allievi con la fonte) + passi-notturni.md 02.10 |
| #81 | MAI «copia, apri, incolla»: UN bottone che consegna davvero | 1 | D | B | audit_regole.py (passi notturni 01.1) 01 (pagina con Modulo e «incolla») |
| #82 (15/10) | Prima di scrivere per una classe si controllano le sue lingue | 1 | D | A | hook limite-comandi.py (lingue della classe prima del push) |
| #82 (19/10) | Il battito dello script è una voce di ogni audit e di ogni giro | 2 | B | B | Chat del giorno, passo 5 (battito con un comando del ponte) |
| #83 | Lo screenshot non è la prova: la prova è il file nel repository | 2 | D | A | BLOCCO `controlli_ripristinati.non_caricato_senza_ricerca` («non ha caricato» / «non ha fatto niente» da Veyon / «ha già» da uno screenshot senza la ricerca). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (r) «non ha caricato» senza fonte e (c)) |
| #84 | Un link si mette solo se la pagina esiste | 2 | D | B | audit_regole.py (passi notturni 01.1) 01 (link a file che non esistono) |
| #85 | Nomi e voti in docs/ solo cifrati | 1 | D | A | hook limite-comandi.py (nomi in chiaro prima del push) + audit_regole.py (passi notturni 01.1) 01-02 |
| #86 | Finita una classe, il giro di quella classe si ferma | 4 | D | B | passi-notturni.md 03.3 |
| #87 | «FIRMA ✓» in verde = firmata | 1 | D | A | BLOCCO `controllo-messaggio.controllo_firma_ricordata` (firma ricordata con FIRME-REGISTRO tutto firmato, R5.1). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (m)) |
| #88 | Battito di meno di 3 minuti prima di «lo pubblica lo script» | 2 | D | A | avviso `controlli_ripristinati.avviso_tempi_script`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (f) promesse sui tempi dello script + (d)) |
| #89 | Una sola strada per volta; stesso titolo per l'anti-doppione | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 (un compito per classe al giorno) |
| #90 | «Nessuna AI» solo dopo aver visto tutte le finestre | 2 | D | A | avviso `controlli_ripristinati.avviso_nessuna_ai`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (h)) |
| #91 | Titoli del registro solo sull'Allegato A più recente | 6 | D | D | servirebbe un controllo dei titoli del registro sul .docx dell'Allegato A |
| #92 | «Altro» = presente | 1 | D | D | conteggio dei presenti fatto a mano dallo screenshot |
| #93 | Un solo compito per lezione; quiz diverso dalla verifica | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 |
| #94 | Ogni lezione ha l'annuncio «OGGI FATE SOLO…» in cima | 4 | D | A | verifica_lezione.py (annuncio più recente senza «OGGI» = GIALLO) + hook controllo-messaggio.py (d) |
| #95 | Si legge il massimo di ogni quiz; «non risulta» mai su una fonte sola | 2 | D | D | massimo del quiz: servirebbe nel calcolo dei voti; la parte «non risulta» è coperta da hook controllo-messaggio.py (r) |
| #96 | Colonna «Firma» con data e ora = firmata | 1 | D | A | BLOCCO `controllo-messaggio.controllo_firma_ricordata` (firma ricordata con FIRME-REGISTRO tutto firmato, R5.1). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (m)) |
| #97 | Scadenze sulle campanelle vere | 1 | D | B | audit_regole.py (passi notturni 01.1) 04 |
| #98 | Prima della stringa dei voti, la materia dell'ora | 1 | D | A | avviso `controlli_ripristinati.avviso_didaweb` (Disciplina da scegliere, voti da 40). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (g)) |
| #99 | Prima di preparare una lezione si rilegge la storia della classe | 4 | D | B | passi-notturni.md 02.1 |
| #100 | PC senza nome: si chiede subito chi c'è | 1 | D | A | avviso `controlli_ripristinati.avviso_utente_non_indicato`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (i)) |
| #101 | Terza volta #50: procedura dello script da RIPARTENZA §03 | 1 | A | A | hook controllo-messaggio.py (a) e (v) |
| #102 | Durata stimata dal contenuto e provata a tempo | 6 | D | B | passi-notturni.md 02.5 |
| #103 | Ogni pagina che produce un risultato lo fa arrivare al docente | 6 | D | B | passi-notturni.md 02.8 |
| #104 | «Ponte OK» solo dopo un comando di prova eseguito | 2 | B | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: Chat del giorno, passo 5 (battito) + passi-notturni.md 01.4) |
| #105 | Pubblicare = pagina + compito + annuncio | 2 | A | A | hook controllo-messaggio.py (d) con verifica_lezione.py |
| #106 | I nomi dei bottoni si copiano dalla pagina vera | 2 | D | D | il nome giusto non è noto all'hook |
| #107 | Un solo annuncio e un solo compito al giorno per classe | 1 | D | B | audit_regole.py (passi notturni 01.1) 05 |
| #108 | Nelle tabelle tutti e soli i presenti; abbinamento per cognome | 6 | D | D | servirebbe un controllo nei generatori dei cruscotti |
| #109 | «Fuori compito» solo se lo schermo mostra un'altra attività | 2 | D | D | lettura delle schermate: giudizio |
| #110 | Il primo passo produce qualcosa di visibile entro 10 minuti | 4 | D | B | passi-notturni.md 02.4 |
| #111 | Due ritagli uguali consecutivi: ne resta uno | 6 | D | D | si può aggiungere a report_ore.py un confronto delle immagini |
| #112 | In lezione i giri non spingono sul riservato; si recuperano le righe «SOLO QUI» | 1 | B | B | audit pre-lezione delle 06:50 punto 4 + passi-notturni.md 03.3 |
| #113 | Un errore da registrare si scrive subito, con il numero | 4 | D | A | avviso `controlli_ripristinati.avviso_con_docente` (registrazione senza il numero #NNN). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (n)) |
| #114 | Un comando del ponte = poche azioni e un salvataggio; controllo entro 5 minuti | 1 | D | B | audit_regole.py (passi notturni 01.1) 06 |
| #115 | Mai «risolto» per lo script senza prova nel tempo | 2 | A | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (c)) |
| #116 | Ogni conteggio che dà punti si protegge dagli abusi prima | 4 | D | D | servirebbe una prova con testo finto nei controlli della lezione |
| #117 | Pacchetto DIDAweb con «Disciplina da scegliere» sopra | 1 | D | A | avviso `controlli_ripristinati.avviso_didaweb` (Disciplina da scegliere, voti da 40). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (g)) |
| #118 | Dopo ogni modifica: node --check di tutti gli script e prova | 1 | D | A | hook limite-comandi.py (sintassi prima del push) + audit_regole.py (passi notturni 01.1) 01 |
| #119 | Lingue di ogni classe dai documenti, con un audit | 1 | D | A | hook limite-comandi.py (lingue prima del push) + passi-notturni.md 02.11 |
| #120 | Prima di «pubblicata» i tre pezzi; una cosa decisa si prepara senza richiederla | 1 | A | A | hook controllo-messaggio.py (d) |
| #121 | Prima di un compito si leggono i compiti del giorno su Classroom | 1 | D | D | servirebbe che chi scrive la coda chieda prima classroom.compiti al ponte |
| #122 | La scadenza la decide il docente; non si inventano orari | 6 | D | D | solo il docente sa che cosa ha detto; la campanella è controllata da audit_regole.py (passi notturni 01.1) 04 |
| #123 | Ogni passo per un dodicenne; domande all'assistente lette a ogni giro | 5 | D | B | passi-notturni.md 02.2 |
| #124 | «Mandata!» solo quando l'invio è partito | 2 | A | A | rimedio nel codice: docs/assistente/assistente.js |
| #125 | Pochi comandi al ponte; prova prima di dire che lo script funziona | 1 | D | B | audit_regole.py (passi notturni 01.1) 06 (più di 40 comandi in un giorno) |
| #126 | Versione facile di massimo 3 passi preparata prima | 4 | D | B | passi-notturni.md 02.3 |
| #127 | Dati fermi = ora in rosso; «fatto» solo dopo averlo fatto | 2 | A | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (c); l'ora in rosso nelle pagine è da controllare a mano) |
| #128 | «Tutto a posto» solo dopo le tre prove | 2 | A | A | hook controllo-messaggio.py (d) |
| #129 | Quiz e Moduli prima della campanella; mai «arriva tra poco» | 4 | B | B | Chat del giorno, passo 5 (quiz) + audit_regole.py (passi notturni 01.1) 01 («arriva tra poco») |
| #130 | Non si promettono tempi per ciò che fa lo script | 3 | D | A | avviso `controlli_ripristinati.avviso_tempi_script`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (f)) |
| #131 | Piano B: annuncio pronto 10 minuti prima | 4 | B | B | Chat del giorno, passo 5 (piano B) + passi-notturni.md 03.2 |
| #132 | Comandi di una riga, risultati lunghi in un file | 5 | A | A | hook limite-comandi.py (massimo 3 comandi, 600 caratteri) |
| #133 | Cruscotto progettato sulla consegna del giorno | 4 | B | B | Chat del giorno, passo 5 (cruscotto con la colonna delle consegne) |
| #134 | Ogni audit confronta 2 allievi con la fonte | 2 | B | B | Chat del giorno, passo 5 (confronto di 2 allievi) |
| #135 | «A posto» solo dopo una compilazione riuscita | 2 | A | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (c)) |
| #136 | Nessun link al sito della Regione nelle pagine dei ragazzi | 6 | D | A | hook limite-comandi.py (prima del push) + audit_regole.py (passi notturni 01.1) 01 |
| #137 | La cosa bloccante va da sola nella prima riga | 5 | A | A | hook controllo-messaggio.py (b) + passi-notturni.md 03.1 (firma alle 13:30) |
| #138 | Copia e incolla: un Ctrl+V usa l'ultima cosa copiata | 1 | A | A | hook controllo-messaggio.py (a) |
| #139 | Un ROSSO dell'audit non si liquida come atteso: va in prima riga | 2 | D | A | avviso `controlli_ripristinati.avviso_rosso_atteso`. RIMESSO 23/11/2026 (era: controlla_controlli.py (prima riga «DA SAPERE SUBITO», notte di oggi)) |
| #140 | Un bottone è presente solo se si vede sul sito vero, modalità Docente | 2 | D | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (y) + controlla_controlli.py --fine-giornata (piano con «pubblicata»)) |
| #141 | Nessuna classe in aula con Classroom vuoto | 3 | D | A | controlla_controlli.py (notte girata da sola, #152) + --fine-giornata (compito uscito entro la campanella) |
| #142 | Cruscotto con i KPI del giorno e una riga per presente alla campanella | 4 | D | A | controlla_controlli.py --fine-giornata (righe = presenti) + coppia docente/ragazzi (#148) |
| #143 | Al massimo 2 aiutanti accesi insieme | 6 | D | A | avviso `controllo-messaggio.controlli_con_trascrizione` (più di 2 Agent nel turno). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (bb)) |
| #144 | Dopo la pubblicazione il piano mostra solo la proposta fatta, senza bottoni | 2 | D | A | controlla_controlli.py --fine-giornata (piano senza «pubblicata» = ROSSO) + hook (c) |
| #145 | Le domande del giorno si vedono tutte e hanno risposta | 4 | D | A | controlla_controlli.py --fine-giornata (domande senza risposta, regola 22) |
| #146 | Percorso provato da capo; mai «null» o PC non confermati nel cruscotto | 4 | D | A | controlli_pagine.py (valore_nudo, prima del push) + controlla_controlli.py --fine-giornata (nessun «null») |
| #147 | Un JSON letto da una pagina non perde campi: i vecchi restano come alias | 6 | D | A | controlla_controlli.py (formato dei JSON, #147) |
| #148 | Docente e ragazzi leggono dati dello stesso giro (stesso «generato») | 6 | D | A | controlla_controlli.py (coppia docente/ragazzi, #148) |
| #149 | Tutti i quiz del giorno letti insieme, ognuno con il suo comando | 6 | D | A | controlla_controlli.py (ponte dei quiz, #149) |
| #150 | Sicurezza: compito con quiz e ora dopo pronti prima della lezione | 4 | D | A | controlla_controlli.py (Sicurezza preparata, #150) |
| #151 | Un conteggio di consegne si rilegge alla fonte e porta fonte e ora | 2 | D | A | BLOCCO `controlli_ripristinati.conteggio_senza_fonte`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (w)) |
| #152 | Attività automatica pronta solo dopo un giro di prova vero | 2 | D | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (x) + controlla_controlli.py (notte girata da sola)) |
| #153 | Pagina verificata sul sito vero con i dati veri, non con ?prova=1 | 2 | D | A | BLOCCO `controlli_ripristinati.prova_con_dati_finti`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (y)) |
| #154 | Prima di chiedere al docente si guarda nei file del giorno | 1 | D | A | avviso `controlli_ripristinati.avviso_domanda_su_file_del_giorno`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (z)) |
| #155 | Si misura il risultato: controllore di fine giornata sul dato vero | 2 | D | A | controlla_controlli.py --fine-giornata (report/<giorno>/non-andato.md) |
| #156 | Nessun 40 a chi ha finito o consegnato; senza consegna «voto dopo la consegna» | 6 | D | A | controlla_controlli.py --fine-giornata (40 con percorso finito) + controlli_pagine.py (valore_nudo) |
| #157 | Una release vale per tutto il repository; progetto serio = repository suo | 5 | D | A | avviso `controlli_ripristinati.avviso_release_cartella`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (aa)) |
| #158 | Incolla in Apps Script: clic dentro il codice, Ctrl+A «tutto blu», Ctrl+V, controllo righe | 5 | D | A | avviso `controlli_ripristinati.avviso_apps_script`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (ii)) |
| #159 | «Prima ora» = ora della giornata; nella risposta si scrive l'orario | 6 | D | A | hook controllo-messaggio.py (gg) |
| #160 | Il quiz chiede solo lavoro già fatto prima del quiz | 4 | D | A | controlla_controlli.py --fine-giornata (_quiz_lavoro_futuro) |
| #161 | Mai «non arrivato» su dati di più di 5 minuti; il docente non controlla da solo | 2 | D | A | hook controllo-messaggio.py (hh) + watchdog del laboratorio |
| #162 | Laboratorio di 2-3 ore: un lavoro per ogni ora, pronto entro le 18 del giorno prima | 4 | D | A | controlla_controlli.py --fine-giornata (proposta non divisa ora per ora) |
| #163 | 1INF: ogni materiale per i ragazzi in italiano, arabo e cinese insieme | 1 | D | A | controlla_controlli.py --fine-giornata (dispensa e pagine del piano senza ar/zh) |
| #164 | Ai ragazzi un solo posto: compito del giorno con la pagina hub | 5 | D | A | hook controllo-messaggio.py (ff) + controlla_controlli.py --fine-giornata (troppi compiti «OGGI») |
| #165 | I dati del docente si scrivono in caselle (foglio Google), non in un PDF | 5 | D | A | avviso `controllo-messaggio.controlli_con_trascrizione` (griglia da compilare data in PDF). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (ee)) |
| #166 | Una domanda del docente chiede una spiegazione; si toglie solo con «togli/elimina» | 6 | D | A | avviso `controlli_ripristinati.avviso_con_docente` (domanda presa per un ordine di togliere). RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (cc)) |
| #167 | Il genere di un allievo non si dà per scontato: si usa il nome | 6 | D | A | avviso `controlli_ripristinati.avviso_genere`. RIMESSO 23/11/2026 (era: hook controllo-messaggio.py (dd)) |
| #168 | Script nuovo provato con una bozza vera la sera prima; piano B pronto subito | 4 | D | A | verifica_lezione.py (coda senza id = ROSSO, «sospeso» = verde) + controlla_controlli.py --fine-giornata |
| #169 | I giri del cruscotto lasciano un segnale e si riaccendono; nessun buco > 12 minuti | 2 | D | A | controlla_controlli.py --fine-giornata (buchi nello storico) |
| #170 | Colonna del cruscotto solo dopo un invio vero; fonte vuota detta subito | 2 | D | A | controlla_controlli.py --fine-giornata (colonna «pratica» vuota) + situazione_quiz.py (storico) |
| #223 | Sull Allegato A dopo il 30/10 si puo solo togliere; prima di proporre si leggono le note | 1 | D | D | il controllo dei testi del registro deve dire «voce piu vicina»; ancora da costruire |
| #224 | Proposte fatte senza aver letto le regole | 1 | D | D | promemoria-errori.py deve ricordare, a ogni richiesta di proposta su registro o Allegato A, «prima leggi NOTE-DA-DISCUTERE.md» (da costruire) |
| #225 | Post ora 4 della 1INF pubblicato dal docente senza link | 1 | D | D | Il pacchetto del post (R2.3) deve avere sempre il link gia dentro (da costruire) |
| #226 | Pacchetto voti DIDAweb con «h 1» invece di «h 6» | 2 | D | D | Il generatore del pacchetto voti deve leggere l ora dalla riga del registro e confrontarla (da costruire) |
| #227 | Copiare lfm e pas da Classroom: i ragazzi non ce l hanno fatta | 1 | D | A | BLOCCO prima del push (`controlli_pagine.copia_file_da_classroom`, R9.5) e audit notturno. RIMESSO 23/11/2026 (era: controlli_pagine.py e il controllo del post: un passo che dice «copia» un file senza zip o percorso e un errore (da costruire)) |
| #228 | «Nessun blocco» come prima riga solo per superare il controllo | 1 | D | D | controllo-messaggio.py: la prima riga «Nessun blocco» o simili senza prova non vale (da costruire) |
| #229 | Il cruscotto non aveva il nome di un allievo della 2INF (presenze del giorno prima) | 2 | D | D | Il giro del cruscotto deve confrontare i presenti con il registro presenze e dare ROSSO se ne manca uno (da costruire) |
| #230 | Quiz recuperi 2INF: un allievo della 2INF «Hai gia risposto» | 2 | D | D | I generatori dei quiz creano i Moduli con piu risposte (da costruire) |
| #231 | Testo vecchio in piano-b/ora-6 parlava di Windows | 4 | D | D | Quando il docente cambia la lezione, i file del piano B si rigenerano o si archiviano (da costruire) |
| #232 | Orario della settimana dopo scritto senza leggere il registro | 2 | D | D | Il file orario si scrive solo dal registro (da costruire) |
| #233 | Cruscotto 1INF del 06/11 fermo ai dati del 05/11 | 2 | D | D | verifica_lezione.py deve dare ROSSO se docs/<classe>/dati.json non e del giorno e la classe ha lezione (da costruire) |
| #234 | Report orari, presenze e Veyon del 06/11 assenti | 4 | D | D | report_ore.py va lanciato dal giro a fine di ogni ora (gia scritto nel #222, ancora non fatto) (da costruire) |
| #235 | 2INF: nessun compito del 06/11 su Classroom | 4 | D | D | Il ponte deve dire all apertura della giornata quali azioni non conosce (confronto tra versione del deployment e azioni nei comandi) (da costruire) |
| #236 | Numero del PC come menu a tendina da 1 a 24 nelle pagine dei ragazzi | 4 | A | A | controlli_pagine.py: pc_a_menu, tra i SICURI, prima del push (fatto); nei generatori del riservato da costruire |
| #237 | Teoria dell ora 5 (2INF, 09/11) su cose che i ragazzi non hanno fatto e non potevano fare | 4 | D | D | Prima di scrivere una teoria o una dispensa si chiede al docente in una riga che cosa hanno davvero fatto e su quali PC; ogni passo della teoria deve |
| #238 | Quiz «scegli 2» creati come scelta singola dal ponte vecchio (09/11) | 4 | D | D | Dopo ogni forms.crea_quiz il ponte rilegge il Modulo e scrive in esito se «limita a 1 risposta» e attivo; il generatore dei quiz da ROSSO e non conseg |
| #239 | Lezione cambiata in corsa tre volte (PC reinstallati, poi PC dell aula) il 09/11 | 4 | D | D | Ogni cambio di lezione del docente apre un «cambio piano»: si archiviano piano, cruscotto e quiz del vecchio piano e si rigenerano insieme (come #231) |
| #240 | Cruscotto 2INF con dati vecchi di circa 2 ore mostrato ai ragazzi (09/11) | 4 | D | D | Il giro del cruscotto lascia un segnale; controlla_controlli.py --fine-giornata segna ROSSO un buco superiore a 12 minuti e la pagina scrive DATI VECC |
| #241 | Quiz v2.0 non selettivo: tutti 9 o 10 su 10 (09/11) | 4 | D | D | Il generatore dei quiz calcola per ogni domanda quante delle 3-4 risposte sbagliate sono plausibili (stessa lunghezza, stesso lessico) e segnala le do |
| #242 | Messaggi in lezione troppo lunghi e senza riquadri da copiare (09/11) | 4 | D | A | (avviso dal 16/11, #342) controllo-messaggio.py (R4): in ora di lezione ROSSO se il messaggio ha piu di 10 righe, o un testo da incollare fuori da un blocco di codice. Da veri |
| #243 | Messaggio con link senza PUBBLICATO bloccato dall hook (09/11) | 2 | A | A | Nessuno nuovo: controllo-messaggio.py funziona. Resta da insegnare al generatore di messaggi a non scrivere il link prima. Voce A. |
| #244 | Cruscotto 3INF fermo ai dati del 04/11, nessun dato dei presenti il 09/11 | 4 | D | D | verifica_lezione.py e cruscotto_classe.py: ROSSO se dati.json non e del giorno e la classe ha lezione oggi (gia in #233). Da verificare perche non ha |
| #245 | Report PDF orari, presenze e Veyon del 09/11 assenti | 4 | D | D | report_ore.py va lanciato dal giro a fine di ogni ora; controlla_controlli.py --fine-giornata ROSSO se per un ora in orario manca il PDF. Da costruire |
| #246 | Ponte: due comandi in-attesa-PUBB mai chiusi e riepilogo del ponte fermo al 03/11 (09/11) | 2 | D | D | Il riepilogo del ponte si rigenera a ogni giro; a fine giornata i comandi in-attesa-PUBB si annullano o si chiudono. controlla_controlli.py --fine-gio |
| #247 | Stop hook «tutto versionato» scattato circa 25 volte il 09/11 | 2 | D | D | Commit e push a fine di ogni blocco di lavoro (R11.1); un hook di fine turno che committa da solo i file del riservato (come la bobina automatica). Da |
| #248 | Codice lungo e spiegazioni mescolati in chat (10/11) | 4 | D | D | R4 3ter senza controllo: da costruire, ma da riallineare con #253 |
| #249 | Account PIAMARTA e testi in riquadro non rispettati (10/11) | 4 | D | D | Nessun controllo automatico che verifichi 3bis nei messaggi |
| #250 | Troppa verbosita, spiegazioni non capite, «ricomincia da zero» (10/11) | 4 | D | A | (avviso dal 16/11, #342) Il limite di lunghezza in ora di lezione (R4.2) non e controllato da uno strumento |
| #251 | PPP con codice visibile nelle finestre (10/11) | 4 | D | D | Nessun controllo sui PPP |
| #252 | Link al sito dato prima di PUBBLICATO con deploy fallito (10/11) | 4 | D | D | Il controllo (e) di #79 esiste ma non ha impedito il caso |
| #253 | Contraddizione R4 3ter e richiesta finale del docente (10/11) | 4 | D | D | Decisione del docente |
| #255 | Un script da incollare per ogni lavoro, nessun sistema (10/11) | 4 | D | D | controllo automatico: mancante |
| #256 | Dati richiesti senza i file da scaricare (10/11) | 4 | D | D | controllo automatico: mancante |
| #257 | Script e istruzioni con errori, non provati su Google (10/11) | 4 | D | D | controllo automatico: mancante |
| #258 | Piantina non versionata (PDF ignorato da git) (10/11) | 4 | D | D | controllo automatico: mancante |
| #259 | Piantina fatta per numero PC e non per i banchi reali (10/11) | 4 | D | D | controllo automatico: mancante |
| #260 | Valutazione con criterio sbagliato (10/11) | 4 | D | D | controllo automatico: mancante |
| #261 | Richieste interpretate male, date e nomi file ambigui (10/11) | 4 | D | D | controllo automatico: mancante |
| #262 | Compito 4TI troppo difficile e rifatto (10/11) | 4 | D | D | controllo automatico: mancante |
| #263 | Schede su carta per tutti senza stampante (10/11) | 4 | D | A | audit notturno `controlli_pagine.carta_e_penna` (non blocca il push: 13 pagine vecchie lo violano). RIMESSO 23/11/2026 (era: controllo automatico: mancante) |
| #264 | Cruscotto dato come file e non come URL (10/11) | 4 | D | D | controllo automatico: mancante |
| #265 | Sistema nuovo non spiegato e nome non visibile (10/11) | 4 | D | D | controllo automatico: mancante |
| #266 | Passo non riscritto, rimando a messaggi precedenti (10/11) | 4 | D | D | controllo automatico: mancante |
| #268 | Passo senza la finestra Chrome dell'account (11/11) | 4 | D | D | controllo automatico: mancante (idea: in controllo-messaggio.py ogni riga «Passo N» deve contenere PIAMARTA o PERSONALE) |
| #269 | Soglia «7 su 10» presunta nel post e nei quiz (11/11) | 7 | D | D | controllo automatico: mancante (idea: cercare nei testi per i ragazzi numeri e soglie non presenti in un file verificato) |
| #270 | PPP ignorato: consegna subito e file due volte (11/11) | 3 | D | D | controllo automatico: mancante (idea: controllo-messaggio.py segnala un messaggio lungo dopo una richiesta che comincia con PPP) |
| #271 | Richiesta interpretata invece di seguire la lettera (11/11) | 7 | D | D | controllo automatico: mancante |
| #272 | Controlli e passi chiesti al docente in lezione (11/11) | 4 | D | D | controllo automatico: mancante (idea: controllo-messaggio.py segnala in ora di lezione messaggi con più di un passo o richieste di screenshot di controllo) |
| #273 | Stesso file rimandato con lo stesso nome (11/11) | 6 | D | D | controllo automatico: mancante |
| #274 | Lingue della 1INF dimenticate nei quiz e nel post (11/11) | 1 | D | A | `strumenti/controlla_lingue_quiz.py` (R6): per ogni quiz con id `1inf` in `fabbrica/indice.json` controlla arabo e cinese, «MANCA arabo e cinese» e uscita 1; si lancia con `python3 -I strumenti/controlla_lingue_quiz.py` prima di dire che un quiz 1INF è pronto. Voce #274 in `REGISTRO-ERRORI-CLAUDE.md` |
| #267 | Link senza account e non in casella copiabile (11/11) | 4 | D | D | controllo automatico: mancante (CLAUDE.md v2.8 R4 3quater, LINK-UTILI.md) |
| #275 | Strumento garantito senza prova, chiedeva l'amministratore (11/11) | 7 | D | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: `STRUMENTI-PC-AULA-VERIFICATI-v1.0.md` (riservato); controllo automatico: mancante) |
| #276 | Argomento di un'ora copiato da un documento vecchio (11/11) | 7 | D | D | `generatori/diario_dati.py` legge FIRME-REGISTRO; controllo automatico per ARGOMENTI-SVOLTI: parziale, dal 13/11/2026 `strumenti/controlla_controlli.py` (fine giornata) verifica che ogni lezione del giorno abbia la sua riga in ARGOMENTI-SVOLTI-2026-27.md (R5.3); non verifica che l'argomento sia quello giusto |
| #277 | Chat 3INF presentata senza provare che chatta (11/11) | 9 | D | A | BLOCCO `controlli_ripristinati.affermazione_senza_prova` («a posto», «risolto», «funziona», «garantito», «c'è sul sito» senza prova). RIMESSO 23/11/2026 (era: CHECKLIST-LEZIONE (prova con due istanze); controllo automatico: mancante) |
| #278 | Quiz Sicurezza non sulle slide ufficiali (11/11) | 9 | D | D | FRAMEWORK-QUIZ cap. 10; controllo automatico: mancante |
| #279 | Scheda Situazione 2INF vuota (11/11) | 8 | D | A | motore Fabbrica v2.15 e `test_situazione_v2_15.js` (riservato) |
| #280 | Pannello e schede senza «a che serve» (11/11) | 4 | D | A | audit notturno `controlli_pagine.senza_a_che_serve`. RIMESSO 23/11/2026 (era: idea: `controlli_pagine.py`; FABBRICA-MANUALE v2.6 da fare) |
| #281 | Allievi nominati senza cognome (11/11) | 7 | D | A | avviso `controllo_nomi.avviso_nome_solo` (nome di battesimo da solo). RIMESSO 23/11/2026 (era: avviso non bloccante in `controllo-messaggio.py` (v. #329, 13/11): cognome + nome di battesimo; la regola ora è «solo il COGNOME») |
| #329 | Nome di battesimo accanto al cognome, COGNOME Nome (13/11) | 7 | D | A | `controllo_nomi.avviso_nome_battesimo` richiamato da `controllo-messaggio.py`, avviso non bloccante; prove in `prove/prova_messaggio.py` (10 casi) |
| #282 | Formato del pacchetto per il post rifatto cinque volte (11/11) | 4 | D | A | hook controllo-messaggio.py (ff) R-D, R-F; GUIDA-MESSAGGI 03sexies |
| #283 | Controllo di fine giornata cieco, VERDE «nessuna lezione» (11/11) | 7 | D | D | `controlla_controlli.py --fine-giornata` da collegare a FIRME e `fabbrica/indice.json` |
| #284 | Incoerenze trovate e non corrette nei file (11/11) | 7 | D | D | controllo automatico: mancante |
| #285 | PDF dato solo come nome, senza la scheda da scaricare (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-A: ogni SendUserFile di documento ha testo con 🟦 e 📄 prima e testo con 🟦 dopo |
| #286 | Ordine dell'ora ignorato: pacchetto prima della dispensa docente (12/11) | 1 | D | D | controllo automatico: mancante (il controllo ff non conosce l'ordine dell'ora) |
| #287 | Testo del pacchetto prima della scheda PDF non visibile (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-A, R-D |
| #288 | Scheda PDF fuori dalla cornice rossa (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-A, R-D (ultima riga rossa) |
| #289 | Pacchetto Classroom: formati sbagliati prima di quello giusto (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-D, R-E |
| #291 | Messaggi per il docente senza cornice verde (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-F |
| #293 | Kit consegnato in un turno sporco (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-C |
| #309 | Documento mandato senza i quadratini blu (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-A |
| #311 | Due kit con due PDF nella stessa risposta (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-B |
| #312 | Controllo automatico del formato kit e documenti aggiunto (12/11) | 1 | A | A | hook controllo-messaggio.py (ff), prove `prova_formato_kit.py` (55 casi); chiude la famiglia #282, #285-#289, #293, #309, #311 |
| #292 | Quiz in inglese su PC con Windows in italiano (12/11) | 1 | D | A | `strumenti/controlla_lingue_quiz.py` v1.1 (sigle inglesi di Windows nei quiz 2INF). RIMESSO 23/11/2026 (era: `controlla_lingue_quiz.py` da estendere alle sigle inglesi di Windows nei quiz 2INF; controllo automatico: mancante) |
| #294 | Chiesto di cercare sullo schermo cose che non c'erano (12/11) | 2 | D | D | regola: un passo si scrive solo se visto in uno screenshot reale; controllo automatico: mancante |
| #295 | Versione sbagliata del PDF nei post e nei kit (12/11) | 2 | D | D | da fare: controllo che il PDF del kit sia l'ultima versione del suo nome |
| #296 | Cruscotto che dipendeva da gesti del docente (12/11) | 6 | D | D | file dati aggiornato da me (v2.5); giro automatico ogni 2 minuti: mancante (vedi #323) |
| #297 | Quiz rigenerato quattro volte mentre i ragazzi lo facevano (12/11) | 1 | D | D | Fabbrica v2.20 (campo `versioni`); controllo automatico: mancante |
| #298 | Numeri dei PC del foglio diversi da quelli di Veyon (12/11) | 2 | D | D | decide il docente quale fonte vale; controllo automatico: mancante |
| #299 | Ora del dato ingannevole nella scheda Situazione (12/11) | 2 | D | D | da fare nel motore («Letto alle» e celle di punteggio in formato testo) |
| #300 | Richieste del docente capite male, tre volte (12/11) | 1 | D | D | controllo automatico: mancante |
| #301 | Posti dei PC copiati da un altro giorno e dati per veri (12/11) | 2 | D | D | mappa del giorno nel riservato; controllo automatico: mancante |
| #302 | Pagina del cruscotto con «letto alle 08:27» sotto i quiz (12/11) | 2 | D | D | pagina v2.6 corretta; motore da correggere (come #299) |
| #303 | «Presenti 20» mentre il registro ne dava 19 (12/11) | 2 | D | D | pagina v2.6; dove tenere le assenze senza nomi nel pubblico: da decidere |
| #304 | Allievo senza utente GitHub salta in silenzio da «Git 2INF» (12/11) | 6 | D | D | da fare nel motore (riga «manca l'utente»); controllo automatico: mancante |
| #305 | Elenco email del quiz con due orari e contenuto più vecchio dell'ora scritta (12/11) | 2 | D | D | regola R7 (ora dell'incolla chiesta, non stimata); controllo automatico: mancante |
| #306 | Due formule del «voto proposto» nello stesso documento (12/11) | 2 | D | D | rimando in documento v1.9; controllo automatico: mancante (vedi #322) |
| #307 | Cognome intero nella scheda pubblica 4TI (12/11) | 1 | D | A | controllo della privacy a ogni export (`strumenti/aggiorna_cruscotto_dati.py`); regola «Nome I.» del motore da correggere (correzione v2.21 preparata, non deployata) |
| #308 | Riscrittura della storia git da un clone shallow (12/11) | 1 | D | D | regola nel registro; script `strumenti/riscrivi_storia.sh` da scrivere |
| #310 | md2pdf non incorporava le immagini (12/11) | 6 | D | A | `strumenti/md2pdf.py` corretto (immagini incorporate) |
| #313 | Controllo del post ROSSO perché leggeva il ponte (12/11) | 2 | D | A | `verifica_lezione.py` v2.0: Fabbrica come fonte, senza dato fresco GIALLO «NON PROVATO», mai ROSSO (provato 12/11 14:09) |
| #314 | «Non ha consegnato» con un dato di 6 minuti prima (12/11) | 2 | D | A | hook controllo-messaggio.py (hh), prove `prova_messaggio.py` 46 casi |
| #315 | Domande aperte non contate: «10/14» letto come risultato (12/11) | 2 | D | D | `fabbrica/correzioni/motore-v2.21.js` preparato e provato, NON deployato; fino ad allora «solo chiuse» |
| #316 | Domanda aperta su un dato di un passo «facoltativo» (12/11) | 1 | D | D | `strumenti/controlla_quiz_dispensa.py` (CHECKLIST 06.16): da lanciare a mano, non collegato ai passi notturni |
| #317 | Script voti DIDAweb dato due volte senza aver visto la pagina (12/11) | 2 | D | D | `generatori/didaweb_diagnostico_v1.0.js` (sola lettura, non provato); controllo automatico: mancante |
| #318 | Kit del quiz in un turno con altri strumenti, testo non visibile (12/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-B, R-C: ricaduta dopo il controllo, efficacia non provata (vede i blocchi, non come l'app li mostra) |
| #319 | Cognome in un file di fabbrica/ pushato: il controllo guardava solo docs/ (12/11) | 1 | D | A | hook limite-comandi.py: al push controlla il contenuto di tutti i file cambiati; prove `prova_limite.py` 42 casi |
| #320 | Script voti scritto per Classroom invece che per DIDAweb (12/11) | 1 | D | D | regola: i voti vanno nel registro DIDAweb; nel dubbio una domanda sola (R7.6); controllo automatico: mancante |
| #321 | Parole «pubblicato»/«online» fermate quattro volte (12/11) | 2 | A | A | hook controllo-messaggio.py (già attivo); da fare: distinguere Classroom e sito per ridurre i falsi allarmi |
| #322 | Formula del voto presunta (40 + 30 × punti / 14) (12/11) | 2 | D | D | regola R7.6; idea: file dei voti con «formula da confermare» in prima riga; controllo automatico: mancante |
| #323 | Cruscotto 1INF nell'ora 6 senza giro automatico, senza Veyon, senza «Serve te» (12/11) | 4 | D | D | giro ogni 2 minuti dalla Fabbrica e campo Veyon: da costruire |
| #324 | Piani del giorno e report orari assenti, controlli di notte e fine giornata ciechi (12/11) | 4 | D | A | `strumenti/controlla_controlli.py`: orario del giorno anche da FIRME-REGISTRO e PROSSIME-LEZIONI (`_lezioni_da_testi`), prove `prova_controlla_controlli.py` 29/29; piani e report orari da produrre (decisione sul sistema) |
| #325 | Nome intero di un allievo in un file di prova, controllo privacy VERDE (12/11) | 1 | D | A | `controlla_controlli.py` controlla_privacy: cerca anche il nome intero «COGNOME NOME» in ogni file, codice compreso (provato rosso/verde) |
| #328 | Dispense poco chiare per ragazzi delle medie, ripetuto (13/11) | 5 | D | A | `strumenti/controlla_leggibilita.py` (CHECKLIST 06.17): da lanciare a mano e dagli agenti prima di consegnare una dispensa; NON è un hook bloccante; prove in `strumenti/prova_controlla_leggibilita.py` (21 casi) |
| #326 | Presenza presunta riservata, senza chiedere (13/11) | 7 | D | A | `strumenti/aggiorna_presenze_dati.py` (solo «Nome I.», controllo privacy bloccante); regola R7.6 NON PRESUMERE; CLAUDE.md v2.10 |
| #327 | Cruscotto 1INF non coerente tra le viste (13/11) | 8 | D | B | `strumenti/aggiorna_oggi_dati.py` incrocia Situazione e Ris; controllo a mano a ogni refresh (non ancora automatico) |
| #330 | Dispensa PDF non scaricabile dal nome del file (13/11) | 2 | D | A | `strumenti/controlla_pdf_ragazzi.py` (nome sicuro, PDF vero, copia su origin/main); download vero non provabile da qui |
| #331 | Dispensa fitta e con note tecniche nel PDF dei ragazzi (13/11) | 9 | D | A | `strumenti/controlla_pdf_ragazzi.py` (note tecniche = ROSSO, oltre 150 parole per pagina = avviso, soglia da confermare); CHECKLIST 06.18 |
| #332 | «Chi manca» con dato vecchio e assenti non incrociati (13/11) | 7 | D | D | famiglia di #314 (hook hh) e #327; incrocio automatico presenze e mancanti da costruire |
| #333 | Motore non provato con servizi veri attivato: primo giro non completato (13/11) | 2 | D | D | regola: giro vero completo su copia, tempo massimo per giro e rollback pronto prima di attivare; dopo l'attivazione lettura di «Stato» a 2 e 6 minuti (v. #152, #153) |
| #334 | Orario di lunedì presunto e domanda che contraddice il docente (13/11) | 7 | D | D | R7.6; CHECKLIST 06.13 (orario solo da DIDAweb o dallo screenshot del docente); confronto automatico da costruire |
| #335 | Correzioni del motore pubblicate su motore.js prima del «via» (13/11) | 1 | D | D | regola: correzioni non autorizzate solo in `fabbrica/correzioni/`; avviso in `limite-comandi.py` per un commit su `fabbrica/motore.js` da costruire |
| #336 | Kit in turno con strumenti prima: titolo e testo non mostrati (16/11) | 1 | D | A | hook controllo-messaggio.py (ff) R-C, kit in turno pulito: segnala solo dopo l'invio; non impedisce (vedi #349) |
| #337 | Pagine riservate cifrate con una chiave che il docente non conosce (16/11) | 1 | D | D | passphrase del docente in `config/PASSPHRASE-DOCENTE.txt`, `passphrase_docente.py`; controllo nel generatore da aggiungere |
| #338 | URL dei siti degli allievi dedotti invece che letti (16/11) | 2 | D | A | `url_siti_3inf.py` distingue «dal Documento» da «dedotto» e non pubblica i dedotti |
| #339 | Codici di recupero GitHub non conservati, risposta «non esistono» (16/11) | 2 | D | B | `strumenti/dove.py` e indice rapido del riservato; salvataggio cifrato dei file con segreti (D) |
| #340 | Ricerca di un file noto durata ore, indice mancante (16/11) | 6 | D | A | `strumenti/dove.py`, `aggiorna_indice_rapido.py`, `prova_dove.py` |
| #341 | Audit cruscotti: dati di ore diverse, screenshot prima dell'export, tabella illeggibile a 390 px (16/11) | 2 | D | D | cruscotti v0.6.1; scansione dei repository dello script e controllo «repository cambiato dopo la verifica» da fare |
| #342 | Messaggi ancora troppo lunghi, «troppa roba inutile» (16/11; ripete #242, #250) | 5 | D | A | `.claude/hooks/controllo-messaggio.py` controllo (ii): avviso non bloccante oltre 10 righe o 160 parole fuori dai riquadri; prove `prova_messaggio.py` 62/62. #242 e #250 passano da D ad A (avviso) |
| #343 | Orario di firma letto male dallo screenshot, 08:15 invece di 09:41 (16/11) | 2 | D | A | `strumenti/controlla_controlli.py` `firme_sospette` nel controllo di fine giornata (firma oltre 60 minuti prima dell'ora = ROSSO); prove 41/41 |
| #344 | Password del docente di nuovo in chiaro nella bobina: la sessione usa la copia pubblica dell'hook (16/11) | 2 | D | B | maschera aggiunta a `bobina-automatica.py` (copia pubblica e del riservato, percorso assoluto); un'unica copia dell'hook e controllo di fine giornata sulla password nelle bobine da fare (D) |
| #345 | Giri del cruscotto fermi per ore, piani del giorno assenti, orario scritto a lezione iniziata (16/11; ripete #169, #324, #334) | 4 | D | B | `controlla_controlli.py --fine-giornata` segnala giri fermi e piani assenti dopo; giro creato insieme alla pagina da costruire (D) |
| #346 | Report PDF orari assenti per tutta la giornata (16/11; sesta volta) | 4 | D | B | `controlla_controlli.py --fine-giornata` ROSSO se manca il PDF; sei PDF generati a fine giornata con `generatori/report_ore.py`; lancio a fine ora da costruire (D) |
| #347 | Istruzioni per i ragazzi lunghe o non chiare, informazioni mancanti (16/11) | 5 | D | B | `controlla_leggibilita.py` e `controlla_coerenza_materiale.py` (a mano, non bloccanti); lista delle domande dei ragazzi da costruire (D) |
| #348 | Verifica della lezione mai VERDE, giro della Fabbrica oltre il limite, export ogni ora (16/11) | 2 | D | D | export automatico in ora di lezione e avviso sul «Giro: durata» da costruire |
| #349 | Formato del messaggio sbagliato ancora dopo #336 (16/11) | 1 | D | A | hook controllo-messaggio.py (ff), solo dopo l'invio; prova di consegna riuscita prima di scrivere «sistemato» |
| #350 | Modalità già decise cambiate (voti DIDAweb), codice non in fondo (17/11) | 2 | A | A | `promemoria-errori.py` (rilettura del mattino) e `controllo-messaggio.py` (jj) «codice non in fondo» |
| #351 | Prova archiviata in più ZIP, cartella «Regge» incompleta (17/11) | 1 | A | A | `strumenti/archivia_prova.py` (riservato): un solo ZIP + controllo di completezza (esce 1 se manca qualcosa); D: aggancio alla parola «archiviato» |
| #352 | Kit senza «che cosa si consegna e quanto tempo», formato e colori da richiedere (17/11; ripete #347, #349) | 5 | D | D | da costruire: righe «Consegna:» e «Tempo:» controllate prima dell'invio |
| #353 | Script voti per il lotto sbagliato, senza chiedere (17/11) | 1 | D | D | R7.6; da costruire: domanda «quale classe e quale prova?» se ci sono più lotti |
| #354 | Archivio su Drive promesso senza provare l'accesso (17/11) | 1 | D | D | da costruire: lettura di prova della cartella prima di promettere; `archivia_prova.py` per lo ZIP a mano |
| #355 | Fine giornata 17/11 ROSSO: piani, cruscotto fermo, report orari, 4TI (ripete #345, #346) | 4 | D | B | `controlla_controlli.py --fine-giornata`; report 2INF generati con `report_ore.py`; da costruire: controllo a metà giornata |
| #357 | Budget dei preventivi 1INF cambiati per una frase ambigua, valori diversi nei file (18/11) | 1 | D | A | `strumenti/controlla_budget_1inf.py` agganciato a `controlla_controlli.py` (fonte unica `config/budget-1inf-1811.json`, dal 18/11 ore 09:5x v2.0 con 500/600/1000 per decisione del docente: le versioni 450/600/900 sono «da non usare oggi» e non si guardano); la domanda su una frase ambigua resta R7.6 |
| #358 | Repo `mio-sito` attribuito a un allievo senza prova (18/11) | 1 | D | D | R7.6; da creare: `strumenti/autore_repo.py` (git log degli autori); finché non esiste: «autore non provato» |
| #359 | Passo «Assegna» invece di «Salva» (18/11) | 1 | D | D | da creare: checklist dei bottoni di Classroom per stato in `CHECKLIST-LEZIONE.md`; guardare lo screenshot prima del passo |
| #360 | Modello Word e Documento Google: opzione inesistente, Drive sbagliato (18/11) | 1 | D | D | da creare: prova del menu «Crea una copia per ogni studente» e Doc nel Drive PIAMARTA prima del via |
| #361 | Riquadri non visibili, 6 messaggi per incollare un testo (18/11) | 1 | D | D | da creare: controllo in `controllo-messaggio.py` per più di un riquadro; testo corto o in un solo riquadro |
| #362 | Scheda trilingue con caselle ripetute 3 volte (18/11) | 1 | D | A | audit notturno `controlli_pagine.campi_ripetuti`. RIMESSO 23/11/2026 (era: da creare: controllo in `controlli_pagine.py` e `controlla_pdf_ragazzi.py` (sottotitolo uguale all'italiano)) |
| #363 | Check Lazarus da console invece che con l'interfaccia decisa (18/11) | 1 | D | D | da creare: elenco delle decisioni del docente per giornata, riletto prima di generare |
| #364 | «3 test a testa» incoerente con modello e istruzioni (18/11) | 1 | D | D | stesso elenco del #363 più controllo di coerenza dei numeri |
| #365 | Guide di trasferimento repository senza il passo di rinomina (18/11) | 1 | D | D | da creare: passo fisso di rinomina prima del trasferimento (sospeso con la 3INF fino a febbraio) |
| #366 | Verifica siti con indirizzi dedotti, non aperti (18/11) | 1 | D | D | da creare: «non provato» per ogni indirizzo non aperto, bottone dal browser del docente |
| #367 | Passi dati senza leggere le informazioni già disponibili (18/11) | 1 | D | B | `report/INFO-PIU-USATE-v1.1.md` (riservato) letto dall'hook `promemoria-errori.py` v1.3 al primo messaggio del giorno |
| #368 | Registro nel formato sbagliato: complessivo invece che per materia (18/11) | 1 | D | B | registro per materia v1.1 (riservato, generatore); da creare: domanda con lo schema prima di costruire un registro |
| #369 | Richieste di permesso moltiplicate dagli agenti (18/11) | 1 | D | D | `PERMESSI-AGENTI-v1.0.md` (30 regole di sola lettura, modalità «Auto» da confermare); da creare: una sola richiesta cumulativa |
| #370 | Priorità sbagliate e domande fuori dalle 4 priorità (18/11) | 1 | D | D | da creare: `stato/coda-priorita.json` riscritto a ogni PRI; domande solo sulle priorità in corso |
| #371 | Allegato A frainteso: blocco e materia presunti (18/11) | 1 | D | D | R5.2 e `NOTE-DA-DISCUTERE.md`; da creare: una domanda con le alternative prima di proporre |
| #372 | Cose già fatte non cercate (piantine) e piano dell'ora presunto (18/11) | 1 | D | B | `INFO-PIU-USATE-v1.1.md` sezione piantine; da creare: ricerca per parola chiave prima di dire «non c'è» |
| #373 | Messaggio con tre file non capito (18/11) | 1 | D | A | BLOCCO `controllo-messaggio.controlli_con_trascrizione` (più file senza «a che serve» per ognuno, R4). RIMESSO 23/11/2026 (era: `controllo-messaggio.py` formato kit; da aggiungere: frase «a che cosa serve» e SendUserFile per ogni file) |
| #374 | Fine giornata 18/11 ROSSO: report orari, cruscotto, verifiche (ripete #355) | 1 | D | B | `controlla_controlli.py --fine-giornata`; 6 report minimi generati da `report_ore.py`; da costruire: controllo a metà giornata e giro cruscotti automatico |
| #375 | «Non posso creare il Moduli» invece della Fabbrica (19/11) | 1 | D | B | `report/INFO-PIU-USATE-v1.2.md` sezione 9; `strumenti/crea_quiz_fabbrica.py`; da costruire: avviso «non posso» senza lettura di `fabbrica/LEGGIMI.md` |
| #376 | Kit 2INF Sicurezza a lezione avviata, recupero tolto senza dirlo (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.3.md` sezione 10; da costruire: segnalazione in prima riga a ora iniziata senza kit |
| #377 | La bobina non era la memoria completa (19/11) | 1 | D | A | `bobina-automatica.py` v2.0; `strumenti/ingresso_dati.py` |
| #378 | Registro Sicurezza 2INF mandato senza confronto col DIDAweb (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.8.md` sezione 16.1; da costruire: file di confronto del giorno per ogni xlsx di materia |
| #379 | PC attribuiti dal testo incollato (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.8.md` sezione 16.2; da costruire: lettura automatica dell'esportazione delle mail |
| #380 | Troppe domande quando il docente chiedeva autonomia (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.8.md` sezione 16.3; da costruire: avviso in `controllo-messaggio.py` per più di 3 domande numerate |
| #381 | Richieste ripetute per la stessa cosa (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.8.md` sezione 16.4; `COSE-DA-FARE-20-11.md`; da costruire: controllo della stessa richiesta ripetuta |
| #382 | Materiale importante finito in un'altra chat (19/11) | 1 | D | B | `INFO-PIU-USATE-v1.8.md` sezione 16.5; bobina v2.0 con indice degli allegati |
| #383 | Lentezza e output spesso sbagliato (19/11) | 1 | D | D | confronto prima dell'invio (#378, #379); da provare: routine 06:50 del 20/11 |
| #384 | Esercizio 1INF ora 4: scheda senza materiale (20/11) | 5 | A | A | `strumenti/controlla_kit.py` v1.2: «KIT INCOMPLETO: scheda senza esempio/materiale» |
| #385 | PDF ragazzi 1INF di 28 pagine (20/11) | 5 | A | A | `strumenti/controlla_kit.py` v1.3: massimo 10 pagine per la 1INF, frasi corte |
| #386 | Formato pacchetto PUBB e kit non mantenuto (20/11) | 1 | D | A | (kk) di `controllo-messaggio.py`: «PUBB n» senza pacchetto rosso/blu con TITOLO e OGGETTO in riquadri; `strumenti/controlli_consegna.py`; `prova_consegna.py` |
| #387 | Testi dei post incoerenti con gli allegati e con la data (20/11) | 2 | D | A | `controlla_kit.py` v1.4 (riservato) + `controlli_consegna.py`: «KIT INCOERENTE» per «ieri/domani», «_», «???», ora/data del titolo, Documento senza modello, carte senza intervallo, quiz; `prova_controlla_kit.py` |
| #388 | Formato predefinito PDF non applicato (20/11) | 1 | D | A | (ll) di `controllo-messaggio.py`: file xlsx/docx/csv/md senza PDF e senza formato chiesto; `promemoria-errori.py` v1.16 resta |
| #389 | Cruscotto senza dati di oggi e non in tempo reale (20/11) | 6 | D | A | (mm) di `controllo-messaggio.py` e `controlla_controlli.py` punto 10 (`controlla_cruscotto_oggi`); «giri fermi» (A); cruscotto live v1.2 da provare |

## 05 Voci scoperte (D): perché e che cosa servirebbe

1. 01/10-4: procedura rara di fine compito: servirebbe una lista di controllo dentro il generatore di chiusura.
2. 01/10-5: comprensione: non si controlla con parole o file.
3. 01/10-7: contenuto dei libri: servirebbe un controllo nel generatore di chiusura.
4. 01/10-12: giudizio didattico: servirebbe la foto della lavagna nel diario.
5. 01/10-14: giudizio visivo: servirebbe generare le due cose dalla stessa immagine.
6. 02/10-2: non si riconosce in automatico quale passo apre un sito.
7. 02/10-3: servirebbe un controllo del piano B (gen_pianob.py) sul Documento allegato.
8. 02/10-4: giudizio didattico.
9. 02/10-6: bloccare i push in lezione fermerebbe anche le correzioni urgenti.
10. 02/10-7: giudizio didattico.
11. 02/10-8: servirebbe un controllo automatico dei PDF (titoli orfani, tabelle tagliate).
12. 02/10-10: la memoria del browser del docente non si vede da qui.
13. 02/10-12: consiglio dato in chat: nessuna parola sicura da cercare.
14. 02/10-14: servirebbe il divieto di sovrascrivere chiavi nei generatori.
15. 02/10-15: promesso e mai costruito: servirebbe nel generatore delle dispense.
16. #7: scelta di progetto della lezione.
17. #8: la pagina per PC non si distingue in automatico dalla pagina per tutti.
18. #14: scelta di metodo; la rigenerazione è coperta in parte da passi-notturni.md 02.9.
19. #15: i nomi di file nelle pagine sono spesso leciti: troppi falsi allarmi.
20. #17: l'invio dei file in chat non passa da un hook.
21. #18: servirebbe un controllo nei correttori.
22. #19: servirebbe un elenco dei guasti letto dall'audit.
23. #22: servirebbe un controllo nel generatore delle griglie.
24. #25: servirebbe la prova di apertura dentro il generatore dello zip.
25. #26: servirebbe un controllo nei generatori dei libri.
26. #27: l'invio dei file in chat non passa da un hook.
27. #28: giudizio di progetto.
28. #30: come #22.
29. #33: non si sa in automatico se i ragazzi hanno un materiale.
30. #39: lezione in corsa; solo «modifiche verificate» è coperta da hook controllo-messaggio.py (c).
31. #40: servirebbe un controllo sulle pagine del docente (cifrate).
32. #46: non si sa in automatico quale testo il docente dovrà scrivere.
33. #47: giudizio di scrittura.
34. #54: intenzione del docente: non controllabile.
35. #59: non si riconosce in automatico una richiesta dentro un PPP.
36. #64: chat con i ragazzi su GitHub: non passa dagli hook.
37. #65: come #64.
38. #66: giudizio didattico.
39. #67: giudizio in lezione.
40. #69: manca l'elenco della 4TI nel config: aggiunto quello, lo coprirebbe hook limite-comandi.py.
41. #70: github.io non è raggiungibile da qui (proxy).
42. #72: giudizio di progetto.
43. #73: in lezione: servirebbe un giro che segnali le schermate non ancora nel monitor.
44. #74: giudizio di progetto.
45. #91: servirebbe un controllo dei titoli del registro sul .docx dell'Allegato A.
46. #92: conteggio dei presenti fatto a mano dallo screenshot.
47. #95: massimo del quiz: servirebbe nel calcolo dei voti; la parte «non risulta» è coperta da hook controllo-messaggio.py (r).
48. #106: il nome giusto non è noto all'hook.
49. #108: servirebbe un controllo nei generatori dei cruscotti.
50. #109: lettura delle schermate: giudizio.
51. #111: si può aggiungere a report_ore.py un confronto delle immagini.
52. #116: servirebbe una prova con testo finto nei controlli della lezione.
53. #121: servirebbe che chi scrive la coda chieda prima classroom.compiti al ponte.
54. #122: solo il docente sa che cosa ha detto; la campanella è controllata da audit_regole.py (passi notturni 01.1) 04.

## 06 Quando si registra un errore nuovo

1. Si aggiunge la riga in questa tabella, con schema e copertura.
2. Se la regola si può riconoscere da parole nel messaggio, da un comando o da un file, si aggiunge un controllo (hook o audit) con le sue prove, poi la riga diventa A o B.
3. Se no, la riga resta D con il perché; il conteggio della sezione 01 si aggiorna.

## 07 Banco di prova degli errori (23/11/2026, v1.32, sezione nuova)

Ordine del docente, 23/11/2026: ogni errore passato diventa un test automatico che scatta se si ripresenta. Questa mappa dice che cosa un controllo DOVREBBE fare; il banco dice che cosa fa DAVVERO.

1. Dove sta: `strumenti/banco_errori_v1.1.py` (il lanciatore; la v1.0 resta, ma lascia scritti alla lettera i segnaposto {{ORA-1}}), `tests/errori/indice.json` (una riga per voce: categoria dell'audit, schema, motivo se non verificabile), `tests/errori/casi/*.json` (un caso per errore verificabile: input sbagliato, input giusto, controllo che deve scattare), `tests/errori/specifiche-v1.0.json` (il controllo più piccolo che coprirebbe i NON COPERTI), `tests/errori/baseline-coperti.json` (gli errori coperti all'ultimo giro). Rapporto: `report/2026-11-23/BANCO-ERRORI-v1.0.md` del riservato.
2. Come si lancia: `python3 /home/user/corso-informatica/strumenti/banco_errori_v1.1.py -v`. Con `--regressioni` esce 1 se un errore prima coperto non scatta più (un controllo tolto o rotto) o se un controllo scatta sul caso giusto. Va lanciato prima di modificare un hook o uno strumento dei controlli.
3. Stati: COPERTO (il controllo scatta e sul caso giusto non scatta), NON COPERTO (nessun controllo lo fermerebbe: è un buco, mai «atteso»), CASO DA SCRIVERE (verificabile, caso non ancora scritto), NON VERIFICABILE A MACCHINA (con il motivo scritto), ERRORE DEL BANCO (il caso non gira: non conta come coperto).
4. Primo giro, 23/11/2026: 414 voci; 119 COPERTE, 96 NON COPERTE, 13 casi da scrivere, 186 non verificabili a macchina, 0 errori del banco. Il banco e le colonne «Prima» e «Ora» di questa mappa dicono cose diverse: 43 voci che la sezione 04 dà con copertura «A» non scattano più al banco (per lo più controlli dell'hook tolti il 04/11/2026); la tabella della sezione 04 non è stata riscritta: vale quella del banco, che si può rieseguire.
5. Regola per la sezione 06: quando si registra un errore nuovo si scrive PRIMA il caso in `tests/errori/casi/` (e la riga in `indice.json`); nasce NON COPERTO e il controllo che lo ferma lo porta a COPERTO. Un errore senza caso scritto è un errore senza prova.

## 08 Controlli rimessi il 23/11/2026 (v1.33, sezione nuova)

Ordine del docente, 23/11/2026: «se ci sono errori che tu hai tolto dagli avvertimenti rimettili; se invece li abbiamo risolti va bene così». Il banco (sezione 07) aveva trovato 43 errori dati con copertura «A» il cui controllo non scattava più, e 96 NON COPERTI. Il codice storico dei controlli tolti il 04/11 non è più nella storia di git (il repository comincia il 18/11/2026): i controlli sono rifatti dalla descrizione di `.claude/hooks/LEGGIMI-controlli.md` (capitolo 05.2) e dai casi del banco, sulle regole R1-R11 di oggi. Regola di scelta: BLOCCO per le regole bloccanti di CLAUDE.md (R4 formato, R5 firma, R7 prova prima delle parole, R9 pagine prima del push), AVVISO (non blocca) per il resto.

1. **Rimessi: 47** (39 dei 43 e 8 dei primi 10 NON COPERTI). Dei 43: #3, #5, #16, #21, #23, #31, #51, #53, #55, #56, #63, #83, #87, #88, #90, #96, #98, #100, #113, #115, #117, #127, #130, #135, #139, #140, #143, #151, #152, #153, #154, #157, #158, #165, #166, #167, #281, #373, 01/10-6. Dei primi 10 NON COPERTI: #362, #178, #292, #280, #263, #227, #211, #177. In più 5 errori NON COPERTI sono ora coperti dagli stessi controlli: #39, #104, #173, #275, #277. Codice: `.claude/hooks/controlli_ripristinati.py` (testo del messaggio), `controllo-messaggio.py` (firma, trascrizione, nomi), `controllo_nomi.py` (nome solo), `controlli_pagine.py` (pagine), `strumenti/controlla_lingue_quiz.py` v1.1.
2. **Risolti altrove: 4** (copertura corretta da A a C nella tabella): #11, #36, #52 (R5.1 di CLAUDE.md v2.0: «FIRMA ✓» in verde = firmata; la vecchia regola «la firma non si deduce dal bottone» è abrogata) e 02/10-9 (i PDF dei ragazzi vanno ora come Allegato del post, kit del 20/11/2026).
3. **Ancora da fare: 2 dei primi 10** (#352 e #198: servono `controlla_kit.py` e `controlli_consegna.py`, file di altri agenti; non toccati; la parte #177 sul post già creato sta nello stesso file). Resto del banco, non in questo incarico: 44 NON COPERTI e 13 CASI DA SCRIVERE. NON COPERTI: #11, #186, #188, #190, #198, #204, #215, #220, #223, #225, #228, #240, #249, #251, #254, #264, #266, #267, #268, #269, #27, #270, #273, #295, #308, #322, #334, #335, #352, #354, #358, #36, #361, #37, #372, #375, #380, #46, #52, #8, #95, 02/10-15, 02/10-2, 02/10-9.
4. Prove: banco v1.1 (`strumenti/banco_errori_v1.1.py`; la v1.0 lasciava scritti alla lettera i segnaposto {{ORA-1}}…): COPERTI da 119 a 171, NON COPERTI da 96 a 44, 0 errori del banco, 0 falsi allarmi sui casi giusti; `tests/errori/baseline-coperti.json` riscritto con i 171. `prove/prova_controlli_ripristinati.py`: 74/74, con 0 falsi allarmi su 166 messaggi veri di Claude e 5 kit del 20/11/2026 (più le pagine di docs/ con i controlli che bloccano il push). Sugli 1.263 messaggi del 15-22/11 i controlli rimessi hanno scattato 10 volte (0,8 %), quasi tutte per errori veri.
5. Limite: sono controlli sulle parole; «risolto», «a posto», «funziona» passano se nel messaggio c'è una qualunque prova (fonte, ora, esito, «non provato»), come per il vecchio (c). Il controllo #263 (carta e penna) non blocca il push: 13 pagine vecchie di docs/ lo violano e il blocco impedirebbe di modificarle.

## Changelog

1. v1.0 (28/10/2026): prima versione; 22 controlli dell'hook del messaggio (18 nuovi), 3 nuovi controlli prima dei comandi, audit notturno, passi notturni, annuncio «OGGI» in verifica_lezione.py.
2. v1.1 (28/10/2026, audit): passi notturni v1.1 con lo stato della notte e il controllore dei controlli; hook limite-comandi.py anche contro mv e git mv delle versioni; audit_regole.py vede anche le versioni rinominate.
3. v1.2 (29/10/2026): §03 punto 8, regola 30 (bottone «Serve te» del cruscotto con le sole criticità per il docente).
4. v1.3 (29/10/2026, audit della giornata): voci #147-#154 con i loro controlli (hook w, x, y, z; 5 controlli nuovi in `controlla_controlli.py`); conteggio a 176 voci.
5. v1.4 (29/10/2026, controllore di fine giornata): voci #139-#146 e #155-#157 in tabella, tutte A; hook (aa) e (bb), controllo `valore_nudo` prima del push, `controlla_controlli.py --fine-giornata`; conteggio a 187 voci.
6. v1.5 (30/10/2026, controllore di fine giornata): voci #158-#170 in tabella, tutte A; hook (cc)-(ii), 7 controlli nuovi in `controlla_controlli.py --fine-giornata` (#160, #162, #163, #164, #168, #169, #170), voci «sospeso» verdi in `verifica_lezione.py`, storico dei quiz in `situazione_quiz.py`; conteggio a 200 voci.
7. v1.6 (06/11/2026, controllore di fine giornata): voci #223-#235 in tabella, tutte D (strumenti da costruire, descritti nella colonna «Dove scatta»); i conteggi della sezione 01 e le voci #171-#222 non sono stati ricalcolati e vanno riallineati.
8. v1.7 (09/11/2026): voce #236 (numero del PC come casella di testo, 11-38 in aula 11) con controllo pc_a_menu in controlli_pagine.py.
9. v1.8 (09/11/2026, controllore di fine giornata): voci #237-#247 (teoria non fattibile, quiz scegli 2 e non selettivi, lezione cambiata in corsa, cruscotti fermi, report orari assenti, ponte, messaggi lunghi, hook versionato); #243 A, le altre D.
10. v1.9 (10/11/2026, controllore di fine giornata): voci #248-#253, tutte D (nessun controllo automatico ancora).
11. v1.10 (11/11/2026): voci #255-#266 dalla chat segnata del 10/11, tutte D (controllo automatico: mancante).
12. v1.12 (11/11/2026): voci #270-#271 (PPP ignorato, richiesta interpretata), tutte D, controllo automatico: mancante.
13. v1.13 (11/11/2026): voce #272 (controlli e passi chiesti al docente in lezione), D, controllo automatico: mancante.
14. v1.14 (11/11/2026): voce #273 (stesso file rimandato, D, controllo mancante) e voce #274 (lingue 1INF nei quiz, A: `strumenti/controlla_lingue_quiz.py`, R6). Il conteggio della sezione 01 non è stato ricalcolato.
15. v1.15 (11/11/2026, controllore di fine giornata): voci #267 e #275-#284; #279 A, le altre D. Il conteggio della sezione 01 non è stato ricalcolato.
16. v1.16 (12/11/2026): controllo (ff) formato kit e documenti nell'hook del messaggio; voci #285-#289, #291, #293, #309, #311, #312 in tabella (#286 resta D); #282 passa ad A. Il conteggio della sezione 01 non è stato ricalcolato.
17. v1.17 (12/11/2026, controllore di fine giornata sera): aggiunte le voci mancanti #292, #294-#308, #310 e #313-#325 (le ultime sei, #320-#325, nate dal controllo di fine giornata); #324 e #325 con controllo automatico nuovo in `controlla_controlli.py` (orario del giorno da FIRME-REGISTRO e PROSSIME-LEZIONI, nome intero nella privacy). Il conteggio della sezione 01 non è stato ricalcolato.
18. v1.18 (13/11/2026): il controllo di fine giornata di `strumenti/controlla_controlli.py` verifica che per ogni lezione del giorno ci sia una riga in ARGOMENTI-SVOLTI-2026-27.md e che non sia ancora «previsto, da aggiornare» (R5.3, Allegato A allineato; richiesta del docente «tieni sempre allineato e aggiornato l'Allegato A»); prove 36/36 in `strumenti/prova_controlla_controlli.py`. Voce #276: da «mancante» a «parziale». Il conteggio della sezione 01 non è stato ricalcolato.
19. v1.19 (13/11/2026): voce #328 (dispense poco chiare per ragazzi delle medie) con il controllo `strumenti/controlla_leggibilita.py`: frasi lunghe, parole astratte senza spiegazione, passi senza «dove», esercizi senza esempio, pronomi vaghi, consegne senza soggetto o senza oggetto, parole non allineate. Richiamabile a mano, non bloccante; il conteggio della sezione 01 non è aggiornato (le voci #326-#327 non sono ancora in tabella).
20. v1.20 (13/11/2026): voce #329 (solo il COGNOME in chat) e voce #281 passata ad automatico (avviso non bloccante).
21. v1.21 (13/11/2026, audit del pomeriggio): voci #326, #327 (mancavano nella mappa), #330, #331 e #332; nuovo controllo `strumenti/controlla_pdf_ragazzi.py` (nome del file sicuro, note tecniche, fittezza, copia su origin/main); #150 di `controlla_controlli.py` adeguato alla Fabbrica (quiz di Sicurezza in `fabbrica/indice.json`).
22. v1.22 (13/11/2026, controllore di fine giornata): voci #333 (motore non provato attivato), #334 (orario presunto, domanda che contraddice il docente) e #335 (correzioni su motore.js prima del «via»), tutte D con la regola e il controllo da costruire.
23. v1.23 (16/11/2026, controllore di fine giornata): voci #336-#349 (il registro era a #335); nuovi controlli: avviso di lunghezza del messaggio in `controllo-messaggio.py` (#342, chiude da D ad A anche #242 e #250) e `firme_sospette` in `controlla_controlli.py` (#343); maschera della password nel hook bobina (#344). Il conteggio della sezione 01 non è stato ricalcolato.
24. v1.24 (17/11/2026): voci #350 (mancava) e #351 (archivio prove: `archivia_prova.py`, un solo ZIP e controllo di completezza). Il conteggio della sezione 01 non è stato ricalcolato.
25. v1.25 (17/11/2026): voci #352-#355 dal controllore di fine giornata (kit senza consegna e tempo, script voti per il lotto sbagliato, Drive promesso senza prova, fine giornata ROSSO). Il conteggio della sezione 01 non è stato ricalcolato.
26. v1.26 (18/11/2026): voce #357 (budget dei preventivi 1INF) con il controllo `strumenti/controlla_budget_1inf.py` e la fonte unica `config/budget-1inf-1811.json`. Il conteggio della sezione 01 non è stato ricalcolato.
27. v1.27 (18/11/2026, ore 09:5x): decisione del docente, budget 500/600/1000: fonte unica v2.0, `controlla_budget_1inf.py` accetta 500/600/1000 e rifiuta 450/900 nelle versioni correnti (chiave «non_usare_oggi»); nota al #357 in `REGISTRO-ERRORI-CLAUDE.md` v3.42.
28. v1.28 (18/11/2026, controllore di fine giornata): righe #358-#374 aggiunte (#358-#366 e #367 mancavano; #368-#374 nuove). Copertura: nessun controllo automatico nuovo (principio: da costruire = D); il conteggio della sezione 01 non è stato ricalcolato.
29. v1.29 (19/11/2026, controllore di fine giornata): righe #375-#383 aggiunte (#375-#377 mancavano; #378-#383 nuove). Copertura: nessun controllo automatico nuovo (principio: da costruire = D, correzione in `INFO-PIU-USATE-v1.8.md`); il conteggio della sezione 01 non è stato ricalcolato.
30. v1.30 (20/11/2026, controllore di fine giornata): righe #384-#389 (#384 e #385 mancavano; #386-#389 nuove, tutte D salvo #388 B). Il conteggio della sezione 01 non è stato ricalcolato.
31. v1.31 (23/11/2026, ordine del docente: controlli mancanti per #386-#389): #386, #387, #388, #389 da D ad A; controlli (kk) (ll) (mm) in `controllo-messaggio.py`, `controlla_kit.py` v1.4, `controlla_controlli.py` punto 10, libreria `strumenti/controlli_consegna.py`; prove 331 su 331 (prova_consegna 60, prova_controlla_kit 15, prova_controlla_controlli 48). Il conteggio della sezione 01 non è stato ricalcolato.
32. v1.32 (23/11/2026, ordine del docente: banco di prova degli errori): aggiunta la sezione 07; la tabella della sezione 04 e i conteggi della sezione 01 non sono stati riscritti. Banco: 414 voci, 119 coperte, 96 non coperte, 13 casi da scrivere, 186 non verificabili a macchina.
33. v1.33 (23/11/2026): sezione 08, controlli rimessi (47) e risolti altrove (4: #11, #36, #52, 02/10-9); righe corrette nella tabella; banco v1.1.
