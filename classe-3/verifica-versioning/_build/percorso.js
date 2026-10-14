(function () {
  var ID = '3inf-versioning-20261014', L = 'perc-3inf-verifica-', R = null, REC = null;
  var ORDINE = ['nome', 'rip', 'ver', 'val', 'rec'];
  function $(i) { return document.getElementById(i); }
  function g(k) { try { return localStorage.getItem(k); } catch (x) { return null; } }
  function s(k, v) { try { localStorage.setItem(k, v); } catch (x) {} }
  function e(x) { return String(x == null ? '' : x).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function nome() { return (g('nome-3inf') || '').trim(); }
  function breve(x) { var p = (x || '').trim().split(/\s+/); if (!p[0]) return ''; var a = p[0].charAt(0).toUpperCase() + p[0].slice(1).toLowerCase(); return p.length > 1 ? a + ' ' + p[p.length - 1].charAt(0).toUpperCase() + '.' : a; }
  function esito(m) { try { var r = JSON.parse(g('esito-' + ID + '-' + m) || 'null'); return r && r.consegnata ? r : null; } catch (x) { return null; } }
  function spegni(el) { if (el) el.classList.add('spento'); }
  function mioRisultato() { var me = breve(nome()); return (R && R.allievi || []).filter(function (x) { return x.allievo === me; })[0]; }
  function mioRecupero() { var me = breve(nome()); return (REC && REC.allievi || []).filter(function (x) { return x.allievo === me; })[0]; }
  function fatto(k) {
    if (k === 'nome') return nome().indexOf(' ') > 0;
    if (k === 'rip') return !!g(L + 'rip');
    if (k === 'ver') return !!esito('verifica');
    if (k === 'val') return !!mioRisultato();
    if (k === 'rec') { var r = mioRecupero(); return !!(r && r.fatto); }
  }
  function disegna() {
    var ora = null;
    ORDINE.forEach(function (k) { var sec = $('p-' + k), f = fatto(k); if (!f && !ora) ora = k; sec.classList.toggle('fatto', f); sec.classList.toggle('ora', ora === k); sec.querySelector('.bollo').textContent = f ? '✓ Fatto' : (ora === k ? 'Adesso' : 'Da fare'); });
    if (fatto('nome')) { $('nome').value = nome(); $('esNome').style.color = '#1a7f37'; $('esNome').textContent = 'Ciao ' + breve(nome()) + '!'; }
    if (fatto('rip')) spegni($('bRip'));
    if (fatto('ver')) { spegni($('bVer')); spegni($('bRip')); $('bVer').textContent = '✓ Verifica fatta'; if (!mioRisultato()) $('val').innerHTML = '<b>Verifica consegnata.</b> Il prof sta correggendo: il voto e il perché compaiono qui da soli.<div class="bn" lang="bn">পরীক্ষা জমা হয়েছে। নম্বর এখানে আসবে।</div>'; }
    var a = mioRisultato();
    if (a) $('val').innerHTML = '<div style="font-size:30px;font-weight:800">Voto: ' + e(a.voto) + '</div>' + (a.aree || []).map(function (z) { return '<div>' + e(z.nome) + ': <b>' + e(z.giuste) + ' su ' + e(z.su) + '</b></div>'; }).join('') +
      (a.scritte ? '<div style="margin-top:6px"><b>Risposte scritte:</b> ' + e(a.scritte) + '</div>' : '') + (a.giudizio ? '<div style="margin-top:6px"><b>Perché questo voto:</b> ' + e(a.giudizio) + '</div>' : '');
    var r = mioRecupero();
    if (r) $('rec').innerHTML = (r.fatto ? '<b>✓ Recupero fatto.</b> ' : '') + (r.testo ? e(r.testo) + ' ' : '') + (r.link && !r.fatto ? '<br><a class="bot" href="' + e(r.link) + '" target="_blank" rel="noopener">Il mio recupero</a>' : '') + (r.voto_complessivo ? '<div style="font-size:26px;font-weight:800;margin-top:6px">Voto complessivo: ' + e(r.voto_complessivo) + '</div>' : '');
  }
  function j(u) { return fetch(u + '?t=' + Date.now(), { cache: 'no-store' }).then(function (x) { return x.json(); }).catch(function () { return null; }); }
  function carica() { Promise.all([j('../../verifica/risultati/3inf-versioning.json'), j('recupero.json')]).then(function (x) { R = x[0]; REC = x[1]; disegna(); }); }
  $('okNome').onclick = function () { var v = $('nome').value.trim().replace(/\s+/g, ' '); if (v.indexOf(' ') < 0) { $('esNome').style.color = '#c0392b'; $('esNome').textContent = 'Scrivi nome E cognome.'; return; } s('nome-3inf', v); if (!g('nome-' + ID)) s('nome-' + ID, JSON.stringify(v)); disegna(); };
  $('nome').addEventListener('keydown', function (ev) { if (ev.key === 'Enter') $('okNome').click(); });
  $('bRip').addEventListener('click', function () { s(L + 'rip', '1'); setTimeout(disegna, 500); });
  carica(); setInterval(carica, 60000); window.addEventListener('focus', disegna); document.addEventListener('visibilitychange', disegna);
})();
