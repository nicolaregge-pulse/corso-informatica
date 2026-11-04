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

  NOVITA' v4.1 - la GARA (una modalita' in piu': la partita libera di sopra funziona come prima):
    1. Premi "Avvia server".
    2. Scegli quanti codici (di solito 5) e quanti secondi per ogni codice (di solito 180).
    3. Quando i ragazzi sono collegati premi "Inizia gara". Parte il codice 1.
    4. Ogni codice finisce da solo quando scade il tempo, oppure quando tutti hanno trovato il codice,
       oppure quando premi "Prossimo codice". Dopo una breve pausa parte il codice successivo.
    5. La "Classifica generale" a destra e' sempre aggiornata. "Fine gara" chiude tutto.
  I punteggi si calcolano in UnitGara.pas (che non conosce ne' finestre ne' rete).

  Niente thread: il Timer1 chiama la rete ogni 50 millisecondi e la finestra resta libera.
  Protocollo (una riga in, una riga fuori), identico a quello del client:
    GUESS;nome;1234  ->  WAIT | RESULT;esatte;spostate;... | WIN;... | ERR;...
    STATO;nome       ->  STATO;ATTESA;... | STATO;GIOCO;...
  Le cifre 1..6 sono i colori: 1 rosso, 2 giallo, 3 verde, 4 blu, 5 arancio, 6 porpora. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Types, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls, Grids,
  sockets, ssockets, UnitGara;

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
    { v4.1: la gara }
    LblGara: TLabel;           // scritta "GARA"
    LblCodici: TLabel;         // scritta sopra la casella dei codici
    EdCodici: TEdit;           // quanti codici ha la gara (di solito 5)
    LblSecondi: TLabel;        // scritta sopra la casella dei secondi
    EdSecondi: TEdit;          // quanti secondi ha ogni codice (di solito 180)
    BtnInizia: TButton;        // "Inizia gara"
    BtnProssimo: TButton;      // "Prossimo codice"
    BtnFine: TButton;          // "Fine gara"
    LblRound: TLabel;          // il codice in corso e il tempo che manca
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure BtnAvviaClick(Sender: TObject);
    procedure BtnViaClick(Sender: TObject);
    procedure BtnStopClick(Sender: TObject);
    procedure BtnNuovaClick(Sender: TObject);
    procedure BtnMostraClick(Sender: TObject);
    procedure BtnIniziaClick(Sender: TObject);
    procedure BtnProssimoClick(Sender: TObject);
    procedure BtnFineClick(Sender: TObject);
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
    Gara: TGara;                  // v4.1: la gara (nil = nessuna gara lanciata)
    StatoVisto: TStatoGara;       // lo stato della gara all'ultimo controllo
    RoundVisto: Integer;
    ChiusiVisti: Integer;
    procedure Scrivi(const Testo: String);
    procedure Connesso(Sender: TObject; Data: TSocketStream);
    procedure Inattivo(Sender: TObject);
    function ServiBase(const Ip, Linea: String): String;
    function Servi(const Ip, Linea: String): String;
    function GaraAttiva: Boolean;
    function RigheGara(Idx: Integer): String;
    procedure SincronizzaGara;
    procedure ImpostaIntestazioni(PerGara: Boolean);
    procedure AggiornaClassificaGara;
    procedure AggiornaRound;
    function NomeCodice(const Codice: String): String;
    function Trova(const Nome: String; Crea: Boolean): Integer;
    function Sintesi(i: Integer): String;
    function Collegati: Integer;
    procedure AggiornaStato;
    procedure AggiornaSegreto;
    procedure AggiornaClassifica;
    procedure NuovaPartita;
  public
    Avviato: Boolean;                 // True quando FormCreate e' gia' partita
    property LaGara: TGara read Gara; // v4.1: per le prove (e per guardare la gara da fuori)
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
  Gara := nil;
  StatoVisto := sgFerma;
  RoundVisto := 0;
  ChiusiVisti := 0;
  Griglia.ColCount := 6;
  Griglia.RowCount := 1;
  Griglia.FixedRows := 1;
  Griglia.FixedCols := 0;
  ImpostaIntestazioni(False);
  EdCodici.Text := IntToStr(CODICI_DEFAULT);
  EdSecondi.Text := IntToStr(SECONDI_DEFAULT);
  BtnInizia.Enabled := False;
  BtnProssimo.Enabled := False;
  BtnFine.Enabled := False;
  AggiornaRound;
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
  if not Assigned(BtnInizia.OnClick) then BtnInizia.OnClick := @BtnIniziaClick;
  if not Assigned(BtnProssimo.OnClick) then BtnProssimo.OnClick := @BtnProssimoClick;
  if not Assigned(BtnFine.OnClick) then BtnFine.OnClick := @BtnFineClick;
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
  FreeAndNil(Gara);
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

