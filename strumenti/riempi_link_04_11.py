#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mette i link dei Moduli di mercoledì 04/11 (creati dal ponte) al posto dei segnaposto __QUIZ1__/2/3 nelle pagine e nei compiti in coda.
import glob, json, os, sys
R = '/home/user/corso-informatica-riservato/'
P = '/home/user/corso-informatica/docs/anteprima/'
MAPPA = {'__QUIZ1__': '1inf-lab-0411-testo-numero', '__QUIZ2__': '2inf-sicurezza-6ora', '__QUIZ3__': '3inf-mastermind-rete'}
link = {}
for tok, k in MAPPA.items():
    f = R + 'comandi/2026-11-04_MODULO-%s-quiz.json' % k
    if not os.path.exists(f): f = R + 'comandi/archivio/2026-11-04_MODULO-%s-quiz.json' % k
    try:
        d = json.load(open(f, encoding='utf-8'))
        link[tok] = d['risultati'][0]['dati'][0]['compila'] if d.get('risultati') and d['risultati'][0].get('ok') else None
    except Exception:
        link[tok] = None
print({k: bool(v) for k, v in link.items()})
n = 0
for f in glob.glob(P + '*-04-11/*.html') + glob.glob(R + 'coda/2026-11-04_*.json'):
    t = open(f, encoding='utf-8').read(); t2 = t
    for tok, v in link.items():
        if v: t2 = t2.replace(tok, v)
    if t2 != t: open(f, 'w', encoding='utf-8').write(t2); n += 1; print('riempito', os.path.basename(f))
resto = [os.path.basename(f) for f in glob.glob(P + '*-04-11/*.html') + glob.glob(R + 'coda/2026-11-04_*.json') if '__QUIZ' in open(f, encoding='utf-8').read()]
print('segnaposto ancora presenti in:', resto or 'nessuno')
