#!/usr/bin/env python3
"""Genera la lezione 3INF del 04/11/2026 (protocollo di rete del Mastermind v4.0).
Uscite (nella cartella sopra): lezione.md, lezione.html (ora 1 + ora 2 bloccata), ora2.html,
img/*.svg, lavagna.html (+ PDF con shot/pdf), quiz-rete-12.json, quiz-rete-12.md.
BOZZA NON PUBBLICA: non finisce in docs/."""
import html, json, os
from xml.sax.saxutils import escape as E

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.makedirs(OUT + '/img', exist_ok=True)

COL = ['', '#DC2828', '#F0C81E', '#28A03C', '#285ADC', '#F0821E', '#8C32AA']
INK = '#1d1d1f'; MU = '#5d5a52'; BD = '#cfc8b8'; CB = '#0b5fa5'; SR = '#a24a00'; PAPER = '#fffdf8'
FONT = 'font-family="system-ui,Segoe UI,Arial,sans-serif"'
MONO = 'font-family="Consolas,Courier New,monospace"'


# ------------------------------------------------------------------ piccoli pezzi SVG
def svg(w, h, body, label):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-label="%s">'
            '<rect width="%d" height="%d" fill="%s"/>%s</svg>') % (w, h, E(label, {'"': '&quot;'}), w, h, PAPER, body)


def t(x, y, s, size=22, fill=INK, anchor='start', bold=False, mono=False):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" %s%s>%s</text>' % (
        x, y, size, fill, anchor, MONO if mono else FONT, ' font-weight="700"' if bold else '', E(s))


def box(x, y, w, h, fill='#fff', stroke=BD, sw=3, r=14):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, r, fill, stroke, sw)


def arrow(x1, y1, x2, y2, col=INK, sw=5):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = max(16, sw * 3)
    p1 = (x2 - L * math.cos(a - .45), y2 - L * math.sin(a - .45)); p2 = (x2 - L * math.cos(a + .45), y2 - L * math.sin(a + .45))
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"/>'
            '<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>') % (x1, y1, x2, y2, col, sw, x2, y2, p1[0], p1[1], p2[0], p2[1], col)


def peg(cx, cy, r, c):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="rgba(0,0,0,.35)" stroke-width="2"/>' % (cx, cy, r, c)


def chips(x, y, items, size=26, hi=None):
    """items = [(valore, etichetta)] -> casellette in fila"""
    out = ''; cx = x
    for i, (v, lab) in enumerate(items):
        w = max(len(v) * size * 0.62 + 24, len(lab) * 11 + 14)
        out += box(cx, y, w, 86, '#fff', CB if i == 0 else BD, 4 if i == 0 else 2, 10)
        out += t(cx + w / 2, y + 38, v, size, INK, 'middle', i == 0, True)
        out += t(cx + w / 2, y + 68, lab, 15, MU, 'middle')
        cx += w + 8
    return out, cx


def caption_schema(s):
    return s + '<text x="8" y="14" font-size="11" fill="#9a9384" %s>schema disegnato</text>' % FONT


# ------------------------------------------------------------------ gli schemi della teoria
def s_due_programmi():
    b = box(20, 30, 280, 220, '#eaf3fb', CB) + t(160, 70, 'CLIENT', 34, CB, 'middle', True) + t(160, 105, 'il programma di Sara', 20, MU, 'middle')
    b += box(60, 130, 200, 90, '#fff', BD) + t(160, 185, 'UnitRete', 26, INK, 'middle', True)
    b += box(700, 30, 280, 220, '#fbeee1', SR) + t(840, 70, 'SERVER', 34, SR, 'middle', True) + t(840, 105, 'il programma del Prof', 20, MU, 'middle')
    b += box(740, 130, 200, 90, '#fff', BD) + t(840, 168, 'porta', 22, MU, 'middle') + t(840, 205, '5050', 34, INK, 'middle', True, True)
    b += '<rect x="300" y="150" width="400" height="50" rx="25" fill="#d9d2c0" stroke="%s" stroke-width="3"/>' % BD
    b += t(500, 182, 'la rete (il tubo)', 24, MU, 'middle')
    b += t(500, 285, 'Si parlano scrivendosi righe di testo', 26, INK, 'middle', True)
    return svg(1000, 310, caption_schema(b), 'Schema: il client e il server collegati da un tubo, il server ascolta alla porta 5050')


def s_riga_va_torna():
    b = box(20, 30, 220, 200, '#eaf3fb', CB) + t(130, 75, 'CLIENT', 30, CB, 'middle', True)
    b += box(760, 30, 220, 200, '#fbeee1', SR) + t(870, 75, 'SERVER', 30, SR, 'middle', True)
    b += arrow(250, 90, 750, 90, CB) + box(310, 62, 380, 44, CB, CB, 1, 10) + t(500, 93, 'GUESS;Sara;1234', 26, '#fff', 'middle', True, True)
    b += arrow(750, 180, 250, 180, SR) + box(290, 152, 420, 44, SR, SR, 1, 10) + t(500, 183, 'RESULT;1;2;1;0;1;6;6', 26, '#fff', 'middle', True, True)
    b += t(500, 135, '1) UNA riga che va', 22, CB, 'middle', True) + t(500, 225, '2) UNA riga che torna', 22, SR, 'middle', True)
    b += t(500, 280, 'Poi la conversazione finisce. Per parlare ancora: di nuovo una riga che va.', 22, INK, 'middle')
    return svg(1000, 310, caption_schema(b), 'Schema: una riga va dal client al server e una riga torna')


def s_campi():
    x, y = 30, 40
    c1, end = chips(x, y, [('RESULT', 'tipo di risposta'), ('1', 'neri'), ('2', 'bianchi'), ('1', 'tentativi'), ('0', 'posto'), ('1', 'finiti'), ('6', 'migliore'), ('6', 'peggiore')], 28)
    b = c1
    # punti e virgola
    b += t(500, 175, 'I campi sono separati da  ;  (punto e virgola)', 28, INK, 'middle', True)
    b += t(500, 215, 'La riga finisce con un "a capo". Il primo campo dice che cosa è.', 22, MU, 'middle')
    b += t(500, 262, 'RESULT;1;2;1;0;1;6;6', 36, CB, 'middle', True, True)
    return svg(1000, 290, caption_schema(b), 'Schema: la riga RESULT;1;2;1;0;1;6;6 divisa nei suoi campi')


def s_domande_risposte():
    b = box(20, 20, 300, 250, '#eaf3fb', CB) + t(170, 55, 'Il client chiede', 26, CB, 'middle', True)
    b += box(40, 80, 260, 70, '#fff', CB, 3, 10) + t(170, 111, 'STATO;nome', 25, INK, 'middle', True, True) + t(170, 138, 'come va la partita?', 17, MU, 'middle')
    b += box(40, 170, 260, 80, '#fff', CB, 3, 10) + t(170, 200, 'GUESS;nome;1234', 25, INK, 'middle', True, True) + t(170, 232, 'ecco il mio tentativo', 17, MU, 'middle')
    b += box(480, 20, 500, 250, '#fbeee1', SR) + t(730, 55, 'Il server risponde', 26, SR, 'middle', True)
    rows = [('STATO;GIOCO;...', 'la classifica (gioco acceso o fermo)'), ('WAIT', 'aspetta: il Prof non ha detto Via'), ('RESULT;n;b;...', 'neri, bianchi e classifica'), ('WIN;nome;...', 'hai vinto!'), ('ERR;motivo', 'qualcosa non va')]
    for i, (a, d) in enumerate(rows):
        y = 70 + i * 40
        b += t(500, y + 24, a, 22, INK, 'start', True, True) + t(710, y + 24, d, 16, MU)
    b += arrow(325, 115, 470, 115, CB) + arrow(470, 205, 325, 205, SR)
    return svg(1000, 290, caption_schema(b), 'Schema: le due domande del client e le cinque risposte del server')


