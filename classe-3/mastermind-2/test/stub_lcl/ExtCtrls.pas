unit ExtCtrls;
{$mode objfpc}{$H+}
interface
uses Classes, Controls;
type TTimer = class(TControl) public Interval: Integer; OnTimer: TNotifyEvent; end;
implementation
end.
