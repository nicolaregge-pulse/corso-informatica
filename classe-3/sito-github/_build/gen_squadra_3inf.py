# -*- coding: utf-8 -*-
"""Classe 3 — giovedì 08/10/2026: «Lavoriamo come un'azienda» — il gioco della classe con fork, Pull Request, merge e versioni.

Richiesta di Nicola (08/10): tutti mettono il loro lavoro su Git, tutti fanno modifiche, poi merge e grafico delle versioni:
ingegneria del software, product e project management, lavoro diviso in pezzi. Più 15 minuti finali sulle competenze
(cosa ho imparato lavorando in squadra, cosa ho imparato qui che altrove non avrei imparato).
Repository del gioco: nicolaregge-pulse/assalto-dei-mostri (sorgente anche in progetto-gruppo/assalto-dei-mostri/).

Produce: Dispensa 6 e Compito 4 (IT e IT-BN) in classe-3/sito-github/ e docs/3inf-sito/, e mette in testa alla pagina
docs/3inf-sito/ il blocco di oggi (con «scegli il tuo PC» che prepara nome del file e mostro da copiare).
Uso:  python3 classe-3/sito-github/_build/gen_squadra_3inf.py
"""
import os, sys, re, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_sito_github as G
from gen_sito_github import pagina, cover, step, box, T, codice, E

VER = "1.0"
CART, DOCS = G.CART, G.DOCS
DATA = "08/10/2026"
REPO = "https://github.com/nicolaregge-pulse/assalto-dei-mostri"
GIOCO = "https://nicolaregge-pulse.github.io/assalto-dei-mostri/"
MOSTRO = """{
  "nome": "Gnam Gnam",
  "colore": "#ff6fb1",
  "occhi": 3,
  "corna": 1,
  "bocca": 0,
  "velocita": 2,
  "frase": "Ti mangio il Wi-Fi!",
  "immagine": false
}
"""
SQUADRE = [("REGOLE", "regole.json", "quanti colpi regge il vetro, quanto in fretta sparano i mostri, i punti",
            "ভাঙার আগে কাচ কতটা গুলি সহ্য করে, দানবরা কত দ্রুত গুলি করে, পয়েন্ট"),
           ("GRAFICA", "grafica.json", "i colori della città: cielo, luna, palazzi, finestre, strada",
            "শহরের রং: আকাশ, চাঁদ, দালান, জানালা, রাস্তা"),
           ("TESTI", "testi.json", "il titolo, le frasi di fine partita, i messaggi (anche nella tua lingua)",
            "শিরোনাম, খেলা শেষের বাক্য, বার্তা (তোমার ভাষাতেও)"),
           ("SUONI", "suoni.json", "il volume e le note della musica di vittoria",
            "ভলিউম আর জয়ের সুরের নোট")]
GLOSS = [("Repository", "la cartella del progetto su GitHub, con tutta la sua storia", "প্রজেক্টের ফোল্ডার, তার পুরো ইতিহাস সহ"),
         ("Fork", "la TUA copia del repository: lavori lì senza toccare l'originale", "রিপোজিটরির তোমার নিজের কপি"),
         ("Commit", "una modifica salvata, con il suo messaggio", "সংরক্ষিত একটি পরিবর্তন"),
         ("Pull Request", "la proposta: «prof, unisci la mia modifica al gioco»", "প্রস্তাব: «স্যার, আমার পরিবর্তন খেলায় যোগ করুন»"),
         ("Revisione", "qualcuno (o il controllo automatico) guarda la modifica prima di unirla", "যোগ করার আগে পরিবর্তনটি পরীক্ষা করা"),
         ("Merge", "unire la modifica al progetto", "পরিবর্তনটি প্রজেক্টে যোগ করা"),
         ("Conflitto", "due persone hanno cambiato la stessa riga: bisogna scegliere", "দুজন একই লাইন বদলেছে: বেছে নিতে হবে"),
         ("Issue", "un lavoro da fare, scritto nella lista del progetto (il backlog)", "করণীয় একটি কাজ, প্রজেক্টের তালিকায়"),
         ("Release", "una versione finita e numerata del gioco: v1.0, v1.1, v1.2", "খেলার শেষ করা, নম্বর দেওয়া সংস্করণ")]


