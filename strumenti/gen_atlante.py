# -*- coding: utf-8 -*-
"""Atlante del corso: mappa illustrata e cliccabile («come un parco») + testo dell'Atlante, in HTML e in PDF.
Fonte del testo: ATLANTE.md (la versione si legge da lì). Le zone della mappa e i loro link stanno in ZONE, qui sotto.
Uscite: docs/<CARTELLA>/index.html (pagina raggiungibile solo con il link, noindex) e <data>_Atlante_Docente_vX.Y.pdf
nella radice, con i link cliccabili anche nel PDF.
Uso: python3 strumenti/gen_atlante.py"""
import sys as _sp, os as _op; _sp.path.append(_op.path.dirname(_op.path.abspath(__file__))); import privacy_pubblico  # noqa: E401,F401 privacy 28/10/2026: nel pubblico i ragazzi solo come «Nome C.»
import html, json, os, random, re, subprocess
import markdown

QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARTELLA = "atlante-k4x9w2"
VERS_PARCO = "1.2"   # «Il parco del corso», la versione pubblica con la sola mappa
BASE = "https://nicolaregge-pulse.github.io/corso-informatica/"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
e = html.escape

def u(p):
    return p if p.startswith("http") else BASE + p

# ====================== LE ZONE DEL PARCO ======================
# id, x, y, colore, titolo, sottotitolo, link principale, edificio, descrizione, [ (testo, link) ... ]
ZONE = [
 ("ingresso", 700, 745, "#e8590c", "Il laboratorio raccontato", "comunicazione e marketing", "cm-qma7yay4q5/", "porta",
  "L'ingresso del parco: i materiali per chi sta fuori dall'aula. Scuole, genitori, ragazzi, chi non sa niente di computer.",
  [("La pagina con le schede per destinatario", "cm-qma7yay4q5/"), ("Racconto «Cinque giorni da azienda»", "cm-qma7yay4q5/racconto/"),
   ("Demo con accesso via email", "https://script.google.com/macros/s/AKfycbyhkWr44IWarPFRvcyP0Ku1pI-XbFaeBVJA4I0iEITq_4U4XvD5rqiPci77-p2FLory/exec")]),
 ("stazione", 700, 285, "#c92a2a", "Stazione del Treno blindato", "il gioco della classe", "giochi/", "stazione",
  "Il gioco nato in classe e tutte le sue copie. Ogni proposta dei ragazzi diventa una versione nuova.",
  [("Tutti i giochi del corso", "giochi/"), ("Il treno della 1INF (fork del 13/10)", "giochi/treno-1inf-fork/"), ("Il treno della 2INF", "2inf-treno/"),
   ("La base del prof", "giochi/treno-prof/"), ("Il treno sulla Luna", "giochi/treno-luna/")]),
 ("grafo", 960, 215, "#7048e8", "Torre del Grafo", "tutte le versioni", "giochi/grafo/", "torre",
  "La storia del gioco come un albero: rami, copie, unioni. Ogni pallino è una versione che si gioca.",
  [("Il grafo delle versioni", "giochi/grafo/"), ("Lezione: le versioni del treno", "lezione-versioni/")]),
 ("1inf", 235, 185, "#f08c00", "Quartiere 1INF", "prima: fork e prima proposta", "compito/1inf-20261013-proposta/", "casa",
  "La prima superiore: il binario, le versioni, la copia del treno e la prima proposta di modifica.",
  [("Compito del 13/10: la mia prima Pull Request", "compito/1inf-20261013-proposta/"), ("I voti", "1inf-voti/"), ("Il backlog", "1inf-backlog/"),
   ("Il monitor della lezione", "1inf-monitor/"), ("Cosa è cambiato nel gioco", "1inf-novita/"), ("La classifica", "1inf-top/"),
   ("Cruscotto del prof (cifrato)", "1inf-cruscotto/"), ("Monta il PC (simulatore)", "monta-pc-v3/"), ("Ripasso e test: assemblaggio (16/10)", "verifica/?b=1inf-assemblaggio"),
   ("La sfida lampo sui pezzi del PC", "sfida-pc/"), ("Compito del 09/10: le versioni", "compito/1inf-20261009-versioni/"), ("Decimale e binario", "1inf-conversione/")]),
 ("2inf", 215, 455, "#1c7ed6", "Quartiere 2INF", "seconda: l'azienda in classe", "compito/2inf-20261012-documento/", "casa",
  "La seconda: 129 proposte e 20 versioni in tre ore, poi ripasso, verifica e recupero.",
  [("Il tuo Documento (12-13/10)", "compito/2inf-20261012-documento/"), ("I voti", "2inf-voti/"), ("Il backlog", "2inf-backlog/"),
   ("Il monitor della lezione", "2inf-monitor/"), ("Cosa è cambiato nel gioco", "2inf-novita/"), ("La classifica", "2inf-top/"),
   ("Cruscotto del prof (cifrato)", "2inf-cruscotto/"), ("Il ciclo FOR (15/10)", "verifica/?b=2inf-for"), ("Il ciclo FOR, seconda parte (19/10)", "verifica/?b=2inf-for2"),
   ("If annidati e il cassiere del cinema", "2inf-if/")]),
 ("3inf", 440, 640, "#2b8a3e", "Quartiere 3INF", "terza: siti e il gioco", "compito/3inf-20261012-documento/", "casa",
  "La terza: il primo sito pubblico, la copia del treno, le proposte in tempo reale.",
  [("Il tuo Documento (12/10)", "compito/3inf-20261012-documento/"), ("Il backlog", "3inf-backlog/"), ("Le Pull Request in tempo reale", "3inf-gioco/"),
   ("Il sito pubblicato online", "3inf-sito/"), ("Il mio sito diventa il mio portfolio (19/10)", "verifica/?b=3inf-portfolio"),
   ("Il mio punto: cosa mi manca", "3inf-mio-punto/"), ("Il monitor della lezione", "3inf-monitor/"), ("I voti", "3inf-voti/"), ("I siti della classe", "siti-classe/")]),
 ("4ti", 1180, 455, "#0b7285", "Laboratorio dello Stage", "quarta: progetti veri", "4ti-progetti/", "officina",
  "La quarta: reti e progetti di stage, un deposito per ragazzo e una chat con il prof e l'assistente.",
  [("Cruscotto dei progetti (dal vivo)", "4ti-progetti/"), ("Il viaggio di un pacchetto (ISO/OSI)", "4ti-iso-osi/"), ("App di reti", "4ti-app/"),
   ("Progetti della quarta: stazione meteo e router da allenamento", "cm-qma7yay4q5/progetti/")]),
 ("verifica", 465, 320, "#d6336c", "Torre delle Verifiche", "ripasso, verifica, recupero", "verifica/?b=2inf-versioning", "torre",
  "Un solo motore per tutte le classi: ripasso con la risposta subito, verifica, recupero sui propri errori.",
  [("Ripasso e verifica (2INF, versioni)", "verifica/?b=2inf-versioning"), ("Risultati della classe", "verifica/risultati.html?b=2inf-versioning"),
   ("Quiz personale", "quiz/"), ("Recupero a fianco", "recupero/")]),
 ("prof", 1185, 175, "#495057", "Sala di controllo", "gli strumenti del prof", "docenti/", "schermo",
  "Da qui il docente guida la lezione: cruscotti cifrati, strumenti per il registro e per la classe virtuale.",
  [("Strumenti per il registro e la classe virtuale", "docenti/"), ("Cruscotto 2INF", "2inf-cruscotto/"), ("Cruscotto 1INF", "1inf-cruscotto/"),
   ("Controlla chi ha fatto giusto", "controlla/"), ("Valutazione dei singoli 2INF", "2inf-valutazione/"),
   ("Cruscotto dal vivo: 3INF portfolio", "avanzamento/?b=3inf-portfolio-v1"), ("Cruscotto dal vivo: 2INF ciclo FOR", "avanzamento/?b=2inf-for2-v1"),
   ("Il cruscotto in demo, senza nomi", "demo/cruscotto/?b=3inf-portfolio-v1")]),
 ("info", 955, 430, "#f59f00", "Ufficio informazioni", "i registri che crescono", "avanzamento/registri.html", "info",
  "Tutti i registri che si aggiornano da soli e crescono a ogni lezione: il cruscotto della lezione, le uscite dall'aula, il fuori compito con le foto di Veyon, i diari, le consegne, le prossime lezioni.",
  [("L'ufficio informazioni", "avanzamento/registri.html"), ("Cruscotto della lezione", "avanzamento/oggi.html"), ("Uscite dall'aula", "avanzamento/uscite.html"),
   ("Registro del fuori compito", "avanzamento/fuori-compito.html"), ("Pubblica senza script (piano B)", "prof-pubblica/")]),
 ("giochi", 965, 645, "#ae3ec9", "Sala giochi", "i minigiochi del corso", "gioco/", "joystick",
  "I minigiochi costruiti e usati nelle lezioni, e l'azienda dei videogiochi.",
  [("Tutti i minigiochi", "gioco/"), ("L'azienda dei videogiochi", "azienda/"), ("Assalto dei mostri", "giochi/assalto-dei-mostri/"),
   ("Schiva gli asteroidi", "asteroidi/"), ("Acchiappa la talpa", "talpa/"), ("Rompi i mattoni", "mattoni/")]),
 ("biblioteca", 200, 690, "#5c940d", "Biblioteca", "teoria e lezioni", "teoria/agile-it/", "libro",
  "Le teorie da leggere, in più lingue: Agile, versioni, sicurezza.",
  [("Teoria Agile", "teoria/agile-it/"), ("Le versioni del treno", "lezione-versioni/"), ("Voci e volti falsi (deepfake)", "sicurezza-deepfake/"),
   ("Decimale e binario", "1inf-decimale-binario/")]),
 ("cassaforte", 1195, 700, "#343a40", "Cassaforte", "repository riservato", "", "lucchetto",
  "Nomi, voti, presenze, consegne, la coda della classe virtuale e i comandi per l'automazione stanno nel repository riservato: non si vedono da qui.",
  []),
]

