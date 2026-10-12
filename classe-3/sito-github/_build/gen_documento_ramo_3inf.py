"""3INF 12/10/2026 — Teoria: il tuo Documento nell'albero delle versioni (IT + BN).
Genera docs/compito/3inf-20261012-documento/pagina.html (index.html è il caricatore fisso).
Segue REGOLE-COSTRUZIONE-TEORIA.md: titolo + traduzione, percorso in alto, FASE 1 teoria solo da leggere, FASE 2 bottone verde.
"""
import json, os, html
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(R, "docs", "compito", "3inf-20261012-documento", "pagina.html")
e = html.escape

TITOLO = ("Il tuo Documento nell'albero delle versioni", "সংস্করণের গাছে তোমার ডকুমেন্ট")
BREVE = [
    ("Il gioco della 3INF è un fork: una copia del gioco della 2INF che cresce per conto suo.",
     "৩INF-এর খেলা একটি fork: ২INF-এর খেলার একটি কপি, যা নিজে নিজে বড় হয়।"),
    ("Il tuo Documento su Classroom è il TUO ramo: parte dalla versione del gioco che stai giocando.",
     "Classroom-এ তোমার ডকুমেন্ট হলো তোমার নিজের শাখা: তুমি খেলার যে সংস্করণ খেলছ, সেখান থেকে শুরু হয়।"),
    ("Ogni Pull Request che scrivi nel Documento è un pallino sul tuo ramo: una proposta di modifica.",
     "ডকুমেন্টে লেখা প্রতিটি Pull Request তোমার শাখার একটি বিন্দু: একটি পরিবর্তনের প্রস্তাব।"),
    ("Il prof la legge. SÌ: merge, la proposta entra nel gioco e nasce una versione nuova (v1.1, v1.2…). NO: resta sul tuo ramo e la puoi correggere.",
     "শিক্ষক এটি পড়েন। হ্যাঁ: merge, প্রস্তাবটি খেলায় ঢোকে এবং নতুন সংস্করণ হয় (v1.1, v1.2…)। না: এটি তোমার শাখায় থাকে, তুমি ঠিক করতে পারো।"),
    ("Senza Pull Request il tuo ramo è vuoto: nel gioco non entra niente di tuo.",
     "Pull Request ছাড়া তোমার শাখা খালি: খেলায় তোমার কিছুই ঢোকে না।"),
]
PR_PARTI = [
    ("Titolo", "শিরোনাম", "Black Panter"),
    ("Cosa cambia nel gioco", "খেলায় কী বদলায়", "un cattivo nuovo, con la mimetica nera e argento"),
    ("Dove", "কোথায়", "esce da una porta"),
    ("Perché", "কেন", "così la città fa più paura; quando spara dice «Yahuu!»"),
]
ERRORI = [
    ("Documento vuoto.", "Il tuo ramo resta vuoto: nel gioco non entra niente.",
     "খালি ডকুমেন্ট।", "তোমার শাখা খালি থাকে: খেলায় কিছুই ঢোকে না।"),
    ("Modello copiato senza cambiare le parole in MAIUSCOLO.", "La Pull Request non propone niente: il prof non può fare il merge.",
     "বড় হাতের শব্দ না বদলে নমুনা কপি করা।", "Pull Request কিছুই প্রস্তাব করে না: শিক্ষক merge করতে পারেন না।"),
    ("Lavoro scritto fuori dal Documento (un altro file, una chat).", "Il prof non lo vede: non diventa un pallino del tuo ramo.",
     "ডকুমেন্টের বাইরে লেখা কাজ (অন্য ফাইল, চ্যাট)।", "শিক্ষক এটি দেখেন না: এটি তোমার শাখার বিন্দু হয় না।"),
    ("Tutto in un unico testo, senza PR-1, PR-2, PR-3.", "Non si capisce quali sono le proposte: ognuna deve avere il suo numero.",
     "PR-1, PR-2, PR-3 ছাড়া সব এক লেখায়।", "কোনগুলো প্রস্তাব বোঝা যায় না: প্রতিটির নিজের নম্বর থাকতে হবে।"),
]

