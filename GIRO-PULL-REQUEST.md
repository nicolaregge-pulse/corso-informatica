# Il giro delle Pull Request in classe

**Versione 1.0** — 12/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano. Area Docente.

Metodo provato con la 2INF il 12/10/2026: in tre ore i ragazzi hanno mandato più di 120 Pull Request (PR) e il gioco della classe è passato dalla versione 0.11 alla 0.31. Questo documento serve a rifarlo uguale, con qualunque classe e qualunque gioco.

## 00 Come funziona, in breve

1. I ragazzi leggono la teoria e mandano le loro richieste di modifica del gioco (PR) dal Modulo «Consegna».
2. Lo script «Consegne Classroom → Git» porta ogni invio nel repository riservato entro un minuto.
3. Claude legge ogni PR, la mette nel **backlog** con un riepilogo e un **peso**, la mette nel gioco come **versione nuova**, scrive il **changelog** e la segna **FATTO** (oppure **NO** con il motivo).
4. Quattro pagine pubbliche si aggiornano da sole ogni minuto: il backlog, i voti, il monitor della lezione, «Cosa è cambiato oggi nel gioco».
5. A fine lezione il docente riceve il PDF con la valutazione per allievo, una pagina per ragazzo.

## 01 Prima della lezione (una volta per classe)

| N. | Cosa | Chi | Dove |
|---|---|---|---|
| 1 | Il gioco della classe, con le versioni ferme e il controllo automatico | Claude | `docs/giochi/<gioco>/` con `versioni/` e `strumenti/controlla.py` |
| 2 | Il file delle impostazioni della lezione | Claude | repository riservato, `config/lezioni/<AAAAMMGG>_<CLASSE>.json` |
| 3 | La pagina del compito: teoria, poi i bottoni «1) Feedback» e «2) PR1», e in alto i quattro bottoni delle pagine | Claude | `docs/compito/<classe>-<data>-documento/` |
| 4 | Il Modulo Feedback sulla teoria (uno per classe) | Claude, con lo script | comando `forms.crea_modulo` |
| 5 | Il Modulo «Consegna» generico: è lo stesso per tutte le classi | già pronto | Google Moduli |
| 6 | Il Modulo Feedback nuovo dentro lo script (invio immediato) | Claude scrive il codice, il docente lo incolla | `AUTO_MODULI_LIVE` in `strumenti/automazione-corso.gs` |
| 7 | Il compito su Classroom con il link fisso della pagina | lo script | coda dei compiti |

> **Nota:** il file delle impostazioni contiene classe, data, ore della lezione (in ora UTC, cioè due ore in meno), le cartelle delle pagine, il gioco, i Moduli, l'elenco dei presenti e degli assenti, i computer (PC → nome e iniziale), le regole del voto e le decisioni del docente. Per una lezione nuova si copia quello di una lezione vecchia e si cambiano i campi.

## 02 Cosa fa il docente durante la lezione

1. Firma il registro subito, con il programma previsto (entro le 14:05).
2. Dice «pubblica» quando la pagina del compito va bene.
3. Se lo script è cambiato, lo ricopia dal link pubblico (vedi capitolo 06) ed esegue `attivaAutomatico` e `attivaInvioModuli`.
4. Fa i giri con Veyon e manda la schermata in chat: Claude la trascrive nel monitor (solo fatti, fuori compito in rosso).
5. Se vuole, decide lui su una PR («sì» o «no») o su un voto (per esempio: «ammettiamolo con 65»). Se dice «fai tu», decide Claude con le regole del capitolo 04.
6. A fine lezione dice a che ora congelare i voti.

## 03 Cosa fa Claude durante la lezione

1. Fa partire il giro automatico, che è UN solo processo e scrive su Git ogni minuto:

```
python3 generatori/lezione_pr.py 20261012_2INF giro 14:30
```

2. Per ogni PR nuova: la legge (anche i file allegati), scrive riepilogo, peso e motivo nel file dei pesi.
3. Mette in produzione le PR in ordine di backlog (peso più basso prima, a parità di peso chi è arrivato prima). Per ognuna: modifica il codice del gioco, lo prova nel browser, poi lancia:

```
python3 strumenti/rilascia_versione_pr.py 20261012_2INF v0.27 "Binari gialli" "PR di Nome I." '["riga 1","riga 2"]' '{"email|ora":{"fatto":"v0.27"}}'
```

4. Il comando fa tutto il giro: controllo automatico (se fallisce si ferma), changelog, versione ferma, FATTO nel backlog, pagina «Cosa è cambiato oggi», commit e push dei due repository. Il grafo delle versioni si aggiorna da solo.
5. Avvisa il docente in chat ogni poche versioni: numero, cosa cambia, chi l'ha chiesta.
6. A fine lezione: voti congelati e PDF della valutazione per allievo, mandato in chat:

```
python3 generatori/lezione_pr.py 20261012_2INF voti --pdf
```

## 04 Le regole del backlog

