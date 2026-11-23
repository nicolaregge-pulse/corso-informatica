/* Test di classroom_pubblica_v1.0.gs con SERVIZI FINTI (Classroom, Drive, Fogli, UrlFetch, Proprieta, Lock, orologio). 23/11/2026.
 * Uso: node fabbrica/test_classroom_pubblica_v1.0.js      (dalla cartella del repository pubblico)
 * Prova la LOGICA e il modo di usare le API; NON prova Classroom vero (permessi, limiti, comportamento reale): vedi il progetto, capitolo 2. */
'use strict';
const fs = require('fs'), vm = require('vm'), path = require('path');
const SRC = fs.readFileSync(path.join(__dirname, 'classroom_pubblica_v1.0.gs'), 'utf8');
const PROVA5 = fs.readFileSync(path.join(__dirname, 'classroom_pubblica_prova5min_v1.0.gs'), 'utf8');
const BASE = 'https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/fabbrica/';
const ARABO = 'العربية', CINESE = '中文';
let ok = 0, ko = 0;
function t(nome, cond, extra) { if (cond) { ok++; console.log('  ok   ' + nome); } else { ko++; console.log('  FALLITO ' + nome + (extra ? ' -> ' + extra : '')); } }

function fusoParti(d) {
  const p = {}; new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Rome', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23', weekday: 'short' }).formatToParts(d).forEach(x => p[x.type] = x.value);
  return p;
}
function mondayBased(w) { return { Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6, Sun: 7 }[w]; }

