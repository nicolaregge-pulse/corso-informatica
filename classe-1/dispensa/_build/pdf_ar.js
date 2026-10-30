// PDF della dispensa unica 1INF in arabo. Uso: NODE_PATH=$(npm root -g) node classe-1/dispensa/_build/pdf_ar.js [X.Y]
// con la versione X.Y rifà solo quel PDF (le versioni già consegnate restano congelate)
const fs = require('fs'), path = require('path'); const OUT = path.resolve(__dirname, '..');
(async () => { const { chromium } = require('playwright'); const b = await chromium.launch();
  for (const f of fs.readdirSync(OUT).filter(x => /^dispensa-1inf-ar-v[\d.]+\.html$/.test(x) && (!process.argv[2] || x === `dispensa-1inf-ar-v${process.argv[2]}.html`))) {
    const p = await b.newPage(); await p.goto('file://' + path.join(OUT, f)); await p.waitForTimeout(800);
    await p.pdf({ path: path.join(OUT, f.replace('.html', '.pdf')), format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-family:DejaVu Sans;font-size:8pt;width:100%;text-align:center;color:#5c6672">Dispensa unica 1INF · AR · ${f.replace('.html', '').replace('dispensa-1inf-ar-', '')} · <span class="pageNumber"></span> / <span class="totalPages"></span></div>`,
      margin: { top: '14mm', bottom: '16mm', left: '15mm', right: '15mm' } });
    console.log(f.replace('.html', '.pdf')); }
  await b.close(); })();
