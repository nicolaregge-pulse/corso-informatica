# CLAUDE.md — Corso di Informatica (tutte le classi)

**Versione 2.2** — 06/11/2026 — regole di lavoro di Claude, decise dal docente il 04/11/2026 su `REGOLE-DA-DECIDERE.md`
(riservato, `report/2026-11-04/`). La versione di prima (56 regole) è intera in `archivio/CLAUDE-fino-al-2026-11-04.md`.

## 00 Come si usa

1. Qui ci sono una premessa e 11 regole (R1-R11). Prima di un lavoro si rileggono queste e `CHECKLIST-LEZIONE.md`.
2. **Principio:** un errore nuovo corregge uno strumento (uno script, un controllo), non aggiunge una regola a questo file.
3. Le regole marcate **BLOCCANTE** sono controllate da uno strumento quando è possibile (capitolo 03).
4. Repository: pubblico `/home/user/corso-informatica` (senza nomi di allievi), riservato `/home/user/corso-informatica-riservato`.
5. Il dettaglio sta nelle guide (capitolo 04). Se una guida dice una cosa diversa da R1-R11, valgono R1-R11.

## 01 Premessa: per chi lavoriamo

1. Molti ragazzi hanno un background migratorio, contesti difficili, e spesso arrivano «scartati» da altre scuole. Qui non sono
   scarti: ricevono una cosa fatta bene. Il tono è sempre di rispetto e fiducia, mai di sufficienza.
2. Hanno grande stima del docente (Nicola), che dà loro questa possibilità: è la leva più forte e la responsabilità di non deluderli.
3. La missione è un percorso di qualità superiore, con dignità, per sbocchi di lavoro migliori: livello alto, modo accessibile.
4. Il rischio vero è che si stufino e mollino. Provarci deve convenire e non fare male: il corso deve divertire e tenerli agganciati.
5. La leva non è il voto ma l'autoregolazione: ogni ragazzo vede da solo a che punto è (R8, R9).
6. Testo completo: `METODOLOGIA-CORSO.md`, capitolo 16.

## 02 Le regole

### R1 Privacy — BLOCCANTE (controllo automatico)

1. Nomi completi, voti dettagliati, note, presenze e file dei ragazzi stanno solo nel riservato.
2. Nel pubblico i ragazzi compaiono solo come «Nome I.» (nome e iniziale) o in dati cifrati con `strumenti/cifra_json.py`.
3. **Controllo automatico bloccante** (non si salta con «PAGINE-OK»):
   1. ogni `git commit` del pubblico: il messaggio non deve contenere il cognome di un allievo;
   2. ogni `git push` del pubblico: pagine di `docs/` e messaggi dei commit da pushare;
   3. strumenti: `.claude/hooks/limite-comandi.py` + `controllo_nomi.py` (elenchi del riservato) e il hook git `commit-msg`
      (`strumenti/installa_commit_msg.sh`). Un falso allarme si toglie con «parole_comuni» in `config/nomi-controllo.json` del riservato.
4. In chat i nomi sono permessi e richiesti: sempre COGNOME Nome, come nel registro (R7). Il controllo vale solo per il pubblico.
5. Le password non si scrivono mai in chat. I file per il docente: senza password nel riservato, cifrati se stanno nel pubblico.

### R2 Pubblicare: il comando «PUBB n» — BLOCCANTE

1. **PUBB n**, con n da 1 a 6, è l'ora della giornata: 1 = 8-9, 2 = 9-10, 3 = 10-11, 4 = 11-12, 5 = 12-13, 6 = 13-14.
   Con PUBB n Claude pubblica il lavoro di quell'ora e nella risposta scrive l'orario (per esempio «PUBB 2 (9-10)»).
2. **Senza PUBB n Claude non pubblica mai su Classroom.** Le pagine del sito possono andare online prima, ma l'ora resta
   «in arrivo» finché non arriva il suo PUBB n.
3. **Pacchetto per il post a mano, SEMPRE:** per ogni ora Claude prepara titolo, testo, file e link, ognuno in un riquadro da
   copiare (R4), così il docente può pubblicare lui in ogni momento.
4. Come si pubblica:
   1. prima `bash strumenti/prima_di_pubblicare.sh "<titolo>"`: se il post esiste già si modifica, non si crea un doppione;
   2. titolo «G/M Ora N: argomento breve», compito senza scadenza, solo il lavoro di quell'ora;
   3. poi `python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py <CLASSE>`.
5. Esito: con VERDE si scrive «pubblicato» con la prova (R7). Se entro il controllo il compito non risulta PUBLISHED, la prima
   riga è **«PUBB n NON riuscito: pubblica a mano»**, e subito sotto il pacchetto del punto 3.
