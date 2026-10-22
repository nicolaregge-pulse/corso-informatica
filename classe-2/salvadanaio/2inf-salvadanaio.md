# Il mio salvadanaio: FOR e WHILE insieme

**Versione 1.0** — 22/10/2026 · 2INF · 22/10/2026 · Lazarus · un programma tuo con il FOR e il WHILE (circa 2 ore)

La pagina della lezione, con il ripasso: https://nicolaregge-pulse.github.io/corso-informatica/verifica/?b=2inf-salvadanaio

## 01 Il mio salvadanaio: che cosa facciamo oggi

Oggi fai un programma **tuo**: un salvadanaio.
Tu scegli **che cosa vuoi comprare** (delle scarpe, una cuffia, un gioco) e **quanto costa**.
Ogni giorno metti nel salvadanaio da **1 a 5 euro**, a caso.
Il programma ha **tre bottoni**:
1) **Una settimana**: quanto risparmi in 7 giorni. Qui usi il **FOR**.
2) **Quanti giorni mi servono?**: quanti giorni servono per arrivare al prezzo. Qui usi il **WHILE**.
3) **Con la paghetta** (sfida): il sabato arrivano 10 euro in più.
Un pezzo alla volta. Ogni pezzo finisce con un **FATTO!** verde.

## 02 FOR o WHILE? Ripasso lampo

**FOR** = so **prima** quante volte. Una settimana ha sempre 7 giorni:
```
for giorno := 1 to 7 do
```
**WHILE** = **non so** quante volte. Ripeto **finché** la condizione è vera:
```
while totale < prezzo do
```
Si legge: **finché** il totale è **minore** del prezzo, metto altri soldi.
Nel FOR il contatore aumenta **da solo**. Nel WHILE lo fai aumentare **tu**: `giorni := giorni + 1`.
Nel WHILE qualcosa deve cambiare la condizione, se no il ciclo **non finisce mai** (ciclo infinito: **Esegui → Ferma**, oppure **Ctrl+F2**).

## 03 PEZZO 1: la Form (circa 15 minuti)

1) Apri Lazarus: **Progetto → Nuovo progetto → Applicazione → Ok**.
2) Metti un **TLabel**. Caption: **Che cosa vuoi comprare?**
3) Accanto metti un **TEdit** (si chiama **Edit1**). Nella proprietà **Text** scrivi la cosa che vuoi tu, per esempio **scarpe**.
4) Sotto metti un altro **TLabel**. Caption: **Quanto costa (euro)?**
5) Accanto metti un **TEdit** (**Edit2**). Text: il prezzo, per esempio **80**. Solo il numero, senza €.
6) Metti tre **TButton**, uno sotto l'altro. Caption: **Una settimana** (Button1), **Quanti giorni mi servono?** (Button2), **Con la paghetta** (Button3).
7) Metti un **TMemo** grande (Memo1). **ScrollBars = ssVertical**. Cancella le righe di **Lines**.
8) **Fallo tuo**: Caption del form = **Il salvadanaio di** e il tuo nome. Cambia il colore (Color) del form.
9) Premi **F9**: si apre la tua finestra.

FATTO! La finestra si apre e vedi le due caselle, i tre bottoni e il Memo.

## 04 PEZZO 2: il bottone «Una settimana», con il FOR (circa 20 minuti)

1) Chiudi la finestra. Fai **doppio clic** sul bottone **Una settimana**.
2) Lazarus scrive la procedura. Completala così: le righe con `// QUI` dicono che cosa scrivere al loro posto.
```
procedure TForm1.Button1Click(Sender: TObject);
var giorno, euro, totale: integer;
begin
  Randomize;
  Memo1.Clear;
  totale := 0;
  // QUI il ciclo FOR: giorno da 1 a 7
  //   QUI euro a caso da 1 a 5
  //   QUI aggiungi euro al totale
  //   QUI scrivi nel Memo: Giorno 1: +3 euro
  // QUI, dopo il ciclo, scrivi il totale della settimana
end;
```
**Indizi**, se ti servono:
Il ciclo: `for giorno := 1 to 7 do` poi `begin` … `end;`
Il soldo del giorno: `euro := Random(5) + 1;` (da 1 a 5)
Nel salvadanaio: `totale := totale + euro;`
La riga nel Memo: `Memo1.Lines.Add('Giorno ' + IntToStr(giorno) + ': +' + IntToStr(euro) + ' euro');`
Il totale, **dopo** l'`end;` del ciclo: `Memo1.Lines.Add('In una settimana: ' + IntToStr(totale) + ' euro');`
3) Premi **F9** e poi il bottone **Una settimana**, più volte.

FATTO! Nel Memo vedi 7 righe, da Giorno 1 a Giorno 7, e sotto il totale. Ogni volta i numeri cambiano.

