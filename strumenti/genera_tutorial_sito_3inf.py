# -*- coding: utf-8 -*-
"""Tutorial 3INF «Il mio sito: Stage e Presenze» (v1.1, 18/11/2026; sostituisce la v1.0 del 17/11).
Una sola fonte (questo file) per tre uscite:
  1. docs/3inf/sito-stage/index.html   pagina guidata a bottoni («Ho fatto»), con controllo della cartella
  2. classe-3/sito-stage/*-IT.md       per il PDF solo italiano
  3. classe-3/sito-stage/*-IT-BN.md    per il PDF italiano + una riga in bangla sotto ogni frase (allievo del PC 14)
I riquadri di codice sono LETTI dai file del modello (docs/3inf/sito-stage/modello/): tutorial e modello non si possono scostare.
Niente Git ne' GitHub per gli allievi (decisione del docente, 17/11/2026): il sito e' una cartella di file sul PC.
Uso: python3 strumenti/genera_tutorial_sito_3inf.py   (poi: MD2PDF_ARIOSO=1 python3 strumenti/md2pdf.py ...)"""
import html, os, json

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITO = os.path.join(RADICE, "docs/3inf/sito-stage")
MODELLO = os.path.join(SITO, "modello")
MDDIR = os.path.join(RADICE, "classe-3/sito-stage")
VERSIONE, DATA = "1.1", "18/11/2026"
URL_COPIA = "https://nicolaregge-pulse.github.io/corso-informatica/stage/copia.html"


def codice(nome):
    return open(os.path.join(MODELLO, nome), encoding="utf-8").read().rstrip("\n")


SALVA = ("Salva con nome: cartella sito-personale, nome {n}, tipo Tutti i file, codifica UTF-8. Premi Salva.",
         "Salva con nome চাপো: ফোল্ডার sito-personale, নাম {n}, ধরন Tutti i file, কোডিং UTF-8। Salva চাপো।")

# Ogni passo: id, titolo (it, bn), frasi [(it, bn)], riquadri [(etichetta, testo)], immagine (file, didascalia) | None, extra | None, fallo_tuo [(it,bn)]
P = []


def passo(**k):
    P.append(k)


passo(id="albero", t=("Il tuo sito è una cartella", "তোমার সাইট একটি ফোল্ডার"),
      f=[("Il tuo sito è una cartella sul PC.", "তোমার সাইট পিসির একটি ফোল্ডার।"),
         ("Dentro ci sono dei file: pagine, colori e foto.", "ভেতরে ফাইল আছে: পেজ, রং আর ছবি।"),
         ("Li apri con il browser. Per guardare le pagine non serve internet.", "ব্রাউজার দিয়ে খোলো। পেজ দেখতে ইন্টারনেট লাগে না।"),
         ("Tutti i siti hanno gli stessi nomi: così il prof trova subito ogni cosa.", "সব সাইটে একই নাম থাকে: তাই স্যার সবকিছু সহজে খুঁজে পান।")],
      img=("s-albero.png", "Lo schema del sito"), btn="Ho letto")

passo(id="cartella", t=("Crea la cartella", "ফোল্ডার বানাও"),
      f=[("Apri Esplora file. Vai nella cartella dove salvi i tuoi lavori (il prof ti dice quale).", "ফাইল এক্সপ্লোরার খোলো। যেখানে কাজ সেভ করো সেই ফোল্ডারে যাও (স্যার বলে দেবেন কোনটা)।"),
         ("Fai clic destro su un punto vuoto, poi Nuovo, poi Cartella.", "ফাঁকা জায়গায় রাইট-ক্লিক করো, তারপর Nuovo, তারপর Cartella।"),
         ("Scrivi questo nome (tutto minuscolo, senza spazi) e premi Invio.", "এই নামটি লেখো (সব ছোট হাতের অক্ষর, ফাঁকা ছাড়া) আর Invio চাপো।")],
      box=[("NOME 1 — la cartella del sito", "sito-personale")],
      f2=[("Apri la cartella sito-personale. Dentro crea un'altra cartella con questo nome.", "sito-personale ফোল্ডারটি খোলো। তার ভেতরে এই নামে আরেকটি ফোল্ডার বানাও।")],
      box2=[("NOME 2 — la cartella delle foto", "img")])

passo(id="css", t=("Il file style.css (i colori)", "style.css ফাইল (রং)"),
      f=[("Apri il Blocco note: premi il tasto Windows, scrivi Blocco note e premi Invio.", "Blocco note খোলো: Windows বোতাম চাপো, Blocco note লেখো, Invio চাপো।"),
         ("Premi Copia sul riquadro qui sotto. Nel Blocco note premi Ctrl + V.", "নিচের বাক্সে Copia চাপো। Blocco note-এ Ctrl + V চাপো।"),
         ("Premi File, poi Salva con nome.", "File চাপো, তারপর Salva con nome।"),
         ("Compila la finestra come nel disegno. Poi premi Salva.", "ছবির মতো জানালা ভরো। তারপর Salva চাপো।")],
      files=["style.css"], img=("s-salva.png", "La finestra Salva con nome"), nome_file="style.css")

