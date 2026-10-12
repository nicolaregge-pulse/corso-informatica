"""Toglie ogni testo in cinese/arabo/bengalese da una pagina per una classe SOLO ITALIANO (2INF).

Uso: python3 strumenti/solo_italiano.py FILE.html [FILE2.html ...]
Toglie gli elementi con classe zh / t-zh / ar / t-ar / bn / t-bn e poi CONTROLLA:
se resta anche un solo carattere cinese, arabo o bengalese si ferma con errore (niente push).
"""
import re
import sys

CLASSI = r"(?:t-)?(?:zh|ar|bn)"
STRANI = re.compile(r"[؀-ۿঀ-৿　-〿一-鿿＀-￯]")


def pulisci(h):
    for tag in ("p", "span", "div", "li", "td"):
        h = re.sub(rf"(?:<br>)?<{tag} [^>]*?class=['\"]{CLASSI}['\"][^>]*>.*?</{tag}>", "", h, flags=re.S)
    h = re.sub(r"<tr>\s*</tr>", "", h)
    # pezzi in altra lingua attaccati con « · » dentro un testo italiano
    h = re.sub(r" · [^<>·]*[\u0600-\u06ff\u0980-\u09ff\u3000-\u303f\u4e00-\u9fff\uff00-\uffef][^<>]*", "", h)
    return h


def controlla(h, nome):
    resti = STRANI.findall(h)
    if resti:
        riga = h[:STRANI.search(h).start()].count("\n") + 1
        sys.exit(f"ERRORE {nome}: restano {len(resti)} caratteri non italiani (riga {riga}). NON pubblicare.")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        h = pulisci(open(f, encoding="utf-8").read())
        controlla(h, f)
        open(f, "w", encoding="utf-8").write(h)
        print("OK solo italiano:", f)
