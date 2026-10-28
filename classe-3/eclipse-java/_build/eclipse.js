// 28/10/2026 3INF, Laboratorio 12-14: Java con Eclipse portabile, dalla cartella al primo programma.
// Nessuno conosce Eclipse: ogni passo dice DOVE è la cosa sullo schermo, con il nome inglese esatto e la traduzione.
// Italiano + una riga in bangla (PC 14). Uso: node eclipse.js -> docs/verifica/banche/3inf-eclipse-java.js (+ stato).
// Codici Java verificati con javac 21 (Main a console e Finestra Swing).
const fs = require('fs'), path = require('path'); const DOCS = path.join(__dirname, '../../../docs/');
const bn = t => '<p lang="bn" style="color:#5b6573;margin-top:-6px">' + t + '</p>';
const k = t => '<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">' + t + '</code>';
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const box = t => '<pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:16px;overflow-x:auto">' + t + '</pre>';
const tab = (h, r) => '<div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr>' + h.map(x => '<th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">' + x + '</th>').join('') + '</tr>' +
  r.map(rr => '<tr>' + rr.map(x => '<td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">' + x + '</td>').join('') + '</tr>').join('') + '</table></div>';
const p = (it, b) => '<p>' + it + '</p>' + (b ? bn(b) : '');
const passo = (n, it, b) => p('<b>' + n + '.</b> ' + it, b);
const FATTO = (it, b) => '<div style="background:#e8f7ee;border:2px solid #2f855a;border-radius:10px;padding:8px 12px;margin:10px 0"><p style="margin:0"><b>FATTO!</b> ' + it + '</p>' + bn('<b>হয়ে গেছে!</b> ' + b) + '</div>';
// riquadro con il bottone «Copia» (il codice si copia con un clic)
const boxc = t => '<div style="position:relative">' + box(esc(t)) + '<button type="button" onclick="var b=this;navigator.clipboard.writeText(b.previousElementSibling.innerText).then(function(){b.textContent=\'Copiato!\';setTimeout(function(){b.textContent=\'Copia\'},2000)})" style="position:absolute;top:6px;right:6px;background:#2f855a;color:#fff;border:0;border-radius:8px;padding:6px 12px;font-size:15px;font-weight:bold;cursor:pointer">Copia</button></div>';
const en = (t, it) => '<b>«' + t + '»</b> (' + it + ')';   // nome inglese esatto in Eclipse + traduzione
const NOTA = (it, b) => '<div style="background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:8px 12px;margin:10px 0"><p style="margin:0">' + it + '</p>' + bn(b) + '</div>';
const STOP = (it, b) => '<div style="background:#fde8e8;border:2px solid #c53030;border-radius:10px;padding:8px 12px;margin:10px 0"><p style="margin:0">' + it + '</p>' + bn(b) + '</div>';
const ZIP = 'eclipse-java-2026-09-R-win32-x86_64';
const MAIN = 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello World");\n    }\n}';
const SWING = 'import javax.swing.*;\n\npublic class Finestra {\n    public static void main(String[] args) {\n        JFrame finestra = new JFrame("Il mio saluto");\n        JTextField casella = new JTextField(12);\n        JButton bottone = new JButton("Saluta");\n        bottone.addActionListener(e ->\n            JOptionPane.showMessageDialog(null, "Ciao " + casella.getText() + "!"));\n        JPanel pannello = new JPanel();\n        pannello.add(casella);\n        pannello.add(bottone);\n        finestra.add(pannello);\n        finestra.setSize(350, 120);\n        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n        finestra.setVisible(true);\n    }\n}';
const MAPPA =
'+------------------------------------------------------------+\n' +
'| File  Edit  Source  Refactor  Navigate  Search  Project  Run | <- BARRA DEI MENU (in alto)\n' +
'| [ ] [ ] [ ] ... ( > ) ...                                  | <- BARRA DEI BOTTONI: ( > ) verde = Run\n' +
'+----------------+-------------------------------------------+\n' +
'| Package        |                                           |\n' +
'| Explorer       |   EDITOR                                  |\n' +
'|                |   qui scrivi il codice                    |\n' +
'| > HelloWorld   |   (Main.java)                             |\n' +
'|   > src        |                                           |\n' +
'|     Main.java  |                                           |\n' +
'| (A SINISTRA:   |   (AL CENTRO)                             |\n' +
'|  i progetti)   |                                           |\n' +
'+----------------+-------------------------------------------+\n' +
'| Problems   Javadoc   Declaration   Console                 | <- schede IN BASSO\n' +
'| Hello World                <- qui esce quello che stampi   |\n' +
'+------------------------------------------------------------+';
const S = [];
S.push({ titolo: '1. Oggi: Java con Eclipse, senza installare niente · আজ: Eclipse দিয়ে Java, কিছু ইনস্টল না করে',
  testo: '<a href="../3inf-eclipse-guida/" style="display:block;text-align:center;background:#1f6feb;color:#fff;font-weight:bold;font-size:20px;text-decoration:none;border-radius:12px;padding:14px 12px;margin:0 0 12px">LA GUIDA CON LE FOTO: Eclipse passo per passo, fino al bottone Hello World<span lang="bn" style="display:block;font-weight:normal;font-size:16px;margin-top:4px">ছবিসহ গাইড: ধাপে ধাপে Eclipse, Hello World বোতাম পর্যন্ত</span></a>' +
    '<div style="background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 6px"><b>Questa pagina cambia durante la lezione: ogni tanto premi F5 per vedere la versione nuova.</b></p>' + bn('<b>এই পাতাটি ক্লাসের সময় বদলায়: মাঝে মাঝে F5 চাপো, নতুন সংস্করণ দেখতে।</b>') + '</div>' +
    p('Oggi scrivi il tuo primo programma Java in un programma vero da programmatori: <b>Eclipse</b>.', 'আজ তুমি প্রোগ্রামারদের আসল প্রোগ্রাম Eclipse-এ তোমার প্রথম Java প্রোগ্রাম লিখবে।') +
    p('Eclipse è un <b>IDE</b> (si legge «ài-di-ì»), cioè un <b>ambiente di sviluppo</b>: un unico programma che contiene tre cose.', 'Eclipse একটি IDE, মানে উন্নয়নের পরিবেশ: একটি প্রোগ্রামের ভিতরে তিনটি জিনিস।') +
    tab(['Pezzo', 'Che cosa fa', 'In Lazarus'], [
      ['1. Editor', 'il foglio dove scrivi il codice', 'la finestra del codice (unit1.pas)'],
      ['2. Compilatore', 'traduce il codice nella lingua del computer e trova gli errori', 'Compila'],
      ['3. Esecuzione', 'fa partire il programma', 'il triangolo verde Esegui (F9)']]) +
    bn('১. Editor: কোড লেখার পাতা। ২. Compiler: কোড কম্পিউটারের ভাষায় অনুবাদ করে আর ভুল খোঁজে। ৩. চালানো: প্রোগ্রাম শুরু করে। Lazarus-ও একটি IDE।') +
    p('Anche <b>Lazarus è un IDE</b>: tu lo conosci già. Eclipse è la stessa idea, ma per Java.', 'Lazarus-ও একটি IDE: তুমি এটা চেনো। Eclipse একই ধারণা, কিন্তু Java-র জন্য।') +
    p('Eclipse qui è <b>portabile</b>: non si installa. È una cartella dentro un file ZIP (un pacchetto compresso): la apri («scompatti») e fai doppio clic sul programma. Dentro c\'è già anche Java. Per questo funziona a scuola senza chiedere niente al tecnico.', 'এখানে Eclipse পোর্টেবল: ইনস্টল করতে হয় না। এটি একটি ZIP ফাইলের ভিতরে একটি ফোল্ডার: খুলে (আনজিপ করে) প্রোগ্রামে দুবার ক্লিক করো। ভিতরে Java-ও আছে।') +
    NOTA('Eclipse è <b>in inglese</b>. In questa pagina trovi il nome inglese esatto di ogni menu e bottone, e accanto la traduzione italiana tra parentesi.', 'Eclipse ইংরেজিতে। এই পাতায় প্রতিটি মেনু আর বোতামের সঠিক ইংরেজি নাম আছে, পাশে বন্ধনীতে ইতালীয় অনুবাদ।') +
    tab(['Parte', 'Che cosa fai', 'Schede'], [
      ['A. Preparare', 'prendi lo ZIP, scompattalo, apri Eclipse', '2, 3, 4'],
      ['B. Programmare', 'il progetto HelloWorld e la prova a console', '5, 6'],
      ['C. LA META', '<b>una finestra con un bottone: lo premi e compare «Hello World»</b>', '7, 8, 9'],
      ['D. Consegna', 'lo screenshot nel Documento su Classroom, entro le 14:00', '10'],
      ['E. Per chi ha finito', 'il saluto con il tuo nome (facoltativo)', '11']]) +
    bn('A: ZIP নাও, আনজিপ করো, Eclipse খোলো। B: HelloWorld প্রজেক্ট আর কনসোলে পরীক্ষা। C: লক্ষ্য: বোতামসহ জানালা, চাপলে «Hello World» আসে। D: Classroom-এ স্ক্রিনশট, ১৪:০০-এর মধ্যে। E: যারা শেষ করেছে: তোমার নাম দিয়ে শুভেচ্ছা।') });
