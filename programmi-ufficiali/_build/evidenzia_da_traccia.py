#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evidenziazione dell'Allegato A dalla TRACCIA (fatto / da fare), versione 1.0 (23/11/2026).

Che cosa fa: prende il Word piu' recente della scuola (parte «Regge» della riga di quest'anno), legge lo stato di ogni voce da
<riservato>/dati/allegato-a-traccia/stato-traccia.json (strumento strumenti/argomenti_allegato_a.py) e cambia SOLO il colore
dell'evidenziatore, secondo la legenda di COME-SI-AGGIORNA-ALLEGATO-A.md v1.3/v1.4:
  - voce FATTA  -> nessuna evidenziazione (bianco);
  - voce DA FARE (anche se solo in parte, righe «a» FATTA e «b» DA FARE) -> giallo;
  - modulo: bianco se tutte le sue voci sono FATTE, altrimenti giallo; «Regge»: bianco se tutto il blocco e' FATTO, altrimenti giallo;
  - voci in «Da chiedere al docente» (nota che comincia con «DA CHIEDERE AL DOCENTE»): colore lasciato COM'E' (R7.6, non presumere);
    un modulo o «Regge» che dipendono da una voce lasciata restano come sono, a meno che una voce decisa DA FARE li renda gialli.
Non cambia il testo, non aggiunge ne' toglie voci (R5.2), non tocca le parti degli altri docenti ne' il verde degli anni scorsi.
Controlla alla fine che il testo del documento sia identico e che fuori dal blocco di Regge i colori siano identici.
Uso: python3 evidenzia_da_traccia.py --classe 1INF --docx FILE.docx --out FILE_NUOVO.docx [--riservato DIR] [--json RESOCONTO.json]
Il pubblico non contiene nomi di allievi: lo script legge solo voci dell'Allegato A.
"""
import argparse, json, os, re, sys
import docx
from docx.enum.text import WD_COLOR_INDEX as W

RISERVATO = os.environ.get('ARGOMENTI_RISERVATO', '/home/user/corso-informatica-riservato')
PER_ANNO = {'1INF': r'^I\s+anno', '2INF': r'^II\s+anno', '3INF': r'^III\s+anno', '4TI': r'^(IV\s+anno|4\s+anno|4°\s+annualit)'}
GIALLO = W.YELLOW
# Voci di Sicurezza FATTE per la traccia (firma sul registro) ma lasciate «da decidere dal docente» da svolto-2026-27.json v1.2 e
# INDICE-DOCUMENTI 5b (18/11/2026, R5.2bis): fonti discordanti, quindi il colore resta com'e' (R7.6). Si tolgono da qui dopo la risposta del docente.
LASCIA_DECIDERE = {'1INF': ['6ª ora: rischi meccanici ed elettrici generali'],
                   '2INF': ['5ª ora: rischio infortuni', '6ª ora: rischi meccanici ed elettrici generali'], '3INF': [], '4TI': []}


def norma(t):
    """Titolo del modulo senza l'eventuale nota tra parentesi finale (es. «(si tiene se la classe ci arriva)»)."""
    return re.sub(r'\s*\([^)]*\)\s*$', '', t.strip())


def colore(p):
    cs = {r.font.highlight_color for r in p.runs if r.text.strip()}
    if not cs: return 'vuoto'
    if len(cs) > 1: return 'misto'
    c = next(iter(cs))
    return {None: 'bianco', GIALLO: 'giallo'}.get(c, str(c))


def imposta(p, giallo):
    for r in p.runs:
        if r.text.strip(): r.font.highlight_color = GIALLO if giallo else None


def stati(traccia, classe):
    """(modulo, testo) -> 'F' | 'D' | '?' ; modulo -> {stati}. Controlla la coerenza tra le competenze."""
    voci = {}
    for x in traccia['classi'][classe]:
        ignota = (x.get('da_confermare_nota') or '').startswith('DA CHIEDERE AL DOCENTE')
        ignota = ignota or x['testo'] in LASCIA_DECIDERE.get(classe, [])
        s = '?' if ignota else ('F' if x['stato_allegato'] == 'FATTO' else 'D')
        voci.setdefault((norma(x['modulo']), x['testo']), set()).add(s)
    out = {}
    for k, v in voci.items():
        # una voce divisa a/b ha una riga FATTA e una DA FARE ma stato_allegato e' sempre DA FARE: qui v ha un solo valore
        if len(v) > 1: raise SystemExit('Stati incoerenti per %r: %s' % (k, v))
        out[k] = next(iter(v))
    return out


