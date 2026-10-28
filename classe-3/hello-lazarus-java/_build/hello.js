// 28/10/2026 3INF, Laboratorio 12-14: Hello World in Lazarus (finestra con TEdit, TButton, TLabel, RadioGroup) e in Java nel browser (JavaFiddle).
// Lunedì 26/10 la classe ha visto la teoria «Object Pascal e Java a confronto»: oggi si passa alla pratica. Italiano + una riga in bangla (PC 14).
// Uso: node hello.js  →  docs/verifica/banche/3inf-hello-lazarus-java.js (+ stato). Impostazione presa da classe-1/lazarus-ciao/_build/lazarus.js.
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
const JAVA_URL = 'https://javafiddle.leaningtech.com', PIANO_B = 'https://www.onlinegdb.com/online_java_compiler';
const LAZ = "procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  Label1.Caption := 'Ciao ' + Edit1.Text + '!';\n  ShowMessage('Hello World, ' + Edit1.Text);\nend;";
const LAZ_RG = "procedure TForm1.Button1Click(Sender: TObject);\nvar\n  saluto: string;\nbegin\n  case RadioGroup1.ItemIndex of\n    1: saluto := 'Hello ';\n    2: saluto := 'Hola ';\n    3: saluto := 'Salam ';\n  else\n    saluto := 'Ciao ';\n  end;\n  Label1.Caption := saluto + Edit1.Text + '!';\nend;";
const LAZ_CB = "procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  Label1.Caption := ComboBox1.Text + ' ' + Edit1.Text + '!';\nend;";
const JAVA = 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello World");\n        System.out.println("Ciao, sono Ahmed");\n    }\n}';
const JAVA_GUI = 'import javax.swing.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        JFrame finestra = new JFrame("Il mio saluto");\n        JButton bottone = new JButton("Saluta");\n        bottone.addActionListener(e ->\n            JOptionPane.showMessageDialog(null, "Hello World"));\n        finestra.add(bottone);\n        finestra.setSize(300, 200);\n        finestra.setVisible(true);\n    }\n}';
const SCHEMA = "Documenti\\\n  Lazarus\\            <- TUTTI i miei progetti\n    Saluto\\           <- UN progetto = UNA cartella\n      Saluto.lpi  Saluto.lpr  unit1.pas  unit1.lfm   <- i 4 da tenere";
const S = [];
S.push({ titolo: '1. Oggi: Hello World in due linguaggi · আজ: দুই ভাষায় Hello World',
  testo: '<div style="background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 6px"><b>Questa pagina cambia durante la lezione: ogni tanto premi F5 per vedere la versione nuova.</b></p>' + bn('<b>এই পাতাটি ক্লাসের সময় বদলায়: মাঝে মাঝে F5 চাপো, নতুন সংস্করণ দেখতে।</b>') + '</div>' +
    '<div style="background:#fdf2e6;border:2px solid #b45309;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 8px"><a href="../3inf-lazarus/" target="_blank" rel="noopener" style="display:block;text-align:center;background:#b45309;color:#fff;font-weight:bold;font-size:18px;padding:14px 12px;border-radius:10px;text-decoration:none">Il mio cruscotto: voto, che cosa ho fatto e che cosa manca</a></p>' + p('Guardalo ogni tanto: ti dice a che punto sei e che cosa ti manca per consegnare.', 'মাঝে মাঝে দেখো: তুমি কোথায় আছো আর জমা দিতে কী বাকি আছে, তা বলে।') + '</div>' +
    p('Lunedì avete visto la teoria: <b>Object Pascal</b> (Lazarus) e <b>Java</b> a confronto. Oggi li <b>provate davvero</b>, tutti e due.', 'সোমবার তোমরা তত্ত্ব দেখেছো: Object Pascal (Lazarus) আর Java তুলনা। আজ দুটোই সত্যি সত্যি চালিয়ে দেখবে।') +
    p('<b>Hello World</b> («Ciao mondo») è il primo programma di ogni programmatore, in ogni linguaggio: serve a controllare che tutto funzioni.', 'Hello World হলো প্রত্যেক প্রোগ্রামারের প্রথম প্রোগ্রাম, যেকোনো ভাষায়: সব ঠিক চলছে কিনা দেখার জন্য।') +
    tab(['Parte', 'Che cosa fai', 'Schede'], [
      ['A. Lazarus', 'un progetto pulito e una finestra che saluta', '2, 3, 4, 5, 6'],
      ['B. Java', 'Hello World in Java, nel browser, senza installare niente', '7, 8'],
      ['C. Consegna', 'il Documento su Classroom, entro le 14:00', '9']]) +
    bn('A: Lazarus-এ একটি জানালা যা শুভেচ্ছা জানায়। B: ব্রাউজারে Java, কিছু ইনস্টল না করে। C: Classroom-এ ডকুমেন্ট জমা, ১৪:০০-এর মধ্যে।') +
    p('Per aprire Lazarus: doppio clic sull\'icona di Lazarus. Poi vai alla scheda 2.', 'Lazarus খুলতে: Lazarus আইকনে দুবার ক্লিক করো। তারপর ২ নম্বর কার্ডে যাও।') });
