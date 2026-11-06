unit Unit1;

{ 1INF - Lo scontrino che parla. Progetto Lazarus completo (livelli 1, 2, 3).
  Somme di stringhe, StrToInt, IntToStr e un if: niente cicli.
  Memo1.Lines.Add scrive UNA riga nuova per volta nello scontrino. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

{ Livello 1: riga semplice. Livello 2: if con la x. Livello 3: totale in Label2 e reset delle caselle }
procedure TForm1.Button1Click(Sender: TObject);
var
  riga: string;
  quanti, prezzo, costo, totale: Integer;
begin
  quanti := StrToInt(Edit3.Text);
  prezzo := StrToInt(Edit2.Text);
  costo := quanti * prezzo;
  if quanti > 1 then
    riga := Edit3.Text + ' x ' + Edit1.Text + ' da ' + Edit2.Text + ' euro: ' + IntToStr(costo) + ' euro'
  else
    riga := Edit1.Text + ' ' + Edit2.Text + ' euro';
  Memo1.Lines.Add(riga);
  totale := StrToInt(Label2.Caption) + costo;
  Label2.Caption := IntToStr(totale);
  Edit3.Text := '1';
  Edit1.Clear;
  Edit2.Clear;
  Edit1.SetFocus;
end;

{ Livello 3: la riga del totale }
procedure TForm1.Button2Click(Sender: TObject);
begin
  Memo1.Lines.Add('TOTALE: ' + Label2.Caption + ' euro. Grazie e arrivederci!');
end;

{ Livello 3: nuovo scontrino (Fallo tuo: metti il nome del TUO negozio) }
procedure TForm1.Button3Click(Sender: TObject);
begin
  Memo1.Clear;
  Memo1.Lines.Add('Negozio La Bottega');
  Label2.Caption := '0';
end;

end.
