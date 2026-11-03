/* Porta dell'ora. Legge config.json -> "ore_sbloccate": 0 = pagine chiuse, 1 o piu = aperte.
   Il docente cambia SOLO quel numero (strumenti/sblocca_ora.py 2inf-sicurezza 1). Uso: <script src="ore.js" data-ora="1"></script> nel <head>. */
(function () {
  var sc = document.currentScript, base = sc.src.replace(/[^\/]*$/, ''), ora = +(sc.getAttribute('data-ora') || 1);
  var stile = document.createElement('style'); stile.textContent = 'main{display:none!important}'; document.head.appendChild(stile);
  function leggi(cb) {
    fetch(base + 'config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); })
      .then(function (c) { cb(Math.max(0, +(c && c.ore_sbloccate) || 0)); }).catch(function () { cb(null); });
  }
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function chiudi(motivo) {
    pronto(function () {
      if (document.getElementById('ore-chiuso')) return;
      var d = document.createElement('div'); d.id = 'ore-chiuso';
      d.style.cssText = 'max-width:640px;margin:40px auto;padding:20px 18px;border:3px solid #1f6feb;border-radius:14px;font:20px/1.5 system-ui,Arial,sans-serif;background:#fff;color:#111';
      d.innerHTML = '<h1 style="font-size:1.3em;margin:0 0 8px">Questa ora non è ancora aperta</h1>' +
        '<p>' + (motivo === 'errore' ? 'Non riesco a controllare se è aperta. Premi F5 tra poco.' : 'Il Professore la apre tra poco. Per ora fai l\'ora che hai davanti: quando sarà il momento, questa pagina si apre da sola.') + '</p>';
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
