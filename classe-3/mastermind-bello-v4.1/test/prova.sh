#!/bin/bash
# Compila i VERI file UnitInterfaccia.pas, UnitServer.pas e UnitGara.pas contro finte unita' LCL (cartella stub_lcl) e li prova:
#  - UnitGara da sola (punteggi, parita', i 3 modi in cui finisce un round),
#  - UnitRete da sola (righe, parser, anche le righe nuove della gara v4.1),
#  - logica (neri/bianchi con colori ripetuti), partita da soli con controllo del disegno,
#  - rete in modalita' LIBERA (come la v4.0.1): N client contro il server (porta 5050), Stop e Via, codice mostrato,
#  - GARA di 3 codici: 6 client v4.1 + 2 client VECCHI (v4.0.1) contro il server, e verifica dei conti (porta 5051).
# Uso: bash prova.sh [numero_client]   (serve fpc 3.2.x e python3). NON compila con la vera LCL: serve Lazarus.
AQUI="$(cd "$(dirname "$0")" && pwd)"; OUT="${OUT:-/tmp/mm_out_bello_v41}"
cd /tmp
rm -rf "$OUT"; mkdir -p "$OUT/oc" "$OUT/os" "$OUT/ov" "$OUT/og" "$OUT/stub"; N="${1:-6}"; PORTA=5050; PORTA_GARA=5051
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
cp "$AQUI"/stub_lcl/*.pas "$OUT/stub/"
mkdir -p "$OUT/cl" "$OUT/sv" "$OUT/rt" "$OUT/vecchio"; cp -r "$AQUI/../Comune" "$OUT/Comune"
sed 's/{\$R \*.lfm}//' "$AQUI/../Client/UnitInterfaccia.pas" > "$OUT/cl/UnitInterfaccia.pas"
cp "$AQUI/../Client/UnitRete.pas" "$OUT/cl/UnitRete.pas"
# il client v4.0.1 (congelato), per provare che con il server v4.1 funziona ancora
sed 's/{\$R \*.lfm}//' "$AQUI/vecchio_v4.0.1/UnitInterfaccia.pas" > "$OUT/vecchio/UnitInterfaccia.pas"
cp "$AQUI/vecchio_v4.0.1/UnitRete.pas" "$OUT/vecchio/UnitRete.pas"
# la regola della v4.0: UnitRete non deve conoscere la finestra, UnitInterfaccia non deve toccare i socket
if sed -n '/^uses/,/;/p' "$AQUI/../Client/UnitRete.pas" | grep -qiE "Forms|Controls|Graphics|StdCtrls|ExtCtrls|Dialogs|UnitInterfaccia"; then echo "ERRORE: UnitRete conosce la finestra"; exit 1; fi
if grep -qiE "ssockets|TInetSocket" "$AQUI/../Client/UnitInterfaccia.pas"; then echo "ERRORE: UnitInterfaccia usa i socket"; exit 1; fi
# la regola della v4.1: UnitGara e' pura (solo calcoli): niente finestre, niente rete
if sed -n '/^uses/,/;/p' "$AQUI/../Server/UnitGara.pas" | grep -qiE "Forms|Controls|Graphics|StdCtrls|ExtCtrls|Dialogs|sockets|UnitServer|UnitRete"; then echo "ERRORE: UnitGara conosce finestre o rete"; exit 1; fi
echo "== regole: UnitRete senza finestre, UnitInterfaccia senza socket, UnitGara senza finestre ne' rete: ok =="
# i file delle icone non devono contenere immagini PNG (Lazarus non le legge)
for f in "$AQUI"/../Client/*.ico "$AQUI"/../Server/*.ico "$AQUI"/../Risorse/*.ico "$AQUI"/../Client/*.res "$AQUI"/../Server/*.res; do
  if grep -qaP '\x89PNG\r\n\x1a\n' "$f"; then echo "ERRORE: PNG dentro $f"; exit 1; fi
done
echo "== icone: nessun PNG dentro i file .ico e .res: ok =="
# UnitGara da sola (puro Pascal)
fpc -Mobjfpc -Sh -vewn -FU"$OUT/og" -Fu"$AQUI/../Server" -o"$OUT/test_gara" "$AQUI/test_gara.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_gara" ] || { echo COMPILAZIONE test_gara FALLITA; exit 1; }
"$OUT/test_gara" | grep -vE '^  ok ' || true
"$OUT/test_gara" > "$OUT/test_gara.log" || { echo "test_gara FALLITO"; exit 1; }
echo "   (UnitGara: $(grep -c '^  ok ' "$OUT/test_gara.log") controlli ok)"
# UnitRete da sola, SENZA le finte unita' LCL (prova che non ne ha bisogno)
fpc -Mobjfpc -Sh -vewn -FU"$OUT/rt" -Fu"$OUT/cl" $FCL -o"$OUT/test_rete" "$AQUI/test_rete.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_rete" ] || { echo COMPILAZIONE test_rete FALLITA; exit 1; }
"$OUT/test_rete" > "$OUT/test_rete.log" || { cat "$OUT/test_rete.log"; exit 1; }
grep -vE '^  ok ' "$OUT/test_rete.log"; echo "   (UnitRete: $(grep -c '^  ok ' "$OUT/test_rete.log") controlli ok)"
sed 's/{\$R \*.lfm}//' "$AQUI/../Server/UnitServer.pas" > "$OUT/sv/UnitServer.pas"
cp "$AQUI/../Server/UnitGara.pas" "$OUT/sv/UnitGara.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/oc" -Fu"$OUT/stub" -Fu"$OUT/cl" $FCL -o"$OUT/test_client" "$AQUI/test_client.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/os" -Fu"$OUT/stub" -Fu"$OUT/sv" $FCL -o"$OUT/test_server" "$AQUI/test_server.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
fpc -Mobjfpc -Sh -vewn -dVECCHIO -FU"$OUT/ov" -Fu"$OUT/stub" -Fu"$OUT/vecchio" $FCL -o"$OUT/test_client_vecchio" "$AQUI/test_client.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_client" ] && [ -x "$OUT/test_server" ] && [ -x "$OUT/test_client_vecchio" ] || { echo COMPILAZIONE FALLITA; exit 1; }
"$OUT/test_client" logica || exit 1
"$OUT/test_client" locale || exit 1
echo "== rete: server spento =="; "$OUT/test_client" spento 127.0.0.1 Prova
attendi() { for i in $(seq 1 60); do python3 -c "import socket,sys;sys.exit(socket.socket().connect_ex(('127.0.0.1',$1)))" 2>/dev/null && break; sleep 0.5; done; }

# ---------- 1. modalita' LIBERA, come la v4.0.1 ----------
"$OUT/test_server" $PORTA "$OUT/fatto" "$OUT" b > "$OUT/driver.log" 2>&1 &
SPID=$!
attendi $PORTA
echo "== rete (partita libera): $N client in parallelo contro il server =="
for i in $(seq 1 $N); do "$OUT/test_client" rete 127.0.0.1 "Alunno$i" > "$OUT/c$i.log" 2>&1 & done
wait $(jobs -p | grep -v $SPID) 2>/dev/null
sleep 0.5; touch "$OUT/fatto"; wait $SPID
echo "client arrivati alla vittoria: $(cat "$OUT"/c*.log | grep -c ' FINE ') su $N"
cat "$OUT"/c*.log | grep -i "ERRORE" | head -3
grep -h " FINE " "$OUT"/c1.log | head -1
echo "server: vittorie registrate: $(grep -c 'HA VINTO' "$OUT/registro.txt")"
head -3 "$OUT/griglia.txt"
# nella partita libera la risposta e' IDENTICA alla v4.0.1: una sola riga, niente righe della gara
if grep -q "ROUND\|CLASSIFICA" "$OUT/registro.txt"; then echo "ERRORE: righe della gara nella partita libera"; fi
mkdir -p "$OUT/libera"; mv "$OUT"/c*.log "$OUT"/griglia.txt "$OUT"/registro.txt "$OUT"/messaggi.txt "$OUT/libera/" 2>/dev/null; rm -f "$OUT/fatto"

# ---------- 2. la GARA: 3 codici, 6 client v4.1 (4 forti, 2 deboli) + 2 client v4.0.1 ----------
echo
echo "== GARA di 3 codici contro il server: 6 client v4.1 + 2 client VECCHI v4.0.1 =="
"$OUT/test_server" $PORTA_GARA "$OUT/fatto" "$OUT" b gara 4 > "$OUT/driver_gara.log" 2>&1 &
SPID=$!
attendi $PORTA_GARA
for i in 1 2 3 4; do "$OUT/test_client" gara 127.0.0.1:$PORTA_GARA "Nuovo$i" forte > "$OUT/n$i.log" 2>&1 & echo $! >> "$OUT/pidc"; done
for i in 5 6; do "$OUT/test_client" gara 127.0.0.1:$PORTA_GARA "Nuovo$i" debole > "$OUT/n$i.log" 2>&1 & echo $! >> "$OUT/pidc"; done
for i in 1 2; do "$OUT/test_client_vecchio" rete 127.0.0.1:$PORTA_GARA "Vecchio$i" > "$OUT/v$i.log" 2>&1 & echo $! >> "$OUT/pidc"; done
python3 -I "$AQUI/sonda_gara.py" $PORTA_GARA "$OUT" Nuovo1 Nuovo1 Nuovo2 Nuovo3 Nuovo4 Nuovo5 Nuovo6 Vecchio1 Vecchio2 > "$OUT/sonda.log" 2>&1 &
SONDA=$!
for p in $(cat "$OUT/pidc"); do wait $p 2>/dev/null; done
touch "$OUT/sonda_stop"; wait $SONDA
sleep 0.3; touch "$OUT/fatto"; wait $SPID
cat "$OUT"/n*.log | grep -E "ERRORE|FINE|RIS" | head -60
cat "$OUT"/v*.log | grep -E "ERRORE| FINE " | head -4
cat "$OUT/driver_gara.log" | grep -iE "ERRORE" | head
echo "-- classifica generale del server (come nella finestra) --"; head -12 "$OUT/griglia.txt"
echo "-- verifica dei conti --"
python3 -I "$AQUI/verifica_gara.py" "$OUT" 6 2
