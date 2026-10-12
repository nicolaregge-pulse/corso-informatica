"""2INF 12/10/2026 — Teoria: il tuo Documento nell'albero delle versioni (IT + ZH; per la 2INF niente arabo, §2.49).
Genera docs/compito/3inf-20261012-documento/pagina.html (index.html è il caricatore fisso).
Segue REGOLE-COSTRUZIONE-TEORIA.md: titolo + traduzione, percorso in alto, FASE 1 teoria solo da leggere, FASE 2 bottone verde.
"""
import json, os, html
MODULO_PARERE = os.environ.get("MODULO_PARERE", "https://docs.google.com/forms/d/e/1FAIpQLSd2c6QvvtKgmY0E0iP8IsuceOlLQ_da8YmiDEILPUNQ3oGnkQ/viewform")
MODULO_CONSEGNA = "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform"
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(R, "docs", "compito", "2inf-20261012-documento", "pagina.html")
e = html.escape

TITOLO = ("Il tuo Documento nell'albero delle versioni", "你的文档在版本树里的位置")
BREVE = [
    ("Il gioco della 2INF è il gioco ORIGINALE: la 3INF e la 1INF ne hanno fatto una copia (fork).",
     "2INF 的游戏是原版游戏：3INF 和 1INF 复制了它（fork）。"),
    ("Il tuo Documento su Classroom è il TUO ramo: parte dalla versione del gioco che stai giocando (v0.11).",
     "你在 Classroom 上的文档就是你自己的分支：它从你正在玩的游戏版本（v0.11）开始。"),
    ("Ogni Pull Request che scrivi è un pallino sul tuo ramo: una proposta di modifica.",
     "你写的每一个 Pull Request 都是你分支上的一个圆点：一个修改的建议。"),
    ("Il prof la legge. SÌ: merge, la proposta entra nel gioco e nasce una versione nuova (v0.12, v0.13…). NO: resta sul tuo ramo e la puoi correggere.",
     "老师会读它。是：merge，建议进入游戏，产生一个新版本（v0.12、v0.13……）。不：它留在你的分支上，你可以修改。"),
    ("Senza Pull Request il tuo ramo è vuoto: nel gioco non entra niente di tuo.",
     "没有 Pull Request，你的分支是空的：游戏里没有你的东西。"),
]
PR_PARTI = [
    ("Titolo", "标题", "Più lento"),
    ("Cosa cambia nel gioco", "游戏里改变什么", "il treno va più piano: la velocità passa da 1 a 0,7"),
    ("Dove", "在哪里", "in tutto il gioco, dall'inizio"),
    ("Perché", "为什么", "il gioco andava troppo veloce e non si riusciva a colpire i cattivi"),
]
ERRORI = [
    ("Mandare solo un file, senza scrivere la richiesta.", "Il prof non sa cosa vuoi: scrivi sempre Titolo, Cosa cambia, Dove, Perché.",
     "只发一个文件，不写要求。", "老师不知道你想要什么：一定要写标题、改变什么、在哪里、为什么。"),
    ("La foto di una persona vera.", "Nel gioco pubblico non mettiamo volti di ragazzi (privacy): usa un personaggio disegnato o di un videogioco.",
     "真人的照片。", "公开的游戏里不放同学的脸（隐私）：用画的人物或游戏里的人物。"),
    ("Scrivere fuori dal Modulo o dal Documento (una chat, un altro file).", "Il prof non lo vede: non diventa un pallino del tuo ramo.",
     "在表格或文档以外的地方写（聊天、别的文件）。", "老师看不到：它不会变成你分支上的圆点。"),
    ("Tutto in un unico testo, senza PR1, PR2.", "Ogni proposta deve avere il suo numero: PR1, PR2, PR3…",
     "所有内容写在一起，没有 PR1、PR2。", "每个建议都要有自己的编号：PR1、PR2、PR3……"),
]

