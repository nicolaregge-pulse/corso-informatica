#!/bin/bash
# Compila il VERO unit1.pas del modello contro finte unita' LCL e lo prova (serve fpc 3.2.x).
# NON e' la vera Lazarus: la prova vera (apri il .lpi, Salva progetto con nome, F9) va fatta su un PC di aula.
AQUI="$(cd "$(dirname "$0")" && pwd)"; STUB="$AQUI/../../../classe-3/mastermind-3-bello/test/stub_lcl"; OUT="${OUT:-/tmp/modello_out}"
rm -rf "$OUT"; mkdir -p "$OUT/oc" "$OUT/stub"; cp "$STUB"/*.pas "$OUT/stub/"
sed 's/{\$R \*.lfm}//' "$AQUI/../ModelloLazarus/unit1.pas" > "$OUT/stub/Unit1.pas"
fpc -Mobjfpc -Sh -vewn -FU"$OUT/oc" -Fu"$OUT/stub" -o"$OUT/test_modello" "$AQUI/test_modello.pas" 2>&1 | grep -iE "error|warning|fatal|lines compiled"
[ -x "$OUT/test_modello" ] || { echo COMPILAZIONE FALLITA; exit 1; }
"$OUT/test_modello"
