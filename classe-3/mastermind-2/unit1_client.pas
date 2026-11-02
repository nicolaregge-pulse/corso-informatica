unit Unit1;
{ Il Mastermind NORMALE della 3INF (ora2_unit1.pas) con in piu' la scheda "Classifica".
  Il gioco ora e' contro il codice del SERVER del prof, uguale per tutta la classe.
  Cosa e' cambiato rispetto a prima: vedi i commenti "// NUOVO" e "// CAMBIATO". }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ComCtrls, ExtCtrls,
  mm_logica, mm_tcp, client_unit;                 // NUOVO: i 4 file del Mastermind 2.0

type
  TForm1 = class(TForm)
    PageControl1: TPageControl;   // le schede
    TabSheet1: TTabSheet;         // scheda Gioco
    TabSheet2: TTabSheet;         // scheda Regole
    TabSheet3: TTabSheet;         // scheda Classifica (prima si chiamava Record)
    Button1: TButton;             // Prova
    Button2: TButton;             // Nuova partita (ora la decide il prof: non fa niente)
    Edit1: TEdit;                 // il tuo tentativo
    Edit2: TEdit;                 // NUOVO: il tuo nome (nella scheda Gioco)
    Label1: TLabel;               // risultato del tentativo
    Label2: TLabel;               // (il codice ora e' segreto: resta li' ma non lo mostra)
    Label3: TLabel;               // le regole (scheda Regole)
    Label4: TLabel;               // CAMBIATO: la console della classifica (scheda Classifica)
    Memo1: TMemo;                 // i tentativi
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    Cl: TMMClient;                // NUOVO: tutta la parte di rete/file sta qui dentro
    Orologio3s: TTimer;           // NUOVO: ogni 3 secondi aggiorna la classifica (creato nel codice)
    UltimoTentativo: String;
    procedure Timer1Timer(Sender: TObject);
    procedure MostraEsito(const R: TRisposta; const Tent: String);
    procedure RispostaTentativo(Sender: TObject);
    procedure RispostaStato(Sender: TObject);
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
  Label3.Caption := 'Il server del prof pensa 4 cifre da 1 a 6, uguali per tutti. ' +
    'Tu provi. "Esatte" = cifra giusta al posto giusto. ' +
    '"Spostate" = cifra giusta ma al posto sbagliato. Vince chi usa meno tentativi.';
  Label4.Caption := 'Scrivi il tuo nome e aspetta il Via del prof';
  Cl := TMMClient.Create;
  // legge server.txt (IP:PORTA) e/o cartella.txt accanto al programma
  if not Cl.CaricaConfig(ExtractFilePath(Application.ExeName)) then
    Label1.Caption := 'Manca il file server.txt o cartella.txt accanto al programma';
  Label2.Caption := 'Codice segreto: ????';
  Orologio3s := TTimer.Create(Self);        // il timer nasce qui, non serve metterlo sulla Form
  Orologio3s.Interval := 3000;
  Orologio3s.OnTimer := @Timer1Timer;
  Orologio3s.Enabled := True;
end;

procedure TForm1.Button2Click(Sender: TObject);   // Nuova partita
begin
  Label1.Caption := 'La nuova partita la fa partire il prof';
end;

{ Scrive nel Label1 e nel Memo cosa e' successo }
procedure TForm1.MostraEsito(const R: TRisposta; const Tent: String);
begin
  Label1.Caption := Cl.TestoRisposta(R);
  if (R.Tipo = 'RESULT') or (R.Tipo = 'WIN') then
    Memo1.Lines.Add(IntToStr(R.Sintesi.Tentativi) + ') ' + Tent + ' -> esatte: ' +
      IntToStr(R.Esatte) + '  spostate: ' + IntToStr(R.Spostate));
  Label4.Caption := Cl.Console;
end;

procedure TForm1.Button1Click(Sender: TObject);   // Prova
begin
  Cl.Nome := Edit2.Text;
  UltimoTentativo := Edit1.Text;
  if Length(UltimoTentativo) <> 4 then
  begin
    Label1.Caption := 'Scrivi 4 cifre!';
    Exit;
  end;
  if Cl.Modo = moRete then
  begin
    Label1.Caption := 'Invio al server...';
    // la richiesta parte in un THREAD: la finestra non si blocca
    TMMRichiestaAsync.Create(Cl.Host, Cl.Porta, Cl.RigaProva(UltimoTentativo), @RispostaTentativo);
  end
  else
    MostraEsito(Cl.Prova(UltimoTentativo), UltimoTentativo);   // i file sono veloci
  Edit1.Clear;
end;

procedure TForm1.RispostaTentativo(Sender: TObject);   // chiamata quando il server ha risposto
var
  testo: String;
begin
  testo := TMMRichiestaAsync(Sender).Risposta;
  MostraEsito(Cl.RispostaDaRete(testo, UltimoTentativo), UltimoTentativo);
end;

procedure TForm1.RispostaStato(Sender: TObject);
begin
  Cl.ApplicaRisposta(TMMRichiestaAsync(Sender).Risposta);
  Label4.Caption := Cl.Console;
end;

procedure TForm1.Timer1Timer(Sender: TObject);   // ogni 3 secondi
begin
  Cl.Nome := Edit2.Text;
  if Cl.Nome = '' then Exit;
  if Cl.Modo = moRete then
    TMMRichiestaAsync.Create(Cl.Host, Cl.Porta, Cl.RigaStato, @RispostaStato)
  else
  begin
    Cl.Aggiorna;
    Label4.Caption := Cl.Console;
  end;
end;

end.
