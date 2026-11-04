unit UnitGara;
{ MASTERMIND BELLO v4.1 - LA GARA (solo calcoli: niente finestre, niente rete, niente orologio).

  Questa unit sa fare UNA cosa: tenere i conti di una gara di piu' codici.
    - una gara e' fatta di N "round" (N codici segreti, uno dopo l'altro);
    - in ogni round ogni ragazzo fa dei tentativi: piu' si avvicina al codice, piu' punti prende;
    - alla fine si sommano i punti dei round e si fa la classifica.
  NON conosce il Server (UnitServer) e NON conosce la rete: il Server le dice "e' arrivato un
  tentativo di Sara" e lei risponde con i punti. Per questo si puo' provare da sola con fpc (test_gara.pas).
  Il tempo non lo legge da sola: glielo passa chi la usa (in millisecondi), cosi' le prove sono sempre uguali.

  ---------- COME SI FANNO I PUNTI (tutto in italiano semplice, i numeri sono qui sotto) ----------
  Per ogni round, ogni ragazzo prende:
    1. VICINANZA: guarda il suo tentativo MIGLIORE. Ogni piolo NERO vale 2, ogni piolo BIANCO vale 1;
       si somma e si moltiplica per 10. (3 neri = 60 punti, 2 neri + 1 bianco = 50, ...)
    2. BONUS RISOLTO: +50 se trova il codice (4 neri).
    3. BONUS VELOCITA': tra chi risolve, il 1o prende +30, il 2o +20, il 3o +10, gli altri +0.
    4. PENALITA': -1 per ogni tentativo oltre il 6o (cosi' non conviene provare a caso).
    Punti del round = vicinanza + bonus risolto + bonus velocita' - penalita' (mai sotto zero).
    Massimo di un round: 80 + 50 + 30 = 160. Chi non risolve arriva al massimo a 60.
  Punti TOTALI = somma dei punti dei round. In classifica: piu' punti sta sopra; a parita' di punti
  vince chi ha fatto MENO tentativi in tutto; a ulteriore parita' chi e' stato piu' veloce.
  A pari di tutto: stesso posto (pari merito).

  ---------- QUANDO FINISCE UN ROUND ----------
    1. e' scaduto il tempo del round (default 180 secondi);
    2. TUTTI i collegati hanno trovato il codice;
    3. il Prof preme "Prossimo codice".
  Dopo la fine di un round c'e' una pausa breve (PausaTraRoundSec) in cui si vede la classifica,
  poi parte da solo il round successivo (oppure subito, se il Prof preme "Prossimo codice"). }

{$mode objfpc}{$H+}

interface

uses
  SysUtils;

const
  { ---- i numeri del punteggio: si cambiano qui (e poi si aggiorna il LEGGIMI) ---- }
  PUNTI_PER_NERO = 2;                // un piolo nero (colore giusto al posto giusto) vale 2
  PUNTI_PER_BIANCO = 1;              // un piolo bianco (colore giusto al posto sbagliato) vale 1
  MOLTIPLICATORE_VICINANZA = 10;     // la somma neri/bianchi del tentativo migliore si moltiplica per 10
  BONUS_RISOLTO = 50;                // chi trova il codice prende +50
  BONUS_VELOCITA: array[1..3] of Integer = (30, 20, 10);   // 1o, 2o, 3o a risolvere; gli altri 0
  TENTATIVI_SENZA_PENALITA = 6;      // fino al 6o tentativo non si perde niente
  PENALITA_PER_TENTATIVO = 1;        // poi -1 per ogni tentativo in piu'

  { ---- i numeri della gara ---- }
  CODICI_DEFAULT = 5;                // quanti codici (round) ha una gara, se il Prof non cambia
  CODICI_MIN = 1;
  CODICI_MAX = 30;
  SECONDI_DEFAULT = 180;             // quanti secondi dura un round, se il Prof non cambia
  SECONDI_MIN = 10;
  SECONDI_MAX = 1800;
  PAUSA_TRA_ROUND_DEFAULT = 8;       // secondi di pausa tra un round e il successivo
  FUORI_LINEA_GARA_MS = 20000;       // dopo 20 secondi senza notizie uno non e' piu' "collegato"

