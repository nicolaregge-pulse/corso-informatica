#!/usr/bin/env python3
# bobina-automatica.py — v1.1, 7 ottobre 2026 (v1.1: allegati salvati anche se esclusi da .gitignore)
#
# Scrive la BOBINA (trascrizione integrale) di ogni giorno di una sessione di
# Claude Code e la mette su Git (commit + push). Regola di Nicola Regge del
# 07/10/2026: "tutte le chat Claude Code devono avere le bobine di tutti i
# giorni, backuppate".
#
# Come parte:
#   1. da solo, come hook "Stop" (.claude/settings.json): a ogni fine risposta
#      riceve su stdin il JSON con transcript_path e session_id;
#   2. a mano, per la sessione in corso:
#        python3 .claude/hooks/bobina-automatica.py --sessione-corrente
#
# Cosa fa:
#   1. legge tutti i file .jsonl della sessione (~/.claude/projects/*/<id>.jsonl);
#   2. scrive un file per giorno (ora italiana): <dest>/AAAA-MM-GG_bobina_<id8>.md
#      con tutti i messaggi di Nicola e di Claude, in ordine e per intero;
#      le operazioni tecniche fra parentesi quadre; chiavi -> [CHIAVE RIMOSSA];
#   3. salva in <dest>/allegati/<id8>/ i file caricati nella sessione
#      (foto originali, PDF, zip) e le immagini incollate in chat;
#   4. fa commit solo di <dest> e push in background.
#
# La destinazione si legge da .claude/bobina.json nella cartella del repository:
#   {"dest": ["bobine"]}            -> cartella dentro questo repository
#   {"dest": ["../altro-repo/bobine", "/home/user/altro-repo/bobine"]}
#                                    -> la prima che esiste (repo gemello)
# Se nessuna destinazione esiste, non scrive niente e lo segnala.
#
# Non blocca mai Claude: esce sempre con 0.

import base64, glob, hashlib, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone

try:
    from zoneinfo import ZoneInfo
    ROMA = ZoneInfo('Europe/Rome')
except Exception:  # pragma: no cover
    from datetime import timedelta
    ROMA = timezone(timedelta(hours=1))

VERSIONE = '1.1'
LIMITE_FILE = 95 * 1024 * 1024  # GitHub rifiuta i file oltre 100 MB

SEGRETI = [
    r'sk-ant-[A-Za-z0-9_\-]{8,}',
    r'AIza[0-9A-Za-z_\-]{20,}',
    r'\bAQ\.[A-Za-z0-9_\-\.]{10,}',
    r'gh[pousr]_[A-Za-z0-9]{20,}',
    r'github_pat_[A-Za-z0-9_]{20,}',
    r'xox[baprs]-[A-Za-z0-9\-]{10,}',
]
SEGRETO_CHIAVE = r'(?i)\b(password|passwd|token|api[_-]?key|secret)(\s*[:=]\s*)[\'"]?[^\s\'"]{6,}'


def avviso(msg):
    """Messaggio che compare nella sessione, senza bloccarla."""
    print(json.dumps({'systemMessage': 'Bobina automatica: ' + msg}, ensure_ascii=False))


def pulisci_segreti(t):
    for p in SEGRETI:
        t = re.sub(p, '[CHIAVE RIMOSSA]', t)
    return re.sub(SEGRETO_CHIAVE, lambda m: m.group(1) + m.group(2) + '[CHIAVE RIMOSSA]', t)


def pulisci(t):
    t = re.sub(r'<system-reminder>.*?</system-reminder>', '', t, flags=re.S)
    t = re.sub(r'\[Image: source: [^\]]*\]', '', t)
    return t.strip()


def ora_roma(ts):
    return datetime.fromisoformat(ts.replace('Z', '+00:00')).astimezone(ROMA)


