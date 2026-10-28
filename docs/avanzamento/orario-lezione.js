// Orario della lezione per le pagine di monitoraggio (28/10/2026, richiesta del docente).
// Gli allarmi rossi sui dati vecchi («il dato ha N minuti», «Script FERMO») servono SOLO durante la lezione della classe
// e fino a 15 minuti dopo; dopo la lezione la pagina mostra in grigio «Dati finali della lezione, letti alle HH:MM».
// Dati: orario-lezioni.json (generato da strumenti/orario_json.py dalle tabelle orario/settimana-*.md).
// Uso: statoLezione('2INF').then(function (s) { ... s.stato: 'durante' | 'prima' | 'dopo' | 'nessuna' | 'ignoto' ... })
(function () {
  var MARGINE = 15;   // minuti dopo la fine della lezione in cui gli allarmi valgono ancora
  var promessa = null;
  function cartella() {
    var s = document.currentScript && document.currentScript.src;
    return s ? s.replace(/[^\/]*$/, '') : '';
  }
  var BASE = cartella();
  function adessoRoma() {
    var p = {};
    new Intl.DateTimeFormat('en-GB', {timeZone: 'Europe/Rome', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hour12: false})
      .formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
    return {giorno: p.year + '-' + p.month + '-' + p.day, min: (parseInt(p.hour, 10) % 24) * 60 + parseInt(p.minute, 10)};
  }
  function minuti(hhmm) { var a = String(hhmm).split(':'); return parseInt(a[0], 10) * 60 + parseInt(a[1] || '0', 10); }
  function carica() {
    if (!promessa) promessa = fetch(BASE + 'orario-lezioni.json?t=' + Date.now(), {cache: 'no-store'})
      .then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
    return promessa;
  }
  // stato della lezione di oggi per la classe: durante (da inizio a fine + 15 minuti), prima, dopo, nessuna (oggi non ha lezione),
  // ignoto (orario non leggibile: la pagina si comporta come prima, allarmi accesi)
  window.statoLezione = function (classe) {
    return carica().then(function (o) {
      if (!o || !o.lezioni) return {stato: 'ignoto'};
      var t = adessoRoma(), ore = (o.lezioni[t.giorno] || []).filter(function (v) { return v.classe === classe; });
      if (!ore.length) return {stato: 'nessuna'};
      var inizio = Math.min.apply(null, ore.map(function (v) { return minuti(v.da); }));
      var fine = Math.max.apply(null, ore.map(function (v) { return minuti(v.a); }));
      var dentro = ore.some(function (v) { return t.min >= minuti(v.da) && t.min <= minuti(v.a) + MARGINE; });
      var hh = function (m) { return String(Math.floor(m / 60)).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0'); };
      return {stato: dentro ? 'durante' : (t.min < inizio ? 'prima' : 'dopo'), inizio: hh(inizio), fine: hh(fine)};
    });
  };
  // il prossimo giorno di lezione della classe dopo il giorno g (AAAA-MM-GG); se l'orario non arriva così avanti,
  // si ripetono i giorni della settimana dell'ultima settimana nota
  window.prossimaLezione = function (classe, g) {
    return carica().then(function (o) {
      if (!o || !o.lezioni) return null;
      var giorni = Object.keys(o.lezioni).sort().filter(function (d) {
        return o.lezioni[d].some(function (v) { return v.classe === classe; }); });
      var dopo = giorni.filter(function (d) { return d > g; });
      if (dopo.length) return dopo[0];
      if (!giorni.length) return null;
      var ultimo = giorni[giorni.length - 1], lim = new Date(ultimo + 'T12:00:00Z');
      var dow = {};
      giorni.forEach(function (d) { if ((lim - new Date(d + 'T12:00:00Z')) / 864e5 < 7) dow[new Date(d + 'T12:00:00Z').getUTCDay()] = 1; });
      var x = new Date((g > ultimo ? g : ultimo) + 'T12:00:00Z');
      for (var i = 0; i < 14; i++) { x = new Date(x.getTime() + 864e5); if (dow[x.getUTCDay()]) return x.toISOString().slice(0, 10); }
      return null;
    });
  };
})();