def dispensa6(bn):
    c = cover("Dispensa 6 — Lavoriamo come un'azienda", "ডিসপেন্সা ৬ — চলো একটি কোম্পানির মতো কাজ করি",
              "Classe 3 · Informatica · %s · il gioco della classe: fork, Pull Request, merge, versioni · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa facciamo oggi:</b> costruiamo <b>tutti insieme</b> un gioco per il telefono, come si fa nelle aziende di software. "
             "Il lavoro è diviso in pezzi: ognuno fa il suo, lo propone con una <b>Pull Request</b>, il prof lo <b>unisce</b> (merge) e alla fine "
             "esce una <b>versione nuova</b> del gioco, con dentro il lavoro di tutti.",
             "<b>আজ আমরা কী করব:</b> সবাই মিলে ফোনের জন্য একটি খেলা বানাব, সফটওয়্যার কোম্পানির মতো। কাজটি টুকরো টুকরো ভাগ করা: "
             "প্রত্যেকে নিজের অংশ করে, <b>Pull Request</b> দিয়ে প্রস্তাব দেয়, শিক্ষক <b>যোগ করেন</b> (merge), আর শেষে সবার কাজ নিয়ে খেলার <b>নতুন সংস্করণ</b> বের হয়।", bn)
    c += "<h2>1. I ruoli, come in un'azienda</h2><table><tr><th>Ruolo</th><th>Chi</th><th>Cosa fa</th></tr>"
    ruoli = [("Product owner", "il prof", "decide cosa entra in ogni versione e fa il merge", "শিক্ষক: কী যোগ হবে ঠিক করেন, merge করেন"),
             ("Project manager", "uno per squadra, a turno", "tiene la lista dei lavori della squadra e apre la Pull Request di squadra", "প্রতি দলে একজন, পালাক্রমে: কাজের তালিকা রাখে, দলের Pull Request খোলে"),
             ("Sviluppatori", "tutti", "fanno il proprio pezzo e lo propongono", "সবাই: নিজের অংশ বানায় ও প্রস্তাব দেয়"),
             ("Revisore", "il controllo automatico + un compagno", "guarda la modifica prima del merge", "স্বয়ংক্রিয় পরীক্ষা + একজন সহপাঠী: merge-এর আগে দেখে")]
    for a, b, d, e2 in ruoli:
        c += "<tr><td><b>%s</b></td><td>%s</td><td>%s%s</td></tr>" % (a, b, d, "<div class='bn'>%s</div>" % e2 if bn else "")
    c += "</table>"
    c += "<h2>2. Il primo lavoro di tutti: il tuo mostro</h2>"
    c += codice("RIQUADRO 11 — il tuo mostro (cambia i valori!)", MOSTRO)
    c += box("note", "Il file si chiama come il tuo PC, sempre con due cifre: PC 7 → " + T("mostri/pc07.json") + ", PC 14 → " + T("mostri/pc14.json") + ". "
             "Sulla pagina della classe scegli il tuo PC: il nome del file è già pronto da copiare.",
             "ফাইলের নাম তোমার PC-র নম্বরে, সবসময় দুই অঙ্কে: PC 7 → " + T("mostri/pc07.json") + "। ক্লাসের পেজে তোমার PC বেছে নাও: ফাইলের নাম কপি করার জন্য তৈরি।", bn)
    n = 0
    def S(*a, **k):
        nonlocal n; n += 1
        return step(n, *a, bn=bn, **k)
    c += S("Apri il progetto", "প্রজেক্ট খোলো",
           "Entra su github.com con il TUO account e apri " + T(REPO) + ".",
           "তোমার অ্যাকাউন্ট দিয়ে github.com-এ ঢোকো আর খোলো " + T(REPO) + "।")
    c += S("Crea il file", "ফাইল বানাও",
           "Sopra l'elenco dei file: bottone grigio <b>Add file</b> &rarr; <b>Create new file</b>. GitHub ti dice che serve una copia tua: premi il bottone <b>verde</b> "
           "<b>Fork this repository</b> (crea la tua copia).",
           "ফাইলের তালিকার উপরে: ধূসর বোতাম <b>Add file</b> &rarr; <b>Create new file</b>। GitHub বলবে তোমার নিজের কপি লাগবে: <b>সবুজ</b> বোতাম "
           "<b>Fork this repository</b> চাপো।")
    c += S("Nome e contenuto", "নাম ও বিষয়বস্তু",
           "Nel campo del nome incolla il TUO nome di file (es. " + T("mostri/pc14.json") + "). Nel riquadro grande incolla il RIQUADRO 11.",
           "নামের ঘরে তোমার ফাইলের নাম পেস্ট করো (যেমন " + T("mostri/pc14.json") + ")। বড় বাক্সে বাক্স ১১ পেস্ট করো।")
    c += S("Fallo tuo", "নিজের মতো করো",
           "Cambia nome, colore, occhi (1-3), corna (0-1), bocca (0-2), velocità (1-3) e la frase che grida. Lascia le virgolette e le virgole come sono.",
           "নাম, রং, চোখ (১-৩), শিং (০-১), মুখ (০-২), গতি (১-৩) আর তার চিৎকারের বাক্য বদলাও। উদ্ধৃতি চিহ্ন আর কমা যেমন আছে রাখো।")
    c += S("Proponi la modifica", "পরিবর্তন প্রস্তাব করো",
           "Bottone verde <b>Commit changes...</b> &rarr; nella finestra bottone verde <b>Propose changes</b> (proponi). Poi bottone verde <b>Create pull request</b>, e ancora "
           "<b>Create pull request</b>.",
           "সবুজ বোতাম <b>Commit changes...</b> &rarr; জানালায় সবুজ বোতাম <b>Propose changes</b>। তারপর সবুজ বোতাম <b>Create pull request</b>, আবার <b>Create pull request</b>।")
    c += S("Il controllo automatico", "স্বয়ংক্রিয় পরীক্ষা",
           "Aspetta un minuto nella pagina della tua Pull Request: compare una <b>spunta verde</b> (tutto a posto) o una <b>X rossa</b>. Con la X, clic su <b>Details</b>: "
           "c'è scritto cosa sistemare (di solito una virgola). Sistema il file nella tua copia: la Pull Request si aggiorna da sola.",
           "তোমার Pull Request-এর পেজে এক মিনিট অপেক্ষা করো: <b>সবুজ টিক</b> (সব ঠিক) অথবা <b>লাল X</b> আসবে। X হলে <b>Details</b>-এ ক্লিক করো: "
           "কী ঠিক করতে হবে লেখা আছে (সাধারণত একটি কমা)। তোমার কপিতে ফাইল ঠিক করো: Pull Request নিজেই আপডেট হবে।")
    c += S("Il merge", "Merge",
           "Il prof guarda la tua Pull Request e la unisce al gioco. Quando è viola con scritto <b>Merged</b>: <b>FATTO! Il tuo mostro è nel gioco.</b> "
           "Apri " + T(GIOCO) + " e cercalo nell'elenco dei mostri della classe.",
           "শিক্ষক তোমার Pull Request দেখে খেলায় যোগ করবেন। বেগুনি হয়ে <b>Merged</b> লেখা এলে: <b>হয়ে গেছে! তোমার দানব খেলায় আছে।</b> "
           "খোলো " + T(GIOCO) + " আর ক্লাসের দানবদের তালিকায় খুঁজে দেখো।", ok=True)
    c += "<h2>3. Il lavoro di squadra</h2><table><tr><th>Squadra</th><th>File</th><th>Cosa cambia</th></tr>"
    for sq, f, it, b in SQUADRE:
        c += "<tr><td><b>%s</b></td><td>%s</td><td>%s%s</td></tr>" % (sq, T(f), it, "<div class='bn'>%s</div>" % b if bn else "")
    c += "</table>"
    passi = [("Il project manager apre la <b>Issue</b> della squadra (scheda <b>Issues</b> del progetto) e scrive nei commenti chi fa cosa.",
              "প্রজেক্ট ম্যানেজার দলের <b>Issue</b> খোলে (<b>Issues</b> ট্যাব) আর মন্তব্যে কে কী করবে লেখে।"),
             ("La squadra decide su carta i valori nuovi (colori, frasi, regole).", "দল কাগজে নতুন মান ঠিক করে (রং, বাক্য, নিয়ম)।"),
             ("Il project manager cambia il file della squadra con la <b>matita</b> e fa la Pull Request, come per il mostro. Negli <b>autori</b> scrive solo i numeri dei PC.",
              "প্রজেক্ট ম্যানেজার <b>পেনসিল</b> দিয়ে দলের ফাইল বদলায় আর Pull Request করে, দানবের মতোই। <b>autori</b>-তে শুধু PC নম্বর লেখে।"),
             ("Un compagno di un'altra squadra fa la <b>revisione</b>: nella Pull Request, scheda <b>Files changed</b>, guarda le modifiche e scrive un commento.",
              "অন্য দলের একজন <b>রিভিউ</b> করে: Pull Request-এ <b>Files changed</b> ট্যাবে পরিবর্তন দেখে মন্তব্য লেখে।")]
    for a, b in passi:
        c += S("Squadra", "দল", a, b)
    c += box("warn", "<b>Il conflitto:</b> se due persone cambiano la stessa riga dello stesso file, GitHub non sa quale tenere. Non è un disastro: "
             "succede in tutte le aziende. Il prof ve lo fa vedere alla lavagna e lo risolve con voi.",
             "<b>কনফ্লিক্ট:</b> দুজন একই ফাইলের একই লাইন বদলালে GitHub জানে না কোনটি রাখবে। এটা বিপদ নয়: সব কোম্পানিতে হয়। শিক্ষক বোর্ডে দেখিয়ে তোমাদের সাথে সমাধান করবেন।", bn)
    c += "<h2>4. La versione nuova e il grafico</h2>"
    c += S("La release", "রিলিজ",
           "Quando i lavori sono uniti, il prof pubblica la <b>release v1.1</b> (i mostri della classe) e poi la <b>v1.2</b> (le squadre). Il numero in basso a destra nel gioco cambia.",
           "কাজগুলো যোগ হলে শিক্ষক <b>v1.1 রিলিজ</b> (ক্লাসের দানব) আর পরে <b>v1.2</b> (দলগুলোর কাজ) প্রকাশ করেন। খেলার নিচে ডানদিকের নম্বর বদলায়।")
    c += S("Il grafico delle versioni", "সংস্করণের গ্রাফ",
           "Nel progetto: scheda <b>Insights</b> &rarr; a sinistra <b>Network</b>. Vedi tutte le copie (fork), i commit e i merge: è la storia del lavoro di tutti.",
           "প্রজেক্টে: <b>Insights</b> ট্যাব &rarr; বাঁদিকে <b>Network</b>। সব কপি (fork), commit আর merge দেখবে: সবার কাজের ইতিহাস।", ok=True)
    c += box("note", "<b>Carta e penna:</b> disegna il grafico delle versioni del gioco: la linea principale (main) da v1.0 a v1.2, la tua copia che parte, il tuo commit, "
             "la freccia del merge che torna nella linea principale.",
             "<b>কাগজ-কলম:</b> খেলার সংস্করণের গ্রাফ আঁকো: মূল লাইন (main) v1.0 থেকে v1.2, তোমার কপি যেখান থেকে শুরু, তোমার commit, আর merge-এর তীর যা মূল লাইনে ফেরে।", bn)
    c += "<h2>5. Le parole del mestiere</h2><table><tr><th style='width:30mm'>Parola</th><th>Cosa vuol dire</th></tr>"
    for a, b, d in GLOSS:
        c += "<tr><td><b>%s</b></td><td>%s%s</td></tr>" % (a, b, "<div class='bn'>%s</div>" % d if bn else "")
    c += "</table><div class='foot'>Classe 3 · Dispensa 6 · v%s</div>" % VER
    return pagina("Dispensa 6 — Lavoriamo come un'azienda", c)