def s_partita():
    b = t(130, 30, 'CLIENT (Sara)', 24, CB, 'middle', True) + t(870, 30, 'SERVER (Prof)', 24, SR, 'middle', True)
    b += '<line x1="130" y1="42" x2="130" y2="400" stroke="%s" stroke-width="3"/><line x1="870" y1="42" x2="870" y2="400" stroke="%s" stroke-width="3"/>' % (CB, SR)
    msgs = [(1, 'STATO;Sara', 'STATO;ATTESA;0;0;0;0;0'), (2, 'GUESS;Sara;1234', 'WAIT'), (3, 'GUESS;Sara;1234', 'RESULT;1;2;1;0;1;6;6'),
            (4, 'GUESS;Sara;1237', 'ERR;codice non valido...'), (5, 'GUESS;Sara;1413', 'WIN;Sara;3;75;1;2;3;6')]
    y = 70
    for n, a, r in msgs:
        b += arrow(140, y, 860, y, CB, 4) + t(500, y - 8, '%d  %s' % (n, a), 20, CB, 'middle', True, True)
        b += arrow(860, y + 30, 140, y + 30, SR, 4) + t(500, y + 24, r, 20, SR, 'middle', True, True)
        y += 68
    b += t(500, 418, 'Tra il 2 e il 3 il Prof ha premuto Via. Il 7 non è un colore: ERR e il tentativo non conta.', 18, MU, 'middle')
    return svg(1000, 435, caption_schema(b), 'Schema: una partita con cinque scambi di righe tra client e server')


def s_unit():
    b = box(40, 20, 440, 130, '#eaf3fb', CB) + t(260, 62, 'UnitInterfaccia', 30, CB, 'middle', True) + t(260, 96, 'finestra, disegni, bottoni, pioli', 20, MU, 'middle') + t(260, 126, 'niente rete qui dentro', 19, INK, 'middle')
    b += box(40, 230, 440, 130, '#fff', INK) + t(260, 272, 'UnitRete', 30, INK, 'middle', True) + t(260, 306, 'collegarsi, scrivere una riga,', 20, MU, 'middle') + t(260, 332, 'leggere una riga, il protocollo', 20, MU, 'middle')
    b += arrow(150, 155, 150, 225, CB, 6) + t(162, 196, 'chiama: ChiediStato, InviaTentativo', 18, CB)
    b += arrow(380, 225, 380, 155, '#c47a00', 6) + t(368, 196, 'EVENTO: OnRisultato...', 18, '#c47a00', 'end', True)
    b += box(600, 230, 360, 130, '#fbeee1', SR) + t(780, 285, 'Il server', 30, SR, 'middle', True) + t(780, 322, 'porta 5050', 22, MU, 'middle', False, True)
    b += arrow(485, 295, 595, 295, INK, 5) + arrow(595, 325, 485, 325, INK, 5)
    b += t(540, 280, 'righe', 17, MU, 'middle')
    b += box(560, 40, 400, 110, '#fffbe6', '#d4a017', 3, 10) + t(760, 80, 'Come OnClick di un bottone:', 21, INK, 'middle', True) + t(760, 112, 'quando succede qualcosa,', 21, INK, 'middle') + t(760, 138, 'la rete AVVISA la finestra', 21, INK, 'middle')
    return svg(1000, 390, caption_schema(b), 'Schema: UnitInterfaccia chiama UnitRete e UnitRete avvisa con eventi; UnitRete parla con il server')


def s_eventi_tabella():
    rows = [('riga che arriva', 'evento', 'cosa fa la finestra'), ('STATO;...', 'OnStato', 'scrive GIOCO o ATTESA e la classifica'), ('WAIT', 'OnAttesa', 'scrive: aspetta il Via'),
            ('RESULT;n;b;...', 'OnRisultato', 'disegna i piolini neri e bianchi'), ('WIN;...', 'OnVittoria', 'HAI VINTO + 4 piolini neri'), ('ERR;...', 'OnRifiuto', 'scrive il motivo'), ('(rete rotta)', 'OnErrore', 'scrive cosa non va')]
    b = ''
    for i, (a, e, c) in enumerate(rows):
        y = 20 + i * 52; head = i == 0
        b += box(20, y, 960, 46, '#e9e3d3' if head else '#fff', BD, 2, 8)
        b += t(40, y + 31, a, 21, INK, 'start', head, not head) + t(330, y + 31, e, 21, CB if not head else INK, 'start', True, not head) + t(520, y + 31, c, 20, INK, 'start', head)
    return svg(1000, 400, caption_schema(b), 'Tabella: ogni riga del server fa partire un evento')


# ------------------------------------------------------------------ finte finestre per le istruzioni (schemi)
def mock(title, items, hi=None, w=760, h=230, note=''):
    """items: (kind, x, y, w, h, label). kind: btn, inp, txt, menu, box"""
    b = box(10, 10, w - 20, h - 20, '#fff', '#8d8a80', 3, 10) + '<rect x="10" y="10" width="%d" height="34" rx="10" fill="#d8dde6"/>' % (w - 20)
    b += t(24, 34, title, 18, INK, 'start', True)
    hl = ''
    for k, (kind, x, y, ww, hh, lab) in enumerate(items):
        fill = {'btn': '#e8eef7', 'inp': '#fff', 'menu': '#f3f3f3', 'box': '#fafafa', 'txt': 'none'}[kind]
        st = '#8d8a80' if kind != 'txt' else 'none'
        b += '<rect x="%s" y="%s" width="%s" height="%s" rx="6" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, ww, hh, fill, st)
        b += t(x + ww / 2 if kind in ('btn', 'menu') else x + 8, y + hh / 2 + 7, lab, 18, INK, 'middle' if kind in ('btn', 'menu') else 'start')
        if hi is not None and k == hi:
            hl = '<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="none" stroke="#e11d48" stroke-width="6"/>' % (x - 6, y - 6, ww + 12, hh + 12)
    return svg(w, h, caption_schema(b + hl), title + ' (schema)')


def schemi_ora2():
    d = {}
    d['lazarus-apri'] = mock('Lazarus', [('menu', 20, 54, 110, 30, 'Progetto'), ('menu', 140, 54, 110, 30, 'Modifica'), ('box', 20, 90, 330, 34, 'Apri progetto...'), ('box', 20, 128, 330, 34, 'Salva'), ('txt', 380, 150, 340, 30, 'Cerca: Client\\ClientMastermind.lpi')], hi=2)
    d['lazarus-f9'] = mock('Lazarus', [('menu', 20, 54, 90, 30, 'File'), ('menu', 120, 54, 110, 30, 'Esegui'), ('btn', 20, 100, 130, 46, 'F9  (play verde)'), ('txt', 180, 120, 520, 30, 'Compare la finestra del client con la tavola di legno')], hi=2)
    d['client-connetti'] = mock('Mastermind bello - il tuo CLIENT', [('txt', 30, 60, 150, 26, 'IP del server'), ('inp', 30, 88, 200, 34, '192.168.xx.xx'), ('txt', 250, 60, 150, 26, 'Il tuo nome'), ('inp', 250, 88, 200, 34, 'Sara'), ('btn', 480, 88, 120, 34, 'Connetti'), ('btn', 610, 88, 120, 34, 'Gioca da solo')], hi=5 - 1)
    d['client-collegato'] = mock('Mastermind bello - il tuo CLIENT', [('box', 30, 60, 700, 44, 'Collegato! Ciao Sara.'), ('txt', 30, 130, 700, 30, 'In alto a destra: GIOCO: provaci! oppure ATTESA: aspetta il Via del Prof')], hi=0)
    d['client-gioca'] = mock('Mastermind bello - il tuo CLIENT', [('btn', 30, 60, 90, 40, 'rosso'), ('btn', 130, 60, 90, 40, 'giallo'), ('btn', 230, 60, 90, 40, 'verde'), ('btn', 330, 60, 90, 40, 'blu'), ('btn', 560, 60, 160, 40, 'Prova'), ('txt', 30, 130, 690, 30, '1) clicca 4 colori   2) premi Prova   3) guarda i piolini neri e bianchi')], hi=4)
    d['unitrete'] = mock('Lazarus: UnitRete.pas', [('txt', 30, 60, 700, 28, 'const  PORTA_SERVER = 5050;'), ('txt', 30, 92, 700, 28, "function RigaGuess ... Result := 'GUESS;' + Nome + ';' + Codice;"), ('txt', 30, 124, 700, 28, 'procedure TClienteRete.Elabora(const Riga: String);'), ('txt', 30, 156, 700, 28, '  Tipo := Campo(Riga, 0);  se Tipo = RESULT ... OnRisultato')], hi=2, h=210)
    d['cerca'] = mock('Lazarus', [('menu', 20, 54, 90, 30, 'Cerca'), ('box', 20, 90, 330, 34, 'Trova...   (Ctrl + F)'), ('inp', 380, 90, 330, 34, 'PORTA_SERVER'), ('btn', 380, 134, 110, 34, 'Trova')], hi=1)
    d['titolo'] = mock('Lazarus: UnitInterfaccia.pas', [('txt', 30, 60, 700, 28, "TITOLO_FORM = 'Mastermind bello - il tuo CLIENT';"), ('txt', 30, 110, 700, 28, "TITOLO_FORM = 'Mastermind di Sara';   <- scrivi il TUO nome"), ('txt', 30, 160, 700, 28, 'Poi premi F9: il titolo della finestra cambia')], hi=1)
    d['github-upload'] = mock('github.com  -  il tuo repository', [('btn', 20, 60, 140, 36, 'Add file'), ('box', 20, 100, 260, 34, 'Upload files'), ('txt', 300, 100, 440, 28, 'poi trascina qui la cartella del tuo progetto')], hi=1)
    d['github-commit'] = mock('github.com  -  Commit changes', [('inp', 30, 60, 700, 38, 'Mastermind v4: provato il protocollo, titolo con il mio nome'), ('btn', 30, 120, 200, 40, 'Commit changes (verde)'), ('txt', 250, 130, 480, 28, 'Il messaggio dice COSA hai fatto, in una frase')], hi=0)
    return d


