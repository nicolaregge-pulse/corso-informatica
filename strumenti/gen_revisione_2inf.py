# -*- coding: utf-8 -*-
"""Revisione delle versioni del treno della 2INF (12/10/2026): una riga positiva e una da migliorare per versione.
Scrive docs/2inf-revisione/index.html (solo italiano) e classe-2/revisione-versioni/revisione-versioni.md.
Uso: python3 strumenti/gen_revisione_2inf.py"""
import html, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = {x["versione"]: x for x in json.load(open(os.path.join(ROOT, "docs/giochi/treno-blindato/versioni/versioni.json"), encoding="utf-8"))}
R = [
 ("v0.12", "Con una sola idea il gioco cambia atmosfera: il tramonto lo rende più bello da guardare.", "Al tramonto i cattivi scuri si staccano meno dallo sfondo: vanno provati con colori più chiari."),
 ("v0.13", "Ogni livello è un posto nuovo: chi gioca sente che sta andando avanti.", "Il cambio di scenario arriva di colpo: una scritta o un attimo di pausa lo annuncerebbe meglio."),
 ("v0.14", "L'ultimo colpo dà ancora una possibilità e crea tensione.", "Con il vetro tutto crepato l'ultimo colpo si gioca quasi alla cieca: per questo nella base del prof le crepe partono dai bordi."),
 ("v0.15", "Il gioco resta interessante anche per chi è bravo.", "Nessuno ha ancora misurato quanto diventa difficile dopo il livello 5: serve un collaudo."),
 ("v0.16", "Partite più lunghe e meno frustrazione per chi comincia.", "Con 10 colpi i primi livelli diventano facili: la difficoltà va bilanciata insieme al vetro."),
 ("v0.17", "Difetto vero, trovato giocando: è il lavoro di chi fa il collaudo.", "Ora i cattivi sono più lontani: sul telefono vanno controllati, potrebbero essere piccoli da toccare."),
 ("v0.18", "Il colpo si sente e si vede: soddisfazione immediata.", "Tre richieste sulla stessa cosa: prima di mandarla, conviene guardare il backlog e unirsi a quella che c'è già."),
 ("v0.19", "Il mirino rosso rende la mira più precisa e il gioco più «da gioco».", "Sul telefono il mirino non c'è, perché si tocca con il dito: l'idea vale solo per il PC."),
 ("v0.20", "Corregge un difetto che rovinava la partita.", "Il difetto era nato da una versione precedente: ogni modifica va provata giocando prima di pubblicarla."),
 ("v0.21", "Tolto un lampeggio fastidioso, che può anche dare fastidio agli occhi.", "Con le luci ferme il paese sembra meno vivo: si potrebbero accendere piano piano."),
 ("v0.22", "La sfida continua contro se stessi: il record è sempre lì accanto ai punti.", "Il record resta solo su quel computer: su un altro PC si riparte da zero."),
 ("v0.23", "Indispensabile in classe: si può fermare la partita (anche con il tasto P o Esc) e riprenderla.", "Il bottone è piccolo: sul telefono va provato che si tocchi bene."),
 ("v0.24", "Premia chi resiste di più: andare avanti conviene.", "I punti crescono in fretta: i record dei primi giorni diventano impossibili da battere?"),
 ("v0.25", "Premia la precisione, non solo la velocità.", "Non si capisce subito quando un colpo è «preciso»: serve una scritta che lo dica."),
 ("v0.26", "Quattro richieste sulla stessa idea diventano una versione sola: lavoro di squadra vero.", "Con pioggia e nebbia si vede poco: va bene per i livelli alti, ma all'inizio potrebbe scoraggiare."),
 ("v0.27", "I binari gialli si vedono meglio: modifica piccola, effetto grande.", "Il giallo non c'entra molto con il bosco bruciato: un colore più scuro potrebbe stare meglio."),
 ("v0.28", "Si vede quanto manca al prossimo livello: dà un obiettivo vicino.", "La barra è in alto al centro, vicino ad altre scritte: va controllato che non copra i cattivi."),
 ("v0.29", "A fine partita si vede cosa si è fatto bene: precisione e colpi sbagliati.", "Le statistiche spariscono con la partita dopo: si potrebbero tenere le migliori."),
 ("v0.30", "La sfera d'oro dà un momento di sorpresa e cambia il ritmo.", "Quando si colpisce la sfera, non si vede bene quanto resta dei 10 secondi: serve un contatore."),
 ("v0.31", "Gli uccelli rendono il cielo vivo: un dettaglio che fa sembrare il mondo vero.", "Gli uccelli possono distrarre: non devono sembrare cattivi da colpire."),
]
e = html.escape
righe, md = [], ["# Revisione delle versioni del treno — 2INF", "", "**Versione 1.0** — 13/10/2026 — Prof. Nicola Regge. Per l'analisi in classe.", "",
                 "| Versione | Cosa è entrato | Cosa funziona | Cosa si può migliorare |", "|---|---|---|---|"]
