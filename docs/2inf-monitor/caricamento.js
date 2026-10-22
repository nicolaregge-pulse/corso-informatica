// 22/10/2026: riquadro grande «chi ha caricato la cartella su GitHub e chi manca», uguale per ragazzi e docente.
// d = lazarus.json (ora, cartella, scadenza, righe[{alunno, caricato}]). Restituisce l'HTML del riquadro.
function bannerCaricamento(d) {
  if (!d || !d.righe || !d.scadenza) return '';
  var e = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var si = d.righe.filter(function (r) { return r.caricato; }), no = d.righe.filter(function (r) { return !r.caricato; });
  var ora = new Date().toLocaleTimeString('it-IT', { timeZone: 'Europe/Rome', hour: '2-digit', minute: '2-digit' });
  var scaduto = ora > d.scadenza, tutti = !no.length;
  var col = tutti ? '#1f7a3f' : (scaduto ? '#e0413a' : '#d08a00');
  return '<div style="border:3px solid ' + col + ';border-radius:14px;padding:14px 16px;margin:12px 0;font-size:18px;line-height:1.5">' +
    '<b style="font-size:22px;color:' + col + '">💾 Cartella «' + e(d.cartella) + '» su GitHub: entro le ' + e(d.scadenza) + (scaduto && !tutti ? ' (tempo scaduto)' : '') + '</b><br>' +
    '<b>' + e(d.si || 'Caricato') + ' ' + si.length + ' su ' + d.righe.length + '</b> · controllo delle ' + e(d.ora) + ' (ogni 5 minuti)<br>' +
    '<span style="color:#1f7a3f">✔ ' + e(d.si || 'Caricato') + ': ' + (si.length ? si.map(function (r) { return e(r.alunno); }).join(', ') : 'ancora nessuno') + '</span><br>' +
    (no.length ? '<span style="color:#e0413a">✘ ' + e(d.no || 'Manca') + ': ' + no.map(function (r) { return e(r.alunno); }).join(', ') + '</span>' : '<span style="color:#1f7a3f">Tutti hanno caricato. Bravi!</span>') +
    '</div>';
}
