program test_tcp;
{ Prove della RETE (TCP su localhost). Parla con un VERO server_mastermind avviato a parte.
  Uso:  test_tcp A porta cartella seme     (prove principali)
        test_tcp B porta cartella seme     (server con ip-nomi.txt: 127.0.0.1;Mario Rossi) }
{$mode objfpc}{$H+}
uses {$ifdef unix}cthreads,{$endif} SysUtils, Classes, sockets, mm_logica, mm_file, mm_tcp, client_unit;
{$I prova.inc}

type
  TAttesa = class
    Fatto: Boolean;
    Risposta: String;
    procedure Finito(Sender: TObject);
  end;

procedure TAttesa.Finito(Sender: TObject);
begin
  Risposta := TMMRichiestaAsync(Sender).Risposta;
  Fatto := True;
end;

var
  porta: Word;
  cart, seg, txt, modo: String;
  seme: Int64;

function Nuovo(const Nome: String): TMMClient;
begin
  Result := TMMClient.Create;
  Result.Modo := moRete;
  Result.Host := '127.0.0.1';
  Result.Porta := porta;
  Result.Nome := Nome;
  Result.Cartella := '';
end;

procedure ProveA;
var
  A, B, C, D, G, I: TMMClient;
  R: TRisposta;
  att: TAttesa;
  k: Integer;
begin
  seg := CodiceDaSeme(seme);
  A := Nuovo('Anna'); B := Nuovo('Bruno'); C := Nuovo('Carla'); D := Nuovo('Dino'); G := Nuovo('Gina');

  WriteLn('== Prima del Via (rete)');
  R := A.Aggiorna;
  Controlla('STATO risponde ATTESA', (R.Tipo = 'STATO') and (R.Messaggio = 'ATTESA'));
  R := A.Prova(seg);
  Controlla('GUESS prima del Via: WAIT', R.Tipo = 'WAIT');
  ControllaTesto('riga cruda', 'WAIT', MMTcpRichiesta('127.0.0.1', porta, 'GUESS;Anna;' + seg));
  Controlla('riga senza senso: ERR, il server non muore',
    Copy(MMTcpRichiesta('127.0.0.1', porta, '!!!'), 1, 3) = 'ERR');
  Controlla('server ancora vivo dopo la riga strana', A.Aggiorna.Tipo = 'STATO');

  WriteLn('== Via!');
  MMScriviTesto(IncludeTrailingPathDelimiter(cart) + 'comando.txt', 'VIA' + LineEnding);
  for k := 1 to 40 do
  begin
    Sleep(100);
    if A.Aggiorna.Messaggio = 'GIOCO' then Break;
  end;
  Controlla('dopo il comando Via lo STATO e'' GIOCO', A.Aggiorna.Messaggio = 'GIOCO');

  R := A.Prova(Sbagliato(seg));
  Controlla('Anna sbaglia: RESULT, 1 tentativo, posizione 0', (R.Tipo = 'RESULT') and (R.Sintesi.Tentativi = 1) and (R.Sintesi.Posizione = 0));
  Sleep(1100);
  R := A.Prova(seg);
  Controlla('Anna indovina: WIN al 2o tentativo, posizione 1 di 1', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 2) and (R.Sintesi.Posizione = 1) and (R.Sintesi.Totale = 1));
  Controlla('  ... ha impiegato almeno 1 secondo', R.Secondi >= 1);
  Sleep(1100);
  R := B.Prova(seg);
  Controlla('Bruno indovina al 1o: primo, Anna scende a seconda', (R.Sintesi.Tentativi = 1) and (R.Sintesi.Posizione = 1) and (A.Aggiorna.Sintesi.Posizione = 2));
  Controlla('Bruno vede migliore 1 e peggiore 2', (R.Sintesi.Migliore = 1) and (R.Sintesi.Peggiore = 2));
  // Carla: 3 tentativi, con Async (la form non si blocca)
  C.Prova(Sbagliato(seg)); C.Prova(Sbagliato(seg));
  att := TAttesa.Create;
  TMMRichiestaAsync.Create('127.0.0.1', porta, C.RigaProva(seg), @att.Finito);
  for k := 1 to 50 do
  begin
    CheckSynchronize(100);
    if att.Fatto then Break;
  end;
  Controlla('richiesta ASINCRONA (thread) completata con CheckSynchronize', att.Fatto);
  R := C.ApplicaRisposta(att.Risposta);
  Controlla('Carla (async): WIN a 3 tentativi, ultima', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 3) and (R.Sintesi.Posizione = 3) and (R.Sintesi.Peggiore = 3));
  ControllaTesto('console di Carla', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 3 tentativi, posizione 3 di 3', C.Console);
  // Dino: 2 tentativi dopo Anna -> stessa quantita' di tentativi di Anna ma piu' lento
  D.Prova(Sbagliato(seg)); Sleep(1100);
  R := D.Prova(seg);
  Controlla('Dino 2 tentativi come Anna ma piu'' lento: dietro Anna', R.Sintesi.Posizione > A.Aggiorna.Sintesi.Posizione);
  // Gina arriva tardi
  Sleep(1100);
  R := G.Prova(seg);
  Controlla('Gina (ritardataria) indovina al 1o: seconda per tentativi', (R.Tipo = 'WIN') and (R.Sintesi.Posizione = 2) and (R.Sintesi.Totale = 5));
  att.Free;
  // dopo la vittoria si resta vincitori
  R := A.Prova(Sbagliato(seg));
  Controlla('dopo aver vinto, ripetere non cambia i tentativi', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 2));
  // client muto: si collega e non scrive niente
  MMTcpRichiesta('127.0.0.1', porta, '', 500);
  Controlla('server ancora vivo dopo un client muto', A.Aggiorna.Tipo = 'STATO');

  WriteLn('== Server spento: il client passa da solo ai file (piano B)');
  I := Nuovo('Ivo');
  I.Porta := 1;                      // nessuno ascolta qui
  I.Cartella := cart;
  R := I.Prova(Sbagliato(seg));
  Controlla('rete non raggiungibile -> modo file automatico', (I.Modo = moFile) and I.FallbackFile and (R.Tipo = 'RESULT'));
  Sleep(3500);                       // il server rilegge la cartella ogni 2 s
  MMLeggiTesto(IncludeTrailingPathDelimiter(cart) + 'ranking.txt', txt);
  Controlla('il server ha letto Ivo dal file e lo mette in ranking.txt', Pos('R;0;Ivo;1;', txt) > 0);

  WriteLn('== ranking.txt scritto dal server per chi usa i file');
  Controlla('contiene Bruno primo', Pos('R;1;Bruno;1;', txt) > 0);
  Controlla('contiene Carla', Pos('Carla;3;', txt) > 0);
  Controlla('MIGLIORE;1 PEGGIORE;3', (Pos('MIGLIORE;1', txt) > 0) and (Pos('PEGGIORE;3', txt) > 0));

  WriteLn('== Nuova partita (comando) ');
  MMScriviTesto(IncludeTrailingPathDelimiter(cart) + 'comando.txt', 'NUOVA' + LineEnding);
  Sleep(600);
  Controlla('dopo NUOVA: di nuovo ATTESA', A.Aggiorna.Messaggio = 'ATTESA');
  Controlla('  ... e Anna non ha piu'' tentativi', A.Aggiorna.Sintesi.Tentativi = 0);
