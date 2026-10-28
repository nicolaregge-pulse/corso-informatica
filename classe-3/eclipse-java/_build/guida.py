# 28/10/2026 3INF: guida passo passo «Java con Eclipse: la finestra con il bottone Hello World»,
# fatta con gli screenshot reali del docente. Una sola fonte -> tre uscite:
#   docs/3inf-eclipse-guida/index.html (pagina per i ragazzi, spunte «Fatto» in localStorage)
#   classe-3/eclipse-java/20261028_Classe-3_v1.0_Eclipse-Hello-World.md (+ .html per il PDF)
# Uso: python3 classe-3/eclipse-java/_build/guida.py && NODE_PATH=$(npm root -g) node classe-3/eclipse-java/_build/pdf.js
# Codice Java verificato con javac (compila senza avvisi).
import html, os, re

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.abspath(os.path.join(QUI, '../../..'))
OUT_DIR = os.path.abspath(os.path.join(QUI, '..'))
PAGINA = os.path.join(RADICE, 'docs/3inf-eclipse-guida/index.html')
VERSIONE = '1.1'
NOME = f'20261028_Classe-3_v{VERSIONE}_Eclipse-Hello-World'
TITOLO = 'Java con Eclipse: la finestra con il bottone Hello World'
TITOLO_BN = 'Eclipse দিয়ে Java: Hello World বোতামসহ জানালা'
ZIP = 'eclipse-java-2026-09-R-win32-x86_64.zip'

CODICE = '''import javax.swing.*;
import java.awt.FlowLayout;

public class Main {

    public static void main(String[] args) {
        JFrame finestra = new JFrame("Il mio primo programma");
        JButton bottone = new JButton("Premi");

        bottone.addActionListener(e -> JOptionPane.showMessageDialog(finestra, "Hello World"));

        finestra.setLayout(new FlowLayout());
        finestra.add(bottone);
        finestra.setSize(300, 150);
        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        finestra.setVisible(true);
    }

}'''

