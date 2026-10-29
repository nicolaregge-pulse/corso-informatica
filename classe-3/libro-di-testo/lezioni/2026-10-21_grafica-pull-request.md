# Struttura del sito, CSS e lavoro in coppia

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 21/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 21/10/2026, 2 ore, Laboratorio.
2. **Argomenti:** Albero del sito, nomi giusti, cartella img, immagine di sfondo, animazione con transition e @keyframes, numero di versione; invito come collaboratore, ramo, Pull Request e merge sul sito del compagno; quiz su Moduli.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Prima di tutto: il sito in ordine

<div class="scheda">Un sito funziona solo se i file sono <b>nel posto giusto</b> e con il <b>nome giusto</b>. Nella cartella principale del repository servono:<br><code>index.html</code> · <code>style.css</code> · <code>competenze.html</code> · <code>passione.html</code> · la cartella <code>img</code> con le tue immagini.<br><br>Apri <a href="../3inf-albero/" target="_blank" rel="noopener">L'albero del mio sito</a>, scrivi l'indirizzo del tuo sito e premi <b>Controlla</b>. Sistema le croci rosse <b>una alla volta</b> finché è tutto verde. Questo è il primo traguardo di oggi.</div>

#### 2. Le tre regole dei nomi

<div class="scheda">1) <b>Tutto minuscolo</b>: GitHub distingue <code>Index.html</code> da <code>index.html</code>: per lui sono due file diversi, e il link non funziona.<br>2) <b>Niente spazi</b>: <code>mia foto.jpg</code> no, <code>mia-foto.jpg</code> sì.<br>3) <b>Il collegamento uguale al nome, lettera per lettera</b>: se il file è <code>sfondo.jpeg</code>, nel CSS scrivi <code>sfondo.jpeg</code>, non <code>sfondo.jpg</code>.<br><br>Per rinominare su GitHub: apri il file, matita, cambia il nome in alto, <b>Commit changes</b>. Per spostarlo nella cartella img scrivi <code>img/</code> davanti al nome.</div>

#### 3. Un'immagine di sfondo

<div class="scheda">Carica la tua immagine: <b>Add file → Upload files</b>, poi rinominala in <code>img/sfondo.jpg</code>. Poi in <code>style.css</code>, dentro <code>body { }</code>, aggiungi:<pre>background-image: url("img/sfondo.jpg"); background-size: cover; background-attachment: fixed;</pre>Se il testo non si legge bene, metti il contenuto in un riquadro semitrasparente:<pre>main { background: rgba(255,255,255,0.85); padding: 20px; border-radius: 12px; }</pre>L'immagine la scegli tu: è il tuo sito.</div>

#### 4. Una piccola animazione

<div class="scheda"><b>Transition</b>: un cambiamento morbido quando passi sopra con il mouse.<pre>nav a { transition: transform 0.3s; } nav a:hover { transform: scale(1.15); }</pre><b>@keyframes</b>: un'animazione che parte da sola, per esempio il titolo che entra piano.<pre>@keyframes entra {   from { opacity: 0; transform: translateY(-20px); }   to   { opacity: 1; transform: translateY(0); } } h1 { animation: entra 1s ease; }</pre>Poche animazioni e leggere: un sito che si muove troppo stanca chi lo guarda.</div>

#### 5. A coppie: ramo, Pull Request, merge

<div class="scheda">Ora lavori sul sito del compagno, come in un'azienda.<br>1) Il compagno ti aggiunge come <b>collaboratore</b>: Settings → Collaborators → Add people.<br>2) Tu, nel suo repository, apri un file, matita, e in basso scegli <b>Create a new branch</b> (un ramo: la tua copia per provare). Aggiungi una sezione «Il mio compagno di lavoro»: tre righe su di lui e un consiglio per il suo sito.<br>3) Premi <b>Propose changes</b> e poi <b>Create pull request</b>.<br>4) Il compagno apre la Pull Request, guarda le modifiche e preme <b>Merge pull request</b>. Il suo sito ora ha la tua sezione!<br>Poi vi scambiate i ruoli.</div>

#### 6. Il numero di versione

<div class="scheda">Nel piè di pagina di <code>index.html</code> scrivi la versione: <code>&lt;footer&gt;Versione 1.0&lt;/footer&gt;</code>.<br>Ogni Pull Request accettata che aggiunge qualcosa fa salire il secondo numero: <b>1.0 → 1.1 → 1.2</b>. Il primo numero sale solo per un cambiamento grande (un sito tutto nuovo: 2.0).<br><b>Sfida finale</b>: tutti e due cambiate la <b>stessa riga</b> del titolo in due rami diversi. GitHub dice <b>conflitto</b>: scegliete insieme quale tenere (Resolve conflicts), poi merge. Avete risolto il vostro primo conflitto, come i programmatori veri.</div>


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
