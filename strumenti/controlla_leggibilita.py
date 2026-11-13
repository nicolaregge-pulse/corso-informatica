#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllo di leggibilità dei testi per i ragazzi (dispense MD e pagine HTML di docs/).

Versione 1.0 (13/11/2026). Nasce dall'errore «dispense poco chiare per ragazzi delle medie, ripetuto» (REGISTRO-ERRORI-CLAUDE
v3.25): il docente ha chiesto più volte testi «più chiari ed espliciti». Principio del corso: un errore ripetuto corregge
uno STRUMENTO. Questo è lo strumento: si lancia a mano e lo usano gli agenti PRIMA di consegnare una dispensa (CHECKLIST-LEZIONE
voce 17). NON è un hook e non ferma niente da solo: in aula non può bloccare il docente.

Uso:    python3 strumenti/controlla_leggibilita.py FILE.md|FILE.html [altro file ...] [--max-parole 14] [--grave-oltre 25]
                                                    [--luogo PAROLA] [--strict] [--solo-gravi]
Esito:  0 = nessun avviso GRAVE (gli AVVISI si stampano ma non cambiano l'esito; con --strict anche loro danno 1)
        1 = almeno un avviso GRAVE (o, con --strict, almeno un avviso)
        2 = file illeggibile o non trovato
Output: per ogni file, per ogni pagina, per ogni riga:  riga N: [GRAVE|AVVISO] CODICE: messaggio. In fondo il riepilogo.

COSA LEGGE (decisioni di progetto, 13/11/2026)
  Legge SOLO il testo italiano. Salta:
  - i blocchi di codice (```), le tabelle (righe con «|»; in HTML <table>, <pre>, <code> a blocco), i commenti HTML
    (compresi il Changelog e la riga di versione in testa), le immagini, i titoli (non si misurano, ma si usano per le parole astratte);
  - l'arabo, il cinese e il bangla: le righe scritte quasi solo in quegli alfabeti, le righe «- AR:» / «- ZH:» e la coda
    «AR: ...» / «ZH: ...» in fondo a una riga italiana; in HTML gli elementi con lang="ar|zh|bn" o dir="rtl";
  - la riga «**Versione ...**» in testa (è per il docente, non per i ragazzi).
  Le righe «Deve vedersi» (e «Come:», «Mai password vere») dentro i riquadri FAI LO SCREENSHOT SONO testo per i ragazzi:
  si misurano come le altre frasi e si cercano le parole astratte; NON entrano nel controllo «dove» (non sono passi da fare
  in un posto ma la descrizione di che cosa si vede).
  Una «pagina» è il pezzo di testo tra due «<<PAGINA>>» (come nelle dispense del 13/11); se il file non ha «<<PAGINA>>», tra
  due titoli di livello 2 (##); in HTML è tutta la pagina.

COSA SEGNALA
  LUNGA      frase con più di --max-parole parole (14): AVVISO; da --grave-oltre parole (25, scelta di Claude, da confermare
             dal docente): GRAVE. Le parole sono i pezzi separati da spazi con almeno una lettera o cifra.
  ASTRATTA   parola della lista ASTRATTE (piccola, qui sotto) senza spiegazione: AVVISO, una volta per pagina. Si considera
             spiegata se, nella stessa frase dopo la parola o nelle 2 frasi dopo (stessa pagina), c'è: una parentesi subito dopo la
             parola, «:» o trattino subito dopo, «vuol dire», «significa», «cioè», «ovvero», «si chiama», «per esempio»,
             «ad esempio», «è quando», «è come», «=». Una parola nel titolo cerca la spiegazione nel testo che segue.
  DOVE       frase (non titolo, non «Deve vedersi») che comincia con un verbo di azione (apri, clicca, premi, scrivi, ...) e non
             contiene un luogo (Blocco note, Documento, Classroom, cartella, Cestino, finestra, tasto, ...: lista LUOGHI) né
             nella frase né in quella prima nello stesso paragrafo: AVVISO (solo avviso, mai grave).
  SENZAESEMPIO  frase con «scrivi» (o scrivete, scrivere) in un esercizio senza esempio: GRAVE. C'è l'esempio se nel paragrafo
             (riga o elenco con le righe attaccate) c'è «esempio» («Per esempio», «Esempio:», «ad esempio»), oppure se «scrivi»
             è seguito subito da un testo già dato (tra apici inversi, virgolette «», in grassetto, o un solo numero: «scrivi `ciao`»,
             «scrivi 2 e premi»). Se dopo «scrivi» c'è solo un conteggio («scrivi 4 righe») o «con parole tue», NON basta:
             anche con un pezzo di testo dato altrove nel paragrafo (le sole etichette `1 PASSWORD` non sono una risposta
             di esempio). Eccezione: «scrivi il tuo nome» (si capisce da solo).
  VAGO       consegna (frase che comincia con un verbo di azione o contiene «scrivi») con «ciò», «lo stesso» o «quello/questo/
             quella/...» usati da soli (non seguiti da un nome): AVVISO. [PPP del docente, 13/11]
  SOGGETTO   consegna senza soggetto esplicito: impersonale («si scrive»), passivo («va scritto», «deve essere»), infinito
             («Scrivere ...»), «bisogna», «è necessario»: AVVISO. Si scrive con «tu» implicito: «Scrivi», «Apri».
  COSA       «scrivi/fai/metti/inserisci/disegna» senza oggetto («Scrivi.», «Scrivi e premi», «Fai questo»): AVVISO.
  COMPLETA   consegna con «scrivi» in un paragrafo che non ha né luogo né esempio: AVVISO (cosa, dove, esempio insieme).
  ALLINEA    parola da scrivere nell'esercizio (in MAIUSCOLO, o tra apici come `1 PASSWORD`) che non c'è nel titolo della
             pagina-regola con lo stesso numero («### 1) ...») oppure, per le altre, non c'è in nessun punto del testo prima
             dell'esercizio: AVVISO. Serve a trovare esercizi che chiedono parole che le pagine non hanno mai usato.

Limiti (non provato / euristico): l'italiano si riconosce dall'alfabeto, non dalla lingua (una frase in inglese si misura come
italiano); la lista delle parole astratte è piccola di proposito; le frasi si dividono con . ! ? e «…», quindi un'abbreviazione
con il punto può spezzare una frase; l'HTML con JavaScript che scrive il testo a video non si legge. Falsi avvisi: si leggono
a mano. Non misura la comprensione vera: è un filtro, non un giudizio.
"""
import argparse
import html
import re
import sys
from html.parser import HTMLParser

SOGLIA_AVVISO = 14
SOGLIA_GRAVE = 25

# Parole lunghe o astratte (regex, senza \b): se compaiono vanno spiegate o esemplificate. Lista piccola, si allunga solo
# quando un errore nuovo lo richiede (tenere qui anche la spiegazione del perché).
ASTRATTE = {
    "regolamento": r"regolament[oi]",
    "privacy": r"privacy",
    "generativa": r"generativ[aoei]",
    "autenticazione": r"autenticazion[ei]",
    "configurazione": r"configurazion[ei]",
    "algoritmo": r"algoritm[oi]",
    "protocollo": r"protocoll[oi]",
    "crittografia": r"crittografi[ac]",
    "piattaforma": r"piattaform[ae]",
    "consenso": r"consens[oi]",
    "riservatezza": r"riservatezza",
    "vulnerabilità": r"vulnerabilit[àa]",
    "infrastruttura": r"infrastruttur[ae]",
    "sincronizzazione": r"sincronizzazion[ei]",
    "identità": r"identit[àa]",
    "responsabilità": r"responsabilit[àa]",
    "procedura": r"procedur[ae]",
    "funzionalità": r"funzionalit[àa]",
}

# Verbi di azione (imperativo, 2a persona singolare) che cominciano un passo.
VERBI = ("apri clicca premi scrivi vai scegli seleziona trascina digita cerca crea copia incolla sposta rinomina salva chiudi "
         "torna metti inserisci cancella elimina ripristina tocca doppio avvia accendi spegni esci entra accedi carica "
         "scarica stampa premete aprite scrivete").split()
RE_VERBO = re.compile(r"^(?:" + "|".join(VERBI) + r")\b", re.I)

# Luoghi: dove si clicca o si scrive. Si può aggiungere con --luogo.
LUOGHI = ["blocco note", "documento", "documenti", "classroom", "esplora", "desktop", "cartella", "cartelle", "cestino",
          "finestra", "barra", "menu", "schermo", "tasto", "tasti", "bottone", "pulsante", "browser", "google", "chrome",
          "moduli", "pagina", "scheda", "riquadro", "tastiera", "ctrl", "invio", "maiusc", "stamp", "canc", "esc", "windows",
          "f2", "mouse", "icona", "lista", "elenco", "sito", "link", "quiz", "compito", "quaderno", "foglio", "posto",
          "dentro", "sotto", "accanto", "in alto", "in basso", "a destra", "a sinistra", "sul pc", "nel pc", "il pc"]

CUE_SPIEGAZIONE = re.compile(
    r"vuol dire|vuole dire|significa|cioè|ovvero|si chiama|per esempio|ad esempio|esempio|è quando|sono quando|è come|sono come|=",
    re.I)

# Alfabeti non italiani (arabo, cinese e simili, bangla).
RE_STRANI = re.compile(r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿　-〿㐀-鿿＀-￯"
                       r"ঀ-৿]")
RE_LATINE = re.compile(r"[A-Za-zÀ-ÿ]")
RE_CODA_LINGUA = re.compile(r"\s(?:AR|ZH|BN):.*$")
RE_RIGA_LINGUA = re.compile(r"^\s*(?:[-*]\s*)?(?:AR|ZH|BN)\s*:")


def parole_di(testo):
    testo = testo.replace("\u27e6", "").replace("\u27e7", "")
    return [t for t in testo.split() if re.search(r"[0-9A-Za-zÀ-ÿ]", t)]


def pulisci_inline(s):
    """Toglie il markdown di una riga e restituisce il testo semplice (le parentesi e gli apici inversi restano come contenuto)."""
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\*\*([^*\n]+)\*\*", "\u27e6\\1\u27e7", s)   # il grassetto resta riconoscibile (testo già dato)
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"\1", s)
    return html.unescape(s)


def solo_italiano(riga):
    """Restituisce la riga senza gli alfabeti non italiani, o '' se la riga è quasi tutta in un'altra lingua."""
    riga = RE_CODA_LINGUA.sub("", riga)
    strani = len(RE_STRANI.findall(riga))
    if not strani:
        return riga
    if strani >= len(RE_LATINE.findall(riga)):
        return ""
    riga = RE_STRANI.sub("", riga)
    riga = re.sub(r"[(（]\s*[)）]", "", riga)
    return re.sub(r"\s{2,}", " ", riga).strip()


class Riga:
    """Una riga di testo italiano pulita, con la riga originale, il tipo e la pagina."""
    __slots__ = ("n", "testo", "tipo", "pagina", "par")

    def __init__(self, n, testo, tipo, pagina, par):
        self.n, self.testo, self.tipo, self.pagina, self.par = n, testo, tipo, pagina, par


def leggi_md(testo):
    righe, pagina, par = [], 1, 0
    ci_sono_pagine = "<<PAGINA>>" in testo
    in_codice = in_commento = False
    for n, grezza in enumerate(testo.splitlines(), 1):
        r = grezza.rstrip()
        s = r.strip()
        if in_commento:
            if "-->" in s:
                in_commento = False
            continue
        if s.startswith("<!--"):
            if "-->" not in s:
                in_commento = True
            continue
        if s.startswith("```"):
            in_codice = not in_codice
            continue
        if in_codice:
            continue
        if s == "<<PAGINA>>":
            pagina += 1
            par += 1
            continue
        if not s:
            par += 1
            continue
        if s.startswith("|") or s.startswith("![") or re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            continue
        if re.match(r"^\*\*Versione\b", s) or RE_RIGA_LINGUA.match(s):
            continue
        tipo = "testo"
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            tipo = "titolo"
            s = m.group(2)
            if len(m.group(1)) == 2 and not ci_sono_pagine:
                pagina += 1
            par += 1
        else:
            if s.startswith(">"):
                s = re.sub(r"^(?:>\s*)+", "", s)
                if re.search(r"Deve vedersi|Come:|Mai password|FAI LO SCREENSHOT", s):
                    tipo = "riquadro"
            if re.match(r"^(?:[-*+]|\d+[.)])\s+", s):
                par += 1   # ogni voce di elenco è un paragrafo a sé: l'esempio di una voce non copre le altre
            s = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", s)
        s = solo_italiano(pulisci_inline(s)).strip()
        if s:
            righe.append(Riga(n, s, tipo, pagina, par))
    return righe


class _Estrattore(HTMLParser):
    """HTML di docs/ -> righe di testo italiano (salta script, stile, tabelle, codice a blocco, arabo, cinese)."""
    BLOCCHI = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "br", "section", "article", "ol", "ul", "tr", "button",
               "label", "summary", "details", "header", "footer", "main", "figcaption", "blockquote"}
    VUOTI = {"br", "img", "hr", "meta", "link", "input", "source", "col", "area", "base", "wbr"}
    SALTA = {"script", "style", "pre", "table", "head", "svg", "textarea", "noscript", "template"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila, self.righe, self.buf, self.n0, self.tipo = [], [], [], 1, "testo"

    def _salta_ora(self):
        return any(s for _, s in self.pila)

    def _chiudi(self):
        t = "".join(self.buf)
        t = re.sub(r"\s+", " ", t).strip()
        self.buf = []
        if t and not self._salta_ora():
            t = solo_italiano(t).strip()
            if t:
                self.righe.append(Riga(self.n0, t, self.tipo, 1, len(self.righe)))
        self.tipo = "testo"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.BLOCCHI:
            self._chiudi()
        if tag in self.VUOTI:
            return
        lang = (a.get("lang") or "").lower()
        salta = (tag in self.SALTA or lang.startswith(("ar", "zh", "bn")) or (a.get("dir") or "").lower() == "rtl"
                 or "hidden" in a or a.get("aria-hidden") == "true")
        self.pila.append((tag, salta))
        if re.match(r"h[1-6]$", tag):
            self.tipo = "titolo"
        self.n0 = self.getpos()[0]

    def handle_endtag(self, tag):
        if tag in self.BLOCCHI:
            self._chiudi()
        for i in range(len(self.pila) - 1, -1, -1):
            if self.pila[i][0] == tag:
                del self.pila[i:]
                break

    def handle_data(self, data):
        if not self.buf:
            self.n0 = self.getpos()[0]
        if not self._salta_ora():
            self.buf.append(data)

    def chiudi_tutto(self):
        self._chiudi()


def leggi_html(testo):
    e = _Estrattore()
    e.feed(testo)
    e.close()
    e.chiudi_tutto()
    return e.righe


def frasi(testo):
    """Divide in frasi; restituisce la lista dei testi."""
    pezzi = re.split(r"(?<=[.!?…])\s+(?=[«\"“'A-ZÀ-Ý0-9`*])", testo.strip())
    return [p.strip() for p in pezzi if p.strip()]


def ha_esempio_scrivi(frase, paragrafo_testo):
    """True se «scrivi» ha un esempio: «esempio» nel paragrafo o un testo già dato subito dopo il verbo."""
    if re.search(r"esempio|\bes\.", paragrafo_testo, re.I):
        return True
    for m in re.finditer(r"(?<!non )\bscriv(?:i|ete)\b", frase, re.I):
        dopo = frase[m.end():]
        if re.match(r"\s*(?:il tuo nome|il tuo nome e cognome)\b", dopo, re.I):
            continue
        # testo già dato: subito apici inversi, virgolette, o un numero solo (scrivi 2 e premi)
        if re.match(r"\s*(?::\s*)?(?:il|la|lo|un|una)?\s*[`«\"“\u27e6]", dopo):
            continue
        if re.match(r"[^.!?]{0,40}\(\s*\d+\s*(?:,|o\b)", dopo):   # «scrivi il numero (1, 2, 3 o 4)»: i valori sono dati
            continue
        if re.match(r"\s*\d+\s*(?:e\b|[.,;:)]|$|poi\b)", dopo):
            continue
        return False
    return True


def controlla(righe, max_parole, grave_oltre, luoghi):
    """Restituisce la lista di (n_riga, pagina, gravita, codice, messaggio)."""
    avvisi = []
    luoghi_re = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(x) for x in luoghi) + r")(?!\w)", re.I)

    # paragrafi: gruppi di righe con lo stesso `par` e la stessa pagina
    par_testo = {}
    for r in righe:
        par_testo.setdefault((r.pagina, r.par), []).append(r.testo)

    # tutte le frasi del testo, in ordine, con pagina e paragrafo
    tutte = []  # (riga, frase)
    for r in righe:
        for f in frasi(r.testo):
            tutte.append((r, f))

    # 1) frasi lunghe, 3) dove, 4) senza esempio
    prima_in_par = {}
    gia_senza_esempio = set()
    for r, f in tutte:
        k = (r.pagina, r.par)
        if r.tipo != "titolo":
            n = len(parole_di(f))
            if n >= grave_oltre:
                avvisi.append((r.n, r.pagina, "GRAVE", "LUNGA", f"frase di {n} parole (dal {grave_oltre} è grave): «{riassunto(f)}»"))
            elif n > max_parole:
                avvisi.append((r.n, r.pagina, "AVVISO", "LUNGA", f"frase di {n} parole (più di {max_parole}): «{riassunto(f)}»"))
            if r.tipo != "riquadro" or not re.search(r"Deve vedersi", f):
                f_pulita = re.sub(r"^(?:Passo\s+\d+\s*[:.)-]?\s*)", "", f)
                if RE_VERBO.match(f_pulita) and not f_pulita.startswith("FAI LO") and not luoghi_re.search(f_pulita) \
                        and not (prima_in_par.get(k) and luoghi_re.search(prima_in_par[k])):
                    avvisi.append((r.n, r.pagina, "AVVISO", "DOVE", f"il passo non dice dove: «{riassunto(f)}»"))
            if re.search(r"(?<!non )\bscriv(?:i|ete)\b", f, re.I):
                par = " ".join(par_testo[k])
                if not ha_esempio_scrivi(f, par) and k not in gia_senza_esempio:
                    gia_senza_esempio.add(k)   # una segnalazione per esercizio (paragrafo)
                    avvisi.append((r.n, r.pagina, "GRAVE", "SENZAESEMPIO",
                                   f"esercizio con «scrivi» senza esempio (manca «Per esempio» o il testo già dato): «{riassunto(f)}»"))
            avvisi += controlla_consegna(r, f, k, par_testo, prima_in_par, luoghi_re)
        prima_in_par[k] = f

    # 2) parole astratte non spiegate: una volta per pagina
    visti = set()
    for i, (r, f) in enumerate(tutte):
        for nome, rx in ASTRATTE.items():
            if (r.pagina, nome) in visti:
                continue
            m = re.search(r"(?<!\w)(" + rx + r")(?!\w)", f, re.I)
            if not m:
                continue
            visti.add((r.pagina, nome))
            dopo_nella_frase = f[m.end():]
            finestra = dopo_nella_frase
            if r.tipo == "titolo":
                finestra = ""  # un titolo non spiega sé stesso: si guarda il testo che segue
            for r2, f2 in tutte[i + 1:i + 3]:
                if r2.pagina != r.pagina:
                    break
                finestra += " " + f2
            subito = re.match(r"\s*(?:\(|:|–|—|-\s)", dopo_nella_frase)
            if not subito and not CUE_SPIEGAZIONE.search(finestra):
                avvisi.append((r.n, r.pagina, "AVVISO", "ASTRATTA",
                               f"«{m.group(1)}» senza spiegazione o esempio nelle 2 frasi dopo (stessa pagina)"))

    # 5) parole del compito non allineate alle pagine
    avvisi += controlla_allineamento(righe)
    avvisi.sort(key=lambda a: (a[1], a[0]))
    return avvisi