# ------------------------------------------------------------------ il contenuto della lezione
NOME_LEZIONE = 'Il protocollo del Mastermind: la UnitRete e il linguaggio tra client e server'
VOCE = ('Allegato A, 3INF (Classe 3 2026/27), Competenza 16 "Eseguire la manutenzione ordinaria e straordinaria di sistemi, reti, dispositivi e '
        'terminali", III Anno: voci "Protocolli di rete" e "TCP/IP porte". Collegata a Competenza 8, II Anno: "Master Mind".')

TEORIA = [
    ('Due programmi che si parlano',
     'Il Mastermind in rete ha DUE programmi. Il CLIENT è quello di ogni ragazzo. Il SERVER è quello del Prof. In mezzo c\'è la rete, come un tubo. '
     'Il server ascolta a una "porta": un numero. La nostra porta è la 5050.',
     s_due_programmi(), 'Un indirizzo IP dice QUALE computer. La porta dice QUALE programma dentro quel computer.',
     'ক্লায়েন্ট হলো প্রত্যেকের প্রোগ্রাম, সার্ভার হলো স্যারের প্রোগ্রাম। সার্ভার ৫০৫০ নম্বর পোর্টে শোনে।'),
    ('Una riga che va, una riga che torna',
     'Per parlare, il client scrive UNA riga di testo e la manda. Il server legge, pensa e risponde con UNA riga. '
     'Poi la conversazione è finita. Il programma di Sara si collega, scrive, legge e chiude, ogni volta.',
     s_riga_va_torna(), 'Per questo il client chiede lo STATO ogni 3 secondi: ogni volta è una conversazione nuova.',
     'ক্লায়েন্ট একটি লাইন পাঠায়, সার্ভার একটি লাইন ফেরত দেয়।'),
    ('Come è fatta una riga',
     'Una riga è fatta di CAMPI separati da un punto e virgola ( ; ). Il primo campo dice che cosa è la riga. '
     'Gli altri campi sono i dati. Chi legge conta i campi: il primo è il numero 0.',
     s_campi(), 'Nel codice, la funzione Campo(Riga, 2) prende il campo numero 2. In RESULT;1;2;1;0;1;6;6 il campo 2 è il 2 (i bianchi).',
     'লাইনের অংশগুলো সেমিকোলন (;) দিয়ে আলাদা করা থাকে। প্রথম অংশ বলে লাইনটা কী।'),
    ('Le due domande e le cinque risposte',
     'Il client sa fare DUE domande: STATO (come va la partita?) e GUESS (ecco il mio tentativo). '
     'Il server sa dare CINQUE risposte: STATO, WAIT, RESULT, WIN, ERR. Questo piccolo elenco è il PROTOCOLLO: il linguaggio che i due programmi hanno deciso insieme.',
     s_domande_risposte(), 'I colori nei tentativi sono numeri: 1 rosso, 2 giallo, 3 verde, 4 blu, 5 arancio, 6 porpora. Il codice 1234 è rosso, giallo, verde, blu.',
     'STATO মানে: খেলা কেমন চলছে? GUESS মানে: আমার অনুমান এই। সার্ভার পাঁচ রকম উত্তর দিতে পারে: STATO, WAIT, RESULT, WIN, ERR।'),
    ('Una partita passo per passo',
     'Guarda i cinque scambi. Sara si collega (1), prova troppo presto e riceve WAIT (2), il Prof preme Via e Sara riceve il suo primo risultato (3), '
     'sbaglia a scrivere un colore e riceve ERR (4), poi indovina e riceve WIN (5).',
     s_partita(), 'Neri = colore giusto al posto giusto. Bianchi = colore giusto al posto sbagliato. Con segreto 1413 e tentativo 1234: 1 nero e 2 bianchi.',
     'WAIT মানে: স্যার এখনো "ভিয়া" বলেননি, অপেক্ষা করো। RESULT-এ কালো গুটি = সঠিক রঙ সঠিক জায়গায়; সাদা গুটি = সঠিক রঙ ভুল জায়গায়। WIN মানে: তুমি জিতেছ! ERR মানে: ভুল হয়েছে।'),
    ('Come è fatta la UnitRete',
     'Nella versione 4 il client è diviso in DUE pezzi (due "unit"). UnitInterfaccia = la finestra: disegni, bottoni, pioli. UnitRete = la rete: collegarsi, scrivere una riga, leggere una riga e capire il protocollo. '
     'La UnitRete NON conosce la finestra. Quando arriva una risposta, avvisa la finestra con un EVENTO: come l\'evento click di un bottone in Lazarus, ma lo lancia la rete.',
     s_unit(), 'Perché dividere? 1) la rete si può provare da sola, 2) chi disegna non tocca la rete, 3) niente giri in tondo: la finestra conosce la rete, la rete non conosce la finestra.',
     'UnitRete শুধু নেটওয়ার্কের কাজ করে; UnitInterfaccia শুধু জানালা ও ছবি। ইভেন্ট হলো বোতামের OnClick-এর মতো: কিছু ঘটলে প্রোগ্রাম জানিয়ে দেয়।'),
    ('Quale riga fa partire quale evento',
     'Ogni risposta del server ha il suo evento. La UnitRete guarda il primo campo della riga e sceglie l\'evento giusto. La finestra ha già scritto cosa fare per ciascuno.',
     s_eventi_tabella(), 'Nel codice: Rete.OnRisultato := @ReteRisultato; vuol dire "quando arriva RESULT, chiama la mia procedura ReteRisultato".',
     'প্রতিটি উত্তরের নিজস্ব ইভেন্ট আছে। প্রথম অংশ দেখে UnitRete ঠিক ইভেন্টটি চালু করে।'),
]

# ------------------------------------------------------------------ quiz (12 domande vere sul protocollo spiegato)
QUIZ = [
    ('Su quale porta ascolta il server del Mastermind?', '5050', ['80', '21', '1234']),
    ('Quale riga manda il client per chiedere "come va la partita?" (il nome è Sara)?', 'STATO;Sara', ['GUESS;Sara;STATO', 'WAIT;Sara', 'RESULT;Sara']),
    ('Il Prof non ha ancora premuto Via. Sara manda GUESS;Sara;1234. Che cosa risponde il server?', 'WAIT', ['WIN;Sara;1;0;1;1;1;1', 'RESULT;4;0;1;0;0;0;0', 'STATO;GIOCO;0;0;0;0;0']),
    ('Il server risponde RESULT;2;1;4;0;3;3;7. Quanti piolini neri e quanti bianchi?', '2 neri e 1 bianco', ['1 nero e 2 bianchi', '4 neri e 0 bianchi', '0 neri e 4 bianchi']),
    ('Nella stessa riga RESULT;2;1;4;0;3;3;7 il campo "posto" vale 0. Che cosa vuol dire?', 'Non hai ancora finito: non hai ancora un posto in classifica', ['Sei arrivato ultimo', 'Il server ha sbagliato', 'Hai vinto con 0 tentativi']),
    ('Il server risponde WIN;Sara;5;62;2;4;3;8. Quanti tentativi e quanti secondi?', '5 tentativi e 62 secondi', ['62 tentativi e 5 secondi', '2 tentativi e 4 secondi', '3 tentativi e 8 secondi']),
    ('Sara scrive per errore GUESS;Sara;1237. Che cosa risponde il server?', 'ERR;codice non valido (servono 4 cifre da 1 a 6)', ['WAIT', 'RESULT;4;0;1;0;0;0;0', 'WIN;Sara;1;0;1;1;1;1']),
    ('Nella riga RESULT;1;2;5;0;3;4;9 il primo campo (RESULT) è il numero 0. Quale numero ha il campo dei bianchi?', '2', ['1', '3', '0']),
    ('Il codice segreto è 1123 e il tentativo è 1211. Quanti neri e quanti bianchi risponde il server?', '1 nero e 2 bianchi', ['2 neri e 1 bianco', '0 neri e 4 bianchi', '3 neri e 0 bianchi']),
    ('Ogni quanto tempo il client chiede STATO al server, anche se nessuno preme niente?', 'Ogni 3 secondi', ['Mai', 'Solo quando si preme Prova', 'Ogni ora']),
    ('Quando arriva una riga RESULT, che cosa fa la UnitRete per avvisare la finestra?', 'Fa partire l\'evento OnRisultato, come un click su un bottone', ['Disegna lei i piolini sulla tavola', 'Chiude il programma', 'Scrive nella finestra con Forms']),
    ('Quale unit contiene i socket e il protocollo, e NON conosce nessuna finestra?', 'UnitRete', ['UnitInterfaccia', 'UnitServer', 'DisegnoMastermind']),
]


