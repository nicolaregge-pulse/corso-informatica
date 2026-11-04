program SlideshowAnimazione;

{ Slideshow animato 3INF - v1.0 (04/11/2026) }

{$mode objfpc}{$H+}

uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Interfaces, // la parte grafica di Lazarus (LCL)
  Forms, UnitFotogrammi, UnitPrincipale;

{$R *.res}

begin
  RequireDerivedFormResource := True;
  Application.Title := 'Slideshow animato';
  Application.Scaled := True;
  Application.Initialize;
  Application.CreateForm(TFormSlideshow, FormSlideshow);
  Application.Run;
end.
