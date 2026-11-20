/* prova di doPost (eventi-webapp-v1.0.gs) con finti SpreadsheetApp/LockService/CacheService. Uso: node prova_gs.js */
const fs = require('fs'), vm = require('vm'), path = require('path');
const righe = []; const cache = {}; let ok = true;
const sh = { getLastRow: () => righe.length, getRange: () => ({ setValues: v => { righe.push(v[0]); return { setFontWeight() {} }; } }), appendRow: r => righe.push(r) };
const ctx = { Date, JSON, Math, Number, String, console,
  PropertiesService: { getScriptProperties: () => ({ getProperty: () => null }) },
  SpreadsheetApp: { getActive: () => ({ getSheetByName: () => sh, insertSheet: () => sh }) },
  LockService: { getScriptLock: () => ({ waitLock() {}, releaseLock() {} }) },
  CacheService: { getScriptCache: () => ({ get: k => cache[k], put: (k, v) => { cache[k] = v; } }) },
  ContentService: { MimeType: { JSON: 'json' }, createTextOutput: t => ({ t, setMimeType() { return this; } }) } };
vm.createContext(ctx); vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'eventi-webapp-v1.0.gs'), 'utf8'), ctx);
const base = { v: 1, a: 'Prova R.', t: 'teoria', id: 'prova-v1', s: 'visto', n: 0, m: 3, sec: 0, cl: '2INF', se: 'abc123', ts: '2026-11-20T10:00:00Z' };
const prova = (nome, d, atteso) => { const r = JSON.parse(ctx.doPost({ parameter: { d: JSON.stringify(d) } }).t); const c = atteso(r); ok = ok && c; console.log((c ? 'OK   ' : 'FALLITO ') + nome + ' -> ' + JSON.stringify(r)); };
prova('evento valido scritto', base, r => r.ok && righe.length === 2);
prova('stesso evento entro 10 s ignorato', base, r => r.doppio && righe.length === 2);
prova('cognome intero rifiutato', { ...base, a: 'Prova Rossi', s: 'iniziato' }, r => !r.ok && righe.length === 2);
prova('nome senza iniziale rifiutato', { ...base, a: 'Prova', s: 'iniziato' }, r => !r.ok);
prova('email rifiutata', { ...base, a: 'prova.rossi@studenti.piamarta.it' }, r => !r.ok);
prova('tipo sconosciuto rifiutato', { ...base, t: 'altro', s: 'avanzato' }, r => !r.ok);
prova('id con caratteri strani rifiutato', { ...base, id: '../x', s: 'avanzato' }, r => !r.ok);
prova('avanzato 2/3 con secondi scritto', { ...base, s: 'avanzato', n: 2, sec: 30 }, r => r.ok && righe.length === 3 && righe[2][7] === 2 && righe[2][9] === 30);
prova('json rotto', 'non json', r => !r.ok);
console.log('righe nella scheda (con intestazione):', righe.length); process.exit(ok ? 0 : 1);