def quiz_json():
    dom = []
    for k, (q, ok, sb) in enumerate(QUIZ, 1):
        dom.append({'A': ['%d) %s' % (k, q), ok, sb]})
    return {'titolo': 'Quiz di rete: il protocollo del Mastermind (3INF, 04/11)',
            'descrizione': '12 domande sul protocollo spiegato oggi (STATO, GUESS, WAIT, RESULT, WIN, ERR, la porta 5050, la UnitRete). Ogni risposta giusta vale 1 punto. Per il voto serve almeno 8 su 12.',
            'punti': 1, 'mescola': True, 'versioni': ['A'], 'domande': dom}


# ------------------------------------------------------------------ il simulatore "Il Prof finto" (JS, tutto dentro la pagina)
SIM_JS = r"""
(function(){
"use strict";
function $(i){return document.getElementById(i);}
var COL=["","#DC2828","#F0C81E","#28A03C","#285ADC","#F0821E","#8C32AA"];
var NOMI=["","rosso","giallo","verde","blu","arancio","porpora"];
var seg=[0,0,0,0],gioco=false,tent=0,risolto=false,secondi=0,t0=0,nome="";
var altri={tent:6,sec:90}; /* un altro ragazzo (finto) ha gia' finito in 6 tentativi */
var visti={STATO:0,WAIT:0,RESULT:0,WIN:0,ERR:0};
function nuovo(){for(var i=0;i<4;i++)seg[i]=1+Math.floor(Math.random()*6);tent=0;risolto=false;}
nuovo();
function val(s,p){var n=0,cs=[0,0,0,0,0,0,0],cp=[0,0,0,0,0,0,0],b=0,i;
  for(i=0;i<4;i++){if(s[i]===p[i])n++;else{cs[s[i]]++;cp[p[i]]++;}}
  for(i=1;i<=6;i++)b+=Math.min(cs[i],cp[i]);return [n,b];}
function campo(r,n){var a=r.split(";");return n<a.length?a[n].trim():"";}
function classifica(){var fin=1+(risolto?1:0),mig=altri.tent,peg=altri.tent;
  if(risolto){mig=Math.min(mig,tent);peg=Math.max(peg,tent);}
  var posto=0;if(risolto){posto=1;if(altri.tent<tent||(altri.tent===tent&&altri.sec<secondi))posto++;}
  return (tent)+";"+posto+";"+fin+";"+mig+";"+peg;}
/* IL SERVER FINTO: stesse regole del vero UnitServer */
function server(riga){
  var cmd=campo(riga,0).toUpperCase(),n=campo(riga,1).replace(/[^A-Za-z0-9 ._-]/g,"");
  if(cmd==="STATO"){return "STATO;"+(gioco?"GIOCO":"ATTESA")+";"+classifica();}
  if(cmd!=="GUESS")return "ERR;comando sconosciuto";
  var g=campo(riga,2);
  if(n==="")return "ERR;nome non valido";
  if(!/^[1-6]{4}$/.test(g))return "ERR;codice non valido (servono 4 cifre da 1 a 6)";
  if(!gioco)return "WAIT";
  var p=[+g[0],+g[1],+g[2],+g[3]],r=val(seg,p);
  if(!risolto){tent++;if(r[0]===4){risolto=true;secondi=Math.round((Date.now()-t0)/1000);}}
  if(risolto)return "WIN;"+n+";"+tent+";"+secondi+";"+classifica().split(";").slice(1).join(";");
  return "RESULT;"+r[0]+";"+r[1]+";"+classifica();
}
function riga(cls,txt){var d=document.createElement("div");d.className=cls;d.textContent=txt;$("log").appendChild(d);$("log").scrollTop=1e6;}
function pioli(neri,bianchi,cod){
  var d=document.createElement("div");d.className="rowp";
  for(var i=0;i<4;i++){var s=document.createElement("span");s.className="pg";s.style.background=COL[cod[i]];d.appendChild(s);}
  var sp=document.createElement("span");sp.className="sp";d.appendChild(sp);
  for(var k=0;k<4;k++){var q=document.createElement("span");q.className="pr";q.style.background=k<neri?"#111":(k<neri+bianchi?"#f4f4f4":"#c9b38a");d.appendChild(q);}
  $("tav").appendChild(d);
}
function aggiorna(){
  var n=0;for(var k in visti)if(visti[k])n++;
  for(var k2 in visti){$("v"+k2).className="vis"+(visti[k2]?" ok":"");}
  $("conta").textContent=n+" su 5";
  $("gstato").textContent=gioco?"GIOCO (acceso)":"ATTESA (fermo)";
  $("gstato").className=gioco?"on":"off";
  if(n===5)$("fatto").style.display="block";
}
function manda(r){
  riga("c","client → server:  "+r);
  var ris=server(r);
  riga("s","server → client:  "+ris);
  var tipo=campo(ris,0);if(visti[tipo]!==undefined)visti[tipo]=1;
  if(tipo==="RESULT"||tipo==="WIN"){var g=campo(r,2),cod=[+g[0],+g[1],+g[2],+g[3]];
    pioli(tipo==="WIN"?4:+campo(ris,1),tipo==="WIN"?0:+campo(ris,2),cod);}
  if(tipo==="WIN"){riga("n","★ Hai indovinato il codice! Premi 'Nuova partita' per rigiocare.");}
  $("sp").textContent=ris;
  spiega(ris);
  aggiorna();
}
function spiega(ris){
  var t=campo(ris,0),s="";
  if(t==="STATO")s="STATO: il server dice se il gioco è acceso ("+campo(ris,1)+") e ti manda la classifica.";
  else if(t==="WAIT")s="WAIT: il Prof non ha ancora premuto Via. Il tuo tentativo NON conta.";
  else if(t==="RESULT")s="RESULT: "+campo(ris,1)+" neri e "+campo(ris,2)+" bianchi. Poi la classifica.";
  else if(t==="WIN")s="WIN: hai vinto con "+campo(ris,2)+" tentativi in "+campo(ris,3)+" secondi.";
  else if(t==="ERR")s="ERR: il server ti dice cosa non va ("+campo(ris,1)+"). Il tentativo NON conta.";
  $("spiega").textContent=s;
}
window.PF={
  nome:function(){var v=$("nome").value.replace(/[;\n]/g,"").trim();if(!v){$("nome").focus();$("nome").classList.add("err");return null;}$("nome").classList.remove("err");nome=v;try{localStorage.setItem("pf_nome",v);}catch(e){}return v;},
  stato:function(){var n=PF.nome();if(n)manda("STATO;"+n);},
  via:function(){gioco=true;t0=Date.now();riga("n","(il Prof ha premuto Via: ora i tentativi contano)");aggiorna();},
  ferma:function(){gioco=false;riga("n","(il Prof ha premuto Stop)");aggiorna();},
  prova:function(){var n=PF.nome();if(!n)return;var cod="";for(var i=0;i<4;i++)cod+=PF.sc[i]||"";
    if(cod.length<4){riga("n","Scegli 4 colori (clicca i pallini), poi premi Manda.");return;}manda("GUESS;"+n+";"+cod);PF.sc=[];colori();},
  libera:function(){var r=$("libera").value;if(r.trim()==="")return;manda(r.trim());},
  nuova:function(){nuovo();$("tav").textContent="";riga("n","(nuova partita: codice nuovo)");},
  sc:[]
};
function colori(){
  var c=$("scelta");c.textContent="";
  for(var i=0;i<4;i++){var s=document.createElement("span");s.className="pg";s.style.background=PF.sc[i]?COL[PF.sc[i]]:"#c9b38a";c.appendChild(s);}
}
function tavolozza(){
  var t=$("tavoloz");
  for(var i=1;i<=6;i++){(function(i){var b=document.createElement("button");b.type="button";b.className="pgb";b.style.background=COL[i];b.title=NOMI[i]+" ("+i+")";b.setAttribute("aria-label",NOMI[i]+" "+i);b.textContent=i;
    b.onclick=function(){if(PF.sc.length<4){PF.sc.push(i);colori();}};t.appendChild(b);})(i);}
}
$("togli").onclick=function(){PF.sc.pop();colori();};
tavolozza();colori();aggiorna();
try{var v=localStorage.getItem("pf_nome");if(v)$("nome").value=v;}catch(e){}
})();
"""

