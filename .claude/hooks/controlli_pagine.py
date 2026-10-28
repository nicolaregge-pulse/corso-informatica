#!/usr/bin/env python3
"""Controlli sulle pagine del sito (docs/), nati dal REGISTRO-ERRORI-CLAUDE.md.

Li usano:
1. limite-comandi.py, prima di un «git push» del repository pubblico (controlli SICURI:
   lingue, link alla Regione, nomi in chiaro, sintassi degli script);
2. generatori/audit_regole.py del riservato, nell'attività notturna (tutti i controlli).

Ogni funzione riceve il percorso relativo (es. docs/2inf-oggi/index.html) e il testo e
restituisce una lista di problemi (stringhe corte). Non solleva mai eccezioni verso
chi la chiama: un controllo che si rompe non segnala niente.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import tempfile

RIS = "/home/user/corso-informatica-riservato"
NODE = shutil.which("node") or ("/opt/node22/bin/node" if os.path.exists("/opt/node22/bin/node") else "node")

ARABO = "؀-ۿݐ-ݿ"
CINESE = "　-〿一-鿿＀-￯"
BANGLA = "ঀ-৿"
RX_NON_ITALIANO = re.compile("[%s%s%s]" % (ARABO, CINESE, BANGLA))
RX_ARABO_CINESE = re.compile("[%s%s]" % (ARABO, CINESE))


def classe_di(percorso):
    """1INF, 2INF, 3INF, 4TI dal percorso (una cartella o un file che comincia così)."""
    for parte in re.split(r"[/\\]", percorso.lower()):
        m = re.match(r"([1-4])(inf|ti)(?![a-z])", parte)
        if m:
            return m.group(1) + ("TI" if m.group(2) == "ti" else "INF")
    return None


def pagina_docente(percorso):
    p = percorso.lower()
    return any(x in p for x in ("prof", "docent", "/strumenti/"))


def _riga(testo, pos):
    return testo[:pos].count("\n") + 1


# 1. Lingue della classe (#49, #82, #119; 05/10 n. 8)
RX_PRE = re.compile(r"<(pre|code)\b.*?</\1\s*>", re.I | re.S)


def lingue(percorso, testo):
    """Esempi di codice (<pre>, <code>) esclusi: un elenco di lingue in un programma è lecito."""
    c = classe_di(percorso)
    testo = RX_PRE.sub(lambda m: "\n" * m.group(0).count("\n"), testo)
    if c in ("2INF", "4TI"):
        m = RX_NON_ITALIANO.search(testo)
        if m:
            return ["%s: pagina della %s (solo italiano) con caratteri arabi/cinesi/bengalesi (riga %d) (#49 #82)"
                    % (percorso, c, _riga(testo, m.start()))]
    if c == "3INF":
        m = RX_ARABO_CINESE.search(testo)
        if m:
            return ["%s: pagina della 3INF (italiano + bangla) con caratteri arabi o cinesi (riga %d) (#119)"
                    % (percorso, _riga(testo, m.start()))]
    return []


# 2. Link al sito della Regione nelle pagine dei ragazzi (#136)
RX_REGIONE = re.compile(r"sites\.google\.com/piamarta\.it/formazionesicurezza|formazionesicurezzamilano", re.I)


def regione(percorso, testo):
    if pagina_docente(percorso):
        return []
    m = RX_REGIONE.search(testo)
    if m:
        return ["%s: link al sito della Regione (bottone TEST) nella pagina dei ragazzi (riga %d) (#136)"
                % (percorso, _riga(testo, m.start()))]
    return []


# 3. «Arriva tra poco» in una pagina dei ragazzi (#129)
RX_TRA_POCO = re.compile(r"arriv\w*\s+(?:tra|fra)\s+poco|arriv\w*\s+a\s+breve|in\s+arrivo\s+(?:tra|fra)\s+poco", re.I)


def tra_poco(percorso, testo):
    if pagina_docente(percorso):
        return []
    m = RX_TRA_POCO.search(testo)
    if m:
        return ["%s: «%s» in una pagina dei ragazzi: un passo non può dipendere dai tempi dello script (riga %d) (#129)"
                % (percorso, m.group(0), _riga(testo, m.start()))]
    return []


# 4. Sintassi degli script della pagina (#118; 05/10 n. 9; 06/10 n. 20)
RX_SCRIPT = re.compile(r"<script\b([^>]*)>(.*?)</script\s*>", re.I | re.S)


def _node_check(codice, modulo):
    with tempfile.NamedTemporaryFile("w", suffix=".mjs" if modulo else ".js", delete=False,
                                     encoding="utf-8") as f:
        f.write(codice)
        nome = f.name
    try:
        r = subprocess.run([NODE, "--check", nome], capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            err = [x for x in (r.stderr or "").splitlines() if "Error" in x]
            return err[0][:120] if err else "errore di sintassi"
        return None
    except Exception:
        return None  # node assente o lento: non segnala
    finally:
        try:
            os.unlink(nome)
        except Exception:
            pass


def sintassi(percorso, testo):
    out = []
    if percorso.endswith(".js"):
        e = _node_check(testo, False)
        if e:
            out.append("%s: %s (#118)" % (percorso, e))
        return out
    for m in RX_SCRIPT.finditer(testo):
        attr, codice = m.group(1), m.group(2)
        if re.search(r"\bsrc\s*=", attr, re.I) or not codice.strip():
            continue
        tipo = re.search(r"type\s*=\s*['\"]?([\w/+-]+)", attr, re.I)
        tipo = tipo.group(1).lower() if tipo else "text/javascript"
        if tipo not in ("text/javascript", "module", "application/javascript"):
            continue
        e = _node_check(codice, tipo == "module")
        if e:
            out.append("%s: script alla riga %d non si compila: %s (#118)"
                       % (percorso, _riga(testo, m.start()), e))
    return out


# 5. Nomi degli allievi in chiaro nei file pubblici (#85)
_NOMI = None


def nomi_allievi():
    """Coppie «COGNOME NOME» (prime due parole) dagli elenchi del riservato."""
    global _NOMI
    if _NOMI is not None:
        return _NOMI
    coppie = set()
    for f in glob.glob(os.path.join(RIS, "config", "*presenti*.json")) + \
            glob.glob(os.path.join(RIS, "config", "*elenco*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        voci = d if isinstance(d, list) else d.get("presenti") or d.get("elenco") or []
        for v in voci:
            if isinstance(v, str):
                parole = v.replace("'", " ").split()
                if len(parole) >= 2 and len(parole[0]) >= 3 and len(parole[1]) >= 3:
                    coppie.add((parole[0].lower(), parole[1].lower()))
    _NOMI = coppie
    return coppie


def nomi_in_chiaro(percorso, testo):
    if not percorso.endswith(".json") and not percorso.endswith(".md"):
        return []
    coppie = nomi_allievi()
    if not coppie:
        return []
    basso = testo.lower()
    for a, b in coppie:
        if re.search(r"\b%s\W{1,3}%s\b|\b%s\W{1,3}%s\b" % (re.escape(a), re.escape(b), re.escape(b), re.escape(a)),
                     basso):
            return ["%s: nome di un allievo in chiaro (%s %s…): va cifrato con strumenti/cifra_json.py (#85)"
                    % (percorso, a.upper(), b[:1].upper())]
    return []


# 6. «Copia, apri il Modulo, incolla» in una pagina dei ragazzi (#81, regola 15)
RX_MODULO = re.compile(r"docs\.google\.com/forms|forms\.gle", re.I)
RX_INCOLLA = re.compile(r"\bincoll\w*|ctrl\s*\+\s*v", re.I)


def copia_incolla_modulo(percorso, testo):
    if pagina_docente(percorso) or not percorso.endswith(".html"):
        return []
    if RX_MODULO.search(testo) and RX_INCOLLA.search(testo):
        return ["%s: la pagina ha un Modulo e chiede di incollare: consegna con UN bottone, mai «copia, apri, incolla» (#81)"
                % percorso]
    return []


# 6b. Passo con la foto o il telefono in una pagina dei ragazzi (#44)
RX_FOTO = re.compile(r"fai\s+(?:una|la)\s+foto|fotograf\w*\s+(?:il|la|lo)\s+(?:foglio|quaderno|disegno|lavagna)|"
                     r"con\s+il\s+(?:tuo\s+)?(?:telefono|cellulare)", re.I)


def foto_telefono(percorso, testo):
    if pagina_docente(percorso) or not percorso.endswith(".html"):
        return []
    m = RX_FOTO.search(RX_SCRIPT.sub(" ", testo))
    if m:
        return ["%s: «%s»: in laboratorio ogni passo si fa al computer, niente foto né telefono (#44)"
                % (percorso, m.group(0))]
    return []


# 7. Link relativi a file che non esistono (#84; 02/10 n. 9; 05/10 n. 4)
RX_LINK = re.compile(r"""(?:href|src)\s*=\s*["']([^"'#?]+)""", re.I)


def link_mancanti(percorso, testo, radice):
    if not percorso.endswith(".html"):
        return []
    out = []
    cartella = os.path.dirname(os.path.join(radice, percorso))
    docs = os.path.join(radice, "docs")
    testo = RX_SCRIPT.sub(" ", testo)  # i link costruiti dal codice non si controllano
    for m in RX_LINK.finditer(testo):
        u = m.group(1).strip()
        if not u or re.match(r"^(?:[a-z]+:|//|\$|\{)", u, re.I) or any(c in u for c in "${}+ "):
            continue
        if u.startswith("/corso-informatica/"):
            dest = os.path.join(docs, u[len("/corso-informatica/"):])
        elif u.startswith("/"):
            continue
        else:
            dest = os.path.normpath(os.path.join(cartella, u))
        if not os.path.exists(dest):
            out.append("%s: link a «%s», che non esiste (404) (#84)" % (percorso, u))
            if len(out) >= 3:
                break
    return out


SICURI = (lingue, regione, nomi_in_chiaro, sintassi)
TUTTI = (lingue, regione, tra_poco, nomi_in_chiaro, sintassi, copia_incolla_modulo, foto_telefono)


def controlla(percorso, testo, controlli=SICURI, radice=None):
    out = []
    for c in controlli:
        try:
            out.extend(c(percorso, testo))
        except Exception:
            pass
    if radice and controlli is TUTTI:
        try:
            out.extend(link_mancanti(percorso, testo, radice))
        except Exception:
            pass
    return out


def da_controllare(percorso):
    p = percorso.replace("\\", "/")
    return p.startswith("docs/") and p.endswith((".html", ".js", ".json", ".md")) \
        and "/_legacy/" not in p and not p.endswith(".min.js") and not re.search(r"docs/index\.(?:js|audio)", p)
