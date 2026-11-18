# -*- coding: utf-8 -*-
"""Guida 3INF «Il mio sito cambia casa» (v1.1, 18/11/2026: nuovo passo 2 «Cambia il nome del repository»; la v1.0 resta in cartella) + pagina docente (riservata).
Uscite: docs/3inf/guida-organizzazione/guida-trasferire-sito-it-v1-1.pdf e ...-it-bn-v1-1.pdf (bangla solo PC 14);
        riservato report/2026-11-18/PAGINA-DOCENTE-TRASFERIMENTO-REPO-v1.0.(md|pdf) con --docente.
Uso: python3 strumenti/genera_guida_organizzazione_3inf.py"""
import html, os, subprocess, sys, tempfile

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RADICE, "docs/3inf/guida-organizzazione")
RIS = "/home/user/corso-informatica-riservato/report/2026-11-18"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
e = html.escape
ORG = "piamarta-informatica-2026-27"

def hl(t, cls="hl"):
    return f"<span class='{cls}'>{e(t)}</span>"

# Disegni (schemi dichiarati): box con la parte da cliccare evidenziata
def mock(titolo, righe):
    r = "".join(f"<div class='mr'>{x}</div>" for x in righe)
    return f"<div class='mock'><div class='mt'>{e(titolo)}</div>{r}</div>"

M1 = mock("Disegno: la tua mail o la pagina dell'invito", [
    "Invito a <b>" + ORG + "</b>", "<span class='btn'>Join</span> <span class='hint'>← clicca qui</span>"])
M2 = mock("Disegno: il tuo repository su GitHub", [
    "<span class='tab'>Code</span> <span class='tab'>Issues</span> <span class='tab sel'>Settings</span> <span class='hint'>← clicca Settings</span>"])
M3 = mock("Disegno: Settings, in fondo alla pagina", [
    "<span class='dz'>Danger Zone</span>", "<span class='btn red'>Transfer ownership</span> <span class='hint'>← clicca qui</span>"])
M4 = mock("Disegno: la finestra che si apre", [
    "New owner's GitHub username or organization name", "<span class='inp'>" + ORG + "</span> <span class='hint'>← scrivi qui</span>",
    "Type the repository name to confirm", "<span class='inp'>mio-sito-COGNOME</span> <span class='hint'>← scrivi qui</span>",
    "<span class='btn red'>I understand, transfer this repository</span>"])
M6 = mock("Disegno: Settings → General", [
    "Repository name", "<span class='inp'>mio-sito-COGNOME</span> <span class='hint'>← scrivi qui</span>",
    "<span class='btn'>Rename</span> <span class='hint'>← clicca Rename</span>"])
M5 = mock("Disegno: Settings → Pages", [
    "Branch: <span class='inp'>main</span> &nbsp; Folder: <span class='inp'>/ (root)</span>", "<span class='btn'>Save</span> <span class='hint'>← clicca Save</span>"])

# (it, bn) frasi; ogni passo: titolo, lista di azioni, disegno
STEPS = [
 (("1", "Accetta l'invito", "ধাপ ১: আমন্ত্রণ গ্রহণ করো"), [
  ("Apri la mail del tuo account GitHub (@studenti.piamarta.it).", "তোমার GitHub অ্যাকাউন্টের মেইল খোলো (@studenti.piamarta.it)।"),
  ("Oppure apri questo indirizzo.", "অথবা এই ঠিকানা খোলো।")], "ADDR1", M1,
  [("Premi «Join».", "«Join» চাপো।")]),
 (("2", "Trasferisci il tuo repository", "ধাপ ২: তোমার repository সরাও"), [
  ("Apri il tuo repository (quello del sito) su GitHub.", "GitHub-এ তোমার repository (সাইটের) খোলো।"),
  ("Clicca «Settings».", "«Settings» চাপো।")], None, M2,
  [("Scorri in fondo fino a «Danger Zone».", "একদম নিচে «Danger Zone» পর্যন্ত যাও।"),
   ("Clicca «Transfer ownership».", "«Transfer ownership» চাপো।")]),
]
STEP2B = ([("Scrivi come nuovo proprietario:", "নতুন মালিক হিসেবে লেখো:"),
           ("Scrivi il nome del repository per confermare.", "নিশ্চিত করতে repository-র নাম লেখো।"),
           ("Clicca «I understand, transfer this repository».", "«I understand, transfer this repository» চাপো।")])
