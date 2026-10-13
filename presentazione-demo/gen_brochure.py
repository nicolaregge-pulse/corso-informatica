# -*- coding: utf-8 -*-
"""Brochure commerciale del metodo «Una scuola che lavora come un'azienda di software».

Scrive brochure.md (la fonte) e il PDF A4 con le schermate vere (nomi dei ragazzi sostituiti).
Uso:  python3 presentazione-demo/gen_brochure.py
"""
import html, os, subprocess

QUI = os.path.dirname(os.path.abspath(__file__))
VER = "1.3"
DATA = "20261013"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
DEMO = "https://script.google.com/macros/s/AKfycbyhkWr44IWarPFRvcyP0Ku1pI-XbFaeBVJA4I0iEITq_4U4XvD5rqiPci77-p2FLory/exec"
GIOCO = "https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/"
E = html.escape

# Pull Request ricevute per quarto d'ora, 2INF 12/10/2026 (dal backlog della giornata)
RITMO = [("12:15", 3), ("12:30", 4), ("12:45", 22), ("13:00", 49), ("13:15", 23), ("13:30", 21), ("13:45", 7)]

PROBLEMA = [
    ("Si arrendono prima di provarci", "Molti ragazzi arrivano da percorsi difficili e hanno imparato che provarci vuol dire sbagliare davanti a tutti. Si difendono mollando."),
    ("Il risultato arriva tardi", "Il voto arriva giorni dopo, quando il lavoro è già dimenticato. Nessuno vede subito che il suo impegno conta."),
    ("Il docente non vede tutto", "In una classe di venti ragazzi, con lingue diverse, è difficile sapere chi sta lavorando, su cosa e quanto."),
    ("Esercizi lontani dal lavoro vero", "Gli esercizi di scuola non somigliano a quello che chiedono le aziende."),
]
PILASTRI = [
    ("Vinci subito", "Il primo passo è facile per tutti: nei primi dieci minuti ognuno vede qualcosa di suo funzionare."),
    ("Fallo tuo", "Ogni ragazzo propone le sue modifiche al gioco della classe: il nome, il colore, il nemico nuovo sono suoi."),
    ("Mostralo", "Ogni richiesta accettata diventa una versione nuova del gioco, giocabile subito, con il nome di chi l'ha chiesta."),
    ("Tutto si aggiorna da solo", "Backlog, voti, classifica e monitor della lezione si aggiornano ogni minuto, senza lavoro in più per il docente."),
]
PASSI = [
    ("01-compito.png", "1. Un solo link su Classroom", "La pagina della lezione: il percorso della giornata, la teoria breve, poi i bottoni verdi del lavoro."),
    ("12-prova-pr.png", "2. La Pull Request", "Il ragazzo propone una modifica al gioco con quattro parti: titolo, cosa cambia, dove, perché. È la stessa richiesta di modifica che si fa nelle aziende di software."),
    ("02-backlog.png", "3. Il backlog", "Ogni richiesta entra nella coda di lavoro con un peso (quanto lavoro chiede). Si fanno prima le più leggere; ogni richiesta finisce FATTO con la sua versione, oppure NO con il motivo."),
    ("03-novita.png", "4. Una versione nuova", "Ogni richiesta accettata è una versione del gioco con il suo registro delle modifiche: chi l'ha chiesta, cosa cambia, dove nel codice."),
    ("09-gioco-in-corso.png", "5. Il gioco della classe", "Il gioco cresce davanti ai loro occhi: 20 versioni in tre ore, tutte nate da proposte dei ragazzi."),
]
DOCENTE = [
    ("04-voti.png", "I voti, con il perché", "Il voto proposto si calcola da solo: richieste inviate, richieste entrate nel gioco, come sono scritte, feedback sulla teoria. Il voto finale lo decide il docente."),
    ("05-classifica.png", "La classifica", "Chi ha portato più modifiche dentro il gioco. È pubblica durante la lezione: chi è indietro vede subito come recuperare."),
    ("06-monitor.png", "Il monitor della lezione", "Durante i giri il docente guarda gli schermi; resta scritto cosa c'era su ogni computer. Solo fatti, senza giudizi."),
    ("10-grafo.png", "L'albero delle versioni", "La storia del progetto come la disegna Git: rami, copie delle altre classi, unioni, versioni maggiori."),
]
COMPETENZE = ["Versionare il software: versioni, rami, copie (fork), unioni (merge), release",
              "Chiedere una modifica come in azienda: la Pull Request con titolo, cosa, dove, perché",
              "Lavorare con il metodo Agile: backlog, pesi, piccoli passi, sbagliare presto e correggere presto",
              "Lavorare in team su un prodotto unico, con regole chiare e il proprio contributo visibile",
              "Scrivere in modo preciso e verificabile: la richiesta si capisce o viene rimandata indietro"]
