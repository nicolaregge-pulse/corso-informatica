#!/usr/bin/env python3
# bobina-automatica-v2.py — v2.0, 19/11/2026 (decisione del docente: «nella bobina deve esserci tutto, chat e allegati»). Sostituisce la v1.1 (copia: bobina-automatica-v1-backup.py).
# Novita' rispetto alla v1.1 (requisito del docente 19/11: la bobina e' la memoria completa):
#   1. USCITE DEGLI STRUMENTI: dopo ogni comando una riga «[esito HH:MM: ...]» con le prime righe dell'uscita (max 400 caratteri,
#      segreti tolti); gli errori sono marcati «[ERRORE strumento ...]»;
#   2. ALLEGATI: per ogni file caricato citato in un messaggio, una riga «[allegato: nome originale · ora · sha256 · copia: ...]»
#      ;
#   3. AGENTI: le azioni dei sotto-agenti (isSidechain) compaiono come «[agente: ...]» invece di essere saltate;
#   5. FAIL-SAFE: file scritti in modo atomico con lock, mai una bobina esistente sostituita da una piu' corta, ogni parte facoltativa
#      (allegati, agenti, indice) in try/except: se fallisce, la bobina dei messaggi si scrive lo stesso;
#   6. INGRESSO DATI: ogni file caricato e' copiato anche in dati/ingresso/<data>/ del riservato con INDICE.md/INDICE.json
#      (nome originale, ora, tipo, sha256, byte, anteprima: fogli/righe per xlsx, righe per csv/txt, pagine per pdf, «da trascrivere» per le immagini);
#   7. AGENTI: file <giorno>_agenti_<id8>.md con le azioni dei sotto-agenti (lettura incrementale, cache fuori dal repository).
#   4. intestazione: il conteggio dei messaggi di Nicola e' fatto sul testo scritto davvero.
# Prova: python3 bobina-automatica-v2.py --prova DEST   (scrive solo in DEST, niente git, niente push).
# --- testo della v1.1 ---
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

import base64, glob, hashlib, json, os, re, shutil, subprocess, sys, time
from datetime import datetime, timezone

try:
    from zoneinfo import ZoneInfo
    ROMA = ZoneInfo('Europe/Rome')
except Exception:  # pragma: no cover
    from datetime import timedelta
    ROMA = timezone(timedelta(hours=1))

VERSIONE = '2.0'
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


def _password_docente():
    """Password del docente (config/PASSPHRASE-DOCENTE.txt del riservato, 16/11/2026): se compare in chat non deve finire nelle bobine.
    La sessione parte da /home/user e usa la copia PUBBLICA di questo hook (errore #342, 16/11): si cerca anche con percorso assoluto."""
    qui = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for f in (os.path.join(qui, 'config', 'PASSPHRASE-DOCENTE.txt'),
              '/home/user/corso-informatica-riservato/config/PASSPHRASE-DOCENTE.txt'):
        try:
            return open(f, encoding='utf-8').read().strip()
        except OSError:
            continue
    return ''


def pulisci_segreti(t):
    pw = _password_docente()
    if len(pw) >= 8:
        t = re.sub(re.escape(pw), '[PASSWORD DOCENTE RIMOSSA]', t, flags=re.I)
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
    cmd = str(inp.get('command') or '').replace('\n', ' ')[:240]
    extra = (' · comando: ' + cmd) if cmd else ''
    return '[%s%s%s]' % (nome, (' — ' + str(desc).replace('\n', ' ')[:160]) if desc else '', extra)