S.push({ titolo: '2. Partenza pulita: progetto nuovo in Documenti\\Lazarus\\Saluto · পরিষ্কার শুরু: নতুন প্রজেক্ট',
  testo: '<p><a href="../1inf-howto-progetto/" target="_blank" rel="noopener" style="display:block;text-align:center;background:#0b6e99;color:#fff;font-weight:bold;font-size:18px;padding:14px 12px;border-radius:10px;text-decoration:none">Come si crea un progetto nuovo (la guida con le figure)</a></p>' +
    p('La regola è la stessa per tutti: nella cartella <b>Documenti → Lazarus</b> stanno tutti i tuoi progetti, e <b>ogni progetto ha la sua cartella</b>. Oggi il progetto si chiama ' + k('Saluto') + '.', 'নিয়ম সবার জন্য এক: Documenti → Lazarus ফোল্ডারে তোমার সব প্রজেক্ট থাকে, আর প্রতিটি প্রজেক্টের নিজের ফোল্ডার। আজকের প্রজেক্টের নাম Saluto।') +
    box(esc(SCHEMA)) +
    passo(1, 'In alto a sinistra in Lazarus clicca il menu <b>File</b>, poi <b>Chiudi tutto</b>. Se chiede di salvare un progetto vecchio, clicca <b>No</b>.', 'উপরে বাঁদিকে File মেনুতে ক্লিক করো, তারপর «Chiudi tutto»। পুরনো প্রজেক্ট সেভ করতে বললে «No» চাপো।') +
    passo(2, 'In alto clicca il menu <b>Progetto</b>, poi <b>Nuovo progetto…</b>.', 'উপরে Progetto মেনুতে ক্লিক করো, তারপর «Nuovo progetto…»।') +
    passo(3, 'Nell\'elenco a sinistra clicca <b>Applicazione</b>, poi in basso <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.', 'বাঁদিকের তালিকায় «Applicazione» ক্লিক করো, তারপর নিচে OK। মাঝখানে খালি Form1 জানালা আসবে।') +
    passo(4, 'Subito si salva: menu <b>Progetto</b> → <b>Salva progetto con nome…</b>.', 'এখনই সেভ করো: Progetto মেনু → «Salva progetto con nome…»।') +
    passo(5, 'Nel pannello a sinistra clicca <b>Documenti</b>, poi fai doppio clic sulla cartella <b>Lazarus</b>.', 'বাঁদিকের প্যানেলে Documenti ক্লিক করো, তারপর Lazarus ফোল্ডারে দুবার ক্লিক করো।') +
    passo(6, 'In alto clicca <b>Nuova cartella</b>, scrivi questo nome e premi ' + k('Invio') + ':', 'উপরে «Nuova cartella» ক্লিক করো, এই নামটি লেখো আর Invio চাপো:') + box('Saluto') +
    passo(7, 'Fai doppio clic sulla cartella ' + k('Saluto') + '. In alto ora c\'è scritto <b>Documenti › Lazarus › Saluto</b>.', 'Saluto ফোল্ডারে দুবার ক্লিক করো। উপরে এখন লেখা থাকবে Documenti › Lazarus › Saluto।') +
    passo(8, 'Nella casella <b>Nome file</b> scrivi questo nome, poi clicca <b>Salva</b>:', 'Nome file ঘরে এই নামটি লেখো, তারপর Salva ক্লিক করো:') + box('Saluto.lpi') +
    passo(9, 'Lazarus chiede il nome della unit (il file del codice): lascia ' + k('unit1.pas') + ' e clicca <b>Salva</b>.', 'Lazarus ইউনিটের (কোডের ফাইল) নাম চাইবে: unit1.pas রেখে দাও আর Salva চাপো।') +
    FATTO('In alto, nella barra del titolo di Lazarus, c\'è scritto ' + k('Saluto') + ' e il percorso che finisce con ' + k('Documents\\Lazarus\\Saluto') + '.', 'Lazarus-এর উপরের শিরোনামে Saluto আর Documents\\Lazarus\\Saluto লেখা আছে।') });
