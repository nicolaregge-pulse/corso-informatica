/* carrello.js - il cervello del negozio (solo HTML, CSS e JavaScript: nessun server, nessun servizio esterno).
   PARTE 1: qui sotto ci sono i punti che cambi tu per fare IL TUO negozio. Cambia solo il testo tra le virgolette. */

var NEGOZIO = "Il Negozio di Prova";            // 1) il nome del negozio
var LOGO = "🛍️";                                // 5) un'immagine: un emoji, oppure il nome di un file (es. "logo.png")
var PRODOTTI = [                                // 3) i tuoi 3 prodotti: id (unico), nome, prezzo in euro, foto (emoji o file)
  { id: "zaino",  nome: "Zaino blu",    prezzo: 25, foto: "🎒" },
  { id: "cuffie", nome: "Cuffie nere",  prezzo: 40, foto: "🎧" },
  { id: "penna",  nome: "Penna verde",  prezzo: 2.5, foto: "🖊️" }
];
var TESTO_EMAIL = "Grazie per il tuo ordine! Lo prepariamo subito.";   // 4) il testo della email di conferma
var MITTENTE = "ordini@nome-del-tuo-negozio.example";   // indirizzo FINTO (.example è riservato agli esempi): non scrivere un indirizzo vero
var LINK_HOME = "../index.html";                 // dove porta il menu «Il mio sito» (la home di mio-sito, una cartella sopra). Vuoto = niente link
// 2) i colori si cambiano in stile.css (la riga --colore)

/* PARTE 2: il carrello. Non serve cambiarla: puoi leggerla per capire come funziona. */

function leggi(chiave, base) {                  // legge dalla memoria del browser (localStorage)
  try { return JSON.parse(localStorage.getItem(chiave)) || base; } catch (e) { return base; }
}
function salva(chiave, valore) {                // scrive nella memoria del browser
  try { localStorage.setItem(chiave, JSON.stringify(valore)); } catch (e) { /* memoria non disponibile */ }
}
function euro(n) { return n.toFixed(2).replace(".", ",") + " €"; }
function trova(id) { return PRODOTTI.filter(function (p) { return p.id === id; })[0]; }

var carrello = leggi("carrello", {});           // un oggetto: { "zaino": 2, "penna": 1 }  (id -> quantità)

function aggiungi(id) { carrello[id] = (carrello[id] || 0) + 1; salva("carrello", carrello); }
function cambia(id, delta) {                    // +1 o -1; a zero il prodotto sparisce
  carrello[id] = (carrello[id] || 0) + delta;
  if (carrello[id] <= 0) delete carrello[id];
  salva("carrello", carrello);
}
function togli(id) { delete carrello[id]; salva("carrello", carrello); }
function svuota() { carrello = {}; salva("carrello", carrello); }

function righe() {                              // l'elenco delle righe del carrello, con il totale di ogni riga
  return Object.keys(carrello).filter(trova).map(function (id) {
    var p = trova(id);
    return { nome: p.nome, prezzo: p.prezzo, q: carrello[id], id: id, somma: Math.round(p.prezzo * carrello[id] * 100) / 100 };
  });
}
function totale() { return righe().reduce(function (t, r) { return Math.round((t + r.somma) * 100) / 100; }, 0); }
function pezzi() { return righe().reduce(function (t, r) { return t + r.q; }, 0); }
