// Legge le banche delle pagine della lezione (docs/verifica/banche/*.js) e scrive titolo e schede in JSON.
// Uso: node estrai_banche.js <cartella banche> <file.json>
const fs = require('fs'); const d = process.argv[2]; const o = {};
for (const f of fs.readdirSync(d)) {
  if (!f.endsWith('.js')) continue;
  global.window = {}; global.document = {};
  try { eval(fs.readFileSync(d + '/' + f, 'utf8')); const B = window.BANCA; o[f] = { titolo: B.titolo, sotto: B.sotto, schede: B.schede || [] }; } catch (e) {}
}
fs.writeFileSync(process.argv[3], JSON.stringify(o));
