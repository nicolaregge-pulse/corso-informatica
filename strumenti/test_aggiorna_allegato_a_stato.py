# -*- coding: utf-8 -*-
"""Prova di aggiorna_allegato_a_stato.py su un dato FINTO (nessun file del repository viene toccato) e prova di idempotenza.
Uso: python3 strumenti/test_aggiorna_allegato_a_stato.py   -> stampa OK o il primo controllo fallito."""
import hashlib, json, os, subprocess, sys, tempfile
AQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aggiorna_allegato_a_stato.py")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(dati, out, ora, pdf=False):
    cmd = [sys.executable, AQ, "--dati", dati, "--out", out, "--ora", ora] + ([] if pdf else ["--no-pdf"])
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout + r.stderr


def scrivi(p, obj):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def controlla(cond, msg):
    if not cond:
        print("FALLITO:", msg)
        sys.exit(1)


def main():
    tmp = tempfile.mkdtemp()
    dati, out = os.path.join(tmp, "dati"), os.path.join(tmp, "out")
    os.makedirs(dati)
    scrivi(os.path.join(dati, "registro-allegati.json"), {"1INF": {"blocchi": {"8": ["Regge", "Gruppo finto", "   – Voce uno", "   – Voce due"]}}})
    scrivi(os.path.join(dati, "svolto-2026-27.json"), {"1INF": ["Voce uno"]})
    scrivi(os.path.join(dati, "competenze.json"), {"1INF": {"8": "Titolo finto della competenza 8"}})
    open(os.path.join(dati, "FIRME-REGISTRO-2026-27.md"), "w", encoding="utf-8").write("# finto\n1. Ora 8-9, 1INF: FIRMATA, argomento «Argomento finto due».\n2. Ora 9-10: «Argomento senza voce».\n")
    open(os.path.join(dati, "ARGOMENTI-SVOLTI-2026-27.md"), "w", encoding="utf-8").write("# finto\n")
    cop = {"lezioni": [{"id": "x1", "classe": "1INF", "data": "2026-12-01", "ora": "8-9", "titolo": "Argomento finto due", "file": "firme", "fonte": "firmata alle 08:10, FIRME-REGISTRO"}],
           "copertura": [{"classe": "1INF", "voce": "Voce due", "stato": "fatto", "lezioni": ["x1"]}]}
    scrivi(os.path.join(dati, "copertura-allegato-a.json"), cop)
    st = os.path.join(out, "stato-allegato-a.json")

    # 1) ora 08:30: la lezione non e finita -> Voce due resta DA FARE; prima versione 1.0
    o = run(dati, out, "2026-12-01T08:30")
    controlla("versione 1.0 (NUOVA)" in o and "FATTO 1, DA FARE 1" in o, "prima versione: " + o)
    controlla("Argomento senza voce" in o, "titolo firmato senza voce non segnalato")
    controlla("da confermare a fine ora" in open(os.path.join(out, "ALLEGATO-A-STATO-DEL-PROGRAMMA-v1.0.html"), encoding="utf-8").read(), "nota ora non finita")
    # 2) idempotenza: stesso dato, stessa ora -> nessun cambio, file identici byte per byte
    h = {f: sha(os.path.join(out, f)) for f in os.listdir(out)}
    o = run(dati, out, "2026-12-01T08:30")
    controlla("invariata" in o, "rilancio: versione cambiata " + o)
    controlla(h == {f: sha(os.path.join(out, f)) for f in os.listdir(out)}, "rilancio: file diversi")
    # 3) stesso dato ma ore 09:05: la lezione e finita -> 1.1, FATTO 2, riga di changelog
    o = run(dati, out, "2026-12-01T09:05")
    controlla("versione 1.1 (NUOVA)" in o and "FATTO 2, DA FARE 0" in o, "bump 1.1: " + o)
    s = json.load(open(st, encoding="utf-8"))
    controlla(len(s["changelog"]) == 2 and "Voce due" in s["changelog"][1]["righe"][0], "changelog: " + str(s["changelog"]))
    # 4) idempotenza dopo il cambio
    h = {f: sha(os.path.join(out, f)) for f in os.listdir(out)}
    o = run(dati, out, "2026-12-01T09:05")
    controlla("invariata" in o and h == {f: sha(os.path.join(out, f)) for f in os.listdir(out)}, "rilancio dopo 1.1 non idempotente")
    o = run(dati, out, "2026-12-01T17:00")
    controlla("invariata" in o, "un'ora dopo senza cambi di stato non deve alzare la versione: " + o)
    # 5) fonte non trovata: il titolo non c'e nelle fonti -> la voce NON diventa FATTO e lo strumento segnala il problema
    cop["lezioni"][0]["titolo"] = "Titolo che non esiste"
    scrivi(os.path.join(dati, "copertura-allegato-a.json"), cop)
    o = run(dati, out, "2026-12-01T17:00")
    controlla("PROBLEMA" in o and "versione 1.2 (NUOVA)" in o and "FATTO 1, DA FARE 1" in o, "fonte mancante: " + o)
    # 6) con il PDF: due rilanci senza cambi -> PDF identico (non rigenerato)
    out2 = os.path.join(tmp, "out2")
    cop["lezioni"][0]["titolo"] = "Argomento finto due"
    scrivi(os.path.join(dati, "copertura-allegato-a.json"), cop)
    o = run(dati, out2, "2026-12-01T09:05", pdf=True)
    p = os.path.join(out2, "ALLEGATO-A-STATO-DEL-PROGRAMMA-v1.0.pdf")
    controlla(os.path.exists(p) and os.path.getsize(p) > 2000, "PDF non creato: " + o)
    a = sha(p)
    run(dati, out2, "2026-12-01T09:05", pdf=True)
    controlla(a == sha(p), "PDF cambiato al rilancio")
    print("OK: prima versione 1.0, rilancio invariato (file identici), bump 1.1 con changelog, nessun bump senza cambi di stato, fonte mancante segnalata, PDF stabile")


main()
