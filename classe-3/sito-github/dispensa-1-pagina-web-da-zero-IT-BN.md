<!-- generato da dispensa-1-pagina-web-da-zero-IT-BN.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 1 — La mia pagina web da zero

ডিসপেন্সা ১ — শূন্য থেকে আমার ওয়েব পেজ

Classe 3 · Informatica · 05/10/2026 · HTML + CSS in due file separati · IT / বাংলা

**Cosa ottieni oggi:** una cartella **mio-sito** con **due file** : **index.html** (il **contenuto** : i testi) e **style.css** (l'**aspetto** : i colori). Doppio clic e la tua pagina si apre nel browser. Nella Dispensa 2 la mettiamo **su internet**.

**আজ তুমি পাবে:** **mio-sito** নামের একটি ফোল্ডার, তাতে **দুটি ফাইল** : **index.html** (**বিষয়বস্তু** : লেখা) এবং **style.css** (**চেহারা** : রং)। ডাবল ক্লিক করলেই ব্রাউজারে পেজ খুলবে। ডিসপেন্সা ২-এ আমরা এটাকে **ইন্টারনেটে** দেব।

# Ciao, sono Leo

Questo è il mio primo sito web.

### Chi sono

Studio informatica e mi piace creare cose nuove.

### Le mie passioni

  * Calcio
  * Videogiochi
  * Musica

### Il mio sogno

Lavorare con i computer.

Sito creato da me - 2026

Ecco come sarà (poi la fai tua)

Desktop > mio-sito

index.html style.css  
  
index.html = CONTENUTO  
style.css = ASPETTO

La cartella: esattamente due file

**Carta e penna:** disegna sul quaderno la cartella **mio-sito** con dentro i due file. Fai una freccia da index.html a style.css e scrivici sopra **< link>**. Scrivi: **HTML = contenuto, CSS = aspetto**.

**কাগজ-কলম:** খাতায় **mio-sito** ফোল্ডার আর তার ভিতরের দুটি ফাইল আঁকো। index.html থেকে style.css-এর দিকে একটি তীর আঁকো, উপরে লেখো **< link>**। লেখো: **HTML = বিষয়বস্তু, CSS = চেহারা** ।

**Il tuo sito diventerà PUBBLICO** (lo vedrà chiunque su internet). Quindi scrivi **solo il nome o un soprannome**. **MAI** cognome, telefono, email, indirizzo, foto del viso.

**তোমার সাইট সবার জন্য খোলা হবে** (ইন্টারনেটে যে কেউ দেখবে)। তাই শুধু **নাম বা ডাকনাম** লেখো। **কখনো না:** পদবি, ফোন, ইমেল, ঠিকানা, মুখের ছবি।

## 1\. Il codice (uguale per tutti — poi lo fai tuo)

**Il modo più sicuro per copiare:** apri la pagina del corso (il link è nel compito su Classroom) e premi il bottone **Copia** sopra il codice. Poi nel Blocco note premi Ctrl \+ V. Copiare dal PDF a volte rovina gli spazi.

**কপি করার সবচেয়ে নিরাপদ উপায়:** কোর্সের পেজ খোলো (লিংকটি Classroom-এর কাজে আছে) এবং কোডের উপরের **Copia** (কপি) বোতাম চাপো। তারপর Notepad-এ Ctrl \+ V চাপো। PDF থেকে কপি করলে কখনো কখনো ফাঁকা জায়গা নষ্ট হয়।

RIQUADRO 1 — file index.html (il contenuto)
    
    
    <!DOCTYPE html>
    <html lang="it">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Il mio primo sito</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <h1>Ciao, sono Leo</h1>
      <p class="sotto">Questo è il mio primo sito web.</p>
    
      <div class="scheda">
        <h2>Chi sono</h2>
        <p>Studio informatica e mi piace creare cose nuove.</p>
    
        <h2>Le mie passioni</h2>
        <ul>
          <li>Calcio</li>
          <li>Videogiochi</li>
          <li>Musica</li>
        </ul>
    
        <h2>Il mio sogno</h2>
        <p>Lavorare con i computer.</p>
      </div>
    
      <p class="piede">Sito creato da me - 2026</p>
    </body>
    </html>
    

RIQUADRO 2 — file style.css (l'aspetto)
    
    
    body {
      background: lightblue;
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
    }
    
    h1 {
      color: darkblue;
    }
    
    .sotto {
      color: gray;
    }
    
    .scheda {
      background: white;
      max-width: 500px;
      margin: 20px auto;
      padding: 20px;
      border-radius: 12px;
      text-align: left;
    }
    
    h2 {
      color: teal;
    }
    
    .piede {
      font-size: 12px;
      color: gray;
    }
    

## 2\. I passi, uno alla volta

1Crea la cartella · ফোল্ডার বানাও

Sul **Desktop** , in un punto vuoto: clic con il tasto **DESTRO** del mouse -> **Nuovo** -> **Cartella**. Scrivi il nome mio-sito e premi Invio.

**Desktop** -এর খালি জায়গায় মাউসের **ডান** বোতামে ক্লিক করো -> **Nuovo** (নতুন) -> **Cartella** (ফোল্ডার)। নাম লেখো mio-sito এবং Invio (Enter) চাপো।

2Fai vedere la fine dei nomi (consigliato) · ফাইলের নামের শেষ অংশ দেখাও

Apri la cartella **mio-sito**. In alto clic su **Visualizza** -> **Mostra** -> **Estensioni nomi file** (compare la spunta). Così vedi se un file finisce con **.html** o, per errore, con **.txt**.

**mio-sito** ফোল্ডার খোলো। উপরে **Visualizza** (View) -> **Mostra** (Show) -> **Estensioni nomi file** (File name extensions)-এ ক্লিক করো (টিক চিহ্ন আসবে)। এতে দেখবে ফাইলের নাম **.html** দিয়ে শেষ, নাকি ভুল করে **.txt** দিয়ে।

3Apri il Blocco note · Notepad খোলো

In basso a sinistra clic su **Start** , scrivi Blocco note e clicca sul programma **Blocco note**.

নিচে বাঁদিকে **Start** -এ ক্লিক করো, লেখো Blocco note (Notepad) এবং প্রোগ্রামটিতে ক্লিক করো।

4Incolla il codice HTML · HTML কোড পেস্ট করো

Copia **tutto** il **RIQUADRO 1** e incollalo nel Blocco note (Ctrl \+ V).

**বাক্স ১** -এর **পুরো** কোড কপি করে Notepad-এ পেস্ট করো (Ctrl \+ V)।

5Fallo tuo · নিজের মতো করো

Cambia **Leo** con il tuo nome o un soprannome. Cambia **Chi sono** , **le passioni** e **il sogno** con cose tue. Non toccare le parole tra < e >: cambia solo il testo in mezzo.

**Leo** -র জায়গায় তোমার নাম বা ডাকনাম লেখো। **Chi sono** (আমি কে), **শখ** আর **স্বপ্ন** নিজের মতো বদলাও। < আর >-এর ভিতরের শব্দ বদলাবে না: শুধু মাঝের লেখা বদলাও।

6Salva come index.html · index.html নামে সেভ করো

In alto a sinistra **File** -> **Salva con nome**. A sinistra scegli **Desktop** e apri **mio-sito**. In basso: **Salva come** -> **Tutti i file** ; **Nome file** : index.html; **Codifica** : **UTF-8**. Clic su **Salva**.

উপরে বাঁদিকে **File** -> **Salva con nome** (Save as)। বাঁদিকে **Desktop** বেছে **mio-sito** খোলো। নিচে: **Salva come** (Save as type) -> **Tutti i file** (All files); নাম: index.html; **Codifica** (Encoding): **UTF-8** । **Salva** (Save) চাপো।

Salva con nome

Cartella: **Desktop > mio-sito**

Nome file: index.html

Salva come: Tutti i file (*.*)

Codifica: UTF-8   Salva

7Un foglio nuovo per il CSS · CSS-এর জন্য নতুন পাতা

Nel Blocco note: **File** -> **Nuovo** (si apre un foglio vuoto). Copia **tutto** il **RIQUADRO 2** e incollalo.

Notepad-এ: **File** -> **Nuovo** (New) (খালি পাতা খুলবে)। **বাক্স ২** -এর **পুরো** কোড কপি করে পেস্ট করো।

8Salva come style.css · style.css নামে সেভ করো

Come prima: **File** -> **Salva con nome** , **stessa cartella mio-sito** , **Tutti i file** , nome style.css, **UTF-8** , **Salva**.

আগের মতো: **File** -> **Salva con nome** , **একই mio-sito ফোল্ডার** , **Tutti i file** , নাম style.css, **UTF-8** , **Salva** ।

9Controlla la cartella · ফোল্ডার মিলিয়ে দেখো

Dentro **mio-sito** ci devono essere **due file** : index.html e style.css. Nomi tutti **minuscoli** , senza spazi, senza **.txt** alla fine.

**mio-sito** -র ভিতরে **দুটি ফাইল** থাকতে হবে: index.html এবং style.css। সব **ছোট হাতের** অক্ষর, কোনো ফাঁকা নেই, শেষে **.txt** নেই।

10Apri la tua pagina · তোমার পেজ খোলো

Doppio clic su **index.html** : si apre nel browser, **con i colori**. **FATTO! Hai creato la tua pagina web.**

**index.html** -এ ডাবল ক্লিক করো: ব্রাউজারে **রঙসহ** খুলবে। **হয়ে গেছে! তুমি নিজের ওয়েব পেজ বানিয়েছ।**

11Cambia i colori (il CSS) · রং বদলাও (CSS)

Clic **destro** su **style.css** -> **Apri con** -> **Blocco note**. Cambia lightblue con un colore che ti piace. Salva (Ctrl \+ S) e nel browser premi F5: il colore cambia!

**style.css** -এ **ডান** ক্লিক -> **Apri con** (Open with) -> **Blocco note** । lightblue বদলে তোমার পছন্দের রং লেখো। সেভ করো (Ctrl \+ S) এবং ব্রাউজারে F5 চাপো: রং বদলে যাবে!

Colore| Scrivi| Colore| Scrivi| Colore| Scrivi  
---|---|---|---|---|---  
| pink| | lightgreen| | gold  
| orange| | lavender| | coral  
| khaki| | turquoise| | salmon  
  
## 3\. Cosa fa ogni pezzo

Pezzo di codice| Cosa fa| কী করে  
---|---|---  
<head> ... </head>| istruzioni per il browser (non si vedono)| ব্রাউজারের জন্য নির্দেশ (দেখা যায় না)  
<link rel="stylesheet" href="style.css">| **collega** l'HTML al file style.css| HTML-কে style.css ফাইলের সাথে **যুক্ত** করে  
<body> ... </body>| tutto quello che si vede nella pagina| পেজে যা দেখা যায় সব  
<h1> <h2>| titolo grande, titolo più piccolo| বড় শিরোনাম, ছোট শিরোনাম  
<p>| un paragrafo di testo| এক অনুচ্ছেদ লেখা  
<ul> <li>| un elenco e le sue voci| একটি তালিকা ও তার আইটেম  
<div class="scheda">| una scatola; il nome **scheda** lo usa il CSS| একটি বাক্স; **scheda** নামটি CSS ব্যবহার করে  
.scheda { background: white; }| CSS: **chi** { **proprietà** : **valore** ; }| CSS: **কে** { **বৈশিষ্ট্য** : **মান** ; }  
  
## 4\. Se qualcosa non va (succede a tutti, anche ai professionisti)

Problema| Soluzione  
---|---  
Vedo il **codice** invece della pagina**কোড** দেখা যাচ্ছে, পেজ নয়| Il file è stato salvato come **.txt** : risalva con **Tutti i file**.ফাইলটি **.txt** হয়ে গেছে: **Tutti i file** বেছে আবার সেভ করো।  
La pagina è **senza colori** পেজে **রং নেই**|  style.css non è nella stessa cartella, o ha un nome diverso (es. **Style.css** , **stile.css** , **style.css.txt**).style.css একই ফোল্ডারে নেই, বা নাম আলাদা (যেমন **Style.css** , **stile.css** , **style.css.txt**)।  
Al posto di **è** vedo simboli strani**è** -এর জায়গায় অদ্ভুত চিহ্ন| Risalva index.html scegliendo **Codifica: UTF-8**.**Codifica: UTF-8** বেছে index.html আবার সেভ করো।  
Ho cambiato ma non vedo nienteবদলেছি কিন্তু কিছু দেখছি না| Hai salvato? (Ctrl+S) Poi nel browser F5.সেভ করেছ? (Ctrl+S) তারপর ব্রাউজারে F5।  
  
**Hai già fatto la pagina del 30/09?** Benissimo: puoi riusare i tuoi testi. Ma per il sito servono **questi nomi esatti** : **index.html** e **style.css** , e nel <link> deve esserci **style.css**.

**৩০/০৯-এর পেজ আগেই বানিয়েছ?** খুব ভালো: তোমার লেখা আবার ব্যবহার করতে পারো। কিন্তু সাইটের জন্য **ঠিক এই নাম** লাগবে: **index.html** এবং **style.css** , আর <link>-এ থাকতে হবে **style.css** ।

**Prossimo passo:** Dispensa 2 — mettiamo il tuo sito **su internet** , con un indirizzo da aprire anche sul telefono.

**পরের ধাপ:** ডিসপেন্সা ২ — তোমার সাইট **ইন্টারনেটে** দেব, একটি ঠিকানা সহ যা ফোনেও খোলা যাবে।

Classe 3 · Dispensa 1 · v1.0 · Tutti i dati negli esempi sono inventati.