S.push({ titolo: '3. La finestra: TEdit, TButton, TLabel · জানালা: TEdit, TButton, TLabel',
  testo: p('Tre pezzi dalla palette, linguetta <b>Standard</b>. Li conoscete già: oggi li usate insieme.', 'প্যালেটের Standard ট্যাব থেকে তিনটি অংশ। তোমরা এগুলো আগেই চেনো: আজ একসাথে ব্যবহার করবে।') +
    tab(['Pezzo', 'A che cosa serve', 'Proprietà che conta'], [
      ['<b>TEdit</b>', 'chi usa il programma <b>scrive</b> il nome', k('Text')],
      ['<b>TButton</b>', 'si <b>preme</b> per far succedere una cosa', k('Caption')],
      ['<b>TLabel</b>', 'un testo da <b>leggere</b>: qui compare il saluto', k('Caption')]]) +
    bn('TEdit: নাম লেখার ঘর। TButton: চাপার বোতাম। TLabel: পড়ার লেখা, এখানে শুভেচ্ছা দেখা যাবে।') +
    passo(1, 'Nella palette clicca <b>TEdit</b>, poi clicca nella Form1 in alto a sinistra.', 'প্যালেটে TEdit ক্লিক করো, তারপর Form1-এর উপরে বাঁদিকে ক্লিক করো।') +
    passo(2, 'Nell\'Ispettore oggetti, a sinistra, cancella il testo della proprietà ' + k('Text') + ': la casella resta vuota.', 'বাঁদিকের Ispettore oggetti-তে Text-এর লেখা মুছে দাও: ঘরটি খালি থাকবে।') +
    passo(3, 'Nella palette clicca <b>TButton</b>, poi clicca nella Form1 sotto la casella.', 'প্যালেটে TButton ক্লিক করো, তারপর ঘরের নিচে Form1-এ ক্লিক করো।') +
    passo(4, 'Nell\'Ispettore oggetti cambia ' + k('Caption') + ' del bottone in:', 'Ispettore oggetti-তে বোতামের Caption বদলে লেখো:') + box('Saluta') +
    passo(5, 'Nella palette clicca <b>TLabel</b> (la «A»), poi clicca nella Form1 sotto il bottone.', 'প্যালেটে TLabel («A») ক্লিক করো, তারপর বোতামের নিচে Form1-এ ক্লিক করো।') +
    passo(6, 'Nell\'Ispettore oggetti cambia ' + k('Caption') + ' della label in:', 'Ispettore oggetti-তে লেবেলের Caption বদলে লেখো:') + box('...') +
    FATTO('La finestra ha una casella, il bottone «Saluta» e la label «...».', 'জানালায় একটি ঘর, «Saluta» বোতাম আর «...» লেবেল আছে।') });
S.push({ titolo: '4. Il codice: il saluto nella Label e nel ShowMessage · কোড: লেবেলে আর ShowMessage-এ শুভেচ্ছা',
  testo: passo(1, 'Fai <b>doppio clic sul bottone</b> «Saluta». Si apre il codice, dentro la procedura ' + k('Button1Click') + '.', '«Saluta» বোতামে দুবার ক্লিক করো। কোড খুলবে, Button1Click প্রসিডিউরের ভিতরে।') +
    passo(2, 'Tra ' + k('begin') + ' e ' + k('end;') + ' scrivi le due righe. La procedura completa è questa:', 'begin আর end;-এর মাঝে দুটি লাইন লেখো। পুরো প্রসিডিউরটি এই রকম:') + box(esc(LAZ)) +
    tab(['Riga', 'Che cosa fa'], [
      [k("Label1.Caption := 'Ciao ' + Edit1.Text + '!';"), 'scrive nella <b>Label</b> «Ciao», il nome della casella e «!». Il saluto <b>resta</b> nella finestra'],
      [k("ShowMessage('Hello World, ' + Edit1.Text);"), 'apre una <b>finestrella</b> con «Hello World» e il nome, e il bottone OK'],
      [k(':='), 'assegna: «metti dentro». In Pascal si scrive con i due punti'],
      [k('+'), 'attacca due scritte una dopo l\'altra'],
      [k("'Ciao '"), 'una scritta fissa, tra apici singoli. Lo spazio dopo Ciao evita «CiaoAhmed»']]) +
    bn('প্রথম লাইন: লেবেলে «Ciao» + নাম + «!» লেখে, জানালায় থেকে যায়। দ্বিতীয় লাইন: «Hello World» আর নাম সহ একটি ছোট জানালা খোলে। := মানে «ভিতরে রাখো»। + দুটি লেখা জোড়া দেয়।') });
