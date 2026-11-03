unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Label1: TLabel;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var
  prezzo, dati, resto, b10, b5, m2, m1: Integer;
begin
  prezzo := StrToIntDef(Edit2.Text, 0);
  dati := StrToIntDef(Edit3.Text, 0);
  resto := dati - prezzo;
  b10 := resto div 10;
  resto := resto mod 10;
  b5 := resto div 5;
  resto := resto mod 5;
  m2 := resto div 2;
  m1 := resto mod 2;
  Memo1.Clear;
  Memo1.Lines.Add('SCONTRINO');
  Memo1.Lines.Add('Cliente: ' + Edit1.Text);
  Memo1.Lines.Add('Prezzo: ' + IntToStr(prezzo) + ' euro');
  Memo1.Lines.Add('Dati: ' + IntToStr(dati) + ' euro');
  Memo1.Lines.Add('Resto: ' + IntToStr(dati - prezzo) + ' euro');
  Memo1.Lines.Add(IntToStr(b10) + ' banconote da 10, ' + IntToStr(b5) + ' da 5');
  Memo1.Lines.Add(IntToStr(m2) + ' monete da 2, ' + IntToStr(m1) + ' da 1');
end;


end.
