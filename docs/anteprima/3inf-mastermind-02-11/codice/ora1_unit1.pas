unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;      // Prova
    Edit1: TEdit;          // dove scrivi il tuo tentativo (4 cifre)
    Label1: TLabel;        // il risultato del tentativo
    Label2: TLabel;        // il codice segreto (per ora lo vediamo, poi lo nascondiamo)
    Memo1: TMemo;          // la lista dei tentativi
    procedure Button1Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    Segreto: String;       // il codice segreto, per esempio '3142'
    Tentativi: Integer;    // quanti tentativi hai fatto
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

procedure TForm1.FormCreate(Sender: TObject);
var
  i: Integer;
begin
  Randomize;                         // mescola i numeri a caso
  Segreto := '';
  for i := 1 to 4 do
    Segreto := Segreto + IntToStr(Random(6) + 1);   // una cifra da 1 a 6
  Tentativi := 0;
  Label2.Caption := 'Codice segreto: ' + Segreto;
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  i, giuste: Integer;
  tentativo: String;
begin
  tentativo := Edit1.Text;
  if Length(tentativo) <> 4 then
  begin
    Label1.Caption := 'Scrivi 4 cifre!';
    Exit;
  end;
  Tentativi := Tentativi + 1;
  giuste := 0;
  for i := 1 to 4 do
    if tentativo[i] = Segreto[i] then
      giuste := giuste + 1;
  Memo1.Lines.Add(IntToStr(Tentativi) + ') ' + tentativo + ' -> giuste: ' + IntToStr(giuste));
  if giuste = 4 then
    Label1.Caption := 'BRAVO! Hai indovinato in ' + IntToStr(Tentativi) + ' tentativi'
  else
    Label1.Caption := 'Cifre al posto giusto: ' + IntToStr(giuste);
  Edit1.Clear;
end;

end.
