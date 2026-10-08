// Service worker del Treno blindato: il gioco si installa come app (telefono e Chrome su PC) e parte anche senza rete.
// Strategia: prima la rete (così i pezzi nuovi della classe arrivano subito), se manca la rete la copia salvata.
const CACHE = "treno3inf-v1";
self.addEventListener("install", e => { self.skipWaiting(); e.waitUntil(caches.open(CACHE).then(c => c.addAll(["./", "index.html", "manifest.webmanifest", "img/copertina.jpg", "img/icona-192.png"]))); });
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(fetch(new Request(e.request.url, { cache: "no-cache" })).then(r => { const k = r.clone(); caches.open(CACHE).then(c => c.put(e.request.url.split("?")[0], k)); return r; })
    .catch(() => caches.match(e.request.url.split("?")[0])));
});
