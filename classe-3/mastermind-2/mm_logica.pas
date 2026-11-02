unit mm_logica;
{ MASTERMIND 2.0 - LOGICA (nessuna finestra, nessuna rete).
  Qui c'e' il cervello: il codice segreto, il conteggio esatte/spostate,
  la tabella dei giocatori, la classifica e il "linguaggio" a righe di testo.
  Si puo' provare da solo, senza Lazarus e senza rete. }

{$mode objfpc}{$H+}

interface

uses
  SysUtils, Classes;

type
  TFase = (faAttesa, faGioco);
  TEsito = (esAttesa, esNonValido, esOk, esVinto, esGiaVinto);

  { Quello che serve alla "console" dello studente }
  TSintesi = record
    Tentativi: Integer;   // tentativi fatti da te
    Posizione: Integer;   // il tuo posto tra chi ha finito (0 = non hai ancora finito)
    Totale: Integer;      // quanti hanno finito
    Migliore: Integer;    // tentativi del migliore (0 = nessuno ha ancora finito)
    Peggiore: Integer;    // tentativi del peggiore tra chi ha finito
  end;

  { Una riga di risposta del server, gia' letta }
  TRisposta = record
    Tipo: String;         // RESULT, WIN, WAIT, STATO, ERR
    Esatte, Spostate: Integer;
    Secondi: Integer;     // solo per WIN
    Sintesi: TSintesi;
    Messaggio: String;    // testo dell'errore (ERR)
  end;

  TGiocatore = class
    Nome: String;
    Tentativi: Integer;
    Risolto: Boolean;
    Secondi: Integer;     // secondi dal "Via!" alla vittoria
  end;

  TFunzioneSecondi = function: Double;   // orologio (in secondi), sostituibile nei test

  TMMTabella = class
  private
    FGiocatori: TList;
    FSegreto: String;
    FSeme: Int64;
    FFase: TFase;
    FIdPartita: String;
    FViaOra: Double;
    FCS: TRTLCriticalSection;
    FNumPartite: Integer;
    function Cerca(const ANome: String): TGiocatore;
    function Crea(const ANome: String): TGiocatore;
    function PosizioneDi(G: TGiocatore): Integer;
    function GetCount: Integer;
    function GetGiocatore(I: Integer): TGiocatore;
  public
    Orologio: TFunzioneSecondi;
    IpNomi: TStringList;       // righe IP=NOME (da ip-nomi.txt), facoltativo
    procedure CaricaIpNomi(const Testo: String);   // righe  IP;NOME
    function NomePerIp(const Ip: String): String;
    function TestoPresenze: String;   // chi ha provato / chi no (in base a ip-nomi)
    procedure Blocca;      // il thread di rete e quello principale non si pestano i piedi
    procedure Sblocca;
    constructor Create;
    destructor Destroy; override;
    procedure NuovaPartita(ASeme: Int64 = -1);
    procedure Via;
    function Tentativo(const ANome, AGuess: String; ASecondiForzati: Integer;
      out Esatte, Spostate: Integer): TEsito;
    function SintesiDi(const ANome: String): TSintesi;
    function Gestisci(const Linea: String; const IpClient: String = ''): String;
    function TestoClassifica: String;      // per la console del docente
    function TestoRanking: String;         // contenuto di ranking.txt
    function TestoPartita: String;         // contenuto di partita.txt
    property Fase: TFase read FFase;
    property IdPartita: String read FIdPartita;
    property Segreto: String read FSegreto;
    property Seme: Int64 read FSeme;
    property Count: Integer read GetCount;
    property Giocatori[I: Integer]: TGiocatore read GetGiocatore;
  end;

{ Funzioni "pure" (usate anche dai client) }
function CodiceDaSeme(ASeme: Int64): String;
procedure Valuta(const Segreto, Tent: String; out Esatte, Spostate: Integer);
function CodiceValido(const S: String): Boolean;
function PulisciNome(const S: String): String;
function ParsaRisposta(const Linea: String; out R: TRisposta): Boolean;
function SintesiDaRanking(const Testo, ANome: String; out Fase: TFase;
  out Id: String; out Seme: Int64): TSintesi;
function TestoConsole(const S: TSintesi): String;
function SecondiOra: Double;
function Campo(const Linea: String; N: Integer): String;   // N parte da 1

implementation

function SecondiOra: Double;
begin
  Result := Now * 86400.0;
end;

{ Il campo numero N (da 1) di una riga separata da punti e virgola }
function Campo(const Linea: String; N: Integer): String;
var
  i, k, ini: Integer;
begin
  Result := '';
  k := 1;
  ini := 1;
  for i := 1 to Length(Linea) + 1 do
    if (i > Length(Linea)) or (Linea[i] = ';') then
    begin
      if k = N then
      begin
        Result := Copy(Linea, ini, i - ini);
        Exit;
      end;
      k := k + 1;
      ini := i + 1;
    end;
end;

{ Da un numero (seme) esce sempre lo stesso codice: cosi' server e client
  del piano B (file) possono avere lo stesso codice senza parlarsi. }
function CodiceDaSeme(ASeme: Int64): String;
var
  x: Int64;
  i: Integer;
begin
  x := ASeme and $7FFFFFFF;
  Result := '';
  for i := 1 to 4 do
  begin
    x := (x * 1103515245 + 12345) and $7FFFFFFF;
    Result := Result + IntToStr(((x shr 16) mod 6) + 1);
  end;
end;

{ Stessa logica del Mastermind normale: prima le esatte, poi le spostate }
procedure Valuta(const Segreto, Tent: String; out Esatte, Spostate: Integer);
var
  i, j: Integer;
  usataS, usataT: array[1..4] of Boolean;
begin
  for i := 1 to 4 do
  begin
    usataS[i] := False;
    usataT[i] := False;
  end;
  Esatte := 0;
  for i := 1 to 4 do
    if Tent[i] = Segreto[i] then
    begin
      Esatte := Esatte + 1;
      usataS[i] := True;
      usataT[i] := True;
    end;
  Spostate := 0;
  for i := 1 to 4 do
    if not usataT[i] then
      for j := 1 to 4 do
        if (not usataS[j]) and (Tent[i] = Segreto[j]) then
        begin
          Spostate := Spostate + 1;
          usataS[j] := True;
          Break;
        end;
end;

function CodiceValido(const S: String): Boolean;
var
  i: Integer;
begin
  Result := Length(S) = 4;
  if Result then
    for i := 1 to 4 do
      if not (S[i] in ['1'..'6']) then
        Result := False;
end;

{ Toglie ; e caratteri strani dal nome (il ; separa i campi!), max 20 }
function PulisciNome(const S: String): String;
var
  i: Integer;
begin
  Result := '';
  for i := 1 to Length(S) do
    if (S[i] >= ' ') and not (S[i] in [';', '/', '\', ':', '*', '?', '"', '<', '>', '|']) then
      Result := Result + S[i];
  Result := Trim(Result);
  if Length(Result) > 20 then
    Result := Trim(Copy(Result, 1, 20));
end;

function SIntero(const S: String; Pred: Integer = 0): Integer;
begin
  Result := StrToIntDef(Trim(S), Pred);
end;

{ ------------------------------------------------------------ tabella }

constructor TMMTabella.Create;
begin
  inherited Create;
  InitCriticalSection(FCS);
  IpNomi := TStringList.Create;
  FGiocatori := TList.Create;
  Orologio := @SecondiOra;
  NuovaPartita;
end;

destructor TMMTabella.Destroy;
var
  i: Integer;
begin
  for i := 0 to FGiocatori.Count - 1 do
    TGiocatore(FGiocatori[i]).Free;
  FGiocatori.Free;
  IpNomi.Free;
  DoneCriticalSection(FCS);
  inherited Destroy;
end;

procedure TMMTabella.Blocca;
begin
  EnterCriticalSection(FCS);
end;

procedure TMMTabella.Sblocca;
begin
  LeaveCriticalSection(FCS);
end;

function TMMTabella.GetCount: Integer;
begin
  Result := FGiocatori.Count;
end;

function TMMTabella.GetGiocatore(I: Integer): TGiocatore;
begin
  Result := TGiocatore(FGiocatori[I]);
end;

function TMMTabella.Cerca(const ANome: String): TGiocatore;
var
  i: Integer;
begin
  Result := nil;
  for i := 0 to FGiocatori.Count - 1 do
    if SameText(TGiocatore(FGiocatori[i]).Nome, ANome) then
    begin
      Result := TGiocatore(FGiocatori[i]);
      Exit;
    end;
end;

function TMMTabella.Crea(const ANome: String): TGiocatore;
begin
  Result := TGiocatore.Create;
  Result.Nome := ANome;
  FGiocatori.Add(Result);
end;

procedure TMMTabella.NuovaPartita(ASeme: Int64);
var
  i: Integer;
begin
  for i := 0 to FGiocatori.Count - 1 do
    TGiocatore(FGiocatori[i]).Free;
  FGiocatori.Clear;
  if ASeme < 0 then
  begin
    Randomize;
    ASeme := Random(2000000000) + 1;
  end;
  FSeme := ASeme;
  FSegreto := CodiceDaSeme(FSeme);
  FFase := faAttesa;
  FNumPartite := FNumPartite + 1;      // l'id NON deve dipendere dal seme (rivelerebbe il codice)
  FIdPartita := 'P' + IntToStr(FNumPartite) + 'x' + IntToStr(Trunc(Orologio()) mod 100000);
  FViaOra := 0;
end;

procedure TMMTabella.Via;
begin
  if FFase = faAttesa then
  begin
    FFase := faGioco;
    FViaOra := Orologio();
  end;
end;

{ Chi e' meglio di G? Meglio = piu' risolti, a parita' meno tentativi, poi meno secondi.
  La posizione e' 1 + il numero di chi ha finito ed e' STRETTAMENTE meglio.
  Pari tentativi e pari secondi = stessa posizione (parimerito). }
function TMMTabella.PosizioneDi(G: TGiocatore): Integer;
var
  i: Integer;
  H: TGiocatore;
begin
  Result := 0;
  if not G.Risolto then Exit;
  Result := 1;
  for i := 0 to FGiocatori.Count - 1 do
  begin
    H := TGiocatore(FGiocatori[i]);
    if H.Risolto and ((H.Tentativi < G.Tentativi) or
       ((H.Tentativi = G.Tentativi) and (H.Secondi < G.Secondi))) then
      Result := Result + 1;
  end;
end;

function TMMTabella.Tentativo(const ANome, AGuess: String; ASecondiForzati: Integer;
  out Esatte, Spostate: Integer): TEsito;
var
  G: TGiocatore;
  nome: String;
begin
  Esatte := 0;
  Spostate := 0;
  nome := PulisciNome(ANome);
  if (nome = '') or not CodiceValido(AGuess) then
  begin
    Result := esNonValido;
    Exit;
  end;
  if FFase = faAttesa then
  begin
    Result := esAttesa;
    Exit;
  end;
  G := Cerca(nome);
  if G = nil then G := Crea(nome);
  Valuta(FSegreto, AGuess, Esatte, Spostate);
  if G.Risolto then
  begin
    Result := esGiaVinto;     // non conta piu': il risultato resta quello di prima
    Exit;
  end;
  G.Tentativi := G.Tentativi + 1;
  if Esatte = 4 then
  begin
    G.Risolto := True;
    if ASecondiForzati >= 0 then
      G.Secondi := ASecondiForzati
    else
      G.Secondi := Round(Orologio() - FViaOra);
    Result := esVinto;
  end
  else
    Result := esOk;
end;

function TMMTabella.SintesiDi(const ANome: String): TSintesi;
var
  i: Integer;
  G, H: TGiocatore;
begin
  Result.Tentativi := 0;
  Result.Posizione := 0;
  Result.Totale := 0;
  Result.Migliore := 0;
  Result.Peggiore := 0;
  for i := 0 to FGiocatori.Count - 1 do
  begin
    H := TGiocatore(FGiocatori[i]);
    if H.Risolto then
    begin
      Result.Totale := Result.Totale + 1;
      if (Result.Migliore = 0) or (H.Tentativi < Result.Migliore) then
        Result.Migliore := H.Tentativi;
      if H.Tentativi > Result.Peggiore then
        Result.Peggiore := H.Tentativi;
    end;
  end;
  G := Cerca(PulisciNome(ANome));
  if G <> nil then
  begin
    Result.Tentativi := G.Tentativi;
    Result.Posizione := PosizioneDi(G);
  end;
end;

function SintesiTesto(const S: TSintesi): String;
begin
  Result := IntToStr(S.Tentativi) + ';' + IntToStr(S.Posizione) + ';' +
    IntToStr(S.Totale) + ';' + IntToStr(S.Migliore) + ';' + IntToStr(S.Peggiore);
end;

{ IL PROTOCOLLO A RIGHE (vedi protocollo.md). Riceve UNA riga, restituisce UNA riga. }
function TMMTabella.Gestisci(const Linea: String; const IpClient: String): String;
var
  cmd, nome, guess: String;
  esa, spo: Integer;
  S: TSintesi;
  G: TGiocatore;
begin
  cmd := UpperCase(Trim(Campo(Linea, 1)));
  nome := PulisciNome(Campo(Linea, 2));
  if (IpClient <> '') and (NomePerIp(IpClient) <> '') then
    nome := NomePerIp(IpClient);        // IP noto: vale il nome della tabella, non quello scritto dal client
  if cmd = 'GUESS' then
  begin
    guess := Trim(Campo(Linea, 3));
    case Tentativo(nome, guess, -1, esa, spo) of
      esAttesa: Result := 'WAIT';
      esNonValido:
        if nome = '' then Result := 'ERR;nome non valido'
        else Result := 'ERR;codice non valido (servono 4 cifre da 1 a 6)';
      esOk:
        begin
          S := SintesiDi(nome);
          Result := 'RESULT;' + IntToStr(esa) + ';' + IntToStr(spo) + ';' + SintesiTesto(S);
        end;
      esVinto, esGiaVinto:
        begin
          S := SintesiDi(nome);
          G := Cerca(nome);
          Result := 'WIN;' + nome + ';' + IntToStr(G.Tentativi) + ';' + IntToStr(G.Secondi) +
            ';' + IntToStr(S.Posizione) + ';' + IntToStr(S.Totale) + ';' +
            IntToStr(S.Migliore) + ';' + IntToStr(S.Peggiore);
        end;
    end;
  end
  else if cmd = 'STATO' then
  begin
    S := SintesiDi(nome);
    if FFase = faAttesa then Result := 'STATO;ATTESA;' else Result := 'STATO;GIOCO;';
    Result := Result + SintesiTesto(S);
  end
  else
    Result := 'ERR;comando sconosciuto';
end;

procedure TMMTabella.CaricaIpNomi(const Testo: String);
var
  L: TStringList;
  i: Integer;
  ip, nm: String;
begin
  IpNomi.Clear;
  L := TStringList.Create;
  try
    L.Text := Testo;
    for i := 0 to L.Count - 1 do
    begin
      ip := Trim(Campo(L[i], 1));
      nm := PulisciNome(Campo(L[i], 2));
      if (ip <> '') and (ip[1] <> '#') and (nm <> '') then
        IpNomi.Add(ip + '=' + nm);
    end;
  finally
    L.Free;
  end;
end;

function TMMTabella.NomePerIp(const Ip: String): String;
begin
  Result := IpNomi.Values[Trim(Ip)];
end;

function TMMTabella.TestoPresenze: String;
var
  i: Integer;
  nm, st: String;
  G: TGiocatore;
  nessuno: Boolean;
begin
  Result := 'CHI HA GIA'' PROVATO / CHI NO (dalla lista ip-nomi.txt)' + LineEnding;
  nessuno := True;
  for i := 0 to IpNomi.Count - 1 do
  begin
    nm := IpNomi.ValueFromIndex[i];
    G := Cerca(nm);
    if G = nil then st := 'NON ha ancora provato'
    else if G.Risolto then st := 'ha indovinato (' + IntToStr(G.Tentativi) + ' tentativi)'
    else st := 'sta provando (' + IntToStr(G.Tentativi) + ' tentativi)';
    Result := Result + Format('  %-16s %-20s %s', [IpNomi.Names[i], nm, st]) + LineEnding;
    nessuno := False;
  end;
  if nessuno then Result := Result + '  (nessun file ip-nomi.txt: si usano i nomi scritti dai ragazzi)' + LineEnding;
end;

function TMMTabella.TestoClassifica: String;
var
  i, k, pos, n: Integer;
  lista: TList;
  G, H: TGiocatore;
  S: TSintesi;
  rig: String;
begin
  lista := TList.Create;
  try
    for i := 0 to FGiocatori.Count - 1 do lista.Add(FGiocatori[i]);
    // ordinamento a bolle: risolti prima, poi tentativi, poi secondi
    for i := 0 to lista.Count - 2 do
      for k := 0 to lista.Count - 2 - i do
      begin
        G := TGiocatore(lista[k]);
        H := TGiocatore(lista[k + 1]);
        if (H.Risolto and not G.Risolto) or
           ((H.Risolto = G.Risolto) and ((H.Tentativi < G.Tentativi) or
           ((H.Tentativi = G.Tentativi) and H.Risolto and (H.Secondi < G.Secondi)))) then
          lista.Exchange(k, k + 1);
      end;
    S := SintesiDi('');
    if FFase = faAttesa then rig := 'IN ATTESA DEL VIA' else rig := 'IN GIOCO';
    Result := 'PARTITA ' + FIdPartita + ' - ' + rig + ' - finiti: ' + IntToStr(S.Totale) +
      ' di ' + IntToStr(FGiocatori.Count) + ' - migliore: ' + IntToStr(S.Migliore) +
      ' - peggiore: ' + IntToStr(S.Peggiore) + LineEnding;
    Result := Result + ' Pos  Nome                  Tentativi  Secondi  Stato' + LineEnding;
    n := 0;
    for i := 0 to lista.Count - 1 do
    begin
      G := TGiocatore(lista[i]);
      pos := PosizioneDi(G);
      if pos > 0 then rig := IntToStr(pos) else rig := '-';
      Result := Result + Format(' %3s  %-20s  %9d  %7s  %s', [rig, G.Nome, G.Tentativi,
        BoolToStr(G.Risolto, IntToStr(G.Secondi), '-'),
        BoolToStr(G.Risolto, 'INDOVINATO', 'sta provando')]) + LineEnding;
      n := n + 1;
    end;
    if n = 0 then Result := Result + ' (nessuno ha ancora provato)' + LineEnding;
  finally
    lista.Free;
  end;
end;

{ ranking.txt: una riga per giocatore, ordinata (vedi protocollo.md, parte B) }
function TMMTabella.TestoRanking: String;
var
  i, k: Integer;
  lista: TList;
  G, H: TGiocatore;
  S: TSintesi;
begin
  lista := TList.Create;
  try
    for i := 0 to FGiocatori.Count - 1 do lista.Add(FGiocatori[i]);
    for i := 0 to lista.Count - 2 do
      for k := 0 to lista.Count - 2 - i do
      begin
        G := TGiocatore(lista[k]);
        H := TGiocatore(lista[k + 1]);
        if (H.Risolto and not G.Risolto) or
           ((H.Risolto = G.Risolto) and ((H.Tentativi < G.Tentativi) or
           ((H.Tentativi = G.Tentativi) and H.Risolto and (H.Secondi < G.Secondi)))) then
          lista.Exchange(k, k + 1);
      end;
    S := SintesiDi('');
    Result := 'PARTITA;' + FIdPartita + LineEnding;
    if FFase = faAttesa then Result := Result + 'STATO;ATTESA' + LineEnding
    else Result := Result + 'STATO;GIOCO' + LineEnding;
    Result := Result + 'TOTALE;' + IntToStr(S.Totale) + LineEnding +
      'MIGLIORE;' + IntToStr(S.Migliore) + LineEnding +
      'PEGGIORE;' + IntToStr(S.Peggiore) + LineEnding;
    for i := 0 to lista.Count - 1 do
    begin
      G := TGiocatore(lista[i]);
      Result := Result + 'R;' + IntToStr(PosizioneDi(G)) + ';' + G.Nome + ';' +
        IntToStr(G.Tentativi) + ';' + IntToStr(G.Secondi) + ';' +
        BoolToStr(G.Risolto, 'S', 'N') + LineEnding;
    end;
  finally
    lista.Free;
  end;
end;

{ partita.txt: il seme (e quindi il codice) si scrive SOLO dopo il Via }
function TMMTabella.TestoPartita: String;
begin
  if FFase = faAttesa then
    Result := 'PARTITA;' + FIdPartita + ';0;ATTESA' + LineEnding
  else
    Result := 'PARTITA;' + FIdPartita + ';' + IntToStr(FSeme) + ';GIOCO;' + IntToStr(Round(FViaOra)) + LineEnding;
end;

{ ------------------------------------------------------------ lato client }

function ParsaRisposta(const Linea: String; out R: TRisposta): Boolean;
var
  cmd: String;
begin
  FillChar(R, SizeOf(R), 0);
  R.Tipo := '';
  R.Messaggio := '';
  cmd := UpperCase(Trim(Campo(Linea, 1)));
  Result := True;
  if cmd = 'RESULT' then
  begin
    R.Tipo := 'RESULT';
    R.Esatte := SIntero(Campo(Linea, 2));
    R.Spostate := SIntero(Campo(Linea, 3));
    R.Sintesi.Tentativi := SIntero(Campo(Linea, 4));
    R.Sintesi.Posizione := SIntero(Campo(Linea, 5));
    R.Sintesi.Totale := SIntero(Campo(Linea, 6));
    R.Sintesi.Migliore := SIntero(Campo(Linea, 7));
    R.Sintesi.Peggiore := SIntero(Campo(Linea, 8));
  end
  else if cmd = 'WIN' then
  begin
    R.Tipo := 'WIN';
    R.Esatte := 4;
    R.Sintesi.Tentativi := SIntero(Campo(Linea, 3));
    R.Secondi := SIntero(Campo(Linea, 4));
    R.Sintesi.Posizione := SIntero(Campo(Linea, 5));
    R.Sintesi.Totale := SIntero(Campo(Linea, 6));
    R.Sintesi.Migliore := SIntero(Campo(Linea, 7));
    R.Sintesi.Peggiore := SIntero(Campo(Linea, 8));
  end
  else if cmd = 'WAIT' then
    R.Tipo := 'WAIT'
  else if cmd = 'STATO' then
  begin
    R.Tipo := 'STATO';
    R.Messaggio := Campo(Linea, 2);          // ATTESA o GIOCO
    R.Sintesi.Tentativi := SIntero(Campo(Linea, 3));
    R.Sintesi.Posizione := SIntero(Campo(Linea, 4));
    R.Sintesi.Totale := SIntero(Campo(Linea, 5));
    R.Sintesi.Migliore := SIntero(Campo(Linea, 6));
    R.Sintesi.Peggiore := SIntero(Campo(Linea, 7));
  end
  else if cmd = 'ERR' then
  begin
    R.Tipo := 'ERR';
    R.Messaggio := Campo(Linea, 2);
  end
  else
  begin
    R.Tipo := 'ERR';
    R.Messaggio := 'risposta non capita';
    Result := False;
  end;
end;

{ Legge ranking.txt (piano B): tira fuori la sintesi per il nome dato }
function SintesiDaRanking(const Testo, ANome: String; out Fase: TFase;
  out Id: String; out Seme: Int64): TSintesi;
var
  L: TStringList;
  i, pos, num: Integer;
  riga, nome: String;
  mio: Boolean;
begin
  FillChar(Result, SizeOf(Result), 0);
  Fase := faAttesa;
  Id := '';
  Seme := 0;
  nome := PulisciNome(ANome);
  L := TStringList.Create;
  try
    L.Text := Testo;
    for i := 0 to L.Count - 1 do
    begin
      riga := Trim(L[i]);
      if Copy(riga, 1, 8) = 'PARTITA;' then
      begin
        Id := Campo(riga, 2);
        if Campo(riga, 3) <> '' then Seme := StrToInt64Def(Campo(riga, 3), 0);
        if Campo(riga, 4) = 'GIOCO' then Fase := faGioco;      // forma di partita.txt
      end
      else if riga = 'STATO;GIOCO' then Fase := faGioco
      else if Copy(riga, 1, 7) = 'TOTALE;' then Result.Totale := SIntero(Campo(riga, 2))
      else if Copy(riga, 1, 9) = 'MIGLIORE;' then Result.Migliore := SIntero(Campo(riga, 2))
      else if Copy(riga, 1, 9) = 'PEGGIORE;' then Result.Peggiore := SIntero(Campo(riga, 2))
      else if Copy(riga, 1, 2) = 'R;' then
      begin
        pos := SIntero(Campo(riga, 2));
        mio := SameText(Campo(riga, 3), nome);
        num := SIntero(Campo(riga, 4));
        if mio then
        begin
          Result.Tentativi := num;
          Result.Posizione := pos;
        end;
      end;
    end;
  finally
    L.Free;
  end;
end;

function TestoConsole(const S: TSintesi): String;
begin
  Result := '';
  if S.Totale = 0 then
    Result := 'Nessuno ha ancora indovinato'
  else
    Result := 'Migliore: ' + IntToStr(S.Migliore) + ' tentativi ' + #194#183 +
      ' Peggiore: ' + IntToStr(S.Peggiore) + ' tentativi';
  Result := Result + ' ' + #194#183 + ' Tu: ' + IntToStr(S.Tentativi) + ' tentativi';
  if S.Posizione > 0 then
    Result := Result + ', posizione ' + IntToStr(S.Posizione) + ' di ' + IntToStr(S.Totale)
  else
    Result := Result + ', non hai ancora indovinato (hanno finito in ' + IntToStr(S.Totale) + ')';
end;

end.