function TFormServer.ServiBase(const Ip, Linea: String): String;
var
  cmd, nome, guess: String;
  i, esa, spo, gi, n2, b2: Integer;
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
    if GaraAttiva then Gara.Registra(nome, Int64(GetTickCount64));   // v4.1: anche la gara sa che c'e'
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
      if GaraAttiva and (Gara.Stato = sgRound) then
      begin
        gi := Gara.Cerca(nome);                 // la gara fa i suoi conti (punti), qui sopra restano quelli di sempre
        if gi >= 0 then Gara.Tentativo(gi, guess, Int64(GetTickCount64), n2, b2);
      end;
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

{ ---- v4.1: la gara ---- }

function TFormServer.GaraAttiva: Boolean;
begin
  Result := (Gara <> nil) and (Gara.Stato <> sgFerma);
end;

{ Il nome dei 4 colori del codice, per il registro del prof }
function TFormServer.NomeCodice(const Codice: String): String;
var
  i: Integer;
begin
  Result := '';
  for i := 1 to Length(Codice) do
    if Codice[i] in ['1'..'6'] then
      Result := Result + NOMI_COLORI[Ord(Codice[i]) - 48] + ' ';
  Result := Trim(Result);
end;

{ Le righe NUOVE della v4.1, da mettere SOTTO la riga di sempre (separate da "a capo"):
    ROUND;k;N;secondi
    CLASSIFICA;il tuo posto;i tuoi punti;quanti giocatori;nome del primo;punti del primo
    FINEGARA;il tuo posto;i tuoi punti;quanti giocatori      (solo a gara finita)
  Vengono con OGNI risposta (STATO e GUESS): il client chiede lo STATO ogni 3 secondi, quindi la
  classifica si rinnova almeno ogni 3 secondi e a ogni tentativo. }
function TFormServer.RigheGara(Idx: Integer): String;
var
  ord_: TElencoIndici;
  Adesso: Int64;
  pos, tot, quanti, rimasti: Integer;
  primo: String;
  puntiPrimo: Integer;
begin
  Result := '';
  if (not GaraAttiva) or (Idx < 0) or (Idx >= Gara.Giocatori) then Exit;
  Adesso := Int64(GetTickCount64);
  pos := Gara.Posizione(Idx);
  tot := Gara.Totale(Idx);
  quanti := Gara.Giocatori;
  ord_ := Gara.Ordine;
  primo := '-';
  puntiPrimo := 0;
  if Length(ord_) > 0 then
  begin
    primo := Gara.Giocatore[ord_[0]].Nome;
    puntiPrimo := Gara.Totale(ord_[0]);
  end;
  case Gara.Stato of
    sgRound:
      begin
        rimasti := Gara.SecondiRimasti(Adesso);
        Result := 'ROUND;' + IntToStr(Gara.RoundCorrente) + ';' + IntToStr(Gara.NumCodici) + ';' + IntToStr(rimasti) + #10;
      end;
    sgPausa:
      Result := 'ROUND;' + IntToStr(Gara.RoundCorrente) + ';' + IntToStr(Gara.NumCodici) + ';0' + #10;
  end;
  Result := Result + 'CLASSIFICA;' + IntToStr(pos) + ';' + IntToStr(tot) + ';' + IntToStr(quanti) + ';' +
    primo + ';' + IntToStr(puntiPrimo);
  if Gara.Stato = sgFinita then
    Result := Result + #10 + 'FINEGARA;' + IntToStr(pos) + ';' + IntToStr(tot) + ';' + IntToStr(quanti);
end;

function TFormServer.Servi(const Ip, Linea: String): String;
var
  nome: String;
  gi: Integer;
begin
  Result := ServiBase(Ip, Linea);
  // se c'e' una gara, sotto la riga di sempre si aggiungono le righe della gara (un client vecchio non le legge)
  if GaraAttiva and (Copy(Result, 1, 3) <> 'ERR') then
  begin
    nome := PulisciNome(Campo(Linea, 2));
    gi := Gara.Cerca(nome);
    if gi >= 0 then Result := Result + #10 + RigheGara(gi);
  end;
