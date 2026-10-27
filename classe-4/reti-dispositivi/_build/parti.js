// 27/10/2026 4TI (Nicola: «classe fragile, 4 URL con quiz alla fine su Moduli»): divide la lezione reti-dispositivi in 4 parti corte.
// Uso: node parti.js <file json con i link dei quiz {"1":"https://…","2":…}>
const fs = require('fs'), path = require('path');
const BASE = path.join(__dirname, '../../../docs/verifica/banche/');
global.window = {}; require(BASE + '4ti-reti-dispositivi.js'); const B = window.BANCA;
const link = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const PARTI = { 1: [1, 2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9] };
const TIT = { 1: 'i livelli, le reti, i protocolli', 2: 'lo switch e il router', 3: "l'access point, il Wi-Fi e il firewall", 4: 'il tuo indirizzo IP e il programma dell\'anno' };
for (const [n, idx] of Object.entries(PARTI)) {
  const P = JSON.parse(JSON.stringify(B));
  const mappa = {}; idx.forEach((v, i) => mappa[v] = i + 1);
  P.id = '4ti-reti-' + n + '-v1'; P.titolo = 'Le reti, parte ' + n + ' di 4: ' + TIT[n];
  P.sotto = '4TI · 27/10/2026 · leggi le schede, fai il ripasso, poi il quiz su Moduli in fondo all\'ultima scheda';
  P.stato = 'stato/4ti-reti-' + n + '.json'; P.risultati = 'risultati.html?b=4ti-reti-' + n; P.ripasso_n = 0;
  P.schede = idx.map(i => B.schede[i - 1]);
  const ult = P.schede[P.schede.length - 1];
  const q = link[n] ? '<a href="' + link[n] + '" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">Fai il QUIZ della parte ' + n + '</a>' : '<b>Il quiz della parte ' + n + ' arriva tra poco: premi F5.</b>';
  ult.testo += '<div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p style="margin:0 0 8px"><b>FINE DELLA PARTE ' + n + '.</b> Adesso il quiz: domande su quello che hai appena letto. Rispondi da solo, senza AI.</p>' + q + (n < 4 ? '<p style="margin:10px 0 0">Poi aspetta il via del prof per la parte ' + (+n + 1) + '.</p>' : '<p style="margin:10px 0 0">Poi l\'ultima ora: il tuo progetto.</p>') + '</div>';
  P.schede_temi = {}; for (const [t, v] of Object.entries(B.schede_temi || {})) if (mappa[v]) P.schede_temi[t] = mappa[v];
  const tieni = x => !x.tema || P.schede_temi[x.tema];
  P.allenamento = (B.allenamento || []).filter(x => x.scheda ? mappa[x.scheda] : tieni(x)).map(x => x.scheda ? Object.assign(x, { scheda: mappa[x.scheda] }) : x);
  P.crocette = (B.crocette || []).filter(tieni); P.recupero = (B.recupero || []).filter(tieni);
  P.aperte = []; delete P.prepara; P.minuti = 10;
  fs.writeFileSync(BASE + '4ti-reti-' + n + '.js', '// Generato da classe-4/reti-dispositivi/_build/parti.js (27/10/2026): parte ' + n + ' di 4 della lezione 4ti-reti-dispositivi.\nwindow.BANCA = ' + JSON.stringify(P, null, 1) + ';\n');
  const st = path.join(__dirname, '../../../docs/verifica/stato/4ti-reti-' + n + '.json');
  if (!fs.existsSync(st)) fs.writeFileSync(st, JSON.stringify({ verifica: 'chiusa', recupero: 'chiuso', _nota: '27/10: il quiz è su Moduli, in fondo all\'ultima scheda' }, null, 1));
  console.log(n, P.schede.length, 'schede', P.allenamento.length, 'ripasso', P.crocette.length, 'crocette');
}
