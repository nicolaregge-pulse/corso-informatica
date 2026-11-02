unit UnitServer;
{ MASTERMIND BELLO - SERVER CON FINESTRA, TUTTO IN UN FILE (per il prof) + UnitServer.lfm.

  Il PC del prof pensa UNA combinazione segreta per tutta la classe, riceve i tentativi
  dei ragazzi e tiene la classifica. Tutto con il mouse:
    1. Premi "Avvia server" (la porta e' 5050: non toccarla).
    2. Di' ai ragazzi l'indirizzo scritto in grande (IP e porta).
    3. Quando sono collegati, premi "Via!". Con "Stop" metti in pausa (la classifica resta).
    4. Per ricominciare con un'altra combinazione: "Nuova combinazione".
  La combinazione ha 4 colori che possono ripetersi: si vede come 4 pioli sulla tavola di
  legno quando premi "Mostra il codice".

  Niente thread: il Timer1 chiama la rete ogni 50 millisecondi e la finestra resta libera.
  Protocollo (una riga in, una riga fuori), identico a quello del client:
    GUESS;nome;1234  ->  WAIT | RESULT;esatte;spostate;... | WIN;... | ERR;...
    STATO;nome       ->  STATO;ATTESA;... | STATO;GIOCO;...
  Le cifre 1..6 sono i colori: 1 rosso, 2 giallo, 3 verde, 4 blu, 5 arancio, 6 porpora. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Types, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls, Grids,
  sockets, ssockets;

type
  TGioc = record            // un ragazzo
    Nome: String;
    Ip: String;             // indirizzo IP del PC del ragazzo
    Tent: Integer;          // tentativi fatti
    Secondi: Integer;       // secondi dal Via alla vittoria
    Risolto: Boolean;
    Ultimo: QWord;          // ultimo istante in cui si e' fatto sentire (millisecondi)
  end;

  TFormServer = class(TForm)
    LblPorta: TLabel;          // scritta sopra la porta
    EdPorta: TEdit;            // la porta, di solito 5050
    BtnAvvia: TButton;         // "Avvia server"
    LblStato: TLabel;          // dice se il server e' acceso
    LblIp: TLabel;             // l'IP di questo PC
    LblIndirizzo: TLabel;      // scritta sopra l'indirizzo da dire ai ragazzi
    EdIndirizzo: TEdit;        // IP:porta in grande, pronto da copiare (Ctrl+C)
    BtnVia: TButton;           // "Via!"
    BtnStop: TButton;          // "Stop": pausa
    BtnNuova: TButton;         // "Nuova combinazione"
    PbSegreto: TPaintBox;      // la tavola di legno con i 4 pioli del codice segreto
    BtnMostra: TButton;        // mostra / nasconde il codice
    LblGiocatori: TLabel;      // quanti collegati / vinto / stanno provando
    LblClassifica: TLabel;     // scritta "Classifica"
    LblRegistro: TLabel;       // scritta "Registro"
    Griglia: TStringGrid;      // la classifica con l'elenco dei giocatori
    MemoRegistro: TMemo;       // collegamenti e tentativi in tempo reale
    Timer1: TTimer;            // ogni 50 ms: rete e classifica
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure BtnAvviaClick(Sender: TObject);
    procedure BtnViaClick(Sender: TObject);
    procedure BtnStopClick(Sender: TObject);
    procedure BtnNuovaClick(Sender: TObject);
    procedure BtnMostraClick(Sender: TObject);
    procedure EdPortaChange(Sender: TObject);
    procedure PbSegretoPaint(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    Srv: TInetServer;             // la rete (nil = spento)
    Servite: Integer;             // richieste servite nel Tick in corso
    G: array of TGioc;            // tutti i ragazzi visti
    Segreto: String;              // la combinazione, 4 cifre da 1 a 6 (si possono ripetere)
    Gioco: Boolean;               // False = si aspetta il Via (o pausa), True = si gioca
    ViaMs: QWord;                 // istante del primo Via (0 = non ancora dato)
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
  FormServer: TFormServer;
  FondoSegreto, BufSegreto: TBitmap;  // il legno del pannello del codice (disegnato una volta sola, in grande) e la tela su cui si disegna

implementation

{$R *.lfm}

const
  FUORI_LINEA_MS = 20000;   // dopo 20 secondi senza notizie un ragazzo risulta "scollegato"
  MAX_PER_TICK = 12;        // richieste servite al massimo ad ogni Tick
  LARG_SEGRETO = 380;       // misure del pannello di legno con il codice segreto (pixel di progetto, schermo al 100%)
  ALT_SEGRETO = 64;
  // sei colori, in ordine 1..6: rosso, giallo, verde, blu, arancio, porpora (formato BGR)
  COLORI: array[1..6] of Integer = ($002828DC, $001EC8F0, $003CA028, $00DC5A28, $001E82F0, $00AA328C);
  NOMI_COLORI: array[1..6] of String = ('rosso', 'giallo', 'verde', 'blu', 'arancio', 'porpora');

{$I ../Comune/DisegnoMastermind.inc}

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

{ Conta i piolini di risposta con lo STESSO conteggio del client (anche con colori ripetuti):
  Esatte = giuste al posto giusto (nere); Spostate = colore giusto al posto sbagliato (bianche). }
procedure Valuta(const Segr, Tent: String; out Esatte, Spostate: Integer);
var
  CS, CP: array[1..6] of Integer;
  i: Integer;
begin
  for i := 1 to 6 do
  begin
    CS[i] := 0;
    CP[i] := 0;
  end;
  Esatte := 0;
  for i := 1 to 4 do
    if Segr[i] = Tent[i] then
      Inc(Esatte)
    else
    begin
      Inc(CS[Ord(Segr[i]) - 48]);
      Inc(CP[Ord(Tent[i]) - 48]);
    end;
  Spostate := 0;
  for i := 1 to 6 do
    if CS[i] < CP[i] then Inc(Spostate, CS[i]) else Inc(Spostate, CP[i]);
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

{ ---- il pannello di legno con il codice segreto ---- }

procedure PreparaFondoSegreto(Ppi: Integer);
begin
  if ImpostaScala(Ppi) then
  begin
    FreeAndNil(FondoSegreto);
    FreeAndNil(BufSegreto);
  end;
  if FondoSegreto = nil then
  begin
    FondoSegreto := TBitmap.Create;
    FondoSegreto.Width := Sc(LARG_SEGRETO);
    FondoSegreto.Height := Sc(ALT_SEGRETO);
    DisegnaLegno(FondoSegreto.Canvas, FondoSegreto.Width, FondoSegreto.Height, 7);   // stesso legno del client
    BufSegreto := TBitmap.Create;
    BufSegreto.Width := FondoSegreto.Width;
    BufSegreto.Height := FondoSegreto.Height;
  end;
end;

procedure TFormServer.PbSegretoPaint(Sender: TObject);
var
  B: TCanvas;
  I, Cx, Cy: Integer;
begin
  PreparaFondoSegreto(PixelsPerInch);
  B := BufSegreto.Canvas;
  B.Draw(0, 0, FondoSegreto);
  Cy := Sc(ALT_SEGRETO div 2);
  for I := 0 to 3 do
  begin
    Cx := Sc(LARG_SEGRETO div 2 - 105 + I * 70);
    if (Srv <> nil) and (Length(Segreto) = 4) and MostraSegreto then
    begin
      DisegnaBuco(B, Cx, Cy, Sc(18));
      DisegnaPiolo(B, Cx, Cy, Sc(17), COLORI[Ord(Segreto[I + 1]) - 48]);
    end
    else
    begin
      DisegnaBuco(B, Cx, Cy, Sc(18));                 // nascosto: buco con il punto interrogativo
      B.Brush.Style := bsClear;
      B.Font.Name := 'Arial';
      B.Font.Height := -Sc(22);
      B.Font.Style := [fsBold];
      B.Font.Quality := fqCleartype;
      B.Font.Color := MioColore(236, 194, 134);
      B.TextOut(Cx - B.TextWidth('?') div 2, Cy - B.TextHeight('?') div 2, '?');
      B.Brush.Style := bsSolid;
    end;
  end;
  RiduciSu(PbSegreto.Canvas, Rect(0, 0, PbSegreto.Width, PbSegreto.Height), BufSegreto);
end;

{ ---- avvio e chiusura ---- }

procedure TFormServer.FormCreate(Sender: TObject);
begin
  Avviato := True;
  Randomize;
  Srv := nil;
  Gioco := False;
  ViaMs := 0;
  Sporco := True;
  MostraSegreto := False;
  UltimoGiro := 0;
  Griglia.ColCount := 6;
  Griglia.RowCount := 1;
  Griglia.FixedRows := 1;
  Griglia.FixedCols := 0;
  Griglia.Cells[0, 0] := 'Posto';
  Griglia.Cells[1, 0] := 'Nome';
  Griglia.Cells[2, 0] := 'Tentativi';
  Griglia.Cells[3, 0] := 'Tempo';
  Griglia.Cells[4, 0] := 'Stato';
  Griglia.Cells[5, 0] := 'IP';
  Griglia.ColWidths[0] := 36;
  Griglia.ColWidths[1] := 92;
  Griglia.ColWidths[2] := 48;
  Griglia.ColWidths[3] := 44;
  Griglia.ColWidths[4] := 76;
  Griglia.ColWidths[5] := 76;
  IpPc := MMIpDelPc;
  if IpPc = '' then
    LblIp.Caption := 'IP di questo PC: non si ricava'
  else
    LblIp.Caption := 'IP di questo PC: ' + IpPc;
  EdPortaChange(nil);
  AggiornaStato;
  AggiornaSegreto;
  Scrivi('Benvenuto! Premi "Avvia server" per cominciare.');
end;

{ A prova di errore: se il form e' stato caricato senza i collegamenti dei bottoni
  li colleghiamo da qui, dopo che la finestra e' stata costruita. }
procedure TFormServer.AfterConstruction;
begin
  inherited AfterConstruction;
  if not Assigned(BtnAvvia.OnClick) then BtnAvvia.OnClick := @BtnAvviaClick;
  if not Assigned(BtnVia.OnClick) then BtnVia.OnClick := @BtnViaClick;
  if not Assigned(BtnStop.OnClick) then BtnStop.OnClick := @BtnStopClick;
  if not Assigned(BtnNuova.OnClick) then BtnNuova.OnClick := @BtnNuovaClick;
  if not Assigned(BtnMostra.OnClick) then BtnMostra.OnClick := @BtnMostraClick;
  if not Assigned(PbSegreto.OnClick) then PbSegreto.OnClick := @BtnMostraClick;
  if not Assigned(PbSegreto.OnPaint) then PbSegreto.OnPaint := @PbSegretoPaint;
  if not Assigned(EdPorta.OnChange) then EdPorta.OnChange := @EdPortaChange;
  if not Assigned(Timer1.OnTimer) then Timer1.OnTimer := @Timer1Timer;
  if not Assigned(OnDestroy) then OnDestroy := @FormDestroy;
  if not Avviato then FormCreate(nil);
end;

procedure TFormServer.FormDestroy(Sender: TObject);
begin
  Timer1.Enabled := False;
  FreeAndNil(Srv);
end;

procedure TFormServer.EdPortaChange(Sender: TObject);
begin
  if EdIndirizzo = nil then Exit;     // mentre Lazarus carica la finestra la casella non esiste ancora
  if IpPc <> '' then
    EdIndirizzo.Text := IpPc + ':' + Trim(EdPorta.Text)
  else
    EdIndirizzo.Text := '(IP non ricavato):' + Trim(EdPorta.Text);
end;

{ ---- registro ---- }

procedure TFormServer.Scrivi(const Testo: String);
begin
  if MemoRegistro.Lines.Count > 1500 then
    while MemoRegistro.Lines.Count > 1000 do MemoRegistro.Lines.Delete(0);
  MemoRegistro.Lines.Add(FormatDateTime('hh:nn:ss', Now) + '  ' + Testo);
  MemoRegistro.SelStart := MemoRegistro.GetTextLen;     // scorre in fondo
end;

{ ---- la rete: niente thread, il Timer1 la chiama ogni 50 ms ---- }

procedure TFormServer.Inattivo(Sender: TObject);
begin
  Srv.StopAccepting;            // nessuno bussa: torniamo alla finestra
end;

procedure TFormServer.Connesso(Sender: TObject; Data: TSocketStream);
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
function TFormServer.Trova(const Nome: String; Crea: Boolean): Integer;
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
function TFormServer.Sintesi(i: Integer): String;
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

function TFormServer.Servi(const Ip, Linea: String): String;
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
  begin
    i := Trova(nome, True);
    G[i].Ip := Ip;
  end;
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

function TFormServer.Collegati: Integer;
var
  i: Integer;
begin
  Result := 0;
  for i := 0 to High(G) do
    if GetTickCount64 - G[i].Ultimo <= FUORI_LINEA_MS then Inc(Result);
end;

{ ---- scritte e classifica ---- }

procedure TFormServer.AggiornaStato;
begin
  if Srv = nil then
    LblStato.Caption := 'Server SPENTO'
  else if Gioco then
    LblStato.Caption := 'ACCESO (porta ' + EdPorta.Text + ') - SI GIOCA'
  else if ViaMs > 0 then
    LblStato.Caption := 'ACCESO (porta ' + EdPorta.Text + ') - IN PAUSA'
  else
    LblStato.Caption := 'ACCESO (porta ' + EdPorta.Text + ') - aspetto il Via';
end;

procedure TFormServer.AggiornaSegreto;
begin
  if MostraSegreto then
    BtnMostra.Caption := 'Nascondi il codice'
  else
    BtnMostra.Caption := 'Mostra il codice';
  PbSegreto.Invalidate;
end;

{ Chiave per ordinare: prima chi ha vinto (meno tentativi, meno secondi), poi chi prova, poi gli altri }
function ChiaveDi(const R: TGioc): String;
begin
  if R.Risolto then Result := '0' + Zeri(R.Tent, 6) + Zeri(R.Secondi, 8)
  else if R.Tent > 0 then Result := '1' + Zeri(R.Tent, 6) + Zeri(0, 8)
  else Result := '2' + Zeri(0, 14);
end;

procedure TFormServer.AggiornaClassifica;
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
          stato := 'ha vinto';
          if chiave = ultimaChiave then posto := ultimaPos else posto := i + 1;   // pari merito
          ultimaChiave := chiave;
          ultimaPos := posto;
          Griglia.Cells[0, i + 1] := IntToStr(posto);
          Griglia.Cells[3, i + 1] := IntToStr(Secondi) + ' s';
        end
        else
        begin
          if Tent > 0 then
          begin
            Inc(provano);
            stato := 'sta provando';
          end
          else
            stato := 'pronto';
          Griglia.Cells[0, i + 1] := '-';
          Griglia.Cells[3, i + 1] := '-';
        end;
        if GetTickCount64 - Ultimo > FUORI_LINEA_MS then
          if Tent > 0 then stato := stato + ' (scollegato)' else stato := 'scollegato';
        Griglia.Cells[1, i + 1] := Nome;
        Griglia.Cells[2, i + 1] := IntToStr(Tent);
        Griglia.Cells[4, i + 1] := stato;
        Griglia.Cells[5, i + 1] := Ip;
      end;
  finally
    Griglia.EndUpdate;
  end;
  LblGiocatori.Caption := 'Collegati: ' + IntToStr(Collegati) +
    '     Hanno vinto: ' + IntToStr(vinti) + '     Stanno provando: ' + IntToStr(provano);
end;

{ ---- i bottoni ---- }

procedure TFormServer.NuovaPartita;
var
  i: Integer;
begin
  Segreto := '';
  for i := 1 to 4 do Segreto := Segreto + IntToStr(Random(6) + 1);   // 4 colori a caso, anche ripetuti
  Gioco := False;
  ViaMs := 0;
  SetLength(G, 0);          // i ragazzi ricompaiono da soli al loro prossimo messaggio
  Sporco := True;
end;

procedure TFormServer.BtnAvviaClick(Sender: TObject);
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
  BtnStop.Enabled := False;
  BtnNuova.Enabled := True;
  BtnMostra.Enabled := True;
  EdPortaChange(nil);
  Scrivi('Server acceso sulla porta ' + IntToStr(porta) + '. Codice scelto (nascosto).');
  if IpPc <> '' then
    Scrivi('Di'' ai ragazzi di scrivere: ' + IpPc + ':' + IntToStr(porta));
  Scrivi('Se Windows chiede "Consenti accesso", clicca "Consenti accesso".');
  Timer1.Enabled := True;
  AggiornaStato;
  AggiornaSegreto;
end;

procedure TFormServer.BtnViaClick(Sender: TObject);
begin
  if (Srv = nil) or Gioco then Exit;
  Gioco := True;
  if ViaMs = 0 then ViaMs := GetTickCount64;   // dopo uno Stop il tempo continua dal primo Via
  BtnVia.Enabled := False;
  BtnStop.Enabled := True;
  Scrivi('VIA! Tutti giocano sullo stesso codice. Che vinca il migliore!');
  AggiornaStato;
  Sporco := True;
end;

procedure TFormServer.BtnStopClick(Sender: TObject);
begin
  if (Srv = nil) or not Gioco then Exit;
  Gioco := False;
  BtnStop.Enabled := False;
  BtnVia.Enabled := True;
  Scrivi('STOP. Pausa: i tentativi non contano. La classifica resta. Premi "Via!" per ripartire.');
  AggiornaStato;
  Sporco := True;
end;

procedure TFormServer.BtnNuovaClick(Sender: TObject);
begin
  if Srv = nil then Exit;
  if (Gioco or (ViaMs > 0)) and (Length(G) > 0) then
    if MessageDlg('La partita e'' in corso. Vuoi ricominciare con un nuovo codice? ' +
      'La classifica attuale si perde.', mtConfirmation, [mbYes, mbNo], 0) <> mrYes then Exit;
  NuovaPartita;
  BtnVia.Enabled := True;
  BtnStop.Enabled := False;
  Scrivi('NUOVO codice scelto (nascosto). Premi "Via!" quando sono pronti.');
  AggiornaStato;
  AggiornaSegreto;
end;

procedure TFormServer.BtnMostraClick(Sender: TObject);
begin
  if Srv = nil then Exit;
  MostraSegreto := not MostraSegreto;
  AggiornaSegreto;
end;

{ ---- il cuore: ogni 50 millisecondi ---- }

procedure TFormServer.Timer1Timer(Sender: TObject);
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