S.push({ titolo: '5. Salva e fai partire · সেভ করো আর চালাও',
  testo: passo(1, 'Premi ' + k('Ctrl') + ' + ' + k('S') + ': Lazarus salva tutto nella cartella Saluto.', 'Ctrl + S চাপো: Lazarus সব Saluto ফোল্ডারে সেভ করে।') +
    passo(2, 'Premi ' + k('F9') + ' (o la freccia verde ▶ in alto). Si apre la TUA finestra.', 'F9 চাপো (বা উপরের সবুজ ▶)। তোমার জানালা খুলবে।') +
    passo(3, 'Scrivi il tuo nome nella casella e clicca <b>Saluta</b>. Compare la finestrella «Hello World» con il tuo nome.', 'ঘরে তোমার নাম লেখো আর Saluta চাপো। তোমার নাম সহ «Hello World» ছোট জানালা আসবে।') +
    passo(4, 'Clicca <b>OK</b>: nella Label c\'è scritto «Ciao» e il tuo nome.', 'OK চাপো: লেবেলে «Ciao» আর তোমার নাম লেখা আছে।') +
    passo(5, 'Prima di chiudere fai lo <b>screenshot</b> per la consegna: ' + k('Win') + ' + ' + k('Shift') + ' + ' + k('S') + ', trascina un rettangolo intorno alla finestra. L\'immagine resta in memoria: la incolli nel Documento (scheda 9).', 'বন্ধ করার আগে স্ক্রিনশট নাও: Win + Shift + S, জানালার চারপাশে আয়তক্ষেত্র টানো। ছবিটি ডকুমেন্টে পেস্ট করবে (কার্ড ৯)।') +
    p('<b>Errore? È normale, succede a tutti i programmatori.</b> Guarda la finestra Messaggi in basso: dice la riga. I più comuni: manca il ' + k(';') + '; hai scritto ' + k('=') + ' invece di ' + k(':=') + '; manca un apice ' + k("'") + '; la riga è fuori da begin … end.', 'ভুল? স্বাভাবিক, সব প্রোগ্রামারেরই হয়। নিচের Messaggi জানালা লাইনটি বলে। সাধারণ ভুল: ; নেই, := এর বদলে =, ' + "'" + ' নেই, লাইনটি begin … end-এর বাইরে।') +
    FATTO('Il tuo Hello World in Lazarus funziona.', 'Lazarus-এ তোমার Hello World চলছে।') +
    p('<b>Ripasso veloce dei file</b> (li avete già visti): nella cartella Saluto, dopo F9, ci sono tanti file. Si tengono, si consegnano e vanno su GitHub solo questi 4:', 'ফাইলের ছোট পুনরাবৃত্তি: F9-এর পরে Saluto ফোল্ডারে অনেক ফাইল থাকে। শুধু এই ৪টি রাখতে, জমা দিতে আর GitHub-এ দিতে হয়:') +
    tab(['File', 'Che cos\'è', 'Tenere?'], [
      [k('Saluto.lpi'), 'le informazioni e le opzioni del progetto (si riapre con doppio clic)', '<b>SÌ</b>'],
      [k('Saluto.lpr'), 'il programma principale, fa partire tutto', '<b>SÌ</b>'],
      [k('unit1.pas'), 'il TUO codice (Button1Click)', '<b>SÌ</b>'],
      [k('unit1.lfm'), 'com\'è fatta la finestra: pezzi, posizioni, Caption', '<b>SÌ</b>'],
      [k('.lps') + ' ' + k('.res') + ' ' + k('.ico') + ' ' + k('.exe'), 'sessione, risorse, icona, programma finito', 'no: Lazarus li rifà'],
      [k('lib\\') + ' (' + k('.o') + ' ' + k('.ppu') + ' ' + k('.compiled') + ' ' + k('.or') + ') e ' + k('backup\\'), 'file di lavoro del compilatore e copie di sicurezza', 'no: si rifanno']]) +
    bn('রাখতে হবে: .lpi .lpr .pas .lfm। বাকি সব (.lps .res .ico .exe, lib\\, backup\\) Lazarus নিজেই আবার বানায়।') });
