// audit_e2e_pagina.js (29/10/2026): parte «Rendering» di strumenti/audit_e2e.py (anello 3).
// Apre il cruscotto unico servito da un server locale con i file del COMMIT PUBBLICATO, come il docente:
// browser nuovo (niente localStorage), 390 px, modalità Docente, codice del docente in sessionStorage «tokmon».
// Uso: node strumenti/audit_e2e_pagina.js <config.json> <uscita.json>
// config: {base, sito_dir, tok, prova, data, oggi, classi: [{classe, titoli: [...]}]}
// Scrive per ogni classe: testo delle linguette, bottoni del piano, file JSON caricati, errori JS.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const cfg = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = { classi: [] };
  const browser = await chromium.launch();
  for (const cl of cfg.classi) {
    const r = { classe: cl.classe, errori_js: [], console_errori: [], json: [], bloccati: [], schede: {} };
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
    // raw.githubusercontent.com (dati dal vivo delle pagine docente): servito dai file dello stesso commit pubblicato
    await ctx.route(/https:\/\/raw\.githubusercontent\.com\/nicolaregge-pulse\/corso-informatica\/main\/(.*?)(\?.*)?$/, async (route) => {
      const m = route.request().url().match(/\/main\/([^?]*)/);
      const f = path.join(cfg.sito_dir, decodeURIComponent(m[1]));
      if (fs.existsSync(f)) await route.fulfill({ path: f, headers: { 'access-control-allow-origin': '*' } });
      else await route.fulfill({ status: 404, body: '' });
    });
    // tutto il resto fuori dal server locale: non raggiungibile da questo ambiente, lo si annota
    await ctx.route(u => !u.href.startsWith(cfg.base) && !/raw\.githubusercontent\.com/.test(u.href), async (route) => {
      r.bloccati.push(route.request().url().slice(0, 120));
      await route.abort();
    });
    if (cfg.tok) await ctx.addInitScript(t => { try { sessionStorage.setItem('tokmon', t); } catch (e) {} }, cfg.tok);
    const p = await ctx.newPage();
    p.on('pageerror', e => r.errori_js.push(String(e).slice(0, 300)));
    p.on('console', m => { if (m.type() === 'error') r.console_errori.push(m.text().slice(0, 200)); });
    p.on('response', resp => { const u = resp.url(); if (/\.json(\?|$)/.test(u)) r.json.push({ url: u.split('?')[0], stato: resp.status() }); });
    const q = '&ruolo=docente&classe=' + cl.classe + (cfg.prova ? '&prova=1' : '');
    const tokOk = async () => { for (let i = 0; i < 20; i++) { if (await p.evaluate(() => !!window.TOK_OK).catch(() => false)) return true; await p.waitForTimeout(500); } return false; };
    try {
      // 1) Piano del giorno della DATA dell'audit
      await p.goto(cfg.base + 'cruscotto/?tab=piano&giorno=' + cfg.data + q, { waitUntil: 'load' });
      r.codice_docente_accettato = await tokOk();
      await p.waitForTimeout(2500);
      const piano = p.locator('#t-piano');
      r.schede.piano = {
        testo: (await piano.innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 1500),
        scelgo: await piano.locator('button', { hasText: 'Scelgo questa' }).count(),
        pubblica: await piano.locator('button', { hasText: 'Pubblica' }).count(),
        titoli_visti: [],
      };
      for (const t of cl.titoli || []) if (r.schede.piano.testo.indexOf(t.replace(/\s+/g, ' ').slice(0, 40)) >= 0) r.schede.piano.titoli_visti.push(t);
      // 2) Le altre linguette con il giorno di OGGI (i dati devono essere di oggi)
      await p.goto(cfg.base + 'cruscotto/?tab=oggi&giorno=' + cfg.oggi + q, { waitUntil: 'load' });
      await tokOk();
      await p.waitForTimeout(4000);
      for (const t of ['oggi', 'domande', 'uscite', 'script', 'riepilogo']) {
        const b = p.locator('#tabs button[data-t="' + t + '"]');
        if (await b.count()) { await b.first().click(); await p.waitForTimeout(t === 'oggi' ? 2000 : 3500); }
        const s = { visibile: await p.locator('#t-' + t).isVisible().catch(() => false) };
        s.testo = (await p.locator('#t-' + t).innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 1500);
        const fr = t === 'oggi' ? '#vista' : t === 'uscite' ? '#usc' : null;
        if (fr) {
          const h = await p.locator(fr).elementHandle().catch(() => null);
          const f = h ? await h.contentFrame() : null;
          s.frame_url = f ? f.url() : '';
          s.testo = f ? (await f.locator('body').innerText().catch(() => '')).replace(/\s+/g, ' ').slice(0, 1500) : '';
        }
        if (t === 'oggi') s.nota = (await p.locator('#nota').innerText().catch(() => '')).trim();
        r.schede[t] = s;
      }
      r.larghezza = await p.evaluate(() => document.documentElement.scrollWidth);
    } catch (e) {
      r.errore = String(e).slice(0, 300);
    }
    await ctx.close();
    out.classi.push(r);
  }
  await browser.close();
  fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
})().catch(e => { console.error(String(e)); process.exit(1); });
