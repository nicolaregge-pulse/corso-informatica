unit Dialogs;
{ FINTA: ShowMessage scrive su un file di log, MessageDlg risponde Si' (o No se RISPOSTA_NO). }
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
var
  MessaggiMostrati: TStringList;
  RispostaDlg: TModalResult = 6;
procedure ShowMessage(const Msg: String);
function MessageDlg(const aMsg: String; DlgType: TMsgDlgType; Buttons: TMsgDlgButtons; HelpCtx: Longint): TModalResult;
implementation
procedure ShowMessage(const Msg: String);
begin
  MessaggiMostrati.Add('ShowMessage: ' + Msg);
end;
function MessageDlg(const aMsg: String; DlgType: TMsgDlgType; Buttons: TMsgDlgButtons; HelpCtx: Longint): TModalResult;
begin
  MessaggiMostrati.Add('MessageDlg: ' + aMsg);
  Result := RispostaDlg;
end;
initialization
  MessaggiMostrati := TStringList.Create;
end.