S.push({ titolo: '2. La mappa dello schermo di Eclipse · Eclipse-এর পর্দার মানচিত্র',
  testo: p('Prima di cominciare, guarda com\'è fatta la finestra di Eclipse. Ti servono solo <b>5 zone</b>.', 'শুরু করার আগে Eclipse-এর জানালাটা দেখো। শুধু ৫টি জায়গা দরকার।') +
    box(esc(MAPPA)) +
    tab(['Dove', 'Nome in Eclipse', 'A che cosa serve'], [
      ['in alto, la prima riga di parole', 'la barra dei menu: ' + en('File', 'File') + ', ' + en('Run', 'Esegui') + '…', 'i comandi, come in Lazarus'],
      ['in alto, sotto i menu', 'la barra dei bottoni; il <b>cerchio verde con il triangolo bianco</b> è ' + en('Run', 'Esegui'), 'fa partire il programma'],
      ['a sinistra', en('Package Explorer', 'Esplora pacchetti'), 'l\'elenco dei tuoi progetti e dei tuoi file'],
      ['al centro, la parte grande', 'l\'<b>editor</b>', 'qui scrivi il codice'],
      ['in basso', 'la scheda ' + en('Console', 'Console'), 'qui compare quello che il programma scrive']]) +
    bn('উপরে: মেনু (File, Run)। মেনুর নিচে: বোতাম; সবুজ বৃত্তে সাদা ত্রিভুজ = Run (চালাও)। বামে: Package Explorer (তোমার প্রজেক্ট আর ফাইল)। মাঝখানে: editor (কোড লেখো)। নিচে: Console (প্রোগ্রাম যা লেখে)।') +
    p('Il triangolo verde lo conosci già: in Lazarus fa la stessa cosa.', 'সবুজ ত্রিভুজ তুমি চেনো: Lazarus-এও একই কাজ করে।') });
