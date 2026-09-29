# Compito Lazarus — Convertitore metri ↔ piedi

**Classe 2 · Informatica · Versione 1.0 · da svolgere da soli**

Costruisci un'app in Lazarus **uguale nella struttura** a quella Km/h↔mph vista a lezione,
ma che converte le **lunghezze** (metri ↔ piedi). Cambia solo il numero: il metodo è lo stesso.

## 1. Componenti (UI)
1. **Edit1** (metri) e **Edit2** (piedi).
2. **RadioGroup1** (Items, una voce per riga): `Da metri` e `Da piedi`; `ItemIndex = 0`.
3. **Button1** con `Caption = Converti`.

## 2. Comportamento (LOGICA)
1. Leggi il numero con **StrToFloat**.
2. **1 metro ≈ 3,28 piedi.** Se ItemIndex = 0 (Da metri): `R := valore * 3.28`. Altrimenti: `R := valore / 3.28`.
3. Risultato con **una cifra decimale**: `FormatFloat('0.0', …)`.

Controlli: 10 m → 32.8 piedi · 100 piedi → 30.5 m.

## 3. Uso con mouse E con tastiera (UX)
1. Deve funzionare su **Windows**, usabile col **mouse** e **solo con tastiera**.
2. Sistema **TabStop** e **TabOrder** (Edit1 → RadioGroup → Edit2 → Button); `Button1.Default = True`.

## 4. Consegna
1. 2 screenshot: app funzionante + codice del bottone.
2. Rispondi: cosa fa StrToFloat? cosa fa FormatFloat('0.0', …)? a cosa serve ItemIndex?
3. Consegna su Classroom.

## 5. Valutazione (100 punti)
| Voce | Punti |
|---|---|
| Componenti giusti | 20 |
| StrToFloat corretto | 15 |
| Due direzioni giuste (ItemIndex) | 25 |
| Risultato 1 decimale (FormatFloat) | 15 |
| Uso con tastiera (TabStop/TabOrder) | 10 |
| Sa spiegare a voce | 15 |
