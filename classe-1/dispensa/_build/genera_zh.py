#!/usr/bin/env python3
"""Dispensa 1INF in cinese semplificato: dispensa-1inf-zh.md -> dispensa-1inf-zh-vX.Y.html (font WenQuanYi Zen Hei).
Uso: python3 classe-1/dispensa/_build/genera_zh.py ; poi il PDF con Chromium dall'HTML.
L'MD cinese si scrive a mano (traduzione); il generatore riusa md_a_html e il CSS di genera.py."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera

CSS = genera.CSS.replace('font-family:"DejaVu Sans","Amiri","WenQuanYi Zen Hei",sans-serif',
                         'font-family:"WenQuanYi Zen Hei","DejaVu Sans","Amiri",sans-serif').replace('line-height:1.45', 'line-height:1.6')


def main():
    md = open(os.path.join(genera.OUT, 'dispensa-1inf-zh.md'), encoding='utf8').read()
    ver = re.search(r'\*\*Versione (\d+\.\d+)\*\*', md).group(1)
    corpo = genera.md_a_html(md)
    doc = (f'<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>1INF 讲义 v{ver}</title><style>{CSS}</style></head><body>{corpo}</body></html>')
    out = os.path.join(genera.OUT, f'dispensa-1inf-zh-v{ver}.html')
    open(out, 'w', encoding='utf8').write(doc)
    print(out, len(doc) // 1024, 'KB')


if __name__ == '__main__':
    main()
