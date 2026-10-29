# Il sito diventa portfolio

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 19/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 19/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Ripasso di HTML5, CSS3 e GitHub Pages; la pagina competenze.html «Cosa so fare» con menu e link nella Home; verifica e recupero.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Dove siamo: il tuo sito · ১. আমরা কোথায় আছি

<div class="scheda">Hai già un <b>sito pubblico</b> su Internet: lo hai fatto tu, dall'8 ottobre. Sta in un <b>repository</b> su GitHub (quasi tutti lo hanno chiamato <b>mio-sito</b>) e ha dentro almeno due file: <b>index.html</b> (la pagina) e <b>style.css</b> (i colori e lo stile). Chi ha fatto la Dispensa 4 ha anche una <b>seconda pagina</b> e un <b>menu</b> per passare da una pagina all'altra. L'indirizzo è <b>https://tuonome.github.io/mio-sito/</b>. Oggi il sito diventa il tuo <b>portfolio</b>: una pagina che dice <b>cosa sai fare</b>, da mostrare a un'azienda per lo stage. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">তোমার একটি ওয়েবসাইট আছে, GitHub-এ <b>mio-sito</b> নামে। আজ এটি তোমার <b>portfolio</b> হবে: কী কী পারো, কোম্পানিকে দেখানোর জন্য।</span></div>

#### 2. Ripasso HTML: i mattoni della pagina · ২. HTML

<div class="scheda"><b>HTML</b> è la lingua delle pagine web. Ogni pezzo sta tra due <b>tag</b>: uno apre <code>&lt;p&gt;</code>, uno chiude <code>&lt;/p&gt;</code>. Quelli che usi tu:<br><code>&lt;h1&gt;</code> titolo grande · <code>&lt;h2&gt;</code> titolo piccolo · <code>&lt;p&gt;</code> paragrafo (un pezzo di testo) · <code>&lt;ul&gt;</code> elenco, con dentro un <code>&lt;li&gt;</code> per ogni riga · <code>&lt;a href="pagina.html"&gt;Testo&lt;/a&gt;</code> link, cioè un collegamento a un'altra pagina · <code>&lt;div class="scheda"&gt;</code> una scatola che raggruppa.<br>La pagina ha una <b>testa</b> <code>&lt;head&gt;</code> (il titolo della scheda del browser e il collegamento al CSS) e un <b>corpo</b> <code>&lt;body&gt;</code> (tutto quello che si vede). <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">HTML-এ প্রতিটি অংশ দুটি <b>tag</b>-এর মাঝে থাকে: <code>&lt;p&gt;</code> খোলে, <code>&lt;/p&gt;</code> বন্ধ করে। h1 বড় শিরোনাম, ul/li তালিকা, a href লিংক।</span></div>

#### 3. Ripasso CSS: i colori e lo stile · ৩. CSS

<div class="scheda">Il <b>CSS</b> decide com'è fatta la pagina: colori, bordi, spazi. Sta nel file <b>style.css</b>, collegato alla pagina con la riga <code>&lt;link rel="stylesheet" href="style.css"&gt;</code> dentro head. Una regola CSS è fatta così:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">.menu {   background: darkblue;   padding: 10px; }</pre><b>.menu</b> è il <b>selettore</b>: dice <i>a chi</i> si applica (qui: a tutto quello che ha <code>class="menu"</code>). Tra le graffe ci sono le <b>proprietà</b>: <code>background</code> il colore di sfondo, <code>padding</code> lo spazio interno, <code>color</code> il colore del testo, <code>border-radius</code> gli angoli arrotondati. Ogni proprietà finisce con <b>;</b>. Il punto davanti (<code>.menu</code>) vuol dire «classe». <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>CSS</b> পাতার রং আর স্টাইল ঠিক করে, ফাইল <b>style.css</b>-এ। <b>.menu</b> হলো selector (কাকে প্রযোজ্য), গোল বন্ধনীর ভিতরে property: background, padding, color।</span></div>

#### 4. Ripasso GitHub Pages: come si pubblica · ৪. GitHub Pages

