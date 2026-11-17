/* Domande della procedura guidata «Documento del progetto» (4TI). Solo italiano.
   Le competenze sono quelle scritte nell'Allegato A della 4TI 2026/27 (parte del docente):
   programmi-ufficiali/2026-27/20261102_ALLEGATO_A__PFP_4_Tecnico_Informatico_2026-2027.docx */
window.PASSI = [
{ id: 1, titolo: "Chi sei e come si chiama il progetto", cap: 1,
  intro: "Scrivi il titolo del progetto, il tuo nome e la tua classe. Il nome resta nel tuo computer.",
  aiuto: ["Il titolo dice che cosa è il progetto, in poche parole.", "Scrivi nome e cognome come li scrivi a scuola.", "Il link di GitHub si scrive solo se il repository c'è già. Altrimenti lascia vuoto."],
  esempio: "Titolo: Sensore di sete per la pianta\nNome e cognome: Nome Cognome\nClasse: 4TI",
  campi: [
    { k: "titolo", tipo: "text", label: "Titolo del progetto", ph: "Per esempio: Sensore di sete per la pianta", max: 90 },
    { k: "nome", tipo: "text", label: "Il tuo nome e cognome", ph: "Nome Cognome", max: 60 },
    { k: "classe", tipo: "text", label: "La tua classe", ph: "4TI", max: 12 },
    { k: "repo", tipo: "text", label: "Link del repository GitHub (se c'è già)", ph: "https://github.com/...", max: 200 }
  ] },
{ id: 2, titolo: "Di che cosa si tratta", cap: 1,
  intro: "Racconta il progetto con parole tue. Poi scrivi che cosa vuoi ottenere e a chi serve.",
  aiuto: ["Descrizione: 5 righe. Che cosa è, che cosa fa, che cosa costruisci.", "Obiettivo: il risultato che vuoi vedere alla fine.", "A chi serve: chi userà il progetto."],
  esempio: "Descrizione: Una piccola scatola con un sensore misura quanto è umida la terra di una pianta. Se la terra è secca si accende una luce rossa. Se è bagnata si accende una luce verde. La scatola sta sul davanzale della classe.\nObiettivo: ricordarsi di annaffiare la pianta al momento giusto.\nA chi serve: agli studenti della classe.",
  campi: [
    { k: "descr", tipo: "area", label: "Descrizione del progetto (circa 5 righe)", rows: 6 },
    { k: "obiettivo", tipo: "area", label: "Obiettivo: che cosa vuoi ottenere", rows: 3 },
    { k: "destinatari", tipo: "area", label: "A chi serve", rows: 2 }
  ] },
{ id: 3, titolo: "Che cosa deve fare e che cosa NON fa", cap: 2,
  intro: "Scrivi una riga per ogni cosa che il progetto deve fare. Poi scrivi le cose che NON fa.",
  aiuto: ["Ogni riga è una azione che si vede o si prova.", "Cominciano bene con un verbo: «Accende», «Misura», «Mostra».", "Le cose che NON fa servono a non promettere troppo."],
  esempio: "Deve fare:\n1. Misura l'umidità della terra ogni 10 secondi.\n2. Accende la luce verde se la terra è bagnata.\n3. Accende la luce rossa se la terra è secca.\nNON fa: non annaffia da solo. Non manda messaggi sul telefono.",
  campi: [
    { k: "fa", tipo: "tabella", label: "Che cosa deve fare", riga: "Requisito", colonne: [{ k: "t", label: "Il progetto deve...", tipo: "area" }], inizio: 3 },
    { k: "nonfa", tipo: "tabella", label: "Che cosa NON fa", riga: "Cosa non fa", colonne: [{ k: "t", label: "Il progetto NON...", tipo: "area" }], inizio: 1 }
  ] },
{ id: 4, titolo: "Competenze richieste", cap: 1,
  intro: "Metti la spunta alle competenze che userai nel progetto. Sono quelle scritte nell'Allegato A della tua classe.",
  aiuto: ["Metti la spunta solo a quello che il progetto usa davvero.", "Se una cosa non c'è nell'elenco, scrivila nella riga libera in fondo.", "Puoi cambiare idea più avanti."],
  esempio: "Competenza 13: Analisi dei requisiti e scelta del progetto; Collaudo e rilascio; Manuale utente.\nCompetenza 15: Autenticazione, password e backup.",
  campi: [
    { k: "comp", tipo: "caselle", label: "Competenze e voci dell'Allegato A", gruppi: [
      { titolo: "Competenza 13: Elaborare prodotti di comunicazione che descrivono prodotti, servizi, componenti o applicazioni conformi con i requisiti relativi alla documentazione, identificando e selezionando lo stile e il media appropriato per il materiale di presentazione", sigla: "Comp. 13", voci: [
        "Analisi dei requisiti e scelta del progetto", "Sviluppo in Lazarus o progettazione della rete", "Controllo di versione con Git", "Collaudo e rilascio", "Relazione tecnica", "Manuale utente", "Presentazione del progetto", "Git e intelligenza artificiale con NotebookLM"] },
      { titolo: "Competenza 14: Curare gli interventi necessari pianificati per implementare la soluzione, tra cui l'installazione, l'aggiornamento e la dismissione, registrando tutte le informazioni rilevanti, compreso gli indirizzi delle apparecchiature, i dati di configurazione e di performance", sigla: "Comp. 14", voci: [
        "Progetto logico della rete", "Configurazione di switch, router e VLAN", "Collaudo con il ping e documentazione"] },
      { titolo: "Competenza 15: Collaborare all'implementazione delle politiche della sicurezza dell'informazione, controllando e attuando interventi a fronte di intrusioni, frodi e buchi o falle della sicurezza al fine di assicurare che i rischi legati siano analizzati e gestiti per i dati e le informazioni aziendali", sigla: "Comp. 15", voci: [
        "Firewall e segmentazione della rete", "Autenticazione, password e backup", "Phishing e intrusioni: rilevamento e contromisure"] },
      { titolo: "Competenza 16: Installare hardware, software o componenti di sottosistema in un sistema esistente o proposto, conformandosi ai processi e alle procedure definite, identificando la compatibilità delle specifiche hardware e software e proponendo eventuali azioni di recupero", sigla: "Comp. 16", voci: [
        "Modelli di riferimento ISO/OSI e TCP/IP: livelli, incapsulamento, viaggio di un pacchetto", "Mezzi di trasmissione: cavo in rame, fibra ottica, Wi-Fi", "Indirizzamento IPv4 e subnetting: maschera, gateway, DHCP, DNS", "Diagnosi dei guasti di rete: il metodo del tecnico, dal livello fisico all'applicazione", "Progettazione di una rete in Cisco Packet Tracer: switch, router, VLAN, collaudo"] },
      { titolo: "Competenza 7: Utilizzare le reti e gli strumenti informatici in maniera consapevole nelle attività di studio, ricerca, sociali e professionali", sigla: "Comp. 7", voci: [
        "Protezione dei dati e GDPR", "Normativa e codice etico", "Intelligenza artificiale: usi e limiti nel lavoro"] }
    ] },
    { k: "comp_altro", tipo: "text", label: "Un'altra competenza che non trovi nell'elenco (riga libera)", ph: "Scrivi qui, se serve", max: 160 }
  ] },
{ id: 5, titolo: "Piano di lavoro e Gantt", cap: 3,
  intro: "Scrivi le fasi del lavoro, una per riga, con la data di inizio e la data di fine. Sotto vedi il disegno del Gantt.",
  aiuto: ["Una fase è un pezzo di lavoro: «Scelgo i componenti», «Costruisco», «Provo».", "Le date si scelgono con il calendario. La fine non può venire prima dell'inizio.", "Nell'ultima colonna scrivi il materiale o il risultato che hai alla fine della fase.", "Il disegno si fa da solo. Va nel Documento come immagine."],
  esempio: "Fase 1: Scelgo i componenti, dal 24/11 al 30/11. Risultato: elenco dei componenti.\nFase 2: Collego il sensore, dal 01/12 al 14/12. Risultato: il sensore misura.\nFase 3: Accendo le luci, dal 15/12 al 21/12. Risultato: rosso e verde funzionano.\nFase 4: Provo e scrivo il manuale, dal 22/12 al 11/01. Risultato: prove fatte.",
  campi: [
    { k: "fasi", tipo: "tabella", label: "Le fasi del lavoro", riga: "Fase", inizio: 3, colonne: [
      { k: "f", label: "Fase", tipo: "text" }, { k: "a", label: "Data di inizio", tipo: "date" }, { k: "b", label: "Data di fine", tipo: "date" }, { k: "m", label: "Materiale o risultato", tipo: "text" }] },
    { k: "gantt", tipo: "gantt", label: "Il tuo Gantt (si disegna da solo)", da: "fasi" }
  ] },
{ id: 6, titolo: "Materiali, componenti e costi", cap: 4,
  intro: "Scrivi che cosa ti serve per il progetto, quanti pezzi e quanto costa un pezzo. Il totale si calcola da solo.",
  aiuto: ["Una riga per ogni cosa: componente, strumento, programma.", "Scrivi il prezzo di UN pezzo, in euro. Si può usare la virgola: 4,50.", "Se una cosa è già tua o è gratis, scrivi 0."],
  esempio: "Scheda Arduino, 1 pezzo, 22 euro.\nSensore di umidità, 1 pezzo, 4,50 euro.\nLuci a LED, 2 pezzi, 0,30 euro l'una.\nTotale: 27,10 euro.",
  campi: [
    { k: "mat", tipo: "tabella", label: "Materiali e costi", riga: "Materiale", inizio: 3, calcolo: "costi", colonne: [
      { k: "c", label: "Componente o materiale", tipo: "text" }, { k: "q", label: "Quanti pezzi", tipo: "num" }, { k: "p", label: "Prezzo di un pezzo (euro)", tipo: "num" }] }
  ] },
{ id: 7, titolo: "Schema e progetto", cap: 5,
  intro: "Spiega come è fatto il progetto. Poi scegli dal computer le immagini degli schemi e delle foto.",
  aiuto: ["Scrivi come sono collegate le parti, una cosa alla volta.", "Per ogni immagine scrivi una didascalia: una frase che dice che cosa si vede.", "Le immagini si ridimensionano da sole a 1000 punti di larghezza."],
  esempio: "Testo: Il sensore va al pin A0. La luce rossa va al pin 7 e la verde al pin 8. Tutto è alimentato dal cavo USB del computer.\nImmagine: Schema dei collegamenti. Didascalia: Schema dei collegamenti tra la scheda, il sensore e le due luci.",
  campi: [
    { k: "schema", tipo: "area", label: "Come è fatto il progetto", rows: 7 },
    { k: "img", tipo: "immagini", label: "Immagini: schemi, disegni, foto" }
  ] },
{ id: 8, titolo: "Diario di realizzazione", cap: 6,
  intro: "Ogni volta che lavori al progetto scrivi la data e che cosa hai fatto. Puoi tornare qui quando vuoi.",
  aiuto: ["Una riga per ogni giorno di lavoro.", "Scrivi che cosa hai fatto, anche se è piccolo.", "Il diario si continua a scrivere nel Documento di Google."],
  esempio: "24/11: ho scelto i componenti e ho scritto l'elenco.\n01/12: ho collegato il sensore e ho letto il primo valore.",
  campi: [
    { k: "diario", tipo: "tabella", label: "Le voci del diario", riga: "Voce", inizio: 2, colonne: [
      { k: "d", label: "Data", tipo: "date" }, { k: "t", label: "Che cosa ho fatto", tipo: "area" }] }
  ] },
{ id: 9, titolo: "Prove e collaudo", cap: 7,
  intro: "Scrivi le prove che fai per controllare che il progetto funziona. Per ogni prova scrivi che cosa ti aspetti e che cosa succede davvero.",
  aiuto: ["Ogni prova controlla una cosa che il progetto deve fare.", "Prima scrivi il risultato che ti aspetti.", "Dopo la prova scrivi il risultato vero. Se è diverso, vai al passo dei problemi."],
  esempio: "Prova: tocco il sensore con la terra bagnata. Risultato atteso: si accende la luce verde. Risultato vero: la luce verde si è accesa.",
  campi: [
    { k: "prove", tipo: "tabella", label: "Le prove", riga: "Prova", inizio: 2, colonne: [
      { k: "p", label: "Prova", tipo: "area" }, { k: "a", label: "Risultato atteso", tipo: "area" }, { k: "v", label: "Risultato vero", tipo: "area" }] }
  ] },
{ id: 10, titolo: "Problemi trovati e soluzioni", cap: 8,
  intro: "Scrivi i problemi che hai trovato e come li hai risolti. Anche i problemi non risolti.",
  aiuto: ["Scrivi il problema come lo vedi: «La luce non si accende».", "Poi scrivi che cosa hai provato e che cosa ha funzionato.", "Se non lo hai risolto, scrivilo: è un dato vero."],
  esempio: "Problema: il sensore dà sempre lo stesso numero.\nSoluzione: il filo era collegato al pin sbagliato. L'ho spostato sul pin A0.",
  campi: [
    { k: "prob", tipo: "tabella", label: "Problemi e soluzioni", riga: "Problema", inizio: 2, colonne: [
      { k: "p", label: "Problema", tipo: "area" }, { k: "s", label: "Soluzione (o come sta andando)", tipo: "area" }] }
  ] },
{ id: 11, titolo: "Manuale utente", cap: 9,
  intro: "Scrivi come si usa il progetto, un passo alla volta. Pensa a una persona che non lo conosce.",
  aiuto: ["Un passo per riga. Ogni passo è una sola azione.", "Cominciano con un verbo: «Collega», «Premi», «Guarda».", "Il numero del passo si mette da solo."],
  esempio: "Passo 1: Collega la scatola al computer con il cavo USB.\nPasso 2: Metti il sensore nella terra della pianta.\nPasso 3: Guarda la luce. Verde: la terra è bagnata. Rossa: serve acqua.",
  campi: [
    { k: "man_serve", tipo: "area", label: "Che cosa serve per usarlo (prima di cominciare)", rows: 3 },
    { k: "man", tipo: "tabella", label: "I passi", riga: "Passo", inizio: 3, numerata: true, colonne: [{ k: "t", label: "Che cosa fa chi usa il progetto", tipo: "area" }] }
  ] },
{ id: 12, titolo: "Sicurezza e privacy", cap: 10,
  intro: "Scrivi che cosa può andare storto per la sicurezza e che cosa fai per proteggere le persone e i dati.",
  aiuto: ["Sicurezza: corrente, caldo, parti che si rompono, password.", "Privacy: il progetto raccoglie dati di persone? Quali? Dove stanno?", "Se il progetto non raccoglie dati di persone, scrivilo."],
  esempio: "Sicurezza: la scheda usa 5 volt dal cavo USB, non c'è corrente pericolosa. I fili sono fermati con il nastro.\nPrivacy: il progetto non raccoglie nessun dato di persone.",
  campi: [
    { k: "sic", tipo: "area", label: "Sicurezza: rischi e protezioni", rows: 5 },
    { k: "priv", tipo: "area", label: "Privacy: dati di persone e come li proteggo", rows: 5 }
  ] },
{ id: 13, titolo: "Formato di presentazione", cap: 1,
  intro: "Come presenterai il progetto? Metti la spunta a tutti i modi che userai.",
  aiuto: ["Puoi scegliere più di un modo.", "La durata è in minuti.", "Scrivi che cosa mostrerai: la parte più importante del progetto."],
  esempio: "Formato: dimostrazione dal vivo e slide.\nDurata: 5 minuti.\nCosa mostro: la scatola che cambia luce quando bagno la terra.",
  campi: [
    { k: "formati", tipo: "caselle", label: "Come presento il progetto", gruppi: [{ titolo: "", sigla: "", voci: ["Slide", "Video", "Poster", "Dimostrazione dal vivo", "Relazione scritta"] }] },
    { k: "formato_altro", tipo: "text", label: "Un altro modo (riga libera)", ph: "Scrivi qui, se serve", max: 100 },
    { k: "durata", tipo: "text", label: "Quanto dura la presentazione (minuti)", ph: "Per esempio: 5", max: 20 },
    { k: "mostro", tipo: "area", label: "Che cosa mostrerò", rows: 3 }
  ] },
{ id: 14, titolo: "Documentazione tecnica e scientifica", cap: 12,
  intro: "Scrivi le fonti che hai usato: siti, libri, schede tecniche (datasheet), norme. Una riga per ogni fonte.",
  aiuto: ["Scrivi il titolo, l'autore, l'anno e l'indirizzo o il posto dove si trova.", "Se non sai l'autore o l'anno, lascia vuoto.", "Gli allegati sono file o link che aggiungi al Documento: foto, codice, schemi."],
  esempio: "Tipo: scheda tecnica. Titolo: Scheda del sensore di umidità. Autore: il produttore. Anno: 2020. Indirizzo: il sito del produttore.",
  campi: [
    { k: "fonti", tipo: "tabella", label: "Le fonti", riga: "Fonte", inizio: 2, colonne: [
      { k: "tp", label: "Tipo", tipo: "scelta", opz: ["Sito web", "Libro", "Scheda tecnica (datasheet)", "Norma", "Articolo", "Video", "Altro"] },
      { k: "ti", label: "Titolo", tipo: "text" }, { k: "au", label: "Autore", tipo: "text" }, { k: "an", label: "Anno", tipo: "text" }, { k: "ur", label: "Indirizzo o dove si trova", tipo: "text" }] },
    { k: "allegati", tipo: "area", label: "Allegati: file o link da aggiungere (codice, foto, schemi)", rows: 3 }
  ] },
{ id: 15, titolo: "Conclusioni e autovalutazione", cap: 11,
  intro: "Ultima domanda. Scrivi come è andato il progetto e che cosa hai imparato.",
  aiuto: ["Conclusioni: il progetto fa quello che volevi?", "Scrivi anche le cose che non hanno funzionato.", "Autovalutazione: guarda le competenze scelte al passo 4. Che cosa sai fare adesso?"],
  esempio: "Conclusioni: la scatola funziona. La luce cambia colore quando la terra cambia.\nHa funzionato: il sensore e le luci.\nFarei diversamente: userei una scatola più grande.\nHo imparato: a leggere un sensore e a scrivere un manuale.",
  campi: [
    { k: "concl", tipo: "area", label: "Conclusioni: il progetto fa quello che volevi?", rows: 4 },
    { k: "ok", tipo: "area", label: "Che cosa ha funzionato bene", rows: 3 },
    { k: "meglio", tipo: "area", label: "Che cosa farei in modo diverso", rows: 3 },
    { k: "imparato", tipo: "area", label: "Che cosa ho imparato di nuovo, e che cosa so fare adesso", rows: 4 }
  ] }
];

