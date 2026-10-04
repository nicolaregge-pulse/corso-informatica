<!-- generato da dispensa-3-migliora-sito-github-IT-BN.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 3 — Migliora il tuo sito direttamente su GitHub

ডিসপেন্সা ৩ — সরাসরি GitHub-এ তোমার সাইট উন্নত করো

Classe 3 · Informatica · 07/10/2026 · la matita, il commit, la storia delle versioni · IT / বাংলা

**Cosa ottieni oggi:** nel tuo sito compaiono due **bottoni-link** che cambiano colore quando ci passi sopra, e la scheda ha un'**ombra**. Modifichi i file **direttamente su GitHub** , senza scaricare niente: ogni modifica è un **commit** , cioè una nuova **versione** salvata nella storia.

**আজ তুমি পাবে:** তোমার সাইটে দুটি **বোতাম-লিংক** , মাউস রাখলে রং বদলায়, আর কার্ডে একটি **ছায়া** । ফাইলগুলো **সরাসরি GitHub-এ** বদলাবে, কিছু ডাউনলোড না করে: প্রতিটি পরিবর্তন একটি **commit** , মানে ইতিহাসে সেভ করা একটি নতুন **সংস্করণ** ।

**Il sito è pubblico:** anche oggi solo nome o soprannome, niente dati personali.

**সাইটটি পাবলিক:** আজও শুধু নাম বা ডাকনাম, কোনো ব্যক্তিগত তথ্য নয়।

## 1\. Il codice nuovo

Il codice si copia dalla **pagina del corso** con il bottone **Copia** (link nel compito su Classroom).

কোডটি **কোর্সের পেজ** থেকে **Copia** বোতাম দিয়ে কপি করো (লিংক Classroom-এর কাজে)।

RIQUADRO 3 — da aggiungere in index.html (prima di </div>)
    
    
        <h2>I miei siti preferiti</h2>
        <p>
          <a class="bottone" href="https://it.wikipedia.org/wiki/HTML" target="_blank">Cos'è l'HTML</a>
          <a class="bottone" href="https://www.w3schools.com/css/" target="_blank">Imparo il CSS</a>
        </p>
    

