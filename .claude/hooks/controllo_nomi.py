#!/usr/bin/env python3
"""Controllo dei nomi degli allievi nel repository PUBBLICO (regola R1 di CLAUDE.md, 04/11/2026).

Nel pubblico i ragazzi compaiono solo come «Nome I.» (nome e iniziale) o in dati cifrati.
Questo modulo cerca i COGNOMI (e le coppie cognome-nome) presi dagli elenchi del riservato:
1. config/*presenti*.json e config/*elenco*.json (voci «COGNOME NOME»);
2. config/nomi-controllo.json, campo «nomi» (nomi in più) e campo facoltativo «parole_comuni»
   (cognomi che sono anche parole comuni e danno falsi allarmi: non si cercano).

Lo usano:
1. limite-comandi.py, prima di un «git commit» del pubblico (testo del comando, cioè il messaggio
   del commit, e il file di -F) e prima di un «git push» del pubblico (messaggi dei commit da pushare);
2. il hook git «commit-msg» del pubblico (strumenti/installa_commit_msg.sh), per i commit fatti
   da altri script.
L'elenco dei nomi resta nel riservato: in questo file non c'è nessun nome.
Robusto: se il riservato non c'è o un file non si legge, non trova niente (non blocca).
"""
import glob
import json
import os
import re
import sys

RIS = "/home/user/corso-informatica-riservato"
_CACHE = {}


def elenchi(ris=None):
    """(cognomi, coppie) dagli elenchi del riservato. Tutto in minuscolo."""
    ris = ris or RIS
    if ris in _CACHE:
        return _CACHE[ris]
    voci, extra, comuni = [], set(), set()
    for f in glob.glob(os.path.join(ris, "config", "*presenti*.json")) + \
            glob.glob(os.path.join(ris, "config", "*elenco*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        lista = d if isinstance(d, list) else (d.get("presenti") or d.get("elenco") or [])
        voci += [v for v in lista if isinstance(v, str)]
    try:
        d = json.load(open(os.path.join(ris, "config", "nomi-controllo.json"), encoding="utf-8"))
        extra = {n.lower() for n in d.get("nomi") or [] if isinstance(n, str) and len(n) >= 4}
        comuni = {n.lower() for n in d.get("parole_comuni") or [] if isinstance(n, str)}
    except Exception:
        pass
    parole = [v.replace("'", " ").replace("’", " ").lower().split() for v in voci]
    nomi_propri = {p[-1] for p in parole if len(p) >= 2}  # l'ultima parola è il nome: «Nome I.» è ammesso
    cognomi, coppie = set(), set()
    for p in parole:
        if len(p) < 2:
            continue
        for t in p[:-1]:
            if len(t) >= 4 and t not in nomi_propri:
                cognomi.add(t)
        if len(p[0]) >= 3 and len(p[1]) >= 3:
            coppie.add((p[0], p[1]))
    cognomi |= extra
    cognomi -= comuni
    _CACHE[ris] = (cognomi, coppie)
    return cognomi, coppie


def trova(testo, ris=None):
    """Lista dei problemi (cognome in maiuscolo + iniziale, mai il nome intero)."""
    if not testo:
        return []
    cognomi, coppie = elenchi(ris)
    if not cognomi and not coppie:
        return []
    basso = re.sub(r"https?://\S+", " ", testo.lower())
    trovati = []
    for c in sorted(cognomi):
        if re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(c), basso):
            trovati.append(c)
    for a, b in sorted(coppie):
        if a in trovati:
            continue
        if re.search(r"\b%s\W{1,3}%s\b|\b%s\W{1,3}%s\b" % (re.escape(a), re.escape(b), re.escape(b), re.escape(a)), basso):
            trovati.append(a)
    return ["%s… (%d lettere)" % (c[:2].upper(), len(c)) for c in trovati]


def avviso_nome_battesimo(testo, ris=None):
    """Avviso NON bloccante (13/11/2026): in un messaggio per il docente gli allievi si indicano solo con il
    COGNOME. Trova il COGNOME seguito (o preceduto) subito dal suo nome di battesimo, preso dagli elenchi
    del riservato. Cerca solo la coppia attaccata (cognome + suo nome), mai un nome da solo: nessun falso
    allarme sui nomi comuni. Dà «COGNOME… (N lettere)», mai il nome. Il testo da controllare è il messaggio
    SENZA riquadri e codice (lo toglie il chiamante)."""
    if not testo:
        return []
    ris = ris or RIS
    voci, comuni = [], set()
    for f in glob.glob(os.path.join(ris, "config", "*presenti*.json")) + \
            glob.glob(os.path.join(ris, "config", "*elenco*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        lista = d if isinstance(d, list) else (d.get("presenti") or d.get("elenco") or [])
        voci += [v for v in lista if isinstance(v, str)]
    try:
        d = json.load(open(os.path.join(ris, "config", "nomi-controllo.json"), encoding="utf-8"))
        comuni = {n.lower() for n in d.get("parole_comuni") or [] if isinstance(n, str)}
    except Exception:
        pass
    basso = re.sub(r"https?://\S+", " ", testo.lower())
    coppie = set()
    for v in voci:
        p = v.replace("'", " ").replace("\u2019", " ").lower().split()
        if len(p) < 2 or len(p[0]) < 4 or p[0] in comuni:
            continue
        for n in {p[1], p[-1]}:
            if len(n) >= 3:
                coppie.add((p[0], n))
    trovati = []
    for c, n in sorted(coppie):
        if re.search(r"(?<![\w-])%s[ \t]+%s(?![\w-])|(?<![\w-])%s[ \t]+%s(?![\w-])"
                     % (re.escape(c), re.escape(n), re.escape(n), re.escape(c)), basso):
            trovati.append("%s\u2026 (%d lettere)" % (c[:2].upper(), len(c)))
    return sorted(set(trovati))


def motivo_commit(testo, ris=None):
    p = trova(testo, ris)
    if not p:
        return None
    return ("Commit del repository PUBBLICO con il cognome di un allievo (regola R1, privacy): %s. "
            "Nel pubblico si scrive solo «Nome I.» (nome e iniziale) o niente nomi: riscrivi il "
            "messaggio del commit. Se è una parola comune e non un allievo, aggiungila a "
            "«parole_comuni» in config/nomi-controllo.json del riservato." % ", ".join(p[:3]))


def main_commit_msg(percorso):
    """Uso come hook git commit-msg: esce 1 (commit rifiutato) se il messaggio ha un cognome."""
    try:
        testo = open(percorso, encoding="utf-8", errors="replace").read()
        testo = "\n".join(r for r in testo.splitlines() if not r.startswith("#"))
        m = motivo_commit(testo)
    except Exception:
        return 0
    if m:
        sys.stderr.write(m + "\n")
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 2:
        sys.exit(main_commit_msg(sys.argv[1]))
    sys.exit(0)
