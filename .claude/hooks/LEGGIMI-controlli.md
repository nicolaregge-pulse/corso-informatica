# 00 Controlli automatici contro gli errori ripetuti

**Versione 1.7** — 12/11/2026 — documento interno del docente e di Claude

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

## Changelog

1. v1.2 (28/10/2026 sera): controlli (e)-(v) dell'hook del messaggio, controlli prima del push, audit notturno.
2. v1.3 (28/10/2026, audit): mv e git mv di una versione in docs/ rifiutati (4 prove nuove, 27 in tutto); controllore dei controlli `strumenti/controlla_controlli.py` (punto 01.7); punti di 03 rimessi in ordine; tolta una frase ripetuta in 04.4.
3. v1.4 (04/11/2026): capitolo 05, revisione sulle decisioni del docente (5 controlli nell'hook del messaggio, controllo dei cognomi nei commit del pubblico, 8 comandi per turno, elenco dei controlli tolti).
4. v1.5 (06/11/2026): capitolo 05.4, punti da correggere negli strumenti emersi dalla rilettura delle regole.
5. v1.6 (12/11/2026): capitolo 06, controllo (ff) del formato dei kit e dei documenti; prova nuova `prova_formato_kit.py`.
6. v1.7 (12/11/2026): capitolo 07, controllo (hh) «non ha consegnato» con dato non fresco (errore #314); prova_messaggio.py a 46 casi.