S.push({ titolo: '6. Fallo tuo: il saluto in tante lingue (RadioGroup o ComboBox) · নিজের মতো করো: অনেক ভাষায় শুভেচ্ছা',
  testo: p('Chi usa il programma <b>sceglie la lingua</b> del saluto. Scegli <b>uno</b> dei due modi.', 'ব্যবহারকারী শুভেচ্ছার ভাষা বেছে নেয়। দুটি উপায়ের একটি বেছে নাও।') +
    p('<b>Modo 1: RadioGroup</b> (un gruppo di pallini: se ne sceglie uno solo).', 'উপায় ১: RadioGroup (কয়েকটি গোল বোতাম: শুধু একটি বেছে নেওয়া যায়)।') +
    passo(1, 'Nella palette, linguetta <b>Standard</b>, clicca <b>TRadioGroup</b>, poi clicca nella Form1 a destra.', 'প্যালেটের Standard ট্যাবে TRadioGroup ক্লিক করো, তারপর Form1-এর ডানদিকে ক্লিক করো।') +
    passo(2, 'Nell\'Ispettore oggetti cambia ' + k('Caption') + ' in:', 'Ispettore oggetti-তে Caption বদলে লেখো:') + box('Lingua') +
    passo(3, 'Clicca la proprietà ' + k('Items') + ', poi il bottoncino <b>…</b> a destra. Si apre una finestra: scrivi una lingua per riga, poi <b>OK</b>:', 'Items-এ ক্লিক করো, তারপর ডানদিকে ছোট … বোতাম। একটি জানালা খুলবে: প্রতি লাইনে একটি ভাষা লেখো, তারপর OK:') + box('Italiano\nEnglish\nEspañol\nالعربية') +
    passo(4, 'Cambia ' + k('ItemIndex') + ' in ' + k('0') + ': il primo pallino (Italiano) è già scelto.', 'ItemIndex বদলে 0 করো: প্রথম গোল বোতাম (Italiano) আগেই বাছা থাকবে।') +
    passo(5, 'Doppio clic sul bottone Saluta e cambia la procedura così:', 'Saluta বোতামে দুবার ক্লিক করো আর প্রসিডিউরটি এভাবে বদলাও:') + box(esc(LAZ_RG)) +
    p(k('ItemIndex') + ' è il numero del pallino scelto: si conta da <b>0</b>. ' + k('case … of') + ' sceglie la riga giusta, ' + k('else') + ' vale per tutti gli altri casi (qui il numero 0, Italiano).', 'ItemIndex হলো বাছা গোল বোতামের নম্বর: ০ থেকে গোনা হয়। case … of ঠিক লাইনটি বাছে, else বাকি সব ক্ষেত্রে (এখানে ০, Italiano)।') +
    p('<b>Modo 2: ComboBox</b> (una tendina con l\'elenco).', 'উপায় ২: ComboBox (একটি ড্রপ-ডাউন তালিকা)।') +
    passo(1, 'Nella palette clicca <b>TComboBox</b>, poi clicca nella Form1. Nella proprietà ' + k('Items') + ' (bottoncino …) scrivi un saluto per riga:', 'প্যালেটে TComboBox ক্লিক করো, তারপর Form1-এ। Items-এ (… বোতাম) প্রতি লাইনে একটি শুভেচ্ছা লেখো:') + box('Ciao\nHello\nHola\nSalam') +
    passo(2, 'Cambia ' + k('ItemIndex') + ' in ' + k('0') + ', poi doppio clic sul bottone Saluta e scrivi:', 'ItemIndex বদলে 0 করো, তারপর Saluta বোতামে দুবার ক্লিক করে লেখো:') + box(esc(LAZ_CB)) +
    p('Poi ' + k('F9') + ', scegli una lingua e premi Saluta. Rifai lo screenshot: nel Documento può andare questa versione.', 'তারপর F9, একটি ভাষা বেছে Saluta চাপো। আবার স্ক্রিনশট নাও: ডকুমেন্টে এই সংস্করণটি দিতে পারো।') +
    FATTO('Il tuo programma saluta in più lingue.', 'তোমার প্রোগ্রাম অনেক ভাষায় শুভেচ্ছা জানায়।') });
