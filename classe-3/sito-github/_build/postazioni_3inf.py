# -*- coding: utf-8 -*-
"""Riquadro "LA TUA POSTAZIONE" della pagina unica 3INF: indicazioni personali per numero di PC.

Regole (05/10/2026, richieste da Nicola): per ogni PC prima "Fatto bene", poi "Da fare" in passi numerati e chiari;
chi ha il sito online lo vede subito (link cliccabile + anteprima, trovati in automatico da GitHub con il nome utente);
quando un ragazzo sceglie il suo PC la pagina mostra SOLO il suo riquadro (niente cose generiche che confondono).
Sulla pagina pubblica NON ci sono nomi di allievi: solo il numero del PC (e il nome utente GitHub, già pubblico nel sito).
"""
AGGIORNATO = "09:30"

# PC: (nome utente GitHub o "", fatto bene, [passi da fare], testo in bengali o "")
PC = {
    "12": ("alessandroamiciPIA", "hai caricato index.html e style.css su GitHub: hai capito come si pubblica.",
           ["I tuoi file giusti sono nel repository <b>mio-sito1</b>. Negli altri (mio-sito, mio---sito) c'è solo il README: per questo vedi 404 o la scritta \"mio-sito\".",
            "Apri il repository <b>mio-sito1</b> &rarr; <b>Settings</b> &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>.",
            "Dopo 2 minuti il tuo sito sarà su <b>.../mio-sito1/</b>: mettilo nel Documento.",
            "<b>Fallo tuo</b>: passioni e sogno sono ancora quelli dell'esempio (index.html &rarr; matita &rarr; Commit changes)."], ""),
    "14": ("rafiforhad", "hai creato il tuo repository su GitHub.",
           ["Nel repository clic su <b>Add file</b> &rarr; <b>Upload files</b>.",
            "Trascina <b>index.html</b> e <b>style.css</b> dalla cartella mio-sito. Bottone verde <b>Commit changes</b>.",
            "<b>Settings</b> &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>.",
            "Aspetta 2 minuti, poi torna qui e premi Ctrl + F5: qui sotto vedrai il tuo sito."],
           "<b>Add file</b> &rarr; <b>Upload files</b> &rarr; index.html ও style.css &rarr; <b>Commit changes</b>। তারপর <b>Settings</b> &rarr; <b>Pages</b> &rarr; <b>main</b> &rarr; <b>Save</b>। ২ মিনিট পরে এখানে Ctrl + F5: নিচে তোমার সাইট দেখবে।"),
    "15": ("tomaslous", "hai creato il repository e hai già iniziato il Documento.",
           ["<b>Il riquadro qui sotto controlla da solo</b> se il tuo sito è online (verde) oppure no (giallo).",
            "<b>Se è GIALLO:</b> nel tuo repository <b>Settings</b> (se non lo vedi: <b>More &#9662;</b>) &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Aspetta 2 minuti e premi Ctrl + F5 su questa pagina.",
            "<b>Se è VERDE:</b> <b>fallo tuo</b>: su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi passioni e sogno tuoi &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link verde qui sotto, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>."], ""),
    "18": ("danisaracino", "hai creato il repository e attivato Pages: manca solo un passo.",
           ["Nel repository <b>mio-sito</b> c'è <b>solo il README</b>: per questo il sito dà 404.",
            "Clic su <b>Aggiungi file</b> (Add file) &rarr; <b>Carica file</b> (Upload files) &rarr; trascina <b>index.html</b> e <b>style.css</b> dalla cartella mio-sito &rarr; bottone verde <b>Commit changes</b>.",
            "Aspetta 2 minuti e premi Ctrl + F5 su questa pagina: il riquadro qui sotto diventa verde."], ""),
    "22": ("", "stai salvando i file nella cartella giusta.",
           ["Salva <b>index.html</b> e <b>style.css</b> nella cartella <b>mio-sito</b> (Salva come: <b>Tutti i file</b>).",
            "Doppio clic su index.html: la tua pagina si apre nel browser.",
            "Poi passa alla <b>scheda facile 2</b> (su internet)."], ""),
    "23": ("ericcarrasco", "la tua pagina funziona, con il tuo nome, e hai già fatto lo screenshot.",
           ["Nel repository <b>mio-sito</b>: <b>Add file</b> &rarr; <b>Upload files</b> &rarr; index.html e style.css &rarr; <b>Commit changes</b>.",
            "<b>Settings</b> &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>.",
            "Aspetta 2 minuti, poi torna qui e premi Ctrl + F5: qui sotto vedrai il tuo sito."], ""),
    "24": ("", "hai il codice nel Blocco note: sei a buon punto.",
           ["Scheda facile 1, passo 5: salva come <b>index.html</b> (Tutti i file) nella cartella mio-sito.",
            "Passo 6: foglio nuovo, RIQUADRO 2, salva come <b>style.css</b>.",
            "Passo 7: doppio clic su index.html. Poi la scheda 2."], ""),
    "25": ("", "stai seguendo la scheda facile passo per passo.",
           ["Usa il <b>TUO</b> account, non quello di un compagno: il lavoro deve arrivare a tuo nome. Password dimenticata? Chiedi al professore.",
            "Intanto finisci la <b>scheda facile 1</b>: la pagina sul computer non ha bisogno di account."], ""),
    "26": ("mahmoudelkeran", "il tuo sito è online: hai fatto tutto il percorso, bravo!",
           ["<b>Il riquadro qui sotto controlla da solo</b> se il tuo sito è online (verde) oppure no (giallo).",
            "<b>Fallo tuo</b>: passioni e sogno sono ancora quelli dell'esempio. Su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi i tuoi &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link verde qui sotto, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>."], ""),
    "27": ("3infpiamartauser1", "hai recuperato l'account e pubblicato il tuo sito: bravo!",
           ["<b>Fallo tuo</b>: su GitHub apri <b>index.html</b> &rarr; matita &rarr; passioni e sogno <b>tuoi</b> &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link del sito, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot. Poi <b>Consegna</b>."], ""),
    "28": ("", "hai già aperto il compito e il Documento.",
           ["Apri la <b>scheda facile 1</b> e fai il <b>passo 1</b> adesso: la cartella mio-sito.",
            "Poi un passo alla volta: ce la fai!"], ""),
    "29": ("", "hai già aperto il compito e il Documento.",
           ["Chiudi le altre pagine.", "Apri la <b>scheda facile 1</b>: passo 1, la cartella mio-sito."], ""),
    "35": ("denisandronache", "hai caricato i file su GitHub tra i primi della classe.",
           ["<b>Il riquadro qui sotto controlla da solo</b> se il tuo sito è online (verde) oppure no (giallo).",
            "<b>Se è GIALLO:</b> nel tuo repository <b>Settings</b> (se non lo vedi: <b>More &#9662;</b>) &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Aspetta 2 minuti e premi Ctrl + F5 su questa pagina.",
            "<b>Se è VERDE:</b> <b>fallo tuo</b> (passioni e sogno sono ancora quelli dell'esempio): su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi passioni e sogno tuoi &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link verde qui sotto, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>."], ""),
    "36": ("andreagervasoniPIA", "hai caricato i file su GitHub e cambiato i colori: l'hai già fatto un po' tuo.",
           ["<b>Il riquadro qui sotto controlla da solo</b> se il tuo sito è online (verde) oppure no (giallo).",
            "<b>Se è GIALLO:</b> nel tuo repository <b>Settings</b> (se non lo vedi: <b>More &#9662;</b>) &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Aspetta 2 minuti e premi Ctrl + F5 su questa pagina.",
            "<b>Se è VERDE:</b> <b>fallo tuo</b>: su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi passioni e sogno tuoi &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link verde qui sotto, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>."], ""),
    "37": ("noahvalerio", "hai recuperato la password da solo e creato il tuo repository.",
           ["<b>Il riquadro qui sotto controlla da solo</b> se il tuo sito è online (verde) oppure no (giallo).",
            "<b>Se è GIALLO:</b> nel tuo repository <b>Settings</b> (se non lo vedi: <b>More &#9662;</b>) &rarr; <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Aspetta 2 minuti e premi Ctrl + F5 su questa pagina.",
            "<b>Se è VERDE:</b> <b>fallo tuo</b> (passioni e sogno sono ancora quelli dell'esempio): su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi passioni e sogno tuoi &rarr; <b>Commit changes</b>.",
            "Poi il Documento del compito: 1) il link verde qui sotto, 2) tutto l'HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>."], ""),
}
GENERICO = ("", "", ["Segui la <b>scheda facile 1</b> (la tua pagina sul computer), poi la <b>scheda facile 2</b> (su internet).",
                     "Se hai già finito: <b>fallo tuo</b> (passioni e sogno) e completa il Documento del compito.",
                     "Problemi? Torna alla pagina completa e guarda il riquadro giallo."],
            "প্রথমে <b>scheda facile 1</b>, তারপর <b>scheda facile 2</b>। শেষ হলে: নিজের মতো করো এবং Documento পূরণ করো।")