def radice_repo(partenza):
    try:
        r = subprocess.run(['git', '-C', partenza, 'rev-parse', '--show-toplevel'],
                           capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or None
    except Exception:
        return None


def file_sessione(session_id, transcript_path):
    files = set(glob.glob(os.path.expanduser('~/.claude/projects/*/%s.jsonl' % session_id)))
    if transcript_path and os.path.exists(transcript_path):
        files.add(transcript_path)
    return sorted(files)


def leggi_righe(files):
    visti, righe = set(), []
    for f in files:
        for riga in open(f, encoding='utf-8', errors='replace'):
            try:
                d = json.loads(riga)
            except Exception:
                continue
            u = d.get('uuid') or hashlib.sha1(riga.encode()).hexdigest()
            if u in visti:
                continue
            visti.add(u)
            if d.get('timestamp'):
                righe.append(d)
    righe.sort(key=lambda d: d['timestamp'])
    return righe


def descrivi_strumento(b):
    inp = b.get('input', {}) or {}
    desc = (inp.get('description') or inp.get('file_path') or inp.get('query')
            or inp.get('skill') or inp.get('url') or inp.get('pattern') or '')
    nome = b.get('name', '?')
    return '[%s%s]' % (nome, (' — ' + str(desc).replace('\n', ' ')[:160]) if desc else '')


def messaggi(righe, cartella_allegati, rel_allegati):
    """Restituisce la lista (chi, datetime, testo, modello) e salva le immagini incollate."""
    out, n_img = [], 0
    for d in righe:
        if d.get('isSidechain'):
            continue
        t = d.get('type')
        ts = ora_roma(d['timestamp'])
        if t == 'user':
            cont = d.get('message', {}).get('content')
            if d.get('isCompactSummary') or d.get('isMeta'):
                continue
            if isinstance(cont, str):
                testo = pulisci(cont)
                blocchi = []
            else:
                blocchi = cont or []
                if any(b.get('type') == 'tool_result' for b in blocchi):
                    continue
                testo = '\n\n'.join(pulisci(b.get('text', '')) for b in blocchi
                                    if b.get('type') == 'text' and pulisci(b.get('text', '')))
            if testo.startswith('Base directory for this skill:') or testo in ('Tool loaded.',):
                continue
            immagini = [b for b in blocchi if b.get('type') == 'image']
            righe_img = []
            gia_caricata = '/.claude/uploads/' in json.dumps(cont, ensure_ascii=False)
            for b in immagini:
                src = b.get('source', {})
                if src.get('type') != 'base64' or gia_caricata:
                    righe_img.append('[immagine: vedi allegati della sessione]')
                    continue
                n_img += 1
                ext = (src.get('media_type', 'image/png').split('/')[-1]).replace('jpeg', 'jpg')
                nome = '%s_incollata_%02d.%s' % (ts.strftime('%Y%m%d_%H%M%S'), n_img, ext)
                p = os.path.join(cartella_allegati, nome)
                if not os.path.exists(p):
                    os.makedirs(cartella_allegati, exist_ok=True)
                    with open(p, 'wb') as f:
                        f.write(base64.b64decode(src.get('data', '')))
                righe_img.append('[immagine: %s/%s]' % (rel_allegati, nome))
            if righe_img:
                testo = (testo + '\n\n' if testo else '') + '\n'.join(righe_img)
            if testo:
                out.append(('NICOLA', ts, testo, None))
        elif t == 'attachment' and (d.get('attachment') or {}).get('type') == 'queued_command':
            p = d['attachment'].get('prompt')
            if isinstance(p, list):
                testo = '\n\n'.join(pulisci(b.get('text', '')) for b in p if b.get('type') == 'text')
            else:
                testo = pulisci(p or '')
            if testo:
                out.append(('NICOLA', ts, testo + '\n\n[inviato mentre Claude lavorava]', None))
        elif t == 'assistant':
            modello = d.get('message', {}).get('model')
            for b in d.get('message', {}).get('content', []) or []:
                if b.get('type') == 'text' and b.get('text', '').strip():
                    out.append(('CLAUDE', ts, b['text'].strip(), modello))
                elif b.get('type') == 'tool_use':
                    out.append(('CLAUDE', ts, descrivi_strumento(b), modello))
    return out


def copia_caricati(session_id, cartella_allegati):
    """Copia i file caricati nella sessione (originali, non ridimensionati)."""
    copiati, saltati = 0, []
    for f in glob.glob(os.path.expanduser('~/.claude/uploads/%s/*' % session_id)):
        if not os.path.isfile(f):
            continue
        if os.path.getsize(f) > LIMITE_FILE:
            saltati.append(os.path.basename(f))
            continue
        dst = os.path.join(cartella_allegati, os.path.basename(f))
        if not os.path.exists(dst):
            os.makedirs(cartella_allegati, exist_ok=True)
            shutil.copy2(f, dst)
            copiati += 1
    return copiati, saltati


def scrivi_giorni(msgs, dest, nome_repo, sid8):
    giorni = {}
    for m in msgs:
        giorni.setdefault(m[1].strftime('%Y-%m-%d'), []).append(m)
    scritti = []
    for giorno, lista in sorted(giorni.items()):
        modelli = sorted({m[3] for m in lista if m[3] and m[3] != '<synthetic>'})
        nn = sum(1 for m in lista if m[0] == 'NICOLA')
        righe = [
            '# BOBINA — %s — %s' % (nome_repo, datetime.strptime(giorno, '%Y-%m-%d').strftime('%d/%m/%Y')),
            '',
            '*Trascrizione integrale automatica della sessione Claude Code `%s`, giorno %s. '
            'Tutti i messaggi di Nicola e di Claude, in ordine e per intero, con l\'ora italiana. '
            'I dettati sono come sono arrivati, refusi compresi. Le operazioni tecniche sono fra parentesi quadre; '
            'le loro uscite non sono riportate. Chiavi e password sostituite con [CHIAVE RIMOSSA].*' % (sid8, giorno),
            '',
            '*Modello: %s. Messaggi di Nicola: %d. Generata da bobina-automatica.py v%s.*'
            % (', '.join(modelli) or 'non registrato', nn, VERSIONE),
            '', '---', '',
        ]
        prec = None
        for chi, ts, testo, _ in lista:
            testo = pulisci_segreti(testo)
            if chi == prec and testo.startswith('['):
                righe.append(testo)
                righe.append('')
            else:
                righe.append('**%s** (%s):' % (chi, ts.strftime('%H:%M')))
                righe.append('')
                righe.append(testo)
                righe.append('')
            prec = chi
        contenuto = '\n'.join(righe).rstrip() + '\n'
        p = os.path.join(dest, '%s_bobina_%s.md' % (giorno, sid8))
        vecchio = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if vecchio != contenuto:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(contenuto)
            scritti.append(p)
    return scritti


def git_salva(dest, sid8):
    repo = radice_repo(dest)
    if not repo:
        return 'la cartella %s non è dentro un repository Git' % dest
    rel = os.path.relpath(dest, repo)
    def g(*a, **k):
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, timeout=60, **k)
    g('add', '--', rel)
    # gli allegati sono originali di Nicola: si salvano anche se .gitignore esclude PDF e immagini
    g('add', '-f', '--', os.path.join(rel, 'allegati')) if os.path.isdir(os.path.join(dest, 'allegati')) else None
    if not g('diff', '--cached', '--quiet', '--', rel).returncode:
        return None  # niente di nuovo
    oggi = datetime.now(ROMA).strftime('%Y-%m-%d %H:%M')
    r = g('commit', '-q', '-m', 'Bobina automatica %s (sessione %s)' % (oggi, sid8), '--', rel)
    if r.returncode:
        return 'commit non riuscito: ' + (r.stderr or r.stdout).strip()[:200]
    if os.environ.get('BOBINA_PUSH_SINCRONO'):
        # usato dal controllo "tutto versionato" del corso: il push deve essere finito prima
        try:
            g('push', '-q', 'origin', 'HEAD')
        except Exception:
            pass
        return None
    # push in background: se il remoto è più avanti fallisce in silenzio e riprova al giro dopo
    subprocess.Popen('git -C "%s" push -q origin HEAD >/dev/null 2>&1' % repo, shell=True,
                     start_new_session=True)
    return None


