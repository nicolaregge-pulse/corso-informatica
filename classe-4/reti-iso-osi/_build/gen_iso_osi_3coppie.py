# -*- coding: utf-8 -*-
"""Classe 4 (4TI) — 06/10/2026 — ISO/OSI in 3 COPPIE teoria + esercitazione (una per ora).

  Ora 1: Teoria 1 «I sette livelli»                 + Esercitazione 1 «La pila dei sette livelli»
  Ora 2: Teoria 2 «Incapsulamento e dispositivi»    + Esercitazione 2 «Chi lavora a che livello»
  Ora 3: Teoria 3 «Il metodo del tecnico di rete»   + Esercitazione 3 «Il viaggio del mio messaggio»

Genera: 6 PDF + 6 MD in classe-4/reti-iso-osi/, la pagina unica docs/4ti-iso-osi/ (mostra solo i pezzi
elencati in docs/4ti-iso-osi/fase.json: si sbloccano uno alla volta, §2.38-2.39), la banca del quiz
docs/quiz/banche/4ti-incapsulamento.js. I v1.0 già in docs/ non si cancellano (§2.31).
Uso: python3 classe-4/reti-iso-osi/_build/gen_iso_osi_3coppie.py
"""
import html, json, os, re, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_iso_osi import CSS, COL, LIV, CHROME, CART, DOCS, ROOT  # stesso stile della scheda v1.0

VER = "2.0"
DATA = "06/10/2026"
PREF = "20261006_Classe-4-PerTutti_v%s" % VER
SITO = "https://nicolaregge-pulse.github.io/corso-informatica/"
Q1 = SITO + "quiz/?b=4ti-iso-osi&n=1"
Q2 = SITO + "quiz/?b=4ti-incapsulamento&n=1"


def cover(tit, sotto):
    return "<div class='cover'><span class='ver'>v%s</span><h1>%s</h1><div class='s'>Classe 4 · Reti · %s · %s</div></div>" % (VER, tit, DATA, sotto)


def lista(voci, tag="ol"):
    return "<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % v for v in voci), tag)