def messaggi(righe, cartella_allegati, rel_allegati):
    """Restituisce la lista (chi, datetime, testo, modello) e salva le immagini incollate."""
    out, n_img = [], 0
    for d in righe:
        t = d.get('type')
        ts = ora_roma(d['timestamp'])
        if d.get('isSidechain'):
            if t == 'assistant':
                for b in d.get('message', {}).get('content', []) or []:
                    if b.get('type') == 'tool_use':
                        out.append(('CLAUDE', ts, '[agente: ' + descrivi_strumento(b)[1:], None))
            continue
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
                    for b in blocchi:
                        if b.get('type') == 'tool_result':
                            c = b.get('content')
                            if isinstance(c, list):
                                c = ' '.join(x.get('text', '') for x in c if isinstance(x, dict))
                            c = re.sub(r'\s+', ' ', str(c or '')).strip()[:400]
                            err = b.get('is_error')
                            out.append(('CLAUDE', ts, '[%s %s: %s]' % ('ERRORE strumento' if err else 'esito', ts.strftime('%H:%M'), c or 'nessuna uscita'), None))
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
                righe_img.append('[immagine: %s/%s · sha256 %s · da trascrivere]' % (rel_allegati, nome, hashlib.sha256(base64.b64decode(src.get('data', ''))).hexdigest()[:16]))
            if righe_img:
                testo = (testo + '\n\n' if testo else '') + '\n'.join(righe_img)
            for pth in sorted(set(re.findall(r'/\.claude/uploads/[^\s\]\)"\']+', json.dumps(cont, ensure_ascii=False)))):
                pth = os.path.expanduser('~') + pth if pth.startswith('/.claude') else '/root' + pth
                if os.path.isfile(pth):
                    hh = hashlib.sha256(open(pth, 'rb').read()).hexdigest()
                    testo = (testo + '\n\n' if testo else '') + '[allegato: %s · ricevuto %s · sha256 %s · copia: %s/%s]' % (
                        re.sub(r'^[0-9a-f]{8}-', '', os.path.basename(pth)), ts.strftime('%H:%M'), hh[:16], rel_allegati, os.path.basename(pth))
            if testo:
                out.append(('NICOLA', ts, testo, None))
        elif t == 'attachment' and (d.get('attachment') or {}).get('type') == 'inlined_image_paths':
            for pth in d['attachment'].get('paths', []):
                if os.path.isfile(pth):
                    hh = hashlib.sha256(open(pth, 'rb').read()).hexdigest()
                    out.append(('NICOLA', ts, '[allegato: %s · ricevuto %s · sha256 %s · %d byte · copia: %s/%s]' % (
                        re.sub(r'^[0-9a-f]{8}-', '', os.path.basename(pth)), ts.strftime('%H:%M'), hh[:16], os.path.getsize(pth),
                        rel_allegati, os.path.basename(pth)), None))
                else:
                    out.append(('NICOLA', ts, '[allegato: %s · ricevuto %s · file non piu\' presente sul disco]' % (os.path.basename(pth), ts.strftime('%H:%M')), None))
        elif t == 'attachment' and (d.get('attachment') or {}).get('type') == 'pdf_reference':
            a = d['attachment']
            out.append(('NICOLA', ts, '[allegato PDF: %s · ricevuto %s · %s pagine · %s byte · copia: %s/%s]' % (
                re.sub(r'^[0-9a-f]{8}-', '', os.path.basename(a.get('filename', ''))), ts.strftime('%H:%M'), a.get('pageCount'), a.get('fileSize'),
                rel_allegati, os.path.basename(a.get('filename', ''))), None))
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



NOMI_SEGRETI = ('CODICI', 'PASSPHRASE', 'PASSWORD', 'RECUPERO-ACCOUNT')


def anteprima(p):
    """Descrizione verificabile del contenuto, solo da script (le immagini restano «da trascrivere»)."""
    ext = os.path.splitext(p)[1].lower()
    try:
        if ext in ('.xlsx', '.xlsm'):
            import openpyxl
            wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
            parti = ['%s (%s righe)' % (ws.title, ws.max_row) for ws in wb.worksheets[:8]]
            return 'xlsx: %d fogli: %s' % (len(wb.worksheets), '; '.join(parti))
        if ext in ('.csv', '.txt', '.md', '.json') and os.path.getsize(p) < 30 * 1024 * 1024:
            with open(p, 'rb') as f:
                n = sum(1 for _ in f)
            prima = open(p, encoding='utf-8', errors='replace').readline().strip()[:80]
            return '%s: %d righe, prima riga «%s»' % (ext[1:], n, pulisci_segreti(prima))
        if ext == '.pdf':
            b = open(p, 'rb').read()
            return 'pdf: circa %d pagine' % len(re.findall(rb'/Type\s*/Page[^s]', b))
        if ext in ('.zip', '.docx', '.pptx'):
            import zipfile
            return '%s: %d elementi' % (ext[1:], len(zipfile.ZipFile(p).namelist()))
        if ext in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
            return 'immagine: da trascrivere (descrizione non possibile da script)'
    except Exception as e:
        return 'anteprima non riuscita (%s)' % type(e).__name__
    return 'tipo non riconosciuto'


