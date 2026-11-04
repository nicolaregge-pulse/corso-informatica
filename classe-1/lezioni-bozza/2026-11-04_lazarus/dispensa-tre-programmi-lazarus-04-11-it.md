# Tre programmi in Lazarus

*Convertitore di misure · Calcolatrice a 4 bottoni · Il cassiere*

Dispensa · Classe 1INF · Laboratorio · 04/11/2026 · Versione 1.0

Oggi fai tre programmi veri. Ognuno funziona subito e lo puoi far provare a un compagno. Il codice qui è lo stesso delle pagine della lezione: copia e ricopia senza paura. Se sbagli qualcosa non fa niente: succede a tutti i programmatori, anche ai professionisti.

## 01 Come far girare il programma

*Schema disegnato (non è uno screenshot): dove si preme e dove compare il programma.* (schema nel PDF)

1. Salva con `Ctrl` + `S`.
2. Premi `F9`, oppure il bottone verde con il triangolo (**Esegui**) sotto i menu.
3. Aspetta qualche secondo: in basso, nella finestra **Messaggi**, Lazarus costruisce il programma. Se compare una riga rossa c'è un errore (vedi gli errori comuni di ogni programma).
4. La tua finestra si apre **sopra** Lazarus, come un programma vero. Non la vedi? Guardala nella barra in basso di Windows, vicino all'orologio.
5. Prova il programma: scrivi i numeri nelle caselle e premi i bottoni.
6. Per fermarlo: clicca la **X** rossa in alto a destra della tua finestra. Se è bloccato: premi `Ctrl` + `F2` dentro Lazarus.
7. Torna a modificare: il codice e la finestra sono ancora lì. Cambia, salva, premi di nuovo `F9`.

> **Dove si trova il programma:** quando premi `F9`, Lazarus crea nella cartella del progetto (per esempio `Documenti\convertitore`) un file con lo stesso nome del progetto e la fine `.exe`, per esempio `convertitore.exe`. È il tuo programma: con doppio clic parte anche senza Lazarus. Se non lo vedi, il programma non è stato costruito: guarda la finestra Messaggi.

## 02 I passi sempre uguali (per tutti e tre i programmi)

Questi sei passi li ripeti in ogni programma. Nelle ricette sotto trovi la lettera (A, B, C, D, E, F): guarda il disegno con la stessa lettera.

1. **A**: Nuovo progetto: Progetto → Nuovo progetto… → Applicazione → OK
2. **B**: Salva: cartella nuova in Documenti, poi Salva due volte
3. **C**: Palette Standard: clic sul pezzo, poi clic sulla Form
4. **D**: Ispettore oggetti: cambia Caption o Text
5. **E**: Doppio clic sul bottone: si apre il codice
6. **F**: F9: il programma parte

### Parole da sapere

| Parola | Che cosa fa | Esempio |
|---|---|---|
| `StrToInt('5')` | da testo a numero (si blocca se non è un numero) | `'5'` diventa `5` |
| `StrToIntDef('ab', 0)` | da testo a numero; se non va, usa 0 e NON si blocca | `'ab'` diventa `0`; `'7'` diventa `7` |
| `IntToStr(5000)` | da numero a testo | `5000` diventa `'5000'` |
| `div` | divisione senza virgola | `17 div 5 = 3` |
| `mod` | quello che avanza | `17 mod 5 = 2` |
| `+` con testi | unisce due testi | `'Ciao ' + 'Anna'` |

> **Testo contro numero:** `'5' + '3'` fa `'53'` (due testi incollati). `5 + 3` fa `8` (due numeri). Per questo si converte sempre: prima da testo a numero per fare i conti, poi da numero a testo per scrivere il risultato.

## 03 Programma 1: il convertitore di misure

**A che cosa serve.** Scrivi un numero, premi un bottone e il programma lo trasforma: chilometri in metri, ore in minuti, euro in centesimi, gradi Celsius in Fahrenheit, minuti in ore e minuti. **Quando funziona** vedi questo:

*Schema disegnato: il convertitore finito.* (schema nel PDF)

*Schema con i numeri: i numeri rossi sono quelli della tabella.* (schema nel PDF)

