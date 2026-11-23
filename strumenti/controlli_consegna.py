#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlli_consegna.py v1.0 (23/11/2026): i controlli automatici degli errori #386-#389 del 20/11/2026.
Libreria + riga di comando, solo libreria standard, nessun nome di allievo, nessuna scrittura.
Usata da: .claude/hooks/controllo-messaggio.py (blocchi sul messaggio), strumenti/controlla_controlli.py (cruscotto di oggi),
riservato strumenti/controlla_kit.py v1.4 (testi dei post nel kit).

  #386 formato PUBB e kit        -> pacchetto_pubb_mancante(): «PUBB n» / «dati per Classroom» senza il pacchetto rosso e blu.
  #387 testi dei post incoerenti -> problemi_post(): titolo/oggetto con «ieri/domani», «_» iniziale, «????» (arabo/cinese persi),
                                    ora del titolo diversa da quella del kit, data del titolo diversa da quella del kit,
                                    «carte» del foglio senza l'intervallo nell'oggetto, quiz nel kit e non nell'oggetto (o al contrario).
  #388 PDF come formato predefinito -> file_non_pdf_non_richiesto(): SendUserFile di xlsx/docx/csv/md/... senza PDF e senza che il
                                    docente abbia chiesto quel formato.
  #389 cruscotto senza dati di oggi -> cruscotto_senza_dati_di_oggi() e messaggio_dice_cruscotto_pronto().

