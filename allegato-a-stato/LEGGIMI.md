# LEGGIMI: Allegato A — Stato del programma (fatto / da fare)

**Versione 1.0** — 18/11/2026. Pubblico (nessun nome di allievo). Fa parte dei registri, come `ARGOMENTI-SVOLTI-2026-27.md` e `FIRME-REGISTRO-2026-27.md`.

## 01 Che cosa è

1. Un PDF unico, `ALLEGATO-A-STATO-DEL-PROGRAMMA-vX.Y.pdf` (A4 verticale, stampabile), con una sezione per classe (1INF, 2INF, 3INF, 4TI) e in fondo il registro delle versioni. Ogni voce dell'Allegato A ufficiale (Word del 02/11/2026, parte «Regge») è FATTO (verde, con data e fonte in piccolo) o DA FARE (giallo, con la nota «da confermare» se un argomento firmato la tocca senza coprirla tutta).
2. Il file corrente è quello con il numero di versione più alto in `allegato-a-stato/`; `stato-allegato-a.json` ricorda versione, data e ora, voci e changelog. Le versioni vecchie non si cancellano. Il documento v0.3 del 17/09 (voci larghe, prima dell'Allegato ufficiale) è in `archivio/`.
3. Il riservato ha una copia del PDF in `report/AAAA-MM-GG/` (stesso file, nessun nome).

## 02 Come si lancia (a fine giornata)

1. `python3 strumenti/aggiorna_allegato_a_stato.py --copia-pdf /home/user/corso-informatica-riservato/report/AAAA-MM-GG`
2. Lo strumento legge `programmi-ufficiali/2026-27/registro-allegati.json` (le voci), `svolto-2026-27.json` (voci confermate dal docente), `copertura-allegato-a.json` (quali lezioni coprono quali voci) e controlla che ogni lezione sia scritta in `FIRME-REGISTRO-2026-27.md` o in `ARGOMENTI-SVOLTI-2026-27.md`.
3. Se lo stato non è cambiato non fa nulla: stessa versione, stessi file (si può rilanciare quante volte si vuole). Se è cambiato: versione +0.1, riga di changelog automatica (quali voci sono passate a FATTO), nuovo PDF.
4. Scrive alla fine l'elenco dei titoli firmati che non sono ancora in `copertura-allegato-a.json`: ognuno si mappa su una voce esistente oppure resta senza voce. **Non si aggiungono mai voci all'Allegato A** (R5.2, dopo il 30/10 si può solo togliere).
5. Una lezione conta solo quando è finita (data e ora di Roma): una ora firmata in anticipo resta DA FARE con la nota «da confermare a fine ora» finché non è passata. Per questo conviene lanciarlo dopo le 14.
6. Prova su dati finti e idempotenza: `python3 strumenti/test_aggiorna_allegato_a_stato.py` (non tocca i file veri).

## 03 Come si aggiorna la copertura (dopo ogni lezione firmata)

1. In `copertura-allegato-a.json`, sezione «lezioni»: una riga con classe, data, ora, titolo come scritto sul registro, fonte (`firme` e il titolo tra «», oppure `argomenti` e una frase di `ARGOMENTI-SVOLTI-2026-27.md`).
2. Sezione «copertura»: `stato: fatto` con le lezioni che coprono TUTTA la voce, oppure `stato: nota` con il testo della nota se la copre solo in parte o se la voce è la più vicina (da confermare). Il testo della voce deve essere identico a quello del Word.
3. Nel dubbio si usa `nota`, non `fatto` (R7.6: non presumere, chiedi).

## 04 Proposta di aggancio (NON attivata)

1. Al giro di fine giornata e alla bobina: dopo il controllo di `controlla_controlli.py` (che già verifica che ogni lezione del giorno abbia la riga in ARGOMENTI-SVOLTI) lanciare il comando del capitolo 02 e scrivere nella bobina «Allegato A stato vX.Y: FATTO per classe».
2. Al REGISTRO-ALLIEVI: è citato in `LEGGIMI-REGISTRO-ALLIEVI.md` del riservato (capitolo «parte dei registri»); nel foglio Indice potrebbe comparire la riga «Allegato A stato: versione e ora».
3. Si attiva solo se il docente lo chiede.

## 05 Registro delle versioni

1. v1.0 (18/11/2026): prima versione dello strumento e del documento sull'Allegato A ufficiale; PPP del docente del 18/11/2026 (foto del documento v0.2 della Classe 1: «averlo aggiornato e tenerlo sempre aggiornato, fa parte dei registri»).
