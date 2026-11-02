program test_modello;
{ Prova il VERO unit1.pas del modello contro finte unita' LCL (NON e' la vera LCL):
  crea la finestra a mano, scrive un nome, "preme" il bottone e controlla il saluto. }
{$mode objfpc}{$H+}
uses Classes, SysUtils, StdCtrls, Unit1;

var
  F: TForm1;
  Errori: Integer = 0;

procedure Controlla(const Cosa, Atteso, Trovato: String);
begin
  if Atteso = Trovato then WriteLn('OK   ', Cosa, ': ', Trovato)
  else begin WriteLn('ERRORE ', Cosa, ': atteso [', Atteso, '] trovato [', Trovato, ']'); Inc(Errori); end;
end;

begin
  F := TForm1.Create(nil);
  F.LblTitolo := TLabel.Create(F);
  F.LblNome := TLabel.Create(F);
  F.EdNome := TEdit.Create(F);
  F.BtnCiao := TButton.Create(F);
  F.LblRisposta := TLabel.Create(F);
  F.AfterConstruction;                       // il collegamento di sicurezza deve dare il gestore al bottone
  Controlla('il bottone ha il gestore del clic', 'si', BoolToStr(Assigned(F.BtnCiao.OnClick), 'si', 'no'));
  F.EdNome.Text := 'Giulia';
  F.BtnCiao.OnClick(F.BtnCiao);              // "premo" il bottone
  Controlla('saluto con il nome', 'Ciao Giulia!', F.LblRisposta.Caption);
  F.EdNome.Text := '';
  F.BtnCiao.OnClick(F.BtnCiao);
  Controlla('saluto con casella vuota', 'Ciao !', F.LblRisposta.Caption);
  if Errori = 0 then WriteLn('TUTTO OK') else begin WriteLn('FALLITO: ', Errori); Halt(1); end;
end.
