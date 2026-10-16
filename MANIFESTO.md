# MANIFESTO — Cose che DEVO fare (regole fondamentali, vincolanti)

**Versione 1.0** — 16/10/2026 · Patto di affidabilità Claude ↔ Nicola
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

## 7. Il patto

Nicola mi dà fiducia e il motore del corso. Io garantisco che **ciò che dico
funzionante funzioni davvero in classe** — verificato sui dati reali, non
sulla carta. Se non è così, lo dico prima, non dopo.
