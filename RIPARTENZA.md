# RIPARTENZA — da qui riparte ogni chat nuova

**Versione 1.0** — 21/10/2026 · Area Docente · senza nomi di allievi

*Perché esiste: le chat lunghe consumano il limite settimanale (ogni messaggio rilegge tutta la conversazione). Regola nuova: **una chat nuova ogni giorno di lezione**. La chat nuova legge questo file (corto) e `CLAUDE.md` (le regole), e trova tutto il resto su Git. Questo file lo aggiorna Claude a fine giornata.*

## 01 Come si apre la chat nuova

1. Nicola apre una chat nuova sul repository del corso e scrive: «Leggi RIPARTENZA.md e PROSSIME-LEZIONI.md, poi dimmi cosa facciamo oggi».
2. Claude legge questo file, `PROSSIME-LEZIONI.md`, il diario del giorno prima della classe in orario (riservato `diario/<classe>/`) e parte.
3. La chat del giorno prima non si usa più (resta come bobina nel riservato).

## 02 I due repository (clonati uno accanto all'altro)

1. **Pubblico** `corso-informatica` (cartella `corso-godot`): sito su GitHub Pages da `docs/`; push `git push origin HEAD:main`; dopo il push `bash strumenti/aspetta_pubblicazione.sh`, il link solo dopo «PUBBLICATO».
2. **Riservato** `corso-informatica-riservato`: nomi, voti, diari, coda e ponte dello script. Push con il giro di tentativi:
```
for i in $(seq 1 15); do git fetch -q origin main && git rebase -q origin/main && git push -q origin HEAD:main 2>/dev/null && break; sleep 3; done
```
3. Lo stop hook vuole tutto committato e pushato in tutti e due.

## 03 Lo script di Google «Consegne Classroom → Git» (account PIAMARTA)

1. Versione in uso: **v8.1** (deployment Versione 3, 21/10/2026, ore 09:35): i segnali di avanzamento vanno solo nel Foglio, niente lucchetto; il giro gira ogni minuto.
2. **Coda** `coda/*.json` (stato `da-pubblicare` → compito su Classroom) e **ponte** `comandi/*.json` (stato `da-eseguire`: `forms.crea_quiz`, `forms.risposte`, `drive.esporta`, `classroom.compiti`, `classroom.consegne`, `classroom.annuncio`, `classroom.annuncio_cancella`).
3. ID dei corsi: 1INF 877008807336 · 2INF 162656105584 · 3INF 25324574640 · 4TI 25324465949.
4. Foglio «Arrivi verifiche»: `1hpyJGHZpwDW7Y4ZwajtB_Qzr9AHc29Q_esgHr8NqJs8`.
5. **Se lo script è fermo:** piano B `docs/prof-pubblica/` (generatore `strumenti/gen_pianob.py AAAA-MM-GG`), piano C il testo da copiare. Per aggiornare lo script: codice dal link pubblico (`strumenti/automazione-corso.gs` su raw.githubusercontent), Ctrl+A, Ctrl+V, Ctrl+S, poi Esegui il deployment → Gestisci deployment → matita → Nuova versione → Esegui il deployment.

## 04 Come si fa una lezione (deciso il 21/10)

1. **Su Classroom al massimo un compito e un annuncio per classe al giorno**; l'annuncio dice «OGGI FATE SOLO QUESTE COSE, IN QUESTO ORDINE» con i link diretti.
2. Teoria e ripasso sulla pagina `verifica/?b=<banca>` (motore unico, banche in `docs/verifica/banche/`); gli **esercizi valutati sono un quiz su Google Moduli** (traccia per la Regione) creato dal ponte con `forms.crea_quiz`.
3. Documento della lezione MD+PDF dalla banca: `python3 strumenti/banca2md.py <banca> <cartella> AAAAMMGG <Nome-Pdf> [passi…]`.
4. Prova come un ragazzo prima di pubblicare: `NODE_PATH=$(npm root -g) node strumenti/prova_verifica.js <banca>` (serve `cd docs && python3 -m http.server 8765`).
5. **Scadenze sulle campanelle vere:** 08:55 · 09:55 · 10:50 · intervallo · 11:10 · 12:05 · 13:05 · 14:00; la scadenza è la campanella dell'ultima ora della classe (REGISTRO-ERRORI #97).
6. Nicola ha detto «pubblica tutto, fai tu» il 21/10: si pubblica la sera prima o all'alba, in orario utile; si dice sempre cosa si è pubblicato.

## 05 Il cruscotto unico (approvato il 21/10) e l'ufficio informazioni

1. **Ufficio informazioni** `docs/avanzamento/registri.html`: tutti i registri che crescono a ogni lezione.
2. **Cruscotto della lezione** `docs/avanzamento/oggi.html?t=<teoria-v1>&e=<esercizi-v1>&g=<giochi-v1>&q=<quiz cifrato>&v=<veyon cifrato>`: una riga per presente, teoria, esercizi, giochi, quiz Moduli, domande orali 70/50, Veyon e note, voto proposto 40-80.
3. I dati con i nomi sono **sempre cifrati** (`strumenti/cifra_json.py`): quiz e presenti → `docs/avanzamento/<classe>-oggi-quiz.json` (giro ogni 3 minuti con il ponte `forms.risposte`); Veyon e note → `<classe>-oggi-veyon.json` da `dati/<classe>-veyon-AAAAMMGG.json` del riservato ([ora, cosa, fuori]).
4. **Uscite dall'aula** `uscite.html` (`strumenti/uscite.py` legge i diari: righe «- HH:MM COGNOME NOME: bagno|uscita|rientro»).
5. **Fuori compito** `fuori-compito.html` (`strumenti/fuori_compito.py`, con le foto dei giri di Veyon: mappa ora → file in `dati/<classe>-veyon-giri-AAAAMMGG.json`).
6. Regole: `CRUSCOTTO-DAL-VIVO.md` v1.1.

## 06 Ogni giorno, in classe

1. Presenze nel diario riservato (`diario/<classe>/AAAA-MM-GG.md`); «Altro» = presente.
2. Titoli del registro ≤40 caratteri, voce dell'Allegato A; la firma è fatta se la colonna «Firma» ha data e ora.
3. Domande orali: risposta secca 70 giusta, 50 sbagliata, nel diario e nel cruscotto.
4. Veyon: solo fatti, nel diario e nel cruscotto.
5. A fine lezione: stringa per DIDAweb `GG/MM/AAAA h N | argomento | COGNOME NOME;voto …` con voti 40-80 = 40 + 40 × punti/massimo (leggere SEMPRE il massimo del quiz) e tutti i presenti.

## 07 Cose aperte (21/10)

1. 3INF del 21/10: dopo la lezione, il cruscotto dei siti dalla pagina «L'albero del mio sito».
2. 2INF giovedì 22/10: finire le interrogazioni sul WHILE (sorteggio di due).
3. 1INF prossima volta: il percorso a sfide sul binario e la pixel art.
4. In 2INF e 3INF, quando hanno finito: i giochi dei byte della 1INF.
5. Storico dei cruscotti: una fotografia a ogni giro in `storico/cruscotti/` del riservato (da fare).
