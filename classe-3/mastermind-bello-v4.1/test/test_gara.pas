program test_gara;
{ PROVA di UnitGara DA SOLA (puro Pascal: niente finestre, niente rete, niente orologio).
  Controlla i punteggi, i bonus, le penalita', la classifica con le parita' e i tre modi in cui finisce un round.
  Il tempo e' deciso dalla prova (in millisecondi), quindi il risultato e' sempre lo stesso. }
{$mode objfpc}{$H+}
uses
  SysUtils, UnitGara;

var
  errori: Integer = 0;

procedure Verifica(Ok: Boolean; const Cosa: String);
begin
  if Ok then WriteLn('  ok   ', Cosa) else begin WriteLn('  ERRORE ', Cosa); Inc(errori); end;
end;

procedure Uguale(Trovato, Atteso: Integer; const Cosa: String);
begin
  Verifica(Trovato = Atteso, Cosa + ' (atteso ' + IntToStr(Atteso) + ', trovato ' + IntToStr(Trovato) + ')');
end;

{ un tentativo qualsiasi di un giocatore }
function Prova(G: TGara; Idx: Integer; const Cod: String; T: Int64): TEsitoTentativo;
var
  n, b: Integer;
begin
  Result := G.Tentativo(Idx, Cod, T, n, b);
end;

{ fa N tentativi sbagliati, tutti "1111" (con segreto 2345 danno 0 neri e 0 bianchi) }
procedure Sbagli(G: TGara; Idx: Integer; N: Integer; T: Int64);
var
  i: Integer;
begin
  for i := 1 to N do Prova(G, Idx, '1111', T);
end;

procedure TestFunzioni;
var
  n, b: Integer;
begin
  WriteLn('== funzioni semplici ==');
  Verifica(CodiceValido('1234') and CodiceValido('6611'), 'codici validi');
  Verifica(not CodiceValido('123') and not CodiceValido('12345') and not CodiceValido('1237') and not CodiceValido('12a4') and not CodiceValido('0123'), 'codici non validi');
  ValutaCodice('1123', '1211', n, b);
  Verifica((n = 1) and (b = 2), 'segreto 1123, prova 1211: 1 nero 2 bianchi');
  ValutaCodice('1234', '1234', n, b);
  Verifica((n = 4) and (b = 0), '4 neri');
  ValutaCodice('1122', '2211', n, b);
  Verifica((n = 0) and (b = 4), '4 bianchi');
  Uguale(Vicinanza(3, 0), 6, 'vicinanza 3 neri = 6');
  Uguale(Vicinanza(2, 2), 6, 'vicinanza 2 neri 2 bianchi = 6');
  Uguale(Vicinanza(0, 4), 4, 'vicinanza 4 bianchi = 4');
  Uguale(Vicinanza(4, 0), 8, 'vicinanza 4 neri = 8');
  Uguale(BonusVelocita(1), 30, 'bonus 1o = 30');
  Uguale(BonusVelocita(2), 20, 'bonus 2o = 20');
  Uguale(BonusVelocita(3), 10, 'bonus 3o = 10');
  Uguale(BonusVelocita(4), 0, 'bonus 4o = 0');
  Uguale(BonusVelocita(0), 0, 'bonus di chi non ha risolto = 0');
  Uguale(Penalita(6), 0, 'penalita'' al 6o tentativo = 0');
  Uguale(Penalita(7), 1, 'penalita'' al 7o tentativo = 1');
  Uguale(Penalita(16), 10, 'penalita'' al 16o tentativo = 10');
  Uguale(Penalita(0), 0, 'penalita'' a 0 tentativi = 0');
  Uguale(PunteggioRound(6, False, 0, 3), 60, 'esempio: 3 neri, non risolto = 60');
  Uguale(PunteggioRound(8, True, 1, 3), 160, 'esempio: risolto per primo in 3 tentativi = 160 (il massimo)');
  Uguale(PunteggioRound(8, True, 2, 4), 150, 'esempio: risolto 2o = 150');
  Uguale(PunteggioRound(8, True, 3, 5), 140, 'esempio: risolto 3o = 140');
  Uguale(PunteggioRound(8, True, 4, 5), 130, 'esempio: risolto 4o = 130');
  Uguale(PunteggioRound(8, True, 4, 10), 126, 'esempio: risolto 4o al 10o tentativo = 130 - 4');
  Uguale(PunteggioRound(0, False, 0, 40), 0, 'mai sotto zero');
  Uguale(PunteggioRound(1, False, 0, 40), 0, 'mai sotto zero anche con vicinanza bassa');
  Verifica(Length(NuovoCodiceCasuale) = 4, 'il codice casuale ha 4 cifre');
  n := 0;
  for b := 1 to 500 do if not CodiceValido(NuovoCodiceCasuale) then Inc(n);
  Uguale(n, 0, '500 codici casuali: tutti validi');