SIM_HTML = """
<div class="sim">
  <div class="rg"><label for="nome"><b>1. Il tuo nome</b> (fallo tuo!)</label>
  <input id="nome" type="text" maxlength="20" placeholder="Scrivi il tuo nome" autocomplete="off"></div>
  <div class="rg"><b>2. Il Prof finto</b> &nbsp; Il gioco è: <span id="gstato" class="off">ATTESA (fermo)</span><br>
  <button type="button" class="bt alt" onclick="PF.via()">Via! (fai il Prof)</button> <button type="button" class="bt alt" onclick="PF.ferma()">Stop</button> <button type="button" class="bt alt" onclick="PF.nuova()">Nuova partita</button></div>
  <div class="rg"><b>3. Mandaci una riga</b><br>
  <button type="button" class="bt" onclick="PF.stato()">Manda STATO</button>
  <div class="small">Questo bottone scrive per te la riga <code>STATO;il tuo nome</code>.</div></div>
  <div class="rg"><b>4. Fai un tentativo (GUESS)</b><br>
  <span id="tavoloz" class="tv"></span> <span id="scelta" class="tv"></span> <button type="button" class="bt alt" id="togli">Togli l'ultimo</button> <button type="button" class="bt" onclick="PF.prova()">Manda GUESS</button></div>
  <div class="rg"><b>5. Scrivi tu una riga a mano</b> (anche sbagliata: il server finto non si arrabbia)<br>
  <input id="libera" type="text" class="mono" value="GUESS;;1234" aria-label="riga da mandare">
  <button type="button" class="bt alt" onclick="PF.libera()">Manda questa riga</button></div>
  <div class="grid2">
    <div><b>La tavola</b><div id="tav" class="tav"></div></div>
    <div><b>Le righe che passano</b><div id="log" class="logp"></div></div>
  </div>
  <div class="rg"><b>Ultima risposta del server:</b> <code id="sp">(ancora niente)</code><div id="spiega" class="small"></div></div>
  <div class="rg"><b>Risposte scoperte: <span id="conta">0 su 5</span></b><br>
    <span id="vSTATO" class="vis">STATO</span> <span id="vWAIT" class="vis">WAIT</span> <span id="vRESULT" class="vis">RESULT</span> <span id="vWIN" class="vis">WIN</span> <span id="vERR" class="vis">ERR</span>
    <div id="fatto" class="fatto" style="display:none">FATTO! Hai scoperto TUTTE e cinque le risposte del server. Ora il protocollo è tuo.</div></div>
</div>
"""

CSS = """
:root{--bg:#f6f4ee;--fg:#1d1d1f;--mu:#5d5a52;--card:#fffdf8;--bd:#cfc8b8;--acc:#0b5fa5;--ok:#1a7f37;--bad:#b3261e;--q:#fff4c2;--bn:#eef7ee}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15130f;--fg:#f1ede3;--mu:#b5ae9d;--card:#211e17;--bd:#3d382c;--acc:#6db3f2;--ok:#56d364;--bad:#ff7b72;--q:#3b3200;--bn:#16301a}}
:root[data-theme="dark"]{--bg:#15130f;--fg:#f1ede3;--mu:#b5ae9d;--card:#211e17;--bd:#3d382c;--acc:#6db3f2;--ok:#56d364;--bad:#ff7b72;--q:#3b3200;--bn:#16301a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:19px/1.5 system-ui,"Segoe UI",Arial,sans-serif}
main{max-width:900px;margin:0 auto;padding:10px 16px 60px}h1{font-size:1.45em;margin:.4em 0}h2{font-size:1.2em;margin:.2em 0 .4em}
.card{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 16px;margin:14px 0}
.card svg{width:100%;height:auto;display:block;border-radius:8px;margin:8px 0;border:1px solid var(--bd)}
.nota{background:var(--q);border-radius:10px;padding:8px 12px;font-size:.95em}
.bozza{background:#fde8e8;border:2px solid #c0392b;border-radius:10px;padding:8px 12px;font-size:.95em;margin:10px 0}
.bn{background:var(--bn);border:1px dashed var(--ok);border-radius:10px;padding:6px 12px;margin:8px 0;font-size:.95em}
.bn summary{cursor:pointer;color:var(--ok);font-weight:700}
.lock{border:3px dashed var(--bd);text-align:center;color:var(--mu)}
code,.mono{font-family:Consolas,"Courier New",monospace}code{background:rgba(120,120,120,.15);padding:1px 5px;border-radius:5px}
.bt{display:inline-block;background:var(--acc);color:#fff;font:inherit;font-weight:700;padding:9px 16px;border-radius:10px;border:2px solid var(--acc);cursor:pointer;margin:4px 4px 4px 0}
.bt.alt{background:transparent;color:var(--acc)}
.small{font-size:.85em;color:var(--mu)}
.sim .rg{border-top:1px solid var(--bd);padding:10px 0}.sim .rg:first-child{border-top:0}
.sim input[type=text]{font:inherit;padding:8px;border:2px solid var(--bd);border-radius:8px;background:var(--card);color:var(--fg);width:100%;max-width:420px}
.sim input.err{border-color:var(--bad)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media (max-width:700px){.grid2{grid-template-columns:1fr}}
.tav{background:#b98a52;border:3px solid #8a5a2b;border-radius:10px;min-height:60px;padding:8px}
.rowp{display:flex;align-items:center;gap:6px;margin:4px 0}.pg{display:inline-block;width:26px;height:26px;border-radius:50%;border:2px solid rgba(0,0,0,.35)}
.pr{display:inline-block;width:12px;height:12px;border-radius:50%;border:1px solid rgba(0,0,0,.4)}.sp{width:14px}
.pgb{width:42px;height:42px;border-radius:50%;border:3px solid rgba(0,0,0,.4);color:#fff;font-weight:700;font-size:18px;cursor:pointer;margin-right:4px;text-shadow:0 0 3px #000}
.tv{display:inline-flex;gap:4px;vertical-align:middle;margin-right:8px}
.logp{background:#14110d;color:#f1ede3;border-radius:10px;padding:8px;font:15px/1.45 Consolas,"Courier New",monospace;height:16em;overflow:auto}
.logp .c{color:#7fc2ff}.logp .s{color:#ffb066}.logp .n{color:#a8a291}
.vis{display:inline-block;border:2px solid var(--bd);border-radius:8px;padding:2px 12px;font-family:Consolas,monospace;font-weight:700;color:var(--mu)}
.vis.ok{border-color:var(--ok);color:var(--ok)}.vis.ok::before{content:"✔ "}
.fatto{margin-top:10px;background:var(--ok);color:#fff;border-radius:10px;padding:10px 14px;font-weight:700}
#gstato.on{color:var(--ok);font-weight:700}#gstato.off{color:var(--bad);font-weight:700}
.kpi td,.kpi th{border:1px solid var(--bd);padding:4px 10px;text-align:left}.kpi{border-collapse:collapse}
"""


def card(n, titolo, testo, img, nota, bn=None):
    s = '<section class="card"><h2>%s. %s</h2><p>%s</p>%s' % (n, titolo, testo, img)
    if nota: s += '<p class="nota">%s</p>' % nota
    if bn: s += '<details class="bn"><summary>বাংলা সাহায্য (se ti serve)</summary><p>%s</p></details>' % bn
    return s + '</section>'


def pagina(titolo, corpo, script=''):
    return ('<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>%s</style></head><body><main>%s</main>%s</body></html>') % (titolo, CSS, corpo, script)


