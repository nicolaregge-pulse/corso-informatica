/* server di raccolta finto: serve la pagina di prova e lo snippet, registra i POST su /evento, li elenca su /eventi */
const http = require('http'), fs = require('fs'), path = require('path');
const ev = [];
http.createServer((q, r) => {
  if (q.method === 'POST' && q.url === '/evento') { let b = ''; q.on('data', c => b += c); q.on('end', () => { try { ev.push(JSON.parse(new URLSearchParams(b).get('d'))); } catch (e) { ev.push({ errore: 'json' }); } r.end('ok'); }); return; }
  if (q.url === '/eventi') { r.setHeader('content-type', 'application/json'); return r.end(JSON.stringify(ev)); }
  const f = q.url === '/segnala.js' ? path.join(__dirname, '..', 'segnala-avanzamento-v1.0.js') : path.join(__dirname, 'pagina-prova.html');
  r.setHeader('content-type', q.url === '/segnala.js' ? 'text/javascript' : 'text/html; charset=utf-8'); r.end(fs.readFileSync(f));
}).listen(8765, () => console.log('pronto'));