/* I 12 capitoli del Documento (stessi titoli della guida e del modello .docx) */
window.CAPITOLI = [
  { n: 1, t: "Scheda del progetto", passi: [1, 2, 4, 13], keys: ["titolo", "nome", "descr", "obiettivo", "destinatari", "comp", "formati", "durata", "mostro"] },
  { n: 2, t: "Analisi e requisiti", passi: [3], keys: ["fa", "nonfa"] },
  { n: 3, t: "Piano di lavoro e Gantt", passi: [5], keys: ["fasi"] },
  { n: 4, t: "Materiali e costi", passi: [6], keys: ["mat"] },
  { n: 5, t: "Schema e progetto", passi: [7], keys: ["schema", "img"] },
  { n: 6, t: "Realizzazione e diario", passi: [8], keys: ["diario"] },
  { n: 7, t: "Prove e collaudo", passi: [9], keys: ["prove"] },
  { n: 8, t: "Problemi e soluzioni", passi: [10], keys: ["prob"] },
  { n: 9, t: "Manuale utente", passi: [11], keys: ["man_serve", "man"] },
  { n: 10, t: "Sicurezza e privacy", passi: [12], keys: ["sic", "priv"] },
  { n: 11, t: "Conclusioni e autovalutazione", passi: [15], keys: ["concl", "ok", "meglio", "imparato"] },
  { n: 12, t: "Fonti e allegati", passi: [14], keys: ["fonti", "allegati"] }
];