# ------------------------------------------------------------------ ORA 1 (esercizio)
def ora1_html():
    c = '<div class="bozza"><b>BOZZA NON PUBBLICATA.</b> Teoria e compito vanno prima analizzati insieme al Prof. I disegni sono schemi, non schermate vere.</div>'
    c += '<h1>%s</h1><p class="small">3INF, mercoledì 04/11/2026, 12:00-14:00. Ora 1 di 2 (le ore successive sono bloccate). Aiuto: la casella dell\'assistente del Prof Regge.</p>' % E(NOME_LEZIONE)
    c += '<p>%s</p>' % E(VOCE).replace('"', '&quot;')
    c += '<div class="card"><h2>Che cosa farai oggi</h2><p>Capirai come parlano il client e il server del Mastermind. Alla fine di questa ora avrai <b>provato il protocollo con le tue mani</b> e saprai spiegarlo a un compagno. Prima guardiamo insieme l\'animazione alla lavagna.</p></div>'
    for k, (ti, te, im, no, bn) in enumerate(TEORIA, 1):
        c += card(k, ti, te, im, no, bn)
    c += '<section class="card"><h2>Ora tocca a te: il Prof finto</h2><p>Qui sotto c\'è un server finto che risponde come quello vero. Non serve nessuna rete. Vinci subito: premi un bottone e vedi la prima risposta.</p>'
    c += svg(760, 200, caption_schema(box(10, 10, 740, 180, '#fff', '#8d8a80', 3, 10) + box(30, 30, 200, 44, '#e8eef7', '#8d8a80', 2, 6) + t(130, 60, 'Manda STATO', 20, INK, 'middle') + arrow(240, 52, 330, 52, '#e11d48', 5) + box(340, 30, 390, 44, '#14110d', '#14110d', 2, 6) + t(350, 59, 'server → client: STATO;ATTESA;0;0;0;0;0', 17, '#ffb066', 'start', False, True) + t(30, 120, '1) scrivi il tuo nome   2) premi Manda STATO   3) leggi la risposta', 20, INK) + t(30, 156, 'Poi: Via!, scegli 4 colori, Manda GUESS. Gioca finché vinci.', 20, INK)), 'Schema del Prof finto: nome, bottone, risposta')
    c += '</section>'
    c += '<section class="card"><h2>Missione 1: scopri le 5 risposte</h2><p>Il server sa dare cinque risposte: <b>STATO, WAIT, RESULT, WIN, ERR</b>. Il tuo lavoro è farle comparire tutte e cinque. Ogni risposta trovata si accende con un segno verde.</p>'
    c += '<ol><li>Scrivi il tuo nome. Premi <b>Manda STATO</b>: hai trovato STATO.</li><li>Senza premere Via, scegli 4 colori e premi <b>Manda GUESS</b>: troverai WAIT (il Prof non ha detto Via).</li><li>Premi <b>Via! (fai il Prof)</b>. Manda un tentativo: troverai RESULT.</li><li>Nella casella a mano scrivi un colore sbagliato, per esempio <code>GUESS;TuoNome;1237</code>, e premi <b>Manda questa riga</b>: troverai ERR.</li><li>Continua a provare finché indovini il codice: troverai WIN. Il codice cambia a ogni partita.</li></ol>'
    c += '<details class="bn"><summary>বাংলা সাহায্য (se ti serve)</summary><p>নিজের নাম লিখো। ধাপে ধাপে চেষ্টা করো: STATO, তারপর "ভিয়া" ছাড়া একটি অনুমান (WAIT), তারপর "ভিয়া" চাপো (RESULT), একটি ভুল কোড লিখে ERR, শেষে সঠিক কোড (WIN)।</p></details>'
    c += SIM_HTML + '</section>'
    c += ('<section class="card"><h2>Missione 2: leggi e spiega</h2><p>Guarda l\'ultima riga che il server ha mandato. Spiega a voce a un compagno, con parole tue, che cosa vuol dire ogni campo. '
          'Esempio: in <code>RESULT;1;2;3;0;1;6;6</code> il primo numero sono i neri. Se riesci a spiegarlo, hai capito davvero: è la prova del nove.</p>'
          '<p class="nota">Se qualcosa non funziona, scrivi all\'assistente del Prof Regge nella casella d\'aiuto. Se il Prof finto si blocca, ricarica la pagina con F5: non succede niente di grave.</p></section>')
    c += ('<section class="card lock"><h2>Ora 2: in arrivo</h2><p id="lockmsg">L\'ora 2 si apre quando il Prof la sblocca. Non serve fare niente: aspetta qui.</p>'
          '<p id="ora2link" style="display:none"><a class="bt" href="ora2.html">Apri l\'ora 2</a></p></section>')
    c += '<script>var ORE_SBLOCCATE = 1; /* 1 = solo ora 1; il Prof lo porta a 2 per aprire l\'ora 2 */ if (ORE_SBLOCCATE >= 2) { document.getElementById("lockmsg").style.display = "none"; document.getElementById("ora2link").style.display = "block"; }</script>'
    return pagina('Il protocollo del Mastermind', c, '<script>%s</script>' % SIM_JS)


# ------------------------------------------------------------------ ORA 2
def ora2_pagine():
    d = schemi_ora2()
    passi = [
        ('Apri il client versione 4', 'In Lazarus apri il menu <b>Progetto</b> in alto e scegli <b>Apri progetto...</b>. Cerca la cartella del Mastermind v4, apri <b>Client</b> e scegli <b>ClientMastermind.lpi</b>.', d['lazarus-apri'], None),
        ('Premi F9: vinci subito', 'Premi il tasto <b>F9</b> sulla tastiera. La prima volta Lazarus impiega un po\'. Poi compare il client con la tavola di legno. Premi <b>Gioca da solo</b> e prova un tentativo: funziona anche senza rete.', d['lazarus-f9'], None),
        ('Fallo tuo: collegati al Prof', 'Nella casella <b>IP del server</b> scrivi l\'indirizzo che il Prof ha scritto alla lavagna. Nella casella del nome scrivi il TUO nome. Premi <b>Connetti</b>.', d['client-connetti'], 'Se compare un errore rosso, leggi le parole: dicono cosa controllare (IP, server acceso). Puoi giocare con "Gioca da solo" e chiedere all\'assistente.'),
        ('FATTO: sei collegato', 'In basso compare <b>Collegato! Ciao</b> e il tuo nome. Dietro le quinte il tuo programma ha mandato <code>STATO;il tuo nome</code> e il server ha risposto. Questo è il momento che conta per il voto: client collegato.', d['client-collegato'], None),
        ('Gioca e guarda le righe', 'Quando il Prof preme Via, clicca 4 colori e premi <b>Prova</b>. Ogni volta il tuo programma manda <code>GUESS;nome;codice</code> e il server risponde RESULT. I piolini neri e bianchi sono quelli del RESULT.', d['client-gioca'], None),
        ('Trova la porta nel codice', 'Premi <b>Ctrl + F</b> in Lazarus. Scrivi <code>PORTA_SERVER</code> e premi <b>Trova</b>. Sei dentro <b>UnitRete.pas</b>: il valore è 5050. Per aprire UnitRete.pas: tasto <b>Ctrl + F12</b>, doppio clic su UnitRete.', d['cerca'], None),
        ('Trova dove si legge una riga', 'Sempre in UnitRete.pas cerca la parola <code>Elabora</code>. Qui la rete legge il primo campo e decide quale evento lanciare. Cerca anche <code>GUESS</code>: è la riga che il client scrive.', d['unitrete'], 'Spiega a un compagno, con parole tue: perché UnitRete non ha bisogno di nessuna finestra?'),
        ('Fallo tuo: il titolo con il tuo nome', 'Apri <b>UnitInterfaccia.pas</b> (Ctrl + F12) e cerca <code>TITOLO_FORM</code>. Cambia il testo tra gli apici con il tuo nome, per esempio come nello schema. Premi F9: il titolo della finestra è cambiato.', d['titolo'], None),
        ('Mettilo su GitHub (browser)', 'Apri github.com nel browser, entra nel tuo repository, premi <b>Add file</b> (in alto a destra) e poi <b>Upload files</b> (Carica file). Trascina nella pagina la cartella <b>Client</b> con il tuo titolo.', d['github-upload'], None),
        ('Il commit chiaro', 'In basso scrivi nel riquadro il messaggio, una frase che dice COSA hai fatto. Poi premi il bottone verde <b>Commit changes</b> (Salva le modifiche).', d['github-commit'], 'Un buon messaggio dice cosa e perché: questo si vede nella storia del progetto.'),
    ]
    copia = 'Mastermind v4: provato il protocollo, titolo con il mio nome'
    c = '<div class="bozza"><b>BOZZA NON PUBBLICATA: ORA 2.</b> Si apre solo quando il Prof la sblocca. I disegni sono schemi.</div>'
    c += '<h1>Ora 2: provi il client vero collegato al server</h1><p class="small">3INF, 04/11/2026. Il Prof ha acceso il server sul suo PC (porta 5050).</p>'
    for k, (ti, te, im, no) in enumerate(passi, 1):
        c += '<section class="card"><h2>%d. %s</h2><p>%s</p>%s%s</section>' % (k, ti, te, im, ('<p class="nota">%s</p>' % no) if no else '')
        if k == 10:
            c += '<section class="card"><p>Per il messaggio del commit puoi copiare questo (oppure scrivere uno tuo, più bello):</p><pre class="mono" style="background:#14110d;color:#f1ede3;padding:10px;border-radius:8px;overflow:auto">%s</pre></section>' % E(copia)
    c += ('<section class="card"><h2>11. Il quiz sulla rete</h2><p>Il quiz ha 12 domande su quello che hai provato. Per un buon voto serve almeno 8 su 12. Il link del quiz compare qui quando il Prof lo apre (Modulo).</p></section>'
          '<section class="card"><h2>Piano B: se il server non risponde</h2><p>Torna alla pagina dell\'ora 1 e usa il Prof finto: funziona senza rete. Oppure premi <b>Gioca da solo</b> nel client. Poi avvisa l\'assistente nella casella d\'aiuto.</p>'
          '<details class="bn"><summary>বাংলা সাহায্য (se ti serve)</summary><p>সার্ভার না পেলে "Gioca da solo" চাপো বা প্রথম পাতার নকল সার্ভার ব্যবহার করো। সংযুক্ত হলে "Collegato!" লেখা দেখা যাবে।</p></details></section>')
    return pagina('Ora 2 - il client collegato', c), passi, copia


