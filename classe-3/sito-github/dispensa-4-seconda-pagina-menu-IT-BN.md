<!-- generato da dispensa-4-seconda-pagina-menu-IT-BN.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 4 — La seconda pagina e il menu

ডিসপেন্সা ৪ — দ্বিতীয় পেজ ও মেনু

Classe 3 · Informatica · 08/10/2026 · un sito vero ha più pagine collegate · IT / বাংলা

**Cosa ottieni oggi:** il tuo sito ha **due pagine** (Home e La mia passione) e un **menu** in alto per passare dall'una all'altra, come i siti veri. Le due pagine usano lo **stesso style.css** : cambi un colore e cambia in tutto il sito.

**আজ তুমি পাবে:** তোমার সাইটে **দুটি পেজ** (Home ও La mia passione) আর উপরে একটি **মেনু** , এক পেজ থেকে অন্যটিতে যেতে, আসল সাইটের মতো। দুটি পেজ **একই style.css** ব্যবহার করে: একটি রং বদলালে পুরো সাইটে বদলায়।

## 1\. Il codice nuovo

RIQUADRO 5 — file nuovo passione.html (la seconda pagina)
    
    
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
    

RIQUADRO 6 — il menu: da mettere in index.html, subito dopo <body>
    
    
      <nav class="menu">
        <a href="index.html">Home</a>
        <a href="passione.html">La mia passione</a>
      </nav>
    

RIQUADRO 7 — in fondo a style.css
    
    
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
    

## 2\. I passi, uno alla volta

1Crea il file nuovo · নতুন ফাইল বানাও

Nel repository **mio-sito** : bottone **Add file** (grigio) -> **Create new file** (Crea nuovo file). In alto, nel campo del nome, scrivi passione.html.

**mio-sito** repository-তে: **Add file** বোতাম (ধূসর) -> **Create new file** (নতুন ফাইল)। উপরে নামের ঘরে লেখো passione.html।

github.com/tuonome/mio-sito/new/main

mio-sito / passione.html

Enter file contents here

2Incolla la seconda pagina · দ্বিতীয় পেজ পেস্ট করো

Nel riquadro grande incolla il RIQUADRO 5. Poi **Commit changes...** -> **Commit changes**.

বড় বাক্সে বাক্স ৫ পেস্ট করো। তারপর **Commit changes...** -> **Commit changes** ।

3Fallo tuo · নিজের মতো করো

Con la **matita** cambia la pagina: la **tua** passione (sport, musica, cucina, un videogioco, un paese...), perché ti piace, tre cose che sai fare, una curiosità. Poi Commit.

**পেনসিল** দিয়ে পেজটি বদলাও: **তোমার** শখ (খেলা, গান, রান্না, ভিডিও গেম, একটি দেশ...), কেন ভালো লাগে, তিনটি জিনিস যা পারো, একটি মজার তথ্য। তারপর Commit।

4Il menu anche nella Home · Home-এও মেনু

Apri **index.html** -> **matita**. Subito dopo la riga <body> incolla il RIQUADRO 6. Commit.

**index.html** খোলো -> **পেনসিল** । <body> লাইনের ঠিক পরে বাক্স ৬ পেস্ট করো। Commit।

5Lo stile del menu · মেনুর স্টাইল

Apri **style.css** -> **matita** -> in fondo incolla il RIQUADRO 7. Commit.

**style.css** খোলো -> **পেনসিল** -> একদম নিচে বাক্স ৭ পেস্ট করো। Commit।

6Prova il menu · মেনু চেষ্টা করো

Aspetta 1 minuto, apri il sito, Ctrl \+ F5. Clic su **La mia passione** , poi su **Home** : passi da una pagina all'altra. **FATTO! Hai un sito a due pagine.**

১ মিনিট অপেক্ষা করো, সাইট খোলো, Ctrl \+ F5। **La mia passione** -এ, তারপর **Home** -এ ক্লিক করো: এক পেজ থেকে অন্য পেজে যাবে। **হয়ে গেছে! তোমার দুই পেজের সাইট।**

7Mostralo · দেখাও

L'indirizzo della seconda pagina è https://tuonome.github.io/mio-sito/passione.html. Aprila sul telefono e falla vedere a un compagno.

দ্বিতীয় পেজের ঠিকানা https://tuonome.github.io/mio-sito/passione.html। ফোনে খোলো আর একজন সহপাঠীকে দেখাও।

## 3\. Se qualcosa non va

Problema| Soluzione  
---|---  
Clic su **La mia passione** e vedo **404****La mia passione** -এ ক্লিক করলে **404**|  Il file deve chiamarsi esattamente **passione.html** (minuscolo), come nel menu.ফাইলের নাম ঠিক **passione.html** (ছোট হাতের) হতে হবে, মেনুর মতো।  
La seconda pagina è **senza colori** দ্বিতীয় পেজে **রং নেই**|  Manca la riga <link rel="stylesheet" href="style.css"> nel <head>.<head>-এ <link rel="stylesheet" href="style.css"> লাইনটি নেই।  
Il menu c'è ma è **senza stile** মেনু আছে কিন্তু **স্টাইল নেই**|  Il RIQUADRO 7 non è in style.css, oppure aspetta un minuto e Ctrl \+ F5.বাক্স ৭ style.css-এ নেই, অথবা এক মিনিট অপেক্ষা করে Ctrl \+ F5।  
  
**Carta e penna:** disegna la **mappa del sito** : due rettangoli (index.html e passione.html) con le frecce del menu, e una freccia da ciascuno verso style.css.

**কাগজ-কলম:** **সাইটের মানচিত্র** আঁকো: দুটি আয়তক্ষেত্র (index.html ও passione.html) মেনুর তীর সহ, আর প্রতিটি থেকে style.css-এর দিকে একটি তীর।

Classe 3 · Dispensa 4 · v1.0