passo(id="index", t=("La pagina Chi sono (index.html)", "Chi sono পেজ (index.html)"),
      f=[("Nel Blocco note premi Ctrl + N: si apre un foglio vuoto.", "Blocco note-এ Ctrl + N চাপো: একটি ফাঁকা পাতা খুলবে।"),
         ("Premi Copia sul riquadro. Nel foglio vuoto premi Ctrl + V.", "বাক্সে Copia চাপো। ফাঁকা পাতায় Ctrl + V চাপো।"),
         SALVA, ("Apri la cartella sito-personale. Fai doppio clic su index.html: si apre nel browser.", "sito-personale ফোল্ডার খোলো। index.html-এ ডাবল ক্লিক করো: ব্রাউজারে খুলবে।")],
      files=["index.html"], nome_file="index.html", img=("s-index.png", "La pagina Chi sono nel browser"),
      fallo=[("Fallo tuo. Nel Blocco note cambia Esempio E. con il tuo nome e le frasi con le tue. Premi Ctrl + S. Nel browser premi F5.", "নিজের মতো করো। Blocco note-এ Esempio E. বদলে নিজের নাম লেখো, বাক্যগুলোও নিজের লেখো। Ctrl + S চাপো। ব্রাউজারে F5 চাপো।"),
             ("Vuoi altri colori? Apri style.css e cambia i tre colori in cima, dopo i due punti.", "অন্য রং চাও? style.css খোলো, উপরের তিনটি রং দুই ফোঁটার পরে বদলাও।")])

passo(id="passione", t=("La pagina Hobby (passione.html)", "Hobby পেজ (passione.html)"),
      f=[("Premi Ctrl + N nel Blocco note. Premi Copia sul riquadro e poi Ctrl + V.", "Blocco note-এ Ctrl + N চাপো। বাক্সে Copia চাপো, তারপর Ctrl + V।"),
         SALVA, ("Apri passione.html con doppio clic.", "passione.html-এ ডাবল ক্লিক করে খোলো।")],
      files=["passione.html"], nome_file="passione.html", img=("s-passione.png", "La pagina Hobby"),
      fallo=[("Fallo tuo. Scrivi il tuo hobby vero e perché ti piace.", "নিজের মতো করো। তোমার সত্যিকারের শখ আর কেন ভালো লাগে তা লেখো।")])

passo(id="competenze", t=("La pagina Competenze (competenze.html)", "Competenze পেজ (competenze.html)"),
      f=[("Premi Ctrl + N nel Blocco note. Premi Copia sul riquadro e poi Ctrl + V.", "Blocco note-এ Ctrl + N চাপো। বাক্সে Copia চাপো, তারপর Ctrl + V।"),
         SALVA, ("Apri competenze.html con doppio clic.", "competenze.html-এ ডাবল ক্লিক করে খোলো।")],
      files=["competenze.html"], nome_file="competenze.html", img=("s-competenze.png", "La pagina Competenze"),
      fallo=[("Fallo tuo. Nella tabella scrivi tre cose che sai fare davvero e cosa hai fatto.", "নিজের মতো করো। টেবিলে তিনটি জিনিস লেখো যা তুমি সত্যিই পারো, আর কী করেছ।")])

passo(id="stage", t=("La pagina Il mio stage (diario.html)", "Il mio stage পেজ (diario.html)"),
      f=[("Premi Ctrl + N nel Blocco note. Premi Copia sul riquadro e poi Ctrl + V.", "Blocco note-এ Ctrl + N চাপো। বাক্সে Copia চাপো, তারপর Ctrl + V।"),
         SALVA, ("Apri diario.html con doppio clic.", "diario.html-এ ডাবল ক্লিক করে খোলো।")],
      files=["diario.html"], nome_file="diario.html", img=("s-diario.png", "La pagina Il mio stage"),
      fallo=[("Fallo tuo. Scrivi dove fai lo stage, che cosa fai e che cosa vuoi imparare.", "নিজের মতো করো। স্টেজ কোথায় করছ, কী করছ, কী শিখতে চাও তা লেখো।"),
             ("Se non lo sai ancora, scrivi «da definire» e torna a cambiarlo dopo.", "এখনো না জানলে «da definire» লেখো, পরে এসে বদলাও।")])

passo(id="menu", t=("Prova il menu", "মেনু পরীক্ষা করো"),
      f=[("Apri index.html. In alto ci sono cinque bottoni blu.", "index.html খোলো। উপরে পাঁচটি নীল বোতাম আছে।"),
         ("Premi Hobby, Competenze, Il mio stage e poi Chi sono: passi da una pagina all'altra.", "Hobby, Competenze, Il mio stage, তারপর Chi sono চাপো: এক পেজ থেকে অন্য পেজে যাবে।"),
         ("Presenze ancora non funziona: lo facciamo nei prossimi passi.", "Presenze এখনো চলবে না: পরের ধাপে বানাব।")],
      btn="Funziona il menu")