def tabella(intest, righe):
    return "<table><tr>%s</tr>%s</table>" % ("".join("<th>%s</th>" % h for h in intest),
                                            "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in righe))


def box(cl, t):
    return "<div class='box %s'>%s</div>" % (cl, t)


def griglia(voci):
    return "<h2>Come viene valutato (in centesimi)</h2>" + tabella(["Cosa guardo", "Punti"], [(a, "<b>%s</b>" % p) for a, p in voci])


ENV = ("<div class='env'><span style='background:%s'>MAC</span><span style='background:%s'>IP</span><span style='background:%s'>TCP</span>"
       "<span style='background:#8e44ad'>Ciao prof!</span><span style='background:%s'>coda MAC</span></div>"
       "<div style='text-align:center;font-size:9pt;color:#667'>Il frame che viaggia sul cavo: il messaggio dentro tre buste</div>" % (COL[2], COL[3], COL[4], COL[2]))

PEZZI = []   # (chiave, tipo, titolo, sottotitolo, nome file, html)

# ---------------------------------------------------------------- ORA 1
t1 = cover("Teoria 1 di 3 — I sette livelli ISO/OSI", "teoria · prima ora")
t1 += box("goal", "<b>Perché ci serve:</b> ogni messaggio che parte dal tuo PC attraversa <b>7 livelli</b>. Se sai a quale livello sta un problema, sai <b>dove cercare il guasto</b>: è il lavoro del tecnico di rete ed è la base dell'esame con <b>Packet Tracer</b>.")
t1 += "<h2>1. L'idea: come spedire un pacco</h2><p>Tu scrivi il biglietto, lo metti in una scatola, il negozio scrive l'indirizzo, il corriere sceglie la strada, il furgone lo porta. Ognuno fa <b>un solo lavoro</b> e si fida di quello sotto. Una rete funziona allo stesso modo: <b>7 livelli</b>, ognuno con il suo compito.</p>"
t1 += "<h2>2. La tabella dei 7 livelli</h2>" + tabella(["Livello", "Cosa fa", "Esempi"], [("<span class='l' style='background:%s;display:block'>%d %s</span>" % (COL[n], n, nome), cosa, es) for n, nome, cosa, pdu, disp, es, tcp in LIV])
t1 += "<h2>3. Come ricordarli</h2>" + lista(["Dal basso (1) all'alto (7): <b>F</b>isico, <b>C</b>ollegamento, <b>R</b>ete, <b>T</b>rasporto, <b>S</b>essione, <b>P</b>resentazione, <b>A</b>pplicazione.",
    "Frase per ricordare le iniziali F-C-R-T-S-P-A: <b>«Fiori Colorati Rendono Tutti Sereni, Perfino gli Arrabbiati»</b>.",
    "In inglese (Physical, Data link, Network, Transport, Session, Presentation, Application): «Please Do Not Throw Sausage Pizza Away»."])
t1 += "<h2>4. Guarda il viaggio</h2><p>Apri la pagina interattiva <b>Il viaggio di un pacchetto</b> (è nella pagina della classe): fai scendere il messaggio dal 7 all'1 e guardalo risalire dall'altra parte.</p>"
t1 += box("carta", "<b>Carta e penna:</b> disegna la pila dei 7 livelli, dal 7 in alto all'1 in basso, ognuno con il suo colore. Ti serve per l'Esercitazione 1.")
PEZZI.append(("1a", "teoria", "Teoria 1 di 3 — I sette livelli ISO/OSI", "La tabella, il trucco per ricordarli, il viaggio interattivo.", "Teoria-1-Sette-Livelli", t1))

e1 = cover("Esercitazione 1 di 3 — La pila dei sette livelli", "esercitazione · si consegna su Classroom")
e1 += box("goal", "<b>Cosa consegni:</b> il Documento del compito su Classroom, con <b>3 parti</b>.")
e1 += "<h2>Parte 1 — Lo schema a mano</h2>" + lista(["Sul foglio disegna la pila dei 7 livelli, dal 7 in alto all'1 in basso.",
    "Accanto a ogni livello scrivi <b>un esempio tuo</b> (un programma che usi, un cavo che vedi, il router di casa...).",
    "Fai una foto del foglio con il telefono.",
    "Nel Documento, sotto Parte 1: menu <b>Inserisci</b> → <b>Immagine</b> → <b>Carica dal computer</b> (o dal telefono con l'app di Google Drive)."])
e1 += "<h2>Parte 2 — Il quiz personale</h2>" + lista(["Apri il quiz (link nella pagina della classe): ognuno ha domande e ordine diversi.",
    "Scrivi nome e cognome, rispondi, premi <b>Controlla</b>. Puoi correggere e ricontrollare.",
    "Premi <b>Copia</b> e incolla nel Documento sotto Parte 2 con Ctrl + V."])
e1 += "<h2>Parte 3 — Riflessione</h2>" + lista(["Quale livello ti sembra più difficile da capire, e perché?", "Cosa NON ho capito?"])
e1 += griglia([("Parte 1: i 7 livelli nell'ordine giusto", "20"), ("Parte 1: un esempio tuo per ogni livello", "15"), ("Parte 2: quiz (risposte giuste e tentativi)", "50"), ("Parte 3: riflessione", "15")])
e1 += box("note", "Alla fine premi il bottone blu <b>Consegna</b>. Conta che tu lo sappia <b>spiegare a voce</b>.")
PEZZI.append(("1b", "esercitazione", "Esercitazione 1 di 3 — La pila dei sette livelli", "Schema a mano con i tuoi esempi, quiz personale, riflessione.", "Esercitazione-1-Pila-dei-Livelli", e1))

# ---------------------------------------------------------------- ORA 2
t2 = cover("Teoria 2 di 3 — Incapsulamento e dispositivi di rete", "teoria · seconda ora")
t2 += "<h2>1. L'incapsulamento: le buste</h2><p>Chi spedisce, scendendo dal 7 all'1, <b>aggiunge</b> a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le <b>toglie</b> nell'ordine inverso.</p>" + ENV
t2 += "<h2>2. Come si chiama il pezzo di dati (PDU)</h2>" + tabella(["Livello", "Nome del pezzo (PDU)"], [("7 · 6 · 5", "dati"), ("4 Trasporto", "segmento"), ("3 Rete", "pacchetto"), ("2 Collegamento", "frame (trama)"), ("1 Fisico", "bit")])
t2 += box("note", "<b>PDU</b> = Protocol Data Unit, unità di dati del protocollo: il nome del pezzo di dati a quel livello.")
t2 += "<h2>3. Due indirizzi diversi: MAC e IP</h2>" + tabella(["", "Indirizzo MAC (livello 2)", "Indirizzo IP (livello 3)"], [
    ("Cos'è", "il «nome e cognome» della scheda di rete, scritto in fabbrica", "l'«indirizzo di casa», dato dalla rete in cui sei"),
    ("Esempio", "<code>3C:52:82:1A:7F:09</code>", "<code>192.168.1.23</code>"),
    ("Dove vale", "solo dentro la rete locale", "anche tra reti diverse, fino a Internet"),
    ("Chi lo usa", "lo switch", "il router")])
t2 += "<h2>4. I dispositivi e il loro livello</h2>" + tabella(["Dispositivo", "Livello", "Cosa fa"], [
    ("cavo, antenna, hub", "1", "trasporta i bit; l'hub ripete tutto a tutte le porte"),
    ("scheda di rete", "1-2", "trasforma i dati in segnali; ha il MAC"),
    ("switch, access point Wi-Fi", "2", "consegna il frame solo al dispositivo giusto, usando il MAC"),
    ("router", "3", "collega reti diverse e sceglie la strada, usando l'IP"),
    ("firewall", "3-4 e oltre", "decide cosa può passare (indirizzi, porte)")])
t2 += box("note", "Il «modem» di casa di solito è <b>più dispositivi in uno</b>: router + switch + access point Wi-Fi.")
t2 += "<h2>5. Trasporto: TCP o UDP</h2>" + tabella(["TCP", "UDP"], [("come una <b>raccomandata con ricevuta</b>: controlla che arrivi tutto, in ordine", "come una <b>cartolina</b>: veloce, ma se un pezzo si perde va avanti"),
    ("download, siti web, email", "videochiamate, giochi online, dirette")])
t2 += "<p>Le <b>porte</b> dicono a quale programma va il segmento: 80 = web (HTTP), 443 = web sicuro (HTTPS), 53 = DNS.</p>"
t2 += box("carta", "<b>Carta e penna:</b> disegna le buste di un messaggio (MAC · IP · TCP · dati · coda) e scrivi sotto ogni busta il suo livello.")
PEZZI.append(("2a", "teoria", "Teoria 2 di 3 — Incapsulamento e dispositivi di rete", "Le buste, i nomi dei pezzi, MAC e IP, i dispositivi, TCP e UDP.", "Teoria-2-Incapsulamento-Dispositivi", t2))

e2 = cover("Esercitazione 2 di 3 — Chi lavora a che livello", "esercitazione · si consegna su Classroom")
e2 += box("goal", "<b>Cosa consegni:</b> il Documento del compito su Classroom, con <b>4 parti</b>.")
e2 += "<h2>Parte 1 — Il quiz personale</h2>" + lista(["Apri il quiz «Incapsulamento e dispositivi» (link nella pagina della classe).", "Rispondi, premi <b>Controlla</b>, poi <b>Copia</b> e incolla sotto Parte 1."])
e2 += "<h2>Parte 2 — La rete di casa mia</h2><p>Nella tabella del Documento scrivi <b>almeno 4 dispositivi</b> che hai a casa o a scuola (modem-router, ripetitore Wi-Fi, switch, smart TV, console, telefono...). Per ognuno: cosa fa e il livello più alto a cui lavora.</p>"
e2 += "<h2>Parte 3 — Con parole tue</h2>" + lista(["Differenza tra indirizzo MAC e indirizzo IP, con un esempio.", "Un'attività che usa TCP e una che usa UDP, e perché."])
e2 += "<h2>Parte 4 — Riflessione</h2>" + lista(["Cosa NON ho capito?"])
e2 += griglia([("Parte 1: quiz", "40"), ("Parte 2: almeno 4 dispositivi con livello giusto", "25"), ("Parte 3: MAC e IP, TCP e UDP con parole tue", "25"), ("Parte 4: riflessione", "10")])
e2 += box("note", "Alla fine premi il bottone blu <b>Consegna</b>.")
PEZZI.append(("2b", "esercitazione", "Esercitazione 2 di 3 — Chi lavora a che livello", "Quiz, la rete di casa tua, MAC e IP, TCP e UDP.", "Esercitazione-2-Chi-Lavora-a-che-Livello", e2))

# ---------------------------------------------------------------- ORA 3
t3 = cover("Teoria 3 di 3 — Il metodo del tecnico di rete", "teoria · terza ora")
t3 += "<h2>1. ISO/OSI e TCP/IP</h2><p>ISO/OSI è il modello per <b>ragionare</b>; Internet usa il modello <b>TCP/IP</b>, che ha 4 livelli e raggruppa quelli OSI così:</p>"
t3 += tabella(["TCP/IP (4 livelli)", "Livelli ISO/OSI"], [("Applicazione", "7 · 6 · 5"), ("Trasporto", "4"), ("Internet", "3"), ("Accesso alla rete", "2 · 1")])
t3 += "<h2>2. Il metodo: dal basso verso l'alto</h2><p>Quando «Internet non va», il tecnico controlla <b>prima i livelli bassi</b>: se il cavo è staccato, è inutile cercare il problema nel browser.</p>"
t3 += tabella(["Livello", "Cosa controllo", "Come"], [
    ("1 Fisico", "cavo collegato, lucine accese, Wi-Fi attivo", "guardo e tocco: lucina della scheda di rete, icona della rete"),
    ("2 Collegamento", "switch o access point acceso, porta funzionante", "cambio porta o cavo; mi ricollego al Wi-Fi"),
    ("3 Rete", "il PC ha un IP giusto? il router risponde?", "<code>ipconfig</code>: se l'IP inizia con 169.254 non l'ha ricevuto; <code>ping</code> al router"),
    ("4-7", "il servizio e il nome del sito funzionano?", "<code>ping 8.8.8.8</code> va ma il sito no → problema di DNS")])
t3 += box("note", "<b>ipconfig</b> mostra l'indirizzo IP del PC; <b>ping</b> manda un piccolo messaggio e aspetta la risposta (protocollo ICMP, livello 3). <b>DNS</b> traduce il nome del sito (www.google.it) in un indirizzo IP.")
t3 += "<h2>3. Tre casi svolti</h2>" + tabella(["Sintomo", "Livello", "Cosa faccio"], [
    ("L'icona della rete ha una X: «cavo di rete scollegato»", "1", "ricollego il cavo o lo cambio"),
    ("<code>ipconfig</code> mostra 169.254.10.5", "3", "il PC non ha ricevuto l'IP dal router: riavvio la scheda di rete, controllo il router"),
    ("<code>ping 8.8.8.8</code> risponde ma www.google.it non si apre", "7 (DNS)", "il collegamento c'è, manca la traduzione dei nomi: controllo il DNS")])
t3 += box("carta", "<b>Carta e penna:</b> scrivi i 4 controlli in ordine, dal livello 1 in su. È la scaletta che userai anche in Packet Tracer.")
PEZZI.append(("3a", "teoria", "Teoria 3 di 3 — Il metodo del tecnico di rete", "ISO/OSI e TCP/IP, i controlli dal basso, tre guasti svolti.", "Teoria-3-Metodo-del-Tecnico", t3))

e3 = cover("Esercitazione 3 di 3 — Il viaggio del mio messaggio", "esercitazione · si consegna su Classroom")
e3 += box("goal", "<b>Cosa consegni:</b> il Documento del compito su Classroom, con <b>3 parti</b>.")
e3 += "<h2>Parte 1 — Il viaggio del mio messaggio</h2><p>Scegli una cosa che fai davvero (un messaggio WhatsApp, aprire un sito, una partita online, una mail). Per <b>ogni livello dal 7 all'1</b> scrivi <b>una frase tua</b>: cosa succede a quel livello nel tuo esempio. Poi il viaggio di ritorno (dall'1 al 7) in 3 righe: chi toglie quale busta.</p>"
e3 += "<h2>Parte 2 — Il tecnico</h2><p>Per ogni guasto scrivi: <b>a quale livello</b> sta il problema e <b>cosa controlli o fai</b>.</p>" + lista([
    "A — Il PC dice: «cavo di rete scollegato».", "B — <code>ipconfig</code> mostra l'indirizzo 169.254.10.5.", "C — <code>ping 8.8.8.8</code> risponde, ma www.google.it non si apre."])
e3 += "<h2>Parte 3 — Riflessione</h2>" + lista(["Cosa NON ho capito oggi?", "Quale dei tre guasti ti è sembrato più difficile, e perché?"])
e3 += griglia([("Parte 1: i 7 livelli spiegati sul TUO esempio", "30"), ("Parte 1: viaggio di ritorno (le buste tolte)", "10"), ("Parte 2: i 3 guasti, livello e controllo (15 l'uno)", "45"), ("Parte 3: riflessione", "15")])
e3 += box("note", "Testi copiati da Internet o da un'AI senza parole tue non valgono: conta che tu lo sappia <b>spiegare a voce</b>. Alla fine premi <b>Consegna</b>.")
PEZZI.append(("3b", "esercitazione", "Esercitazione 3 di 3 — Il viaggio del mio messaggio", "Il tuo esempio livello per livello e tre guasti da risolvere.", "Esercitazione-3-Viaggio-del-Mio-Messaggio", e3))


def pagina(t, c):
    return "<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>%s<div class='foot'>Classe 4 · %s · v%s</div></body></html>" % (t, CSS, c, t, VER)


def in_md(titolo, h):
    """MD sorgente (testo per l'IA dei ragazzi) ricavato dall'HTML del pezzo."""
    t = re.sub(r"<div class='cover'>.*?</div></div>", "", h, flags=re.S)
    t = re.sub(r"<h2>(.*?)</h2>", r"\n## \1\n", t)
    t = re.sub(r"<tr>(.*?)</tr>", lambda m: "| " + " | ".join(re.findall(r"<t[hd]>(.*?)</t[hd]>", m.group(1))) + " |\n", t)
    t = re.sub(r"<li>(.*?)</li>", r"1. \1\n", t)
    t = re.sub(r"<code>(.*?)</code>", r"`\1`", t)
    t = re.sub(r"<b>(.*?)</b>", r"**\1**", t)
    t = re.sub(r"</?(p|div|ol|ul|table|span)[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(re.sub(r"\n{3,}", "\n\n", t)).strip()
    return "# %s\n\n**Versione %s** — %s — Classe 4, Reti.\n\n%s\n" % (titolo, VER, DATA, t)


def hub():
    sez = ""
    col = {"teoria": "#1f6fa5", "esercitazione": "#d9731a"}
    for k, tipo, tit, sotto, nome, _ in PEZZI:
        extra = ""
        if k == "1a":
            extra = "<a class='bt' style='background:#3a1c71' href='viaggio.html'>Il viaggio di un pacchetto<small>pagina interattiva</small></a>"
        if k == "1b":
            extra = "<a class='bt' style='background:#2f9e57' href='../quiz/?b=4ti-iso-osi&amp;n=1'>Quiz personale — i sette livelli</a>"
        if k == "2b":
            extra = "<a class='bt' style='background:#2f9e57' href='../quiz/?b=4ti-incapsulamento&amp;n=1'>Quiz personale — incapsulamento e dispositivi</a>"
        sez += ("<div class='box' data-k='%s' hidden><div class='tipo' style='color:%s'>%s</div><h2>%s</h2><p>%s</p>%s"
                "<a class='bt' style='background:%s' href='%s-v%s.pdf'>Apri la %s<small>PDF</small></a></div>") % (
            k, col[tipo], "TEORIA" if tipo == "teoria" else "ESERCITAZIONE · si consegna su Classroom", html.escape(tit), html.escape(sotto), extra,
            col[tipo], nome, VER, "teoria" if tipo == "teoria" else "consegna")
    return """<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Classe 4 — ISO/OSI</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f7fb;color:#1a2330;font-family:"Segoe UI",Arial,sans-serif}[hidden]{display:none!important}
.w{max-width:760px;margin:0 auto;padding:18px 16px 40px}h1{font-size:26px;margin:6px 0 4px;color:#12467a}.sub{color:#556;margin-bottom:12px}
.box{background:#fff;border-radius:14px;padding:16px;margin:16px 0;box-shadow:0 1px 4px rgba(0,0,0,.08);display:flex;flex-direction:column;gap:10px}
.box h2{margin:0;font-size:22px}.box p{margin:0;color:#556}.tipo{font-size:13px;font-weight:700;letter-spacing:.06em}
a.bt{display:block;text-align:center;text-decoration:none;color:#fff;font-size:20px;font-weight:700;padding:14px 10px;border-radius:12px}
a.bt small{display:block;font-size:13px;font-weight:400;opacity:.9;margin-top:4px}
.attesa{color:#556;font-style:italic}.ver{float:right;background:#12467a;color:#fff;border-radius:12px;padding:2px 10px;font-size:13px;margin-top:10px}
</style></head><body><div class="w"><span class="ver">v%(v)s</span><h1>Classe 4 — Il modello ISO/OSI</h1>
<div class="sub">%(d)s · Reti · tre coppie: teoria, poi esercitazione. Carta e penna sul banco.</div>
%(sez)s<p class="attesa" id="attesa">Il prossimo pezzo compare qui quando il prof lo apre: non serve ricaricare la pagina.</p>
</div><script>
function fase(){fetch("fase.json?t="+Date.now(),{cache:"no-store"}).then(function(r){return r.json()}).then(mostra).catch(function(){mostra({visibili:["1a"]})})}
function mostra(f){var v=(f&&f.visibili)||["1a"];document.querySelectorAll("[data-k]").forEach(function(b){b.hidden=v.indexOf(b.getAttribute("data-k"))<0});
document.getElementById("attesa").hidden=v.length>=6}
fase();setInterval(fase,60000);
</script></body></html>""" % {"v": VER, "d": DATA, "sez": sez}


QUIZ2 = [
 ("Come si chiama il pezzo di dati al livello 4 (Trasporto)?", ["segmento", "pacchetto", "frame", "bit"]),
 ("Come si chiama il pezzo di dati al livello 3 (Rete)?", ["pacchetto", "segmento", "frame", "bit"]),
 ("Come si chiama il pezzo di dati al livello 2 (Collegamento dati)?", ["frame (trama)", "pacchetto", "segmento", "dati"]),
 ("Al livello 1 (Fisico) i dati viaggiano come…", ["bit (segnali elettrici, luce, onde radio)", "pacchetti", "segmenti", "file"]),
 ("Quale di questi è un <b>indirizzo IP</b>?", ["192.168.1.23", "3C:52:82:1A:7F:09", "www.scuola.it", "443"]),
 ("Quale di questi è un <b>indirizzo MAC</b>?", ["3C:52:82:1A:7F:09", "192.168.1.23", "8.8.8.8", "80"]),
 ("Differenza tra <b>hub</b> e <b>switch</b>?", ["L'hub ripete i dati a tutte le porte; lo switch li manda solo alla porta giusta usando il MAC",
   "Sono la stessa cosa", "Lo switch collega reti diverse usando l'IP", "L'hub cifra i dati"]),
 ("Il <b>router</b> di casa serve a…", ["collegare la tua rete locale a Internet (reti diverse) usando l'IP", "trasformare i bit in luce",
   "dare il MAC alla scheda di rete", "velocizzare il computer"]),
 ("L'<b>access point Wi-Fi</b> lavora soprattutto al livello…", ["2 Collegamento dati", "3 Rete", "5 Sessione", "7 Applicazione"]),
 ("Una videochiamata o un gioco online usano spesso…", ["UDP: veloce, se perde un pezzo va avanti", "TCP: controlla ogni pezzo e aspetta", "solo il MAC", "la porta 25"]),
 ("Scaricare un file usa…", ["TCP: deve arrivare tutto e in ordine", "UDP: non importa se manca un pezzo", "l'hub", "il livello 1 soltanto"]),
 ("La porta <b>443</b> indica…", ["il web sicuro (HTTPS)", "la posta", "il DNS", "il cavo di rete"]),
 ("Sul cavo, quale busta è la più esterna?", ["quella del livello 2 (intestazione MAC)", "quella TCP", "quella IP", "i dati"]),
 ("Chi riceve il frame, quale busta toglie per prima?", ["quella del livello 2 (MAC)", "quella del livello 4 (TCP)", "quella del livello 7", "nessuna"]),
]


def banca2():
    d = {"titolo": "Incapsulamento e dispositivi", "sotto": "Classe 4 · Reti · ognuno ha le sue domande · ripassa con la Teoria 2 nella <a href='../4ti-iso-osi/'>pagina della classe</a>",
         "regola": "Pezzi di dati: <b>dati</b> (7-5) · <b>segmento</b> (4) · <b>pacchetto</b> (3) · <b>frame</b> (2) · <b>bit</b> (1). <b>MAC</b> = livello 2, lo usa lo switch; <b>IP</b> = livello 3, lo usa il router. <b>TCP</b> controlla tutto, <b>UDP</b> è veloce.",
         "quante": 10, "domande": [{"q": q, "o": o, "a": 0} for q, o in QUIZ2]}
    open(os.path.join(ROOT, "docs", "quiz", "banche", "4ti-incapsulamento.js"), "w", encoding="utf-8").write(
        "// Classe 4 — Incapsulamento e dispositivi (06/10/2026). Generato da classe-4/reti-iso-osi/_build/gen_iso_osi_3coppie.py\nwindow.BANCA = " + json.dumps(d, ensure_ascii=False, indent=1) + ";\n")


if __name__ == "__main__":
    os.makedirs(DOCS, exist_ok=True)
    for k, tipo, tit, sotto, nome, h in PEZZI:
        base = "%s_%s_IT" % (PREF, nome)
        hp = os.path.join(CART, nome.lower() + ".html")
        open(hp, "w", encoding="utf-8").write(pagina(tit, h))
        out = os.path.join(CART, base + ".pdf")
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + out, "file://" + hp], check=True, capture_output=True)
        open(os.path.join(CART, nome.lower() + ".md"), "w", encoding="utf-8").write(in_md(tit, h))
        shutil.copy(out, os.path.join(DOCS, "%s-v%s.pdf" % (nome, VER)))
        print(base + ".pdf")
    shutil.copy(os.path.join(CART, "viaggio-pacchetto-iso-osi.html"), os.path.join(DOCS, "viaggio.html"))
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(hub())
    if not os.path.exists(os.path.join(DOCS, "fase.json")):
        json.dump({"visibili": ["1a"]}, open(os.path.join(DOCS, "fase.json"), "w"))
    banca2()
