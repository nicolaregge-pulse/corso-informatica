# -*- coding: utf-8 -*-
"""Percorso 3INF 14/10/2026: ripasso, verifica, valutazione, recupero individuale. Un solo percorso dall'alto in basso;
il passo fatto diventa verde e il suo bottone si spegne. Bottoni del framework per «ripasso e verifica»:
voti, monitor, classifica, cruscotto, situazione (nero). Uscita: docs/compito/3inf-20261014-verifica/index.html"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, "docs", "compito", "3inf-20261014-verifica", "index.html")
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
V = SITO + "verifica/?b=3inf-versioning"
def T(it, bn): return '<div class="it">%s</div><div class="bn" lang="bn">%s</div>' % (it, bn)
def passo(n, k, it, bn, corpo):
    return '<section class="passo" id="p-%s"><h2><span class="num">%d</span> %s<span class="bollo"></span><br><span class="bn" lang="bn">%s</span></h2>\n%s\n</section>\n' % (k, n, it, bn, corpo)
P = [passo(1, "nome", "Il tuo nome", "আপনার নাম", T("Scrivi nome e cognome e premi OK.", "নাম ও পদবি লিখে OK চাপুন।") +
       '<input type="text" id="nome" autocomplete="name" placeholder="Nome Cognome"> <button class="bot blu" id="okNome">OK</button><div class="esito" id="esNome"></div>'),
     passo(2, "rip", "Ripasso", "পুনরালোচনা", T("Si apre una finestra nuova: leggi le schede (versioni, Pull Request, merge, backlog, sprint, cerimonie Agile) e fai l'allenamento. Poi torna qui.",
       "নতুন উইন্ডো খুলবে: কার্ড পড়ুন (সংস্করণ, Pull Request, merge, backlog, স্প্রিন্ট, Agile) এবং অনুশীলন করুন। তারপর এখানে ফিরুন।") +
       '<a class="bot" id="bRip" href="%s" target="_blank" rel="noopener">Ripasso</a>' % V),
     passo(3, "ver", "Verifica", "পরীক্ষা", T("La apre il prof. Si apre una finestra nuova. Alla fine premi il bottone verde in fondo alla verifica, poi torna qui: vedrai «Verifica fatta».",
       "শিক্ষক এটি খুলবেন। শেষে পরীক্ষার নিচের সবুজ বোতাম চাপুন, তারপর এখানে ফিরুন।") +
       '<a class="bot" id="bVer" href="%s&amp;modo=verifica" target="_blank" rel="noopener">Verifica</a>' % V),
     passo(4, "val", "La tua valutazione", "আপনার মূল্যায়ন", '<div id="val" class="nota">' + T("Compare qui quando il prof ha corretto: il voto e perché.", "শিক্ষক দেখার পরে এখানে আসবে: নম্বর এবং কেন।") + '</div>'),
     passo(5, "rec", "Il tuo recupero", "আপনার পুনরুদ্ধার", '<div id="rec" class="nota">' + T("Il recupero è fatto apposta per te, sulle domande che hai sbagliato. Compare qui quando è pronto. Alla fine c'è il voto complessivo.",
       "পুনরুদ্ধার শুধু আপনার জন্য, আপনার ভুল প্রশ্নের উপর। প্রস্তুত হলে এখানে আসবে। শেষে মোট নম্বর।") + '</div>')]
B = [("I voti", "নম্বর", "#238636", "3inf-voti/"), ("Il monitor della lezione", "পাঠের মনিটর", "#6e40c9", "3inf-monitor/"),
     ("La classifica", "র‍্যাঙ্কিং", "#b8432a", "3inf-top/"), ("Il cruscotto", "ড্যাশবোর্ড", "#0b7285", "3inf-cruscotto/"),
     ("La situazione della classe", "ক্লাসের অবস্থা", "#30363d", "3inf-valutazione/")]
sei = ('<p class="t" style="margin:10px 0 2px">Come sta andando · কেমন চলছে</p><div>' +
       ''.join('<a class="bt" style="background:%s" href="%s%s" target="_blank" rel="noopener">%s<small style="display:block;font-weight:400;font-size:13px;opacity:.9">%s</small></a>' % (c, SITO, u, t, b) for t, b, c, u in B) + '</div>')
CSS = open(os.path.join(ROOT, "classe-3", "merge-versioni", "_build", "gen_lezione_3inf_merge.py"), encoding="utf-8").read().split('CSS = """', 1)[1].split('"""', 1)[0]
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "percorso.js"), encoding="utf-8").read()
H = ('<!DOCTYPE html>\n<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ripasso e verifica</title><style>' + CSS + '</style></head>\n<body><div class="w">\n'
     '<h1>Ripasso e verifica: versioni, Pull Request, Agile</h1><div class="bn" lang="bn">পুনরালোচনা ও পরীক্ষা</div><p class="t">3INF · 14/10/2026</p>\n' + sei +
     '<div class="nota">' + T("Fai i passi in ordine, dall'alto in basso. Il passo da fare adesso ha il bordo blu. Quando un passo è fatto diventa verde e il suo bottone si spegne.",
                              "উপর থেকে নিচে ধাপগুলো করুন। এখনকার ধাপের নীল বর্ডার। শেষ হলে সবুজ হয়।") + '</div>\n' + ''.join(P) +
     '\n</div>\n<script>\n' + JS + '\n</script>\n<script src="../../assistente/assistente.js" data-pagina="3inf-verifica" data-lingue="it"></script>\n</body></html>\n')
open(OUT, "w", encoding="utf-8").write(H)
print("scritto:", OUT)