# ====================== LA MAPPA (SVG disegnato a mano) ======================
def edificio(tipo, c):
    if tipo == "casa":
        return f'<rect x="-48" y="-38" width="96" height="58" rx="4" fill="{c}"/><polygon points="-58,-36 0,-80 58,-36" fill="#7a3d1d"/><rect x="-12" y="-6" width="24" height="26" fill="#fff8e6"/><rect x="-38" y="-24" width="16" height="14" fill="#fff8e6"/><rect x="22" y="-24" width="16" height="14" fill="#fff8e6"/>'
    if tipo == "torre":
        return f'<rect x="-24" y="-96" width="48" height="116" rx="4" fill="{c}"/><polygon points="-32,-94 0,-138 32,-94" fill="#7a3d1d"/><rect x="-9" y="-70" width="18" height="18" rx="9" fill="#fff8e6"/><rect x="-9" y="-36" width="18" height="18" rx="2" fill="#fff8e6"/>'
    if tipo == "stazione":
        return (f'<rect x="-90" y="-40" width="180" height="60" rx="5" fill="{c}"/><polygon points="-104,-38 0,-82 104,-38" fill="#7a3d1d"/>'
                f'<circle cx="0" cy="-52" r="12" fill="#fff8e6" stroke="#7a3d1d" stroke-width="3"/><line x1="0" y1="-52" x2="0" y2="-60" stroke="#333" stroke-width="2"/><line x1="0" y1="-52" x2="6" y2="-50" stroke="#333" stroke-width="2"/>'
                + "".join(f'<rect x="{x}" y="-24" width="22" height="30" rx="11" fill="#fff8e6"/>' for x in (-70, -35, 13, 48)))
    if tipo == "porta":
        return f'<rect x="-110" y="-70" width="28" height="90" fill="{c}"/><rect x="82" y="-70" width="28" height="90" fill="{c}"/><path d="M-110,-70 Q0,-150 110,-70 L82,-70 Q0,-122 -82,-70 Z" fill="{c}"/><circle cx="-96" cy="-80" r="9" fill="#ffd43b"/><circle cx="96" cy="-80" r="9" fill="#ffd43b"/>'
    if tipo == "lucchetto":
        return f'<rect x="-48" y="-50" width="96" height="70" rx="6" fill="{c}"/><path d="M-20,-50 V-70 A20,20 0 0 1 20,-70 V-50" fill="none" stroke="#adb5bd" stroke-width="8"/><circle cx="0" cy="-18" r="9" fill="#ffd43b"/><rect x="-3" y="-14" width="6" height="16" fill="#ffd43b"/>'
    icona = {
        "officina": '<circle cx="0" cy="-12" r="16" fill="none" stroke="#fff8e6" stroke-width="7" stroke-dasharray="7 5"/><circle cx="0" cy="-12" r="6" fill="#fff8e6"/>',
        "schermo": '<rect x="-22" y="-30" width="44" height="28" rx="3" fill="#a5d8ff"/><rect x="-6" y="-2" width="12" height="8" fill="#fff8e6"/><polyline points="-16,-12 -6,-20 4,-14 16,-24" fill="none" stroke="#1c7ed6" stroke-width="3"/>',
        "joystick": '<rect x="-24" y="-24" width="48" height="24" rx="12" fill="#fff8e6"/><circle cx="-11" cy="-12" r="4" fill="#333"/><circle cx="11" cy="-15" r="3" fill="#e03131"/><circle cx="16" cy="-9" r="3" fill="#2f9e44"/>',
        "info": '<circle cx="0" cy="-12" r="22" fill="#fff8e6"/><circle cx="0" cy="-24" r="3.5" fill="#7a3d1d"/><rect x="-3.5" y="-17" width="7" height="18" rx="2" fill="#7a3d1d"/>',
        "libro": '<path d="M-24,-30 Q-12,-36 0,-28 Q12,-36 24,-30 V2 Q12,-4 0,4 Q-12,-4 -24,2 Z" fill="#fff8e6"/><line x1="0" y1="-28" x2="0" y2="4" stroke="#7a3d1d" stroke-width="2"/>',
    }[tipo]
    return f'<rect x="-56" y="-46" width="112" height="66" rx="6" fill="{c}"/><polygon points="-66,-44 0,-84 66,-44" fill="#7a3d1d"/>{icona}'

