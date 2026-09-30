# Libro individuale — Classe 1 (struttura generativa)

**Versione 1.0** — 30/09/2026

*Come è fatto e come si genera il "libro individuale" di ogni allievo: il suo
portfolio personale che raccoglie, in ordine di data, TUTTO il lavoro (teoria +
testo del compito + il suo compito svolto con valutazione + la sua riflessione)
di TUTTE le lezioni. Cresce a ogni lezione.*

---

## 1. L'idea (perché così)
1. Il libro individuale del singolo contiene **due tipi di contenuto**:
   1. **Condiviso** (uguale per tutti): la **teoria** della lezione, il **testo
      del compito**, i **criteri di valutazione**. Non contiene nomi.
   2. **Personale** (del singolo allievo): il suo **lavoro consegnato**, la sua
      **valutazione**, la sua **riflessione** (cosa non ho fatto/perché + cosa
      non ho capito). Contiene il nome → dato di minore.
2. Per questo si separano:
   1. la parte **condivisa** sta **su Git**, versionata, una **unità per lezione**
      in `unita/` (deterministica: come i file col nome, permette di ricostruire
      sempre la stessa struttura);
   2. la parte **personale** sta **fuori da Git** (riservata, scratchpad), perché
      sono dati di minori.
3. Il **libro complessivo** di un allievo si **genera** unendo tutte le unità (da
   Git) con i suoi dati personali (riservati). Aggiungendo una nuova lezione basta
   aggiungere una unità e aggiornare il `manifesto.md`: il libro di tutti si
   aggiorna da solo.

## 2. Struttura dei file
1. `manifesto.md` — l'elenco ordinato delle unità (id, titolo, data). È l'ordine
   con cui compaiono nel libro.
2. `unita/NN-slug.md` — una unità per lezione. Sezioni fisse:
   `## Teoria`, `## Il compito`, `## Criteri di valutazione`.
3. `_build/genera_libro_individuale.py` — il generatore: legge il manifesto, le
   unità e i **dati riservati** del singolo, e produce il PDF complessivo.
4. **Dati riservati** (NON in questa cartella, NON su Git): un file per allievo
   con, per ogni unità, il lavoro svolto + valutazione + riflessione. Vive nello
   scratchpad del docente.

## 3. Come si aggiorna a ogni lezione
1. Si crea `unita/NN-<nuova-lezione>.md` (teoria + testo compito + criteri).
2. Si aggiunge la riga nel `manifesto.md`.
3. Si aggiornano i **dati riservati** dei singoli (lavoro + valutazione +
   riflessione) man mano che si correggono le consegne.
4. Si rigenera il libro complessivo di ciascuno.

## 4. Privacy (vincolante)
1. In questa cartella (su Git) **non entrano mai nomi di allievi**: solo teoria,
   testo compito, criteri.
2. I nomi e i lavori dei singoli restano **fuori da Git** (riservato). Il PDF
   complessivo generato (che contiene il nome) si consegna al docente/allievo, non
   si versiona su Git.

## 5. Changelog
1. **v1.0 (30/09/2026)**: prima struttura generativa (README, manifesto, prime
   unità, generatore).