S.push({ titolo: '3. Prendi lo ZIP e scompattalo in una cartella corta · ZIP নাও আর ছোট নামের ফোল্ডারে আনজিপ করো',
  testo: p('Il prof ti manda il file <b>' + ZIP + '.zip</b> (360 MB) sul tuo computer.', 'প্রফেসর তোমার কম্পিউটারে ' + ZIP + '.zip ফাইলটি (৩৬০ MB) পাঠাবেন।') +
    passo(1, 'Apri <b>Esplora file</b>: l\'icona della <b>cartella gialla</b> nella barra in basso dello schermo (oppure premi ' + k('Win') + ' + ' + k('E') + ').', 'Esplora file খোলো: স্ক্রিনের নিচের বারে হলুদ ফোল্ডারের আইকন (বা Win + E)।') +
    passo(2, 'Il file è nella tua cartella personale. Per trovarlo: in Esplora file clicca nella <b>casella di ricerca in alto a destra</b>, scrivi ' + k('eclipse-java') + ' e aspetta che compaia il file con la cerniera (l\'icona dello ZIP).', 'ফাইলটি তোমার ব্যক্তিগত ফোল্ডারে। Esplora file-এ উপরে ডানদিকে খোঁজার ঘরে ক্লিক করো, eclipse-java লেখো, চেনওয়ালা (ZIP) ফাইল আসা পর্যন্ত অপেক্ষা করো।') +
    p('Se il prof ti dice di prenderlo dal disco <b>P:</b>, nel pannello a sinistra di Esplora file clicca <b>P:</b> e poi la cartella che ti indica.', 'প্রফেসর P: ডিস্ক থেকে নিতে বললে, Esplora file-এর বামে P: ক্লিক করো, তারপর যে ফোল্ডার বলবেন।') +
    passo(3, 'Clic <b>destro</b> sul file ZIP → <b>Estrai tutto…</b>', 'ZIP ফাইলে ডান ক্লিক → Estrai tutto…') +
    passo(4, 'Clicca il bottone verde <b>Copia</b> qui sotto: è una cartella dal nome corto.', 'নিচের সবুজ Copia বোতামে ক্লিক করো: ছোট নামের একটি ফোল্ডার।') + boxc('C:\\Users\\Public\\ec') +
    passo(5, 'Nella finestra di Estrai tutto clicca nella casella del percorso (la riga lunga con ' + k('C:\\Users\\…') + '), premi ' + k('Ctrl') + ' + ' + k('A') + ' e poi ' + k('Ctrl') + ' + ' + k('V') + '.', 'Estrai tutto জানালায় পথের ঘরে ক্লিক (C:\\Users\\… লেখা লম্বা লাইন), Ctrl + A তারপর Ctrl + V।') +
    NOTA('Perché una cartella corta: Eclipse contiene file con nomi lunghissimi. Se il percorso è troppo lungo, Windows non riesce a scompattarli tutti ed Eclipse non parte.', 'ছোট ফোল্ডার কেন: Eclipse-এ খুব লম্বা নামের ফাইল আছে। পথ বেশি লম্বা হলে Windows সব আনজিপ করতে পারে না, Eclipse চালু হয় না।') +
    passo(6, 'Clicca il bottone <b>Estrai</b> in basso a destra.', 'নিচে ডানদিকে Estrai বোতামে ক্লিক করো।') +
    NOTA('<b>Dura qualche minuto</b> (sono migliaia di file): la barra verde avanza piano. È normale: aspetta che la finestra si chiuda da sola e non chiudere niente.', 'কয়েক মিনিট লাগে (হাজার হাজার ফাইল): সবুজ বার ধীরে এগোয়। স্বাভাবিক: জানালা নিজে বন্ধ হওয়া পর্যন্ত অপেক্ষা করো।') +
    p('Se Windows dice che non puoi scrivere in ' + k('C:\\Users\\Public') + ': rifai i passi 3-6 e incolla invece questo percorso, poi sostituisci <b>nome.cognome</b> con il tuo:', 'C:\\Users\\Public-এ লিখতে না দিলে: ৩-৬ ধাপ আবার করো, এই পথ পেস্ট করো, nome.cognome-এর জায়গায় তোমারটা লেখো:') + boxc('C:\\Users\\nome.cognome\\Documents\\ec') +
    passo(7, 'Alla fine Windows apre la cartella <b>ec</b>. Dentro c\'è la cartella <b>eclipse</b>: doppio clic per entrare.', 'শেষে Windows ec ফোল্ডার খুলবে। ভিতরে eclipse ফোল্ডার: দুবার ক্লিক করে ঢোকো।') +
    passo(8, '<b>Controllo:</b> dentro <b>eclipse</b> devono esserci le tre cartelle <b>configuration</b>, <b>features</b> e <b>plugins</b>.', 'যাচাই: eclipse-এর ভিতরে তিনটি ফোল্ডার থাকতে হবে: configuration, features, plugins।') +
    STOP('Se le vedi solo 6 cose e mancano <b>plugins</b> e <b>features</b>: l\'estrazione non è finita. Chiudi Esplora file, cancella la cartella <b>ec</b> e rifai dal passo 3, aspettando la fine.', 'যদি শুধু ৬টি জিনিস থাকে আর plugins, features না থাকে: আনজিপ শেষ হয়নি। ec ফোল্ডার মুছে ৩ নম্বর ধাপ থেকে আবার করো, শেষ পর্যন্ত অপেক্ষা করো।') +
    FATTO('Hai la cartella ' + k('C:\\Users\\Public\\ec\\eclipse') + ' con dentro plugins. Il programma è pronto, senza installare niente.', 'ec\\eclipse ফোল্ডারে plugins আছে। কিছু ইনস্টল না করেই প্রোগ্রাম তৈরি।') });
