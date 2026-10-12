#!/usr/bin/env python3
"""Congela una versione del treno su Godot (strumento del prof / di Claude, non per i ragazzi).

Dopo l'esportazione Web (docs/giochi/treno-2inf-godot/index.html + index.pck + index.wasm ...)
copia la versione attuale in docs/giochi/treno-2inf-godot/versioni/vX.Y/ :
  - index.pck  (il gioco: codice + dati di questa versione)
  - index.html (la pagina, che usa il motore index.js / index.wasm della cartella principale)
e aggiunge la riga in versioni/versioni.json.

Uso:  python3 strumenti/congela_versione.py 1.0 "Nome della versione" "Cosa cambia"
Il numero deve essere uguale a quello scritto in dati/versione.json.
"""
import json
import pathlib
import re
import shutil
import sys

QUI = pathlib.Path(__file__).resolve().parent.parent          # treno-2inf-godot/
WEB = QUI.parent / "docs" / "giochi" / "treno-2inf-godot"


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    numero, nome, cambi = sys.argv[1], sys.argv[2], sys.argv[3]
    dichiarato = json.loads((QUI / "dati" / "versione.json").read_text(encoding="utf-8"))["versione"]
    if dichiarato != numero:
        sys.exit(f"dati/versione.json dice {dichiarato}, non {numero}: prima si cambia il numero, poi si esporta, poi si congela.")
    dest = WEB / "versioni" / f"v{numero}"
    if dest.exists():
        sys.exit(f"{dest} esiste già: una versione consegnata non si cambia (si fa la versione dopo).")
    dest.mkdir(parents=True)
    shutil.copy2(WEB / "index.pck", dest / "index.pck")
    h = (WEB / "index.html").read_text(encoding="utf-8")
    h = re.sub(r"<title>(.*?)</title>", lambda m: f"<title>v{numero} · {m.group(1)}</title>", h, count=1)
    for f in ("index.icon.png", "index.apple-touch-icon.png", "index.png", "index.js"):
        h = h.replace(f'"{f}"', f'"../../{f}"')
    h = h.replace('"executable":"index"', '"executable":"../../index","mainPack":"index.pck"')
    (dest / "index.html").write_text(h, encoding="utf-8")
    elenco = WEB / "versioni" / "versioni.json"
    righe = json.loads(elenco.read_text(encoding="utf-8")) if elenco.exists() else []
    righe.append({"versione": f"v{numero}", "nome": nome, "cambi": cambi, "data": "", "commit": "", "cartella_codice": "treno-2inf-godot"})
    elenco.write_text(json.dumps(righe, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Congelata v{numero} in {dest}")


if __name__ == "__main__":
    main()