end;

procedure TestPunteggiRound;
var
  G: TGara;
  a, b, c, d, e, f: Integer;
begin
  WriteLn('== punteggi di un round (segreto 1234) ==');
  G := TGara.Create;
  G.NumCodici := 2;
  G.SecondiRound := 180;
  a := G.Registra('Anna', 0); b := G.Registra('Bruno', 0); c := G.Registra('Carla', 0);
  d := G.Registra('Dino', 0); e := G.Registra('Elena', 0); f := G.Registra('Fabio', 0);
  G.ImpostaSegreti(['1234', '4321']);
  G.Inizia(1000);
  Verifica(G.Stato = sgRound, 'la gara e'' in round');
  Uguale(G.RoundCorrente, 1, 'siamo al round 1');
  Verifica(G.Segreto = '1234', 'il codice del round 1 e'' quello deciso');
  // Anna: non risolve, miglior tentativo 3 neri (1235) dopo uno da 1 nero
  Prova(G, a, '1111', 2000);
  Prova(G, a, '1235', 3000);
  Uguale(G.PuntiRound(a), 60, 'Anna: 3 neri come miglior tentativo = 60');
  Uguale(G.Totale(a), 60, 'il totale in diretta segue il round');
  // Bruno: risolve per primo al 3o tentativo
  Prova(G, b, '1111', 4000); Prova(G, b, '1243', 5000);
  Verifica(Prova(G, b, '1234', 11000) = etRisolto, 'Bruno risolve');
  Uguale(G.PuntiRound(b), 160, 'Bruno: 80 + 50 + 30 = 160');
  // Carla: 2o, al 4o tentativo
  Sbagli(G, c, 3, 12000);
  Verifica(Prova(G, c, '1234', 21000) = etRisolto, 'Carla risolve');
  Uguale(G.PuntiRound(c), 150, 'Carla: 80 + 50 + 20 = 150 (miglior tentativo = quello giusto)');
  // Dino: 3o, al 7o tentativo (penalita' 1)
  Sbagli(G, d, 6, 22000);
  Verifica(Prova(G, d, '1234', 31000) = etRisolto, 'Dino risolve');
  Uguale(G.PuntiRound(d), 139, 'Dino: 80 + 50 + 10 - 1 = 139');
  // Elena: 4a, nessun bonus velocita'
  Verifica(Prova(G, e, '1234', 41000) = etRisolto, 'Elena risolve');
  Uguale(G.PuntiRound(e), 130, 'Elena: 80 + 50 + 0 = 130');
  // Fabio: 12 tentativi sbagliati, miglior tentativo 1 nero (1555 -> 1 nero)
  Prova(G, f, '1555', 42000); Sbagli(G, f, 11, 43000);
  Uguale(G.PuntiRound(f), 20 - 6, 'Fabio: 1 nero = 20, 12 tentativi = -6, totale 14');
  // dopo la vittoria i tentativi non contano
  Verifica(Prova(G, b, '1111', 50000) = etGiaRisolto, 'dopo la vittoria: etGiaRisolto');
  Uguale(G.Giocatore[b].TentRound, 3, 'i tentativi dopo la vittoria non si contano');
  Verifica(Prova(G, a, '12', 50000) = etCodiceNonValido, 'codice di 2 cifre: non valido');
  Verifica(Prova(G, a, '1237', 50000) = etCodiceNonValido, 'cifra 7: non valida');
  Uguale(G.Giocatore[a].TentRound, 2, 'un codice non valido non conta come tentativo');
  Verifica(Prova(G, 99, '1234', 50000) = etNonInGioco, 'giocatore inesistente: non in gioco');
  // classifica in diretta
  Uguale(G.Posizione(b), 1, 'Bruno e'' 1o');
  Uguale(G.Posizione(c), 2, 'Carla e'' 2a');
  Uguale(G.Posizione(d), 3, 'Dino e'' 3o');
  Uguale(G.Posizione(e), 4, 'Elena e'' 4a');
  Uguale(G.Posizione(a), 5, 'Anna e'' 5a');
  Uguale(G.Posizione(f), 6, 'Fabio e'' 6o');
  Verifica(G.Ordine[0] = b, 'l''ordine comincia da Bruno');
  G.Free;
