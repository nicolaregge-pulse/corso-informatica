# -*- coding: utf-8 -*-
"""Genera i libri di testo di una classe: i PARZIALI (uno per lezione) e il TOTALE.

Uso (dalla radice del repository):
    python3 strumenti/libri/genera_libri_classe.py 2INF [--nota "testo per il changelog"]

1. Per ogni lezione di lezioni_registro.py scrive
   classe-N/libro-di-testo/lezioni/AAAA-MM-GG_<slug>.md e il PDF ...-vX.Y.pdf accanto.
   Se il testo di una lezione cambia, la versione sale (1.0 -> 1.1) e si aggiunge il changelog.
2. Riempie il libro totale classe-N/libro-di-testo/libro-classeN.md tra i segnaposti
   <!-- LEZIONI:INIZIO --> e <!-- LEZIONI:FINE -->; se il contenuto cambia, la versione sale
   e il PDF esce come libro-classeN-vX.Y.pdf (con indice e segnalibri).
Il PDF passa da HTML (stile del corso, classe-1/_build/genera_pdf.py) con i font per arabo
(Amiri), cinese (WenQuanYi Zen Hei) e bangla (Noto Sans Bengali). Nessun nome di allievo qui.
"""
import argparse, base64, datetime, html, importlib.util, json, mimetypes, os, re, subprocess, sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
REPO = QUI.parent.parent
sys.path.insert(0, str(QUI))
import lezioni_registro as REG  # noqa: E402

_spec = importlib.util.spec_from_file_location("gpdf", REPO / "classe-1/_build/genera_pdf.py")
G = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(G)

OGGI = datetime.date.today().strftime("%d/%m/%Y")
INIZIO, FINE = "<!-- LEZIONI:INIZIO -->", "<!-- LEZIONI:FINE -->"
CSS_IN_PIU = """
:root{--mu:#5b6573}
body{font-family:"DejaVu Serif","Amiri","WenQuanYi Zen Hei","Noto Sans Bengali",serif}
[lang=ar],[dir=rtl]{font-family:"Amiri","DejaVu Serif",serif;direction:rtl;text-align:right;font-size:1.08em}
[lang=zh]{font-family:"WenQuanYi Zen Hei","DejaVu Sans",sans-serif}
[lang=bn]{font-family:"Noto Sans Bengali","DejaVu Sans",sans-serif}
.scheda{border:1px solid #d9d0c2;border-left:4px solid #3a6ea5;border-radius:6px;padding:2.5mm 4mm;margin:2mm 0 4mm;background:#fbfaf7}
.scheda img{max-width:100%;max-height:120mm}
.breve p{margin:1mm 0}
"""


# ---------------------------------------------------------------- fonti -> markdown
def _banche():
    out = Path(os.environ.get("LIBRI_TMP", "/tmp")) / "banche.json"
    subprocess.run(["node", str(QUI / "estrai_banche.js"), str(REPO / "docs/verifica/banche"), str(out)], check=True)
    d = json.loads(out.read_text(encoding="utf-8")); out.unlink()
    return d


BANCHE = None


def _sposta_percorsi(testo, da: Path, a: Path):
    """Riscrive i percorsi relativi delle immagini da cartella 'da' a cartella 'a'."""
    def fix(p):
        if re.match(r"^(https?:|data:|/|#)", p):
            return p
        assoluto = (da / p).resolve()
        return os.path.relpath(assoluto, a) if assoluto.exists() else ""
    testo = re.sub(r'(!\[[^\]]*\]\()([^)\s]+)(\))', lambda m: m.group(1) + fix(m.group(2)) + m.group(3) if fix(m.group(2)) else "", testo)
    testo = re.sub(r'(<img[^>]*?src=")([^"]+)(")', lambda m: m.group(1) + fix(m.group(2)) + m.group(3) if fix(m.group(2)) else "", testo)
    return testo


