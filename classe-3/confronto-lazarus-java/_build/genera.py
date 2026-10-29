#!/usr/bin/env python3
# 3INF 29/10/2026: percorso guidato «Lazarus e Java a confronto» (CLAUDE.md regola 29).
# Una sola fonte (i PASSI qui sotto) per tre uscite:
#   1. la pagina dei ragazzi docs/3inf-confronto/index.html (passi controllati, «✓ Fatto» con una prova breve che arriva nel riservato,
#      riga in bangla solo per il PC 14, percorso facilitato di 3 passi, riquadro «Come viene valutato», casella dell'assistente);
#   2. il Documento della lezione classe-3/confronto-lazarus-java/AAAAMMGG_Classe-3_vX.Y_Confronto-Lazarus-Java.md (+ .html per il PDF);
#   3. il PDF si fa con: NODE_PATH=$(npm root -g) node classe-3/confronto-lazarus-java/_build/pdf.js
# Uso: python3 classe-3/confronto-lazarus-java/_build/genera.py
import html, json, os, re

VERSIONE = '1.0'
DATA = '20261029'
QUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(QUI, '..', '..', '..'))
CART = os.path.abspath(os.path.join(QUI, '..'))
PAGINA = os.path.join(ROOT, 'docs', '3inf-confronto', 'index.html')
NOME_DOC = DATA + '_Classe-3_v' + VERSIONE + '_Confronto-Lazarus-Java'
CLASSROOM = 'https://classroom.google.com/c/MjUzMjQ1NzQ2NDBa/a/MjU1MTAyOTQzNjBa/details'
GUIDA = '../3inf-eclipse-guida/'

