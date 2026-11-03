/* Un'ora per volta. Legge config.json -> "ore_sbloccate" (1, 2 o 3). Il docente cambia SOLO quel numero.
   Uso nelle pagine: <script src="ore.js" data-ora="2"></script> (o data-ora="query" per consegna.html?ora=N) nel <head>;
   nell'hub: <script src="ore.js" data-hub></script> (mostra/nasconde i blocchi data-ora-chiuso / data-ora-aperto). */
(function () {
  var sc = document.currentScript, base = sc.src.replace(/[^\/]*$/, ''), hub = sc.hasAttribute('data-hub');
  var ora = sc.getAttribute('data-ora') === 'query' ? Math.min(9, Math.max(1, +new URLSearchParams(location.search).get('ora') || 1)) : +(sc.getAttribute('data-ora') || 0);
  var stile = null;
  function leggi(cb) {
    fetch(base + 'config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); })
      .then(function (c) { cb(Math.max(1, +(c && c.ore_sbloccate) || 1)); }).catch(function () { cb(null); });
  }
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  if (hub) {
    var applica = function (n) {
      if (n === null) n = 1;
      var tutti = document.querySelectorAll('[data-ora-chiuso],[data-ora-aperto]');
      for (var i = 0; i < tutti.length; i++) {
        var el = tutti[i], k = +(el.getAttribute('data-ora-chiuso') || el.getAttribute('data-ora-aperto')), apri = k <= n;
        el.hidden = el.hasAttribute('data-ora-chiuso') ? apri : !apri;
      }
    };
    var giro = function () { leggi(applica); };
    pronto(function () { giro(); setInterval(giro, 45000); });
    return;
  }
  if (ora <= 1) return;
  stile = document.createElement('style'); stile.textContent = 'main{display:none!important}';
  document.head.appendChild(stile);
  function chiudi(motivo) {
    pronto(function () {
      if (document.getElementById('ore-chiuso')) return;
      var d = document.createElement('div'); d.id = 'ore-chiuso';
      d.style.cssText = 'max-width:640px;margin:40px auto;padding:20px 18px;border:3px solid #1f6feb;border-radius:14px;font:20px/1.5 system-ui,Arial,sans-serif;background:#fff;color:#111';
      d.innerHTML = '<h1 style="font-size:1.3em;margin:0 0 8px">Questa ora non è ancora aperta</h1>' +
        '<p>' + (motivo === 'errore' ? 'Non riesco a controllare se è aperta. Premi F5 tra poco.' : 'Il Professore la apre tra poco. Per ora fai l\'ora che hai davanti: quando sarà il momento, questa pagina si apre da sola.') + '</p>' +
        '<p><a href="./" style="font-weight:700">Torna alla pagina di oggi</a></p>';
      document.body.appendChild(d);
    });
  }
  function controlla(primo) {
    leggi(function (n) {
      if (n !== null && n >= ora) { stile.remove(); var d = document.getElementById('ore-chiuso'); if (d) d.remove(); if (!primo) clearInterval(giro); return; }
      if (primo) chiudi(n === null ? 'errore' : 'chiuso');
    });
  }
  controlla(true);
  var giro = setInterval(function () { controlla(false); }, 30000);
})();
