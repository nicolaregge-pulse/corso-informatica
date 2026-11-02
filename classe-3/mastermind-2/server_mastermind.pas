program server_mastermind;
{ MASTERMIND 2.0 - SERVER (programma a console, gira sul PC del prof).
  Tasti:  V = Via!   N = Nuova partita (nuovo codice)   R = ridisegna
          I = rileggi ip-nomi.txt   Q = esci
  Opzioni (tutte facoltative), per esempio:  server_mastermind --porta=5050 --cartella=partita
    --porta=N        porta TCP (predefinita 5050)
    --cartella=PATH  cartella dei file (predefinita: sottocartella "partita")
    --senza-rete     solo file, niente TCP (nessun permesso del firewall)
    --seme=N         codice fisso (per le prove)
    --via            parte subito senza aspettare il tasto V
    --senza-tasti    non legge la tastiera (per le prove automatiche)
    --durata=SEC     si ferma da solo dopo SEC secondi (per le prove)
  Comandi anche da file: scrivere VIA oppure NUOVA dentro  <cartella>\comando.txt }

{$mode objfpc}{$H+}

uses
  {$ifdef unix}cthreads,{$endif}
  SysUtils, Classes, Crt, mm_logica, mm_file, mm_tcp;

var
  Tab: TMMTabella;
  FS: TMMFileServer;
  Srv: TMMTcpServerThread;
  porta: Word;
  cartella, fileIp, ultimoQuadro, quadro, cmd, t: String;
  senzaRete, senzaTasti, avviaVia: Boolean;
  durata: Integer;
  i, nuovi: Integer;
  seme: Int64;
  inizio, ultimoPoll: Double;
  fine: Boolean;
  ultimoRanking: String;
  exeDir: String;

function Opzione(const Nome: String; out Valore: String): Boolean;
var
  k: Integer;
begin
  Result := False;
  for k := 1 to ParamCount do
    if (ParamStr(k) = Nome) or (Copy(ParamStr(k), 1, Length(Nome) + 1) = Nome + '=') then
    begin
      Valore := Copy(ParamStr(k), Length(Nome) + 2, 500);
      Result := True;
      Exit;
    end;
end;

procedure CaricaIp;
var
  txt: String;
begin
  if MMLeggiTesto(fileIp, txt) then Tab.CaricaIpNomi(txt) else Tab.IpNomi.Clear;
end;

procedure NuovaPartita;
begin
  Tab.Blocca;
  try
    Tab.NuovaPartita(seme);     // seme = -1 -> casuale
    seme := -1;
  finally
    Tab.Sblocca;
  end;
  FS.Dimentica;
  FS.ScriviFile;
end;

procedure FaiVia;
begin
  Tab.Blocca;
  try
    Tab.Via;
  finally
    Tab.Sblocca;
  end;
  FS.ScriviFile;
end;

function Quadro_: String;
begin
  Tab.Blocca;
  try
    Result := 'MASTERMIND 2.0 - SERVER   [V] Via!  [N] Nuova partita  [R] ridisegna  [I] ip-nomi  [Q] esci' + LineEnding;
    if senzaRete then Result := Result + 'Rete: SPENTA (solo file)  '
    else if Srv.Pronto then Result := Result + 'Rete: in ascolto sulla porta ' + IntToStr(porta) + '  '
    else Result := Result + 'Rete: NON attiva ' + Srv.Errore + '  ';
    Result := Result + 'Cartella: ' + cartella + LineEnding + LineEnding +
      Tab.TestoClassifica + LineEnding + Tab.TestoPresenze;
  finally
    Tab.Sblocca;
  end;
end;

procedure Disegna(Forza: Boolean);
begin
  quadro := Quadro_;
  if Forza or (quadro <> ultimoQuadro) then
  begin
    ultimoQuadro := quadro;
    if not senzaTasti then ClrScr else WriteLn('------------------------------------------------');
    Write(quadro);
  end;
end;

begin
  Tab := TMMTabella.Create;
  exeDir := ExtractFilePath(ParamStr(0));
  porta := 5050;
  if Opzione('--porta', t) then porta := StrToIntDef(t, 5050);
  if not Opzione('--cartella', cartella) then cartella := exeDir + 'partita';
  fileIp := exeDir + 'ip-nomi.txt';
  if Opzione('--ipnomi', t) then fileIp := t;
  senzaRete := Opzione('--senza-rete', t);
  senzaTasti := Opzione('--senza-tasti', t);
  avviaVia := Opzione('--via', t);
  durata := 0;
  if Opzione('--durata', t) then durata := StrToIntDef(t, 0);
  seme := -1;
  if Opzione('--seme', t) then seme := StrToInt64Def(t, -1);

  FS := TMMFileServer.Create(Tab, cartella);
  CaricaIp;
  NuovaPartita;
  Srv := nil;
  if not senzaRete then
  begin
    Srv := TMMTcpServerThread.Create(Tab, porta);
    Sleep(300);
  end;
  if avviaVia then FaiVia;
  inizio := SecondiOra;
  ultimoPoll := 0;
  fine := False;
  ultimoQuadro := '';
  ultimoRanking := '';
  repeat
    // 1. tastiera
    if not senzaTasti then
      while KeyPressed do
        case UpCase(ReadKey) of
          'V': FaiVia;
          'N': begin NuovaPartita; ultimoQuadro := ''; end;
          'R': ultimoQuadro := '';
          'I': CaricaIp;
          'Q': fine := True;
        end;
    // 2. comando da file
    if MMLeggiTesto(IncludeTrailingPathDelimiter(cartella) + 'comando.txt', cmd) then
    begin
      DeleteFile(IncludeTrailingPathDelimiter(cartella) + 'comando.txt');
      cmd := UpperCase(Trim(cmd));
      if cmd = 'VIA' then FaiVia
      else if cmd = 'NUOVA' then NuovaPartita
      else if cmd = 'FINE' then fine := True;
    end;
    // 3. ogni 2 secondi rilegge i file dei ragazzi
    if SecondiOra - ultimoPoll >= 2 then
    begin
      ultimoPoll := SecondiOra;
      nuovi := FS.Poll;
      if nuovi > 0 then FS.ScriviFile;
    end;
    // 4. se la rete ha cambiato la classifica, riscrivo i file (cosi' chi usa i file la vede)
    Tab.Blocca;
    try
      t := Tab.TestoRanking;
    finally
      Tab.Sblocca;
    end;
    if t <> ultimoRanking then
    begin
      ultimoRanking := t;
      FS.ScriviFile;
    end;
    Disegna(False);
    Sleep(100);
    if (durata > 0) and (SecondiOra - inizio > durata) then fine := True;
  until fine;
  FS.ScriviFile;
  if Srv <> nil then
  begin
    Srv.Terminate;
    Srv.WaitFor;
    Srv.Free;
  end;
  FS.Free;
  Tab.Free;
end.