SERVE = ["Un browser: niente da installare sui computer della scuola",
         "Google Classroom e Google Moduli, già in uso in tanti istituti",
         "Un repository Git (GitHub) per il gioco e le pagine della lezione",
         "Pagine in più lingue per le classi con ragazzi stranieri (italiano, arabo, cinese, bengalese)",
         "Uno script che porta le consegne dai Moduli a Git entro un minuto"]
PER_CHI = [("Scuole e centri di formazione professionale", "un laboratorio di informatica che tiene agganciati anche i ragazzi più difficili"),
           ("Docenti", "un metodo pronto, con pagine, regole del voto e strumenti già provati in classe"),
           ("Aziende ed enti di formazione", "un percorso che allena le competenze che si usano davvero nei team di sviluppo")]


def grafico():
    """Barre verticali, una serie: le Pull Request per quarto d'ora. Etichetta solo sul picco."""
    W, H, ml, mb, mt = 640, 230, 34, 28, 16
    mx = 50
    bw = (W - ml - 10) / len(RITMO)
    s = ['<svg viewBox="0 0 %d %d" role="img" aria-label="Pull Request ricevute ogni quarto d\'ora: %s">' % (
        W, H, ", ".join("%s %d" % x for x in RITMO))]
    for v in (0, 25, 50):
        y = H - mb - (H - mb - mt) * v / mx
        s.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#e4e1d9" stroke-width="1"/>' % (ml, W - 10, y, y))
        s.append('<text x="%d" y="%.1f" font-size="11" fill="#6b6b6b" text-anchor="end">%d</text>' % (ml - 6, y + 4, v))
    for i, (ora, n) in enumerate(RITMO):
        h = (H - mb - mt) * n / mx
        x = ml + i * bw + bw * 0.22
        w = bw * 0.56
        y = H - mb - h
        s.append('<path d="M%.1f,%.1f v%.1f a4,4 0 0 1 4,-4 h%.1f a4,4 0 0 1 4,4 v%.1f z" fill="#1f6feb"/>' % (
            x, H - mb, -(h - 4), w - 8, h - 4))
        s.append('<text x="%.1f" y="%d" font-size="11" fill="#6b6b6b" text-anchor="middle">%s</text>' % (x + w / 2, H - 9, ora))
        if n == max(v for _, v in RITMO):
            s.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="700" fill="#111" text-anchor="middle">%d</text>' % (x + w / 2, y - 6, n))
    xv = ml + 4.47 * bw  # voti pubblicati alle 13:22
    s.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#111" stroke-width="1.5" stroke-dasharray="4 3"/>' % (xv, xv, mt, H - mb))
    s.append('<text x="%.1f" y="%d" font-size="11.5" fill="#111">13:22 voti pubblicati</text>' % (xv + 5, mt + 10))
    s.append("</svg>")
    return "".join(s)