RASSICURA = ("Non è pericoloso: il tuo sito cambia solo casa.", "বিপজ্জনক নয়: তোমার সাইট শুধু নতুন বাড়িতে যায়।")

TAB = [
 ("Non vedo «Transfer ownership».", "Non sei il proprietario. Controlla di essere entrato con il TUO account."),
 ("Non trovo il nome dell'organizzazione.", "Non hai accettato l'invito. Torna al passo 1."),
 ("Il sito mostra «404».", "Aspetta due minuti. Poi ricontrolla Settings → Pages."),
 ("Ho un dubbio.", "Chiedi all'assistente."),
]
TAB_BN = [
 ("«Transfer ownership» দেখছি না।", "তুমি মালিক নও। নিজের অ্যাকাউন্টে ঢুকেছ কিনা দেখো।"),
 ("সংগঠনের নাম খুঁজে পাচ্ছি না।", "তুমি আমন্ত্রণ নাওনি। ধাপ ১-এ ফিরে যাও।"),
 ("সাইটে «404» দেখাচ্ছে।", "দুই মিনিট অপেক্ষা করো। তারপর Settings → Pages আবার দেখো।"),
 ("আমার সন্দেহ আছে।", "সহকারীকে জিজ্ঞেস করো।"),
]
CHECK = [
 ("Ho premuto «Join».", "আমি «Join» চেপেছি।"),
 ("Ho cambiato il nome in mio-sito-COGNOME.", "আমি নাম বদলে mio-sito-COGNOME করেছি।"),
 ("Ho trasferito il repository del sito.", "আমি সাইটের repository সরিয়েছি।"),
 ("Se ne ho due, li ho trasferiti tutti e due.", "দুটি থাকলে দুটিই সরিয়েছি।"),
 ("Ho attivato Pages: main e / (root), poi Save.", "আমি Pages চালু করেছি: main আর / (root), তারপর Save।"),
 ("Il nuovo indirizzo si apre.", "নতুন ঠিকানা খোলে।"),
 ("L'ho scritto nel Documento di consegna («Il mio sito»).", "Documento di consegna-য় («Il mio sito») লিখেছি।"),
]

