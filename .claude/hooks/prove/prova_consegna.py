#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove dei controlli #386-#389 (23/11/2026): strumenti/controlli_consegna.py e i controlli (kk) (ll) (mm) di controllo-messaggio.py.
Uso: python3 /home/user/corso-informatica/.claude/hooks/prove/prova_consegna.py   (ultima riga «N/N»)
Ogni controllo ha casi che DEVONO passare (nessun avviso) e casi che DEVONO scattare. Dati finti in cartelle temporanee."""
import datetime
import importlib.util
import json
import os
import sys
import tempfile

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.dirname(os.path.dirname(H))
os.environ["CORSO_STATO_FORMATO"] = ""
sys.path.insert(0, os.path.join(PUB, "strumenti"))
import controlli_consegna as lib

os.environ["CORSO_STATO_BUON_SENSO"] = ""   # il filtro di buon senso (#390) non ricorda i messaggi finti delle prove
spec = importlib.util.spec_from_file_location("cm", os.path.join(H, "controllo-messaggio.py"))
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)
cm.STATO_FORMATO = ""
T = tempfile.mkdtemp()
ok = tot = 0


def prova(nome, cond):
    global ok, tot
    tot += 1
    ok += bool(cond)
    print(("OK   " if cond else "NO   ") + nome)


ROSSO, BLU = "🟥" * 14, "🟦" * 14
OGG = "Oggi fai il tecnico. Segui il foglio PDF. Premi Consegna. Poi fai il quiz."

# ================= #387 testi dei post
def pp(**k):
    base = dict(titolo="20/11 Ora 4: Il metodo del tecnico", oggetto=OGG, ora=4, data_kit=(20, 11), quiz_in_sezione=True)
    base.update(k)
    return lib.problemi_post(**base)


prova("#387 passa: post coerente", pp() == [])
prova("#387 scatta: «ieri» nel testo", any("ieri" in x for x in pp(oggetto="Oggi guardi i guasti di ieri e di oggi. Poi fai il quiz.")))
prova("#387 scatta: «domani» nel titolo", any("domani" in x for x in pp(titolo="20/11 Ora 4: Il quiz di domani")))
prova("#387 passa: «oggi» e «Ieri» non scritto", pp(oggetto="Oggi fai il tecnico. Poi fai il quiz.") == [])
prova("#387 scatta: «_» iniziale nel testo", any("«_»" in x for x in pp(oggetto="_" + OGG)))
prova("#387 scatta: «_» iniziale nel titolo", any("«_»" in x for x in pp(titolo="_20/11 Ora 4: Il metodo")))
prova("#387 scatta: ???? al posto di arabo e cinese", any("???" in x for x in pp(oggetto=OGG + "\n???? ???? ?? ??")))
prova("#387 passa: arabo e cinese veri", pp(oggetto=OGG + "\nاليوم أنت الفني. 今天你当技术员。") == [])
prova("#387 scatta: ora del titolo diversa dal kit", any("Ora 5" in x for x in pp(titolo="20/11 Ora 5: Il metodo")))
prova("#387 scatta: titolo senza «Ora N»", any("Ora 4" in x for x in pp(titolo="Il metodo del tecnico")))
prova("#387 scatta: data del titolo diversa dal kit", any("data del titolo" in x for x in pp(titolo="19/11 Ora 4: Il metodo")))
prova("#387 scatta: 25 carte e il testo non dice quali", any("25 carte" in x for x in pp(
    testo_sezione="Allegato 1, foglio (28 pagine: 2 di spiegazione, 25 carte, 1 scheda)", quiz_in_sezione=False,
    oggetto="Ogni pagina del foglio è una carta con un guasto. Scegli A, B o C.")))
prova("#387 passa: 25 carte e il testo dice «carte da 1 a 8»", pp(
    testo_sezione="foglio (28 pagine, 25 carte)", quiz_in_sezione=False, oggetto="Oggi fai le carte da 1 a 8. Premi Consegna.") == [])
prova("#387 scatta: «carte da 1 a 30» ma il foglio ne ha 25", any("fino alla 30" in x for x in pp(
    testo_sezione="25 carte", quiz_in_sezione=False, oggetto="Fai le carte da 1 a 30.")))
prova("#387 passa: poche carte (5) senza intervallo", pp(testo_sezione="5 carte", quiz_in_sezione=False, oggetto="Fai le carte. Premi Consegna.") == [])
prova("#387 scatta: il kit ha il quiz e il testo no", any("non lo nomina" in x for x in pp(oggetto="Oggi fai il tecnico. Premi Consegna.")))
prova("#387 scatta: il testo cita il quiz e il kit no", any("non ne ha uno" in x for x in pp(quiz_in_sezione=False)))
prova("#387 passa: «Nessun quiz in quest'ora» nel kit", pp(quiz_in_sezione=False, testo_sezione="Nessun quiz in quest'ora.") == [])
prova("#387 passa: quiz non noto (None) non controlla", pp(quiz_in_sezione=None, oggetto="Oggi fai il tecnico.") == [])

# ================= #386 pacchetto PUBB
PACCHETTO = ROSSO + "\n**TITOLO**\n```\n20/11 Ora 4: Il metodo\n```\n**OGGETTO**\n```\nOggi fai il tecnico. Seguirà il quiz.\n```\n" + BLU + "\n📄 DISPENSA ALLIEVI ORA 4 ⬇️\n"
LUNGA = "Ho pubblicato la prima ora su Classroom e ho controllato la consegna: il compito risulta PUBLISHED alle 08:21 nel dato letto."
prova("#386 scatta: PUBB 4 e risposta lunga senza pacchetto", lib.pacchetto_pubb_mancante("PUBB 4", [LUNGA]) is not None)
prova("#386 passa: PUBB 4 con il pacchetto nel formato", lib.pacchetto_pubb_mancante("PUBB 4", [PACCHETTO, BLU + "\n" + ROSSO]) is None)
prova("#386 scatta: pacchetto con TITOLO e OGGETTO fuori dai riquadri", lib.pacchetto_pubb_mancante(
    "ridammi i dati per Classroom kit 4 ora", [ROSSO + "\nTITOLO: 20/11 Ora 4: Il metodo\nOGGETTO: Oggi fai il tecnico e poi il quiz.\n"]) is not None)
prova("#386 scatta: pacchetto senza cornice rossa", lib.pacchetto_pubb_mancante("PUBB 6 con formato giusto", [PACCHETTO.replace(ROSSO, "")]) is not None)
prova("#386 passa: il docente non ha chiesto PUBB", lib.pacchetto_pubb_mancante("dammi il kit", [LUNGA]) is None)
prova("#386 passa: «Annotato.» (risposta breve)", lib.pacchetto_pubb_mancante("PUBB 3", ["Annotato."]) is None)
prova("#386 passa: PUBB n NON riuscito con il pacchetto sotto", lib.pacchetto_pubb_mancante(
    "PUBB 2", ["PUBB 2 NON riuscito: pubblica a mano\n" + PACCHETTO]) is None)
prova("#386 la frase dice che cosa manca", "cornice rossa" in (lib.pacchetto_pubb_mancante("PUBB 4", [LUNGA]) or ""))

# ================= #388 PDF predefinito
prova("#388 scatta: xlsx senza formato chiesto", lib.file_non_pdf_non_richiesto(["/x/ARGOMENTI.xlsx"], "mandami l'ultima versione del file ARGOMENTI") is not None)
prova("#388 scatta: docx, md, csv", all(lib.file_non_pdf_non_richiesto(["/x/a" + e], "dammi il file") for e in (".docx", ".md", ".csv")))
prova("#388 passa: il docente chiede Excel", lib.file_non_pdf_non_richiesto(["/x/A.xlsx"], "mandami l'Excel degli argomenti") is None)
prova("#388 passa: il docente chiede il modello", lib.file_non_pdf_non_richiesto(["/x/m.docx"], "dammi il Documento modello") is None)
prova("#388 passa: PDF", lib.file_non_pdf_non_richiesto(["/x/A.pdf"], "mandami il file ARGOMENTI") is None)
prova("#388 passa: xlsx e PDF dello stesso nome nel turno", lib.file_non_pdf_non_richiesto(["/x/A.xlsx", "/x/A.pdf"], "mandami il file") is None)
prova("#388 passa: immagine", lib.file_non_pdf_non_richiesto(["/x/schermo.png"], "fammi vedere") is None)
prova("#388 passa: dentro un kit (righe rosse)", lib.file_non_pdf_non_richiesto(["/x/m.docx"], "dammi", [PACCHETTO.replace(BLU, ROSSO)]) is None)
prova("#388 la frase nomina il file e il PDF", "A.xlsx" in lib.file_non_pdf_non_richiesto(["/x/A.xlsx"], "mandami il file") and
      "PDF" in lib.file_non_pdf_non_richiesto(["/x/A.xlsx"], "mandami il file"))

# ================= #389 cruscotto di oggi
OGGI = "2026-11-23"


def pub_finto(letto_il=None, dato_iso=None, lezione_oggi=True, classe="1INF"):
    d = tempfile.mkdtemp()
    c = classe.lower()
    os.makedirs(d + "/docs/" + c)
    os.makedirs(d + "/docs/avanzamento")
    json.dump({"v": 1, "letto_il": letto_il}, open(d + "/docs/%s/live.json" % c, "w"))
    if dato_iso:
        json.dump({"dato": {"iso": dato_iso}}, open(d + "/docs/%s/dati-cruscotto.json" % c, "w"))
    json.dump({"lezioni": {OGGI: [{"classe": classe, "disciplina": "Lab"}] if lezione_oggi else []}},
              open(d + "/docs/avanzamento/orario-lezioni.json", "w"))
    return d


def adesso(hhmm):
    return datetime.datetime.fromisoformat("%sT%s:00" % (OGGI, hhmm)).replace(tzinfo=cm.TZ_ROMA)


MSG = "Il cruscotto della 1INF è pronto: lo vedi in tempo reale."
prova("#389 lib: dato di oggi in live.json -> None", lib.cruscotto_senza_dati_di_oggi("1INF", OGGI, pub_finto(letto_il="2026-11-23T09:15:00+01:00")) is None)
prova("#389 lib: dato di oggi in dati-cruscotto.json -> None", lib.cruscotto_senza_dati_di_oggi("1INF", OGGI, pub_finto(dato_iso="2026-11-23T08:40:00+01:00")) is None)
prova("#389 lib: dato del 05/11 -> frase", "05/11" in (lib.cruscotto_senza_dati_di_oggi("1INF", OGGI, pub_finto(dato_iso="2026-11-05T13:26:15+01:00")) or ""))
prova("#389 lib: letto_il vuoto e nessun altro dato -> frase", lib.cruscotto_senza_dati_di_oggi("1INF", OGGI, pub_finto()) is not None)
prova("#389 lib: dato UTC delle 23:30 del giorno prima = 00:30 di oggi a Roma -> None", lib.cruscotto_senza_dati_di_oggi(
    "1INF", OGGI, pub_finto(letto_il="2026-11-22T23:30:00+00:00")) is None)
prova("#389 messaggio: «il cruscotto è pronto» riconosciuto", lib.messaggio_dice_cruscotto_pronto(MSG)[0] == ["1INF"])
prova("#389 messaggio: «cruscotto 2INF aggiornato» riconosciuto", lib.messaggio_dice_cruscotto_pronto("Il cruscotto 2INF è aggiornato.")[0] == ["2INF"])
prova("#389 messaggio: avviso «DATI VECCHI» non scatta", lib.messaggio_dice_cruscotto_pronto("Il cruscotto 1INF è pronto ma DATI VECCHI (ultimo dato 05/11).")[0] == [])
prova("#389 messaggio: «non è ancora aggiornato» non scatta", lib.messaggio_dice_cruscotto_pronto("Il cruscotto 1INF non è ancora aggiornato.")[0] == [])
prova("#389 messaggio: senza «cruscotto» non scatta", lib.messaggio_dice_cruscotto_pronto("Il compito della 1INF è pronto.")[0] == [])
prova("#389 hook: pronto + dato del 05/11 + lezione cominciata -> scatta", cm.controllo_cruscotto_oggi(
    MSG, adesso=adesso("11:30"), pub=pub_finto(dato_iso="2026-11-05T13:26:15+01:00")) is not None)
prova("#389 hook: pronto + dato di oggi -> passa", cm.controllo_cruscotto_oggi(
    MSG, adesso=adesso("11:30"), pub=pub_finto(dato_iso="2026-11-23T11:20:00+01:00")) is None)
prova("#389 hook: pronto ma oggi la classe non ha lezione -> passa", cm.controllo_cruscotto_oggi(
    MSG, adesso=adesso("11:30"), pub=pub_finto(dato_iso="2026-11-05T13:26:15+01:00", lezione_oggi=False)) is None)
prova("#389 hook: pronto ma sono le 07:00 (prima della lezione) -> passa", cm.controllo_cruscotto_oggi(
    MSG, adesso=adesso("07:00"), pub=pub_finto(dato_iso="2026-11-05T13:26:15+01:00")) is None)
prova("#389 hook: pronto con avviso «DATI VECCHI» -> passa", cm.controllo_cruscotto_oggi(
    "Il cruscotto 1INF è pronto, DATI VECCHI.", adesso=adesso("11:30"), pub=pub_finto(dato_iso="2026-11-05T13:26:15+01:00")) is None)
prova("#389 hook: messaggio senza cruscotto -> passa", cm.controllo_cruscotto_oggi(
    "Fatto, tutto in ordine.", adesso=adesso("11:30"), pub=pub_finto()) is None)

# ================= i controlli (kk) e (ll) sul processo vero: trascrizione finta
tr = T + "/tr.jsonl"


def trascrizione(docente, blocchi):
    righe = [{"type": "user", "uuid": "u1", "origin": {"kind": "human"}, "message": {"content": docente}}]
    for i, b in enumerate(blocchi):
        if b[0] == "T":
            righe.append({"type": "assistant", "uuid": "a%d" % i, "message": {"content": [{"type": "text", "text": b[1]}]}})
        else:
            righe.append({"type": "assistant", "uuid": "b%d" % i, "message": {"content": [
                {"type": "tool_use", "id": "t%d" % i, "name": b[1], "input": b[2]}]}})
            righe.append({"type": "user", "uuid": "r%d" % i, "message": {"content": [
                {"type": "tool_result", "tool_use_id": "t%d" % i, "content": "ok"}]}})
    with open(tr, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


trascrizione("PUBB 4", [("T", LUNGA)])
prova("#386 hook: PUBB 4 senza pacchetto -> blocca", cm.controllo_pacchetto_pubb(LUNGA, {"transcript_path": tr}) is not None)
trascrizione("PUBB 4", [("T", PACCHETTO)])
prova("#386 hook: PUBB 4 con pacchetto -> passa", cm.controllo_pacchetto_pubb(PACCHETTO, {"transcript_path": tr}) is None)
trascrizione("che ore sono?", [("T", LUNGA)])
prova("#386 hook: nessun PUBB -> passa", cm.controllo_pacchetto_pubb(LUNGA, {"transcript_path": tr}) is None)
trascrizione("mandami l'ultima versione del file ARGOMENTI", [("T", "Ecco.\n" + BLU), ("U", "SendUserFile", {"files": ["/x/ARGOMENTI.xlsx"]}), ("T", BLU)])
prova("#388 hook: xlsx non chiesto -> blocca", cm.controllo_file_predefinito(BLU, {"transcript_path": tr}) is not None)
trascrizione("mandami l'excel degli argomenti", [("T", "Ecco.\n" + BLU), ("U", "SendUserFile", {"files": ["/x/ARGOMENTI.xlsx"]}), ("T", BLU)])
prova("#388 hook: xlsx chiesto -> passa", cm.controllo_file_predefinito(BLU, {"transcript_path": tr}) is None)
trascrizione("mandami il file ARGOMENTI", [("T", "Ecco.\n" + BLU), ("U", "SendUserFile", {"files": ["/x/ARGOMENTI.pdf"]}), ("T", BLU)])
prova("#388 hook: PDF -> passa", cm.controllo_file_predefinito(BLU, {"transcript_path": tr}) is None)
prova("#388 hook: nessuna trascrizione -> passa", cm.controllo_file_predefinito(BLU, {}) is None)

# memoria: lo stesso errore non si segnala due volte nello stesso turno
cm.STATO_FORMATO = T + "/stato.json"
trascrizione("PUBB 4", [("T", LUNGA)])
a = cm.controllo_pacchetto_pubb(LUNGA, {"transcript_path": tr})
b = cm.controllo_pacchetto_pubb(LUNGA, {"transcript_path": tr})
prova("memoria: primo giro segnala, secondo nello stesso turno tace", a is not None and b is None)
cm.STATO_FORMATO = ""

print("%d/%d" % (ok, tot))
sys.exit(0 if ok == tot else 1)
