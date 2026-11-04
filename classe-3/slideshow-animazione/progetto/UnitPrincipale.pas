unit UnitPrincipale;

{ Slideshow animato 3INF - v1.0 (04/11/2026)
  I tuoi disegni, uno dopo l'altro, diventano un'animazione (come un cartone animato).
  - Al via il programma cerca la cartella "fotogrammi" vicino al progetto.
  - "Scegli cartella..." carica TUTTE le immagini di un'altra cartella, in ordine di nome.
  - La barra cambia la VELOCITA': quanti fotogrammi al secondo (e quindi l'Interval del Timer). }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  ComCtrls, UnitFotogrammi;

type

  { TFormSlideshow }

  TFormSlideshow = class(TForm)
    ImmagineFotogramma: TImage;         // qui si vede il disegno
    PannelloComandi: TPanel;            // la fascia dei comandi in basso
    BottoneCartella: TButton;           // "Scegli cartella..."
    BottoneIndietro: TButton;           // "< Indietro"
    BottoneAvvia: TButton;              // "Avvia"
    BottoneFerma: TButton;              // "Ferma"
    BottoneAvanti: TButton;             // "Avanti >"
    BarraVelocita: TTrackBar;           // da 1 a 24 fotogrammi al secondo
    EtichettaVelocita: TLabel;          // "6 fotogrammi al secondo (167 ms)"
    EtichettaFotogramma: TLabel;        // "Fotogramma 2 / 6"
    TimerAnimazione: TTimer;            // ogni Interval millisecondi: fotogramma dopo
    DialogoCartella: TSelectDirectoryDialog;
    procedure BarraVelocitaChange(Sender: TObject);
    procedure BottoneAvantiClick(Sender: TObject);
    procedure BottoneAvviaClick(Sender: TObject);
    procedure BottoneCartellaClick(Sender: TObject);
    procedure BottoneFermaClick(Sender: TObject);
    procedure BottoneIndietroClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure TimerAnimazioneTimer(Sender: TObject);
  private
    Fotogrammi: array of TPicture;      // i disegni gia' caricati in memoria
    Quanti: Integer;                    // quanti disegni ci sono
    N: Integer;                         // quale disegno stiamo guardando (0 = il primo)
    procedure SvuotaFotogrammi;
    procedure CaricaCartella(const Cartella: String);
    procedure Mostra;
    procedure AggiornaVelocita;
  public
  end;

var
  FormSlideshow: TFormSlideshow;

implementation

{$R *.lfm}

{ TFormSlideshow }

procedure TFormSlideshow.FormCreate(Sender: TObject);
begin
  Quanti := 0;
  N := 0;
  TimerAnimazione.Enabled := False;
  AggiornaVelocita;
  { la cartella "fotogrammi" sta vicino al programma (e al progetto) }
  CaricaCartella(Application.Location + 'fotogrammi');
end;

procedure TFormSlideshow.FormDestroy(Sender: TObject);
begin
  SvuotaFotogrammi;
end;

procedure TFormSlideshow.SvuotaFotogrammi;
var
  I: Integer;
begin
  for I := 0 to Quanti - 1 do
    Fotogrammi[I].Free;
  SetLength(Fotogrammi, 0);
  Quanti := 0;
end;

procedure TFormSlideshow.CaricaCartella(const Cartella: String);
var
  Elenco: TStringList;
  I: Integer;
  Disegno: TPicture;
begin
  TimerAnimazione.Enabled := False;
  SvuotaFotogrammi;
  Elenco := TStringList.Create;
  try
    ElencaFotogrammi(Cartella, Elenco);          // tutti i .bmp .png .jpg, in ordine di nome
    SetLength(Fotogrammi, Elenco.Count);
    for I := 0 to Elenco.Count - 1 do
    begin
      Disegno := TPicture.Create;
      try
        Disegno.LoadFromFile(Elenco[I]);
        Fotogrammi[Quanti] := Disegno;
        Inc(Quanti);
      except
        Disegno.Free;                            // un file rovinato si salta
      end;
    end;
  finally
    Elenco.Free;
  end;
  N := 0;
  Caption := 'Slideshow animato - ' + ExtractFileName(ExcludeTrailingPathDelimiter(Cartella));
  Mostra;
end;

procedure TFormSlideshow.Mostra;
begin
  if Quanti = 0 then
  begin
    ImmagineFotogramma.Picture.Clear;
    EtichettaFotogramma.Caption := 'Nessun disegno: premi "Scegli cartella..."';
    Exit;
  end;
  ImmagineFotogramma.Picture.Assign(Fotogrammi[N]);
  EtichettaFotogramma.Caption := 'Fotogramma ' + IntToStr(N + 1) + ' / ' + IntToStr(Quanti);
end;

procedure TFormSlideshow.AggiornaVelocita;
begin
  { Position = fotogrammi al secondo. 1000 ms = 1 secondo. }
  TimerAnimazione.Interval := 1000 div BarraVelocita.Position;
  EtichettaVelocita.Caption := IntToStr(BarraVelocita.Position) + ' fotogrammi al secondo (' +
    IntToStr(TimerAnimazione.Interval) + ' ms)';
end;

procedure TFormSlideshow.BarraVelocitaChange(Sender: TObject);
begin
  AggiornaVelocita;
end;

procedure TFormSlideshow.BottoneAvantiClick(Sender: TObject);
begin
  if Quanti = 0 then Exit;
  N := (N + 1) mod Quanti;                       // dopo l'ultimo torna al primo
  Mostra;
end;

procedure TFormSlideshow.BottoneIndietroClick(Sender: TObject);
begin
  if Quanti = 0 then Exit;
  N := (N - 1 + Quanti) mod Quanti;              // prima del primo va all'ultimo
  Mostra;
end;

procedure TFormSlideshow.BottoneAvviaClick(Sender: TObject);
begin
  if Quanti > 0 then
    TimerAnimazione.Enabled := True;
end;

procedure TFormSlideshow.BottoneFermaClick(Sender: TObject);
begin
  TimerAnimazione.Enabled := False;
end;

procedure TFormSlideshow.BottoneCartellaClick(Sender: TObject);
begin
  if DialogoCartella.Execute then
    CaricaCartella(DialogoCartella.FileName);
end;

procedure TFormSlideshow.TimerAnimazioneTimer(Sender: TObject);
begin
  BottoneAvantiClick(Sender);                    // il Timer "preme Avanti" da solo
end;

end.
