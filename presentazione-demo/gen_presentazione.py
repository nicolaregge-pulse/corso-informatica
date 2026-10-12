# -*- coding: utf-8 -*-
"""Presentazione della demo: la lezione della 2INF del 12/10/2026, senza nomi.

Scrive presentazione-demo.md (la fonte da leggere) e il PDF con le schermate.
Le schermate stanno in schermate/ e vengono dalla demo (strumenti/gen_demo.py): nomi già sostituiti.
Uso:  python3 presentazione-demo/gen_presentazione.py
"""
import html, os, subprocess

QUI = os.path.dirname(os.path.abspath(__file__))
VER = "1.0"
DATA = "20261012"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
DEMO = "https://script.google.com/macros/s/AKfycbyhkWr44IWarPFRvcyP0Ku1pI-XbFaeBVJA4I0iEITq_4U4XvD5rqiPci77-p2FLory/exec"
TITOLO = "Una scuola che lavora come un'azienda di software"

INTRO = [
    "Laboratorio di informatica del prof. Nicola Regge, istituto professionale a Milano. Molti ragazzi hanno alle spalle percorsi scolastici difficili; qui lavorano come in un'azienda vera, con gli strumenti dei programmatori.",
    "Questa è la lezione di una seconda del 12 ottobre 2026: tre ore di laboratorio. I nomi dei ragazzi sono sostituiti con «Allievo 01», «Allievo 02»…",
]
NUMERI = [("3 ore", "di laboratorio"), ("17", "ragazzi presenti"), ("129", "richieste di modifica"),
          ("20", "versioni nuove del gioco"), ("17 su 17", "hanno mandato almeno una richiesta")]
PAGINE = [
    ("00-home.png", "La demo", "La pagina d'ingresso della demo: si entra con la propria email e un codice, l'accesso vale 24 ore."),
    ("11-lavagna.jpg", "La lavagna", "Si parte dalla lavagna: versioni, registro delle modifiche (changelog), copia del progetto (fork), richiesta di modifica (Pull Request), accettata o rifiutata, unione (merge)."),
    ("01-compito.png", "Il compito della lezione", "Un solo link fisso su Classroom. In alto il percorso della giornata, poi la teoria da leggere (versioni del software e metodo Agile), poi i bottoni verdi del lavoro."),
    ("02-backlog.png", "Il backlog", "Ogni richiesta dei ragazzi entra qui con un riassunto e un peso (quanto lavoro chiede, con i numeri di Fibonacci). Si fanno prima le più leggere; ognuna diventa FATTO con la versione del gioco, oppure NO con il motivo."),
    ("03-novita.png", "Cosa è cambiato oggi nel gioco", "Il registro delle modifiche della giornata: ogni richiesta accettata è una versione nuova del gioco, con chi l'ha chiesta, cosa cambia e dove nel codice."),
    ("09-gioco-in-corso.png", "Il gioco della classe", "«Il treno blindato»: è cresciuto di 20 versioni in tre ore, tutte proposte dai ragazzi. Ogni versione resta giocabile."),
    ("04-voti.png", "I voti", "Il voto proposto si calcola da solo dalle richieste inviate, da quelle entrate nel gioco, da come sono scritte e dal feedback sulla teoria. Il voto finale lo decide il docente."),
    ("05-classifica.png", "La classifica", "Chi ha portato più modifiche dentro il gioco. Un allievo è passato da 40 a 62 dopo aver visto i voti pubblicati e aver chiesto aiuto: in pochi minuti ha mandato quattro richieste nuove."),
    ("06-monitor.png", "Il monitor della lezione", "Durante i giri il docente guarda gli schermi della classe; qui resta scritto cosa c'era su ogni computer. Solo fatti, senza giudizi."),
    ("10-grafo.png", "L'albero delle versioni", "La storia del gioco come la disegna Git: il ramo principale, le copie delle altre classi, i rami di lavoro, le unioni e le versioni maggiori."),
]


def md():
    r = ["# " + TITOLO, "", "**Versione %s** — 12/10/2026 — Prof. Nicola Regge. Presentazione della demo (lezione della 2INF, senza nomi)." % VER, ""]
    r += INTRO + ["", "## 00 I numeri della giornata", ""]
    r += ["%d. **%s** %s" % (i + 1, a, b) for i, (a, b) in enumerate(NUMERI)]
    for i, (img, t, d) in enumerate(PAGINE):
        r += ["", "## %02d %s" % (i + 1, t), "", "![%s](schermate/%s)" % (t, img), "", d]
    r += ["", "## %02d Prova la demo" % (len(PAGINE) + 1), "", "Apri l'indirizzo, scrivi la tua email, inserisci il codice che arriva per email e clicca «Apri la demo».", "", "```", DEMO, "```", ""]
    open(os.path.join(QUI, "presentazione-demo.md"), "w", encoding="utf-8").write("\n".join(r))


def pdf():
    e = html.escape
    num = "".join("<div><b>%s</b>%s</div>" % (e(a), e(b)) for a, b in NUMERI)
    pag = "".join('<section><h2>%02d %s</h2><p>%s</p><img src="schermate/%s"></section>' % (i + 1, e(t), e(d), img)
                  for i, (img, t, d) in enumerate(PAGINE))
    h = """<!doctype html><html lang=it><meta charset=utf-8><style>
@page{size:A4;margin:14mm}body{font:11.5pt/1.45 'DejaVu Sans',Arial,sans-serif;color:#111;margin:0}
h1{font-size:24pt;margin:30mm 0 6px;line-height:1.15}h2{font-size:15pt;margin:0 0 4px}.mu{color:#555}
.num{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}.num div{border:1px solid #ccc;border-radius:8px;padding:8px 12px;font-size:10pt}.num b{display:block;font-size:20pt}
section{break-before:page}section img{width:100%%;max-height:205mm;object-fit:contain;object-position:top;border:1px solid #ccc;border-radius:6px;margin-top:6px}
.link{border-left:5px solid #1f6feb;background:#eef4ff;padding:10px 12px;margin-top:16px;word-break:break-all;font-size:10pt}
</style><h1>%s</h1><p class=mu><b>Versione %s</b> — 12/10/2026 — Prof. Nicola Regge</p>%s<div class=num>%s</div>
<div class=link><b>Prova la demo.</b> Apri l'indirizzo, scrivi la tua email, inserisci il codice che arriva per email e clicca «Apri la demo».<br><br><a href="%s">%s</a></div>%s</html>""" % (
        e(TITOLO), VER, "".join("<p>%s</p>" % e(x) for x in INTRO), num, e(DEMO), e(DEMO), pag)
    hp = os.path.join(QUI, "_presentazione.html")
    open(hp, "w", encoding="utf-8").write(h)
    out = os.path.join(QUI, "%s_Demo-Lezione-2INF_Presentazione_v%s.pdf" % (DATA, VER))
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + out, "file://" + hp], capture_output=True)
    os.remove(hp)
    print(out)


if __name__ == "__main__":
    md()
    pdf()
