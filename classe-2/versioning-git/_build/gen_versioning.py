# -*- coding: utf-8 -*-
"""2INF, 09/10/2026 (1 ora): dispensa «Versioni e Git» costruita sul Treno blindato di ieri (e sul fork della 3INF).
Una fonte → .md (per l'AI dei ragazzi), pagina web docs/2inf-versioning/ e PDF. Lingue della 2INF: italiano e cinese (§2.49)."""
import html, os, base64
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VER, DATA = "1.0", "09/10/2026"
S = "https://nicolaregge-pulse.github.io/corso-informatica/"
G = "https://github.com/nicolaregge-pulse/corso-informatica"
e = html.escape
LINK = [
    ("Il grafo delle versioni (clicca i pallini)", S + "giochi/grafo/", "版本图（点圆点）"),
    ("Tutte le versioni del vostro treno, giocabili", S + "giochi/treno-blindato/versioni/", "你们火车游戏的所有版本，都可以玩"),
    ("Il changelog del treno (la lista dei cambiamenti)", G + "/blob/main/docs/giochi/treno-blindato/CHANGELOG.md", "火车游戏的更新日志"),
    ("La storia dei commit del ramo treno-2inf", G + "/commits/treno-2inf", "treno-2inf 分支的提交历史"),
    ("Il grafo vero di Git su GitHub (Network)", G + "/network", "GitHub 上真正的 Git 图"),
    ("Il fork della 3INF: il loro treno", S + "giochi/treno-3inf/", "3INF 的 fork：他们的火车"),
    ("La versione 2.0 su Godot", S + "giochi/treno-godot/", "Godot 上的 2.0 版本"),
]
TEORIA = [
    ("Versione", "Una «fotografia» del progetto in un momento preciso, con un numero. Il vostro treno è passato da v0.0 (prima idea, finestrino laterale) a v0.11 (i punteggi si salvano sempre): 12 versioni in un giorno.",
     "版本：项目在某个时刻的「照片」，有一个编号。你们的火车从 v0.0 到 v0.11，一天12个版本。",
     "Apri «Tutte le versioni» e gioca la v0.0 e la v0.11: cosa è cambiato?"),
    ("Git e GitHub", "Git è il programma che ricorda TUTTA la storia del progetto: chi ha cambiato cosa, quando e perché. GitHub è il sito dove il progetto (il repository) sta online. Il nostro repository si chiama corso-informatica.",
     "Git 是记住项目全部历史的程序：谁、什么时候、改了什么、为什么。GitHub 是放项目（仓库 repository）的网站。",
     "Apri «La storia dei commit»: ogni riga è un salvataggio."),
    ("Commit", "Un salvataggio nella storia di Git, con un messaggio che spiega il cambiamento. Esempio vero di ieri: 7724900 «Treno blindato v0.11: i punteggi si salvano sempre». Il numero strano (7724900) è il codice del commit.",
     "提交（commit）：Git 历史里的一次保存，带一句说明。昨天的例子：7724900「v0.11：分数总是保存」。",
     "Trova nella storia il commit della v0.5 (la Pull Request #104)."),
    ("Branch (ramo)", "Una linea di lavoro separata. Si apre un ramo per provare una cosa nuova senza rompere il gioco che funziona. Il vostro gioco sta nel ramo treno-2inf; il prof ha provato le «immagini della classe» su un ramo a parte.",
     "分支（branch）：一条单独的工作线，用来试新东西而不弄坏能玩的游戏。你们的游戏在 treno-2inf 分支。",
     "Nel grafo: quante linee (rami) vedi?"),
    ("Fork (copia)", "La copia di un progetto intero che cresce per conto suo. Ieri la 3INF ha fatto il fork del vostro treno alla v0.11 e lo ha portato alla v1.4 (montagna, Black Panter, Nash…); anche la 1INF.",
     "复刻（fork）：整个项目的复制，自己继续发展。昨天 3INF 在 v0.11 复制了你们的火车，做到了 v1.4。",
     "Nel grafo: da quale vostra versione parte la linea verde della 3INF?"),
    ("Push", "Mandare i propri commit dal PC al repository online (GitHub). Ieri, dopo ogni versione, il prof ha fatto il push: per questo il gioco sul sito cambiava da solo.",
     "推送（push）：把自己的提交从电脑发送到网上的仓库（GitHub）。",
     "Perché il gioco sul telefono cambiava senza scaricare niente?"),
    ("Pull", "Il contrario del push: prendere da GitHub l'ultima versione e portarla sul proprio PC. La v0.11 del treno «chiede sempre alla rete la versione nuova»: è un pull automatico.",
     "拉取（pull）：和 push 相反，从 GitHub 把最新版本拿到自己的电脑上。",
     "Quando fai un pull, cosa ricevi?"),
    ("Pull Request (proposta di modifica)", "«Ho fatto una modifica: la vuoi nel progetto?». Qualcuno la controlla e, se va bene, fa il MERGE (la unisce). Ieri le vostre richieste su Classroom erano Pull Request: la #104 della squadra MOTORE FISICA è diventata la v0.5.",
     "合并请求（Pull Request）：「我做了一个修改，你要放进项目吗？」检查后如果可以就合并（merge）。#104 变成了 v0.5。",
     "Chi decide se una Pull Request entra nel gioco?"),
    ("Changelog (registro dei cambiamenti)", "La lista, versione per versione, di cosa è cambiato e perché. Il treno ha il suo CHANGELOG.md: chi gioca sa cosa c'è di nuovo, chi programma sa dove cercare un errore.",
     "更新日志（changelog）：每个版本改变了什么、为什么的清单。",
     "Apri il changelog: qual è la novità della v0.7?"),
    ("Numeri delle versioni (major.minor)", "v0.x = prove; 1.0 = prima versione stabile (il fork della 3INF parte da 1.0); 1.1, 1.2 = piccole aggiunte (minor); 2.0 = cambio grosso (major): il gioco rifatto con Godot è la v2.0.",
     "版本号：v0.x 是试验；1.0 第一个稳定版本；1.1、1.2 小改动（minor）；2.0 大改变（major），用 Godot 重做的游戏就是 2.0。",
     "Perché la versione Godot non si chiama v1.5?"),
]

