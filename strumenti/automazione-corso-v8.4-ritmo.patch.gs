/* AUTOMAZIONE CORSO v8.4 — PROPOSTA (28/10/2026): la «leva» del ritmo dal cruscotto del docente.
 * NON e' il file da incollare: e' la modifica da applicare a strumenti/automazione-corso.gs (v8.3) quando Nicola
 * decide di passare alla v8.4. Finche' non si applica, il cruscotto dice «Per ora il ritmo si cambia chiedendolo a Claude».
 *
 * Che cosa fa: doGet accetta ?ritmo=0|1|5|10&k=<chiave> e cambia il timer SUBITO (non al prossimo giro del ponte).
 * Protezione: la chiave sta nelle proprieta' dello script, RITMO_CHIAVE (Impostazioni progetto -> Proprieta' dello script).
 * Senza chiave giusta non cambia niente. Funziona anche quando lo script e' SPENTO (il ponte invece no: da spento
 * non gira, quindi un comando «script.ritmo» non lo riaccende).
 *
 * Il cruscotto (docs/cruscotto/index.html) apre una scheda verso <invio>?ritmo=N&k=<codice docente>: per non avere
 * una seconda password, RITMO_CHIAVE si imposta uguale a MONITOR_TOKEN (il codice del monitor che il docente usa gia').
 * Poi nel cruscotto si mette RITMO_V84 = true (una riga) e i bottoni diventano attivi.
 *
 * MODIFICA 1 — in AUTO_stato(): versione '8.4' e il campo leva_ritmo, cosi' il cruscotto sa che la leva c'e'.
 *   return { versione: '8.4', leva_ritmo: true, ritmo: ... (resto uguale) };
 *
 * MODIFICA 2 — in doGet(e), SUBITO DOPO la riga «var p = (e && e.parameter) || {};» aggiungere:
 *   if (p.ritmo !== undefined) return AUTO_ritmoDaWeb(p.ritmo, p.k, p.callback);
 *   AUTO_assicuraTimer() resta la prima riga di doGet com'e' (rispetta il ritmo scelto).
 *
 * MODIFICA 3 — aggiungere questa funzione (per esempio subito dopo doGet):
 */
function AUTO_ritmoDaWeb(min, k, cb) {
  var pr = PropertiesService.getScriptProperties(), atteso = pr.getProperty('RITMO_CHIAVE') || '';
  var mm = +min;
  if (!atteso || String(k || '') !== atteso) {
    var e1 = { ok: false, errore: atteso ? 'codice' : 'manca RITMO_CHIAVE nelle proprieta dello script' };
    return cb ? AUTO_rispostaJs(JSON.stringify(e1), cb)
      : AUTO_paginaArrivo('Ritmo NON cambiato', atteso ? 'Il codice non e\' giusto.' : 'Manca RITMO_CHIAVE nelle proprieta dello script.', '#c0392b');
  }
  if ([0, 1, 5, 10].indexOf(mm) < 0) {
    return cb ? AUTO_rispostaJs(JSON.stringify({ ok: false, errore: 'ritmo 0, 1, 5 o 10' }), cb)
      : AUTO_paginaArrivo('Ritmo NON cambiato', 'Il ritmo puo\' essere 1, 5, 10 minuti o 0 (spento).', '#c0392b');
  }
  AUTO_ritmo(mm);                                    // cancella il vecchio timer e ne crea uno nuovo: vale da subito
  var st = AUTO_stato(); st.ok = true; st.ora = new Date().toISOString();
  if (cb) return AUTO_rispostaJs(JSON.stringify(st), cb);
  return AUTO_paginaArrivo('Ritmo cambiato', mm ? 'Lo script ora gira ogni ' + mm + (mm === 1 ? ' minuto.' : ' minuti.') : 'Lo script ora e\' SPENTO.', '#1a7f37');
}
/*
 * DOPO AVER INCOLLATO: «Salva», poi «Esegui il deployment» -> «Gestisci deployment» -> matita -> Versione «Nuova versione»
 * -> «Esegui il deployment» (stesso indirizzo /exec di prima). Senza nuova versione il web app resta alla v8.3.
 */
