# Inventario degli strumenti e dell'automazione

**Versione 1.0** — 07/10/2026 · Area Docente · Prof. Nicola Regge, Centro Padre Piamarta, Milano

Fotografia di come abbiamo lavorato dal 25/09 al 07/10/2026: le modalità di lavoro, le piattaforme, chi fa cosa e, per ogni passaggio, che cosa è già automatico, che cosa è semiautomatico (serve un clic del docente) e che cosa resta a mano. Il file MD è la fonte (da dare anche a un'AI); il PDF è per la lettura. Nessun nome di allievo.

## 00 In breve

1. **Automatico** (lo fanno Claude e lo script, il docente dà solo l'OK): preparare pagine e dispense, pubblicare i compiti su Classroom, raccogliere le consegne, creare moduli e quiz, leggere le risposte, controllare i lavori su GitHub, fare libri, griglie, report e zip, aggiornare «Il mio punto».
2. **Semiautomatico** (pochi clic del docente): voti su DIDAweb con il segnalibro AUTO, voti su Classroom in bozza (il docente preme «Restituisci»), annunci (OK scritto del docente), aggiornamento dello script (incolla una volta).
3. **A mano** (decisione o presenza del docente): firma delle ore e presenze, Veyon (osservare, riavviare, aprire siti sui PC), pubblicazione dei voti alle famiglie, cancellazioni su Classroom, colloqui e «prova del nove» a voce, verifica dei casi dubbi (copiatura, AI, assenze).

> **Nota:** in 13 giorni di lezione: 32 compiti passati dalla coda dello script, 36 file di comandi al «ponte» Google (oltre 100 azioni), 40 generatori di documenti, 36 pagine del sito del corso, 64 errori registrati con la loro regola.

## 01 Le piattaforme

| Piattaforma | Account | A cosa serve | Chi la usa |
|---|---|---|---|
| Chat con Claude (sessione cloud) | PERSONALE | regia: comandi del docente, screenshot, documenti, controlli | docente + Claude |
| GitHub, repository pubblico + GitHub Pages | PERSONALE | sito del corso: pagine dei compiti, dispense, quiz, recupero, «Il mio punto», manuali | Claude scrive, ragazzi e docente leggono |
| GitHub, repository riservato | PERSONALE | voti, presenze, password, consegne, coda e comandi dello script | Claude e lo script |
| GitHub, account dei ragazzi | dei ragazzi | i loro repository e siti (Pages), commit dal browser | ragazzi; Claude controlla con git clone |
| Google Classroom | PIAMARTA | compiti, consegne, annunci, voti in bozza | script + docente |
| Google Drive, Documenti, Fogli | PIAMARTA | Documento personale di ogni compito, export PDF/TXT | script |
| Google Moduli | PIAMARTA | quiz con punteggio, moduli a risposta scritta (password del libro) | script |
| Gmail | PIAMARTA | solo bozze preparate dallo script; le invia il docente | docente |
| Apps Script «Consegne Classroom → Git» | PIAMARTA | lo script che collega Google e Git, ogni 5 minuti | automatico |
| DIDAweb (registro elettronico) | credenziali del docente | firma ore, argomenti, voti, annotazioni | docente + segnalibri |
| Chrome: segnalibri della cartella «DidaWeb» | PIAMARTA | programmi-segnalibro che leggono e scrivono la pagina di DIDAweb | docente (un clic) |
| Veyon | PC del docente | vedere gli schermi, riavviare, aprire siti sui PC degli allievi | docente |
| Lazarus, browser, Blocco note, SumatraPDF | PC dell'aula | strumenti dei ragazzi (niente installazioni) | ragazzi |
| NotebookLM, Gemini | PIAMARTA | AI per spiegare e tradurre il materiale (MD) | ragazzi e docente |

## 02 Le modalità di lavoro (come parliamo e come ci passiamo le cose)

1. **Comandi a voce o scritti del docente**: «avanti», «PPP» (parcheggia: preparo in silenzio, consegno all'«avanti»; «fammeli» vince sul PPP), «Chiudi classe», «VALUTAZIONE COMPLESSIVA classe», «situazione», «dammi …».
2. **Screenshot del docente** (Classroom, DIDAweb, Veyon, Apps Script): Claude li legge e indica il punto esatto; quelli di Veyon diventano il monitoraggio (solo fatti, con ora e PC).
3. **Passi a tabella** (07/10): N. · Account · Finestra / scheda · Dove · Cosa fare; una riga = una azione; solo il prossimo passo, senza ripetere quelli già fatti.
4. **Caselle da copiare**: un valore per casella, sempre nello stesso messaggio; tra copia e incolla niente screenshot (lo screenshot cancella gli appunti).
5. **Zona di scambio Git**: Claude scrive file nel repository riservato (`coda/`, `comandi/`), lo script li esegue e scrive lì i risultati; nessun copia-incolla del docente.
6. **Segnalibri-programma** su DIDAweb: il docente apre la pagina giusta e clicca; il programma fa il resto.
7. **Pagine per i ragazzi** sul sito: un'azione per passo, «devi vedere», «non mi torna», bottone Copia, tre lingue nelle consegne; «Il mio punto» personale con la password del libro.
8. **Documenti in doppio formato**: MD (fonte, per l'AI) + PDF versionato (lettura); libri dei ragazzi protetti da password.
9. **Promemoria programmati**: Claude si programma da solo i controlli (es. «ripresa dopo le lezioni», verifica di un annuncio).

## 03 Il giro di una lezione: automatico, semiautomatico, a mano

| Fase | Automatico | Semiautomatico (clic del docente) | A mano |
|---|---|---|---|
| Prima | dispense, pagina del compito, quiz, pagine di recupero, testi del registro corti | OK alla pubblicazione | firma delle ore (entro le 14:05), presenze |
| Avvio | compito su Classroom (script), annuncio di aiuto | OK all'annuncio | spiegazione, carta e penna |
| Durante | controlli ogni 5 minuti: consegne, commit su GitHub, password scelte; «Il mio punto» aggiornato | aprire una pagina su tutti i PC con Veyon («Apri sito web») | Veyon: osservare, richiamare, riavviare; aiuto a fianco |
| Fine ora | raccolta delle consegne (+10 min), libri protetti, report docente, zip | consegna dello zip su Classroom | messaggio alla classe |
| Dopo | voti proposti, report di monitoraggio, pacchetti per DIDAweb, aggiornamento libro di testo | voti su DIDAweb (segnalibro AUTO: classe/materia + clic + incolla + OK), voti Classroom in bozza («Restituisci») | decidere i voti finali e la pubblicazione alle famiglie, argomenti svolti |

## 04 Cosa si può fare in automatico, piattaforma per piattaforma

### 04.1 Classroom e Google (script + ponte)

1. **Sì, in automatico**: pubblicare compiti con Documento personale; raccogliere consegne (anche in ritardo); elencare compiti e consegne; creare quiz e moduli; leggere risposte e punteggi; cercare ed esportare file da Drive; creare e modificare Documenti e Fogli; voti in bozza sui compiti creati dallo script.
2. **Con l'OK del docente**: annunci; pubblicare il compito; restituire i voti ai ragazzi.
3. **No (per scelta di sicurezza)**: cancellare (bozze, compiti, annunci doppi: li toglie il docente), condividere fuori dalla scuola, inviare mail.
4. **No (limite di Classroom)**: modificare o mettere voti sui compiti creati a mano; vedere le bozze del docente dall'elenco.

### 04.2 GitHub

1. **Sì**: pubblicare il sito del corso; controllare i repository dei ragazzi (file, commit di oggi, «fallo tuo», Pages) con git clone; trovare un repository spostato.
2. **No**: entrare negli account dei ragazzi; creare per loro account o repository (lo fanno loro, con le pagine passo-passo).

### 04.3 DIDAweb

1. **Sì, con i segnalibri**: creare la colonna della lezione, scrivere voti e argomento, salvare dopo la conferma; se c'è un avviso non salva.
2. **Da costruire**: firma delle ore e argomenti (Registro → Oggi) con lo stesso metodo; coda di più pacchetti (classi e materie diverse, un clic per pagina).
3. **No**: entrare in DIDAweb al posto del docente (accesso e password restano suoi); pubblicare alle famiglie senza decisione del docente.

### 04.4 Veyon e aula

1. **No in automatico**: Claude non vede gli schermi; lavora sugli screenshot che manda il docente.
2. **Sì**: trasformare gli screenshot in monitoraggio ordinato, osservazioni nel voto (regola decisa dal docente), report per allievo con le immagini.

## 05 Lezioni imparate (dagli errori registrati)

1. A fine ora si consegna subito quello che c'è (bozza) e si aggiorna dopo: mai attese bloccanti; zip pronto 10 minuti prima della campanella.
2. Prima di nominare un materiale ai ragazzi si controlla che lo abbiano e si dice dove trovarlo.
3. Un annuncio in attesa: niente altro nel repository finché non è pubblicato (altrimenti esce due volte).
4. I nomi nelle liste per DIDAweb si scrivono come in DIDAweb; il segnalibro si ferma se un nome non torna.
5. Screenshot e appunti: lo screenshot cancella quello che si è copiato.
6. Account sempre dichiarato: PERSONALE (GitHub, chat) e PIAMARTA (DIDAweb, Classroom, script).
7. Lo script si aggiorna incollando il codice solo nel suo file; prossimo passo: caricatore automatico da GitHub.

## 06 Prossimi passi

1. Caricatore dello script: lo script scarica da solo la versione nuova (niente più incolla).
2. DIDAweb: firma delle ore e argomenti con segnalibro; coda di pacchetti su tutte le classi.
3. «Il mio punto» per tutte le classi, aggiornato da solo durante l'ora.
4. Manuale docenti: capitolo «Strumenti automatici: DIDAweb e Google» (v1.0 fatto) e questo inventario tenuti allineati.

## 07 Changelog

1. **v1.0 (07/10/2026)** — prima versione: piattaforme, modalità, giro della lezione, automatico/semiautomatico/a mano, lezioni imparate, prossimi passi.