passo(id="presenze", t=("Presenze stage: prendi la pagina", "Presenze stage: পেজটি নাও"),
      f=[("Apri la pagina «Copia la pagina Presenze stage».", "«Copia la pagina Presenze stage» পেজটি খোলো।"),
         ("Scegli il tuo nome nell'elenco.", "তালিকা থেকে তোমার নাম বেছে নাও।"),
         ("Premi il bottone blu «2. Scarica il file presenze.html».", "নীল বোতাম «2. Scarica il file presenze.html» চাপো।"),
         ("Apri la cartella Download. Taglia il file presenze.html con Ctrl + X.", "Download ফোল্ডার খোলো। presenze.html ফাইলটি Ctrl + X দিয়ে কাটো।"),
         ("Apri la cartella sito-personale e incolla il file con Ctrl + V.", "sito-personale ফোল্ডার খোলো আর Ctrl + V দিয়ে ফাইলটি রাখো।")],
      extra="link_copia")

passo(id="password", t=("Presenze stage: la tua password", "Presenze stage: তোমার পাসওয়ার্ড"),
      f=[("Fai doppio clic su presenze.html. Premi il bottone «Modifica (solo io)».", "presenze.html-এ ডাবল ক্লিক করো। «Modifica (solo io)» বোতাম চাপো।"),
         ("Scegli una password di almeno 8 caratteri e scrivila due volte. Ricordala: la dimentichi, la azzera solo il prof.", "কমপক্ষে ৮ অক্ষরের একটি পাসওয়ার্ড বেছে দুইবার লেখো। মনে রাখো: ভুলে গেলে শুধু স্যার আবার শুরু করতে পারেন।"),
         ("Premi «Entra». In alto leggi «Modifica».", "«Entra» চাপো। উপরে «Modifica» লেখা দেখবে।")],
      img=("s-presenze-password.png", "La pagina Presenze: scelta della password"))

passo(id="giorno", t=("Presenze stage: segna un giorno", "Presenze stage: একটি দিন চিহ্নিত করো"),
      f=[("Premi il numero del giorno nel calendario. Lo stage va dal 23/11/2026 al 18/02/2027, da lunedì a sabato.", "ক্যালেন্ডারে দিনের নম্বরে চাপো। স্টেজ ২৩/১১/২০২৬ থেকে ১৮/০২/২০২৭, সোমবার থেকে শনিবার।"),
         ("Premi «Presente». Scrivi le ore.", "«Presente» চাপো। ঘণ্টা লেখো।"),
         ("In «Che cosa hai fatto» scrivi poche parole: ogni giorno di presenza ha la sua nota.", "«Che cosa hai fatto»-তে অল্প কথায় লেখো: প্রতিটি উপস্থিতির দিনের একটি নোট থাকে।"),
         ("Premi «Salva il giorno». Il giorno diventa verde.", "«Salva il giorno» চাপো। দিনটি সবুজ হবে।")],
      img=("s-presenze-giorno.png", "Il giorno: Presente, ore e nota"), img2=("s-presenze-calendario.png", "Il calendario con tre giorni segnati"))

passo(id="copia", t=("Presenze stage: la copia di sicurezza", "Presenze stage: নিরাপত্তার কপি"),
      f=[("I giorni restano nel browser di questo PC. Per non perderli salva un file.", "দিনগুলো এই পিসির ব্রাউজারে থাকে। হারিয়ে না যাওয়ার জন্য একটি ফাইল সেভ করো।"),
         ("Premi «Scarica i dati (file)». Metti il file presenze-stage.json nella cartella sito-personale.", "«Scarica i dati (file)» চাপো। presenze-stage.json ফাইলটি sito-personale ফোল্ডারে রাখো।"),
         ("Se cambi PC o browser: apri presenze.html, premi «Modifica (solo io)» e poi «Carica il mio file».", "পিসি বা ব্রাউজার বদলালে: presenze.html খোলো, «Modifica (solo io)» চাপো, তারপর «Carica il mio file»।"),
         ("Quando il prof attiva il servizio condiviso, ogni «Salva il giorno» arriva anche a lui. Il prof ti dice quando.", "স্যার যখন শেয়ার্ড সার্ভিস চালু করবেন, প্রতিটি «Salva il giorno» তাঁর কাছেও যাবে। কখন, স্যার বলবেন।")],
      btn="Ho salvato il file")

passo(id="foto", t=("Una tua foto (se vuoi)", "তোমার একটি ছবি (ইচ্ছা হলে)"),
      f=[("Metti una tua foto nella cartella img. Chiamala foto.jpg. Usa solo foto che vuoi far vedere.", "img ফোল্ডারে তোমার একটি ছবি রাখো। নাম দাও foto.jpg। শুধু সেই ছবি দাও যা দেখাতে চাও।"),
         ("In index.html, sotto la riga con Ciao, sono, aggiungi questa riga. Premi Ctrl + S.", "index.html-এ «Ciao, sono» লাইনের নিচে এই লাইনটি যোগ করো। Ctrl + S চাপো।")],
      box=[("RIGA — la tua foto in index.html", '<img src="img/foto.jpg" alt="La mia foto">')], btn="Fatto (o salto)")