<div class="scheda">Il sito vive nel <b>repository</b> su github.com. Per cambiare un file: apri il file, clicca la <b>matita</b> (in alto a destra), scrivi, poi <b>Commit changes</b> due volte. Il <b>commit</b> è il salvataggio con la data e un messaggio: GitHub tiene tutta la storia. Per un file nuovo: <b>Add file → Create new file</b>, scrivi il nome, incolla, commit.<br>Dopo il commit, <b>GitHub Pages</b> ricostruisce il sito: aspetta <b>1 minuto</b>, poi nel sito premi <b>Ctrl+F5</b> (ricarica senza memoria). Se vedi <b>404</b>, il nome del file non è quello che c'è scritto nel link: controlla maiuscole e minuscole, <b>competenze.html</b> tutto minuscolo. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">GitHub-এ ফাইল বদলাতে: ফাইল খোলো, <b>pencil</b> চাপো, লেখো, <b>Commit changes</b> দুইবার। ১ মিনিট পর সাইটে <b>Ctrl+F5</b>। <b>404</b> মানে ফাইলের নাম ভুল।</span></div>

#### 5. Il portfolio: a cosa serve, e la regola d'oro · ৫. Portfolio

<div class="scheda">Un <b>portfolio</b> è la pagina che racconta <b>cosa sai fare</b>: le competenze <b>tecniche</b> (HTML, CSS, GitHub, Lazarus, montare un PC…) e quelle <b>personali</b> (chiedo aiuto quando mi blocco, se sbaglio riprovo, aiuto un compagno). È il tuo <b>biglietto da visita</b> per lo stage e per un colloquio: un'azienda lo apre e in 30 secondi capisce chi sei.<br><b>Regola d'oro (privacy):</b> la pagina è <b>pubblica</b>, la vede chiunque. Scrivi <b>solo cose vere e solo cose positive</b>, e solo il tuo <b>nome o soprannome</b>: niente cognome, telefono, indirizzo, classe, scuola, foto di altri. Le cose personali (difficoltà, famiglia, da dove vieni) <b>non</b> vanno sul sito: le scrivi nella verifica, che legge solo il prof. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>Portfolio</b> = কী পারো তার পাতা: technical আর personal দক্ষতা। স্টেজ আর ইন্টারভিউর জন্য। <b>নিয়ম:</b> পাতা সবাই দেখে, তাই শুধু সত্য আর ভালো কথা, শুধু নাম বা ডাকনাম; ফোন, ঠিকানা, পরিবারের কথা নয়।</span></div>

#### 6. Il codice: la pagina competenze.html · ৬. কোড

<div class="scheda">Questa è la pagina intera. Oggi la copi <b>da qui</b> dentro GitHub (il bottone in alto a destra del riquadro, oppure seleziona tutto e Ctrl+C). Poi la cambi con le <b>tue</b> cose vere.<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">&lt;!DOCTYPE html> &lt;html lang="it"> &lt;head>   &lt;meta charset="utf-8">   &lt;meta name="viewport" content="width=device-width, initial-scale=1">   &lt;title>Cosa so fare&lt;/title>   &lt;link rel="stylesheet" href="style.css"> &lt;/head> &lt;body>   &lt;nav class="menu">     &lt;a href="index.html">Home&lt;/a>     &lt;a href="competenze.html">Cosa so fare&lt;/a>   &lt;/nav>   &lt;h1>Cosa so fare&lt;/h1>   &lt;div class="scheda">     &lt;h2>Le mie competenze tecniche&lt;/h2>     &lt;ul>       &lt;li>Scrivo una pagina web in HTML&lt;/li>       &lt;li>Cambio colori e stile con il CSS&lt;/li>       &lt;li>Pubblico il mio sito su Internet con GitHub&lt;/li>       &lt;li>Salvo ogni modifica con un commit&lt;/li>     &lt;/ul>     &lt;h2>Le mie competenze personali&lt;/h2>     &lt;ul>       &lt;li>Quando mi blocco, chiedo aiuto&lt;/li>       &lt;li>Se sbaglio, riprovo&lt;/li>       &lt;li>Aiuto un compagno quando posso&lt;/li>     &lt;/ul>     &lt;h2>Cosa ho imparato in questa scuola&lt;/h2>     &lt;p>Qui ho imparato a ...&lt;/p>     &lt;h2>La mia frase per un'azienda&lt;/h2>     &lt;p>Studio informatica. So creare e pubblicare un sito web. Imparo in fretta e non mi arrendo.&lt;/p>   &lt;/div>   &lt;p class="piede">Sito creato da me - 2026&lt;/p> &lt;/body> &lt;/html></pre>Guarda com'è fatta: il <b>menu</b> in alto (nav) con due link, un <b>h1</b>, una <b>scheda</b> (div) con quattro <b>h2</b> e gli elenchi. La riga <code>&lt;link rel="stylesheet" href="style.css"&gt;</code> le dà gli stessi colori della tua Home. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">এই পুরো পাতাটি কপি করে GitHub-এ বসাও, তারপর নিজের সত্য কথা দিয়ে বদলাও।</span></div>

