# Argomenti — la fonte unica del sapere del corso (a 3 livelli)

**Versione 1.0** — 30/09/2026

*La metodologia efficiente: ogni ARGOMENTO (topic) esiste UNA volta sola qui, come
fonte unica, scritto in 3 livelli di profondità. Da questi argomenti si generano il
Manuale (per argomento) e i libri di classe/individuali (per data). Migliorando un
argomento, si aggiornano da soli il Manuale e tutti i libri di tutte le classi.*

---

## 1. Perché così (efficienza)
1. Un argomento (es. "Stampanti") si può insegnare **più volte** (più classi, più
   mesi): sono **tante lezioni**, ma **un solo argomento**.
2. Il testo vive **in un posto solo** (`argomenti/<slug>.md`): niente copie da
   tenere allineate a mano. Lo migliori lì e si propaga ovunque.

## 2. Argomento vs Lezione
1. **Argomento** = il contenuto (questa cartella). Fonte unica, 3 livelli, versionato.
2. **Lezione** = una volta che l'argomento è insegnato, a una classe, in una data,
   a un certo livello (vedi `REGISTRO-ORE-2026-27.md`). La lezione **punta**
   all'argomento, non ne ricopia il testo.

## 3. I 3 livelli di profondità
1. **Livello 1 (base):** il minimo per farlo funzionare, a prova di errore.
2. **Livello 2 (intermedio):** aggiunge strumenti e casi d'uso.
3. **Livello 3 (avanzato):** approfondimenti, buone pratiche, problemi comuni.

## 4. Le tre "viste" generate dagli argomenti
1. **Manuale / Libro Completo** → per ARGOMENTO, tutti e 3 i livelli (il posto unico
   che ingloba tutto il meglio).
2. **Libro complessivo di classe** e **individuale** → per DATA (dal registro): per
   ogni lezione tira l'argomento al livello svolto; l'individuale aggiunge il lavoro
   del singolo.
3. **Libro parziale** (giornata/lezione) → stessa cosa, filtrata.

## 5. Formato di un file argomento
1. Front-matter: `slug`, `titolo`, `macro`, `versione`, opzionali `materiale`
   (dispensa collegata) e `immagini` (percorsi separati da `|`).
2. Sezioni fisse: `## Livello 1 (base)`, `## Livello 2 (intermedio)`,
   `## Livello 3 (avanzato)`, con liste numerate.

## 6. Changelog
1. **v1.0 (30/09/2026)**: prima impostazione della metodologia a 3 livelli.
