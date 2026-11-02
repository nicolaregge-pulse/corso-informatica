unit mm_tcp_poll;
{ MASTERMIND 2.0 - SERVER CON FINESTRA: la RETE senza thread.
  Come mm_tcp.pas usa SOLO ssockets (dentro Free Pascal/Lazarus), ma qui NON c'e'
  nessun thread: la finestra chiama Tick ogni 50 millisecondi (e' il Timer1).
  Ad ogni Tick il server guarda se c'e' qualcuno che bussa, risponde (una riga per
  ogni richiesta, come in protocollo.md) e restituisce subito il controllo alla
  finestra. Cosi' la finestra non si blocca mai e non servono thread.
  Dentro un Tick si servono al massimo 12 connessioni: con 22 ragazzi che
  chiamano ogni 3 secondi bastano e avanzano.
  In piu': MMIpDelPc ricava l'IP del PC con la sola unita' "sockets". }

{$mode objfpc}{$H+}

interface

uses
  SysUtils, Classes, sockets, ssockets, mm_logica;

type
  { Avvisa la finestra di ogni richiesta arrivata: chi (IP), che cosa ha chiesto, che cosa ha risposto }
  TMMRichiestaEvent = procedure(const Ip, Linea, Risposta: String) of object;

  TMMTcpServerPoll = class
  private
    FServer: TInetServer;
    FTabella: TMMTabella;
    FPorta: Word;
    FServite: Integer;
    FOnRichiesta: TMMRichiestaEvent;
    procedure Connesso(Sender: TObject; Data: TSocketStream);
    procedure Inattivo(Sender: TObject);
  public
    Errore: String;          // se non riesce ad aprire la porta
    Pronto: Boolean;         // True quando sta ascoltando
    MaxPerTick: Integer;     // connessioni servite al massimo ad ogni Tick
    constructor Create(ATabella: TMMTabella; APorta: Word);
    destructor Destroy; override;
    function Avvia: Boolean;       // apre la porta; False (e Errore) se e' occupata o bloccata
    procedure Tick;                // da chiamare ogni 50 ms dal Timer
    procedure Ferma;
    property OnRichiesta: TMMRichiestaEvent read FOnRichiesta write FOnRichiesta;
  end;

{ IP del PC nella rete locale (per esempio 192.168.10.5), oppure '' se non si ricava }
function MMIpDelPc: String;

implementation

constructor TMMTcpServerPoll.Create(ATabella: TMMTabella; APorta: Word);
begin
  inherited Create;
  FTabella := ATabella;
  FPorta := APorta;
  MaxPerTick := 12;
end;

destructor TMMTcpServerPoll.Destroy;
begin
  Ferma;
  inherited Destroy;
end;

function TMMTcpServerPoll.Avvia: Boolean;
begin
  Result := False;
  Errore := '';
  Pronto := False;
  Ferma;
  try
    FServer := TInetServer.Create('0.0.0.0', FPorta);
    {$ifdef unix}FServer.ReuseAddress := True;{$endif}
    FServer.QueueSize := 64;            // 22 client che bussano insieme restano in coda
    FServer.AcceptIdleTimeout := 1;     // un giro di accettazione dura al massimo ~1 ms
    FServer.OnConnect := @Connesso;
    FServer.OnIdle := @Inattivo;
    FServer.Listen;                     // qui si scopre se la porta e' occupata
    Pronto := True;
    Result := True;
  except
    on E: Exception do
    begin
      Errore := E.Message;
      Pronto := False;
      FreeAndNil(FServer);
    end;
  end;
end;

procedure TMMTcpServerPoll.Ferma;
begin
  Pronto := False;
  FreeAndNil(FServer);
end;

procedure TMMTcpServerPoll.Tick;
begin
  if (FServer = nil) or not Pronto then Exit;
  FServite := 0;
  try
    FServer.StartAccepting;     // torna indietro da solo: Inattivo (o il limite) lo ferma
  except
    on E: Exception do Errore := E.Message;   // un errore di rete non deve rompere la finestra
  end;
end;

procedure TMMTcpServerPoll.Inattivo(Sender: TObject);
begin
  FServer.StopAccepting;        // nessuno bussa: torniamo alla finestra
end;

procedure TMMTcpServerPoll.Connesso(Sender: TObject; Data: TSocketStream);
var
  c: Char;
  n: Integer;
  linea, risp, ip: String;
begin
  Inc(FServite);
  if FServite >= MaxPerTick then FServer.StopAccepting;   // gli altri al prossimo Tick
  try
    try
      Data.IOTimeout := 500;            // un client muto fa aspettare la finestra al massimo mezzo secondo
      linea := '';
      repeat
        n := Data.Read(c, 1);
        if (n = 1) and (c <> #10) and (c <> #13) then linea := linea + c;
      until (n <= 0) or (c = #10) or (Length(linea) > 200);
      if linea <> '' then
      begin
        ip := NetAddrToStr(Data.RemoteAddress.sin_addr);
        FTabella.Blocca;
        try
          risp := FTabella.Gestisci(linea, ip);
        finally
          FTabella.Sblocca;
        end;
        if Assigned(FOnRichiesta) then FOnRichiesta(ip, linea, risp);
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

{ Si "prepara" una telefonata UDP verso un indirizzo qualunque: NON parte nessun
  pacchetto, ma il sistema sceglie la scheda di rete giusta e noi leggiamo il
  suo indirizzo. Funziona uguale su Windows e Linux con la sola unita' sockets. }
function IpVerso(const Destinazione: String): String;
var
  s: TSocket;
  a, b: TInetSockAddr;
  l: TSockLen;
begin
  Result := '';
  s := fpSocket(AF_INET, SOCK_DGRAM, 0);
  if s < 0 then Exit;
  try
    FillChar(a, SizeOf(a), 0);
    a.sin_family := AF_INET;
    a.sin_port := htons(53);
    a.sin_addr := StrToNetAddr(Destinazione);
    if fpConnect(s, @a, SizeOf(a)) <> 0 then Exit;
    FillChar(b, SizeOf(b), 0);
    l := SizeOf(b);
    if fpGetSockName(s, @b, @l) <> 0 then Exit;
    Result := NetAddrToStr(b.sin_addr);
    if (Result = '0.0.0.0') or (Copy(Result, 1, 4) = '127.') then Result := '';
  finally
    CloseSocket(s);
  end;
end;

function MMIpDelPc: String;
begin
  Result := IpVerso('8.8.8.8');                       // rete con uscita su Internet
  if Result = '' then Result := IpVerso('192.168.0.1');   // rete di classe senza Internet
  if Result = '' then Result := IpVerso('10.0.0.1');
  if Result = '' then Result := IpVerso('172.16.0.1');
end;

end.