end;

procedure TestRoundEClassifica;
var
  G: TGara;
  a, b, c: Integer;
begin
  WriteLn('== due round, somma, parita'' e fine gara ==');
  PausaTraRoundSec := 5;
  G := TGara.Create;
  G.NumCodici := 2;
  G.SecondiRound := 100;
  a := G.Registra('Anna', 0); b := G.Registra('Bruno', 0); c := G.Registra('Carla', 0);
  G.ImpostaSegreti(['2345', '3456']);
  G.Inizia(0);
  // round 1: Anna risolve per prima in 2 tentativi (160), Bruno 2o in 2 tentativi (150), Carla non risolve: 3 neri = 60
  Sbagli(G, a, 1, 1000); Prova(G, a, '2345', 5000);
  Sbagli(G, b, 1, 1500); Prova(G, b, '2345', 5500);
  Prova(G, c, '2341', 7000);
  Uguale(G.Totale(a), 160, 'round 1: Anna 160');
  Uguale(G.Totale(b), 150, 'round 1: Bruno 150');
  Uguale(G.Totale(c), 60, 'round 1: Carla 60');
  G.ProssimoCodice(8000);       // il Prof preme "Prossimo codice"
  Verifica(G.UltimoMotivo = mfDocente, 'il round 1 e'' finito per scelta del Prof');
  Uguale(G.RoundChiusi, 1, 'un round chiuso');
  Verifica(G.Stato = sgRound, 'ProssimoCodice durante un round passa subito al round dopo');
  Uguale(G.RoundCorrente, 2, 'siamo al round 2');
  Verifica(G.CodiceUltimoChiuso = '2345', 'ricordo il codice del round chiuso');
  Verifica(G.Segreto = '3456', 'nuovo codice');
  Uguale(G.Totale(a), 160, 'a inizio round 2 il totale e'' quello del round 1 (Anna)');
  Uguale(G.PuntiRound(a), 0, 'a inizio round 2 i punti del round sono 0');
  // round 2 (parte a 8000): Carla risolve per prima in 1 tentativo (160): totale 220. Bruno 2o (150): 300. Anna 3a (140): 300.
  Prova(G, c, '3456', 9000);
  Prova(G, b, '3456', 9500);
  Prova(G, a, '3456', 10000);
  Uguale(G.Totale(c), 220, 'Carla: 60 + 160 = 220');
  Uguale(G.Totale(b), 300, 'Bruno: 150 + 150 = 300');
  Uguale(G.Totale(a), 300, 'Anna: 160 + 140 = 300');
  // Anna e Bruno a pari punti: Anna ha fatto 2+1 = 3 tentativi, Bruno 2+1 = 3: stessi. Tempo: Anna 5000 + 2000 = 7000 ms; Bruno 5500 + 1500 = 7000 ms.
  Uguale(G.TentativiTotali(a), 3, 'Anna: 3 tentativi in tutto');
  Uguale(G.TentativiTotali(b), 3, 'Bruno: 3 tentativi in tutto');
  Verifica(G.TempoTotaleMs(a) = G.TempoTotaleMs(b), 'stesso tempo totale: ' + IntToStr(G.TempoTotaleMs(a)) + ' ms');
  Uguale(G.Posizione(a), 1, 'pari merito: Anna 1a');
  Uguale(G.Posizione(b), 1, 'pari merito: Bruno 1o');
  Uguale(G.Posizione(c), 3, 'dopo due pari merito il posto e'' il 3o');
  Verifica(G.Giocatore[a].Nome = 'Anna', 'Anna e'' ancora il primo nell''elenco');
  Verifica(G.Ordine[0] = a, 'a parita'' completa si ordina per nome: prima Anna');
  Verifica(G.Ordine[1] = b, 'poi Bruno');
  // fine round 2 e gara: round 2 e' l'ultimo
  G.ProssimoCodice(11000);
  Verifica(G.Stato = sgFinita, 'dopo l''ultimo round la gara e'' finita');
  Uguale(G.RoundChiusi, 2, 'due round chiusi');
  Uguale(G.Totale(a), 300, 'a gara finita il totale resta 300');
  Uguale(G.Giocatore[c].Storico[0].Punti, 60, 'storico: Carla round 1 = 60');
  Uguale(G.Giocatore[c].Storico[1].Punti, 160, 'storico: Carla round 2 = 160');
  Verifica(G.Giocatore[a].Storico[0].Risolto and (G.Giocatore[a].Storico[0].PosVelocita = 1), 'storico: Anna ha risolto 1a nel round 1');
  Verifica(not G.Giocatore[c].Storico[0].Risolto, 'storico: Carla non ha risolto nel round 1');
  Verifica(Prova(G, a, '3456', 12000) = etNonInGioco, 'a gara finita i tentativi non servono');
  G.ProssimoCodice(13000);
  Verifica(G.Stato = sgFinita, 'ProssimoCodice a gara finita non fa niente');

  // spareggio per TENTATIVI: stessi punti (nessuno risolve, miglior tentativo 1 nero = 20), meno tentativi = sopra
  G.Free;
  G := TGara.Create;
  G.NumCodici := 1;
  G.SecondiRound := 100;
  a := G.Registra('Zeta', 0); b := G.Registra('Alfa', 0); c := G.Registra('Mimmo', 0);
  G.ImpostaSegreti(['1111']);
  G.Inizia(0);
  Prova(G, a, '1222', 100);                      // Zeta: 1 tentativo, 20
  Prova(G, b, '2222', 100); Prova(G, b, '1222', 200);   // Alfa: 2 tentativi, 20
  Prova(G, c, '1222', 100); Prova(G, c, '2222', 200); Prova(G, c, '2222', 300);   // Mimmo: 3 tentativi, 20
  Uguale(G.Totale(a), 20, 'Zeta 20'); Uguale(G.Totale(b), 20, 'Alfa 20'); Uguale(G.Totale(c), 20, 'Mimmo 20');
  Uguale(G.Posizione(a), 1, 'a pari punti vince chi ha fatto meno tentativi: Zeta 1a');
  Uguale(G.Posizione(b), 2, 'Alfa 2a');
  Uguale(G.Posizione(c), 3, 'Mimmo 3o');
  Verifica((G.Ordine[0] = a) and (G.Ordine[1] = b) and (G.Ordine[2] = c), 'ordine: Zeta, Alfa, Mimmo');
  G.Free;

  // chi risolve un round sta sopra chi non risolve
  G := TGara.Create;
  G.NumCodici := 2;
  G.SecondiRound := 100;
  PausaTraRoundSec := 1;
  a := G.Registra('Uno', 0); b := G.Registra('Due', 0);
  G.ImpostaSegreti(['1111', '2222']);
  G.Inizia(0);
  Prova(G, a, '1222', 10); Prova(G, b, '1222', 20);
  G.Tick(100000);
  Verifica(G.Stato = sgPausa, 'tempo scaduto: pausa');
  Uguale(G.Posizione(a), 1, 'stessi punti, tentativi e tempo: pari merito (Uno)');
  Uguale(G.Posizione(b), 1, 'stessi punti, tentativi e tempo: pari merito (Due)');
  G.Tick(101000);
  Verifica(G.Stato = sgRound, 'dopo la pausa parte il round 2');
  Prova(G, b, '2222', 106000);
  Verifica(G.Posizione(b) < G.Posizione(a), 'Due (ha risolto il round 2) e'' sopra Uno');
  G.Free;

  // lo spareggio per tempo vero e proprio: stessi punti e stessi tentativi ma tempo diverso
  G := TGara.Create;
  G.NumCodici := 2;
  G.SecondiRound := 100;
  PausaTraRoundSec := 1;
  a := G.Registra('Lenta', 0); b := G.Registra('Rapida', 0);
  G.ImpostaSegreti(['3333', '4444']);
  G.Inizia(0);
  Prova(G, a, '3333', 50000);   // Lenta risolve il round 1 per prima a 50 s: 160
  Prova(G, b, '3333', 60000);   // Rapida 2a a 60 s: 150
  G.ProssimoCodice(61000);
  Prova(G, b, '4444', 62000);   // round 2 (parte a 61000): Rapida 1a a 1 s: 160 -> totale 310
  Prova(G, a, '4444', 90000);   // Lenta 2a a 29 s: 150 -> totale 310
  Uguale(G.Totale(a), 310, 'Lenta 310');
  Uguale(G.Totale(b), 310, 'Rapida 310');
  Uguale(G.TentativiTotali(a), 2, 'stessi tentativi (2)');
  Uguale(G.TentativiTotali(b), 2, 'stessi tentativi (2)');
  Verifica(G.TempoTotaleMs(b) < G.TempoTotaleMs(a), 'Rapida ha impiegato meno tempo (' + IntToStr(G.TempoTotaleMs(b)) + ' contro ' + IntToStr(G.TempoTotaleMs(a)) + ' ms)');
  Uguale(G.Posizione(b), 1, 'a pari punti e tentativi vince il tempo: Rapida 1a');
  Uguale(G.Posizione(a), 2, 'Lenta 2a');
  G.Free;
