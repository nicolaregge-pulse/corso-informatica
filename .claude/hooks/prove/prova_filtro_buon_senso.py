#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove del filtro di buon senso v1.1 (23/11/2026, errori #390 e #391): filtro_buon_senso.py dentro controllo-messaggio.py.

1. Casi sbagliati (devono scattare, con il numero del controllo giusto) e giusti (non devono scattare), anche con i testi veri dei
   messaggi del 23/11/2026 riscritti in modo anonimo.
2. Prova di insieme: l'hook intero (main) con trascrizione finta, cartella riservata finta e memoria dell'ultimo messaggio.
3. FALSI ALLARMI: i messaggi veri di Claude del 20/11/2026 (bobina del riservato) e i kit del 20/11/2026: si contano i blocchi per
   controllo; i messaggi BREVI normali (entro 12 righe e 900 caratteri, una domanda al massimo) devono dare 0 blocchi. Se il riservato non c'è la
   parte 3 si salta e lo dice («non provato»).
Uso: python3 -I /home/user/corso-informatica/.claude/hooks/prove/prova_filtro_buon_senso.py   (ultima riga «N/N»)
"""
import contextlib
import datetime
import glob
import importlib.util
import io
import json
import os
import re
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.dirname(QUI)
RIS = "/home/user/corso-informatica-riservato"
OGGI = datetime.date(2026, 11, 23)


def carica(nome):
    spec = importlib.util.spec_from_file_location("m_" + re.sub(r"\W", "_", nome), os.path.join(HOOKS, nome))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


fb = carica("filtro_buon_senso.py")
cm = carica("controllo-messaggio.py")
CFG = json.load(open(RIS + "/config/modalita-assenza.json", encoding="utf-8")) if os.path.exists(RIS + "/config/modalita-assenza.json") else None
ok = tot = 0


def verifica(nome, condizione):
    global ok, tot
    tot += 1
    if condizione:
        ok += 1
    else:
        print("FALLITO:", nome)


def pulito(testo):
    return cm.senza_citazioni(cm.senza_codice_in_linea(cm.senza_riquadri(testo)))


def numeri(testo, oggi=OGGI, cfg=None, precedente=None, docente=None):
    """Numeri dei controlli che scattano (dal testo «controllo N» di ogni motivo)."""
    motivi = fb.esegui(pulito(testo), testo, oggi=oggi, ris="/non-esiste", precedente=precedente, cfg=cfg if cfg is not None else {}, docente=docente)
    return sorted({int(re.search(r"controllo (\d)", m).group(1)) for m in motivi}), motivi


def scatta(nome, testo, n, **kw):
    ns, motivi = numeri(testo, **kw)
    verifica("scatta %d: %s (ottenuto %s)" % (n, nome, ns), n in ns)
    for m in motivi:   # ogni blocco dice PERCHÉ e che cosa TOGLIERE, in una riga
        verifica("una riga con perché e TOGLI: " + nome, "\n" not in m and "TOGLI:" in m and len(m) > 60)


def tace(nome, testo, **kw):
    ns, motivi = numeri(testo, **kw)
    verifica("NON scatta: %s (ottenuto %s %s)" % (nome, ns, [m[:70] for m in motivi]), not ns)


# ------------------------------------------------------------------ 1 dato già nei file / del giorno
scatta("orario di oggi chiesto (testo del 23/11 anonimo)",
       "Mi dai l'orario di lunedì 23/11? Mi serve per preparare le ore di oggi.", 1)
scatta("orario di ieri", "Che orario aveva ieri la 2INF?", 1)
scatta("orario futuro: sta nei file", "Puoi dirmi l'orario di giovedì 26/11?", 1)
scatta("presenti di oggi", "Chi sono i presenti di oggi?", 1)
scatta("firme", "Hai già firmato le ore di oggi?", 1)
scatta("che giorno è", "Scusa, che giorno è oggi?", 1)
tace("orario detto, non chiesto", "L'orario di lunedì 23/11 l'ho letto da orario/: ore 3 e 4 in 2INF.")
tace("domanda su una cosa che solo lui sa", "Vuoi la versione con le immagini o senza?")
tace("orario dentro un riquadro da copiare", "Incolla questo:\n```\nMi dai l'orario di lunedì?\n```")
tace("orario citato", "Nel file c'è scritto «che orario ha la 2INF?» ma è solo il titolo.")

# ------------------------------------------------------------------ 2 modalità assenza
scatta("elenco di decisioni in assenza (anonimo, del 23/11)",
       "Ci sono tre decisioni da prendere:\n1. Quale quiz usare per la 2INF\n2. Se spostare la verifica\nA) sì\nB) no", 2, cfg=CFG)
scatta("domanda in assenza", "Preferisci la prova di giovedì o di venerdì", 2, cfg=CFG)
scatta("ti propongo in assenza", "Ti propongo di rimandare la verifica alla settimana dopo.", 2, cfg=CFG)
tace("firma in assenza è criticità", "Firma: le ore 5 e 6 non risultano firmate, scadenza 14:05.", cfg=CFG)
tace("PC rotto in assenza", "Il PC 14 è rotto: serve il tuo intervento.", cfg=CFG)
tace("decisione con scadenza oggi", "Decisione solo tua: il preventivo scade oggi 23/11, confermi?", cfg=CFG)
tace("messaggio di sola presa d'atto", "Annotato. Niente da fare per te fino al 26/11.", cfg=CFG)
tace("nessuna decisione", "Nessuna decisione da prendere, tutto in coda.", cfg=CFG)
tace("fuori dal periodo", "Preferisci la prova di giovedì o di venerdì", cfg=CFG, oggi=datetime.date(2026, 11, 26))
tace("file di stato assente: nessun blocco", "Preferisci la prova di giovedì?", cfg=None)
cfg_off = dict(CFG or {}, attiva=False)
tace("modalità spenta", "Preferisci la prova di giovedì", cfg=cfg_off)
verifica("le date del file sono 23/11-25/11", bool(CFG) and CFG["inizio"] == "2026-11-23" and CFG["fine"] == "2026-11-25")
verifica("le date non sono nel codice del filtro", not re.search(r"2026-11-2[0-9]", open(os.path.join(HOOKS, "filtro_buon_senso.py"), encoding="utf-8").read().split('"""', 2)[2]))

