# -*- coding: utf-8 -*-
"""Gioco della 1INF «Acchiappa la talpa»: un personaggio accettato -> una versione nuova (merge), con changelog lungo.

Ogni personaggio arriva come Pull Request (richiesta), ha il suo ramo e, dopo il controllo del prof, entra con il merge.
Lo script aggiorna, tutto insieme:
  1. docs/giochi/talpa-1inf/talpe/tNN.jpg  (immagine ridotta a 320x320)
  2. docs/giochi/talpa-1inf/talpe/elenco.json  (i personaggi del gioco, con la versione in cui sono entrati)
  3. docs/giochi/talpa-1inf/versioni/versioni.json  (la storia: ramo, PR, chi è entrato, tutti i presenti, changelog lungo)
  4. docs/1inf-backlog/backlog.json  (la voce del backlog, con la versione in cui è entrata)
Sulle pagine pubbliche il nome è «Nome I.» (iniziale del cognome), come in tutte le pagine della 1INF.

Uso:
  python3 strumenti/talpa_versione.py --nome "Mario Rossi" --immagine cartoon.jpg --descrizione "testo del ragazzo" \
      [--pr 3] [--arrivo 09:35] [--foto-ok] [--secondo]
  python3 strumenti/talpa_versione.py --inizio     (crea la v1.0, il fork con la sola talpa originale)
"""
import argparse, datetime, json, os, re, unicodedata
from PIL import Image

QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIOCO = os.path.join(QUI, "docs", "giochi", "talpa-1inf")
F_ELENCO = os.path.join(GIOCO, "talpe", "elenco.json")
F_VERS = os.path.join(GIOCO, "versioni", "versioni.json")
F_BACK = os.path.join(QUI, "docs", "1inf-backlog", "backlog.json")
REGOLE = "30 secondi di partita, 9 buchi (3 righe e 3 colonne), una talpa alla volta che resta su per 0,9 secondi, un punto per ogni talpa presa, la classifica online alla fine"


def leggi(f, vuoto):
    try: return json.load(open(f, encoding="utf-8"))
    except Exception: return vuoto


def scrivi(f, d):
    os.makedirs(os.path.dirname(f), exist_ok=True)
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def breve(nome):
    p = nome.split()
    return p[0].capitalize() + (" " + p[-1][0].upper() + "." if len(p) > 1 else "")


