#!/bin/bash
# COMANDO UNICO di refresh del cruscotto (v1.0, 13/11/2026). Si lancia A RICHIESTA: non gira da solo.
# Perche' non e' automatico ogni 2 minuti: il foglio Fabbrica e' PRIVATO e nessun processo del repository puo' leggerlo;
# lo legge l'assistente (export xlsx dal connettore Drive, account PIAMARTA). Il foglio stesso e' aggiornato dal motore Fabbrica
# (Apps Script) a intervalli suoi: Moduli a ogni giro, Classroom ogni 2 minuti per la 2INF e ogni 10 per le altre classi.
#
# Uso (dalla cartella del repository pubblico):
#   bash strumenti/refresh_cruscotto.sh /percorso/FABBRICA.xlsx            # scrive i dati in docs/cruscotto/dati/
#   bash strumenti/refresh_cruscotto.sh /percorso/FABBRICA.xlsx --push     # in piu': git pull --rebase, commit dei soli dati, push
# Scrive anche: docs/cruscotto/dati/<CLASSE>-presenze.json (solo «Nome I.») e, nel RISERVATO, cruscotti/1INF-docente-AAAAMMGG-HHMM.html (con i cognomi).
# L'xlsx va tenuto FUORI dal repository. Ogni script ha il controllo privacy bloccante (R1): se un file non passa, non viene scritto.
set -u
X="${1:-}"
[ -f "$X" ] || { echo "Uso: bash strumenti/refresh_cruscotto.sh FABBRICA.xlsx [--push]"; exit 1; }
cd "$(dirname "$0")/.." || exit 1
ESITO=0
# l'ordine conta: il primo riscrive meta.json, gli altri vi aggiungono le loro voci
python3 -I strumenti/aggiorna_cruscotto_dati.py "$X" || ESITO=$?
python3 -I strumenti/aggiorna_sicurezza_dati.py "$X" || ESITO=$?
for C in strumenti/oggi-*-config.json; do
  [ -f "$C" ] || continue
  CL=$(basename "$C" | sed 's/^oggi-//; s/-config\.json$//')
  python3 -I strumenti/aggiorna_oggi_dati.py "$X" "$CL" || ESITO=$?
done
# presenze del giorno (solo «Nome I.», dal registro salvato nel riservato; se non c'e' un file, non fa niente)
python3 -I strumenti/aggiorna_presenze_dati.py || ESITO=$?
# versione DOCENTE con i cognomi: HTML autonomo scritto SOLO nel riservato (cruscotti/), mai nel pubblico
GEN="$(dirname "$PWD")/corso-informatica-riservato/generatori/cruscotto_docente.py"
if [ -f "$GEN" ]; then python3 -I "$GEN" 1INF || ESITO=$?; else echo "versione docente non generata: manca $GEN"; fi
echo "--- refresh finito (esito $ESITO, 0 = tutto scritto). Ora del dato: docs/cruscotto/dati/meta.json"
if [ "${2:-}" = "--push" ]; then
  [ "$ESITO" = "0" ] || [ "$ESITO" = "3" ] || { echo "NON faccio il push: errore vero in uno script (esito $ESITO)."; exit "$ESITO"; }
  [ "$ESITO" = "3" ] && echo "ATTENZIONE: esito 3 = un file NON e passato dal controllo privacy ed e stato saltato (non scritto): vedi sopra."
  git pull --rebase --autostash -q || { echo "git pull --rebase fallito"; exit 1; }
  RIS="$(dirname "$PWD")/corso-informatica-riservato"
  if [ -d "$RIS/cruscotti" ]; then   # versione docente: commit dei soli file di cruscotti/ nel riservato
    ( cd "$RIS" && git pull --rebase --autostash -q; git add cruscotti && { git diff --cached --quiet -- cruscotti || git commit -q -m "Cruscotto docente: versione aggiornata $(date +%H:%M)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -- cruscotti; git push -q; } ) || echo "ATTENZIONE: commit/push del riservato non riusciti"
  fi
  git add docs/cruscotto/dati
  git diff --cached --quiet && { echo "Nessuna differenza nei dati: niente commit."; exit 0; }
  git commit -q -m "Cruscotto: dati aggiornati $(date +%H:%M)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git push -q && echo "push fatto: poi bash strumenti/aspetta_pubblicazione.sh"
fi
exit "$ESITO"
