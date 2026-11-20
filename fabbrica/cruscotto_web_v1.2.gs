/**
 * CRUSCOTTO WEB (tempo reale) - Apps Script v1.2 (20/11/2026) - sostituisce la v1.1 (cruscotto_web.gs, resta in cartella)
 * File da incollare come file SEPARATO (nome: cruscotto_web) nello STESSO progetto Apps Script del motore Fabbrica
 * (account PIAMARTA, il progetto che ha le funzioni ciclo/installa del lancio). Non tocca motore.js ne il lancio.
 *
 * NOVITA DELLA v1.2 (richiesta del docente 20/11/2026: «una singola attivita, per tutte le classi, ore e materie in laboratorio con me»)
 *  1) JOB CONSAPEVOLE DELL'ORARIO. Legge fabbrica/orario-live.json (raw GitHub, cache 5 minuti, come indice.json; si genera da
 *     orario/settimana-AAAA-MM-GG.md con strumenti/orario_live_da_md.py). In ogni giro lavora SOLO sulle classi che hanno lezione con il
 *     docente nell'ora in corso (ora n = 07+n:00 - 08+n:00; da 5 minuti prima dell'inizio); se sono due, tutte e due (prima la piu vecchia).
 *     Fuori lezione (ore libere, prima e dopo) lavora solo sulla classe dell'ora precedente (fino a 2 ore dopo) e su quella dell'ora
 *     successiva (da 1 ora prima), e solo se il suo dato ha piu di 8 minuti: cosi chiude i dati senza consumare quota.
 *     Se l'orario non si legge (rete, file rotto, settimana scaduta) RICADE sul comportamento della v1.1 (tutte le classi, o quelle di
 *     LV_CLASSI, la piu vecchia per prima) e lo scrive nell'avviso di ogni scheda Live («orario non letto: ...»).
 *     La proprieta LV_CLASSI non serve piu con l'orario letto: conta solo nella modalita di riserva.
 *  2) TUTTI I CORSI E TUTTE LE MATERIE. Legge TUTTI i corsi Classroom della classe nella scheda Corsi (una riga per corso con la colonna
 *     Classe; piu righe per la stessa classe = piu corsi, gli iscritti si uniscono per userId); proprieta facoltativa LV_CORSI_EXTRA
 *     («2INF:123456789;3INF:987654321») per aggiungere corsi che la scheda Corsi segna con «-». Un compito e di oggi se la data GG/MM
 *     e in QUALUNQUE punto del titolo («20/11 Ora 4: ...», «11/11 Ore 4-5: ...», «17/11 PROGETTO», «Entrare nell'organizzazione 18/11»);
 *     senza data nel titolo, se e stato CREATO oggi. Ogni compito e quiz porta la MATERIA (dall'orario: il compito «Ora N» e dell'ora N
 *     di oggi; il quiz con «sic» nell'id o «Sicurezza» nel titolo e Sicurezza professionale) e il nome del corso se la classe ne ha piu di uno.
 *  3) La scheda Live ha in C2 il contesto (modo orario o riserva, ruolo lezione o vicina, ora, materia) e il web app lo restituisce in «contesto».
 *
 * COSA FA (come la v1.1, due parti)
 *  A) JOB LEGGERO live_giro(): trigger a tempo ogni 1 minuto (si crea una volta con live_installa()). Legge SOLO
 *     - i compiti di Classroom della classe con titolo «GG/MM Ora N» di OGGI (stato di ogni allievo) e
 *     - le risposte dei Moduli dei quiz di OGGI (chi ha risposto)
 *     e scrive una scheda piccola «Live <CLASSE>» nel foglio Fabbrica (solo «Nome I.», mai email, mai voti).
 *     Non legge storico, Documenti, Git, Situazione, ecc.: quelle restano al motore (giro lungo, ogni qualche minuto).
 *  B) WEB APP doGet(e): ?classe=1inf|2inf|3inf|4ti  -> JSON letto SOLO dalla scheda «Live <CLASSE>» (risponde in meno di 2 s).
 *     Con &callback=nome risponde in JSONP (riserva se il browser blocca il fetch tra domini).
 *
 *  C) BLOCCO RISERVATO CIFRATO (v1.1, solo se la proprieta script LV_CHIAVE esiste): la percentuale di ogni quiz di oggi per allievo (serve alla pagina per
 *     il voto proposto, CRUSCOTTO-DAL-VIVO.md par. 05 punto 0) e' scritta nel JSON SOLO cifrata con AES-256-GCM, stesso formato di strumenti/cifra_json.py
 *     ({cifrato, salt, iter, iv, ct}); la pagina la decifra nel browser con il codice del docente. LV_CHIAVE = chiave AES di 32 byte in base64, GIA derivata
 *     dal codice (PBKDF2-SHA256, salt «cruscotto-docente-v1», 150000 giri) dalla pagina docs/live/chiave.html: il docente la incolla nelle proprieta script.
 *     Il codice NON sta mai ne qui ne in chat. Senza LV_CHIAVE il JSON ha riservato = null e nessuna percentuale esce dal foglio.
 *     La cifratura AES-GCM e scritta qui in JavaScript puro (Apps Script non ha AES) ed e provata contro il modulo crypto di Node (test_aes_gcm.js).
 *
 * CALCOLO DEL TEMPO DEL JOB (stima, NON provata su Google: da verificare con live_prova(), il log dice la durata vera)
 *  per classe: elenco iscritti (1 chiamata, in cache 20 min) ~1 s + elenco compiti (1 chiamata) ~1 s
 *              + consegne di ogni compito di oggi (1 chiamata ciascuno, 3-4 compiti) ~1-2 s l'una = 4-8 s
 *              + per ogni quiz di oggi FormApp.openById + getResponses ~1-3 s (2-5 quiz) = 3-12 s
 *              + lettura Esiti/Corsi/Abbinamenti + scrittura della scheda Live ~2 s
 *       => circa 10-25 s per classe. Il job non INIZIA una classe dopo 30 s dall'avvio e si ferma a 50 s: sotto il minuto.
 *  v1.2: con l'orario letto di norma lavora UNA classe per giro (due se il docente ha due classi nella stessa ora, o a cavallo di due ore dalle
 *  5 minuti prima), quindi il dato di ogni classe in lezione e rifatto a ogni giro. Per le classi in lezione il job inizia comunque la seconda
 *  classe solo entro 30 s dall'avvio; se non ce la fa, il dato di quella classe e quello del giro prima e nel giro dopo ha la precedenza
 *  (la piu vecchia per prima): nessuna resta indietro piu di 2 minuti. Nella modalita di riserva (orario non letto) vale ancora il vecchio
 *  comportamento con 4 classi e LV_CLASSI.
 *  QUOTA: una classe in lezione per giro, 6 ore al giorno = fino a circa 90 minuti di tempo di trigger al giorno (NON provato se la quota
 *  dell'account PIAMARTA lo consente: vedi LIMITI NOTI).
 *
 * LIMITI NOTI
 *  - Quota Apps Script: il tempo totale dei trigger al giorno e limitato (di norma 90 min per account normali, 6 ore Workspace;
 *    NON provato quale vale per l'account PIAMARTA). Per questo il job esce subito fuori dall'orario (lun-ven 07:45-14:20, Roma).
 *  - I compiti si riconoscono dalla data GG/MM nel titolo (anche senza «Ora N») o, senza data, dalla data di creazione di oggi. Il motore
 *    (Consegne) usa ancora solo «GG/MM Ora N»: le due letture possono quindi differire per titoli come «17/11 PROGETTO».
 *  - La materia dei compiti viene dall'ORARIO (ora N del titolo = ora N di oggi). Se il compito dice «Ora 3» ma e stato dato in un'ora che
 *    secondo l'orario non e di quella classe, la materia resta vuota (non si inventa). I quiz di Sicurezza hanno numeri di ora propri del corso
 *    (5, 6A, 7): la materia e Sicurezza professionale dal nome, non dall'ora.
 *  - I quiz di oggi = lavori di fabbrica/indice.json (o Esiti) il cui id contiene GGMM di oggi (es. quiz-1inf-2011-ora4) o il cui
 *    titolo contiene GG/MM di oggi; le versioni dello stesso quiz si uniscono SOLO se indice.json ha il campo «versioni».
 *  - Usa LockService.getUserLock(): il motore usa getScriptLock(), quindi i due non si bloccano a vicenda.
 *
 * R1: nel JSON e nella scheda Live: solo «Nome I.» (stesso algoritmo del motore, SM_brevi_), mai email, cognomi, note, voti.
 * R7: se qualcosa non si legge, la scheda dice stato «non_letto» o «parziale» con il motivo; niente numeri inventati.
 * Nomi: tutte le funzioni e variabili globali hanno prefisso LV_ / live_ e doGet esiste solo qui (il motore non ha doGet;
 * il codice del motore gira dentro eval in ciclo(), quindi non ci sono conflitti di nomi).
 */

