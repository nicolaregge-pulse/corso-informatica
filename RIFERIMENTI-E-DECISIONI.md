# Riferimenti rapidi e decisioni (Nicola ↔ Claude)

**Versione 1.1** — 30/09/2026

*File durevole su Git: raccoglie contatti, convenzioni e decisioni stabili, così non
si perdono quando la sessione viene compattata. Regola: qui NON entrano mai nomi di
allievi (minori) né voti nominali; quelli restano solo in scratchpad/PDF riservati.*

---

## 1. Contatti e riferimenti
1. **Assistenza tecnica (sysadmin):** `support.piamarta@piamarta.it`
2. **Email studenti:** `nome.cognome@studenti.piamarta.it`
3. **Email docenti:** `nome.cognome@piamarta.it` (Nicola: `NICOLA.REGGE@PIAMARTA.IT`)
4. **Scuola:** Piamarta · **Aula laboratorio:** 11
5. **Docente:** Regge Nicola · **Discipline:** Tecnologia professionale, Laboratorio
   professionale, Sicurezza professionale, Informatica.
6. **Classi:** 1INFspe (Classe 1), 2INFspe (Classe 2), 3INFspe (Classe 3), 4TI (Classe 4).
7. **Sicurezza = programma della REGIONE** (si fa ciò che dice la Regione, non ciò che
   decidiamo noi): quando si corregge, farlo sempre notare a Nicola.

## 2. Convenzioni durature
1. **PPP** = "parcheggia": annota, prepara in silenzio, **non consegnare** finché
   Nicola non dice **"avanti"**. Eccezione: se dentro il PPP c'è un'azione concreta
   esplicita, quella si fa subito.
2. **Riflessione obbligatoria:** ogni compito finisce con "cosa NON ho fatto e perché"
   + "cosa NON ho capito". È la parte più importante da leggere.
3. **Un foglio = una cosa sola.** Coordinate complete (app → scheda → area → azione).
   Cose da copiare sempre in **blocco di codice** (bottone copia).
4. **Lingue materiali ragazzi:** versione **italiana per tutti** + **bilingue** solo
   per chi serve. Classe 1 = IT/AR/ZH; Classe 3 = IT + bangla. Materiali docente = IT.
5. **Git — DUE repo:** il **pubblico** `corso-informatica` (ex `corso-godot`, che
   resta come redirect; contiene anche i **giochi Godot**) tiene solo materiale
   **condivisibile** (didattica, esperimenti/giochi/siti dei ragazzi): **mai** nomi
   di minori, voti nominali o dati personali. Tutto ciò che è
   **riservato/strategico/personale** (nomi, voti nominali, presenze, anti-plagio,
   dati di rete, cedolini) va nel repo **PRIVATO** `corso-informatica-riservato`
   (le **fonti** versionate stanno lì). I **PDF/ZIP pesanti** sono **rigenerabili**:
   NON si versionano (scratchpad + consegna a Nicola).
6. **Consegne ragazzi:** preferire **un solo Documento Google** (screenshot + testo/codice
   + riflessione), non file .html/ZIP da raccogliere.
7. **Metodo:** "Vinci subito · Fallo tuo · Mostralo"; passi piccoli, micro-vittorie ogni
   15-20 min; niente 3 ore di fila sullo stesso compito (spezzare, "mostralo" al compagno).
8. **GIT come archivio e struttura (regola):** usare Git per **archiviare i materiali** e
   costruire **strutture logiche riusabili** (fonti uniche `argomenti/`, generatori, indici,
   registro, file di riferimento) così da **non perdere lavoro** col compattamento e
   **ottimizzare i tempi di Claude**. Preferire sempre strutture Git-backed a file effimeri;
   i dati **riservati** (nomi di minori) restano comunque fuori da Git (scratchpad + PDF).
9. **Due griglie a ogni compito (per il docente):** (a) **griglia completa** del lavoro —
   tutte le note + cosa NON ha fatto in **neretto** + voto; (b) **griglia incrementale** —
   solo info principali, **una colonna per compito** che si accumula nel tempo. Vale per
   tutte le classi. Entrambe RISERVATE (nomi) → PDF a Nicola, mai su Git.

