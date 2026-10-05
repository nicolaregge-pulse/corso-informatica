/* Controllo "sito online" SENZA l'API di GitHub (che dalla rete della scuola si blocca dopo ~60 controlli all'ora).
   Si chiede direttamente la pagina del sito: se risponde, e' online. */
function urlSito(u, repo) { return 'https://' + String(u).toLowerCase() + '.github.io/' + (repo || 'mio-sito') + '/'; }
function sitoOnline(url, cb) {
  var fatto = false; function fine(v) { if (!fatto) { fatto = true; cb(v); } }
  fetch(url + '?v=' + Date.now(), { cache: 'no-store' }).then(function (r) { fine(r.ok); }).catch(function () {
    var l = document.createElement('link'); l.rel = 'stylesheet'; l.media = '(max-width:1px)'; l.href = url + 'style.css?v=' + Date.now();
    l.onload = function () { fine(true); l.remove(); }; l.onerror = function () { fine(false); l.remove(); };
    document.head.appendChild(l); setTimeout(function () { fine(false); }, 15000);
  });
}
