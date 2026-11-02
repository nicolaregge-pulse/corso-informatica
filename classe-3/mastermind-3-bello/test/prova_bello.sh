#!/bin/bash
# Compila il VERO unit1.pas del client bello contro finte unita' LCL e lo prova:
#  - logica (neri/bianchi con colori ripetuti), partita da soli con controllo del disegno,
#  - rete: N client contro il server-unico della cartella mastermind-2 (porta 5050).
# Uso: bash prova_bello.sh [numero_client]   (serve fpc 3.2.x; NON compila con la vera LCL: serve Lazarus)
AQUI="$(cd "$(dirname "$0")" && pwd)"; SRV="$AQUI/../../mastermind-2/server-unico/test"; OUT="${OUT:-/tmp/mm_out_bello}"
cd /tmp   # importante: da qui fpc non trova per sbaglio un altro unit1.pas nella cartella corrente
rm -rf "$OUT"; mkdir -p "$OUT/oc" "$OUT/os"; N="${1:-6}"; PORTA=5050
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
mkdir -p "$OUT/stubc"; cp "$AQUI"/stub_lcl/*.pas "$OUT/stubc/"; sed 's/{\$R \*.lfm}//' "$AQUI/../unit1.pas" > "$OUT/stubc/Unit1.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/oc" -Fu"$OUT/stubc" $FCL -o"$OUT/test_bello" "$AQUI/test_bello.pas" 2>&1 | grep -iE "error|warning|fatal|Warn|lines compiled"
mkdir -p "$OUT/stubs"; cp "$SRV"/stub_lcl_server/*.pas "$OUT/stubs/"; sed 's/{\$R \*.lfm}//' "$AQUI/../../mastermind-2/server-unico/unit1.pas" > "$OUT/stubs/Unit1.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/os" -Fu"$OUT/stubs" $FCL -o"$OUT/test_finestra" "$SRV/test_finestra.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_bello" ] && [ -x "$OUT/test_finestra" ] || { echo COMPILAZIONE FALLITA; exit 1; }
"$OUT/test_bello" logica || exit 1
"$OUT/test_bello" locale || exit 1
echo "== rete: server spento =="; "$OUT/test_bello" spento 127.0.0.1 Prova
"$OUT/test_finestra" $PORTA "$OUT/fatto" "$OUT" b > "$OUT/driver.log" 2>&1 &
SPID=$!
for i in $(seq 1 60); do python3 -c "import socket,sys;sys.exit(socket.socket().connect_ex(('127.0.0.1',$PORTA)))" 2>/dev/null && break; sleep 0.5; done
echo "== rete: $N client in parallelo contro il server =="
for i in $(seq 1 $N); do "$OUT/test_bello" rete 127.0.0.1 "Alunno$i" > "$OUT/c$i.log" 2>&1 & done
wait $(jobs -p | grep -v $SPID) 2>/dev/null
sleep 0.5; touch "$OUT/fatto"; wait $SPID
echo "client arrivati alla vittoria: $(cat "$OUT"/c*.log | grep -c ' FINE ') su $N"
cat "$OUT"/c*.log | grep -i "ERRORE" | head -3
grep -h " FINE " "$OUT"/c1.log | head -1
echo "server: vittorie registrate: $(grep -c 'HA VINTO' "$OUT/registro.txt")"
