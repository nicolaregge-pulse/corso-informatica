#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Situazione dei quiz di sicurezza (Regione) della 2INF, ora per ora (21/10/2026, Nicola: «tutti devono fare i quiz delle prime 4 ore»).
# Legge i risultati dei Moduli nel riservato e scrive dati/situazione/2INF_sicurezza-ore.md (con i nomi: SOLO riservato).
import csv, json, os, sys, unicodedata
R = '/home/user/corso-informatica-riservato/'
ORE = [("1ª ora", "Rischio e danno", "01/10", "2inf-quiz-sicurezza1-20261001"),
       ("2ª ora", "Prevenzione e protezione", "09/10", "2inf-quiz-sicurezza2-20261009"),
       ("3ª ora", "Organizzazione della prevenzione", "16/10", "2inf-quiz-sicurezza3-20261021"),
       ("4ª ora", "Diritti, doveri, sanzioni, vigilanza", "21/10", "2inf-quiz-sicurezza4-20261021")]
CLASSE = json.load(open(R + 'dati/2inf-classe.json'))
def tok(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().upper().replace('.', ' ')
    return set(w for w in s.split() if len(w) > 2)
def chi(nome):
    t = tok(nome); best, bn = 0, None
    for n in CLASSE:
        k = len(t & tok(n))
        if k > best: best, bn = k, n
    return bn
T = {n: {} for n in CLASSE}
for ora, _, _, cart in ORE:
    f = R + 'dati/verifiche/' + cart + '/_RISULTATI-QUIZ.csv'
    if not os.path.exists(f): continue
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
        n = chi(r['nome'] + ' ' + r.get('email', '').split('@')[0])
        if n: T[n][ora] = max(T[n].get(ora, 0), round(40 + 40 * int(r['punteggio']) / int(r['massimo'])))
righe = ['# 2INF · Sicurezza (Regione): quiz ora per ora (RISERVATO)', '',
         'Voto = 40 + 40 × punti/massimo. «manca» = quiz non fatto.', '',
         '| Allievo | ' + ' | '.join(o[0] for o in ORE) + ' | Mancano |', '|---|' + '---|' * (len(ORE) + 1)]
for n in sorted(CLASSE):
    m = [o[0] for o in ORE if o[0] not in T[n]]
    righe.append('| ' + n + ' | ' + ' | '.join(str(T[n].get(o[0], 'manca')) for o in ORE) + ' | ' + (', '.join(m) or 'nessuno') + ' |')
righe += ['', '## Quanti hanno fatto ogni ora', ''] + ['%d. %s %s (%s): %d su %d' % (i + 1, o[0], o[1], o[2], sum(1 for n in CLASSE if o[0] in T[n]), len(CLASSE)) for i, o in enumerate(ORE)]
open(R + 'dati/situazione/2INF_sicurezza-ore.md', 'w', encoding='utf-8').write('\n'.join(righe) + '\n')
# 28/10/2026: anche in JSON (per la pagina del recupero, generatori/2inf_sicurezza_recupero.py nel riservato)
json.dump({n: {'voti': T[n], 'mancano': [i + 1 for i, o in enumerate(ORE) if o[0] not in T[n]]} for n in sorted(CLASSE)},
          open(R + 'dati/situazione/2INF_sicurezza-ore.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(righe))