S.push({ titolo: '7. Java nel browser, senza installare niente · ব্রাউজারে Java, কিছু ইনস্টল না করে',
  testo: p('Java di solito va <b>installato</b>. Oggi usiamo <b>JavaFiddle</b>: un sito che compila ed esegue Java <b>dentro il browser</b>. Non si installa niente e non serve un account.', 'সাধারণত Java ইনস্টল করতে হয়। আজ আমরা JavaFiddle ব্যবহার করবো: একটি সাইট যা ব্রাউজারের ভিতরেই Java চালায়। কিছু ইনস্টল করতে হয় না।') +
    passo(1, 'Premi ' + k('Ctrl') + ' + ' + k('T') + ': si apre una scheda nuova del browser.', 'Ctrl + T চাপো: ব্রাউজারে নতুন ট্যাব খুলবে।') +
    passo(2, 'Scrivi questo indirizzo in alto e premi ' + k('Invio') + ':', 'উপরে এই ঠিকানাটি লেখো আর Invio চাপো (ঠিকানা, ঠিক এভাবেই লেখো):') + box(JAVA_URL) +
    passo(3, 'Aspetta: la prima volta il sito carica Java nel browser e ci mette fino a un minuto. A sinistra c\'è il riquadro del codice.', 'অপেক্ষা করো: প্রথমবার সাইটটি ব্রাউজারে Java লোড করে, এক মিনিট পর্যন্ত লাগে। বাঁদিকে কোডের ঘর।') +
    passo(4, 'Clicca dentro il riquadro del codice, premi ' + k('Ctrl') + ' + ' + k('A') + ' e poi ' + k('Canc') + ': il riquadro è vuoto.', 'কোডের ঘরে ক্লিক করো, Ctrl + A তারপর Canc চাপো: ঘরটি খালি।') +
    passo(5, 'Scrivi questo programma (al posto di Ahmed metti il tuo nome):', 'এই প্রোগ্রামটি লেখো (Ahmed-এর জায়গায় তোমার নাম):') + box(esc(JAVA)) +
    passo(6, 'Clicca il bottone <b>Run</b> (in alto, «esegui»). Sotto o a destra compare la scritta <b>Hello World</b> e il tuo saluto.', 'Run বোতাম চাপো (উপরে, «চালাও»)। নিচে বা ডানদিকে Hello World আর তোমার শুভেচ্ছা দেখা যাবে।') +
    passo(7, 'Fai lo <b>screenshot</b> con il codice e la scritta: ' + k('Win') + ' + ' + k('Shift') + ' + ' + k('S') + '.', 'কোড আর লেখা সহ স্ক্রিনশট নাও: Win + Shift + S।') +
    FATTO('Hai scritto ed eseguito il tuo primo programma Java.', 'তুমি তোমার প্রথম Java প্রোগ্রাম লিখে চালিয়েছো।') +
    '<div style="background:#eef6ff;border:2px solid #1f6feb;border-radius:10px;padding:8px 12px;margin:10px 0">' +
    p('<b>Piano B.</b> Il sito non si apre o resta bloccato più di 2 minuti? Usa questo, funziona allo stesso modo (il bottone verde <b>Run</b> è in alto; la scritta compare in basso):', 'পরিকল্পনা B: সাইট না খুললে বা ২ মিনিটের বেশি আটকে থাকলে এটা ব্যবহার করো, একইভাবে চলে (উপরে সবুজ Run বোতাম; লেখা নিচে আসে):') + box(PIANO_B) +
    p('Il nome dopo ' + k('public class') + ' resta ' + k('Main') + ': i due siti cercano una classe con questo nome.', 'public class-এর পরের নাম Main থাকবে: দুটি সাইটই এই নামের ক্লাস খোঁজে।') + '</div>' +
    p('<b>Per i più veloci: una finestra con un bottone in Java.</b> JavaFiddle sa aprire anche le finestre (Swing). Prova questo programma: confrontalo con le righe che hai scritto in Lazarus.', 'দ্রুতদের জন্য: Java-তে বোতাম সহ একটি জানালা। JavaFiddle জানালাও (Swing) খুলতে পারে। এই প্রোগ্রামটি চেষ্টা করো, Lazarus-এর লাইনের সাথে তুলনা করো।') + box(esc(JAVA_GUI)) });
