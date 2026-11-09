/* 2INF 09/11/2026, ora 5: dispensa in linea a schede. Un solo gruppo di schede visibile alla volta; indice in alto; il bottone «Vai qui adesso»
   apre da solo la scheda giusta. Senza questo file le schede restano nascoste (c'è un <noscript> che le mostra tutte). */
(function () {
  function tutti(s, d) { return [].slice.call((d || document).querySelectorAll(s)); }
  var TAB = tutti('.tab');
  function apri(id, scorri) {
    var t = document.getElementById('t-' + id); if (!t) return;
    TAB.forEach(function (x) { x.classList.toggle('on', x === t); });
    tutti('#indice button').forEach(function (b) { b.classList.toggle('sel', b.getAttribute('data-t') === id); });
    try { sessionStorage.setItem('tab-2inf0911-ora5', id); } catch (x) {}
    if (scorri) { var i = document.getElementById('indice'); if (i) i.scrollIntoView({ block: 'start' }); }
  }
  function dellaScheda(el) { var t = el && el.closest ? el.closest('.tab') : null; return t ? t.getAttribute('data-t') : null; }
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest ? ev.target.closest('button[data-t]') : null;
    if (b) { apri(b.getAttribute('data-t'), true); return; }
    var a = ev.target.closest ? ev.target.closest('a[href^="#p"]') : null;
    if (a) {
      var el = document.getElementById(a.getAttribute('href').slice(1)), id = dellaScheda(el);
      if (id) { ev.preventDefault(); apri(id, false); el.scrollIntoView({ block: 'start' }); }
    }
  });
  /* scheda iniziale: da #pN, altrimenti la scheda del passo ADESSO, altrimenti l'ultima aperta, altrimenti A */
  var h = (location.hash || '').slice(1), el = h ? document.getElementById(h) : null, ini = dellaScheda(el) || (h && document.getElementById('t-' + h) ? h : null);
  if (!ini) ini = dellaScheda(document.querySelector('.passo.ora'));
  if (!ini) { try { ini = sessionStorage.getItem('tab-2inf0911-ora5'); } catch (x) {} }
  apri(ini || (TAB[0] && TAB[0].getAttribute('data-t')), false);
  if (el) el.scrollIntoView({ block: 'start' });
})();