## 05 PEZZO 3: il bottone «Quanti giorni mi servono?», con il WHILE (circa 25 minuti)

1) Doppio clic sul bottone **Quanti giorni mi servono?** e completa:
```
procedure TForm1.Button2Click(Sender: TObject);
var giorni, euro, totale, prezzo: integer;
begin
  Randomize;
  prezzo := StrToInt(Edit2.Text);
  Memo1.Clear;
  totale := 0;
  giorni := 0;
  // QUI il ciclo WHILE: finché il totale è minore del prezzo
  //   QUI euro a caso da 1 a 5
  //   QUI aggiungi euro al totale
  //   QUI conta un giorno in più
  // QUI, dopo il ciclo, scrivi quanti giorni servono
end;
```
**Indizi**:
Il ciclo: `while totale < prezzo do` poi `begin` … `end;`
Dentro: `euro := Random(5) + 1;` poi `totale := totale + euro;` poi `giorni := giorni + 1;`
Se vuoi vedere i giorni nel Memo: `Memo1.Lines.Add('Giorno ' + IntToStr(giorni) + ': ho ' + IntToStr(totale) + ' euro');`
Dopo il ciclo: `Memo1.Lines.Add('Per ' + Edit1.Text + ' ti servono ' + IntToStr(giorni) + ' giorni');`
**Perché si ferma?** Ogni giro il totale cresce. Quando arriva al prezzo (o lo supera), `totale < prezzo` diventa **falso** e il ciclo finisce. Questa è la **condizione di uscita**.
2) F9, scrivi 80 nella casella del prezzo, premi il bottone.

FATTO! Il Memo dice: Per scarpe ti servono … giorni (con la tua cosa e il tuo prezzo).

## 06 PEZZO 4: quante settimane? (circa 10 minuti)

In Pascal ci sono due operazioni per le divisioni **senza virgola**:
**div** = quante volte ci sta. `23 div 7` = **3** (3 settimane intere).
**mod** = quanto avanza. `23 mod 7` = **2** (avanzano 2 giorni).
Aggiungi alla fine del bottone **Quanti giorni mi servono?**, dopo l'altra riga:
```
Memo1.Lines.Add('Cioè ' + IntToStr(giorni div 7) + ' settimane e ' + IntToStr(giorni mod 7) + ' giorni');
```
Prova con un prezzo grande, per esempio **150**.

FATTO! Il Memo dice anche: Cioè … settimane e … giorni.

## 07 SFIDA: il bottone «Con la paghetta» (circa 20 minuti)

Il **sabato** arriva la paghetta: **10 euro in più**. Facciamo finta che il giorno 7, il 14, il 21… siano i sabati.
Come si riconosce? Il giorno è un sabato quando `giorni mod 7 = 0` (7, 14, 21 divisi per 7 non hanno resto).
1) Doppio clic sul bottone **Con la paghetta**.
2) Copia dentro tutto il codice del bottone «Quanti giorni mi servono?» (le var e le righe tra begin ed end).
3) Dentro il while, **dopo** `giorni := giorni + 1;`, aggiungi:
```
if giorni mod 7 = 0 then
begin
  totale := totale + 10;
  Memo1.Lines.Add('Sabato: paghetta +10 euro!');
end;
```
4) F9 e premi i due bottoni con lo stesso prezzo. Con la paghetta servono **meno giorni**?

FATTO! Nel Memo compare «Sabato: paghetta +10 euro!» e i giorni sono meno di prima.

## 08 Errori tipici e la consegna

**Errori tipici** (succede a tutti, anche ai pro):
1) **Identifier not found**: manca la variabile nella riga `var`.
2) Il totale è sempre 0 o sbagliato: manca `totale := 0;` prima del ciclo, o `totale := totale + euro;` dentro.
3) Dice sempre 0 giorni: manca `giorni := giorni + 1;`.
4) Il programma si blocca: ciclo infinito. Il totale non cresce dentro il while. **Esegui → Ferma** e controlla.
5) Errore quando premi il bottone: la casella del prezzo è vuota o ha lettere (o il simbolo €). Scrivi solo il numero.
6) Il totale della settimana compare 7 volte: la riga del totale è **dentro** il ciclo. Spostala dopo l'`end;`.
**La consegna**: nella verifica c'è una domanda dove incolli **tutto il tuo codice**. In Lazarus, nella finestra del codice, seleziona dalla prima `procedure TForm1.Button1Click` fino all'ultimo `end;` dei bottoni e premi **Ctrl+C**. Poi nella domanda premi **Ctrl+V**. Poi scrivi con parole tue che cosa fa.

FATTO! Hai il codice copiato e sai dire a voce che cosa fa ogni bottone.
