unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

type
  TForm1 = class(TForm)
    Panel1: TPanel;        // la "diapositiva": cambia scritta e colore
    Label1: TLabel;        // per esempio "2 / 4"
    Button1: TButton;      // Indietro
    Button2: TButton;      // Avanti
    CheckBox1: TCheckBox;  // Automatico
    Timer1: TTimer;        // Interval = 2000 (2 secondi), Enabled = False
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure CheckBox1Change(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    N: Integer;            // quale diapositiva stiamo guardando (0, 1, 2, 3)
    procedure Mostra;
  public
  end;

const
  Scritte: array[0..3] of String = ('Ciao, sono io!', 'Il mio gioco', 'La mia squadra', 'Grazie!');
  Colori: array[0..3] of TColor = (clYellow, clAqua, clLime, clSilver);

var
  Form1: TForm1;

implementation

{$R *.lfm}

procedure TForm1.Mostra;
begin
  Panel1.Caption := Scritte[N];
  Panel1.Color := Colori[N];
  Label1.Caption := IntToStr(N + 1) + ' / 4';
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  N := 0;
  Timer1.Enabled := False;
  Mostra;
end;

procedure TForm1.Button2Click(Sender: TObject);   // Avanti
begin
  if N < 3 then N := N + 1 else N := 0;
  Mostra;
end;

procedure TForm1.Button1Click(Sender: TObject);   // Indietro
begin
  if N > 0 then N := N - 1 else N := 3;
  Mostra;
end;

procedure TForm1.CheckBox1Change(Sender: TObject);
begin
  Timer1.Enabled := CheckBox1.Checked;
end;

procedure TForm1.Timer1Timer(Sender: TObject);
begin
  Button2Click(Sender);        // ogni 2 secondi fa come se premessi Avanti
end;

end.
