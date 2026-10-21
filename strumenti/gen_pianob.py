# -*- coding: utf-8 -*-
"""PIANO B della pubblicazione (21/10/2026, Nicola: «tutti i giorni la stessa storia: un sistema alternativo e un piano B»).
Se lo script di Google è fermo, il docente pubblica da questa pagina con il bottone ufficiale «Condividi su Classroom»:
classe, tipo (compito o annuncio), titolo e testo arrivano già compilati; lui preme solo «Vai» e «Assegna» / «Pubblica».
Piano C, sulla stessa pagina: il testo con il bottone «Copia» per incollarlo a mano.
Legge i compiti del giorno da coda/ del riservato (solo titoli, testi e link: niente nomi di allievi).
Uso: python3 strumenti/gen_pianob.py AAAA-MM-GG"""
import glob, html, json, os, sys, urllib.parse

giorno = sys.argv[1]
RIS = "/home/user/corso-informatica-riservato"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "prof-pubblica")
e = html.escape


def share(cid, tipo, titolo, testo, url):
    q = {"url": url or "https://nicolaregge-pulse.github.io/corso-informatica/", "title": titolo, "body": testo, "itemtype": tipo, "courseid": cid}
    return "https://classroom.google.com/share?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)


schede = []
for f in sorted(glob.glob(RIS + "/coda/" + giorno + "_*.json")):
    j = json.load(open(f, encoding="utf-8"))
    if j.get("stato") in ("bozza",) or not j.get("course_id"):
        continue
    t = j.get("descrizione", "")
    primo = next((r for r in t.split() if r.startswith("https://nicolaregge-pulse.github.io")), "")
    ann = "ANNUNCIO DI OGGI\n\n" + t
    stato = j.get("stato", "")
    schede.append(f"""<div class="card"><h2>{e(j['classe'])} · {e(j['titolo'])}</h2>
<p class="mu">Stato nello script: <b>{e(stato)}</b>{' — è già su Classroom, NON ripubblicare' if stato.startswith('pubblicato') else ''}</p>
<div class="row"><a class="b" target="_blank" rel="noopener" href="{e(share(j['course_id'], 'assignment', j['titolo'], t, primo))}">1. Pubblica il COMPITO</a>
<a class="b g" target="_blank" rel="noopener" href="{e(share(j['course_id'], 'announcement', j['titolo'], ann, primo))}">2. Pubblica l'ANNUNCIO</a></div>
<details><summary>Piano C: il testo da copiare a mano</summary><button class="c" onclick="navigator.clipboard.writeText(this.nextElementSibling.textContent);this.textContent='Copiato'">Copia</button><pre>{e(t)}</pre></details></div>""")

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(f"""<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Pubblica senza script</title>
<style>:root{{--bg:#f4f1ea;--card:#fff;--fg:#1b2430;--mu:#5c6672;--acc:#1f6feb}}body{{margin:0;background:var(--bg);color:var(--fg);font-family:"Segoe UI",system-ui,Arial,sans-serif}}
.w{{max-width:860px;margin:0 auto;padding:16px}}.card{{background:var(--card);border-radius:14px;padding:14px;margin:12px 0;box-shadow:0 1px 3px #0002}}
h2{{font-size:18px;margin:0 0 6px}}.mu{{color:var(--mu)}}.row{{display:flex;gap:8px;flex-wrap:wrap}}
.b{{display:inline-block;padding:12px 16px;border-radius:10px;background:var(--acc);color:#fff;font-weight:700;text-decoration:none}}.b.g{{background:#1a7f37}}
pre{{white-space:pre-wrap;background:#f6f8fa;padding:10px;border-radius:8px;font-size:14px}}.c{{margin-top:8px;padding:6px 12px}}</style></head>
<body><div class="w"><h1>Pubblica senza script — {e(giorno)}</h1>
<p>Usala solo se lo script di Google è fermo. Apri questa pagina nella finestra <b>PIAMARTA</b>. Ogni bottone apre la finestra ufficiale di Classroom
con la classe, il titolo e il testo già scritti: premi <b>Vai</b>, controlla, poi <b>Assegna</b> (compito) o <b>Pubblica</b> (annuncio).</p>
{''.join(schede) or '<p>Nessun compito in coda per questo giorno.</p>'}
</div></body></html>""")
print(len(schede), "compiti ->", OUT)
