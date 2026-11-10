/**
 * FABBRICA - MOTORE v2.4 (10/11/2026)
 * Codice puro: lo scarica ed esegue (eval) il "lancio" a ogni giro. Usa le globali del lancio FB_BASE e UTENTI
 * ({ '3INF': [[pc, utenteGitHub, 'COGNOME Nome'], ...] }) e i servizi Google. Chiama FB_main_() dopo l'eval.
 * Properties usate: FB_FOGLIO, FB_FATTI, GITHUB_TOKEN (da v1), FB_FORMS, FB_NR, FB_ULTERR (nuove).
 * Changelog: 2.4 modulo GIT (scheda 'Git <CLASSE>' per ogni classe di indice.json "git", elenco dalla scheda 'Utenti <CLASSE>' A=PC B=Utente C=Allievo, una classe per giro, ogni classe al massimo ogni ogni_minuti, Progetto/README/Commit totali); 2.3 modulo CLASSROOM (schede 'Corsi' e 'Consegne <CLASSE>', una classe per giro, mappa in indice.json); 2.2 errori in una sola riga di 'Stato' (Ultimo errore), mai piu righe ERRORE in 'Esiti' (pulite a ogni giro); 2.1 elenco ragazzi letto dalla scheda 'Cruscotto Git <classe>' (UTENTI del lancio puo essere {}); 2.0 tutte le classi, registro Moduli, risultati (schede "Ris <id>"), scheda "Stato", cruscotti per classe.
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
var FB_ERRS = [];
function FB_errore_(ss, passo, e) {
  FB_ERRS.push(passo + ': ' + (e && e.message ? e.message : e));
}

function FB_pulisci_(ss) {
  var sh = ss.getSheetByName('Esiti');
  if (!sh) return;
  var v = sh.getDataRange().getValues(), i = v.length - 1, fine;
  while (i >= 1) {
    if (v[i][1] !== 'ERRORE') { i--; continue; }
    fine = i;
    while (i >= 1 && v[i][1] === 'ERRORE') i--;
    sh.deleteRows(i + 2, fine - i);
  }
}

function FB_ultimoErrore_() {
  if (!FB_ERRS.length) return 'nessuno';
  var t = FB_ERRS.join(' | ');
  if (t.indexOf('autorizzazioni') >= 0) return "Manca un'autorizzazione Google: eseguire installa e consentire";
  return FB_ora_() + ' ' + t;
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
    ['Ultimo errore', FB_ultimoErrore_()]
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

/* ---------- Git e progetti per classe (v2.4) ---------- */
function GT_get_(path) {
  var tok = FB_p_().getProperty('GITHUB_TOKEN');
  var h = { 'Accept': 'application/vnd.github+json', 'User-Agent': 'fabbrica' };
  if (tok) h['Authorization'] = 'Bearer ' + tok;
  try {
    var r = UrlFetchApp.fetch('https://api.github.com/' + path, { headers: h, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null;
    var lk = '';
    try { var hh = r.getHeaders ? r.getHeaders() : {}; lk = String(hh.Link || hh.link || ''); } catch (e1) { lk = ''; }
    return { body: JSON.parse(r.getContentText()), link: lk };
  } catch (e) { return null; }
}
function GT_lista_(path) { var r = GT_get_(path); return r && r.body && r.body.length !== undefined ? r.body : []; }

function GT_riga_(pc, utente, nome, oggi) {
  var repos = GT_lista_('users/' + utente + '/repos?per_page=100&sort=pushed'), sc = null, i;
  for (i = 0; i < repos.length; i++) { if (/master|mastermind/i.test(repos[i].name)) { sc = repos[i]; break; } }
  if (!sc) for (i = 0; i < repos.length; i++) { if ((repos[i].pushed_at || '').slice(0, 10) === oggi) { sc = repos[i]; break; } }
  if (!sc && repos.length) sc = repos[0];
  var d = { repo: '-', push: '-', oggi: 0, tot: 0, prog: 'no', rd: 'no', tag: '-', rel: '-', ult: '-', st: 'ROSSO' };
  if (sc) {
    var full = sc.full_name, bozza = false, hasTag = false, hasRel = false;
    d.repo = sc.name;
    d.push = (sc.pushed_at || '').replace('T', ' ').slice(0, 16) + ' UTC';
    var c = GT_get_('repos/' + full + '/commits?per_page=30'), com = c ? c.body : [];
    for (i = 0; i < com.length; i++) { if (String((com[i].commit.author || {}).date).slice(0, 10) === oggi) d.oggi++; }
    if (com.length) d.ult = String(com[0].commit.message).split('\n')[0].slice(0, 60);
    d.tot = com.length;
    var m = c && /[?&]page=(\d+)>;\s*rel="last"/.exec(c.link);
    if (m) d.tot = '~' + (Number(m[1]) * 30);
    var cont = GT_lista_('repos/' + full + '/contents/'), lz = false, altro = false;
    for (i = 0; i < cont.length; i++) {
      if (/\.(lpi|lpr)$/i.test(cont[i].name)) lz = true;
      if (/^readme/i.test(cont[i].name)) d.rd = 'si';
      altro = true;
    }
    d.prog = lz ? 'Lazarus' : (altro ? 'altro' : 'no');
    if (/master|mastermind/i.test(sc.name)) {
      var tags = GT_lista_('repos/' + full + '/tags?per_page=5'), rel = GT_lista_('repos/' + full + '/releases?per_page=5');
      if (tags.length) { d.tag = tags.map(function (t) { return t.name; }).join(', '); hasTag = true; }
      if (rel.length) { d.rel = (rel[0].name || rel[0].tag_name || 'senza nome') + (rel[0].draft ? ' (bozza)' : ''); bozza = !!rel[0].draft; hasRel = true; }
      if (hasRel && !bozza && hasTag) d.st = 'VERDE';
      else if (hasRel || hasTag) d.st = 'GIALLO';
      else if (d.oggi > 0) d.st = 'ARANCIO';
    } else if (d.oggi > 0) d.st = 'ARANCIO';
  }
  return [d.st, 'PC ' + pc, nome, utente, d.repo, d.push, d.oggi, d.tot, d.prog, d.rd, d.tag, d.rel, d.ult];
}

function GT_elenco_(ss, classe) {
  var sh = ss.getSheetByName('Utenti ' + classe), out = [];
  if (sh) {
    var v = sh.getDataRange().getValues();
    for (var i = 0; i < v.length; i++) {
      var ut = String(v[i][1] || '').trim();
      if (!ut || /^utente/i.test(ut)) continue;
      out.push([String(v[i][0]).replace(/\D/g, '') || '-', ut, String(v[i][2] || '').trim() || '-']);
    }
    return out;
  }
  if (classe === '3INF') return CG_leggiElenco_(ss, classe);
  return null;
}

function GT_scheda_(ss, classe, utenti, t0) {
  var oggi = Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd'), righe = [], errori = 0, i;
  for (i = 0; i < utenti.length; i++) {
    if (Date.now() - t0 > 270000) { FB_errore_(ss, 'Git ' + classe, 'tempo quasi finito, righe parziali'); break; }
    try { righe.push(GT_riga_(utenti[i][0], utenti[i][1], utenti[i][2], oggi)); }
    catch (e) { errori++; righe.push(['ROSSO', 'PC ' + utenti[i][0], utenti[i][2], utenti[i][1], '-', '-', 0, 0, 'no', 'no', '-', '-', 'errore lettura']); }
  }
  if (errori) FB_errore_(ss, 'Git ' + classe, errori + ' righe con errore di lettura');
  var ord = { VERDE: 0, GIALLO: 1, ARANCIO: 2, ROSSO: 3 };
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]]; });
  var sh = ss.getSheetByName('Git ' + classe) || ss.insertSheet('Git ' + classe);
  sh.clear();
  var ora = Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss');
  sh.getRange(1, 1).setValue(classe + ' · Git e progetti · dati letti alle ' + ora).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = release pubblicata con tag · GIALLO = tag o bozza · ARANCIO = commit di oggi · ROSSO = nessuna attività. Tag e release solo per i repository Mastermind. Solo repository pubblici. Commit totali approssimati.');
  var testa = ['Stato', 'PC', 'Allievo', 'Utente GitHub', 'Repository', 'Ultimo push', 'Commit oggi', 'Commit totali', 'Progetto', 'README', 'Tag', 'Release', 'Ultimo commit'];
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}

