/* Lezione 3INF 14/10/2026: percorso unico; il passo fatto diventa verde e il suo bottone si spegne. */
(function () {
  var ID = '3inf-versioning-20261014', L = 'perc-3inf-merge-', R = null;
  var ORDINE = ['nome', 'teoria', 'gioca', 'changelog', 'rev', 'pr', 'bk', 'sprint', 'rip', 'ver', 'val', 'fw'];
  function $(i) { return document.getElementById(i); }
  function g(k) { try { return localStorage.getItem(k); } catch (x) { return null; } }
  function s(k, v) { try { localStorage.setItem(k, v); } catch (x) {} }
  function n(k) { return parseInt(g(L + k) || '0', 10); }
  function e(x) { return String(x == null ? '' : x).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function rosso(el, t) { el.style.color = '#c0392b'; el.innerHTML = t; } function verde(el, t) { el.style.color = '#1a7f37'; el.innerHTML = t; }
  function nome() { return (g('nome-3inf') || '').trim(); }
  function breve(x) { var p = (x || '').trim().split(/\s+/); if (!p[0]) return ''; var a = p[0].charAt(0).toUpperCase() + p[0].slice(1).toLowerCase(); return p.length > 1 ? a + ' ' + p[p.length - 1].charAt(0).toUpperCase() + '.' : a; }
  function esito(m) { try { var r = JSON.parse(g('esito-' + ID + '-' + m) || 'null'); return r && r.consegnata ? r : null; } catch (x) { return null; } }
  function spegni(el) { if (el) el.classList.add('spento'); }
  function fatto(k) {
    if (k === 'nome') return nome().indexOf(' ') > 0;
    if (k === 'pr') return n('pr') >= 3;
    if (k === 'ver') return !!esito('verifica');
    if (k === 'val') return !!esito('recupero');
    return n(k) > 0;
  }
  function disegna() {
    var ora = null;
    ORDINE.forEach(function (k) {
      var sec = $('p-' + k), f = fatto(k); if (!f && !ora) ora = k;
      sec.classList.toggle('fatto', f); sec.classList.toggle('ora', ora === k);
      sec.querySelector('.bollo').textContent = f ? '✓ Fatto' : (ora === k ? 'Adesso' : 'Da fare');
    });
    if (fatto('nome')) { $('nome').value = nome(); verde($('esNome'), 'Ciao ' + e(breve(nome())) + '!'); }
    if (fatto('teoria')) [].forEach.call(document.querySelectorAll('#quiz button'), spegni);
    if (fatto('gioca')) spegni($('bGioca'));
    if (fatto('changelog')) spegni($('bChangelog'));
    if (fatto('bk')) { $('t-bk').disabled = true; [].forEach.call(document.querySelectorAll('#p-bk .bot'), spegni); verde($('e-bk'), '✓ Risposte mandate.'); }
    if (fatto('sprint')) spegni($('bSprint'));
    if (fatto('fw')) { $('t-fw').disabled = true; [].forEach.call(document.querySelectorAll('#p-fw .bot'), spegni); verde($('e-fw'), '✓ Grazie: le tue note aiutano il prof.'); }
    if (fatto('rev')) { ['t-rev'].forEach(function (i) { $(i).disabled = true; }); [].forEach.call(document.querySelectorAll('#p-rev .bot'), spegni); verde($('e-rev'), '✓ Revisione mandata.'); }
    var np = n('pr');
    $('contaPR').innerHTML = 'Richieste mandate: <b>' + np + (np >= 3 ? '</b> · ✓ le 3 obbligatorie sono fatte: puoi mandarne altre' : ' di 3</b>') + ' · পাঠানো অনুরোধ: ' + np + (np >= 3 ? ' ✓' : '/3');
    if (fatto('rip')) spegni($('bRip'));
    var v = esito('verifica');
    if (v) { spegni($('bVer')); spegni($('bRip')); $('bVer').textContent = '✓ Verifica fatta'; }
    var me = breve(nome()), a = (R && R.allievi || []).filter(function (x) { return x.allievo === me; })[0];
    if (v && !a) $('val').innerHTML = '<b>Verifica consegnata.</b> Il prof sta correggendo: la tua valutazione compare qui da sola.<div class="bn" lang="bn">পরীক্ষা জমা হয়েছে। শিক্ষক দেখছেন: আপনার মূল্যায়ন এখানে নিজে থেকে আসবে।</div>';
    if (a) {
      $('val').innerHTML = '<div style="font-size:30px;font-weight:800">Voto: ' + e(a.voto) + '</div>' + (a.aree || []).map(function (z) { return '<div>' + e(z.nome) + ': <b>' + e(z.giuste) + ' su ' + e(z.su) + '</b></div>'; }).join('') +
        (a.scritte ? '<div style="margin-top:6px"><b>Risposte scritte:</b> ' + e(a.scritte) + '</div>' : '') + (a.giudizio ? '<div style="margin-top:6px"><b>Il giudizio del prof:</b> ' + e(a.giudizio) + '</div>' : '');
      $('bRec').hidden = false; if (esito('recupero')) { spegni($('bRec')); $('bRec').textContent = '✓ Recupero fatto'; }
    }
  }
  function carica() { fetch('../../verifica/risultati/3inf-versioning.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (d) { R = d; disegna(); }).catch(disegna); }
  $('okNome').onclick = function () { var v = $('nome').value.trim().replace(/\s+/g, ' '); if (v.indexOf(' ') < 0) return rosso($('esNome'), 'Scrivi nome E cognome. · নাম ও পদবি লিখুন।'); s('nome-3inf', v); if (!g('nome-' + ID)) s('nome-' + ID, JSON.stringify(v)); disegna(); };
  $('nome').addEventListener('keydown', function (ev) { if (ev.key === 'Enter') $('okNome').click(); });
  $('quiz').addEventListener('click', function (ev) { var b = ev.target.closest('button'); if (!b) return; var q = b.parentNode, es = q.querySelector('.esito');
    [].forEach.call(q.querySelectorAll('button'), function (x) { x.className = ''; }); b.className = b.dataset.g === '1' ? 'si' : 'no';
    if (b.dataset.g === '1') verde(es, 'Giusto!'); else rosso(es, 'Riprova: rileggi le 4 frasi. · আবার চেষ্টা করুন।');
    if (document.querySelectorAll('#quiz button.si').length === 4) { s(L + 'teoria', '1'); setTimeout(disegna, 600); } });
  $('bGioca').addEventListener('click', function () { s(L + 'gioca', '1'); setTimeout(disegna, 500); });
  $('bChangelog').addEventListener('click', function () { s(L + 'changelog', '1'); setTimeout(disegna, 500); });
  $('bSprint').addEventListener('click', function () { s(L + 'sprint', '1'); setTimeout(disegna, 500); });
  $('bRip').addEventListener('click', function () { s(L + 'rip', '1'); setTimeout(disegna, 500); });
  // Revisione e PR: «Copia» prepara il testo; «Apri il Modulo» dopo la copia conta come mandata (il prof la vede nel Modulo).
  [].forEach.call(document.querySelectorAll('[data-copia]'), function (b) {
    b.onclick = function () {
      var k = b.dataset.copia, es = $('e-' + k), t = $('t-' + k).value.trim();
      if (!fatto('nome')) return rosso(es, 'Prima scrivi il tuo nome al Passo 1. · প্রথমে ধাপ ১-এ নাম লিখুন।');
      if (t.length < 15) { $('t-' + k).focus(); return rosso(es, 'Scrivi almeno una frase completa. · অন্তত একটি সম্পূর্ণ বাক্য লিখুন।'); }
      var testo = nome() + ' — ' + (k === 'rev' ? 'REVISIONE' : k === 'bk' ? 'ANALISI DEL BACKLOG' : k === 'fw' ? 'NOTE SUL FRAMEWORK' : 'PR' + (n('pr') + 1)) + ': ' + t;
      navigator.clipboard.writeText(testo).then(function () { s(L + k + '-copiata', '1'); verde(es, 'Copiata! Ora premi «Apri il Modulo». · কপি হয়েছে! এখন «Apri il Modulo» চাপুন।'); });
    };
  });
  [].forEach.call(document.querySelectorAll('[data-apri]'), function (a) {
    a.addEventListener('click', function () {
      var k = a.dataset.apri; if (!g(L + k + '-copiata')) return;
      s(L + k + '-copiata', ''); s(L + k, String(n(k) + 1)); $('t-' + k).value = '';
      verde($('e-' + k), 'Nel Modulo: prima casella, poi Ctrl+V nella seconda, poi «Invia».'); setTimeout(disegna, 500);
    });
  });
  carica(); setInterval(carica, 60000); window.addEventListener('focus', disegna); document.addEventListener('visibilitychange', disegna);
})();
