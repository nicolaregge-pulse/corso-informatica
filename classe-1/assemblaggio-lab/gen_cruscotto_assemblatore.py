#!/usr/bin/env python3
# Cruscotto del prof per il LAB ASSEMBLATORE (gioco "Monta il PC").
# Legge gli eventi inviati dall'app (docs/monta-pc-v3) e salvati dallo script
# in dati/verifiche/monta-pc-lab/arrivi/*.json (repo riservato).
# Produce un HTML: per ogni allievo assemblati, smontati, tempo medio, punteggio
# (montare = 1, smontare = 0,7) + classifica. NIENTE nel repo pubblico (contiene nomi).
#
# Uso:  python3 gen_cruscotto_assemblatore.py <cartella_arrivi> [out.html]
import sys, os, json, glob, html

def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else '../../../corso-informatica-riservato/dati/verifiche/monta-pc-lab/arrivi'
    out = sys.argv[2] if len(sys.argv) > 2 else 'cruscotto-assemblatore.html'
    ev = []
    for f in sorted(glob.glob(os.path.join(folder, '*.json'))):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if d.get('id') == 'monta-pc-lab' or d.get('tipo') in ('assemblato', 'smontato'):
            ev.append(d)
    stud = {}
    for d in ev:
        nm = (d.get('nome') or '').strip()
        if not nm:
            continue
        low = nm.lower()
        if low.startswith('prova') or low.startswith('test') or low.startswith('demo'):
            continue  # eventi di prova: non entrano nella classifica
        s = stud.setdefault(nm.lower(), {'nome': nm, 'asm': 0, 'dis': 0, 'ta': []})
        try:
            ms = float(d.get('ms') or 0)
        except Exception:
            ms = 0
        if d.get('tipo') == 'smontato':
            s['dis'] += 1
        else:
            s['asm'] += 1
            if ms > 0:
                s['ta'].append(ms)  # tempi solo ASSEMBLAGGIO
    rows = list(stud.values())
    for s in rows:
        s['pt'] = s['asm'] + 0.7 * s['dis']
        tt = s['ta']
        s['avg'] = (sum(tt) / len(tt) / 1000.0) if tt else 0.0
        s['best'] = (min(tt) / 1000.0) if tt else 0.0
    rows.sort(key=lambda s: (-s['pt'], s['best'] or 9e9))

    def e(x): return html.escape(str(x))
    def fmt(x): return ('%.1f' % x).rstrip('0').rstrip('.')
    tot_asm = sum(s['asm'] for s in rows)
    tot_dis = sum(s['dis'] for s in rows)
    body = ''.join(
        '<tr><td>%d</td><td class=nm>%s</td><td>%d</td><td>%d</td><td>%s</td><td>%s</td><td class=v>%s</td></tr>' % (
            i + 1, e(s['nome']), s['asm'], s['dis'],
            ('%.0fs' % s['avg']) if s['avg'] else '–',
            ('%.1fs' % s['best']) if s['best'] else '–',
            fmt(s['pt']))
        for i, s in enumerate(rows))
    HTML = """<!doctype html><html lang=it><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Cruscotto assemblatore</title><style>
:root{{--bg:#f3f1ec;--card:#fff;--tx:#17202a;--mu:#5a6572;--ln:#dde3ea;--ok:#2f9e57;--acc:#1f6feb}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--ok:#3fb950;--acc:#58a6ff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.45 system-ui,Segoe UI,Arial,sans-serif;padding:20px}}
.w{{max-width:720px;margin:0 auto}}h1{{font-size:21px;margin:0 0 2px}}.sub{{color:var(--mu);margin:0 0 14px}}
.kpi{{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0 16px}}.k{{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:10px 14px;min-width:110px}}
.k b{{font-size:22px;display:block}}.k span{{color:var(--mu);font-size:13px}}
table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--ln);border-radius:12px;overflow:hidden}}
th,td{{padding:8px 10px;text-align:left;border-bottom:1px solid var(--ln);font-variant-numeric:tabular-nums}}
th{{background:rgba(127,127,127,.08);font-size:13px;color:var(--mu)}}.nm{{font-weight:700}}.v{{font-weight:800;color:var(--acc)}}
</style></head><body><div class=w>
<h1>Cruscotto — Lab assemblaggio PC (1INF)</h1>
<p class=sub>Gioco «Monta il PC» · punteggio = assemblati ×1 + smontati ×0,7</p>
<div class=kpi>
<div class=k><b>{n}</b><span>allievi attivi</span></div>
<div class=k><b>{ta}</b><span>assemblati tot.</span></div>
<div class=k><b>{td}</b><span>smontati tot.</span></div>
</div>
<table><tr><th>#</th><th>Allievo</th><th>🔧 Assemblati</th><th>↩ Smontati</th><th>Medio (asm)</th><th>Record (asm)</th><th>Punteggio</th></tr>
{body}</table>
<p class=sub style="margin-top:10px">Dati locali del browser di ciascun PC + inviati al centro. Se un allievo non compare, non ha ancora completato nessun PC o l'invio non è arrivato.</p>
</div></body></html>""".format(n=len(rows), ta=tot_asm, td=tot_dis, body=body or '<tr><td colspan=7>Nessun dato ancora.</td></tr>')
    open(out, 'w').write(HTML)
    print('OK allievi %d · assemblati %d · smontati %d -> %s' % (len(rows), tot_asm, tot_dis, out))

if __name__ == '__main__':
    main()