passo(id="controllo", t=("Controlla la tua cartella", "তোমার ফোল্ডার পরীক্ষা করো"),
      f=[("Premi il bottone «Scegli la cartella sito-personale» e scegli la tua cartella.", "«Scegli la cartella sito-personale» বোতাম চাপো আর তোমার ফোল্ডার বেছে নাও।"),
         ("Ogni riga ha una spunta verde o una croce rossa. Sotto la croce c'è come si sistema.", "প্রতিটি লাইনে সবুজ টিক বা লাল ক্রস আছে। ক্রসের নিচে কীভাবে ঠিক করবে লেখা আছে।"),
         ("Il controllo legge la cartella solo sul tuo PC e non manda niente a nessuno.", "পরীক্ষা শুধু তোমার পিসিতে ফোল্ডার পড়ে, কাউকে কিছু পাঠায় না।")],
      extra="checker", btn="Tutto verde")

passo(id="consegna", t=("Consegna il sito", "সাইট জমা দাও"),
      f=[("Fai clic destro sulla cartella sito-personale. Premi Invia a, poi Cartella compressa.", "sito-personale ফোল্ডারে রাইট-ক্লিক করো। Invia a চাপো, তারপর Cartella compressa।"),
         ("Si crea il file sito-personale.zip accanto alla cartella.", "ফোল্ডারের পাশে sito-personale.zip ফাইল তৈরি হবে।"),
         ("Apri Classroom e il compito di consegna che ti indica il prof. Premi Aggiungi o crea, poi File.", "Classroom আর স্যারের বলা জমার কাজটি খোলো। Aggiungi o crea চাপো, তারপর File।"),
         ("Scegli sito-personale.zip e premi Consegna.", "sito-personale.zip বেছে নাও আর Consegna চাপো।")],
      btn="Consegnato")

PROBLEMI = [
    ("Il file si chiama style.css.txt", "Nel Salva con nome il Tipo deve essere «Tutti i file». Riapri il Salva con nome e correggi il nome."),
    ("La pagina è senza colori", "Manca il file style.css nella cartella, oppure ha un nome diverso. Premi F5 nel browser."),
    ("Le lettere strane (è diventa Ã¨)", "Nel Salva con nome la Codifica deve essere UTF-8."),
    ("Un bottone del menu dà «file non trovato»", "Quel file non c'è ancora nella cartella o ha un nome diverso. I nomi sono tutti minuscoli, senza spazi."),
    ("Presenze: «Modifica (solo io)» non entra", "La password è sbagliata. Riprova. Se l'hai dimenticata, la azzera solo il prof."),
    ("Presenze: ho cambiato PC e i giorni non ci sono", "Apri presenze.html, «Modifica (solo io)», poi «Carica il mio file» e scegli presenze-stage.json."),
]
PROBLEMI_BN = [
    "Tipo অবশ্যই «Tutti i file» হতে হবে। Salva con nome আবার খুলে নাম ঠিক করো।",
    "ফোল্ডারে style.css নেই বা নাম আলাদা। ব্রাউজারে F5 চাপো।",
    "Salva con nome-এ Codifica অবশ্যই UTF-8 হতে হবে।",
    "ফাইলটি এখনো ফোল্ডারে নেই বা নাম আলাদা। সব নাম ছোট হাতের অক্ষরে, ফাঁকা ছাড়া।",
    "পাসওয়ার্ড ভুল। আবার চেষ্টা করো। ভুলে গেলে স্যারকে বলো আবার শুরু করতে।",
    "presenze.html খোলো, «Modifica (solo io)», তারপর «Carica il mio file» চাপো আর presenze-stage.json বেছে নাও।",
]
BN_TITOLO = "টিউটোরিয়াল: আমার সাইট, স্টেজ ও উপস্থিতি"