def _abbassa_titoli(md, livelli=2):
    righe, fence, out = md.split("\n"), False, []
    for r in righe:
        if r.lstrip().startswith("```"):
            fence = not fence
        if not fence and re.match(r"^#{1,6} ", r):
            n = len(r) - len(r.lstrip("#"))
            r = "#" * min(6, n + livelli) + r[n:]
        out.append(r)
    return "\n".join(out)


def _codice_rientrato_a_recinto(md):
    """I blocchi di codice rientrati di 4 spazi diventano blocchi ``` (sicuri anche dopo un elenco)."""
    righe, out, i, fence = md.split("\n"), [], 0, False
    while i < len(righe):
        r = righe[i]
        if r.lstrip().startswith("```"):
            fence = not fence
        if not fence and r.startswith("    ") and r.strip() and (i == 0 or not righe[i - 1].strip()):
            j = i
            while j < len(righe) and (righe[j].startswith("    ") or not righe[j].strip()):
                j += 1
            blocco = righe[i:j]
            while blocco and not blocco[-1].strip():
                blocco.pop()
            if any(re.match(r"\s*(<|[{};]|\w+\s*[:=(])", b) or b.rstrip().endswith((";", "{", "}")) for b in blocco) \
                    and not any(re.match(r"\s*(\d+\.|[-*+]) ", b) for b in blocco):
                out += ["```"] + [b[4:] for b in blocco] + ["```", ""]
                i = i + len(blocco)
                continue
        out.append(r)
        i += 1
    return "\n".join(out)


def _esc_tabella(r):
    """Nelle righe di tabella un tag scritto come esempio (<div>) non deve aprire un blocco HTML."""
    if "|" not in r or "<" not in r:
        return r
    pezzi = r.split("`")
    for i in range(0, len(pezzi), 2):
        pezzi[i] = re.sub(r"<(?!br\s*/?>)", "&lt;", pezzi[i])
    return "`".join(pezzi)


def _pulisci_md(testo):
    """Toglie titolo H1, riga Versione, sottotitolo e changelog; i titoli scendono di 2 livelli."""
    righe = testo.split("\n")
    if righe and righe[0].startswith("---"):  # front matter delle unità 1INF
        try:
            fine = righe[1:].index("---") + 1
            righe = righe[fine + 1:]
        except ValueError:
            pass
    out, testa = [], True
    for r in righe:
        if testa and (r.startswith("# ") or "**Versione" in r or r.strip() in ("---", "") or r.startswith("*") and r.endswith("*")):
            continue
        testa = False
        if re.match(r"^#{1,3} .*(Changelog|CHANGELOG|Registro delle versioni)", r):
            break
        out.append(r)
    md = "\n".join(out).strip()
    md = re.sub(r"<!--[\s\S]*?-->\n?", "", md)
    md = "\n".join(_esc_tabella(r) for r in md.split("\n"))
    md = re.sub(r"\n---\s*$", "", md)
    return _abbassa_titoli(_codice_rientrato_a_recinto(md))


def _rimetti_minore(md):
    """Il segno < scritto nel testo (non un tag): nel codice resta <, nel testo diventa &lt;."""
    out, fence = [], False
    for r in md.split("\n"):
        if r.lstrip().startswith("```"):
            fence = not fence
        if fence:
            out.append(r.replace("\x01", "<"))
            continue
        pezzi = r.split("`")
        for i in range(len(pezzi)):
            pezzi[i] = pezzi[i].replace("\x01", "<" if i % 2 else "&lt;")
        out.append("`".join(pezzi))
    return "\n".join(out)


SCRITTURE = {"ar": "[\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]", "zh": "[\u3400-\u9fff\u3000-\u303f\uff01-\uff60]",
             "bn": "[\u0980-\u09ff]"}
LINGUE = {"1INF": {"ar", "zh"}, "2INF": set(), "3INF": {"bn"}, "4TI": set()}


