{ DisegnoMastermind.inc - il disegno CONDIVISO da Client e Server (versione v3.0).
  Si include con:  {$I ../Comune/DisegnoMastermind.inc}   dentro la parte "implementation".
  Idea per avere un disegno nitido su ogni schermo:
    1) si legge la scala dello schermo (S = PixelsPerInch / 96: 1, 1.25, 1.5 ...);
    2) si disegna in GRANDE (fattore K = 2 * S), come su una tela piu' fine;
    3) si RIMPICCIOLISCE sullo schermo con la modalita' "halftone" di Windows (tutti i punti
       vengono mediati): bordi morbidi, pioli senza scalini.
  Tutte le misure nel programma sono in "pixel di progetto" (schermo normale 100%):
  la funzione Sc(N) le porta ai pixel grandi del disegno. }

const
  SUPERCAMPIONAMENTO = 2;     // si disegna a 2 volte la risoluzione dello schermo

var
  Scala: Double = 1.0;        // S: scala dello schermo (arrotondata a 0.25, da 1 a 3)
  Fattore: Double = 2.0;      // K = SUPERCAMPIONAMENTO * S
  SemeLegno: Int64;
  BordoW, BordoH: Integer;

{$IFDEF WINDOWS}
{ la modalita' "halftone" e' nella gdi32 di Windows: la dichiariamo qui perche' non si puo'
  usare l'unita' Windows (ha un suo TBitmap che disturberebbe quello di Lazarus) }
function SetStretchBltMode(DC: PtrUInt; Mode: LongInt): LongInt; stdcall; external 'gdi32.dll' name 'SetStretchBltMode';
function SetBrushOrgEx(DC: PtrUInt; X, Y: LongInt; Old: Pointer): LongBool; stdcall; external 'gdi32.dll' name 'SetBrushOrgEx';
{$ENDIF}

{ ---------- la scala ---------- }

function ScalaDa(Ppi: Integer): Double;
var
  S: Double;
begin
  if Ppi < 96 then Ppi := 96;
  S := Round(Ppi / 96 * 4) / 4;          // a passi di 0.25: 1, 1.25, 1.5, 1.75, 2 ...
  if S < 1 then S := 1;
  if S > 3 then S := 3;
  Result := S;
end;

