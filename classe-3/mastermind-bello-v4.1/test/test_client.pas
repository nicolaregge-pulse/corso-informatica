program test_client;
{ PROVA del VERO unit1.pas del client bello (copiato come UnitInterfaccia.pas) contro finte unita' LCL.
  Uso: test_client modo [host nome]    modo: logica | locale | rete | spento | gara (v4.1: gara a piu' codici)
  Compilato con -dVECCHIO serve a provare il client v4.0.1 (senza gara) contro il server v4.1.
  logica = conteggio neri/bianchi (anche colori ripetuti), locale = partita da soli con controllo del disegno,
  rete = partita contro il server vero (porta 5050), spento = server non raggiungibile. }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, Controls, Graphics, Forms, StdCtrls, ExtCtrls, Dialogs, UnitInterfaccia;

var
  F: TFormClient;
  modo: String;
  errori: Integer = 0;

procedure Verifica(Ok: Boolean; const Cosa: String);
begin
  if Ok then WriteLn('  ok   ', Cosa) else begin WriteLn('  ERRORE ', Cosa); Inc(errori); end;
end;

function Nuovo(const Host, Nome: String): TFormClient;
begin
  Result := TFormClient(TFormClient.NewInstance);
  with Result do
  begin
    LblIp := TLabel.Create(Result); EdIp := TEdit.Create(Result); LblNome := TLabel.Create(Result);
    EdNome := TEdit.Create(Result); BtnConnetti := TButton.Create(Result); BtnLocale := TButton.Create(Result);
    LblEsito := TLabel.Create(Result); LblStato := TLabel.Create(Result);
    PbTavola := TPaintBox.Create(Result); PbTavolozza := TPaintBox.Create(Result); PbMessaggio := TPaintBox.Create(Result);
    BtnProva := TButton.Create(Result); BtnCancella := TButton.Create(Result);
    LblPosizione := TLabel.Create(Result); LblMigliore := TLabel.Create(Result);
    LblPeggiore := TLabel.Create(Result); LblFiniti := TLabel.Create(Result);
    {$IFNDEF VECCHIO}PbGara := TPaintBox.Create(Result);{$ENDIF}
    Timer1 := TTimer.Create(Result);
    BtnProva.Enabled := False; BtnCancella.Enabled := False; Timer1.Enabled := False;   // come nel .lfm
    EdIp.Text := Host; EdNome.Text := Nome;
    AfterConstruction;
  end;
  if not (Assigned(Result.BtnConnetti.OnClick) and Assigned(Result.BtnLocale.OnClick) and
          Assigned(Result.BtnProva.OnClick) and Assigned(Result.BtnCancella.OnClick) and
          Assigned(Result.Timer1.OnTimer) and Assigned(Result.PbTavola.OnPaint) and
          Assigned(Result.PbTavolozza.OnPaint) and Assigned(Result.PbMessaggio.OnPaint) and Assigned(Result.PbTavolozza.OnMouseDown) and Result.Avviato
          {$IFNDEF VECCHIO} and Assigned(Result.PbGara.OnPaint) and Assigned(Result.TimerGara.OnTimer){$ENDIF}) then
  begin
    WriteLn('ERRORE: eventi non collegati'); Halt(3);
  end;
end;

{ ---- conteggio indipendente: totale colori in comune - neri ---- }
procedure ValutaDue(const S, P: TCodice; out Ne, Bi: Integer);
var a, b: array[1..6] of Integer; i, tot: Integer;
begin
  FillChar(a, SizeOf(a), 0); FillChar(b, SizeOf(b), 0); Ne := 0;
  for i := 0 to 3 do begin Inc(a[S[i]]); Inc(b[P[i]]); if S[i] = P[i] then Inc(Ne); end;
  tot := 0;
  for i := 1 to 6 do if a[i] < b[i] then Inc(tot, a[i]) else Inc(tot, b[i]);
  Bi := tot - Ne;
end;

function Cod(a, b, c, d: Integer): TCodice;
begin
  Result[0] := a; Result[1] := b; Result[2] := c; Result[3] := d;
end;

procedure Prova(const S, P: TCodice; ne, bi: Integer);
var n, b: Integer;
begin
  Valuta(S, P, n, b);
  Verifica((n = ne) and (b = bi), Format('segreto %d%d%d%d prova %d%d%d%d -> %d neri %d bianchi (trovati %d e %d)',
    [S[0], S[1], S[2], S[3], P[0], P[1], P[2], P[3], ne, bi, n, b]));
end;

procedure ModoLogica;
var s, p: TCodice; i, j, n1, b1, n2, b2, diversi: Integer;
begin
  WriteLn('== logica: neri e bianchi, anche con colori ripetuti ==');
  Prova(Cod(1,1,2,3), Cod(1,2,1,1), 1, 2);
  Prova(Cod(1,1,1,1), Cod(1,1,1,1), 4, 0);
  Prova(Cod(1,1,1,1), Cod(2,2,2,2), 0, 0);
  Prova(Cod(1,1,2,2), Cod(2,2,1,1), 0, 4);
  Prova(Cod(1,1,2,3), Cod(1,1,1,1), 2, 0);
  Prova(Cod(1,2,3,4), Cod(4,3,2,1), 0, 4);
  Prova(Cod(1,2,3,4), Cod(1,1,1,1), 1, 0);
  Prova(Cod(6,6,5,5), Cod(5,6,6,5), 2, 2);
  diversi := 0;
  for i := 0 to 1295 do
    for j := 0 to 1295 do
    begin
      s := Cod(i div 216 mod 6 + 1, i div 36 mod 6 + 1, i div 6 mod 6 + 1, i mod 6 + 1);
      p := Cod(j div 216 mod 6 + 1, j div 36 mod 6 + 1, j div 6 mod 6 + 1, j mod 6 + 1);
      Valuta(s, p, n1, b1); ValutaDue(s, p, n2, b2);
      if (n1 <> n2) or (b1 <> b2) then Inc(diversi);
    end;
  Verifica(diversi = 0, 'tutte le 1296 x 1296 coppie: stesso risultato del conteggio indipendente (diversi: ' + IntToStr(diversi) + ')');
end;

function ContaCerchi(Cv: TCanvas; Raggio, Colore: Integer): Integer;
var i: Integer; chiave: String;
begin
  Result := 0; chiave := IntToStr(Raggio) + ';' + IntToStr(Colore);
  for i := 0 to Cv.Cerchi.Count - 1 do if Cv.Cerchi[i] = chiave then Inc(Result);
end;

const NERO = $0C0C0C; BIANCO = $EBEBEB;      // colori dei piolini piccoli di risposta
      R_RISP = 12;                          // raggio dei piolini di risposta nel disegno grande (6 x scala 2)

procedure Ridisegna;
begin
  if BufTavola <> nil then BufTavola.Canvas.Pulisci; F.PbTavola.Canvas.Pulisci; F.PbTavola.OnPaint(nil);
end;

procedure Clicca(c: Integer);      // come un click vero sul piolo c della tavolozza
begin
  F.PbTavolozza.OnMouseDown(nil, mbLeft, [], 22 + (c - 1) * 40, 30);        // il centro del colore c nella fascia
end;

procedure ModoLocale;
var i, t, ne, bi: Integer; g: TCodice; cand: TStringList; s: String; e2, b2: Integer;
begin
  WriteLn('== locale: partita da soli, pioli e disegno ==');
  F := Nuovo('', '');
  F.BtnLocale.OnClick(nil);
  Verifica(F.Modo = mLocale, 'dopo "Gioca da solo" il modo e'' locale');
  Verifica(Pos('Codice: ', F.Caption) = 1, 'il codice segreto compare nel titolo: ' + F.Caption);
  F.TimerTitolo.OnTimer(nil);
  Verifica(Pos('Codice: ', F.Caption) = 0, 'dopo il timer il titolo torna normale: ' + F.Caption);
  Verifica(F.TimerTitolo.Interval = 2300, 'il codice resta nel titolo 2300 ms (intervallo del timer: ' + IntToStr(F.TimerTitolo.Interval) + ')');
  Verifica(not F.BtnProva.Enabled, 'Prova spento con la riga vuota');
  F.Segreto := Cod(1, 1, 2, 3);            // codice noto, con un colore ripetuto
  Clicca(1); Clicca(2); Clicca(1);
  Verifica((F.NCorr = 3) and not F.BtnProva.Enabled, '3 colori scelti: Prova ancora spento');
  F.BtnProva.OnClick(nil);
  Verifica(F.NT = 0, 'Prova con 3 colori non registra niente');
  Clicca(1);
  Verifica(F.NCorr = 4, '4 colori scelti');
  Verifica(F.BtnProva.Enabled, 'Prova acceso con 4 colori');
  F.BtnCancella.OnClick(nil);
  Verifica(F.NCorr = 3, 'Togli l''ultimo toglie un colore');
  Clicca(1);
  F.PbTavolozza.OnMouseDown(nil, mbLeft, [], 5, 5);        // click fuori da ogni colore
  Verifica(F.NCorr = 4, 'click fuori dai colori non fa niente');
  F.BtnProva.OnClick(nil);
  Verifica((F.NT = 1) and (F.Storia[0].Neri = 1) and (F.Storia[0].Bianchi = 2), 'segreto 1123, prova 1211: 1 nero e 2 bianchi (trovati ' +
    IntToStr(F.Storia[0].Neri) + ' e ' + IntToStr(F.Storia[0].Bianchi) + ')');
  Verifica(F.NCorr = 0, 'la riga corrente si svuota dopo Prova');
  Ridisegna;
  Verifica(ContaCerchi(BufTavola.Canvas, R_RISP, NERO) = 1, 'sulla tavola: 1 piolino nero (trovati ' + IntToStr(ContaCerchi(BufTavola.Canvas, R_RISP, NERO)) + ')');
  Verifica(ContaCerchi(BufTavola.Canvas, R_RISP, BIANCO) = 2, 'sulla tavola: 2 piolini bianchi (trovati ' + IntToStr(ContaCerchi(BufTavola.Canvas, R_RISP, BIANCO)) + ')');
  Verifica(FondoTavola.Canvas.Linee > 20000, 'le fibre del legno sono disegnate nella bitmap (linee: ' + IntToStr(FondoTavola.Canvas.Linee) + ')');
  Verifica(FondoTavola.Canvas.Testi = 3, 'la scritta 3 INF e'' intagliata (3 passate di testo: ombra, luce, fondo)');
  Verifica(F.PbTavola.Canvas.Copie >= 1, 'il legno viene copiato dalla bitmap sulla tavola');
  if BufTavolozza <> nil then BufTavolozza.Canvas.Pulisci; F.PbTavolozza.Canvas.Pulisci; F.PbTavolozza.OnPaint(nil);
  F.PbMessaggio.OnPaint(nil);
  Verifica(F.PbMessaggio.Canvas.Copie >= 1, 'la legenda viene disegnata e rimpicciolita sullo schermo');
  Verifica(BufTavolozza.Canvas.Cerchi.Count >= 6 * 12, 'la tavolozza disegna i 6 piolini colorati');
  { tanti tentativi sbagliati: la tavola scorre senza errori }
  for t := 1 to 12 do begin Clicca(2); Clicca(2); Clicca(2); Clicca(2); F.BtnProva.OnClick(nil); end;
  Ridisegna;
  Verifica(F.NT = 13, 'dopo 13 tentativi la storia ne ha 13 e la tavola ne mostra 10 senza errori');
  { vince per eliminazione: i colori possono ripetersi }
  F.BtnLocale.OnClick(nil);
  Verifica((F.NT = 0) and not F.Finita, 'una nuova partita ricomincia da zero');
  cand := TStringList.Create;
  for i := 0 to 1295 do cand.Add(Chr(49 + i div 216 mod 6) + Chr(49 + i div 36 mod 6) + Chr(49 + i div 6 mod 6) + Chr(49 + i mod 6));
  t := 0;
  while (not F.Finita) and (t < 20) do
  begin
    Inc(t);
    s := cand[Random(cand.Count)];
    for i := 1 to 4 do Clicca(Ord(s[i]) - 48);
    F.BtnProva.OnClick(nil);
    ne := F.Storia[F.NT - 1].Neri; bi := F.Storia[F.NT - 1].Bianchi;
    for i := cand.Count - 1 downto 0 do
    begin
      g := Cod(Ord(cand[i][1]) - 48, Ord(cand[i][2]) - 48, Ord(cand[i][3]) - 48, Ord(cand[i][4]) - 48);
      ValutaDue(g, Cod(Ord(s[1]) - 48, Ord(s[2]) - 48, Ord(s[3]) - 48, Ord(s[4]) - 48), e2, b2);
      if (e2 <> ne) or (b2 <> bi) then cand.Delete(i);
    end;
  end;
  Verifica(F.Finita and (F.LblStato.Caption = 'HAI VINTO!'), 'partita vinta per eliminazione in ' + IntToStr(F.NT) + ' tentativi');
  Verifica(not F.BtnProva.Enabled, 'dopo la vittoria Prova e'' spento');
  Ridisegna;
  Verifica(ContaCerchi(BufTavola.Canvas, R_RISP, NERO) >= 4, 'la riga vincente mostra 4 piolini neri');
end;

procedure ModoRete(const Host, Nome: String);
var cand: TStringList; i, t, ne, bi, e2, b2: Integer; s: String; t0: QWord; g, p: TCodice;
begin
  F := Nuovo(Host, Nome);
  t0 := GetTickCount64;
  F.BtnConnetti.OnClick(nil);
  WriteLn(Nome, ' connetti (', GetTickCount64 - t0, ' ms): ', F.LblEsito.Caption, ' | ', F.LblStato.Caption);
  if modo = 'spento' then
  begin
    Verifica((F.Modo = mNessuno) and not F.BtnProva.Enabled, 'senza server il modo resta "nessuno" e Prova e'' spento');
    Halt(errori);
  end;
  while (Pos('GIOCO', F.LblStato.Caption) = 0) and (GetTickCount64 - t0 < 60000) do begin Sleep(300); F.Timer1.OnTimer(nil); end;
  if Pos('GIOCO', F.LblStato.Caption) = 0 then begin WriteLn(Nome, ' ERRORE: Via mai arrivato: ', F.LblStato.Caption); Halt(5); end;
  cand := TStringList.Create;
  for i := 0 to 1295 do cand.Add(Chr(49 + i div 216 mod 6) + Chr(49 + i div 36 mod 6) + Chr(49 + i div 6 mod 6) + Chr(49 + i mod 6));
  t := 0;
  while (not F.Finita) and (t < 30) do
  begin
    Inc(t);
    s := cand[Random(cand.Count)];
    for i := 1 to 4 do Clicca(Ord(s[i]) - 48);
    F.BtnProva.OnClick(nil);
    if F.Finita then Break;
    if F.NT < t then begin WriteLn(Nome, ' ERRORE: tentativo non registrato: ', F.LblEsito.Caption); Halt(6); end;
    ne := F.Storia[F.NT - 1].Neri; bi := F.Storia[F.NT - 1].Bianchi;
    p := Cod(Ord(s[1]) - 48, Ord(s[2]) - 48, Ord(s[3]) - 48, Ord(s[4]) - 48);
    for i := cand.Count - 1 downto 0 do
    begin
      g := Cod(Ord(cand[i][1]) - 48, Ord(cand[i][2]) - 48, Ord(cand[i][3]) - 48, Ord(cand[i][4]) - 48);
      ValutaDue(g, p, e2, b2);
      if (e2 <> ne) or (b2 <> bi) then cand.Delete(i);
    end;
  end;
  if not F.Finita then begin WriteLn(Nome, ' ERRORE: troppi tentativi'); Halt(7); end;
  F.Timer1.OnTimer(nil);
  Ridisegna;
  WriteLn(Nome, ' FINE tent=', F.NT, ' | ', F.LblEsito.Caption, ' | ', F.LblPosizione.Caption, ' | neri nell''ultima riga: ',
    F.Storia[F.NT - 1].Neri);
end;


{$IFNDEF VECCHIO}
{ v4.1: partecipa a una GARA. Tipo "forte" gioca sempre; "debole" nei codici 2 e 3 si ferma dopo 3 tentativi
  (cosi' si vedono round che finiscono per tempo e punteggi di vicinanza). Scrive una riga RIS per ogni codice
  e una riga FINE con la posizione che il client ha ricevuto. }
procedure ModoGara(const Host, Nome, Tipo: String);
var
  cand: TStringList;
  i, ne, bi, e2, b2, giro, maxT: Integer;
  s: String;
  t0: QWord;
  g, p: TCodice;
  rnd, nt, best, ntPrima: Integer;
  risolto: Boolean;

  procedure NuoviCandidati;
  var k: Integer;
  begin
    cand.Clear;
    for k := 0 to 1295 do cand.Add(Chr(49 + k div 216 mod 6) + Chr(49 + k div 36 mod 6) + Chr(49 + k div 6 mod 6) + Chr(49 + k mod 6));
  end;

  procedure ChiudiRound;
  begin
    if rnd > 0 then
      WriteLn('RIS ', Nome, ' k=', rnd, ' tent=', nt, ' best=', best, ' solved=', Ord(risolto));
  end;

begin
  F := Nuovo(Host, Nome);
  t0 := GetTickCount64;
  F.BtnConnetti.OnClick(nil);
  WriteLn(Nome, ' connetti (', GetTickCount64 - t0, ' ms): ', F.LblEsito.Caption, ' | ', F.LblStato.Caption);
  cand := TStringList.Create;
  rnd := 0; nt := 0; best := 0; risolto := False; giro := 0;
  while (not F.GaraConclusa) and (GetTickCount64 - t0 < 170000) do
  begin
    Sleep(100);
    Inc(giro);
    if giro mod 3 = 0 then F.Timer1.OnTimer(nil);       // chiede lo STATO (il Timer vero lo fa ogni 3 secondi)
    if F.GaraConclusa then Break;
    if not F.GaraAttiva then Continue;
    if F.GaraRound <> rnd then                          // nuovo codice: si chiude il vecchio e si ricomincia
    begin
      ChiudiRound;
      rnd := F.GaraRound; nt := 0; best := 0; risolto := False;
      NuoviCandidati;
      if F.NT <> 0 then begin WriteLn(Nome, ' ERRORE: la tavola non si e'' azzerata al codice ', rnd); Halt(8); end;
    end;
    if F.GaraInPausa or F.Finita or risolto then Continue;
    maxT := 1000;
    if (Tipo = 'debole') and (rnd >= 2) then maxT := 3;
    if nt >= maxT then Continue;
    if cand.Count = 0 then Continue;
    s := cand[Random(cand.Count)];
    for i := 1 to 4 do Clicca(Ord(s[i]) - 48);
    ntPrima := F.NT;
    F.BtnProva.OnClick(nil);
    if F.NT > ntPrima then                              // il server ha risposto: il tentativo e' valido
    begin
      Inc(nt);
      ne := F.Storia[F.NT - 1].Neri; bi := F.Storia[F.NT - 1].Bianchi;
      if 2 * ne + bi > best then best := 2 * ne + bi;
      if ne = 4 then risolto := True;
      p := Cod(Ord(s[1]) - 48, Ord(s[2]) - 48, Ord(s[3]) - 48, Ord(s[4]) - 48);
      for i := cand.Count - 1 downto 0 do
      begin
        g := Cod(Ord(cand[i][1]) - 48, Ord(cand[i][2]) - 48, Ord(cand[i][3]) - 48, Ord(cand[i][4]) - 48);
        ValutaDue(g, p, e2, b2);
        if (e2 <> ne) or (b2 <> bi) then cand.Delete(i);
      end;
    end
    else
      while F.NCorr > 0 do F.BtnCancella.OnClick(nil);  // il tentativo non e' stato accettato (codice finito): si toglie
  end;
  ChiudiRound;
  if not F.GaraConclusa then begin WriteLn(Nome, ' ERRORE: la gara non e'' finita in tempo'); Halt(9); end;
  Verifica(not F.BtnProva.Enabled, 'a gara finita Prova e'' spento');
  Verifica(Pos('GARA FINITA', F.LblStato.Caption) = 1, 'a gara finita la scritta dice GARA FINITA');
  F.PbGara.OnPaint(nil); F.PbGara.Canvas.Pulisci; BufGara.Canvas.Pulisci; F.PbGara.OnPaint(nil);
  Verifica(F.PbGara.Canvas.Copie >= 1, 'il riquadro della gara viene disegnato');
  WriteLn('FINE ', Nome, ' pos=', F.GaraPos, ' tot=', F.GaraPunti, ' n=', F.GaraGiocatori, ' primo=', F.GaraPrimo, ' ', F.GaraPuntiPrimo, ' | ', F.LblEsito.Caption);
end;
{$ENDIF}

begin
  Randomize;
  modo := ParamStr(1);
  if modo = 'logica' then ModoLogica
  else if modo = 'locale' then ModoLocale
  {$IFNDEF VECCHIO}else if modo = 'gara' then ModoGara(ParamStr(2), ParamStr(3), ParamStr(4)){$ENDIF}
  else ModoRete(ParamStr(2), ParamStr(3));
  if errori > 0 then begin WriteLn('PROVA FALLITA: errori = ', errori); Halt(1); end;
end.
