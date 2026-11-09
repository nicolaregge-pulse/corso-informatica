/* 2INF 09/11/2026: il percorso a passi (R9): Hai fatto / Ti manca / Vai qui adesso, mini-ripasso, scheda e consegna con UN bottone.
   Lingua (R6): solo italiano. */
(function () {
  var B = document.body, SLUG = B.getAttribute('data-slug') || 'pagina';
  var K = 'st-' + SLUG, KS = 'sc-' + SLUG, KN = 'nome-2inf0911', KP = 'pc-2inf0911', CONF = {};
  function $(i) { return document.getElementById(i); }
  function prendi(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (x) { return d; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  function tutti(sel, dove) { return [].slice.call((dove || document).querySelectorAll(sel)); }
  var S = prendi(K, {}), SC = prendi(KS, {}), P = tutti('.passo[data-p]');
  var NOME = prendi(KN, ''), PC = prendi(KP, '');

  var inp = $('nome');
  if (inp) {
    inp.value = NOME;
    inp.addEventListener('change', function () {
      var v = inp.value.trim().replace(/\s+/g, ' ');
      if (v.split(' ').length < 2) { $('nomeok').textContent = 'Scrivi nome e cognome.'; return; }
      NOME = v; metti(KN, v); $('nomeok').textContent = 'Ciao ' + v + '!'; ping(true); disegna();
    });
  }
  if ($('pc')) {
    var sel = $('pc'), h = '<option value="">—</option>';
    for (var i = 1; i <= 24; i++) { var n = (i < 10 ? '0' : '') + i; h += '<option value="' + (i < 10 ? '0' + i : '' + i) + '">PC ' + n + '</option>'; }
    sel.innerHTML = h; sel.value = PC;
    sel.onchange = function () { PC = sel.value; metti(KP, PC); ping(true); };
  }

  function corto(p) { return p.querySelector('h2').textContent.replace(/^\d+/, '').trim().slice(0, 60); }
  function disegna() {
    var prossimo = null;
    P.forEach(function (p) {
      var k = p.getAttribute('data-p'), f = !!S[k];
      p.classList.toggle('fatto', f); p.classList.remove('ora');
      p.querySelector('.bollo').textContent = f ? 'FATTO' : 'da fare';
      var b = p.querySelector('button.fb');
      if (b) b.textContent = f ? 'Fatto ✓ (clic per togliere)' : 'Ho fatto!';
      if (!f && !prossimo && !p.hasAttribute('data-bonus')) prossimo = p;
    });
    if (prossimo) { prossimo.classList.add('ora'); prossimo.querySelector('.bollo').textContent = 'ADESSO'; }
    var PO = P.filter(function (p) { return !p.hasAttribute('data-bonus'); });
    var n = PO.filter(function (p) { return S[p.getAttribute('data-p')]; }).length;
    if ($('barra')) $('barra').style.width = Math.round(100 * n / Math.max(1, PO.length)) + '%';
    if ($('conta')) $('conta').textContent = 'Passi fatti: ' + n + ' su ' + PO.length + (n === PO.length ? ' — BRAVO, hai finito!' : '');
    var fa = P.filter(function (p) { return S[p.getAttribute('data-p')]; }).map(function (p) { return p.getAttribute('data-p'); });
    var ma = PO.filter(function (p) { return !S[p.getAttribute('data-p')]; }).map(function (p) { return p.getAttribute('data-p'); });
    if ($('d-fatto')) $('d-fatto').textContent = fa.length ? 'passi ' + fa.join(', ') : 'niente, per ora';
    if ($('d-manca')) $('d-manca').textContent = ma.length ? 'passi ' + ma.join(', ') : 'niente: hai finito!';
    var vai = $('vai');
    if (vai) {
      if (prossimo) { vai.style.display = ''; vai.textContent = 'Passo ' + prossimo.getAttribute('data-p') + ' · ' + corto(prossimo) + ' →'; vai.href = '#p' + prossimo.getAttribute('data-p'); }
      else vai.style.display = 'none';
    }
  }
  P.forEach(function (p) {
    var b = p.querySelector('button.fb');
    if (b) b.onclick = function () { var k = p.getAttribute('data-p'); S[k] = !S[k]; metti(K, S); disegna(); ping(false); };
  });

  /* mini-ripasso (.mq): ogni domanda ha UNA scelta giusta (data-ok); tutte giuste = passo fatto */
  tutti('.mq').forEach(function (mq) {
    var dom = tutti('.mq-d', mq);
    dom.forEach(function (d) {
      tutti('button', d).forEach(function (b) {
        b.onclick = function () {
          var ok = b.hasAttribute('data-ok'), es = d.querySelector('.esito');
          b.classList.add(ok ? 'giusta' : 'sbagliata');
          es.className = 'esito ' + (ok ? 'ok' : 'ko');
          es.innerHTML = ok ? (d.getAttribute('data-p') || '✔') : '✘ Non ancora: riprova.';
          if (ok) { d.setAttribute('data-fatto', '1'); tutti('button', d).forEach(function (x) { x.disabled = true; }); }
          if (dom.every(function (x) { return x.getAttribute('data-fatto'); })) {
            var pa = mq.closest('.passo'); if (pa) { S[pa.getAttribute('data-p')] = true; metti(K, S); disegna(); ping(false); }
          }
        };
      });
    });
  });

  tutti('#scheda [data-k]').forEach(function (c) {
    var k = c.getAttribute('data-k');
    if (c.type === 'checkbox') { c.checked = !!SC[k]; c.onchange = function () { SC[k] = c.checked; metti(KS, SC); }; }
    else { c.value = SC[k] || ''; c.addEventListener('input', function () { SC[k] = c.value; metti(KS, SC); }); }
  });

  /* bottoni con l'indirizzo in config.json (quiz) */
  function link() {
    tutti('a[data-conf]').forEach(function (a) {
      var u = String(CONF[a.getAttribute('data-conf')] || '').trim(), m = document.querySelector('[data-confmsg="' + a.getAttribute('data-conf') + '"]');
      if (u) { a.href = u; a.target = '_blank'; a.rel = 'noopener'; a.classList.remove('spento'); if (m) m.textContent = 'Si apre in una finestra nuova: poi torna qui.'; }
      else { a.href = '#'; a.classList.add('spento'); if (m) m.textContent = 'Il bottone si accende quando il quiz è pronto: premi F5 tra qualche minuto.'; }
    });
  }

  /* avanzamento al cruscotto (dato vero, ogni volta che cambia) */
  var ultimo = -1;
  function ping(forza) {
    if (!CONF.attivo || !CONF.invio || !NOME) return;
    var fatti = P.filter(function (p) { return S[p.getAttribute('data-p')]; }).length;
    if (fatti === ultimo && !forza) return; ultimo = fatti;
    var max = 0; P.forEach(function (p) { if (S[p.getAttribute('data-p')]) max = Math.max(max, +p.getAttribute('data-p')); });
    var d = { id: 'avz-' + SLUG, modo: 'avanzamento', classe: '2INF', nome: NOME, compagno: '', pc: PC || '', scheda: max, totale: P.length, risposte: fatti,
      titolo: max ? corto(P.filter(function (p) { return +p.getAttribute('data-p') === max; })[0]) : '', quando: new Date().toISOString() };
    try { fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) }).catch(function () {}); } catch (x) {}
  }

  /* Manda al prof: UN bottone (stesso canale delle altre pagine) */
  function postaForm(d) {
    var f = document.createElement('form'); f.method = 'POST'; f.action = CONF.invio; f.target = '_blank'; f.acceptCharset = 'UTF-8';
    var i = document.createElement('input'); i.type = 'hidden'; i.name = 'd'; i.value = JSON.stringify(d); f.appendChild(i);
    document.body.appendChild(f); f.submit(); f.remove();
  }
  if ($('manda')) $('manda').onclick = function () {
    var v = (inp.value || '').trim().replace(/\s+/g, ' '), msg = $('msg');
    if (v.split(' ').length < 2) { msg.className = 'msg ko'; msg.textContent = 'Scrivi nome e cognome in alto (Chi sei?), poi premi di nuovo.'; inp.focus(); return; }
    NOME = v; metti(KN, v);
    var d = { id: SLUG, modo: 'verifica', classe: '2INF', nome: NOME, compagno: '', pc: PC || '', cosa: 'scheda', chiave: Date.now().toString(36), scheda: SC,
      passi_fatti: P.filter(function (p) { return S[p.getAttribute('data-p')]; }).map(function (p) { return +p.getAttribute('data-p'); }), quando: new Date().toISOString() };
    if (!CONF.attivo || !CONF.invio) { msg.className = 'msg ko'; msg.textContent = 'ANTEPRIMA: invio spento.'; return; }
    try {
      postaForm(d); var pm = $('manda').closest('.passo'); if (pm) S[pm.getAttribute('data-p')] = true;
      metti(K, S); metti('consegnato-' + SLUG, d.quando); disegna(); ping(true);
      msg.className = 'msg ok'; msg.textContent = 'Mandato! Si è aperta una scheda con «Consegna arrivata al prof». Puoi mandare di nuovo: vale l\'ultima.';
    } catch (x) { msg.className = 'msg ko'; msg.textContent = 'Non è partito. Premi di nuovo «Manda al prof».'; }
  };

  function giro() {
    fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); })
      .then(function (c) { CONF = c || {}; link(); ping(false); }).catch(function () { link(); });
  }
  giro(); setInterval(giro, 120000);
  disegna();
})();
