#!/usr/bin/env python3
"""Controlli sulle pagine del sito (docs/), nati dal REGISTRO-ERRORI-CLAUDE.md.

Li usano:
1. limite-comandi.py, prima di un «git push» del repository pubblico (controlli SICURI:
   lingue, link alla Regione, nomi in chiaro, sintassi degli script);
2. generatori/audit_regole.py del riservato, nell'attività notturna (tutti i controlli).

v1.1 (23/11/2026): controlli nuovi quiz_sul_sito, carta_e_penna, copia_file_da_classroom, senza_a_che_serve, campi_ripetuti,
ruoli_non_richiesti (errori #178 #263 #227 #280 #362 #211); i primi due che non hanno pagine vecchie fuori regola (quiz_sul_sito e
copia_file_da_classroom) sono anche in SICURI, gli altri solo nell'audit notturno (TUTTI).

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


# 6c. «Alza la mano / chiedi al prof» per problemi di contenuto (regole 14 e 30, #171)
RX_ALZA = re.compile(r"alza\s+la\s+mano(?!\s+solo\s+se)|chiedi\s+al\s+prof|chiama\s+il\s+prof|"
                     r"il\s+professore\s+(?:viene|arriva)|arriva\s+il\s+professore", re.I)


def alza_la_mano(percorso, testo):
    if pagina_docente(percorso) or not percorso.endswith((".html", ".js")):
        return []
    m = RX_ALZA.search(testo)
    if m:
        return ["%s: «%s»: le domande vanno all'assistente, il prof solo per PC rotto, salute, comportamento (#171)"
                % (percorso, m.group(0))]
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


def valore_nudo(percorso, testo):
    """#146 (29/10/2026): un voto (o un PC) scritto nella pagina senza controllo del vuoto mostra «null» al docente.
    Segnala «'+r.voto+'» e «'+r.pc+'» concatenati senza e() e senza «==null»."""
    if not percorso.endswith((".html", ".js")):
        return []
    m = re.search(r"'\+r\.(voto|pc)\+'", testo)
    if not m:
        return []
    return ["%s: r.%s scritto nudo nella pagina, se manca compare «null» (riga %d) (#146): usare (r.%s==null?'—':r.%s)"
            % (percorso, m.group(1), _riga(testo, m.start()), m.group(1), m.group(1))]


def pc_a_menu(percorso, testo):
    """#236 (09/11/2026): il numero del PC si chiede con una casella di testo (11-38 in aula 11), non con un menu a tendina.
    Segnala <select id="pc"> e il ciclo che riempie le opzioni fino a 24 (o 20) nelle pagine per i ragazzi."""
    if pagina_docente(percorso) or not percorso.endswith(".js"):  # l html puo avere il select che il percorso.js sostituisce
        return []
    m = re.search(r"<select[^>]*id=[\"']pc[\"']|\$\('pc'\)[^;]*<option|for\s*\(var i = 1; i <= (?:20|24);[^\n]*<option", testo)
    if m:
        return ["%s: numero del PC come menu a tendina (riga %d) (#236): usare un input type=text inputMode=numeric maxLength=2"
                % (percorso, _riga(testo, m.start()))]
    return []


# ---- Controlli rimessi o nuovi del 23/11/2026 (banco di prova degli errori; ordine del docente)
def _html_ragazzi(percorso):
    return percorso.endswith((".html", ".js")) and not pagina_docente(percorso)


def quiz_sul_sito(percorso, testo):
    """#178 #173 (R9.7): i quiz sono sempre su Moduli Google; la copia sul sito è solo ripasso, senza un invio proprio."""
    if not _html_ragazzi(percorso) or RX_MODULO.search(testo) or re.search(r"ripasso", testo, re.I):
        return []
    if re.search(r"quiz", testo, re.I) and (re.search(r"<form\b", testo, re.I) or re.search(r"<button[^>]*>[^<]*invia", testo, re.I)) \
            and re.search(r"fetch\(|XMLHttpRequest|onsubmit|\.submit\(", testo):
        return ["%s: quiz con un invio proprio sul sito, senza il Modulo Google (#178 #173, R9.7): i quiz sono su Moduli; sul sito "
                "solo la copia di ripasso" % percorso]
    return []


RX_CARTA = re.compile(r"\bstamp(?:a|are|ala|alo|ate|ato|ata)\s+(?:la|le|il|i|lo|gli)\s+(?:scheda|schede|foglio|fogli|pagina|pagine|dispensa|esercizio)\b|"
                      r"\bpenna\b|\bfoglio\s+di\s+carta\b|\bcarta\s+e\s+penna\b|\bstampa\s+e\s+(?:scrivi|compila)\b", re.I)


