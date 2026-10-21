# 00 Il cruscotto dal vivo del docente

**Versione 1.1** — 21/10/2026 · Area Docente · Il laboratorio di informatica secondo le idee di Nicola Regge

*Il framework nato e provato in classe con la 3INF il 19/10/2026 (lezione «Il mio sito diventa il mio portfolio», 18 allievi, 8:00-10:50). Una sola pagina dice al docente, per ogni allievo, che cosa sta facendo, che cosa ha fatto, che cosa gli manca e quanto vale. Il docente non controlla le pagine: guarda il cruscotto, va di persona da chi è fermo e dà a Claude le correzioni. Senza nomi di allievi.*

## 01 A che cosa serve

1. **Il docente vede tutta la classe in una pagina**, dal telefono o dal PC, aggiornata da sola.
2. **I ragazzi lavorano senza aspettare il docente:** la pagina della lezione li guida, l'assistente risponde alle domande, «Il mio punto» dice a ognuno che cosa gli manca.
3. **Il voto si costruisce durante la lezione**, con il conto scritto per ognuno: a fine ora è pronto il pacchetto per il registro.

## 02 Dove si apre

1. Indirizzo: `avanzamento/?b=<lezione>-v1` sul sito del corso (per esempio `?b=3inf-portfolio-v1`).
2. Si apre con il **codice dell'area docente**. Senza codice non si vede niente: i dati con nomi e voti sono **cifrati** (vedi capitolo 07).

## 03 Che cosa c'è in ogni riga (un allievo per riga)

1. **Nome e cognome** e l'ora dell'ultimo segnale dalla pagina della lezione.
2. **Schede lette** (barra e percentuale), con il titolo della scheda dove si trova.
3. **🏁 FINITO** davanti al nome e bordo verde quando il lavoro vero è completo al **controllo automatico** (per la 3INF: il portfolio 9 su 9 sul sito vero). «Schede lette 11/11» non vuol dire finito.
4. **🌐 portfolio X/9 · manca: …** con l'elenco completo di ciò che manca; il link alla pagina c'è solo se la pagina esiste davvero (niente 404).
5. **Miniature** delle pagine del sito dell'allievo (index, competenze, passione), cliccabili verso il sito vero.
6. **🖥 PC · ora · che cosa fa**: l'ultimo giro di schermate Veyon letto da Claude; in rosso se è fuori dalla lezione.
7. **DOMANDA delle hh:mm: «…» ✅ risposta data / ⏳ senza risposta**: cliccando si leggono la domanda all'assistente e la risposta.
8. **Verifica**: crocette giuste, voto della verifica.
9. **★ voto proposto** in centesimi, con il conto (vedi capitolo 05).

## 04b Il cruscotto UNICO della lezione (21/10/2026, regole di Nicola)

1. **A che cosa serve:** a TENERE SOTTO CONTROLLO LE ATTIVITÀ DEGLI ALLIEVI. È sempre questa la logica.
2. **Uno solo per lezione:** in una pagina tutte le attività del giorno (lettura della teoria e ripasso, esercizi, quiz su Moduli), una riga per ogni presente, anche chi non ha fatto niente. Modello: `docs/avanzamento/oggi.html?t=<teoria>&e=<esercizi>&q=<quiz cifrato>&v=<veyon e note cifrati>`.
3. **Le domande orali:** la risposta secca in interrogazione (giusta 70, sbagliata 50) ha la sua colonna ed entra nella media del voto proposto.
4. **Veyon e note:** il cruscotto tiene conto delle attività rilevate da Veyon (ultimo giro, rosso = fuori compito, quante volte fuori compito, tutti i giri apribili) e delle note della lezione (nota sul registro, uscite, entrate fuori orario). Solo fatti, come nel diario.
5. **Voto proposto 40-80:** media dei voti che ci sono (esercizi, quiz, domande orali); chi non ha consegnato niente 40. Per DIDAweb la prova che resta è il quiz su Moduli.
6. **APPROVATO da Nicola il 21/10/2026 («così va bene»):** questo è il modello del cruscotto per tutte le lezioni e tutte le classi. Colonne fisse: allievo e ultimo segnale · teoria e ripasso · esercizi della lezione · quiz su Moduli · domande orali (70/50) · Veyon e note · voto proposto 40-80. Una riga per ogni presente, ordine dal voto più alto, giallo chi è fermo. Si cambiano solo le attività del giorno nei parametri della pagina.
7. **Storico:** i dati dei cruscotti si storicizzano sempre, per poterli riguardare (riservato `storico/cruscotti/<classe>/<data>/`; le consegne grezze in `dati/verifiche/<id>/arrivi/`).

