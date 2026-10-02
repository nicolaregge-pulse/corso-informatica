# Visione — Pipeline automazione didattica (lavagna → Classroom → CHIUDI)

**Versione 0.1** — 02/10/2026 · *Esigenza principale di Nicola (dettata il 02/10). Questo file è
la specifica-guida del flusso automatico. La MECCANICA la fanno gli script Apps Script; i
CONTENUTI e la VALUTAZIONE li fa l'AI. Nomi/voti dei minori: solo repo privato.*

---

## 1. Il flusso completo (come lo vuole Nicola)

### Fase A — Dalla lavagna ai materiali (AI)
1. Nicola fa la lezione **alla lavagna** e manda la **foto**.
2. L'AI genera la **DISPENSA** (teoria) in base a ciò che è stato fatto alla lavagna, con
   **l'immagine della lavagna dentro** (regola §2.18) — trilingue dove serve.
3. L'AI genera il **COMPITO** coerente, con **grafica IDENTICA alla dispensa** (regola §2.19).

### Fase B — Pubblicazione su Classroom (script)
4. Lo script pubblica su Classroom **sia la dispensa sia il compito** (allegati/link).
5. Lo script **fissa l'ora di consegna** del compito.

### Fase C — "CHIUDI" (script raccoglie → AI genera)
6. Al comando **CHIUDI**, lo script **raccoglie le consegne** e le mette dove servono all'AI
   (ponte: condivide col Gmail personale → l'AI legge col connettore Drive; verificato che
   funziona la lettura dei Google Doc).
7. L'AI genera **TUTTO**:

   **a) LIBRO COMPLETO INDIVIDUALE** (per ogni allievo) — NON solo il compito del giorno, ma
   **l'insieme di tutto il suo percorso**: tutte le lezioni, tutti i suoi compiti, tutte le sue
   valutazioni e indicazioni. Il libro **cresce** a ogni lezione/compito.

   **b) ZIP per i ragazzi** — i PDF dei libri individuali, **ciascuno protetto da password**
   (una password per allievo; stabili, non cambiano — errore #8).

   **c) Documenti PER IL DOCENTE (aperti, senza password):**
   - **Griglia di valutazione** (voti /10, proposta AI);
   - **"Cosa non hanno capito i ragazzi"** (dalle riflessioni);
   - **Report lavoro/monitoraggio** (chi ha lavorato o no, segnalazioni, con orari);
   - **I compiti/libri dei singoli ragazzi SENZA password** (copia per il docente).

## 2. Divisione dei ruoli
1. **Script Apps Script = meccanica:** pubblica dispensa+compito, fissa scadenza, raccoglie le
   consegne, le condivide/mette dove servono. NON corregge, NON giudica.
2. **AI = contenuti e giudizio:** dispensa, compito, correzione, voti/giudizi ("dell'AI"),
   anti-plagio, "parole loro", libri individuali cumulativi, documenti docente.

## 2b. Account coinvolti (ATTENZIONE — chiariti da Nicola 02/10)
1. **Account DIDATTICO/scuola (Classroom + script):** `nicola.regge@piamarta.com`
   *(DA CONFERMARE se `.com` o `.it`: gli allievi sono `@studenti.piamarta.it`, e una condivisione
   di ieri era a `nicola.regge@piamarta.it`).* Qui vivono Classroom e le consegne; qui girano gli script.
2. **Account PERSONALE (connettore Drive dell'AI):** `nicolaregge@gmail.com`. Qui l'AI legge i
   file (connettore Google Drive verificato).
3. **Il ponte:** lo script (account scuola) **condivide** la cartella/ZIP delle consegne con
   l'account **personale** → l'AI la legge e genera i documenti. (Se la scuola blocca la
   condivisione esterna, ripiego: Nicola scarica e passa la ZIP a mano.)

## 3. Privacy (vincolante)
1. **Ragazzi:** ricevono SOLO il proprio libro, **con la propria password**.
2. **Docente:** riceve i documenti **aperti** + le **copie senza password** dei singoli.
3. **Nomi/voti/osservazioni:** solo nel **repo privato**; mai nel pubblico.
4. **Ponte:** la condivisione ZIP/cartella col Gmail personale fa passare dati di minori
   dall'account scuola al personale → da mettere esplicitamente nelle regole e confermare.

## 4. Stato
1. **Ponte verificato:** il connettore Drive legge i Google Doc del Drive personale (02/10).
2. Script base pronti: `crea-compito-classroom.gs`, `consegne-controlla-e-zip.gs`,
   `prepara-chiusura.gs`.
3. **PONTE B COSTRUITO E FUNZIONANTE (02/10/2026)** ✅ — `strumenti/invia-consegne-git.gs`
   (nel repo privato) + progetto Apps Script "Consegne Classroom → Git" sull'account scuola,
   con token fine-grained di `nicolaregge-pulse` (solo repo privato, Contents RW) nelle Proprietà
   dello script. **Prova riuscita:** compito "Da binario a decimale" 1INF → 20/22 consegne
   depositate come PDF in `dati/consegne/1INF/binario-decimale/` (+ `_INDICE.txt`), lette dall'AI.
4. **Vale per TUTTE le classi:** il setup (token+script+servizio) è **una tantum**; per un'altra
   classe/compito si cambiano solo 4 valori (COURSE_ID, COURSEWORK_ID, CLASSE, CARTELLA).
5. **Da rifinire:** (a) config **"solo incolla"** via Proprietà dello script / menu, per non
   toccare il codice (regola §2.20); (b) collegare al comando **CHIUDI** (AI genera libri+report);
   (c) accumulo per-allievo per il "libro completo individuale".

> PPP 02/10: specifica registrata. Preparazione in silenzio; consegna all'"avanti".