# Mini-marcatura nei testi: **grassetto**, `codice`. Ogni frase: (italiano, bangla).
# Elementi di un passo: ('p', it, bn) · ('img', file, didascalia_it, didascalia_bn) · ('copia', testo)
#                      ('nota'|'stop'|'fatto', it, bn)
PARTI = [
 dict(t='Prima di cominciare', bn='শুরু করার আগে', intro=[
  ('p', 'Oggi fai il tuo primo programma Java con la finestra, in **Eclipse**: un programma vero da programmatori.', 'আজ তুমি Eclipse-এ জানালাসহ তোমার প্রথম Java প্রোগ্রাম বানাবে: প্রোগ্রামারদের আসল প্রোগ্রাম।'),
  ('p', 'La meta: una finestra con il bottone **Premi**. Lo premi e si apre una finestrella con scritto **Hello World** e il bottone **OK**. È come `ShowMessage` di Lazarus.', 'লক্ষ্য: Premi বোতামসহ একটি জানালা। চাপলে ছোট জানালা খোলে, তাতে Hello World লেখা আর OK বোতাম। Lazarus-এর ShowMessage-এর মতো।'),
  ('p', 'Eclipse è **in inglese**: qui trovi il nome inglese esatto di ogni bottone e, tra parentesi, la traduzione italiana.', 'Eclipse ইংরেজিতে: এখানে প্রতিটি বোতামের সঠিক ইংরেজি নাম আছে, আর বন্ধনীতে ইতালীয় অনুবাদ।'),
  ('p', 'Ogni passo è **una sola azione**. Quando l\'hai fatta, metti la spunta **Fatto**.', 'প্রতিটি ধাপে একটি মাত্র কাজ। করা হলে Fatto (হয়ে গেছে)-তে টিক দাও।'),
 ], passi=[]),
 dict(t='Scompattare Eclipse', bn='Eclipse আনজিপ করা', intro=[
  ('p', f'Il prof ti dà il file **{ZIP}** (360 MB). È uno ZIP, cioè un pacchetto compresso: Eclipse non si installa, si scompatta e basta.', f'প্রফেসর তোমাকে {ZIP} ফাইল (৩৬০ MB) দেবেন। এটি ZIP, মানে সংকুচিত প্যাকেট: Eclipse ইনস্টল করতে হয় না, শুধু আনজিপ করতে হয়।'),
 ], passi=[
  dict(t='Estrai tutto', bn='Estrai tutto (সব বের করো)', el=[
   ('p', 'Fai clic **destro** sul file ZIP e scegli **Estrai tutto…**', 'ZIP ফাইলে ডান ক্লিক করো, Estrai tutto… বেছে নাও।')]),
  dict(t='Una cartella dal nome corto', bn='ছোট নামের ফোল্ডার', el=[
   ('p', 'Copia questo percorso con il bottone **Copia**:', 'Copia বোতাম দিয়ে এই পথটি কপি করো:'),
   ('copia', r'C:\Users\Public\ec'),
   ('p', 'Nella finestra di Estrai tutto clicca nella casella del percorso, premi `Ctrl` + `A` e poi `Ctrl` + `V`.', 'Estrai tutto জানালায় পথের ঘরে ক্লিক করো, Ctrl + A তারপর Ctrl + V চাপো।'),
   ('nota', 'Il nome deve essere corto (per esempio anche `Documenti\\ec`): Eclipse ha file con nomi lunghissimi e con un percorso lungo Windows non li scompatta tutti.', 'নাম ছোট হতে হবে (যেমন Documenti\\ec): Eclipse-এ খুব লম্বা নামের ফাইল আছে, পথ লম্বা হলে Windows সব আনজিপ করতে পারে না।')]),
  dict(t='Aspetta la fine', bn='শেষ পর্যন্ত অপেক্ষা করো', el=[
   ('p', 'Clicca **Estrai** in basso a destra e aspetta che la finestra con la barra verde si chiuda **da sola**. Dura qualche minuto: sono migliaia di file.', 'নিচে ডানদিকে Estrai ক্লিক করো, সবুজ বারের জানালা নিজে বন্ধ হওয়া পর্যন্ত অপেক্ষা করো। কয়েক মিনিট লাগে: হাজার হাজার ফাইল।')]),
  dict(t='Controlla la cartella eclipse', bn='eclipse ফোল্ডার যাচাই করো', el=[
   ('p', 'Apri la cartella **ec** e poi la cartella **eclipse**. Dentro ci devono essere le cartelle **configuration**, **features** e **plugins**.', 'ec ফোল্ডার খোলো, তারপর eclipse ফোল্ডার। ভিতরে configuration, features আর plugins ফোল্ডার থাকতে হবে।'),
   ('stop', 'Mancano **features** o **plugins**? L\'estrazione non è finita. Se fai partire Eclipse così, compare l\'errore «unable to locate its companion shared library» (non trova i suoi pezzi). Cancella la cartella **ec** e rifai dal passo 1, aspettando la fine.', 'features বা plugins নেই? আনজিপ শেষ হয়নি। এভাবে চালালে «unable to locate its companion shared library» ভুল আসে। ec ফোল্ডার মুছে ১ নম্বর ধাপ থেকে আবার করো, শেষ পর্যন্ত অপেক্ষা করে।')]),
  dict(t='Avvia Eclipse', bn='Eclipse চালু করো', el=[
   ('p', 'Nella cartella **eclipse** fai doppio clic su **eclipse.exe** (l\'icona con il cerchio viola). La prima volta si apre piano: aspetta.', 'eclipse ফোল্ডারে eclipse.exe-তে (বেগুনি বৃত্তের আইকন) দুবার ক্লিক করো। প্রথমবার ধীরে খোলে: অপেক্ষা করো।')]),
  dict(t='Il workspace: Launch', bn='workspace: Launch', el=[
   ('p', 'Compare la finestra del **workspace** (la cartella dove Eclipse salva i tuoi progetti). Non cambiare niente e clicca **«Launch»** (Avvia) in basso a destra.', 'workspace জানালা আসবে (যে ফোল্ডারে Eclipse তোমার প্রজেক্ট রাখে)। কিছু বদলিও না, নিচে ডানদিকে Launch (চালু করো) ক্লিক করো।')]),
 ]),
 dict(t='Il primo avvio', bn='প্রথমবার চালু', intro=[], passi=[
  dict(t='La pagina Sponsor: Later', bn='Sponsor পাতা: Later', el=[
   ('p', 'Si apre la pagina **«Sponsor the Eclipse IDE»** (Sostieni Eclipse). Clicca il bottone arancione **«Later»** (Più tardi).', '«Sponsor the Eclipse IDE» পাতা খুলবে। কমলা রঙের Later (পরে) বোতামে ক্লিক করো।'),
   ('img', '01-sponsor.jpg', 'La pagina Sponsor: il bottone «Later» è arancione.', 'Sponsor পাতা: Later বোতামটি কমলা রঙের।')]),
  dict(t='Chiudi le linguette', bn='ট্যাবগুলো বন্ধ করো', el=[
   ('p', 'In alto restano delle linguette (schede) aperte. Chiudile una alla volta con la **X** accanto al nome. A sinistra compare il riquadro **«Package Explorer»** (Esplora pacchetti) con la scritta blu **«Create a Java project»**.', 'উপরে কিছু ট্যাব খোলা থাকে। নামের পাশের X দিয়ে একটা একটা করে বন্ধ করো। বামে Package Explorer দেখা যাবে, নীল লেখা Create a Java project সহ।'),
   ('img', '02-package-explorer.jpg', 'A sinistra il Package Explorer con «Create a Java project».', 'বামে Package Explorer, Create a Java project সহ।')]),
 ]),
 dict(t='Il progetto HelloWorld', bn='HelloWorld প্রজেক্ট', intro=[
  ('p', 'Come in Lazarus: **un progetto = una cartella**. Eclipse la crea da solo.', 'Lazarus-এর মতো: একটি প্রজেক্ট = একটি ফোল্ডার। Eclipse নিজেই বানায়।')], passi=[
  dict(t='Create a Java project', bn='Create a Java project', el=[
   ('p', 'A sinistra clicca la scritta blu **«Create a Java project»** (Crea un progetto Java). Si apre la finestra **«New Java Project»** (Nuovo progetto Java).', 'বামে নীল লেখা Create a Java project-এ ক্লিক করো। New Java Project জানালা খুলবে।')]),
  dict(t='Il nome del progetto', bn='প্রজেক্টের নাম', el=[
   ('p', 'Nella casella in alto **«Project name»** (Nome del progetto) scrivi, tutto attaccato:', 'উপরের Project name ঘরে লেখো, একসাথে:'),
   ('copia', 'HelloWorld'),
   ('nota', 'Compare un avviso giallo sul nome del modulo («discouraged module name»): si ignora, sparisce al passo dopo.', 'মডিউলের নাম নিয়ে হলুদ সতর্কবার্তা আসে: উপেক্ষা করো, পরের ধাপে চলে যায়।'),
   ('img', '03-nuovo-progetto.jpg', 'New Java Project: Project name HelloWorld; in basso la sezione Module.', 'New Java Project: Project name HelloWorld; নিচে Module অংশ।')]),
  dict(t='Togli la spunta module-info', bn='module-info-র টিক তুলে দাও', el=[
   ('p', 'In fondo alla finestra, nella parte **«Module»** (Modulo), **togli la spunta** a **«Create module-info.java file»** (Crea il file module-info.java). L\'avviso giallo sparisce.', 'জানালার নিচে Module অংশে Create module-info.java file-এর টিক তুলে দাও। হলুদ সতর্কবার্তা চলে যায়।'),
   ('stop', 'La spunta **«Create module-info.java file»** va **TOLTA**. Se resta, dopo compaiono gli errori «Unresolved compilation problem» e «A package name must be specified for a module» (vedi gli errori comuni in fondo).', 'Create module-info.java file-এর টিক অবশ্যই তুলে দিতে হবে। থেকে গেলে পরে «Unresolved compilation problem» আর «A package name must be specified for a module» ভুল আসে (শেষে সাধারণ ভুল দেখো)।'),
   ('img', '04-senza-module-info.jpg', 'Spunta tolta, nessun avviso: ora si può fare Finish.', 'টিক তোলা, কোনো সতর্কবার্তা নেই: এখন Finish করা যায়।')]),
  dict(t='Finish', bn='Finish', el=[
   ('p', 'Clicca **«Finish»** (Fine) in basso a destra. A sinistra compare il progetto **HelloWorld**.', 'নিচে ডানদিকে Finish (শেষ) ক্লিক করো। বামে HelloWorld প্রজেক্ট দেখা যাবে।'),
   ('img', '05-progetto-creato.jpg', 'Il progetto HelloWorld nel Package Explorer.', 'Package Explorer-এ HelloWorld প্রজেক্ট।'),
   ('fatto', 'Il tuo primo progetto Java esiste.', 'তোমার প্রথম Java প্রজেক্ট তৈরি।')]),
 ]),
 dict(t='La classe Main', bn='Main ক্লাস', intro=[
  ('p', 'Il codice Java sta dentro una **classe**: per ora pensala come la unit di Lazarus, un file di codice.', 'Java কোড একটি ক্লাসের ভিতরে থাকে: এখন এটাকে Lazarus-এর unit-এর মতো ভাবো, একটি কোডের ফাইল।')], passi=[
  dict(t='Apri il progetto', bn='প্রজেক্ট খোলো', el=[
   ('p', 'A sinistra clicca la **freccina** accanto a **HelloWorld**: compare la cartella **src** (da «source», il codice).', 'বামে HelloWorld-এর পাশের ছোট তীরে ক্লিক করো: src ফোল্ডার দেখা যাবে (source = কোড)।')]),
  dict(t='New Class', bn='New Class', el=[
   ('p', 'Clic **destro** su **src**, poi **«New»** (Nuovo), poi **«Class»** (Classe). Si apre la finestra **«New Java Class»**.', 'src-এ ডান ক্লিক, তারপর New (নতুন), তারপর Class (ক্লাস)। New Java Class জানালা খুলবে।'),
   ('img', '06-nuova-classe.jpg', 'La finestra New Java Class.', 'New Java Class জানালা।')]),
  dict(t='Il nome: Main', bn='নাম: Main', el=[
   ('p', 'Clicca nella casella **«Name»** (Nome) e scrivi, con la M maiuscola:', 'Name (নাম) ঘরে ক্লিক করো আর লেখো, বড় হাতের M দিয়ে:'),
   ('copia', 'Main'),
   ('stop', 'Errore comune: Main scritto nella casella **«Package»** (Pacchetto) invece che in **«Name»**. Compare «Type name is empty» (il nome è vuoto). La casella **Package resta vuota**.', 'সাধারণ ভুল: Main লেখা হয়েছে Package ঘরে, Name-এ নয়। «Type name is empty» আসে। Package ঘর খালি থাকবে।'),
   ('img', '06b-errore-package.jpg', 'ERRORE: Main finito in Package. Va in Name.', 'ভুল: Main গেছে Package-এ। এটা Name-এ যাবে।'),
   ('nota', 'Con il nome giusto compare l\'avviso giallo «The use of the default package is discouraged» (meglio non usare il pacchetto di base). Si ignora.', 'সঠিক নাম দিলে হলুদ সতর্কবার্তা আসে «The use of the default package is discouraged»। উপেক্ষা করো।'),
   ('img', '07-avviso-default-package.jpg', 'Name: Main. L\'avviso giallo si ignora.', 'Name: Main। হলুদ সতর্কবার্তা উপেক্ষা করো।')]),
  dict(t='La spunta main', bn='main-এর টিক', el=[
   ('p', 'Più sotto metti la spunta a **«public static void main(String[] args)»**: è il punto di partenza del programma.', 'নিচে public static void main(String[] args)-এ টিক দাও: এটা প্রোগ্রামের শুরুর জায়গা।'),
   ('img', '08-pronto-finish.jpg', 'Tutto pronto: Name Main e la spunta main.', 'সব তৈরি: Name Main আর main-এর টিক।')]),
  dict(t='Finish: si apre Main.java', bn='Finish: Main.java খোলে', el=[
   ('p', 'Clicca **«Finish»** (Fine). Al centro si apre il file **Main.java** con un po\' di codice già scritto da Eclipse.', 'Finish ক্লিক করো। মাঝখানে Main.java খুলবে, Eclipse-এর লেখা কিছু কোডসহ।'),
   ('img', '09-main-java.jpg', 'Main.java aperto al centro.', 'মাঝখানে Main.java খোলা।')]),
 ]),
 dict(t='Il codice e il bottone Hello World', bn='কোড আর Hello World বোতাম', intro=[], passi=[
  dict(t='Copia il codice', bn='কোড কপি করো', el=[
   ('p', 'Clicca il bottone **Copia** del riquadro qui sotto: copia tutto il programma.', 'নিচের বাক্সের Copia বোতামে ক্লিক করো: পুরো প্রোগ্রাম কপি হবে।'),
   ('codice',)]),
  dict(t='Incolla al posto di tutto', bn='সবকিছুর জায়গায় পেস্ট করো', el=[
   ('p', 'Clicca dentro il codice di **Main.java**, premi `Ctrl` + `A` (seleziona tutto) e poi `Ctrl` + `V` (incolla).', 'Main.java-র কোডের ভিতরে ক্লিক করো, Ctrl + A (সব বাছো) তারপর Ctrl + V (পেস্ট) চাপো।'),
   ('img', '14-codice-v2.jpg', 'Il codice incollato. Il pallino nero sulla linguetta Main.java vuol dire: non ancora salvato.', 'পেস্ট করা কোড। Main.java ট্যাবে কালো বিন্দু মানে: এখনো সেভ হয়নি।'),
   ('stop', 'Errore comune: righe doppie e una **X rossa** a sinistra. Hai incollato dentro una riga un testo vecchio rimasto negli appunti. Copia di nuovo con il bottone Copia, poi `Ctrl` + `A` e `Ctrl` + `V`.', 'সাধারণ ভুল: দুবার লাইন আর বামে লাল X। একটি লাইনের ভিতরে পুরনো লেখা পেস্ট হয়েছে। আবার Copia দিয়ে কপি করো, তারপর Ctrl + A আর Ctrl + V।'),
   ('img', '13-errore-incolla.jpg', 'ERRORE: testo vecchio incollato dentro una riga.', 'ভুল: একটি লাইনের ভিতরে পুরনো লেখা পেস্ট হয়েছে।')]),
  dict(t='Salva', bn='সেভ করো', el=[
   ('p', 'Premi `Ctrl` + `S` (salva). Il pallino nero sulla linguetta sparisce.', 'Ctrl + S (সেভ) চাপো। ট্যাবের কালো বিন্দু চলে যায়।'),
   ('p', 'In basso, nella scheda **«Problems»** (Problemi), conta solo **0 errors** (0 errori). Un **warning** (avviso giallo) non blocca niente.', 'নিচে Problems (সমস্যা) ট্যাবে শুধু 0 errors (০ ভুল) দরকার। warning (হলুদ সতর্কবার্তা) কিছু আটকায় না।'),
   ('img', '11-salvato.jpg', 'Esempio in basso: «0 errors, 1 warning». Va bene.', 'নিচে উদাহরণ: «0 errors, 1 warning»। ঠিক আছে।')]),
  dict(t='Run', bn='Run', el=[
   ('p', 'In alto clicca il **cerchio verde con il triangolo bianco**: è **«Run»** (Esegui), come il triangolo verde di Lazarus.', 'উপরে সবুজ বৃত্তে সাদা ত্রিভুজে ক্লিক করো: এটা Run (চালাও), Lazarus-এর সবুজ ত্রিভুজের মতো।'),
   ('p', 'Si apre la finestra **«Il mio primo programma»** con il bottone **Premi**. Se non la vedi, è dietro Eclipse: cercala nella barra in basso dello schermo.', '«Il mio primo programma» জানালা খুলবে, Premi বোতামসহ। না দেখলে, এটা Eclipse-এর পিছনে: স্ক্রিনের নিচের বারে খোঁজো।')]),
  dict(t='Premi', bn='Premi চাপো', el=[
   ('p', 'Clicca **Premi**. Si apre una finestrella con scritto **Hello World** e il bottone **OK**.', 'Premi ক্লিক করো। ছোট জানালা খুলবে, Hello World লেখা আর OK বোতাম।'),
   ('stop', 'Vedi «Hello World» scritto **accanto al bottone**, nella stessa finestra, senza finestrella? Hai ancora il codice vecchio: rifai i passi 18, 19 e 20 (copia, incolla, salva).', 'বোতামের পাশে, একই জানালায় Hello World দেখছো, ছোট জানালা ছাড়া? পুরনো কোড আছে: ১৮, ১৯, ২০ ধাপ আবার করো (কপি, পেস্ট, সেভ)।'),
   ('img', '12-versione1-finestra.jpg', 'Così è il codice VECCHIO: la scritta nella stessa finestra.', 'এটা পুরনো কোড: একই জানালায় লেখা।'),
   ('fatto', 'La finestrella **Hello World** con **OK**: il tuo primo programma Java con la finestra! Clicca OK e chiudi con la X.', 'OK-সহ Hello World ছোট জানালা: জানালাসহ তোমার প্রথম Java প্রোগ্রাম! OK ক্লিক করো, X দিয়ে বন্ধ করো।')]),
  dict(t='Fallo tuo', bn='নিজের মতো করো', el=[
   ('p', 'Nel codice cambia **"Hello World"** con una frase tua e **"Premi"** con una parola tua. Lascia le virgolette `"`. Poi `Ctrl` + `S` e Run.', 'কোডে "Hello World"-এর জায়গায় তোমার নিজের বাক্য আর "Premi"-এর জায়গায় তোমার শব্দ লেখো। " চিহ্ন রেখে দাও। তারপর Ctrl + S আর Run।'),
   ('p', '**Mostralo** al compagno: premi il bottone davanti a lui.', 'সহপাঠীকে দেখাও: তার সামনে বোতাম চাপো।')]),
 ]),
]

