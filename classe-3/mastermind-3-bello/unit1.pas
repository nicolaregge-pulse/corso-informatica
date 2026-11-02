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
    procedure MostraDemo;
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
  FondoTavola, FondoTavolozza: TBitmap;   // il legno, disegnato una volta sola

implementation

{$R *.lfm}

const
  PORTA_SERVER = 5050;      // la porta del server: non toccarla
  TEMPO_MS = 2000;          // dopo 2 secondi senza risposta ci arrendiamo
  RIGHE = 10;               // righe visibili sulla tavola
  CELLA = 40;               // altezza di una riga
  PASSO_X = 44;             // distanza tra i buchi in orizzontale
  TITOLO = 40;              // la fascia in alto con la scritta intagliata
  MARGINE = 14;
  RAGGIO = 17;              // raggio di un piolo grande
  LARG_TAVOLA = 270;
  ALT_TAVOLA = 468;         // TITOLO + 2 * MARGINE + RIGHE * CELLA
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

{ ---------- il legno: fibre sottili, toni morbidi, striature, fessure, pori, bordi piu' scuri ----------
  Si usa un "caso" tutto nostro con il seme fisso, cosi' la tavola e' SEMPRE uguale.
  Si disegna UNA volta su una bitmap e poi si copia sullo schermo: e' veloce. }

var
  SemeLegno: Int64;
  BordoW, BordoH: Integer;

procedure InizioCaso(S: Integer);
begin
  SemeLegno := S;
end;

function Caso(N: Integer): Integer;       // un numero da 0 a N-1, sempre la stessa sequenza
begin
  SemeLegno := (SemeLegno * 1103515245 + 12345) and $7FFFFFFF;
  Result := (SemeLegno shr 8) mod N;
end;

function Mescola(A, B, Perc: Integer): Integer;     // A mescolato con B (Perc% di B): come un colore semitrasparente
var
  Ra, Ga, Ba, Rb, Gb, Bb: Integer;
begin
  Ra := A and $FF;
  Ga := (A shr 8) and $FF;
  Ba := (A shr 16) and $FF;
  Rb := B and $FF;
  Gb := (B shr 8) and $FF;
  Bb := (B shr 16) and $FF;
  Result := MioColore(Ra + (Rb - Ra) * Perc div 100, Ga + (Gb - Ga) * Perc div 100,
    Ba + (Bb - Ba) * Perc div 100);
end;

{ il colore del legno in un punto: dal miele al rovere con macchie larghe e morbide,
  e un po' piu' scuro vicino ai bordi della tavola }
function TonoLegno(X, Y: Integer): Integer;
var
  F, V: Integer;
begin
  F := 50 + Round(26 * Sin(Y * 0.011 + X * 0.0028 + 0.7) + 14 * Sin(Y * 0.029 - X * 0.0049 + 2.1) +
    8 * Sin(X * 0.011 + Y * 0.017));
  if F < 0 then F := 0;
  if F > 100 then F := 100;
  Result := Mescola(MioColore(212, 166, 102), MioColore(170, 120, 66), F * 7 div 10);
  V := X;
  if BordoW - 1 - X < V then V := BordoW - 1 - X;
  if Y < V then V := Y;
  if BordoH - 1 - Y < V then V := BordoH - 1 - Y;
  if V < 0 then V := 0;
  if V < 34 then Result := Mescola(Result, MioColore(48, 26, 10), (34 - V) * 30 div 34);
end;

procedure DisegnaLegno(C: TCanvas; W, H, Semi: Integer);
var
  I, N, X, Y, Y0, X0, Lun, Xe, Perc, K, Pezzo: Integer;
  Amp, Fre, Fase: Double;
  NNodi, NodoX, NodoY, Tono: Integer;
  Chiaro: Boolean;

  function Dentro(Xp: Integer): Integer;
  begin
    Result := Xp;
    if Result < 0 then Result := 0;
    if Result > W - 1 then Result := W - 1;
  end;

  { la fibra ondeggia piano e, vicino al nodino, gira intorno }
  function Deforma(Xp, Yb: Integer; Ap, Fr, Fa: Double): Integer;
  var
    D: Double;
  begin
    D := Ap * Sin(Xp * Fr + Fa) + Ap * 0.5 * Sin(Xp * Fr * 2.3 + Fa * 1.7);
    if NNodi > 0 then
      D := D + 6 * (Yb - NodoY) / (Abs(Yb - NodoY) + 12) * Exp(-Sqr((Xp - NodoX) / 26.0));
    Result := Yb + Round(D);
  end;

begin
  BordoW := W;
  BordoH := H;
  InizioCaso(Semi);
  C.Brush.Style := bsSolid;
  C.Pen.Style := psSolid;
  C.Pen.Width := 1;
  NNodi := 0;
  NodoX := 0;
  NodoY := 0;
  if W >= 200 then            // un solo nodino piccolo, solo sulla tavola grande
  begin
    NNodi := 1;
    NodoX := 60 + Caso(W - 120);
    NodoY := 100 + Caso(H - 200);
  end;
  // 1) i toni di base: un pixel alla volta, il colore cambia piano piano (niente righe nette)
  Y := 0;
  while Y < H do
  begin
    X := 0;
    C.Pen.Color := TonoLegno(0, Y);
    C.MoveTo(0, Y);
    while X < W do
    begin
      Inc(X, 6);
      C.Pen.Color := TonoLegno(X, Y);
      C.LineTo(X, Y);
    end;
    Inc(Y);
  end;
  // 2) le fibre: tante linee sottilissime, un po' piu' chiare o piu' scure del legno sotto
  N := (W * H) div 55;
  for I := 1 to N do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - 30;
    Lun := 60 + Caso(W + 40);
    Amp := 1.0 + Caso(35) / 10.0;
    Fre := 0.005 + Caso(16) / 1000.0;
    Fase := Caso(628) / 100.0;
    Chiaro := Caso(100) < 36;
    Tono := TonoLegno(Dentro(X0), Y0);
    if Chiaro then
      C.Pen.Color := Mescola(Tono, MioColore(232, 190, 130), 14 + Caso(18))
    else
      C.Pen.Color := Mescola(Tono, MioColore(66, 38, 16), 16 + Caso(26));
    X := X0;
    C.MoveTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    Xe := X0 + Lun;
    while X < Xe do
    begin
      Inc(X, 5);
      C.LineTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    end;
  end;
  // 3) qualche striatura piu' scura, lunga e sottile
  for I := 1 to (W * H) div 4000 do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - 40;
    Lun := 100 + Caso(W);
    Amp := 2.0 + Caso(30) / 10.0;
    Fre := 0.004 + Caso(9) / 1000.0;
    Fase := Caso(628) / 100.0;
    Perc := 40 + Caso(18);
    C.Pen.Color := Mescola(TonoLegno(Dentro(X0), Y0), MioColore(60, 34, 12), Perc);
    X := X0;
    C.MoveTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    Xe := X0 + Lun;
    while X < Xe do
    begin
      Inc(X, 5);
      C.LineTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    end;
  end;
  // 4) qualche fessura sottile e interrotta
  for I := 1 to 3 + (W * H) div 30000 do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - 30;
    Lun := 80 + Caso(W);
    Fase := Caso(628) / 100.0;
    X := X0;
    while X < X0 + Lun do
    begin
      Pezzo := 8 + Caso(40);
      C.Pen.Color := Mescola(TonoLegno(Dentro(X), Y0), MioColore(30, 16, 6), 66 + Caso(10));
      C.MoveTo(X, Deforma(X, Y0, 2.0, 0.012, Fase));
      Xe := X + Pezzo;
      while X < Xe do
      begin
        Inc(X, 4);
        C.LineTo(X, Deforma(X, Y0, 2.0, 0.012, Fase));
      end;
      Inc(X, 4 + Caso(24));
    end;
  end;
  // 5) i pori: piccoli trattini scuri lunghi 3-14 pixel
  for I := 1 to (W * H) div 200 do
  begin
    X := Caso(W);
    Y := Caso(H);
    Lun := 3 + Caso(12);
    Perc := 34 + Caso(21);
    C.Pen.Color := Mescola(TonoLegno(X, Y), MioColore(50, 28, 10), Perc);
    C.MoveTo(X, Deforma(X, Y, 1.5, 0.012, 1.0));
    C.LineTo(X + Lun, Deforma(X + Lun, Y, 1.5, 0.012, 1.0));
  end;
  // 6) il nodino: tre anelli sottili e un centro scuro
  if NNodi > 0 then
  begin
    C.Brush.Style := bsClear;
    Tono := TonoLegno(NodoX, NodoY);
    for K := 3 downto 1 do
    begin
      C.Pen.Color := Mescola(Tono, MioColore(60, 34, 12), 16 + K * 4);
      C.Ellipse(NodoX - K * 5 - 3, NodoY - K * 2 - 2, NodoX + K * 5 + 4, NodoY + K * 2 + 3);
    end;
    C.Brush.Style := bsSolid;
    C.Brush.Color := Mescola(Tono, MioColore(40, 22, 8), 55);
    C.Pen.Color := C.Brush.Color;
    C.Ellipse(NodoX - 3, NodoY - 2, NodoX + 4, NodoY + 3);
  end;
  // 7) la cornice lucida: luce in alto a sinistra, ombra in basso a destra
  C.Brush.Style := bsClear;
  C.Pen.Width := 6;
  C.Pen.Color := MioColore(84, 50, 22);
  C.Rectangle(0, 0, W, H);
  C.Pen.Width := 1;
  C.Pen.Color := MioColore(150, 100, 52);
  C.Rectangle(3, 3, W - 3, H - 3);
  C.Pen.Color := MioColore(232, 190, 132);
  C.MoveTo(4, 4);
  C.LineTo(W - 5, 4);
  C.MoveTo(4, 4);
  C.LineTo(4, H - 5);
  C.Pen.Color := MioColore(255, 230, 176);
  C.MoveTo(8, 6);
  C.LineTo(W - 14, 6);
  C.Pen.Color := MioColore(54, 30, 12);
  C.MoveTo(W - 5, 5);
  C.LineTo(W - 5, H - 5);
  C.LineTo(4, H - 5);
  C.Brush.Style := bsSolid;
end;

{ la scritta INTAGLIATA nel legno: ombra scura in alto a sinistra, bordo chiaro in basso a destra }
procedure IncidiScritta(C: TCanvas; W, Alt: Integer; const Testo: String);
var
  Tx, Ty: Integer;
begin
  C.Brush.Style := bsClear;
  C.Font.Name := 'Arial';
  C.Font.Size := 22;
  C.Font.Style := [fsBold];
  Tx := (W - C.TextWidth(Testo)) div 2;
  Ty := (Alt - C.TextHeight(Testo)) div 2;
  C.Font.Color := MioColore(46, 24, 8);
  C.TextOut(Tx - 1, Ty - 1, Testo);
  C.Font.Color := MioColore(236, 194, 134);
  C.TextOut(Tx + 1, Ty + 1, Testo);
  C.Font.Color := MioColore(98, 58, 26);
  C.TextOut(Tx, Ty, Testo);
  C.Brush.Style := bsSolid;
end;

{ si disegna il legno una volta sola su una bitmap, poi basta copiarla }
procedure PreparaFondi;
begin
  if FondoTavola = nil then
  begin
    FondoTavola := TBitmap.Create;
    FondoTavola.Width := LARG_TAVOLA;
    FondoTavola.Height := ALT_TAVOLA;
    DisegnaLegno(FondoTavola.Canvas, LARG_TAVOLA, ALT_TAVOLA, 7);
    IncidiScritta(FondoTavola.Canvas, LARG_TAVOLA, TITOLO + 12, '3 INF');
  end;
  if FondoTavolozza = nil then
  begin
    FondoTavolozza := TBitmap.Create;
    FondoTavolozza.Width := LARG_PALETTE;
    FondoTavolozza.Height := ALT_PALETTE;
    DisegnaLegno(FondoTavolozza.Canvas, LARG_PALETTE, ALT_PALETTE, 19);
  end;
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

{ una partita di ESEMPIO: appena premi F9 vedi subito il legno, i pioli colorati e i
  piolini neri e bianchi. Sparisce quando premi "Gioca da solo" o "Connetti". }
procedure TForm1.MostraDemo;
const
  DEMO: array[0..4, 0..3] of Integer =
    ((2, 2, 5, 6), (1, 1, 2, 3), (1, 4, 4, 3), (4, 1, 1, 3), (1, 4, 1, 5));
var
  I, J: Integer;
  Sec: TCodice;
begin
  Sec[0] := 1;      // il codice dell'esempio: rosso, blu, rosso, verde (il rosso si ripete)
  Sec[1] := 4;
  Sec[2] := 1;
  Sec[3] := 3;
  for I := 0 to 4 do
  begin
    for J := 0 to 3 do Storia[I].Colori[J] := DEMO[I, J];
    Valuta(Sec, Storia[I].Colori, Storia[I].Neri, Storia[I].Bianchi);
  end;
  NT := 5;
  NCorr := 0;
end;

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
  LblEsito.Caption := 'Questa e'' una partita di esempio. Premi "Gioca da solo" per giocare davvero.';
  MostraDemo;
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
  PreparaFondi;
  Cv.Draw(0, 0, FondoTavola);
  Prima := PrimaRigaVisibile;
  for Riga := 0 to RIGHE - 1 do
  begin
    Cy := TITOLO + MARGINE + Riga * CELLA + CELLA div 2;
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
      Cx := MARGINE + 22 + Col * PASSO_X;
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
      Cy := TITOLO + MARGINE + Riga * CELLA + CELLA div 2 - 10 + (K div 2) * 20;
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
  PreparaFondi;
  Cv.Draw(0, 0, FondoTavolozza);
  for I := 1 to 6 do
    DisegnaPiolo(Cv, LARG_PALETTE div 2, 35 + (I - 1) * 50, RAGGIO, COLORI[I]);
end;

end.
