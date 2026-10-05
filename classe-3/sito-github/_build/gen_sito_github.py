# -*- coding: utf-8 -*-
"""Classe 3 — lunedì 05/10/2026: il primo sito PUBBLICO.

Genera (HTML -> PDF con Chrome headless):
  1. Dispensa 1 — La mia pagina web da zero (index.html + style.css, due file distinti)   IT / IT-BN
  2. Dispensa 2 — Pubblica il tuo primo sito su GitHub (GitHub Pages, solo browser)       IT / IT-BN
  3. Compito — Il mio primo sito pubblico (Documento con HTML, CSS separati, screenshot)   IT / IT-BN
  4. Chiave e griglia per il docente
  5. Pagina unica docs/3inf-sito/ (link stabile per Classroom, con i bottoni COPIA del codice)

Uso:  python3 classe-3/sito-github/_build/gen_sito_github.py
"""
import html, os, shutil, subprocess, glob

VER = "1.0"
DATA = "05/10/2026"
PREF = "20261005_Classe-3"
QUI = os.path.dirname(os.path.abspath(__file__))
CART = os.path.dirname(QUI)                                   # classe-3/sito-github
ROOT = os.path.dirname(os.path.dirname(CART))                 # repo
DOCS = os.path.join(ROOT, "docs", "3inf-sito")
FONTS = os.path.join(ROOT, "classe-3", "cosa-e-git", "fonts")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HUB = "https://nicolaregge-pulse.github.io/corso-informatica/3inf-sito/"

# ---------------------------------------------------------------- il codice (dati INVENTATI)
HTML_CODE = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Il mio primo sito</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Ciao, sono Leo</h1>
  <p class="sotto">Questo è il mio primo sito web.</p>

  <div class="scheda">
    <h2>Chi sono</h2>
    <p>Studio informatica e mi piace creare cose nuove.</p>

    <h2>Le mie passioni</h2>
    <ul>
      <li>Calcio</li>
      <li>Videogiochi</li>
      <li>Musica</li>
    </ul>

    <h2>Il mio sogno</h2>
    <p>Lavorare con i computer.</p>
  </div>

  <p class="piede">Sito creato da me - 2026</p>