CONFRONTO = [
 ('la finestra', '`Form1`', '`JFrame`'),
 ('il bottone', '`TButton`', '`JButton`'),
 ('quando premi il bottone', '`Button1Click`', '`addActionListener`'),
 ('il messaggio', "`ShowMessage('Hello World');`", '`JOptionPane.showMessageDialog(finestra, "Hello World");`'),
]
CONFRONTO_BN = 'Form1 = JFrame (জানালা)। TButton = JButton (বোতাম)। Button1Click = addActionListener (বোতাম চাপলে)। ShowMessage = JOptionPane.showMessageDialog (বার্তা)।'

RIGHE = [
 ('`import javax.swing.*;`', 'prende i pezzi per fare le finestre (come `uses` in Lazarus)', 'জানালা বানানোর অংশ আনে (Lazarus-এর uses-এর মতো)'),
 ('`import java.awt.FlowLayout;`', 'prende il modo di mettere in fila i componenti', 'অংশগুলো সারিতে রাখার নিয়ম আনে'),
 ('`public class Main {`', 'la classe: il nome è uguale al file Main.java', 'ক্লাস: নাম ফাইল Main.java-র মতো'),
 ('`public static void main(String[] args) {`', 'il punto di partenza: il programma comincia da qui', 'শুরুর জায়গা: প্রোগ্রাম এখান থেকে শুরু'),
 ('`JFrame finestra = new JFrame("…");`', 'crea la finestra con il titolo (il Form)', 'শিরোনামসহ জানালা বানায় (Form)'),
 ('`JButton bottone = new JButton("Premi");`', 'crea il bottone (TButton)', 'বোতাম বানায় (TButton)'),
 ('`bottone.addActionListener(e -> …);`', 'quando premi il bottone, fai questo (Button1Click)', 'বোতাম চাপলে এটা করো (Button1Click)'),
 ('`JOptionPane.showMessageDialog(finestra, "Hello World")`', 'apre la finestrella con il messaggio e OK (ShowMessage)', 'বার্তা আর OK-সহ ছোট জানালা খোলে (ShowMessage)'),
 ('`finestra.setLayout(new FlowLayout());`', 'i componenti si mettono in fila, uno dopo l\'altro', 'অংশগুলো একটার পর একটা সারিতে বসে'),
 ('`finestra.add(bottone);`', 'mette il bottone nella finestra', 'বোতামটি জানালায় রাখে'),
 ('`finestra.setSize(300, 150);`', 'larghezza e altezza (Width e Height)', 'প্রস্থ আর উচ্চতা (Width, Height)'),
 ('`setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)`', 'con la X il programma si chiude davvero', 'X চাপলে প্রোগ্রাম সত্যিই বন্ধ হয়'),
 ('`finestra.setVisible(true);`', 'mostra la finestra', 'জানালা দেখায়'),
 ('`;` e `{ }`', 'fine istruzione; inizio e fine di un blocco (`begin … end`)', 'নির্দেশের শেষ; ব্লকের শুরু আর শেষ (begin … end)'),
]

