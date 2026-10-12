# -*- coding: utf-8 -*-
"""Compila i file Word dell'Allegato A 2026/27 con le parti del prof. Regge.

Fonte delle voci: PROGRAMMA-PREVENTIVO-2026-27.md (una sezione per classe, una per competenza).
Ogni voce va nella riga dell'annualità giusta della competenza, sotto l'etichetta «Regge»,
evidenziata in GIALLO (= prevista). Durante l'anno: voce fatta -> si toglie il giallo;
voce non fatta -> si cancella.

Uso:  python3 programmi-ufficiali/_build/compila_allegati.py [versione]
Esce in programmi-ufficiali/2026-27/: un .docx e un .pdf per classe.
"""
import copy, os, re, subprocess, sys
import docx
from docx.enum.text import WD_COLOR_INDEX

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UFF = os.path.join(ROOT, "programmi-ufficiali")
OUT = os.path.join(UFF, "2026-27")
VER = sys.argv[1] if len(sys.argv) > 1 else "0.1"
DATA = "20261012"

# classe -> (file dell'anno scorso, riga dell'annualità, nuovo documento?, mappa competenza preventivo -> n. competenza nel file)
OPERATORE = {"12": "12", "14": "14", "15": "15", "16": "16", "17": "17", "1.2": "2", "trasv.": "8", "9": "9"}
TECNICO = {"12": "13", "14": "10", "15": "16", "16": "14", "17": "13", "1.2": "2", "trasv.": "7", "9": "8"}
CLASSI = {
    "Classe 1": ("ALLEGATO-A_PFP1_Operatore_2025-26.docx", "I Anno", True, OPERATORE, "1INF"),
    "Classe 2": ("ALLEGATO-A_PFP1_Operatore_2025-26.docx", "II Anno", False, OPERATORE, "2INF"),
    "Classe 3": ("ALLEGATO-A_PFP2_Operatore_2025-26.docx", "III Anno", False, OPERATORE, "3INF"),
    "Classe 4": ("ALLEGATO-A_PFP4_Tecnico_2025-26.docx", "IV Anno", True, TECNICO, "4TI"),
}
# voci che nel Tecnico vanno in una competenza diversa dalla loro sezione
TECNICO_VOCE = {"Sicurezza di rete": "15"}


def leggi_preventivo():
    s = open(os.path.join(ROOT, "PROGRAMMA-PREVENTIVO-2026-27.md"), encoding="utf-8").read()
    s = s.split("## Registro delle versioni")[0]
    classi, cl, comp = {}, None, None
    for riga in s.splitlines():
        m = re.match(r"## (Classe \d)", riga)
        if m:
            cl = m.group(1); classi[cl] = []; comp = None; continue
        m = re.match(r"### Competenza (\S+)", riga)
        if m and cl:
            comp = (m.group(1), []); classi[cl].append(comp); continue
        t = riga.strip()
        if cl and comp and t and not t.startswith(("#", ">", "*", "---")):
            comp[1].append(t)
    return classi


def tabella_competenza(d, numero):
    for t in d.tables[1:]:
        for r in t.rows[:4]:
            tx = r.cells[0].text.replace("\n", " ")
            if re.search(r"(^|\s)%s\s*\." % re.escape(numero), tx) and "Compet" in tx:
                return t
    raise SystemExit("competenza %s non trovata" % numero)


def cella_anno(t, anno):
    for r in t.rows:
        if r.cells[0].text.strip().startswith(anno):
            return r.cells[0]
    for i, r in enumerate(t.rows):  # nessuna riga «IV Anno»: si usa quella sotto «Argomenti»
        if r.cells[0].text.strip().lower().startswith("argomenti"):
            return t.rows[i + 1].cells[0]
    raise SystemExit("riga %s non trovata" % anno)


def svuota(cella, anno):
    """Documento nuovo: resta solo il titolo dell'annualità (il testo dell'anno scorso era di un'altra classe)."""
    ps = cella.paragraphs
    for p in ps[1:]:
        p._p.getparent().remove(p._p)
    p0 = ps[0]
    for r in p0.runs[1:]:
        r._r.getparent().remove(r._r)
    if p0.runs:
        p0.runs[0].text = anno
        p0.runs[0].font.highlight_color = None