def svg():
    # 2INF (blu) -> fork 3INF (verde) -> il ramo del Documento (rosa) con PR sì/no
    s = ["<svg viewBox='0 0 760 300' style='width:100%;max-width:760px;height:auto' role='img' aria-label='Albero: il gioco della 2INF, il fork della 3INF e il ramo del tuo Documento con le Pull Request'>"]
    s.append("<text x='10' y='22' font-size='15' font-weight='700' fill='#2f81f7'>2INF — il gioco originale</text>")
    s.append("<line x1='30' y1='50' x2='170' y2='50' stroke='#2f81f7' stroke-width='5'/>")
    for x, t in [(30, 'v0.10'), (170, 'v0.11')]:
        s.append(f"<circle cx='{x}' cy='50' r='11' fill='#2f81f7'/><text x='{x}' y='78' font-size='12' text-anchor='middle' fill='currentColor'>{t}</text>")
    s.append("<path d='M170 50 C 210 50, 210 140, 250 140' stroke='#3fb950' stroke-width='5' fill='none' stroke-dasharray='8 6'/>")
    s.append("<text x='185' y='105' font-size='13' fill='#3fb950' font-weight='700'>fork</text>")
    s.append("<text x='250' y='118' font-size='15' font-weight='700' fill='#3fb950'>3INF — il vostro gioco</text>")
    s.append("<line x1='250' y1='140' x2='730' y2='140' stroke='#3fb950' stroke-width='5'/>")
    for x, t in [(250, 'v1.0'), (430, 'v1.1'), (580, 'v1.2'), (730, 'v1.3')]:
        s.append(f"<circle cx='{x}' cy='140' r='12' fill='#3fb950'/><text x='{x}' y='166' font-size='12' text-anchor='middle' fill='currentColor'>{t}</text>")
    s.append("<path d='M250 140 C 280 140, 280 240, 310 240' stroke='#db61a2' stroke-width='5' fill='none'/>")
    s.append("<line x1='310' y1='240' x2='620' y2='240' stroke='#db61a2' stroke-width='5'/>")
    s.append("<text x='300' y='290' font-size='15' font-weight='700' fill='#db61a2'>il TUO ramo = il tuo Documento</text>")
    for x, t in [(340, 'PR-1'), (500, 'PR-2'), (620, 'PR-3')]:
        s.append(f"<circle cx='{x}' cy='240' r='12' fill='#db61a2'/><text x='{x}' y='222' font-size='12' text-anchor='middle' fill='currentColor'>{t}</text>")
    s.append("<path d='M340 240 C 380 240, 400 160, 422 148' stroke='#db61a2' stroke-width='4' fill='none'/><polygon points='422,148 409,150 416,160' fill='#db61a2'/>")
    s.append("<text x='370' y='195' font-size='13' font-weight='800' fill='#2f9e57'>SÌ = merge</text>")
    s.append("<path d='M500 240 C 540 240, 555 165, 572 150' stroke='#db61a2' stroke-width='4' fill='none'/><polygon points='572,150 559,152 566,162' fill='#db61a2'/>")
    s.append("<text x='510' y='195' font-size='13' font-weight='800' fill='#2f9e57'>SÌ</text>")
    s.append("<text x='640' y='246' font-size='22' font-weight='900' fill='#e0413a'>✗ NO</text>")
    s.append("</svg>")
    return "".join(s)

def main():
    vv = json.load(open(os.path.join(R, "docs", "giochi", "treno-3inf", "versioni", "versioni.json"), encoding="utf-8"))
    storia = "".join(f"<tr><td><b>{e(v['versione'])}</b></td><td>{e(v['nome'])}</td><td>{e(v.get('cambi',''))}</td></tr>" for v in vv)
    breve = "".join(f"<li><b>{e(a)}</b><p class='bn'>{e(b)}</p></li>" for a, b in BREVE)
    parti = "".join(f"<tr><td><b>{e(a)}</b><br><span class='bn'>{e(b)}</span></td><td>{e(c)}</td></tr>" for a, b, c in PR_PARTI)
    errori = "".join(f"<li><b>{e(a)}</b> {e(b)}<p class='bn'>{e(c)} {e(d)}</p></li>" for a, b, c, d in ERRORI)
    h = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Il tuo Documento 3INF</title><style>