# ------------------------------------------------------------------ il MD
def md_lezione(passi2, copia):
    m = ['# 04/11/2026, 3INF: %s' % NOME_LEZIONE, '',
         '**BOZZA NON PUBBLICATA.** Da analizzare con il docente (regole 7 e 17). Sorgenti: `lezione.html` (ora 1, con ora 2 bloccata) e `ora2.html`. I disegni sono schemi, non schermate.', '',
         '## 1 Voce dell\'Allegato A', '', VOCE, '',
         'Controllo fatto su `MIE-PARTI-ALLEGATO-A.md`: le voci ci sono, la lezione NON è scoperta. Non ho riletto i file Word originali in `programmi-ufficiali/2026-27/`.', '',
         '## 2 Organizzazione delle due ore', '',
         '1. Ora 1 (12:00-13:00): animazione alla lavagna (`animazione-protocollo.html`, 25 passi), poi i 6 schemi di teoria, poi "Il Prof finto" (missioni: scoprire le 5 risposte e spiegare una riga a voce).',
         '2. Ora 2 (13:00-14:00, bloccata fino allo sblocco, flag `ORE_SBLOCCATE`): client v4 in Lazarus (Progetto, Apri progetto, F9), collegamento al server del Prof, partita, ricerca di PORTA_SERVER ed Elabora in UnitRete.pas, titolo con il proprio nome, commit su GitHub, quiz di 12 domande su Moduli.',
         '3. Quaderno (regola 23, solo 1INF): non applicabile. Carta e penna: sospese per i compiti, tutto al PC.', '',
         '## 3 KPI proposti (voto 40-80)', '',
         '1. Client collegato al server (il server registra il nome): +15.', '2. Commit chiaro su GitHub (messaggio che dice cosa è stato fatto): +15.', '3. Quiz rete 8 su 12 o più: +10.',
         '4. Il voto parte da 40; i tre KPI portano a 80. Il cruscotto mostra per primi questi tre, una spunta per ragazzo.', '',
         '## 4 Teoria (schede con disegno)', '']
    for k, (ti, te, im, no, bn) in enumerate(TEORIA, 1):
        m += ['### 4.%d %s' % (k, ti), '', te, '', '![schema](img/teoria-%d.svg)' % k, '', no, '', '> Aiuto in bangla (solo PC 14, blocco opzionale): ' + bn, '']
    m += ['## 5 Esercizio ora 1: il Prof finto', '',
          'Pagina `lezione.html`. Un server finto in JavaScript (stesse regole di UnitServer) risponde a STATO e GUESS. Il ragazzo scrive il suo nome (fallo tuo), fa comparire le 5 risposte STATO, WAIT, RESULT, WIN, ERR (un segno verde per ogni risposta scoperta, "FATTO!" a 5 su 5) e poi spiega a voce una riga a un compagno (prova del nove). Tutto al PC, niente carta e telefono.', '',
          '## 6 Ora 2: i passi (ognuno con il suo schema)', '']
    for k, (ti, te, im, no) in enumerate(passi2, 1):
        import re
        txt = re.sub(r'<[^>]+>', '', te)
        m += ['%d. **%s.** %s' % (k, ti, txt), '', '   ![schema](img/ora2-%d.svg)' % k, '']
        if no: m += ['   Nota: ' + re.sub(r'<[^>]+>', '', no), '']
        if k == 10: m += ['   Messaggio di commit da copiare:', '', '```', copia, '```', '']
    m += ['## 7 Quiz sulla rete (12 domande, da trasformare in Modulo con il ponte, NON ancora creato)', '', 'File pronto: `quiz-rete-12.json` (formato forms.crea_quiz) e `quiz-rete-12.md`. Soglia per il KPI: 8 su 12. Regola 33: il quiz vale come prova solo se è il Modulo allegato al compito su Classroom.', '',
          '## 8 Controlli prima di pubblicare', '',
          '1. Il docente guarda animazione, teoria e compito (regola 7).', '2. Si decide chi vede il blocco in bangla (solo PC 14) e lo si fa controllare da chi lo legge: l\'ho scritto io.',
          '3. Gli schemi vanno sostituiti con screenshot veri di Lazarus e GitHub se disponibili (regola 32).', '4. Il server del Prof deve essere acceso e l\'IP scritto alla lavagna prima dell\'ora 2.', '5. Prima di pubblicare su Classroom: `bash strumenti/prima_di_pubblicare.sh "<titolo>"` (regola 34). Una ora per volta (regola 31).', '']
    return '\n'.join(m)


def quiz_md():
    m = ['# Quiz di rete: il protocollo del Mastermind (12 domande)', '', 'Soglia KPI: 8 su 12. La risposta giusta è la prima di ogni elenco (nel Modulo le risposte si mescolano).', '']
    for k, (q, ok, sb) in enumerate(QUIZ, 1):
        m += ['%d. %s' % (k, q), '   - GIUSTA: %s' % ok] + ['   - sbagliata: %s' % x for x in sb] + ['']
    return '\n'.join(m)



def bigchips(x, y, items, vs, ls, wd, gap=14):
    """casellette grandi per la lavagna: items = [(valore, etichetta)]"""
    out = ''; cx = x
    for i, (v, lab) in enumerate(items):
        out += box(cx, y, wd[i], 130, '#fff', CB if i == 0 else BD, 6 if i == 0 else 3, 14)
        out += t(cx + wd[i] / 2, y + 68, v, vs, INK, 'middle', i == 0, True)
        out += t(cx + wd[i] / 2, y + 112, lab, ls, MU, 'middle')
        cx += wd[i] + gap
    return out

