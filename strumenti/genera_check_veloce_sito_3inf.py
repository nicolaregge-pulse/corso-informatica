# -*- coding: utf-8 -*-
"""Check veloce 3INF «Sito Stage» (v1.0, 18/11/2026): UNA pagina A4 con le caselle da spuntare e il rimando al passo
del tutorial (genera_tutorial_sito_3inf.py, v1.1). Due uscite: italiano e italiano + bangla (PC 14).
Uso: python3 strumenti/genera_check_veloce_sito_3inf.py   (scrive docs/3inf/sito-stage/Check-Veloce-Sito-Stage-IT[-BN]-v1.0.pdf
e le copie in classe-3/sito-stage/ con il nome 20261118_Classe-3_Check-Veloce_..._v1.0.pdf)"""
import base64, html, os, shutil, subprocess, tempfile

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITO = os.path.join(RADICE, "docs/3inf/sito-stage")
CLASSE = os.path.join(RADICE, "classe-3/sito-stage")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
VERSIONE, DATA = "1.0", "18/11/2026"

# (frase italiana, frase bangla, rimando al passo del tutorial v1.1)
RIGHE = [
    ("Ho creato la cartella sito-personale.", "আমি sito-personale ফোল্ডার বানিয়েছি।", "passo 2"),
    ("Ci sono i 5 file e style.css.", "৫টি ফাইল আর style.css আছে।", "passi 3-7"),
    ("Il menu funziona in ogni pagina.", "প্রতিটি পেজে মেনু কাজ করে।", "passo 8"),
    ("Chi sono, Hobby, Competenze: scritti da me.", "Chi sono, Hobby, Competenze: আমার লেখা।", "passi 4, 5, 6"),
    ("Il mio stage: scritto da me.", "Il mio stage: আমার লেখা।", "passo 7"),
    ("La pagina Presenze stage si apre.", "Presenze stage পেজ খোলে।", "passi 9-10"),
    ("Ho segnato almeno un giorno.", "অন্তত একটি দিন চিহ্নিত করেছি।", "passo 11"),
    ("presenze-stage.json è nella cartella.", "presenze-stage.json ফোল্ডারে আছে।", "passo 12"),
    ("Ho creato sito-personale.zip.", "sito-personale.zip বানিয়েছি।", "passo 15"),
    ("Ho premuto Consegna.", "Consegna চেপেছি।", "passo 15"),
]
TITOLO_BN = "দ্রুত চেক: আমার সাইট"
BASSO = ("Se una riga non è ☑: vai al passo scritto a destra.", "যদি কোনো লাইন ☑ না হয়: ডানদিকে লেখা ধাপে যাও।")
ASSIST = ("Hai un dubbio? Chiedi all'assistente.", "সন্দেহ আছে? সহকারীকে জিজ্ঞেস করো।")
SOTTO = ("Passi di quest'ora: da 1 a 12, poi 15. Dettaglio: Tutorial «Il mio sito: Stage e Presenze».", "এই ঘণ্টার ধাপ: ১ থেকে ১২, তারপর ১৫। বিস্তারিত: Tutorial «Il mio sito: Stage e Presenze»।")


def esc(s):
    return html.escape(s)


def pagina(bn):
    img = base64.b64encode(open(os.path.join(SITO, "img/s-albero.png"), "rb").read()).decode()
    b = lambda t: f"<div class='bn' lang='bn'>{esc(t)}</div>" if bn else ""
    righe = ""
    for it, ben, passo in RIGHE:
        righe += f"<tr><td class='c'>☐</td><td class='t'>{esc(it)}{b(ben)}</td><td class='p'>→ {esc(passo)}</td></tr>"
    return f"""<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><style>
@page{{size:A4;margin:12mm 14mm}}
body{{font-family:'Inter','Noto Sans','Noto Sans Bengali',Arial,sans-serif;color:#14202b;margin:0}}
h1{{font-size:26px;margin:0;color:#12467a}} .sub{{font-size:12px;color:#4a5968;margin:2px 0 8px}}
table{{border-collapse:collapse;width:100%}} td{{border-bottom:1px solid #c9d3e0;padding:{'4px' if bn else '7px'} 6px;vertical-align:middle}}
td.c{{font-size:{'24px' if bn else '28px'};width:36px;color:#0b57d0;text-align:center}} td.t{{font-size:{'16px' if bn else '19px'};font-weight:600}}
td.p{{font-size:{'15px' if bn else '17px'};font-weight:700;color:#b25b00;white-space:nowrap;text-align:right}}
.bn{{font-size:14px;font-weight:400;color:#3a4a5a;margin-top:1px}}
.fine{{display:flex;gap:14px;align-items:center;margin-top:10px}} .fine img{{width:{'215px' if bn else '250px'};border:1px solid #c9d3e0;border-radius:8px}}
.box{{flex:1;background:#fff6d6;border:2px solid #e0b400;border-radius:10px;padding:8px 12px;font-size:{'16px' if bn else '19px'};font-weight:700}}
.box .bn{{font-weight:400;font-size:14px}} .s{{font-size:12px;color:#4a5968;margin-top:6px}}
</style></head><body>
<h1>CHECK VELOCE — Il mio sito</h1>{b(TITOLO_BN)}
<div class='sub'>3INF · Laboratorio · Spunta una riga alla volta.</div>
<table>{righe}</table>
<div class='fine'><img src='data:image/png;base64,{img}' alt='Schema della cartella sito-personale con i file'>
<div class='box'>{esc(BASSO[0])}{b(BASSO[1])}<div style='margin-top:8px'>{esc(ASSIST[0])}{b(ASSIST[1])}</div></div></div>
<div class='s'>{esc(SOTTO[0])}{b(SOTTO[1]) if bn else ''}</div>
<div class='s'>Schema (disegno): la cartella con i file. Versione {VERSIONE} · {DATA}</div>
</body></html>"""


def pdf(bn):
    nome = "Check-Veloce-Sito-Stage-" + ("IT-BN" if bn else "IT") + f"-v{VERSIONE}.pdf"
    dest = os.path.join(SITO, nome)
    with tempfile.TemporaryDirectory() as d:
        h = os.path.join(d, "c.html")
        open(h, "w", encoding="utf-8").write(pagina(bn))
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        "--print-to-pdf=" + dest, "file://" + h], capture_output=True)
    copia = os.path.join(CLASSE, f"20261118_Classe-3_Check-Veloce_{'IT-BN' if bn else 'IT'}_v{VERSIONE}.pdf")
    shutil.copyfile(dest, copia)
    n = subprocess.run(["pdfinfo", dest], capture_output=True, text=True).stdout
    print(dest, [r for r in n.splitlines() if r.startswith("Pages")])


if __name__ == "__main__":
    pdf(False)
    pdf(True)