var LV_VERSIONE = '1.2';
var LV_CLASSI_TUTTE = ['1INF', '2INF', '3INF', '4TI'];
var LV_AVVIO_MAX_MS = 30000;   // dopo 30 s dall'avvio non si inizia un'altra classe
var LV_FINE_MS = 50000;        // a 50 s si smette di leggere e si scrive quello che c'e (stato «parziale»)
var LV_META = 8;               // righe prima dei dati: 1..7 intestazioni, 8 = testata colonne, dati dalla 9
var LV_BASE_DEFAULT = 'https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/fabbrica/';
var LV_ANTICIPO_MIN = 5;       // una classe e «in lezione» da 5 minuti prima dell'inizio dell'ora (dato fresco dal primo minuto)
var LV_CHIUSURA_MIN = 120;     // la classe dell'ora precedente si chiude (ogni 8 minuti) per le 2 ore dopo la fine della sua lezione
var LV_SUCCESSIVA_MIN = 60;    // la classe dell'ora successiva si prepara (ogni 8 minuti) nell'ora prima dell'inizio
var LV_VICINE_OGNI_S = 480;    // fuori lezione una classe si rilegge solo se il suo dato ha piu di 8 minuti (la pagina tollera 11)
var LV_GG = ['', 'lun', 'mar', 'mer', 'gio', 'ven', 'sab', 'dom'];   // indice = giorno ISO (u: 1 = lunedi)

/* ---------- servizi di base ---------- */
function LV_roma_(d, f) { return Utilities.formatDate(d || new Date(), 'Europe/Rome', f); }
function LV_iso_(d) { return LV_roma_(d, "yyyy-MM-dd'T'HH:mm:ssXXX"); }

function LV_foglio_() {
  var p = PropertiesService.getScriptProperties(), id = p.getProperty('FB_FOGLIO');
  if (id) return SpreadsheetApp.openById(id);
  try { var a = SpreadsheetApp.getActive(); if (a) return a; } catch (e) { }
  var it = DriveApp.getFilesByName('Fabbrica (10/11/2026)');
  if (it.hasNext()) return SpreadsheetApp.open(it.next());
  throw new Error('foglio Fabbrica non trovato (manca la proprieta FB_FOGLIO)');
}

