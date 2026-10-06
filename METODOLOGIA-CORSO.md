# Metodologia del corso di Informatica

**Versione 1.1** — 06/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano.

*Documento del docente (in italiano, senza nomi di allievi). Raccoglie in un solo posto il metodo
che usiamo, la giornata di lezione, i compiti, la valutazione, la chiusura delle classi, la
documentazione per la Regione, l'automazione, i comandi da dare a Claude e dove stanno i documenti.
Le regole complete e datate sono in `RIFERIMENTI-E-DECISIONI.md`; questo documento ne è la sintesi
operativa da stampare.*

---

## 00 Come si usa questo documento

1. È la **sintesi da tenere sul banco**: per ogni situazione dice cosa si fa e quale comando si dà a Claude.
2. La fonte di verità delle regole resta `RIFERIMENTI-E-DECISIONI.md` (versione 2.23): il numero tra parentesi quadre, per esempio [§2.39], rimanda alla regola completa.
3. Quando una regola cambia, si aggiorna prima `RIFERIMENTI-E-DECISIONI.md`, poi questo documento con una versione nuova. La versione stampata resta congelata.

<div class="box blu" markdown="1">
**Approvato e da provare.** In classe si usa solo ciò che il docente ha provato e approvato [§2.41]. Ciò che è pronto ma non ancora provato è segnato **DA PROVARE** in questo documento (riepilogo al capitolo 13).
</div>

## 01 Missione e contesto