def guida(bn):
    b = lambda t: f"<div class='bn' lang='bn'>{e(t)}</div>" if bn else ""
    def az(lst):
        return "".join(f"<li>{e(i)}{b(n)}</li>" for i, n in lst)
    s = ""
    # passo 1
    s += f"<div class='st'><h2><span class='n'>1</span> Accetta l'invito</h2>{b('ধাপ ১: আমন্ত্রণ গ্রহণ করো')}<div class='row'><ol>{az(STEPS[0][1])}</ol></div>"
    s += f"<div class='box'>https://github.com/orgs/{ORG}/invitation</div><div class='row'>{M1}<ol start='3'>{az(STEPS[0][4])}</ol></div></div>"
    # passo 2 (nuovo in v1.1): cambia il nome
    s += f"<div class='st'><h2><span class='n'>2</span> Cambia il nome del repository</h2>{b('ধাপ ২: repository-র নাম বদলাও')}"
    s += f"<div class='ok'>{e('GitHub non accetta due repository con lo stesso nome nell' + chr(39) + 'organizzazione: tanti di voi hanno «mio-sito».')}{b('সংগঠনে একই নামের দুটি repository GitHub নেয় না: তোমাদের অনেকের «mio-sito» আছে।')}</div>"
    s += f"<div class='row'>{M2}<ol>{az([('Apri il tuo repository (quello del sito) su GitHub.', 'GitHub-এ তোমার repository (সাইটের) খোলো।'), ('Clicca «Settings», poi «General».', '«Settings» চাপো, তারপর «General»।')])}</ol></div>"
    s += f"<div class='row'>{M6}<ol start='3'>{az([('Nella casella «Repository name» scrivi il nuovo nome.', '«Repository name» ঘরে নতুন নাম লেখো।'), ('Clicca «Rename».', '«Rename» চাপো।')])}</ol></div>"
    s += f"<div class='box'>mio-sito-COGNOME</div>"
    s += f"<ol start='5'>{az([('COGNOME è il tuo cognome, tutto minuscolo, senza spazi (se ha spazi usa il trattino -).', 'COGNOME হল তোমার পদবি, সব ছোট অক্ষরে, ফাঁকা ছাড়া (ফাঁকা থাকলে হাইফেন - দাও)।'), ('Esempio: Rossi diventa mio-sito-rossi.', 'উদাহরণ: Rossi হয় mio-sito-rossi।')])}</ol>"
    s += f"<div class='ok'>{e('Il vecchio indirizzo del sito smette di funzionare: è normale, il nuovo è al passo 6.')}{b('সাইটের পুরনো ঠিকানা আর কাজ করবে না: এটা স্বাভাবিক, নতুনটা ধাপ ৬-এ।')}</div></div>"
    # passo 3
    s += f"<div class='st'><h2><span class='n'>3</span> Trasferisci il tuo repository</h2>{b('ধাপ ৩: তোমার repository সরাও')}"
    s += f"<div class='ok'>{e(RASSICURA[0])}{b(RASSICURA[1])}</div>"
    s += f"<div class='row'>{M2}<ol>{az(STEPS[1][1])}</ol></div>"
    s += f"<div class='row'>{M3}<ol start='3'>{az(STEPS[1][4])}</ol></div>"
    s += f"<div class='row'>{M4}<ol start='5'>{az(STEP2B[:1])}</ol></div><div class='box'>{ORG}</div>"
    s += f"<ol start='6'>{az(STEP2B[1:])}</ol></div>"
    # passo 3
    s += f"<div class='st brk'><h2><span class='n'>4</span> Hai DUE repository?</h2>{b('ধাপ ৪: তোমার দুটি repository আছে?')}<ol>{az([('Per esempio il vecchio e sito-personale: dai un nome diverso a ciascuno (per esempio mio-sito-COGNOME e sito-personale-COGNOME).', 'যেমন পুরনোটা আর sito-personale: প্রত্যেকটাকে আলাদা নাম দাও (যেমন mio-sito-COGNOME আর sito-personale-COGNOME)।'), ('Trasferisci TUTTI e due, uno alla volta.', 'দুটিই সরাও, একটা একটা করে।')])}</ol></div>"
    # passo 4
    s += f"<div class='st'><h2><span class='n'>5</span> Riattiva Pages</h2>{b('ধাপ ৫: Pages আবার চালু করো')}<div class='row'>{M5}<ol>{az([('Apri il repository nella nuova casa.', 'নতুন বাড়িতে repository খোলো।'), ('Vai in Settings → Pages.', 'Settings → Pages-এ যাও।'), ('Scegli «Branch: main» e «/ (root)».', '«Branch: main» আর «/ (root)» বেছে নাও।'), ('Clicca «Save».', '«Save» চাপো।')])}</ol></div></div>"
    # passo 5
    s += f"<div class='st'><h2><span class='n'>6</span> Il nuovo indirizzo del sito</h2>{b('ধাপ ৬: সাইটের নতুন ঠিকানা')}<div class='box'>https://{ORG}.github.io/mio-sito-COGNOME/</div>"
    s += f"<ol>{az([('COGNOME è lo stesso del passo 2.', 'COGNOME হল ধাপ ২-এর মতোই।'), ('Esempio: Rossi, indirizzo .../mio-sito-rossi/', 'উদাহরণ: Rossi, ঠিকানা .../mio-sito-rossi/'), ('Il vecchio indirizzo non funziona più.', 'পুরনো ঠিকানা আর কাজ করে না।'), ('Apri il nuovo indirizzo.', 'নতুন ঠিকানা খোলো।'), ('Non si apre? Aspetta 1-2 minuti e riprova.', 'খোলে না? ১-২ মিনিট অপেক্ষা করো, আবার চেষ্টা করো।')])}</ol></div>"
    # passo 6
    s += f"<div class='st'><h2><span class='n'>7</span> Scrivi l'indirizzo nel Documento di consegna</h2>{b('ধাপ ৭: Documento di consegna-য় ঠিকানা লেখো')}<ol>{az([('Apri il Documento di consegna.', 'Documento di consegna খোলো।'), ('Trova la riga «Il mio sito».', '«Il mio sito» লাইনটা খুঁজে নাও।'), ('Scrivi lì il nuovo indirizzo.', 'ওখানে নতুন ঠিকানা লেখো।')])}</ol></div>"
    # checklist
    c = "".join(f"<tr><td class='c'>☐</td><td>{e(i)}{b(n)}</td></tr>" for i, n in CHECK)
    s += f"<div class='st brk'><h2><span class='n'>8</span> Ho fatto</h2>{b('ধাপ ৮: আমি করেছি')}<table>{c}</table></div>"
    t = "".join(f"<tr><td><b>{e(p)}</b>{b(TAB_BN[k][0])}</td><td>{e(r)}{b(TAB_BN[k][1])}</td></tr>" for k, (p, r) in enumerate(TAB))
    s += f"<div class='st'><h2>Se qualcosa non va</h2>{b('কিছু ঠিক না হলে')}<table class='tb'><tr><th>Problema</th><th>Cosa fare</th></tr>{t}</table></div>"
    dich = "Guida non ancora provata con un account di allievo: i passi sono quelli di GitHub, da controllare con il primo allievo."
    dbn = "এই গাইড এখনও কোনো ছাত্রের অ্যাকাউন্টে পরীক্ষা করা হয়নি: ধাপগুলো GitHub-এর, প্রথম ছাত্রের সঙ্গে দেখে নিতে হবে।"
    return f"""<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><style>{CSS(bn)}</style></head><body>
<h1>Il mio sito cambia casa</h1>{b('আমার সাইট নতুন বাড়িতে যায়')}
<div class='dich'>{e(dich)}{b(dbn)}</div>{s}</body></html>"""