end;

procedure TFormServer.ImpostaIntestazioni(PerGara: Boolean);
begin
  if PerGara then
  begin
    Griglia.Cells[0, 0] := 'Pos.';
    Griglia.Cells[1, 0] := 'Nome';
    Griglia.Cells[2, 0] := 'Round';
    Griglia.Cells[3, 0] := 'Totale';
    Griglia.Cells[4, 0] := 'Tent.';
    Griglia.Cells[5, 0] := 'Stato';
    Griglia.ColWidths[0] := 34;
    Griglia.ColWidths[1] := 104;
    Griglia.ColWidths[2] := 52;
    Griglia.ColWidths[3] := 56;
    Griglia.ColWidths[4] := 46;
    Griglia.ColWidths[5] := 84;
    LblClassifica.Caption := 'Classifica generale (Round = punti di questo codice, Totale = tutti i codici)';
  end
  else
  begin
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
    LblClassifica.Caption := 'Classifica';
  end;
end;

{ La scritta grande: che codice e', quanto tempo manca }
procedure TFormServer.AggiornaRound;
var
  Adesso: Int64;
  Sec: Integer;
  ord_: TElencoIndici;
begin
  if Gara = nil then
  begin
    LblRound.Caption := 'Nessuna gara in corso';
    Exit;
  end;
  Adesso := Int64(GetTickCount64);
  case Gara.Stato of
    sgRound:
      begin
        Sec := Gara.SecondiRimasti(Adesso);
        LblRound.Caption := 'CODICE ' + IntToStr(Gara.RoundCorrente) + ' di ' + IntToStr(Gara.NumCodici) +
          '   tempo ' + IntToStr(Sec div 60) + ':' + Zeri(Sec mod 60, 2) +
          '   hanno risolto: ' + IntToStr(Gara.Risolti);
      end;
    sgPausa:
      LblRound.Caption := 'Codice ' + IntToStr(Gara.RoundCorrente) + ' finito. Prossimo tra ' +
        IntToStr(Gara.SecondiPausaRimasti(Adesso)) + ' s';
    sgFinita:
      begin
        ord_ := Gara.Ordine;
        if Length(ord_) > 0 then
          LblRound.Caption := 'GARA FINITA - primo: ' + Gara.Giocatore[ord_[0]].Nome + ' (' +
            IntToStr(Gara.Totale(ord_[0])) + ' punti)'
        else
          LblRound.Caption := 'GARA FINITA';
      end;
  else
    LblRound.Caption := 'Nessuna gara in corso';
  end;
end;

{ La classifica generale della gara: posto, nome, punti del round, totale, tentativi, stato }
procedure TFormServer.AggiornaClassificaGara;
var
  ord_: TElencoIndici;
  j, ix, risolti: Integer;
  Adesso: Int64;
  stato: String;
begin
  Adesso := Int64(GetTickCount64);
  ord_ := Gara.Ordine;
  Griglia.BeginUpdate;
  try
    Griglia.RowCount := Length(ord_) + 1;
    for j := 0 to High(ord_) do
    begin
      ix := ord_[j];
      with Gara.Giocatore[ix] do
      begin
        if Gara.Stato = sgFinita then
          stato := 'finito'
        else if Risolto then
          stato := 'risolto ' + IntToStr(PosVelocita) + 'o'
        else if Gara.Stato = sgPausa then
          stato := 'non risolto'
        else if TentRound > 0 then
          stato := 'sta provando'
        else
          stato := 'pronto';
        if (Gara.Stato <> sgFinita) and not Gara.Collegato(ix, Adesso) then stato := 'scollegato';
        Griglia.Cells[0, j + 1] := IntToStr(Gara.Posizione(ix));
        Griglia.Cells[1, j + 1] := Nome;
        Griglia.Cells[2, j + 1] := IntToStr(Gara.PuntiRound(ix));
        Griglia.Cells[3, j + 1] := IntToStr(Gara.Totale(ix));
        Griglia.Cells[4, j + 1] := IntToStr(Gara.TentativiTotali(ix));
        Griglia.Cells[5, j + 1] := stato;
      end;
    end;
  finally
    Griglia.EndUpdate;
  end;
  risolti := Gara.Risolti;
  LblGiocatori.Caption := 'Collegati: ' + IntToStr(Collegati) + '     Hanno risolto questo codice: ' + IntToStr(risolti);
end;

{ Confronta la gara con quello che il server aveva visto l'ultima volta: se e' cambiato qualcosa
  (round finito, round nuovo, gara finita) lo scrive nel registro e sistema i bottoni. }
procedure TFormServer.SincronizzaGara;
var
  i, j: Integer;
  ord_: TElencoIndici;
  motivo, riga: String;
begin
  if Gara = nil then Exit;
  if ChiusiVisti <> Gara.RoundChiusi then
  begin
    case Gara.UltimoMotivo of
      mfTempo: motivo := 'e'' scaduto il tempo';
      mfTutti: motivo := 'tutti hanno trovato il codice';
      mfDocente: motivo := 'il Prof ha detto basta';
    else
      motivo := '';
    end;
    Scrivi('=== CODICE ' + IntToStr(Gara.RoundChiusi) + ' FINITO (' + motivo + '). Il codice era: ' +
      NomeCodice(Gara.CodiceUltimoChiuso) + ' ===');
    ord_ := Gara.Ordine;
    for j := 0 to High(ord_) do
      if j < 3 then
      begin
        riga := IntToStr(Gara.Posizione(ord_[j])) + 'o ' + Gara.Giocatore[ord_[j]].Nome + ': ' +
          IntToStr(Gara.Totale(ord_[j])) + ' punti';
        Scrivi('   ' + riga);
      end;
    ChiusiVisti := Gara.RoundChiusi;
    Sporco := True;
  end;
  if (Gara.Stato <> StatoVisto) or (Gara.RoundCorrente <> RoundVisto) then
  begin
    case Gara.Stato of
      sgRound:
        begin
          Segreto := Gara.Segreto;                // la finestra e il resto del server usano questo codice
          Gioco := True;
          ViaMs := GetTickCount64;
          for i := 0 to High(G) do                // il vecchio protocollo conta i tentativi di QUESTO codice
          begin
            G[i].Tent := 0;
            G[i].Secondi := 0;
            G[i].Risolto := False;
          end;
          MostraSegreto := False;
          Scrivi('=== CODICE ' + IntToStr(Gara.RoundCorrente) + ' di ' + IntToStr(Gara.NumCodici) +
            ': VIA! (codice nascosto, ' + IntToStr(Gara.SecondiRound) + ' secondi) ===');
          BtnProssimo.Enabled := True;
          BtnFine.Enabled := True;
        end;
      sgPausa:
        begin
          Gioco := False;
          Scrivi('Pausa di ' + IntToStr(PausaTraRoundSec) + ' secondi. Per saltarla premi "Prossimo codice".');
        end;
      sgFinita:
        begin
          Gioco := False;
          Scrivi('=== GARA FINITA! ===');
          ord_ := Gara.Ordine;
          for j := 0 to High(ord_) do
            if j < 3 then
              Scrivi('   ' + IntToStr(Gara.Posizione(ord_[j])) + 'o ' + Gara.Giocatore[ord_[j]].Nome + ': ' +
                IntToStr(Gara.Totale(ord_[j])) + ' punti');
          BtnProssimo.Enabled := False;
          BtnFine.Enabled := False;
          BtnInizia.Enabled := Srv <> nil;        // si puo' lanciare un'altra gara
          EdCodici.Enabled := True;
          EdSecondi.Enabled := True;
          BtnVia.Enabled := False;                // la partita libera riparte con "Nuova combinazione"
          BtnStop.Enabled := False;
          BtnNuova.Enabled := Srv <> nil;
        end;
    end;
    StatoVisto := Gara.Stato;
    RoundVisto := Gara.RoundCorrente;
    AggiornaSegreto;
    Sporco := True;
  end;
end;

procedure TFormServer.BtnIniziaClick(Sender: TObject);
var
  n, sec, i: Integer;
  Adesso: Int64;
begin
  if Srv = nil then
  begin
    ShowMessage('Prima premi "Avvia server".');
    Exit;
  end;
  if GaraAttiva and (Gara.Stato in [sgRound, sgPausa]) then Exit;
  n := StrToIntDef(Trim(EdCodici.Text), 0);
  sec := StrToIntDef(Trim(EdSecondi.Text), 0);
  if (n < CODICI_MIN) or (n > CODICI_MAX) then
  begin
    ShowMessage('Il numero di codici deve essere un numero tra ' + IntToStr(CODICI_MIN) + ' e ' +
      IntToStr(CODICI_MAX) + '. Di solito si usa ' + IntToStr(CODICI_DEFAULT) + '.');
    Exit;
  end;
  if (sec < SECONDI_MIN) or (sec > SECONDI_MAX) then
  begin
    ShowMessage('I secondi per ogni codice devono essere tra ' + IntToStr(SECONDI_MIN) + ' e ' +
      IntToStr(SECONDI_MAX) + '. Di solito si usa ' + IntToStr(SECONDI_DEFAULT) + '.');
    Exit;
  end;
  if Gioco and (Gara = nil) then
    if MessageDlg('La partita libera e'' in corso. Vuoi fermarla e lanciare la gara?',
      mtConfirmation, [mbYes, mbNo], 0) <> mrYes then Exit;
  Adesso := Int64(GetTickCount64);
  FreeAndNil(Gara);
  Gara := TGara.Create;
  Gara.NumCodici := n;
  Gara.SecondiRound := sec;
  for i := 0 to High(G) do                     // chi e' gia' collegato entra subito in classifica
    if GetTickCount64 - G[i].Ultimo <= FUORI_LINEA_MS then Gara.Registra(G[i].Nome, Adesso);
  StatoVisto := sgFerma;
  RoundVisto := 0;
  ChiusiVisti := 0;
  ImpostaIntestazioni(True);
  EdCodici.Enabled := False;
  EdSecondi.Enabled := False;
  BtnInizia.Enabled := False;
  BtnVia.Enabled := False;
  BtnStop.Enabled := False;
  BtnNuova.Enabled := False;
  Scrivi('*** GARA LANCIATA: ' + IntToStr(n) + ' codici, ' + IntToStr(sec) + ' secondi per ogni codice ***');
  Gara.Inizia(Adesso);
  SincronizzaGara;
  AggiornaStato;
  AggiornaRound;
  Sporco := True;
end;

procedure TFormServer.BtnProssimoClick(Sender: TObject);
begin
  if (Gara = nil) or not (Gara.Stato in [sgRound, sgPausa]) then Exit;
  Gara.ProssimoCodice(Int64(GetTickCount64));
  SincronizzaGara;
  AggiornaRound;
end;

procedure TFormServer.BtnFineClick(Sender: TObject);
begin
  if (Gara = nil) or not (Gara.Stato in [sgRound, sgPausa]) then Exit;
  if MessageDlg('Vuoi chiudere la gara adesso? Resta visibile la classifica finale.',
    mtConfirmation, [mbYes, mbNo], 0) <> mrYes then Exit;
  Gara.Ferma(Int64(GetTickCount64));
  SincronizzaGara;
  AggiornaRound;
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
  else if GaraAttiva and (Gara.Stato in [sgRound, sgPausa]) then
    LblStato.Caption := 'ACCESO (porta ' + EdPorta.Text + ') - GARA IN CORSO'
  else if GaraAttiva and (Gara.Stato = sgFinita) then
    LblStato.Caption := 'ACCESO (porta ' + EdPorta.Text + ') - gara finita'
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
  if Gara <> nil then      // v4.1: durante e dopo la gara si vede la classifica generale
  begin
    AggiornaClassificaGara;
    Exit;
  end;
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
  if Gara <> nil then      // si torna alla partita libera: la gara (e la sua classifica) si chiude
  begin
    FreeAndNil(Gara);
    ImpostaIntestazioni(False);
    EdCodici.Enabled := True;
    EdSecondi.Enabled := True;
    BtnProssimo.Enabled := False;
    BtnFine.Enabled := False;
    AggiornaRound;
  end;
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
  BtnInizia.Enabled := True;
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
  if (Srv = nil) or Gioco or GaraAttiva then Exit;
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
  if (Srv = nil) or not Gioco or GaraAttiva then Exit;
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
    if Gara <> nil then
    begin
      Gara.Tick(Int64(adesso));        // v4.1: fa finire e partire i round
      SincronizzaGara;
    end;
    if Sporco or (adesso - UltimoGiro >= 1000) then   // ridisegna subito se c'e' novita', altrimenti ogni secondo
    begin
      UltimoGiro := adesso;
      Sporco := False;
      AggiornaClassifica;
      AggiornaStato;
      AggiornaRound;
    end;
  except
    on E: Exception do
      Scrivi('Attenzione: ' + E.Message);       // un errore non deve fermare il Timer
  end;
end;

end.