S.push({ titolo: '4. Primo avvio di Eclipse · Eclipse প্রথমবার চালু করা',
  testo: passo(1, 'Nella cartella <b>ec\\eclipse</b> cerca il file <b>eclipse.exe</b>: ha l\'icona di un <b>cerchio viola</b> (a volte si vede solo «eclipse», senza «.exe»). Doppio clic.', 'eclipse ফোল্ডারে eclipse.exe খোঁজো: বেগুনি বৃত্তের আইকন (কখনো শুধু «eclipse» দেখায়)। দুবার ক্লিক।') +
    NOTA('Se compare la finestra blu <b>«Windows ha protetto il PC»</b>: clicca la scritta <b>Ulteriori informazioni</b>, poi il bottone <b>Esegui comunque</b>.', 'নীল জানালা «Windows ha protetto il PC» এলে: Ulteriori informazioni লেখায় ক্লিক, তারপর Esegui comunque বোতাম।') +
    STOP('Se Windows dice che l\'app è <b>bloccata dall\'amministratore</b>: fermati e chiama il prof. Non è colpa tua: oggi si userà Java nel sito web.', 'Windows যদি বলে অ্যাপটি অ্যাডমিন ব্লক করেছে: থামো আর প্রফেসরকে ডাকো। তোমার দোষ নয়: আজ ওয়েবসাইটে Java ব্যবহার হবে।') +
    passo(2, 'Aspetta: Eclipse si apre piano la prima volta (anche un minuto).', 'অপেক্ষা করো: প্রথমবার Eclipse ধীরে খোলে (এক মিনিট পর্যন্ত)।') +
    passo(3, 'Compare la finestra ' + en('Select a directory as workspace', 'Scegli una cartella come area di lavoro') + '. Il <b>workspace</b> è la cartella dove Eclipse salva i tuoi progetti. Non cambiare niente: clicca il bottone ' + en('Launch', 'Avvia') + ' in basso a destra.', '«Select a directory as workspace» জানালা আসবে। workspace হলো যে ফোল্ডারে Eclipse তোমার প্রজেক্ট রাখে। কিছু বদলিও না: নিচে ডানদিকে Launch ক্লিক করো।') +
    passo(4, 'Si apre la pagina ' + en('Sponsor the Eclipse IDE', 'Sostieni Eclipse') + ' con dei bottoni arancioni. Clicca il bottone arancione ' + en('Later', 'Più tardi') + '.', '«Sponsor the Eclipse IDE» পাতা খুলবে, কমলা বোতামসহ। কমলা Later (পরে) বোতামে ক্লিক করো।') +
    passo(5, 'In alto ci sono altre linguette (schede) aperte, per esempio ' + en('Install Java 27 Support', 'Installa il supporto a Java 27') + ' e ' + en('Eclipse IDE for Java Developers 2026-12 M1', 'notizie sulla prossima versione') + '. Non servono: chiudile una alla volta con la <b>✕</b> accanto al loro nome.', 'উপরে আরও ট্যাব খোলা আছে, যেমন Install Java 27 Support আর Eclipse IDE for Java Developers 2026-12 M1। দরকার নেই: নামের পাশের ✕ দিয়ে একটা একটা করে বন্ধ করো।') +
    passo(6, 'Ora rimetti in ordine le zone dello schermo. In alto clicca il menu ' + en('Window', 'Finestra') + '.', 'এখন পর্দার জায়গাগুলো ঠিক করো। উপরে Window (জানালা) মেনুতে ক্লিক করো।') +
    passo(7, 'Porta il mouse su ' + en('Perspective', 'Vista') + ' e clicca ' + en('Reset Perspective…', 'Ripristina la vista') + '.', 'Perspective-এর উপর মাউস রাখো, Reset Perspective… ক্লিক করো।') +
    passo(8, 'Nella finestrella clicca il bottone ' + en('Reset', 'Ripristina') + '. Ora a sinistra compare il riquadro ' + en('Package Explorer', 'Esplora pacchetti') + '.', 'ছোট জানালায় Reset বোতামে ক্লিক করো। এখন বামে Package Explorer দেখা যাবে।') +
    NOTA('Se a sinistra vedi ancora solo icone piccole: menu ' + en('Window', 'Finestra') + ' → ' + en('Show View', 'Mostra vista') + ' → ' + en('Package Explorer', 'Esplora pacchetti') + '.', 'বামে এখনো শুধু ছোট আইকন থাকলে: Window → Show View → Package Explorer।') +
    p('Ora vedi lo schermo della mappa (scheda 2): a sinistra ' + en('Package Explorer', 'Esplora pacchetti') + ', ancora vuoto.', 'এখন মানচিত্রের পর্দা দেখছো (কার্ড ২): বামে Package Explorer, এখনো খালি।') +
    FATTO('Eclipse è aperto.', 'Eclipse খোলা হয়েছে।') });
