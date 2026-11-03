#!/usr/bin/env python3
# Scrive le pagine HTML dei cruscotti del 04/11 (docente cifrato e ragazzi) nelle due cartelle di anteprima, dal modello 1inf-deepfake-03-11.
import os, re, shutil
B = '/home/user/corso-informatica/docs/anteprima/'; M = B + '1inf-deepfake-03-11/'
doc = open(M + 'cruscotto.html', encoding='utf-8').read(); rag = open(M + 'cruscotto-ragazzi.html', encoding='utf-8').read()
for slug, cl, tit, sott in [('3inf-protocollo-04-11', '3INF', '3INF · 04/11 · protocollo del Mastermind', 'mercoledì 04/11: il protocollo del Mastermind'), ('2inf-sicurezza-04-11', '2INF', '2INF · 04/11 · Sicurezza 6ª ora', 'mercoledì 04/11: Sicurezza, 6ª ora')]:
    d = B + slug + '/'; shutil.copy('/home/user/corso-informatica/strumenti/vista_cruscotto_0411.js', d + 'cruscotto-vista.js'); shutil.copy(M + 'cruscotto.css', d + 'cruscotto.css')
    h = doc.replace('1inf-deepfake-03-11', slug).replace('Cruscotto 1INF', 'Cruscotto ' + cl).replace('1INF · 03/11 · deepfake', tit).replace('Cruscotto di martedì 03/11: deepfake, teoria e quiz.', 'Cruscotto di ' + sott + '.').replace('20261103i', '20261104a')
    open(d + 'cruscotto.html', 'w', encoding='utf-8').write(h)
    r = rag.replace('1INF 03/11', cl + ' 04/11').replace('20261103i', '20261104a')
    open(d + 'cruscotto-ragazzi.html', 'w', encoding='utf-8').write(r)
    assert 'deepfake' not in h.lower().replace('1inf-deepfake', ''), slug
print('ok')