RE_VAGO = re.compile(
    r"(?<!\w)(?:ciò|lo stesso|la stessa|(?:quello|quella|quelli|quelle|questo|questa|questi|queste)"
    r"(?=\s*(?:[,.;:!?]|$|che\b|e\b|per\b|con\b|di\b|in\b|a\b|è\b|sono\b)))(?!\w)", re.I)
RE_IMPERSONALE = re.compile(
    r"\bsi (?:scrive|apre|clicca|preme|deve|devono|fa|fanno)\b|\bva\s+\w+(?:ato|ito|uto)\b|\bdeve essere\s+\w+(?:ato|ita|ito|uto)\b|\bdevono essere\s+\w+(?:ati|ate|iti|uti)\b"
    r"|\bbisogna\b|\bè necessario\b|\boccorre\b|^(?:scrivere|aprire|cliccare|premere|inserire)\b", re.I)
RE_SENZA_OGGETTO = re.compile(
    r"\b(?:scrivi|scrivete|fai|fate|metti|inserisci|disegna)\s*(?:$|[.,;:!?]|(?:e|poi|qui|lì|li|tutto|così)\b"
    r"|(?:questo|quello|ciò)\b)", re.I)


def controlla_consegna(r, f, k, par_testo, prima_in_par, luoghi_re):
    """Regola del docente (13/11, PPP): una consegna dice COSA si fa (verbo + oggetto), DOVE e con quale ESEMPIO; niente
    pronomi vaghi, niente forme senza soggetto (impersonale, passivo, infinito)."""
    out = []
    consegna = bool(RE_VERBO.match(f) or re.search(r"(?<!non )\bscriv(?:i|ete)\b", f, re.I)
                    or RE_IMPERSONALE.search(f))
    if not consegna or r.tipo == "titolo" or f.startswith("FAI LO"):
        return out
    if RE_VAGO.search(f):
        out.append((r.n, r.pagina, "AVVISO", "VAGO",
                    f"pronome vago nella consegna (ciò, quello, questo...): di' la cosa con il suo nome: «{riassunto(f)}»"))
    if RE_IMPERSONALE.search(f):
        out.append((r.n, r.pagina, "AVVISO", "SOGGETTO",
                    f"consegna senza soggetto (impersonale, passivo o infinito): scrivi «tu» + verbo («Scrivi...»): «{riassunto(f)}»"))
    if RE_SENZA_OGGETTO.search(f):
        out.append((r.n, r.pagina, "AVVISO", "COSA",
                    f"la consegna non dice che cosa (manca l'oggetto del verbo): «{riassunto(f)}»"))
    # consegna di scrittura che non dice cosa + dove + esempio insieme: segnalata una volta per paragrafo
    if re.search(r"(?<!non )\bscriv(?:i|ete)\b", f, re.I):
        par = " ".join(par_testo[k])
        manca = []
        if not luoghi_re.search(par):
            manca.append("dove")
        if not re.search(r"esempio|\bes\.", par, re.I) and not ha_esempio_scrivi(f, par):
            manca.append("esempio")
        if len(manca) == 2:
            out.append((r.n, r.pagina, "AVVISO", "COMPLETA",
                        f"la consegna non dice {' né '.join(manca)}: «{riassunto(f)}»"))
    return out


