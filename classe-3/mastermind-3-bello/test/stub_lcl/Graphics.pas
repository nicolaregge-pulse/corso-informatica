unit Graphics;
{ FINTA unita' LCL: il "canvas" non disegna, ma si ricorda ogni cerchio (raggio e colore),
  cosi' il test puo' contare i piolini neri e bianchi che il programma disegna. }
{$mode objfpc}{$H+}
interface
uses Classes, SysUtils;
type
  TColor = Longint;
  TPenStyle = (psSolid, psClear);
  TBrushStyle = (bsSolid, bsClear);
  TPen = class
  public
    Color: TColor; Width: Integer; Style: TPenStyle;
  end;
  TBrush = class
  public
    Color: TColor; Style: TBrushStyle;
  end;
  TCanvas = class
  public
    Pen: TPen;
    Brush: TBrush;
    Cerchi: TStringList;      // "raggio;colore" per ogni Ellipse con la penna trasparente
    Rettangoli, Linee: Integer;
    constructor Create;
    procedure Rectangle(X1, Y1, X2, Y2: Integer);
    procedure Ellipse(X1, Y1, X2, Y2: Integer);
    procedure MoveTo(X, Y: Integer);
    procedure LineTo(X, Y: Integer);
    procedure Pulisci;
  end;
implementation
constructor TCanvas.Create;
begin
  Pen := TPen.Create; Brush := TBrush.Create; Cerchi := TStringList.Create;
end;
procedure TCanvas.Pulisci;
begin
  Cerchi.Clear; Rettangoli := 0; Linee := 0;
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
end.