## 04 Le regole del cruscotto (sempre valide, 19/10/2026)

1. **Ordine: dal più bravo al meno.** All'inizio della lezione conta ciò che ha **svolto** (schede, lavoro vero, verifica consegnata); man mano che ci si avvicina alla fine conta il **voto proposto**. Il peso scorre con l'orologio della lezione e in cima alla pagina c'è scritto («adesso conta 30% svolto e 70% voto»).
2. **🏁 per chi ha finito, «manca: …» per gli altri.** Finito = controllo automatico completo, non schede cliccate.
3. **Grigio = fermo e fuori.** La riga diventa grigia solo se l'allievo non manda segnali da più di 2 minuti **e** Veyon lo vede fuori dalla lezione; chi scrive codice su GitHub resta a colori.
4. **Tutti i presenti ci sono.** Chi Veyon vede ma non ha ancora scritto il nome sulla pagina compare con «non ha ancora scritto il nome». Lo stesso ragazzo scritto in due modi è una riga sola.
5. **Le domande si capiscono da sole:** «DOMANDA delle…» con domanda e risposta.
6. **Avviso giallo** quando metà classe ha il lavoro completo: il passo dopo deve essere già pronto.

## 05 Il voto proposto

1. **Scala 40-80** (la lezione normale; oltre 80 con la verifica e il recupero).
2. **Pesi:** 30% quanto lavora (giri Veyon al lavoro sul totale dei giri), 30% che cosa ha fatto (schede, verifica, risposte scritte), 40% com'è il lavoro vero (controllo automatico del sito).
3. **Chiedere aiuto conta:** +5 a chi ha chiesto all'assistente; chi non fa e non chiede ha l'insufficienza peggiore (−5).
4. A fine lezione il generatore fa il **pacchetto per il segnalibro «Voti DIDAweb AUTO»** con i nomi come nel registro e i soli presenti.

## 06 Il giro dell'assistente durante la lezione

1. **Ogni 2 minuti:** battito dello script, nuove righe del Foglio «Arrivi verifiche» e della cartella `arrivi/` su Git; risposte alle domande; correzione delle verifiche; recupero aperto per chi è sotto 60.
2. **Ogni 10 minuti:** controllo dei siti veri (`portfolio_3inf.py`), «Il mio punto» di ognuno, voto proposto, miniature.
3. **A ogni screenshot di Veyon:** `strumenti/giro_veyon.py` lo mette nel monitor pubblico della classe (nomi abbreviati) e nel cruscotto (nomi interi, cifrato).

## 07 Privacy

1. Tutto ciò che ha nomi interi o voti e sta nel repository pubblico si scrive **cifrato** con `strumenti/cifra_json.py` (AES-GCM, chiave dal codice dell'area docente con PBKDF2): `avanzamento/<lezione>.json`, `-siti`, `-voti`, `-schermi`, `thumb/<lezione>/indice.json`.
2. Il cruscotto li decifra nel browser con il codice che il docente scrive. Senza codice, i file sono illeggibili.
3. Le pagine per i ragazzi usano «Nome I.»; i materiali per l'esterno nessun nome.

## 08 Se lo script si ferma

1. Il cruscotto ripiega da solo sulla copia che aggiorna Claude (scritto in cima: «aggiornato dall'assistente»).
2. **Quota di Google:** il 19/10 il timer si è fermato alle 04:07 perché lo script lavorava anche di notte. Dalla versione 8.0 il giro dorme fuori orario (lun-ven 7-15), legge solo la coda degli ultimi 7 giorni e scrive un battito: la quota basta sempre. Serve il deploy «Nuova versione» da PC (una volta).

## 09 Come si rifà per un'altra lezione

1. La lezione nel motore `verifica/?b=<lezione>` con le schede e le domande di controllo (MANIFESTO §9.5).
2. Un controllo automatico del lavoro vero (come `portfolio_3inf.py` per i siti): definisce il 🏁.
3. `voto_<classe>_oggi.py` con i pesi del capitolo 05.
4. Il cruscotto è lo stesso per tutte le lezioni: cambia solo `?b=`.

## 10 Registro delle versioni

1. **v1.0 (19/10/2026):** prima versione, dalla lezione della 3INF: righe complete, 🏁, «manca», miniature, Veyon dentro il cruscotto, domande con risposta, voto proposto 40-80 con la regola delle domande, ordine dal più bravo, dati cifrati.
