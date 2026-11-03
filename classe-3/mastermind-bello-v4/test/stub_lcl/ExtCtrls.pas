unit ExtCtrls;
{$mode objfpc}{$H+}
interface
uses Classes, Controls, Graphics;
type
  TTimer = class(TControl) public Interval: Integer; OnTimer: TNotifyEvent; end;
  TPaintBox = class(TControl)
  public
    Canvas: TCanvas;
    OnPaint: TNotifyEvent;
    OnMouseDown: TMouseEvent;
    Rifatta: Integer;
    constructor Create(AOwner: TComponent); override;
    procedure Invalidate;
  end;
implementation
constructor TPaintBox.Create(AOwner: TComponent);
begin
  inherited Create(AOwner);
  Canvas := TCanvas.Create;
end;
procedure TPaintBox.Invalidate;
begin
  Inc(Rifatta);
end;
end.
