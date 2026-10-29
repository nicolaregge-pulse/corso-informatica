# Cronaca dal 28/10 ore 14:00 al 29/10 ore 12:15

**Versione 1.0** — 29/10/2026 — documento interno del docente, senza nomi di allievi

Fonti: i commit dei due repository (gli orari del repository pubblico sono in UTC e qui sono riportati con un'ora in più, cioè in ora di Roma), le bobine del 28/10 e del 29/10 (messaggi del docente e risposte di Claude), il registro degli errori dal #125 al #146, `orario/da-fare-2026-10-29.md`, `FIRME-REGISTRO-2026-27.md` e l'audit `audit/20261029_Audit-28-29-ottobre_v1.0.md`. Il numero tra parentesi, per esempio (#141), è la voce del registro degli errori.

## 01 Mercoledì 28/10 pomeriggio

1. **Che cosa ha chiesto il docente.**
   1.1. Alle 14:29: controllare tutto, il registro degli errori, la lista delle cose da fare e la velocità dello script; «una cosa per volta».
   1.2. Alle 14:33-14:35: «se fai così io mi perdo la cosa»; le ore erano già tutte firmate; creare un file con la situazione delle firme da guardare prima di chiedere.
   1.3. Dalle 15:28: risolvere gli errori che si ripetono, meno righe inutili in chat, una chat nuova da sola alle 0:00 che rilegga tutte le regole.
   1.4. Dalle 16:36: il modo di lavorare nuovo. Alle 0:00 la valutazione delle 2 settimane e 3 proposte per classe; prima delle 8 la scelta e la pubblicazione senza scadenza; il cruscotto dice che cosa fa ogni ragazzo, anche ai ragazzi; un report PDF per ogni ora; le tre modalità di lavoro; «nel cruscotto dobbiamo mettere tutto», a linguette, con le domande dei ragazzi a Claude.
2. **Che cosa ha fatto Claude.**
   2.1. Dalle 14:31 alle 14:49: registro degli errori #135, #136, #137 e #138; script v8.4 con la leva del ritmo dal cruscotto (14:42); file della situazione firme (14:35); dispensa di Sicurezza della 2INF senza il link alla Regione (14:36); guida Eclipse della 3INF v1.1 (14:38); dispense arabe della 1INF rifatte con il font Amiri (14:44).
   2.2. Dalle 15:39 alle 16:31: controlli automatici (hook) contro gli errori ripetuti; regola 25 (niente output lungo); mappa che lega ogni voce del registro a un controllo, con 18 controlli nuovi.
   2.3. Dalle 16:37 alle 16:40: regole 26, 27, 28 e 29 e il report PDF di ogni ora scritti in `CLAUDE.md`.
   2.4. Dalle 16:49 alle 17:37: cruscotto unico a linguette (piano del giorno, chiedi aiuto, domande con priorità, scrivi a Claude, uscite, riepilogo di 2 settimane); un audit che ha rimesso tre dispense arabe sparite; il «controllore del controllore» `strumenti/controlla_controlli.py`; nomi completi tolti dal pubblico.
3. **Che cosa è andato bene.** Le regole nuove sono state scritte tutte e subito; le dispense sparite sono state ritrovate; il cruscotto a linguette è nato in poco più di un'ora.
4. **Che cosa no.**
   4.1. Il controllo della firma della 3INF è arrivato alle 14:33, dentro un messaggio lungo, quando le 14:05 erano passate (#137).
   4.2. La sequenza di copia e incolla per lo script v8.4 cancellava gli appunti: lo stesso errore del #50 (#138).
   4.3. La chat è rimasta piena di righe automatiche sugli aiutanti; il docente alle 15:42: «riscrivimi solo le cose per me» (#132).

## 02 Mercoledì 28/10 sera e notte

1. **Che cosa ha chiesto il docente.**
   1.1. Alle 18:41: un riepilogo sintetico. Alle 18:47: le domande dei ragazzi valgono solo in giornata.
   1.2. Alle 21:45-21:47: lasciare i nomi e i link dei ragazzi nelle pagine, perché servono per trovare le cose giuste.
2. **Che cosa ha fatto Claude.**
   2.1. Alle 20:12, 20:31 e 21:00: cognomi e nomi utente tolti dal pubblico, RIPARTENZA v1.4 con la chat del giorno a mezzanotte, regola 27 con il compito senza scadenza.
   2.2. Alle 21:54: i link GitHub dei ragazzi rimessi nelle pagine.
   2.3. Dalle 0:00 alle 6:20: la chat notturna avrebbe dovuto preparare tutto da sola.
3. **Che cosa è andato bene.** La regola sulle domande è stata applicata la sera stessa.
4. **Che cosa no.**
   4.1. Cognomi e link tolti tre volte e rimessi alle 21:54: lavoro deciso senza chiedere quale informazione serviva al docente.
   4.2. La chat di mezzanotte si è fermata dopo un minuto: partiva senza il repository riservato e veniva bloccata dal limite dei comandi. Non c'era nessuna prova di una notte intera prima di prometterla (#139, #141).

## 03 Giovedì 29/10 prima delle lezioni

1. **Che cosa ha chiesto il docente.**
   1.1. Alle 6:17: un audit e il link del cruscotto. Alle 6:20: «non c'è un solo piano del giorno», manca la quarta.
   1.2. Alle 6:29: tre alternative per classe, la scelta con un segno, la pubblicazione al suo «pubblica». Alle 6:31 (PPP): aggiornare tutti i libri PDF.
   1.3. Alle 8:00-8:02: audit e cruscotto con le proposte; «ho 3 ore con la seconda e non c'è niente»; «non c'è la casella per dire scelgo questo e il bottone pubblica».
2. **Che cosa ha fatto Claude.**
   2.1. Dalle 6:24 alle 6:51: controllo della notte (#139), la quarta (4TI) nel cruscotto e nelle prossime lezioni, piano del giorno con le proposte per 2INF, 3INF e 1INF, bottone «Scelgo questa», libri di testo totali e 66 parziali, proposte della 4TI per il 3/11.
   2.2. Alle 8:07: bottoni «Scelgo questa» e «Pubblica» sempre visibili, con la barra ferma in alto.
3. **Che cosa è andato bene.** Le proposte e i libri di testo erano pronti prima delle 7.
4. **Che cosa no.**
   4.1. L'audit delle 6:18 ha detto «a posto» con un ROSSO spiegato come «atteso» (#139).
   4.2. Il bottone «Scelgo questa» era stato provato solo su un server locale: sul sito vero il docente non lo vedeva (#140).
   4.3. Alle 8:00 la 2INF era in aula con Classroom vuoto; la regola delle 6:29 non aveva un caso di riserva per la campanella (#141).

## 04 2INF 8-11

1. **Che cosa ha chiesto il docente.**
   1.1. Alle 8:07-8:10: proposta 3; una scheda PDF sui tipi di file di Lazarus; un percorso guidato per la calcolatrice con 2 caselle, i bottoni + e x e il commit su GitHub; un percorso più facile se nessuno fa il commit; «adesso pubblica».
   1.2. Alle 8:27: «stiamo lavorando da ieri pomeriggio, mi hai garantito il flusso ma non è cambiato niente».
   1.3. Dalle 9:13 alle 10:07: la release v1.0 e poi la v1.2 della calcolatrice, fatte dal docente passo passo; alle 9:53, 10:05 e 10:20: chi ha fatto la v1 e la v2 con il codice giusto?
   1.4. Dalle 10:40 alle 10:43: release solo della calcolatrice; decisione «lasciamo le cose come stanno», un progetto serio avrà un repository nuovo.
2. **Che cosa ha fatto Claude.**
   2.1. Scheda «I file di un progetto Lazarus» v1.0, MD e PDF, alle 8:10. Percorso guidato della calcolatrice (completo, facile, facilissimo) alle 8:15. Documento della lezione v1.0 alle 8:26.
   2.2. Compito pubblicato su Classroom alle 8:26; verifica della lezione VERDE alle 8:47.
   2.3. Regola 30 e bottone rosso «Serve te (N)» alle 8:18; regola 27 allineata (si pubblica senza aspettare) e comando PUBB alle 8:35-8:36; script v8.5 con i compiti senza scadenza alle 9:08.
   2.4. Cruscotto della 2INF rigenerato circa ogni 5 minuti dalle 8:10 alle 11:05; risposte dell'assistente alle 8:47, 9:20 e 10:46.
   2.5. Percorso «La calcolatrice v1.2: meno e diviso» alle 9:37, sul sito alle 9:38, link nel compito dopo il PUBB delle 9:39.
   2.6. Pagina dei repository della 2INF alle 10:13; tabella per allievo (versione 1, versione 2, codice, release, Documento) data in chat verso le 10:25.
   2.7. Firme: ora della prima firma corretta da 8:55 a 8:17 (8:20); tutte e 6 le ore firmate entro le 10:45, `FIRME-REGISTRO-2026-27.md` aggiornato alle 10:46; bottone rosso vuoto alle 10:47.
3. **Che cosa è andato bene.** Scheda e percorso pronti pochi minuti dopo la richiesta; il docente ha fatto da solo le release v1.0 e v1.2; il primo invio vero dal bottone del cruscotto è arrivato a Claude alle 10:33; la verifica finale della 2INF, ROSSA alle 10:47 per il ponte, è tornata VERDE alle 10:57.
4. **Che cosa no.**
   4.1. Compito uscito alle 8:26, 16 minuti dopo il «pubblica»; il docente alle 8:28: «ti ho già detto di non aspettare» (#141).
   4.2. Alle 8:33 il cruscotto aveva le colonne della proposta sbagliata e nessun allievo (#141, ripete #133).
   4.3. Il cruscotto non rispondeva alla domanda vera del docente; i KPI del giorno non erano stati concordati all'inizio; alle 10:25: «oggi il tuo cruscotto è stato poco utile» (#142).
   4.4. Il controllo di GitHub ha dato «sì» falsi: file vuoti, commit del giorno prima, cartelle senza i file del progetto (#142, ripete #134).
   4.5. Versioni confuse: Claude ha indicato «v2.0» quando il docente voleva la 1.2; il percorso ha cambiato nome tre volte; non era stato detto prima che una release vale per tutto il repository.
   4.6. Alle 10:26 il limite di utilizzo: troppi aiutanti accesi insieme, fino a 6-7, due sullo stesso lavoro (#143).

## 05 3INF dalle 11

1. **Che cosa ha chiesto il docente.**
   1.1. Alle 8:13: finire il lavoro del giorno prima e un Documento guidato, valutato, sul confronto tra Eclipse e Java e Lazarus e Object Pascal.
   1.2. Dalle 11:18 alle 11:39: «come mai tutti questi errori?»; perché il piano mostra ancora «Pubblica»; un ragazzo non sa che cosa fare; il migliore della classe risulta a 40; le domande dei ragazzi non si vedono nel cruscotto; «dimmi cosa fare da 0».
   1.3. Alle 11:56-12:01: la situazione di Java dei ragazzi; «per la seconda volta di fila un percorso non controllabile»; un riepilogo del lavoro fatto.
2. **Che cosa ha fatto Claude.**
   2.1. Percorso «Lazarus e Java a confronto» e Documento della lezione v1.0 alle 8:25; compito pubblicato alle 8:36-8:37; verifica VERDE alle 8:47 e alle 10:37.
   2.2. Alle 11:26-11:36: registro #143, #144 e #145; piano del giorno senza bottoni dopo la pubblicazione; domande dei ragazzi rigenerate (erano ferme al 28/10 alle 18:47); «voto dopo la consegna» al posto del voto quando manca la consegna.
   2.3. Alle 11:45: percorso facilitato per tutti, perché meno di metà della classe era oltre Eclipse.
   2.4. Alle 11:57: registro #146; alle 12:00: cruscotto senza «null» e con i PC presi da Veyon.
3. **Che cosa è andato bene.** Dopo il percorso facilitato le consegne sono arrivate: dalle 11:21 alle 12:01 più di 30 invii. Le domande all'assistente hanno avuto risposta.
4. **Che cosa no.**
   4.1. Il percorso partiva solo con nome e PC: alle 11:20 nessun «Fatto»; il passo 2 chiedeva una «linguetta» che i ragazzi non trovavano; alle 11:45 solo 5 su 21 erano oltre Eclipse (#146, seconda volta di fila).
   4.2. Il cruscotto mostrava «null», PC sbagliati, 40 a chi non aveva consegnato e ore del mattino sbagliate (#146).
   4.3. Il piano del giorno mostrava ancora «Scelgo questa» e «Pubblica» dopo l'uscita su Classroom; molti «risolto» del giorno non erano risolti sul sito vero (#144).
   4.4. La scheda delle domande dei ragazzi era ferma alla sera prima: il docente non vedeva le domande di oggi (#145).

## 06 Che cosa resta aperto

1. **1INF 13-14.** La seconda ora di Sicurezza è pubblicata con verifica VERDE; il quiz e il recupero della prima ora si controllano durante l'ora.
2. **3INF.** Le consegne del Documento si leggono e si confrontano con il cruscotto prima di proporre i voti; i voti si danno in fila in chat, uno per riga.
3. **Controllo sul sito vero (#144).** A fine giornata si riapre, in modalità Docente, ogni cosa detta «sistemata» oggi.
4. **Cruscotto (#142, #145, #146).** KPI concordati alle 8:00 e colonne costruite su quelli; ogni linguetta con l'ora di aggiornamento, in rosso se è di un altro giorno; il «sì» di GitHub solo dopo aver letto il file di oggi.
5. **Notte del 30/10 (#139, #141).** Preparazione nella sessione con i due repository; compito della proposta consigliata pronto alle 7:45; se alle 7:55 non c'è la scelta si pubblica quella.
6. **Aiutanti (#143).** Durante la lezione al massimo 2 aiutanti accesi insieme.
7. **Lavori parcheggiati.** Foto della lavagna nella teoria; un PDF per ogni lezione nel libro; piano B per ogni operazione; revisione di PRI e PRI+; casella del voto del docente nel cruscotto.
