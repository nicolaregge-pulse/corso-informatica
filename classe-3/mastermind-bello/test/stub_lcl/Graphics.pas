unit Graphics;
{ FINTA unita' LCL: il "canvas" non disegna, ma si ricorda ogni cerchio (raggio e colore),
  cosi' il test puo' contare i piolini neri e bianchi che il programma disegna.
  Ha anche i pezzi che servono per il legno: font, testo, bitmap. }
{$mode objfpc}{$H+}
interface
uses Classes, SysUtils, Types;
type
  TColor = Longint;
  TPenStyle = (psSolid, psClear);
  TBrushStyle = (bsSolid, bsClear);
  TFontStyle = (fsBold, fsItalic, fsUnderline, fsStrikeOut);
  TFontStyles = set of TFontStyle;
  TFontQuality = (fqDefault, fqDraft, fqProof, fqNonAntialiased, fqAntialiased, fqCleartype);
  TPen = class
  public
    Color: TColor; Width: Integer; Style: TPenStyle;
  end;
  TBrush = class
  public
    Color: TColor; Style: TBrushStyle;
  end;
  TFont = class
  public
    Name: String; Size, Height: Integer; Color: TColor; Style: TFontStyles; Quality: TFontQuality;
  end;
  TCanvas = class;
  TBitmap = class
  public
    Canvas: TCanvas;
    Width, Height: Integer;
    constructor Create;
  end;
  TCanvas = class
  public
    Pen: TPen;
    Brush: TBrush;
    Font: TFont;
    Cerchi: TStringList;      // "raggio;colore" per ogni Ellipse
    Rettangoli, Linee, Testi, Copie: Integer;
    constructor Create;
    procedure Rectangle(X1, Y1, X2, Y2: Integer);
    procedure Ellipse(X1, Y1, X2, Y2: Integer);
    procedure MoveTo(X, Y: Integer);
    procedure LineTo(X, Y: Integer);
    procedure TextOut(X, Y: Integer; const S: String);
    function TextWidth(const S: String): Integer;
    function TextHeight(const S: String): Integer;
    procedure Draw(X, Y: Integer; B: TBitmap);
    procedure CopyRect(const Dest: TRect; Canvas: TCanvas; const Source: TRect);
    procedure RoundRect(X1, Y1, X2, Y2, RX, RY: Integer);
    procedure Pulisci;
  end;
implementation
constructor TBitmap.Create;
begin
  Canvas := TCanvas.Create;
end;
constructor TCanvas.Create;
begin
  Pen := TPen.Create; Brush := TBrush.Create; Font := TFont.Create; Cerchi := TStringList.Create;
end;
procedure TCanvas.CopyRect(const Dest: TRect; Canvas: TCanvas; const Source: TRect);
begin
  Inc(Copie);
end;
procedure TCanvas.RoundRect(X1, Y1, X2, Y2, RX, RY: Integer);
begin
  Inc(Rettangoli);
end;
procedure TCanvas.Pulisci;
begin
  Cerchi.Clear; Rettangoli := 0; Linee := 0; Testi := 0; Copie := 0;
end;
procedure TCanvas.Rectangle(X1, Y1, X2, Y2: Integer);
begin
  Inc(Rettangoli);
end;
procedure TCanvas.Ellipse(X1, Y1, X2, Y2: Integer);
begin
  Cerchi.Add(IntToStr((X2 - X1) div 2) + ';' + IntToStr(Brush.Color));
end;
procedure TCanvas.MoveTo(X, Y: Integer);
begin
end;
procedure TCanvas.LineTo(X, Y: Integer);
begin
  Inc(Linee);
end;
procedure TCanvas.TextOut(X, Y: Integer; const S: String);
begin
  Inc(Testi);
end;
function TCanvas.TextWidth(const S: String): Integer;
begin
  if Font.Height <> 0 then Result := Length(S) * (Abs(Font.Height) * 5 div 9) else
  Result := Length(S) * (Font.Size * 2 div 3 + 4);
end;
function TCanvas.TextHeight(const S: String): Integer;
begin
  if Font.Height <> 0 then Result := Abs(Font.Height) * 5 div 4 else
  Result := Font.Size * 4 div 3 + 2;
end;
procedure TCanvas.Draw(X, Y: Integer; B: TBitmap);
begin
  Inc(Copie);
end;
end.
