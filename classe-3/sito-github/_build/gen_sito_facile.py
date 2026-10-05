# -*- coding: utf-8 -*-
"""Classe 3 — 05/10/2026: le due SCHEDE FACILI (livello scuola media), una pagina ciascuna, 7 passi.
  Scheda facile 1 — La mia pagina web in 7 passi
  Scheda facile 2 — Metti la tua pagina su internet in 7 passi
IT e IT-BN. Stessi codici (RIQUADRO 1 e 2) della Dispensa 1: si copiano dalla pagina del corso con il bottone Copia.
Le mette in cima alla pagina unica docs/3inf-sito/ e rigenera tutto (Dispense 1-4).
Uso:  python3 classe-3/sito-github/_build/gen_sito_facile.py
"""
import os, sys, glob, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_sito_github as G
import gen_sito_github_2 as G2
from gen_sito_github import pagina, cover, step, box, T

VER = G.VER
PREF = "20261005_Classe-3-Facile"
CART, DOCS = G.CART, G.DOCS

GRANDE = ("<style>body{font-size:12.6pt;line-height:1.5}.bn{font-size:12.6pt}.step{margin:2mm 0}.step .h{font-size:12pt}"
          ".step .b{padding:1.6mm 3.5mm}.cover{padding:5mm 7mm}.cover h1{font-size:20pt;padding-right:18mm}.tasto{font-size:11pt}</style>")

CARTELLA = ("<div class='scr' style='width:70mm'><div class='bar'>Desktop &gt; mio-sito</div><div class='in' style='text-align:center'>"
            "<span class='file'>index.html</span> <span class='file'>style.css</span></div></div>")
SALVA = ("<div class='scr' style='width:95mm'><div class='bar'>Salva con nome</div><div class='in'>"
         "Nome file: <span class='fld hl'>index.html</span><br>Salva come: <span class='fld hl'>Tutti i file (*.*)</span></div></div>")
NUOVO = ("<div class='scr' style='width:80mm'><div class='gh'><span>GitHub</span><span class='hl' style='padding:0 2mm'>+ &#9662;</span></div>"
         "<div class='in' style='text-align:right'><span class='hl' style='padding:0 2mm'>New repository</span></div></div>")
CREA = ("<div class='scr' style='width:95mm'><div class='in'>Repository name: <span class='fld hl'>mio-sito</span><br>"
        "&#9673; Public &nbsp; Add README: <b style='background:#1f883d;color:#fff;padding:0 2mm;border-radius:8px'>On</b><br>"
        "<div style='text-align:right'><span class='gbtn hl'>Create repository</span></div></div></div>")
CARICA = ("<div class='scr' style='width:100mm'><div class='in' style='text-align:right'><span class='wbtn hl'>Add file &#9662;</span> <span class='gbtn'>Code</span>"
          "<div class='drop' style='text-align:center'>index.html &nbsp; style.css</div><span class='gbtn hl'>Commit changes</span></div></div>")
PAGES = ("<div class='scr' style='width:110mm'><div class='in'><span class='wbtn hl'>&#9881; Settings</span> &rarr; <span class='hl' style='padding:0 1mm'><b>Pages</b></span> &rarr; "
         "Branch: <span class='wbtn hl'>main &#9662;</span> <span class='wbtn hl'>Save</span></div></div>")
LIVE = ("<div class='scr' style='width:110mm'><div class='in'><div class='live'>Your site is live at <b>https://tuonome.github.io/mio-sito/</b> "
        "<span class='wbtn hl'>Visit site</span></div></div></div>")