def compito(bn):
    tit, tbn = "Compito 4 — Il gioco della classe: lavoriamo come un'azienda", "কাজ ৪ — ক্লাসের খেলা: কোম্পানির মতো কাজ"
    c = "<style>.step{margin:1.3mm 0}.step .b{padding:1.1mm 3mm}.step .h{padding:1mm 3mm}.cover{padding:5mm 8mm}table td,table th{padding:1mm 2mm}</style>"
    c += cover(tit, tbn, "Classe 3 · Informatica · %s · si consegna su Classroom · %s" % (DATA, "IT / বাংলা" if bn else "italiano"), bn)
    c += box("goal", "<b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom. Le ultime due parti le legge solo il prof: scrivi con sincerità.",
             "<b>কী জমা দেবে:</b> Classroom-এর কাজে তৈরি <b>Documento</b>। শেষ দুটি অংশ শুধু শিক্ষক পড়েন: মন খুলে লেখো।", bn)
    parti = [("Il link della TUA Pull Request del mostro e uno screenshot con la spunta verde (o con Merged)",
              "তোমার দানবের Pull Request-এর লিংক আর সবুজ টিক (বা Merged) সহ স্ক্রিনশট"),
             ("La tua squadra, il tuo ruolo e cosa hai fatto (link della Pull Request di squadra o del tuo commento di revisione)",
              "তোমার দল, তোমার ভূমিকা আর তুমি কী করেছ (দলের Pull Request বা তোমার রিভিউ মন্তব্যের লিংক)"),
             ("Foto del grafico delle versioni disegnato a mano e spiegalo: cosa sono fork, Pull Request e merge?",
              "হাতে আঁকা সংস্করণের গ্রাফের ছবি আর ব্যাখ্যা: fork, Pull Request আর merge কী?"),
             ("Lavorare in squadra: nella tabella metti un numero da 1 a 4 e un esempio vero di oggi",
              "দলে কাজ: টেবিলে ১ থেকে ৪ একটি সংখ্যা আর আজকের একটি সত্যি উদাহরণ"),
             ("Cosa ho imparato in questa scuola che da un'altra parte non avrei imparato, e perché",
              "এই স্কুলে কী শিখেছি যা অন্য কোথাও শিখতাম না, আর কেন")]
    for i, (a, b) in enumerate(parti, 1):
        c += step(i, "Parte %d" % i, "অংশ %d" % i, a, b, bn)
    voci = [("Ho collaborato con la squadra", "দলের সাথে সহযোগিতা করেছি"), ("Ho rispettato il lavoro degli altri (non ho toccato i loro file)", "অন্যদের কাজকে সম্মান করেছি"),
            ("Ho spiegato le mie idee e ascoltato quelle degli altri", "নিজের ধারণা বলেছি আর অন্যদেরটা শুনেছি"), ("Ho chiesto aiuto o aiutato un compagno", "সাহায্য চেয়েছি বা করেছি"),
            ("Ho rispettato i tempi della squadra", "দলের সময় মেনে চলেছি")]
    t = ("<h2>La tabella della parte 4</h2><p style='margin:0 0 1mm'>1 = ancora no · 2 = a volte · 3 = spesso · 4 = sempre</p>"
         "<table><tr><th>Competenza</th><th style='width:14mm'>1-4</th><th style='width:60mm'>Un esempio vero di oggi</th></tr>")
    for it, b in voci:
        t += "<tr><td>%s%s</td><td></td><td></td></tr>" % (it, " <span class='bn'>%s</span>" % b if bn else "")
    c += t + "</table>"
    val = [("Pull Request del mostro con la spunta verde", "3"), ("Lavoro di squadra o revisione, con il link", "2"),
           ("Grafico delle versioni disegnato e spiegato", "2"), ("Tabella con esempi veri", "2"), ("Cosa ho imparato qui", "1")]
    t = "<h2>Come viene valutato (voto in decimi)</h2><table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in val:
        t += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += t + "</table>"
    return pagina(tit, c)


