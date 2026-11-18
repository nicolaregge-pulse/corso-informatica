# -*- coding: utf-8 -*-
"""Allegato A — Stato del programma (fatto / da fare), per tutte le classi. Fa parte dei registri.

Legge (tutto nel repository pubblico, nessun nome di allievo):
  programmi-ufficiali/2026-27/registro-allegati.json   le voci dell'Allegato A ufficiale (Word del 02/11), blocco «Regge»
  programmi-ufficiali/2026-27/svolto-2026-27.json      voci svolte, confermate dal docente
  programmi-ufficiali/2026-27/copertura-allegato-a.json lezioni firmate/svolte e quali voci coprono
  FIRME-REGISTRO-2026-27.md, ARGOMENTI-SVOLTI-2026-27.md  fonti: ogni lezione della copertura deve esserci scritta
  allegato-a-stato/competenze.json                      titoli delle competenze
Regole (CLAUDE.md R5.2, R7, R11):
  - NON aggiunge mai voci all'Allegato A: le righe sono solo quelle del Word ufficiale.
  - una voce e FATTO solo se (a) e nel svolto-2026-27.json (confermata dal docente), oppure (b) ogni lezione che la copre
    e trovata scritta nelle fonti E e gia finita (data e ora di Roma); nel dubbio resta DA FARE con la nota «da confermare».
  - versione automatica: 1.0 la prima, poi +0.1 a ogni cambio di stato; riga di changelog automatica; stesso dato = stesso file.
Scrive in --out: ALLEGATO-A-STATO-DEL-PROGRAMMA-vX.Y.html e .pdf (A4 verticale, una sezione per classe), stato-allegato-a.json.
Uso (a fine giornata):  python3 strumenti/aggiorna_allegato_a_stato.py [--copia-pdf DIR ...] [--no-pdf] [--ora AAAA-MM-GGTHH:MM]
Per prova su dati finti:  --dati DIR_DATI --out DIR_USCITA   (vedi strumenti/test_aggiorna_allegato_a_stato.py)
"""
import argparse, datetime, hashlib, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
CLASSI = [("1INF", "Classe 1 (1INF)", "I anno"), ("2INF", "Classe 2 (2INF)", "II anno"),
          ("3INF", "Classe 3 (3INF)", "III anno"), ("4TI", "Classe 4 (4TI)", "IV anno")]
NUM = {"1INF": 1, "2INF": 2, "3INF": 3, "4TI": 4}
BREVI = {  # abbreviazione del titolo ufficiale (il titolo intero resta in piccolo sotto)
    "8": "Tecnologie informatiche per la comunicazione e la ricezione di informazioni",
    "12": "Definire e pianificare le fasi delle operazioni",
    "13": "Manutenzione ordinaria di strumenti, utensili, attrezzature",
    "14": "Operare in sicurezza, igiene e salvaguardia ambientale",
    "15": "Installare, configurare e utilizzare supporti hardware e software",
    "16": "Manutenzione ordinaria e straordinaria di sistemi, reti, dispositivi",
    "17": "Elaborazione, manutenzione e trasmissione di dati",
}
BREVI_4TI = {"7": "Reti e strumenti informatici in modo consapevole", "13": "Prodotti di comunicazione e documentazione tecnica",
             "14": "Interventi di installazione, aggiornamento e dismissione", "15": "Politiche di sicurezza dell'informazione",
             "16": "Installare hardware, software o componenti di sottosistema"}
IGNORA = ("provvisorio", "firma", "non firmata", "da verificare", "non provato", "ore ", "crea un file", "pagine web: …")
FONTE_JSON = "confermato dal docente (svolto-2026-27.json)"


def leggi_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def adesso(ora):
    if ora:
        return datetime.datetime.fromisoformat(ora)
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("Europe/Rome")).replace(tzinfo=None, second=0, microsecond=0)
    except Exception:
        return datetime.datetime.now().replace(second=0, microsecond=0)


def fine_lezione(lez):
    """data e ora in cui la lezione e finita (ora «H-K»: finisce alle K:00; senza ora: a fine giornata)"""
    d = datetime.date.fromisoformat(lez["data"])
    m = re.match(r"^\s*(\d+)\s*-\s*(\d+)\s*$", lez.get("ora", ""))
    if m:
        return datetime.datetime.combine(d, datetime.time(int(m.group(2)), 0))
    return datetime.datetime.combine(d, datetime.time(23, 59))


def etichetta(lez):
    g = lez["data"][8:10] + "/" + lez["data"][5:7]
    return f"{g} ore {lez['ora']}" if lez.get("ora") else g


