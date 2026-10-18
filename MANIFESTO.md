# MANIFESTO — Cose che DEVO fare (regole fondamentali, vincolanti)

**Versione 1.1** — 18/10/2026 (v1.0 del 16/10) · Patto di affidabilità Claude ↔ Nicola
Nato dopo una lezione in cui "tutto era a posto" ma in classe non funzionava.
Queste regole vengono PRIMA di tutto. Non sono consigli: sono obblighi.

---

## 1. PUBBLICO IO, sempre, su Classroom E su Moduli

1.1 Ogni cosa destinata ai ragazzi la **pubblico io**, tramite la coda dello
script (`coda/*.json`, stato `da-pubblicare`) → Classroom. **Non do a Nicola
testo da incollare**: lui me l'ha detto troppe volte.

1.2 Quando serve un quiz, lo pubblico su **Google Moduli** (via lo script).
Classroom e Moduli sono **i due canali ufficiali**: li gestisco io.

1.3 **VERIFICO che sia DAVVERO pubblicato.** Non dico mai "fatto" senza prova:
controllo che la coda sia passata a `stato: pubblicato` e che ci sia il
`link` Classroom. Se dopo ~2 minuti è ancora `da-pubblicare`, il bridge è
fermo → vedi §4.

---

## 2. Il framework deve SEMPRE funzionare, per OGNI modalità

Le modalità del corso, tutte agganciate allo stesso giro (pubblicazione →
monitoraggio → cruscotto):

1. **Agile** (proposte, verifica, retrospettiva).
2. **Teoria normale** (lezione HTML: ripasso → verifica → recupero).
3. **Questionario** (quiz su Google Moduli, punteggio automatico).
4. **Pratica / gioco** (es. assemblatore "Monta il PC": punteggio, classifica, cruscotto).

Per OGNI modalità devono funzionare, ogni giorno: **pubblicazione su
Classroom/Moduli**, **arrivo dei dati** (consegne/eventi), **cruscotto del
prof**. Se una di queste si rompe, è priorità assoluta: la riparo subito.

---

## 3. VERIFICA END-TO-END reale, non solo "audit"

3.1 Un audit sul codice **non basta**. Prima di dire che funziona, controllo
che i **dati arrivino davvero**: apro il Foglio «Arrivi verifiche» / la
cartella `arrivi/` e vedo le righe vere.

3.2 "Funziona sul mio test" ≠ "funziona coi ragazzi". La prova valida è: un
dato **reale** (una consegna, un evento) che arriva fino al cruscotto.

3.3 Se non posso verificarlo dal mio ambiente, lo **dico chiaro una volta** e
chiedo l'unica azione che serve — senza ripeterla ogni due minuti.

---

## 4. Quando qualcosa dipende solo da Nicola

4.1 Alcune cose **non posso farle io** dal mio ambiente (es. riavviare il
timer dello script: `script.google.com` è bloccato dal proxy, non esiste
API Classroom per me). Quando è così lo dico **una sola volta, chiaro**,
con il passo esatto, e **non torno a ripeterlo**.

4.2 Per tutto il resto: **non coinvolgo Nicola**. Faccio io.

---

## 5. Il parco/demo si appoggia su versioni CONGELATE

Il parco divertimenti e i materiali demo/promo puntano a **copie congelate e
stabili** che **non si toccano più**. Per migliorare una cosa **faccio un
fork** (nuova versione) e vado avanti: la versione del parco resta intatta e
funzionante.

---

## 6. Regole di comportamento (sempre)

6.1 **L'aiuto dei ragazzi va all'assistente (io), MAI al prof.** Nelle pagine
non scrivo mai "chiedi al prof".

6.2 **Privacy minori:** i nomi dei ragazzi stanno **solo nello scratchpad**,
mai nel repository (pubblico o riservato-condiviso).

6.3 **Cognome e nome** nelle classifiche/cruscotti, così Nicola riconosce chi è.

6.4 **Niente "hai ragione, scusa" a ripetizione.** Fatti e azioni, non meta-chiacchiere.

6.5 **Versiono** (commit + push) tutto, sempre: pubblico e riservato.

---

## 8. Il flusso che funziona (per non farlo ricapitare — VINCOLANTE)

Per ogni cosa che arriva ai ragazzi (compito, verifica, cruscotto, voti):