MAIN = '''import javax.swing.*;
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

# Righe della tabella del confronto (sezione 6 del Documento). La prima è l'esempio già scritto e non conta per il voto.
RIGHE = [
    ('Ambiente', 'Lazarus', 'Eclipse', 'Esempio già scritto: copialo così.', 'উদাহরণ: এভাবেই লেখো।'),
    ('Linguaggio', '…', '…', 'Come si chiama la lingua del codice in Lazarus? E in Eclipse?', 'Lazarus-এ কোডের ভাষার নাম কী? আর Eclipse-এ?'),
    ('Dove si scrive il codice', '…', '…', 'In quale file e in quale parte della finestra scrivi le istruzioni?', 'কোন ফাইলে আর জানালার কোন অংশে নির্দেশ লেখো?'),
    ('Come si avvia', '…', '…', 'Quale tasto premi in Lazarus? Quale bottone in Eclipse?', 'Lazarus-এ কোন কী চাপো? Eclipse-এ কোন বোতাম?'),
    ('La finestra e il bottone', '…', '…', 'Come si chiamano in Lazarus? E nel codice Java (guarda le righe con new)?', 'Lazarus-এ এদের নাম কী? আর Java কোডে (new লেখা লাইন দেখো)?'),
    ('Il punto e virgola e le parentesi', '…', '…', 'Dove metti il ; in tutti e due? Che virgolette usa ShowMessage e che virgolette usa Java?', 'দুটোতেই ; কোথায় বসে? ShowMessage কোন উদ্ধৃতিচিহ্ন ব্যবহার করে, আর Java কোনটা?'),
    ('begin…end contro { }', '…', '…', 'Con che cosa apri e chiudi un blocco di istruzioni in Lazarus? E in Java?', 'Lazarus-এ নির্দেশের ব্লক কী দিয়ে খোলো আর বন্ধ করো? আর Java-তে?'),
    ('File del progetto', '…', '…', 'Quali file ha il progetto Lazarus (.lpi .pas .lfm)? E quello Java (.java, e dopo il Run .class)?', 'Lazarus প্রজেক্টে কোন ফাইল থাকে (.lpi .pas .lfm)? আর Java-তে (.java, Run-এর পরে .class)?'),
]

# Ogni passo: titolo, corpo (lista di blocchi), prova. Blocchi: ('p', it, bn) · ('ol', [(it, bn), ...]) · ('box', tipo, it, bn) · ('copia', testo)
# · ('link', testo, href) · ('tabella',) · ('facilitato',) · ('guida',) · ('mappa',). Testi it con un po' di HTML (b, code, kbd).
PASSI = [
    {'parte': 1, 't': 'Dove sei arrivato?', 'tb': 'তুমি কোথায় পৌঁছেছো?',
     'c': [('p', 'Guarda il tuo PC e scegli la frase giusta. Non ci sono risposte sbagliate: serve a sapere da dove ripartire.',
            'তোমার PC দেখো আর ঠিক বাক্যটি বেছে নাও। ভুল উত্তর নেই: কোথা থেকে আবার শুরু করবে তা জানার জন্য।')],
     'prova': {'tipo': 'scelta', 'd': 'Dove sei arrivato con Eclipse?', 'db': 'Eclipse-এ তুমি কোথায় পৌঁছেছো?',
               'scelte': [('Hello World in Eclipse funziona già', 'Eclipse-এ Hello World আগেই চলে'),
                          ('Eclipse si apre, ma il programma non funziona', 'Eclipse খোলে, কিন্তু প্রোগ্রাম চলে না'),
                          ('Non ho ancora scompattato o aperto Eclipse', 'Eclipse এখনো আনজিপ করিনি বা খুলিনি')],
               'giusta': None,
               'dopo': [('Bravo! I passi 2 e 3 li fai in un minuto, poi vai alla parte 2.', 'দারুণ! ২ আর ৩ নম্বর ধাপ এক মিনিটে করো, তারপর ২ নম্বর অংশে যাও।'),
                        ('Al passo 2 apri la guida dal punto giusto: c\'è l\'elenco.', '২ নম্বর ধাপে ঠিক জায়গা থেকে গাইড খোলো: তালিকা আছে।'),
                        ('Al passo 2 fai il percorso facilitato: 3 passi.', '২ নম্বর ধাপে সহজ পথ করো: ৩টি ধাপ।')]}},
    {'parte': 1, 't': 'Eclipse aperto, con Main.java', 'tb': 'Eclipse খোলা, Main.java সহ',
     'c': [('facilitato',), ('guida',)],
     'prova': {'tipo': 'testo', 'd': 'Scrivi il nome della linguetta aperta al centro di Eclipse, sopra il codice.', 'db': 'Eclipse-এর মাঝখানে, কোডের উপরে খোলা ট্যাবের নাম লেখো।',
               'regex': r'main\s*\.?\s*java', 'no': 'Al centro deve esserci la linguetta Main.java: rifai il passo 3 del percorso facilitato.',
               'nob': 'মাঝখানে Main.java ট্যাব থাকতে হবে: সহজ পথের ৩ নম্বর ধাপ আবার করো।'}},
    {'parte': 1, 't': 'Run: la finestrella Hello World', 'tb': 'Run: Hello World ছোট জানালা',
     'c': [('ol', [('In alto clicca il <b>cerchio verde con il triangolo bianco</b>: è «Run» (Esegui), come F9 in Lazarus.', 'উপরে সাদা ত্রিভুজসহ সবুজ বৃত্তে ক্লিক করো: এটা Run, Lazarus-এর F9-এর মতো।'),
                   ('Si apre la finestra con il bottone <b>Premi</b>: cliccalo.', 'Premi বোতামসহ জানালা খোলে: সেটাতে ক্লিক করো।')]),
           ('box', 'nota', 'Non vedi la finestra? È dietro Eclipse: cercala nella barra in basso dello schermo.', 'জানালা দেখছো না? এটা Eclipse-এর পিছনে: স্ক্রিনের নিচের বারে খোঁজো।')],
     'prova': {'tipo': 'testo', 'd': 'Che cosa c\'è scritto nella finestrella che si apre?', 'db': 'যে ছোট জানালা খোলে তাতে কী লেখা আছে?', 'min': 1,
               'fatto': ('FATTO! Il tuo primo programma Java con la finestra. Mostralo al compagno. Vuoi farlo tuo? Cambia "Hello World" con una frase tua (guida, passo 23).',
                         'হয়ে গেছে! জানালাসহ তোমার প্রথম Java প্রোগ্রাম। সহপাঠীকে দেখাও।')}},
    {'parte': 2, 't': 'Apri il tuo Documento', 'tb': 'তোমার ডকুমেন্ট খোলো',
     'c': [('ol', [('Clicca il bottone qui sotto: si apre il compito su Classroom «Hello World in Lazarus e in Java».', 'নিচের বোতামে ক্লিক করো: Classroom-এ «Hello World in Lazarus e in Java» কাজটি খোলে।'),
                   ('A destra, nel riquadro «Il tuo lavoro», clicca il Documento con il tuo nome.', 'ডানদিকে «Il tuo lavoro» ঘরে তোমার নামের ডকুমেন্টে ক্লিক করো।')]),
           ('link', 'Apri il compito su Classroom', CLASSROOM),
           ('box', 'nota', 'Hai già consegnato ieri? In alto a destra clicca «Annulla consegna»: così puoi modificare il Documento. Alla fine lo consegni di nuovo (passo 10).',
            'গতকাল জমা দিয়েছো? উপরে ডানদিকে «Annulla consegna» ক্লিক করো: তাহলে ডকুমেন্ট বদলাতে পারবে। শেষে আবার জমা দেবে (১০ নম্বর ধাপ)।'),
           ('mappa',)],
     'prova': {'tipo': 'scelta', 'd': 'Come si chiama la sezione 2 del tuo Documento?', 'db': 'তোমার ডকুমেন্টের ২ নম্বর অংশের নাম কী?',
               'scelte': [('Il mio codice Java', ''), ('Il mio programma Lazarus che funziona (screenshot)', ''), ('Con parole mie', '')], 'giusta': 1,
               'no': 'Guarda bene il titolo con il numero 2 nel tuo Documento.', 'nob': 'ডকুমেন্টে ২ নম্বর শিরোনামটি ভালো করে দেখো।'}},
    {'parte': 2, 't': 'Sezione 2: lo screenshot di Lazarus', 'tb': '২ নম্বর অংশ: Lazarus-এর স্ক্রিনশট',
     'c': [('ol', [('Apri Lazarus e il tuo progetto di ieri. Premi <kbd>F9</kbd> e poi il bottone: compare il saluto.', 'Lazarus আর গতকালের প্রজেক্ট খোলো। F9 চাপো, তারপর বোতাম: শুভেচ্ছা দেখা যায়।'),
                   ('Premi <kbd>Windows</kbd> + <kbd>Maiusc</kbd> + <kbd>S</kbd> e trascina il mouse sopra la finestra del programma.', 'Windows + Shift + S চাপো আর প্রোগ্রামের জানালার উপর মাউস টেনে নাও।'),
                   ('Nel Documento clicca nella riga vuota sotto il titolo «2.» e premi <kbd>Ctrl</kbd> + <kbd>V</kbd>.', 'ডকুমেন্টে «2.» শিরোনামের নিচের খালি লাইনে ক্লিক করো, Ctrl + V চাপো।')]),
           ('box', 'nota', 'Non trovi il progetto di ieri? Fanne uno nuovo: «File», «Nuovo», «Applicazione»; metti un bottone; doppio clic sul bottone; scrivi <code>ShowMessage(\'Hello World\');</code> e premi <kbd>F9</kbd>.',
            'গতকালের প্রজেক্ট পাচ্ছো না? নতুন বানাও: File, Nuovo, Applicazione; একটি বোতাম রাখো; বোতামে দুবার ক্লিক; ShowMessage(\'Hello World\'); লেখো আর F9 চাপো।')],
     'prova': {'tipo': 'testo', 'd': 'Che cosa scrive il tuo programma Lazarus quando premi il bottone?', 'db': 'বোতাম চাপলে তোমার Lazarus প্রোগ্রাম কী লেখে?', 'min': 1}},
    {'parte': 2, 't': 'Sezione 4: lo screenshot di Eclipse', 'tb': '৪ নম্বর অংশ: Eclipse-এর স্ক্রিনশট',
     'c': [('ol', [('Torna in Eclipse, premi Run e poi il bottone <b>Premi</b>: si apre la finestrella Hello World.', 'Eclipse-এ ফিরে যাও, Run চাপো, তারপর Premi বোতাম: Hello World ছোট জানালা খোলে।'),
                   ('Premi <kbd>Windows</kbd> + <kbd>Maiusc</kbd> + <kbd>S</kbd> e prendi la finestra con la finestrella.', 'Windows + Shift + S চাপো আর ছোট জানালাসহ জানালাটি নাও।'),
                   ('Nel Documento clicca nella riga vuota sotto il titolo «4.» e premi <kbd>Ctrl</kbd> + <kbd>V</kbd>.', 'ডকুমেন্টে «4.» শিরোনামের নিচের খালি লাইনে ক্লিক করো, Ctrl + V চাপো।')])],
     'prova': {'tipo': 'numero', 'd': 'Quante immagini ci sono adesso nel tuo Documento? Scrivi il numero.', 'db': 'এখন তোমার ডকুমেন্টে কতগুলো ছবি আছে? সংখ্যা লেখো।', 'minimo': 2,
               'no': 'Servono due screenshot: Lazarus nella sezione 2 ed Eclipse nella sezione 4.', 'nob': 'দুটি স্ক্রিনশট দরকার: ২ নম্বর অংশে Lazarus আর ৪ নম্বর অংশে Eclipse।'}},
    {'parte': 2, 't': 'Sezione 6: la tabella, prima metà', 'tb': '৬ নম্বর অংশ: টেবিল, প্রথম অর্ধেক',
     'c': [('ol', [('Nel Documento premi <kbd>Ctrl</kbd> + <kbd>Fine</kbd>: vai in fondo.', 'ডকুমেন্টে Ctrl + End চাপো: একদম নিচে যাও।'),
                   ('Scrivi il titolo:', 'শিরোনাম লেখো:')]),
           ('copia', '6. Lazarus e Java a confronto'),
           ('p', 'Sotto, scrivi la riga di esempio:', 'নিচে উদাহরণের লাইনটি লেখো:'),
           ('copia', 'Ambiente: Lazarus - Eclipse'),
           ('p', 'Poi scrivi le righe da 2 a 5 della tabella qui sotto, <b>una per riga, con parole tue</b>: il nome della riga, i due punti, Lazarus, un trattino, Java. La domanda accanto ti aiuta.',
            'তারপর নিচের টেবিলের ২ থেকে ৫ নম্বর লাইন লেখো, প্রতি লাইনে একটি, নিজের ভাষায়: লাইনের নাম, দুই বিন্দু, Lazarus, একটি ড্যাশ, Java। পাশের প্রশ্ন তোমাকে সাহায্য করবে।'),
           ('tabella', 0, 5)],
     'prova': {'tipo': 'riga', 'd': 'Scrivi qui la tua riga «Come si avvia», uguale a quella del Documento.', 'db': 'তোমার «Come si avvia» লাইনটি এখানে লেখো, ডকুমেন্টের মতোই।', 'min': 3}},
    {'parte': 2, 't': 'Sezione 6: la tabella, seconda metà', 'tb': '৬ নম্বর অংশ: টেবিল, দ্বিতীয় অর্ধেক',
     'c': [('p', 'Sotto le righe di prima scrivi le righe da 6 a 8, sempre una per riga e con parole tue.', 'আগের লাইনের নিচে ৬ থেকে ৮ নম্বর লাইন লেখো, প্রতি লাইনে একটি, নিজের ভাষায়।'),
           ('tabella', 5, 8),
           ('box', 'nota', 'Le righe vuote, copiate dall\'esempio o senza senso non contano per il voto.', 'খালি, উদাহরণ থেকে কপি করা বা অর্থহীন লাইন নম্বর পায় না।')],
     'prova': {'tipo': 'riga', 'd': 'Scrivi qui la tua riga «File del progetto», uguale a quella del Documento.', 'db': 'তোমার «File del progetto» লাইনটি এখানে লেখো, ডকুমেন্টের মতোই।', 'min': 3}},
    {'parte': 2, 't': 'Sezione 7: in 3 frasi', 'tb': '৭ নম্বর অংশ: ৩টি বাক্যে',
     'c': [('ol', [('Sotto la tabella scrivi il titolo:', 'টেবিলের নিচে শিরোনাম লেখো:')]),
           ('copia', '7. In 3 frasi: che cosa cambia e che cosa resta uguale'),
           ('p', 'Poi scrivi 3 frasi tue, una per riga. Puoi cominciare così:', 'তারপর নিজের ৩টি বাক্য লেখো, প্রতি লাইনে একটি। এভাবে শুরু করতে পারো:'),
           ('ol', [('In tutti e due i programmi resta uguale che …', 'দুটো প্রোগ্রামেই একই থাকে যে …'),
                   ('In Java invece cambia che …', 'Java-তে কিন্তু বদলায় যে …'),
                   ('Secondo me il più facile è … perché …', 'আমার মতে সবচেয়ে সহজ … কারণ …')])],
     'prova': {'tipo': 'testo', 'd': 'Scrivi qui la tua prima frase, uguale a quella del Documento.', 'db': 'তোমার প্রথম বাক্যটি এখানে লেখো, ডকুমেন্টের মতোই।', 'min': 6}},
    {'parte': 2, 't': 'Consegna su Classroom', 'tb': 'Classroom-এ জমা দাও',
     'c': [('ol', [('Torna nella scheda di Classroom del compito.', 'কাজের Classroom ট্যাবে ফিরে যাও।'),
                   ('In alto a destra clicca il bottone blu <b>«Consegna»</b>, poi ancora «Consegna» nella finestrella.', 'উপরে ডানদিকে নীল «Consegna» বোতামে ক্লিক করো, তারপর ছোট জানালায় আবার «Consegna»।')]),
           ('box', 'nota', 'Entro le 13:00. Dopo le 13 il Documento si valuta lo stesso, ma il ritardo viene segnato.', '১৩:০০-র মধ্যে। ১৩টার পরে ডকুমেন্ট মূল্যায়ন হয়, কিন্তু দেরি লেখা থাকে।')],
     'prova': {'tipo': 'scelta', 'd': 'Che cosa c\'è scritto adesso sul bottone in alto a destra?', 'db': 'এখন উপরে ডানদিকের বোতামে কী লেখা আছে?',
               'scelte': [('Consegna', ''), ('Annulla consegna', ''), ('Aggiungi o crea', '')], 'giusta': 1,
               'no': 'Non hai ancora consegnato: clicca «Consegna» in alto a destra.', 'nob': 'এখনো জমা দাওনি: উপরে ডানদিকে «Consegna» ক্লিক করো।',
               'fatto': ('HAI FINITO! Il voto provvisorio lo vedi in «La mia giornata della 3INF» (decide il prof). Hai tempo? Fai la finestra Java che saluta il tuo nome (lezione Java, scheda 11).',
                         'তুমি শেষ করেছো! অস্থায়ী নম্বর «La mia giornata»-তে দেখো (প্রফেসর ঠিক করবেন)।')}},
]

FACILITATO = [
    ('Scompatta lo ZIP in una cartella corta', 'ছোট নামের ফোল্ডারে ZIP আনজিপ করো',
     'Fai clic destro sul file <b>eclipse-java-2026-09-R-win32-x86_64.zip</b> e scegli «Estrai tutto…». Nella casella del percorso premi <kbd>Ctrl</kbd> + <kbd>A</kbd>, scrivi il percorso qui sotto, clicca «Estrai» e aspetta che la finestra si chiuda da sola.',
     'ZIP ফাইলে ডান ক্লিক করে «Estrai tutto…» বেছে নাও। পথের ঘরে Ctrl + A চাপো, নিচের পথটি লেখো, «Estrai» ক্লিক করো আর জানালা নিজে বন্ধ হওয়া পর্যন্ত অপেক্ষা করো।',
     'C:\\Users\\Public\\ec'),
    ('Apri Eclipse e crea il progetto', 'Eclipse খোলো আর প্রজেক্ট বানাও',
     'Apri la cartella <b>C:\\Users\\Public\\ec\\eclipse</b> e fai doppio clic su <b>eclipse.exe</b>. Clicca «Launch», poi «Later». A sinistra clicca «Create a Java project», scrivi il nome qui sotto, togli la spunta «Create module-info.java» e clicca «Finish».',
     'C:\\Users\\Public\\ec\\eclipse ফোল্ডার খোলো, eclipse.exe-তে দুবার ক্লিক করো। «Launch», তারপর «Later» ক্লিক করো। বামে «Create a Java project» ক্লিক করো, নিচের নামটি লেখো, «Create module-info.java»-র টিক তুলে দাও আর «Finish» ক্লিক করো।',
     'HelloWorld'),
    ('Incolla la classe Main e premi Run', 'Main ক্লাস পেস্ট করো আর Run চাপো',
     'Clicca «Copia» sul codice qui sotto. A sinistra apri <b>HelloWorld</b> e clicca una volta su <b>src</b>. Premi <kbd>Ctrl</kbd> + <kbd>V</kbd>: Eclipse crea da solo <b>Main.java</b>. Poi in alto clicca il cerchio verde (Run).',
     'নিচের কোডে «Copia» ক্লিক করো। বামে HelloWorld খোলো, src-এ একবার ক্লিক করো। Ctrl + V চাপো: Eclipse নিজেই Main.java বানায়। তারপর উপরে সবুজ বৃত্তে (Run) ক্লিক করো।',
     MAIN),
]
GUIDA_PUNTI = [
    ('Eclipse non si apre o dà un errore', 'Eclipse খোলে না বা ভুল দেখায়', 'passo-1', 'passi 1-6'),
    ('Eclipse è aperto ma non c\'è il progetto HelloWorld', 'Eclipse খোলা, কিন্তু HelloWorld প্রজেক্ট নেই', 'passo-9', 'passi 9-12'),
    ('C\'è il progetto ma non c\'è Main.java', 'প্রজেক্ট আছে, কিন্তু Main.java নেই', 'passo-13', 'passi 13-17'),
    ('Main.java c\'è, ma il codice è vecchio o ha la X rossa', 'Main.java আছে, কিন্তু কোড পুরনো বা লাল X আছে', 'passo-18', 'passi 18-22, poi «Errori comuni» in fondo'),
]
VALUTAZIONE = [
    ('+10 lo screenshot di Hello World in Lazarus (sezione 2)', '+১০ Lazarus-এ Hello World-এর স্ক্রিনশট (২ নম্বর অংশ)'),
    ('+10 lo screenshot di Hello World in Eclipse/Java (sezione 4)', '+১০ Eclipse/Java-তে Hello World-এর স্ক্রিনশট (৪ নম্বর অংশ)'),
    ('+10 la tabella del confronto completa (sezione 6): righe scritte con parole tue, non copiate dall\'esempio', '+১০ সম্পূর্ণ তুলনার টেবিল (৬ নম্বর অংশ): নিজের ভাষায় লেখা লাইন, উদাহরণ থেকে কপি নয়'),
    ('+10 le 3 frasi finali (sezione 7)', '+১০ শেষের ৩টি বাক্য (৭ নম্বর অংশ)'),
]
MAPPA = [
    ('1', 'Il mio codice Lazarus', 'di ieri'), ('2', 'Il mio programma Lazarus che funziona (screenshot)', 'oggi: +10'),
    ('3', 'Il mio codice Java', 'di ieri'), ('4', 'Il mio programma Java che funziona (screenshot)', 'oggi: +10, lo screenshot di Eclipse'),
    ('5', 'Con parole mie', 'di ieri'), ('6', 'Lazarus e Java a confronto (la tabella)', 'nuova: +10'), ('7', 'In 3 frasi: che cosa cambia e che cosa resta uguale', 'nuova: +10'),
]

E = html.escape


def bn(t, tag='p'):
    return '<%s class="bn" lang="bn">%s</%s>' % (tag, E(t), tag) if t else ''


def copia_html(t):
    return '<div class="copia"><pre>%s</pre><button class="bt-copia" type="button" onclick="copia(this)">Copia</button></div>' % E(t)


def tabella_html(a, b):
    h = '<div class="tab"><table><thead><tr><th>#</th><th>Riga</th><th>Lazarus</th><th>Java</th><th>Domanda che ti aiuta</th></tr></thead><tbody>'
    for i in range(a, b):
        r = RIGHE[i]
        es = ' class="es"' if i == 0 else ''
        h += '<tr%s><td>%d</td><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s%s</td></tr>' % (es, i + 1, E(r[0]), E(r[1]), E(r[2]), E(r[3]), bn(r[4], 'span'))
    return h + '</tbody></table></div>'


def blocco_html(b):
    k = b[0]
    if k == 'p':
        return '<p>%s</p>%s' % (b[1], bn(b[2]))
    if k == 'ol':
        return '<ol>' + ''.join('<li>%s%s</li>' % (it, bn(t)) for it, t in b[1]) + '</ol>'
    if k == 'box':
        return '<div class="box %s"><p>%s</p>%s</div>' % (b[1], b[2], bn(b[3]))
    if k == 'copia':
        return copia_html(b[1])
    if k == 'link':
        return '<p><a class="bt bt-cl" href="%s" target="_blank" rel="noopener">%s</a></p>' % (E(b[2]), E(b[1]))
    if k == 'tabella':
        return tabella_html(b[1], b[2])
    if k == 'mappa':
        h = '<p>Il tuo Documento, alla fine, ha queste sezioni:</p>%s<div class="tab"><table><thead><tr><th>Sezione</th><th>Titolo</th><th>Che cosa fai</th></tr></thead><tbody>' % bn('শেষে তোমার ডকুমেন্টে এই অংশগুলো থাকবে:')
        for n, t, c in MAPPA:
            h += '<tr%s><td>%s</td><td>%s</td><td>%s</td></tr>' % (' class="nuova"' if 'oggi' in c or 'nuova' in c else '', n, E(t), E(c))
        return h + '</tbody></table></div>'
    if k == 'facilitato':
        h = '<details class="facile" id="facile"><summary><b>Percorso facilitato: 3 passi</b> (per chi deve ancora scompattare o aprire Eclipse)%s</summary><ol class="fac">' % bn('সহজ পথ: ৩টি ধাপ', 'span')
        for t, tb, it, itb, cp in FACILITATO:
            h += '<li><b>%s</b>%s<p>%s</p>%s%s</li>' % (E(t), bn(tb, 'span'), it, bn(itb), copia_html(cp))
        return h + '</ol></details>'
    if k == 'guida':
        h = '<div class="box guida"><p><b>Eclipse è già aperto?</b> Riparti dalla guida passo passo, dal punto in cui sei:</p>%s<ol>' % bn('Eclipse আগেই খোলা? যেখানে আছো সেখান থেকে গাইড আবার শুরু করো:')
        for t, tb, anc, q in GUIDA_PUNTI:
            h += '<li>%s: <a href="%s#%s" target="_blank" rel="noopener">guida, %s</a>%s</li>' % (E(t), GUIDA, anc, E(q), bn(tb, 'span'))
        return h + '</ol></div>'
    raise ValueError(k)


def prova_html(i, p):
    pr = p['prova']
    h = '<div class="prova"><p class="dom"><b>Prova:</b> %s</p>%s' % (E(pr['d']), bn(pr['db']))
    if pr['tipo'] == 'scelta':
        h += '<div class="scelte">' + ''.join('<label><input type="radio" name="s%d" value="%d"> %s%s</label>' % (i, k, E(s[0]), bn(s[1], 'span')) for k, s in enumerate(pr['scelte'])) + '</div>'
    elif pr['tipo'] == 'numero':
        h += '<input class="risp" type="number" min="0" max="20" inputmode="numeric" placeholder="numero">'
    else:
        h += '<input class="risp" type="text" maxlength="300" placeholder="scrivi qui">'
    h += '<div class="riga-bt"><button class="fatto" type="button" data-i="%d">✓ Fatto</button><span class="esito" aria-live="polite"></span></div></div>' % i
    return h


def pagina():
    parti = {1: ('Parte 1 · Finisci Hello World in Eclipse', 'অংশ ১ · Eclipse-এ Hello World শেষ করো',
                 'Ognuno riparte dal punto in cui è arrivato ieri. Prima vittoria, entro 10 minuti: la finestrella Hello World di Java.',
                 'সবাই গতকাল যেখানে থেমেছিল সেখান থেকে শুরু করে। প্রথম জয়, ১০ মিনিটের মধ্যে: Java-র Hello World ছোট জানালা।'),
             2: ('Parte 2 · Il Documento del confronto', 'অংশ ২ · তুলনার ডকুমেন্ট',
                 'Usi il Documento del compito di ieri «Hello World in Lazarus e in Java». Oggi completi le sezioni 2 e 4 e aggiungi in fondo la 6 e la 7.',
                 'গতকালের «Hello World in Lazarus e in Java» কাজের ডকুমেন্টই ব্যবহার করো। আজ ২ আর ৪ নম্বর অংশ শেষ করো, নিচে ৬ আর ৭ যোগ করো।')}
    corpo, ultima = '', 0
    for i, p in enumerate(PASSI):
        if p['parte'] != ultima:
            ultima = p['parte']; t, tb, it, itb = parti[ultima]
            corpo += '<h2>%s%s</h2><p>%s</p>%s' % (E(t), bn(tb, 'span'), E(it), bn(itb))
        corpo += '<section class="passo" id="p%d"><div class="testa"><span class="num">%d</span><h3>%s%s</h3><span class="stato"></span></div>' % (i + 1, i + 1, E(p['t']), bn(p['tb'], 'span'))
        corpo += ''.join(blocco_html(b) for b in p['c']) + prova_html(i, p) + '</section>'
    val = '<ol>' + ''.join('<li>%s%s</li>' % (E(a), bn(b, 'span')) for a, b in VALUTAZIONE) + '</ol>'
    dati = {'id': '3inf-confronto', 'totale': len(PASSI), 'versione': VERSIONE,
            'passi': [{'t': p['t'], 'prova': {k: v for k, v in p['prova'].items() if k not in ('d', 'db')}} for p in PASSI],
            'esempio': 'Ambiente: Lazarus - Eclipse', 'righe': [r[0] for r in RIGHE]}
    T = open(os.path.join(QUI, 'pagina.html'), encoding='utf-8').read()
    out = (T.replace('{{VALUTAZIONE}}', val).replace('{{PASSI}}', corpo).replace('{{VERSIONE}}', VERSIONE)
            .replace('{{DATI}}', json.dumps(dati, ensure_ascii=False)).replace('{{TOTALE}}', str(len(PASSI))))
    open(PAGINA, 'w', encoding='utf-8').write(out)
    return out


def senza_tag(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))


def documento():
    L = ['# Lazarus e Java a confronto', '',
         '**Versione %s** — 29/10/2026 — Classe 3 (3INF), Laboratorio professionale, ore 11-13 — percorso guidato per gli allievi' % VERSIONE, '',
         'Pagina per i ragazzi (indirizzo fisso): `https://nicolaregge-pulse.github.io/corso-informatica/3inf-confronto/` (con `?pc=14` compare la riga in bangla).', '',
         '## 00 Che cosa si fa oggi', '',
         '1. Parte 1: si finisce Hello World in Eclipse, ognuno dal punto in cui è arrivato il 28/10 (passi 1-3; percorso facilitato di 3 passi per chi deve ancora scompattare o aprire Eclipse).',
         '2. Parte 2: si completa il Documento del compito di ieri su Classroom «Hello World in Lazarus e in Java» (sezioni 2 e 4) e si aggiungono la tabella del confronto (sezione 6) e 3 frasi (sezione 7) (passi 4-10).',
         '3. Ogni passo si chiude con «✓ Fatto» e una prova breve, che arriva al prof (riservato `dati/verifiche/3inf-confronto/arrivi/`): il cruscotto sa a che passo è ognuno.',
         '4. Consegna su Classroom entro le 13:00.', '',
         '## 01 Come viene valutato', '',
         'Il Documento del confronto viene valutato. Il voto parte da 40 (massimo 80):', '']
    L += ['%d. %s' % (k + 1, a) for k, (a, _) in enumerate(VALUTAZIONE)]
    L += ['5. Consegnato entro le 13:00; dopo le 13 si valuta lo stesso, ma il ritardo viene segnato.', '',
          '> [GIALLO] Protezione dagli abusi: righe vuote, copiate dall\'esempio o testo senza senso non contano; gli screenshot si contano solo nel PDF della consegna vera. Il voto del cruscotto è provvisorio: decide il prof.', '',
          '## 02 Il Documento alla fine', '']
    L += ['%s. %s — %s' % (n, t, c) for n, t, c in MAPPA]
    L += ['', '## 03 La tabella del confronto (sezione 6)', '', '| # | Riga | Lazarus | Java | Domanda che aiuta |', '|---|---|---|---|---|']
    L += ['| %d | %s | %s | %s | %s |' % (i + 1, r[0], r[1], r[2], r[3]) for i, r in enumerate(RIGHE)]
    L += ['', 'La riga 1 è l\'esempio già scritto: non conta per il voto.', '', '## 04 I passi', '']
    for i, p in enumerate(PASSI):
        L += ['### Passo %d · %s' % (i + 1, p['t']), '']
        n = 0
        for b in p['c']:
            if b[0] == 'p': L += [senza_tag(b[1]), '']
            elif b[0] == 'ol':
                L += ['%d. %s' % (k + 1, senza_tag(x)) for k, (x, _) in enumerate(b[1])] + ['']
            elif b[0] == 'box': L += ['> [GIALLO] ' + senza_tag(b[2]), '']
            elif b[0] == 'copia': L += ['```', b[1], '```', '']
            elif b[0] == 'link': L += ['Link: %s' % b[2], '']
            elif b[0] == 'tabella': L += ['Righe %d-%d della tabella (sezione 03).' % (b[1] + 1, b[2]), '']
            elif b[0] == 'mappa': L += ['Le sezioni del Documento sono nella sezione 02.', '']
            elif b[0] == 'facilitato':
                L += ['Percorso facilitato (3 passi):', '']
                for k, (t, _, it, _, cp) in enumerate(FACILITATO):
                    L += ['%d. **%s.** %s' % (k + 1, t, senza_tag(it)), '', '```', cp, '```', '']
            elif b[0] == 'guida':
                L += ['Chi ha già Eclipse aperto riparte dalla guida `docs/3inf-eclipse-guida/`:', '']
                L += ['%d. %s: guida, %s' % (k + 1, t, q) for k, (t, _, _, q) in enumerate(GUIDA_PUNTI)] + ['']
        pr = p['prova']
        q = 'Prova: ' + pr['d']
        if pr['tipo'] == 'scelta':
            q += ' Scelte: ' + ' · '.join(s[0] for s in pr['scelte']) + ('' if pr['giusta'] is None else ' (giusta: «%s»)' % pr['scelte'][pr['giusta']][0])
        L += [q, '']
    L += ['## 05 Per il docente: che cosa vede il cruscotto', '',
          '1. Colonna Percorso: passo raggiunto (1-10) e da quanti minuti il ragazzo è fermo.',
          '2. Colonna Documento: consegnato sì/no e a che ora; sezioni compilate (lette dal Documento); dopo la consegna le immagini contate dal PDF.',
          '3. Voto 40-80 con il conto, provvisorio: decide il prof. Tutti i presenti.', '',
          '## Changelog', '', '1. v1.0 (29/10/2026): prima versione.', '']
    md = '\n'.join(L)
    open(os.path.join(CART, NOME_DOC + '.md'), 'w', encoding='utf-8').write(md)
    # HTML per il PDF: la pagina stessa, con tutte le righe in bangla, i dettagli aperti e senza la parte interattiva
    T = open(PAGINA, encoding='utf-8').read()
    T = T.replace('<details class="facile" id="facile">', '<details class="facile" id="facile" open>').replace('<body>', '<body class="stampa bn-on">', 1)
    open(os.path.join(CART, NOME_DOC + '.html'), 'w', encoding='utf-8').write(T)


if __name__ == '__main__':
    pagina(); documento()
    print('ok', PAGINA, NOME_DOC)