def main():
    manuale = '--sessione-corrente' in sys.argv
    dati = {}
    if not manuale:
        try:
            dati = json.loads(sys.stdin.read() or '{}')
        except Exception:
            dati = {}
    session_id = dati.get('session_id')
    transcript = dati.get('transcript_path')
    if manuale or not session_id:
        tutti = glob.glob(os.path.expanduser('~/.claude/projects/*/*.jsonl'))
        if not tutti:
            avviso('non trovo il file della sessione.')
            return
        transcript = max(tutti, key=os.path.getmtime)
        session_id = os.path.basename(transcript)[:-6]
    sid8 = session_id[:8]

    base = os.environ.get('CLAUDE_PROJECT_DIR') or dati.get('cwd') or os.getcwd()
    repo = radice_repo(base) or base
    conf_p = os.path.join(repo, '.claude', 'bobina.json')
    conf = json.load(open(conf_p)) if os.path.exists(conf_p) else {'dest': ['bobine']}
    dest = None
    for c in conf.get('dest', []):
        p = c if os.path.isabs(c) else os.path.normpath(os.path.join(repo, c))
        # la cartella va bene solo se sta dentro un repository Git già clonato
        a = p
        while a and not os.path.isdir(a):
            a = os.path.dirname(a)
        r = radice_repo(a) if a else None
        if r and (p == r or p.startswith(r + os.sep)):
            dest = p
            break
    if not dest:
        avviso('nessuna cartella di destinazione trovata (%s). %s'
               % (', '.join(conf.get('dest', [])), conf.get('se_manca', '')))
        return
    os.makedirs(dest, exist_ok=True)
    nome_repo = conf.get('nome') or os.path.basename(repo)
    rel_all = 'allegati/%s' % sid8
    cartella_all = os.path.join(dest, rel_all)

    files = file_sessione(session_id, transcript)
    if not files:
        avviso('file della sessione %s non trovato.' % sid8)
        return
    msgs = messaggi(leggi_righe(files), cartella_all, rel_all)
    scrivi_giorni(msgs, dest, nome_repo, sid8)
    _, saltati = copia_caricati(session_id, cartella_all)
    errore = git_salva(dest, sid8)
    if saltati:
        avviso('file troppo grandi per GitHub, non salvati: ' + ', '.join(saltati))
    if errore:
        avviso(errore)
    if manuale:
        print('Bobine scritte in %s' % dest)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:  # non bloccare mai la sessione
        avviso('errore %s: %s' % (type(e).__name__, e))
    sys.exit(0)