TUTTI = ["11", "12", "13", "14", "15", "16", "17", "18", "21", "22", "23", "24", "25", "26", "27", "28", "29",
         "31", "32", "33", "34", "35", "36", "37"]


def postazioni_html():
    bot, pan = "", ""
    for n in TUTTI:
        u, bene, passi, bn = PC.get(n, GENERICO)
        bot += "<button class='pcb%s' data-u='%s' onclick=\"pc('%s')\">PC %s</button>" % (" rosso" if n in PC else "", u, n, n)
        h = "<div class='pcp' id='pc%s' data-u='%s' style='display:none'><div class='pct'>PC %s</div>" % (n, u, n)
        if bene:
            h += "<div class='bene'><b>Fatto bene:</b> %s</div>" % bene
        h += "<div class='dafare'><b>Da fare, un passo alla volta:</b><ol>%s</ol></div>" % "".join("<li>%s</li>" % p for p in passi)
        if bn:
            h += "<div class='bnx'>%s</div>" % bn
        if u:
            h += "<div class='sito' id='sito%s'>Cerco il tuo sito su GitHub…</div>" % n
        h += "</div>"
        pan += h
    return ("<div class='box mia' style='border:3px solid #1f6fa5'><h2 style='color:#1f6fa5'>LA TUA POSTAZIONE: clicca il numero del tuo PC</h2>"
            "<p>Indicazioni personali del professore (aggiornate alle %s). Quando scegli il tuo PC vedi solo le tue cose. "
            "<b style='color:#2f9e57'>VERDE</b> = sito online · <b style='color:#c0392b'>ROSSO</b> = sito non ancora online · bianco = postazione libera.</p>"
            "<style>.pcb{background:#eaf2fb;color:#12467a;border:2px solid #1f6fa5;border-radius:10px;font-size:17px;font-weight:700;padding:8px 12px;margin:4px;cursor:pointer;width:auto}"
            ".pcb.on{outline:4px solid #12467a}.pcb.verde{background:#2f9e57;color:#fff;border-color:#1e7a44}.pcb.rosso{background:#c0392b;color:#fff;border-color:#8e2a20}.pcp{margin-top:12px;font-size:18px;line-height:1.55;background:#f4f9ff;border-radius:12px;padding:14px}"
            ".pct{font-size:24px;font-weight:800;color:#12467a}.bene{background:#eafaf0;border-left:6px solid #2f9e57;border-radius:8px;padding:8px 10px;margin:8px 0;color:#1e7a44}"
            ".dafare ol{margin:6px 0 0;padding-left:26px}.dafare li{margin:6px 0}.bnx{color:#1d4d2f;margin-top:8px;font-size:17px}"
            ".sito{margin-top:12px;background:#fff;border:2px solid #cfdbe8;border-radius:10px;padding:10px}"
            ".sito a.vai{display:block;background:#2f9e57;color:#fff;text-align:center;font-size:19px;font-weight:700;padding:12px;border-radius:10px;text-decoration:none;margin:6px 0;word-break:break-all}"
            ".sito iframe{width:100%%;height:420px;border:1px solid #cfdbe8;border-radius:8px;margin-top:6px}"
            "body.focus .w>*:not(.mia){display:none!important}#tuttapagina{display:none;background:#7a8794;width:auto}body.focus #tuttapagina{display:inline-block}</style>"
            "<div>%s</div><button id='tuttapagina' onclick='tutta()'>Torna alla pagina completa</button>%s"
            "<script>function pc(n){document.querySelectorAll('.pcp').forEach(function(e){e.style.display='none'});"
            "document.querySelectorAll('.pcb').forEach(function(b){b.classList.toggle('on',b.textContent=='PC '+n)});"
            "var p=document.getElementById('pc'+n);p.style.display='block';document.body.classList.add('focus');window.scrollTo(0,0);"
            "try{localStorage.setItem('mio-pc',n)}catch(e){}var u=p.getAttribute('data-u');if(u)cercaSito(n,u)}"
            "function tutta(){document.body.classList.remove('focus')}"
            "function mostraSito(n,url,ok){var s=document.getElementById('sito'+n);"
            "if(ok){var d=document.querySelector('#pc'+n+' .dafare');if(d)d.innerHTML='<b>Da fare, un passo alla volta:</b><ol><li><b>Fallo tuo</b>: su GitHub apri <b>index.html</b> &rarr; matita &rarr; scrivi passioni e sogno TUOI &rarr; <b>Commit changes</b>.</li><li>Completa il Documento del compito: 1) il link verde qui sotto, 2) tutto l&#39;HTML, 3) tutto il CSS a parte, 4) lo screenshot, 5) la spiegazione. Poi <b>Consegna</b>.</li></ol>';"
            "var x=document.querySelector('#pc'+n+' .bnx');if(x)x.innerHTML='<b>নিজের মতো করো</b>: index.html &rarr; পেনসিল &rarr; নিজের শখ ও স্বপ্ন &rarr; Commit changes। তারপর Documento পূরণ করে Consegna।'}"
            "s.innerHTML=(ok?'<b style=\"color:#2f9e57\">Il tuo sito è ONLINE.</b> Clicca per aprirlo, o copia il link nel Documento (parte 1):':"
            "'<b style=\"color:#a07c00\">Il sito non è ancora attivo</b> (manca Settings &rarr; Pages &rarr; main &rarr; Save, oppure aspetta 2 minuti). Il tuo indirizzo sarà:')"
            "+'<a class=\"vai\" target=\"_blank\" href=\"'+url+'\">'+url+'</a>'+(ok?'<iframe loading=\"lazy\" src=\"'+url+'?v='+Date.now()+'\"></iframe>':'')}"
            "function cercaSito(n,u){var dflt='https://'+u.toLowerCase()+'.github.io/mio-sito/';"
            "fetch('https://api.github.com/users/'+u+'/repos?per_page=100').then(function(r){return r.json()}).then(function(d){"
            "if(!d.filter){mostraSito(n,dflt,false);return}var pg=d.filter(function(r){return r.has_pages});"
            "if(pg.length){var r0=pg.filter(function(r){return /mio/i.test(r.name)})[0]||pg[0];mostraSito(n,'https://'+u.toLowerCase()+'.github.io/'+r0.name+'/',true)}"
            "else mostraSito(n,dflt,false)}).catch(function(){mostraSito(n,dflt,false)})}"
            "function colori(){var us=[].slice.call(document.querySelectorAll('.pcb')).map(function(b){return b.getAttribute('data-u')}).filter(function(u){return u});"
            "if(!us.length)return;var q=us.map(function(u){return 'user:'+u}).join(' ');"
            "fetch('https://api.github.com/search/repositories?per_page=100&q='+encodeURIComponent(q)).then(function(r){return r.json()}).then(function(j){"
            "if(!j.items)return;var on={};j.items.forEach(function(r){if(r.has_pages)on[r.owner.login.toLowerCase()]=1});"
            "document.querySelectorAll('.pcb').forEach(function(b){var u=(b.getAttribute('data-u')||'').toLowerCase();if(!u)return;"
            "if(on[u]){b.classList.remove('rosso');b.classList.add('verde')}})}).catch(function(){})}"
            "colori();setInterval(colori,3*60*1000);"
            "try{var m=localStorage.getItem('mio-pc');if(m&&document.getElementById('pc'+m))pc(m)}catch(e){}</script></div>") % (AGGIORNATO, bot, pan)