def carta_e_penna(percorso, testo):
    """#263 (R9.9): niente carta e penna; per la 1INF c'è solo la riga «Ricopia sul quaderno»."""
    if not _html_ragazzi(percorso):
        return []
    t = re.sub(r"<(script|style)\b.*?</\1\s*>", " ", testo, flags=re.I | re.S)
    m = RX_CARTA.search(re.sub(r"<[^>]+>", " ", t))
    if m:
        return ["%s: carta e penna («%s») (#263, R9.9): le schede non si stampano e non si scrive a penna; solo browser e Blocco note"
                % (percorso, m.group(0))]
    return []


def copia_file_da_classroom(percorso, testo):
    """#227 (R9.5): un passo che dice di copiare un singolo file da Classroom nella cartella del progetto: serve un bottone o uno zip."""
    if not _html_ragazzi(percorso):
        return []
    t = re.sub(r"<[^>]+>", " ", testo)
    m = re.search(r"\bcopi\w+\b[^\n]{0,100}?\.(?:lfm|pas|pdf|docx|zip)\b[^\n]{0,60}?\bda\s+Classroom\b|"
                  r"\bscaric\w+\b[^\n]{0,70}?\.(?:lfm|pas)\b[^\n]{0,50}?\bClassroom\b", t, re.I)
    if m:
        return ["%s: passo che copia un file da Classroom (#227, R9.5): «%s». Un bottone unico o un solo zip da estrarre"
                % (percorso, re.sub(r"\s+", " ", m.group(0))[:80])]
    return []


def senza_a_che_serve(percorso, testo):
    """#280: ogni pannello ha una riga «A che serve:»."""
    if not _html_ragazzi(percorso):
        return []
    out = []
    for m in re.finditer(r"<(section|div)\b[^>]*\b(?:id|class)=[\"']pannello[\w-]*[\"'][^>]*>", testo, re.I):
        resto = testo[m.end():m.end() + 2500]
        fine = re.search(r"<(?:section|div)\b[^>]*\b(?:id|class)=[\"']pannello", resto, re.I)
        corpo = resto[:fine.start()] if fine else resto
        if not re.search(r"a\s+che\s+serve\s*:", corpo, re.I):
            out.append("%s: pannello o scheda senza «A che serve:» (riga %d) (#280)" % (percorso, _riga(testo, m.start())))
            break
    return out


def campi_ripetuti(percorso, testo):
    """#362: un campo da riempire (etichetta e linea) compare una volta sola; nella 1INF le tre lingue stanno sulla stessa riga,
    mai una casella per lingua. Segnala le linee di riempimento in arabo o cinese e le etichette ripetute."""
    if not _html_ragazzi(percorso):
        return []
    t = re.sub(r"<[^>]+>", "\n", testo)
    campi = re.findall(r"^([^\n:]{2,40}):\s*(?:_{3,}|\.{4,}|…{2,})", t, re.M)
    if not campi:
        return []
    non_it = [c for c in campi if RX_NON_ITALIANO.search(c)]
    ripetuti = sorted({c for c in campi if campi.count(c) > 1})
    if non_it:
        return ["%s: campo da riempire ripetuto nelle tre lingue, una casella per lingua (#362): una casella sola per campo, le "
                "tre lingue sulla stessa riga" % percorso]
    if ripetuti:
        return ["%s: campo da riempire ripetuto (%s) (#362)" % (percorso, ripetuti[0])]
    return []


def ruoli_non_richiesti(percorso, testo):
    """#211: i ruoli «MANI» e «OCCHI» non li ha chiesti il docente."""
    if not _html_ragazzi(percorso):
        return []
    t = re.sub(r"<[^>]+>", " ", testo)
    if re.search(r"\bMANI\b", t) and re.search(r"\bOCCHI\b", t):
        return ["%s: ruoli «MANI» e «OCCHI» non richiesti dal docente (#211)" % percorso]
    return []



SICURI = (lingue, regione, nomi_in_chiaro, sintassi, valore_nudo, alza_la_mano, pc_a_menu, quiz_sul_sito, copia_file_da_classroom)
TUTTI = (lingue, regione, tra_poco, nomi_in_chiaro, sintassi, copia_incolla_modulo, foto_telefono, valore_nudo, alza_la_mano, pc_a_menu,
         quiz_sul_sito, carta_e_penna, copia_file_da_classroom, senza_a_che_serve, campi_ripetuti, ruoli_non_richiesti)


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
