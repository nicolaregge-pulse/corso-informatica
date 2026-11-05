#!/usr/bin/env python3
"""Inserisce le foto del docente nella «Mini guida PC» al posto degli schemi e rigenera i PDF con una versione nuova.

Uso:
  python3 strumenti/inserisci_foto_dispensa.py --versione 1.1 FOTO-02-06=/percorso/foto.jpg [FOTO-03-03=/altra.jpg@x,y,w,h] ...
  python3 strumenti/inserisci_foto_dispensa.py --versione 1.1 --elenco elenco.txt      (righe: «FOTO-02-06 /percorso/foto.jpg [x,y,w,h]»)
  --prova DIR   lavora solo le immagini e le scrive in DIR: non tocca la dispensa e non rigenera niente.

Per ogni foto:
  1. la raddrizza secondo l'orientamento EXIF del telefono;
  2. la ritaglia se dopo il file c'è @x,y,w,h (pixel della foto già raddrizzata);
  3. la porta a massimo 1600 px sul lato lungo;
  4. la salva in JPEG SENZA dati EXIF (niente posizione GPS, niente modello del telefono)
     in classe-2/dispense/img-mini-guida-pc/FOTO-CC-NN.jpg e la segna in foto.json.
Poi rilancia strumenti/genera_dispensa_pc.py --versione V (ragazzi, 3INF bangla, docente, FOTO-DA-INSERIRE.md).
Gli schemi .png restano: le versioni già date continuano a vederli (R11).
Le foto vanno anche nella dispensa PUBBLICA dei ragazzi: niente volti, nomi, password sullo schermo (R1).
"""
import argparse
import json
import os
import re
import subprocess
import sys

from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera_dispensa_pc as D  # noqa: E402

MAX = 1600


def leggi_voci(a):
    voci = []
    for x in a.foto:
        m = re.match(r'^(FOTO-\d\d-\d\d)=(.+?)(?:@(\d+),(\d+),(\d+),(\d+))?$', x)
        if not m:
            sys.exit(f'Non capisco «{x}»: scrivi FOTO-02-06=/percorso/foto.jpg oppure ...@x,y,w,h')
        voci.append((m.group(1), m.group(2), tuple(map(int, m.groups()[2:])) if m.group(3) else None))
    if a.elenco:
        for riga in open(a.elenco, encoding='utf-8'):
            p = riga.split()
            if not p or p[0].startswith('#'):
                continue
            rit = tuple(map(int, p[2].split(','))) if len(p) > 2 else None
            voci.append((p[0], p[1], rit))
    return voci


def lavora(src, dest, ritaglio):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    if ritaglio:
        x, y, w, h = ritaglio
        if x < 0 or y < 0 or x + w > im.width or y + h > im.height or w < 50 or h < 50:
            sys.exit(f'Ritaglio {ritaglio} fuori dalla foto {src} ({im.width}x{im.height})')
        im = im.crop((x, y, x + w, y + h))
    im.thumbnail((MAX, MAX), Image.LANCZOS)
    pulita = Image.new('RGB', im.size, 'white')   # immagine nuova: nessun metadato si porta dietro
    pulita.paste(im.convert('RGBA'), mask=im.convert('RGBA').split()[3])
    pulita.save(dest, 'JPEG', quality=85, optimize=True, progressive=True)
    return pulita.size


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument('foto', nargs='*', help='FOTO-CC-NN=file[@x,y,w,h]')
    a.add_argument('--versione', help='versione nuova della dispensa (per esempio 1.1)')
    a.add_argument('--elenco', help='file con una riga per foto: ID file [x,y,w,h]')
    a.add_argument('--prova', help='cartella di prova: lavora solo le immagini, non rigenera')
    a = a.parse_args()
    voci = leggi_voci(a)
    if not voci:
        sys.exit('Nessuna foto. ' + __doc__)
    validi = {p['id']: p for p in D.TUTTI_PASSI}
    for i, f, _ in voci:
        if i not in validi:
            sys.exit(f'{i} non esiste. Gli ID sono in riservato report/2026-11-05/FOTO-DA-INSERIRE.md')
        if not os.path.isfile(f):
            sys.exit(f'File non trovato: {f}')
    if not a.prova and not (a.versione and re.match(r'^\d+\.\d+$', a.versione)):
        sys.exit('Serve --versione nuova (per esempio 1.1): una versione già data non si riscrive (R11).')
    out = a.prova or D.IMG
    os.makedirs(out, exist_ok=True)
    fatte = {}
    for i, f, rit in voci:
        nome = i + '.jpg'
        w, h = lavora(f, os.path.join(out, nome), rit)
        fatte[i] = nome
        print(f'{i}: {os.path.basename(f)} -> {nome} ({w}x{h}, senza EXIF) · {validi[i]["titolo"]}')
    if a.prova:
        print('PROVA: dispensa non toccata.')
        return
    fv = D.foto_vere()
    fv.update(fatte)
    json.dump(dict(sorted(fv.items())), open(D.FOTO_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    nota = 'foto del docente al posto degli schemi: ' + ', '.join(sorted(fatte))
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'genera_dispensa_pc.py'),
                    '--versione', a.versione, '--nota', nota], check=True)
    print(f'FATTO: {len(fatte)} foto, dispensa v{a.versione}. Ora: registra la riga in INDICE-DOCUMENTI.md, poi commit e push '
          '(pubblico: classe-2/dispense e classe-3/dispense; riservato: report/2026-11-05 con git add -f).')


if __name__ == '__main__':
    main()