| N. | Name | Tipo | Che cosa cambi |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` vuoto |
| 2 | `Label1` | TLabel | niente (la riempie il codice) |
| 3 | `Button1` | TButton | `Caption` = `Km in metri` |
| 4 | `Button2` | TButton | `Caption` = `Ore in minuti` |
| 5 | `Button3` | TButton | `Caption` = `Euro in centesimi` |
| 6 | `Button4` | TButton | `Caption` = `Celsius in Fahrenheit` |
| 7 | `Button5` | TButton | `Caption` = `Minuti in ore e minuti` |

### La ricetta, un'azione per riga

1. [A] Apri Lazarus: menu `Progetto`, `Nuovo progetto…`, `Applicazione`, `OK`.
2. [B] Menu `Progetto`, `Salva progetto con nome…`: in `Documenti` crea la cartella `convertitore`, scrivi `convertitore` come nome file e premi `Salva` (poi ancora `Salva` per `unit1.pas`).
3. [C] Palette `Standard`: clic su `TEdit`, poi clic sulla Form in alto.
4. [C] Clic su `TLabel`, poi clic sulla Form sotto la casella.
5. [C] Clic su `TButton`, poi clic sulla Form sotto l'etichetta.
6. [D] Clicca `Button1`. Nell'Ispettore oggetti scrivi in `Caption`: `Km in metri`.
7. [D] Clicca `Edit1`. Nell'Ispettore cancella il valore di `Text`: deve restare vuoto.
8. [E] Doppio clic su `Button1`: si apre il codice.
9. Tra `begin` e `end;` Lazarus ha già scritto l'inizio. Completa il gestore così (il codice completo è qui sotto):

```
procedure TForm1.Button1Click(Sender: TObject);
var
  km, metri: Integer;
begin
  km := StrToInt(Edit1.Text);
  metri := km * 1000;
  Label1.Caption := IntToStr(metri) + ' metri';
end;
```

10. [F] Premi `F9`, scrivi `5` nella casella e premi il bottone.

> **Vinci subito (5 minuti):** con `5` deve comparire **5000 metri**. FATTO! Hai fatto il tuo primo programma.

**Gli altri quattro bottoni:** stesso metodo (clicca il pezzo, scrivi `Caption`, doppio clic, ricopia il codice). Il codice cambia solo nel conto.

Ore in minuti (`Button2`). Prova `2`: **120 minuti**.

```
procedure TForm1.Button2Click(Sender: TObject);
var
  ore, minuti: Integer;
begin
  ore := StrToInt(Edit1.Text);
  minuti := ore * 60;
  Label1.Caption := IntToStr(minuti) + ' minuti';
end;
```

Euro in centesimi (`Button3`). Prova `3`: **300 centesimi**.

```
procedure TForm1.Button3Click(Sender: TObject);
var
  euro, centesimi: Integer;
begin
  euro := StrToInt(Edit1.Text);
  centesimi := euro * 100;
  Label1.Caption := IntToStr(centesimi) + ' centesimi';
end;
```

Celsius in Fahrenheit (`Button4`). `c * 9 div 5 + 32`. Prova `100`: **212**.

```
procedure TForm1.Button4Click(Sender: TObject);
var
  c, f: Integer;
begin
  c := StrToInt(Edit1.Text);
  f := c * 9 div 5 + 32;
  Label1.Caption := IntToStr(c) + ' gradi C sono ' + IntToStr(f) + ' gradi F';
end;
```

Minuti in ore e minuti (`Button5`): `div` dà le ore intere, `mod` quello che avanza. Prova `135`: **2 ore e 15 minuti**.

```
procedure TForm1.Button5Click(Sender: TObject);
var
  minuti, ore, resto: Integer;
begin
  minuti := StrToInt(Edit1.Text);
  ore := minuti div 60;
  resto := minuti mod 60;
  Label1.Caption := IntToStr(minuti) + ' minuti sono ' + IntToStr(ore) + ' ore e ' + IntToStr(resto) + ' minuti';