N = len(P)


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- Markdown (PDF)
def md(bn):
    o = [f"# Tutorial 3INF — Il mio sito: Stage e Presenze", "", f"**Versione {VERSIONE}** — {DATA} · Classe 3 · Laboratorio · " + ("italiano + bangla (PC 14)" if bn else "italiano"), ""]
    if bn: o += [BN_TITOLO, ""]
    intro = [("Alla fine hai un sito uguale a quello dei compagni: Chi sono, Hobby, Competenze, Il mio stage e Presenze.", "শেষে তোমার সাইট বন্ধুদের মতোই হবে: Chi sono, Hobby, Competenze, Il mio stage, Presenze।"),
             ("Lavori con due programmi: il Blocco note e il browser. Non installi niente.", "তুমি দুটি প্রোগ্রামে কাজ করবে: Blocco note আর ব্রাউজার। কিছু ইনস্টল করতে হবে না।")]
    for it, b in intro:
        o += [it, ""]
        if bn: o += [b, ""]
    o += ["> **Nota:** in ogni passo fai UNA cosa. Quando hai fatto, vai al passo dopo.", ""]
    n = 0
    for s in P:
        n += 1
        o += ["<<PAGINA>>", "", f"## Passo {n} di {N}: {s['t'][0]}", ""]
        if bn: o += [s["t"][1], ""]
        k = 0

        def frasi(lista, k):
            for it, b in lista:
                k += 1
                it = it.format(n=s.get("nome_file", ""))
                b = b.format(n=s.get("nome_file", ""))
                o.extend([f"{k}. {it}", ""])
                if bn: o.extend([b, ""])
            return k
        k = frasi(s.get("f", []), k)
        for etichetta, testo in s.get("box", []):
            o += [f"**{etichetta}**", "", "```", testo, "```", ""]
        k = frasi(s.get("f2", []), k)
        for etichetta, testo in s.get("box2", []):
            o += [f"**{etichetta}**", "", "```", testo, "```", ""]
        if s.get("extra") == "link_copia":
            o += ["**Indirizzo della pagina «Copia la pagina Presenze stage»** (scrivilo nella barra del browser)", "", "```", URL_COPIA, "```", ""]
        if s.get("extra") == "checker":
            o += ["> **Nota:** il controllo è nella pagina del tutorial (bottone «Scegli la cartella sito-personale»). Senza la pagina, controlla a mano: nella cartella devono esserci i 5 file .html e style.css, tutti in minuscolo, senza spazi.", ""]
        for nf in s.get("files", []):
            o += [f"**RIQUADRO — file {nf}**", "", "```", codice(nf), "```", ""]
        if s.get("img"):
            o += [f"![{s['img'][1]}|520](../../docs/3inf/sito-stage/img/{s['img'][0]})", ""]
        if s.get("img2"):
            o += [f"![{s['img2'][1]}|520](../../docs/3inf/sito-stage/img/{s['img2'][0]})", ""]
        if s.get("fallo"):
            for it, b in s["fallo"]:
                o += [f"> **Fallo tuo:** {it.replace('Fallo tuo. ', '')}", ">"]
                if bn: o += [f"> {b}", ">"]
            o.append("")
    o += ["<<PAGINA>>", "", "## Se qualcosa non va", ""]
    o += ["| Problema | Come si sistema |", "|---|---|"]
    for i, (a, b) in enumerate(PROBLEMI):
        o.append(f"| {a} | {b}" + (f" <br> {PROBLEMI_BN[i]}" if False else "") + " |")
    o.append("")
    if bn:
        o += ["সমস্যা হলে (বাংলায়):", ""]
        for i, b in enumerate(PROBLEMI_BN):
            o += [f"{i + 1}. {b}", ""]
    o += ["> **Limite:** il sito è una cartella sul tuo PC: non lo vede nessun altro finché non lo consegni. I giorni delle presenze restano nel browser di questo PC finché il prof non attiva il servizio condiviso: per questo c'è il file di sicurezza.", ""]
    if bn: o += ["> সীমা: সাইটটি তোমার পিসির একটি ফোল্ডার: জমা না দেওয়া পর্যন্ত অন্য কেউ দেখতে পায় না।", ""]
    o += [f"<!-- Versione {VERSIONE} ({DATA}): v1.1: sostituisce la v1.0. Generato da strumenti/genera_tutorial_sito_3inf.py: non modificare a mano. -->", ""]
    return "\n".join(o)