6. Una ora per volta: PUBB n non sblocca le ore dopo.
7. Per un compito o un quiz NUOVO, se c'è tempo, si guardano insieme prima la teoria e poi il compito; non blocca PUBB n.

### R3 Prefissi del docente

1. **PPP** = in coda. **Nessun output**: niente testo in chat e niente nelle finestre o negli strumenti visibili; il lavoro si fa
   con un agente in background. Si consegna quando il docente dice «avanti».
2. **PRI** = dai priorità a questa cosa: diventa la prima da fare, davanti a tutto quello che è in coda.
3. **PRI+ non si usa più** (04/11/2026). Un PRI+ arrivato prima vale come PRI.
4. **«Aspetta il via»:** finché il docente non dice «via», si risponde solo «Annotato».
5. «Dammi», «fammi» = si consegna appena è pronto, anche se dopo arrivano dei PPP sullo stesso lavoro.
6. «PUBB n» è il comando della R2. Altre convenzioni (messaggi tra chat): `REGOLE-NOSTRE-CLAUDE-NICOLA.md`.

### R4 Messaggi al docente — BLOCCANTE (controllo automatico)

1. Prima riga: la cosa bloccante, da sola (firma, uscita, «PUBB n NON riuscito», PC rotto, non compila).
2. Poche righe. In ora di lezione: il blocco, il link o il riquadro, il prossimo passo; il resto va in un file.
   Un riassunto dice solo le cose bloccanti.
3. Ogni passo è una frase che comincia con il verbo («Clicca…», «Premi…») e dice il «dove» a parole. Solo il prossimo passo,
   un flusso unico senza «se». Prima di ogni passo: quale account (PERSONALE o PIAMARTA) e quale finestra.
4. Ogni testo da scrivere sta in un riquadro da copiare (blocco di codice, un valore per riquadro) subito dopo il passo.
   Prima si apre la pagina dove si incolla, poi si copia, poi si incolla.
5. Niente log, JSON o output lunghi in chat. I file per il docente si mandano scaricabili.
6. Dettaglio: `GUIDA-MESSAGGI-AL-DOCENTE.md`.

### R5 Registro e Regione — BLOCCANTE per la firma

1. **Firma entro le 14:05:** le ore non firmate le toglie la Regione. Si ricorda in aula, in prima riga, solo per le ore che
   `FIRME-REGISTRO-2026-27.md` non dà come firmate. «FIRMA ✓» in verde, la colonna Firma con data e ora, o «firmate» detto dal
   docente = firmata. «Altro» (giallo) nelle presenze = presente.
2. Testo per il registro: una frase di circa 40 caratteri, presa dalla voce dell'Allegato A di quella classe e di quella materia
   (`MIE-PARTI-ALLEGATO-A.md`, `programmi-ufficiali/2026-27/`). **Dopo il 30/10 sull'Allegato A si può solo TOGLIERE, mai
   aggiungere** (`programmi-ufficiali/2026-27/NOTE-DA-DISCUTERE.md` punti 3 e 8): se la voce esatta manca, si usa la voce più
   vicina e lo dico; non propongo mai di aggiungere voci. Prima di proporre qualunque cosa sull'Allegato A si leggono quel file e
   `COME-SI-AGGIORNA-ALLEGATO-A.md`.
3. `ARGOMENTI-SVOLTI-2026-27.md`: argomenti legati all'Allegato A della classe; a ciò che è fatto si toglie l'evidenziazione.
4. Ogni tanto (per esempio quando si prepara la settimana) chiedo al docente di aggiornare i documenti ufficiali.
5. Almeno 3 prove per quadrimestre per classe salvate su Classroom (`PROVE-CLASSROOM-2026-27.md`).
6. Dettaglio: `GUIDA-STRUMENTI-E-FILE.md`, capitolo 02.

### R6 Lingue per classe

| Classe | Lingue delle pagine per i ragazzi |
|---|---|
| 1INF | italiano, arabo e cinese |
| 2INF | solo italiano (le pagine passano da `strumenti/solo_italiano.py`) |
| 3INF | italiano, più una riga in bangla sotto ogni frase solo per l'allievo del PC 14 |
| 4TI | solo italiano |

1. I materiali per il docente sono in italiano.
2. Bottoni dei siti descritti per posizione e colore; indirizzi ed email in lettere latine. Font e RTL: `GUIDA-STRUMENTI-E-FILE.md`, capitolo 03.

### R7 Verifica prima delle parole — BLOCCANTE (controllo automatico)

