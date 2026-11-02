#!/bin/bash
# Compila i VERI file UnitClient.pas e UnitServer.pas contro finte unita' LCL (cartella stub_lcl) e li prova:
#  - logica (neri/bianchi con colori ripetuti), partita da soli con controllo del disegno,
#  - rete: N client contro il server (porta 5050), Stop e Via, codice mostrato come pioli.
# Uso: bash prova.sh [numero_client]   (serve fpc 3.2.x). NON compila con la vera LCL: serve Lazarus.
AQUI="$(cd "$(dirname "$0")" && pwd)"; OUT="${OUT:-/tmp/mm_out_bello_nuovo}"
cd /tmp
rm -rf "$OUT"; mkdir -p "$OUT/oc" "$OUT/os" "$OUT/stub"; N="${1:-6}"; PORTA=5050
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
cp "$AQUI"/stub_lcl/*.pas "$OUT/stub/"
mkdir -p "$OUT/cl" "$OUT/sv"; cp -r "$AQUI/../Comune" "$OUT/Comune"
sed 's/{\$R \*.lfm}//' "$AQUI/../Client/UnitClient.pas" > "$OUT/cl/UnitClient.pas"
sed 's/{\$R \*.lfm}//' "$AQUI/../Server/UnitServer.pas" > "$OUT/sv/UnitServer.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/oc" -Fu"$OUT/stub" -Fu"$OUT/cl" $FCL -o"$OUT/test_client" "$AQUI/test_client.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/os" -Fu"$OUT/stub" -Fu"$OUT/sv" $FCL -o"$OUT/test_server" "$AQUI/test_server.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_client" ] && [ -x "$OUT/test_server" ] || { echo COMPILAZIONE FALLITA; exit 1; }
"$OUT/test_client" logica || exit 1
"$OUT/test_client" locale || exit 1
echo "== rete: server spento =="; "$OUT/test_client" spento 127.0.0.1 Prova
"$OUT/test_server" $PORTA "$OUT/fatto" "$OUT" b > "$OUT/driver.log" 2>&1 &
SPID=$!
for i in $(seq 1 60); do python3 -c "import socket,sys;sys.exit(socket.socket().connect_ex(('127.0.0.1',$PORTA)))" 2>/dev/null && break; sleep 0.5; done
echo "== rete: $N client in parallelo contro il server =="
for i in $(seq 1 $N); do "$OUT/test_client" rete 127.0.0.1 "Alunno$i" > "$OUT/c$i.log" 2>&1 & done
wait $(jobs -p | grep -v $SPID) 2>/dev/null
sleep 0.5; touch "$OUT/fatto"; wait $SPID
echo "client arrivati alla vittoria: $(cat "$OUT"/c*.log | grep -c ' FINE ') su $N"
cat "$OUT"/c*.log | grep -i "ERRORE" | head -3
grep -h " FINE " "$OUT"/c1.log | head -1
echo "server: vittorie registrate: $(grep -c 'HA VINTO' "$OUT/registro.txt")"
head -3 "$OUT/griglia.txt"