/* ---------- «Nome I.»: stesso algoritmo del motore (SM_brevi_), copiato qui perche il motore gira in eval ---------- */
var LV_PART_ = { DE: 1, DI: 1, DA: 1, DEL: 1, DELLA: 1, DEI: 1, DEGLI: 1, DAL: 1, DALLA: 1, DALL: 1, DELLE: 1, LO: 1, LA: 1, LE: 1, EL: 1, AL: 1, BEN: 1, BIN: 1, BEL: 1, ABD: 1, ABDEL: 1, ABDUL: 1, ABU: 1, ABOU: 1, OULD: 1, VAN: 1, VON: 1, DOS: 1, DAS: 1, DU: 1, SAN: 1, SANTA: 1, MAC: 1, MC: 1 };
function LV_cap_(w) { return String(w || '').toLowerCase().replace(/(^|[-'’\s])([a-zà-ÿ])/g, function (m, a, b) { return a + b.toUpperCase(); }); }
function LV_tuttoMai_(t) { return t === t.toUpperCase() && t !== t.toLowerCase(); }
function LV_parti_(s, k) {
  s = String(s || '').replace(/\s+/g, ' ').trim();
  if (s.indexOf('@') > 0) return { nome: 'Allievo ' + (k + 1), cog: '' };   // mai un'email in uscita
  var p = s.split(' ').filter(function (x) { return x; });
  if (p.length < 2) return { nome: p.length ? LV_cap_(p[0]) : 'Allievo ' + (k + 1), cog: '' };
  var nc = 0;
  while (nc < p.length && LV_tuttoMai_(p[nc])) nc++;
  if (nc === 0 || nc === p.length) {
    nc = 0;
    while (nc < p.length - 2 && LV_PART_[p[nc].toUpperCase().replace(/[.']/g, '')]) nc++;
    nc++;
    if (p.length - nc >= 2) nc = p.length - 1;
  }
  return { nome: p.slice(nc).map(LV_cap_).join(' '), cog: p.slice(0, nc).join(' ').toUpperCase() };
}
function LV_brevi_(nomi) {
  var pt = nomi.map(function (n, k) { return LV_parti_(n, k); }), lab = [], i, L;
  function etichetta(p, n) {
    var sl = String(p.cog || '').toUpperCase().replace(/[^A-ZÀ-Ý]/g, '');
    if (!sl) return p.nome;
    return p.nome + ' ' + sl.charAt(0) + sl.slice(1, n).toLowerCase() + '.';
  }
  for (i = 0; i < pt.length; i++) lab.push(etichetta(pt[i], 1));
  for (L = 2; L <= 4; L++) {
    var conta = {};
    lab.forEach(function (x) { conta[x.toUpperCase()] = (conta[x.toUpperCase()] || 0) + 1; });
    for (i = 0; i < lab.length; i++) if (conta[lab[i].toUpperCase()] > 1) lab[i] = etichetta(pt[i], L);
  }
  var vis = {};
  for (i = 0; i < lab.length; i++) {
    var u = lab[i].toUpperCase();
    if (vis[u]) { vis[u]++; lab[i] = lab[i] + ' (' + vis[u] + ')'; } else vis[u] = 1;
  }
  return lab;
}

/* ---------- Classroom ---------- */
/* TUTTI i corsi Classroom della classe: righe della scheda Corsi con la colonna Classe uguale (Nome, Id, Classe) + proprieta LV_CORSI_EXTRA */
function LV_corsi_(ss, classe) {
  var out = [], visti = {}, sh = ss.getSheetByName('Corsi'), i;
  function aggiungi(id, nome) { id = String(id).replace(/\.0+$/, ''); if (!id || visti[id]) return; visti[id] = 1; out.push({ id: id, nome: String(nome || id) }); }
  if (sh) {
    var v = sh.getDataRange().getValues();
    for (i = 1; i < v.length; i++) if (String(v[i][2]).toUpperCase() === classe && v[i][1] !== '') aggiungi(v[i][1], v[i][0]);
  }
  var ex = PropertiesService.getScriptProperties().getProperty('LV_CORSI_EXTRA') || '';
  ex.split(/[;\s]+/).forEach(function (x) {
    var m = /^([A-Za-z0-9]+)\s*[:=]\s*(\d+)$/.exec(x);
    if (m && m[1].toUpperCase() === classe) aggiungi(m[2], 'corso ' + m[2]);
  });
  return out;
}
function LV_iscritti_(corsoId, classe) {
  var cache = CacheService.getScriptCache(), k = 'LV_R_' + classe + '_' + corsoId, c = cache.get(k);
  if (c) { try { return JSON.parse(c); } catch (e) { } }
  var out = [], tok = null, r;
  do {
    r = Classroom.Courses.Students.list(corsoId, { pageSize: 100, pageToken: tok || undefined });
    (r.students || []).forEach(function (s) {
      var n = (s.profile && s.profile.name) || {};
      out.push({ u: s.userId, e: String((s.profile && s.profile.emailAddress) || '').toLowerCase(), c: n.familyName || '', n: n.givenName || '', f: n.fullName || '' });
    });
    tok = r.nextPageToken || null;
  } while (tok);
  try { cache.put(k, JSON.stringify(out), 1200); } catch (e) { }
  return out;
}
function LV_nomeCR_(s) { return (s.c && s.n) ? String(s.c).toUpperCase() + ' ' + s.n : (s.f || '(senza nome)'); }
function LV_statoSub_(s) {   // come CR_statoSub_ del motore
  if (s.state === 'RETURNED') return 'RICONSEGNATO';
  if (s.state === 'TURNED_IN') {
    var h = s.submissionHistory || [];
    for (var i = 0; i < h.length; i++) if (h[i] && h[i].stateHistory && h[i].stateHistory.state === 'RETURNED') return 'RICONSEGNATO';
    return 'CONSEGNATO';
  }
  return 'ASSEGNATO';
}
/* un compito e di oggi se la data GG/MM e in un punto qualunque del titolo; senza data nel titolo, se e stato creato oggi.
   ora: 0 se il titolo non dice «Ora N» / «Ore N-M» (v1.1 scartava questi compiti). */
var LV_RE_DATA = /(^|\D)(\d{1,2})\s*\/\s*(\d{1,2})(?=\D|$)/;
var LV_RE_ORA = /(^|\W)Or[ae]\s*(\d)/i;
function LV_titolo_(t, w, gg, mm, giorno) {   // -> {oggi: bool, ora: n} oppure null
  t = String(t || '');
  var d = LV_RE_DATA.exec(t), oggi;
  if (d) oggi = Number(d[2]) === gg && Number(d[3]) === mm;
  else {
    var ct = Date.parse(w && w.creationTime || '');
    oggi = !isNaN(ct) && LV_roma_(new Date(ct), 'yyyy-MM-dd') === giorno;
  }
  if (!oggi) return null;
  var o = LV_RE_ORA.exec(t);
  return { oggi: true, ora: o ? Number(o[2]) : 0 };
}
function LV_compitiOggi_(corsoId, gg, mm, giorno) {
  var r = Classroom.Courses.CourseWork.list(corsoId, { courseWorkStates: ['PUBLISHED'], orderBy: 'updateTime desc', pageSize: 30 });
  var out = [];
  (r.courseWork || []).forEach(function (w) {
    var m = LV_titolo_(w.title, w, gg, mm, giorno);
    if (m) out.push({ id: w.id, titolo: String(w.title), ora: m.ora, link: w.alternateLink || '' });
  });
  out.sort(function (a, b) { return a.ora - b.ora; });
  return out;
}
function LV_consegne_(corsoId, wid) {
  var out = {}, tok = null, r;
  do {
    r = Classroom.Courses.CourseWork.StudentSubmissions.list(corsoId, wid, { pageSize: 100, pageToken: tok || undefined });
    (r.studentSubmissions || []).forEach(function (s) { out[s.userId] = { stato: LV_statoSub_(s), t: s.updateTime || '' }; });
    tok = r.nextPageToken || null;
  } while (tok);
  return out;
}

/* ---------- quiz di oggi ---------- */
function LV_indice_() {
  var cache = CacheService.getScriptCache(), c = cache.get('LV_INDICE');
  if (c) { try { return JSON.parse(c); } catch (e) { } }
  var base = (typeof FB_BASE !== 'undefined') ? FB_BASE : LV_BASE_DEFAULT;
  var r = UrlFetchApp.fetch(base + 'indice.json?t=' + Date.now(), { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('indice.json HTTP ' + r.getResponseCode());
  var t = r.getContentText();
  var d = JSON.parse(t), min = { lavori: (d.lavori || []).map(function (l) { return { id: l.id, versioni: l.versioni || [] }; }) };
  try { cache.put('LV_INDICE', JSON.stringify(min), 300); } catch (e) { }
  return min;
}
function LV_esiti_(ss) {   // id -> {titolo, link, classe, formId}
  var sh = ss.getSheetByName('Esiti'), out = {};
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][1]) out[String(v[i][1])] = { titolo: String(v[i][2] || ''), link: String(v[i][3] || ''), classe: String(v[i][6] || '').toUpperCase(), formId: String(v[i][7] || '') };
  return out;
}
/* quiz attivi di oggi per la classe: [{id, titolo, link, ids:[id attivo + versioni con Moduli creato]}] */
function LV_quizOggi_(ss, classe, gg, mm) {
  var esiti = LV_esiti_(ss), ind = LV_indice_(), gm = (gg < 10 ? '0' : '') + gg + (mm < 10 ? '0' : '') + mm;
  var reId = new RegExp('(^|-)' + gm + '(-|$)'), reTit = new RegExp('(^|\\D)0?' + gg + '\\s*/\\s*0?' + mm + '(\\D|$)');
  var assorbiti = {};
  ind.lavori.forEach(function (l) { (l.versioni || []).forEach(function (v) { if (v !== l.id) assorbiti[v] = 1; }); });
  var out = [];
  ind.lavori.forEach(function (l) {
    var e = esiti[l.id];
    if (!e || e.classe !== classe || assorbiti[l.id]) return;
    if (!(reId.test(l.id) || reTit.test(e.titolo))) return;
    var ids = (l.versioni && l.versioni.length ? l.versioni.slice() : []);
    if (ids.indexOf(l.id) < 0) ids.push(l.id);
    ids = ids.filter(function (x) { return esiti[x] && esiti[x].formId; });
    if (ids.length) out.push({ id: l.id, titolo: e.titolo, link: e.link, ids: ids, forms: ids.map(function (x) { return esiti[x].formId; }) });
  });
  return out;
}
function LV_abbinamenti_(ss, classe) {   // email -> 'COGNOME Nome' (scheda Abbinamenti, solo uso interno)
  var sh = ss.getSheetByName('Abbinamenti ' + classe), out = {};
  if (!sh) return out;
  var v = sh.getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][0] && v[i][1] && String(v[i][1]) !== '-') out[String(v[i][0]).toLowerCase()] = String(v[i][1]).toUpperCase();
  return out;
}

/* ---------- AES-256-GCM in JavaScript puro (Apps Script non ha AES). Provato contro Node crypto: report/2026-11-20/prova-live/test_aes_gcm.js ---------- */
var LV_SB_ = null;
function LV_aesInit_() {
  if (LV_SB_) return;
  var sb = new Array(256), p = 1, q = 1;
  do {
    p = (p ^ ((p << 1) & 0xff) ^ ((p & 0x80) ? 0x1b : 0)) & 0xff;
    q ^= (q << 1) & 0xff; q ^= (q << 2) & 0xff; q ^= (q << 4) & 0xff; if (q & 0x80) q ^= 0x09; q &= 0xff;
    var x = q ^ (((q << 1) | (q >> 7)) & 0xff) ^ (((q << 2) | (q >> 6)) & 0xff) ^ (((q << 3) | (q >> 5)) & 0xff) ^ (((q << 4) | (q >> 4)) & 0xff);
    sb[p] = (x ^ 0x63) & 0xff;
  } while (p !== 1);
  sb[0] = 0x63; LV_SB_ = sb;
}
function LV_xt_(a) { return ((a << 1) ^ ((a & 0x80) ? 0x1b : 0)) & 0xff; }
function LV_aesChiave_(key) {   // key: 32 byte -> 15 round key da 16 byte
  LV_aesInit_();
  var w = [], i, t, rc = 1, Nk = 8, Nr = 14;
  for (i = 0; i < Nk; i++) w.push([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]);
  for (i = Nk; i < 4 * (Nr + 1); i++) {
    t = w[i - 1].slice();
    if (i % Nk === 0) { t = [LV_SB_[t[1]] ^ rc, LV_SB_[t[2]], LV_SB_[t[3]], LV_SB_[t[0]]]; rc = LV_xt_(rc); }
    else if (i % Nk === 4) t = [LV_SB_[t[0]], LV_SB_[t[1]], LV_SB_[t[2]], LV_SB_[t[3]]];
    w.push([w[i - Nk][0] ^ t[0], w[i - Nk][1] ^ t[1], w[i - Nk][2] ^ t[2], w[i - Nk][3] ^ t[3]]);
  }
  var rk = [];
  for (var r = 0; r <= Nr; r++) { var b = []; for (var c = 0; c < 4; c++) b = b.concat(w[4 * r + c]); rk.push(b); }
  return rk;
}
function LV_aesBlocco_(rk, inp) {
  var s = inp.slice(), r, i, Nr = rk.length - 1, t;
  for (i = 0; i < 16; i++) s[i] ^= rk[0][i];
  for (r = 1; r <= Nr; r++) {
    for (i = 0; i < 16; i++) s[i] = LV_SB_[s[i]];
    t = [s[0], s[5], s[10], s[15], s[4], s[9], s[14], s[3], s[8], s[13], s[2], s[7], s[12], s[1], s[6], s[11]];   // ShiftRows
    if (r < Nr) {
      for (var c = 0; c < 4; c++) {
        var a0 = t[4 * c], a1 = t[4 * c + 1], a2 = t[4 * c + 2], a3 = t[4 * c + 3];
        s[4 * c] = LV_xt_(a0) ^ (LV_xt_(a1) ^ a1) ^ a2 ^ a3;
        s[4 * c + 1] = a0 ^ LV_xt_(a1) ^ (LV_xt_(a2) ^ a2) ^ a3;
        s[4 * c + 2] = a0 ^ a1 ^ LV_xt_(a2) ^ (LV_xt_(a3) ^ a3);
        s[4 * c + 3] = (LV_xt_(a0) ^ a0) ^ a1 ^ a2 ^ LV_xt_(a3);
      }
    } else s = t;
    for (i = 0; i < 16; i++) s[i] ^= rk[r][i];
  }
  return s;
}
function LV_gfMul_(X, Y) {
  var Z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], V = Y.slice(), i, j;
  for (i = 0; i < 128; i++) {
    if ((X[i >> 3] >> (7 - (i & 7))) & 1) for (j = 0; j < 16; j++) Z[j] ^= V[j];
    var lsb = V[15] & 1;
    for (j = 15; j > 0; j--) V[j] = ((V[j] >> 1) | ((V[j - 1] & 1) << 7)) & 0xff;
    V[0] = V[0] >> 1;
    if (lsb) V[0] ^= 0xe1;
  }
  return Z;
}
/** key 32 byte, iv 12 byte, dati: array di byte (0-255). Restituisce testo cifrato + tag di 16 byte (come cryptography AESGCM e WebCrypto). */
function LV_aesGcm_(key, iv, dati) {
  var rk = LV_aesChiave_(key), H = LV_aesBlocco_(rk, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), out = [], i, j, n = dati.length;
  var ctr = iv.concat([0, 0, 0, 1]), J0 = ctr.slice();
  for (i = 0; i < n; i += 16) {
    for (j = 15; j >= 12; j--) { ctr[j] = (ctr[j] + 1) & 0xff; if (ctr[j] !== 0) break; }
    var ks = LV_aesBlocco_(rk, ctr);
    for (j = 0; j < 16 && i + j < n; j++) out.push(dati[i + j] ^ ks[j]);
  }
  var Y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (i = 0; i < out.length; i += 16) {
    var blk = out.slice(i, i + 16); while (blk.length < 16) blk.push(0);
    for (j = 0; j < 16; j++) Y[j] ^= blk[j];
    Y = LV_gfMul_(Y, H);
  }
  var bits = out.length * 8, lenBlk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (bits >>> 24) & 0xff, (bits >>> 16) & 0xff, (bits >>> 8) & 0xff, bits & 0xff];
  for (j = 0; j < 16; j++) Y[j] ^= lenBlk[j];
  Y = LV_gfMul_(Y, H);
  var ek = LV_aesBlocco_(rk, J0), tag = [];
  for (j = 0; j < 16; j++) tag.push(Y[j] ^ ek[j]);
  return out.concat(tag);
}
function LV_utf8_(s) {
  var e = unescape(encodeURIComponent(s)), b = [];
  for (var i = 0; i < e.length; i++) b.push(e.charCodeAt(i));
  return b;
}
function LV_b64_(bytes) { return Utilities.base64Encode(bytes.map(function (x) { return x > 127 ? x - 256 : x; })); }
function LV_b64dec_(s) { return Utilities.base64Decode(s).map(function (x) { return x & 0xff; }); }
function LV_cifra_(obj, chiaveB64) {
  var key = LV_b64dec_(chiaveB64);
  if (key.length !== 32) throw new Error('LV_CHIAVE non e di 32 byte');
  var u = Utilities.getUuid().replace(/-/g, ''), iv = [];
  for (var i = 0; i < 12; i++) iv.push(parseInt(u.substr(2 * i, 2), 16));
  var ct = LV_aesGcm_(key, iv, LV_utf8_(JSON.stringify(obj)));
  return { cifrato: 1, salt: 'Y3J1c2NvdHRvLWRvY2VudGUtdjE=', iter: 150000, iv: LV_b64_(iv), ct: LV_b64_(ct) };
}
function LV_puntiTotali_(form) {   // come FB_puntiTotali_ del motore
  var tot = 0, T = FormApp.ItemType;
  form.getItems().forEach(function (it) {
    try {
      var tp = it.getType(), x = null;
      if (tp === T.CHECKBOX) x = it.asCheckboxItem();
      else if (tp === T.MULTIPLE_CHOICE) x = it.asMultipleChoiceItem();
      else if (tp === T.TEXT) x = it.asTextItem();
      else if (tp === T.PARAGRAPH_TEXT) x = it.asParagraphTextItem();
      if (x) tot += Number(x.getPoints()) || 0;
    } catch (e) { }
  });
  return tot;
}
function LV_punteggio_(r) { var s = 0; (r.getGradableItemResponses() || []).forEach(function (g) { s += Number(g.getScore()) || 0; }); return s; }

/* ---------- ORARIO (v1.2): fabbrica/orario-live.json ---------- */
/* Il file: {valido_dal, valido_al, fonte, giorni: {lun..ven: {ora_1..ora_6: {classe, materia, tipo}}}}; ora libera = chiave assente. */
function LV_orarioLeggi_(giorno) {   // -> {ok, errore, orario, fonte}
  var t = '';
  try {
    var cache = CacheService.getScriptCache(), c = cache.get('LV_ORARIO');
    if (c) t = c;
    else {
      var base = (typeof FB_BASE !== 'undefined') ? FB_BASE : LV_BASE_DEFAULT;
      var r = UrlFetchApp.fetch(base + 'orario-live.json?t=' + Date.now(), { muteHttpExceptions: true });
      if (r.getResponseCode() !== 200) return { ok: false, errore: 'orario-live.json HTTP ' + r.getResponseCode() };
      t = r.getContentText();
      JSON.parse(t);
      try { cache.put('LV_ORARIO', t, 300); } catch (e) { }
    }
    var o = JSON.parse(t), er = LV_orarioControlla_(o, giorno);
    return er ? { ok: false, errore: er } : { ok: true, errore: '', orario: o, fonte: String(o.fonte || '') };
  } catch (e) { return { ok: false, errore: 'orario-live.json non leggibile: ' + String(e.message || e).slice(0, 100) }; }
}
function LV_orarioControlla_(o, giorno) {   // '' se usabile oggi, altrimenti il motivo
  if (!o || typeof o !== 'object' || !o.giorni || typeof o.giorni !== 'object') return 'file senza «giorni»';
  if (!/^\d{4}-\d\d-\d\d$/.test(String(o.valido_dal || '')) || !/^\d{4}-\d\d-\d\d$/.test(String(o.valido_al || ''))) return 'file senza date di validita';
  if (giorno < o.valido_dal || giorno > o.valido_al) return 'orario valido dal ' + o.valido_dal + ' al ' + o.valido_al + ': oggi (' + giorno + ') e fuori, serve l\'orario nuovo';
  return '';
}
function LV_orarioElenco_(g, n) {   // lezioni della n-esima ora del giorno g (un oggetto, oppure un elenco se il docente ha DUE classi nella stessa ora), solo classi nostre
  var v = g && g['ora_' + n], out = [];
  if (!v) return out;
  (Object.prototype.toString.call(v) === '[object Array]' ? v : [v]).forEach(function (e) {
    var k = String((e && e.classe) || '').toUpperCase();
    if (LV_CLASSI_TUTTE.indexOf(k) >= 0) out.push({ classe: k, ora: n, materia: String(e.materia || ''), tipo: String(e.tipo || '') });
  });
  return out;
}
function LV_orarioOra_(g, n) { var l = LV_orarioElenco_(g, n); return l.length ? l[0] : null; }
/** u = giorno ISO (1 lun .. 7 dom), min = minuti dalla mezzanotte (ora di Roma).
 *  -> {lezione: [{classe, ora, materia, tipo, anticipo}], prec: {...}|null, succ: {...}|null}
 *  lezione = classi con ora in corso (o che comincia entro LV_ANTICIPO_MIN); prec/succ solo se non c'e nessuna lezione. */
function LV_piano_(o, u, min) {
  var g = (o && o.giorni && o.giorni[LV_GG[u]]) || {}, lez = {}, ordine = [], n, e, ini, fin;
  for (n = 1; n <= 6; n++) {
    ini = (7 + n) * 60; fin = (8 + n) * 60;
    if (!(min >= ini - LV_ANTICIPO_MIN && min < fin)) continue;
    LV_orarioElenco_(g, n).forEach(function (e) {
      e.anticipo = min < ini;
      if (!lez[e.classe]) { lez[e.classe] = e; ordine.push(e.classe); }
      else if (lez[e.classe].anticipo && !e.anticipo) lez[e.classe] = e;
    });
  }
  var out = { lezione: ordine.map(function (k) { return lez[k]; }), prec: null, succ: null };
  if (out.lezione.length) return out;
  for (n = 6; n >= 1; n--) { e = LV_orarioOra_(g, n); if (e && (8 + n) * 60 <= min && min - (8 + n) * 60 <= LV_CHIUSURA_MIN) { out.prec = e; break; } }
  for (n = 1; n <= 6; n++) { e = LV_orarioOra_(g, n); if (e && (7 + n) * 60 - LV_ANTICIPO_MIN > min && (7 + n) * 60 - min <= LV_SUCCESSIVA_MIN) { out.succ = e; break; } }
  return out;
}
function LV_oreClasse_(o, u, classe) {   // {n: {materia, tipo}} le ore di oggi in cui la classe ha lezione con il docente
  var g = (o && o.giorni && o.giorni[LV_GG[u]]) || {}, out = {}, n, e;
  for (n = 1; n <= 6; n++) LV_orarioElenco_(g, n).forEach(function (x) { if (x.classe === classe) out[n] = { materia: x.materia, tipo: x.tipo }; });
  return out;
}
function LV_materiaCompito_(c, ore) { return (c.ora && ore && ore[c.ora]) ? ore[c.ora].materia : ''; }
function LV_materiaQuiz_(q, ore) {
  if (/(^|[^a-z])sic/i.test(q.id) || /sicurezza/i.test(q.titolo || '')) return 'Sicurezza professionale';
  var m = /ora\s*(\d)/i.exec(q.id || '') || /ora\s*(\d)/i.exec(q.titolo || '');
  return (m && ore && ore[Number(m[1])]) ? ore[Number(m[1])].materia : '';
}

/* ---------- una classe ---------- */
function LV_classe_(ss, classe, t0, ctx) {
  ctx = ctx || {};
  var ora = new Date(), gg = Number(LV_roma_(ora, 'd')), mm = Number(LV_roma_(ora, 'M')), giorno = LV_roma_(ora, 'yyyy-MM-dd');
  var avvisi = (ctx.avvisi || []).slice(), stato = 'ok', motivo = '', ore = ctx.ore || {};
  var corsi = LV_corsi_(ss, classe);
  if (!corsi.length) { LV_scriviErrore_(ss, classe, 'corso Classroom non trovato nella scheda Corsi'); return; }
  var isc = [], visti = {}, ci;
  for (ci = 0; ci < corsi.length; ci++) {
    LV_iscritti_(corsi[ci].id, classe).forEach(function (s) { if (!visti[s.u]) { visti[s.u] = 1; isc.push(s); } });   // stesso allievo in piu corsi: una riga sola
  }
  if (!isc.length) { LV_scriviErrore_(ss, classe, 'nessun iscritto letto dal corso Classroom'); return; }
  isc.sort(function (a, b) { var x = LV_nomeCR_(a), y = LV_nomeCR_(b); return x < y ? -1 : (x > y ? 1 : 0); });
  var etich = LV_brevi_(isc.map(LV_nomeCR_)), perUtente = {}, perEmail = {}, perNome = {};
  isc.forEach(function (s, i) { perUtente[s.u] = i; if (s.e) perEmail[s.e] = i; perNome[LV_nomeCR_(s).toUpperCase()] = i; });
  var ab = LV_abbinamenti_(ss, classe);
  Object.keys(ab).forEach(function (em) { if (perEmail[em] === undefined && perNome[ab[em]] !== undefined) perEmail[em] = perNome[ab[em]]; });
  var ultimo = isc.map(function () { return ''; });
  function agg(i, iso) { var ms = Date.parse(iso); if (isNaN(ms)) return; var cur = ultimo[i] ? Date.parse(ultimo[i]) : 0; if (ms > cur) ultimo[i] = LV_iso_(new Date(ms)); }
  var colonne = [], dati = isc.map(function () { return []; });
  // compiti di oggi, di TUTTI i corsi della classe
  var compiti = [];
  corsi.forEach(function (cr) {
    try { LV_compitiOggi_(cr.id, gg, mm, giorno).forEach(function (c) { c.corso = cr.id; c.corsoNome = cr.nome; compiti.push(c); }); }
    catch (e) { avvisi.push('compiti del corso «' + cr.nome + '» non letti: ' + String(e.message || e).slice(0, 100)); stato = 'parziale'; }
  });
  compiti.sort(function (a, b) { return a.ora - b.ora; });
  for (var c = 0; c < compiti.length; c++) {
    if (Date.now() - t0 > LV_FINE_MS) { stato = 'parziale'; motivo = 'tempo del giro finito: compiti ' + compiti.slice(c).map(function (x) { return x.ora ? 'Ora ' + x.ora : x.titolo.slice(0, 20); }).join(', ') + ' non letti'; break; }
    var cons = LV_consegne_(compiti[c].corso, compiti[c].id);
    var col = { k: 'C', titolo: compiti[c].titolo, link: compiti[c].link, ora: compiti[c].ora };
    var mat = LV_materiaCompito_(compiti[c], ore); if (mat) col.m = mat;
    if (corsi.length > 1) col.c = compiti[c].corsoNome;
    colonne.push(col);
    isc.forEach(function (s, i) {
      var x = cons[s.u];
      dati[i].push(x ? x.stato : '-');
      if (x && x.stato !== 'ASSEGNATO') agg(i, x.t);
    });
  }
  // quiz di oggi
  var quiz = [], nonAbb = 0, chiave = PropertiesService.getScriptProperties().getProperty('LV_CHIAVE') || '', pq = {};
  try { quiz = LV_quizOggi_(ss, classe, gg, mm); } catch (e) { avvisi.push('quiz di oggi non letti: ' + String(e.message || e).slice(0, 120)); stato = 'parziale'; }
  for (var q = 0; q < quiz.length; q++) {
    if (Date.now() - t0 > LV_FINE_MS) { stato = 'parziale'; motivo = (motivo ? motivo + '; ' : '') + 'tempo del giro finito: quiz ' + quiz.slice(q).map(function (x) { return x.id; }).join(', ') + ' non letti'; break; }
    var fatti = {}; pq[quiz[q].id] = {};
    quiz[q].forms.forEach(function (fid) {
      var form = FormApp.openById(fid), ris = form.getResponses(), tot = chiave ? LV_puntiTotali_(form) : 0;
      ris.forEach(function (r) {
        var em = String(r.getRespondentEmail() || '').toLowerCase(), i = perEmail[em];
        if (i === undefined) { nonAbb++; return; }
        fatti[i] = 1; agg(i, LV_iso_(r.getTimestamp()));
        if (chiave && tot > 0) { var pc = Math.round(LV_punteggio_(r) / tot * 100), cur = pq[quiz[q].id][i]; if (cur === undefined || pc > cur) pq[quiz[q].id][i] = pc; }   // miglior tentativo
      });
    });
    var colQ = { k: 'Q', id: quiz[q].id, titolo: quiz[q].titolo, link: quiz[q].link };
    var matQ = LV_materiaQuiz_(quiz[q], ore); if (matQ) colQ.m = matQ;
    colonne.push(colQ);
    isc.forEach(function (s, i) { dati[i].push(fatti[i] ? 'FATTO' : 'MANCA'); });
  }
  if (nonAbb) avvisi.push(nonAbb + ' risposte ai quiz di oggi con email non abbinata (non contate)');
  if (!compiti.length) avvisi.push('nessun compito «GG/MM Ora N» di oggi pubblicato su Classroom');
  if (!quiz.length) avvisi.push('nessun quiz di oggi trovato');
  var riservato = null;
  if (chiave) {
    try {
      var blocco = { v: 1, dato: LV_iso_(new Date(t0)), quiz: {} };
      Object.keys(pq).forEach(function (id) { blocco.quiz[id] = {}; Object.keys(pq[id]).forEach(function (i) { blocco.quiz[id][etich[i]] = pq[id][i]; }); });
      riservato = LV_cifra_(blocco, chiave);
    } catch (e) { avvisi.push('blocco riservato non scritto: ' + String(e.message || e).slice(0, 100)); }
  }
  LV_scrivi_(ss, classe, { contesto: ctx.contesto || { modo: 'riserva' }, riservato: riservato, dato: new Date(t0),   /* ora di INIZIO del giro: tutto cio che e scritto e stato letto dopo questo istante, quindi il dato e fresco almeno quanto dichiarato */ giorno: giorno, stato: stato, motivo: motivo, durata: Math.round((Date.now() - t0) / 1000), nonAbb: nonAbb, avvisi: avvisi, colonne: colonne, nomi: etich, dati: dati, ultimo: ultimo });
}

/* ---------- la scheda «Live <CLASSE>» ---------- */
function LV_scheda_(ss, classe) { return ss.getSheetByName('Live ' + classe) || ss.insertSheet('Live ' + classe); }
function LV_scrivi_(ss, classe, o) {
  var sh = LV_scheda_(ss, classe), nc = o.colonne.length, larg = Math.max(3, nc + 2), righe = [], i, j;
  function riga(a, b, c) { var r = [a, b, c || '']; while (r.length < larg) r.push(''); return r; }
  righe.push(riga('Live ' + classe, LV_iso_(o.dato), 'dati letti alle ' + LV_roma_(o.dato, 'HH:mm:ss')));
  righe.push(riga('lezione', o.giorno, JSON.stringify(o.contesto || {})));
  righe.push(riga('stato', o.stato, o.motivo));
  righe.push(riga('durata_s', o.durata));
  righe.push(riga('non_abbinate', o.nonAbb));
  righe.push(riga('versione', LV_VERSIONE, o.avvisi.join(' | ')));
  righe.push(riga('lavori', JSON.stringify(o.colonne)));
  var testa = ['Allievo'];
  o.colonne.forEach(function (c) { testa.push((c.k === 'C' ? 'C|' : 'Q|') + c.titolo); });
  testa.push('ULTIMO'); while (testa.length < larg) testa.push('');
  righe.push(testa);
  for (i = 0; i < o.nomi.length; i++) {
    var r = [o.nomi[i]];
    for (j = 0; j < nc; j++) r.push(o.dati[i][j]);
    r.push(o.ultimo[i]); while (r.length < larg) r.push('');
    righe.push(r);
  }
  var sr = ss.getSheetByName('Live riservato ' + classe) || ss.insertSheet('Live riservato ' + classe);
  sr.getRange(1, 1, 1, 2).setNumberFormat('@').setValues([[o.riservato ? JSON.stringify(o.riservato) : '', LV_iso_(o.dato)]]);
  sh.clearContents();
  var rg = sh.getRange(1, 1, righe.length, larg);
  rg.setNumberFormat('@');             // tutto testo: l'ora ISO non deve diventare una data
  rg.setValues(righe);
  SpreadsheetApp.flush();
}
function LV_scriviErrore_(ss, classe, msg) {   // non cancella i dati vecchi: cambia solo lo stato (l'ora del dato resta quella vecchia)
  var sh = LV_scheda_(ss, classe);
  if (sh.getLastRow() < 3) {
    sh.getRange(1, 1, 3, 3).setNumberFormat('@').setValues([['Live ' + classe, '', ''], ['lezione', LV_roma_(new Date(), 'yyyy-MM-dd'), ''], ['stato', 'non_letto', String(msg).slice(0, 300)]]);
  } else {
    sh.getRange(3, 1, 1, 3).setNumberFormat('@').setValues([['stato', 'non_letto', String(msg).slice(0, 300)]]);
  }
}

/* ---------- il job ---------- */
function LV_etaScheda_(ss, classe) {   // secondi dall'ora del dato in B1 della scheda Live; Infinity se non c'e
  var sh = ss.getSheetByName('Live ' + classe);
  if (!sh || sh.getLastRow() < 1) return Infinity;
  var ms = Date.parse(String(sh.getRange(1, 2).getValue() || ''));
  return isNaN(ms) ? Infinity : Math.max(0, (Date.now() - ms) / 1000);
}
/** Modalita di RISERVA (v1.1): tutte le classi, o quelle di LV_CLASSI, la piu vecchia per prima. */
function LV_classiRiserva_(ss) {
  var p = PropertiesService.getScriptProperties().getProperty('LV_CLASSI');
  var lista = p ? String(p).split(/[\s,;]+/).map(function (x) { return x.toUpperCase(); }).filter(function (x) { return LV_CLASSI_TUTTE.indexOf(x) >= 0; }) : LV_CLASSI_TUTTE.slice();
  var eta = {};
  lista.forEach(function (c) { var sh = ss.getSheetByName('Live ' + c); eta[c] = sh && sh.getLastRow() >= 1 ? String(sh.getRange(1, 2).getValue() || '') : ''; });
  lista.sort(function (a, b) { return eta[a] < eta[b] ? -1 : (eta[a] > eta[b] ? 1 : 0); });   // prima il dato piu vecchio (ISO si ordina come testo)
  return lista;
}
/** Che cosa fare in questo giro. -> {modo: 'orario'|'riserva', avviso, lavori: [{classe, ruolo: 'lezione'|'vicina', ora, materia, tipo, ore}]}
 *  Con l'orario letto: lezione = ogni classe in lezione (la piu vecchia per prima), vicina = classe dell'ora precedente/successiva con dato
 *  di piu di 8 minuti. Senza orario: tutte le classi (riserva) con l'avviso che dice perche. */
function LV_classiDaFare_(ss, ora, forza) {
  var giorno = LV_roma_(ora, 'yyyy-MM-dd'), u = Number(LV_roma_(ora, 'u')), min = Number(LV_roma_(ora, 'HH')) * 60 + Number(LV_roma_(ora, 'mm'));
  var po = LV_orarioLeggi_(giorno), lavori = [];
  if (!po.ok) {
    LV_classiRiserva_(ss).forEach(function (c) { lavori.push({ classe: c, ruolo: '', ora: 0, materia: '', tipo: '', ore: {} }); });
    return { modo: 'riserva', avviso: 'orario non letto: ' + po.errore + ' (modalita di riserva: tutte le classi a turno, non solo quella in lezione)', lavori: lavori };
  }
  var piano = LV_piano_(po.orario, u, min), eta = {};
  function voce(e, ruolo) { return { classe: e.classe, ruolo: ruolo, ora: e.ora, materia: e.materia, tipo: e.tipo, ore: LV_oreClasse_(po.orario, u, e.classe) }; }
  piano.lezione.forEach(function (e) { eta[e.classe] = LV_etaScheda_(ss, e.classe); });
  piano.lezione.sort(function (a, b) { return eta[a.classe] === eta[b.classe] ? 0 : (eta[b.classe] > eta[a.classe] ? 1 : -1); });   // il dato piu vecchio per primo (Infinity = mai letto: prima di tutti)
  piano.lezione.forEach(function (e) { lavori.push(voce(e, 'lezione')); });
  [piano.prec, piano.succ].forEach(function (e) {
    if (e && (forza || LV_etaScheda_(ss, e.classe) >= LV_VICINE_OGNI_S)) lavori.push(voce(e, 'vicina'));
  });
  return { modo: 'orario', avviso: '', lavori: lavori, fonte: po.fonte };
}
function LV_inOrario_() {
  var n = new Date(), g = Number(LV_roma_(n, 'u')), hm = LV_roma_(n, 'HH:mm');   // u: 1 = lunedi ... 7 = domenica
  return g >= 1 && g <= 5 && hm >= '07:45' && hm <= '14:20';
}
function LV_esegui_(forza) {
  var t0 = Date.now(), lock = LockService.getUserLock();
  if (!lock.tryLock(2000)) { Logger.log('live: un altro giro e in corso, salto'); return; }
  try {
    if (!forza && !LV_inOrario_()) return;
    var ss = LV_foglio_(), piano = LV_classiDaFare_(ss, new Date(t0), forza);
    if (forza && piano.modo === 'orario' && !piano.lavori.length) {   // prova a mano fuori lezione: si leggono tutte le classi per misurare la durata
      LV_classiRiserva_(ss).forEach(function (c) { piano.lavori.push({ classe: c, ruolo: '', ora: 0, materia: '', tipo: '', ore: {} }); });
      piano.avviso = 'prova a mano fuori lezione: tutte le classi';
    }
    Logger.log('live: modo ' + piano.modo + (piano.avviso ? ' (' + piano.avviso + ')' : '') + ', da fare: ' + (piano.lavori.map(function (l) { return l.classe + (l.ruolo ? ' ' + l.ruolo : ''); }).join(', ') || 'niente (nessuna lezione ora)'));
    for (var i = 0; i < piano.lavori.length; i++) {
      var l = piano.lavori[i];
      if (Date.now() - t0 > LV_AVVIO_MAX_MS) { Logger.log('live: saltate per il tempo ' + piano.lavori.slice(i).map(function (x) { return x.classe; }).join(', ') + ' (al giro dopo la piu vecchia va per prima)'); break; }
      var ctx = { avvisi: piano.avviso ? [piano.avviso] : [], ore: l.ore, contesto: { modo: piano.modo, ruolo: l.ruolo, ora: l.ora, materia: l.materia, tipo: l.tipo } };
      try { LV_classe_(ss, l.classe, t0, ctx); }
      catch (e) { Logger.log('live ' + l.classe + ': ' + e); try { LV_scriviErrore_(ss, l.classe, String(e.message || e).slice(0, 200)); } catch (e2) { } }
      Logger.log('live ' + l.classe + ' fatto dopo ' + Math.round((Date.now() - t0) / 1000) + ' s');
    }
  } finally { lock.releaseLock(); }
}
/** Funzione del trigger a tempo (ogni minuto). */
function live_giro() { LV_esegui_(false); }
/** Prova a mano, fuori orario: legge, scrive la scheda Live e nel log (Visualizza, Log di esecuzione) c'e la durata. */
function live_prova() { LV_esegui_(true); }
/** Si lancia UNA volta: crea il trigger a tempo ogni minuto per live_giro (toglie quelli vecchi). */
function live_installa() {
  live_spegni();
  ScriptApp.newTrigger('live_giro').timeBased().everyMinutes(1).create();
  Logger.log('CRUSCOTTO LIVE ATTIVO: live_giro ogni minuto, lun-ven 07:45-14:20, sulle classi in lezione secondo orario-live.json.');
}
function live_spegni() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'live_giro') ScriptApp.deleteTrigger(t); });
}

