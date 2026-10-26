from codici import *
L = dict(lang='it', dir='ltr', file='20261026_Classe-3-Teoria_v%s_Object-Pascal-e-Java', titolo='Object Pascal e Java a confronto',
         sotto='Perché con Object Pascal (Lazarus) si impara prima: meno codice, variabili senza «new», finestre disegnate con il mouse',
         classe='Classe 3 · 26/10/2026', es='Esempio', nota='Da sapere', sol='Soluzioni', foto='', pag='Pagina',
         intro='Lo stesso programma scritto in due linguaggi. Guarda quante righe servono e quante parole nuove devi imparare: capirai perché per cominciare usiamo Lazarus.')
S = [
('01 Due linguaggi', [
 ('p', '<b>Object Pascal</b> è il linguaggio di <b>Lazarus</b> (e di Delphi). <b>Java</b> è un linguaggio molto usato nelle aziende e nelle app Android.'),
 ('tab', [['', 'Object Pascal (Lazarus)', 'Java'], ['Come diventa un programma', 'compilato: diventa un file .exe', 'compilato in «bytecode», poi interpretato dalla Java Virtual Machine'], ['Che cosa serve sul PC', 'niente: il .exe parte da solo', 'Java installato (la macchina virtuale)'], ['Le finestre', 'le disegni con il mouse', 'le scrivi con il codice']])]),
('02 Hello World', [
 ('code', 'Object Pascal', HP), ('code', 'Java', HJ),
 ('p', 'In Java già per scrivere una frase servono una <b>classe</b> e il metodo <b>main</b>, con parole come <b>public</b>, <b>static</b>, <b>void</b>, <b>String[] args</b>. In Object Pascal bastano <b>begin</b> ed <b>end</b>.')]),
('03 Le variabili: niente «new»', [
 ('p', 'In Object Pascal le variabili si <b>dichiarano</b> nella sezione <b>var</b> con nome e tipo, e poi si usano subito. Anche un array è già pronto.'),
 ('code', 'Object Pascal', VP),
 ('p', 'In Java i tipi semplici (int, double) vanno bene, ma per un array o per leggere dalla tastiera bisogna <b>creare un oggetto</b> con la parola <b>new</b>.'),
 ('code', 'Java', VJ),
 ('nota', 'In Java l\'array parte da 0; in Pascal decidi tu dove parte (qui da 1). In Java ogni cosa «grande» va creata con new prima di usarla.')]),
('04 Una finestra con un bottone', [
 ('p', 'Con Lazarus trascini il bottone sul Form, fai doppio clic e scrivi <b>una riga</b>:'),
 ('code', 'Object Pascal (Lazarus)', FP),
 ('p', 'In Java (con Swing) la finestra e il bottone si scrivono tutti con il codice, e ognuno si crea con <b>new</b>:'),
 ('code', 'Java', FJ)]),
('05 Riassunto', [
 ('tab', [['Che cosa', 'Object Pascal', 'Java'], ['Hello World', '1 riga dentro begin…end', '5 righe con classe e main'], ['Variabili e array', 'nella sezione var, pronte subito', 'gli array e molti oggetti con new'], ['Leggere dalla tastiera', 'readln', 'new Scanner(System.in)'], ['Finestre e bottoni', 'disegnati con il mouse', 'scritti con il codice e new'], ['Programma finito', 'un .exe che parte ovunque', 'serve Java installato']])]),
('06 Per essere onesti', [
 ('p', 'Anche in Object Pascal le <b>classi</b> più complesse si creano (<b>Create</b>) e poi si liberano (<b>Free</b>). Java invece libera la memoria da solo. E Java è usatissimo nel lavoro: per questo è bene sapere che esiste.'),
 ('code', 'Object Pascal', CP),
 ('nota', 'Per imparare a programmare e vedere subito il risultato, però, Object Pascal con Lazarus è la strada più semplice: meno parole da imparare, finestre con il mouse, un .exe che funziona ovunque.')]),
('07 I due programmi completi, con la finestra e il bottone', [
 ('p', '<b>Lazarus.</b> Tutto questo codice lo scrive Lazarus da solo quando trascini il bottone sul Form. Tu scrivi <b>una riga</b> sola: quella con ShowMessage.'),
 ('code', 'Object Pascal: Unit1.pas', UP),
 ('p', '<b>Java.</b> Qui ogni riga la scrivi tu: la finestra, il bottone, che cosa succede al clic, la grandezza, la chiusura. Ogni oggetto si crea con <b>new</b>.'),
 ('code', 'Java: Ciao.java', JC)]),
('08 Provare Java senza installare niente', [
 ('p', 'A scuola non si installa niente. Ci sono due modi per vedere la finestra di Java.'),
 ('ol', ['<b>Nel browser, con JavaFiddle.</b> Apri l\'indirizzo qui sotto, cancella il codice di esempio, incolla il programma Ciao.java e premi «Run»: la finestra con il bottone si apre dentro la pagina. Funziona solo se il firewall della scuola lascia passare il sito.', '<b>Java portabile, come Godot.</b> Si scarica Java in versione .zip (per esempio «Eclipse Temurin JDK», file zip) e si scompatta in una cartella, per esempio C:\\java\\jdk: niente installazione e niente amministratore. Dalla Java 11 in poi basta un comando per far partire il file Ciao.java, senza compilarlo a parte.']),
 ('p', 'Indirizzo di JavaFiddle, da scrivere così: <b>javafiddle.leaningtech.com</b>'),
 ('code', 'Comando per Java portabile (cartella del file Ciao.java)', JR),
 ('nota', 'Con Lazarus invece il programma diventa un file .exe: lo copi su una chiavetta e parte su qualunque PC Windows, anche senza Lazarus.')]),
('09 Prova tu', [
 ('ol', ['Quante righe servono per Hello World in Object Pascal e quante in Java?', 'In Java, che cosa serve per creare un array di 5 numeri?', 'Perché un programma fatto con Lazarus parte su ogni PC Windows senza installare niente?']),
 ('sol', ['Object Pascal: 1 riga (dentro begin…end). Java: 5 righe con classe e main.', 'La parola new: int[] voti = new int[5];', 'Perché è compilato in un file .exe; Java invece ha bisogno della sua macchina virtuale installata.'])]),
]