def riassunto(f, n=110):
    f = f.replace("\u27e6", "").replace("\u27e7", "")
    f = re.sub(r"\s+", " ", f).strip()
    return f if len(f) <= n else f[:n - 1] + "…"


def controlla_allineamento(righe):
    """Parole da scrivere nell'esercizio (`1 PASSWORD`, MAIUSCOLO) che non compaiono nelle pagine."""
    avvisi = []
    titoli_regola = {}  # numero -> (testo del titolo)
    for r in righe:
        if r.tipo == "titolo":
            m = re.match(r"^(\d+)\)\s*(.*)$", r.testo)
            if m:
                titoli_regola.setdefault(int(m.group(1)), []).append(r.testo)
    # righe di esercizio: contengono «scrivi» e parole da scrivere
    for idx, r in enumerate(righe):
        if r.tipo == "titolo" or not re.search(r"(?<!non )\bscriv(?:i|ete)\b", r.testo, re.I):
            continue
        # unisce la riga con le successive dello stesso paragrafo
        testo = " ".join(x.testo for x in righe[idx:idx + 3] if x.par == r.par)
        prima = " ".join(x.testo for x in righe[:idx] if x.tipo != "riquadro")
        vista = set()
        for m in re.finditer(r"`(\d+)\s+([A-ZÀ-Ý]{2,})`", r.testo):
            num, parola = int(m.group(1)), m.group(2)
            vista.add(parola)
            tit = " ".join(titoli_regola.get(num, []))
            if tit and parola.lower() not in tit.lower():
                avvisi.append((r.n, r.pagina, "AVVISO", "ALLINEA",
                               f"l'esercizio chiede «{num} {parola}» ma il titolo della pagina {num} dice «{riassunto(tit, 70)}»: "
                               f"la parola non c'è nel titolo"))
        scelta = re.search(r"\bscegli tra\b(.*)", testo, re.I)
        for parola in re.findall(r"(?<![\w`])([A-ZÀ-Ý]{2,})(?![\w`])", scelta.group(1) if scelta else ""):
            if parola in vista:
                continue
            if not re.search(re.escape(parola), prima, re.I):
                avvisi.append((r.n, r.pagina, "AVVISO", "ALLINEA",
                               f"l'esercizio chiede la parola «{parola}» che non compare nelle pagine prima"))
            vista.add(parola)
    return avvisi


