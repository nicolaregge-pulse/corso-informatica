unit Unit1;
{ MASTERMIND BELLO - CLIENT per i ragazzi, TUTTO IN UN FILE (piu' il suo unit1.lfm).
  Due modi per giocare:
    - "Connetti": ti colleghi al PC del prof (porta 5050) e giochi la partita di classe;
    - "Gioca da solo": il programma pensa lui il codice, non serve la rete.
  I colori sono 6 e possono RIPETERSI (rosso, rosso, blu, giallo e' un codice valido).
  Piolini di risposta: NERO = colore giusto al posto giusto, BIANCO = colore giusto al posto sbagliato.
  Come si gioca: clicca i colori nella colonna di destra (si riempiono i 4 buchi della riga
  illuminata), poi premi "Prova". Con "Togli l'ultimo" correggi.
  Ogni richiesta alla rete: ti colleghi, mandi UNA riga, leggi UNA riga, chiudi. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  sockets, ssockets;

type
  TCodice = array[0..3] of Integer;      // 4 colori, ognuno da 1 a 6 (0 = buco vuoto)
  TTentativo = record
    Colori: TCodice;
    Neri, Bianchi: Integer;
  end;
  TModo = (mNessuno, mRete, mLocale);

  TForm1 = class(TForm)
    LblIp: TLabel;
    EdIp: TEdit;
    LblNome: TLabel;
    EdNome: TEdit;
    BtnConnetti: TButton;
    BtnLocale: TButton;
    LblEsito: TLabel;
    LblStato: TLabel;
    PbTavola: TPaintBox;
    PbTavolozza: TPaintBox;
    BtnProva: TButton;
    BtnCancella: TButton;
    LblPosizione: TLabel;
    LblMigliore: TLabel;
    LblPeggiore: TLabel;
    LblFiniti: TLabel;
    Timer1: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure BtnConnettiClick(Sender: TObject);
    procedure BtnLocaleClick(Sender: TObject);
    procedure BtnProvaClick(Sender: TObject);
    procedure BtnCancellaClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure PbTavolaPaint(Sender: TObject);
    procedure PbTavolozzaPaint(Sender: TObject);
    procedure PbTavolozzaMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private
    Errori: Integer;
    Nome: String;
    function PulisciNome: String;
    function Chiedi(const Riga: String; out Risposta: String): String;
    function Campo(const S: String; N: Integer): String;
    procedure Mostra(const R: String; Dopo: Integer);
    procedure AggiornaBottoni;
    procedure Ricomincia;
    procedure Registra(Neri, Bianchi: Integer);
    procedure ProvaInLocale;
    procedure ProvaInRete;
    function PrimaRigaVisibile: Integer;
  public
    Avviato: Boolean;                 // True quando FormCreate e' gia' partita
    Modo: TModo;
    Finita: Boolean;                  // True dopo che hai indovinato
    Segreto: TCodice;                 // il codice (solo nel gioco "da solo")
    Corrente: TCodice;                // il tentativo che stai riempiendo
    NCorr: Integer;                   // quanti buchi hai gia' riempito (0..4)
    Storia: array[0..299] of TTentativo;
    NT: Integer;                      // quanti tentativi hai fatto
    procedure AfterConstruction; override;
    procedure AggiungiColore(C: Integer);
    procedure TogliUltimo;
    procedure ProvaTentativo;
    procedure NuovaPartitaLocale;
  end;

{ Conta i piolini di risposta. Neri = giusti al posto giusto; Bianchi = colore giusto al
  posto sbagliato. Funziona anche con colori ripetuti (esempio: segreto 1123, prova 1211). }
procedure Valuta(const Segreto, Prova: TCodice; out Neri, Bianchi: Integer);

var
  Form1: TForm1;

implementation

{$R *.lfm}

const
  PORTA_SERVER = 5050;      // la porta del server: non toccarla
  TEMPO_MS = 2000;          // dopo 2 secondi senza risposta ci arrendiamo
  RIGHE = 10;               // righe visibili sulla tavola
  CELLA = 44;               // altezza di una riga e distanza tra i buchi
  MARGINE = 14;
  RAGGIO = 17;              // raggio di un piolo grande
  LARG_TAVOLA = 270;
  ALT_TAVOLA = 468;         // 2 * MARGINE + RIGHE * CELLA
  LARG_PALETTE = 90;
  ALT_PALETTE = 330;
  // sei colori, in ordine 1..6: rosso, giallo, verde, blu, arancio, viola (formato BGR)
  COLORI: array[1..6] of Integer = ($002828DC, $001EC8F0, $003CA028, $00DC5A28, $001E82F0, $00AA328C);
  NOMI_COLORI: array[1..6] of String = ('rosso', 'giallo', 'verde', 'blu', 'arancio', 'viola');

{ ---------- il cervello: nessuna finestra, nessuna rete ---------- }

procedure Valuta(const Segreto, Prova: TCodice; out Neri, Bianchi: Integer);
var
  CS, CP: array[1..6] of Integer;
  I: Integer;
begin
  for I := 1 to 6 do
  begin
    CS[I] := 0;
    CP[I] := 0;
  end;
  Neri := 0;
  for I := 0 to 3 do
    if Segreto[I] = Prova[I] then
      Inc(Neri)
    else
    begin
      Inc(CS[Segreto[I]]);
      Inc(CP[Prova[I]]);
    end;
  Bianchi := 0;
  for I := 1 to 6 do
    if CS[I] < CP[I] then Inc(Bianchi, CS[I]) else Inc(Bianchi, CP[I]);
end;

{ ---------- i colori: mischia un colore col bianco (Perc da 0 a 100) ---------- }

function MioColore(R, G, B: Integer): Integer;
begin
  Result := R or (G shl 8) or (B shl 16);
end;

function Schiarisci(Col, Perc: Integer): Integer;
var
  R, G, B: Integer;
begin
  R := Col and $FF;
  G := (Col shr 8) and $FF;
  B := (Col shr 16) and $FF;
  R := R + (255 - R) * Perc div 100;
  G := G + (255 - G) * Perc div 100;
  B := B + (255 - B) * Perc div 100;
  Result := MioColore(R, G, B);
end;

{ ---------- il disegno: legno, buchi, pioli ---------- }

procedure DisegnaLegno(C: TCanvas; W, H: Integer);
var
  Y, D: Integer;
begin
  C.Brush.Style := bsSolid;
  C.Pen.Style := psSolid;
  C.Pen.Width := 1;
  C.Brush.Color := MioColore(170, 118, 66);
  C.Pen.Color := MioColore(170, 118, 66);
  C.Rectangle(0, 0, W, H);
  // le venature: righe orizzontali di marrone un po' piu' chiaro o scuro
  Y := 0;
  while Y < H do
  begin
    D := ((Y * 37) mod 23) - 11;
    C.Pen.Color := MioColore(170 + D, 118 + D, 66 + D div 2);
    C.MoveTo(0, Y);
    C.LineTo(W, Y);
    if (Y mod 29) = 5 then
    begin
      C.Pen.Color := MioColore(120, 78, 40);   // ogni tanto una vena piu' scura
      C.MoveTo(0, Y + 1);
      C.LineTo(W, Y + 1);
    end;
    Inc(Y, 3);
  end;
  // la cornice
  C.Brush.Style := bsClear;
  C.Pen.Width := 6;
  C.Pen.Color := MioColore(92, 56, 26);
  C.Rectangle(0, 0, W, H);
  C.Pen.Width := 1;
  C.Brush.Style := bsSolid;
end;

procedure DisegnaBuco(C: TCanvas; Cx, Cy, R: Integer);
begin
  C.Pen.Style := psClear;
  C.Brush.Color := MioColore(48, 28, 12);
  C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
  C.Brush.Color := MioColore(78, 48, 24);
  C.Ellipse(Cx - R + 2, Cy - R + 2, Cx + R - 1, Cy + R - 1);
  C.Brush.Color := MioColore(40, 22, 8);
  C.Ellipse(Cx - R + 3, Cy - R + 3, Cx + R - 3, Cy + R - 3);
  C.Pen.Style := psSolid;
end;

{ un piolo: cerchi sempre piu' piccoli e piu' chiari, spostati in alto a sinistra: sembra una sfera }
procedure DisegnaPiolo(C: TCanvas; Cx, Cy, R, Col: Integer);
var
  K, Rk, Off: Integer;
begin
  C.Pen.Style := psClear;
  C.Brush.Color := MioColore(40, 24, 10);                       // l'ombra sul legno
  C.Ellipse(Cx - R + 2, Cy - R + 3, Cx + R + 3, Cy + R + 4);
  for K := 0 to 5 do
  begin
    Rk := R - (K * R) div 7;
    Off := -(K * R) div 14;
    C.Brush.Color := Schiarisci(Col, K * 11);
    C.Ellipse(Cx + Off - Rk, Cy + Off - Rk, Cx + Off + Rk + 1, Cy + Off + Rk + 1);
  end;
  C.Pen.Style := psSolid;
end;

{ piolino di risposta (piccolo): nero o bianco }
procedure DisegnaRisposta(C: TCanvas; Cx, Cy, R: Integer; Nero: Boolean);
begin
  C.Pen.Style := psClear;
  if Nero then
  begin
    C.Brush.Color := MioColore(12, 12, 12);
    C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
    C.Brush.Color := MioColore(90, 90, 90);
    C.Ellipse(Cx - R div 2 - 1, Cy - R div 2 - 1, Cx - 1, Cy - 1);
  end
  else
  begin
    C.Brush.Color := MioColore(235, 235, 235);
    C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
    C.Brush.Color := MioColore(255, 255, 255);
    C.Ellipse(Cx - R div 2 - 1, Cy - R div 2 - 1, Cx - 1, Cy - 1);
  end;
  C.Pen.Style := psSolid;
end;

{ ---------- la finestra ---------- }

procedure TForm1.FormCreate(Sender: TObject);
begin
  Avviato := True;
  Modo := mNessuno;
  Finita := False;
  Errori := 0;
  NT := 0;
  NCorr := 0;
  Timer1.Enabled := False;
  Timer1.Interval := 3000;
  LblStato.Caption := 'Scegli come giocare';
  LblEsito.Caption := 'Premi "Gioca da solo", oppure scrivi il tuo nome e premi Connetti.';
  AggiornaBottoni;
end;

{ Se Lazarus non ha collegato gli eventi, li colleghiamo noi da qui }
procedure TForm1.AfterConstruction;
begin
  inherited AfterConstruction;
  if not Assigned(BtnConnetti.OnClick) then BtnConnetti.OnClick := @BtnConnettiClick;
  if not Assigned(BtnLocale.OnClick) then BtnLocale.OnClick := @BtnLocaleClick;
  if not Assigned(BtnProva.OnClick) then BtnProva.OnClick := @BtnProvaClick;
  if not Assigned(BtnCancella.OnClick) then BtnCancella.OnClick := @BtnCancellaClick;
  if not Assigned(Timer1.OnTimer) then Timer1.OnTimer := @Timer1Timer;
  if not Assigned(PbTavola.OnPaint) then PbTavola.OnPaint := @PbTavolaPaint;
  if not Assigned(PbTavolozza.OnPaint) then PbTavolozza.OnPaint := @PbTavolozzaPaint;
  if not Assigned(PbTavolozza.OnMouseDown) then PbTavolozza.OnMouseDown := @PbTavolozzaMouseDown;
  if not Avviato then FormCreate(nil);
end;

{ il quarto, il terzo... campo di una riga separata da punto e virgola }
function TForm1.Campo(const S: String; N: Integer): String;
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

function TForm1.PulisciNome: String;
begin
  Result := Trim(StringReplace(EdNome.Text, ';', '', [rfReplaceAll]));
end;

{ Manda UNA riga al server e legge UNA riga. Risultato: '' se tutto bene,
  altrimenti il motivo dell'errore in parole semplici. }
function TForm1.Chiedi(const Riga: String; out Risposta: String): String;
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
  Host := Trim(EdIp.Text);
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
      Buf := Riga + #10;
      S.WriteBuffer(Buf[1], Length(Buf));
      Fine := GetTickCount64 + TEMPO_MS;
      repeat
        N := S.Read(Ch, 1);
        if N <= 0 then Break;
        if Ch = #10 then Break;
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

{ Aggiorna le scritte della classifica. Dopo = posizione del campo "tentativi" nella risposta }
procedure TForm1.Mostra(const R: String; Dopo: Integer);
var
  Mig, Peg, Pos_, Tot: String;
begin
  Pos_ := Campo(R, Dopo + 1);
  Tot := Campo(R, Dopo + 2);
  Mig := Campo(R, Dopo + 3);
  Peg := Campo(R, Dopo + 4);
  if Mig = '0' then LblMigliore.Caption := 'Migliore: nessuno ha ancora finito'
  else LblMigliore.Caption := 'Migliore: ' + Mig + ' tentativi';
  if Peg = '0' then LblPeggiore.Caption := 'Peggiore: -'
  else LblPeggiore.Caption := 'Peggiore: ' + Peg + ' tentativi';
  if (Pos_ = '0') or (Pos_ = '') then LblPosizione.Caption := 'Il tuo posto: non hai ancora indovinato'
  else LblPosizione.Caption := 'Il tuo posto: ' + Pos_ + 'o';
  LblFiniti.Caption := 'Hanno finito: ' + Tot;
end;

procedure TForm1.AggiornaBottoni;
begin
  BtnProva.Enabled := (Modo <> mNessuno) and (not Finita) and (NCorr = 4);
  BtnCancella.Enabled := (Modo <> mNessuno) and (not Finita) and (NCorr > 0);
  PbTavola.Invalidate;
end;

{ la prima riga della storia che si vede: se hai fatto piu' di 10 tentativi scorre }
function TForm1.PrimaRigaVisibile: Integer;
begin
  if NT < RIGHE then Result := 0 else Result := NT - RIGHE + 1;
end;

procedure TForm1.Ricomincia;
begin
  NT := 0;
  NCorr := 0;
  Finita := False;
  FillChar(Corrente, SizeOf(Corrente), 0);
  LblPosizione.Caption := '';
  LblMigliore.Caption := '';
  LblPeggiore.Caption := '';
  LblFiniti.Caption := '';
end;

{ ---------- i bottoni ---------- }

procedure TForm1.BtnLocaleClick(Sender: TObject);
begin
  NuovaPartitaLocale;
end;

procedure TForm1.NuovaPartitaLocale;
var
  I: Integer;
begin
  Timer1.Enabled := False;
  Modo := mLocale;
  Randomize;
  for I := 0 to 3 do Segreto[I] := Random(6) + 1;   // i colori possono ripetersi
  Ricomincia;
  LblStato.Caption := 'DA SOLO: indovina il codice';
  LblEsito.Caption := 'Ho pensato 4 colori (anche uguali). Clicca i colori a destra e premi Prova.';
  AggiornaBottoni;
end;

procedure TForm1.BtnConnettiClick(Sender: TObject);
var
  R, Err: String;
begin
  Nome := PulisciNome;
  if Nome = '' then
  begin
    LblEsito.Caption := 'Scrivi prima il tuo nome nella casella.';
    Exit;
  end;
  if Trim(EdIp.Text) = '' then
  begin
    LblEsito.Caption := 'Scrivi l''IP del server (e'' scritto in alto nella pagina).';
    Exit;
  end;
  LblEsito.Caption := 'Mi collego...';
  Err := Chiedi('STATO;' + Nome, R);
  if (Err = '') and (Campo(R, 0) <> 'STATO') then
    Err := 'Risposta strana dal server: ' + R;
  if Err <> '' then
  begin
    Timer1.Enabled := False;
    if Modo = mRete then Modo := mNessuno;
    LblStato.Caption := 'Non collegato';
    LblEsito.Caption := Err;
    AggiornaBottoni;
    Exit;
  end;
  Modo := mRete;
  Errori := 0;
  Ricomincia;
  LblEsito.Caption := 'Collegato! Ciao ' + Nome + '.';
  Mostra(R, 2);
  if Campo(R, 1) = 'GIOCO' then LblStato.Caption := 'GIOCO: provaci!'
  else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  AggiornaBottoni;
  Timer1.Enabled := True;
end;

procedure TForm1.AggiungiColore(C: Integer);
begin
  if Modo = mNessuno then
  begin
    LblEsito.Caption := 'Prima premi "Gioca da solo" oppure Connetti.';
    Exit;
  end;
  if Finita or (C < 1) or (C > 6) then Exit;
  if NCorr < 4 then
  begin
    Corrente[NCorr] := C;
    Inc(NCorr);
    LblEsito.Caption := 'Hai scelto: ' + NOMI_COLORI[C] + '.';
  end;
  AggiornaBottoni;
end;

procedure TForm1.TogliUltimo;
begin
  if NCorr > 0 then
  begin
    Dec(NCorr);
    Corrente[NCorr] := 0;
  end;
  AggiornaBottoni;
end;

procedure TForm1.BtnCancellaClick(Sender: TObject);
begin
  TogliUltimo;
end;

procedure TForm1.PbTavolozzaMouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
var
  I, Dx, Dy: Integer;
begin
  for I := 1 to 6 do
  begin
    Dx := X - LARG_PALETTE div 2;
    Dy := Y - (35 + (I - 1) * 50);
    if Dx * Dx + Dy * Dy <= (RAGGIO + 4) * (RAGGIO + 4) then
    begin
      AggiungiColore(I);
      Exit;
    end;
  end;
end;

{ mette il tentativo appena giudicato nella storia e svuota la riga corrente }
procedure TForm1.Registra(Neri, Bianchi: Integer);
begin
  if NT > High(Storia) then Exit;
  Storia[NT].Colori := Corrente;
  Storia[NT].Neri := Neri;
  Storia[NT].Bianchi := Bianchi;
  Inc(NT);
  NCorr := 0;
  FillChar(Corrente, SizeOf(Corrente), 0);
end;

procedure TForm1.BtnProvaClick(Sender: TObject);
begin
  ProvaTentativo;
end;

procedure TForm1.ProvaTentativo;
begin
  if Modo = mNessuno then
  begin
    LblEsito.Caption := 'Prima premi "Gioca da solo" oppure Connetti.';
    Exit;
  end;
  if NCorr <> 4 then
  begin
    LblEsito.Caption := 'Servono 4 colori: clicca ancora sui colori a destra.';
    Exit;
  end;
  if Modo = mLocale then ProvaInLocale else ProvaInRete;
  AggiornaBottoni;
end;

procedure TForm1.ProvaInLocale;
var
  N, B: Integer;
begin
  Valuta(Segreto, Corrente, N, B);
  Registra(N, B);
  if N = 4 then
  begin
    Finita := True;
    LblStato.Caption := 'HAI VINTO!';
    LblEsito.Caption := 'BRAVO! Hai indovinato in ' + IntToStr(NT) + ' tentativi.';
  end
  else
    LblEsito.Caption := IntToStr(N) + ' neri (giusti al posto giusto), ' + IntToStr(B) +
      ' bianchi (giusti al posto sbagliato).';
end;

procedure TForm1.ProvaInRete;
var
  R, Err, Cod, T: String;
  I: Integer;
begin
  Cod := '';
  for I := 0 to 3 do Cod := Cod + Chr(48 + Corrente[I]);
  Err := Chiedi('GUESS;' + Nome + ';' + Cod, R);
  if Err <> '' then
  begin
    LblEsito.Caption := Err;
    Exit;
  end;
  T := Campo(R, 0);
  if T = 'WAIT' then
  begin
    LblEsito.Caption := 'Il Prof non ha ancora detto Via: aspetta.';
    LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  end
  else if T = 'RESULT' then
  begin
    LblStato.Caption := 'GIOCO: provaci!';
    Registra(StrToIntDef(Campo(R, 1), 0), StrToIntDef(Campo(R, 2), 0));
    LblEsito.Caption := Campo(R, 1) + ' neri, ' + Campo(R, 2) + ' bianchi';
    Mostra(R, 3);
  end
  else if T = 'WIN' then
  begin
    Registra(4, 0);
    Finita := True;
    LblStato.Caption := 'HAI VINTO!';
    LblEsito.Caption := 'BRAVO! Hai indovinato in ' + Campo(R, 2) + ' tentativi e ' +
      Campo(R, 3) + ' secondi.';
    Mostra(R, 3);
  end
  else if T = 'ERR' then
    LblEsito.Caption := 'Il server dice: ' + Campo(R, 1)
  else
    LblEsito.Caption := 'Risposta strana dal server: ' + R;
end;

{ ogni 3 secondi chiede al server come siamo messi (solo nel gioco in rete) }
procedure TForm1.Timer1Timer(Sender: TObject);
var
  R, Err: String;
begin
  if Modo <> mRete then Exit;
  Err := Chiedi('STATO;' + Nome, R);
  if Err <> '' then
  begin
    Inc(Errori);
    LblEsito.Caption := Err;
    if Errori >= 3 then
    begin
      Modo := mNessuno;
      Timer1.Enabled := False;
      LblStato.Caption := 'Non collegato';
      LblEsito.Caption := 'Il server non risponde piu'': premi Connetti per riprovare.';
      AggiornaBottoni;
    end;
    Exit;
  end;
  Errori := 0;
  if Campo(R, 0) <> 'STATO' then Exit;
  Mostra(R, 2);
  if Finita and (Campo(R, 3) = '0') then
  begin
    // il Prof ha ricominciato con un'altra combinazione
    Ricomincia;
    LblStato.Caption := '';
  end;
  if not Finita then
    if Campo(R, 1) = 'GIOCO' then LblStato.Caption := 'GIOCO: provaci!'
    else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  AggiornaBottoni;
end;

{ ---------- il disegno della tavola e della tavolozza ---------- }

procedure TForm1.PbTavolaPaint(Sender: TObject);
var
  Cv: TCanvas;
  Riga, Col, K, Cx, Cy, Ind, Prima: Integer;
begin
  Cv := PbTavola.Canvas;
  DisegnaLegno(Cv, LARG_TAVOLA, ALT_TAVOLA);
  Prima := PrimaRigaVisibile;
  for Riga := 0 to RIGHE - 1 do
  begin
    Cy := MARGINE + Riga * CELLA + CELLA div 2;
    Ind := Prima + Riga;
    if (Ind = NT) and (Modo <> mNessuno) and (not Finita) then
    begin
      // la riga che stai riempiendo e' "illuminata"
      Cv.Brush.Style := bsClear;
      Cv.Pen.Width := 2;
      Cv.Pen.Color := MioColore(255, 226, 120);
      Cv.Rectangle(MARGINE - 4, Cy - CELLA div 2 + 2, LARG_TAVOLA - MARGINE + 4, Cy + CELLA div 2 - 1);
      Cv.Pen.Width := 1;
      Cv.Brush.Style := bsSolid;
    end;
    for Col := 0 to 3 do
    begin
      Cx := MARGINE + 22 + Col * CELLA;
      if Ind < NT then
        DisegnaPiolo(Cv, Cx, Cy, RAGGIO, COLORI[Storia[Ind].Colori[Col]])
      else if (Ind = NT) and (Col < NCorr) then
        DisegnaPiolo(Cv, Cx, Cy, RAGGIO, COLORI[Corrente[Col]])
      else
        DisegnaBuco(Cv, Cx, Cy, RAGGIO - 3);
    end;
    // i 4 piolini piccoli di risposta, a 2 a 2
    for K := 0 to 3 do
    begin
      Cx := 218 + (K mod 2) * 20;
      Cy := MARGINE + Riga * CELLA + CELLA div 2 - 10 + (K div 2) * 20;
      if Ind < NT then
      begin
        if K < Storia[Ind].Neri then DisegnaRisposta(Cv, Cx, Cy, 7, True)
        else if K < Storia[Ind].Neri + Storia[Ind].Bianchi then DisegnaRisposta(Cv, Cx, Cy, 7, False)
        else DisegnaBuco(Cv, Cx, Cy, 5);
      end
      else
        DisegnaBuco(Cv, Cx, Cy, 5);
    end;
  end;
end;

procedure TForm1.PbTavolozzaPaint(Sender: TObject);
var
  Cv: TCanvas;
  I: Integer;
begin
  Cv := PbTavolozza.Canvas;
  DisegnaLegno(Cv, LARG_PALETTE, ALT_PALETTE);
  for I := 1 to 6 do
    DisegnaPiolo(Cv, LARG_PALETTE div 2, 35 + (I - 1) * 50, RAGGIO, COLORI[I]);
end;

end.
