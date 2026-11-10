/**
 * FABBRICA - MOTORE v2.1 (10/11/2026)
 * Codice puro: lo scarica ed esegue (eval) il "lancio" a ogni giro. Usa le globali del lancio FB_BASE e UTENTI
 * ({ '3INF': [[pc, utenteGitHub, 'COGNOME Nome'], ...] }) e i servizi Google. Chiama FB_main_() dopo l'eval.
 * Properties usate: FB_FOGLIO, FB_FATTI, GITHUB_TOKEN (da v1), FB_FORMS, FB_NR, FB_ULTERR (nuove).
 * Changelog: 2.1 elenco ragazzi letto dalla scheda 'Cruscotto Git <classe>' (UTENTI del lancio puo essere {}); 2.0 tutte le classi, registro Moduli, risultati (schede "Ris <id>"), scheda "Stato", cruscotti per classe.
 */

function FB_p_() { return PropertiesService.getScriptProperties(); }
function FB_json_(k) { try { return JSON.parse(FB_p_().getProperty(k) || '{}') || {}; } catch (e) { return {}; } }
function FB_salva_(k, o) { FB_p_().setProperty(k, JSON.stringify(o)); }
function FB_ora_(f) { return Utilities.formatDate(new Date(), 'Europe/Rome', f || 'dd/MM HH:mm:ss'); }