const GUI = 'import javax.swing.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        JFrame finestra = new JFrame("Il mio primo programma");\n        JButton bottone = new JButton("Premi qui");\n        JLabel scritta = new JLabel("...");\n        bottone.addActionListener(e -> scritta.setText("Hello World"));\n        JPanel pannello = new JPanel();\n        pannello.add(bottone);\n        pannello.add(scritta);\n        finestra.add(pannello);\n        finestra.setSize(300, 120);\n        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n        finestra.setVisible(true);\n    }\n}';
S.push({ titolo: '5. Il progetto nuovo «HelloWorld» · নতুন প্রজেক্ট «HelloWorld»',
  testo: p('Come in Lazarus: <b>un progetto = una cartella</b>. Eclipse la crea da solo nel workspace.', 'Lazarus-এর মতো: একটি প্রজেক্ট = একটি ফোল্ডার। Eclipse নিজেই workspace-এ বানায়।') +
    passo(1, 'A sinistra, nel riquadro ' + en('Package Explorer', 'Esplora pacchetti') + ', clicca la scritta blu ' + en('Create a Java project', 'Crea un progetto Java') + '.', 'বামে Package Explorer-এ নীল লেখা Create a Java project-এ ক্লিক করো।') +
    p('Se la scritta blu non c\'è: in alto a sinistra menu ' + en('File', 'File') + ' → ' + en('New', 'Nuovo') + ' → ' + en('Java Project', 'Progetto Java') + '.', 'নীল লেখা না থাকলে: উপরে বামে File → New → Java Project।') +
    passo(2, 'Nella casella in alto ' + en('Project name', 'Nome del progetto') + ' scrivi (tutto attaccato):', 'উপরের Project name ঘরে লেখো (একসাথে):') + boxc('HelloWorld') +
    passo(3, 'Scendi in fondo alla finestra, nella parte ' + en('Module', 'Modulo') + ': <b>togli la spunta</b> a ' + en('Create module-info.java file', 'Crea il file module-info.java') + '.', 'জানালার নিচে Module অংশে: Create module-info.java file-এর টিক তুলে দাও।') +
    p('Perché: quel file serve per i programmi grandi, divisi in tanti pezzi; per il nostro programma piccolo dà solo fastidio.', 'কারণ: ওই ফাইল বড় প্রোগ্রামের জন্য; আমাদের ছোট প্রোগ্রামে শুধু ঝামেলা করে।') +
    passo(4, 'Clicca il bottone ' + en('Finish', 'Fine') + ' in basso a destra.', 'নিচে ডানদিকে Finish ক্লিক করো।') +
    p('Se compare una domanda su ' + en('Open Associated Perspective?', 'Aprire la vista collegata?') + ': clicca ' + en('Open Perspective', 'Apri la vista') + '.', '«Open Associated Perspective?» প্রশ্ন এলে: Open Perspective ক্লিক করো।') +
    FATTO('A sinistra, nel Package Explorer, c\'è il progetto <b>HelloWorld</b>.', 'বামে Package Explorer-এ HelloWorld প্রজেক্ট আছে।') });
S.push({ titolo: '6. La classe Main e la prova veloce: Hello World nella Console · Main ক্লাস আর দ্রুত পরীক্ষা: Console-এ Hello World',
  testo: passo(1, 'A sinistra, nel Package Explorer, clicca la <b>freccina ></b> accanto a <b>HelloWorld</b>: compare la cartella <b>src</b> (da «source», il codice).', 'বামে HelloWorld-এর পাশের > তীরে ক্লিক করো: src ফোল্ডার দেখা যাবে (source = কোড)।') +
    passo(2, 'Clic <b>destro</b> su <b>src</b> → ' + en('New', 'Nuovo') + ' → ' + en('Class', 'Classe') + '.', 'src-এ ডান ক্লিক → New → Class।') +
    passo(3, 'Nella finestra, casella ' + en('Package', 'Pacchetto') + ': cliccaci dentro, premi ' + k('Ctrl') + ' + ' + k('A') + ' e poi ' + k('Canc') + ': deve restare <b>vuota</b>. Compare un avviso giallo: va bene così.', 'Package ঘরে ক্লিক, Ctrl + A তারপর Canc: ঘরটি খালি থাকবে। হলুদ সতর্কবার্তা আসবে: ঠিক আছে।') +
    passo(4, 'Nella casella ' + en('Name', 'Nome') + ' scrivi (con la M maiuscola):', 'Name ঘরে লেখো (বড় হাতের M):') + boxc('Main') +
    passo(5, 'Più sotto metti la spunta a ' + en('public static void main(String[] args)', 'crea il punto di partenza main') + '.', 'নিচে public static void main(String[] args)-এ টিক দাও।') +
    passo(6, 'Clicca ' + en('Finish', 'Fine') + ' in basso a destra. Al centro, nell\'editor, si apre il file <b>Main.java</b>.', 'Finish ক্লিক করো। মাঝখানে editor-এ Main.java খুলবে।') +
    passo(7, 'Clicca <b>Copia</b> qui sotto.', 'নিচে Copia ক্লিক করো।') + boxc(MAIN) +
    passo(8, 'Clicca dentro l\'editor (al centro), premi ' + k('Ctrl') + ' + ' + k('A') + ' (seleziona tutto), poi ' + k('Ctrl') + ' + ' + k('V') + ' (incolla), poi ' + k('Ctrl') + ' + ' + k('S') + ' (salva).', 'editor-এ ক্লিক, Ctrl + A (সব বাছো), Ctrl + V (পেস্ট), Ctrl + S (সেভ)।') +
    passo(9, 'In alto clicca il <b>cerchio verde con il triangolo bianco</b> ' + en('Run', 'Esegui') + '. Oppure ' + k('Ctrl') + ' + ' + k('F11') + '. Se compare ' + en('Save and Launch', 'Salva e avvia') + ': ' + en('OK', 'OK') + '.', 'উপরে সবুজ বৃত্তে সাদা ত্রিভুজ Run। বা Ctrl + F11। Save and Launch এলে: OK।') +
    passo(10, 'Guarda <b>in basso</b>, nella scheda ' + en('Console', 'Console') + ': c\'è scritto <b>Hello World</b>.', 'নিচে Console ট্যাবে দেখো: Hello World লেখা আছে।') +
    FATTO('Run funziona: Eclipse compila ed esegue. Ora la meta vera: la finestra con il bottone (scheda 7).', 'Run কাজ করছে। এখন আসল লক্ষ্য: বোতামসহ জানালা (কার্ড ৭)।') });
