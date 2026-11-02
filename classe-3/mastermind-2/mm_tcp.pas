unit mm_tcp;
{ MASTERMIND 2.0 - TRASPORTO A: RETE (TCP) - modo VELOCE e facoltativo.
  Usa SOLO ssockets, che e' dentro Free Pascal/Lazarus (niente pacchetti da
  installare, niente lNet, niente Indy).
  Ogni richiesta = una connessione: si manda UNA riga, si legge UNA riga, si chiude.
  Il server gira in un THREAD, cosi' la finestra non si blocca. }

{$mode objfpc}{$H+}

interface

uses
  SysUtils, Classes, sockets, ssockets, mm_logica;

type
  { SERVER: ascolta sulla porta e risponde con Tabella.Gestisci }
  TMMTcpServerThread = class(TThread)
  private
    FServer: TInetServer;
    FTabella: TMMTabella;
    FPorta: Word;
    procedure Connesso(Sender: TObject; Data: TSocketStream);
    procedure Inattivo(Sender: TObject);
  protected
    procedure Execute; override;
  public
    Errore: String;          // se non riesce ad aprire la porta
    Pronto: Boolean;         // True quando sta ascoltando
    constructor Create(ATabella: TMMTabella; APorta: Word);
  end;

{ CLIENT: manda una riga, restituisce la risposta. In caso di problemi: 'ERR;...' }
function MMTcpRichiesta(const Host: String; Porta: Word; const Linea: String;
  TimeoutMs: Integer = 3000): String;

type
  { Richiesta in un thread a parte: la finestra non si blocca mai.
    Si crea, e quando ha finito chiama AlFinire (nel thread principale). }
  TMMRichiestaAsync = class(TThread)
  private
    FHost: String;
    FPorta: Word;
    FLinea: String;
    FAlFinire: TNotifyEvent;
    procedure Fine;
  protected
    procedure Execute; override;
  public
    Risposta: String;
    constructor Create(const AHost: String; APorta: Word; const ALinea: String;
      AlFinire: TNotifyEvent);
  end;

implementation

{ ---- server ---- }

constructor TMMTcpServerThread.Create(ATabella: TMMTabella; APorta: Word);
begin
  FTabella := ATabella;
  FPorta := APorta;
  FreeOnTerminate := False;
  inherited Create(False);
end;

procedure TMMTcpServerThread.Connesso(Sender: TObject; Data: TSocketStream);
var
  c: Char;
  n: Integer;
  linea, risp: String;
begin
  try
    try
      Data.IOTimeout := 2000;           // un client muto non blocca il server
      linea := '';
      repeat
        n := Data.Read(c, 1);
        if (n = 1) and (c <> #10) and (c <> #13) then linea := linea + c;
      until (n <= 0) or (c = #10) or (Length(linea) > 200);
      if linea <> '' then
      begin
        FTabella.Blocca;
        try
          risp := FTabella.Gestisci(linea, NetAddrToStr(Data.RemoteAddress.sin_addr));
        finally
          FTabella.Sblocca;
        end;
        risp := risp + #10;
        Data.WriteBuffer(risp[1], Length(risp));
      end;
    except
      on E: Exception do ;               // un client che sbaglia non deve fermare il server
    end;
  finally
    Data.Free;
  end;
end;

procedure TMMTcpServerThread.Inattivo(Sender: TObject);
begin
  if Terminated then FServer.StopAccepting;
end;

procedure TMMTcpServerThread.Execute;
begin
  Errore := '';
  FServer := nil;
  try
    FServer := TInetServer.Create('0.0.0.0', FPorta);
    {$ifdef unix}FServer.ReuseAddress := True;{$endif}   // riavvio veloce senza "porta occupata"
    FServer.AcceptIdleTimeout := 250;    // ogni 1/4 di secondo controlla se deve fermarsi
    FServer.OnConnect := @Connesso;
    FServer.OnIdle := @Inattivo;
    Pronto := True;
    FServer.StartAccepting;              // resta qui finche' non arriva StopAccepting
  except
    on E: Exception do
    begin
      Errore := E.Message;
      Pronto := False;
    end;
  end;
  FServer.Free;
end;

{ ---- client ---- }

function MMTcpRichiesta(const Host: String; Porta: Word; const Linea: String;
  TimeoutMs: Integer): String;
var
  S: TInetSocket;
  c: Char;
  n: Integer;
  riga: String;
begin
  Result := '';
  try
    S := TInetSocket.Create(Host, Porta, TimeoutMs);
    try
      S.IOTimeout := TimeoutMs;
      riga := Linea + #10;
      S.WriteBuffer(riga[1], Length(riga));
      repeat
        n := S.Read(c, 1);
        if (n = 1) and (c <> #10) and (c <> #13) then Result := Result + c;
      until (n <= 0) or (c = #10) or (Length(Result) > 300);
    finally
      S.Free;
    end;
    if Result = '' then Result := 'ERR;nessuna risposta dal server';
  except
    on E: Exception do
      Result := 'ERR;server non raggiungibile (' + E.Message + ')';
  end;
end;

constructor TMMRichiestaAsync.Create(const AHost: String; APorta: Word;
  const ALinea: String; AlFinire: TNotifyEvent);
begin
  FHost := AHost;
  FPorta := APorta;
  FLinea := ALinea;
  FAlFinire := AlFinire;
  FreeOnTerminate := True;
  inherited Create(False);
end;

procedure TMMRichiestaAsync.Fine;
begin
  if Assigned(FAlFinire) then FAlFinire(Self);
end;

procedure TMMRichiestaAsync.Execute;
begin
  Risposta := MMTcpRichiesta(FHost, FPorta, FLinea);
  Synchronize(@Fine);
end;

end.
