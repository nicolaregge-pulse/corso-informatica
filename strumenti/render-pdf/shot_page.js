// Screenshot generico di una pagina HTML locale -> PNG. Args: htmlPath pngPath
const { chromium } = require(process.env.NODE_PATH + '/playwright');
(async () => {
  const [htmlPath, pngPath] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 640, height: 520 }, deviceScaleFactor: 2 });
  try { await p.goto('file://' + htmlPath, { waitUntil: 'domcontentloaded', timeout: 8000 }); } catch (e) {}
  await p.waitForTimeout(1200);
  try { await p.screenshot({ path: pngPath }); } catch (e) { console.error('shot-fail', e.message); process.exit(2); }
  await b.close();
  console.log('ok');
})().catch(e => { console.error(e.message); process.exit(1); });
