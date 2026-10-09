# -*- coding: utf-8 -*-
"""Lezione 09/10/2026 (1INF e 2INF): la storia del Treno blindato — versioni, rami, fork, merge e il grafo di Git.
Genera dalla stessa fonte: il .md (per l'AI dei ragazzi), la pagina web docs/lezione-versioni/index.html e il PDF trilingue.
Le versioni si leggono dai file versioni.json dei giochi, così la storia è sempre quella vera."""
import html, json, os, base64
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GI = os.path.join(ROOT, "docs", "giochi")
VERSIONE = "1.0"
DATA = "09/10/2026"
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
GRAFO = SITO + "giochi/grafo/"
e = html.escape

def V(d): return json.load(open(os.path.join(GI, d, "versioni", "versioni.json"), encoding="utf-8"))

STORIA = [
    ("2INF — Il treno blindato (HTML), il ramo principale", "#2f81f7", V("treno-blindato"),
     "١٢ نسخة من v0.0 إلى v0.11: من الفكرة الأولى إلى اللعبة الكاملة.", "从 v0.0 到 v0.11 共12个版本：从第一个想法到完整的游戏。"),
    ("3INF — fork (copia) del gioco della 2INF", "#3fb950", V("treno-3inf"),
     "صف 3INF نسخ لعبة 2INF (fork) وأضاف أشراراً ومناظر جديدة.", "3INF 班复制（fork）了 2INF 的游戏，并加入了新的坏人和风景。"),
    ("1INF — fork (copia) del gioco della 2INF", "#f0883e", V("treno-1inf"),
     "صفكم 1INF نسخ اللعبة وأضاف أشراركم وألوان السماء.", "你们 1INF 班复制了游戏，加入了你们的坏人和天空的颜色。"),
    ("Ramo di lavoro del prof: «immagini della classe» → merge nella 1INF", "#db61a2",
     [{"versione": "immagini", "nome": "Nuova funzione su un ramo separato", "cambi": "Il prof prova una cosa nuova su un RAMO a parte, così il gioco che funziona non si rompe: cartelle per le immagini (cattivi, paesaggi, difetti, revisioni), galleria con i nomi, foto prese da sole dalle consegne di Classroom. Quando funziona: MERGE (unione) nel ramo della 1INF."}],
     "الأستاذ جرّب ميزة جديدة في فرع منفصل، ثم دمجها (merge) في فرع 1INF.", "老师在一个单独的分支上试了新功能，然后把它合并（merge）到 1INF 的分支。"),
    ("1INF su Godot — versione 2.0 (major)", "#a371f7", V("treno-godot"),
     "نفس اللعبة لكن بمحرك Godot: تغيير كبير، لذلك الرقم يصبح 2.0.", "同一个游戏，但是用 Godot 引擎做的：大变化，所以版本号变成 2.0。"),
]

PAROLE = [
    ("versione (commit)", "نسخة (حفظ commit)", "版本（提交 commit）", "Ogni pallino del grafo: v0.3, v1.1, v2.0…"),
    ("ramo (branch)", "فرع (branch)", "分支（branch）", "Una linea del grafo: il gioco cresce lungo il ramo."),
    ("fork (copia)", "نسخة مستقلة (fork)", "复刻（fork，复制）", "La 1INF copia il gioco della 2INF e lo fa crescere per conto suo."),
    ("Pull Request (proposta di modifica)", "اقتراح تعديل (Pull Request)", "修改建议（Pull Request）", "Il vostro Documento su Classroom: «il mio cattivo si chiama…»."),
    ("merge (unione)", "دمج (merge)", "合并（merge）", "Il ramo «immagini» rientra nel ramo della 1INF."),
    ("versione minor (1.1, 1.2…)", "إصدار صغير (1.1، 1.2…)", "小版本（1.1、1.2……）", "Piccole aggiunte: un cattivo nuovo, un cielo nuovo."),
    ("versione major (2.0)", "إصدار كبير (2.0)", "大版本（2.0）", "Cambia una cosa grossa: il motore diventa Godot."),
    ("release (versione pubblicata)", "إصدار منشور (release)", "发布（release）", "La versione che tutti possono giocare con un link."),
]