def leggi_file(percorso):
    with open(percorso, encoding="utf-8") as f:
        testo = f.read()
    if percorso.lower().endswith((".html", ".htm")):
        return leggi_html(testo)
    return leggi_md(testo)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Controllo di leggibilità dei testi per i ragazzi (vedi la docstring).")
    ap.add_argument("file", nargs="+")
    ap.add_argument("--max-parole", type=int, default=SOGLIA_AVVISO)
    ap.add_argument("--grave-oltre", type=int, default=SOGLIA_GRAVE)
    ap.add_argument("--luogo", action="append", default=[], help="luogo in più, per esempio «Excel»")
    ap.add_argument("--strict", action="store_true", help="esce con 1 anche per i semplici AVVISI")
    ap.add_argument("--solo-gravi", action="store_true", help="stampa solo gli avvisi GRAVI")
    a = ap.parse_args(argv)

    luoghi = LUOGHI + [x.lower() for x in a.luogo]
    gravi = avvisi_tot = 0
    errore = False
    for percorso in a.file:
        try:
            righe = leggi_file(percorso)
        except (OSError, UnicodeDecodeError) as e:
            print(f"ERRORE: non riesco a leggere {percorso}: {e}")
            errore = True
            continue
        av = controlla(righe, a.max_parole, a.grave_oltre, luoghi)
        g = sum(1 for x in av if x[2] == "GRAVE")
        t = len(av)
        gravi += g
        avvisi_tot += t
        print(f"== {percorso}: {len(righe)} righe di testo italiano, {t} avvisi ({g} gravi)")
        pagina_corr = None
        for n, pag, grav, cod, msg in av:
            if a.solo_gravi and grav != "GRAVE":
                continue
            if pag != pagina_corr:
                print(f"  -- pagina {pag}")
                pagina_corr = pag
            print(f"    riga {n}: [{grav}] {cod}: {msg}")
    print(f"TOTALE: {avvisi_tot} avvisi, di cui {gravi} gravi. "
          + ("ESITO: DA CORREGGERE (almeno un avviso grave)." if gravi else "ESITO: nessun avviso grave."))
    if errore:
        return 2
    if gravi or (a.strict and avvisi_tot):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
