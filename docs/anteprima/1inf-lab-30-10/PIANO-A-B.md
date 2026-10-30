# Piano A e piano B, laboratorio 1INF del 30/10/2026

**Versione 1.2** — 30/10/2026 — documento interno del docente e di Claude. Pubblicato: il laboratorio è in corso (hub, moduli, consegna e cruscotti sono online).

Regola di Nicola (29/10/2026): «per tutto fai una cosa e prepara un piano B, devono esserci tutte e due le cose già pronte».

## 01 Tabella

| Pezzo | Piano A | Piano B | Come si passa a B |
|---|---|---|---|
| Percorso | `modulo-N.html`, percorso completo | percorso facilitato di 3 passi, nella stessa pagina (riquadro arancione) | lo sceglie il ragazzo o glielo dice il prof; nessun cambio tecnico |
| Consegna | `consegna.html?ora=N`: sceglie unit1.pas e lo screenshot, controllo automatico subito (verde/rosso, non blocca mai), un bottone manda tutto allo script delle consegne (`dati/verifiche/1inf-lab3010-oraN/arrivi/`) | allegati al compito Classroom unico «Laboratorio 11-14: stringhe e interi in Lazarus» (896632311675; `oraN_unit1.pas` e `oraN_screenshot.png`), passi C2-C5 della pagina; lo script li raccoglie in `dati/consegne/1INF/lab3010-unico/` e il generatore ricava l'ora dal codice | ogni pagina mostra sempre «Se il bottone non funziona: …»; il prof lo dice a voce |
| Quiz | Modulo Google creato dal comando `comandi/2026-10-30_quiz-1inf-lab3010-tipi.json` (22 crocette), fatto su Moduli la mattina del 30/10 | `docs/verifica/?b=1inf-lab3010-tipi`, modo verifica (stesse 22 crocette + 3 aperte); si apre con `docs/verifica/stato/1inf-lab3010-tipi.json` → `"verifica": "aperta"` | Claude apre lo stato della verifica e mette il link nel compito |
| Cruscotto | `generatori/cruscotto_1inf_lab3010.py`: segnali delle pagine (Foglio «Arrivi verifiche» via `drive.esporta`), consegne della pagina, quiz, Veyon | stesso generatore con `--piano-b`: solo file e stato di Classroom | Claude lancia il generatore con `--piano-b`; la pagina è la stessa |

## 02 Che cosa serve il giorno della lezione

1. In `docs/anteprima/1inf-lab-30-10/config.json` mettere `"attivo": true`: senza, le pagine non mandano niente (anteprima). Fatto il 30/10 alle 08:15.
2. Cambiato il 30/10 (piano B): i tre compiti «Ora N» non sono nati dalla coda (sospesi). Le tre ore usano UN compito solo, la bozza 896632311675 con titolo «Laboratorio 11-14: stringhe e interi in Lazarus (3 programmi)»; in `config/1inf-lab3010.json` del riservato le tre ore hanno quell'id e la cartella `lab3010-unico`. Si pubblica con il comando pronto `classroom.mostra` dopo il «pubblica» di Nicola.
3. Dopo il comando del quiz: l'id del Modulo in `config/1inf-lab3010.json` (`quiz_moduli_id`).
4. A ogni giro: `python3 generatori/cruscotto_1inf_lab3010.py comando`, poi `python3 generatori/cruscotto_1inf_lab3010.py`.

## 03 Che cosa è provato e che cosa no

1. Provati il 29/10: i tre codici (Free Pascal 3.2, stesse procedure in un programma di prova), le 22 risposte del quiz (compilatore), il controllo automatico sui 3 codici e su 2 codici rotti (JavaScript e Python), la pagina di consegna nel browser con un indirizzo finto (invii, pezzi dello screenshot, JPEG ricomposto), i segnali dei percorsi, il cruscotto con dati finti (piano A+B e solo B).
2. NON provato da qui: l'invio vero allo script di Google (la rete di questa sessione non raggiunge script.google.com), il comando del Modulo (gira venerdì alle 7:00), la raccolta Classroom dei file .pas e .png (lo script la fa già con estensione originale, ma non con questi compiti).

## 04 Changelog

1. Versione 1.1, 30/10/2026: compito Classroom unico 896632311675 per le tre ore (piano B del ponte), `attivo` a true, passo C4 dei percorsi con il nome del compito unico e «Annulla consegna».
