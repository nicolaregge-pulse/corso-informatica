# Registro degli errori di Claude ("SBIRRO") — Corso Informatica

**Versione 1.4** — 01/10/2026

*Registro onesto degli errori che Claude commette, giorno per giorno, con la correzione
adottata e la regola nata di conseguenza. Serve a non ripeterli e a migliorare. Lo tiene
aggiornato Claude su richiesta di Nicola: a ogni nuovo problema si aggiunge una voce con la
data. NON contiene nomi di allievi (quelli restano nel repo privato).*

---

## 01/10/2026 — Chiusura compito Classe 2INF (Convertitore temperature)

1. **Pacchetto unico con i dati di tutti (privacy).**
   - Cosa: ho consegnato un solo ZIP con dentro i libri di tutti gli allievi + la griglia con
     tutti i voti + il monitoraggio, **senza protezione**. Aperto lo ZIP, si vedevano tutti i
     file di tutti e i documenti riservati del docente.
   - Perché è sbagliato: i dati di un allievo non devono mai stare in un file accessibile agli
     altri; i documenti del docente non vanno mescolati a ciò che può arrivare ai ragazzi.
   - Correzione: ZIP unico **ma** con i libri **cifrati, una password per allievo**, e i
     documenti docente cifrati con una password docente. → RIFERIMENTI §2.14.

2. **"Valutazione del docente" non autorizzata.**
   - Cosa: nei libri degli allievi avevo messo una sezione "Valutazione del docente", mentre
     Nicola non li aveva valutati lui.
   - Perché è sbagliato: non si attribuisce al docente un giudizio che non ha dato.
   - Correzione: la valutazione la dà l'AI, intitolata **"Valutazione dell'AI"**. → RIFERIMENTI §2.15.

3. **Sovra-correzione: avevo tolto del tutto la valutazione.**
   - Cosa: dopo l'errore 2, avevo tolto voto e giudizio dai libri.
   - Perché è sbagliato: il ragazzo deve avere voto e giudizio (utili), solo attribuiti all'AI.
   - Correzione: rimessa la valutazione come "dell'AI". → RIFERIMENTI §2.15 (v1.9).

4. **Standard del compito incompleto (mancava l'anti-plagio e il report completo).**
   - Cosa: la prima chiusura non seguiva lo standard della Classe 3 (mancavano anti-plagio,
     dossier evidenze col testo reale, report complessivo a più sezioni) e usava voti /100.
   - Correzione: 5 documenti docente (scheda valutazione, dossier evidenze, report complessivo
     con anti-plagio + indicazioni ragazzi + segnalazioni, griglia, incrementale), voti **/10**.

5. **Frainteso il problema di privacy segnalato.**
   - Cosa: alla segnalazione "senza password tutti vedono tutto" ho risposto con opzioni
     tecniche invece di capire subito l'accordo mancato (separazione + attribuzione corretta).
   - Correzione: prima capire la regola mancata, poi agire.

6. **Anti-plagio troppo assertivo all'inizio.**
   - Cosa: avevo scritto "ha copiato" per screenshot/testi simili.
   - Perché è sbagliato: possono essere lo **stesso account su 2 PC**; va verificato.
   - Correzione: sempre al condizionale ("da verificare") finché non confermato.

7. **Contenuto del libro dell'allievo da delimitare.**
   - Cosa: rischio di mettere nel libro del ragazzo indicazioni pensate per il docente.
   - Correzione: nel libro va tutto ciò che riguarda **lui** (lavoro, valutazione AI, come ha
     lavorato/monitoraggio su di lui, anti-plagio su di lui), **tranne** le indicazioni
     specifiche per il docente (prossimo passo, strategia di recupero).

8. **Password casuali che cambiano a ogni rigenerazione.**
   - Cosa: avevo generato le password dei libri in modo **casuale**; rigenerando lo zip (per
     un'altra correzione) sono cambiate, diverse da quelle già consegnate agli allievi.
   - Perché è sbagliato: una password consegnata deve restare **stabile** per sempre.
   - Correzione: password **fisse** (hardcoded) nel generatore; non cambiano più a nessuna
     rigenerazione.

9. **Password messa anche sui documenti del docente.**
   - Cosa: avevo cifrato anche griglie/report del docente. Nicola non deve sbloccare i propri
     documenti.
   - Perché è sbagliato: la password serve solo a separare i libri tra allievi; i documenti del
     docente li legge lui, devono essere **aperti**.
   - Correzione: cifratura **solo** sui libri degli allievi; documenti docente aperti (incluso
     il foglio riepilogo password).

10. **Non ho versionato lo ZIP finale di chiusura.**
    - Cosa: ho generato il deliverable finale (lo ZIP di CHIUDI CLASSE 2INF) e l'ho consegnato
      senza metterlo su Git.
    - Perché è sbagliato: regola di Nicola "tutto versionato"; il deliverable finale va
      conservato com'è stato consegnato.
    - Correzione: lo ZIP di chiusura si **archivia nel repo PRIVATO** (`dati/chiusure/<CLASSE>/`,
      force oltre il `.gitignore`), perché contiene nomi → mai nel pubblico. → RIFERIMENTI §2.5.

11. **Proposto argomenti senza il report delle lezioni precedenti.**
    - Cosa: ho suggerito argomenti per la Classe 1 senza prima dare il quadro di **cosa era
      stato fatto** nelle lezioni precedenti.
    - Perché è sbagliato: le proposte vanno ancorate allo svolto; Nicola deve vedere prima il
      report del fatto.
    - Correzione: **sempre** prima il report "lezioni precedenti" (dal registro svolti), poi le
      proposte. → RIFERIMENTI §2.16.

12. **Introdotto un argomento NON spiegato in classe (direzione inversa).**
    - Cosa: nella dispensa bit/byte ho aggiunto **decimale→binario**, mentre in classe (lavagna)
      si era fatto **solo binario→decimale**. Può confondere i ragazzi.
    - Perché è sbagliato: il materiale deve seguire la lezione reale; introdurre argomenti nuovi
      di mia iniziativa non va bene ("se Nicola avesse voluto, lo avrebbe fatto alla lavagna").
    - Correzione: **integrare** sì, **introdurre argomenti nuovi** solo dopo **confronto**; nel
      dubbio chiedo. Inoltre: la **foto della lavagna** va dentro la dispensa di teoria.
      → RIFERIMENTI §2.17, §2.18, §7.

---

*(Le prossime giornate si aggiungono qui sotto con la loro data.)*