def blocco_pagina(nomi):
    def bt(f, lab):
        return "<a class='bt' href='%s'>%s</a>" % (f, lab)
    def riquadro(id_, lab, testo):
        return ("<div class='cb'><span class='lab'>%s</span><button class='cp' data-t='%s'>Copia</button><pre id='%s'>%s</pre></div>" % (lab, id_, id_, E(testo)))
    opz = "".join("<option value='%02d'>PC %d</option>" % (i, i) for i in range(1, 41))
    js = ("<script>function scegliPC(v){var f='mostri/pc'+v+'.json';document.getElementById('rpc').textContent=f;"
          "document.getElementById('pcScelto').hidden=!v;try{localStorage.setItem('pc-3inf-gioco',v)}catch(e){}}"
          "(function(){var v='';try{v=localStorage.getItem('pc-3inf-gioco')||''}catch(e){}if(v){document.getElementById('selPC').value=v;scegliPC(v)}})();</script>")
    return ("<!--OGGI-SQUADRA--><h1 style='margin-top:12px'>Giovedì 08/10 — Il gioco della classe: lavoriamo come un'azienda</h1>"
            "<div class='box' style='border:3px solid #2f9e57'><p><b>Oggi:</b> 1) il tuo mostro con una Pull Request; 2) il lavoro della tua squadra; "
            "3) il merge e la versione nuova; 4) il grafico delle versioni; 5) ultimi 15 minuti: cosa ho imparato lavorando in squadra.</p>"
            "<div class='btns'><a class='bt' style='background:#12467a;color:#fff' href='" + REPO + "'>Il progetto su GitHub</a><a class='bt' style='background:#2f9e57;color:#fff' href='" + GIOCO + "'>Gioca!</a></div></div>"
            "<div class='box b1'><h2>10. Dispensa 6 — Lavoriamo come un'azienda</h2><p>Ruoli, fork, Pull Request, merge, versioni, grafico.</p><div class='btns'>%s%s</div></div>"
            "<div class='box code'><h2>Il tuo mostro</h2><p><b>1. Scegli il tuo PC:</b> <select id='selPC' onchange='scegliPC(this.value)' style='font-size:18px;padding:6px'>"
            "<option value=''>— scegli —</option>%s</select></p><div id='pcScelto' hidden>%s</div>%s</div>"
            "<div class='box b3'><h2>11. Compito 4 — Il gioco della classe</h2><div class='btns'>%s%s</div></div>"
            "<h2 style='margin-top:20px;color:#5a6b7b'>Per un'altra volta: il portfolio «Cosa so fare»</h2><!--/OGGI-SQUADRA-->") % (
        bt(nomi["d6_it"], "Italiano"), bt(nomi["d6_bn"], "Italiano + বাংলা"), opz,
        "<div class='cb'><span class='lab'>2. Il nome del TUO file</span><button class='cp' data-t='rpc'>Copia</button><pre id='rpc'></pre></div>",
        riquadro("r11", "3. RIQUADRO 11 — il tuo mostro (poi cambia i valori)", MOSTRO) + js,
        bt(nomi["c4s_it"], "Italiano"), bt(nomi["c4s_bn"], "Italiano + বাংলা"))


def main():
    lav = [("d6", dispensa6, "Dispensa-6-Lavoriamo-Come-Azienda"), ("c4s", compito, "Compito-4-Gioco-Della-Classe")]
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
    s = re.sub(r"<!--OGGI-SQUADRA-->.*?<!--/OGGI-SQUADRA-->", "", s, flags=re.S)
    a = s.find("<!--OGGI-PORTFOLIO-->")
    assert a > 0, "blocco del portfolio non trovato"
    s = s[:a] + blocco_pagina(nomi) + s[a:]
    s = s.replace("<h1 style='margin-top:12px'>Giovedì 08/10 — Il mio sito diventa il mio portfolio</h1>",
                  "<h1 style='margin-top:8px;font-size:18px'>Il mio sito diventa il mio portfolio (Dispensa 5)</h1>", 1)
    open(p, "w", encoding="utf-8").write(s)
    print(p)


if __name__ == "__main__":
    main()
