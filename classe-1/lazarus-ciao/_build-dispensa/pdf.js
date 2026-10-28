// PDF della dispensa «Lazarus: il mio primo programma» (3 lingue). Uso: node _build-dispensa/pdf.js
const fs = require('fs'), path = require('path'); const OUT = path.resolve(__dirname, '..');
(async () => { const { chromium } = require('playwright'); const b = await chromium.launch();
  for (const f of fs.readdirSync(OUT).filter(x => /^20261028_Classe-1_v[\d.]+_Lazarus-Primo-Programma_(IT|AR|ZH)\.html$/.test(x))) {
    const p = await b.newPage(); await p.goto('file://' + path.join(OUT, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const lg = f.match(/_(IT|AR|ZH)\.html$/)[1], tit = await p.title();
    const pag = { IT: 'pag. <span class="pageNumber"></span> di <span class="totalPages"></span>', AR: 'صفحة <span class="pageNumber"></span> من <span class="totalPages"></span>', ZH: '第 <span class="pageNumber"></span> 页，共 <span class="totalPages"></span> 页' }[lg];
    const st = 'font-size:8pt;width:100%;padding:0 16mm;color:#5c6672;display:flex;justify-content:space-between;font-family:"DejaVu Sans","WenQuanYi Zen Hei",sans-serif';
    await p.pdf({ path: path.join(OUT, f.replace('.html', '.pdf')), format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: `<div style="${st}"><span dir="auto">${tit}</span><span>1INF · 2026/27</span></div>`,
      footerTemplate: `<div style="${st}"><span>Corso di Informatica · Classe 1 · Versione 1.0 — 28/10/2026</span><span dir="auto">${pag}</span></div>`,
      margin: { top: '20mm', bottom: '18mm', left: '16mm', right: '16mm' } });
    console.log(f.replace('.html', '.pdf')); } await b.close(); })();
