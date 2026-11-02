program test_client;
{ PROVA del VERO unit1.pas del client (copiato come Unit1.pas) contro finte unita' LCL.
  Crea il form come la LCL, "preme" Connetti e poi gioca per eliminazione contro un server vero.
  Uso: test_client host nome modo     modo: gioca | spento | wait | errori }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, Controls, Forms, StdCtrls, ExtCtrls, Dialogs, Unit1;

var
  F: TForm1;
  cand: TStringList;
  nome, modo: String;
  t0: QWord;
  i, j, k, e, s, e2, s2, n: Integer;
  g, riga: String;
  used: array[1..6] of Integer;

procedure Fb(const a, b: String; out es, sp: Integer);
var ca, cb: array[1..6] of Integer; x: Integer;
begin
  FillChar(ca, SizeOf(ca), 0); FillChar(cb, SizeOf(cb), 0); es := 0; sp := 0;
  for x := 1 to 4 do
    if a[x] = b[x] then Inc(es)
    else begin Inc(ca[Ord(a[x]) - 48]); Inc(cb[Ord(b[x]) - 48]); end;
  for x := 1 to 6 do if ca[x] < cb[x] then Inc(sp, ca[x]) else Inc(sp, cb[x]);
end;

function Ultimo: String; begin Result := F.LblEsito.Caption; end;

begin
  nome := ParamStr(2); modo := ParamStr(3);
  F := TForm1(TForm1.NewInstance);
  F.LblIp := TLabel.Create(F); F.EdIp := TEdit.Create(F); F.LblNome := TLabel.Create(F);
  F.EdNome := TEdit.Create(F); F.BtnConnetti := TButton.Create(F); F.LblEsito := TLabel.Create(F);
  F.LblStato := TLabel.Create(F); F.LblTentativo := TLabel.Create(F); F.EdTentativo := TEdit.Create(F);
  F.BtnProva := TButton.Create(F); F.MemoStoria := TMemo.Create(F); F.LblMigliore := TLabel.Create(F);
  F.LblPeggiore := TLabel.Create(F); F.LblPosizione := TLabel.Create(F); F.LblFiniti := TLabel.Create(F);
  F.Timer1 := TTimer.Create(F);
  F.BtnProva.Enabled := False; F.Timer1.Enabled := False;    // come nel .lfm
  F.EdIp.Text := ParamStr(1); F.EdNome.Text := nome;
  F.AfterConstruction;
  if not Assigned(F.BtnConnetti.OnClick) or not Assigned(F.BtnProva.OnClick) or
     not Assigned(F.Timer1.OnTimer) or not F.Avviato then begin WriteLn('ERRORE collegamenti'); Halt(3); end;
  t0 := GetTickCount64;
  F.BtnConnetti.OnClick(nil);
  WriteLn(nome, ' connetti (', GetTickCount64 - t0, ' ms): ', F.LblEsito.Caption, ' | ', F.LblStato.Caption);
  if modo = 'spento' then
  begin
    if F.BtnProva.Enabled then begin WriteLn('ERRORE: Prova attivo senza server'); Halt(4); end;
    Halt(0);
  end;
  if modo = 'errori' then
  begin
    F.EdTentativo.Text := '12'; F.BtnProva.OnClick(nil); WriteLn('codice corto: ', Ultimo);
    F.EdTentativo.Text := '1237'; F.BtnProva.OnClick(nil); WriteLn('codice 7: ', Ultimo);
    F.EdTentativo.Text := 'abcd'; F.BtnProva.OnClick(nil); WriteLn('lettere: ', Ultimo);
    F.EdTentativo.Text := '1111'; F.BtnProva.OnClick(nil); WriteLn('prima del Via: ', Ultimo, ' | ', F.LblStato.Caption);
    Halt(0);
  end;
  if modo = 'wait' then
  begin
    F.EdTentativo.Text := '1234'; F.BtnProva.OnClick(nil); WriteLn('WAIT: ', Ultimo);
    Halt(0);
  end;
  { gioca: aspetta il Via con il Timer (come ogni 3 s) }
  while (Pos('GIOCO', F.LblStato.Caption) = 0) and (GetTickCount64 - t0 < 60000) do
  begin Sleep(300); F.Timer1.OnTimer(nil); end;
  if Pos('GIOCO', F.LblStato.Caption) = 0 then begin WriteLn(nome, ' ERRORE: Via mai arrivato: ', F.LblStato.Caption); Halt(5); end;
  cand := TStringList.Create;
  for i := 1 to 6 do for j := 1 to 6 do for k := 1 to 6 do for n := 1 to 6 do
    cand.Add(Chr(48+i)+Chr(48+j)+Chr(48+k)+Chr(48+n));
  n := 0;
  while (F.LblStato.Caption <> 'HAI VINTO!') and (n < 30) do
  begin
    Inc(n);
    g := cand[Random(cand.Count)];
    F.EdTentativo.Text := g; F.BtnProva.OnClick(nil);
    if F.LblStato.Caption = 'HAI VINTO!' then Break;
    riga := F.MemoStoria.Lines[F.MemoStoria.Lines.Count - 1];
    { dal memo: ...esatte E   spostate S }
    e := StrToIntDef(Copy(riga, Pos('esatte ', riga) + 7, 1), -1);
    s := StrToIntDef(Copy(riga, Pos('spostate ', riga) + 9, 1), -1);
    if e < 0 then begin WriteLn(nome, ' ERRORE memo: ', riga, ' | ', Ultimo); Halt(6); end;
    for i := cand.Count - 1 downto 0 do
    begin Fb(cand[i], g, e2, s2); if (e2 <> e) or (s2 <> s) then cand.Delete(i); end;
  end;
  if n >= 30 then begin WriteLn(nome, ' ERRORE: troppi tentativi'); Halt(7); end;
  F.Timer1.OnTimer(nil);
  WriteLn(nome, ' FINE tent=', n, ' | ', Ultimo, ' | ', F.LblPosizione.Caption, ' | ', F.LblMigliore.Caption, ' | ', F.LblPeggiore.Caption, ' | ', F.LblFiniti.Caption);
  WriteLn(nome, ' memo ultima: ', F.MemoStoria.Lines[F.MemoStoria.Lines.Count - 1]);
end.
