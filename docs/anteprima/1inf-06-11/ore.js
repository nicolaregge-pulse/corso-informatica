/* Porta dell'ora (1INF 06/11/2026; ora 5 = Lo scontrino che parla). Legge config.json -> "ore_sbloccate": 0 = tutto chiuso; 4, 5 o 6 = aperte le ore fino a quella.
   data-ora = l'ora della giornata della pagina (4 = 11-12, 5 = 12-13, 6 = 13-14).
   data-flag (facoltativo) = chiave di config.json che deve essere true (es. riserva_aperta per «Se avanza tempo»).
   Si cambia SOLO con: bash /home/user/corso-informatica-riservato/lezioni-pronte/1inf-06-11/pubblica.sh N (al PUBB N). */
(function () {
  var sc = document.currentScript, base = sc.src.replace(/[^\/]*$/, ''), ora = +(sc.getAttribute('data-ora') || 1), flag = sc.getAttribute('data-flag');
  var stile = document.createElement('style'); stile.textContent = 'main{display:none!important}'; document.head.appendChild(stile);
  function leggi(cb) {
    fetch(base + 'config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); })
      .then(function (c) { var n = Math.max(0, +(c && c.ore_sbloccate) || 0); cb(flag && !(c && c[flag]) ? 0 : n); }).catch(function () { cb(null); });
  }
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function chiudi(motivo) {
    pronto(function () {
      if (document.getElementById('ore-chiuso')) return;
      var d = document.createElement('div'); d.id = 'ore-chiuso';
      d.style.cssText = 'max-width:640px;margin:40px auto;padding:20px 18px;border:3px solid #1f6feb;border-radius:14px;font:20px/1.5 system-ui,Arial,sans-serif;background:#fff;color:#111';
      d.innerHTML = '<h1 style="font-size:1.3em;margin:0 0 8px">Questa ora non è ancora aperta</h1>' +
        '<p>' + (motivo === 'errore' ? 'Non riesco a controllare se è aperta. Premi F5 tra poco.' : 'Il Professore la apre al momento giusto. Per ora fai l\'ora che hai davanti: quando sarà il momento, questa pagina si apre da sola.') + '</p>' +
        '<p dir="rtl" lang="ar" style="color:#444">هذه الساعة لم تُفتح بعد. ستُفتح الصفحة وحدها في الوقت المناسب.</p><p lang="zh" style="color:#444">这节课还没有开放。到时候页面会自己打开。</p>';
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
