#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Piano B di mercoledì 04/11/2026: titoli e testi pronti da copiare (md nel riservato, html senza nomi nel pubblico).
import glob, html, json, os
R = '/home/user/corso-informatica-riservato/'
U = 'https://nicolaregge-pulse.github.io/corso-informatica/anteprima/'
coda = {}
for f in sorted(glob.glob(R + 'coda/2026-11-04_*.json')):
    c = json.load(open(f, encoding='utf-8')); coda[os.path.basename(f)[11:-5]] = c
T31 = ("OGGI 4/11, ORA 1: il tuo Mastermind si collega al server.\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "3inf-mastermind-04-11/ <<<\n"
       "La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.\n\nIP del server: 192.168.38.70 (porta 5050, già dentro il programma).\n"
       "PASSO 1-4: apri il progetto mastermind-client, F9, scrivi IP e nome, premi Connetti.\nPASSO 5: quando il Prof dice Via, gioca.\nPASSO 6-7: screenshot e «Manda al prof».\n\nA che punto sono:\n" + U + "3inf-mastermind-04-11/cruscotto-ragazzi.html\n\nHai una domanda? Scrivila nella casella dell'assistente, in fondo alla pagina di oggi.")
ORDINE = [('1INF · ORE 8:00 (ora 1)', '1INF_ora1-convertitore', '1inf-lab-04-11 1'), ('1INF · ORE 9:00 (ora 2)', '1INF_ora2-calcolatrice', '1inf-lab-04-11 2'),
          ('1INF · ORE 10:00 (ora 3)', '1INF_ora3-cassiere', '1inf-lab-04-11 3'), ('2INF · ORE 11:00 (Sicurezza)', '2INF_sicurezza-6ora', '2inf-sicurezza-04-11 1'),
          ('3INF · ORE 12:00 (ora 1) — compito creato a mano dal docente, non modificabile', None, '3inf-mastermind-04-11 1'), ('3INF · ORE 13:00 (ora 2)', '3INF_ora2-partita-github-quiz', '3inf-mastermind-04-11 2')]
blocchi = []  # (titolo sezione, [(etichetta, testo)], sblocco)
for sez, k, sb in ORDINE:
    if k: c = coda[k]; b = [('Titolo da copiare:', c['titolo']), ('Testo da copiare:', c['descrizione'])]
    else: b = [('Titolo da copiare:', '4/11 Ora 1: il tuo Mastermind si collega al server (client)'), ('Testo da copiare (da incollare nel compito che hai già creato, o in uno nuovo):', T31)]
    blocchi.append((sez, b, sb))
INTRO = ["Se il ponte non mostra i compiti, si fa a mano. UN compito alla volta, all'inizio di ogni ora, mai le ore successive (regola 31). Nessun nome di ragazzi in questo file.",
         "Prima di cominciare (ogni compito)",
         "1. Apri Classroom, scheda «Lavori del corso» della classe, e cerca il titolo: se esiste già (anche in bozza) NON crearlo un'altra volta (anti-doppione, regola 34). Il ponte può averlo già creato come bozza invisibile: allora basta «Pubblica» sulla bozza.",
         "2. Se non esiste: clicca «Crea», poi «Compito». Copia il titolo dal riquadro e incollalo nella casella «Titolo».",
         "3. Copia il testo dal secondo riquadro e incollalo nella casella «Istruzioni».", "4. Lascia vuota la data di consegna.", "5. Clicca «Assegna».",
         "6. Scrivimi «pubblicato a mano» e io tolgo il comando dalla coda, così il ponte non crea un doppione."]
md = ['# Piano B: pubblicare a mano i compiti di mercoledì 04/11/2026', '', INTRO[0], '', '## ' + INTRO[1], ''] + INTRO[2:] + ['', '## Ordine giusto della mattina', '']
for sez, b, sb in blocchi:
    md += ['### ' + sez, '']
    for e, t in b: md += [e, '', '```', t, '```', '']
    md += ['Poi sblocca la pagina di quest\'ora (lo faccio io con `python3 strumenti/sblocca_ora.py %s`).' % sb, '']
md += ['## Link utili', '', 'Cruscotto dei ragazzi e assistente: già dentro il testo di ogni compito. Link dei quiz su Moduli: già dentro il testo dei compiti 1INF ora 1 e 2INF.', '']
os.makedirs(R + 'report/2026-11-04', exist_ok=True)
open(R + 'report/2026-11-04/PIANO-B-PUBBLICAZIONE-04-11.md', 'w', encoding='utf-8').write('\n'.join(md))
E_ = html.escape; BT = '<button onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);this.textContent=\'Copiato!\'">Copia</button>'
h = ['<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Piano B 04/11</title><style>body{font:18px/1.5 system-ui;max-width:860px;margin:0 auto;padding:12px 16px;background:#f6f7f9;color:#1f2328}pre{background:#fff;border:1px solid #c9d1da;border-radius:10px;padding:10px;white-space:pre-wrap;word-break:break-word}button{font:inherit;font-weight:700;padding:6px 14px;border-radius:8px;border:2px solid #0b6e99;background:#fff;color:#0b6e99;cursor:pointer;margin:0 0 14px}h3{margin-top:28px}</style></head><body>',
     '<h1>Piano B: pubblicare a mano i compiti di mercoledì 04/11/2026</h1>', '<p>%s</p>' % E_(INTRO[0]), '<h2>%s</h2>' % INTRO[1]] + ['<p>%s</p>' % E_(x) for x in INTRO[2:]] + ['<h2>Ordine giusto della mattina</h2>']
for sez, b, sb in blocchi:
    h.append('<h3>%s</h3>' % E_(sez))
    for e, t in b: h += ['<p>%s</p>' % E_(e), '<pre>%s</pre>%s' % (E_(t), BT)]
    h.append('<p>Poi sblocca la pagina di quest\'ora (lo faccio io con <code>strumenti/sblocca_ora.py %s</code>).</p>' % sb)
h.append('<p>Cruscotto dei ragazzi e assistente: già dentro il testo di ogni compito.</p></body></html>')
open('/home/user/corso-informatica/docs/prof-pubblica/piano-b-04-11.html', 'w', encoding='utf-8').write('\n'.join(h))
print('piano B scritto;', sum('__QUIZ' in t for _, b, _ in blocchi for _, t in b), 'blocchi con segnaposto')
