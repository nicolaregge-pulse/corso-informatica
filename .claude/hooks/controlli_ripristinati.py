#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controlli del messaggio RIMESSI il 23/11/2026 (ordine del docente: «se ci sono errori che tu hai tolto dagli avvertimenti
rimettili; se invece li abbiamo risolti va bene così»).

Versione 1.0 (23/11/2026). Sono i controlli che l'hook controllo-messaggio.py aveva fino al 04/11/2026 (lettere (c)...(ii), v. LEGGIMI-controlli.md
capitolo 05.2), riscritti per le regole R1-R11 di oggi: non si riportano le regole abrogate (per esempio «la firma non si deduce dal
bottone FIRMA ✓» è abrogata da R5.1: «FIRMA ✓» in verde = firmata).
Il codice storico non è più nella storia di git (il repository comincia il 18/11/2026): i controlli sono rifatti dalla descrizione nel
LEGGIMI e dai casi del banco di prova (tests/errori/casi/).

Come scattano
  BLOCCO  = regola bloccante di CLAUDE.md (R4 formato, R5 firma, R7 prova prima delle parole): il messaggio va riscritto (una volta).
  AVVISO  = tutto il resto: un messaggio breve (systemMessage), non blocca.
Ogni funzione prende il testo ripulito (senza riquadri, codice in linea e citazioni) e restituisce una lista di (tipo, messaggio) con il
numero dell'errore nel registro. Nessuna funzione solleva eccezioni verso chi la chiama.
Prova: .claude/hooks/prove/prova_controlli_ripristinati.py (casi giusti e sbagliati + falsi allarmi sui messaggi veri del 20/11/2026).
"""
import re

BLOCCO, AVVISO = "blocco", "avviso"

# ------------------------------------------------------------------ R7: affermazioni senza prova

# la prova: una fonte, un'ora, un esito, un «non provato» (basta una nello stesso messaggio)
PROVA = re.compile(
    r"\bho\s+(?:visto|letto|controllat\w*|verificat\w*|provat\w*|compilat\w*|riletto|aperto|eseguit\w*|fatto\s+girare)\b|"
    r"\b(?:risult\w+|PUBBLICAT\w*|PUBLISHED|VERDE|GIALLO|ROSSO|schermata|screenshot|controllat\w*|verificat\w*|lett[oaie]|"
    r"rilett[oaie]|provat\w*|prova|esito|compil\w+|commit|hash|scritto|eseguit\w*|miniatur\w+|repository|clone|"
    r"non\s+provat\w*|visibile|visto)\b|"
    r"\b(?:alle|delle|ore|dopo\s+le)\s+\d{1,2}[:.]\d{2}|\b\d+\s*/\s*\d+\b|\b\d+\s+su\s+\d+\b|\b\d+\s+righe\b", re.I)

AFFERMA = re.compile(
    r"\b(?:a\s+posto|risolt[oaie]|sistemat[oaie]|garantit[oaie]|tutto\s+fatto|funziona(?:no)?|funzionante|"
    r"(?:c['’]è|è\s+presente|si\s+vede|compare|ci\s+sono)\s+sul\s+sito(?:\s+vero)?)\b", re.I)
NEGAZIONE = re.compile(r"\b(?:non|né|ancora\s+da|da|se|quando|finché|affinché|senza|nessun\w*|come|cosa|perché|per|"
                       r"dovrebbe|dovrebbero|deve|devono|basta|quasi|ma|finché)\s+(?:\w+\s+){0,3}$", re.I)


def _frasi(t):
    return [f for f in re.split(r"(?<=[.!?:;])\s+|\n+", t) if f.strip()]


def affermazione_senza_prova(t):
    """R7.1 (ex controllo (c); errori #63 #115 #127 #135 #140 #152 #39 #104 #277): «a posto», «risolto», «funziona», «c'è sul sito»
    detti come un fatto, senza una prova (fonte, ora, esito, «non provato») in tutto il messaggio. BLOCCO."""
    if PROVA.search(t):
        return []
    for f in _frasi(t):
        if "?" in f or len(f) > 220:
            continue
        for m in AFFERMA.finditer(f):
            if NEGAZIONE.search(f[:m.start()]) or re.match(r"\s+(?:senza|come|così|con|su|in|anche|solo|bene|per|se|quando|offline|online)\b", f[m.end():], re.I):
                continue
            return [(BLOCCO, "«%s» senza una prova nello stesso messaggio (R7.1; errori #63 #115 #127 #135 #140 #152): la frase "
                     "«%s» non dice come lo sai. Scrivi la prova (che cosa hai visto o provato, la fonte e l'ora, per esempio "
                     "«compilato alle 10:42: riga compilazione riuscita») oppure «non provato»."
                     % (m.group(0), f.strip()[:110]))]
    return []


RE_CONTEGGIO = re.compile(
    r"\b(?:hanno|ha)\s+(?:già\s+)?consegnat\w+\s+(?:\d+|tutti)\b|"
    r"\b\d+\s+(?:su|di|/)\s*\d+\s+(?:hanno\s+)?(?:consegnat\w+|present\w+|allievi|ragazzi)|"
    r"\bconsegnat[oie]\s+(?:da\s+)?\d+\s+(?:su|di)\s+\d+", re.I)
FONTE_ORA = re.compile(r"(?:lett[oaie]|fonte|dato|dati|da\s+(?:Classroom|Moduli|Fogli?|cruscotto|registro)|dal\s+(?:foglio|cruscotto|registro)|"
                       r"screenshot|aggiornat\w+)[^.\n;]{0,80}\b\d{1,2}[:.]\d{2}|non\s+provat", re.I)


def conteggio_senza_fonte(t):
    """R7.1 (ex (w); errore #151): un conteggio di consegne o presenze porta la fonte e l'ora della lettura. BLOCCO."""
    m = RE_CONTEGGIO.search(t)
    if m and not FONTE_ORA.search(t):
        return [(BLOCCO, "Conteggio senza fonte e ora (R7.1, errore #151): «%s». Rileggi la fonte adesso e scrivi da dove e a che ora "
                 "(per esempio «letto da Classroom alle 13:58»), oppure «non provato»." % m.group(0)[:60])]
    return []


RE_NON_CARICATO = re.compile(
    r"\bnon\s+(?:ha|hanno)\s+(?:ancora\s+)?(?:caricat\w+|pushat\w+|salvat\w+|pubblicat\w+|inviat\w+|mandat\w+)\b|"
    r"\bnon\s+risult\w+\s+(?:caricat\w+|inviat\w+|present\w+|fatt\w+)", re.I)
RE_VEYON_NIENTE = re.compile(r"\bnon\s+(?:ha|sta|stanno|hanno)\s+(?:fatto|facendo)\s+(?:niente|nulla)\b", re.I)
RE_VEYON_FONTE = re.compile(r"\b(?:veyon|miniatur\w+|screenshot|schermata)\b", re.I)
RE_STATO_DA_VEYON = re.compile(
    r"\b(?:dallo|dalla|dalle|dai|dal)\s+(?:screenshot|miniatur\w+|schermat\w+|veyon)[^.\n]{0,80}?"
    r"(?:\bha\s+già|\bè\s+già|già\s+online|\bè\s+online|\bha\s+(?:caricat\w+|consegnat\w+|pubblicat\w+|fatto))", re.I)
RICERCA = re.compile(r"\b(?:clone|ricerca|cercato|commit|non\s+provat\w*|letto|letta)\b|\b(?:alle|delle)\s+\d{1,2}[:.]\d{2}", re.I)


def non_caricato_senza_ricerca(t):
    """R7.1 (ex (r); errori #16 #5 #83 #95): «non ha caricato», «non ha fatto niente» (Veyon) e «ha già ...» da uno screenshot,
    senza la ricerca nel repository o l'ora del dato. BLOCCO."""
    out = []
    m = RE_NON_CARICATO.search(t)
    if m and not RICERCA.search(t):
        out.append((BLOCCO, "«%s» senza la ricerca (R7.1, errore #16): prima di dire che un allievo non ha caricato si cerca nel "
                    "repository e si fa il clone; scrivi dove hai cercato e l'ora, oppure «non provato»." % m.group(0)[:60]))
    m = RE_VEYON_NIENTE.search(t)
    if m and RE_VEYON_FONTE.search(t):
        out.append((BLOCCO, "Dalla miniatura Veyon non si dice «non ha fatto niente» (R7.1, errore #5): scrivi solo che cosa si vede, "
                    "«sulla pagina X alle HH:MM», e «non so altro»."))
    m = RE_STATO_DA_VEYON.search(t)
    if m and not re.search(r"\b(?:repository|repo|commit|clone)\b", t, re.I):
        out.append((BLOCCO, "Lo screenshot non è la prova (R7.1, errori #83 e #5): «%s». La prova è il file nel repository "
                    "dell'allievo: cercalo e scrivi che cosa hai trovato e a che ora, oppure «non provato»." % m.group(0)[:70]))
    return out


def prova_con_dati_finti(t):
    """R7.1 (ex (y); errore #153): una pagina data per funzionante provandola con ?prova=1 o con dati simulati. BLOCCO."""
    if re.search(r"\?prova=1|dati\s+(?:simulat\w+|finti|di\s+prova)|modalità\s+prova", t, re.I) \
            and re.search(r"\b(?:funziona|a\s+posto|ok|verificat\w+)\b", t, re.I) \
            and not re.search(r"dati\s+veri|sito\s+vero|non\s+(?:è\s+)?provat\w+", t, re.I):
        return [(BLOCCO, "Pagina provata solo con ?prova=1 o dati simulati (R7.1, errore #153): non vale. Aprila sul sito vero con i "
                 "dati veri e scrivi l'ora della prova, oppure scrivi «non provato».")]
    return []


# ------------------------------------------------------------------ R4: formato

def rimando_a_riquadri_di_prima(t):
    """R4 (ex (u); errori #31 #266): ogni passo ha il suo riquadro, scritto per intero: niente «il riquadro di prima». BLOCCO."""
    m = re.search(r"\b(?:riquadr\w+|codice|testo|link)\s+(?:di\s+prima|precedente)\b|"
                  r"\b(?:riquadr\w+|codice)[^.\n]{0,25}\b(?:nel|nei|dal|dai)\s+messaggi?\s+(?:di\s+prima|precedent\w+)\b", t, re.I)
    if m:
        return [(BLOCCO, "Rimando a un riquadro di prima: «%s» (R4, errori #31 e #266). Ogni messaggio con passi ha TUTTE le caselle "
                 "da copiare, anche se il testo è già stato dato: riscrivi il passo per intero con il suo riquadro." % m.group(0))]
    return []


RE_ALZA = re.compile(r"alza\s+la\s+mano(?!\s+solo\s+se)|chiedi\s+al\s+prof|chiama\s+il\s+prof|"
                     r"il\s+professore\s+(?:viene|arriva)|arriva\s+il\s+professore", re.I)


def alza_la_mano_nel_kit(grezzo):
    """R8.6 / R9.8 (errori #177 #171): nel testo di un post Classroom (kit con TITOLO e OGGETTO) niente «alza la mano» o «il
    Professore viene da te»: le domande vanno all'assistente. BLOCCO (testo per i ragazzi, R9)."""
    if re.search(r"\bTITOLO\b", grezzo) and re.search(r"\bOGGETTO\b", grezzo):
        m = RE_ALZA.search(grezzo)
        if m:
            return [(BLOCCO, "Nel testo del post per i ragazzi c'è «%s» (errori #177 e #171, R9.8): le domande dei ragazzi vanno "
                     "all'assistente («Scrivi la domanda all'assistente»), il prof solo per PC rotto, salute, comportamento." % m.group(0))]
    return []


# ------------------------------------------------------------------ avvisi

def _av(msg):
    return [(AVVISO, msg)]


def avviso_apps_script(t, grezzo):
    """(ex (v) e (ii); errori #51 e #158): incollare in Apps Script."""
    if not re.search(r"apps\s*script", t, re.I) or not re.search(r"ctrl\s*\+\s*v|\bincolla\b", t, re.I):
        return []
    if re.search(r"automazione-corso\.gs", grezzo, re.I):
        return []
    out = []
    if re.search(r"ctrl\s*\+\s*v", t, re.I) and not re.search(r"^\s*(```|~~~)", grezzo, re.M):
        out += _av("Avviso (non blocca, errore #51): prima di incollare in Apps Script si apre il file automazione-corso.gs dal link "
                   "pubblico (o il codice è in un riquadro in questo messaggio): scrivilo nel passo.")
    if not (re.search(r"ctrl\s*\+\s*a\b", t, re.I) and re.search(r"\bdentro\b|\bclicc\w+|\bclic\b", t, re.I)):
        out += _av("Avviso (non blocca, errore #158): incollare in Apps Script si fa così: clicca dentro il codice, premi Ctrl+A (si "
                   "vede tutto blu), poi Ctrl+V e controlla il numero di righe.")
    return out


def avviso_stile(t):
    """Avvisi di stile (ex (j), (k), (l); errori #53 #56 #55)."""
    out = []
    m = re.search(r"\b(?:onestamente|sinceramente|francamente)\b", t, re.I)
    if m:
        out += _av("Avviso (non blocca, errore #53): «%s» non serve: togli gli avverbi e gli aggettivi che non dicono niente." % m.group(0))
    for r in t.splitlines():
        if not r.lstrip().startswith(("|", "[")) and r.count(" · ") >= 2:
            out += _av("Avviso (non blocca, errore #56, R4.3): catena di coordinate con « · »: ogni passo è una frase che comincia "
                       "con il verbo e dice il «dove» a parole.")
            break
    m = re.search(r"\bsalta\s+(?:al|il|ai)\s+passo|\bse\s+(?:la|lo|è|sei|hai)\s+(?:\w+\s+){0,3}già\s+(?:aperta|aperto|fatto|fatta)\b|"
                  r"\bse\s+non\s+(?:la|lo)\s+vedi\b", t, re.I)
    if m:
        out += _av("Avviso (non blocca, errore #55, R4.3): «%s»: un flusso unico senza «se», senza «salta» e senza domande dentro i "
                   "passi; solo il prossimo passo." % m.group(0))
    return out


def avviso_nessuna_ai(t):
    """(ex (h); errore #90): «nessuna AI» solo dopo aver visto tutte le finestre."""
    if re.search(r"\bnessuna\s+(?:AI|IA|intelligenza\s+artificiale)\b|\bnon\s+(?:c['’]è|ci\s+sono)\s+(?:nessuna\s+)?(?:AI|IA)\b", t, re.I) \
            and not re.search(r"\bfinestr\w+|\bminiatur\w+|\bveyon\b|\bscreenshot\b|\bviste\b|\bvisto\b", t, re.I):
        return _av("Avviso (non blocca, errore #90): «nessuna AI» si scrive solo dopo aver visto tutte le finestre: scrivi da dove "
                   "(miniature Veyon, quante finestre viste, a che ora) oppure «non provato».")
    return []


def avviso_tempi_script(t):
    """(ex (f); errori #88 #130): non si promettono tempi per ciò che fa lo script, senza il piano B."""
    if re.search(r"\b(?:entro|tra|in)\s+(?:pochi|qualche|\d+|un\s+paio\s+di)\s+minut\w+", t, re.I) \
            and re.search(r"\bscript\b|\bponte\b|\bautomatic\w+|\blo\s+pubblica\b|\bli\s+pubblica\b", t, re.I) \
            and not re.search(r"piano\s*B|battito|a\s+mano", t, re.I):
        return _av("Avviso (non blocca, errori #130 e #88): non si promettono tempi per ciò che fa lo script. Scrivi l'ora del "
                   "battito (meno di 3 minuti fa) e il piano B a mano.")
    return []


def avviso_utente_non_indicato(t):
    """(ex (i); errore #100): PC senza nome: si chiede subito chi c'è."""
    if re.search(r"\b(?:utente|nome|allievo)\s+non\s+(?:indicat\w+|noto|presente)\b|\bPC\s+senza\s+nome\b|"
                 r"\bnon\s+so\s+chi\s+(?:è|c['’]è)\s+al\s+PC\b", t, re.I):
        return _av("Avviso (non blocca, errore #100): un PC senza nome non si lascia così: chiedi subito chi c'è (una domanda sola).")
    return []


def avviso_ha_copiato(t):
    """(ex (s); errore 01/10 n.6): anti-plagio sempre al condizionale."""
    if re.search(r"(?:\b[A-ZÀ-Ý]{3,}|\ballievo|\ballieva|\bragazz[oa]|\bstudente)\s+(?:ha|hanno)\s+copiato\b", t) \
            and not re.search(r"da\s+verificare|\bsembra\b|\bpotrebbe|\bprobabil\w+|\bsimil\w+|\bforse\b|\brisulta", t, re.I):
        return _av("Avviso (non blocca, 01/10 n.6): «ha copiato» è un fatto che non si sa: l'anti-plagio si scrive sempre al "
                   "condizionale e con «da verificare» (per esempio «il compito è molto simile: da verificare»).")
    return []


def avviso_rosso_atteso(t):
    """(errore #139): un ROSSO dell'audit non si liquida come atteso."""
    m = re.search(r"\bROSSO\b[^.\n]{0,60}\b(?:atteso|normale|previsto|ignor\w+)\b|\bignor\w+\s+(?:il\s+)?ROSSO\b", t)
    if m:
        return _av("Avviso (non blocca, errore #139): un ROSSO dell'audit non è «atteso» e non si ignora: va in prima riga, con "
                   "la causa e che cosa fai adesso.")
    return []


def avviso_release_cartella(t):
    """(ex (aa); errore #157): una release vale per tutto il repository."""
    if re.search(r"\brelease\s+(?:della|di|per\s+la|solo\s+(?:della|di))\s+(?:cartella|docs|sottocartella)\b", t, re.I):
        return _av("Avviso (non blocca, errore #157): una release vale per tutto il repository, non per una cartella; un progetto "
                   "serio ha un repository suo.")
    return []


def avviso_genere(t):
    """(ex (dd); errore #167): il genere di un allievo non si dà per scontato: si usa il nome (il cognome, R7.4)."""
    if re.search(r"(?:^|[.!?]\s+|\n)\s*(?:Lei|Lui|Egli|Ella)\s+(?:ha|è|sta|non|ancora|deve|può|si|ha\s+già)\b", t):
        return _av("Avviso (non blocca, errore #167): non si dà per scontato il genere di un allievo con «lei» o «lui»: usa il "
                   "COGNOME (R7.4).")
    return []


def avviso_domanda_su_file_del_giorno(t):
    """(ex (z); errore #154): prima di chiedere al docente si guarda nei file del giorno (presenti, presenze, voti)."""
    for f in _frasi(t):
        if "?" in f and re.search(r"\b(?:chi\s+sono|quali\s+sono|mi\s+(?:dai|dici|passi)|dammi)\b[^.?]{0,40}\b(?:presenti|assenti|elenco|presenze|voti)\b",
                                  f, re.I):
            return _av("Avviso (non blocca, errore #154): presenti, presenze e voti stanno già nei file del giorno (diario, "
                       "presenze, registro): guarda lì prima di chiedere al docente.")
    return []


def avviso_didaweb(grezzo):
    """(ex (g); errori #98 #117 #23): la stringa dei voti DIDAweb ha sopra la «Disciplina da scegliere» e voti da 40 a 80."""
    out = []
    righe = []
    dentro = False
    for r in grezzo.splitlines():
        if re.match(r"^\s*(```|~~~)", r):
            dentro = not dentro
            continue
        if dentro:
            righe.append(r)
    stringa = [r for r in righe if re.search(r"\bh\s*[1-6]\s*[|;]", r)]
    if not stringa:
        return out
    if not re.search(r"Disciplina", grezzo, re.I):
        out += _av("Avviso (non blocca, errori #98 e #117): prima della stringa dei voti DIDAweb scrivi la «Disciplina da scegliere» "
                   "(la materia dell'ora, dall'argomento).")
    voti = [int(v) for r in stringa for v in re.findall(r"[A-ZÀ-Ý][A-Za-zÀ-ý' ]*?[;\s]\s*(\d{1,3})(?=\s|;|$)", r)]
    if any(0 < v < 40 for v in voti):
        out += _av("Avviso (non blocca, errore #23, R8.3): nella stringa dei voti c'è un voto sotto 40; il voto minimo è 40 (da 40 a 80).")
    return out


# ------------------------------------------------------------------ con il messaggio del docente

def avviso_con_docente(t, grezzo, docente):
    """Avvisi che dipendono da che cosa ha scritto il docente (ex (t), (n), (cc); errori #21 #190, #113 #3, #166)."""
    out = []
    d = docente or ""
    if re.search(r"\b(?:dammi|fammi|ridammi|mandami|voglio)\b", d, re.I) and not re.search(r"\bPPP\b", d) \
            and re.search(r"\bal\s+tuo\s+avanti\b|\bquando\s+(?:mi\s+)?dici\s+(?:avanti|via)\b|\baspetto\s+(?:il\s+tuo\s+)?(?:avanti|via)\b", t, re.I):
        out += _av("Avviso (non blocca, R3.5, errori #21 e #190): il docente ha scritto «dammi/fammi»: si consegna appena è pronto, "
                   "senza aspettare il suo «avanti» (solo il PPP aspetta).")
    if re.search(r"\b(?:registra|segna|annota|scrivi)\w*\b[^.\n]{0,40}\berror\w+|\berror\w+[^.\n]{0,30}\b(?:registr|segn)\w+", d, re.I) \
            and re.search(r"\b(?:registrat\w+|segnat\w+|annotat\w+)\b|aggiunt\w+\s+al\s+registro", t, re.I) \
            and not re.search(r"#\d{2,3}", grezzo):
        out += _av("Avviso (non blocca, errori #113 e #3): un errore da registrare si scrive subito, e il messaggio dice il numero "
                   "della voce (per esempio «registrato come #391»); tutto ciò che il docente segnala va nel registro e in una regola.")
    domanda = ("?" in d) or re.match(r"\s*(?:cosa|che\s+cosa|cos['’]è|perch[eé]|come\s+mai|a\s+che\s+serve|quale|quanto)\b", d, re.I)
    if domanda and not re.search(r"\b(?:togli|elimina|rimuovi|cancella)\w*\b", d, re.I) \
            and re.search(r"\b(?:ho|l['’]ho|abbiamo)\s+(?:già\s+)?(?:tolt\w+|eliminat\w+|rimoss\w+|cancellat\w+)\b", t, re.I):
        out += _av("Avviso (non blocca, errore #166): una domanda del docente chiede una spiegazione; una cosa si toglie solo se "
                   "il docente scrive «togli» o «elimina».")
    return out


def esegui(t, grezzo, docente=""):
    """Tutti i controlli sul testo. Restituisce [(tipo, messaggio)]."""
    out = []
    for f in (affermazione_senza_prova, conteggio_senza_fonte, non_caricato_senza_ricerca, prova_con_dati_finti,
              rimando_a_riquadri_di_prima, avviso_nessuna_ai, avviso_tempi_script, avviso_utente_non_indicato, avviso_ha_copiato,
              avviso_rosso_atteso, avviso_release_cartella, avviso_genere, avviso_domanda_su_file_del_giorno, avviso_stile):
        try:
            out.extend(f(t))
        except Exception:
            pass
    for f in (lambda: alza_la_mano_nel_kit(grezzo), lambda: avviso_apps_script(t, grezzo), lambda: avviso_didaweb(grezzo),
              lambda: avviso_con_docente(t, grezzo, docente)):
        try:
            out.extend(f())
        except Exception:
            pass
    return out
