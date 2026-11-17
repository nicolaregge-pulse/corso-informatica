/* Procedura guidata «Documento del progetto» (4TI). Tutto resta nel browser: nessuna richiesta di rete. */
(function () {
  "use strict";
  var PASSI = window.PASSI, CAP = window.CAPITOLI, GEN = window.GEN;
  var KEY = "progetto4ti_v1", KEYI = "progetto4ti_img_v1";
  var NP = PASSI.length;             // 15 domande; la schermata finale è la numero NP+1
  var S = { pos: 0, r: {}, img: [] };
  var okSt = true, timer = null;
  var $ = function (i) { return document.getElementById(i); };

  function el(t, c, x) { var e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }
  function uid() { uid.n = (uid.n || 0) + 1; return "c" + uid.n; }

  // ---------- salvataggio nel browser ----------
  function carica() {
    try {
      var a = localStorage.getItem(KEY), b = localStorage.getItem(KEYI);
      if (a) { var o = JSON.parse(a); if (o && typeof o === "object") { S.pos = o.pos | 0; S.r = o.r || {}; } }
      if (b) { var im = JSON.parse(b); if (Array.isArray(im)) S.img = im; }
    } catch (e) { okSt = false; }
  }
  var avvisoImg = false;
  function salvaOra() {
    try {
      localStorage.setItem(KEY, JSON.stringify({ pos: S.pos, r: S.r }));
      try { localStorage.setItem(KEYI, JSON.stringify(S.img)); avvisoImg = false; } catch (e2) { avvisoImg = true; }
      okSt = true;
    } catch (e) { okSt = false; }
    avvisi();
    var s = $("salvato"); if (s) s.textContent = okSt ? "Salvato nel tuo browser" : "NON salvato";
  }
  function salva() { clearTimeout(timer); timer = setTimeout(function () { timer = null; salvaOra(); }, 250); }
  function subito() { if (timer) { clearTimeout(timer); timer = null; salvaOra(); } }
  function avvisi() {
    $("avvisoStorage").hidden = okSt;
    $("avvisoImg").hidden = !avvisoImg;
  }

  // ---------- valori ----------
  function getR(k) { return S.r[k]; }
  function setR(k, v) { S.r[k] = v; salva(); }
  function riga(campo) { var o = {}; campo.colonne.forEach(function (c) { o[c.k] = ""; }); return o; }
  function righe(campo) {
    var a = S.r[campo.k];
    if (!Array.isArray(a)) { a = []; for (var i = 0; i < (campo.inizio || 1); i++) a.push(riga(campo)); S.r[campo.k] = a; }
    return a;
  }

  // ---------- costruzione dei campi ----------
  function campoTesto(f, box) {
    var id = uid(), lab = el("label", null, f.label); lab.setAttribute("for", id); box.appendChild(lab);
    var inp = f.tipo === "area" ? el("textarea") : el("input"); inp.id = id;
    if (f.tipo === "area") inp.rows = f.rows || 4; else { inp.type = "text"; if (f.max) inp.maxLength = f.max; }
    if (f.ph) inp.placeholder = f.ph;
    inp.autocomplete = "off"; inp.spellcheck = true;
    inp.value = getR(f.k) != null ? getR(f.k) : (f.k === "classe" ? "4TI" : "");
    if (f.k === "classe" && getR("classe") == null) S.r.classe = "4TI";
    inp.addEventListener("input", function () { setR(f.k, inp.value); });
    box.appendChild(inp);
  }

  function campoCaselle(f, box) {
    box.appendChild(el("p", "lab", f.label));
    var sel = Array.isArray(getR(f.k)) ? getR(f.k) : (S.r[f.k] = []);
    f.gruppi.forEach(function (g, gi) {
      var cont = box;
      if (g.titolo) {
        var det = el("details", "gr"); det.open = true;
        det.appendChild(el("summary", null, g.titolo));
        box.appendChild(det); cont = det;
      }
      g.voci.forEach(function (v, vi) {
        var id = g.sigla || "x", val = gi + "." + vi;
        var lb = el("label", "ho"); var cb = document.createElement("input"); cb.type = "checkbox"; cb.value = val;
        cb.checked = sel.indexOf(val) >= 0;
        cb.addEventListener("change", function () {
          var a = S.r[f.k], p = a.indexOf(val);
          if (cb.checked && p < 0) a.push(val); if (!cb.checked && p >= 0) a.splice(p, 1);
          salva();
        });
        lb.appendChild(cb); lb.appendChild(el("span", null, v)); cont.appendChild(lb);
      });
    });
  }

  function campoTabella(f, box) {
    box.appendChild(el("p", "lab", f.label));
    var lista = el("div"); box.appendChild(lista);
    var tot = null;
    if (f.calcolo === "costi") { tot = el("p", "totale"); }
    function aggiorna() {
      if (tot) {
        var t = 0, ok = false;
        righe(f).forEach(function (x) { var q = GEN.num(x.q), p = GEN.num(x.p); if (!isNaN(q) && !isNaN(p)) { t += q * p; ok = true; } });
        tot.textContent = "Totale: " + (ok ? GEN.euro(t) : "0,00") + " euro";
      }
      var gp = $("ganttBox"); if (gp && gp._agg) gp._agg();
    }
    function disegna() {
      lista.textContent = "";
      righe(f).forEach(function (x, ri) {
        var card = el("div", "riga");
        card.appendChild(el("p", "rt", f.riga + " " + (ri + 1)));
        var g = el("div", "gcols");
        f.colonne.forEach(function (c) {
          var id = uid(), w = el("div", "col"), lb = el("label", null, c.label); lb.setAttribute("for", id); w.appendChild(lb);
          var inp;
          if (c.tipo === "area") { inp = el("textarea"); inp.rows = 2; }
          else if (c.tipo === "scelta") { inp = el("select"); [""].concat(c.opz).forEach(function (o) { var op = el("option", null, o || "Scegli..."); op.value = o; inp.appendChild(op); }); }
          else { inp = el("input"); inp.type = c.tipo === "date" ? "date" : "text"; if (c.tipo === "num") inp.inputMode = "decimal"; }
          inp.id = id; inp.value = x[c.k] || ""; inp.autocomplete = "off";
          var ev = c.tipo === "scelta" || c.tipo === "date" ? "change" : "input";
          inp.addEventListener(ev, function () { x[c.k] = inp.value; salva(); aggiorna(); if (c.tipo === "date") avvisoData(card, x); if (f.calcolo) rtot(card, x); });
          if (c.tipo === "date") inp.addEventListener("input", function () { x[c.k] = inp.value; salva(); aggiorna(); avvisoData(card, x); });
          w.appendChild(inp); g.appendChild(w);
        });
        card.appendChild(g);
        if (f.calcolo) { card._rt = el("p", "rtot"); card.appendChild(card._rt); rtot(card, x); }
        if (f.k === "fasi") { card._av = el("p", "err"); card._av.setAttribute("role", "alert"); card.appendChild(card._av); avvisoData(card, x); }
        var del = el("button", "elim", "Togli questa riga"); del.type = "button";
        del.addEventListener("click", function () { righe(f).splice(ri, 1); if (!righe(f).length) righe(f).push(riga(f)); salva(); disegna(); aggiorna(); });
        card.appendChild(del);
        lista.appendChild(card);
      });
    }
    function rtot(card, x) {
      var q = GEN.num(x.q), p = GEN.num(x.p);
      card._rt.textContent = (!isNaN(q) && !isNaN(p)) ? "Totale di questa riga: " + GEN.euro(q * p) + " euro" : "Totale di questa riga: scrivi quanti pezzi e il prezzo";
    }
    function avvisoData(card, x) {
      if (!card._av) return;
      card._av.textContent = (x.a && x.b && x.b < x.a) ? "Attenzione: la data di fine viene prima della data di inizio." : "";
    }
    disegna();
    var add = el("button", "sec", "Aggiungi una riga"); add.type = "button";
    add.addEventListener("click", function () { righe(f).push(riga(f)); salva(); disegna(); aggiorna(); var k = lista.querySelectorAll("input,textarea"); if (k.length) k[k.length - f.colonne.length].focus(); });
    box.appendChild(add);
    if (tot) { box.appendChild(tot); }
    aggiorna();
  }

  // ---------- Gantt ----------
  function giorni(iso) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || ""); return m ? Date.UTC(+m[1], +m[2] - 1, +m[3]) / 86400000 : NaN; }
  function dmy(g) { var d = new Date(g * 86400000); return ("0" + d.getUTCDate()).slice(-2) + "/" + ("0" + (d.getUTCMonth() + 1)).slice(-2); }
  function ganttRighe() {
    var out = [], tutte = (S.r.fasi || []).filter(function (x) { return GEN.pieno(x.f) || x.a || x.b; });
    tutte.forEach(function (x) {
      var a = giorni(x.a), b = giorni(x.b);
      if (GEN.pieno(x.f) && !isNaN(a) && !isNaN(b) && b >= a) out.push({ f: x.f.trim(), a: a, b: b });
    });
    return { ok: out, scartate: tutte.length - out.length };
  }
  function disegnaGantt(cv, rr) {
    var n = rr.length, W = 1000, LW = 310, RW = 680, X0 = LW + 10, top = 62, rh = 56, H = top + n * rh + 24;
    cv.width = W; cv.height = H;
    var c = cv.getContext("2d");
    c.fillStyle = "#ffffff"; c.fillRect(0, 0, W, H);
    var min = Math.min.apply(null, rr.map(function (x) { return x.a; })), max = Math.max.apply(null, rr.map(function (x) { return x.b; })) + 1;
    var span = max - min, passo = [7, 14, 28, 56, 91, 182].filter(function (p) { return span / p <= 12; })[0] || 365;
    var px = function (g) { return X0 + (g - min) / span * (RW - 20); };
    c.font = "20px Arial, sans-serif"; c.textBaseline = "middle";
    c.strokeStyle = "#d5dae4"; c.lineWidth = 1; c.fillStyle = "#5b6573";
    for (var g = min; g <= max && px(g) < W - 30; g += passo) {
      var x = Math.round(px(g)) + .5; c.beginPath(); c.moveTo(x, top - 10); c.lineTo(x, H - 12); c.stroke();
      c.textAlign = "center"; c.fillText(dmy(g), x, top - 30);
    }
    rr.forEach(function (r, i) {
      var y = top + i * rh;
      if (i % 2 === 0) { c.fillStyle = "#f4f6fb"; c.fillRect(0, y, W, rh); }
      c.fillStyle = "#1d2433"; c.textAlign = "left"; c.font = "bold 22px Arial, sans-serif";
      var t = r.f; while (c.measureText(t).width > LW - 16 && t.length > 3) t = t.slice(0, -2);
      if (t !== r.f) t += "...";
      c.fillText((i + 1) + ". " + t, 10, y + rh / 2);
      var xa = px(r.a), xb = px(r.b + 1), w = Math.max(xb - xa, 8);
      c.fillStyle = "#0b6bcb"; c.beginPath();
      if (c.roundRect) c.roundRect(xa, y + 10, w, rh - 20, 8); else c.rect(xa, y + 10, w, rh - 20);
      c.fill();
      c.font = "18px Arial, sans-serif"; c.fillStyle = "#1d2433"; c.textAlign = "left";
      var lab = dmy(r.a) + " - " + dmy(r.b);
      if (xa + w + 6 + c.measureText(lab).width < W - 4) c.fillText(lab, xa + w + 6, y + rh / 2);
      else { c.textAlign = "right"; c.fillStyle = "#ffffff"; c.fillText(lab, xa + w - 6, y + rh / 2); }
    });
    c.strokeStyle = "#8a94a6"; c.strokeRect(.5, .5, W - 1, H - 1);
  }
  function campoGantt(f, box) {
    box.appendChild(el("p", "lab", f.label));
    var gb = el("div"); gb.id = "ganttBox"; box.appendChild(gb);
    var cv = el("canvas", "gantt"); cv.setAttribute("role", "img"); cv.id = "ganttCv";
    var msg = el("p", "nota");
    var gw = el("div", "ganttw"); gw.appendChild(cv); gb.appendChild(gw); gb.appendChild(msg);
    gb._agg = function () {
      var g = ganttRighe();
      if (g.ok.length) { cv.hidden = false; cv.setAttribute("aria-label", "Diagramma di Gantt con " + g.ok.length + " fasi"); disegnaGantt(cv, g.ok); } else { cv.hidden = true; }
      msg.textContent = g.ok.length ? (g.scartate ? g.scartate + " righe non sono nel disegno: manca il nome, manca una data o la fine viene prima dell'inizio." : "")
        : "Il disegno compare quando scrivi almeno una fase con la data di inizio e la data di fine.";
    };
    gb._agg();
  }
  function ganttDati() {
    var g = ganttRighe(); if (!g.ok.length) return null;
    var cv = document.createElement("canvas"); disegnaGantt(cv, g.ok);
    return { url: cv.toDataURL("image/png"), w: cv.width, h: cv.height };
  }

  // ---------- immagini ----------
  function ridimensiona(file, ok, ko) {
    var fr = new FileReader();
    fr.onerror = ko;
    fr.onload = function () {
      var im = new Image();
      im.onerror = ko;
      im.onload = function () {
        var w = im.naturalWidth, h = im.naturalHeight, m = Math.max(w, h);
        if (m > 1000) { w = Math.round(w * 1000 / m); h = Math.round(h * 1000 / m); }
        var cv = document.createElement("canvas"); cv.width = w; cv.height = h;
        var c = cv.getContext("2d"); c.fillStyle = "#fff"; c.fillRect(0, 0, w, h); c.drawImage(im, 0, 0, w, h);
        ok({ n: file.name, w: w, h: h, d: cv.toDataURL("image/jpeg", 0.85), cap: "" });
      };
      im.src = fr.result;
    };
    fr.readAsDataURL(file);
  }
  function campoImmagini(f, box) {
    box.appendChild(el("p", "lab", f.label));
    var lista = el("div"), err = el("p", "err"); err.setAttribute("role", "alert");
    var id = uid(), lb = el("label", null, "Scegli una o più immagini dal tuo computer"); lb.setAttribute("for", id);
    var inp = el("input"); inp.type = "file"; inp.accept = "image/*"; inp.multiple = true; inp.id = id;
    function disegna() {
      lista.textContent = "";
      S.img.forEach(function (im, i) {
        var card = el("div", "riga");
        card.appendChild(el("p", "rt", "Immagine " + (i + 1) + ": " + im.w + " x " + im.h + " punti"));
        var pr = el("img", "anteprima"); pr.src = im.d; pr.alt = im.cap ? im.cap : "Anteprima dell'immagine " + (i + 1); card.appendChild(pr);
        var cid = uid(), cl = el("label", null, "Didascalia: che cosa si vede"); cl.setAttribute("for", cid); card.appendChild(cl);
        var ci = el("input"); ci.type = "text"; ci.id = cid; ci.maxLength = 160; ci.value = im.cap || ""; ci.autocomplete = "off";
        ci.addEventListener("input", function () { im.cap = ci.value; salva(); }); card.appendChild(ci);
        var del = el("button", "elim", "Togli questa immagine"); del.type = "button";
        del.addEventListener("click", function () { S.img.splice(i, 1); salva(); disegna(); });
        card.appendChild(del); lista.appendChild(card);
      });
    }
    inp.addEventListener("change", function () {
      var fl = Array.prototype.slice.call(inp.files || []); err.textContent = "";
      var cod = fl.slice();
      (function avanti() {
        var file = cod.shift(); if (!file) { inp.value = ""; return; }
        ridimensiona(file, function (o) { S.img.push(o); salva(); disegna(); avanti(); }, function () { err.textContent = "Non riesco a leggere il file «" + file.name + "». Scegli una immagine (JPG o PNG)."; avanti(); });
      })();
    });
    box.appendChild(lb); box.appendChild(inp); box.appendChild(err); box.appendChild(lista);
    disegna();
  }

  // ---------- schermate ----------
  function badge(p) { return "Va nel capitolo " + p.cap + " del Documento: " + CAP[CAPDI(p.cap)].t; }
  function CAPDI(n) { return n - 1; }

  function mostra(i) {
    S.pos = i; salva();
    var box = $("schermata"); box.textContent = "";
    var tot = NP + 1;
    $("avtxt").textContent = i < NP ? "Passo " + (i + 1) + " di " + NP : "Ultimo passo: scarica il Documento";
    var perc = i < NP ? Math.round(i / NP * 100) : 100;
    $("avbar").firstElementChild.style.width = perc + "%";
    $("avbar").setAttribute("aria-valuenow", String(perc));
    $("vai").value = String(i);
    $("indietro").disabled = i === 0;
    $("avanti").hidden = i >= NP;
    if (i < NP) {
      var p = PASSI[i];
      box.appendChild(el("p", "capbadge", badge(p)));
      var h = el("h2", null, (i + 1) + ". " + p.titolo); h.tabIndex = -1; h.id = "titoloPasso"; box.appendChild(h);
      box.appendChild(el("p", null, p.intro));
      var det = el("details", "aiuto"); det.appendChild(el("summary", null, "Che cosa scrivere"));
      var ul = el("ul", "s"); p.aiuto.forEach(function (a) { ul.appendChild(el("li", null, a)); }); det.appendChild(ul); box.appendChild(det);
      var es = el("div", "box blu esempio"); es.appendChild(el("p", "et", "Esempio, con un progetto FINTO (non è di nessun allievo)"));
      es.appendChild(el("div", "etx", p.esempio)); box.appendChild(es);
      p.campi.forEach(function (f) {
        var c = el("div", "campo");
        if (f.tipo === "text" || f.tipo === "area") campoTesto(f, c);
        else if (f.tipo === "caselle") campoCaselle(f, c);
        else if (f.tipo === "tabella") campoTabella(f, c);
        else if (f.tipo === "gantt") campoGantt(f, c);
        else if (f.tipo === "immagini") campoImmagini(f, c);
        box.appendChild(c);
      });
      $("avanti").textContent = i === NP - 1 ? "Avanti: vai a scaricare il Documento" : "Avanti";
    } else {
      fine(box);
    }
    window.scrollTo(0, 0);
    var t = $("titoloPasso"); if (t) t.focus({ preventScroll: true });
  }

  function statoCap(c) {
    var v = 0; c.keys.forEach(function (k) { if (!GEN.vuotoVal(k === "img" ? S.img : S.r[k])) v++; });
    return { v: v, t: c.keys.length };
  }

  function schemaSvg(finestra, bottone, nota) {
    var s = '<svg viewBox="0 0 320 150" role="img" aria-label="Schema del passo: ' + bottone + '" xmlns="http://www.w3.org/2000/svg">' +
      '<rect x="2" y="2" width="316" height="146" rx="10" fill="#fff" stroke="#8a94a6" stroke-width="2"/>' +
      '<rect x="2" y="2" width="316" height="24" rx="10" fill="#e6eaf2"/><rect x="2" y="14" width="316" height="12" fill="#e6eaf2"/>' +
      '<circle cx="16" cy="14" r="4" fill="#c9d0de"/><circle cx="28" cy="14" r="4" fill="#c9d0de"/>' +
      '<rect x="48" y="7" width="200" height="14" rx="7" fill="#fff"/><text x="58" y="18" font-size="10" fill="#444">' + finestra + '</text>' +
      '<rect x="20" y="50" width="130" height="38" rx="19" fill="#0b6bcb"/><text x="85" y="73" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">' + bottone + '</text>' +
      '<ellipse cx="85" cy="69" rx="76" ry="28" fill="none" stroke="#d11" stroke-width="3" stroke-dasharray="6 3"/>' +
      '<text x="20" y="122" font-size="12" fill="#222">' + nota + '</text></svg>';
    return s;
  }

  function fine(box) {
    var h = el("h2", null, "Scarica il tuo Documento"); h.tabIndex = -1; h.id = "titoloPasso"; box.appendChild(h);
    box.appendChild(el("p", null, "Hai finito le domande. Qui sotto vedi quali capitoli hanno già il testo. I capitoli vuoti nel Documento hanno la scritta DA COMPLETARE."));
    var ul = el("ul", "capelenco");
    CAP.forEach(function (c) {
      var st = statoCap(c), li = el("li", st.v === st.t ? "ok" : st.v ? "meta" : "vuoto");
      li.appendChild(el("span", "ct", c.n + ". " + c.t));
      li.appendChild(el("span", "cs", st.v === st.t ? "completo" : st.v + (st.v === 1 ? " parte su " : " parti su ") + st.t));
      var b = el("button", "link", "Vai a scriverlo"); b.type = "button"; b.addEventListener("click", function () { mostra(c.passi[0] - 1); });
      li.appendChild(b); ul.appendChild(li);
    });
    box.appendChild(ul);
    var g = el("button", "grande", "Scarica il tuo Documento"); g.type = "button"; g.id = "scarica"; box.appendChild(g);
    var m = el("p", "ok2"); m.id = "msgScarica"; m.setAttribute("role", "status"); box.appendChild(m);
    var e = el("p", "err"); e.id = "errScarica"; e.setAttribute("role", "alert"); box.appendChild(e);
    g.addEventListener("click", scarica);

    box.appendChild(el("h2", null, "Adesso mettilo su Drive: 4 passi"));
    box.appendChild(el("p", null, "Il file che scarichi è un file di Word (.docx). Lo porti su Drive e lo apri con Documenti Google. Da quel momento continui a scrivere lì, tutto l'anno."));
    var passi = [
      ["Apri Drive", "Con l'account della scuola apri la pagina drive.google.com. In alto a sinistra clicca il bottone «Nuovo».", "drive.google.com", "Nuovo", "Bottone in alto a sinistra"],
      ["Carica il file", "Nel menu clicca «Caricamento file». Scegli il file che hai scaricato (di solito sta nella cartella Download).", "Drive: menu Nuovo", "Caricamento file", "Poi scegli il tuo file .docx"],
      ["Aprilo con Documenti Google", "Nell'elenco di Drive fai doppio clic sul file. In alto clicca il bottone «Apri con Documenti Google».", "Drive: anteprima del file", "Apri con Documenti Google", "Bottone in alto nella pagina"],
      ["Salvalo come Documento Google", "Nel menu «File» clicca «Salva come Documenti Google». Da adesso lavori sul Documento Google e non più sul file .docx.", "Documenti Google: menu File", "Salva come Documenti Google", "Voce del menu File"]
    ];
    var ol = el("ol", "steps");
    passi.forEach(function (p, i) {
      var li = el("li", "step"); li.appendChild(el("div", "n", String(i + 1)));
      var sb = el("div", "sb"); sb.appendChild(el("h3", null, "Passo " + (i + 1) + ": " + p[0])); sb.appendChild(el("p", null, p[1]));
      var fg = el("div", "fig"); fg.innerHTML = schemaSvg(p[2], p[3], p[4]); sb.appendChild(fg);
      sb.appendChild(el("p", "nota", "Questo è uno schema disegnato, non una foto vera dello schermo. I bottoni di Google possono avere un posto un po' diverso."));
      li.appendChild(sb); ol.appendChild(li);
    });
    box.appendChild(ol);
    box.appendChild(el("div", "box giallo", "Per aggiungere l'indice con i numeri di pagina: nel Documento Google clicca il menu «Inserisci», poi «Indice». Se il Documento ha una immagine storta, controllala prima di consegnare."));
  }

  function slug(s) {
    return String(s || "progetto").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "progetto";
  }
  function oggiIt() { var d = new Date(); return ("0" + d.getDate()).slice(-2) + "/" + ("0" + (d.getMonth() + 1)).slice(-2) + "/" + d.getFullYear(); }
  function scarica() {
    var e = $("errScarica"), m = $("msgScarica"); e.textContent = ""; m.textContent = "";
    try {
      if (!window.docx) throw new Error("manca la libreria");
      var gd = ganttDati();
      GEN.blob(S, gd && gd.url, gd, oggiIt()).then(function (blob) {
        var nome = "Documento-progetto-" + slug(S.r.titolo) + "-v0.1.docx";
        var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = nome;
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
        m.textContent = "Fatto. Il file «" + nome + "» è nella cartella Download. Ora vai ai 4 passi per Drive.";
      }, function (er) { e.textContent = "Non riesco a creare il file. Prova a togliere le immagini troppo grandi e riprova."; });
    } catch (er) { e.textContent = "Non riesco a creare il file. Ricarica la pagina e riprova."; }
  }

  // ---------- file .json, ricomincia ----------
  function salvaFile() {
    var o = { app: "progetto4ti", v: 1, salvato: new Date().toISOString(), r: S.r, img: S.img };
    var blob = new Blob([JSON.stringify(o)], { type: "application/json" });
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob);
    var d = new Date(); a.download = "risposte-progetto-" + d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2) + ".json";
    document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
    $("msgFile").textContent = "Fatto. Il file «" + a.download + "» è nella cartella Download. Tienilo nel tuo Drive.";
  }
  function caricaFile(file) {
    var msg = $("msgFile"); msg.textContent = "";
    var fr = new FileReader();
    fr.onerror = function () { msg.textContent = "Non riesco a leggere il file."; };
    fr.onload = function () {
      try {
        var o = JSON.parse(fr.result);
        if (!o || o.app !== "progetto4ti" || typeof o.r !== "object") throw new Error("no");
        S.r = o.r; S.img = Array.isArray(o.img) ? o.img : []; salvaOra();
        msg.textContent = "Risposte caricate. Controlla i passi.";
        mostra(0);
      } catch (e) { msg.textContent = "Questo file non è un file di risposte di questa pagina. Scegli un file .json salvato qui."; }
    };
    fr.readAsText(file);
  }
  var tRic = null;
  function ricomincia() {
    var b = $("ricomincia");
    if (!b.dataset.sicuro) {
      b.dataset.sicuro = "1"; b.textContent = "Sì, cancella tutte le risposte"; b.classList.add("elim");
      tRic = setTimeout(function () { delete b.dataset.sicuro; b.textContent = "Ricomincia"; b.classList.remove("elim"); }, 6000);
      return;
    }
    clearTimeout(tRic); delete b.dataset.sicuro; b.textContent = "Ricomincia"; b.classList.remove("elim");
    S = { pos: 0, r: {}, img: [] };
    try { localStorage.removeItem(KEY); localStorage.removeItem(KEYI); } catch (e) { }
    $("msgFile").textContent = "Tutte le risposte sono state cancellate."; mostra(0);
  }

  // ---------- avvio ----------
  function avvia() {
    carica();
    var sel = $("vai");
    PASSI.forEach(function (p, i) { var o = el("option", null, (i + 1) + ". " + p.titolo); o.value = String(i); sel.appendChild(o); });
    var o2 = el("option", null, "Scarica il Documento"); o2.value = String(NP); sel.appendChild(o2);
    sel.addEventListener("change", function () { mostra(parseInt(sel.value, 10)); });
    $("avanti").addEventListener("click", function () { mostra(Math.min(NP, S.pos + 1)); });
    $("indietro").addEventListener("click", function () { mostra(Math.max(0, S.pos - 1)); });
    $("salvaFile").addEventListener("click", salvaFile);
    $("caricaFile").addEventListener("change", function () { if (this.files[0]) caricaFile(this.files[0]); this.value = ""; });
    $("ricomincia").addEventListener("click", ricomincia);
    window.addEventListener("pagehide", subito);
    document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") subito(); });
    avvisi();
    var p = S.pos; if (!(p >= 0 && p <= NP)) p = 0;
    mostra(p);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", avvia); else avvia();
})();