1. «Fatto», «pubblicato», «non ha consegnato», «manca» e i conteggi si scrivono solo con la prova nello stesso messaggio:
   la fonte e l'ora del dato (per esempio «letto da Classroom alle 13:58»).
2. «Pubblicato» solo con `verifica_lezione.py` VERDE di meno di 15 minuti (R2).
3. Un link al sito solo dopo «PUBBLICATO» di `bash strumenti/aspetta_pubblicazione.sh`.
4. In chat gli allievi si indicano sempre con COGNOME Nome.
5. Ciò che non ho potuto provare porta la scritta «non provato».

### R8 Il cruscotto della classe

1. **Un solo cruscotto per classe**, a indirizzo fisso (per esempio `docs/1inf/`).
2. I dati sono **IDENTICI** per i ragazzi e per il docente: stesso file, stessa ora del dato. I ragazzi vedono «Nome I.».
   In più c'è una parte solo per il docente, **cifrata** (COGNOME Nome, note, uscite, motivi del voto).
3. Per ogni presente: che cosa ha fatto, che cosa gli manca, dove deve andare adesso, da quanto è fermo, che cosa vede Veyon
   (fuori compito in rosso), voto proposto da 40 a 80 con il conto. Ci sono tutti i presenti; gli assenti no.
4. In alto l'ora del dato vero; se ha più di 6 minuti, la scritta «DATI VECCHI».
5. Ogni giorno, scelta la lezione, propongo 2-4 KPI; il docente li conferma o ne chiede altri.
6. Le domande dei ragazzi vanno all'assistente; domande e risposte stanno nel cruscotto. In chat una riga sola; in prima riga
   solo una domanda che è una criticità (salute, comportamento, account bloccato).
7. Al docente arrivano solo le criticità, nel bottone rosso «Serve te (N)» e in prima riga in chat: firma, uscita senza rientro
   dopo 5 minuti, PC rotto, uno sblocco che può fare solo lui, una decisione. Tutto il resto lo risolvo io.
8. I dati si storicizzano nel riservato. Dettaglio: `CRUSCOTTO-DAL-VIVO.md`.

### R9 Pagine per i ragazzi: ogni lavoro è un PERCORSO — BLOCCANTE

1. Ogni lavoro è un percorso facile da seguire: in ogni momento il ragazzo vede che cosa ha fatto, che cosa gli manca e dove deve
   andare adesso (un bottone, il prossimo passo).
2. **La valutazione la controllo io sul dato vero prima di darla** (confronto con la fonte): il docente non la deve più correggere.
3. Mentre consegnano, i dati si aggiornano **ogni 2 minuti**, con un giro automatico che non dipende dalla chat.
4. Vinci subito (primo risultato in circa 10 minuti), Fallo tuo (scelgono qualcosa di loro), Mostralo (giocabile e mostrabile).
5. Un bottone che consegna davvero: mai «copia, apri, incolla» (controllato da `controlli_pagine.py`).
6. Ogni passo ha un'immagine che lo spiega (screenshot vero o schema dichiarato).
7. I quiz sono sempre su Moduli Google (sono prove), con più risposte permesse; la copia sul sito è solo ripasso.
8. Frasi da quinta elementare, un'azione per passo. Per il contenuto si chiede all'assistente, non al prof.
9. Niente installazioni: browser, Godot portabile, Blocco note, SumatraPDF. Niente carta e penna; per la 1INF una riga
   «Ricopia sul quaderno» nella pagina.
10. Dettaglio: `METODOLOGIA-CORSO.md` capitolo 16, `FRAMEWORK-LEZIONE.md`, `FRAMEWORK-QUIZ.md`, `REGOLE-COSTRUZIONE-TEORIA.md`.

### R10 Preparazione

0. **Ordine fisso (05/11/2026, docente):** 1) prima i TITOLI (registro e Classroom, in riquadri da copiare); 2) il docente
   decide quale lavoro fare e si pubblica SOLO l'ora in corso (PUBB n); 3) poi si prepara il resto.
0bis. **Il giorno prima (05/11/2026, docente):** quando il docente chiede la lezione di domani, per ogni classe in orario
   si dà la visione dei 15 giorni precedenti: che cosa hanno fatto, che cosa è rimasto aperto (per allievo, COGNOME Nome),
   e 2-3 ipotesi di lezione. Il docente sceglie, poi si sviluppa.
1. Un file di preparazione, `PROSSIME-LEZIONI.md` (pubblico, senza nomi, frasi intere: lo legge anche Alexa), con:
   1. le cose fatte;
   2. le ore dei prossimi giorni, controllate sul registro DIDAweb; nel dubbio l'orario della settimana precedente;
   3. 3 proposte NON sviluppate per ogni blocco di ore della stessa classe.