ERRORI = [
 ('«unable to locate its companion shared library»', 'lo ZIP non è stato scompattato tutto', 'cancella la cartella ec e rifai dal passo 1, aspettando la fine', 'ZIP পুরো আনজিপ হয়নি: ec মুছে ১ নম্বর ধাপ থেকে আবার করো'),
 ('«Unresolved compilation problem», X rossa sulla riga `import javax.swing`', 'il progetto ha il file module-info.java', 'cancella module-info.java, poi Ctrl + S e Run', 'প্রজেক্টে module-info.java আছে: সেটি মুছে দাও, তারপর Ctrl + S আর Run'),
 ('«A package name must be specified for a module»', 'il progetto ha il file module-info.java', 'cancella module-info.java, poi rifai la classe', 'প্রজেক্টে module-info.java আছে: সেটি মুছে দাও, তারপর ক্লাস আবার বানাও'),
 ('«Type name is empty»', 'Main scritto in Package', 'Package vuoto, Main in Name', 'Main Package-এ লেখা: Package খালি, Main যাবে Name-এ'),
 ('righe doppie e X rossa', 'incollato dentro una riga un testo vecchio', 'copia di nuovo, poi Ctrl + A e Ctrl + V', 'লাইনের ভিতরে পুরনো লেখা: আবার কপি, তারপর Ctrl + A আর Ctrl + V'),
 ('pallino nero sulla linguetta', 'il file non è salvato', 'Ctrl + S', 'ফাইল সেভ হয়নি: Ctrl + S'),
 ('Hello World accanto al bottone', 'codice vecchio', 'rifai i passi 18, 19 e 20', 'পুরনো কোড: ১৮, ১৯, ২০ ধাপ আবার করো'),
 ('premi Run e non si vede niente', 'la finestra è dietro Eclipse', 'cercala nella barra in basso dello schermo', 'জানালা Eclipse-এর পিছনে: নিচের বারে খোঁজো'),
]

