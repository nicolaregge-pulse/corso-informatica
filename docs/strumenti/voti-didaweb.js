/* Voti DIDAweb v1.0 (07/10/2026) — scrive i voti nella colonna scelta del Registro delle valutazioni.
   Struttura reale della pagina (registro_docente_valutazioni_nuovo.aspx): nomi in
   #ContentPlaceHolder1_griglia_elenco_alunni (righe R_<num>_<idAlunno>, cella cell_nome_<idAlunno>),
   caselle dei voti in td#ContentPlaceHolder1_Cell_<idColonna>_<idAlunno> > input (onchange = segna_aggiornamento).
   NON salva: il docente controlla e preme SALVA. Non scrive dove c'è già un voto diverso. */
(function () {
  var V = '1.0';
  function norm(s) { return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toUpperCase().replace(/[^A-Z ]/g, ' ').replace(/\s+/g, ' ').trim(); }
  var alunni = [];
  document.querySelectorAll('#ContentPlaceHolder1_griglia_elenco_alunni tr[id^="R_"]').forEach(function (r) {
    var m = r.id.match(/^R_(\d+)_(\d+)$/); if (!m) return;
    var c = document.getElementById('cell_nome_' + m[2]);
    if (c) alunni.push({ num: m[1], id: m[2], nome: norm(c.textContent), vero: c.textContent.trim() });
  });
  if (!alunni.length) { alert('Voti DIDAweb v' + V + ': non trovo gli alunni.\nApri Registro personale, scheda VALUTAZIONI.'); return; }
  var celle = document.querySelectorAll('td[id^="ContentPlaceHolder1_Cell_"][id$="_' + alunni[0].id + '"]');
  var r1 = document.querySelectorAll('#ContentPlaceHolder1_tabella_intestazione_dx tr:nth-child(1) td');
  var r2 = document.querySelectorAll('#ContentPlaceHolder1_tabella_intestazione_dx tr:nth-child(2) td');
  var col = [];
  for (var i = 0; i < celle.length; i++) {
    var m = celle[i].id.match(/_Cell_(\w+)_\d+$/);
    if (!m || m[1] === 'M') break;                      // le colonne dei voti stanno prima della MEDIA
    col.push({ id: m[1], nome: ((r1[i] ? r1[i].textContent : '') + ' ' + (r2[i] ? r2[i].textContent : '')).replace(/\s+/g, ' ').trim() });
  }
  if (!col.length) { alert('Voti DIDAweb v' + V + ': non c\'è nessuna colonna di voti.\nPrima premi NUOVO VOTO, scegli data e ora, OK.'); return; }
  var scelta = col[0];
  if (col.length > 1) {
    var t = 'In quale colonna scrivo i voti? Scrivi il numero:\n';
    col.forEach(function (c, k) { t += (k + 1) + ' = ' + c.nome + '\n'; });
    var n = parseInt(prompt(t, String(col.length)), 10);
    if (!(n >= 1 && n <= col.length)) { alert('Numero non valido: non ho scritto niente.'); return; }
    scelta = col[n - 1];
  }
  var lista = prompt('Colonna: ' + scelta.nome + '\nIncolla la lista dei voti (una riga sola, la prepara Claude):', '');
  if (!lista) return;
  var re = /([^;0-9]+?)\s*;\s*(\d{1,3})/g, x, scritti = [], nonTrovati = [], doppi = [], giaPresenti = [], fuori = [];
  while ((x = re.exec(lista))) {
    var chiave = norm(x[1]), voto = parseInt(x[2], 10);
    if (!chiave) continue;
    if (voto < 40 || voto > 100) { fuori.push(x[1].trim() + ' ' + voto); continue; }
    var parole = chiave.split(' ');
    var trovati = alunni.filter(function (a) { var s = ' ' + a.nome + ' '; return parole.every(function (p) { return s.indexOf(' ' + p + ' ') >= 0; }); });
    if (trovati.length === 0) { nonTrovati.push(x[1].trim()); continue; }
    if (trovati.length > 1) { doppi.push(x[1].trim()); continue; }
    var a = trovati[0], cella = document.getElementById('ContentPlaceHolder1_Cell_' + scelta.id + '_' + a.id);
    var inp = cella && cella.querySelector('input');
    if (!inp || inp.disabled) { nonTrovati.push(x[1].trim() + ' (casella non trovata)'); continue; }
    if (inp.value && inp.value.trim() !== String(voto)) { giaPresenti.push(a.vero + ' (c\'è già ' + inp.value + ')'); continue; }
    inp.value = String(voto);
    inp.dispatchEvent(new Event('input', { bubbles: true }));
    inp.dispatchEvent(new Event('change', { bubbles: true }));
    inp.style.background = '#fff3a0';
    scritti.push(a.num + ' ' + a.vero + ' = ' + voto);
  }
  var msg = 'Voti DIDAweb v' + V + ' — colonna ' + scelta.nome + '\nScritti: ' + scritti.length + ' (in giallo).';
  if (nonTrovati.length) msg += '\nNON trovati: ' + nonTrovati.join(', ');
  if (doppi.length) msg += '\nNome che vale per più alunni: ' + doppi.join(', ');
  if (giaPresenti.length) msg += '\nNON scritti perché c\'è già un voto: ' + giaPresenti.join(', ');
  if (fuori.length) msg += '\nVoto fuori da 40-100: ' + fuori.join(', ');
  msg += '\n\nControlla i numeri in giallo, poi premi SALVA.';
  alert(msg);
})();
