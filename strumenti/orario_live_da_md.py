#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Orario del cruscotto in tempo reale (20/11/2026): legge orario/settimana-AAAA-MM-GG.md (tabella del registro DIDAweb,
copiata dal docente) e scrive fabbrica/orario-live.json (letto dal job Apps Script) e docs/live/orario-live.json (letto dalla pagina).
Nessun nome di allievi. Uso (dal repository pubblico):  python3 strumenti/orario_live_da_md.py orario/settimana-2026-11-16.md
Regole: ora n = n-esima ora della giornata (1 = 08-09 ... 6 = 13-14, come PUBB n); le righe «DA CONFERMARE» (classe '-') NON entrano
(ora libera = nessuna lezione con il docente); la validita e' da lunedi a venerdi della settimana del file; l'anno viene dal nome del file.
"""
import datetime, json, os, re, sys

GG = {'lun': 0, 'mar': 1, 'mer': 2, 'gio': 3, 'ven': 4}
CLASSI = ('1INF', '2INF', '3INF', '4TI')


def tipo_di(materia):
    m = materia.lower()
    return 'laboratorio' if ('laboratorio' in m or '(lab)' in m) else 'disciplina'


def leggi(md, anno):
    giorni = {g: {} for g in GG}
    fonte_v = re.search(r'\*\*Versione ([0-9.]+)\*\*', md)
    for riga in md.splitlines():
        c = [x.strip() for x in riga.strip().strip('|').split('|')]
        if len(c) != 4:
            continue
        m = re.match(r'(Lun|Mar|Mer|Gio|Ven) (\d\d)/(\d\d)$', c[0])
        o = re.match(r'(\d\d)-(\d\d)', c[1])
        if not (m and o):
            continue
        classe = c[2].upper()
        if classe not in CLASSI:
            continue   # '—' = da confermare: non si dichiara una lezione che non e' confermata
        materia = re.sub(r'\s*\(lab\)\s*$', '', c[3]).strip()
        g = m.group(1).lower()
        a, b = int(o.group(1)), int(o.group(2))
        for h in range(a, b):
            n = h - 7
            if not 1 <= n <= 6:
                raise SystemExit('ora fuori da 1-6 nella riga: ' + riga)
            voce = {'classe': classe, 'materia': materia, 'tipo': tipo_di(c[3])}
            k = 'ora_%d' % n
            if k not in giorni[g]:
                giorni[g][k] = voce
            else:   # due classi nella stessa ora (con il docente): la chiave diventa un elenco; la stessa classe due volte e un errore
                v = giorni[g][k] if isinstance(giorni[g][k], list) else [giorni[g][k]]
                if any(x['classe'] == classe for x in v):
                    raise SystemExit('stessa classe due volte nella stessa ora: ' + riga)
                giorni[g][k] = v + [voce]
    return giorni, (fonte_v.group(1) if fonte_v else '?')


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    p = sys.argv[1]
    nome = os.path.basename(p)
    m = re.match(r'settimana-(\d{4})-(\d\d)-(\d\d)\.md$', nome)
    if not m:
        raise SystemExit('il nome del file deve essere settimana-AAAA-MM-GG.md')
    lun = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if lun.weekday() != 0:
        raise SystemExit('la data nel nome del file non e un lunedi')
    giorni, ver = leggi(open(p, encoding='utf-8').read(), lun.year)
    if not any(giorni.values()):
        raise SystemExit('nessuna lezione letta: tabella non riconosciuta')
    out = {
        'versione': '1.0',
        'valido_dal': lun.isoformat(),
        'valido_al': (lun + datetime.timedelta(days=4)).isoformat(),
        'fonte': 'orario/%s v%s (registro DIDAweb, tabella copiata dal docente)' % (nome, ver),
        'generato_da': 'strumenti/orario_live_da_md.py',
        'ore_registro': {str(n): '%02d:00-%02d:00' % (7 + n, 8 + n) for n in range(1, 7)},
        'giorni': {g: giorni[g] for g in GG},
    }
    testo = json.dumps(out, ensure_ascii=False, indent=1) + '\n'
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for rel in ('fabbrica/orario-live.json', 'docs/live/orario-live.json'):
        open(os.path.join(base, rel), 'w', encoding='utf-8').write(testo)
        print('scritto', rel)
    for g in GG:
        print(g, ', '.join('%s=%s' % (k[4:], '+'.join(x['classe'] for x in (v if isinstance(v, list) else [v]))) for k, v in sorted(giorni[g].items())) or '-')


if __name__ == '__main__':
    main()
