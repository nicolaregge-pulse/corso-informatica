unit Grids;
{ FINTA: tiene le celle in un elenco di righe, per poterle rileggere nelle prove. }
{$mode objfpc}{$H+}
interface
uses SysUtils, Classes, Controls;
type
  TStringGrid = class(TControl)
  private
    FCelle: array of array of String;
    FColCount, FRowCount: Integer;
    FColW: array[0..20] of Integer;
    function GetCella(C, R: Integer): String;
    procedure SetCella(C, R: Integer; const V: String);
    procedure SetRowCount(V: Integer);
    procedure SetColCount(V: Integer);
    function GetColW(I: Integer): Integer;
    procedure SetColW(I, V: Integer);
  public
    FixedRows, FixedCols: Integer;
    property ColCount: Integer read FColCount write SetColCount;
    property RowCount: Integer read FRowCount write SetRowCount;
    property Cells[C, R: Integer]: String read GetCella write SetCella;
    property ColWidths[I: Integer]: Integer read GetColW write SetColW;
    procedure BeginUpdate;
    procedure EndUpdate;
  end;
implementation
function TStringGrid.GetCella(C, R: Integer): String;
begin
  Result := '';
  if (R < Length(FCelle)) and (C < Length(FCelle[R])) then Result := FCelle[R][C];
end;
procedure TStringGrid.SetCella(C, R: Integer; const V: String);
begin
  if (C < 0) or (C >= FColCount) or (R < 0) or (R >= FRowCount) then
    raise Exception.Create('cella fuori griglia');
  FCelle[R][C] := V;
end;
procedure TStringGrid.SetRowCount(V: Integer);
var i: Integer;
begin
  FRowCount := V;
  SetLength(FCelle, V);
  for i := 0 to V - 1 do SetLength(FCelle[i], FColCount);
end;
procedure TStringGrid.SetColCount(V: Integer);
var i: Integer;
begin
  FColCount := V;
  for i := 0 to High(FCelle) do SetLength(FCelle[i], V);
end;
function TStringGrid.GetColW(I: Integer): Integer; begin Result := FColW[I]; end;
procedure TStringGrid.SetColW(I, V: Integer); begin FColW[I] := V; end;
procedure TStringGrid.BeginUpdate; begin end;
procedure TStringGrid.EndUpdate; begin end;
end.
