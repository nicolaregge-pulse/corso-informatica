#!/bin/bash
# Regola 34 (REGISTRO-ERRORI #174): prima di accodare un post su Classroom si guarda se ne esiste gia' uno analogo
# nell'ULTIMO elenco classroom.compiti archiviato dal ponte, e quanti minuti ha quell'elenco.
# Uso: bash strumenti/prima_di_pubblicare.sh "Titolo del compito" [classe]     (dal repository pubblico)
# Il riservato si cerca in $RISERVATO oppure in ../corso-informatica-riservato. Esce 0 = via libera, 1 = esiste gia', 2 = elenco vecchio/assente.
TITOLO="$1"; CLASSE="${2:-}"
[ -z "$TITOLO" ] && { echo "Uso: prima_di_pubblicare.sh \"Titolo\" [classe]"; exit 3; }
RIS="${RISERVATO:-$(cd "$(dirname "$0")/../.." && pwd)/corso-informatica-riservato}"
[ -d "$RIS/comandi" ] || { echo "Riservato non trovato in $RIS: accoda prima classroom.compiti e aspetta."; exit 2; }
python3 - "$RIS" "$TITOLO" "$CLASSE" <<'PY'
import sys, os, json, glob, time, subprocess, re
ris, titolo, classe = sys.argv[1:4]
norm = lambda t: re.sub(r'\s+', ' ', (t or '').lower()).strip()
best = None
for f in glob.glob(ris + '/comandi/archivio/*.json') + glob.glob(ris + '/comandi/*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    for az, r in zip(d.get('azioni', []), d.get('risultati', [])):
        if az.get('tipo') != 'classroom.compiti' or not r.get('ok'): continue
        if classe and az.get('classe', '').lower() != classe.lower(): continue
        # ora dell'elenco = ora dell'ultimo commit del file (altrimenti data di modifica)
        o = subprocess.run(['git', '-C', ris, 'log', '-1', '--format=%ct', '--', f], capture_output=True, text=True).stdout.strip()
        t = int(o) if o else int(os.path.getmtime(f))
        if best is None or t > best[0]: best = (t, f, r.get('dati') or [], az.get('classe', ''))
if not best:
    print('Nessun elenco classroom.compiti trovato: accoda prima classroom.compiti e aspetta.'); sys.exit(2)
t, f, dati, cl = best
minuti = (time.time() - t) / 60
n = norm(titolo)
sim = [x for x in dati if norm(x.get('titolo')) == n or n in norm(x.get('titolo')) or norm(x.get('titolo')) in n]
print('Ultimo elenco: %s (classe %s), vecchio di %.0f minuti.' % (os.path.basename(f), cl, minuti))
if sim:
    for x in sim: print('ESISTE GIA\' un titolo analogo: %s [%s] id %s %s' % (x.get('titolo'), x.get('stato'), x.get('id'), x.get('link', '')))
    print('Non creare: modifica il post esistente (regola 34).')
else:
    print('Nessun titolo analogo in quell\'elenco.')
if minuti > 2:
    print('elenco vecchio: accoda prima classroom.compiti e aspetta'); sys.exit(2)
sys.exit(1 if sim else 0)
PY
