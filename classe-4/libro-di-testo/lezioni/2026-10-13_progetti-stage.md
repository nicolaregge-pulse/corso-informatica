# I progetti di stage su GitHub

**Versione 1.0** — 29/10/2026
*Libro parziale della 4TI: la lezione del 13/10/2026. Fa parte del libro di testo della classe (libro-classe4). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 13/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Avvio dei progetti di stage individuali su GitHub (per esempio un automa meteo in Python, un router-firewall virtuale): prima capire, poi scrivere il codice.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Che cos'è un automa

<div class="scheda">Un <b>automa</b> è un programma che fa da solo un lavoro che si ripete: legge un dato, lo salva, lo mostra, poi aspetta e ricomincia. I sistemi di controllo delle fabbriche e dei laboratori (come <b>EPICS</b>) sono fatti così, in grande: <b>sorgente dei dati → automa → storico → pannello di controllo</b>. Il tuo progetto ha gli stessi quattro blocchi.</div>

#### 2. API REST e JSON

<div class="scheda">Una <b>API REST</b> è un indirizzo web che invece di una pagina restituisce <b>dati</b>. Open-Meteo risponde in <b>JSON</b>: testo con parentesi graffe, fatto di coppie <i>nome: valore</i>, una dentro l'altra come cassetti in un armadio. In Python <code>json.loads()</code> trasforma quel testo in un dizionario, e <code>dati["current_weather"]["temperature"]</code> apre il cassetto «current_weather» e prende «temperature».</div>

#### 3. Funzioni, return e None

<div class="scheda">Una <b>funzione</b> (<code>def</code>) è un pezzo di programma con un nome, che si richiama quando serve. Con <code>return</code> restituisce un risultato a chi l'ha chiamata. I <b>parametri</b>, tra le parentesi, sono i dati che riceve: <code>vento=None</code> vuol dire «se non me lo dai, vale None». <b>None</b> vuol dire «niente»: lo si usa quando un dato manca, per esempio se Internet non risponde (<code>try</code> / <code>except</code>).</div>

#### 4. Lo storico: file CSV

<div class="scheda">Un <b>CSV</b> è un file di testo a tabella: una riga per lettura, le colonne separate da <code>;</code>. Si apre con Excel. Aprendo il file in modalità <code>"a"</code> (append) si aggiunge in fondo senza cancellare. In Excel italiano i decimali vogliono la <b>virgola</b>: con il punto, 18.9 diventa testo e non si può fare la media.</div>

#### 5. Il ciclo e il tempo

<div class="scheda"><code>while True:</code> ripete per sempre; <code>time.sleep(60)</code> aspetta 60 secondi. Il computer che esegue il programma può avere un altro fuso orario: con <code>ZoneInfo("Europe/Rome")</code> si usa l'ora italiana.</div>

#### 6. La dashboard: Python scrive una pagina web

<div class="scheda">Una pagina web è solo testo HTML. Python la costruisce con una <b>f-string</b> (<code>f"...{temperatura}..."</code>), che mette i valori al posto giusto, e la scrive in <code>index.html</code>. <code>&lt;meta charset="utf-8"&gt;</code> serve perché simboli come «°» si vedano bene.</div>

#### 7. GitHub Actions e Pages

<div class="scheda"><b>GitHub Actions</b> esegue il tuo programma da solo, agli orari scritti nel file <code>.github/workflows/automa.yml</code> (ogni 30 minuti), anche a computer spento, e salva i risultati con un commit. <b>GitHub Pages</b> pubblica la cartella <code>docs</code> come sito: la dashboard si apre anche dal telefono.</div>

#### 8. LA PRATICA: costruisci il tuo automa

<div class="scheda">La pratica è il <b>percorso a tappe</b> nel tuo deposito: scrivi l'automa da zero, nella cartella <code>mio-automa/</code>, un pezzo alla volta, con gli aiuti a livelli e senza codice da copiare. Ogni tappa: funziona + commit + la sai spiegare nella chat del progetto.<br><a href="https://github.com/chasedeleon/automa-meteo-python/blob/main/documenti/PERCORSO.md" target="_blank"><b>Apri il percorso a tappe</b></a> · <a href="https://colab.research.google.com" target="_blank">Apri Google Colab</a> · <a href="https://github.com/chasedeleon/automa-meteo-python/pulls" target="_blank">La chat del progetto</a></div>


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
