# Verifica sul versioning e il merge

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 14/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 14/10/2026, Laboratorio.
2. **Argomenti:** Verifica sul versioning (fork, Pull Request, merge, changelog); revisione del backlog Agile con le richieste al gioco del treno.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Le versioni e il changelog · ১. সংস্করণ ও changelog

<div class="scheda">Una <b>versione</b> è un salvataggio del gioco con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Il numero ha due parti: <b>major.minor</b>. Da v1.4 a v1.5 cambia il numero dopo il punto: è un passo piccolo, <b>minor</b>. Da v1.5 a v2.0 cambia il primo numero: è un cambio grande, <b>major</b> (per esempio un motore nuovo). Il <b>changelog</b> è il registro di tutte le modifiche, versione per versione: che cosa è cambiato e da quale richiesta. Un programma <b>cambia</b> perché chi lo usa chiede cose nuove e perché si trovano <b>difetti</b> da sistemare: nella v1.4 Dani e Ale hanno trovato che il cielo cambiava in ritardo, ed è stato sistemato. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>সংস্করণ</b> মানে খেলার একটি সেভ: একটি <b>নম্বর</b> আর কী বদলেছে তার একটি লাইন। নম্বরের দুই অংশ: <b>major.minor</b>। v1.4 থেকে v1.5: ছোট পরিবর্তন (<b>minor</b>)। v1.5 থেকে v2.0: বড় পরিবর্তন (<b>major</b>)। <b>changelog</b> হলো সব পরিবর্তনের তালিকা। প্রোগ্রাম বদলায়, কারণ মানুষ নতুন জিনিস চায় আর ভুল ঠিক করতে হয়।</span></div>

#### 2. Fork, ramo e merge · ২. fork, শাখা ও merge

<div class="scheda">L'08/10 la 3INF ha fatto il suo <b>fork</b>: una <b>copia</b> del treno della 2INF (versione v0.11), per lavorarci senza toccare il gioco della 2INF. Da lì è partita la v1.0 della 3INF. Un <b>ramo</b> (branch) è una strada di lavoro parallela nello stesso progetto. Il <b>merge</b> unisce una modifica (o un ramo) dentro il gioco: lo fa il prof quando accetta una Pull Request. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">০৮/১০ তারিখে 3INF <b>fork</b> করেছে: 2INF-এর ট্রেন খেলার একটি <b>কপি</b> (v0.11), যাতে ওদের খেলা না বদলায়। <b>শাখা</b> (branch) মানে একই প্রজেক্টে পাশাপাশি আরেকটি কাজের রাস্তা। <b>merge</b> মানে একটি পরিবর্তন খেলার সাথে যোগ করা: শিক্ষক Pull Request গ্রহণ করলে এটা করেন।</span></div>

#### 3. La Pull Request · ৩. Pull Request

<div class="scheda">Una <b>Pull Request</b> (PR) è una <b>richiesta di modifica scritta</b>. Ha quattro parti: <b>Titolo</b>, <b>Cosa cambia</b>, <b>Dove</b> (in quale punto del gioco), <b>Perché</b>. L'08/10 le squadre SCENARI, PERSONAGGI, MOTORE FISICA e TEST QUALITÀ hanno mandato le PR dalla #1 alla #21: da quelle sono nate le versioni dalla v1.1 alla v1.4. Lunedì 12/10 sono arrivate 14 richieste: da queste nascono oggi le versioni nuove, dalla v1.5 in poi. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>Pull Request</b> (PR) মানে লিখিত একটি পরিবর্তনের অনুরোধ। এর চারটি অংশ: <b>শিরোনাম</b>, <b>কী বদলাবে</b>, <b>কোথায়</b>, <b>কেন</b>। ০৮/১০-এ দলগুলো PR #1 থেকে #21 পাঠিয়েছে: তা থেকে v1.1 থেকে v1.4 হয়েছে। ১২/১০-এ ১৪টি অনুরোধ এসেছে: আজ তা থেকে v1.5 আর পরের সংস্করণ হচ্ছে।</span></div>

#### 4. Il backlog e i pesi · ৪. backlog ও ওজন