function FB_git_(ss, indice, t0) {
  var cfg = indice.git;
  if (!cfg || cfg.attivo === false) return;
  var classi = cfg.classi || ['3INF', '4TI', '2INF', '1INF'], ogni = (cfg.ogni_minuti || 10) * 60000;
  var T = FB_json_('GT_T'), ora = Date.now(), fatta = false;
  var dovute = classi.filter(function (c) { return !T[c] || ora - T[c] >= ogni; });
  dovute.sort(function (a, b) { return (T[a] || 0) - (T[b] || 0); });
  dovute.forEach(function (c) {
    try {
      var u = GT_elenco_(ss, c);
      if (!u || !u.length) { FB_ERRS.push('Git ' + c + ': manca la scheda Utenti ' + c); return; }
      if (fatta || Date.now() - t0 > 240000) return;
      GT_scheda_(ss, c, u, t0);
      T[c] = ora; fatta = true; FB_salva_('GT_T', T);
    } catch (e) { FB_errore_(ss, 'Git ' + c, e); }
  });
}

/* ---------- Classroom: consegne per classe (v2.3) ---------- */
function CR_corsi_() {
  var out = [], tok = null, r;
  do {
    r = Classroom.Courses.list({ courseStates: ['ACTIVE'], pageSize: 100, pageToken: tok || undefined });
    out = out.concat(r.courses || []);
    tok = r.nextPageToken || null;
  } while (tok);
  return out;
}
function CR_classe_(nome, mappa) {
  for (var c in mappa) { if (mappa[c] && String(nome).indexOf(mappa[c]) >= 0) return c; }
  return '-';
}
function CR_nome_(s) {
  var n = (s.profile && s.profile.name) || {};
  if (n.familyName && n.givenName) return String(n.familyName).toUpperCase() + ' ' + n.givenName;
  return n.fullName || '(senza nome)';
}
function CR_quiz_(ss, classe, email) {
  var parti = [], c = String(classe).toLowerCase();
  ss.getSheets().forEach(function (sh) {
    var m = /^Ris (.+)$/.exec(sh.getName ? sh.getName() : sh.name);
    if (!m || m[1].toLowerCase().indexOf(c) < 0) return;
    var v = sh.getDataRange().getValues();
    for (var i = 1; i < v.length; i++) {
      if (String(v[i][0]).toLowerCase() === String(email).toLowerCase()) { parti.push(v[i][1] + '/' + v[i][2]); break; }
    }
  });
  return parti.length ? parti.join(' · ') : '-';
}
function CR_scheda_(ss, classe, corso, cfg) {
  var N = cfg.ultimi || 8, id = corso.id, i, j;
  var studenti = [], tok = null, r;
  do {
    r = Classroom.Courses.Students.list(id, { pageSize: 100, pageToken: tok || undefined });
    studenti = studenti.concat(r.students || []); tok = r.nextPageToken || null;
  } while (tok);
  var lavori = [];
  tok = null;
  do {
    r = Classroom.Courses.CourseWork.list(id, { courseWorkStates: ['PUBLISHED'], pageSize: 100, pageToken: tok || undefined });
    lavori = lavori.concat(r.courseWork || []); tok = r.nextPageToken || null;
  } while (tok);
  lavori = lavori.filter(function (w) { return w.workType === 'ASSIGNMENT'; });
  lavori.sort(function (a, b) { return String(b.creationTime) < String(a.creationTime) ? -1 : 1; });
  lavori = lavori.slice(0, N);
  var cons = {};
  lavori.forEach(function (w) {
    var t = null; tok = null;
    do {
      r = Classroom.Courses.CourseWork.StudentSubmissions.list(id, w.id, { pageSize: 100, pageToken: tok || undefined });
      (r.studentSubmissions || []).forEach(function (s) {
        if (s.state === 'TURNED_IN' || s.state === 'RETURNED') (cons[w.id] = cons[w.id] || {})[s.userId] = 1;
      });
      tok = r.nextPageToken || null;
    } while (tok);
  });
  var ord = { ROSSO: 0, ARANCIO: 1, GIALLO: 2, VERDE: 3 };
  var righe = studenti.map(function (s) {
    var m = 0, celle = lavori.map(function (w) {
      if ((cons[w.id] || {})[s.userId]) return 'Consegnato';
      m++; return 'Mancante';
    });
    var st = m === 0 ? 'VERDE' : m === 1 ? 'GIALLO' : m <= 3 ? 'ARANCIO' : 'ROSSO';
    var em = (s.profile && s.profile.emailAddress) || '';
    return [st, CR_nome_(s), em].concat(celle, [lavori.length - m, m, em ? CR_quiz_(ss, classe, em) : '-']);
  });
  righe.sort(function (a, b) { return ord[a[0]] - ord[b[0]] || (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : 0); });
  var nomeSh = 'Consegne ' + classe;
  var sh = ss.getSheetByName(nomeSh) || ss.insertSheet(nomeSh);
  sh.clear();
  sh.getRange(1, 1).setValue(classe + ' · Consegne · dati letti alle ' + Utilities.formatDate(new Date(), 'Europe/Rome', 'HH:mm:ss')).setFontWeight('bold');
  sh.getRange(2, 1).setValue('VERDE = nessun compito mancante · GIALLO = ne manca 1 · ARANCIO = ne mancano 2-3 · ROSSO = 4 o più. Ultimi compiti pubblicati; Consegnato = consegnato o restituito.');
  var testa = ['Stato', 'Allievo', 'Email'];
  lavori.forEach(function (w) {
    var d = String(w.creationTime || '').slice(0, 10).split('-');
    testa.push(String(w.title || '').slice(0, 28) + ' ' + (d.length === 3 ? d[2] + '/' + d[1] : ''));
  });
  testa = testa.concat(['Consegnati', 'Mancanti', 'Quiz migliori']);
  sh.getRange(4, 1, 1, testa.length).setValues([testa]).setFontWeight('bold').setBackground('#e8eef9');
  if (righe.length) sh.getRange(5, 1, righe.length, testa.length).setValues(righe);
  var col = { VERDE: '#a5d6a7', GIALLO: '#fff59d', ARANCIO: '#ffcc80', ROSSO: '#ef9a9a' };
  for (i = 0; i < righe.length; i++) sh.getRange(5 + i, 1).setBackground(col[righe[i][0]]).setFontWeight('bold');
}
function FB_classroom_(ss, indice, t0) {
  var cfg = indice.classroom;
  if (!cfg || cfg.attivo === false) return;
  if (typeof Classroom === 'undefined') { FB_ERRS.push('Classroom non abilitato: aggiungere il servizio Classroom API in Apps Script'); return; }
  if (Date.now() - t0 > 240000) return;
  var corsi = CR_corsi_(), mappa = cfg.classi || {}, trovati = {}, ordine = [];
  var ts = Number(FB_p_().getProperty('FB_CORSI_T') || 0);
  if (Date.now() - ts >= 600000 || !ss.getSheetByName('Corsi')) {
    var sc = ss.getSheetByName('Corsi') || ss.insertSheet('Corsi');
    sc.clear();
    sc.getRange(1, 1, 1, 3).setValues([['Nome', 'Id', 'Classe']]).setFontWeight('bold');
    var rr = corsi.map(function (c) { return [c.name, c.id, CR_classe_(c.name, mappa)]; });
    if (rr.length) sc.getRange(2, 1, rr.length, 3).setValues(rr);
    FB_p_().setProperty('FB_CORSI_T', String(Date.now()));
  }
  corsi.forEach(function (c) { var k = CR_classe_(c.name, mappa); if (k !== '-' && !trovati[k]) trovati[k] = c; });
  for (var k in mappa) if (trovati[k]) ordine.push(k);
  if (!ordine.length) return;
  var cl = ordine[Math.floor(new Date().getMinutes() / 1) % ordine.length];
  CR_scheda_(ss, cl, trovati[cl], cfg);
}