# ---------------------------------------------------------------- HTML guidato
CSS = """:root{--bg:#f6f7f9;--card:#fff;--ink:#14202b;--mut:#4a5968;--line:#cdd5dd;--acc:#0b57d0;--accd:#fff;--ok:#0a7a3d;--okbg:#c8f0d2;--ko:#a32020;--code:#1e2733;--codet:#e8eef5;--bnbg:#eef7ee}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10161c;--card:#1a232c;--ink:#e8eef4;--mut:#a9b7c4;--line:#33424f;--acc:#8ab4f8;--accd:#10161c;--ok:#7fd69b;--okbg:#17402a;--ko:#ff9b9b;--bnbg:#1d2e22}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow-wrap:anywhere}
main{max-width:760px;margin:0 auto;padding:14px 16px 80px}
h1{font-size:27px;line-height:1.2;margin:8px 0 4px}h2{font-size:21px;margin:0}
.sub{color:var(--mut)}
.bar{position:sticky;top:0;background:var(--bg);padding:8px 0;z-index:5;border-bottom:1px solid var(--line)}
.bar .t{height:12px;background:var(--line);border-radius:8px;overflow:hidden}.bar .t i{display:block;height:100%;width:0;background:var(--ok);transition:width .4s}
.bar .c{font-weight:700;margin-top:4px;display:inline-block}#vai{min-height:36px;padding:4px 12px;font-size:15px;margin-left:8px}
details{background:var(--card);border:2px solid var(--line);border-radius:16px;margin:14px 0;padding:0}
details[open]{border-color:var(--acc)}details.fatto{border-color:var(--ok)}
summary{cursor:pointer;list-style:none;padding:14px 16px;font-weight:700;font-size:20px;display:flex;gap:10px;align-items:center}
summary::-webkit-details-marker{display:none}
.num{flex:0 0 36px;height:36px;border-radius:50%;background:var(--acc);color:var(--accd);text-align:center;line-height:36px;font-size:18px}
details.fatto .num{background:var(--ok)}
.corpo{padding:0 16px 16px}
ol.az{padding-left:0;list-style:none;counter-reset:a;margin:6px 0}
ol.az>li{counter-increment:a;display:block;margin:10px 0}
ol.az>li::before{content:counter(a);display:inline-block;width:28px;height:28px;border-radius:50%;background:var(--acc);color:var(--accd);text-align:center;line-height:28px;font-weight:700;margin-right:8px}
.bn{display:none;background:var(--bnbg);border-left:4px solid var(--ok);padding:4px 10px;margin:4px 0 8px 36px;font-family:"Noto Sans Bengali","Vrinda","Nirmala UI",sans-serif}
body.pc14 .bn{display:block}
.cb{margin:12px 0;border:2px solid var(--line);border-radius:12px;overflow:hidden}
.cb .lab{display:flex;justify-content:space-between;gap:8px;align-items:center;padding:6px 10px;background:var(--line);font-weight:700;font-size:15px}
.cb pre{margin:0;background:var(--code);color:var(--codet);padding:12px;overflow:auto;font-size:14px;line-height:1.4;max-height:300px;white-space:pre}
.btn{min-height:48px;padding:10px 16px;border-radius:12px;border:2px solid var(--acc);background:var(--acc);color:var(--accd);font-weight:700;font-size:17px;font-family:inherit;cursor:pointer;text-decoration:none;display:inline-block;touch-action:manipulation}
.btn.sec{background:transparent;color:var(--acc)}.cp{min-height:36px;padding:4px 14px;font-size:15px}
.fatto-b{margin-top:14px;display:flex;gap:10px;flex-wrap:wrap}
img.s{max-width:100%;border:1px solid var(--line);border-radius:10px;margin:8px 0;display:block}
.cap{font-size:14px;color:var(--mut);margin:0 0 8px}
.fallo{background:#fff8e1;border:2px solid #e6c96a;border-radius:12px;padding:8px 12px;margin:12px 0;color:#14202b}
.fallo .bn{background:#fdf3d0;margin-left:0}
.ris{margin:10px 0;padding:0;list-style:none}.ris li{padding:6px 0;border-bottom:1px solid var(--line)}
.ris .ok{color:var(--ok);font-weight:700}.ris .no{color:var(--ko);font-weight:700}.ris .fix{color:var(--mut);font-size:15px;margin-left:26px}
.tot{font-size:22px;font-weight:700;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:16px}th,td{border:1px solid var(--line);padding:8px;text-align:left;vertical-align:top}
.nota{color:var(--mut);font-size:15px}
"""


def h_frasi(lista, nome_file=""):
    r = []
    for it, b in lista:
        r.append(f"<li>{esc(it.format(n=nome_file))}<div class='bn' lang='bn'>{esc(b.format(n=nome_file))}</div></li>")
    return "<ol class='az'>" + "".join(r) + "</ol>"


def h_box(titolo, testo, i):
    return (f"<div class='cb'><div class='lab'><span>{esc(titolo)}</span><button class='btn cp' type='button' data-t='c{i}'>Copia</button></div>"
            f"<pre id='c{i}'>{esc(testo)}</pre></div>")


CHECKER = """<div class='cb' style='padding:12px'>
<p><label class='btn' style='cursor:pointer'>Scegli la cartella sito-personale<input id='cart' type='file' webkitdirectory multiple hidden></label></p>
<p class='nota'>Il browser ti chiede di «caricare» la cartella: non viene caricato niente. Il controllo gira solo sul tuo PC.</p>
<div id='ris' aria-live='polite'></div></div>"""