# ===================== VERSIONE SEMPLICE (09:35): UN SOLO PASSO ALLA VOLTA =====================
PASSI = [  # (italiano, bengali, copia: "" | "h" | "c")
    ("Sul <b>Desktop</b>: clic con il tasto <b>DESTRO</b> &rarr; <b>Nuovo</b> &rarr; <b>Cartella</b>. Scrivi il nome <b>mio-sito</b> e premi Invio.",
     "Desktop-এ <b>ডান</b> ক্লিক &rarr; Nuovo &rarr; Cartella। নাম লেখো <b>mio-sito</b>।", ""),
    ("Apri il <b>Blocco note</b>: in basso a sinistra <b>Start</b>, scrivi <b>Blocco note</b>, clic sul programma.",
     "<b>Blocco note</b> খোলো: Start &rarr; লেখো Blocco note।", ""),
    ("Premi il bottone giallo <b>COPIA CODICE 1</b> qui sotto. Poi nel Blocco note premi <b>Ctrl + V</b>.",
     "নিচের হলুদ বোতাম <b>COPIA CODICE 1</b> চাপো। তারপর Blocco note-এ <b>Ctrl + V</b>।", "h"),
    ("Nel Blocco note trova la parola <b>Leo</b> e scrivi al suo posto <b>il tuo nome</b>.",
     "<b>Leo</b> খুঁজে তার জায়গায় <b>তোমার নাম</b> লেখো।", ""),
    ("<b>File</b> &rarr; <b>Salva con nome</b> &rarr; apri la cartella <b>mio-sito</b>. In basso <b>Salva come: Tutti i file</b>. Nome: <b>index.html</b>. Clic su <b>Salva</b>.",
     "<b>File</b> &rarr; <b>Salva con nome</b> &rarr; <b>mio-sito</b> ফোল্ডার। <b>Tutti i file</b>। নাম: <b>index.html</b>। <b>Salva</b>।", ""),
    ("Nel Blocco note: <b>File</b> &rarr; <b>Nuovo</b>. Premi il bottone giallo <b>COPIA CODICE 2</b> qui sotto, poi <b>Ctrl + V</b>.",
     "<b>File</b> &rarr; <b>Nuovo</b>। হলুদ বোতাম <b>COPIA CODICE 2</b> চাপো, তারপর <b>Ctrl + V</b>।", "c"),
    ("<b>File</b> &rarr; <b>Salva con nome</b> &rarr; cartella <b>mio-sito</b> &rarr; <b>Tutti i file</b>. Nome: <b>style.css</b>. Clic su <b>Salva</b>.",
     "<b>File</b> &rarr; <b>Salva con nome</b> &rarr; <b>mio-sito</b> &rarr; <b>Tutti i file</b>। নাম: <b>style.css</b>। <b>Salva</b>।", ""),
    ("Apri la cartella <b>mio-sito</b> e fai <b>doppio clic su index.html</b>. Vedi la tua pagina colorata? <b>BRAVO!</b>",
     "<b>mio-sito</b> ফোল্ডারে <b>index.html</b>-এ ডাবল ক্লিক। রঙিন পেজ দেখছ? <b>দারুণ!</b>", ""),
    ("Apri una scheda nuova e vai su <b>github.com</b>. In alto a destra <b>Sign in</b>: entra con il tuo nome utente e password.",
     "নতুন ট্যাবে <b>github.com</b>। উপরে ডানদিকে <b>Sign in</b>: ইউজারনেম ও পাসওয়ার্ড।", ""),
    ("In alto a destra clic sul <b>+</b> &rarr; <b>New repository</b>. Nome: <b>mio-sito</b>. <b>Add README</b> su <b>On</b>. Bottone verde <b>Create repository</b>.",
     "উপরে ডানদিকে <b>+</b> &rarr; <b>New repository</b>। নাম <b>mio-sito</b>। <b>Add README: On</b>। সবুজ <b>Create repository</b>।", ""),
    ("Clic su <b>Add file</b> &rarr; <b>Upload files</b>. Trascina <b>index.html</b> e <b>style.css</b> dalla cartella mio-sito. Bottone verde <b>Commit changes</b>.",
     "<b>Add file</b> &rarr; <b>Upload files</b>। <b>index.html</b> ও <b>style.css</b> টেনে আনো। সবুজ <b>Commit changes</b>।", ""),
    ("Clic su <b>Settings</b> (in alto, ultima a destra; se non c'è: <b>More</b> &rarr; Settings) &rarr; a sinistra <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>.",
     "<b>Settings</b> (না দেখলে <b>More</b>) &rarr; বাঁদিকে <b>Pages</b> &rarr; <b>main</b> &rarr; <b>Save</b>।", ""),
    ("Aspetta <b>2 minuti</b>. Poi torna su questa pagina e premi <b>Ctrl + F5</b>: se il tuo PC diventa <b>VERDE</b> il sito è online!",
     "<b>২ মিনিট</b> অপেক্ষা করো। তারপর এই পেজে <b>Ctrl + F5</b>: তোমার PC <b>সবুজ</b> হলে সাইট অনলাইন!", ""),
    ("<b>Fallo tuo</b>: su GitHub apri <b>index.html</b> &rarr; <b>matita</b> &rarr; cambia passioni e sogno con i <b>tuoi</b> &rarr; <b>Commit changes</b>.",
     "<b>নিজের মতো করো</b>: GitHub-এ <b>index.html</b> &rarr; পেনসিল &rarr; নিজের শখ ও স্বপ্ন &rarr; <b>Commit changes</b>।", ""),
    ("Su <b>Classroom</b> apri il compito, metti nel Documento il <b>link del tuo sito</b>, e premi <b>Consegna</b>. Il professore poi ti fa qualche domanda.",
     "<b>Classroom</b>-এ কাজ খোলো, Documento-তে <b>সাইটের লিংক</b> দাও, <b>Consegna</b> চাপো।", ""),
]
# passo (numero da 1) da cui parte ogni postazione, alle 09:35
INIZIO = {"12": 12, "14": 14, "15": 14, "18": 11, "22": 11, "23": 14, "24": 5, "25": 1, "26": 14, "27": 14,
          "28": 9, "29": 1, "32": 1, "33": 5, "34": 5, "35": 14, "36": 14, "37": 14}
