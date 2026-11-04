program ProvaFotogrammi;
{ Prova con Free Pascal (senza grafica) della unit UnitFotogrammi: ordine dei nomi e ricerca nella cartella. }
{$mode objfpc}{$H+}
uses Classes, SysUtils, UnitFotogrammi;
var
  Errori: Integer = 0;
  L: TStringList;
  Cartella, S: String;
  I: Integer;
procedure Atteso(Cond: Boolean; const Cosa: String);
begin
  if Cond then WriteLn('OK   ', Cosa) else begin WriteLn('NO   ', Cosa); Inc(Errori); end;
end;
procedure Crea(const Nome: String);
var F: TFileStream;
begin
  F := TFileStream.Create(Cartella + Nome, fmCreate); F.Free;
end;
begin
  Atteso(ConfrontaNomi('omino2.png', 'omino10.png') < 0, 'omino2 prima di omino10');
  Atteso(ConfrontaNomi('02.png', '1.png') > 0, '02 dopo 1');
  Atteso(ConfrontaNomi('A.png', 'b.png') < 0, 'maiuscole e minuscole uguali');
  Atteso(ConfrontaNomi('3.png', '3.png') = 0, 'nomi uguali');
  Atteso(EUnaImmagine('x.PNG') and EUnaImmagine('x.bmp') and EUnaImmagine('x.jpeg'), 'estensioni immagine');
  Atteso(not EUnaImmagine('x.txt') and not EUnaImmagine('x'), 'non immagini');
  Cartella := IncludeTrailingPathDelimiter(GetTempDir) + 'prova-fotogrammi-' + IntToStr(GetProcessID) + PathDelim;
  ForceDirectories(Cartella);
  ForceDirectories(Cartella + 'sotto.png');
  Crea('10.png'); Crea('2.bmp'); Crea('1.png'); Crea('note.txt'); Crea('Omino 3.JPG');
  L := TStringList.Create;
  ElencaFotogrammi(Cartella, L);
  S := '';
  for I := 0 to L.Count - 1 do S := S + ExtractFileName(L[I]) + ' ';
  WriteLn('trovati: ', S);
  Atteso(S = '1.png 2.bmp 10.png Omino 3.JPG ', 'ordine 1, 2, 10, Omino 3 (niente .txt, niente cartelle)');
  ElencaFotogrammi(Cartella + 'non-esiste', L);
  Atteso(L.Count = 0, 'cartella che non esiste: elenco vuoto');
  L.Free;
  if Errori = 0 then WriteLn('TUTTO OK') else WriteLn('ERRORI: ', Errori);
  Halt(Errori);
end.