def slug(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def adesso():
    t = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
    return t.strftime("%d/%m/%Y"), t.strftime("%H:%M")


def inizio():
    data, ora = adesso()
    scrivi(F_ELENCO, {"versione": "v1.0", "talpe": []})
    scrivi(F_VERS, [{
        "versione": "v1.0", "nome": "Il fork della 1INF", "data": data, "ora": ora, "ramo": "main (fork di «Acchiappa la talpa»)",
        "pr": "", "autore": "il prof", "entrati": [], "presenti": [{"chi": "La talpa originale", "file": "", "dal": "v1.0"}],
        "riassunto": {"it": "Si parte: la classe ha la sua copia (fork) del gioco «Acchiappa la talpa», con la sola talpa originale.",
                      "ar": "البداية: للصف نسخته (fork) من لعبة «اصطد الخُلد»، مع الخُلد الأصلي فقط.",
                      "zh": "开始：全班有了自己的「打地鼠」游戏副本（fork），里面只有原来的地鼠。"},
        "cambi": [
            "Il prof ha fatto una copia (fork) del gioco «Acchiappa la talpa», fatto con Godot, per la 1INF. La copia è della classe: il gioco originale resta com'era, al sicuro.",
            "Nella copia è stata aggiunta una sola cosa nuova: il gioco legge l'elenco dei personaggi della classe (talpe/elenco.json) e fa uscire dai buchi i loro personaggi. All'inizio l'elenco è vuoto, quindi esce solo la talpa originale.",
            "Il gioco funziona nel browser, sul computer e sul telefono (si tocca la talpa con il dito).",
        ],
        "file": ["talpa-1inf/ (la copia del progetto Godot)", "docs/giochi/talpa-1inf/ (il gioco esportato per il browser)", "talpe/elenco.json (vuoto)"],
        "invariato": "Tutte le regole del gioco: " + REGOLE + ".",
        "tipo": "Versione di partenza: v1.0.",
    }])
    print("v1.0 creata")


def aggiungi(a):
    data, ora = adesso()
    elenco = leggi(F_ELENCO, {"versione": "v1.0", "talpe": []})
    vers = leggi(F_VERS, [])
    if not vers: raise SystemExit("prima: --inizio")
    ultima = vers[-1]["versione"]
    maj, mi = ultima[1:].split(".")[:2]
    nuova = f"v{maj}.{int(mi) + 1}"
    chi = a.chi or breve(a.nome)
    quanti_suoi = sum(1 for t in elenco["talpe"] if t["chi"] == chi)
    n = len(elenco["talpe"]) + 1
    nome_file = f"t{n:02d}.jpg"
    im = Image.open(a.immagine).convert("RGB"); lato = min(im.size)
    im = im.crop(((im.width - lato) // 2, (im.height - lato) // 2, (im.width + lato) // 2, (im.height + lato) // 2)).resize((320, 320))
    im.save(os.path.join(GIOCO, "talpe", nome_file), quality=88)
    ramo = f"personaggio-{slug(chi)}" + (f"-{quanti_suoi + 1}" if quanti_suoi else "")
    pr = a.pr or (sum(1 for v in vers if v.get("pr")) + 1)
    numero = "secondo" if quanti_suoi == 1 else "terzo" if quanti_suoi == 2 else f"{quanti_suoi + 1}°" if quanti_suoi else "primo"
    elenco["talpe"].append({"file": nome_file, "chi": chi, "dal": nuova, "descrizione": a.descrizione})
    elenco["versione"] = nuova
    prima = len(vers[-1]["presenti"])
    presenti = vers[-1]["presenti"] + [{"chi": chi + (f" ({numero} personaggio)" if quanti_suoi else ""), "file": "talpe/" + nome_file, "dal": nuova}]
    cambi = [
        f"Da dove arriva: dalla Pull Request n. {pr} di {chi}, arrivata alle {a.arrivo or ora} con la richiesta «Ecco il mio personaggio, mettilo nel gioco». Per questa richiesta è stato aperto il ramo «{ramo}»: lì il personaggio è stato preparato senza toccare il gioco di tutti.",
        f"Che cosa entra: il {numero} personaggio di {chi}, descritto così con le sue parole: «{a.descrizione}».",
        "Il controllo del prof: " + ("la foto di partenza era adatta (si vede la testa, si capisce chi è, c'è solo lui); " if a.foto_ok else "") +
        "nel buco si vede bene la testa del personaggio e dal personaggio si capisce chi è. Il prof ha detto sì e ha fatto il merge: il ramo «" + ramo + "» è stato unito al gioco della classe.",
        f"Come cambia il gioco: prima i personaggi che potevano uscire dai buchi erano {prima}, adesso sono {len(presenti)}. Ogni volta che esce una talpa, il gioco sceglie a caso fra i personaggi della classe (e ogni tanto fa uscire la talpa originale): adesso anche quello di {chi}.",
        f"Che cosa è cambiato nei file: è stata AGGIUNTA l'immagine talpe/{nome_file} (320 x 320 punti) ed è stata AGGIUNTA una riga nell'elenco talpe/elenco.json. Nessun file è stato cancellato e nessun personaggio degli altri è stato toccato: regola «aggiungere sì, cancellare no».",
    ]
    vers.append({
        "versione": nuova, "nome": f"Entra il personaggio di {chi}", "data": data, "ora": ora, "ramo": ramo, "pr": f"PR {pr}", "autore": chi,
        "entrati": [{"chi": chi, "file": "talpe/" + nome_file, "descrizione": a.descrizione}], "presenti": presenti,
        "riassunto": {"it": f"Entra il personaggio di {chi}: adesso nel gioco ci sono {len(presenti)} personaggi.",
                      "ar": f"تدخل شخصية {chi}: الآن في اللعبة {len(presenti)} شخصيات.",
                      "zh": f"{chi} 的角色加入了：现在游戏里有 {len(presenti)} 个角色。"},
        "cambi": cambi,
        "file": [f"aggiunto talpe/{nome_file}", "aggiunta una riga in talpe/elenco.json"],
        "invariato": "Le regole del gioco: " + REGOLE + ". E tutti i personaggi che c'erano già.",
        "tipo": f"Versione minor: si aggiunge un pezzo senza cambiare come funziona il gioco, quindi sale il numero dopo il punto ({ultima} → {nuova}).",
    })
    scrivi(F_ELENCO, elenco); scrivi(F_VERS, vers)
    b = leggi(F_BACK, {"aggiornato": "", "voci": []})
    b["voci"].append({"ora": f"{data[:5]} {a.arrivo or ora}", "alunno": chi, "pr": f"PR {pr} talpa", "richiesta": f"Il mio personaggio nel gioco della talpa: {a.descrizione}",
                      "file": True, "peso": 2, "motivo": "si aggiunge un personaggio", "fatto": f"Talpa {nuova}", "no": "", "pos": len(b["voci"]) + 1})
    b["aggiornato"] = f"{data[:5]}/{data[6:]} {ora}"
    scrivi(F_BACK, b)
    print(nuova, chi, nome_file, ramo)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--inizio", action="store_true"); p.add_argument("--nome"); p.add_argument("--immagine"); p.add_argument("--descrizione", default="")
    p.add_argument("--pr", type=int); p.add_argument("--chi", help="nome da mostrare, se diverso da «Nome I.»"); p.add_argument("--arrivo"); p.add_argument("--foto-ok", action="store_true")
    a = p.parse_args()
    inizio() if a.inizio else aggiungi(a)
