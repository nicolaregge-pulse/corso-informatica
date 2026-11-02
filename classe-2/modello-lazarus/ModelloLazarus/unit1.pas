unit Unit1;
{ MODELLO LAZARUS - il punto di partenza per il tuo progetto.
  Una sola finestra (Form1) e una sola unit con tutto il codice: questo file.

  Che cosa fa gia' adesso:
    scrivi il tuo nome nella casella e premi il bottone: sotto compare «Ciao» + il tuo nome.

  DOVE SCRIVERE TU: cerca i commenti che iniziano con  >>> QUI
  Il resto, per ora, non toccarlo: funziona.

  Quando hai finito di provare: nel menu «Progetto» scegli «Salva progetto con nome»
  e dai un nome TUO al progetto, sempre nella stessa cartella. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    LblTitolo: TLabel;      // il titolo grande in alto
    LblNome: TLabel;        // la scritta «Come ti chiami?»
    EdNome: TEdit;          // la casella dove scrivi il nome (la sua scritta e' la proprieta' Text)
    BtnCiao: TButton;       // il bottone (la sua scritta e' la proprieta' Caption)
    LblRisposta: TLabel;    // qui compare il saluto
    procedure BtnCiaoClick(Sender: TObject);   // il «gestore del clic»: parte quando premi il bottone
  public
    procedure AfterConstruction; override;
  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ Questo codice parte OGNI VOLTA che premi il bottone «Salutami». }
procedure TForm1.BtnCiaoClick(Sender: TObject);
begin
  // >>> QUI: cambia il saluto. Per esempio prova 'Benvenuto ' + EdNome.Text
  LblRisposta.Caption := 'Ciao ' + EdNome.Text + '!';

  // >>> QUI: aggiungi le tue righe. Per esempio un messaggio a finestra:
  // ShowMessage('Piacere di conoscerti, ' + EdNome.Text);
end;

{ Collegamento di sicurezza: se il bottone non avesse il suo gestore del clic, glielo diamo noi.
  Non serve cambiarlo. }
procedure TForm1.AfterConstruction;
begin
  inherited AfterConstruction;
  if Assigned(BtnCiao) and not Assigned(BtnCiao.OnClick) then BtnCiao.OnClick := @BtnCiaoClick;
end;

end.
