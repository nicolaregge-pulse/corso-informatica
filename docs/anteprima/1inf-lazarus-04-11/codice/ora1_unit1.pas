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
    Button5: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
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
  km, metri: Integer;
begin
  km := StrToInt(Edit1.Text);
  metri := km * 1000;
  Label1.Caption := IntToStr(metri) + ' metri';
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  ore, minuti: Integer;
begin
  ore := StrToInt(Edit1.Text);
  minuti := ore * 60;
  Label1.Caption := IntToStr(minuti) + ' minuti';
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  euro, centesimi: Integer;
begin
  euro := StrToInt(Edit1.Text);
  centesimi := euro * 100;
  Label1.Caption := IntToStr(centesimi) + ' centesimi';
end;

procedure TForm1.Button4Click(Sender: TObject);
var
  c, f: Integer;
begin
  c := StrToInt(Edit1.Text);
  f := c * 9 div 5 + 32;
  Label1.Caption := IntToStr(c) + ' gradi C sono ' + IntToStr(f) + ' gradi F';
end;

procedure TForm1.Button5Click(Sender: TObject);
var
  minuti, ore, resto: Integer;
begin
  minuti := StrToInt(Edit1.Text);
  ore := minuti div 60;
  resto := minuti mod 60;
  Label1.Caption := IntToStr(minuti) + ' minuti sono ' + IntToStr(ore) + ' ore e ' + IntToStr(resto) + ' minuti';
end;


end.
