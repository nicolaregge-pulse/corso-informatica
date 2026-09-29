# Convertitore Km/h ↔ mph in Lazarus — scheda per te (e per la tua AI)

**Classe 2 · Informatica · Versione 1.2**

*Questo file è **per te**: puoi leggerlo e puoi **darlo a Gemini** (o a un'altra AI) per
farti spiegare le parti che non capisci, o farti tradurre nella tua lingua. Regola
d'oro: l'AI serve per **capire meglio**, non per saltare il pensiero. Alla fine devi
saper **spiegare a voce** cosa fa il tuo programma.*

---

## 1. Cosa costruiamo
Un'app che converte una velocità tra **km/h** e **mph** (miglia all'ora). Scrivi un
numero, scegli la direzione con dei pallini, premi **Converti** e leggi il risultato
con **una cifra decimale**.

## 2. UI — l'interfaccia (cosa si vede)
1. **Edit1** con etichetta **Km/h** e **Edit2** con etichetta **mph** (le due caselle).
2. **RadioGroup1** (pallini della direzione). Per inserire le due voci: nell'Object Inspector trova la
   proprietà **Items**, clicca il pulsante `…` a destra e nell'editor scrivi **una voce per riga**:
   `Da Km/h` e `Da mph`, poi OK. Infine metti `ItemIndex = 0`.
3. **Button1** con `Caption = Converti`.

## 3. UX — come si usa (con mouse E con sola tastiera)
L'app gira su **Windows** e si deve poter usare in due modi: col **mouse** e anche
**solo con la tastiera**. Si regola con le proprietà dei controlli:
1. **TabStop** (True/False): se True il controllo si raggiunge con `Tab`; se False viene saltato.
2. **TabOrder**: l'ordine con cui `Tab` passa da un controllo all'altro (0, 1, 2…). Ordine logico: Edit1 → RadioGroup → Edit2 → Button.
3. **Button1.Default = True**: premendo `Invio` parte la conversione senza cliccare.

## 4. LOGICA — il calcolo
1. **1 mph ≈ 1,6 km/h** (in classe usiamo 1,6; il valore preciso è 1,60934).
2. Da **Km/h** a mph: si **divide** per 1,6. Da **mph** a Km/h: si **moltiplica** per 1,6.

Il codice del bottone:

```pascal
procedure TForm1.Button1Click(Sender: TObject);
var
  a: Real;
begin
  if RadioGroup1.ItemIndex = 0 then      // Da Km/h a mph
  begin
    a := StrToFloat(Edit1.Text);         // Edit1 = Km/h
    Edit2.Text := FormatFloat('0.0', a / 1.6);
  end
  else                                    // Da mph a Km/h
  begin
    a := StrToFloat(Edit2.Text);         // Edit2 = mph
    Edit1.Text := FormatFloat('0.0', a * 1.6);
  end;
end;
```

1. `StrToFloat(...)` trasforma il **testo** della casella in un **numero** con la virgola.
2. `FormatFloat('0.0', ...)` trasforma il numero in **testo con 1 cifra decimale**.

## 5. Come chiedere aiuto a Gemini (esempi di domande)
Copia questo file dentro Gemini e prova a chiedere, con parole tue:
1. «Spiegami con parole semplici cosa fa `StrToFloat` in questo codice.»
2. «Perché serve `FormatFloat('0.0', ...)`? Cosa cambia se scrivo `'0.00'`?»
3. «Cos'è `ItemIndex` del RadioGroup e perché il primo pallino è 0?»
4. «Traducimi questa scheda in [la tua lingua], così la capisco meglio.»
5. «Fammi 3 domande per controllare se ho capito il convertitore.»

> Ricorda: dopo che l'AI ti ha spiegato, **prova a rifarlo tu** e a spiegarlo a voce a un
> compagno. Se lo sai spiegare, l'hai capito davvero.
