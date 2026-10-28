# 00 Controlli automatici contro gli errori ripetuti

**Versione 1.1** — 28/10/2026 — documento interno del docente e di Claude

Nicola, 28/10/2026: niente più promesse, servono meccanismi. Questi controlli (hook di Claude Code, in `.claude/settings.json`) girano da soli: non dipendono dalla memoria di Claude. Nascono dagli errori di `REGISTRO-ERRORI-CLAUDE.md`.

## 01 I controlli

1. **Promemoria a ogni messaggio** (`promemoria-errori.py`, evento UserPromptSubmit). A ogni messaggio del docente aggiunge per Claude il testo di `.claude/promemoria-errori.md` (10 regole, gli errori che si ripetono di più). Per cambiare le regole si modifica solo quel file, al massimo 12 righe.
2. **Limite dei comandi** (`limite-comandi.py`, evento PreToolUse sui comandi Bash, #132).
   1. Dal 4° comando dello stesso turno il comando viene rifiutato: il lavoro va a un subagente.
   2. Un comando più lungo di 600 caratteri viene rifiutato: il codice va in un file nello scratchpad.
   3. Un turno comincia a ogni messaggio che arriva nella sessione (del docente, programmato o resoconto di un subagente). I comandi dei subagenti non si contano e non si bloccano.
3. **Controllo del messaggio** (`controllo-messaggio.py`, secondo hook di Stop, dopo `versiona-tutto.sh`). Prima che il messaggio resti al docente lo rilegge; se trova un errore, Claude deve riscriverlo:
   1. ordine copia/incolla sbagliato: un riquadro o una seconda copia tra «Ctrl+C» e «Ctrl+V» (#50, #138);
   2. cosa bloccante (firma, scadenza, 14:05, uscita, PC rotto, non compila) non nelle prime 2 righe (#137);
   3. «fatto», «a posto», «funziona», «risolto» senza una prova nello stesso messaggio (ho visto, risulta, PUBBLICATO, PUBLISHED, schermata, controllato, verificato) (#63, #115, #128, #135).
   4. «pubblicat…», «è tutto pronto», «tutto a posto», «è online», «possono cominciare» riferiti a una classe (1INF, 2INF, 3INF, 4INF/4TI) senza la verifica sulla fonte vera: nel riservato deve esserci `dati/verifiche-lezione/<oggi>_<CLASSE>.json`, VERDE e non più vecchio di 15 minuti (#63, #83, #104, #105, #115, #120, #127, #128, #135). Le frasi negate («non è ancora pubblicato») e le parole tra virgolette non contano.
   Blocca una volta sola per messaggio (`stop_hook_active`): niente cicli.
4. **Verifica della lezione** (`generatori/verifica_lezione.py`, nel riservato; si lancia a mano, prima di dire «pubblicato»). Un comando per classe:

```
python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py 3INF
```

   1. Manda UN comando al ponte Google (`classroom.compiti` + `classroom.annunci`) e aspetta l'esito, al massimo 12 minuti (git pull ogni 20 secondi): con lo script al ritmo di 1 minuto bastano 1-2 minuti.
   2. Trova il compito del giorno (dalla coda `coda/<giorno>_<CLASSE>_*.json`, altrimenti dalla scadenza o dalla programmazione) e controlla che sia PUBLISHED; DRAFT programmato per più tardi = GIALLO, DRAFT non programmato = ROSSO.
   3. Controlla i link della pagina citati nel testo del compito: richiesta diretta a github.io, e se da qui non si raggiunge, come `aspetta_pubblicazione.sh` (file presente in origin/main e commit dentro un giro «Pages» riuscito). Conta i link dei Moduli Google.
   4. Scrive `dati/verifiche-lezione/<giorno>_<CLASSE>.json` (ora, esito per pezzo, link), fa commit e push del riservato e stampa una riga sola: «VERDE», «GIALLO: …» o «ROSSO: …». Opzione `--giorno AAAA-MM-GG` per un altro giorno.

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
5. `verifica_lezione.py` non legge il testo del compito da Classroom (lo script v8.4 non lo restituisce): lo prende dalla coda locale che ha creato il compito; un compito creato a mano dal docente risulta GIALLO per i link. Se lo script Google è spento (ritmo spento), dopo 12 minuti l'esito è ROSSO.
4. Se uno script ha un problema, esce senza bloccare: la sessione non si rompe mai.

## 04 Prove

Script di prova con 28 casi (bloccare e non bloccare), tutti superati il 28/10/2026; provato anche sugli ultimi 80 messaggi veri: ha trovato i due messaggi del 28/10 con l'errore #138.

Prove del 28/10/2026 per il controllo 4 dell'hook: 11 casi (senza file, verde recente, verde vecchio di 20 minuti, giallo, stop_hook_active, negazione, nessuna classe, citazione, 4TI, input rotto), tutti come atteso.