def md():
    r = ["# Una scuola che lavora come un'azienda di software", "",
         "**Versione %s** — 12/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica. Brochure del metodo." % VER, "",
         "Il laboratorio di informatica che trasforma la classe in un team di sviluppo.", "", "## 01 Il problema", ""]
    r += ["%d. **%s.** %s" % (i + 1, a, b) for i, (a, b) in enumerate(PROBLEMA)]
    r += ["", "## 02 La soluzione", ""] + ["%d. **%s.** %s" % (i + 1, a, b) for i, (a, b) in enumerate(PILASTRI)]
    r += ["", "## 03 Come funziona una lezione", ""] + ["%d. **%s.** %s ![](schermate/%s)" % (i + 1, t, d, img) for i, (img, t, d) in enumerate(PASSI)]
    r += ["", "## 04 Cosa vede il docente", ""] + ["%d. **%s.** %s ![](schermate/%s)" % (i + 1, t, d, img) for i, (img, t, d) in enumerate(DOCENTE)]
    r += ["", "## 05 I risultati di una lezione vera (2INF, 12/10/2026)", "",
          "1. 3 ore, 17 ragazzi presenti, 129 Pull Request, 20 versioni nuove del gioco.", "2. 17 ragazzi su 17 hanno mandato almeno una richiesta.",
          "3. Pull Request per quarto d'ora: " + ", ".join("%s %d" % x for x in RITMO) + ".",
          "4. Un allievo era a 40; alle 13:22 i voti sono stati pubblicati, ha chiesto aiuto e in pochi minuti ha mandato quattro richieste nuove: ha chiuso a 62."]
    r += ["", "## 06 Le competenze che restano", ""] + ["%d. %s" % (i + 1, x) for i, x in enumerate(COMPETENZE)]
    r += ["", "## 07 Cosa serve", ""] + ["%d. %s" % (i + 1, x) for i, x in enumerate(SERVE)]
    r += ["", "## 08 Per chi", ""] + ["%d. **%s:** %s." % (i + 1, a, b) for i, (a, b) in enumerate(PER_CHI)]
    r += ["", "## 09 Provalo", "", "1. La demo del sistema: fai l'allievo, scrivi la tua Pull Request e guardala diventare una versione del gioco.", "", "```", DEMO, "```", "",
          "2. Il gioco della classe.", "", "```", GIOCO, "```", "", "Contatti: prof. Nicola Regge, nicola.regge@gmail.com", ""]
    open(os.path.join(QUI, "brochure.md"), "w", encoding="utf-8").write("\n".join(r))


def figura(img, t, d, alta=False):
    return '<figure%s><img src="schermate/%s"><figcaption><b>%s</b> %s</figcaption></figure>' % (' class="alta"' if alta else "", img, E(t), E(d))


