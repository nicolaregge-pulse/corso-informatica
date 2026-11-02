program test_logica;
{ Prove della LOGICA pura (nessuna rete, nessun file): orologio finto. }
{$mode objfpc}{$H+}
uses SysUtils, Classes, mm_logica;
{$I prova.inc}

var
  Ora: Double;
function OroFinto: Double; begin Result := Ora; end;

var
  T: TMMTabella;
  seg, r: String;
  e, s: Integer;
  S1: TSintesi;
  R1: TRisposta;
  seme1: Int64;
begin
  WriteLn('== Valutazione esatte/spostate (stessa logica del Mastermind normale)');
  Valuta('1234', '1234', e, s); Controlla('1234 vs 1234 = 4 esatte', (e = 4) and (s = 0));
  Valuta('1234', '4321', e, s); Controlla('1234 vs 4321 = 0 esatte 4 spostate', (e = 0) and (s = 4));
  Valuta('1123', '1111', e, s); Controlla('1123 vs 1111 = 2 esatte 0 spostate', (e = 2) and (s = 0));
  Valuta('1234', '1355', e, s); Controlla('1234 vs 1355 = 1 esatta 1 spostata', (e = 1) and (s = 1));
  Valuta('1122', '2211', e, s); Controlla('1122 vs 2211 = 0 esatte 4 spostate', (e = 0) and (s = 4));
  Controlla('codice valido 1234', CodiceValido('1234'));
  Controlla('codice non valido 1237 / 123 / abcd / 12345',
    not CodiceValido('1237') and not CodiceValido('123') and not CodiceValido('abcd') and not CodiceValido('12345'));
  Controlla('stesso seme = stesso codice', CodiceDaSeme(777) = CodiceDaSeme(777));
  Controlla('codice da seme: 4 cifre da 1 a 6', CodiceValido(CodiceDaSeme(123456789)));

  WriteLn('== Partita (orologio finto)');
  T := TMMTabella.Create;
  T.Orologio := @OroFinto;
  Ora := 1000;
  T.NuovaPartita(4242);
  seg := T.Segreto;
  seme1 := T.Seme;
  ControllaTesto('prima del Via: WAIT', 'WAIT', T.Gestisci('GUESS;Anna;' + seg));
  Controlla('prima del Via nessun giocatore registrato', T.Count = 0);
  T.Via;
  ControllaTesto('codice non valido', 'ERR;codice non valido (servono 4 cifre da 1 a 6)', T.Gestisci('GUESS;Anna;12'));
  ControllaTesto('nome mancante', 'ERR;nome non valido', T.Gestisci('GUESS;;1111'));
  ControllaTesto('comando sconosciuto', 'ERR;comando sconosciuto', T.Gestisci('CIAO;Anna;1111'));

  // Anna: 1 sbagliato + giusto
  Ora := 1005;
  r := T.Gestisci('GUESS;Anna;' + Sbagliato(seg));
  Controlla('tentativo sbagliato: RESULT', ParsaRisposta(r, R1) and (R1.Tipo = 'RESULT') and (R1.Esatte < 4));
  Controlla('  ... 1 tentativo, posizione 0, totale 0', (R1.Sintesi.Tentativi = 1) and (R1.Sintesi.Posizione = 0) and (R1.Sintesi.Totale = 0));
  Ora := 1010;
  ControllaTesto('Anna indovina al 2o tentativo dopo 10 s', 'WIN;Anna;2;10;1;1;2;2', T.Gestisci('GUESS;Anna;' + seg));
  // Bruno: al primo colpo
  Ora := 1020;
  ControllaTesto('Bruno al 1o tentativo dopo 20 s: primo', 'WIN;Bruno;1;20;1;2;1;2', T.Gestisci('GUESS;Bruno;' + seg));
  Controlla('Anna ora e'' seconda', T.SintesiDi('Anna').Posizione = 2);
  // Dino: 2 tentativi, 10 secondi -> PARI MERITO con Anna
  Ora := 1003; T.Gestisci('GUESS;Dino;' + Sbagliato(seg));
  Ora := 1010;
  r := T.Gestisci('GUESS;Dino;' + seg);
  Controlla('Dino pari merito con Anna (2 tentativi, 10 s): posizione 2', T.SintesiDi('Dino').Posizione = 2);
  Controlla('  ... e Anna resta seconda', T.SintesiDi('Anna').Posizione = 2);
  // Ennio: 2 tentativi ma 15 s -> dopo Anna e Dino (a parita' di tentativi vince chi e' piu' veloce)
  Ora := 1008; T.Gestisci('GUESS;Ennio;' + Sbagliato(seg));
  Ora := 1015; T.Gestisci('GUESS;Ennio;' + seg);
  Controlla('Ennio (2 tentativi, 15 s) e'' quarto (dopo il pari merito)', T.SintesiDi('Ennio').Posizione = 4);
  // Carla: 3 tentativi -> il PEGGIORE
  Ora := 1012; T.Gestisci('GUESS;Carla;' + Sbagliato(seg));
  Ora := 1022; T.Gestisci('GUESS;Carla;' + Sbagliato(seg));
  Ora := 1030; T.Gestisci('GUESS;Carla;' + seg);
  S1 := T.SintesiDi('Carla');
  Controlla('Carla: 3 tentativi, posizione 5 di 5', (S1.Tentativi = 3) and (S1.Posizione = 5) and (S1.Totale = 5));
  Controlla('migliore = 1 tentativo, peggiore = 3 tentativi', (S1.Migliore = 1) and (S1.Peggiore = 3));
  // Fabio: prova e non finisce
  Ora := 1040; T.Gestisci('GUESS;Fabio;' + Sbagliato(seg));
  S1 := T.SintesiDi('Fabio');
  Controlla('Fabio (non finito): 1 tentativo, posizione 0, totale resta 5', (S1.Tentativi = 1) and (S1.Posizione = 0) and (S1.Totale = 5));
  // di nuovo dopo la vittoria
  ControllaTesto('Anna riprova dopo aver vinto: resta WIN con 2 tentativi', 'WIN;Anna;2;10;2;5;1;3', T.Gestisci('GUESS;Anna;' + Sbagliato(seg)));
  Controlla('nomi senza distinzione maiuscole: "anna" e'' Anna', (T.Gestisci('GUESS;anna;' + seg) <> '') and (T.Count = 6));

  WriteLn('== Chi arriva tardi');
  Ora := 2000;
  ControllaTesto('Gina entra molto dopo e indovina subito: WIN dopo 1000 s, seconda', 'WIN;Gina;1;1000;2;6;1;3', T.Gestisci('GUESS;Gina;' + seg));
  Controlla('  ... Anna e Dino scalano al 3o posto, Ennio 5o, Carla 6a',
    (T.SintesiDi('Anna').Posizione = 3) and (T.SintesiDi('Dino').Posizione = 3) and
    (T.SintesiDi('Ennio').Posizione = 5) and (T.SintesiDi('Carla').Posizione = 6));
  ControllaTesto('STATO di chi non ha ancora provato (Hugo)', 'STATO;GIOCO;0;0;6;1;3', T.Gestisci('STATO;Hugo'));

  WriteLn('== Console dello studente');
  S1 := T.SintesiDi('Carla');
  ControllaTesto('testo console', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 3 tentativi, posizione 6 di 6', TestoConsole(S1));
  ControllaTesto('testo console chi non ha finito', 'Migliore: 1 tentativi ' + #194#183 + ' Peggiore: 3 tentativi ' + #194#183 + ' Tu: 1 tentativi, non hai ancora indovinato (hanno finito in 6)', TestoConsole(T.SintesiDi('Fabio')));
  Controlla('ParsaRisposta capisce WIN', ParsaRisposta('WIN;Gina;1;1000;2;6;1;3', R1) and (R1.Tipo = 'WIN') and (R1.Secondi = 1000) and (R1.Sintesi.Posizione = 2));
  Controlla('ParsaRisposta capisce WAIT', ParsaRisposta('WAIT', R1) and (R1.Tipo = 'WAIT'));
  Controlla('ParsaRisposta rifiuta rumore', not ParsaRisposta('boh', R1));

  WriteLn('== File ranking.txt riletto da un client');
  r := T.TestoRanking;
  Controlla('ranking.txt contiene la riga di Carla', Pos('R;6;Carla;3;30;S', r) > 0);
  Controlla('ranking.txt: MIGLIORE;1 e PEGGIORE;3', (Pos('MIGLIORE;1', r) > 0) and (Pos('PEGGIORE;3', r) > 0));
  Controlla('partita.txt dopo il Via contiene il seme', Pos(IntToStr(seme1), T.TestoPartita) > 0);

  WriteLn('== Nuova partita');
  T.NuovaPartita(9999);
  Controlla('tabella vuota, di nuovo in attesa, codice nuovo',
    (T.Count = 0) and (T.Fase = faAttesa) and (T.Segreto <> seg));
  ControllaTesto('WAIT di nuovo', 'WAIT', T.Gestisci('GUESS;Anna;' + T.Segreto));
  Controlla('partita.txt in attesa NON rivela il seme', Pos('9999', T.TestoPartita) = 0);

  WriteLn('== IP -> nome (ip-nomi.txt)');
  T.CaricaIpNomi('# esempio' + LineEnding + '192.168.0.5;Luca Verdi' + LineEnding + '192.168.0.6;Sara Neri' + LineEnding);
  T.Via;
  seg := T.Segreto;
  r := T.Gestisci('GUESS;Falso;' + Sbagliato(seg), '192.168.0.5');
  Controlla('IP noto: il nome scritto dal client viene ignorato', (T.Count = 1) and (T.Giocatori[0].Nome = 'Luca Verdi'));
  r := T.Gestisci('GUESS;Ospite;' + Sbagliato(seg), '10.9.9.9');
  Controlla('IP sconosciuto: vale il nome scritto', (T.Count = 2) and (T.Giocatori[1].Nome = 'Ospite'));
  Controlla('pannello presenze: Sara non ha ancora provato', Pos('Sara Neri', T.TestoPresenze) > 0);
  Controlla('  ... e Luca sta provando', Pos('sta provando (1', T.TestoPresenze) > 0);
  T.Free;
  Fine;
end.
