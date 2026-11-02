#!/usr/bin/env python3
"""Sblocca un'ora per volta nelle pagine di lezione (ore_sbloccate in config.json).
Uso:  python3 strumenti/sblocca_ora.py 3inf 2      (3inf, 2inf, 3inf-client o 2inf-dhcp o 2inf-sicurezza; ora 1, 2 o 3; per 3inf-client, 2inf-dhcp e 2inf-sicurezza basta 1 = pagina aperta, 0 = chiusa)
Cambia SOLO il numero, fa commit + pull --rebase + push (mai force). Poi: bash strumenti/aspetta_pubblicazione.sh
Le pagine aperte dei ragazzi si accorgono dello sblocco da sole entro ~45 secondi (dopo la pubblicazione del sito)."""
import json, subprocess, sys, pathlib
CART = {'3inf': 'docs/anteprima/3inf-mastermind-02-11', '2inf': 'docs/anteprima/2inf-reti-02-11',
        '3inf-client': 'docs/anteprima/3inf-client-lazarus-02-11',
        '2inf-dhcp': 'docs/anteprima/2inf-dhcp-dns-02-11',
        '2inf-sicurezza': 'docs/anteprima/2inf-sicurezza-02-11',
        '2inf-oggi': 'docs/anteprima/2inf-03-11',
        '2inf-phishing': 'docs/anteprima/2inf-phishing-v2',
        '4ti': 'docs/anteprima/4ti-ipv4-03-11',
        '1inf-deepfake': 'docs/anteprima/1inf-deepfake-03-11'}
if len(sys.argv) != 3 or sys.argv[1] not in CART or sys.argv[2] not in ('0', '1', '2', '3'):
    sys.exit(__doc__)
radice = pathlib.Path(__file__).resolve().parent.parent
f = radice / CART[sys.argv[1]] / 'config.json'
c = json.loads(f.read_text()); c['ore_sbloccate'] = int(sys.argv[2])
f.write_text(json.dumps(c, ensure_ascii=False, indent=1))
def g(*a): subprocess.run(['git', '-C', str(radice), *a], check=True)
g('add', str(f)); g('commit', '-m', 'Sblocca ora %s (%s)' % (sys.argv[2], sys.argv[1]))
g('pull', '--rebase'); g('push')
print('FATTO: %s ora %s sbloccata. Ora: bash strumenti/aspetta_pubblicazione.sh' % (sys.argv[1], sys.argv[2]))
