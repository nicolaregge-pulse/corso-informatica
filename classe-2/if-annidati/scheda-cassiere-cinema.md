<!-- generato da scheda-cassiere-cinema.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Il cassiere del cinema

Classe 2 · Informatica · Lazarus · 08/10/2026 · if annidati su 3 livelli · esercitazione valutata

**La missione:** il cinema ti assume come programmatore. Devi fare l'app della cassa: il cliente scrive l'**età** , spunta se oggi è **mercoledì** , preme **Prezzo** e l'app dice quanto paga. È un vero programma da lavoro, fatto tutto con gli **if**.

## 1\. Le regole del cinema

Chi| Quanto paga  
---|---  
meno di 6 anni| **Gratis!**  
da 6 a 13 anni, oppure 65 anni e più| **Ridotto: 5 euro**  
tutti gli altri, di mercoledì| **Mercoledì: 6 euro**  
tutti gli altri| **Intero: 8 euro**  
  
età < 6 ?

SÌ -> **Gratis**

NO ->

età < 14 _oppure_ età ≥ 65 ?

SÌ -> **5 euro**

NO ->

mercoledì ?

SÌ -> **6 euro**

NO -> **8 euro**

**Carta e penna, PRIMA del computer:** ricopia lo schema a frecce: 3 domande, 4 risposte. Ogni domanda è un **if** ; ogni NO porta al prossimo if, dentro l'**else**.

## 2\. Parola nuova: or (oppure)

`(eta < 14) or (eta >= 65)` è vero se **almeno una** delle due condizioni è vera. Le condizioni vanno **tra parentesi**. Componente nuovo: la **CheckBox** (casella da spuntare): `CheckBoxMercoledi.Checked` è vero se è spuntata.

Cinema Stella — Cassa

Quanti anni hai? 15  
  
☑ Oggi è mercoledì   Prezzo  
  
**Mercoledì: 6 euro**

La tua app (il nome del cinema lo scegli tu)

## 3\. Costruisci l'app

Livello 1 — Cosa deve fare

Una casella per l'età, una casella da spuntare per il mercoledì, un bottone **Prezzo** , una scritta che mostra il prezzo secondo le regole del punto 1.

Livello 2 — Un aiuto

Tre if uno dentro l'altro, nell'ordine dello schema: prima "età < 6", nell'else "età < 14 or età ≥ 65", nell'else "mercoledì?". Scrivi **prima tutte le coppie begin/end** , poi riempi.

Livello 3 — I pezzi sulla Form

Pezzo| Name| Proprietà  
---|---|---  
Form| Form1| Caption = il nome del TUO cinema  
Label| Label1| Caption = Quanti anni hai?  
Edit| EditEta| Text = (vuoto)  
CheckBox| CheckBoxMercoledi| Caption = Oggi è mercoledì (gruppo Standard, icona con la spunta)  
Button| ButtonPrezzo| Caption = Prezzo  
Label| LabelPrezzo| Caption = (vuoto) · Font grande e colorato  
  
Livello 4 — Il codice completo

Doppio clic su **Prezzo** e scrivi:
    
    
    procedure TForm1.ButtonPrezzoClick(Sender: TObject);
    var
      eta: Integer;
    begin
      eta := StrToInt(EditEta.Text);
      if eta < 6 then
        begin
          LabelPrezzo.Caption := 'Gratis!';
        end
      else
        begin
          if (eta < 14) or (eta >= 65) then
            begin
              LabelPrezzo.Caption := 'Ridotto: 5 euro';
            end
          else
            begin
              if CheckBoxMercoledi.Checked then
                begin
                  LabelPrezzo.Caption := 'Mercoledì: 6 euro';
                end
              else
                begin
                  LabelPrezzo.Caption := 'Intero: 8 euro';
                end;
            end;
        end;
    end;

## 4\. Collaudo: la tabella di prova

I programmatori veri **provano** ogni strada prima di consegnare. Prova questi casi e scrivi cosa esce:

Età| Mercoledì?| Deve uscire| È uscito (scrivi tu)  
---|---|---|---  
4| no| Gratis!|   
10| sì| Ridotto: 5 euro|   
70| no| Ridotto: 5 euro|   
16| sì| Mercoledì: 6 euro|   
30| no| Intero: 8 euro|   
14| no| Intero: 8 euro|   
  
**Fallo tuo:** nome del cinema, colori, il titolo del film di oggi in una Label. Puoi cambiare i prezzi: ma allora cambia anche la tabella di prova.

## 5\. Sfide per chi ha finito

  1. **Popcorn:** aggiungi la CheckBox **Popcorn (+3 euro)**. Aiuto: usa una variabile `prezzo: Integer`, calcola il prezzo con gli if, poi `if CheckBoxPopcorn.Checked then prezzo := prezzo + 3;` e alla fine scrivi `IntToStr(prezzo) + ' euro'`.
  2. **Età impossibile:** se l'età è minore di 0 o maggiore di 120 scrivi **Età non valida** (un if in più, prima di tutti gli altri).
  3. **Biglietti per la famiglia:** una casella **Quanti biglietti?** e il totale da pagare.

Classe 2 · Il cassiere del cinema · v1.0
