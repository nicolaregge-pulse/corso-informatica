unit Unit1;
{ MASTERMIND 2.0 - IL SERVER CON LA FINESTRA (per il prof).

  Il PC del prof pensa UNA combinazione segreta per tutta la classe, riceve i
  tentativi dei ragazzi e tiene la classifica. Tutto con il mouse:
    1. Premi "Avvia server" (la porta e' 5050: non toccarla).
    2. Dai ai ragazzi l'indirizzo che compare nella casella "Da dire ai ragazzi".
    3. Quando sono collegati, premi "Via!".
    4. Per ricominciare con un'altra combinazione: "Nuova combinazione".

  Le parti difficili (rete, protocollo, classifica) stanno nei file mm_logica,
  mm_file e mm_tcp_poll: qui c'e' solo la finestra.
  Niente thread: il Timer1 chiama la rete ogni 50 millisecondi e la finestra
  resta sempre libera. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls, Grids,
  mm_logica, mm_file, mm_tcp_poll;

type
  TVisto = record
    Nome: String;
    Ultimo: QWord;        // ultimo istante in cui si e' fatto sentire (millisecondi)
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
    Timer1: TTimer;            // ogni 50 ms: rete, file e classifica
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure BtnAvviaClick(Sender: TObject);
    procedure BtnViaClick(Sender: TObject);
    procedure BtnNuovaClick(Sender: TObject);
    procedure EdPortaChange(Sender: TObject);
    procedure LblSegretoClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    Tab: TMMTabella;              // il cervello: segreto, tentativi, classifica
    FS: TMMFileServer;            // il modo "file" (cartella condivisa)
    Srv: TMMTcpServerPoll;        // il modo "rete"
    Visti: array of TVisto;       // chi si e' fatto sentire dalla rete
    IpPc: String;
    Cartella: String;
    Sporco: Boolean;              // True = c'e' qualcosa di nuovo da ridisegnare
    MostraSegreto: Boolean;
    UltimoGiro, UltimoPoll: QWord;
    UltimoRanking: String;
    procedure Scrivi(const Testo: String);
    procedure RichiestaArrivata(const Ip, Linea, Risposta: String);
    function Visto(const Nome: String): Boolean;   // True se e' la prima volta
    function Collegati: Integer;
    procedure AggiornaStato;
    procedure AggiornaSegreto;
    procedure AggiornaClassifica;
    procedure NuovaPartita;
  public
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

const
  FUORI_LINEA_MS = 20000;   // dopo 20 secondi senza notizie un ragazzo risulta "scollegato"

function Zeri(N, Larghezza: Integer): String;
begin
  Result := IntToStr(N);
  while Length(Result) < Larghezza do Result := '0' + Result;
end;

{ ---- avvio e chiusura ---- }

procedure TForm1.FormCreate(Sender: TObject);
begin
  Randomize;
  Tab := TMMTabella.Create;
  Cartella := ExtractFilePath(ParamStr(0)) + 'partita';
  FS := TMMFileServer.Create(Tab, Cartella);
  Srv := nil;
  Sporco := True;
  MostraSegreto := False;
  UltimoGiro := 0;
  UltimoPoll := GetTickCount64;
  UltimoRanking := '';
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
    LblIp.Caption := 'IP di questo PC: non si ricava (guarda il file README-server.txt)'
  else
    LblIp.Caption := 'IP di questo PC: ' + IpPc;
  EdPortaChange(nil);
  AggiornaStato;
  AggiornaSegreto;
  Scrivi('Benvenuto! Premi "Avvia server" per cominciare.');
end;

procedure TForm1.FormDestroy(Sender: TObject);
begin
  Timer1.Enabled := False;
  if (FS <> nil) and (Srv <> nil) then FS.ScriviFile;
  FreeAndNil(Srv);
  FreeAndNil(FS);
  FreeAndNil(Tab);
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

{ ---- chi e' collegato ---- }

function TForm1.Visto(const Nome: String): Boolean;
var
  i: Integer;
begin
  for i := 0 to High(Visti) do
    if SameText(Visti[i].Nome, Nome) then
    begin
      Visti[i].Ultimo := GetTickCount64;
      Result := False;
      Exit;
    end;
  SetLength(Visti, Length(Visti) + 1);
  Visti[High(Visti)].Nome := Nome;
  Visti[High(Visti)].Ultimo := GetTickCount64;
  Result := True;
end;

function TForm1.Collegati: Integer;
var
  i: Integer;
  adesso: QWord;
begin
  Result := 0;
  adesso := GetTickCount64;
  for i := 0 to High(Visti) do
    if adesso - Visti[i].Ultimo <= FUORI_LINEA_MS then Inc(Result);
end;

{ Chiamata dalla rete per OGNI richiesta (nel thread principale: nessun problema) }
procedure TForm1.RichiestaArrivata(const Ip, Linea, Risposta: String);
var
  nome, cmd, tipo: String;
begin
  cmd := UpperCase(Trim(Campo(Linea, 1)));
  nome := PulisciNome(Campo(Linea, 2));
  if Tab.NomePerIp(Ip) <> '' then nome := Tab.NomePerIp(Ip);
  if nome = '' then
  begin
    Scrivi('Richiesta strana da ' + Ip + ': ' + Risposta);
    Exit;
  end;
  if Visto(nome) then Scrivi(nome + ' si e'' collegato (PC ' + Ip + ')');
  Sporco := True;
  if cmd <> 'GUESS' then Exit;      // STATO: e' solo il client che aggiorna la sua console
  tipo := Campo(Risposta, 1);
  if tipo = 'RESULT' then
    Scrivi(nome + ' prova ' + Trim(Campo(Linea, 3)) + ':  ' + Campo(Risposta, 2) +
      ' esatte, ' + Campo(Risposta, 3) + ' spostate  (tentativo n. ' + Campo(Risposta, 4) + ')')
  else if tipo = 'WIN' then
    Scrivi('*** ' + nome + ' HA VINTO! ' + Campo(Risposta, 3) + ' tentativi, ' +
      Campo(Risposta, 4) + ' secondi, posto n. ' + Campo(Risposta, 5) + ' ***')
  else if tipo = 'WAIT' then
    Scrivi(nome + ' ha provato prima del Via: non conta')
  else
    Scrivi(nome + ': ' + Risposta);
end;

{ ---- scritte e classifica ---- }

procedure TForm1.AggiornaStato;
begin
  if (Srv = nil) or not Srv.Pronto then
    LblStato.Caption := 'Server SPENTO'
  else if Tab.Fase = faAttesa then
    LblStato.Caption := 'Server acceso (porta ' + EdPorta.Text + ') - si aspetta il Via!'
  else
    LblStato.Caption := 'Server acceso (porta ' + EdPorta.Text + ') - GIOCO IN CORSO';
end;

procedure TForm1.AggiornaSegreto;
begin
  if (Srv = nil) or not Srv.Pronto then
    LblSegreto.Caption := 'Combinazione segreta: (non ancora scelta)'
  else if MostraSegreto then
    LblSegreto.Caption := 'Combinazione segreta: ' + Tab.Segreto + '   (clicca per nasconderla)'
  else
    LblSegreto.Caption := 'Combinazione segreta: ????   (clicca per vederla)';
end;

procedure TForm1.AggiornaClassifica;
var
  L: TStringList;
  i, k, vinti, provano, riga, posto, ultimaPos: Integer;
  G: TGiocatore;
  chiave, ultimaChiave, nome, tent, stato, resto: String;
  trovato: Boolean;
  adesso: QWord;
  p: Integer;
begin
  L := TStringList.Create;
  try
    vinti := 0;
    provano := 0;
    adesso := GetTickCount64;
    Tab.Blocca;
    try
      // 1. chi ha gia' provato (o vinto)
      for i := 0 to Tab.Count - 1 do
      begin
        G := Tab.Giocatori[i];
        if G.Risolto then
        begin
          Inc(vinti);
          chiave := '0' + Zeri(G.Tentativi, 6) + Zeri(G.Secondi, 8);
          stato := 'HA VINTO (' + IntToStr(G.Secondi) + ' s)';
        end
        else
        begin
          Inc(provano);
          chiave := '1' + Zeri(G.Tentativi, 6) + Zeri(0, 8);
          stato := 'sta provando';
        end;
        for k := 0 to High(Visti) do
          if SameText(Visti[k].Nome, G.Nome) and (adesso - Visti[k].Ultimo > FUORI_LINEA_MS) then
            stato := stato + ' (scollegato)';
        L.Add(chiave + LowerCase(G.Nome) + #1 + G.Nome + #1 + IntToStr(G.Tentativi) + #1 + stato);
      end;
    finally
      Tab.Sblocca;
    end;
    // 2. chi e' collegato ma non ha ancora provato
    for k := 0 to High(Visti) do
    begin
      trovato := False;
      for i := 0 to L.Count - 1 do
      begin
        resto := Copy(L[i], Pos(#1, L[i]) + 1, 200);
        nome := Copy(resto, 1, Pos(#1, resto) - 1);
        if SameText(nome, Visti[k].Nome) then trovato := True;
      end;
      if not trovato then
      begin
        stato := 'collegato, non ha ancora provato';
        if adesso - Visti[k].Ultimo > FUORI_LINEA_MS then stato := 'scollegato';
        L.Add('2' + Zeri(0, 14) + LowerCase(Visti[k].Nome) + #1 + Visti[k].Nome + #1 + '0' + #1 + stato);
      end;
    end;
    L.Sort;
    // 3. disegno la griglia
    Griglia.BeginUpdate;
    try
      Griglia.RowCount := L.Count + 1;
      ultimaChiave := '';
      ultimaPos := 0;
      for riga := 0 to L.Count - 1 do
      begin
        chiave := Copy(L[riga], 1, 15);
        resto := Copy(L[riga], Pos(#1, L[riga]) + 1, 400);
        p := Pos(#1, resto);
        nome := Copy(resto, 1, p - 1);
        resto := Copy(resto, p + 1, 400);
        p := Pos(#1, resto);
        tent := Copy(resto, 1, p - 1);
        stato := Copy(resto, p + 1, 400);
        if chiave[1] = '0' then
        begin
          if chiave = ultimaChiave then posto := ultimaPos else posto := riga + 1;   // pari merito
          ultimaChiave := chiave;
          ultimaPos := posto;
          Griglia.Cells[0, riga + 1] := IntToStr(posto);
        end
        else
          Griglia.Cells[0, riga + 1] := '-';
        Griglia.Cells[1, riga + 1] := nome;
        Griglia.Cells[2, riga + 1] := tent;
        Griglia.Cells[3, riga + 1] := stato;
      end;
    finally
      Griglia.EndUpdate;
    end;
  finally
    L.Free;
  end;
  LblGiocatori.Caption := 'Giocatori collegati: ' + IntToStr(Collegati) +
    '     Hanno vinto: ' + IntToStr(vinti) + '     Stanno provando: ' + IntToStr(provano);
end;

{ ---- i bottoni ---- }

procedure TForm1.NuovaPartita;
begin
  Tab.Blocca;
  try
    Tab.NuovaPartita(-1);       // -1 = combinazione a caso
  finally
    Tab.Sblocca;
  end;
  FS.Dimentica;
  FS.ScriviFile;
  SetLength(Visti, 0);          // i ragazzi ricompaiono da soli al loro prossimo messaggio
  UltimoRanking := '';
  Sporco := True;
end;

procedure TForm1.BtnAvviaClick(Sender: TObject);
var
  porta: Integer;
begin
  porta := StrToIntDef(Trim(EdPorta.Text), 0);
  if (porta < 1) or (porta > 65535) then
  begin
    ShowMessage('La porta deve essere un numero tra 1 e 65535. Di solito si usa 5050.');
    Exit;
  end;
  FreeAndNil(Srv);
  Srv := TMMTcpServerPoll.Create(Tab, Word(porta));
  Srv.OnRichiesta := @RichiestaArrivata;
  if not Srv.Avvia then
  begin
    Scrivi('NON riesco ad aprire la porta ' + IntToStr(porta) + ': ' + Srv.Errore);
    ShowMessage('Non riesco ad aprire la porta ' + IntToStr(porta) + '.' + LineEnding +
      'Forse un altro server e'' gia'' acceso, oppure la porta e'' bloccata.' + LineEnding +
      'Prova un''altra porta, per esempio 5051, e premi di nuovo "Avvia server".');
    FreeAndNil(Srv);
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
  UltimoPoll := GetTickCount64;
  Timer1.Enabled := True;
  AggiornaStato;
  AggiornaSegreto;
end;

procedure TForm1.BtnViaClick(Sender: TObject);
begin
  if (Srv = nil) or (Tab.Fase = faGioco) then Exit;
  Tab.Blocca;
  try
    Tab.Via;
  finally
    Tab.Sblocca;
  end;
  FS.ScriviFile;
  BtnVia.Enabled := False;
  Scrivi('VIA! Tutti giocano sulla stessa combinazione. Che vinca il migliore!');
  AggiornaStato;
  Sporco := True;
end;

procedure TForm1.BtnNuovaClick(Sender: TObject);
begin
  if Srv = nil then Exit;
  if (Tab.Fase = faGioco) and (Tab.Count > 0) then
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
  nuovi: Integer;
  r: String;
begin
  adesso := GetTickCount64;
  try
    if Srv <> nil then Srv.Tick;                 // 1. la rete: risponde a chi bussa
    if adesso - UltimoPoll >= 2000 then          // 2. ogni 2 secondi rilegge i file dei ragazzi
    begin
      UltimoPoll := adesso;
      nuovi := FS.Poll;
      if nuovi > 0 then
      begin
        FS.ScriviFile;
        Scrivi('Dai file: ' + IntToStr(nuovi) + ' tentativi nuovi');
        Sporco := True;
      end;
    end;
    if Sporco or (adesso - UltimoGiro >= 1000) then   // 3. ridisegna (subito se c'e' novita', altrimenti ogni secondo)
    begin
      UltimoGiro := adesso;
      Sporco := False;
      Tab.Blocca;
      try
        r := Tab.TestoRanking;
      finally
        Tab.Sblocca;
      end;
      if r <> UltimoRanking then       // la classifica e' cambiata: riscrivo i file (chi usa i file la vede)
      begin
        UltimoRanking := r;
        FS.ScriviFile;
      end;
      AggiornaClassifica;
      AggiornaStato;
    end;
  except
    on E: Exception do
      Scrivi('Attenzione: ' + E.Message);       // un errore non deve fermare il Timer
  end;
end;

end.
