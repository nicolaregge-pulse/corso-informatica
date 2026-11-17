/* Crea il file .docx del Documento del progetto, nel browser, con la libreria docx (cartella vendor).
   Nessuna richiesta di rete. Capitoli e parole: gli stessi della guida e del modello (12 capitoli). */
(function () {
  "use strict";
  var D = window.docx;
  var AZZ = "0B6BCB";
  var W = 9072; // larghezza utile in DXA (A4 con margini di 2,5 cm)

  function pul(s) { return String(s == null ? "" : s).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f￾￿]/g, ""); }
  function pieno(s) { return pul(s).trim() !== ""; }
  function dataIt(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || "");
    return m ? m[3] + "/" + m[2] + "/" + m[1] : pul(iso);
  }
  function num(s) {
    s = String(s == null ? "" : s).trim();
    if (!s) return NaN;
    if (s.indexOf(",") >= 0) s = s.replace(/\./g, "").replace(",", ".");
    return parseFloat(s);
  }
  function euro(n) { return n.toLocaleString("it-IT", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function bytes(dataUrl) {
    var b = atob(dataUrl.split(",")[1]), a = new Uint8Array(b.length);
    for (var i = 0; i < b.length; i++) a[i] = b.charCodeAt(i);
    return a;
  }
  function vuotoVal(v) {
    if (v == null) return true;
    if (typeof v === "string") return !pieno(v);
    if (Array.isArray(v)) {
      if (!v.length) return true;
      return v.every(function (x) {
        if (x && typeof x === "object") return x.d ? false : Object.keys(x).every(function (k) { return !pieno(x[k]); });
        return !pieno(x);
      });
    }
    return false;
  }
  function righeVere(arr) {
    return (arr || []).filter(function (r) { return Object.keys(r).some(function (k) { return pieno(r[k]); }); });
  }

  // ---------- elementi ----------
  function T(text, o) { return new D.TextRun(Object.assign({ text: pul(text) }, o || {})); }
  function P(text, o) {
    o = o || {};
    return new D.Paragraph({ spacing: { after: 120 }, alignment: o.align, children: [T(text, o.run)] });
  }
  function testo(s) { // testo su più righe -> più paragrafi
    return pul(s).split(/\r?\n/).map(function (r) { return P(r); });
  }
  function H1(n, t) {
    return new D.Paragraph({ heading: D.HeadingLevel.HEADING_1, children: [new D.Bookmark({ id: "cap" + n, children: [T(n + ". " + t)] })] });
  }
  function H2(t) { return new D.Paragraph({ heading: D.HeadingLevel.HEADING_2, children: [T(t)] }); }
  function seg(testoPh) { // segnaposto
    return new D.Paragraph({ spacing: { after: 160 }, children: [T("DA COMPLETARE: " + testoPh, { bold: true, color: "9A3412", highlight: "yellow" })] });
  }
  function didascalia(t) {
    return new D.Paragraph({ style: "Caption", spacing: { after: 200 }, alignment: D.AlignmentType.CENTER, children: [T(t, { italics: true, size: 20 })] });
  }
  var BORDO = { style: D.BorderStyle.SINGLE, size: 4, color: "9AA5B8" };
  function tabella(cols, widths, rows, opz) {
    opz = opz || {};
    function cella(testoCella, w, o) {
      o = o || {};
      var righe = pul(testoCella).split(/\r?\n/);
      return new D.TableCell({
        width: { size: w, type: D.WidthType.DXA },
        shading: o.fill ? { type: D.ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: righe.map(function (r) {
          return new D.Paragraph({ alignment: o.align, children: [T(r, { bold: o.bold, color: o.color, size: 20 })] });
        })
      });
    }
    var head = new D.TableRow({ tableHeader: true, cantSplit: true, children: cols.map(function (c, i) { return cella(c, widths[i], { fill: AZZ, bold: true, color: "FFFFFF" }); }) });
    var body = rows.map(function (r, ri) {
      return new D.TableRow({ cantSplit: true, children: r.map(function (c, i) {
        var o = {};
        if (opz.ultimaRiga && ri === rows.length - 1) { o.bold = true; o.fill = "E1EFFF"; }
        if (opz.destra && opz.destra.indexOf(i) >= 0) o.align = D.AlignmentType.RIGHT;
        return cella(c, widths[i], o);
      }) });
    });
    return new D.Table({
      width: { size: W, type: D.WidthType.DXA }, columnWidths: widths, layout: D.TableLayoutType.FIXED,
      borders: { top: BORDO, bottom: BORDO, left: BORDO, right: BORDO, insideHorizontal: BORDO, insideVertical: BORDO },
      rows: [head].concat(body)
    });
  }
  function spazio() { return new D.Paragraph({ spacing: { after: 120 }, children: [] }); }
  function elenco(items) {
    return items.map(function (t) { return new D.Paragraph({ bullet: { level: 0 }, spacing: { after: 60 }, children: [T(t)] }); });
  }

  // ---------- contenuto dei capitoli ----------
  function costruisci(S, ganttUrl, ganttDim, oggi) {
    var r = S.r, img = S.img || [];
    var titolo = pieno(r.titolo) ? pul(r.titolo).trim() : "Progetto senza titolo";
    var autore = pieno(r.nome) ? pul(r.nome).trim() : "da completare";
    var classe = pieno(r.classe) ? pul(r.classe).trim() : "4TI";
    var cap = {};
    var nfig = 0;

    // 1 Scheda
    (function () {
      var c = [H1(1, "Scheda del progetto")];
      c.push(tabella(["Voce", "Dato"], [2400, 6672], [
        ["Titolo", titolo], ["Autore", autore], ["Classe", classe],
        ["Repository GitHub", pieno(r.repo) ? r.repo : "non c'è ancora"], ["Data della prima versione", oggi]
      ]));
      c.push(spazio());
      c.push(H2("1.1 Descrizione"));
      c = c.concat(pieno(r.descr) ? testo(r.descr) : [seg("scrivi in 5 righe che cosa è il progetto.")]);
      c.push(H2("1.2 Obiettivo"));
      c = c.concat(pieno(r.obiettivo) ? testo(r.obiettivo) : [seg("scrivi che cosa vuoi ottenere.")]);
      c.push(H2("1.3 A chi serve"));
      c = c.concat(pieno(r.destinatari) ? testo(r.destinatari) : [seg("scrivi chi userà il progetto.")]);
      c.push(H2("1.4 Competenze richieste"));
      var sel = (r.comp || []), gruppi = window.PASSI[3].campi[0].gruppi, righeC = [];
      gruppi.forEach(function (g, gi) { g.voci.forEach(function (v, vi) { if (sel.indexOf(gi + "." + vi) >= 0) righeC.push(g.sigla + ": " + v); }); });
      if (pieno(r.comp_altro)) righeC.push("Altra competenza: " + pul(r.comp_altro).trim());
      c = c.concat(righeC.length ? elenco(righeC) : [seg("scegli le competenze dell'Allegato A che usi nel progetto.")]);
      c.push(H2("1.5 Formato di presentazione"));
      var fv = window.PASSI[12].campi[0].gruppi[0].voci, fs = [];
      (r.formati || []).forEach(function (i) { fs.push(fv[parseInt(i.split(".")[1], 10)]); });
      if (pieno(r.formato_altro)) fs.push(pul(r.formato_altro).trim());
      if (fs.length) {
        c.push(P("Formato: " + fs.join(", ") + "."));
        c.push(P("Durata: " + (pieno(r.durata) ? pul(r.durata).trim() + " minuti" : "da decidere") + "."));
        c = c.concat(pieno(r.mostro) ? [P("Che cosa mostrerò:")].concat(testo(r.mostro)) : [seg("scrivi che cosa mostrerai.")]);
      } else c.push(seg("scegli come presenterai il progetto (slide, video, poster, dimostrazione dal vivo, relazione scritta)."));
      cap[1] = c;
    })();

    // 2 Analisi e requisiti
    (function () {
      var c = [H1(2, "Analisi e requisiti")];
      var fa = righeVere(r.fa), nf = righeVere(r.nonfa);
      c.push(H2("2.1 Che cosa deve fare"));
      c = c.concat(fa.length ? [tabella(["Codice", "Il progetto deve..."], [1300, 7772], fa.map(function (x, i) { return ["R" + (i + 1), x.t]; })), spazio()] : [seg("scrivi le cose che il progetto deve fare, una per riga.")]);
      c.push(H2("2.2 Che cosa NON fa"));
      c = c.concat(nf.length ? elenco(nf.map(function (x) { return pul(x.t); })) : [seg("scrivi le cose che il progetto NON fa.")]);
      cap[2] = c;
    })();

    // 3 Piano e Gantt
    (function () {
      var c = [H1(3, "Piano di lavoro e Gantt")];
      var f = righeVere(r.fasi);
      if (ganttUrl) {
        var w = 600, h = Math.round(w * ganttDim.h / ganttDim.w);
        c.push(H2("3.1 Diagramma di Gantt"));
        c.push(new D.Paragraph({ alignment: D.AlignmentType.CENTER, keepNext: true, children: [new D.ImageRun({ data: bytes(ganttUrl), transformation: { width: w, height: h } })] }));
        nfig++; c.push(didascalia("Figura " + nfig + ": diagramma di Gantt delle fasi del lavoro."));
      }
      c.push(H2("3.2 Tabella delle fasi"));
      c = c.concat(f.length ? [tabella(["Fase", "Inizio", "Fine", "Materiale o risultato"], [3000, 1400, 1400, 3272], f.map(function (x) { return [x.f || "", dataIt(x.a), dataIt(x.b), x.m || ""]; })), spazio()] : [seg("scrivi le fasi del lavoro con le date di inizio e di fine.")]);
      cap[3] = c;
    })();

    // 4 Materiali e costi
    (function () {
      var c = [H1(4, "Materiali e costi")];
      var m = righeVere(r.mat);
      if (m.length) {
        var tot = 0, ok = false;
        var rows = m.map(function (x) {
          var q = num(x.q), p = num(x.p), t = (!isNaN(q) && !isNaN(p)) ? q * p : NaN;
          if (!isNaN(t)) { tot += t; ok = true; }
          return [x.c || "", isNaN(q) ? "" : String(x.q).trim(), isNaN(p) ? "" : euro(p), isNaN(t) ? "" : euro(t)];
        });
        rows.push(["Totale", "", "", ok ? euro(tot) : ""]);
        c.push(tabella(["Componente o materiale", "Quanti pezzi", "Prezzo di un pezzo (euro)", "Totale riga (euro)"], [3672, 1400, 2000, 2000], rows, { ultimaRiga: true, destra: [1, 2, 3] }));
        c.push(spazio());
      } else c.push(seg("scrivi i materiali, quanti pezzi e il prezzo di un pezzo."));
      cap[4] = c;
    })();

    // 5 Schema e progetto
    (function () {
      var c = [H1(5, "Schema e progetto")];
      c = c.concat(pieno(r.schema) ? testo(r.schema) : [seg("spiega come è fatto il progetto e come sono collegate le parti.")]);
      if (img.length) {
        img.forEach(function (im) {
          var w = Math.min(600, im.w), h = Math.round(w * im.h / im.w);
          c.push(new D.Paragraph({ alignment: D.AlignmentType.CENTER, keepNext: true, spacing: { before: 120 }, children: [new D.ImageRun({ data: bytes(im.d), transformation: { width: w, height: h } })] }));
          nfig++; c.push(didascalia("Figura " + nfig + (pieno(im.cap) ? ": " + pul(im.cap).trim() : ": da completare (scrivi che cosa si vede).")));
        });
      } else c.push(seg("aggiungi gli schemi, i disegni o le foto del progetto, con una didascalia."));
      cap[5] = c;
    })();

    // 6 Diario
    (function () {
      var c = [H1(6, "Realizzazione e diario")];
      var d = righeVere(r.diario);
      c = c.concat(d.length ? [tabella(["Data", "Che cosa ho fatto"], [1500, 7572], d.map(function (x) { return [dataIt(x.d), x.t || ""]; })), spazio()] : [seg("scrivi una riga per ogni giorno di lavoro: la data e che cosa hai fatto.")]);
      cap[6] = c;
    })();

    // 7 Prove
    (function () {
      var c = [H1(7, "Prove e collaudo")];
      var p = righeVere(r.prove);
      c = c.concat(p.length ? [tabella(["Prova", "Risultato atteso", "Risultato vero"], [3000, 3036, 3036], p.map(function (x) { return [x.p || "", x.a || "", x.v || "da provare"]; })), spazio()] : [seg("scrivi le prove: che cosa provi, che cosa ti aspetti e che cosa succede davvero.")]);
      cap[7] = c;
    })();

    // 8 Problemi
    (function () {
      var c = [H1(8, "Problemi e soluzioni")];
      var p = righeVere(r.prob);
      c = c.concat(p.length ? [tabella(["Problema", "Soluzione"], [4000, 5072], p.map(function (x) { return [x.p || "", x.s || ""]; })), spazio()] : [seg("scrivi i problemi che hai trovato e come li hai risolti.")]);
      cap[8] = c;
    })();

    // 9 Manuale
    (function () {
      var c = [H1(9, "Manuale utente")];
      var s = righeVere(r.man);
      if (pieno(r.man_serve)) { c.push(P("Che cosa serve per usarlo:", { run: { bold: true } })); c = c.concat(testo(r.man_serve)); }
      if (s.length) {
        c.push(P("I passi:", { run: { bold: true } }));
        s.forEach(function (x, i) { c.push(new D.Paragraph({ spacing: { after: 100 }, indent: { left: 500, hanging: 500 }, children: [T((i + 1) + ".  " + pul(x.t))] })); });
      } else c.push(seg("scrivi come si usa il progetto, un passo alla volta."));
      cap[9] = c;
    })();

    // 10 Sicurezza e privacy
    (function () {
      var c = [H1(10, "Sicurezza e privacy")];
      c.push(H2("10.1 Sicurezza"));
      c = c.concat(pieno(r.sic) ? testo(r.sic) : [seg("scrivi i rischi per la sicurezza e che cosa fai per proteggere.")]);
      c.push(H2("10.2 Privacy"));
      c = c.concat(pieno(r.priv) ? testo(r.priv) : [seg("scrivi se il progetto raccoglie dati di persone e come li proteggi.")]);
      cap[10] = c;
    })();

    // 11 Conclusioni
    (function () {
      var c = [H1(11, "Conclusioni e autovalutazione")];
      [["11.1 Conclusioni", "concl", "scrivi se il progetto fa quello che volevi."], ["11.2 Che cosa ha funzionato bene", "ok", "scrivi che cosa ha funzionato."],
       ["11.3 Che cosa farei in modo diverso", "meglio", "scrivi che cosa cambieresti."], ["11.4 Che cosa ho imparato e che cosa so fare adesso", "imparato", "scrivi che cosa hai imparato."]].forEach(function (x) {
        c.push(H2(x[0]));
        c = c.concat(pieno(r[x[1]]) ? testo(r[x[1]]) : [seg(x[2])]);
      });
      cap[11] = c;
    })();

    // 12 Fonti e allegati
    (function () {
      var c = [H1(12, "Fonti e allegati")];
      c.push(H2("12.1 Documentazione tecnica e scientifica"));
      var f = righeVere(r.fonti);
      c = c.concat(f.length ? [tabella(["Tipo", "Titolo", "Autore", "Anno", "Indirizzo o dove si trova"], [1500, 2400, 1500, 800, 2872], f.map(function (x) { return [x.tp || "", x.ti || "", x.au || "", x.an || "", x.ur || ""]; })), spazio()] : [seg("scrivi le fonti: siti, libri, schede tecniche, norme.")]);
      c.push(H2("12.2 Allegati"));
      c = c.concat(pieno(r.allegati) ? testo(r.allegati) : [seg("elenca i file o i link da allegare (codice, foto, schemi).")]);
      cap[12] = c;
    })();

    // copertina + versioni + indice
    var primo = [];
    primo.push(new D.Paragraph({ spacing: { before: 1800, after: 200 }, children: [T("Documento del progetto individuale", { size: 28, color: "5B6573" })] }));
    primo.push(new D.Paragraph({ heading: D.HeadingLevel.TITLE, spacing: { after: 300 }, children: [T(titolo)] }));
    primo.push(P("Autore: " + autore, { run: { size: 26 } }));
    primo.push(P("Classe: " + classe, { run: { size: 26 } }));
    primo.push(P("Data: " + oggi, { run: { size: 26 } }));
    primo.push(new D.Paragraph({ spacing: { before: 600, after: 120 }, children: [T("Versioni del documento", { bold: true, size: 24, color: AZZ })] }));
    primo.push(tabella(["Versione", "Data", "Autore", "Che cosa è cambiato"], [1300, 1600, 2600, 3572], [["0.1", oggi, autore, "Prima stesura, creata dalla procedura guidata."]]));
    primo.push(P("Ogni volta che cambi il Documento aggiungi una riga a questa tabella: versione 0.2, 0.3 e così via.", { run: { italics: true, size: 20 } }));
    primo.push(new D.Paragraph({ children: [new D.PageBreak()] }));
    primo.push(new D.Paragraph({ spacing: { after: 200 }, children: [T("Indice", { bold: true, size: 32, color: AZZ })] }));
    window.CAPITOLI.forEach(function (c) {
      primo.push(new D.Paragraph({ spacing: { after: 100 }, children: [new D.InternalHyperlink({ anchor: "cap" + c.n, children: [T(c.n + ". " + c.t, { color: AZZ, underline: {} })] })] }));
    });
    primo.push(P("Per avere i numeri di pagina: in Documenti Google scegli il menu «Inserisci», poi «Indice».", { run: { italics: true, size: 20 } }));
    primo.push(new D.Paragraph({ children: [new D.PageBreak()] }));

    var figli = primo;
    for (var i = 1; i <= 12; i++) figli = figli.concat(cap[i]);

    return new D.Document({
      creator: autore, title: "Documento del progetto: " + titolo, description: "Documento del progetto individuale, versione 0.1",
      styles: {
        default: {
          document: { run: { font: "Arial", size: 22 } },
          title: { run: { font: "Arial", size: 56, bold: true, color: "1D2433" } },
          heading1: { run: { font: "Arial", size: 32, bold: true, color: AZZ }, paragraph: { spacing: { before: 360, after: 160 }, keepNext: true } },
          heading2: { run: { font: "Arial", size: 26, bold: true, color: "1D2433" }, paragraph: { spacing: { before: 240, after: 120 }, keepNext: true } }
        }
      },
      sections: [{
        properties: { titlePage: true, page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } } },
        footers: {
          default: new D.Footer({ children: [new D.Paragraph({ alignment: D.AlignmentType.CENTER, children: [
            T(titolo + "   |   Pagina ", { size: 18, color: "5B6573" }),
            new D.TextRun({ children: [D.PageNumber.CURRENT], size: 18, color: "5B6573" }),
            T(" di ", { size: 18, color: "5B6573" }),
            new D.TextRun({ children: [D.PageNumber.TOTAL_PAGES], size: 18, color: "5B6573" })
          ] })] }),
          first: new D.Footer({ children: [new D.Paragraph({ children: [] })] })
        },
        children: figli
      }]
    });
  }

  window.GEN = {
    costruisci: costruisci, vuotoVal: vuotoVal, pieno: pieno, num: num, euro: euro, dataIt: dataIt,
    blob: function (S, ganttUrl, ganttDim, oggi) { return D.Packer.toBlob(costruisci(S, ganttUrl, ganttDim, oggi)); }
  };
})();
