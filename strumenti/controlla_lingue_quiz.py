#!/usr/bin/env python3
"""Controlla che i quiz della 1INF (id con '1inf') abbiano italiano, arabo e cinese (R6).
Uso: python3 -I strumenti/controlla_lingue_quiz.py   (dalla radice del repository pubblico)
Esce con 1 se un quiz 1INF in fabbrica/indice.json non ha arabo e cinese. v1.0 - 11/11/2026"""
import base64, json, re, sys, os

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = re.compile(r'[؀-ۿ]')
ZH = re.compile(r'[一-鿿]')


def testo(q):
    pezzi = [q.get('titolo', ''), q.get('descrizione', '')]
    for d in q.get('domande', []):
        pezzi.append(d.get('t', ''))
        pezzi.append(d.get('sp', '') or '')
        for s in d.get('s', []):
            pezzi.append(s[0])
    return ' '.join(str(p) for p in pezzi)


def main():
    indice = json.load(open(os.path.join(RADICE, 'fabbrica', 'indice.json'), encoding='utf-8'))
    errori = 0
    for l in indice.get('lavori', []):
        if '1inf' not in l['id']:
            continue
        raw = open(os.path.join(RADICE, 'fabbrica', l['file']), encoding='utf-8').read().strip()
        q = json.loads(base64.b64decode(raw).decode('utf-8'))
        t = testo(q)
        mancano = [n for n, r in (('arabo', AR), ('cinese', ZH)) if not r.search(t)]
        if mancano:
            errori += 1
            print('MANCA ' + ' e '.join(mancano) + ': ' + l['id'])
        else:
            print('ok: ' + l['id'])
    sys.exit(1 if errori else 0)


main()
