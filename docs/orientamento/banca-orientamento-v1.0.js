/* Banca del test di orientamento — Versione 1.0 — 21/10/2026.
   Test per ragazzi di terza media (circa 1 ora). Una versione nuova = un file nuovo (banca-orientamento-v1.1.js …)
   e il numero in index.html. Domande a crocette: [testo, risposta giusta, [sbagliate]]. Nessun dato raccolto. */
window.BANCA_ORIENTAMENTO = {
  versione: "1.0",
  blocchi: [
    { id: "logica", titolo: "Logica", minuti: 10,
      intro: "Ragiona con calma. Non servono calcoli difficili: guarda bene e trova la regola.",
      domande: [
        ["Che numero viene dopo? 2, 4, 8, 16, …", "32", ["24", "20", "18"]],
        ["Che lettera viene dopo? A, C, E, G, …", "I", ["H", "L", "J"]],
        ["Quale parola non c'entra con le altre?", "rosa", ["cane", "gatto", "cavallo"]],
        ["Tutti i gatti sono animali. Fufi è un gatto. Allora…", "Fufi è un animale", ["Fufi non è un animale", "Tutti gli animali sono gatti", "Non si può sapere"]],
        ["Marco è più alto di Luca. Luca è più alto di Anna. Chi è il più basso?", "Anna", ["Marco", "Luca", "Non si può sapere"]],
        ["Oggi è lunedì. Che giorno sarà tra 10 giorni?", "giovedì", ["mercoledì", "venerdì", "lunedì"]],
        ["Che numero viene dopo? 1, 1, 2, 3, 5, 8, …", "13", ["11", "12", "16"]]
      ] },
    { id: "matematica", titolo: "Matematica", minuti: 15,
      intro: "Puoi usare carta e penna. Non usare la calcolatrice.",
      domande: [
        ["Quanto fa 7 × 8?", "56", ["54", "48", "64"]],
        ["Quanto è il 25% di 80?", "20", ["25", "40", "16"]],
        ["Un telefono costa 200 €. Con lo sconto del 10% quanto costa?", "180 €", ["190 €", "100 €", "20 €"]],
        ["3 quaderni costano 6 €. Quanto costano 5 quaderni?", "10 €", ["8 €", "11 €", "15 €"]],
        ["Risolvi: 3x + 5 = 20. Quanto vale x?", "5", ["15", "8", "3"]],
        ["Un rettangolo è lungo 6 cm e largo 4 cm. Quanto è la sua area?", "24 cm²", ["20 cm²", "10 cm²", "48 cm²"]],
        ["Qual è la media di 4, 6 e 8?", "6", ["5", "18", "7"]],
        ["Un film dura 1 ora e 45 minuti. Inizia alle 20:30. A che ora finisce?", "22:15", ["21:75", "22:05", "21:45"]]
      ] },
    { id: "informatica", titolo: "Informatica pratica", minuti: 20,
      intro: "Prima porti il robot alla bandiera con i blocchi, poi rispondi a poche domande.",
      robot: [
        { nome: "Livello 1", righe: ["R...B"] },
        { nome: "Livello 2", righe: ["R....", ".....", "....B"] },
        { nome: "Livello 3", righe: ["R.#..", "..#..", "....B"] },
        { nome: "Livello 4", righe: ["R#...", ".#.#.", ".#.#.", "...#B"] }
      ],
      domande: [
        ["Un programma dice: «ripeti 3 volte: fai un passo avanti». Quanti passi fa il robot?", "3", ["1", "4", "6"]],
        ["Che cos'è un algoritmo?", "una serie di passi in ordine per risolvere un problema", ["un tipo di computer", "un virus", "un sito internet"]],
        ["Quale di questi serve per mettere dati DENTRO il computer?", "la tastiera", ["il monitor", "la stampante", "le casse"]],
        ["Nel sistema binario si usano solo le cifre…", "0 e 1", ["da 0 a 9", "1 e 2", "A e B"]],
        ["Il numero binario 101 vale, in decimale…", "5", ["101", "3", "6"]],
        ["Una foto pesa 2 MB. Quante ne stanno in 10 MB?", "5", ["20", "8", "12"]]
      ] },
    { id: "motivazione", titolo: "Motivazione e autovalutazione", minuti: 10,
      intro: "Qui non ci sono risposte giuste o sbagliate. Rispondi sinceramente: serve solo a te.",
      scala: ["per niente", "poco", "abbastanza", "molto", "moltissimo"],
      frasi: [
        "Mi piace capire come funzionano le cose (un'app, un gioco, un computer).",
        "Mi piace usare il computer per CREARE qualcosa, non solo per giocare o guardare video.",
        "Quando un problema è difficile, provo ancora invece di lasciar perdere.",
        "Mi piacerebbe creare un videogioco, un sito o un'app.",
        "Mi piace montare, smontare o aggiustare oggetti e dispositivi.",
        "Mi piace lavorare in gruppo con i compagni.",
        "Mi piacerebbe fare un lavoro con i computer da grande."
      ] }
  ]
};
