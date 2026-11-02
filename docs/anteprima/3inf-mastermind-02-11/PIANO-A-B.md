# Piano A e piano B, 3INF del 02/11/2026 (Mastermind e Slideshow)

**Versione 1.0** — 02/11/2026 — documento interno. ANTEPRIMA: nulla è collegato ai ragazzi.

## 01 Tabella

| Pezzo | Piano A | Piano B | Come si passa a B |
|---|---|---|---|
| Percorso | `modulo-N.html`, percorso completo | percorso facilitato di 3 passi nella stessa pagina (riquadro arancione) | lo sceglie il ragazzo o glielo dice il prof |
| Consegna | `consegna.html?ora=N`: unit1.pas e screenshot, controllo automatico (verde/rosso, non blocca mai), un bottone manda allo script (`dati/verifiche/3inf-mm0211-oraN/arrivi/`) | allegati al compito Classroom (`oraN_unit1.pas`, `oraN_screenshot.png`), sezione «Piano B» in fondo a ogni percorso | ogni pagina mostra «Se il bottone non funziona…» |
| Cruscotto | `generatori/cruscotto_3inf_mastermind.py` (segnali dal Foglio + consegne della pagina + Classroom + Veyon) | stesso generatore con `--piano-b` (solo Classroom) | Claude lancia il generatore con `--piano-b` |
| Codice di riferimento | `codice/ora1_unit1.pas`, `ora2_unit1.pas`, `ora3_unit1.pas` (aiuto 3 di ogni ora) | percorso facilitato (codice di 1-2 righe) | — |

## 02 Prima della lezione

1. In `config.json` di questa cartella `attivo` è **false** (anteprima). Si mette **true** solo dopo il «pubblica» del docente: da quel momento le pagine mandano segnali e consegne.
2. Compito Classroom: vedi `3inf-classroom.json` (scratchpad) e `config/3inf-mm0211.json` del riservato (coursework_id e cartella di raccolta).
3. Presenze: `config/3inf-presenti-20261102.json` (lista di nomi). Se manca, il cruscotto mostra tutta la classe.

## 03 Che cosa è provato

1. I tre `unit1.pas` compilati con Free Pascal 3.2 (`-Mobjfpc -Sc -Sh`) contro un finto Lazarus (stub di Forms, StdCtrls, ComCtrls, ExtCtrls), con prove su casi di esatte e spostate.
2. Il controllo automatico (JavaScript e Python) sui tre codici.
3. Pagine nel browser a 390 px: nessun errore JavaScript, nessuno scroll orizzontale.
4. NON provato: l'invio vero allo script di Google, il progetto dentro Lazarus vero (nessuna installazione di Lazarus qui), la raccolta Classroom.