Uso: python3 strumenti/controlli_consegna.py --cruscotto 1INF [--oggi AAAA-MM-GG]   (stampa DATO DI OGGI / SENZA DATI DI OGGI)
"""
import datetime
import json
import os
import re
import sys

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    from zoneinfo import ZoneInfo
    ROMA = ZoneInfo("Europe/Rome")
except Exception:  # pragma: no cover
    ROMA = None


# ------------------------------------------------------------------ #387 testi dei post

PAROLE_DATA = re.compile(r"\b(ieri|l.altro\s+ieri|domani|dopodomani)\b", re.I)
DATA_IN_TITOLO = re.compile(r"\b(\d{1,2})/(\d{1,2})\b")
ORA_IN_TITOLO = re.compile(r"\bOra\s+(\d{1,2})\b", re.I)
INTERVALLO_CARTE = re.compile(r"\bcart[ae]\s+(?:da(?:l)?\s+)?\d+\s*(?:a|al|-|–)\s*\d+|\bcart[ae]\s+\d+\b", re.I)
NUM_CARTE = re.compile(r"\b(\d+)\s+cart[ae]\b", re.I)
MAX_CARTE_SENZA_INTERVALLO = 8


def problemi_post(titolo, oggetto, ora=None, data_kit=None, testo_sezione="", quiz_in_sezione=None, pdf_testo=""):
    """Lista di frasi (vuota = coerente). titolo e oggetto sono i testi da incollare su Classroom.
    ora = numero dell'ora della sezione del kit; data_kit = (giorno, mese) del kit; testo_sezione = la sezione del kit
    (etichette degli allegati comprese); quiz_in_sezione = True/False/None; pdf_testo = testo del PDF ragazzi se letto."""
    out = []
    titolo = (titolo or "").strip()
    oggetto = (oggetto or "").strip()
    for nome, t in (("titolo", titolo), ("testo del post", oggetto)):
        if t.startswith("_"):
            out.append("%s comincia con «_» (resto di un'incollatura): toglilo" % nome)
        m = PAROLE_DATA.search(t)
        if m:
            out.append("%s dice «%s»: parola di data che il giorno dopo è falsa; scrivi la data o niente" % (nome, m.group(1)))
    if re.search(r"\?{3,}", oggetto) or "�" in oggetto:
        out.append("il testo del post contiene «???» o caratteri rotti: arabo e cinese sono andati persi; "
                   "controlla la codifica prima di consegnare (incolla in una finestra che li mostri)")
    if titolo:
        mo = ORA_IN_TITOLO.search(titolo)
        if ora is not None and not mo:
            out.append("il titolo non dice «Ora %d» (formato «G/M Ora N: argomento breve», R2.4)" % ora)
        elif ora is not None and mo and int(mo.group(1)) != int(ora):
            out.append("il titolo dice «Ora %s» ma il kit è per l'ora %s" % (mo.group(1), ora))
        md = DATA_IN_TITOLO.search(titolo)
        if md and data_kit and (int(md.group(1)), int(md.group(2))) != tuple(int(x) for x in data_kit):
            out.append("la data del titolo (%s/%s) non è quella del kit (%d/%d)"
                       % (md.group(1), md.group(2), data_kit[0], data_kit[1]))
    # carte: il foglio ha tante carte e l'oggetto non dice quali fare
    carte = [int(n) for n in NUM_CARTE.findall(testo_sezione)]
    carte_pdf = len(set(re.findall(r"\bCarta\s+(\d+)\b", pdf_testo)))
    tot = max(carte + [carte_pdf]) if (carte or carte_pdf) else 0
    if tot > MAX_CARTE_SENZA_INTERVALLO and not INTERVALLO_CARTE.search(oggetto):
        out.append("il foglio ha %d carte ma il testo del post non dice quali fare (per esempio «carte da 1 a 8»)" % tot)
    mi = re.search(r"\bcart[ae]\s+(?:da(?:l)?\s+)?(\d+)\s*(?:a|al|-|–)\s*(\d+)", oggetto, re.I)
    if mi and tot and int(mi.group(2)) > tot:
        out.append("il testo dice carte fino alla %s ma il foglio ne ha %d" % (mi.group(2), tot))
    # quiz: nel kit e non nell'oggetto, o l'oggetto lo cita e il kit no
    dice_quiz = bool(re.search(r"\bquiz\b", oggetto, re.I))
    if quiz_in_sezione is True and not dice_quiz:
        out.append("il kit ha il quiz ma il testo del post non lo nomina (per esempio «Poi fai il quiz.»)")
    if quiz_in_sezione is False and dice_quiz and not re.search(r"\bnessun quiz\b", testo_sezione, re.I):
        out.append("il testo del post cita il quiz ma il kit non ne ha uno")
    return out


# ------------------------------------------------------------------ #386 pacchetto PUBB

RE_RICHIESTA_PACCHETTO = re.compile(
    r"\bPUBB\s*[1-6]\b|dati\s+per\s+Classroom|ridammi[^.\n]{0,40}\bkit\b|formato\s+(?:per\s+la\s+)?pubblicazione", re.I)
RE_NO_PACCHETTO_OK = re.compile(r"PUBB\s*[1-6]\s+NON\s+riuscito|^\s*Annotato\b", re.I | re.M)


def richiesta_di_pacchetto(testo_docente):
    return bool(RE_RICHIESTA_PACCHETTO.search(testo_docente or ""))


def pacchetto_pubb_mancante(testo_docente, testi_assistente):
    """Il docente ha chiesto PUBB n (o i «dati per Classroom»): la risposta deve contenere il pacchetto nel formato rosso/blu
    (riga di 🟥, TITOLO e OGGETTO in riquadri) e, se manca il quiz o il link, dirlo. Ritorna None o una frase.
    «PUBB n NON riuscito» ha già il pacchetto sotto (R2.5): vale la stessa regola. Risposte brevi (<60 caratteri) escluse."""
    if not richiesta_di_pacchetto(testo_docente):
        return None
    testi = [t for t in testi_assistente if t and t.strip()]
    if not testi or max(len(t.strip()) for t in testi) < 60:
        return None
    tutto = "\n".join(testi)
    manca = []
    if "🟥🟥🟥" not in tutto:
        manca.append("la cornice rossa 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 (in testa e in fondo)")
    for et in ("TITOLO", "OGGETTO"):
        if not _etichetta_in_riquadro(tutto, et):
            manca.append("%s in un riquadro di codice da copiare" % et)
    if not manca:
        return None
    return ("Il docente ha chiesto «%s» e il pacchetto non è nel formato (#386, GUIDA-MESSAGGI 03sexies/03octies; R2.3, R4 3ter): "
            "manca %s. Rimanda il pacchetto UNA volta, completo e nel formato: riga rossa, TITOLO e OGGETTO in riquadri, riga blu con "
            "«📄 DISPENSA ALLIEVI ORA N ⬇️», il file con SendUserFile, riga blu, riga rossa; il link del quiz nel messaggio "
            "del kit quiz subito dopo, mai a rate."
            % (RE_RICHIESTA_PACCHETTO.search(testo_docente).group(0), "; ".join(manca)))


def _etichetta_in_riquadro(testo, etichetta):
    righe = testo.splitlines()
    dentro = False
    for i, r in enumerate(righe):
        if r.strip().startswith("```"):
            dentro = not dentro
            continue
        if re.search(r"\b%s\b" % etichetta, r):
            if dentro:
                return True
            for s in righe[i + 1:]:
                if s.strip():
                    return s.strip().startswith("```")
    return False


# ------------------------------------------------------------------ #388 PDF come formato predefinito

EST_NON_PDF = (".xlsx", ".xls", ".docx", ".doc", ".csv", ".md", ".txt", ".pptx", ".odt", ".ods", ".html", ".htm")
RE_FORMATO_CHIESTO = re.compile(
    r"excel|xlsx|\bxls\b|\bword\b|docx|\bcsv\b|\.md\b|markdown|html|modificabil|editabil|powerpoint|pptx|\bzip\b|\btxt\b|"
    r"originale|sorgente|foglio\s+di\s+calcolo|google\s+doc|\bmodello\b|\bkit\b|template|importa|da\s+caricare", re.I)


def file_non_pdf_non_richiesto(percorsi, testo_docente, testi_assistente=()):
    """Nel turno sono stati mandati file xlsx/docx/csv/md/... Se il docente non ha detto il formato, il predefinito è il PDF
    (#388: «Io se non specifico, chiedo il PDF»). Esce senza segnalare se: nello stesso turno c'è anche un PDF con lo
    stesso nome, il docente ha nominato un formato (o «modello», «kit»), il messaggio è un kit (righe rosse)."""
    non_pdf = [p for p in percorsi if p.lower().endswith(EST_NON_PDF)]
    if not non_pdf:
        return None
    if RE_FORMATO_CHIESTO.search(testo_docente or ""):
        return None
    if any("🟥🟥" in (t or "") for t in testi_assistente):
        return None
    stems = {os.path.splitext(os.path.basename(p))[0].lower() for p in percorsi if p.lower().endswith(".pdf")}
    manca = [p for p in non_pdf if os.path.splitext(os.path.basename(p))[0].lower() not in stems]
    if not manca:
        return None
    return ("Formato predefinito dei file: PDF (#388, docente 20/11/2026: «Io se non specifico, chiedo il PDF»). Hai mandato «%s» "
            "ma il docente non ha chiesto quel formato. Rimanda lo stesso contenuto in PDF (python3 strumenti/md2pdf.py o "
            "libreoffice --convert-to pdf) con la cornice blu; l'altro formato solo se lo chiede."
            % os.path.basename(manca[0]))


# ------------------------------------------------------------------ #389 cruscotto con i dati di oggi

RE_CRUSCOTTO_PRONTO = re.compile(
    r"cruscott\w*[^.\n]{0,80}?(?:pront\w*|aggiornat\w*|funzion\w*|\blive\b|tempo\s+reale|online|attiv\w*|i\s+dati\s+di\s+oggi)|"
    r"(?:pront\w*|aggiornat\w*|online|attiv\w*)[^.\n]{0,40}?cruscott\w*", re.I)
RE_CRUSCOTTO_AVVISA = re.compile(
    r"dati\s+vecchi|senza\s+i?\s*dati\s+di\s+oggi|non\s+(?:ha|ci\s+sono)\s+(?:ancora\s+)?(?:i\s+)?dati\s+di\s+oggi|"
    r"non\s+in\s+tempo\s+reale|non\s+(?:è|e')\s+(?:ancora\s+)?(?:pront\w*|aggiornat\w*|in\s+tempo\s+reale)|non\s+provato|"
    r"ultimo\s+dato|dato\s+del\s+\d{1,2}/\d{1,2}|dati\s+del\s+\d{1,2}/\d{1,2}|dato\s+delle?\s+\d{1,2}[:.]\d{2}", re.I)
RE_CLASSE = re.compile(r"\b([1-4])\s*(INF|TI)\b", re.I)


def messaggio_dice_cruscotto_pronto(testo):
    """(classi, frase): le classi di cui il messaggio dice che il cruscotto è pronto/aggiornato/live, senza avvisare dei dati
    vecchi. ([], None) se non lo dice o se avvisa."""
    if not testo or RE_CRUSCOTTO_AVVISA.search(testo):
        return [], None
    classi, frase = [], None
    for riga in testo.splitlines():
        m = RE_CRUSCOTTO_PRONTO.search(riga)
        if not m:
            continue
        if re.search(r"\bnon\s+(?:\w+\s+){0,2}$", riga[:m.start() + 20][-40:], re.I):
            continue
        frase = frase or m.group(0)
        for c in RE_CLASSE.finditer(riga) or []:
            k = c.group(1) + c.group(2).upper()
            if k not in classi:
                classi.append(k)
    if frase and not classi:
        for c in RE_CLASSE.finditer(testo):
            k = c.group(1) + c.group(2).upper()
            if k not in classi:
                classi.append(k)
    return (classi, frase) if frase else ([], None)


def _ora_roma(iso):
    try:
        d = datetime.datetime.fromisoformat(str(iso))
    except Exception:
        return None
    if d.tzinfo is None:
        return d
    return d.astimezone(ROMA) if ROMA else d


def ultimo_dato_cruscotto(classe, pub=None):
    """(datetime|None, fonte): il dato più recente del cruscotto di docs/<classe>/ (live.json letto_il, dati-cruscotto.json
    dato.iso). Il «giorno» e il vecchio dati.json non contano: sono la lezione, non l'ora del dato."""
    pub = pub or PUB
    base = os.path.join(pub, "docs", classe.lower())
    cand = []
    try:
        d = json.load(open(os.path.join(base, "live.json"), encoding="utf-8"))
        t = _ora_roma(d.get("letto_il")) if d.get("letto_il") else None
        if t:
            cand.append((t, "live.json letto_il"))
    except Exception:
        pass
    try:
        d = json.load(open(os.path.join(base, "dati-cruscotto.json"), encoding="utf-8"))
        t = _ora_roma((d.get("dato") or {}).get("iso"))
        if t:
            cand.append((t, "dati-cruscotto.json dato.iso"))
    except Exception:
        pass
    if not cand:
        return None, "nessun dato letto in docs/%s/" % classe.lower()
    return max(cand, key=lambda x: x[0])


def cruscotto_senza_dati_di_oggi(classe, oggi, pub=None):
    """None se l'ultimo dato del cruscotto è di oggi (oggi = AAAA-MM-GG, ora di Roma); altrimenti la frase con l'ultimo dato."""
    t, fonte = ultimo_dato_cruscotto(classe, pub)
    if t is None:
        return "%s: %s" % (classe, fonte)
    if t.strftime("%Y-%m-%d") == oggi:
        return None
    return "%s: l'ultimo dato è del %s (%s), non di oggi" % (classe, t.strftime("%d/%m %H:%M"), fonte)


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "--cruscotto":
        oggi = a[3] if len(a) >= 4 and a[2] == "--oggi" else (datetime.datetime.now(ROMA) if ROMA else datetime.datetime.now()).strftime("%Y-%m-%d")
        p = cruscotto_senza_dati_di_oggi(a[1].upper(), oggi)
        print("DATO DI OGGI" if p is None else "SENZA DATI DI OGGI: " + p)
        return 0 if p is None else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
