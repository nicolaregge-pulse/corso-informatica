# INDICE GENERALE — Dove stanno le cose

**Versione 1.0** — 02/10/2026 · *Mappa pratica dei DUE repository: dove trovare ogni cosa.
Complementare ad `ATLANTE.md` (che spiega i concetti) e a `RIFERIMENTI-E-DECISIONI.md` (le regole).*

---

## 1. I due repository
| | Nome GitHub | Contenuto | Dati di minori? |
|---|---|---|---|
| **PUBBLICO** | `nicolaregge-pulse/corso-informatica` (vecchio nome: corso-godot) | Tutto il corso: teoria, esercizi, giochi, strumenti, documenti | **NO** (mai nomi reali) |
| **PRIVATO** | `nicolaregge-pulse/corso-informatica-riservato` | Dati, consegne, voti, chiusure, esami, osservazioni | **SÌ** (resta solo qui) |

## 2. Repo PUBBLICO — mappa cartelle
### Didattica per classe
- `classe-1/ classe-2/ classe-3/ classe-4/` — materiali per anno (schede, dispense, lab, compiti).
  - es. `classe-1/dati-in-binario/` (scheda frontale), `classe-1/bit-e-byte/`, `classe-1/libro-di-testo/`.
- `argomenti/` — fonte unica del Manuale per argomento (3 livelli).
- `manuale/` — Manuale (libro di testo) + eserciziario; PDF versionati (ultime visibili, vecchie in `_storico/`).
- `manuale-docenti/ corso-docente-ai/ guida-docenti-alunni-non-italofoni/` — materiali per i DOCENTI.
- `esercizi/` — Fase 1 (esercizi separati). `consegne/` — modello/flusso consegne (solo segnaposto, no nomi).

### Giochi (Godot) e Pages
- `docs/` — **giochi pubblicati** su GitHub Pages (asteroidi, mattoni, quindici, talpa, torta, torta-panaccione, cassaforte).
- Sorgenti giochi: `acchiappa-la-talpa/ rompi-i-mattoni/ schiva-gli-asteroidi/ gioco-del-quindici/ torta-in-faccia/ torta-panaccione/ chirurgo-pasticcione/ battaglia-navale-3d/`.

### Strumenti e automazione
- `strumenti/` — script e tool. In particolare `strumenti/classroom-script/`:
  - `crea-compito-classroom.gs` (crea compiti), `consegne-controlla-e-zip.gs`, `prepara-chiusura.gs`,
    `VISIONE-AUTOMAZIONE.md` (la pipeline lavagna→Classroom→CHIUDI, il ponte, il dizionario).
  - `strumenti/render-pdf/` (HTML→PDF).

### Documenti di riferimento (radice)
- `RIFERIMENTI-E-DECISIONI.md` — le REGOLE durature (numerate §2.x).
- `ATLANTE.md` — mappa concettuale del corso.
- `AUDIT-REPOSITORY-2026-10-02.md` — audit dei repo.
- `PROMEMORIA-NICOLA.md` — cose da fare + roadmap (§6 sviluppi, §7 brochure).
- `REGISTRO-ERRORI-CLAUDE.md` — errori e correzioni.
- `ARGOMENTI-SVOLTI-2026-27.md` — registro dello svolto per classe (per l'Allegato A).
- Programmi/Regione: `classe-N/programma.md`, `allegato-a-*`, `programmi-ufficiali/`, `PROGRAMMA-PREVENTIVO-*`.
- `brochure/` — brochure commerciale (metodo + AI).
- `libro-paganini/` — indice del libro di testo "Paganini" (riferimento) + confronto col nostro libro.

## 3. Repo PRIVATO — mappa cartelle (DATI DEI MINORI)
- `dati/anagrafiche/` — nomi/nickname allievi, preferenze lingua (per classe).
- `dati/consegne/<classe>/<compito>/` — le consegne reali (PDF + TXT, depositate dal **ponte**).
- `dati/chiusure/<CLASSE>/` — gli **ZIP di chiusura** versionati (libri + griglie + report).
- `dati/andamento/report-andamento-classe-<CLASSE>.md` — **monitoraggio** (Veyon, segnalazioni, orari).
- `dati/presenze/ dati/valutazioni / quiz-*` — presenze, voti, risultati quiz.
- `config/classi.json` — **DIZIONARIO** delle classi (corso Classroom attivo per classe) gestito dall'AI.
- `generatori/` — script Python che generano chiusure/libri/griglie dai dati.
- `strumenti/invia-consegne-git.gs` — **IL PONTE** (Classroom → repo privato via GitHub).
- `materiale-esami/` — prove d'esame, soluzioni, griglie, rubriche (spostate qui per integrità).
- `antiplagio/ strategico/ backup/` — anti-plagio, note strategiche, backup (es. scratchpad).

## 4. L'automazione in breve (chi fa cosa, dove)
1. **Scheda frontale** (docente) → `classe-N/<argomento>/`.
2. **Ponte** raccoglie le consegne → `riservato: dati/consegne/<classe>/<compito>/` (PDF+TXT).
3. **Dizionario** classi → `riservato: config/classi.json`.
4. **CHIUSURA** (libri+griglie+report) → `riservato: dati/chiusure/<CLASSE>/`.
5. **Regole** del flusso → `pubblico: RIFERIMENTI §2.23`; visione → `VISIONE-AUTOMAZIONE.md`.

> Regola d'oro: **dati con nomi di minori → SOLO nel privato**; tutto il resto → pubblico. Entrambi versionati.
