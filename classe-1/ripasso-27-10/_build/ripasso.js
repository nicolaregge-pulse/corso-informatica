// 27/10/2026 1INF (Nicola: «un ripasso da zero, poi la teoria nuova, due quiz su Moduli»): pagina di ripasso fatta con le schede già studiate.
// Uso: node ripasso.js <link quiz ripasso> <link quiz nuovo>
const fs = require('fs'), path = require('path'); const BASE = path.join(__dirname, '../../../docs/verifica/banche/');
global.window = {}; require(BASE + '1inf-byte-velocita.js'); const A = window.BANCA; require(BASE + '1inf-gamer.js'); const G = window.BANCA;
require(BASE + '1inf-video-cavi.js'); const V = window.BANCA;
const [qR, qN] = process.argv.slice(2);
const bott = (u, t) => u ? '<p><a href="' + u + '" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">' + t + '</a></p>' : '<p><b>Il quiz arriva tra poco: premi F5. · الاختبار قريبًا · 测验马上就来</b></p>';
const schede = [A.schede[0], A.schede[1], A.schede[2], A.schede[6], G.schede[1], G.schede[2], G.schede[4], G.schede[5]].map(s => JSON.parse(JSON.stringify(s)));
schede.forEach((s, i) => { s.titolo = s.titolo.replace(/^\d+\./, (i + 1) + '.'); });
schede[schede.length - 1].testo += '<div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE DEL RIPASSO · نهاية المراجعة · 复习结束</b></p>' + bott(qR, 'QUIZ di ripasso · اختبار المراجعة · 复习测验') + '<p>Poi la teoria nuova · ثم الدرس الجديد · 然后新课: <a href="./?b=1inf-video-cavi">la scheda video e i cavi video</a></p></div>';
const R = { id: '1inf-ripasso-2710-v1', classe: '1INF', titolo: 'Ripasso da zero · مراجعة من البداية · 从头复习', sotto: '1INF · 27/10/2026 · bit, byte, Mbps, ping, jitter, FPS, Hz · poi il quiz di ripasso su Moduli',
  stato: 'stato/1inf-ripasso-2710.json', risultati: 'risultati.html?b=1inf-ripasso-2710', minuti: 10, anteprima: A.anteprima, aree: A.aree, schede: schede, schede_temi: {}, allenamento: [], crocette: [], aperte: [], recupero: [] };
fs.writeFileSync(BASE + '1inf-ripasso-2710.js', '// Generato da classe-1/ripasso-27-10/_build/ripasso.js (27/10/2026)\nwindow.BANCA = ' + JSON.stringify(R, null, 1) + ';\n');
const st = path.join(__dirname, '../../../docs/verifica/stato/1inf-ripasso-2710.json');
if (!fs.existsSync(st)) fs.writeFileSync(st, JSON.stringify({ verifica: 'chiusa', recupero: 'chiuso', _nota: '27/10: il quiz è su Moduli' }, null, 1));
// teoria nuova: il quiz nuovo in fondo all'ultima scheda (una sola volta)
let v = fs.readFileSync(BASE + '1inf-video-cavi.js', 'utf8');
v = v.replace(/<!--QUIZNUOVO-->[\s\S]*?<!--\/QUIZNUOVO-->/, '');
const fine = '<!--QUIZNUOVO--><div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE · النهاية · 结束</b></p>' + bott(qN, 'QUIZ sulla lezione nuova · اختبار الدرس الجديد · 新课测验') + '</div><!--/QUIZNUOVO-->';
global.window = {}; eval(v); const VV = window.BANCA; const u = VV.schede[VV.schede.length - 1];
u.testo = u.testo.replace(/<!--QUIZNUOVO-->[\s\S]*?<!--\/QUIZNUOVO-->/, '') + fine;
fs.writeFileSync(BASE + '1inf-video-cavi.js', '// 1INF · La scheda video e i cavi video (27/10/2026), IT/AR/ZH. Rigenerato da classe-1/ripasso-27-10/_build/ripasso.js con il link del quiz.\nwindow.BANCA = ' + JSON.stringify(VV, null, 1) + ';\n');
console.log('ok', schede.length, 'schede di ripasso');