PASSI = [
    ("Carta e penna sul banco: oggi si disegna il grafo a mano.", "ضع الورقة والقلم على الطاولة: اليوم نرسم الرسم البياني باليد.", "桌上放好纸和笔：今天我们用手画版本图。"),
    ("VINCI SUBITO (5 minuti). Apri il grafo, clicca il primo pallino BLU (v0.0) e premi il bottone verde «Apri questa versione»: gioca 30 secondi. Poi torna al grafo, clicca il pallino VIOLA (v2.0) e gioca ancora. Sul foglio scrivi 2 cose che sono cambiate.",
     "اربح فوراً: افتح الرسم البياني، اضغط أول دائرة زرقاء (v0.0) ثم الزر الأخضر، والعب 30 ثانية. ثم اضغط الدائرة البنفسجية (v2.0) والعب. اكتب على الورقة شيئين تغيّرا.",
     "马上赢：打开版本图，点第一个蓝色圆点（v0.0），按绿色按钮，玩30秒。再点紫色圆点（v2.0）再玩。在纸上写两样改变了的东西。"),
    ("Leggi le 8 parole del grafo (tabella qui sotto) e copiale sul foglio con la traduzione nella tua lingua.",
     "اقرأ الكلمات الثماني (الجدول أدناه) وانسخها على الورقة مع الترجمة بلغتك.", "读下面表格里的8个词，把它们和你的语言的翻译一起抄在纸上。"),
    ("Clicca i pallini del TUO ramo (arancione per la 1INF, blu per la 2INF): leggi «Cosa è cambiato e perché». Trova la versione dove c'è una cosa fatta dalla tua classe.",
     "اضغط دوائر فرعك (برتقالي لـ 1INF، أزرق لـ 2INF) واقرأ ماذا تغيّر ولماذا. ابحث عن النسخة التي فيها شيء صنعه صفك.",
     "点你们分支的圆点（1INF 是橙色，2INF 是蓝色），读「改变了什么，为什么」。找到有你们班做的东西的版本。"),
    ("SCHEMA A MANO: disegna sul foglio un grafo con 3 colori: il ramo principale, un fork e un ramo di lavoro che rientra con un merge. Sotto ogni pallino scrivi il numero di versione.",
     "ارسم باليد رسماً بثلاثة ألوان: الفرع الرئيسي، نسخة fork، وفرع عمل يعود بـ merge. اكتب رقم النسخة تحت كل دائرة.",
     "手画图：用三种颜色画：主分支、一个 fork、一个用 merge 合并回来的工作分支。在每个圆点下写版本号。"),
    ("PROVA DEL NOVE: spiega a voce al compagno, con parole tue, cos'è un merge e perché la versione Godot si chiama 2.0 e non 1.2.",
     "اشرح لزميلك بكلماتك: ما هو merge، ولماذا نسخة Godot اسمها 2.0 وليس 1.2.",
     "用你自己的话给同学讲：什么是 merge，为什么 Godot 版本叫 2.0 而不是 1.2。"),
]

PERCHE = [
    ("Perché i numeri cambiano così", "v0.x = le prove, prima della versione stabile (la 2INF ha fatto 12 prove: v0.0 → v0.11). 1.0 = la prima versione «vera» di un ramo (il fork della 1INF e della 3INF). 1.1, 1.2 = versioni MINOR: piccole aggiunte (un cattivo, un cielo). 2.0 = versione MAJOR: cambia una cosa grossa (il motore Godot), il primo numero sale e il secondo riparte da 0.",
     "v0.x = تجارب. 1.0 = أول نسخة حقيقية. 1.1، 1.2 = إضافات صغيرة (minor). 2.0 = تغيير كبير (major): الرقم الأول يزيد والثاني يعود إلى 0.",
     "v0.x = 试验。1.0 = 第一个真正的版本。1.1、1.2 = 小的增加（minor）。2.0 = 大的改变（major）：第一个数字加一，第二个数字回到 0。"),
    ("Perché si fanno i rami", "Per provare una cosa nuova SENZA rompere il gioco che funziona. Il prof ha fatto la funzione «immagini della classe» su un ramo a parte; quando funzionava l'ha unita (merge) al ramo della 1INF. Nelle aziende si lavora sempre così: ognuno sul suo ramo, poi Pull Request, controllo e merge.",
     "لنجرّب شيئاً جديداً دون أن نكسر اللعبة التي تعمل. في الشركات يعمل كل واحد على فرعه، ثم Pull Request، ثم مراجعة، ثم merge.",
     "为了试新东西而不弄坏能玩的游戏。在公司里大家都这样工作：每人在自己的分支上，然后 Pull Request、检查、合并（merge）。"),
    ("Perché Godot (v2.0)", "Godot è un motore vero per videogiochi, gratis e portabile (non si installa), usato anche nel lavoro. I vostri cattivi ci sono ancora: stanno nei file di dati (cattivi.json), uguali a prima. Ponte da Lazarus: Lazarus REAGISCE (aspetta un clic), Godot PULSA (_process gira da solo circa 60 volte al secondo).",
     "Godot محرك حقيقي للألعاب، مجاني ولا يحتاج تثبيت. أشراركم ما زالوا موجودين في ملف البيانات cattivi.json. Lazarus ينتظر النقرة، Godot ينبض 60 مرة في الثانية.",
     "Godot 是真正的游戏引擎，免费、不用安装。你们的坏人还在数据文件 cattivi.json 里。Lazarus 等待点击，Godot 每秒跳动约60次。"),
]

