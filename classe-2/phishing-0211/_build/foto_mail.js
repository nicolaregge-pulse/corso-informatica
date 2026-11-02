// Fotografa mail-N.html in mail-N.png (playwright). Uso: node foto_mail.js <cartella mail>
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
(async () => { const dir = process.argv[2], b = await chromium.launch(), p = await b.newPage({ viewport: { width: 900, height: 900 }, deviceScaleFactor: 1.5 });
  for (const f of fs.readdirSync(dir).filter(x => /^mail-\d+\.html$/.test(x))) { await p.goto('file://' + path.resolve(dir, f)); await (await p.$('#mail')).screenshot({ path: path.resolve(dir, f.replace('.html', '.png')) }); }
  await b.close(); console.log('png ok'); })();