def blocchi_voci(reg, classe):
    """per ogni competenza: lista di (testo, livello) dal blocco «Regge» del Word ufficiale; livello 0 = voce madre, 1 = sotto-voce"""
    out = {}
    for comp, righe in reg[classe]["blocchi"].items():
        voci = []
        for r in righe[1:]:  # la prima riga e l'etichetta «Regge»
            t = r.strip()
            if not t:
                continue
            if r.startswith(" ") or t.startswith("–"):
                voci.append((t.lstrip("–").strip(), 1))
            else:
                voci.append((t, 0))
        out[comp] = voci
    return out


def calcola(dati, adesso_dt):
    reg = leggi_json(os.path.join(dati, "registro-allegati.json"))
    svolto = leggi_json(os.path.join(dati, "svolto-2026-27.json"))
    cop = leggi_json(os.path.join(dati, "copertura-allegato-a.json"))
    comp = leggi_json(os.path.join(dati, "competenze.json"))
    firme = open(os.path.join(dati, "FIRME-REGISTRO-2026-27.md"), encoding="utf-8").read()
    argo = open(os.path.join(dati, "ARGOMENTI-SVOLTI-2026-27.md"), encoding="utf-8").read()
    fonti_txt = {"firme": firme, "argomenti": argo}
    lezioni = {}
    problemi = []
    for lz in cop["lezioni"]:
        cerca = lz.get("cerca") or "«" + lz["titolo"] + "»"
        trovata = cerca in fonti_txt[lz["file"]]
        lz["_verificata"] = trovata
        lz["_finita"] = fine_lezione(lz) <= adesso_dt
        if not trovata:
            problemi.append(f"lezione {lz['id']}: testo non trovato in {lz['file']}: {cerca[:60]}")
        lezioni[lz["id"]] = lz
    conf = {c: set(svolto.get(c, [])) for c, _, _ in CLASSI}
    cop_voci = {}
    for e in cop["copertura"]:
        cop_voci.setdefault((e["classe"], e["voce"]), []).append(e)
    risultato = {}
    visti = set()
    for classe, _, _ in CLASSI:
        if classe not in reg:
            continue
        righe_classe = []
        for c, voci in blocchi_voci(reg, classe).items():
            lista = []
            for testo, liv in voci:
                if liv == 0:
                    lista.append({"testo": testo, "liv": 0})
                    continue
                visti.add((classe, testo))
                stato, fonte, nota = "DA FARE", "", ""
                entries = cop_voci.get((classe, testo), [])
                date = []
                for e in entries:
                    for lid in e.get("lezioni", []):
                        lz = lezioni.get(lid)
                        if lz is None:
                            problemi.append(f"{classe} «{testo[:40]}»: lezione {lid} inesistente")
                            continue
                        date.append(lz)
                if testo in conf[classe]:
                    stato = "FATTO"
                    fonte = "; ".join(sorted({etichetta(l) + " · " + l["fonte"] for l in date})) or FONTE_JSON
                    if date:
                        fonte += " · confermato dal docente"
                else:
                    fatti = [e for e in entries if e["stato"] == "fatto"]
                    note = [e for e in entries if e["stato"] == "nota"]
                    if fatti:
                        lz_all = [lezioni[l] for e in fatti for l in e["lezioni"] if l in lezioni]
                        if lz_all and all(l["_verificata"] for l in lz_all):
                            if all(l["_finita"] for l in lz_all):
                                stato = "FATTO"
                                fonte = "; ".join(etichetta(l) + " · " + l["fonte"] for l in lz_all)
                            else:
                                nota = "firmata " + ", ".join(etichetta(l) for l in lz_all if not l["_finita"]) + ": da confermare a fine ora"
                        else:
                            nota = "fonte non trovata: da confermare"
                    if stato != "FATTO" and note:
                        nota = (nota + "; " if nota else "") + "; ".join(e["nota"] for e in note)
                lista.append({"testo": testo, "liv": 1, "stato": stato, "fonte": fonte, "nota": nota})
            righe_classe.append({"comp": c, "titolo": comp[classe].get(c, ""), "voci": lista})
        risultato[classe] = righe_classe
    for classe in conf:
        for v in conf[classe]:
            if (classe, v) not in visti and classe in reg:
                problemi.append(f"{classe}: voce del svolto-2026-27.json non presente nel Word ufficiale: «{v}»")
    # titoli firmati non ancora in copertura (da mappare)
    mappati = {l["titolo"].strip().lower() for l in cop["lezioni"] if l.get("titolo")}
    titoli = [t.strip() for t in re.findall(r"«([^«»\n]{8,140})»", firme)]
    non_mappati = sorted({t for t in titoli if t.lower() not in mappati and not t.lower().startswith(IGNORA)})
    return risultato, problemi, non_mappati


