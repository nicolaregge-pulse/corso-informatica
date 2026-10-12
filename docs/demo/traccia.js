/* Demo: accesso e tracciamento. Ogni pagina della demo manda allo script dell'accesso (account PERSONALE)
   l'apertura e i clic; senza un accesso valido la pagina resta coperta. */
(function () {
  var WEBAPP = 'https://script.google.com/macros/s/AKfycbyhkWr44IWarPFRvcyP0Ku1pI-XbFaeBVJA4I0iEITq_4U4XvD5rqiPci77-p2FLory/exec';
  var T = new URLSearchParams(location.search).get('t') || '';
  try { if (T) localStorage.setItem('demo_t', T); else T = localStorage.getItem('demo_t') || ''; } catch (e) {}
  var velo = document.createElement('div');
  velo.style.cssText = 'position:fixed;inset:0;z-index:99999;background:#fbfaf7;color:#111;display:flex;align-items:center;justify-content:center;font:17px/1.5 system-ui,Segoe UI,Arial,sans-serif;padding:16px;text-align:center';
  velo.innerHTML = '<div>Controllo dell\'accesso in corso…</div>';
  document.documentElement.appendChild(velo);
  function chiusa() { velo.innerHTML = '<div style="max-width:480px;background:#fff;border:2px solid #c0392b;border-radius:12px;padding:18px">Per vedere la demo serve un accesso valido.<br><a href="' + WEBAPP + '" target="_top">Chiedi il codice dalla pagina di accesso</a></div>'; }
  function traccia(evento, dettaglio, cb) {
    if (!T) { if (cb) cb({ ok: false }); return; }
    var n = 'cb' + Date.now() + Math.floor(Math.random() * 1000), s = document.createElement('script');
    window[n] = function (r) { if (cb) cb(r); delete window[n]; s.remove(); };
    s.onerror = function () { if (cb) cb({ ok: false }); };
    s.src = WEBAPP + '?azione=traccia&t=' + encodeURIComponent(T) + '&evento=' + evento + '&pagina=' + encodeURIComponent(location.pathname.replace(/^.*\/demo\//, 'demo/')) +
      '&dettaglio=' + encodeURIComponent(dettaglio || '') + '&callback=' + n;
    document.head.appendChild(s);
  }
  traccia('apertura', document.title, function (r) { if (r && r.ok) velo.remove(); else chiusa(); });
  document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('a,button'); if (a) traccia('clic', (a.textContent || '').trim().slice(0, 60)); }, true);
})();
