#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lavagne A4 orizzontali del 04/11/2026: 3INF (ora 1 riusa lavagna.html + 5 pagine ora 2) e 2INF (Sicurezza 6a ora).
Una idea per pagina, poche parole, grandi disegni. Nessun nome di allievo. PDF con playwright (come _build/pdf.py)."""
import os, re, subprocess, sys
from xml.sax.saxutils import escape as E
B3 = '/home/user/corso-informatica/classe-3/lezioni-bozza/2026-11-04_protocollo-rete/'
B2 = '/home/user/corso-informatica/classe-2/lezioni-bozza/2026-11-04_sicurezza/'
F = 'font-family="system-ui,Segoe UI,Arial,sans-serif"'
def svg(body): return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400"><rect width="1000" height="400" fill="#fff"/>%s</svg>' % body
def t(x, y, s, sz=44, fill='#1d1d1f', a='middle', b=True): return '<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" %s%s>%s</text>' % (x, y, sz, fill, a, F, ' font-weight="700"' if b else '', E(s))
def bx(x, y, w, h, fill='#eaf3fb', st='#0b5fa5', r=16): return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="6"/>' % (x, y, w, h, r, fill, st)
def ar(x1, y1, x2, y2, c='#1d1d1f'): return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="8"/><polygon points="%s,%s %s,%s %s,%s" fill="%s"/>' % (x1, y1, x2 - 18 if x2 > x1 else x2 + 18, y2, c, x2, y2, x2 - 30 if x2 > x1 else x2 + 30, y2 - 16, x2 - 30 if x2 > x1 else x2 + 30, y2 + 16, c)
def pag(n, titolo, fig, parole): return '<section class="pg"><div class="n">%d</div><h1>%s</h1><div class="fig">%s</div><p class="w">%s</p></section>' % (n, E(titolo), fig, E(parole))
CSS = ('@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Segoe UI",Arial,sans-serif;color:#1d1d1f;background:#fff}'
       '.pg{width:297mm;height:210mm;padding:10mm 14mm;page-break-after:always;position:relative;overflow:hidden}.pg h1{font-size:40pt;margin:0 0 4mm;line-height:1.1}'
       '.pg .n{position:absolute;right:12mm;top:8mm;font-size:18pt;color:#9a9384}.fig svg{width:100%;height:auto;display:block;max-height:150mm}.w{font-size:28pt;margin:4mm 0 0;color:#444;text-align:center}')
def doc(titolo, pages): return '<!doctype html><html lang="it"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s</body></html>' % (E(titolo), CSS, ''.join(pages))
def pdf(src, out):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox']); pg = b.new_page()
        pg.goto('file://' + src); pg.wait_for_timeout(300); pg.pdf(path=out, format='A4', landscape=True, print_background=True, prefer_css_page_size=True); b.close()

# ---------------- 3INF: ora 1 dal file esistente + ora 2
old = open(B3 + 'lavagna.html', encoding='utf-8').read()
sez = re.findall(r'<section class="pg">.*?</section>', old, flags=re.S)
sez = [s for s in sez if 'Tocca a te' not in s]   # l'ultima pagina dell'ora 1 resta: la ripetiamo come chiusura ora 1
sez = re.findall(r'<section class="pg">.*?</section>', old, flags=re.S)
n = len(sez)
o2 = []
o2.append(pag(n + 1, 'ORA 2 · Il client vero', svg(bx(60, 60, 380, 280) + t(250, 170, 'Apri il progetto', 46) + t(250, 235, 'Client ▸', 38, '#5d5a52') + t(250, 285, 'ClientMastermind.lpi', 34, '#0b5fa5') + ar(450, 200, 560, 200) + bx(570, 60, 370, 280, '#e8f6ea', '#1a7f37') + t(755, 190, 'F9', 120, '#1a7f37') + t(755, 280, 'si parte!', 44)), 'Progetto ▸ Apri progetto ▸ Client. Poi premi F9.'))
o2.append(pag(n + 2, 'Collegati al Prof', svg(bx(40, 40, 420, 130) + t(250, 90, 'IP del server', 36, '#5d5a52') + t(250, 145, '(scritto alla lavagna)', 32) + bx(40, 200, 420, 130) + t(250, 250, 'Il TUO nome', 36, '#5d5a52') + t(250, 305, 'scrivilo tu', 32) + ar(480, 190, 600, 190) + bx(610, 120, 350, 140, '#e8f6ea', '#1a7f37') + t(785, 205, 'Connetti', 54, '#1a7f37')), 'In basso compare «Collegato!»: fatto.'))
o2.append(pag(n + 3, 'La partita di classe', svg(bx(40, 120, 260, 160, '#fbeee1', '#a24a00') + t(170, 215, 'SERVER', 44, '#a24a00') + ''.join(bx(560 + (i % 2) * 210, 40 + (i // 2) * 160, 190, 130) + t(655 + (i % 2) * 210, 120 + (i // 2) * 160, 'CLIENT', 34, '#0b5fa5') for i in range(4)) + ar(310, 160, 545, 100) + ar(310, 200, 545, 250) + t(170, 340, 'il Prof preme VIA', 36)), 'Stesso codice per tutti. Chi indovina prima, sale in classifica.'))
o2.append(pag(n + 4, 'Il commit su GitHub', svg(bx(40, 40, 920, 100, '#f2f2f2', '#888') + t(500, 108, 'github.com ▸ Add file ▸ Upload files', 44) + bx(40, 170, 920, 100, '#fff8d9', '#b8860b') + t(500, 238, 'Un messaggio che dice COSA hai fatto', 42) + bx(300, 300, 400, 80, '#e8f6ea', '#1a7f37') + t(500, 357, 'Commit changes', 44, '#1a7f37')), 'Messaggio chiaro = cosa e perché. Poi invii il link del commit.'))
o2.append(pag(n + 5, 'Il quiz sulla rete', svg(bx(60, 60, 880, 280, '#fff8d9', '#b8860b') + t(500, 190, '12 domande', 110, '#b8860b') + t(500, 290, 'per un buon voto: almeno 8', 52)), 'Su Moduli Google. Lavoro tuo: rispondi da solo.'))
open(B3 + 'lavagna-3inf-04-11.html', 'w', encoding='utf-8').write(old.replace('</body>', ''.join(o2) + '</body>'))
pdf(B3 + 'lavagna-3inf-04-11.html', B3 + 'lavagna-3inf-04-11.pdf')

# ---------------- 2INF: Sicurezza 6a ora
P = []
P.append(pag(1, 'Rischi meccanici ed elettrici', svg(bx(40, 60, 420, 280, '#fbeee1', '#a24a00') + t(250, 180, 'MACCHINE', 56, '#a24a00') + t(250, 250, 'parti che si muovono', 32, '#5d5a52') + bx(540, 60, 420, 280, '#fff8d9', '#b8860b') + t(750, 180, 'CORRENTE', 56, '#b8860b') + t(750, 250, 'passa nel corpo', 32, '#5d5a52')), 'Oggi, 6ª ora: due rischi che ci sono in ogni lavoro.'))
P.append(pag(2, 'Rischio meccanico', svg(''.join(bx(30 + i * 240, 60, 220, 150, '#fbeee1', '#a24a00') + t(140 + i * 240, 150, w, 30) for i, w in enumerate(['ingranaggi', 'cinghie', 'lame', 'rulli'])) + t(500, 290, 'parti di una macchina che si muovono', 46) + t(500, 350, 'anche un PC ha le ventole', 36, '#5d5a52')), 'Succede vicino a noi: stampanti, porte automatiche, carrelli.'))
P.append(pag(3, 'Come ci si fa male', svg(''.join(bx(20 + i * 196, 70, 180, 200, '#fde8e8', '#c0392b') + t(110 + i * 196, 185, w, 26) for i, w in enumerate(['schiaccia-', 'taglio', 'trascina-', 'cesoia-', 'proiezione'])) + ''.join(t(110 + i * 196, 225, w, 26, '#c0392b') for i, w in enumerate(['mento', '', 'mento', 'mento', ''])) + t(500, 350, 'sciarpe, cravatte e capelli lunghi: attenzione!', 38)), 'Cinque modi. Tieni lontane mani e vestiti.'))
P.append(pag(4, 'Le protezioni', svg(bx(20, 60, 230, 200, '#e8f6ea', '#1a7f37') + t(135, 150, 'RIPARO', 38, '#1a7f37') + t(135, 200, 'fisso', 38, '#1a7f37') + bx(270, 60, 230, 200, '#e8f6ea', '#1a7f37') + t(385, 150, 'INTERBLOCCO', 30, '#1a7f37') + t(385, 200, 'apri = si ferma', 28, '#1a7f37') + bx(520, 60, 230, 200, '#e8f6ea', '#1a7f37') + t(635, 150, 'SENSORI', 38, '#1a7f37') + t(635, 200, 'fotocellule', 30, '#1a7f37') + '<circle cx="875" cy="160" r="95" fill="#c0392b"/>' + t(875, 175, 'STOP', 52, '#fff') + t(500, 340, 'MAI togliere o bloccare una protezione', 44)), 'Il fungo rosso ferma tutto subito.'))
P.append(pag(5, 'Prima di pulire o riparare', svg(''.join(bx(20 + i * 245, 80, 225, 180, '#eaf3fb', '#0b5fa5') + t(132 + i * 245, 140, str(i + 1), 80, '#0b5fa5') + t(132 + i * 245, 215, w, 36) for i, w in enumerate(['FERMO', 'STACCO', 'CARTELLO', 'CONTROLLO'])) + t(500, 340, 'solo dopo ci metto le mani', 46)), 'Fermo · stacco l\'energia · cartello · controllo.'))
P.append(pag(6, 'Rischio elettrico', svg(bx(30, 60, 450, 260, '#fde8e8', '#c0392b') + t(255, 160, 'DIRETTO', 56, '#c0392b') + t(255, 230, 'tocchi un filo scoperto', 34) + bx(520, 60, 450, 260, '#fff8d9', '#b8860b') + t(745, 160, 'INDIRETTO', 56, '#b8860b') + t(745, 230, 'tocchi una carcassa', 34) + t(745, 275, 'andata in tensione per un guasto', 26, '#5d5a52')), 'Le prese di casa (230 volt) sono pericolose.'))
P.append(pag(7, 'Che cosa fa la corrente', svg(bx(30, 60, 290, 260, '#eaf3fb', '#0b5fa5') + t(175, 170, 'QUANTA', 50, '#0b5fa5') + t(175, 230, 'corrente', 36) + bx(355, 60, 290, 260, '#eaf3fb', '#0b5fa5') + t(500, 170, 'PER QUANTO', 42, '#0b5fa5') + t(500, 230, 'tempo', 36) + bx(680, 60, 290, 260, '#eaf3fb', '#0b5fa5') + t(825, 170, 'DOVE', 50, '#0b5fa5') + t(825, 230, 'passa: cuore!', 34)), 'Muscoli bloccati, ustioni, cuore. Mani bagnate = molto peggio.'))
P.append(pag(8, 'Come ti proteggi', svg(bx(30, 60, 290, 260, '#e8f6ea', '#1a7f37') + t(175, 160, 'ISOLAMENTO', 40, '#1a7f37') + t(175, 225, 'dei cavi', 36) + bx(355, 60, 290, 260, '#e8f6ea', '#1a7f37') + t(500, 160, 'MESSA', 46, '#1a7f37') + t(500, 225, 'A TERRA', 46, '#1a7f37') + bx(680, 60, 290, 260, '#e8f6ea', '#1a7f37') + t(825, 160, 'SALVAVITA', 40, '#1a7f37') + t(825, 225, 'differenziale', 32)), 'Niente cavi rovinati. Niente ciabatte in fila. Niente mani bagnate.'))
P.append(pag(9, 'Se succede', svg(''.join(bx(20 + i * 325, 70, 305, 230, '#fde8e8', '#c0392b') + t(172 + i * 325, 150, str(i + 1), 80, '#c0392b') + t(172 + i * 325, 230, w, 38) for i, w in enumerate(['TOLGO la corrente', 'NON tocco il collega', 'CHIAMO il 112']))), 'Spina o interruttore, mai le mani sul collega. Poi avvisi il preposto.'))
P.append(pag(10, 'Il quiz', svg(bx(60, 60, 880, 280, '#fff8d9', '#b8860b') + t(500, 190, '20 casi', 110, '#b8860b') + t(500, 290, '5 punti l\'uno · massimo 100', 50)), 'Su Moduli Google. Prova tua: rispondi da solo.'))
open(B2 + 'lavagna-2inf-04-11.html', 'w', encoding='utf-8').write(doc('Sicurezza 6ª ora alla lavagna', P))
pdf(B2 + 'lavagna-2inf-04-11.html', B2 + 'lavagna-2inf-04-11.pdf')
print('ok', n)