# Errori comuni con la schermata e la soluzione passo per passo (28/10/2026, v1.1)
ERRORI_IMG = [
 dict(t='«Unresolved compilation problem» e la X rossa su import javax.swing', bn='«Unresolved compilation problem» আর import javax.swing-এ লাল X',
  el=[
  ('p', 'Premi Run e in basso, nella scheda **«Console»**, compare in rosso **«Unresolved compilation problem»** (problema di compilazione non risolto). Sulla riga `import javax.swing.*;` c\'è una **X rossa**.', 'Run চাপলে নিচে Console ট্যাবে লাল রঙে «Unresolved compilation problem» আসে। import javax.swing.*; লাইনে লাল X থাকে।'),
  ('img', '15-errore-import-module.jpg', 'ERRORE: X rossa sulla riga 1 e «Unresolved compilation problem» nella Console.', 'ভুল: ১ নম্বর লাইনে লাল X আর Console-এ «Unresolved compilation problem»।'),
  ('p', 'Perché: il progetto è stato creato **con** il file **module-info.java** (la spunta non è stata tolta). Questo file non lascia usare le finestre di `javax.swing`.', 'কারণ: প্রজেক্ট module-info.java ফাইলসহ বানানো হয়েছে (টিক তোলা হয়নি)। এই ফাইল javax.swing-এর জানালা ব্যবহার করতে দেয় না।'),
  ('p', 'Soluzione 1: a sinistra, nel **Package Explorer**, apri **HelloWorld** e poi **src**.', 'সমাধান ১: বামে Package Explorer-এ HelloWorld খোলো, তারপর src।'),
  ('p', 'Soluzione 2: fai clic **destro** su **module-info.java** e scegli **«Delete»** (Elimina).', 'সমাধান ২: module-info.java-তে ডান ক্লিক করো, Delete (মুছে ফেলো) বেছে নাও।'),
  ('p', 'Soluzione 3: nella finestrella clicca **«OK»**.', 'সমাধান ৩: ছোট জানালায় OK ক্লিক করো।'),
  ('p', 'Soluzione 4: clicca dentro Main.java, premi `Ctrl` + `S` e poi **Run**.', 'সমাধান ৪: Main.java-র ভিতরে ক্লিক করো, Ctrl + S চাপো, তারপর Run।'),
  ('nota', 'Se nella Console leggi **Main.Main.main**, la classe è finita nel pacchetto «Main»: rifai la classe lasciando vuota la casella **Package** (passo 15).', 'Console-এ Main.Main.main লেখা থাকলে ক্লাসটি «Main» প্যাকেজে চলে গেছে: Package ঘর খালি রেখে ক্লাস আবার বানাও (১৫ নম্বর ধাপ)।')]),
 dict(t='«A package name must be specified for a module»', bn='«A package name must be specified for a module»',
  el=[
  ('p', 'Nella finestra **«New Java Class»** compare in alto, con la X rossa, **«A package name must be specified for a module»** (per un modulo serve il nome del pacchetto) e **Finish** è grigio.', 'New Java Class জানালায় উপরে লাল X-সহ «A package name must be specified for a module» আসে, আর Finish ধূসর থাকে।'),
  ('img', '16-errore-package-module.jpg', 'ERRORE: la X rossa in alto e Finish grigio.', 'ভুল: উপরে লাল X আর Finish ধূসর।'),
  ('p', 'Perché: è la stessa causa, il progetto ha il file **module-info.java**.', 'কারণ: একই কারণ, প্রজেক্টে module-info.java ফাইল আছে।'),
  ('p', 'Soluzione 1: clicca **«Cancel»** (Annulla) in basso a destra.', 'সমাধান ১: নিচে ডানদিকে Cancel (বাতিল) ক্লিক করো।'),
  ('p', 'Soluzione 2: cancella **module-info.java** come sopra: **Package Explorer**, **src**, clic destro, **«Delete»**, **«OK»**.', 'সমাধান ২: উপরের মতো module-info.java মুছে দাও: Package Explorer, src, ডান ক্লিক, Delete, OK।'),
  ('p', 'Soluzione 3: rifai la classe dal passo 14 (clic destro su **src**, New, Class).', 'সমাধান ৩: ১৪ নম্বর ধাপ থেকে ক্লাস আবার বানাও (src-এ ডান ক্লিক, New, Class)।')]),
]

# numerazione continua dei passi
n = 0
for parte in PARTI:
    for p in parte['passi']:
        n += 1; p['n'] = n
TOT = n
assert TOT == 23, TOT  # i riferimenti «passi 18, 19 e 20» dipendono da questo

def inl(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)

def bnp(t):
    return f'<p class="bn" lang="bn">{inl(t)}</p>'

