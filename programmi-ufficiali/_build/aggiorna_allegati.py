#!/usr/bin/env python3
"""Aggiorna la parte di Regge nell'Allegato A più recente, senza mai toccare il lavoro degli altri docenti (14/10/2026).

Il problema: il file dell'Allegato A lo modificano più persone (gli altri docenti a scuola, Nicola, Claude). Se si lavora
su una copia vecchia e poi la si ricarica, si cancella il lavoro degli altri: un «mischione».
La regola: la parte di Regge non vive nel file Word. Vive in PROGRAMMI-DI-MASSIMA-2026-27.md. Il file Word si prende
SEMPRE nella versione più recente della scuola, questo script ci rimette dentro la nostra parte, e il file torna subito a
scuola. Così in giro c'è un solo file vero e la finestra in cui due persone lavorano sulla stessa copia dura pochi minuti.

Che cosa fa, per ogni file:
  1. riconosce la classe dalla tabella delle annualità (riga 2026-2027: I = 1INF, II = 2INF, III = 3INF, IV = 4TI);
  2. nella riga di quest'anno toglie il vecchio blocco «Regge», se c'è, e ci rimette quello aggiornato: giallo il previsto, bianco il già svolto (svolto-2026-27.json);
  3. se qualcuno ha cambiato a mano il nostro blocco verde nel Word, si FERMA e mostra la differenza (niente sovrascritture);
  4. dice che cosa hanno cambiato gli altri docenti dall'ultima volta;
  5. controlla, riaprendo il file salvato, che il testo degli altri sia identico a prima: se no, butta il file e si ferma.
Uso: python3 programmi-ufficiali/_build/aggiorna_allegati.py FILE.docx [FILE.docx ...]
     python3 programmi-ufficiali/_build/aggiorna_allegati.py --verifica FILE.docx ...   (controllo del file che sta a scuola)
"""
import difflib, json, os, re, sys
from datetime import datetime, timedelta, timezone
import docx
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml.ns import qn

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from allegati_comune import CLASSI, COLORE, CART, leggi_programma, numero_competenza, par_dopo, cella_anno  # noqa: E402

REGISTRO = os.path.join(CART, 'registro-allegati.json')
USCITA = os.path.join(CART, 'consegna')
PER_ANNO = {'I': '03', 'II': '04', 'III': '05', 'IV': '06'}


def classe_del_file(d):
    for r in d.tables[0].rows[1:]:
        c = [x.text.strip() for x in r.cells]
        if len(c) > 1 and c[1] == '2026-2027' and c[0] in PER_ANNO:
            return PER_ANNO[c[0]]
    raise SystemExit('Non trovo la riga 2026-2027 nella tabella delle annualità: è davvero un Allegato A di quest\'anno?')


def tutto_verde(p):
    """Solo per i file preparati prima del 14/10 sera: il blocco di quest'anno era rosa o verde."""
    runs = [r for r in p.runs if r.text.strip()]
    return bool(runs) and all(r.font.highlight_color in (WD_COLOR_INDEX.PINK, WD_COLOR_INDEX.BRIGHT_GREEN) for r in runs)


SVOLTO = os.path.join(CART, 'svolto-2026-27.json')


def svolto():
    """Le voci già svolte e firmate sul registro, per classe: vanno in bianco (senza evidenziatore)."""
    return json.load(open(SVOLTO)) if os.path.exists(SVOLTO) else {}


# etichette degli altri docenti negli anni scorsi: il blocco «Regge» finisce dove ne comincia una
ALTRI_DOCENTI = {'meles', 'prof. meles', 'panaccione', 'erba'}


def colora_pregresso(d, rx):
    """Colora di VERDE la parte di Regge degli anni scorsi (righe degli anni prima di questo): da «Regge» fino
    all'etichetta di un altro docente o alla fine della cella. Il testo non cambia, solo il colore. Restituisce le righe colorate."""
    n, viste = 0, set()
    for tab in d.tables[1:]:
        for r in tab.rows:
            c = r.cells[0]
            if c._tc in viste: continue
            viste.add(c._tc)
            ps = c.paragraphs
            et = ps[0].text.strip() if ps else ''
            if re.match(rx, c.text.strip(), re.I) or not re.match(r'^(I|II|III|IV)\s+anno', et, re.I): continue
            dentro = False
            for p in ps:
                t = p.text.strip()
                if t == 'Regge': dentro = True
                elif t.lower() in ALTRI_DOCENTI or t.startswith('Prof.'):
                    dentro = False
                    for ru in p.runs:  # il verde è solo di Regge: l'etichetta di un altro docente in verde torna senza colore
                        if ru.font.highlight_color == WD_COLOR_INDEX.BRIGHT_GREEN: ru.font.highlight_color = None
                if dentro and t:
                    for ru in p.runs:
                        if ru.text.strip() and ru.font.highlight_color != WD_COLOR_INDEX.BRIGHT_GREEN:
                            ru.font.highlight_color = WD_COLOR_INDEX.BRIGHT_GREEN
                    n += 1
    return n


