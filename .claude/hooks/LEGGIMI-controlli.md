# 00 Controlli automatici contro gli errori ripetuti

**Versione 1.20** — 24/11/2026 (capitolo 17: hook vivi, errore #392; prima: 1.19, 1.18, 1.17, 1.16, 1.15, 1.14, 1.13, 1.12) — documento interno del docente e di Claude


> **OBIETTIVO PRINCIPALE DEL FILTRO DI BUON SENSO (23/11/2026).** Il docente: «Io perdo il 50% del tempo con te o a gestire domande inutili o a gestire i tuoi errori.» (il 50% è una STIMA dichiarata dal docente, non una misura). Quindi: niente domande ovvie, messaggi brevi, controllare prima di scrivere. Capitolo 15.

> **Dal 04/11/2026 (v1.4) valgono le decisioni del docente su `REGOLE-DA-DECIDERE.md`:** l'hook del messaggio fa solo 5 controlli (capitolo 05), il limite è di 8 comandi per turno, e c'è il controllo dei cognomi degli allievi nei commit e nei push del pubblico. Dove i capitoli 01-04 dicono altro, vale il capitolo 05.

Nicola, 28/10/2026: niente più promesse, servono meccanismi. Questi controlli (hook di Claude Code, in `.claude/settings.json`) girano da soli: non dipendono dalla memoria di Claude. Nascono dagli errori di `REGISTRO-ERRORI-CLAUDE.md`.

## 01 I controlli

1. **Promemoria a ogni messaggio** (`promemoria-errori.py`, evento UserPromptSubmit). A ogni messaggio del docente aggiunge per Claude il testo di `.claude/promemoria-errori.md` (10 regole, gli errori che si ripetono di più). Per cambiare le regole si modifica solo quel file, al massimo 12 righe.
2. **Limite dei comandi** (`limite-comandi.py`, evento PreToolUse sui comandi Bash, #132).
   1. Dal 4° comando dello stesso turno il comando viene rifiutato: il lavoro va a un subagente.
   2. Un comando più lungo di 600 caratteri viene rifiutato: il codice va in un file nello scratchpad.
   3. Un turno comincia a ogni messaggio che arriva nella sessione (del docente, programmato o resoconto di un subagente). I comandi dei subagenti non si contano e non si bloccano.
   4. Per TUTTI, anche i subagenti (v1.2): cancellare con rm o git rm una versione in docs/ (PDF, «vN.N», jolly) è rifiutato (01/10 n. 13, #4). Dalla v1.3 anche spostarla o rinominarla con mv o git mv: il 28/10 tre dispense arabe erano sparite da docs/ così (rimesse al loro posto dall'audit).
   5. Per TUTTI: prima di un «git push» del pubblico, i file di docs/ cambiati rispetto a origin/main passano da `controlli_pagine.py` (lingue della classe #49 #82 #119, link al sito della Regione #136, nomi di allievi in chiaro #85, sintassi degli script con node --check #118); se c'è un problema il push è rifiutato con l'elenco.
   6. Per TUTTI: prima di un «git push» del riservato, coda/*.json e comandi/*.json devono leggersi (05/10 n. 12).
   7. Falso allarme dei punti 4-6: si aggiunge al comando il commento «# PAGINE-OK: <motivo>» e lo si dice al docente.
3. **Controllo del messaggio** (`controllo-messaggio.py`, secondo hook di Stop, dopo `versiona-tutto.sh`). Prima che il messaggio resti al docente lo rilegge; se trova un errore, Claude deve riscriverlo:
   1. ordine copia/incolla sbagliato: un riquadro o una seconda copia tra «Ctrl+C» e «Ctrl+V» (#50, #138);
   2. cosa bloccante (firma, scadenza, 14:05, uscita, PC rotto, non compila) non nelle prime 2 righe (#137);
   3. «fatto», «a posto», «funziona», «risolto» senza una prova nello stesso messaggio (ho visto, risulta, PUBBLICATO, PUBLISHED, schermata, controllato, verificato) (#63, #115, #128, #135).
   4. «pubblicat…», «è tutto pronto», «tutto a posto», «è online», «possono cominciare» riferiti a una classe (1INF, 2INF, 3INF, 4INF/4TI) senza la verifica sulla fonte vera: nel riservato deve esserci `dati/verifiche-lezione/<oggi>_<CLASSE>.json`, VERDE e non più vecchio di 15 minuti (#63, #83, #104, #105, #115, #120, #127, #128, #135). Le frasi negate («non è ancora pubblicato») e le parole tra virgolette non contano.
   5. Aggiunti il 28/10/2026 sera (v1.2), dalla `MAPPA-REGOLE-CONTROLLI.md`: (e) link al sito senza «PUBBLICATO» delle ultime modifiche di docs/ (#79; il timbro lo scrive `strumenti/aspetta_pubblicazione.sh`); (f) tempi promessi per ciò che fa lo script, senza piano B (#129 #130); (g) stringa DIDAweb senza «Disciplina» o con voti sotto 40 (#98 #117); (h) «nessuna AI» senza aver visto tutte le finestre (#90); (i) «utente non indicato» (#100); (j) «onestamente», «sinceramente» (#53); (k) catene di coordinate con « · » (#56); (l) «salta al passo», «se è già aperta» (#55); (m) firma ricordata quando `FIRME-REGISTRO-2026-27.md` dice che oggi è tutto firmato (#36 #52 #87 #96); (n) richiesta di registrare un errore senza il numero #NNN (#113); (o) link al riservato senza «personale», script copiato dal riservato (#48); (p) indirizzo diretto del progetto Apps Script (regola 10); (q) più di 30 righe di testo nelle ore di lezione (05/10 n. 6); (r) «non ha consegnato», «non risulta» senza dire dove si è controllato (#83 #95); (s) «ha copiato» come certo (01/10 n. 6); (t) «al tuo avanti» dopo «dammi/fammi» (05/10 n. 21); (u) rimando a riquadri di prima (05/10 n. 31); (v) Ctrl+V in Apps Script senza «automazione-corso.gs» (#51).
   Blocca una volta sola per messaggio (`stop_hook_active`): niente cicli.
4. **Verifica della lezione** (`generatori/verifica_lezione.py`, nel riservato; si lancia a mano, prima di dire «pubblicato»). Un comando per classe:

```
python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py 3INF
```

   1. Manda UN comando al ponte Google (`classroom.compiti` + `classroom.annunci`) e aspetta l'esito, al massimo 12 minuti (git pull ogni 20 secondi): con lo script al ritmo di 1 minuto bastano 1-2 minuti.
   2. Trova il compito del giorno (dalla coda `coda/<giorno>_<CLASSE>_*.json`, altrimenti dalla scadenza o dalla programmazione) e controlla che sia PUBLISHED; DRAFT programmato per più tardi = GIALLO, DRAFT non programmato = ROSSO.
   3. Controlla i link della pagina citati nel testo del compito: richiesta diretta a github.io, e se da qui non si raggiunge, come `aspetta_pubblicazione.sh` (file presente in origin/main e commit dentro un giro «Pages» riuscito). Conta i link dei Moduli Google.
   4. Dalla v1.2 di questo file: se l'annuncio più recente della classe non dice «OGGI…» l'esito è GIALLO (#94).
   5. Scrive `dati/verifiche-lezione/<giorno>_<CLASSE>.json` (ora, esito per pezzo, link), fa commit e push del riservato e stampa una riga sola: «VERDE», «GIALLO: …» o «ROSSO: …». Opzione `--giorno AAAA-MM-GG` per un altro giorno.

5. **Audit notturno delle regole** (`generatori/audit_regole.py`, nel riservato; lo lancia la Chat del giorno, passi in `.claude/passi-notturni.md`). Pagine cambiate negli ultimi 2 giorni (tutti i controlli di `controlli_pagine.py`, anche «arriva tra poco» #129, Modulo con «incolla» #81, foto e telefono #44, link a file che non esistono #84), un compito e un annuncio per classe al giorno (#93 #107), scadenze sulle campanelle (#97), istruzioni impaginate, comandi del ponte fermi, troppo grandi, non archiviati o più di 40 al giorno (#58 #114 #125), versioni cancellate, sezione del giorno in FIRME-REGISTRO (#137). Stampa VERDE o ROSSO con i dettagli in `dati/audit-regole/<giorno>.md`.

```
python3 /home/user/corso-informatica-riservato/generatori/audit_regole.py
```

6. **Passi notturni** (`.claude/passi-notturni.md`): comandi, domande sì/no sulla lezione e promemoria a orario che la Chat del giorno esegue tutti (RIPARTENZA sezione 08). La mappa di quale voce del registro è coperta da quale controllo è `MAPPA-REGOLE-CONTROLLI.md`.
7. **Controllore dei controlli** (`strumenti/controlla_controlli.py`, v1.3): in un colpo dice se i controlli sono vivi (hook registrati nel repository e in /home/user, file degli hook senza errori, attiva-controlli-home.py idempotente, tutte le prove «N/N», passi notturni leggibili, file `stato/notte-<giorno>.json` della notte precedente nel riservato); una riga VERDE o ROSSO per controllo. Lo lancia l'ultimo passo dei passi notturni (sezione 06).

```
python3 /home/user/corso-informatica/strumenti/controlla_controlli.py
```

## 02 Quando valgono

1. Claude Code legge `.claude/settings.json` della cartella da cui **parte** la sessione; le modifiche agli hook si caricano da sole durante la sessione.
2. Se la sessione parte da `/home/user` (e non da `/home/user/corso-informatica`) questi controlli **non valgono**. Per attivarli lì, un comando che stampa «ok»:

```
python3 /home/user/corso-informatica/.claude/hooks/attiva-controlli-home.py
```

## 03 Limiti

1. Sono controlli sulle parole, non sul significato: possono sbagliare in tutte e due le direzioni (un «fatto» detto con altre parole passa; una parola bloccante usata per altro fa riscrivere il messaggio).
2. Non verificano che la prova citata sia vera: controllano solo che ci sia.
3. Non coprono gli errori di contenuto (dati sbagliati, pagine): per quelli resta `CHECKLIST-LEZIONE.md`. Lo stato di Classroom e del sito lo controlla `verifica_lezione.py` (punto 01.4).
4. Se uno script ha un problema, esce senza bloccare: la sessione non si rompe mai.
5. `verifica_lezione.py` non legge il testo del compito da Classroom (lo script v8.4 non lo restituisce): lo prende dalla coda locale che ha creato il compito; un compito creato a mano dal docente risulta GIALLO per i link. Se lo script Google è spento (ritmo spento), dopo 12 minuti l'esito è ROSSO.

## 04 Prove

Script di prova con 28 casi (bloccare e non bloccare), tutti superati il 28/10/2026; provato anche sugli ultimi 80 messaggi veri: ha trovato i due messaggi del 28/10 con l'errore #138.

Prove della v1.2 (28/10/2026 sera), versionate e rilanciabili con un comando di una riga, tutte superate:

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_messaggio.py
```

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_limite.py
```

1. `prova_messaggio.py`: 59 casi sui controlli (e)-(v) e su main (blocca una volta, subagenti liberi, input rotto = uscita 0).
2. `prova_limite.py`: 27 casi dalla v1.3 (versioni, spostamento di versioni con mv e git mv, push del pubblico con cinese, arabo nel solo `<pre>`, Regione, script rotto, nomi in chiaro, «Nome I.», push del riservato con conflitto, limite dei comandi, input rotto).
3. `generatori/prova_audit_regole.py` nel riservato: 11 casi.
4. Sugli ultimi 250 messaggi veri i controlli nuovi (f)-(v) hanno bloccato una sola frase, che la regola vieta («lo fa al prossimo giro, entro 5 minuti»); il controllo (e) dipende dallo stato del repository e non si prova sul passato. Tre falsi allarmi trovati («non hanno consegnato» letto su Classroom, «ha copiato» detto di Windows, «si incolla in Apps Script» senza Ctrl+V) sono stati tolti.

Prove del 28/10/2026 per il controllo 4 dell'hook: 11 casi (senza file, verde recente, verde vecchio di 20 minuti, giallo, stop_hook_active, negazione, nessuna classe, citazione, 4TI, input rotto), tutti come atteso.

## 05 Revisione del 04/11/2026 (decisioni del docente)

### 05.1 Controlli tenuti in `controllo-messaggio.py`

1. (a) ordine del copia e incolla (#50, #138; regola R4).
2. (b) cosa bloccante nelle prime 2 righe: firma, scadenza, 14:05, uscita, PC rotto, non compila e, nuovo, «PUBB n NON riuscito» (#137; R4). Assorbe il vecchio (m): se `FIRME-REGISTRO-2026-27.md` dà tutte le ore di oggi firmate, la firma non conta come bloccante.
3. (d) «pubblicato», «è tutto pronto», «è online», «possono cominciare» per una classe solo con `verifica_lezione.py` VERDE di meno di 15 minuti (R2, R7).
4. (e) link al sito solo dopo «PUBBLICATO» (#79); assorbe il vecchio (o): link al riservato senza la finestra PERSONALE, script copiato dal riservato (#48).
5. (gg) orario scritto quando il docente nomina un'ora della giornata (#159). Ristretto: vale solo se il docente ha davvero parlato di un'ora («prima ora», «3ª ora», «PUBB 2»); «tra 1 ora» e i quiz di Sicurezza non contano.

### 05.2 Controlli tolti da `controllo-messaggio.py`

1. (c) «fatto», «a posto», «funziona» senza prova: unito alla regola R7 e al controllo (d).
2. (f) tempi promessi dallo script senza piano B.
3. (g) stringa DIDAweb senza Disciplina e voti sotto 40.
4. (h) «nessuna AI» senza aver visto tutte le finestre.
5. (i) «utente non indicato».
6. (j) «onestamente», «sinceramente».
7. (k) catene di coordinate con « · ».
8. (l) «salta al passo», «se è già aperta».
9. (m) firma già fatta: assorbito in (b).
10. (n) errore da registrare senza il numero.
11. (o) link al riservato: assorbito in (e).
12. (p) indirizzo diretto del progetto Apps Script.
13. (q) più di 30 righe nelle ore di lezione.
14. (r) «non ha consegnato», «non risulta» senza fonte.
15. (s) «ha copiato» detto come certo.
16. (t) «al tuo avanti» dopo «dammi».
17. (u) rimando a riquadri di prima.
18. (v) incolla in Apps Script senza il file automazione-corso.gs.
19. (w) conteggio senza fonte e ora.
20. (x) attività automatica non provata.
21. (y) pagina provata solo con dati simulati.
22. (z) domanda su presenze o voti già nei file.
23. (aa) release «della cartella».
24. (bb) più di 2 aiutanti accesi.
25. (cc) domanda presa per un ordine di togliere.
26. (dd) genere dato per scontato.
27. (ee) griglia dei voti data in PDF.
28. (ff) più indirizzi ai ragazzi nello stesso messaggio.
29. (hh) «non arrivato» su dati vecchi.
30. (ii) incolla in Apps Script senza clic dentro il codice.
La versione di prima è nella storia di Git (commit precedente al 04/11/2026 sera) e si può rimettere con un `git checkout` del file.

### 05.3 Altri cambi

1. `limite-comandi.py`: da 3 a 8 comandi per turno nella chat principale.
2. Nuovo `controllo_nomi.py` (regola R1): cognomi degli allievi presi dagli elenchi del riservato (`config/*presenti*.json`, `config/*elenco*.json`, `config/nomi-controllo.json`; i nomi propri, che nel pubblico sono ammessi come «Nome I.», non si cercano). Lo usano:
   1. `limite-comandi.py`, su ogni `git commit` del pubblico (testo del comando, heredoc compreso, e file di `-F`) e su ogni `git push` del pubblico (messaggi dei commit da pushare). Non si salta con «PAGINE-OK».
   2. il hook git `commit-msg` del pubblico, installato da `bash strumenti/installa_commit_msg.sh` (vale anche per i commit fatti da altri script).
   3. Falso allarme: la parola si aggiunge a «parole_comuni» in `config/nomi-controllo.json` del riservato.
3. `promemoria-errori.md`: riscritto con le 11 regole nuove.
4. Prove: `prova_messaggio.py` 38 casi, `prova_limite.py` 39 casi, tutti superati il 04/11/2026; il controllo dei cognomi provato anche sugli ultimi 1.200 messaggi di commit veri del pubblico: un solo caso, il cognome finito in un commit del 04/11 mattina (nessun falso allarme).

### 05.4 Da correggere negli strumenti (rilettura delle regole del 06/11/2026, nessuno strumento toccato)

1. `promemoria-errori.md`, riga R5: aggiungere «Allegato A dopo il 30/10 solo togliere: voce più vicina, mai aggiungere; Sicurezza: titoli della direzione» (errore #223).
2. Controllo dei testi del registro: deve dire «voce più vicina», mai «voce da aggiungere» (#223); per la Sicurezza non proporre titoli.
3. `generatori/audit_regole.py` (01.5) segnala più di un compito per classe al giorno, ma R2 e R10.3 prevedono un compito per ora: contare per ora (titolo «G/M Ora N»).
4. `generatori/verifica_lezione.py` (01.4) cerca «il compito del giorno»: con PUBB n va verificato il compito dell'ora n.

## 06 Controllo (ff): formato dei kit e dei documenti (12/11/2026)

Nasce dalla famiglia di errori #282, #285-#289, #291, #293, #309, #311 (registro #312): io non vedo come l'app mostra la risposta, quindi il formato lo controlla l'hook. Sta in `controllo-messaggio.py` (secondo hook di Stop), legge `transcript_path` e guarda i blocchi dell'ULTIMO turno dell'assistente (testo e strumenti in ordine, dall'ultimo messaggio vero del docente; i risultati degli strumenti, le notifiche e il feedback degli hook non sono il docente; i sottoagenti non contano). Il messaggio finale (`last_assistant_message`) si aggiunge se non è ancora nella trascrizione. Regole (dettaglio nella GUIDA-MESSAGGI, sezioni 03sexies-03octies):

1. **R-A, cornice blu:** ogni SendUserFile di `.pdf`, `.docx`, `.xlsx`, `.csv`, `.zip` (le immagini no) ha SUBITO PRIMA un testo che finisce con una riga di quadratini blu 🟦 e una riga che comincia con 📄, e SUBITO DOPO un testo che comincia con una riga 🟦.
2. **R-B, un solo PDF:** se nel turno ci sono righe rosse 🟥🟥, al massimo un PDF per risposta (due: il testo sparisce, #311).
3. **R-C, turno pulito:** se c'è un kit (testo con 🟥🟥 e TITOLO, OGGETTO o un link in riquadro), prima del suo primo blocco non ci sono altri strumenti (Read, Bash, Agent, ecc.; SendUserFile sì). Si risponde in testo semplice, senza colori, e il kit va nel messaggio dopo.
4. **R-D, kit Classroom** (testo con TITOLO e OGGETTO): comincia con una riga rossa 🟥, TITOLO e OGGETTO sono in riquadri di codice, l'ultimo testo (dopo il PDF) finisce con una riga rossa senza altro dopo (righe vuote ammesse).
5. **R-E:** nell'oggetto non compare «lo facciamo quando lo dico io».
6. **R-F, cornice verde:** ogni risposta che non è un kit ha una riga di quadratini verdi 🟩. Eccezioni: comincia con 🔴 o con una riga 🟥/🟦, meno di 60 caratteri, meno di 2 righe.
7. Un errore già segnalato nello stesso turno non si segnala di nuovo (memoria in `corso-controllo-formato-stato.json` nella cartella temporanea; `CORSO_STATO_FORMATO=""` la spegne). Blocca una volta sola per risposta (`stop_hook_active`), come gli altri.
8. **Limiti:** vede i blocchi, NON come l'app li mostra (per esempio il testo prima di una scheda che l'app sostituisce con un riassunto: lo deduce dalle regole); non controlla il contenuto (versione del PDF, ordine dell'ora #286, nomi); se la trascrizione non è ancora scritta o non si legge, controlla solo il messaggio finale e non rompe niente. 85 ms circa a ogni risposta.
9. Prove: `python3 /home/user/corso-informatica/.claude/hooks/prove/prova_formato_kit.py` (55 casi: kit giusti, un caso per ogni errore R-A…R-F, turni vecchi, sottoagenti, notifiche, memoria, processo vero).

## 07 Controllo (hh): «non ha consegnato» senza dato fresco (12/11/2026)

1. **Errore #314:** alle 13:54 ho scritto «ROSSI Mario non ha consegnato» con un dato letto fino alle 13:48:57; la consegna era arrivata alle 13:54:56. La regola R7.1 c'era, ma non c'era uno strumento che guardasse l'età del dato.
2. **Controllo:** `controllo_dato_vecchio` in `controllo-messaggio.py`. Se il messaggio (fuori da riquadri, codice e virgolette) dice «non ha/hanno (ancora) consegnato» o «non ha/hanno (ancora) fatto il quiz»: senza una fonte con ora («letto … alle HH:MM», «dato delle HH:MM», «fino alle HH:MM», «screenshot … alle HH:MM») il messaggio viene fatto riscrivere; con un dato più vecchio di 3 minuti (la fonte più vecchia citata) anche. Passa se c'è «non provato» o se la frase è «non risulta consegnato nel dato delle HH:MM (N minuti fa)».
3. **Prova:** `prove/prova_messaggio.py` (8 casi nuovi, 46 in tutto). Limite: il controllo legge il testo, non sa se la fonte citata è davvero quella letta.

## 08 Controllo dei cognomi nei file del push (12/11/2026)

1. **Errore #319:** un cognome di allievo scritto in `fabbrica/` (esempio nel changelog del motore) è stato pushato: il controllo del push guardava solo docs/ e i messaggi dei commit.
2. **Controllo:** `limite-comandi.py`, al «git push» del pubblico controlla con `controllo_nomi.py` (elenchi del riservato) il contenuto di tutti i file di testo cambiati rispetto a origin/main (e dei nuovi, se il comando ha «git add»), in qualunque cartella; ferma il push e non si salta con «PAGINE-OK». Prova: `prove/prova_limite.py` (42 casi).

## 09 Rilettura del mattino e «codice non in fondo» (17/11/2026)

1. **Errore #350:** modalità già decise cambiate (voti DIDAweb) e codice non in un riquadro in fondo (R4 3ter); il docente chiede di rileggere i documenti ogni mattina.
2. **Rilettura del mattino:** `promemoria-errori.py`, al primo messaggio di ogni giornata (ora di Roma) antepone al promemoria l'obbligo di rileggere CLAUDE.md, GUIDA-MESSAGGI-AL-DOCENTE.md, CHECKLIST-LEZIONE.md e la guida dei segnalibri DIDAweb. Stato: un file per giorno nella cartella temporanea; `CORSO_STATO_RILETTURA=""` la spegne.
3. **Codice non in fondo:** controllo (jj) di `controllo-messaggio.py`, avviso non bloccante se dopo il riquadro ci sono passi numerati. Prova: `prove/prova_messaggio.py` (67 casi).
4. **Limite:** non si sa se la rilettura è avvenuta; il controllo non vede un metodo diverso da quello deciso.

## 10 Rilettura del mattino: INFO-PIU-USATE e COSE-DA-FARE (18/11/2026)

1. `promemoria-errori.py` v1.1: la costante `RILETTURA` ordina anche di leggere, PRIMA di dare passi al docente, `report/INFO-PIU-USATE-v1.0.md` (o l'ultima versione) e, se esiste, il file `report/*/COSE-DA-FARE-<GG-MM di oggi>*.md` del riservato, e di dire in una riga quante cose bloccanti ci sono. Comportamento di prima invariato (una volta al giorno, promemoria a ogni messaggio, uscita 0 su input rotto).
2. Il file lo scrive la sera prima il controllore di fine giornata (trigger delle 17:47, punto 7 del prompt); la preparazione notturna (00:09, punto 5bis) lo legge e riporta «da_fare_oggi» in `stato/notte-<giorno>.json`. Trigger cambiati il 18/11/2026 ~16:40 con `update_trigger`, solo il prompt.
3. Prova: l'hook è stato lanciato con un JSON finto e uno stato temporaneo (`CORSO_STATO_RILETTURA=<file>`): al primo messaggio il testo contiene INFO-PIU-USATE e COSE-DA-FARE, al secondo no; con input rotto esce 0 con il promemoria. `prova_messaggio.py` 67/67 e `prova_limite.py` 42/42 invariate.

## 11 Procedura del mattino (18/11/2026 sera)

1. `promemoria-errori.py` v1.3: al primo messaggio UMANO del giorno, dopo la frase della rilettura (capitoli 09 e 10), aggiunge l'ordine di seguire, PRIMA di rispondere nel merito, `/home/user/corso-informatica-riservato/report/PROCEDURA-MATTINA-<ultima versione>.md`: il percorso è completo e la versione più alta si cerca sul disco (le BOZZE non contano). Se il file manca la frase lo dice.
2. La procedura (riservato) fa rileggere i documenti, gli ultimi 3 giorni e l'orario, scrive `report/<oggi>/PROPOSTE-CLASSROOM-<GG-MM>.md` (2-3 alternative per blocco, senza pubblicare) e dà al docente una sola schermata con una domanda. Solo Read, Grep e Write.
3. Nessun trigger è cambiato (decisione del docente 18/11). La proposta di un trigger alle 06:30, NON applicata, è `report/2026-11-18/PROPOSTA-TRIGGER-MATTINO-v1.0.md` nel riservato.
4. Prova: `prove/prova_promemoria.py` 26/26 (11 casi nuovi con un riservato finto: frase presente, percorso completo, versione 1.10 maggiore di 1.9, bozza ignorata, secondo messaggio e trigger senza frase, file mancante, hook spento); `prova_messaggio.py` 67/67; `prova_limite.py` 42/42.

## 12 Controlli (kk) (ll) (mm): pacchetto PUBB, formato del file, cruscotto di oggi (23/11/2026)

1. **(kk) Pacchetto PUBB** (errore #386): se il docente scrive «PUBB n», «dati per Classroom» o «ridammi … kit» (messaggio breve, al massimo 240 caratteri) e la risposta non ha riga rossa 🟥, TITOLO e OGGETTO in riquadri, blocca una volta per turno e dice che cosa manca. Fa eccezione la risposta breve (sotto 60 caratteri).
2. **(ll) Formato del file** (errore #388): SendUserFile di .xlsx, .docx, .csv, .md, .txt, .pptx, .html senza un PDF dello stesso nome nel turno, se il docente non ha nominato il formato (excel, word, csv, modello, kit, originale, …) e il messaggio non è un kit rosso: blocca e chiede il PDF.
3. **(mm) Cruscotto di oggi** (errore #389): «il cruscotto è pronto/aggiornato/live/in tempo reale» per una classe che oggi ha lezione già iniziata e il cui ultimo dato non è di oggi (ora di Roma), senza «DATI VECCHI», «ultimo dato del …» o «non provato»: blocca. Lo stesso controllo, a cadenza di giorno, è il punto 10 di `controlla_controlli.py`.
4. I testi dei post (errore #387) li controlla `controlla_kit.py` v1.4 nel riservato («KIT INCOERENTE»).
5. Libreria `strumenti/controlli_consegna.py`; prove `prove/prova_consegna.py` (60 casi); `prova_controlla_kit.py` nel riservato (15); la lista delle prove di `controlla_controlli.py` le comprende tutte.

## 13 Controlli rimessi (23/11/2026)

Ordine del docente: «se ci sono errori che tu hai tolto dagli avvertimenti rimettili; se invece li abbiamo risolti va bene così». Il banco `strumenti/banco_errori_v1.1.py` aveva trovato 43 errori «A» senza più controllo (capitolo 05.2) e 96 NON COPERTI. Dettaglio, con il numero di ogni errore, in `MAPPA-REGOLE-CONTROLLI.md` v1.33, sezione 08.

1. **Dove:** `controlli_ripristinati.py` (nuovo, testo del messaggio e del kit), `controllo-messaggio.py` (firma ricordata, controlli sulla trascrizione, nomi), `controllo_nomi.py` (`avviso_nome_solo`), `controlli_pagine.py` (6 controlli nuovi; `quiz_sul_sito` e `copia_file_da_classroom` anche prima del push), `strumenti/controlla_lingue_quiz.py` v1.1. Il codice storico non è più in git: rifatti dalla descrizione del capitolo 05.2 e dai casi del banco, sulle regole R1-R11 di oggi (la regola «la firma non si deduce dal bottone» è abrogata da R5.1).
2. **BLOCCO** (regole bloccanti, il messaggio va riscritto una volta): «a posto/risolto/funziona/garantito/c'è sul sito» senza prova nel messaggio (R7.1, ex (c)); conteggio di consegne senza fonte e ora (ex (w)); «non ha caricato», «non ha fatto niente» da Veyon, «ha già» da uno screenshot, senza la ricerca (ex (r)); pagina provata con ?prova=1 (ex (y)); rimando a «il riquadro di prima» (ex (u)); firma ricordata con FIRME-REGISTRO tutto firmato (ex (m), R5.1); più file senza «a che serve» per ognuno (#373); «alza la mano» nel testo del kit (#177).
3. **AVVISO** (non blocca, `systemMessage`): «nessuna AI», tempi dello script, «utente non indicato», «ha copiato», ROSSO «atteso», release della cartella, «lei/lui», domanda su presenti già nei file, «onestamente», catene « · », «salta al passo», incolla in Apps Script, stringa DIDAweb senza Disciplina o con voti sotto 40, «al tuo avanti» dopo «dammi», registrazione senza #NNN, domanda presa per ordine di togliere, più di 2 Agent nel turno, griglia da compilare in PDF, nome di battesimo da solo.
4. **Pagine** (audit notturno `TUTTI`; solo i primi due anche prima del push, `SICURI`): quiz con invio proprio sul sito, copia di un file da Classroom, carta e penna (solo audit: 13 pagine vecchie lo violano), pannello senza «A che serve:», campi ripetuti nelle tre lingue, ruoli MANI e OCCHI.
5. **Non rimessi** (4): #11, #36, #52 (regola abrogata da R5.1) e 02/10-9 (i PDF ora vanno come Allegato). **Ancora da fare:** #352 e #198 (`controlla_kit.py` e `controlli_consegna.py`, file di altri agenti).
6. **Prove:** `python3 /home/user/corso-informatica/.claude/hooks/prove/prova_controlli_ripristinati.py` (74/74: 73 casi giusti e sbagliati più «0 falsi allarmi» sui 166 messaggi veri di Claude e sui 5 kit del 20/11/2026 della bobina del riservato); `prova_messaggio.py` 67/67, `prova_limite.py` 42/42, `prova_formato_kit.py` 55/55, `prova_consegna.py` 60/60 invariate; il controllore dei controlli la include da solo. Banco: 171 coperti su 414, 0 falsi allarmi.
7. **Limiti:** controlli sulle parole; per la prova basta una qualunque fonte, ora, esito o «non provato» nel messaggio.

## 14 Cancello di consegna (23/11/2026)

Uso: `python3 -I /home/user/corso-informatica-riservato/strumenti/cancello_consegna_v1.0.py KIT.md|POST.json|CARTELLA [--dettagli] [--senza-banco] [--giallo-rosso]`; uscita 0 VERDE, 2 ROSSO; prova `--selftest`. Dettaglio in `MAPPA-REGOLE-CONTROLLI.md` sezione 09.

## 15 Filtro di buon senso (23/11/2026, errore #390)

Obiettivo: far perdere al docente meno tempo con domande inutili ed errori (il docente stima il 50%). Libreria `.claude/hooks/filtro_buon_senso.py`, chiamata da `controllo-messaggio.py` v2.2 a ogni fine risposta: BLOCCA (Claude riscrive il messaggio una volta), e ogni blocco dice in una riga perché e che cosa togliere.

1. **Dato già nei file** (orario, presenti, presenze, firme, data e ora) chiesto al docente: il dato sta nei file o è del giorno corrente o passato.
2. **Modalità assenza:** `config/modalita-assenza.json` nel riservato (inizio 2026-11-23, fine 2026-11-25, lette dal file; `"attiva": false` la spegne). In quei giorni niente domande né elenchi di decisioni, salvo firma, PC rotto, decisione solo sua che scade oggi.
3. **Lunghezza:** oltre 12 righe o 900 caratteri fuori dai riquadri di codice, se il messaggio non è un kit o un pacchetto (cornice rossa o blu, TITOLO e OGGETTO con due riquadri). L'avviso di lunghezza (ii) a 10 righe resta.
4. **Più di una domanda** (R7.6).
5. **Frasi già dette** nel messaggio precedente della stessa conversazione (memoria in `corso-filtro-buon-senso-stato.json` nella cartella temporanea; `CORSO_STATO_BUON_SENSO=""` la spegne) o ripetute due volte nello stesso messaggio.
6. **Elenco di conteggi** senza fonte né ora (R7.1; il blocco dei conteggi di consegne e presenze resta in `controlli_ripristinati.py`).
7. **Conferma chiesta su un ordine già dato** (errore #391, «se te le dico è perché tu le faccia»): se l'ultimo messaggio del docente contiene un ordine, bloccano «vuoi che lo faccia?», «procedo?», «posso procedere», «te lo preparo?», «dimmi se devo…», «fammi sapere quale/se…», «aspetto il tuo ok». Perché: il docente deve ripetere l'ordine. Eccezioni: PUBB n, firma, pubblicazione e Classroom, push e dati non pubblici, azioni distruttive, decisione solo sua con scadenza oggi, «aspetta il via». Senza il testo del docente (trascrizione illeggibile) non scatta.

Un turno senza testo nuovo (notifica) non viene rifiltrato. Prova: `python3 -I /home/user/corso-informatica/.claude/hooks/prove/prova_filtro_buon_senso.py` (102/102, con 0 falsi allarmi sui messaggi brevi e sulle cornici rosse e blu dei 155 messaggi veri del 20/11/2026, ognuno con il suo messaggio del docente; 41 di quei 155 messaggi superavano i limiti di lunghezza). Limiti: controlli sulle parole, non capiscono il significato; il blocco della lunghezza vale anche per un messaggio lungo e utile.

## 16 Traccia degli errori (23/11/2026)

1. `strumenti/traccia_errori_v1.0.py` (riservato) calcola per ogni errore e categoria: data del controllo, episodi prima e dopo, ultima ricorrenza, stato RISOLTO (controllo continuo da almeno 14 giorni e 0 episodi dopo), RICORRE (3 episodi in 14 giorni o 2 dopo il controllo), DA ALZARE DI LIVELLO (ricorre con il controllo attivo, o in gravità 3), NON MISURABILE. Soglie: `config/soglie-errori.json` del riservato (proposta di Claude, modificabili). Non presume le date: senza una data provata del controllo un errore non è mai RISOLTO.
2. Gira da solo ogni fine giornata dentro `strumenti/controlla_controlli.py` (funzione `traccia_errori_fine_giornata`, non blocca mai, scrive `dati/traccia-errori/` nel riservato). Prova: `python3 -I strumenti/prova_controlla_controlli.py` (48/48 il 23/11/2026).

## Changelog

1. v1.2 (28/10/2026 sera): controlli (e)-(v) dell'hook del messaggio, controlli prima del push, audit notturno.
2. v1.3 (28/10/2026, audit): mv e git mv di una versione in docs/ rifiutati (4 prove nuove, 27 in tutto); controllore dei controlli `strumenti/controlla_controlli.py` (punto 01.7); punti di 03 rimessi in ordine; tolta una frase ripetuta in 04.4.
3. v1.4 (04/11/2026): capitolo 05, revisione sulle decisioni del docente (5 controlli nell'hook del messaggio, controllo dei cognomi nei commit del pubblico, 8 comandi per turno, elenco dei controlli tolti).
4. v1.5 (06/11/2026): capitolo 05.4, punti da correggere negli strumenti emersi dalla rilettura delle regole.
5. v1.6 (12/11/2026): capitolo 06, controllo (ff) del formato dei kit e dei documenti; prova nuova `prova_formato_kit.py`.
6. v1.7 (12/11/2026): capitolo 07, controllo (hh) «non ha consegnato» con dato non fresco (errore #314); prova_messaggio.py a 46 casi.
7. v1.8 (12/11/2026): capitolo 08, controllo dei cognomi nel contenuto dei file cambiati al push del pubblico (errore #319); prova_limite.py a 42 casi.
9. v1.9 (17/11/2026): capitolo 09, rilettura del mattino e controllo (jj) «codice non in fondo» (errore #350); prova_messaggio.py a 67 casi.
10. v1.10 (18/11/2026): capitolo 10, rilettura del mattino con INFO-PIU-USATE e COSE-DA-FARE del giorno (audit del meccanismo sera/mattino, richiesta del docente).
11. v1.11 (18/11/2026): `promemoria-errori.py` v1.2: il segnale «primo messaggio del giorno» lo consuma solo un messaggio del docente, non i prompt di trigger/routine (segni: `<task-notification>`, «scheduled trigger», «Fired by routine», prefissi PROMEMORIA / Controllo di fine giornata / Preparazione notturna); file BOZZA esclusi, versione più alta; percorso completo di `didaweb-auto.js`. Prova nuova `prove/prova_promemoria.py` (15 casi); prova_messaggio 67/67 e prova_limite 42/42 invariate (audit del metodo sera/mattina, residui R2, R6, R8).
12. v1.12 (18/11/2026 sera): `strumenti/controlla_controlli.py` (punto 5, la notte): dal 19/11 lo stato `stato/notte-<giorno>.json` deve avere anche il campo `da_fare_oggi` (punto 5bis della preparazione notturna), altrimenti ROSSO (residuo R1 dell'audit del metodo sera/mattina). Prove di `prova_controlla_controlli.py`: 44/44. Non provato con una notte reale (la prima è quella del 19/11).
13. v1.13 (18/11/2026 sera): capitolo 11, `promemoria-errori.py` v1.3 (frase della procedura del mattino) e 11 prove nuove in `prova_promemoria.py` (26 casi).
14. v1.14 (23/11/2026): capitolo 12, controlli (kk) (ll) (mm) dell'hook del messaggio per gli errori #386, #388, #389; `controlla_kit.py` v1.4 per #387; prova_consegna.py (60 casi).
15. v1.15 (23/11/2026): capitolo 13, controlli rimessi (47) e risolti altrove (4); `controlli_ripristinati.py`, prova `prova_controlli_ripristinati.py`.
16. v1.16 (23/11/2026): capitolo 14, cancello di consegna.
17. v1.17 (23/11/2026): capitolo 15, filtro di buon senso (errore #390), obiettivo principale in testa; prova nuova `prova_filtro_buon_senso.py`.
18. v1.18 (23/11/2026): capitolo 15, controllo 7 (errore #391); `controllo-messaggio.py` v2.3, `filtro_buon_senso.py` v1.1, prova 102/102.
19. v1.19 (23/11/2026): capitolo 16, traccia degli errori (`traccia_errori_v1.0.py`, soglie `config/soglie-errori.json`), lanciata dal controllore di fine giornata.

## 17 I hook sono vivi? (24/11/2026, errore #392)

1. La sessione cloud parte da `/home/user`: Claude Code legge i hook da `/home/user/.claude/settings.json`, NON da `corso-informatica/.claude/settings.json`. Quel file si perde quando il contenitore viene rifatto (hookCount 3 il 20/11 fino alle 12:53, poi 1: solo il hook di sistema).
2. Rimetterlo: `python3 /home/user/corso-informatica/.claude/hooks/attiva-controlli-home.py` (si carica da solo, senza riavvio: provato, il primo Bash dopo ha fatto partire `limite-comandi.py`).
3. Battito: ogni partenza di un hook scrive una riga in `/tmp/corso-hook-vivi.log` (ora, hook, cwd, CLAUDE_PROJECT_DIR). Per sapere se girano: `tail /tmp/corso-hook-vivi.log`. Nel transcript, `stop_hook_summary.hookCount` deve essere 3 e non 1.
4. Limite: lo script di avvio dell'ambiente (non provato) renderebbe la cosa permanente; serve il docente.