# ---------- HTML (pagina e PDF condividono il corpo) ----------
def corpo_html(img_dir, pagina):
    o = []
    def el_html(e, idp):
        k = e[0]
        if k == 'p': return f'<p>{inl(e[1])}</p>' + bnp(e[2])
        if k in ('nota', 'stop', 'fatto'):
            pre = {'nota': 'Nota', 'stop': 'Attenzione', 'fatto': 'FATTO!'}[k]
            pbn = {'nota': 'মনে রাখো', 'stop': 'সাবধান', 'fatto': 'হয়ে গেছে!'}[k]
            return f'<div class="box {k}"><p><b>{pre}</b> {inl(e[1])}</p>' + bnp(f'**{pbn}** ' + e[2]) + '</div>'
        if k == 'img':
            src = img_dir + e[1]
            im = f'<img src="{src}" alt="{html.escape(e[2])}"' + (' loading="lazy">' if pagina else '>')
            if pagina: im = f'<a href="{src}" target="_blank" rel="noopener">{im}</a>'
            return f'<figure>{im}<figcaption>{inl(e[2])}' + f'<span class="bn" lang="bn">{inl(e[3])}</span></figcaption></figure>'
        if k == 'copia': return copia_html(e[1])
        if k == 'codice': return copia_html(CODICE, codice=True)
    for i, parte in enumerate(PARTI, 1):
        o.append(f'<section class="parte"><h2>{i:02d} {inl(parte["t"])}<span class="bn h" lang="bn">{inl(parte["bn"])}</span></h2>')
        for e in parte['intro']: o.append(el_html(e, None))
        for p in parte['passi']:
            fatto = (f'<label class="fatto-chk"><input type="checkbox" data-k="{p["n"]}"> Fatto <span lang="bn">হয়ে গেছে</span></label>' if pagina else '')
            o.append(f'<div class="passo" id="passo-{p["n"]}"><div class="testa"><span class="num">{p["n"]}</span><h3>{inl(p["t"])}<span class="bn h" lang="bn">{inl(p["bn"])}</span></h3>{fatto}</div>')
            for e in p['el']: o.append(el_html(e, p['n']))
            o.append('</div>')
        o.append('</section>')
    i = len(PARTI)
    # confronto Lazarus
    i += 1
    o.append(f'<section class="parte fine"><h2>{i:02d} Lazarus e Java a confronto<span class="bn h" lang="bn">Lazarus আর Java তুলনা</span></h2>')
    o.append('<p>Hai già fatto lo stesso programma in Lazarus: cambiano le parole, l\'idea è la stessa.</p>' + bnp('তুমি একই প্রোগ্রাম Lazarus-এ বানিয়েছো: শব্দ বদলায়, ধারণা একই।'))
    o.append('<div class="tab"><table><tr><th>Che cosa</th><th>Lazarus</th><th>Java</th></tr>' + ''.join(f'<tr><td>{inl(a)}</td><td>{inl(b)}</td><td>{inl(c)}</td></tr>' for a, b, c in CONFRONTO) + '</table></div>' + bnp(CONFRONTO_BN))
    src = img_dir + 'lazarus-showmessage.jpg'
    o.append(f'<figure class="piccola"><img src="{src}" alt="Lazarus: ShowMessage Hello World"><figcaption>In Lazarus: Form1, Button1 e la finestrella di <code>ShowMessage</code> con OK.<span class="bn" lang="bn">Lazarus-এ: Form1, Button1 আর ShowMessage-এর OK-সহ ছোট জানালা।</span></figcaption></figure></section>')
    # riga per riga
    i += 1
    o.append(f'<section class="parte fine"><h2>{i:02d} Il codice riga per riga<span class="bn h" lang="bn">লাইন ধরে ধরে কোড</span></h2>')
    o.append('<div class="tab"><table><tr><th>Riga</th><th>Che cosa vuol dire</th></tr>' + ''.join(f'<tr><td>{inl(a)}</td><td>{inl(b)}<span class="bn" lang="bn">{inl(c)}</span></td></tr>' for a, b, c in RIGHE) + '</table></div>')
    o.append('<div class="box nota"><p><b>Prova del nove</b> Spiega al compagno, in 30 secondi e con parole tue, che cosa succede quando premi il bottone.</p>' + bnp('**নিজে যাচাই** ৩০ সেকেন্ডে, নিজের ভাষায়, সহপাঠীকে বলো বোতাম চাপলে কী হয়।') + '</div></section>')
    # errori
    i += 1
    o.append(f'<section class="parte"><h2>{i:02d} Errori comuni: succede a tutti<span class="bn h" lang="bn">সাধারণ ভুল: সবার হয়</span></h2>')
    o.append('<p>Sbagliare è normale, anche per i programmatori professionisti. Con `Ctrl` + `Z` annulli l\'ultima modifica.</p>'.replace('`Ctrl`', '<code>Ctrl</code>').replace('`Z`', '<code>Z</code>') + bnp('ভুল হওয়া স্বাভাবিক, পেশাদার প্রোগ্রামারদেরও। Ctrl + Z দিয়ে শেষ পরিবর্তন বাতিল করো।'))
    o.append('<div class="tab"><table><tr><th>Che cosa vedi</th><th>Perché</th><th>Come si sistema</th></tr>' + ''.join(f'<tr><td>{inl(a)}</td><td>{inl(b)}</td><td>{inl(c)}<span class="bn" lang="bn">{inl(d)}</span></td></tr>' for a, b, c, d in ERRORI) + '</table></div>')
    for x in ERRORI_IMG:
        o.append(f'<div class="passo errore"><div class="testa"><span class="num">!</span><h3>{inl(x["t"])}<span class="bn h" lang="bn">{inl(x["bn"])}</span></h3></div>')
        for e in x['el']: o.append(el_html(e, None))
        o.append('</div>')
    o.append('</section>')
    return '\n'.join(o)

def copia_html(t, codice=False):
    return (f'<div class="copia{" lungo" if codice else ""}"><pre>{html.escape(t)}</pre>'
            '<button type="button" class="bt-copia" onclick="copia(this)">Copia</button></div>')

