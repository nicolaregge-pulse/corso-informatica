/* pagine.js - disegna le pagine usando carrello.js. Non serve cambiarlo. */

function esc(t) { return String(t).replace(/[&<>"']/g, function (c) { return "&#" + c.charCodeAt(0) + ";"; }); }
function foto(f) { return /\./.test(f) ? '<img src="' + esc(f) + '" alt="">' : esc(f); }   // file o emoji

function intestazione(pagina) {                 // nome del negozio e menu, uguali in tutte le pagine
  document.title = NEGOZIO;
  var voci = LINK_HOME ? [[LINK_HOME, "Il mio sito"]] : [];
  voci = voci.concat([["index.html", "Vetrina"], ["prodotti.html", "Prodotti"], ["carrello.html", "Carrello (" + pezzi() + ")"]]);
  document.getElementById("testata").innerHTML =
    '<a class="logo" href="index.html">' + foto(LOGO) + " " + esc(NEGOZIO) + "</a><nav>" +
    voci.map(function (v) { return '<a href="' + v[0] + '"' + (v[0] === pagina ? ' class="qui"' : "") + ">" + v[1] + "</a>"; }).join("") + "</nav>";
}

function mostraProdotti(dove, quanti) {         // le schede dei prodotti con il bottone «Aggiungi al carrello»
  var el = document.getElementById(dove);
  el.innerHTML = PRODOTTI.slice(0, quanti || PRODOTTI.length).map(function (p) {
    return '<article class="scheda"><div class="foto">' + foto(p.foto) + "</div><h3>" + esc(p.nome) + '</h3><p class="prezzo">' +
      euro(p.prezzo) + '</p><button class="grande" data-id="' + esc(p.id) + '">Aggiungi al carrello</button></article>';
  }).join("");
  el.onclick = function (e) {
    var id = e.target.getAttribute("data-id");
    if (!id) return;
    aggiungi(id);
    intestazione(document.body.getAttribute("data-pagina"));
    e.target.textContent = "Aggiunto ✓";
    setTimeout(function () { e.target.textContent = "Aggiungi al carrello"; }, 900);
  };
}

function mostraCarrello() {                     // l'elenco del carrello con quantità, totale, «Togli» e «Svuota»
  var r = righe(), el = document.getElementById("elenco");
  document.getElementById("vuoto").hidden = r.length > 0;
  document.getElementById("pieno").hidden = r.length === 0;
  el.innerHTML = r.map(function (x) {
    return "<tr><td>" + esc(x.nome) + "</td><td>" + euro(x.prezzo) + '</td><td class="q">' +
      '<button data-az="meno" data-id="' + esc(x.id) + '" aria-label="Meno">−</button> <b>' + x.q +
      '</b> <button data-az="piu" data-id="' + esc(x.id) + '" aria-label="Più">+</button></td><td>' + euro(x.somma) +
      '</td><td><button data-az="togli" data-id="' + esc(x.id) + '">Togli</button></td></tr>';
  }).join("");
  document.getElementById("totale").textContent = euro(totale());
  intestazione("carrello.html");
}

function leggiModulo() {                        // controlla nome ed email di PROVA e crea l'ordine
  var nome = document.getElementById("nome").value.trim(), email = document.getElementById("email").value.trim();
  var errore = document.getElementById("errore");
  errore.textContent = "";
  if (righe().length === 0) { errore.textContent = "Il carrello è vuoto: aggiungi un prodotto."; return null; }
  if (nome === "") { errore.textContent = "Scrivi un nome di prova (non il tuo nome vero)."; return null; }
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { errore.textContent = "Scrivi un'email di prova, per esempio: prova@esempio.example"; return null; }
  return { nome: nome, email: email, righe: righe(), totale: totale(), numero: "N" + (Date.now() % 100000) };
}

function confermaOrdine() {                     // salva l'ordine, svuota il carrello e va alla pagina della finta email
  var ordine = leggiModulo();
  if (!ordine) return;
  salva("ordine", ordine);
  svuota();
  location.href = "conferma.html";
}

function corpoEmail(o) {                        // il testo della email: saluto, elenco, totale
  var t = "Ciao " + o.nome + ",\n" + TESTO_EMAIL + "\n\nOrdine " + o.numero + ":\n";
  o.righe.forEach(function (r) { t += "- " + r.nome + ": " + r.q + " x " + euro(r.prezzo) + " = " + euro(r.somma) + "\n"; });
  return t + "\nTotale: " + euro(o.totale) + "\n\n" + NEGOZIO;
}

function mostraConferma() {                     // la finta email a video
  var o = leggi("ordine", null);
  intestazione("");
  document.getElementById("senza").hidden = !!o;
  document.getElementById("con").hidden = !o;
  if (!o) return;
  document.getElementById("da").textContent = NEGOZIO + " <" + MITTENTE + ">";
  document.getElementById("a").textContent = o.email;
  document.getElementById("oggetto").textContent = "Il tuo ordine " + o.numero;
  document.getElementById("corpo").textContent = corpoEmail(o);
  document.getElementById("mailto").href = "mailto:" + encodeURIComponent(o.email) + "?subject=" +
    encodeURIComponent("Il tuo ordine " + o.numero) + "&body=" + encodeURIComponent(corpoEmail(o));
}

function nuovoOrdine() { salva("ordine", null); location.href = "prodotti.html"; }
