/* Presenze stage 3INF - servizio Google Apps Script (v2.1, 16/11/2026: nuova impronta del docente; se il servizio e' gia' distribuito, aggiornare DOCENTE_VERIFICA). Account PIAMARTA.
   Un foglio con una riga per allievo e per giorno. Legge per tutti (sola lettura). Scrive solo con la chiave dello stagista
   (derivata dalla sua password) o, se DOCENTE_MODIFICA e' true, con la chiave del docente. Qui ci sono solo impronte, mai password. */
var DOCENTE_MODIFICA = true;                 /* UN SOLO VALORE: false = puo' modificare solo lo stagista */
/*DOC-INIZIO*/
var DOCENTE_VERIFICA = "aa7f3bc6ee890cc2c3f1fb0e5d5bc6c0f261cc8dd26fa501a1899412390e0832";
/*DOC-FINE*/
var INIZIO = "2026-11-23", FINE = "2027-02-18";
var ALLIEVI = ["Alessandro A.","Denis A.","David A.","Eric C.","Nicolo' C.","Mirko D.","Ariel D.","Mahmoud E.","Rafi F.","Emmanuel F.","Andrea G.","Simone G.","Zhan L.","Tomas L.","Filippo M.","Beatrice N.","Kelvin P.","Kevin R.","Gabriele R.","Dani S.","Samuele U.","Noah V."];
var STATI = ["N", "L", "P", "A"];

