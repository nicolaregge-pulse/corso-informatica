/* Lezione «smonta, rimonta, installa» (genera_lezione_pc.py). Legge window.LEZ e config.json:
   variante_os (A Windows 10, B Linux Mint), persone_per_pc, pc_da_smontare, rete, quiz_pc, invio, attivo, ore_sbloccate. */
(function () {
  var L = window.LEZ, CONF = L.conf || {}, $ = function (i) { return document.getElementById(i); };
  function prendi(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (x) { return d; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  try { if (/[?&]pc=14\b/.test(location.search)) localStorage.setItem('pc14', '1'); if (localStorage.getItem('pc14') === '1') document.body.classList.add('pc14'); } catch (x) {}
  var KG = 'pc0511-' + L.classe, K = 'st-' + L.slug, KS = 'sch-' + L.slug;
  var G = prendi(KG, { nome: '', comp1: '', comp2: '', banco: '' }), S = prendi(K, {}), R = prendi(KS, {});
  function ipDi(b) { var r = CONF.rete || {}; return b ? (r.prefisso || '') + ((+r.primo || 0) + (+b)) : '?'; }

  /* ---------- indice: ore aperte / in arrivo, «vai qui adesso» ---------- */
  function indice() {
    var n = +CONF.ore_sbloccate || 0, primo = null;
    [].forEach.call(document.querySelectorAll('.ora-card'), function (c) {
      var aperta = n >= +c.dataset.ora, fatta = !!prendi('inviata-' + L.classe + '-' + c.dataset.num, null);
      c.classList.toggle('aperta', aperta && !fatta); c.classList.toggle('fatta', aperta && fatta);
      c.querySelector('.st').textContent = !aperta ? 'in arrivo' : fatta ? 'FATTA' : 'APERTA';
      c.querySelector('a').style.display = aperta ? '' : 'none';
      if (aperta && !fatta && !primo) primo = c;
    });
    $('vai-ind').innerHTML = primo ? 'Vai qui adesso: <a href="' + primo.dataset.file + '">' + esc(primo.querySelector('h2').textContent) + ' &rarr;</a>' : (n ? 'Hai fatto tutte le ore aperte. Bravi!' : 'Le ore non sono ancora aperte.');
    var pp = +CONF.persone_per_pc || 2;
    $('info-gruppi').textContent = 'PC da smontare oggi: ' + (CONF.pc_da_smontare || '?') + ' · persone per PC: ' + pp + ' · sistema: ' + (CONF.variante_os === 'B' ? 'Linux Mint' : 'Windows 10') + '.';
  }

  /* ---------- chi siete (a coppie, niente ruoli: docente 05/11/2026) ---------- */
  function chi() {
    if (!$('nome')) return;
    var pp = +CONF.persone_per_pc || 2, sel = $('banco'), n = +CONF.pc_da_smontare || 10, h = '<option value="">scegli</option>';
    for (var i = 1; i <= n; i++) h += '<option' + (String(i) === String(G.banco) ? ' selected' : '') + '>' + i + '</option>';
    sel.innerHTML = h; $('riga-comp2').style.display = pp >= 3 ? '' : 'none';
    $('nome').value = G.nome; $('comp1').value = G.comp1; $('comp2').value = G.comp2;
    ['nome', 'comp1', 'comp2', 'banco'].forEach(function (k) {
      $(k).addEventListener('change', function () { G[k] = $(k).value.trim().replace(/\s+/g, ' '); metti(KG, G); ruoli(); rete(); ping(true); });
    });
    ruoli();
  }
  function ruoli() {}
  function rete() {
    var r = CONF.rete || {};
    [].forEach.call(document.querySelectorAll('[data-v]'), function (e) {
      var k = e.dataset.v; e.textContent = k === 'ip' ? ipDi(G.banco) : k === 'banco' ? (G.banco || '?') : (r[k] || '');
    });
  }

  /* ---------- passi ---------- */
  var ALL = [].slice.call(document.querySelectorAll('.passo')), P = [];
  function disegna() {
    var os = CONF.variante_os === 'B' ? 'B' : 'A'; document.body.dataset.os = os;
    P = ALL.filter(function (p) { return !p.dataset.os || p.dataset.os === os; });
    var n = 0, prossimo = null;
    P.forEach(function (p) {
      p.querySelector('.num').textContent = String(++n);
      var f = !!S[p.dataset.id]; p.classList.toggle('fatto', f); p.classList.remove('ora');
      p.querySelector('.bollo').textContent = f ? 'FATTO' : 'da fare'; p.querySelector('.fb').textContent = f ? 'Fatto ✓ (clic per togliere)' : 'Ho fatto!';
      if (!f && !prossimo) prossimo = p;
    });
    if (prossimo) { prossimo.classList.add('ora'); prossimo.querySelector('.bollo').textContent = 'ADESSO'; }
    var k = P.filter(function (p) { return S[p.dataset.id]; }).length;
    if ($('barra')) $('barra').style.width = Math.round(100 * k / (P.length || 1)) + '%';
    if ($('conta')) $('conta').textContent = 'Hai fatto ' + k + ' passi su ' + P.length + (k === P.length ? ' — BRAVI, avete finito questa ora!' : '. Ti mancano ' + (P.length - k) + ' passi.');
    if ($('vai')) $('vai').innerHTML = prossimo ? 'Vai qui adesso: <a href="#" id="vai-a">passo ' + esc(prossimo.querySelector('.num').textContent) + ' · ' + esc(prossimo.querySelector('h2').textContent.replace(/^\d+/, '')) + ' &rarr;</a>' : '<a href="index.html">Torna al percorso di oggi &rarr;</a>';
    if ($('vai-a')) $('vai-a').onclick = function (e) { e.preventDefault(); prossimo.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  }
  ALL.forEach(function (p) { p.querySelector('.fb').onclick = function () { S[p.dataset.id] = !S[p.dataset.id]; metti(K, S); disegna(); ping(false); }; });

  /* ---------- scheda ---------- */
  function scheda() {
    var box = $('scheda'); if (!box || !L.scheda) return;
    var h = '<h3>' + esc(L.scheda.titolo) + '</h3>';
    L.scheda.campi.forEach(function (c) {
      var v = R[c.k];
      if (c.t === 'scelta') h += '<div class="campo"><label for="f-' + c.k + '">' + esc(c.l) + '</label><select id="f-' + c.k + '" data-k="' + c.k + '"><option value="">scegli</option>' + c.o.map(function (o) { return '<option' + (o === v ? ' selected' : '') + '>' + esc(o) + '</option>'; }).join('') + '</select> <span id="e-' + c.k + '"></span></div>';
      else if (c.t === 'testo') h += '<div class="campo"><label for="f-' + c.k + '">' + esc(c.l) + '</label><input type="text" id="f-' + c.k + '" data-k="' + c.k + '" value="' + esc(v || '') + '"></div>';
      else if (c.t === 'spunta') h += '<div class="campo sp"><label><input type="checkbox" data-k="' + c.k + '"' + (v ? ' checked' : '') + '>' + esc(c.l) + '</label></div>';
      else if (c.t === 'spunte') h += '<div class="campo sp"><b>' + esc(c.l) + '</b>' + c.o.map(function (o) { return '<label><input type="checkbox" data-k="' + c.k + '" data-o="' + esc(o) + '"' + ((v || []).indexOf(o) >= 0 ? ' checked' : '') + '>' + esc(o) + '</label>'; }).join('') + '</div>';
    });
    if (Object.keys(L.chiave).length) h += '<button class="bt b" type="button" id="controlla">Controlla le lettere</button><p id="esito-l"></p>';
    box.innerHTML = h;
    [].forEach.call(box.querySelectorAll('[data-k]'), function (e) {
      e.addEventListener('change', function () {
        var k = e.dataset.k;
        if (e.dataset.o) R[k] = [].filter.call(box.querySelectorAll('[data-k="' + k + '"]'), function (x) { return x.checked; }).map(function (x) { return x.dataset.o; });
        else R[k] = e.type === 'checkbox' ? e.checked : e.value.trim();
        metti(KS, R); if (k === 'ip_vicino') cmd();
      });
    });
    if ($('controlla')) $('controlla').onclick = function () {
      var g = 0, ks = Object.keys(L.chiave);
      ks.forEach(function (k) { var ok = R[k] === L.chiave[k]; if (ok) g++; $('e-' + k).innerHTML = R[k] ? (ok ? '<span class="ok">✔</span>' : '<span class="ko">✘ riprova</span>') : ''; });
      $('esito-l').innerHTML = '<b>Giuste: ' + g + ' su ' + ks.length + '.</b> ' + (g >= 6 ? 'Bravi! Ora mandate la scheda.' : 'Ne servono almeno 6: guardate lo schema e riprovate.');
    };
    if (L.scheda.n === 3 && !R.ip && G.banco) { R.ip = ipDi(G.banco); metti(KS, R); var f = $('f-ip'); if (f) f.value = R.ip; }
    cmd();
    $('manda').onclick = manda;
  }
  function cmd() { var c = $('cmdping'); if (c) c.textContent = R.ip_vicino ? 'ping ' + R.ip_vicino : 'ping (scrivi nella scheda l\'IP del PC accanto)'; }
  function punti() { var g = 0; Object.keys(L.chiave).forEach(function (k) { if (R[k] === L.chiave[k]) g++; }); return g; }
  function postaForm(d) {
    var f = document.createElement('form'); f.method = 'POST'; f.action = CONF.invio; f.target = '_blank'; f.acceptCharset = 'UTF-8';
    var i = document.createElement('input'); i.type = 'hidden'; i.name = 'd'; i.value = JSON.stringify(d); f.appendChild(i);
    document.body.appendChild(f); f.submit(); f.remove();
  }
  window.costruisciScheda = function () {   // esposta per la prova automatica
    var comp = [G.comp1, G.comp2].filter(function (x) { return x && x.split(' ').length >= 2; });
    return { id: L.scheda.id, modo: 'verifica', classe: L.classe, nome: G.nome, compagni: comp, banco: G.banco, ora: L.ora,
      variante_os: CONF.variante_os || 'A', risposte: R, punti_lettere: punti(), quando: new Date().toISOString() };
  };
  function manda() {
    var m = $('msg');
    if (!G.nome || G.nome.split(' ').length < 2) { m.className = 'msg ko'; m.textContent = 'Scrivi nome e cognome nel riquadro «Chi siete?» in alto.'; $('nome').focus(); return; }
    var d = window.costruisciScheda();
    if (!d.compagni.length && !confirm('Non hai scritto il nome del compagno. Mandi lo stesso?')) return;
    if (!CONF.attivo || !CONF.invio) { m.className = 'msg ko'; m.textContent = 'ANTEPRIMA: invio spento.'; return; }
    postaForm(d);
    m.className = 'msg ok'; m.textContent = 'Mandata! Si è aperta una scheda con scritto «Consegna arrivata al prof». Potete rimandarla se cambiate qualcosa: vale l\'ultima.';
    metti('inviata-' + L.classe + '-' + L.ora, new Date().toISOString());
    S.scheda = true; metti(K, S); disegna(); ping(true);
  }

  /* ---------- segnale di avanzamento (cruscotto) e quiz ---------- */
  var ultimo = '';
  function ping(forza) {
    if (!CONF.attivo || !CONF.invio || !G.nome || L.indice) return;
    var fatti = P.filter(function (p) { return S[p.dataset.id]; }).length, ch = fatti + ':' + G.banco;
    if (ch === ultimo && !forza) return; ultimo = ch;
    var d = { id: 'avz-' + L.slug, modo: 'avanzamento', classe: L.classe, nome: G.nome, compagni: [G.comp1, G.comp2].filter(Boolean), banco: G.banco,
      scheda: fatti, totale: P.length, risposte: fatti, quiz: !!S.quiz, quando: new Date().toISOString() };
    try { fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) }); } catch (x) {}
  }
  function quiz() {
    [].forEach.call(document.querySelectorAll('[data-quiz]'), function (a) {
      var u = (CONF[a.dataset.quiz] || '').trim(), m = document.querySelector('[data-quizmsg="' + a.dataset.quiz + '"]');
      if (u) { a.href = u; a.style.opacity = 1; a.style.pointerEvents = ''; if (m) m.textContent = ''; }
      else { a.removeAttribute('href'); a.style.opacity = .5; a.style.pointerEvents = 'none'; if (m) m.textContent = 'Il quiz non è ancora aperto: premi F5 quando il Professore lo dice.'; }
    });
  }
  [].forEach.call(document.querySelectorAll('pre'), function (pr) {
    var b = document.createElement('button'); b.className = 'cp'; b.type = 'button'; b.textContent = 'Copia';
    b.onclick = function () { var t = (pr.querySelector('.t') || pr).textContent; try { navigator.clipboard.writeText(t).then(function () { b.textContent = 'Copiato!'; }, function () { b.textContent = 'Seleziona a mano'; }); } catch (x) { b.textContent = 'Seleziona a mano'; } setTimeout(function () { b.textContent = 'Copia'; }, 1800); };
    pr.appendChild(b);
  });
  function tutto() { if (L.indice) indice(); disegna(); ruoli(); rete(); quiz(); }
  function giro() { fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) { CONF = c || CONF; tutto(); }).catch(function () {}); }
  chi(); scheda(); tutto(); giro(); setInterval(giro, 30000); setInterval(function () { ping(true); }, 120000);
})();
