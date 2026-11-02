// Test pagina docs/2fa: RFC 6238 + layout. Uso: node strumenti/test_2fa.js  (server locale interno)
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', 'docs');
const srv = http.createServer((q, r) => { let p = path.join(root, decodeURIComponent(q.url.split('?')[0])); if (p.endsWith('/')) p += 'index.html';
  fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'}); r.end(d); } }); });
let fail = 0; const ok = (c, m) => { console.log((c ? 'OK   ' : 'FAIL ') + m); if (!c) fail++; };
(async () => {
  await new Promise(r => srv.listen(0, r)); const url = `http://localhost:${srv.address().port}/2fa/`;
  const b = await chromium.launch();
  const S = 'GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ';
  for (const w of [390, 1280]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 800 }, permissions: ['clipboard-read', 'clipboard-write'] });
    const pg = await ctx.newPage(); const errs = [];
    pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); pg.on('pageerror', e => errs.push(String(e)));
    await pg.goto(url);
    if (w === 390) {
      const v = await pg.evaluate(async S => [await totp(S, 59, 8), await totp(S, 59, 6), await totp(S, 1111111109, 6), await totp(S, 1234567890, 6)], S);
      ok(v[0] === '94287082', 'RFC T=59 8 cifre = ' + v[0]); ok(v[1] === '287082', 'RFC T=59 6 cifre = ' + v[1]);
      ok(v[2] === '081804', 'RFC T=1111111109 = ' + v[2]); ok(v[3] === '005924', 'RFC T=1234567890 = ' + v[3]);
      const v2 = await pg.evaluate(async () => totp('gezd gnbv-gy3t qojq gezdgnbvgy3tqojq', 59, 6)); ok(v2 === '287082', 'minuscolo con spazi = ' + v2);
    }
    await pg.evaluate(() => { window.__fakeNow = 59000; });
    await pg.fill('#sec', 'gezd gnbv gy3t qojq gezd gnbv gy3t qojq'); await pg.fill('#nm', 'GitHub'); await pg.click('#add');
    await pg.waitForFunction(() => /^\d{3} \d{3}$/.test(document.getElementById('num0').textContent));
    const t1 = await pg.textContent('#num0'); ok(t1 === '287 082', w + 'px account aggiunto, numero a T=59: ' + t1);
    await pg.evaluate(() => { window.__fakeNow = 31000; }); await pg.waitForTimeout(600);
    const w1 = await pg.evaluate(() => parseFloat(document.querySelector('#bar0 i').style.width));
    await pg.evaluate(() => { window.__fakeNow = 45000; }); await pg.waitForTimeout(600);
    const w2 = await pg.evaluate(() => parseFloat(document.querySelector('#bar0 i').style.width));
    ok(w2 < w1, w + 'px barra scende ' + w1 + ' -> ' + w2);
    await pg.evaluate(() => { window.__fakeNow = 60000; }); await pg.waitForTimeout(700);
    const t2 = await pg.textContent('#num0'); const ex = await pg.evaluate(async S => { const c = await totp(S, 60, 6); return c.slice(0, 3) + ' ' + c.slice(3); }, S);
    ok(t2 === ex && t2 !== t1, w + 'px cambio finestra a 30 s: ' + t1 + ' -> ' + t2);
    await pg.reload(); await pg.waitForSelector('#num0'); ok(true, 'account salvato dopo ricarica');
    const sc = await pg.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth); ok(sc, w + 'px nessuno scroll orizzontale');
    ok(errs.length === 0, w + 'px zero errori console ' + errs.join('|'));
    if (w === 390) {
      const posts = []; await pg.route('https://script.google.com/**', r => { posts.push(decodeURIComponent(r.request().postData() || '')); r.fulfill({ status: 200, body: 'ok' }); });
      ok(await pg.isDisabled('#consegna'), 'consegna bloccata a inizio');
      for (let i = 1; i <= 8; i++) await pg.check('input[data-p="' + i + '"]');
      await pg.fill('#chi', 'Beretta Luca'); await pg.fill('#ncod', 'ABCD'); await pg.fill('#fatto', 'fatto'); await pg.click('#consegna');
      ok(/solo il numero/.test(await pg.textContent('#finerr')), 'rifiuta codici scritti a lettere');
      await pg.fill('#ncod', '16'); await pg.click('#consegna'); await pg.waitForTimeout(400);
      ok((await pg.textContent('#avtxt')) === '8 passi su 8', 'avanzamento 8 su 8');
      ok(posts.length === 9 && /consegna/.test(posts[8]) && /codici_recupero_scaricati":16/.test(posts[8]) && !/GEZD/.test(posts.join('')), 'segnali: ' + posts.length + ' invii, consegna senza segreti');
    }
    await ctx.close();
  }
  await b.close(); srv.close(); console.log(fail ? 'FALLITO ' + fail : 'TUTTO OK'); process.exit(fail ? 1 : 0);
})();
