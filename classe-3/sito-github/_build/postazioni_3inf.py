# -*- coding: utf-8 -*-
"""Riquadro "LA TUA POSTAZIONE" della pagina unica 3INF: indicazioni personali per numero di PC.

Regole (05/10/2026, richieste da Nicola): per ogni PC prima "Fatto bene", poi "Da fare" in passi numerati e chiari;
chi ha il sito online lo vede subito (link cliccabile + anteprima, trovati in automatico da GitHub con il nome utente);
quando un ragazzo sceglie il suo PC la pagina mostra SOLO il suo riquadro (niente cose generiche che confondono).
Sulla pagina pubblica NON ci sono nomi di allievi: solo il numero del PC (e il nome utente GitHub, già pubblico nel sito).
"""
AGGIORNATO = "08:55"

# PC: (nome utente GitHub o "", fatto bene, [passi da fare], testo in bengali o "")
PC = {
    "12": ("alessandroamiciPIA", "hai già creato il repository e caricato dei file: hai capito come si pubblica.",
           ["Su GitHub hai <b>3 repository</b>: usa solo quello che si chiama <b>mio-sito</b>.",
            "Dentro <b>mio-sito</b> clic su <b>Add file</b> &rarr; <b>Upload files</b> e carica <b>index.html</b> e <b>style.css</b> (i file, non la cartella). Bottone verde <b>Commit changes</b>.",
            "<b>Settings</b> &rarr; a sinistra <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Custom domain: lascia vuoto.",
            "Aspetta 2 minuti, poi torna qui e premi Ctrl + F5: qui sotto vedrai il tuo sito."], ""),
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
    "18": ("danisaracino", "hai recuperato: ora lavori su GitHub con il tuo repository.",
           ["Nel repository <b>mio-sito</b>: <b>Settings</b> (se non lo vedi: <b>More &#9662;</b>).",
            "A sinistra <b>Pages</b> &rarr; Branch: <b>main</b> &rarr; <b>Save</b>. Custom domain: lascia vuoto.",
            "Aspetta 2 minuti, poi torna qui e premi Ctrl + F5: qui sotto vedrai il tuo sito. Ci sei quasi!"], ""),
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
    "26": ("", "hai aperto la pagina del corso: il primo passo è fatto.",
           ["Apri la <b>scheda facile 1</b> (riquadro arancione qui sopra: torna alla pagina completa).",
            "Passo 1: sul Desktop, tasto destro &rarr; Nuovo &rarr; Cartella &rarr; <b>mio-sito</b>.",
            "Continua un passo alla volta: in 20 minuti hai la tua pagina!"], ""),
    "27": ("", "vai avanti con la scheda anche senza account: bravo.",
           ["Finisci la <b>scheda facile 1</b>: la pagina sul tuo computer.",
            "Il tuo account è in recupero: appena funziona, fai la <b>scheda facile 2</b>."], ""),
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
        bot += "<button class='pcb' onclick=\"pc('%s')\">PC %s</button>" % (n, n)
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
            "<p>Indicazioni personali del professore (aggiornate alle %s). Quando scegli il tuo PC vedi solo le tue cose.</p>"
            "<style>.pcb{background:#eaf2fb;color:#12467a;border:2px solid #1f6fa5;border-radius:10px;font-size:17px;font-weight:700;padding:8px 12px;margin:4px;cursor:pointer;width:auto}"
            ".pcb.on{background:#1f6fa5;color:#fff}.pcp{margin-top:12px;font-size:18px;line-height:1.55;background:#f4f9ff;border-radius:12px;padding:14px}"
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
            "s.innerHTML=(ok?'<b style=\"color:#2f9e57\">Il tuo sito è ONLINE.</b> Clicca per aprirlo, o copia il link nel Documento (parte 1):':"
            "'<b style=\"color:#a07c00\">Il sito non è ancora attivo</b> (manca Settings &rarr; Pages &rarr; main &rarr; Save, oppure aspetta 2 minuti). Il tuo indirizzo sarà:')"
            "+'<a class=\"vai\" target=\"_blank\" href=\"'+url+'\">'+url+'</a>'+(ok?'<iframe loading=\"lazy\" src=\"'+url+'\"></iframe>':'')}"
            "function cercaSito(n,u){var dflt='https://'+u.toLowerCase()+'.github.io/mio-sito/';"
            "fetch('https://api.github.com/users/'+u+'/repos?per_page=100').then(function(r){return r.json()}).then(function(d){"
            "if(!d.filter){mostraSito(n,dflt,false);return}var pg=d.filter(function(r){return r.has_pages});"
            "if(pg.length){var r0=pg.filter(function(r){return /mio/i.test(r.name)})[0]||pg[0];mostraSito(n,'https://'+u.toLowerCase()+'.github.io/'+r0.name+'/',true)}"
            "else mostraSito(n,dflt,false)}).catch(function(){mostraSito(n,dflt,false)})}"
            "try{var m=localStorage.getItem('mio-pc');if(m&&document.getElementById('pc'+m))pc(m)}catch(e){}</script></div>") % (AGGIORNATO, bot, pan)
