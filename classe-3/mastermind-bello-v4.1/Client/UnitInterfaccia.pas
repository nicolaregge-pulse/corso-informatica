unit UnitInterfaccia;
{ MASTERMIND BELLO v4.1 - CLIENT per i ragazzi: la parte della FINESTRA (UnitInterfaccia + il suo .lfm).
  Qui ci sono finestra, disegni, bottoni, tavola di legno e pioli: NIENTE rete scritta qui.
  Tutta la rete sta in UnitRete.pas (un oggetto TClienteRete): questa unit lo usa e ascolta i suoi
  EVENTI (OnStato, OnRisultato, OnVittoria...), come ascolti OnClick di un bottone.
  UnitRete non sa niente di questa unit: cosi' non ci sono giri in tondo.
  Due modi per giocare:
    - "Connetti": ti colleghi al PC del prof (porta 5050) e giochi la partita di classe;
    - "Gioca da solo": il programma pensa lui il codice, non serve la rete.
  I colori sono 6 e possono RIPETERSI (rosso, rosso, blu, giallo e' un codice valido).
  Piolini di risposta: NERO = colore giusto al posto giusto, BIANCO = colore giusto al posto sbagliato.
  Come si gioca: clicca i colori nella fascia sotto la tavola (si riempiono i 4 buchi della riga
  illuminata), poi premi "Prova". Con "Togli l'ultimo" correggi.
  Versione v4.0: stessa grafica della v3.0, ma il programma e' diviso in due unit (interfaccia e rete).
  Versione v4.1: la GARA. Se il Prof lancia una gara a piu' codici, in alto compare un riquadro con
  "La tua posizione", i tuoi punti, il codice a cui sei (2 di 5) e il tempo che manca. La rete
  avvisa la finestra con tre eventi nuovi (OnRound, OnClassifica, OnFineGara). A fine gara
  compare un messaggio con il tuo posto. Il resto (tavola di legno, colori, tasti) e' come prima. }

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Types, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls,
  UnitRete;

type
  TCodice = array[0..3] of Integer;      // 4 colori, ognuno da 1 a 6 (0 = buco vuoto)
  TTentativo = record
    Colori: TCodice;
    Neri, Bianchi: Integer;
  end;
  TModo = (mNessuno, mRete, mLocale);

  TFormClient = class(TForm)
    LblIp: TLabel;
    EdIp: TEdit;
    LblNome: TLabel;
    EdNome: TEdit;
    BtnConnetti: TButton;
    BtnLocale: TButton;
    LblEsito: TLabel;
    LblStato: TLabel;
    PbTavola: TPaintBox;
    PbTavolozza: TPaintBox;
    PbMessaggio: TPaintBox;
    BtnProva: TButton;
    BtnCancella: TButton;
    LblPosizione: TLabel;
    LblMigliore: TLabel;
    LblPeggiore: TLabel;
    LblFiniti: TLabel;
    PbGara: TPaintBox;                // v4.1: il riquadro della gara (posizione, punti, codice, tempo)
    Timer1: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure BtnConnettiClick(Sender: TObject);
    procedure BtnLocaleClick(Sender: TObject);
    procedure BtnProvaClick(Sender: TObject);
    procedure BtnCancellaClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure PbTavolaPaint(Sender: TObject);
    procedure PbTavolozzaPaint(Sender: TObject);
    procedure PbMessaggioPaint(Sender: TObject);
    procedure PbGaraPaint(Sender: TObject);
    procedure PbTavolozzaMouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
  private
    Errori: Integer;
    Nome: String;
    Rete: TClienteRete;               // l'oggetto che parla con il server (UnitRete)
    UltimaCl: TClassifica;            // l'ultima classifica arrivata dalla rete
    UltimoInGioco: Boolean;           // l'ultimo STATO diceva GIOCO?
    function PulisciNome: String;
    procedure Mostra(const Cl: TClassifica);
    { i gestori degli eventi della rete: la rete li chiama, la finestra li scrive }
    procedure ReteErrore(Sender: TObject; const Motivo: String);
    procedure ReteRifiuto(Sender: TObject; const Motivo: String);
    procedure ReteStato(Sender: TObject; InGioco: Boolean; const Cl: TClassifica);
    procedure ReteAttesa(Sender: TObject);
    procedure ReteRisultato(Sender: TObject; Neri, Bianchi: Integer; const Cl: TClassifica);
    procedure ReteVittoria(Sender: TObject; Tentativi, Secondi: Integer; const Cl: TClassifica);
    { v4.1: gli eventi della gara }
    procedure ReteRound(Sender: TObject; Round, Totale, Secondi: Integer);
    procedure ReteClassifica(Sender: TObject; Pos, Punti, Giocatori: Integer;
      const NomePrimo: String; PuntiPrimo: Integer);
    procedure ReteFineGara(Sender: TObject; Pos, Punti, Giocatori: Integer);
    procedure AzzeraGara;
    procedure GaraTimer(Sender: TObject);
    procedure AggiornaBottoni;
    procedure Ricomincia;
    procedure Registra(Neri, Bianchi: Integer);
    procedure ProvaInLocale;
    procedure ProvaInRete;
    function PrimaRigaVisibile: Integer;
    procedure MostraDemo;
    procedure TastoPremuto(Sender: TObject; var Key: Char);
    procedure TitoloTimer(Sender: TObject);
  public
    TimerTitolo: TTimer;              // fa tornare il titolo normale dopo un istante
    TimerGara: TTimer;                // v4.1: ogni secondo rinfresca il tempo del riquadro della gara
    { v4.1: quello che sappiamo della gara (GaraAttiva = False: nessuna gara, il riquadro e' spento) }
    GaraAttiva: Boolean;
    GaraConclusa: Boolean;            // e' arrivato FINEGARA
    GaraInPausa: Boolean;             // il codice e' finito, si aspetta il prossimo
    GaraRound, GaraTotali: Integer;   // "codice 2 di 5"
    GaraSecondi: Integer;             // secondi che mancavano quando e' arrivato l'ultimo ROUND
    GaraRicevutoMs: QWord;            // e quando e' arrivato
    GaraHaClassifica: Boolean;
    GaraPos, GaraPunti, GaraGiocatori, GaraPuntiPrimo: Integer;
    GaraPrimo: String;
    GaraMessaggioDato: Boolean;       // il messaggio del podio si mostra una volta sola
    Avviato: Boolean;                 // True quando FormCreate e' gia' partita
    Modo: TModo;
    Finita: Boolean;                  // True dopo che hai indovinato
    Segreto: TCodice;                 // il codice (solo nel gioco "da solo")
    Corrente: TCodice;                // il tentativo che stai riempiendo
    NCorr: Integer;                   // quanti buchi hai gia' riempito (0..4)
    Storia: array[0..299] of TTentativo;
    NT: Integer;                      // quanti tentativi hai fatto
    procedure AfterConstruction; override;
    destructor Destroy; override;
    procedure AggiungiColore(C: Integer);
    procedure TogliUltimo;
    procedure ProvaTentativo;
    procedure NuovaPartitaLocale;
  end;

{ Conta i piolini di risposta. Neri = giusti al posto giusto; Bianchi = colore giusto al
  posto sbagliato. Funziona anche con colori ripetuti (esempio: segreto 1123, prova 1211). }
procedure Valuta(const Segreto, Prova: TCodice; out Neri, Bianchi: Integer);

var
  FormClient: TFormClient;
  FondoTavola: TBitmap;      // il legno (tavola + fascia dei colori, UN solo pezzo), disegnato una volta sola, in grande
  BufTavola, BufTavolozza, BufMessaggio, BufGara: TBitmap;   // le tele grandi su cui si disegna, poi si rimpiccioliscono

implementation

{$R *.lfm}

const
  // le misure sono in "pixel di progetto" (schermo al 100%), versione v3.0 al 90%
  RIGHE = 10;               // righe visibili sulla tavola
  CELLA = 36;               // altezza di una riga
  PASSO_X = 47;             // distanza tra i buchi in orizzontale
  TITOLO = 36;              // la fascia in alto con la scritta intagliata
  MARGINE = 13;
  RAGGIO = 14;              // raggio di un piolo grande
  RAGGIO_BUCO = 12;
  LARG_TAVOLA = 243;
  ALT_TAVOLA = 422;         // TITOLO + 2 * MARGINE + RIGHE * CELLA
  ALT_FASCIA = 60;          // la fascia dei 6 colori, sotto la tavola, stesso legno
  ALT_GARA = 54;            // v4.1: l'altezza del riquadro della gara
  X_PRIMO = 32;             // centro del primo buco di ogni riga
  LATO_RISP = 34;           // la nicchia delle risposte e' un QUADRATO 34 x 34
  X_PRIMO_COLORE = 22;      // centro del primo colore nella fascia
  PASSO_COLORE = 40;
  // sei colori, in ordine 1..6: rosso, giallo, verde, blu, arancio, porpora (formato BGR)
  COLORI: array[1..6] of Integer = ($002828DC, $001EC8F0, $003CA028, $00DC5A28, $001E82F0, $00AA328C);
  NOMI_COLORI: array[1..6] of String = ('rosso', 'giallo', 'verde', 'blu', 'arancio', 'porpora');
  LETTERE_COLORI: array[1..6] of String = ('R', 'G', 'V', 'B', 'A', 'P');   // la lettera di ogni colore
  TEMPO_CODICE_TITOLO_MS = 2300;     // il codice segreto resta nel titolo 2,3 secondi (23 decimi)
  MOSTRA_CODICE_NEL_TITOLO = True;   // metti False per non mostrarlo mai
  TITOLO_FORM = 'Mastermind bello - il tuo CLIENT';

{ ---------- il cervello: nessuna finestra, nessuna rete ---------- }

procedure Valuta(const Segreto, Prova: TCodice; out Neri, Bianchi: Integer);
var
  CS, CP: array[1..6] of Integer;
  I: Integer;
begin
  for I := 1 to 6 do
  begin
    CS[I] := 0;
    CP[I] := 0;
  end;
  Neri := 0;
  for I := 0 to 3 do
    if Segreto[I] = Prova[I] then
      Inc(Neri)
    else
    begin
      Inc(CS[Segreto[I]]);
      Inc(CP[Prova[I]]);
    end;
  Bianchi := 0;
  for I := 1 to 6 do
    if CS[I] < CP[I] then Inc(Bianchi, CS[I]) else Inc(Bianchi, CP[I]);
end;

{$I ../Comune/DisegnoMastermind.inc}

{ ---------- i fondi (disegnati UNA volta, in grande) e le tele ---------- }

procedure LiberaFondi;
begin
  FreeAndNil(FondoTavola);
  FreeAndNil(BufTavola);
  FreeAndNil(BufTavolozza);
  FreeAndNil(BufMessaggio);
  FreeAndNil(BufGara);
end;

function NuovaTela(W, H: Integer): TBitmap;
begin
  Result := TBitmap.Create;
  Result.Width := Sc(W);
  Result.Height := Sc(H);
end;

procedure PreparaFondi(Ppi: Integer);
begin
  if ImpostaScala(Ppi) then LiberaFondi;          // se lo schermo e' cambiato si rifa' tutto
  if FondoTavola = nil then
  begin
    // UN solo pezzo di legno: tavola + fascia dei colori, stesso tono
    FondoTavola := NuovaTela(LARG_TAVOLA, ALT_TAVOLA + ALT_FASCIA);
    DisegnaLegno(FondoTavola.Canvas, FondoTavola.Width, FondoTavola.Height, 7);
    IncidiScritta(FondoTavola.Canvas, FondoTavola.Width, Sc(TITOLO + 10), '3 INF');
    DisegnaScanalatura(FondoTavola.Canvas, Sc(8), Sc(LARG_TAVOLA - 8), Sc(ALT_TAVOLA));
    BufTavola := NuovaTela(LARG_TAVOLA, ALT_TAVOLA);
    BufTavolozza := NuovaTela(LARG_TAVOLA, ALT_FASCIA);
    BufMessaggio := NuovaTela(LARG_TAVOLA + 4, 32);
    BufGara := NuovaTela(LARG_TAVOLA + 4, ALT_GARA);
  end;
end;

{ ---------- la finestra ---------- }

{ una partita di ESEMPIO: appena premi F9 vedi subito il legno, i pioli colorati e i
  piolini neri e bianchi. Sparisce quando premi "Gioca da solo" o "Connetti". }
procedure TFormClient.MostraDemo;
const
  DEMO: array[0..4, 0..3] of Integer =
    ((2, 2, 5, 6), (1, 1, 2, 3), (1, 4, 4, 3), (4, 1, 1, 3), (1, 4, 1, 5));
var
  I, J: Integer;
  Sec: TCodice;
begin
  Sec[0] := 1;      // il codice dell'esempio: rosso, blu, rosso, verde (il rosso si ripete)
  Sec[1] := 4;
  Sec[2] := 1;
  Sec[3] := 3;
  for I := 0 to 4 do
  begin
    for J := 0 to 3 do Storia[I].Colori[J] := DEMO[I, J];
    Valuta(Sec, Storia[I].Colori, Storia[I].Neri, Storia[I].Bianchi);
  end;
  NT := 5;
  NCorr := 0;
end;

procedure TFormClient.FormCreate(Sender: TObject);
begin
  Avviato := True;
  Rete := TClienteRete.Create;            // la rete: e' un oggetto a parte, qui la colleghiamo ai nostri gestori
  Rete.OnErrore := @ReteErrore;
  Rete.OnRifiuto := @ReteRifiuto;
  Rete.OnStato := @ReteStato;
  Rete.OnAttesa := @ReteAttesa;
  Rete.OnRisultato := @ReteRisultato;
  Rete.OnVittoria := @ReteVittoria;
  Rete.OnRound := @ReteRound;               // v4.1: gli eventi della gara
  Rete.OnClassifica := @ReteClassifica;
  Rete.OnFineGara := @ReteFineGara;
  AzzeraGara;
  Modo := mNessuno;
  Finita := False;
  Errori := 0;
  NT := 0;
  NCorr := 0;
  Timer1.Enabled := False;
  Timer1.Interval := 3000;
  LblStato.Caption := 'Scegli come giocare';
  LblEsito.Caption := 'Questa e'' una partita di esempio. Premi "Gioca da solo" per giocare davvero.';
  MostraDemo;
  AggiornaBottoni;
end;

{ Se Lazarus non ha collegato gli eventi, li colleghiamo noi da qui }
procedure TFormClient.AfterConstruction;
begin
  inherited AfterConstruction;
  if not Assigned(BtnConnetti.OnClick) then BtnConnetti.OnClick := @BtnConnettiClick;
  if not Assigned(BtnLocale.OnClick) then BtnLocale.OnClick := @BtnLocaleClick;
  if not Assigned(BtnProva.OnClick) then BtnProva.OnClick := @BtnProvaClick;
  if not Assigned(BtnCancella.OnClick) then BtnCancella.OnClick := @BtnCancellaClick;
  if not Assigned(Timer1.OnTimer) then Timer1.OnTimer := @Timer1Timer;
  if not Assigned(PbTavola.OnPaint) then PbTavola.OnPaint := @PbTavolaPaint;
  if not Assigned(PbTavolozza.OnPaint) then PbTavolozza.OnPaint := @PbTavolozzaPaint;
  if not Assigned(PbMessaggio.OnPaint) then PbMessaggio.OnPaint := @PbMessaggioPaint;
  if not Assigned(PbGara.OnPaint) then PbGara.OnPaint := @PbGaraPaint;
  if not Assigned(PbTavolozza.OnMouseDown) then PbTavolozza.OnMouseDown := @PbTavolozzaMouseDown;
  KeyPreview := True;                                   // la finestra legge i tasti prima dei bottoni
  if not Assigned(OnKeyPress) then OnKeyPress := @TastoPremuto;
  // timer che fa tornare il titolo normale dopo che e' comparso il codice segreto
  TimerTitolo := TTimer.Create(Self);
  TimerTitolo.Enabled := False;
  TimerTitolo.Interval := TEMPO_CODICE_TITOLO_MS;
  TimerTitolo.OnTimer := @TitoloTimer;
  // timer del riquadro della gara: ogni secondo ricalcola il tempo che manca
  TimerGara := TTimer.Create(Self);
  TimerGara.Enabled := True;
  TimerGara.Interval := 1000;
  TimerGara.OnTimer := @GaraTimer;
  if not Avviato then FormCreate(nil);
end;

destructor TFormClient.Destroy;
begin
  Rete.Free;
  inherited Destroy;
end;

procedure TFormClient.TitoloTimer(Sender: TObject);
begin
  TimerTitolo.Enabled := False;
  Caption := TITOLO_FORM;
end;

{ Scorciatoia con la tastiera: R G V B A P = Rosso Giallo Verde Blu Arancio Porpora,
  Cancella (Backspace) toglie l'ultimo, Invio prova. Se stai scrivendo il nome o l'IP non succede niente. }
procedure TFormClient.TastoPremuto(Sender: TObject; var Key: Char);
var
  C: Integer;
begin
  if ActiveControl is TEdit then Exit;
  C := 0;
  case UpCase(Key) of
    'R': C := 1;
    'G': C := 2;
    'V': C := 3;
    'B': C := 4;
    'A': C := 5;
    'P': C := 6;
  end;
  if C > 0 then
  begin
    AggiungiColore(C);
    Key := #0;
  end
  else if Key = #8 then
  begin
    TogliUltimo;
    Key := #0;
  end
  else if Key = #13 then
  begin
    if BtnProva.Enabled then ProvaTentativo;
    Key := #0;
  end;
end;

function TFormClient.PulisciNome: String;
begin
  Result := Trim(StringReplace(EdNome.Text, ';', '', [rfReplaceAll]));
end;

{ Aggiorna le scritte della classifica con i numeri arrivati dalla rete }
procedure TFormClient.Mostra(const Cl: TClassifica);
begin
  if Cl.Migliore = 0 then LblMigliore.Caption := 'Migliore: -'
  else LblMigliore.Caption := 'Migliore: ' + IntToStr(Cl.Migliore);
  if Cl.Peggiore = 0 then LblPeggiore.Caption := 'Peggiore: -'
  else LblPeggiore.Caption := 'Peggiore: ' + IntToStr(Cl.Peggiore);
  if GaraAttiva then
  begin
    // in gara la tua posizione sta nel riquadro in alto: qui restano i numeri di QUESTO codice
    LblPosizione.Caption := 'Questo codice:';
    LblFiniti.Caption := 'Risolto da: ' + IntToStr(Cl.Finiti);
    LblPeggiore.Caption := '';
    Exit;
  end;
  if Cl.Posto = 0 then LblPosizione.Caption := 'Posto: non ancora'
  else LblPosizione.Caption := 'Posto: ' + IntToStr(Cl.Posto) + 'o';
  LblFiniti.Caption := 'Finiti: ' + IntToStr(Cl.Finiti);
end;

procedure TFormClient.AggiornaBottoni;
begin
  BtnProva.Enabled := (Modo <> mNessuno) and (not Finita) and (NCorr = 4) and
    (not GaraConclusa) and (not (GaraAttiva and GaraInPausa));
  BtnCancella.Enabled := (Modo <> mNessuno) and (not Finita) and (NCorr > 0) and (not GaraConclusa);
  PbTavola.Invalidate;
  PbMessaggio.Invalidate;
  PbGara.Invalidate;
end;

{ la prima riga della storia che si vede: se hai fatto piu' di 10 tentativi scorre }
function TFormClient.PrimaRigaVisibile: Integer;
begin
  if NT < RIGHE then Result := 0 else Result := NT - RIGHE + 1;
end;

procedure TFormClient.Ricomincia;
begin
  NT := 0;
  NCorr := 0;
  Finita := False;
  FillChar(Corrente, SizeOf(Corrente), 0);
  LblPosizione.Caption := '';
  LblMigliore.Caption := '';
  LblPeggiore.Caption := '';
  LblFiniti.Caption := '';
end;

{ ---------- i bottoni ---------- }

procedure TFormClient.BtnLocaleClick(Sender: TObject);
begin
  NuovaPartitaLocale;
end;

procedure TFormClient.NuovaPartitaLocale;
var
  I: Integer;
  Lettere: String;
begin
  Timer1.Enabled := False;
  AzzeraGara;
  Modo := mLocale;
  Randomize;
  for I := 0 to 3 do Segreto[I] := Random(6) + 1;   // i colori possono ripetersi
  if MOSTRA_CODICE_NEL_TITOLO then                  // il codice si vede un attimo nel titolo, poi torna normale
  begin
    Lettere := '';
    for I := 0 to 3 do Lettere := Lettere + LETTERE_COLORI[Segreto[I]] + ' ';
    Caption := 'Codice: ' + Trim(Lettere);
    TimerTitolo.Enabled := False;
    TimerTitolo.Enabled := True;
  end;
  Ricomincia;
  LblStato.Caption := 'DA SOLO: indovina il codice';
  LblEsito.Caption := 'Ho pensato 4 colori (anche uguali). Clicca i colori sotto la tavola e premi Prova.';
  AggiornaBottoni;
end;

procedure TFormClient.BtnConnettiClick(Sender: TObject);
begin
  Nome := PulisciNome;
  if Nome = '' then
  begin
    LblEsito.Caption := 'Scrivi prima il tuo nome nella casella.';
    Exit;
  end;
  if Trim(EdIp.Text) = '' then
  begin
    LblEsito.Caption := 'Scrivi l''IP del server (e'' scritto in alto nella pagina).';
    Exit;
  end;
  LblEsito.Caption := 'Mi collego...';
  AzzeraGara;                             // v4.1: si riparte da zero, la gara (se c'e') la dira' il server
  Rete.Nome := Nome;                      // diciamo alla rete chi siamo e dove andare...
  Rete.Indirizzo := EdIp.Text;
  if not Rete.ChiediStato then            // ...e le chiediamo lo STATO (se qualcosa va storto, scatta ReteErrore)
  begin
    Timer1.Enabled := False;
    if Modo = mRete then Modo := mNessuno;
    LblStato.Caption := 'Non collegato';
    AggiornaBottoni;
    Exit;
  end;
  Modo := mRete;
  Errori := 0;
  Ricomincia;
  LblEsito.Caption := 'Collegato! Ciao ' + Nome + '.';
  Mostra(UltimaCl);
  if UltimoInGioco then LblStato.Caption := 'GIOCO: provaci!'
  else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  if GaraAttiva and not GaraConclusa then      // v4.1: se c'e' una gara, le scritte sono quelle della gara
    ReteRound(Self, GaraRound, GaraTotali, GaraSecondi);
  AggiornaBottoni;
  Timer1.Enabled := True;
end;

procedure TFormClient.AggiungiColore(C: Integer);
begin
  if Modo = mNessuno then
  begin
    LblEsito.Caption := 'Prima premi "Gioca da solo" oppure Connetti.';
    Exit;
  end;
  if Finita or (C < 1) or (C > 6) then Exit;
  if NCorr < 4 then
  begin
    Corrente[NCorr] := C;
    Inc(NCorr);
    LblEsito.Caption := 'Hai scelto: ' + NOMI_COLORI[C] + '.';
  end;
  AggiornaBottoni;
end;

procedure TFormClient.TogliUltimo;
begin
  if NCorr > 0 then
  begin
    Dec(NCorr);
    Corrente[NCorr] := 0;
  end;
  AggiornaBottoni;
end;

procedure TFormClient.BtnCancellaClick(Sender: TObject);
begin
  TogliUltimo;
end;

procedure TFormClient.PbTavolozzaMouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
var
  I: Integer;
  S, Dx, Dy: Double;
begin
  S := 1;                                   // quanto lo schermo ingrandisce rispetto al progetto
  if PbTavolozza.Width > 0 then S := PbTavolozza.Width / LARG_TAVOLA;
  for I := 0 to 5 do
  begin
    Dx := X / S - (X_PRIMO_COLORE + I * PASSO_COLORE);
    Dy := Y / S - ALT_FASCIA div 2;
    if Dx * Dx + Dy * Dy <= (RAGGIO + 4) * (RAGGIO + 4) then
    begin
      AggiungiColore(I + 1);
      Exit;
    end;
  end;
end;

{ mette il tentativo appena giudicato nella storia e svuota la riga corrente }
procedure TFormClient.Registra(Neri, Bianchi: Integer);
begin
  if NT > High(Storia) then Exit;
  Storia[NT].Colori := Corrente;
  Storia[NT].Neri := Neri;
  Storia[NT].Bianchi := Bianchi;
  Inc(NT);
  NCorr := 0;
  FillChar(Corrente, SizeOf(Corrente), 0);
end;

procedure TFormClient.BtnProvaClick(Sender: TObject);
begin
  ProvaTentativo;
end;

procedure TFormClient.ProvaTentativo;
begin
  if Modo = mNessuno then
  begin
    LblEsito.Caption := 'Prima premi "Gioca da solo" oppure Connetti.';
    Exit;
  end;
  if NCorr <> 4 then
  begin
    LblEsito.Caption := 'Servono 4 colori: clicca ancora sui colori sotto la tavola.';
    Exit;
  end;
  if Modo = mLocale then ProvaInLocale else ProvaInRete;
  AggiornaBottoni;
end;

procedure TFormClient.ProvaInLocale;
var
  N, B: Integer;
begin
  Valuta(Segreto, Corrente, N, B);
  Registra(N, B);
  if N = 4 then
  begin
    Finita := True;
    LblStato.Caption := 'HAI VINTO!';
    LblEsito.Caption := 'BRAVO! Hai indovinato in ' + IntToStr(NT) + ' tentativi.';
  end
  else
    LblEsito.Caption := IntToStr(N) + ' neri (giusti al posto giusto), ' + IntToStr(B) +
      ' bianchi (giusti al posto sbagliato).';
end;

procedure TFormClient.ProvaInRete;
var
  Cod: String;
  I: Integer;
begin
  Cod := '';
  for I := 0 to 3 do Cod := Cod + Chr(48 + Corrente[I]);
  Rete.InviaTentativo(Cod);               // la risposta arriva con gli eventi: ReteRisultato, ReteVittoria...
end;

{ ---------- gli eventi della rete: la rete chiama, la finestra disegna ---------- }

procedure TFormClient.ReteErrore(Sender: TObject; const Motivo: String);
begin
  LblEsito.Caption := Motivo;
end;

procedure TFormClient.ReteRifiuto(Sender: TObject; const Motivo: String);
begin
  LblEsito.Caption := 'Il server dice: ' + Motivo;
end;

procedure TFormClient.ReteAttesa(Sender: TObject);
begin
  if GaraAttiva then
  begin
    LblEsito.Caption := 'Il codice e'' finito: aspetta il prossimo.';
    LblStato.Caption := 'CODICE FINITO: aspetta il prossimo';
    Exit;
  end;
  LblEsito.Caption := 'Il Prof non ha ancora detto Via: aspetta.';
  LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
end;

procedure TFormClient.ReteRisultato(Sender: TObject; Neri, Bianchi: Integer; const Cl: TClassifica);
begin
  if not GaraAttiva then LblStato.Caption := 'GIOCO: provaci!';
  Registra(Neri, Bianchi);
  LblEsito.Caption := IntToStr(Neri) + ' neri, ' + IntToStr(Bianchi) + ' bianchi';
  Mostra(Cl);
end;

procedure TFormClient.ReteVittoria(Sender: TObject; Tentativi, Secondi: Integer; const Cl: TClassifica);
begin
  Registra(4, 0);
  Finita := True;
  if GaraAttiva then
  begin
    LblStato.Caption := 'CODICE TROVATO!';
    LblEsito.Caption := 'BRAVO! Trovato in ' + IntToStr(Tentativi) + ' tentativi e ' +
      IntToStr(Secondi) + ' secondi. Aspetta il prossimo codice.';
  end
  else
  begin
    LblStato.Caption := 'HAI VINTO!';
    LblEsito.Caption := 'BRAVO! Hai indovinato in ' + IntToStr(Tentativi) + ' tentativi e ' +
      IntToStr(Secondi) + ' secondi.';
  end;
  Mostra(Cl);
end;

{ ---------- v4.1: la gara ---------- }

{ Si riparte senza gara: il riquadro si spegne }
procedure TFormClient.AzzeraGara;
begin
  GaraAttiva := False;
  GaraConclusa := False;
  GaraInPausa := False;
  GaraRound := 0;
  GaraTotali := 0;
  GaraSecondi := 0;
  GaraRicevutoMs := 0;
  GaraHaClassifica := False;
  GaraPos := 0;
  GaraPunti := 0;
  GaraGiocatori := 0;
  GaraPuntiPrimo := 0;
  GaraPrimo := '';
  GaraMessaggioDato := False;
end;

{ ROUND;k;N;secondi - siamo al codice k di N. Se k e' cambiato: tavola nuova, si riparte da zero. }
procedure TFormClient.ReteRound(Sender: TObject; Round, Totale, Secondi: Integer);
var
  Nuovo: Boolean;
begin
  Nuovo := (not GaraAttiva) or GaraConclusa or (Round <> GaraRound);
  GaraAttiva := True;
  GaraConclusa := False;
  GaraMessaggioDato := False;
  GaraTotali := Totale;
  GaraSecondi := Secondi;
  GaraRicevutoMs := GetTickCount64;
  GaraInPausa := Secondi <= 0;
  if Nuovo then
  begin
    GaraRound := Round;
    Ricomincia;                          // tavola pulita: nuovo codice, nuovi tentativi
    if GaraInPausa then
      LblEsito.Caption := 'Il codice ' + IntToStr(Round) + ' e'' finito. Aspetta il prossimo!'
    else
      LblEsito.Caption := 'Nuovo codice! Sei al codice ' + IntToStr(Round) + ' di ' + IntToStr(Totale) + '. Via!';
  end;
  if not Finita then
    if GaraInPausa then LblStato.Caption := 'CODICE FINITO: aspetta il prossimo'
    else LblStato.Caption := 'GARA - codice ' + IntToStr(Round) + ' di ' + IntToStr(Totale) + ': provaci!'
  else if GaraInPausa then
    LblStato.Caption := 'CODICE FINITO: aspetta il prossimo';
  AggiornaBottoni;
end;

{ CLASSIFICA;pos;totale;giocatori;nome1;punti1 - il tuo posto in classifica }
procedure TFormClient.ReteClassifica(Sender: TObject; Pos, Punti, Giocatori: Integer;
  const NomePrimo: String; PuntiPrimo: Integer);
begin
  GaraHaClassifica := True;
  GaraPos := Pos;
  GaraPunti := Punti;
  GaraGiocatori := Giocatori;
  GaraPrimo := NomePrimo;
  GaraPuntiPrimo := PuntiPrimo;
  PbGara.Invalidate;
end;

{ FINEGARA;pos;totale;giocatori - la gara e' finita: ecco il tuo posto }
procedure TFormClient.ReteFineGara(Sender: TObject; Pos, Punti, Giocatori: Integer);
var
  Frase, Podio: String;
begin
  GaraAttiva := True;
  GaraConclusa := True;
  GaraInPausa := True;
  GaraPos := Pos;
  GaraPunti := Punti;
  GaraGiocatori := Giocatori;
  GaraHaClassifica := True;
  case Pos of
    1: Frase := 'Sei 1o! Hai VINTO la gara! Complimenti, campione!';
    2: Frase := 'Sei 2o! Sei sul podio, che bravo!';
    3: Frase := 'Sei 3o! Sei sul podio, bravissimo!';
  else
    if (Giocatori > 0) and (Pos * 2 <= Giocatori) then
      Frase := 'Sei ' + IntToStr(Pos) + 'o su ' + IntToStr(Giocatori) + '! Bella gara, sei nella meta'' alta!'
    else
      Frase := 'Sei ' + IntToStr(Pos) + 'o su ' + IntToStr(Giocatori) + '. Hai finito la gara e questo conta! La prossima volta andra'' meglio.';
  end;
  LblStato.Caption := 'GARA FINITA!';
  LblEsito.Caption := Frase;
  AggiornaBottoni;
  if not GaraMessaggioDato then
  begin
    GaraMessaggioDato := True;       // il messaggio compare una volta sola
    Podio := 'GARA FINITA!' + LineEnding + LineEnding + Frase + LineEnding +
      'Hai fatto ' + IntToStr(Punti) + ' punti.';
    if (GaraPrimo <> '') and (Pos <> 1) then
      Podio := Podio + LineEnding + 'In testa c''e'' ' + GaraPrimo + ' con ' + IntToStr(GaraPuntiPrimo) + ' punti.';
    ShowMessage(Podio);
  end;
end;

{ ogni secondo: il tempo che manca scende (si ridisegna solo il riquadro) }
procedure TFormClient.GaraTimer(Sender: TObject);
begin
  if GaraAttiva and (not GaraConclusa) then PbGara.Invalidate;
end;

{ arriva STATO: aggiorna la classifica e la scritta GIOCO / ATTESA }
procedure TFormClient.ReteStato(Sender: TObject; InGioco: Boolean; const Cl: TClassifica);
begin
  UltimoInGioco := InGioco;
  UltimaCl := Cl;
  Mostra(Cl);
  if Finita and (Cl.Posto = 0) then
  begin
    // il Prof ha ricominciato con un'altra combinazione
    Ricomincia;
    LblStato.Caption := '';
  end;
  if (not Finita) and (not GaraAttiva) then
    if InGioco then LblStato.Caption := 'GIOCO: provaci!'
    else LblStato.Caption := 'ATTESA: aspetta il Via del Prof';
  AggiornaBottoni;
end;

{ ogni 3 secondi chiede al server come siamo messi (solo nel gioco in rete) }
procedure TFormClient.Timer1Timer(Sender: TObject);
begin
  if Modo <> mRete then Exit;
  if not Rete.ChiediStato then
  begin
    Inc(Errori);
    if Errori >= 3 then
    begin
      Modo := mNessuno;
      Timer1.Enabled := False;
      LblStato.Caption := 'Non collegato';
      LblEsito.Caption := 'Il server non risponde piu'': premi Connetti per riprovare.';
      AggiornaBottoni;
    end;
    Exit;
  end;
  Errori := 0;
end;


{ ---------- il disegno della tavola, della fascia dei colori e della legenda ---------- }

procedure TFormClient.PbTavolaPaint(Sender: TObject);
var
  B: TCanvas;
  Riga, Col, K, Cx, Cy, Ind, Prima, Bx0, Bx1: Integer;
begin
  PreparaFondi(PixelsPerInch);
  B := BufTavola.Canvas;
  B.Draw(0, 0, FondoTavola);                     // il legno (la parte alta del pezzo grande)
  Prima := PrimaRigaVisibile;
  for Riga := 0 to RIGHE - 1 do
  begin
    Cy := Sc(TITOLO + MARGINE + Riga * CELLA + CELLA div 2);
    Ind := Prima + Riga;
    if (Ind = NT) and (Modo <> mNessuno) and (not Finita) then
    begin
      // la riga che stai riempiendo e' "illuminata"
      B.Brush.Style := bsClear;
      B.Pen.Width := Sc(2);
      B.Pen.Color := MioColore(255, 226, 120);
      B.Rectangle(Sc(7), Cy - Sc(CELLA div 2 - 2), Sc(LARG_TAVOLA - 7), Cy + Sc(CELLA div 2 - 2));
      B.Pen.Width := 1;
      B.Brush.Style := bsSolid;
    end;
    for Col := 0 to 3 do
    begin
      Cx := Sc(X_PRIMO + Col * PASSO_X);
      if Ind < NT then
        DisegnaPiolo(B, Cx, Cy, Sc(RAGGIO), COLORI[Storia[Ind].Colori[Col]])
      else if (Ind = NT) and (Col < NCorr) and (Modo <> mNessuno) then
        DisegnaPiolo(B, Cx, Cy, Sc(RAGGIO), COLORI[Corrente[Col]])
      else
        DisegnaBuco(B, Cx, Cy, Sc(RAGGIO_BUCO));
    end;
    // la nicchia delle risposte: un QUADRATO nello stesso legno, solo un bordo incavato
    Bx1 := Sc(LARG_TAVOLA - 11);
    Bx0 := Bx1 - Sc(LATO_RISP);
    B.Pen.Style := psSolid;
    B.Pen.Width := Sc(2);
    B.Pen.Color := MioColore(84, 50, 22);        // ombra sopra e a sinistra
    B.MoveTo(Bx1, Cy - Sc(LATO_RISP div 2));
    B.LineTo(Bx0, Cy - Sc(LATO_RISP div 2));
    B.LineTo(Bx0, Cy + Sc(LATO_RISP div 2));
    B.Pen.Width := Sc(1);
    B.Pen.Color := MioColore(236, 194, 134);     // luce sotto e a destra
    B.MoveTo(Bx0, Cy + Sc(LATO_RISP div 2));
    B.LineTo(Bx1, Cy + Sc(LATO_RISP div 2));
    B.LineTo(Bx1, Cy - Sc(LATO_RISP div 2));
    B.Pen.Width := 1;
    // i 4 piolini piccoli di risposta, a 2 a 2
    for K := 0 to 3 do
    begin
      Cx := Bx0 + Sc(9 + (K mod 2) * 16);
      Col := Cy - Sc(8) + Sc((K div 2) * 16);
      if Ind < NT then
      begin
        if K < Storia[Ind].Neri then DisegnaRisposta(B, Cx, Col, Sc(6), True)
        else if K < Storia[Ind].Neri + Storia[Ind].Bianchi then DisegnaRisposta(B, Cx, Col, Sc(6), False)
        else DisegnaBuco(B, Cx, Col, Sc(4));
      end
      else
        DisegnaBuco(B, Cx, Col, Sc(4));
    end;
    if (Ind < NT) and (Storia[Ind].Neri = 4) then      // tutto giusto: la nicchia si illumina di verde
    begin
      B.Brush.Style := bsClear;
      B.Pen.Width := Sc(3);
      B.Pen.Color := MioColore(120, 220, 120);
      B.RoundRect(Bx0, Cy - Sc(LATO_RISP div 2), Bx1, Cy + Sc(LATO_RISP div 2), Sc(6), Sc(6));
      B.Pen.Width := 1;
      B.Brush.Style := bsSolid;
    end;
  end;
  RiduciSu(PbTavola.Canvas, Rect(0, 0, PbTavola.Width, PbTavola.Height), BufTavola);
end;

procedure TFormClient.PbTavolozzaPaint(Sender: TObject);
var
  B: TCanvas;
  I, Cx, Cy: Integer;
begin
  PreparaFondi(PixelsPerInch);
  B := BufTavolozza.Canvas;
  // la parte bassa dello stesso pezzo di legno
  B.CopyRect(Rect(0, 0, BufTavolozza.Width, BufTavolozza.Height), FondoTavola.Canvas,
    Rect(0, Sc(ALT_TAVOLA), BufTavolozza.Width, Sc(ALT_TAVOLA) + BufTavolozza.Height));
  Cy := Sc(ALT_FASCIA div 2);
  for I := 0 to 5 do
  begin
    Cx := Sc(X_PRIMO_COLORE + I * PASSO_COLORE);
    DisegnaBuco(B, Cx, Cy, Sc(RAGGIO));
    DisegnaPiolo(B, Cx, Cy, Sc(RAGGIO - 1), COLORI[I + 1]);   // solo pioli colorati da cliccare
  end;
  RiduciSu(PbTavolozza.Canvas, Rect(0, 0, PbTavolozza.Width, PbTavolozza.Height), BufTavolozza);
end;

{ la legenda: l'ultimo tentativo con i piolini veri (nero = giusto al posto giusto, bianco = posto sbagliato) }
procedure TFormClient.PbMessaggioPaint(Sender: TObject);
var
  B: TCanvas;
  Ex, Cy: Integer;
  Testo: String;
begin
  PreparaFondi(PixelsPerInch);
  B := BufMessaggio.Canvas;
  B.Brush.Style := bsSolid;
  B.Brush.Color := MioColore(255, 250, 235);
  B.Pen.Style := psSolid;
  B.Pen.Width := Sc(1);
  B.Pen.Color := MioColore(190, 170, 120);
  B.Rectangle(0, 0, BufMessaggio.Width, BufMessaggio.Height);
  B.Pen.Width := 1;
  B.Font.Name := 'Arial';
  B.Font.Height := -Sc(13);
  B.Font.Quality := fqCleartype;
  B.Font.Style := [];
  B.Font.Color := MioColore(0, 0, 0);
  B.Brush.Style := bsClear;
  Cy := BufMessaggio.Height div 2;
  Ex := Sc(14);
  if NT = 0 then
  begin
    B.Font.Color := MioColore(90, 70, 40);
    B.TextOut(Sc(8), Cy - B.TextHeight('Nero') div 2, 'Nero: giusto al posto giusto. Bianco: posto sbagliato.');
  end
  else
  begin
    DisegnaRisposta(B, Ex, Cy, Sc(6), True);
    Testo := IntToStr(Storia[NT - 1].Neri) + ' neri';
    B.TextOut(Ex + Sc(11), Cy - B.TextHeight(Testo) div 2, Testo);
    Ex := Ex + Sc(11) + B.TextWidth(Testo) + Sc(22);
    DisegnaRisposta(B, Ex, Cy, Sc(6), False);
    Testo := IntToStr(Storia[NT - 1].Bianchi) + ' bianchi';
    B.TextOut(Ex + Sc(11), Cy - B.TextHeight(Testo) div 2, Testo);
  end;
  B.Brush.Style := bsSolid;
  RiduciSu(PbMessaggio.Canvas, Rect(0, 0, PbMessaggio.Width, PbMessaggio.Height), BufMessaggio);
end;

{ v4.1: il riquadro della gara. Tre righe grandi e chiare:
    La tua posizione: 3o su 14
    punti 240   |   codice 2 di 5
    tempo 1:32   |   in testa: Sara (410)   }
procedure TFormClient.PbGaraPaint(Sender: TObject);
var
  B: TCanvas;
  Riga1, Riga2, Riga3, Primo: String;
  Rimasti, Trascorsi: Int64;
  Sfondo, Bordo: Integer;
begin
  PreparaFondi(PixelsPerInch);
  B := BufGara.Canvas;
  if not GaraAttiva then
  begin
    Sfondo := MioColore(255, 250, 235);
    Bordo := MioColore(190, 170, 120);
    Riga1 := 'Gara';
    Riga2 := 'Quando il Prof lancia una gara, qui vedi';
    Riga3 := 'la tua posizione in classifica.';
  end
  else
  begin
    Sfondo := MioColore(255, 240, 190);
    Bordo := MioColore(214, 160, 40);
    if GaraConclusa then
    begin
      Sfondo := MioColore(214, 240, 214);
      Bordo := MioColore(60, 150, 60);
    end;
    if GaraHaClassifica and (GaraPos > 0) then
      Riga1 := 'La tua posizione: ' + IntToStr(GaraPos) + 'o su ' + IntToStr(GaraGiocatori)
    else
      Riga1 := 'La tua posizione: in arrivo...';
    Riga2 := 'punti ' + IntToStr(GaraPunti) + '   |   codice ' + IntToStr(GaraRound) + ' di ' + IntToStr(GaraTotali);
    Primo := GaraPrimo;
    if Length(Primo) > 12 then Primo := Copy(Primo, 1, 12);
    if GaraConclusa then
      Riga3 := 'GARA FINITA   |   in testa: ' + Primo + ' (' + IntToStr(GaraPuntiPrimo) + ')'
    else if GaraInPausa then
      Riga3 := 'codice finito: aspetta il prossimo'
    else
    begin
      Trascorsi := Int64(GetTickCount64) - Int64(GaraRicevutoMs);
      Rimasti := GaraSecondi - (Trascorsi div 1000);
      if Rimasti < 0 then Rimasti := 0;
      Riga3 := 'tempo ' + IntToStr(Rimasti div 60) + ':' + Format('%.2d', [Integer(Rimasti mod 60)]);
      if GaraHaClassifica and (Primo <> '') then
        Riga3 := Riga3 + '   |   in testa: ' + Primo + ' (' + IntToStr(GaraPuntiPrimo) + ')';
    end;
  end;
  B.Brush.Style := bsSolid;
  B.Brush.Color := Sfondo;
  B.Pen.Style := psSolid;
  B.Pen.Width := Sc(3);
  B.Pen.Color := Bordo;
  B.Rectangle(0, 0, BufGara.Width, BufGara.Height);
  B.Pen.Width := 1;
  B.Brush.Style := bsClear;
  B.Font.Name := 'Arial';
  B.Font.Quality := fqCleartype;
  B.Font.Color := MioColore(60, 35, 10);
  B.Font.Height := -Sc(17);
  B.Font.Style := [fsBold];
  B.TextOut(Sc(8), Sc(4), Riga1);
  B.Font.Height := -Sc(13);
  B.Font.Style := [fsBold];
  B.TextOut(Sc(8), Sc(25), Riga2);
  B.Font.Style := [];
  B.TextOut(Sc(8), Sc(39), Riga3);
  B.Brush.Style := bsSolid;
  RiduciSu(PbGara.Canvas, Rect(0, 0, PbGara.Width, PbGara.Height), BufGara);
end;

end.
