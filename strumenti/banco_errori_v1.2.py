#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Banco di prova degli errori v1.2 (v1.0: 23/11/2026, ordine del docente: «ogni errore passato diventa un test automatico»).

Principio R00.2 di CLAUDE.md: un errore nuovo corregge uno STRUMENTO. Questo è lo strumento che dice, per ogni errore del
registro (REGISTRO-ERRORI-CLAUDE.md, #1-#389 più le voci del 01/10 e del 02/10), se un controllo automatico LO FERMEREBBE
davvero se si ripresentasse. Non spiega mai un NON COPERTO come «atteso»: è un buco.

DATI (nel pubblico, nessun cognome di allievo: i nomi dei test sono inventati)
  tests/errori/indice.json        una riga per errore: numero, titolo, categoria dell'audit, schema, copertura dichiarata dalla
                                  MAPPA, e uno tra «caso» (file in casi/) e «non_verificabile» (motivo scritto).
  tests/errori/casi/*.json        un caso per errore verificabile a macchina: input SBAGLIATO (rifatto dalla descrizione del
                                  registro, anonimizzato), input GIUSTO e il controllo che deve scattare. Formato:
      {"errore": "#50", "titolo": "...", "categoria": "F", "schema": 1, "origine_input": "...", "controllo_atteso": "...",
       "prove": [{"canale": "messaggio|comando|pagina|kit|pdf|leggibilita|post|cruscotto|budget|quiz_lingue",
                  "atteso": "regex che deve comparire nell'esito del controllo (solo per messaggio e comando)",
                  "sbagliato": {...}, "giusto": {...}}]}
      Piu' «prove» = più strumenti che potrebbero fermare lo stesso errore: il caso è COPERTO se ALMENO UNA scatta sul
      sbagliato senza scattare sul giusto.
  tests/errori/specifiche-v1.0.json   per gli errori NON COPERTI: il controllo più piccolo che li coprirebbe (solo testo).
  tests/errori/baseline-coperti.json  errori COPERTI all'ultimo giro: con --regressioni il banco esce 1 se uno non scatta più
                                      (un controllo tolto o rotto) o se un controllo scatta sul GIUSTO (falso allarme).

CANALI (chiamano i controlli veri, senza modificarli, su repository finti in una cartella temporanea)
  messaggio    .claude/hooks/controllo-messaggio.py (main con trascrizione finta); atteso = regex sul motivo del blocco/avviso
  comando      .claude/hooks/limite-comandi.py (comando Bash, push e commit del pubblico, cognomi finti)
  pagina       .claude/hooks/controlli_pagine.py (TUTTI i controlli sulle pagine dei ragazzi)
  kit          corso-informatica-riservato/strumenti/controlla_kit.py (kit Classroom con PDF finti)
  pdf          strumenti/controlla_pdf_ragazzi.py
  leggibilita  strumenti/controlla_leggibilita.py
  post         strumenti/controlli_consegna.py (titolo e testo del post)
  cruscotto    strumenti/controlli_consegna.py (dato di oggi del cruscotto)
  budget       strumenti/controlla_budget_1inf.py
  quiz_lingue  strumenti/controlla_lingue_quiz.py
  audit_regole riservato generatori/audit_regole.py (coda, annunci, comandi del ponte; cartelle finte)
  fine_giornata strumenti/controlla_controlli.py (controllore di fine giornata e firme_sospette; cartelle finte)
  bobina       .claude/hooks/bobina-automatica.py (pulizia di chiavi e password)

USCITA
  stato per errore: COPERTO | NON COPERTO | NON VERIFICABILE A MACCHINA (con il motivo scritto) | CASO DA SCRIVERE (verificabile a macchina,
  ma il caso non è ancora stato scritto: è lavoro da fare, non una scusa) | ERRORE DEL BANCO (il caso non si è potuto eseguire:
  NON conta mai come coperto).
  Uso: python3 strumenti/banco_errori_v1.2.py [--solo "#50,#63"] [--json FILE] [--md FILE] [--regressioni] [--aggiorna-baseline] [-v]
  Esce 0 se non ci sono ERRORE DEL BANCO né regressioni (i NON COPERTI non fanno fallire: sono il lavoro da fare, sono nel rapporto).

Versioni: v1.2 (23/11/2026, errore #390, filtro di buon senso): il canale «messaggio» accetta «ris_files» (file scritti nel riservato finto, per esempio config/modalita-assenza.json) e la memoria dell'ultimo messaggio del filtro è spenta. v1.0 (23/11/2026) prima versione. v1.1 (23/11/2026, controlli rimessi): i segnaposto {{ORA-1}}, {{ORA-2}}, {{ORA-3}} dei casi
(finora lasciati scritti alla lettera, e cosi' i casi «giusti» con l'ora della fonte davano un falso allarme) ora si sostituiscono come gli altri.
"""
import argparse
import contextlib
import datetime
import glob
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from zoneinfo import ZoneInfo

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIS = "/home/user/corso-informatica-riservato"
HOOKS = os.environ.get("BANCO_HOOKS") or os.path.join(PUB, ".claude", "hooks")   # BANCO_HOOKS: copia degli hook per provare il banco stesso
STR = os.path.join(PUB, "strumenti")
DATI = os.path.join(PUB, "tests", "errori")
TZ = ZoneInfo("Europe/Rome")
NOMI_FINTI = ["ROSSI MARIO", "BIANCHI ANNA", "VERDI LUCA"]   # nomi inventati: nessun allievo vero nei test

# Categorie dell'audit (AUDIT-ERRORI-STATISTICA-v1.0.md, sezione 6): codice -> (nome, indice di importanza, posizione)
CATEGORIE = {
    "K": ("Kit e materiali per i ragazzi", 332, 1), "P": ("Pubblicazione Classroom", 255, 2),
    "R": ("Regole/errori noti non riletti o non applicati", 245, 3), "F": ("Formato dei messaggi e hook", 240, 4),
    "Q": ("Dichiarato senza verificare / non funziona", 228, 5), "C": ("Cruscotto e monitoraggio", 189, 6),
    "H": ("Messaggio poco chiaro", 165, 7), "D": ("Dati, presenze, registro, voti", 107, 8),
    "V": ("Versioni e file", 86, 9), "S": ("Presunto invece di chiedere", 55, 10),
    "X": ("Privacy", 0, 11), "A": ("Account e accessi", 0, 12), "O": ("Altro", 0, 13),
}
COPERTO, NON_COPERTO, NON_VERIF, ERR = "COPERTO", "NON COPERTO", "NON VERIFICABILE A MACCHINA", "ERRORE DEL BANCO"
DA_SCRIVERE = "CASO DA SCRIVERE"


# ------------------------------------------------------------------ utilita'

def carica(nome, cartella):
    spec = importlib.util.spec_from_file_location("banco_" + re.sub(r"\W", "_", nome), os.path.join(cartella, nome))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sh(*a, cwd=None):
    subprocess.run(a, cwd=cwd, check=True, capture_output=True)


def git_commit(cwd, msg):
    sh("git", "-c", "user.name=banco", "-c", "user.email=banco@example.invalid", "commit", "-q", "-m", msg, cwd=cwd)


def scrivi(base, rel, contenuto):
    p = os.path.join(base, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(contenuto)
    return p


def _esc_pdf(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def crea_pdf(percorso, pagine):
    """PDF minimo ma vero (si apre con pdfinfo e pdftotext). pagine = [[riga, riga, ...], ...]."""
    out, off = [b"%PDF-1.4\n"], []

    def aggiungi(b):
        off.append(sum(len(x) for x in out))
        out.append(b)

    n = len(pagine)
    figli = " ".join("%d 0 R" % (4 + 2 * i) for i in range(n))
    aggiungi(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    aggiungi(("2 0 obj\n<< /Type /Pages /Kids [%s] /Count %d >>\nendobj\n" % (figli, n)).encode())
    aggiungi(b"3 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")
    for i, righe in enumerate(pagine):
        pid, cid = 4 + 2 * i, 5 + 2 * i
        aggiungi(("%d 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R >> >> "
                  "/Contents %d 0 R >>\nendobj\n" % (pid, cid)).encode())
        cs = ["BT", "/F1 6 Tf", "7 TL", "30 820 Td"] + ["(%s) Tj T*" % _esc_pdf(r) for r in righe] + ["ET"]
        flusso = "\n".join(cs).encode("cp1252", "replace")
        aggiungi(("%d 0 obj\n<< /Length %d >>\nstream\n" % (cid, len(flusso))).encode() + flusso + b"\nendstream\nendobj\n")
    pos = sum(len(x) for x in out)
    xref = ["xref\n0 %d\n0000000000 65535 f \n" % (len(off) + 1)] + ["%010d 00000 n \n" % o for o in off]
    out.append("".join(xref).encode())
    out.append(("trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(off) + 1, pos)).encode())
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    with open(percorso, "wb") as f:
        f.write(b"".join(out))


class Banco:
    """Repository finti (pubblico con origin, riservato con elenchi di nomi inventati) in una cartella temporanea."""

    def __init__(self):
        self.t = tempfile.mkdtemp(prefix="banco-errori-")
        self.pub, self.ris, self.bare = self.t + "/pub", self.t + "/ris", self.t + "/bare.git"
        sh("git", "init", "-q", "--bare", self.bare)
        sh("git", "init", "-q", "-b", "main", self.pub)
        scrivi(self.pub, "docs/2inf-prova/index.html", "<p>ciao</p>")
        scrivi(self.pub, "docs/1inf/index.html", "<p>ciao</p>")
        scrivi(self.pub, "fabbrica/nota.md", "nota\n")
        scrivi(self.pub, "fabbrica/motore.js", "var motore = 1;\n")
        scrivi(self.pub, "docs/1inf/elenco.md", "elenco\n")
        scrivi(self.pub, "docs/4ti/scheda.md", "scheda\n")
        scrivi(self.pub, "PROSSIME-LEZIONI.md", "# Prossime lezioni\n")
        scrivi(self.pub, "prove/esempio.md", "esempio\n")
        sh("git", "add", "-A", cwd=self.pub)
        git_commit(self.pub, "base")
        sh("git", "remote", "add", "origin", self.bare, cwd=self.pub)
        sh("git", "push", "-q", "origin", "main", cwd=self.pub)
        sh("git", "fetch", "-q", cwd=self.pub)
        os.symlink(STR, self.pub + "/strumenti")   # le librerie dei controlli (controlli_consegna.py...) restano quelle vere
        for d in ("coda", "comandi", "config", "dati/verifiche-lezione"):
            os.makedirs(os.path.join(self.ris, d), exist_ok=True)
        json.dump(NOMI_FINTI, open(self.ris + "/config/2inf-presenti-20261028.json", "w"))
        json.dump({"nomi": [], "parole_comuni": []}, open(self.ris + "/config/nomi-controllo.json", "w"))
        scrivi(self.ris, "coda/a.json", '{"stato": "ok"}')
        self.n = 0
        self.scritti_ris = []
        # moduli degli hook: i nomi finti sostituiscono gli elenchi del riservato vero
        sys.path.insert(0, HOOKS)
        import controllo_nomi
        import controlli_pagine
        self.cn, self.cp = controllo_nomi, controlli_pagine
        controllo_nomi.RIS = self.ris
        controllo_nomi._CACHE.clear()
        controlli_pagine.RIS = self.ris
        controlli_pagine._NOMI = None

    def scrivi_ris(self, rel, contenuto):
        p = scrivi(self.ris, rel, contenuto)
        self.scritti_ris.append(p)
        return p

    def scrivi_in(self, rel, contenuto):
        """«ris:percorso» scrive nel riservato finto, altrimenti nel pubblico finto."""
        if rel.startswith("ris:"):
            return self.scrivi_ris(rel[4:], contenuto)
        return scrivi(self.pub, rel, contenuto)

    def pulisci_pub(self):
        for p in getattr(self, "scritti_ris", []):
            try:
                os.remove(p)
            except OSError:
                pass
        self.scritti_ris = []
        subprocess.run(["git", "-C", self.pub, "checkout", "-q", "--", "."], capture_output=True)
        subprocess.run(["git", "-C", self.pub, "clean", "-fdq", "-e", "strumenti"], capture_output=True)
        subprocess.run(["git", "-C", self.pub, "reset", "-q", "--hard", "origin/main"], capture_output=True)
        try:
            os.remove(self.pub + "/.git/ultimo-pubblicato")
        except OSError:
            pass
        for f in glob.glob(self.ris + "/dati/verifiche-lezione/*"):
            os.remove(f)

    def nuovo_id(self):
        self.n += 1
        return "c%d" % self.n


# ------------------------------------------------------------------ canale: messaggio (hook Stop)

def _trascrizione(percorso, turni):
    n = [0]
    righe = []
    for t in turni:
        n[0] += 1
        righe.append({"type": "user", "uuid": "u%d" % n[0], "origin": {"kind": "human"}, "message": {"content": t.get("docente", "")}})
        for b in t.get("blocchi", []):
            n[0] += 1
            if b[0] == "T":
                righe.append({"type": "assistant", "uuid": "a%d" % n[0], "message": {"content": [{"type": "text", "text": b[1]}]}})
            else:
                righe.append({"type": "assistant", "uuid": "b%d" % n[0], "message": {"content": [
                    {"type": "tool_use", "id": "t%d" % n[0], "name": b[1], "input": b[2]}]}})
                righe.append({"type": "user", "uuid": "r%d" % n[0], "message": {"content": [
                    {"type": "tool_result", "tool_use_id": "t%d" % n[0], "content": "ok"}]}})
    with open(percorso, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def run_messaggio(inp, fx):
    os.environ["CORSO_STATO_FORMATO"] = ""
    os.environ["CORSO_STATO_BUON_SENSO"] = ""   # v1.2: nessuna memoria dei messaggi tra un caso e l'altro
    for rel, contenuto in (inp.get("ris_files") or {}).items():   # v1.2: file nel riservato finto (modalità assenza ecc.)
        fx.scrivi_ris(rel, contenuto)
    cm = carica("controllo-messaggio.py", HOOKS)
    cm.PUB, cm.RIS = fx.pub, fx.ris
    cm.STATO_FORMATO = None
    adesso = datetime.datetime.now(TZ)
    for v in inp.get("verifiche", []):
        ora = adesso - datetime.timedelta(minutes=v.get("minuti_fa", 1))
        json.dump({"ora": ora.isoformat(), "esito": v.get("esito", "VERDE"), "riga": v.get("riga", "")},
                  open("%s/dati/verifiche-lezione/%s_%s.json" % (fx.ris, adesso.strftime("%Y-%m-%d"), v["classe"]), "w"))
    if inp.get("pub_sporco"):
        scrivi(fx.pub, "docs/1inf/index.html", "<p>modificata e non pushata</p>")
    if inp.get("pubblicato"):   # timbro di aspetta_pubblicazione.sh: le pagine pushate risultano PUBBLICATE
        gd = subprocess.run(["git", "-C", fx.pub, "rev-parse", "--absolute-git-dir"], capture_output=True, text=True).stdout.strip()
        head = subprocess.run(["git", "-C", fx.pub, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        open(gd + "/ultimo-pubblicato", "w").write(head)
    if inp.get("firme"):
        scrivi(fx.pub, "FIRME-REGISTRO-2026-27.md", inp["firme"].replace("{{OGGI}}", adesso.strftime("%d/%m/%Y")))
    raw = json.dumps(inp, ensure_ascii=False)
    for k in (1, 2, 3, 5, 10, 30, 60):
        raw = raw.replace("{{ORA-%d}}" % k, (adesso - datetime.timedelta(minutes=k)).strftime("%H:%M"))
    inp = json.loads(raw.replace("{{ORA}}", adesso.strftime("%H:%M")))
    if "finale" not in inp:   # il messaggio finale è l'ultimo blocco di testo dell'ultimo turno
        inp["finale"] = [b[1] for b in (inp.get("turni") or [{}])[-1].get("blocchi", []) if b[0] == "T"][-1]
    tr = fx.t + "/tr.jsonl"
    turni = inp.get("turni") or [{"docente": inp.get("docente", "ok"), "blocchi": []}]
    _trascrizione(tr, turni)
    stdin = json.dumps({"last_assistant_message": inp["finale"], "transcript_path": tr}, ensure_ascii=False)
    sys.stdin = io.StringIO(stdin)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        cm.main()
    sys.stdin = sys.__stdin__
    return _esito_hook(out.getvalue())


def _esito_hook(testo):
    testo = testo.strip()
    if not testo:
        return None
    d = json.loads(testo)
    if d.get("decision") == "block":
        return ("blocca", d.get("reason", ""))
    if d.get("systemMessage"):
        return ("avviso", d["systemMessage"])
    return None


# ------------------------------------------------------------------ canale: comando (hook PreToolUse)

def run_comando(inp, fx):
    lc = carica("limite-comandi.py", HOOKS)
    lc.PUB, lc.RIS = fx.pub, fx.ris
    for rel, contenuto in (inp.get("files") or {}).items():
        fx.scrivi_in(rel, contenuto)
    cwd = fx.ris if inp.get("cwd") == "ris" else fx.pub
    sessione = "banco-" + fx.nuovo_id()
    prompt = "p-" + sessione
    out = io.StringIO()
    for k in range(int(inp.get("precedenti", 0)) + 1):
        ultimo = k == int(inp.get("precedenti", 0))
        d = {"tool_name": "Bash", "tool_input": {"command": inp["cmd"] if ultimo else "ls"}, "cwd": cwd,
             "session_id": sessione, "scratchpad_dir": fx.t, "prompt_id": prompt, "tool_use_id": "id%d" % k}
        if not inp.get("principale"):
            d["agent_id"] = "a1"
        sys.stdin = io.StringIO(json.dumps(d))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            lc.main()
    sys.stdin = sys.__stdin__
    t = out.getvalue().strip()
    if t and "deny" in t:
        return ("blocca", json.loads(t)["hookSpecificOutput"]["permissionDecisionReason"])
    return None


# ------------------------------------------------------------------ canale: pagina

def run_pagina(inp, fx):
    cp = fx.cp
    radice = fx.t + "/radice-" + fx.nuovo_id()
    for rel, contenuto in (inp.get("files") or {}).items():
        scrivi(radice, rel, contenuto)
    prob = cp.controlla(inp["percorso"], inp["testo"], controlli=cp.TUTTI, radice=radice)
    return ("blocca", "; ".join(prob)) if prob else None


# ------------------------------------------------------------------ canale: kit (riservato/strumenti/controlla_kit.py)

def _prepara_file(base, files):
    for nome, spec in (files or {}).items():
        p = os.path.join(base, nome)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        if isinstance(spec, dict) and "pdf" in spec:
            crea_pdf(p, spec["pdf"])
        elif isinstance(spec, dict) and spec.get("docx"):
            with open(p, "wb") as f:
                f.write(b"PK\x03\x04finto")
        else:
            with open(p, "w", encoding="utf-8") as f:
                f.write(spec if isinstance(spec, str) else "")


def run_kit(inp, fx):
    cartella = os.path.join(RIS, "strumenti")
    if not os.path.exists(os.path.join(cartella, "controlla_kit.py")):
        raise RuntimeError("controlla_kit.py non c'è nel riservato")
    ck = carica("controlla_kit.py", cartella)
    base = fx.t + "/kit-" + fx.nuovo_id()
    os.makedirs(base)
    _prepara_file(base, inp.get("files"))
    kit = os.path.join(base, "kit.md")
    with open(kit, "w", encoding="utf-8") as f:
        f.write(inp["kit"].replace("{{TMP}}", base))
    ore, manca = ck.controlla(kit)
    return ("blocca", " | ".join(manca)) if manca else None


# ------------------------------------------------------------------ canale: pdf (controlla_pdf_ragazzi.py)

def run_pdf(inp, fx):
    mod = carica("controlla_pdf_ragazzi.py", STR)
    base = fx.t + "/pdf-" + fx.nuovo_id()
    p = os.path.join(base, inp["nome"])
    crea_pdf(p, inp["pagine"])
    gravi, avvisi = mod.controlla(p)
    return ("blocca", "; ".join(gravi + avvisi)) if (gravi or avvisi) else None


# ------------------------------------------------------------------ canale: leggibilita

def run_leggibilita(inp, fx):
    mod = carica("controlla_leggibilita.py", STR)
    base = fx.t + "/leg-" + fx.nuovo_id()
    p = scrivi(base, inp.get("nome", "dispensa.md"), inp["testo"])
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = mod.main([p] + list(inp.get("opzioni", [])))
    t = out.getvalue()
    righe = [r.strip() for r in t.splitlines() if "[GRAVE]" in r or "[AVVISO]" in r]
    return ("blocca" if rc == 1 else "avviso", " | ".join(righe)) if righe else None


# ------------------------------------------------------------------ canale: post (titolo e testo del post Classroom)

def run_post(inp, fx):
    lib = carica("controlli_consegna.py", STR)
    kw = {k: inp[k] for k in ("ora", "data_kit", "testo_sezione", "quiz_in_sezione", "pdf_testo") if k in inp}
    if "data_kit" in kw:
        kw["data_kit"] = tuple(kw["data_kit"])
    prob = lib.problemi_post(inp.get("titolo", ""), inp.get("oggetto", ""), **kw)
    return ("blocca", "; ".join(prob)) if prob else None


def run_cruscotto(inp, fx):
    lib = carica("controlli_consegna.py", STR)
    base = fx.t + "/cru-" + fx.nuovo_id()
    for rel, contenuto in (inp.get("files") or {}).items():
        scrivi(base, rel, contenuto)
    p = lib.cruscotto_senza_dati_di_oggi(inp["classe"], inp["oggi"], base)
    return ("blocca", p) if p else None


def run_budget(inp, fx):
    mod = carica("controlla_budget_1inf.py", STR)
    s = mod.sospetti_nel_testo(inp["testo"], set(inp["ammessi"]))
    return ("blocca", str(s)) if s else None


def run_quiz_lingue(inp, fx):
    base = fx.t + "/ql-" + fx.nuovo_id()
    os.makedirs(base + "/strumenti")
    shutil.copy(os.path.join(STR, "controlla_lingue_quiz.py"), base + "/strumenti/controlla_lingue_quiz.py")
    import base64
    indice = {"lavori": []}
    for q in inp["quiz"]:
        nome = q["id"] + ".txt"
        scrivi(base, "fabbrica/" + nome, base64.b64encode(json.dumps(q["dati"], ensure_ascii=False).encode()).decode())
        indice["lavori"].append({"id": q["id"], "file": nome})
    scrivi(base, "fabbrica/indice.json", json.dumps(indice))
    r = subprocess.run([sys.executable, "-I", base + "/strumenti/controlla_lingue_quiz.py"], capture_output=True, text=True, timeout=60)
    return ("blocca", r.stdout.strip()) if r.returncode != 0 else None


def run_audit_regole(inp, fx):
    cartella = os.path.join(RIS, "generatori")
    if not os.path.exists(os.path.join(cartella, "audit_regole.py")):
        raise RuntimeError("audit_regole.py non c'è nel riservato")
    sys.path.insert(0, cartella)
    mod = carica("audit_regole.py", cartella)
    mod.RIS, mod.PUB = fx.ris, fx.pub
    for rel, contenuto in (inp.get("files") or {}).items():
        fx.scrivi_in(rel, contenuto)
    out = getattr(mod, inp["funzione"])(inp["giorno"])
    return ("blocca", "; ".join(out)) if out else None


def run_fine_giornata(inp, fx):
    cc = carica("controlla_controlli.py", STR)
    for rel, contenuto in (inp.get("files") or {}).items():
        fx.scrivi_in(rel, contenuto)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        if inp.get("funzione") == "firme_sospette":
            prob = cc.firme_sospette(inp["giorno"], fx.pub)
        else:
            prob = cc.controlla_fine_giornata(inp["giorno"], fx.pub, fx.ris)
    return ("blocca", "; ".join(prob)) if prob else None


def run_bobina(inp, fx):
    mod = carica("bobina-automatica.py", HOOKS)
    pulito = mod.pulisci_segreti(inp["testo"])
    # scatta se la pulizia ha tolto qualcosa dal testo che finirebbe nella bobina (e il segreto non c'è più)
    return ("blocca", "segreto rimosso dalla bobina") if (pulito != inp["testo"] and inp.get("segreto", "") not in pulito) else None


CANALI = {"messaggio": run_messaggio, "comando": run_comando, "pagina": run_pagina, "kit": run_kit, "pdf": run_pdf,
          "leggibilita": run_leggibilita, "post": run_post, "cruscotto": run_cruscotto, "budget": run_budget,
          "quiz_lingue": run_quiz_lingue,
          "audit_regole": run_audit_regole, "fine_giornata": run_fine_giornata, "bobina": run_bobina}


# ------------------------------------------------------------------ esecuzione dei casi

def _scatta(esito, atteso):
    """True se il controllo ha scattato (e, se c'è una regex attesa, per il motivo giusto)."""
    if esito is None:
        return False
    if atteso:
        return bool(re.search(atteso, esito[1], re.I | re.S))
    return True


def _giusto_scatta(esito, atteso, canale):
    """Sul caso GIUSTO nessun controllo deve scattare. Per messaggio e comando qualunque blocco è un falso allarme;
    per gli altri canali (che stampano problemi non legati al caso) conta solo il motivo atteso."""
    if esito is None:
        return False
    if _scatta(esito, atteso):
        return True
    return canale in ("messaggio", "comando") and esito[0] == "blocca"


def esegui_prova(prova, fx):
    fn = CANALI[prova["canale"]]
    atteso = prova.get("atteso")
    ris = {"canale": prova["canale"]}
    for ruolo in ("sbagliato", "giusto"):
        fx.pulisci_pub()
        e = fn(prova[ruolo], fx)
        ris[ruolo] = {"scatta": _scatta(e, atteso) if ruolo == "sbagliato" else _giusto_scatta(e, atteso, prova["canale"]),
                      "tipo": e[0] if e else None, "motivo": (e[1][:220] if e else "")}
    fx.pulisci_pub()
    return ris


def esegui_caso(caso, fx):
    prove = caso.get("prove") or [{k: caso[k] for k in ("canale", "atteso", "sbagliato", "giusto") if k in caso}]
    risultati, errori = [], []
    for p in prove:
        try:
            risultati.append(esegui_prova(p, fx))
        except Exception as e:   # il banco non decide mai «coperto» se non riesce a girare
            errori.append("%s: %s" % (p.get("canale"), "".join(traceback.format_exception_only(type(e), e)).strip()[:200]))
    coperte = [r for r in risultati if r["sbagliato"]["scatta"]]
    pulite = [r for r in coperte if not r["giusto"]["scatta"]]
    if coperte:
        stato = COPERTO
    elif errori and not risultati:
        stato = ERR
    else:
        stato = NON_COPERTO
    falso_allarme = bool(coperte) and not pulite
    solo_avviso = stato == COPERTO and all(r["sbagliato"]["tipo"] == "avviso" for r in (pulite or coperte))
    scelta = (pulite or coperte or risultati or [{}])[0]
    return {"stato": stato, "falso_allarme_sul_giusto": falso_allarme, "solo_avviso": solo_avviso, "errori_banco": errori,
            "canali": [r["canale"] for r in risultati],
            "controllo_che_scatta": scelta.get("canale") if coperte else None,
            "motivo_sbagliato": scelta.get("sbagliato", {}).get("motivo", "") if coperte else "",
            # un controllo può scattare sul sbagliato per un ALTRO motivo: non conta come copertura, ma si dice
            "scatta_per_altro_motivo": "" if coperte else " | ".join(r["sbagliato"]["motivo"][:160] for r in risultati if r["sbagliato"]["motivo"])}


def carica_dati():
    indice = json.load(open(os.path.join(DATI, "indice.json"), encoding="utf-8"))
    casi = {}
    for f in sorted(glob.glob(os.path.join(DATI, "casi", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        casi[d["errore"]] = d
    return indice, casi


def giro(solo=None):
    indice, casi = carica_dati()
    fx = Banco()
    risultati = []
    try:
        for voce in indice:
            if solo and voce["errore"] not in solo:
                continue
            r = {"errore": voce["errore"], "titolo": voce["titolo"], "categoria": voce["categoria"], "schema": voce.get("schema"),
                 "mappa_ora": voce.get("mappa_ora"), "ripete": voce.get("ripete", False)}
            caso = casi.get(voce["errore"])
            if caso:
                r.update(esegui_caso(caso, fx))
                r["controllo_atteso"] = caso.get("controllo_atteso", "")
                r["origine_input"] = caso.get("origine_input", "")
            elif voce.get("da_scrivere"):
                r.update({"stato": DA_SCRIVERE, "motivo": voce["da_scrivere"]})
            else:
                r.update({"stato": NON_VERIF, "motivo": voce.get("non_verificabile") or "motivo non scritto (da completare in indice.json)"})
            risultati.append(r)
    finally:
        shutil.rmtree(fx.t, ignore_errors=True)
    return risultati


# ------------------------------------------------------------------ rapporto

def chiave_importanza(r):
    cat = CATEGORIE.get(r["categoria"], ("", 0, 99))
    m = re.match(r"#(\d+)", r["errore"])
    n = int(m.group(1)) if m else -1
    return (-cat[1], cat[2], 0 if r.get("ripete") else 1, -n)


STATI = (COPERTO, NON_COPERTO, DA_SCRIVERE, NON_VERIF, ERR)


def conteggi(risultati):
    out = {}
    for r in risultati:
        c = out.setdefault(r["categoria"], {s: 0 for s in STATI})
        c[r["stato"]] += 1
    return out


def _t(s, n):
    return (s or "").replace("|", "/").replace("\n", " ")[:n]


def rapporto_md(risultati, specifiche, adesso):
    tot = {s: sum(1 for r in risultati if r["stato"] == s) for s in STATI}
    nc = sorted([r for r in risultati if r["stato"] == NON_COPERTO], key=chiave_importanza)
    con_caso = tot[COPERTO] + tot[NON_COPERTO] + tot[ERR]
    a_ma_no = [r for r in nc if r.get("mappa_ora") == "A"]
    db_ma_si = [r for r in risultati if r["stato"] == COPERTO and r.get("mappa_ora") in ("B", "D")]
    L = ["# Banco di prova degli errori: rapporto", "",
         "**Versione 1.0** — %s — documento riservato del docente · generato da `strumenti/banco_errori_v1.0.py` (repository pubblico) · "
         "dati in `tests/errori/` (repository pubblico, senza cognomi di allievi)" % adesso.strftime("%d/%m/%Y"), "",
         "## 1 Esito in breve", ""]
    L.append("- Errori nel banco: **%d** (tutte le voci della MAPPA-REGOLE-CONTROLLI.md e del REGISTRO-ERRORI-CLAUDE.md: #1-#389 più le voci del 01/10 e del 02/10; "
             "l'audit ne contava 364: qui ci sono anche le voci #171-#222 che la MAPPA non ha)." % len(risultati))
    L.append("- **COPERTO (il controllo scatta): %d.**" % tot[COPERTO])
    L.append("- **NON COPERTO (nessun controllo lo fermerebbe): %d.**" % tot[NON_COPERTO])
    L.append("- **CASO DA SCRIVERE (verificabile, ma il caso del banco non è ancora scritto): %d.**" % tot[DA_SCRIVERE])
    L.append("- **NON VERIFICABILE A MACCHINA (con il motivo): %d.**" % tot[NON_VERIF])
    L.append("- Casi non eseguibili (ERRORE DEL BANCO): %d. Casi scritti, ciascuno con input sbagliato e input giusto: **%d**." % (tot[ERR], con_caso))
    L.append("- Tra i COPERTI: %d scattano solo come avviso che non blocca; %d hanno un falso allarme sul caso giusto." % (
        sum(1 for r in risultati if r.get("solo_avviso")), sum(1 for r in risultati if r.get("falso_allarme_sul_giusto"))))
    L.append("- **Divergenza con la MAPPA:** %d errori che la MAPPA dichiara con copertura «A» (controllo automatico attivo) NON scattano più al banco "
             "(per lo più controlli dell'hook tolti il 04/11/2026); %d errori che la MAPPA dichiara «B» o «D» sono invece COPERTI da un controllo nato dopo." % (
                 len(a_ma_no), len(db_ma_si)))
    L += ["", "Un NON COPERTO è un buco: se l'errore si ripresentasse domani, nessuno strumento lo fermerebbe. Non è mai «atteso»: "
          "per ognuno c'è un input che si può scrivere e un controllo che si può costruire.", "",
          "**Che cosa vuol dire e che cosa no.** COPERTO = il controllo vero scatta sull'input sbagliato ricostruito dal registro e NON scatta sull'input giusto, "
          "in un repository finto; non prova che scatti su ogni variante del testo. Gli input non sono i messaggi originali (il registro non li conserva alla lettera): "
          "sono rifatti dalla descrizione dell'errore, anonimizzati, con nomi inventati. La categoria dell'audit è assegnata da me per ogni voce (l'audit non "
          "pubblica la classificazione voce per voce): è una scelta soggettiva, non verificata da un secondo lettore. "
          "Il banco non modifica nessun controllo e non tocca Classroom, Drive o i repository veri.", "",
          "## 2 Conteggi per categoria dell'audit", "",
          "| Categoria | Indice audit | Voci | COPERTO | NON COPERTO | DA SCRIVERE | NON VERIFICABILE | Errore banco |", "|---|---|---|---|---|---|---|---|"]
    c = conteggi(risultati)
    for cod, (nome, ind, pos) in sorted(CATEGORIE.items(), key=lambda x: x[1][2]):
        if cod in c:
            v = c[cod]
            L.append("| %s %s | %s | %d | %d | %d | %d | %d | %d |" % (cod, nome, ind or "n.d.", sum(v.values()), v[COPERTO], v[NON_COPERTO], v[DA_SCRIVERE], v[NON_VERIF], v[ERR]))
    L.append("| **Totale** | | %d | %d | %d | %d | %d | %d |" % (len(risultati), tot[COPERTO], tot[NON_COPERTO], tot[DA_SCRIVERE], tot[NON_VERIF], tot[ERR]))
    L += ["", "L'indice è quello dell'audit (sezione 6: I = (2F + C + V) × G × (1 + R)); X, A e O non hanno un indice nell'audit.", "",
          "## 3 Errori NON COPERTI, in ordine di importanza", "",
          "Ordine: indice dell'audit della categoria (le TOP 10 per prime), poi gli errori ripetuti, poi i più recenti. "
          "«MAPPA» = copertura che la MAPPA dichiarava (A automatico, B passo notturno, C superata, D scoperta, «-» voce non presente nella MAPPA). "
          "«Perché» = che cosa manca (controllo tolto o mai costruito).", "",
          "| # | Errore | Cat. | MAPPA | Titolo | Perché nessun controllo lo ferma |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(nc, 1):
        altro = (" Scatta un controllo, ma per un altro motivo." if r.get("scatta_per_altro_motivo") else "")
        L.append("| %d | %s | %s | %s | %s | %s |" % (i, r["errore"], r["categoria"], r.get("mappa_ora") or "-", _t(r["titolo"], 90), _t(r.get("controllo_atteso", ""), 150) + altro))
    L += ["", "### 3b Errori che la MAPPA dichiara con copertura «A» e che non scattano più", "",
          "Elenco (è lo stesso insieme della tabella sopra, filtrato): %s." % (", ".join(r["errore"] for r in a_ma_no) or "nessuno"), "",
          "Causa più frequente: il 04/11/2026 l'hook controllo-messaggio.py è stato ridotto (28 controlli tolti, 5 tenuti; CLAUDE.md v2.0, LEGGIMI-controlli.md capitolo 05) "
          "e la MAPPA non è stata riallineata. La MAPPA va corretta o i controlli ripristinati: oggi la MAPPA promette una copertura che non c'è.", "",
          "## 4 Il controllo più piccolo che coprirebbe i primi 10 NON COPERTI", "",
          "Sono specifiche, non implementazioni: le costruirà l'integratore. Ogni specifica dice dove va il controllo, che cosa cerca e quale caso del banco passa da "
          "NON COPERTO a COPERTO.", ""]
    for r in nc[:10]:
        L += _blocco_specifica(r, specifiche)
    L += ["## 5 Un controllo per ognuna delle categorie TOP 10", "",
          "Per ogni categoria, il controllo unico più piccolo che coprirebbe il maggior numero dei suoi NON COPERTI.", ""]
    for cod in sorted([k for k, v in CATEGORIE.items() if v[1]], key=lambda k: CATEGORIE[k][2]):
        elenco = [r["errore"] for r in nc if r["categoria"] == cod]
        L.append("### %s %s (indice %d): %d NON COPERTI" % (cod, CATEGORIE[cod][0], CATEGORIE[cod][1], len(elenco)))
        L.append("")
        L.append(specifiche.get("categoria:" + cod, "Specifica non scritta."))
        L.append("")
        if elenco:
            L.append("Casi del banco che diventerebbero COPERTI: %s." % ", ".join(elenco))
            L.append("")
    L += ["## 6 Errori COPERTI: dove scatta il controllo", "",
          "| Errore | Cat. | MAPPA | Controllo che scatta | Nota |", "|---|---|---|---|---|"]
    for r in sorted([r for r in risultati if r["stato"] == COPERTO], key=chiave_importanza):
        nota = []
        if r.get("solo_avviso"):
            nota.append("solo avviso, non blocca")
        if r.get("falso_allarme_sul_giusto"):
            nota.append("FALSO ALLARME sul caso giusto")
        L.append("| %s | %s | %s | %s | %s |" % (r["errore"], r["categoria"], r.get("mappa_ora") or "-", _t(r.get("controllo_atteso", ""), 130), "; ".join(nota)))
    errs = [r for r in risultati if r["stato"] == ERR]
    n = 7
    if errs:
        L += ["", "## %d Casi non eseguibili (ERRORE DEL BANCO)" % n, ""]
        n += 1
        for r in errs:
            L.append("- %s: %s" % (r["errore"], "; ".join(r.get("errori_banco", []))))
    L += ["", "## %d Errori verificabili ma con il caso ancora da scrivere" % n, "",
          "| Errore | Cat. | Titolo | Che cosa serve per scrivere il caso |", "|---|---|---|---|"]
    n += 1
    for r in sorted([r for r in risultati if r["stato"] == DA_SCRIVERE], key=chiave_importanza):
        L.append("| %s | %s | %s | %s |" % (r["errore"], r["categoria"], _t(r["titolo"], 90), _t(r.get("motivo", ""), 260)))
    L += ["", "## %d Errori NON VERIFICABILI A MACCHINA, con il motivo" % n, "",
          "Il motivo è scritto per ogni voce in `tests/errori/indice.json`: errori di giudizio didattico, che avvengono in aula, che dipendono da servizi esterni "
          "non raggiungibili da un test, regole superate, oppure rimedi che stanno nel codice di un generatore.", "",
          "| Errore | Cat. | Titolo | Motivo |", "|---|---|---|---|"]
    n += 1
    for r in sorted([r for r in risultati if r["stato"] == NON_VERIF], key=chiave_importanza):
        L.append("| %s | %s | %s | %s |" % (r["errore"], r["categoria"], _t(r["titolo"], 90), _t(r.get("motivo", ""), 200)))
    L += ["", "## %d Limiti di questo rapporto" % n, "",
          "- Gli input sbagliati sono ricostruiti dalla descrizione del registro, non sono i messaggi originali; una variante diversa dello stesso errore potrebbe non essere fermata anche quando il caso è COPERTO.",
          "- La categoria di ogni voce è assegnata da me (non è nell'audit voce per voce) e la marca «ripete» è un'euristica sul titolo («ripete», «ancora», «di nuovo», «terza volta»): servono solo a ordinare.",
          "- Il banco chiama i controlli veri su repository finti. Non prova che gli hook siano registrati nelle impostazioni di Claude Code (lo fa controlla_controlli.py) né i controlli che richiedono Classroom, Moduli, Drive, DIDAweb, Veyon o GitHub Pages dal vivo.",
          "- I controlli delle altre sessioni (controllo-messaggio.py, controlla_kit.py, controlli_consegna.py, controlla_controlli.py) sono quelli presenti sul disco al momento del giro; se cambiano, un caso può cambiare stato: con --regressioni il banco lo dice.", ""]
    n += 1
    L += ["", "## %d Come si usa" % n, "",
          "- `python3 /home/user/corso-informatica/strumenti/banco_errori_v1.0.py -v` stampa lo stato di ogni errore.",
          "- `... --regressioni` esce 1 se un errore prima COPERTO non scatta più o se un controllo scatta sul caso giusto (da lanciare prima di toccare un hook).",
          "- `... --solo \"#50,#386\"` esegue pochi casi; `--json FILE` e `--md FILE` scrivono i risultati.",
          "- Un errore nuovo: si aggiunge un file in `tests/errori/casi/` (e la riga in `indice.json`) PRIMA di costruire il controllo; il caso nasce NON COPERTO e il controllo lo porta a COPERTO.", "",
          "## Changelog", "",
          "- v1.0 (%s): prima versione. %d voci, %d casi scritti, %d COPERTI, %d NON COPERTI." % (adesso.strftime("%d/%m/%Y"), len(risultati), con_caso, tot[COPERTO], tot[NON_COPERTO])]
    return "\n".join(L) + "\n"


def _blocco_specifica(r, specifiche):
    s = specifiche.get(r["errore"])
    out = ["### %s (cat. %s): %s" % (r["errore"], r["categoria"], _t(r["titolo"], 130)), ""]
    out.append(s if s else "Specifica non ancora scritta.")
    out.append("")
    return out


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description="Banco di prova degli errori (vedi la docstring).")
    ap.add_argument("--solo", help="errori separati da virgola, per esempio «#50,#63»")
    ap.add_argument("--json", help="scrive i risultati in un file JSON")
    ap.add_argument("--md", help="scrive il rapporto in Markdown")
    ap.add_argument("--regressioni", action="store_true", help="esce 1 se un errore prima COPERTO non scatta più")
    ap.add_argument("--aggiorna-baseline", action="store_true", help="riscrive tests/errori/baseline-coperti.json")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    solo = set(x.strip() for x in a.solo.split(",")) if a.solo else None
    risultati = giro(solo)
    adesso = datetime.datetime.now(TZ)
    if a.json:
        json.dump({"generato": adesso.isoformat(), "risultati": risultati}, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if a.md:
        sp = {}
        f = os.path.join(DATI, "specifiche-v1.0.json")
        if os.path.exists(f):
            sp = json.load(open(f, encoding="utf-8"))
        open(a.md, "w", encoding="utf-8").write(rapporto_md(risultati, sp, adesso))
    tot = {s: sum(1 for r in risultati if r["stato"] == s) for s in STATI}
    if a.verbose:
        for r in sorted(risultati, key=chiave_importanza):
            print("%-12s %-27s %s %s" % (r["errore"], r["stato"], r["categoria"], r["titolo"][:70]))
    print("BANCO ERRORI: %d errori | COPERTI %d | NON COPERTI %d | CASI DA SCRIVERE %d | NON VERIFICABILI %d | ERRORE DEL BANCO %d" % (
        len(risultati), tot[COPERTO], tot[NON_COPERTO], tot[DA_SCRIVERE], tot[NON_VERIF], tot[ERR]))
    base_f = os.path.join(DATI, "baseline-coperti.json")
    rc = 1 if tot[ERR] else 0
    if a.aggiorna_baseline and not solo:
        json.dump(sorted(r["errore"] for r in risultati if r["stato"] == COPERTO and not r.get("falso_allarme_sul_giusto")),
                  open(base_f, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print("baseline aggiornata: %s" % base_f)
    if a.regressioni and os.path.exists(base_f):
        prima = set(json.load(open(base_f, encoding="utf-8")))
        per = {r["errore"]: r for r in risultati}
        for e in sorted(prima):
            r = per.get(e)
            if r is None:
                continue
            if r["stato"] != COPERTO:
                print("REGRESSIONE: %s non scatta più (%s)" % (e, r["stato"]))
                rc = 1
            elif r.get("falso_allarme_sul_giusto"):
                print("REGRESSIONE: %s scatta anche sul caso giusto (falso allarme)" % e)
                rc = 1
    for r in risultati:
        if r["stato"] == ERR:
            print("ERRORE DEL BANCO %s: %s" % (r["errore"], "; ".join(r.get("errori_banco", []))))
    return rc


if __name__ == "__main__":
    sys.exit(main())
