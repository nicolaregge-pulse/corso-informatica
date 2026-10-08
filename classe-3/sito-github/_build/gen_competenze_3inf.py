# -*- coding: utf-8 -*-
"""Classe 3 — giovedì 08/10/2026: «Il mio sito diventa il mio portfolio» (competenze personali).

Richiesta di Nicola (08/10): lavorare sulle competenze personali e su quello che i ragazzi hanno imparato qui,
che non avrebbero imparato se non fossero venuti in questa scuola. Il sito pubblico guadagna una seconda pagina,
competenze.html («Cosa so fare»), da mostrare allo stage; la riflessione sincera resta PRIVATA nel Documento
di Classroom. Stessa tecnica della Dispensa 4 (file nuovo + menu), che resta come facoltativa.

Produce: Dispensa 5 e Compito 4 (IT e IT-BN) in classe-3/sito-github/ e in docs/3inf-sito/, e mette in testa
alla pagina docs/3inf-sito/ il blocco di oggi (con i riquadri Copia), spostando «Il sito a due pagine» tra i facoltativi.
Uso:  python3 classe-3/sito-github/_build/gen_competenze_3inf.py
"""
import os, sys, glob, re, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_sito_github as G
from gen_sito_github import pagina, cover, step, box, T, codice, E
from gen_sito_github_2 import CSS_MENU

VER = "1.0"
CART, DOCS = G.CART, G.DOCS
DATA = "08/10/2026"

COMPETENZE = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cosa so fare</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="competenze.html">Cosa so fare</a>
  </nav>

  <h1>Cosa so fare</h1>

  <div class="scheda">
    <h2>Le mie competenze tecniche</h2>
    <ul>
      <li>Scrivo una pagina web in HTML</li>
      <li>Cambio colori e stile con il CSS</li>
      <li>Pubblico il mio sito su Internet con GitHub</li>
      <li>Salvo ogni modifica con un commit</li>
    </ul>

    <h2>Le mie competenze personali</h2>
    <ul>
      <li>Quando mi blocco, chiedo aiuto</li>
      <li>Se sbaglio, riprovo</li>
      <li>Aiuto un compagno quando posso</li>
    </ul>

    <h2>Cosa ho imparato in questa scuola</h2>
    <p>Qui ho imparato a ...</p>

    <h2>La mia frase per un'azienda</h2>
    <p>Studio informatica. So creare e pubblicare un sito web. Imparo in fretta e non mi arrendo.</p>
  </div>

  <p class="piede">Sito creato da me - 2026</p>
</body>
</html>
"""
MENU = """  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="competenze.html">Cosa so fare</a>
  </nav>
