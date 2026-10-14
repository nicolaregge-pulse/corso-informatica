/* Changelog del gioco della talpa (1INF): legge versioni.json e scrive, per ogni versione, tutto quello che è cambiato.
   Uso: <div id="changelog" data-base="(percorso della cartella talpa-1inf)/"></div><script src=".../changelog.js"></script> */
(function () {
  var box = document.getElementById('changelog'), base = box.getAttribute('data-base') || '../';
  function e(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function img(f, alt) { return f ? '<img src="' + base + e(f) + '" alt="' + e(alt) + '" loading="lazy">' : '<img src="' + base + '../../compito/1inf-20261014-talpa/talpa.png" alt="La talpa originale">'; }
  function carica() {
    fetch(base + 'versioni/versioni.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (V) {
      var h = '<p class="mu">Versioni: ' + V.length + ' · ultima: <b>' + e(V[V.length - 1].versione) + '</b> · personaggi nel gioco adesso: <b>' + V[V.length - 1].presenti.length + '</b></p>';
      V.slice().reverse().forEach(function (v, k) {
        h += '<section class="ver"><div class="testa"><span class="num">' + e(v.versione) + '</span> <b>' + e(v.nome) + '</b></div>' +
          '<div class="mu">' + e(v.data) + ' alle ' + e(v.ora) + (v.pr ? ' · ' + e(v.pr) : '') + ' · ramo: <code>' + e(v.ramo) + '</code> · di: ' + e(v.autore) + '</div>' +
          '<p class="it">' + e(v.riassunto.it) + '</p><p class="ar">' + e(v.riassunto.ar) + '</p><p class="zh">' + e(v.riassunto.zh) + '</p>';
        if (v.entrati.length) h += '<h4>Chi è entrato in questa versione · من دخل · 谁加入了</h4><div class="g">' + v.entrati.map(function (p) { return '<figure class="nuovo">' + img(p.file, p.chi) + '<figcaption><b>' + e(p.chi) + '</b><br>«' + e(p.descrizione) + '»</figcaption></figure>'; }).join('') + '</div>';
        h += '<h4>Che cosa è cambiato, tutto · ما الذي تغيّر · 改变了什么</h4><ol>' + v.cambi.map(function (c) { return '<li>' + e(c) + '</li>'; }).join('') + '</ol>';
        h += '<h4>Tutti i personaggi presenti in ' + e(v.versione) + ' (' + v.presenti.length + ') · كل الشخصيات · 所有角色</h4><div class="g">' + v.presenti.map(function (p) { return '<figure>' + img(p.file, p.chi) + '<figcaption>' + e(p.chi) + '<br><span class="mu">dalla ' + e(p.dal) + '</span></figcaption></figure>'; }).join('') + '</div>';
        h += '<h4>File cambiati · الملفات · 文件</h4><ol>' + v.file.map(function (c) { return '<li><code>' + e(c) + '</code></li>'; }).join('') + '</ol>';
        h += '<p><b>Che cosa NON è cambiato:</b> ' + e(v.invariato) + '</p><p><b>Che tipo di versione è:</b> ' + e(v.tipo) + '</p>' +
          '<a class="gioca" href="' + base + '?v=' + e(v.versione) + '" target="_blank" rel="noopener">Gioca la ' + e(v.versione) + ' · العب · 玩</a></section>';
      });
      box.innerHTML = h;
    }).catch(function () { box.textContent = 'Non riesco a leggere le versioni: ricarica la pagina.'; });
  }
  carica(); setInterval(carica, 60000);
})();
