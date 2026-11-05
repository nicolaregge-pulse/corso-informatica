#!/usr/bin/env python3
"""Genera la lezione «smonta, rimonta, installa» del PC (percorso a passi, R9) per una classe.

Uso:  python3 strumenti/genera_lezione_pc.py 2INF     -> docs/anteprima/2inf-pc-05-11/
      python3 strumenti/genera_lezione_pc.py 3INF     -> docs/anteprima/3inf-pc-05-11/
Scrive: index.html, ora1.html, ora2.html (ora3.html), impostazioni-base.html, lezione.js, ore.js, config.json, img/*.svg.
Le pagine sono uguali per tutte le classi: cambiano solo SPEC (ore, blocchi) e le lingue
(2INF solo italiano, passa da solo_italiano.py; 3INF italiano + riga in bangla visibile solo con ?pc=14).
config.json (il docente cambia SOLO questo, poi push):
  ore_sbloccate  0 = tutto chiuso; si alza di UNA ora con PUBB n (strumenti/sblocca_ora.py <cartella> n)
  variante_os    "A" = Windows 10 da chiavetta USB (deciso dal docente il 04/11/2026), "B" = Linux Mint da chiavetta
  pc_da_smontare, persone_per_pc (2 = coppie; 3 = gruppi da tre). Niente ruoli (docente, 05/11/2026)
  rete           prefisso, primo, maschera, gateway, dns  (IP del banco N = prefisso + (primo + N))
  quiz_pc        indirizzo viewform del Modulo (vuoto finché il quiz non è creato con PUBB)
Il config.json esistente NON si sovrascrive (si aggiungono solo le chiavi mancanti): ore_sbloccate resta quello che è.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_svg_pc as S  # noqa: E402

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PONTE = 'https://script.google.com/macros/s/AKfycbzJ-4JRlTsSRSL77wXNG6ysffGURuDwyFVLin681obuwaw51a5Iso9KHqlUVLcig4_m/exec'
SITO = 'https://nicolaregge-pulse.github.io/corso-informatica/'
RETE = {'prefisso': '192.168.10.', 'primo': 10, 'maschera': '255.255.255.0', 'gateway': '192.168.10.1', 'dns': '192.168.10.1'}

# ------------------------------------------------------------------ le classi
SPEC = {
    '2INF': {
        'cartella': '2inf-pc-05-11', 'k': '2inf', 'bn': False, 'data': '05/11/2026', 'giorno': 'giovedì',
        'materia': 'Laboratorio professionale', 'cruscotto': '../../2inf/', 'monitor': '../../2inf-monitor/',
        'ore': [
            {'n': 1, 'file': 'ora1.html', 'orario': '8-9', 'titolo': 'Ora 1 · Sicurezza e smontaggio del PC',
             'blocchi': ['ruoli', 'sicurezza', 'apri', 'riconosci', 'smonta', 'scheda1'], 'fasi': [0]},
            {'n': 2, 'file': 'ora2.html', 'orario': '9-10', 'titolo': 'Ora 2 · Rimontaggio, accensione e BIOS',
             'blocchi': ['rimonta', 'bios', 'scheda2'], 'fasi': [1, 2]},
            {'n': 3, 'file': 'ora3.html', 'orario': '10-11', 'titolo': 'Ora 3 · Windows 10, utenti e rete',
             'blocchi': ['installa', 'quiz', 'primo_avvio', 'utenti', 'strumenti', 'rete', 'base_link', 'scheda3'], 'fasi': [3, 4]},
        ],
        'base_ora': 3, 'guasti': True,
    },
    '3INF': {
        'cartella': '3inf-pc-05-11', 'k': '3inf', 'bn': True, 'data': '05/11/2026', 'giorno': 'giovedì',
        'materia': 'Laboratorio', 'cruscotto': '../../3inf/', 'monitor': '../../3inf-monitor/',
        'ore': [
            {'n': 1, 'file': 'ora1.html', 'orario': '11-12', 'titolo': 'Ora 1 · Impostazioni di base, sicurezza e smontaggio',
             'blocchi': ['base_link', 'ruoli', 'sicurezza', 'apri', 'riconosci', 'smonta', 'scheda1'], 'fasi': [0]},
            {'n': 2, 'file': 'ora2.html', 'orario': '12-13', 'titolo': 'Ora 2 · Rimontaggio, BIOS e quiz',
             'blocchi': ['rimonta', 'bios', 'quiz', 'scheda2'], 'fasi': [1, 2]},
            {'n': 2, 'extra': True, 'file': 'ora3.html', 'orario': 'se avanza tempo',
             'titolo': 'Se avanza tempo · Windows 10, utenti e rete',
             'blocchi': ['installa', 'primo_avvio', 'utenti', 'strumenti', 'rete', 'scheda3'], 'fasi': [3, 4]},
        ],
        'base_ora': 1,
    },
}

FASI = ['Smontaggio', 'Rimontaggio', 'Accensione e BIOS', 'Installazione', 'Utenti e rete']
FASI_BN = ['খোলা', 'আবার জোড়া', 'চালু করা ও BIOS', 'ইনস্টল', 'ইউজার ও নেটওয়ার্ক']

# ------------------------------------------------------------------ i passi
# ogni passo: id, titolo, testo (HTML, frasi corte), img (nome del file in img/), bn (una riga in bangla), os ('A', 'B' o None)
P = {}


def passo(blocco, id, titolo, testo, img, bn, os_=None, extra=''):
    P.setdefault(blocco, []).append({'id': id, 'titolo': titolo, 'testo': testo, 'img': img, 'bn': bn, 'os': os_, 'extra': extra})


# 05/11/2026 (docente, in aula): si smontano e rimontano SOLO RAM e disco; CPU e ventola (dissipatore) si riconoscono e non si toccano.
NON_SI_TOCCA = ('<div class="aiutoprof" style="background:#fde8e8;border:3px solid #c0392b;border-radius:12px;padding:8px 12px;margin:8px 0;color:#000">'
                '<b>NON SI TOCCA: CPU e ventola (dissipatore).</b> Si guardano e si riconoscono (lettera A), ma non si toccano. '
                'Disco e lettore DVD restano nel loro rack: si staccano solo i loro cavi.</div>')

# --- ora 1: ruoli, sicurezza, componenti, smontaggio
passo('ruoli', 'ruoli', 'Vinci subito: scrivete i nomi e il banco',
      'Si lavora a coppie, un PC per coppia. Scrivete i vostri nomi nel riquadro «Chi siete?» e scegliete il numero del banco.',
      'ruoli.svg', 'জোড়ায় কাজ করো, প্রতি জোড়ায় একটা PC। নাম লেখো, বেঞ্চের নম্বর বেছে নাও।')
passo('sicurezza', 'spina', 'Spegni il PC e togli la spina',
      'Spegni il PC del banco. Togli la spina dalla presa della corrente. Solo dopo si apre il case.',
      'spina.svg', 'PC বন্ধ করো আর প্লাগ খুলে ফেলো। তারপরই কেস খোলো।')
passo('sicurezza', 'esd', 'Scarica l\'elettricità statica',
      'Tocca con la mano il metallo del case. Se c\'è il braccialetto antistatico, mettilo e attacca la pinza al metallo del case. Così non rompi la RAM.',
      'esd.svg', 'কেসের ধাতু হাত দিয়ে ছোঁও (অথবা অ্যান্টিস্ট্যাটিক ব্রেসলেট পরো)। এতে RAM নষ্ট হয় না।')
passo('sicurezza', 'piano', 'Prepara il tavolo',
      'Liberate il tavolo vicino al PC: qui metterete la RAM quando la togliete. Non servono attrezzi: i PC sono senza viti.',
      'tavolo.svg', 'PC-র পাশের টেবিল খালি করো। কোনো যন্ত্র লাগবে না: PC-তে স্ক্রু নেই।')
passo('apri', 'apri', 'Apri il case',
      'Gira il PC. Dietro, tira la leva (o premi il gancio) del pannello laterale. Fai scorrere il pannello verso il retro e appoggialo sul tavolo.',
      'apri-case.svg', 'PC ঘোরাও। পেছনে প্যানেলের লিভার টানো (বা হুক চাপো), প্যানেল পেছনের দিকে সরিয়ে খুলে ফেলো।')
passo('riconosci', 'riconosci', 'Riconosci i componenti',
      'Guarda lo schema: ci sono 8 lettere, da A a H. Nella <b>scheda</b> in fondo alla pagina scegli il nome di ogni lettera. Poi cercate ogni pezzo dentro il vostro PC e indicatelo con il dito.',
      'componenti.svg', 'ছবিতে A থেকে H পর্যন্ত ৮টি অক্ষর আছে। নিচের ফর্মে প্রতিটি অক্ষরের নাম বেছে নাও। তারপর আসল PC-তে টুকরোটা খুঁজে আঙুল দিয়ে দেখাও।',
      extra=NON_SI_TOCCA)
passo('riconosci', 'mappa', 'Segna la mappa dei cavi',
      'Prima di staccare un cavo, guardate dove è attaccato e spuntate il cavo nella <b>mappa dei cavi</b> della scheda. Si tira sempre dalla spina, mai dal filo.',
      'mappa-cavi.svg', 'তার খোলার আগে দেখো কোথায় লাগানো আছে আর ফর্মে টিক দাও। সবসময় প্লাগ ধরে টানো, তার ধরে নয়।')
passo('smonta', 'ordine', 'Guarda l\'ordine dello smontaggio',
      'Oggi si toglie solo la <b>RAM</b>. Disco e lettore DVD restano nel loro rack di alluminio: si staccano solo i loro cavi SATA. Ordine: cavi del disco, cavi del DVD, RAM. <b>CPU e ventola (dissipatore) non si toccano.</b>',
      'ordine-smontaggio.svg', 'আজ শুধু RAM খোলা হবে। ডিস্ক আর DVD র‍্যাকে থাকে: শুধু তাদের SATA তার খোলো। CPU আর ফ্যান ছোঁবে না।')
passo('smonta', 'stacca', 'Stacca i cavi del disco e del DVD',
      'Stacca i due cavi SATA del disco e i due del lettore DVD: quello sottile (dati) e quello largo (corrente). Tira dalla spina, mai dal filo. Disco e DVD restano nel rack.',
      'mappa-cavi.svg', 'ডিস্ক আর DVD-র দুটি করে SATA তার খোলো। ডিস্ক আর DVD র‍্যাকে থাকে।')
passo('smonta', 'ram-via', 'Togli la RAM',
      'Apri i due ganci della RAM: il banco si alza da solo. Prendilo dai bordi, mai dai contatti dorati. Attento: la ventola della CPU è lì vicino e non si tocca.',
      'ram.svg', 'RAM-এর দুই হুক খোলো, RAM নিজেই উঠে আসবে। কিনারা ধরে নাও, সোনালি অংশ ছোঁবে না। পাশের CPU ফ্যান ছোঁবে না।')
passo('smonta', 'disco-via', 'Guarda il disco senza toglierlo',
      'Il disco resta nel rack di alluminio: non si toglie. Se l\'etichetta si vede, leggila: SSD o HDD? Quanti GB? Se non si vede, lo leggerete nel BIOS.',
      'disco.svg', 'ডিস্ক র‍্যাকেই থাকে, খুলবে না। লেবেল দেখা গেলে পড়ো: SSD না HDD? কত GB?')
passo('smonta', 'tavolo', 'Metti la RAM sul tavolo',
      'Appoggia la RAM sul tavolo, dalla parte dei bordi. Leggi l\'etichetta (per esempio 8GB DDR4) e scrivila nella scheda.',
      'tavolo.svg', 'RAM টেবিলে রাখো। লেবেল পড়ো (যেমন 8GB DDR4) আর ফর্মে লেখো।')

# --- ora 2: rimontaggio e BIOS
passo('rimonta', 'ordine-inv', 'Rimonta in ordine inverso',
      'Si rimonta al contrario: RAM, poi i cavi del DVD e del disco. Ogni pezzo si spinge finché fa clic.',
      'ordine-montaggio.svg', 'উল্টো ক্রমে জোড়া দাও: RAM, তারপর DVD আর ডিস্কের তার। «ক্লিক» পর্যন্ত চাপো।')
passo('rimonta', 'ram-dentro', 'Rimetti la RAM',
      'Guarda la tacca della RAM e il dentino dello slot: devono combaciare. Spingi dritto con due pollici fino al «clic».',
      'ram.svg', 'RAM-এর খাঁজ আর স্লটের দাঁত মেলাও। দুই বুড়ো আঙুলে সোজা চাপো, «ক্লিক» শব্দ পর্যন্ত।')
passo('rimonta', 'cavi-dentro', 'Riattacca i cavi del DVD e del disco',
      'Attacca al lettore DVD e al disco il cavo SATA dati (sottile) e il cavo SATA di alimentazione (largo). Ogni spina entra in un solo verso: non forzare.',
      'mappa-cavi.svg', 'DVD আর ডিস্কে SATA ডেটা আর পাওয়ার তার লাগাও। জোর করবে না।')
passo('rimonta', 'checklist', 'Fai i 5 controlli prima di accendere',
      'Controllate insieme: RAM con i ganci chiusi, disco con 2 cavi, DVD con 2 cavi, 24 pin al suo posto, niente lasciato dentro il case. Spunta i 5 controlli nella <b>scheda</b> in fondo. Se un controllo è NO, non accendere: sistema prima.',
      'checklist.svg', 'চালু করার আগে ৫টি জিনিস দেখে ফর্মে টিক দাও। কোনোটা না হলে চালু করবে না।')
passo('rimonta', 'chiudi', 'Chiudi il case e collega i cavi',
      'Rimetti il pannello e fallo scorrere finché fa clic. Collega monitor, tastiera, mouse e rete. La corrente per ultima.',
      'collega.svg', 'প্যানেল লাগিয়ে «ক্লিক» পর্যন্ত সরাও। মনিটর, কীবোর্ড, মাউস, নেটওয়ার্ক লাগাও। বিদ্যুৎ সবার শেষে।')
passo('bios', 'accendi', 'Accendi ed entra nel BIOS',
      'Premi il tasto di accensione. Subito, più volte, premi <b>Esc</b>: si apre il menu HP. Poi premi <b>F10</b> (BIOS Setup). Entri nel BIOS/UEFI.',
      'tasti-bios.svg', 'চালু করে সঙ্গে সঙ্গে বারবার Esc চাপো, তারপর F10। BIOS খুলবে।')
passo('bios', 'leggi', 'Leggi CPU e RAM in System Information',
      'In Main scegli <b>System Information</b> (oppure dal menu Esc premi <b>F1</b>). Leggi Processor e Memory Size: <b>4096 MB = 4 GB</b>. Se dopo il rimontaggio vedi meno memoria, la RAM non è inserita bene. Scrivi CPU e RAM nella scheda.',
      'bios-info.svg', 'Main > System Information (বা Esc > F1)। Processor আর Memory Size পড়ো: 4096 MB = 4 GB। কম দেখালে RAM ঠিকমতো বসেনি।')
passo('bios', 'boot', 'Controlla l\'avvio da USB',
      'Apri la scheda <b>Advanced</b>, poi <b>Boot Options</b>. <b>USB Storage Boot</b> deve essere spuntato. Poi torna in <b>Main</b>, scegli <b>Save Changes and Exit</b> e conferma.',
      'bios-boot.svg', 'Advanced > Boot Options: USB Storage Boot-এ টিক থাকতে হবে। তারপর Main > Save Changes and Exit।')
passo('bios', 'menu-avvio', 'Se non trovi l\'ordine di avvio: menu F9',
      'Nessun problema: spegni, accendi, premi <b>Esc</b> e poi <b>F9</b> (Boot Menu). Nel menu di avvio scegli la chiavetta USB. Vale solo per questa volta.',
      'menu-avvio.svg', 'না পেলে: চালু করে Esc, তারপর F9 চাপো, মেনু থেকে USB বেছে নাও।')

# --- ora 3: installazione di Windows 10 (A) o Linux Mint (B)
passo('installa', 'w-avvio', 'Parti dalla chiavetta di Windows 10',
      'Metti la chiavetta nella porta USB. Accendi, premi <b>Esc</b> e poi <b>F9</b>: scegli la riga con <b>USB</b>. Se compare «Premi un tasto per avviare da…», premi un tasto qualsiasi.',
      'w-avvio.svg', 'USB লাগাও, চালু করে Esc তারপর F9 চাপো, USB বেছে নাও।', 'A')
passo('installa', 'w-lingua', 'Lingua: Italiano, poi Installa',
      'Lascia Italiano in tutte e tre le caselle. Premi <b>Avanti</b>, poi <b>Installa</b>.',
      'w-lingua.svg', 'ভাষা Italiano রাখো। Avanti, তারপর Installa চাপো।', 'A')
passo('installa', 'w-key', 'Non ho un codice Product Key',
      'Clicca la scritta in basso <b>Non ho un codice Product Key</b>. Poi scegli l\'edizione che dice il Professore (di solito <b>Windows 10 Pro</b>) e premi Avanti.',
      'w-key.svg', '«Non ho un codice Product Key» চাপো। Windows 10 Pro বেছে Avanti চাপো।', 'A')
passo('installa', 'w-tipo', 'Accetta e scegli Personalizzata',
      'Spunta <b>Accetto le condizioni di licenza</b> e premi Avanti. Poi scegli <b>Personalizzata: installa solo Windows</b>.',
      'w-tipo.svg', 'লাইসেন্সে টিক দাও। তারপর «Personalizzata» বেছে নাও।', 'A')
passo('installa', 'w-disco', 'Scegli il disco',
      'Questo è il PC del banco: si può cancellare tutto. Seleziona ogni partizione e premi <b>Elimina</b>. Resta «Unità 0 Spazio non allocato»: selezionala e premi <b>Avanti</b>.',
      'w-disco.svg', 'বেঞ্চের PC: সব মুছে ফেলা যায়। প্রতিটি পার্টিশন Elimina করো। «Spazio non allocato» বেছে Avanti।', 'A')
passo('installa', 'w-copia', 'Aspetta: Windows copia i file',
      'Windows copia i file e riavvia da solo (15-25 minuti). <b>Non toccare niente.</b> Intanto leggete la teoria qui sotto e fate il quiz.',
      'w-copia.svg', 'Windows ফাইল কপি করে নিজে রিস্টার্ট হয় (১৫-২৫ মিনিট)। কিছু ছোঁবে না। এর মধ্যে নিচের থিওরি পড়ো আর কুইজ করো।', 'A',
      extra='TEORIA')
passo('installa', 'm-avvio', 'Parti dalla chiavetta di Linux Mint',
      'Metti la chiavetta. Accendi, premi <b>Esc</b> e poi <b>F9</b>: scegli <b>USB</b>. Nel menu scegli <b>Start Linux Mint</b>.',
      'm-avvio.svg', 'USB লাগাও, Esc তারপর F9 চাপো, Start Linux Mint বেছে নাও।', 'B')
passo('installa', 'm-installa', 'Doppio clic su «Install Linux Mint»',
      'Sul desktop fai doppio clic sull\'icona del disco <b>Install Linux Mint</b>. Scegli Italiano e la tastiera Italiano.',
      'm-installa.svg', 'ডেস্কটপে «Install Linux Mint»-এ ডাবল ক্লিক করো। Italiano বেছে নাও।', 'B')
passo('installa', 'm-disco', 'Cancella il disco e installa',
      'Scegli <b>Cancella il disco e installa Linux Mint</b>. Premi Installa e poi Continua. Fuso orario: Roma.',
      'm-disco.svg', '«Cancella il disco e installa» বেছে Installa চাপো। সময় অঞ্চল: Roma।', 'B')
passo('installa', 'm-utente', 'Il primo utente (amministratore)',
      'Nome: <b>tecnico</b>. Nome del computer: <b>PC-B</b> e il numero del banco. Scegli la password che dice il Professore. Aspetta la copia e riavvia. Intanto leggete la teoria e fate il quiz.',
      'm-utente.svg', 'নাম tecnico, কম্পিউটারের নাম PC-B আর বেঞ্চ নম্বর। কপির সময় থিওরি পড়ো আর কুইজ করো।', 'B', extra='TEORIA')

passo('quiz', 'quiz', 'Quiz su Moduli (8 domande, servono 6 giuste)',
      'Premi il bottone verde, rispondi e premi <b>Invia</b>. Puoi rifarlo: vale il migliore.',
      'quiz.svg', 'সবুজ বাটন চাপো, উত্তর দাও, Invia চাপো। ৮টির মধ্যে ৬টি ঠিক লাগবে।', None,
      extra='<a class="bt v" data-quiz="quiz_pc" href="#" target="_blank" rel="noopener">Apri il quiz</a><p class="mu" data-quizmsg="quiz_pc"></p>')

passo('primo_avvio', 'w-regione', 'Primo avvio: Italia e tastiera Italiano',
      'Scegli <b>Italia</b> e premi Sì. Tastiera <b>Italiano</b>, Sì. Alla seconda tastiera premi <b>Ignora</b>.',
      'w-regione.svg', 'Italia বেছে Sì। কীবোর্ড Italiano, Sì। দ্বিতীয় কীবোর্ডে Ignora।', 'A')
passo('primo_avvio', 'w-rete', 'Non ho Internet',
      'Il PC non è in rete: va bene. In basso a sinistra clicca <b>Non ho Internet</b>, poi <b>Continua con configurazione limitata</b>. (Nella versione Pro: «Configura per uso personale», poi «Account offline» e «Esperienza limitata».)',
      'w-rete.svg', 'নিচে বাঁয়ে «Non ho Internet», তারপর «Continua con configurazione limitata»।', 'A')
passo('primo_avvio', 'w-account', 'Account locale: l\'utente tecnico',
      'Così non serve un account Microsoft: è un <b>account locale</b>. Nome: <b>tecnico</b>. Questo primo utente è <b>amministratore</b>. Password: quella che dice il Professore. Poi 3 domande di sicurezza.',
      'w-account.svg', 'Microsoft অ্যাকাউন্ট লাগবে না: লোকাল অ্যাকাউন্ট। নাম tecnico। এটা অ্যাডমিন।', 'A')
passo('primo_avvio', 'w-privacy', 'Privacy: tutto No, poi Accetta',
      'Metti <b>No</b> a tutte le voci e premi <b>Accetta</b>. Se chiede Cortana: «Non ora». Aspetta il desktop.',
      'w-privacy.svg', 'সব No করে Accetta চাপো। ডেস্কটপের জন্য অপেক্ষা করো।', 'A')
passo('primo_avvio', 'w-nomepc', 'Fallo tuo: dai il nome al PC',
      'Tasto destro su Start, <b>Sistema</b>. Premi <b>Rinomina questo PC</b>. Scrivi <b>PC-B</b> e il numero del banco (per esempio PC-B3). Riavvia più tardi.',
      'w-nomepc.svg', 'Start-এ ডান ক্লিক, Sistema, «Rinomina questo PC»। নাম PC-B আর বেঞ্চ নম্বর।', 'A')

passo('utenti', 'w-utenti', 'Strumento 1: crea l\'utente standard',
      'Start, <b>Impostazioni</b> (ingranaggio), <b>Account</b>, <b>Famiglia e altri utenti</b>. Premi <b>Aggiungi un altro utente a questo PC</b>.',
      'w-utenti.svg', 'Impostazioni > Account > Famiglia e altri utenti > Aggiungi un altro utente।', 'A')
passo('utenti', 'w-senza-ms', 'Utente senza account Microsoft',
      'Clicca <b>Non ho le informazioni di accesso di questa persona</b>, poi <b>Aggiungi un utente senza account Microsoft</b>. Nome: <b>studente</b>. Password e domande. Avanti.',
      'w-senza-ms.svg', '«Non ho le informazioni…», তারপর «Aggiungi un utente senza account Microsoft»। নাম studente।', 'A')
passo('utenti', 'w-tipo-account', 'Controlla: amministratore e standard',
      'Clicca <b>studente</b>, poi <b>Cambia tipo di account</b>: deve dire <b>Utente standard</b>. L\'utente tecnico è <b>Amministratore</b>. Con l\'edizione Pro lo vedi anche in <b>Gestione computer</b> (tasto destro su Start), <b>Utenti e gruppi locali</b>, <b>Utenti</b>.',
      'w-tipo-account.svg', 'studente = Utente standard, tecnico = Amministratore। Pro হলে: Gestione computer > Utenti e gruppi locali।', 'A')
passo('utenti', 'm-utenti', 'Strumento 1: crea l\'utente standard',
      'Menu, <b>Utenti e gruppi</b>. Premi <b>Aggiungi</b>. Tipo di account: <b>Standard</b>. Nome: <b>studente</b>. Poi imposta la password.',
      'm-utenti.svg', 'মেনু > Utenti e gruppi > Aggiungi। ধরন Standard, নাম studente।', 'B')

passo('strumenti', 'w-taskmgr', 'Strumento 2: Gestione attività',
      'Premi insieme <b>Ctrl + Maiusc + Esc</b>. Clicca <b>Più dettagli</b>, poi la scheda <b>Prestazioni</b>. Leggi quanta <b>Memoria</b> (RAM) ha il PC: scrivila nella scheda.',
      'w-taskmgr.svg', 'Ctrl + Shift + Esc চাপো। Prestazioni ট্যাবে RAM কত দেখে লেখো।', 'A')
passo('strumenti', 'w-devmgr', 'Strumento 3: Gestione dispositivi e Gestione disco',
      'Tasto destro su Start, <b>Gestione dispositivi</b>: c\'è un triangolo giallo? Scrivilo. Poi tasto destro su Start, <b>Gestione disco</b>: leggi quanti GB ha il disco C:.',
      'w-devmgr.svg', 'Start-এ ডান ক্লিক > Gestione dispositivi: হলুদ ত্রিভুজ আছে? তারপর Gestione disco: C: কত GB?', 'A')
passo('strumenti', 'm-monitor', 'Strumento 2: Monitor di sistema',
      'Menu, <b>Monitor di sistema</b>, scheda <b>Risorse</b>: leggi quanta memoria ha il PC. Poi apri <b>Dischi</b> e leggi quanti GB ha il disco.',
      'm-monitor.svg', 'মেনু > Monitor di sistema > Risorse: RAM কত দেখো। Dischi: ডিস্ক কত GB।', 'B')

passo('rete', 'schema-rete', 'Capire l\'indirizzo IP',
      'Ogni PC ha un indirizzo IP. Nella stessa rete le prime 3 parti sono <b>uguali</b>, l\'ultima è <b>diversa</b>. Il vostro IP è nel riquadro blu qui sotto: chiedete al PC accanto il suo e controllate che le prime 3 parti siano uguali.',
      'rete-schema.svg', 'একই নেটওয়ার্কে IP-র প্রথম ৩ অংশ এক, শেষটা আলাদা। পাশের PC-র IP জেনে মিলিয়ে দেখো।', None, extra='IP')
passo('rete', 'w-ncpa', 'Apri le impostazioni della scheda di rete',
      'Start, scrivi <b>Pannello di controllo</b>, Invio. <b>Rete e Internet</b>, <b>Centro connessioni di rete e condivisione</b>, a sinistra <b>Modifica impostazioni scheda</b>. Tasto destro su <b>Ethernet</b>, <b>Proprietà</b>.',
      'w-ncpa.svg', 'Pannello di controllo > Centro connessioni > Modifica impostazioni scheda > Ethernet > Proprietà।', 'A')
passo('rete', 'w-ipv4', 'Scrivi l\'IP a mano',
      'Doppio clic su <b>Protocollo Internet versione 4 (TCP/IPv4)</b>. Scegli <b>Utilizza il seguente indirizzo IP</b> e scrivi i valori del riquadro blu: indirizzo, subnet mask, gateway, DNS. OK, OK.',
      'w-ipv4.svg', 'IPv4-এ ডাবল ক্লিক। «Utilizza il seguente indirizzo IP» বেছে নীল বাক্সের মান লেখো।', 'A')
passo('rete', 'w-firewall', 'Lascia passare il ping',
      'Windows blocca il ping. Start, scrivi <b>Windows Defender Firewall con sicurezza avanzata</b>, Invio. <b>Regole connessioni in entrata</b>: tasto destro su ogni riga <b>Condivisione file e stampanti (Richiesta echo - ICMPv4 in entrata)</b>, <b>Abilita regola</b>.',
      'w-firewall.svg', 'Firewall con sicurezza avanzata > Regole in entrata > «Richiesta echo - ICMPv4» > Abilita regola।', 'A')
passo('rete', 'm-ip', 'Scrivi l\'IP a mano',
      'Menu, <b>Impostazioni di rete</b>, <b>Cablata</b>, ingranaggio, scheda <b>IPv4</b>: metodo <b>Manuale</b>. Scrivi i valori del riquadro blu. Applica.',
      'm-ip.svg', 'Impostazioni di rete > Cablata > IPv4 > Manuale। নীল বাক্সের মান লেখো।', 'B')
passo('rete', 'cavo', 'Il Professore vi mette in rete',
      'Quando il Professore lo dice, collegate il cavo di rete del PC del banco allo switch.',
      'collega.svg', 'প্রফেসর বললে বেঞ্চের PC-র নেটওয়ার্ক তার সুইচে লাগাও।')
passo('rete', 'ping', 'Mostralo: ping al PC accanto',
      'Scrivete nella scheda l\'IP del PC accanto. Sul PC del banco: Start, scrivi <b>cmd</b>, Invio. Scrivi il comando del riquadro scuro qui sotto e premi Invio. «Risposta da…» = la rete funziona!',
      'ping.svg', 'পাশের PC-র IP ফর্মে লেখো। cmd খোলো, নিচের কমান্ড লিখে Enter। «Risposta da…» = কাজ করছে!', None, extra='PING')

passo('base_link', 'base', 'Impostazioni di base: Chrome ed estensioni',
      'Apri la pagina <b>Impostazioni di base</b> e fai i suoi 5 passi: Chrome come browser predefinito e le estensioni dei file visibili. Poi torna qui.',
      'w-estensioni.svg', '«Impostazioni di base» পাতা খোলো: Chrome ডিফল্ট ব্রাউজার আর ফাইলের এক্সটেনশন দেখানো। তারপর ফিরে এসো।', None,
      extra='<a class="bt" href="impostazioni-base.html" target="_blank" rel="noopener">Apri «Impostazioni di base» (si apre in una finestra nuova, poi torna qui)</a>')

for n in (1, 2, 3):
    passo(f'scheda{n}', 'scheda', 'Compila la scheda e mandala al prof',
          'Compilate insieme la scheda qui sotto. Poi premi <b>Manda al prof</b>: un clic solo. Si apre la pagina «Consegna arrivata al prof».',
          'consegna.svg', 'নিচের ফর্ম পূরণ করো, তারপর «Manda al prof» চাপো। একবার ক্লিক।', None, extra='SCHEDA')

# --- la pagina «caccia al guasto» (2INF; chiusa finché config.json non ha "guasti_aperta": true)
passo('guasti', 'g-mosse', 'Le 4 mosse del tecnico',
      'Il Professore ha messo un guasto nel PC del banco. Voi siete i tecnici. Si lavora con 4 mosse: <b>sintomo</b>, <b>ipotesi</b>, <b>prova</b>, <b>soluzione</b>.',
      'caccia.svg', 'প্রফেসর PC-তে একটা সমস্যা রেখেছেন। ৪টি ধাপ: লক্ষণ, ধারণা, পরীক্ষা, সমাধান।')
passo('guasti', 'g-sintomo', 'Mossa 1: guarda il sintomo',
      'Accendi il PC e guarda bene. Le ventole girano? Lo schermo dice qualcosa? Scegli il sintomo nella scheda qui sotto.',
      'tasti-bios.svg', 'PC চালু করে ভালো করে দেখো। ফর্মে লক্ষণ বেছে নাও।')
passo('guasti', 'g-ipotesi', 'Mossa 2: scrivi un\'ipotesi',
      'Che cosa può essere? Guardate lo schema dei componenti e scrivete la vostra idea nella scheda.',
      'componenti.svg', 'কী হতে পারে? তোমাদের ধারণা ফর্মে লেখো।')
passo('guasti', 'g-spegni', 'Prima di aprire: spegni e togli la spina',
      'Se dovete aprire il case: spegnete il PC, togliete la spina e toccate il metallo del case. Sempre.',
      'spina.svg', 'কেস খোলার আগে PC বন্ধ করো, প্লাগ খোলো, ধাতু ছোঁও।', extra=NON_SI_TOCCA)
passo('guasti', 'g-prova', 'Mossa 3: fai una prova',
      'Controllate <b>una cosa sola</b> per volta. Scrivete nella scheda che cosa avete controllato.',
      'mappa-cavi.svg', 'একবারে একটা জিনিস দেখো। ফর্মে লেখো কী দেখেছ।')
passo('guasti', 'g-soluzione', 'Mossa 4: ripara e riprova',
      'Riparate, chiudete e riaccendete. Funziona? Scrivete la soluzione. Non funziona? Tornate alla mossa 2 con un\'altra ipotesi.',
      'checklist.svg', 'ঠিক করে আবার চালু করো। কাজ না করলে ধাপ ২-এ ফিরে যাও।')
passo('scheda_g', 'scheda', 'Compila la scheda e mandala al prof',
      'Scrivete i guasti trovati (fino a 3). Poi premete <b>Manda al prof</b>: un clic solo. Potete rimandarla dopo il guasto nuovo: vale l\'ultima.',
      'consegna.svg', 'ফর্ম পূরণ করে «Manda al prof» চাপো।', None, extra='SCHEDA')

# --- la pagina «impostazioni di base» (riusabile: 2INF, 3INF)
BASE = [
    ('b-chrome', 'Chrome c\'è?',
     'Clicca Start e scrivi <b>Chrome</b>. Se compare Google Chrome, vai al passo 2. Se non c\'è: apri <b>Microsoft Edge</b>, scrivi <b>google.com/chrome</b>, premi <b>Scarica Chrome</b> e apri il file scaricato (serve Internet).',
     'w-chrome.svg', 'Start-এ Chrome লেখো। না থাকলে Edge খুলে google.com/chrome থেকে ডাউনলোড করো (ইন্টারনেট লাগবে)।'),
    ('b-predefinito', 'Chrome browser predefinito',
     'Start, <b>Impostazioni</b>, <b>App</b>, <b>App predefinite</b>. Sotto <b>Web browser</b> clicca il browser che c\'è e scegli <b>Google Chrome</b>. Se chiede conferma: <b>Cambia comunque</b>.',
     'w-predefinite.svg', 'Impostazioni > App > App predefinite > Web browser > Google Chrome।'),
    ('b-estensioni', 'Mostra le estensioni dei file',
     'Apri <b>Esplora file</b> (tasti Windows + E). In alto clicca la scheda <b>Visualizza</b>. Spunta la casella <b>Estensioni nomi file</b>.',
     'w-estensioni.svg', 'Esplora file (Windows + E) > Visualizza > «Estensioni nomi file»-এ টিক দাও।'),
    ('b-nascosti', 'Mostra gli elementi nascosti',
     'Sempre nella scheda <b>Visualizza</b>, spunta anche la casella <b>Elementi nascosti</b>. Le cartelle nascoste diventano più chiare ma si vedono.',
     'w-nascosti.svg', 'Visualizza ট্যাবে «Elementi nascosti»-এ টিক দাও।'),
    ('b-prova', 'Prova: vedi .txt?',
     'In <b>Documenti</b> fai tasto destro, <b>Nuovo</b>, <b>Documento di testo</b>. Il nome finisce con <b>.txt</b>? Allora le estensioni si vedono. Fatto!',
     'w-prova.svg', 'Documenti-এ নতুন টেক্সট ফাইল বানাও। নামের শেষে .txt দেখা যাচ্ছে? তাহলে হয়ে গেছে!'),
]

# ------------------------------------------------------------------ le schede
OPZ_COMP = ['CPU e dissipatore', 'RAM', 'Alimentatore', 'Disco', 'Cavo SATA dati', 'Cavo di alimentazione 24 pin',
            'Scheda video', 'Scheda madre']
CHIAVE1 = {'A': 'CPU e dissipatore', 'B': 'RAM', 'C': 'Alimentatore', 'D': 'Disco', 'E': 'Cavo SATA dati',
           'F': 'Cavo di alimentazione 24 pin', 'G': 'Scheda video', 'H': 'Scheda madre'}
SCHEDE = {
    1: {'titolo': 'Scheda dell\'ora 1: riconoscimento e smontaggio', 'campi':
        [{'k': x, 'l': f'Lettera {x}', 't': 'scelta', 'o': sorted(OPZ_COMP)} for x in 'ABCDEFGH'] + [
            {'k': 'video', 'l': 'Il vostro PC ha la scheda video separata?', 't': 'scelta', 'o': ['sì', 'no']},
            {'k': 'disco_tipo', 'l': 'Il disco è… (dall\'etichetta, se si vede)', 't': 'scelta', 'o': ['SSD 2,5"', 'SSD M.2', 'HDD 3,5"', 'HDD 2,5"', 'non si vede']},
            {'k': 'disco_gb', 'l': 'Quanti GB ha il disco (dall\'etichetta, se si vede)?', 't': 'testo'},
            {'k': 'ram_n', 'l': 'Quanti banchi di RAM?', 't': 'scelta', 'o': ['1', '2', '3', '4']},
            {'k': 'ram_etichetta', 'l': 'Che cosa dice l\'etichetta della RAM (per esempio 8GB DDR4)?', 't': 'testo'},
            {'k': 'watt', 'l': 'Quanti watt (W) ha l\'alimentatore (etichetta)?', 't': 'testo'},
            {'k': 'mappa', 'l': 'Mappa dei cavi: spunta i cavi che avete staccato', 't': 'spunte',
             'o': ['Disco: SATA dati', 'Disco: SATA alimentazione', 'DVD: SATA dati', 'DVD: SATA alimentazione']},
            {'k': 'dvd', 'l': 'Il vostro PC ha il lettore DVD nel rack?', 't': 'scelta', 'o': ['sì', 'no']}]},
    2: {'titolo': 'Scheda dell\'ora 2: controlli e BIOS', 'campi': [
        {'k': 'c_ram', 'l': 'RAM ben dentro, ganci chiusi', 't': 'spunta'},
        {'k': 'c_sata', 'l': 'Disco: 2 cavi SATA attaccati', 't': 'spunta'},
        {'k': 'c_dvd', 'l': 'DVD: 2 cavi SATA attaccati', 't': 'spunta'},
        {'k': 'c_24', 'l': 'Cavo 24 pin al suo posto', 't': 'spunta'},
        {'k': 'c_dentro', 'l': 'Niente lasciato dentro il case', 't': 'spunta'},
        {'k': 'tasto', 'l': 'Con quale tasto siete entrati nel BIOS?', 't': 'scelta', 'o': ['Esc poi F10', 'F10', 'Canc (Del)', 'F2', 'F1', 'altro']},
        {'k': 'cpu', 'l': 'Nome della CPU (dal BIOS)', 't': 'testo'},
        {'k': 'ram', 'l': 'Quanta RAM (dal BIOS)', 't': 'testo'},
        {'k': 'disco', 'l': 'Nome o dimensione del disco (dal BIOS)', 't': 'testo'},
        {'k': 'boot_usb', 'l': 'USB Storage Boot spuntato (o USB scelta con F9)', 't': 'spunta'}]},
    3: {'titolo': 'Scheda dell\'ora 3: sistema, utenti e rete', 'campi': [
        {'k': 'installato', 'l': 'Sistema installato: il desktop si vede', 't': 'spunta'},
        {'k': 'nome_pc', 'l': 'Nome del PC (per esempio PC-B3)', 't': 'testo'},
        {'k': 'admin', 'l': 'Nome dell\'utente amministratore', 't': 'testo'},
        {'k': 'standard', 'l': 'Nome dell\'utente standard', 't': 'testo'},
        {'k': 'ram_gb', 'l': 'RAM letta in Gestione attività (o Monitor di sistema)', 't': 'testo'},
        {'k': 'dispositivi', 'l': 'Gestione dispositivi: triangoli gialli?', 't': 'scelta', 'o': ['nessuno', 'sì, uno o più']},
        {'k': 'disco_c', 'l': 'Quanti GB ha il disco C: (Gestione disco)', 't': 'testo'},
        {'k': 'ip', 'l': 'Il vostro indirizzo IP', 't': 'testo'},
        {'k': 'ip_vicino', 'l': 'L\'indirizzo IP del PC accanto', 't': 'testo'},
        {'k': 'ping', 'l': 'Il ping al PC accanto è…', 't': 'scelta', 'o': ['riuscito', 'non riuscito']},
        {'k': 'chrome', 'l': 'Chrome è il browser predefinito', 't': 'spunta'},
        {'k': 'estensioni', 'l': 'Le estensioni dei file si vedono', 't': 'spunta'}]},
}

SINTOMI = ['Non si accende niente', 'Ventole girano ma schermo nero', 'Beep e schermo nero', 'Si spegne da solo',
           'Nessun dispositivo di avvio', 'Non parte dalla chiavetta USB', 'Monitor: nessun segnale', 'Il ping non risponde',
           'Conflitto di indirizzi IP', 'Altro']
SCHEDE['G'] = {'titolo': 'Scheda «Caccia al guasto»', 'campi': [
    c for g in (1, 2, 3) for c in (
        {'k': f'g{g}_sintomo', 'l': f'Guasto {g} · Sintomo: che cosa vedete?', 't': 'scelta', 'o': SINTOMI},
        {'k': f'g{g}_ipotesi', 'l': f'Guasto {g} · Ipotesi: che cosa può essere?', 't': 'testo'},
        {'k': f'g{g}_prova', 'l': f'Guasto {g} · Prova: che cosa avete controllato?', 't': 'testo'},
        {'k': f'g{g}_soluzione', 'l': f'Guasto {g} · Soluzione: che cosa avete fatto?', 't': 'testo'},
        {'k': f'g{g}_risolto', 'l': f'Guasto {g} · Risolto?', 't': 'scelta', 'o': ['sì', 'no']})]}

TEORIA = '''<details class="teo" open><summary>Teoria da leggere mentre Windows copia i file</summary>
<p><b>Utente amministratore</b>: può installare programmi e cambiare tutto. <b>Utente standard</b>: usa il PC ma non può cambiare le impostazioni importanti. Si lavora di solito con l'utente standard: è più sicuro.</p>
<p><b>Account locale</b>: il nome e la password stanno solo su questo PC. Non serve Internet.</p>
<p><b>Indirizzo IP</b>: il «numero civico» del PC nella rete. <b>Maschera</b> (255.255.255.0): dice che le prime 3 parti sono la rete. <b>Gateway</b>: la porta verso fuori. <b>DNS</b>: la rubrica che trasforma un nome (google.com) in un IP.</p>
<p><b>Ping</b>: manda un piccolo messaggio a un altro PC e aspetta la risposta. Se risponde, i due PC si parlano.</p></details>'''

# ------------------------------------------------------------------ schemi SVG
def disegni(conf):
    rete = conf['rete']
    f = S.finestra
    ip_es = rete['prefisso'] + str(rete['primo'] + 2)
    D = {
        'ruoli.svg': S.sicurezza('ruoli'), 'spina.svg': S.sicurezza('spina'), 'esd.svg': S.sicurezza('esd'),
        'tavolo.svg': S.sicurezza('tavolo'), 'disco.svg': S.sicurezza('disco'), 'apri-case.svg': S.sicurezza('apri-case'), 'componenti.svg': S.componenti_lettere(),
        'mappa-cavi.svg': S.sicurezza('mappa'), 'ram.svg': S.sicurezza('ram'), 'checklist.svg': S.sicurezza('checklist'),
        'collega.svg': S.sicurezza('collega'), 'tasti-bios.svg': S.sicurezza('tasti-bios'),
        'rete-schema.svg': S.sicurezza('rete', rete['prefisso'], rete['primo']),
        'ordine-smontaggio.svg': S.ordine('Ordine dello smontaggio', ['Cavi del disco', 'Cavi del DVD', 'RAM']),
        'ordine-montaggio.svg': S.ordine('Ordine del rimontaggio', ['RAM', 'Cavi del DVD', 'Cavi del disco'], True),
        'consegna.svg': S.consegna(), 'quiz.svg': S.quiz(),
        'bios-info.svg': S.bios('HP · System Information (F1)', [
            ('Product Name', 'HP ProDesk 600 G3 MT'), ('Processor 1', 'Intel Core i3-6100 3.70GHz'), ('Memory Size', '4096 MB (= 4 GB)'),
            ('System BIOS', 'P02 Ver. 02.38'), ('', '')], evid=[1, 2], nota='Meno di 4096 MB dopo il rimontaggio = RAM non inserita bene'),
        'bios-boot.svg': S.bios('HP Computer Setup · Advanced · Boot Options', [
            ('[ ] Fast Boot', ''), ('[ ] CD-ROM Boot', ''), ('[x] USB Storage Boot', 'deve essere spuntato'),
            ('UEFI Boot Order', 'SATA0: Windows Boot Manager'), ('', '')], evid=[2], nota='Poi Main > Save Changes and Exit'),
        'menu-avvio.svg': S.bios('Boot Menu (Esc, poi F9)', [
            ('1.', 'Windows Boot Manager'), ('2.', 'UEFI: USB Flash Disk'), ('3.', 'SATA 0: SSD 240GB'), ('4.', 'Enter Setup')],
            evid=[1], nota='Frecce su/giù per scegliere, Invio per partire'),
        'w-avvio.svg': S.bios('Boot Menu (Esc, poi F9)', [('1.', 'Windows Boot Manager'), ('2.', 'UEFI: USB Flash Disk'), ('3.', 'SATA 0')],
                              evid=[1], nota='Scegli la riga con USB e premi Invio'),
        'w-lingua.svg': f('Installazione di Windows', [
            ('c', 60, 90, 420, 'Lingua da installare', 'Italiano (Italia)'), ('c', 60, 160, 420, 'Formato ora e valuta', 'Italiano (Italia)'),
            ('c', 60, 230, 420, 'Tastiera o metodo di input', 'Italiano'), ('b', 540, 320, 130, 'Avanti', True)]),
        'w-key.svg': f('Attiva Windows', [
            ('t', 50, 90, 'Se è la prima volta che installi Windows, immetti un Product Key.'),
            ('c', 50, 130, 500, 'Product Key', ''), ('v', 50, 300, 300, 'Non ho un codice Product Key', True),
            ('a', 420, 315, 360, 315), ('b', 560, 320, 120, 'Avanti', False)]),
        'w-tipo.svg': f('Installazione di Windows', [
            ('k', 50, 100, 'Accetto le condizioni di licenza', True, True),
            ('t', 50, 160, 'Scegli il tipo di installazione:', 17, True),
            ('v', 50, 180, 600, 'Aggiornamento: installa Windows e mantieni file, impostazioni…', False),
            ('v', 50, 230, 600, 'Personalizzata: installa solo Windows (opzioni avanzate)', True)]),
        'w-disco.svg': f('Dove vuoi installare Windows?', [
            ('v', 40, 75, 640, 'Unità 0 Partizione 1: Riservato per il sistema     500 MB', False),
            ('v', 40, 110, 640, 'Unità 0 Partizione 2                              237 GB', False),
            ('v', 40, 145, 640, 'Unità 0 Spazio non allocato                       238 GB', True),
            ('b', 40, 210, 130, 'Elimina', False), ('b', 190, 210, 130, 'Nuovo', False),
            ('n', 40, 290, 'Elimina ogni partizione: resta «Spazio non allocato».'),
            ('b', 540, 320, 130, 'Avanti', True)]),
        'w-copia.svg': f('Installazione di Windows', [
            ('t', 50, 90, 'Stato', 17, True), ('k', 60, 130, 'Copia dei file di Windows', True, False),
            ('k', 60, 165, 'Preparazione dei file per l\'installazione (47%)', False, True),
            ('k', 60, 200, 'Installazione delle funzionalità', False, False), ('k', 60, 235, 'Installazione degli aggiornamenti', False, False),
            ('n', 50, 300, 'Il PC si riavvia da solo: non toccare niente.')]),
        'w-regione.svg': f('Configurazione di Windows', [
            ('t', 50, 90, 'Iniziamo dall\'area geografica. È corretta?', 19, True),
            ('v', 50, 120, 400, 'Irlanda', False), ('v', 50, 155, 400, 'Italia', True), ('v', 50, 190, 400, 'Kenya', False),
            ('b', 560, 320, 110, 'Sì', True)]),
        'w-rete': None,
        'w-rete.svg': f('Connettiamoti a una rete', [
            ('t', 50, 90, 'Per continuare devi connetterti a Internet.', 18, True),
            ('v', 50, 120, 400, 'Ethernet: non connessa', False),
            ('v', 40, 320, 230, 'Non ho Internet', True), ('a', 330, 335, 280, 335),
            ('b', 440, 320, 240, 'Continua con config. limitata', False)]),
        'w-account.svg': f('Chi userà questo PC?', [
            ('t', 50, 100, 'Account locale (offline): niente account Microsoft.', 17, True),
            ('c', 50, 140, 420, 'Nome', 'tecnico'), ('t', 50, 240, 'Il primo utente è AMMINISTRATORE.', 17, True),
            ('b', 560, 320, 110, 'Avanti', True)]),
        'w-privacy.svg': f('Scegli le impostazioni di privacy', [
            ('k', 50, 100, 'Posizione: No', False, True), ('k', 50, 140, 'Trova il mio dispositivo: No', False, True),
            ('k', 50, 180, 'Dati di diagnostica: obbligatori', False, False), ('k', 50, 220, 'Annunci personalizzati: No', False, True),
            ('b', 540, 320, 130, 'Accetta', True)]),
        'w-nomepc.svg': f('Impostazioni · Sistema · Informazioni', [
            ('t', 50, 90, 'Specifiche del dispositivo', 18, True), ('t', 50, 125, 'Nome dispositivo    DESKTOP-7Q2K1LM'),
            ('t', 50, 155, 'Processore           Intel Core i5'), ('t', 50, 185, 'RAM installata      8,00 GB'),
            ('b', 50, 220, 250, 'Rinomina questo PC', True), ('c', 360, 210, 300, 'Nuovo nome', 'PC-B3')]),
        'w-utenti.svg': f('Impostazioni · Account', [
            ('v', 30, 70, 200, 'Le tue info', False), ('v', 30, 105, 200, 'Opzioni di accesso', False),
            ('v', 30, 140, 200, 'Famiglia e altri utenti', True), ('t', 260, 100, 'Altri utenti', 18, True),
            ('b', 260, 120, 400, '+ Aggiungi un altro utente a questo PC', True)]),
        'w-senza-ms.svg': f('Account Microsoft', [
            ('t', 50, 90, 'In che modo accederà questa persona?', 18, True), ('c', 50, 110, 500, 'Email o telefono', ''),
            ('v', 50, 180, 470, 'Non ho le informazioni di accesso di questa persona', True),
            ('v', 50, 230, 470, 'Aggiungi un utente senza account Microsoft', True), ('c', 50, 290, 300, 'Nome utente', 'studente')]),
        'w-tipo-account.svg': f('Cambia tipo di account', [
            ('t', 50, 90, 'studente', 19, True), ('t', 50, 130, 'Tipo di account'),
            ('v', 50, 145, 300, 'Utente standard', True), ('v', 50, 180, 300, 'Amministratore', False),
            ('t', 380, 165, 'tecnico = Amministratore', 17, True), ('t', 380, 195, 'studente = Utente standard', 17, True),
            ('b', 400, 320, 130, 'OK', True)]),
        'w-taskmgr.svg': f('Gestione attività · Prestazioni', [
            ('v', 30, 70, 180, 'CPU   12%', False), ('v', 30, 105, 180, 'Memoria  2,1/8,0 GB', True), ('v', 30, 140, 180, 'Disco 0 (C:)', False),
            ('v', 30, 175, 180, 'Ethernet', False), ('r', 240, 75, 430, 200, '#e8f1fb'),
            ('t', 260, 110, 'Memoria   8,0 GB', 22, True), ('t', 260, 300, 'Ctrl + Maiusc + Esc  apre Gestione attività')]),
        'w-devmgr.svg': f('Gestione dispositivi', [
            ('t', 50, 90, 'PC-B3', 17, True), ('v', 70, 105, 400, '> Controller audio, video e giochi', False),
            ('v', 70, 140, 400, '> Schede di rete', False), ('v', 70, 175, 400, '> Unità disco', False),
            ('v', 70, 210, 400, '> Altri dispositivi  (triangolo giallo = driver mancante)', True),
            ('t', 50, 300, 'Gestione disco:  Disco 0   C:  NTFS   237 GB   Integro', 17, True)]),
        'w-ncpa.svg': f('Connessioni di rete', [
            ('t', 50, 90, 'Pannello di controllo > Rete e Internet > Centro connessioni', 15),
            ('v', 50, 105, 260, 'Modifica impostazioni scheda', True), ('r', 360, 150, 260, 80, '#e8f1fb'),
            ('t', 380, 185, 'Ethernet', 18, True), ('t', 380, 210, 'tasto destro > Proprietà', 15),
            ('v', 360, 250, 260, 'Proprietà', True), ('a', 330, 200, 358, 200)]),
        'w-ipv4.svg': f('Proprietà - Protocollo Internet versione 4 (TCP/IPv4)', [
            ('k', 50, 90, 'Utilizza il seguente indirizzo IP:', True, True),
            ('c', 70, 110, 260, 'Indirizzo IP', ip_es), ('c', 380, 110, 260, 'Subnet mask', rete['maschera']),
            ('c', 70, 180, 260, 'Gateway predefinito', rete['gateway']), ('c', 380, 180, 260, 'Server DNS preferito', rete['dns']),
            ('b', 420, 320, 110, 'OK', True), ('b', 550, 320, 120, 'Annulla', False)]),
        'w-firewall.svg': f('Windows Defender Firewall con sicurezza avanzata', [
            ('v', 30, 70, 230, 'Regole connessioni in entrata', True),
            ('v', 280, 110, 400, 'Condivisione file e stampanti (Richiesta echo', True),
            ('t', 290, 160, '- ICMPv4 in entrata)   tasto destro'), ('v', 280, 180, 220, 'Abilita regola', True),
            ('n', 50, 300, 'Abilita tutte le righe «Richiesta echo - ICMPv4 in entrata».')]),
        'ping.svg': f('Prompt dei comandi', [
            ('r', 22, 52, 676, 326, '#0c0c0c')], barra='#333') .replace('</svg>', '')
        + S.t(40, 90, 'C:\\Users\\tecnico> ping ' + rete['prefisso'] + str(rete['primo'] + 1), 17, '#f0f0f0')
        + S.t(40, 130, 'Risposta da ' + rete['prefisso'] + str(rete['primo'] + 1) + ': byte=32 durata<1ms TTL=128', 17, '#7ee787')
        + S.t(40, 160, 'Risposta da ' + rete['prefisso'] + str(rete['primo'] + 1) + ': byte=32 durata<1ms TTL=128', 17, '#7ee787')
        + S.t(40, 220, '«Risposta da…» = la rete funziona.', 18, '#ffd33d', True)
        + S.t(40, 250, '«Richiesta scaduta» = controlla IP, cavo e firewall.', 18, '#ffd33d', True) + '</svg>\n',
        # Linux Mint (variante B)
        'm-avvio.svg': S.bios('Linux Mint (menu della chiavetta)', [('', 'Start Linux Mint'), ('', 'OEM install'), ('', 'Boot from next volume')],
                              evid=[0], nota='Invio su «Start Linux Mint»'),
        'm-installa.svg': f('Desktop di Linux Mint (dalla chiavetta)', [
            ('r', 60, 90, 90, 80, '#cfe8cf'), ('t', 50, 200, 'Install Linux Mint', 16, True), ('a', 250, 130, 160, 130),
            ('t', 260, 136, 'doppio clic qui'), ('c', 50, 240, 300, 'Lingua', 'Italiano'), ('c', 380, 240, 300, 'Tastiera', 'Italian')], barra='#3c9a3c'),
        'm-disco.svg': f('Tipo di installazione', [
            ('k', 50, 110, 'Cancella il disco e installa Linux Mint', True, True), ('k', 50, 160, 'Altro (partizioni a mano)', False, False),
            ('b', 540, 320, 130, 'Installa', True)], barra='#3c9a3c'),
        'm-utente.svg': f('Chi sei?', [
            ('c', 50, 90, 300, 'Il tuo nome', 'tecnico'), ('c', 380, 90, 300, 'Nome del computer', 'PC-B3'),
            ('c', 50, 170, 300, 'Nome utente', 'tecnico'), ('c', 380, 170, 300, 'Password', '••••••'), ('b', 540, 320, 130, 'Continua', True)], barra='#3c9a3c'),
        'm-utenti.svg': f('Utenti e gruppi', [
            ('v', 30, 70, 200, 'tecnico (Amministratore)', False), ('b', 30, 300, 120, 'Aggiungi', True),
            ('c', 280, 90, 380, 'Tipo di account', 'Standard'), ('c', 280, 170, 380, 'Nome utente', 'studente')], barra='#3c9a3c'),
        'm-monitor.svg': f('Monitor di sistema · Risorse', [
            ('t', 50, 100, 'Memoria   2,0 GB (25%) di 7,7 GB', 20, True), ('t', 50, 160, 'Dischi: 240 GB'), ('r', 50, 190, 600, 90, '#e8f1fb')], barra='#3c9a3c'),
        'm-ip.svg': f('Cablata · IPv4', [
            ('k', 50, 90, 'Metodo IPv4: Manuale', True, True), ('c', 70, 110, 260, 'Indirizzo', ip_es), ('c', 380, 110, 260, 'Netmask', rete['maschera']),
            ('c', 70, 180, 260, 'Gateway', rete['gateway']), ('c', 380, 180, 260, 'DNS', rete['dns']), ('b', 540, 320, 130, 'Applica', True)], barra='#3c9a3c'),
        # impostazioni di base
        'w-chrome.svg': f('Microsoft Edge', [
            ('c', 50, 80, 600, 'Indirizzo', 'google.com/chrome'), ('t', 50, 170, 'Google Chrome', 24, True),
            ('b', 50, 200, 220, 'Scarica Chrome', True), ('t', 50, 300, 'Serve Internet: se il PC non è in rete, fallo dopo.')]),
        'w-predefinite.svg': f('Impostazioni · App · App predefinite', [
            ('t', 50, 90, 'Web browser', 18, True), ('v', 50, 100, 300, 'Microsoft Edge', False), ('a', 370, 115, 420, 115),
            ('v', 430, 100, 240, 'Google Chrome', True), ('t', 50, 200, 'Se chiede «Prima di cambiare…»: Cambia comunque.')]),
        'w-estensioni.svg': f('Esplora file · Visualizza', [
            ('v', 30, 62, 100, 'File', False), ('v', 140, 62, 100, 'Home', False), ('v', 250, 62, 120, 'Visualizza', True),
            ('k', 420, 120, 'Estensioni nomi file', True, True), ('k', 420, 160, 'Elementi nascosti', True, False),
            ('t', 50, 260, 'appunti.txt     foto.jpg     gioco.exe', 18, True)]),
        'w-nascosti.svg': f('Esplora file · Visualizza', [
            ('v', 250, 62, 120, 'Visualizza', True), ('k', 420, 120, 'Estensioni nomi file', True, False),
            ('k', 420, 160, 'Elementi nascosti', True, True), ('t', 50, 260, 'AppData (cartella nascosta: un po\' più chiara)', 17)]),
        'w-prova.svg': f('Documenti', [
            ('v', 50, 80, 300, 'Nuovo > Documento di testo', True), ('r', 50, 150, 70, 80, '#fff8c5'),
            ('t', 140, 200, 'Nuovo documento di testo.txt', 18, True), ('n', 140, 240, 'si vede .txt = fatto!')]),
    }
    D['caccia.svg'] = caccia_svg()
    D.pop('w-rete', None)
    return D


def caccia_svg():
    c = [S.t(360, 50, 'Caccia al guasto: 4 mosse', 20, '#1f2328', True, 'middle')]
    sotto = ['che cosa vedo?', 'che cosa può essere?', 'controllo UNA cosa', 'riparo e riprovo']
    for i, (v, s_) in enumerate(zip(['Sintomo', 'Ipotesi', 'Prova', 'Soluzione'], sotto)):
        x = 30 + i * 172
        c.append(S.r(x, 120, 150, 120, '#fff', S.BLU, 3, 10))
        c.append(f'<circle cx="{x + 22}" cy="120" r="16" fill="{S.BLU}"/>')
        c.append(S.t(x + 22, 126, str(i + 1), 16, '#fff', True, 'middle'))
        c.append(S.t(x + 75, 172, v, 19, '#1f2328', True, 'middle'))
        c.append(S.t(x + 75, 205, s_, 13, '#57606a', False, 'middle'))
        if i < 3:
            c.append(S.freccia(x + 152, 180, x + 170, 180))
    c.append(S.t(360, 300, 'La prova non funziona? Torna al passo 2 con un\'altra ipotesi.', 17, '#1f2328', True, 'middle'))
    c.append(S.t(360, 335, 'Prima di aprire il case: PC spento e spina staccata.', 17, S.ROSSO, True, 'middle'))
    return S._svg(''.join(c), 'caccia al guasto')


# ------------------------------------------------------------------ pagine
CSS = open(os.path.join(PUB, 'docs/modelli/framework-quiz/modello.html'), encoding='utf-8').read().split('<style>')[1].split('</style>')[0]
CSS += ('\n.ruoli td,.ruoli th{border:1px solid var(--bd);padding:4px 8px}.ruoli{border-collapse:collapse;margin:6px 0;width:100%}'
        '\n.campo{margin:10px 0}.campo label{display:block;font-weight:600}select{font:inherit;padding:6px;border:2px solid var(--acc);border-radius:8px;background:var(--card);color:var(--fg);max-width:100%}'
        '\n.sp label{font-weight:400;display:flex;gap:8px;align-items:flex-start;margin:4px 0}.sp input{width:22px;height:22px;flex:none}'
        '\n.ok{color:var(--ok);font-weight:700}.ko{color:#c0392b;font-weight:700}.ore a{display:block}'
        '\nbody[data-os="A"] [data-os="B"],body[data-os="B"] [data-os="A"]{display:none!important}'
        '\n.ora-card{border:3px solid var(--bd);border-radius:14px;padding:10px 14px;margin:12px 0;background:var(--card)}'
        '\n.ora-card.aperta{border-color:var(--blu)}.ora-card .st{float:right;font-size:14px;padding:3px 10px;border-radius:8px;color:#fff;background:#6e7781}'
        '\n.ora-card.aperta .st{background:var(--blu)}.ora-card.fatta{border-color:var(--ok)}.ora-card.fatta .st{background:var(--ok)}'
        '\n#ipbox .g{font-size:1.3em;font-weight:800;word-break:break-all}')


def bn(spec, s):
    return f'<p class="bn" lang="bn">{s}</p>' if spec['bn'] and s else ''


def testa(spec, titolo, data_ora=None):
    ore = f'<script src="ore.js" data-ora="{data_ora}"></script>' if data_ora else ''
    return (f'<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>{titolo}</title>{ore}<style>{CSS}</style></head>'
            f'<body data-os="A"><main>')


def html_passo(spec, p, ora):
    ex = p['extra']
    if ex == 'TEORIA':
        ex = TEORIA
    elif ex == 'IP':
        ex = ('<div id="ipbox" class="card" style="border:3px solid var(--blu)"><p>Il vostro banco: <b data-v="banco">?</b> (sceglietelo in «Chi siete?»)</p>'
              '<p>Indirizzo IP: <span class="g" data-v="ip">?</span></p><p>Subnet mask: <b data-v="maschera"></b> · Gateway: <b data-v="gateway"></b> · DNS: <b data-v="dns"></b></p></div>')
    elif ex == 'PING':
        ex = '<pre><span class="t" id="cmdping">ping (scrivi nella scheda l\'IP del PC accanto)</span></pre><p class="mu" data-os="B">In Linux Mint: menu, Terminale, stesso comando; per fermarlo premi Ctrl + C.</p>'
    elif ex == 'SCHEDA':
        ex = f'<div id="scheda" data-n="{ora}"></div><button class="bt v" id="manda" type="button">Manda al prof</button><p class="msg" id="msg"></p>' \
             '<p class="mu">Se il bottone non funziona: premilo di nuovo tra un minuto. La scheda resta salvata in questa pagina.</p>'
    os_ = f' data-os="{p["os"]}"' if p['os'] else ''
    return (f'<div class="passo" data-id="{p["id"]}"{os_}><span class="bollo">da fare</span><h2><span class="num"></span>{p["titolo"]}</h2>'
            f'<p>{p["testo"]}</p>{bn(spec, p["bn"])}{ex}<figure style="margin:8px 0"><img class="sx-img" src="img/{p["img"]}" alt="{p["titolo"]}" loading="lazy">'
            f'<figcaption class="mu" style="font-size:15px">Schema disegnato (non è uno screenshot)</figcaption></figure>'
            f'<button class="fb" type="button">Ho fatto!</button></div>')


def barra_link(spec, quiz):
    q = '<a class="bt v" data-quiz="quiz_pc" href="#" target="_blank" rel="noopener">Quiz</a>' if quiz else ''
    return (f'<div id="barra-link" style="border:3px solid #0969da;border-radius:12px;padding:6px 12px;margin:10px 0">'
            f'<a class="bt b" href="index.html">Il percorso di oggi (tutte le ore)</a>'
            f'<a class="bt b" href="{spec["cruscotto"]}" target="_blank" rel="noopener">A che punto sono</a>'
            f'<a class="bt b" href="{spec["monitor"]}" target="_blank" rel="noopener">Monitor della lezione</a>{q}'
            f'<a class="bt b" href="#aiuto">Chiedi all\'assistente</a></div>')


CHI = ('<section class="card"><h2>Chi siete?</h2><p>Scrivete i vostri nomi e il numero del banco: servono al cruscotto e alla scheda.</p>{bn}'
       '<div class="campo"><label for="nome">Il tuo nome e cognome</label><input type="text" id="nome" autocomplete="name" placeholder="Nome Cognome"></div>'
       '<div class="campo"><label for="comp1">Il compagno (nome e cognome)</label><input type="text" id="comp1" placeholder="Nome Cognome"></div>'
       '<div class="campo" id="riga-comp2"><label for="comp2">Il terzo compagno (se siete in tre)</label><input type="text" id="comp2" placeholder="Nome Cognome"></div>'
       '<div class="campo"><label for="banco">Numero del banco (PC da smontare)</label><select id="banco"></select></div>'
       '<p class="mu" id="nomeok"></p></section>')

SEI_BLOCCATO = ('<div class="aiutoprof" style="background:#fde8e8;border:3px solid #c0392b;border-radius:12px;padding:10px 12px;margin:12px 0;color:#000">'
                '<p style="font-size:1.1em"><b>Sei bloccato? Scrivi la domanda nella casella dell\'assistente in fondo alla pagina: ti risponde subito. '
                'Alza la mano solo se il PC non funziona, se un pezzo si rompe o se qualcuno si fa male.</b></p>{bn}</div>')


def pagina_ora(spec, o, conf):
    ora_id = 3 if o.get('extra') else o['n']
    passi = []
    for b in o['blocchi']:
        passi += [dict(p, id=(p['id'] if b[:6] != 'scheda' else 'scheda')) for p in P[b]]
    quiz = 'quiz' in o['blocchi']
    schedan = next((int(b[-1]) for b in o['blocchi'] if b.startswith('scheda')), None)
    lez = {'slug': f"{spec['k']}-pc-05-11-ora{ora_id}", 'classe': spec['k'].upper(), 'ora': ora_id, 'fasi': o['fasi'],
           'fasi_nomi': FASI, 'scheda': {'n': schedan, 'id': f"{spec['k']}-pc0511-ora{schedan}", **SCHEDE[schedan]} if schedan else None,
           'chiave': CHIAVE1 if schedan == 1 else {}, 'conf': conf}
    h = [testa(spec, o['titolo'], o['n']),
         f'<p class="mu">{spec["k"].upper()} · {spec["materia"]} · {spec["giorno"]} {spec["data"]} · ore {o["orario"]} · a coppie: un PC per coppia · si consegna la scheda con un bottone</p>',
         f'<h1>{o["titolo"]}</h1>', bn(spec, 'আজকের কাজ: PC খোলা, আবার জোড়া দেওয়া আর সিস্টেম চালু করা। জোড়ায় কাজ করো।'),
         '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>',
         barra_link(spec, quiz), CHI.format(bn=bn(spec, 'তোমার নাম, সঙ্গীর নাম আর বেঞ্চের নম্বর লেখো।')),
         '<section class="card"><h2>Il percorso di questa ora</h2><p>Non dovete scegliere niente: partite dal passo con il bordo blu. '
         'Ogni passo fatto: premete «Ho fatto!».</p>' + bn(spec, 'নীল বর্ডারের ধাপ থেকে শুরু করো। প্রতিটি ধাপ শেষে «Ho fatto!» চাপো।') +
         '<div class="barra"><i id="barra"></i></div><p id="conta" class="mu"></p><p id="vai"></p></section>',
         SEI_BLOCCATO.format(bn=bn(spec, 'আটকে গেলে নিচের সহকারী বাক্সে প্রশ্ন লেখো। PC কাজ না করলে, কিছু ভাঙলে বা কেউ আঘাত পেলে তবেই হাত তোলো।'))]
    h += [html_passo(spec, p, schedan) for p in passi]
    h.append('<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p><div id="aiuto"></div></main>')
    lingue = 'it'
    h.append(f'<script src="../../assistente/assistente.js" data-pagina="{lez["slug"]}" data-lingue="{lingue}" data-dove="aiuto"></script>')
    h.append(f'<script>window.LEZ={json.dumps(lez, ensure_ascii=False)};</script><script src="lezione.js"></script></body></html>\n')
    return ''.join(h)


def pagina_base(spec, conf):
    h = [testa(spec, 'Impostazioni di base', spec['base_ora']),
         f'<p class="mu">{spec["k"].upper()} · {spec["giorno"]} {spec["data"]} · 5 passi, 10 minuti · si fa sul PC che avete davanti</p>',
         '<h1>Impostazioni di base: Chrome ed estensioni dei file</h1>',
         bn(spec, 'মৌলিক সেটিং: Chrome ডিফল্ট ব্রাউজার আর ফাইলের এক্সটেনশন দেখানো।'),
         '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>',
         '<section class="card"><h2>Perché</h2><p>Un tecnico sceglie il browser giusto e vede sempre il tipo di ogni file: '
         '<b>.txt</b> è testo, <b>.jpg</b> è una foto, <b>.exe</b> è un programma. Un file «foto.jpg.exe» è un programma travestito: attenzione!</p>'
         + bn(spec, 'ফাইলের শেষের অংশ বলে ফাইলটা কী: .txt লেখা, .jpg ছবি, .exe প্রোগ্রাম। «foto.jpg.exe» আসলে প্রোগ্রাম: সাবধান!') +
         '<div class="barra"><i id="barra"></i></div><p id="conta" class="mu"></p><p id="vai"></p></section>',
         '<p data-os="B" class="card">Linux Mint: Firefox o Chrome si scelgono in <b>Applicazioni preferite</b>; le estensioni si vedono già, i file nascosti con <b>Ctrl + H</b>.</p>']
    for pid, tit, testo, img, b in BASE:
        h.append(html_passo(spec, {'id': pid, 'titolo': tit, 'testo': testo, 'img': img, 'bn': b, 'os': None, 'extra': ''}, None))
    h.append('<a class="bt" id="torna" href="index.html">Fatto: torna al percorso</a><div id="aiuto"></div></main>')
    lez = {'slug': f"{spec['k']}-pc-05-11-base", 'classe': spec['k'].upper(), 'ora': spec['base_ora'], 'fasi': [], 'fasi_nomi': FASI,
           'scheda': None, 'chiave': {}, 'conf': conf, 'senza_chi': True}
    h.append(f'<script src="../../assistente/assistente.js" data-pagina="{lez["slug"]}" data-lingue="it" data-dove="aiuto"></script>')
    h.append(f'<script>window.LEZ={json.dumps(lez, ensure_ascii=False)};</script><script src="lezione.js"></script></body></html>\n')
    return ''.join(h).replace('<section class="card"><h2>Chi siete?', '<section class="card" hidden><h2>Chi siete?')


def pagina_guasti(spec, conf):
    passi = [dict(p) for p in P['guasti'] + P['scheda_g']]
    lez = {'slug': f"{spec['k']}-pc-05-11-guasti", 'classe': spec['k'].upper(), 'ora': 'guasti', 'fasi': [], 'fasi_nomi': FASI,
           'scheda': {'n': 'G', 'id': f"{spec['k']}-pc0511-guasti", **SCHEDE['G']}, 'chiave': {}, 'conf': conf}
    h = [testa(spec, 'Caccia al guasto').replace('<style>', '<script src="flag.js" data-chiave="guasti_aperta"></script><style>', 1),
         f'<p class="mu">{spec["k"].upper()} · {spec["materia"]} · {spec["giorno"]} {spec["data"]} · a coppie · si consegna la scheda con un bottone</p>',
         '<h1>Caccia al guasto</h1>', bn(spec, 'সমস্যা খোঁজো: তোমরা টেকনিশিয়ান।'),
         '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>',
         barra_link(spec, False), CHI.format(bn=bn(spec, 'তোমার নাম, সঙ্গীর নাম আর বেঞ্চের নম্বর লেখো।')),
         '<section class="card"><h2>Il percorso</h2><p>Partite dal passo con il bordo blu. Ogni passo fatto: premete «Ho fatto!». '
         'Dopo il primo guasto il Professore ne mette un altro: rifate le mosse 1-4 e scrivete il guasto 2 nella scheda.</p>'
         '<div class="barra"><i id="barra"></i></div><p id="conta" class="mu"></p><p id="vai"></p></section>',
         SEI_BLOCCATO.format(bn=bn(spec, 'আটকে গেলে নিচের সহকারী বাক্সে প্রশ্ন লেখো।'))]
    h += [html_passo(spec, p, 'G') for p in passi]
    h.append('<a class="bt" href="index.html">Torna al percorso di oggi</a><div id="aiuto"></div></main>')
    h.append(f'<script src="../../assistente/assistente.js" data-pagina="{lez["slug"]}" data-lingue="it" data-dove="aiuto"></script>')
    h.append(f'<script>window.LEZ={json.dumps(lez, ensure_ascii=False)};</script><script src="lezione.js"></script></body></html>\n')
    return ''.join(h)


FLAG_JS = r'''/* Porta a bandierina (genera_lezione_pc.py). La pagina si vede solo se config.json ha la chiave data-chiave = true.
   Uso: <script src="flag.js" data-chiave="guasti_aperta"></script> nel <head>.
   Il docente apre: python3 strumenti/sblocca_ora.py 2inf-pc-05-11 guasti  (chiude: ... guasti-chiudi). */
(function () {
  var sc = document.currentScript, base = sc.src.replace(/[^\/]*$/, ''), k = sc.getAttribute('data-chiave') || 'aperta';
  var stile = document.createElement('style'); stile.textContent = 'main{display:none!important}'; document.head.appendChild(stile);
  function pronto(f) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', f); else f(); }
  function avviso(t) {
    pronto(function () {
      var d = document.getElementById('flag-chiuso');
      if (!d) { d = document.createElement('div'); d.id = 'flag-chiuso'; document.body.appendChild(d);
        d.style.cssText = 'max-width:640px;margin:40px auto;padding:20px 18px;border:3px solid #1f6feb;border-radius:14px;font:20px/1.5 system-ui,Arial,sans-serif;background:#fff;color:#111'; }
      d.innerHTML = '<h1 style="font-size:1.3em;margin:0 0 8px">Questa scheda non è ancora aperta</h1><p>' + t + '</p>';
    });
  }
  function controlla() {
    fetch(base + 'config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) {
      if (c && c[k] === true) { stile.remove(); var d = document.getElementById('flag-chiuso'); if (d) d.remove(); clearInterval(giro); }
      else avviso('Si apre quando il Professore la sblocca. Intanto continua l\'ora che hai davanti: questa pagina si apre da sola.');
    }).catch(function () { avviso('Non riesco a controllare se è aperta. Premi F5 fra un minuto.'); });
  }
  controlla(); var giro = setInterval(controlla, 30000);
})();
'''


def pagina_indice(spec, conf):
    carte = []
    for o in spec['ore']:
        num = 3 if o.get('extra') else o['n']
        carte.append(f'<div class="ora-card" data-ora="{o["n"]}" data-file="{o["file"]}" data-num="{num}"><span class="st">in arrivo</span>'
                     f'<h2>{o["titolo"]}</h2><p class="mu">ore {o["orario"]}</p><a class="bt" href="{o["file"]}">Apri</a></div>')
    base = (f'<div class="ora-card" data-ora="{spec["base_ora"]}" data-file="impostazioni-base.html" data-num="base"><span class="st">in arrivo</span>'
            '<h2>Impostazioni di base: Chrome ed estensioni dei file</h2><p class="mu">10 minuti</p><a class="bt" href="impostazioni-base.html">Apri</a></div>')
    if spec['base_ora'] == 1:
        carte.insert(0, base)
    else:
        carte.insert(len(carte), base)
    lez = {'slug': f"{spec['k']}-pc-05-11-indice", 'classe': spec['k'].upper(), 'ora': 0, 'fasi': [], 'fasi_nomi': FASI,
           'scheda': None, 'chiave': {}, 'conf': conf, 'indice': True}
    h = [testa(spec, 'Smonta, rimonta, installa'),
         f'<p class="mu">{spec["k"].upper()} · {spec["materia"]} · {spec["giorno"]} {spec["data"]} · a coppie</p>',
         '<h1>Smonta, rimonta e fai ripartire un PC</h1>', bn(spec, 'একটা PC খোলো, আবার জোড়া দাও আর চালু করো।'),
         '<p class="f5">La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova.</p>',
         '<section class="card"><h2>Oggi fate il lavoro di un tecnico</h2><p>Si lavora a coppie, un PC per coppia. '
         'Le ore si aprono una alla volta: quella aperta ha il bordo blu. <b id="vai-ind">Le ore non sono ancora aperte.</b></p>'
         + bn(spec, 'জোড়ায় কাজ, প্রতি জোড়ায় একটা PC। ঘণ্টাগুলো একটা একটা করে খোলে।') +
         '<p class="mu" id="info-gruppi"></p></section>', *carte,
         f'<a class="bt b" href="{spec["cruscotto"]}" target="_blank" rel="noopener">A che punto sono</a><div id="aiuto"></div></main>',
         f'<script src="../../assistente/assistente.js" data-pagina="{lez["slug"]}" data-lingue="it" data-dove="aiuto"></script>',
         f'<script>window.LEZ={json.dumps(lez, ensure_ascii=False)};</script><script src="lezione.js"></script></body></html>\n']
    return ''.join(h)


LEZIONE_JS = r'''/* Lezione «smonta, rimonta, installa» (genera_lezione_pc.py). Legge window.LEZ e config.json:
   variante_os (A Windows 10, B Linux Mint), persone_per_pc, pc_da_smontare, rete, quiz_pc, invio, attivo, ore_sbloccate. */
(function () {
  var L = window.LEZ, CONF = L.conf || {}, $ = function (i) { return document.getElementById(i); };
  function prendi(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (x) { return d; } }
  function metti(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  try { if (/[?&]pc=14\b/.test(location.search)) localStorage.setItem('pc14', '1'); if (localStorage.getItem('pc14') === '1') document.body.classList.add('pc14'); } catch (x) {}
  var KG = 'pc0511-' + L.classe, K = 'st-' + L.slug, KS = 'sch-' + L.slug;
  var G = prendi(KG, { nome: '', comp1: '', comp2: '', banco: '' }), S = prendi(K, {}), R = prendi(KS, {});
  function ipDi(b) { var r = CONF.rete || {}; return b ? (r.prefisso || '') + ((+r.primo || 0) + (+b)) : '?'; }

  /* ---------- indice: ore aperte / in arrivo, «vai qui adesso» ---------- */
  function indice() {
    var n = +CONF.ore_sbloccate || 0, primo = null;
    [].forEach.call(document.querySelectorAll('.ora-card'), function (c) {
      var aperta = n >= +c.dataset.ora, fatta = !!prendi('inviata-' + L.classe + '-' + c.dataset.num, null);
      c.classList.toggle('aperta', aperta && !fatta); c.classList.toggle('fatta', aperta && fatta);
      c.querySelector('.st').textContent = !aperta ? 'in arrivo' : fatta ? 'FATTA' : 'APERTA';
      c.querySelector('a').style.display = aperta ? '' : 'none';
      if (aperta && !fatta && !primo) primo = c;
    });
    $('vai-ind').innerHTML = primo ? 'Vai qui adesso: <a href="' + primo.dataset.file + '">' + esc(primo.querySelector('h2').textContent) + ' &rarr;</a>' : (n ? 'Hai fatto tutte le ore aperte. Bravi!' : 'Le ore non sono ancora aperte.');
    var pp = +CONF.persone_per_pc || 2;
    $('info-gruppi').textContent = 'PC da smontare oggi: ' + (CONF.pc_da_smontare || '?') + ' · persone per PC: ' + pp + ' · sistema: ' + (CONF.variante_os === 'B' ? 'Linux Mint' : 'Windows 10') + '.';
  }

  /* ---------- chi siete (a coppie, niente ruoli: docente 05/11/2026) ---------- */
  function chi() {
    if (!$('nome')) return;
    var pp = +CONF.persone_per_pc || 2, sel = $('banco'), n = +CONF.pc_da_smontare || 10, h = '<option value="">scegli</option>';
    for (var i = 1; i <= n; i++) h += '<option' + (String(i) === String(G.banco) ? ' selected' : '') + '>' + i + '</option>';
    sel.innerHTML = h; $('riga-comp2').style.display = pp >= 3 ? '' : 'none';
    $('nome').value = G.nome; $('comp1').value = G.comp1; $('comp2').value = G.comp2;
    ['nome', 'comp1', 'comp2', 'banco'].forEach(function (k) {
      $(k).addEventListener('change', function () { G[k] = $(k).value.trim().replace(/\s+/g, ' '); metti(KG, G); ruoli(); rete(); ping(true); });
    });
    ruoli();
  }
  function ruoli() {}
  function rete() {
    var r = CONF.rete || {};
    [].forEach.call(document.querySelectorAll('[data-v]'), function (e) {
      var k = e.dataset.v; e.textContent = k === 'ip' ? ipDi(G.banco) : k === 'banco' ? (G.banco || '?') : (r[k] || '');
    });
  }

  /* ---------- passi ---------- */
  var ALL = [].slice.call(document.querySelectorAll('.passo')), P = [];
  function disegna() {
    var os = CONF.variante_os === 'B' ? 'B' : 'A'; document.body.dataset.os = os;
    P = ALL.filter(function (p) { return !p.dataset.os || p.dataset.os === os; });
    var n = 0, prossimo = null;
    P.forEach(function (p) {
      p.querySelector('.num').textContent = String(++n);
      var f = !!S[p.dataset.id]; p.classList.toggle('fatto', f); p.classList.remove('ora');
      p.querySelector('.bollo').textContent = f ? 'FATTO' : 'da fare'; p.querySelector('.fb').textContent = f ? 'Fatto ✓ (clic per togliere)' : 'Ho fatto!';
      if (!f && !prossimo) prossimo = p;
    });
    if (prossimo) { prossimo.classList.add('ora'); prossimo.querySelector('.bollo').textContent = 'ADESSO'; }
    var k = P.filter(function (p) { return S[p.dataset.id]; }).length;
    if ($('barra')) $('barra').style.width = Math.round(100 * k / (P.length || 1)) + '%';
    if ($('conta')) $('conta').textContent = 'Hai fatto ' + k + ' passi su ' + P.length + (k === P.length ? ' — BRAVI, avete finito questa ora!' : '. Ti mancano ' + (P.length - k) + ' passi.');
    if ($('vai')) $('vai').innerHTML = prossimo ? 'Vai qui adesso: <a href="#" id="vai-a">passo ' + esc(prossimo.querySelector('.num').textContent) + ' · ' + esc(prossimo.querySelector('h2').textContent.replace(/^\d+/, '')) + ' &rarr;</a>' : '<a href="index.html">Torna al percorso di oggi &rarr;</a>';
    if ($('vai-a')) $('vai-a').onclick = function (e) { e.preventDefault(); prossimo.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  }
  ALL.forEach(function (p) { p.querySelector('.fb').onclick = function () { S[p.dataset.id] = !S[p.dataset.id]; metti(K, S); disegna(); ping(false); }; });

  /* ---------- scheda ---------- */
  function scheda() {
    var box = $('scheda'); if (!box || !L.scheda) return;
    var h = '<h3>' + esc(L.scheda.titolo) + '</h3>';
    L.scheda.campi.forEach(function (c) {
      var v = R[c.k];
      if (c.t === 'scelta') h += '<div class="campo"><label for="f-' + c.k + '">' + esc(c.l) + '</label><select id="f-' + c.k + '" data-k="' + c.k + '"><option value="">scegli</option>' + c.o.map(function (o) { return '<option' + (o === v ? ' selected' : '') + '>' + esc(o) + '</option>'; }).join('') + '</select> <span id="e-' + c.k + '"></span></div>';
      else if (c.t === 'testo') h += '<div class="campo"><label for="f-' + c.k + '">' + esc(c.l) + '</label><input type="text" id="f-' + c.k + '" data-k="' + c.k + '" value="' + esc(v || '') + '"></div>';
      else if (c.t === 'spunta') h += '<div class="campo sp"><label><input type="checkbox" data-k="' + c.k + '"' + (v ? ' checked' : '') + '>' + esc(c.l) + '</label></div>';
      else if (c.t === 'spunte') h += '<div class="campo sp"><b>' + esc(c.l) + '</b>' + c.o.map(function (o) { return '<label><input type="checkbox" data-k="' + c.k + '" data-o="' + esc(o) + '"' + ((v || []).indexOf(o) >= 0 ? ' checked' : '') + '>' + esc(o) + '</label>'; }).join('') + '</div>';
    });
    if (Object.keys(L.chiave).length) h += '<button class="bt b" type="button" id="controlla">Controlla le lettere</button><p id="esito-l"></p>';
    box.innerHTML = h;
    [].forEach.call(box.querySelectorAll('[data-k]'), function (e) {
      e.addEventListener('change', function () {
        var k = e.dataset.k;
        if (e.dataset.o) R[k] = [].filter.call(box.querySelectorAll('[data-k="' + k + '"]'), function (x) { return x.checked; }).map(function (x) { return x.dataset.o; });
        else R[k] = e.type === 'checkbox' ? e.checked : e.value.trim();
        metti(KS, R); if (k === 'ip_vicino') cmd();
      });
    });
    if ($('controlla')) $('controlla').onclick = function () {
      var g = 0, ks = Object.keys(L.chiave);
      ks.forEach(function (k) { var ok = R[k] === L.chiave[k]; if (ok) g++; $('e-' + k).innerHTML = R[k] ? (ok ? '<span class="ok">✔</span>' : '<span class="ko">✘ riprova</span>') : ''; });
      $('esito-l').innerHTML = '<b>Giuste: ' + g + ' su ' + ks.length + '.</b> ' + (g >= 6 ? 'Bravi! Ora mandate la scheda.' : 'Ne servono almeno 6: guardate lo schema e riprovate.');
    };
    if (L.scheda.n === 3 && !R.ip && G.banco) { R.ip = ipDi(G.banco); metti(KS, R); var f = $('f-ip'); if (f) f.value = R.ip; }
    cmd();
    $('manda').onclick = manda;
  }
  function cmd() { var c = $('cmdping'); if (c) c.textContent = R.ip_vicino ? 'ping ' + R.ip_vicino : 'ping (scrivi nella scheda l\'IP del PC accanto)'; }
  function punti() { var g = 0; Object.keys(L.chiave).forEach(function (k) { if (R[k] === L.chiave[k]) g++; }); return g; }
  function postaForm(d) {
    var f = document.createElement('form'); f.method = 'POST'; f.action = CONF.invio; f.target = '_blank'; f.acceptCharset = 'UTF-8';
    var i = document.createElement('input'); i.type = 'hidden'; i.name = 'd'; i.value = JSON.stringify(d); f.appendChild(i);
    document.body.appendChild(f); f.submit(); f.remove();
  }
  window.costruisciScheda = function () {   // esposta per la prova automatica
    var comp = [G.comp1, G.comp2].filter(function (x) { return x && x.split(' ').length >= 2; });
    return { id: L.scheda.id, modo: 'verifica', classe: L.classe, nome: G.nome, compagni: comp, banco: G.banco, ora: L.ora,
      variante_os: CONF.variante_os || 'A', risposte: R, punti_lettere: punti(), quando: new Date().toISOString() };
  };
  function manda() {
    var m = $('msg');
    if (!G.nome || G.nome.split(' ').length < 2) { m.className = 'msg ko'; m.textContent = 'Scrivi nome e cognome nel riquadro «Chi siete?» in alto.'; $('nome').focus(); return; }
    var d = window.costruisciScheda();
    if (!d.compagni.length && !confirm('Non hai scritto il nome del compagno. Mandi lo stesso?')) return;
    if (!CONF.attivo || !CONF.invio) { m.className = 'msg ko'; m.textContent = 'ANTEPRIMA: invio spento.'; return; }
    postaForm(d);
    m.className = 'msg ok'; m.textContent = 'Mandata! Si è aperta una scheda con scritto «Consegna arrivata al prof». Potete rimandarla se cambiate qualcosa: vale l\'ultima.';
    metti('inviata-' + L.classe + '-' + L.ora, new Date().toISOString());
    S.scheda = true; metti(K, S); disegna(); ping(true);
  }

  /* ---------- segnale di avanzamento (cruscotto) e quiz ---------- */
  var ultimo = '';
  function ping(forza) {
    if (!CONF.attivo || !CONF.invio || !G.nome || L.indice) return;
    var fatti = P.filter(function (p) { return S[p.dataset.id]; }).length, ch = fatti + ':' + G.banco;
    if (ch === ultimo && !forza) return; ultimo = ch;
    var d = { id: 'avz-' + L.slug, modo: 'avanzamento', classe: L.classe, nome: G.nome, compagni: [G.comp1, G.comp2].filter(Boolean), banco: G.banco,
      scheda: fatti, totale: P.length, risposte: fatti, quiz: !!S.quiz, quando: new Date().toISOString() };
    try { fetch(CONF.invio, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'd=' + encodeURIComponent(JSON.stringify(d)) }); } catch (x) {}
  }
  function quiz() {
    [].forEach.call(document.querySelectorAll('[data-quiz]'), function (a) {
      var u = (CONF[a.dataset.quiz] || '').trim(), m = document.querySelector('[data-quizmsg="' + a.dataset.quiz + '"]');
      if (u) { a.href = u; a.style.opacity = 1; a.style.pointerEvents = ''; if (m) m.textContent = ''; }
      else { a.removeAttribute('href'); a.style.opacity = .5; a.style.pointerEvents = 'none'; if (m) m.textContent = 'Il quiz non è ancora aperto: premi F5 quando il Professore lo dice.'; }
    });
  }
  [].forEach.call(document.querySelectorAll('pre'), function (pr) {
    var b = document.createElement('button'); b.className = 'cp'; b.type = 'button'; b.textContent = 'Copia';
    b.onclick = function () { var t = (pr.querySelector('.t') || pr).textContent; try { navigator.clipboard.writeText(t).then(function () { b.textContent = 'Copiato!'; }, function () { b.textContent = 'Seleziona a mano'; }); } catch (x) { b.textContent = 'Seleziona a mano'; } setTimeout(function () { b.textContent = 'Copia'; }, 1800); };
    pr.appendChild(b);
  });
  function tutto() { if (L.indice) indice(); disegna(); ruoli(); rete(); quiz(); }
  function giro() { fetch('config.json?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) { CONF = c || CONF; tutto(); }).catch(function () {}); }
  chi(); scheda(); tutto(); giro(); setInterval(giro, 30000); setInterval(function () { ping(true); }, 120000);
})();
'''


def main():
    classe = (sys.argv[1] if len(sys.argv) > 1 else '2INF').upper()
    spec = SPEC[classe]
    out = os.path.join(PUB, 'docs/anteprima', spec['cartella'])
    os.makedirs(os.path.join(out, 'img'), exist_ok=True)
    fc = os.path.join(out, 'config.json')
    base = {'invio': PONTE, 'attivo': True, 'ore_sbloccate': 0, 'variante_os': 'A', 'pc_da_smontare': 9, 'persone_per_pc': 2,
            'rete': RETE, 'quiz_pc': '',
            '_nota': f'{classe} 05/11/2026 smonta, rimonta, installa (genera_lezione_pc.py). Pagina CHIUSA finché non arriva PUBB n (R2).',
            '_ore': f'0 = tutto chiuso; con PUBB n: python3 strumenti/sblocca_ora.py {spec["cartella"]} n',
            '_variante_os': 'A = Windows 10 da chiavetta USB (deciso dal docente il 04/11/2026); B = Linux Mint da chiavetta USB',
            '_rete': 'IP del banco N = prefisso + (primo + N). Valori da confermare dal docente.',
            'guasti_aperta': False,
            '_guasti': 'pagina guasti.html (solo 2INF): false = chiusa; si apre con python3 strumenti/sblocca_ora.py <cartella> guasti'}
    try:
        conf = json.load(open(fc, encoding='utf-8'))
    except Exception:
        conf = {}
    for k, v in base.items():
        conf.setdefault(k, v)
    json.dump(conf, open(fc, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for nome, svg in disegni(conf).items():
        open(os.path.join(out, 'img', nome), 'w', encoding='utf-8').write(svg)
    pagine = {'index.html': pagina_indice(spec, conf), 'impostazioni-base.html': pagina_base(spec, conf)}
    for o in spec['ore']:
        pagine[o['file']] = pagina_ora(spec, o, conf)
    if spec.get('guasti'):
        pagine['guasti.html'] = pagina_guasti(spec, conf)
        open(os.path.join(out, 'flag.js'), 'w', encoding='utf-8').write(FLAG_JS)
    for nome, h in pagine.items():
        open(os.path.join(out, nome), 'w', encoding='utf-8').write(h)
    open(os.path.join(out, 'lezione.js'), 'w', encoding='utf-8').write(LEZIONE_JS)
    ore = open(os.path.join(PUB, 'docs/modelli/framework-quiz/ore.js'), encoding='utf-8').read()
    open(os.path.join(out, 'ore.js'), 'w', encoding='utf-8').write(ore)
    # immagini usate e presenti
    usate = {p['img'] for b in P.values() for p in b} | {x[3] for x in BASE}
    manca = sorted(u for u in usate if not os.path.exists(os.path.join(out, 'img', u)))
    if manca:
        sys.exit('MANCANO immagini: ' + ', '.join(manca))
    print(f'{classe}: {len(pagine)} pagine in docs/anteprima/{spec["cartella"]}/ (ore_sbloccate={conf["ore_sbloccate"]}, variante_os={conf["variante_os"]})')


if __name__ == '__main__':
    main()
