/* Voti DIDAweb v0.3 (07/10/2026) — riempie la colonna del voto nuovo nel "Registro delle valutazioni" di DIDAweb.
   Nessun dato degli allievi qui dentro: nomi e voti li incolla il docente nella finestrella.
   Funziona sia se nomi e caselle stanno nella stessa tabella, sia se stanno in due tabelle affiancate
   (in quel caso abbina per posizione: si clicca prima la casella del PRIMO alunno). Non preme SALVA. */
(function () {
  var a = window.__votiCella || document.activeElement;
  if (!a || a.tagName !== 'INPUT') { alert('Prima clicca dentro la casella del PRIMO alunno nella colonna del voto nuovo, poi clicca di nuovo il segnalibro.'); return; }
  var td = a.closest('td'), col = td.cellIndex, tab = a.closest('table'), tr0 = a.closest('tr');
  var t = prompt('Incolla qui la riga dei voti preparata da Claude e premi OK');
  if (!t) return;
  function P(s) { return s.toUpperCase().normalize('NFD').split('').filter(function (c) { return c.charCodeAt(0) < 128; }).join('').split(/[^A-Z]+/).filter(function (x) { return x.length > 1; }); }
  var L = [], re = /([^;\d]+);\s*(\d{1,3})/g, m;
  while ((m = re.exec(t))) { var n = P(m[1]); if (n.length) L.push({ n: n, v: m[2] }); }
  if (!L.length) { alert('Non ho trovato voti nel testo incollato.'); return; }
  function trova(rows, x) { return rows.filter(function (tr) { var nome = P(tr.textContent); return x.n.every(function (w) { return nome.indexOf(w) >= 0; }); }); }
  // righe con la casella nella colonna scelta (stessa tabella della casella cliccata)
  var righeVoto = [].slice.call(tab.rows).filter(function (tr) { var c = tr.cells[col]; return c && c.querySelector('input'); });
  var base = righeVoto.indexOf(tr0);
  // righe degli alunni nelle ALTRE tabelle: prima cella = numero
  var righeNomi = [].slice.call(document.querySelectorAll('tr')).filter(function (tr) {
    return !tab.contains(tr) && tr.cells.length >= 2 && /^\s*\d{1,2}\s*$/.test(tr.cells[0].textContent) && P(tr.textContent).length >= 2; });
  var ok = 0, manca = [];
  L.forEach(function (x) {
    var stesse = trova([].slice.call(tab.rows), x), riga = null;
    if (stesse.length === 1) riga = stesse[0];
    else if (stesse.length === 0) {
      var r = trova(righeNomi, x);
      if (r.length === 1) { var k = righeNomi.indexOf(r[0]); riga = righeVoto[base + k] || null; }
      else { manca.push(x.n.join(' ') + (r.length ? ' (doppio)' : '')); return; }
    } else { manca.push(x.n.join(' ') + ' (doppio)'); return; }
    var c = riga && riga.cells[col], i = c && c.querySelector('input');
    if (!i) { manca.push(x.n.join(' ') + ' (casella non trovata)'); return; }
    i.focus(); i.value = x.v;
    ['input', 'change', 'keyup', 'blur'].forEach(function (ev) { i.dispatchEvent(new Event(ev, { bubbles: true })); });
    ok++;
  });
  alert('Voti scritti: ' + ok + (manca.length ? '\nNon trovati: ' + manca.join(', ') : '') + '\nControlla la colonna (i nomi devono coincidere riga per riga) e poi premi SALVA.');
})();
