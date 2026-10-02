# AUDIT — Repository e lavoro del corso

**Versione 1.0** — 02/10/2026 · *Fotografia dei due repository (pubblico `corso-informatica`
e privato `corso-informatica-riservato`), rischi e ottimizzazioni, in ordine di priorità.*

---

## 1. Quadro dimensioni
| Repo | Working tree | `.git` (storia) | File tracciati |
|---|---|---|---|
| Pubblico (corso-informatica) | **528 MB** | 151 MB | 807 |
| Privato (riservato) | 107 MB | 52 MB | 271 |

## 2. 🔴 Priorità ALTA

### 2.1 — 269 MB di giochi Godot (wasm) nel pubblico
`docs/` contiene **7 esportazioni HTML5** di giochi, ciascuna con un `index.wasm` da **38 MB**
(il motore Godot, **identico** in tutte e 7). Da solo è **oltre l'80% del peso** del repo e
gonfia anche la storia (`.git` 151 MB): ogni clone scarica 500+ MB.
- **Opzioni:** (a) tenere su Pages **solo i giochi che servono davvero**, togliere i duplicati;
  (b) spostare i giochi pubblicati in un **repo separato** dedicato a GitHub Pages; (c) **Git LFS**
  per i `.wasm`. È l'intervento che pesa di più sul risultato.

### 2.2 — Soluzioni/chiavi d'esame nel repo PUBBLICO
In `materiale-da-organizzare/` ci sono file tipo *"Busta A/B … con **Chiave Correzione** /
**Soluzioni Docente** / **Griglia Soluzioni**"*. Essendo nel repo **pubblico**, chiunque (anche gli
studenti) può trovarli → **integrità d'esame a rischio**.
- **Fix:** spostarli nel **repo PRIVATO** (sono materiale docente sensibile).

## 3. 🟡 Priorità MEDIA

### 3.1 — .gitignore (come richiesto)
- **Privato: BEN FATTO.** Ignora i binari rigenerabili (`*.pdf/*.zip/*.png/*.jpg`) con l'eccezione
  `!dati/consegne/**` per tenere le consegne; i deliverable (chiusure, backup) si **force-addano**
  apposta. Nessuna modifica necessaria.
- **Pubblico: MINIMALE** (solo `.godot/`, `/android/`, `__pycache__`, `*.pyc`). Da arricchire:
  aggiungere `.DS_Store`, `*.tmp`, e **decidere la politica sui build dei giochi** (`docs/` export):
  se non servono su Pages, ignorarli; se servono, valutare LFS (vedi 2.1).

### 3.2 — Versioni vecchie del manuale
`manuale/` ha **v0.1 → v0.20** (20 PDF). La regola "versioni congelate" dice di tenerle, ma le
intermedie molto vecchie (v0.1-0.13) si possono **archiviare** (uno zip in `manuale/_storico/`)
per alleggerire, tenendo visibili le ultime.

### 3.3 — `materiale-da-organizzare/`
Il nome lo dice: va **smistato** (esami → privato, materiali buoni → cartelle giuste, il resto
archiviato). È un contenitore di cose non ancora collocate.

### 3.4 — Peso della storia git
Anche togliendo file ora, `.git` resta grande (151 MB pubblico) perché la **storia** li conserva.
Una pulizia della storia (`git filter-repo`/BFG) la ridurrebbe, ma è **avanzata e delicata** (riscrive
la storia): da fare solo se serve davvero, con backup.

## 4. 🟢 Priorità BASSA / già a posto
1. **Privacy pubblico: OK.** Nelle consegne pubbliche c'è solo `rossi-mario` (segnaposto finto):
   **nessun nome reale di minore nel pubblico**. I dati veri dei minori sono tutti nel privato. ✅
2. **Struttura privato: ordinata** (`antiplagio/ backup/ config/ dati/ generatori/ strategico/
   strumenti/`): dizionario classi, ponte, chiusure al loro posto. ✅
3. **Automazione: validata** (ponte Classroom→Git funzionante). Da consolidare nella versione
   "dizionario + funzioni per classe" e applicare in via definitiva il fix "deposita testo".

## 5. Proposta di azione (ordine consigliato)
1. **Spostare le soluzioni d'esame → privato** (rapido, importante — integrità).
2. **Decidere cosa fare dei giochi wasm** (l'intervento che pesa di più): quali tenere, dove.
3. **Arricchire il .gitignore pubblico**.
4. **Archiviare le versioni vecchie del manuale**.
5. **Smistare `materiale-da-organizzare/`**.
6. **Consolidare gli script di automazione** (dizionario + funzioni per classe + fix testo).
