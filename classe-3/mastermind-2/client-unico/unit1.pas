unit Unit1;
{ MASTERMIND 2.0 - CLIENT (per i ragazzi), TUTTO IN UN FILE.
  Ti collegi al PC del prof, quando il prof dice "Via" provi le combinazioni.
  Ogni richiesta: ti colleghi, mandi UNA riga, leggi UNA riga, chiudi. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  sockets, ssockets;

type
  TForm1 = class(TForm)
    LblIp: TLabel;
    EdIp: TEdit;
    LblNome: TLabel;
    EdNome: TEdit;
    BtnConnetti: TButton;
    LblEsito: TLabel;
    LblStato: TLabel;
    LblTentativo: TLabel;
    EdTentativo: TEdit;
    BtnProva: TButton;
    MemoStoria: TMemo;
    LblMigliore: TLabel;
    LblPeggiore: TLabel;
    LblPosizione: TLabel;
    LblFiniti: TLabel;
    Timer1: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure BtnConnettiClick(Sender: TObject);
    procedure BtnProvaClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    Collegato: Boolean;
    Errori: Integer;
    Nome: String;
    function PulisciNome: String;
    function Chiedi(const Riga: String; out Risposta: String): String;
    function Campo(const S: String; N: Integer): String;
    procedure Mostra(const R: String; Dopo: Integer);
  public
    Avviato: Boolean;                 // True quando FormCreate e' gia' partita
    procedure AfterConstruction; override;
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

const
  PORTA_SERVER = 5050;      // la porta del server: non toccarla
  TEMPO_MS = 2000;   // dopo 2 secondi senza risposta ci arrendiamo

procedure TForm1.FormCreate(Sender: TObject);
begin
  Avviato := True;
  Collegato := False;
  Errori := 0;
  Timer1.Enabled := False;
  Timer1.Interval := 3000;
  BtnProva.Enabled := False;
  LblStato.Caption := 'Non collegato';
  LblEsito.Caption := 'Scrivi il tuo nome e premi Connetti.';
end;

{ Se Lazarus non ha collegato i bottoni, li colleghiamo noi da qui }
procedure TForm1.AfterConstruction;
begin
  inherited AfterConstruction;
  if not Assigned(BtnConnetti.OnClick) then BtnConnetti.OnClick := @BtnConnettiClick;
  if not Assigned(BtnProva.OnClick) then BtnProva.OnClick := @BtnProvaClick;
  if not Assigned(Timer1.OnTimer) then Timer1.OnTimer := @Timer1Timer;
  if not Avviato then FormCreate(nil);
end;

{ il quarto, il terzo... campo di una riga separata da punto e virgola }
function TForm1.Campo(const S: String; N: Integer): String;
var
  L: TStringList;
begin
  Result := '';
  L := TStringList.Create;
  try
    L.StrictDelimiter := True;
    L.Delimiter := ';';
    L.DelimitedText := S;
    if (N >= 0) and (N < L.Count) then Result := Trim(L[N]);
  finally
    L.Free;
  end;
end;

function TForm1.PulisciNome: String;
begin
  Result := Trim(StringReplace(EdNome.Text, ';', '', [rfReplaceAll]));
end;

{ Manda UNA riga al server e legge UNA riga. Risultato: '' se tutto bene,
  altrimenti il motivo dell'errore in parole semplici. }
function TForm1.Chiedi(const Riga: String; out Risposta: String): String;
var
  S: TInetSocket;
  Ch: Char;
  N: Integer;
  Fine: QWord;
  Buf, Host: String;
  Porta, K: Integer;
begin
  Result := '';
  Risposta := '';
  S := nil;
  // se qualcuno scrive anche ":5050" dopo l'IP, va bene lo stesso
  Host := Trim(EdIp.Text);
  Porta := PORTA_SERVER;
  K := Pos(':', Host);
  if K > 0 then
  begin
    Porta := StrToIntDef(Trim(Copy(Host, K + 1, 10)), PORTA_SERVER);
    Host := Trim(Copy(Host, 1, K - 1));
  end;
  try
    try
      S := TInetSocket.Create(Host, Porta, TEMPO_MS);
      S.IOTimeout := TEMPO_MS;
      Buf := Riga + #10;
      S.WriteBuffer(Buf[1], Length(Buf));
      Fine := GetTickCount64 + TEMPO_MS;
      repeat
        N := S.Read(Ch, 1);
        if N <= 0 then Break;
        if Ch = #10 then Break;
        if Ch <> #13 then Risposta := Risposta + Ch;
      until GetTickCount64 > Fine;
      if Risposta = '' then Result := 'Il server non ha risposto. Riprova tra un attimo.';
    except
      on E: ESocketError do
        case E.Code of
          seConnectFailed:
            Result := 'Connessione rifiutata: il server non e'' acceso oppure la porta e'' sbagliata.';
          seConnectTimeOut, seIOTimeOut:
            Result := 'Il server non risponde: controlla l''IP (deve essere quello scritto in alto nella pagina) e il firewall.';
          seHostNotFound:
            Result := 'L''IP non e'' scritto bene: deve avere 4 numeri separati da punti.';
        else
          Result := 'Non riesco a collegarmi: controlla l''IP e che il server sia acceso.';
        end;
      on E: Exception do
        Result := 'Non riesco a collegarmi: controlla l''IP e che il server sia acceso.';
    end;
  finally
    S.Free;
  end;
end;

{ Aggiorna le scritte grandi. Dopo = posizione del campo "tentativi" nella risposta }
procedure TForm1.Mostra(const R: String; Dopo: Integer);
var
  Mig, Peg, Pos_, Tot: String;
begin
  Pos_ := Campo(R, Dopo + 1);
  Tot := Campo(R, Dopo + 2);
  Mig := Campo(R, Dopo + 3);
  Peg := Campo(R, Dopo + 4);
  if Mig = '0' then LblMigliore.Caption := 'Migliore: nessuno ha ancora finito'
  else LblMigliore.Caption := 'Migliore: ' + Mig + ' tentativi';
  if Peg = '0' then LblPeggiore.Caption := 'Peggiore: -'
  else LblPeggiore.Caption := 'Peggiore: ' + Peg + ' tentativi';
  if (Pos_ = '0') or (Pos_ = '') then LblPosizione.Caption := 'Il tuo posto: non hai ancora indovinato'
  else LblPosizione.Caption := 'Il tuo posto: ' + Pos_ + 'o';
  LblFiniti.Caption := 'Hanno finito: ' + Tot;
end;

procedure TForm1.BtnConnettiClick(Sender: TObject);
var
  R, Err: String;
begin
  Nome := PulisciNome;
  if Nome = '' then
  begin
    LblEsito.Caption := 'Scrivi prima il tuo nome nella casella.';
    Exit;
  end;
  if Trim(EdIp.Text) = '' then
  begin
    LblEsito.Caption := 'Scrivi l''IP del server (e'' scritto in alto nella pagina).';
    Exit;
  end;
  LblEsito.Caption := 'Mi collego...';
  Err := Chiedi('STATO;' + Nome, R);
  if (Err = '') and (Campo(R, 0) <> 'STATO') then
    Err := 'Risposta strana dal server: ' + R;
  if Err <> '' then
  begin
    Collegato := False;
    Timer1.Enabled := False;
    BtnProva.Enabled := False;
    LblStato.Caption := 'Non collegato';
    LblEsito.Caption := Err;
    Exit;
  end;
  Collegato := True;
  Errori := 0;
  BtnProva.Enabled := True;
  LblEsito.Caption := 'Collegato! Ciao ' + Nome + '.';
  Mostra(R, 2);
  if Campo(R, 1) = 'GIOCO' then LblStato.Caption := 'GIOCO: provaci!'
  else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  Timer1.Enabled := True;
end;

procedure TForm1.BtnProvaClick(Sender: TObject);
var
  R, Err, Cod, T: String;
  I: Integer;
  Ok: Boolean;
begin
  if not Collegato then
  begin
    LblEsito.Caption := 'Prima premi Connetti.';
    Exit;
  end;
  Cod := Trim(EdTentativo.Text);
  Ok := Length(Cod) = 4;
  for I := 1 to Length(Cod) do
    if not (Cod[I] in ['1'..'6']) then Ok := False;
  if not Ok then
  begin
    LblEsito.Caption := 'Servono 4 cifre, ognuna da 1 a 6 (esempio: 1234).';
    Exit;
  end;
  Err := Chiedi('GUESS;' + Nome + ';' + Cod, R);
  if Err <> '' then
  begin
    LblEsito.Caption := Err;
    Exit;
  end;
  T := Campo(R, 0);
  if T = 'WAIT' then
  begin
    LblEsito.Caption := 'Il Prof non ha ancora detto Via: aspetta.';
    LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  end
  else if T = 'RESULT' then
  begin
    LblStato.Caption := 'GIOCO: provaci!';
    LblEsito.Caption := Cod + ': ' + Campo(R, 1) + ' esatte, ' + Campo(R, 2) + ' spostate';
    MemoStoria.Lines.Add('n. ' + Campo(R, 3) + '   ' + Cod + '   esatte ' + Campo(R, 1) +
      '   spostate ' + Campo(R, 2));
    Mostra(R, 3);
    EdTentativo.Text := '';
  end
  else if T = 'WIN' then
  begin
    LblStato.Caption := 'HAI VINTO!';
    LblEsito.Caption := 'BRAVO! Hai indovinato in ' + Campo(R, 2) + ' tentativi e ' +
      Campo(R, 3) + ' secondi.';
    MemoStoria.Lines.Add('n. ' + Campo(R, 2) + '   ' + Cod + '   INDOVINATO!  Posto ' + Campo(R, 4));
    Mostra(R, 3);
    BtnProva.Enabled := False;
  end
  else if T = 'ERR' then
    LblEsito.Caption := 'Il server dice: ' + Campo(R, 1)
  else
    LblEsito.Caption := 'Risposta strana dal server: ' + R;
end;

{ ogni 3 secondi chiede al server come siamo messi }
procedure TForm1.Timer1Timer(Sender: TObject);
var
  R, Err: String;
begin
  if not Collegato then Exit;
  Err := Chiedi('STATO;' + Nome, R);
  if Err <> '' then
  begin
    Inc(Errori);
    LblEsito.Caption := Err;
    if Errori >= 3 then
    begin
      Collegato := False;
      Timer1.Enabled := False;
      BtnProva.Enabled := False;
      LblStato.Caption := 'Non collegato';
      LblEsito.Caption := 'Il server non risponde piu'': premi Connetti per riprovare.';
    end;
    Exit;
  end;
  Errori := 0;
  if Campo(R, 0) <> 'STATO' then Exit;
  Mostra(R, 2);
  if (LblStato.Caption = 'HAI VINTO!') and (Campo(R, 3) = '0') then
  begin
    // il Prof ha ricominciato con un'altra combinazione
    MemoStoria.Lines.Clear;
    BtnProva.Enabled := True;
    LblStato.Caption := '';
  end;
  if LblStato.Caption <> 'HAI VINTO!' then
    if Campo(R, 1) = 'GIOCO' then LblStato.Caption := 'GIOCO: provaci!'
    else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
end;

end.
