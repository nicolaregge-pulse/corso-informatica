/* PROVA DELLA VERIFICA COME UN RAGAZZO (13/10/2026, REGISTRO-ERRORI #61): da lanciare PRIMA di aprire una verifica.
   Prova: ripasso, verifica, ricarica a metà, chiusura della scheda, consegna con un clic fino all'arrivo, risultato
   dopo la ricarica, recupero con la teoria mirata. Il punto di arrivo dello script di Google è finto (locale).
   Uso:  cd docs && python3 -m http.server 8765 &   poi   NODE_PATH=$(npm root -g) node strumenti/prova_verifica.js 2inf-versioning */
const { chromium } = require('playwright'); const http = require('http');
const BANCA = process.argv[2] || '2inf-versioning', BASE = 'http://localhost:8765/verifica/?b=' + BANCA;
const arrivi = [], avz = [];
const finto = http.createServer((q, r) => { let b = ''; q.on('data', c => b += c); q.on('end', () => {
  const d = JSON.parse(decodeURIComponent(new URLSearchParams(b).get('d') || '{}')); if (d.modo !== 'avanzamento') arrivi.push(d); else avz.push(d);
  r.writeHead(200, { 'Content-Type': 'text/html' }); r.end('<h1>Consegna arrivata al prof</h1>'); }); }).listen(8766);
let ko = 0; const permesses = n => n; const ok = (cond, t) => { console.log((cond ? 'OK   ' : 'NO   ') + t); if (!cond) ko++; };
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const c = await b.newContext(); const err = [];
  await c.route('**/verifica/config.json*', r => r.fulfill({ contentType: 'application/json', body: JSON.stringify({ invio: 'http://localhost:8766/exec' }) }));
  await c.route('**/stato/' + BANCA + '.json*', r => r.fulfill({ contentType: 'application/json', body: JSON.stringify({ verifica: 'aperta', recupero: 'aperto', recupero_per: 'tutti', scadenza: new Date(Date.now() + 3600e3).toISOString() }) }));
  let p = await c.newPage(); p.on('pageerror', e => err.push(e.message)); p.on('dialog', d => d.accept());
  await p.goto(BASE); await p.waitForTimeout(1200);
  ok(await p.$('#nome'), 'ripasso: chiede il nome');
  await p.fill('#nome', 'Prova Ragazzo'); await p.click('#okn'); await p.waitForTimeout(800);
  ok((await p.innerText('body')).includes('Per regolarti da solo'), 'ripasso: bottoni per autoregolarsi (monitor, risultati)');
  await p.goto(BASE + '&modo=verifica'); await p.waitForTimeout(1000); await p.click('#via'); await p.waitForTimeout(500);
  await p.click('.op >> nth=0'); await p.click('#succ'); await p.click('#succ'); await p.waitForTimeout(2500);
  const dove = await p.innerText('#dove');
  await p.reload(); await p.waitForTimeout(1500);
  ok((await p.innerText('#dove').catch(() => '')) === dove, 'ricarica a metà: riparte dalla stessa domanda (' + dove + ')');
  await p.close(); p = await c.newPage(); p.on('pageerror', e => err.push(e.message)); p.on('dialog', d => d.accept());
  await p.goto(BASE + '&modo=verifica'); await p.waitForTimeout(1500);
  ok((await p.innerText('#dove').catch(() => '')) === dove, 'scheda chiusa e riaperta: riparte dalla stessa domanda');
  // domande «incolla qui» (codice, indirizzo): l'incolla deve essere permesso; nelle altre bloccato
  let trovInc = 0, bloccate = 0, permesse = 0;
  for (let i = 0; i < 30; i++) {
    const ph = await p.$eval('#ta', t => t.placeholder).catch(() => '');
    if (ph) { await p.focus('#ta'); await p.evaluate(() => navigator.clipboard && 0); 
      await p.evaluate(() => { const t = document.getElementById('ta'); const ev = new Event('paste', { bubbles: true, cancelable: true }); t.dispatchEvent(ev); window.__p = ev.defaultPrevented; });
      const prev = await p.evaluate(() => window.__p);
      if (ph.startsWith('Incolla')) { trovInc++; if (!prev) permesse++; } else if (prev) bloccate++; }
    const s = await p.$('#succ'); if (!s || !(await s.isVisible().catch(() => false))) break; await s.click({ timeout: 1500 }).catch(() => 0); await p.waitForTimeout(120);
  }
  ok(trovInc === 0 || permesse === trovInc, 'domande «incolla qui»: ' + trovInc + ' trovate, incolla permesso in ' + permesses(permesse));
  ok(bloccate > 0 || trovInc === 0, 'nelle altre risposte scritte l\'incolla resta bloccato (' + bloccate + ')');
  await p.goto(BASE + '&modo=verifica'); await p.waitForTimeout(1200);
  const nuova = c.waitForEvent('page', { timeout: 5000 }).catch(() => null);
  await p.click('#fine'); const sch = await nuova; await p.waitForTimeout(1500);
  ok(arrivi.length === 1 && arrivi[0].nome === 'Prova Ragazzo' && arrivi[0].crocette && arrivi[0].tempi, 'consegna con un clic: il risultato completo arriva allo script (' + arrivi.length + ')');
  ok(avz.length >= 1 && avz[0].id === 'avz-' + arrivi[0].id && typeof avz[0].scheda === 'number', 'il monitor riceve i segnali di avanzamento della teoria (' + avz.length + ')');
  ok(sch && (await sch.content()).includes('Consegna arrivata'), 'si apre la scheda «Consegna arrivata al prof»');
  ok((await p.innerText('body')).includes('Hai finito'), 'la pagina dice «Hai finito»');
  await p.reload(); await p.waitForTimeout(1500);
  ok((await p.innerText('body')).includes('Hai finito'), 'dopo la ricarica il risultato resta, niente da rifare');
  await p.goto(BASE + '&modo=recupero'); await p.waitForTimeout(1500);
  ok((await p.innerText('body')).includes('Ripassa i punti dove hai sbagliato'), 'recupero: prima la teoria mirata sui propri errori');
  ok(err.filter(x => !x.includes('Permissions')).length === 0, 'nessun errore nella pagina ' + err.join(' / '));
  await b.close(); finto.close();
  console.log(ko ? '\nATTENZIONE: ' + ko + ' prove non passate. Non aprire la verifica.' : '\nTutto a posto: la verifica si può aprire.');
  process.exit(ko ? 1 : 0);
})();