def img_b64(p): return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()

def build_md():
    L = [f"# La storia del nostro gioco: versioni, rami e il grafo di Git", "", f"**Versione {VERSIONE}** — {DATA} · Classi 1INF e 2INF · Laboratorio",
         "", "Testo per la tua AI: chiedile di spiegarti ogni parte nella tua lingua.", "",
         "## 01 Che cosa facciamo oggi", ""]
    for i, (it, ar, zh) in enumerate(PASSI, 1):
        L += [f"{i}. {it}", f"   {i}.1 العربية: {ar}", f"   {i}.2 中文：{zh}"]
    L += ["", "Indirizzo del grafo (scrivilo esattamente così):", "", "```", GRAFO, "```", "", "![Il grafo delle versioni](../../docs/lezione-versioni/grafo-20261009.png)", "",
          "## 02 Le 8 parole del grafo", "", "| Italiano | العربية | 中文 | Nel nostro gioco |", "|---|---|---|---|"]
    for it, ar, zh, es in PAROLE:
        L.append(f"| {it} | {ar} | {zh} | {es} |")
    L += ["", "## 03 Perché", ""]
    for i, (t, it, ar, zh) in enumerate(PERCHE, 1):
        L += [f"{i}. **{t}.** {it}", f"   {i}.1 العربية: {ar}", f"   {i}.2 中文：{zh}"]
    L += ["", "## 04 La storia, ramo per ramo", ""]
    for i, (nome, col, vers, ar, zh) in enumerate(STORIA, 1):
        L += [f"{i}. **{nome}** — العربية: {ar} · 中文：{zh}"]
        for j, v in enumerate(vers, 1):
            L.append(f"   {i}.{j} **{v['versione']} — {v['nome']}.** {v.get('cambi', '')}")
    L += ["", "## 05 Changelog", "", f"1. v{VERSIONE} ({DATA}) — prima versione della lezione."]
    return "\n".join(L) + "\n"

