#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il compito lavagna «Biblioteca e PC» (1INF, dopo il quiz): 8 immagini disegnate con PIL
e docs/lavagna/spec/biblioteca-pc-1inf-ora6.json (8 passi «cerchia», ordine casuale per ragazzo).

Uso (dalla cartella del repository pubblico):
    python3 strumenti/genera_lavagna_bibpc.py [--riservato /home/user/corso-informatica-riservato]

Le zone bersaglio sono calcolate dalle stesse funzioni che disegnano: nessun rettangolo scritto a mano.
Nessuna etichetta di testo nelle immagini dei PC. Nessun nome di allievo. Niente immagini da internet.
Con --riservato copia le 8 immagini originali e le zone in <riservato>/lavagne/1INF/bibpc-originali/.
"""
import argparse, json, os, random, shutil, sys
from PIL import Image, ImageDraw

W, H, S = 1200, 700, 2
RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class P:
    """Disegno con supersampling 2x: tutte le coordinate sono a 1200x700."""
    def __init__(self, sfondo):
        self.bg = sfondo
        self.im = Image.new('RGB', (W * S, H * S), sfondo)
        self.d = ImageDraw.Draw(self.im)

    def _c(self, c):
        """Colori a 8 cifre (#rrggbbaa): trasparenza mescolata con lo sfondo di base."""
        if isinstance(c, str) and len(c) == 9:
            a = int(c[7:9], 16) / 255.0
            f = [int(self.bg[i:i + 2], 16) for i in (1, 3, 5)]
            return '#%02x%02x%02x' % tuple(int(int(c[i:i + 2], 16) * a + f[k] * (1 - a)) for k, i in enumerate((1, 3, 5)))
        return c

    def _b(self, b):
        return [int(round(v * S)) for v in b]

    def r(self, b, fill=None, out=None, w=0, rad=0):
        if rad:
            self.d.rounded_rectangle(self._b(b), radius=rad * S, fill=self._c(fill), outline=self._c(out), width=w * S)
        else:
            self.d.rectangle(self._b(b), fill=self._c(fill), outline=self._c(out), width=w * S)

    def e(self, b, fill=None, out=None, w=0):
        self.d.ellipse(self._b(b), fill=self._c(fill), outline=self._c(out), width=w * S)

    def p(self, pts, fill, out=None):
        self.d.polygon([(x * S, y * S) for x, y in pts], fill=self._c(fill), outline=self._c(out))

    def l(self, pts, fill, w=2):
        self.d.line([(x * S, y * S) for x, y in pts], fill=self._c(fill), width=int(w * S), joint='curve')

    def salva(self, path):
        self.im.resize((W, H), Image.LANCZOS).save(path, optimize=True)


def bbox(items, pad=0):
    x0 = min(i[0] for i in items); y0 = min(i[1] for i in items)
    x1 = max(i[2] for i in items); y1 = max(i[3] for i in items)
    return [int(x0 - pad), int(y0 - pad), int(x1 + pad), int(y1 + pad)]


# ---------------------------------------------------------------- biblioteca
# Regole di disegno (feedback del docente 12/11/2026): il TAVOLO DI LETTURA ha legno chiaro, 2-3 sedie, libri aperti e lampada;
# il BANCO PRESTITI e alto, grigio-azzurro, con pannello frontale, cartello, scanner e schermo, senza sedie;
# il tavolo non tocca mai gli scaffali (almeno 40 px di distanza, controllato in fondo).
def libri(p, box, righe, rnd, pieno=1.0):
    x0, y0, x1, y1 = box
    h = (y1 - y0) / righe
    cols = ['#b5362f', '#2f6db5', '#2e8b57', '#d9a21b', '#7a4fa3', '#c7662c', '#3a9aa8', '#8b3a62', '#556b2f', '#d0d0d0']
    for k in range(righe):
        yb = y0 + (k + 1) * h - 4
        p.r([x0, yb, x1, yb + 6], '#6b4423')
        x = x0 + 4
        while x < x1 - 8:
            bw = rnd.randint(9, 20); bh = rnd.randint(int(h * .62), int(h * .9))
            if rnd.random() <= pieno:
                p.r([x, yb - bh, x + bw, yb], rnd.choice(cols), '#00000030', 1)
            x += bw + 1


def persona(p, cx, ytop, h, veste, gilet=None, occhiali=False, pelle='#e0ac7e', capelli='#3b2a20', seduta=False):
    hr = h * .11
    ybody = ytop + 2.3 * hr
    yfine = ytop + (h * .62 if not seduta else h * .75)
    if not seduta:
        p.r([cx - hr * .8, yfine - 4, cx - hr * .1, ytop + h], '#2d3a4f', rad=3)
        p.r([cx + hr * .1, yfine - 4, cx + hr * .8, ytop + h], '#2d3a4f', rad=3)
    p.r([cx - hr * 1.3, ybody, cx + hr * 1.3, yfine], veste, rad=10)
    if gilet:
        p.r([cx - hr * 1.3, ybody, cx + hr * 1.3, yfine], gilet, rad=10)
        p.r([cx - hr * .25, ybody + 4, cx + hr * .25, yfine - 2], veste)
        p.r([cx + hr * .5, ybody + hr * .5, cx + hr * 1.0, ybody + hr * .95], '#ffffff', '#555555', 1)  # cartellino senza testo
    p.e([cx - hr, ytop, cx + hr, ytop + 2 * hr], pelle)
    p.e([cx - hr, ytop - 2, cx + hr, ytop + hr * 1.1], capelli)
    p.e([cx - hr * .8, ytop + hr * .55, cx + hr * .8, ytop + 2 * hr], pelle)
    p.e([cx - hr * .42, ytop + hr * .95, cx - hr * .22, ytop + hr * 1.15], '#222222')
    p.e([cx + hr * .22, ytop + hr * .95, cx + hr * .42, ytop + hr * 1.15], '#222222')
    if occhiali:
        p.e([cx - hr * .62, ytop + hr * .8, cx - hr * .05, ytop + hr * 1.3], None, '#222222', 2)
        p.e([cx + hr * .05, ytop + hr * .8, cx + hr * .62, ytop + hr * 1.3], None, '#222222', 2)
        p.l([(cx - hr * .05, ytop + hr * 1.05), (cx + hr * .05, ytop + hr * 1.05)], '#222222', 2)
    return [cx - hr * 1.6, ytop - 3, cx + hr * 1.6, ytop + h]


def libro_aperto(p, cx, cy, w=70, h=40):
    p.p([(cx - w, cy), (cx, cy - 8), (cx, cy + h - 8), (cx - w, cy + h)], '#fdfdf5', '#555555')
    p.p([(cx, cy - 8), (cx + w, cy), (cx + w, cy + h), (cx, cy + h - 8)], '#f1f1e4', '#555555')
    for k in range(3):
        p.l([(cx - w + 10, cy + 8 + k * 9), (cx - 8, cy + 3 + k * 9)], '#8aa', 1.5)
        p.l([(cx + 8, cy + 3 + k * 9), (cx + w - 10, cy + 8 + k * 9)], '#8aa', 1.5)


def lampada(p, x, y):
    """Lampada da tavolo: (x,y) = punto d'appoggio sul piano."""
    p.e([x - 14, y - 6, x + 14, y + 2], '#555555')
    p.l([(x, y - 3), (x + 6, y - 34)], '#555555', 4)
    p.p([(x - 8, y - 52), (x + 24, y - 52), (x + 34, y - 28), (x - 4, y - 28)], '#f3d54a', '#8a6d00')


def tavolo_lettura(p, x, y, w, libri_sopra=True, lamp=True, portatile=False, lettore=None):
    """Tavolo di lettura inequivocabile: legno chiaro, 3 sedie, libri aperti, lampada. y = piano. Ritorna il rettangolo."""
    legno, bordo, sedia, gambe = '#ecd29c', '#a67c3d', '#3f6aa0', '#2c4a70'
    cx = x + w / 2
    top = y - 80
    if lettore:
        b = persona(p, cx + w * .12, y - 108, 150, lettore[0], seduta=True, capelli=lettore[1])
        top = min(top, b[1])
    else:
        p.r([cx - 30, y - 78, cx + 30, y - 8], sedia, '#1d3250', 2, 8)      # sedia dietro il tavolo
    for lato in (-1, 1):                                                   # sedie ai lati
        sx = x - 50 if lato < 0 else x + w + 8
        p.r([sx, y + 12, sx + 42, y + 24], sedia, '#1d3250', 2)
        bx = sx if lato < 0 else sx + 32
        p.r([bx, y - 38, bx + 10, y + 24], sedia, '#1d3250', 2)
        p.r([sx + 5, y + 24, sx + 11, y + 80], gambe); p.r([sx + 31, y + 24, sx + 37, y + 80], gambe)
    p.r([x + 10, y + 16, x + 24, y + 80], '#c9a15f', '#7a5a2b', 1); p.r([x + w - 24, y + 16, x + w - 10, y + 80], '#c9a15f', '#7a5a2b', 1)
    p.r([x, y, x + w, y + 16], legno, bordo, 3)
    if libri_sopra:
        libro_aperto(p, x + w * .36, y - 34, w * .26, 32); libro_aperto(p, x + w * .73, y - 32, w * .2, 28)
    if portatile:
        p.p([(x + w * .5 - 30, y - 2), (x + w * .5 + 30, y - 2), (x + w * .5 + 22, y - 36), (x + w * .5 - 22, y - 36)], '#3a3f48')
        p.r([x + w * .5 - 18, y - 33, x + w * .5 + 18, y - 8], '#9ec5e8')
    if lamp:
        lampada(p, x + 22, y)
        top = min(top, y - 54)
    return [x - 52, top - 2, x + w + 52, y + 82]


def banco_prestiti(p, x, y, w, h, cartello_cx=None, scanner=True, schermo=True):
    """Banco prestiti: bancone ALTO grigio-azzurro con pannello frontale, cartello, scanner e piccolo schermo, senza sedie."""
    p.r([x, y, x + w, y + h], '#9fb4c8', '#5b7089', 3)
    p.r([x - 8, y - 6, x + w + 8, y + 14], '#c3d1de', '#5b7089', 3)
    p.r([x + 14, y + 30, x + w - 14, y + h - 14], '#7b93ab', '#4a5f75', 3, 4)
    for k in range(1, 4):
        p.l([(x + 14 + k * (w - 28) / 4, y + 34), (x + 14 + k * (w - 28) / 4, y + h - 18)], '#4a5f75', 2)
    cx = cartello_cx if cartello_cx is not None else x + w / 2
    p.l([(cx - 34, y - 6), (cx - 34, y - 70)], '#5b7089', 5); p.l([(cx + 34, y - 6), (cx + 34, y - 70)], '#5b7089', 5)
    p.r([cx - 56, y - 124, cx + 56, y - 66], '#ffffff', '#2f4f7a', 4, 4)             # cartello (senza testo)
    p.r([cx - 46, y - 114, cx + 46, y - 104], '#2f6db5'); p.r([cx - 46, y - 96, cx + 20, y - 88], '#9fb4c8'); p.r([cx - 46, y - 82, cx + 36, y - 76], '#9fb4c8')
    top = y - 126
    if scanner:
        sx = x + 22
        p.r([sx, y - 30, sx + 74, y - 6], '#f2f2f2', '#555555', 2); p.p([(sx + 8, y - 30), (sx + 66, y - 30), (sx + 70, y - 52), (sx + 12, y - 52)], '#d9dde3', '#555555')
        p.l([(sx + 12, y - 18), (sx + 62, y - 18)], '#e53935', 3)
    if schermo:
        mx = x + w - 112
        p.r([mx, y - 70, mx + 84, y - 14], '#333b45', '#111111', 3); p.r([mx + 6, y - 64, mx + 78, y - 20], '#9ec5e8')
        p.r([mx + 36, y - 14, mx + 48, y - 6], '#333b45')
        top = min(top, y - 126)
    return [x - 12, top - 2, x + w + 12, y + h + 3]


def sfondo_sala(p, muro, pavimento, yp=420):
    p.r([0, 0, W, yp], muro)
    p.r([0, yp, W, H], pavimento)
    for k in range(0, W, 90):
        p.l([(k, yp), (k - 120, H)], '#00000018', 2)


def scena0(path, rnd):
    """Immagine base della lavagna «biblioteca» (v2): scaffali, tavolo di lettura, bibliotecario, banco prestiti, corridoi, stampante."""
    p = P('#faf3e6'); sfondo_sala(p, '#faf3e6', '#ede3d0', 470)
    libri(p, [740, 50, 1150, 415], 4, rnd); p.r([734, 44, 1156, 421], None, '#6b4423', 6)
    z = {}
    z['scaffali'] = [728, 38, 1162, 427]
    z['banco_prestiti'] = banco_prestiti(p, 30, 340, 210, 160, cartello_cx=135)
    z['bibliotecario'] = persona(p, 305, 262, 215, '#3a6ea5', gilet='#2e9d4f', occhiali=True)
    z['tavolo_lettura'] = tavolo_lettura(p, 425, 400, 200, portatile=True)
    p.r([800, 520, 1000, 620], '#dcdde2', '#3d3d4a', 4, 10); p.r([830, 500, 970, 522], '#ffffff', '#3d3d4a', 3); p.r([880, 580, 960, 606], '#5a5a66')
    z['stampante'] = [794, 494, 1006, 626]
    for (x0, x1, y, verso) in ((230, 760, 600, 1), (230, 760, 650, -1)):
        p.r([x0 + (0 if verso > 0 else 30), y - 5, x1 - (30 if verso > 0 else 0), y + 5], '#7b9ac4')
        if verso > 0:
            p.p([(x1 - 30, y - 17), (x1, y), (x1 - 30, y + 17)], '#7b9ac4')
        else:
            p.p([(x0 + 30, y - 17), (x0, y), (x0 + 30, y + 17)], '#7b9ac4')
    z['corridoio'] = [222, 580, 768, 672]
    p.salva(path)
    return z


def scena1(path, rnd):
    """Sala di lettura: il bibliotecario (gilet verde, cartellino, occhiali) lavora al banco prestiti; tre tavoli di lettura."""
    p = P('#f0e6d2'); sfondo_sala(p, '#efe3cb', '#cfae82')
    z = {}
    libri(p, [30, 70, 400, 380], 4, rnd); p.r([26, 66, 404, 386], None, '#6b4423', 5)
    libri(p, [800, 70, 1170, 380], 4, rnd); p.r([796, 66, 1174, 386], None, '#6b4423', 5)
    z['scaffali_sinistra'] = [20, 60, 410, 392]; z['scaffali_destra'] = [790, 60, 1180, 392]
    b = persona(p, 560, 205, 195, '#3a6ea5', gilet='#2e9d4f', occhiali=True)
    z['bibliotecario'] = [b[0], b[1], b[2], 405]
    z['banco_prestiti'] = banco_prestiti(p, 430, 360, 340, 100, cartello_cx=700, scanner=True, schermo=False)
    z['tavolo_a'] = tavolo_lettura(p, 100, 565, 190, lettore=('#7d4a8a', '#222222'))
    z['tavolo_b'] = tavolo_lettura(p, 505, 595, 190, lamp=False, lettore=('#2f8f8f', '#a0522d'))
    z['tavolo_c'] = tavolo_lettura(p, 905, 565, 190, lettore=('#c7662c', '#6b3b1a'))
    p.salva(path)
    return z


def scena2(path, rnd):
    """Sala con fotocopiatrice e tavoli: solo UN tavolo ha i libri aperti che si usano adesso."""
    p = P('#eef0f2'); sfondo_sala(p, '#e8edf1', '#c3c2b0', 400)
    z = {}
    for wx in (420, 640, 860):
        p.r([wx, 60, wx + 160, 280], '#bfe0f2', '#6b7280', 5); p.l([(wx + 80, 60), (wx + 80, 280)], '#6b7280', 4); p.l([(wx, 170), (wx + 160, 170)], '#6b7280', 4)
    p.r([70, 300, 340, 540], '#c9ced6', '#5f6672', 3, 10)
    p.p([(70, 300), (340, 300), (320, 262), (92, 262)], '#e4e8ee', '#5f6672')
    p.r([100, 330, 310, 380], '#2d3a4f'); p.r([110, 338, 300, 372], '#8fd1ff')
    p.r([100, 400, 310, 430], '#f4f4f4', '#777777', 2); p.r([110, 470, 300, 540], '#9aa1ab', '#5f6672', 2)
    p.e([290, 396, 306, 412], '#e53935'); p.l([(120, 395), (290, 395)], '#ffffff', 2)
    z['fotocopiatrice'] = [62, 254, 348, 548]
    z['tavolo_lettura'] = tavolo_lettura(p, 450, 545, 200, lettore=('#c7662c', '#222222'), portatile=False)
    z['tavolo_vuoto'] = tavolo_lettura(p, 810, 480, 200, libri_sopra=False, lamp=False)
    p.e([1075, 470, 1140, 530], '#2e8b57'); p.e([1090, 440, 1130, 500], '#3a9d63'); p.r([1093, 515, 1122, 580], '#a05a2c', '#6b3b1a', 2)
    z['pianta'] = [1072, 436, 1144, 584]
    p.salva(path)
    return z


def scena3(path, rnd):
    """Magazzino con carrelli: gli scaffali pieni (tutti i libri) sono il bersaglio."""
    p = P('#dcdde0'); sfondo_sala(p, '#d4d7dc', '#a3a39e', 520)
    z = {}
    sx0, sy0, sx1, sy1 = 70, 60, 770, 490
    p.r([sx0 - 8, sy0 - 8, sx1 + 8, sy1 + 8], '#7b8794', '#4b5563', 4)
    for k in range(5):
        p.r([sx0 - 8, sy0 + k * 86 + 80, sx1 + 8, sy0 + k * 86 + 88], '#4b5563')
    libri(p, [sx0, sy0, sx1, sy1], 5, rnd)
    z['scaffali'] = [sx0 - 14, sy0 - 14, sx1 + 14, sy1 + 14]
    p.r([850, 120, 1150, 460], '#aab2bd', '#4b5563', 3)
    for k in range(3):
        p.r([850, 120 + k * 113 + 100, 1150, 120 + k * 113 + 110], '#4b5563')
    for bx, by in ((870, 360), (990, 370), (905, 245), (1040, 250)):
        p.r([bx, by, bx + 90, by + 90 - 10 if by > 300 else by + 80], '#c89b5b', '#7a5a2b', 2)
    z['scaffale_scatoloni'] = [842, 112, 1158, 468]

    def carrello(x, y, w, carico):
        p.r([x, y, x + w, y + 14], '#3b82f6', '#1e3a8a', 2)
        p.l([(x + w - 8, y), (x + w + 25, y - 95)], '#1e3a8a', 6)
        p.e([x + 14, y + 16, x + 44, y + 46], '#222222'); p.e([x + w - 44, y + 16, x + w - 14, y + 46], '#222222')
        for k in range(carico):
            p.r([x + 12 + k * 34, y - 36 - (k % 2) * 6, x + 40 + k * 34, y], ['#b5362f', '#2e8b57', '#d9a21b', '#7a4fa3', '#2f6db5'][k % 5], '#333333', 1)
        return [x - 4, y - 99, x + w + 30, y + 50]
    z['carrello_a'] = carrello(120, 610, 260, 6)
    z['carrello_b'] = carrello(520, 600, 270, 5)
    z['addetto'] = persona(p, 1000, 530, 150, '#c2410c', capelli='#222222')
    p.salva(path)
    return z


def scena4(path, rnd):
    """Banco prestiti con scanner a sinistra, scaffali a destra: il corridoio con il carrello e il bersaglio."""
    p = P('#f3ead8'); sfondo_sala(p, '#f0e4cc', '#c4ae86', 380)
    z = {}
    libri(p, [900, 70, 1170, 500], 5, rnd); p.r([894, 64, 1176, 506], None, '#6b4423', 5)
    z['scaffali'] = [888, 58, 1182, 512]
    z['banco_prestiti'] = banco_prestiti(p, 40, 385, 290, 170, cartello_cx=120)
    z['bibliotecario'] = persona(p, 395, 265, 215, '#556b8d', gilet='#2e9d4f', capelli='#4a2f1b')
    cx0, cy0, cx1, cy1 = 470, 470, 850, 660
    p.p([(cx0, cy0), (cx1, cy0), (cx1 + 10, cy1), (cx0 - 20, cy1)], '#ddd5c0', '#9a8f74')
    for k in range(6):
        p.r([cx0 + 20 + k * 62, 560, cx0 + 56 + k * 62, 572], '#f2c200')
    p.r([540, 520, 760, 536], '#3b82f6', '#1e3a8a', 2); p.l([(752, 520), (782, 430)], '#1e3a8a', 6)
    p.e([554, 540, 582, 568], '#222222'); p.e([715, 540, 743, 568], '#222222')
    for k, c in enumerate(['#b5362f', '#2e8b57', '#d9a21b', '#7a4fa3', '#2f6db5']):
        p.r([552 + k * 38, 484 - (k % 2) * 6, 586 + k * 38, 520], c, '#333333', 1)
    for ax in (490, 770):
        p.p([(ax, 622), (ax + 36, 622), (ax + 36, 608), (ax + 62, 628), (ax + 36, 648), (ax + 36, 634), (ax, 634)], '#2e9d4f')
    z['corridoio'] = [cx0 - 24, 425, cx1 + 14, cy1 + 4]
    p.salva(path)
    return z


# ---------------------------------------------------------------- scheda madre (vista dall'alto, senza testo)
def ventola(p, cx, cy, r, giri=7, colore='#222222'):
    p.e([cx - r, cy - r, cx + r, cy + r], '#d9dde3', '#555555', 3)
    import math
    for k in range(giri):
        a = 2 * math.pi * k / giri
        pts = [(cx + 8 * math.cos(a), cy + 8 * math.sin(a)),
               (cx + r * .86 * math.cos(a - .38), cy + r * .86 * math.sin(a - .38)),
               (cx + r * .92 * math.cos(a + .12), cy + r * .92 * math.sin(a + .12))]
        p.p(pts, colore, '#000000')
    p.e([cx - 10, cy - 10, cx + 10, cy + 10], '#888888', '#222222', 2)


def cpu(p, cx, cy, s):
    b = [cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2]
    p.r(b, '#2b2f36', '#111111', 4, 8)
    for k in range(1, 9):
        p.l([(b[0] + 8, b[1] + k * s / 9), (b[2] - 8, b[1] + k * s / 9)], '#454b55', 2)
    ventola(p, cx, cy, s * .38)
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        p.e([cx + dx * s * .44 - 7, cy + dy * s * .44 - 7, cx + dx * s * .44 + 7, cy + dy * s * .44 + 7], '#c0c4cc', '#555555', 2)
    return [b[0] - 6, b[1] - 6, b[2] + 6, b[3] + 6]


def ram(p, x, y, n, h, occupati, w=30, gap=16):
    blocchi = []
    for k in range(n):
        bx = x + k * (w + gap)
        p.r([bx, y, bx + w, y + h], '#1c1f24', '#000000', 2, 3)
        p.r([bx + 8, y + 4, bx + w - 8, y + h - 4], '#0e1013')
        if k in occupati:
            p.r([bx - 2, y + 2, bx + w + 2, y + h - 2], '#2f9e5b', '#145c33', 2, 3)
            for j in range(6):
                p.r([bx + 4, y + 14 + j * (h - 40) / 6, bx + w - 4, y + 14 + j * (h - 40) / 6 + (h - 40) / 6 - 8], '#111111', '#555555', 1)
            p.r([bx + 4, y + h - 14, bx + w - 4, y + h - 6], '#d9b44a')
            p.r([bx + 2, y - 8, bx + w - 2, y + 4], '#9aa1ab')
    return [x - 8, y - 12, x + n * (w + gap) - gap + 8, y + h + 6]


def traccia_bus(p, a, b, n=8, passo=11, jog=34, colore='#e6b422'):
    """Fascio di n piste dorate parallele da a=(x,y) a b=(x,y), con una piega: ritorna il rettangolo."""
    xs = []; ys = []
    (ax, ay), (bx, by) = a, b
    mx = (ax + bx) / 2
    for k in range(n):
        off = k * passo
        pts = [(ax, ay + off), (mx - (n - k) * 6, ay + off), (mx - (n - k) * 6 + jog, by + off), (bx, by + off)]
        p.l(pts, '#00000030', 8); p.l(pts, colore, 5)
        xs += [q[0] for q in pts]; ys += [q[1] for q in pts]
    return [min(xs) - 6, min(ys) - 6, max(xs) + 6, max(ys) + 6]


def piste_sottili(p, tracce, colore):
    for pts in tracce:
        p.l(pts, colore, 3)
        p.e([pts[-1][0] - 5, pts[-1][1] - 5, pts[-1][0] + 5, pts[-1][1] + 5], colore)


def porte_usb(p, x, y, n=4):
    for k in range(n):
        bx, by = x + k * 44, y
        p.r([bx, by, bx + 34, by + 28], '#c9ced6', '#555555', 2)
        p.r([bx + 5, by + 8, bx + 29, by + 20], '#2b6cd0' if k % 2 == 0 else '#222222')
    return [x - 4, y - 4, x + (n - 1) * 44 + 38, y + 32]


def condensatori(p, pos, colore='#3a3f48'):
    for x, y in pos:
        p.e([x - 11, y - 11, x + 11, y + 11], colore, '#111111', 2); p.l([(x - 6, y), (x + 6, y)], '#aaaaaa', 2)
    return [min(x for x, y in pos) - 14, min(y for x, y in pos) - 14, max(x for x, y in pos) + 14, max(y for x, y in pos) + 14]


def ssd25(p, x, y, w, h):
    p.r([x, y, x + w, y + h], '#2b2f36', '#111111', 3, 8)
    p.r([x + 12, y + 14, x + w - 12, y + 46], '#4a505b')
    for j in range(3):
        p.r([x + 16 + j * (w - 40) / 3, y + 20, x + 16 + j * (w - 40) / 3 + (w - 60) / 3, y + 40], '#111111', '#777777', 1)
    p.r([x + w - 40, y + h - 16, x + w - 8, y + h - 4], '#d9b44a')
    return [x - 4, y - 4, x + w + 4, y + h + 4]


def hdd35(p, x, y, w, h):
    p.r([x, y, x + w, y + h], '#b8bec8', '#4b5563', 3, 6)
    cx, cy, r = x + h * .5, y + h * .5, h * .38
    p.e([cx - r, cy - r, cx + r, cy + r], '#8a929e', '#333333', 3)
    p.e([cx - r * .75, cy - r * .75, cx + r * .75, cy + r * .75], '#c9d0da', '#555555', 2)
    p.e([cx - 8, cy - 8, cx + 8, cy + 8], '#444444')
    p.l([(x + w - 30, y + 14), (cx + 6, cy + 4)], '#333333', 6)
    p.r([x + h * .98, y + 12, x + w - 10, y + h - 12], '#9aa1ab', '#555555', 2)
    p.r([x + w - 48, y + h - 8, x + w - 6, y + h + 6], '#d9b44a')
    return [x - 4, y - 4, x + w + 4, y + h + 6]


def alimentatore(p, b, cavi=True, lato='destra'):
    x0, y0, x1, y1 = b
    p.r(b, '#8f98a5', '#3b4350', 3, 8)
    ventola(p, (x0 + x1) / 2, (y0 + y1) / 2, min(x1 - x0, y1 - y0) * .36, 9, '#3b4350')
    if cavi:
        for k, c in enumerate(['#d03030', '#222222', '#e0b020', '#2f6db5']):
            p.l([(x0, y0 + 20 + k * 12), (x0 - 40, y0 + 30 + k * 16), (x0 - 60, y0 + 80 + k * 16)], c, 5)
        return [x0 - 66, y0, x1, y1]
    return [x0 - 3, y0 - 3, x1 + 3, y1 + 3]


def scheda(path, v):
    p = P(v['sfondo'])
    bx0, by0, bx1, by1 = v['scheda']
    p.r([bx0 - 8, by0 - 8, bx1 + 8, by1 + 8], '#00000030', None, 0, 14)
    p.r(v['scheda'], v['colore'], v['bordo'], 5, 14)
    for x, y in ((bx0 + 22, by0 + 22), (bx1 - 22, by0 + 22), (bx0 + 22, by1 - 22), (bx1 - 22, by1 - 22)):
        p.e([x - 8, y - 8, x + 8, y + 8], '#d9dde3', '#555555', 2)
    piste_sottili(p, v['sottili'], v['piste'])
    z = {}
    pc = []
    for (x, y, w) in v['pcie']:
        p.r([x, y, x + w, y + 22], '#c9ced6', '#555555', 2, 3); p.r([x + 8, y + 7, x + w - 8, y + 15], '#2b2f36')
        pc.append([x - 3, y - 3, x + w + 3, y + 25])
    z['pcie'] = bbox(pc)
    cx, cy, s = v['cpu']
    z['bus'] = traccia_bus(p, *v['bus'])        # disegnato prima: i capi vanno sotto CPU e RAM
    z['cpu'] = cpu(p, cx, cy, s)
    chip = v['chipset']
    p.r(chip, '#6b7280', '#333333', 3, 4)
    for k in range(1, 5):
        p.l([(chip[0] + 6, chip[1] + k * (chip[3] - chip[1]) / 5), (chip[2] - 6, chip[1] + k * (chip[3] - chip[1]) / 5)], '#9aa1ab', 2)
    z['chipset'] = [chip[0] - 3, chip[1] - 3, chip[2] + 3, chip[3] + 3]
    z['ram'] = ram(p, *v['ram'])
    z['cond'] = condensatori(p, v['cond'], v['colcond'])
    z['usb'] = porte_usb(p, *v['usb'])
    for (x, y) in v['jack']:
        p.e([x - 10, y - 10, x + 10, y + 10], '#3b82f6' if (x + y) % 3 else '#2e9d4f', '#222222', 2)
    z['jack'] = bbox([[x - 12, y - 12, x + 12, y + 12] for x, y in v['jack']])
    p.e(v['batteria'], '#c9ced6', '#555555', 3)
    z['batteria'] = [v['batteria'][0] - 3, v['batteria'][1] - 3, v['batteria'][2] + 3, v['batteria'][3] + 3]
    z['psu'] = alimentatore(p, v['psu'], cavi=v['cavi'])
    st = v['disco']
    z['disco'] = (ssd25 if st[0] == 'ssd' else hdd35)(p, *st[1:])
    p.l(v['cavo_sata'], '#d03030', 6)
    p.salva(path)
    return z


VARIANTI = {
    # 05: bersaglio CPU. scheda verde, CPU al centro-sinistra, RAM a destra, SSD 2,5" fuori scheda
    5: dict(sfondo='#e9edf2', scheda=[60, 40, 930, 660], colore='#2c6e49', bordo='#14391f', piste='#3f8a5f',
            cpu=(330, 300, 210), ram=(660, 120, 4, 300, [0, 1]),
            bus=((440, 270), (650, 190), 8, 12, 34), chipset=[560, 500, 650, 590],
            pcie=[(110, 560, 380), (110, 610, 380)], cond=[(470, 100), (500, 100), (530, 100)], colcond='#3a3f48',
            usb=(110, 80, 3), jack=[(760, 560), (800, 560), (840, 560)], batteria=[700, 490, 750, 540],
            psu=[960, 60, 1160, 260], cavi=True, disco=('ssd', 960, 360, 190, 240), cavo_sata=[(960, 480), (900, 480), (850, 520), (700, 540)],
            sottili=[[(200, 300), (140, 300), (140, 380)], [(470, 330), (540, 400), (540, 480)], [(330, 440), (330, 500)]], chiave='cpu'),
    # 06: bersaglio RAM. scheda blu, CPU a destra, RAM a sinistra (6 slot), HDD 3,5" in basso
    6: dict(sfondo='#f1ede6', scheda=[60, 40, 940, 640], colore='#1f4e8c', bordo='#0d2747', piste='#4a78b5',
            cpu=(690, 280, 220), ram=(120, 90, 6, 280, [1, 3]),
            bus=((400, 240), (575, 220), 7, 12, 40), chipset=[600, 480, 690, 570],
            pcie=[(330, 560, 340), (330, 600, 340)], cond=[(780, 100), (810, 100), (840, 100), (870, 100)], colcond='#c9ced6',
            usb=(130, 540, 3), jack=[(500, 520), (540, 520), (580, 520)], batteria=[450, 470, 500, 520],
            psu=[970, 60, 1160, 240], cavi=True, disco=('hdd', 790, 440, 240, 150), cavo_sata=[(790, 520), (760, 520), (720, 560), (690, 560)],
            sottili=[[(690, 400), (690, 460)], [(150, 410), (150, 480), (260, 480)]], chiave='ram'),
    # 07: bersaglio disco. scheda scura, CPU in alto a sinistra, RAM in alto a destra, HDD grande in basso a destra
    7: dict(sfondo='#e6e9ee', scheda=[50, 40, 800, 660], colore='#25272c', bordo='#0b0c0e', piste='#b8452e',
            cpu=(250, 230, 200), ram=(560, 90, 4, 270, [0, 2]),
            bus=((360, 200), (550, 150), 8, 12, 30), chipset=[360, 420, 450, 500],
            pcie=[(90, 520, 330), (90, 570, 330)], cond=[(520, 420), (550, 420), (580, 420), (610, 420)], colcond='#6b7280',
            usb=(90, 70, 1), jack=[(480, 590), (520, 590), (560, 590)], batteria=[690, 440, 740, 490],
            psu=[830, 60, 1160, 250], cavi=True, disco=('hdd', 840, 350, 320, 220), cavo_sata=[(840, 450), (790, 450), (760, 380), (700, 380)],
            sottili=[[(250, 330), (250, 400)], [(560, 380), (500, 440)]], chiave='disco'),
    # 08: bersaglio bus. scheda grigio-verde, CPU a sinistra, RAM a destra, fascio ben largo
    8: dict(sfondo='#eef1ea', scheda=[60, 40, 960, 660], colore='#4a6b5d', bordo='#1f332a', piste='#6c8f80',
            cpu=(260, 330, 220), ram=(760, 110, 4, 300, [1, 2]),
            bus=((390, 300), (740, 240), 9, 14, 60), chipset=[450, 500, 550, 590],
            pcie=[(120, 570, 300), (120, 610, 300)], cond=[(640, 520), (670, 520), (700, 520), (640, 560), (670, 560)], colcond='#3a3f48',
            usb=(110, 70, 3), jack=[(780, 560), (820, 560), (860, 560)], batteria=[880, 470, 930, 520],
            psu=[990, 60, 1170, 240], cavi=False, disco=('ssd', 990, 380, 180, 240), cavo_sata=[(990, 500), (950, 500), (900, 540), (860, 540)],
            sottili=[[(260, 450), (260, 520)], [(380, 380), (380, 450), (450, 450)]], chiave='bus'),
}


def disegna_pc(path, num):
    return scheda(path, VARIANTI[num])


# ---------------------------------------------------------------- nomi delle zone e spec
IMG_V = 2   # versione delle immagini: finisce nell'indirizzo (img/x.png?v=2) per non vedere la copia vecchia in cache

NOMI = {
    'bibliotecario': ('il bibliotecario', 'أمين المكتبة', '图书管理员'),
    'banco_prestiti': ('il banco prestiti', 'مكتب الإعارة', '借书台'),
    'tavolo_lettura': ('il tavolo di lettura', 'طاولة القراءة', '阅读桌'),
    'tavolo_vuoto': ('il tavolo vuoto', 'الطاولة الفارغة', '空桌子'),
    'tavolo_a': ('il tavolo di lettura a sinistra', 'طاولة القراءة على اليسار', '左边的阅读桌'),
    'tavolo_b': ('il tavolo di lettura davanti', 'طاولة القراءة في المقدمة', '前面的阅读桌'),
    'tavolo_c': ('il tavolo di lettura a destra', 'طاولة القراءة على اليمين', '右边的阅读桌'),
    'scaffali': ('gli scaffali', 'الرفوف', '书架'),
    'scaffali_sinistra': ('gli scaffali a sinistra', 'الرفوف على اليسار', '左边的书架'),
    'scaffali_destra': ('gli scaffali a destra', 'الرفوف على اليمين', '右边的书架'),
    'scaffale_scatoloni': ('lo scaffale con gli scatoloni', 'الرف الذي عليه الصناديق', '放纸箱的架子'),
    'corridoio': ('il corridoio', 'الممر', '走廊'),
    'stampante': ('la stampante', 'الطابعة', '打印机'),
    'fotocopiatrice': ('la fotocopiatrice', 'آلة التصوير', '复印机'),
    'pianta': ('la pianta', 'النبتة', '植物'),
    'carrello_a': ('il carrello a sinistra', 'العربة على اليسار', '左边的推车'),
    'carrello_b': ('il carrello a destra', 'العربة على اليمين', '右边的推车'),
    'addetto': ('la persona del magazzino', 'عامل المخزن', '仓库工作人员'),
    'cpu': ('la CPU', 'المعالج (CPU)', '处理器（CPU）'),
    'ram': ('la RAM', 'الرام (RAM)', '内存（RAM）'),
    'disco': ('il disco', 'القرص', '硬盘'),
    'bus': ('le piste (il bus)', 'المسارات (الناقل)', '电路走线（总线）'),
    'psu': ('l’alimentatore', 'مزود الطاقة', '电源'),
    'usb': ('le porte USB', 'منافذ USB', 'USB接口'),
    'chipset': ('il chip centrale', 'الشريحة الوسطى', '中间的芯片'),
    'pcie': ('le fessure lunghe', 'الفتحات الطويلة', '长插槽'),
    'cond': ('i condensatori', 'المكثفات', '电容'),
    'batteria': ('la pila rotonda', 'البطارية المستديرة', '圆形电池'),
    'jack': ('le uscite audio', 'مخارج الصوت', '音频接口'),
}


def nome(k):
    t = NOMI[k]
    return {'it': t[0], 'ar': t[1], 'zh': t[2]}


def zone_lista(z):
    out = []
    for k, r in z.items():
        r = [max(0, int(round(r[0]))), max(0, int(round(r[1]))), min(W, int(round(r[2]))), min(H, int(round(r[3])))]
        out.append({'id': k, 'rett': r, 'nome': nome(k)})
    return out


def inter(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))