def scheda1(bn):
    c = GRANDE + cover("La mia pagina web in 7 passi", "৭ ধাপে আমার ওয়েব পেজ",
                       "Classe 3 · scheda FACILE · 05/10/2026 · %s" % ("IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Alla fine:</b> una pagina web con il <b>tuo nome</b>, che si apre nel browser. Ci vogliono circa 20 minuti. Una cosa alla volta!",
             "<b>শেষে:</b> <b>তোমার নাম</b> সহ একটি ওয়েব পেজ, ব্রাউজারে খুলবে। প্রায় ২০ মিনিট লাগবে। একবারে একটি কাজ!", bn)
    s = [("Fai una cartella", "একটি ফোল্ডার বানাও",
          "Sul Desktop: tasto <b>destro</b> del mouse &rarr; <b>Nuovo</b> &rarr; <b>Cartella</b>. Scrivi " + T("mio-sito") + " e premi " + T("Invio") + ".",
          "Desktop-এ মাউসের <b>ডান</b> বোতাম &rarr; <b>Nuovo</b> &rarr; <b>Cartella</b>। লেখো " + T("mio-sito") + " এবং " + T("Invio") + " চাপো।", ""),
         ("Copia il codice", "কোড কপি করো",
          "Apri il link del compito su Classroom. Sul <b>RIQUADRO 1</b> premi il bottone giallo <b>Copia</b>.",
          "Classroom-এর কাজের লিংক খোলো। <b>বাক্স ১</b>-এ হলুদ <b>Copia</b> বোতাম চাপো।", ""),
         ("Incolla nel Blocco note", "Notepad-এ পেস্ট করো",
          "Start &rarr; scrivi " + T("Blocco note") + " &rarr; aprilo. Premi " + T("Ctrl") + " + " + T("V") + ".",
          "Start &rarr; লেখো " + T("Blocco note") + " &rarr; খোলো। " + T("Ctrl") + " + " + T("V") + " চাপো।", ""),
         ("Metti il tuo nome", "তোমার নাম লেখো",
          "Trova <b>Leo</b> e scrivi al suo posto il tuo nome (o un soprannome). Niente cognome!",
          "<b>Leo</b> খুঁজে তার জায়গায় তোমার নাম (বা ডাকনাম) লেখো। পদবি নয়!", ""),
         ("Salva: index.html", "সেভ: index.html",
          "<b>File</b> &rarr; <b>Salva con nome</b> &rarr; cartella <b>mio-sito</b>. <b>Salva come: Tutti i file</b>. Nome: " + T("index.html") + " &rarr; <b>Salva</b>.",
          "<b>File</b> &rarr; <b>Salva con nome</b> &rarr; <b>mio-sito</b> ফোল্ডার। <b>Salva come: Tutti i file</b>। নাম: " + T("index.html") + " &rarr; <b>Salva</b>।", SALVA),
         ("Il secondo file: style.css", "দ্বিতীয় ফাইল: style.css",
          "<b>File</b> &rarr; <b>Nuovo</b>. Copia il <b>RIQUADRO 2</b> (bottone Copia) e incolla. Salva come prima, nome " + T("style.css") + ".",
          "<b>File</b> &rarr; <b>Nuovo</b>। <b>বাক্স ২</b> কপি করো (Copia বোতাম) এবং পেস্ট করো। আগের মতো সেভ করো, নাম " + T("style.css") + "।", CARTELLA),
         ("Apri la tua pagina", "তোমার পেজ খোলো",
          "Nella cartella <b>mio-sito</b> fai <b>doppio clic</b> su <b>index.html</b>. <b>FATTO! È la tua pagina web!</b>",
          "<b>mio-sito</b> ফোল্ডারে <b>index.html</b>-এ <b>ডাবল ক্লিক</b> করো। <b>হয়ে গেছে! এটা তোমার ওয়েব পেজ!</b>", "")]
    for i, (a, a2, b, b2, x) in enumerate(s, 1):
        c += step(i, a, a2, b, b2, bn, extra=x, ok=(i == 7))
    c += box("note", "<b>Bonus:</b> apri style.css con il Blocco note, cambia " + T("lightblue") + " con " + T("pink") + " o " + T("gold") +
             ", salva e premi " + T("F5") + ". <b>Problema?</b> Alza la mano: succede a tutti!",
             "<b>বোনাস:</b> Notepad দিয়ে style.css খোলো, " + T("lightblue") + " বদলে " + T("pink") + " বা " + T("gold") +
             " লেখো, সেভ করে " + T("F5") + " চাপো। <b>সমস্যা?</b> হাত তোলো: সবার হয়!", bn)
    return pagina("Scheda facile 1", c)


def scheda2(bn):
    c = GRANDE + cover("Metti la tua pagina su internet in 7 passi", "৭ ধাপে তোমার পেজ ইন্টারনেটে দাও",
                       "Classe 3 · scheda FACILE · 05/10/2026 · %s" % ("IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Alla fine:</b> la tua pagina ha un <b>indirizzo vero</b> e la apri anche sul <b>telefono</b>. Cerca i bottoni con il <b style='color:#e0312b'>cerchio rosso</b> nei disegni.",
             "<b>শেষে:</b> তোমার পেজের একটি <b>আসল ঠিকানা</b> থাকবে, <b>ফোনেও</b> খুলবে। ছবিতে <b style='color:#e0312b'>লাল দাগ</b> দেওয়া বোতামগুলো খোঁজো।", bn)
    s = [("Entra su GitHub", "GitHub-এ ঢোকো",
          "Vai su " + T("github.com") + " &rarr; in alto a destra <b>Sign in</b> &rarr; nome utente e password.",
          "এই ঠিকানায় যাও: " + T("github.com") + " &rarr; উপরে ডানদিকে <b>Sign in</b> &rarr; ইউজারনেম ও পাসওয়ার্ড।", ""),
         ("Nuovo repository", "নতুন repository",
          "In alto a destra clic sul <b>+</b> &rarr; <b>New repository</b>.",
          "উপরে ডানদিকে <b>+</b> চিহ্নে ক্লিক &rarr; <b>New repository</b>।", NUOVO),
         ("Dai il nome", "নাম দাও",
          "Nome: " + T("mio-sito") + ". Lascia <b>Public</b>. <b>Add README</b> su <b>On</b>. Bottone verde <b>Create repository</b>.",
          "নাম: " + T("mio-sito") + "। <b>Public</b> রাখো। <b>Add README</b> <b>On</b> করো। সবুজ বোতাম <b>Create repository</b>।", CREA),
         ("Carica i 2 file", "২টি ফাইল আপলোড করো",
          "<b>Add file</b> &rarr; <b>Upload files</b>. Trascina <b>index.html</b> e <b>style.css</b> dalla cartella mio-sito. Bottone verde <b>Commit changes</b>.",
          "<b>Add file</b> &rarr; <b>Upload files</b>। mio-sito ফোল্ডার থেকে <b>index.html</b> ও <b>style.css</b> টেনে আনো। সবুজ বোতাম <b>Commit changes</b>।", CARICA),
         ("Apri Settings", "Settings খোলো",
          "Nella fila di schede in alto (Code, Issues...) clic sull'ultima a destra: <b>Settings</b> (ingranaggio). "
          "<b>Non la vedi?</b> Clic su <b>More &#9662;</b> (o sui <b>...</b>) tutto a destra: Settings è lì dentro.",
          "উপরের ট্যাবের সারিতে (Code, Issues...) একদম ডানদিকের <b>Settings</b>-এ (গিয়ার) ক্লিক করো। "
          "<b>দেখতে পাচ্ছ না?</b> একদম ডানদিকে <b>More &#9662;</b> (বা <b>...</b>)-এ ক্লিক করো: Settings ওর ভিতরে আছে।", ""),
         ("Pages: scegli main e Save", "Pages: main বেছে Save",
          "Nel menu a sinistra clic su <b>Pages</b>. Sotto <b>Branch</b> clic su <b>None</b> &rarr; scegli <b>main</b> &rarr; bottone <b>Save</b>. "
          "<b>Custom domain (dominio personalizzato): NON scrivere niente, lascialo vuoto!</b> Non serve.",
          "বাঁদিকের মেনুতে <b>Pages</b>-এ ক্লিক করো। <b>Branch</b>-এর নিচে <b>None</b>-এ ক্লিক &rarr; <b>main</b> বেছে নাও &rarr; <b>Save</b> বোতাম। "
          "<b>Custom domain: কিছুই লিখবে না, খালি রাখো!</b> দরকার নেই।", PAGES),
         ("Aspetta e apri il sito", "অপেক্ষা করে সাইট খোলো",
          "Aspetta 2 minuti e premi " + T("F5") + ": in alto compare <b>Your site is live</b> e il bottone <b>Visit site</b>. Cliccalo. "
          "<b>FATTO! Sei su internet.</b> Il tuo indirizzo è " + T("https://TUONOME.github.io/mio-sito/") + ": aprilo sul telefono!",
          "২ মিনিট অপেক্ষা করে " + T("F5") + " চাপো: উপরে আসবে <b>Your site is live</b> আর <b>Visit site</b> বোতাম। ক্লিক করো। "
          "<b>হয়ে গেছে! তুমি ইন্টারনেটে।</b> তোমার ঠিকানা " + T("https://TUONOME.github.io/mio-sito/") + ": ফোনে খোলো!", LIVE)]
    for i, (a, a2, b, b2, x) in enumerate(s, 1):
        c += step(i, a, a2, b, b2, bn, extra=x, ok=(i == 7))
    c += box("warn", "<b>GitHub chiede un \"Custom domain\" (dominio personalizzato)?</b> NON serve e NON si compra niente: lascia il campo vuoto. "
             "Il tuo indirizzo gratis è già pronto. <b>Prima di caricare:</b> nella pagina solo nome o soprannome.",
             "<b>GitHub \"Custom domain\" চাইছে?</b> দরকার নেই, কিছু কিনতে হবে না: ঘরটি খালি রাখো। তোমার ফ্রি ঠিকানা আগে থেকেই তৈরি। "
             "<b>আপলোডের আগে:</b> পেজে শুধু নাম বা ডাকনাম।", bn)
    return pagina("Scheda facile 2", c)


def main():
    for v in glob.glob(os.path.join(CART, PREF + "_*.pdf")): os.remove(v)
    for v in glob.glob(os.path.join(DOCS, "Scheda-Facile-*.pdf")): os.remove(v)
    nomi = {}
    for k, fn, base, ver in [("s1", scheda1, "Scheda-Facile-1-Pagina-Web", "1.0"), ("s2", scheda2, "Scheda-Facile-2-Su-Internet", "1.1")]:
        G.VER = ver   # v1.1 (05/10, in classe): Settings sotto More, Pages passo per passo, Custom domain da lasciare vuoto
        for lin, bn in (("IT", False), ("IT-BN", True)):
            nome = "%s_%s_%s_v%s.pdf" % (PREF, base, lin, ver)
            G.pdf(fn(bn), "%s-%s.html" % (base.lower(), lin), nome)
            breve = "%s-%s-v%s.pdf" % (base, lin, ver)
            shutil.copy(os.path.join(CART, nome), os.path.join(DOCS, breve))
            nomi[k + ("_bn" if bn else "_it")] = breve
            print(nome)
    bt = lambda f, l: "<a class='bt' href='%s'>%s</a>" % (f, l)
    G.FACILE = ("<div class='box b2'><h2>VERSIONE FACILE — 2 schede da 7 passi</h2><p>Comincia da qui! Una pagina sola, un passo alla volta.</p>"
                "<div class='btns'>%s%s</div><div class='btns' style='margin-top:10px'>%s%s</div></div>") % (
        bt(nomi["s1_it"], "1. La mia pagina<small>italiano</small>"), bt(nomi["s1_bn"], "1. La mia pagina<small>italiano + বাংলা</small>"),
        bt(nomi["s2_it"], "2. Su internet<small>italiano</small>"), bt(nomi["s2_bn"], "2. Su internet<small>italiano + বাংলা</small>"))
    G.VER = VER
    G.FACILE += ("<div class='box' style='border:3px solid #c0392b'><h2 style='color:#c0392b'>PUBBLICARE: i passi giusti (leggi qui se ti blocchi)</h2>"
                 "<ol style='font-size:17px;line-height:1.7'><li>Nel tuo repository <b>mio-sito</b> clic su <b>Settings</b> (ingranaggio, ultima scheda in alto a destra). "
                 "Non la vedi? Clic su <b>More &#9662;</b> tutto a destra.</li><li>Nel menu a sinistra clic su <b>Pages</b>.</li>"
                 "<li>Sotto <b>Branch</b> clic su <b>None</b> &rarr; scegli <b>main</b> &rarr; <b>Save</b>.</li>"
                 "<li><b>Custom domain: NON scrivere niente.</b> Non serve, non si paga niente.</li>"
                 "<li>Aspetta 2 minuti, premi F5: in alto <b>Your site is live</b> &rarr; <b>Visit site</b>. Indirizzo: <b>https://TUONOME.github.io/mio-sito/</b></li></ol>"
                 "<p style='font-size:16px;color:#1d4d2f'>Settings &rarr; Pages &rarr; Branch: main &rarr; Save. <b>Custom domain: কিছুই লিখবে না, খালি রাখো।</b> ২ মিনিট পরে F5 &rarr; Visit site।</p></div>")
    PROB = [("Il sito dice <b>404</b> / <b>There isn't a GitHub Pages site here</b>",
             "Settings &rarr; Pages: sotto <b>Branch</b> deve esserci <b>main</b> (non None) e devi aver premuto <b>Save</b>. Poi aspetta 2 minuti e premi Ctrl + F5.",
             "Settings &rarr; Pages: <b>Branch</b>-এ <b>main</b> থাকতে হবে (None নয়) এবং <b>Save</b> চাপতে হবে। তারপর ২ মিনিট অপেক্ষা করে Ctrl + F5।"),
            ("Il sito mostra solo la scritta <b>mio-sito</b>",
             "GitHub mostra il README perché manca <b>index.html</b>. Nel repository: <b>Add file &rarr; Upload files</b> e carica <b>index.html</b> e <b>style.css</b> (i file, non la cartella).",
             "README দেখাচ্ছে কারণ <b>index.html</b> নেই। <b>Add file &rarr; Upload files</b> দিয়ে <b>index.html</b> ও <b>style.css</b> আপলোড করো (ফাইল, ফোল্ডার নয়)।"),
            ("Non vedo il bottone <b>Add file</b>",
             "Hai creato il repository senza README: al centro della pagina clic sul link blu <b>uploading an existing file</b>.",
             "README ছাড়া repository বানিয়েছ: পেজের মাঝখানে নীল লিংক <b>uploading an existing file</b>-এ ক্লিক করো।"),
            ("Non trovo <b>Settings</b>",
             "La finestra è stretta: in alto a destra clic su <b>More &#9662;</b> (o <b>...</b>) e poi <b>Settings</b>.",
             "জানালা ছোট: উপরে ডানদিকে <b>More &#9662;</b> (বা <b>...</b>), তারপর <b>Settings</b>।"),
            ("GitHub chiede un <b>Custom domain</b>",
             "<b>Lascialo vuoto.</b> Non serve e non si paga niente: il tuo indirizzo gratis è https://TUONOME.github.io/mio-sito/",
             "<b>খালি রাখো।</b> দরকার নেই, টাকা লাগে না: তোমার ফ্রি ঠিকানা https://TUONOME.github.io/mio-sito/"),
            ("Ho chiamato il repository <b>mio_sito</b> o in un altro modo",
             "Va bene lo stesso: cambia solo l'indirizzo, che diventa https://TUONOME.github.io/NOME-DEL-REPOSITORY/",
             "চলবে: শুধু ঠিকানা বদলায়: https://TUONOME.github.io/REPOSITORY-এর-নাম/"),
            ("Non ricordo la password di GitHub",
             "Pagina di accesso &rarr; <b>Forgot password?</b> &rarr; scrivi la tua email della scuola &rarr; apri la mail e crea una password nuova. Scrivila sul quaderno.",
             "লগইন পেজে <b>Forgot password?</b> &rarr; স্কুলের ইমেল লেখো &rarr; মেইল খুলে নতুন পাসওয়ার্ড বানাও। খাতায় লিখে রাখো।"),
            ("Vedo il codice invece della pagina, oppure è senza colori",
             "Il file è salvato come .txt, oppure style.css ha un nome diverso. Risalva con <b>Tutti i file</b> e nomi tutti minuscoli: index.html e style.css.",
             "ফাইল .txt হয়ে গেছে, বা style.css-এর নাম আলাদা। <b>Tutti i file</b> বেছে আবার সেভ করো, ছোট হাতের নাম: index.html ও style.css।")]
    righe = "".join("<tr><td style='padding:8px;border-bottom:1px solid #e3e9f0;vertical-align:top;width:34%%'><b>%s</b></td>"
                    "<td style='padding:8px;border-bottom:1px solid #e3e9f0'>%s<div style='color:#1d4d2f;margin-top:4px'>%s</div></td></tr>" % p for p in PROB)
    G.FACILE += ("<div class='box' style='border:3px solid #d0a516'><h2 style='color:#8a6d00'>PROBLEMI? Le soluzioni (dai problemi di oggi)</h2>"
                 "<table style='width:100%%;border-collapse:collapse;font-size:16px'>%s</table></div>" % righe)
    G2.main()


if __name__ == "__main__":
    main()
