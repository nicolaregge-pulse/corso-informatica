# VERIFICA della gara: confronta cio' che hanno visto i client e la sonda con i conti del server (gara_dump.txt)
# e ricalcola i punteggi con la formula, in modo indipendente da UnitGara.
# Uso: python3 verifica_gara.py cartella_uscita num_nuovi num_vecchi
import sys, os, re, glob
OUT = sys.argv[1]; NNUOVI = int(sys.argv[2]); NVECCHI = int(sys.argv[3])
err = []
def ok(c, msg):
    print(('  ok   ' if c else '  ERRORE ') + msg)
    if not c: err.append(msg)
# --- la formula, riscritta qui (diversa da UnitGara) ---
def punti(vic, risolto, rank, tent):
    p = vic * 10
    if risolto: p += 50 + {1: 30, 2: 20, 3: 10}.get(rank, 0)
    p -= max(0, tent - 6)
    return max(0, p)
# --- dump del server ---
dump = {}      # nome -> {'round': {k: dict}, 'tot':..., 'tent':..., 'tempo':..., 'pos':...}
stato = None
for r in open(os.path.join(OUT, 'gara_dump.txt')):
    f = r.split()
    if f[0] == 'STATO': stato = r.strip()
    elif f[0] == 'ROUND':
        d = {a.split('=')[0]: int(a.split('=')[1]) for a in f[3:]}
        dump.setdefault(f[1], {'round': {}})['round'][int(f[2])] = d
    elif f[0] == 'TOT':
        d = {a.split('=')[0]: int(a.split('=')[1]) for a in f[2:]}
        dump.setdefault(f[1], {'round': {}}).update(d)
ok('round_chiusi=3' in stato and stato.split()[1] == '3', 'la gara e'' finita (stato 3) con 3 round chiusi: ' + stato)
# --- 1. punteggio di ogni round ricalcolato ---
for n, d in dump.items():
    for k, r in d['round'].items():
        calc = punti(r['vic'], r['risolto'] == 1, r['rank'], r['tent'])
        if calc != r['punti']: ok(False, '%s round %d: server %d, formula %d' % (n, k, r['punti'], calc))
ok(not [1 for n in dump for k, r in dump[n]['round'].items() if punti(r['vic'], r['risolto'] == 1, r['rank'], r['tent']) != r['punti']],
   'tutti i punteggi di round del server coincidono con la formula (%d righe)' % sum(len(d['round']) for d in dump.values()))
# --- 2. ranghi di velocita' 1..m senza buchi ---
for k in (1, 2, 3):
    rk = sorted(d['round'][k]['rank'] for d in dump.values() if k in d['round'] and d['round'][k]['risolto'] == 1)
    ok(rk == list(range(1, len(rk) + 1)), 'round %d: i %d che hanno risolto hanno bonus velocita'' 1..%d senza buchi' % (k, len(rk), len(rk)))
# --- 3. totali e posizioni ---
for n, d in dump.items():
    if sum(r['punti'] for r in d['round'].values()) != d['tot']: ok(False, '%s: totale %d != somma round' % (n, d['tot']))
    if sum(r['tent'] for r in d['round'].values()) != d['tent']: ok(False, '%s: tentativi %d != somma round' % (n, d['tent']))
ok(all(sum(r['punti'] for r in d['round'].values()) == d['tot'] and sum(r['tent'] for r in d['round'].values()) == d['tent'] for d in dump.values()),
   'totale e tentativi di ognuno = somma dei round')
def chiave(n): return (-dump[n]['tot'], dump[n]['tent'], dump[n]['tempo'])
pos = {n: 1 + sum(1 for m in dump if chiave(m) < chiave(n)) for n in dump}
ok(all(pos[n] == dump[n]['pos'] for n in dump), 'le posizioni del server coincidono con quelle ricalcolate (punti, poi tentativi, poi tempo)')
ordine = sorted(dump, key=lambda n: (chiave(n), n.lower()))
# --- 4. i client nuovi ---
nuovi = sorted(glob.glob(os.path.join(OUT, 'n*.log')))
ok(len(nuovi) == NNUOVI, 'ci sono i log dei %d client nuovi' % NNUOVI)
giocatori_gara = [n for n in dump if n != 'Sonda']
for lf in nuovi:
    righe = open(lf).read().splitlines()
    nome = None; fine = None; ris = {}
    for r in righe:
        m = re.match(r'RIS (\S+) k=(\d+) tent=(\d+) best=(\d+) solved=(\d)', r)
        if m: nome = m.group(1); ris[int(m.group(2))] = (int(m.group(3)), int(m.group(4)), int(m.group(5)))
        m = re.match(r'FINE (\S+) pos=(\d+) tot=(\d+) n=(\d+) primo=(\S*) (\d+)', r)
        if m: fine = m.groups()
        if 'ERRORE' in r: ok(False, lf + ': ' + r)
    if not fine: ok(False, lf + ': manca la riga FINE'); continue
    nome = fine[0]
    d = dump[nome]
    for k in (1, 2, 3):
        c = ris.get(k); s = d['round'].get(k)
        if c is None or s is None: ok(False, '%s round %d mancante' % (nome, k)); continue
        if (c[0], c[1], c[2]) != (s['tent'], s['vic'], s['risolto']):
            ok(False, '%s round %d: client %s, server tent=%d vic=%d risolto=%d' % (nome, k, c, s['tent'], s['vic'], s['risolto']))
    if (int(fine[1]), int(fine[2])) != (d['pos'], d['tot']): ok(False, '%s: il client ha ricevuto pos=%s tot=%s, il server ha pos=%d tot=%d' % (nome, fine[1], fine[2], d['pos'], d['tot']))
    if int(fine[3]) != len(giocatori_gara): ok(False, '%s: giocatori %s, in gara %d' % (nome, fine[3], len(giocatori_gara)))
    if fine[4] != ordine[0] or int(fine[5]) != dump[ordine[0]]['tot']: ok(False, '%s: il primo per il client e'' %s %s, per il server %s %d' % (nome, fine[4], fine[5], ordine[0], dump[ordine[0]]['tot']))
