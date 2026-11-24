#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Filtro di buon senso v1.2 (25/11/2026: limite 4 righe in modalità assenza; v1.1 23/11/2026, errori #390 e #391, ordine del docente).

Il docente, 23/11/2026: «ne fai troppo di errori. Ogni cosa è un errore. Vorrei che prima di darmi le risposte ci fosse un controllo
da togliere le cose che non hanno senso.» E, subito dopo: «Io perdo il 50% del tempo con te o a gestire domande inutili o a gestire i
tuoi errori.» (il 50% è una STIMA dichiarata dal docente, non una misura).
OBIETTIVO PRINCIPALE: far perdere al docente meno tempo con domande inutili ed errori: messaggi brevi, niente domande ovvie.

Il filtro gira nell'hook controllo-messaggio.py (fine di ogni risposta). Se trova qualcosa BLOCCA: Claude deve riscrivere il messaggio
(una volta: contro i cicli vale stop_hook_active). Ogni blocco dice in una riga PERCHÉ e che cosa TOGLIERE.
Sette controlli:
  1 dato già nei file o del giorno corrente/passato chiesto al docente (orario, presenti, presenze, firme, che giorno è);
  2 modalità assenza (config/modalita-assenza.json del riservato, date lette dal file): niente domande né elenchi di decisioni,
    salvo le criticità vere (firma, PC rotto, decisione solo sua con scadenza oggi);
  3 messaggio lungo (oltre 12 righe, 4 con la modalità assenza attiva o 900 caratteri fuori dai riquadri di codice) che non è un kit/pacchetto;
  4 più di una domanda (R7.6: una domanda sola);
  5 frasi già dette nel messaggio precedente della stessa conversazione (o ripetute nello stesso messaggio);
  6 elenco di conteggi senza fonte e ora (R7.1);
  7 (#391) conferma o permesso chiesti su un lavoro che l'ultimo messaggio del docente ha già ordinato («vuoi che lo faccia?»,
    «procedo?», «te lo preparo?», «dimmi se», «fammi sapere quale scegli»): «se te le dico è perché tu le faccia». Eccezioni: PUBB n,
    firma, decisione solo sua che scade oggi, azioni distruttive o verso l'esterno (R2, push di dati non pubblici). Senza il testo del
    docente il controllo 7 non scatta.