def riepilogo(ris):
    """voci per classe, ciascuna contata una volta anche se compare in piu competenze"""
    out = {}
    for classe, comps in ris.items():
        stati = {}
        for c in comps:
            for v in c["voci"]:
                if v["liv"] == 1:
                    stati[v["testo"]] = v["stato"]
        f = sum(1 for x in stati.values() if x == "FATTO")
        out[classe] = (f, len(stati) - f)
    return out


def impronta(ris):
    s = json.dumps(ris, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def cambi(vecchio, nuovo):
    """righe di changelog: voci passate a FATTO (o tornate DA FARE) e conteggi"""
    righe = []
    def mappa(r):
        m = {}
        for classe, comps in r.items():
            for c in comps:
                for v in c["voci"]:
                    if v["liv"] == 1:
                        m[(classe, v["testo"])] = dict(v, comp=c.get("comp", ""))
        return m
    a, b = mappa(vecchio), mappa(nuovo)
    for k, v in b.items():
        s0 = a.get(k, {}).get("stato", "DA FARE")
        if v["stato"] != s0:
            righe.append(f"{k[0]}: «{k[1][:70]}» da {s0} a {v['stato']}")
        c0 = a.get(k, {}).get("comp")
        if c0 and c0 != v["comp"]:  # spostamento di una voce da una competenza all'altra (v1.1, 18/11/2026)
            righe.append(f"{k[0]}: «{k[1][:70]}» spostata dalla Comp. {c0} alla Comp. {v['comp']} (stesso stato)")
    if not righe:
        righe.append("cambiate note o fonti, nessuna voce ha cambiato stato")
    return righe


def esc(x):
    return html.escape(x, quote=False)


CSS = r"""
 @page { size: A4; }
 *{box-sizing:border-box;}
 body{font-family:"Liberation Sans",Arial,sans-serif;color:#161616;margin:0;font-size:8.6pt;line-height:1.26;}
 h1{font-size:15pt;text-align:center;margin:0 0 2px;}
 .subt{text-align:center;font-size:8.8pt;color:#3a6ea5;margin:0 0 8px;}
 h2{font-size:12pt;color:#16324a;border-bottom:1.5px solid #3a6ea5;padding:2px 0;margin:12px 0 4px;}
 h3{font-size:9.6pt;color:#16324a;margin:9px 0 1px;break-after:avoid;}
 .tit{font-size:6.8pt;color:#6b6b6b;margin:0 0 3px;break-after:avoid;}
 .legend{font-size:8.4pt;margin:0 0 7px;}
 .chip{display:inline-block;padding:1px 9px;border-radius:11px;margin-right:6px;font-weight:bold;}
 .chip.f{background:#e7f5e9;color:#1e5a22;border:1px solid #2e7d33;}
 .chip.d{background:#fbf3c9;color:#7a5c00;border:1px solid #d9b400;}
 table{border-collapse:collapse;width:100%;margin:1px 0 4px;}
 td{border:1px solid #cbc4b6;padding:2px 7px;vertical-align:top;}
 tr{break-inside:avoid;}
 td.st{width:62px;text-align:center;font-weight:bold;font-size:7.4pt;white-space:nowrap;}
 tr.f td{background:#eef8f0;} tr.f td.st{background:#d6efd9;color:#1e5a22;}
 tr.d td{background:#fdf8e3;} tr.d td.st{background:#fbf0b8;color:#7a5c00;}
 tr.g td{background:#eef2f7;font-weight:bold;color:#16324a;font-size:8.3pt;}
 .src{display:block;font-size:6.6pt;color:#4d6b4f;font-weight:normal;}
 .nota{display:block;font-size:6.8pt;color:#7a5c00;font-weight:normal;}
 .box{border-left:4px solid #3a6ea5;background:#eaf1f8;padding:6px 10px;border-radius:4px;margin:6px 0;font-size:8.2pt;color:#274b73;}
 .cl{break-before:page;} .cl.primo{break-before:auto;}
 ol{margin:3px 0 0 16px;padding:0;font-size:8pt;}
"""


def html_classe(classe, label, anno, comps, ver, quando, nota_box=True):
    p = [f'<div class="cl primo"><h1>Allegato A — Stato del programma (fatto / da fare)</h1>',
         f'<div class="subt">a.f. 2026/2027 · prof. Nicola Regge · Versione {ver} · aggiornato il {quando}</div>',
         '<div class="legend"><span class="chip f">FATTO</span> parte già svolta &nbsp; <span class="chip d">DA FARE</span> parte non ancora svolta (in giallo)</div>']
    if nota_box:
        p.append('<div class="box"><b>Programma dichiarato ampio:</b> le voci sono quelle dell\'Allegato A ufficiale (Word del 02/11/2026, '
                 'parte «Regge»); ciò che non riusciamo a svolgere resta semplicemente in giallo (<b>da fare</b>). Una voce passa a '
                 '<b>fatto</b> solo se un argomento firmato sul registro, o confermato dal docente, la copre; sotto ogni voce svolta '
                 'sono scritte la data della lezione registrata (può non essere la prima) e la fonte. Dopo il 30/10 sull\'Allegato A si può solo togliere, mai aggiungere.</div>')
    p.append(f'<h2>{esc(label)} — {esc(anno)} — a.f. 2026/2027</h2>')
    for c in comps:
        brevi = BREVI_4TI if classe == "4TI" else BREVI
        p.append(f'<h3>Competenza {esc(c["comp"])} — {esc(brevi.get(c["comp"], c["titolo"][:90]))}</h3>')
        p.append(f'<div class="tit">{esc(c["titolo"])}</div><table>')
        for v in c["voci"]:
            if v["liv"] == 0:
                p.append(f'<tr class="g"><td class="st"></td><td>{esc(v["testo"])}</td></tr>')
                continue
            cls = "f" if v["stato"] == "FATTO" else "d"
            extra = ""
            if v["fonte"]:
                extra += f'<span class="src">{esc(v["fonte"])}</span>'
            if v["nota"]:
                extra += f'<span class="nota">{esc(v["nota"])}</span>'
            p.append(f'<tr class="{cls}"><td class="st">{v["stato"]}</td><td>{esc(v["testo"])}{extra}</td></tr>')
        p.append('</table>')
    p.append('</div>')
    return "\n".join(p)


def html_registro(stato):
    righe = "".join(f'<li><b>v{esc(c["versione"])}</b> ({esc(c["quando"])}): {esc("; ".join(c["righe"][:12]))}</li>' for c in reversed(stato["changelog"][-8:]))
    return f'<div class="cl primo"><h2>Registro delle versioni</h2><ol reversed>{righe}</ol></div>'


def pagina(corpo):
    return f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{corpo}</body></html>'


def pdf_unico(ris, stato, out_pdf):
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter
    import tempfile
    ver, quando = stato["versione"], stato["aggiornato_txt"]
    w = PdfWriter()
    sezioni = [(f"Classe {NUM[c]}", html_classe(c, l, a, ris[c], ver, quando)) for c, l, a in CLASSI if c in ris]
    sezioni.append(("Registro delle versioni", html_registro(stato)))
    with sync_playwright() as pw, tempfile.TemporaryDirectory() as tmp:
        br = pw.chromium.launch(executable_path=CHROME)
        for i, (nome, corpo) in enumerate(sezioni):
            pg = br.new_page()
            pg.set_content(pagina(corpo))
            hdr = (f'<div style="font-size:7px;width:100%;padding:0 12mm;color:#777;text-align:right;font-family:Arial">'
                   f'Allegato A — Stato del programma · v{ver} · {quando}</div>')
            ftr = (f'<div style="font-size:8px;width:100%;padding:0 12mm;color:#444;font-family:Arial;display:flex;justify-content:space-between">'
                   f'<span>Corso di Informatica — {nome}</span><span>Pag. <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
            f = os.path.join(tmp, f"s{i}.pdf")
            pg.pdf(path=f, format="A4", print_background=True, display_header_footer=True, header_template=hdr, footer_template=ftr,
                   margin={"top": "14mm", "bottom": "14mm", "left": "11mm", "right": "11mm"})
            pg.close()
            for pagina_pdf in PdfReader(f).pages:
                w.add_page(pagina_pdf)
        br.close()
    w.add_metadata({"/Title": f"Allegato A — Stato del programma v{ver}", "/Author": "Corso di Informatica"})
    with open(out_pdf, "wb") as fh:
        w.write(fh)
    return len(w.pages)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dati", help="cartella con i file dati (default: i file del repository)")
    ap.add_argument("--out", help="cartella di uscita (default: allegato-a-stato/)")
    ap.add_argument("--ora", help="AAAA-MM-GGTHH:MM (per prove); default: adesso, ora di Roma")
    ap.add_argument("--copia-pdf", action="append", default=[], help="copia anche il PDF in questa cartella (ripetibile)")
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    out = a.out or os.path.join(ROOT, "allegato-a-stato")
    os.makedirs(out, exist_ok=True)
    dati = a.dati
    if not dati:  # i file del repository, riuniti in una cartella virtuale: usiamo percorsi diretti
        import tempfile
        dati = tempfile.mkdtemp()
        for src, dst in [("programmi-ufficiali/2026-27/registro-allegati.json", "registro-allegati.json"),
                         ("programmi-ufficiali/2026-27/svolto-2026-27.json", "svolto-2026-27.json"),
                         ("programmi-ufficiali/2026-27/copertura-allegato-a.json", "copertura-allegato-a.json"),
                         ("allegato-a-stato/competenze.json", "competenze.json"),
                         ("FIRME-REGISTRO-2026-27.md", "FIRME-REGISTRO-2026-27.md"),
                         ("ARGOMENTI-SVOLTI-2026-27.md", "ARGOMENTI-SVOLTI-2026-27.md")]:
            shutil.copy(os.path.join(ROOT, src), os.path.join(dati, dst))
    now = adesso(a.ora)
    ris, problemi, non_mappati = calcola(dati, now)
    h = impronta(ris)
    p_stato = os.path.join(out, "stato-allegato-a.json")
    if os.path.exists(p_stato):
        stato = leggi_json(p_stato)
    else:
        stato = {"versione": None, "impronta": "", "changelog": [], "voci": {}}
    nuova = stato["impronta"] != h
    if nuova:
        rs = riepilogo(ris)
        if stato["versione"] is None:
            ver = "1.0"
            righe = ["prima versione sull'Allegato A ufficiale del 02/11/2026 (parte «Regge»), tutte le classi; FATTO per classe: " +
                     ", ".join(f"{c} {f}" for c, (f, d) in rs.items())]
        else:
            M, m = stato["versione"].split(".")
            ver = f"{M}.{int(m) + 1}"
            righe = cambi(stato["voci"], ris)
        quando = now.strftime("%d/%m/%Y ore %H:%M")
        stato.update({"versione": ver, "impronta": h, "aggiornato": now.isoformat(timespec="minutes"), "aggiornato_txt": quando, "voci": ris,
                      "riepilogo": {c: {"fatto": f, "da_fare": d} for c, (f, d) in rs.items()}})
        stato["changelog"].append({"versione": ver, "quando": quando, "righe": righe})
    ver = stato["versione"]
    base = f"ALLEGATO-A-STATO-DEL-PROGRAMMA-v{ver}"
    p_html, p_pdf = os.path.join(out, base + ".html"), os.path.join(out, base + ".pdf")
    corpo = "".join(html_classe(c, l, an, ris[c], ver, stato["aggiornato_txt"]).replace('class="cl primo"', 'class="cl' + (' primo"' if i == 0 else '"'), 1)
                    for i, (c, l, an) in enumerate([x for x in CLASSI if x[0] in ris])) + html_registro(stato).replace('class="cl primo"', 'class="cl"')
    with open(p_html, "w", encoding="utf-8") as fh:
        fh.write(pagina(corpo))
    if nuova or not os.path.exists(p_stato):
        with open(p_stato, "w", encoding="utf-8") as fh:
            json.dump(stato, fh, ensure_ascii=False, indent=1, sort_keys=True)
            fh.write("\n")
    npag = None
    if not a.no_pdf and (nuova or not os.path.exists(p_pdf)):
        npag = pdf_unico(ris, stato, p_pdf)
    if not a.no_pdf:
        for d in a.copia_pdf:
            os.makedirs(d, exist_ok=True)
            shutil.copy(p_pdf, os.path.join(d, base + ".pdf"))
    rs = riepilogo(ris)
    print(f"Allegato A stato: versione {ver} ({'NUOVA' if nuova else 'invariata'}), dato del {now.strftime('%d/%m/%Y %H:%M')} (ora di Roma)")
    for c, (f, d) in rs.items():
        print(f"  {c}: FATTO {f}, DA FARE {d}")
    print(f"  file: {p_html}" + (f"\n        {p_pdf}" + (f" ({npag} pagine)" if npag else "") if not a.no_pdf else ""))
    for pr in problemi:
        print("  PROBLEMA:", pr)
    if non_mappati:
        print(f"  Titoli firmati in FIRME-REGISTRO non ancora in copertura-allegato-a.json ({len(non_mappati)}), da mappare o da lasciare senza voce (R5.2):")
        for t in non_mappati:
            print("   -", t)
    return 1 if problemi else 0


if __name__ == "__main__":
    sys.exit(main())