CSS = '''
:root{--bg:#f6f8fb;--card:#fff;--tx:#1d2733;--mu:#5b6573;--bd:#d5dbe3;--ac:#1f6feb;--ok:#2f855a}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--tx);font-family:Verdana,"Segoe UI",Arial,"Noto Sans Bengali","Nirmala UI","Vrinda",sans-serif;font-size:18px;line-height:1.6}
main{max-width:860px;margin:0 auto;padding:12px 16px 60px}
h1{font-size:1.5em;line-height:1.25;margin:14px 0 4px}h2{font-size:1.3em;margin:28px 0 10px;border-bottom:3px solid var(--ac);padding-bottom:4px}
h3{font-size:1.1em;margin:0;line-height:1.3}
.bn{display:block;color:var(--mu);font-size:.92em;margin-top:-4px;font-family:"Noto Sans Bengali","Nirmala UI","Vrinda",FreeSans,sans-serif}
.h{font-weight:normal;font-size:.8em;margin-top:2px}
p{margin:8px 0}code{background:#eef2f7;border:1px solid var(--bd);border-radius:5px;padding:0 5px;font-family:Consolas,"JetBrains Mono",monospace;font-size:.92em;word-break:break-word}
.banner{background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:10px 12px;margin:10px 0}
.passo{background:var(--card);border:2px solid var(--bd);border-radius:14px;padding:12px 14px;margin:14px 0}
.passo.ok{border-color:var(--ok);background:#f1faf4}
.testa{display:flex;gap:10px;align-items:flex-start;flex-wrap:wrap}
.num{flex:0 0 auto;background:var(--ac);color:#fff;font-weight:bold;border-radius:50%;width:38px;height:38px;display:flex;align-items:center;justify-content:center;font-size:1.05em}
.passo.ok .num{background:var(--ok)}
.testa h3{flex:1 1 200px}
.fatto-chk{flex:0 0 auto;border:2px solid var(--ok);border-radius:10px;padding:4px 10px;font-weight:bold;color:var(--ok);cursor:pointer;user-select:none;font-size:.9em}
.fatto-chk input{width:20px;height:20px;vertical-align:middle;accent-color:var(--ok)}
figure{margin:10px 0}figure img{width:100%;height:auto;border:1px solid var(--bd);border-radius:8px;display:block}
figure.piccola img{max-width:520px}
figcaption{font-size:.85em;color:var(--mu);margin-top:4px}
.box{border-radius:10px;padding:8px 12px;margin:10px 0;border:2px solid}
.box p{margin:4px 0}.nota{background:#fff8d6;border-color:#d4a017}.stop{background:#fde8e8;border-color:#c53030}.fatto{background:#e8f7ee;border-color:var(--ok)}
.copia{position:relative;margin:8px 0}
.copia pre{background:#0d1117;color:#e6edf3;padding:12px;padding-right:90px;border-radius:10px;font-size:15px;overflow-x:auto;margin:0;font-family:Consolas,"JetBrains Mono",monospace;line-height:1.45}
.bt-copia{position:absolute;top:6px;right:6px;background:var(--ok);color:#fff;border:0;border-radius:8px;padding:8px 14px;font-size:16px;font-weight:bold;cursor:pointer}
.tab{overflow-x:auto;max-width:100%}table{border-collapse:collapse;width:100%;margin:8px 0;font-size:.9em}
th,td{border:1px solid var(--bd);padding:6px;text-align:left;vertical-align:top}th{background:#eef2f7}td .bn{margin-top:4px}
.contatore{position:sticky;top:0;z-index:5;background:var(--ac);color:#fff;border-radius:0 0 10px 10px;padding:6px 12px;font-weight:bold;font-size:.95em}
.torna{display:inline-block;margin-top:6px;color:var(--ac)}
'''

JS = '''
function copia(b){var t=b.previousElementSibling.innerText;function ok(){b.textContent='Copiato!';setTimeout(function(){b.textContent='Copia'},2000)}
 if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){vecchio(t);ok()})}else{vecchio(t);ok()}}
function vecchio(t){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(a)}
var K='3inf-eclipse-guida-v1',S={};try{S=JSON.parse(localStorage.getItem(K)||'{}')||{}}catch(e){S={}}
function conta(){var c=document.querySelectorAll('.fatto-chk input'),f=0;c.forEach(function(x){if(x.checked)f++});document.getElementById('cnt').textContent=f+' / '+c.length}
document.querySelectorAll('.fatto-chk input').forEach(function(x){var k=x.dataset.k;x.checked=!!S[k];x.closest('.passo').classList.toggle('ok',x.checked);
 x.addEventListener('change',function(){S[k]=x.checked;x.closest('.passo').classList.toggle('ok',x.checked);try{localStorage.setItem(K,JSON.stringify(S))}catch(e){}conta()})});
conta();
'''

def pagina():
    corpo = corpo_html('img/', True)
    return f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Eclipse Hello World</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="contatore">3INF · Passi fatti: <span id="cnt">0 / {TOT}</span></div>
<main>
<div class="banner"><p style="margin:0"><b>Questa pagina può cambiare durante la lezione: ogni tanto premi F5 per vedere la versione nuova.</b></p>{bnp("**এই পাতাটি ক্লাসের সময় বদলাতে পারে: মাঝে মাঝে F5 চাপো, নতুন সংস্করণ দেখতে।**")}</div>
<h1>{TITOLO}</h1>{bnp(TITOLO_BN)}
<p style="color:var(--mu);font-size:.85em">3INF · 28/10/2026 · guida con le schermate vere di Eclipse · versione {VERSIONE}</p>
<a class="torna" href="../verifica/?b=3inf-eclipse-java">Torna alla lezione di oggi</a>
{corpo}
<p style="margin-top:30px"><a class="torna" href="../verifica/?b=3inf-eclipse-java">Torna alla lezione di oggi (consegna su Classroom)</a></p>
</main><script>{JS}</script></body></html>
'''

def stampa():
    img = 'file://' + os.path.join(RADICE, 'docs/3inf-eclipse-guida/img/')
    css = CSS.replace('font-size:18px', 'font-size:11pt') + '''
