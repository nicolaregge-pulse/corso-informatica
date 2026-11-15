#!/bin/bash
# COMANDO UNICO di refresh del cruscotto (v1.3, 15/11/2026: + cruscotto docente cifrato docs/docente; v1.2, 15/11/2026: nel pubblico niente numeri per allievo, controllo privacy_pubblico.py, numeri nel riservato dati/cruscotto-pieno/; v1.1, 15/11/2026: + cruscotto completo; v1.0, 13/11/2026). Si lancia A RICHIESTA: non gira da solo.
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
# CRUSCOTTO COMPLETO (v1.0, 15/11/2026): registro, presenza, compiti, quiz, voti, note, Veyon, Sicurezza, Git, recuperi, per le 4 classi.
# Scrive nel RISERVATO cruscotti/<CLASSE>-completo-docente-*.html (cognomi, voti, note) e nel pubblico docs/cruscotto/completo/<CLASSE>.html (solo «Nome I.», niente voti/note/Veyon).
GEN2="$(dirname "$PWD")/corso-informatica-riservato/generatori/cruscotto_completo.py"
if [ -f "$GEN2" ]; then python3 -I "$GEN2" "$X" || ESITO=$?; else echo "cruscotto completo non generato: manca $GEN2"; fi
# CRUSCOTTO DOCENTE TOTALE (v1.0-1.1, 15/11/2026): Fotografia di classe + scheda allievo, 4 classi. Il generatore sta nel RISERVATO e scrive SOLO li (cruscotti/DOCENTE-TUTTE-LE-CLASSI-*.html).
GEN3="$(dirname "$PWD")/corso-informatica-riservato/generatori/cruscotto_docente_totale.py"
if [ -f "$GEN3" ]; then python3 -I "$GEN3" "$X" || ESITO=$?; else echo "cruscotto docente totale non generato: manca $GEN3"; fi
# CRUSCOTTO DOCENTE PUBBLICO CIFRATO (v1.0, 15/11/2026): il generatore sta nel RISERVATO, prende il file DOCENTE-TUTTE-LE-CLASSI-*.html piu' recente,
# lo cifra (AES-GCM, parola d'ordine solo nel riservato) e scrive nel pubblico SOLO docs/docente/index.html (blob cifrato, nessun dato in chiaro).
GEN4="$(dirname "$PWD")/corso-informatica-riservato/generatori/cruscotto_docente_pubblico_cifrato.py"
if [ -f "$GEN4" ]; then python3 -I "$GEN4" >/dev/null || ESITO=$?; else echo "cruscotto docente cifrato non generato: manca $GEN4"; fi
# CONTROLLO BLOCCANTE (15/11/2026, R1): nessun numero per allievo (percentuali, punti, voti) nei file pubblici del cruscotto
python3 -I strumenti/privacy_pubblico.py || { echo "STOP: numeri per allievo nei file pubblici: NON faccio il push."; exit 1; }
echo "--- refresh finito (esito $ESITO, 0 = tutto scritto). Ora del dato: docs/cruscotto/dati/meta.json"
if [ "${2:-}" = "--push" ]; then
  [ "$ESITO" = "0" ] || [ "$ESITO" = "3" ] || { echo "NON faccio il push: errore vero in uno script (esito $ESITO)."; exit "$ESITO"; }
  [ "$ESITO" = "3" ] && echo "ATTENZIONE: esito 3 = un file NON e passato dal controllo privacy ed e stato saltato (non scritto): vedi sopra."
  git pull --rebase --autostash -q || { echo "git pull --rebase fallito"; exit 1; }
  RIS="$(dirname "$PWD")/corso-informatica-riservato"
  if [ -d "$RIS/cruscotti" ]; then   # versione docente: commit dei soli file di cruscotti/ nel riservato
    ( cd "$RIS" && git pull --rebase --autostash -q; git add cruscotti && { git diff --cached --quiet -- cruscotti || git commit -q -m "Cruscotto docente: versione aggiornata $(date +%H:%M)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" -- cruscotti; git push -q; } ) || echo "ATTENZIONE: commit/push del riservato non riusciti"
  fi
  git add docs/cruscotto/dati docs/cruscotto/completo docs/cruscotto/index.html docs/docente/index.html
  git diff --cached --quiet && { echo "Nessuna differenza nei dati: niente commit."; exit 0; }
  git commit -q -m "Cruscotto: dati aggiornati $(date +%H:%M)" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" && git push -q && echo "push fatto: poi bash strumenti/aspetta_pubblicazione.sh"
fi
exit "$ESITO"
