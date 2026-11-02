#!/bin/bash
# Prova di rete su localhost: avvia il VERO server e lancia i client simulati.
# Uso:  bash prova_tcp.sh   (serve fpc; i sorgenti di ssockets sono in /usr/share/fpcsrc se non installati)
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
OUT="${OUT:-/tmp/mm_out}"; mkdir -p "$OUT"
FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
fpc -Mobjfpc -Sh -FU"$OUT" -Fu"$AQUI/.." $FCL -o"$OUT/server_mastermind" "$AQUI/../server_mastermind.pas" >/dev/null 2>&1 || { echo "compilazione server fallita"; exit 2; }
fpc -Mobjfpc -Sh -FU"$OUT" -Fu"$AQUI/.." $FCL -o"$OUT/test_tcp" "$AQUI/test_tcp.pas" >/dev/null 2>&1 || { echo "compilazione test fallita"; exit 2; }
rm -rf "$OUT/cartA" "$OUT/cartB"; mkdir -p "$OUT/cartA" "$OUT/cartB"
printf '127.0.0.1;Mario Rossi\n' > "$OUT/ip-nomi-B.txt"
"$OUT/server_mastermind" --porta=5077 --cartella="$OUT/cartA" --seme=424242 --senza-tasti --durata=40 --ipnomi=/nonesiste > "$OUT/serverA.log" 2>&1 &
PA=$!
"$OUT/server_mastermind" --porta=5078 --cartella="$OUT/cartB" --seme=777 --senza-tasti --durata=25 --ipnomi="$OUT/ip-nomi-B.txt" > "$OUT/serverB.log" 2>&1 &
PB=$!
sleep 1
echo "######## PROVE A: server senza ip-nomi.txt (porta 5077)"
"$OUT/test_tcp" A 5077 "$OUT/cartA" 424242; RA=$?
echo "######## PROVE B: server con ip-nomi.txt (porta 5078)"
"$OUT/test_tcp" B 5078 "$OUT/cartB" 777; RB=$?
printf 'FINE\n' > "$OUT/cartA/comando.txt"; printf 'FINE\n' > "$OUT/cartB/comando.txt"
sleep 1; kill $PA $PB 2>/dev/null
echo; echo "Ultime righe della console del server A:"; tail -14 "$OUT/serverA.log"
exit $((RA+RB))
