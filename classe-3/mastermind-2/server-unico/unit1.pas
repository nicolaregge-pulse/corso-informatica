unit Unit1;
{ MASTERMIND 2.0 - SERVER CON FINESTRA, TUTTO IN UN FILE (per il prof).

  Il PC del prof pensa UNA combinazione segreta per tutta la classe, riceve i
  tentativi dei ragazzi e tiene la classifica. Tutto con il mouse:
    1. Premi "Avvia server" (la porta e' 5050: non toccarla).
    2. Dai ai ragazzi l'indirizzo che compare nella casella "Da dire ai ragazzi".
    3. Quando sono collegati, premi "Via!".
    4. Per ricominciare con un'altra combinazione: "Nuova combinazione".

  Niente thread: il Timer1 chiama la rete ogni 50 millisecondi e la finestra
  resta sempre libera. Il protocollo e' quello di protocollo.md:
    GUESS;nome;1234  ->  WAIT | RESULT;esatte;spostate;... | WIN;... | ERR;...
    STATO;nome       ->  STATO;ATTESA;... | STATO;GIOCO;... }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls, Grids,
  sockets, ssockets;

type
  TGioc = record            // un ragazzo
    Nome: String;
    Tent: Integer;          // tentativi fatti
    Secondi: Integer;       // secondi dal Via alla vittoria
    Risolto: Boolean;
    Ultimo: QWord;          // ultimo istante in cui si e' fatto sentire (millisecondi)
  end;

  TForm1 = class(TForm)
    LblPorta: TLabel;          // scritta sopra la porta
    EdPorta: TEdit;            // la porta, di solito 5050
    BtnAvvia: TButton;         // "Avvia server"
    LblStato: TLabel;          // dice se il server e' acceso
    LblIp: TLabel;             // l'IP di questo PC
    LblIndirizzo: TLabel;      // scritta sopra l'indirizzo da dire ai ragazzi
    EdIndirizzo: TEdit;        // IP:porta pronto da copiare (Ctrl+C)
    BtnVia: TButton;           // "Via!"
    BtnNuova: TButton;         // "Nuova combinazione"
    LblSegreto: TLabel;        // la combinazione segreta (nascosta; un clic la mostra)
    LblGiocatori: TLabel;      // quanti collegati / vinto / stanno provando
    LblClassifica: TLabel;     // scritta "Classifica"
    LblRegistro: TLabel;       // scritta "Registro"
    Griglia: TStringGrid;      // la classifica
    MemoRegistro: TMemo;       // collegamenti e tentativi in tempo reale
    Timer1: TTimer;            // ogni 50 ms: rete e classifica
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure BtnAvviaClick(Sender: TObject);
    procedure BtnViaClick(Sender: TObject);
    procedure BtnNuovaClick(Sender: TObject);
    procedure EdPortaChange(Sender: TObject);
    procedure LblSegretoClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    Srv: TInetServer;             // la rete (nil = spento)
    Servite: Integer;             // richieste servite nel Tick in corso
    G: array of TGioc;            // tutti i ragazzi visti
    Segreto: String;              // la combinazione, 4 cifre da 1 a 6
    Gioco: Boolean;               // False = si aspetta il Via, True = si gioca
    ViaMs: QWord;                 // istante del Via
    IpPc: String;
    Sporco: Boolean;              // True = c'e' qualcosa di nuovo da ridisegnare
    MostraSegreto: Boolean;
    UltimoGiro: QWord;
    procedure Scrivi(const Testo: String);
    procedure Connesso(Sender: TObject; Data: TSocketStream);
    procedure Inattivo(Sender: TObject);
    function Servi(const Ip, Linea: String): String;
    function Trova(const Nome: String; Crea: Boolean): Integer;
    function Sintesi(i: Integer): String;
    function Collegati: Integer;
    procedure AggiornaStato;
    procedure AggiornaSegreto;
    procedure AggiornaClassifica;
    procedure NuovaPartita;
  public
    Avviato: Boolean;                 // True quando FormCreate e' gia' partita
    procedure AfterConstruction; override;
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

const
  FUORI_LINEA_MS = 20000;   // dopo 20 secondi senza notizie un ragazzo risulta "scollegato"
  MAX_PER_TICK = 12;        // richieste servite al massimo ad ogni Tick

{ ---- piccole funzioni di aiuto ---- }

function Zeri(N, Larghezza: Integer): String;
begin
  Result := IntToStr(N);
  while Length(Result) < Larghezza do Result := '0' + Result;
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
  if Length(Result) > 20 then Result := Trim(Copy(Result, 1, 20));
end;

function CodiceValido(const S: String): Boolean;
var
  i: Integer;
begin
  Result := Length(S) = 4;
  if Result then
    for i := 1 to 4 do
      if not (S[i] in ['1'..'6']) then Result := False;
end;

{ Come il Mastermind normale: prima le esatte, poi le spostate }
procedure Valuta(const Segr, Tent: String; out Esatte, Spostate: Integer);
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
  Spostate := 0;
  for i := 1 to 4 do
    if Tent[i] = Segr[i] then
    begin
      Inc(Esatte);
      usataS[i] := True;
      usataT[i] := True;
    end;
  for i := 1 to 4 do
    if not usataT[i] then
      for j := 1 to 4 do
        if (not usataS[j]) and (Tent[i] = Segr[j]) then
        begin
          Inc(Spostate);
          usataS[j] := True;
          Break;
        end;
end;

{ Si "prepara" una telefonata UDP verso un indirizzo qualunque: NON parte nessun
  pacchetto, ma il sistema sceglie la scheda di rete giusta e noi leggiamo il
  suo indirizzo. Funziona uguale su Windows e Linux. }
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
  Result := IpVerso('8.8.8.8');                           // rete con uscita su Internet
  if Result = '' then Result := IpVerso('192.168.0.1');   // rete di classe senza Internet
  if Result = '' then Result := IpVerso('10.0.0.1');
  if Result = '' then Result := IpVerso('172.16.0.1');
end;

{ ---- avvio e chiusura ---- }

procedure TForm1.FormCreate(Sender: TObject);
begin
  Avviato := True;
  Randomize;
  Srv := nil;
  Gioco := False;
  Sporco := True;
  MostraSegreto := False;
  UltimoGiro := 0;
  Griglia.ColCount := 4;
  Griglia.RowCount := 1;
  Griglia.FixedRows := 1;
  Griglia.FixedCols := 0;
  Griglia.Cells[0, 0] := 'Posto';
  Griglia.Cells[1, 0] := 'Nome';
  Griglia.Cells[2, 0] := 'Tentativi';
  Griglia.Cells[3, 0] := 'Stato';
  Griglia.ColWidths[0] := 50;
  Griglia.ColWidths[1] := 130;
  Griglia.ColWidths[2] := 70;
  Griglia.ColWidths[3] := 140;
  IpPc := MMIpDelPc;
  if IpPc = '' then
    LblIp.Caption := 'IP di questo PC: non si ricava (chiedi al prof)'
  else
    LblIp.Caption := 'IP di questo PC: ' + IpPc;
  EdPortaChange(nil);
  AggiornaStato;
  AggiornaSegreto;
  Scrivi('Benvenuto! Premi "Avvia server" per cominciare.');
end;

{ A prova di errore: se il form e' stato caricato senza i collegamenti dei bottoni
  (succede quando si incolla il form PRIMA del codice) li colleghiamo da qui,
  dopo che la finestra e' stata costruita. Se erano gia' collegati non cambia nulla. }
procedure TForm1.AfterConstruction;
begin
  inherited AfterConstruction;
  if not Assigned(BtnAvvia.OnClick) then BtnAvvia.OnClick := @BtnAvviaClick;
  if not Assigned(BtnVia.OnClick) then BtnVia.OnClick := @BtnViaClick;
  if not Assigned(BtnNuova.OnClick) then BtnNuova.OnClick := @BtnNuovaClick;
  if not Assigned(LblSegreto.OnClick) then LblSegreto.OnClick := @LblSegretoClick;
  if not Assigned(EdPorta.OnChange) then EdPorta.OnChange := @EdPortaChange;
  if not Assigned(Timer1.OnTimer) then Timer1.OnTimer := @Timer1Timer;
  if not Assigned(OnDestroy) then OnDestroy := @FormDestroy;
  if not Avviato then FormCreate(nil);
end;

procedure TForm1.FormDestroy(Sender: TObject);
begin
  Timer1.Enabled := False;
  FreeAndNil(Srv);
end;

procedure TForm1.EdPortaChange(Sender: TObject);
begin
  if EdIndirizzo = nil then Exit;     // mentre Lazarus carica la finestra la casella non esiste ancora
  if IpPc <> '' then
    EdIndirizzo.Text := IpPc + ':' + Trim(EdPorta.Text)
  else
    EdIndirizzo.Text := '(IP non ricavato):' + Trim(EdPorta.Text);
end;

{ ---- registro ---- }

procedure TForm1.Scrivi(const Testo: String);
begin
  if MemoRegistro.Lines.Count > 1500 then
    while MemoRegistro.Lines.Count > 1000 do MemoRegistro.Lines.Delete(0);
  MemoRegistro.Lines.Add(FormatDateTime('hh:nn:ss', Now) + '  ' + Testo);
  MemoRegistro.SelStart := MemoRegistro.GetTextLen;     // scorre in fondo
end;

{ ---- la rete: niente thread, il Timer1 la chiama ogni 50 ms ---- }

procedure TForm1.Inattivo(Sender: TObject);
begin
  Srv.StopAccepting;            // nessuno bussa: torniamo alla finestra
end;

procedure TForm1.Connesso(Sender: TObject; Data: TSocketStream);
var
  c: Char;
  n: Integer;
  linea, risp: String;
begin
  Inc(Servite);
  if Servite >= MAX_PER_TICK then Srv.StopAccepting;   // gli altri al prossimo Tick
  try
    try
      Data.IOTimeout := 500;       // un client muto fa aspettare la finestra al massimo mezzo secondo
      linea := '';
      repeat
        n := Data.Read(c, 1);
        if (n = 1) and (c <> #10) and (c <> #13) then linea := linea + c;
      until (n <= 0) or (c = #10) or (Length(linea) > 200);
      if linea <> '' then
      begin
        risp := Servi(NetAddrToStr(Data.RemoteAddress.sin_addr), linea) + #10;
        Data.WriteBuffer(risp[1], Length(risp));
      end;
    except
      on E: Exception do ;         // un client che sbaglia non deve fermare il server
    end;
  finally
    Data.Free;
  end;
end;

{ ---- il protocollo: UNA riga in, UNA riga fuori (e una riga nel registro) ---- }

{ Indice del ragazzo (-1 se non c'e'); con Crea lo aggiunge e segna che si e' fatto sentire }
function TForm1.Trova(const Nome: String; Crea: Boolean): Integer;
var
  i: Integer;
begin
  Result := -1;
  for i := 0 to High(G) do
    if SameText(G[i].Nome, Nome) then Result := i;
  if (Result < 0) and Crea then
  begin
    SetLength(G, Length(G) + 1);
    Result := High(G);
    FillChar(G[Result], SizeOf(TGioc), 0);
    G[Result].Nome := Nome;
    Scrivi(Nome + ' si e'' collegato');
  end;
  if Crea then G[Result].Ultimo := GetTickCount64;
end;

{ "tentativi;posto;quanti hanno finito;migliore;peggiore" - posto 0 = non ha ancora finito }
function TForm1.Sintesi(i: Integer): String;
var
  k, tot, mig, peg, posto: Integer;
begin
  tot := 0; mig := 0; peg := 0;
  for k := 0 to High(G) do
    if G[k].Risolto then
    begin
      Inc(tot);
      if (mig = 0) or (G[k].Tent < mig) then mig := G[k].Tent;
      if G[k].Tent > peg then peg := G[k].Tent;
    end;
  posto := 0;
  if (i >= 0) and G[i].Risolto then
  begin
    posto := 1;     // 1 + chi e' STRETTAMENTE meglio: a pari tentativi e secondi, stesso posto
    for k := 0 to High(G) do
      if G[k].Risolto and ((G[k].Tent < G[i].Tent) or
         ((G[k].Tent = G[i].Tent) and (G[k].Secondi < G[i].Secondi))) then Inc(posto);
  end;
  if i >= 0 then Result := IntToStr(G[i].Tent) else Result := '0';
  Result := Result + ';' + IntToStr(posto) + ';' + IntToStr(tot) + ';' + IntToStr(mig) + ';' + IntToStr(peg);
end;

function TForm1.Servi(const Ip, Linea: String): String;
var
  cmd, nome, guess: String;
  i, esa, spo: Integer;
begin
  cmd := UpperCase(Trim(Campo(Linea, 1)));
  nome := PulisciNome(Campo(Linea, 2));
  Sporco := True;
  if nome = '' then
    i := -1
  else
    i := Trova(nome, True);
  if cmd = 'STATO' then
  begin
    if Gioco then Result := 'STATO;GIOCO;' else Result := 'STATO;ATTESA;';
    Result := Result + Sintesi(i);
  end
  else if cmd <> 'GUESS' then
    Result := 'ERR;comando sconosciuto'
  else
  begin
    guess := Trim(Campo(Linea, 3));
    if i < 0 then
      Result := 'ERR;nome non valido'
    else if not CodiceValido(guess) then
      Result := 'ERR;codice non valido (servono 4 cifre da 1 a 6)'
    else if not Gioco then
    begin
      Result := 'WAIT';
      Scrivi(nome + ' ha provato prima del Via: non conta');
    end
    else
    begin
      Valuta(Segreto, guess, esa, spo);
      if not G[i].Risolto then            // dopo la vittoria i tentativi non contano piu'
      begin
        Inc(G[i].Tent);
        if esa = 4 then
        begin
          G[i].Risolto := True;
          G[i].Secondi := Round((GetTickCount64 - ViaMs) / 1000);
        end
        else
          Scrivi(nome + ' prova ' + guess + ':  ' + IntToStr(esa) + ' esatte, ' +
            IntToStr(spo) + ' spostate  (tentativo n. ' + IntToStr(G[i].Tent) + ')');
      end;
      if G[i].Risolto then
      begin
        Result := Sintesi(i);       // tent;posto;totale;migliore;peggiore
        Scrivi('*** ' + nome + ' HA VINTO! ' + IntToStr(G[i].Tent) + ' tentativi, ' +
          IntToStr(G[i].Secondi) + ' secondi, posto n. ' + Campo(Result, 2) + ' ***');
        Result := 'WIN;' + nome + ';' + IntToStr(G[i].Tent) + ';' + IntToStr(G[i].Secondi) +
          ';' + Copy(Result, Pos(';', Result) + 1, 100);
      end
      else
        Result := 'RESULT;' + IntToStr(esa) + ';' + IntToStr(spo) + ';' + Sintesi(i);
    end;
  end;
end;

function TForm1.Collegati: Integer;
var
  i: Integer;
begin
  Result := 0;
  for i := 0 to High(G) do
    if GetTickCount64 - G[i].Ultimo <= FUORI_LINEA_MS then Inc(Result);
end;

{ ---- scritte e classifica ---- }

procedure TForm1.AggiornaStato;
begin
  if Srv = nil then
    LblStato.Caption := 'Server SPENTO'
  else if not Gioco then
    LblStato.Caption := 'Server acceso (porta ' + EdPorta.Text + ') - si aspetta il Via!'
  else
    LblStato.Caption := 'Server acceso (porta ' + EdPorta.Text + ') - GIOCO IN CORSO';
end;

procedure TForm1.AggiornaSegreto;
begin
  if Srv = nil then
    LblSegreto.Caption := 'Combinazione segreta: (non ancora scelta)'
  else if MostraSegreto then
    LblSegreto.Caption := 'Combinazione segreta: ' + Segreto + '   (clicca per nasconderla)'
  else
    LblSegreto.Caption := 'Combinazione segreta: ????   (clicca per vederla)';
end;

{ Chiave per ordinare: prima chi ha vinto (meno tentativi, meno secondi), poi chi prova, poi gli altri }
function ChiaveDi(const R: TGioc): String;
begin
  if R.Risolto then Result := '0' + Zeri(R.Tent, 6) + Zeri(R.Secondi, 8)
  else if R.Tent > 0 then Result := '1' + Zeri(R.Tent, 6) + Zeri(0, 8)
  else Result := '2' + Zeri(0, 14);
end;

procedure TForm1.AggiornaClassifica;
var
  ord_: array of Integer;
  i, k, t, vinti, provano, posto, ultimaPos: Integer;
  chiave, ultimaChiave, stato: String;
begin
  SetLength(ord_, Length(G));
  for i := 0 to High(G) do ord_[i] := i;
  for i := 1 to High(G) do          // ordinamento a inserimento
  begin
    t := ord_[i];
    k := i - 1;
    while (k >= 0) and ((ChiaveDi(G[ord_[k]]) + LowerCase(G[ord_[k]].Nome)) >
          (ChiaveDi(G[t]) + LowerCase(G[t].Nome))) do
    begin
      ord_[k + 1] := ord_[k];
      Dec(k);
    end;
    ord_[k + 1] := t;
  end;
  vinti := 0;
  provano := 0;
  ultimaChiave := '';
  ultimaPos := 0;
  Griglia.BeginUpdate;
  try
    Griglia.RowCount := Length(G) + 1;
    for i := 0 to High(G) do
      with G[ord_[i]] do
      begin
        chiave := ChiaveDi(G[ord_[i]]);
        if Risolto then
        begin
          Inc(vinti);
          stato := 'HA VINTO (' + IntToStr(Secondi) + ' s)';
          if chiave = ultimaChiave then posto := ultimaPos else posto := i + 1;   // pari merito
          ultimaChiave := chiave;
          ultimaPos := posto;
          Griglia.Cells[0, i + 1] := IntToStr(posto);
        end
        else
        begin
          if Tent > 0 then
          begin
            Inc(provano);
            stato := 'sta provando';
          end
          else
            stato := 'collegato, non ha ancora provato';
          Griglia.Cells[0, i + 1] := '-';
        end;
        if GetTickCount64 - Ultimo > FUORI_LINEA_MS then
          if Tent > 0 then stato := stato + ' (scollegato)' else stato := 'scollegato';
        Griglia.Cells[1, i + 1] := Nome;
        Griglia.Cells[2, i + 1] := IntToStr(Tent);
        Griglia.Cells[3, i + 1] := stato;
      end;
  finally
    Griglia.EndUpdate;
  end;
  LblGiocatori.Caption := 'Giocatori collegati: ' + IntToStr(Collegati) +
    '     Hanno vinto: ' + IntToStr(vinti) + '     Stanno provando: ' + IntToStr(provano);
end;

{ ---- i bottoni ---- }

procedure TForm1.NuovaPartita;
var
  i: Integer;
begin
  Segreto := '';
  for i := 1 to 4 do Segreto := Segreto + IntToStr(Random(6) + 1);   // combinazione a caso
  Gioco := False;
  SetLength(G, 0);          // i ragazzi ricompaiono da soli al loro prossimo messaggio
  Sporco := True;
end;

procedure TForm1.BtnAvviaClick(Sender: TObject);
var
  porta: Integer;
  errore: String;
begin
  porta := StrToIntDef(Trim(EdPorta.Text), 0);
  if (porta < 1) or (porta > 65535) then
  begin
    ShowMessage('La porta deve essere un numero tra 1 e 65535. Di solito si usa 5050.');
    Exit;
  end;
  FreeAndNil(Srv);
  try
    Srv := TInetServer.Create('0.0.0.0', Word(porta));
    {$ifdef unix}Srv.ReuseAddress := True;{$endif}
    Srv.QueueSize := 64;            // 22 client che bussano insieme restano in coda
    Srv.AcceptIdleTimeout := 1;     // un giro di accettazione dura al massimo ~1 ms
    Srv.OnConnect := @Connesso;
    Srv.OnIdle := @Inattivo;
    Srv.Listen;                     // qui si scopre se la porta e' occupata
  except
    on E: Exception do
    begin
      errore := E.Message;
      FreeAndNil(Srv);
    end;
  end;
  if Srv = nil then
  begin
    Scrivi('NON riesco ad aprire la porta ' + IntToStr(porta) + ': ' + errore);
    ShowMessage('Non riesco ad aprire la porta ' + IntToStr(porta) + '.' + LineEnding +
      'Forse un altro server e'' gia'' acceso, oppure la porta e'' bloccata.' + LineEnding +
      'Prova un''altra porta, per esempio 5051, e premi di nuovo "Avvia server".');
    AggiornaStato;
    Exit;
  end;
  NuovaPartita;
  EdPorta.Enabled := False;
  BtnAvvia.Enabled := False;
  BtnAvvia.Caption := 'Server acceso';
  BtnVia.Enabled := True;
  BtnNuova.Enabled := True;
  EdPortaChange(nil);
  Scrivi('Server acceso sulla porta ' + IntToStr(porta) + '. Combinazione scelta (nascosta).');
  if IpPc <> '' then
    Scrivi('Di'' ai ragazzi di scrivere: ' + IpPc + ':' + IntToStr(porta));
  Scrivi('Se Windows chiede "Consenti accesso", clicca "Consenti accesso".');
  Timer1.Enabled := True;
  AggiornaStato;
  AggiornaSegreto;
end;

procedure TForm1.BtnViaClick(Sender: TObject);
begin
  if (Srv = nil) or Gioco then Exit;
  Gioco := True;
  ViaMs := GetTickCount64;
  BtnVia.Enabled := False;
  Scrivi('VIA! Tutti giocano sulla stessa combinazione. Che vinca il migliore!');
  AggiornaStato;
  Sporco := True;
end;

procedure TForm1.BtnNuovaClick(Sender: TObject);
begin
  if Srv = nil then Exit;
  if Gioco and (Length(G) > 0) then
    if MessageDlg('La partita e'' in corso. Vuoi ricominciare con una nuova combinazione? ' +
      'La classifica attuale si perde.', mtConfirmation, [mbYes, mbNo], 0) <> mrYes then Exit;
  NuovaPartita;
  BtnVia.Enabled := True;
  Scrivi('NUOVA combinazione scelta (nascosta). Premi "Via!" quando sono pronti.');
  AggiornaStato;
  AggiornaSegreto;
end;

procedure TForm1.LblSegretoClick(Sender: TObject);
begin
  MostraSegreto := not MostraSegreto;
  AggiornaSegreto;
end;

{ ---- il cuore: ogni 50 millisecondi ---- }

procedure TForm1.Timer1Timer(Sender: TObject);
var
  adesso: QWord;
begin
  adesso := GetTickCount64;
  try
    if Srv <> nil then
    begin
      Servite := 0;
      Srv.StartAccepting;      // risponde a chi bussa e torna indietro da solo
    end;
    if Sporco or (adesso - UltimoGiro >= 1000) then   // ridisegna subito se c'e' novita', altrimenti ogni secondo
    begin
      UltimoGiro := adesso;
      Sporco := False;
      AggiornaClassifica;
      AggiornaStato;
    end;
  except
    on E: Exception do
      Scrivi('Attenzione: ' + E.Message);       // un errore non deve fermare il Timer
  end;
end;

end.
