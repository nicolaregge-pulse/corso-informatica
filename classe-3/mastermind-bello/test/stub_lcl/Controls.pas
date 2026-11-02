unit Controls;
{ FINTA unita' LCL: serve solo a controllare che il codice compili e giri. NON e' la vera LCL. }
{$mode objfpc}{$H+}
interface
uses Classes;
type
  TModalResult = Integer;
  TMsgDlgType = (mtWarning, mtError, mtInformation, mtConfirmation);
  TMsgDlgBtn = (mbYes, mbNo, mbOK, mbCancel);
  TMsgDlgButtons = set of TMsgDlgBtn;
  TMouseButton = (mbLeft, mbRight, mbMiddle);
  TShiftStateEnum = (ssShift, ssAlt, ssCtrl);
  TShiftState = set of TShiftStateEnum;
  TMouseEvent = procedure(Sender: TObject; Button: TMouseButton; Shift: TShiftState; X, Y: Integer) of object;
  TControl = class(TComponent)
  public
    Caption: String;
    Enabled: Boolean;
    Width, Height: Integer;
    OnClick: TNotifyEvent;
    constructor Create(AOwner: TComponent); override;
  end;
const
  mrYes = 6;
  mrNo = 7;
implementation
constructor TControl.Create(AOwner: TComponent);
begin
  inherited Create(AOwner);
  Enabled := True;
end;
end.