def celle_di_quest_anno(d, rx):
    """(numero competenza, cella) di ogni competenza, nella riga di quest'anno."""
    for tab in d.tables[1:]:
        n = numero_competenza(tab)
        if not n: continue
        cella, _ = cella_anno(tab, rx)
        if cella is not None: yield n, cella


def togli_blocco(cella, atteso=None):
    """Toglie il blocco «Regge» di quest'anno e restituisce il suo testo (righe).
    Il blocco si riconosce dal testo che lo script ci aveva messo (registro), perché ora le righe svolte sono in bianco;
    per i file preparati prima del 14/10 sera si riconosce dal colore (rosa o verde)."""
    ps = cella.paragraphs
    for i, p in enumerate(ps):
        if p.text.strip() != 'Regge': continue
        if atteso and [q.text for q in ps[i:i + len(atteso)]] == atteso:
            blocco = ps[i:i + len(atteso)]
        elif tutto_verde(p):
            blocco = [p]
            for q in ps[i + 1:]:
                if q.text.strip() and tutto_verde(q): blocco.append(q)
                else: break
        elif atteso:
            return [q.text for q in ps[i:i + len(atteso)]]  # c'è un blocco «Regge» ma non è come l'avevo messo: lo segnalo, non lo tocco
        else:
            continue
        righe = [q.text for q in blocco]
        for q in blocco:
            if q is ps[0]:
                for r in list(q.runs): r._r.getparent().remove(r._r)
            else:
                q._p.getparent().remove(q._p)
        return righe
    return []


def testo_di_tutti(d):
    """Tutto il testo del documento, cella per cella (le celle unite contano una volta)."""
    righe, viste = [p.text for p in d.paragraphs], set()
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                if c._tc in viste: continue
                viste.add(c._tc)
                righe += [p.text for p in c.paragraphs]
    return righe


def metti_blocco(cella, ha_etichetta, moduli, fatte=()):
    """Scrive «Regge» e i moduli con le sotto-voci: giallo = previsto, bianco = già svolto e firmato sul registro.
    Un modulo è bianco quando tutte le sue sotto-voci sono svolte; «Regge» è bianco quando lo è tutto il blocco."""
    fatte = set(fatte)
    col = lambda ok: None if ok else COLORE
    tutto = all(m['titolo'] in fatte or all(x in fatte for x in m['sotto']) for m in moduli)
    p0, righe = cella.paragraphs[0], ['Regge']
    if not ha_etichetta and p0.text.strip() == '':
        r = p0.add_run('Regge'); r.bold = True; r.font.highlight_color = col(tutto); ultimo = p0
    else:
        ultimo = par_dopo(p0, 'Regge', True, col(tutto))
    for m in moduli:
        mod_fatto = m['titolo'] in fatte or (m['sotto'] and all(x in fatte for x in m['sotto']))
        ultimo = par_dopo(ultimo, m['titolo'], False, col(mod_fatto)); righe.append(m['titolo'])
        for x in m['sotto']:
            ultimo = par_dopo(ultimo, '   – ' + x, False, col(mod_fatto or x in fatte)); righe.append('   – ' + x)
    return righe


