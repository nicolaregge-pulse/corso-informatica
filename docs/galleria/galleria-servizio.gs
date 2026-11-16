/* Galleria fotografica 2INF - servizio Google Apps Script v1.0 (16/11/2026). Account PIAMARTA.
   Ogni allievo ha la sua galleria (utente = nome utente GitHub, in minuscolo). Tutti VEDONO. Per CARICARE serve utente + password personale.
   ADMIN (utente "admin") puo' approvare gli account, caricare e togliere foto per chiunque.
   Qui ci sono solo SALE e IMPRONTE (hash): nessuna password in chiaro, nessun nome di allievo. Il browser deriva la chiave k = PBKDF2-SHA256(password, sale, iterazioni)
   e manda k; qui si confronta SHA-256(k) con l'impronta salvata. Foto: cartella Drive + foglio «Foto». Account: foglio «Utenti». */
/*ADMIN-INIZIO*/
var ADMIN_SALE = "ba3584d74839fcb725c0b1b46eaac528";        /* 32 caratteri esadecimali (sale PBKDF2 di ADMIN) */
var ADMIN_ITER = 2000000;   /* iterazioni PBKDF2 di ADMIN */
var ADMIN_VERIFICA = "070ec91801e7aecbde06aa30910967077df3d55732927e8fb0a1b7fbe4930a09";    /* SHA-256 della chiave derivata (64 caratteri esadecimali) */
/*ADMIN-FINE*/
var MAX_FOTO_UTENTE = 12, MAX_BASE64 = 420000, MAX_ATTESA = 200, MAX_ERRORI = 5, BLOCCO_SEC = 600;
var UTENTE_RE = /^[a-z0-9](?:[a-z0-9-]{0,37}[a-z0-9])?$/;

