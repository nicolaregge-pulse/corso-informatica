<!-- generato da dispensa-if-annidati.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Le decisioni: if / then / else  
e gli if uno dentro l'altro

Classe 2 · Informatica · Lazarus · 05/10/2026 · e alla fine il gioco **Indovina il numero**

**Cosa impari oggi:** a far **decidere** il programma (**if** = se, **then** = allora, **else** = altrimenti) e a mettere un if **dentro** un altro if (si dice **if annidati** : come una scatola dentro una scatola). Alla fine costruisci un **gioco vero** : il computer pensa un numero e tu lo devi indovinare.

## 1\. Ripasso: if / then / else

Si legge come in italiano: **SE** la condizione è vera **ALLORA** fai questo, **ALTRIMENTI** fai quest'altro.

numero pari?

SÌ -> scrivi PARI

NO -> scrivi DISPARI
    
    
    numero := StrToInt(Edit1.Text);
    if numero mod 2 = 0 then
      begin
        Label1.Caption := 'PARI';
      end
    else
      begin
        Label1.Caption := 'DISPARI';
      end;

`mod` = il **resto** della divisione: se diviso 2 il resto è 0, il numero è pari. I confronti: `=` uguale · `<>` diverso · `<` minore · `>` maggiore · `<=` · `>=`.

## 2\. La regola dei rientri (si fa sempre così)

Regola| Perché  
---|---  
**if** ed **else** sullo **stesso rientro** (stessa colonna)| si vede subito quale else appartiene a quale if  
**begin** ed **end** sullo **stesso rientro** , con lo stesso numero e colore| ogni begin ha il suo end, come una parentesi che si apre e si chiude  
tutto quello che sta **dentro** va **un gradino più a destra** (2 spazi)| si vede a colpo d'occhio chi sta dentro a chi  
dopo **then** e dopo **else** mettiamo **sempre** begin ... end, anche per una riga sola| il codice resta sempre ordinato e puoi aggiungere righe senza errori  
  
**L'errore che fanno tutti (anche i professionisti):** il **;** prima di **else**. L'**end** che sta subito prima di **else** va **senza** punto e virgola. Il **;** si mette solo all'**end** finale dell'if.

**Trucco per non perdere le coppie:** appena scrivi **begin** , scrivi subito sotto il suo **end** allo stesso rientro. Poi riempi in mezzo.

## 3\. Un if dentro un altro if (if annidati)

Con un solo if hai **2 strade**. Se dentro l'else metti un altro if, le strade diventano **3**. Esempio: positivo, negativo o zero?

numero > 0 ?

SÌ -> **POSITIVO**

NO ->

numero < 0 ?

SÌ -> **NEGATIVO**

NO -> **ZERO**
    
    
    numero := StrToInt(Edit1.Text);
    if numero > 0 then
      begin
        Label1.Caption := 'POSITIVO';
      end
    else
      begin
        if numero < 0 then
          begin
            Label1.Caption := 'NEGATIVO';
          end
        else
          begin
            Label1.Caption := 'ZERO';
          end;
      end;

**Carta e penna:** ricopia questo codice sul quaderno e traccia una **graffa** da ogni begin al suo end (stesso numero). Poi disegna lo schema a frecce: due domande, tre risposte.

## 4\. Riscaldamento (Form: Edit1, Button1, Label1)

Stessa Form per tutti e tre: una casella **Edit1** , un bottone **Button1** (Caption: **Controlla**), una scritta **Label1**. Doppio clic sul bottone e scrivi il codice tra begin ed end. Ricordati `var numero: Integer;` sopra il begin.

N.| Esercizio| Quante strade  
---|---|---  
R1| **Pari o dispari** : copia l'esempio del punto 1 e provalo con 4, 7, 0.| 2 (un if)  
R2| **Positivo, negativo o zero** : copia l'esempio del punto 3 e provalo con 5, -3, 0.| 3 (if annidati)  
R3| **Il voto** (fallo tu!): se il voto è minore di 6 scrivi **Insufficiente** ; altrimenti, se è minore di 8 scrivi **Sufficiente** ; altrimenti **Ottimo!**. Prova con 4, 6, 7, 9.| 3 (if annidati)  
R4| **Maggiorenne?** (fallo tu!): età minore di 14 -> **Bambino** ; minore di 18 -> **Ragazzo** ; altrimenti **Maggiorenne**.| 3 (if annidati)  
  
**Aiuto per R3:** è identico a R2: cambia solo le condizioni (`voto < 6`, `voto < 8`) e le scritte.

## 5\. Il gioco: Indovina il numero

Indovina il numero

