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
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
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
  nome: String;
  animale: String;
begin
  nome := Edit1.Text;
  animale := Edit2.Text;
  Label1.Caption := nome + ' detto ' + animale + '!';
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Edit1.Text := '';
  Edit2.Text := '';
  Label1.Caption := '...';
end;

end.
