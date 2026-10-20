// Genera le slide per la lezione frontale (HTML + PDF) dalla banca docs/verifica/banche/2inf-while.js
// Uso: NODE_PATH=$(npm root -g) node classe-1/byte-velocita/_build/gen_slide.js
const fs = require('fs'), path = require('path');
const R = path.resolve(__dirname, '../../..'), OUT = path.resolve(__dirname, '..');
global.window = {}; require(R + '/docs/verifica/banche/2inf-while.js'); const B = window.BANCA;
const NOME = '20261020_Classe-2-PerTutti_v1.0_Ciclo-While-Dado_IT';
const css = `@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:"DejaVu Sans",Arial,sans-serif;color:#1b2430;--mu:#5c6672;--ln:#b9c2cc}
.s{width:297mm;height:210mm;padding:14mm 18mm;page-break-after:always;display:flex;flex-direction:column;overflow:hidden;border-top:10mm solid #1f6feb}
h1{font-size:30pt;margin:0 0 6mm;line-height:1.15}h1 span{font-size:17pt!important}
.t{font-size:19pt;line-height:1.4}.t table{font-size:16pt!important}.t td,.t th{padding:4px 10px!important}
[lang=ar]{font-family:Amiri,serif;font-size:1.05em!important}[lang=zh]{font-family:"WenQuanYi Zen Hei",sans-serif}
.pie{margin-top:auto;font-size:11pt;color:#5c6672}.cop{justify-content:center;text-align:center}.cop h1{font-size:40pt}`;
let h = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Il ciclo WHILE</title><style>${css}</style></head><body>`;
h += `<div class="s cop"><h1>Il ciclo WHILE<br>«ripeti finché…»</h1><div class="t">Lancia il dado finché esce il tuo numero magico</div><div class="pie">Classe 2 · Informatica · Lazarus · 20/10/2026 · v1.0</div></div>`;
B.schede.forEach((s, i) => { const tt = [s.titolo]; h += `<div class="s"><h1>${tt[0]}<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:#5c6672">${tt[1] || ''}</span><span lang="zh" style="display:block;font-weight:400;color:#5c6672">${tt[2] || ''}</span></h1><div class="t">${s.testo}</div><div class="pie">Il ciclo WHILE · ${i + 1} / ${B.schede.length}</div></div>`; });
h += `<div class="s cop"><h1>Adesso tocca a te!</h1><div class="t">Apri Lazarus e costruisci il gioco del dado.<br>Poi la verifica sulla pagina della lezione.</div></div></body></html>`;
fs.writeFileSync(`${OUT}/${NOME}.html`, h);
(async () => { const { chromium } = require('playwright'); const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage(); await p.goto('file://' + `${OUT}/${NOME}.html`); await p.waitForTimeout(400);
  await p.evaluate(() => document.querySelectorAll('.s').forEach(s => { const t = s.querySelector('.t'); let f = 19; while (s.scrollHeight > s.clientHeight + 1 && f > 11) { f -= 0.5; t.style.fontSize = f + 'pt'; t.querySelectorAll('table').forEach(x => x.style.setProperty('font-size', (f - 3) + 'pt', 'important')); } }));
  fs.writeFileSync(`${OUT}/${NOME}.html`, await p.content());
  await p.pdf({ path: `${OUT}/${NOME}.pdf`, landscape: true, format: 'A4', printBackground: true }); await b.close(); console.log(`${OUT}/${NOME}.pdf`); })();