"""
RIGA_PASSIONE = """    <a href="passione.html">La mia passione</a>
"""
CSS_SCHEDA = """.scheda {
  background: white;
  border-radius: 12px;
  padding: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
"""

# (italiano, bangla) — competenze personali: dal quadro europeo delle competenze personali e sociali
VOCI = [("Chiedo aiuto quando mi blocco", "আটকে গেলে সাহায্য চাই"),
        ("Non mi arrendo dopo un errore: riprovo", "ভুল করলে হাল ছাড়ি না: আবার চেষ্টা করি"),
        ("Lavoro da solo seguendo una guida", "নির্দেশিকা দেখে নিজে নিজে কাজ করি"),
        ("Rispetto i tempi e consegno", "সময় মেনে কাজ জমা দিই"),
        ("Rispetto le regole del laboratorio", "ল্যাবের নিয়ম মেনে চলি"),
        ("Aiuto e collaboro con i compagni", "সহপাঠীদের সাহায্য ও সহযোগিতা করি"),
        ("Resto concentrato sul lavoro", "কাজে মনোযোগ রাখি"),
        ("Spiego con parole mie quello che ho fatto", "যা করেছি তা নিজের ভাষায় বুঝিয়ে বলি"),
        ("Tengo in ordine file, account e password", "ফাইল, অ্যাকাউন্ট ও পাসওয়ার্ড গুছিয়ে রাখি"),
        ("Uso internet e l'AI in modo responsabile", "ইন্টারনেট ও AI দায়িত্বের সাথে ব্যবহার করি")]


def dispensa5(bn):
    c = cover("Dispensa 5 — Il mio sito diventa il mio portfolio", "ডিসপেন্সা ৫ — আমার সাইট হবে আমার পোর্টফোলিও",
              "Classe 3 · Informatica · %s · le mie competenze, da mostrare allo stage · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa ottieni oggi:</b> il tuo sito ha una pagina nuova, <b>Cosa so fare</b>: le tue competenze tecniche e personali, "
             "spiegate da te. È il tuo <b>biglietto da visita</b>: lo puoi mostrare a un'azienda, allo stage, a un colloquio.",
             "<b>আজ তুমি পাবে:</b> তোমার সাইটে একটি নতুন পেজ, <b>Cosa so fare</b> (আমি কী পারি): তোমার কারিগরি ও ব্যক্তিগত দক্ষতা, "
             "তোমার নিজের ভাষায়। এটি তোমার <b>ভিজিটিং কার্ড</b>: কোম্পানি, ইন্টার্নশিপ বা সাক্ষাৎকারে দেখাতে পারো।", bn)
    c += "<h2>1. Prima, carta e penna (15 minuti)</h2>"
    c += step(1, "Prima e dopo", "আগে ও এখন",
              "Sul foglio fai due colonne: <b>A settembre</b> e <b>Oggi</b>. Scrivi almeno <b>3 cose</b> che oggi sai fare e a settembre no "
              "(per esempio: ho un account GitHub, il mio sito è su Internet, so cos'è un commit...).",
              "কাগজে দুটি কলাম করো: <b>সেপ্টেম্বরে</b> আর <b>আজ</b>। অন্তত <b>৩টি জিনিস</b> লেখো যা আজ পারো কিন্তু সেপ্টেম্বরে পারতে না "
              "(যেমন: আমার GitHub অ্যাকাউন্ট আছে, আমার সাইট ইন্টারনেটে আছে, commit কী জানি...)।", bn)
    c += step(2, "Cosa ho imparato qui", "এখানে কী শিখেছি",
              "Scrivi <b>una cosa</b> che hai imparato in questa scuola e che da un'altra parte, secondo te, non avresti imparato. Anche non di informatica.",
              "<b>একটি জিনিস</b> লেখো যা এই স্কুলে শিখেছ এবং তোমার মতে অন্য কোথাও শিখতে না। কম্পিউটারের বাইরেরও হতে পারে।", bn)
    c += step(3, "A coppie: ti ho visto bravo quando...", "জোড়ায়: আমি তোমাকে ভালো করতে দেখেছি যখন...",
              "Scambia il foglio con il compagno. Sul suo foglio scrivi una frase vera: <b>«Ti ho visto bravo quando...»</b>. Poi riprendi il tuo foglio.",
              "সহপাঠীর সাথে কাগজ বদলাও। তার কাগজে একটি সত্যি বাক্য লেখো: <b>«আমি তোমাকে ভালো করতে দেখেছি যখন...»</b>। তারপর নিজের কাগজ ফেরত নাও।", bn)
    c += "<h2>2. Il codice nuovo</h2>"
    c += codice("RIQUADRO 8 — file nuovo competenze.html", COMPETENZE)
    c += codice("RIQUADRO 9 — il menu: da mettere in index.html, subito dopo &lt;body&gt;", MENU)
    c += codice("RIQUADRO 10 — in fondo a style.css (solo se il menu è senza colori)", CSS_MENU, css=True)
    c += "<h2>3. I passi su GitHub, uno alla volta</h2>"
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Crea il file nuovo", "নতুন ফাইল বানাও",
           "Nel repository <b>mio-sito</b>: bottone <b>Add file</b> (grigio) &rarr; <b>Create new file</b> (Crea nuovo file). Nel campo del nome scrivi " + T("competenze.html") + ".",
           "<b>mio-sito</b> repository-তে: <b>Add file</b> বোতাম (ধূসর) &rarr; <b>Create new file</b> (নতুন ফাইল)। নামের ঘরে লেখো " + T("competenze.html") + "।")
    c += S("Incolla la pagina", "পেজ পেস্ট করো",
           "Nel riquadro grande incolla il RIQUADRO 8. Poi <b>Commit changes...</b> &rarr; <b>Commit changes</b>.",
           "বড় বাক্সে বাক্স ৮ পেস্ট করো। তারপর <b>Commit changes...</b> &rarr; <b>Commit changes</b>।")
    c += S("Fallo tuo: solo cose VERE", "নিজের মতো করো: শুধু সত্যি কথা",
           "Con la <b>matita</b> cambia la pagina usando il tuo foglio: lascia solo le competenze che hai davvero, aggiungi le tue, "
           "scrivi cosa hai imparato in questa scuola e la tua frase per un'azienda. Poi Commit.",
           "<b>পেনসিল</b> দিয়ে তোমার কাগজ দেখে পেজটি বদলাও: শুধু যে দক্ষতা সত্যিই আছে সেগুলো রাখো, নিজেরগুলো যোগ করো, "
           "এই স্কুলে কী শিখেছ আর কোম্পানির জন্য তোমার বাক্যটি লেখো। তারপর Commit।")
    c += S("Il menu nella Home", "Home-এ মেনু",
           "Apri <b>index.html</b> &rarr; <b>matita</b>. Subito dopo la riga " + T("&lt;body&gt;") + " incolla il RIQUADRO 9. Commit. "
           "Hai già la pagina della passione? Nel menu aggiungi anche la riga di passione.html.",
           "<b>index.html</b> খোলো &rarr; <b>পেনসিল</b>। " + T("&lt;body&gt;") + " লাইনের ঠিক পরে বাক্স ৯ পেস্ট করো। Commit। "
           "শখের পেজ আগে থেকেই আছে? মেনুতে passione.html-এর লাইনটিও যোগ করো।")
    c += S("Prova", "চেষ্টা করো",
           "Aspetta 1 minuto, apri il sito, " + T("Ctrl") + " + " + T("F5") + ". Clic su <b>Cosa so fare</b>, poi su <b>Home</b>. <b>FATTO! Il tuo portfolio è online.</b>",
           "১ মিনিট অপেক্ষা করো, সাইট খোলো, " + T("Ctrl") + " + " + T("F5") + "। <b>Cosa so fare</b>-এ, তারপর <b>Home</b>-এ ক্লিক করো। <b>হয়ে গেছে! তোমার পোর্টফোলিও অনলাইনে।</b>", ok=True)
    c += S("Mostralo", "দেখাও",
           "L'indirizzo è " + T("https://tuonome.github.io/mio-sito/competenze.html") + ". Leggi ad alta voce la tua frase per un'azienda, come a un colloquio: 30 secondi.",
           "ঠিকানা: " + T("https://tuonome.github.io/mio-sito/competenze.html") + "। কোম্পানির জন্য তোমার বাক্যটি জোরে পড়ো, সাক্ষাৎকারের মতো: ৩০ সেকেন্ড।", ok=True)
    c += box("warn", "<b>Pagina pubblica:</b> scrivi solo cose positive e solo il nome o il soprannome. Le cose più personali (le difficoltà, la famiglia, "
             "da dove vieni) NON vanno sul sito: le scrivi solo nel Documento di Classroom, che legge solo il prof.",
             "<b>পাবলিক পেজ:</b> শুধু ইতিবাচক কথা আর শুধু নাম বা ডাকনাম লেখো। খুব ব্যক্তিগত কথা (কষ্ট, পরিবার, কোথা থেকে এসেছ) "
             "সাইটে নয়: সেগুলো শুধু Classroom-এর Documento-তে লেখো, যা শুধু শিক্ষক পড়েন।", bn)
    c += "<h2>4. Se qualcosa non va</h2>"
    err = [("Clic su <b>Cosa so fare</b> e vedo <b>404</b>", "Il file deve chiamarsi esattamente <b>competenze.html</b> (minuscolo), come nel menu.",
            "<b>Cosa so fare</b>-এ ক্লিক করলে <b>404</b>", "ফাইলের নাম ঠিক <b>competenze.html</b> (ছোট হাতের) হতে হবে, মেনুর মতো।"),
           ("Il menu è <b>senza colori</b>", "In fondo a style.css incolla il RIQUADRO 10, poi aspetta un minuto e " + T("Ctrl") + " + " + T("F5") + ".",
            "মেনুতে <b>রং নেই</b>", "style.css-এর একদম নিচে বাক্স ১০ পেস্ট করো, তারপর এক মিনিট অপেক্ষা করে " + T("Ctrl") + " + " + T("F5") + "।"),
           ("La scheda bianca <b>non ha il bordo</b>", "Ti manca il RIQUADRO 4 di ieri: è nella pagina della classe, tra i lavori dei giorni scorsi.",
            "সাদা কার্ডে <b>বর্ডার নেই</b>", "গতকালের বাক্স ৪ নেই: ক্লাসের পেজে, আগের দিনের কাজের মধ্যে আছে।")]
    t = "<table><tr><th style='width:34%'>Problema</th><th>Soluzione</th></tr>"
    for a, b, a2, b2 in err:
        t += "<tr><td>%s%s</td><td>%s%s</td></tr>" % (a, "<div class='bn'>%s</div>" % a2 if bn else "", b, "<div class='bn'>%s</div>" % b2 if bn else "")
    c += t + "</table>"
    c += "<div class='foot'>Classe 3 · Dispensa 5 · v%s</div>" % VER
    return pagina("Dispensa 5 — Il mio sito diventa il mio portfolio", c)


def compito(bn):
    tit, tbn = "Compito 4 — Il mio portfolio: cosa so fare", "কাজ ৪ — আমার পোর্টফোলিও: আমি কী পারি"
    c = "<style>.step{margin:1.3mm 0}.step .b{padding:1.1mm 3mm}.step .h{padding:1mm 3mm}.cover{padding:5mm 8mm}table td,table th{padding:1mm 2mm}</style>"
    c += cover(tit, tbn, "Classe 3 · Informatica · %s · si consegna su Classroom · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom (c'è già il tuo nome). Lo legge <b>solo il prof</b>: puoi scrivere con sincerità.",
             "<b>কী জমা দেবে:</b> Classroom-এর কাজে আগে থেকে তৈরি <b>Documento</b> (তোমার নাম সহ)। এটি <b>শুধু শিক্ষক</b> পড়েন: মন খুলে লিখতে পারো।", bn)
    parti = [("Prima e dopo: 3 cose che oggi sai fare e a settembre no (puoi mettere la foto del foglio)",
              "আগে ও এখন: ৩টি জিনিস যা আজ পারো কিন্তু সেপ্টেম্বরে পারতে না (কাগজের ছবিও দিতে পারো)"),
             ("Le mie competenze personali: nella tabella metti un numero da 1 a 4 e un esempio VERO",
              "আমার ব্যক্তিগত দক্ষতা: টেবিলে ১ থেকে ৪ একটি সংখ্যা আর একটি সত্যি উদাহরণ লেখো"),
             ("Cosa ho imparato in questa scuola che da un'altra parte non avrei imparato, e perché",
              "এই স্কুলে কী শিখেছি যা অন্য কোথাও শিখতাম না, আর কেন"),
             ("Cosa ha scritto di me il compagno («Ti ho visto bravo quando...»)", "সহপাঠী আমার সম্পর্কে কী লিখেছে («আমি তোমাকে ভালো করতে দেখেছি যখন...»)"),
             ("Una cosa su cui voglio migliorare, e come farò", "একটি জিনিস যেখানে উন্নতি করতে চাই, আর কীভাবে করব"),
             ("Il link della pagina competenze.html e uno screenshot", "competenze.html পেজের লিংক আর একটি স্ক্রিনশট")]
    for i, (a, b) in enumerate(parti, 1):
        c += step(i, "Parte %d" % i, "অংশ %d" % i, a, b, bn)
    t = ("<h2>La tabella della parte 2</h2><p style='margin:0 0 1mm'>1 = ancora no · 2 = a volte · 3 = spesso · 4 = sempre"
         + (" <span class='bn'>১ = এখনো না · ২ = মাঝে মাঝে · ৩ = প্রায়ই · ৪ = সবসময়</span>" if bn else "")
         + "</p><table><tr><th>Competenza</th><th style='width:14mm'>1-4</th><th style='width:60mm'>Un esempio vero</th></tr>")
    for it, b in VOCI:
        t += "<tr><td>%s%s</td><td></td><td></td></tr>" % (it, " <span class='bn'>%s</span>" % b if bn else "")
    c += t + "</table>"
    val = [("Pagina competenze.html pubblicata e menu funzionante", "3"), ("Competenze con esempi veri (parte 2)", "3"),
           ("Cosa ho imparato qui: risposta pensata, con il perché", "2"), ("Come migliorerò", "1"), ("Link e screenshot", "1")]
    t = "<h2>Come viene valutato (voto in decimi)</h2><p style='margin:0 0 1mm'>Non si valuta quanto sei bravo: si valuta se sei sincero e preciso.</p><table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in val:
        t += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += t + "</table>"
    return pagina(tit, c)


def blocco_pagina(nomi):
    def bt(f, lab):
        return "<a class='bt' href='%s'>%s</a>" % (f, lab)
    def riquadro(id_, lab, testo, css=False):
        return ("<div class='cb%s'><span class='lab'>%s</span><button class='cp' data-t='%s'>Copia</button><pre id='%s'>%s</pre></div>"
                % (" css" if css else "", lab, id_, id_, E(testo)))
    return ("<!--OGGI-PORTFOLIO--><h1 style='margin-top:12px'>Giovedì 08/10 — Il mio sito diventa il mio portfolio</h1>"
            "<div class='box' style='border:3px solid #2f9e57'><p><b>Oggi:</b> 1) carta e penna: prima e dopo, cosa ho imparato qui; "
            "2) a coppie: «ti ho visto bravo quando...»; 3) la pagina <b>competenze.html</b> sul tuo sito; 4) il Documento su Classroom; "
            "5) leggi la tua frase per un'azienda, come a un colloquio.</p></div>"
            "<div class='box b1'><h2>8. Dispensa 5 — Il mio sito diventa il mio portfolio</h2><p>Le mie competenze tecniche e personali, da mostrare allo stage.</p>"
            "<div class='btns'>%s%s</div></div>"
            "<div class='box code'><h2>Il codice di oggi</h2><p>Premi <b>Copia</b>, poi su GitHub premi Ctrl + V.</p>%s%s%s%s</div>"
            "<div class='box b3'><h2>9. Compito 4 — Il mio portfolio: cosa so fare</h2><div class='btns'>%s%s</div></div>"
            "<h2 style='margin-top:20px;color:#5a6b7b'>Facoltativo per chi ha finito: anche la pagina della passione</h2><!--/OGGI-PORTFOLIO-->") % (
        bt(nomi["d5_it"], "Italiano"), bt(nomi["d5_bn"], "Italiano + বাংলা"),
        riquadro("r8", "RIQUADRO 8 — competenze.html", COMPETENZE), riquadro("r9", "RIQUADRO 9 — il menu in index.html", MENU),
        riquadro("r9b", "Hai anche passione.html? Questa riga in più nel menu", RIGA_PASSIONE),
        riquadro("r10", "RIQUADRO 10 — in fondo a style.css (se il menu è senza colori)", CSS_MENU, True),
        bt(nomi["c4p_it"], "Italiano"), bt(nomi["c4p_bn"], "Italiano + বাংলা"))


def main():
    lav = [("d5", dispensa5, "Dispensa-5-Portfolio-Competenze"), ("c4p", compito, "Compito-4-Portfolio-Cosa-So-Fare")]
    nomi = {}
    for k, fn, base in lav:
        for lin, bn in (("IT", False), ("IT-BN", True)):
            nome = "20261008_Classe-3_%s_%s_v%s.pdf" % (base, lin, VER)
            G.pdf(fn(bn), "%s-%s.html" % (base.lower(), lin), nome)
            breve = "%s-%s-v%s.pdf" % (base, lin, VER)
            shutil.copy(os.path.join(CART, nome), os.path.join(DOCS, breve))
            nomi[k + ("_bn" if bn else "_it")] = breve
            print(nome)
    p = os.path.join(DOCS, "index.html")
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"<!--OGGI-PORTFOLIO-->.*?<!--/OGGI-PORTFOLIO-->", "", s, flags=re.S)
    a = s.find("<h1 style='margin-top:12px'>Giovedì 08/10 — Il sito a due pagine</h1>")
    assert a > 0, "blocco di giovedì non trovato"
    s = s[:a] + blocco_pagina(nomi) + s[a:].replace("<h1 style='margin-top:12px'>Giovedì 08/10 — Il sito a due pagine</h1>",
                                                    "<h1 style='margin-top:8px;font-size:18px'>Il sito a due pagine (Dispensa 4)</h1>", 1)
    open(p, "w", encoding="utf-8").write(s)
    print(p)


if __name__ == "__main__":
    main()
