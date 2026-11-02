unit client_unit;
{ MASTERMIND 2.0 - LOGICA DEL CLIENT (la parte dello studente).
  Nessuna finestra qui dentro: la form chiama queste funzioni.
  Due modi:  moFile = cartella condivisa / GitHub (PREDEFINITO, senza permessi di rete)
             moRete = TCP verso il PC del prof (veloce, se il firewall lo permette) }

{$mode objfpc}{$H+}

interface

uses
  SysUtils, Classes, mm_logica, mm_file, mm_tcp;

type
  TModoMM = (moFile, moRete);

  TMMClient = class
  private
    FIdVisto: String;      // partita di cui abbiamo gia' fissato lo "zero" del tempo
    FZero: Double;         // istante (orologio del PC) in cui abbiamo visto il Via
    function ProvaFile(const Tent: String): TRisposta;
  public
    Modo: TModoMM;
    Nome: String;
    Host: String;          // IP del PC del prof (modo rete)
    Porta: Word;           // 5050
    Cartella: String;      // cartella condivisa (modo file)
    Orologio: TFunzioneSecondi;
    Ultima: TSintesi;      // l'ultima sintesi conosciuta
    FallbackFile: Boolean; // True se la rete non andava e siamo passati ai file
    constructor Create;
    { modo rete: la riga da mandare e la lettura della risposta (la form puo' usare
      TMMRichiestaAsync per non bloccarsi) }
    function RigaProva(const Tent: String): String;
    function RigaStato: String;
    function ApplicaRisposta(const Linea: String): TRisposta;
    { fa tutto (in modo rete BLOCCA fino a 3 secondi: preferire l'Async) }
    function Prova(const Tent: String): TRisposta;
    { usata dalla form col thread: riceve la riga arrivata dalla rete; se la rete non
      andava e c'e' una cartella, rifa' il tentativo con i file (piano B automatico) }
    function RispostaDaRete(const Linea, Tent: String): TRisposta;
    function Aggiorna: TRisposta;      // aggiorna la console senza fare tentativi
    function Console: String;          // la frase da mostrare in una Label
    function TestoRisposta(const R: TRisposta): String;   // frase per l'esito del tentativo
    { Legge i due file di configurazione messi accanto al programma:
        server.txt    una riga:  IP:PORTA        (es. 192.168.10.5:5050)  -> modo rete
        cartella.txt  una riga:  percorso cartella condivisa                -> modo file
      Se ci sono tutti e due: parte in rete e, se il server non risponde, passa
      da solo ai file. Se c'e' solo cartella.txt: file. }
    function CaricaConfig(const CartellaProgramma: String): Boolean;
  end;

implementation

constructor TMMClient.Create;
begin
  inherited Create;
  Modo := moFile;
  Porta := 5050;
  Orologio := @SecondiOra;
  FillChar(Ultima, SizeOf(Ultima), 0);
end;

function TMMClient.RigaProva(const Tent: String): String;
begin
  Result := 'GUESS;' + PulisciNome(Nome) + ';' + Trim(Tent);
end;

function TMMClient.RigaStato: String;
begin
  Result := 'STATO;' + PulisciNome(Nome);
end;

function TMMClient.ApplicaRisposta(const Linea: String): TRisposta;
begin
  ParsaRisposta(Linea, Result);
  if (Result.Tipo = 'RESULT') or (Result.Tipo = 'WIN') or (Result.Tipo = 'STATO') then
    Ultima := Result.Sintesi;
end;

{ ---- modo file ---- }

{ ---- modo file ---- }

function TMMClient.ProvaFile(const Tent: String): TRisposta;
var
  base, testoP, testoR, mio, riga, segreto, id, tutto: String;
  seme, via: Int64;
  fase: TFase;
  sint: TSintesi;
  righe: TStringList;
  i, mie, ultimoSec, esa, spo, sec: Integer;
  risolto: Boolean;
begin
  Result := Default(TRisposta);
  base := IncludeTrailingPathDelimiter(Cartella);
  if not CodiceValido(Trim(Tent)) then
  begin
    Result.Tipo := 'ERR';
    Result.Messaggio := 'codice non valido (servono 4 cifre da 1 a 6)';
    Exit;
  end;
  if (PulisciNome(Nome) = '') then
  begin
    Result.Tipo := 'ERR';
    Result.Messaggio := 'scrivi il tuo nome';
    Exit;
  end;
  if not MMLeggiTesto(base + 'partita.txt', testoP) then
  begin
    Result.Tipo := 'ERR';
    Result.Messaggio := 'non trovo partita.txt nella cartella (sincronizza o controlla il percorso)';
    Exit;
  end;
  // partita.txt ha la stessa forma di una riga PARTITA di ranking.txt
  sint := SintesiDaRanking(testoP, Nome, fase, id, seme);
  if (fase <> faGioco) or (seme = 0) then
  begin
    Result.Tipo := 'WAIT';
    Exit;
  end;
  segreto := CodiceDaSeme(seme);
  mio := MMFileGiocatore(Cartella, Nome);
  // rileggo il MIO file: quanti tentativi ho fatto in questa partita? ho gia' vinto?
  mie := 0;
  ultimoSec := 0;
  risolto := False;
  righe := TStringList.Create;
  try
    if MMLeggiTesto(mio, tutto) then righe.Text := tutto;
    for i := 0 to righe.Count - 1 do
    begin
      riga := Trim(righe[i]);
      if Campo(riga, 1) = id then
      begin
        mie := mie + 1;
        ultimoSec := StrToIntDef(Campo(riga, 4), 0);
        if Campo(riga, 3) = segreto then risolto := True;
      end;
    end;
  finally
    righe.Free;
  end;
  // lo "zero" del tempo: il Via scritto dal server in partita.txt
  if FIdVisto <> id then
  begin
    FIdVisto := id;
    via := StrToInt64Def(Campo(Trim(testoP), 5), 0);      // ora del Via secondo il server
    if (via > 0) and (Orologio() - via >= 0) and (Orologio() - via < 14400) then
      FZero := via                                        // orologi d'accordo: conta dal Via vero
    else
      FZero := Orologio() - ultimoSec;                    // orologi sballati: conta da quando lo vedo io
  end;
  sec := Round(Orologio() - FZero);
  Valuta(segreto, Trim(Tent), esa, spo);
  if not risolto then
  begin
    MMAggiungiRiga(mio, id + ';' + PulisciNome(Nome) + ';' + Trim(Tent) + ';' + IntToStr(sec));
    mie := mie + 1;
    risolto := (esa = 4);
  end
  else
  begin
    esa := 4;      // ha gia' vinto: i tentativi in piu' non contano
    spo := 0;
  end;
  // la classifica la vedo da ranking.txt (puo' essere in ritardo)
  sint := Default(TSintesi);
  if MMLeggiTesto(base + 'ranking.txt', testoR) then
    sint := SintesiDaRanking(testoR, Nome, fase, id, seme);
  sint.Tentativi := mie;
  if not risolto then sint.Posizione := 0;
  Result.Esatte := esa;
  Result.Spostate := spo;
  Result.Sintesi := sint;
  if risolto then
  begin
    Result.Tipo := 'WIN';
    Result.Secondi := sec;
  end
  else
    Result.Tipo := 'RESULT';
  Ultima := sint;
end;

function TMMClient.RispostaDaRete(const Linea, Tent: String): TRisposta;
begin
  Result := ApplicaRisposta(Linea);
  if (Result.Tipo = 'ERR') and (Pos('server non raggiungibile', Result.Messaggio) > 0)
     and (Cartella <> '') then
  begin
    Modo := moFile;                 // piano B automatico
    FallbackFile := True;
    Result := ProvaFile(Tent);
  end;
end;

function TMMClient.Prova(const Tent: String): TRisposta;
begin
  if Modo = moFile then
    Result := ProvaFile(Tent)
  else
    Result := RispostaDaRete(MMTcpRichiesta(Host, Porta, RigaProva(Tent)), Tent);
end;

function LeggiPrimaRiga(const Nomefile: String): String;
var
  t: String;
  L: TStringList;
begin
  Result := '';
  if not MMLeggiTesto(Nomefile, t) then Exit;
  L := TStringList.Create;
  try
    L.Text := t;
    if L.Count > 0 then Result := Trim(L[0]);
  finally
    L.Free;
  end;
end;

function TMMClient.CaricaConfig(const CartellaProgramma: String): Boolean;
var
  base, srv, cart: String;
  k: Integer;
begin
  base := IncludeTrailingPathDelimiter(CartellaProgramma);
  srv := LeggiPrimaRiga(base + 'server.txt');
  cart := LeggiPrimaRiga(base + 'cartella.txt');
  Result := False;
  Cartella := cart;
  if srv <> '' then
  begin
    k := Pos(':', srv);
    if k = 0 then
    begin
      Host := srv;
      Porta := 5050;
    end
    else
    begin
      Host := Trim(Copy(srv, 1, k - 1));
      Porta := StrToIntDef(Trim(Copy(srv, k + 1, 10)), 5050);
    end;
    Modo := moRete;
    Result := True;
  end
  else if cart <> '' then
  begin
    Modo := moFile;
    Result := True;
  end;
end;

function TMMClient.Aggiorna: TRisposta;
var
  testo, id: String;
  fase: TFase;
  seme: Int64;
  s: TSintesi;
  mie: Integer;
begin
  Result := Default(TRisposta);
  if Modo = moRete then
  begin
    Result := ApplicaRisposta(MMTcpRichiesta(Host, Porta, RigaStato));
    Exit;
  end;
  if MMLeggiTesto(IncludeTrailingPathDelimiter(Cartella) + 'ranking.txt', testo) then
  begin
    mie := Ultima.Tentativi;
    s := SintesiDaRanking(testo, Nome, fase, id, seme);
    if s.Tentativi < mie then s.Tentativi := mie;     // i miei tentativi li conosco meglio io
    Ultima := s;
    Result.Tipo := 'STATO';
    Result.Sintesi := s;
    if fase = faAttesa then Result.Messaggio := 'ATTESA' else Result.Messaggio := 'GIOCO';
  end
  else
  begin
    Result.Tipo := 'ERR';
    Result.Messaggio := 'non trovo ranking.txt nella cartella';
  end;
end;

function TMMClient.Console: String;
begin
  Result := TestoConsole(Ultima);
end;

function TMMClient.TestoRisposta(const R: TRisposta): String;
begin
  if R.Tipo = 'RESULT' then
    Result := 'Esatte: ' + IntToStr(R.Esatte) + '  Spostate: ' + IntToStr(R.Spostate)
  else if R.Tipo = 'WIN' then
    Result := 'BRAVO! Indovinato in ' + IntToStr(R.Sintesi.Tentativi) + ' tentativi'
  else if R.Tipo = 'WAIT' then
    Result := 'Aspetta il Via del prof...'
  else
    Result := 'Problema: ' + R.Messaggio;
end;

end.