def mappa():
    W, H = 1400, 880
    rnd = random.Random(7)
    s = [f'<svg viewBox="0 0 {W} {H}" class="mappa" role="img" aria-label="Mappa illustrata del corso">',
         '<defs><radialGradient id="prato" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#c8ebb0"/><stop offset="1" stop-color="#9fd18a"/></radialGradient>'
         '<filter id="ombra" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="5" stdDeviation="4" flood-opacity=".25"/></filter></defs>',
         f'<rect width="{W}" height="{H}" rx="28" fill="url(#prato)"/>',
         # il lago
         '<ellipse cx="700" cy="505" rx="150" ry="70" fill="#74c0fc"/><ellipse cx="700" cy="505" rx="122" ry="50" fill="#a5d8ff"/>',
         '<path d="M640,495 q14,-10 28,0 q14,10 28,0" fill="none" stroke="#e7f5ff" stroke-width="3"/><path d="M712,520 q14,-10 28,0 q14,10 28,0" fill="none" stroke="#e7f5ff" stroke-width="3"/>']
    # i vialetti: dall'ingresso a ogni zona
    gx, gy = 700, 735
    for z in ZONE[1:]:
        x, y = z[1], z[2]
        cx, cy = (gx + x) / 2 + (90 if x < gx else -90), (gy + y) / 2 + 40
        s.append(f'<path d="M{gx},{gy} Q{cx:.0f},{cy:.0f} {x},{y + 30}" fill="none" stroke="#f1e3c6" stroke-width="22" stroke-linecap="round"/>')
    # gli alberi, lontani dalle zone e dal lago
    alberi = []
    prove = 0   # 21/10: con una zona in più lo spazio libero cala: si smette dopo tanti tentativi (prima girava all'infinito)
    while len(alberi) < 70 and prove < 20000:
        prove += 1
        x, y = rnd.randint(110, 1290), rnd.randint(110, 800)
        if any((x - z[1]) ** 2 + (y - z[2]) ** 2 < 150 ** 2 for z in ZONE): continue
        if ((x - 700) / 190) ** 2 + ((y - 505) / 105) ** 2 < 1: continue
        if any((x - a) ** 2 + (y - b) ** 2 < 40 ** 2 for a, b in alberi): continue
        alberi.append((x, y))
    for x, y in alberi:
        r = rnd.randint(13, 22)
        s.append(f'<rect x="{x - 3}" y="{y}" width="6" height="{r}" fill="#8d5a2b"/><circle cx="{x}" cy="{y}" r="{r}" fill="{rnd.choice(["#2f9e44", "#37b24d", "#40c057", "#2b8a3e"])}"/>')
    # la ferrovia del parco, tutto intorno
    rail = "M120,70 H1280 Q1340,70 1340,130 V790 Q1340,850 1280,850 H120 Q60,850 60,790 V130 Q60,70 120,70 Z"
    s.append(f'<path id="rail" d="{rail}" fill="none" stroke="#6d4c2f" stroke-width="20"/>')
    s.append(f'<path d="{rail}" fill="none" stroke="#8a6a49" stroke-width="18" stroke-dasharray="4 10"/>')
    s.append(f'<path d="{rail}" fill="none" stroke="#ced4da" stroke-width="2.5" transform="translate(0,0)"/>')
    s.append('<g><g transform="translate(-34,-14)"><rect width="46" height="26" rx="5" fill="#c92a2a"/><rect x="30" y="-10" width="12" height="14" fill="#c92a2a"/>'
             '<rect x="6" y="5" width="14" height="10" fill="#fff8e6"/><circle cx="10" cy="28" r="6" fill="#343a40"/><circle cx="36" cy="28" r="6" fill="#343a40"/>'
             '<rect x="-34" y="4" width="30" height="20" rx="4" fill="#1c7ed6"/><circle cx="-26" cy="28" r="5" fill="#343a40"/><circle cx="-10" cy="28" r="5" fill="#343a40"/></g>'
             '<animateMotion dur="48s" repeatCount="indefinite" rotate="auto"><mpath href="#rail"/></animateMotion></g>')
    # le zone
    for (zid, x, y, c, tit, sub, link, tipo, *_r) in ZONE:
        lw = max(len(tit) * 10.5, len(sub) * 7.6) + 30
        inner = (f'<g transform="translate({x},{y})" class="zona"><ellipse cx="0" cy="24" rx="70" ry="12" fill="#000" opacity=".12"/>'
                 f'<g filter="url(#ombra)">{edificio(tipo, c)}</g>'
                 f'<rect x="{-lw / 2:.0f}" y="34" width="{lw:.0f}" height="50" rx="12" fill="#fffdf7" stroke="{c}" stroke-width="3"/>'
                 f'<text x="0" y="56" text-anchor="middle" class="t1">{e(tit)}</text><text x="0" y="75" text-anchor="middle" class="t2">{e(sub)}</text></g>')
        s.append(f'<a href="{e(u(link))}" target="_blank">{inner}</a>' if link else inner)
    s.append('<text x="700" y="44" text-anchor="middle" class="tt">IL PARCO DEL CORSO DI INFORMATICA</text>')
    s.append('</svg>')
    return "\n".join(s)