function mondo(opz) {
  opz = opz || {};
  const W = { now: Date.parse(opz.ora || '2026-11-24T08:30:00Z'), files: {}, creati: [], patch: [], rimossi: [], fetch: [], cw: {}, seq: 100, props: {}, drive: {}, faults: {}, righe: [], log: [] };
  const spec = (o) => Object.assign({ id: '2026-11-24_2INF_ora2', classe: '2INF', giorno: '2026-11-24', ora: 2, titolo: '24/11 Ora 2: il CSS', descrizione: 'Oggi impari il CSS.\nApri la pagina e segui i passi.\n' + ARABO + ' ' + CINESE, allegati: [{ tipo: 'pdf', file: 'post/2026-11-24_2INF_ora2-guida.pdf', nome: 'Guida ora 2.pdf' }, { tipo: 'documento', modello_id: 'MODELLODOC1234567890AB', nome: 'Documento ora 2' }, { tipo: 'quiz', id: 'quiz-2inf-2411-ora2' }, { tipo: 'link', url: 'https://nicolaregge-pulse.github.io/corso-informatica/anteprima/2inf-24-11/' }] }, o || {});
  W.spec = spec;
  const pdf = '%PDF-1.4\n' + 'x'.repeat(300) + '\n%%EOF';
  W.files['indice.json'] = JSON.stringify({ classroom: { classi: { '2INF': 'NUOVO 2 INFO', '1INF': '1 INF 26/27' } } });
  W.files['post/2026-11-24_2INF_ora2.json'] = JSON.stringify(spec());
  W.files['post/2026-11-24_2INF_ora2-guida.pdf'] = pdf;
  W.files['post/coda.json'] = JSON.stringify({ attivo: true, richieste: [{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'r1', prova: true }] });
  W.setCoda = (rich, attivo) => { W.files['post/coda.json'] = JSON.stringify({ attivo: attivo !== false, richieste: rich }); };
  W.setSpec = (id, o) => { W.files['post/' + id + '.json'] = JSON.stringify(spec(o)); };
  const corsi = [{ id: 'c2', name: 'NUOVO 2 INFO' }, { id: 'cp', name: 'PROVA PUBBLICAZIONE' }, { id: 'c1', name: '1 INF 26/27' }];
  const fail = (nome) => { const q = W.faults[nome]; if (q && q.length) { const e = q.shift(); if (e) throw new Error(e); } };
  const Classroom = {
    Courses: {
      list() { return { courses: corsi }; },
      CourseWork: {
        list(cid, p) { const st = (p && p.courseWorkStates) || ['PUBLISHED']; return { courseWork: Object.values(W.cw).filter(x => x.courseId === cid && st.includes(x.state)) }; },
        get(cid, id) { fail('get'); const x = W.cw[id]; if (!x || x.courseId !== cid) throw new Error('404 Requested entity was not found'); return JSON.parse(JSON.stringify(x)); },
        create(res, cid) {
          fail('create');
          const id = String(++W.seq), x = Object.assign({}, JSON.parse(JSON.stringify(res)), { id, courseId: cid, alternateLink: 'https://classroom.google.com/c/' + cid + '/a/' + id, creatoDa: 'motore' });
          if (W.mutaTesto) x.description = W.mutaTesto(x.description);
          if (W.aggiungiScadenza) x.dueDate = { year: 2026, month: 11, day: 30 };
          W.cw[id] = x; W.creati.push(JSON.parse(JSON.stringify(res))); return JSON.parse(JSON.stringify(x));
        },
        patch(res, cid, id, p) {
          fail('patch'); const x = W.cw[id];
          if (x.creatoDa === 'altro') throw new Error('403 @ProjectPermissionDenied');
          const mask = p.updateMask.split(','); mask.forEach(k => { if (!['title', 'description', 'state'].includes(k)) throw new Error('maschera non ammessa ' + k); x[k] = res[k]; });
          W.patch.push({ id, mask: p.updateMask, res }); return JSON.parse(JSON.stringify(x));
        },
        remove(cid, id) { W.rimossi.push(id); W.cw[id].state = 'DELETED'; }
      }
    }
  };
  const resp = (code, body, bin) => ({ getResponseCode: () => code, getContentText: () => (typeof body === 'string' ? body : ''), getBlob: () => { const b = Buffer.from(body, 'latin1'); return { getBytes: () => Array.from(b).map(v => (v > 127 ? v - 256 : v)), setName(n) { this.nome = n; return this; }, nome: '' }; } });
  const UrlFetchApp = {
    fetch(url) {
      W.fetch.push(url);
      if (/tokeninfo/.test(url)) return resp(200, JSON.stringify({ scope: W.scope || 'https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/drive' }));
      const p = url.replace(BASE, '').replace(/\?t=\d+$/, '');
      if (W.files[p] === undefined) return resp(404, '');
      const r = resp(200, p.endsWith('.json') ? Buffer.from(W.files[p], 'utf8').toString('utf8') : W.files[p]);
      return r;
    }
  };
  const mkFile = (nome) => { const id = 'F' + (++W.seq); const f = { getId: () => id, setTrashed() { }, nome }; W.drive[id] = f; return f; };
  const cartella = { createFile(b) { return mkFile(b.nome); } };
  const DriveApp = {
    getFoldersByName() { return { hasNext: () => false }; }, createFolder() { return cartella; }, createFile(b) { return mkFile(b.nome); },
    getFileById(id) { return { makeCopy(n) { return mkFile(n); } }; }
  };
  const fogli = { Esiti: [['Ora', 'Id', 'Titolo', 'Ragazzi', 'Modifica', 'Controllo', 'Classe', 'FormId'], ['x', 'quiz-2inf-2411-ora2', 'Quiz', 'https://docs.google.com/forms/d/e/1FAIpQLSabc/viewform', 'edit', 'OK', '2INF', 'abc']] };
  const SpreadsheetApp = {
    openById() {
      return {
        getSheetByName(n) { return fogli[n] ? sh(n) : null; },
        insertSheet(n) { fogli[n] = fogli[n] || []; return sh(n); }
      };
    }
  };
  function sh(n) {
    return {
      getDataRange: () => ({ getValues: () => fogli[n] }),
      getRange: (r, c, nr, nc) => ({ setValues(v) { v.forEach((riga, i) => { fogli[n][r - 1 + i] = riga; }); return this; }, setFontWeight() { return this; } }),
      appendRow(riga) { fogli[n].push(riga); W.righe.push(riga); }
    };
  }
  W.fogli = fogli;
  class FakeDate extends Date { constructor(...a) { if (a.length) super(...a); else super(W.now); } static now() { return W.now; } }
  const ctx = {
    Classroom, UrlFetchApp, DriveApp, SpreadsheetApp, Date: FakeDate, Buffer, JSON, Math, Object, String, Number, Array, Error, RegExp, parseInt, console,
    FB_BASE: BASE,
    Logger: { log: (x) => W.log.push(String(x)) },
    Utilities: {
      sleep() { }, newBlob(c, m, n) { const b = Buffer.from(c, 'latin1'); return { getBytes: () => Array.from(b), nome: n, setName(x) { this.nome = x; return this; } }; },
      formatDate(d, tz, f) { const p = fusoParti(d); return f.replace('yyyy', p.year).replace('MM', p.month).replace('dd', p.day).replace('HHmm', p.hour + p.minute).replace('HH', p.hour).replace('mm', p.minute).replace('ss', p.second).replace(/^u$/, String(mondayBased(p.weekday))); }
    },
    PropertiesService: { getScriptProperties: () => ({ getProperty: (k) => (k in W.props ? W.props[k] : null), setProperty: (k, v) => { W.props[k] = v; } }) },
    LockService: { getUserLock: () => ({ tryLock: () => !W.lockOccupato, releaseLock() { } }) },
    ScriptApp: { getOAuthToken: () => 'tok', getProjectTriggers: () => [], newTrigger: () => ({ timeBased: () => ({ everyMinutes: () => ({ create() { } }) }) }) }
  };
  W.props.FB_FOGLIO = 'foglio'; W.props.PB_CORSO_PROVA = 'PROVA PUBBLICAZIONE';
  vm.createContext(ctx);
  W.ctx = ctx;
  vm.runInContext(SRC, ctx);
  /* come fa il lancio: eval() dentro una funzione, poi si chiama PB_main_ */
  vm.runInContext('function pubb_ciclo(){ eval(__SRC__); return PB_main_(); }', Object.assign(ctx, { __SRC__: SRC }));
  W.giro = () => vm.runInContext('pubb_ciclo()', ctx);
  W.main = () => vm.runInContext('PB_main_()', ctx);
  W.valida = (s, r) => vm.runInContext('PB_valida_(' + JSON.stringify(s) + ',' + JSON.stringify(r || null) + ')', ctx);
  return W;
}

