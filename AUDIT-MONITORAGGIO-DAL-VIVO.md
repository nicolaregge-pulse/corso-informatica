# Audit: perché il monitoraggio dal vivo non funziona — e la soluzione

**Versione 1.0** — 18/10/2026 · per Nicola · scritto da Fable dopo aver riletto tutta la chat e il codice.

---

## 1. Il problema, in una frase

Vuoi una cosa che **gira da sola** e ti mostra **in tempo reale** cosa sta facendo ogni ragazzo
(a che scheda della teoria è, quanti PC ha montato, se ha consegnato il quiz) — **senza che nessuno
faccia il passamano**. Oggi il monitor si muove solo quando l'assistente legge il Foglio a mano.

---

## 2. Cosa funziona davvero (provato con dati reali)

2.1 Le pagine dei ragazzi mandano ogni evento allo script di Google (`/exec`): consegne del quiz,
eventi del simulatore, domande all'assistente e, da ieri, l'avanzamento nella teoria. **Arrivano
subito** nel Foglio «Arrivi verifiche» (ieri 19 consegne vere; Serena: 6 segnali in un minuto).

2.2 Teoria, simulatore, quiz, correzione, voti, pubblicazione su Classroom: funzionano.

---

## 3. Dov'è rotto (il solo anello mancante)

3.1 Il monitor del docente è una pagina **statica** su GitHub Pages: legge un file JSON nel
repository. Quel file cambia **solo** se qualcuno legge il Foglio, rigenera il file e fa un push,
e poi GitHub ci mette ~1 minuto a pubblicarlo. Non è automatico e non è dal vivo.

3.2 La via «lo script scrive su Git» è inaffidabile (righe «SOLO QUI») e comunque passerebbe dal
push + 1 minuto di GitHub.

3.3 **La via giusta esiste già nel codice ma NON è pubblicata.** Nello script c'è `doGet`
(v7.8, righe 659-695) che legge il Foglio e risponde **dal vivo** in JSONP. Il `/exec` oggi in
rete serve una versione **vecchia** senza quel pezzo. Pubblicare lo script è un'azione che
**può fare solo Nicola**: `script.google.com` è bloccato dall'ambiente dell'assistente.

3.4 Anche una volta pubblicato, il `doGet` attuale ha due mancanze:
- serve **solo la classifica del simulatore** (montati/smontati/tempi), non l'**avanzamento della
  teoria** né le **consegne del quiz**;
- **privacy**: `/exec` è pubblico (i ragazzi ci scrivono); senza un **codice del docente**
  chiunque con l'indirizzo leggerebbe i nomi.

3.5 Perché finora è andata male: i monitor sono stati costruiti sulla via sbagliata (file statico
+ passamano) invece di chiudere l'unico anello (lettura dal vivo del Foglio via script), e si è
detto «funziona» guardando render locali, non lo schermo del docente.

---

## 4. La soluzione (una sola)

**Il browser del docente legge il Foglio dal vivo attraverso lo script, ogni pochi secondi, con un
codice del docente.** Niente Git, niente push, niente passamano, niente attese di GitHub.

4.1 **Assistente — estende lo script** (file `strumenti/automazione-corso.gs`, specchiato nel
riservato e sul link pubblico): nuovo modo `?live=<id>&tok=<codice>&callback=fn` che risponde con
l'**ultima riga di ogni ragazzo** per quell'id: teoria (scheda/totale/titolo/quando), quiz
(giusti/voto), simulatore (montati/smontati). Il codice si controlla contro la proprietà
`MONITOR_TOKEN` dello script: senza codice giusto, risposta vuota.

4.2 **Assistente — rifà il monitor** (`docs/avanzamento/`): interroga lo script ogni 5-10 secondi
(JSONP); il docente scrive il codice una volta (resta salvato nel browser, come le altre password).
Se lo script non risponde, ripiega sul file statico. Una riga per ragazzo: nome · scheda N/10 ·
titolo · % · «attivo X secondi fa» · quiz consegnato/voto.

4.3 **Nicola — un solo deploy, una volta** (passi esatti forniti a parte): apre lo script
«Consegne Classroom → Git», incolla il codice aggiornato dal link pubblico, salva, imposta la
proprietà `MONITOR_TOKEN`, poi Deploy → Gestisci deployment → modifica → **Nuova versione** →
Deploy. L'indirizzo `/exec` **resta lo stesso**: niente da cambiare nelle pagine.

4.4 **Prova**: Nicola apre la pagina da allievo in una scheda e il monitor nell'altra e vede la
propria riga muoversi da sola. L'assistente verifica in parallelo leggendo il Foglio.

---

## 5. Cosa NON serve

- Un nuovo servizio esterno (Firebase e simili): soluzione valida ma più lunga; il deploy sopra
  richiede 5 minuti e usa quello che c'è già.
- Pubblicare il Foglio sul web: esporrebbe i nomi dei minori. No.

## 6. Se il deploy non si fa

Il monitor dal vivo **non è possibile** su questo impianto: resta solo l'aggiornamento a mano
dell'assistente. Va detto chiaro, non girato intorno.
