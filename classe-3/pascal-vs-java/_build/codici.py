# Codici comuni ai 3 documenti (uguali in tutte le lingue)
HP = "begin\n  writeln('Hello World');\nend."
HJ = "public class Ciao {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World\");\n    }\n}"
VP = "var\n  nome: string;\n  eta: integer;\n  voti: array[1..5] of integer;\nbegin\n  nome := 'Ali';\n  eta := 16;\n  voti[1] := 8;\n  readln(nome);        // leggo dalla tastiera\nend."
VJ = "String nome = \"Ali\";\nint eta = 16;\nint[] voti = new int[5];          // serve new\nvoti[0] = 8;                       // si parte da 0\nScanner tastiera = new Scanner(System.in);   // serve new\nnome = tastiera.nextLine();"
FP = "procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  ShowMessage('Hello World');\nend;"
FJ = "JFrame finestra = new JFrame(\"Ciao\");\nJButton bottone = new JButton(\"Premi\");\nbottone.addActionListener(e ->\n    JOptionPane.showMessageDialog(null, \"Hello World\"));\nfinestra.add(bottone);\nfinestra.setSize(300, 200);\nfinestra.setVisible(true);"
CP = "var lista: TStringList;\nbegin\n  lista := TStringList.Create;   // anche qui si crea\n  lista.Add('Ali');\n  lista.Free;                    // e si libera\nend;"
# v1.1 (26/10, Nicola): i programmi COMPLETI con la finestra e il bottone
UP = "unit Unit1;\n\n{$mode objfpc}{$H+}\n\ninterface\n\nuses\n  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;\n\ntype\n  TForm1 = class(TForm)\n    Button1: TButton;\n    procedure Button1Click(Sender: TObject);\n  end;\n\nvar\n  Form1: TForm1;\n\nimplementation\n\n{$R *.lfm}\n\nprocedure TForm1.Button1Click(Sender: TObject);\nbegin\n  ShowMessage('Hello World');   // l'UNICA riga scritta da te\nend;\n\nend."
JC = "import javax.swing.*;\n\npublic class Ciao {\n    public static void main(String[] args) {\n        JFrame finestra = new JFrame(\"Ciao\");\n        JButton bottone = new JButton(\"Premi\");\n        bottone.addActionListener(e ->\n            JOptionPane.showMessageDialog(finestra, \"Hello World\"));\n        finestra.add(bottone);\n        finestra.setSize(300, 200);\n        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n        finestra.setLocationRelativeTo(null);\n        finestra.setVisible(true);\n    }\n}"
JR = "C:\\java\\jdk\\bin\\java.exe Ciao.java"