1. Ogni richiesta vale 1, chiunque la faccia.
2. **Peso** con i numeri di Fibonacci, cioè quanto lavoro sul codice: 1 testo o colore · 2 un numero · 3 un personaggio nuovo · 5 un ambiente o un oggetto nuovo · 8 una regola nuova del gioco · 13 una parte grande nuova.
3. **Ordine**: peso più basso prima; a parità di peso, chi è arrivato prima.
4. **FATTO** in verde, con la versione che l'ha portata nel gioco. «già fatto» se c'era già: non conta come PR eseguita.
5. **NO** in rosso, sempre con il motivo scritto per il ragazzo. Motivi usati:
   1. foto di una persona vera (privacy);
   2. musica o immagini con diritti d'autore;
   3. non dice cosa cambiare e dove: «riscrivila con Titolo, Cosa cambia, Dove, Perché»;
   4. doppione, o testo copiato dal backlog;
   5. c'è già nel gioco.
6. Nei giochi di scuola niente sangue: si propone un'alternativa (per esempio il cattivo che cade a terra).

## 05 Le regole del voto (proposta, il voto lo decide il docente)

1. Nessuna PR: 40. Assenti: nessun voto.
2. Da 1 a 4 PR: da 45 a 54.
3. Almeno 5 PR: 60, poi si sale; senza nessuna PR messa nel gioco il massimo è 70.
4. Oltre 70 serve almeno una PR messa nel gioco; contano anche le PR scritte bene con le 4 parti e il Feedback sulla teoria.
5. Non contano: i doppioni, le richieste che non dicono cosa cambiare, le foto di persone vere.
6. Le decisioni del docente vincono sul calcolo; nella pagina pubblica il motivo è solo «decisione del prof», quello vero resta nel riservato.

> **Da confermare:** quando i ragazzi scoprono che servono 5 PR, ne arrivano molte scritte in fretta o con l'intelligenza artificiale. La regola del «saperlo spiegare» resta: il docente può chiedere a voce di spiegare una PR.

## 06 Lo script e i Moduli

1. Il codice dello script si copia SEMPRE dal link pubblico, nella finestra PIAMARTA:

```
https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/strumenti/automazione-corso.gs
```

2. Il progetto si apre da `script.google.com/home` → «Consegne Classroom → Git». Ha 5 file: il codice va incollato in **automazione-corso.gs** (non in «Codice.gs», che si apre per primo).
3. Dopo aver incollato: Ctrl+S, poi «Esegui» su `attivaAutomatico` (giro ogni minuto) e su `attivaInvioModuli` (invio immediato dei Moduli).

## 07 Privacy e lingue

1. Pagine pubbliche: solo nome e iniziale. Nomi completi, voti dettagliati, note del docente, file dei ragazzi: solo nel repository riservato.
2. Mai foto di persone vere nel gioco.
3. Lingue della classe (2INF solo italiano; 1INF italiano, arabo, cinese; 3INF italiano e bengalese). Per le classi solo italiano ogni pagina passa da `strumenti/solo_italiano.py`, che blocca la pubblicazione se resta un'altra lingua.

## 08 Errori del 12/10 da non ripetere

| N. | Errore | Regola |
|---|---|---|
| 1 | Pagina della 2INF copiata dalla 3INF con il cinese dentro | `solo_italiano.py` blocca la pubblicazione (REGISTRO-ERRORI #49) |
| 2 | «Premi Ctrl+V» senza dire cosa c'è da incollare | la memoria del copia e incolla si considera vuota (#50) |
| 3 | «Incolla nel riquadro del codice» senza dire in quale file | le guide si scrivono sulla mappa vera dello schermo (#51) |
| 4 | Firma data per mancante guardando il bottone «FIRMA ✓» | il bottone c'è anche sulle ore firmate (#52) |
| 5 | Parole in più che confondono («onestamente», «valide») | se togliendo la parola il senso resta uguale, si toglie (#53) |
| 6 | Più giri automatici che scrivono su Git insieme: repository bloccato | un solo processo scrive (`lezione_pr.py giro`) |
| 7 | Giro automatico scaduto a metà lezione: backlog fermo | l'ora di fine del giro va oltre la fine della lezione |
| 8 | Prima PR messa nel gioco senza chiedere al docente | se il docente non dice «fai tu», si chiede «sì» o «no» |

## 09 Dove sta cosa

| Cosa | Dove |
|---|---|
| Impostazioni della lezione | riservato, `config/lezioni/<id>.json` |
| Giro automatico, backlog, file, voti, monitor | riservato, `generatori/lezione_pr.py` |
| Pesi e riepiloghi delle PR | riservato, il file indicato in `pesi` |
| Messa in produzione di una PR | pubblico, `strumenti/rilascia_versione_pr.py` |
| Pagina «Cosa è cambiato oggi» | pubblico, `strumenti/gen_novita.py` |
| Pagine per i ragazzi | pubblico, `docs/<classe>-backlog/`, `-voti/`, `-monitor/`, `-novita/` |
| Valutazione per allievo (PDF) | riservato, cartella indicata in `valutazioni` |

## 10 Registro delle versioni

1. **v1.0 (12/10/2026)**: prima versione, dalla lezione della 2INF del 12/10/2026.