Ho pensato un numero da 1 a 100. Quale?  
  
50   Prova   Nuova partita  
  
**Troppo ALTO: prova un numero più piccolo**

Ecco come sarà il tuo gioco (titolo e colori li scegli tu)

Livello 1 — Cosa deve fare

All'avvio il computer pensa un numero **segreto** da 1 a 100. Tu scrivi un numero e premi **Prova**. Il programma risponde: **Troppo BASSO** , **Troppo ALTO** oppure **BRAVO! Indovinato** (con il numero di tentativi). Il bottone **Nuova partita** pensa un altro numero.

Livello 2 — Un aiuto

Ti servono 2 variabili che **durano per tutta la partita** (segreto e tentativi): vanno in alto, sotto `Form1: TForm1;`. Il numero segreto si crea con `Random(100) + 1`, all'avvio (evento **OnCreate** della Form: doppio clic su un punto vuoto della Form). Nel bottone Prova usa un **if annidato** : prima chiedi "è uguale?", nell'else chiedi "è più piccolo?".

Livello 3 — I pezzi sulla Form

Pezzo| Name| Proprietà  
---|---|---  
Form| Form1| Caption = Indovina il numero  
Label| Label1| Caption = Ho pensato un numero da 1 a 100. Quale?  
Edit| EditNumero| Text = (vuoto)  
Button| ButtonProva| Caption = Prova  
Button| ButtonNuova| Caption = Nuova partita  
Label| LabelRisposta| Caption = (vuoto) · Font: grande e colorato, a tuo gusto  
  
Livello 4 — Il codice completo

**A) In alto nel codice** , sotto `Form1: TForm1;`, aggiungi le due variabili:
    
    
    var
      Form1: TForm1;
      segreto: Integer;     // il numero pensato dal computer
      tentativi: Integer;   // quante prove hai fatto

**B) Doppio clic su un punto vuoto della Form** -> nasce **FormCreate** :
    
    
    procedure TForm1.FormCreate(Sender: TObject);
    begin
      Randomize;                     // mescola i numeri a caso
      segreto := Random(100) + 1;    // un numero da 1 a 100
      tentativi := 0;
    end;

**C) Doppio clic su Prova** -> il cuore del gioco, con l'**if annidato** :
    
    
    procedure TForm1.ButtonProvaClick(Sender: TObject);
    var
      numero: Integer;
    begin
      numero := StrToInt(EditNumero.Text);
      tentativi := tentativi + 1;
      if numero = segreto then
        begin
          LabelRisposta.Caption := 'Indovinato! Tentativi: ' + IntToStr(tentativi);
        end
      else
        begin
          if numero < segreto then
            begin
              LabelRisposta.Caption := 'Troppo BASSO: prova un numero più grande';
            end
          else
            begin
              LabelRisposta.Caption := 'Troppo ALTO: prova un numero più piccolo';
            end;
        end;
      EditNumero.Clear;
    end;

**D) Doppio clic su Nuova partita** :
    
    
    procedure TForm1.ButtonNuovaClick(Sender: TObject);
    begin
      segreto := Random(100) + 1;
      tentativi := 0;
      LabelRisposta.Caption := 'Ho pensato un nuovo numero da 1 a 100';
    end;

**Se Lazarus dà errore su else:** guarda l'end subito prima: non deve avere il **;**. **Se dà errore appena premi Prova con la casella vuota:** è normale, StrToInt vuole un numero (vedi sfida 3).

**Fallo tuo:** cambia il titolo della finestra, i colori, le frasi (anche spiritose) e il nome del gioco. Poi fallo provare a un compagno: chi indovina con meno tentativi?

## 6\. Sfide per chi ha finito (sempre con gli if)

  1. **Ci sei quasi!** Dentro "troppo alto" e "troppo basso" aggiungi un altro if: se la differenza è al massimo 5, scrivi **Ci sei quasi!** (aiuto: `if Abs(numero - segreto) <= 5 then`).
  2. **Massimo 7 tentativi:** se tentativi arriva a 7 e non hai indovinato, scrivi **Hai perso! Il numero era** ... (aiuto: `IntToStr(segreto)`).
  3. **Fuori campo:** se il numero è minore di 1 o maggiore di 100 scrivi **Solo numeri da 1 a 100!** e non contare il tentativo (aiuto: `if (numero < 1) or (numero > 100) then`).
  4. **Livelli:** aggiungi tre bottoni **Facile** (1-10), **Medio** (1-100), **Difficile** (1-1000).

Classe 2 · Dispensa if / then / else e if annidati · v1.0 · Non si consegna: si consegna il foglio del COMPITO.
