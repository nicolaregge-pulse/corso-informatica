unit Forms;
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
type
  TKeyPressEvent = procedure(Sender: TObject; var Key: Char) of object;
  TForm = class(TControl)
  public
    OnDestroy: TNotifyEvent;
    KeyPreview: Boolean;               // nella vera LCL esiste: la finestra legge i tasti prima dei controlli
    OnKeyPress: TKeyPressEvent;
    PixelsPerInch: Integer;            // la scala dello schermo (96 = 100%)
    ActiveControl: TControl;           // nella vera LCL e' il controllo con il fuoco
  end;
implementation
end.