def aggiungi(cella, voci, etichetta):
    modello = cella.paragraphs[0]
    font = next((r.font for r in modello.runs if r.text.strip()), None)

    def nuovo(testo, grassetto=False, giallo=False):
        p = cella.add_paragraph()
        if modello._p.pPr is not None:
            p._p.insert(0, copy.deepcopy(modello._p.pPr))
        r = p.add_run(testo)
        if font is not None:
            r.font.name, r.font.size = font.name, font.size
        r.bold = grassetto or None
        if giallo:
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
        return p

    if etichetta:
        nuovo("")
        nuovo("Regge", grassetto=True)
    for v in voci:
        nuovo(v, giallo=True)


def compila(cl, sezioni):
    src, anno, nuovo_doc, mappa, sigla = CLASSI[cl]
    d = docx.Document(os.path.join(UFF, src))
    h = d.tables[0]
    for r in h.rows[1:]:
        if r.cells[0].text.strip() == anno.split()[0]:
            runs = r.cells[1].paragraphs[0].runs
            if runs:
                runs[0].text = "2026-2027"
                for x in runs[1:]:
                    x.text = ""
            else:
                r.cells[1].paragraphs[0].add_run("2026-2027")
            if nuovo_doc:
                for c in r.cells[2:]:
                    for p in c.paragraphs:
                        for run in p.runs:
                            run.text = ""
    if nuovo_doc:
        anni = ["I", "II", "III", "IV"]
        base = anni.index(anno.split()[0])
        for r in h.rows[1:]:
            k = r.cells[0].text.strip()
            if k in anni:
                a = 2026 + anni.index(k) - base
                runs = r.cells[1].paragraphs[0].runs
                if runs:
                    runs[0].text = "%d-%d" % (a, a + 1)
                    for x in runs[1:]:
                        x.text = ""
    gruppi, svuotate = {}, set()
    for comp, voci in sezioni:
        for v in voci:
            n = mappa[comp]
            if mappa is TECNICO:
                n = next((k for pre, k in TECNICO_VOCE.items() if v.startswith(pre)), n)
            gruppi.setdefault(n, []).append(v)
    for n, voci in gruppi.items():
        cella = cella_anno(tabella_competenza(d, n), anno)
        if nuovo_doc and n not in svuotate:
            svuota(cella, anno); svuotate.add(n)
        aggiungi(cella, voci, etichetta=True)
    if nuovo_doc:  # le altre competenze del documento nuovo restano solo con il titolo dell'annualità
        for t in d.tables[1:]:
            try:
                cella = cella_anno(t, anno)
            except SystemExit:
                continue
            if not any(r.font.highlight_color == WD_COLOR_INDEX.YELLOW and r.text in sum(gruppi.values(), [])
                       for p in cella.paragraphs for r in p.runs):
                svuota(cella, anno)
    os.makedirs(OUT, exist_ok=True)
    nome = "%s_Allegato-A-%s-2026-27_Docente_v%s" % (DATA, sigla, VER)
    path = os.path.join(OUT, nome + ".docx")
    d.save(path)
    print(cl, sigla, "->", nome, {k: len(v) for k, v in gruppi.items()})
    return path


CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
NOTE = [
    "Ogni voce in giallo è prevista per il 2026/27. Quando la fai, togli il giallo; quella che non fai, la cancelli.",
    "Le voci sono sotto l'etichetta «Regge», nella riga dell'annualità della classe.",
    "1INF e 4TI sono documenti nuovi, fatti a partire dal modello dell'anno scorso: le righe dell'annualità degli altri docenti sono vuote, da riempire a loro cura. Mancano I.D. Corso, I.D. Sezione e n. int.",
    "2INF e 3INF continuano il documento della loro classe: la riga dell'anno scorso resta com'era.",
]
DA_CONFERMARE = [
    "Quale documento per ogni classe: 1INF modello PFP1 nuovo; 2INF documento PFP1 (I.D. Corso 55328), riga II Anno; 3INF documento PFP2 (I.D. Corso 45316), riga III Anno; 4TI modello Tecnico nuovo, riga IV Anno.",
    "4TI, competenze del Tecnico: pianificazione, documentazione e programmazione in 13; sicurezza sul lavoro in 10; reti in 14; sicurezza di rete in 15; installazione e web in 16; comunicazione visiva in 2; cittadinanza in 8; glossario e sicurezza digitale in 7.",
    "Glossario e sicurezza digitale (deepfake, phishing): nella Competenza digitale (8 per l'Operatore).",
]


def riepilogo(percorsi):
    import html
    e = html.escape
    parti = []
    for cl, path in percorsi:
        sigla = CLASSI[cl][4]; anno = CLASSI[cl][1]
        d = docx.Document(path)
        righe = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % e(c.text) for c in r.cells) for r in d.tables[0].rows)
        blocchi = []
        for t in d.tables[1:]:
            tit = next((r.cells[0].text.replace("\n", " ") for r in t.rows[:4]
                        if re.search(r"\d+\s*\.", r.cells[0].text) and "Compet" in r.cells[0].text), "")
            try:
                cella = cella_anno(t, anno)
            except SystemExit:
                continue
            voci = [p.text for p in cella.paragraphs
                    if any(r.font.highlight_color == WD_COLOR_INDEX.YELLOW for r in p.runs)]
            if voci:
                blocchi.append("<h3>%s</h3><p class=a>%s · Regge</p><ol>%s</ol>" % (
                    e(tit[:160]), e(anno), "".join("<li><mark>%s</mark></li>" % e(v) for v in voci)))
        parti.append("<section><h2>%s · %s (%s)</h2><table>%s</table>%s</section>" % (
            sigla, cl, e(os.path.basename(path)), righe, "".join(blocchi)))
    corpo = """<!doctype html><html lang=it><meta charset=utf-8><style>
@page{size:A4;margin:16mm 14mm}body{font:11pt/1.4 'DejaVu Sans',Arial,sans-serif;color:#111}
h1{font-size:20pt;margin:0 0 4px}h2{font-size:15pt;margin:0 0 8px;break-after:avoid}
h3{font-size:10.5pt;margin:12px 0 2px;break-after:avoid}.a{margin:0;color:#555;font-size:9.5pt}
section{break-before:page}ol{margin:4px 0 0 0;padding-left:22px}li{margin:1px 0}mark{background:#fff200}
table{border-collapse:collapse;margin:0 0 6px;font-size:9.5pt}td{border:1px solid #999;padding:2px 6px}
.box{border-left:5px solid;padding:6px 10px;margin:10px 0}.g{border-color:#d4b000;background:#fffbe0}.b{border-color:#1f6feb;background:#eef4ff}
</style><h1>00 Allegato A 2026/27 — le parti del prof. Regge</h1>
<p><b>Versione %s</b> — 12/10/2026 — Area Docente. Riepilogo dei quattro file Word, letto dai file stessi.</p>
<div class="box g"><b>Nota.</b><ol>%s</ol></div><div class="box b"><b>Da confermare.</b><ol>%s</ol></div>%s</html>""" % (
        VER, "".join("<li>%s</li>" % e(x) for x in NOTE), "".join("<li>%s</li>" % e(x) for x in DA_CONFERMARE), "".join(parti))
    h = os.path.join(OUT, "_riepilogo.html")
    open(h, "w", encoding="utf-8").write(corpo)
    pdf = os.path.join(OUT, "%s_Allegato-A-2026-27-Riepilogo_Docente_v%s.pdf" % (DATA, VER))
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + pdf, "file://" + h], capture_output=True)
    os.remove(h)
    print("riepilogo ->", pdf)


if __name__ == "__main__":
    prev = leggi_preventivo()
    riepilogo([(cl, compila(cl, prev[cl])) for cl in CLASSI])