NOTE = {"12": "I tuoi file giusti sono nel repository <b>mio-sito1</b>: fai questo passo dentro <b>mio-sito1</b>.",
        "18": "Nel tuo repository c'è solo il README: manca questo passo.",
        "29": "<b>Oggi fai solo la tua pagina sul computer</b> (passi da 1 a 8). Un passo alla volta: quando hai fatto premi FATTO. A pubblicarla su internet ti aiuta il professore.",
        "32": "<b>Oggi fai solo la tua pagina sul computer</b> (passi da 1 a 8). Un passo alla volta: quando hai fatto premi FATTO. A pubblicarla su internet ti aiuta il professore.",
        "33": "Stai usando l'account di un compagno: esci e entra con il <b>TUO</b> (chiedi al professore)."}


def postazioni_semplici_html():
    import json as _j
    bot = ""
    for n in TUTTI:
        u = PC.get(n, GENERICO)[0]
        cls = " rosso" if n in PC or n in INIZIO else ""
        bot += "<button class='pcb%s' data-u='%s' onclick=\"pc('%s')\">PC %s</button>" % (cls, u, n, n)
    dati = {"passi": PASSI, "inizio": INIZIO, "note": NOTE,
            "bene": {n: PC[n][1] for n in PC}, "user": {n: PC[n][0] for n in PC}}
    return ("<div class='box mia' style='border:3px solid #1f6fa5'><h2 style='color:#1f6fa5'>LA TUA POSTAZIONE: clicca il numero del tuo PC</h2>"
            "<p><b style='color:#2f9e57'>VERDE</b> = sito online · <b style='color:#c0392b'>ROSSO</b> = non ancora · bianco = postazione libera.</p>"
            "<style>.pcb{background:#eaf2fb;color:#12467a;border:2px solid #1f6fa5;border-radius:10px;font-size:17px;font-weight:700;padding:8px 12px;margin:4px;cursor:pointer;width:auto}"
            ".pcb.on{outline:4px solid #12467a}.pcb.verde{background:#2f9e57;color:#fff;border-color:#1e7a44}.pcb.rosso{background:#c0392b;color:#fff;border-color:#8e2a20}"
            "#passo{display:none;margin-top:14px}.pnum{font-size:20px;font-weight:800;color:#12467a}.bene2{background:#eafaf0;border-left:6px solid #2f9e57;border-radius:8px;padding:8px 10px;margin:8px 0;color:#1e7a44;font-size:17px}"
            ".nota2{background:#fff8e1;border-left:6px solid #d0a516;border-radius:8px;padding:8px 10px;margin:8px 0;font-size:17px}"
            ".ptesto{font-size:24px;line-height:1.5;background:#f4f9ff;border:3px solid #1f6fa5;border-radius:14px;padding:16px;margin:8px 0}"
            ".pbn{font-size:20px;color:#1d4d2f;margin-top:8px}.cpb{background:#ffd34d;color:#1a2330;font-size:22px;font-weight:800;border-radius:12px;padding:14px;width:100%%;margin-top:10px}"
            ".avanti{background:#2f9e57;font-size:22px;padding:16px}.indietro{background:#7a8794;font-size:16px;width:auto;padding:10px 14px}"
            ".barra{height:12px;background:#e3e9f0;border-radius:6px;overflow:hidden;margin:6px 0}.barra div{height:100%%;background:#2f9e57}"
            "body.focus .w>*:not(.mia){display:none!important}#tuttapagina{display:none;background:#7a8794;width:auto}body.focus #tuttapagina{display:inline-block}</style>"
            "<div>%s</div><button id='tuttapagina' onclick='tutta()'>Torna alla pagina completa</button>"
            "<div id='passo'><div class='pnum' id='pnum'></div><div class='barra'><div id='pbar'></div></div><div id='pbene'></div><div id='pnota'></div>"
            "<div class='ptesto' id='ptesto'></div><div id='pcopia'></div>"
            "<button class='avanti' onclick='muovi(1)'>FATTO &rarr; passo dopo</button> <button class='indietro' onclick='muovi(-1)'>&larr; passo prima</button>"
            "<div id='psito' style='margin-top:12px'></div></div>"
            "<script>var D=%s,PCN=null,P=0;"
            "function chiave(){return 'passo-pc-'+PCN}"
            "function pc(n){PCN=n;document.querySelectorAll('.pcb').forEach(function(b){b.classList.toggle('on',b.textContent=='PC '+n)});"
            "document.body.classList.add('focus');document.getElementById('passo').style.display='block';"
            "var s=null;try{s=localStorage.getItem(chiave())}catch(e){}P=s?parseInt(s):((D.inizio[n]||1)-1);"
            "document.getElementById('pbene').innerHTML=D.bene[n]?'<div class=\"bene2\"><b>Fatto bene:</b> '+D.bene[n]+'</div>':'';"
            "try{localStorage.setItem('mio-pc',n)}catch(e){}disegna();var u=D.user[n];if(u)controllaUno(u)}"
            "function disegna(){var t=D.passi[P];document.getElementById('pnum').textContent='PC '+PCN+' — passo '+(P+1)+' di '+D.passi.length;"
            "document.getElementById('pbar').style.width=Math.round((P+1)*100/D.passi.length)+'%%';"
            "document.getElementById('ptesto').innerHTML=t[0]+'<div class=\"pbn\">'+t[1]+'</div>';"
            "var no=D.note[PCN];document.getElementById('pnota').innerHTML=no&&(P+1)==(D.inizio[PCN]||1)?'<div class=\"nota2\">'+no+'</div>':'';"
            "document.getElementById('pcopia').innerHTML=t[2]?'<button class=\"cpb\" onclick=\"copiaCodice(\\''+t[2]+'\\',this)\">COPIA CODICE '+(t[2]=='h'?'1 (index.html)':'2 (style.css)')+'</button>':'';"
            "window.scrollTo(0,0)}"
            "function muovi(d){P=Math.max(0,Math.min(D.passi.length-1,P+d));try{localStorage.setItem(chiave(),P)}catch(e){}disegna()}"
            "function copiaCodice(id,b){var t=document.getElementById(id).textContent;function ok(){b.textContent='COPIATO! Ora Ctrl + V nel Blocco note'}"
            "if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){fb(t);ok()})}else{fb(t);ok()}}"
            "function tutta(){document.body.classList.remove('focus');document.getElementById('passo').style.display='none'}"
            "function controllaUno(u){fetch('https://api.github.com/users/'+u+'/repos?per_page=100').then(function(r){return r.json()}).then(function(d){"
            "if(!d.filter)return;var pg=d.filter(function(r){return r.has_pages});var el=document.getElementById('psito');"
            "if(pg.length){var r0=pg.filter(function(r){return /mio/i.test(r.name)})[0]||pg[0];var url='https://'+u.toLowerCase()+'.github.io/'+r0.name+'/';"
            "el.innerHTML='<b style=\"color:#2f9e57;font-size:20px\">IL TUO SITO È ONLINE:</b><a target=\"_blank\" href=\"'+url+'\" style=\"display:block;background:#2f9e57;color:#fff;font-size:20px;font-weight:700;padding:12px;border-radius:10px;text-decoration:none;text-align:center;margin-top:6px;word-break:break-all\">'+url+'</a>';"
            "if(P<13){P=13;disegna()}}}).catch(function(){})}"
            "function colori(){var us=[].slice.call(document.querySelectorAll('.pcb')).map(function(b){return b.getAttribute('data-u')}).filter(function(u){return u});"
            "if(!us.length)return;fetch('https://api.github.com/search/repositories?per_page=100&q='+encodeURIComponent(us.map(function(u){return 'user:'+u}).join(' '))).then(function(r){return r.json()}).then(function(j){"
            "if(!j.items)return;var on={};j.items.forEach(function(r){if(r.has_pages)on[r.owner.login.toLowerCase()]=1});"
            "document.querySelectorAll('.pcb').forEach(function(b){var u=(b.getAttribute('data-u')||'').toLowerCase();if(u&&on[u]){b.classList.remove('rosso');b.classList.add('verde')}})}).catch(function(){})}"
            "colori();setInterval(colori,3*60*1000);try{var m=localStorage.getItem('mio-pc');if(m)pc(m)}catch(e){}</script></div>") % (bot, _j.dumps(dati, ensure_ascii=False))


