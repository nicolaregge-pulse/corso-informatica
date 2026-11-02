{ piccolo aiuto per i test: Controlla(descrizione, condizione) }
var
  NProve, NFalliti: Integer;

procedure Controlla(const Descr: String; Ok: Boolean);
begin
  NProve := NProve + 1;
  if Ok then
    WriteLn('  OK   ', Descr)
  else
  begin
    NFalliti := NFalliti + 1;
    WriteLn('  FAIL ', Descr);
  end;
end;

procedure ControllaTesto(const Descr, Atteso, Avuto: String);
begin
  NProve := NProve + 1;
  if Atteso = Avuto then
    WriteLn('  OK   ', Descr, '  [', Avuto, ']')
  else
  begin
    NFalliti := NFalliti + 1;
    WriteLn('  FAIL ', Descr, '  atteso [', Atteso, '] avuto [', Avuto, ']');
  end;
end;

{ un tentativo SICURAMENTE sbagliato: cambia la prima cifra del codice }
function Sbagliato(const Segreto: String): String;
begin
  Result := Segreto;
  Result[1] := Chr(Ord('1') + (Ord(Segreto[1]) - Ord('1') + 1) mod 6);
end;

procedure Fine;
begin
  WriteLn;
  WriteLn('RISULTATO: ', NProve - NFalliti, ' prove OK su ', NProve, ', fallite: ', NFalliti);
  if NFalliti > 0 then Halt(1);
end;
