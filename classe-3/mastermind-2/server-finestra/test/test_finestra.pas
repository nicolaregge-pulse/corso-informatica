program test_finestra;
{ PROVA della VERA unit1_server.pas (copiata come Unit1.pas) contro finte unita' LCL.
  Fa quello che farebbe Lazarus: crea i componenti, chiama FormCreate, "preme" Avvia server,
  poi chiama Timer1Timer ogni 50 ms (come il TTimer) mentre 22 client veri (script Python)
  bussano alla porta. Dopo 3 s preme "Via!". Alla fine scrive griglia, registro e messaggi.
  Uso: test_finestra porta cartella_file_di_marcatura cartella_uscita }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, Controls, Forms, StdCtrls, ExtCtrls, Grids, Dialogs, Unit1;

var
  F: TForm1;
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
  F := TForm1.Create(nil);
  F.LblPorta := TLabel.Create(F); F.EdPorta := TEdit.Create(F); F.BtnAvvia := TButton.Create(F);
  F.LblStato := TLabel.Create(F); F.LblIp := TLabel.Create(F); F.LblIndirizzo := TLabel.Create(F);
  F.EdIndirizzo := TEdit.Create(F); F.BtnVia := TButton.Create(F); F.BtnNuova := TButton.Create(F);
  F.LblSegreto := TLabel.Create(F); F.LblGiocatori := TLabel.Create(F); F.LblClassifica := TLabel.Create(F);
  F.LblRegistro := TLabel.Create(F); F.Griglia := TStringGrid.Create(F); F.MemoRegistro := TMemo.Create(F);
  F.Timer1 := TTimer.Create(F);
  F.BtnVia.Enabled := False; F.BtnNuova.Enabled := False;   // come nel .lfm
  F.EdPorta.Text := porta;
  F.FormCreate(nil);
  F.BtnAvviaClick(nil);                 // clic su "Avvia server"
  t0 := GetTickCount64; viaDato := False; finito := False; ticks := 0;
  quando := 0;
  while GetTickCount64 - t0 < 120000 do
  begin
    if F.Timer1.Enabled then begin F.Timer1Timer(nil); Inc(ticks); end;
    Sleep(50);
    if (not viaDato) and (GetTickCount64 - t0 > 3000) and F.BtnVia.Enabled then
    begin F.BtnViaClick(nil); viaDato := True; end;
    if FileExists(marc) then
    begin
      if quando = 0 then quando := GetTickCount64;
      if GetTickCount64 - quando > 2500 then Break;   // ancora qualche giro per ridisegnare
    end;
  end;
  out_ := TStringList.Create;
  out_.Add('Stato: ' + F.LblStato.Caption);
  out_.Add('Segreto: ' + F.LblSegreto.Caption);
  out_.Add('IP: ' + F.LblIp.Caption + '  Indirizzo: ' + F.EdIndirizzo.Text);
  out_.Add(F.LblGiocatori.Caption);
  out_.Add('Righe di griglia: ' + IntToStr(F.Griglia.RowCount) + '   Timer chiamato ' + IntToStr(ticks) + ' volte');
  for r := 0 to F.Griglia.RowCount - 1 do
  begin
    riga := '';
    for c := 0 to 3 do riga := riga + F.Griglia.Cells[c, r] + ' | ';
    out_.Add(riga);
  end;
  out_.SaveToFile(uscita + '/griglia.txt');
  F.MemoRegistro.Lines.SaveToFile(uscita + '/registro.txt');
  MessaggiMostrati.SaveToFile(uscita + '/messaggi.txt');
  F.FormDestroy(nil);
  F.Free;
  WriteLn('FINE test_finestra');
end.
