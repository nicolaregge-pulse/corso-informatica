/* La casella «Chiedi aiuto all'assistente del Prof Regge» (RIFERIMENTI §2.53).
   Si mette in ogni pagina per i ragazzi con UNA riga, in fondo alla pagina:
     <script src="(percorso)/assistente/assistente.js" data-pagina="nome-della-pagina" data-lingue="it,ar,zh"></script>
   Resta nascosta finché docs/verifica/config.json non ha l'indirizzo «invio» (l'applicazione web dello script).
   La domanda va allo script con un solo bottone; le risposte stanno in docs/assistente/risposte/<pagina>.json
   e compaiono sotto la casella a chi ha scritto quel nome. */
(function () {
  'use strict';
  var me = document.currentScript, base = me.src.replace(/assistente\/assistente\.js.*$/, '');
  var pagina = (me.dataset.pagina || location.pathname).replace(/[^a-z0-9-]/gi, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  var lingue = (me.dataset.lingue || 'it').split(',');
  var T = {
    it: { t: "Chiedi aiuto all'assistente del Prof Regge", n: 'Il tuo nome e cognome', q: 'Scrivi la tua domanda', b: 'Manda', ok: 'Mandata! La risposta compare qui sotto.', ko: 'Non è partita: riprova.', vuoto: 'Scrivi il nome e la domanda.', r: 'Le risposte per te' },
    ar: { t: 'اطلب المساعدة من مساعد الأستاذ Regge', n: 'اسمك ولقبك', q: 'اكتب سؤالك', b: 'إرسال', ok: 'تم الإرسال! الجواب يظهر هنا في الأسفل.', ko: 'لم يُرسل: حاول مرة أخرى.', vuoto: 'اكتب الاسم والسؤال.', r: 'الأجوبة لك' },
    zh: { t: '向 Regge 老师的助手求助', n: '你的名字和姓', q: '写你的问题', b: '发送', ok: '发送了！回答会出现在下面。', ko: '没有发出去：再试一次。', vuoto: '写名字和问题。', r: '给你的回答' }
  };
  function tr(k) { return lingue.map(function (l) { return T[l] ? T[l][k] : ''; }).filter(Boolean).join(' · '); }
  function e(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function leggi(k) { try { return localStorage.getItem(k) || ''; } catch (x) { return ''; } }
  function scrivi(k, v) { try { localStorage.setItem(k, v); } catch (x) {} }
  fetch(base + 'verifica/config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (cfg) {
    if (!cfg || !cfg.invio) return;   // consegna diretta non ancora attiva: la casella non compare
    var box = document.createElement('section');
    box.setAttribute('style', 'max-width:860px;margin:30px auto;padding:14px 16px;border:3px solid #1f6feb;border-radius:12px;font:18px/1.5 system-ui,Segoe UI,Arial,sans-serif');
    box.innerHTML = '<h2 style="margin:0 0 8px;font-size:22px">' + e(tr('t')) + '</h2>' +
      '<input id="as-nome" style="font:inherit;width:100%;padding:8px;margin:4px 0;border:1px solid #9aa6b6;border-radius:6px" placeholder="' + e(tr('n')) + '">' +
      '<textarea id="as-q" rows="3" style="font:inherit;width:100%;padding:8px;margin:4px 0;border:1px solid #9aa6b6;border-radius:6px" placeholder="' + e(tr('q')) + '"></textarea>' +
      '<button id="as-b" style="font:inherit;font-weight:700;background:#1a7f37;color:#fff;border:0;border-radius:8px;padding:10px 20px;cursor:pointer">' + e(tr('b')) + '</button> <span id="as-st"></span>' +
      '<div id="as-r"></div>';
    document.body.appendChild(box);
    var nome = document.getElementById('as-nome'); nome.value = leggi('assistente-nome');
    document.getElementById('as-b').onclick = function () {
      var q = document.getElementById('as-q').value.trim(), n = nome.value.trim(), st = document.getElementById('as-st');
      if (!q || !n) { st.textContent = tr('vuoto'); return; }
      scrivi('assistente-nome', n);
      var d = { id: 'assistente-' + pagina, nome: n, modo: 'domanda', domanda: q, pagina: location.href, ora: new Date().toISOString() };
      fetch(cfg.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) })
        .then(function () { st.textContent = tr('ok'); document.getElementById('as-q').value = ''; })
        .catch(function () { st.textContent = tr('ko'); });
    };
    function risposte() {
      var n = (nome.value || leggi('assistente-nome')).trim().toLowerCase(); if (!n) return;
      fetch(base + 'assistente/risposte/' + pagina + '.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : []; }).then(function (L) {
        var mie = (L || []).filter(function (x) { var a = String(x.nome || '').toLowerCase(); return a && (n.indexOf(a.replace(/\.$/, '').split(' ')[0]) === 0); });
        document.getElementById('as-r').innerHTML = mie.length ? '<h3 style="font-size:18px;margin:12px 0 4px">' + e(tr('r')) + '</h3>' + mie.map(function (x) { return '<p style="margin:6px 0"><i>' + e(x.domanda) + '</i><br><b>' + e(x.risposta) + '</b></p>'; }).join('') : '';
      }).catch(function () {});
    }
    risposte(); setInterval(risposte, 60000);
  }).catch(function () {});
})();
