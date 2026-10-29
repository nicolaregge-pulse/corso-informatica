// HTML -> PDF A4 con Chromium (Playwright). Uso: node render_pdf.js <file.html> <file.pdf>
// PDF_OUTLINE=1 aggiunge i segnalibri (libro totale). CHROMIUM_PATH indica il browser.
const { chromium } = require('playwright');
const [, , HTML, PDF] = process.argv;
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
  const page = await browser.newPage();
  await page.goto('file://' + HTML, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const opts = {
    path: PDF, format: 'A4', printBackground: true, displayHeaderFooter: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#8a97a5;font-family:Arial,sans-serif;padding:0 16mm;display:flex;justify-content:space-between;">'
      + '<span>Corso di Informatica — prof. Nicola Regge</span><span>Pag. <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  };
  if (process.env.PDF_OUTLINE) {
    try { await page.pdf({ ...opts, tagged: true, outline: true }); } catch (e) { await page.pdf(opts); }
  } else { await page.pdf(opts); }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