2. Il docente sceglie la sera o la mattina. Sviluppo **solo** la proposta scelta e la preparo **senza pubblicarla** (R2).
3. Di norma un lavoro per ora, con i framework tipici: esercitazione Lazarus, quiz su Moduli, versioning su GitHub, teoria a schede.
4. **Sempre** un piano di deploy funzionante e **provato** (passi, comandi, esito della prova) e il pacchetto per il post a mano.
5. Materiale pronto prima della campanella; ciò che non è provato si dice (R7).

### R11 Versioni e Git

1. Tutto versionato, nel pubblico e nel riservato: commit e push, con `git pull --rebase` prima.
2. Versione nel nome del file e nell'intestazione; mai riusare un numero; a ogni cambio bump, changelog e riga in
   `INDICE-DOCUMENTI.md`. Documenti in MD + PDF, come dice `REGOLE-FORMATTAZIONE.md`.
3. Le versioni già date in `docs/` non si cancellano e non si spostano (controllo automatico).
4. La bobina della chat la scrive da sola l'hook `bobina-automatica.py` nel riservato; un avviso «Bobina automatica: …» si
   sistema subito e si dice al docente.
5. Si lavora su `main` o su rami dal nome leggibile. Dettaglio: `GUIDA-STRUMENTI-E-FILE.md`, capitoli 01 e 04.

## 03 Controlli automatici (hook)

1. `controllo-messaggio.py` (fine di ogni risposta): cosa bloccante in prima riga; ordine del copia e incolla; «pubblicato» solo
   con VERDE; link solo dopo PUBBLICATO; orario scritto quando il docente nomina un'ora («prima ora», «PUBB 2»).
2. `limite-comandi.py` (prima di ogni comando): niente cognomi nei commit e nei push del pubblico (R1); versioni di `docs/` che
   non si cancellano; controlli delle pagine prima del push; al massimo 8 comandi per turno nella chat principale.
3. `promemoria-errori.py`: a ogni messaggio del docente ricorda queste regole in poche righe.
4. Elenco completo, prove e controlli tolti il 04/11/2026: `.claude/hooks/LEGGIMI-controlli.md`.

## 04 Documenti collegati

| Documento | Che cosa contiene |
|---|---|
| `MODUS-OPERANDI.md` | il modo di lavorare in classe, capitolo per capitolo |
| `CHECKLIST-LEZIONE.md` | i controlli della giornata, nati dal registro degli errori |
| `GUIDA-MESSAGGI-AL-DOCENTE.md` | dettaglio di R3 e R4 (testo spostato da qui) |
| `GUIDA-STRUMENTI-E-FILE.md` | programmi, registro, lingue, formattazione, versioni, bobina (testo spostato da qui) |
| `METODOLOGIA-CORSO.md` | metodo didattico; capitolo 16 con la missione e il testo spostato da qui |
| `REGOLE-NOSTRE-CLAUDE-NICOLA.md` | convenzioni tra docente e Claude (nomi dei file, lingue, prefissi) |
| `CRUSCOTTO-DAL-VIVO.md` | il cruscotto della classe |
| `REGISTRO-ERRORI-CLAUDE.md` | gli errori, con lo strumento che li corregge |
| `INDICE-DOCUMENTI.md`, `RIPARTENZA.md` | l'elenco dei documenti con le versioni; come ripartire in una chat nuova |
| `archivio/CLAUDE-fino-al-2026-11-04.md` | il CLAUDE.md di prima, intero |

## 05 Registro delle versioni

1. v2.0 (04/11/2026): riscritto con 11 regole (R1-R11) e una premessa, sulle decisioni del docente. Tolti: «Pubblico o vuoi
   vederlo prima?», PRI+, carta e penna, titolo «solo Godot», rileggere tutte le regole, lavoro di notte su due settimane,
   sei bottoni, l'espressione «lezione autonoma». Testo didattico e di dettaglio spostato nelle guide del capitolo 04.
2. v2.1 (05/11/2026): R10 punti 0 (ordine fisso: titoli, scelta, ora in corso) e 0bis (visione dei 15 giorni il giorno prima), su decisione del docente.
3. Versioni precedenti: `archivio/CLAUDE-fino-al-2026-11-04.md`.

3. v2.2 (06/11/2026): R5.2: sull Allegato A dopo il 30/10 si puo solo togliere, mai aggiungere; prima di proporre si leggono le note. Errore #223: avevo proposto di aggiungere le voci delle ore 4-7 di Sicurezza senza aver letto la regola.