end;
```

### Che cosa fanno le istruzioni nuove

`StrToInt(Edit1.Text)` legge il testo della casella e lo fa numero: se scrivi `5`, diventa `5`. `IntToStr(metri)` fa il contrario: `5000` diventa il testo `'5000'`, che si può mettere nell'etichetta. `135 div 60` = `2` e `135 mod 60` = `15`.

### I 3 errori più comuni

| Che cosa vedi | Che cosa vuol dire | Soluzione |
|---|---|---|
| `Identifier not found "Edit1"` | Manca il componente, oppure il nome nel codice è diverso da `Name` nell'Ispettore. | Controlla che sulla Form ci siano `Edit1`, `Label1`, `Button1`. Scrivi il nome identico (maiuscole comprese). |
| `Incompatible types` | Hai messo un testo dove serve un numero, o un numero dove serve un testo. | Per il conto: `StrToInt(...)`. Per scrivere nell'etichetta: `IntToStr(...)`. |
| Il programma si chiude o compare una finestra con `"5a" is an invalid integer` | Nella casella il numero non è scritto bene: lettere, spazi, virgola, oppure è vuota. | Scrivi solo cifre intere (`5`, non `5,5` né `5 km`). Poi premi di nuovo il bottone. |

> **Fallo tuo:** cambia la scritta del bottone, il titolo della finestra (`Caption` della Form) e il colore (`Color`). Aggiungi UN bottone con una conversione che piace a te (per esempio metri in centimetri: `* 100`).

## 04 Programma 2: la calcolatrice a 4 bottoni

**A che cosa serve.** Scrivi due numeri e premi `+`, `-`, `*` oppure `/`: il programma scrive la frase con il risultato. **Quando funziona** vedi questo:

*Schema disegnato: la calcolatrice finita.* (schema nel PDF)

*Schema con i numeri: i numeri rossi sono quelli della tabella.* (schema nel PDF)

| N. | Name | Tipo | Che cosa cambi |
|---|---|---|---|
| 1 | `Edit1` | TEdit | `Text` vuoto |
| 2 | `Edit2` | TEdit | `Text` vuoto |
| 3 | `Button1` | TButton | `Caption` = `+` |
| 4 | `Button2` | TButton | `Caption` = `-` |
| 5 | `Button3` | TButton | `Caption` = `*` |
| 6 | `Button4` | TButton | `Caption` = `/` |
| 7 | `Label1` | TLabel | niente (la riempie il codice) |

### La ricetta, un'azione per riga

1. [A] Menu `Progetto`, `Nuovo progetto…`, `Applicazione`, `OK`.
2. [B] `Progetto`, `Salva progetto con nome…`: cartella `calcolatrice` in `Documenti`, nome file `calcolatrice`, `Salva` due volte.
3. [C] Palette `Standard`: clic su `TEdit`, clic sulla Form. Poi un secondo `TEdit` sotto il primo.
4. [C] Clic su `TButton`, clic sulla Form. Ripetilo quattro volte, in fila.
5. [C] Clic su `TLabel`, clic sulla Form sotto i bottoni.
6. [D] Clicca ogni bottone e metti `Caption`: `+`, poi `-`, poi `*`, poi `/`.
7. [D] Clicca `Edit1` e svuota `Text`. Fai lo stesso con `Edit2`.
8. [E] Doppio clic sul bottone `+` (`Button1`). Completa il gestore così:

```
procedure TForm1.Button1Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' più ' + IntToStr(b) + ' fa ' + IntToStr(a + b);
end;
```

9. [F] Premi `F9`, scrivi `7` e `5`, premi `+`.

> **Vinci subito (5 minuti):** deve comparire la frase **7 più 5 fa 12**.

**Gli altri tre bottoni:** doppio clic su `-`, poi su `*`, poi su `/` e ricopia. Cambia solo l'operazione e la parola. Prova `7` e `5`: **7 meno 5 fa 2**, **7 per 5 fa 35**.

```
procedure TForm1.Button2Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' meno ' + IntToStr(b) + ' fa ' + IntToStr(a - b);
end;
```

```
procedure TForm1.Button3Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' per ' + IntToStr(b) + ' fa ' + IntToStr(a * b);
end;
```

Il bottone `/` controlla lo zero con `if`: non si può dividere per zero. Prova `8` e `0`: **Non si può dividere per zero**. Con `8` e `2`: **8 diviso 2 fa 4**.

```
procedure TForm1.Button4Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  if b = 0 then
    Label1.Caption := 'Non si può dividere per zero'
  else
    Label1.Caption := IntToStr(a) + ' diviso ' + IntToStr(b) + ' fa ' + IntToStr(a div b);