/* ---------- WEB APP ---------- */
function LV_pulisciNome_(s, k) {
  s = String(s || '').trim();
  if (/@/.test(s) || !/^[^\s\d@]+( [^\s\d@]+)* [A-ZÀ-Ý][a-zà-ÿ]{0,3}\.( \(\d+\))?$/.test(s)) return 'Allievo ' + (k + 1);
  return s;
}
function LV_leggi_(classe) {
  var ss = LV_foglio_(), sh = ss.getSheetByName('Live ' + classe), adesso = new Date();
  var base = { versione: LV_VERSIONE, classe: classe, generato_il: LV_iso_(adesso), dato_il: null, secondi_dal_dato: null, lezione: null, contesto: null, stato: 'non_letto', non_letto: null, criticita: [], lavori: { compiti: [], quiz: [] }, allievi: [] };
  if (!sh || sh.getLastRow() < 3) { base.non_letto = 'scheda Live ' + classe + ' non ancora scritta dal job'; base.criticita.push(base.non_letto); return base; }
  var v = sh.getDataRange().getDisplayValues(), i, j;
  var iso = String(v[0][1] || '');
  var ms = Date.parse(iso);
  base.dato_il = iso || null;
  base.riservato = null;
  try { var sr = ss.getSheetByName('Live riservato ' + classe); if (sr) { var rv = String(sr.getRange(1, 1).getDisplayValue() || ''); if (rv) { var ro = JSON.parse(rv); if (ro && ro.cifrato === 1) base.riservato = ro; } } } catch (e) { base.riservato = null; }
  base.secondi_dal_dato = isNaN(ms) ? null : Math.max(0, Math.round((adesso.getTime() - ms) / 1000));
  base.lezione = String(v[1][1] || '') || null;
  base.contesto = null; try { var cx = JSON.parse(String(v[1][2] || '')); if (cx && typeof cx === 'object') base.contesto = cx; } catch (e) { base.contesto = null; }
  base.stato = String(v[2][1] || 'non_letto');
  var motivo = String(v[2][2] || '');
  if (base.stato !== 'ok') { base.non_letto = motivo || base.stato; base.criticita.push((base.stato === 'parziale' ? 'Dato parziale: ' : 'Dato non letto: ') + (motivo || base.stato)); }
  var durata = Number(v[3] && v[3][1]), nonAbb = Number(v[4] && v[4][1]);
  base.durata_job_s = isNaN(durata) ? null : durata;
  if (nonAbb > 0) base.criticita.push(nonAbb + ' risposte ai quiz di oggi con email non abbinata (non contate)');
  var avv = String((v[5] && v[5][2]) || ''); if (avv) avv.split(' | ').forEach(function (a) { if (a && a.indexOf('email non abbinata') < 0) base.criticita.push(a); });
  var meta = []; try { meta = JSON.parse(String((v[6] && v[6][1]) || '[]')); } catch (e) { meta = []; }
  meta.forEach(function (m) { if (m.k === 'C') base.lavori.compiti.push({ titolo: m.titolo, link: m.link || '', ora: m.ora, materia: m.m || '', corso: m.c || '' }); else base.lavori.quiz.push({ id: m.id, titolo: m.titolo, link: m.link || '', materia: m.m || '' }); });
  for (i = LV_META; i < v.length; i++) {
    var nome = LV_pulisciNome_(v[i][0], i - LV_META);
    if (!String(v[i][0] || '').trim()) continue;
    var al = { nome: nome, compiti: [], quiz: [], ultimo: null };
    for (j = 0; j < meta.length; j++) {
      var cella = String(v[i][1 + j] || '');
      if (meta[j].k === 'C') al.compiti.push({ titolo: meta[j].titolo, stato: cella });
      else al.quiz.push({ id: meta[j].id, fatto: cella === 'FATTO' });
    }
    var u = String(v[i][1 + meta.length] || ''); al.ultimo = u && !isNaN(Date.parse(u)) ? u : null;
    base.allievi.push(al);
  }
  return base;
}
function doGet(e) {
  var p = (e && e.parameter) || {}, classe = String(p.classe || '').toUpperCase(), out;
  if (LV_CLASSI_TUTTE.indexOf(classe) < 0) out = { versione: LV_VERSIONE, errore: 'parametro classe mancante o sconosciuto (1inf, 2inf, 3inf, 4ti)', allievi: [], criticita: [] };
  else { try { out = LV_leggi_(classe); } catch (x) { out = { versione: LV_VERSIONE, classe: classe, generato_il: LV_iso_(new Date()), stato: 'non_letto', non_letto: 'errore del web app: ' + String(x.message || x).slice(0, 150), allievi: [], criticita: ['errore del web app'] }; } }
  var testo = JSON.stringify(out), cb = String(p.callback || '');
  if (/^[A-Za-z_][A-Za-z0-9_.]{0,40}$/.test(cb)) return ContentService.createTextOutput(cb + '(' + testo + ');').setMimeType(ContentService.MimeType.JAVASCRIPT);
  return ContentService.createTextOutput(testo).setMimeType(ContentService.MimeType.JSON);
}
/** Prova a mano del web app: scrive nel log il JSON della 1INF (solo Nome I.). */
function live_provaWeb() { Logger.log(JSON.stringify(LV_leggi_('1INF')).slice(0, 3000)); }
