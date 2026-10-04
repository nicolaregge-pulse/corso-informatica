# -*- coding: utf-8 -*-
"""Classe 3 — il sito cresce (dopo il primo sito pubblico del 05/10).

  Mercoledì 07/10: Dispensa 3 — Migliora il tuo sito direttamente su GitHub (matita, commit, storia)  + Compito 3
  Giovedì   08/10: Dispensa 4 — La seconda pagina e il menu                                           + Compito 4
IT e IT-BN, stessi stili e funzioni della Dispensa 1-2 (gen_sito_github.py). Rigenera anche la pagina unica
docs/3inf-sito/ aggiungendo i nuovi riquadri.
Uso:  python3 classe-3/sito-github/_build/gen_sito_github_2.py
"""
import os, sys, glob, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_sito_github as G
from gen_sito_github import pagina, cover, bil, step, box, T, codice, E

VER = G.VER
CART, DOCS = G.CART, G.DOCS

HTML_LINK = """    <h2>I miei siti preferiti</h2>
    <p>
      <a class="bottone" href="https://it.wikipedia.org/wiki/HTML" target="_blank">Cos'è l'HTML</a>
      <a class="bottone" href="https://www.w3schools.com/css/" target="_blank">Imparo il CSS</a>
    </p>
"""
CSS_NUOVO = """.scheda {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.bottone {
  display: inline-block;
  background: darkblue;
  color: white;
  padding: 8px 14px;
  border-radius: 8px;
  text-decoration: none;
  margin: 4px;
}

.bottone:hover {
  background: orange;
}
"""
MENU = """  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="passione.html">La mia passione</a>
  </nav>
"""
PASSIONE = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>La mia passione</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="passione.html">La mia passione</a>
  </nav>

  <h1>La mia passione: il calcio</h1>

  <div class="scheda">
    <h2>Perché mi piace</h2>
    <p>Mi piace giocare in squadra e allenarmi con gli amici.</p>

    <h2>Tre cose che so fare</h2>
    <ol>
      <li>Passare la palla con precisione</li>
      <li>Correre veloce</li>
      <li>Parare un rigore</li>
    </ol>

    <h2>Lo sapevi che...</h2>
    <p>Il primo mondiale di calcio si è giocato nel 1930.</p>
  </div>

  <p class="piede">Sito creato da me - 2026</p>
</body>
</html>
"""
CSS_MENU = """.menu {
  background: darkblue;
  padding: 10px;
  border-radius: 10px;
}

.menu a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  margin: 0 12px;
}