console.log('1. controlli della specifica');
{
  const W = mondo(), buona = W.spec(), r = { azione: 'pubblica', pubb: 2, giorno: '2026-11-24' };
  t('specifica buona: nessun errore', W.valida(buona, r).err.length === 0, JSON.stringify(W.valida(buona, r)));
  t('titolo senza «G/M Ora N:» respinto', W.valida(W.spec({ titolo: 'Il CSS' }), r).err.some(e => /titolo/.test(e)));
  t('titolo con ora sbagliata respinto', W.valida(W.spec({ titolo: '24/11 Ora 3: il CSS' }), r).err.length > 0);
  t('titolo con giorno sbagliato respinto', W.valida(W.spec({ titolo: '25/11 Ora 2: il CSS' }), r).err.length > 0);
  t('scadenza respinta', W.valida(W.spec({ scadenza_iso: '2026-11-24T10:00:00Z' }), r).err.some(e => /scadenza/.test(e)));
  t('punti respinti', W.valida(W.spec({ punti: 10 }), r).err.some(e => /punti/.test(e)));
  t('«????» nel testo respinto', W.valida(W.spec({ descrizione: 'ciao ???? mondo' }), r).err.some(e => /\?\?\?\?/.test(e)));
  t('PUBB 3 su un post di ora 2 respinto (una ora per volta)', W.valida(buona, { azione: 'pubblica', pubb: 3, giorno: '2026-11-24' }).err.some(e => /una ora per volta/.test(e)));
  t('arabo in 2INF: solo avviso R6, non errore', (() => { const x = W.valida(buona, r); return x.avv.length === 1 && x.err.length === 0; })());
  t('arabo in 1INF: nessun avviso', W.valida(W.spec({ id: '2026-11-24_1INF_ora2', classe: '1INF' }), r).avv.length === 0);
  t('pdf con percorso fuori da post/ respinto', W.valida(W.spec({ allegati: [{ tipo: 'pdf', file: '../x.pdf', nome: 'a' }] }), r).err.length > 0);
  t('link http (non https) respinto', W.valida(W.spec({ allegati: [{ tipo: 'link', url: 'http://x.it' }] }), r).err.length > 0);
}