def svg():
    s = ["<svg viewBox='0 0 760 270' style='width:100%;max-width:760px;height:auto' role='img' aria-label='Albero: il gioco della 2INF e il ramo del tuo Documento con le Pull Request'>"]
    s.append("<text x='10' y='22' font-size='15' font-weight='700' fill='#2f81f7'>2INF — il gioco originale (ramo principale)</text>")
    s.append("<line x1='40' y1='60' x2='730' y2='60' stroke='#2f81f7' stroke-width='5'/>")
    for x, t in [(40, 'v0.9'), (200, 'v0.10'), (360, 'v0.11'), (560, 'v0.12'), (730, 'v0.13')]:
        s.append(f"<circle cx='{x}' cy='60' r='12' fill='#2f81f7'/><text x='{x}' y='88' font-size='12' text-anchor='middle' fill='currentColor'>{t}</text>")
    s.append("<path d='M360 60 C 390 60, 390 180, 420 180' stroke='#db61a2' stroke-width='5' fill='none'/>")
    s.append("<line x1='420' y1='180' x2='700' y2='180' stroke='#db61a2' stroke-width='5'/>")
    s.append("<text x='400' y='240' font-size='15' font-weight='700' fill='#db61a2'>il TUO ramo = il tuo Documento</text>")
    for x, t in [(450, 'PR1'), (600, 'PR2'), (700, 'PR3')]:
        s.append(f"<circle cx='{x}' cy='180' r='12' fill='#db61a2'/><text x='{x}' y='162' font-size='12' text-anchor='middle' fill='currentColor'>{t}</text>")
    s.append("<path d='M450 180 C 500 180, 520 90, 552 68' stroke='#db61a2' stroke-width='4' fill='none'/><polygon points='552,68 539,70 546,80' fill='#db61a2'/>")
    s.append("<text x='470' y='130' font-size='13' font-weight='800' fill='#2f9e57'>SÌ = merge</text>")
    s.append("<path d='M600 180 C 650 180, 690 100, 722 70' stroke='#db61a2' stroke-width='4' fill='none'/><polygon points='722,70 709,72 716,82' fill='#db61a2'/>")
    s.append("<text x='640' y='130' font-size='13' font-weight='800' fill='#2f9e57'>SÌ</text>")
    s.append("<text x='690' y='215' font-size='20' font-weight='900' fill='#e0413a'>✗ NO</text>")
    s.append("</svg>")
    return "".join(s)

def main():
    vv = json.load(open(os.path.join(R, "docs", "giochi", "treno-blindato", "versioni", "versioni.json"), encoding="utf-8"))
    storia = "".join(f"<tr><td><b>{e(v['versione'])}</b></td><td>{e(v['nome'])}</td><td>{e(v.get('cambi',''))}</td></tr>" for v in vv)
    breve = "".join(f"<li><b>{e(a)}</b><p class='zh'>{e(b)}</p></li>" for a, b in BREVE)
    parti = "".join(f"<tr><td><b>{e(a)}</b><br><span class='zh'>{e(b)}</span></td><td>{e(c)}</td></tr>" for a, b, c in PR_PARTI)
    errori = "".join(f"<li><b>{e(a)}</b> {e(b)}<p class='zh'>{e(c)} {e(d)}</p></li>" for a, b, c, d in ERRORI)
    h = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Il tuo Documento 2INF</title><style>
