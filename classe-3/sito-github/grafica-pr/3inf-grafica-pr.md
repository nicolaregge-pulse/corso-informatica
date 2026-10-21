# Il mio sito: in ordine, più bello, e lavoro in coppia

**Versione 1.0** — 21/10/2026 · 3INF · 21/10/2026 · struttura, sfondo, animazioni, Pull Request e versioni

La pagina della lezione, con il ripasso: https://nicolaregge-pulse.github.io/corso-informatica/verifica/?b=3inf-grafica-pr

## 01 Prima di tutto: il sito in ordine

Un sito funziona solo se i file sono **nel posto giusto** e con il **nome giusto**. Nella cartella principale del repository servono:
`index.html` · `style.css` · `competenze.html` · `passione.html` · la cartella `img` con le tue immagini.

Apri L'albero del mio sito (../3inf-albero/), scrivi l'indirizzo del tuo sito e premi **Controlla**. Sistema le croci rosse **una alla volta** finché è tutto verde. Questo è il primo traguardo di oggi.

## 02 Le tre regole dei nomi

1) **Tutto minuscolo**: GitHub distingue `Index.html` da `index.html`: per lui sono due file diversi, e il link non funziona.
2) **Niente spazi**: `mia foto.jpg` no, `mia-foto.jpg` sì.
3) **Il collegamento uguale al nome, lettera per lettera**: se il file è `sfondo.jpeg`, nel CSS scrivi `sfondo.jpeg`, non `sfondo.jpg`.

Per rinominare su GitHub: apri il file, matita, cambia il nome in alto, **Commit changes**. Per spostarlo nella cartella img scrivi `img/` davanti al nome.

## 03 Un'immagine di sfondo

Carica la tua immagine: **Add file → Upload files**, poi rinominala in `img/sfondo.jpg`. Poi in `style.css`, dentro `body { }`, aggiungi:
```
background-image: url("img/sfondo.jpg");
background-size: cover;
background-attachment: fixed;
```
Se il testo non si legge bene, metti il contenuto in un riquadro semitrasparente:
```
main { background: rgba(255,255,255,0.85); padding: 20px; border-radius: 12px; }
```
L'immagine la scegli tu: è il tuo sito.

## 04 Una piccola animazione

**Transition**: un cambiamento morbido quando passi sopra con il mouse.
```
nav a { transition: transform 0.3s; }
nav a:hover { transform: scale(1.15); }
```
**@keyframes**: un'animazione che parte da sola, per esempio il titolo che entra piano.
```
@keyframes entra {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}
h1 { animation: entra 1s ease; }
```
Poche animazioni e leggere: un sito che si muove troppo stanca chi lo guarda.

## 05 A coppie: ramo, Pull Request, merge

Ora lavori sul sito del compagno, come in un'azienda.
1) Il compagno ti aggiunge come **collaboratore**: Settings → Collaborators → Add people.
2) Tu, nel suo repository, apri un file, matita, e in basso scegli **Create a new branch** (un ramo: la tua copia per provare). Aggiungi una sezione «Il mio compagno di lavoro»: tre righe su di lui e un consiglio per il suo sito.
3) Premi **Propose changes** e poi **Create pull request**.
4) Il compagno apre la Pull Request, guarda le modifiche e preme **Merge pull request**. Il suo sito ora ha la tua sezione!
Poi vi scambiate i ruoli.

## 06 Il numero di versione

Nel piè di pagina di `index.html` scrivi la versione: `<footer>Versione 1.0</footer>`.
Ogni Pull Request accettata che aggiunge qualcosa fa salire il secondo numero: **1.0 → 1.1 → 1.2**. Il primo numero sale solo per un cambiamento grande (un sito tutto nuovo: 2.0).
**Sfida finale**: tutti e due cambiate la **stessa riga** del titolo in due rami diversi. GitHub dice **conflitto**: scegliete insieme quale tenere (Resolve conflicts), poi merge. Avete risolto il vostro primo conflitto, come i programmatori veri.

## 07 Che cosa fare oggi

1. Leggi le 6 schede sulla pagina della lezione.
2. Metti in ordine il sito con L'albero del mio sito: https://nicolaregge-pulse.github.io/corso-informatica/3inf-albero/
3. A coppie: sfondo, animazione, Pull Request sul sito del compagno, merge e versione.
4. Fai il quiz su Google Moduli (link su Classroom) e premi Invia.