def pdf():
    css = """
@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font:10.5pt/1.45 'DejaVu Sans',Arial,sans-serif;color:#15171a}
.p{width:210mm;height:297mm;padding:16mm 15mm;position:relative;break-after:page;overflow:hidden}
.cop{background:#0f2a5c;color:#fff;padding:0}.cop .top{padding:26mm 16mm 10mm}.cop h1{font-size:34pt;line-height:1.08;margin:0 0 8mm;letter-spacing:-.5px}
.cop .sub{font-size:15pt;color:#cfe0ff;max-width:150mm}.cop .img{position:absolute;left:16mm;right:16mm;bottom:50mm;height:100mm;border-radius:10px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.4)}
.cop .img img{width:100%;height:100%;object-fit:cover;object-position:top}.cop .piede{position:absolute;left:16mm;bottom:12mm;color:#cfe0ff;font-size:11pt}
.kick{font-size:9pt;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#1f6feb;margin:0 0 2mm}
h2{font-size:21pt;line-height:1.15;margin:0 0 6mm;letter-spacing:-.3px}h3{font-size:12pt;margin:0 0 1.5mm}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6mm}.box{border:1px solid #e1ddd3;border-radius:8px;padding:5mm;background:#fbfaf7}
.box.blu{border-color:#1f6feb;background:#eef4ff}.box.verde{border-color:#1a7f37;background:#edf7ef}
figure{margin:0 0 5mm}figure img{width:100%;height:62mm;object-fit:cover;object-position:top;border:1px solid #d9d5cb;border-radius:6px;display:block}
figure.alta img{height:96mm}figcaption{font-size:9.5pt;margin-top:2mm;color:#333}figcaption b{color:#15171a}
.num{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;margin:2mm 0 6mm}.num div{border-left:4px solid #1f6feb;padding:1mm 0 1mm 4mm}.num b{display:block;font-size:24pt;line-height:1.1}
ol{margin:0;padding-left:5mm}li{margin:0 0 1.5mm}.quote{font-size:13pt;line-height:1.4;border-left:4px solid #1a7f37;padding:3mm 0 3mm 5mm;margin:5mm 0}
svg{width:100%;height:auto;display:block}.link{word-break:break-all;font-size:9.5pt;background:#fff;border:1px solid #c9d8f5;border-radius:6px;padding:3mm;margin:2mm 0 5mm;display:block;color:#0b4bbd;text-decoration:none}
a.bot{display:block;text-align:center;color:#fff;text-decoration:none;font-weight:800;font-size:14pt;padding:5mm 4mm;border-radius:9px;margin:3mm 0 2mm}a.bot.b{background:#1f6feb}a.bot.v{background:#1a7f37}
.cop .bots{position:absolute;left:16mm;right:16mm;bottom:24mm;display:grid;grid-template-columns:1fr 1fr;gap:6mm}.cop .bots a.bot{margin:0}
.pn{position:absolute;right:15mm;bottom:9mm;font-size:8.5pt;color:#888}"""
    pagine = []
    pagine.append('<div class="p cop"><div class="top"><p class="kick" style="color:#9cc0ff">Laboratorio di informatica · prof. Nicola Regge</p>'
                  "<h1>Una scuola che lavora come un'azienda di software</h1><p class=sub>Il laboratorio che trasforma la classe in un team di sviluppo: "
                  "i ragazzi propongono modifiche, il gioco della classe cresce versione dopo versione, il voto si vede subito.</p></div>"
                  '<div class="img"><img src="schermate/08-gioco-copertina.png"></div><div class="bots"><a class="bot b" href="%s">▶ Prova il sistema come un allievo</a><a class="bot v" href="%s">▶ Gioca al gioco della classe</a></div>'
                  '<div class="piede">Il laboratorio di informatica secondo le idee di Nicola Regge · ottobre 2026</div></div>' % (E(DEMO), E(GIOCO)))
    pagine.append('<div class="p"><p class="kick">01 Il problema</p><h2>I ragazzi non mollano perché non capiscono. Mollano per non sbagliare davanti a tutti.</h2><div class="grid2">%s</div>'
                  '<p class="kick" style="margin-top:9mm">02 La soluzione</p><h2>Qui provarci conviene, e non fa male.</h2><div class="grid2">%s</div><div class="pn">2</div></div>' % (
                      "".join('<div class="box"><h3>%s</h3>%s</div>' % (E(a), E(b)) for a, b in PROBLEMA),
                      "".join('<div class="box blu"><h3>%s</h3>%s</div>' % (E(a), E(b)) for a, b in PILASTRI)))
    pagine.append('<div class="p"><p class="kick">03 Come funziona una lezione</p><h2>Dalla proposta del ragazzo alla versione nuova del gioco, in pochi minuti.</h2>'
                  '<div class="grid2"><div>%s%s</div><div>%s%s</div></div>%s<div class="pn">3</div></div>' % (
                      figura(*PASSI[0]), figura(*PASSI[1]), figura(*PASSI[2]), figura(*PASSI[3]), ""))
    pagine.append('<div class="p"><p class="kick">03 Come funziona una lezione</p>%s'
                  '<div class="box" style="margin-top:2mm"><h3>Lo stesso flusso delle aziende di software</h3><ol><li>Il ragazzo invia la richiesta da un Modulo Google.</li>'
                  '<li>Uno script la porta su Git entro un minuto.</li><li>Entra nel backlog con un peso.</li><li>Il docente la mette nel gioco: nasce una versione nuova, con il suo registro delle modifiche.</li>'
                  '<li>Voti, classifica e pagine della lezione si aggiornano da soli.</li></ol></div><div class="pn">4</div></div>' % figura(*PASSI[4], alta=True))
    pagine.append('<div class="p"><p class="kick">04 Cosa vede il docente</p><h2>Tutta la classe in una pagina, mentre la lezione è in corso.</h2>'
                  '<div class="grid2"><div>%s%s</div><div>%s%s</div></div><div class="pn">5</div></div>' % tuple(figura(*x) for x in DOCENTE))
    pagine.append('<div class="p"><p class="kick">05 I risultati di una lezione vera</p><h2>Seconda classe, lunedì 12 ottobre 2026, tre ore di laboratorio.</h2>'
                  '<div class="num"><div><b>129</b>Pull Request</div><div><b>20</b>versioni nuove del gioco</div><div><b>17/17</b>ragazzi hanno partecipato</div><div><b>3 ore</b>di laboratorio</div></div>'
                  '<h3>Pull Request ricevute ogni quarto d\'ora</h3>%s'
                  '<p class="quote">Un allievo era a 40. Alle 13:22 i voti sono diventati pubblici: ha chiesto aiuto, e in pochi minuti ha mandato quattro richieste nuove. Ha chiuso la giornata a 62.</p>'
                  '<p class="kick" style="margin-top:6mm">06 Le competenze che restano</p><ol>%s</ol><div class="pn">6</div></div>' % (
                      grafico(), "".join("<li>%s</li>" % E(x) for x in COMPETENZE)))
    pagine.append('<div class="p"><p class="kick">07 Cosa serve</p><h2>Niente da installare. Si parte con quello che la scuola ha già.</h2><ol>%s</ol>'
                  '<p class="kick" style="margin-top:9mm">08 Per chi</p><div class="grid2" style="grid-template-columns:1fr 1fr 1fr">%s</div>'
                  '<p class="kick" style="margin-top:9mm">09 Provalo</p><h2>Due link, cinque minuti.</h2><div class="grid2"><div class="box blu"><h3>La demo del sistema</h3>'
                  'Fai l\'allievo: scrivi la tua Pull Request e guardala entrare nel backlog, diventare una versione del gioco e cambiare il tuo voto. Si entra con la propria email e un codice.'
                  '<a class="bot b" href="%s">▶ Prova il sistema come un allievo</a><span style="font-size:8pt;color:#555;word-break:break-all">%s</span></div><div class="box verde"><h3>Il gioco della classe</h3>«Il treno blindato», costruito dai ragazzi una Pull Request alla volta.'
                  '<a class="bot v" href="%s">▶ Gioca al gioco della classe</a><span style="font-size:8pt;color:#555;word-break:break-all">%s</span></div></div><p style="margin-top:8mm;font-size:12pt"><b>Prof. Nicola Regge</b><br>Laboratorio di informatica<br><a href="mailto:nicola.regge@gmail.com" style="color:#0b4bbd">nicola.regge@gmail.com</a></p><div class="pn">7</div></div>' % (
                      "".join("<li>%s</li>" % E(x) for x in SERVE), "".join('<div class="box"><h3>%s</h3>%s</div>' % (E(a), E(b)) for a, b in PER_CHI),
                      E(DEMO), E(DEMO), E(GIOCO), E(GIOCO)))
    h = "<!doctype html><html lang=it><meta charset=utf-8><title>Brochure</title><style>%s</style>%s</html>" % (css, "".join(pagine))
    hp = os.path.join(QUI, "_brochure.html")
    open(hp, "w", encoding="utf-8").write(h)
    out = os.path.join(QUI, "%s_Brochure-Scuola-Azienda-Software_v%s.pdf" % (DATA, VER))
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + out, "file://" + hp], capture_output=True)
    os.remove(hp)
    print(out)


if __name__ == "__main__":
    md()
    pdf()