/* ---------- Giro principale ---------- */
function FB_main_() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var t0 = Date.now();
    FB_ERRS = [];
    var ss = FB_foglio_(), indice = { lavori: [] };
    try { FB_pulisci_(ss); } catch (e) { FB_errore_(ss, 'pulizia', e); }
    try { indice = JSON.parse(FB_get_(FB_BASE + 'indice.json')); } catch (e) { FB_errore_(ss, 'indice', e); indice = null; }
    if (indice) {
      try { FB_nuovi_(ss, indice); } catch (e) { FB_errore_(ss, 'nuovi', e); }
    }
    try { FB_ripara_(ss); } catch (e) { FB_errore_(ss, 'ripara', e); }
    try { FB_risultati_(ss, t0); } catch (e) { FB_errore_(ss, 'risultati', e); }
    if (indice) {
      try { FB_cruscotti_(ss, indice); } catch (e) { FB_errore_(ss, 'cruscotti', e); }
    }
    if (indice) {
      try { FB_classroom_(ss, indice, t0); } catch (e) { FB_errore_(ss, 'classroom', e); }
    }
    if (indice) {
      try { FB_git_(ss, indice, t0); } catch (e) { FB_errore_(ss, 'git', e); }
    }
    try { FB_stato_(ss); } catch (e) { Logger.log('stato: ' + e); }
  } finally {
    lock.releaseLock();
  }
}
