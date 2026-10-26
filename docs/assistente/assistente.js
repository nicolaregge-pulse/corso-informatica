/* La casella «Chiedi aiuto all'assistente» (RIFERIMENTI §2.53).
   Si mette in ogni pagina per i ragazzi con UNA riga, in fondo alla pagina:
     <script src="(percorso)/assistente/assistente.js" data-pagina="nome-della-pagina" data-lingue="it,ar,zh"></script>
   Senza l'indirizzo «invio» (applicazione web dello script) la domanda passa dal Modulo «Consegna»: Copia, Apri il Modulo, prima casella «aiuto», seconda Ctrl+V, Invia (14/10/2026).
   La domanda va allo script con un solo bottone; le risposte stanno in docs/assistente/risposte/<pagina>.json
   e compaiono sotto la casella a chi ha scritto quel nome. */
(function () {
  'use strict';
  var me = document.currentScript, base = me.src.replace(/assistente\/assistente\.js.*$/, '');
  var pagina = (me.dataset.pagina || location.pathname).replace(/[^a-z0-9-]/gi, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  var lingue = (me.dataset.lingue || 'it').split(',');
  var MODULO = 'https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform';
  var T = {
    it: { t: "Chiedi aiuto all'assistente", n: 'Il tuo nome e cognome', q: 'Scrivi la domanda, oppure incolla qui il codice o l\'errore: faccio un check', img: 'Aggiungi la foto dell\'errore (o incolla lo screenshot con Ctrl+V)', imgok: 'Foto pronta', imgno: 'Togli la foto', b: 'Manda', in: 'Sto mandando…', ok: 'Mandata! La risposta compare qui sotto entro qualche minuto.', ko: 'Non è partita: riprova.', vuoto: 'Scrivi il nome e la domanda.', r: 'Le risposte per te', m1: 'Premi «Copia la domanda».', m2: 'Premi «Apri il Modulo».', m3: 'Nel Modulo: prima casella scrivi aiuto, seconda casella premi Ctrl+V, poi «Invia».', cq: 'Copia la domanda', am: 'Apri il Modulo', cp: 'Copiata: nel Modulo, seconda casella, Ctrl+V' },
    // senza applicazione web: la strada del Modulo
    ar: { t: 'اطلب المساعدة من المساعد', n: 'اسمك ولقبك', q: 'اكتب سؤالك، أو الصق هنا الكود أو الخطأ: سأتحقق منه', img: 'أضف صورة الخطأ (أو الصق لقطة الشاشة بـ Ctrl+V)', imgok: 'الصورة جاهزة', imgno: 'احذف الصورة', b: 'إرسال', in: 'جارٍ الإرسال…', ok: 'تم الإرسال! الجواب يظهر هنا في الأسفل.', ko: 'لم يُرسل: حاول مرة أخرى.', vuoto: 'اكتب الاسم والسؤال.', r: 'الأجوبة لك', m1: 'اضغط «Copia la domanda» (انسخ السؤال).', m2: 'اضغط «Apri il Modulo» (افتح النموذج).', m3: 'في النموذج: الخانة الأولى اكتب aiuto، الخانة الثانية اضغط Ctrl+V، ثم «Invia».', cq: 'انسخ السؤال', am: 'افتح النموذج', cp: 'نُسخ' },
    zh: { t: '向助手求助', n: '你的名字和姓', q: '写你的问题，或者在这里粘贴代码或错误：我来检查', img: '添加错误的图片（或用 Ctrl+V 粘贴截图）', imgok: '图片已准备好', imgno: '删除图片', b: '发送', in: '正在发送…', ok: '发送了！回答会出现在下面。', ko: '没有发出去：再试一次。', vuoto: '写名字和问题。', r: '给你的回答', m1: '按「Copia la domanda」（复制问题）。', m2: '按「Apri il Modulo」（打开表单）。', m3: '在表单里：第一个框写 aiuto，第二个框按 Ctrl+V，然后按「Invia」（发送）。', cq: '复制问题', am: '打开表单', cp: '已复制' }
  };
  function tr(k) { return lingue.map(function (l) { return T[l] ? T[l][k] : ''; }).filter(Boolean).join(' · '); }
  function e(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function leggi(k) { try { return localStorage.getItem(k) || ''; } catch (x) { return ''; } }
  function scrivi(k, v) { try { localStorage.setItem(k, v); } catch (x) {} }
  fetch(base + 'verifica/config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (cfg) {
    cfg = cfg || {}; var diretta = !!cfg.invio;
    var box = document.createElement('section');
    box.setAttribute('style', 'max-width:860px;margin:30px auto;padding:14px 16px;border:3px solid #1f6feb;border-radius:12px;font:18px/1.5 system-ui,Segoe UI,Arial,sans-serif');
    box.innerHTML = '<h2 style="margin:0 0 8px;font-size:22px">' + e(tr('t')) + '</h2>' +
      '<input id="as-nome" style="font:inherit;width:100%;padding:8px;margin:4px 0;border:1px solid #9aa6b6;border-radius:6px" placeholder="' + e(tr('n')) + '">' +
      '<textarea id="as-q" rows="3" style="font:inherit;width:100%;padding:8px;margin:4px 0;border:1px solid #9aa6b6;border-radius:6px" placeholder="' + e(tr('q')) + '"></textarea>' +
      (diretta ? '<div style="margin:4px 0 8px"><label style="display:inline-block;cursor:pointer;background:#eef3fb;border:1px dashed #1f6feb;border-radius:8px;padding:8px 12px">' + e(tr('img')) + '<input id="as-f" type="file" accept="image/*" style="display:none"></label> <span id="as-fp"></span></div>' : '') +
      (diretta ? '<button id="as-b" style="font:inherit;font-weight:700;background:#1a7f37;color:#fff;border:0;border-radius:8px;padding:10px 20px;cursor:pointer">' + e(tr('b')) + '</button>' :
        '<ol style="padding-left:22px"><li>' + e(tr('m1')) + '<br><button id="as-c" style="font:inherit;font-weight:700;background:#1f6feb;color:#fff;border:0;border-radius:8px;padding:8px 16px;cursor:pointer">' + e(tr('cq')) + '</button></li><li>' + e(tr('m2')) + '<br><a target="_blank" rel="noopener" href="' + MODULO + '" style="display:inline-block;font-weight:700;background:#1f6feb;color:#fff;border-radius:8px;padding:8px 16px;text-decoration:none">' + e(tr('am')) + '</a></li><li>' + e(tr('m3')) + '</li></ol>') + ' <span id="as-st"></span>' +
      '<div id="as-r"></div>';
    document.body.appendChild(box);
    var nome = document.getElementById('as-nome'); nome.value = leggi('assistente-nome');
    if (!diretta) document.getElementById('as-c').onclick = function () {
      var q = document.getElementById('as-q').value.trim(), n = nome.value.trim(), st = document.getElementById('as-st');
      if (!q || !n) { st.textContent = tr('vuoto'); return; } scrivi('assistente-nome', n);
      navigator.clipboard.writeText(n + ' (' + pagina + '): ' + q).then(function () { st.textContent = tr('cp'); });
    };
    // 22/10/2026: la foto dell'errore (file o Ctrl+V nella casella), ridotta a JPEG perché lo script accetta al massimo 300.000 caratteri
    var foto = '';
    function mettiFoto(file) {
      if (!file || !/^image\//.test(file.type)) return;
      var r = new FileReader();
      r.onload = function () {
        var img = new Image();
        img.onload = function () {
          var lato = 1400, k = Math.min(1, lato / Math.max(img.width, img.height)), c = document.createElement('canvas');
          c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
          c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
          var q = 0.8; foto = c.toDataURL('image/jpeg', q);
          while (foto.length > 230000 && q > 0.25) { q -= 0.1; foto = c.toDataURL('image/jpeg', q); }
          if (foto.length > 230000) { c.width = Math.round(c.width / 2); c.height = Math.round(c.height / 2); c.getContext('2d').drawImage(img, 0, 0, c.width, c.height); foto = c.toDataURL('image/jpeg', 0.5); }
          document.getElementById('as-fp').innerHTML = '<img src="' + foto + '" style="height:60px;vertical-align:middle;border:1px solid #9aa6b6;border-radius:4px"> ' + e(tr('imgok')) + ' <button id="as-fx" style="font:inherit">' + e(tr('imgno')) + '</button>';
          document.getElementById('as-fx').onclick = function () { foto = ''; document.getElementById('as-fp').innerHTML = ''; document.getElementById('as-f').value = ''; };
        };
        img.src = r.result;
      };
      r.readAsDataURL(file);
    }
    if (diretta) {
      document.getElementById('as-f').onchange = function () { mettiFoto(this.files[0]); };
      document.getElementById('as-q').addEventListener('paste', function (ev) {
        var it = (ev.clipboardData && ev.clipboardData.items) || [];
        for (var i = 0; i < it.length; i++) if (it[i].type.indexOf('image') === 0) { mettiFoto(it[i].getAsFile()); ev.preventDefault(); return; }
      });
    }
    if (diretta) document.getElementById('as-b').onclick = function () {
      var q = document.getElementById('as-q').value.trim(), n = nome.value.trim(), st = document.getElementById('as-st');
      if ((!q && !foto) || !n) { st.textContent = tr('vuoto'); return; }
      scrivi('assistente-nome', n);
      var bt = this; bt.disabled = true; bt.style.opacity = '.6';
      var d = { id: 'assistente-' + pagina, nome: n, modo: 'domanda', domanda: q || '(foto)', pagina: location.href, ora: new Date().toISOString() };
      if (foto) { d.immagine = foto; foto = ''; document.getElementById('as-fp').innerHTML = ''; document.getElementById('as-f').value = ''; }
      // 15/10: lo script ci mette fino a un minuto a rispondere; la domanda però è già partita, quindi lo diciamo subito
      // e svuotiamo la casella adesso (mai dopo, per non cancellare quello che il ragazzo sta scrivendo)
      document.getElementById('as-q').value = ''; st.textContent = '…';   // 26/10: «Mandata!» solo quando l'invio è partito davvero (domanda di Bettinelli persa)
      setTimeout(function () { bt.disabled = false; bt.style.opacity = '1'; }, 3000);
      fetch(cfg.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) })
        .then(function () { st.textContent = tr('ok'); })
        .catch(function () { st.textContent = tr('ko'); document.getElementById('as-q').value = q; });
    };
    function risposte() {
      var n = (nome.value || leggi('assistente-nome')).trim().toLowerCase(); if (!n) return;
      fetch(base + 'assistente/risposte/' + pagina + '.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : []; }).then(function (L) {
        var mie = (L || []).filter(function (x) { var a = String(x.nome || '').toLowerCase(); return a && (n.indexOf(a.replace(/\.$/, '').split(' ')[0]) === 0); });
        document.getElementById('as-r').innerHTML = mie.length ? '<h3 style="font-size:18px;margin:12px 0 4px">' + e(tr('r')) + '</h3>' + mie.map(function (x) { return '<p style="margin:6px 0"><i>' + e(x.domanda) + '</i><br><b style="white-space:pre-line">' + e(x.risposta) + '</b></p>'; }).join('') : '';
      }).catch(function () {});
    }
    risposte(); setInterval(risposte, 60000);
  }).catch(function () {});
})();