S.push({ titolo: '8. Java riga per riga, e il confronto con Pascal · Java লাইন ধরে ধরে, Pascal-এর সাথে তুলনা',
  testo: tab(['Riga Java', 'Che cosa vuol dire'], [
      [k('public class Main {'), 'in Java tutto sta dentro una <b>classe</b>. Si chiama ' + k('Main') + '; la graffa ' + k('{') + ' apre il blocco'],
      [k('public static void main(String[] args) {'), 'il <b>metodo main</b>: il punto da cui parte il programma. Ogni programma Java ne ha uno'],
      [k('System.out.println("Hello World");'), 'scrive una riga sullo schermo (la <b>console</b>) e va a capo. Il testo sta tra virgolette doppie'],
      [k('}'), 'chiude il blocco: la prima ' + k('}') + ' chiude main, l\'ultima chiude la classe']]) +
    bn('public class Main: Java-তে সব একটি ক্লাসের ভিতরে থাকে। main: প্রোগ্রাম এখান থেকে শুরু হয়। System.out.println: স্ক্রিনে একটি লাইন লেখে। } ব্লক বন্ধ করে।') +
    p('<b>Lo stesso programma in Pascal</b> (da console, come lunedì):', 'একই প্রোগ্রাম Pascal-এ (কনসোল, সোমবারের মতো):') + box(esc("program Saluto;\nbegin\n  writeln('Hello World');\n  writeln('Ciao, sono Ahmed');\nend.")) +
    tab(['', 'Pascal (Lazarus)', 'Java'], [
      ['inizio del programma', k('program Saluto;') + ' … ' + k('begin'), k('public class Main {') + ' + ' + k('main')],
      ['fine', k('end.') + ' (con il punto)', k('}') + ' e ' + k('}')],
      ['scrivere una riga', k('writeln(…)'), k('System.out.println(…)')],
      ['finestrella con un messaggio', k('ShowMessage(…)'), k('JOptionPane.showMessageDialog(null, …)')],
      ['le scritte', 'apici singoli ' + k("'Ciao'"), 'virgolette doppie ' + k('"Ciao"')],
      ['assegnare', k(':='), k('=')],
      ['maiuscole e minuscole', 'uguali: ' + k('WriteLn') + ' = ' + k('writeln'), 'diverse: ' + k('system.out') + ' è un errore'],
      ['la finestra', 'disegnata con il mouse', 'scritta con il codice (Swing)']]) +
    bn('Pascal: program … begin … end.,  writeln, \'একক উদ্ধৃতি\', :=, বড়-ছোট হাতের অক্ষর একই। Java: class + main, { }, System.out.println, "দ্বৈত উদ্ধৃতি", =, বড়-ছোট হাতের অক্ষর আলাদা।') +
    p('<b>Prova del nove:</b> spiega al compagno in 30 secondi che cosa fa ' + k('System.out.println') + ' e a che cosa corrisponde in Pascal.', 'নিজে যাচাই করো: ৩০ সেকেন্ডে সহপাঠীকে বলো System.out.println কী করে আর Pascal-এ এর মতো কী।') });
