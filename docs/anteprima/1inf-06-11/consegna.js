/* 1INF 06/11/2026: consegna di unit1.pas + screenshot con UN bottone (come 1inf-lazarus-04-11/consegna.html).
   ?ora=4 = «Il convertitore che parla»; ?ora=r = «Lo scontrino che parla» (se avanza tempo). */
(function () {
  var qs = new URLSearchParams(location.search), R = qs.get('ora') === 'r';
  var CART = R ? 'scontrino-parla' : 'convertitore-parla', ID = R ? '1inf-scontrino0611' : '1inf-conv0611', QUALE = R ? 'scontrino' : 'conv';
  var IMGN = R ? 'riserva_screenshot' : 'ora4_screenshot', PEZZO = 200000, CONF = {};
  function $(i) { return document.getElementById(i); }
  function prendi(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (x) { return d; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  $('tit').textContent = (R ? 'Lo scontrino che parla' : 'Ora 4 · Il convertitore che parla') + ' · Consegna';
  $('cart').textContent = CART; $('nomeimg').textContent = IMGN + '.png'; $('torna').href = R ? 'riserva.html' : 'ora4.html';
  var PAS = null, CHECK = null, IMG = null, NOME = prendi('nome-0611', '') || '';
  $('nome').value = NOME;
  fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) { CONF = c || {}; }).catch(function () { CONF = {}; });
  function pronto() { NOME = $('nome').value.trim().replace(/\s+/g, ' '); $('manda').disabled = !(NOME.split(' ').length >= 2 && (PAS || IMG)); }
  $('nome').addEventListener('input', function () { pronto(); metti('nome-0611', $('nome').value.trim()); });
  $('pas').onchange = function () {
    var f = $('pas').files[0]; PAS = null; CHECK = null; $('voci').innerHTML = ''; $('esito').textContent = '';
    if (!f) return pronto();
    var r = new FileReader();
    r.onload = function () {
      PAS = { nome: f.name, testo: String(r.result || '').slice(0, 60000) };
      try {   // il controllo è solo un aiuto: se va in errore, si consegna lo stesso
        CHECK = ControllaPas(PAS.testo, QUALE);
        $('voci').innerHTML = CHECK.voci.map(function (v) {
          var c = v.ok ? 'ok' : (v.avviso ? 'av' : 'ko'), s = v.ok ? '✔' : (v.avviso ? '!' : '✘');
          return '<li class="' + c + '"><b>' + s + '</b>' + v.it + '<div class="ar" lang="ar" dir="rtl">' + v.ar + '</div><div class="zh" lang="zh">' + v.zh + '</div></li>';
        }).join('');
        $('esito').innerHTML = CHECK.livello ? '<b style="color:var(--ok)">Livello ' + CHECK.livello + ' fatto: bravo!</b>' + (CHECK.livello < 3 ? ' Le righe gialle sono il livello dopo.' : '')
          : 'Qualcosa manca: guarda le righe rosse e correggi in Lazarus (poi Ctrl + S e scegli di nuovo il file). Puoi anche mandare lo stesso.';
      } catch (x) { CHECK = { ok: null, errore: String(x) }; $('esito').textContent = 'Controllo non riuscito: puoi mandare lo stesso.'; }
      pronto();
    };
    r.onerror = function () { $('esito').textContent = 'Non riesco a leggere il file: scegline un altro o usa Classroom.'; pronto(); };
    r.readAsText(f);
  };
  $('img').onchange = function () {
    var f = $('img').files[0]; IMG = null; $('anteprima').innerHTML = '';
    if (!f) return pronto();
    var r = new FileReader();
    r.onload = function () {
      var url = String(r.result), im = new Image();
      im.onload = function () {
        $('anteprima').innerHTML = '<img alt="il tuo screenshot" src="' + url + '"><span class="mu">' + f.name + '</span>';
        try {   // più leggero: al massimo 1600 punti di larghezza, JPEG
          var w = Math.min(1600, im.naturalWidth), h = Math.round(im.naturalHeight * w / im.naturalWidth), c = document.createElement('canvas');
          c.width = w; c.height = h; c.getContext('2d').drawImage(im, 0, 0, w, h);
          IMG = { nome: IMGN + '.jpg', tipo: 'image/jpeg', b64: c.toDataURL('image/jpeg', 0.85).split(',')[1], originale: f.name };
        } catch (x) { IMG = { nome: f.name, tipo: f.type, b64: url.split(',')[1], originale: f.name }; }
        pronto();
      };
      im.onerror = function () { IMG = { nome: f.name, tipo: f.type, b64: url.split(',')[1], originale: f.name }; pronto(); };
      im.src = url;
    };
    r.readAsDataURL(f);
  };
  function pausa(ms) { return new Promise(function (ok) { setTimeout(ok, ms); }); }
  function posta(d) { return fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) }); }
  function postaForm(d) {   // l'ultimo invio apre la pagina «Consegna arrivata al prof» dello script
    var f = document.createElement('form'); f.method = 'POST'; f.action = CONF.invio; f.target = '_blank'; f.acceptCharset = 'UTF-8';
    var i = document.createElement('input'); i.type = 'hidden'; i.name = 'd'; i.value = JSON.stringify(d); f.appendChild(i);
    document.body.appendChild(f); f.submit(); f.remove();
  }
  window.costruisciInvii = function (nome, pas, check, img, chiave) {   // esposta per la prova automatica
    var out = [], parti = img ? Math.max(1, Math.ceil(img.b64.length / PEZZO)) : 0, base = { id: ID, modo: 'verifica', classe: '1INF', nome: nome, chiave: chiave };
    for (var k = 0; k < parti; k++) out.push(Object.assign({}, base, { cosa: 'screenshot', file: img.nome, tipo: img.tipo, originale: img.originale, parte: k + 1, parti: parti, base64: img.b64.slice(k * PEZZO, (k + 1) * PEZZO), quando: new Date().toISOString() }));
    out.push(Object.assign({}, base, { cosa: 'unit1', file: (R ? 'riserva' : 'ora4') + '_unit1.pas', originale: pas ? pas.nome : '', testo_pas: pas ? pas.testo : '',
      controllo: check ? { ok: check.ok, livello: check.livello, punti: check.punti, mancano: (check.voci || []).filter(function (v) { return !v.ok; }).map(function (v) { return v.it; }) } : null,
      screenshot: img ? { file: img.nome, parti: parti } : null, quando: new Date().toISOString() }));
    return out;
  };
  $('manda').onclick = async function () {
    pronto(); if ($('manda').disabled) return;
    var inv = window.costruisciInvii(NOME, PAS, CHECK, IMG, Date.now().toString(36));
    if (!PAS || !IMG) { if (!confirm('Manca ' + (!PAS ? 'unit1.pas' : 'lo screenshot') + '. Mandi lo stesso? Poi manda anche l\'altro.')) return; }
    if (!CONF.attivo || !CONF.invio) { $('msg').className = 'msg ko'; $('msg').textContent = 'ANTEPRIMA: invio spento. Partirebbero ' + inv.length + ' invii.'; return; }
    $('manda').disabled = true; $('msg').className = 'msg'; $('msg').textContent = 'Sto mandando…';
    try {
      for (var i = 0; i < inv.length - 1; i++) { await posta(inv[i]); $('msg').textContent = 'Sto mandando lo screenshot… ' + Math.round((i + 1) / (inv.length - 1) * 100) + '%'; await pausa(1300); }
      postaForm(inv[inv.length - 1]);
      $('msg').className = 'msg ok'; $('msg').textContent = 'Mandato! Si è aperta una scheda con scritto «Consegna arrivata al prof». Torna alla pagina dei passi: il passo è verde.';
      metti('consegnato-' + ID, new Date().toISOString());
    } catch (x) {
      $('msg').className = 'msg ko'; $('msg').textContent = 'Non è partito. Premi di nuovo «Manda al prof» oppure consegna su Classroom.'; $('manda').disabled = false;
    }
  };
})();