## 3. Tassonomia dei libri (decisa)
1. **A — Manuale / Libro totale:** per ARGOMENTO, **3 livelli** (base/intermedio/avanzato).
   Fonte unica = `argomenti/`.
2. **B — Libro complessivo di classe:** teoria + compiti di tutte le lezioni (senza nomi).
3. **C — Libro individuale:** B + il lavoro del singolo **valutato** + indicazioni +
   **riflessione** + (foto della lavagna, fornite da Nicola). Riservato.
4. **D — Libro parziale:** una giornata o una lezione (sottoinsieme).
5. **Core vs Approfondimento:** core = ciò che ha fatto QUELLA classe; il meglio fatto
   nelle altre classi = **"Approfondimento"** in un riquadro distinto.
6. **Naming:** `Libro-Classe-N_COMPLESSIVO_vX.Y` · `Manuale-Informatica_vX.Y` ·
   `Libro-Individuale_Cognome-Nome_Classe-N_..._RISERVATO`.
7. **Header/footer:** standard vincolante (vedi `REGOLE-FORMATTAZIONE.md` §12): banda per
   unità (macro-argomento · materia · data · orario · contenuto) + footer di pagina.

## 4. Dove stanno le cose (repo)
1. `argomenti/` — la **fonte unica** a 3 livelli + `_build/genera_manuale.py` (Manuale).
2. `classe-1/libro-individuale/` — `unita/`, `manifesto.md`, generatori (`_build/`:
   individuale, generale, `render_libro.js`).
3. `REGISTRO-ORE-2026-27.md` — tutte le ore (navigabile per giorno / classe / materia).
4. `manuale-informatica/` — il Manuale generato.
5. **Dati riservati** (voti + nomi, anti-plagio, presenze, strategico, personale):
   nel repo **PRIVATO** `corso-informatica-riservato`, clonato in
   `/home/user/corso-informatica-riservato`. Struttura: `dati/` (fonte di verità,
   con `libro-dati-riservato.json` + `anagrafiche/` + `presenze/`), `generatori/`
   (script che producono output coi nomi), `antiplagio/`, `strategico/` (+ `personale/`,
   `password/`). I PDF/ZIP si **rigenerano**, non si versionano (`.gitignore`).
6. **Libri individuali:** generatore **pubblico**
   `classe-1/libro-individuale/_build/genera_libro_individuale.py` con i dati passati
   dal privato: `--dati /home/user/corso-informatica-riservato/dati/libro-dati-riservato.json`.
   La teoria/descrizione compiti (pubblica, senza nomi) viene **infrapposta** al lavoro
   valutato del singolo (dal privato). Output = PDF in scratchpad, consegnati a Nicola.

## 5. Aperte (da completare)
1. **PDF tassonomia dei libri** — FATTO: `TOPOLOGIA-LIBRI-E-METODOLOGIA.md` (v0.1)
   + `...-v0.1.pdf` (tipi A/B/C/D, fonti a 3 livelli, nomi/versioni, due repo, operatività).
2. **Programma Sicurezza (Regione)** — atteso da Nicola.
3. **"Io e la mia famiglia" 17/09** — manca lo ZIP per l'ultima colonna della griglia.
4. **Lezione HTML Classe 3 → nei libri** (dopo il PDF tassonomia): diventa argomento + unità.

## 6. Changelog
1. **v1.0 (30/09/2026)**: prima versione, per non perdere i riferimenti al compattamento.
2. **v1.1 (30/09/2026)**: modello a **due repo** (pubblico `corso-informatica`, ex `corso-godot` + privato
   `corso-informatica-riservato`). I dati riservati (nomi, voti, presenze, anti-plagio,
   strategico, personale) non stanno più solo in scratchpad ma nel repo privato; i
   PDF/ZIP restano rigenerabili. Aggiornati §2.5, §4.5 e §4.6.
