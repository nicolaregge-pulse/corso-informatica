program test_server;
{ PROVA della VERA unit1_server.pas (copiata come UnitServer.pas) contro finte unita' LCL.
  Fa quello che farebbe Lazarus: crea i componenti, chiama FormCreate, "preme" Avvia server,
  poi chiama Timer1Timer ogni 50 ms (come il TTimer) mentre 22 client veri (script Python)
  bussano alla porta. Dopo 3 s preme "Via!". Alla fine scrive griglia, registro e messaggi.
  Uso: test_server porta cartella_file_di_marcatura cartella_uscita [a|b [gara [numero_forti]]]
  Con "gara" il prof preme "Inizia gara" (3 codici da 14 secondi, pausa 1 s) invece di "Via!", e quando nel
  codice 3 hanno risolto tutti i "forti" preme "Prossimo codice". Alla fine scrive gara_dump.txt. }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, Controls, Forms, StdCtrls, ExtCtrls, Grids, Dialogs, UnitServer, UnitGara;

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
  modoGara: Boolean;
  forti, k, j: Integer;
  prossimoPremuto: Boolean;
  quandoRisolti: QWord;
  Ga: TGara;

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
  F.LblGara := TLabel.Create(F); F.LblCodici := TLabel.Create(F); F.EdCodici := TEdit.Create(F);
  F.LblSecondi := TLabel.Create(F); F.EdSecondi := TEdit.Create(F); F.BtnInizia := TButton.Create(F);
  F.BtnProssimo := TButton.Create(F); F.BtnFine := TButton.Create(F); F.LblRound := TLabel.Create(F);
  F.BtnInizia.Enabled := False; F.BtnProssimo.Enabled := False; F.BtnFine.Enabled := False;   // come nel .lfm
  F.BtnVia.Enabled := False; F.BtnNuova.Enabled := False; F.BtnStop.Enabled := False; F.BtnMostra.Enabled := False;   // come nel .lfm
  F.EdPorta.Text := porta;
  if ParamStr(4) = 'a' then   // caso (a): eventi gia' collegati dal .lfm, il form chiama FormCreate
  begin
    F.BtnAvvia.OnClick := @F.BtnAvviaClick; F.BtnVia.OnClick := @F.BtnViaClick;
    F.BtnNuova.OnClick := @F.BtnNuovaClick; F.BtnStop.OnClick := @F.BtnStopClick; F.BtnMostra.OnClick := @F.BtnMostraClick; F.PbSegreto.OnPaint := @F.PbSegretoPaint; F.PbSegreto.OnClick := @F.BtnMostraClick;
    F.BtnInizia.OnClick := @F.BtnIniziaClick; F.BtnProssimo.OnClick := @F.BtnProssimoClick; F.BtnFine.OnClick := @F.BtnFineClick;
    F.EdPorta.OnChange := @F.EdPortaChange; F.Timer1.OnTimer := @F.Timer1Timer;
    F.OnDestroy := @F.FormDestroy;
    F.FormCreate(nil);
    F.AfterConstruction;
    if not F.Avviato then begin WriteLn('ERRORE: Avviato falso'); Halt(3); end;
  end
  else F.AfterConstruction;   // caso (b): non collegati, AfterConstruction fa tutto
  if not Assigned(F.BtnAvvia.OnClick) or not Assigned(F.OnDestroy) or not F.Avviato then begin WriteLn('ERRORE: collegamenti/Avviato'); Halt(3); end;
  modoGara := ParamStr(5) = 'gara';
  forti := StrToIntDef(ParamStr(6), 0);
  prossimoPremuto := False; quandoRisolti := 0;
  if modoGara then
  begin
    PausaTraRoundSec := 1;                // pausa corta, per far durare poco la prova
    F.EdCodici.Text := '3'; F.EdSecondi.Text := '14';
    if not (Assigned(F.BtnInizia.OnClick) and Assigned(F.BtnProssimo.OnClick) and Assigned(F.BtnFine.OnClick)) then
    begin WriteLn('ERRORE: bottoni della gara non collegati'); Halt(3); end;
  end;
  F.BtnAvviaClick(nil);                 // clic su "Avvia server"
  if not F.BtnInizia.Enabled then begin WriteLn('ERRORE: dopo Avvia server il bottone Inizia gara dovrebbe essere acceso'); Halt(4); end;
  t0 := GetTickCount64; viaDato := False; finito := False; ticks := 0;
  quando := 0;
  while GetTickCount64 - t0 < 120000 do
  begin
    if F.Timer1.Enabled then begin F.Timer1Timer(nil); Inc(ticks); end;
    Sleep(50);
    if modoGara and (not viaDato) and (GetTickCount64 - t0 > 3000) then
    begin
      F.BtnIniziaClick(nil); viaDato := True;
      if F.BtnVia.Enabled or F.BtnNuova.Enabled then begin WriteLn('ERRORE: in gara i bottoni della partita libera devono essere spenti'); Halt(4); end;
      F.BtnViaClick(nil);   // in gara "Via!" non deve fare niente (e' spento)
    end;
    if modoGara and viaDato and (F.LaGara <> nil) and (F.LaGara.Stato = sgRound) and (F.LaGara.RoundCorrente = 3) and
       (not prossimoPremuto) and (forti > 0) and (F.LaGara.Risolti >= forti) then
    begin
      if quandoRisolti = 0 then quandoRisolti := GetTickCount64;
      if GetTickCount64 - quandoRisolti > 2000 then begin F.BtnProssimoClick(nil); prossimoPremuto := True; end;
    end;
    if (not modoGara) and (not viaDato) and (GetTickCount64 - t0 > 3000) and F.BtnVia.Enabled then
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
  if modoGara and (F.LaGara <> nil) then
  begin
    Ga := F.LaGara;
    out_.Clear;
    out_.Add('STATO ' + IntToStr(Ord(Ga.Stato)) + ' round_chiusi=' + IntToStr(Ga.RoundChiusi) + ' codici=' + IntToStr(Ga.NumCodici));
    for j := 0 to Ga.Giocatori - 1 do
    begin
      for k := 0 to High(Ga.Giocatore[j].Storico) do
        with Ga.Giocatore[j].Storico[k] do
          out_.Add(Format('ROUND %s %d tent=%d vic=%d risolto=%d rank=%d punti=%d', [Ga.Giocatore[j].Nome, k + 1, Tentativi, Vicinanza, Ord(Risolto), PosVelocita, Punti]));
      out_.Add(Format('TOT %s tot=%d tent=%d tempo=%d pos=%d', [Ga.Giocatore[j].Nome, Ga.Totale(j), Ga.TentativiTotali(j), Ga.TempoTotaleMs(j), Ga.Posizione(j)]));
    end;
    out_.SaveToFile(uscita + '/gara_dump.txt');
  end;
  MessaggiMostrati.SaveToFile(uscita + '/messaggi.txt');
  F.FormDestroy(nil);
  F.Free;
  WriteLn('FINE test_server');
end.