def aggiorna(path, prog, registro):
    d = docx.Document(path)
    sec = classe_del_file(d)
    _, rx, nome = CLASSI[sec]
    moduli = prog[sec]
    prima = registro.get(nome, {})
    vecchi, manuali = {}, []
    for n, cella in celle_di_quest_anno(d, rx):
        atteso = prima.get('blocchi', {}).get(n)
        righe = togli_blocco(cella, atteso)
        if righe:
            vecchi[n] = righe
            if atteso and atteso != righe:
                manuali.append((n, atteso, righe))
    if manuali:
        print('\n%s: FERMO. Il blocco «Regge» di quest\'anno è stato cambiato a mano nel Word:' % nome)
        for n, atteso, righe in manuali:
            print('  competenza %s' % n)
            for l in difflib.unified_diff(atteso, righe, 'come l\'avevo messo', 'come è adesso', lineterm='', n=0): print('    ' + l)
        print('  Le modifiche vanno portate nel programma (PROGRAMMI-DI-MASSIMA-2026-27.md), poi si rilancia.')
        return None
    verdi = colora_pregresso(d, rx)
    altri = testo_di_tutti(d)
    cambi_altri = []
    if prima.get('altri'):
        cambi_altri = [l for l in difflib.unified_diff(prima['altri'], altri, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
    blocchi = {}
    for n, cella in celle_di_quest_anno(d, rx):
        mie = [m for m in moduli if n in m['comp']]
        if mie:
            _, ha_et = cella_anno(next(t for t in d.tables[1:] if cella._tc in [c._tc for r in t.rows for c in r.cells]), rx)
            blocchi[n] = metti_blocco(cella, ha_et, mie, svolto().get(nome, []))
    os.makedirs(USCITA, exist_ok=True)
    ora = datetime.now(timezone(timedelta(hours=2)))
    out = os.path.join(USCITA, '%s_Allegato-A-%s-2026-27_Regge.docx' % (ora.strftime('%Y%m%d-%H%M'), nome))
    d.save(out)
    # controllo finale: riapro il file, tolgo i nostri blocchi, il resto deve essere identico a prima
    d2 = docx.Document(out)
    for n, cella in celle_di_quest_anno(d2, rx): togli_blocco(cella, blocchi.get(n))
    if testo_di_tutti(d2) != altri:
        os.remove(out)
        raise SystemExit('%s: ERRORE nel controllo finale, il testo degli altri non torna. File buttato, niente consegna.' % nome)
    registro[nome] = {'quando': ora.strftime('%d/%m/%Y %H:%M'), 'da': os.path.basename(path), 'file': os.path.basename(out),
                      'blocchi': blocchi, 'altri': altri}
    print('\n%s: OK -> consegna/%s' % (nome, os.path.basename(out)))
    print('  competenze con la parte di Regge: %s' % ', '.join(sorted(blocchi, key=lambda x: float(x.split('.')[0]))))
    print('  blocchi vecchi tolti e rimessi: %d · testo degli altri docenti: identico (controllato)' % len(vecchi))
    print('  parte di Regge degli anni scorsi in verde: %d righe' % verdi)
    if prima.get('altri'):
        print('  cambiamenti degli altri docenti dall\'ultima volta (%s): %d righe' % (prima['quando'], len(cambi_altri)))
        for l in cambi_altri[:15]: print('    ' + l[:110])
    return out


def verifica(path, prog, registro):
    """Controllo del file che sta a scuola dopo il caricamento: la nostra parte c'è ed è quella giusta, il resto è com'era."""
    d = docx.Document(path)
    sec = classe_del_file(d)
    _, rx, nome = CLASSI[sec]
    atteso = registro.get(nome, {})
    problemi, trovati = [], {}
    for n, cella in celle_di_quest_anno(d, rx):
        righe = togli_blocco(cella, atteso.get('blocchi', {}).get(n))
        if righe: trovati[n] = righe
    for n, righe in atteso.get('blocchi', {}).items():
        if n not in trovati: problemi.append('competenza %s: manca la parte di Regge' % n)
        elif trovati[n] != righe: problemi.append('competenza %s: la parte di Regge è diversa da quella preparata' % n)
    for n in trovati:
        if n not in atteso.get('blocchi', {}): problemi.append('competenza %s: c\'è una parte di Regge in più' % n)
    altri = testo_di_tutti(d)
    diff = [l for l in difflib.unified_diff(atteso.get('altri', []), altri, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
    print('\n%s, file «%s»' % (nome, os.path.basename(path)))
    if not problemi and not diff:
        print('  TUTTO A POSTO: la parte di Regge è quella preparata alle %s e il testo degli altri è identico.' % atteso.get('quando'))
    for p in problemi: print('  PROBLEMA: ' + p)
    if diff:
        print('  Il testo degli altri è cambiato rispetto al file preparato (%d righe):' % len(diff))
        for l in diff[:20]: print('    ' + l[:110])
    return not problemi and not diff


if __name__ == '__main__':
    if len(sys.argv) < 2: raise SystemExit(__doc__)
    prog = leggi_programma()
    registro = json.load(open(REGISTRO)) if os.path.exists(REGISTRO) else {}
    if sys.argv[1] == '--verifica':
        ok = all([verifica(f, prog, registro) for f in sys.argv[2:]])
        raise SystemExit(0 if ok else 1)
    for f in sys.argv[1:]:
        aggiorna(f, prog, registro)
    json.dump(registro, open(REGISTRO, 'w'), ensure_ascii=False, indent=1)
