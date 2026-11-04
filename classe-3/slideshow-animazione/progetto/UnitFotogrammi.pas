unit UnitFotogrammi;

{ Slideshow animato 3INF - v1.0 (04/11/2026)
  Trova i disegni (fotogrammi) di una cartella e li mette in ordine di nome.
  L'ordine e' "naturale": 2.png viene prima di 10.png (non come in Esplora file vecchio).
  Questa unit non usa la grafica: si prova anche da sola con Free Pascal (test/ProvaFotogrammi.lpr). }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils;

{ True se il file e' un'immagine che il programma sa aprire: .bmp .png .jpg .jpeg }
function EUnaImmagine(const NomeFile: String): Boolean;

{ Confronta due nomi: < 0 se A viene prima, 0 se uguali, > 0 se A viene dopo.
  I numeri dentro i nomi si confrontano come numeri: 'omino2' < 'omino10'. }
function ConfrontaNomi(const A, B: String): Integer;

{ Mette in Elenco il percorso completo di tutte le immagini di Cartella, in ordine di nome. }
procedure ElencaFotogrammi(const Cartella: String; Elenco: TStrings);

implementation

function EUnaImmagine(const NomeFile: String): Boolean;
var
  Estensione: String;
begin
  Estensione := LowerCase(ExtractFileExt(NomeFile));
  Result := (Estensione = '.bmp') or (Estensione = '.png') or
            (Estensione = '.jpg') or (Estensione = '.jpeg');
end;

function EUnaCifra(C: Char): Boolean;
begin
  Result := (C >= '0') and (C <= '9');
end;

function ConfrontaNomi(const A, B: String): Integer;
var
  I, J, InizioI, InizioJ: Integer;
  NumeroA, NumeroB: String;
  CA, CB: Char;
begin
  I := 1;
  J := 1;
  while (I <= Length(A)) and (J <= Length(B)) do
  begin
    if EUnaCifra(A[I]) and EUnaCifra(B[J]) then
    begin
      { tutte e due le parti sono numeri: le confronto come numeri }
      InizioI := I;
      while (I <= Length(A)) and EUnaCifra(A[I]) do Inc(I);
      InizioJ := J;
      while (J <= Length(B)) and EUnaCifra(B[J]) do Inc(J);
      NumeroA := Copy(A, InizioI, I - InizioI);
      NumeroB := Copy(B, InizioJ, J - InizioJ);
      { tolgo gli zeri davanti: 007 vale come 7 }
      while (Length(NumeroA) > 1) and (NumeroA[1] = '0') do Delete(NumeroA, 1, 1);
      while (Length(NumeroB) > 1) and (NumeroB[1] = '0') do Delete(NumeroB, 1, 1);
      if Length(NumeroA) <> Length(NumeroB) then
        Exit(Length(NumeroA) - Length(NumeroB));   { il numero piu' corto e' il piu' piccolo }
      Result := CompareStr(NumeroA, NumeroB);
      if Result <> 0 then Exit;
    end
    else
    begin
      CA := LowerCase(A[I]);
      CB := LowerCase(B[J]);
      if CA <> CB then
        Exit(Ord(CA) - Ord(CB));
      Inc(I);
      Inc(J);
    end;
  end;
  { un nome e' finito: il piu' corto viene prima }
  Result := (Length(A) - I) - (Length(B) - J);
  if Result = 0 then
    Result := CompareStr(A, B);
end;

function ConfrontaRighe(Lista: TStringList; Indice1, Indice2: Integer): Integer;
begin
  Result := ConfrontaNomi(ExtractFileName(Lista[Indice1]), ExtractFileName(Lista[Indice2]));
end;

procedure ElencaFotogrammi(const Cartella: String; Elenco: TStrings);
var
  Ricerca: TSearchRec;
  Percorso: String;
  Trovati: TStringList;
begin
  Elenco.Clear;
  if (Cartella = '') or not DirectoryExists(Cartella) then Exit;
  Percorso := IncludeTrailingPathDelimiter(Cartella);
  Trovati := TStringList.Create;
  try
    if FindFirst(Percorso + '*', faAnyFile, Ricerca) = 0 then
    begin
      repeat
        if ((Ricerca.Attr and faDirectory) = 0) and EUnaImmagine(Ricerca.Name) then
          Trovati.Add(Percorso + Ricerca.Name);
      until FindNext(Ricerca) <> 0;
      FindClose(Ricerca);
    end;
    Trovati.CustomSort(@ConfrontaRighe);
    Elenco.Assign(Trovati);
  finally
    Trovati.Free;
  end;
end;

end.