:root{{--bg:#fbfaf7;--card:#fff;--tx:#111;--mu:#555;--ln:#ddd;--acc:#1f6feb;--ok:#2f9e57}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}}}
:root[data-theme="dark"]{{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}
body{{margin:0;background:var(--bg);color:var(--tx);font:18px/1.5 system-ui,Segoe UI,Arial,sans-serif}}.w{{max-width:900px;margin:0 auto;padding:16px}}
h1{{font-size:clamp(24px,6vw,32px);margin:8px 0 2px}}h2{{font-size:22px;margin:26px 0 8px;border-bottom:2px solid var(--ln);padding-bottom:4px}}h3{{margin:14px 0 6px}}
.mu{{color:var(--mu)}}.bn{{font-family:"Noto Sans Bengali","Vrinda",sans-serif;color:var(--mu);margin:2px 0}}.t-bn{{font-family:"Noto Sans Bengali","Vrinda",sans-serif;font-size:24px;color:var(--mu);margin:0}}
.card{{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:12px 16px;margin:10px 0;overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:16px}}td,th{{border:1px solid var(--ln);padding:7px 9px;text-align:left;vertical-align:top}}th{{background:var(--acc);color:#fff}}
.bt{{display:inline-block;background:#238636;color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:12px 18px;margin:6px 0;font-size:20px}}
</style></head><body><div class="w">
<h1>{e(TITOLO[0])}</h1><p class="t-bn">{e(TITOLO[1])}</p><p class="mu">3INF · 12/10/2026</p>
<div class="card" style="border:3px solid var(--acc)"><p><b>Il tuo percorso di oggi</b></p><p class="bn">আজ তোমার পথ</p><ol>
<li><b>FASE 1 — Leggi la teoria qui sotto, dall'inizio alla fine.</b><p class="bn">ধাপ ১ — নিচের তত্ত্ব শুরু থেকে শেষ পর্যন্ত পড়ো।</p></li>
<li><b>FASE 2 — In fondo trovi il bottone verde: premilo e fai il compito.</b><p class="bn">ধাপ ২ — শেষে সবুজ বোতাম আছে: চাপো এবং কাজটি করো।</p></li></ol></div>
<h2>FASE 1 — La teoria</h2>
<div class="card"><h3>In breve</h3>{svg()}<ol>{breve}</ol></div>
<div class="card"><h3>La lavagna del prof</h3><img src="lavagna-versioni.jpg" alt="La lavagna: numeri delle versioni, changelog, fork, Pull Request accettata e rifiutata, merge" style="max-width:100%;border-radius:10px"><p>Sulla linea rossa le versioni (v0.8, v0.9, v1.0). In blu il fork che parte dalla v0.9. Sul ramo, le Pull Request: quella accettata (ACCEPT ✓) rientra con il MERGE, quella rifiutata (REFUSE ✗) resta fuori.</p><p class="bn">লাল রেখায় সংস্করণ। নীল রঙে fork। শাখায় Pull Request: গৃহীত (ACCEPT ✓) MERGE দিয়ে ফিরে আসে, প্রত্যাখ্যাত (REFUSE ✗) বাইরে থাকে।</p></div>
<div class="card"><h3>La storia vera del vostro gioco</h3><p>Ogni riga è una versione nata dalle vostre Pull Request (dal grafo delle versioni).</p><p class="bn">প্রতিটি সারি তোমাদের Pull Request থেকে জন্মানো একটি সংস্করণ।</p>
<table><tr><th>Versione</th><th>Nome</th><th>Cosa è entrato e da quale Pull Request</th></tr>{storia}</table>
<p><a class="bt" style="font-size:16px;padding:8px 14px" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/">Apri il grafo delle versioni</a></p><p class="mu">Si apre in una scheda nuova: quando hai finito, chiudila e torni qui. · নতুন ট্যাবে খোলে: শেষ হলে বন্ধ করে এখানে ফিরে এসো।</p></div>
<div class="card"><h3>Com'è fatta una Pull Request nel Documento</h3><p>Quattro parti, sempre. Esempio vero: la Pull Request #1, entrata nel gioco con la v1.1.</p><p class="bn">সবসময় চারটি অংশ। সত্যিকারের উদাহরণ: Pull Request #1, যা v1.1-এ খেলায় ঢুকেছে।</p>
<table><tr><th>Parte</th><th>Esempio</th></tr>{parti}</table></div>
<div class="card"><h3>Gli errori della settimana scorsa (e perché)</h3><ol>{errori}</ol></div>
<h2>FASE 2 — Il compito</h2><div class="card mu">Il compito si costruisce insieme al prof, dopo che la teoria è approvata.</div>
</div></body></html>"""
    open(OUT, "w", encoding="utf-8").write(h)
    print(OUT)

main()
