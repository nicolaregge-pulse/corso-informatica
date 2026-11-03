program test_server;
{ PROVA della VERA unit1_server.pas (copiata come UnitServer.pas) contro finte unita' LCL.
  Fa quello che farebbe Lazarus: crea i componenti, chiama FormCreate, "preme" Avvia server,
  poi chiama Timer1Timer ogni 50 ms (come il TTimer) mentre 22 client veri (script Python)
  bussano alla porta. Dopo 3 s preme "Via!". Alla fine scrive griglia, registro e messaggi.
  Uso: test_server porta cartella_file_di_marcatura cartella_uscita }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, Controls, Forms, StdCtrls, ExtCtrls, Grids, Dialogs, UnitServer;

var
  F: TFormServer;
  porta, marc, uscita: String;
  t0: QWord;
  viaDato, finito: Boolean;
  quando: QWord;
  r, c: Integer;
  riga: String;
  out_: TStringList;
  ticks: Integer;

function Nuovo(C: TComponentClass): TComponent;
begin
  Result := C.Create(nil);
end;

begin
  porta := ParamStr(1); marc := ParamStr(2); uscita := ParamStr(3);
  { come la LCL vera: prima si costruiscono i componenti, poi scatta AfterConstruction }
  F := TFormServer(TFormServer.NewInstance);   { senza costruttore: niente AfterConstruction anticipato }
  F.LblPorta := TLabel.Create(F); F.EdPorta := TEdit.Create(F); F.BtnAvvia := TButton.Create(F);
  F.LblStato := TLabel.Create(F); F.LblIp := TLabel.Create(F); F.LblIndirizzo := TLabel.Create(F);
  F.EdIndirizzo := TEdit.Create(F); F.BtnVia := TButton.Create(F); F.BtnNuova := TButton.Create(F);
  F.PbSegreto := TPaintBox.Create(F); F.BtnStop := TButton.Create(F); F.BtnMostra := TButton.Create(F); F.LblGiocatori := TLabel.Create(F); F.LblClassifica := TLabel.Create(F);
  F.LblRegistro := TLabel.Create(F); F.Griglia := TStringGrid.Create(F); F.MemoRegistro := TMemo.Create(F);
  F.Timer1 := TTimer.Create(F);
  F.BtnVia.Enabled := False; F.BtnNuova.Enabled := False; F.BtnStop.Enabled := False; F.BtnMostra.Enabled := False;   // come nel .lfm
  F.EdPorta.Text := porta;
  if ParamStr(4) = 'a' then   // caso (a): eventi gia' collegati dal .lfm, il form chiama FormCreate
  begin
    F.BtnAvvia.OnClick := @F.BtnAvviaClick; F.BtnVia.OnClick := @F.BtnViaClick;
    F.BtnNuova.OnClick := @F.BtnNuovaClick; F.BtnStop.OnClick := @F.BtnStopClick; F.BtnMostra.OnClick := @F.BtnMostraClick; F.PbSegreto.OnPaint := @F.PbSegretoPaint; F.PbSegreto.OnClick := @F.BtnMostraClick;
    F.EdPorta.OnChange := @F.EdPortaChange; F.Timer1.OnTimer := @F.Timer1Timer;
    F.OnDestroy := @F.FormDestroy;
    F.FormCreate(nil);
    F.AfterConstruction;
    if not F.Avviato then begin WriteLn('ERRORE: Avviato falso'); Halt(3); end;
  end
  else F.AfterConstruction;   // caso (b): non collegati, AfterConstruction fa tutto
  if not Assigned(F.BtnAvvia.OnClick) or not Assigned(F.OnDestroy) or not F.Avviato then begin WriteLn('ERRORE: collegamenti/Avviato'); Halt(3); end;
  F.BtnAvviaClick(nil);                 // clic su "Avvia server"
  t0 := GetTickCount64; viaDato := False; finito := False; ticks := 0;
  quando := 0;
  while GetTickCount64 - t0 < 120000 do
  begin
    if F.Timer1.Enabled then begin F.Timer1Timer(nil); Inc(ticks); end;
    Sleep(50);
    if (not viaDato) and (GetTickCount64 - t0 > 3000) and F.BtnVia.Enabled then
    begin F.BtnViaClick(nil); F.BtnStopClick(nil); F.BtnViaClick(nil); F.BtnMostraClick(nil); F.PbSegreto.Canvas.Pulisci; F.PbSegreto.OnPaint(nil); viaDato := True; end;
    if FileExists(marc) then
    begin
      if quando = 0 then quando := GetTickCount64;
      if GetTickCount64 - quando > 2500 then Break;   // ancora qualche giro per ridisegnare
    end;
  end;
  out_ := TStringList.Create;
  out_.Add('Stato: ' + F.LblStato.Caption);
  out_.Add('Codice: ' + F.BtnMostra.Caption + ' - cerchi disegnati nel pannello: ' + IntToStr(F.PbSegreto.Canvas.Cerchi.Count));
  out_.Add('IP: ' + F.LblIp.Caption + '  Indirizzo: ' + F.EdIndirizzo.Text);
  out_.Add(F.LblGiocatori.Caption);
  out_.Add('Righe di griglia: ' + IntToStr(F.Griglia.RowCount) + '   Timer chiamato ' + IntToStr(ticks) + ' volte');
  for r := 0 to F.Griglia.RowCount - 1 do
  begin
    riga := '';
    for c := 0 to 5 do riga := riga + F.Griglia.Cells[c, r] + ' | ';
    out_.Add(riga);
  end;
  out_.SaveToFile(uscita + '/griglia.txt');
  F.MemoRegistro.Lines.SaveToFile(uscita + '/registro.txt');
  MessaggiMostrati.SaveToFile(uscita + '/messaggi.txt');
  F.FormDestroy(nil);
  F.Free;
  WriteLn('FINE test_server');
end.