console.log('2. PUBB 2 sul corso di prova: bozza, rilettura, pubblica, prova');
{
  const W = mondo(), r = W.giro();
  const e = r.fatte[0] || {};
  t('esito PUBBLICATO', e.stato === 'PUBBLICATO', JSON.stringify(e));
  t('un solo compito creato', W.creati.length === 1);
  const c = W.creati[0] || {};
  t('creato in BOZZA (mai direttamente PUBLISHED)', c.state === 'DRAFT');
  t('senza scadenza e senza punti', !c.dueDate && !c.dueTime && !c.maxPoints);
  t('4 allegati: PDF, Documento copia, link quiz, link pagina', (c.materials || []).length === 4);
  t('Documento con shareMode STUDENT_COPY', (c.materials || []).some(m => m.driveFile && m.driveFile.shareMode === 'STUDENT_COPY'));
  t('PDF con shareMode VIEW', (c.materials || []).some(m => m.driveFile && m.driveFile.shareMode === 'VIEW'));
  t('link del quiz preso da Esiti colonna D', (c.materials || []).some(m => m.link && m.link.url === 'https://docs.google.com/forms/d/e/1FAIpQLSabc/viewform'));
  t('testo arabo e cinese identico byte per byte', Buffer.from(c.description, 'utf8').equals(Buffer.from(W.spec().descrizione, 'utf8')));
  t('titolo «24/11 Ora 2: il CSS»', c.title === '24/11 Ora 2: il CSS');
  const cw = Object.values(W.cw)[0];
  t('stato finale su Classroom (finto) PUBLISHED', cw.state === 'PUBLISHED');
  t('creato nel corso di PROVA, non in quello vero', cw.courseId === 'cp');
  t('un solo patch, solo sullo stato', W.patch.length === 1 && W.patch[0].mask === 'state');
  t('riga nella scheda Pubblicazioni con Esito PUBBLICATO e «PUBLISHED alle»', W.righe.length === 1 && W.righe[0][5] === 'PUBBLICATO' && /PUBLISHED alle/.test(W.righe[0][6]));
  const r2 = W.giro();
  t('secondo giro: niente di nuovo (idempotente)', r2.fatte.length === 0 && W.creati.length === 1);
  W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'r2', prova: true }]);
  const r3 = W.giro();
  t('PUBB ripetuto con nuova richiesta: GIA_PUBBLICATO, nessun doppione', r3.fatte[0].stato === 'GIA_PUBBLICATO' && W.creati.length === 1 && Object.keys(W.cw).length === 1);
}

console.log('3. anti-doppione e corsi veri');
{
  let W = mondo();
  W.cw['900'] = { id: '900', courseId: 'cp', title: '24/11  ora 2: IL CSS', state: 'PUBLISHED', creatoDa: 'altro', alternateLink: 'https://x/900' };
  let r = W.giro();
  t('compito a mano con stesso titolo (anche con maiuscole/spazi diversi): NON_RIUSCITO e nessuna creazione', r.fatte[0].stato === 'NON_RIUSCITO' && W.creati.length === 0 && /non lo tocco/.test(r.fatte[0].motivo));
  W = mondo(); W.cw['901'] = { id: '901', courseId: 'cp', title: '24/11 Ora 2: il CSS', state: 'DRAFT', creatoDa: 'altro' };
  r = W.giro();
  t('bozza non del motore con stesso titolo: NON_RIUSCITO', r.fatte[0].stato === 'NON_RIUSCITO' && W.creati.length === 0 && W.patch.length === 0);
  W = mondo(); W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'r1' }]);
  r = W.giro();
  t('corso vero con PB_ABILITA_REALE spento: solo BOZZA, mai PUBLISHED', r.fatte[0].stato === 'BOZZA_PRONTA' && Object.values(W.cw)[0].state === 'DRAFT' && Object.values(W.cw)[0].courseId === 'c2' && W.patch.length === 0);
  W = mondo(); W.props.PB_ABILITA_REALE = '1'; W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'r1' }]);
  r = W.giro();
  t('corso vero con PB_ABILITA_REALE=1: PUBBLICATO nel corso c2', r.fatte[0].stato === 'PUBBLICATO' && Object.values(W.cw)[0].courseId === 'c2');
}