def filtra_lingue(md, cls):
    """Regola 21: 1INF italiano, arabo, cinese; 2INF e 4TI solo italiano; 3INF italiano e bangla."""
    via = [l for l in SCRITTURE if l not in LINGUE[cls]]
    if not via:
        return md
    for l in via:
        md = re.sub(r'<(span|p|div)[^>]*lang="%s"[^>]*>[\s\S]*?</\1>' % l, "", md)
    rx = re.compile("|".join(SCRITTURE[l] for l in via))
    out = []
    for r in md.split("\n"):
        if rx.search(r):
            r = " · ".join(x for x in r.split(" · ") if not rx.search(x))
            if rx.search(r):
                continue
        out.append(r)
    return "\n".join(out)


def _html_a_md(path: Path):
    from markdownify import markdownify
    t = path.read_text(encoding="utf-8", errors="ignore")
    t = re.sub(r"<(script|style|nav|footer|button|form)[\s\S]*?</\1>", "", t, flags=re.I)
    t = re.sub(r'<img[^>]*src="data:[^"]*"[^>]*>', "", t)
    m = re.search(r"<body[^>]*>([\s\S]*)</body>", t, re.I)
    t = m.group(1) if m else t
    t = t.replace("&lt;", "\x01")
    md = markdownify(t, heading_style="ATX", strip=["a", "span"])
    md = _rimetti_minore(md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return _pulisci_md(md)


def _banca_md(nome, dest: Path):
    global BANCHE
    if BANCHE is None:
        BANCHE = _banche()
    b = BANCHE.get(nome)
    if not b:
        return ""
    parti = []
    for s in b["schede"]:
        tit = re.sub(r"<[^>]+>", "", s.get("titolo", "")).strip()
        testo = s.get("testo", "").replace("\n", " ")
        testo = _sposta_percorsi(testo, REPO / "docs/verifica", dest)
        parti.append(f"#### {tit}\n\n<div class=\"scheda\">{testo}</div>\n")
    return "\n".join(parti)


def contenuto_lezione(lez, cls, dest: Path):
    parti = []
    for tipo, rel in lez.get("fonti", []):
        if tipo == "banca":
            t = _banca_md(rel, dest)
            if t:
                parti.append("### Le schede della lezione\n\n" + t)
        else:
            p = REPO / rel
            if not p.exists():
                continue
            t = _html_a_md(p) if tipo == "html" else _pulisci_md(p.read_text(encoding="utf-8"))
            t = _sposta_percorsi(t, p.parent, dest)
            if t:
                parti.append(t)
    return "\n\n".join(parti)


def _data_it(iso):
    a, m, g = iso.split("-")
    return f"{g}/{m}/{a}"


def corpo_lezione(lez, cls, dest: Path):
    """Il testo della lezione (uguale nel parziale e nel totale)."""
    righe = [f"### Che cosa abbiamo fatto\n\n1. **Quando:** {_data_it(lez['data'])}, {lez.get('ore', '')}.\n2. **Argomenti:** {lez['fatto']}"]
    if lez.get("breve"):
        it, ar, zh = lez["breve"]
        righe.append("### In breve · باختصار · 简要\n\n<div class=\"scheda breve\">"
                     f"<p lang=\"it\">{html.escape(it)}</p><p lang=\"ar\" dir=\"rtl\">{html.escape(ar)}</p>"
                     f"<p lang=\"zh\">{html.escape(zh)}</p></div>")
    c = filtra_lingue(contenuto_lezione(lez, cls, dest), cls)
    if c:
        righe.append("### La teoria e l'esercitazione\n\n" + c)
    else:
        righe.append("### La teoria e l'esercitazione\n\nQuesta lezione è stata di organizzazione e di avvio: non ha una dispensa scritta. "
                     "Gli argomenti sono quelli elencati sopra.")
    return "\n\n".join(righe)


# ---------------------------------------------------------------- versioni
def _leggi_versione(md):
    m = re.search(r"\*\*Versione\s+(\d+)\.(\d+)\*\*", md)
    return (int(m.group(1)), int(m.group(2))) if m else None


def _sale(v):
    return (v[0], v[1] + 1)


# ---------------------------------------------------------------- PDF
def _incorpora_img(body, base: Path):
    def rep(m):
        src = m.group(2)
        if src.startswith("data:"):
            return m.group(0)
        p = (base / src).resolve()
        if not p.exists():
            return ""
        mime = mimetypes.guess_type(str(p))[0] or "image/png"
        return m.group(1) + f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode() + m.group(3)
    return re.sub(r'(<img[^>]*?src=")([^"]+)(")', rep, body)


def md_a_pdf(md_path: Path, titolo: str, sottotitolo: str, segnalibri=False):
    md = md_path.read_text(encoding="utf-8")
    v = _leggi_versione(md)
    ver = f"{v[0]}.{v[1]}"
    pdf = md_path.parent / f"{md_path.stem}-v{ver}.pdf"
    G.DOC_DIR = md_path.parent
    # la freccia → verrebbe tolta dal filtro delle emoji del motore: si usa ⟶ (stesso segno)
    body = _incorpora_img(G.build_body_html(md.replace("→", "⟶")), md_path.parent)
    data = re.search(r"\*\*Versione [^*]+\*\*\s*[—-]\s*([0-9/]+)", md)
    meta = f"Versione {ver}" + (f" · {data.group(1)}" if data else "")
    doc = (f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"/><title>{html.escape(titolo)}</title>'
           f"<style>{G.CSS}{CSS_IN_PIU}</style></head><body>"
           f'<section class="cover"><div class="title">{html.escape(titolo)}</div><div class="rule-cover"></div>'
           f'<div class="subtitle">{html.escape(sottotitolo)}</div><div class="meta">{html.escape(meta)}</div>'
           f'<div class="author">{html.escape(G.COVER_AUTHOR)}</div></section><main>{body}</main></body></html>')
    tmp = Path(os.environ.get("LIBRI_TMP", "/tmp")) / (md_path.stem + ".html")
    tmp.write_text(doc, encoding="utf-8")
    rende_pdf(tmp, pdf, segnalibri)
    if segnalibri:  # libro totale: si archivia anche l'HTML (regola 5)
        md_path.with_suffix(".html").write_text(doc, encoding="utf-8")
    tmp.unlink()
    return pdf


def rende_pdf(html_path: Path, pdf_path: Path, segnalibri=False):
    env = dict(os.environ)
    env.setdefault("NODE_PATH", "/opt/node-tools/node_modules")
    if not env.get("CHROMIUM_PATH"):
        cand = sorted(Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"))
        if cand:
            env["CHROMIUM_PATH"] = str(cand[-1])
    if segnalibri:
        env["PDF_OUTLINE"] = "1"
    subprocess.run(["node", str(QUI / "render_pdf.js"), str(html_path), str(pdf_path)], check=True, env=env,
                   stdout=subprocess.DEVNULL)


# ---------------------------------------------------------------- parziali e totale
def parziale(cls, info, lez):
    cart = REPO / info["cartella"] / "libro-di-testo/lezioni"
    cart.mkdir(parents=True, exist_ok=True)
    md_path = cart / f"{lez['data']}_{lez['slug']}.md"
    corpo = corpo_lezione(lez, cls, cart)
    vecchio = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
    cl_vecchio = ""
    if vecchio:
        v = _leggi_versione(vecchio)
        m = re.search(r"\n---\n\n([\s\S]*)\n\n## Changelog\n", vecchio)
        if m and m.group(1).strip() == corpo.strip():
            pdf = cart / f"{md_path.stem}-v{v[0]}.{v[1]}.pdf"
            if not pdf.exists():
                md_a_pdf(md_path, lez["titolo"], f"{cls} · lezione del {_data_it(lez['data'])}")
            return md_path, f"{v[0]}.{v[1]}", False
        v = _sale(v)
        cl_vecchio = vecchio.split("## Changelog\n", 1)[1].strip() if "## Changelog\n" in vecchio else ""
        cl = f"1. **v{v[0]}.{v[1]} ({OGGI})**: testo aggiornato dalle fonti della lezione.\n" + re.sub(r"^(\d+)\.", lambda m: m.group(0), cl_vecchio)
    else:
        v = (1, 0)
        cl = f"1. **v1.0 ({OGGI})**: prima versione, dalle fonti della lezione."
    ver = f"{v[0]}.{v[1]}"
    testo = (f"# {lez['titolo']}\n\n**Versione {ver}** — {OGGI}\n"
             f"*Libro parziale della {cls}: la lezione del {_data_it(lez['data'])}. Fa parte del libro di testo della classe "
             f"(libro-classe{info['numero']}). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*\n\n"
             f"---\n\n{corpo}\n\n## Changelog\n{cl}\n")
    md_path.write_text(testo, encoding="utf-8")
    md_a_pdf(md_path, lez["titolo"], f"{cls} · lezione del {_data_it(lez['data'])}")
    return md_path, ver, True


def totale(cls, info, nota):
    libro = REPO / info["cartella"] / f"libro-di-testo/libro-classe{info['numero']}.md"
    testo = libro.read_text(encoding="utf-8")
    dest = libro.parent
    blocchi = []
    for i, lez in enumerate(sorted(info["lezioni"], key=lambda x: x["data"]), 1):
        corpo = corpo_lezione(lez, cls, dest)
        corpo = _abbassa_titoli(corpo, 1)
        blocchi.append(f"### L{i:02d} {_data_it(lez['data'])} — {lez['titolo']}\n\n"
                       f"*Libro parziale: lezioni/{lez['data']}_{lez['slug']}.md*\n\n" + corpo)
    nuovo_blocco = INIZIO + "\n" + "\n\n".join(blocchi) + "\n" + FINE
    vecchio_blocco = testo[testo.index(INIZIO): testo.index(FINE) + len(FINE)]
    if vecchio_blocco.strip() == nuovo_blocco.strip():
        v = _leggi_versione(testo)
        return libro, f"{v[0]}.{v[1]}", False
    testo = testo.replace(vecchio_blocco, nuovo_blocco)
    v = _sale(_leggi_versione(testo)) if not nota.startswith("=") else _leggi_versione(testo)
    nota = nota.lstrip("=")
    ver = f"{v[0]}.{v[1]}"
    testo = re.sub(r"\*\*Versione [^*]+\*\*\s*[—-]\s*[0-9/]+", f"**Versione {ver}** — {OGGI}", testo, count=1)
    m = re.search(r"\n## (\d+\.? )?Changelog\n", testo)
    if m:
        dopo = testo[m.end():]
        num = re.match(r"\s*(\d+)\.", dopo)
        n = int(num.group(1)) + 1 if num else 1
        testo = testo[:m.end()] + f"{n}. **v{ver} ({OGGI})**: {nota}\n" + dopo
    libro.write_text(testo, encoding="utf-8")
    return libro, ver, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classe")
    ap.add_argument("--nota", default="aggiornate le lezioni una per una dai libri parziali.")
    ap.add_argument("--solo-parziali", action="store_true")
    a = ap.parse_args()
    info = REG.CLASSI[a.classe]
    rapporto = {"classe": a.classe, "parziali": [], "totale": None}
    for lez in info["lezioni"]:
        p, ver, nuovo = parziale(a.classe, info, lez)
        rapporto["parziali"].append([p.name, ver, nuovo])
    if not a.solo_parziali:
        libro, ver, cambiato = totale(a.classe, info, a.nota)
        pdf = libro.parent / f"{libro.stem}-v{ver}.pdf"
        if cambiato or not pdf.exists():
            md_a_pdf(libro, info["titolo"], "Corso di Informatica — a.s. 2026/27", segnalibri=True)
        rapporto["totale"] = [libro.name, ver, cambiato]
    print(json.dumps(rapporto, ensure_ascii=False))


if __name__ == "__main__":
    main()