#### 7. Il menu nella Home e i suoi colori · ৭. মেনু

<div class="scheda">Perché dalla Home si arrivi al portfolio, anche <b>index.html</b> deve avere il menu. Si mette <b>subito dopo</b> la riga <code>&lt;body&gt;</code>:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">  &lt;nav class="menu">     &lt;a href="index.html">Home&lt;/a>     &lt;a href="competenze.html">Cosa so fare&lt;/a>   &lt;/nav></pre>Se hai già il menu della Dispensa 4, aggiungi solo la riga di <b>competenze.html</b>. Se hai anche <b>passione.html</b>, lascia anche quella.<br>Se il menu resta senza colori, in fondo a <b>style.css</b> ci va questo:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre;overflow-x:auto">.menu {   background: darkblue;   padding: 10px;   border-radius: 10px; } .menu a {   color: white;   text-decoration: none;   font-weight: bold;   margin: 0 12px; } .menu a:hover {   color: orange; }</pre> <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>index.html</b>-এও মেনু লাগবে, <code>&lt;body&gt;</code>-এর ঠিক পরে। মেনুতে রং না থাকলে <b>style.css</b>-এর শেষে এই কোড।</span></div>

#### 8. LA PRATICA, passi 1-3: la pagina nuova su GitHub · ৮. অনুশীলন ১-৩

<div class="scheda">Un passo alla volta. Ogni passo è una cosa sola.<br>1) Vai su <b>github.com</b>, entra, apri il tuo repository <b>mio-sito</b>.<br>2) Clicca il bottone grigio <b>Add file</b> (in alto a destra, vicino al verde), poi <b>Create new file</b>. Nella casella del nome scrivi esattamente <b>competenze.html</b> (tutto minuscolo).<br>3) Nel riquadro grande incolla la pagina della scheda 6 (Ctrl+V). Poi il bottone verde <b>Commit changes...</b>, poi di nuovo <b>Commit changes</b>. <b>FATTO!</b> Il file esiste.<br>Rispondi alla domanda qui sotto: così il monitor sa che sei a questo punto. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">১) github.com → <b>mio-sito</b>। ২) <b>Add file → Create new file</b>, নাম <b>competenze.html</b>। ৩) কোড পেস্ট, <b>Commit changes</b> দুইবার।</span></div>

#### 9. LA PRATICA, passi 4-6: fallo tuo e collega la Home · ৯. অনুশীলন ৪-৬

<div class="scheda">4) <b>Fallo tuo, solo cose vere.</b> Apri <b>competenze.html</b>, clicca la <b>matita</b>. Cambia gli elenchi: lascia solo le competenze che hai davvero, aggiungine di tue (una cosa che sai fare al PC, in Lazarus, con le mani…). Scrivi la frase «Qui ho imparato a …» e la <b>tua frase per un'azienda</b>. Commit.<br>5) Apri <b>index.html</b>, matita. Subito dopo la riga <code>&lt;body&gt;</code> incolla il menu della scheda 7 (se c'è già, aggiungi solo la riga di competenze.html). Commit.<br>6) Aspetta 1 minuto. Apri il tuo sito, <b>Ctrl+F5</b>. Clicca <b>Cosa so fare</b>, poi <b>Home</b>. <b>FATTO!</b> Il tuo portfolio è online. Copia l'indirizzo della pagina dalla barra del browser: ti serve per la verifica. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">৪) <b>competenze.html</b> → pencil → নিজের সত্য দক্ষতা লেখো → Commit। ৫) <b>index.html</b>-এ <code>&lt;body&gt;</code>-এর পরে মেনু → Commit। ৬) ১ মিনিট পর সাইট খোলো, <b>Ctrl+F5</b>। ঠিকানাটি কপি করো।</span></div>

#### 10. Se qualcosa non va, e la sfida per chi ha finito · ১০. সমস্যা ও চ্যালেঞ্জ

