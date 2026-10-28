# RIPARTENZA — da qui riparte ogni chat nuova

**Versione 1.3** — 28/10/2026 · Area Docente · senza nomi di allievi · v1.3: punto 08.2.4, controllore dei controlli · v1.2: punto 08.2.3, passi notturni obbligatori · v1.1: sezione 08 «Stato al 28/10/2026 sera»; tolti i nomi dalle cose aperte del 21/10

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

1. Versione in uso dal 28/10/2026: **v8.4** (leva del ritmo dal cruscotto, vedi sezione 08). Prima: **v8.3 (27/10/2026)**: il giro ha un RITMO scelto dal docente o da Claude — `ritmo1` (ogni minuto, solo durante le consegne), `ritmo5` (ogni 5 minuti, il normale), `ritmo10` (lezione senza consegne), `disattivaAutomatico` (spento quando non c'è lezione); dal ponte l'azione `script.ritmo` con `minuti` 1, 5, 10 o 0. I comandi già letti non si rileggono (prima: centinaia di letture al minuto, limite di GitHub di 5.000 l'ora superato e limite di Google di 100.000 chiamate al giorno finito, REGISTRO-ERRORI #125). Contatori nel cruscotto (giri e chiamate di oggi, richieste GitHub rimaste e ora dell'azzeramento) da `?ping=1`. Claude archivia in `comandi/archivio/` i comandi eseguiti. Prima: **v8.1** (deployment Versione 3, 21/10/2026, ore 09:35): i segnali di avanzamento vanno solo nel Foglio, niente lucchetto; il giro gira ogni minuto. **v8.2 pronta su Git, da incollare e da pubblicare come nuova versione:** bozze (il docente vede, i ragazzi no), `classroom.mostra`, `classroom.programma`, `classroom.compito_modifica`, `classroom.annuncio_modifica`, `classroom.compito_cancella` (conferma «CANCELLA», si ferma se ci sono consegne), `classroom.voti`, `classroom.annunci`.
2. **Coda** `coda/*.json` (stato `da-pubblicare` → compito su Classroom) e **ponte** `comandi/*.json` (stato `da-eseguire`: `forms.crea_quiz`, `forms.risposte`, `drive.esporta`, `classroom.compiti`, `classroom.consegne`, `classroom.annuncio`, `classroom.annuncio_cancella`).
3. ID dei corsi: 1INF 877008807336 · 2INF 162656105584 · 3INF 25324574640 · 4TI 25324465949.
4. Foglio «Arrivi verifiche»: `1hpyJGHZpwDW7Y4ZwajtB_Qzr9AHc29Q_esgHr8NqJs8`.
5. **Se lo script è fermo:** piano B `docs/prof-pubblica/` (generatore `strumenti/gen_pianob.py AAAA-MM-GG`), piano C il testo da copiare. **Per aggiornare lo script, SEMPRE in questo ordine (REGISTRO-ERRORI #50, #57, #101: la seconda copia cancella la prima):** 1) Ctrl+T, `https://script.google.com/home`, progetto «Consegne Classroom → Git», file «automazione-corso.gs»; 2) Ctrl+T, il link pubblico `https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/strumenti/automazione-corso.gs`; 3) Ctrl+A, Ctrl+C; 4) tornare alla scheda di Apps Script, clic nel codice, Ctrl+A, Ctrl+V, Ctrl+S; 5) Esegui il deployment → Gestisci deployment → matita → Nuova versione → Esegui il deployment. Nessun riquadro da copiare tra il punto 3 e il punto 4.

## 04 Come si fa una lezione (deciso il 21/10)

1. **Su Classroom al massimo un compito e un annuncio per classe al giorno**; l'annuncio dice «OGGI FATE SOLO QUESTE COSE, IN QUESTO ORDINE» con i link diretti.
2. Teoria e ripasso sulla pagina `verifica/?b=<banca>` (motore unico, banche in `docs/verifica/banche/`); gli **esercizi valutati sono un quiz su Google Moduli** (traccia per la Regione) creato dal ponte con `forms.crea_quiz`.
3. Documento della lezione MD+PDF dalla banca: `python3 strumenti/banca2md.py <banca> <cartella> AAAAMMGG <Nome-Pdf> [passi…]`.
4. Prova come un ragazzo prima di pubblicare: `NODE_PATH=$(npm root -g) node strumenti/prova_verifica.js <banca>` (serve `cd docs && python3 -m http.server 8765`).
5. **Scadenze sulle campanelle vere:** 08:55 · 09:55 · 10:50 · intervallo · 11:10 · 12:05 · 13:05 · 14:00; la scadenza è la campanella dell'ultima ora della classe (REGISTRO-ERRORI #97).
6d. **«Pubblicare» vuol dire ANCHE Classroom (Nicola, 22/10/2026):** una lezione è pubblicata solo quando sono pubblicati la pagina sul sito E, su Classroom, il compito con la spiegazione e il link e l'annuncio «OGGI FATE SOLO QUESTE COSE». Mai dire «pubblicata» per la sola pagina.
6c. **TEMPI STRETTI, SEMPRE MISURATI (Nicola, 22/10/2026: «una cosa essenziale per ogni classe»):** mai tempi lunghi; ogni lavoro ha un tempo per ogni pezzo (10-15 minuti) e una scadenza vicina; a fine lezione si scrive nel diario quanto ci hanno messo davvero (primo, metà classe, ultimo) e la volta dopo si usa quel dato (REGISTRO-ERRORI #102).
6b. **Richieste bloccanti in ROSSO (Nicola, 21/10/2026):** in chat ogni cosa che blocca il lavoro e aspetta Nicola (un «pubblica», un clic, una conferma) si scrive con 🔴 e in grassetto, in cima o subito dopo il passo.
6. **Non si chiede più «pubblica» (Nicola, 21/10/2026, «a me sta storia che devo dire pubblica non piace tanto»):** Claude pubblica da solo e scrive sempre che cosa ha pubblicato con il link.
6e. **Lazarus su GitHub: un progetto = una sottocartella (Nicola, 22/10/2026):** ogni ragazzo ha UN repository «lazarus»; ogni progetto sta in una sua sottocartella con il nome del progetto (oggi «salvadanaio», poi i prossimi), che si carica intera trascinando la cartella (Add file → Upload files → Commit changes). Nella cartella principale del repository restano solo il README e le sottocartelle; i file che non c'entrano si tolgono. Controllo: `python3 generatori/lazarus_2inf_oggi.py <cartella>` nel riservato (accetta nomi quasi giusti e file sciolti, ma lo dice al ragazzo). Con Veyon il copia e incolla non funziona: i passi sui PC dei ragazzi usano testi brevi da scrivere a mano.
6f. **Cruscotto a COLONNE, una per attività (Nicola, 22/10/2026: «questa è più chiara»):** una riga per presente, una colonna per ogni attività della giornata nell'ordine in cui si fanno (teoria, programma, quiz, teoria 2, lavoro 2, quiz 2), ognuna con il suo voto 40-80 e le cose fatte ✔ / mancanti ○; «voto di oggi» = media dei voti delle attività − 3 per fuori compito, con il conto scritto; colonna «Monitoraggio». Docente cifrato `docs/avanzamento/git-2inf.html` (anche bagno e note), ragazzi `docs/2inf-oggi/` (Nome C., senza bagno e note). Generatore: riservato `generatori/cruscotto_git_2inf.py`. Il vecchio monitor a schede non lo capisce: non darlo più.
6a. Nicola ha detto «pubblica tutto, fai tu» il 21/10: si pubblica la sera prima o all'alba, in orario utile; si dice sempre cosa si è pubblicato.

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
4. Veyon: solo fatti, nel diario e nel cruscotto. **Se un riquadro non mostra il nome dell'utente (PC acceso con schermata di blocco, schermo blu, video, utente non indicato), CHIEDERE SUBITO a Nicola chi c'è** (Nicola, 21/10/2026): mai lasciare «utente non indicato».
5. **3INF, a ogni lezione (Nicola, 21/10):** si controllano TUTTI i siti dei ragazzi con `python3 generatori/lavori_3inf_oggi.py` nel riservato (giro ogni 3 minuti per tutta la lezione): file e nomi giusti, cartella img, sfondo, animazione, versione, rami, Pull Request, merge, commit del giorno. Gli utenti GitHub stanno in `config/3inf-github.json`; chi non c'è si aggiunge appena si vede il suo indirizzo.
6. A fine lezione: stringa per DIDAweb `GG/MM/AAAA h N | argomento | COGNOME NOME;voto …` con voti 40-80 = 40 + 40 × punti/massimo (leggere SEMPRE il massimo del quiz) e tutti i presenti.

## 07 Cose aperte (21/10) — storiche, lo stato attuale è nella sezione 08

1. 3INF del 21/10: dopo la lezione, il cruscotto dei siti dalla pagina «L'albero del mio sito».
2. 2INF giovedì 22/10: finire le interrogazioni sul WHILE (sorteggio di due).
3. 1INF prossima volta: il 21/10 si è arrivati fino al ping escluso; restano ping, jitter, lag e FPS, monitor, schede video e cavi video (slide dalla parte del gamer). Poi il percorso a sfide sul binario e la pixel art.
4. In 2INF e 3INF, quando hanno finito: i giochi dei byte della 1INF.
5. 2INF sicurezza: rileggere `classe-2/sicurezza-piano/PIANO-SICUREZZA-2INF.md` prima di ogni ora (ore n. 6-7 chiusura della formazione generale, dall'ora n. 8 i 12 argomenti del coordinatore).
6. Storico dei cruscotti: fotografia di fine lezione in `storico/cruscotti/<classe>/<data>/` del riservato (fatto il 21/10; da automatizzare a ogni giro).
7. Script v8.2 scritto il 21/10 (anche `classroom.voti` e `annuncio_cancella` con `annuncio_id` o `id`): manca solo che Nicola lo incolli e pubblichi la nuova versione.
8. 3INF: voti di Classroom del 21/10 da caricare con la v8.2; recupero individuale per due allievi (nomi nel riservato); un report individuale v1.1 da correggere (il repository esiste).
9. 2INF sicurezza: recupero dei quiz delle ore 1-4 (tabella nel riservato `dati/situazione/2INF_sicurezza-ore.md`); dall'ora n. 8 i 12 argomenti del coordinatore.
10. 1INF: compito di un'allieva del 20/10 non trovato in nessun Modulo né consegna (chiederle dove l'ha fatto).

## 08 Stato al 28/10/2026 sera

Una chat nuova riparte da qui senza chiedere niente al docente. Prima di tutto: regola 21 di `CLAUDE.md` (rileggere regole, `MODUS-OPERANDI.md`, `REGISTRO-ERRORI-CLAUDE.md`, `CHECKLIST-LEZIONE.md`).

1. **Script Apps Script v8.4** (`strumenti/automazione-corso.gs`).
   1.1. Il ritmo del giro si cambia dal cruscotto con la leva: indirizzo `?ritmo=N&k=<codice>`; la risposta è «Il cambio vale da subito».
   1.2. Ritmo consigliato: 5 minuti durante la lezione, 1 minuto durante le consegne, 10 minuti fuori lezione.
   1.3. Da «spento» solo Apps Script lo riaccende (la leva non basta): evitare di spegnerlo se non serve.
2. **Controlli automatici (hook)** in `.claude/hooks/`, spiegati in `.claude/hooks/LEGGIMI-controlli.md`.
   2.1. Se la sessione parte da `/home/user`, attivarli con `python3 /home/user/corso-informatica/.claude/hooks/attiva-controlli-home.py`.
   2.2. Il promemoria degli errori da non ripetere è `.claude/promemoria-errori.md`.
   2.3. **La Chat del giorno esegue TUTTI i passi di `.claude/passi-notturni.md`, in ordine, prima del messaggio del mattino** (audit delle regole, prove dei controlli, sito pubblicato, verifica di ogni classe, domande sì/no sulla lezione, promemoria a orario). Quale controllo copre ogni voce del registro: `MAPPA-REGOLE-CONTROLLI.md`.
   2.4. **Controllore dei controlli:** `python3 /home/user/corso-informatica/strumenti/controlla_controlli.py` dice in un colpo, una riga VERDE o ROSSO per controllo, se gli hook sono registrati (repository e /home/user), se le prove sono tutte «N/N», se i passi notturni si leggono e se la notte precedente ha lasciato `stato/notte-<giorno>.json` nel riservato (lo scrive l'ultimo passo dei passi notturni, sezione 06). Se dice ROSSO, si sistema prima di tutto il resto.
3. **Attività programmata «Chat del giorno»**: ogni lunedì-venerdì alle 6:47 parte una sessione nuova che prepara la giornata. La chat nuova del mattino è quella.
4. **Regole e registri nuovi.**
   4.1. Regola 23 di `CLAUDE.md`: in 1INF si dà sempre qualcosa da ricopiare sul quaderno, e lo si ricorda a ogni cambio di attività.
   4.2. Regola 24: un report PDF per ogni ora con gli screenshot di Veyon a piena risoluzione; solo nel riservato in `report/AAAA-MM-GG/`; script `generatori/report_ore.py` con `config/report-ore-AAAAMMGG.json`.
   4.3. Prima di ricordare una firma si legge `FIRME-REGISTRO-2026-27.md`.
   4.4. Il registro degli errori arriva al #138.
5. **Lezioni del 28/10 (fatte).**
   5.1. 1INF Lazarus «Ciao»: pagina `docs/verifica/?b=1inf-lazarus-ciao`, guida `docs/1inf-howto-progetto/`; tutti i progetti stanno nella cartella `Documenti\Lazarus`.
   5.2. 2INF sicurezza: recupero dei quiz delle ore 1-4 (`docs/2inf-sicurezza-recupero/`), monitor `docs/avanzamento/2inf-sicurezza-oggi.html`.
   5.3. 3INF Java: Eclipse portabile da zip, guida `docs/3inf-eclipse-guida/` v1.1; la consegna è spostata a giovedì 29/10 ore 13:00.
6. **Cose aperte che riguardano il docente** (chiederle UNA volta sola, quando servono).
   6.1. Voti 1INF del 28/10: ora tutti 80 provvisori, da confermare.
   6.2. Punti per i voti della 3INF.
   6.3. Conferma del piano B per pubblicare: annuncio pronto 10 minuti prima.
   6.4. Presenze 2INF del 28/10.
   6.5. PC 32 dell'aula 11: Lazarus 4.8 a metà installazione; va reinstallato fino in fondo, premendo «Ignora» sull'errore `Qt4Pas5.dll`.
   6.6. Facoltativa: richiesta su GitHub ad Anthropic per nascondere i riquadri.
7. **Cose aperte che fa Claude da solo.**
   7.1. Cruscotto: giorni passati, vista dell'allievo, grafico dell'uso dell'AI.
   7.2. Ripasso 3INF di giovedì.
   7.3. Lezioni di giovedì 29/10: vedi `PROSSIME-LEZIONI.md`.