.menu a:hover {
  color: orange;
}
"""


def scr_edit(nome_file):
    return ("<div class='scr'><div class='bar'>github.com/tuonome/mio-sito/blob/main/%s</div><div class='in'>"
            "<b>mio-sito / %s</b><div style='text-align:right;margin-top:-4mm'><span class='wbtn'>Raw</span> "
            "<span class='wbtn hl'>&#9998;</span> <span class='fr'>&larr; matita</span> <span class='wbtn'>&#8942;</span></div></div></div>" % (nome_file, nome_file))


SCR_COMMIT = ("<div class='scr'><div class='in'><div style='text-align:right'><span class='wbtn'>Cancel changes</span> "
              "<span class='gbtn hl'>Commit changes...</span> <span class='fr'>&larr; 1</span></div>"
              "<div class='menu' style='margin-top:2mm'><div><b>Commit changes</b></div><div>Commit message: <span class='fld'>Update index.html</span></div>"
              "<div style='text-align:right'><span class='gbtn hl'>Commit changes</span> <span class='fr'>&larr; 2</span></div></div></div></div>")


def dispensa3(bn):
    c = cover("Dispensa 3 — Migliora il tuo sito direttamente su GitHub", "ডিসপেন্সা ৩ — সরাসরি GitHub-এ তোমার সাইট উন্নত করো",
              "Classe 3 · Informatica · 07/10/2026 · la matita, il commit, la storia delle versioni · %s" % ("IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa ottieni oggi:</b> nel tuo sito compaiono due <b>bottoni-link</b> che cambiano colore quando ci passi sopra, "
             "e la scheda ha un'<b>ombra</b>. Modifichi i file <b>direttamente su GitHub</b>, senza scaricare niente: ogni modifica è un <b>commit</b>, "
             "cioè una nuova <b>versione</b> salvata nella storia.",
             "<b>আজ তুমি পাবে:</b> তোমার সাইটে দুটি <b>বোতাম-লিংক</b>, মাউস রাখলে রং বদলায়, আর কার্ডে একটি <b>ছায়া</b>। "
             "ফাইলগুলো <b>সরাসরি GitHub-এ</b> বদলাবে, কিছু ডাউনলোড না করে: প্রতিটি পরিবর্তন একটি <b>commit</b>, মানে ইতিহাসে সেভ করা একটি নতুন <b>সংস্করণ</b>।", bn)
    c += box("warn", "<b>Il sito è pubblico:</b> anche oggi solo nome o soprannome, niente dati personali.",
             "<b>সাইটটি পাবলিক:</b> আজও শুধু নাম বা ডাকনাম, কোনো ব্যক্তিগত তথ্য নয়।", bn)
    c += "<h2>1. Il codice nuovo</h2>"
    c += box("info", "Il codice si copia dalla <b>pagina del corso</b> con il bottone <b>Copia</b> (link nel compito su Classroom).",
             "কোডটি <b>কোর্সের পেজ</b> থেকে <b>Copia</b> বোতাম দিয়ে কপি করো (লিংক Classroom-এর কাজে)।", bn)
    c += codice("RIQUADRO 3 — da aggiungere in index.html (prima di &lt;/div&gt;)", HTML_LINK)
    c += codice("RIQUADRO 4 — da aggiungere in fondo a style.css", CSS_NUOVO, css=True)
    c += "<h2>2. I passi, uno alla volta</h2>"
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Apri il tuo repository", "তোমার repository খোলো",
           "Vai su " + T("github.com") + ", entra (Sign in) e apri il repository <b>mio-sito</b> (in alto a sinistra, o dal tuo profilo).",
           "এই ঠিকানায় যাও: " + T("github.com") + ", ঢোকো (Sign in) এবং <b>mio-sito</b> repository খোলো (উপরে বাঁদিকে, বা তোমার প্রোফাইল থেকে)।")
    c += S("Apri index.html e premi la matita", "index.html খুলে পেনসিলে চাপো",
           "Nell'elenco dei file clic su <b>index.html</b>. In alto a destra del codice clic sulla <b>matita</b> &#9998; (Modifica).",
           "ফাইলের তালিকায় <b>index.html</b>-এ ক্লিক করো। কোডের উপরে ডানদিকে <b>পেনসিল</b> &#9998; (এডিট)-এ ক্লিক করো।",
           extra=scr_edit("index.html"))
    c += S("Incolla il RIQUADRO 3", "বাক্স ৩ পেস্ট করো",
           "Trova la riga " + T("&lt;p&gt;Lavorare con i computer.&lt;/p&gt;") + " (o il tuo sogno). Clic alla fine della riga, premi " + T("Invio") +
           " e incolla il RIQUADRO 3 (" + T("Ctrl") + " + " + T("V") + "). Deve stare <b>prima</b> di " + T("&lt;/div&gt;") + ".",
           T("&lt;p&gt;Lavorare con i computer.&lt;/p&gt;") + " (বা তোমার স্বপ্ন) লাইনটি খোঁজো। লাইনের শেষে ক্লিক করে " + T("Invio") +
           " চাপো, তারপর বাক্স ৩ পেস্ট করো (" + T("Ctrl") + " + " + T("V") + ")। এটি " + T("&lt;/div&gt;") + "-এর <b>আগে</b> থাকতে হবে।")
    c += S("Salva: Commit changes", "সেভ: Commit changes",
           "In alto a destra bottone <b>verde</b> <b>Commit changes...</b> &rarr; si apre una finestrella &rarr; di nuovo <b>Commit changes</b> (verde).",
           "উপরে ডানদিকে <b>সবুজ</b> বোতাম <b>Commit changes...</b> &rarr; একটি ছোট জানালা খুলবে &rarr; আবার <b>Commit changes</b> (সবুজ)।",
           extra=SCR_COMMIT)
    c += S("Ora style.css", "এবার style.css",
           "Torna al repository (clic su <b>mio-sito</b> in alto), clic su <b>style.css</b> &rarr; <b>matita</b>. Vai <b>in fondo</b>, premi " + T("Invio") +
           " e incolla il RIQUADRO 4. Poi <b>Commit changes...</b> &rarr; <b>Commit changes</b>.",
           "repository-তে ফিরে যাও (উপরে <b>mio-sito</b>-এ ক্লিক), <b>style.css</b>-এ ক্লিক &rarr; <b>পেনসিল</b>। <b>একদম নিচে</b> যাও, " + T("Invio") +
           " চাপো এবং বাক্স ৪ পেস্ট করো। তারপর <b>Commit changes...</b> &rarr; <b>Commit changes</b>।")
    c += S("Guarda il sito", "সাইট দেখো",
           "Aspetta 1 minuto, apri il tuo sito (" + T("https://tuonome.github.io/mio-sito/") + ") e premi " + T("Ctrl") + " + " + T("F5") +
           ". Passa con il mouse sui bottoni: diventano arancioni! <b>FATTO!</b>",
           "১ মিনিট অপেক্ষা করো, তোমার সাইট খোলো (" + T("https://tuonome.github.io/mio-sito/") + ") এবং " + T("Ctrl") + " + " + T("F5") +
           " চাপো। বোতামের উপর মাউস রাখো: কমলা হয়ে যাবে! <b>হয়ে গেছে!</b>", ok=True)
    c += S("La storia delle versioni", "সংস্করণের ইতিহাস",
           "Nel repository clic sul file <b>index.html</b> &rarr; in alto a destra <b>History</b> (Cronologia, icona con l'orologio). "
           "Vedi la lista dei tuoi <b>commit</b>: ogni riga è una versione del file, con data e messaggio. Fai uno <b>screenshot</b>: serve per il compito.",
           "repository-তে <b>index.html</b>-এ ক্লিক &rarr; উপরে ডানদিকে <b>History</b> (ইতিহাস, ঘড়ির চিহ্ন)। "
           "তোমার <b>commit</b>-এর তালিকা দেখবে: প্রতিটি লাইন ফাইলের একটি সংস্করণ, তারিখ ও বার্তা সহ। একটি <b>স্ক্রিনশট</b> নাও: কাজের জন্য লাগবে।")
    c += S("Fallo tuo", "নিজের মতো করো",
           "Cambia i link con <b>due siti utili che piacciono a te</b> (niente social, niente siti vietati) e i colori dei bottoni. Ogni volta: matita &rarr; Commit.",
           "লিংক বদলে <b>তোমার পছন্দের দুটি দরকারি সাইট</b> দাও (সোশ্যাল নয়, নিষিদ্ধ সাইট নয়) এবং বোতামের রং বদলাও। প্রতিবার: পেনসিল &rarr; Commit।")
    c += "<h2>3. Cosa fa ogni pezzo</h2>"
    rows = [("&lt;a href=\"...\"&gt;testo&lt;/a&gt;", "un <b>link</b>: <b>href</b> è l'indirizzo dove porta", "একটি <b>লিংক</b>: <b>href</b> হলো ঠিকানা যেখানে নিয়ে যায়"),
            ("target=\"_blank\"", "apre il link in una scheda nuova", "লিংকটি নতুন ট্যাবে খোলে"),
            ("class=\"bottone\"", "il nome che usa il CSS per dare l'aspetto", "যে নাম দিয়ে CSS চেহারা দেয়"),
            (".bottone:hover", "lo stile quando il mouse <b>passa sopra</b>", "মাউস <b>উপরে রাখলে</b> যে স্টাইল"),
            ("box-shadow", "l'ombra della scatola", "বাক্সের ছায়া"),
            ("commit", "una versione salvata, con data e messaggio", "তারিখ ও বার্তা সহ একটি সেভ করা সংস্করণ")]
    t = "<table><tr><th>Pezzo</th><th>Cosa fa</th>%s</tr>" % ("<th class='bn'>কী করে</th>" if bn else "")
    for a, b, d in rows:
        t += "<tr><td class='c'>%s</td><td>%s</td>%s</tr>" % (a, b, "<td class='bn'>%s</td>" % d if bn else "")
    c += t + "</table>"
    c += box("note", "<b>Non vedi i cambiamenti?</b> Aspetta ancora un minuto e premi " + T("Ctrl") + " + " + T("F5") +
             " (ricarica forzata). Se il sito si rompe: apri <b>History</b>, guardi la versione di prima e la ricopi. Con Git <b>niente si perde</b>.",
             "<b>পরিবর্তন দেখছ না?</b> আরও এক মিনিট অপেক্ষা করে " + T("Ctrl") + " + " + T("F5") +
             " চাপো। সাইট ভেঙে গেলে: <b>History</b> খুলে আগের সংস্করণ দেখে আবার কপি করো। Git-এ <b>কিছুই হারায় না</b>।", bn)
    c += box("note", "<b>Carta e penna:</b> disegna una linea del tempo con i tuoi commit (pallino = versione) e scrivi sotto cosa hai cambiato in ognuno.",
             "<b>কাগজ-কলম:</b> তোমার commit-গুলো দিয়ে একটি সময়রেখা আঁকো (বিন্দু = সংস্করণ) এবং নিচে লেখো প্রতিটিতে কী বদলেছ।", bn)
    c += "<div class='foot'>Classe 3 · Dispensa 3 · v%s</div>" % VER
    return pagina("Dispensa 3 — Migliora il tuo sito", c)


def dispensa4(bn):
    c = cover("Dispensa 4 — La seconda pagina e il menu", "ডিসপেন্সা ৪ — দ্বিতীয় পেজ ও মেনু",
              "Classe 3 · Informatica · 08/10/2026 · un sito vero ha più pagine collegate · %s" % ("IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa ottieni oggi:</b> il tuo sito ha <b>due pagine</b> (Home e La mia passione) e un <b>menu</b> in alto per passare dall'una all'altra, "
             "come i siti veri. Le due pagine usano lo <b>stesso style.css</b>: cambi un colore e cambia in tutto il sito.",
             "<b>আজ তুমি পাবে:</b> তোমার সাইটে <b>দুটি পেজ</b> (Home ও La mia passione) আর উপরে একটি <b>মেনু</b>, এক পেজ থেকে অন্যটিতে যেতে, "
             "আসল সাইটের মতো। দুটি পেজ <b>একই style.css</b> ব্যবহার করে: একটি রং বদলালে পুরো সাইটে বদলায়।", bn)
    c += "<h2>1. Il codice nuovo</h2>"
    c += codice("RIQUADRO 5 — file nuovo passione.html (la seconda pagina)", PASSIONE)
    c += codice("RIQUADRO 6 — il menu: da mettere in index.html, subito dopo &lt;body&gt;", MENU)
    c += codice("RIQUADRO 7 — in fondo a style.css", CSS_MENU, css=True)
    c += "<h2>2. I passi, uno alla volta</h2>"
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Crea il file nuovo", "নতুন ফাইল বানাও",
           "Nel repository <b>mio-sito</b>: bottone <b>Add file</b> (grigio) &rarr; <b>Create new file</b> (Crea nuovo file). In alto, nel campo del nome, scrivi " + T("passione.html") + ".",
           "<b>mio-sito</b> repository-তে: <b>Add file</b> বোতাম (ধূসর) &rarr; <b>Create new file</b> (নতুন ফাইল)। উপরে নামের ঘরে লেখো " + T("passione.html") + "।",
           extra="<div class='scr'><div class='bar'>github.com/tuonome/mio-sito/new/main</div><div class='in'>mio-sito / <span class='fld hl'>passione.html</span>"
                 "<div style='border:1px solid #d0d7de;border-radius:4px;margin-top:2mm;padding:2mm;color:#888;font-family:monospace'>Enter file contents here</div></div></div>")
    c += S("Incolla la seconda pagina", "দ্বিতীয় পেজ পেস্ট করো",
           "Nel riquadro grande incolla il RIQUADRO 5. Poi <b>Commit changes...</b> &rarr; <b>Commit changes</b>.",
           "বড় বাক্সে বাক্স ৫ পেস্ট করো। তারপর <b>Commit changes...</b> &rarr; <b>Commit changes</b>।")
    c += S("Fallo tuo", "নিজের মতো করো",
           "Con la <b>matita</b> cambia la pagina: la <b>tua</b> passione (sport, musica, cucina, un videogioco, un paese...), perché ti piace, tre cose che sai fare, una curiosità. Poi Commit.",
           "<b>পেনসিল</b> দিয়ে পেজটি বদলাও: <b>তোমার</b> শখ (খেলা, গান, রান্না, ভিডিও গেম, একটি দেশ...), কেন ভালো লাগে, তিনটি জিনিস যা পারো, একটি মজার তথ্য। তারপর Commit।")
    c += S("Il menu anche nella Home", "Home-এও মেনু",
           "Apri <b>index.html</b> &rarr; <b>matita</b>. Subito dopo la riga " + T("&lt;body&gt;") + " incolla il RIQUADRO 6. Commit.",
           "<b>index.html</b> খোলো &rarr; <b>পেনসিল</b>। " + T("&lt;body&gt;") + " লাইনের ঠিক পরে বাক্স ৬ পেস্ট করো। Commit।")
    c += S("Lo stile del menu", "মেনুর স্টাইল",
           "Apri <b>style.css</b> &rarr; <b>matita</b> &rarr; in fondo incolla il RIQUADRO 7. Commit.",
           "<b>style.css</b> খোলো &rarr; <b>পেনসিল</b> &rarr; একদম নিচে বাক্স ৭ পেস্ট করো। Commit।")
    c += S("Prova il menu", "মেনু চেষ্টা করো",
           "Aspetta 1 minuto, apri il sito, " + T("Ctrl") + " + " + T("F5") + ". Clic su <b>La mia passione</b>, poi su <b>Home</b>: passi da una pagina all'altra. <b>FATTO! Hai un sito a due pagine.</b>",
           "১ মিনিট অপেক্ষা করো, সাইট খোলো, " + T("Ctrl") + " + " + T("F5") + "। <b>La mia passione</b>-এ, তারপর <b>Home</b>-এ ক্লিক করো: এক পেজ থেকে অন্য পেজে যাবে। <b>হয়ে গেছে! তোমার দুই পেজের সাইট।</b>", ok=True)
    c += S("Mostralo", "দেখাও",
           "L'indirizzo della seconda pagina è " + T("https://tuonome.github.io/mio-sito/passione.html") + ". Aprila sul telefono e falla vedere a un compagno.",
           "দ্বিতীয় পেজের ঠিকানা " + T("https://tuonome.github.io/mio-sito/passione.html") + "। ফোনে খোলো আর একজন সহপাঠীকে দেখাও।", ok=True)
    c += "<h2>3. Se qualcosa non va</h2>"
    err = [("Clic su <b>La mia passione</b> e vedo <b>404</b>", "Il file deve chiamarsi esattamente <b>passione.html</b> (minuscolo), come nel menu.",
            "<b>La mia passione</b>-এ ক্লিক করলে <b>404</b>", "ফাইলের নাম ঠিক <b>passione.html</b> (ছোট হাতের) হতে হবে, মেনুর মতো।"),
           ("La seconda pagina è <b>senza colori</b>", "Manca la riga " + T("&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;") + " nel &lt;head&gt;.",
            "দ্বিতীয় পেজে <b>রং নেই</b>", "&lt;head&gt;-এ " + T("&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;") + " লাইনটি নেই।"),
           ("Il menu c'è ma è <b>senza stile</b>", "Il RIQUADRO 7 non è in style.css, oppure aspetta un minuto e " + T("Ctrl") + " + " + T("F5") + ".",
            "মেনু আছে কিন্তু <b>স্টাইল নেই</b>", "বাক্স ৭ style.css-এ নেই, অথবা এক মিনিট অপেক্ষা করে " + T("Ctrl") + " + " + T("F5") + "।")]
    t = "<table><tr><th style='width:34%'>Problema</th><th>Soluzione</th></tr>"
    for a, b, a2, b2 in err:
        t += "<tr><td>%s%s</td><td>%s%s</td></tr>" % (a, "<div class='bn'>%s</div>" % a2 if bn else "", b, "<div class='bn'>%s</div>" % b2 if bn else "")
    c += t + "</table>"
    c += box("note", "<b>Carta e penna:</b> disegna la <b>mappa del sito</b>: due rettangoli (index.html e passione.html) con le frecce del menu, e una freccia da ciascuno verso style.css.",
             "<b>কাগজ-কলম:</b> <b>সাইটের মানচিত্র</b> আঁকো: দুটি আয়তক্ষেত্র (index.html ও passione.html) মেনুর তীর সহ, আর প্রতিটি থেকে style.css-এর দিকে একটি তীর।", bn)
    c += "<div class='foot'>Classe 3 · Dispensa 4 · v%s</div>" % VER
    return pagina("Dispensa 4 — La seconda pagina e il menu", c)


def compito(num, bn):
    if num == 3:
        tit, tbn, data = "Compito 3 — Il sito migliorato", "কাজ ৩ — উন্নত সাইট", "07/10/2026"
        parti = [("Il link del tuo sito", "তোমার সাইটের লিংক"),
                 ("Screenshot del sito con i due bottoni-link", "দুটি বোতাম-লিংক সহ সাইটের স্ক্রিনশট"),
                 ("Il codice CSS che hai aggiunto (RIQUADRO 4, con i tuoi colori)", "যে CSS কোড যোগ করেছ (বাক্স ৪, তোমার রং সহ)"),
                 ("Screenshot della History (la lista dei commit)", "History-র স্ক্রিনশট (commit-এর তালিকা)"),
                 ("Spiegalo con parole tue: a) a cosa serve href? b) cos'è un commit e perché con Git niente si perde?",
                  "নিজের ভাষায়: ক) href কী কাজে লাগে? খ) commit কী এবং Git-এ কেন কিছু হারায় না?")]
        val = [("Sito con i due bottoni funzionanti", "3"), ("CSS aggiunto e personalizzato", "2"), ("Screenshot della History", "2"),
               ("Spiegazione con parole tue", "2"), ("Riflessione: cosa non ho capito", "1")]
    else:
        tit, tbn, data = "Compito 4 — Il sito a due pagine", "কাজ ৪ — দুই পেজের সাইট", "08/10/2026"
        parti = [("I due link: la Home e la pagina passione.html", "দুটি লিংক: Home ও passione.html পেজ"),
                 ("Due screenshot: la Home con il menu e la tua pagina della passione", "দুটি স্ক্রিনশট: মেনু সহ Home ও তোমার শখের পেজ"),
                 ("Tutto il codice di passione.html", "passione.html-এর পুরো কোড"),
                 ("Il codice CSS del menu (RIQUADRO 7)", "মেনুর CSS কোড (বাক্স ৭)"),
                 ("Spiegalo con parole tue: perché le due pagine hanno gli stessi colori? Disegna (foto) la mappa del sito.",
                  "নিজের ভাষায়: দুটি পেজে কেন একই রং? সাইটের মানচিত্র আঁকো (ছবি)।")]
        val = [("Due pagine pubblicate, il menu funziona", "3"), ("La pagina della passione è tua (testi tuoi)", "2"),
               ("Codice HTML e CSS completi e separati", "2"), ("Spiegazione + mappa del sito", "2"), ("Riflessione", "1")]
    c = "<style>.step{margin:1.5mm 0}.step .b{padding:1.2mm 3mm}.step .h{padding:1.1mm 3mm}.cover{padding:5mm 8mm}</style>"
    c += cover(tit, tbn, "Classe 3 · Informatica · %s · si consegna su Classroom · %s" % (data, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom (c'è già il tuo nome), una parte sotto l'altra.",
             "<b>কী জমা দেবে:</b> Classroom-এর কাজে আগে থেকে তৈরি <b>Documento</b> (তোমার নাম সহ), একটি অংশের নিচে আরেকটি।", bn)
    c += box("warn", "<b>Privacy:</b> sul sito solo nome o soprannome. <b>Screenshot:</b> " + T("Win") + " + " + T("Shift") + " + " + T("S") + ", poi nel Documento " + T("Ctrl") + " + " + T("V") + ".",
             "<b>গোপনীয়তা:</b> সাইটে শুধু নাম বা ডাকনাম। <b>স্ক্রিনশট:</b> " + T("Win") + " + " + T("Shift") + " + " + T("S") + ", তারপর Documento-তে " + T("Ctrl") + " + " + T("V") + "।", bn)
    for i, (a, b) in enumerate(parti, 1):
        c += step(i, "Parte %d" % i, "অংশ %d" % i, a, b, bn)
    c += step(len(parti) + 1, "Riflessione e consegna", "চিন্তা ও জমা",
              "Scrivi cosa NON sei riuscito a fare e cosa NON hai capito. Poi in Classroom bottone <b>blu</b> <b>Consegna</b>.",
              "লেখো কী করতে পারোনি আর কী বোঝোনি। তারপর Classroom-এ <b>নীল</b> বোতাম <b>Consegna</b> (জমা দাও)।", bn, ok=True)
    t = "<h2>Come viene valutato (voto in decimi)</h2><table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in val:
        t += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += t + "</table>"
    pass  # niente piè di pagina: il compito sta in una pagina
    return pagina(tit, c)


def main():
    lav = [("d3", dispensa3, "20261007_Classe-3", "Dispensa-3-Migliora-Sito-GitHub"),
           ("c3", lambda bn: compito(3, bn), "20261007_Classe-3", "Compito-3-Sito-Migliorato"),
           ("d4", dispensa4, "20261008_Classe-3", "Dispensa-4-Seconda-Pagina-Menu"),
           ("c4", lambda bn: compito(4, bn), "20261008_Classe-3", "Compito-4-Sito-Due-Pagine")]
    for pref in ("20261007_Classe-3", "20261008_Classe-3"):
        for v in glob.glob(os.path.join(CART, pref + "_*.pdf")): os.remove(v)
    for _, _, _, base in lav:
        for v in glob.glob(os.path.join(DOCS, base + "*.pdf")): os.remove(v)
    nomi = {}
    for k, fn, pref, base in lav:
        for lin, bn in (("IT", False), ("IT-BN", True)):
            nome = "%s_%s_%s_v%s.pdf" % (pref, base, lin, VER)
            G.pdf(fn(bn), "%s-%s.html" % (base.lower(), lin), nome)
            breve = "%s-%s-v%s.pdf" % (base, lin, VER)
            shutil.copy(os.path.join(CART, nome), os.path.join(DOCS, breve))
            nomi[k + ("_bn" if bn else "_it")] = breve
            print(nome)
    def bt(f, lab):
        return "<a class='bt' href='%s'>%s</a>" % (f, lab)
    def riquadro(id_, lab, testo, css=False):
        return ("<div class='cb%s'><span class='lab'>%s</span><button class='cp' data-t='%s'>Copia</button><pre id='%s'>%s</pre></div>"
                % (" css" if css else "", lab, id_, id_, E(testo)))
    extra = ("<h1 style='margin-top:30px'>Mercoledì 07/10 — Il sito migliorato</h1>"
             "<div class='box b1'><h2>4. Dispensa 3 — Migliora il tuo sito su GitHub</h2><p>La matita, il commit, la storia delle versioni.</p><div class='btns'>%s%s</div></div>"
             "<div class='box code'><h2>Il codice di oggi</h2><p>Premi <b>Copia</b>, poi su GitHub (matita) premi Ctrl + V.</p>%s%s</div>"
             "<div class='box b3'><h2>5. Compito 3 — Il sito migliorato</h2><div class='btns'>%s%s</div></div>"
             "<h1 style='margin-top:30px'>Giovedì 08/10 — Il sito a due pagine</h1>"
             "<div class='box b1'><h2>6. Dispensa 4 — La seconda pagina e il menu</h2><p>Un file nuovo, il menu, lo stesso stile.</p><div class='btns'>%s%s</div></div>"
             "<div class='box code'><h2>Il codice di giovedì</h2>%s%s%s</div>"
             "<div class='box b3'><h2>7. Compito 4 — Il sito a due pagine</h2><div class='btns'>%s%s</div></div>") % (
        bt(nomi["d3_it"], "Italiano"), bt(nomi["d3_bn"], "Italiano + বাংলা"),
        riquadro("r3", "RIQUADRO 3 — in index.html", HTML_LINK), riquadro("r4", "RIQUADRO 4 — in fondo a style.css", CSS_NUOVO, True),
        bt(nomi["c3_it"], "Italiano"), bt(nomi["c3_bn"], "Italiano + বাংলা"),
        bt(nomi["d4_it"], "Italiano"), bt(nomi["d4_bn"], "Italiano + বাংলা"),
        riquadro("r5", "RIQUADRO 5 — passione.html", PASSIONE), riquadro("r6", "RIQUADRO 6 — il menu in index.html", MENU),
        riquadro("r7", "RIQUADRO 7 — in fondo a style.css", CSS_MENU, True),
        bt(nomi["c4_it"], "Italiano"), bt(nomi["c4_bn"], "Italiano + বাংলা"))
    G.main(extra)   # rigenera anche la lezione del 05/10 e la pagina unica con tutti i riquadri


if __name__ == "__main__":
    main()