def build_md():
    L = ["# Versioni e Git: la storia del nostro Treno blindato", "", f"**Versione {VER}** — {DATA} · Classe 2INF · lezione frontale di 1 ora", "",
         "Testo per la tua AI: chiedile di spiegarti ogni parola nella tua lingua.", "", "## 01 I link della lezione", ""]
    for i, (t, u, z) in enumerate(LINK, 1):
        L += [f"{i}. {t} · {z}", "", "```", u, "```", ""]
    L += ["## 02 Le 10 parole, con il nostro gioco", ""]
    for i, (t, it, zh, prova) in enumerate(TEORIA, 1):
        L += [f"{i}. **{t}.** {it}", f"   {i}.1 中文：{zh}", f"   {i}.2 Prova: {prova}"]
    L += ["", "## 03 Changelog", "", f"1. v{VER} ({DATA}) — prima versione."]
    return "\n".join(L) + "\n"

def build_html(pdf=False):
    css = """:root{--bg:#fbfaf7;--card:#fff;--tx:#111;--mu:#555;--ln:#ddd;--acc:#1f6feb}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}}
:root[data-theme="dark"]{--bg:#0d1117;--card:#161b22;--tx:#e6edf3;--mu:#9aa4ae;--ln:#30363d;--acc:#58a6ff}
body{margin:0;background:var(--bg);color:var(--tx);font:17px/1.5 "DejaVu Sans",system-ui,Segoe UI,Arial,sans-serif}.w{max-width:980px;margin:0 auto;padding:16px}
h1{font-size:clamp(24px,6vw,34px);margin:4px 0}h2{font-size:21px;margin:24px 0 8px;border-bottom:2px solid var(--ln);padding-bottom:4px}.mu{color:var(--mu)}
.zh{font-family:"WenQuanYi Zen Hei","Noto Sans CJK SC",sans-serif;color:var(--mu);margin:3px 0}
.card{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:12px 14px;margin:10px 0}
.n{display:inline-block;min-width:30px;height:30px;line-height:30px;text-align:center;border-radius:50%;background:var(--acc);color:#fff;font-weight:800;margin-right:8px}
.pr{border-left:4px solid #2f9e57;padding:4px 10px;margin-top:6px;background:rgba(47,158,87,.08);border-radius:4px}
a.l{display:block;padding:9px 12px;border:1px solid var(--ln);border-radius:10px;margin:6px 0;text-decoration:none;color:var(--acc);font-weight:700;background:var(--card)}
a.l span{display:block;font-weight:400;font-size:14px}
.box{border-left:5px solid #b07a00;background:rgba(255,211,77,.12);padding:8px 12px;border-radius:6px}
@media print{.np{display:none}.card{break-inside:avoid}}"""
    H = [f"<!doctype html><html lang='it'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>2INF Versioni e Git</title><style>{css}</style></head><body><div class='w'>",
         "<h1>Versioni e Git: la storia del nostro Treno blindato</h1>", f"<p class='mu'>Versione {VER} — {DATA} · Classe 2INF · 1 ora</p>",
         "<p class='zh'>版本和 Git：我们的装甲火车的故事</p>",
         "<div class='box'>Carta e penna sul banco: scrivi le 10 parole e disegna il grafo a mano. · 桌上放好纸和笔：写下10个词，用手画版本图。</div>",
         "<h2>01 I link della lezione</h2>"]
    for t, u, z in LINK:
        H.append(f"<a class='l' href='{u}'>{e(t)}<span class='zh'>{e(z)}</span>" + (f"<span class='mu'>{e(u)}</span>" if pdf else "") + "</a>")
    H.append("<h2>02 Le 10 parole, con il nostro gioco</h2>")
    for i, (t, it, zh, prova) in enumerate(TEORIA, 1):
        H.append(f"<div class='card'><b><span class='n'>{i}</span>{e(t)}</b><p>{e(it)}</p><p class='zh'>{e(zh)}</p><div class='pr'><b>Prova:</b> {e(prova)}</div></div>")
    H.append(f"<p class='np'><a class='l' href='avanzamento/'>Avanzamento della classe<span class='zh'>全班进度</span></a></p><p class='mu'>Changelog: v{VER} ({DATA}) — prima versione.</p></div></body></html>")
    return "\n".join(H)

def main():
    D = os.path.join(ROOT, "classe-2", "versioning-git")
    open(os.path.join(D, "versioning-git.md"), "w", encoding="utf-8").write(build_md())
    open(os.path.join(ROOT, "docs", "2inf-versioning", "index.html"), "w", encoding="utf-8").write(build_html())
    open(os.path.join(D, "_build", "versioning-git.html"), "w", encoding="utf-8").write(build_html(pdf=True))
    print("ok")

if __name__ == "__main__":
    main()