end;

procedure TestFineRound;
var
  G: TGara;
  a, b, c: Integer;
begin
  WriteLn('== i tre modi in cui finisce un round ==');
  PausaTraRoundSec := 5;
  // 1. scade il tempo
  G := TGara.Create;
  G.NumCodici := 3; G.SecondiRound := 60;
  a := G.Registra('A', 0); b := G.Registra('B', 0);
  G.ImpostaSegreti(['1111', '2222', '3333']);
  G.Inizia(0);
  Uguale(G.SecondiRimasti(0), 60, 'all''inizio mancano 60 secondi');
  Uguale(G.SecondiRimasti(15000), 45, 'dopo 15 s ne mancano 45');
  Uguale(G.SecondiRimasti(59500), 1, 'a 59,5 s ne manca 1 (arrotondato per eccesso)');
  Prova(G, a, '1222', 10000);
  G.Tick(59999);
  Verifica(G.Stato = sgRound, 'a 59,999 s il round non e'' finito');
  G.Tick(60000);
  Verifica(G.Stato = sgPausa, 'a 60 s il round e'' finito: pausa');
  Verifica(G.UltimoMotivo = mfTempo, 'motivo: tempo scaduto');
  Uguale(G.SecondiRimasti(60000), 0, 'in pausa il tempo del round e'' 0');
  Uguale(G.SecondiPausaRimasti(60000), 5, 'pausa di 5 s');
  Uguale(G.PuntiRound(a), 20, 'in pausa si vedono ancora i punti del round: A = 20');
  Uguale(G.Totale(a), 20, 'e il totale non li conta due volte: 20');
  Verifica(Prova(G, a, '1111', 61000) = etNonInGioco, 'in pausa i tentativi non servono');
  G.Tick(64999);
  Verifica(G.Stato = sgPausa, 'dopo 4,999 s di pausa si aspetta ancora');
  G.Tick(65000);
  Verifica((G.Stato = sgRound) and (G.RoundCorrente = 2), 'finita la pausa parte da solo il round 2');
  Verifica(G.Segreto = '2222', 'con il codice 2222');
  Uguale(G.Totale(a), 20, 'il totale resta 20');
  Uguale(G.PuntiRound(a), 0, 'i punti del round 2 ripartono da 0');
  G.Free;

  // 2. tutti i collegati hanno risolto
  G := TGara.Create;
  G.NumCodici := 2; G.SecondiRound := 100;
  a := G.Registra('A', 0); b := G.Registra('B', 0); c := G.Registra('C', 0);
  G.ImpostaSegreti(['1111', '2222']);
  G.Inizia(0);
  Prova(G, a, '1111', 1000);
  G.Tick(1100);
  Verifica(G.Stato = sgRound, 'uno su tre ha risolto: il round continua');
  Prova(G, b, '1111', 2000);
  G.Tick(2100);
  Verifica(G.Stato = sgRound, 'due su tre: il round continua');
  Prova(G, c, '1111', 3000);
  G.Tick(3000);
  Verifica(G.Stato = sgPausa, 'tutti e tre hanno risolto: il round finisce');
  Verifica(G.UltimoMotivo = mfTutti, 'motivo: tutti hanno risolto');
  G.Free;

  // 2b. chi e' scollegato da piu' di 20 s non blocca la fine del round
  G := TGara.Create;
  G.NumCodici := 2; G.SecondiRound := 100;
  a := G.Registra('A', 0); b := G.Registra('B', 0);
  G.ImpostaSegreti(['1111', '2222']);
  G.Inizia(0);
  G.Registra('A', 30000);                    // A si fa sentire ancora, B e' sparito da 30 s
  Prova(G, a, '1111', 30500);
  G.Tick(30600);
  Verifica(G.Stato = sgPausa, 'B e'' scollegato da 30 s: non blocca la fine del round');
  Verifica(G.UltimoMotivo = mfTutti, 'motivo: tutti i collegati hanno risolto');
  G.Free;

  // 2c. nessun collegato: non finisce da solo
  G := TGara.Create;
  G.NumCodici := 2; G.SecondiRound := 100;
  G.Inizia(0);
  G.Tick(500);
  Verifica(G.Stato = sgRound, 'senza giocatori il round non finisce da solo');
  G.Tick(100000);
  Verifica(G.Stato = sgPausa, 'ma finisce col tempo');
  G.Free;

  // 3. il Prof preme "Prossimo codice" (in round, in pausa) e "Fine gara"
  G := TGara.Create;
  G.NumCodici := 3; G.SecondiRound := 100;
  a := G.Registra('A', 0); b := G.Registra('B', 0);
  G.ImpostaSegreti(['1111', '2222', '3333']);
  G.Inizia(0);
  G.ProssimoCodice(1000);
  Verifica((G.Stato = sgRound) and (G.RoundCorrente = 2) and (G.UltimoMotivo = mfDocente), 'Prossimo codice in round: round 2 subito');
  G.Tick(101000);
  Verifica(G.Stato = sgPausa, 'round 2 finito col tempo');
  G.ProssimoCodice(102000);
  Verifica((G.Stato = sgRound) and (G.RoundCorrente = 3), 'Prossimo codice in pausa: round 3 subito, senza aspettare');
  G.Free;

  G := TGara.Create;
  G.NumCodici := 3; G.SecondiRound := 100;
  a := G.Registra('A', 0);
  G.ImpostaSegreti(['1111', '2222', '3333']);
  G.Inizia(0);
  Prova(G, a, '1222', 500);
  G.Ferma(1000);
  Verifica(G.Stato = sgFinita, '"Fine gara" in round: la gara e'' finita');
  Uguale(G.Totale(a), 20, 'e i punti del round interrotto contano (20)');
  Uguale(G.RoundChiusi, 1, 'un round chiuso');
  G.Free;

  // ultimo round: finisce la gara in ognuno dei tre modi
  G := TGara.Create;
  G.NumCodici := 1; G.SecondiRound := 30;
  a := G.Registra('A', 0);
  G.ImpostaSegreti(['1111']);
  G.Inizia(0);
  Prova(G, a, '1111', 5000);
  G.Tick(5001);
  Verifica(G.Stato = sgFinita, 'un solo codice e tutti risolvono: gara finita');
  G.Free;

  // numeri fuori misura sono riportati nei limiti
  G := TGara.Create;
  G.NumCodici := 0; G.SecondiRound := 1;
  G.Inizia(0);
  Uguale(G.NumCodici, CODICI_MIN, 'numero di codici minimo');
  Uguale(G.SecondiRound, SECONDI_MIN, 'secondi minimi');
  G.Free;
  G := TGara.Create;
  G.NumCodici := 999; G.SecondiRound := 99999;
  G.Inizia(0);
  Uguale(G.NumCodici, CODICI_MAX, 'numero di codici massimo');
  Uguale(G.SecondiRound, SECONDI_MAX, 'secondi massimi');
  G.Free;
  G := TGara.Create;
  Uguale(G.NumCodici, 5, 'default: 5 codici');
  Uguale(G.SecondiRound, 180, 'default: 180 secondi');
  Verifica(G.Stato = sgFerma, 'una gara nuova e'' ferma');
  G.Free;
