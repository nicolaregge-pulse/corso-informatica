# Strumenti automatici del docente: DIDAweb e Google

**Versione 1.3** — 07/10/2026 · Area Docente · Prof. Nicola Regge, Centro Padre Piamarta, Milano

Guida passo-passo, per i docenti, agli strumenti che fanno il lavoro ripetitivo al posto nostro: i segnalibri che scrivono i voti su DIDAweb e lo script che collega Classroom, Moduli, Drive e i voti con il repository Git. Ogni passo è una riga di tabella: account, finestra, dove, cosa fare. Tutto quello che va copiato è in una casella con il bottone «Copia».

## 00 Come si legge questa guida

1. Ogni capitolo è una fase. Si può leggere da solo: non serve leggere gli altri prima.
2. I passi sono in tabella, con le colonne sempre nello stesso ordine: N. · Account · Finestra / scheda · Dove · Cosa fare. Una riga = una sola azione.
3. Le caselle grigie si copiano con il bottone «Copia» (nella versione HTML) e si incollano con Ctrl + V. Non selezionare il testo con il mouse.
4. Box colorati: giallo = nota utile; rosso = attenzione, si rischia di sbagliare; blu = da confermare.
5. Questa guida non contiene nomi di allievi né password: i dati veri stanno solo nel repository riservato.

## 01 I due account e dove sta cosa