def build_html(per_pdf=False):
    img = img_b64(os.path.join(ROOT, "docs", "lezione-versioni", "grafo-20261009.png")) if per_pdf else "grafo-20261009.png"
    css = """:root{--bg:#fbfaf7;--card:#fff;--tx:#111;--mu:#555;--ln:#ddd;--oro:#b07a00}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--oro:#ffd34d}}
:root[data-theme="dark"]{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--oro:#ffd34d}
body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.5 "DejaVu Sans",system-ui,Segoe UI,Arial,sans-serif}.w{max-width:1000px;margin:0 auto;padding:16px}
h1{font-size:clamp(24px,6vw,34px);margin:4px 0}h2{font-size:21px;margin:26px 0 8px;border-bottom:2px solid var(--ln);padding-bottom:4px}.mu{color:var(--mu)}
.card{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:12px 14px;margin:10px 0}
ol{padding-left:22px}li{margin:8px 0}.ar{direction:rtl;text-align:right;font-family:Amiri,"DejaVu Sans",serif;font-size:19px;color:var(--mu);margin:2px 0}
.zh{font-family:"WenQuanYi Zen Hei","Noto Sans CJK SC",sans-serif;color:var(--mu);margin:2px 0}
table{border-collapse:collapse;width:100%;font-size:15px}td,th{border:1px solid var(--ln);padding:6px 8px;text-align:left;vertical-align:top}th{background:rgba(127,127,127,.12)}
td.ar{text-align:right}.dot{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:6px;vertical-align:-2px}
.box{border-left:5px solid #2f81f7;background:rgba(47,129,247,.08);padding:8px 12px;border-radius:6px}
pre{background:rgba(127,127,127,.12);padding:8px 10px;border-radius:8px;overflow-x:auto;font-size:15px}
.bt{display:inline-block;background:#238636;color:#fff;font-weight:700;text-decoration:none;border-radius:10px;padding:10px 16px;margin:6px 8px 6px 0}
img{max-width:100%;border-radius:10px;border:1px solid var(--ln)}
@media print{.np{display:none}h2{break-after:avoid}.card,tr{break-inside:avoid}}"""
    H = [f"<!doctype html><html lang='it'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Versioni del treno</title><style>{css}</style></head><body><div class='w'>",
         f"<h1>La storia del nostro gioco: versioni, rami e il grafo di Git</h1>",
         f"<p class='mu'>Versione {VERSIONE} — {DATA} · Classi 1INF e 2INF · Laboratorio</p>",
         "<p class='ar'>قصة لعبتنا: النسخ والفروع ورسم Git البياني</p><p class='zh'>我们游戏的故事：版本、分支和 Git 版本图</p>",
         f"<p class='np'><a class='bt' href='{GRAFO}'>Apri il grafo delle versioni</a><a class='bt' href='{SITO}giochi/treno-godot/' style='background:#8957e5'>Gioca la v2.0 (Godot)</a></p>",
         "<h2>01 Che cosa facciamo oggi</h2><ol>"]
    for it, ar, zh in PASSI:
        H.append(f"<li><b>{e(it)}</b><p class='ar'>{e(ar)}</p><p class='zh'>{e(zh)}</p></li>")
    H.append(f"</ol><div class='card'>Indirizzo del grafo · <span class='ar' style='display:inline'>العنوان (اكتبه كما هو تماماً)</span> · <span class='zh' style='display:inline'>网址（照原样输入）</span><pre>{GRAFO}</pre></div>")
    H.append(f"<img src='{img}' alt='Il grafo delle versioni: ramo blu della 2INF, fork verde della 3INF, fork arancione della 1INF, ramo rosa delle immagini con il merge, versione 2.0 viola su Godot'>")
    H.append("<h2>02 Le 8 parole del grafo</h2><table><tr><th>Italiano</th><th>العربية</th><th>中文</th><th>Nel nostro gioco</th></tr>")
    for it, ar, zh, es in PAROLE:
        H.append(f"<tr><td><b>{e(it)}</b></td><td class='ar'>{e(ar)}</td><td class='zh'>{e(zh)}</td><td>{e(es)}</td></tr>")
    H.append("</table><h2>03 Perché</h2><ol>")
    for t, it, ar, zh in PERCHE:
        H.append(f"<li><b>{e(t)}.</b> {e(it)}<p class='ar'>{e(ar)}</p><p class='zh'>{e(zh)}</p></li>")
    H.append("</ol><h2>04 La storia, ramo per ramo</h2>")
    for nome, col, vers, ar, zh in STORIA:
        H.append(f"<div class='card'><b><span class='dot' style='background:{col}'></span>{e(nome)}</b><p class='ar'>{e(ar)}</p><p class='zh'>{e(zh)}</p><table>")
        for v in vers:
            H.append(f"<tr><td style='width:90px'><b>{e(v['versione'])}</b></td><td><b>{e(v['nome'])}.</b> {e(v.get('cambi', ''))}</td></tr>")
        H.append("</table></div>")
    H.append(f"<p class='mu'>Changelog: v{VERSIONE} ({DATA}) — prima versione della lezione.</p></div></body></html>")
    return "\n".join(H)

def main():
    D = os.path.join(ROOT, "classe-1", "lezione-versioni-treno")
    open(os.path.join(D, "lezione-versioni-treno.md"), "w", encoding="utf-8").write(build_md())
    open(os.path.join(ROOT, "docs", "lezione-versioni", "index.html"), "w", encoding="utf-8").write(build_html())
    open(os.path.join(D, "_build", "lezione-versioni-treno.html"), "w", encoding="utf-8").write(build_html(per_pdf=True))
    print("ok")

if __name__ == "__main__":
    main()
