unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ComCtrls;

type
  TForm1 = class(TForm)
    PageControl1: TPageControl;   // le schede
    TabSheet1: TTabSheet;         // scheda Gioco
    TabSheet2: TTabSheet;         // scheda Regole
    TabSheet3: TTabSheet;         // scheda Record
    Button1: TButton;             // Prova
    Button2: TButton;             // Nuova partita
    Edit1: TEdit;                 // il tuo tentativo
    Label1: TLabel;               // risultato del tentativo
    Label2: TLabel;               // il codice segreto (per provare)
    Label3: TLabel;               // le regole (scheda Regole)
    Label4: TLabel;               // il record (scheda Record)
    Memo1: TMemo;                 // i tentativi
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    Segreto: String;
    Tentativi: Integer;
    Record_: Integer;             // il minor numero di tentativi (0 = nessun record)
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
  Randomize;
  Record_ := 0;
  Label3.Caption := 'Il computer pensa 4 cifre da 1 a 6. ' +
    'Tu provi. "Esatte" = cifra giusta al posto giusto. ' +
    '"Spostate" = cifra giusta ma al posto sbagliato.';
  Label4.Caption := 'Record: nessuno (gioca una partita!)';
  Button2Click(Sender);              // comincia una partita nuova
end;

procedure TForm1.Button2Click(Sender: TObject);   // Nuova partita
var
  i: Integer;
begin
  Segreto := '';
  for i := 1 to 4 do
    Segreto := Segreto + IntToStr(Random(6) + 1);
  Tentativi := 0;
  Memo1.Clear;
  Edit1.Clear;
  Label2.Caption := 'Codice segreto: ' + Segreto;
  Label1.Caption := 'Partita nuova: indovina le 4 cifre (da 1 a 6)';
end;

procedure TForm1.Button1Click(Sender: TObject);   // Prova
var
  i, j, esatte, spostate: Integer;
  tentativo: String;
  usataS, usataT: array[1..4] of Boolean;
begin
  tentativo := Edit1.Text;
  if Length(tentativo) <> 4 then
  begin
    Label1.Caption := 'Scrivi 4 cifre!';
    Exit;
  end;
  Tentativi := Tentativi + 1;
  for i := 1 to 4 do
  begin
    usataS[i] := False;
    usataT[i] := False;
  end;
  esatte := 0;
  for i := 1 to 4 do                      // prima le esatte
    if tentativo[i] = Segreto[i] then
    begin
      esatte := esatte + 1;
      usataS[i] := True;
      usataT[i] := True;
    end;
  spostate := 0;
  for i := 1 to 4 do                      // poi le spostate
    if not usataT[i] then
      for j := 1 to 4 do
        if (not usataS[j]) and (tentativo[i] = Segreto[j]) then
        begin
          spostate := spostate + 1;
          usataS[j] := True;
          Break;
        end;
  Memo1.Lines.Add(IntToStr(Tentativi) + ') ' + tentativo + ' -> esatte: ' +
    IntToStr(esatte) + '  spostate: ' + IntToStr(spostate));
  if esatte = 4 then
  begin
    Label1.Caption := 'BRAVO! Indovinato in ' + IntToStr(Tentativi) + ' tentativi';
    if (Record_ = 0) or (Tentativi < Record_) then
    begin
      Record_ := Tentativi;
      Label4.Caption := 'Record: ' + IntToStr(Record_) + ' tentativi';
    end;
  end
  else
    Label1.Caption := 'Esatte: ' + IntToStr(esatte) + '  Spostate: ' + IntToStr(spostate);
  Edit1.Clear;
end;

end.