type
  TStatoGara = (sgFerma, sgRound, sgPausa, sgFinita);
  TMotivoFine = (mfNessuno, mfTempo, mfTutti, mfDocente);
  TEsitoTentativo = (etNonInGioco, etCodiceNonValido, etRisultato, etRisolto, etGiaRisolto);
  TElencoIndici = array of Integer;

  { cosa e' successo a un ragazzo in un round chiuso (resta nello storico) }
  TRisultatoRound = record
    Tentativi: Integer;
    Vicinanza: Integer;       // 2 * neri + bianchi del tentativo migliore (0..8)
    Risolto: Boolean;
    PosVelocita: Integer;     // 1, 2, 3... tra chi ha risolto (0 = non ha risolto)
    Punti: Integer;           // punti presi in quel round
  end;

  TGiocatoreGara = record
    Nome: String;
    UltimoVisto: Int64;       // l'ultima volta che si e' fatto sentire (ms)
    { il round in corso (o l'ultimo finito) }
    TentRound: Integer;
    MigliorVic: Integer;
    Risolto: Boolean;
    PosVelocita: Integer;
    TempoRisoltoMs: Int64;
    PuntiUltimoRound: Integer;   // punti dell'ultimo round chiuso (si vedono durante la pausa)
    { la somma dei round gia' chiusi }
    PuntiChiusi: Integer;
    TentChiusi: Integer;
    TempoChiusoMs: Int64;
    Storico: array of TRisultatoRound;     // un elemento per ogni round chiuso
  end;

  TGara = class
  private
    FG: array of TGiocatoreGara;
    FStato: TStatoGara;
    FRound: Integer;
    FSegreto: String;
    FInizioRound: Int64;
    FFinePausa: Int64;
    FRisolti: Integer;
    FRoundChiusi: Integer;
    FMotivo: TMotivoFine;
    FSegretiPronti: array of String;
    FUltimoChiuso: String;
    procedure IniziaRound(Adesso: Int64);
    procedure ChiudiRound(Motivo: TMotivoFine; Adesso: Int64);
    function TuttiHannoRisolto(Adesso: Int64): Boolean;
    function Meglio(A, B: Integer): Boolean;
    function GetGiocatore(Idx: Integer): TGiocatoreGara;
  public
    NumCodici: Integer;       // quanti round (da impostare prima di Inizia)
    SecondiRound: Integer;    // quanti secondi dura un round (da impostare prima di Inizia)
    constructor Create;
    { ---- i giocatori ---- }
    function Giocatori: Integer;
    function Cerca(const Nome: String): Integer;                  // -1 se non c'e'
    function Registra(const Nome: String; Adesso: Int64): Integer; // lo trova o lo aggiunge; segna che si e' fatto sentire
    property Giocatore[Idx: Integer]: TGiocatoreGara read GetGiocatore;
    function Collegato(Idx: Integer; Adesso: Int64): Boolean;
    { ---- il filo della gara ---- }
    procedure ImpostaSegreti(const Elenco: array of String);      // codici decisi in anticipo (per le prove)
    procedure Inizia(Adesso: Int64);                              // parte il round 1
    procedure ImpostaSegreto(const S: String);                    // cambia il codice del round in corso (per le prove)
    function Tentativo(Idx: Integer; const Codice: String; Adesso: Int64;
      out Neri, Bianchi: Integer): TEsitoTentativo;
    procedure Tick(Adesso: Int64);                                // da chiamare spesso: fa finire/partire i round
    procedure ProssimoCodice(Adesso: Int64);                      // il Prof: "basta cosi', prossimo"
    procedure Ferma(Adesso: Int64);                               // il Prof: "fine gara"
    { ---- cosa si vede ---- }
    property Stato: TStatoGara read FStato;
    property RoundCorrente: Integer read FRound;
    property Segreto: String read FSegreto;
    property Risolti: Integer read FRisolti;                      // quanti hanno risolto nel round in corso
    property RoundChiusi: Integer read FRoundChiusi;              // quanti round sono finiti (cresce di 1 a ogni fine)
    property UltimoMotivo: TMotivoFine read FMotivo;              // perche' e' finito l'ultimo round
    property CodiceUltimoChiuso: String read FUltimoChiuso;       // il codice dell'ultimo round finito
    function SecondiRimasti(Adesso: Int64): Integer;              // nel round: quanto manca; in pausa 0
    function SecondiPausaRimasti(Adesso: Int64): Integer;
    function PuntiRound(Idx: Integer): Integer;                   // i punti del round (in diretta, o dell'ultimo finito)
    function Totale(Idx: Integer): Integer;                       // punti totali (round chiusi + round in corso)
    function TentativiTotali(Idx: Integer): Integer;
    function TempoTotaleMs(Idx: Integer): Int64;
    function Ordine: TElencoIndici;                               // gli indici dal primo all'ultimo
    function Posizione(Idx: Integer): Integer;                    // 1, 2, 3... (pari merito = stesso posto)
  end;

var
  PausaTraRoundSec: Integer = PAUSA_TRA_ROUND_DEFAULT;   // le prove lo accorciano

{ ---- funzioni semplici, usabili da sole ---- }
function CodiceValido(const S: String): Boolean;
procedure ValutaCodice(const Segreto, Prova: String; out Neri, Bianchi: Integer);
function Vicinanza(Neri, Bianchi: Integer): Integer;              // 2 * neri + bianchi
function BonusVelocita(PosVelocita: Integer): Integer;
function Penalita(Tentativi: Integer): Integer;
function PunteggioRound(Vic: Integer; Risolto: Boolean; PosVelocita, Tentativi: Integer): Integer;
function NuovoCodiceCasuale: String;

implementation

function CodiceValido(const S: String): Boolean;
var
  i: Integer;
begin
  Result := Length(S) = 4;
  if Result then
    for i := 1 to 4 do
      if not (S[i] in ['1'..'6']) then Result := False;
end;

{ Neri = giusti al posto giusto; Bianchi = colore giusto al posto sbagliato (anche con colori ripetuti) }
procedure ValutaCodice(const Segreto, Prova: String; out Neri, Bianchi: Integer);
var
  CS, CP: array[1..6] of Integer;
  i: Integer;
begin
  for i := 1 to 6 do
  begin
    CS[i] := 0;
    CP[i] := 0;
  end;
  Neri := 0;
  for i := 1 to 4 do
    if Segreto[i] = Prova[i] then
      Inc(Neri)
    else
    begin
      Inc(CS[Ord(Segreto[i]) - 48]);
      Inc(CP[Ord(Prova[i]) - 48]);
    end;
  Bianchi := 0;
  for i := 1 to 6 do
    if CS[i] < CP[i] then Inc(Bianchi, CS[i]) else Inc(Bianchi, CP[i]);
end;

function Vicinanza(Neri, Bianchi: Integer): Integer;
begin
  Result := PUNTI_PER_NERO * Neri + PUNTI_PER_BIANCO * Bianchi;
end;

function BonusVelocita(PosVelocita: Integer): Integer;
begin
  if (PosVelocita >= Low(BONUS_VELOCITA)) and (PosVelocita <= High(BONUS_VELOCITA)) then
    Result := BONUS_VELOCITA[PosVelocita]
  else
    Result := 0;
end;

function Penalita(Tentativi: Integer): Integer;
begin
  if Tentativi > TENTATIVI_SENZA_PENALITA then
    Result := (Tentativi - TENTATIVI_SENZA_PENALITA) * PENALITA_PER_TENTATIVO
  else
    Result := 0;
end;

function PunteggioRound(Vic: Integer; Risolto: Boolean; PosVelocita, Tentativi: Integer): Integer;
begin
  Result := Vic * MOLTIPLICATORE_VICINANZA;
  if Risolto then Result := Result + BONUS_RISOLTO + BonusVelocita(PosVelocita);
  Result := Result - Penalita(Tentativi);
  if Result < 0 then Result := 0;
end;

function NuovoCodiceCasuale: String;
var
  i: Integer;
begin
  Result := '';
  for i := 1 to 4 do Result := Result + IntToStr(Random(6) + 1);   // 4 colori, anche ripetuti
end;

{ ---------------- TGara ---------------- }

constructor TGara.Create;
begin
  inherited Create;
  NumCodici := CODICI_DEFAULT;
  SecondiRound := SECONDI_DEFAULT;
  FStato := sgFerma;
  FRound := 0;
  FSegreto := '';
  FMotivo := mfNessuno;
  FUltimoChiuso := '';
end;

function TGara.Giocatori: Integer;
begin
  Result := Length(FG);
end;

function TGara.GetGiocatore(Idx: Integer): TGiocatoreGara;
begin
  Result := FG[Idx];
end;

function TGara.Cerca(const Nome: String): Integer;
var
  i: Integer;
begin
  Result := -1;
  for i := 0 to High(FG) do
    if SameText(FG[i].Nome, Nome) then
    begin
      Result := i;
      Exit;
    end;
end;

function TGara.Registra(const Nome: String; Adesso: Int64): Integer;
var
  k: Integer;
begin
  Result := Cerca(Nome);
  if Result < 0 then
  begin
    SetLength(FG, Length(FG) + 1);
    Result := High(FG);
    FG[Result].Nome := Nome;
    FG[Result].TentRound := 0;
    FG[Result].MigliorVic := 0;
    FG[Result].Risolto := False;
    FG[Result].PosVelocita := 0;
    FG[Result].TempoRisoltoMs := 0;
    FG[Result].PuntiUltimoRound := 0;
    FG[Result].PuntiChiusi := 0;
    FG[Result].TentChiusi := 0;
    FG[Result].TempoChiusoMs := 0;
    // chi arriva a gara iniziata ha zero nei round gia' chiusi
    SetLength(FG[Result].Storico, FRoundChiusi);
    for k := 0 to FRoundChiusi - 1 do
      FillChar(FG[Result].Storico[k], SizeOf(TRisultatoRound), 0);
  end;
  FG[Result].UltimoVisto := Adesso;
end;

function TGara.Collegato(Idx: Integer; Adesso: Int64): Boolean;
begin
  Result := Adesso - FG[Idx].UltimoVisto <= FUORI_LINEA_GARA_MS;
end;

procedure TGara.ImpostaSegreti(const Elenco: array of String);
var
  i: Integer;
begin
  SetLength(FSegretiPronti, Length(Elenco));
  for i := 0 to High(Elenco) do FSegretiPronti[i] := Elenco[i];
end;

procedure TGara.ImpostaSegreto(const S: String);
begin
  if CodiceValido(S) then FSegreto := S;
end;

procedure TGara.IniziaRound(Adesso: Int64);
var
  i: Integer;
begin
  Inc(FRound);
  if (FRound - 1 <= High(FSegretiPronti)) and CodiceValido(FSegretiPronti[FRound - 1]) then
    FSegreto := FSegretiPronti[FRound - 1]
  else
    FSegreto := NuovoCodiceCasuale;
  FInizioRound := Adesso;
  FRisolti := 0;
  FStato := sgRound;
  for i := 0 to High(FG) do
  begin
    FG[i].TentRound := 0;
    FG[i].MigliorVic := 0;
    FG[i].Risolto := False;
    FG[i].PosVelocita := 0;
    FG[i].TempoRisoltoMs := 0;
    FG[i].PuntiUltimoRound := 0;
  end;
end;

procedure TGara.Inizia(Adesso: Int64);
var
  i: Integer;
begin
  if NumCodici < CODICI_MIN then NumCodici := CODICI_MIN;
  if NumCodici > CODICI_MAX then NumCodici := CODICI_MAX;
  if SecondiRound < SECONDI_MIN then SecondiRound := SECONDI_MIN;
  if SecondiRound > SECONDI_MAX then SecondiRound := SECONDI_MAX;
  FRound := 0;
  FRoundChiusi := 0;
  FMotivo := mfNessuno;
  for i := 0 to High(FG) do      // una gara nuova riparte da zero, ma i nomi restano
  begin
    SetLength(FG[i].Storico, 0);
    FG[i].PuntiChiusi := 0;
    FG[i].TentChiusi := 0;
    FG[i].TempoChiusoMs := 0;
  end;
  IniziaRound(Adesso);
end;

function TGara.Tentativo(Idx: Integer; const Codice: String; Adesso: Int64;
  out Neri, Bianchi: Integer): TEsitoTentativo;
var
  V: Integer;
begin
  Neri := 0;
  Bianchi := 0;
  if (FStato <> sgRound) or (Idx < 0) or (Idx > High(FG)) then
  begin
    Result := etNonInGioco;
    Exit;
  end;
  if not CodiceValido(Codice) then
  begin
    Result := etCodiceNonValido;
    Exit;
  end;
  FG[Idx].UltimoVisto := Adesso;
  ValutaCodice(FSegreto, Codice, Neri, Bianchi);
  if FG[Idx].Risolto then            // dopo la vittoria i tentativi non contano piu'
  begin
    Result := etGiaRisolto;
    Exit;
  end;
  Inc(FG[Idx].TentRound);
  V := Vicinanza(Neri, Bianchi);
  if V > FG[Idx].MigliorVic then FG[Idx].MigliorVic := V;
  if Neri = 4 then
  begin
    FG[Idx].Risolto := True;
    Inc(FRisolti);
    FG[Idx].PosVelocita := FRisolti;
    FG[Idx].TempoRisoltoMs := Adesso - FInizioRound;
    Result := etRisolto;
  end
  else
    Result := etRisultato;
end;

function TGara.TuttiHannoRisolto(Adesso: Int64): Boolean;
var
  i, quanti: Integer;
begin
  quanti := 0;
  Result := True;
  for i := 0 to High(FG) do
    if Collegato(i, Adesso) then
    begin
      Inc(quanti);
      if not FG[i].Risolto then Result := False;
    end;
  if quanti = 0 then Result := False;
end;

procedure TGara.ChiudiRound(Motivo: TMotivoFine; Adesso: Int64);
var
  i, n, k: Integer;
begin
  if FStato <> sgRound then Exit;
  for i := 0 to High(FG) do
  begin
    FG[i].PuntiUltimoRound := PunteggioRound(FG[i].MigliorVic, FG[i].Risolto, FG[i].PosVelocita, FG[i].TentRound);
    Inc(FG[i].PuntiChiusi, FG[i].PuntiUltimoRound);
    Inc(FG[i].TentChiusi, FG[i].TentRound);
    if FG[i].Risolto then
      Inc(FG[i].TempoChiusoMs, FG[i].TempoRisoltoMs)
    else
      Inc(FG[i].TempoChiusoMs, Adesso - FInizioRound);
    n := Length(FG[i].Storico);
    SetLength(FG[i].Storico, FRoundChiusi + 1);
    for k := n to FRoundChiusi - 1 do FillChar(FG[i].Storico[k], SizeOf(TRisultatoRound), 0);
    FG[i].Storico[FRoundChiusi].Tentativi := FG[i].TentRound;
    FG[i].Storico[FRoundChiusi].Vicinanza := FG[i].MigliorVic;
    FG[i].Storico[FRoundChiusi].Risolto := FG[i].Risolto;
    FG[i].Storico[FRoundChiusi].PosVelocita := FG[i].PosVelocita;
    FG[i].Storico[FRoundChiusi].Punti := FG[i].PuntiUltimoRound;
  end;
  Inc(FRoundChiusi);
  FMotivo := Motivo;
  FUltimoChiuso := FSegreto;
  if FRound >= NumCodici then
    FStato := sgFinita
  else
  begin
    FStato := sgPausa;
    FFinePausa := Adesso + Int64(PausaTraRoundSec) * 1000;
  end;
end;

procedure TGara.Tick(Adesso: Int64);
begin
  case FStato of
    sgRound:
      if Adesso - FInizioRound >= Int64(SecondiRound) * 1000 then
        ChiudiRound(mfTempo, Adesso)
      else if TuttiHannoRisolto(Adesso) then
        ChiudiRound(mfTutti, Adesso);
    sgPausa:
      if Adesso >= FFinePausa then IniziaRound(Adesso);
  end;
end;

procedure TGara.ProssimoCodice(Adesso: Int64);
begin
  if FStato = sgRound then ChiudiRound(mfDocente, Adesso);
  if FStato = sgPausa then IniziaRound(Adesso);
end;

procedure TGara.Ferma(Adesso: Int64);
begin
  if FStato = sgRound then ChiudiRound(mfDocente, Adesso);
  if FStato = sgPausa then FStato := sgFinita;
end;

function TGara.SecondiRimasti(Adesso: Int64): Integer;
var
  ms: Int64;
begin
  if FStato <> sgRound then
  begin
    Result := 0;
    Exit;
  end;
  ms := Int64(SecondiRound) * 1000 - (Adesso - FInizioRound);
  if ms < 0 then ms := 0;
  Result := Integer((ms + 999) div 1000);     // si arrotonda per eccesso: 0 solo a tempo scaduto
end;

function TGara.SecondiPausaRimasti(Adesso: Int64): Integer;
var
  ms: Int64;
begin
  if FStato <> sgPausa then
  begin
    Result := 0;
    Exit;
  end;
  ms := FFinePausa - Adesso;
  if ms < 0 then ms := 0;
  Result := Integer((ms + 999) div 1000);
end;

function TGara.PuntiRound(Idx: Integer): Integer;
begin
  if FStato = sgRound then
    Result := PunteggioRound(FG[Idx].MigliorVic, FG[Idx].Risolto, FG[Idx].PosVelocita, FG[Idx].TentRound)
  else
    Result := FG[Idx].PuntiUltimoRound;
end;

function TGara.Totale(Idx: Integer): Integer;
begin
  Result := FG[Idx].PuntiChiusi;
  if FStato = sgRound then Result := Result + PuntiRound(Idx);
end;

function TGara.TentativiTotali(Idx: Integer): Integer;
begin
  Result := FG[Idx].TentChiusi;
  if FStato = sgRound then Result := Result + FG[Idx].TentRound;
end;

function TGara.TempoTotaleMs(Idx: Integer): Int64;
begin
  Result := FG[Idx].TempoChiusoMs;
  if (FStato = sgRound) and FG[Idx].Risolto then Result := Result + FG[Idx].TempoRisoltoMs;
end;

{ True se A sta strettamente sopra B: piu' punti, poi meno tentativi, poi meno tempo }
function TGara.Meglio(A, B: Integer): Boolean;
var
  ta, tb: Integer;
  ma, mb: Int64;
begin
  if Totale(A) <> Totale(B) then
  begin
    Result := Totale(A) > Totale(B);
    Exit;
  end;
  ta := TentativiTotali(A);
  tb := TentativiTotali(B);
  if ta <> tb then
  begin
    Result := ta < tb;
    Exit;
  end;
  ma := TempoTotaleMs(A);
  mb := TempoTotaleMs(B);
  Result := ma < mb;
end;

function TGara.Ordine: TElencoIndici;
var
  i, k, t: Integer;
begin
  Result := nil;
  SetLength(Result, Length(FG));
  for i := 0 to High(FG) do Result[i] := i;
  for i := 1 to High(FG) do          // ordinamento a inserimento (a parita' completa: ordine alfabetico)
  begin
    t := Result[i];
    k := i - 1;
    while (k >= 0) and (Meglio(t, Result[k]) or
      (not Meglio(Result[k], t) and (LowerCase(FG[t].Nome) < LowerCase(FG[Result[k]].Nome)))) do
    begin
      Result[k + 1] := Result[k];
      Dec(k);
    end;
    Result[k + 1] := t;
  end;
end;

function TGara.Posizione(Idx: Integer): Integer;
var
  k: Integer;
begin
  Result := 1;
  for k := 0 to High(FG) do
    if (k <> Idx) and Meglio(k, Idx) then Inc(Result);
end;

end.