end;

procedure ProveB;
var
  X: TMMClient;
  R: TRisposta;
begin
  seg := CodiceDaSeme(seme);
  WriteLn('== IP noto -> nome dalla tabella ip-nomi.txt');
  MMScriviTesto(IncludeTrailingPathDelimiter(cart) + 'comando.txt', 'VIA' + LineEnding);
  Sleep(800);
  X := Nuovo('Nome Falso');
  R := X.Prova(Sbagliato(seg));
  Controlla('GUESS accettato', R.Tipo = 'RESULT');
  R := X.Prova(seg);
  Controlla('WIN', R.Tipo = 'WIN');
  Sleep(500);                 // il server riscrive ranking.txt entro 0,1-0,2 s
  MMLeggiTesto(IncludeTrailingPathDelimiter(cart) + 'ranking.txt', txt);
  Controlla('ranking.txt ha il nome VERO "Mario Rossi"', Pos('Mario Rossi', txt) > 0);
  Controlla('  ... e NON il nome falso scritto dal client', Pos('Falso', txt) = 0);
end;

begin
  NProve := 0; NFalliti := 0;
  modo := ParamStr(1);
  porta := StrToInt(ParamStr(2));
  cart := ParamStr(3);
  seme := StrToInt64(ParamStr(4));
  if modo = 'A' then ProveA else ProveB;
  Fine;
end.
