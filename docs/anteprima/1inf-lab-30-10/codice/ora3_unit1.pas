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
    Edit1: TEdit;
    Label1: TLabel;
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

procedure TForm1.Button1Click(Sender: TObject);
var
  punti: Integer;
begin
  punti := StrToInt(Label1.Caption);
  punti := punti + 1;
  Label1.Caption := IntToStr(punti);
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  punti: Integer;
  aggiunta: Integer;
begin
  punti := StrToInt(Label1.Caption);
  aggiunta := StrToInt(Edit1.Text);
  punti := punti + aggiunta;
  Label1.Caption := IntToStr(punti);
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  Label1.Caption := '0';
end;

end.
