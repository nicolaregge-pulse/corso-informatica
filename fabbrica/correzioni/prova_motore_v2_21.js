// Prova locale delle due correzioni del motore v2.21 (nomi composti 4TI, domande aperte). NOMI INVENTATI. Servizi Google FINTI (non e Google).
// Uso: node fabbrica/correzioni/prova_motore_v2_21.js   (dalla radice del repository)
var fs = require('fs'), vm = require('vm'), path = require('path');
var DIR = path.join(__dirname, '..');
function carica(file) {
  var src = fs.readFileSync(file, 'utf8');
  var a = src.indexOf('var SM_PART_'), b = src.indexOf('/* valori della scheda docente');
  var c = src.indexOf('function FB_aperteItems_'), d = src.indexOf('function FB_puntiTotali_');
  var ctx = { FormApp: { ItemType: { TEXT: 'T', PARAGRAPH_TEXT: 'P', MULTIPLE_CHOICE: 'M' } } };
  vm.createContext(ctx);
  vm.runInContext(src.slice(a, b), ctx);
  if (c > 0) vm.runInContext(src.slice(c, d), ctx);
  return ctx;
}
var vecchio = carica(path.join(DIR, 'motore.js')), nuovo = carica(path.join(DIR, 'correzioni', 'motore-v2.21.js'));
var fail = [];
function check(c, m) { if (!c) fail.push(m); }
var elenco = ['ROSSI BIANCHI MARIO LUCA', 'VERDI ANNA MARIA', 'DE LUCA PAOLO', 'NERI SARA', 'GRIGI BLU GIORGIO ENZO', 'MORI ENZO', 'DE LEON CHASE', 'Bianchi Luca', 'ROSSI Mario Luca', 'LI WEI MING ANDREA BEN CHEN'];
var lv = vecchio.SM_brevi_(elenco), ln = nuovo.SM_brevi_(elenco);
console.log('VECCHIO:', JSON.stringify(lv));
console.log('NUOVO  :', JSON.stringify(ln));
// il bug: nel vecchio compare un secondo cognome
check(/Bianchi Mario Luca/.test(lv[0]), 'la prova non riproduce il difetto nel motore attuale (atteso «Bianchi Mario Luca R.»)');
check(/Blu Giorgio Enzo/.test(lv[4]), 'la prova non riproduce il difetto per il secondo caso');
// nel nuovo: mai un cognome (dopo il primo) dentro l'etichetta
check(ln[0] === 'Luca R.', 'atteso «Luca R.», trovato ' + ln[0]);
check(ln[4] === 'Enzo G.', 'atteso «Enzo G.», trovato ' + ln[4]);
check(ln[1] === 'Maria V.', 'atteso «Maria V.», trovato ' + ln[1]);
check(ln.every(function (x) { return !/Bianchi|Blu |Chen|Wei/.test(x) || /^Bianchi Luca$/.test(x) === false; }), 'un cognome nell etichetta');
// i casi che erano gia giusti restano uguali
check(ln[2] === vecchio.SM_brevi_(['DE LUCA PAOLO'])[0], 'DE LUCA PAOLO cambiato');
check(ln[3] === 'Sara N.' && lv[3] === 'Sara N.', 'NERI SARA');
check(ln[5] === 'Enzo M.' && lv[5] === 'Enzo M.', 'MORI ENZO');
check(ln[6] === lv[6], 'DE LEON CHASE cambiato: ' + lv[6] + ' -> ' + ln[6]);
check(ln[8] === lv[8] && ln[8] === 'Mario Luca R.', 'ROSSI Mario Luca (maiuscole miste) cambiato: ' + ln[8]);
// domande aperte: FB_aperteItems_ prende solo testo/paragrafo con punti > 0
function item(t, p) { var o = { getType: function () { return t; } }; o.asTextItem = o.asParagraphTextItem = function () { return { getPoints: function () { return p; } }; }; return o; }
var form = { getItems: function () { return [item('M', 1), item('M', 1), item('P', 2), item('T', 2), item('P', 0), item('T', 0)]; } };
var ap = nuovo.FB_aperteItems_(form);
check(ap.length === 2, 'FB_aperteItems_ deve trovare 2 aperte con punti, trovate ' + ap.length);
check(typeof vecchio.FB_aperteItems_ === 'undefined', 'il motore attuale non ha FB_aperteItems_ (previsto)');
if (fail.length) { console.log('PROVA FALLITA:\n- ' + fail.join('\n- ')); process.exit(1); }
console.log('PROVA OK (2 correzioni; FB_risultati_ con Moduli veri: non provato)');
