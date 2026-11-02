#!/bin/bash
# Compila la VERA unit1.pas contro le finte unita' LCL e la prova con 22 client veri.
# Uso:  bash prova_finestra.sh [numero_client]      (serve fpc 3.2.x e python3)
AQUI="$(cd "$(dirname "$0")" && pwd)"; SUP="$AQUI/.."
OUT="${OUT:-/tmp/mm_out_finestra}"; rm -rf "$OUT"; mkdir -p "$OUT/o"
N="${1:-22}"; PORTA=$((5600 + RANDOM % 300))
sed 's/{\$R \*.lfm}//' "$SUP/unit1.pas" > "$AQUI/stub_lcl_server/Unit1.pas"
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
echo "== compilazione (fpc $(fpc -iV)), nessun thread: niente cthreads =="
fpc -Mobjfpc -Sh -vewn -FU"$OUT/o" -Fu"$AQUI/stub_lcl_server" $FCL -o"$OUT/test_finestra" "$AQUI/test_finestra.pas" 2>&1 | grep -iE "error|warning|fatal|Warn|Hint: .*Unit1|lines compiled" 
rm -f "$AQUI/stub_lcl_server/Unit1.pas"
[ -x "$OUT/test_finestra" ] || { echo "COMPILAZIONE FALLITA"; exit 1; }
echo "== prova con $N client sulla porta $PORTA =="
"$OUT/test_finestra" $PORTA "$OUT/fatto" "$OUT" > "$OUT/driver.log" 2>&1 &
PID=$!; sleep 1
python3 "$AQUI/prova_22.py" $PORTA $N "$OUT/fatto"
wait $PID
echo "== griglia vista dalla finestra =="; cat "$OUT/griglia.txt"
echo "== ultime righe del registro =="; tail -8 "$OUT/registro.txt"
echo "== righe di registro: $(wc -l < "$OUT/registro.txt"), vittorie registrate: $(grep -c 'HA VINTO' "$OUT/registro.txt")"
echo "== messaggi a video =="; cat "$OUT/messaggi.txt"
