#!/usr/bin/env python3
"""Scrive l'IP del server del Mastermind in rete nella pagina dei ragazzi (3inf-client-lazarus-02-11/config.json).
Uso:  python3 strumenti/imposta_ip_server.py 192.168.10.5     (solo l'IP, senza porta: la pagina aggiunge :5050)
      python3 strumenti/imposta_ip_server.py ""                (svuota)
Fa commit + pull --rebase + push (mai force). Poi: bash strumenti/aspetta_pubblicazione.sh
Le pagine aperte dei ragazzi si aggiornano da sole entro ~30 secondi dalla pubblicazione."""
import json, re, subprocess, sys, pathlib
if len(sys.argv) != 2 or not re.fullmatch(r'|\d{1,3}(\.\d{1,3}){3}', sys.argv[1].strip()):
    sys.exit(__doc__)
radice = pathlib.Path(__file__).resolve().parent.parent
f = radice / 'docs/anteprima/3inf-client-lazarus-02-11/config.json'
c = json.loads(f.read_text()); c['server_ip'] = sys.argv[1].strip()
f.write_text(json.dumps(c, ensure_ascii=False, indent=1))
def g(*a): subprocess.run(['git', '-C', str(radice), *a], check=True)
g('add', str(f)); g('commit', '-m', 'IP del server Mastermind: %s' % (sys.argv[1] or 'vuoto'))
g('pull', '--rebase'); g('push')
print('FATTO. Ora: bash strumenti/aspetta_pubblicazione.sh')