Funzioni pure: esegui(...) non scrive nulla; la memoria dell'ultimo messaggio la tiene chi chiama (controllo-messaggio.py).
Prova: .claude/hooks/prove/prova_filtro_buon_senso.py
"""
import datetime
import json
import os
import re

RIS = "/home/user/corso-informatica-riservato"
MAX_RIGHE = 12
MAX_RIGHE_ASSENZA = 4   # v1.2 (25/11/2026, audit «Utilizzo Claude»): con la modalità assenza attiva il limite è 4 righe
MAX_CARATTERI = 900
MIN_PAROLE_FRASE_RIPETUTA = 6

RE_RECINTO = re.compile(r"^\s*(```|~~~)")
RE_CORNICE = re.compile(r"^\s*(?:[🟩🟦🟥🟨🟧🟪⬛⬜]\s*){3,}$")
RE_CORNICE_KIT = re.compile(r"^\s*(?:[🟦🟥]\s*){3,}$", re.M)
RE_URL = re.compile(r"https?://\S+")
RE_PASSO = re.compile(r"^\s*(?:\d+[.)]|[-*•])\s+")


# ------------------------------------------------------------------ utilità

def fuori_riquadri(testo):
    """Righe di testo fuori dai riquadri di codice (``` o ~~~)."""
    out, dentro, chiusura = [], False, None
    for riga in testo.splitlines():
        m = RE_RECINTO.match(riga)
        if not dentro and m:
            dentro, chiusura = True, m.group(1)
            continue
        if dentro and riga.strip().startswith(chiusura):
            dentro = False
            continue
        if not dentro:
            out.append(riga)
    return out


def _frasi(t):
    return [f.strip() for f in re.split(r"(?<=[.!?:;])\s+|\n+", t) if f.strip()]


def _norm(frase):
    return " ".join(re.findall(r"\w+", frase.lower()))


def e_pacchetto(grezzo):
    """Kit / pacchetto: cornice blu o rossa, oppure TITOLO e OGGETTO con almeno due riquadri (R2.3, R4 3ter)."""
    if RE_CORNICE_KIT.search(grezzo):
        return True
    n_riq = sum(1 for r in grezzo.splitlines() if RE_RECINTO.match(r)) // 2
    return bool(re.search(r"\bTITOLO\b", grezzo) and re.search(r"\bOGGETTO\b", grezzo) and n_riq >= 2)


def _perche(n, perche, togli):
    return "Filtro di buon senso (#390, controllo %d): %s TOGLI: %s" % (n, perche, togli)


# ------------------------------------------------------------------ 1 dato già nei file, del giorno corrente o passato

# Una RICHIESTA al docente: verbo che chiede un dato («dimmi», «mi dai», «puoi dirmi», «ti serve») oppure una domanda che comincia
# con una parola interrogativa («chi», «quali», «che orario»). Una domanda come «vuoi che aggiorni le presenze?» NON è una richiesta di dato.
RE_RICHIESTA_VERBO = re.compile(
    r"\b(?:dimmi|dammi|mandami|passami|indicami|scrivimi|conferma(?:mi)?|mi\s+(?:serve|servono|servirebbe|puoi|potresti|dai|"
    r"dici|passi|mandi|indichi)|puoi\s+(?:dirmi|darmi|mandarmi)|potresti|ti\s+serve)\b", re.I)
RE_INTERROGATIVA = re.compile(r"^\W*(?:chi|quali?|quanti|quante|quando|a\s+che\s+ora|che\s+(?:orario|giorno|ora|data|classe|ore)|"
                              r"(?:hai|ha|avete)\s+(?:già\s+)?firmat\w+|scusa,?\s+che)\b", re.I)


RE_OFFERTA = re.compile(r"^\W*(?:vuoi\s+che|preferisci|posso|devo|ti\s+propongo|facciamo|ti\s+va)\b", re.I)


def finestra_richiesta(frase):
    """Testo su cui cercare il dato chiesto: per una domanda interrogativa tutta la frase; per un verbo di richiesta («mi dai»,
    «dimmi») la parte della frase entro 40 caratteri dal verbo. Una proposta («vuoi che…») non è una richiesta di dato."""
    if RE_OFFERTA.search(frase):
        return ""
    if "?" in frase and RE_INTERROGATIVA.search(frase):
        return frase
    m = RE_RICHIESTA_VERBO.search(frase)
    if m:
        return frase[max(0, m.start() - 40):m.end() + 40]
    return ""


RE_DATA = re.compile(r"\b(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?\b")
RE_PASSATO = re.compile(r"\b(?:oggi|ieri|stamattina|stamani|stamane|ieri\s+sera|stasera|l['’]altro\s+ieri|adesso|ora\s+di\s+oggi)\b", re.I)
DATI_NEI_FILE = [
    ("orario", re.compile(r"\borari[oe]\b|\bcampanell\w+|\bquali\s+ore\b|\bche\s+ore\s+(?:ho|ha|hanno)\b|"
                          r"\bquali\s+classi\b|\bche\s+classe\s+(?:ho|ha)\b", re.I),
     "l'orario sta già in orario/ e in PROSSIME-LEZIONI.md (registro DIDAweb; nel dubbio l'orario della settimana precedente, R10.1.2)"),
    ("presenze", re.compile(r"\bchi\s+(?:è|e|sono)\s+(?:present\w+|assent\w+)\b|\bpresenz[ae]\b|\bquanti\s+(?:present\w+|assent\w+)\b|"
                            r"\b(?:present[ei]|assent[ei])\s+(?:di\s+)?(?:oggi|ieri)\b", re.I),
     "presenti e assenti stanno nei file del giorno (config/<classe>-presenti-<data>.json del riservato) e nel registro"),
    ("firme", re.compile(r"\b(?:hai|ha|avete)\s+(?:già\s+)?firmat\w+|\bore\s+firmat\w+|\bfirmat[ae]\s+(?:le\s+ore|oggi)\b", re.I),
     "le firme stanno in FIRME-REGISTRO-2026-27.md"),
    ("data", re.compile(r"\bche\s+giorno\s+è\b|\bche\s+data\s+è\b|\bche\s+ora\s+è\b|\bche\s+ore\s+sono\b", re.I),
     "la data e l'ora le dà il sistema"),
]


def _data_passata(frase, oggi):
    """True se nella frase c'è una data gg/mm (con o senza anno) uguale o precedente a oggi, o una parola come «oggi»/«ieri»."""
    if RE_PASSATO.search(frase):
        return True
    for m in RE_DATA.finditer(frase):
        g, mese = int(m.group(1)), int(m.group(2))
        anno = int(m.group(3)) if m.group(3) else oggi.year
        if anno < 100:
            anno += 2000
        try:
            if datetime.date(anno, mese, g) <= oggi:
                return True
        except ValueError:
            continue
    return False


def dato_gia_nei_file(t, oggi):
    for f in _frasi(RE_URL.sub(" ", t)):
        w = finestra_richiesta(f)
        if not w:
            continue
        for nome, rx, dove in DATI_NEI_FILE:
            if rx.search(w):
                quando = "e riguarda oggi o un giorno già passato: non si chiede" if _data_passata(f, oggi) else "e non serve chiederlo"
                return [_perche(1, "chiedi al docente un dato (%s) che sta già nei file, %s: %s." % (nome, quando, dove),
                                "la domanda «%s»; leggi il file e scrivi il dato, con la fonte." % f[:90])]
    return []


# ------------------------------------------------------------------ 2 modalità assenza

def carica_assenza(ris=RIS):
    """Config della modalità assenza (date lette dal file, mai dal codice). None se manca o non è leggibile."""
    try:
        with open(os.path.join(ris, "config", "modalita-assenza.json"), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def assenza_attiva(cfg, oggi):
    try:
        if not cfg or not cfg.get("attiva", True):
            return False
        ini = datetime.date.fromisoformat(cfg["inizio"])
        fine = datetime.date.fromisoformat(cfg["fine"])
        return ini <= oggi <= fine
    except Exception:
        return False


def assenza(t, cfg, oggi):
    if not assenza_attiva(cfg, oggi):
        return []
    try:
        crit = [re.compile(r.replace("{OGGI}", oggi.strftime("%d/%m")), re.I) for r in (cfg.get("criticita") or {}).values()]
        dec = re.compile(cfg.get("decisione_o_domanda") or r"\?", re.I | re.M)
    except Exception:
        return []
    pulito = re.sub(r"\bnessun\w*\s+(?:decisione|domanda|scelta)\b", " ", RE_URL.sub(" ", t), flags=re.I)
    m = dec.search(pulito)
    if not m:
        return []
    if any(c.search(t) for c in crit):
        return []
    return [_perche(2, "il docente è assente dal %s al %s (%s): niente domande né elenchi di decisioni, solo le criticità vere "
                    "(firma, PC rotto, decisione solo sua che scade oggi)."
                    % (datetime.date.fromisoformat(cfg["inizio"]).strftime("%d/%m"), datetime.date.fromisoformat(cfg["fine"]).strftime("%d/%m"),
                       cfg.get("motivo", "modalità assenza")[:90]),
                    "la domanda o la decisione «%s»: scegli tu l'opzione più ovvia e dillo in una riga, oppure rimanda a dopo l'assenza."
                    % pulito[max(0, m.start() - 20):m.end() + 40].replace("\n", " ").strip())]


# ------------------------------------------------------------------ 3 lunghezza

def troppo_lungo(grezzo, cfg=None, oggi=None):
    if e_pacchetto(grezzo):
        return []
    righe = [r for r in fuori_riquadri(grezzo) if r.strip() and not RE_CORNICE.match(r)]
    car = sum(len(r.strip()) for r in righe)
    limite = MAX_RIGHE_ASSENZA if (oggi is not None and assenza_attiva(cfg, oggi)) else MAX_RIGHE
    if len(righe) <= limite and car <= MAX_CARATTERI:
        return []
    return [_perche(3, "il messaggio ha %d righe e %d caratteri fuori dai riquadri (limite %d righe e %d caratteri%s) e non è un kit o un "
                    "pacchetto: il docente perde tempo a leggere." % (len(righe), car, limite, MAX_CARATTERI,
                                                                      ", modalità assenza" if limite == MAX_RIGHE_ASSENZA else ""),
                    "tutto tranne la cosa bloccante, il riquadro da copiare e il prossimo passo; il resto va in un file (R4.2).")]


# ------------------------------------------------------------------ 4 più di una domanda

def piu_domande(t):
    dom = [f for f in _frasi(RE_URL.sub(" ", t)) if "?" in f]
    if len(dom) <= 1:
        return []
    return [_perche(4, "ci sono %d domande (R7.6: una domanda sola, con risposte brevi)." % len(dom),
                    "tutte le domande tranne la più importante: «%s»; le altre decidile tu o toglile." % dom[0][:70])]


# ------------------------------------------------------------------ 5 ripetizioni

def ripetizioni(t, precedente):
    """precedente = lista di frasi normalizzate del messaggio già consegnato nella stessa conversazione (o None)."""
    frasi = [f for f in _frasi(t) if not RE_CORNICE.match(f)]
    lunghe = [(f, _norm(f)) for f in frasi if len(_norm(f).split()) >= MIN_PAROLE_FRASE_RIPETUTA]
    visti, doppie = set(), []
    for f, n in lunghe:
        if n in visti:
            doppie.append(f)
        visti.add(n)
    if doppie:
        return [_perche(5, "la stessa frase compare due volte nel messaggio.", "la ripetizione: «%s»." % doppie[0][:80])]
    prec = set(precedente or [])
    ripetute = [f for f, n in lunghe if n in prec]
    if len(ripetute) >= 2 or (len(ripetute) == 1 and len(lunghe) == 1):
        return [_perche(5, "%d frasi sono già nel messaggio di prima: il docente le ha già lette." % len(ripetute),
                        "le frasi già dette (per esempio «%s»): scrivi solo che cosa è cambiato." % ripetute[0][:80])]
    return []


def frasi_per_memoria(t):
    return [_norm(f) for f in _frasi(t) if len(_norm(f).split()) >= MIN_PAROLE_FRASE_RIPETUTA and not RE_CORNICE.match(f)]


# ------------------------------------------------------------------ 6 conteggi senza fonte

RE_FATTO_NUMERICO = re.compile(
    r"(?<![\d/])\d+\s+(?:su|di)\s+\d+\b(?!/)|(?<![\d/])\d+\s+(?:allievi|ragazzi|present[ie]|assent[ie]|consegn\w+|quiz)\b", re.I)
RE_FONTE = re.compile(
    r"\b(?:lett[oaie]|fonte|dato\s+delle|dati\s+delle|non\s+provat\w*|esito|commit|hash|capitolo|documento|nel\s+file|sul\s+foglio|"
    r"registro|export|cruscotto|Classroom|Moduli|Veyon|DIDAweb|ho\s+(?:visto|letto|controllato|verificato|provato)|"
    r"da\s+(?:Classroom|Moduli|Fogli?|cruscotto|registro|DIDAweb)|dal\s+(?:foglio|cruscotto|registro))\b|"
    r"\b(?:alle|delle|ore)\s+\d{1,2}[:.]\d{2}\b|\b\d{1,2}[:.]\d{2}\b", re.I)


def conteggi_senza_fonte(t):
    righe = [r for r in t.splitlines() if RE_PASSO.match(r) and RE_FATTO_NUMERICO.search(r)]
    if len(righe) < 2 or RE_FONTE.search(t):
        return []
    return [_perche(6, "elenchi %d conteggi senza dire da dove vengono né a che ora (R7.1)." % len(righe),
                    "i numeri: oppure scrivi una riga con la fonte e l'ora («letto da … alle HH:MM») o «non provato».")]


# ------------------------------------------------------------------ 7 conferma chiesta su un ordine già dato (#391)

RE_ORDINE_DOCENTE = re.compile(
    r"\b(?:fai|fa'|fammi|dammi|mandami|preparami|prepara|creami|crea|costruisci|costruiscimi|aggiungi|aggiorna|correggi|sistema|"
    r"metti|togli|scrivi|scrivimi|genera|controlla|verifica|usa|rifai|rendi|voglio|vorrei|devi|deve\s+essere|serve|servono|mi\s+serve|"
    r"PRI|PPP|dammelo|dammela|falle|fallo|falla|falli|trasforma|sposta|cambia|riscrivi|continua|avanti|procedi|vai)\b|"
    r"\bse\s+te\s+le?\s+dico\b", re.I)
RE_CONFERMA = re.compile(
    r"\bvuoi\s+che\s+(?:lo|la|li|le|ci|ti|te|mi|procedo|proceda|faccia|prepari|scriva|crei|generi|aggiorni|mandi|invii|costruisca|"
    r"metta|sistemi|corregga|aggiunga|continui|vada)\b|"
    r"\b(?:procedo|proseguo|continuo|vado\s+avanti|lo\s+faccio|la\s+faccio|li\s+faccio|le\s+faccio|lo\s+preparo|la\s+preparo)\s*\?|"
    r"\bposso\s+(?:procedere|proseguire|continuare|iniziare|cominciare|farlo|farla|prepararlo|prepararla)\b|"
    r"\bdevo\s+(?:procedere|proseguire|continuare|farlo|farla|prepararlo|prepararla)\b|"
    r"\bdimmi\s+(?:se\s+(?:devo|posso|vuoi\s+che|procedo|lo\s+faccio|la\s+faccio)|quando\s+(?:posso|devo))\b|"
    r"\bfammi\s+sapere\s+(?:se|quale|quali|come\s+preferisci|cosa\s+(?:scegli|preferisci|vuoi)|quando)\b|"
    r"\b(?:aspetto|attendo)\s+(?:il\s+tuo|la\s+tua)\s+(?:ok|via|conferma|ordine|ok\s+per)\b|"
    r"\bse\s+vuoi\s+(?:lo|la|li|le)\s+(?:faccio|preparo|scrivo|genero|creo)\b", re.I)
# «te lo preparo?» è una richiesta solo se è una domanda; «te lo mando appena…» è una promessa e non si blocca
RE_CONFERMA_DOMANDA = re.compile(r"\b(?:te|ti)\s+(?:lo|la|li|le)\s+(?:preparo|faccio|scrivo|genero|creo|mando|costruisco)\b[^.!]*\?", re.I)
RE_ECCEZIONE_ORDINE = re.compile(
    r"\bPUBB\b|\bfirm\w*|\bpubblic\w*|\bClassroom\b|\bpush\b|\bcancell\w+|\belimin\w+|\bdistrugg\w+|\bripristin\w+|"
    r"\bsovrascri\w+|\bsvuot\w+|\bdati\s+non\s+pubblic\w+|\bcognom\w+|\bpassword\b|\bemail\b|\bmail\b|\binvi\w+\s+(?:a|agli|ai)\b|"
    r"\bscad\w+\s+oggi\b|\bdecisione\s+(?:solo\s+tua|che\s+solo)|\bsolo\s+tu\s+puoi\b|\bnon\s+si\s+(?:può|puo)\s+(?:annullare|rifare)", re.I)


def conferma_su_ordine(t, docente):
    """Il messaggio chiede conferma su un lavoro che l'ultimo messaggio del docente ordina già. Senza il testo del docente: nessun blocco."""
    if not docente or not docente.strip() or not RE_ORDINE_DOCENTE.search(docente):
        return []
    if re.search(r"\baspetta\s+(?:il\s+)?via\b", docente, re.I):
        return []   # R3.4: «aspetta il via» = si risponde solo «Annotato»
    for f in _frasi(RE_URL.sub(" ", t)):
        m = RE_CONFERMA.search(f) or RE_CONFERMA_DOMANDA.search(f)
        if m and not RE_ECCEZIONE_ORDINE.search(f):
            return [_perche(7, "il docente ha già ordinato questo lavoro («se te le dico è perché tu le faccia», #391): chiedere conferma o "
                            "permesso gli fa perdere tempo e ripetere l'ordine.",
                            "la richiesta «%s»: esegui il lavoro e scrivi solo il risultato con la prova (resta solo ciò che richiede una "
                            "decisione sua con scadenza oggi, PUBB n, firma o un'azione distruttiva o verso l'esterno)." % f[:90])]
    return []


# ------------------------------------------------------------------ insieme

def esegui(t, grezzo, oggi=None, ris=RIS, precedente=None, cfg=None, docente=None):
    """t = testo ripulito (senza riquadri, codice in linea e citazioni); grezzo = messaggio intero.
    Restituisce la lista dei motivi (una riga ciascuno). Nessuna eccezione verso chi chiama."""
    oggi = oggi or datetime.date.today()
    cfg = cfg if cfg is not None else carica_assenza(ris)
    out = []
    for f in (lambda: dato_gia_nei_file(t, oggi), lambda: assenza(t, cfg, oggi), lambda: troppo_lungo(grezzo, cfg, oggi),
              lambda: piu_domande(t), lambda: ripetizioni(t, precedente), lambda: conteggi_senza_fonte(t), lambda: conferma_su_ordine(t, docente)):
        try:
            out.extend(f())
        except Exception:
            pass
    return out
