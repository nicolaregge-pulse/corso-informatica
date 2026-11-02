unit mm_file;
{ MASTERMIND 2.0 - TRASPORTO B: FILE - e' il modo PREDEFINITO (non chiede permessi di rete).
  Cartella condivisa (cartella di rete, oppure repository GitHub clonato e sincronizzato):
    partita.txt          scritto dal SERVER:  PARTITA;id;seme;ATTESA|GIOCO
    ranking.txt          scritto dal SERVER:  la classifica (vedi protocollo.md)
    giocatori\NOME.txt   scritto da OGNI studente, una riga per tentativo:
                         id;NOME;1234;secondi
  Ogni studente scrive SOLO il suo file: niente conflitti in Git.
  Il server rilegge la cartella ogni 2 secondi e ricalcola tutto. }

{$mode objfpc}{$H+}

interface

uses
  SysUtils, Classes, mm_logica;

type
  { LATO SERVER }
  TMMFileServer = class
  private
    FTab: TMMTabella;
    FCartella: String;
    FLetti: TStringList;     // nomefile=righe gia' elaborate
  public
    constructor Create(ATab: TMMTabella; const ACartella: String);
    destructor Destroy; override;
    procedure ScriviFile;            // scrive partita.txt e ranking.txt
    function Poll: Integer;          // legge le righe nuove; ritorna quanti tentativi nuovi
    procedure Dimentica;             // dopo "Nuova partita"
    property Cartella: String read FCartella;
  end;

function MMScriviTesto(const NomeFile, Testo: String): Boolean;
function MMLeggiTesto(const NomeFile: String; out Testo: String): Boolean;
function MMAggiungiRiga(const NomeFile, Riga: String): Boolean;
function MMCartellaGiocatori(const Cartella: String): String;
function MMFileGiocatore(const Cartella, Nome: String): String;

implementation

function MMCartellaGiocatori(const Cartella: String): String;
begin
  Result := IncludeTrailingPathDelimiter(Cartella) + 'giocatori';
end;

function MMFileGiocatore(const Cartella, Nome: String): String;
begin
  Result := IncludeTrailingPathDelimiter(MMCartellaGiocatori(Cartella)) +
    PulisciNome(Nome) + '.txt';
end;

{ Lettura che non da' fastidio a chi sta scrivendo (fmShareDenyNone), con 3 tentativi }
function MMLeggiTesto(const NomeFile: String; out Testo: String): Boolean;
var
  F: TFileStream;
  k: Integer;
begin
  Testo := '';
  Result := False;
  for k := 1 to 3 do
  begin
    try
      if not FileExists(NomeFile) then Exit;
      F := TFileStream.Create(NomeFile, fmOpenRead or fmShareDenyNone);
      try
        SetLength(Testo, F.Size);
        if F.Size > 0 then F.ReadBuffer(Testo[1], F.Size);
      finally
        F.Free;
      end;
      Result := True;
      Exit;
    except
      Sleep(50);
    end;
  end;
end;

function MMScriviTesto(const NomeFile, Testo: String): Boolean;
var
  F: TFileStream;
begin
  Result := False;
  try
    ForceDirectories(ExtractFilePath(NomeFile));
    F := TFileStream.Create(NomeFile, fmCreate);
    try
      if Length(Testo) > 0 then F.WriteBuffer(Testo[1], Length(Testo));
    finally
      F.Free;
    end;
    Result := True;
  except
    Result := False;
  end;
end;

{ Aggiunge UNA riga in fondo (crea il file se non c'e'). Riprova 3 volte. }
function MMAggiungiRiga(const NomeFile, Riga: String): Boolean;
var
  F: TFileStream;
  k: Integer;
  s: String;
begin
  Result := False;
  s := Riga + LineEnding;
  for k := 1 to 3 do
  begin
    try
      ForceDirectories(ExtractFilePath(NomeFile));
      if FileExists(NomeFile) then
        F := TFileStream.Create(NomeFile, fmOpenWrite or fmShareDenyNone)
      else
        F := TFileStream.Create(NomeFile, fmCreate or fmShareDenyNone);
      try
        F.Seek(0, soEnd);
        F.WriteBuffer(s[1], Length(s));
      finally
        F.Free;
      end;
      Result := True;
      Exit;
    except
      Sleep(80);
    end;
  end;
end;

{ ------------------------------------------------------------ server }

constructor TMMFileServer.Create(ATab: TMMTabella; const ACartella: String);
begin
  inherited Create;
  FTab := ATab;
  FCartella := ACartella;
  FLetti := TStringList.Create;
  ForceDirectories(MMCartellaGiocatori(FCartella));
end;

destructor TMMFileServer.Destroy;
begin
  FLetti.Free;
  inherited Destroy;
end;

procedure TMMFileServer.Dimentica;
begin
  FLetti.Clear;
end;

procedure TMMFileServer.ScriviFile;
var
  base: String;
begin
  base := IncludeTrailingPathDelimiter(FCartella);
  FTab.Blocca;
  try
    MMScriviTesto(base + 'partita.txt', FTab.TestoPartita);
    MMScriviTesto(base + 'ranking.txt', FTab.TestoRanking);
  finally
    FTab.Sblocca;
  end;
end;

function TMMFileServer.Poll: Integer;
var
  sr: TSearchRec;
  cart, nomef, testo, riga, id: String;
  righe: TStringList;
  fatti, i, ultimo, idx, sec, esa, spo: Integer;
  esito: TEsito;
begin
  Result := 0;
  cart := IncludeTrailingPathDelimiter(MMCartellaGiocatori(FCartella));
  if FindFirst(cart + '*.txt', faAnyFile, sr) <> 0 then Exit;
  righe := TStringList.Create;
  try
    repeat
      nomef := cart + sr.Name;
      if not MMLeggiTesto(nomef, testo) then Continue;
      righe.Text := testo;
      ultimo := righe.Count;
      // l'ultima riga conta solo se il file finisce con "a capo" (altrimenti e' a meta')
      if (Length(testo) > 0) and not (testo[Length(testo)] in [#10, #13]) then
        ultimo := ultimo - 1;
      idx := FLetti.IndexOfName(sr.Name);
      if idx < 0 then fatti := 0 else fatti := StrToIntDef(FLetti.ValueFromIndex[idx], 0);
      i := fatti;
      while i < ultimo do
      begin
        riga := Trim(righe[i]);
        id := Campo(riga, 1);
        if (riga <> '') and (id = FTab.IdPartita) then
        begin
          sec := StrToIntDef(Campo(riga, 4), 0);
          FTab.Blocca;
          try
            esito := FTab.Tentativo(Campo(riga, 2), Campo(riga, 3), sec, esa, spo);
          finally
            FTab.Sblocca;
          end;
          if esito = esAttesa then Break;     // prima del Via: la riga resta in attesa
          if esito in [esOk, esVinto] then Result := Result + 1;
        end;
        i := i + 1;
      end;
      if idx < 0 then FLetti.Add(sr.Name + '=' + IntToStr(i))
      else FLetti.ValueFromIndex[idx] := IntToStr(i);
    until FindNext(sr) <> 0;
  finally
    righe.Free;
    FindClose(sr);
  end;
end;

end.
