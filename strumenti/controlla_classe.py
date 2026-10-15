#!/usr/bin/env python3
"""Controllo automatico PRIMA di pubblicare (15/10/2026, Nicola: «voglio che le cose funzionino al primo colpo»).
Per ogni file (comando del ponte, compito in coda, pagina HTML) riconosce la classe e controlla, con la scheda
della classe (strumenti/schede-classi.json):
  1. le lingue: niente caratteri di una lingua che la classe non usa (cinese, arabo, bengalese);
  2. il corso di Classroom: il course_id deve essere quello della classe;
  3. la regola 15: nelle pagine per i ragazzi niente «copia… apri il Modulo… incolla».
Esce con errore se trova un problema: il file NON si pubblica finché non è corretto.
Uso: python3 strumenti/controlla_classe.py FILE [FILE ...]"""
import json, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
SCHEDE = json.load(open(os.path.join(QUI, 'schede-classi.json')))
SCRITTURE = {'zh': ('cinese', re.compile(r'[一-鿿]')), 'ar': ('arabo', re.compile(r'[؀-ۿ]')), 'bn': ('bengalese', re.compile(r'[ঀ-৿]'))}
ALIAS = {a: k for k, v in SCHEDE.items() if not k.startswith('_') for a in v.get('alias', [])}


def classe_di(path, testo):
    m = re.search(r'"classe"\s*:\s*"([0-9A-Z]+)"', testo)
    c = m.group(1) if m else None
    if not c:
        m = re.search(r'(?<![0-9])([1-4](?:INF|TI))(?![A-Z])', os.path.basename(path).upper()) or re.search(r'/([1-4](?:inf|ti))[-_/]', path.lower())
        c = m.group(1).upper() if m else None
    return ALIAS.get(c, c)


def controlla(path):
    testo = open(path, encoding='utf-8', errors='ignore').read()
    c = classe_di(path, testo)
    if c not in SCHEDE:
        return []
    s, err = SCHEDE[c], []
    for lingua, (nome, rx) in SCRITTURE.items():
        if lingua not in s['lingue'] and rx.search(testo):
            err.append('%s: c\'è testo in %s, ma la %s usa solo %s' % (os.path.basename(path), nome, c, ', '.join(s['lingue'])))
    for cid in re.findall(r'"course_id"\s*:\s*"(\d+)"', testo):
        if cid != s['course_id']:
            err.append('%s: course_id %s non è quello della %s (%s)' % (os.path.basename(path), cid, c, s['course_id']))
    if path.endswith('.html') and re.search(r'(?is)copia.{0,200}apri il modulo.{0,200}(incolla|ctrl\+v)', testo):
        err.append('%s: chiede «copia, apri il Modulo, incolla»: vietato dalla regola 15' % os.path.basename(path))
    return err


if __name__ == '__main__':
    errori = [e for f in sys.argv[1:] if os.path.isfile(f) for e in controlla(f)]
    for e in errori: print('FERMO: ' + e)
    if not errori: print('Controllo classi: OK (%d file)' % len([f for f in sys.argv[1:] if os.path.isfile(f)]))
    sys.exit(1 if errori else 0)
