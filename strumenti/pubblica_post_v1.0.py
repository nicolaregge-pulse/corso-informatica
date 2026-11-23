#!/usr/bin/env python3
"""PUBB n: aggiunge UNA richiesta a fabbrica/post/coda.json (prototipo v1.0, 23/11/2026, NON attivato: il motore non la legge ancora).
Uso:  python3 strumenti/pubblica_post_v1.0.py PUBB 2 --classe 2INF [--giorno AAAA-MM-GG] [--bozza] [--prova] [--push]
- trova fabbrica/post/<giorno>_<CLASSE>_ora<n>.json, lo controlla con la stessa funzione del motore (node, valida_post_v1.0.js);
- senza --push NON scrive nulla (mostra cosa farebbe); con --push: commit, git pull --rebase, git push (mai force);
- una ora per volta: la richiesta porta SOLO n e il post di quell'ora; --bozza prepara la bozza (invisibile ai ragazzi) senza pubblicare;
- --prova usa il corso di prova (proprieta PB_CORSO_PROVA del motore) invece del corso vero.
R2 di CLAUDE.md: questo comando si lancia solo dopo «PUBB n» scritto dal docente in chat."""
import argparse, datetime, json, pathlib, subprocess, sys
from zoneinfo import ZoneInfo

RAD = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument('pubb_kw'); ap.add_argument('n', type=int)
ap.add_argument('--classe', required=True, choices=['1INF', '2INF', '3INF', '4TI'])
ap.add_argument('--giorno'); ap.add_argument('--bozza', action='store_true'); ap.add_argument('--prova', action='store_true'); ap.add_argument('--push', action='store_true')
a = ap.parse_args()
if a.pubb_kw != 'PUBB' or not 1 <= a.n <= 6: sys.exit('Uso: PUBB n (n da 1 a 6)')
adesso = datetime.datetime.now(ZoneInfo('Europe/Rome'))
giorno = a.giorno or adesso.strftime('%Y-%m-%d')
pid = '%s_%s_ora%d' % (giorno, a.classe, a.n)
f = RAD / 'fabbrica' / 'post' / (pid + '.json')
if not f.exists(): sys.exit('NON riuscito: manca %s (la specifica del post di quell\'ora)' % f.relative_to(RAD))
azione = 'bozza' if a.bozza else 'pubblica'
r = subprocess.run(['node', str(RAD / 'fabbrica' / 'valida_post_v1.0.js'), str(f), azione, str(a.n)], capture_output=True, text=True)
v = json.loads(r.stdout or '{"err":["controllo non eseguito"],"avv":[]}')
if v['err']: sys.exit('NON riuscito: la specifica non passa i controlli: ' + '; '.join(v['err']))
cf = RAD / 'fabbrica' / 'post' / 'coda.json'
coda = json.loads(cf.read_text()) if cf.exists() else {'attivo': True, 'richieste': []}
limite = (adesso - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
coda['richieste'] = [x for x in coda['richieste'] if x.get('giorno', '9') >= limite]
rich = {'post': pid, 'azione': azione, 'giorno': giorno, 'richiesta': adesso.strftime('%Y-%m-%dT%H:%M:%S')}
if azione == 'pubblica': rich['pubb'] = a.n
if a.prova: rich['prova'] = True
coda['richieste'].append(rich)
testo = json.dumps(coda, ensure_ascii=False, indent=1) + '\n'
print('Richiesta:', json.dumps(rich, ensure_ascii=False)); 
if v['avv']: print('Avvisi (non bloccano):', '; '.join(v['avv']))
if not a.push: print('(prova a vuoto: niente scritto; aggiungi --push)'); sys.exit(0)
cf.write_text(testo)
def g(*c): return subprocess.run(['git', '-C', str(RAD)] + list(c), capture_output=True, text=True)
g('add', str(cf)); g('commit', '-m', 'PUBB %d %s %s' % (a.n, a.classe, giorno))
for i in range(3):
    g('pull', '--rebase'); p = g('push')
    if p.returncode == 0: print('Push fatto. Il motore la legge entro circa 1 minuto (+ cache di GitHub: stima 1-3 minuti).'); sys.exit(0)
sys.exit('NON riuscito: push non riuscito: ' + p.stderr[-200:])
