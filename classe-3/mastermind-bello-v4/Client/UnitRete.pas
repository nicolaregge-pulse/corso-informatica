unit UnitRete;
{ MASTERMIND BELLO v4.0 - la UNIT DELLA RETE.
  Qui dentro c'e' TUTTO quello che parla con il server e NIENTE che parla con lo schermo:
  nessuna finestra, nessun bottone, nessun disegno (guarda l'elenco "uses": non c'e' Forms).
  Come parla la rete: una riga che va, una riga che torna. Le righe sono fatte di campi
  separati da punto e virgola. Il protocollo (porta 5050) e' quello di sempre:

    il client scrive            il server risponde
    ------------------------    ----------------------------------------------------------
    STATO;nome                  STATO;GIOCO;tent;posto;finiti;migliore;peggiore
                                STATO;ATTESA;tent;posto;finiti;migliore;peggiore
    GUESS;nome;1234             WAIT                                   (il Prof non ha detto Via)
                                RESULT;neri;bianchi;tent;posto;finiti;migliore;peggiore
                                WIN;nome;tent;secondi;posto;finiti;migliore;peggiore
                                ERR;motivo

  Come avvisa la finestra, senza conoscerla: con gli EVENTI, proprio come l'evento OnClick di un
  bottone in Lazarus. Qui sotto trovi i "tipi evento" (procedure ... of object). La finestra
  (UnitInterfaccia) scrive le sue procedure e le attacca agli eventi: Rete.OnRisultato := @MioRisultato.
  Cosi' UnitInterfaccia conosce UnitRete, ma UnitRete NON conosce UnitInterfaccia:
  niente giri in tondo (riferimenti circolari). }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, sockets, ssockets;

const
  PORTA_SERVER = 5050;      // la porta del server: non toccarla
  TEMPO_MS = 2000;          // dopo 2 secondi senza risposta ci arrendiamo

type
  { i numeri della classifica, che il server scrive in fondo a quasi ogni risposta }
  TClassifica = record
    Tentativi: Integer;     // quanti tentativi hai fatto tu
    Posto: Integer;         // il tuo posto (0 = non hai ancora finito)
    Finiti: Integer;        // quanti hanno gia' indovinato
    Migliore: Integer;      // il minor numero di tentativi (0 = nessuno ha finito)
    Peggiore: Integer;      // il maggior numero di tentativi
  end;

  { i tipi evento: come TNotifyEvent (l'evento click), ma con le informazioni che servono }
  TEventoErrore = procedure(Sender: TObject; const Motivo: String) of object;
  TEventoStato = procedure(Sender: TObject; InGioco: Boolean; const Cl: TClassifica) of object;
  TEventoRisultato = procedure(Sender: TObject; Neri, Bianchi: Integer; const Cl: TClassifica) of object;
  TEventoVittoria = procedure(Sender: TObject; Tentativi, Secondi: Integer; const Cl: TClassifica) of object;

  TClienteRete = class
  private
    FOnErrore: TEventoErrore;
    FOnRifiuto: TEventoErrore;
    FOnStato: TEventoStato;
    FOnAttesa: TNotifyEvent;
    FOnRisultato: TEventoRisultato;
    FOnVittoria: TEventoVittoria;
    procedure DaiErrore(const Motivo: String);
    function LeggiClassifica(const R: String; Primo: Integer): TClassifica;
  public
    Indirizzo: String;      // l'IP del PC del Prof (si puo' scrivere anche 192.168.1.5:5050)
    Nome: String;           // il tuo nome, senza punto e virgola
    { il testo semplice: una riga va, una riga torna. Risultato '' = tutto bene, altrimenti il
      motivo dell'errore in parole semplici. }
    function Chiedi(const Riga: String; out Risposta: String): String;
    { le due frasi che il client sa dire al server }
    function RigaStato: String;
    function RigaGuess(const Codice: String): String;
    { il cuore del protocollo: legge UNA riga arrivata dal server e fa partire l'evento giusto }
    procedure Elabora(const Riga: String);
    { chiede lo stato; True se il server ha risposto davvero STATO;... }
    function ChiediStato: Boolean;
    { manda un tentativo (4 cifre da 1 a 6): l'esito arriva con gli eventi }
    procedure InviaTentativo(const Codice: String);
    { gli eventi: la finestra ci attacca le sue procedure }
    property OnErrore: TEventoErrore read FOnErrore write FOnErrore;         // la rete non va
    property OnRifiuto: TEventoErrore read FOnRifiuto write FOnRifiuto;      // il server ha risposto ERR;...
    property OnStato: TEventoStato read FOnStato write FOnStato;             // e' arrivato STATO;...
    property OnAttesa: TNotifyEvent read FOnAttesa write FOnAttesa;          // e' arrivato WAIT
    property OnRisultato: TEventoRisultato read FOnRisultato write FOnRisultato;  // e' arrivato RESULT;...
    property OnVittoria: TEventoVittoria read FOnVittoria write FOnVittoria;      // e' arrivato WIN;...
  end;

{ il N-esimo campo di una riga separata da punto e virgola (il primo e' il numero 0) }
function Campo(const S: String; N: Integer): String;

implementation

function Campo(const S: String; N: Integer): String;
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

procedure TClienteRete.DaiErrore(const Motivo: String);
begin
  if Assigned(FOnErrore) then FOnErrore(Self, Motivo);
end;

{ legge i 5 campi della classifica a partire dal campo numero Primo }
function TClienteRete.LeggiClassifica(const R: String; Primo: Integer): TClassifica;
begin
  Result.Tentativi := StrToIntDef(Campo(R, Primo), 0);
  Result.Posto := StrToIntDef(Campo(R, Primo + 1), 0);
  Result.Finiti := StrToIntDef(Campo(R, Primo + 2), 0);
  Result.Migliore := StrToIntDef(Campo(R, Primo + 3), 0);
  Result.Peggiore := StrToIntDef(Campo(R, Primo + 4), 0);
end;

function TClienteRete.RigaStato: String;
begin
  Result := 'STATO;' + Nome;
end;

function TClienteRete.RigaGuess(const Codice: String): String;
begin
  Result := 'GUESS;' + Nome + ';' + Codice;
end;

{ Manda UNA riga al server e legge UNA riga. Ti colleghi, scrivi, leggi, chiudi. }
function TClienteRete.Chiedi(const Riga: String; out Risposta: String): String;
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
  Host := Trim(Indirizzo);
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
      Buf := Riga + #10;                       // la riga finisce sempre con "a capo" (#10)
      S.WriteBuffer(Buf[1], Length(Buf));
      Fine := GetTickCount64 + TEMPO_MS;
      repeat
        N := S.Read(Ch, 1);                    // si legge un carattere alla volta
        if N <= 0 then Break;
        if Ch = #10 then Break;                // "a capo": la riga e' finita
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

{ Il parser: il primo campo dice che tipo di risposta e', gli altri sono i dati.
  Posizioni dei campi (il primo e' lo 0):
    STATO   0 STATO   1 GIOCO/ATTESA  2 tentativi  3 posto  4 finiti  5 migliore  6 peggiore
    RESULT  0 RESULT  1 neri  2 bianchi  3 tentativi  4 posto  5 finiti  6 migliore  7 peggiore
    WIN     0 WIN  1 nome  2 tentativi  3 secondi  4 posto  5 finiti  6 migliore  7 peggiore
    WAIT    0 WAIT
    ERR     0 ERR  1 motivo }
procedure TClienteRete.Elabora(const Riga: String);
var
  Tipo: String;
  Cl: TClassifica;
begin
  Tipo := Campo(Riga, 0);
  if Tipo = 'STATO' then
  begin
    if Assigned(FOnStato) then FOnStato(Self, Campo(Riga, 1) = 'GIOCO', LeggiClassifica(Riga, 2));
  end
  else if Tipo = 'WAIT' then
  begin
    if Assigned(FOnAttesa) then FOnAttesa(Self);
  end
  else if Tipo = 'RESULT' then
  begin
    if Assigned(FOnRisultato) then
      FOnRisultato(Self, StrToIntDef(Campo(Riga, 1), 0), StrToIntDef(Campo(Riga, 2), 0),
        LeggiClassifica(Riga, 3));
  end
  else if Tipo = 'WIN' then
  begin
    // WIN ha in piu' i secondi: la classifica comincia un campo dopo e i tentativi si leggono a parte
    Cl := LeggiClassifica(Riga, 3);
    Cl.Tentativi := StrToIntDef(Campo(Riga, 2), 0);
    if Assigned(FOnVittoria) then FOnVittoria(Self, Cl.Tentativi, StrToIntDef(Campo(Riga, 3), 0), Cl);
  end
  else if Tipo = 'ERR' then
  begin
    if Assigned(FOnRifiuto) then FOnRifiuto(Self, Campo(Riga, 1));
  end
  else
    DaiErrore('Risposta strana dal server: ' + Riga);
end;

function TClienteRete.ChiediStato: Boolean;
var
  R, Err: String;
begin
  Result := False;
  Err := Chiedi(RigaStato, R);
  if Err <> '' then
  begin
    DaiErrore(Err);
    Exit;
  end;
  if Campo(R, 0) <> 'STATO' then
  begin
    DaiErrore('Risposta strana dal server: ' + R);
    Exit;
  end;
  Result := True;
  Elabora(R);
end;

procedure TClienteRete.InviaTentativo(const Codice: String);
var
  R, Err: String;
begin
  Err := Chiedi(RigaGuess(Codice), R);
  if Err <> '' then
    DaiErrore(Err)
  else
    Elabora(R);
end;

end.