def controlla_zone(sigla, z, avvisi):
    """Segnala le zone che si sovrappongono troppo (un bersaglio non deve stare dentro un'altra zona) e le distanze tavolo/scaffali."""
    ks = list(z)
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            a, b = z[ks[i]], z[ks[j]]
            o = inter(a, b)
            if o:
                fa = o / float((a[2] - a[0]) * (a[3] - a[1])); fb = o / float((b[2] - b[0]) * (b[3] - b[1]))
                if max(fa, fb) > 0.15:
                    avvisi.append('%s: %s e %s si sovrappongono (%.0f%% / %.0f%%)' % (sigla, ks[i], ks[j], fa * 100, fb * 100))
    for t in ks:
        if t.startswith('tavolo'):
            for s_ in ks:
                if s_.startswith('scaffal'):
                    a, b = z[t], z[s_]
                    dx = max(0, max(a[0], b[0]) - min(a[2], b[2])); dy = max(0, max(a[1], b[1]) - min(a[3], b[3]))
                    if (dx * dx + dy * dy) ** .5 < 40:
                        avvisi.append('%s: %s e a meno di 40 px da %s' % (sigla, t, s_))


# (immagine, scena, bersaglio, testo it/ar/zh)
PASSI = [
    (1, 'bibliotecario', {
        'it': 'Questa è una biblioteca. Con la penna rossa fai un cerchio intorno a chi fa il lavoro della CPU: chi lavora, prende i libri e fa le cose.',
        'ar': 'هذه مكتبة. ارسم بالقلم الأحمر دائرة حول من يقوم بعمل المعالج (CPU): الشخص الذي يعمل ويأخذ الكتب وينفذ الأشياء.',
        'zh': '这是一个图书馆。用红笔圈出相当于处理器（CPU）的人：干活的人，拿书、做事情。'}),
    (2, 'tavolo_lettura', {
        'it': 'Fai un cerchio intorno al posto che fa il lavoro della RAM: dove appoggi i libri che usi ADESSO.',
        'ar': 'ارسم دائرة حول المكان الذي يقوم بعمل الرام (RAM): المكان الذي تضع عليه الكتب التي تستخدمها الآن.',
        'zh': '圈出相当于内存（RAM）的地方：你把现在正在用的书放在哪里。'}),
    (3, 'scaffali', {
        'it': 'Fai un cerchio intorno al posto che fa il lavoro dell’hard disk o dell’SSD: dove stanno TUTTI i libri, anche a biblioteca chiusa.',
        'ar': 'ارسم دائرة حول المكان الذي يقوم بعمل القرص الصلب أو SSD: المكان الذي توجد فيه كل الكتب، حتى عندما تكون المكتبة مغلقة.',
        'zh': '圈出相当于硬盘或固态硬盘（SSD）的地方：所有的书都放在那里，就算图书馆关门也在。'}),
    (4, 'corridoio', {
        'it': 'Fai un cerchio intorno al posto che fa il lavoro del bus: le strade dove passano i libri da un posto all’altro.',
        'ar': 'ارسم دائرة حول المكان الذي يقوم بعمل الناقل (bus): الطرق التي تمر فيها الكتب من مكان إلى آخر.',
        'zh': '圈出相当于总线（bus）的地方：书从一个地方运到另一个地方的路。'}),
    (5, 'cpu', {
        'it': 'Questo è l’interno di un PC visto dall’alto. Fai un cerchio intorno all’elemento che sei TU nel PC quando sei in biblioteca a fare una ricerca.',
        'ar': 'هذا هو الجزء الداخلي من الكمبيوتر من الأعلى. ارسم دائرة حول العنصر الذي تكون أنت في الكمبيوتر عندما تكون في المكتبة وتبحث عن شيء.',
        'zh': '这是从上面看到的电脑内部。圈出当你在图书馆查资料时，在电脑里相当于“你”的那一个部件。'}),
    (6, 'ram', {
        'it': 'Questo è l’interno di un altro PC. Fai un cerchio intorno a dove appoggi i libri che stai usando ADESSO.',
        'ar': 'هذا هو الجزء الداخلي من كمبيوتر آخر. ارسم دائرة حول المكان الذي تضع فيه الكتب التي تستخدمها الآن.',
        'zh': '这是另一台电脑的内部。圈出你把现在正在用的书放在哪里。'}),
    (7, 'disco', {
        'it': 'Questo è l’interno di un terzo PC. Fai un cerchio intorno a dove stanno tutti i libri anche a biblioteca chiusa.',
        'ar': 'هذا هو الجزء الداخلي من كمبيوتر ثالث. ارسم دائرة حول المكان الذي توجد فيه كل الكتب حتى عندما تكون المكتبة مغلقة.',
        'zh': '这是第三台电脑的内部。圈出所有的书放在哪里，就算图书馆关门也在。'}),
    (8, 'bus', {
        'it': 'Questo è l’interno di un quarto PC. Fai un cerchio intorno alle strade dove passano i libri da un posto all’altro.',
        'ar': 'هذا هو الجزء الداخلي من كمبيوتر رابع. ارسم دائرة حول الطرق التي تمر فيها الكتب من مكان إلى آخر.',
        'zh': '这是第四台电脑的内部。圈出书从一个地方运到另一个地方的路。'}),
]
SCENE = {1: scena1, 2: scena2, 3: scena3, 4: scena4}

