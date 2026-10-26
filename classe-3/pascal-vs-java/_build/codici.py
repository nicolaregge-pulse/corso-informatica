# Codici comuni ai 3 documenti (uguali in tutte le lingue)
HP = "begin\n  writeln('Hello World');\nend."
HJ = "public class Ciao {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World\");\n    }\n}"
VP = "var\n  nome: string;\n  eta: integer;\n  voti: array[1..5] of integer;\nbegin\n  nome := 'Ali';\n  eta := 16;\n  voti[1] := 8;\n  readln(nome);        // leggo dalla tastiera\nend."
VJ = "String nome = \"Ali\";\nint eta = 16;\nint[] voti = new int[5];          // serve new\nvoti[0] = 8;                       // si parte da 0\nScanner tastiera = new Scanner(System.in);   // serve new\nnome = tastiera.nextLine();"
FP = "procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  ShowMessage('Hello World');\nend;"
FJ = "JFrame finestra = new JFrame(\"Ciao\");\nJButton bottone = new JButton(\"Premi\");\nbottone.addActionListener(e ->\n    JOptionPane.showMessageDialog(null, \"Hello World\"));\nfinestra.add(bottone);\nfinestra.setSize(300, 200);\nfinestra.setVisible(true);"
CP = "var lista: TStringList;\nbegin\n  lista := TStringList.Create;   // anche qui si crea\n  lista.Add('Ali');\n  lista.Free;                    // e si libera\nend;"