JS = r"""
var $=function(i){return document.getElementById(i)};
var N=%(N)d,CH='tutorial-sito-3inf-v1-1';
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
// bangla: solo per l'allievo del PC 14 (?pc=14 una volta, poi si ricorda; stessa chiave delle altre pagine della 3INF)
(function(){var m=location.search.match(/[?&]pc=(\d+)/);if(m)ls('pc-3inf-gioco',m[1]);if(ls('pc-3inf-gioco')==='14')document.body.classList.add('pc14')})();
var fatti={};try{fatti=JSON.parse(ls(CH)||'{}')}catch(e){}
var det=[].slice.call(document.querySelectorAll('details.passo'));
function aggiorna(){var n=0;det.forEach(function(d){var f=!!fatti[d.id];d.classList.toggle('fatto',f);if(f)n++;d.querySelector('.num').textContent=f?'✓':d.dataset.n});
 $('barra').style.width=Math.round(100*n/N)+'%%';
 var prox=det.filter(function(d){return !fatti[d.id]})[0];
 $('conta').textContent=prox?('Fatti '+n+(n===1?' passo':' passi')+' su '+N+'. Adesso: passo '+prox.dataset.n):('Hai fatto tutti i '+N+' passi. Bravo!');
 $('vai').onclick=function(){if(prox){prox.open=true;prox.scrollIntoView({behavior:'smooth',block:'start'})}};$('vai').hidden=!prox}
det.forEach(function(d,i){
 d.querySelector('.ho').addEventListener('click',function(){fatti[d.id]=1;ls(CH,JSON.stringify(fatti));d.open=false;var s=det[i+1];if(s){s.open=true;setTimeout(function(){s.scrollIntoView({behavior:'smooth',block:'start'})},50)}aggiorna()})});
var primo=det.filter(function(d){return !fatti[d.id]})[0];if(primo)primo.open=true;aggiorna();
// Copia
document.addEventListener('click',function(e){var b=e.target.closest('.cp');if(!b)return;var t=$(b.dataset.t).textContent;
 var ok=function(){b.textContent='Copiato';setTimeout(function(){b.textContent='Copia'},1500)};
 var vecchio=function(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(x){b.textContent='Seleziona e Ctrl+C'}document.body.removeChild(a)};
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(t).then(ok,vecchio);else vecchio()});
// Controllo della cartella (legge i file in locale, non invia niente)
var RICH=['index.html','passione.html','competenze.html','diario.html','presenze.html','style.css'];
var MENU=['index.html','passione.html','competenze.html','diario.html','presenze.html'];
function leggi(f){return new Promise(function(ok){var r=new FileReader();r.onload=function(){ok(String(r.result))};r.onerror=function(){ok('')};r.readAsText(f)})}
$('cart').addEventListener('change',async function(){
 var files=[].slice.call(this.files),mappa={},nomi=[];
 files.forEach(function(f){var p=(f.webkitRelativePath||f.name).split('/');p.shift();var r=p.join('/');mappa[r]=f;nomi.push(r)});
 var righe=[];function R(ok,t,fix){righe.push({ok:ok,t:t,fix:fix||''})}
 if(!files.length){$('ris').textContent='Non ho letto nessun file. Riprova.';return}
 RICH.forEach(function(n){R(!!mappa[n],'Il file '+n+' c’è',mappa[n]?'':'Manca il file '+n+' nella cartella. Rifai il passo di quel file. Il nome deve essere uguale, tutto minuscolo.')});
 var tx={};for(var n of RICH){if(mappa[n])tx[n]=await leggi(mappa[n])}
 MENU.forEach(function(n){if(!tx[n]||n==='presenze.html')return;
  var mancano=MENU.filter(function(m){return tx[n].indexOf('href="'+m+'"')<0});
  R(mancano.length===0,n+': il menu ha i cinque bottoni',mancano.length?'Nel menu mancano: '+mancano.join(', ')+'. Ricopia il file dal riquadro.':'');
  R(tx[n].indexOf('href="style.css"')>=0,n+': usa style.css','Manca la riga con style.css nel <head>. Ricopia il file dal riquadro.')});
 if(tx['presenze.html']){var p=tx['presenze.html'];var m=p.match(/allievo:\s*"([^"]*)"/);
  R(!!m&&m[1].charAt(0)!=='@','presenze.html: c’è il tuo nome'+(m&&m[1].charAt(0)!=='@'?' ('+m[1]+')':''),'Il file non ha il tuo nome. Rifai il passo Presenze stage e scegli il tuo nome.');
  R(p.indexOf('Carica il mio file')>=0,'presenze.html: è la versione nuova','Il file è vecchio. Scaricalo di nuovo dalla pagina «Copia la pagina Presenze stage».')}
 var strani=nomi.filter(function(r){var b=r.split('/').pop();return r.indexOf('/')<0&&(/[A-Z ]/.test(b)||/\.(css|html|js)\.txt$/i.test(b))});
 R(strani.length===0,'I nomi dei file sono giusti (minuscolo, senza spazi)',strani.length?'Nomi da sistemare: '+strani.join(', ')+'.':'');
 var ok=righe.filter(function(x){return x.ok}).length;
 $('ris').innerHTML='<div class="tot">'+ok+' controlli su '+righe.length+(ok===righe.length?' — tutto verde!':'')+'</div><ul class="ris">'+righe.map(function(x){return '<li><span class="'+(x.ok?'ok':'no')+'">'+(x.ok?'✓':'✗')+'</span> '+x.t.replace(/</g,'&lt;')+(x.ok?'':'<div class="fix">'+x.fix.replace(/</g,'&lt;')+'</div>')+'</li>'}).join('')+'</ul>'});
"""