S.push({ titolo: '9. Consegna · জমা দেওয়া',
  testo: p('Su Classroom c\'è il compito <b>«Hello World in Lazarus e in Java»</b>. Dentro c\'è un <b>Documento Google</b> già pronto, solo tuo. Aprilo e metti 5 cose:', 'Classroom-এ «Hello World in Lazarus e in Java» কাজটি আছে। ভিতরে তোমার নিজের একটি Google ডকুমেন্ট আছে। খুলে ৫টি জিনিস দাও:') +
    passo(1, '<b>Il codice Lazarus.</b> In Lazarus seleziona la procedura, da ' + k('procedure TForm1.Button1Click') + ' fino a ' + k('end;') + ', premi ' + k('Ctrl') + ' + ' + k('C') + '; nel Documento clicca sotto «1» e premi ' + k('Ctrl') + ' + ' + k('V') + '.', 'Lazarus কোড: procedure থেকে end; পর্যন্ত বেছে Ctrl + C, ডকুমেন্টে «1»-এর নিচে Ctrl + V।') +
    passo(2, '<b>Lo screenshot Lazarus.</b> Programma acceso con il saluto: ' + k('Win') + ' + ' + k('Shift') + ' + ' + k('S') + ', poi nel Documento sotto «2» ' + k('Ctrl') + ' + ' + k('V') + '.', 'Lazarus স্ক্রিনশট: চালু প্রোগ্রাম, Win + Shift + S, ডকুমেন্টে «2»-এর নিচে Ctrl + V।') +
    passo(3, '<b>Il codice Java.</b> In JavaFiddle ' + k('Ctrl') + ' + ' + k('A') + ' e ' + k('Ctrl') + ' + ' + k('C') + ' nel riquadro del codice; nel Documento sotto «3» ' + k('Ctrl') + ' + ' + k('V') + '.', 'Java কোড: JavaFiddle-এ কোডের ঘরে Ctrl + A আর Ctrl + C, ডকুমেন্টে «3»-এর নিচে Ctrl + V।') +
    passo(4, '<b>Lo screenshot Java</b> con la scritta Hello World: sotto «4».', 'Hello World লেখা সহ Java স্ক্রিনশট: «4»-এর নিচে।') +
    passo(5, '<b>Con parole tue.</b> Sotto «5» scrivi una o due frasi: che differenza c\'è tra ' + k('ShowMessage') + ' in Lazarus e ' + k('System.out.println') + ' in Java? Puoi scrivere anche nella tua lingua.', 'নিজের ভাষায়: «5»-এর নিচে এক-দুই বাক্য লেখো: Lazarus-এর ShowMessage আর Java-র System.out.println-এর পার্থক্য কী? নিজের ভাষাতেও লিখতে পারো।') +
    passo(6, 'In Classroom premi <b>Consegna</b> (il bottone blu in alto a destra nel compito), entro le <b>14:00</b>.', 'Classroom-এ «Consegna» চাপো (কাজের উপরে ডানদিকে নীল বোতাম), ১৪:০০-এর মধ্যে।') +
    p('Il tuo cruscotto (scheda 1) ti dice che cosa manca nel Documento. Se manca qualcosa: «Annulla consegna», completa, «Consegna».', 'তোমার ড্যাশবোর্ড (কার্ড ১) বলে ডকুমেন্টে কী বাকি। কিছু বাকি থাকলে: «Annulla consegna», সম্পূর্ণ করো, আবার «Consegna»।') });
const B = { id: '3inf-hello-lazarus-java-v1', classe: '3INF', titolo: 'Hello World in Lazarus e in Java · Lazarus আর Java-তে Hello World',
  sotto: '3INF · 28/10/2026 · TEdit, TButton, TLabel, RadioGroup · Java nel browser · consegna su Classroom',
  stato: 'stato/3inf-hello-lazarus-java.json', risultati: 'risultati.html?b=3inf-hello-lazarus-java', minuti: 10, anteprima: '868848605',
  aree: { nozioni: { nome: 'Lazarus e Java', peso: 100 } }, schede: S, schede_temi: {},
  strumenti: [{ t: 'Il mio cruscotto: voto, fatto e da fare', u: '../3inf-lazarus/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../3inf-monitor/', c: '#6e40c9' }],
  allenamento: [], crocette: [], aperte: [], recupero: [] };
fs.writeFileSync(DOCS + 'verifica/banche/3inf-hello-lazarus-java.js', '// 3INF · Hello World in Lazarus e in Java (28/10/2026), IT + bangla. Generato da classe-3/hello-lazarus-java/_build/hello.js\nwindow.BANCA = ' + JSON.stringify(B, null, 1) + ';\n');
const st = DOCS + 'verifica/stato/3inf-hello-lazarus-java.json';
if (!fs.existsSync(st)) fs.writeFileSync(st, JSON.stringify({ verifica: 'chiusa', recupero: 'chiuso', _nota: '28/10: si consegna il Documento su Classroom' }, null, 1));
console.log('ok', S.length, 'schede');