# ------------------------------------------------------------------ la LAVAGNA (A4 orizzontale, grandi disegni, poche parole)
def lavagna_html():
    W = 'font-family="system-ui,Segoe UI,Arial,sans-serif"'

    def pg(n, titolo, body, parola=''):
        return ('<section class="pg"><div class="n">%d</div><h1>%s</h1><div class="fig">%s</div>%s</section>' % (n, titolo, body, ('<p class="w">%s</p>' % parola) if parola else ''))

    def big(w, h, body, label):
        return svg(w, h, body, label).replace(PAPER, '#ffffff')

    pages = []
    # 1 titolo
    f = big(1000, 400, box(40, 60, 330, 280, '#eaf3fb', CB, 6) + t(205, 160, 'CLIENT', 60, CB, 'middle', True) + t(205, 230, 'Sara', 44, MU, 'middle') +
            box(630, 60, 330, 280, '#fbeee1', SR, 6) + t(795, 160, 'SERVER', 60, SR, 'middle', True) + t(795, 230, 'il Prof', 44, MU, 'middle') +
            '<rect x="370" y="170" width="260" height="60" rx="30" fill="#d9d2c0" stroke="%s" stroke-width="4"/>' % BD + t(500, 212, 'rete', 38, MU, 'middle'), 'Client e server')
    pages.append(pg(1, 'Come parlano due programmi?', f, 'Mastermind in rete. Capiamo la UnitRete e il protocollo.'))
    # 2 porta
    f = big(1000, 400, box(40, 60, 330, 280, '#eaf3fb', CB, 6) + t(205, 190, 'CLIENT', 60, CB, 'middle', True) +
            box(630, 60, 330, 280, '#fbeee1', SR, 6) + t(795, 160, 'SERVER', 60, SR, 'middle', True) + t(795, 260, '5050', 90, INK, 'middle', True, True) +
            '<rect x="370" y="170" width="260" height="60" rx="30" fill="#d9d2c0" stroke="%s" stroke-width="4"/>' % BD, 'La porta 5050')
    pages.append(pg(2, 'Il server ascolta alla porta 5050', f, 'La porta è il numero della sua porta.'))
    # 3 riga va torna
    f = big(1000, 400, box(30, 40, 200, 320, '#eaf3fb', CB, 6) + t(130, 210, 'CLIENT', 38, CB, 'middle', True) + box(770, 40, 200, 320, '#fbeee1', SR, 6) + t(870, 210, 'SERVER', 38, SR, 'middle', True) +
            arrow(240, 120, 760, 120, CB, 10) + t(500, 100, 'UNA riga va', 46, CB, 'middle', True) + arrow(760, 290, 240, 290, SR, 10) + t(500, 340, 'UNA riga torna', 46, SR, 'middle', True), 'Una riga va, una torna')
    pages.append(pg(3, 'Una riga va, una riga torna', f))
    # 4 campi
    cs = bigchips(40, 70, [('RESULT', 'tipo'), ('1', 'neri'), ('2', 'bianchi')], 66, 34, [340, 170, 220], 90)
    f = big(1000, 520, cs + t(425, 190, ';', 140, SR, 'middle', True, True) + t(685, 190, ';', 140, SR, 'middle', True, True) + t(500, 380, 'punto e virgola tra un campo e l\'altro', 44, INK, 'middle', True) +
            t(500, 450, 'RESULT;1;2', 70, CB, 'middle', True, True), 'Campi')
    pages.append(pg(4, 'Una riga è fatta di campi', f, 'Il primo campo dice che cosa è.'))
    # 5 domande
    f = big(1000, 400, box(60, 40, 880, 140, '#eaf3fb', CB, 6) + t(500, 120, 'STATO;Sara', 70, INK, 'middle', True, True) + t(500, 165, 'come va la partita?', 30, MU, 'middle') +
            box(60, 210, 880, 150, '#eaf3fb', CB, 6) + t(500, 290, 'GUESS;Sara;1234', 70, INK, 'middle', True, True) + t(500, 340, 'ecco il mio tentativo (colori da 1 a 6)', 30, MU, 'middle'), 'Due domande')
    pages.append(pg(5, 'Il client fa DUE domande', f))
    # 6 risposte
    rows = [('STATO;...', 'la classifica'), ('WAIT', 'aspetta il Via'), ('RESULT;...', 'neri e bianchi'), ('WIN;...', 'hai vinto!'), ('ERR;...', 'errore')]
    body = ''
    for i, (a, b) in enumerate(rows):
        y = 20 + i * 76
        body += box(40, y, 920, 66, '#fbeee1', SR, 4, 12) + t(70, y + 48, a, 46, INK, 'start', True, True) + t(500, y + 46, b, 38, MU)
    pages.append(pg(6, 'Il server dà CINQUE risposte', big(1000, 400, body, 'Cinque risposte')))
    # 7 RESULT
    cs = bigchips(10, 20, [('RESULT', 'tipo'), ('1', 'neri'), ('2', 'bianchi'), ('1', 'prove'), ('0', 'posto'), ('1', 'finiti'), ('6', 'migl.'), ('6', 'pegg.')], 44, 26, [230, 80, 120, 90, 90, 90, 90, 90])
    f = big(1000, 520, cs + peg(90, 280, 46, '#111') + t(150, 298, '= 1 nero', 54, INK) + peg(470, 280, 46, '#f4f4f4') + peg(560, 280, 46, '#f4f4f4') + t(620, 298, '= 2 bianchi', 54, INK) +
            t(500, 450, 'nero: giusto al posto giusto', 46, INK, 'middle') + t(500, 505, 'bianco: giusto ma al posto sbagliato', 46, MU, 'middle'), 'RESULT letto campo per campo')
    pages.append(pg(7, 'Leggiamo una risposta', f))
    # 8 partita
    b = t(100, 44, 'CLIENT', 48, CB, 'middle', True) + t(900, 44, 'SERVER', 48, SR, 'middle', True)
    ms = [('STATO;Sara', 'STATO;ATTESA;...'), ('GUESS;Sara;1234', 'WAIT'), ('GUESS;Sara;1234', 'RESULT;1;2;...'), ('GUESS;Sara;1413', 'WIN;Sara;3;...')]
    y = 110
    for a, r in ms:
        b += arrow(60, y, 940, y, CB, 8) + t(500, y - 14, a, 42, CB, 'middle', True, True) + arrow(940, y + 52, 60, y + 52, SR, 8) + t(500, y + 34, r, 42, SR, 'middle', True, True)
        y += 108
    pages.append(pg(8, 'Una partita', big(1000, 540, b, 'Partita'), 'Il Prof preme Via tra la seconda e la terza.'))
    # 9 unit
    f = big(1000, 520, box(30, 20, 560, 170, '#eaf3fb', CB, 8) + t(310, 125, 'UnitInterfaccia', 60, CB, 'middle', True) + box(30, 330, 560, 170, '#fff', INK, 8) + t(310, 435, 'UnitRete', 60, INK, 'middle', True) +
            arrow(130, 200, 130, 320, CB, 12) + t(165, 275, 'chiama', 36, CB) + arrow(500, 320, 500, 200, '#c47a00', 12) + t(485, 275, 'EVENTO', 36, '#c47a00', 'end', True) +
            box(700, 330, 280, 170, '#fbeee1', SR, 8) + t(840, 435, 'Server', 56, SR, 'middle', True) + arrow(600, 400, 690, 400, INK, 9) + arrow(690, 440, 600, 440, INK, 9) +
            t(840, 80, 'UnitRete non', 44, INK, 'middle', True) + t(840, 135, 'conosce la', 44, INK, 'middle', True) + t(840, 190, 'finestra', 44, INK, 'middle', True), 'Due unit')
    pages.append(pg(9, 'Il client ha due pezzi', f, 'La rete avvisa la finestra con un evento, come OnClick.'))
    # 10 tocca a te
    f = big(1000, 400, box(60, 40, 880, 320, '#fffbe6', '#d4a017', 6) + t(500, 140, 'Ora provi tu', 70, INK, 'middle', True) + t(500, 230, 'scopri le 5 risposte del server', 46, INK, 'middle') + t(500, 300, 'STATO  WAIT  RESULT  WIN  ERR', 52, SR, 'middle', True, True), 'Tocca a te')
    pages.append(pg(10, 'Tocca a te', f))
    css = """@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Segoe UI",Arial,sans-serif;color:#1d1d1f;background:#fff}
.pg{width:297mm;height:210mm;padding:10mm 14mm;page-break-after:always;position:relative;overflow:hidden}
.pg h1{font-size:40pt;margin:0 0 4mm;line-height:1.1}.pg .n{position:absolute;right:12mm;top:8mm;font-size:18pt;color:#9a9384}
.fig svg{width:100%;height:auto;display:block;max-height:150mm}.w{font-size:28pt;margin:4mm 0 0;color:#444;text-align:center}"""
    return '<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Il protocollo alla lavagna</title><style>%s</style></head><body>%s</body></html>' % (css, ''.join(pages))


# ------------------------------------------------------------------ scrittura
def w(path, s):
    with open(os.path.join(OUT, path), 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    for k, (ti, te, im, no, bn) in enumerate(TEORIA, 1):
        w('img/teoria-%d.svg' % k, im)
    o2, passi, copia = ora2_pagine()
    for k, (ti, te, im, no) in enumerate(passi, 1):
        w('img/ora2-%d.svg' % k, im)
    w('lezione.html', ora1_html())
    w('ora2.html', o2)
    w('lezione.md', md_lezione(passi, copia))
    w('quiz-rete-12.json', json.dumps(quiz_json(), ensure_ascii=False, indent=1))
    w('quiz-rete-12.md', quiz_md())
    w('lavagna.html', lavagna_html())
    print('ok')


main()
