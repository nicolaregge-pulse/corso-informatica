#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlla le spec della lavagna (docs/lavagna/spec/*.json) e riscrive spec/indice.json.

Uso (dal repository pubblico):  python3 strumenti/controlla_lavagna_spec.py [--indice]
Controlli: campi obbligatori, id = nome del file, tipi ammessi, immagini esistenti, rettangoli dentro l'immagine, bersagli e
risposte che puntano a zone esistenti, LINGUE PER CLASSE (R6: 1INF it+ar+zh in ogni testo; 2INF, 4TI solo it; 3INF it, bn solo
facoltativo), nessun cognome di allievo (R1, elenchi del riservato). Esce con 1 se c'e un errore."""
import glob, json, os, re, sys

RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAV = os.path.join(RAD, 'docs', 'lavagna')
TIPI = {'cerchia', 'disegna', 'collega', 'freccia', 'scegli'}
LINGUE_CLASSE = {'1INF': ['it', 'ar', 'zh'], '2INF': ['it'], '3INF': ['it'], '4TI': ['it']}
LINGUE_AMMESSE = {'1INF': {'it', 'ar', 'zh'}, '2INF': {'it'}, '3INF': {'it', 'bn'}, '4TI': {'it'}}


def privacy(testo):
    try:
        sys.path.insert(0, os.path.join(RAD, '.claude', 'hooks'))
        import controllo_nomi
        return controllo_nomi.trova(testo)
    except Exception:
        return []


def testi(o, percorso=''):
    """Tutti i dizionari di testo per lingua {it: ..} trovati nell'oggetto."""
    out = []
    if isinstance(o, dict):
        if 'it' in o and all(isinstance(v, str) for v in o.values()) and len(o) <= 4:
            out.append((percorso, o))
        else:
            for k, v in o.items():
                out += testi(v, percorso + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out += testi(v, percorso + '[%d]' % i)
    return out


def rett_ok(r, W, H):
    return isinstance(r, list) and len(r) == 4 and 0 <= r[0] < r[2] <= W and 0 <= r[1] < r[3] <= H


def controlla(path):
    err = []; avv = []
    nome = os.path.basename(path)[:-5]
    try:
        s = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        return ['JSON non valido: %s' % e], [], None
    for k in ('id', 'versione', 'classe', 'lingue', 'titolo', 'sfondo', 'passi'):
        if k not in s:
            err.append('manca il campo «%s»' % k)
    if err:
        return err, avv, s
    if s['id'] != nome:
        err.append('id «%s» diverso dal nome del file «%s»' % (s['id'], nome))
    cl = s['classe']
    if cl not in LINGUE_CLASSE:
        err.append('classe «%s» sconosciuta' % cl)
    else:
        if s['lingue'] != LINGUE_CLASSE[cl] and not (cl == '3INF' and s['lingue'] in (['it'], ['it', 'bn'])):
            err.append('lingue %s non ammesse per la %s (R6: %s)' % (s['lingue'], cl, LINGUE_CLASSE[cl]))
    W, H = (s.get('dimensioni') or [1200, 700])
    ids = set()
    for k, st in enumerate(s['passi']):
        sid = st.get('id', 'passo%d' % (k + 1))
        if sid in ids:
            err.append('id passo doppio: %s' % sid)
        ids.add(sid)
        t = st.get('tipo')
        if t not in TIPI:
            err.append('%s: tipo «%s» non ammesso' % (sid, t)); continue
        sf = (st.get('sfondo') or s['sfondo']).split('?')[0]
        if not os.path.exists(os.path.join(LAV, sf)):
            err.append('%s: immagine mancante %s' % (sid, sf))
        if 'testo' not in st:
            err.append('%s: manca il testo' % sid)
        zone = {z['id']: z for z in st.get('zone', [])}
        for z in zone.values():
            if not rett_ok(z.get('rett'), W, H):
                err.append('%s: zona %s con rettangolo non valido' % (sid, z.get('id')))
            if not (z.get('nome') or {}).get('it'):
                err.append('%s: zona %s senza nome in italiano' % (sid, z.get('id')))
        if t == 'cerchia':
            b = st.get('bersaglio')
            if isinstance(b, str):
                if b not in zone:
                    err.append('%s: bersaglio «%s» non e tra le zone' % (sid, b))
            elif isinstance(b, dict):
                if not rett_ok(b.get('rett'), W, H):
                    err.append('%s: bersaglio con rettangolo non valido' % sid)
            else:
                err.append('%s: manca il bersaglio' % sid)
            if isinstance(b, str) and len(zone) < 2:
                avv.append('%s: una sola zona, il controllo «un\'altra zona piu coperta» non serve' % sid)
        elif t == 'scegli':
            if st.get('giusta') not in zone:
                err.append('%s: «giusta» non e tra le zone' % sid)
            if len(zone) < 2:
                err.append('%s: servono almeno 2 zone' % sid)
        elif t == 'collega':
            for e in st.get('etichette', []):
                if e.get('zona') not in zone:
                    err.append('%s: etichetta %s con zona inesistente' % (sid, e.get('id')))
            if not st.get('etichette'):
                err.append('%s: nessuna etichetta' % sid)
        elif t == 'freccia':
            for lato in ('da', 'a'):
                if not rett_ok((st.get(lato) or {}).get('rett'), W, H):
                    err.append('%s: «%s» senza rettangolo valido' % (sid, lato))
    ammesse = LINGUE_AMMESSE.get(cl, {'it'})
    obbl = LINGUE_CLASSE.get(cl, ['it'])
    for p, d in testi(s):
        if p.endswith('/criteri') or '/criteri' in p:
            continue
        for l in d:
            if l not in ammesse:
                err.append('%s: lingua «%s» non ammessa per la %s' % (p, l, cl))
        for l in obbl:
            if not d.get(l):
                err.append('%s: manca la lingua «%s»' % (p, l))
    pr = privacy(json.dumps(s, ensure_ascii=False))
    if pr:
        err.append('PRIVACY: cognomi di allievi nella spec: %s' % ', '.join(pr))
    return err, avv, s


def main():
    files = sorted(f for f in glob.glob(os.path.join(LAV, 'spec', '*.json')) if not f.endswith('indice.json'))
    cattivi = 0; indice = []
    for f in files:
        err, avv, s = controlla(f)
        print('%s %s' % ('ERRORE' if err else 'ok    ', os.path.basename(f)))
        for e in err:
            print('   -', e)
        for a in avv:
            print('   ~', a)
        cattivi += bool(err)
        if s and not err:
            indice.append({'id': s['id'], 'classe': s['classe'], 'versione': s['versione'], 'titolo': {'it': s['titolo']['it']}, 'passi': len(s['passi'])})
    if '--indice' in sys.argv and not cattivi:
        with open(os.path.join(LAV, 'spec', 'indice.json'), 'w', encoding='utf-8') as fh:
            json.dump({'compiti': indice}, fh, ensure_ascii=False, indent=1); fh.write('\n')
        print('indice.json scritto con %d compiti' % len(indice))
    return 1 if cattivi else 0


if __name__ == '__main__':
    sys.exit(main())