end;

procedure TestArrivoTardiEGaraNuova;
var
  G: TGara;
  a, b: Integer;
begin
  WriteLn('== chi arriva tardi, e una seconda gara ==');
  PausaTraRoundSec := 2;
  G := TGara.Create;
  G.NumCodici := 3; G.SecondiRound := 50;
  a := G.Registra('Presto', 0);
  G.ImpostaSegreti(['1111', '2222', '3333']);
  G.Inizia(0);
  Prova(G, a, '1111', 1000);
  G.Tick(50000);               // il round 1 e' finito col tempo
  G.Tick(52000);               // parte il round 2
  b := G.Registra('Tardi', 53000);
  Uguale(G.Totale(b), 0, 'chi arriva al round 2 parte da 0');
  Uguale(Length(G.Giocatore[b].Storico), 1, 'e nel suo storico c''e'' il round 1 a zero');
  Uguale(G.Giocatore[b].Storico[0].Punti, 0, 'round 1 a zero');
  Prova(G, b, '2222', 54000);
  Uguale(G.Totale(b), 160 - 0, 'Tardi risolve il round 2 per primo: 160');
  G.ProssimoCodice(55000);
  Uguale(G.Giocatore[b].Storico[1].Punti, 160, 'storico di Tardi: round 2 = 160');
  Uguale(G.Giocatore[a].Storico[0].Punti, 160, 'storico di Presto: round 1 = 160');
  G.Ferma(56000);
  Verifica(G.Stato = sgFinita, 'gara finita');
  Uguale(G.RoundChiusi, 3, 'tre round chiusi');
  // seconda gara: i nomi restano, i punti ripartono da zero
  G.ImpostaSegreti(['4444']);
  G.NumCodici := 1;
  G.Inizia(60000);
  Verifica(G.Stato = sgRound, 'la seconda gara parte');
  Uguale(G.Giocatori, 2, 'i due nomi ci sono ancora');
  Uguale(G.Totale(a), 0, 'punti di Presto azzerati');
  Uguale(G.Totale(b), 0, 'punti di Tardi azzerati');
  Uguale(G.TentativiTotali(a), 0, 'tentativi azzerati');
  Uguale(G.RoundChiusi, 0, 'round chiusi azzerati');
  Uguale(Length(G.Giocatore[a].Storico), 0, 'storico azzerato');
  G.Free;
end;

begin
  Randomize;
  TestFunzioni;
  TestPunteggiRound;
  TestRoundEClassifica;
  TestFineRound;
  TestArrivoTardiEGaraNuova;
  if errori > 0 then begin WriteLn('PROVA FALLITA: errori = ', errori); Halt(1); end;
  WriteLn('UnitGara: tutto ok');
end.
