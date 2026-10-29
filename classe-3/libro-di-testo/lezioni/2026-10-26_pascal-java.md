# Object Pascal e Java

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 26/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 26/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Confronto tra Object Pascal e Java: Hello World, compilato e interpretato.

### La teoria e l'esercitazione

Perché con Object Pascal (Lazarus) si impara prima: meno codice, variabili senza «new», finestre disegnate con il mouse

Classe 3 · 26/10/2026 · Versione 1.1

Lo stesso programma scritto in due linguaggi. Guarda quante righe servono e quante parole nuove devi imparare: capirai perché per cominciare usiamo Lazarus.

#### 01 Due linguaggi

**Object Pascal** è il linguaggio di **Lazarus** (e di Delphi). **Java** è un linguaggio molto usato nelle aziende e nelle app Android.

|  | Object Pascal (Lazarus) | Java |
|---|---|---|
| Come diventa un programma | compilato: diventa un file .exe | compilato in «bytecode», poi interpretato dalla Java Virtual Machine |
| Che cosa serve sul PC | niente: il .exe parte da solo | Java installato (la macchina virtuale) |
| Le finestre | le disegni con il mouse | le scrivi con il codice |

#### 02 Hello World

**Object Pascal**

```
begin
  writeln('Hello World');
end.
```

**Java**

```
public class Ciao {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

In Java già per scrivere una frase servono una **classe** e il metodo **main**, con parole come **public**, **static**, **void**, **String[] args**. In Object Pascal bastano **begin** ed **end**.

#### 03 Le variabili: niente «new»

In Object Pascal le variabili si **dichiarano** nella sezione **var** con nome e tipo, e poi si usano subito. Anche un array è già pronto.

**Object Pascal**

```
var
  nome: string;
  eta: integer;
  voti: array[1..5] of integer;
begin
  nome := 'Ali';
  eta := 16;
  voti[1] := 8;
  readln(nome);        // leggo dalla tastiera
end.
```

In Java i tipi semplici (int, double) vanno bene, ma per un array o per leggere dalla tastiera bisogna **creare un oggetto** con la parola **new**.

**Java**

```
String nome = "Ali";
int eta = 16;
int[] voti = new int[5];          // serve new
voti[0] = 8;                       // si parte da 0
Scanner tastiera = new Scanner(System.in);   // serve new
nome = tastiera.nextLine();
```

> **Da sapere.** In Java l'array parte da 0; in Pascal decidi tu dove parte (qui da 1). In Java ogni cosa «grande» va creata con new prima di usarla.

#### 04 Una finestra con un bottone

Con Lazarus trascini il bottone sul Form, fai doppio clic e scrivi **una riga**:

**Object Pascal (Lazarus)**

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello World');
end;
```

In Java (con Swing) la finestra e il bottone si scrivono tutti con il codice, e ognuno si crea con **new**:

**Java**

```
JFrame finestra = new JFrame("Ciao");
JButton bottone = new JButton("Premi");
bottone.addActionListener(e ->
    JOptionPane.showMessageDialog(null, "Hello World"));
finestra.add(bottone);
finestra.setSize(300, 200);
finestra.setVisible(true);
```

#### 05 Riassunto

| Che cosa | Object Pascal | Java |
|---|---|---|
| Hello World | 1 riga dentro begin…end | 5 righe con classe e main |
| Variabili e array | nella sezione var, pronte subito | gli array e molti oggetti con new |
| Leggere dalla tastiera | readln | new Scanner(System.in) |
| Finestre e bottoni | disegnati con il mouse | scritti con il codice e new |
| Programma finito | un .exe che parte ovunque | serve Java installato |

#### 06 Per essere onesti

Anche in Object Pascal le **classi** più complesse si creano (**Create**) e poi si liberano (**Free**). Java invece libera la memoria da solo. E Java è usatissimo nel lavoro: per questo è bene sapere che esiste.

**Object Pascal**

```
var lista: TStringList;
begin
  lista := TStringList.Create;   // anche qui si crea
  lista.Add('Ali');
  lista.Free;                    // e si libera
end;
```

> **Da sapere.** Per imparare a programmare e vedere subito il risultato, però, Object Pascal con Lazarus è la strada più semplice: meno parole da imparare, finestre con il mouse, un .exe che funziona ovunque.

#### 07 I due programmi completi, con la finestra e il bottone

**Lazarus.** Tutto questo codice lo scrive Lazarus da solo quando trascini il bottone sul Form. Tu scrivi **una riga** sola: quella con ShowMessage.

**Object Pascal: Unit1.pas**

```
unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello World');   // l'UNICA riga scritta da te
end;

end.
```

**Java.** Qui ogni riga la scrivi tu: la finestra, il bottone, che cosa succede al clic, la grandezza, la chiusura. Ogni oggetto si crea con **new**.

**Java: Ciao.java**

```
import javax.swing.*;

public class Ciao {
    public static void main(String[] args) {
        JFrame finestra = new JFrame("Ciao");
        JButton bottone = new JButton("Premi");
        bottone.addActionListener(e ->
            JOptionPane.showMessageDialog(finestra, "Hello World"));
        finestra.add(bottone);
        finestra.setSize(300, 200);
        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        finestra.setLocationRelativeTo(null);
        finestra.setVisible(true);
    }
}
```

#### 08 Provare Java senza installare niente

A scuola non si installa niente. Ci sono due modi per vedere la finestra di Java.

1. <b>Nel browser, con JavaFiddle.</b> Apri l'indirizzo qui sotto, cancella il codice di esempio, incolla il programma Ciao.java e premi «Run»: la finestra con il bottone si apre dentro la pagina. Funziona solo se il firewall della scuola lascia passare il sito.
2. <b>Java portabile, come Godot.</b> Si scarica Java in versione .zip (per esempio «Eclipse Temurin JDK», file zip) e si scompatta in una cartella, per esempio C:\java\jdk: niente installazione e niente amministratore. Dalla Java 11 in poi basta un comando per far partire il file Ciao.java, senza compilarlo a parte.

Indirizzo di JavaFiddle, da scrivere così: **javafiddle.leaningtech.com**

**Comando per Java portabile (cartella del file Ciao.java)**

```
C:\java\jdk\bin\java.exe Ciao.java
```

> **Da sapere.** Con Lazarus invece il programma diventa un file .exe: lo copi su una chiavetta e parte su qualunque PC Windows, anche senza Lazarus.

#### 09 Prova tu

1. Quante righe servono per Hello World in Object Pascal e quante in Java?
2. In Java, che cosa serve per creare un array di 5 numeri?
3. Perché un programma fatto con Lazarus parte su ogni PC Windows senza installare niente?

##### Soluzioni

1. Object Pascal: 1 riga (dentro begin…end). Java: 5 righe con classe e main.
2. La parola new: int[] voti = new int[5];
3. Perché è compilato in un file .exe; Java invece ha bisogno della sua macchina virtuale installata.

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
