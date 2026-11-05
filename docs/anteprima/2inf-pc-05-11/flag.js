/* Porta a bandierina (genera_lezione_pc.py). La pagina si vede solo se config.json ha la chiave data-chiave = true.
   Uso: <script src="flag.js" data-chiave="guasti_aperta"></script> nel <head>.
   Il docente apre: python3 strumenti/sblocca_ora.py 2inf-pc-05-11 guasti  (chiude: ... guasti-chiudi). */
(function () {
  var sc = document.currentScript, base = sc.src.replace(/[^\/]*$/, ''), k = sc.getAttribute('data-chiave') || 'aperta';
  var stile = document.createElement('style'); stile.textContent = 'main{display:none!important}'; document.head.appendChild(stile);
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function avviso(t) {
    pronto(function () {
      var d = document.getElementById('flag-chiuso');
      if (!d) { d = document.createElement('div'); d.id = 'flag-chiuso'; document.body.appendChild(d);
        d.style.cssText = 'max-width:640px;margin:40px auto;padding:20px 18px;border:3px solid #1f6feb;border-radius:14px;font:20px/1.5 system-ui,Arial,sans-serif;background:#fff;color:#111'; }
      d.innerHTML = '<h1 style="font-size:1.3em;margin:0 0 8px">Questa scheda non è ancora aperta</h1><p>' + t + '</p>';
    });
  }
  function controlla() {
    fetch(base + 'config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) {
      if (c && c[k] === true) { stile.remove(); var d = document.getElementById('flag-chiuso'); if (d) d.remove(); clearInterval(giro); }
      else avviso('Si apre quando il Professore la sblocca. Intanto continua l\'ora che hai davanti: questa pagina si apre da sola.');
    }).catch(function () { avviso('Non riesco a controllare se è aperta. Premi F5 fra un minuto.'); });
  }
  controlla(); var giro = setInterval(controlla, 30000);
})();
