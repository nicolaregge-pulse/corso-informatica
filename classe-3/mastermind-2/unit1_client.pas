unit Unit1;
{ MASTERMIND 2.0 - IL CLIENT DEI RAGAZZI (la finestra).

  Tutta la classe gioca INSIEME sulla stessa combinazione segreta, pensata dal
  PC del prof (il SERVER). Tu provi, il server ti dice quante cifre sono
  "esatte" e quante "spostate", e ti mette in classifica.

  I passi del gioco, nell'ordine:
    1. Scrivi l'indirizzo del server (te lo dice il prof) e il tuo nome.
    2. Premi "Connetti": il programma chiede al server "ci sei?".
    3. Scrivi 4 cifre da 1 a 6 e premi "Prova".
    4. Ogni 3 secondi la classifica si aggiorna da sola.

  Le parti difficili (rete, protocollo) stanno nei file mm_logica, mm_tcp e
  client_unit: qui c'e' solo la finestra. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  mm_logica, mm_tcp, client_unit;

type
  TForm1 = class(TForm)
    LblTitoloServer: TLabel;   // scritta sopra l'indirizzo
    LblTitoloNome: TLabel;     // scritta sopra il nome
    LblTitoloTentativo: TLabel; // scritta sopra il tentativo
    EdServer: TEdit;        // indirizzo del server, per esempio 192.168.10.5:5050
    EdNome: TEdit;          // il tuo nome
    BtnConnetti: TButton;   // "Connetti"
    EdTentativo: TEdit;     // le 4 cifre che provi
    BtnProva: TButton;      // "Prova"
    LblStato: TLabel;       // dice se sei collegato al server
    LblEsito: TLabel;       // risultato dell'ultimo tentativo
    LblClassifica: TLabel;  // migliore e peggiore della classe
    LblPosizione: TLabel;   // la tua posizione
    MemoStoria: TMemo;      // tutti i tuoi tentativi
    Timer1: TTimer;         // ogni 3 secondi chiede la classifica
    procedure FormCreate(Sender: TObject);
    procedure BtnConnettiClick(Sender: TObject);
    procedure BtnProvaClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    Cl: TMMClient;                 // il "postino": parla con il server
    UltimoTentativo: String;       // le cifre appena inviate
    InAttesa: Boolean;             // True se stiamo aspettando una risposta
    procedure RispostaConnessione(Sender: TObject);
    procedure RispostaTentativo(Sender: TObject);
    procedure RispostaClassifica(Sender: TObject);
    procedure AggiornaClassifica;  // scrive migliore, peggiore e posizione
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ Parte quando si apre il programma }
procedure TForm1.FormCreate(Sender: TObject);
begin
  Cl := TMMClient.Create;
  Cl.Modo := moRete;              // useremo la rete (TCP)
  InAttesa := False;
  BtnProva.Enabled := False;      // si accende solo dopo "Connetti"
  Timer1.Enabled := False;        // parte solo dopo "Connetti"
  LblStato.Caption := 'Non collegato. Scrivi il tuo nome e premi Connetti.';
  LblEsito.Caption := '';
  LblClassifica.Caption := 'Classifica: appare dopo Connetti';
  LblPosizione.Caption := '';
end;

{ Passo 2: il bottone Connetti }
procedure TForm1.BtnConnettiClick(Sender: TObject);
var
  testo: String;
  k: Integer;
begin
  if PulisciNome(EdNome.Text) = '' then
  begin
    LblStato.Caption := 'Scrivi prima il tuo nome!';
    Exit;
  end;
  // l'indirizzo e' del tipo  IP:PORTA  (se manca la porta usiamo 5050)
  testo := Trim(EdServer.Text);
  k := Pos(':', testo);
  if k = 0 then
  begin
    Cl.Host := testo;
    Cl.Porta := 5050;
  end
  else
  begin
    Cl.Host := Trim(Copy(testo, 1, k - 1));
    Cl.Porta := StrToIntDef(Trim(Copy(testo, k + 1, 10)), 5050);
  end;
  Cl.Nome := EdNome.Text;
  LblStato.Caption := 'Mi collego al server...';
  BtnConnetti.Enabled := False;
  // la domanda parte in un THREAD (un aiutante): la finestra non si blocca
  TMMRichiestaAsync.Create(Cl.Host, Cl.Porta, Cl.RigaStato, @RispostaConnessione);
