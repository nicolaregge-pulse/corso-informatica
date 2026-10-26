# Object Pascal e Java a confronto

Perché con Object Pascal (Lazarus) si impara prima: meno codice, variabili senza «new», finestre disegnate con il mouse

Classe 3 · 26/10/2026 · Versione 1.0

Lo stesso programma scritto in due linguaggi. Guarda quante righe servono e quante parole nuove devi imparare: capirai perché per cominciare usiamo Lazarus.

## 01 Due linguaggi

**Object Pascal** è il linguaggio di **Lazarus** (e di Delphi). **Java** è un linguaggio molto usato nelle aziende e nelle app Android.

|  | Object Pascal (Lazarus) | Java |
|---|---|---|
| Come diventa un programma | compilato: diventa un file .exe | compilato in «bytecode», poi interpretato dalla Java Virtual Machine |
| Che cosa serve sul PC | niente: il .exe parte da solo | Java installato (la macchina virtuale) |
| Le finestre | le disegni con il mouse | le scrivi con il codice |

## 02 Hello World

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

## 03 Le variabili: niente «new»

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

## 04 Una finestra con un bottone

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

## 05 Riassunto

| Che cosa | Object Pascal | Java |
|---|---|---|
| Hello World | 1 riga dentro begin…end | 5 righe con classe e main |
| Variabili e array | nella sezione var, pronte subito | gli array e molti oggetti con new |
| Leggere dalla tastiera | readln | new Scanner(System.in) |
| Finestre e bottoni | disegnati con il mouse | scritti con il codice e new |
| Programma finito | un .exe che parte ovunque | serve Java installato |

## 06 Per essere onesti

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

## 07 Prova tu

1. Quante righe servono per Hello World in Object Pascal e quante in Java?
2. In Java, che cosa serve per creare un array di 5 numeri?
3. Perché un programma fatto con Lazarus parte su ogni PC Windows senza installare niente?

### Soluzioni

1. Object Pascal: 1 riga (dentro begin…end). Java: 5 righe con classe e main.
2. La parola new: int[] voti = new int[5];
3. Perché è compilato in un file .exe; Java invece ha bisogno della sua macchina virtuale installata.
