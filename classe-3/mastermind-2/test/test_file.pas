program test_file;
{ Prove del TRASPORTO FILE: server (in questo programma) + client simulati sulla stessa cartella. }
{$mode objfpc}{$H+}
uses SysUtils, Classes, mm_logica, mm_file, client_unit;
{$I prova.inc}

var
  Ora: Double;
function OroFinto: Double; begin Result := Ora; end;

function NuovoClient(const Nome, Cart: String): TMMClient;
begin
  Result := TMMClient.Create;
  Result.Modo := moFile;
  Result.Nome := Nome;
  Result.Cartella := Cart;
  Result.Orologio := @OroFinto;
end;

var
  T: TMMTabella;
  FS: TMMFileServer;
  cart, seg, txt, base: String;
  A, B, C, D, G: TMMClient;
  R: TRisposta;
  F: TFileStream;
  n: Integer;
  p: String;
begin
  NProve := 0; NFalliti := 0;
  cart := ParamStr(1);
  if cart = '' then cart := '/tmp/mm_prova_file';
  base := IncludeTrailingPathDelimiter(cart);
  // pulizia cartella di prova
  DeleteFile(base + 'partita.txt'); DeleteFile(base + 'ranking.txt');
  ForceDirectories(cart);
  T := TMMTabella.Create;
  T.Orologio := @OroFinto;
  Ora := 1000;
  T.NuovaPartita(31337);
  seg := T.Segreto;
  FS := TMMFileServer.Create(T, cart);
  // niente vecchi file di giocatori
  for p in TStringArray.Create('Anna', 'Bruno', 'Carla', 'Dino', 'Gina', 'Hugo', 'Zeno') do
    DeleteFile(MMFileGiocatore(cart, p));
  FS.ScriviFile;

  WriteLn('== Prima del Via');
  A := NuovoClient('Anna', cart); B := NuovoClient('Bruno', cart); C := NuovoClient('Carla', cart);
  D := NuovoClient('Dino', cart); G := NuovoClient('Gina', cart);
  Controlla('partita.txt in attesa NON contiene il seme', (MMLeggiTesto(base + 'partita.txt', txt)) and (Pos('31337', txt) = 0) and (Pos('ATTESA', txt) > 0));
  R := A.Prova(seg);
  Controlla('il client risponde WAIT prima del Via', R.Tipo = 'WAIT');
  Controlla('  ... e non scrive nulla', not FileExists(MMFileGiocatore(cart, 'Anna')));
  Controlla('console in attesa: nessuno ha indovinato', Pos('Nessuno', A.Console) = 1);

  WriteLn('== Via!');
  T.Via; FS.ScriviFile;
  Controlla('partita.txt ora contiene il seme', (MMLeggiTesto(base + 'partita.txt', txt)) and (Pos('31337', txt) > 0) and (Pos('GIOCO', txt) > 0));
  Controlla('ERR se il codice e'' scritto male', A.Prova('99').Tipo = 'ERR');

  // Anna: sbagliato a 5 s, giusto a 10 s
  Ora := 1005; R := A.Prova(Sbagliato(seg));
  Controlla('Anna sbaglia: RESULT, 1 tentativo', (R.Tipo = 'RESULT') and (R.Sintesi.Tentativi = 1));
  Ora := 1010; R := A.Prova(seg);
  Controlla('Anna indovina: WIN, 2 tentativi, 10 secondi', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 2) and (R.Secondi = 10));
  // Bruno al primo colpo a 20 s
  Ora := 1020; R := B.Prova(seg);
  Controlla('Bruno indovina subito: WIN, 1 tentativo, 20 s', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 1) and (R.Secondi = 20));
  // Carla 3 tentativi, ultimo a 30 s
  Ora := 1012; C.Prova(Sbagliato(seg));
  Ora := 1022; C.Prova(Sbagliato(seg));
  Ora := 1030; R := C.Prova(seg);
  Controlla('Carla: WIN con 3 tentativi', (R.Tipo = 'WIN') and (R.Sintesi.Tentativi = 3));
  // Dino come Anna: pari merito
  Ora := 1003; D.Prova(Sbagliato(seg));
  Ora := 1010; D.Prova(seg);
  // Anna riprova dopo la vittoria: il file non cresce
  Ora := 1040; A.Prova(Sbagliato(seg));
  MMLeggiTesto(MMFileGiocatore(cart, 'Anna'), txt);
  Controlla('Anna dopo la vittoria: il suo file resta di 2 righe', Length(txt) - Length(StringReplace(txt, #10, '', [rfReplaceAll])) = 2);

  WriteLn('== Il server rilegge la cartella');
  n := FS.Poll;
  Controlla('Poll vede 8 tentativi nuovi (2+1+3+2)', n = 8);
  Controlla('un secondo Poll non conta due volte', FS.Poll = 0);
  FS.ScriviFile;
  Controlla('tabella del server: Anna 2 tentativi 10 s',
    (T.SintesiDi('Anna').Tentativi = 2) and (T.SintesiDi('Anna').Posizione = 2));
  Controlla('Dino pari merito con Anna (posizione 2)', T.SintesiDi('Dino').Posizione = 2);
  Controlla('Carla e'' quarta di 4', (T.SintesiDi('Carla').Posizione = 4) and (T.SintesiDi('Carla').Totale = 4));
  Controlla('migliore 1, peggiore 3', (T.SintesiDi('Carla').Migliore = 1) and (T.SintesiDi('Carla').Peggiore = 3));

  WriteLn('== I client leggono ranking.txt');
  R := C.Aggiorna;
  ControllaTesto('console di Carla', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 3 tentativi, posizione 4 di 4', C.Console);
  A.Aggiorna;
  ControllaTesto('console di Anna', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 2 tentativi, posizione 2 di 4', A.Console);

  WriteLn('== Chi arriva tardi');
  Ora := 3000;
  R := G.Prova(seg);
  Controlla('Gina entra tardi e indovina: WIN, 1 tentativo, 2000 s (conta dal Via)', (R.Tipo = 'WIN') and (R.Secondi = 2000));
  FS.Poll; FS.ScriviFile;
  G.Aggiorna;
  ControllaTesto('console di Gina', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 1 tentativi, posizione 2 di 5', G.Console);

  WriteLn('== Righe strane');
  MMAggiungiRiga(MMFileGiocatore(cart, 'Zeno'), 'VECCHIA;Zeno;' + seg + ';5');
  FS.Poll;
  Controlla('riga di una partita vecchia (altro id): ignorata', T.Count = 5);
  // riga a meta' (senza a capo)
  F := TFileStream.Create(MMFileGiocatore(cart, 'Hugo'), fmCreate);
  txt := T.IdPartita + ';Hugo;' + seg + ';77';
  F.WriteBuffer(txt[1], Length(txt)); F.Free;
  FS.Poll;
  Controlla('riga a meta'' (senza a capo): non ancora letta', T.Count = 5);
  MMAggiungiRiga(MMFileGiocatore(cart, 'Hugo'), '');     // aggiunge solo l'a capo
  FS.Poll;
  Controlla('quando arriva l''a capo la riga conta; il server ha ricalcolato: e'' una vittoria',
    (T.Count = 6) and (T.SintesiDi('Hugo').Posizione > 0));

  WriteLn('== Nuova partita');
  T.NuovaPartita(555); FS.Dimentica; FS.ScriviFile;
  FS.Poll;
  Controlla('dopo Nuova partita le vecchie righe non contano', T.Count = 0);
  Controlla('client: WAIT di nuovo', NuovoClient('Anna', cart).Prova(seg).Tipo = 'WAIT');
  WriteLn('== File di configurazione accanto al programma');
  MMScriviTesto(base + 'cartella.txt', cart + LineEnding);
  A := TMMClient.Create;
  Controlla('solo cartella.txt: modo file', A.CaricaConfig(cart) and (A.Modo = moFile) and (A.Cartella = cart));
  MMScriviTesto(base + 'server.txt', '192.168.10.5:5051' + LineEnding);
  A.CaricaConfig(cart);
  Controlla('server.txt IP:PORTA: modo rete', (A.Modo = moRete) and (A.Host = '192.168.10.5') and (A.Porta = 5051));
  MMScriviTesto(base + 'server.txt', '192.168.10.5' + LineEnding);
  A.CaricaConfig(cart);
  Controlla('server.txt solo IP: porta predefinita 5050', A.Porta = 5050);
  DeleteFile(base + 'server.txt'); DeleteFile(base + 'cartella.txt');
  Controlla('nessun file: non configurato', not A.CaricaConfig(cart));
  Fine;
end.
