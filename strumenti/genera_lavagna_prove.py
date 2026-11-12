#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera le immagini e le spec di PROVA della lavagna: scegli (3 zone), disegna (freccia tastiera-CPU), collega+freccia.
Uso (dal repository pubblico): python3 strumenti/genera_lavagna_prove.py
Immagini semplici con PIL, nessun nome di allievo, nessuna immagine da internet."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera_lavagna_bibpc as G
from PIL import ImageFont

RAD = G.RADICE
IMG = os.path.join(RAD, 'docs', 'lavagna', 'img'); SPEC = os.path.join(RAD, 'docs', 'lavagna', 'spec')
V = G.IMG_V
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def testo(p, xy, s, size, fill='#1c2430'):
    f = ImageFont.truetype(FONT, size * G.S)
    p.d.text((xy[0] * G.S, xy[1] * G.S), s, font=f, fill=fill, anchor='mm')


def computer(path):
    p = G.P('#eef1f6')
    p.r([330, 60, 870, 400], '#2b2f36', '#111111', 5, 14); p.r([350, 80, 850, 380], '#9ec5e8')
    p.r([420, 130, 760, 150], '#ffffff'); p.r([420, 170, 700, 190], '#ffffff'); p.r([420, 210, 640, 230], '#ffffff')
    p.r([560, 400, 640, 450], '#555b66'); p.r([480, 450, 720, 480], '#555b66', None, 0, 8)
    p.r([280, 520, 920, 640], '#d9dde3', '#555b66', 4, 14)
    for r in range(4):
        for c in range(14):
            p.r([300 + c * 44, 536 + r * 26, 336 + c * 44, 556 + r * 26], '#ffffff', '#8a929e', 2, 4)
    p.e([1000, 500, 1090, 640], '#d9dde3', '#555b66', 4); p.l([(1045, 500), (1045, 560)], '#555b66', 3); p.l([(1045, 500), (1045, 440), (900, 420)], '#555b66', 3)
    p.salva(path)
    return {'schermo': [310, 40, 890, 500], 'tastiera': [260, 500, 940, 660], 'mouse': [980, 430, 1105, 650]}


def tastiera_cpu(path):
    p = G.P('#f4f1ea')
    p.r([60, 260, 460, 440], '#d9dde3', '#555b66', 4, 12)
    for r in range(4):
        for c in range(8):
            p.r([76 + c * 46, 276 + r * 38, 112 + c * 46, 304 + r * 38], '#ffffff', '#8a929e', 2, 4)
    testo(p, (260, 480), 'TASTIERA', 30)
    p.r([840, 250, 1040, 450], '#2b2f36', '#111111', 4, 10)
    for k in range(7):
        p.l([(820, 270 + k * 26), (840, 270 + k * 26)], '#c9ced6', 4); p.l([(1040, 270 + k * 26), (1060, 270 + k * 26)], '#c9ced6', 4)
    p.r([890, 300, 990, 400], '#4a505b', '#888888', 3, 6)
    testo(p, (940, 350), 'CPU', 30, '#ffffff')
    testo(p, (940, 480), 'CPU', 30)
    p.salva(path)
    return {'tastiera': [40, 240, 480, 500], 'cpu': [800, 230, 1080, 500]}


def scrivi(path, o):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(o, fh, ensure_ascii=False, indent=1); fh.write('\n')


def zl(d, nomi):
    return [{'id': k, 'rett': r, 'nome': nomi[k]} for k, r in d.items()]


