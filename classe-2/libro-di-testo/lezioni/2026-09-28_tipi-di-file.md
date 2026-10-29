# I tipi di file

**Versione 1.0** — 29/10/2026
*Libro parziale della 2INF: la lezione del 28/09/2026. Fa parte del libro di testo della classe (libro-classe2). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 28/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Che cos'è un file, l'estensione, file di testo e file binari, il dizionario dei formati, la compressione; compito sui tipi di file.

### La teoria e l'esercitazione

Dispensa · Classe 2 · Informatica · v1.1

### I tipi di file

a cosa servono, gli esempi, i file "a tag", video e compressione

Ogni file ha un **tipo** (lo dice l'estensione: .md, .mp4…). Capire i tipi serve a sapere **cosa contiene** un file, **con che programma** si apre e **perché** pesa tanto o poco. Con esempi da mondi diversi.

#### Di cosa parliamo

**1.** Cos'è un file e a cosa serve l'estensione
**2.** Le grandi famiglie di file (testo, immagini, audio, video, archivi…)
**3.** Dizionario dei formati (uno per uno, con esempio)
**4.** I file "a TAG": HTML, XML, MD — con esempi veri
**5.** La compressione: perché un file diventa più piccolo
**6.** Il Markdown (MD) e l'intelligenza artificiale
**7.** Glossario

#### 1. Cos'è un file e a cosa serve l'estensione

Un **file** è un contenitore di informazioni salvato nel computer: un testo, una foto, una canzone, un video, un programma. Ogni file ha un **nome** e, alla fine, un'**estensione**: le lettere dopo il punto (es. canzone.mp3, foto.jpg).

**L'estensione è come il "cognome" del file:** dice di che **tipo** è, così il computer sa **con quale programma** aprirlo. Cambiare l'estensione non cambia il contenuto: rinominare foto.jpg in foto.txt non la trasforma in testo, la fa solo aprire con il programma sbagliato.

**Esempio quotidiano.** È come le **etichette** sui barattoli in cucina: "zucchero", "sale". Il contenuto è dentro; l'etichetta ti dice cosa aspettarti e come usarlo.

##### Il percorso (path): dove si trova il file

Oltre al tipo, un file ha un **indirizzo** nel computer: il **percorso** (in inglese **path**), cioè la lista di cartelle per arrivarci, es. C:\Documenti\Scuola\appunti.txt. Su Windows le cartelle si separano con la barra rovescia \ — è un'eredità del vecchio sistema **DOS**, dove tutto si scriveva a mano (es. C:\DOS).

#### 2. Due grandi mondi: TESTO e BINARIO

La prima grande divisione (come alla lavagna) è tra file di **testo** e file **binari**.

1. **File di TESTO (TXT):** dentro ci sono solo **lettere e simboli**, quindi li puoi aprire col **Blocco note** e **leggerli**. Sono a "formato libero". Esempi: txt, md, html, css, js, xml, csv, json, .gd.
2. **File BINARI (BIN):** dentro ci sono **codici** che il Blocco note non sa mostrare (escono simboli strani): servono **programmi specifici**. Esempi: doc, xls, pdf, dwg, png, jpeg, zip, exe, mp3, mp4, wav.

**Prova del nove.** Per sapere se un file è testo o binario, aprilo col **Blocco note**: se lo **leggi** è testo; se vedi **simboli strani** è binario.

##### Le famiglie più in dettaglio

Dentro questi due mondi ci sono le **famiglie** per uso:

| Famiglia | A cosa serve | Esempi di estensione |
| --- | --- | --- |
| **Testo semplice** | solo lettere, nessuna formattazione | .txt .md |
| **Testo "a tag"** | testo con etichette che danno struttura | .html .xml |
| **Dati / tabelle** | elenchi e tabelle di dati | .csv .json |
| **Documenti impaginati** | testo formattato, pronto da leggere/stampare | .pdf .docx .xlsx |
| **Immagini** | foto e disegni | .jpg .png |
| **Audio / Video** | suoni e filmati | .mp3 .mp4 .wav |
| **Archivi** | tanti file compressi in uno solo | .zip |
| **Pagine web** | struttura, stile e comportamento dei siti | .html .css .js |
| **Disegno tecnico (CAD)** | disegni e progetti tecnici | .dwg |
| **Programmi (eseguibili)** | si avviano col doppio clic | .exe |
| **Codice / progetto** | istruzioni per un programma | .gd (Godot) .py |

#### 3. Dizionario dei formati (uno per uno)

Per ognuno: **a cosa serve**, un **esempio**, e **con che programma si apre** (a scuola: Blocco note, browser, Godot portabile, SumatraPDF).

##### TXT — testo semplice

Solo testo, senza grassetti né colori. Leggerissimo. Si apre col **Blocco note**. Esempio: una lista della spesa, degli appunti veloci.

##### MD (Markdown) — testo con formattazione "leggera"

Testo semplice ma con simboli che diventano formattazione: # = titolo, \*\*...\*\* = grassetto. È il formato con cui scriviamo le dispense (poi diventano PDF). Si legge su GitHub o col Blocco note.

##### HTML — la pagina web

Il linguaggio delle **pagine dei siti**. Usa i **tag** (vedi §4). Lo apre il **browser**, che trasforma i tag in una pagina bella da vedere.

##### XML — dati con etichette

Come HTML usa i tag, ma per **organizzare dati** (non per fare pagine). Tanti programmi si scambiano informazioni in XML.

##### CSV — tabella semplice

Una tabella scritta come testo: ogni riga è una riga della tabella, le colonne separate da **virgole** (comma). Lo aprono Excel/Fogli Google. Esempio: l'esportazione dei voti di un quiz.

##### JSON — dati per i programmi

Come CSV ma per dati più complessi (a "scatole dentro scatole"). È il modo con cui le app si scambiano dati su Internet.

##### PDF — il documento "congelato"

Un documento impaginato che si vede **uguale ovunque** e si stampa bene, ma non si modifica facilmente. Si apre con **SumatraPDF** o il browser. Le nostre dispense finali sono PDF.

##### DOCX / XLSX — Word ed Excel

Documento di testo (DOCX) e foglio di calcolo (XLSX). Servono per **scrivere e modificare**. Li aprono Word/Excel o Documenti/Fogli Google.

##### JPG / PNG — le immagini

**JPG**: foto, molto compresse (leggere, ma perdono un po' di qualità). **PNG**: disegni/loghi, senza perdita e con sfondo trasparente. Le apre qualsiasi visualizzatore o il browser.

##### MP3 / MP4 — audio e video

**MP3** = audio compresso. **MP4** = video (immagini in movimento + audio insieme). Li apre il lettore multimediale o il browser.

##### ZIP — l'archivio

Una **valigia**: mette tanti file dentro uno solo e li **comprime** per pesare meno e spedirli comodi. Si "estrae" per riavere i file dentro.

##### CSS / JS — stile e comportamento delle pagine

Vanno insieme all'HTML: **CSS** dà lo **stile** (colori, caratteri, posizioni), **JS** (JavaScript) dà il **comportamento** (bottoni che fanno cose). Sono testo, li apre il Blocco note; il browser li usa con l'HTML.

##### DWG — il disegno tecnico (CAD)

Il formato dei **disegni tecnici** fatti con programmi CAD (es. AutoCAD): piantine, progetti. È binario, serve il programma giusto per aprirlo.

##### EXE — il programma da avviare

Un **programma eseguibile**: col doppio clic **parte**. Godot portabile è un .exe. Attenzione: aprire un .exe che non conosci è rischioso (può contenere virus).

##### WAV — audio senza compressione

Audio di qualità piena ma **pesante** perché **non compresso** (a differenza dell'MP3). Si usa quando serve la massima qualità.

##### GD — lo script di Godot

Un file di **codice**: le istruzioni del nostro gioco in Godot. È testo, ma lo apre **Godot** (col doppio clic parte il gioco: per leggerlo come testo, tasto destro → Apri con → Blocco note).

#### 4. I file "a TAG": HTML, XML, MD

Alcuni file di testo usano i **tag** (etichette). Un **tag** è un'etichetta tra parentesi angolari che **marca** un pezzo di testo dicendo "questo è un titolo", "questo è grassetto". Di solito vanno a coppie: uno apre &lt;titolo> e uno chiude &lt;/titolo>.

**Analogia.** I tag sono come gli **evidenziatori e le note a margine** su un foglio: il testo è lo stesso, ma le marcature dicono a cosa serve ogni parte.

##### Esempio HTML (pagina web)

&lt;h1>La mia prima pagina&lt;/h1>
&lt;p>Ciao, questo è un &lt;b>paragrafo&lt;/b> in grassetto.&lt;/p>
&lt;a href="github.com">vai a GitHub&lt;/a>

&lt;h1> = titolo grande · &lt;p> = paragrafo · &lt;b> = grassetto · &lt;a> = link. Il browser legge questi tag e disegna la pagina.

##### Esempio XML (dati)

&lt;studente>
&lt;nome>Mario&lt;/nome>
&lt;classe>3 INF&lt;/classe>
&lt;voto>90&lt;/voto>
&lt;/studente>

Qui i tag non servono a fare una pagina, ma a **organizzare i dati**: si capisce quale pezzo è il nome, quale la classe, quale il voto.

##### Esempio MD (Markdown)

### Titolo grande
#### Sottotitolo
Testo normale con una parola in \*\*grassetto\*\*.
- primo punto
- secondo punto

Il Markdown non usa parentesi angolari ma **simboli leggeri** (#, \*\*, -): più veloce da scrivere a mano, poi un programma lo trasforma in PDF o pagina.

**In comune:** tutti e tre sono **testo** (li apre anche il Blocco note), ma con **marcature** che danno **struttura**. Cambia solo il "dialetto": angolari per HTML/XML, simboli per MD.

#### 5. La compressione: perché un file diventa più piccolo

**Comprimere** vuol dire scrivere la stessa informazione occupando **meno spazio**. Serve a far pesare meno i file (per salvarli, inviarli, metterli online). Ci sono due modi:

1. **Senza perdita (lossless):** si comprime ma si può tornare **identici** all'originale. È come **piegare bene** un vestito nella valigia: occupa meno, ma è lo stesso vestito. Esempi: .zip, .png.
2. **Con perdita (lossy):** si butta via un po' di dettaglio che quasi non si nota, per pesare **molto** meno. È come **riassumere** un tema: perdi qualche parola ma il senso resta. Esempi: .jpg, .mp3, .mp4.

**Esempio concreto.** La stessa foto: in **PNG** senza perdita può pesare 8 MB; in **JPG** con perdita 0,8 MB — dieci volte meno, e a occhio quasi uguale. Per una foto sul telefono va benissimo il JPG; per un logo con linee nette meglio il PNG.

**Perché ci riguarda:** un video lungo non compresso peserebbe **giga e giga**; grazie all'MP4 (compressione con perdita) sta in pochi MB e si guarda in streaming. È lo stesso motivo per cui abbiamo **compresso l'immagine** nelle dispense: pesare meno senza perdere qualità utile.

#### 6. Il Markdown (MD) e l'intelligenza artificiale

C'è un motivo se vi diamo le dispense anche in **MD** (Markdown), oltre che in PDF: il Markdown è il formato **perfetto da dare a un'intelligenza artificiale** (come Gemini o ChatGPT) per farsi **spiegare** o **tradurre** un testo.

##### Perché l'AI legge bene un MD

1. **È testo puro:** l'AI legge **esattamente** il contenuto, senza la "sporcizia" nascosta di un PDF o di un DOCX (che dentro hanno codici di formattazione, e da binari sono illeggibili).
2. **La struttura è chiara:** i simboli del Markdown (# titolo, \*\* grassetto, - elenco) dicono all'AI **com'è organizzato** il testo, così capisce cosa è titolo, cosa è elenco, cosa è importante.
3. **È leggero:** si **copia e incolla** facilmente dentro una chat con l'AI.

**Analogia.** Dare all'AI un MD è come darle un foglio **pulito e ordinato** invece di uno pieno di scarabocchi e formattazioni strane: lo capisce molto meglio.

**Come lo usate voi:** prendete il file .md della dispensa, lo **date alla vostra AI** e le chiedete, ad esempio: "*spiegamelo in modo semplice*" oppure "*traducilo nella mia lingua*". Così ognuno ripassa la lezione **come e nella lingua che preferisce**.

**Regola d'uso dell'AI:** serve per **capire meglio**, non per saltare il ragionamento. La prova che hai capito è **saperlo spiegare a voce, con parole tue**.

#### 7. Glossario

| Parola | Vuol dire |
| --- | --- |
| file | un contenitore di informazioni salvato nel computer |
| percorso (path) | l'indirizzo del file nel computer (es. C:\cartella\file.txt) |
| file di testo | leggibile col Blocco note (txt, md, html, css, js, xml, csv…) |
| file binario | serve un programma specifico (doc, pdf, png, mp4, exe, zip…) |
| estensione | le lettere dopo il punto: dicono il tipo del file (.mp4, .md…) |
| tag | un'etichetta (es. &lt;titolo>) che marca un pezzo di testo |
| HTML | il linguaggio a tag delle pagine web |
| XML | testo a tag per organizzare dati |
| Markdown (MD) | testo con simboli leggeri per la formattazione |
| CSV | tabella scritta come testo, colonne separate da virgole |
| MP4 | formato video (immagini in movimento + audio, compressi) |
| compressione | scrivere la stessa informazione occupando meno spazio |
| lossless / lossy | senza perdita (identico) / con perdita (più leggero) |
| ZIP | archivio: tanti file compressi in uno solo |

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
