program test_rete;
{ PROVA di UnitRete DA SOLA: nessuna finestra, nessuna finta LCL. Controlla le righe che il client scrive,
  il parser (ogni riga del server fa partire l'evento giusto, con i numeri giusti) e il server spento. }
{$mode objfpc}{$H+}
uses
  SysUtils, Classes, UnitRete;

type
  TAscolto = class
    Eventi: String;
    Cl: TClassifica;
    Neri, Bianchi, Tent, Sec: Integer;
    InGioco: Boolean;
    procedure Errore(Sender: TObject; const Motivo: String);
    procedure Rifiuto(Sender: TObject; const Motivo: String);
    procedure Stato(Sender: TObject; AInGioco: Boolean; const ACl: TClassifica);
    procedure Attesa(Sender: TObject);
    procedure Risultato(Sender: TObject; ANeri, ABianchi: Integer; const ACl: TClassifica);
    procedure Vittoria(Sender: TObject; ATent, ASec: Integer; const ACl: TClassifica);
  end;

var
  errori: Integer = 0;
  A: TAscolto;
  R: TClienteRete;

procedure TAscolto.Errore(Sender: TObject; const Motivo: String); begin Eventi := Eventi + 'ERRORE:' + Motivo + '|'; end;
procedure TAscolto.Rifiuto(Sender: TObject; const Motivo: String); begin Eventi := Eventi + 'RIFIUTO:' + Motivo + '|'; end;
procedure TAscolto.Stato(Sender: TObject; AInGioco: Boolean; const ACl: TClassifica);
begin Eventi := Eventi + 'STATO|'; InGioco := AInGioco; Cl := ACl; end;
procedure TAscolto.Attesa(Sender: TObject); begin Eventi := Eventi + 'ATTESA|'; end;
procedure TAscolto.Risultato(Sender: TObject; ANeri, ABianchi: Integer; const ACl: TClassifica);
begin Eventi := Eventi + 'RISULTATO|'; Neri := ANeri; Bianchi := ABianchi; Cl := ACl; end;
procedure TAscolto.Vittoria(Sender: TObject; ATent, ASec: Integer; const ACl: TClassifica);
begin Eventi := Eventi + 'VITTORIA|'; Tent := ATent; Sec := ASec; Cl := ACl; end;

procedure Verifica(Ok: Boolean; const Cosa: String);
begin
  if Ok then WriteLn('  ok   ', Cosa) else begin WriteLn('  ERRORE ', Cosa); Inc(errori); end;
end;

procedure Dai(const Riga: String);
begin A.Eventi := ''; R.Elabora(Riga); end;

begin
  WriteLn('== UnitRete da sola: righe e parser ==');
  A := TAscolto.Create;
  R := TClienteRete.Create;
  R.OnErrore := @A.Errore; R.OnRifiuto := @A.Rifiuto; R.OnStato := @A.Stato;
  R.OnAttesa := @A.Attesa; R.OnRisultato := @A.Risultato; R.OnVittoria := @A.Vittoria;
  R.Nome := 'Sara';
  Verifica(R.RigaStato = 'STATO;Sara', 'la riga di STATO e'' STATO;Sara');
  Verifica(R.RigaGuess('1234') = 'GUESS;Sara;1234', 'la riga di GUESS e'' GUESS;Sara;1234');
  Verifica(Campo('RESULT;1;2;3', 2) = '2', 'Campo numero 2 di RESULT;1;2;3 e'' 2');
  Verifica(Campo('WAIT', 5) = '', 'un campo che non c''e'' e'' vuoto');
  Dai('STATO;GIOCO;3;0;2;4;9');
  Verifica((A.Eventi = 'STATO|') and A.InGioco and (A.Cl.Tentativi = 3) and (A.Cl.Posto = 0) and (A.Cl.Finiti = 2) and
    (A.Cl.Migliore = 4) and (A.Cl.Peggiore = 9), 'STATO;GIOCO;3;0;2;4;9 -> evento Stato, in gioco, classifica giusta');
  Dai('STATO;ATTESA;0;0;0;0;0');
  Verifica((A.Eventi = 'STATO|') and not A.InGioco, 'STATO;ATTESA... -> non in gioco');
  Dai('WAIT');
  Verifica(A.Eventi = 'ATTESA|', 'WAIT -> evento Attesa');
  Dai('RESULT;1;2;5;0;3;4;9');
  Verifica((A.Eventi = 'RISULTATO|') and (A.Neri = 1) and (A.Bianchi = 2) and (A.Cl.Tentativi = 5) and
    (A.Cl.Finiti = 3) and (A.Cl.Migliore = 4) and (A.Cl.Peggiore = 9), 'RESULT;1;2;5;0;3;4;9 -> 1 nero, 2 bianchi, 5 tentativi');
  Dai('WIN;Sara;7;41;2;5;4;9');
  Verifica((A.Eventi = 'VITTORIA|') and (A.Tent = 7) and (A.Sec = 41) and (A.Cl.Tentativi = 7) and (A.Cl.Posto = 2) and
    (A.Cl.Finiti = 5) and (A.Cl.Migliore = 4) and (A.Cl.Peggiore = 9), 'WIN;Sara;7;41;2;5;4;9 -> 7 tentativi, 41 secondi, posto 2');
  Dai('ERR;nome non valido');
  Verifica(A.Eventi = 'RIFIUTO:nome non valido|', 'ERR;nome non valido -> evento Rifiuto con il motivo');
  Dai('CIAO');
  Verifica(Pos('ERRORE:Risposta strana', A.Eventi) = 1, 'una riga sconosciuta -> evento Errore');
  Dai('RESULT;x;y');
  Verifica((A.Eventi = 'RISULTATO|') and (A.Neri = 0), 'numeri rotti non fanno crashare (valgono 0)');
  WriteLn('== UnitRete da sola: server spento ==');
  R.Indirizzo := '127.0.0.1:5999';
  A.Eventi := '';
  Verifica(not R.ChiediStato, 'ChiediStato con il server spento dice False');
  Verifica(Pos('ERRORE:Connessione rifiutata', A.Eventi) = 1, 'e fa partire l''evento Errore: ' + A.Eventi);
  R.Free; A.Free;
  if errori > 0 then begin WriteLn('PROVA FALLITA: errori = ', errori); Halt(1); end;
  WriteLn('UnitRete: tutto ok');
end.
