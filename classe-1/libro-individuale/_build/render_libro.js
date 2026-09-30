// Render del libro individuale in PDF con header/footer di pagina.
// Uso: node render_libro.js <htmlPath assoluto> <pdfPath assoluto> "<Nome Allievo>"
// Richiede playwright disponibile (NODE_PATH) e un Chromium (PW_EXECUTABLE o path noto).
const { chromium } = require('playwright');
const [, , htmlPath, pdfPath, nome = '', footerLeft = 'RISERVATO — non pubblicare', headerLeftOverride = ''] = process.argv;
const EXE = process.env.PW_EXECUTABLE || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const esc = s => String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
(async () => {
  const browser = await chromium.launch({ executablePath: EXE });
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  const headerLeft = headerLeftOverride || ('Il mio libro di Informatica — ' + esc(nome));
  const footerColor = footerLeft.startsWith('RISERVATO') ? '#8a2a1c' : '#12467a';
  const header = `<div style="font-size:8px;width:100%;padding:0 12mm;color:#12467a;display:flex;justify-content:space-between">`
    + `<span>${headerLeft}</span>`
    + `<span>Classe 1 INF · a.s. 2026/27</span></div>`;
  const footer = `<div style="font-size:8px;width:100%;padding:0 12mm;color:${footerColor};display:flex;justify-content:space-between">`
    + `<span>${esc(footerLeft)}</span>`
    + `<span>pag. <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
  await page.pdf({
    path: pdfPath, format: 'A4', printBackground: true,
    displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer,
    margin: { top: '20mm', bottom: '16mm', left: '12mm', right: '12mm' }
  });
  await browser.close();
  console.log('OK ' + pdfPath);
})().catch(e => { console.error(e); process.exit(1); });
