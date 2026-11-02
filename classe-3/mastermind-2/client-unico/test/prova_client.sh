#!/bin/bash
# Compila il VERO unit1.pas del client contro finte unita' LCL e lo prova contro il server-unico (finto form + 22 client).
# Uso: bash prova_client.sh [numero_client]   (serve fpc 3.2.x)
AQUI="$(cd "$(dirname "$0")" && pwd)"; SRV="$AQUI/../../server-unico/test"; OUT="${OUT:-/tmp/mm_out_client}"
rm -rf "$OUT"; mkdir -p "$OUT/oc" "$OUT/os"; N="${1:-22}"; PORTA=5050
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
# client
mkdir -p "$OUT/stubc"; cp "$AQUI"/stub_lcl_client/*.pas "$OUT/stubc/"; sed 's/{\$R \*.lfm}//' "$AQUI/../unit1.pas" > "$OUT/stubc/Unit1.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/oc" -Fu"$OUT/stubc" $FCL -o"$OUT/test_client" "$AQUI/test_client.pas" 2>&1 | grep -iE "error|warning|fatal|Warn|lines compiled"
# server (driver del server-unico)
mkdir -p "$OUT/stubs"; cp "$SRV"/stub_lcl_server/*.pas "$OUT/stubs/"; sed 's/{\$R \*.lfm}//' "$AQUI/../../server-unico/unit1.pas" > "$OUT/stubs/Unit1.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/os" -Fu"$OUT/stubs" $FCL -o"$OUT/test_finestra" "$SRV/test_finestra.pas" 2>&1 | grep -iE "error|fatal|lines compiled"
[ -x "$OUT/test_client" ] && [ -x "$OUT/test_finestra" ] || { echo COMPILAZIONE FALLITA; exit 1; }
echo "== server spento =="; "$OUT/test_client" 127.0.0.1 Prova spento
echo "== IP sbagliato (non raggiungibile) =="; "$OUT/test_client" 10.255.255.1 Prova spento
echo "== IP scritto male =="; "$OUT/test_client" 192.168.x.y Prova spento
"$OUT/test_finestra" $PORTA "$OUT/fatto" "$OUT" b > "$OUT/driver.log" 2>&1 &
SPID=$!; sleep 1
echo "== prima del Via =="; "$OUT/test_client" 127.0.0.1 Wait1 wait; "$OUT/test_client" 127.0.0.1 Err1 errori
echo "== $N client in parallelo =="
for i in $(seq 1 $N); do "$OUT/test_client" 127.0.0.1 "Alunno$i" gioca > "$OUT/c$i.log" 2>&1 & done
wait $(jobs -p | grep -v $SPID) 2>/dev/null
sleep 0.5; touch "$OUT/fatto"; wait $SPID
cat "$OUT"/c*.log | grep -c " FINE " | sed 's/^/client arrivati alla vittoria: /'
cat "$OUT"/c*.log | grep -i "ERRORE" | head
grep -h " FINE " "$OUT"/c1.log "$OUT"/c2.log; grep -h "connetti" "$OUT"/c1.log
echo "== server: vittorie registrate: $(grep -c 'HA VINTO' "$OUT/registro.txt")"; head -8 "$OUT/griglia.txt"
