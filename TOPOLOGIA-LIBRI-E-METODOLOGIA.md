# Topologia dei libri e metodologia di lavoro

**Versione 0.1** — 30/09/2026 · Corso Informatica (Piamarta)

*Documento di riferimento del docente. Fissa in modo stabile: come sono fatti i
libri del corso (tipi, contenuti, nomi, versioni), come si generano da fonti
uniche senza rifare il lavoro, e come si tiene tutto ordinato ed efficiente su
Git. Nasce dal modo di lavorare messo a punto nelle lezioni di fine settembre
2026. Non contiene nomi di allievi: è materiale di metodo, condivisibile.*

---

## 00 Scopo e come si usa

1. Questo file è la **mappa del sistema**: se tra sei mesi ci si chiede "che tipi
   di libri abbiamo, come si chiamano, da dove nascono e come li aggiorno senza
   perdere tempo", la risposta è qui.
2. La regola d'oro di tutto il sistema è una sola: **una cosa si scrive una volta
   sola** (in una fonte unica) e da lì si **genera** ovunque serva. Niente
   copia-incolla manuale che poi va tenuto allineato a mano.
3. Il **PDF** è la resa da leggere/stampare; l'**MD** è la fonte versionata (sta
   su Git) e si dà anche ai ragazzi per la loro IA (che spiega/traduce).

## 01 I principi (il modo di lavorare)

1. **Git come archivio e struttura, non come ripostiglio.** Ogni materiale utile
   sta su Git in una struttura logica riusabile (fonti, generatori, indici,
   registro). Così il lavoro non si perde e non si rifà.
2. **Fonti uniche + generazione.** I contenuti stanno in una sola fonte; i
   documenti finali (manuale, libri, griglie) si **costruiscono** da quella.
3. **Le fonti si versionano, gli output si rigenerano.** Su Git stanno i file
   sorgente (testo, dati, script). I prodotti pesanti (PDF, ZIP, immagini) NON si
   versionano: si ricreano quando servono. Questo tiene i repository leggeri e
   veloci.
4. **Due ambienti.** `main` = cucina dell'autore (Nicola): si lavora e si migliora.
   Le **Release** taggate (`v1.0`, `v1.1`…) = versioni congelate per i ragazzi.
5. **Due repository per riservatezza** (dettaglio nel capitolo 05).
6. **Privacy dei minori.** Nomi, voti nominali, presenze e osservazioni non
   stanno mai sul repository pubblico (vedi 05 e 07).
7. **Tre lingue per gli allievi.** Ogni testo destinato agli allievi esiste in
   versione italiana per tutti e, dove serve, bilingue (Classe 1: IT/AR/ZH;
   Classe 3: IT + bangla). I materiali per il docente restano in italiano.
8. **PPP = "parcheggia".** Quando una richiesta inizia con `PPP`, si annota e si
   prepara in silenzio, ma non si consegna l'output finale finché non si dice
   "avanti" (eccezione: se dentro il PPP c'è un'azione concreta esplicita, quella
   si fa subito). Senza `PPP`, si procede.

## 02 La topologia dei libri (i tipi)

> I libri del corso sono quattro tipi. Cambiano l'**asse** con cui sono
> organizzati (per argomento oppure per data) e il **destinatario**.

### 02.1 Tipo A — Manuale / Libro totale (per ARGOMENTO)
1. **Cos'è:** il libro di teoria organizzato per argomento, non per data.
2. **Struttura a 3 livelli** per ogni argomento: (1) base, (2) intermedio,
   (3) avanzato. Chi vuole solo l'essenziale legge il livello 1; chi vuole
   approfondire scende ai livelli 2 e 3.
3. **Fonte:** la cartella `argomenti/` (un file per argomento, con dentro i 3
   livelli). Il Manuale si **genera** da lì.
4. **Per chi:** tutti; è il riferimento teorico stabile che cresce nel tempo.

### 02.2 Tipo B — Libro complessivo di classe (per DATA)
1. **Cos'è:** raccoglie, lezione per lezione, la **teoria** spiegata e la
   **descrizione dei compiti** assegnati a quella classe. Senza nomi.
2. **Core vs Approfondimento:** il "core" è ciò che ha fatto **quella** classe;
   il meglio fatto nelle altre classi entra come **"Approfondimento"** in un
   riquadro distinto.
3. **Per chi:** gli allievi della classe; è il loro libro di testo che cresce a
   ogni lezione.

### 02.3 Tipo C — Libro individuale (per DATA, personale)
1. **Cos'è:** il libro B **più** il lavoro realmente svolto dal singolo allievo,
   **valutato**. Ricalca l'esperienza dell'allievo: teoria, testo del compito,
   il suo compito con screenshot e codice, la **valutazione compito per compito**,
   la sua **riflessione** e (dove ci sono) le foto della lavagna.
2. **Valutazione:** sempre **per singolo compito**, mai un voto complessivo unico.
3. **Riservato:** contiene il nome dell'allievo e i voti → sta nel repository
   privato / si consegna in PDF; mai sul pubblico.
4. **Per chi:** il singolo allievo (motore "Mostralo" + prova del nove).

### 02.4 Tipo D — Libro parziale (una giornata o una lezione)
1. **Cos'è:** un sottoinsieme di B o C limitato a una giornata o a una singola
   lezione. Utile per consegne rapide.
2. **Come:** stesso generatore, con un filtro per data/giornata.

### 02.5 Schema riassuntivo
1. **Asse per ARGOMENTO** → Tipo A (Manuale).
2. **Asse per DATA, senza nomi** → Tipo B (Libro di classe).
3. **Asse per DATA, con nome + valutazione** → Tipo C (Libro individuale, riservato).
4. **Sottoinsieme di B o C** → Tipo D (parziale).