def celle_regge(d, rx):
    """Celle della riga di quest'anno che contengono un paragrafo «Regge»."""
    viste = set()
    for ti, tab in enumerate(d.tables):
        for r in tab.rows:
            c = r.cells[0]
            if c._tc in viste: continue
            viste.add(c._tc)
            ps = c.paragraphs
            if not any(p.text.strip() == 'Regge' for p in ps): continue
            et = ps[0].text.strip() if ps else ''
            if not re.match(rx, et, re.I): continue  # solo la riga di quest'anno
            yield ti, c


def testo_tutti(d):
    righe, viste = [p.text for p in d.paragraphs], set()
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                if c._tc in viste: continue
                viste.add(c._tc)
                righe += [p.text for p in c.paragraphs]
    return righe


def colori_tutti(d):
    out, viste = [], set()
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                if c._tc in viste: continue
                viste.add(c._tc)
                out += [(p.text, colore(p)) for p in c.paragraphs]
    return out


def elabora(path, out, classe, traccia):
    d = docx.Document(path)
    st = stati(traccia, classe)
    prima = testo_tutti(d)
    cambi, fuori_traccia, mancanti, lasciate = [], [], set(st), []
    blocchi_par = set()
    for ti, c in celle_regge(d, PER_ANNO[classe]):
        ps = c.paragraphs
        i = next(k for k, p in enumerate(ps) if p.text.strip() == 'Regge')
        # blocco: Regge, poi moduli e sotto-voci conosciuti
        blocco = [('regge', None, None, ps[i])]
        mod = None
        for p in ps[i + 1:]:
            t = p.text
            if not t.strip(): break  # il blocco finisce alla prima riga vuota
            if t.startswith('   – '):
                if mod is None: break
                blocco.append(('voce', mod, t[5:].strip(), p))
            else:
                mod = norma(t); blocco.append(('modulo', mod, None, p))
        stato_voci = {}
        for tipo, m, v, p in blocco:
            if tipo == 'voce':
                s = st.get((m, v))
                if s is None: fuori_traccia.append((m, v)); s = '?'
                else: mancanti.discard((m, v))
                stato_voci.setdefault(m, []).append(s)
        for tipo, m, v, p in blocco:
            blocchi_par.add(id(p._p))
            prima_c = colore(p)
            if tipo == 'voce':
                s = st.get((m, v), '?')
                nuovo = None if s == '?' else ('bianco' if s == 'F' else 'giallo')
                if s == '?': lasciate.append((m, v, prima_c))
            elif tipo == 'modulo':
                ss = stato_voci.get(m, [])
                if 'D' in ss: nuovo = 'giallo'
                elif '?' in ss or not ss: nuovo = None
                else: nuovo = 'bianco'
            else:
                tutte = [s for l in stato_voci.values() for s in l]
                nuovo = 'giallo' if 'D' in tutte else (None if '?' in tutte else 'bianco')
            if nuovo is None or nuovo == prima_c: continue
            imposta(p, nuovo == 'giallo')
            cambi.append({'competenza_cella': ti, 'tipo': tipo, 'modulo': m or '', 'voce': v or (p.text.strip() if tipo != 'voce' else ''), 'prima': prima_c, 'dopo': nuovo})
    d.save(out)
    # controlli: testo identico; fuori dai blocchi di Regge i colori identici
    d0, d2 = docx.Document(path), docx.Document(out)
    assert testo_tutti(d2) == prima, 'il testo e\' cambiato: file da buttare'
    c0, c2 = colori_tutti(d0), colori_tutti(d2)
    nd = sum(1 for a, b in zip(c0, c2) if a != b)
    assert len(c0) == len(c2) and nd == len(cambi), 'colori cambiati fuori dal previsto (%d contro %d)' % (nd, len(cambi))
    return {'classe': classe, 'cambi': cambi, 'lasciate_com_e': lasciate, 'voci_traccia_non_trovate_nel_word': sorted(mancanti), 'voci_word_non_in_traccia': fuori_traccia,
            'paragrafi_regge': len(blocchi_par)}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--classe', required=True, choices=list(PER_ANNO))
    ap.add_argument('--docx', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--riservato', default=RISERVATO); ap.add_argument('--json')
    a = ap.parse_args()
    tr = json.load(open(os.path.join(a.riservato, 'dati/allegato-a-traccia/stato-traccia.json'), encoding='utf-8'))
    if os.path.exists(a.out): raise SystemExit('Il file di uscita esiste gia\': non si sovrascrive (R11).')
    r = elabora(a.docx, a.out, a.classe, tr)
    if a.json: json.dump(r, open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%s: %d righe cambiate; lasciate come sono %d; voci traccia non trovate nel Word %d; voci Word non in traccia %d' % (
        a.classe, len(r['cambi']), len(r['lasciate_com_e']), len(r['voci_traccia_non_trovate_nel_word']), len(r['voci_word_non_in_traccia'])))