<div class="scheda"><b>Vedo 404</b> cliccando «Cosa so fare»: il file deve chiamarsi esattamente <b>competenze.html</b>, minuscolo, come nel menu. <b>Il menu è senza colori</b>: in fondo a style.css incolla il CSS della scheda 7, aspetta un minuto, Ctrl+F5. <b>La scheda bianca non ha il bordo</b>: ti manca il CSS della Dispensa 3 (.scheda), lo trovi nella pagina della classe. <b>Non vedo le modifiche</b>: hai fatto il commit? Hai aspettato un minuto? Ctrl+F5?<br><b>Mostralo:</b> leggi al compagno la tua frase per un'azienda, come a un colloquio, 30 secondi.<br><b>Sfida per chi ha finito:</b> 1) una terza pagina <b>passione.html</b> (la cosa che ti piace di più) con la sua riga nel menu; 2) cambia un colore del menu e lo sfondo della scheda; 3) nella Home metti un link al portfolio anche in fondo alla pagina.<br>Ti blocchi? Scrivi la domanda all'assistente, in fondo alla pagina: ti risponde. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>404</b>: ফাইলের নাম <b>competenze.html</b> ছোট হাতের। মেনুতে রং নেই: style.css-এর শেষে CSS। শেষ করলে: <b>passione.html</b> তৃতীয় পাতা, রং বদলাও। আটকে গেলে নিচে সহকারীকে প্রশ্ন করো।</span></div>

#### 11. Ultimi 10 minuti: prepariamo mercoledì (lavoro in coppia) · ১১. বুধবারের প্রস্তুতি

<div class="scheda">Mercoledì lavorate <b>in coppia</b>: il compagno scrive una pagina nel <b>tuo</b> sito e tu nel suo, come in un'azienda. Per farlo, oggi vi date il permesso a vicenda. Il prof vi dice chi è il vostro compagno.<br>1) Chiedi al compagno il suo <b>nome utente GitHub</b> (quello dell'indirizzo, prima di .github.io).<br>2) Nel tuo repository <b>mio-sito</b> clicca <b>Settings</b> (l'ingranaggio, in alto a destra nella barra del repository).<br>3) Nel menu a sinistra clicca <b>Collaborators</b> (Collaboratori). Se chiede la password, rimettila.<br>4) Clicca il bottone verde <b>Add people</b>, scrivi il nome utente del compagno, sceglilo dall'elenco e conferma.<br>5) Il compagno riceve l'invito: lo trova nella <b>campanella</b> in alto a destra su github.com (o nella posta) e preme <b>Accept invitation</b>. Poi fate lo stesso al contrario. <b>FATTO!</b> Mercoledì potete lavorare uno nel sito dell'altro.<br>Rispondi alla domanda qui sotto. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">বুধবার জোড়ায় কাজ: সঙ্গী তোমার সাইটে একটি পাতা লিখবে। আজ: <b>Settings → Collaborators → Add people</b>, সঙ্গীর GitHub নাম লেখো। সঙ্গী ঘণ্টার আইকনে <b>Accept invitation</b> চাপে। তারপর উল্টোটা।</span></div>

#### 12. Per chi ha finito: una FOTO DI SFONDO al tuo sito · ১২. পটভূমির ছবি

<div class="scheda">Solo se hai la bandiera 🏁 (portfolio completo). Il sito diventa tuo davvero con una foto di sfondo.<br>1) Scegli una foto: una TUA (fatta da te, senza persone riconoscibili) oppure una libera da <a href='https://pixabay.com' target='_blank' rel='noopener'>pixabay.com</a>. Scaricala sul PC e rinominala <b>sfondo.jpg</b> (tutto minuscolo).<br>2) Nel tuo repository: <b>Add file → Upload files</b>, trascina <b>sfondo.jpg</b>, poi il verde <b>Commit changes</b>.<br>3) Apri <b>style.css</b> → matita. Dentro le graffe di <b>body { }</b> aggiungi queste tre righe, poi <b>Commit changes</b>:<br><pre style='background:#f3f5f8;padding:8px;border-radius:8px'>background-image: url("sfondo.jpg"); background-size: cover; background-attachment: fixed;</pre>4) Se il testo si legge male: alle regole <b>.scheda</b> (o <b>main</b>) aggiungi <b>background: #fff; padding: 16px; border-radius: 12px;</b> così il testo sta su un riquadro bianco.<br>5) Aspetta 1 minuto, apri il sito, <b>Ctrl+F5</b>: la foto è dietro a tutte le pagine (anche «Cosa so fare», perché usano lo stesso style.css). <b>FATTO!</b> Rispondi alla domanda qui sotto. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">শুধু 🏁 থাকলে। একটি ছবি (নিজের বা pixabay.com থেকে), নাম <b>sfondo.jpg</b>। Repository-তে <b>Add file → Upload files</b>। তারপর <b>style.css</b>-এর <b>body { }</b>-তে: background-image: url("sfondo.jpg"); background-size: cover; background-attachment: fixed; → Commit। ১ মিনিট পরে Ctrl+F5।</span></div>



