#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove dei controlli rimessi il 23/11/2026 (controlli_ripristinati.py, controllo-messaggio.py, controlli_pagine.py).

1. Casi giusti e sbagliati scritti qui (uno per controllo): lo sbagliato deve scattare con il tipo giusto (blocco o avviso),
   il giusto non deve scattare.
2. FALSI ALLARMI sul lavoro normale: tutti i messaggi veri di Claude del 20/11/2026 (bobina del riservato) e tutti i kit del
   20/11/2026 (report/2026-11-20/KIT-CLASSROOM-*.md) passano dai controlli: devono dare 0 scatti. Se il riservato non c'è la parte 2
   si salta e lo dice.
Uso: python3 .claude/hooks/prove/prova_controlli_ripristinati.py   (ultima riga «N/N», falsi allarmi a parte)
"""
import glob
import importlib.util
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.dirname(QUI)
RIS = "/home/user/corso-informatica-riservato"


def carica(nome, cartella=HOOKS):
    spec = importlib.util.spec_from_file_location("m_" + re.sub(r"\W", "_", nome), os.path.join(cartella, nome))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


cm = carica("controllo-messaggio.py")
cr = carica("controlli_ripristinati.py")
cp = carica("controlli_pagine.py")
cn = carica("controllo_nomi.py")

ok = tot = 0


def verifica(nome, condizione):
    global ok, tot
    tot += 1
    if condizione:
        ok += 1
    else:
        print("FALLITO:", nome)


def tipi(testo, docente=""):
    t = cm.senza_citazioni(cm.senza_codice_in_linea(cm.senza_riquadri(testo)))
    return sorted({x[0] for x in cr.esegui(t, testo, docente)})


# ---- testo: (nome, sbagliato, giusto, tipo atteso, docente)
CASI = [
    ("a posto senza prova", "Lazarus sul PC 32 è a posto.\nPuò continuare.", "Lazarus sul PC 32 compila alle 10:42: riga «compilazione riuscita».", "blocco", ""),
    ("risolto senza prova", "Il blocco dello script è risolto.", "Il blocco è risolto: letto il battito alle 10:41.", "blocco", ""),
    ("funziona negato", "Non funziona ancora: provo di nuovo.", "Non funziona ancora: provo di nuovo.", None, ""),
    ("conteggio senza fonte", "Hanno consegnato 17 su 19.", "Hanno consegnato 17 su 19 (letto da Classroom alle 10:42).", "blocco", ""),
    ("non ha caricato senza ricerca", "L'allievo non ha caricato il file.", "L'allievo non ha caricato il file: clone fatto alle 10:40.", "blocco", ""),
    ("Veyon niente", "Dalla miniatura Veyon il PC 12 non ha fatto niente.", "Il PC 12 mostra la pagina del compito alle 10:40 (miniatura Veyon).", "blocco", ""),
    ("screenshot come prova", "Dallo screenshot Veyon l'allievo ha già la pagina online.", "Nel repository (letto alle 10:40) la pagina c'è.", "blocco", ""),
    ("pagina con prova=1", "Ho provato la pagina con ?prova=1: funziona.", "Pagina aperta sul sito vero con i dati veri alle 10:40.", "blocco", ""),
    ("riquadro di prima", "Incolla il testo del riquadro di prima.", "Incolla questo testo:\n```\nPresenti\n```", "blocco", ""),
    ("nessuna AI", "Nessuna AI aperta sui PC.", "Dalle miniature Veyon (22 finestre viste) nessuna AI aperta.", "avviso", ""),
    ("tempi dello script", "Arrivano entro pochi minuti: li pubblica lo script.", "Lo script non ha risposto al battito delle 10:40: piano B a mano.", "avviso", ""),
    ("utente non indicato", "Utente non indicato per il PC 14.", "Chi è al PC 14? Non lo vedo nelle presenze.", "avviso", ""),
    ("ha copiato", "ROSSI ha copiato il compito di BIANCHI.", "Il compito di ROSSI è molto simile a quello di BIANCHI: da verificare.", "avviso", ""),
    ("rosso atteso", "L'audit dà ROSSO ma è atteso: lo ignoro.", "ROSSO dell'audit: manca il report delle 10:00.", "avviso", ""),
    ("release cartella", "Faccio la release della cartella docs/1inf.", "Faccio la release: vale per tutto il repository.", "avviso", ""),
    ("genere", "Lei ha finito il quiz.", "ROSSI ha finito il quiz.", "avviso", ""),
    ("onestamente", "Onestamente, il risultato è valido.", "Il risultato è 5 su 5.", "avviso", ""),
    ("catena di coordinate", "Account PIAMARTA · finestra Chrome · clicca il «+».", "Account PIAMARTA. Premi Ctrl+T.", "avviso", ""),
    ("salta al passo", "1. Se la scheda è già aperta, salta al passo 4.", "1. Apri la scheda.", "avviso", ""),
    ("Apps Script senza file", "Apri Apps Script, premi Ctrl+V e salva.", "Apri automazione-corso.gs, copia tutto e incolla in Apps Script con Ctrl+V.", "avviso", ""),
    ("DIDAweb senza disciplina", "Stringa:\n```\nh 3; ROSSI 60; BIANCHI 70\n```", "**Disciplina da scegliere: LABORATORIO PROFESSIONALE**\n```\nh 3; ROSSI 60; BIANCHI 70\n```", "avviso", ""),
    ("voto sotto 40", "**Disciplina da scegliere: INFORMATICA**\n```\nh 3; ROSSI 35; BIANCHI 70\n```", "**Disciplina da scegliere: INFORMATICA**\n```\nh 3; ROSSI 40; BIANCHI 70\n```", "avviso", ""),
    ("domanda su presenti", "Chi sono i presenti di oggi? Mi dai l'elenco?", "Presenti di oggi dal diario (letto alle 10:40): 19.", "avviso", ""),
    ("avanti dopo dammi", "Te lo consegno al tuo avanti.", "Eccolo.", "avviso", "dammi il quiz appena è pronto"),
    ("avanti dopo PPP", "Te lo consegno al tuo avanti.", "Te lo consegno al tuo avanti.", None, "PPP prepara il quiz"),
    ("errore senza numero", "Registrato l'errore.", "Registrato come #391.", "avviso", "registra l'errore che ho appena detto"),
    ("tolto su domanda", "Ho tolto la colonna.", "La colonna conta le prove; la lascio.", "avviso", "cosa vuol dire la colonna Allenamenti?"),
    ("alza la mano nel kit", "TITOLO\n```\nG Ora 2\n```\nOGGETTO\n```\nSe sei bloccato alza la mano.\n```", "TITOLO\n```\nG Ora 2\n```\nOGGETTO\n```\nScrivi all'assistente.\n```", "blocco", ""),
    ("tolto su ordine", "Ho tolto la colonna.", "Ho tolto la colonna.", None, "togli la colonna Allenamenti"),
]
for nome, s, g, tipo, doc in CASI:
    ts, tg = tipi(s, doc), tipi(g, doc)
    if tipo is None:
        verifica(nome + " (non deve scattare)", not ts)
    else:
        verifica(nome + " sbagliato", tipo in ts)
        verifica(nome + " giusto", tipo not in tg and not (tipo == "blocco" and "blocco" in tg))

# ---- firma ricordata per ore già firmate (blocco, R5.1)
import datetime
import tempfile
t = tempfile.mkdtemp()
oggi = datetime.datetime.now(cm.TZ_ROMA)
open(os.path.join(t, "FIRME-REGISTRO-2026-27.md"), "w").write(
    "## 01 Lunedì %s\n\n1. Ora 08-09, 1INF: FIRMATA il %s alle 08:42.\n" % (oggi.strftime("%d/%m/%Y"), oggi.strftime("%d/%m/%Y")))
cm.PUB = t
verifica("firma ricordata ma firmata", bool(cm.controllo_firma_ricordata("FIRMA: ricordati di firmare le ore entro le 14:05.", oggi)))
verifica("firma: niente da ricordare", not cm.controllo_firma_ricordata("Tutte le ore di oggi sono firmate. Niente da ricordare.", oggi))
verifica("firma di un altro giorno", not cm.controllo_firma_ricordata("FIRMA: ricordati di firmare l'ora del 19/11.", oggi))
cm.PUB = "/home/user/corso-informatica"

# ---- nome di battesimo da solo (avviso), con un elenco finto
ris = tempfile.mkdtemp()
os.makedirs(ris + "/config")
import json
json.dump(["ROSSI MARIO", "BIANCHI ANNA"], open(ris + "/config/presenti-finto.json", "w"))
verifica("nome da solo", bool(cn.avviso_nome_solo("Mario ha consegnato il quiz.", ris)))
verifica("cognome e nome", not cn.avviso_nome_solo("ROSSI Mario ha consegnato il quiz.", ris))
verifica("solo cognome", not cn.avviso_nome_solo("ROSSI ha consegnato il quiz.", ris))

# ---- pagine (controlli_pagine.py, controlli TUTTI)
PAGINE = [
    ("quiz sul sito", "docs/3inf-rete/quiz.html", "<form id='quiz'><button>Invia le risposte</button></form><script>fetch('/api/quiz')</script>",
     "<a href='https://docs.google.com/forms/d/x/viewform'>Fai il quiz sul Modulo</a>"),
    ("carta e penna", "docs/1inf/index.html", "<p>Stampa la scheda e scrivi le risposte con la penna.</p>", "<p>Scrivi le risposte nel Documento.</p>"),
    ("copia file da Classroom", "docs/3inf-rete/index.html", "<p>Copia i file unit1.lfm e unit1.pas da Classroom nella cartella del progetto.</p>",
     "<p>Premi il bottone verde: il progetto si scarica da solo.</p>"),
    ("senza a che serve", "docs/3inf-x/index.html", "<section id='pannello'><h2>Situazione</h2><table><tr><td>1</td></tr></table></section>",
     "<section id='pannello'><h2>Situazione</h2><p>A che serve: vedi chi ha finito.</p><table><tr><td>1</td></tr></table></section>"),
    ("campi ripetuti nelle tre lingue", "docs/1inf/index.html", "<p>Ho ascoltato: ____</p><p>سمعت: ____</p><p>我听了: ____</p>",
     "<p>Ho ascoltato: ____</p><p>Ho guardato: ____</p>"),
    ("ruoli non richiesti", "docs/1inf/index.html", "<h2>Ruoli: MANI e OCCHI</h2><p>Uno guarda.</p>", "<h2>Lavorate in coppia</h2><p>Uno guarda.</p>"),
]
for nome, perc, s, g in PAGINE:
    verifica("pagina %s sbagliato" % nome, bool(cp.controlla(perc, s, controlli=cp.TUTTI)))
    verifica("pagina %s giusto" % nome, not cp.controlla(perc, g, controlli=cp.TUTTI))

print("casi su testi, nomi e pagine: %d/%d" % (ok, tot))

# ---- falsi allarmi sul lavoro normale del 20/11/2026
falsi = []
n_msg = n_kit = 0
bob = RIS + "/bobine/corso/2026-11-20_bobina_b09df496.md"
if os.path.exists(bob):
    testo = open(bob, encoding="utf-8").read()
    parti = re.split(r"\n\*\*(NICOLA|CLAUDE)\*\* \((\d\d:\d\d)\):\n", testo)
    for i in range(1, len(parti) - 2, 3):
        if parti[i] != "CLAUDE":
            continue
        corpo = re.sub(r"\[esito .*?\]\n", "\n", parti[i + 2] + "\n", flags=re.S)
        corpo = "\n".join(r for r in corpo.splitlines() if not re.match(r"^\s*\[[^\]]*\]\s*$", r)).strip()
        if len(corpo) < 20:
            continue
        n_msg += 1
        t = cm.senza_citazioni(cm.senza_codice_in_linea(cm.senza_riquadri(corpo)))
        for tipo, msg in cr.esegui(t, corpo, ""):
            falsi.append(("messaggio %s" % parti[i + 1], tipo, msg[:130]))
        try:
            f = cm.controllo_firma_ricordata(corpo, datetime.datetime(2026, 11, 20, 12, 0, tzinfo=cm.TZ_ROMA))
            if f:
                falsi.append(("messaggio %s" % parti[i + 1], "blocco", f[:130]))
        except Exception:
            pass
        try:
            soli = cn.avviso_nome_solo(t)
            if soli:
                falsi.append(("messaggio %s" % parti[i + 1], "avviso", "nome solo " + ",".join(soli)))
        except Exception:
            pass
    for f in sorted(glob.glob(RIS + "/report/2026-11-20/KIT-CLASSROOM-*.md")):
        n_kit += 1
        corpo = open(f, encoding="utf-8").read()
        t = cm.senza_citazioni(cm.senza_codice_in_linea(cm.senza_riquadri(corpo)))
        for tipo, msg in cr.esegui(t, corpo, ""):
            falsi.append((os.path.basename(f), tipo, msg[:130]))
    # pagine del sito toccate il 20/11: tutte le pagine dei ragazzi in docs/ (controlli TUTTI)
    for f in sorted(glob.glob("/home/user/corso-informatica/docs/**/*.html", recursive=True)):
        p = os.path.relpath(f, "/home/user/corso-informatica")
        if not cp.da_controllare(p):
            continue
        pr = [x for x in cp.controlla(p, open(f, encoding="utf-8", errors="replace").read(), controlli=cp.SICURI)
              if re.search(r"#(?:178|227)", x)]
        for x in pr:
            falsi.append((p, "pagina", x[:130]))
    print("FALSI ALLARMI: %d su %d messaggi e %d kit del 20/11/2026 (più le pagine di docs/ con i controlli che bloccano il push)" % (len(falsi), n_msg, n_kit))
    for f in falsi[:40]:
        print("  ", f)
else:
    print("FALSI ALLARMI: non provato (riservato assente)")
tot += 1
ok += 0 if falsi else 1   # i falsi allarmi sul lavoro normale contano come una prova: devono essere 0
print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