S.push({ titolo: '7. LA META: una finestra con un bottone che scrive «Hello World» · লক্ষ্য: বোতামসহ জানালা যা «Hello World» লেখে',
  testo: p('Ora fai un programma con la finestra, come quelli di Lazarus: un <b>bottone</b> e una <b>scritta</b>. Premi il bottone e la scritta diventa <b>Hello World</b>. In Java la finestra non si disegna con il mouse: si scrive con il codice (si chiama <b>Swing</b>).', 'এখন Lazarus-এর মতো জানালাসহ প্রোগ্রাম বানাও: একটি বোতাম আর একটি লেখা। বোতাম চাপলে লেখাটি Hello World হয়। Java-তে জানালা মাউসে আঁকা হয় না: কোডে লেখা হয় (Swing)।') +
    passo(1, 'Clicca <b>Copia</b> qui sotto.', 'নিচে Copia ক্লিক করো।') + boxc(GUI) +
    passo(2, 'Clicca dentro l\'editor di <b>Main.java</b> (al centro), ' + k('Ctrl') + ' + ' + k('A') + ', ' + k('Ctrl') + ' + ' + k('V') + ', ' + k('Ctrl') + ' + ' + k('S') + '.', 'Main.java-র editor-এ ক্লিক, Ctrl + A, Ctrl + V, Ctrl + S।') +
    passo(3, 'Clicca il triangolo verde ' + en('Run', 'Esegui') + ' in alto.', 'উপরে সবুজ Run ক্লিক করো।') +
    passo(4, 'Si apre una finestrella nuova «Il mio primo programma» (può comparire dietro Eclipse: guarda nella barra in basso dello schermo). Clicca <b>Premi qui</b>.', 'নতুন ছোট জানালা «Il mio primo programma» খুলবে (Eclipse-এর পিছনে থাকতে পারে: স্ক্রিনের নিচের বারে দেখো)। Premi qui ক্লিক করো।') +
    FATTO('Accanto al bottone compare <b>Hello World</b>. Il tuo primo programma Java con la finestra!', 'বোতামের পাশে Hello World দেখা যাবে। জানালাসহ তোমার প্রথম Java প্রোগ্রাম!') +
    passo(5, '<b>Fallo tuo:</b> cambia il titolo «Il mio primo programma» e la scritta del bottone «Premi qui» con parole tue (lascia le virgolette ' + k('"') + '). Salva e Run di nuovo.', 'নিজের মতো করো: «Il mio primo programma» শিরোনাম আর «Premi qui» বোতামের লেখা বদলাও (" রেখে দাও)। সেভ করে আবার Run।') +
    p('Per chiudere il programma: la <b>X</b> della finestrella.', 'প্রোগ্রাম বন্ধ করতে: ছোট জানালার X।') });
S.push({ titolo: '8. Riga per riga, e il confronto con Lazarus · লাইন ধরে ধরে, Lazarus-এর সাথে তুলনা',
  testo: box(esc(GUI)) +
    tab(['Riga', 'Che cosa vuol dire', 'In Lazarus'], [
      [k('import javax.swing.*;'), 'prende i pezzi per fare le finestre', k('uses') + ' in cima alla unit'],
      [k('public class Main {'), 'tutto sta dentro una <b>classe</b>; il nome <b>Main</b> è uguale al file Main.java', 'la unit'],
      [k('public static void main(…) {'), 'il punto di partenza: il programma comincia da qui', 'il file .lpr'],
      [k('new JFrame("…")'), 'crea la finestra con il suo titolo', 'il Form, con la sua Caption'],
      [k('new JButton("Premi qui")'), 'crea il bottone', 'TButton'],
      [k('new JLabel("...")'), 'crea la scritta', 'TLabel'],
      [k('bottone.addActionListener(e -> …);'), 'che cosa fare quando premi il bottone', 'il doppio clic sul bottone: Button1Click'],
      [k('scritta.setText("Hello World")'), 'cambia il testo della scritta', k("Label1.Caption := 'Hello World';")],
      [k('JPanel') + ' e ' + k('add(…)'), 'mette bottone e scritta nella finestra', 'trascinare i componenti sul Form'],
      [k('setSize(300, 120)'), 'larghezza e altezza della finestra', 'Width e Height'],
      [k('setDefaultCloseOperation(…)'), 'con la X il programma si chiude davvero', 'automatico'],
      [k('setVisible(true)'), 'mostra la finestra', 'automatico'],
      [k(';') + ' e ' + k('{ }'), 'fine istruzione; apri e chiudi un blocco', k(';') + ' e ' + k('begin … end')]]) +
    bn('import: জানালার অংশ আনে (uses)। class Main: ক্লাস, নাম = ফাইল Main.java। main: শুরু। JFrame = Form। JButton = TButton। JLabel = TLabel। addActionListener = Button1Click। setText = Label1.Caption :=। add = Form-এ রাখা। setSize = Width, Height। setVisible(true) = জানালা দেখায়। { } = begin … end।') +
    tab(['', 'Pascal', 'Java'], [
      ['scrivi una riga in console', k('writeln(…)'), k('System.out.println(…)')],
      ['le scritte', k("'Ciao'"), k('"Ciao"')],
      ['assegnare', k(':='), k('=') + ' oppure ' + k('setText(…)')],
      ['maiuscole e minuscole', 'uguali', '<b>diverse</b>: ' + k('jbutton') + ' è un errore']]) +
    p('<b>Prova del nove:</b> spiega al compagno in 30 secondi che cosa succede quando premi il bottone, e a che cosa corrisponde in Lazarus.', 'নিজে যাচাই: ৩০ সেকেন্ডে সহপাঠীকে বলো বোতাম চাপলে কী হয়, আর Lazarus-এ এর মতো কী।') });
