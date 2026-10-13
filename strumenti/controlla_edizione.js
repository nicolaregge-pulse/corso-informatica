// Prova nel browser per controlla_edizione.py: ogni pagina sul telefono (390 px) e sul computer (1280 px),
// errori di JavaScript, file mancanti, pagina più larga dello schermo; poi il racconto fino in fondo con una voce simulata.
// Le pagine dei giochi con file facoltativi (un mostro per ogni PC) non contano come errore.
const { chromium } = require('playwright'); const fs = require('fs');
const FACOLTATIVI = [/assalto-dei-mostri\/mostri\/pc\d+\.(json|png)/];
(async () => {
  const pagine = fs.readFileSync(process.argv[2], 'utf8').trim().split('\n').filter(Boolean);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--use-gl=swiftshader', '--enable-webgl'] });
  let ko = 0;
  for (const vp of [{ width: 390, height: 844 }, { width: 1280, height: 800 }]) {
    const ctx = await b.newContext({ viewport: vp });
    for (const u of pagine) {
      const p = await ctx.newPage(); const errs = [], fail = [];
      p.on('pageerror', e => errs.push(e.message.slice(0, 80)));
      p.on('response', r => { if (r.status() >= 400 && r.url().startsWith('http://localhost') && !FACOLTATIVI.some(x => x.test(r.url()))) fail.push(r.status() + ' ' + r.url().replace('http://localhost:8799/', '')); });
      try {
        await p.goto('http://localhost:8799/' + u, { waitUntil: 'load', timeout: 20000 }); await p.waitForTimeout(1200);
        const w = await p.evaluate(() => document.documentElement.scrollWidth);
        if (errs.length || fail.length || w > vp.width + 2) { ko++; console.log('KO', vp.width + 'px', u, w > vp.width + 2 ? 'più larga dello schermo (' + w + ')' : '', errs.join(' ; '), fail.slice(0, 3).join(' ; ')); }
      } catch (e) { ko++; console.log('KO', vp.width + 'px', u, e.message.slice(0, 80)); }
      await p.close();
    }
    await ctx.close();
  }
  // il racconto fino alla fine, con una voce finta che «parla» subito
  const p = await b.newPage({ viewport: { width: 1280, height: 800 } }); const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.addInitScript(() => { window.__detti = 0; const S = { speaking: false, getVoices: () => [{ name: 'Alice', lang: 'it-IT' }], cancel() {}, pause() {}, resume() {},
    speak(u) { window.__detti++; setTimeout(() => u.onend && u.onend(), 30); }, onvoiceschanged: null };
    Object.defineProperty(window, 'speechSynthesis', { value: S }); window.SpeechSynthesisUtterance = function (t) { this.text = t; }; });
  await p.goto('http://localhost:8799/cm-qma7yay4q5/racconto/'); await p.click('#via');
  let fine = false; const t0 = Date.now();
  while (Date.now() - t0 < 150000) { await p.waitForTimeout(1000); if (/Guarda di nuovo/.test(await p.textContent('#scena'))) { fine = true; break; } }
  const detti = await p.evaluate(() => window.__detti);
  if (!fine || errs.length) { ko++; console.log('KO racconto: fine', fine, 'frasi', detti, errs.join(' ; ')); }
  await b.close();
  console.log(`browser: ${pagine.length} pagine × 2 schermi, racconto ${fine ? 'fino in fondo' : 'NON finito'} (${detti} frasi dette), problemi ${ko}`);
})();
