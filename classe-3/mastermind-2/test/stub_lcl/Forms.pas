unit Forms;
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
type
  TCloseAction = (caNone, caHide, caFree, caMinimize);
  TForm = class(TComponent) end;
  TApplication = class public ExeName: String; end;
var Application: TApplication;
implementation
end.