S.push({ titolo: '9. Errori comuni: l\'errore è normale · সাধারণ ভুল: ভুল হওয়া স্বাভাবিক',
  testo: p('Sbagliare succede a tutti i programmatori, anche ai professionisti. Eclipse ti aiuta: sottolinea l\'errore in <b>rosso</b> e mette una <b>X rossa</b> a sinistra della riga. Passa il mouse sulla X per leggere il messaggio.', 'ভুল সব প্রোগ্রামারের হয়, পেশাদারদেরও। Eclipse ভুলে লাল দাগ দেয় আর লাইনের বামে লাল X দেয়। বার্তা পড়তে X-এর উপর মাউস রাখো।') +
    tab(['Che cosa vedi', 'Perché', 'Come si sistema'], [
      [k('The Eclipse executable launcher was unable to locate its companion shared library'), 'lo ZIP non è stato scompattato tutto: manca la cartella <b>plugins</b> (percorso troppo lungo o estrazione interrotta)', 'chiudi, cancella la cartella, rifai la scheda 3 con la cartella corta ' + k('C:\\Users\\Public\\ec') + ' e aspetta la fine'],
      ['rosso sotto ' + k('system') + ' o ' + k('jbutton'), 'Java distingue maiuscole e minuscole', 'copia di nuovo il codice con il bottone Copia'],
      [k('Syntax error, insert ";"'), 'manca il punto e virgola', 'aggiungi ' + k(';') + ' alla fine della riga'],
      [k('The public type … must be defined in its own file'), 'il nome dopo ' + k('class') + ' è diverso dal nome del file', 'dopo ' + k('public class') + ' scrivi ' + k('Main') + ', come il file Main.java'],
      ['rosso sulle virgolette', 'una virgoletta ' + k('"') + ' manca', 'il testo sta tra due ' + k('"')],
      ['il Run è <b>grigio</b> o chiede che cosa avviare', 'manca ' + k('main') + ', oppure il cursore non è nel file Main.java', 'clicca dentro Main.java nell\'editor e riprova'],
      ['premi Run e la finestrella non si vede', 'è dietro Eclipse', 'guarda nella barra in basso dello schermo e cliccala'],
      ['la Console non si vede', 'la scheda è nascosta', 'menu ' + en('Window', 'Finestra') + ' → ' + en('Show View', 'Mostra vista') + ' → ' + en('Console', 'Console')]]) +
    bn('companion shared library: ZIP পুরো আনজিপ হয়নি (plugins নেই): ফোল্ডার মুছে কার্ড ৩ আবার করো, ছোট ফোল্ডার C:\\Users\\Public\\ec দিয়ে। লাল system/jbutton: বড়-ছোট অক্ষর; কোড আবার কপি করো। insert ";": ; দাও। must be defined in its own file: class-এর পরে Main। Run ধূসর: Main.java-তে ক্লিক করো। জানালা দেখা যায় না: নিচের বারে দেখো। Console নেই: Window → Show View → Console।') +
    p('Per tornare indietro: ' + k('Ctrl') + ' + ' + k('Z') + ' annulla l\'ultima modifica.', 'পিছনে যেতে: Ctrl + Z শেষ পরিবর্তন বাতিল করে।') });
S.push({ titolo: '10. Consegna · জমা দেওয়া',
  testo: p('Su Classroom c\'è il compito di oggi <b>«Hello World in Lazarus e in Java»</b>, con il tuo Documento Google.', 'Classroom-এ আজকের কাজ «Hello World in Lazarus e in Java», তোমার Google ডকুমেন্টসহ।') +
    passo(1, 'Apri il Documento del compito su Classroom (nella finestra del browser).', 'Classroom-এ কাজের ডকুমেন্ট খোলো (ব্রাউজারে)।') +
    passo(2, 'Torna su Eclipse: fai partire il programma e premi il bottone, così si vede <b>Hello World</b> nella finestrella.', 'Eclipse-এ ফিরে যাও: প্রোগ্রাম চালাও, বোতাম চাপো, যাতে ছোট জানালায় Hello World দেখা যায়।') +
    passo(3, 'Premi ' + k('Win') + ' + ' + k('Shift') + ' + ' + k('S') + ' e trascina il mouse attorno a Eclipse <b>e</b> alla finestrella con Hello World.', 'Win + Shift + S চাপো, Eclipse আর Hello World লেখা ছোট জানালার চারপাশে মাউস টানো।') +
    passo(4, 'Nel Documento clicca sotto «4» (lo screenshot Java): se c\'è già uno screenshot Java, cliccalo e premi ' + k('Canc') + '. Poi premi ' + k('Ctrl') + ' + ' + k('V') + '.', 'ডকুমেন্টে «4»-এর নিচে ক্লিক করো: আগের Java স্ক্রিনশট থাকলে সেটিতে ক্লিক করে Canc। তারপর Ctrl + V।') +
    passo(5, 'In Classroom premi <b>Consegna</b> (il bottone blu in alto a destra nel compito), entro le <b>14:00</b>. Se l\'avevi già consegnato: prima <b>Annulla consegna</b>, poi incolla, poi di nuovo <b>Consegna</b>.', 'Classroom-এ Consegna চাপো (উপরে ডানদিকে নীল বোতাম), ১৪:০০-এর মধ্যে। আগে জমা দিয়ে থাকলে: আগে Annulla consegna, তারপর পেস্ট, তারপর আবার Consegna।') +
    FATTO('Hai consegnato il tuo programma Java con la finestra, fatto con Eclipse.', 'Eclipse দিয়ে বানানো জানালাসহ তোমার Java প্রোগ্রাম জমা দিয়েছো।') });