v1.0

### Dispensa 4 — La seconda pagina e il menu

Classe 3 · Informatica · 08/10/2026 · un sito vero ha più pagine collegate · italiano

**Cosa ottieni oggi:** il tuo sito ha **due pagine** (Home e La mia passione) e un **menu** in alto per passare dall'una all'altra, come i siti veri. Le due pagine usano lo **stesso style.css** : cambi un colore e cambia in tutto il sito.

#### 1\. Il codice nuovo

RIQUADRO 5 — file nuovo passione.html (la seconda pagina)
    
    
```
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>La mia passione</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="passione.html">La mia passione</a>
  </nav>

  <h1>La mia passione: il calcio</h1>

  <div class="scheda">
    <h2>Perché mi piace</h2>
    <p>Mi piace giocare in squadra e allenarmi con gli amici.</p>

    <h2>Tre cose che so fare</h2>
    <ol>
      <li>Passare la palla con precisione</li>
      <li>Correre veloce</li>
      <li>Parare un rigore</li>
    </ol>

    <h2>Lo sapevi che...</h2>
    <p>Il primo mondiale di calcio si è giocato nel 1930.</p>
  </div>

  <p class="piede">Sito creato da me - 2026</p>
</body>
</html>
```

    

RIQUADRO 6 — il menu: da mettere in index.html, subito dopo <body>
    
    
```
  <nav class="menu">
    <a href="index.html">Home</a>
    <a href="passione.html">La mia passione</a>
  </nav>
```

    

RIQUADRO 7 — in fondo a style.css
    
    
```
.menu {
  background: darkblue;
  padding: 10px;
  border-radius: 10px;
}

.menu a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  margin: 0 12px;
}

.menu a:hover {
  color: orange;
}
```

    

#### 2\. I passi, uno alla volta

1Crea il file nuovo

Nel repository **mio-sito** : bottone **Add file** (grigio) -> **Create new file** (Crea nuovo file). In alto, nel campo del nome, scrivi passione.html.

github.com/tuonome/mio-sito/new/main

mio-sito / passione.html

Enter file contents here

2Incolla la seconda pagina

Nel riquadro grande incolla il RIQUADRO 5. Poi **Commit changes...** -> **Commit changes**.

3Fallo tuo

Con la **matita** cambia la pagina: la **tua** passione (sport, musica, cucina, un videogioco, un paese...), perché ti piace, tre cose che sai fare, una curiosità. Poi Commit.

4Il menu anche nella Home

Apri **index.html** -> **matita**. Subito dopo la riga <body> incolla il RIQUADRO 6. Commit.

5Lo stile del menu

Apri **style.css** -> **matita** -> in fondo incolla il RIQUADRO 7. Commit.

6Prova il menu

Aspetta 1 minuto, apri il sito, Ctrl \+ F5. Clic su **La mia passione** , poi su **Home** : passi da una pagina all'altra. **FATTO! Hai un sito a due pagine.**

7Mostralo

L'indirizzo della seconda pagina è https://tuonome.github.io/mio-sito/passione.html. Aprila sul telefono e falla vedere a un compagno.

#### 3\. Se qualcosa non va

Problema| Soluzione  
---|---  
Clic su **La mia passione** e vedo **404**|  Il file deve chiamarsi esattamente **passione.html** (minuscolo), come nel menu.  
La seconda pagina è **senza colori**|  Manca la riga &lt;link rel="stylesheet" href="style.css"> nel &lt;head>.  
Il menu c'è ma è **senza stile**|  Il RIQUADRO 7 non è in style.css, oppure aspetta un minuto e Ctrl \+ F5.  
  
**Carta e penna:** disegna la **mappa del sito** : due rettangoli (index.html e passione.html) con le frecce del menu, e una freccia da ciascuno verso style.css.

Classe 3 · Dispensa 4 · v1.0

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