body{background:#fff;font-family:"DejaVu Sans",FreeSans,sans-serif}.bn{font-family:FreeSans,"DejaVu Sans",sans-serif}
main{max-width:none;padding:0}.bt-copia{display:none}.copia pre{padding-right:12px;font-size:9pt;white-space:pre-wrap}
.passo{padding:8px 12px;margin:10px 0}figure,.box,.copia,tr{break-inside:avoid;page-break-inside:avoid}.testa,h2,h2+p,h2+p+p.bn{break-after:avoid;page-break-after:avoid}figure img{max-height:105mm;width:auto;max-width:100%}
h2{break-after:avoid;page-break-after:avoid}.parte{break-before:auto}code{font-size:.88em}
.fine{break-before:page;page-break-before:always}.intest{border:1px solid #d5dbe3;border-radius:8px;padding:8px 12px;margin:8px 0;font-size:.9em}
'''
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><title>{NOME}</title><style>{css}</style></head><body><main>
<h1>{TITOLO}</h1>{bnp(TITOLO_BN)}
<div class="intest"><p><b>Versione {VERSIONE}</b> · 28/10/2026 · Classe 3INF · dispensa per gli allievi (italiano con una riga di aiuto in bangla)</p>
<p>La pagina con le spunte e il bottone Copia: nicolaregge-pulse.github.io/corso-informatica/3inf-eclipse-guida/</p></div>
{corpo_html(img, False)}
<h2>{len(PARTI)+4:02d} Changelog</h2><p>1. Versione 1.0 (28/10/2026): prima versione, con le schermate reali di Eclipse 2026-09 prese dal docente.</p><p>2. Versione 1.1 (28/10/2026): due errori comuni con la schermata e la soluzione («Unresolved compilation problem» con la X rossa su import javax.swing; «A package name must be specified for a module»): si cancella module-info.java; riquadro rosso al passo della spunta module-info.</p>
</main></body></html>'''

# ---------- Markdown ----------
def md():
    L = [f'# {TITOLO}', '', f'*{TITOLO_BN}*', '',
         f'**Versione {VERSIONE}** · 28/10/2026 · Classe 3INF · dispensa per gli allievi (italiano con una riga di aiuto in bangla, bengalese, sotto ogni frase)', '',
         'Pagina con le spunte e il bottone Copia: https://nicolaregge-pulse.github.io/corso-informatica/3inf-eclipse-guida/ (sorgente `docs/3inf-eclipse-guida/index.html`). Generato da `classe-3/eclipse-java/_build/guida.py`.', '', '---', '']
    IMG = '../../docs/3inf-eclipse-guida/img/'
    def el(e, rientro=''):
        k = e[0]; r = rientro
        if k == 'p': return [r + e[1], '', r + f'*{e[2]}*', '']
        if k in ('nota', 'stop', 'fatto'):
            tag = {'nota': 'GIALLO', 'stop': 'ROSSO', 'fatto': 'GIALLO'}[k]
            pre = {'nota': 'Nota.', 'stop': 'Attenzione.', 'fatto': 'FATTO!'}[k]
            return [r + f'> [{tag}] {pre} {e[1]}', r + '>', r + f'> *{e[2]}*', '']
        if k == 'img': return [r + f'![{e[2]}]({IMG}{e[1]})', '', r + f'*{e[2]} · {e[3]}*', '']
        if k == 'copia': return [r + '```', *[r + x for x in e[1].split('\n')], r + '```', '']
        if k == 'codice': return [r + '```java', *[(r + x) if x else '' for x in CODICE.split('\n')], r + '```', '']
    for i, parte in enumerate(PARTI, 1):
        L += [f'## {i:02d} {parte["t"]}', '', f'*{parte["bn"]}*', '']
        for e in parte['intro']: L += el(e)
        for p in parte['passi']:
            L += [f'{p["n"]}. **{p["t"]}** ({p["bn"]})', '']
            for e in p['el']: L += el(e, '   ')
    i = len(PARTI) + 1
    L += [f'## {i:02d} Lazarus e Java a confronto', '', '*Lazarus আর Java তুলনা*', '',
          'Hai già fatto lo stesso programma in Lazarus: cambiano le parole, l\'idea è la stessa.', '', '*তুমি একই প্রোগ্রাম Lazarus-এ বানিয়েছো: শব্দ বদলায়, ধারণা একই।*', '',
          '| Che cosa | Lazarus | Java |', '|---|---|---|', *[f'| {a} | {b} | {c} |' for a, b, c in CONFRONTO], '', f'*{CONFRONTO_BN}*', '',
          f'![Lazarus: ShowMessage Hello World]({IMG}lazarus-showmessage.jpg)', '', '*In Lazarus: Form1, Button1 e la finestrella di ShowMessage con OK.*', '']
    i += 1
    L += [f'## {i:02d} Il codice riga per riga', '', '*লাইন ধরে ধরে কোড*', '', '| Riga | Che cosa vuol dire | বাংলা |', '|---|---|---|',
          *[f'| {a} | {b} | {c} |' for a, b, c in RIGHE], '',
          '> [GIALLO] Prova del nove: spiega al compagno, in 30 secondi e con parole tue, che cosa succede quando premi il bottone.', '>', '> *নিজে যাচাই: ৩০ সেকেন্ডে, নিজের ভাষায়, সহপাঠীকে বলো বোতাম চাপলে কী হয়।*', '']
    i += 1
    L += [f'## {i:02d} Errori comuni: succede a tutti', '', '*সাধারণ ভুল: সবার হয়*', '',
          'Sbagliare è normale, anche per i programmatori professionisti. Con `Ctrl` + `Z` annulli l\'ultima modifica.', '', '*ভুল হওয়া স্বাভাবিক, পেশাদার প্রোগ্রামারদেরও। Ctrl + Z দিয়ে শেষ পরিবর্তন বাতিল করো।*', '',
          '| Che cosa vedi | Perché | Come si sistema | বাংলা |', '|---|---|---|---|', *[f'| {a} | {b} | {c} | {d} |' for a, b, c, d in ERRORI], '']
    for x in ERRORI_IMG:
        L += [f'### {x["t"]}', '', f'*{x["bn"]}*', '']
        for e in x['el']: L += el(e)
    i += 1
    L += [f'## {i:02d} Changelog', '', '1. Versione 1.0 (28/10/2026): prima versione, con le schermate reali di Eclipse 2026-09 prese dal docente.', '2. Versione 1.1 (28/10/2026): due errori comuni con la schermata e la soluzione («Unresolved compilation problem» con la X rossa su import javax.swing; «A package name must be specified for a module»): si cancella module-info.java; riquadro rosso al passo della spunta module-info.', '']
    return '\n'.join(L)

os.makedirs(os.path.dirname(PAGINA), exist_ok=True)
open(PAGINA, 'w', encoding='utf-8').write(pagina())
open(os.path.join(OUT_DIR, NOME + '.md'), 'w', encoding='utf-8').write(md())
open(os.path.join(OUT_DIR, NOME + '.html'), 'w', encoding='utf-8').write(stampa())
print('ok', TOT, 'passi')
