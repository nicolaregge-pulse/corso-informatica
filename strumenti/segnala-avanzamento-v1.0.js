/* segnala-avanzamento v1.0 (20/11/2026). Passo raggiunto = il suo titolo e salito sopra il 70% dello schermo (anche scorrendo veloce). Nessun cognome lascia il browser: si manda solo «Nome I.».
   USO nella pagina (due righe, in fondo al body):
     <script>var CS_CONF={url:'https://script.google.com/macros/s/.../exec',id:'2inf-negozio-v1',tipo:'teoria',classe:'2INF'};</script>
     <script src="../live/segnala-v1.0.js"></script>
   Passi: ogni elemento [data-passo] (o il selettore CS_CONF.sel, per esempio '.passo' nel negozio; oppure, se non ce ne sono, ogni h2 dentro main). Quiz/compito: CS.apri(link) e CS.fatto().
   Stati mandati: visto (pagina aperta), iniziato (primo gesto), avanzato (passo n di m, e ogni 30 s di tempo attivo), consegnato (CS.fatto()). */
(function (w, d) {
  var C = w.CS_CONF || {}, K = 'cs_nome', nome = '', n = 0, m = 0, sec = 0, ult = 0, ini = 0, fin = 0, sess = Math.random().toString(36).slice(2, 8), els = [];
  function ls(k, v) { try { if (v === undefined) return w.localStorage.getItem(k) || ''; w.localStorage.setItem(k, v); } catch (e) { return ''; } }
  function ridotto(t) { /* «Marco Rossi» -> «Marco R.»: il cognome non esce dal browser */
    var p = String(t || '').trim().replace(/\s+/g, ' ').split(' ');
    if (p.length < 2 || !/^\p{L}/u.test(p[0]) || !/^\p{L}/u.test(p[p.length - 1])) return '';
    var a = p[0].charAt(0).toUpperCase() + p[0].slice(1).toLowerCase();
    return /^\p{L}[\p{L}'’-]{1,24}$/u.test(a) ? a + ' ' + p[p.length - 1].charAt(0).toUpperCase() + '.' : '';
  }
  function manda(stato) {
    if (!C.url || !nome || fin && stato !== 'consegnato') return;
    var e = { v: 1, a: nome, t: C.tipo || 'teoria', id: C.id, s: stato, n: n, m: m, sec: sec, cl: C.classe || '', se: sess, ts: new Date().toISOString() };
    try { w.fetch(C.url, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(e)) }); } catch (x) { }
  }
  function gesto() { ult = Date.now(); if (!ini) { ini = 1; manda('iniziato'); } }
  function parti() {
    els = [].slice.call(d.querySelectorAll(C.sel || '[data-passo]')); if (!els.length) els = [].slice.call(d.querySelectorAll('main h2'));
    m = els.length || m; manda('visto');
    var tt = 0;
    function guarda() { tt = 0; for (var i = els.length; i > n; i--) if (els[i - 1].getBoundingClientRect().top < w.innerHeight * 0.7) { n = i; gesto(); manda('avanzato'); break; } }
    function scorri() { if (!tt) tt = w.setTimeout(guarda, 250); }
    w.addEventListener('scroll', scorri, { passive: true }); w.addEventListener('resize', scorri); guarda();
    ['scroll', 'click', 'keydown', 'touchstart'].forEach(function (t) { d.addEventListener(t, gesto, { passive: true }); });
    w.setInterval(function () { if (d.visibilityState === 'visible' && Date.now() - ult < 60000) { sec += (C.hb || 30000) / 1000; manda('avanzato'); } }, C.hb || 30000);
  }
  function chiedi() {
    var b = d.createElement('div'); b.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;z-index:99999;font:18px system-ui';
    b.innerHTML = '<form style="background:#fff;color:#111;padding:20px;border-radius:12px;max-width:340px"><p><b>Come ti chiami?</b><br>Scrivi nome e cognome. Il sito salva solo il nome e la lettera del cognome (per esempio Marco R.).</p><input id="cs_in" style="width:100%;font:inherit;padding:8px" autocomplete="off"><p id="cs_er" style="color:#b42318"></p><button style="font:inherit;padding:8px 16px">Vai</button></form>';
    d.body.appendChild(b);
    b.querySelector('form').onsubmit = function (ev) {
      ev.preventDefault(); var r = ridotto(b.querySelector('#cs_in').value);
      if (!r) { b.querySelector('#cs_er').textContent = 'Scrivi nome e cognome, per esempio Marco Rossi.'; return; }
      nome = r; ls(K, r); b.remove(); parti();
    };
  }
  w.CS = {
    fatto: function () { gesto(); if (n < m) n = m; manda('consegnato'); fin = 1; },
    apri: function (url) { gesto(); manda('avanzato'); if (url) w.open(url, '_blank'); },
    nome: function () { return nome; }, cambiaNome: function () { ls(K, ''); w.location.reload(); }
  };
  function via() { nome = ls(K); if (nome) parti(); else chiedi(); }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', via); else via();
})(window, document);