RIQUADRO 4 — da aggiungere in fondo a style.css
    
    
    .scheda {
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    .bottone {
      display: inline-block;
      background: darkblue;
      color: white;
      padding: 8px 14px;
      border-radius: 8px;
      text-decoration: none;
      margin: 4px;
    }
    
    .bottone:hover {
      background: orange;
    }
    

## 2\. I passi, uno alla volta

1Apri il tuo repository · তোমার repository খোলো

Vai su github.com, entra (Sign in) e apri il repository **mio-sito** (in alto a sinistra, o dal tuo profilo).

এই ঠিকানায় যাও: github.com, ঢোকো (Sign in) এবং **mio-sito** repository খোলো (উপরে বাঁদিকে, বা তোমার প্রোফাইল থেকে)।

2Apri index.html e premi la matita · index.html খুলে পেনসিলে চাপো

Nell'elenco dei file clic su **index.html**. In alto a destra del codice clic sulla **matita** ✎ (Modifica).

ফাইলের তালিকায় **index.html** -এ ক্লিক করো। কোডের উপরে ডানদিকে **পেনসিল** ✎ (এডিট)-এ ক্লিক করো।

github.com/tuonome/mio-sito/blob/main/index.html

**mio-sito / index.html**

Raw ✎ <- matita ⋮

3Incolla il RIQUADRO 3 · বাক্স ৩ পেস্ট করো

Trova la riga <p>Lavorare con i computer.</p> (o il tuo sogno). Clic alla fine della riga, premi Invio e incolla il RIQUADRO 3 (Ctrl \+ V). Deve stare **prima** di </div>.

<p>Lavorare con i computer.</p> (বা তোমার স্বপ্ন) লাইনটি খোঁজো। লাইনের শেষে ক্লিক করে Invio চাপো, তারপর বাক্স ৩ পেস্ট করো (Ctrl \+ V)। এটি </div>-এর **আগে** থাকতে হবে।

4Salva: Commit changes · সেভ: Commit changes

In alto a destra bottone **verde** **Commit changes...** -> si apre una finestrella -> di nuovo **Commit changes** (verde).

উপরে ডানদিকে **সবুজ** বোতাম **Commit changes...** -> একটি ছোট জানালা খুলবে -> আবার **Commit changes** (সবুজ)।

Cancel changes Commit changes... <- 1

**Commit changes**

Commit message: Update index.html

Commit changes <- 2

5Ora style.css · এবার style.css

Torna al repository (clic su **mio-sito** in alto), clic su **style.css** -> **matita**. Vai **in fondo** , premi Invio e incolla il RIQUADRO 4. Poi **Commit changes...** -> **Commit changes**.

repository-তে ফিরে যাও (উপরে **mio-sito** -এ ক্লিক), **style.css** -এ ক্লিক -> **পেনসিল** । **একদম নিচে** যাও, Invio চাপো এবং বাক্স ৪ পেস্ট করো। তারপর **Commit changes...** -> **Commit changes** ।

6Guarda il sito · সাইট দেখো

Aspetta 1 minuto, apri il tuo sito (https://tuonome.github.io/mio-sito/) e premi Ctrl \+ F5. Passa con il mouse sui bottoni: diventano arancioni! **FATTO!**

১ মিনিট অপেক্ষা করো, তোমার সাইট খোলো (https://tuonome.github.io/mio-sito/) এবং Ctrl \+ F5 চাপো। বোতামের উপর মাউস রাখো: কমলা হয়ে যাবে! **হয়ে গেছে!**

7La storia delle versioni · সংস্করণের ইতিহাস

Nel repository clic sul file **index.html** -> in alto a destra **History** (Cronologia, icona con l'orologio). Vedi la lista dei tuoi **commit** : ogni riga è una versione del file, con data e messaggio. Fai uno **screenshot** : serve per il compito.

repository-তে **index.html** -এ ক্লিক -> উপরে ডানদিকে **History** (ইতিহাস, ঘড়ির চিহ্ন)। তোমার **commit** -এর তালিকা দেখবে: প্রতিটি লাইন ফাইলের একটি সংস্করণ, তারিখ ও বার্তা সহ। একটি **স্ক্রিনশট** নাও: কাজের জন্য লাগবে।

8Fallo tuo · নিজের মতো করো

Cambia i link con **due siti utili che piacciono a te** (niente social, niente siti vietati) e i colori dei bottoni. Ogni volta: matita -> Commit.

লিংক বদলে **তোমার পছন্দের দুটি দরকারি সাইট** দাও (সোশ্যাল নয়, নিষিদ্ধ সাইট নয়) এবং বোতামের রং বদলাও। প্রতিবার: পেনসিল -> Commit।

## 3\. Cosa fa ogni pezzo

Pezzo| Cosa fa| কী করে  
---|---|---  
<a href="...">testo</a>| un **link** : **href** è l'indirizzo dove porta| একটি **লিংক** : **href** হলো ঠিকানা যেখানে নিয়ে যায়  
target="_blank"| apre il link in una scheda nuova| লিংকটি নতুন ট্যাবে খোলে  
class="bottone"| il nome che usa il CSS per dare l'aspetto| যে নাম দিয়ে CSS চেহারা দেয়  
.bottone:hover| lo stile quando il mouse **passa sopra**|  মাউস **উপরে রাখলে** যে স্টাইল  
box-shadow| l'ombra della scatola| বাক্সের ছায়া  
commit| una versione salvata, con data e messaggio| তারিখ ও বার্তা সহ একটি সেভ করা সংস্করণ  
  
**Non vedi i cambiamenti?** Aspetta ancora un minuto e premi Ctrl \+ F5 (ricarica forzata). Se il sito si rompe: apri **History** , guardi la versione di prima e la ricopi. Con Git **niente si perde**.

**পরিবর্তন দেখছ না?** আরও এক মিনিট অপেক্ষা করে Ctrl \+ F5 চাপো। সাইট ভেঙে গেলে: **History** খুলে আগের সংস্করণ দেখে আবার কপি করো। Git-এ **কিছুই হারায় না** ।

**Carta e penna:** disegna una linea del tempo con i tuoi commit (pallino = versione) e scrivi sotto cosa hai cambiato in ognuno.

**কাগজ-কলম:** তোমার commit-গুলো দিয়ে একটি সময়রেখা আঁকো (বিন্দু = সংস্করণ) এবং নিচে লেখো প্রতিটিতে কী বদলেছ।

Classe 3 · Dispensa 3 · v1.0
