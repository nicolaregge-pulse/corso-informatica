#!/usr/bin/env python3
"""Controlla che i quiz della 1INF (id con '1inf') abbiano italiano, arabo e cinese (R6).
v1.1 (23/11/2026, errore #292): i quiz della 2INF (id con '2inf', solo italiano, R6) non hanno le sigle inglesi dell'interfaccia di
Windows (Settings, Network & internet, Apps, Start...): i PC hanno Windows in italiano. Per le altre classi la lista non si applica
finche' il docente non lo conferma (R7.6).
Uso: python3 -I strumenti/controlla_lingue_quiz.py   (dalla radice del repository pubblico)
Esce con 1 se un quiz 1INF in fabbrica/indice.json non ha arabo e cinese, o se un quiz 2INF ha sigle inglesi di Windows. v1.0 - 11/11/2026"""
import base64, json, re, sys, os

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = re.compile(r'[؀-ۿ]')
ZH = re.compile(r'[一-鿿]')
# sigle inglesi dell'interfaccia di Windows che nei quiz della 2INF devono stare in italiano (PC con Windows in italiano)
INGLESE_WINDOWS = re.compile(r'\b(?:Settings|Network\s*(?:&|and)\s*internet|Control\s+Panel|Task\s+Manager|File\s+Explorer|'
                             r'Apps\s*(?:&|and)\s*features|Windows\s+Update|Click\s+(?:Start|on)|Open\s+Settings|Privacy\s*(?:&|and)\s*security|'
                             r'Device\s+Manager|Start\s+menu)\b|\b(?:Click|Choose|Select|Open)\s+(?:the\s+)?[A-Z]\w+', re.I)


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
        if '2inf' in l['id']:
            raw = open(os.path.join(RADICE, 'fabbrica', l['file']), encoding='utf-8').read().strip()
            q = json.loads(base64.b64decode(raw).decode('utf-8'))
            m = INGLESE_WINDOWS.search(testo(q))
            if m:
                errori += 1
                print('INGLESE nel quiz 2INF (Windows e in italiano, #292): «' + m.group(0) + '» in ' + l['id'])
            else:
                print('ok: ' + l['id'])
            continue
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
