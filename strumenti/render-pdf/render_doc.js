// Render di un DOCUMENTO in PDF con HEADER e FOOTER di pagina (numeri di pagina inclusi).
// Uso: node render_doc.js <htmlPath assoluto> <pdfPath> "<headerLeft>" "<headerRight>" "<footerLeft>"
// Il footer mostra sempre a destra: pag. N / Tot.
const { chromium } = require('playwright');
const [, , htmlPath, pdfPath, headerLeft = '', headerRight = '', footerLeft = ''] = process.argv;
const EXE = process.env.PW_EXECUTABLE || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const esc = s => String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
(async () => {
  const browser = await chromium.launch({ executablePath: EXE });
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  const fcol = footerLeft.startsWith('RISERVATO') ? '#8a2a1c' : '#12467a';
  const header = `<div style="font-size:8px;width:100%;padding:0 15mm;color:#12467a;display:flex;justify-content:space-between">`
    + `<span>${esc(headerLeft)}</span><span>${esc(headerRight)}</span></div>`;
  const footer = `<div style="font-size:8px;width:100%;padding:0 15mm;color:${fcol};display:flex;justify-content:space-between">`
    + `<span>${esc(footerLeft)}</span>`
    + `<span>pag. <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
  await page.pdf({
    path: pdfPath, format: 'A4', printBackground: true,
    displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer,
    margin: { top: '20mm', bottom: '16mm', left: '17mm', right: '17mm' }
  });
  await browser.close();
  console.log('OK ' + pdfPath);
})().catch(e => { console.error(e); process.exit(1); });