end;

{ Il server ha risposto alla domanda "ci sei?" }
procedure TForm1.RispostaConnessione(Sender: TObject);
var
  R: TRisposta;
begin
  R := Cl.ApplicaRisposta(TMMRichiestaAsync(Sender).Risposta);
  if R.Tipo = 'STATO' then
  begin
    LblStato.Caption := 'Collegato come ' + PulisciNome(EdNome.Text) + '!  Giochiamo.';
    EdNome.Enabled := False;        // il nome non si cambia piu'
    EdServer.Enabled := False;
    BtnProva.Enabled := True;
    Timer1.Enabled := True;
    AggiornaClassifica;
  end
  else
  begin
    LblStato.Caption := 'Non trovo il server. Controlla l''indirizzo e riprova.';
    BtnConnetti.Enabled := True;     // si puo' riprovare, nessun problema!
  end;
end;

{ Passo 3: il bottone Prova }
procedure TForm1.BtnProvaClick(Sender: TObject);
begin
  if InAttesa then Exit;                  // un tentativo alla volta
  UltimoTentativo := Trim(EdTentativo.Text);
  if not CodiceValido(UltimoTentativo) then
  begin
    LblEsito.Caption := 'Scrivi 4 cifre, ognuna da 1 a 6 (per esempio 1234)';
    Exit;
  end;
  InAttesa := True;
  LblEsito.Caption := 'Invio al server...';
  TMMRichiestaAsync.Create(Cl.Host, Cl.Porta, Cl.RigaProva(UltimoTentativo), @RispostaTentativo);
end;

{ Il server ha risposto al tentativo }
procedure TForm1.RispostaTentativo(Sender: TObject);
var
  R: TRisposta;
begin
  InAttesa := False;
  R := Cl.ApplicaRisposta(TMMRichiestaAsync(Sender).Risposta);
  LblEsito.Caption := Cl.TestoRisposta(R);        // per esempio "Esatte: 1  Spostate: 2"
  if (R.Tipo = 'RESULT') or (R.Tipo = 'WIN') then
  begin
    MemoStoria.Lines.Add(IntToStr(R.Sintesi.Tentativi) + ')  ' + UltimoTentativo +
      '   esatte: ' + IntToStr(R.Esatte) + '   spostate: ' + IntToStr(R.Spostate));
    EdTentativo.Clear;
  end;
  if R.Tipo = 'WIN' then
  begin
    MemoStoria.Lines.Add('*** INDOVINATO! ***');
    BtnProva.Enabled := False;                     // hai finito, ora guardi la classifica
  end;
  AggiornaClassifica;
end;

{ Ogni 3 secondi: chiedo solo la classifica (nessun tentativo) }
procedure TForm1.Timer1Timer(Sender: TObject);
begin
  TMMRichiestaAsync.Create(Cl.Host, Cl.Porta, Cl.RigaStato, @RispostaClassifica);
end;

procedure TForm1.RispostaClassifica(Sender: TObject);
begin
  Cl.ApplicaRisposta(TMMRichiestaAsync(Sender).Risposta);
  AggiornaClassifica;
end;

{ Scrive nelle due etichette cio' che il server ci ha detto }
procedure TForm1.AggiornaClassifica;
begin
  LblClassifica.Caption := Cl.Console;
  if Cl.Ultima.Posizione > 0 then
    LblPosizione.Caption := 'La tua posizione: ' + IntToStr(Cl.Ultima.Posizione) +
      ' su ' + IntToStr(Cl.Ultima.Totale)
  else
    LblPosizione.Caption := 'La tua posizione: non hai ancora indovinato';
end;

end.