end;
```

### Che cosa fanno le istruzioni nuove

`StrToIntDef(Edit1.Text, 0)` legge il numero e, se la casella è vuota o ci sono lettere, usa `0` invece di bloccarsi: `'7'` fa `7`, `'ab'` fa `0`. `if b = 0 then … else …` vuol dire: **se** b è zero fai la prima cosa, **altrimenti** la seconda. `8 div 2` fa `4`.

### I 3 errori più comuni

| Che cosa vedi | Che cosa vuol dire | Soluzione |
|---|---|---|
| `Identifier not found "Edit2"` | Manca il secondo `Edit`, oppure il nome è diverso. | Metti un secondo `TEdit` sulla Form e controlla che si chiami `Edit2`. |
| `Incompatible types` | Testo contro numero: hai scritto `Label1.Caption := a + b`. | Per scrivere nell'etichetta serve il testo: `IntToStr(a + b)`. |
| Il programma si chiude con `Division by zero` | Hai diviso per zero e manca il controllo `if b = 0`. | Ricopia il codice del bottone `/` con l'`if`. Prova `8` e `0`. |

> **Fallo tuo:** cambia il titolo della finestra, i colori e le frasi (per esempio al posto di `più` scrivi `sommato a`).

## 05 Programma 3: il cassiere

**A che cosa serve.** Scrivi il nome del cliente, il prezzo e i soldi dati: il programma calcola il resto, dice quante banconote e monete servono e scrive lo scontrino con il nome. **Quando funziona** vedi questo:

*Schema disegnato: lo scontrino finito.* (schema nel PDF)

*Schema con i numeri: i numeri rossi sono quelli della tabella.* (schema nel PDF)

| N. | Name | Tipo | A che cosa serve |
|---|---|---|---|
| 1 | `Edit1` | TEdit | nome del cliente (`Text` vuoto) |
| 2 | `Edit2` | TEdit | prezzo (`Text` vuoto) |
| 3 | `Edit3` | TEdit | soldi dati (`Text` vuoto) |
| 4 | `Button1` | TButton | `Caption` = `Calcola il resto` |
| 5 | `Label1` | TLabel | scrive il resto |
| 6 | `Memo1` | TMemo | lo scontrino (righe vuote) |

### La ricetta, un'azione per riga

1. [A] Menu `Progetto`, `Nuovo progetto…`, `Applicazione`, `OK`.
2. [B] `Progetto`, `Salva progetto con nome…`: cartella `cassiere` in `Documenti`, nome file `cassiere`, `Salva` due volte.
3. [C] Palette `Standard`: tre volte `TEdit` (clic sul pezzo, clic sulla Form), uno sotto l'altro.
4. [C] Un `TButton` sotto le caselle, poi un `TLabel` accanto al bottone.
5. [C] Un `TMemo` grande in fondo alla Form.
6. [D] Clicca `Button1` e scrivi `Caption`: `Calcola il resto`.
7. [D] Svuota `Text` di `Edit1`, `Edit2`, `Edit3`.
8. [D] Clicca `Memo1`: nell'Ispettore, a destra di `Lines`, clic sui tre puntini, cancella il testo e `OK`.
9. [E] Doppio clic sul bottone. Per **vincere subito** scrivi solo il resto (soldi dati meno prezzo):

```
procedure TForm1.Button1Click(Sender: TObject);
var
  prezzo, dati, resto: Integer;
begin
  prezzo := StrToIntDef(Edit2.Text, 0);
  dati := StrToIntDef(Edit3.Text, 0);
  resto := dati - prezzo;
  Label1.Caption := 'Resto: ' + IntToStr(resto) + ' euro';
end;
```

10. [F] Premi `F9`, scrivi prezzo `13` e soldi dati `50`, premi il bottone.

> **Vinci subito (5 minuti):** deve comparire **Resto: 37 euro**.

11. Ferma il programma (la `X` rossa). Cancella tutto il codice tra `begin` e `end;` e usa il codice completo qui sotto: aggiunge banconote, monete e scontrino.

```
procedure TForm1.Button1Click(Sender: TObject);
var
  prezzo, dati, resto, b10, b5, m2, m1: Integer;
