#!/bin/bash
# Lancia TUTTE le prove e scrive risultati-test.txt. Serve fpc (3.2.x). Uso:  bash prova_tutto.sh
AQUI="$(cd "$(dirname "$0")" && pwd)"
OUT="${OUT:-/tmp/mm_out}"; mkdir -p "$OUT/stub"
# se ssockets non e' installato come unita' compilata, si usa il sorgente di FPC
FCL=""; [ -d /usr/share/fpcsrc/3.2.2/packages/fcl-net/src ] && FCL="-Fu/usr/share/fpcsrc/3.2.2/packages/fcl-net/src -Fu/usr/share/fpcsrc/3.2.2/packages/fcl-base/src"
RIS="$AQUI/risultati-test.txt"; : > "$RIS"
{
echo "MASTERMIND 2.0 - risultati delle prove ($(date '+%d/%m/%Y %H:%M')) - fpc $(fpc -iV)"
echo
echo "##### 1. LOGICA PURA (test_logica)"
fpc -Mobjfpc -Sh -FU"$OUT" -Fu"$AQUI/.." -o"$OUT/test_logica" "$AQUI/test_logica.pas" >/dev/null 2>&1 && "$OUT/test_logica"; R1=$?
echo
echo "##### 2. TRASPORTO FILE (test_file): server + 5 client sulla stessa cartella"
fpc -Mobjfpc -Sh -FU"$OUT" -Fu"$AQUI/.." $FCL -o"$OUT/test_file" "$AQUI/test_file.pas" >/dev/null 2>&1
rm -rf "$OUT/provafile"; mkdir -p "$OUT/provafile"; "$OUT/test_file" "$OUT/provafile"; R2=$?
echo
echo "##### 3. RETE TCP su localhost (server_mastermind vero + client simulati)"
OUT="$OUT" bash "$AQUI/prova_tcp.sh" | grep -v "^Ultime righe" | sed '/^------/,$d'; R3=${PIPESTATUS[0]}
echo
echo "##### 4. CONTROLLO DI COMPILAZIONE della scheda dello studente (unit1_client.pas) contro finte unita' LCL"
sed 's/{\$R \*.lfm}//' "$AQUI/../unit1_client.pas" > "$AQUI/stub_lcl/Unit1.pas"
fpc -Mobjfpc -Sh -FU"$OUT/stub" -Fu"$AQUI/stub_lcl" -Fu"$AQUI/.." $FCL "$AQUI/stub_lcl/Unit1.pas" >/dev/null 2>&1 && echo "  OK   unit1_client.pas compila (sintassi e tipi; NON e' una prova con la vera LCL)" || { echo "  FAIL compilazione"; R4=1; }
[ -z "$R4" ] && R4=0
rm -f "$AQUI/stub_lcl/Unit1.pas"
echo
[ "$R1$R2$R3$R4" = "0000" ] && echo "TUTTO OK" || echo "QUALCOSA E' FALLITO"
} 2>&1 | tee "$RIS"
