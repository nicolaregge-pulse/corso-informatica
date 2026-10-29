# Il cruscotto della lezione: idea, errori, che cosa ha funzionato

**Versione 1.0** — giovedì 29/10/2026, ore 12:10. Documento interno del docente e di Claude, senza nomi di allievi. Va letto insieme a `audit/20261029_Audit-28-29-ottobre_v1.0.md` e al registro degli errori `REGISTRO-ERRORI-CLAUDE.md` (voci da #140 a #146).

## 01 L'idea del cruscotto

1. **Lo scopo**, chiesto dal docente: tenere sotto controllo che cosa fa ogni allievo durante la lezione, senza che il docente debba aprire dieci pagine. In classe il docente fa gli screenshot di Veyon, aiuta chi è bloccato e decide; il resto lo prepara e lo controlla Claude (regole 14, 18, 28, 29 e 30 di CLAUDE.md).
2. **Una sola pagina**, `docs/cruscotto/`, con le classi del giorno e una riga per ogni presente:
   1. a che punto è del lavoro del giorno (percorso guidato, teoria, quiz, repository su GitHub);
   2. che cosa ha consegnato su Classroom e che cosa c'è dentro;
   3. da quanto è fermo, che cosa mostra Veyon (fuori compito in rosso), uscite e note;
   4. il voto proposto 40-80 con il conto, che decide il docente.
3. **Le schede di servizio**: «Piano del giorno» (3 proposte per classe, bottoni «Scelgo questa» e «Pubblica»), «Serve te» (solo le cose che richiedono il docente: firme, presenze, PC rotti, decisioni), «Domande dei ragazzi» (le domande all'assistente con la risposta), «Script e ponte» (stato del collegamento Classroom-GitHub).
4. **Il flusso promesso il 28/10**: di notte una chat prepara le proposte; al mattino il docente sceglie con un bottone; Claude pubblica da solo su Classroom; durante la lezione i giri automatici aggiornano il cruscotto ogni pochi minuti; alla fine i voti per DIDAweb sono già pronti.
5. **La versione per i ragazzi**: la stessa informazione, senza note riservate e con Nome e iniziale, perché ognuno si regoli da solo (regola AUTOREGOLAZIONE).

## 02 Che cosa ho cercato di fare il 28 e il 29/10

1. Riscritto il cruscotto in una pagina unica con tutte le classi, la barra in alto ferma, le modalità Docente e Allievo.
2. Aggiunto i bottoni «Scelgo questa», «Pubblica» e «Serve te», che mandano un messaggio a Claude attraverso lo script di Classroom.
3. Costruito per la 2INF il controllo automatico dei repository GitHub (versione 1, versione 2, codice, release) e la pagina con i link ai repository di tutti.
4. Costruito per la 3INF il percorso «Lazarus e Java a confronto» a passi con «Fatto», più un percorso facilitato, e il cruscotto che legge i «Fatto».
5. Acceso fino a 6-7 aiutanti in parallelo: un giro per classe, il piano, l'ascolto dei bottoni, l'audit, controlli singoli.
6. Messo controlli automatici sui messaggi di Claude (niente «pubblicato» senza prova, niente link prima della pubblicazione).

## 03 Che cosa NON ha funzionato

1. **Il flusso della notte** non è partito: la chat di mezzanotte si è fermata dopo un minuto, le proposte sono state fatte all'alba a mano (#141).
2. **I bottoni «Scelgo questa» e «Pubblica»** alle 8:00 non si vedevano sul sito vero: erano stati provati solo su una copia locale (#140). La 2INF è entrata in aula con Classroom vuoto.
3. **Il cruscotto della 2INF** alle 8:30 mostrava le colonne di un'altra lezione e nessun allievo. Il controllo dei repository ha dato dei «sì» falsi: file vuoti, commit di ieri, cartelle senza i file del progetto. La tabella che serviva al docente (versione 1, codice, versione 2, codice, release, Documento) è arrivata solo in chat verso le 10:25 (#142).
4. **Il «Piano del giorno»** ha continuato a mostrare «Scelgo questa» e «Pubblica» anche dopo la pubblicazione (#144).
5. **La scheda «Domande dei ragazzi»** era ferma alle 18:47 del giorno prima: il docente non vedeva le domande di oggi (#145).
6. **Il riquadro del ponte** mostrava il giorno prima, con errori che non erano più veri.
7. **Il percorso della 3INF**, per il secondo giorno di fila, non ha dato il controllo della classe (#146):
   1. il «Fatto» partiva solo con nome e PC scritti in alto;
   2. un passo chiedeva una «linguetta» che i ragazzi non trovavano;
   3. non prevedeva l'errore di Eclipse più comune (package e module-info);
   4. nel cruscotto sono comparsi «null», PC sbagliati, 40 a chi non aveva ancora consegnato, ore sbagliate.
8. **Troppi aiutanti**: hanno consumato il limite di utilizzo alle 10:26, due facevano lo stesso lavoro, e la qualità non è migliorata (#143).
9. **Le consegne su Classroom** (il Documento) non sono state lette durante la lezione: la colonna è rimasta «da leggere».

## 04 Le cause, dette senza giri di parole

1. **Ho dichiarato funzionante quello che avevo provato solo in locale**, non sul sito vero, non con i dati veri, non come lo vede il docente in classe.
2. **Ho costruito molto e provato poco**: ogni giorno strumenti nuovi, nessuno portato fino in fondo e provato da capo prima della campanella.
3. **Il cruscotto mostra quello che è facile misurare, non quello che serve al docente.** Il docente vuole sapere, per ogni allievo, se il lavoro c'è e se è giusto. I «Fatto» dichiarati dai ragazzi non lo dicono; il file vero su GitHub o il Documento su Classroom sì.
4. **Ogni scheda dipende da un giro che qualcuno deve ricordarsi di lanciare**: quando il giro si ferma, la scheda resta vecchia e non lo dice.
5. **Ho messo più aiutanti invece di più controllo**: più rumore, più token, meno qualità.

## 05 Che cosa ha funzionato, con la prova

1. **Compiti su Classroom delle 3 classi**: usciti tra le 8:26 e le 8:57, con `verifica_lezione.py` VERDE (2INF ricontrollata VERDE alle 11:05).
2. **Il primo invio vero dai bottoni del cruscotto**: «Pubblica» della 1INF alle 10:31 e della 3INF alle 10:33, arrivati nel repository riservato. «Mandate» di «Serve te» alle 11:18.
3. **Firme**: tutte e 6 le ore di oggi firmate entro le 10:45.
4. **2INF**: 15 allievi su 18 con la prima versione della calcolatrice su GitHub, 7 con la seconda. La pagina con i link ai repository di tutti e la tabella Ver1, Codice V1, Ver2, Codice V2, Release, Voto (pubblicata, ma arrivata tardi).
5. **Materiali consegnati al docente**: scheda PDF sui file di Lazarus, scheda della calcolatrice con la foto della lavagna, quiz della 1INF su Moduli.
6. **Il docente ha fatto da solo l'esercizio con le release v1.0 e v1.2**, guidato passo passo.
7. **Le risposte dell'assistente alle domande dei ragazzi** (2INF e 3INF): date nella pagina dei ragazzi.

## 06 Che cosa cambierei, in ordine

1. **Meno cose, provate da capo**: un solo strumento per lezione, provato il giorno prima sul sito vero e sul PC della scuola, come farebbe un ragazzo.
2. **Il cruscotto parte dalla prova vera**: il file su GitHub di oggi letto davvero, il Documento consegnato su Classroom letto davvero. I «Fatto» dichiarati servono solo come indicazione.
3. **I KPI del giorno si concordano alle 8:00** e il cruscotto mostra per prime quelle colonne (regola 13).
4. **Ogni scheda scrive l'ora del dato** e, se il dato è vecchio, lo dice in rosso.
5. **Al massimo 2 aiutanti** durante la lezione (#143).
6. **Piano B scritto prima**: se a 20 minuti dall'inizio meno di metà classe è avanti, si passa a una sola consegna semplice su Classroom, come ha fatto il docente alle 11:59 nella 3INF.
7. **Nessun «risolto» senza averlo visto** sulla pagina che vede il docente (#144).