def CSS(bn):
    fs = "14px" if bn else "17px"
    return f"""@page{{size:A4;margin:11mm 13mm}}
body{{font-family:'Inter','Noto Sans','Noto Sans Bengali',Arial,sans-serif;color:#14202b;margin:0;font-size:{fs}}}
h1{{font-size:28px;margin:0 0 4px;color:#12467a}} h2{{font-size:{'18px' if bn else '21px'};margin:8px 0 2px;color:#12467a}}
.n{{display:inline-block;background:#0b57d0;color:#fff;border-radius:50%;width:28px;height:28px;text-align:center;line-height:28px;margin-right:6px}}
.bn{{font-size:{'12.5px'};font-weight:400;color:#3a4a5a;margin:0 0 2px}} ol{{margin:3px 0 3px 22px;padding:0;font-weight:600}} li{{margin:{'2px' if bn else '4px'} 0}}
.st{{border-top:2px solid #c9d3e0;padding-bottom:2px}} .brk{{break-before:page}} .row{{display:flex;gap:12px;align-items:center}}
.mock{{flex:0 0 55%;border:2px solid #7a8aa0;border-radius:8px;padding:5px 8px;background:#f4f7fb;font-size:12.5px;break-inside:avoid}}
.mt{{font-size:10.5px;color:#4a5968;margin-bottom:3px}} .mr{{margin:3px 0}}
.btn{{display:inline-block;background:#1f883d;color:#fff;font-weight:700;padding:2px 10px;border-radius:5px;outline:3px solid #e8590c}} .btn.red{{background:#cf222e}}
.hint{{color:#e8590c;font-weight:700}} .tab{{padding:2px 7px;border:1px solid #bbb;border-radius:4px;background:#fff}} .tab.sel{{outline:3px solid #e8590c}}
.dz{{color:#cf222e;font-weight:700;border-bottom:1px solid #cf222e}} .inp{{border:1px solid #888;background:#fff;padding:1px 6px;outline:3px solid #e8590c;border-radius:4px}}
.box{{background:#fff6d6;border:2px solid #e0b400;border-radius:8px;padding:5px 10px;font-family:monospace;font-size:{'13px' if bn else '15px'};font-weight:700;margin:4px 0;word-break:break-all}}
.ok{{background:#e6f6ea;border:2px solid #1f883d;border-radius:8px;padding:4px 10px;font-weight:700;margin:3px 0}}
.dich{{background:#fdecea;border:2px solid #cf222e;border-radius:8px;padding:4px 10px;font-size:12.5px;font-weight:600;margin:4px 0}}
table{{border-collapse:collapse;width:100%}} td,th{{border-bottom:1px solid #c9d3e0;padding:5px 6px;text-align:left;vertical-align:top}}
td.c{{font-size:24px;width:34px;color:#0b57d0;text-align:center}} .tb th{{background:#12467a;color:#fff}} .tb td,.tb th{{border:1px solid #c9d3e0}}"""

def stampa(h, dest):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "g.html"); open(p, "w", encoding="utf-8").write(h)
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + dest, "file://" + p], capture_output=True)
    print(dest, [r for r in subprocess.run(["pdfinfo", dest], capture_output=True, text=True).stdout.splitlines() if r.startswith("Pages")])

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    stampa(guida(False), os.path.join(OUT, "guida-trasferire-sito-it-v1-1.pdf"))
    stampa(guida(True), os.path.join(OUT, "guida-trasferire-sito-it-bn-v1-1.pdf"))
