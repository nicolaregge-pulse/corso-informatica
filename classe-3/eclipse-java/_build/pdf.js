// PDF della guida Eclipse 3INF. Uso: NODE_PATH=$(npm root -g) node classe-3/eclipse-java/_build/pdf.js
const fs = require('fs'), path = require('path'); const OUT = path.resolve(__dirname, '..');
(async () => { const { chromium } = require('playwright'); const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const f of fs.readdirSync(OUT).filter(x => x.endsWith('.html') && x.includes('Eclipse-Hello-World'))) { const p = await b.newPage(); await p.goto('file://' + path.join(OUT, f)); await p.waitForTimeout(800);
    await p.pdf({ path: path.join(OUT, f.replace('.html', '.pdf')), format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-size:8pt;width:100%;text-align:center;color:#5c6672">${f.replace('.html','')} · Pagina <span class="pageNumber"></span> / <span class="totalPages"></span></div>`, margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' } });
    console.log(f.replace('.html', '.pdf')); } await b.close(); })();
