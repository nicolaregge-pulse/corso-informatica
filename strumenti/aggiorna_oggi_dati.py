#!/usr/bin/env python3
"""Dati della vista «Oggi» del cruscotto (docs/cruscotto/dati/<CLASSE>-oggi.json). Versione 1.1 (13/11/2026).

Per ogni allievo e per ogni «voce» del giorno (un Documento su Classroom o un quiz su Moduli, per ora) scrive lo stato:
    documento: consegnato | non_consegnato | nd
    quiz:      fatto (punti, aperte «in correzione») | manca | non_abbinata | non_assegnato | nd
L'ELENCO delle voci viene dai dati: il file di configurazione (strumenti/oggi-<CLASSE>-config.json, senza nomi) dice quali voci
si ATTENDONO (ora, scadenza, ora del post, quiz nel post); lo script aggiunge da solo le colonne del giorno che trova nel foglio
e che il file non cita. La pagina non ha nessuna voce scritta a mano: disegna le colonne da questo JSON.

Fonti nel foglio Fabbrica (xlsx esportato, tenuto FUORI dal repository):
    «Situazione pubblica <CLASSE>»  quiz: miglior punteggio, MANCA, NON ABBINATA, «(provv.)» = aperte da correggere (solo «Nome I.»)
    «Situazione <CLASSE>»           SOLO per sapere quale «Nome I.» e' quale COGNOME Nome (stesso ordine); i cognomi NON escono
    «Consegne <CLASSE>»             Documenti di Classroom: Consegnato / Mancante, per allievo (cognomi: si convertono in «Nome I.»)
    «Elenco <CLASSE>», «Abbinamenti <CLASSE>», «Ris <id quiz>»   solo per l'ultimo invio dei quiz (ultimo segnale), mai in uscita con le email
    «Stato»                         ora dell'ultimo giro del motore Fabbrica

NOVITA' 1.1 (motore Fabbrica v2.22, schede nuove; se non ci sono, la voce dice «dato non disponibile: serve il motore v2.22» e il resto funziona come prima):
    «Documenti <CLASSE>»            per allievo e compito: stato, ora di consegna, immagini aggiunte al Documento (rispetto al modello), caratteri
                                    (cognomi: si convertono in «Nome I.»; il testo, il titolo del file e il link NON escono mai nel pubblico)
    «Risposte <id quiz>»            per allievo (tentativo migliore) e per domanda: punti (o «c» = aperta da correggere); in uscita solo punti e testo della
                                    DOMANDA (scritto dal docente), mai il testo delle risposte degli allievi; errori ricorrenti per domanda
Il foglio NON da': voti dei Documenti (il giudizio), presenze, Veyon. Dove il dato manca la voce dice «nd» con il perche' (R7: niente numeri senza fonte).

CONTROLLO PRIVACY BLOCCANTE (R1) prima di scrivere: nessuna chiocciola, ogni allievo «Nome I.», nessun cognome (generatori/privacy_nomi.py
del riservato; se manca lo script si ferma). Un file che non passa NON viene scritto.

Uso:
    python3 -I strumenti/aggiorna_oggi_dati.py FABBRICA.xlsx [CLASSE] [--esportato 2026-11-13T12:05:00+01:00]
CLASSE di partenza: 1INF. Config: strumenti/oggi-<CLASSE>-config.json.
"""
import csv
import datetime
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import aggiorna_cruscotto_dati as base  # noqa: E402  (stesse regole di privacy e di lettura delle celle)

try:
    from zoneinfo import ZoneInfo
    ROMA = ZoneInfo("Europe/Rome")
except Exception:  # noqa: BLE001
    ROMA = None

REPO = base.REPO
DEST = os.environ.get("CRUSCOTTO_DEST") or base.DEST   # solo per le prove: la cartella di prova al posto di docs/cruscotto/dati


def aware(dt):
    if dt.tzinfo is None and ROMA is not None:
        dt = dt.replace(tzinfo=ROMA)
    return dt


def iso(dt):
    return aware(dt).isoformat(timespec="seconds") if dt else None