</body>
</html>
"""

CSS_CODE = """body {
  background: lightblue;
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

h1 {
  color: darkblue;
}

.sotto {
  color: gray;
}

.scheda {
  background: white;
  max-width: 500px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 12px;
  text-align: left;
}

h2 {
  color: teal;
}

.piede {
  font-size: 12px;
  color: gray;
}
"""

E = html.escape

# ---------------------------------------------------------------- stile comune dei PDF
CSS_PDF = """
@font-face{font-family:'NotoBN';src:url('file://%(f)s/bn-400.woff2') format('woff2');}
@font-face{font-family:'NotoBN';font-weight:bold;src:url('file://%(f)s/bn-700.woff2') format('woff2');}
@page{size:A4;margin:13mm 13mm 12mm}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;color:#1a1a1a;line-height:1.5;font-size:10.8pt;font-family:"DejaVu Sans",Arial,sans-serif}
.bn{font-family:'NotoBN',"DejaVu Sans",sans-serif;font-size:11.2pt;line-height:1.75;color:#1d4d2f}
.cover{background:linear-gradient(160deg,#eef4fb,#e9f7ee);padding:7mm 8mm;border-radius:8px;margin-bottom:4mm;position:relative}
.cover h1{color:#12467a;font-size:18.5pt;margin:0 0 1.5mm;line-height:1.25}.cover .s{color:#445;font-size:10pt}
.cover .bn{font-size:12pt;margin-top:1mm}
.ver{position:absolute;top:4mm;right:5mm;background:#12467a;color:#fff;font-weight:bold;font-size:10pt;padding:1mm 3mm;border-radius:12px}
h2{color:#12467a;font-size:13.5pt;margin:5mm 0 2mm;border-bottom:3px solid #cfe0f0;padding-bottom:1mm;page-break-after:avoid}
.goal{background:#e9f6ee;border-left:5px solid #2f9e57;padding:2.5mm 3.5mm;border-radius:4px;margin:2.5mm 0;page-break-inside:avoid}
.note{background:#fff8e6;border-left:5px solid #d0a516;padding:2.5mm 3.5mm;border-radius:4px;margin:2.5mm 0;page-break-inside:avoid}
.warn{background:#fdecea;border-left:5px solid #c0392b;padding:2.5mm 3.5mm;border-radius:4px;margin:2.5mm 0;page-break-inside:avoid}
.info{background:#eaf2fb;border-left:5px solid #1f6fa5;padding:2.5mm 3.5mm;border-radius:4px;margin:2.5mm 0;page-break-inside:avoid}
.step{border:1px solid #cfdae6;border-radius:8px;margin:2.6mm 0;page-break-inside:avoid;overflow:hidden}
.step .h{background:#1f6fa5;color:#fff;padding:1.6mm 3mm;font-weight:bold;font-size:10.8pt}
.step .h .n{display:inline-block;background:#fff;color:#1f6fa5;border-radius:50%%;width:6.5mm;height:6.5mm;text-align:center;line-height:6.5mm;margin-right:2mm;font-size:10pt}
.step .b{padding:2mm 3.5mm}
.step .b p{margin:0 0 1.2mm}
.step.ok .h{background:#2f9e57}.step.ok .h .n{color:#2f9e57}
.tasto{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #cddae8;padding:0 4px;border-radius:3px;font-size:9.6pt;white-space:nowrap}
pre{background:#1e2733;color:#e8eef5;border-radius:6px;padding:3mm 4mm;font-family:"DejaVu Sans Mono",monospace;font-size:8.7pt;line-height:1.38;white-space:pre-wrap;margin:1.5mm 0 3mm;page-break-inside:avoid}
.codet{font-weight:bold;color:#fff;background:#12467a;display:inline-block;padding:1mm 3mm;border-radius:5px 5px 0 0;margin-top:3mm;font-size:10pt}
.codet.css{background:#8a3ab9}
table{border-collapse:collapse;width:100%%;margin:2mm 0;page-break-inside:avoid}
th,td{border:1px solid #cfdbe8;padding:1.4mm 2.4mm;vertical-align:top;text-align:left;font-size:9.8pt}
th{background:#12467a;color:#fff}th.bn{color:#fff}
td.c{font-family:"DejaVu Sans Mono",monospace;white-space:nowrap;font-size:9.2pt}
.sw{display:inline-block;width:4mm;height:4mm;border:1px solid #888;vertical-align:middle;margin-right:1.5mm;border-radius:2px}
/* schermate disegnate */
.scr{border:2px solid #9aa9b8;border-radius:7px;background:#fff;font-size:8.8pt;margin:2mm 0 1mm;overflow:hidden;page-break-inside:avoid;font-family:"DejaVu Sans",Arial,sans-serif;color:#24292f}
.scr .bar{background:#e8edf2;padding:1mm 2.5mm;font-family:"DejaVu Sans Mono",monospace;color:#555;font-size:8.2pt;border-bottom:1px solid #cfd8e2}
.scr .gh{background:#24292f;color:#fff;padding:1.6mm 3mm;display:flex;justify-content:space-between;align-items:center}
.scr .in{padding:2.5mm 3.5mm}
.hl{outline:3px solid #e0312b;outline-offset:1px;border-radius:4px}
.fr{color:#e0312b;font-weight:bold;font-size:9pt;white-space:nowrap}
.gbtn{display:inline-block;background:#1f883d;color:#fff;font-weight:bold;padding:1mm 3mm;border-radius:5px}
.wbtn{display:inline-block;background:#f6f8fa;color:#24292f;border:1px solid #d0d7de;padding:1mm 3mm;border-radius:5px}
.fld{display:inline-block;border:1px solid #8c959f;border-radius:4px;padding:.6mm 2.5mm;min-width:32mm;font-family:"DejaVu Sans Mono",monospace;background:#fff}
.menu{display:inline-block;border:1px solid #d0d7de;border-radius:6px;box-shadow:0 2px 6px rgba(0,0,0,.15);padding:1mm 0;background:#fff;color:#24292f;margin-top:1mm}
.menu div{padding:.8mm 4mm}
.tabs span{display:inline-block;padding:1mm 2.5mm;margin-right:1mm;color:#57606a}
.side div{padding:.8mm 2mm;color:#57606a}
.drop{border:2px dashed #8c959f;border-radius:6px;padding:3mm;text-align:center;color:#57606a;margin:1.5mm 0}
.file{display:inline-block;border:1px solid #d0d7de;border-radius:4px;padding:1mm 2.5mm;margin:.8mm;background:#f6f8fa;font-family:"DejaVu Sans Mono",monospace}
.live{background:#dafbe1;border:1px solid #4ac26b;border-radius:6px;padding:2mm 3mm}
.cap{font-size:8.6pt;color:#667;text-align:center;margin:0 0 2.5mm}
.two{display:flex;gap:4mm}.two>div{flex:1}
.prev{border:2px solid #9aa9b8;border-radius:7px;overflow:hidden;page-break-inside:avoid}
.prev .pg{background:lightblue;text-align:center;padding:3mm;font-family:Arial,sans-serif}
.prev h1{color:darkblue;font-size:15pt;margin:1mm 0}.prev .sotto{color:gray;margin:0 0 2mm;font-size:9pt}
.prev .sch{background:#fff;max-width:85mm;margin:0 auto;padding:2.5mm 4mm;border-radius:8px;text-align:left;font-size:8.6pt}
.prev h3{color:teal;font-size:10pt;margin:1mm 0}.prev ul{margin:0;padding-left:5mm}.prev p{margin:0 0 1mm}
.prev .piede{font-size:7pt;color:gray;margin-top:2mm}
.foot{margin-top:5mm;font-size:8.6pt;color:#778;border-top:1px solid #dde4ec;padding-top:1.5mm}
.chk td:first-child{width:8mm;text-align:center;font-size:12pt}
""" % {"f": FONTS}


def pagina(titolo, corpo):
    return ("<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><title>%s</title><style>%s</style></head>"
            "<body>%s</body></html>") % (E(titolo), CSS_PDF, corpo)


def cover(t_it, t_bn, sotto, bn):
    b = "<div class='bn'>%s</div>" % t_bn if bn else ""
    return ("<div class='cover'><span class='ver'>v%s</span><h1>%s</h1>%s<div class='s'>%s</div></div>"
            % (VER, t_it, b, sotto))


def bil(it, bn_txt, bn, tag="p"):
    """Una riga italiana + (se IT-BN) la stessa riga in bengali sotto."""
    s = "<%s>%s</%s>" % (tag, it, tag)
    if bn and bn_txt:
        s += "<%s class='bn'>%s</%s>" % (tag, bn_txt, tag)
    return s


def step(n, tit_it, tit_bn, it, bn_txt, bn, extra="", ok=False):
    t = tit_it + (" · <span class='bn' style='color:#fff;font-size:10.5pt'>%s</span>" % tit_bn if bn else "")
    return ("<div class='step%s'><div class='h'><span class='n'>%s</span>%s</div><div class='b'>%s%s</div></div>"
            % (" ok" if ok else "", n, t, bil(it, bn_txt, bn), extra))


def box(cls, it, bn_txt, bn):
    return "<div class='%s'>%s</div>" % (cls, bil(it, bn_txt, bn, "div"))


def T(x):
    return "<span class='tasto'>%s</span>" % x


def codice(titolo, testo, css=False):
    return ("<div style='page-break-inside:avoid'><div class='codet%s'>%s</div><pre>%s</pre></div>"
            % (" css" if css else "", titolo, E(testo)))


def anteprima():
    return ("<div class='prev'><div class='pg'><h1>Ciao, sono Leo</h1><p class='sotto'>Questo è il mio primo sito web.</p>"
            "<div class='sch'><h3>Chi sono</h3><p>Studio informatica e mi piace creare cose nuove.</p>"
            "<h3>Le mie passioni</h3><ul><li>Calcio</li><li>Videogiochi</li><li>Musica</li></ul>"
            "<h3>Il mio sogno</h3><p>Lavorare con i computer.</p></div><div class='piede'>Sito creato da me - 2026</div></div></div>")


# ================================================================ DISPENSA 1
def dispensa1(bn):
    c = cover("Dispensa 1 — La mia pagina web da zero",
              "ডিসপেন্সা ১ — শূন্য থেকে আমার ওয়েব পেজ",
              "Classe 3 · Informatica · %s · HTML + CSS in due file separati · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal",
             "<b>Cosa ottieni oggi:</b> una cartella <b>mio-sito</b> con <b>due file</b>: "
             "<b>index.html</b> (il <b>contenuto</b>: i testi) e <b>style.css</b> (l'<b>aspetto</b>: i colori). "
             "Doppio clic e la tua pagina si apre nel browser. Nella Dispensa 2 la mettiamo <b>su internet</b>.",
             "<b>আজ তুমি পাবে:</b> <b>mio-sito</b> নামের একটি ফোল্ডার, তাতে <b>দুটি ফাইল</b>: "
             "<b>index.html</b> (<b>বিষয়বস্তু</b>: লেখা) এবং <b>style.css</b> (<b>চেহারা</b>: রং)। "
             "ডাবল ক্লিক করলেই ব্রাউজারে পেজ খুলবে। ডিসপেন্সা ২-এ আমরা এটাকে <b>ইন্টারনেটে</b> দেব।", bn)
    c += "<div class='two'><div>" + anteprima() + "<div class='cap'>Ecco come sarà (poi la fai tua)</div></div><div>"
    c += ("<div class='scr'><div class='bar'>Desktop &gt; mio-sito</div><div class='in' style='text-align:center'>"
          "<span class='file'>index.html</span> <span class='file'>style.css</span><br><br>"
          "<span style='color:#12467a'>index.html = CONTENUTO</span><br><span style='color:#8a3ab9'>style.css = ASPETTO</span>"
          "</div></div><div class='cap'>La cartella: esattamente due file</div>")
    c += box("note", "<b>Carta e penna:</b> disegna sul quaderno la cartella <b>mio-sito</b> con dentro i due file. "
             "Fai una freccia da index.html a style.css e scrivici sopra <b>&lt;link&gt;</b>. Scrivi: <b>HTML = contenuto, CSS = aspetto</b>.",
             "<b>কাগজ-কলম:</b> খাতায় <b>mio-sito</b> ফোল্ডার আর তার ভিতরের দুটি ফাইল আঁকো। "
             "index.html থেকে style.css-এর দিকে একটি তীর আঁকো, উপরে লেখো <b>&lt;link&gt;</b>। লেখো: <b>HTML = বিষয়বস্তু, CSS = চেহারা</b>।", bn)
    c += "</div></div>"
    c += box("warn", "<b>Il tuo sito diventerà PUBBLICO</b> (lo vedrà chiunque su internet). Quindi scrivi <b>solo il nome o un soprannome</b>. "
             "<b>MAI</b> cognome, telefono, email, indirizzo, foto del viso.",
             "<b>তোমার সাইট সবার জন্য খোলা হবে</b> (ইন্টারনেটে যে কেউ দেখবে)। তাই শুধু <b>নাম বা ডাকনাম</b> লেখো। "
             "<b>কখনো না:</b> পদবি, ফোন, ইমেল, ঠিকানা, মুখের ছবি।", bn)

    c += "<h2>1. Il codice (uguale per tutti — poi lo fai tuo)</h2>"
    c += box("info", "<b>Il modo più sicuro per copiare:</b> apri la pagina del corso (il link è nel compito su Classroom) e premi il bottone "
             "<b>Copia</b> sopra il codice. Poi nel Blocco note premi " + T("Ctrl") + " + " + T("V") + ". Copiare dal PDF a volte rovina gli spazi.",
             "<b>কপি করার সবচেয়ে নিরাপদ উপায়:</b> কোর্সের পেজ খোলো (লিংকটি Classroom-এর কাজে আছে) এবং কোডের উপরের "
             "<b>Copia</b> (কপি) বোতাম চাপো। তারপর Notepad-এ " + T("Ctrl") + " + " + T("V") + " চাপো। PDF থেকে কপি করলে কখনো কখনো ফাঁকা জায়গা নষ্ট হয়।", bn)
    c += codice("RIQUADRO 1 — file index.html (il contenuto)", HTML_CODE)
    c += codice("RIQUADRO 2 — file style.css (l'aspetto)", CSS_CODE, css=True)

    c += "<h2>2. I passi, uno alla volta</h2>"
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Crea la cartella", "ফোল্ডার বানাও",
           "Sul <b>Desktop</b>, in un punto vuoto: clic con il tasto <b>DESTRO</b> del mouse &rarr; <b>Nuovo</b> &rarr; <b>Cartella</b>. "
           "Scrivi il nome " + T("mio-sito") + " e premi " + T("Invio") + ".",
           "<b>Desktop</b>-এর খালি জায়গায় মাউসের <b>ডান</b> বোতামে ক্লিক করো &rarr; <b>Nuovo</b> (নতুন) &rarr; <b>Cartella</b> (ফোল্ডার)। "
           "নাম লেখো " + T("mio-sito") + " এবং " + T("Invio") + " (Enter) চাপো।")
    c += S("Fai vedere la fine dei nomi (consigliato)", "ফাইলের নামের শেষ অংশ দেখাও",
           "Apri la cartella <b>mio-sito</b>. In alto clic su <b>Visualizza</b> &rarr; <b>Mostra</b> &rarr; <b>Estensioni nomi file</b> (compare la spunta). "
           "Così vedi se un file finisce con <b>.html</b> o, per errore, con <b>.txt</b>.",
           "<b>mio-sito</b> ফোল্ডার খোলো। উপরে <b>Visualizza</b> (View) &rarr; <b>Mostra</b> (Show) &rarr; <b>Estensioni nomi file</b> (File name extensions)-এ ক্লিক করো (টিক চিহ্ন আসবে)। "
           "এতে দেখবে ফাইলের নাম <b>.html</b> দিয়ে শেষ, নাকি ভুল করে <b>.txt</b> দিয়ে।")
    c += S("Apri il Blocco note", "Notepad খোলো",
           "In basso a sinistra clic su <b>Start</b>, scrivi " + T("Blocco note") + " e clicca sul programma <b>Blocco note</b>.",
           "নিচে বাঁদিকে <b>Start</b>-এ ক্লিক করো, লেখো " + T("Blocco note") + " (Notepad) এবং প্রোগ্রামটিতে ক্লিক করো।")
    c += S("Incolla il codice HTML", "HTML কোড পেস্ট করো",
           "Copia <b>tutto</b> il <b>RIQUADRO 1</b> e incollalo nel Blocco note (" + T("Ctrl") + " + " + T("V") + ").",
           "<b>বাক্স ১</b>-এর <b>পুরো</b> কোড কপি করে Notepad-এ পেস্ট করো (" + T("Ctrl") + " + " + T("V") + ")।")
    c += S("Fallo tuo", "নিজের মতো করো",
           "Cambia <b>Leo</b> con il tuo nome o un soprannome. Cambia <b>Chi sono</b>, <b>le passioni</b> e <b>il sogno</b> con cose tue. "
           "Non toccare le parole tra &lt; e &gt;: cambia solo il testo in mezzo.",
           "<b>Leo</b>-র জায়গায় তোমার নাম বা ডাকনাম লেখো। <b>Chi sono</b> (আমি কে), <b>শখ</b> আর <b>স্বপ্ন</b> নিজের মতো বদলাও। "
           "&lt; আর &gt;-এর ভিতরের শব্দ বদলাবে না: শুধু মাঝের লেখা বদলাও।")
    dlg = lambda nome: ("<div class='scr'><div class='bar'>Salva con nome</div><div class='in'>"
                        "<div>Cartella: <b>Desktop &gt; mio-sito</b></div>"
                        "<div style='margin-top:1mm'>Nome file: <span class='fld hl'>%s</span></div>"
                        "<div style='margin-top:1mm'>Salva come: <span class='fld hl'>Tutti i file (*.*)</span></div>"
                        "<div style='margin-top:1mm'>Codifica: <span class='fld hl'>UTF-8</span> &nbsp; <span class='wbtn'>Salva</span></div>"
                        "</div></div>") % nome
    c += S("Salva come index.html", "index.html নামে সেভ করো",
           "In alto a sinistra <b>File</b> &rarr; <b>Salva con nome</b>. A sinistra scegli <b>Desktop</b> e apri <b>mio-sito</b>. "
           "In basso: <b>Salva come</b> &rarr; <b>Tutti i file</b>; <b>Nome file</b>: " + T("index.html") + "; <b>Codifica</b>: <b>UTF-8</b>. Clic su <b>Salva</b>.",
           "উপরে বাঁদিকে <b>File</b> &rarr; <b>Salva con nome</b> (Save as)। বাঁদিকে <b>Desktop</b> বেছে <b>mio-sito</b> খোলো। "
           "নিচে: <b>Salva come</b> (Save as type) &rarr; <b>Tutti i file</b> (All files); নাম: " + T("index.html") + "; <b>Codifica</b> (Encoding): <b>UTF-8</b>। <b>Salva</b> (Save) চাপো।",
           extra=dlg("index.html"))
    c += S("Un foglio nuovo per il CSS", "CSS-এর জন্য নতুন পাতা",
           "Nel Blocco note: <b>File</b> &rarr; <b>Nuovo</b> (si apre un foglio vuoto). Copia <b>tutto</b> il <b>RIQUADRO 2</b> e incollalo.",
           "Notepad-এ: <b>File</b> &rarr; <b>Nuovo</b> (New) (খালি পাতা খুলবে)। <b>বাক্স ২</b>-এর <b>পুরো</b> কোড কপি করে পেস্ট করো।")
    c += S("Salva come style.css", "style.css নামে সেভ করো",
           "Come prima: <b>File</b> &rarr; <b>Salva con nome</b>, <b>stessa cartella mio-sito</b>, <b>Tutti i file</b>, nome " + T("style.css") + ", <b>UTF-8</b>, <b>Salva</b>.",
           "আগের মতো: <b>File</b> &rarr; <b>Salva con nome</b>, <b>একই mio-sito ফোল্ডার</b>, <b>Tutti i file</b>, নাম " + T("style.css") + ", <b>UTF-8</b>, <b>Salva</b>।")
    c += S("Controlla la cartella", "ফোল্ডার মিলিয়ে দেখো",
           "Dentro <b>mio-sito</b> ci devono essere <b>due file</b>: " + T("index.html") + " e " + T("style.css") +
           ". Nomi tutti <b>minuscoli</b>, senza spazi, senza <b>.txt</b> alla fine.",
           "<b>mio-sito</b>-র ভিতরে <b>দুটি ফাইল</b> থাকতে হবে: " + T("index.html") + " এবং " + T("style.css") +
           "। সব <b>ছোট হাতের</b> অক্ষর, কোনো ফাঁকা নেই, শেষে <b>.txt</b> নেই।")
    c += S("Apri la tua pagina", "তোমার পেজ খোলো",
           "Doppio clic su <b>index.html</b>: si apre nel browser, <b>con i colori</b>. <b>FATTO! Hai creato la tua pagina web.</b>",
           "<b>index.html</b>-এ ডাবল ক্লিক করো: ব্রাউজারে <b>রঙসহ</b> খুলবে। <b>হয়ে গেছে! তুমি নিজের ওয়েব পেজ বানিয়েছ।</b>", ok=True)
    tab = ("<table><tr><th>Colore</th><th>Scrivi</th><th>Colore</th><th>Scrivi</th><th>Colore</th><th>Scrivi</th></tr>")
    col = ["pink", "lightgreen", "gold", "orange", "lavender", "coral", "khaki", "turquoise", "salmon"]
    for i in range(0, 9, 3):
        tab += "<tr>" + "".join("<td><span class='sw' style='background:%s'></span></td><td class='c'>%s</td>" % (k, k) for k in col[i:i + 3]) + "</tr>"
    tab += "</table>"
    c += S("Cambia i colori (il CSS)", "রং বদলাও (CSS)",
           "Clic <b>destro</b> su <b>style.css</b> &rarr; <b>Apri con</b> &rarr; <b>Blocco note</b>. Cambia " + T("lightblue") +
           " con un colore che ti piace. Salva (" + T("Ctrl") + " + " + T("S") + ") e nel browser premi " + T("F5") + ": il colore cambia!",
           "<b>style.css</b>-এ <b>ডান</b> ক্লিক &rarr; <b>Apri con</b> (Open with) &rarr; <b>Blocco note</b>। " + T("lightblue") +
           " বদলে তোমার পছন্দের রং লেখো। সেভ করো (" + T("Ctrl") + " + " + T("S") + ") এবং ব্রাউজারে " + T("F5") + " চাপো: রং বদলে যাবে!",
           extra=tab)

    c += "<h2>3. Cosa fa ogni pezzo</h2>"
    rows = [("&lt;head&gt; ... &lt;/head&gt;", "istruzioni per il browser (non si vedono)", "ব্রাউজারের জন্য নির্দেশ (দেখা যায় না)"),
            ("&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;", "<b>collega</b> l'HTML al file style.css", "HTML-কে style.css ফাইলের সাথে <b>যুক্ত</b> করে"),
            ("&lt;body&gt; ... &lt;/body&gt;", "tutto quello che si vede nella pagina", "পেজে যা দেখা যায় সব"),
            ("&lt;h1&gt; &lt;h2&gt;", "titolo grande, titolo più piccolo", "বড় শিরোনাম, ছোট শিরোনাম"),
            ("&lt;p&gt;", "un paragrafo di testo", "এক অনুচ্ছেদ লেখা"),
            ("&lt;ul&gt; &lt;li&gt;", "un elenco e le sue voci", "একটি তালিকা ও তার আইটেম"),
            ("&lt;div class=\"scheda\"&gt;", "una scatola; il nome <b>scheda</b> lo usa il CSS", "একটি বাক্স; <b>scheda</b> নামটি CSS ব্যবহার করে"),
            (".scheda { background: white; }", "CSS: <b>chi</b> { <b>proprietà</b>: <b>valore</b>; }", "CSS: <b>কে</b> { <b>বৈশিষ্ট্য</b>: <b>মান</b>; }")]
    t = "<table><tr><th>Pezzo di codice</th><th>Cosa fa</th>%s</tr>" % ("<th class='bn'>কী করে</th>" if bn else "")
    for a, b, d in rows:
        t += "<tr><td class='c'>%s</td><td>%s</td>%s</tr>" % (a, b, "<td class='bn'>%s</td>" % d if bn else "")
    c += t + "</table>"

    c += "<h2>4. Se qualcosa non va (succede a tutti, anche ai professionisti)</h2>"
    err = [("Vedo il <b>codice</b> invece della pagina", "Il file è stato salvato come <b>.txt</b>: risalva con <b>Tutti i file</b>.",
            "<b>কোড</b> দেখা যাচ্ছে, পেজ নয়", "ফাইলটি <b>.txt</b> হয়ে গেছে: <b>Tutti i file</b> বেছে আবার সেভ করো।"),
           ("La pagina è <b>senza colori</b>", "style.css non è nella stessa cartella, o ha un nome diverso (es. <b>Style.css</b>, <b>stile.css</b>, <b>style.css.txt</b>).",
            "পেজে <b>রং নেই</b>", "style.css একই ফোল্ডারে নেই, বা নাম আলাদা (যেমন <b>Style.css</b>, <b>stile.css</b>, <b>style.css.txt</b>)।"),
           ("Al posto di <b>è</b> vedo simboli strani", "Risalva index.html scegliendo <b>Codifica: UTF-8</b>.",
            "<b>è</b>-এর জায়গায় অদ্ভুত চিহ্ন", "<b>Codifica: UTF-8</b> বেছে index.html আবার সেভ করো।"),
           ("Ho cambiato ma non vedo niente", "Hai salvato? (" + T("Ctrl") + "+" + T("S") + ") Poi nel browser " + T("F5") + ".",
            "বদলেছি কিন্তু কিছু দেখছি না", "সেভ করেছ? (" + T("Ctrl") + "+" + T("S") + ") তারপর ব্রাউজারে " + T("F5") + "।")]
    t = "<table><tr><th style='width:34%'>Problema</th><th>Soluzione</th></tr>"
    for a, b, a2, b2 in err:
        t += "<tr><td>%s%s</td><td>%s%s</td></tr>" % (a, "<div class='bn'>%s</div>" % a2 if bn else "", b, "<div class='bn'>%s</div>" % b2 if bn else "")
    c += t + "</table>"
    c += box("note", "<b>Hai già fatto la pagina del 30/09?</b> Benissimo: puoi riusare i tuoi testi. Ma per il sito servono <b>questi nomi esatti</b>: "
             "<b>index.html</b> e <b>style.css</b>, e nel &lt;link&gt; deve esserci <b>style.css</b>.",
             "<b>৩০/০৯-এর পেজ আগেই বানিয়েছ?</b> খুব ভালো: তোমার লেখা আবার ব্যবহার করতে পারো। কিন্তু সাইটের জন্য <b>ঠিক এই নাম</b> লাগবে: "
             "<b>index.html</b> এবং <b>style.css</b>, আর &lt;link&gt;-এ থাকতে হবে <b>style.css</b>।", bn)
    c += box("goal", "<b>Prossimo passo:</b> Dispensa 2 — mettiamo il tuo sito <b>su internet</b>, con un indirizzo da aprire anche sul telefono.",
             "<b>পরের ধাপ:</b> ডিসপেন্সা ২ — তোমার সাইট <b>ইন্টারনেটে</b> দেব, একটি ঠিকানা সহ যা ফোনেও খোলা যাবে।", bn)
    c += "<div class='foot'>Classe 3 · Dispensa 1 · v%s · Tutti i dati negli esempi sono inventati.</div>" % VER
    return pagina("Dispensa 1 — La mia pagina web da zero", c)


# ================================================================ DISPENSA 2
def dispensa2(bn):
    c = cover("Dispensa 2 — Pubblica il tuo primo sito su GitHub",
              "ডিসপেন্সা ২ — GitHub-এ তোমার প্রথম সাইট প্রকাশ করো",
              "Classe 3 · Informatica · %s · GitHub Pages, tutto dal browser · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa ottieni:</b> un <b>indirizzo internet vero</b>, come " + T("https://tuonome.github.io/mio-sito/") +
             ", che chiunque può aprire, <b>anche sul telefono</b>. È il tuo primo sito pubblico.",
             "<b>তুমি পাবে:</b> একটি <b>সত্যিকারের ইন্টারনেট ঠিকানা</b>, যেমন " + T("https://tuonome.github.io/mio-sito/") +
             ", যা যে কেউ খুলতে পারবে, <b>ফোনেও</b>। এটা তোমার প্রথম পাবলিক সাইট।", bn)
    c += box("info", "<b>Prima di iniziare ti serve:</b> 1) la cartella <b>mio-sito</b> con <b>index.html</b> e <b>style.css</b> (Dispensa 1); "
             "2) il tuo account <b>GitHub</b> (nome utente e password).<br>"
             "<b>Parole nuove:</b> <b>repository</b> = la cartella del progetto su GitHub · <b>commit</b> = salvare una versione · "
             "<b>upload</b> = caricare · <b>GitHub Pages</b> = il servizio gratis che trasforma il repository in un sito.",
             "<b>শুরু করার আগে লাগবে:</b> ১) <b>index.html</b> ও <b>style.css</b> সহ <b>mio-sito</b> ফোল্ডার (ডিসপেন্সা ১); "
             "২) তোমার <b>GitHub</b> অ্যাকাউন্ট (ইউজারনেম ও পাসওয়ার্ড)।<br>"
             "<b>নতুন শব্দ:</b> <b>repository</b> = GitHub-এ প্রজেক্টের ফোল্ডার · <b>commit</b> = একটি সংস্করণ সেভ করা · "
             "<b>upload</b> = আপলোড করা · <b>GitHub Pages</b> = ফ্রি সেবা যা repository-কে সাইট বানায়।", bn)
    c += box("warn", "<b>Controllo privacy PRIMA di caricare:</b> apri index.html e verifica: <b>niente cognome, telefono, email, indirizzo, foto del viso</b>. "
             "Quello che carichi lo vede il mondo intero.",
             "<b>আপলোডের আগে গোপনীয়তা যাচাই:</b> index.html খুলে দেখো: <b>পদবি, ফোন, ইমেল, ঠিকানা, মুখের ছবি নেই</b>। "
             "যা আপলোড করবে, সারা পৃথিবী দেখবে।", bn)
    c += box("note", "<b>Se la pagina di GitHub è tradotta</b> (in italiano o nella tua lingua) i nomi dei bottoni cambiano: "
             "cerca il bottone per <b>posizione e colore</b>, come nei disegni (il cerchio <b style='color:#e0312b'>rosso</b> indica dove cliccare).",
             "<b>GitHub-এর পেজ অনুবাদ করা থাকলে</b> (ইতালিয়ান বা তোমার ভাষায়) বোতামের নাম বদলে যায়: "
             "ছবির মতো <b>জায়গা আর রং</b> দেখে বোতাম খোঁজো (<b style='color:#e0312b'>লাল</b> দাগ দেখায় কোথায় ক্লিক করতে হবে)।", bn)

    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += "<h2>1. Crea il repository</h2>"
    c += S("Entra su GitHub", "GitHub-এ ঢোকো",
           "Apri il browser e vai all'indirizzo " + T("github.com") + ". In alto a destra <b>Sign in</b> (Accedi): scrivi nome utente e password.",
           "ব্রাউজার খুলে এই ঠিকানায় যাও (ঠিক এভাবে লেখো): " + T("github.com") + "। উপরে ডানদিকে <b>Sign in</b> (ঢোকো): ইউজারনেম ও পাসওয়ার্ড লেখো।")
    c += S("Nuovo repository", "নতুন repository",
           "In alto a destra clic sul <b>+</b> &rarr; <b>New repository</b> (Nuovo repository).",
           "উপরে ডানদিকে <b>+</b> চিহ্নে ক্লিক করো &rarr; <b>New repository</b> (নতুন repository)।",
           extra="<div class='scr'><div class='bar'>github.com</div><div class='gh'><span>GitHub</span><span><span class='hl' style='padding:0 2mm'>+ &#9662;</span> <span class='fr'>&larr; 1</span></span></div>"
                 "<div class='in' style='text-align:right'><div class='menu' style='text-align:left'><div class='hl'>New repository <span class='fr'>&larr; 2</span></div><div>Import repository</div><div>New organization</div></div></div></div>")
    c += S("Dai il nome e crea", "নাম দাও ও বানাও",
           "In <b>Repository name</b> scrivi " + T("mio-sito") + ". Lascia <b>Public</b> (Pubblico). Metti <b>Add README</b> su <b>On</b> (o spunta la casella). "
           "In basso a destra clic sul bottone <b>verde</b> <b>Create repository</b>.",
           "<b>Repository name</b>-এ লেখো " + T("mio-sito") + "। <b>Public</b> (পাবলিক) রেখে দাও। <b>Add README</b> <b>On</b> করো (বা বাক্সে টিক দাও)। "
           "নিচে ডানদিকে <b>সবুজ</b> বোতাম <b>Create repository</b>-এ ক্লিক করো।",
           extra="<div class='scr'><div class='bar'>github.com/new</div><div class='in'>"
                 "<div>Repository name: <span class='fld hl'>mio-sito</span></div>"
                 "<div style='margin-top:1.5mm'>&#9673; <b>Public</b> &nbsp; &#9675; Private</div>"
                 "<div style='margin-top:1.5mm'>Add README: <span class='hl' style='padding:0 2mm;background:#1f883d;color:#fff;border-radius:8px'>On</span></div>"
                 "<div style='text-align:right;margin-top:1.5mm'><span class='gbtn hl'>Create repository</span></div></div></div>")

    c += "<h2>2. Carica i tuoi due file</h2>"
    c += S("Add file &rarr; Upload files", "Add file &rarr; Upload files",
           "Nella pagina del repository clic su <b>Add file</b> (bottone <b>grigio</b>, a sinistra del bottone verde <b>Code</b>) &rarr; <b>Upload files</b> (Carica file).",
           "repository-র পেজে <b>Add file</b>-এ ক্লিক করো (<b>ধূসর</b> বোতাম, সবুজ <b>Code</b> বোতামের বাঁদিকে) &rarr; <b>Upload files</b> (ফাইল আপলোড)।",
           extra="<div class='scr'><div class='bar'>github.com/tuonome/mio-sito</div><div class='in'><b>tuonome / mio-sito</b> &nbsp; <i>Public</i>"
                 "<div style='text-align:right;margin-top:1.5mm'><span class='wbtn'>Go to file</span> <span class='wbtn hl'>Add file &#9662;</span> <span class='gbtn'>&lt;&gt; Code &#9662;</span></div>"
                 "<div style='text-align:right'><div class='menu' style='text-align:left;margin-right:20mm'><div>Create new file</div><div class='hl'>Upload files <span class='fr'>&larr;</span></div></div></div></div></div>")
    c += S("Trascina i file", "ফাইল টেনে আনো",
           "Apri <b>Esplora file</b> &rarr; <b>Desktop</b> &rarr; <b>mio-sito</b>. Seleziona i due file (" + T("Ctrl") + " + " + T("A") +
           ") e <b>trascinali</b> nel riquadro tratteggiato della pagina. (Oppure clic su <b>choose your files</b> e scegli i due file.)",
           "<b>Esplora file</b> (File Explorer) খোলো &rarr; <b>Desktop</b> &rarr; <b>mio-sito</b>। দুটি ফাইল বেছে নাও (" + T("Ctrl") + " + " + T("A") +
           ") এবং পেজের ডট-দাগের বাক্সে <b>টেনে আনো</b>। (অথবা <b>choose your files</b>-এ ক্লিক করে দুটি ফাইল বেছে নাও।)",
           extra="<div class='scr'><div class='bar'>github.com/tuonome/mio-sito/upload/main</div><div class='in'>"
                 "<div class='drop hl'>Drag files here to add them to your repository<br>or <u>choose your files</u></div>"
                 "<span class='file'>index.html</span> <span class='file'>style.css</span></div></div>")
    c += S("Salva su GitHub: il commit", "GitHub-এ সেভ: commit",
           "Controlla che si vedano <b>index.html</b> e <b>style.css</b>. In basso clic sul bottone <b>verde</b> <b>Commit changes</b>. "
           "Hai fatto un <b>commit</b>: hai salvato una versione, come abbiamo visto con Git.",
           "দেখো <b>index.html</b> ও <b>style.css</b> দেখা যাচ্ছে কিনা। নিচে <b>সবুজ</b> বোতাম <b>Commit changes</b>-এ ক্লিক করো। "
           "তুমি একটি <b>commit</b> করলে: একটি সংস্করণ সেভ করলে, যেমন Git-এ দেখেছি।",
           extra="<div class='scr'><div class='in'>Commit changes<div class='fld' style='min-width:70mm;color:#888'>Add files via upload</div>"
                 "<div style='margin-top:1.5mm'><span class='gbtn hl'>Commit changes</span> <span class='fr'>&larr;</span></div></div></div>")

    c += "<h2>3. Accendi il sito (GitHub Pages)</h2>"
    c += S("Settings", "Settings",
           "In alto, nella fila di schede del repository, clic sull'<b>ultima a destra</b>: <b>Settings</b> (Impostazioni, con l'<b>ingranaggio</b> &#9881;).",
           "উপরে repository-র ট্যাবের সারিতে <b>একদম ডানদিকের</b> ট্যাবে ক্লিক করো: <b>Settings</b> (সেটিংস, <b>গিয়ার</b> &#9881; চিহ্ন)।",
           extra="<div class='scr'><div class='in tabs'><span><b>&lt;&gt; Code</b></span><span>Issues</span><span>Pull requests</span><span>Actions</span>"
                 "<span>Projects</span><span>Security</span><span class='hl' style='color:#24292f'>&#9881; Settings</span> <span class='fr'>&larr;</span></div></div>")
    c += S("Pages", "Pages",
           "Nel <b>menu a sinistra</b> scendi un po' e clic su <b>Pages</b>.",
           "<b>বাঁদিকের মেনুতে</b> একটু নিচে নেমে <b>Pages</b>-এ ক্লিক করো।")
    c += S("Scegli main e salva", "main বেছে সেভ করো",
           "Sotto <b>Build and deployment</b>: <b>Source</b> = <b>Deploy from a branch</b>. In <b>Branch</b> clic su <b>None</b> e scegli <b>main</b>; "
           "accanto lascia <b>/ (root)</b>. Clic su <b>Save</b> (Salva).",
           "<b>Build and deployment</b>-এর নিচে: <b>Source</b> = <b>Deploy from a branch</b>। <b>Branch</b>-এ <b>None</b>-এ ক্লিক করে <b>main</b> বেছে নাও; "
           "পাশে <b>/ (root)</b> রেখে দাও। <b>Save</b> (সেভ)-এ ক্লিক করো।",
           extra="<div class='scr'><div class='in' style='display:flex;gap:4mm'><div class='side' style='width:30mm;border-right:1px solid #d0d7de'>"
                 "<div>General</div><div>Collaborators</div><div>Branches</div><div>Actions</div><div class='hl' style='color:#24292f;font-weight:bold'>Pages</div></div>"
                 "<div><b>Build and deployment</b><div style='margin-top:1mm'>Source: <span class='wbtn'>Deploy from a branch &#9662;</span></div>"
                 "<div style='margin-top:1.5mm'>Branch: <span class='wbtn hl'>main &#9662;</span> <span class='wbtn'>/ (root) &#9662;</span> <span class='wbtn hl'>Save</span></div></div></div></div>")
    c += S("Aspetta 1-2 minuti", "১-২ মিনিট অপেক্ষা করো",
           "Premi " + T("F5") + " ogni tanto. In alto compare <b>Your site is live at ...</b> (Il tuo sito è online) con il bottone <b>Visit site</b>. "
           "Cliccalo: <b>FATTO! Il tuo sito è su internet.</b>",
           "মাঝে মাঝে " + T("F5") + " চাপো। উপরে আসবে <b>Your site is live at ...</b> (তোমার সাইট অনলাইন) আর <b>Visit site</b> বোতাম। "
           "ক্লিক করো: <b>হয়ে গেছে! তোমার সাইট ইন্টারনেটে।</b>",
           extra="<div class='scr'><div class='in'><div class='live'>Your site is live at <b>https://tuonome.github.io/mio-sito/</b> &nbsp; <span class='wbtn hl'>Visit site</span></div></div></div>",
           ok=True)
    c += S("Mostralo", "দেখাও",
           "L'indirizzo è " + T("https://TUONOME.github.io/mio-sito/") + " (TUONOME = il tuo nome utente GitHub). "
           "Aprilo sul <b>telefono</b> e fallo vedere a un compagno. L'hai fatto tu!",
           "ঠিকানা হলো " + T("https://TUONOME.github.io/mio-sito/") + " (TUONOME = তোমার GitHub ইউজারনেম)। "
           "<b>ফোনে</b> খোলো আর একজন সহপাঠীকে দেখাও। তুমি নিজে বানিয়েছ!", ok=True)

    c += "<h2>4. Se qualcosa non va</h2>"
    err = [("Vedo <b>404</b> / <b>There isn't a GitHub Pages site here</b>",
            "Aspetta ancora 2 minuti e premi F5. Controlla che il file si chiami proprio <b>index.html</b> (minuscolo) e che in Pages ci sia <b>main</b> salvato.",
            "<b>404</b> দেখাচ্ছে", "আরও ২ মিনিট অপেক্ষা করে F5 চাপো। দেখো ফাইলের নাম ঠিক <b>index.html</b> (ছোট হাতের) এবং Pages-এ <b>main</b> সেভ আছে কিনা।"),
           ("Il sito si vede ma <b>senza colori</b>", "Nel repository manca <b>style.css</b>, o ha un nome diverso. Ricaricalo con <b>Add file &rarr; Upload files</b>.",
            "সাইট দেখা যায় কিন্তু <b>রং নেই</b>", "repository-তে <b>style.css</b> নেই, বা নাম আলাদা। <b>Add file &rarr; Upload files</b> দিয়ে আবার আপলোড করো।"),
           ("Non trovo un bottone", "Guarda il disegno: posizione e colore. Poi alza la mano: ti aiuto io.",
            "বোতাম খুঁজে পাচ্ছি না", "ছবি দেখো: জায়গা আর রং। তারপর হাত তোলো: আমি সাহায্য করব।")]
    t = "<table><tr><th style='width:34%'>Problema</th><th>Soluzione</th></tr>"
    for a, b, a2, b2 in err:
        t += "<tr><td>%s%s</td><td>%s%s</td></tr>" % (a, "<div class='bn'>%s</div>" % a2 if bn else "", b, "<div class='bn'>%s</div>" % b2 if bn else "")
    c += t + "</table>"
    c += box("info", "<b>Vuoi cambiare il sito dopo?</b> Nel repository clic sul file (es. <b>style.css</b>) &rarr; la <b>matita</b> &#9998; in alto a destra &rarr; "
             "cambia &rarr; bottone verde <b>Commit changes</b>. Dopo un minuto, " + T("F5") + " sul sito: è aggiornato. Ogni modifica è una <b>nuova versione</b>.",
             "<b>পরে সাইট বদলাতে চাও?</b> repository-তে ফাইলে ক্লিক করো (যেমন <b>style.css</b>) &rarr; উপরে ডানদিকে <b>পেনসিল</b> &#9998; &rarr; "
             "বদলাও &rarr; সবুজ বোতাম <b>Commit changes</b>। এক মিনিট পরে সাইটে " + T("F5") + ": আপডেট হয়ে গেছে। প্রতিটি পরিবর্তন একটি <b>নতুন সংস্করণ</b>।", bn)
    c += box("note", "<b>Carta e penna:</b> scrivi sul quaderno il tuo indirizzo <b>github.io</b> e lo schema: "
             "<b>PC</b> (cartella mio-sito) &rarr; <b>upload + commit</b> &rarr; <b>GitHub</b> (repository) &rarr; <b>Pages</b> &rarr; <b>sito pubblico</b>.",
             "<b>কাগজ-কলম:</b> খাতায় তোমার <b>github.io</b> ঠিকানা আর এই ছক লেখো: "
             "<b>PC</b> (mio-sito ফোল্ডার) &rarr; <b>upload + commit</b> &rarr; <b>GitHub</b> (repository) &rarr; <b>Pages</b> &rarr; <b>পাবলিক সাইট</b>।", bn)
    c += "<div class='foot'>Classe 3 · Dispensa 2 · v%s · Se GitHub cambia l'aspetto delle pagine, i passi restano gli stessi.</div>" % VER
    return pagina("Dispensa 2 — Pubblica il tuo primo sito su GitHub", c)


# ================================================================ COMPITO
def compito(bn):
    c = cover("Compito — Il mio primo sito pubblico",
              "কাজ — আমার প্রথম পাবলিক সাইট",
              "Classe 3 · Informatica · %s · si consegna su Classroom · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa consegni:</b> il <b>Documento</b> che trovi già pronto nel compito su Classroom (c'è già il tuo nome), "
             "con <b>5 parti separate</b>. HTML e CSS <b>NON</b> vanno insieme: ognuno nella sua parte.",
             "<b>কী জমা দেবে:</b> Classroom-এর কাজে আগে থেকে তৈরি <b>Documento</b> (তোমার নাম সহ), "
             "<b>৫টি আলাদা অংশ</b> নিয়ে। HTML আর CSS <b>একসাথে নয়</b>: প্রতিটি নিজের অংশে।", bn)
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Apri il Documento", "Documento খোলো",
           "Su <b>Classroom</b> apri il compito <b>Il mio primo sito pubblico</b>. Clic sul Documento con il <b>tuo nome</b>: si apre.",
           "<b>Classroom</b>-এ <b>Il mio primo sito pubblico</b> কাজটি খোলো। <b>তোমার নামের</b> Documento-তে ক্লিক করো: খুলে যাবে।")
    c += S("Parte 1 — Il link", "অংশ ১ — লিংক",
           "Apri il tuo sito pubblicato, clic sulla <b>barra dell'indirizzo</b> in alto, " + T("Ctrl") + " + " + T("C") +
           ". Nel Documento, sotto <b>1. Il link</b>, " + T("Ctrl") + " + " + T("V") + ". Deve contenere <b>github.io</b>.",
           "তোমার প্রকাশিত সাইট খোলো, উপরের <b>ঠিকানার বারে</b> ক্লিক করো, " + T("Ctrl") + " + " + T("C") +
           "। Documento-তে <b>1. Il link</b>-এর নিচে " + T("Ctrl") + " + " + T("V") + "। এতে <b>github.io</b> থাকতে হবে।")
    c += S("Parte 2 — Tutto l'HTML", "অংশ ২ — পুরো HTML",
           "Clic <b>destro</b> su <b>index.html</b> &rarr; <b>Apri con</b> &rarr; <b>Blocco note</b>. " + T("Ctrl") + " + " + T("A") + " (seleziona tutto), " +
           T("Ctrl") + " + " + T("C") + ". Nel Documento, sotto <b>2. Codice HTML</b>, " + T("Ctrl") + " + " + T("V") + ".",
           "<b>index.html</b>-এ <b>ডান</b> ক্লিক &rarr; <b>Apri con</b> &rarr; <b>Blocco note</b>। " + T("Ctrl") + " + " + T("A") + " (সব বাছাই), " +
           T("Ctrl") + " + " + T("C") + "। Documento-তে <b>2. Codice HTML</b>-এর নিচে " + T("Ctrl") + " + " + T("V") + "।")
    c += S("Parte 3 — Tutto il CSS, a parte", "অংশ ৩ — পুরো CSS, আলাদা করে",
           "Stessa cosa con <b>style.css</b>: lo incolli sotto <b>3. Codice CSS</b>. <b>Non</b> mischiarlo con l'HTML.",
           "<b>style.css</b> দিয়ে একই কাজ: <b>3. Codice CSS</b>-এর নিচে পেস্ট করো। HTML-এর সাথে <b>মেশাবে না</b>।")
    c += S("Parte 4 — Lo screenshot", "অংশ ৪ — স্ক্রিনশট",
           "Apri il sito <b>pubblicato</b> (quello con github.io). Premi " + T("Win") + " + " + T("Shift") + " + " + T("S") +
           " e seleziona la finestra <b>con anche la barra dell'indirizzo</b>. Nel Documento, sotto <b>4. Screenshot</b>, " + T("Ctrl") + " + " + T("V") + ".",
           "<b>প্রকাশিত</b> সাইট খোলো (github.io যুক্ত)। " + T("Win") + " + " + T("Shift") + " + " + T("S") +
           " চাপো এবং <b>ঠিকানার বার সহ</b> জানালাটি বেছে নাও। Documento-তে <b>4. Screenshot</b>-এর নিচে " + T("Ctrl") + " + " + T("V") + "।")
    c += S("Parte 5 — Spiegalo con parole tue", "অংশ ৫ — নিজের ভাষায় বোঝাও",
           "Rispondi con 1-2 frasi: a) a cosa serve il file style.css? b) cosa NON sono riuscito a fare e perché? c) cosa NON ho capito?",
           "১-২ বাক্যে উত্তর দাও: ক) style.css ফাইল কী কাজে লাগে? খ) কী করতে পারিনি ও কেন? গ) কী বুঝিনি?")
    c += S("Consegna", "জমা দাও",
           "Torna sul compito in Classroom e clic sul bottone <b>blu</b> <b>Consegna</b> (a destra).",
           "Classroom-এর কাজে ফিরে ডানদিকের <b>নীল</b> বোতাম <b>Consegna</b> (জমা দাও)-এ ক্লিক করো।", ok=True)
    c += "<h2>Controlla prima di consegnare</h2>"
    chk = [("Il link si apre e contiene <b>github.io</b>", "লিংক খোলে এবং তাতে <b>github.io</b> আছে"),
           ("L'HTML è <b>tutto</b>: dalla prima riga &lt;!DOCTYPE html&gt; all'ultima &lt;/html&gt;", "HTML <b>পুরোটা</b>: প্রথম লাইন &lt;!DOCTYPE html&gt; থেকে শেষ &lt;/html&gt; পর্যন্ত"),
           ("Il CSS è in una <b>parte separata</b>", "CSS একটি <b>আলাদা অংশে</b>"),
           ("Lo screenshot mostra la <b>barra dell'indirizzo</b>", "স্ক্রিনশটে <b>ঠিকানার বার</b> দেখা যায়"),
           ("Sul sito <b>niente cognome, telefono, email</b>", "সাইটে <b>পদবি, ফোন, ইমেল নেই</b>"),
           ("Ho risposto alle 3 domande della parte 5", "অংশ ৫-এর ৩টি প্রশ্নের উত্তর দিয়েছি")]
    t = "<table class='chk'>"
    for a, b in chk:
        t += "<tr><td>&#9744;</td><td>%s%s</td></tr>" % (a, "<div class='bn'>%s</div>" % b if bn else "")
    c += t + "</table>"
    c += "<h2>Come viene valutato (voto in decimi)</h2>"
    val = [("Il sito è pubblicato e il link funziona", "2"), ("HTML completo e corretto", "2"),
           ("CSS in un file separato, collegato: i colori si vedono sul sito", "2"),
           ("Il sito è tuo: testi e colori scelti da te", "1,5"), ("Screenshot con la barra dell'indirizzo", "1"),
           ("Parte 5: spieghi con parole tue", "1"), ("Privacy rispettata", "0,5")]
    t = "<table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in val:
        t += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += t + "<tr><td><b>Totale</b></td><td style='text-align:center'><b>10</b></td></tr></table>"
    c += box("note", "<b>Non hai finito in tempo?</b> Consegna lo stesso quello che hai fatto e scrivilo nella parte 5: conta anche il pezzo fatto. "
             "Un errore non è una vergogna: succede a tutti i programmatori.",
             "<b>সময়ে শেষ করতে পারোনি?</b> যা করেছ তাই জমা দাও এবং অংশ ৫-এ লেখো: অর্ধেক কাজেরও মূল্য আছে। "
             "ভুল লজ্জার কিছু নয়: সব প্রোগ্রামারেরই হয়।", bn)
    c += "<div class='foot'>Classe 3 · Compito · v%s</div>" % VER
    return pagina("Compito — Il mio primo sito pubblico", c)


# ================================================================ CHIAVE DOCENTE
def docente():
    c = cover("Docente — Il primo sito pubblico (3INF, 05/10/2026)", "", "Piano delle 3 ore · chiave di correzione · errori tipici · NON per gli allievi", False)
    c += "<h2>Piano delle 3 ore (08:00 – 10:50)</h2><table><tr><th>Ora</th><th>Cosa</th><th>Vittoria visibile</th></tr>"
    c += "<tr><td>08:00–08:55</td><td>Dispensa 1: cartella mio-sito, index.html + style.css dal Blocco note. Schema a mano: HTML = contenuto, CSS = aspetto.</td><td>La pagina si apre con i colori.</td></tr>"
    c += "<tr><td>08:55–09:55</td><td>Dispensa 2: repository mio-sito, Upload files, Commit, Settings &rarr; Pages &rarr; main &rarr; Save.</td><td>Your site is live: il sito sul telefono.</td></tr>"
    c += "<tr><td>09:55–10:45</td><td>Compito: Documento in 5 parti (link, HTML, CSS separato, screenshot, spiegazione). Chi ha finito: Fallo tuo (colori, una voce in più).</td><td>Consegna entro le 10:45.</td></tr></table>"
    c += box("warn", "<b>Prima della lezione:</b> serve l'account GitHub di ogni allievo. Chi non ce l'ha o non ricorda la password: "
             "lavora in coppia con un compagno per la Dispensa 2 e recupera l'account a fine ora (non bloccare la classe).", "", False)
    c += box("info", "<b>Link unico per gli allievi</b> (con i bottoni Copia del codice): " + T(HUB), "", False)
    c += "<h2>Chiave di correzione (10 punti)</h2><table><tr><th>Voce</th><th>Punti</th><th>Come controllo</th></tr>"
    for a, p, b in [("Sito pubblicato, link funzionante", "2", "apro il link: risponde e non è 404"),
                    ("HTML completo e corretto", "2", "DOCTYPE, head con meta charset e &lt;link href=\"style.css\"&gt;, h1, p, ul/li, div.scheda, chiusure"),
                    ("CSS separato e collegato", "2", "il CSS è in una parte a sé del Documento e i colori si vedono sul sito pubblico"),
                    ("Personalizzazione", "1,5", "testi propri (non Leo/Calcio/Videogiochi) e almeno un colore cambiato"),
                    ("Screenshot", "1", "si vede la barra dell'indirizzo con github.io"),
                    ("Spiegazione e riflessione", "1", "risponde alle 3 domande con parole proprie"),
                    ("Privacy", "0,5", "nessun cognome/telefono/email: se presenti, si chiede di toglierli e si rivaluta")]:
        c += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td><td>%s</td></tr>" % (a, p, b)
    c += "</table>"
    c += "<h2>Errori tipici e rimedio veloce</h2><table><tr><th>Sintomo</th><th>Causa</th><th>Rimedio</th></tr>"
    for a, b, d in [("si vede il codice", "salvato .txt", "Salva con nome &rarr; Tutti i file"),
                    ("senza colori in locale", "style.css con altro nome o altra cartella", "rinominare / spostare"),
                    ("senza colori online", "style.css non caricato o maiuscole (Style.css)", "Upload di nuovo con il nome giusto"),
                    ("404 su github.io", "Pages non attivato, branch None, attesa, file non index.html", "Settings &rarr; Pages &rarr; main &rarr; Save, attendere 2 min"),
                    ("è diventa simboli", "codifica ANSI", "risalvare in UTF-8"),
                    ("cartella dentro la cartella su GitHub", "trascinata la cartella invece dei 2 file", "caricare i file, non la cartella")]:
        c += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, b, d)
    c += "</table>"
    c += box("note", "<b>Raccolta automatica:</b> alla scadenza il Documento di ogni allievo arriva nel repo riservato come testo; "
             "Claude controlla HTML e CSS (completi, separati, collegati, personalizzati, dati personali) e prepara la griglia. "
             "I link github.io si verificano aprendoli dal PC di classe o dal telefono (dall'ambiente di Claude non sono raggiungibili).", "", False)
    c += "<div class='foot'>Docente · v%s · Testo registro (max 40 caratteri): «HTML e CSS: primo sito su GitHub Pages»</div>" % VER
    return pagina("Docente — primo sito pubblico", c)


# ================================================================ PAGINA UNICA (docs/)
FACILE = ""   # riquadro delle schede facili (lo riempie gen_sito_facile.py)


def hub(nomi, extra=""):
    def bt(f, lab, sub=""):
        return "<a class='bt' href='%s'>%s<small>%s</small></a>" % (f, lab, sub)
    s = """<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Classe 3 — Il mio primo sito</title><style>
:root{--blu:#1f6fa5;--viola:#8a3ab9;--verde:#2f9e57;--aran:#d9731a;--txt:#1a2330;--bg:#f4f7fb}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font-family:"Segoe UI",Arial,sans-serif}
.w{max-width:820px;margin:0 auto;padding:18px 16px 40px}
h1{font-size:26px;margin:6px 0 4px;color:#12467a}.sub{color:#556;margin-bottom:12px}
.box{background:#fff;border-radius:14px;padding:16px;margin:16px 0;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.box h2{margin:0 0 6px;font-size:22px}.box p{margin:0 0 12px;color:#556}
.btns{display:flex;flex-wrap:wrap;gap:10px}
a.bt{flex:1 1 220px;display:block;text-align:center;text-decoration:none;color:#fff;font-size:21px;font-weight:700;padding:16px 10px;border-radius:12px}
a.bt small{display:block;font-size:13px;font-weight:400;opacity:.92;margin-top:4px}
.b1 h2{color:var(--blu)}.b1 a.bt{background:var(--blu)}.b2 h2{color:var(--verde)}.b2 a.bt{background:var(--verde)}
.b3 h2{color:var(--aran)}.b3 a.bt{background:var(--aran)}
.code h2{color:#12467a}.cb{position:relative;margin:10px 0 18px}
.cb .lab{font-weight:700;color:#fff;background:#12467a;display:inline-block;padding:6px 12px;border-radius:8px 8px 0 0}
.cb.css .lab{background:var(--viola)}
.cb pre{margin:0;background:#1e2733;color:#e8eef5;padding:14px;border-radius:0 8px 8px 8px;overflow:auto;font-size:14px;line-height:1.4;max-height:360px}
.cp{position:absolute;right:8px;top:0;background:#ffd34d;color:#1a2330;border:0;border-radius:8px;font-size:17px;font-weight:700;padding:8px 16px;cursor:pointer}
.cp.ok{background:#2f9e57;color:#fff}
.warn{background:#fdecea;border-left:6px solid #c0392b;padding:10px 12px;border-radius:6px;margin:10px 0}
.ver{float:right;background:#12467a;color:#fff;border-radius:12px;padding:2px 10px;font-size:13px;margin-top:10px}
</style></head><body><div class="w"><span class="ver">v%(ver)s</span><h1>Classe 3 — Il mio primo sito</h1>
<div class="sub">%(data)s · HTML + CSS + GitHub Pages · Italiano / বাংলা</div>
<div class="warn"><b>Il tuo sito sarà pubblico:</b> solo nome o soprannome. Mai cognome, telefono, email, indirizzo, foto del viso.</div>
%(facile)s
<div class="box b1"><h2>1. Dispensa 1 — La mia pagina web da zero</h2><p>Crea la cartella mio-sito con index.html e style.css.</p><div class="btns">%(d1)s</div></div>
<div class="box code"><h2>Il codice da copiare</h2><p>Premi il bottone giallo <b>Copia</b>, poi nel Blocco note premi Ctrl + V.</p>
<div class="cb"><span class="lab">RIQUADRO 1 — index.html</span><button class="cp" data-t="h">Copia</button><pre id="h">%(html)s</pre></div>
<div class="cb css"><span class="lab">RIQUADRO 2 — style.css</span><button class="cp" data-t="c">Copia</button><pre id="c">%(css)s</pre></div></div>
<div class="box b1"><h2>Ecco il risultato finito</h2><p>Apri l'esempio: il tuo sito sarà così, ma con i TUOI testi e colori.</p><div class="btns"><a class="bt" href="esempio/" target="_blank">Vedi l'esempio<small>sito di prova con dati inventati</small></a></div></div>
<div class="box b2"><h2>2. Dispensa 2 — Pubblica il sito su GitHub</h2><p>Il tuo sito su internet, con un indirizzo da aprire anche sul telefono.</p><div class="btns">%(d2)s</div></div>
<div class="box b3"><h2>3. Compito — Il mio primo sito pubblico</h2><p>Il Documento in 5 parti: link, HTML, CSS a parte, screenshot, spiegazione.</p><div class="btns">%(cp)s</div></div>
%(extra)s</div><script>
document.querySelectorAll('.cp').forEach(function(b){b.onclick=function(){
 var t=document.getElementById(b.dataset.t).textContent;
 function ok(){b.textContent='Copiato!';b.classList.add('ok');setTimeout(function(){b.textContent='Copia';b.classList.remove('ok')},2500)}
 if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){fb(t);ok()})}else{fb(t);ok()}}});
function fb(t){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}
</script></body></html>"""
    return s % {"ver": VER, "data": DATA, "html": E(HTML_CODE), "css": E(CSS_CODE),
                "d1": bt(nomi["d1_it"], "Italiano") + bt(nomi["d1_bn"], "Italiano + বাংলা"),
                "d2": bt(nomi["d2_it"], "Italiano") + bt(nomi["d2_bn"], "Italiano + বাংলা"),
                "cp": bt(nomi["cp_it"], "Italiano") + bt(nomi["cp_bn"], "Italiano + বাংলা"), "extra": extra,
                "facile": FACILE}


def pdf(html_txt, nome_html, nome_pdf):
    hp = os.path.join(CART, nome_html)
    open(hp, "w", encoding="utf-8").write(html_txt)
    out = os.path.join(CART, nome_pdf)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + out, "file://" + hp], check=True, capture_output=True)
    return out


def main(extra=""):
    # tolgo solo i PDF di QUESTA lezione (le lezioni successive hanno il loro generatore)
    for v in glob.glob(os.path.join(CART, PREF + "_*.pdf")):
        os.remove(v)
    os.makedirs(DOCS, exist_ok=True)
    for base in ("Dispensa-1-", "Dispensa-2-", "Compito-Primo-"):
        for v in glob.glob(os.path.join(DOCS, base + "*.pdf")):
            os.remove(v)
    lav = [("d1", dispensa1, "Dispensa-1-Pagina-Web-da-Zero"),
           ("d2", dispensa2, "Dispensa-2-Pubblica-Sito-GitHub"),
           ("cp", compito, "Compito-Primo-Sito-Pubblico")]
    nomi = {}
    for k, fn, base in lav:
        for lin, bn in (("IT", False), ("IT-BN", True)):
            nome = "%s_%s_%s_v%s.pdf" % (PREF, base, lin, VER)
            pdf(fn(bn), "%s-%s.html" % (base.lower(), lin), nome)
            breve = "%s-%s-v%s.pdf" % (base, lin, VER)
            shutil.copy(os.path.join(CART, nome), os.path.join(DOCS, breve))
            nomi["%s_%s" % (k, "bn" if bn else "it")] = breve
            print(nome)
    # la chiave del docente NON resta nel repo pubblico: va nel repo riservato
    out = pdf(docente(), "docente.html", "%s_Primo-Sito-Pubblico_DOCENTE_v%s.pdf" % (PREF, VER))
    ris = "/home/user/corso-informatica-riservato/materiale-docente/classe-3"
    os.makedirs(ris, exist_ok=True)
    for f in (out, os.path.join(CART, "docente.html")):
        shutil.move(f, os.path.join(ris, os.path.basename(f)))
    print("docente ->", ris)
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(hub(nomi, extra))
    for d in (os.path.join(CART, "esempio"), os.path.join(DOCS, "esempio")):   # il sito d'esempio, vivo
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(HTML_CODE)
        open(os.path.join(d, "style.css"), "w", encoding="utf-8").write(CSS_CODE)
    print("hub:", DOCS)


if __name__ == "__main__":
    main()