def html_pagina():
    o = ["<!DOCTYPE html>", "<html lang='it'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>",
         "<meta name='robots' content='noindex'><link rel='icon' href='data:,'>",
         "<title>Il mio sito: Stage e Presenze</title>", f"<style>{CSS}</style></head><body><main>",
         "<h1>Il mio sito: Stage e Presenze</h1>",
         f"<div class='sub'>Classe 3 · Laboratorio · Versione {VERSIONE} · {DATA}</div>",
         "<p>Alla fine hai un sito uguale a quello dei compagni: Chi sono, Hobby, Competenze, Il mio stage e Presenze. Lavori con il Blocco note e il browser. Non installi niente.</p>",
         "<div class='bn' lang='bn' style='margin-left:0'>শেষে তোমার সাইট বন্ধুদের মতোই হবে: Chi sono, Hobby, Competenze, Il mio stage, Presenze। তুমি Blocco note আর ব্রাউজারে কাজ করবে। কিছু ইনস্টল করতে হবে না।</div>",
         "<div class='bar'><div class='t'><i id='barra'></i></div><div class='c' id='conta'></div><button class='btn' id='vai' type='button'>Vai al passo di adesso</button></div>"]
    for i, s in enumerate(P, 1):
        nf = s.get("nome_file", "")
        o.append(f"<details class='passo' id='{s['id']}' data-n='{i}'><summary><span class='num'>{i}</span><span>{esc(s['t'][0])}<div class='bn' lang='bn' style='margin:0;padding:0 8px;font-size:16px;font-weight:400'>{esc(s['t'][1])}</div></span></summary><div class='corpo'>")
        o.append(h_frasi(s.get("f", []), nf))
        for j, (e, t) in enumerate(s.get("box", [])): o.append(h_box(e, t, f"{s['id']}b{j}"))
        if s.get("f2"): o.append(h_frasi(s["f2"], nf))
        for j, (e, t) in enumerate(s.get("box2", [])): o.append(h_box(e, t, f"{s['id']}c{j}"))
        for j, f in enumerate(s.get("files", [])): o.append(h_box(f"RIQUADRO — file {f}", codice(f), f"{s['id']}f{j}"))
        if s.get("extra") == "link_copia":
            o.append(f"<p><a class='btn' href='{URL_COPIA}' target='_blank' rel='noopener'>Apri «Copia la pagina Presenze stage»</a></p><p class='nota'>Si apre in una scheda nuova: questa pagina resta aperta.</p>")
        if s.get("extra") == "checker": o.append(CHECKER)
        if s.get("img"): o.append(f"<img class='s' src='img/{s['img'][0]}' alt='{esc(s['img'][1])}'><p class='cap'>{esc(s['img'][1])}</p>")
        if s.get("img2"): o.append(f"<img class='s' src='img/{s['img2'][0]}' alt='{esc(s['img2'][1])}'><p class='cap'>{esc(s['img2'][1])}</p>")
        for it, b in s.get("fallo", []):
            o.append(f"<div class='fallo'><b>{esc(it.split('.')[0]) + '.' if it.startswith('Fallo tuo.') else ''}</b>{esc(it[len('Fallo tuo.'):] if it.startswith('Fallo tuo.') else it)}<div class='bn' lang='bn'>{esc(b)}</div></div>")
        o.append(f"<div class='fatto-b'><button class='btn ho' type='button'>{esc(s.get('btn', 'Ho fatto'))}</button></div></div></details>")
    o.append("<h2 style='margin-top:26px'>Se qualcosa non va</h2><table><tr><th>Problema</th><th>Come si sistema</th></tr>")
    for i, (a, b) in enumerate(PROBLEMI):
        o.append(f"<tr><td>{esc(a)}</td><td>{esc(b)}<div class='bn' lang='bn' style='margin-left:0'>{esc(PROBLEMI_BN[i])}</div></td></tr>")
    o.append("</table>")
    o.append("<p class='nota'><b>Limite:</b> il sito è una cartella sul tuo PC: non lo vede nessun altro finché non lo consegni. I giorni delle presenze restano nel browser di questo PC finché il prof non attiva il servizio condiviso: per questo c'è il file di sicurezza.</p>")
    o.append(f"<p class='nota'>Versione {VERSIONE} · {DATA} · PDF: <a href='Tutorial-Sito-Stage-IT-v{VERSIONE}.pdf'>italiano</a> · <a href='Tutorial-Sito-Stage-IT-BN-v{VERSIONE}.pdf'>italiano + বাংলা</a></p>")
    o.append("</main><script>" + (JS % {"N": N}) + "</script></body></html>")
    return "\n".join(o)


if __name__ == "__main__":
    os.makedirs(MDDIR, exist_ok=True)
    open(os.path.join(MDDIR, "tutorial-sito-stage-IT.md"), "w", encoding="utf-8").write(md(False))
    open(os.path.join(MDDIR, "tutorial-sito-stage-IT-BN.md"), "w", encoding="utf-8").write(md(True))
    open(os.path.join(SITO, "index.html"), "w", encoding="utf-8").write(html_pagina())
    print("passi:", N)
