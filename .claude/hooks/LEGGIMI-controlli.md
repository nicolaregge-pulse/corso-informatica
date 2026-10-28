# 00 Controlli automatici contro gli errori ripetuti

**Versione 1.3** — 28/10/2026 — documento interno del docente e di Claude

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

## Changelog

1. v1.2 (28/10/2026 sera): controlli (e)-(v) dell'hook del messaggio, controlli prima del push, audit notturno.
2. v1.3 (28/10/2026, audit): mv e git mv di una versione in docs/ rifiutati (4 prove nuove, 27 in tutto); controllore dei controlli `strumenti/controlla_controlli.py` (punto 01.7); punti di 03 rimessi in ordine; tolta una frase ripetuta in 04.4.