GH = "https://github.com/nicolaregge-pulse/corso-informatica/blob/main/"
DOCUMENTI = [   # i documenti del prof: si aprono su GitHub (il PDF si legge impaginato)
 ("Come lavoriamo", [("Il modo di lavorare (Modus operandi)", "20261012_Modus-Operandi_Docente_v1.5.pdf"), ("La metodologia del corso", "METODOLOGIA-CORSO-v1.3.pdf"),
   ("Le regole per costruire una lezione", "20261009_Regole-Costruzione-Teoria_Docente_v1.2.pdf"), ("Riferimenti e decisioni", "RIFERIMENTI-E-DECISIONI.md")]),
 ("In classe", [("Il giro delle Pull Request", "20261012_Giro-Pull-Request_Docente_v1.0.pdf"), ("Ripasso, verifica e recupero: come si rifà", "20261013_Verifica-Come-Si-Fa_Docente_v1.0.pdf"),
   ("I rami delle classi e il gioco", "20261012_Organizzazione-Rami-Classi_Docente_v1.1.pdf"), ("Guida al gioco della classe", "manuale-docenti/gioco-della-classe/20261008_Gioco-Della-Classe_Guida-Docente_v1.1.pdf")]),
 ("Strumenti e automazione", [("Strumenti per il registro e la classe virtuale", "manuale-docenti/strumenti-didaweb-google/20261007_Strumenti-DIDAweb-Google_Docente_v1.3.pdf"),
   ("Inventario degli strumenti e dell'automazione", "20261007_Inventario-Strumenti-e-Automazione_Docente_v1.0.pdf")]),
 ("Le regole fisse", [("Il patto e il flusso che funziona (MANIFESTO)", "MANIFESTO.md"), ("Il cruscotto dal vivo: come funziona", "20261019_Cruscotto-Dal-Vivo_Docente_v1.0.pdf"), ("Audit: il monitoraggio dal vivo", "AUDIT-MONITORAGGIO-DAL-VIVO.md"),
   ("Regia della 3INF del 19/10 (portfolio)", "classe-3/sito-github/20261019_Classe-3_Regia-Portfolio_Docente_v1.0.pdf"), ("Orario della settimana 19-23/10", "orario/settimana-2026-10-19.md")]),
 ("Migliorare", [("Revisione e retrospettiva (Agile)", "20261013_Agile-Cerimonie_Docente_v1.2.pdf"), ("Le retrospettive, come storia", "RETROSPETTIVE.md"),
   ("Il registro degli errori di Claude", "REGISTRO-ERRORI-CLAUDE.md"), ("Le prove che il metodo funziona", "PROVE-METODO.md")]),
 ("Comunicazione", [("Comunicazione e marketing", "comunicazione-marketing/README.md"), ("Le edizioni e come si controllano", "comunicazione-marketing/EDIZIONI.md"),
   ("Questo Atlante in PDF", "20261013_Atlante_Docente_v{vers}.pdf")]),
]