function ss_() {
  var p = PropertiesService.getScriptProperties(), id = p.getProperty("FOGLIO_ID"), ss = id ? SpreadsheetApp.openById(id) : null;
  if (!ss) { ss = SpreadsheetApp.create("Galleria 2INF"); p.setProperty("FOGLIO_ID", ss.getId()); }
  return ss;
}
function foglio_(nome, colonne) {
  var ss = ss_(), f = ss.getSheetByName(nome) || ss.insertSheet(nome);
  if (f.getLastRow() === 0) f.appendRow(colonne);
  return f;
}
function utenti_() { return foglio_("Utenti", ["utente", "sale", "iter", "impronta", "stato", "creato_il"]); }
function foto_() { return foglio_("Foto", ["id", "utente", "file_id", "titolo", "caricata_il"]); }
function cartella_() {
  var p = PropertiesService.getScriptProperties(), id = p.getProperty("CARTELLA_ID");
  if (id) return DriveApp.getFolderById(id);
  var c = DriveApp.createFolder("Galleria 2INF (foto)"); p.setProperty("CARTELLA_ID", c.getId()); return c;
}
/* da eseguire UNA volta dall'editor (gesto unico del docente) */
function prepara() { utenti_(); foto_(); cartella_(); Logger.log("Pronto: " + ss_().getUrl()); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function sha_(t) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, t, Utilities.Charset.UTF_8)
    .map(function (b) { return ("0" + (b < 0 ? b + 256 : b).toString(16)).slice(-2); }).join("");
}
function utente_(nome) {
  var v = utenti_().getDataRange().getValues();
  for (var i = 1; i < v.length; i++) if (v[i][0] === nome) return {riga: i + 1, sale: String(v[i][1]), iter: Number(v[i][2]), impronta: String(v[i][3]), stato: String(v[i][4])};
  return null;
}
function erroriChiave_(u) { return "err:" + sha_(u).slice(0, 16); }
function bloccato_(u) { return Number(CacheService.getScriptCache().get(erroriChiave_(u)) || 0) >= MAX_ERRORI; }
function sbagliata_(u) {
  var c = CacheService.getScriptCache(), k = erroriChiave_(u), n = Number(c.get(k) || 0) + 1;
  c.put(k, String(n), BLOCCO_SEC); Utilities.sleep(1000);
}
/* chi e' questa chiave? "admin", "allievo" o null. Dopo MAX_ERRORI errori l'utente e' bloccato per BLOCCO_SEC secondi. */
function chi_(u, k) {
  if (typeof u !== "string") return null;
  if (bloccato_(u)) return "bloccato";
  if (typeof k !== "string" || !/^[0-9a-f]{64}$/.test(k)) { sbagliata_(u); return null; }
  var h = sha_(k);
  if (u === "admin") { if (ADMIN_VERIFICA && h === ADMIN_VERIFICA) return "admin"; sbagliata_(u); return null; }
  var a = utente_(u);
  if (a && a.stato === "attivo" && a.impronta && h === a.impronta) return "allievo";
  sbagliata_(u); return null;
}
function elencoFoto_(per) {
  var v = foto_().getDataRange().getValues(), out = [];
  for (var i = 1; i < v.length; i++) if (v[i][0] && (!per || v[i][1] === per)) out.push({id: String(v[i][0]), u: v[i][1], url: "https://drive.google.com/thumbnail?id=" + v[i][2] + "&sz=w1000", t: String(v[i][3] || "")});
  return out;
}
function doGet(e) {
  var q = (e && e.parameter) || {}, op = q.op || "lista", u = String(q.u || "").toLowerCase();
  if (op === "utente") {   /* sale e iterazioni per accedere (pubblici) */
    if (u === "admin") return json_({ok: true, esiste: true, stato: "attivo", sale: ADMIN_SALE, iter: ADMIN_ITER});
    var a = utente_(u);
    return json_({ok: true, esiste: !!a, stato: a ? a.stato : "", sale: a ? a.sale : "", iter: a ? a.iter : 0});
  }
  var v = utenti_().getDataRange().getValues(), utenti = [], i;
  for (i = 1; i < v.length; i++) if (v[i][4] === "attivo") utenti.push(v[i][0]);
  return json_({ok: true, versione: "1.0", utenti: utenti, foto: elencoFoto_(u && u !== "admin" ? u : "")});
}
function doPost(e) {
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var q = JSON.parse(e.postData.contents), op = q.op, u = String(q.u || "").toLowerCase(), per = String(q.per || u).toLowerCase();
    if (op === "richiedi") {   /* un allievo chiede l'account: resta «attesa» finche' ADMIN non approva */
      if (!UTENTE_RE.test(u) || u === "admin") return json_({ok: false, errore: "nome utente"});
      if (utente_(u)) return json_({ok: false, errore: "esiste gia"});
      if (!/^[0-9a-f]{32}$/.test(q.sale || "") || !/^[0-9a-f]{64}$/.test(q.impronta || "") || !(Number(q.iter) >= 100000 && Number(q.iter) <= 1000000)) return json_({ok: false, errore: "formato"});
      var att = 0, vv = utenti_().getDataRange().getValues(), j; for (j = 1; j < vv.length; j++) if (vv[j][4] === "attesa") att++;
      if (att >= MAX_ATTESA) return json_({ok: false, errore: "troppe richieste"});
      utenti_().appendRow([u, q.sale, Number(q.iter), q.impronta, "attesa", new Date()]);
      return json_({ok: true, stato: "attesa"});
    }
    var chi = chi_(u, q.k);
    if (chi === "bloccato") return json_({ok: false, errore: "troppi tentativi: riprova tra 10 minuti"});
    if (!chi) return json_({ok: false, errore: "accesso negato"});
    if (op === "verifica") return json_({ok: true, chi: chi});
    if (chi === "admin" && op === "attesa") {
      var w = utenti_().getDataRange().getValues(), l = [], r; for (r = 1; r < w.length; r++) if (w[r][4] === "attesa") l.push(w[r][0]);
      return json_({ok: true, attesa: l});
    }
    if (chi === "admin" && (op === "approva" || op === "rifiuta" || op === "reset")) {
      var t = String(q.utente || "").toLowerCase(), a = utente_(t); if (!a) return json_({ok: false, errore: "utente"});
      if (op === "approva") utenti_().getRange(a.riga, 5).setValue("attivo"); else utenti_().deleteRow(a.riga);
      return json_({ok: true});
    }
    if (per !== u && chi !== "admin") return json_({ok: false, errore: "solo la tua galleria"});
    if (per !== "admin" && !utente_(per)) return json_({ok: false, errore: "utente"});
    if (op === "carica") {
      var b = String(q.img || "");
      if (b.length < 100 || b.length > MAX_BASE64 || !/^[A-Za-z0-9+\/=]+$/.test(b)) return json_({ok: false, errore: "immagine"});
      var bytes = Utilities.base64Decode(b);
      if (!(bytes.length > 3 && (bytes[0] & 255) === 255 && (bytes[1] & 255) === 216 && (bytes[2] & 255) === 255)) return json_({ok: false, errore: "solo JPEG"});
      if (elencoFoto_(per).length >= MAX_FOTO_UTENTE) return json_({ok: false, errore: "massimo " + MAX_FOTO_UTENTE + " foto"});
      var id = Utilities.getUuid().replace(/-/g, "").slice(0, 12), nome = per + "-" + id + ".jpg";
      var file = cartella_().createFile(Utilities.newBlob(bytes, "image/jpeg", nome)); file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      foto_().appendRow([id, per, file.getId(), String(q.titolo || "").replace(/[<>]/g, "").slice(0, 80), new Date()]);
      return json_({ok: true, id: id, foto: elencoFoto_(per)});
    }
    if (op === "togli") {
      var f = foto_(), z = f.getDataRange().getValues(), k;
      for (k = 1; k < z.length; k++) if (z[k][0] === q.id && z[k][1] === per) {
        try { DriveApp.getFileById(z[k][2]).setTrashed(true); } catch (x) {}
        f.deleteRow(k + 1); return json_({ok: true, foto: elencoFoto_(per)});
      }
      return json_({ok: false, errore: "foto"});
    }
    return json_({ok: false, errore: "operazione"});
  } finally { lock.releaseLock(); }
}