ok(not [e for e in err], 'ogni client nuovo: tentativi, vicinanza, risolto per ogni round, e posizione/punti/primo finali = quelli del server')
# --- 5. i client vecchi (v4.0.1) ---
vecchi = sorted(glob.glob(os.path.join(OUT, 'v*.log')))
ok(len(vecchi) == NVECCHI, 'ci sono i log dei %d client vecchi (v4.0.1)' % NVECCHI)
for lf in vecchi:
    t = open(lf).read()
    ok(' FINE ' in t and 'ERRORE' not in t, '%s: il client v4.0.1 ha giocato il codice 1 fino alla vittoria, senza errori' % os.path.basename(lf))
vn = [n for n in dump if n.startswith('Vecchio')]
ok(len(vn) == NVECCHI and all(dump[n]['round'][1]['risolto'] == 1 for n in vn), 'il server ha contato la vittoria dei client vecchi nel codice 1 (e i punti: %s)' % [dump[n]['round'][1]['punti'] for n in vn])
# --- 6. quello che e' passato in rete ---
fin = dict(r.rstrip('\n').split('|', 1) for r in open(os.path.join(OUT, 'sonda_finale.txt')) if '|' in r)
mal = 0
for n in giocatori_gara:
    r = fin.get(n, '')
    parti = r.split(' // ')
    m = re.match(r'CLASSIFICA;(\d+);(\d+);(\d+);([^;]*);(\d+)$', parti[1]) if len(parti) > 1 else None
    f = re.match(r'FINEGARA;(\d+);(\d+);(\d+)$', parti[2]) if len(parti) > 2 else None
    if not (parti[0].startswith('STATO;ATTESA;') and m and f): mal += 1; print('   risposta strana per', n, ':', r); continue
    if (int(m.group(1)), int(m.group(2))) != (dump[n]['pos'], dump[n]['tot']) or (int(f.group(1)), int(f.group(2))) != (dump[n]['pos'], dump[n]['tot']):
        mal += 1; print('   NON coincide per', n, r, dump[n]['pos'], dump[n]['tot'])
    if m.group(4) != ordine[0] or int(m.group(5)) != dump[ordine[0]]['tot']: mal += 1; print('   primo diverso per', n, r)
ok(mal == 0 and len(giocatori_gara) > 0, 'la risposta di rete (STATO + CLASSIFICA + FINEGARA) per tutti i %d giocatori coincide con i conti del server' % len(giocatori_gara))
pr = fin.get('PRIMA_RIGA', '')
ok(pr.startswith('STATO;') and 'CLASSIFICA' not in pr and 'ROUND' not in pr and pr.count(';') == 6, 'la PRIMA riga (l''unica letta da un client v4.0.1) e'' quella di sempre, 7 campi: ' + pr)
# --- 7. la traccia durante la gara ---
righe = [l.rstrip('\n') for l in open(os.path.join(OUT, 'trace.txt')) if '|' in l]
ultimo_k = 0; cattive = 0; visti_round = set(); max_sec = 0
for l in righe:
    parti = l.split('|', 1)[1].split(' // ')
    if not parti[0].startswith('STATO;'): cattive += 1; continue
    for p in parti[1:]:
        c = p.split(';')
        if c[0] == 'ROUND':
            k, N, sec = int(c[1]), int(c[2]), int(c[3])
            if k < ultimo_k or N != 3 or sec < 0 or sec > 14: cattive += 1
            ultimo_k = max(ultimo_k, k); visti_round.add(k); max_sec = max(max_sec, sec)
        elif c[0] == 'CLASSIFICA':
            if len(c) != 6 or not (1 <= int(c[1]) <= int(c[3])): cattive += 1
        elif c[0] == 'FINEGARA':
            if len(c) != 4: cattive += 1
        else: cattive += 1
ok(len(righe) > 20 and cattive == 0, 'traccia della gara: %d risposte, tutte ben fatte; round visti %s, secondi massimi %d' % (len(righe), sorted(visti_round), max_sec))
ok(visti_round == {1, 2, 3}, 'la sonda ha visto passare i codici 1, 2 e 3')
# --- 8. i motivi con cui sono finiti i round (dal registro del server) ---
reg = open(os.path.join(OUT, 'registro.txt')).read()
m = re.findall(r'CODICE (\d) FINITO \(([^)]*)\)', reg)
ok(m == [('1', 'tutti hanno trovato il codice'), ('2', "e' scaduto il tempo"), ('3', 'il Prof ha detto basta')],
   'i tre round sono finiti nei TRE modi: tutti hanno risolto, tempo scaduto, Prof che preme Prossimo: ' + str(m))
ok('GARA FINITA' in reg, 'il registro del server dice GARA FINITA')
print()
if err: print('VERIFICA GARA FALLITA: %d errori' % len(err)); sys.exit(1)
print('VERIFICA GARA: tutto ok')
