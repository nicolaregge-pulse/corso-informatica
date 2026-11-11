# 00 Mappa regole e controlli

**Versione 1.12** — 11/11/2026 — documento interno del docente e di Claude

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
| 01/10-6 | Anti-plagio sempre al condizionale, «da verificare» | 2 | D | A | hook controllo-messaggio.py (s), «ha copiato» detto come certo |
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
| 02/10-9 | Nelle istruzioni di Classroom solo il link unico della pagina, mai PDF versionati | 6 | D | A | hook limite-comandi.py (versioni non cancellabili) + audit_regole.py (passi notturni 01.1) 01 (link a file che non esistono) |
| 02/10-10 | Versione in copertina, pagina senza cache, Ctrl+F5 | 6 | D | D | la memoria del browser del docente non si vede da qui |
| 02/10-11 | Mai agganciare un compito manuale prima che il docente lo crei | 6 | C | C | superata: dal 21/10 i compiti nascono solo dalla coda, in bozza (script v8.2) |
| 02/10-12 | Non far modificare un compito durante la lezione (sale in cima) | 6 | D | D | consiglio dato in chat: nessuna parola sicura da cercare |
| 02/10-13 | Una azione per messaggio quando la situazione è nuova; punto esatto dello screenshot | 5 | D | A | hook controllo-messaggio.py (q) messaggi lunghi in lezione, (k) catene di coordinate |
| 02/10-14 | Ogni chiave di correzione ha la versione nel nome, mai sovrascritta | 6 | D | D | servirebbe il divieto di sovrascrivere chiavi nei generatori |
| 02/10-15 | Controllo aritmetico automatico degli esempi prima del PDF | 3 | D | D | promesso e mai costruito: servirebbe nel generatore delle dispense |
| #1 | I testi per Classroom vanno impaginati (una riga per passo) | 5 | D | B | audit_regole.py (passi notturni 01.1) 04 (righe più lunghe di 300 caratteri) |
| #2 | Titoletti in maiuscolo, numeri, righe vuote tra i blocchi | 5 | D | B | come #1 |
| #3 | Tutto ciò che il docente segnala va nel registro e in una regola | 1 | D | A | hook controllo-messaggio.py (n) richiesta di registrare un errore senza numero |
| #4 | In docs/ le versioni già usate in classe non si cancellano | 1 | D | A | hook limite-comandi.py (cancellazione di versioni rifiutata) + audit_regole.py (passi notturni 01.1) 07 |
| #5 | Dalla miniatura Veyon solo «sulla pagina X alle HH:MM», mai «non ha fatto niente» | 2 | D | A | hook controllo-messaggio.py (r) «non ha iniziato / non ha fatto niente» senza fonte |
| #6 | In classe risposte corte: solo testo da incollare e link | 5 | D | A | hook controllo-messaggio.py (q) più di 30 righe nelle ore di lezione |
| #7 | Quando il lavoro è su GitHub, la consegna la genera Claude | 6 | D | D | scelta di progetto della lezione |
| #8 | Le traduzioni si mostrano solo a chi servono (bangla solo PC 14) | 1 | D | D | la pagina per PC non si distingue in automatico dalla pagina per tutti |
| #9 | Dopo ogni modifica a una pagina con script: node --check e prova | 1 | D | A | hook limite-comandi.py (prima del push: sintassi di tutti gli script) + audit_regole.py (passi notturni 01.1) 01 |
| #10 | La pagina della classe mostra solo il lavoro del giorno | 4 | D | B | passi-notturni.md 02.9 |
| #11 | La firma non si deduce dal bottone «FIRMA ✓» | 2 | D | A | hook controllo-messaggio.py (m) firma ricordata con FIRME-REGISTRO tutto firmato |
| #12 | Dopo un rebase i coda/*.json si devono leggere prima del push | 1 | D | A | hook limite-comandi.py (push del riservato fermato con JSON rotti) + audit_regole.py (passi notturni 01.1) 03 |
| #13 | Un solo compito aperto alla volta su Classroom | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 (un compito per classe al giorno) |
| #14 | Caricare file su GitHub con Add file → Upload files; dopo una rigenerazione si contano i riquadri | 6 | D | D | scelta di metodo; la rigenerazione è coperta in parte da passi-notturni.md 02.9 |
| #15 | Mai chiedere di riconoscere un file dall'estensione | 5 | D | D | i nomi di file nelle pagine sono spesso leciti: troppi falsi allarmi |
| #16 | Mai «non ha caricato» senza la ricerca e il clone | 2 | D | A | hook controllo-messaggio.py (r) |
| #17 | File grandi divisi prima; dire quali scaricare e quanti | 5 | D | D | l'invio dei file in chat non passa da un hook |
| #18 | Chiusura dopo l'ultima raccolta; abbinamenti sul cognome intero | 6 | D | D | servirebbe un controllo nei correttori |
| #19 | Segnalazioni di guasti salvate nel riservato; prima di «mai segnalato» si guarda lì | 2 | D | D | servirebbe un elenco dei guasti letto dall'audit |
| #20 | Ripubblicando una pagina che si salva da sola, il blocco dati si sostituisce una volta | 1 | D | A | hook limite-comandi.py (sintassi degli script prima del push) |
| #21 | Se un risultato è stato chiesto, si consegna appena pronto (il PPP non lo ferma) | 1 | D | A | hook controllo-messaggio.py (t) «al tuo avanti» dopo «dammi/fammi» |
| #22 | Prima di una media, ogni colonna è un lavoro diverso | 6 | D | D | servirebbe un controllo nel generatore delle griglie |
| #23 | Materia del voto dall'argomento; voto minimo 40 | 1 | D | A | hook controllo-messaggio.py (g) voti sotto 40 e Disciplina nella stringa DIDAweb |
| #24 | I passaggi che si possono automatizzare si automatizzano subito | 3 | C | C | superata: i quiz su Moduli li crea il ponte (forms.crea_quiz) |
| #25 | Una sola lista di password per classe; prova di apertura di ogni libro | 1 | D | D | servirebbe la prova di apertura dentro il generatore dello zip |
| #26 | Ogni file personale comincia con Cognome-Nome | 5 | D | D | servirebbe un controllo nei generatori dei libri |
| #27 | Ogni PDF si apre e si controlla prima di mandarlo | 2 | D | D | l'invio dei file in chat non passa da un hook |
| #28 | Uno strumento per un sito esterno si prova sull'HTML vero | 2 | D | D | giudizio di progetto |
| #29 | Link al riservato sempre con «apri il profilo personale» | 1 | D | A | hook controllo-messaggio.py (o) |
| #30 | Lavori uguali in due caselle = una colonna sola | 6 | D | D | come #22 |
| #31 | Ogni messaggio con passi ha TUTTE le caselle da copiare | 5 | D | A | hook controllo-messaggio.py (u) rimando a riquadri di prima |
| #32 | Mai due copie in fila: la seconda cancella la prima | 1 | A | A | hook controllo-messaggio.py (a) ordine copia/incolla |
| #33 | Prima di nominare un materiale, si dice dove trovarlo | 5 | D | D | non si sa in automatico se i ragazzi hanno un materiale |
| #34 | Mentre un comando che pubblica è in attesa non si spinge altro; un annuncio solo | 1 | D | B | audit_regole.py (passi notturni 01.1) 05 (un annuncio per classe al giorno) |
| #35 | A fine ora si consegna quello che c'è; zip pronto 10 minuti prima | 4 | D | B | passi-notturni.md 03.3 (promemoria 10 minuti prima della fine) |
| #36 | La firma non si deduce dal bottone (ripetizione di #11) | 1 | D | A | hook controllo-messaggio.py (m) |
| #37 | «Script fermo» solo dopo una prova del ponte | 2 | B | B | Chat del giorno, passo 5 (battito con un comando del ponte); la frase «esce entro 5 minuti» è superata da #130 |
| #38 | Progetto di squadra: un canale, tutti consegnano, prima fase entro 20 minuti | 4 | D | B | passi-notturni.md 02.4 e 02.7 |
| #39 | Orari dall'ora vera; una cosa da fare per volta; modifiche verificate | 2 | D | D | lezione in corsa; solo «modifiche verificate» è coperta da hook controllo-messaggio.py (c) |
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
| #51 | Prima di incollare in Apps Script si clicca automazione-corso.gs | 5 | D | A | hook controllo-messaggio.py (v) e (p) |
| #52 | Firma: mai dedotta dallo screenshot (terza volta) | 1 | D | A | hook controllo-messaggio.py (m) |
| #53 | Niente avverbi e aggettivi che non servono | 5 | D | A | hook controllo-messaggio.py (j) |
| #54 | Le considerazioni del docente non si interpretano: una domanda sola | 6 | D | D | intenzione del docente: non controllabile |
| #55 | Istruzioni senza «se», «salta», domande | 5 | D | A | hook controllo-messaggio.py (l) |
| #56 | Passi come frasi che cominciano con il verbo, non catene di coordinate | 5 | D | A | hook controllo-messaggio.py (k) |
| #57 | Ripetizione di #50 | 1 | A | A | hook controllo-messaggio.py (a) |
| #58 | Comandi eseguiti archiviati; dopo un comando controllo entro 2 minuti | 6 | D | B | audit_regole.py (passi notturni 01.1) 06 (comandi non archiviati e fermi) |
| #59 | Ogni richiesta del docente va subito nell'elenco dei lavori aperti | 4 | D | D | non si riconosce in automatico una richiesta dentro un PPP |
| #60 | Ogni pagina dei ragazzi ha i bottoni per autoregolarsi | 1 | B | B | audit pre-lezione delle 06:50 punto 3 + passi-notturni.md 02.10 |
| #61 | Verifica provata con ricarica, chiusura, bottoni e consegna fino all'arrivo | 2 | A | A | rimedio nel codice del motore della verifica (salvataggio ogni 2 secondi, ripresa) + prova_verifica.js |
| #62 | Ai ragazzi una azione per frase; la consegna è UN bottone | 5 | D | B | audit_regole.py (passi notturni 01.1) 01 (Modulo + incolla) + passi-notturni.md 02.7 |
| #63 | «Fatto» o «non serve più» solo dopo la prova | 2 | A | A | hook controllo-messaggio.py (c) e (d) |
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
| #83 | Lo screenshot non è la prova: la prova è il file nel repository | 2 | D | A | hook controllo-messaggio.py (r) «non ha caricato» senza fonte e (c) |
| #84 | Un link si mette solo se la pagina esiste | 2 | D | B | audit_regole.py (passi notturni 01.1) 01 (link a file che non esistono) |
| #85 | Nomi e voti in docs/ solo cifrati | 1 | D | A | hook limite-comandi.py (nomi in chiaro prima del push) + audit_regole.py (passi notturni 01.1) 01-02 |
| #86 | Finita una classe, il giro di quella classe si ferma | 4 | D | B | passi-notturni.md 03.3 |
| #87 | «FIRMA ✓» in verde = firmata | 1 | D | A | hook controllo-messaggio.py (m) |
| #88 | Battito di meno di 3 minuti prima di «lo pubblica lo script» | 2 | D | A | hook controllo-messaggio.py (f) promesse sui tempi dello script + (d) |
| #89 | Una sola strada per volta; stesso titolo per l'anti-doppione | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 (un compito per classe al giorno) |
| #90 | «Nessuna AI» solo dopo aver visto tutte le finestre | 2 | D | A | hook controllo-messaggio.py (h) |
| #91 | Titoli del registro solo sull'Allegato A più recente | 6 | D | D | servirebbe un controllo dei titoli del registro sul .docx dell'Allegato A |
| #92 | «Altro» = presente | 1 | D | D | conteggio dei presenti fatto a mano dallo screenshot |
| #93 | Un solo compito per lezione; quiz diverso dalla verifica | 6 | D | B | audit_regole.py (passi notturni 01.1) 04 |
| #94 | Ogni lezione ha l'annuncio «OGGI FATE SOLO…» in cima | 4 | D | A | verifica_lezione.py (annuncio più recente senza «OGGI» = GIALLO) + hook controllo-messaggio.py (d) |
| #95 | Si legge il massimo di ogni quiz; «non risulta» mai su una fonte sola | 2 | D | D | massimo del quiz: servirebbe nel calcolo dei voti; la parte «non risulta» è coperta da hook controllo-messaggio.py (r) |
| #96 | Colonna «Firma» con data e ora = firmata | 1 | D | A | hook controllo-messaggio.py (m) |
| #97 | Scadenze sulle campanelle vere | 1 | D | B | audit_regole.py (passi notturni 01.1) 04 |
| #98 | Prima della stringa dei voti, la materia dell'ora | 1 | D | A | hook controllo-messaggio.py (g) |
| #99 | Prima di preparare una lezione si rilegge la storia della classe | 4 | D | B | passi-notturni.md 02.1 |
| #100 | PC senza nome: si chiede subito chi c'è | 1 | D | A | hook controllo-messaggio.py (i) |
| #101 | Terza volta #50: procedura dello script da RIPARTENZA §03 | 1 | A | A | hook controllo-messaggio.py (a) e (v) |
| #102 | Durata stimata dal contenuto e provata a tempo | 6 | D | B | passi-notturni.md 02.5 |
| #103 | Ogni pagina che produce un risultato lo fa arrivare al docente | 6 | D | B | passi-notturni.md 02.8 |
| #104 | «Ponte OK» solo dopo un comando di prova eseguito | 2 | B | B | Chat del giorno, passo 5 (battito) + passi-notturni.md 01.4 |
| #105 | Pubblicare = pagina + compito + annuncio | 2 | A | A | hook controllo-messaggio.py (d) con verifica_lezione.py |
| #106 | I nomi dei bottoni si copiano dalla pagina vera | 2 | D | D | il nome giusto non è noto all'hook |
| #107 | Un solo annuncio e un solo compito al giorno per classe | 1 | D | B | audit_regole.py (passi notturni 01.1) 05 |
| #108 | Nelle tabelle tutti e soli i presenti; abbinamento per cognome | 6 | D | D | servirebbe un controllo nei generatori dei cruscotti |
| #109 | «Fuori compito» solo se lo schermo mostra un'altra attività | 2 | D | D | lettura delle schermate: giudizio |
| #110 | Il primo passo produce qualcosa di visibile entro 10 minuti | 4 | D | B | passi-notturni.md 02.4 |
| #111 | Due ritagli uguali consecutivi: ne resta uno | 6 | D | D | si può aggiungere a report_ore.py un confronto delle immagini |
| #112 | In lezione i giri non spingono sul riservato; si recuperano le righe «SOLO QUI» | 1 | B | B | audit pre-lezione delle 06:50 punto 4 + passi-notturni.md 03.3 |
| #113 | Un errore da registrare si scrive subito, con il numero | 4 | D | A | hook controllo-messaggio.py (n) |
| #114 | Un comando del ponte = poche azioni e un salvataggio; controllo entro 5 minuti | 1 | D | B | audit_regole.py (passi notturni 01.1) 06 |
| #115 | Mai «risolto» per lo script senza prova nel tempo | 2 | A | A | hook controllo-messaggio.py (c) |
| #116 | Ogni conteggio che dà punti si protegge dagli abusi prima | 4 | D | D | servirebbe una prova con testo finto nei controlli della lezione |
| #117 | Pacchetto DIDAweb con «Disciplina da scegliere» sopra | 1 | D | A | hook controllo-messaggio.py (g) |
| #118 | Dopo ogni modifica: node --check di tutti gli script e prova | 1 | D | A | hook limite-comandi.py (sintassi prima del push) + audit_regole.py (passi notturni 01.1) 01 |
| #119 | Lingue di ogni classe dai documenti, con un audit | 1 | D | A | hook limite-comandi.py (lingue prima del push) + passi-notturni.md 02.11 |
| #120 | Prima di «pubblicata» i tre pezzi; una cosa decisa si prepara senza richiederla | 1 | A | A | hook controllo-messaggio.py (d) |
| #121 | Prima di un compito si leggono i compiti del giorno su Classroom | 1 | D | D | servirebbe che chi scrive la coda chieda prima classroom.compiti al ponte |
| #122 | La scadenza la decide il docente; non si inventano orari | 6 | D | D | solo il docente sa che cosa ha detto; la campanella è controllata da audit_regole.py (passi notturni 01.1) 04 |
| #123 | Ogni passo per un dodicenne; domande all'assistente lette a ogni giro | 5 | D | B | passi-notturni.md 02.2 |
| #124 | «Mandata!» solo quando l'invio è partito | 2 | A | A | rimedio nel codice: docs/assistente/assistente.js |
| #125 | Pochi comandi al ponte; prova prima di dire che lo script funziona | 1 | D | B | audit_regole.py (passi notturni 01.1) 06 (più di 40 comandi in un giorno) |
| #126 | Versione facile di massimo 3 passi preparata prima | 4 | D | B | passi-notturni.md 02.3 |
| #127 | Dati fermi = ora in rosso; «fatto» solo dopo averlo fatto | 2 | A | A | hook controllo-messaggio.py (c); l'ora in rosso nelle pagine è da controllare a mano |
| #128 | «Tutto a posto» solo dopo le tre prove | 2 | A | A | hook controllo-messaggio.py (d) |
| #129 | Quiz e Moduli prima della campanella; mai «arriva tra poco» | 4 | B | B | Chat del giorno, passo 5 (quiz) + audit_regole.py (passi notturni 01.1) 01 («arriva tra poco») |
| #130 | Non si promettono tempi per ciò che fa lo script | 3 | D | A | hook controllo-messaggio.py (f) |
| #131 | Piano B: annuncio pronto 10 minuti prima | 4 | B | B | Chat del giorno, passo 5 (piano B) + passi-notturni.md 03.2 |
| #132 | Comandi di una riga, risultati lunghi in un file | 5 | A | A | hook limite-comandi.py (massimo 3 comandi, 600 caratteri) |
| #133 | Cruscotto progettato sulla consegna del giorno | 4 | B | B | Chat del giorno, passo 5 (cruscotto con la colonna delle consegne) |
| #134 | Ogni audit confronta 2 allievi con la fonte | 2 | B | B | Chat del giorno, passo 5 (confronto di 2 allievi) |
| #135 | «A posto» solo dopo una compilazione riuscita | 2 | A | A | hook controllo-messaggio.py (c) |
| #136 | Nessun link al sito della Regione nelle pagine dei ragazzi | 6 | D | A | hook limite-comandi.py (prima del push) + audit_regole.py (passi notturni 01.1) 01 |
| #137 | La cosa bloccante va da sola nella prima riga | 5 | A | A | hook controllo-messaggio.py (b) + passi-notturni.md 03.1 (firma alle 13:30) |
| #138 | Copia e incolla: un Ctrl+V usa l'ultima cosa copiata | 1 | A | A | hook controllo-messaggio.py (a) |
| #139 | Un ROSSO dell'audit non si liquida come atteso: va in prima riga | 2 | D | A | controlla_controlli.py (prima riga «DA SAPERE SUBITO», notte di oggi) |
| #140 | Un bottone è presente solo se si vede sul sito vero, modalità Docente | 2 | D | A | hook controllo-messaggio.py (y) + controlla_controlli.py --fine-giornata (piano con «pubblicata») |
| #141 | Nessuna classe in aula con Classroom vuoto | 3 | D | A | controlla_controlli.py (notte girata da sola, #152) + --fine-giornata (compito uscito entro la campanella) |
| #142 | Cruscotto con i KPI del giorno e una riga per presente alla campanella | 4 | D | A | controlla_controlli.py --fine-giornata (righe = presenti) + coppia docente/ragazzi (#148) |
| #143 | Al massimo 2 aiutanti accesi insieme | 6 | D | A | hook controllo-messaggio.py (bb) |
| #144 | Dopo la pubblicazione il piano mostra solo la proposta fatta, senza bottoni | 2 | D | A | controlla_controlli.py --fine-giornata (piano senza «pubblicata» = ROSSO) + hook (c) |
| #145 | Le domande del giorno si vedono tutte e hanno risposta | 4 | D | A | controlla_controlli.py --fine-giornata (domande senza risposta, regola 22) |
| #146 | Percorso provato da capo; mai «null» o PC non confermati nel cruscotto | 4 | D | A | controlli_pagine.py (valore_nudo, prima del push) + controlla_controlli.py --fine-giornata (nessun «null») |
| #147 | Un JSON letto da una pagina non perde campi: i vecchi restano come alias | 6 | D | A | controlla_controlli.py (formato dei JSON, #147) |
| #148 | Docente e ragazzi leggono dati dello stesso giro (stesso «generato») | 6 | D | A | controlla_controlli.py (coppia docente/ragazzi, #148) |
| #149 | Tutti i quiz del giorno letti insieme, ognuno con il suo comando | 6 | D | A | controlla_controlli.py (ponte dei quiz, #149) |
| #150 | Sicurezza: compito con quiz e ora dopo pronti prima della lezione | 4 | D | A | controlla_controlli.py (Sicurezza preparata, #150) |
| #151 | Un conteggio di consegne si rilegge alla fonte e porta fonte e ora | 2 | D | A | hook controllo-messaggio.py (w) |
| #152 | Attività automatica pronta solo dopo un giro di prova vero | 2 | D | A | hook controllo-messaggio.py (x) + controlla_controlli.py (notte girata da sola) |
| #153 | Pagina verificata sul sito vero con i dati veri, non con ?prova=1 | 2 | D | A | hook controllo-messaggio.py (y) |
| #154 | Prima di chiedere al docente si guarda nei file del giorno | 1 | D | A | hook controllo-messaggio.py (z) |
| #155 | Si misura il risultato: controllore di fine giornata sul dato vero | 2 | D | A | controlla_controlli.py --fine-giornata (report/<giorno>/non-andato.md) |
| #156 | Nessun 40 a chi ha finito o consegnato; senza consegna «voto dopo la consegna» | 6 | D | A | controlla_controlli.py --fine-giornata (40 con percorso finito) + controlli_pagine.py (valore_nudo) |
| #157 | Una release vale per tutto il repository; progetto serio = repository suo | 5 | D | A | hook controllo-messaggio.py (aa) |
| #158 | Incolla in Apps Script: clic dentro il codice, Ctrl+A «tutto blu», Ctrl+V, controllo righe | 5 | D | A | hook controllo-messaggio.py (ii) |
| #159 | «Prima ora» = ora della giornata; nella risposta si scrive l'orario | 6 | D | A | hook controllo-messaggio.py (gg) |
| #160 | Il quiz chiede solo lavoro già fatto prima del quiz | 4 | D | A | controlla_controlli.py --fine-giornata (_quiz_lavoro_futuro) |
| #161 | Mai «non arrivato» su dati di più di 5 minuti; il docente non controlla da solo | 2 | D | A | hook controllo-messaggio.py (hh) + watchdog del laboratorio |
| #162 | Laboratorio di 2-3 ore: un lavoro per ogni ora, pronto entro le 18 del giorno prima | 4 | D | A | controlla_controlli.py --fine-giornata (proposta non divisa ora per ora) |
| #163 | 1INF: ogni materiale per i ragazzi in italiano, arabo e cinese insieme | 1 | D | A | controlla_controlli.py --fine-giornata (dispensa e pagine del piano senza ar/zh) |
| #164 | Ai ragazzi un solo posto: compito del giorno con la pagina hub | 5 | D | A | hook controllo-messaggio.py (ff) + controlla_controlli.py --fine-giornata (troppi compiti «OGGI») |
| #165 | I dati del docente si scrivono in caselle (foglio Google), non in un PDF | 5 | D | A | hook controllo-messaggio.py (ee) |
| #166 | Una domanda del docente chiede una spiegazione; si toglie solo con «togli/elimina» | 6 | D | A | hook controllo-messaggio.py (cc) |
| #167 | Il genere di un allievo non si dà per scontato: si usa il nome | 6 | D | A | hook controllo-messaggio.py (dd) |
| #168 | Script nuovo provato con una bozza vera la sera prima; piano B pronto subito | 4 | D | A | verifica_lezione.py (coda senza id = ROSSO, «sospeso» = verde) + controlla_controlli.py --fine-giornata |
| #169 | I giri del cruscotto lasciano un segnale e si riaccendono; nessun buco > 12 minuti | 2 | D | A | controlla_controlli.py --fine-giornata (buchi nello storico) |
| #170 | Colonna del cruscotto solo dopo un invio vero; fonte vuota detta subito | 2 | D | A | controlla_controlli.py --fine-giornata (colonna «pratica» vuota) + situazione_quiz.py (storico) |
| #223 | Sull Allegato A dopo il 30/10 si puo solo togliere; prima di proporre si leggono le note | 1 | D | D | il controllo dei testi del registro deve dire «voce piu vicina»; ancora da costruire |
| #224 | Proposte fatte senza aver letto le regole | 1 | D | D | promemoria-errori.py deve ricordare, a ogni richiesta di proposta su registro o Allegato A, «prima leggi NOTE-DA-DISCUTERE.md» (da costruire) |
| #225 | Post ora 4 della 1INF pubblicato dal docente senza link | 1 | D | D | Il pacchetto del post (R2.3) deve avere sempre il link gia dentro (da costruire) |
| #226 | Pacchetto voti DIDAweb con «h 1» invece di «h 6» | 2 | D | D | Il generatore del pacchetto voti deve leggere l ora dalla riga del registro e confrontarla (da costruire) |
| #227 | Copiare lfm e pas da Classroom: i ragazzi non ce l hanno fatta | 1 | D | D | controlli_pagine.py e il controllo del post: un passo che dice «copia» un file senza zip o percorso e un errore (da costruire) |
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
| #242 | Messaggi in lezione troppo lunghi e senza riquadri da copiare (09/11) | 4 | D | D | controllo-messaggio.py (R4): in ora di lezione ROSSO se il messaggio ha piu di 10 righe, o un testo da incollare fuori da un blocco di codice. Da veri |
| #243 | Messaggio con link senza PUBBLICATO bloccato dall hook (09/11) | 2 | A | A | Nessuno nuovo: controllo-messaggio.py funziona. Resta da insegnare al generatore di messaggi a non scrivere il link prima. Voce A. |
| #244 | Cruscotto 3INF fermo ai dati del 04/11, nessun dato dei presenti il 09/11 | 4 | D | D | verifica_lezione.py e cruscotto_classe.py: ROSSO se dati.json non e del giorno e la classe ha lezione oggi (gia in #233). Da verificare perche non ha |
| #245 | Report PDF orari, presenze e Veyon del 09/11 assenti | 4 | D | D | report_ore.py va lanciato dal giro a fine di ogni ora; controlla_controlli.py --fine-giornata ROSSO se per un ora in orario manca il PDF. Da costruire |
| #246 | Ponte: due comandi in-attesa-PUBB mai chiusi e riepilogo del ponte fermo al 03/11 (09/11) | 2 | D | D | Il riepilogo del ponte si rigenera a ogni giro; a fine giornata i comandi in-attesa-PUBB si annullano o si chiudono. controlla_controlli.py --fine-gio |
| #247 | Stop hook «tutto versionato» scattato circa 25 volte il 09/11 | 2 | D | D | Commit e push a fine di ogni blocco di lavoro (R11.1); un hook di fine turno che committa da solo i file del riservato (come la bobina automatica). Da |
| #248 | Codice lungo e spiegazioni mescolati in chat (10/11) | 4 | D | D | R4 3ter senza controllo: da costruire, ma da riallineare con #253 |
| #249 | Account PIAMARTA e testi in riquadro non rispettati (10/11) | 4 | D | D | Nessun controllo automatico che verifichi 3bis nei messaggi |
| #250 | Troppa verbosita, spiegazioni non capite, «ricomincia da zero» (10/11) | 4 | D | D | Il limite di lunghezza in ora di lezione (R4.2) non e controllato da uno strumento |
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
| #263 | Schede su carta per tutti senza stampante (10/11) | 4 | D | D | controllo automatico: mancante |
| #264 | Cruscotto dato come file e non come URL (10/11) | 4 | D | D | controllo automatico: mancante |
| #265 | Sistema nuovo non spiegato e nome non visibile (10/11) | 4 | D | D | controllo automatico: mancante |
| #266 | Passo non riscritto, rimando a messaggi precedenti (10/11) | 4 | D | D | controllo automatico: mancante |
| #268 | Passo senza la finestra Chrome dell'account (11/11) | 4 | D | D | controllo automatico: mancante (idea: in controllo-messaggio.py ogni riga «Passo N» deve contenere PIAMARTA o PERSONALE) |
| #269 | Soglia «7 su 10» presunta nel post e nei quiz (11/11) | 7 | D | D | controllo automatico: mancante (idea: cercare nei testi per i ragazzi numeri e soglie non presenti in un file verificato) |
| #270 | PPP ignorato: consegna subito e file due volte (11/11) | 3 | D | D | controllo automatico: mancante (idea: controllo-messaggio.py segnala un messaggio lungo dopo una richiesta che comincia con PPP) |
| #271 | Richiesta interpretata invece di seguire la lettera (11/11) | 7 | D | D | controllo automatico: mancante |

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