begin
  prezzo := StrToIntDef(Edit2.Text, 0);
  dati := StrToIntDef(Edit3.Text, 0);
  resto := dati - prezzo;
  b10 := resto div 10;
  resto := resto mod 10;
  b5 := resto div 5;
  resto := resto mod 5;
  m2 := resto div 2;
  m1 := resto mod 2;
  Memo1.Clear;
  Memo1.Lines.Add('SCONTRINO');
  Memo1.Lines.Add('Cliente: ' + Edit1.Text);
  Memo1.Lines.Add('Prezzo: ' + IntToStr(prezzo) + ' euro');
  Memo1.Lines.Add('Dati: ' + IntToStr(dati) + ' euro');
  Memo1.Lines.Add('Resto: ' + IntToStr(dati - prezzo) + ' euro');
  Memo1.Lines.Add(IntToStr(b10) + ' banconote da 10, ' + IntToStr(b5) + ' da 5');
  Memo1.Lines.Add(IntToStr(m2) + ' monete da 2, ' + IntToStr(m1) + ' da 1');
end;
```

12. [F] Premi `F9`, scrivi `Maria`, `13`, `50` e premi il bottone.

> **Risultato atteso:** nel Memo compare lo scontrino: `SCONTRINO`, `Cliente: Maria`, `Prezzo: 13 euro`, `Dati: 50 euro`, `Resto: 37 euro`, `3 banconote da 10, 1 da 5`, `1 monete da 2, 0 da 1`.

### Che cosa fanno le istruzioni nuove

Resto `37`: `37 div 10` = `3` banconote da 10, `37 mod 10` = `7` avanza. `7 div 5` = `1` banconota da 5, avanza `2`. `2 div 2` = `1` moneta da 2, avanza `0`. `'Cliente: ' + Edit1.Text` unisce due testi. `Memo1.Lines.Add(...)` aggiunge una riga allo scontrino, `Memo1.Clear` lo svuota prima di scrivere.

### I 3 errori più comuni

| Che cosa vedi | Che cosa vuol dire | Soluzione |
|---|---|---|
| `Identifier not found "Memo1"` | Manca il `TMemo`, oppure si chiama in un altro modo. | Metti il `TMemo` sulla Form e controlla che il `Name` sia `Memo1`. Lo stesso vale per `Edit1`, `Edit2`, `Edit3`. |
| `Incompatible types` | Testo contro numero: hai scritto `Memo1.Lines.Add(resto)` senza convertire. | Scrivi `IntToStr(resto)` dentro `Add(...)`. |
| Il resto o le banconote sono strani (numeri negativi, o `0`) | I soldi dati sono meno del prezzo, oppure hai scritto i centesimi con la virgola (`13,50` conta come `0`). | Scrivi euro interi (`13`). I soldi dati devono essere almeno uguali al prezzo. |

> **Fallo tuo:** dai un nome al tuo negozio e scrivilo in cima allo scontrino: dopo `Memo1.Clear;` aggiungi `Memo1.Lines.Add('NEGOZIO DI ...');` con il nome che vuoi tu.

## 06 Riassunto dei tre programmi

| Programma | Componenti | Cosa c'è di nuovo | Prova | Deve uscire |
|---|---|---|---|---|
| 1. Convertitore | `Edit1`, `Label1`, 5 `Button` | `StrToInt`, `IntToStr`, `div`, `mod` | `5` | `5000 metri` |
| 2. Calcolatrice | `Edit1`, `Edit2`, 4 `Button`, `Label1` | `StrToIntDef`, `if … else` | `7` e `5` / `8` e `0` | `7 più 5 fa 12` / `Non si può dividere per zero` |
| 3. Cassiere | `Edit1`, `Edit2`, `Edit3`, `Label1`, `Button1`, `Memo1` | `div`, `mod`, `+` sui testi, `Memo1.Lines.Add` | `Maria`, `13`, `50` | `Resto: 37 euro` |

### Ricopia sul quaderno

```
String = testo  '53'
Integer = numero  53
StrToInt = da testo a numero
IntToStr = da numero a testo
StrToIntDef(testo, 0) = se non va, usa 0
div = divisione senza virgola   17 div 5 = 3
mod = quello che avanza    17 mod 5 = 2
resto = dati - prezzo
```

Poi racconta a voce a un compagno, con parole tue, che cosa fa il tuo programma preferito.

Hai fatto tre programmi veri. Mostrali a un compagno: il tuo nome è sul tuo lavoro.