console.log('4. bozza prima, PUBB dopo; modifiche tra le due');
{
  const W = mondo(); W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'bozza', giorno: '2026-11-24', richiesta: 'b1', prova: true }]);
  let r = W.giro();
  t('azione bozza: BOZZA_PRONTA, nessun patch', r.fatte[0].stato === 'BOZZA_PRONTA' && W.patch.length === 0);
  W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'bozza', giorno: '2026-11-24', richiesta: 'b1', prova: true }, { post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'p1', prova: true }]);
  r = W.giro();
  t('poi PUBB 2: pubblica la stessa bozza senza ricrearla', r.fatte.length === 1 && r.fatte[0].stato === 'PUBBLICATO' && W.creati.length === 1);
  const W2 = mondo(); W2.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'bozza', giorno: '2026-11-24', richiesta: 'b1', prova: true }]); W2.giro();
  W2.setSpec('2026-11-24_2INF_ora2', { descrizione: 'Testo corretto dopo la bozza.' });
  W2.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'p1', prova: true }]);
  r = W2.giro();
  t('testo cambiato dopo la bozza: patch di titolo e testo, poi pubblica, nessun doppione', r.fatte[0].stato === 'PUBBLICATO' && W2.patch[0].mask === 'title,description' && W2.creati.length === 1 && Object.values(W2.cw)[0].description === 'Testo corretto dopo la bozza.');
  const W3 = mondo(); W3.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'bozza', giorno: '2026-11-24', richiesta: 'b1', prova: true }]); W3.giro();
  W3.setSpec('2026-11-24_2INF_ora2', { allegati: [{ tipo: 'link', url: 'https://example.org/nuovo' }] });
  W3.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'p1', prova: true }]);
  r = W3.giro();
  t('allegati cambiati: la bozza si cancella e si rifa; il pubblicato non si tocca mai', r.fatte[0].stato === 'PUBBLICATO' && W3.rimossi.length === 1 && W3.creati.length === 2 && Object.values(W3.cw).filter(x => x.state === 'PUBLISHED').length === 1);
}

console.log('5. una ora per volta, giorni, interruttori');
{
  let W = mondo(); W.setSpec('2026-11-24_2INF_ora3', { id: '2026-11-24_2INF_ora3', ora: 3, titolo: '24/11 Ora 3: la griglia' });
  W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-24', richiesta: 'a', prova: true }, { post: '2026-11-24_2INF_ora3', azione: 'pubblica', pubb: 3, giorno: '2026-11-24', richiesta: 'b', prova: true }]);
  let r = W.giro();
  t('due PUBB nella coda: nel primo giro ne parte UNO solo', r.fatte.length === 1 && r.fatte[0].pubb === 2 && W.creati.length === 1);
  r = W.giro();
  t('il secondo parte al giro dopo', r.fatte.length === 1 && r.fatte[0].pubb === 3);
  W = mondo(); W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-23', richiesta: 'a', prova: true }]);
  r = W.giro();
  t('richiesta di un giorno passato: SCADUTA, nulla su Classroom', r.fatte[0].stato === 'SCADUTA' && W.creati.length === 0);
  W = mondo(); W.setCoda([{ post: '2026-11-24_2INF_ora2', azione: 'pubblica', pubb: 2, giorno: '2026-11-25', richiesta: 'a', prova: true }]);
  r = W.giro();
  t('richiesta di domani: non fatta oggi', r.fatte.length === 0 && W.creati.length === 0);
  W = mondo(); W.props.PB_STOP = '1'; r = W.giro();
  t('PB_STOP=1: non legge nemmeno la coda', r.saltato === 'PB_STOP' && W.fetch.length === 0);
  W = mondo({ ora: '2026-11-28T09:00:00Z' }); r = W.giro();
  t('sabato: fuori fascia, nessuna chiamata di rete', r.saltato === 'fuori orario' && W.fetch.length === 0);
  W = mondo({ ora: '2026-11-24T14:45:00Z' }); r = W.giro();
  t('15:45 a Roma: fuori fascia', r.saltato === 'fuori orario');
  W = mondo(); W.setCoda(JSON.parse(W.files['post/coda.json']).richieste, false); r = W.giro();
  t('«attivo»:false nella coda: spento da git', r.saltato === 'coda spenta' && W.creati.length === 0);
  W = mondo(); W.lockOccupato = true; r = W.giro();
  t('giro gia in corso (lock): salta', r.saltato === 'lock');
}

