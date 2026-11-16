/* Registro stage 3INF - servizio Google Apps Script (v1.0, 16/11/2026). Account PIAMARTA.
   Salva le righe nel foglio «Registro stage 3INF» e le restituisce a chi le legge.
   Per scrivere serve la chiave derivata dalla password: qui c'e' solo l'impronta (VERIFICA), mai la password. */
var VERIFICA = "d8823d2283e3f89681d8fbde06c953a7951a60a7a43e390c9694b1e9b661786d";
var ALLIEVI = ["Alessandro A.","Denis A.","David A.","Eric C.","Nicolo' C.","Mirko D.","Ariel D.","Mahmoud E.","Rafi F.","Emmanuel F.","Andrea G.","Simone G.","Zhan L.","Tomas L.","Filippo M.","Beatrice N.","Kelvin P.","Kevin R.","Gabriele R.","Dani S.","Samuele U.","Noah V."];
var COLONNE = ["id","data","allievo","presenza","ore","attivita","inserito_il"];

function foglio_() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty("FOGLIO_ID");
  var ss = id ? SpreadsheetApp.openById(id) : null;
  if (!ss) { ss = SpreadsheetApp.create("Registro stage 3INF"); props.setProperty("FOGLIO_ID", ss.getId()); }
  var f = ss.getSheetByName("Registro") || ss.insertSheet("Registro");
  if (f.getLastRow() === 0) f.appendRow(COLONNE);
  return f;
}
function prepara() { var f = foglio_(); Logger.log("Foglio pronto: " + f.getParent().getUrl()); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function sha_(t) {
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, t, Utilities.Charset.UTF_8)
    .map(function (b) { return ("0" + (b < 0 ? b + 256 : b).toString(16)).slice(-2); }).join("");
}
function doGet() {
  var f = foglio_(), v = f.getDataRange().getValues(), righe = [];
  for (var i = 1; i < v.length; i++) {
    var d = v[i][1]; if (d instanceof Date) d = Utilities.formatDate(d, "Europe/Rome", "yyyy-MM-dd");
    righe.push({ id: v[i][0], data: d, allievo: v[i][2], presenza: v[i][3], ore: Number(v[i][4]), attivita: v[i][5] });
  }
  return json_({ ok: true, righe: righe });
}
function doPost(e) {
  var lock = LockService.getScriptLock(); lock.waitLock(20000);
  try {
    var q = JSON.parse(e.postData.contents);
    if (!VERIFICA || typeof q.k !== "string" || sha_(q.k) !== VERIFICA) return json_({ ok: false, errore: "accesso negato" });
    var f = foglio_();
    if (q.op === "add") {
      var r = q.riga || {};
      if (!/^\d{4}-\d{2}-\d{2}$/.test(r.data || "")) return json_({ ok: false, errore: "data" });
      if (ALLIEVI.indexOf(r.allievo) < 0) return json_({ ok: false, errore: "allievo" });
      if (["Presente", "Assente"].indexOf(r.presenza) < 0) return json_({ ok: false, errore: "presenza" });
      var ore = Number(r.ore); if (isNaN(ore) || ore < 0 || ore > 12) return json_({ ok: false, errore: "ore" });
      var att = String(r.attivita || "").slice(0, 300);
      var v = f.getDataRange().getValues();
      for (var i = 1; i < v.length; i++) {
        var d = v[i][1]; if (d instanceof Date) d = Utilities.formatDate(d, "Europe/Rome", "yyyy-MM-dd");
        if (d === r.data && v[i][2] === r.allievo) return json_({ ok: false, errore: "riga gia' presente" });
      }
      f.appendRow([Utilities.getUuid(), "'" + r.data, r.allievo, r.presenza, ore, att, new Date()]);
      return json_({ ok: true });
    }
    if (q.op === "del") {
      var vv = f.getDataRange().getValues();
      for (var j = 1; j < vv.length; j++) if (vv[j][0] === q.id) { f.deleteRow(j + 1); return json_({ ok: true }); }
      return json_({ ok: false, errore: "non trovata" });
    }
    return json_({ ok: false, errore: "operazione" });
  } finally { lock.releaseLock(); }
}