S.push({ titolo: '11. Per chi ha finito: saluta il tuo nome (facoltativo) · যারা শেষ করেছে: শুভেচ্ছা জানানো জানালা (ঐচ্ছিক)',
  testo: p('Lo stesso programma «Ciao» che la 1INF ha fatto oggi in Lazarus, ma in Java: una casella per il nome, un bottone, un messaggio. Qui la finestra non si disegna con il mouse: si scrive con il codice (si chiama <b>Swing</b>).', '1INF আজ Lazarus-এ যে «Ciao» প্রোগ্রাম বানিয়েছে, সেটাই Java-তে: নামের ঘর, বোতাম, বার্তা। এখানে জানালা মাউসে আঁকা হয় না: কোডে লেখা হয় (Swing)।') +
    passo(1, 'A sinistra clic destro su <b>src</b> → ' + en('New', 'Nuovo') + ' → ' + en('Class', 'Classe') + '.', 'বামে src-এ ডান ক্লিক → New → Class।') +
    passo(2, 'Casella ' + en('Package', 'Pacchetto') + ': ' + k('Ctrl') + ' + ' + k('A') + ' e ' + k('Canc') + ' (vuota). Casella ' + en('Name', 'Nome') + ':', 'Package: Ctrl + A আর Canc (খালি)। Name ঘরে:') + boxc('Finestra') +
    passo(3, 'Clicca ' + en('Finish', 'Fine') + '. Poi clicca <b>Copia</b> qui sotto.', 'Finish ক্লিক করো। তারপর নিচে Copia।') + boxc(SWING) +
    passo(4, 'Nell\'editor: ' + k('Ctrl') + ' + ' + k('A') + ', ' + k('Ctrl') + ' + ' + k('V') + ', ' + k('Ctrl') + ' + ' + k('S') + '. Poi il triangolo verde ' + en('Run', 'Esegui') + '.', 'editor-এ: Ctrl + A, Ctrl + V, Ctrl + S। তারপর সবুজ Run।') +
    passo(5, 'Scrivi il tuo nome nella casella e premi <b>Saluta</b>.', 'ঘরে তোমার নাম লেখো আর Saluta চাপো।') +
    tab(['Java (Swing)', 'Lazarus'], [
      [k('JFrame'), 'il Form (la finestra)'],
      [k('JTextField'), 'TEdit (la casella di testo)'],
      [k('JButton'), 'TButton (il bottone)'],
      [k('addActionListener(e -> …)'), 'il doppio clic sul bottone: Button1Click'],
      [k('casella.getText()'), k('Edit1.Text')],
      [k('JOptionPane.showMessageDialog(null, …)'), k('ShowMessage(…)')],
      [k('JPanel') + ' + ' + k('add(…)'), 'mettere i componenti sul Form'],
      [k('setVisible(true)'), 'mostra la finestra']]) +
    bn('JFrame = Form, JTextField = TEdit, JButton = TButton, addActionListener = Button1Click, getText() = Edit1.Text, showMessageDialog = ShowMessage, setVisible(true) = জানালা দেখায়।') +
    p('<b>Fallo tuo:</b> cambia il titolo «Il mio saluto» e la parola «Ciao» con quello che vuoi tu.', 'নিজের মতো করো: «Il mio saluto» শিরোনাম আর «Ciao» শব্দ বদলে দাও।') });
const B = { id: '3inf-eclipse-java-v1', classe: '3INF', titolo: 'Java con Eclipse portabile · পোর্টেবল Eclipse দিয়ে Java',
  sotto: '3INF · 28/10/2026 · dalla cartella al primo programma · consegna su Classroom',
  stato: 'stato/3inf-eclipse-java.json', risultati: 'risultati.html?b=3inf-eclipse-java', minuti: 10, anteprima: '868848605',
  aree: { nozioni: { nome: 'Eclipse e Java', peso: 100 } }, schede: S, schede_temi: {},
  strumenti: [{ t: 'Il mio cruscotto: voto, fatto e da fare', u: '../3inf-lazarus/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../3inf-monitor/', c: '#6e40c9' }],
  allenamento: [], crocette: [], aperte: [], recupero: [] };
fs.writeFileSync(DOCS + 'verifica/banche/3inf-eclipse-java.js', '// 3INF · Java con Eclipse portabile (28/10/2026), IT + bangla. Generato da classe-3/eclipse-java/_build/eclipse.js\nwindow.BANCA = ' + JSON.stringify(B, null, 1) + ';\n');
const st = DOCS + 'verifica/stato/3inf-eclipse-java.json';
if (!fs.existsSync(st)) fs.writeFileSync(st, JSON.stringify({ verifica: 'chiusa', recupero: 'chiuso', _nota: '28/10: si consegna lo screenshot nel Documento su Classroom' }, null, 1));
console.log('ok', S.length, 'schede');