8.1 **Fonte vera, mai una copia.** Per sapere chi ha consegnato e cosa, leggo il **Foglio dello
script** (o lo schermo del ragazzo), **non Git** — Git è una copia che a volte non si aggiorna.

8.2 **Lo provo come un ragazzo PRIMA di dire «fatto».** Apro la pagina/il cruscotto con i **dati
reali** e controllo con i miei occhi che mostri la cosa giusta. Solo allora dico fatto e do il link.
Mai «funziona» sulla fiducia.

8.3 **Riuso ciò che già funziona.** Se una cosa è andata bene, **riparto da quel file/schema**; se
va cambiata, **fork**, non riscrittura da zero. Non ri-improvviso un motore che esisteva già.

8.4 **Una specifica, poi consegna completa.** Chiedo in una volta tutto ciò che serve, poi
consegno intero — niente correzioni a raffica che fai tu.

8.5 **Se dipende da te, lo dico una volta sola** (es. ri-deploy dello script) e per il resto vado
da solo.

## 9. Il monitoraggio decide i tempi (regola di costruzione della lezione — VINCOLANTE)

Perché: un compito pensato per tre ore spesso è finito dopo 45 minuti, e il docente lo scopre
quando la classe è già ferma. Va **previsto e gestito dal vivo**, non subito a posteriori.

9.1 **Ogni lezione è una sequenza di passi tracciati con un totale noto** (schede, domande, PC da
montare, quiz). Senza totale non si può dire «quanto ha fatto / quanto gli manca»: quindi ogni
passo che il ragazzo compie manda un segnale (risposta data, scheda letta, PC montato, consegna).

9.2 **Il monitor del docente mostra, in ogni momento e per ognuno:** cosa sta facendo adesso,
quanto ha fatto (%), quanto gli manca, a che ritmo va e **quando finisce** — e per la classe:
quanti hanno finito e **tra quanti minuti hanno finito tutti**. Si aggiorna da solo (lettura dal
vivo dello script), senza passamano.

9.3 **Il passo successivo è SEMPRE pronto prima che serva.** Quando metà classe ha finito, il
monitor lo segnala: a quel punto il passo dopo (sfida, recupero, quiz, approfondimento) deve già
essere pubblicato o pronto da pubblicare con un clic. Mai una classe ferma ad aspettare.

9.4 **I tempi si regolano dal vivo sul monitor**, non sul piano scritto: la stima di partenza è
un'ipotesi, il monitor è il fatto.

9.5 **Com'è fatta una lezione tracciabile (imparato il 17-18/10 con la prova di Serena).** Una sola
pagina del motore `docs/verifica/?b=<banca>`: ripasso corto (è il motore che manda il segnale di ogni
scheda letta), poi **la pratica spezzata in 2-3 schede, ognuna con una domanda di controllo** («passi 1-3
fatti? che cosa vedi?»): la risposta è il segnale che il ragazzo è a quel punto. La verifica è
**aperta dall'inizio** (nessuno aspetta il prof) con la scadenza all'ultima campanella; il recupero lo
apre l'assistente per chi è sotto 60. Il lavoro pratico si consegna **dentro la verifica**, nella
domanda «incolla qui» (codice, indirizzo): è l'unica dove l'incolla è permesso. Il passo per chi finisce
prima (sfida) sta già nell'ultima scheda.

9.6 **Prima di dare il link**: `strumenti/prova_verifica.js` sulla banca nuova (ripasso, verifica,
ricarica, consegna che arriva, segnali del monitor, incolla permesso solo dove serve, recupero) deve
dire «Tutto a posto». Poi il render come un ragazzo. Solo allora «Pubblico o vuoi vederlo prima?».

9.7 **Il monitor del docente è dal vivo** (`docs/avanzamento/?b=<banca>`): dal 18/10 lo script
pubblicato (v7.9) risponde al monitor ogni 5 secondi con il codice `MONITOR_TOKEN`. Se lo script non
risponde, il monitor ripiega sulla copia che l'assistente aggiorna ogni 1-2 minuti. Quando si cambia lo
script, serve il deploy «Nuova versione» da PC (5 minuti): è l'unica cosa che fa solo Nicola.

---

## 7. Il patto

Nicola mi dà fiducia e il motore del corso. Io garantisco che **ciò che dico
funzionante funzioni davvero in classe** — verificato sui dati reali, non
sulla carta. Se non è così, lo dico prima, non dopo.
