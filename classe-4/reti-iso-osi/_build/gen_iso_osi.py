# -*- coding: utf-8 -*-
"""Classe 4 — martedì 06/10/2026: il modello ISO/OSI (scheda + compito) e pagina unica docs/4ti-iso-osi/.
Uso:  python3 classe-4/reti-iso-osi/_build/gen_iso_osi.py
"""
import os, shutil, subprocess, glob

VER = "1.0"
DATA = "06/10/2026"
PREF = "20261006_Classe-4-PerTutti"
QUI = os.path.dirname(os.path.abspath(__file__))
CART = os.path.dirname(QUI)
ROOT = os.path.dirname(os.path.dirname(CART))
DOCS = os.path.join(ROOT, "docs", "4ti-iso-osi")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
QUIZ = "https://nicolaregge-pulse.github.io/corso-informatica/quiz/?b=4ti-iso-osi&n=1"

CSS = """@page{size:A4;margin:13mm}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;color:#1a2330;font-family:"DejaVu Sans",Arial,sans-serif;font-size:10.4pt;line-height:1.45}
.cover{background:linear-gradient(135deg,#12467a,#3a1c71);color:#fff;border-radius:12px;padding:8mm 10mm;margin-bottom:4mm;position:relative}
.cover h1{margin:0;font-size:19pt}.cover .s{opacity:.92;margin-top:1.5mm}
.ver{position:absolute;top:4mm;right:5mm;background:#fff;color:#12467a;font-weight:bold;padding:1mm 3mm;border-radius:12px;font-size:10pt}
h2{color:#12467a;font-size:13pt;margin:5mm 0 2mm;border-bottom:3px solid #cfe0f0;padding-bottom:1mm;page-break-after:avoid}
table{border-collapse:collapse;width:100%;margin:2mm 0;page-break-inside:avoid}
th,td{border:1px solid #cfdbe8;padding:1.4mm 2.2mm;text-align:left;vertical-align:top;font-size:9.4pt}th{background:#12467a;color:#fff}
td.l{color:#fff;font-weight:bold;white-space:nowrap}
.box{border-radius:6px;padding:2.5mm 4mm;margin:3mm 0;page-break-inside:avoid}
.goal{background:#e9f6ee;border-left:5px solid #2f9e57}.note{background:#fff8e6;border-left:5px solid #d0a516}
.info{background:#eaf2fb;border-left:5px solid #1f6fa5}.carta{background:#eef4fb;border:1px dashed #9cc0e4}
.env{display:flex;justify-content:center;gap:0;margin:2mm 0;font-size:9pt;font-weight:bold;page-break-inside:avoid}
.env span{padding:2mm 3mm;color:#fff}
ol{margin:1mm 0 2mm;padding-left:7mm}li{margin:1.2mm 0}
.foot{margin-top:4mm;font-size:8.4pt;color:#778;border-top:1px solid #dde4ec;padding-top:1.5mm}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;padding:0 3px;border-radius:3px;font-size:9pt}
"""
COL = {7: "#8e44ad", 6: "#2980b9", 5: "#16a085", 4: "#27ae60", 3: "#f39c12", 2: "#e67e22", 1: "#c0392b"}
LIV = [(7, "Applicazione", "i programmi che usi: dove nasce il messaggio", "dati", "—", "HTTP, HTTPS, DNS, SMTP", "Applicazione"),
       (6, "Presentazione", "traduce in un formato comune, cifra e comprime", "dati", "—", "TLS (lucchetto), JPEG, ASCII", "Applicazione"),
       (5, "Sessione", "apre, tiene aperta e chiude la conversazione", "dati", "—", "sessioni, login", "Applicazione"),
       (4, "Trasporto", "spezza in pezzi, numera, controlla che arrivino tutti", "segmento", "—", "TCP, UDP, porte (80, 443)", "Trasporto"),
       (3, "Rete", "indirizzo IP e scelta della strada tra reti", "pacchetto", "router", "IP, ICMP (ping)", "Internet"),
       (2, "Collegamento dati", "indirizzo MAC, consegna nella rete locale", "frame (trama)", "switch, scheda di rete", "Ethernet, Wi-Fi (MAC)", "Accesso alla rete"),
       (1, "Fisico", "i bit come segnali: corrente, luce, onde radio", "bit", "cavi, hub, antenne", "RJ45, fibra, Wi-Fi", "Accesso alla rete")]


def pagina(t, c):
    return "<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>%s</body></html>" % (t, CSS, c)