function ss_() {
  var props = PropertiesService.getScriptProperties(), id = props.getProperty("FOGLIO_ID"), ss = id ? SpreadsheetApp.openById(id) : null;
  if (!ss) { ss = SpreadsheetApp.create("Presenze stage 3INF"); props.setProperty("FOGLIO_ID", ss.getId()); }
  return ss;
}
function foglio_(nome, colonne) {
  var ss = ss_(), f = ss.getSheetByName(nome) || ss.insertSheet(nome);
  if (f.getLastRow() === 0) { f.appendRow(colonne); f.getRange(1, 1, 1, colonne.length).setNumberFormat("@"); }
  return f;
}
function presenze_() { var f = foglio_("Presenze", ["allievo", "data", "stato", "ore", "attivita", "modificato_il"]); f.getRange(1, 2, 1000, 1).setNumberFormat("@"); return f; }
function accessi_() { return foglio_("Accessi", ["allievo", "salt", "verifier", "impostata_il"]); }
function prepara() { presenze_(); accessi_(); Logger.log("Foglio pronto: " + ss_().getUrl()); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function sha_(t) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, t, Utilities.Charset.UTF_8)
    .map(function (b) { return ("0" + (b < 0 ? b + 256 : b).toString(16)).slice(-2); }).join("");
}
function data_(d) { return d instanceof Date ? Utilities.formatDate(d, "Europe/Rome", "yyyy-MM-dd") : String(d); }
function giornoValido_(d) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d) || d < INIZIO || d > FINE) return false;
  var p = d.split("-"), w = new Date(Date.UTC(+p[0], +p[1] - 1, +p[2])).getUTCDay();
  return w !== 0 && isoOk_(d, p);
}
function isoOk_(d, p) { return new Date(Date.UTC(+p[0], +p[1] - 1, +p[2])).toISOString().slice(0, 10) === d; }
function accessoAllievo_(nome) {
  var v = accessi_().getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][0] === nome) return {riga: i + 1, salt: String(v[i][1]), verifier: String(v[i][2])};
  return null;
}
/* chi e' questa chiave? "allievo", "docente" oppure null. La chiave sbagliata costa 1 secondo (contro i tentativi a raffica). */
function chi_(nome, k) {
  if (typeof k !== "string" || k.length < 16) { Utilities.sleep(1000); return null; }
  var h = sha_(k), a = accessoAllievo_(nome);
  if (a && a.verifier && h === a.verifier) return "allievo";
  if (DOCENTE_MODIFICA && DOCENTE_VERIFICA && h === DOCENTE_VERIFICA) return "docente";
  Utilities.sleep(1000); return null;
}
function doGet() {
  var righe = [], v = presenze_().getDataRange().getValues(), allievi = [], a = accessi_().getDataRange().getValues(), i;
  for (i = 1; i < v.length; i++) if (v[i][0]) righe.push({a: v[i][0], d: data_(v[i][1]), s: v[i][2], o: Number(v[i][3]) || 0, t: String(v[i][4] || "")});
  var mappa = {}; for (i = 1; i < a.length; i++) mappa[a[i][0]] = String(a[i][1]);
  ALLIEVI.forEach(function (n) { allievi.push({nome: n, haPassword: !!mappa[n], salt: mappa[n] || ""}); });
  return json_({ok: true, versione: "2.0", docenteModifica: DOCENTE_MODIFICA, periodo: {inizio: INIZIO, fine: FINE}, allievi: allievi, giorni: righe});
}
function doPost(e) {
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var q = JSON.parse(e.postData.contents), nome = q.allievo;
    if (ALLIEVI.indexOf(nome) < 0) return json_({ok: false, errore: "allievo"});
    if (q.op === "imposta") {
      if (accessoAllievo_(nome)) return json_({ok: false, errore: "password gia' scelta"});
      if (!/^[0-9a-f]{32}$/.test(q.salt || "") || !/^[0-9a-f]{64}$/.test(q.verifier || "")) return json_({ok: false, errore: "formato"});
      accessi_().appendRow([nome, q.salt, q.verifier, new Date()]);
      return json_({ok: true});
    }
    var chi = chi_(nome, q.k);
    if (!chi) return json_({ok: false, errore: "accesso negato"});
    if (q.op === "verifica") return json_({ok: true, chi: chi});
    if (q.op === "reset") {
      if (chi !== "docente") return json_({ok: false, errore: "solo il docente"});
      var a = accessoAllievo_(nome); if (a) accessi_().deleteRow(a.riga);
      return json_({ok: true});
    }
    if (q.op === "salva") {
      var lista = q.giorni; if (!(lista instanceof Array) || !lista.length || lista.length > 200) return json_({ok: false, errore: "elenco"});
      var puliti = [], i;
      for (i = 0; i < lista.length; i++) {
        var g = lista[i] || {}, s = String(g.s || "");
        if (!giornoValido_(String(g.d))) return json_({ok: false, errore: "data"});
        if (s !== "" && STATI.indexOf(s) < 0) return json_({ok: false, errore: "stato"});
        var o = Number(g.o) || 0; if (o < 0 || o > 12) return json_({ok: false, errore: "ore"});
        if (s !== "P") o = 0;
        var t = (s === "P" || s === "L") ? String(g.t || "").slice(0, 200) : "";
        puliti.push({d: String(g.d), s: s, o: o, t: t});
      }
      var f = presenze_(), v = f.getDataRange().getValues(), idx = {}, r;
      for (r = 1; r < v.length; r++) if (v[r][0] === nome) idx[data_(v[r][1])] = r + 1;
      var nuove = [], cancella = [], adesso = new Date();
      puliti.forEach(function (g) {
        var riga = idx[g.d];
        if (g.s === "") { if (riga) cancella.push(riga); }
        else if (riga) f.getRange(riga, 3, 1, 4).setValues([[g.s, g.o, g.t, adesso]]);
        else nuove.push([nome, g.d, g.s, g.o, g.t, adesso]);
      });
      cancella.sort(function (x, y) { return y - x; }).forEach(function (riga) { f.deleteRow(riga); });
      if (nuove.length) { var ult = f.getLastRow(); f.getRange(ult + 1, 2, nuove.length, 1).setNumberFormat("@"); f.getRange(ult + 1, 1, nuove.length, 6).setValues(nuove); }
      return json_({ok: true, chi: chi});
    }
    return json_({ok: false, errore: "operazione"});
  } finally { lock.releaseLock(); }
}
