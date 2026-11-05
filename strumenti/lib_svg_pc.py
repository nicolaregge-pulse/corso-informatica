"""Schemi SVG disegnati (dichiarati come schemi, non screenshot) per la lezione «smonta, rimonta, installa» del PC.

Usato da strumenti/genera_lezione_pc.py (2INF e 3INF, 05/11/2026). Ogni funzione restituisce il testo di un file .svg
720 x 400, con sfondo proprio (si legge anche con il tema scuro della pagina).
"""
from xml.sax.saxutils import escape

W, H = 720, 400
ROSSO, VERDE, BLU, GRIGIO = '#c0392b', '#1a7f37', '#1f6feb', '#8c959f'


def _svg(corpo, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{escape(titolo)}" font-family="Segoe UI, Arial, sans-serif">'
            '<defs><marker id="fr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ROSSO}"/></marker></defs>'
            f'<rect width="{W}" height="{H}" fill="#f4f6f9"/>{corpo}'
            f'<text x="{W - 8}" y="{H - 6}" font-size="11" fill="#6e7781" text-anchor="end">schema disegnato</text></svg>\n')


def t(x, y, s, size=18, fill='#1f2328', bold=False, anchor='start'):
    fw = ' font-weight="700"' if bold else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{fw}>{escape(s)}</text>'