# compito «biblioteca» (stessa immagine, 4 passi): scaffali, tavolo, bibliotecario, corridoio
BIB = [
    ('scaffali', {
        'it': 'Una biblioteca è come un computer. Con la penna rossa fai un cerchio intorno a quello che fa il lavoro dell’hard disk: dove stanno TUTTI i libri, anche a biblioteca chiusa.',
        'ar': 'المكتبة تشبه الكمبيوتر. ارسم بالقلم الأحمر دائرة حول ما يقوم بعمل القرص الصلب: المكان الذي توجد فيه كل الكتب، حتى عندما تكون المكتبة مغلقة.',
        'zh': '图书馆就像一台电脑。用红笔圈出相当于硬盘的东西：所有的书都放在那里，就算图书馆关门也在。'}),
    ('tavolo_lettura', {
        'it': 'Fai un cerchio intorno a quello che fa il lavoro della RAM: dove appoggi i libri che usi ADESSO.',
        'ar': 'ارسم دائرة حول ما يقوم بعمل الرام (RAM): المكان الذي تضع عليه الكتب التي تستخدمها الآن.',
        'zh': '圈出相当于内存（RAM）的东西：你把现在正在用的书放在哪里。'}),
    ('bibliotecario', {
        'it': 'Fai un cerchio intorno a quello che fa il lavoro della CPU: chi lavora, prende i libri e fa le cose.',
        'ar': 'ارسم دائرة حول ما يقوم بعمل المعالج (CPU): من يعمل ويأخذ الكتب وينفذ الأشياء.',
        'zh': '圈出相当于处理器（CPU）的东西：干活的人，拿书、做事情。'}),
    ('corridoio', {
        'it': 'Fai un cerchio intorno a quello che fa il lavoro del bus: le strade dove passano i libri da un posto all’altro.',
        'ar': 'ارسم دائرة حول ما يقوم بعمل الناقل (bus): الطرق التي تمر فيها الكتب من مكان إلى آخر.',
        'zh': '圈出相当于总线（bus）的东西：书从一个地方运到另一个地方的路。'}),
]