console.log('6. guasti');
{
  let W = mondo(); W.faults.create = ['503 Backend Error', '503 Backend Error'];
  let r = W.giro();
  t('503 due volte poi ok (retry interno): PUBBLICATO, un solo compito', r.fatte[0].stato === 'PUBBLICATO' && W.creati.length === 1);
  W = mondo(); W.faults.create = new Array(40).fill('503 Backend Error');
  r = W.giro(); const a = r.fatte[0].stato; r = W.giro(); const b = r.fatte[0].stato; r = W.giro(); const c = r.fatte[0];
  t('503 persistente: RIPROVO, RIPROVO, poi NON_RIUSCITO con il motivo', a === 'RIPROVO' && b === 'RIPROVO' && c.stato === 'NON_RIUSCITO' && /tentativi/.test(c.motivo), a + ' ' + b + ' ' + c.stato);
  t('...e non resta nulla di pubblicato', Object.values(W.cw).filter(x => x.state === 'PUBLISHED').length === 0);
  W = mondo(); W.faults.patch = ['403 PERMISSION_DENIED'];
  r = W.giro();
  t('pubblica rifiutata da Classroom: NON_RIUSCITO, resta la bozza invisibile, link nell\'esito', r.fatte[0].stato === 'NON_RIUSCITO' && Object.values(W.cw)[0].state === 'DRAFT' && !!r.fatte[0].link);
  W = mondo(); W.mutaTesto = (x) => x.replace(/[؀-ۿ一-鿿]/g, '?');
  r = W.giro();
  t('Classroom altera il testo (arabo/cinese perduti): NON pubblicato', r.fatte[0].stato === 'NON_RIUSCITO' && /testo diverso/.test(r.fatte[0].motivo) && Object.values(W.cw)[0].state === 'DRAFT' && W.patch.length === 0);
  W = mondo(); W.aggiungiScadenza = true; r = W.giro();
  t('Classroom mette una scadenza: NON pubblicato', r.fatte[0].stato === 'NON_RIUSCITO' && /scadenza/.test(r.fatte[0].motivo) && W.patch.length === 0);
  W = mondo(); W.files['post/2026-11-24_2INF_ora2-guida.pdf'] = '<html>404</html>'.padEnd(200, ' '); r = W.giro();
  t('il PDF non e un PDF: NON_RIUSCITO e nessun compito creato', r.fatte[0].stato === 'NON_RIUSCITO' && W.creati.length === 0);
  W = mondo(); delete W.files['post/2026-11-24_2INF_ora2.json']; W.faults = {}; r = W.giro();
  t('specifica mancante in git (404): NON_RIUSCITO con il motivo', r.fatte[0].stato === 'NON_RIUSCITO' && /404/.test(r.fatte[0].motivo));
  W = mondo(); W.props.PB_CORSO_PROVA = 'CORSO CHE NON ESISTE'; r = W.giro();
  t('corso di prova inesistente: NON_RIUSCITO, nulla creato', r.fatte[0].stato === 'NON_RIUSCITO' && W.creati.length === 0 && /trovati 0/.test(r.fatte[0].motivo));
  W = mondo(); W.setSpec('2026-11-24_2INF_ora2', { allegati: [{ tipo: 'quiz', id: 'quiz-inesistente' }] }); r = W.giro();
  t('quiz non trovato in Esiti: NON_RIUSCITO, nulla creato', r.fatte[0].stato === 'NON_RIUSCITO' && W.creati.length === 0);
  W = mondo(); r = W.giro(); const s = JSON.stringify(W.creati) + JSON.stringify(W.righe);
  t('nessun cognome o email negli oggetti inviati a Classroom e nel foglio (controllo di forma)', !/@/.test(s));
}

console.log('7. prova di 5 minuti (servizi finti)');
{
  const W = mondo(); W.cw = {};
  const corsi = vm.runInContext('Classroom.Courses.list().courses', W.ctx);
  vm.runInContext(PROVA5 + '\nPB_prova5minuti();', W.ctx);
  const log = W.log.join('\n');
  t('legge i permessi e li riporta', /PROVATO\s+permesso classroom\.coursework\.students/.test(log) && /PROVATO\s+permesso drive/.test(log));
  t('crea in bozza, rilegge testo arabo/cinese, pubblica, cancella', /compito creato in BOZZA con 2 allegati/.test(log) && /testo arabo e cinese identico/.test(log) && /PUBLISHED/.test(log) && /cancellato/.test(log) && !/NON RIUSCITO/.test(log), log);
  const W2 = mondo(); W2.scope = 'https://www.googleapis.com/auth/classroom.coursework.students.readonly https://www.googleapis.com/auth/drive.readonly';
  vm.runInContext(PROVA5 + '\nPB_prova5minuti();', W2.ctx);
  t('con permessi di sola lettura la prova lo dice (NON RIUSCITO su classroom e drive)', (W2.log.join('\n').match(/NON RIUSCITO\s+permesso/g) || []).length === 2);
}

console.log('\nTotale: ' + ok + ' ok, ' + ko + ' falliti');
process.exit(ko ? 1 : 0);
