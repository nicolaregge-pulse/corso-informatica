#!/usr/bin/env python3
"""Dati della vista «Oggi» del cruscotto (docs/cruscotto/dati/<CLASSE>-oggi.json). Versione 1.0 (13/11/2026).

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

Il foglio NON da': voti dei Documenti, ora delle consegne, contenuto dei Documenti (se ci sono davvero gli screenshot), presenze, Veyon.
Dove il dato manca la voce dice «nd» con il perche' (R7: niente numeri senza fonte).

CONTROLLO PRIVACY BLOCCANTE (R1) prima di scrivere: nessuna chiocciola, ogni allievo «Nome I.», nessun cognome (generatori/privacy_nomi.py
del riservato; se manca lo script si ferma). Un file che non passa NON viene scritto.

Uso:
    python3 -I strumenti/aggiorna_oggi_dati.py FABBRICA.xlsx [CLASSE] [--esportato 2026-11-13T12:05:00+01:00]
CLASSE di partenza: 1INF. Config: strumenti/oggi-<CLASSE>-config.json.
"""
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
        if r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        r = r + [""] * (len(rp[hp]) - len(r))
        stud_p.append(r)

    # ---- mappa COGNOME Nome -> «Nome I.» (stesso ordine delle due schede Situazione) ----
    rd = base.righe_foglio(wb["Situazione " + classe])
    hd = trova_testa(rd)
    stud_d = []
    for r in rd[hd + 1:]:
        if r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
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
        if r[0].strip() not in ("VERDE", "ROSSO", "ND", "GIALLO", "ARANCIO"):
            break
        cons[nk(r[1])] = r + [""] * (len(rc[hc]) - len(r))
    g_norm = "%d/%d" % tuple(int(x) for x in giorno.split("/"))

    # ---- elenco delle voci: attese (config) + trovate nel foglio ----
    voci = [dict(v) for v in cfg["voci"]]
    usate_cons, usate_quiz = set(), set()
    for v in voci:
        if v["tipo"] == "documento":
            rx = re.compile(v.get("colonna_consegne") or r"^$")
            c = next((c for c in cons_cols if rx.search(c["titolo"])), None)
            v["_col"] = c
            if c:
                usate_cons.add(c["col"])
        else:
            v["_col"] = colq.get(v.get("quiz_id"))
            if v["_col"] is not None:
                usate_quiz.add(v["_col"])
    for c in cons_cols:
        if c["col"] not in usate_cons and c["giorno"] == g_norm:
            voci.append({"id": "ora%d-documento-%d" % (c["ora"], c["col"]), "tipo": "documento", "ora": c["ora"], "titolo": "Documento: " + c["titolo"], "post_alle": None, "scadenza": None, "_col": c, "_trovata": True})
    for q in quiz_cols:
        mo = re.search(r"-ora(\d+)", q["id"])
        md = re.match(r"^\s*0?(\d{1,2})/0?(\d{1,2})", q["data"] or "")
        if q["col"] not in usate_quiz and md and "%d/%d" % (int(md.group(1)), int(md.group(2))) == g_norm:
            voci.append({"id": "ora%s-quiz-%d" % (mo.group(1) if mo else "0", q["col"]), "tipo": "quiz", "ora": int(mo.group(1)) if mo else 0, "titolo": "Quiz: " + q["label"], "quiz_id": q["id"], "nel_post": None, "_col": q["col"], "_trovata": True})
    voci.sort(key=lambda v: (v["ora"], 0 if v["tipo"] == "documento" else 1))

    # ---- ultimo invio dei quiz (Ris), solo per l'ultimo segnale ----
    email_a_nome = {}
    for nome_sh, ci_e, ci_a in (("Elenco " + classe, 0, 1), ("Abbinamenti " + classe, 0, 1)):
        if nome_sh in wb.sheetnames:
            for r in base.righe_foglio(wb[nome_sh])[1:]:
                if len(r) > ci_a and "@" in r[ci_e] and nk(r[ci_a]) in cognome_a_breve:
                    email_a_nome[r[ci_e].strip().lower()] = cognome_a_breve[nk(r[ci_a])]
    ultimo = {}
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
            o["voto_nd"] = "Classroom, letto dal foglio, non da' il voto ne' il contenuto del Documento (se ci sono gli screenshot): solo consegnato / non consegnato"
        else:
            o.update({"nel_post": v.get("nel_post"), "quiz_id": v["quiz_id"], "fonte": "Situazione pubblica " + classe, "dato": iso(dato_quiz), "risposte_ris": v.get("risposte_ris"),
                      "colonna_foglio": "presente" if v["_col"] is not None else None})
            if v["_col"] is None:
                o["nd_motivo"] = "il quiz non e' una colonna della «Situazione pubblica %s»" % classe
        out_voci.append(o)

    righe_out = []
    for k, nome in enumerate(allievi):
        r_p = stud_p[k]
        nome_d = next((d for d, b in cognome_a_breve.items() if b == nome), None)
        r_c = cons.get(nome_d) if nome_d else None
        stati = {}
        for v in voci:
            if v["tipo"] == "documento":
                if v["_col"] is None or r_c is None:
                    stati[v["id"]] = {"s": "nd"}
                else:
                    x = (r_c[v["_col"]["col"]] or "").strip().lower()
                    stati[v["id"]] = {"s": "consegnato"} if x in ("consegnato", "riconsegnato") else ({"s": "non_consegnato"} if x == "mancante" else {"s": "nd"})
            else:
                if v["_col"] is None:
                    stati[v["id"]] = {"s": "nd"}
                else:
                    st = parse_cella_quiz(r_p[v["_col"]])
                    if st["s"] == "manca" and v.get("nel_post") is False:
                        st = {"s": "non_assegnato"}
                    elif st["s"] == "manca" and v.get("nel_post") is None:
                        st = {"s": "nd", "perche": "non so se il quiz e' nel post"}
                    stati[v["id"]] = st
        righe_out.append({"nome": nome, "stati": stati, "ultimo_segnale": iso(ultimo.get(nome))})

    stato_sh = base.righe_foglio(wb["Stato"]) if "Stato" in wb.sheetnames else []
    giro = next((r[1] for r in stato_sh if r and r[0].strip() == "Fabbrica v2" and len(r) > 1), "")
    mg = re.match(r"^(\d{2})/(\d{2})/(\d{4}) (\d{2}):(\d{2}):(\d{2})$", giro.strip())
    motore = iso(datetime.datetime(int(mg.group(3)), int(mg.group(2)), int(mg.group(1)), int(mg.group(4)), int(mg.group(5)), int(mg.group(6)))) if mg else None

    J = {
        "versione": "1.0", "classe": classe, "giorno": giorno, "esportato": iso(esportato),
        "fonti": {
            "quiz": {"scheda": "Situazione pubblica " + classe, "dato": iso(dato_quiz)},
            "documenti": {"scheda": "Consegne " + classe, "dato": iso(dato_doc)},
            "ultimo_giro_motore": motore,
        },
        "config": {"fonte": cfg.get("fonte_config"), "file": "strumenti/oggi-%s-config.json" % classe},
        "presenze": "non lette: nessuna fonte di oggi (registro, Veyon). Sono elencati tutti gli allievi del foglio; per gli assenti usa la spunta «Assente».",
        "ultimo_segnale_fonte": "solo l'ultimo invio di un quiz del giorno (Moduli). Non c'e' Veyon di oggi ne' l'ora delle consegne dei Documenti",
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
