program lfmsyntax;
{$mode objfpc}{$H+}
uses Classes, SysUtils;
var i, o: TFileStream;
begin
  i := TFileStream.Create(ParamStr(1), fmOpenRead);
  o := TFileStream.Create('/tmp/lfm.bin', fmCreate);
  ObjectTextToBinary(i, o);
  WriteLn('sintassi .lfm OK (', o.Size, ' byte binari): ', ParamStr(1));
end.