def scheda():
    c = "<div class='cover'><span class='ver'>v%s</span><h1>Il modello ISO/OSI — i 7 livelli di una rete</h1><div class='s'>Classe 4 · Reti · %s · scheda di teoria</div></div>" % (VER, DATA)
    c += ("<div class='box goal'><b>Perché ci serve:</b> ogni volta che un messaggio parte dal tuo PC attraversa <b>7 livelli</b>. "
          "Se sai a quale livello sta un problema, sai <b>dove cercare il guasto</b>: è il lavoro del tecnico di rete, ed è la base dell'esame "
          "con <b>Packet Tracer</b>. Prima di leggere apri la pagina interattiva <b>Il viaggio di un pacchetto</b> (link su Classroom).</div>")
    c += "<h2>1. La tabella dei 7 livelli</h2><table><tr><th>Livello</th><th>Cosa fa</th><th>Il pezzo di dati (PDU)</th><th>Dispositivo</th><th>Esempi</th><th>TCP/IP</th></tr>"
    for n, nome, cosa, pdu, disp, es, tcp in LIV:
        c += "<tr><td class='l' style='background:%s'>%d %s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (COL[n], n, nome, cosa, pdu, disp, es, tcp)
    c += "</table>"
    c += ("<div class='box note'><b>PDU</b> (Protocol Data Unit, unità di dati del protocollo) = come si chiama il pezzo di dati a quel livello. "
          "<b>TCP/IP</b> = il modello usato davvero da Internet: ha <b>4 livelli</b> e raggruppa i livelli OSI come nell'ultima colonna.</div>")
    c += "<div style='page-break-inside:avoid'><h2>2. L'incapsulamento: le buste</h2>"
    c += "<p>Chi spedisce, scendendo dal 7 all'1, <b>aggiunge</b> a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le <b>toglie</b> nell'ordine inverso.</p>"
    c += ("<div class='env'><span style='background:%s'>MAC</span><span style='background:%s'>IP</span><span style='background:%s'>TCP</span>"
          "<span style='background:#8e44ad'>Ciao prof!</span><span style='background:%s'>coda MAC</span></div>" % (COL[2], COL[3], COL[4], COL[2]))
    c += "<div style='text-align:center;font-size:9pt;color:#667'>Il frame che viaggia sul cavo: il messaggio dentro tre buste</div></div>"
    c += "<h2>3. Il metodo del tecnico: dal basso verso l'alto</h2><ol>"
    c += "<li><b>1 Fisico:</b> il cavo è collegato? La lucina della scheda di rete è accesa? Il Wi-Fi è attivo?</li>"
    c += "<li><b>2 Collegamento:</b> lo switch è acceso? La porta funziona?</li>"
    c += "<li><b>3 Rete:</b> il PC ha un indirizzo IP corretto? Il router risponde al <code>ping</code>?</li>"
    c += "<li><b>4-7:</b> il servizio funziona? Il nome del sito si traduce (DNS)? Il programma è configurato bene?</li></ol>"
    c += "<div class='box carta'><b>Carta e penna:</b> disegna la pila dei 7 livelli con i colori, e accanto a ogni livello il suo dispositivo e la sua PDU. Poi disegna le buste del punto 2.</div>"
    c += "<div class='foot'>Classe 4 · Scheda ISO/OSI · v%s</div>" % VER
    return pagina("Scheda ISO/OSI", c)


def compito():
    c = "<div class='cover'><span class='ver'>v%s</span><h1>Compito — Il viaggio del mio messaggio</h1><div class='s'>Classe 4 · Reti · %s · si consegna su Classroom</div></div>" % (VER, DATA)
    c += "<div class='box goal'><b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom, con <b>3 parti</b>.</div>"
    c += "<h2>Parte 1 — Il quiz personale</h2><ol><li>Apri il link del quiz (è nel compito su Classroom): ognuno ha domande e ordine diversi.</li>"
    c += "<li>Scrivi nome e cognome, rispondi, premi <b>Controlla</b>. Puoi correggere e ricontrollare.</li>"
    c += "<li>Premi <b>Copia</b> e incolla nel Documento sotto <b>Parte 1</b>.</li></ol>"
    c += "<h2>Parte 2 — Il viaggio del mio messaggio</h2>"
    c += ("<p>Scegli una cosa che fai davvero (un messaggio WhatsApp, aprire un sito, una partita online, mandare una mail). "
          "Per <b>ogni livello dal 7 all'1</b> scrivi <b>una frase tua</b>: cosa succede a quel livello <b>nel tuo esempio</b>. Poi descrivi il viaggio di ritorno (dall'1 al 7) in 3 righe.</p>")
    c += "<h2>Parte 3 — Il tecnico</h2><ol><li>Un compagno dice: <i>\"Internet non va\"</i>. Scrivi i <b>4 controlli</b> che fai, in ordine, dal livello 1 in su, e cosa controlli a ogni livello.</li>"
    c += "<li>Riflessione: cosa NON ho capito? Quale livello mi sembra più difficile e perché?</li></ol>"
    c += "<h2>Come viene valutato (voto in decimi)</h2><table><tr><th>Cosa guardo</th><th>Punti</th></tr>"
    for a, p in [("Parte 1: quiz (giuste su 12, tentativi)", "4"), ("Parte 2: i 7 livelli spiegati sul TUO esempio, con parole tue", "3"),
                 ("Parte 2: viaggio di ritorno (le buste tolte)", "1"), ("Parte 3: i 4 controlli in ordine + riflessione", "2")]:
        c += "<tr><td>%s</td><td><b>%s</b></td></tr>" % (a, p)
    c += "</table><div class='box note'>Testi copiati da Internet o da un'AI senza parole tue non valgono: conta che tu lo sappia <b>spiegare a voce</b>.</div>"
    c += "<div class='foot'>Classe 4 · Compito ISO/OSI · v%s</div>" % VER
    return pagina("Compito ISO/OSI", c)