1. **Account PERSONALE** (l'email privata del docente): finestra Chrome con le schede gialle e la foto in alto a destra. Qui c'è GitHub e la chat con Claude.
2. **Account PIAMARTA** (l'email della scuola): finestra Chrome con le schede arancioni e il bottone «Scuola». Qui ci sono DIDAweb, Classroom, Drive, Moduli e lo script automatico.
3. **Repository pubblico** (sito del corso, GitHub Pages): materiali per i ragazzi, pagine «Il mio punto», recupero, questa guida. Niente nomi.
4. **Repository riservato**: voti, presenze, password, consegne, la coda dei compiti e i comandi dello script. Solo il docente e Claude.

> **Nota:** prima di ogni passo si dice SEMPRE l'account. Un link del repository riservato aperto nell'account PIAMARTA dà «404»: non è un errore, è l'account sbagliato.

## 02 DIDAweb: i segnalibri che scrivono i voti

Un segnalibro (preferito di Chrome) può contenere un piccolo programma al posto dell'indirizzo. Cliccandolo sulla pagina di DIDAweb, il programma lavora su quella pagina: legge gli alunni, crea la colonna, scrive voti e argomento. Non serve installare niente.

### 02.1 I cinque segnalibri

| Nome | A cosa serve | Salva da solo? |
|---|---|---|
| Copia HTML DIDAweb | copia la struttura della pagina per farla studiare a Claude (quando DIDAweb cambia) | no, non scrive niente |
| Copia funzioni DIDAweb | copia il funzionamento dei bottoni NUOVO VOTO, Ok, SALVA | no, non scrive niente |
| Voti DIDAweb | scrive una lista di voti in una colonna che esiste già | no: SALVA lo preme il docente |
| Voti DIDAweb AUTO | dal «pacchetto»: crea la colonna, scrive voti e argomento, chiede conferma e salva | sì, dopo la conferma |
| Firma registro DIDAweb | scrive l'argomento delle proprie ore nel Registro di corso e le firma, un'ora per clic, anche su più classi | sì, dopo la conferma di ogni ora |

### 02.2 Creare un segnalibro nella cartella «DidaWeb»

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | — | questa guida | casella del codice del segnalibro (capitoli 02.3-02.6b) | clic su «Copia» |
| 2 | PIAMARTA | Chrome arancione, scheda DIDAweb | barra dei preferiti, cartella «DidaWeb» (se non c'è: tasto destro sulla barra → «Aggiungi cartella…») | clic con il tasto destro sulla cartella |
| 3 | PIAMARTA | menu che si apre | «Aggiungi pagina…» | clic |
| 4 | PIAMARTA | finestra «Modifica preferito» | casella «URL» | clic dentro, Ctrl + A, Ctrl + V |
| 5 | PIAMARTA | stessa finestra | casella «Nome» | scrivi il nome del segnalibro |
| 6 | PIAMARTA | stessa finestra | elenco cartelle | evidenziata «DidaWeb», poi «Salva» |

> **Attenzione:** se la finestra di Chrome è stretta, i segnalibri finiscono dietro le due frecce «»» a destra della barra. Per cambiare il codice di un segnalibro: tasto destro sul segnalibro → «Modifica…» → casella URL → Ctrl + A → Ctrl + V → «Salva».

### 02.3 Copia HTML DIDAweb

Si usa sulla pagina «Registro delle valutazioni» quando un segnalibro smette di funzionare (DIDAweb aggiornato). Copia la pagina senza programmi e immagini; si incolla nella chat con Claude.

```
CODICE:codice-copia-html.txt
```

> **Attenzione:** tra il clic sul segnalibro e il Ctrl + V nella chat NON fare screenshot: lo screenshot prende il posto del testo copiato.

### 02.4 Copia funzioni DIDAweb

Copia il codice dei bottoni della pagina (NUOVO VOTO, Ok, SALVA, PUBBLICA). Serve solo quando si costruisce o si ripara un segnalibro.

```
CODICE:codice-copia-funzioni.txt
```

### 02.5 Voti DIDAweb (versione 1.0, la più semplice)

1. In DIDAweb: classe, materia, scheda VALUTAZIONI. La colonna del voto deve esistere già (NUOVO VOTO → data → Ok).
2. Clic sul segnalibro «Voti DIDAweb»; se le colonne sono più di una chiede il numero.
3. Incollare la lista che prepara Claude, su UNA riga: `Cognome Nome;voto Cognome Nome;voto …`
4. Il segnalibro scrive i voti in giallo, salta chi ha già un voto diverso, elenca chi non trova. Poi il docente controlla e preme SALVA.

```
CODICE:codice-voti-didaweb-v1.txt
```

### 02.6 Voti DIDAweb AUTO (versione 2.0, fa tutto)

Il «pacchetto» è una riga sola con tre parti separate da `|`: la lezione, l'argomento, i voti.

```
07/10/2026 h 2 | Quiz 1 Cosa scrive il programma | Cognome Nome;90 Cognome Nome;75
```

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PIAMARTA | scheda DIDAweb | menu «Corso» e «Disciplina» in alto | scegli classe e materia del voto |
| 2 | — | chat con Claude | casella del pacchetto | clic su «Copia» |
| 3 | PIAMARTA | scheda DIDAweb | cartella «DidaWeb» | clic su «Voti DIDAweb AUTO» |
| 4 | PIAMARTA | finestrella «Incolla il pacchetto» | casella | Ctrl + V, poi «Ok» |
| 5 | PIAMARTA | finestrella «Creo la colonna del …» | — | «Ok» |
| 6 | PIAMARTA | finestrella «Tutto a posto. Salvo adesso?» | — | «Ok» per salvare, «Annulla» per controllare prima |

1. La lezione deve essere tra le «date suggerite» del registro (ore firmate). Se non c'è, il segnalibro si ferma e non fa niente.
2. Se la colonna di quella lezione esiste già, la usa (non ne crea una seconda).
3. Se c'è anche un solo avviso (nome non trovato, nome doppio, voto già presente, voto fuori da 40-100) NON salva.
4. Se dopo «Ok» la pagina si ricarica, il pacchetto resta in memoria: si clicca di nuovo il segnalibro e finisce il lavoro.
5. Non pubblica mai alle famiglie: i voti restano viola («non pubblicato»); «PUBBLICA» lo preme il docente.

```
CODICE:codice-voti-didaweb-auto-v2.txt
```

### 02.6b Firma registro DIDAweb (versione 1.2)

Serve a firmare le proprie ore nel «Registro di corso» senza dimenticarne nessuna, anche al mattino per le ore che devono ancora arrivare (la firma va fatta entro le 14:05). Si usa dalla pagina che si apre con Registro → «Sfoglia» → classe → giorno. Si firma solo il giorno stesso della lezione: i giorni futuri sono bloccati («BLOCCO GIORNO NON MODIFICABILE»). Il segnalibro usa lo stesso bottone verde «Firma ✔» della pagina: presenze, note e ore degli altri docenti non vengono toccate.

Due modi d'uso:

1. **Pacchetto vuoto**: firma le proprie ore della pagina aperta che non hanno ancora un argomento salvato (lo scrivi nella casella prima del clic, oppure te lo chiede).
2. **Pacchetto di Claude**: una riga con il giorno e, per ogni ora, classe, numero dell'ora e argomento (massimo 70 caratteri, meglio 40). Il segnalibro cambia da solo giorno e classe.

```
07/10/2026 | 3INF h5=Situazione voti e libro dei lavori | 3INF h6=Sito migliorato su GitHub, commit
```

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PIAMARTA | scheda DIDAweb | menu Registro → «Sfoglia» | scegli la classe e il giorno |
| 2 | PIAMARTA | scheda DIDAweb | cartella «DidaWeb» | clic su «Firma registro DIDAweb» |
| 3 | PIAMARTA | finestrella «Incolla il PACCHETTO» | casella | Ctrl + V del pacchetto, oppure lasciala vuota; poi «Ok» |
| 4 | PIAMARTA | finestrella «Ore da firmare … Inizio?» | — | controlla l'elenco, poi «Ok» |
| 5 | PIAMARTA | finestrella «FIRMO adesso?» | — | «Ok»: la pagina si ricarica con l'ora firmata |
| 6 | PIAMARTA | scheda DIDAweb, pagina ricaricata | cartella «DidaWeb» | clic di nuovo su «Firma registro DIDAweb» per l'ora successiva, fino al messaggio «FINITO» |

1. Un clic = un'ora firmata, perché ogni firma ricarica la pagina. Il lavoro che resta è in memoria per 6 ore.
2. Se serve cambiare giorno o classe, il segnalibro lo fa da solo e chiede di cliccare di nuovo.
3. Come si riconosce un'ora firmata: ha l'argomento SALVATO (la firma lo richiede; cancellare la firma cancella anche l'argomento). Il bottone verde «Firma ✔» resta anche sulle ore già firmate (serve a rifirmare dopo aver cambiato l'argomento) e il nome del docente compare anche sulle ore non firmate: né il bottone né il nome dicono se l'ora è firmata. Se l'ora è già firmata con lo stesso argomento, il segnalibro chiede se saltarla; con un argomento diverso chiede se rifirmare.
4. Le ore di altri docenti (casella grigia, senza bottone) non si toccano mai.
5. Il controllo finale si fa sempre dal menu Registro → «Da firmare» (oppure «Visualizza tutte le firme arretrate»).
6. «Annulla» su «FIRMO adesso?» non firma; poi chiede se fermare tutto e cancellare il lavoro in memoria.
7. Gli argomenti si possono correggere dopo, a fine giornata, con quelli realmente svolti.

> **Nota:** la pagina «Oggi» si apre solo durante l'orario delle lezioni e «Da firmare» mostra solo le ore già passate: per firmare al mattino tutte le ore del giorno si usa «Sfoglia».

```
CODICE:codice-firma-registro-v1.2.txt
```

### 02.7 Regole per i voti su DIDAweb

1. Voti in centesimi, minimo 40. Gli assenti non hanno voto.
2. La materia (Informatica, Laboratorio, Sicurezza professionale) si sceglie in base all'argomento del lavoro; Sicurezza professionale solo per le lezioni di sicurezza.
3. Data e ora: quelle della lezione in cui il lavoro è stato svolto.
4. Dopo il salvataggio: screenshot della tabella a Claude, che controlla riga per riga.

### 02.8 Problemi frequenti

| Cosa succede | Perché | Cosa fare |
|---|---|---|
| Nella chat arriva una foto invece del testo | uno screenshot ha sostituito il testo copiato | rifai il clic sul segnalibro e incolla subito |
| Il messaggio dice «HTML copiato» invece di «Funzioni copiate» | nel segnalibro c'è ancora il codice vecchio | Modifica… → URL → Ctrl + A → Ctrl + V → Salva |
| Non trovo il segnalibro | è dietro le frecce «»» o nella cartella «DidaWeb» | clic sulle frecce o sulla cartella |
| «Non c'è la lezione tra le date suggerite» | l'ora non è firmata o classe/materia sbagliate | controlla Corso e Disciplina; firma l'ora |
| «NON trovati: …» | il nome nella lista è scritto diversamente | Claude corregge la lista; si rifà solo per quei nomi |

## 03 Google: lo script automatico «Consegne Classroom → Git»

Uno script di Google (Apps Script) dell'account PIAMARTA gira da solo ogni 5 minuti. Legge dal repository riservato cosa deve fare e scrive lì il risultato. Il docente non lo apre: lo prepara e lo controlla Claude.

### 03.1 Dove sta e come si aggiorna

| N. | Account | Finestra / scheda | Dove | Cosa fare |
|---|---|---|---|---|
| 1 | PIAMARTA | Chrome arancione | script.google.com | apri il progetto «Consegne Classroom → Git» |
| 2 | PIAMARTA | progetto | elenco file a sinistra | il file dello script è «automazione-corso.gs»: NON toccare gli altri |
| 3 | PIAMARTA | progetto | menu in alto, «Esegui» | si usa solo la prima volta (funzione «attivaAutomatico», crea il timer) |

> **Attenzione:** quando lo script va aggiornato, si incolla tutto il codice SOLO dentro «automazione-corso.gs» e si salva (icona del dischetto). Prima di copiare il codice si aprono le schede che servono: copiare altro dopo farebbe perdere il codice negli appunti.

> **Da confermare:** prossima versione con «caricatore»: lo script scarica da solo la versione nuova da GitHub, così il docente non incolla più codice.

### 03.2 Fase 1 — Pubblicare un compito su Classroom (la «coda»)

1. Claude prepara la pagina del compito (sito del corso) e un file nella cartella `coda/` del repository riservato, con titolo, testo, PDF, scadenza.
2. Quando il docente dà l'OK, Claude mette lo stato «da-pubblicare»; al giro successivo (al massimo 5 minuti) lo script crea la cartella Drive, il Documento personale per ogni allievo e pubblica il compito. Stato «pubblicato».
3. Regole: un solo compito aperto alla volta; su Classroom solo il lavoro del giorno; se esiste già un compito con lo stesso titolo lo script non lo duplica.

### 03.3 Fase 2 — Raccogliere le consegne

1. Passata la scadenza (+10 minuti) lo script salva nel repository riservato il PDF e il testo di ogni Documento consegnato (anche in ritardo). Stato «chiuso».
2. Con le «raccolte in più» si riprendono anche le consegne arrivate dopo.
3. La «situazione» (chi ha consegnato e chi no) si aggiorna da sola mentre il compito è aperto.

> **Nota:** le consegne arrivano nel repository qualche minuto dopo la scadenza. A fine ora si consegna subito quello che c'è (bozza) e si aggiorna dopo: mai far aspettare la classe.

### 03.4 Fase 3 — Il «ponte» per tutta la suite Google

Per le cose singole Claude scrive un file nella cartella `comandi/` con «da-eseguire» e un elenco di azioni; lo script le esegue e scrive il risultato nello stesso file.

| Azione | Cosa fa |
|---|---|
| classroom.compiti / classroom.consegne | elenca i compiti di una classe / chi ha consegnato un compito |
| classroom.annuncio | pubblica un annuncio (solo con l'OK del docente scritto nel file) |
| drive.cerca / drive.elenca / drive.esporta / drive.copia / drive.cartella | cerca, elenca, esporta (PDF, TXT, XLSX…), copia file e crea cartelle |
| docs.leggi / docs.crea / docs.sostituisci | legge, crea e modifica Documenti |
| sheets.leggi / sheets.scrivi / sheets.crea | legge, scrive e crea Fogli |
| forms.crea_quiz / forms.risposte | crea quiz con punteggio / legge i risultati |
| forms.crea_modulo / forms.risposte_testo | crea moduli con risposte scritte (es. password del libro) / legge le risposte |
| gmail.bozza | prepara una mail in bozza (la invia il docente) |

> **Attenzione:** per sicurezza il ponte NON cancella niente, NON condivide fuori dalla scuola, NON invia mail. Mentre un annuncio è in attesa non si manda altro nel repository: altrimenti può uscire due volte.

### 03.5 Fase 4 — Moduli: quiz e moduli con risposte scritte

1. Quiz: dal file del compito (campo «quiz») lo script crea un Modulo per ogni versione, mescola le domande, allega i link al compito; alla chiusura salva i risultati.
2. Moduli a risposta scritta: raccolgono l'email della scuola, una sola risposta per account; le risposte vanno solo nel repository riservato.

### 03.6 Fase 5 — Voti su Classroom

1. Claude scrive i voti nel file del compito; lo script li mette su Classroom come BOZZA (centesimi).
2. Il docente controlla e preme «Restituisci». Funziona solo sui compiti creati dallo script.

## 04 Le pagine per i ragazzi collegate agli script

| Pagina | A cosa serve |
|---|---|
| Il mio punto (per classe) | ogni ragazzo scrive la password del suo libro e vede i SUOI lavori, il compito di oggi con «fatto / manca» e come finirlo; si aggiorna da solo durante l'ora; nel sito pubblico solo testo cifrato |
| Recupero | pagine semplificate, un'azione per passo, per rifare un esercizio con il docente accanto; anche versione facile con immagini e lettura ad alta voce |
| La password del mio libro | istruzioni e link al modulo per scegliere la password del proprio libro dei voti |

## 05 Il giro completo di una lezione

1. Prima della lezione: Claude prepara pagina del compito, coda, pagine di recupero; il docente firma le ore sul registro (entro le 14:05).
2. In classe: compito pubblicato dallo script; «Il mio punto» con le istruzioni personali; controlli ogni 5 minuti (consegne, commit su GitHub); monitoraggio Veyon (solo fatti, con ora e PC).
3. 10 minuti prima della campanella: zip con i libri protetti per i ragazzi e report per il docente.
4. Dopo: raccolta completa, voti definitivi, voti su DIDAweb con il segnalibro AUTO, argomenti svolti sul registro.

## 06 Changelog

1. **v1.3 (07/10/2026)** — segnalibro «Firma registro DIDAweb» v1.2: ora firmata = argomento salvato (provato sugli esempi veri del 07/10 e dell'08/10); si firma solo il giorno della lezione (giorni futuri bloccati).
2. **v1.2 (07/10/2026)** — segnalibro «Firma registro DIDAweb» v1.1: il bottone «Firma ✔» resta anche sulle ore firmate, quindi la firma si verifica dall'argomento e dal nome del docente; controllo finale da «Da firmare».
3. **v1.1 (07/10/2026)** — capitolo 02.6b: segnalibro «Firma registro DIDAweb» v1.0 (argomento e firma delle proprie ore dal Registro di corso, anche su più classi, un'ora per clic).
4. **v1.0 (07/10/2026)** — prima versione: segnalibri DIDAweb (Copia HTML, Copia funzioni, Voti v1.0, Voti AUTO v2.0, provati sul registro vero della 2INF), script automatico (coda, raccolta, ponte, moduli, voti), pagine collegate, giro della lezione.