def r(x, y, w, h, fill='#fff', stroke=GRIGIO, sw=2, rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def freccia(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ROSSO}" stroke-width="4" marker-end="url(#fr)"/>'


def lettera(x, y, s):
    return (f'<circle cx="{x}" cy="{y}" r="15" fill="{ROSSO}" stroke="#fff" stroke-width="2"/>'
            + t(x, y + 6, s, 17, '#fff', True, 'middle'))


def finestra(titolo, elementi, barra='#1f6feb'):
    """Schermata tipo: una finestra con titolo e elementi.
    elementi: ('t', x, y, testo[, size, bold]) testo; ('b', x, y, w, etichetta, evidenzia) bottone;
    ('c', x, y, w, etichetta, valore) casella; ('k', x, y, etichetta, spuntata, evidenzia) spunta;
    ('a', x1, y1, x2, y2) freccia rossa; ('n', x, y, testo) nota rossa; ('r', x, y, w, h, colore) rettangolo;
    ('v', x, y, w, testo, evidenzia) voce di elenco (riga cliccabile)."""
    c = [r(20, 18, 680, 362, '#fff', GRIGIO, 2, 8), f'<rect x="20" y="18" width="680" height="34" rx="8" fill="{barra}"/>',
         f'<rect x="20" y="40" width="680" height="12" fill="{barra}"/>', t(36, 41, titolo, 17, '#fff', True)]
    for e in elementi:
        k = e[0]
        if k == 't':
            c.append(t(e[1], e[2], e[3], e[4] if len(e) > 4 else 17, '#1f2328', e[5] if len(e) > 5 else False))
        elif k == 'n':
            c.append(t(e[1], e[2], e[3], 16, ROSSO, True))
        elif k == 'b':
            _, x, y, w, lab, ev = e
            c.append(r(x, y, w, 36, VERDE if ev else '#e6edf3', ROSSO if ev else GRIGIO, 4 if ev else 1.5, 6))
            c.append(t(x + w / 2, y + 24, lab, 16, '#fff' if ev else '#1f2328', ev, 'middle'))
        elif k == 'c':
            _, x, y, w, lab, val = e
            c.append(t(x, y, lab, 15, '#5b6573'))
            c.append(r(x, y + 6, w, 32, '#fff', BLU, 2, 4))
            c.append(t(x + 8, y + 28, val, 16))
        elif k == 'k':
            _, x, y, lab, si, ev = e
            c.append(r(x, y - 16, 20, 20, '#fff', ROSSO if ev else '#57606a', 3 if ev else 2, 3))
            if si:
                c.append(f'<path d="M{x + 4},{y - 6} l5,6 l9,-12" fill="none" stroke="{VERDE}" stroke-width="3.5"/>')
            c.append(t(x + 30, y, lab, 16, '#1f2328', ev))
        elif k == 'v':
            _, x, y, w, lab, ev = e
            c.append(r(x, y, w, 30, '#ddf4ff' if ev else '#fff', ROSSO if ev else '#d0d7de', 3 if ev else 1, 4))
            c.append(t(x + 10, y + 21, lab, 15, '#1f2328', ev))
        elif k == 'a':
            c.append(freccia(*e[1:5]))
        elif k == 'r':
            c.append(r(e[1], e[2], e[3], e[4], e[5], e[5], 1, 4))
    return _svg(''.join(c), titolo)


def bios(titolo, righe, evid=None, nota=''):
    """Schermata tipo del BIOS/UEFI: blu con testo bianco. righe: [(etichetta, valore)]."""
    c = [r(20, 18, 680, 362, '#0b2a6f', '#0b2a6f', 2, 4), t(360, 48, titolo, 19, '#fff', True, 'middle'),
         '<line x1="36" y1="60" x2="684" y2="60" stroke="#9fb6e8" stroke-width="1.5"/>']
    y = 96
    for i, (a, b) in enumerate(righe):
        if evid is not None and i in evid:
            c.append(r(30, y - 24, 660, 34, '#1d4fbf', '#ffd33d', 3, 3))
        c.append(t(50, y, a, 17, '#cfe0ff'))
        c.append(t(330, y, b, 17, '#fff', True))
        y += 40
    c.append(t(360, 366, nota or 'F10 = Salva ed esci    Esc = Esci senza salvare', 15, '#ffd33d', True, 'middle'))
    return _svg(''.join(c), titolo)


# ---------------------------------------------------------------- disegni dell'hardware

def _case(x=70, y=40, w=420, h=330):
    return r(x, y, w, h, '#dfe3e8', '#57606a', 3, 8)


def componenti_lettere():
    """Interno del PC con 8 lettere da riconoscere (A-H)."""
    c = [_case()]
    c.append(r(110, 120, 300, 230, '#2d6a4f', '#1b4332', 2, 4))  # scheda madre H
    c.append(r(240, 150, 70, 70, '#adb5bd', '#495057', 2, 4))  # dissipatore A
    c.append('<circle cx="275" cy="185" r="26" fill="#6c757d" stroke="#343a40" stroke-width="2"/>')
    c.append('<circle cx="275" cy="185" r="6" fill="#343a40"/>')
    for i in range(4):  # RAM B
        c.append(r(330 + i * 14, 135, 8, 110, '#3a86ff' if i % 2 == 0 else '#1b4332', '#14213d', 1, 1))
    c.append(r(130, 285, 230, 24, '#212529', '#000', 1, 2))  # scheda video G
    c.append(r(130, 309, 60, 6, '#e9c46a', '#e9c46a', 1, 1))
    c.append(r(90, 52, 150, 60, '#495057', '#212529', 2, 4))  # alimentatore C
    c.append('<circle cx="140" cy="82" r="20" fill="#343a40"/>')
    c.append(r(420, 250, 60, 90, '#ced4da', '#495057', 2, 4))  # disco D (gabbia a destra)
    c.append(r(428, 262, 44, 66, '#adb5bd', '#495057', 1, 3))
    c.append('<path d="M428,300 C400,300 400,260 392,250" fill="none" stroke="#e63946" stroke-width="5"/>')  # SATA E
    c.append('<path d="M200,112 C210,140 390,110 398,170" fill="none" stroke="#f4a261" stroke-width="12" stroke-linecap="round"/>')  # 24 pin F
    c.append(r(392, 160, 14, 60, '#f4f4f4', '#495057', 1, 2))
    for s, x, y in (('A', 275, 140), ('B', 352, 128), ('C', 225, 66), ('D', 465, 248), ('E', 407, 285), ('F', 300, 118),
                    ('G', 170, 278), ('H', 140, 140)):
        c.append(lettera(x, y, s))
    c.append(t(510, 70, 'Trova le 8 lettere:', 17, '#1f2328', True))
    for i, s in enumerate(['A, B, C, D', 'E, F, G, H', '', 'Per ogni lettera', 'scegli il nome', 'nella scheda.']):
        c.append(t(510, 100 + i * 26, s, 16))
    return _svg(''.join(c), 'Interno del PC con 8 lettere')


def sicurezza(quale, pref='192.168.10.', primo=10):
    c = []
    if quale == 'spina':
        c.append(r(60, 120, 180, 200, '#dfe3e8', '#57606a', 3, 8))
        c.append(t(150, 110, 'PC', 18, '#1f2328', True, 'middle'))
        c.append('<path d="M240,250 C330,250 330,200 420,200" fill="none" stroke="#212529" stroke-width="8"/>')
        c.append(r(420, 180, 50, 40, '#495057', '#212529', 2, 4))
        c.append(r(520, 150, 120, 110, '#fff', '#57606a', 3, 10))
        c.append('<circle cx="565" cy="205" r="7" fill="#212529"/><circle cx="595" cy="205" r="7" fill="#212529"/>')
        c.append(freccia(470, 200, 510, 200))
        c.append('<line x1="400" y1="160" x2="500" y2="250" stroke="#c0392b" stroke-width="6"/>')
        c.append(t(360, 60, '1. Spegni il PC.  2. Togli la spina dalla presa.', 19, ROSSO, True, 'middle'))
        c.append(t(360, 350, 'Solo dopo apri il case.', 18, '#1f2328', True, 'middle'))
    elif quale == 'esd':
        c.append(_case(60, 90, 260, 260))
        c.append(r(60, 90, 30, 260, '#adb5bd', '#57606a', 2, 2))
        c.append('<circle cx="150" cy="210" r="34" fill="#f1c27d" stroke="#8d5524" stroke-width="2"/>')
        c.append(t(150, 216, 'mano', 15, '#5b3a1a', True, 'middle'))
        c.append(freccia(150, 176, 95, 150))
        c.append(t(360, 120, 'Prima di toccare i pezzi:', 19, '#1f2328', True))
        c.append(t(360, 160, 'tocca il metallo del case', 18))
        c.append(t(360, 190, '(oppure metti il braccialetto', 18))
        c.append(t(360, 220, 'antistatico, se c\'è).', 18))
        c.append(t(360, 270, 'Così scarichi l\'elettricità', 18, ROSSO, True))
        c.append(t(360, 300, 'statica e non rompi la RAM.', 18, ROSSO, True))
    elif quale == 'viti':
        c.append(r(80, 200, 260, 120, '#e9c46a', '#a47d1a', 3, 8))
        c.append(t(210, 270, 'SCATOLA DELLE VITI', 17, '#5c4400', True, 'middle'))
        for i in range(6):
            x = 120 + i * 35
            c.append(f'<g transform="translate({x},160)"><circle r="9" fill="#adb5bd" stroke="#495057" stroke-width="2"/>'
                     '<line x1="-5" y1="0" x2="5" y2="0" stroke="#495057" stroke-width="2"/><line x1="0" y1="-5" x2="0" y2="5" stroke="#495057" stroke-width="2"/>'
                     '<rect x="-2" y="9" width="4" height="18" fill="#868e96"/></g>')
        c.append(freccia(210, 190, 210, 215))
        c.append(t(390, 150, 'Ogni vite va subito', 19, '#1f2328', True))
        c.append(t(390, 180, 'nella scatola.', 19, '#1f2328', True))
        c.append(t(390, 230, 'Niente viti sul tavolo', 18))
        c.append(t(390, 258, 'e niente viti dentro il PC:', 18))
        c.append(t(390, 286, 'una vite libera fa un corto.', 18, ROSSO, True))
    elif quale == 'mappa':
        c.append(r(60, 70, 300, 280, '#2d6a4f', '#1b4332', 2, 6))
        c.append(r(300, 110, 40, 120, '#f4f4f4', '#495057', 2, 2))
        c.append(t(320, 250, '24 pin', 14, '#fff', True, 'middle'))
        c.append(r(100, 90, 50, 26, '#f4f4f4', '#495057', 2, 2))
        c.append(t(125, 135, 'CPU 4/8', 14, '#fff', True, 'middle'))
        for i in range(3):
            c.append(r(270 - i * 30, 300, 22, 26, '#e63946', '#7d1d24', 1, 2))
        c.append(t(240, 345, 'SATA', 14, '#fff', True, 'middle'))
        c.append(r(90, 300, 120, 30, '#212529', '#000', 1, 2))
        c.append(t(150, 292, 'pannello frontale', 13, '#fff', True, 'middle'))
        c.append(t(390, 100, 'Prima di staccare un cavo:', 18, '#1f2328', True))
        c.append(t(390, 135, '1. guarda dove è attaccato;', 17))
        c.append(t(390, 165, '2. segnalo nella MAPPA DEI', 17))
        c.append(t(390, 195, '    CAVI della scheda;', 17))
        c.append(t(390, 225, '3. poi tira dalla spina,', 17))
        c.append(t(390, 255, '    MAI dal filo.', 17, ROSSO, True))
        c.append(t(390, 300, 'Lavorate a coppie:', 17, BLU, True))
        c.append(t(390, 328, 'guardate insieme, poi staccate.', 17, BLU, True))
    elif quale == 'ruoli':
        # 05/11/2026 (docente): niente ruoli, solo «a coppie, un PC per coppia»
        c.append(t(360, 60, 'A coppie: un PC per coppia', 24, '#1f2328', True, 'middle'))
        for x in (150, 570):
            c.append(f'<circle cx="{x}" cy="150" r="34" fill="{BLU}"/>')
            c.append(r(x - 50, 190, 100, 110, BLU, BLU, 2, 30))
        c.append(r(290, 150, 140, 150, '#dfe3e8', '#57606a', 3, 8))
        c.append(t(360, 232, 'PC', 22, '#1f2328', True, 'middle'))
        c.append(t(360, 360, 'Scrivete i nomi e il numero del banco.', 18, ROSSO, True, 'middle'))
    elif quale == 'apri-case':
        c.append(r(160, 60, 260, 300, '#dfe3e8', '#57606a', 3, 8))
        c.append(r(420, 70, 30, 280, '#adb5bd', '#57606a', 2, 4))
        for y in (100, 320):
            c.append(f'<circle cx="435" cy="{y}" r="9" fill="#868e96" stroke="#343a40" stroke-width="2"/>')
            c.append(freccia(520, y, 452, y))
        c.append(t(530, 105, 'vite 1', 17, ROSSO, True))
        c.append(t(530, 325, 'vite 2', 17, ROSSO, True))
        c.append(t(290, 200, 'retro del PC', 17, '#1f2328', True, 'middle'))
        c.append(t(60, 390 - 12, 'Svita le 2 viti dietro, poi fai scorrere il pannello laterale verso il retro.', 16, '#1f2328'))
    elif quale == 'ram':
        c.append(r(80, 160, 560, 70, '#1b4332', '#081c15', 2, 4))
        for i in range(8):
            c.append(r(110 + i * 62, 175, 40, 40, '#212529', '#000', 1, 2))
        c.append(r(80, 230, 560, 14, '#e9c46a', '#a47d1a', 1, 1))
        c.append(f'<rect x="330" y="230" width="14" height="14" fill="#f4f6f9"/>')
        c.append(freccia(337, 310, 337, 252))
        c.append(t(337, 335, 'la TACCA: va dove c\'è il dentino dello slot', 17, ROSSO, True, 'middle'))
        c.append(r(40, 120, 26, 140, '#ced4da', '#495057', 2, 4))
        c.append(r(654, 120, 26, 140, '#ced4da', '#495057', 2, 4))
        c.append(t(53, 110, 'gancio', 14, '#1f2328', True, 'middle'))
        c.append(t(667, 110, 'gancio', 14, '#1f2328', True, 'middle'))
        c.append(t(360, 70, 'Apri i ganci. Spingi la RAM dritta con due pollici', 18, '#1f2328', True, 'middle'))
        c.append(t(360, 96, 'fino al «clic»: i ganci si chiudono da soli.', 18, '#1f2328', True, 'middle'))
    elif quale == 'checklist':
        voci = ['RAM ben dentro, ganci chiusi', 'Disco avvitato al suo posto', 'Disco: cavo SATA dati attaccato',
                'Disco: cavo SATA alimentazione attaccato', 'Nessuna vite libera nel case']
        c.append(t(60, 70, 'Prima di accendere: 5 controlli', 21, '#1f2328', True))
        for i, v in enumerate(voci):
            y = 120 + i * 50
            c.append(r(60, y - 22, 28, 28, '#fff', VERDE, 3, 4))
            c.append(f'<path d="M66,{y - 8} l7,8 l12,-16" fill="none" stroke="{VERDE}" stroke-width="4"/>')
            c.append(t(104, y, v, 19))
        c.append(t(60, 380 - 8, 'Se un controllo è NO: non accendere, sistema prima.', 17, ROSSO, True))
    elif quale == 'collega':
        c.append(r(60, 80, 150, 250, '#dfe3e8', '#57606a', 3, 8))
        c.append(t(135, 70, 'retro del PC', 15, '#1f2328', True, 'middle'))
        for i, (s, col) in enumerate((('corrente', '#212529'), ('monitor', BLU), ('tastiera', '#6f42c1'), ('mouse', '#6f42c1'), ('rete', VERDE))):
            y = 120 + i * 42
            c.append(r(90, y - 12, 34, 20, col, col, 1, 3))
            c.append(f'<line x1="124" y1="{y - 2}" x2="300" y2="{y - 2}" stroke="{col}" stroke-width="5"/>')
            c.append(t(310, y + 4, s, 18, col, True))
        c.append(t(430, 150, 'Chiudi il case', 19, '#1f2328', True))
        c.append(t(430, 180, 'con le sue 2 viti.', 18))
        c.append(t(430, 230, 'Poi attacca i cavi:', 19, '#1f2328', True))
        c.append(t(430, 260, 'la corrente per ultima.', 18, ROSSO, True))
    elif quale == 'tasti-bios':
        tasti = [('Canc', True), ('F2', True), ('F12', False), ('Esc', False), ('F10', False)]
        for i, (s, ev) in enumerate(tasti):
            x = 70 + i * 120
            c.append(r(x, 150, 90, 70, '#fff', ROSSO if ev else '#57606a', 4 if ev else 2, 10))
            c.append(t(x + 45, 195, s, 24, ROSSO if ev else '#1f2328', True, 'middle'))
        c.append(t(360, 80, 'Accendi e premi SUBITO, più volte, il tasto del BIOS:', 18, '#1f2328', True, 'middle'))
        c.append(t(360, 110, 'di solito Canc (Del) oppure F2. Lo scrive lo schermo all\'avvio.', 17, '#1f2328', False, 'middle'))
        c.append(t(360, 270, 'F12 (o Esc) = menu di avvio: scegli da dove parte il PC, una volta sola.', 17, '#1f2328', False, 'middle'))
        c.append(t(360, 300, 'F10 = salva ed esci dal BIOS.', 17, '#1f2328', False, 'middle'))
    elif quale == 'rete':
        c.append(r(280, 60, 160, 50, '#e6edf3', '#57606a', 2, 6))
        c.append(t(360, 92, 'SWITCH', 18, '#1f2328', True, 'middle'))
        pcs = [('PC accanto (banco 1)', pref + str(primo + 1), 110), ('Il vostro PC (banco 2)', pref + str(primo + 2), 360), ('Altro PC (banco 3)', pref + str(primo + 3), 610)]
        for nome, ip, x in pcs:
            ev = nome.startswith('Il vostro PC')
            c.append(f'<line x1="{x}" y1="210" x2="360" y2="110" stroke="{VERDE}" stroke-width="4"/>')
            c.append(r(x - 95, 210, 190, 80, '#ddf4ff' if ev else '#fff', ROSSO if ev else '#57606a', 4 if ev else 2, 8))
            c.append(t(x, 238, nome, 16, '#1f2328', True, 'middle'))
            c.append(t(x, 270, ip, 17, ROSSO if ev else '#1f2328', True, 'middle'))
        c.append(t(40, 320, 'Indirizzo IP: le prime 3 parti UGUALI (stessa rete), l\'ultima DIVERSA (ogni PC il suo).', 15, '#1f2328', True))
        c.append(t(40, 345, 'Maschera 255.255.255.0 = le prime 3 parti dicono la rete.', 15))
        c.append(t(40, 370, 'Gateway = la porta verso fuori (router).  DNS = la rubrica dei nomi (google.com).', 15))
    return _svg(''.join(c), quale)


def ordine(titolo, passi, inverso=False):
    c = [t(360, 50, titolo, 20, '#1f2328', True, 'middle')]
    n = len(passi)
    w = 640 // n
    for i, s in enumerate(passi):
        x = 40 + i * w
        c.append(r(x, 120, w - 24, 120, '#fff', BLU, 3, 10))
        c.append(f'<circle cx="{x + 22}" cy="120" r="16" fill="{BLU}"/>')
        c.append(t(x + 22, 126, str(i + 1), 16, '#fff', True, 'middle'))
        parole = s.split(' ')
        righe, cur = [], ''
        for p in parole:
            if len(cur) + len(p) > 8 and cur:
                righe.append(cur)
                cur = p
            else:
                cur = (cur + ' ' + p).strip()
        righe.append(cur)
        for j, rr in enumerate(righe[:4]):
            c.append(t(x + (w - 24) / 2, 165 + j * 22, rr, 15, '#1f2328', j == 0, 'middle'))
        if i < n - 1:
            c.append(freccia(x + w - 22, 180, x + w - 2, 180))
    c.append(t(360, 300, 'Rimontare = stesso elenco, al contrario (da destra a sinistra).' if not inverso
               else 'È l\'ordine dello smontaggio letto al contrario.', 17, ROSSO, True, 'middle'))
    c.append(t(360, 335, 'CPU e ventola (dissipatore): NON si toccano.', 17, '#1f2328', True, 'middle'))
    return _svg(''.join(c), titolo)


def consegna():
    return finestra('Scheda della coppia', [
        ('t', 40, 90, 'Compila la scheda in fondo alla pagina.', 18, True),
        ('c', 40, 120, 300, 'Il tuo nome e cognome', 'Nome Cognome'),
        ('c', 380, 120, 300, 'Il compagno', 'Nome Cognome'),
        ('t', 40, 210, 'Poi premi il bottone verde:'),
        ('b', 40, 230, 300, 'Manda al prof', True),
        ('a', 420, 248, 350, 248),
        ('t', 430, 254, 'un clic solo'),
        ('t', 40, 320, 'Si apre una scheda «Consegna arrivata al prof»: hai finito.'),
    ])


def quiz():
    return finestra('Quiz su Moduli Google', [
        ('t', 40, 90, '8 domande. Servono 6 giuste. Puoi rifarlo.', 18, True),
        ('v', 40, 115, 640, '1) Che cosa fa la RAM?', False),
        ('k', 60, 175, 'tiene i dati mentre il PC è acceso', True, True),
        ('k', 60, 210, 'tiene i dati anche a PC spento', False, False),
        ('k', 60, 245, 'dà la corrente ai pezzi', False, False),
        ('b', 500, 310, 160, 'Invia', True),
    ])