{ imposta Scala e Fattore. Risultato True se la scala e' cambiata (allora i fondi vanno rifatti) }
function ImpostaScala(Ppi: Integer): Boolean;
var
  N: Double;
begin
  N := ScalaDa(Ppi);
  Result := N <> Scala;
  Scala := N;
  Fattore := SUPERCAMPIONAMENTO * N;
end;

function Sc(N: Integer): Integer;        // da pixel di progetto a pixel grandi del disegno
begin
  Result := Round(N * Fattore);
end;

function ScF(N: Double): Double;
begin
  Result := N * Fattore;
end;

{ ---------- rimpicciolire con la modalita' liscia ---------- }

procedure ModoLiscio(Cv: TCanvas);
begin
{$IFDEF WINDOWS}
  SetStretchBltMode(Cv.Handle, 4);       // 4 = HALFTONE
  SetBrushOrgEx(Cv.Handle, 0, 0, nil);
{$ENDIF}
end;

{ copia la bitmap grande Sorg dentro il rettangolo R di Dest, rimpicciolendola con la media dei punti }
procedure RiduciSu(Dest: TCanvas; const R: TRect; Sorg: TBitmap);
begin
  ModoLiscio(Dest);
  Dest.CopyRect(R, Sorg.Canvas, Rect(0, 0, Sorg.Width, Sorg.Height));
end;

{ ---------- i colori ---------- }

function MioColore(R, G, B: Integer): Integer;
begin
  Result := R or (G shl 8) or (B shl 16);
end;

function Schiarisci(Col, Perc: Integer): Integer;     // mischia col bianco (Perc da 0 a 100)
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

function Scurisci(Col, Perc: Integer): Integer;       // mischia col nero (Perc da 0 a 100)
var
  R, G, B: Integer;
begin
  R := (Col and $FF) * (100 - Perc) div 100;
  G := ((Col shr 8) and $FF) * (100 - Perc) div 100;
  B := ((Col shr 16) and $FF) * (100 - Perc) div 100;
  Result := MioColore(R, G, B);
end;

function Mescola(A, B, Perc: Integer): Integer;       // A mescolato con B (Perc% di B)
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

{ ---------- il "caso" tutto nostro con il seme fisso: il legno e' SEMPRE uguale ---------- }

procedure InizioCaso(S: Integer);
begin
  SemeLegno := S;
end;

function Caso(N: Integer): Integer;       // un numero da 0 a N-1, sempre la stessa sequenza
begin
  if N < 1 then N := 1;
  SemeLegno := (SemeLegno * 1103515245 + 12345) and $7FFFFFFF;
  Result := (SemeLegno shr 8) mod N;
end;

{ ---------- il legno: fibre sottili, toni morbidi, striature, fessure, pori, un nodino ---------- }

{ il colore del legno in un punto (X e Y in pixel grandi): dal miele al rovere con macchie
  larghe e morbide, un po' piu' scuro vicino ai bordi }
function TonoLegno(X, Y: Integer): Integer;
var
  F, V: Integer;
  Xn, Yn: Double;
begin
  Xn := X / Fattore;
  Yn := Y / Fattore;
  F := 50 + Round(26 * Sin(Yn * 0.011 + Xn * 0.0028 + 0.7) + 14 * Sin(Yn * 0.029 - Xn * 0.0049 + 2.1) +
    8 * Sin(Xn * 0.011 + Yn * 0.017));
  if F < 0 then F := 0;
  if F > 100 then F := 100;
  Result := Mescola(MioColore(212, 166, 102), MioColore(170, 120, 66), F * 7 div 10);
  V := X;
  if BordoW - 1 - X < V then V := BordoW - 1 - X;
  if Y < V then V := Y;
  if BordoH - 1 - Y < V then V := BordoH - 1 - Y;
  if V < 0 then V := 0;
  V := Round(V / Fattore);
  if V < 34 then Result := Mescola(Result, MioColore(48, 26, 10), (34 - V) * 30 div 34);
end;

{ disegna il legno su tutto il canvas C grande W x H pixel grandi. Semi = seme del caso }
procedure DisegnaLegno(C: TCanvas; W, H, Semi: Integer);
var
  I, N, X, Y, Y0, X0, Lun, Xe, Perc, K, Pezzo, Pas, Area: Integer;
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
      D := D + ScF(6) * (Yb - NodoY) / (Abs(Yb - NodoY) + ScF(12)) * Exp(-Sqr((Xp - NodoX) / ScF(26)));
    Result := Yb + Round(D);
  end;

begin
  BordoW := W;
  BordoH := H;
  InizioCaso(Semi);
  Pas := Sc(3);                                  // lunghezza dei piccoli tratti delle fibre
  if Pas < 2 then Pas := 2;
  Area := Round(W * H / (Fattore * Fattore));    // l'area in pixel di progetto: il numero di fibre non cambia con la scala
  C.Brush.Style := bsSolid;
  C.Pen.Style := psSolid;
  C.Pen.Width := 1;
  NNodi := 0;
  NodoX := 0;
  NodoY := 0;
  if (W >= Sc(200)) and (H >= Sc(300)) then      // un solo nodino piccolo, solo sul legno grande
  begin
    NNodi := 1;
    NodoX := Sc(60) + Caso(W - Sc(120));
    NodoY := Sc(100) + Caso(H - Sc(200));
  end;
  // 1) i toni di base: una riga alla volta, il colore cambia piano piano (niente righe nette)
  Y := 0;
  while Y < H do
  begin
    X := 0;
    C.Pen.Color := TonoLegno(0, Y);
    C.MoveTo(0, Y);
    while X < W do
    begin
      Inc(X, Sc(3));
      C.Pen.Color := TonoLegno(X, Y);
      C.LineTo(X, Y);
    end;
    Inc(Y);
  end;
  // 2) le fibre: tante linee sottilissime, un po' piu' chiare o piu' scure del legno sotto
  N := Area div 55;
  for I := 1 to N do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - Sc(30);
    Lun := Sc(60) + Caso(W + Sc(40));
    Amp := ScF(1.0 + Caso(35) / 10.0);
    Fre := (0.005 + Caso(16) / 1000.0) / Fattore;
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
      Inc(X, Pas);
      C.LineTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    end;
  end;
  // 3) qualche striatura piu' scura, lunga e sottile
  for I := 1 to Area div 4000 do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - Sc(40);
    Lun := Sc(100) + Caso(W);
    Amp := ScF(2.0 + Caso(30) / 10.0);
    Fre := (0.004 + Caso(9) / 1000.0) / Fattore;
    Fase := Caso(628) / 100.0;
    Perc := 40 + Caso(18);
    C.Pen.Color := Mescola(TonoLegno(Dentro(X0), Y0), MioColore(60, 34, 12), Perc);
    X := X0;
    C.MoveTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    Xe := X0 + Lun;
    while X < Xe do
    begin
      Inc(X, Pas);
      C.LineTo(X, Deforma(X, Y0, Amp, Fre, Fase));
    end;
  end;
  // 4) qualche fessura sottile e interrotta
  for I := 1 to 3 + Area div 30000 do
  begin
    Y0 := Caso(H);
    X0 := Caso(W) - Sc(30);
    Lun := Sc(80) + Caso(W);
    Fase := Caso(628) / 100.0;
    X := X0;
    while X < X0 + Lun do
    begin
      Pezzo := Sc(8) + Caso(Sc(40));
      C.Pen.Color := Mescola(TonoLegno(Dentro(X), Y0), MioColore(30, 16, 6), 66 + Caso(10));
      C.MoveTo(X, Deforma(X, Y0, ScF(2.0), 0.012 / Fattore, Fase));
      Xe := X + Pezzo;
      while X < Xe do
      begin
        Inc(X, Pas);
        C.LineTo(X, Deforma(X, Y0, ScF(2.0), 0.012 / Fattore, Fase));
      end;
      Inc(X, Sc(4) + Caso(Sc(24)));
    end;
  end;
  // 5) i pori: piccoli trattini scuri lunghi 3-14 pixel di progetto
  for I := 1 to Area div 200 do
  begin
    X := Caso(W);
    Y := Caso(H);
    Lun := Sc(3) + Caso(Sc(12));
    Perc := 34 + Caso(21);
    C.Pen.Color := Mescola(TonoLegno(X, Y), MioColore(50, 28, 10), Perc);
    C.MoveTo(X, Deforma(X, Y, ScF(1.5), 0.012 / Fattore, 1.0));
    C.LineTo(X + Lun, Deforma(X + Lun, Y, ScF(1.5), 0.012 / Fattore, 1.0));
  end;
  // 6) il nodino: tre anelli sottili e un centro scuro
  if NNodi > 0 then
  begin
    C.Brush.Style := bsClear;
    Tono := TonoLegno(NodoX, NodoY);
    for K := 3 downto 1 do
    begin
      C.Pen.Color := Mescola(Tono, MioColore(60, 34, 12), 16 + K * 4);
      C.Ellipse(NodoX - Sc(K * 5 + 3), NodoY - Sc(K * 2 + 2), NodoX + Sc(K * 5 + 4), NodoY + Sc(K * 2 + 3));
    end;
    C.Brush.Style := bsSolid;
    C.Brush.Color := Mescola(Tono, MioColore(40, 22, 8), 55);
    C.Pen.Color := C.Brush.Color;
    C.Ellipse(NodoX - Sc(3), NodoY - Sc(2), NodoX + Sc(4), NodoY + Sc(3));
  end;
  // 7) la cornice lucida: luce in alto a sinistra, ombra in basso a destra
  C.Brush.Style := bsClear;
  C.Pen.Width := Sc(6);
  C.Pen.Color := MioColore(84, 50, 22);
  C.Rectangle(0, 0, W, H);
  C.Pen.Width := Sc(1);
  C.Pen.Color := MioColore(150, 100, 52);
  C.Rectangle(Sc(3), Sc(3), W - Sc(3), H - Sc(3));
  C.Pen.Color := MioColore(232, 190, 132);
  C.MoveTo(Sc(4), Sc(4));
  C.LineTo(W - Sc(5), Sc(4));
  C.MoveTo(Sc(4), Sc(4));
  C.LineTo(Sc(4), H - Sc(5));
  C.Pen.Color := MioColore(255, 230, 176);
  C.MoveTo(Sc(8), Sc(6));
  C.LineTo(W - Sc(14), Sc(6));
  C.Pen.Color := MioColore(54, 30, 12);
  C.MoveTo(W - Sc(5), Sc(5));
  C.LineTo(W - Sc(5), H - Sc(5));
  C.LineTo(Sc(4), H - Sc(5));
  C.Pen.Width := 1;
  C.Brush.Style := bsSolid;
end;

{ la scritta INTAGLIATA nel legno: ombra scura in alto a sinistra, bordo chiaro in basso a destra.
  W e Alt in pixel grandi }
procedure IncidiScritta(C: TCanvas; W, Alt: Integer; const Testo: String);
var
  Tx, Ty: Integer;
begin
  C.Brush.Style := bsClear;
  C.Font.Name := 'Arial';
  C.Font.Height := -Sc(29);              // altezza in pixel (negativa = pixel veri, non punti)
  C.Font.Style := [fsBold];
  C.Font.Quality := fqCleartype;
  Tx := (W - C.TextWidth(Testo)) div 2;
  Ty := (Alt - C.TextHeight(Testo)) div 2;
  C.Font.Color := MioColore(46, 24, 8);
  C.TextOut(Tx - Sc(1), Ty - Sc(1), Testo);
  C.Font.Color := MioColore(236, 194, 134);
  C.TextOut(Tx + Sc(1), Ty + Sc(1), Testo);
  C.Font.Color := MioColore(98, 58, 26);
  C.TextOut(Tx, Ty, Testo);
  C.Brush.Style := bsSolid;
end;

{ ---------- buchi e pioli (centro e raggio in pixel grandi) ---------- }

procedure DisegnaBuco(C: TCanvas; Cx, Cy, R: Integer);
begin
  C.Pen.Style := psClear;
  C.Brush.Color := MioColore(48, 28, 12);                      // bordo scuro
  C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
  C.Brush.Color := MioColore(92, 58, 30);                      // labbro chiaro in basso a destra
  C.Ellipse(Cx - R + Sc(1), Cy - R + Sc(1), Cx + R, Cy + R);
  C.Brush.Color := MioColore(52, 30, 14);
  C.Ellipse(Cx - R + Sc(2), Cy - R + Sc(2), Cx + R - Sc(1), Cy + R - Sc(1));
  C.Brush.Color := MioColore(40, 22, 8);                       // il fondo
  C.Ellipse(Cx - R + Sc(3), Cy - R + Sc(3), Cx + R - Sc(2), Cy + R - Sc(2));
  C.Pen.Style := psSolid;
end;

{ un piolo: contorno scuro, almeno 9 anelli sempre piu' chiari e piu' piccoli, spostati in alto
  a sinistra (sembra una sfera), e un riflesso morbido }
procedure DisegnaPiolo(C: TCanvas; Cx, Cy, R, Col: Integer);
var
  K, Rk, Off, Ri: Integer;
begin
  C.Pen.Style := psClear;
  C.Brush.Color := MioColore(36, 20, 8);                        // l'ombra sul legno (due passate = bordo sfumato)
  C.Ellipse(Cx - R + Sc(2), Cy - R + Sc(3), Cx + R + Sc(3) + 1, Cy + R + Sc(4) + 1);
  C.Brush.Color := MioColore(52, 30, 12);
  C.Ellipse(Cx - R + Sc(2), Cy - R + Sc(2), Cx + R + Sc(2) + 1, Cy + R + Sc(3) + 1);
  C.Brush.Color := Scurisci(Col, 42);                           // il contorno del piolo
  C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
  Ri := R - Sc(1);
  for K := 0 to 9 do
  begin
    Rk := Ri - (K * Ri) div 12;
    Off := -(K * Ri) div 24;
    C.Brush.Color := Schiarisci(Col, K * 7);
    C.Ellipse(Cx + Off - Rk, Cy + Off - Rk, Cx + Off + Rk + 1, Cy + Off + Rk + 1);
  end;
  C.Brush.Color := Schiarisci(Col, 78);                         // il riflesso
  C.Ellipse(Cx - R div 2 - R div 8, Cy - R div 2 - R div 8, Cx - R div 4, Cy - R div 4);
  C.Pen.Style := psSolid;
end;

{ piolino di risposta: nero o bianco, con contorno e riflesso. Il corpo ha raggio R }
procedure DisegnaRisposta(C: TCanvas; Cx, Cy, R: Integer; Nero: Boolean);
begin
  C.Pen.Style := psClear;
  if Nero then
  begin
    C.Brush.Color := MioColore(30, 18, 8);
    C.Ellipse(Cx - R - Sc(1), Cy - R - Sc(1), Cx + R + Sc(1) + 1, Cy + R + Sc(1) + 1);
    C.Brush.Color := MioColore(12, 12, 12);
    C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
    C.Brush.Color := MioColore(90, 90, 90);
    C.Ellipse(Cx - R div 2 - 1, Cy - R div 2 - 1, Cx - R div 6, Cy - R div 6);
  end
  else
  begin
    C.Brush.Color := MioColore(170, 170, 170);
    C.Ellipse(Cx - R - Sc(1), Cy - R - Sc(1), Cx + R + Sc(1) + 1, Cy + R + Sc(1) + 1);
    C.Brush.Color := MioColore(235, 235, 235);
    C.Ellipse(Cx - R, Cy - R, Cx + R + 1, Cy + R + 1);
    C.Brush.Color := MioColore(255, 255, 255);
    C.Ellipse(Cx - R div 2 - 1, Cy - R div 2 - 1, Cx - R div 6, Cy - R div 6);
  end;
  C.Pen.Style := psSolid;
end;

{ una scanalatura (linea scura + linea chiara sotto) tra X1 e X2 all'altezza Y, in pixel grandi }
procedure DisegnaScanalatura(C: TCanvas; X1, X2, Y: Integer);
begin
  C.Pen.Style := psSolid;
  C.Pen.Width := Sc(2);
  C.Pen.Color := MioColore(84, 50, 22);
  C.MoveTo(X1, Y);
  C.LineTo(X2, Y);
  C.Pen.Width := Sc(1);
  C.Pen.Color := MioColore(232, 190, 132);
  C.MoveTo(X1, Y + Sc(2));
  C.LineTo(X2, Y + Sc(2));
  C.Pen.Width := 1;
end;