:root{{--bg:#fbfaf7;--card:#fff;--tx:#111;--mu:#555;--ln:#ddd;--acc:#1f6feb;--ok:#2f9e57}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}}}
:root[data-theme="dark"]{{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}
body{{margin:0;background:var(--bg);color:var(--tx);font:18px/1.5 system-ui,Segoe UI,Arial,sans-serif}}.w{{max-width:900px;margin:0 auto;padding:16px}}
h1{{font-size:clamp(24px,6vw,32px);margin:8px 0 2px}}h2{{font-size:22px;margin:26px 0 8px;border-bottom:2px solid var(--ln);padding-bottom:4px}}h3{{margin:14px 0 6px}}
.mu{{color:var(--mu)}}.zh{{font-family:"WenQuanYi Zen Hei","Noto Sans CJK SC",sans-serif;color:var(--mu);margin:2px 0}}.t-zh{{font-family:"WenQuanYi Zen Hei","Noto Sans CJK SC",sans-serif;font-size:24px;color:var(--mu);margin:0}}
.card{{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:12px 16px;margin:10px 0;overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:16px}}td,th{{border:1px solid var(--ln);padding:7px 9px;text-align:left;vertical-align:top}}th{{background:var(--acc);color:#fff}}
.bt{{display:inline-block;background:#238636;color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:12px 18px;margin:6px 0;font-size:20px}}
</style></head><body><div class="w">
<h1>{e(TITOLO[0])}</h1><p class="t-zh">{e(TITOLO[1])}</p><p class="mu">2INF · 12/10/2026</p>
<div class="card" style="border:3px solid var(--acc)"><p><b>Il tuo percorso di oggi</b></p><p class="zh">আজ তোমার পথ</p><ol>
<li><b>FASE 1 — Leggiamo insieme la teoria qui sotto, dall'inizio alla fine.</b><p class="zh">ধাপ ১ — আমরা একসাথে নিচের তত্ত্ব শুরু থেকে শেষ পর্যন্ত পড়ি।</p></li>
<li><b>FASE 2 — In fondo trovi due bottoni verdi: 1) Feedback (il tuo parere sulla teoria) e 2) PR1 (la tua prima Pull Request). Entro le 10:15.</b><p class="zh">ধাপ ২ — শেষে দুটি সবুজ বোতাম: 1) Feedback (তত্ত্ব নিয়ে তোমার মত) এবং 2) PR1 (তোমার প্রথম Pull Request)। ১০:১৫-এর মধ্যে।</p></li></ol></div>
<h2>FASE 1 — La teoria</h2>
<div class="card"><p><b>Dispensa a parte:</b> come lavorano le aziende di software, il Manifesto Agile e le 10 regole che usiamo nel nostro treno.</p><p class="zh">আলাদা পাঠ: সফটওয়্যার কোম্পানি কীভাবে কাজ করে, Agile ঘোষণাপত্র এবং আমাদের ট্রেনে ব্যবহৃত ১০টি নিয়ম।</p>
<p><a class="bt" style="background:#1f6feb" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/teoria/agile/">Teoria Agile</a></p><p class="mu">Si apre in una scheda nuova: quando hai finito, chiudila e torni qui. · নতুন ট্যাবে খোলে।</p></div>
<div class="card"><h3>In breve</h3>{svg()}<ol>{breve}</ol></div>
<div class="card"><h3>La lavagna del prof</h3><img src="lavagna-versioni.jpg" alt="La lavagna: numeri delle versioni, changelog, fork, Pull Request accettata e rifiutata, merge" style="max-width:100%;border-radius:10px"><p>Sulla linea rossa le versioni (v0.8, v0.9, v1.0). In blu il fork che parte dalla v0.9. Sul ramo, le Pull Request: quella accettata (ACCEPT ✓) rientra con il MERGE, quella rifiutata (REFUSE ✗) resta fuori.</p><p class="zh">লাল রেখায় সংস্করণ। নীল রঙে fork। শাখায় Pull Request: গৃহীত (ACCEPT ✓) MERGE দিয়ে ফিরে আসে, প্রত্যাখ্যাত (REFUSE ✗) বাইরে থাকে।</p></div>
<div class="card"><h3>La storia vera del vostro gioco</h3><p>Ogni riga è una versione nata dalle vostre Pull Request (dal grafo delle versioni).</p><p class="zh">প্রতিটি সারি তোমাদের Pull Request থেকে জন্মানো একটি সংস্করণ।</p>
<table><tr><th>Versione</th><th>Nome</th><th>Cosa è entrato e da quale Pull Request</th></tr>{storia}</table>
<p><a class="bt" style="font-size:16px;padding:8px 14px" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/">Apri il grafo delle versioni</a></p><p class="mu">Si apre in una scheda nuova: quando hai finito, chiudila e torni qui. · নতুন ট্যাবে খোলে: শেষ হলে বন্ধ করে এখানে ফিরে এসো।</p></div>
<div class="card"><h3>Come si chiede una modifica: il giro della Pull Request</h3>
<p>Nel vostro gioco funziona come in un'azienda vera. Tu proponi, il programma automatico legge, il prof decide, la versione nuova esce.</p>
<p class="zh">তোমাদের খেলায় সত্যিকারের কোম্পানির মতো কাজ হয়। তুমি প্রস্তাব দাও, স্বয়ংক্রিয় প্রোগ্রাম পড়ে, শিক্ষক সিদ্ধান্ত নেন, নতুন সংস্করণ বের হয়।</p>
<ol>
<li><b>Tu scrivi la richiesta</b> nel Modulo «Consegna» (o nel Documento): titolo, cosa cambia, dove, perché. Puoi aggiungere un'immagine.<p class="zh"><b>তুমি অনুরোধ লেখো</b> «Consegna» ফর্মে (বা ডকুমেন্টে): শিরোনাম, কী বদলায়, কোথায়, কেন। ছবিও যোগ করতে পারো।</p></li>
<li><b>Lo script gira da solo</b> ogni 5 minuti: è un programma del prof su Google che legge le richieste nuove e le copia nel repository Git del corso, con il tuo nome e l'ora.<p class="zh"><b>স্ক্রিপ্ট নিজে নিজে চলে</b> প্রতি ৫ মিনিটে: এটি Google-এ শিক্ষকের একটি প্রোগ্রাম, যা নতুন অনুরোধ পড়ে এবং তোমার নাম ও সময়সহ কোর্সের Git repository-তে কপি করে।</p></li>
<li><b>Il prof (con l'intelligenza artificiale) legge</b> la tua Pull Request e decide: SÌ o NO.<p class="zh"><b>শিক্ষক (কৃত্রিম বুদ্ধিমত্তার সাথে) পড়েন</b> এবং সিদ্ধান্ত নেন: হ্যাঁ বা না।</p></li>
<li><b>SÌ = merge:</b> la modifica entra nel gioco, nasce una versione nuova (v1.5, v1.6…) e nel changelog c'è scritto il numero della tua Pull Request.<p class="zh"><b>হ্যাঁ = merge:</b> পরিবর্তনটি খেলায় ঢোকে, নতুন সংস্করণ হয় এবং changelog-এ তোমার Pull Request-এর নম্বর লেখা থাকে।</p></li>
<li><b>Tu controlli</b> nel grafo delle versioni: il pallino nuovo è anche merito tuo. Se è NO, leggi il perché, correggi e rimanda.<p class="zh"><b>তুমি দেখো</b> সংস্করণের গ্রাফে: নতুন বিন্দুটি তোমারও কৃতিত্ব। না হলে, কেন পড়ো, ঠিক করো এবং আবার পাঠাও।</p></li>
</ol></div>
<div class="card"><h3>Com'è fatta una Pull Request</h3><p>Quattro parti, sempre, nel Modulo o nel Documento. Esempio vero: la Pull Request #1, entrata nel gioco con la v1.1.</p><p class="zh">সবসময় চারটি অংশ। সত্যিকারের উদাহরণ: Pull Request #1, যা v1.1-এ খেলায় ঢুকেছে।</p>
<table><tr><th>Parte</th><th>Esempio</th></tr>{parti}</table></div>
<div class="card"><h3>Gli errori della settimana scorsa (e perché)</h3><ol>{errori}</ol></div>
<h2>FASE 2 — 1) Feedback e 2) PR1 (entro le 10:15)</h2>
<div class="card" style="border:3px solid #238636"><p><b>Due lavori, in ordine. Ognuno si apre in una scheda nuova: quando hai finito, chiudila e torni qui.</b></p><p class="zh">দুটি কাজ, ক্রমানুসারে। প্রতিটি নতুন ট্যাবে খোলে: শেষ হলে বন্ধ করে এখানে ফিরে এসো। সময়: ১০:১৫-এর মধ্যে।</p>
<h3>1) Feedback — il mio parere sulla teoria</h3><ol>
<li><b>Premi il bottone verde «1) Feedback».</b><p class="zh">সবুজ বোতাম «1) Feedback» চাপো।</p></li>
<li><b>Rispondi alle 4 domande con parole tue, poi premi «Invia».</b><p class="zh">৪টি প্রশ্নের উত্তর নিজের ভাষায় দাও, তারপর «Invia» চাপো।</p></li></ol>
<p>@@BT1@@</p>
<h3>2) PR1 — la mia prima Pull Request (una richiesta per il gioco)</h3><ol>
<li><b>Premi il bottone verde «2) PR1»: si apre il Modulo «Consegna».</b><p class="zh">সবুজ বোতাম «2) PR1» চাপো: «Consegna» ফর্ম খুলবে।</p></li>
<li><b>In «Cosa consegni?» scrivi il numero della tua Pull Request: PR1 per la prima, PR2 per la seconda, PR3 per la terza…</b><p class="zh">«Cosa consegni?»-এ তোমার Pull Request-এর নম্বর লেখো: প্রথমটির জন্য PR1, দ্বিতীয়টির জন্য PR2, তৃতীয়টির জন্য PR3…</p></li>
<li><b>In «Il tuo testo» scrivi le 4 parti: Titolo · Cosa cambia · Dove · Perché (guarda l'esempio di Black Panter qui sopra).</b><p class="zh">«Il tuo testo»-এ ৪টি অংশ লেখো: শিরোনাম · কী বদলায় · কোথায় · কেন (উপরের Black Panter উদাহরণ দেখো)।</p></li>
<li><b>Se vuoi, aggiungi un'immagine. Poi premi «Invia».</b><p class="zh">চাইলে একটি ছবি যোগ করো। তারপর «Invia» চাপো।</p></li>
<li><b>Per la Pull Request dopo, riapri il Modulo con lo stesso bottone e scrivi PR2, poi PR3.</b><p class="zh">পরের Pull Request-এর জন্য একই বোতাম দিয়ে ফর্মটি আবার খোলো এবং PR2, তারপর PR3 লেখো।</p></li></ol>
<p><a class="bt" style="background:#1f6feb;font-size:16px;padding:8px 14px" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/3inf-backlog/">Il backlog: dove finisce la tua PR</a></p><p class="zh">backlog: তোমার PR কোথায় যায়।</p>
<p class="mu">Se il Modulo non funziona, scrivi la Pull Request nel Documento del compito su Classroom, con le stesse 4 parti. · ফর্ম কাজ না করলে, Classroom-এর ডকুমেন্টে একই ৪টি অংশ লেখো।</p>
<p><a class="bt" target="_blank" href="@@MC@@">2) PR1 — la mia Pull Request</a></p></div>
</div></body></html>"""
    bt1 = (f'<a class="bt" target="_blank" href="{MODULO_PARERE}">1) Feedback</a>' if MODULO_PARERE else '<span class="bt" style="opacity:.5">1) Feedback — arriva fra un minuto</span>')
    h = h.replace("@@BT1@@", bt1).replace("@@MC@@", MODULO_CONSEGNA)
    open(OUT, "w", encoding="utf-8").write(h)
    print(OUT)

main()
