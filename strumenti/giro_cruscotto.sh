#!/bin/bash
# giro_cruscotto.sh v1.0 (19/11/2026) - rigenera i cruscotti delle 4 classi e committa SOLO se i dati sono cambiati.
# NON e' un trigger e non parte da solo: si lancia a mano o da un giro esterno ogni 2 minuti (vedi CRUSCOTTO-DAL-VIVO.md, cap. 06).
# Legge l'export Fabbrica PIU' RECENTE in storico/fabbrica-export/ del riservato: i dati nuovi arrivano solo quando c'e' un export
# nuovo (il foglio Fabbrica e' privato e lo scarica l'assistente con il connettore Drive; vedi strumenti/leggi_fabbrica.sh --nuovo).
# Uso:   bash strumenti/giro_cruscotto.sh [--no-push] [CLASSE ...]     (senza classi: tutte e quattro)
# Esito: 0 = fatto (anche «niente da committare»); 1 = generatore o controllo privacy fermo (R1): non si committa niente.
set -u
PUB="$(cd "$(dirname "$0")/.." && pwd)"
RIS="$(dirname "$PUB")/corso-informatica-riservato"
PUSH=1
[ "${1:-}" = "--no-push" ] && { PUSH=0; shift; }
CLASSI=("$@"); [ ${#CLASSI[@]} -eq 0 ] && CLASSI=(1INF 2INF 3INF 4TI)
GEN="$RIS/generatori/cruscotto_classe_v1_0.py"
[ -f "$GEN" ] || { echo "manca $GEN"; exit 1; }
git -C "$PUB" pull --rebase --autostash -q || { echo "pull del pubblico non riuscito"; exit 1; }
git -C "$RIS" pull --rebase --autostash -q || { echo "pull del riservato non riuscito"; exit 1; }
for C in "${CLASSI[@]}"; do
  python3 -I "$GEN" "$C" || { echo "FERMO su $C: nessun commit"; exit 1; }
done
ORA=$(python3 -I - "$PUB" <<'PY'
import json,sys
d=json.load(open(sys.argv[1]+"/docs/2inf/dati-cruscotto.json"))
print(d["dato"]["ora"][:5]+" del "+d["dato"]["giorno_it"])
PY
)
# pubblico: solo i file dei cruscotti (index.html e dati-cruscotto.json), mai altro
PERCORSI=(); for C in "${CLASSI[@]}"; do c=$(echo "$C" | tr 'A-Z' 'a-z'); PERCORSI+=("docs/$c/index.html" "docs/$c/dati-cruscotto.json"); done
git -C "$PUB" add -- "${PERCORSI[@]}" 2>/dev/null
if git -C "$PUB" diff --cached --quiet -- "${PERCORSI[@]}"; then
  echo "Pubblico: dati invariati, niente da committare."
else
  git -C "$PUB" commit -q -m "Cruscotti delle classi: dati delle $ORA (giro automatico)" -- "${PERCORSI[@]}" && echo "Pubblico: commit fatto."
  [ $PUSH -eq 1 ] && { git -C "$PUB" push -q && echo "Pubblico: push fatto." || echo "Pubblico: push NON riuscito (riprova dopo 5 secondi)."; }
fi
# riservato: versioni docente e fotografie dei dati
git -C "$RIS" add -- cruscotti storico/cruscotti 2>/dev/null
if git -C "$RIS" diff --cached --quiet -- cruscotti storico/cruscotti; then
  echo "Riservato: invariato."
else
  git -C "$RIS" commit -q -m "Cruscotti docente: dati delle $ORA" -- cruscotti storico/cruscotti && echo "Riservato: commit fatto."
  [ $PUSH -eq 1 ] && { git -C "$RIS" push -q && echo "Riservato: push fatto." || echo "Riservato: push NON riuscito (riprova dopo 5 secondi)."; }
fi
exit 0
