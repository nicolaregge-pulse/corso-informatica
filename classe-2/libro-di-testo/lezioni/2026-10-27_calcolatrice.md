# La calcolatrice in Lazarus e su GitHub

**Versione 1.0** — 29/10/2026
*Libro parziale della 2INF: la lezione del 27/10/2026. Fa parte del libro di testo della classe (libro-classe2). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 27/10/2026, 2 ore, Informatica.
2. **Argomenti:** La calcolatrice in Lazarus (versione 1.0 dalla lavagna) e il suo posto su GitHub.

### La teoria e l'esercitazione

#### 01 La lavagna: la calcolatrice versione 1.0

![La lavagna di oggi: la finestra della calcolatrice versione 1.0](../../calcolatrice/lavagna-1-calcolatrice-v1.jpg)

1. La finestra (form) ha tre caselle **Edit**: N1 (primo numero), N2 (secondo numero) e TOTALE (il risultato).
2. Ha due bottoni (**Button**): **+** (più) e **×** (per).
3. Quando premi un bottone, il programma legge N1 e N2, fa il conto e scrive il risultato in TOTALE.

#### 02 StrToInt e IntToStr: testo e numeri

1. Quello che scrivi in una casella Edit è **testo**, anche se sono cifre: «12» è come una parola.
2. Con il testo non si fanno i conti. Prima va trasformato in numero: **StrToInt** (da testo a numero intero).
3. Il risultato è un numero. Per scriverlo nella casella va ritrasformato in testo: **IntToStr** (da numero intero a testo).
4. Il giro è sempre lo stesso: testo → StrToInt → conto → IntToStr → testo.

#### 03 Il codice della versione 1: più e per

```
procedure TForm1.ButtonPiuClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) + StrToInt(Edit2.Text));
end;

procedure TForm1.ButtonPerClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) * StrToInt(Edit2.Text));
end;
```

1. Edit1 è N1, Edit2 è N2, Edit3 è TOTALE.
2. Il codice di ogni bottone si scrive con un doppio clic sul bottone nel form.
3. Prova con Esegui: 7 + 5 = 12, 7 × 5 = 35.

#### 04 La versione 2: meno e divisione intera

```
procedure TForm1.ButtonMenoClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) - StrToInt(Edit2.Text));
end;

procedure TForm1.ButtonDivClick(Sender: TObject);
begin
  if StrToInt(Edit2.Text) = 0 then
    Edit3.Text := 'Non si divide per zero'
  else
    Edit3.Text := IntToStr(StrToInt(Edit1.Text) div StrToInt(Edit2.Text));
end;
```

1. **div** è la divisione intera: dà solo la parte intera, senza virgola. 7 div 2 = 3.
2. Dividere per zero non si può: il programma andrebbe in errore. Per questo prima controlliamo se N2 è 0 (if … then … else).

#### 05 Il tuo PC e GitHub

![La lavagna: su GitHub vanno i file sorgenti, niente .exe; repository lazarus, cartella calcolatrice; commit spesso](../../calcolatrice/lavagna-2-github.jpg)

1. Quando lavori con Lazarus, il programma sta sul tuo PC, nel disco fisso (HD): lavori **in locale**.
2. GitHub è su internet: una copia del progetto che resta al sicuro anche se il PC si rompe.
3. I due posti non si aggiornano da soli: sei tu a portare i file dal PC a GitHub.
4. Su GitHub vanno solo i **file sorgenti**: .lpi, .lpr, .pas, .lfm. Il file calcolatrice.exe NO: Lazarus lo rifà quando premi Esegui.

| Che cosa | Dove | Quando | Come |
|---|---|---|---|
| **Salvare** | sul tuo PC (in locale) | spessissimo, ogni pochi minuti | in Lazarus premi Ctrl + S |
| **Commit** | su GitHub (su internet) | ogni volta che una cosa nuova funziona | carichi i 4 file e premi «Commit changes» |

```
lazarus/
├── README.md
├── primo-programma/
├── salvadanaio/
└── calcolatrice/
    ├── calcolatrice.lpi
    ├── calcolatrice.lpr
    ├── unit1.pas
    └── unit1.lfm
```

#### 06 Su GitHub, passo per passo

1. Apri la pagina guidata: [La calcolatrice su GitHub](https://nicolaregge-pulse.github.io/corso-informatica/2inf-calcolatrice-github/). Ogni passo si apre solo quando quello prima è giusto.
2. La prima volta: crea la cartella con «Add file», «Create new file», nome **calcolatrice/README.md**, «Commit changes».
3. Poi entra nella cartella calcolatrice: «Add file», «Upload files», «choose your files», scegli SOLO i 4 file con Ctrl, «Commit changes».
4. Ogni volta che una cosa nuova funziona: Ctrl + S sul PC, poi ricarichi i 4 file su GitHub con un messaggio che dice che cosa hai cambiato (es. «aggiunto il bottone per»).

#### 07 La release: v1.0 e v2.0

1. Una **release** è una versione finita e funzionante, con un numero.
2. Versione 1 (più e per): nel repository lazarus, a destra, «Releases», «Create a new release», «Choose a tag», scrivi **v1.0**, «Create new tag», titolo «Calcolatrice versione 1», «Publish release».
3. Versione 2 (anche meno e divisione intera): lo stesso con **v2.0**.

#### 08 Sai spiegarlo?

1. A che cosa servono StrToInt e IntToStr?
2. Che differenza c'è tra salvare con Ctrl + S e fare un commit?
3. Perché su GitHub non mettiamo il file .exe?
4. Che cos'è la release v1.0?

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
