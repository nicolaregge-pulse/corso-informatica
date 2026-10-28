# -*- coding: utf-8 -*-
"""Pagina «Cosa è cambiato oggi nel gioco» della 2INF: prende dal CHANGELOG del treno tutte le versioni di una data
e le mette in una pagina, dalla più nuova, con il link per giocare ogni versione. Solo italiano (controllo solo_italiano).
Uso: python3 strumenti/gen_novita.py <cartella del gioco> <cartella della pagina> <data GG/MM/AAAA> <classe>
Esempio: python3 strumenti/gen_novita.py treno-blindato 2inf-novita 12/10/2026 2INF"""
import sys as _sp, os as _op; _sp.path.append(_op.path.dirname(_op.path.abspath(__file__))); import privacy_pubblico  # noqa: E401,F401 privacy 28/10/2026: nel pubblico i ragazzi solo come «Nome C.»
import html, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, "strumenti"))
import solo_italiano
GIOCO, CART, DATA, CLASSE = (sys.argv[1:5] + ["treno-blindato", "2inf-novita", "12/10/2026", "2INF"][len(sys.argv[1:5]):])
CL = open(os.path.join(R, "docs/giochi/" + GIOCO + "/CHANGELOG.md"), encoding="utf-8").read()
e = html.escape
blocchi = re.split(r"\n(?=## v)", CL)
voci = []
for b in blocchi:
    m = re.match(r"## (v[\d.]+) — (\d\d/\d\d/\d{4}) (\d\d:\d\d) — (.+)", b.strip())
    if not m or m.group(2) != DATA:
        continue
    ver, ora, nome = m.group(1), m.group(3), m.group(4)
    righe = [re.sub(r"^\d+\.\s*", "", x.strip()) for x in b.strip().split("\n")[1:] if re.match(r"\s*\d+\.", x)]
    voci.append((ver, ora, nome, righe))
def li(t):
    t = e(t)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
card = "".join(
    f"<div class='card'><h2><span class='v'>{e(v)}</span> {e(n)}</h2><p class='mu'>{e(DATA)} alle {e(o)}</p><ol>" + "".join(f"<li>{li(x)}</li>" for x in rr) +
    f"</ol><p><a class='bt' target='_blank' href='../giochi/{GIOCO}/versioni/{e(v)}/'>Gioca la {e(v)}</a></p></div>" for v, o, n, rr in voci)
pag = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Novità del gioco {e(CLASSE)}</title><style>
:root{{--bg:#fbfaf7;--card:#fff;--tx:#111;--mu:#555;--ln:#ddd;--acc:#1f6feb}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}}}
:root[data-theme="dark"]{{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}
body{{margin:0;background:var(--bg);color:var(--tx);font:17px/1.5 system-ui,Segoe UI,Arial,sans-serif}}.w{{max-width:900px;margin:0 auto;padding:16px}}
h1{{font-size:clamp(24px,6vw,32px);margin:8px 0 2px}}h2{{font-size:20px;margin:0 0 2px}}.mu{{color:var(--mu);margin:0 0 6px}}
.card{{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:12px 16px;margin:12px 0}}
.v{{display:inline-block;background:#2f9e57;color:#fff;border-radius:8px;padding:0 8px;margin-right:6px}}
.bt{{display:inline-block;background:#1f6feb;color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:8px 14px;margin:4px 6px 4px 0}}
</style></head><body><div class="w">
<h1>Cosa è cambiato oggi nel gioco</h1><p class="mu">{e(CLASSE)} · {e(DATA)} · {len(voci)} versioni nuove, dalla più nuova. Ogni versione è nata da una vostra Pull Request.</p>
<p><a class="bt" target="_blank" href="../giochi/{GIOCO}/">Gioca l'ultima versione</a><a class="bt" target="_blank" href="../giochi/{GIOCO}/versioni/">Tutte le versioni</a><a class="bt" target="_blank" href="../{CLASSE.lower()}-backlog/">Il backlog</a><a class="bt" target="_blank" href="../giochi/grafo/">Il grafo delle versioni</a></p>
{card}</div></body></html>"""
pag = solo_italiano.pulisci(pag); solo_italiano.controlla(pag, CART)
open(os.path.join(R, "docs/" + CART + "/index.html"), "w", encoding="utf-8").write(pag)
print(len(voci), "versioni")
