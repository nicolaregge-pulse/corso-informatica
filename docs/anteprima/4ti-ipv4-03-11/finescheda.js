/* Fine scheda 4TI IPv4: un click manda il segnale «scheda finita». Legge config.json (invio, attivo). */
(function () {
  var sc = document.currentScript, n = +(sc.getAttribute('data-scheda') || 0), ID = '4ti-ipv4-0311-schede';
  function $(i) { return document.getElementById(i); }
  function prendi(k) { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (x) { return null; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  var CONF = {}; fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) { CONF = c || {}; }).catch(function () {});
  function nomeSalvato() { var a = prendi('scheda-4ti-0311'), b = prendi('ti-0311-nome'); return String((a && a.nome) || b || '').trim(); }
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  pronto(function () {
    var nav = document.querySelector('.nav'); if (!nav) return;
    var fatte = prendi('ti-0311-finite') || {};
    var box = document.createElement('section'); box.className = 'card vinci';
    box.innerHTML = '<h3>Hai finito questa scheda?</h3>' +
      '<p class="mu">Premi il bottone: il professore vede che sei a questo punto.</p>' +
      '<div id="fs-nome" style="display:none"><p><b>Come ti chiami?</b></p><input type="text" id="fs-in" placeholder="Nome Cognome" autocomplete="name"></div>' +
      '<button class="bt v" id="fs-bt" type="button">Ho finito la scheda ' + n + '</button><p class="msg" id="fs-msg"></p>';
    nav.parentNode.insertBefore(box, nav);
    var bt = $('fs-bt'), msg = $('fs-msg'), nm = nomeSalvato();
    if (!nm) $('fs-nome').style.display = 'block'; else $('fs-in').value = nm;
    function fatto(ora) { bt.disabled = true; bt.textContent = 'Scheda ' + n + ' finita!'; msg.className = 'msg ok'; msg.textContent = 'FATTO! Bravo! Mandato alle ' + ora + '. Ora vai avanti.'; $('fs-nome').style.display = 'none'; }
    if (fatte['s' + n]) fatto(fatte['s' + n]);
    bt.onclick = function () {
      var nome = $('fs-in').value.trim().replace(/\s+/g, ' ');
      if (nome.split(' ').length < 2) { msg.className = 'msg ko'; msg.textContent = 'Scrivi nome e cognome, poi premi di nuovo.'; $('fs-nome').style.display = 'block'; $('fs-in').focus(); return; }
      if (!CONF.attivo || !CONF.invio) { msg.className = 'msg ko'; msg.textContent = 'Ancora non posso mandare. Premi F5 e riprova.'; return; }
      var R = { id: ID, modo: 'verifica', classe: '4TI', cosa: 'scheda_finita', scheda: n, nome: nome, consegnata: true, quando: new Date().toISOString() };
      bt.disabled = true; msg.className = 'msg'; msg.textContent = 'Sto mandando...';
      fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(R)) }).then(function () {
        var ora = new Date().toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' });
        metti('ti-0311-nome', nome); fatte['s' + n] = ora; metti('ti-0311-finite', fatte); fatto(ora);
      }).catch(function () { bt.disabled = false; msg.className = 'msg ko'; msg.textContent = 'Non è partito. Controlla internet e premi di nuovo.'; });
    };
  });
})();
