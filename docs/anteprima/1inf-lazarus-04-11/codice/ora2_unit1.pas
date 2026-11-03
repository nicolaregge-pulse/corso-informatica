unit Unit1;

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
    Button4: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
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
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' più ' + IntToStr(b) + ' fa ' + IntToStr(a + b);
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' meno ' + IntToStr(b) + ' fa ' + IntToStr(a - b);
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  Label1.Caption := IntToStr(a) + ' per ' + IntToStr(b) + ' fa ' + IntToStr(a * b);
end;

procedure TForm1.Button4Click(Sender: TObject);
var
  a, b: Integer;
begin
  a := StrToIntDef(Edit1.Text, 0);
  b := StrToIntDef(Edit2.Text, 0);
  if b = 0 then
    Label1.Caption := 'Non si può dividere per zero'
  else
    Label1.Caption := IntToStr(a) + ' diviso ' + IntToStr(b) + ' fa ' + IntToStr(a div b);
end;


end.
