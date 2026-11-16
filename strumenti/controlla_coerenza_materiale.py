#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllo di COERENZA del materiale di lunedi 16/11/2026 (3INF ore 1-3, 2INF ore 4-6). Versione 1.0, 16/11/2026.
Nato da un errore (principio di CLAUDE.md: un errore nuovo corregge uno strumento): dispense, Documenti semplificati, pacchetti Classroom,
modelli di Documento e pagine del sito dicevano cose diverse (nome del repository, «ultimo commit» o «sito» in cima al Documento, numero di
screenshot, pagine della dispensa v1.1 mentre su Classroom c'era la v1.0).

Che cosa controlla (tabella elemento x documento; ogni riga dice OK, ERRORE o ATTENZIONE):
  01 versioni   l'ultima dispensa/semplificato/«Come compilo»/«Come aggiorno» (MD) ha il PDF nel sito (italiano e PC 14), il PDF si apre,
                pacchetto e pagine (docs/lunedi/index.html, link.html) citano QUELLA versione e nessuna piu' vecchia; l'intestazione del MD = nome del file
  02 screenshot  modello .md, pacchetto, dispensa («FAI LO SCREENSHOT k di N» e «Screenshot k:»), semplificato, pagina: stesso numero per ora (2, 3, 4)
  03 file        elenco dei file del Documento: modello, pacchetto, dispensa, semplificato, pagina
  04 cima        «Nome e cognome» + «URL del repository» + «URL del sito» (formati https://github.com/NOMEUTENTE/NOMEREPO e https://NOMEUTENTE.github.io/NOMEREPO/);
                niente «Ultimo commit» richiesto come indirizzo; stessa frase in modello, pacchetto, dispensa, semplificato, pagina, «Come compilo»
  05 repository nessun testo fisso «repository `sito-personale`»; la regola «usi quello che hai gia', non lo rinomini» c'e' in dispensa e semplificato;
                il cruscotto di lezione non chiede di ricreare il repository a chi lavora in un altro
  06 semplificati rimandi per CAPITOLO (mai «pagina N»), ogni capitolo citato esiste in TUTTE le versioni della dispensa; font >= 11 px e pagine (file JSON del generatore)
  07 quiz        link del Moduli identico in spec, pacchetto, pagine, KIT-INDICE; fabbrica/indice.json e file del quiz esistono, il titolo del quiz ha l'ora giusta
  08 titoli/orari titolo Classroom, testo per il registro e orario di ogni ora uguali in pacchetto, pagine, TITOLI, kit indice, dispensa
  09 date        l'inizio dello stage e' 23/11/2026 dappertutto
  10 link        ogni file linkato da index.html e link.html esiste e i PDF si aprono
  11 2INF        titoli, quiz, orari, repository `il-mio-sito`, 1 screenshot per ora; il Documento 2INF chiede «repository + ultimo commit» (decisione 14/11): coerente
                tra le dispense, e diverso dalla 3INF (segnalato come ATTENZIONE)
Uscita: 0 se nessun ERRORE; 1 altrimenti. Uso:
  python3 strumenti/controlla_coerenza_materiale.py [--riservato DIR] [--pubblico DIR] [--md] [--prova]
  --prova  esegue le prove dello strumento su materiale finto (deve trovare gli errori messi apposta)."""
import argparse, base64, glob, json, os, re, subprocess, sys

QUI = os.path.dirname(os.path.abspath(__file__))
PUB0 = os.path.dirname(QUI)
RIS0 = "/home/user/corso-informatica-riservato"
REPORT = "report/2026-11-16"
DISPENSE = "docs/dispense/lunedi"
PAGINE = ["docs/lunedi/index.html", "docs/lunedi/link.html"]

# famiglie di documenti (nome base dei file MD nel riservato, cartella report/2026-11-16)
DISP = {1: "DISPENSA-3INF-LUN-ORA1-SITO", 2: "DISPENSA-3INF-LUN-ORA2-STILE", 3: "DISPENSA-3INF-LUN-ORA3-DIARIO"}
PUBN = {1: "3inf-ora1-dispensa", 2: "3inf-ora2-dispensa", 3: "3inf-ora3-dispensa"}
COMPILO = ("DISPENSA-3INF-COME-COMPILO-IL-DOCUMENTO", "3inf-come-compilo-il-documento")
AGGIORNO = ("DISPENSA-3INF-STAGE-COME-AGGIORNO-DIARIO", "3inf-ora3-stage-come-aggiorno-diario")
SEMPL = {n: ("DOCUMENTO-3INF-ORA%d-SEMPLIFICATO" % n, "3inf-ora%d-semplificato" % n) for n in (1, 2, 3)}
PACC = {n: "PACCHETTO-CLASSROOM-3INF-LUN-ORA%d" % n for n in (1, 2, 3)}
PACC2 = {n: "PACCHETTO-CLASSROOM-2INF-LUN-ORA%d" % n for n in (4, 5, 6)}
DISP2 = {4: "DISPENSA-2INF-LUN-ORA4-CHI-SONO", 5: "DISPENSA-2INF-LUN-ORA5-TRE-PAGINE", 6: "DISPENSA-2INF-LUN-ORA6-STILE-E-QUALCOSA-DI-MIO"}


class Mat:
    """accesso al materiale: dal disco (reale) o da un dizionario {percorso relativo: testo} (prove). Percorsi: 'R/...' riservato, 'P/...' pubblico."""
    def __init__(self, ris=None, pub=None, finto=None):
        self.ris, self.pub, self.finto = ris, pub, finto
        self.cache = {}

    def _p(self, rel):
        base, resto = rel.split("/", 1)
        return os.path.join(self.ris if base == "R" else self.pub, resto)

    def esiste(self, rel):
        return (rel in self.finto) if self.finto is not None else os.path.exists(self._p(rel))

    def testo(self, rel):
        if rel in self.cache: return self.cache[rel]
        if self.finto is not None: t = self.finto.get(rel, "")
        else:
            try: t = open(self._p(rel), encoding="utf-8").read()
            except Exception: t = ""
        self.cache[rel] = t
        return t

    def elenco(self, cartella_rel):
        if self.finto is not None:
            pre = cartella_rel.rstrip("/") + "/"
            return sorted(k[len(pre):] for k in self.finto if k.startswith(pre) and "/" not in k[len(pre):])
        try: return sorted(os.listdir(self._p(cartella_rel)))
        except Exception: return []

    def pdf_ok(self, rel):
        if self.finto is not None: return self.finto.get(rel) not in (None, "ROTTO")
        p = self._p(rel)
        if not os.path.exists(p): return False
        try:
            r = subprocess.run(["pdfinfo", p], capture_output=True, text=True, timeout=30)
            return r.returncode == 0 and "Pages:" in r.stdout
        except FileNotFoundError:
            return open(p, "rb").read(5) == b"%PDF-"

    def versioni(self, cartella_rel, base, ext="md", sep="."):
        """[(maj, min, nome file)] dei file base-vX.Y.ext (non PC14, a meno che base lo contenga)"""
        r = re.compile(r"^%s-v(\d+)%s(\d+)\.%s$" % (re.escape(base), re.escape(sep), ext))
        out = []
        for f in self.elenco(cartella_rel):
            m = r.match(f)
            if m: out.append((int(m.group(1)), int(m.group(2)), f))
        return sorted(out)

    def ultimo(self, cartella_rel, base, ext="md", sep="."):
        v = self.versioni(cartella_rel, base, ext, sep)
        return v[-1] if v else None


class Esiti:
    def __init__(self): self.righe = []
    def ok(self, ch, det): self.righe.append(("OK", ch, det))
    def err(self, ch, det): self.righe.append(("ERRORE", ch, det))
    def att(self, ch, det): self.righe.append(("ATTENZIONE", ch, det))
    def verifica(self, cond, ch, det_ok, det_err):
        (self.ok if cond else self.err)(ch, det_ok if cond else det_err)
        return cond
    @property
    def errori(self): return [r for r in self.righe if r[0] == "ERRORE"]


def carica_spec(mat):
    rel = "P/strumenti/coerenza_materiale_spec.json"
    t = mat.testo(rel)
    return json.loads(t)


def blocco(t, intestazione):
    """primo blocco ``` che segue la riga che comincia con 'intestazione' (testo vuoto se manca)"""
    i = t.find(intestazione)
    if i < 0: return ""
    a = t.find("```\n", i)
    if a < 0: return ""
    a += 4; b = t.find("\n```", a)
    return t[a:b]


def pul(t):
    """toglie i commenti <!-- ... --> (note per il docente: non vanno nel PDF)"""
    return re.sub(r"<!--.*?-->", "", t, flags=re.S)


def titolo_pacchetto(t):
    """riquadro che segue la riga «Titolo...:» (anche «Titolo (invariato rispetto alla v1.2):»)"""
    m = re.search(r"^Titolo[^\n]*:\n\n```\n(.*?)\n```", t, re.M | re.S)
    return m.group(1).strip() if m else ""


def vtxt(t): return "%d.%d" % (t[0], t[1])
def vpub(t): return "%d-%d" % (t[0], t[1])


# ============================================================ 01 versioni
def c01_versioni(mat, spec, E):
    R = "R/" + REPORT
    fam = []   # (etichetta, base MD, base PDF pubblico, ora o None)
    for n in (1, 2, 3):
        fam.append(("dispensa ora %d" % n, DISP[n], PUBN[n], n))
        fam.append(("semplificato ora %d" % n, SEMPL[n][0], SEMPL[n][1], n))
    fam.append(("come compilo", COMPILO[0], COMPILO[1], None))
    fam.append(("come aggiorno il diario", AGGIORNO[0], AGGIORNO[1], None))
    pagine = {p: mat.testo("P/" + p) for p in PAGINE}
    for et, base, pubb, n in fam:
        for pc in (False, True):
            b = base + ("-PC14" if pc else "")
            u = mat.ultimo(R, b)
            nome = et + (" PC 14" if pc else "")
            if not u:
                E.err("01 versioni", "%s: nessun MD trovato (%s-vX.Y.md)" % (nome, b)); continue
            testo = mat.testo(R + "/" + u[2])
            m = re.search(r"\*\*Versione (\d+)\.(\d+)\*\*", testo)
            E.verifica(bool(m) and (int(m.group(1)), int(m.group(2))) == (u[0], u[1]), "01 versioni",
                       "%s: intestazione = nome del file (v%s)" % (nome, vtxt(u)), "%s: l'intestazione del MD non dice v%s" % (nome, vtxt(u)))
            nomepdf = "%s%s-v%s.pdf" % (pubb, "-pc14" if pc else "", vpub(u))
            E.verifica(mat.pdf_ok("P/%s/%s" % (DISPENSE, nomepdf)), "01 versioni", "%s: PDF nel sito %s si apre" % (nome, nomepdf), "%s: manca o non si apre il PDF %s nel sito" % (nome, nomepdf))
            for p, s in pagine.items():
                # la pagina cita il PDF della versione piu' recente e nessuna piu' vecchia della stessa famiglia
                presenti = re.findall(r"%s%s-v(\d+)-(\d+)\.pdf" % (re.escape(pubb), "-pc14" if pc else r"(?!-pc14)"), s)
                if not presenti: E.err("01 versioni", "%s: %s non cita nessun PDF di «%s»" % (nome, p, pubb)); continue
                vecchie = sorted({(int(a), int(c)) for a, c in presenti if (int(a), int(c)) != (u[0], u[1])})
                if vecchie or (str(u[0]), str(u[1])) not in set(presenti):
                    E.err("01 versioni", "%s: %s cita %s, l'ultima e' v%s" % (nome, p, ", ".join("v%d.%d" % v for v in sorted({(int(a), int(c)) for a, c in presenti})), vtxt(u)))
                else:
                    E.ok("01 versioni", "%s: %s cita v%s" % (nome, p, vtxt(u)))
    # pacchetti: citano i PDF dell'ultima versione (dispensa ora N) e nessuno piu' vecchio
    for n in (1, 2, 3):
        pk = mat.ultimo(R, PACC[n])
        ud = mat.ultimo(R, DISP[n])
        if not pk or not ud: continue
        t = mat.testo(R + "/" + pk[2])
        cit = re.findall(r"ora%d-(?:sito|stile|diario)(?:-pc14)?[-_]v(\d+)\.(\d+)\.pdf|Ora%d-(?:Sito|Stile|Diario)(?:-PC14)?_v(\d+)\.(\d+)\.pdf|ora%d-dispensa(?:-pc14)?-v(\d+)-(\d+)\.pdf" % (n, n, n), t)
        vs = set()
        for g in cit:
            a = [x for x in g if x != ""]
            if len(a) == 2: vs.add((int(a[0]), int(a[1])))
        E.verifica(vs == {(ud[0], ud[1])}, "01 versioni", "pacchetto ora %d (v%s) cita solo la dispensa v%s" % (n, vtxt(pk), vtxt(ud)),
                   "pacchetto ora %d (v%s) cita le dispense %s, l'ultima e' v%s" % (n, vtxt(pk), sorted("v%d.%d" % v for v in vs) or "nessuna", vtxt(ud)))
    # modelli: la pagina cita l'ultimo modello .docx per ogni ora
    for n in (1, 2, 3, 0):
        base = "3inf-modello-documento-ora%d" % n if n else "3inf-modello-documento-complessivo"
        u = mat.ultimo("P/" + DISPENSE + "/modelli", base, ext="docx", sep="-")
        if not u: E.err("01 versioni", "modello di Documento %s: nessun .docx" % base); continue
        for p in PAGINE:
            s = mat.testo("P/" + p)
            cit = {(int(a), int(c)) for a, c in re.findall(re.escape(base) + r"-v(\d+)-(\d+)\.docx", s)}
            E.verifica(cit == {(u[0], u[1])}, "01 versioni", "%s cita %s v%s" % (p, base, vpub(u)),
                       "%s cita %s %s, l'ultimo e' v%s" % (p, base, sorted("v%d-%d" % v for v in cit) or "nessuno", vpub(u)))


# ============================================================ 02 screenshot, 03 file, 04 cima, 05 repository
def modello_md(mat, n):
    base = "3inf-modello-documento-ora%d" % n if n else "3inf-modello-documento-complessivo"
    u = mat.ultimo("P/" + DISPENSE + "/modelli", base, ext="md", sep="-")
    return (u, mat.testo("P/%s/modelli/%s" % (DISPENSE, u[2]))) if u else (None, "")


def c02_03_04_ore(mat, spec, E):
    R = "R/" + REPORT
    for n in (1, 2, 3):
        S = spec["3INF"]["ore"][str(n)]; ns = S["screenshot"]; files = S["file"]; tag = "ora %d" % n
        # --- modello
        u, mt = modello_md(mat, n)
        if not u: E.err("02 screenshot", "modello ora %d: nessun .md" % n)
        else:
            k = len(re.findall(r"^### Screenshot \d+", mt, re.M))
            E.verifica(k == ns, "02 screenshot", "modello %s v%s: %d" % (tag, vpub(u), ns), "modello %s v%s: %d slot, spec %d" % (tag, vpub(u), k, ns))
            f = re.findall(r"^### ([\w.]+\.(?:html|css|js|md))\s*$", mt, re.M)
            E.verifica(f == files, "03 file", "modello %s: file = spec" % tag, "modello %s: file %s, spec %s" % (tag, f, files))
            ok4 = all(x in mt for x in spec["cima_documento"]) and "Ultimo commit" not in mt and not re.search(r"^Repository:", mt, re.M)
            E.verifica(ok4, "04 cima", "modello %s: nome e cognome + URL repository + URL sito" % tag, "modello %s: cima del Documento diversa da «Nome e cognome / URL del repository / URL del sito» (o c'e' ancora «Ultimo commit»/«Repository:»)" % tag)
        # --- pacchetto
        pk = mat.ultimo(R, PACC[n])
        if pk:
            t = mat.testo(R + "/" + pk[2]); con = blocco(t, "Testo della consegna"); ogg = blocco(t, "Oggetto:")
            m = re.search(r"(\d+) screenshot", con)
            E.verifica(bool(m) and int(m.group(1)) == ns, "02 screenshot", "pacchetto %s v%s: %d (consegna)" % (tag, vtxt(pk), ns), "pacchetto %s v%s: la consegna dice %s screenshot, spec %d" % (tag, vtxt(pk), m.group(1) if m else "?", ns))
            m = re.search(r"il codice dei file ([^;]+);", con)
            fl = [x.strip() for x in m.group(1).split(",")] if m else []
            E.verifica(fl == files, "03 file", "pacchetto %s: file = spec" % tag, "pacchetto %s: file %s, spec %s" % (tag, fl, files))
            E.verifica("il tuo nome e cognome e i 2 URL" in con and "l'URL del repository e l'URL del sito" in con and "ultimo commit" not in con.lower(), "04 cima",
                       "pacchetto %s: consegna = nome, cognome, URL repository, URL sito" % tag, "pacchetto %s: la consegna non dice «nome e cognome e i 2 URL: repository e sito» (o cita l'ultimo commit)" % tag)
            E.verifica("nome, cognome e i 2 URL" in ogg, "04 cima", "pacchetto %s: oggetto dice nome, cognome e 2 URL" % tag, "pacchetto %s: l'oggetto non dice «nome, cognome e i 2 URL»" % tag)
            E.verifica(titolo_pacchetto(t) == S["titolo"], "08 titoli", "pacchetto %s: riquadro del titolo = «%s»" % (tag, S["titolo"]), "pacchetto %s: il riquadro «Titolo» non e' «%s»" % (tag, S["titolo"]))
            E.verifica(("ora %d (%s)" % (n, S["orario"])) in t.split("\n")[0], "08 titoli", "pacchetto %s: orario %s" % (tag, S["orario"]), "pacchetto %s: l'intestazione non dice ora %d (%s)" % (tag, n, S["orario"]))
            if n == 1: E.verifica("mio-sito" in con and "sito-personale" in con, "05 repository", "pacchetto ora 1: la consegna dice mio-sito / sito-personale", "pacchetto ora 1: la consegna non dice la regola del repository")
        else: E.err("02 screenshot", "pacchetto ora %d: nessun MD" % n)
        # --- dispensa (ultima)
        for pc in (False, True):
            ud = mat.ultimo(R, DISP[n] + ("-PC14" if pc else ""))
            if not ud: continue
            t = pul(mat.testo(R + "/" + ud[2])); et = "dispensa %s v%s%s" % (tag, vtxt(ud), " PC 14" if pc else "")
            tot = {int(x) for x in re.findall(r"FAI LO SCREENSHOT \d+ di (\d+)", t)}
            cnt = len(set(re.findall(r"FAI LO SCREENSHOT (\d+) di", t)))
            E.verifica(tot == {ns} and cnt == ns, "02 screenshot", "%s: «FAI LO SCREENSHOT k di %d» x%d" % (et, ns, ns), "%s: riquadri rossi %d con totali %s, spec %d" % (et, cnt, sorted(tot), ns))
            didascalie = len(re.findall(r"^Screenshot \d+: ", t, re.M))
            E.verifica(didascalie == ns, "02 screenshot", "%s: %d righe «Screenshot k:»" % (et, ns), "%s: %d righe «Screenshot k:», spec %d" % (et, didascalie, ns))
            m = re.search(r"Fai lo stesso per ogni file: ([^\n]+?)\.\n", t)
            fl = re.findall(r"`([^`]+)`", m.group(1)) if m else []
            E.verifica(fl == files, "03 file", "%s: file del Documento = spec" % et, "%s: file %s, spec %s" % (et, fl, files))
            cima = ("`Nome e cognome:`" in t and "`URL del repository:`" in t and "`URL del sito:`" in t and "https://github.com/NOMEUTENTE/NOMEREPO" in t and "https://NOMEUTENTE.github.io/NOMEREPO/" in t)
            vecchio = bool(re.search(r"Ultimo commit:`|vicino a `Repository:`|indirizzo dell'ultimo commit", t))
            E.verifica(cima and not vecchio, "04 cima", "%s: nome e cognome, URL repository, URL sito (formati giusti)" % et, "%s: la parte «In cima» non e' quella nuova (manca un campo o un formato, o c'e' ancora «ultimo commit»)" % et)
            # 05: nessun testo fisso con sito-personale
            fissi = re.findall(r"(?:tuo repository `sito-personale`|github\.com/NOMEUTENTE/sito-personale|URL del repository: https://github\.com/[^\s`]*sito-personale)", t)
            E.verifica(not fissi, "05 repository", "%s: nessun testo con il repository fisso sito-personale" % et, "%s: ha il repository fisso `sito-personale` in %d punti" % (et, len(fissi)))
            frase = "NON lo rinomini" if n == 1 else "Non lo rinomini"
            E.verifica(frase in t, "05 repository", "%s: dice di non rinominare il repository" % et, "%s: manca la regola «usi il repository che hai gia', non lo rinomini»" % et)
            E.verifica(("Apri il compito «%s»" % S["titolo"]) in t, "08 titoli", "%s: cita il compito «%s»" % (et, S["titolo"]), "%s: non cita il compito «%s»" % (et, S["titolo"]))
            E.verifica("Il Documento è vuoto?" in t and "il tuo Documento" in t and "«Ora %d · Il mio documento»" % n not in t, "04 cima", "%s: non cita il Documento per nome e dice cosa fare se e' vuoto" % et, "%s: cita ancora il Documento per nome o non dice cosa fare se e' vuoto" % et)
            if n == 3: E.verifica("`presenze.html`" in t.split("Devono esserci questi file:")[1].split("\n")[0] if "Devono esserci questi file:" in t else False, "03 file", "%s: elenco dei file del repository con presenze.html" % et, "%s: l'elenco «Devono esserci questi file» non ha presenze.html" % et)
        # --- semplificato (ultimo)
        for pc in (False, True):
            us = mat.ultimo(R, SEMPL[n][0] + ("-PC14" if pc else ""))
            if not us: E.err("02 screenshot", "semplificato ora %d%s: nessun MD" % (n, " PC 14" if pc else "")); continue
            t = pul(mat.testo(R + "/" + us[2])); et = "semplificato %s v%s%s" % (tag, vtxt(us), " PC 14" if pc else "")
            tot = {int(x) for x in re.findall(r"FAI LO SCREENSHOT \d+ di (\d+)", t)}; cnt = len(set(re.findall(r"FAI LO SCREENSHOT (\d+) di", t)))
            E.verifica(tot == {ns} and cnt == ns, "02 screenshot", "%s: %d riquadri" % (et, ns), "%s: riquadri %d totali %s, spec %d" % (et, cnt, sorted(tot), ns))
            m = re.search(r"il codice dei (\d+) file", t)
            E.verifica(bool(m) and int(m.group(1)) == len(files), "03 file", "%s: il codice dei %d file" % (et, len(files)), "%s: dice «il codice dei %s file», spec %d" % (et, m.group(1) if m else "?", len(files)))
            if n > 1:
                m = re.search(r"I file sono almeno ([^\n]+?)\.\n", t)
                fl = [x.strip() for x in m.group(1).split(",")] if m else []
                E.verifica(fl[:len(files)] == [x for x in files] or set(files) <= set(fl), "03 file", "%s: elenco file del repository comprende i file del Documento" % et, "%s: file %s, spec %s" % (et, fl, files))
            lines = [l for l in t.split("\n") if l.startswith("`URL del repository:") or l.startswith("`URL del sito:")]
            E.verifica(len(lines) >= 2 and all(("NOMEUTENTE/NOMEREPO" in l or "NOMEUTENTE.github.io/NOMEREPO/" in l) for l in lines) and "`Nome e cognome:" in t, "04 cima", "%s: form con nome e cognome + 2 URL nei formati giusti" % et, "%s: il riquadro «I miei 2 indirizzi» non ha i formati giusti" % et)
            E.verifica("non lo hai rinominato" in t, "05 repository", "%s: «non lo hai rinominato»" % et, "%s: manca il controllo «il repository ha il nome che avevi gia'»" % et)
            E.verifica(not re.search(r"github\.com/NOMEUTENTE/sito-personale|Il repository si chiama sito-personale", t), "05 repository", "%s: nessun repository fisso" % et, "%s: ha il repository fisso sito-personale" % et)
        # --- pagina (consegna e oggetto)
        for p in PAGINE:
            s = mat.testo("P/" + p)
            if p.endswith("index.html"):
                m = re.search(r'id="3inf-ora%d-con">(.*?)</div>' % n, s, re.S)
                con = (m.group(1) if m else "").replace("&#x27;", "'")
                mm = re.search(r"(\d+) screenshot", con)
                E.verifica(bool(mm) and int(mm.group(1)) == ns, "02 screenshot", "%s ora %d: testo della consegna con %d screenshot" % (p, n, ns), "%s ora %d: la consegna dice %s screenshot, spec %d" % (p, n, mm.group(1) if mm else "?", ns))
                m2 = re.search(r"il codice dei file ([^;]+);", con); fl = [x.strip() for x in m2.group(1).split(",")] if m2 else []
                E.verifica(fl == files, "03 file", "%s ora %d: file = spec" % (p, n), "%s ora %d: file %s, spec %s" % (p, n, fl, files))
                E.verifica("il tuo nome e cognome e i 2 URL" in con and "ultimo commit" not in con.lower(), "04 cima", "%s ora %d: consegna con nome, cognome e 2 URL" % (p, n), "%s ora %d: la consegna non e' quella nuova (nome, cognome, 2 URL) o cita l'ultimo commit" % (p, n))


def c04_compilo(mat, spec, E):
    R = "R/" + REPORT
    for pc in (False, True):
        u = mat.ultimo(R, COMPILO[0] + ("-PC14" if pc else ""))
        if not u: continue
        t = pul(mat.testo(R + "/" + u[2])); et = "«Come compilo il Documento» v%s%s" % (vtxt(u), " PC 14" if pc else "")
        ok = ("`Nome e cognome:`" in t and "`URL del repository:`" in t and "`URL del sito:`" in t and "URL del repository: `https://github.com/NOMEUTENTE/NOMEREPO`" in t
              and "URL del sito: `https://NOMEUTENTE.github.io/NOMEREPO/`" in t and "Ultimo commit" not in t and "sito-personale" not in t)
        E.verifica(ok, "04 cima", "%s: nome e cognome, URL repository, URL sito, esempio con NOMEREPO" % et, "%s: ha ancora «Ultimo commit» o sito-personale, o manca un campo" % et)
    u = mat.ultimo(R, AGGIORNO[0])
    if u:
        t = pul(mat.testo(R + "/" + u[2]))
        E.verifica("Premi `sito-personale`" not in t and "il nome del tuo repository" in t, "05 repository", "«Come aggiorno il diario» v%s: il repository si sceglie con il suo nome" % vtxt(u), "«Come aggiorno il diario» v%s: dice «Premi `sito-personale`»" % vtxt(u))
    # modello complessivo e consegna complessiva
    mu, mt = modello_md(mat, 0)
    if mu:
        E.verifica(all(x in mt for x in spec["cima_documento"]), "04 cima", "modello complessivo v%s: nome e cognome + 2 URL" % vpub(mu), "modello complessivo v%s: manca nome e cognome o un URL in cima" % vpub(mu))
    pk = mat.ultimo(R, "PACCHETTO-CLASSROOM-3INF-LUN-COMPLESSIVO")
    if pk:
        con = blocco(mat.testo(R + "/" + pk[2]), "Testo della consegna")
        E.verifica("il tuo nome e cognome e i 2 URL" in con, "04 cima", "pacchetto complessivo v%s: consegna con nome, cognome e 2 URL" % vtxt(pk), "pacchetto complessivo v%s: la consegna non dice nome, cognome e 2 URL" % vtxt(pk))


# ============================================================ 05 cruscotto
def c05_cruscotto(mat, spec, E):
    t = mat.testo("R/generatori/cruscotto_lezione.py")
    if not t:
        E.att("05 repository", "generatori/cruscotto_lezione.py non trovato: non controllato"); return
    E.verifica("chiedi al docente se va bene o se creare" not in t, "05 repository", "cruscotto di lezione: non chiede di ricreare il repository a chi ne usa un altro",
               "cruscotto di lezione: dice a chi lavora in un altro repository «chiedi al docente se va bene o se creare sito-personale» (contraddice la regola)")
    E.verifica('cfg["repo"], f)' not in t, "05 repository", "cruscotto di lezione: gli URL delle pagine usano il repository vero dell'allievo",
               "cruscotto di lezione: gli URL delle pagine usano sempre il repository fisso della classe")


# ============================================================ 06 semplificati
def titoli_capitoli(testo):
    return [re.sub(r"\s+", " ", m.group(1)).strip() for m in re.finditer(r"^#{2,3} (.+)$", testo, re.M)]


def c06_semplificati(mat, spec, E, ris_report="R/" + REPORT):
    R = ris_report
    for n in (1, 2, 3):
        for pc in (False, True):
            us = mat.ultimo(R, SEMPL[n][0] + ("-PC14" if pc else ""))
            if not us: continue
            t = pul(mat.testo(R + "/" + us[2])); et = "semplificato ora %d v%s%s" % (n, vtxt(us), " PC 14" if pc else "")
            pag = re.findall(r"(?:\bpagin[ae]\s+\d|\bpagine\s+\d|পৃষ্ঠা\s*[\d০-৯])", t)
            E.verifica(not pag, "06 semplificati", "%s: nessun rimando a numeri di pagina" % et, "%s: rimanda a pagine (%s): rompe se la dispensa cambia versione" % (et, pag[:3]))
            if pc: continue
            # i capitoli citati esistono in TUTTE le versioni della dispensa citata
            for m in re.finditer(r"Dispensa Ora (\d),? ((?:capitol[oi]|«)[^.]*?)(?:\.|$)", t, re.M):
                ora_d = int(m.group(1)); resto = m.group(2)
                cit = re.findall(r"(\d+) · ([A-Za-zÀ-ÿ« »'’]+?)(?:,| e |\.|$|\s*\()", resto + ".")
                virg = re.findall(r"«([^»]+)»", resto)
                date = {tuple(int(x) for x in v.split(".")) for v in spec["versioni_date"][str(ora_d)]}
                for ver in mat.versioni(R, DISP[ora_d]):
                    if (ver[0], ver[1]) not in date: continue
                    th = titoli_capitoli(pul(mat.testo(R + "/" + ver[2])))
                    for num, tit in cit:
                        tit = tit.strip().strip("«»").strip()
                        trovato = any(h.startswith("%s · %s" % (num, tit[:10])) for h in th)
                        if not trovato: E.err("06 semplificati", "%s: cita «capitolo %s · %s» che non c'e' nella dispensa ora %d v%s" % (et, num, tit, ora_d, vtxt(ver)))
                    for v in virg:
                        if not any(v[:12] in h for h in th) and not v.startswith("Come compilo"):
                            E.err("06 semplificati", "%s: cita «%s» che non c'e' nella dispensa ora %d v%s" % (et, v, ora_d, vtxt(ver)))
    # font e pagine: file JSON scritto dal generatore (report/.../pdf-ragazzi/semplificati-vX.Y-font.json)
    for n in (1, 2, 3):
        for pc in (False, True):
            us = mat.ultimo(R, SEMPL[n][0] + ("-PC14" if pc else ""))
            if not us: continue
            v = vtxt(us)
            jf = mat.testo(R + "/pdf-ragazzi/semplificati-v%s-font.json" % v)
            nome = "3inf-ora%d-semplificato%s-v%s.pdf" % (n, "-pc14" if pc else "", v)
            et = "semplificato ora %d v%s%s" % (n, v, " PC 14" if pc else "")
            if not jf: E.err("06 semplificati", "%s: manca semplificati-v%s-font.json (font e pagine non verificabili)" % (et, v)); continue
            d = json.loads(jf).get(nome)
            if not d: E.err("06 semplificati", "%s: %s non e' nel file dei font" % (et, nome)); continue
            mx = spec["pagine_max_semplificato"][str(n)][1 if pc else 0]
            E.verifica(d["font_px"] >= spec["font_min_px"] and d["pagine"] <= mx, "06 semplificati", "%s: font %s px (min %d), %d pagine (max %d)" % (et, d["font_px"], spec["font_min_px"], d["pagine"], mx),
                       "%s: font %s px (min %d) o pagine %d (max %d) fuori misura" % (et, d["font_px"], spec["font_min_px"], d["pagine"], mx))
            E.verifica(mat.pdf_ok(R + "/pdf-ragazzi/" + nome), "06 semplificati", "%s: PDF si apre" % et, "%s: PDF mancante o rotto" % et)


# ============================================================ 07 quiz, 08 titoli/orari, 09 date, 10 link
def c07_quiz(mat, spec, E):
    R = "R/" + REPORT
    indice = mat.testo("P/fabbrica/indice.json")
    try: ids = {l["id"]: l["file"] for l in json.loads(indice)["lavori"]} if indice else {}
    except Exception: ids = {}
    kit = mat.ultimo(R, "KIT-LUNEDI-INDICE")
    kt = mat.testo(R + "/" + kit[2]) if kit else ""
    tutte = [("3INF", n, spec["3INF"]["ore"][str(n)]) for n in (1, 2, 3)] + [("2INF", n, spec["2INF"]["ore"][str(n)]) for n in (4, 5, 6)]
    for cl, n, S in tutte:
        q = S["quiz"]
        fonti = {}
        pk = mat.ultimo(R, (PACC if cl == "3INF" else PACC2)[n])
        fonti["pacchetto v%s" % (vtxt(pk) if pk else "?")] = mat.testo(R + "/" + pk[2]) if pk else ""
        for p in PAGINE: fonti[p] = mat.testo("P/" + p)
        fonti["KIT-LUNEDI-INDICE"] = kt
        for nome, t in fonti.items():
            if not t: E.err("07 quiz", "%s: documento non trovato (quiz ora %d)" % (nome, n)); continue
            if nome.endswith("index.html"):
                # nella sezione dell'ora tutti i link «viewform» devono essere quello giusto
                m = re.search(r'<section id="%s-ora%d">(.*?)</section>' % (cl.lower(), n), t, re.S)
                urls = set(re.findall(r"https://docs\.google\.com/forms/d/e/[\w-]+/viewform", m.group(1))) if m else set()
                E.verifica(urls == {q}, "07 quiz", "%s: tutti i link del quiz ora %d = spec" % (nome, n), "%s: nella sezione ora %d i link del quiz sono %s, spec %s" % (nome, n, sorted(u[-12:] for u in urls) or "nessuno", q[-20:]))
                continue
            E.verifica(q in t, "07 quiz", "%s: link del quiz ora %d = spec" % (nome, n), "%s: manca il link del quiz ora %d (%s...)" % (nome, n, q[40:64]))
        fid = ids.get(S["quiz_id"])
        E.verifica(bool(fid) and mat.esiste("P/fabbrica/" + fid), "07 quiz", "fabbrica/indice.json: %s -> %s esiste" % (S["quiz_id"], fid), "fabbrica/indice.json: %s manca o il file non esiste" % S["quiz_id"])
        if fid and mat.esiste("P/fabbrica/" + fid):
            try:
                d = json.loads(base64.b64decode(mat.testo("P/fabbrica/" + fid).strip()).decode("utf-8"))
                tit = d.get("titolo", "")
                E.verifica(("Ora %d" % n) in tit and cl in tit, "07 quiz", "quiz %s: titolo «%s» ha l'ora e la classe giuste" % (S["quiz_id"], tit), "quiz %s: il titolo «%s» non dice Ora %d e %s" % (S["quiz_id"], tit, n, cl))
            except Exception:
                E.att("07 quiz", "quiz %s: file non decodificabile (formato diverso): titolo non controllato" % S["quiz_id"])


def c08_titoli_orari(mat, spec, E):
    R = "R/" + REPORT
    tit3 = mat.ultimo(R, "TITOLI-3INF-LUNEDI"); tit2 = mat.ultimo(R, "TITOLI-2INF-LUNEDI")
    kit = mat.ultimo(R, "KIT-LUNEDI-INDICE")
    kt = mat.testo(R + "/" + kit[2]) if kit else ""
    docs = [("TITOLI 3INF", mat.testo(R + "/" + tit3[2]) if tit3 else "")] + [("TITOLI 2INF", mat.testo(R + "/" + tit2[2]) if tit2 else "")]
    for cl in ("3INF", "2INF"):
        for ns, S in spec[cl]["ore"].items():
            n = int(ns)
            for nome, t in docs:
                if nome.endswith(cl):
                    E.verifica(S["titolo"] in t and S["registro"] in t, "08 titoli", "%s: titolo e registro ora %d" % (nome, n), "%s: manca titolo «%s» o registro «%s» (ora %d)" % (nome, S["titolo"], S["registro"], n))
            E.verifica(S["titolo"] in kt and S["registro"] in kt, "08 titoli", "KIT-LUNEDI-INDICE: titolo e registro ora %d" % n, "KIT-LUNEDI-INDICE: manca titolo o registro ora %d" % n)
            s = mat.testo("P/docs/lunedi/index.html")
            E.verifica(S["titolo"] in s and S["registro"] in s, "08 titoli", "docs/lunedi/index.html: titolo e registro ora %d" % n, "docs/lunedi/index.html: manca titolo «%s» o registro ora %d" % (S["titolo"], n))
            sez = re.search(r"%s, ora %d \(([\d-]+)\)" % (cl, n), mat.testo("P/docs/lunedi/index.html"))
            E.verifica(bool(sez) and sez.group(1) == S["orario"], "08 orari", "index.html: %s ora %d = %s" % (cl, n, S["orario"]), "index.html: %s ora %d ha orario %s, spec %s" % (cl, n, sez.group(1) if sez else "?", S["orario"]))
    # dispense: ogni «Apri il compito «...»» nella dispensa 3INF e' il titolo giusto (fatto in c02_03_04); date
    pass


def c09_date(mat, spec, E):
    R = "R/" + REPORT; ini = spec["stage_inizio"]
    for n in (3,):
        for pc in (False, True):
            u = mat.ultimo(R, DISP[n] + ("-PC14" if pc else ""))
            if not u: continue
            t = mat.testo(R + "/" + u[2])
            altre = {d for d in re.findall(r"Primo giorno dello stage: (?:luned[iì] )?(\d\d/\d\d/\d{4})", t)}
            E.verifica(altre == {ini}, "09 date", "dispensa ora 3 v%s%s: primo giorno dello stage %s" % (vtxt(u), " PC 14" if pc else "", ini), "dispensa ora 3 v%s: date del primo giorno %s, spec %s" % (vtxt(u), sorted(altre), ini))
    for p in PAGINE:
        s = mat.testo("P/" + p)
        trov = set(re.findall(r"stage comincia(?: il)? (\d+ \w+|\d\d/\d\d/\d{4})", s))
        ok = trov <= {"23 novembre", ini}
        E.verifica(ok, "09 date", "%s: l'inizio dello stage e' il 23 novembre" % p, "%s: date dello stage diverse: %s" % (p, sorted(trov)))


def c10_link(mat, spec, E):
    for p in PAGINE:
        s = mat.testo("P/" + p)
        if not s: E.err("10 link", "%s: pagina non trovata" % p); continue
        hrefs = set(re.findall(r'href="([^"#]+)"', s)) | set(re.findall(r'download="([^"]+)"', s))
        manc = []; pdf_rotti = []
        for h in sorted(hrefs):
            if h.startswith("http") or h.startswith("mailto:") or h in ("link.html", "index.html"): continue
            if "/" not in h and not h.endswith((".pdf", ".docx", ".md", ".zip", ".gs")): continue
            if "/" not in h: continue   # attributo download="nome" senza percorso
            rel = os.path.normpath(os.path.join(os.path.dirname(p), h)).replace("\\", "/")
            if not mat.esiste("P/" + rel): manc.append(h)
            elif h.endswith(".pdf") and not mat.pdf_ok("P/" + rel): pdf_rotti.append(h)
        E.verifica(not manc and not pdf_rotti, "10 link", "%s: tutti i file linkati esistono e i PDF si aprono (%d link)" % (p, len(hrefs)), "%s: file mancanti %s, PDF che non si aprono %s" % (p, manc[:4], pdf_rotti[:4]))


# ============================================================ 11 2INF
def c11_2inf(mat, spec, E):
    R = "R/" + REPORT; repo = spec["repo"]["2inf"]
    for n in (4, 5, 6):
        S = spec["2INF"]["ore"][str(n)]
        pk = mat.ultimo(R, PACC2[n])
        if pk:
            t = mat.testo(R + "/" + pk[2]); tp = t.split("## 01")[-1].split("## 02")[0]   # solo il pacchetto vero (capitolo 01)
            E.verifica(S["titolo"] in t and ("ora %d (%s)" % (n, S["orario"])) in t.split("\n")[0], "11 2INF", "pacchetto ora %d: titolo e orario %s" % (n, S["orario"]), "pacchetto ora %d: titolo o orario %s mancano" % (n, S["orario"]))
        ud = mat.ultimo(R, DISP2[n])
        if ud:
            t = mat.testo(R + "/" + ud[2])
            k = len(set(re.findall(r"FAI LO SCREENSHOT (\d+) di (\d+)", t)))
            tot = {int(b) for a, b in re.findall(r"FAI LO SCREENSHOT (\d+) di (\d+)", t)}
            E.verifica(tot == {S["screenshot"]} and k == S["screenshot"], "11 2INF", "dispensa ora %d: %d screenshot" % (n, S["screenshot"]), "dispensa ora %d: screenshot %s/%d, spec %d" % (n, sorted(tot), k, S["screenshot"]))
            # dal 16/11 (lavagna del docente): repository mio-sito per tutti, URL uniformi, in cima al Documento nome, cognome, URL repository, URL sito
            E.verifica(all(x in t for x in spec["cima_documento"]) and "Ultimo commit" not in t and "ultimo commit, cioè" not in t, "11 2INF", "dispensa ora %d: cima del Documento (nome, cognome, URL repository, URL sito)" % n, "dispensa ora %d: cima del Documento non uguale alla 3INF" % n)
            E.verifica(repo in t and "il-mio-sito" not in t and "sito-personale" not in t and "https://github.com/NOMEUTENTE/%s" % repo in t and "https://NOMEUTENTE.github.io/%s/" % repo in t, "11 2INF", "dispensa ora %d: repository %s e URL uniformi" % (n, repo), "dispensa ora %d: repository diverso da %s o URL non uniformi" % (n, repo))
        if pk:
            E.verifica("il-mio-sito" not in tp and "sito-personale" not in tp and (repo in tp), "11 2INF", "pacchetto ora %d: repository %s" % (n, repo), "pacchetto ora %d: repository diverso da %s" % (n, repo))
    E.att("11 2INF", "Regola della lavagna 16/11: repository mio-sito per tutti (2INF), cima del Documento come la 3INF (nome, cognome, URL repository, URL sito); la 3INF resta «ognuno il suo repository»")


# ============================================================ 12 intestazioni delle versioni (R11)
def c12_intestazioni(mat, spec, E):
    R = "R/" + REPORT
    tutti = [f for f in mat.elenco(R) if f.endswith(".md")]
    for base in list(DISP.values()) + [COMPILO[0], AGGIORNO[0]] + [SEMPL[n][0] for n in (1, 2, 3)] + list(PACC.values()) + ["MODELLI-DOCUMENTO-3INF", "PIANO-LEZIONE-3INF-LUNEDI", "KIT-LUNEDI-INDICE"]:
        u = mat.ultimo(R, base)
        if not u: E.err("12 versioni", "%s: nessun MD" % base); continue
        t = mat.testo(R + "/" + u[2])
        m = re.search(r"\*\*Versione (\d+)\.(\d+)\*\*", t)
        E.verifica(bool(m) and (int(m.group(1)), int(m.group(2))) == (u[0], u[1]), "12 versioni", "%s v%s: intestazione = file" % (base, vtxt(u)), "%s: ultima v%s ma l'intestazione dice %s" % (base, vtxt(u), m.group(0) if m else "niente"))


def controlla(mat):
    spec = carica_spec(mat)
    E = Esiti()
    for f in (c01_versioni, c02_03_04_ore, c04_compilo, c05_cruscotto, c06_semplificati, c07_quiz, c08_titoli_orari, c09_date, c10_link, c11_2inf, c12_intestazioni):
        f(mat, spec, E)
    return E


def stampa(E, md=False):
    if md:
        print("| esito | controllo | dettaglio |\n|---|---|---|")
        for s, c, d in E.righe: print("| %s | %s | %s |" % (s, c, d.replace("|", "/")))
    else:
        for s, c, d in E.righe:
            if s != "OK": print("%-10s %-16s %s" % (s, c, d))
    n = {k: sum(1 for r in E.righe if r[0] == k) for k in ("OK", "ERRORE", "ATTENZIONE")}
    print("Coerenza materiale 16/11/2026: %d OK, %d ERRORE, %d ATTENZIONE" % (n["OK"], n["ERRORE"], n["ATTENZIONE"]))


def main():
    ap = argparse.ArgumentParser(description="Controllo di coerenza del materiale di lunedi 16/11/2026")
    ap.add_argument("--riservato", default=os.environ.get("RISERVATO", RIS0)); ap.add_argument("--pubblico", default=PUB0)
    ap.add_argument("--md", action="store_true", help="stampa tutte le righe come tabella markdown"); ap.add_argument("--prova", action="store_true")
    a = ap.parse_args()
    if a.prova:
        import prova_controlla_coerenza_materiale as P
        return P.main()
    if not os.path.isdir(a.riservato):
        print("ERRORE: repository riservato non trovato (%s): senza non si controllano dispense e pacchetti" % a.riservato); return 2
    E = controlla(Mat(a.riservato, a.pubblico))
    stampa(E, a.md)
    return 1 if E.errori else 0


if __name__ == "__main__":
    sys.exit(main())
