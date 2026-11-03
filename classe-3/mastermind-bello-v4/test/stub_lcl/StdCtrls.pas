unit StdCtrls;
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
type
  TLabel = class(TControl) end;
  TButton = class(TControl) end;
  TEdit = class(TControl) public Text: String; OnChange: TNotifyEvent; end;
  TMemo = class(TControl)
  public
    Lines: TStringList;
    SelStart: Integer;
    constructor Create(AOwner: TComponent); override;
    function GetTextLen: Integer;
  end;
implementation
constructor TMemo.Create(AOwner: TComponent);
begin
  inherited Create(AOwner);
  Lines := TStringList.Create;
end;
function TMemo.GetTextLen: Integer;
begin
  Result := Length(Lines.Text);
end;
end.
