# Lazarus: la finestra, i componenti, il clic

**Versione 1.0** - 04/11/2026
*Dispensa di ripasso · Classe 1INF · 04/11/2026 · Laboratorio*

Questa dispensa ti serve per ripassare quello che sai già: come è fatta la finestra di Lazarus, i pezzi che metti nel programma (bottone, casella, etichetta) e che cosa succede quando clicchi. Leggila con calma. Alla fine c'è un esercizio da 5 minuti: lo fai e funziona subito. Se sbagli qualcosa non fa niente: succede a tutti i programmatori, anche ai professionisti.

## 1. La mappa di Lazarus
*Schema disegnato (non è una foto): le parti di Lazarus che usi sempre.* (schema nel PDF)

1. **Barra dei comandi.** In alto: i menu (File, Progetto, Esegui) e il bottone verde con il triangolo, **Esegui**. Anche il tasto `F9` fa partire il tuo programma.
2. **Palette dei componenti.** La fila di pezzi pronti, sotto i menu. Nella scheda **Standard** ci sono il bottone, la casella, l'etichetta. Clic sul pezzo, poi clic sulla finestra: il pezzo si mette lì.
3. **Ispettore oggetti.** A sinistra. Mostra il pezzo selezionato. La scheda **Proprietà** dice come è fatto (testo, nome, grandezza). La scheda **Eventi** dice a che cosa risponde (per esempio al clic).
4. **Form1.** La finestra del tuo programma, al centro. È il foglio dove disegni: ci metti sopra i pezzi.
5. **Editor del codice.** A destra (o dietro la finestra). Qui scrivi le istruzioni. Con `F12` passi dalla finestra al codice e viceversa.
6. **Finestra Messaggi.** In basso. Quando c'è un errore, scrive quale riga è sbagliata.

Non trovi più una finestra? Menu **Visualizza** e la riapri. Non stai rovinando niente.

## 2. I componenti che abbiamo usato
Un **componente** è un pezzo già pronto, come un mattoncino. Lo prendi dalla palette e lo metti nella finestra. Ogni componente ha un tipo che inizia con la lettera **T**.

| Componente | A che cosa serve | Proprietà da ricordare |
|---|---|---|
| **TButton** (bottone) | Si clicca. Fa partire il tuo codice. | `Caption` = la scritta sul bottone ; `Name` = il nome per il codice (Button1) |
| **TEdit** (casella) | L'utente ci scrive dentro (un nome, un numero). | `Text` = ciò che c'è scritto ; `Name` = Edit1 |
| **TLabel** (etichetta) | Mostra una scritta. Il programma la cambia. | `Caption` = la scritta che si vede ; `Name` = Label1 |
| **TMemo** (blocco di righe) | Mostra tante righe di testo (lo scontrino del cassiere). | `Lines` = le righe ; `Name` = Memo1 |

Nel Convertitore di misure: scrivi **5** nella casella (TEdit), clicchi il bottone (TButton) e l'etichetta (TLabel) mostra **5000 metri**.

## 3. L'evento OnClick: il clic che fa partire il codice
Un **evento** è una cosa che succede: un clic, per esempio. Lazarus aspetta il clic. Quando arriva, esegue il tuo codice. Tu scrivi solo che cosa deve fare.

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  Label1.Caption := 'Ciao!';
end;
```

Come lo crei: **doppio clic sul bottone** nella finestra. Lazarus scrive da solo le righe `procedure`, `begin` ed `end;`. Tu scrivi solo la riga in mezzo. Leggila così: **«nell'etichetta, la scritta diventa Ciao!»**. Il segno `:=` vuol dire «diventa». Il `;` chiude la riga, come il punto in una frase.

Gli errori più comuni: manca il `;`, hai scritto `=` invece di `:=`, manca un apice `'`.

## 4. Il ponte: dalla Form alla finestra di Lazarus
Molte cose le conosci già dalle lezioni passate. Questa tabella le mette insieme.

| Lo sai già | In Lazarus si chiama | Un esempio |
|---|---|---|
| La finestra del programma | **Form** (Form1) | la finestra con il bottone |
| I pezzi nella finestra | **Componenti** | TButton, TEdit, TLabel |
| Le caratteristiche di un pezzo | **Proprietà** | Caption, Text, Name |
| Una cosa che succede | **Evento** | OnClick (il clic) |

### Mini glossario

| Parola | Che cosa vuol dire |
|---|---|
| Caption | il testo che si **vede** sul bottone o sull'etichetta |
| Text | il testo che c'è **scritto dentro** la casella |
| Name | il nome **interno**, che usa il codice (Button1, Edit1) |
| Form | la finestra del programma |
| Event (evento) | una cosa che succede, come un clic |
| Run (Esegui) | far partire il programma (tasto F9) |

## 5. Esercizio: vinci subito in 5 minuti
Un bottone che, al clic, cambia la scritta di un'etichetta. Quasi impossibile sbagliare.

1. Apri Lazarus. Menu **Progetto**, poi **Nuovo progetto**, poi **Applicazione**. Salva subito nella tua cartella dentro **Documenti\Lazarus**.
2. Nella palette, scheda **Standard**, clicca il pezzo **TButton** e poi clicca nella finestra Form1.
3. Nella palette clicca il pezzo **TLabel** e poi clicca nella finestra, sotto il bottone.
4. Clicca il bottone. Nell'Ispettore oggetti, scheda Proprietà, cambia `Caption` in **Premimi**.
5. Fai **doppio clic sul bottone**. Si apre il codice. Tra `begin` e `end;` ricopia la riga qui sotto.
6. Premi `Ctrl` + `S` per salvare, poi `F9`. Clicca il bottone: la scritta cambia. FATTO! Hai fatto un programma tuo.

```
Label1.Caption := 'Ciao, funziona!';
```

### Fallo tuo

1. Al posto di `Ciao, funziona!` scrivi una frase tua (il tuo nome, la tua squadra, un saluto).
2. Clicca la Form1 e cambia la proprietà `Color`: scegli il tuo colore preferito.
3. Cambia il `Caption` del bottone con una parola tua. Fai provare il programma a un compagno.

### Da ricopiare sul quaderno

Ricopia queste righe. Poi spiegale a voce a un compagno con parole tue.

```
Form = la finestra
Componente = un pezzo (TButton, TEdit, TLabel)
Proprietà = come è fatto (Caption, Text, Name)
Evento = cosa succede (OnClick = il clic)
clic -> OnClick -> il mio codice
F9 = Esegui
```

## 6. Ripasso: 5 domande per te
Rispondi sul quaderno, poi controlla le risposte qui sotto.

1. Come si chiama il pezzo che si clicca?
2. Quale proprietà cambia la scritta di un bottone o di un'etichetta?
3. Che tasto fa partire il programma?
4. Che cosa fa il doppio clic su un bottone?
5. Che cosa significa `:=` in `Label1.Caption := 'Ciao';`?

### Risposte

1. TButton (il bottone).
2. La proprietà Caption.
3. Il tasto F9 (oppure il bottone verde Esegui).
4. Crea la procedura del clic (OnClick) e ti porta nel codice, dove scrivi che cosa fare.
5. Vuol dire «diventa»: la scritta dell'etichetta diventa Ciao.

Bravo! Ripassare così è il modo giusto per ricordare. Alla prossima.