## 03 Le fonti uniche a 3 livelli (niente doppio lavoro)

1. **Dove:** cartella `argomenti/`. Un file Markdown per argomento (es.
   `cattura-schermo.md`, `stampanti.md`).
2. **Dentro ogni argomento** ci sono tre sezioni: `## Livello 1` (base),
   `## Livello 2` (intermedio), `## Livello 3` (avanzato).
3. **Da qui si genera il Manuale (Tipo A):** ogni argomento diventa un capitolo
   con i tre livelli evidenziati.
4. **Le lezioni (Tipo B e C) richiamano gli argomenti:** la teoria di una lezione
   non si riscrive, si prende dall'argomento. Così, se si corregge una spiegazione
   in un solo posto (l'argomento), si aggiornano insieme Manuale e libri.
5. **Vantaggio:** un errore si corregge una volta; la qualità sale ovunque; il
   tempo di preparazione crolla.

## 04 Nomi e versioni

1. **Versione nell'intestazione:** ogni documento porta `**Versione X.Y**` in
   testa; l'indice generale tiene la riga corrispondente.
2. **Versione nel nome del PDF:** il consegnabile si chiama `nome-vX.Y.pdf`, mai
   un generico `nome.pdf`. Due versioni non si sovrascrivono mai.
3. **Congelamento:** una versione consegnata è congelata; se cambia il contenuto
   si **bumpa** il numero e si aggiunge una riga al changelog. Mai riusare un
   numero già consegnato.
4. **Schemi di nome ricorrenti:**
   1. `Manuale-Informatica_vX.Y` (Tipo A).
   2. `Libro-Classe-N_COMPLESSIVO_vX.Y` (Tipo B).
   3. `Libro-Individuale_Cognome-Nome_Classe-N_..._RISERVATO` (Tipo C).
   4. Materiali per data: prefisso `AAAAMMGG_` (es. `20260930_...`).
5. **Header/footer:** banda per unità (macro-argomento · materia · data · orario ·
   contenuto) + footer di pagina, come da `REGOLE-FORMATTAZIONE.md`.

## 05 I due repository (cosa va dove)

1. **Pubblico — `corso-informatica`** (ex `corso-godot`, che resta come redirect;
   contiene anche i **giochi Godot**). Tiene solo materiale **condivisibile**:
   didattica, manuale, libri di classe (senza nomi), esercizi, esperimenti e
   giochi/siti dei ragazzi. **Mai** nomi di minori, voti nominali o dati personali.
2. **Privato — `corso-informatica-riservato`.** Tiene tutto ciò che è
   **riservato, strategico o personale**: nomi, voti nominali, presenze,
   anti-plagio, dati di rete, dati personali del docente. Struttura:
   1. `dati/` — fonte di verità (dati per i libri individuali, `anagrafiche/`,
      `presenze/`).
   2. `generatori/` — script che producono output con i nomi.
   3. `antiplagio/` — modulo e profili.
   4. `strategico/` — rete, gestione classi, `personale/`, `password/`.
3. **Regola pratica:** riservato/strategico/personale → privato · didattica
   condivisibile + esperimenti dei ragazzi → pubblico.
4. **I libri individuali (Tipo C)** si generano con lo **stesso generatore** del
   pubblico, a cui si passano i **dati dal privato**: la teoria resta pubblica, i
   nomi restano privati, zero duplicazione.

## 06 Operatività: il giro di ogni lezione

1. **Prima/durante:** la teoria nuova entra come argomento (`argomenti/`, 3
   livelli); il testo del compito entra nel libro di classe (Tipo B).
2. **Consegne dei ragazzi:** si raccolgono (di norma un solo Documento Google per
   allievo: screenshot + codice + riflessione).
3. **Valutazione:** per ogni compito si producono due griglie per il docente —
   (a) griglia **completa** (tutte le note + cosa non ha fatto in neretto + voto),
   (b) griglia **incrementale** (una colonna per compito che si accumula nel
   tempo). Entrambe riservate.
4. **Libri individuali:** si (ri)generano dal libro di classe + i dati riservati
   dell'allievo; escono in PDF e si consegnano.
5. **Registro:** le presenze e il programma vanno nel privato; il registro ore
   pubblico (senza nomi) tiene il calendario navigabile per giorno/classe/materia.
6. **Chiusura:** si rigenerano solo gli output cambiati; le fonti sono già su Git.

## 07 Privacy e sicurezza (minori)

1. Nomi, voti nominali, presenze e osservazioni sui singoli **non** stanno mai sul
   repository pubblico.
2. Il modulo anti-plagio e i profili degli allievi sono accessibili **solo al
   docente** (repository privato). Agli allievi arriva solo il **risultato** (la
   loro valutazione, il loro libro).
3. I PDF riservati si consegnano al docente; non si versionano nel pubblico.

## 08 Glossario minimo

1. **Fonte unica:** l'unico file dove un contenuto è scritto; tutto il resto si
   genera da lì.
2. **Generare:** costruire un documento finale a partire dalle fonti, con uno
   script, invece di scriverlo a mano.
3. **Rigenerabile:** un file che si può ricreare in ogni momento dalle fonti (per
   questo non si versiona).
4. **Bump di versione:** aumentare il numero di versione quando il contenuto cambia.
5. **Core / Approfondimento:** core = ciò che ha fatto quella classe; approfondimento
   = il meglio fatto nelle altre classi, in un riquadro distinto.
6. **Repository pubblico / privato:** il primo condivisibile, il secondo riservato.

## 09 Changelog
1. **v0.1 (30/09/2026):** prima stesura. Fissa topologia (tipi A/B/C/D), fonti a 3
   livelli, nomi/versioni, i due repository e l'operatività di ogni lezione.