for ver, pos, neg in R:
    x = V[ver]
    righe.append('<tr><td><a href="../giochi/treno-blindato/versioni/%s/" target="_blank"><b>%s</b></a></td><td><b>%s</b><br><span class="mu">%s</span></td><td class="pos">%s</td><td class="neg">%s</td></tr>' % (
        ver, ver, e(x["nome"]), e(x["cambi"]), e(pos), e(neg)))
    md.append("| %s | %s | %s | %s |" % (ver, x["nome"], pos, neg))
md += ["", "## Domande per l'analisi in classe", "", "1. Quale versione ha migliorato di più il gioco? Perché?", "2. Quale miglioramento proposto qui sopra faresti per primo? Scrivilo come Pull Request: Titolo, Cosa cambia, Dove, Perché.", "3. Trovi un difetto che qui non c'è? Provalo giocando e scrivilo come Pull Request.", ""]
pagina = """<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Revisione delle versioni</title>
<style>:root{--bg:#fbfaf7;--fg:#111;--mu:#5b5b5b;--card:#fff;--bd:#dedbd3}@media (prefers-color-scheme:dark){:root{--bg:#15171a;--fg:#eee;--mu:#aaa;--card:#1f2227;--bd:#353a42}}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,Segoe UI,Arial,sans-serif}.w{max-width:1150px;margin:0 auto;padding:16px}h1{font-size:26px;margin:6px 0}
.mu{color:var(--mu);font-size:14px}table{border-collapse:collapse;width:100%;background:var(--card)}th,td{border:1px solid var(--bd);padding:8px;vertical-align:top;text-align:left}
th{background:#1f6feb;color:#fff}td.pos{border-left:4px solid #1a7f37}td.neg{border-left:4px solid #d4a000}.box{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:14px;margin:14px 0}
@media (max-width:700px){table,thead,tbody,tr,td,th{display:block}thead{display:none}td{border:0;border-bottom:1px solid var(--bd)}tr{border:1px solid var(--bd);margin:10px 0}}</style></head>
<body><div class="w"><h1>Revisione delle versioni del treno</h1><p class="mu">2INF · le 20 versioni di lunedì 12/10, dalla v0.12 alla v0.31. Per ogni versione: cosa funziona e cosa si può migliorare. Clicca la versione per giocarla.</p>
<table><thead><tr><th>Versione</th><th>Cosa è entrato</th><th>Cosa funziona</th><th>Cosa si può migliorare</th></tr></thead><tbody>RIGHE</tbody></table>
<div class="box"><b>Analisi in classe</b><ol><li>Quale versione ha migliorato di più il gioco? Perché?</li><li>Quale miglioramento proposto qui sopra faresti per primo? Scrivilo come Pull Request: Titolo, Cosa cambia, Dove, Perché.</li><li>Trovi un difetto che qui non c'è? Provalo giocando e scrivilo come Pull Request.</li></ol></div></div></body></html>""".replace("RIGHE", "".join(righe))
open(os.path.join(ROOT, "docs/2inf-revisione/index.html"), "w", encoding="utf-8").write(pagina)
os.makedirs(os.path.join(ROOT, "classe-2/revisione-versioni"), exist_ok=True)
open(os.path.join(ROOT, "classe-2/revisione-versioni/revisione-versioni.md"), "w", encoding="utf-8").write("\n".join(md))
print("ok")
