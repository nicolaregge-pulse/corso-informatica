# Compito Lazarus — Convertitore Celsius ↔ Fahrenheit

**Classe 2 · Informatica · Versione 1.1 · da svolgere da soli**

**Cosa devi fare:** costruisci un'app in Lazarus **uguale nella struttura** a quella
Km/h↔mph vista a lezione, ma che converte le **temperature** (°C ↔ °F). Cambia solo la
formula: il metodo è lo stesso.

## 1. Componenti (UI)
1. **Edit1** (°C) e **Edit2** (°F).
2. **RadioGroup1** con `Da C a F` e `Da F a C` (ItemIndex = 0).
3. **Button1** con `Caption = Converti`.

## 2. Comportamento (LOGICA)
1. Leggi il numero con **StrToFloat**.
2. Se ItemIndex = 0: **F = C × 9/5 + 32**. Altrimenti: **C = (F − 32) × 5/9**.
3. Scrivi il risultato con **una cifra decimale** con **FormatFloat('0.0', …)**.

Controlli: 100 °C → 212.0 °F · 32 °F → 0.0 °C · 37 °C → 98.6 °F.

## 3. Uso con mouse E con tastiera (UX)
1. Deve funzionare su **Windows**, usabile col **mouse** e **solo con tastiera**.
2. Sistema **TabStop** e **TabOrder** (ordine: Edit1 → RadioGroup → Edit2 → Button).
3. `Button1.Default = True` così `Invio` lancia la conversione.

## 4. Consegna
1. 2 screenshot: app funzionante + codice del bottone.
2. Rispondi: cosa fa StrToFloat? cosa fa FormatFloat('0.0', …)? a cosa serve TabOrder?
3. Consegna su Classroom.

## 5. Valutazione (100 punti)
| Voce | Punti |
|---|---|
| Componenti giusti (RadioGroup, 2 Edit, Button) | 20 |
| StrToFloat corretto | 15 |
| Due formule giuste con RadioGroup (ItemIndex) | 25 |
| Risultato con 1 decimale (FormatFloat) | 15 |
| Uso con tastiera: TabStop/TabOrder | 10 |
| Sa spiegare a voce | 15 |

Conta la comprensione: se il metodo è giusto e sai spiegarlo, va bene anche con piccoli errori.
