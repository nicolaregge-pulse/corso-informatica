# 2INF Lazarus: il ciclo FOR, la tua app «da … a …»

**Versione 1.0** · Classe 2 · 15/10/2026 · istruzioni passo passo · solo italiano

## 01 Che cosa costruisci oggi

Un'app con due caselle: **da** [ 5 ] **a** [ 12 ]. Premi il bottone e nel riquadro grande compaiono i numeri da 5 a 12, uno per riga. Il computer li scrive da solo, con il **ciclo FOR**: una riga di codice che si ripete tante volte.

> **Nota:** ti blocchi? Apri la pagina del percorso e scrivi la domanda nella casella «Chiedi aiuto all'assistente del Prof Regge». L'indirizzo è nel compito di Classroom.

## 02 La teoria in 5 righe

1. Il **ciclo FOR** ripete quello che c'è tra **begin** ed **end**.
2. `for giro := 5 to 12 do` vuol dire: per giro che va da 5 a 12, fai.
3. **giro** è il **contatore**: una variabile intera (`integer`) che a ogni giro aumenta di 1. Va dichiarata con `var`.
4. I giri sono: fine meno inizio più 1. Da 5 a 12 sono 8 giri.
5. **StrToInt** trasforma il testo di una casella in numero; **IntToStr** trasforma un numero in testo, per scriverlo nel riquadro.

## 03 I componenti della lavagna

| Componente | A cosa serve | Che cosa cambi nell'Ispettore |
|---|---|---|
| TLabel | la scritta «da» | Caption: da |
| TEdit (Edit1) | la casella del primo numero | Text: vuoto |
| TLabel | la scritta «a» | Caption: a |
| TEdit (Edit2) | la casella del secondo numero | Text: vuoto |
| TMemo (Memo1) | il riquadro grande dove compaiono i numeri | ScrollBars: ssBoth (le barre per scorrere) |
| TButton (Button1) | il bottone che fa partire il ciclo | Caption: Conta! |

## 04 I passi in Lazarus

Un passo alla volta. Ogni passo è una cosa sola.

1. Apri Lazarus.
2. In alto clicca il menu **Progetto**, poi **Nuovo progetto**, poi **Applicazione**, poi **Ok**.
3. In alto, nella scheda **Standard** dei componenti, clicca **TLabel**, poi clicca sul form in alto a sinistra.
4. Nell'**Ispettore oggetti** (a sinistra), alla riga **Caption**, scrivi «da» e premi Invio.
5. Nella scheda Standard clicca **TEdit**, poi clicca sul form accanto a «da».
6. Nell'Ispettore, alla riga **Text**, cancella il testo e premi Invio.
7. Metti un altro **TLabel** più a destra; nella Caption scrivi «a».
8. Metti un altro **TEdit** accanto ad «a»; cancella il suo Text.
9. Nella scheda Standard clicca **TMemo** e disegna sul form un riquadro grande, al centro.
10. Nell'Ispettore, alla riga **ScrollBars**, scegli **ssBoth**: così compaiono le barre per scorrere e vedere i valori sotto.
11. Metti un **TButton** in basso; nella Caption scrivi «Conta!».
12. Fai **doppio clic** sul bottone: si apre il codice, dentro `Button1Click`.
13. Scrivi il codice qui sotto, riga per riga, con i rientri (le righe dentro si spostano a destra di 3 spazi).

```
procedure TForm1.Button1Click(Sender: TObject);
var giro, inizio, fine: integer;
begin
   inizio := StrToInt(Edit1.Text);
   fine := StrToInt(Edit2.Text);
   Memo1.Clear;
   for giro := inizio to fine do
   begin
      Memo1.Lines.Add(IntToStr(giro));
   end;
end;
```

14. Premi **F9**: l'app parte.
15. Scrivi 5 nella prima casella e 12 nella seconda, poi premi **Conta!**. Compaiono i numeri da 5 a 12. **FATTO!**
16. Prova da 1 a 100: i numeri non ci stanno tutti. Usa la **barra di scorrimento** a destra del riquadro per vedere quelli sotto.

## 05 Fallo tuo

1. Accanto al numero metti una frase tua: `Memo1.Lines.Add(IntToStr(giro) + ' - forza!');`
2. Cambia il titolo della finestra: clicca sul form vuoto e nell'Ispettore cambia la sua **Caption** con un nome tuo.
3. **Sfida:** la tabellina del 7: `Memo1.Lines.Add(IntToStr(giro) + ' x 7 = ' + IntToStr(giro * 7));`

## 06 Gli errori di tutti

| Che cosa vedi | Perché | Come si sistema |
|---|---|---|
| «Identifier not found» su giro | il contatore non è dichiarato | scrivi `var giro, inizio, fine: integer;` sopra il begin |
| il ciclo scrive una riga sola | c'è un punto e virgola dopo `do` | togli il `;` dopo do |
| errore sulla riga del Memo | manca IntToStr | scrivi `IntToStr(giro)` |
| errore quando premi Conta! | una casella è vuota o non ha un numero | scrivi un numero in tutte e due le caselle |
| Lazarus non compila | manca un `end;` | ogni begin ha il suo end |

> **Nota:** sbagliare è normale, succede a tutti i programmatori, anche ai professionisti. Leggi il messaggio di Lazarus, guarda la tabella, prova di nuovo.
