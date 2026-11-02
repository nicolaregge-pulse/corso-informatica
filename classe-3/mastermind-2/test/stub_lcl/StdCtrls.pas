unit StdCtrls;
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
type
  TButton = class(TControl) end;
  TEdit = class(TControl) end;
  TLabel = class(TControl) end;
  TMemo = class(TControl) public Lines: TStrings; constructor Create(AOwner: TComponent); override; end;
implementation
constructor TMemo.Create(AOwner: TComponent); begin inherited; Lines := TStringList.Create; end;
end.
