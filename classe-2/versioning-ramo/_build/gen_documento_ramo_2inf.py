"""2INF 12/10/2026 — Teoria: il tuo Documento nell'albero delle versioni (IT + ZH; per la 2INF niente arabo, §2.49).
Genera docs/compito/2inf-20261012-documento/pagina.html (index.html è il caricatore fisso).
Segue REGOLE-COSTRUZIONE-TEORIA.md: titolo + traduzione, percorso in alto, FASE 1 teoria solo da leggere, FASE 2 bottone verde.
"""
import json, os, html
MODULO_PARERE = os.environ.get("MODULO_PARERE", "https://docs.google.com/forms/d/e/1FAIpQLScAY2tXZo-TZZRTKTRwGA85ftqhA5W07eBeAX89YLEugJvHCA/viewform")
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
.zh,.t-zh{{display:none}}
</style></head><body><div class="w">
<h1>{e(TITOLO[0])}</h1><p class="t-zh">{e(TITOLO[1])}</p><p class="mu">2INF · 12/10/2026</p>
<div class="card" style="border:3px solid var(--acc)"><p><b>Il tuo percorso di oggi</b></p><p class="zh">你今天的路线</p><ol>
<li><b>FASE 1 — Leggiamo insieme la teoria qui sotto, dall'inizio alla fine.</b><p class="zh">第1阶段——我们一起从头到尾读下面的理论。</p></li>
<li><b>FASE 2 — In fondo trovi due bottoni verdi: 1) Feedback (il tuo parere sulla teoria) e 2) PR1 (la tua prima Pull Request). </b><p class="zh">第2阶段——最后有两个绿色按钮：1) Feedback（你对理论的意见）和 2) PR1（你的第一个 Pull Request）。</p></li></ol></div>
<h2>FASE 1 — La teoria</h2>
<div class="card"><p><b>Dispensa a parte:</b> come lavorano le aziende di software, il Manifesto Agile e le 10 regole che usiamo nel nostro treno.</p><p class="zh">单独的讲义：软件公司怎么工作、Agile 宣言和我们火车游戏用的10条规则。</p>
<p><a class="bt" style="background:#1f6feb" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/teoria/agile/">Teoria Agile</a></p><p class="mu">Si apre in una scheda nuova: quando hai finito, chiudila e torni qui. · 在新的标签页打开。</p></div>
<div class="card"><h3>In breve</h3>{svg()}<ol>{breve}</ol></div>
<div class="card"><h3>La lavagna del prof</h3><img src="lavagna-versioni.jpg" alt="La lavagna: numeri delle versioni, changelog, fork, Pull Request accettata e rifiutata, merge" style="max-width:100%;border-radius:10px"><p>Sulla linea rossa le versioni (v0.8, v0.9, v1.0). In blu il fork che parte dalla v0.9. Sul ramo, le Pull Request: quella accettata (ACCEPT ✓) rientra con il MERGE, quella rifiutata (REFUSE ✗) resta fuori.</p><p class="zh">红线上是版本。蓝色是 fork。分支上是 Pull Request：接受的（ACCEPT ✓）通过 MERGE 回来，拒绝的（REFUSE ✗）留在外面。</p></div>
<div class="card"><h3>La storia vera del vostro gioco</h3><p>Ogni riga è una versione nata dalle vostre Pull Request (dal grafo delle versioni).</p><p class="zh">每一行是一个由你们的 Pull Request 产生的版本。</p>
<table><tr><th>Versione</th><th>Nome</th><th>Cosa è entrato e da quale Pull Request</th></tr>{storia}</table>
<p><a class="bt" style="font-size:16px;padding:8px 14px" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/">Apri il grafo delle versioni</a></p><p class="mu">Si apre in una scheda nuova: quando hai finito, chiudila e torni qui. · 在新的标签页打开：做完后关闭，回到这里。</p></div>
<div class="card"><h3>Come si chiede una modifica: il giro della Pull Request</h3>
<p>Nel vostro gioco funziona come in un'azienda vera. Tu proponi, il programma automatico legge, il prof decide, la versione nuova esce.</p>
<p class="zh">你们的游戏像真正的公司一样工作。你提出建议，自动程序读取，老师决定，新版本发布。</p>
<ol>
<li><b>Tu scrivi la richiesta</b> nel Modulo «Consegna» (o nel Documento): titolo, cosa cambia, dove, perché. Puoi aggiungere un'immagine.<p class="zh"><b>你写要求</b> «Consegna» 在表格里（或文档里）：标题、改变什么、在哪里、为什么。也可以加图片。</p></li>
<li><b>Lo script gira da solo</b> ogni 5 minuti: è un programma del prof su Google che legge le richieste nuove e le copia nel repository Git del corso, con il tuo nome e l'ora.<p class="zh"><b>脚本自己运行</b> 每几分钟一次：这是老师在 Google 上的程序，它读取新的要求，并连同你的名字和时间复制到课程的 Git repository 里。</p></li>
<li><b>Il prof (con l'intelligenza artificiale) legge</b> la tua Pull Request e decide: SÌ o NO.<p class="zh"><b>老师（和人工智能一起）阅读</b> 并决定：是或不。</p></li>
<li><b>SÌ = merge:</b> la modifica entra nel gioco, nasce una versione nuova (v1.5, v1.6…) e nel changelog c'è scritto il numero della tua Pull Request.<p class="zh"><b>是 = merge：</b> 修改进入游戏，产生新版本，changelog 里写着你的 Pull Request 编号。</p></li>
<li><b>Tu controlli</b> nel grafo delle versioni: il pallino nuovo è anche merito tuo. Se è NO, leggi il perché, correggi e rimanda.<p class="zh"><b>你查看</b> 在版本图里：新的圆点也有你的功劳。如果是不，读原因，修改后再发。</p></li>
</ol></div>
<div class="card"><h3>Com'è fatta una Pull Request</h3><p>Quattro parti, sempre, nel Modulo o nel Documento. Esempio vero: la richiesta «Più lento», entrata nel gioco con la v0.3.</p><p class="zh">总是四个部分。真实的例子：「更慢」的要求，在 v0.3 进入了游戏。</p>
<table><tr><th>Parte</th><th>Esempio</th></tr>{parti}</table></div>
<div class="card"><h3>Gli errori della settimana scorsa (e perché)</h3><ol>{errori}</ol></div>
<h2>FASE 2 — 1) Feedback e 2) PR1</h2>
<div class="card" style="border:3px solid #238636"><p><b>Due lavori, in ordine. Ognuno si apre in una scheda nuova: quando hai finito, chiudila e torni qui.</b></p><p class="zh">两个任务，按顺序。每个都在新的标签页打开：做完后关闭，回到这里。</p>
<h3>1) Feedback — il mio parere sulla teoria</h3><ol>
<li><b>Premi il bottone verde «1) Feedback».</b><p class="zh">按绿色按钮「1) Feedback」。</p></li>
<li><b>Rispondi alle 4 domande con parole tue, poi premi «Invia».</b><p class="zh">用你自己的话回答4个问题，然后按「Invia」（提交）。</p></li></ol>
<p>@@BT1@@</p>
<h3>2) PR1 — la mia prima Pull Request (una richiesta per il gioco)</h3><ol>
<li><b>Premi il bottone verde «2) PR1»: si apre il Modulo «Consegna».</b><p class="zh">按绿色按钮「2) PR1」：会打开「Consegna」表格。</p></li>
<li><b>In «Cosa consegni?» scrivi il numero della tua Pull Request: PR1 per la prima, PR2 per la seconda, PR3 per la terza…</b><p class="zh">在「Cosa consegni?」里写你的 Pull Request 编号：第一个写 PR1，第二个写 PR2，第三个写 PR3……</p></li>
<li><b>In «Il tuo testo» scrivi le 4 parti: Titolo · Cosa cambia · Dove · Perché (guarda l'esempio «Più lento» qui sopra).</b><p class="zh">在「Il tuo testo」里写4个部分：标题 · 改变什么 · 在哪里 · 为什么（看上面的例子）。</p></li>
<li><b>Se vuoi, aggiungi un'immagine. Poi premi «Invia».</b><p class="zh">想的话可以加一张图片。然后按「Invia」（提交）。</p></li>
<li><b>Per la Pull Request dopo, riapri il Modulo con lo stesso bottone e scrivi PR2, poi PR3.</b><p class="zh">下一个 Pull Request：用同一个按钮再打开表格，写 PR2，然后 PR3。</p></li></ol>
<p><a class="bt" style="background:#1f6feb;font-size:16px;padding:8px 14px" target="_blank" href="https://nicolaregge-pulse.github.io/corso-informatica/2inf-backlog/">Il backlog: dove finisce la tua PR</a></p><p class="zh">backlog：你的 PR 去哪里。</p>
<p class="mu">Se il Modulo non funziona, scrivi la Pull Request nel Documento del compito su Classroom, con le stesse 4 parti. · 如果表格不能用，就在 Classroom 的文档里写同样的4个部分。</p>
<p><a class="bt" target="_blank" href="@@MC@@">2) PR1 — la mia Pull Request</a></p></div>
</div></body></html>"""
    bt1 = (f'<a class="bt" target="_blank" href="{MODULO_PARERE}">1) Feedback</a>' if MODULO_PARERE else '<span class="bt" style="opacity:.5">1) Feedback — arriva fra un minuto</span>')
    h = h.replace("@@BT1@@", bt1).replace("@@MC@@", MODULO_CONSEGNA)
    open(OUT, "w", encoding="utf-8").write(h)
    print(OUT)

main()