1. **Chi sono i ragazzi.** Molti hanno un background migratorio, a volte contesti difficili, spesso arrivano "scartati" da altre scuole. Qui non sono scarti: ricevono una cosa fatta bene. Il tono è sempre di rispetto e fiducia.
2. **Il patto di fiducia.** I ragazzi stimano molto il docente perché è lui a dargli questa possibilità. È la leva più forte e insieme la responsabilità di non deluderli: qualità alta, sempre.
3. **La missione.** Un percorso di qualità superiore, con dignità, per sbocchi lavorativi migliori. Non è un corso di serie B: livello alto, modo accessibile.
4. **Il vincolo della scuola.** Niente installazioni (servirebbe l'amministratore di sistema): si usano browser, programmi portabili e ciò che c'è già (Lazarus, Blocco note, Google, GitHub da browser).

## 02 Il motore del coinvolgimento

1. **Il problema numero 1** non è che non capiscano: è che si stufino e mollino, per difesa. Il compito è far sentire che provarci conviene e non fa male.
2. **Vinci subito · Fallo tuo · Mostralo**, sempre tutte e tre:
   1. **Vinci subito** (circa 10 minuti): il primo risultato è quasi impossibile da sbagliare.
   2. **Fallo tuo**: in ogni esercizio scelgono qualcosa di loro (frase, colori, nome, passioni).
   3. **Mostralo**: ogni pezzo è giocabile e mostrabile al compagno o sul telefono.
3. **Passi minuscoli con "FATTO" visibile**: un obiettivo alla volta, una piccola vittoria a ogni passo; niente tre ore di fila sullo stesso compito [§2.7].
4. **Errore senza vergogna**: il bug è normale, succede anche ai professionisti.
5. **La prova del nove**: se sanno spiegare a voce, con parole loro, cosa hanno fatto, la competenza c'è. Vale anche per l'uso dell'intelligenza artificiale (IA): aiuta a capire, non a saltare il pensiero.
6. **Sovradimensionare e gestire il divario** [§2.24]: un nucleo base che tutti riescono a fare e consegnare, più sfide per chi finisce prima, così nessuno resta fermo.
7. **Carta e penna in ogni lezione (tassativo)**: ogni allievo ha carta e penna sul banco per appunti e schemi a mano; chi non li ha li riceve dal docente, che segna una nota.
8. **Solo il metodo del docente** [§2.26]: se i ragazzi faticano si spiega lo stesso metodo in modo più semplice, mai un metodo alternativo.

## 03 Come si scrive per i ragazzi

1. **Un'azione per passo**, numerata. Mai due clic nello stesso passo.
2. **Prima il dove, poi il cosa**: il programma (Lazarus, Windows, GitHub, Classroom), la zona dello schermo, il nome del bottone, l'azione.
3. **"Adesso devi vedere"** sotto ogni passo, così il ragazzo sa se l'ha fatto bene. **"Non mi torna"** con il rimedio all'errore tipico di quel passo.
4. **Niente da scrivere a mano**: nomi e codice si copiano con il bottone giallo e si incollano con Ctrl + V [§2.20].
5. **Mai riconoscere un file dall'estensione**: sui computer della scuola le estensioni sono nascoste. Si fa scegliere tutta la cartella (Ctrl + A).
6. **Lingue** [§2.4]: italiano per tutti; arabo e cinese semplificato per la Classe 1; bangla solo per chi serve in Classe 3. Indirizzi ed email non si traducono; i bottoni dei siti si descrivono per posizione e colore, non con il nome inglese.
7. **Stesse cose, stesso layout** [§2.19]; codice Lazarus con i rientri allineati (if con else, begin con end) [§2.27].
8. **Testi su Classroom già impaginati** [§2.29]: titoletti in maiuscolo, una riga per passo, il link su una riga sua.
9. **Una pagina per i ragazzi e un link per il docente**: tutto il materiale del giorno sta in una sola pagina del sito del corso; il docente ha la sua pagina di controllo.

## 04 La giornata di lezione

### 04.1 Prima della lezione

1. **Report dello svolto** della classe, poi 3-4 argomenti proposti; il docente sceglie [§2.16, §2.23].
2. **Scheda sintetica** di una pagina per la lezione frontale alla lavagna [§2.22].
3. Claude prepara **pagina dei ragazzi, compito su Classroom (in coda, fermo) e testi del registro** nel piano della settimana (`orario/piano-settimana-...`).
4. I compiti restano in coda nello stato **in attesa dell'OK del docente**: non partono da soli.

### 04.2 In classe

1. **Firma delle ore subito, entro le 14:05** (vincolante): si firma il programma previsto, anche provvisorio; le ore non firmate vengono tolte dal monte ore della Regione. Testo del registro corto, massimo circa 40 caratteri, uno per ora [§2.25].
2. **Presenze**: il docente le manda a Claude; gli assenti si escludono da liste, pagine e conteggi [§2.35].
3. **Carta e penna sul banco** (e il materiale del giorno, per esempio cacciaviti e forbici quando servono).
4. **OK del docente** ("OK 1INF") e lo script pubblica il compito su Classroom entro 5 minuti.
5. **Un solo compito aperto alla volta** [§2.39]: il secondo si pubblica quando il docente dice che la classe ha finito il primo. Titoli con l'ordine ("1 di 2").
6. **Solo il lavoro del giorno** su Classroom e sulle pagine [§2.38].
7. **Risposte cortissime di Claude in classe** [§2.33]: il testo del compito da incollare e il link del docente, niente altro se non richiesto.
8. **Monitoraggio con Veyon**: dalla miniatura solo fatti ("PC 12 su Google Maps alle 11:30"), mai giudizi [§2.32]; il fuori compito si annota sempre [§2.36].

### 04.3 A fine lezione

1. La raccolta delle consegne è automatica: alla scadenza più 10 minuti.
2. **Chiudi classe** solo dopo l'ultima raccolta (capitolo 07).
3. Claude chiede gli **argomenti realmente svolti** e aggiorna `ARGOMENTI-SVOLTI-2026-27.md`.

## 05 Il compito: dal testo alla consegna

1. **Struttura**: pagina unica dei ragazzi (spiegazioni, passi, materiali) + compito su Classroom con il testo impaginato + Documento Google da compilare.
2. **Riflessione obbligatoria** in ogni compito [§2.2]: "cosa NON ho fatto e perché" e "cosa NON ho capito". È la parte più importante da leggere.
3. **Un solo Documento** per la consegna [§2.6] (screenshot, codice, spiegazione, riflessione), non file sparsi.
4. **Lavori su GitHub**: caricamento con Add file, poi Upload files, poi la cartella del progetto con Ctrl + A. Il ragazzo su Classroom preme Consegna; il codice lo legge Claude dal repository [§2.34].
5. **Controllo dei lavori su GitHub** [§2.40]: i repository si trovano con la ricerca di GitHub (creati oggi), i file si leggono scaricandoli (clone). Mai dire "non ha caricato" senza aver controllato.
6. **Documenti già su Classroom sono congelati** [§2.11]: si correggono solo se l'errore è grave, avvisando la classe; mai cambiare il metodo a lezione iniziata.

## 06 La valutazione

1. **Voti in centesimi**: O = oggettivo (dalla griglia), C = commisurato (per chi ha un percorso personalizzato).
2. **Griglia scritta prima**, con i punti per voce; le penalità sono dichiarate (per esempio fuori compito osservato: da −5 a −15 centesimi).
3. **Valutazione dell'AI** [§2.15]: Claude propone voto e giudizio, sempre marcati come "dell'AI"; il docente conferma, corregge o sovrascrive.
4. **Prova del nove orale**: tre domande per verificare che il ragazzo sappia spiegare.
5. **Recupero a fianco** [§2.42]: chi ha meno di 60 o non ha svolto rifà l'esercizio in versione semplificata con il docente accanto (pagine `recupero/` del sito; elenco con i nomi nel repository riservato). Proposta da confermare: voto nuovo sul registro, il precedente resta; se non sa rispondere alle domande non supera 60.
6. **Voti su Classroom in bozza (DA PROVARE)**: lo script li scrive come bozza nei compiti creati dallo script; il docente li controlla e preme "Restituisci".
7. **Valutazione complessiva della classe** [§2.43]: il punto su tutti i lavori fino a una data, con la lista standard per il docente; i tre con la media più bassa vengono interrogati per recuperare.
8. **Voti su DIDAweb**: si inseriscono a mano, dall'elenco già in ordine alfabetico con la descrizione corta (`archivio-prove/didaweb/`). Da verificare se DIDAweb permette di caricarli da file.

## 07 Chiudi classe

Il comando **"Chiudi classe 2INF"** chiude il lavoro della classe [§2.30]. Prima Claude dice cosa genera e aspetta il **"via"**.

1. **Per ogni allievo presente**: il libro individuale (teoria dal primo giorno, lavori, voti, cosa fare), in versione protetta da password per il ragazzo e senza password per il docente.
2. **Per il docente**: documento di chiusura (griglie, voti per il registro, report, monitoraggio, fuori compito, cosa non hanno capito), foglio Excel della classe aggiornato.
3. **Due zip separati** [§2.14]: DOCENTE senza password; LIBRI PROTETTI per i ragazzi. Mai documenti del docente nello stesso pacchetto dei ragazzi.
4. **Assenti**: il loro libro va nella cartella `assenti`, fuori dagli zip.
5. Tutto con i nomi resta solo nel **repository riservato** (`dati/chiusure/<CLASSE>/`).
6. Se un file supera il limite di invio (30 MB), si divide prima e si dice esattamente quali file scaricare.

## 08 Documentazione per la Regione

1. **Firma delle ore** entro le 14:05, ogni giorno.
2. **Argomenti svolti** (`ARGOMENTI-SVOLTI-2026-27.md`), agganciati all'Allegato A.
3. **Allegato A** (programma per competenze): le parti del docente in `allegato-a-2026-27/`.
4. **Archivio delle prove (DA PROVARE)** nel repository riservato (`archivio-prove/<CLASSE>/`): per ogni prova la scheda (data, classe, competenza, testo del compito, passi, griglia, presenze, esiti e voti per allievo), la pagina del compito fotografata quel giorno e la chiusura; per ogni classe il **registro delle prove** in PDF.
5. **Consegne su Classroom**: restano sul corso Classroom insieme ai voti; per i lavori su GitHub la prova è nel repository dell'allievo e nell'archivio.

## 09 L'automazione: Git, script e Classroom

1. **Due repository** [§2.5]:
   1. **pubblico** `corso-informatica`: materiali, pagine del sito (cartella `docs/`), mai nomi di minori;
   2. **riservato** `corso-informatica-riservato`: nomi, voti, presenze, consegne, chiusure, coda dei compiti, configurazioni.
2. **La coda dei compiti** (`coda/*.json` nel riservato): un file per compito, con stato:
   1. **in attesa dell'OK del docente**: preparato, fermo;
   2. **da pubblicare**: dopo l'OK, lo script lo pubblica;
   3. **pubblicato**, poi **chiuso** dopo la raccolta.
3. **Lo script di Classroom** (`strumenti/automazione-corso.gs`, progetto "Consegne Classroom → Git" sull'account della scuola) gira da solo ogni 5 minuti e lavora nei due sensi:
   1. da Git a Classroom: pubblica i compiti (solo quelli con la data di oggi); nella versione 3, DA PROVARE, aggiorna i testi e scrive i voti in bozza;
   2. da Classroom a Git: alla scadenza porta le consegne nel repository riservato.
4. **Limiti**:
   1. i compiti creati a mano su Classroom non si possono modificare né votare dallo script, perciò i compiti li crea sempre lo script;
   2. ogni nuova versione dello script la incolla il docente una volta (mai subito prima delle lezioni);
   3. DIDAweb non ha un accesso per i programmi: niente automazione.
5. **Pagine di controllo del docente**: leggono i siti dei ragazzi direttamente, senza le API di GitHub (che si bloccano dalla rete della scuola) [§2.37].

## 10 I comandi da dare a Claude

| Comando | Quando | Cosa succede |
|---|---|---|
| PPP (o "parcheggia") | quando si vuole annotare senza riempire la chat | Claude annota e prepara in silenzio; consegna solo dopo "avanti". Se dentro c'è un'azione esplicita, la fa subito |
| avanti | dopo uno o più PPP | Claude consegna quello che era parcheggiato |
| via | dopo che Claude ha detto cosa farà | Claude esegue (per esempio la chiusura della classe) |
| OK 1INF (o la classe) | in classe, quando si vuole il compito su Classroom | il compito in coda passa a "da pubblicare"; lo script lo pubblica entro 5 minuti |
| Valutazione complessiva 1INF | quando si vuole fare il punto su tutti i lavori | Valutazione complessiva della classe: libri protetti, voti O e C per il registro, griglia, situazione, recupero, due zip |
| Chiudi classe 2INF | a fine lavoro, dopo l'ultima raccolta | libri individuali, zip docente e ragazzi, griglie, voti, report |
| monito, o uno screenshot di Veyon senza testo | durante la lezione | Claude annota i fatti nel report di andamento (riservato) |
| chi manca? | durante la lezione | elenco di chi non ha ancora fatto o consegnato (assenti esclusi) |
| dammi il link per controllare | durante la lezione | link della pagina di controllo del docente |
| dammi il testo per Classroom | quando serve | testo del compito impaginato, in un solo blocco da copiare |
| dammi da scaricare qui | quando si vogliono i file | Claude manda i file in chat (divisi se troppo grandi) |
| ricordami … | quando serve | Claude programma un promemoria che arriva in questa chat all'ora giusta |
| prepara lezioni per domani | il giorno prima | materiali, compiti in coda, testi del registro, promemoria |
| FIRMA · SVOLTO · VOLO · LAVAGNA · STATO | dall'Atlante | firma ore, argomenti svolti, voto "domanda al volo" (70 OK / 50 KO), foto della lavagna nei libri, stato dei dati |

## 11 I documenti: dove sta cosa

### 11.1 Repository pubblico (corso-informatica)

1. `RIFERIMENTI-E-DECISIONI.md`: tutte le regole datate (fonte di verità).
2. `REGISTRO-ERRORI-CLAUDE.md`: ogni errore segnalato dal docente, con la regola nata da lì [§2.28].
3. `METODOLOGIA-CORSO.md`: questo documento.
4. `ATLANTE.md`: la mappa dei libri, dei tipi di file e dei comandi.
5. `CLAUDE.md`: istruzioni per Claude e indice di tutti i documenti con le versioni.
6. `orario/`: orario e piano della settimana, con i testi del registro.
7. `ARGOMENTI-SVOLTI-2026-27.md`, `allegato-a-2026-27/`: documentazione per la Regione.
8. `docs/`: le pagine del sito per i ragazzi (una per classe e argomento), il motore dei quiz, le pagine di recupero.
9. `classe-1/` … `classe-4/`: materiali delle classi (dispense, compiti, generatori).
10. `strumenti/`: generatori comuni (pagine di recupero, nomi dei file).

### 11.2 Repository riservato (corso-informatica-riservato)

1. `coda/`: i compiti per lo script di Classroom.
2. `strumenti/automazione-corso.gs`: lo script di Classroom.
3. `config/`: classi e corsi Classroom, utenti GitHub dei ragazzi, elenco delle prove.
4. `dati/presenze/`, `dati/andamento/`, `dati/consegne/`, `dati/chiusure/`, `dati/recupero/`: presenze, monitoraggio, consegne, chiusure, recuperi.
5. `archivio-prove/`: documentazione delle prove per la Regione e voti pronti per DIDAweb.
6. `generatori/`: chiusure delle classi, archivio delle prove, recupero.
7. `strategico/`: password dei libri (mai incollate in chat).

## 12 Regole di lavoro di Claude

1. **Ogni correzione del docente diventa regola** e va nel registro degli errori [§2.28].
2. **Mai pubblicare su Classroom senza l'OK del docente**; solo il lavoro del giorno; un compito alla volta.
3. **Verificare prima di affermare**: mai dire "non ha fatto" o "non ha caricato" senza aver controllato.
4. **Tutto ciò che il docente deve copiare** sta in un blocco con il bottone copia, una cosa per blocco; ogni azione con le coordinate complete (programma, finestra, zona, bottone).
5. **Privacy**: nomi, voti e presenze dei minori solo nel repository riservato; le password non si scrivono mai in chat.
6. **Solo strumenti approvati** in classe; ciò che è nuovo si prova prima con il docente [§2.41].
7. **File grandi**: si dividono prima di mandarli e si dice esattamente quali scaricare.

## 13 Stato: approvato e da provare (al 06/10/2026)

<div class="box blu" markdown="1">
**Approvato (provato in classe):**

1. pubblicazione del compito con lo script;
2. raccolta automatica delle consegne;
3. una pagina per i ragazzi e un link per il docente;
4. caricamento su GitHub con Upload files e Ctrl + A;
5. Chiudi classe con libri individuali protetti, zip del docente e voti in centesimi.

**Da provare con il docente:**

1. voti in bozza su Classroom (script versione 3);
2. archivio delle prove e registro delle prove;
3. recupero a fianco (pagine semplificate ed elenco del docente);
4. pagina del compito unica in 3 versioni (normale, semplificata, lingue) e correttore unico: da costruire.
</div>

## 14 Glossario delle sigle

| Sigla o termine | Significato |
|---|---|
| IA / AI | intelligenza artificiale |
| PDF | formato di documento da leggere e stampare |
| MD | Markdown, il testo sorgente dei documenti (lo legge anche l'IA dei ragazzi) |
| HTML / CSS | linguaggi delle pagine web (struttura e aspetto) |
| PFP | piano formativo personalizzato |
| Allegato A | il programma per competenze richiesto dalla Regione |
| Repository | cartella di progetto su GitHub, con la storia delle modifiche |
| Commit | salvataggio di una modifica su GitHub |
| Veyon | programma per vedere gli schermi dei computer del laboratorio |
| DIDAweb | il registro elettronico della scuola |
| O / C | voto oggettivo / commisurato |

## 15 Registro delle versioni

2. **v1.1 (06/10/2026)**: aggiunta la Valutazione complessiva della classe (comando e capitolo 06).
1. **v1.0 (06/10/2026)**: prima versione, dalla sintesi di `RIFERIMENTI-E-DECISIONI.md` v2.23, dell'Atlante e del lavoro di settembre-ottobre 2026.