<div class="scheda">Il <b>backlog</b> è la coda dei lavori: tutte le richieste, in ordine. Ogni richiesta ha un <b>peso</b>: quanto lavoro serve sul codice. I pesi sono i numeri di <b>Fibonacci</b>: 1, 2, 3, 5, 8 (ogni numero è la somma dei due prima). 1 = un colore, 2 = un numero nelle regole, 3 = un personaggio, 5 = un ambiente, 8 = due cose insieme o una regola nuova. Si fanno prima le richieste più leggere; a parità di peso, chi è arrivato prima. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>backlog</b> মানে কাজের সারি: সব অনুরোধ, ক্রম অনুযায়ী। প্রতিটি অনুরোধের একটি <b>ওজন</b> আছে: কোডে কত কাজ লাগবে। ওজন হলো Fibonacci সংখ্যা: ১, ২, ৩, ৫, ৮ (প্রতিটি আগের দুইটির যোগফল)। ১ = একটি রং, ২ = একটি সংখ্যা, ৩ = একটি চরিত্র, ৫ = একটি পরিবেশ, ৮ = দুইটি জিনিস একসাথে। আগে হালকা কাজ হয়।</span></div>

#### 5. Agile: sprint e retrospettiva · ৫. Agile: sprint ও retrospettiva

<div class="scheda"><b>Agile</b> è un modo di lavorare delle aziende di software. Il <b>Manifesto Agile</b> dice, per esempio: un programma che <b>funziona</b> conta più di tanti documenti; <b>rispondere ai cambiamenti</b> conta più che seguire un piano fisso; le <b>persone</b> e il parlarsi contano più degli strumenti. Si lavora a <b>sprint</b>: giri di lavoro brevi, con un obiettivo, alla fine dei quali esce una versione che funziona. Alla fine dello sprint c'è la <b>retrospettiva</b>: la squadra dice che cosa è andato bene e che cosa migliorare. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px"><b>Agile</b> হলো সফটওয়্যার কোম্পানির কাজের একটি পদ্ধতি। <b>Agile Manifesto</b> বলে: চালু প্রোগ্রাম অনেক কাগজের চেয়ে বেশি জরুরি; পরিবর্তনে সাড়া দেওয়া নির্দিষ্ট পরিকল্পনার চেয়ে বেশি জরুরি; মানুষ আর কথা বলা যন্ত্রের চেয়ে বেশি জরুরি। কাজ হয় <b>sprint</b>-এ: ছোট কাজের পালা, একটি লক্ষ্য, শেষে একটি চালু সংস্করণ। শেষে <b>retrospettiva</b>: দল বলে কী ভালো হয়েছে আর কী ভালো করা যায়।</span></div>

#### 6. Le regole della squadra · ৬. দলের নিয়ম

<div class="scheda">Il gioco è di <b>tutta la classe</b>. Regola: <b>aggiungere sì, cancellare no</b>. Il cattivo Travor l'ha chiesto Tomas: se hai un'idea, aggiungi un personaggio tuo, non cancelli quello di un compagno. Il gioco è <b>pubblico</b>: lo vede chiunque su Internet. Per questo <b>niente foto di persone vere</b> (privacy): lunedì 3 richieste sono state respinte per questo motivo. Si possono rimandare con un personaggio disegnato o di un videogioco. <span lang="bn" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:3px">খেলাটি <b>পুরো ক্লাসের</b>। নিয়ম: <b>যোগ করা যায়, মুছে ফেলা যায় না</b>। Travor চরিত্রটি Tomas চেয়েছিল: তোমার নতুন ধারণা থাকলে নিজের চরিত্র যোগ করো, বন্ধুরটা মুছে ফেলো না। খেলাটি ইন্টারনেটে <b>সবাই দেখতে পায়</b>। তাই <b>আসল মানুষের ছবি নয়</b> (গোপনীয়তা): সোমবার এই কারণে ৩টি অনুরোধ বাতিল হয়েছে। আঁকা চরিত্র বা ভিডিও গেমের চরিত্র দিয়ে আবার পাঠানো যায়।</span></div>


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