function FB_get_(url) {
  var r = UrlFetchApp.fetch(url + (url.indexOf('?') < 0 ? '?' : '&') + 't=' + Date.now(), { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('HTTP ' + r.getResponseCode() + ' ' + url);
  return r.getContentText();
}

var FB_TESTA_ = ['Ora', 'Id', 'Titolo', 'Link per i ragazzi', 'Link di modifica', 'Controllo', 'Classe', 'FormId'];

function FB_foglio_() {
  var id = FB_p_().getProperty('FB_FOGLIO'), ss;
  if (id) ss = SpreadsheetApp.openById(id);
  else {
    ss = SpreadsheetApp.create('Fabbrica (10/11/2026)');
    FB_p_().setProperty('FB_FOGLIO', ss.getId());
    ss.getSheets()[0].setName('Esiti');
  }
  var sh = ss.getSheetByName('Esiti') || ss.insertSheet('Esiti');
  sh.getRange(1, 1, 1, FB_TESTA_.length).setValues([FB_TESTA_]).setFontWeight('bold');
  return ss;
}

function FB_classe_(q, id) {
  if (q && q.classe) return String(q.classe).toUpperCase();
  var m = /^[A-Za-z]+-(\d+[A-Za-z]+)-/.exec(id || '');
  return m ? m[1].toUpperCase() : '';
}

/* ---------- Moduli ---------- */
function FB_attese_(q) {
  return q.domande.map(function (d) {
    if (d.tipo === 'multi') return { tipo: 'multi', scelte: d.s.length, giuste: d.s.filter(function (x) { return x[1]; }).length, titolo: d.t };
    if (d.tipo === 'singola') return { tipo: 'singola', scelte: d.s.length, giuste: 1, titolo: d.t };
    return { tipo: d.tipo, titolo: d.t };
  });
}

function FB_verifica_(form, attese) {
  var items = form.getItems(), err = [], ok = 0;
  if (items.length !== attese.length) err.push('ci sono ' + items.length + ' domande invece di ' + attese.length);
  for (var i = 0; i < Math.min(items.length, attese.length); i++) {
    var a = attese[i], it = items[i], p = [];
    try {
      if (it.getTitle() !== a.titolo) p.push('titolo diverso');
      if (a.tipo === 'multi' || a.tipo === 'singola') {
        var tipo = a.tipo === 'multi' ? FormApp.ItemType.CHECKBOX : FormApp.ItemType.MULTIPLE_CHOICE;
        if (it.getType() !== tipo) p.push('tipo sbagliato (' + it.getType() + ')');
        else {
          var x = a.tipo === 'multi' ? it.asCheckboxItem() : it.asMultipleChoiceItem();
          var sc = x.getChoices();
          var g = sc.filter(function (c) { return c.isCorrectAnswer(); }).length;
          if (sc.length !== a.scelte) p.push(sc.length + ' scelte invece di ' + a.scelte);
          if (g !== a.giuste) p.push(g + ' giuste invece di ' + a.giuste);
        }
      } else {
        var t2 = a.tipo === 'testo' ? FormApp.ItemType.TEXT : FormApp.ItemType.PARAGRAPH_TEXT;
        if (it.getType() !== t2) p.push('tipo sbagliato (' + it.getType() + ')');
      }
    } catch (e) { p.push('lettura: ' + e); }
    if (p.length) err.push('domanda ' + (i + 1) + ': ' + p.join(', ')); else ok++;
  }
  return { ok: ok, tot: attese.length, err: err };
}

function FB_crea_(q) {
  var f = FormApp.create(q.titolo);
  f.setDescription(q.descrizione || '');
  f.setIsQuiz(true);
  if (q.mescola) f.setShuffleQuestions(true);
  f.setCollectEmail(true);
  f.setLimitOneResponsePerUser(false);
  try { f.setRequireLogin(true); } catch (e) { Logger.log('setRequireLogin: ' + e); }
  f.setConfirmationMessage(q.conferma || 'Fatto!');
  q.domande.forEach(function (d) {
    var it;
    if (d.tipo === 'multi' || d.tipo === 'singola') {
      it = d.tipo === 'multi' ? f.addCheckboxItem() : f.addMultipleChoiceItem();
      it.setTitle(d.t);
      it.setChoices(d.s.map(function (x) { return it.createChoice(x[0], x[1]); }));
      it.setPoints(d.punti || 1);
      if (d.sp) {
        it.setFeedbackForCorrect(FormApp.createFeedback().setText('Giusto! ' + d.sp).build());
        it.setFeedbackForIncorrect(FormApp.createFeedback().setText('Non ancora. ' + d.sp).build());
      }
    } else {
      it = d.tipo === 'testo' ? f.addTextItem() : f.addParagraphTextItem();
      it.setTitle(d.t);
      if (d.punti && typeof it.setPoints === 'function') it.setPoints(d.punti);
      it.setHelpText('Domanda aperta: la corregge il docente a mano.');
    }
    it.setRequired(true);
  });
  var v = FB_verifica_(f, FB_attese_(q));
  return { ragazzi: f.getPublishedUrl(), modifica: f.getEditUrl(), formId: f.getId(), v: v };
}

/* ---------- Errori e stato ---------- */
function FB_errore_(ss, passo, e) {
  var testo = passo + ': ' + (e && e.message ? e.message : e);
  FB_p_().setProperty('FB_ULTERR', FB_ora_() + ' ' + testo);
  try {
    if (FB_p_().getProperty('FB_ULTERR_RIGA') !== testo) {
      FB_p_().setProperty('FB_ULTERR_RIGA', testo);
      ss.getSheetByName('Esiti').appendRow([FB_ora_(), 'ERRORE', '', '', '', 'ERRORE: ' + testo, '', '']);
    }
  } catch (x) { Logger.log('FB_errore_: ' + x); }
}

function FB_stato_(ss) {
  var sh = ss.getSheetByName('Stato') || ss.insertSheet('Stato');
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), tot = 0, k, n = 0;
  for (k in forms) n++;
  for (k in nr) tot += Number(nr[k]) || 0;
  sh.getRange(1, 1, 4, 2).setValues([
    ['Fabbrica v2', FB_ora_('dd/MM/yyyy HH:mm:ss')],
    ['Moduli', n],
    ['Risposte totali', tot],
    ['Ultimo errore', FB_p_().getProperty('FB_ULTERR') || '']
  ]);
  sh.getRange(1, 1).setFontWeight('bold');
}

/* ---------- Passi ---------- */
function FB_nuovi_(ss, indice) {
  var fatti = FB_json_('FB_FATTI'), forms = FB_json_('FB_FORMS'), sh = ss.getSheetByName('Esiti');
  (indice.lavori || []).forEach(function (l) {
    if (fatti[l.id]) return;
    var ora = FB_ora_();
    try {
      var testo = Utilities.newBlob(Utilities.base64Decode(FB_get_(FB_BASE + l.file).trim())).getDataAsString('UTF-8');
      var q = JSON.parse(testo);
      var r = FB_crea_(q), cl = FB_classe_(q, l.id);
      var ctrl = r.v.err.length ? 'ERRORE: ' + r.v.err.join('; ') + ' (NON darlo ai ragazzi)' : 'OK ' + r.v.ok + '/' + r.v.tot;
      sh.appendRow([ora, l.id, q.titolo, r.ragazzi, r.modifica, ctrl, cl, r.formId]);
      forms[l.id] = { formId: r.formId, classe: cl, titolo: q.titolo };
      FB_salva_('FB_FORMS', forms);
    } catch (e) {
      sh.appendRow([ora, l.id, '', '', '', 'ERRORE: ' + e, FB_classe_(null, l.id), '']);
    }
    fatti[l.id] = 1;
    FB_salva_('FB_FATTI', fatti);
  });
}

function FB_ripara_(ss) {
  var sh = ss.getSheetByName('Esiti'), forms = FB_json_('FB_FORMS'), cambiato = false;
  var dati = sh.getDataRange().getValues();
  for (var i = 1; i < dati.length; i++) {
    var r = dati[i], id = String(r[1] || ''), link = String(r[4] || '');
    if (!id || id === 'ERRORE' || !link || forms[id]) continue;
    try {
      var fid = r[7] ? String(r[7]) : FormApp.openByUrl(link).getId();
      var cl = r[6] ? String(r[6]) : FB_classe_(null, id);
      forms[id] = { formId: fid, classe: cl, titolo: String(r[2] || '') };
      cambiato = true;
      sh.getRange(i + 1, 7, 1, 2).setValues([[cl, fid]]);
    } catch (e) { FB_errore_(ss, 'ripara ' + id, e); }
  }
  if (cambiato) FB_salva_('FB_FORMS', forms);
}

function FB_puntiTotali_(form) {
  var tot = 0;
  form.getItems().forEach(function (it) {
    try {
      var t = it.getType(), x = null, T = FormApp.ItemType;
      if (t === T.CHECKBOX) x = it.asCheckboxItem();
      else if (t === T.MULTIPLE_CHOICE) x = it.asMultipleChoiceItem();
      else if (t === T.TEXT) x = it.asTextItem();
      else if (t === T.PARAGRAPH_TEXT) x = it.asParagraphTextItem();
      if (x) tot += Number(x.getPoints()) || 0;
    } catch (e) { }
  });
  return tot;
}

function FB_risultati_(ss, t0) {
  var forms = FB_json_('FB_FORMS'), nr = FB_json_('FB_NR'), fatte = 0, id;
  for (id in forms) {
    if (fatte >= 5 || Date.now() - t0 > 270000) break;
    try {
      var form = FormApp.openById(forms[id].formId);
      var ris = form.getResponses(), n = ris.length;
      if (nr[id] === n) continue;
      var su = FB_puntiTotali_(form), per = {};
      ris.forEach(function (r) {
        var em = r.getRespondentEmail() || '(senza email)', s = 0;
        (r.getGradableItemResponses() || []).forEach(function (g) { s += Number(g.getScore()) || 0; });
        var ts = r.getTimestamp(), p = per[em] || (per[em] = { max: 0, t: 0, ult: null });
        if (s > p.max) p.max = s;
        p.t++;
        if (!p.ult || ts > p.ult) p.ult = ts;
      });
      var righe = Object.keys(per).map(function (em) {
        var p = per[em];
        return [em, p.max, su, p.t, p.ult ? Utilities.formatDate(p.ult, 'Europe/Rome', 'dd/MM HH:mm') : ''];
      });
      righe.sort(function (a, b) { return b[1] - a[1]; });
      var sh = ss.getSheetByName('Ris ' + id) || ss.insertSheet('Ris ' + id);
      sh.clear();
      sh.getRange(1, 1, 1, 5).setValues([['Email', 'Migliore', 'Su', 'Tentativi', 'Ultimo invio']]).setFontWeight('bold');
      if (righe.length) sh.getRange(2, 1, righe.length, 5).setValues(righe);
      nr[id] = n;
      FB_salva_('FB_NR', nr);
      fatte++;
    } catch (e) { FB_errore_(ss, 'risultati ' + id, e); }
  }
}

/* ---------- Cruscotto Git per classe ---------- */
function CG_get_(path) {
  var tok = FB_p_().getProperty('GITHUB_TOKEN');
  var h = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'fabbrica' };
  if (tok) h['Authorization'] = 'Bearer ' + tok;
  try {
    var r = UrlFetchApp.fetch('https://api.github.com/' + path, { headers: h, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null;
    return JSON.parse(r.getContentText());
  } catch (e) { return null; }
}

function CG_riga_(pc, utente, nome, oggi) {
  var repos = CG_get_('users/' + utente + '/repos?per_page=100&sort=pushed') || [];
  var sc = null, i;
  for (i = 0; i < repos.length; i++) { if (/master/i.test(repos[i].name)) { sc = repos[i]; break; } }
  if (!sc) for (i = 0; i < repos.length; i++) { if ((repos[i].pushed_at || '').slice(0, 10) === oggi) { sc = repos[i]; break; } }
  if (!sc && repos.length) sc = repos[0];
  var d = { repo: '-', push: '-', oggi: 0, ult: '-', tag: '-', rel: '-', chg: 'no', st: 'ROSSO' };
  if (sc) {
    var full = sc.full_name;
    d.repo = sc.name;
    d.push = (sc.pushed_at || '').replace('T', ' ').slice(11, 16) + ' UTC';
    var com = CG_get_('repos/' + full + '/commits?per_page=30') || [];
    for (i = 0; i < com.length; i++) { if (com[i].commit.author.date.slice(0, 10) === oggi) d.oggi++; }
    if (com.length) d.ult = String(com[0].commit.message).split('\n')[0].slice(0, 60);
    var tags = CG_get_('repos/' + full + '/tags?per_page=5') || [];
    if (tags.length) d.tag = tags.map(function (t) { return t.name; }).join(', ');
    var rel = CG_get_('repos/' + full + '/releases?per_page=5') || [], bozza = false;
    if (rel.length) { d.rel = (rel[0].name || rel[0].tag_name || 'senza nome') + (rel[0].draft ? ' (bozza)' : ''); bozza = !!rel[0].draft; }
    var cont = CG_get_('repos/' + full + '/contents/') || [];
    for (i = 0; i < cont.length; i++) { if (/changelog/i.test(cont[i].name)) d.chg = 'sì'; }
    if (rel.length && !bozza && tags.length) d.st = 'VERDE';
    else if (rel.length || tags.length) d.st = 'GIALLO';
    else if (d.oggi > 0) d.st = 'ARANCIO';
  }
  return [d.st, 'PC ' + pc, nome, utente, d.repo, d.push, d.oggi, d.tag, d.rel, d.chg, d.ult];
}

function CG_aggiorna_(ss, classe, utenti) {
  var nomeSh = 'Cruscotto Git ' + classe;
  var sh = ss.getSheetByName(nomeSh) || ss.insertSheet(nomeSh);
  var oggi = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd');
  var righe = utenti.map(function (u) { return CG_riga_(u[0], u[1], u[2], oggi); });
  var ord = { VERDE: 0, GIALLO: 1, ARANCIO: 2, ROSSO: 3 };
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]]; });
  sh.clear();
  var ora = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Git e Mastermind · release 1.0 · dati letti alle ' + ora).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = release pubblicata con tag · GIALLO = tag o bozza · ARANCIO = commit di oggi · ROSSO = nessuna attività. Solo repository pubblici.');
  var testa = ['Stato', 'PC', 'Allievo', 'Utente GitHub', 'Repository', 'Ultimo push', 'Commit oggi', 'Tag', 'Release', 'CHANGELOG', 'Ultimo commit'];
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (var i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}

