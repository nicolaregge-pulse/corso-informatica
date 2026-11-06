/* 1INF 06/11/2026: il percorso a passi (R9) comune alle pagine ora4, ora5, ora6 e riserva.
   Hai fatto / Ti manca / Vai qui adesso, lingue (it, ar, zh), mini-giochi, rami (IP), scheda e consegna con UN bottone.
   Le impostazioni stanno nel <body>: data-slug (id della consegna), data-coppia="1" (ore 5-6, lavoro a coppie). */
(function () {
  var B = document.body, SLUG = B.getAttribute('data-slug') || 'pagina', COPPIA = B.getAttribute('data-coppia') === '1';
  var K = 'st-' + SLUG, KS = 'sc-' + SLUG, KN = 'nome-0611', KC = 'compagno-0611', KP = 'pc-0611', KL = 'lingue-0611', CONF = {};
  function $(i) { return document.getElementById(i); }
  function prendi(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (x) { return d; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  function tutti(sel, dove) { return [].slice.call((dove || document).querySelectorAll(sel)); }
  var S = prendi(K, {}), SC = prendi(KS, {}), P = tutti('.passo[data-p]');
  var NOME = prendi(KN, ''), COMP = prendi(KC, ''), PC = prendi(KP, '');

  /* ---- lingue ---- */
  function lingua(l) {
    B.classList.toggle('no-ar', l === 'zh'); B.classList.toggle('no-zh', l === 'ar');
    tutti('#lingue button').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-l') === l); }); metti(KL, l);
  }
  tutti('#lingue button').forEach(function (b) { b.onclick = function () { lingua(b.getAttribute('data-l')); }; });
  lingua(prendi(KL, 'tutte'));

  /* ---- chi sei / chi siete ---- */
  var inp = $('nome');
  if (inp) {
    inp.value = NOME;
    inp.addEventListener('change', function () {
      var v = inp.value.trim().replace(/\s+/g, ' ');
      if (v.split(' ').length < 2) { $('nomeok').textContent = 'Scrivi nome e cognome.'; return; }
      NOME = v; metti(KN, v); $('nomeok').textContent = 'Ciao ' + v + '!'; ping(true); disegna();
    });
  }
  if ($('compagno')) { $('compagno').value = COMP; $('compagno').addEventListener('change', function () { COMP = $('compagno').value.trim().replace(/\s+/g, ' '); metti(KC, COMP); }); }
  if ($('pc')) {
    var sel = $('pc'), h = '<option value="">—</option>';
    for (var i = 1; i <= 20; i++) { var n = (i < 10 ? '0' : '') + i; h += '<option value="' + n + '">PC ' + n + '</option>'; }
    sel.innerHTML = h; sel.value = PC;
    sel.onchange = function () { PC = sel.value; metti(KP, PC); ip(); };
  }

  /* ---- il riquadro dell'IP (ore 5-6): dai valori di config.json, se il docente li ha scritti ---- */
  function ip() {
    var box = $('ipbox'); if (!box) return;
    var r = CONF.rete || {}, n = +PC || 0, righe = [];
    if (r.prefisso && n) righe.push('Indirizzo IP del vostro PC: <b>' + r.prefisso + (+(r.primo || 0) + n) + '</b>');
    else righe.push('Indirizzo IP: lo prendete dalla <b>tabella alla lavagna</b>, alla riga del vostro PC.');
    righe.push('Subnet mask: <b>' + (r.maschera || 'uguale al PC originale') + '</b>');
    righe.push('Gateway predefinito: <b>' + (r.gateway || 'uguale al PC originale') + '</b>');
    righe.push('Server DNS preferito: <b>' + (r.dns || 'uguale al PC originale') + '</b>');
    box.innerHTML = righe.map(function (x) { return '<div>' + x + '</div>'; }).join('');
  }

  /* ---- passi: Ho fatto, Hai fatto / Ti manca / Vai qui adesso ---- */
  function corto(p) { return p.querySelector('h2').textContent.replace(/^\d+/, '').trim().slice(0, 60); }
  function disegna() {
    var prossimo = null;
    P.forEach(function (p) {
      var k = p.getAttribute('data-p'), f = !!S[k], salt = S[k] === 'salta';
      p.classList.toggle('fatto', f); p.classList.remove('ora');
      p.querySelector('.bollo').textContent = salt ? 'NON SERVE' : (f ? 'FATTO' : 'da fare');
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

  /* ---- rami: «il mio IP comincia con 169.254» / «è un altro numero» ---- */
  tutti('.ramo button').forEach(function (b) {
    b.onclick = function () {
      var salta = (b.getAttribute('data-salta') || '').split(',').filter(Boolean), fai = (b.getAttribute('data-fai') || '').split(',').filter(Boolean);
      salta.forEach(function (k) { S[k] = 'salta'; }); fai.forEach(function (k) { if (S[k] === 'salta') delete S[k]; });
      var pa = b.closest('.passo'); if (pa) S[pa.getAttribute('data-p')] = true;
      SC['ramo_' + (pa ? pa.getAttribute('data-p') : '')] = b.getAttribute('data-v') || b.textContent; metti(KS, SC);
      tutti('button', b.parentNode).forEach(function (x) { x.classList.toggle('giusta', x === b); });
      var m = b.parentNode.parentNode.querySelector('.ramo-msg'); if (m) m.innerHTML = b.getAttribute('data-msg') || '';
      metti(K, S); disegna(); ping(false);
    };
  });

  /* ---- mini-giochi (.mq): ogni domanda ha UNA scelta giusta (data-ok); tutte giuste = passo fatto ---- */
  tutti('.mq').forEach(function (mq) {
    var dom = tutti('.mq-d', mq);
    dom.forEach(function (d) {
      tutti('button', d).forEach(function (b) {
        b.onclick = function () {
          var ok = b.hasAttribute('data-ok'), es = d.querySelector('.esito');
          b.classList.add(ok ? 'giusta' : 'sbagliata');
          es.className = 'esito ' + (ok ? 'ok' : 'ko');
          es.innerHTML = ok ? (d.getAttribute('data-p') || '✔') : '✘ Non ancora: riprova. · <span lang="ar">ليس بعد: حاول مرة أخرى</span> · <span lang="zh">还不对：再试一次</span>';
          if (ok) { d.setAttribute('data-fatto', '1'); tutti('button', d).forEach(function (x) { x.disabled = true; }); }
          if (dom.every(function (x) { return x.getAttribute('data-fatto'); })) {
            var pa = mq.closest('.passo'); if (pa) { S[pa.getAttribute('data-p')] = true; metti(K, S); disegna(); ping(false); }
          }
        };
      });
    });
  });

  /* ---- aiuti a livelli: si aprono uno alla volta ---- */
  tutti('.aiuti').forEach(function (a) {
    var det = tutti('details', a);
    det.forEach(function (d, i) { if (i > 0) d.classList.add('chiuso'); d.addEventListener('toggle', function () { if (d.open && det[i + 1]) det[i + 1].classList.remove('chiuso'); }); });
  });

  /* ---- scheda (campi data-k) ---- */
  tutti('#scheda [data-k]').forEach(function (c) {
    var k = c.getAttribute('data-k');
    if (c.type === 'checkbox') { c.checked = !!SC[k]; c.onchange = function () { SC[k] = c.checked; metti(KS, SC); }; }
    else { c.value = SC[k] || ''; c.addEventListener('input', function () { SC[k] = c.value; metti(KS, SC); }); }
  });

  /* ---- bottoni con l'indirizzo in config.json (quiz, recuperi) ---- */
  function link() {
    tutti('a[data-conf]').forEach(function (a) {
      var u = String(CONF[a.getAttribute('data-conf')] || '').trim(), m = document.querySelector('[data-confmsg="' + a.getAttribute('data-conf') + '"]');
      if (u) { a.href = u; a.target = '_blank'; a.rel = 'noopener'; a.classList.remove('spento'); if (m) m.textContent = 'Si apre in una finestra nuova: poi torna qui.'; }
      else { a.href = '#'; a.classList.add('spento'); if (m) m.textContent = 'Il bottone si accende quando il quiz è pronto: premi F5 tra qualche minuto.'; }
    });
    tutti('a[data-apri]').forEach(function (a) {   // pagine che si aprono con una chiave di config.json (es. riserva_aperta)
      if (CONF[a.getAttribute('data-apri')]) { a.href = a.getAttribute('data-href'); a.classList.remove('spento'); }
      else { a.href = '#'; a.classList.add('spento'); }
    });
  }

  /* ---- consegna di Lazarus fatta nella pagina consegna.html ---- */
  function consegne() {
    P.forEach(function (p) {
      var c = p.getAttribute('data-cons');
      if (c && prendi('consegnato-' + c, '') && !S[p.getAttribute('data-p')]) { S[p.getAttribute('data-p')] = true; metti(K, S); }
    });
    disegna();
  }
  window.addEventListener('focus', consegne); document.addEventListener('visibilitychange', consegne);

  /* ---- avanzamento al cruscotto (dato vero, ogni volta che cambia) ---- */
  var ultimo = -1;
  function ping(forza) {
    if (!CONF.attivo || !CONF.invio || !NOME) return;
    var fatti = P.filter(function (p) { return S[p.getAttribute('data-p')]; }).length;
    if (fatti === ultimo && !forza) return; ultimo = fatti;
    var max = 0; P.forEach(function (p) { if (S[p.getAttribute('data-p')]) max = Math.max(max, +p.getAttribute('data-p')); });
    var d = { id: 'avz-' + SLUG, modo: 'avanzamento', classe: '1INF', nome: NOME, compagno: COMP || '', pc: PC || '', scheda: max, totale: P.length, risposte: fatti,
      titolo: max ? corto(P.filter(function (p) { return +p.getAttribute('data-p') === max; })[0]) : '', quando: new Date().toISOString() };
    try { fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) }).catch(function () {}); } catch (x) {}
  }

  /* ---- Manda al prof: UN bottone (canale del ponte, come le altre pagine) ---- */
  window.costruisciConsegna = function (nome) {
    return { id: SLUG, modo: 'verifica', classe: '1INF', nome: nome, compagno: COMP || '', pc: PC || '', cosa: 'scheda', chiave: Date.now().toString(36),
      scheda: SC, passi_fatti: P.filter(function (p) { return S[p.getAttribute('data-p')]; }).map(function (p) { return +p.getAttribute('data-p'); }),
      quando: new Date().toISOString() };
  };
  function postaForm(d) {
    var f = document.createElement('form'); f.method = 'POST'; f.action = CONF.invio; f.target = '_blank'; f.acceptCharset = 'UTF-8';
    var i = document.createElement('input'); i.type = 'hidden'; i.name = 'd'; i.value = JSON.stringify(d); f.appendChild(i);
    document.body.appendChild(f); f.submit(); f.remove();
  }
  if ($('manda')) $('manda').onclick = function () {
    var v = (inp.value || '').trim().replace(/\s+/g, ' '), msg = $('msg');
    if (v.split(' ').length < 2) { msg.className = 'msg ko'; msg.textContent = 'Scrivi nome e cognome in alto (Chi sei?), poi premi di nuovo.'; inp.focus(); return; }
    if (COPPIA && !PC) { msg.className = 'msg ko'; msg.textContent = 'Scegli il numero del PC in alto, poi premi di nuovo.'; $('pc').focus(); return; }
    NOME = v; metti(KN, v); var d = window.costruisciConsegna(NOME);
    if (!CONF.attivo || !CONF.invio) { msg.className = 'msg ko'; msg.textContent = 'ANTEPRIMA: invio spento.'; return; }
    try {
      postaForm(d); var pm = $('manda').closest('.passo'); if (pm) S[pm.getAttribute('data-p')] = true;
      metti(K, S); metti('consegnato-' + SLUG, d.quando); disegna(); ping(true);
      msg.className = 'msg ok'; msg.textContent = 'Mandato! Si è aperta una scheda con «Consegna arrivata al prof». ' + (COPPIA ? 'Adesso il compagno scrive il SUO nome in alto e preme di nuovo.' : 'Puoi mandare di nuovo: vale l\'ultima.');
    } catch (x) { msg.className = 'msg ko'; msg.textContent = 'Non è partito. Premi di nuovo «Manda al prof».'; }
  };

  /* ---- config.json: indirizzi e rete ---- */
  function giro() {
    fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); })
      .then(function (c) { CONF = c || {}; link(); ip(); ping(false); }).catch(function () { link(); ip(); });
  }
  giro(); setInterval(giro, 120000);
  consegne();
})();
