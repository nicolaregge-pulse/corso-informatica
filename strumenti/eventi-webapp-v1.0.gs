/**
 * EVENTI ALLIEVO - Apps Script v1.0 (20/11/2026). Raccoglie gli eventi mandati da strumenti/segnala-avanzamento-v1.0.js.
 * SOLO scrive nella scheda «Eventi» del foglio Fabbrica. Non legge niente, non tocca Classroom, Moduli, Drive. Nessun cognome:
 * l'allievo e' accettato solo nella forma «Nome I.» (altro = rifiutato, non scritto).
 * Foglio: proprieta dello script FB_FOGLIO (come cruscotto_web.gs), altrimenti il foglio a cui il progetto e legato.
 * Scheda «Eventi»: Ricevuto | Ora evento | Classe | Allievo | Tipo | Id | Stato | N | M | Secondi | Sessione
 * Se nel progetto c'e gia un doPost (lavagna-webapp.gs, automazione-corso.gs) ne puo esistere uno solo: rinomina questo in EV_doPost
 * e nell'altro doPost aggiungi in testa: if ((e.parameter.d||'').indexOf('"v":1')>0 && (e.parameter.d||'').indexOf('"a":')>0) return EV_doPost(e);
 */
var EV_SCHEDA_ = 'Eventi';
var EV_TIPI_ = { teoria: 1, compito: 1, quiz: 1 };
var EV_STATI_ = { visto: 1, iniziato: 1, avanzato: 1, consegnato: 1 };
var EV_MAX_RIGHE_ = 60000;
function EV_foglio_() {
  var id = PropertiesService.getScriptProperties().getProperty('FB_FOGLIO');
  return id ? SpreadsheetApp.openById(id) : SpreadsheetApp.getActive();
}
function EV_valida_(d) {
  if (!d || d.v !== 1) return 'versione';
  var a = String(d.a || '');
  if (!/^\p{L}[\p{L}'’-]{1,24} \p{L}\.$/u.test(a)) return 'allievo (solo Nome I.)';
  if (!EV_TIPI_[d.t]) return 'tipo';
  if (!EV_STATI_[d.s]) return 'stato';
  if (!/^[a-z0-9-]{1,80}$/i.test(String(d.id || ''))) return 'id';
  if (d.cl && !/^(1INF|2INF|3INF|4TI)$/.test(String(d.cl))) return 'classe';
  return '';
}
function EV_risposta_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function doPost(e) {
  var d;
  try { d = JSON.parse((e && e.parameter && e.parameter.d) || (e && e.postData && e.postData.contents) || '{}'); } catch (x) { return EV_risposta_({ ok: false, errore: 'json' }); }
  var err = EV_valida_(d);
  if (err) return EV_risposta_({ ok: false, errore: err });
  var chiave = ['ev', d.a, d.id, d.s, d.n, d.se].join('|'), cache = CacheService.getScriptCache();
  if (cache.get(chiave)) return EV_risposta_({ ok: true, doppio: true });   // stesso evento entro 10 s: ignorato
  cache.put(chiave, '1', 10);
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    var ss = EV_foglio_(), sh = ss.getSheetByName(EV_SCHEDA_) || ss.insertSheet(EV_SCHEDA_);
    if (sh.getLastRow() === 0) sh.getRange(1, 1, 1, 11).setValues([['Ricevuto', 'Ora evento', 'Classe', 'Allievo', 'Tipo', 'Id', 'Stato', 'N', 'M', 'Secondi', 'Sessione']]).setFontWeight('bold');
    if (sh.getLastRow() >= EV_MAX_RIGHE_) return EV_risposta_({ ok: false, errore: 'scheda piena' });
    sh.appendRow([new Date(), String(d.ts || '').slice(0, 30), String(d.cl || ''), d.a, d.t, String(d.id), d.s,
      Math.max(0, Math.min(999, Number(d.n) || 0)), Math.max(0, Math.min(999, Number(d.m) || 0)), Math.max(0, Math.min(86400, Number(d.sec) || 0)), String(d.se || '').replace(/[^a-z0-9]/gi, '').slice(0, 12)]);
    return EV_risposta_({ ok: true });
  } catch (x) { return EV_risposta_({ ok: false, errore: 'interno' }); }
  finally { try { lock.releaseLock(); } catch (y) { } }
}