def ingresso(session_id, radice_ingresso, tempo_max):
    """Copia ogni file caricato in <radice_ingresso>/<data>/ con INDICE.json e INDICE.md. Incrementale: salta cio' che e' gia' in indice."""
    t0 = time.time()
    nuovi = []
    giorni = {}
    for f in sorted(glob.glob(os.path.expanduser('~/.claude/uploads/%s/*' % session_id)), key=os.path.getmtime):
        if time.time() - t0 > tempo_max:
            break
        if not os.path.isfile(f) or os.path.getsize(f) > LIMITE_FILE:
            continue
        if any(x in os.path.basename(f).upper() for x in NOMI_SEGRETI):
            continue
        ts = datetime.fromtimestamp(os.path.getmtime(f), ROMA)
        giorno = ts.strftime('%Y-%m-%d')
        cart = os.path.join(radice_ingresso, giorno)
        if giorno not in giorni:
            pi = os.path.join(cart, 'INDICE.json')
            giorni[giorno] = (cart, json.load(open(pi, encoding='utf-8')) if os.path.exists(pi) else {'data': giorno, 'voci': []})
        cart, ind = giorni[giorno]
        nome = os.path.basename(f)
        if any(v['salvato'] == nome and v['byte'] == os.path.getsize(f) for v in ind['voci']):
            continue
        os.makedirs(cart, exist_ok=True)
        dst = os.path.join(cart, nome)
        if not os.path.exists(dst):
            shutil.copy2(f, dst)
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        ind['voci'].append({'nome_originale': re.sub(r'^[0-9a-f]{8}-', '', nome), 'salvato': nome, 'ora_ricezione': ts.strftime('%H:%M:%S'),
                            'tipo': os.path.splitext(nome)[1].lower().lstrip('.') or '?', 'sha256': h, 'byte': os.path.getsize(f),
                            'origine': 'chat docente (sessione %s)' % session_id[:8], 'classe': 'da indicare',
                            'contenuto': anteprima(dst)})
        nuovi.append(nome)
    for giorno, (cart, ind) in giorni.items():
        if not any(n for n in nuovi if os.path.exists(os.path.join(cart, n))) and os.path.exists(os.path.join(cart, 'INDICE.json')):
            continue
        ind['voci'].sort(key=lambda v: v['ora_ricezione'])
        tmp = os.path.join(cart, 'INDICE.json.tmp')
        json.dump(ind, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        os.replace(tmp, os.path.join(cart, 'INDICE.json'))
        with open(os.path.join(cart, 'INDICE.md'), 'w', encoding='utf-8') as f:
            f.write('# Ingresso dati %s (riservato)\n\nScritto da bobina-automatica.py v%s. Ogni file ricevuto in chat, con ora, hash e anteprima. '
                    '«da trascrivere» = immagine: descrizione non possibile da script, vedi il file.\n\n'
                    '| Ora | Nome originale | Tipo | Byte | sha256 | Classe | Contenuto | File salvato |\n|---|---|---|---|---|---|---|---|\n' % (giorno, VERSIONE))
            for v in ind['voci']:
                f.write('| %s | %s | %s | %d | %s | %s | %s | %s |\n' % (v['ora_ricezione'], v['nome_originale'], v['tipo'], v['byte'],
                        v['sha256'][:16], v['classe'], v['contenuto'], v['salvato']))
    return nuovi


def agenti(session_id, dest, sid8, cache_dir, tempo_max):
    """Azioni dei sotto-agenti: lettura incrementale dei loro transcript, cache fuori dal repository."""
    t0 = time.time()
    os.makedirs(cache_dir, exist_ok=True)
    pc = os.path.join(cache_dir, '%s-agenti.json' % sid8)
    cache = json.load(open(pc)) if os.path.exists(pc) else {}
    files = glob.glob(os.path.expanduser('~/.claude/projects/*/%s/subagents/agent-*.jsonl' % session_id))
    files.sort(key=os.path.getmtime, reverse=True)
    cambiati = 0
    for f in files:
        if time.time() - t0 > tempo_max:
            break
        sz = os.path.getsize(f)
        k = os.path.basename(f)
        if cache.get(k, {}).get('s') == sz:
            continue
        aid = k[6:14]
        ev = []
        meta = f[:-6] + '.meta.json'
        try:
            m = json.load(open(meta))
            ev.append(['', '[agente %s avviato: %s]' % (aid, str(m.get('description') or m.get('agentType') or '')[:160])])
        except Exception:
            pass
        for riga in open(f, encoding='utf-8', errors='replace'):
            try:
                d = json.loads(riga)
            except Exception:
                continue
            if not d.get('timestamp'):
                continue
            ts = d['timestamp']
            if d.get('type') == 'assistant':
                for b in d.get('message', {}).get('content', []) or []:
                    if b.get('type') == 'tool_use':
                        ev.append([ts, '[agente %s: %s' % (aid, descrivi_strumento(b)[1:])])
                    elif b.get('type') == 'text' and b.get('text', '').strip():
                        ev.append([ts, '[agente %s dice: %s]' % (aid, re.sub(r'\s+', ' ', b['text']).strip()[:300])])
            elif d.get('type') == 'user' and isinstance(d.get('message', {}).get('content'), list):
                for b in d['message']['content']:
                    if b.get('type') == 'tool_result' and b.get('is_error'):
                        c = b.get('content')
                        if isinstance(c, list):
                            c = ' '.join(x.get('text', '') for x in c if isinstance(x, dict))
                        ev.append([ts, '[agente %s ERRORE: %s]' % (aid, re.sub(r'\s+', ' ', str(c or '')).strip()[:300])])
        cache[k] = {'s': sz, 'e': ev}
        cambiati += 1
    if cambiati:
        tmp = pc + '.tmp'
        json.dump(cache, open(tmp, 'w'), ensure_ascii=False)
        os.replace(tmp, pc)
        giorni = {}
        for v in cache.values():
            for ts, t in v['e']:
                if ts:
                    o = ora_roma(ts)
                    giorni.setdefault(o.strftime('%Y-%m-%d'), []).append((o, t))
        for giorno, lista in giorni.items():
            lista.sort(key=lambda x: x[0])
            testo = '# AZIONI DEGLI AGENTI — %s (sessione %s)\n\n*Generato da bobina-automatica.py v%s: comando, ora e uscita sintetica, errori. Non e\' la trascrizione integrale degli agenti.*\n\n' % (giorno, sid8, VERSIONE)
            testo += '\n'.join('%s %s' % (o.strftime('%H:%M:%S'), pulisci_segreti(t)) for o, t in lista) + '\n'
            p = os.path.join(dest, '%s_agenti_%s.md' % (giorno, sid8))
            vecchio = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
            if len(testo) >= len(vecchio):
                tmp = p + '.tmp'
                open(tmp, 'w', encoding='utf-8').write(testo)
                os.replace(tmp, p)
    return cambiati, len(files)


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
            if vecchio and len(contenuto) < 0.9 * len(vecchio):
                # la trascrizione di partenza e' piu' corta (compattazione, file ruotato): MAI perdere la bobina esistente
                p2 = p[:-3] + '.nuova-%s.md' % datetime.now(ROMA).strftime('%H%M')
                avviso('bobina %s: la nuova e piu corta, tengo la vecchia e scrivo %s' % (os.path.basename(p), os.path.basename(p2)))
                p = p2
            tmp = p + '.tmp'
            with open(tmp, 'w', encoding='utf-8') as f:
                f.write(contenuto)
            os.replace(tmp, p)
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
    extra = [e for e in ('dati/ingresso',) if os.path.isdir(os.path.join(repo, e))]
    for e in extra:
        g('add', '-f', '--', e)  # xlsx, pdf e immagini ricevuti: sorgente, si versionano anche se .gitignore li esclude
    # gli allegati sono originali di Nicola: si salvano anche se .gitignore esclude PDF e immagini
    g('add', '-f', '--', os.path.join(rel, 'allegati')) if os.path.isdir(os.path.join(dest, 'allegati')) else None
    if not g('diff', '--cached', '--quiet', '--', rel, *extra).returncode:
        return None  # niente di nuovo
    oggi = datetime.now(ROMA).strftime('%Y-%m-%d %H:%M')
    r = g('commit', '-q', '-m', 'Bobina automatica %s (sessione %s)' % (oggi, sid8), '--', rel, *extra)
    if r.returncode:
        return 'commit non riuscito: ' + (r.stderr or r.stdout).strip()[:200]
    if os.environ.get('BOBINA_PUSH_SINCRONO'):
        # usato dal controllo "tutto versionato" del corso: il push deve essere finito prima
        # 13/10/2026: il riservato riceve di continuo le consegne dello script di Google, quindi il remoto è spesso
        # più avanti e un push semplice viene rifiutato: il controllo poi bloccava Claude per un commit fatto da
        # questo hook. Prima si riallinea (pull --rebase), poi push, fino a 3 tentativi.
        for _ in range(3):
            try:
                if g('pull', '-q', '--rebase', 'origin', 'main').returncode:
                    g('rebase', '--abort')
                if not g('push', '-q', 'origin', 'HEAD:main').returncode:
                    break
            except Exception:
                pass
        return None
    # push in background: se il remoto è più avanti fallisce in silenzio e riprova al giro dopo
    subprocess.Popen('git -C "%s" push -q origin HEAD >/dev/null 2>&1' % repo, shell=True,
                     start_new_session=True)
    return None


def main():
    prova = sys.argv[sys.argv.index('--prova') + 1] if '--prova' in sys.argv else None
    manuale = '--sessione-corrente' in sys.argv or bool(prova)
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
    if not os.path.exists(conf_p):
        # 28/10/2026: sessione avviata da /home/user (CLAUDE_PROJECT_DIR=/home/user, non è un repository):
        # si usa il repository in cui sta questo script, con percorso assoluto.
        qui = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        repo = radice_repo(qui) or qui
        conf_p = os.path.join(repo, '.claude', 'bobina.json')
    conf = json.load(open(conf_p)) if os.path.exists(conf_p) else {'dest': ['bobine']}
    dest = os.path.abspath(prova) if prova else None
    for c in ([] if prova else conf.get('dest', [])):
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
    t0 = time.time()
    try:
        import fcntl
        blocco = open(os.path.join(dest, '.bobina.lock'), 'w')
        fcntl.flock(blocco, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return  # un altro giro sta scrivendo: la bobina di questo turno la scrive lui
    except Exception:
        pass
    msgs = messaggi(leggi_righe(files), cartella_all, rel_all)
    scrivi_giorni(msgs, dest, nome_repo, sid8)
    _, saltati = copia_caricati(session_id, cartella_all)
    # parti facoltative: se falliscono la bobina dei messaggi e' gia' scritta
    try:
        r_ing = os.path.join(dest, 'ingresso-prova') if prova else os.path.join(radice_repo(dest) or dest, 'dati', 'ingresso')
        ingresso(session_id, r_ing, 10)
    except Exception as e:
        avviso('ingresso dati non riuscito (%s: %s)' % (type(e).__name__, e))
    try:
        cdir = os.path.join(dest, 'cache-prova') if prova else os.path.expanduser('~/.cache/bobina')
        agenti(session_id, dest, sid8, cdir, max(3, 22 - (time.time() - t0)))
    except Exception as e:
        avviso('azioni degli agenti non riuscite (%s: %s)' % (type(e).__name__, e))
    errore = None if prova else git_salva(dest, sid8)
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
