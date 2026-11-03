#!/usr/bin/env python3
# Aggiunge alla pagina 2INF del 04/11 il riquadro «Recuperi: i quiz che ti mancano» (solo link ai Moduli esistenti, nessun nome). Idempotente.
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_pagine_lezione import svg, SLUGDIR
D = SLUGDIR + '2inf-sicurezza-04-11/'; QB = sys.argv[1] if len(sys.argv) > 1 else '__QUIZB2__'
LK = {'2': QB, '3': 'https://docs.google.com/forms/d/e/1FAIpQLSeANOFnWHWRF-uYH1H6l-eOocMUavGbAwDKC5yIUbYVoCiaUw/viewform', '4': 'https://docs.google.com/forms/d/e/1FAIpQLSevwdJOCe8J00jdKb33gMVypzv8AQoSB9Kup6dfHgHpqJ7azA/viewform', '5': 'https://docs.google.com/forms/d/e/1FAIpQLSeUvK_DEQTCavSQWX1lK1Dv5ZgL9-lNSWLRkTKPCb_vvYkhyg/viewform'}
svg(D + 'img/recuperi.svg', 'Recuperi', [('box', 'Nel cruscotto, accanto al tuo nome:\n«da recuperare: 5ª ora»', 80, 90, 640, 100), ('btn', 'Quiz della 5ª ora', 160, 240, 480)], (0, 1), 'Apri SOLO il quiz dell\'ora che ti manca')
h = open(D + 'index.html', encoding='utf-8').read()
card = ('<section class="card" id="recuperi"><h2>Recuperi: i quiz che ti mancano</h2><p>Apri «Come sto andando». Se accanto al tuo nome c\'è scritto <b>da recuperare</b> e un\'ora (per esempio 5ª), fai SOLO il quiz di quell\'ora, nei primi 10 minuti. Se non c\'è scritto niente, salta e comincia dal passo 1.</p>'
        '<p><a class="bt b" href="cruscotto-ragazzi.html" target="_blank" rel="noopener">Come sto andando</a></p><p>'
        '<a class="bt v" href="%s" target="_blank" rel="noopener">Quiz 2ª ora (breve)</a> <a class="bt v" href="%s" target="_blank" rel="noopener">Quiz 3ª ora</a> <a class="bt v" href="%s" target="_blank" rel="noopener">Quiz 4ª ora</a> <a class="bt v" href="%s" target="_blank" rel="noopener">Quiz 5ª ora</a></p>'
        '<figure style="margin:8px 0"><img class="sx-img" src="img/recuperi.svg" alt="Recuperi" loading="lazy"><figcaption class="mu" style="font-size:15px">Schema (non è uno screenshot esatto)</figcaption></figure></section>\n') % (LK['2'], LK['3'], LK['4'], LK['5'])
if 'id="recuperi"' in h: h = re.sub(r'<section class="card" id="recuperi">.*?</section>\n', lambda m: card, h, flags=re.S)
else: h = h.replace('<div class="passo" data-p="1">', card + '<div class="passo" data-p="1">', 1)
open(D + 'index.html', 'w', encoding='utf-8').write(h); print('ok', QB[:40])