# ------------------------------------------------------------------ 3 lunghezza
lungo = "\n".join("Riga numero %d con una frase di esempio per riempire il messaggio." % i for i in range(1, 16))
scatta("15 righe", lungo, 3)
scatta("oltre 900 caratteri in poche righe", ("Una frase lunga che continua ancora e ancora senza fine. " * 20).strip(), 3)
tace("12 righe esatte", "\n".join("Riga %d." % i for i in range(1, 13)))
tace("codice lungo nel riquadro non conta", "Incolla questo nel foglio:\n```\n" + "\n".join("riga di codice %d" % i for i in range(60)) + "\n```")
kit = "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\nKIT\n" + lungo + "\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥\nTITOLO\n```\nG Ora 2\n```\nOGGETTO\n```\nx\n```"
tace("kit rosso lungo è un pacchetto", kit)
tace("documento con cornice blu", "🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦\n" + lungo + "\n📄 DOCUMENTO ⬇️")
tace("cornice verde sola non conta", "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\nPronto.\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

# ------------------------------------------------------------------ 3b limite 4 righe in modalità assenza (v1.2, 25/11/2026)
_ass = {"attiva": True, "inizio": "2026-11-23", "fine": "2026-11-25"}
_oggi_ass = datetime.date(2026, 11, 24)
dodici = "\n".join("Riga %d." % i for i in range(1, 13))
cornice_v = "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
scatta("assenza: 12 righe (il caso del 24/11 16:54)", cornice_v + "\n" + dodici + "\n" + cornice_v, 3, cfg=_ass, oggi=_oggi_ass)
scatta("assenza: 5 righe", "\n".join("Riga %d." % i for i in range(1, 6)), 3, cfg=_ass, oggi=_oggi_ass)
tace("assenza: 4 righe con cornice verde", cornice_v + "\nNotte: tutto controllato.\nRiga 2.\nRiga 3.\nRiga 4.\n" + cornice_v, cfg=_ass, oggi=_oggi_ass)
tace("assenza: codice lungo nel riquadro non conta", "Una riga.\n```\n" + "\n".join("x%d" % i for i in range(60)) + "\n```", cfg=_ass, oggi=_oggi_ass)
tace("assenza: kit rosso lungo", kit, cfg=_ass, oggi=_oggi_ass)
tace("fuori dalle date: 12 righe passano", dodici, cfg=_ass, oggi=datetime.date(2026, 11, 26))
tace("assenza spenta: 12 righe passano", dodici, cfg=dict(_ass, attiva=False), oggi=_oggi_ass)

# ------------------------------------------------------------------ 4 più domande
scatta("due domande", "Vuoi la prova scritta? E la vuoi anche per la 4TI?", 4)
scatta("tre domande su righe", "Quale quiz?\nQuale classe?\nQuando lo vuoi?", 4)
tace("una domanda", "Vuoi la prova scritta o orale?")
tace("punto interrogativo in un indirizzo", "Apri https://esempio.invalid/pagina?x=1&y=2 e premi il bottone blu.")
tace("domande dentro un riquadro", "Copia le domande:\n```\nChe cosa è un file?\nChe cosa è una cartella?\n```")

# ------------------------------------------------------------------ 5 ripetizioni
prima = "Ho preparato il quiz di Sicurezza per la 2INF e l'ho controllato sul foglio. Il quiz ha dodici domande a risposta multipla."
prec = fb.frasi_per_memoria(pulito(prima))
scatta("stessa frase due volte nel messaggio", "Il quiz ha dodici domande a risposta multipla.\nAltro.\nIl quiz ha dodici domande a risposta multipla.", 5)
scatta("frasi già dette nel messaggio di prima", prima + " Manca solo il titolo.", 5, precedente=prec)
tace("messaggio nuovo dopo uno diverso", "Il titolo è pronto: usa quello nel riquadro qui sotto per il registro.", precedente=prec)
tace("frase breve uguale («Annotato.»)", "Annotato.", precedente=fb.frasi_per_memoria("Annotato. Annotato."))
tace("senza memoria", prima)

# ------------------------------------------------------------------ 6 conteggi senza fonte
scatta("elenco di conteggi senza fonte",
       "Situazione:\n- 12 su 18 hanno finito il quiz\n- 5 allievi sono assenti\n- 3 file da correggere", 6)
tace("conteggi con fonte e ora", "Situazione (letto dal registro alle 13:58):\n- 12 su 18 hanno finito il quiz\n- 5 allievi sono assenti")
tace("conteggi con «non provato»", "Situazione, non provato:\n- 12 su 18 hanno finito il quiz\n- 5 allievi sono assenti")
tace("un solo numero in un passo", "1. Clicca sul bottone blu 3 volte.\n2. Premi il bottone verde.")

# ------------------------------------------------------------------ 7 conferma chiesta su un ordine già dato (#391)
ORD = "Preparami il quiz di Sicurezza per la 2INF e aggiorna il registro. Se te le dico è perché tu le faccia."
for nome, m in {
    "vuoi che lo faccia": "Il quiz è impostato. Vuoi che lo faccia adesso?",
    "procedo": "Ho letto il file del quiz. Procedo?",
    "te lo preparo": "Te lo preparo con le immagini?",
    "dimmi se": "Dimmi se devo aggiornare anche il registro della 2INF.",
    "fammi sapere quale scegli": "Fammi sapere quale scegli tra le due versioni del quiz.",
    "posso procedere": "Posso procedere con la versione breve?",
    "aspetto il tuo ok": "Il quiz è pronto, aspetto il tuo ok per aggiornare il registro.",
}.items():
    scatta("ordine già dato, conferma chiesta: " + nome, m, 7, docente=ORD)
tace("stessa frase ma senza testo del docente (non provato)", "Vuoi che lo faccia adesso?")
tace("docente ha solo chiesto un parere", "Vuoi che lo faccia adesso?", docente="Che ne pensi dei quiz a risposta multipla?")
tace("eccezione PUBB", "Vuoi che pubblichi? Aspetto il tuo PUBB 2.", docente=ORD)
tace("eccezione firma", "Procedo con la firma delle ore 5 e 6?", docente=ORD)
tace("eccezione push di dati non pubblici", "Vuoi che faccia il push dei cognomi nel pubblico?", docente=ORD)
tace("eccezione azione distruttiva", "Vuoi che cancelli la cartella vecchia?", docente=ORD)
tace("eccezione decisione con scadenza oggi", "Decisione solo tua: il preventivo scade oggi, procedo?", docente=ORD)
tace("aspetta il via: solo Annotato", "Vuoi che lo faccia?", docente="Aspetta il via, poi fai il quiz.")
tace("eseguito e riferito", "Fatto: quiz creato e registro aggiornato (letto dal file alle 10:42).", docente=ORD)
tace("domanda di scelta vera su un dato che solo lui ha", "Quale classe vuoi per il quiz, la 2INF o la 3INF?", docente=ORD)
tace("richiesta dentro un riquadro da copiare", "Incolla questo:\n```\nVuoi che lo faccia?\n```", docente=ORD)

# ------------------------------------------------------------------ messaggi brevi normali e cornici esistenti (0 falsi allarmi)
for nome, m in {
    "Annotato": "Annotato.",
    "PUBB non riuscito": "PUBB 2 NON riuscito: pubblica a mano.\nTitolo e testo sono nei riquadri qui sotto.\n```\nG Ora 2: reti\n```",
    "firma": "Firma entro le 14:05: mancano le ore 5 e 6 (FIRME-REGISTRO alle 13:10).",
    "cornice verde": "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\nFatto: ho aggiornato il file e l'ho provato (esito VERDE alle 10:42).\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
    "passi": "1. Clicca sul bottone blu in alto a destra.\n2. Premi «Invia».\n```\nTitolo da incollare\n```",
    "una domanda utile": "Il PC 14 non si accende: lo sostituisco con il PC 15?",
}.items():
    tace("breve normale: " + nome, m, cfg={})

# ------------------------------------------------------------------ 2bis insieme: hook intero con trascrizione finta e memoria
T = tempfile.mkdtemp()
os.makedirs(T + "/ris/config")
json.dump({"attiva": True, "inizio": "2000-01-01", "fine": "2099-12-31", "motivo": "prova",
           "criticita": CFG["criticita"] if CFG else {}, "decisione_o_domanda": CFG["decisione_o_domanda"] if CFG else r"\?"},
          open(T + "/ris/config/modalita-assenza.json", "w"))
cm.RIS = T + "/ris"
cm.STATO_BUON_SENSO = T + "/stato.json"


def hook(testo, sess="s1", attivo=False):
    sys.stdin = io.StringIO(json.dumps({"last_assistant_message": testo, "session_id": sess, "stop_hook_active": attivo,
                                        "transcript_path": T + "/non-esiste.jsonl"}, ensure_ascii=False))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        cm.main()
    sys.stdin = sys.__stdin__
    return out.getvalue()


o = hook("Preferisci la prova di giovedì o di venerdì? E la vuoi anche per la 4TI?")
verifica("hook: blocca domande in assenza", '"decision": "block"' in o and "buon senso" in o)
verifica("hook: il motivo ha perché e TOGLI", "TOGLI:" in o)
o = hook("Annotato.")
verifica("hook: «Annotato» passa", o.strip() == "")
primo = "Ho preparato la scheda della 2INF e l'ho controllata con il registro. La scheda ha dodici passi e un'immagine per passo."
o = hook(primo)
verifica("hook: primo messaggio passa", "buon senso" not in o)
o = hook(primo + " Manca il titolo.")
verifica("hook: ripetizione del messaggio di prima bloccata", "controllo 5" in o)
o = hook(primo + " Manca il titolo.", sess="altra-sessione")
verifica("hook: altra conversazione, nessuna ripetizione", "controllo 5" not in o)
o = hook("Riscritto: manca il titolo.", attivo=True)
verifica("hook: dopo il blocco (stop_hook_active) non blocca di nuovo", o.strip() == "")
o = hook("Il PC 14 è rotto: lo sostituisco con il PC 15?")
verifica("hook: PC rotto è criticità anche in assenza", "controllo 2" not in o)
cm.RIS = RIS

# ------------------------------------------------------------------ 3 falsi allarmi sul lavoro normale del 20/11/2026
conteggio = {}
brevi_bloccati = []
n_msg = n_brevi = 0
puliti = []
bob = RIS + "/bobine/corso/2026-11-20_bobina_b09df496.md"
if os.path.exists(bob) and CFG:
    cfg_nopass = dict(CFG, attiva=False)   # il 20/11 il docente c'era: la modalità assenza non si applica a quei messaggi
    testo = open(bob, encoding="utf-8").read()
    parti = re.split(r"\n\*\*(NICOLA|CLAUDE)\*\* \((\d\d:\d\d)\):\n", testo)
    for i in range(1, len(parti) - 2, 3):
        if parti[i] != "CLAUDE":
            continue
        corpo = re.sub(r"\[esito .*?\]\n", "\n", parti[i + 2] + "\n", flags=re.S)
        corpo = "\n".join(r for r in corpo.splitlines() if not re.match(r"^\s*\[[^\]]*\]\s*$", r)).strip()
        corpo = "\n\n".join(p_ for p_ in re.split(r"\n\s*\n", corpo) if not p_.lstrip().startswith("["))   # via le righe degli strumenti (non sono messaggio)
        if len(corpo.strip()) < 20:
            continue
        if len(corpo) < 20:
            continue
        n_msg += 1
        puliti.append((parti[i + 1], corpo))
        prec_doc = ""   # ultimo messaggio vero del docente prima di questo messaggio di Claude (per il controllo 7)
        for j in range(i - 3, 0, -3):
            if parti[j] == "NICOLA":
                prec_doc = parti[j + 2]
                break
        ns, motivi = numeri(corpo, oggi=datetime.date(2026, 11, 20), cfg=cfg_nopass, docente=prec_doc)
        for n in ns:
            conteggio[n] = conteggio.get(n, 0) + 1
        righe = [r for r in fb.fuori_riquadri(corpo) if r.strip() and not fb.RE_CORNICE.match(r)]
        domande = len([f for f in fb._frasi(fb.RE_URL.sub(" ", pulito(corpo))) if "?" in f])
        if len(righe) <= 12 and sum(len(r.strip()) for r in righe) <= 900 and domande <= 1 and not fb.e_pacchetto(corpo):
            n_brevi += 1
            if ns:
                brevi_bloccati.append((parti[i + 1], ns, [m[:110] for m in motivi]))
    n_kit = 0
    kit_bloccati = []
    for ora_, corpo in puliti:
        if not re.search(r"🟥🟥|🟦🟦", corpo):
            continue
        n_kit += 1
        ns, _m = numeri(corpo, oggi=datetime.date(2026, 11, 20), cfg=cfg_nopass, docente="Fai il kit. Se te le dico è perché tu le faccia.")
        if 3 in ns:
            kit_bloccati.append((ora_, ns))
    print("Messaggi veri del 20/11/2026: %d; blocchi per controllo (messaggi lunghi o con più domande compresi): %s" % (n_msg, conteggio))
    print("FALSI ALLARMI su messaggi BREVI normali (entro i limiti di righe e caratteri, <=1 domanda): %d su %d" % (len(brevi_bloccati), n_brevi))
    for b in brevi_bloccati[:20]:
        print("  ", b)
    print("FALSI ALLARMI (controllo 3 lunghezza) su messaggi con cornice rossa o blu del 20/11/2026: %d su %d" % (len(kit_bloccati), n_kit))
    for b in kit_bloccati[:20]:
        print("  ", b)
    verifica("0 falsi allarmi sui messaggi brevi normali", not brevi_bloccati)
    verifica("0 falsi allarmi sui kit esistenti (cornici rosse e blu)", not kit_bloccati)
else:
    print("FALSI ALLARMI: non provato (riservato o config assenti)")
    verifica("falsi allarmi non provati (riservato assente)", False)
print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
