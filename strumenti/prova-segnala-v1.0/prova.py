"""Prova dello snippet in Chromium contro il server finto (porta 8765). Uso: node server_finto.js & python3 prova.py"""
import json, sys, time, urllib.request
from playwright.sync_api import sync_playwright
def eventi(): return json.load(urllib.request.urlopen('http://localhost:8765/eventi'))
ok = True
def verifica(nome, cond):
    global ok; ok = ok and cond; print(('OK   ' if cond else 'FALLITO ') + nome)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 800, 'height': 600}); pg.goto('http://localhost:8765/')
    pg.fill('#cs_in', 'Mario'); pg.click('form button'); time.sleep(.3)
    verifica('nome con una sola parola rifiutato', 'Scrivi nome e cognome' in pg.inner_text('#cs_er') and not eventi())
    pg.fill('#cs_in', 'Prova Tester Rossi'); pg.click('form button'); time.sleep(.5)
    e = eventi(); verifica('dopo il nome: evento visto con «Prova R.» (cognome non inviato)', e and e[0]['s'] == 'visto' and e[0]['a'] == 'Prova R.' and 'Tester' not in json.dumps(e))
    verifica('passo 1 visibile: avanzato 1/3', any(x['s'] == 'avanzato' and x['n'] == 1 and x['m'] == 3 for x in eventi()))
    for _ in range(3): pg.mouse.wheel(0, 1000); time.sleep(.6)
    e = eventi(); verifica('scroll: iniziato', any(x['s'] == 'iniziato' for x in e))
    verifica('scroll veloce (salta oltre il passo 3): raggiunto comunque 3/3', any(x['s'] == 'avanzato' and x['n'] == 3 and x['m'] == 3 for x in e))
    time.sleep(2.2); e = eventi(); verifica('battito: secondi di tempo attivo > 0', max(x.get('sec', 0) for x in e) >= 1)
    n0 = len(e); pg.click('#fine'); time.sleep(.5); e = eventi()
    verifica('consegnato con n=3 m=3', e[-1]['s'] == 'consegnato' and e[-1]['n'] == 3)
    time.sleep(2.2); verifica('dopo la consegna nessun altro evento', len(eventi()) == len(e))
    verifica('tutti con tipo, id, classe, sessione, ora', all(x['t'] == 'teoria' and x['id'] == 'prova-pagina-v1' and x['cl'] == '2INF' and x['se'] and x['ts'] for x in e))
    pg.reload(); time.sleep(.6); e2 = eventi()
    verifica('ricarico: nome ricordato dal browser, nessuna richiesta del nome, nuovo «visto»', pg.query_selector('#cs_in') is None and any(x['s'] == 'visto' and x['m'] == 3 and x['a'] == 'Prova R.' for x in e2[len(e):]))
    print('eventi totali:', len(eventi())); print(json.dumps([{k: x[k] for k in ('a','s','n','m','sec')} for x in eventi()]))
    b.close()
sys.exit(0 if ok else 1)
