# Registro degli errori di Claude ("SBIRRO") — Corso Informatica

**Versione 2.81** — 26/10/2026 (#122 riallineato con il #97; CHECKLIST-LEZIONE)

*Registro onesto degli errori che Claude commette, giorno per giorno, con la correzione
adottata e la regola nata di conseguenza. Serve a non ripeterli e a migliorare. Lo tiene
aggiornato Claude su richiesta di Nicola: a ogni nuovo problema si aggiunge una voce con la
data. NON contiene nomi di allievi (quelli restano nel repo privato).*

---





## 26/10/2026 — 2INF: la casella dell'assistente ha scritto «Mandata!» e la domanda non è mai arrivata (#124)

1. **Errore.** Verso le 13:00 un ragazzo ha mandato una domanda all'assistente: la pagina gli ha scritto «Mandata! La risposta compare qui sotto entro qualche minuto», ma la domanda non è arrivata nel riservato. Il messaggio compariva subito, prima ancora di sapere se l'invio era partito. Durante la lezione io salvavo nel riservato ogni pochi minuti (uscite, Veyon, controllo dei repository): può essere la stessa collisione del #112.
2. **Regola.** «Mandata!» compare solo quando l'invio è partito davvero (corretto in `docs/assistente/assistente.js`). In lezione non salvo nel riservato più spesso del necessario. Se un ragazzo dice di aver scritto e la domanda non c'è, lo dico subito al docente e gli faccio rimandare la domanda.

## 26/10/2026 — 2INF: passo B troppo difficile, ragazzi sopravvalutati; domande all'assistente senza risposta (#123)

1. **Errore.** Il passo B chiedeva di trovare sul PC la cartella del primo programma, rinominarla e trascinarla su GitHub: alle 12:33 quasi tutti erano fermi lì e chiamavano il docente. Il docente: «te l'avevo già detto di fare le cose semplici, continui a sopravvalutare i ragazzi; devi pensarli come ragazzi di 12 anni». Due domande all'assistente (12:34 e 12:35, una era «non ho capito nulla») sono rimaste senza risposta finché il docente non ha chiesto il report.
2. **Regola.** Ogni passo è un'azione che si vede sullo schermo, pensata per un dodicenne; se il lavoro si può fare tutto su GitHub (spostare un file con la matita scrivendo «cartella/» davanti al nome) non si manda il ragazzo a cercare sul PC. Le domande all'assistente si leggono e si risolvono a ogni giro, e il report va al docente (CLAUDE.md regola 22).

## 26/10/2026 — 2INF: scadenza del compito inventata (#122)

1. **Errore.** Nel compito «OGGI: il mio GitHub in ordine» ho messo la consegna alle 13:45 senza che il docente l'avesse detta; era un lavoro di preparazione, che si spera di finire prima, non una consegna con l'ora. Con la scadenza lo script avrebbe anche chiuso il compito da solo dopo le 13:45.
2. **Regola.** La scadenza di un compito la decide il docente: se non l'ha detta, il compito si pubblica senza scadenza e senza chiusura automatica. Non si inventano orari, durate o voti che il docente non ha dato.
3. **Aggiornamento (26/10/2026, revisione degli errori).** Questa regola e il #97 dicevano due cose diverse. Vale: la scadenza la dice il docente; se non l'ha detta, si mette la campanella dell'ultima ora della classe e lo si scrive in chat (CHECKLIST-LEZIONE §02.3). Lo stesso giorno il docente ha fissato «scadenza h 14».

## 26/10/2026 — 2INF: due compiti su Classroom, il mio e quello del docente (#121)

1. **Errore.** Ho messo in coda il compito e l'annuncio senza guardare se su Classroom ci fosse già il compito della lezione: il docente l'aveva pubblicato alle 12:11 («Repository personale GitHub») e il mio è arrivato dopo, con lo stesso link. È lo stesso errore del #89 e del #107. Il docente: «Così non va bene»; ha dovuto cancellare il suo.
2. **Regola.** Prima di pubblicare un compito si leggono i compiti del giorno della classe (`classroom.compiti` dal ponte). Se ce n'è già uno con lo stesso link, non se ne crea un altro: si dà al docente il testo da aggiungere al suo.

## 26/10/2026 — 2INF: «pubblicata» detto di nuovo per la sola pagina, e una domanda invece di fare (#120)

1. **Errore.** Ho detto «la lezione è già pubblicata» per la pagina «Il mio GitHub in ordine», ma su Classroom non c'erano né il compito né l'annuncio: è lo stesso errore del #105. Prima di pubblicare non avevo riletto il registro degli errori e non avevo fatto passare la pagina dal controllo «solo italiano» (#49). Ho anche chiuso la risposta con una domanda («se lo volete fare oggi, aggiungo…») invece di farlo. Il docente: «Siamo rimasti d'accordo che pubblichi tu, rileggi i documenti e gli errori».
2. **Regola.** Prima di dire «pubblicata» controllo i tre pezzi: la pagina (con `solo_italiano.py` per la 2INF), il compito della coda con lo stato «PUBLISHED» e l'annuncio «OGGI FATE SOLO…» con il link. Li pubblico io (regola 17) e scrivo in chat che cosa manca finché non ci sono tutti e tre. Una cosa decisa dal docente in classe si prepara subito, senza chiederla di nuovo.

## 26/10/2026 — Teoria della 3INF fatta anche in arabo e cinese (#119)

1. **Errore.** Per la 3INF ho preparato la teoria «Object Pascal e Java» in italiano, arabo e cinese, copiando il modo di lavorare della 1INF. In 3INF le tre lingue non servono. Il docente: «siamo nella 3, perché mi dai queste lingue, continui a sbagliare».
2. **Secondo errore, subito dopo.** Correggendo, ho scritto «3INF solo italiano»: sbagliato anche questo. In MODUS-OPERANDI e FRAMEWORK-LEZIONE c'è scritto che in 3INF serve anche il bangla (bengalese) per l'allievo che ne ha bisogno, e il registro lo dice dal 05/10 (bangla solo sul PC 14). Il docente: «hai sbagliato ancora», «non chiederle a me, fai un audit tu».
3. **Regola.** Prima di preparare un materiale rileggo le regole sulle lingue nei documenti (MODUS-OPERANDI, FRAMEWORK-LEZIONE, questo registro): 1INF italiano, arabo, cinese; 2INF solo italiano; 3INF italiano + bangla per l'allievo che ne ha bisogno; 4TI italiano. Le regole le controllo io con un audit, non le chiedo al docente.

## 23/10/2026 — Pacchetto dei voti per DIDAweb senza dire quale Disciplina scegliere (#117)

1. **Errore.** Ho dato la riga dei voti della 5ª ora senza scrivere che la pagina di DIDAweb doveva essere su «LABORATORIO PROFESSIONALE»: era rimasta su Tecnologia (l'ora delle 8) e il segnalibro ha risposto «Nel registro non c'è la lezione del 23/10/2026 h 5». Il docente: «continui a fare audit ma continui a fare gli stessi errori».
2. **Regola.** Ogni pacchetto per DIDAweb ha SOPRA, in grassetto, la riga «Disciplina da scegliere: …» (la materia firmata in quell'ora sul registro), e il passo «scegli la Disciplina» è il primo della tabella.

## 23/10/2026 — Pagina dei ragazzi bloccata da un mio errore di scrittura (#118)

1. **Errore.** Aggiungendo l'avviso «POSSIBILE USO AI ECCESSIVO» alla pagina «La mia giornata» ho dimenticato un «+» nel codice: la pagina restava su «Carico…» per tutti i ragazzi finché il docente non l'ha segnalato («Non va più»). Avevo provato la pagina del docente ma non quella dei ragazzi.
2. **Regola.** Dopo ogni modifica a una pagina, prima di pubblicarla: controllo automatico della sintassi di TUTTI gli script della pagina (`node --check`) e prova della pagina vera in un browser, sia quella del docente sia quella dei ragazzi.

## 23/10/2026 — Ponte bloccato 22 minuti da un MIO comando troppo grande (#114)

1. **Errore.** Durante la lezione della 1INF ho mandato allo script un comando con 18 azioni (16 Documenti da esportare, ognuno con un salvataggio su GitHub). Lo script non lo ha finito: è rimasto «da eseguire» dalle 11:52 alle 12:14, e dietro di lui si sono fermati anche i comandi successivi. Per 22 minuti i cruscotti hanno mostrato dati vecchi; un ragazzo ha detto «ho fatto molto ma tu non vedi il mio lavoro», e aveva ragione. Il docente: «come mai si bloccano gli script, lo hai sistemato per 5 giorni di fila, detto risolto e alla fine continuano a bloccarsi».
2. **Regola.** Un comando del ponte = poche azioni e UN solo salvataggio (per leggere i Documenti si usa `docs.leggi`, che mette i testi nel risultato del comando, non `drive.esporta` uno per uno). Il giro controlla che ogni comando sia eseguito entro 5 minuti; se no, lo dice subito al docente, in rosso nel cruscotto, invece di aspettare in silenzio.

## 23/10/2026 — «Risolto» detto più volte per lo script, senza prova nel tempo (#115)

1. **Errore.** Negli ultimi giorni ho detto più volte che il blocco dello script era risolto. Ogni volta avevo corretto una causa sola (il timer di Google che si spegne, i miei salvataggi che si scontrano con i suoi, i comandi troppo lunghi), ma non le altre, e non l'ho misurato nei giorni dopo. Le cause sono almeno tre e si sommano.
2. **Regola.** Mai più «risolto» per lo script: si dice che cosa è cambiato, che cosa resta fragile e come lo si vede (battito dello script visibile nel cruscotto del docente). Si dichiara stabile solo dopo 5 giorni di lezione senza blocchi.

## 23/10/2026 — Voto per numero di parole senza difesa: un ragazzo ha scritto lettere a caso (#116)

1. **Errore.** Ho pubblicato il voto «+1 ogni 100 parole» senza filtrare le parole finte. Dopo pochi minuti un ragazzo ha riempito il Documento di «xcxc», «hahaha», «9g9g» per far salire il conto.
2. **Regola.** Ogni conteggio automatico che dà punti si protegge dagli abusi PRIMA di pubblicarlo (parole vere, tappe valide solo con il lavoro scritto, testo copiato o generato che non conta), e la regola si spiega ai ragazzi insieme al voto.

## 22/10/2026 — Le consegne dei ragazzi cadute per i MIEI salvataggi ogni 5 minuti (#112)

1. **Errore.** Il giro automatico spingeva i dati sul repository riservato ogni 5 minuti. Lo script di Google salva le consegne nello stesso repository: trovandolo occupato, il suo salvataggio falliva e la consegna restava solo nel Foglio di riserva, mentre la pagina diceva al ragazzo «arrivata al prof». In 3INF sono cadute 5 verifiche (Valerio, Domi, Dimalo, Catalano, Gervasoni), in 2INF 6. Il docente: «qualcosa non funziona nel tuo giro», «ogni giorno un tuo errore».
2. **Regola.** Durante la lezione i giri automatici NON spingono sul riservato: commit locali, push a fine ora. Ogni giro che legge le consegne controlla anche il Foglio di riserva (comando `drive.esporta` del Foglio «Arrivi verifiche») e recupera le righe «SOLO QUI». La pagina della verifica deve dire «arrivata» solo dopo la risposta vera dello script (da correggere nel motore).

## 22/10/2026 — Audit «Ponte OK» per deduzione, con il timer fermo da tre giorni (#104)

1. **Errore.** L'audit pre-lezione ha scritto «Ponte OK» senza una prova: il timer dello script era fermo dal pomeriggio del 21/10 e alle 08:40 niente era su Classroom. Il docente: «3 giorni che mi dici tutto ok poi non riesci a pubblicare».
2. **Regola.** «OK» si scrive solo dopo un comando di prova eseguito dallo script (file in `comandi/` passato a «eseguito» con l'ora). Se la prova non c'è, l'audit dice «NON VERIFICATO» in rosso e propone il piano B.

## 22/10/2026 — «Pubblicata» detto per la sola pagina, senza Classroom (#105)

1. **Errore.** Ho detto al docente che la lezione del salvadanaio era pubblicata quando era online solo la pagina del sito; su Classroom non c'era né il compito né l'annuncio («Non vedo niente su classroom»).
2. **Regola.** Pubblicare = pagina + compito + annuncio su Classroom (RIPARTENZA 6d). Finché manca uno dei tre si dice che cosa manca, mai «pubblicata».

## 22/10/2026 — Nome del bottone del piano B inventato (#106)

1. **Errore.** Ho scritto «Condividi su Classroom» mentre il bottone vero si chiama «1. Pubblica il COMPITO». Il docente: «ma ne fai UNA giusta?».
2. **Regola.** I nomi dei bottoni si copiano dalla pagina vera (o dallo screenshot), mai a memoria.

## 22/10/2026 — Annuncio vecchio lasciato e secondo annuncio in coda (#107)

1. **Errore.** L'annuncio delle 09:12 (in ritardo, con «entro le 9:15» e la consegna sbagliata) l'ho lasciato e ne ho messo in coda un secondo. Il docente: «doppie pubblicazioni creano solo problemi».
2. **Regola.** Un annuncio sbagliato si cancella o si corregge (`classroom.annuncio_cancella` / `annuncio_modifica`); su Classroom resta un solo annuncio e un solo compito al giorno per classe.

## 22/10/2026 — Monitor senza i presenti e con un nome falso; omonimi confusi (#108)

1. **Errore.** Nel monitor mancavano allievi presenti e c'era «xxx sddd»; il controllo Lazarus ha abbinato Khella con Aciobanitei (tutti e due Giorgio) e ha incluso un assente.
2. **Regola.** Nelle tabelle ci sono tutti e soli i presenti (Veyon o registro); l'abbinamento dei nomi si fa per cognome, mai per nome di battesimo.

## 22/10/2026 — «Fuori compito» segnato senza averlo verificato (#109)

1. **Errore.** Picco alle 09:05 (riquadro scuro «da verificare») e Acevedo alle 08:41 (scheda vuota) sono finiti nei messaggi ai ragazzi come «Veyon ti ha visto fuori lezione»; Elkeran alle 11:25 era una pubblicità a comparsa, non una pagina cercata da lui.
2. **Regola.** «Da verificare» non va mai nel pubblico. Fuori compito solo quando lo schermo mostra chiaramente un'altra attività; una pubblicità, una scheda vuota o uno schermo bloccato non lo sono.

## 22/10/2026 — Lezione GitHub troppo lunga, prima vittoria troppo tardi (#110)

1. **Errore.** 11 schede per 45 minuti, con i primi 5 passi su Esplora file che il controllo non vede: dopo 30 minuti nessuno aveva creato una cartella. Il docente: «o ci vuole più tempo, o è troppo difficile, oppure hai spiegato male».
2. **Regola.** Il primo passo di ogni lezione produce qualcosa di visibile nel controllo entro 10 minuti; i passi nell'editor del browser si fanno prima tutti insieme con la Demo di Veyon. La procedura facilitata nasce con la lezione, non dopo.

## 22/10/2026 — Due ritagli uguali nel report dei fatti (#111)

1. **Errore.** Nel PDF dei fatti su Uccheddu c'erano due immagini identiche (schermo bloccato alle 11:31 e 11:33). Il docente: «che senso ha mettere 2 immagini uguali?».
2. **Regola.** Prima di mettere due ritagli consecutivi si confrontano: se sono uguali ne resta uno con le due ore nella didascalia.

## 22/10/2026 — Richiesta «scrivi i tuoi errori nel file» rimandata a fine giornata (#113)

1. **Errore.** Alle 08:5x il docente ha chiesto tre cose, la terza era scrivere subito nel registro degli errori tutto ciò che non aveva funzionato. L'ho rimandata «a fine giornata»; alle 13:30: «hai visto il documento dei tuoi errori?».
2. **Regola.** Quando il docente chiede di registrare un errore, si scrive subito, prima di qualsiasi altro lavoro, e si dice il numero della voce.

## 21/10/2026 — Test di orientamento: risultati solo sul PC del ragazzo, inutilizzabili per il docente (#103)

1. **Errore:** ho letto «nessun dato raccolto» alla lettera e ho fatto un test i cui risultati restavano solo nel browser del ragazzo, con la stampa come unica uscita. Con la stampante guasta e gli utenti ospite, Nicola non ha potuto avere i tre PDF: io da qui non arrivo a quei PC. Nicola: «Ma come ti è venuto in mente di fare qualcosa non utilizzabile da me».
2. **Correzione:** PDF ricostruiti da Veyon (PC12 completo dall'anteprima di stampa, PC11 e PC13 con le fasce e i campi da scrivere a mano).
3. **Regola:** ogni pagina che produce un risultato deve farlo arrivare al docente, come tutte le altre pagine del corso (script delle consegne, riservato, cifrato); la stampa sul PC del ragazzo è solo una riserva. «Niente dati» vuol dire niente dati sul pubblico, non niente dati per il docente: nel dubbio si chiede prima.

## 21/10/2026 — Test di orientamento «di un'ora» finito in pochi minuti (#102)

1. **Errore:** ho dato al test di orientamento 60 minuti (10 + 15 + 20 + 10 + 5) senza misurare quanto tempo chiedono davvero le domande: 7 di logica, 8 di matematica, 4 livelli del robot e 6 domande, 7 frasi. Il primo ragazzo ha finito quasi subito. Nicola: «Avevo ragione io, non hai la minima idea dei tempi».
2. **Correzione:** a chi finisce si dà «Monta il PC» (`docs/monta-pc/`); la v1.1 avrà il doppio delle domande, 8 livelli del robot, una sfida extra e i minuti reali per blocco nella valutazione.
3. **Regola:** una durata si stima dal contenuto (circa 1 minuto per domanda a crocette, 2-3 minuti per livello del robot) e si controlla con una prova a tempo prima di darla; dopo ogni uso si confrontano i minuti reali con quelli previsti.

## 21/10/2026 — TERZA volta il #50: copiare il codice e poi copiare l'indirizzo di Apps Script (#101)

1. **Errore:** nei passi per lo script v8.2 ho fatto copiare il codice (passo 2) e poi l'indirizzo di Apps Script dal riquadro (passo 3): la seconda copia cancella la prima. Nicola se n'è accorto prima di incollare («Lo fai SEMPRE quell'errore»). È la terza volta (#50, #57).
2. **Causa:** in `RIPARTENZA.md` §03 la procedura era scritta nell'ordine sbagliato («codice dal link pubblico, Ctrl+A, Ctrl+V…») e la chat nuova l'ha ricopiata.
3. **Correzione:** passi rifatti nell'ordine giusto; Nicola ha incollato le 948 righe giuste.
4. **Regola:** la procedura per aggiornare lo script è scritta UNA volta, già nell'ordine giusto, in `RIPARTENZA.md` §03 punto 5: si ricopia da lì, mai a memoria. Ordine fisso: 1) aprire Apps Script e il file; 2) aprire il link del codice; 3) copiare; 4) tornare e incollare. Nessun riquadro da copiare tra una copia e il suo incolla.

## 21/10/2026 — PC senza nome lasciato come «utente non indicato» (#100)

1. **Errore:** nei giri di Veyon ho scritto «PC38: video di pugilato, utente non indicato» invece di chiedere chi c'era; era Elkeran.
2. **Correzione:** Nicola ha detto il nome; diario e configurazione aggiornati (PC38).
3. **Regola:** se un riquadro di Veyon non mostra il nome dell'utente, chiedo subito a Nicola chi c'è a quel PC (scritto in `RIPARTENZA.md` §06).

## 21/10/2026 — Lezione di sicurezza già vista dalla classe (#99)

1. **Errore:** per la 2INF ho preparato la 3ª ora della sicurezza (Regione) senza rileggere la storia della classe: il 16/10 la 3ª ora era già stata data con video e slide. I ragazzi: «il modulo 3 l'abbiamo già fatto».
2. **Correzione:** il quiz di oggi vale come verifica della 3ª ora (mai verificata); la prossima lezione di sicurezza è la 4ª ora.
3. **Regola:** prima di preparare una lezione si rileggono, per quella classe, gli annunci e i compiti degli ultimi giorni (`comandi/` e `coda/` del riservato) e `ARGOMENTI-SVOLTI-2026-27.md`; il punto di arrivo si scrive in `PROSSIME-LEZIONI.md`.

## 21/10/2026 — Stringa dei voti con la materia sbagliata (#98)

1. **Errore:** ho dato la stringa per DIDAweb con «h 1» senza dire la materia dell'ora: DIDAweb era su Tecnologia professionale, le ore della 1INF di mercoledì sono di Laboratorio professionale, e il segnalibro ha risposto «non c'è la lezione». Nicola: «Sbagli sempre qualcosa».
2. **Correzione:** il passo «Disciplina in alto → LABORATORIO PROFESSIONALE», poi la stessa stringa.
3. **Regola:** ogni stringa dei voti si dà con PRIMA il passo che sceglie classe e materia in alto in DIDAweb, letta da `orario/settimana-*.md` per quel giorno e quell'ora.

## 21/10/2026 — Scadenza del compito dopo la campanella (#97)

1. **Errore:** il quiz della 1INF è stato pubblicato con la consegna alle 10:58, ma la 3ª ora finisce alle 10:50 e poi c'è l'intervallo. Nicola l'ha cambiata a mano in 10:50.
2. **Correzione:** le scadenze si fissano SEMPRE sulle campanelle vere (RIFERIMENTI §1.10): 08:55 · 09:55 · 10:50 · intervallo · 11:10 · 12:05 · 13:05 · 14:00.
3. **Regola:** prima di pubblicare, controllo che la scadenza cada dentro l'ora giusta della classe, sulla campanella della sua ultima ora (es. 1INF 8-11 → 10:50; 2INF 11-12 → 12:05; 3INF 12-14 → 14:00).

## 21/10/2026 — Firma ricordata su ore già firmate (#96)

1. **Errore:** sulla schermata del registro le tre ore avevano «FIRMA ✓» in rosso e ho chiesto di firmarle; erano già firmate.
2. **Correzione:** Nicola ha mostrato l'elenco delle ore con la colonna «Firma» (data e ora della firma).
3. **Regola:** se nella colonna «Firma» dell'elenco c'è la data e l'ora, l'ora è firmata: non si ricorda più la firma per quell'ora.

## 20/10/2026 — Voti del quiz calcolati su 100 invece che su 70; quiz giusto non riconosciuto (#95)

1. **Errore:** nella 1INF ho calcolato i voti del quiz breve come se il massimo fosse 100, ma il quiz valeva 70 punti (14 domande da 5): tutti i voti erano troppo bassi. Me ne sono accorto solo dallo screenshot di Moduli di Nicola. Inoltre tre ragazzi che dicevano «l'ho fatto» avevano fatto il quiz da 20 domande del mattino, e io li avevo messi a 40. Il monitor, poi, non mostrava chi aveva consegnato senza aprire la pagina della lezione.
2. **Correzione:** voto = 40 + 40 × punti / massimo, leggendo SEMPRE la colonna «massimo»; letti tutti e due i quiz; monitor che mostra «✅ QUIZ CONSEGNATO» con il punteggio anche per chi non ha aperto la pagina.
3. **Regola:** prima di dare una stringa di voti si controllano il massimo di ogni quiz e tutti i quiz aperti per quella classe nel giorno; se un ragazzo dice «l'ho fatto», si cerca in tutti, mai rispondere «non risulta» su una sola fonte.

## 20/10/2026 — Lo stream di Classroom non dice cosa fare (#94)

1. **Errore:** nello stream della 1INF i lavori comparivano tutti come «Nicola Regge ha pubblicato un nuovo compito attraverso Consegne Classroom → Git…», uguali tra loro; a lezione cambiata (studio delle prime 5 pagine e quiz breve) i ragazzi non capivano quale aprire. Nicola: «Capisci che per loro non è facile capire cosa devono fare?».
2. **Correzione:** annuncio in cima allo stream con «OGGI FATE SOLO QUESTE 2 COSE, IN QUESTO ORDINE», i due link diretti e la riga nelle tre lingue (pubblicato da Nicola alle 13:42).
3. **Regola:** a ogni lezione, insieme ai compiti, un annuncio in cima allo stream con il titolo «OGGI FATE SOLO…», i passi numerati e i link diretti; ogni cambio di programma in classe = nuovo annuncio, mai solo a voce.

## 20/10/2026 — Quattro compiti in due posti, e il quiz uguale alla verifica (#93)

1. **Errore.** Per la 4TI e la 1INF ho pubblicato due compiti a testa su Classroom (la lezione e il quiz su Moduli) e il quiz aveva le stesse domande della verifica sulla pagina. Per i ragazzi era confuso: «la stessa domanda in due posti», e chi consegnava la verifica vuota leggeva «hai finito».
2. **Regola.** Un solo compito su Classroom per lezione, con un solo link alla pagina; il quiz su Moduli, se serve, ha domande diverse dalla verifica e sta dentro lo stesso compito. La pagina non deve dire «hai finito» quando le risposte scritte sono vuote.

## 20/10/2026 — «Altro» contato come non presente (#92)

1. **Errore.** Nelle presenze della 4TI ho contato 5 presenti, lasciando fuori un allievo segnato «Altro» sul registro.
2. **Regola.** «Altro» vuol dire entrata o uscita fuori orario: l'allievo è presente e si conta tra i presenti.

## 20/10/2026 — «Manca la voce ISO/OSI», e c'era (#91)

1. **Errore.** Per controllare i titoli del registro della 4TI ho guardato il vecchio `allegato-a-2026-27/allegato-a-classe-4.md` (v0.1) e ho detto che la voce ISO/OSI mancava. Nell'Allegato A vero del 14/10 (`programmi-ufficiali/2026-27/consegna/`) c'è, nella competenza 16, con le sotto-voci.
2. **Regola.** I titoli del registro si controllano SOLO sull'Allegato A più recente in `programmi-ufficiali/2026-27/consegna/` (il .docx), mai sui file v0.1 di `allegato-a-2026-27/`.

## 19/10/2026 — «Nessuna AI» su un PC che aveva Gemini aperto (#90)

1. **Errore.** Durante la verifica su Moduli della 2INF ho guardato la vista remota di un PC e ho scritto «nessuna AI visibile», controllando solo la finestra di Chrome in primo piano. Nella seconda finestra c'era Gemini con le soluzioni. Un minuto prima l'anteprima della barra di Windows mostrava già due finestre di Chrome.
2. **Regola.** Da una vista remota si dice «nessuna AI» solo dopo aver visto TUTTE le finestre di Chrome (anteprime sull'icona nella barra) e tutte le schede. Altrimenti si scrive «nella finestra in primo piano non si vede AI; le altre finestre non le ho viste».

## 19/10/2026 — Tre compiti uguali su Classroom (#89)

1. **Errore.** Ho messo il quiz in coda, poi l'ho dato per perso e ho fatto pubblicare a mano la versione completa. Il timer è ripartito per un momento e ha pubblicato anche la coda (senza poter scrivere su GitHub, quindi non lo vedevo); una prima esecuzione a mano ne ha fatto un terzo. Il docente ha dovuto cancellarne due.
2. **Regola.** Una sola strada per volta: prima di passare alla strada a mano, la voce in coda si annulla e si controlla su Classroom che non sia già uscita. Il titolo del compito resta lo stesso, così il controllo anti-doppione dello script lo riconosce.

## 19/10/2026 — «Lo script è vivo», e il battito era vecchio di 13 minuti (#88)

1. **Errore.** Alle 13:26 ho messo il quiz della 2INF in coda dicendo che lo script era vivo, guardando un battito delle 13:13: era già fermo da 13 minuti (di nuovo la quota giornaliera di Google, la v8.0 non è ancora installata). Il quiz non è uscito e il docente non ha visto niente.
2. **Regola.** Prima di dire «lo pubblica lo script» il battito deve avere meno di 3 minuti (MANIFESTO §9.12). Se è più vecchio, si dice subito e si usa la strada che non dipende dal timer.

## 19/10/2026 — Firma del registro: il verde voleva dire «firmata» (#87)

1. **Errore.** Davanti allo screenshot del registro della 2INF con «FIRMA ✓» in verde su tutte le ore ho scritto che non potevo capire se erano firmate e ho ricordato di firmare.
2. **Regola.** «FIRMA ✓» con la scritta in verde = ora firmata, è OK (Nicola). Si ricorda la firma solo per le ore senza il verde.

## 19/10/2026 — Lo script fermo dalle 04:07 e il compito non pubblicato (#82)

1. **Errore.** L'audit della sera del 18/10 non ha controllato che il timer dello script fosse vivo. Il timer si è fermato alle 04:07 (quota giornaliera di Google finita: lo script lavorava ogni minuto anche di notte) e alle 8:00 il compito della 3INF non era su Classroom: il docente l'ha messo a mano.
2. **Correzione.** Script v8.0: dorme fuori orario, legge solo la coda degli ultimi 7 giorni, scrive un battito. Il battito si controlla in ogni giro.
3. **Regola.** MANIFESTO §9.12: il battito dello script è una voce obbligatoria di ogni audit e di ogni giro.

## 19/10/2026 — «Ha già la pagina online», ed era di un altro (#83)

1. **Errore.** Da uno screenshot Veyon ho scritto che un allievo aveva già la pagina «Cosa so fare» online; nel suo repository non c'era. Un altro allievo diceva di avere il file e io dicevo di no: guardavo il suo vecchio account GitHub.
2. **Regola.** Quello che si vede in uno screenshot non è la prova: la prova è il file nel repository. Quando un ragazzo dice «c'è» e io no, si controlla subito tutto il suo repository e l'account con cui lavora oggi.

## 19/10/2026 — Link del cruscotto che davano 404 (#84)

1. **Errore.** Nel cruscotto ho messo il link alla pagina portfolio di tutti, anche di chi non l'aveva ancora creata: il docente cliccava e trovava 404.
2. **Regola.** Un link si mette solo se la pagina esiste davvero; altrimenti si scrive «pagina non ancora nel repository».

## 19/10/2026 — Nomi e voti in chiaro nel repository pubblico (#85)

1. **Errore.** Le copie del cruscotto (nomi interi, voti proposti, siti, giri Veyon) e il backlog della 3INF stavano in chiaro nel repository pubblico.
2. **Correzione.** I file del cruscotto sono cifrati (`strumenti/cifra_json.py`), il backlog usa «Nome I.». Le versioni vecchie restano nella storia di Git: per toglierle serve riscrivere la storia, solo con il sì del docente.
3. **Regola.** Ogni file con nomi interi o voti che finisce in `docs/` si scrive cifrato. Controllo prima del push: nessun cognome in chiaro nei JSON di `docs/`.

## 19/10/2026 — Due ore di giri in coda e la 2INF non seguita (#86)

1. **Errore.** Il giro automatico ogni 2 minuti si è accumulato in coda: per quasi due ore ho solo eseguito giri e non ho seguito l'inizio della 2INF né dato il pacchetto dei voti alle 10:44.
2. **Regola.** Finita una classe, il giro di quella classe si ferma subito. Il giro dura meno del suo intervallo; se arriva in ritardo, si salta.

## 01/10/2026 — Chiusura compito Classe 2INF (Convertitore temperature)

1. **Pacchetto unico con i dati di tutti (privacy).**
   - Cosa: ho consegnato un solo ZIP con dentro i libri di tutti gli allievi + la griglia con
     tutti i voti + il monitoraggio, **senza protezione**. Aperto lo ZIP, si vedevano tutti i
     file di tutti e i documenti riservati del docente.
   - Perché è sbagliato: i dati di un allievo non devono mai stare in un file accessibile agli
     altri; i documenti del docente non vanno mescolati a ciò che può arrivare ai ragazzi.
   - Correzione: ZIP unico **ma** con i libri **cifrati, una password per allievo**, e i
     documenti docente cifrati con una password docente. → RIFERIMENTI §2.14.

2. **"Valutazione del docente" non autorizzata.**
   - Cosa: nei libri degli allievi avevo messo una sezione "Valutazione del docente", mentre
     Nicola non li aveva valutati lui.
   - Perché è sbagliato: non si attribuisce al docente un giudizio che non ha dato.
   - Correzione: la valutazione la dà l'AI, intitolata **"Valutazione dell'AI"**. → RIFERIMENTI §2.15.

3. **Sovra-correzione: avevo tolto del tutto la valutazione.**
   - Cosa: dopo l'errore 2, avevo tolto voto e giudizio dai libri.
   - Perché è sbagliato: il ragazzo deve avere voto e giudizio (utili), solo attribuiti all'AI.
   - Correzione: rimessa la valutazione come "dell'AI". → RIFERIMENTI §2.15 (v1.9).

4. **Standard del compito incompleto (mancava l'anti-plagio e il report completo).**
   - Cosa: la prima chiusura non seguiva lo standard della Classe 3 (mancavano anti-plagio,
     dossier evidenze col testo reale, report complessivo a più sezioni) e usava voti /100.
   - Correzione: 5 documenti docente (scheda valutazione, dossier evidenze, report complessivo
     con anti-plagio + indicazioni ragazzi + segnalazioni, griglia, incrementale), voti **/10**.

5. **Frainteso il problema di privacy segnalato.**
   - Cosa: alla segnalazione "senza password tutti vedono tutto" ho risposto con opzioni
     tecniche invece di capire subito l'accordo mancato (separazione + attribuzione corretta).
   - Correzione: prima capire la regola mancata, poi agire.

6. **Anti-plagio troppo assertivo all'inizio.**
   - Cosa: avevo scritto "ha copiato" per screenshot/testi simili.
   - Perché è sbagliato: possono essere lo **stesso account su 2 PC**; va verificato.
   - Correzione: sempre al condizionale ("da verificare") finché non confermato.

7. **Contenuto del libro dell'allievo da delimitare.**
   - Cosa: rischio di mettere nel libro del ragazzo indicazioni pensate per il docente.
   - Correzione: nel libro va tutto ciò che riguarda **lui** (lavoro, valutazione AI, come ha
     lavorato/monitoraggio su di lui, anti-plagio su di lui), **tranne** le indicazioni
     specifiche per il docente (prossimo passo, strategia di recupero).

8. **Password casuali che cambiano a ogni rigenerazione.**
   - Cosa: avevo generato le password dei libri in modo **casuale**; rigenerando lo zip (per
     un'altra correzione) sono cambiate, diverse da quelle già consegnate agli allievi.
   - Perché è sbagliato: una password consegnata deve restare **stabile** per sempre.
   - Correzione: password **fisse** (hardcoded) nel generatore; non cambiano più a nessuna
     rigenerazione.

9. **Password messa anche sui documenti del docente.**
   - Cosa: avevo cifrato anche griglie/report del docente. Nicola non deve sbloccare i propri
     documenti.
   - Perché è sbagliato: la password serve solo a separare i libri tra allievi; i documenti del
     docente li legge lui, devono essere **aperti**.
   - Correzione: cifratura **solo** sui libri degli allievi; documenti docente aperti (incluso
     il foglio riepilogo password).

10. **Non ho versionato lo ZIP finale di chiusura.**
    - Cosa: ho generato il deliverable finale (lo ZIP di CHIUDI CLASSE 2INF) e l'ho consegnato
      senza metterlo su Git.
    - Perché è sbagliato: regola di Nicola "tutto versionato"; il deliverable finale va
      conservato com'è stato consegnato.
    - Correzione: lo ZIP di chiusura si **archivia nel repo PRIVATO** (`dati/chiusure/<CLASSE>/`,
      force oltre il `.gitignore`), perché contiene nomi → mai nel pubblico. → RIFERIMENTI §2.5.

11. **Proposto argomenti senza il report delle lezioni precedenti.**
    - Cosa: ho suggerito argomenti per la Classe 1 senza prima dare il quadro di **cosa era
      stato fatto** nelle lezioni precedenti.
    - Perché è sbagliato: le proposte vanno ancorate allo svolto; Nicola deve vedere prima il
      report del fatto.
    - Correzione: **sempre** prima il report "lezioni precedenti" (dal registro svolti), poi le
      proposte. → RIFERIMENTI §2.16.

12. **Introdotto un argomento NON spiegato in classe (direzione inversa).**
    - Cosa: nella dispensa bit/byte ho aggiunto **decimale→binario**, mentre in classe (lavagna)
      si era fatto **solo binario→decimale**. Può confondere i ragazzi.
    - Perché è sbagliato: il materiale deve seguire la lezione reale; introdurre argomenti nuovi
      di mia iniziativa non va bene ("se Nicola avesse voluto, lo avrebbe fatto alla lavagna").
    - Correzione: **integrare** sì, **introdurre argomenti nuovi** solo dopo **confronto**; nel
      dubbio chiedo. Inoltre: la **foto della lavagna** va dentro la dispensa di teoria.
      → RIFERIMENTI §2.17, §2.18, §7.

13. **Cancellato una versione invece di tenerla.**
    - Cosa: rifacendo la dispensa bit/byte, ho **rimosso** i PDF v1.0 sostituendoli con la v1.1.
    - Perché è sbagliato: le versioni sono **congelate** e si **tengono**; si **bumpa sempre**,
      non si cancella la precedente (regola di Nicola "aumenta sempre versione").
    - Correzione: ripristinata la v1.0; d'ora in poi le versioni si accumulano, non si eliminano.

## 01/10/2026 — Compito bit/byte (grafica diversa dalla dispensa)

14. **Grafica del compito DIVERSA dalla dispensa → ragazzi persi.**
    - Cosa: la dispensa usava la griglia a valori posizionali con gli 1 in verde; il compito
      l'avevo fatto con una **tabella diversa** (prima come Google Doc semplice, poi con una
      griglia solo "simile"). I ragazzi non hanno riconosciuto la stessa cosa e si sono persi.
    - Perché è sbagliato: materiali dello stesso argomento che i ragazzi vedono in sequenza devono
      avere la grafica **identica**, non "simile". Il cambio di grafica li confonde.
    - Correzione: compito rifatto con la griglia **identica** alla dispensa, **gestita come
      immagine** (PNG dalla stessa fonte → identica ovunque: PDF/Classroom/stampa), con **sotto lo
      spazio per i conti a mano**. Nasce la regola → RIFERIMENTI §2.19.

---

## 02/10/2026 — 1INF, pubblicazione del compito in classe

1. **Automazione spiegata a metà, scoperta in classe (GRAVE).** Il ponte provato era solo
   Classroom → Git; per PUBBLICARE (Git → Classroom) serve comunque uno script che parte
   dall'account scuola (un Esegui o un timer). Non l'ho detto quando abbiamo progettato il ponte:
   Nicola l'ha scoperto con 20 ragazzi in attesa, che hanno aspettato oltre 10 minuti.
   **Correzione:** (a) dire SUBITO i limiti di ciò che costruisco (cosa resta a Nicola); (b) il
   setup una tantum (timer) si fa FUORI dalla lezione, mai in classe; (c) in classe serve sempre
   una **via rapida pronta** (link/caselle per creare il compito a mano in 1 minuto), consegnata
   insieme ai materiali.
2. **Passi non "solo copia-incolla".** Il passo "apri il progetto Apps Script" era senza link.
   **Correzione:** ogni passo che apre un sito parte da un **link in una casella da copiare**.
3. **Via rapida senza il documento da compilare.** Nella pubblicazione a mano ho messo solo PDF
   (da leggere) e non il **Google Doc da compilare** ("una copia per ogni studente"), che invece c'era
   nello script automatico. I ragazzi non avevano dove scrivere. **Correzione:** ogni compito ha
   SEMPRE il documento da compilare allegato come copia per ogni allievo, in qualunque via di
   pubblicazione (automatica o a mano).
4. **Metodo alternativo introdotto ("metodo delle monete").** Per aiutare chi faticava ho proposto
   un secondo metodo invece di semplificare quello della lavagna: ha confuso i ragazzi. **Correzione:**
   ritirato (v1.0 tolte dal sito), rifatte facilissima / scheda facile / nome-colori v1.1 solo con le
   divisioni per 2. Regola → RIFERIMENTI §2.26.
5. **Orari delle campanelle persi.** Nicola li aveva dati in una sessione precedente; non li avevo
   salvati in un file, quindi ho fissato scadenze "a caso" (14:00, 13:00) e ho dovuto chiederli di
   nuovo in classe. **Correzione:** salvati in RIFERIMENTI §1.10 + `orario/Orario-Campanelle-v1.0.pdf`;
   ogni dato operativo che Nicola mi dà va scritto SUBITO in un file del repo.
6. **Troppe modifiche ai materiali DURANTE la lezione.** In un'ora: monete → divisioni, pagina
   con 4 → 2 → 6 → 12 → 4 bottoni, PDF v1.0 → v1.1 → v1.2 → v1.3 → v1.4. Ogni cambio ha spostato
   il terreno sotto i piedi dei ragazzi e di Nicola ("li hai confusi"). **Correzione:** durante la
   lezione si CONGELA ciò che è pubblicato; si corregge solo un errore bloccante, con UNA modifica
   ragionata, non a tentativi.
7. **Argomenti mescolati.** La scheda sulla divisione (Livello 3) parlava già di binario; ho poi
   proposto un compito unico "dalla divisione al binario". Nicola: "tieni distinti gli argomenti".
   **Correzione:** un argomento = una teoria + un compito; il ponte tra due argomenti è un compito
   a sé, dopo.
8. **Impaginazione non controllata prima di consegnare.** Tabella delle metà tagliata ai bordi,
   tabella del Livello 3 spezzata su due pagine, titoli orfani a fine pagina, "37" senza spiegazione
   di cosa fare. Nicola l'ha visto prima di me. **Correzione:** prima di pubblicare guardo OGNI
   pagina di OGNI lingua (render a immagine), non solo la prima.
9. **Link rotti nelle istruzioni di Classroom.** Ho tolto dal sito i PDF v1.0 che erano linkati
   direttamente nelle istruzioni del compito → link non funzionanti. **Correzione:** nelle istruzioni
   di Classroom SOLO il link unico della pagina (che non cambia mai); mai link diretti ai PDF versionati.
10. **Pagina vecchia rimasta nel browser.** Dopo le modifiche Nicola vedeva ancora la versione
    precedente (cache): ho dato per scontato che "ricaricare" bastasse. **Correzione:** versione
    scritta in copertina (riquadro bianco) + pagina senza cache + avviso esplicito "Ctrl+F5".
11. **Compiti vuoti pubblicati dallo script (GRAVE).** Ho messo in coda "aggancia il compito che
    creerà Nicola" PRIMA che lui lo creasse: lo script non lo ha trovato e ha pubblicato da solo
    "Compito 1" e "Compito 2" VUOTI, visibili ai ragazzi e non eliminabili dalla vista Stream.
    **Correzione:** si aggancia un compito manuale solo DOPO che Nicola conferma "creato"; lo script
    va dotato di uno stato "solo-aggancia" che non pubblica mai.
12. **Consiglio sbagliato: modificare un compito durante la lezione.** Sono stato IO a consigliare di
    trasformare i compiti vuoti modificandoli mentre i ragazzi lavoravano. Classroom ha spostato il
    Compito 2 in cima, sopra il Compito 1: i ragazzi hanno perso l'ordine. Non era da fare: bastava
    lasciarli stare e usarli DOPO, a fine lavoro sul Compito 1. **Correzione:** prima di
    far modificare un compito già pubblicato, avvisare che sale in cima e dare subito "Sposta in alto"
    per rimettere l'ordine (o usare un Argomento ordinato).
13. **Indicazioni imprecise su schermate e account.** "Elimina" dato per possibile dove non c'era
    (Stream), passaggi multipli in un solo messaggio quando Nicola chiedeva "una cosa per volta",
    dubbio sull'account (scuola/personale) gestito male. **Correzione:** UNA azione per messaggio
    quando la situazione è nuova; leggere lo screenshot e indicare il punto ESATTO di quella schermata.
14. **Chiave di correzione sovrascritta.** Rigenerando il compito v1.1 ho sovrascritto la chiave
    della v1.0 che i ragazzi stavano consegnando (rimessa a posto subito). **Correzione:** ogni chiave
    porta la versione nel nome del file; mai sovrascrivere la chiave di un compito in corso.
15. **Compito bit/byte v3.0 di ieri con esempio sbagliato** (griglia di 78, somma scritta
    "128+64+32+16 = 78"). Visto solo oggi. **Correzione:** controllo aritmetico automatico degli
    esempi (somma ricalcolata) prima di generare il PDF.

**Causa comune di oggi:** ho privilegiato la velocità e i tentativi rispetto alla verifica, e ho
cambiato materiale già in mano ai ragazzi. **Regola d'oro da qui in avanti:** *in classe niente
esperimenti: si pubblica una volta, verificato pagina per pagina; le migliorie si fanno dopo la
lezione.*

---

*(Le prossime giornate si aggiungono qui sotto con la loro data.)*

## 05/10/2026 — 3INF, istruzioni del compito su Classroom

1. **Errore:** ho dato a Nicola il testo delle istruzioni del compito come **un unico paragrafo lungo** (tutte le 5 parti in una riga). Su Classroom risulta un blocco illeggibile per i ragazzi ("formattazione pessima").
2. **Regola:** i testi da incollare su Classroom vanno **già impaginati**: titoletti in maiuscolo, una riga per passo, numeri 1. 2. 3., le parti del Documento una per riga, riga vuota tra i blocchi. Mai frasi lunghe con 1) 2) 3) in linea.
3. **Regola generale (chiesta da Nicola):** tutto ciò che Nicola segnala va qui **e** in una regola (RIFERIMENTI §2.28-2.29), per non rifarlo più.
4. **05/10, 08:45 — link rotto "2. Su internet" (scheda facile 2).** Passando alla v1.1 ho cancellato da `docs/` il PDF v1.0: chi aveva la pagina vecchia nel browser cliccava un link che non esisteva più. **Regola (RIFERIMENTI §2.31):** in `docs/` le versioni già usate in classe **non si cancellano mai** durante la giornata; la pagina punta alla nuova, la vecchia resta raggiungibile.
5. **05/10, 09:15 — allievo giudicato "fermo" dalla sola miniatura di Veyon.** Del PC 26 avevo detto "non ha iniziato" perché la miniatura mostrava la pagina del compito; in realtà il suo sito era già online. **Regola (RIFERIMENTI §2.32):** dalla miniatura si dice solo "sulla pagina X alle HH:MM", mai "non ha fatto niente"; prima di un giudizio si controllano le schede aperte e la pagina dei siti.
6. **05/10, 10:00 — risposte troppo lunghe durante la lezione.** Nicola deve seguire i ragazzi e non riesce a leggere tabelle e spiegazioni. **Regola (RIFERIMENTI §2.33):** in classe la risposta è SOLO (a) il testo aggiornato e completo del compito da incollare su Classroom, in un unico blocco copia, e (b) il link per il docente in un blocco copia. Niente tabelle o spiegazioni se non chieste.
7. **05/10, 10:05 — ho fatto preparare il Documento ai ragazzi.** Era deciso che la consegna (link, codice, screenshot) la preparo io leggendo il sito da GitHub. Io invece ho continuato a scrivere "metti nel Documento il link e il codice". **Regola (RIFERIMENTI §2.34):** quando un lavoro è su GitHub, la consegna la genera Claude (`generatori/siti_3inf.py`). Il ragazzo pubblica il sito, preme solo "Consegna" su Classroom e poi viene interrogato. Chi non ha il sito online deve arrivarci, oppure il docente detta il suo nome utente.
8. **05/10, 10:10 — bangla mostrato a tutti.** Il bangla serve solo all'allievo del PC 14; mostrarlo a tutti confonde gli altri. **Regola:** le traduzioni si mostrano solo a chi servono (pagina per PC: bangla solo sul PC 14). Per gli altri, la pagina resta solo in italiano.
9. **05/10, 10:05-10:02 — pagina "Controlla" rotta per un apostrofo.** Ho scritto "l'account" dentro una stringa JavaScript tra apici singoli: lo script non partiva e la lista restava vuota. Poi la cache del browser ha continuato a mostrare la versione rotta. **Regola:** dopo ogni modifica a una pagina con script, controllo la sintassi (`node --check`) e la provo nel browser prima di pubblicare. Al docente do il link con `?v=` e l'ora, così il browser non usa la pagina vecchia.
10. **05/10, 11:00 — nella pagina della 2INF c'erano anche i lavori dei giorni dopo.** La pagina linkata nel compito di oggi mostrava anche il quiz del 07/10 e il cassiere del cinema dell'08/10: troppa roba, i ragazzi si confondono. **Regola:** la pagina della classe mostra SOLO il lavoro del giorno. I materiali dei giorni dopo si preparano ma restano nascosti e compaiono solo il loro giorno.
11. **05/10, 11:36 — firma data per mancante.** Dallo screenshot del registro ho scambiato il bottone "FIRMA ✓" per una firma ancora da fare; Nicola aveva già firmato. **Regola:** su DIDAweb la prova è la casella "Visualizza tutte le firme arretrate": se il calendario non mostra giorni evidenziati, non manca nessuna firma. Prima di dire "manca la firma" chiedo di guardare lì, non deduco dal colore del bottone.
12. **05/10, 11:45 — file della coda rotto da un conflitto di Git.** Mentre lo script di Classroom salvava il suo stato, io ho riscritto lo stesso file: nel rebase sono rimasti i segni del conflitto e il JSON non si leggeva più, bloccando il giro dello script. Riparato in pochi minuti. **Regola:** dopo ogni rebase nel repo riservato controllo che tutti i `coda/*.json` si leggano (`json.load`) prima di pushare; nei conflitti sui file della coda riscrivo il file intero, non prendo un lato a caso.
13. **05/10, 11:50 — due compiti pubblicati insieme.** Ho messo su Classroom subito sia il primo lavoro (programma su GitHub) sia il secondo (Indovina il numero): i ragazzi non hanno capito quale fare per primo. **Regola (RIFERIMENTI §2.39):** su Classroom c'è UN solo compito aperto alla volta. Il secondo si prepara in coda e si pubblica solo quando Nicola dice che la classe ha finito il primo. Il titolo dice sempre l'ordine ("1 di 2", "2 di 2") e le istruzioni del secondo iniziano con "PRIMA finisci ...".
14. **05/10, 12:00 — istruzioni GitHub poco chiare e pagina rigenerata male.** Per pubblicare il programma Lazarus avevo scelto il copia-incolla del codice (Ctrl + A, Ctrl + C, Create new file): né Nicola né i ragazzi l'hanno capito; Nicola si aspettava il caricamento dei file da GitHub web. In più, rigenerando la pagina, il generatore ha rimesso in vista dispensa e compito degli if, che dovevano restare nascosti. **Regole:** 1) per caricare file su GitHub si usa il metodo standard **Add file → Upload files → choose your files**, salvo diversa indicazione di Nicola; nel dubbio si chiede PRIMA di scrivere i passi. 2) Dopo ogni rigenerazione di una pagina della classe si apre la pagina nel browser di prova e si controlla che si veda SOLO il lavoro di oggi (numero di riquadri) prima di pubblicare.
15. **05/10, 12:08 — istruzione "seleziona unit1.pas, unit1.lfm…" impossibile da seguire.** Sui PC della scuola Windows nasconde le estensioni: i ragazzi vedono due "unit1" e due "project1" e non sanno quali prendere. **Regola:** mai chiedere di riconoscere un file dall'estensione. Per scegliere più file si dà un bottone COPIA con i nomi tra virgolette (es. "unit1.pas" "unit1.lfm"), da incollare nella casella "Nome file" della finestra di Windows.
16. **05/10, 12:15 — "nessuno ha caricato" detto senza verificare bene.** Cercavo i lavori indovinando nomi utente e il nome esatto `lazarus`, e leggendo con raw (con cache): Picco aveva caricato in `lazarus-`, Castelletta e Moussa avevano caricato dopo il mio controllo. **Regola (RIFERIMENTI §2.40):** ricerca GitHub dei repository creati oggi + `git clone`; mai dire "non ha caricato" senza il clone.
17. **05/10, sera — file da scaricare poco chiari.** Ho mandato lo zip dei libri protetti intero (troppo grande, 31 MB) e poi le 2 parti: Nicola si è trovato 4 file senza sapere quali scaricare. **Regola:** se un file supera il limite, lo divido PRIMA e mando solo le parti; nel messaggio dico esattamente quali file scaricare e quanti sono.
18. **05/10, sera — voti di Indovina calcolati prima della raccolta dei Documenti e due errori nel correttore.** Ho chiuso la classe alle 13:51, prima della raccolta delle 13:56: mancavano i punti del Documento. In più il correttore abbinava il Documento per pezzo di cognome ("abdel" trovava anche Abdelfattah) e contava le domande del modello vuoto come risposte. **Regole:** 1) la chiusura si fa DOPO l'ultima raccolta delle consegne; 2) gli abbinamenti allievo ↔ file si fanno su parole intere di tutto il cognome; 3) dal Documento si conta solo il testo scritto dal ragazzo, tolte le righe del modello.
19. **06/10, 08:30 — «nessun guasto segnalato prima» detto senza la fonte giusta.** Per il PC 33 ho detto che non c'erano segnalazioni precedenti: in realtà era già nella segnalazione all'assistenza del 28-29/09, che non era salvata nel repository. **Regola:** tutte le segnalazioni all'assistenza si salvano nel repo riservato (`dati/manutenzione/`, con il registro dei guasti); prima di dire «mai segnalato» si controlla lì e, se manca qualcosa, si chiede al docente. A ogni lezione si verifica se i guasti aperti esistono ancora.
20. **06/10, 08:10-09:10 — lista «Cose da fare» pubblicata rotta.** Aggiungendo una voce ho sostituito il blocco dei dati con una ricerca automatica che ha preso anche il codice della pagina: la pagina non partiva più. **Regola:** quando si ripubblica una pagina che si salva da sola, il blocco dei dati si sostituisce una volta sola e in un punto preciso; prima di pubblicare si controlla il codice e si apre la pagina in un browser di prova.
21. **06/10, mattina — report dei voti trattenuto per un PPP.** Nicola aveva chiesto «dammi il report con tutte le valutazioni»; i messaggi PPP successivi ne precisavano il contenuto, ma io ho risposto «te lo do al tuo avanti». Nicola: «smettila con avanti, se ti dico di farmeli fammeli». **Regola (Regole nostre, PPP punti 5-6):** se un risultato è stato chiesto, il PPP successivo ne cambia solo il contenuto e il risultato si consegna appena è pronto; e un PPP non mi tiene mai fermo: se non sto facendo niente, vado avanti.
22. **06/10, mattina — doppioni nella griglia 1INF del 03/10.** Tre colonne erano lo stesso voto contato due volte (GitHub e repository = Ricerca GitHub, Il versioning = Quiz Regole + Versioning, Config. PC teoria = Esercizio Hardware) e mancava «Configurare un PC» del 24/09; il voto complessivo comunicato stamattina ne risente di qualche punto. **Regola:** prima di fare una media si controlla che ogni colonna sia un lavoro diverso (stesse cifre su tutta la classe = doppione) e si confronta l'elenco delle colonne con l'elenco dei compiti su Classroom.
23. **06/10, 09:30 — materia del voto scelta solo dall'ora.** Per DIDAweb ho assegnato il Quiz Regole + Versioning a Laboratorio perché era l'ora di Laboratorio; l'argomento (regole) è Sicurezza. Inoltre davo voti sotto 40. **Regola (RIFERIMENTI §2.44):** la materia si sceglie in base all'argomento realmente trattato; il voto minimo è 40.
24. **06/10, 12:20 — quiz su Moduli ancora da far partire a mano.** Nicola mi aveva chiesto giorni fa che anche i quiz su Moduli si creassero in automatico, come i compiti su Classroom; non l'avevo fatto e gli ho dato di nuovo uno script da eseguire. **Regola:** quando Nicola chiede di automatizzare un passaggio, l'automazione si costruisce subito nello script automatico (oggi: versione 4, quiz su Moduli con risultati depositati nel repo riservato) e si segna nell'elenco delle cose da fare; mai più passaggi a mano che si possono fare da soli.
25. **07/10, 08:50 — password dei libri 2INF diverse tra una chiusura e l'altra.** Per la 2INF esistevano due liste di password (quella del 25/09 e quella fissa del 01/10): i libri del 05/10 e la prima versione di quelli del 07/10 usavano la lista del 25/09, mentre l'elenco dato a Nicola era quello del 01/10, che in più non aveva 3 allievi. Nicola se n'è accorto perché un allievo risultava senza password. **Regole:** 1) per ogni classe c'è UNA sola lista di password, nel repo riservato (`strategico/password/`, file «Password-UNICA»), e tutti i generatori leggono solo quella; 2) prima di consegnare uno zip protetto si prova ad aprire OGNI libro con la password dell'elenco che ha Nicola; 3) a chi non ha ancora una password si prepara il bigliettino.
26. **07/10, 09:10 — nomi dei file dei libri che iniziano con la descrizione.** I libri si chiamavano «Libro-Tutti-i-Lavori_Cognome…»: su Classroom si vede solo l'inizio del nome del file, quindi i ragazzi vedevano tutti lo stesso «Libro-Tutti-i-Lavori_A…» senza capire quale fosse il loro. Nicola l'aveva già chiesto. **Regola:** ogni file personale di un ragazzo inizia con **Cognome-Nome**, poi classe, poi descrizione e data (es. «Cognome-Nome_2INF_Tutti-i-miei-lavori_07-10-2026.pdf»); vale per tutti i generatori.
27. **07/10, 12:15 — PDF delle password vuoto mandato senza controllo.** Il PDF dei bigliettini della 3INF conteneva solo la pagina di errore di Chrome (percorso del file sbagliato), e l'ho mandato senza aprirlo. **Regola:** ogni PDF si apre e si controlla il contenuto (testo atteso presente) PRIMA di mandarlo; il generatore dei PDF usa sempre percorsi assoluti.
28. **07/10, 12:00 — segnalibro DIDAweb provato solo su una pagina finta.** Due errori scoperti solo in classe: la finestrella di Chrome accetta una riga sola (la lista su più righe non funzionava) e su DIDAweb i nomi e le caselle stanno in tabelle separate. **Regola:** uno strumento per un sito esterno si costruisce partendo dall'HTML VERO della pagina (fatto copiare dal docente, salvato solo nel repo riservato) e si prova su quella copia prima di darlo a Nicola.
29. **07/10, 12:35 — link al repository riservato dato per il profilo «Scuola».** Lo stesso 404 del 06/10: nel profilo Chrome della scuola GitHub non è collegato. **Regola:** i link al repository riservato si danno SEMPRE con il passo «apri il profilo personale di Chrome» prima; mai un link nudo.
30. **07/10, 12:20 — lo stesso lavoro contato due volte (3INF).** «Pagina HTML» ed «Esercitazione pagina HTML» erano lo stesso lavoro in due caselle di Classroom: chi l'aveva consegnato in una risultava «non consegnato» (40) nell'altra. **Regola:** prima di una griglia si confrontano i compiti di Classroom tra loro (stesso argomento, stessa data, consegne complementari = stesso lavoro, una colonna sola con il voto migliore) e, per ogni «non consegnato», si controlla anche GitHub.
31. **07/10 — riferimenti a messaggi precedenti invece delle caselle da copiare.** Nicola: «devi darmi tutte le caselle per il copia e incolla senza farmele cercare». **Regola:** ogni messaggio con passi da fare contiene TUTTE le caselle da copiare che servono a quei passi, anche se già date prima.
32. **07/10, 12:40-12:55 — aggiornamento dello script con un flusso inutilizzabile (15 minuti persi).** Ho dato passi che facevano passare da un account all'altro e copiare un indirizzo DOPO aver copiato lo script (così gli appunti si perdevano); poi ho rimesso in chat tutto lo script (550 righe) invece di dire che era già negli appunti. **Regole:** 1) mai far copiare due cose in sequenza se la seconda cancella la prima: gli indirizzi si scrivono a mano o si aprono PRIMA di copiare; 2) prima di dare i passi si controlla cosa Nicola ha già (appunti, schede aperte) e si parte da lì; 3) lo script automatico si aggiorna da solo da GitHub (caricatore): Nicola non incolla più codice, dopo l'ultima volta.
33. **07/10, 13:00 — «la password del tuo libro» senza dire dove sta il libro (3INF).** L'annuncio e la pagina della password parlavano del «libro dei voti», ma i libri con le indicazioni personali erano solo nello zip del docente: non erano mai stati dati ai ragazzi, che hanno chiesto «dove sono le istruzioni personalizzate?». In più il «consiglio del prof» era una frase uguale per livello, non davvero personale. **Regole:** 1) prima di nominare un materiale in un testo per i ragazzi, si controlla che i ragazzi lo abbiano già e si scrive DOVE trovarlo (Classroom, quale compito o materiale); 2) la consegna dei libri ai ragazzi fa parte della chiusura (zip → Classroom) e va indicata a Nicola come passo esplicito; 3) le indicazioni «personalizzate» citano almeno una cosa concreta di quel ragazzo (un lavoro, un errore, un passo successivo).
34. **07/10, 12:55-13:00 — annuncio pubblicato DUE volte su Classroom (3INF).** Lo script ha pubblicato l'annuncio alle 12:55 ma non è riuscito a segnare «eseguito» nel repository, perché nello stesso momento io avevo spinto un altro file (lettura delle risposte): al giro dopo lo ha ripubblicato. **Regole:** 1) mentre un comando che PUBBLICA (annuncio, compito) è in attesa, non si spinge nient'altro nel repository riservato finché non risulta «eseguito»; 2) la sorveglianza automatica si ferma prima di un annuncio e riparte dopo; 3) da fare nello script: prima di pubblicare un annuncio, controllare se ce n'è già uno con lo stesso testo (come già fa per i compiti).
35. **07/10, 13:52-14:01 — zip per i ragazzi non consegnato prima della campanella (3INF).** Nicola ha chiesto lo zip alle 13:52; io ho aspettato bloccato fino a 9 minuti la raccolta automatica dello script per avere gli screenshot, senza dare niente nel frattempo e senza leggere i suoi messaggi («sono 13:57», «2 minuti»). Risultato: classe finita senza zip. **Regole:** 1) a fine ora si consegna SUBITO quello che c'è (bozza con i dati disponibili, segnata come bozza) e si aggiorna dopo; 2) mai attese bloccanti di più di 1 minuto durante la lezione: le attese vanno in background; 3) lo zip per i ragazzi è pronto 10 minuti prima della campanella (per l'ultima ora: alle 13:50), con i dati di quel momento.
36. **07/10, 16:30 — RIPETIZIONE dell'errore 11: firma data per mancante dal bottone «FIRMA ✓» (3INF).** Leggendo l'HTML del Registro di corso ho scritto a Nicola che le ore 5 e 6 «non risultavano firmate» perché c'era il bottone «Firma ✔»; Nicola le aveva firmate in classe. Il bottone resta anche sulle ore firmate (serve a rifirmare dopo aver cambiato l'argomento). In più il segnalibro «Firma registro» v1.0 usava proprio la presenza del bottone per capire se un'ora era firmata. **Regole:** 1) prima di dire qualcosa sulle firme si rilegge la regola 11: la prova è «Visualizza tutte le firme arretrate» o «Da firmare», mai il bottone; 2) uno strumento che deve riconoscere uno stato (firmato / non firmato) si costruisce con un esempio VERO di ENTRAMBI gli stati, chiesto al docente prima di consegnarlo; 3) il segnalibro non decide da solo che un'ora è «da firmare»: mostra lo stato che legge e chiede conferma.
37. **08/10, 09:21 — «lo script è fermo» detto senza prova (2INF).** Nessun commit dello script da ieri alle 14:02 e il compito non ancora su Classroom: ho concluso che lo script era fermo e ho fatto segnare il compito «da creare a mano», togliendolo alla coda. In realtà lo script non aveva niente da fare (i compiti di oggi erano in attesa dell'OK) e il compito era in coda da meno di un giro (5 minuti); rimesso in coda, è uscito alle 09:25. Risultato: 5 minuti persi e rischio di compito doppio. **Regole:** 1) prima di dire che lo script è fermo si manda un comando di prova (`classroom.compiti`) e si aspetta un giro intero (5-6 minuti); 2) un compito in coda non si toglie dalla coda finché la prova non dice che lo script è fermo; 3) al docente si dice subito «esce entro 5 minuti», non «non funziona».

## 08/10/2026 — 2INF, «Il treno blindato»: per un'ora e mezza quasi nessuno ha consegnato (#38)

1. **Cosa è successo.** Fino alle 10:10 le consegne erano zero; la prima consegna vera è arrivata dopo l'annuncio degli investitori, quasi tutti hanno consegnato solo con il compito «idea e difetto» delle 10:35.
2. **Errori miei.**
   1. Ho mescolato due canali: le pagine spiegavano fork e Pull Request vere su GitHub, il compito chiedeva le consegne su Classroom. I ragazzi non sapevano dove consegnare.
   2. Ho fatto consegnare solo il capo squadra: tutti gli altri non avevano un lavoro da consegnare e si sono fermati.
   3. Il primo lavoro obbligatorio con un orario è arrivato tardi; prima c'erano solo «lavori da fare» senza scadenza.
   4. Ho aperto troppi canali (due moduli, pagine, annunci): i moduli hanno avuto zero risposte.
   5. Ho letto i Documenti tardi: all'inizio aspettavo il bottone «Consegna».
3. **Regola (vale da oggi, per tutte le classi).** In un progetto di squadra: (1) un solo canale, il Documento del compito su Classroom; (2) ogni punto del Documento è una Pull Request che Claude legge, integra e pubblica come versione nuova; (3) TUTTI consegnano, ognuno nel suo Documento, con fasi a orario (una ogni 20-25 minuti) e una frase da completare già scritta; (4) la prima fase scade entro 20 minuti dall'inizio; (5) Claude legge i Documenti ogni 5 minuti fin dall'inizio, anche senza «Consegna», e pubblica i numeri di PC che non hanno ancora consegnato; (6) niente GitHub per i ragazzi se non è il lavoro del giorno.

## 08/10/2026 — 3INF, «Il treno blindato della 3INF»: errori in classe (#39)

1. **Orari sbagliati.** Ho scritto le fasi a partire dalle 11:20 senza controllare l'ora vera (erano le 12:00): ho dovuto rifare gli orari tre volte (12:05-13:50, poi fino alle 13:30, poi fino alle 13:05). Regola: prima di scrivere un orario per i ragazzi si chiede l'ora di fine al docente e si parte dall'ora di adesso.
2. **Istruzioni troppo lunghe e poco chiare.** La prima versione spiegava tutto (Pull Request, fasi, voto) ma non diceva COSA fare e COME in un passo solo: i team non hanno capito. Regola: la pagina per i ragazzi mostra una sola cosa da fare adesso, con passi numerati da ragazzi delle medie, la riga già pronta e il bottone COPIA.
3. **La PR-3 non era spiegata.** «Un difetto nella versione nuova» non diceva cosa fare: tutti hanno chiesto. Regola: ogni fase ha un esempio completo e il link a quello che serve (qui: apri il gioco, fai 1 partita, scrivi UNA cosa che non va).
4. **Lavori per PC con i numeri vecchi.** Ho diviso il lavoro per numero di PC usando la foto Veyon delle 12:08; alle 12:26 molti avevano cambiato PC. Regola: prima di assegnare un lavoro per PC si controlla l'ultima foto Veyon; meglio assegnare per nome (nel Documento personale) e usare il PC solo come aiuto.
5. **Modifiche alla pagina non verificate.** Due sostituzioni nel codice della pagina non sono andate a segno (il testo da sostituire non c'era) e me ne sono accorto dopo. Regola: dopo ogni modifica si controlla che il cambiamento ci sia (ricerca nel file o schermata) prima di dire che è fatto.
6. **«Consegna» non spiegata all'inizio.** Due ragazzi hanno premuto «Consegna» e il Documento si è bloccato. Regola: nel testo del compito, fin dall'inizio, «non premere Consegna fino alla fine; se l'hai premuto, premi Annulla consegna».
7. **Pull Request copiate tra compagni.** Tre ragazzi della stessa squadra hanno consegnato lo stesso cattivo. Regola: ogni PR-1 deve essere diversa; le copie si accettano una volta sola e si segnalano.
8. **Nomi nei report.** La regola del corso vieta i nomi dei minori nelle pagine pubbliche; il docente li ha chiesti. Soluzione adottata: report pubblico per numero di PC, nomi visibili solo con la password della classe (cifrati nel repository).

## 08/10/2026 — 3INF, report pubblicato senza nomi leggibili (#40)

1. **Cosa è successo.** Il report della 3INF mostrava «scrivi la password» al posto del nome: il docente non poteva capire a colpo d'occhio di chi fosse ogni riga, quindi il report non serviva in classe.
2. **Correzione.** Nel report ora si vede subito il nome di battesimo; il cognome resta nel report completo del repository privato.
3. **Regola (vale da oggi, per tutte le classi).** Non si pubblica MAI un report, un elenco o una pagina di valutazione che il docente non possa attribuire in modo semplice e immediato a ogni allievo: ogni riga porta almeno il nome di battesimo visibile (mai solo il numero di PC, mai nomi nascosti dietro una password).

## 09/10/2026 — 2INF, Sicurezza 2ª ora: quiz e domande aperte (#41)

1. **Ho pubblicato senza il via del docente.** Alle 08:36 ho fatto uscire il compito del quiz pensando che «ultimi 25 minuti» fosse già il via; il docente ha scritto «aspetta a pubblicare» mentre il ponte lo stava pubblicando. Regola: quando il docente dice «prepara e fammelo vedere», si prepara e si aspetta la parola «pubblica»; un orario detto prima non vale come via.
2. **Non ho capito subito il formato.** Il docente voleva UN Modulo Google con: 15-20 domande di quiz, 5 domande aperte sulle parole della lezione (pericolo, esposizione, rischio, infortunio, incidente) e 1-2 domande sul phishing con l'esercizio. Ho fatto prima un compito con Documento e «carta e penna», poi un Modulo con sole domande aperte e il quiz fuori, poi un secondo Modulo solo a crocette: tre giri e due link invece di uno. Regola: prima di creare, riscrivo in una riga il formato richiesto (dove, quante domande, di che tipo, in che ordine) e lo faccio confermare.
3. **Strumento non adatto.** Il ponte crea Moduli o solo a crocette (`forms.crea_quiz`) o solo con domande aperte (`forms.crea_modulo`), non misti. Regola: per un Modulo misto serve un'azione nuova del ponte (crocette + aperte + sezioni); finché non c'è, lo si dice subito al docente invece di dividere in due Moduli senza avvisare.
4. **Carta e penna al posto sbagliato.** Nell'annuncio di studio ho chiesto di scrivere sul foglio quello che il docente voleva sul Modulo. Regola: dove si scrivono le risposte lo decide il docente; non lo aggiungo io.
5. **Lingue.** Ho messo il cinese anche dove il docente voleva solo l'italiano. Regola: per la 2INF chiedere o seguire l'ultima indicazione («tutto in italiano»).

## 09/10/2026 — Impianto delle consegne: proposto Classroom come cassetta (#42)

1. **Errore.** Ho proposto di usare il compito di Classroom per consegnare testo e file, pur sapendo dall'08/10 (3INF) che per aggiungere un file dopo la consegna bisogna «Annullare la consegna» e riconsegnare: con più file in momenti diversi non è fattibile.
2. **Regola.** Le consegne si fanno da un canale che accetta invii ripetuti senza ritirare niente: Modulo Google a risposte multiple (testo + carica file) oppure la pagina del compito collegata a uno script Google. Su Classroom si preme solo «Consegnato» alla fine.

## 09/10/2026 — 1INF, «Versioni e Git»: compito sbagliato di target (#43)

1. **Errore.** Ho dato alla 1INF cinque attività (A1-A5) scritte con un italiano da scuola media: giocare due versioni e trovare le differenze, 8 definizioni con parole proprie, cercare il numero di versione di un'app, un grafo con fork e Pull Request, un changelog. Con 20 ragazzi erano 100 consegne attese: in mezz'ora ne sono arrivate 4. Molti hanno tradotto la pagina con Google Traduttore e poi hanno solo giocato.
2. **Perché è sbagliato.** Circa il 70% della classe è straniero e legge l'italiano come in quinta elementare. Un compito che non tutti possono iniziare lascia indietro proprio chi ha più bisogno, e «gioca e trova le differenze» non è un compito che tutti sanno svolgere.
3. **Regola.** In 1INF il compito è UNO SOLO e lo possono iniziare TUTTI. La differenza la fa la profondità: livello base (copiare, disegnare, scegliere), livello medio (scrivere i numeri o le parole), livello alto (una frase propria o un'idea). Frasi da quinta elementare, una per riga, con un disegno o un esempio. Prima di pubblicare mi chiedo se lo può fare anche chi non legge l'italiano.

## 09/10/2026 — 1INF, primo passo con la foto: chi non ha il telefono si blocca subito (#44)

1. **Errore.** Nel compito semplificato il passo 1 diceva «disegna sul foglio, fai la foto e mandala». I ragazzi in laboratorio non hanno il telefono e non sanno fare la cattura dello schermo senza una spiegazione. Il primo passo li bloccava tutti: il contrario di «Vinci subito».
2. **Regola.** In laboratorio ogni passo si fa tutto al computer, scrivendo nel Modulo o nella pagina. Foto e catture dello schermo si chiedono solo se il docente dice che ci sono i telefoni, oppure dopo una lezione su come si fa la cattura. Il passo 1 deve essere una risposta che tutti sanno dare (contare, scegliere, copiare una parola). Sotto ogni passo ci sono sempre le istruzioni «come si manda», nelle 3 lingue.

## 09/10/2026 — 1INF, attività a mano (disegnare il grafo): metà lezione persa (#45)

1. **Cosa succede in classe (spiegato da Nicola).** «Prendete carta e penna»: 5-6 ragazzi non ce l'hanno e girano per la classe a cercarla. Dopo 5 minuti chiedono «ma cosa devo disegnare?». Dopo 15 minuti ha consegnato il 70%, il restante 30% va seguito uno per uno. Servono 30 minuti solo per avere i disegni, poi per rispondere a ognuno: 3 minuti a testa = 60 minuti.
2. **Errore.** Ho proposto di disegnare il grafo a mano: un'attività probabilmente inutile, che il docente non può correggere in tempo e che porta via metà della lezione.
3. **Regola.** Niente attività a mano o su carta, se Nicola non le chiede. Ogni attività deve potersi controllare in automatico o a colpo d'occhio dalla pagina del prof, senza passare banco per banco. Prima di proporre un'attività calcolo il tempo reale: preparazione + chi resta indietro + tempo del prof per rispondere a tutti.

## 12/10/2026 — Modulo «Consegna»: annunciato un testo da cambiare senza dare il riquadro da copiare (#46)

1. **Errore.** Ho detto a Nicola «dopo cambiamo anche questa frase» senza mettere nello stesso messaggio la frase nuova pronta da copiare. È la regola COPIA, già chiesta molte volte.
2. **Regola.** Ogni testo che Nicola deve scrivere, anche se arriva nel passo dopo, sta già nel messaggio in un blocco di codice, un valore per blocco (CLAUDE.md, regola 9).

## 12/10/2026 — Modifica del Modulo «Consegna»: spiegazioni che fanno perdere il docente (#47)

1. **Errore.** Ho guidato Nicola indicando i campi con il testo che contenevano. Dopo ogni incolla quel testo cambiava, quindi i riferimenti non valevano più. Non ho detto che in Moduli si scrive nel riquadro attivo, quello con la striscia blu, né cosa doveva vedere dopo ogni azione. Risultato: testi incollati due volte nel posto sbagliato.
2. **Regola.** I campi si indicano per POSIZIONE stabile («secondo riquadro dall'alto, prima riga in grassetto = titolo, riga sotto = descrizione»), non per il testo che contengono. Ogni passo finisce con «Dopo devi vedere: …», così l'errore si accorge subito. Quando un'interfaccia è complicata da guidare, propongo prima la strada automatica (script) o la più corta.

## 12/10/2026 — Script da copiare: 404 sul repository privato, per la seconda volta (#48)

1. **Errore.** Come venerdì, ho mandato Nicola a copiare lo script dal repository privato. Nella finestra PIAMARTA, dove lavora con lo script, GitHub risponde 404 perché lì non è collegato l'account con l'accesso.
2. **Regola.** Lo script si copia sempre dal link pubblico in testo semplice (CLAUDE.md, regola 10). La copia pubblica si aggiorna a ogni modifica.


## 12/10/2026 — 2INF: compito e backlog con il cinese in una classe solo italiana (#49)

1. **Errore.** Ho copiato il compito della 3INF per la 2INF lasciando le righe in cinese (e la dispensa Agile con il bengalese). Poi ho detto che erano «nascoste»: erano ancora nella pagina. La 2INF è solo italiano. Si è persa l'ora.
2. **Regola.** Per una classe solo italiano ogni pagina passa da `strumenti/solo_italiano.py`: toglie le altre lingue e, se resta anche un carattere cinese, arabo o bengalese, si ferma con errore e non si pubblica. Il generatore della 2INF lo chiama da solo. Non si dice mai «sistemato» senza il controllo passato.

## 12/10/2026 — Script: «premi Ctrl+V» senza dire cosa c'è da incollare (#50)

1. **Errore.** Ho scritto «premi Ctrl+A, poi Ctrl+V» dando per scontato che Nicola avesse già copiato il codice. In più, nel passo prima gli facevo incollare un indirizzo, che avrebbe preso il posto del codice copiato.
2. **Regola.** La memoria del copia e incolla si considera VUOTA. Ogni «incolla» viene subito dopo il passo che dice cosa copiare e da dove, e si dice cosa c'è in memoria in quel momento. L'ordine dei passi evita che una copia cancelli quella prima: prima si apre la pagina dove si incolla, poi si copia, poi si incolla.

## 12/10/2026 — Script: «incolla nel riquadro del codice» senza dire in quale file (#51)

1. **Errore.** Il progetto «Consegne Classroom → Git» ha 5 file e si apre su «Codice.gs». Ho detto di incollare «nel riquadro del codice» senza dire di cliccare prima «automazione-corso.gs». Così si rischiava di cancellare il vecchio script della 1INF.
2. **Regola.** Le guide si scrivono sulla mappa vera dello schermo (CLAUDE.md, regola 10: i 5 file, la barra, «Modifiche non salvate»). Prima di dare passi su un programma che non ho ancora visto, chiedo una schermata una volta sola e la salvo come mappa. Non la richiedo a ogni passo.

## 12/10/2026 — TERZA volta: firma data per mancante dal bottone «FIRMA ✓» (#52)

1. **Errore.** Ripetizione degli errori 11 e 36. Dallo screenshot della 2INF ho detto che le tre ore non erano firmate perché c'era il bottone «FIRMA ✓» e non il segno verde degli altri docenti. Nicola aveva già firmato, e ha perso tempo durante la lezione.
2. **Regola.** La regola è stata spostata in CLAUDE.md, regola 4, dove si legge per prima. Su DIDAweb il bottone «FIRMA ✓» c'è anche sulle ore firmate. Dallo screenshot non si deduce mai che un'ora non è firmata. L'unica prova è «Da firmare» o «Visualizza tutte le firme arretrate». Se Nicola dice «firmate», è così.

## 12/10/2026 — Parole in più che confondono: «onestamente», «valide» (#53)

1. **Errore.** Ho scritto «onestamente», che fa pensare che altre volte non lo sia. Poi ho scritto che Katherine A. resta sotto il 60 «perché ne servono 5 valide». Le sue PR erano tutte valide: la parola faceva pensare a un problema che non c'era.
2. **Regola.** Niente avverbi e aggettivi che non servono. Una parola che restringe il senso («valide», «vere», «solo») si usa solo se in quel caso cambia qualcosa. Rileggo ogni frase togliendo la parola: se il senso resta uguale, la tolgo.

## 12/10/2026 — Considerazioni del docente interpretate invece di chiedere (#54)

1. **Errore.** Nicola stava scrivendo le sue considerazioni (PPP). Ho dato per scontato cosa volesse: prima una pagina nuova per il Modulo, poi «i 5 bottoni come modello fisso per ogni lezione». Non me l'aveva chiesto.
2. **Regola.** Quando Nicola ragiona ad alta voce o scrive considerazioni, non si decide niente al posto suo. Se non è chiaro cosa vuole, si chiede con una domanda sola.

## 12/10/2026 — Istruzioni con «se» e domande dentro (#55)

1. **Errore.** Nelle istruzioni per lo script ho scritto «Se la scheda è già aperta, salta alla Parte B» e ho chiuso con una domanda. Così il docente deve decidere mentre esegue.
2. **Regola.** Le istruzioni sono un flusso unico che parte sempre da zero e funziona senza condizioni: niente «se», niente «salta», niente domande dentro i passi.

## 12/10/2026 — Passi scritti come catene di coordinate: non si capiscono (#56)

1. **Errore.** Ho scritto i passi come «Account PIAMARTA · finestra Chrome con le schede arancioni · in alto, a destra dell'ultima scheda: clicca il «+»» e «Qui in chat · riquadro qui sotto». Le catene di coordinate separate da «·» non si leggono come frasi: il docente non le capisce.
2. **Regola.** Ogni passo è una frase semplice in italiano, che comincia con il verbo («Clicca…», «Premi…», «Torna…»). Il «dove» sta dentro la frase, con parole normali. Dove si può si usano i tasti (Ctrl+T per una scheda nuova, Ctrl+V, Invio) invece di cercare un bottone. Il bottone «copia» dei riquadri si descrive com'è: il piccolo bottone a destra del riquadro grigio.

## 12/10/2026 — RIPETIZIONE del #50: un link da copiare dopo aver copiato il codice (#57)

1. **Errore.** Nella versione corta delle istruzioni ho messo: copia il codice, poi copia il link dello script. Il secondo link cancella il codice dalla memoria. È lo stesso errore del #50, nello stesso pomeriggio.
2. **Regola.** Prima di mandare istruzioni con copia e incolla, controllo l'ordine: ogni «copia» deve essere seguito dal suo «incolla» prima di qualunque altra copia. Si apre sempre prima la pagina di arrivo, poi si copia il contenuto, poi si incolla.

## 12/10/2026 — Script fermo: GitHub ha bloccato per troppe richieste (#58)

1. **Errore.** Con lo script ogni minuto e quasi 200 file nella cartella dei comandi, a ogni giro lo script leggeva ogni file: migliaia di richieste all'ora. GitHub ha risposto «403 API rate limit exceeded» e dalle 14 lo script non lavorava più. Me ne sono accorto solo alle 15:12, perché un comando non partiva.
2. **Regola.** I comandi eseguiti e i compiti chiusi da più di 3 giorni vanno in `archivio/` (lo fa `lezione_pr.py archivia`, anche dentro il giro). Lo script v7.2 scrive nel log la risposta di GitHub quando non è 200. Dopo un comando, controllo entro 2 minuti che sia stato eseguito.

## 15/10/2026 — Verifica della 2INF scritta anche in cinese, e in 2INF non c'è nessun cinese (#82)

1. **Cosa è successo:** ho preparato la verifica rapida della 2INF in italiano e cinese. Nicola: «Siamo con la 2, non c'è nessun cinese. Devi imparare a capire la classe e te l'ho data, come mai sbagli?».
2. **Perché:** la regola giusta (2INF solo italiano, 12/10) era scritta solo nel registro delle versioni; la regola §2.49 e l'indice in CLAUDE.md dicevano ancora «italiano e cinese». Ho letto la riga vecchia e non ho controllato la classe.
3. **Correzione:** Modulo rifatto solo in italiano; §2.49 e indice corretti («2INF: SOLO ITALIANO»).
4. **Regola:** prima di scrivere per una classe si controllano le lingue di QUELLA classe nella regola aggiornata; quando una decisione cambia, si corregge la regola stessa, non solo il registro delle versioni.

## 14/10/2026 — Consegna con copia, apri il Modulo, incolla e Invia: un ragazzo non ce l'ha fatta (#81)

1. **Errore.** Nella lezione 3INF del 14/10 ogni consegna (revisione, PR, analisi del backlog) chiedeva quattro azioni: Copia, Apri il Modulo, Ctrl+V nella seconda casella, Invia. Il docente aveva chiesto più volte «al massimo un bottone». Un ragazzo ha scritto le sue richieste ma non le ha mai inviate; la pagina gli mostrava comunque «1 di 3» perché contava l'apertura del Modulo, non l'invio. Il docente: «per colpa tua non ha capito come fare».
2. **Regola.** Per il ragazzo: il testo scritto prima, poi UN bottone che consegna davvero. Prima di una lezione con consegne, il canale diretto deve funzionare (applicazione web dello script, oppure invio diretto al Modulo con i codici del link precompilato); se non c'è, si dice al docente PRIMA della lezione, non durante. La pagina conta una consegna solo quando è arrivata (letta dal Modulo), mai al clic.

## 14/10/2026 — Il monitor mostrava solo la data, mai i giri di Veyon (#80)

1. **Errore.** Nelle pagine del monitor (1INF, 2INF, 3INF) una riga di codice scriveva nella pagina solo la data e buttava via la tabella dei giri di Veyon. Il 14/10 ho aggiunto i giri della 1INF nel file, ma sulla pagina non comparivano: il docente ha detto «non ho un posto dove capire la situazione dei ragazzi e il monitor di cosa guardano». Nell'audit controllavo che la pagina si aprisse senza errori, non che mostrasse i giri.
2. **Regola.** Nell'audit di ogni pagina controllo il CONTENUTO: che compaiano davvero i dati del file (per il monitor: l'ora dell'ultimo giro e almeno una riga), non solo che non ci siano errori.

## 14/10/2026 — Link dato prima che il sito fosse aggiornato (#79)

1. **Errore.** Più volte, il 14/10, ho dato un link appena fatto il push: il docente apriva la pagina e vedeva ancora la versione vecchia (verifica «Non trovato», bottone verde in cima già tolto, anteprima del percorso ancora chiusa). Il docente: «mi dai un link per vedere una cosa che non posso vedere», «è la base dell'intelligenza».
2. **Regola.** Dopo ogni push, prima di dare un link: `bash strumenti/aspetta_pubblicazione.sh` (legge lo stato della pubblicazione di GitHub Pages per quel commit). Il link si dà solo dopo «PUBBLICATO». Se il docente vede ancora la versione vecchia, Ctrl+F5.

## 14/10/2026 — Lezione della talpa in 1INF: «lezione da dimenticare» (#78)

1. **Errore.** La lezione è stata cambiata in corsa troppe volte: il giro delle foto (webcam, Gemini, Modulo), le versioni del gioco che non si vedevano, il backlog e i voti del giorno prima, il bottone nero vuoto, il ripasso messo in cima e poi spostato, la verifica che dava «Non trovato» perché pubblicata nello stesso minuto. Il docente non ha potuto controllare niente; i ragazzi hanno fatto senza capire (alle 09:44-09:59 molti hanno rimandato una foto anche se il loro personaggio era già nel gioco). Il docente: «questa lezione li ha solo confusi».
2. **Regola.**
   1. La lezione è pronta e provata come un ragazzo PRIMA che entri la classe: gioco con le versioni giuste sul sito vero, sei bottoni del giorno, verifica e recupero. In classe non si cambia il giro; si correggono solo errori.
   2. Il percorso è uno solo e va dall'alto verso il basso: Passo 1, 2, 3… Le cose nuove si aggiungono IN FONDO come passo successivo, mai in cima. Ogni passo apre una finestra e si torna alla pagina; il passo fatto diventa «✓ Fatto» e il suo bottone si spegne.
   3. Una pagina si pubblica almeno 3 minuti prima di dare il link a voce, dopo averla aperta dal sito vero.

## 14/10/2026 — Bottone nero dei sei bottoni: portava a una pagina vuota (#77)

1. **Errore.** Il sesto bottone (nero) della pagina della lezione 1INF si chiamava «Valutazione dei singoli (solo prof)» e apriva una pagina con una sola frase, senza dati. Il docente lo ha cliccato in classe e non ha trovato né il monitor né la situazione dei ragazzi. Nell'audit avevo controllato che il bottone si aprisse, non che la pagina servisse a qualcosa. Il docente: «Oggi hai fatto malissimo».
2. **Regola.** Nessun bottone porta a una pagina vuota o «in attesa». Il sesto bottone è «La situazione della classe»: monitor dell'ultimo giro Veyon (sul compito, giocano, fuori compito), e per ognuno personaggio, modifiche nel gioco, richieste mandate e in attesa, voto della lezione, voto della verifica, cosa fa adesso. Nell'audit ogni bottone si apre E si controlla che mostri dati di oggi.

## 14/10/2026 — È entrato il direttore e nessun ragazzo ha saputo spiegare la teoria (#76)

1. **Errore.** La teoria della talpa era lunga, cambiata quattro volte durante la lezione e mai fatta ripetere: nessun momento «spiegalo con parole tue», nessuna domanda di controllo. Quando il direttore ha chiesto, nessuno ha saputo rispondere.
2. **Regola.** Ogni lezione ha in cima il riquadro «Spiegalo in 30 secondi»: 3-4 frasi da dire a voce al compagno e un mini-quiz che corregge subito. Si fa dopo la teoria e prima del compito: è la prova del nove del metodo.

## 14/10/2026 — Audit fatto solo sulle pagine dei ragazzi: la pagina del prof aveva bottoni che non funzionavano (#75)

1. **Errore.** Ho controllato le pagine dei ragazzi e ho detto «tutto a posto», ma nella pagina del prof restavano i bottoni «Foto va bene», «Rifalla» e «Metti nel gioco», che senza l'applicazione web danno errore, e il menu «Chi è?» che non serviva più. Il docente: «non so come usarla», «meno male che hai fatto audit».
2. **Regola.** L'audit comprende anche le pagine del docente (pannello, cruscotto, foto e personaggi) e prova ogni bottone come lo userebbe lui. Un bottone che non può funzionare oggi non si mostra: resta solo quello che funziona.

## 14/10/2026 — Il gioco della talpa sul sito mostrava solo la v1.0 (#70)

1. **Errore.** Ho provato il gioco solo sul mio server di prova, che non comprime i file. Sul sito vero l'elenco dei personaggi arriva compresso e il gioco lo decomprimeva una seconda volta: niente personaggi, «v1.0 · personaggi: 0» per tutti. In più il browser teneva in memoria il gioco vecchio. Il docente se n'è accorto in classe.
2. **Regola.** Un gioco si prova come lo vedono i ragazzi: indirizzo con la cartella del sito, file compressi, ricarica senza memoria. Ogni esportazione mette un numero nuovo nell'indirizzo del pacchetto (`strumenti/esporta_talpa.sh`), e il gioco scrive a schermo l'errore se l'elenco non arriva.

## 14/10/2026 — Le pagine dei sei bottoni erano ancora di ieri (#71)

1. **Errore.** Backlog, voti e classifica mostravano il treno del 13/10: le richieste di oggi finivano in fondo al backlog di ieri. Il docente: «il backlog è di ieri, non sta funzionando niente».
2. **Regola.** Quando comincia una lezione nuova, prima di pubblicare il compito, tutte le pagine dei sei bottoni (voti, backlog, monitor, novità, classifica, valutazione) e il cruscotto passano al lavoro del giorno; quelle di ieri restano in un file a parte con un link «di ieri». Poi si controllano tutte, una per una, sul telefono.

## 14/10/2026 — Percorsi cambiati più volte perché pensati senza guardare gli strumenti veri (#72)

1. **Errore.** Ho proposto strade che in aula non c'erano: la webcam (i PC non ce l'hanno), Gemini che modifica la foto del ragazzo (non lo fa), un bottone unico che ha bisogno dell'applicazione web non ancora accesa. Il percorso è stato rifatto quattro volte mentre la classe aspettava.
2. **Regola.** Prima di disegnare un percorso controllo che cosa c'è davvero: hardware delle postazioni, permessi degli account dei ragazzi, servizi già attivi (applicazione web, Modulo). Se una cosa non è sicura, la strada principale è quella che funziona già (il Modulo «Consegna»), e l'altra si accende dopo.

## 14/10/2026 — Monitor e cruscotto aggiornati solo su richiesta (#73)

1. **Errore.** Le schermate Veyon delle 9:30 sono entrate nel monitor e nel cruscotto solo dopo la domanda del docente («hanno già il bottone per monitorare la loro attività?»). È la stessa regola della #60.
2. **Regola.** Ogni schermata Veyon va nel monitor pubblico e nel cruscotto appena arriva, con chi gioca da più giri e chi è fuori compito.

## 14/10/2026 — Il menu «Chi è?» al posto del nome scritto dal docente (#74)

1. **Errore.** Per abbinare le foto ai nomi ho fatto un menu a tendina nella pagina del docente; lui voleva scrivere i nomi in chat. Un passaggio in più, mentre era in aula.
2. **Regola.** Per le informazioni che sa solo il docente si usa la strada più corta per lui (scriverle in chat); gli strumenti in più si propongono, non si impongono.

## 13/10/2026 — Nomi dei ragazzi della 4TI nelle pagine dei progetti (#69)

1. **Errore.** Nel cruscotto dei progetti di stage, nei diari e nelle chat archiviate dei due progetti ho scritto il nome dei ragazzi. Sono maggiorenni, ma il docente: «toglierei i nomi, metti solo le iniziali».
2. **Regola.** Anche per i maggiorenni, nelle pagine e nei file che scrivo si usano solo le iniziali (C.D.L., G.A.). Restano solo i nomi degli account GitHub dentro gli indirizzi, che non si possono cambiare.

## 13/10/2026 — Due strade per consegnare, e ne leggevo una sola (#68)

1. **Errore.** Il compito della 1INF su Classroom e la pagina davano due strade: il Documento di Classroom, come i ragazzi fanno sempre, e il Modulo «Consegna». Io leggevo solo il Modulo, e solo ogni 5 minuti. I Documenti scritti nel proprio Drive e non consegnati non li posso leggere. Molti ragazzi hanno lavorato e risultavano «senza Pull Request»; il docente ha dovuto spiegare a voce un'altra procedura.
2. **Regola.** Una sola strada di consegna, quella che leggo io in tempo reale, con un solo bottone nella pagina (la casella con «Manda», applicazione web dello script). Il compito su Classroom non deve invitare a scrivere nel Documento se il lavoro si consegna altrove. Prima di pubblicare, provo la consegna come un ragazzo e controllo che mi arrivi entro un minuto.

## 13/10/2026 — Domanda personale a un ragazzo: strade proposte senza guardare il suo schermo (#67)

1. **Errore.** Il docente chiede di fare una domanda personale a un ragazzo della 1INF che non parla italiano. Ho proposto, una dopo l'altra, strade che non potevano funzionare: un messaggio cifrato in fondo alla pagina, da aprire con la password; una frase in italiano da dirgli a voce; un messaggio di Veyon, che finisce dietro al gioco a schermo intero; la password scritta a mano in controllo remoto, con un testo finto dentro un riquadro da copiare. Il ragazzo intanto giocava, e il docente ha perso tempo in classe.
2. **Regola.** Prima di proporre una strada, guardo che cosa c'è DAVVERO sullo schermo del ragazzo (l'ultima schermata di Veyon) e che lingua legge, e percorro la strada al posto suo, passo per passo. Se a un passo si ferma (non legge l'italiano, una finestra finisce dietro, serve una cosa che non sa), quella strada non si propone. Una strada sola, quella che funziona; altrimenti dico che oggi non c'è. Nei riquadri da copiare va solo testo vero da incollare.

## 13/10/2026 — Codice da incollare: il ragazzo l'ha fatto funzionare ma non sa spiegarlo (#66)

1. **Errore.** Per la Tappa 7 (il vento) ho dato a C.D.L. quattro blocchi di codice da copiare e incollare, con il numero di riga. Il codice funzionava, ma alle tre domande del docente («che cosa fa la funzione», «perché vento=None», «chi fa la lettura automatica») non ha saputo rispondere.
2. **Regola.** Con il codice, prima capire e poi scrivere: si mostrano poche righe, il ragazzo le confronta, prevede che cosa succede e risponde con parole sue; i blocchi da incollare solo dopo che sa dire a cosa servono. È la prova del nove del corso: se non lo sa spiegare, la tappa non è fatta.

## 13/10/2026 — Al ragazzo cinque passi in un messaggio (#65)

1. **Errore.** Nella chat del progetto ho dato a C.D.L. un blocco di cinque passi (Actions, abilita, Automa meteo, Run workflow, aspetta). Il ragazzo leggeva e non sapeva se e cosa rispondere. Il docente: «devi essere tu a fargli domande semplici, un passo per volta e una cosa per volta».
2. **Regola.** Con i ragazzi, nella chat: un messaggio = un'azione + una domanda chiusa a cui rispondere con una parola («sì», «verde», «rosso»). Il passo dopo arriva solo dopo la sua risposta.

## 13/10/2026 — Il ragazzo ha scritto «fatto» e non gli ho risposto (#64)

1. **Errore.** Ho chiesto a C.D.L. di unire la Pull Request e di scrivere «fatto». Unendola, la Pull Request si è chiusa e i suoi commenti non mi arrivavano più: il ragazzo ha scritto e non ha avuto risposta finché il docente non me l'ha detto.
2. **Regola.** Mai chiedere una risposta nella stessa pagina che quel passo chiude. Il canale della chat è una Pull Request che resta aperta («Chat del progetto»); prima di chiedere un merge, la chat nuova deve già esistere ed essere seguita.

## 13/10/2026 — «Su Veyon non serve fare più niente», ed era falso (#63)

1. **Errore.** Ho scritto al docente che con Veyon non c'era più niente da fare e che bastava accettare l'invito, senza aver controllato che il ragazzo lo avesse aggiunto come collaboratore. L'invito non esisteva: il passo andava fatto ancora sul computer del ragazzo.
2. **Regola.** Prima di dire «fatto» o «non serve più» si controlla la prova (qui: la voce «Settings» visibile al docente, o la pagina dell'invito). Se non si può controllare, si dice qual è il prossimo passo e dove si fa, senza dare per scontato quello prima.

## 13/10/2026 — Istruzioni di consegna incomprensibili (#62)

1. **Errore.** Per rimediare alla consegna fragile ho dato al docente, da dire alla classe, una frase con cinque passi e un «se» (F5, riquadro rosso, bottone verde, «testo», Ctrl+V, Invia). Il docente: «assurdo, non lo capisco neanche io».
2. **Regola.** Ai ragazzi si dà al massimo una azione per frase, e la consegna è UN bottone. Se un procedimento ha bisogno di una spiegazione lunga, va cambiato il procedimento, non allungata la spiegazione.

## 13/10/2026 — Verifica: grafico, risposte perse, consegna fragile (#61)

1. **Errore.** Tre punti deboli scoperti in classe: il numero sulle barre del grafico si vedeva solo con il mouse e non funzionava; chi ricaricava la pagina o cliccava «1. Ripasso» durante la verifica perdeva tutte le risposte (Katherine A. ha dovuto rifarla); il risultato arriva al prof solo se il ragazzo fa a mano Copia, Modulo, Ctrl+V, Invia, e molti si fermano a «Consegna».
2. **Correzioni fatte in classe:** numeri scritti sopra le barre; salvataggio automatico ogni 2 secondi e ripresa dopo la ricarica; fine chiara («hai finito»); riquadro di riserva con il risultato; promemoria automatico negli ultimi 5 minuti; «Ho un problema con questa domanda».
3. **Regola.** Prima di aprire una verifica si prova anche: ricarica a metà, chiusura della scheda, clic sui bottoni in alto, consegna fino all'arrivo nel repository. Ciò che il docente dovrebbe dire a voce al momento giusto lo dice la pagina da sola. La consegna deve arrivare da sola (vedi `orario/da-fare-2026-10-13.md`, capitolo 05).

## 13/10/2026 — Percorso della verifica pubblicato senza il bottone del monitor (#60)

1. **Errore.** Il percorso della 2INF (ripasso, verifica, recupero) è uscito senza i bottoni del monitor della lezione e dei risultati, e i giri Veyon delle 09:00-09:04 li ho scritti solo nel riservato, non nel monitor pubblico. Il docente: «Va sempre pubblicato il bottone del monitoring».
2. **Regola.** Ogni pagina per i ragazzi ha sempre i bottoni per autoregolarsi (monitor, andamento, risultati) e ogni schermata Veyon va subito nel monitor pubblico della classe (§2.52 AUTOREGOLAZIONE).

## 12/10/2026 — Richiesta «portiamo tutto su Godot» lasciata indietro (#59)

1. **Errore.** Il 09/10 il docente ha detto «mi piacerebbe spostare tutto su Godot» e il 12/10 «PPP mettiamola su Godot». Ho portato su Godot solo il treno della 1INF (v2.0); le 20 versioni della 2INF del 12/10 e quelle della 3INF sono rimaste in HTML. Ho risposto «preparo tutto e lo consegno al tuo avanti» e poi non l'ho messo nell'elenco dei lavori aperti: il docente l'ha scoperto da solo la sera.
2. **Regola.** Ogni richiesta del docente, anche dentro un PPP, va subito nell'elenco dei lavori aperti (`orario/da-fare-*.md`) e compare in ogni aggiornamento sui lavori finché non è fatta o il docente non la toglie. Il gioco della classe si porta su Godot.