function CG_leggiElenco_(ss, classe) {
  var sh = ss.getSheetByName('Cruscotto Git ' + classe), out = [];
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 4; i < v.length; i++) {
    var n = parseInt(String(v[i][1]).replace(/\D/g, ''), 10), nome = String(v[i][2] || '').trim(), ut = String(v[i][3] || '').trim();
    if (!ut || !nome || isNaN(n)) continue;
    out.push([n, ut, nome]);
  }
  return out;
}

function FB_cruscotti_(ss, indice) {
  var lista = indice.cruscotti;
  if (!lista && indice.cruscotto && indice.cruscotto.attivo) lista = [{ classe: '3INF', attivo: true }];
  if (new Date().getMinutes() % 2 !== 0) return;
  (lista || []).forEach(function (c) {
    if (c.attivo === false) return;
    var u = (typeof UTENTI !== 'undefined' && UTENTI) ? UTENTI[c.classe] : null;
    if (!u || !u.length) u = CG_leggiElenco_(ss, c.classe);
    if (!u.length) {
      var es = ss.getSheetByName('Esiti'), msg = 'Cruscotto ' + c.classe + ': nessun elenco';
      var rr = es ? es.getDataRange().getValues() : [];
      if (!rr.length || String(rr[rr.length - 1][5]) !== msg) if (es) es.appendRow([FB_ora_(), 'AVVISO', '', '', '', msg, '', '']);
      return;
    }
    try { CG_aggiorna_(ss, c.classe, u); } catch (e) { FB_errore_(ss, 'cruscotto ' + c.classe, e); }
  });
}

/* ---------- Giro principale ---------- */
function FB_main_() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var t0 = Date.now();
    var ss = FB_foglio_(), indice = { lavori: [] };
    try { indice = JSON.parse(FB_get_(FB_BASE + 'indice.json')); } catch (e) { FB_errore_(ss, 'indice', e); indice = null; }
    if (indice) {
      try { FB_nuovi_(ss, indice); } catch (e) { FB_errore_(ss, 'nuovi', e); }
    }
    try { FB_ripara_(ss); } catch (e) { FB_errore_(ss, 'ripara', e); }
    try { FB_risultati_(ss, t0); } catch (e) { FB_errore_(ss, 'risultati', e); }
    if (indice) {
      try { FB_cruscotti_(ss, indice); } catch (e) { FB_errore_(ss, 'cruscotti', e); }
    }
    try { FB_stato_(ss); } catch (e) { Logger.log('stato: ' + e); }
  } finally {
    lock.releaseLock();
  }
}
