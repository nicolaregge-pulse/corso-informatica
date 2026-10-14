# -*- coding: utf-8 -*-
"""Pagina della lezione 3INF del 14/10/2026: «Il merge: le vostre richieste entrano nel gioco».
Percorso unico dall'alto in basso, italiano semplice con una riga di aiuto in bengalese; ogni passo fatto diventa verde
e il suo bottone si spegne (REGISTRO-ERRORI #78). Uscita: docs/compito/3inf-20261014-merge/index.html"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "docs", "compito", "3inf-20261014-merge", "index.html")
MOD = "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform"
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
V = SITO + "verifica/?b=3inf-versioning"
def T(it, bn): return '<div class="it">%s</div><div class="bn" lang="bn">%s</div>' % (it, bn)
def passo(n, k, it, bn, corpo):
    return ('<section class="passo" id="p-%s"><h2><span class="num">%d</span> %s<span class="bollo"></span><br><span class="bn" lang="bn">%s</span></h2>\n%s\n</section>\n' % (k, n, it, bn, corpo))
def modulo(k, prima, cosa_it, cosa_bn, ph):
    return ('<ol><li>' + T(cosa_it, cosa_bn) + '<textarea id="t-%s" placeholder="%s"></textarea></li>' % (k, ph) +
            '<li>' + T("Premi «Copia».", "«Copia» চাপুন (কপি)।") + '<button class="bot blu" data-copia="%s">Copia</button></li>' % k +
            '<li>' + T("Premi «Apri il Modulo»: si apre una finestra nuova.", "«Apri il Modulo» চাপুন: একটি নতুন উইন্ডো খুলবে।") +
            '<a class="bot blu" data-apri="%s" href="%s" target="_blank" rel="noopener">Apri il Modulo</a></li>' % (k, MOD) +
            '<li>' + T("Nel Modulo: nella prima casella scrivi <b>%s</b>. Nella seconda casella premi Ctrl+V. Poi premi «Invia» e torna qui." % prima,
                       "ফর্মে: প্রথম ঘরে লিখুন <b>%s</b>। দ্বিতীয় ঘরে Ctrl+V চাপুন। তারপর «Invia» (পাঠান) চাপুন এবং এখানে ফিরে আসুন।" % prima) + '</li></ol>'
            '<div class="esito" id="e-%s"></div>' % k)
P = []
P.append(passo(1, "nome", "Il tuo nome", "আপনার নাম", T("Scrivi nome e cognome e premi OK.", "নাম ও পদবি লিখে OK চাপুন।") +
  '<input type="text" id="nome" autocomplete="name" placeholder="Nome Cognome"> <button class="bot blu" id="okNome">OK</button><div class="esito" id="esNome"></div>'))
P.append(passo(2, "teoria", "Il merge: le vostre richieste sono entrate nel gioco", "মার্জ: আপনাদের অনুরোধ গেমে ঢুকেছে",
  T("Lunedì avete mandato le vostre richieste di modifica (Pull Request). Oggi il prof le ha controllate e le ha unite al gioco: questo si chiama <b>Merge</b>. Ogni richiesta unita fa nascere una <b>versione nuova</b>: v1.5, v1.6, v1.7, v1.8, v1.9, v1.10.",
    "সোমবার আপনারা পরিবর্তনের অনুরোধ (Pull Request) পাঠিয়েছিলেন। আজ শিক্ষক সেগুলো দেখে গেমের সাথে যুক্ত করেছেন: একে বলে <b>Merge</b>। প্রতিটি যুক্ত অনুরোধে একটি <b>নতুন সংস্করণ</b> তৈরি হয়।") +
  '<div class="flusso"><span>Pull Request</span><b>→</b><span>controllo del prof</span><b>→</b><span>Merge</span><b>→</b><span>versione nuova</span><b>→</b><span>changelog</span></div>' +
  T("<b>Il changelog</b> è l'elenco scritto di che cosa è cambiato in ogni versione e di chi l'ha chiesto. <b>Il backlog</b> è l'elenco delle richieste ancora da fare.",
    "<b>Changelog</b> হলো প্রতিটি সংস্করণে কী বদলেছে আর কে চেয়েছে তার লিখিত তালিকা। <b>Backlog</b> হলো যে অনুরোধগুলো এখনও করা বাকি তার তালিকা।") +
  '<div class="nota">' + T("<b>Un conflitto vero.</b> Andrea G. ha chiesto il cielo grigio. Ma in montagna Dani e Ale avevano già chiesto il cielo sereno. Non si cancella il lavoro degli altri: il cielo grigio è andato in città. Regola: <b>aggiungere sì, cancellare no</b>.",
    "<b>একটি আসল দ্বন্দ্ব।</b> Andrea G. ধূসর আকাশ চেয়েছিল, কিন্তু পাহাড়ে Dani ও Ale আগে পরিষ্কার আকাশ চেয়েছিল। অন্যের কাজ মোছা হয় না: ধূসর আকাশ শহরে গেছে। নিয়ম: <b>যোগ করা হ্যাঁ, মোছা না</b>।") + '</div>' +
  '<div class="nota">' + T("<b>Tre richieste non sono entrate:</b> erano foto di persone vere. Nel gioco pubblico non si mettono foto di persone. Si può chiedere un personaggio disegnato o descritto a parole.",
    "<b>তিনটি অনুরোধ ঢোকেনি:</b> সেগুলো আসল মানুষের ছবি ছিল। পাবলিক গেমে মানুষের ছবি দেওয়া হয় না। আঁকা বা কথায় বর্ণনা করা চরিত্র চাওয়া যায়।") + '</div>' +
  '<h3>Spiegalo in 30 secondi</h3>' + T("Dillo a voce al compagno, poi scambiatevi:", "সহপাঠীকে মুখে বলুন, তারপর জায়গা বদলান:") +
  '<ol class="frasi"><li>Tutta la classe lavora su un solo gioco: il treno blindato della 3INF.</li><li>Ognuno manda una richiesta di modifica: si chiama Pull Request.</li><li>Il prof la controlla e la unisce al gioco: è il Merge. Nasce una versione nuova.</li><li>Tutto è scritto: nel backlog le richieste, nel changelog che cosa è cambiato.</li></ol>' +
  '<div id="quiz">' + ''.join('<div class="check"><div class="it">%s</div>%s<div class="esito"></div></div>' % (q, ''.join('<button data-g="%d">%s</button>' % (1 if i == 0 else 0, o) for i, o in enumerate(opts)))
    for q, opts in [("1. Che cos'è una Pull Request?", ["Una richiesta di modifica", "Un gioco", "Una password"]),
                    ("2. Che cos'è il Merge?", ["Unire la modifica al gioco", "Cancellare il gioco", "Copiare un file"]),
                    ("3. Dove leggi che cosa è cambiato in una versione?", ["Nel changelog", "Nel backlog", "Su YouTube"]),
                    ("4. Due richieste vogliono cose diverse nello stesso posto. Che cosa si fa?", ["Si trova un posto per tutte e due", "Si cancella quella vecchia", "Si litiga"])]) + '</div>'))
P.append(passo(3, "gioca", "Gioca la versione nuova e trova le modifiche", "নতুন সংস্করণ খেলুন এবং পরিবর্তনগুলো খুঁজুন",
  T("Il gioco si apre in una finestra nuova. Gioca 3 minuti e cerca: il treno lento all'inizio, il cielo grigio in città, le rocce diverse, l'alieno verde, Tuta. Poi torna qui.",
    "গেমটি নতুন উইন্ডোতে খুলবে। ৩ মিনিট খেলুন এবং খুঁজুন: শুরুতে ধীর ট্রেন, শহরে ধূসর আকাশ, ভিন্ন পাথর, সবুজ এলিয়েন, Tuta। তারপর এখানে ফিরে আসুন।") +
  '<a class="bot" id="bGioca" href="../../giochi/treno-3inf/" target="_blank" rel="noopener">Gioca</a>'))
P.append(passo(4, "changelog", "Leggi il changelog", "Changelog পড়ুন",
  T("Si apre l'elenco di tutte le versioni. Leggi le versioni da v1.5 a v1.10: chi ha chiesto che cosa. Poi torna qui.",
    "সব সংস্করণের তালিকা খুলবে। v1.5 থেকে v1.10 পড়ুন: কে কী চেয়েছে। তারপর এখানে ফিরে আসুন।") +
  '<a class="bot" id="bChangelog" href="../../giochi/treno-3inf/versioni/" target="_blank" rel="noopener">Le versioni</a>'))
P.append(passo(5, "rev", "La tua revisione", "আপনার পর্যালোচনা",
  T("Nei lavori veri, dopo il Merge si controlla. Scrivi 2 righe: la tua richiesta è nel gioco? È fatta bene? Che cosa manca? Se la tua richiesta non c'era, scrivi che cosa ti piace o non ti piace di una versione nuova.",
    "আসল কাজে Merge-এর পরে যাচাই করা হয়। ২ লাইন লিখুন: আপনার অনুরোধ কি গেমে আছে? ঠিকমতো করা হয়েছে? কী বাকি? আপনার অনুরোধ না থাকলে, নতুন সংস্করণের কী ভালো বা খারাপ লাগল লিখুন।") +
  modulo("rev", "revisione", "Scrivi la tua revisione qui.", "এখানে আপনার পর্যালোচনা লিখুন।", "Esempio: la v1.8 con l'alieno verde è giusta, ma vorrei che fosse più veloce")))
P.append(passo(6, "pr", "Le tue nuove richieste: almeno 3 (PR1, PR2, PR3)", "আপনার নতুন অনুরোধ: অন্তত ৩টি (PR1, PR2, PR3)",
  T("<b>Oggi mandi almeno 3 richieste</b>, una alla volta: PR1, PR2, PR3. Se vuoi, anche di più. Ogni richiesta ha 4 parti: <b>Titolo</b>, <b>Cosa cambia</b>, <b>Dove</b>, <b>Perché</b>. Niente foto di persone vere. Il prof le mette nel gioco durante la lezione: guarda le versioni nuove!",
    "<b>আজ অন্তত ৩টি অনুরোধ পাঠান</b>, একবারে একটি: PR1, PR2, PR3। চাইলে আরও বেশি। প্রতিটির ৪টি অংশ: <b>শিরোনাম</b>, <b>কী বদলাবে</b>, <b>কোথায়</b>, <b>কেন</b>। আসল মানুষের ছবি নয়। শিক্ষক ক্লাস চলাকালীন সেগুলো গেমে দেবেন।") +
  '<div class="esito" id="contaPR"></div>' +
  modulo("pr", "PR", "Scrivi la richiesta con le 4 parti.", "৪টি অংশসহ অনুরোধ লিখুন।", "Titolo: ...\nCosa cambia: ...\nDove: ...\nPerché: ...")))
P.append(passo(7, "bk", "Analizza il backlog", "Backlog বিশ্লেষণ করুন",
  T("Apri il backlog: è la lista di tutte le richieste, in ordine. Trova le tue richieste: che peso hanno (1, 2, 3, 5, 8)? A che posto sono? In quale sprint entrano? Poi torna qui e rispondi.",
    "Backlog খুলুন: এটি সব অনুরোধের ক্রমানুসারে তালিকা। আপনার অনুরোধ খুঁজুন: ওজন কত (১, ২, ৩, ৫, ৮)? কত নম্বরে? কোন স্প্রিন্টে ঢুকবে? তারপর এখানে ফিরে উত্তর দিন।") +
  '<a class="bot" id="bBacklog" href="../../3inf-backlog/" target="_blank" rel="noopener">Il backlog</a>' +
  T("Rispondi a 2 domande: 1) A che posto è la tua richiesta e perché? 2) Come la faresti più leggera, per farla entrare prima in uno sprint?",
    "২টি প্রশ্নের উত্তর দিন: ১) আপনার অনুরোধ কত নম্বরে এবং কেন? ২) কীভাবে হালকা করবেন, যাতে আগে স্প্রিন্টে ঢোকে?") +
  modulo("bk", "backlog", "Scrivi le 2 risposte.", "২টি উত্তর লিখুন।", "1) La mia richiesta è al posto ... perché ...\n2) La farei più leggera così: ...")))
P.append(passo(8, "sprint", "Il ciclo Agile dal vivo", "সরাসরি Agile চক্র",
  T("Ogni 15 minuti il prof fa uno sprint: prende dal backlog le richieste più leggere, le mette nel gioco e pubblica una versione nuova. Apri la lavagna dello sprint e guarda la tua richiesta: da fare, in lavorazione, fatta. Leggi anche le 4 cerimonie: pianificazione, daily, revisione, retrospettiva.",
    "প্রতি ১৫ মিনিটে শিক্ষক একটি স্প্রিন্ট করেন: backlog থেকে হালকা অনুরোধ নিয়ে গেমে দেন এবং নতুন সংস্করণ প্রকাশ করেন। স্প্রিন্ট বোর্ড খুলে আপনার অনুরোধ দেখুন। ৪টি অনুষ্ঠানও পড়ুন: পরিকল্পনা, daily, পর্যালোচনা, retrospective।") +
  '<a class="bot" id="bSprint" href="../../3inf-sprint/" target="_blank" rel="noopener">La lavagna dello sprint</a>'))
P.append(passo(9, "rip", "Ripasso", "পুনরালোচনা",
  T("Si apre una finestra nuova: leggi le schede e fai l'allenamento. Poi torna qui.", "নতুন উইন্ডো খুলবে: কার্ডগুলো পড়ুন এবং অনুশীলন করুন। তারপর এখানে ফিরে আসুন।") +
  '<a class="bot" id="bRip" href="%s" target="_blank" rel="noopener">Ripasso</a>' % V))
P.append(passo(10, "ver", "Verifica", "পরীক্ষা",
  T("La apre il prof. Alla fine premi il bottone verde in fondo alla verifica, poi torna qui: vedrai «Verifica fatta».",
    "শিক্ষক এটি খুলবেন। শেষে পরীক্ষার নিচের সবুজ বোতাম চাপুন, তারপর এখানে ফিরে আসুন: «Verifica fatta» দেখবেন।") +
  '<a class="bot" id="bVer" href="%s&amp;modo=verifica" target="_blank" rel="noopener">Verifica</a>' % V))
P.append(passo(11, "val", "La tua valutazione e il recupero", "আপনার মূল্যায়ন এবং পুনরুদ্ধার",
  '<div id="val" class="nota">' + T("Compare qui quando il prof ha corretto la tua verifica.", "শিক্ষক আপনার পরীক্ষা দেখার পরে এখানে দেখা যাবে।") + '</div>' +
  '<a class="bot" id="bRec" href="%s&amp;modo=recupero" target="_blank" rel="noopener" hidden>Recupero</a>' % V))
P.append(passo(12, "fw", "Aiuta il prof: come miglioreresti questa lezione?", "শিক্ষককে সাহায্য করুন: এই পাঠ কীভাবে আরও ভালো করবেন?",
  T("Questo percorso fa parte del «framework della lezione»: le regole fisse che il prof usa in ogni lezione. Voi siete i primi a provarlo. Scrivi che cosa ha funzionato, che cosa era difficile o poco chiaro, e un'idea per migliorarlo.",
    "এই পথটি «পাঠের কাঠামো»-র অংশ: শিক্ষক প্রতিটি পাঠে যে নিয়ম ব্যবহার করেন। আপনারা প্রথম চেষ্টা করছেন। লিখুন কী কাজ করেছে, কী কঠিন বা অস্পষ্ট ছিল, এবং উন্নতির একটি ধারণা।") +
  modulo("fw", "framework", "Scrivi le tue note sul percorso.", "পথ সম্পর্কে আপনার মন্তব্য লিখুন।", "Ha funzionato: ...\nEra difficile: ...\nLa mia idea: ...")))
BOTTONI = [("I voti", "নম্বর", "#238636", "3inf-voti/"), ("Il backlog", "অনুরোধের তালিকা", "#1f6feb", "3inf-backlog/"), ("Il monitor della lezione", "পাঠের মনিটর", "#6e40c9", "3inf-monitor/"),
           ("Cosa è cambiato oggi nel gioco", "আজ গেমে কী বদলেছে", "#d4a017", "giochi/treno-3inf/versioni/"), ("La classifica", "র‍্যাঙ্কিং", "#b8432a", "3inf-top/"), ("La situazione della classe", "ক্লাসের অবস্থা", "#30363d", "3inf-valutazione/"), ("Il cruscotto", "ড্যাশবোর্ড", "#0b7285", "3inf-cruscotto/")]
sei = '<p class="t" style="margin:10px 0 2px">Come sta andando la lezione · পাঠ কেমন চলছে</p><div>' + ''.join('<a class="bt" style="background:%s" href="%s%s" target="_blank" rel="noopener">%s<small style="display:block;font-weight:400;font-size:13px;opacity:.9">%s</small></a>' % (c, SITO, u, t, b) for t, b, c, u in BOTTONI) + '</div>'
CSS = """:root{--bg:#fbfaf7;--fg:#111;--mu:#5d6878;--card:#fff;--bd:#d8dee6;--gi:#fff6d6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d1117;--fg:#e6edf3;--mu:#9aa6b6;--card:#161b22;--bd:#30363d;--gi:#3a3216}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:19px/1.55 system-ui,"Segoe UI",Arial,sans-serif}.w{max-width:860px;margin:0 auto;padding:16px}
h1{font-size:30px;margin:6px 0 2px}h2{font-size:22px;margin:6px 0}h3{margin:14px 0 4px}.t{color:var(--mu);font-size:16px}
.it{font-weight:600}.bn{font-family:"Noto Sans Bengali","Vrinda","Nirmala UI",sans-serif;color:var(--mu);font-size:17px}
.bt{display:inline-block;color:#fff;text-decoration:none;font-weight:700;padding:9px 13px;border-radius:9px;margin:3px 2px;font-size:16px}
.bot{display:inline-block;background:#1a7f37;color:#fff;text-decoration:none;font-weight:700;font-size:21px;padding:11px 20px;border-radius:12px;margin:8px 0;border:0;cursor:pointer;font-family:inherit}
.bot.blu{background:#1f6feb;font-size:18px;padding:9px 15px}
.nota{background:var(--gi);border-radius:8px;padding:10px 14px;margin:10px 0}ol{padding-left:26px}li{margin:0 0 12px}
textarea{font:inherit;width:100%;min-height:110px;border-radius:8px;border:2px solid var(--bd);padding:8px;background:var(--card);color:var(--fg)}
input[type=text]{font:inherit;font-size:21px;padding:8px 12px;border-radius:8px;border:2px solid var(--bd);width:min(100%,360px);background:var(--card);color:var(--fg)}
.esito{font-size:19px;font-weight:700;margin-top:6px}
.check{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:8px 12px;margin:8px 0}.check button{font:inherit;font-weight:700;border-radius:8px;border:2px solid var(--bd);background:var(--card);color:var(--fg);padding:4px 14px;margin:4px 6px 0 0;cursor:pointer}.check button.si{background:#d3f9d8;border-color:#2f9e44;color:#111}.check button.no{background:#ffe3e3;border-color:#e03131;color:#111}
.flusso{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:10px 0}.flusso span{background:var(--card);border:2px solid #6e40c9;border-radius:20px;padding:4px 12px;font-weight:700;font-size:16px}.flusso b{color:#6e40c9}
.frasi li{font-weight:600}
.passo{border:3px solid var(--bd);border-radius:14px;padding:4px 14px 12px;margin:18px 0}
.passo .num{display:inline-flex;width:38px;height:38px;border-radius:50%;background:#6e7781;color:#fff;align-items:center;justify-content:center;font-weight:800;margin-right:6px}
.passo .bollo{float:right;font-size:15px;padding:3px 10px;border-radius:8px;color:#fff;background:#6e7781}
.passo.fatto{border-color:#1a7f37}.passo.fatto .num,.passo.fatto .bollo{background:#1a7f37}
.passo.ora{border:5px solid #1f6feb}.passo.ora .num,.passo.ora .bollo{background:#1f6feb}
.spento{opacity:.4!important;pointer-events:none}"""
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lezione.js"), encoding="utf-8").read()
H = ('<!DOCTYPE html>\n<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Il merge del treno</title><style>' + CSS + '</style></head>\n<body><div class="w">\n'
     '<h1>Il merge: le vostre richieste entrano nel gioco</h1><div class="bn" lang="bn">মার্জ: আপনাদের অনুরোধ গেমে ঢুকছে</div><p class="t">3INF · 14/10/2026</p>\n' +
     sei + '\n' + '<div class="nota">' + T("Fai i passi in ordine, dall'alto in basso. Il passo da fare adesso ha il bordo blu. Quando un passo è fatto diventa verde e il suo bottone si spegne.",
                              "উপর থেকে নিচে ক্রমানুসারে ধাপগুলো করুন। এখন যে ধাপ করতে হবে তার নীল বর্ডার। ধাপ শেষ হলে সবুজ হয় এবং বোতাম বন্ধ হয়ে যায়।") + '</div>\n' +
     ''.join(P) + '\n</div>\n<script>\n' + JS + '\n</script>\n'
     '<script src="../../assistente/assistente.js" data-pagina="3inf-merge" data-lingue="it"></script>\n</body></html>\n')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(H)
print("scritto:", OUT)