def main():
    zc = computer(os.path.join(IMG, 'prova-computer.png'))
    zt = tastiera_cpu(os.path.join(IMG, 'prova-tastiera-cpu.png'))
    nc = {'schermo': 'lo schermo', 'tastiera': 'la tastiera', 'mouse': 'il mouse'}
    nci = {k: {'it': v, 'ar': {'schermo': 'الشاشة', 'tastiera': 'لوحة المفاتيح', 'mouse': 'الفأرة'}[k], 'zh': {'schermo': '屏幕', 'tastiera': '键盘', 'mouse': '鼠标'}[k]} for k, v in nc.items()}
    scrivi(os.path.join(SPEC, 'prova-scegli.json'), {
        'id': 'prova-scegli', 'versione': '1.0', 'classe': '2INF', 'lingue': ['it'],
        'titolo': {'it': 'Prova: tocca la parte giusta'}, 'sfondo': 'img/prova-computer.png?v=%d' % V, 'dimensioni': [1200, 700],
        'penne': ['rosso', 'blu', 'nero'], 'tentativi_max': 3,
        'passi': [
            {'id': 's1', 'tipo': 'scegli', 'testo': {'it': 'Tocca la parte del computer che serve per SCRIVERE le lettere.'},
             'zone': zl(zc, {k: {'it': v['it']} for k, v in nci.items()}), 'giusta': 'tastiera'},
            {'id': 's2', 'tipo': 'scegli', 'testo': {'it': 'Tocca la parte del computer che MOSTRA quello che fai.'},
             'zone': zl(zc, {k: {'it': v['it']} for k, v in nci.items()}), 'giusta': 'schermo'}]})
    scrivi(os.path.join(SPEC, 'prova-disegna.json'), {
        'id': 'prova-disegna', 'versione': '1.0', 'classe': '2INF', 'lingue': ['it'],
        'titolo': {'it': 'Prova: disegna una freccia'}, 'sfondo': 'img/prova-tastiera-cpu.png?v=%d' % V, 'dimensioni': [1200, 700],
        'penne': ['rosso', 'blu', 'nero'], 'tentativi_max': 3,
        'passi': [{'id': 'd1', 'tipo': 'disegna', 'penna': 'blu',
                   'testo': {'it': 'Disegna una freccia dalla tastiera alla CPU.'},
                   'criteri': {'it': 'La freccia parte dalla tastiera e finisce sulla CPU; la punta è dalla parte della CPU.'}}]})
    ncf = {'schermo': {'it': 'Schermo', 'ar': 'الشاشة', 'zh': '屏幕'}, 'tastiera': {'it': 'Tastiera', 'ar': 'لوحة المفاتيح', 'zh': '键盘'}, 'mouse': {'it': 'Mouse', 'ar': 'الفأرة', 'zh': '鼠标'}}
    l3 = ['it', 'ar', 'zh']
    scrivi(os.path.join(SPEC, 'prova-collega-freccia.json'), {
        'id': 'prova-collega-freccia', 'versione': '1.0', 'classe': '1INF', 'lingue': l3,
        'titolo': {'it': 'Prova: etichette e freccia', 'ar': 'تجربة: بطاقات وسهم', 'zh': '试用：标签和箭头'},
        'sfondo': 'img/prova-computer.png?v=%d' % V, 'dimensioni': [1200, 700], 'penne': ['rosso', 'blu', 'nero'], 'tentativi_max': 3,
        'passi': [
            {'id': 'c1', 'tipo': 'collega',
             'testo': {'it': 'Metti ogni etichetta sulla parte giusta del computer.', 'ar': 'ضع كل بطاقة على الجزء الصحيح من الكمبيوتر.', 'zh': '把每个标签放到电脑正确的部分上。'},
             'zone': zl(zc, nci),
             'etichette': [{'id': 'e-' + k, 'zona': k, 'testo': ncf[k]} for k in ('mouse', 'schermo', 'tastiera')]},
            {'id': 'f1', 'tipo': 'freccia', 'sfondo': 'img/prova-tastiera-cpu.png?v=%d' % V, 'penna': 'rosso',
             'testo': {'it': 'Con la penna rossa disegna una freccia dalla tastiera alla CPU.', 'ar': 'ارسم بالقلم الأحمر سهما من لوحة المفاتيح إلى المعالج (CPU).', 'zh': '用红笔画一个箭头，从键盘指向处理器（CPU）。'},
             'da': {'rett': zt['tastiera'], 'nome': {'it': 'la tastiera', 'ar': 'لوحة المفاتيح', 'zh': '键盘'}},
             'a': {'rett': zt['cpu'], 'nome': {'it': 'la CPU', 'ar': 'المعالج (CPU)', 'zh': '处理器（CPU）'}}}]})
    print('prove scritte')


if __name__ == '__main__':
    main()