def documenti(vers):
    h = []
    for tit, voci in DOCUMENTI:
        li = "".join(f'<li><a href="{e(GH + f.replace("{vers}", vers))}" target="_blank">{e(t)}</a></li>' for t, f in voci)
        h.append(f'<div class="sc" style="border-top:6px solid #8d5a2b"><h3>{e(tit)}</h3><ol>{li}</ol></div>')
    return '<h2>I documenti del prof</h2><p class="mu">Si aprono su GitHub: i PDF si leggono impaginati, con il bottone per scaricarli.</p><div class="schede">' + "".join(h) + "</div>"

def schede():
    h = []
    for (zid, x, y, c, tit, sub, link, tipo, descr, links) in ZONE:
        li = "".join(f'<li><a href="{e(u(l))}" target="_blank">{e(t)}</a></li>' for t, l in links) or '<li class="mu">Nessun link: è riservato.</li>'
        h.append(f'<div class="sc" style="border-top:6px solid {c}"><h3>{e(tit)}</h3><p class="mu">{e(descr)}</p><ol>{li}</ol></div>')
    return '<div class="schede">' + "".join(h) + "</div>"

def main():
    md = open(os.path.join(QUI, "ATLANTE.md"), encoding="utf-8").read()
    edz = json.load(open(os.path.join(QUI, "comunicazione-marketing", "EDIZIONE.json"), encoding="utf-8"))["edizione"]
    vers = re.search(r"\*\*Versione (\d+\.\d+)\*\*", md).group(1)
    md = re.sub(r"(?m)^   (?=\d+\. )", "    ", md)          # sottoliste a 3 spazi -> 4 (python-markdown)
    corpo = documenti(vers) + markdown.markdown(md.split("\n", 1)[1], extensions=["tables"])
    css = """:root{--bg:#fbf8f3;--fg:#1d1a16;--mu:#62584c;--card:#fff;--bd:#e3dacd;--link:#1c5fb8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15120f;--fg:#f6efe4;--mu:#bcae9b;--card:#211c17;--bd:#3a3128;--link:#74b0ff}}
:root[data-theme="dark"]{--bg:#15120f;--fg:#f6efe4;--mu:#bcae9b;--card:#211c17;--bd:#3a3128;--link:#74b0ff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 "Segoe UI",system-ui,Arial,sans-serif}
.w{max-width:1180px;margin:0 auto;padding:22px 16px 60px}a{color:var(--link)}
h1{font-size:clamp(30px,4.5vw,46px);margin:4px 0}h2{font-size:24px;margin-top:34px;border-bottom:2px solid var(--bd);padding-bottom:4px;break-after:avoid}
.mappa{width:100%;height:auto;display:block;border-radius:22px;box-shadow:0 8px 30px #0003}
.mappa .t1{font:700 18px "Segoe UI",Arial,sans-serif;fill:#1d1a16}.mappa .t2{font:13px "Segoe UI",Arial,sans-serif;fill:#62584c}.mappa .tt{font:800 22px "Segoe UI",Arial,sans-serif;fill:#fffdf7;letter-spacing:.12em}
.mappa a .zona{transition:transform .2s;transform-box:fill-box;transform-origin:center}.mappa a:hover .zona{filter:brightness(1.08)}
.mu{color:var(--mu)}.schede{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:22px}
.sc{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:14px 16px;break-inside:avoid}.sc h3{margin:0 0 4px}.sc p{margin:0 0 8px;font-size:15px}.sc ol{margin:0;padding-left:20px;font-size:15px}
table{border-collapse:collapse;width:100%}td,th{border:1px solid var(--bd);padding:6px 8px;text-align:left;vertical-align:top}th{background:var(--card)}
.sotto{font-size:15px}code{overflow-wrap:anywhere}@media (max-width:600px){table{display:block;overflow-x:auto;max-width:100%}}
@media print{body{font-size:12px;background:#fff;color:#111}.w{padding:0;max-width:none}.mappa{box-shadow:none;width:auto;height:150mm;margin:0 auto}h1{font-size:26px}h2{font-size:17px}.sc{padding:8px 10px}.schede{gap:8px}@page{size:A4 landscape;margin:12mm}}"""
    pagina = f"""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><meta name="versione" content="{vers}">
<title>Atlante del corso</title><meta name="description" content="La mappa illustrata e cliccabile del corso di informatica e l'Atlante: che cosa c'è, dove sta, come si lavora.">
<style>{css}</style></head><body><div class="w">
<div class="mu">Il laboratorio di informatica secondo le idee di Nicola Regge · Area Docente · versione {vers} · edizione {edz}</div>
<h1>Atlante del corso</h1>
<p class="mu sotto">Clicca una zona del parco per andarci. Sotto la mappa trovi le stesse zone con tutti i loro link, e poi l'Atlante da leggere.</p>
{mappa()}
<h2>Le zone del parco</h2>
{schede()}
{corpo}
</div></body></html>"""
    scrivi(pagina, os.path.join(QUI, "docs", CARTELLA), os.path.join(QUI, f"20261013_Atlante_Docente_v{vers}.pdf"))
    # la versione per la comunicazione: la mappa e le zone, niente testo interno, niente cruscotti né pagine del docente
    pubbl = pagina.replace(corpo, "").replace("Area Docente · versione " + vers, "Il parco del corso · versione " + VERS_PARCO).replace(
        "Sotto la mappa trovi le stesse zone con tutti i loro link, e poi l'Atlante da leggere.", "Sotto la mappa trovi le stesse zone, con i loro link.")
    pubbl = re.sub(r'<li><a href="[^"]*(cruscotto|valutazione|controlla|docenti|avanzamento|mio-punto|prof-pubblica|corso-informatica-riservato)[^"]*"[^>]*>[^<]*</a></li>', "", pubbl)
    # i progetti di stage: fuori si vede solo la pagina di presentazione, senza i nomi negli indirizzi
    pubbl = re.sub(r'<li><a href="[^"]*4ti-progetti/"[^>]*>[^<]*</a></li>', "", pubbl).replace(u("4ti-progetti/"), u("cm-qma7yay4q5/progetti/"))
    pubbl = pubbl.replace('href="' + u("docenti/") + '"', 'href="#"').replace("<ol></ol>", '<ol><li class="mu">Gli strumenti del docente sono riservati.</li></ol>')
    pubbl = pubbl.replace('<meta name="versione" content="' + vers + '">', '<meta name="versione" content="' + VERS_PARCO + '">')
    pubbl = pubbl.replace("<title>Atlante del corso</title>", "<title>Il parco del corso</title>").replace("<h1>Atlante del corso</h1>", "<h1>Il parco del corso</h1>")
    scrivi(pubbl, os.path.join(QUI, "docs", "cm-qma7yay4q5", "parco"), os.path.join(QUI, "docs", "cm-qma7yay4q5", "pdf", f"20261013_Il-Parco-del-Corso_v{VERS_PARCO}.pdf"))

def scrivi(pagina, out, pdf):
    os.makedirs(out, exist_ok=True)
    f = os.path.join(out, "index.html"); open(f, "w", encoding="utf-8").write(pagina)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + f],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f, pdf)

if __name__ == "__main__":
    main()
