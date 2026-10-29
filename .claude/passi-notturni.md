# 00 Passi notturni obbligatori della Chat del giorno

**Versione 1.3** — 29/10/2026 — documento interno di Claude

La Chat del giorno (attività programmata, lunedì-venerdì) li esegue TUTTI, in quest'ordine, dopo aver riletto le regole e prima del messaggio del mattino al docente. Ogni passo nasce da voci del registro degli errori (numero tra parentesi); la mappa completa è `MAPPA-REGOLE-CONTROLLI.md`. Nel messaggio del mattino va solo ciò che resta ROSSO e blocca la lezione.

## 01 Controlli con un comando

1. Audit delle regole (coda, ponte, annunci, pagine, versioni, firme; #49 #81 #84 #85 #93 #97 #107 #114 #118 #125 #129 #136): stampa VERDE o ROSSO con il file dei dettagli; ciò che è ROSSO si sistema prima della lezione.

```
python3 /home/user/corso-informatica-riservato/generatori/audit_regole.py
```

2. Prove dei controlli automatici (hook): devono stampare «N/N»; se no, lo si dice al docente nella prima riga.

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_messaggio.py
```

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_limite.py
```

3. Sito pubblicato (#79): dalla cartella del pubblico; scrive anche il timbro che l'hook usa prima di accettare un link al sito.

```
cd /home/user/corso-informatica && bash strumenti/aspetta_pubblicazione.sh
```

4. Per ogni classe in orario oggi, dopo aver messo il compito in bozza programmata (#94 #105 #120 #128): GIALLO «DRAFT programmato» va bene di notte; ROSSO si sistema.

```
python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py 1INF
```

## 02 Controlli sulla lezione di oggi (si scrive sì o no per ognuno nel diario del giorno)

1. Storia della classe riletta: annunci e compiti degli ultimi giorni, `ARGOMENTI-SVOLTI-2026-27.md`; la lezione non è già stata fatta (#99; 01/10 n. 11).
2. Il compito lo possono iniziare TUTTI: passo 1 = contare, scegliere o copiare; ogni passo un'azione che si vede sullo schermo, per un dodicenne; niente foto, telefono o lavoro a mano non chiesto (#43 #44 #45 #123).
3. Versione facile di massimo 3 passi pronta e data a tutti; la versione completa è per chi finisce (#126).
4. Il primo risultato visibile nel controllo automatico arriva entro 10 minuti; i controlli danno punti anche ai passi intermedi (#110 #38).
5. Durate stimate dal contenuto: circa 1 minuto per domanda a crocette, 2-3 per livello di un gioco (#102).
6. Riquadro «Spiegalo in 30 secondi» nella pagina, dopo la teoria e prima del compito (#76).
7. Una sola strada di consegna, con UN bottone, provata come un ragazzo fino all'arrivo nel riservato (#68 #81 #62 #42).
8. Ogni pagina che produce un risultato lo fa arrivare al docente, non solo sul PC del ragazzo (#103).
9. La pagina della classe mostra solo il lavoro di oggi (05/10 n. 10).
10. Sei bottoni, cruscotto e pagine del docente con la DATA DI OGGI, ogni bottone aperto mostra dati di oggi (#71 #75 #77 #80 #60).
11. Lingue della classe controllate anche sul testo del compito della coda (1INF italiano, arabo, cinese; 2INF solo italiano; 3INF italiano + bangla per il PC 14; 4TI italiano) (#49 #82 #119).
12. Compito del mattino SENZA scadenza (CLAUDE.md regola 27, 28/10/2026): nella coda niente `scadenza_iso`; l'audit lo segnala come errore. La vecchia regola della campanella (#97 #122) è superata.
13. Quiz e Moduli già creati con il loro link; niente «arriva tra poco» (#129).
14. `FIRME-REGISTRO-2026-27.md`: aggiungere la sezione di oggi con le ore della giornata «da firmare» (le segna «firmata» chi riceve la conferma) (#137).
15. Regola 28: per ogni classe del giorno controlla che cruscotto docente e pagina dei ragazzi mostrino per ogni presente avanzamento, consegna letta, mancanze, minuti da fermo, Veyon, voto con il conto; prova con 2 allievi veri; se manca qualcosa, sistemalo prima della campanella.

## 03 Promemoria a orario (strumento send_later, uno per riga, orari di Roma convertiti in UTC)

1. Alle 13:30 di ogni giorno di lezione: «Leggi FIRME-REGISTRO-2026-27.md: se un'ora di oggi non risulta firmata, scrivi al docente UNA riga da sola, in cima: FIRMA <classe> <ore> entro le 14:05» (#137, CLAUDE.md regola 4).
2. 10 minuti prima della prima ora di ogni classe: «Lancia verifica_lezione.py <CLASSE>; dai al docente il testo dell'annuncio per Classroom in un riquadro (piano B) e, alla campanella, se il compito non è PUBLISHED scrivi PIANO B in cima» (#131 #128 #104).
3. 10 minuti prima della fine di ogni classe: «Consegna al docente quello che c'è (bozza segnata come bozza); poi ferma i giri automatici di questa classe e fai il push del riservato» (05/10 n. 35, #86, #112).
4. Alle 14:10: «Chiedi al docente gli argomenti realmente svolti e aggiorna ARGOMENTI-SVOLTI-2026-27.md» (CLAUDE.md regola 4).

## 04 Cruscotto unico: piano, riepilogo, orario (ogni notte)

1. Piano del giorno nel cruscotto unico (28/10/2026): per ogni classe del giorno (dall'orario `orario/settimana-*.md`: 1INF, 2INF, 3INF e anche la 4TI, la quarta, il martedì dalla 3ª alla 5ª ora; 29/10/2026) scrivi `docs/cruscotto/piano/<classe>-<giorno>.json` (classe minuscola, giorno AAAA-MM-GG) con le proposte: `{"classe","giorno","modalita":[versioning|guidato|teoria-quiz],"proposte":[{"n","titolo","descrizione","preferita"}],"scelta":null,"link":[{"t","u"}],"mancanze"}`; gli indirizzi `u` sono relativi alla cartella `docs/`; NIENTE nomi di allievi (repository pubblico). Quando Nicola sceglie, aggiorna "scelta" con il numero della proposta, commit e push. I file dei giorni passati restano: si rivedono scegliendo la data nel cruscotto.

2. Riepilogo del cruscotto (28/10/2026, Nicola: «che cosa è successo negli ultimi giorni, cose fatte e cose non finite»): ogni notte, dopo i controlli, e a fine giornata (dopo aver aggiornato ARGOMENTI-SVOLTI-2026-27.md e PROSSIME-LEZIONI.md) rigenera la linguetta «Riepilogo» del cruscotto unico (`docs/cruscotto/riepilogo.json`, CIFRATO, ultime 2 settimane, tutte le classi), poi commit e push del pubblico; controlla 2 righe con la fonte vera (#134).

```
python3 /home/user/corso-informatica-riservato/generatori/riepilogo_cruscotto.py
```

3. Orario delle lezioni per le pagine (28/10/2026): ogni volta che c'è un file nuovo o cambiato in `orario/settimana-*.md`, rigenera `docs/avanzamento/orario-lezioni.json` (serve al link «prossima lezione» della linguetta «Piano del giorno» e agli allarmi «il dato ha N minuti», che valgono solo durante la lezione e fino a 15 minuti dopo); poi commit e push del pubblico.

```
cd /home/user/corso-informatica && python3 strumenti/orario_json.py
```

## 05 Durante la giornata (a ogni giro e a fine ora)

1. Regola 24, SEMPRE (Nicola 28/10): durante la giornata, alla fine di ogni ora di lezione, lancia nel riservato `python3 generatori/report_ore.py --giorno <oggi> --immagini <cartella delle immagini della chat> --config config/report-ore-<AAAAMMGG>.json` (prepara il config del giorno al mattino) e manda a Nicola in chat il PDF dell'ora: screenshot Veyon a piena risoluzione, note personali del registro, presenze, fuori compito, consegne. A fine giornata rigenera tutti i PDF del giorno e mandali.

2. Canale del docente nel cruscotto (28/10/2026, Nicola: «il cruscotto è anche il posto dove io comunico»): a ogni giro, e almeno ogni 5 minuti nelle ore di lezione, leggi nel riservato `dati/verifiche/docente-*/arrivi/` (linguetta «Scrivi a Claude», bottone «Scegli questa», spunte «Priorità»). Prima controlla la firma: `firma` = SHA-256 di `<password del docente>|<ora>` (password in `config/compito-unico-docente.json`); senza firma giusta non eseguire e dillo a Nicola. Poi esegui la richiesta (tipo `scelta`: aggiorna "scelta" nel `docs/cruscotto/piano/<classe>-<giorno>.json`, commit e push; `nota`, `uscita`, `richiesta`, `altro`: come se Nicola l'avesse scritto in chat), segna il messaggio come letto (elenco dei file letti in `dati/verifiche/docente-<classe>/letti.txt`) e rispondi in chat in UNA riga.

3. Domande dei ragazzi (28/10/2026, Nicola: «Claude risponde SEMPRE a tutte»): a ogni giro leggi le domande nuove di `dati/verifiche/assistente-cruscotto-*/arrivi/` e delle caselle delle pagine di lezione; rispondi a TUTTE (regola 22, `docs/assistente/risposte/<pagina>.json`, Nome C.): prima quelle con la spunta «Priorità» del docente (messaggi di tipo `priorita` sul canale `docente-<classe>`), poi le altre in ordine di arrivo. Poi rigenera i file cifrati della linguetta «Domande dei ragazzi» con `python3 /home/user/corso-informatica-riservato/generatori/domande_cruscotto.py`, commit e push. Se la coda di una classe supera 5 domande, scrivi a Nicola in chat UNA riga: «In coda N domande: spunta nel cruscotto quelle con priorità». Valgono SOLO le domande del giorno (Nicola 28/10: «o si rispondono in giornata o non ha più senso tenerle»): quelle dei giorni prima senza risposta sono «chiuse», la chat della notte NON le riprende e non le conta come arretrato.

4. Linguetta «Script e ponte» (28/10/2026): a ogni giro `python3 /home/user/corso-informatica-riservato/generatori/stato_ponte.py --push` scrive anche il conteggio per ora (`per_ora`, solo numeri) usato dall'istogramma.

## 06 Ultimo passo obbligatorio: lo stato della notte

Alla fine del lavoro notturno, DOPO tutti i passi sopra e prima del messaggio del mattino al docente (28/10/2026, «controllore del controllore»):

1. Lancia il controllore dei controlli e copia nel file qui sotto la riga «ESITO» e le righe ROSSO; se è ROSSO, lo si dice al docente nella prima riga del messaggio del mattino (tranne il file della notte stessa, che si scrive al punto 2).

```
python3 /home/user/corso-informatica/strumenti/controlla_controlli.py
```

2. Scrivi nel riservato `stato/notte-<giorno>.json` (giorno = AAAA-MM-GG del giorno di lezione preparato) con questi campi: `ora` (ora di Roma in cui finisce il lavoro notturno), `regole_rilette` (file riletti e ultimo numero del registro degli errori letto, per esempio «#138»), `controlla_controlli` (riga ESITO e righe ROSSO del punto 1), `classi_preparate` (classi del giorno con il file del piano e l'esito di `verifica_lezione.py`), `problemi` (elenco di ciò che resta ROSSO o da fare; elenco vuoto se non c'è niente). Esempio:

```
{"ora": "06:58", "regole_rilette": {"file": ["CLAUDE.md", "MODUS-OPERANDI.md", "REGISTRO-ERRORI-CLAUDE.md", "CHECKLIST-LEZIONE.md", ".claude/passi-notturni.md"], "ultimo_errore": "#138"}, "controlla_controlli": ["ESITO: VERDE"], "classi_preparate": [{"classe": "2INF", "piano": "docs/cruscotto/piano/2inf-2026-10-29.json", "verifica_lezione": "GIALLO: DRAFT programmato"}], "problemi": []}
```

3. Commit e push del riservato (con il giro di tentativi di `RIPARTENZA.md` 02.2). Il controllore della notte dopo controlla che questo file ci sia.

## Changelog

1. v1.0 (28/10/2026): prima versione, dalla mappa regole-controlli.
2. v1.1 (28/10/2026 sera, audit): i passi 15-21 aggiunti dopo il changelog sono stati rimessi al loro posto (02.15; sezioni 04 e 05); nuovo passo 04.3 (orario delle lezioni per le pagine); nuova sezione 06, ultimo passo obbligatorio con `controlla_controlli.py` e `stato/notte-<giorno>.json`.
3. v1.2 (28/10/2026): passo 02.12 allineato alla regola 27 di `CLAUDE.md`: compito del mattino SENZA scadenza.
4. v1.3 (29/10/2026): passo 04.1, la quarta (4TI, martedì 3ª-5ª ora) è tra le classi a cui si preparano le 3 proposte.