def nk(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().upper()


def trova_testa(righe):
    return next((i for i, r in enumerate(righe) if len(r) > 1 and r[0].strip() == "Stato" and r[1].strip() == "Allievo"), None)


def ora_riga1(testo, esportato, giorno_default):
    """«dati letti il 13/11/2026 12:00:34» oppure «dati letti alle 11:46:02» -> datetime (ora di Roma)."""
    m = re.search(r"dati letti il (\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2}):(\d{2})", testo or "")
    if m:
        d, mo, y, h, mi, s = map(int, m.groups())
        return aware(datetime.datetime(y, mo, d, h, mi, s))
    m = re.search(r"dati letti alle (\d{1,2}):(\d{2}):(\d{2})", testo or "")
    if m:
        h, mi, s = map(int, m.groups())
        ex = aware(esportato)
        dt = ex.replace(hour=h, minute=mi, second=s, microsecond=0)
        if dt > ex:
            dt -= datetime.timedelta(days=1)
        return dt
    return None


def parse_cella_quiz(c):
    c = (c or "").strip()
    m = re.match(r"^(\d+)%\s*\((\d+)/(\d+)\)(.*)$", c)
    if m:
        return {"s": "fatto", "pct": int(m.group(1)), "mg": int(m.group(2)), "su": int(m.group(3)),
                "aperte_in_correzione": bool(re.search("provv", m.group(4), re.I)),
                "versione_precedente": bool(re.search("versione precedente", m.group(4), re.I))}
    if re.match(r"^MANCA", c, re.I):
        return {"s": "manca"}
    if re.match(r"^NON ABBINATA", c, re.I):
        return {"s": "non_abbinata"}
    return {"s": "nd"}


def parse_ultimo_invio(v, esportato):
    """«12/11 13:34» o datetime -> datetime di Roma (anno dell'export)."""
    if isinstance(v, datetime.datetime):
        return aware(v)
    m = re.match(r"^\s*(\d{1,2})/(\d{1,2})\s+(\d{1,2}):(\d{2})", str(v or ""))
    if not m:
        return None
    d, mo, h, mi = map(int, m.groups())
    try:
        return aware(datetime.datetime(aware(esportato).year, mo, d, h, mi))
    except ValueError:
        return None


MSG_V222 = "dato non disponibile: serve il motore v2.22"


def num(x):
    """«3», «3.0», 3 -> 3; altro -> None."""
    try:
        f = float(str(x).strip().replace(",", "."))
    except ValueError:
        return None
    return int(f) if f == int(f) else f


def ora_cons(txt, giorno):
    """«13/11 12:24» -> («12:24» se e' del giorno, altrimenti «13/11 12:24»), minuti dall'inizio del giorno o None."""
    m = re.match(r"^\s*0?(\d{1,2})/0?(\d{1,2})\s+(\d{1,2}):(\d{2})", txt or "")
    if not m:
        return None, None, False
    g = "%d/%d" % (int(m.group(1)), int(m.group(2)))
    hm = "%02d:%02d" % (int(m.group(3)), int(m.group(4)))
    stesso = g == "%d/%d" % tuple(int(x) for x in giorno.split("/"))
    return (hm if stesso else "%s %s" % (g, hm)), int(m.group(3)) * 60 + int(m.group(4)), stesso


def leggi_documenti(wb, classe, esportato, giorno):
    """Scheda «Documenti <CLASSE>» -> ({nk(COGNOME Nome): [righe]}, dato) oppure (None, None) se la scheda non c'e' ancora."""
    nome = "Documenti " + classe
    if nome not in wb.sheetnames:
        return None, None
    righe = base.righe_foglio(wb[nome])
    h = next((i for i, r in enumerate(righe) if len(r) > 4 and r[0].strip() == "Allievo" and r[4].strip() == "Stato"), None)
    if h is None:
        return None, None
    dato = ora_riga1(righe[0][0] if righe and righe[0] else "", esportato, giorno)
    out = {}
    for r in righe[h + 1:]:
        if not r or not r[0].strip():
            break
        r = r + [""] * (19 - len(r))
        out.setdefault(nk(r[0]), []).append(r)
    return out, dato


def leggi_risposte(wb, quiz_id):
    """Scheda «Risposte <id>» -> {domande: [{n, testo, max}], righe: {nk(COGNOME Nome): [punti per domanda]}, dato} (tentativo migliore) o None."""
    nome = "Risposte " + quiz_id
    if nome not in wb.sheetnames:
        # l'export di Google taglia i nomi delle schede a 31 caratteri: si cerca per inizio e si controlla l'id nella riga 2 della scheda
        cand = [x for x in wb.sheetnames if x.startswith(nome[:27]) and x.startswith("Risposte ")]
        trovata = None
        for x in cand:
            r2 = base.righe_foglio(wb[x])[1:2]
            if r2 and r2[0] and (" id %s " % quiz_id) in (r2[0][0] + " "):
                trovata = x
                break
        if trovata is None:
            return None
        nome = trovata
    righe = base.righe_foglio(wb[nome])
    h = next((i for i, r in enumerate(righe) if r and r[0].strip() == "Ora invio"), None)
    if h is None or h < 1:
        return None
    testa = righe[h]
    cd = [i for i, t in enumerate(testa) if re.fullmatch(r"D\d+", t.strip())]
    cp = [i for i, t in enumerate(testa) if re.fullmatch(r"P\d+", t.strip())]
    if not cd or len(cd) != len(cp):
        return None
    r3 = righe[h - 1] + [""] * (len(testa) - len(righe[h - 1]))
    domande = []
    for k, (a, b) in enumerate(zip(cd, cp)):
        mx = re.match(r"^max\s+(.+)$", r3[b].strip())
        domande.append({"n": k + 1, "testo": re.sub(r"\s*\(\d+(?:[.,]\d+)? pt\)$", "", r3[a].strip())[:160], "max": num(mx.group(1)) if mx else 0})
    dato = ora_riga1(righe[1][0] if len(righe) > 1 and righe[1] else "", datetime.datetime.now(), "")
    out = {}
    for r in righe[h + 1:]:
        if not r or not r[0].strip():
            break
        r = r + [""] * (len(testa) - len(r))
        if r[6].strip().lower() not in ("sì", "si"):
            continue
        pts = []
        for b in cp:
            v = r[b].strip()
            pts.append("c" if v.lower() == "da correggere" else (num(v) if v != "" else None))
        out[nk(r[1])] = {"p": pts, "mg": num(r[4]), "su": num(r[5])}
    return {"domande": domande, "righe": out, "dato": dato}


def stato_documento(rr, v, giorno):
    """Righe della scheda «Documenti» di UN allievo per UN compito (una per file allegato) -> stato per la vista. Niente testo, titolo o link."""
    stato = rr[0][4].strip().upper()
    d = {"s": "non_consegnato" if stato == "ASSEGNATO" else "consegnato", "stato_classroom": stato}
    if d["s"] == "consegnato":
        hm, minuti, stesso = ora_cons(rr[0][5], giorno)
        if hm:
            d["ora_consegna"] = hm
        scad = v.get("scadenza")
        tardi = stato == "IN RITARDO"
        if scad and minuti is not None and stesso:
            h, m = map(int, scad.split(":"))
            tardi = tardi or minuti > h * 60 + m
        if tardi:
            d["in_ritardo"] = True
    imm = [num(r[13]) for r in rr]
    car = [num(r[14]) for r in rr]
    n_imm = [x for x in imm if x is not None]
    n_car = [x for x in car if x is not None]
    if rr and not any(r[7].strip() for r in rr):
        d["immagini"], d["n_immagini"] = "nd", None
        d["immagini_nd"] = "nessun file allegato"
    elif n_imm:
        d["n_immagini"] = sum(n_imm)
        d["immagini"] = "si" if sum(n_imm) > 0 else "no"
        if len(n_imm) < len(imm):
            d["immagini_parziale"] = True
    else:
        d["immagini"], d["n_immagini"] = "nd", None
        d["immagini_nd"] = next((r[17].strip() for r in rr if r[17].strip()), "file non letto")[:80]
    d["caratteri"] = sum(n_car) if n_car else None
    return d


def carica_config(classe):
    p = os.path.join(QUI, "oggi-%s-config.json" % classe)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 1
    xlsx = args[0]
    classe = args[1].upper() if len(args) > 1 else "1INF"
    if "--esportato" in argv:
        esportato = datetime.datetime.fromisoformat(argv[argv.index("--esportato") + 1])
    else:
        esportato = datetime.datetime.fromtimestamp(os.path.getmtime(xlsx)).astimezone()
    if ROMA is not None:
        esportato = aware(esportato).astimezone(ROMA)   # tutte le ore del dato sono ore di Roma
    cfg = carica_config(classe)
    giorno = cfg["giorno"]
    pn = base.carica_privacy()
    import openpyxl
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    for s in ("Situazione pubblica " + classe, "Situazione " + classe, "Consegne " + classe):
        if s not in wb.sheetnames:
            print("STOP: scheda «%s» non trovata nel foglio." % s)
            return 2

    # ---- quiz: scheda pubblica ----
    rp = base.righe_foglio(wb["Situazione pubblica " + classe])
    hp = trova_testa(rp)
    if hp is None:
        print("STOP: «Situazione pubblica» senza intestazione Stato/Allievo.")
        return 2
    dato_quiz = ora_riga1(rp[0][0] if rp and rp[0] else "", esportato, giorno)
    colq = {}
    quiz_cols = []
    for i, h in enumerate(rp[hp]):
        pz = str(h).split("\n")
        if len(pz) >= 3 and pz[2].strip().startswith("quiz-"):
            quiz_cols.append({"col": i, "label": pz[0].strip(), "data": pz[1].strip(), "id": pz[2].strip()})
            colq[pz[2].strip()] = i
    stud_p = []
    for r in rp[hp + 1:]:
        if not r or r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        r = r + [""] * (len(rp[hp]) - len(r))
        stud_p.append(r)

    # ---- mappa COGNOME Nome -> «Nome I.» (stesso ordine delle due schede Situazione) ----
    rd = base.righe_foglio(wb["Situazione " + classe])
    hd = trova_testa(rd)
    stud_d = []
    for r in rd[hd + 1:]:
        if not r or r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        stud_d.append(r)
    if len(stud_d) != len(stud_p):
        print("STOP: «Situazione» e «Situazione pubblica» hanno un numero diverso di allievi (%d e %d): non abbino i nomi." % (len(stud_d), len(stud_p)))
        return 2
    cognome_a_breve = {}
    for d, p in zip(stud_d, stud_p):
        nome_d, breve = nk(d[1]), p[1].strip()
        cog = nome_d.split(" ")[0]
        # prova di coerenza: l'iniziale del «Nome I.» e' l'iniziale del cognome
        if not breve or breve.rstrip(".")[-1:].upper() != cog[:1]:
            print("STOP: l'abbinamento dei nomi non torna (riga %s): non pubblico." % (len(cognome_a_breve) + 1))
            return 2
        cognome_a_breve[nome_d] = breve
    allievi = [p[1].strip() for p in stud_p]

    # ---- Documenti: scheda Consegne (docente, cognomi) ----
    rc = base.righe_foglio(wb["Consegne " + classe])
    hc = trova_testa(rc)
    dato_doc = ora_riga1(rc[0][0] if rc and rc[0] else "", esportato, giorno)
    cons_cols = []
    for i, h in enumerate(rc[hc]):
        m = re.match(r"^\s*0?(\d{1,2})/0?(\d{1,2})\s+Ora\s*(\d+)", str(h))
        if m:
            cons_cols.append({"col": i, "titolo": str(h).strip(), "giorno": "%d/%d" % (int(m.group(1)), int(m.group(2))), "ora": int(m.group(3))})
    cons = {}
    for r in rc[hc + 1:]:
        if not r or r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        cons[nk(r[1])] = r + [""] * (len(rc[hc]) - len(r))
    g_norm = "%d/%d" % tuple(int(x) for x in giorno.split("/"))
    doc_det, dato_det = leggi_documenti(wb, classe, esportato, giorno)   # None se il motore v2.22 non c'e' ancora

    # ---- elenco delle voci: attese (config) + trovate nel foglio ----
    voci = [dict(v) for v in cfg["voci"]]
    usate_cons, usate_quiz = set(), set()
    for v in voci:
        if v["tipo"] == "documento":
            rx = re.compile(v.get("colonna_consegne") or r"^$")
            c = next((c for c in cons_cols if rx.search(c["titolo"])), None)
            v["_col"] = c
            v["_rx"] = rx
            if c:
                usate_cons.add(c["col"])
        else:
            v["_col"] = colq.get(v.get("quiz_id"))
            if v["_col"] is not None:
                usate_quiz.add(v["_col"])
    for c in cons_cols:
        if c["col"] not in usate_cons and c["giorno"] == g_norm:
            gg, mm = c["giorno"].split("/")
            voci.append({"id": "ora%d-documento-%d" % (c["ora"], c["col"]), "tipo": "documento", "ora": c["ora"], "titolo": "Documento: " + c["titolo"], "post_alle": None, "scadenza": None, "_col": c, "_trovata": True,
                         "_rx": re.compile(r"^\s*0?%s/0?%s\s+Ora\s*%d\b" % (gg, mm, c["ora"]))})
    for q in quiz_cols:
        mo = re.search(r"-ora(\d+)", q["id"])
        md = re.match(r"^\s*0?(\d{1,2})/0?(\d{1,2})", q["data"] or "")
        if q["col"] not in usate_quiz and md and "%d/%d" % (int(md.group(1)), int(md.group(2))) == g_norm:
            voci.append({"id": "ora%s-quiz-%d" % (mo.group(1) if mo else "0", q["col"]), "tipo": "quiz", "ora": int(mo.group(1)) if mo else 0, "titolo": "Quiz: " + q["label"], "quiz_id": q["id"], "nel_post": None, "_col": q["col"], "_trovata": True})
    voci.sort(key=lambda v: (v["ora"], 0 if v["tipo"] == "documento" else 1))

    # ---- risposte per domanda (scheda «Risposte <id>» del motore v2.22) ----
    risposte = {}
    for v in voci:
        if v["tipo"] == "quiz":
            risposte[v["id"]] = leggi_risposte(wb, v["quiz_id"])

    # ---- ultimo invio dei quiz (Ris), solo per l'ultimo segnale ----
    email_a_nome = {}
    for nome_sh, ci_e, ci_a in (("Elenco " + classe, 0, 1), ("Abbinamenti " + classe, 0, 1)):
        if nome_sh in wb.sheetnames:
            for r in base.righe_foglio(wb[nome_sh])[1:]:
                if len(r) > ci_a and "@" in r[ci_e] and nk(r[ci_a]) in cognome_a_breve:
                    email_a_nome[r[ci_e].strip().lower()] = cognome_a_breve[nk(r[ci_a])]
    ultimo = {}
    ris_resp = {}   # id voce -> {«Nome I.»: {mg, su, aperte}}: risposte del foglio «Ris» abbinate a un allievo (controllo incrociato con «Situazione pubblica»)
    for v in voci:
        if v["tipo"] != "quiz":
            continue
        pre = "Ris " + v["quiz_id"][:27]
        nome_sh = next((s for s in wb.sheetnames if s.startswith(pre) or s == "Ris " + v["quiz_id"]), None)
        v["risposte_ris"] = None
        if not nome_sh:
            continue
        ws = wb[nome_sh]
        righe = [list(r) for r in ws.iter_rows(values_only=True)]
        hi = next((i for i, r in enumerate(righe) if r and str(r[0]).strip() == "Email"), None)
        if hi is None:
            continue
        n = non_abb = 0
        for r in righe[hi + 1:]:
            if not r or not r[0]:
                continue
            n += 1
            quando = parse_ultimo_invio(r[4] if len(r) > 4 else None, esportato)
            nome = email_a_nome.get(str(r[0]).strip().lower())
            if nome is None:
                non_abb += 1
            elif quando and (nome not in ultimo or quando > ultimo[nome]):
                ultimo[nome] = quando
            if nome is not None:
                try:
                    ris_resp.setdefault(v["id"], {})[nome] = {"mg": int(float(r[1])), "su": int(float(r[2])), "aperte": int(float(r[5] or 0)) if len(r) > 5 else 0}
                except (TypeError, ValueError):
                    pass
        v["risposte_ris"] = n
        v["risposte_ris_non_abbinate"] = non_abb

    # ---- stati per allievo ----
    out_voci = []
    for v in voci:
        o = {"id": v["id"], "tipo": v["tipo"], "ora": v["ora"], "orario_ora": "%d-%d" % (7 + v["ora"], 8 + v["ora"]) if v["ora"] else None,
             "titolo": v["titolo"], "voto": None}
        if v["tipo"] == "documento":
            o.update({"post_alle": v.get("post_alle"), "scadenza": v.get("scadenza"), "colonna_foglio": v["_col"]["titolo"] if v["_col"] else None,
                      "fonte": "Consegne " + classe, "dato": iso(dato_doc)})
            if not v["_col"]:
                if v.get("post_alle") and dato_doc:
                    hh, mm = map(int, v["post_alle"].split(":"))
                    dopo = dato_doc.replace(hour=hh, minute=mm, second=0, microsecond=0) > dato_doc
                else:
                    dopo = False
                o["nd_motivo"] = ("il compito e' stato pubblicato alle %s, dopo l'ultima lettura di Classroom del foglio (%s): la sua colonna non c'e' ancora" % (v["post_alle"], dato_doc.strftime("%H:%M:%S")) if dopo
                                  else "la colonna di questo compito non c'e' nel foglio «Consegne %s» (letto alle %s)" % (classe, dato_doc.strftime("%H:%M:%S") if dato_doc else "?"))
            titoli_doc = {r[2] for rr in (doc_det or {}).values() for r in rr}
            v["_doc"] = doc_det is not None and any(v["_rx"].search(t) for t in titoli_doc)
            if doc_det is None:
                o["dettaglio_nd"] = MSG_V222
                o["voto_nd"] = "Classroom, letto dal foglio, non da' il voto ne' il contenuto del Documento (se ci sono gli screenshot): solo consegnato / non consegnato. " + MSG_V222
            elif not v["_doc"]:
                o["dettaglio_nd"] = "il compito non e' ancora nella scheda «Documenti %s» (letta alle %s)" % (classe, dato_det.strftime("%H:%M:%S") if dato_det else "?")
                o["voto_nd"] = "Classroom non da' il voto: la scheda «Documenti» da' stato, ora di consegna e immagini aggiunte, non il giudizio. " + o["dettaglio_nd"]
            else:
                o["fonte_dettaglio"] = "Documenti " + classe
                o["dato_dettaglio"] = iso(dato_det)
                o["voto_nd"] = "Classroom non da' il voto: la scheda «Documenti» da' stato, ora di consegna e immagini aggiunte al Documento (rispetto al modello), non il giudizio"
        else:
            o.update({"nel_post": v.get("nel_post"), "quiz_id": v["quiz_id"], "fonte": "Situazione pubblica " + classe, "dato": iso(dato_quiz), "risposte_ris": v.get("risposte_ris"), "risposte_ris_non_abbinate": v.get("risposte_ris_non_abbinate"),
                      "colonna_foglio": "presente" if v["_col"] is not None else None})
            if v["_col"] is None:
                o["nd_motivo"] = "il quiz non e' una colonna della «Situazione pubblica %s»" % classe
            rsp = risposte.get(v["id"])
            if not cfg.get("domande_pubbliche", True):   # interruttore del docente: i punti per domanda restano solo nel foglio (riservato)
                rsp = None
                risposte[v["id"]] = None
            if rsp is None:
                o["dettaglio_nd"] = MSG_V222 if cfg.get("domande_pubbliche", True) else "i punti per domanda non sono pubblici (decisione del docente)"
            else:
                o["domande"] = [{"n": d["n"], "testo": d["testo"], "max": d["max"]} for d in rsp["domande"]]
                o["fonte_dettaglio"] = "Risposte " + v["quiz_id"]
                o["dato_dettaglio"] = iso(rsp["dato"])
        out_voci.append(o)

    righe_out = []
    for k, nome in enumerate(allievi):
        r_p = stud_p[k]
        nome_d = next((d for d, b in cognome_a_breve.items() if b == nome), None)
        r_c = cons.get(nome_d) if nome_d else None
        stati = {}
        for v in voci:
            if v["tipo"] == "documento":
                rr_d = (doc_det or {}).get(nome_d, []) if (doc_det is not None and v.get("_doc")) else []
                rr_d = [r for r in rr_d if v["_rx"].search(r[2])]
                if rr_d:
                    stati[v["id"]] = stato_documento(rr_d, v, giorno)
                elif v["_col"] is None or r_c is None:
                    stati[v["id"]] = {"s": "nd"}
                else:
                    x = (r_c[v["_col"]["col"]] or "").strip().lower()
                    stati[v["id"]] = {"s": "consegnato"} if x in ("consegnato", "riconsegnato") else ({"s": "non_consegnato"} if x == "mancante" else {"s": "nd"})
            else:
                if v["_col"] is None:
                    stati[v["id"]] = {"s": "nd"}
                else:
                    st = parse_cella_quiz(r_p[v["_col"]])
                    rr = ris_resp.get(v["id"], {}).get(nome)
                    if st["s"] == "manca" and rr and rr["su"]:   # «Situazione pubblica» dice MANCA ma il foglio «Ris» ha la sua risposta: vale la risposta (non e' mancante)
                        st = {"s": "fatto", "pct": int(round(100.0 * rr["mg"] / rr["su"])), "mg": rr["mg"], "su": rr["su"], "aperte_in_correzione": rr["aperte"] > 0, "versione_precedente": False, "da_ris": True}
                    rsd = (risposte.get(v["id"]) or {}).get("righe", {}).get(nome_d)
                    if st["s"] == "manca" and rsd and rsd["su"] and rsd["mg"] is not None:   # stessa regola per la scheda «Risposte»: la risposta c'e', non e' mancante
                        st = {"s": "fatto", "pct": int(round(100.0 * rsd["mg"] / rsd["su"])), "mg": rsd["mg"], "su": rsd["su"], "aperte_in_correzione": "c" in rsd["p"], "versione_precedente": False, "da_risposte": True}
                    if st["s"] == "manca" and v.get("nel_post") is False:
                        st = {"s": "non_assegnato"}
                    elif st["s"] == "manca" and v.get("nel_post") is None:
                        st = {"s": "nd", "perche": "non so se il quiz e' nel post"}
                    rsp = risposte.get(v["id"])
                    if rsp is not None and nome_d in rsp["righe"] and st["s"] == "fatto":
                        st["domande"] = rsp["righe"][nome_d]["p"]
                    stati[v["id"]] = st
        righe_out.append({"nome": nome, "stati": stati, "ultimo_segnale": iso(ultimo.get(nome))})

    # errori ricorrenti per domanda (solo allievi con il tentativo migliore letto; chi ha una risposta sotto il massimo conta sbagliata)
    for o in out_voci:
        if not o.get("domande"):
            continue
        err = []
        for d in o["domande"]:
            if not d["max"]:
                continue
            sb = dc = gi = 0
            for a in righe_out:
                dom = a["stati"].get(o["id"], {}).get("domande")
                if not dom or len(dom) < d["n"]:
                    continue
                x = dom[d["n"] - 1]
                if x == "c":
                    dc += 1
                elif isinstance(x, (int, float)) and x >= d["max"]:
                    gi += 1
                else:
                    sb += 1
            err.append({"n": d["n"], "sbagliata": sb, "da_correggere": dc, "giusta": gi})
        err.sort(key=lambda e: (-e["sbagliata"], e["n"]))
        o["errori_ricorrenti"] = err

    stato_sh = base.righe_foglio(wb["Stato"]) if "Stato" in wb.sheetnames else []
    giro = next((r[1] for r in stato_sh if r and r[0].strip() == "Fabbrica v2" and len(r) > 1), "")
    mg = re.match(r"^(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2}):(\d{2})$", giro.strip())
    motore = iso(datetime.datetime(int(mg.group(3)), int(mg.group(2)), int(mg.group(1)), int(mg.group(4)), int(mg.group(5)), int(mg.group(6)))) if mg else None

    J = {
        "versione": "1.1", "classe": classe, "giorno": giorno, "esportato": iso(esportato),
        "fonti": {
            "quiz": {"scheda": "Situazione pubblica " + classe, "dato": iso(dato_quiz)},
            "documenti": {"scheda": "Consegne " + classe, "dato": iso(dato_doc)},
            "documenti_dettaglio": {"scheda": "Documenti " + classe, "dato": iso(dato_det)} if doc_det is not None else None,
            "ultimo_giro_motore": motore,
        },
        "config": {"fonte": cfg.get("fonte_config"), "file": "strumenti/oggi-%s-config.json" % classe},
        "presenze": "dal registro DIDAweb: vedi dati/<CLASSE>-presenze.json (solo Nome I., scritto da strumenti/aggiorna_presenze_dati.py). Veyon di oggi: non letto.",
        "ultimo_segnale_fonte": "solo l'ultimo invio di un quiz del giorno (Moduli). Non c'e' Veyon di oggi" + ("" if doc_det is not None else " ne' l'ora delle consegne dei Documenti (" + MSG_V222 + ")"),
        "n_allievi": len(righe_out),
        "voci": out_voci, "allievi": righe_out,
    }
    testo = json.dumps(J, ensure_ascii=False, indent=1)
    guai = []
    if "@" in testo:
        guai.append("c'e' una chiocciola (email)")
    for a in allievi:
        if not (base.RE_ALLIEVO.match(a) or base.RE_ALLIEVO_N.match(a)):
            guai.append("un allievo non e' in forma «Nome I.»")
            break
    trovati = pn.trova(testo)
    if trovati:
        guai.append("cognome di un allievo nel testo (%s)" % ", ".join(sorted(set(trovati))))
    dest = os.path.join(DEST, "%s-oggi.json" % classe)
    if guai:
        if os.path.exists(dest):
            os.remove(dest)
        print("ATTENZIONE %s oggi: NON pubblicato, %s" % (classe, "; ".join(guai)))
        return 3
    os.makedirs(DEST, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(testo + "\n")
    mp = os.path.join(DEST, "meta.json")
    try:
        with open(mp, encoding="utf-8") as f:
            meta = json.load(f)
        meta.setdefault("classi", {}).setdefault(classe, {})["oggi"] = True
        with open(mp, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=1)
            f.write("\n")
    except Exception as e:  # noqa: BLE001
        print("meta.json non aggiornato (%s)" % str(e)[:60])
    # coerenza con la vista «Quiz e voti»: la sua copia della «Situazione pubblica» (CSV) dice MANCA dove il foglio «Ris» ha la risposta
    # abbinata di un quiz di oggi: nella copia la cella diventa «NN% (punti/totale)», come nella vista «Oggi» (stessa fonte, stesso numero)
    cp = os.path.join(DEST, "%s-situazione.csv" % classe)
    if os.path.exists(cp) and ris_resp:
        with open(cp, encoding="utf-8", newline="") as f:
            rr = list(csv.reader(f))
        hh = trova_testa(rr)
        if hh is not None:
            tocc = 0
            for v in voci:
                if v["tipo"] != "quiz" or v["id"] not in ris_resp:
                    continue
                col = next((i for i, h in enumerate(rr[hh]) if v["quiz_id"] in str(h)), None)
                if col is None:
                    continue
                for r in rr[hh + 1:]:
                    if len(r) > col and len(r) > 1 and r[col].strip().upper().startswith("MANCA") and r[1].strip() in ris_resp[v["id"]]:
                        x = ris_resp[v["id"]][r[1].strip()]
                        if x["su"]:
                            r[col] = "%d%% (%d/%d)%s" % (int(round(100.0 * x["mg"] / x["su"])), x["mg"], x["su"], " (provv.)" if x["aperte"] else "")
                            tocc += 1
            if tocc:
                base.scrivi_csv(cp, rr)
                print("  %s-situazione.csv: %d celle MANCA -> risposta letta nella scheda Ris (stessa fonte della vista Oggi)" % (classe, tocc))
    print("%s oggi: scritto %s (%d allievi, %d voci)" % (classe, dest, len(righe_out), len(out_voci)))
    print("  quiz dato %s · documenti dato %s · motore %s · esportato %s" % (iso(dato_quiz), iso(dato_doc), motore, iso(esportato)))
    for v in out_voci:
        n = {}
        for a in righe_out:
            s = a["stati"][v["id"]]["s"]
            n[s] = n.get(s, 0) + 1
        print("  %-22s %s%s" % (v["id"], n, (" · nd: " + v["nd_motivo"]) if v.get("nd_motivo") else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