def passo(pid, sfondo, zone, bers, testo):
    return {'id': pid, 'tipo': 'cerchia', 'sfondo': '%s?v=%d' % (sfondo, IMG_V), 'penna': 'rosso', 'testo': testo,
            'zone': zone_lista(zone), 'bersaglio': bers,
            'copertura_min': 0.6, 'margine': 0.15, 'dimensione_max': 6}


def scrivi(path, obj):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1); fh.write('\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--riservato', default='/home/user/corso-informatica-riservato')
    a = ap.parse_args()
    img = os.path.join(RADICE, 'docs', 'lavagna', 'img'); os.makedirs(img, exist_ok=True)
    spec_dir = os.path.join(RADICE, 'docs', 'lavagna', 'spec'); os.makedirs(spec_dir, exist_ok=True)
    avvisi = []; tutte = {}
    z0 = scena0(os.path.join(img, 'biblioteca.png'), random.Random(99)); tutte['biblioteca'] = z0
    controlla_zone('biblioteca', z0, avvisi)
    shutil.copy(os.path.join(img, 'biblioteca.png'), os.path.join(RADICE, 'docs', 'lavagna', 'biblioteca.png'))
    passi = []
    for num, bers, testo in PASSI:
        f = os.path.join(img, 'bibpc-%02d.png' % num)
        z = SCENE[num](f, random.Random(100 + num)) if num <= 4 else disegna_pc(f, num)
        tutte['bibpc-%02d' % num] = z
        controlla_zone('bibpc-%02d' % num, z, avvisi)
        passi.append(passo('bp-%02d' % num, 'img/bibpc-%02d.png' % num, z, bers, testo))
    l3 = ['it', 'ar', 'zh']
    scrivi(os.path.join(spec_dir, 'biblioteca-pc-1inf-ora6.json'), {
        'id': 'biblioteca-pc-1inf-ora6', 'versione': '1.1', 'classe': '1INF', 'lingue': l3,
        'titolo': {'it': 'Lavagna: biblioteca e PC (8 domande)', 'ar': 'السبورة: المكتبة والكمبيوتر (8 أسئلة)', 'zh': '白板：图书馆和电脑（8个问题）'},
        'sfondo': 'img/bibpc-01.png?v=%d' % IMG_V, 'dimensioni': [W, H], 'penne': ['rosso', 'blu', 'nero'], 'tentativi_max': 3,
        'ordine': 'casuale', 'passi': passi})
    bp = [passo('b-%02d' % (k + 1), 'img/biblioteca.png', z0, bers, testo) for k, (bers, testo) in enumerate(BIB)]
    scrivi(os.path.join(spec_dir, 'biblioteca-1inf-ora6.json'), {
        'id': 'biblioteca-1inf-ora6', 'versione': '2.0', 'classe': '1INF', 'lingue': l3,
        'titolo': {'it': 'Lavagna: la biblioteca del computer', 'ar': 'السبورة: مكتبة الكمبيوتر', 'zh': '白板：电脑的图书馆'},
        'sfondo': 'img/biblioteca.png?v=%d' % IMG_V, 'dimensioni': [W, H], 'penne': ['rosso', 'blu', 'nero'], 'tentativi_max': 3,
        'ordine': 'fisso', 'passi': bp})
    for x in avvisi:
        print('AVVISO', x)
    if os.path.isdir(a.riservato):
        dst = os.path.join(a.riservato, 'lavagne', '1INF', 'bibpc-originali'); os.makedirs(dst, exist_ok=True)
        for num in range(1, 9):
            shutil.copy(os.path.join(img, 'bibpc-%02d.png' % num), dst)
        shutil.copy(os.path.join(img, 'biblioteca.png'), dst)
        scrivi(os.path.join(dst, 'zone.json'), {k: {i: [int(v) for v in r] for i, r in z.items()} for k, z in tutte.items()})
        print('copiate nel riservato:', dst)
    print('immagini e spec scritte; avvisi:', len(avvisi))


if __name__ == '__main__':
    sys.exit(main())