def hub(nomi):
    return """<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Classe 4 — ISO/OSI</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f7fb;color:#1a2330;font-family:"Segoe UI",Arial,sans-serif}
.w{max-width:760px;margin:0 auto;padding:18px 16px 40px}h1{font-size:26px;margin:6px 0 4px;color:#12467a}.sub{color:#556;margin-bottom:18px}
.box{background:#fff;border-radius:14px;padding:16px;margin:16px 0;box-shadow:0 1px 4px rgba(0,0,0,.08)}.box h2{margin:0 0 4px;font-size:22px}.box p{margin:0 0 12px;color:#556}
a.bt{display:block;text-align:center;text-decoration:none;color:#fff;font-size:21px;font-weight:700;padding:16px 10px;border-radius:12px}
a.bt small{display:block;font-size:13px;font-weight:400;opacity:.9;margin-top:4px}
.ver{float:right;background:#12467a;color:#fff;border-radius:12px;padding:2px 10px;font-size:13px;margin-top:10px}
</style></head><body><div class="w"><span class="ver">v%(v)s</span><h1>Classe 4 — Il modello ISO/OSI</h1><div class="sub">%(d)s · Reti · teoria interattiva, scheda, compito</div>
<div class="box"><h2 style="color:#3a1c71">1. Il viaggio di un pacchetto</h2><p>Clicca i livelli e fai viaggiare il messaggio: le buste si aggiungono e si tolgono.</p><a class="bt" style="background:#3a1c71" href="viaggio.html">Apri la pagina interattiva</a></div>
<div class="box"><h2 style="color:#1f6fa5">2. Scheda di teoria</h2><p>La tabella dei 7 livelli, le buste, il metodo del tecnico.</p><a class="bt" style="background:#1f6fa5" href="%(s)s">Apri la scheda<small>PDF</small></a></div>
<div class="box"><h2 style="color:#2f9e57">3. Quiz personale</h2><p>Ognuno ha le sue domande. Alla fine: Copia e incolla nel Documento.</p><a class="bt" style="background:#2f9e57" href="../quiz/?b=4ti-iso-osi&amp;n=1">Inizia il quiz</a></div>
<div class="box"><h2 style="color:#d9731a">4. Compito — Il viaggio del mio messaggio</h2><p>Il Documento in 3 parti: quiz, il tuo esempio livello per livello, il tecnico.</p><a class="bt" style="background:#d9731a" href="%(c)s">Apri il compito<small>PDF</small></a></div>
</div></body></html>""" % {"v": VER, "d": DATA, "s": nomi["s"], "c": nomi["c"]}


def pdf(h, nh, np_):
    hp = os.path.join(CART, nh); open(hp, "w", encoding="utf-8").write(h)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + os.path.join(CART, np_), "file://" + hp], check=True, capture_output=True)
    print(np_)


if __name__ == "__main__":
    for v in glob.glob(os.path.join(CART, "*.pdf")): os.remove(v)
    os.makedirs(DOCS, exist_ok=True)
    for v in glob.glob(os.path.join(DOCS, "*.pdf")): os.remove(v)
    s = "%s_v%s_Scheda-ISO-OSI_IT.pdf" % (PREF, VER); c = "%s_v%s_Compito-Viaggio-Messaggio_IT.pdf" % (PREF, VER)
    pdf(scheda(), "scheda-iso-osi.html", s); pdf(compito(), "compito-iso-osi.html", c)
    nomi = {"s": "Scheda-ISO-OSI-v%s.pdf" % VER, "c": "Compito-ISO-OSI-v%s.pdf" % VER}
    shutil.copy(os.path.join(CART, s), os.path.join(DOCS, nomi["s"])); shutil.copy(os.path.join(CART, c), os.path.join(DOCS, nomi["c"]))
    shutil.copy(os.path.join(CART, "viaggio-pacchetto-iso-osi.html"), os.path.join(DOCS, "viaggio.html"))
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(hub(nomi))