def siti_classe_html():
    """Riquadro 'I SITI DELLA CLASSE': lista generata dal vivo (solo numero del PC + bottone, niente nomi scritti)."""
    import json as _j
    us = {n: PC[n][0] for n in PC if PC[n][0]}
    return ("<div class='box' id='sitiClasse' style='border:3px solid #2f9e57'><h2 style='color:#2f9e57'>I SITI DELLA CLASSE: clicca il tuo PC</h2>"
            "<p>La lista si crea da sola: compare il bottone appena il sito è online. Il tuo PC non c'è? Riquadro blu qui sotto, un passo alla volta.</p>"
            "<div id='listaSiti' style='display:flex;flex-wrap:wrap;gap:8px'>Controllo i siti su GitHub...</div>"
            "<script>(function(){var U=%s;function giro(){var q=Object.keys(U).map(function(n){return 'user:'+U[n]}).join(' ');"
            "fetch('https://api.github.com/search/repositories?per_page=100&q='+encodeURIComponent(q)).then(function(r){return r.json()}).then(function(j){"
            "if(!j.items)return;var by={};j.items.forEach(function(r){if(!r.has_pages)return;var o=r.owner.login.toLowerCase();if(!by[o]||/mio/i.test(r.name))by[o]=r.name});"
            "var h='';Object.keys(U).sort(function(a,b){return a-b}).forEach(function(n){var o=U[n].toLowerCase();if(by[o])"
            "h+='<a target=\"_blank\" href=\"https://'+o+'.github.io/'+by[o]+'/\" style=\"background:#2f9e57;color:#fff;font-weight:800;font-size:18px;padding:12px 16px;border-radius:10px;text-decoration:none\">PC '+n+' &rarr; apri il sito</a>'});"
            "document.getElementById('listaSiti').innerHTML=h||'Ancora nessun sito online.'}).catch(function(){})}giro();setInterval(giro,3*60*1000)})();</script></div>") % _j.dumps(us)
