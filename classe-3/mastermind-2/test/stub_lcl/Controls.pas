unit Controls;
{$mode objfpc}{$H+}
interface
uses Classes;
type TControl = class(TComponent) public Caption: String; Text: String; Enabled: Boolean; procedure Clear; end;
implementation
procedure TControl.Clear; begin Text := ''; end;
end.
