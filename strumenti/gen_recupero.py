# -*- coding: utf-8 -*-
"""RECUPERO A FIANCO — pagine semplificate per rifare un esercizio con il docente accanto.

Per chi è andato male (voto sotto 60 o lavoro non svolto). Regole delle pagine (audit 05/10):
  1. una sola azione per passo;
  2. in alto il PROGRAMMA in cui si lavora (colore fisso: Lazarus blu, Windows grigio, GitHub nero, ...);
  3. sotto ogni passo "ADESSO DEVI VEDERE" (così il ragazzo sa se l'ha fatto bene);
  4. "NON MI TORNA": il rimedio all'errore tipico di quel passo;
  5. numero del passo GRANDE (si legge dalla miniatura di Veyon);
  6. bottone "tutti i passi" per il docente (vista d'insieme e stampa).
Niente nomi di allievi (pagine pubbliche). Genera docs/recupero/<slug>/index.html e docs/recupero/index.html.
Uso: python3 strumenti/gen_recupero.py
"""
import html, json, os

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "recupero")
VERS = "1.0"
APP = {"LAZARUS": "#1f6fa5", "WINDOWS": "#5b6470", "GITHUB": "#111", "BROWSER": "#7a4fb5",
       "PROGRAMMA": "#2f9e57", "CLASSROOM": "#1e8a3e", "PROF": "#c0392b"}

APPDATA = ("Se compare \"Impossibile creare la cartella ... AppData\": premi Annulla. Menu Strumenti → Opzioni → a sinistra Ambiente "
           "→ riga \"Cartella per costruire progetti di test\" → bottone ... → Documenti → Seleziona cartella → Ok. Poi di nuovo F9.")


def nuovo_progetto(cartella):
    return [
        ("LAZARUS", "Apri Lazarus.", "", "La finestra di Lazarus.", "Non lo trovi? Chiama il prof."),
        ("LAZARUS", "In alto clicca il menu Progetto, poi Nuovo progetto.", "", "Una finestra con un elenco.", ""),
        ("LAZARUS", "Nell'elenco clicca Applicazione, poi il bottone OK.", "", "Una finestra grigia vuota con i puntini: è la Form.", "Ti chiede di salvare il progetto vecchio? Clicca No."),
        ("LAZARUS", "In alto clicca il menu File, poi Salva tutto.", "", "La finestra di Windows per salvare.", ""),
        ("WINDOWS", "Nel pannello a sinistra clicca Documenti.", "", "In alto, nel percorso, c'è scritto Documenti.", "Non vedi Documenti? Cerca Questo PC, poi Documenti."),
        ("WINDOWS", "In alto clicca Nuova cartella.", "", "Una cartella nuova, con il nome colorato di blu.", ""),
        ("WINDOWS", "Premi il bottone giallo. Poi premi Ctrl + V e Invio.", cartella, "La cartella si chiama " + cartella + ".", "Hai scritto un altro nome? Clic destro sulla cartella → Rinomina."),
        ("WINDOWS", "Fai doppio clic sulla cartella " + cartella + ".", "", "La cartella è vuota.", ""),
        ("WINDOWS", "Clicca il bottone Salva.", "", "Si apre di nuovo la finestra per salvare.", ""),
        ("WINDOWS", "Clicca ancora il bottone Salva.", "", "Sei tornato alla Form di Lazarus.", ""),
    ]


def su_github(repo, cartella):
    return [
        ("BROWSER", "Apri una scheda nuova con Ctrl + T. Premi il bottone giallo, poi Ctrl + V e Invio.", "github.com", "La pagina di GitHub. In alto a destra c'è il tuo tondino.", "Non sei entrato con il tuo account? Chiama il prof."),
        ("GITHUB", "In alto a destra clicca il simbolo + (più).", "", "Un piccolo menu.", ""),
        ("GITHUB", "Clicca New repository (nuovo repository).", "", "Una pagina con la casella Repository name.", ""),
        ("GITHUB", "Clicca nella casella Repository name. Premi il bottone giallo, poi Ctrl + V.", repo, "Accanto al nome compare un segno verde.", "Scritta rossa \"already exists\"? Il repository c'è già: chiama il prof, si va direttamente al passo con Add file."),
        ("GITHUB", "Metti l'interruttore Add README su On.", "", "L'interruttore è acceso (colorato).", ""),
        ("GITHUB", "In fondo alla pagina clicca il bottone VERDE Create repository.", "", "La pagina del tuo repository, con il file README.md.", ""),
        ("GITHUB", "Sopra l'elenco dei file clicca Add file.", "", "Un piccolo menu.", ""),
        ("GITHUB", "Clicca Upload files (carica file).", "", "Un grande riquadro tratteggiato.", ""),
        ("GITHUB", "Clicca la scritta blu choose your files (scegli i file).", "", "La finestra di Windows per scegliere i file.", ""),
        ("WINDOWS", "Nel pannello a sinistra clicca Documenti.", "", "Le tue cartelle, tra cui " + cartella + ".", ""),
        ("WINDOWS", "Fai doppio clic sulla cartella " + cartella + ".", "", "I file del programma: unit1, project1 e altri.", "La cartella è vuota? Il programma è salvato altrove: chiama il prof."),
        ("WINDOWS", "Premi Ctrl + A.", "", "Tutti i file diventano blu.", ""),
        ("WINDOWS", "Clicca il bottone Apri.", "", "Su GitHub compare l'elenco dei file che si caricano.", ""),
        ("GITHUB", "Aspetta che l'elenco sia completo. Poi in fondo clicca il bottone VERDE Commit changes.", "", "Il repository con i tuoi file, tra cui unit1.pas. FATTO: è su GitHub!", ""),
    ]


README = [
    ("GITHUB", "Clicca il file README.md.", "", "Il file README aperto.", ""),
    ("GITHUB", "In alto a destra del file clicca la matita.", "", "Puoi scrivere nel file.", ""),
    ("GITHUB", "Scrivi 2 righe con parole tue: cosa ho fatto oggi, cosa ho imparato.", "", "Le tue 2 righe sotto il titolo.", ""),
    ("GITHUB", "Clicca il bottone VERDE Commit changes. Nella finestrella clicca di nuovo Commit changes.", "", "Il README con le tue righe.", ""),
]

ESERCIZI = {}

ESERCIZI["2inf-github"] = {
    "titolo": "Recupero — Il mio primo programma su GitHub",
    "classe": "Classe 2 · Lazarus",
    "domande": ["Cosa succede quando clicchi il bottone? Quale riga lo fa succedere? Cosa vuol dire Caption?",
                "Cos'è un repository e perché ci mettiamo il programma?",
                "Quale file contiene il codice che hai scritto?"],
    "parti": [
        ("A — Il programma", nuovo_progetto("lazarus") + [
            ("LAZARUS", "In alto, nella tavolozza Standard, clicca TButton (il bottone con scritto OK).", "", "Il pulsante TButton è premuto.", ""),
            ("LAZARUS", "Clicca su un punto della Form.", "", "Sulla Form c'è un bottone Button1.", ""),
            ("LAZARUS", "Nella tavolozza Standard clicca TLabel (l'icona con la A).", "", "Il pulsante TLabel è premuto.", ""),
            ("LAZARUS", "Clicca sulla Form, sotto il bottone.", "", "Sulla Form c'è la scritta Label1.", ""),
            ("LAZARUS", "Fai doppio clic sul bottone Button1.", "", "Il codice. Il cursore lampeggia tra begin ed end.", ""),
            ("LAZARUS", "Premi il bottone giallo. Poi in Lazarus premi Ctrl + V.", "Label1.Caption := 'Ciao! Questo è il mio primo programma su GitHub';", "La riga Label1.Caption tra begin ed end.", ""),
            ("LAZARUS", "Tra gli apici ' ' cambia la frase: scrivi una frase TUA, con il tuo nome.", "", "La tua frase tra i due apici.", "Hai cancellato un apice? Ogni frase deve iniziare e finire con '."),
            ("LAZARUS", "Premi F9.", "", "Si apre la finestra Form1 con il bottone.", APPDATA),
            ("PROGRAMMA", "Clicca il bottone Button1.", "", "Al posto di Label1 compare la tua frase. FATTO: il tuo programma funziona!", ""),
            ("PROGRAMMA", "Chiudi la finestra del programma con la X in alto a destra.", "", "Sei tornato al codice in Lazarus.", ""),
            ("LAZARUS", "In alto clicca il menu File, poi Salva tutto.", "", "Niente cambia: il programma è salvato.", ""),
        ]),
        ("B — Su GitHub", su_github("lazarus", "lazarus") + README),
        ("C — Spiegalo", [("PROF", "Chiama il prof e spiegagli con parole tue cosa hai fatto.", "", "Il prof ti fa 3 domande. FATTO: recupero completato!", "")]),
    ],
}

AV = "segreto: Integer;\n  tentativi: Integer;\n  numero: Integer;"
BV = "Randomize;\n  segreto := Random(100) + 1;\n  tentativi := 0;"
CV = """numero := StrToInt(EditNumero.Text);
  tentativi := tentativi + 1;
  if numero = segreto then
    begin
      LabelRisposta.Caption := 'Indovinato! Tentativi: ' + IntToStr(tentativi);
    end
  else
    begin
      if numero < segreto then
        begin
          LabelRisposta.Caption := 'Troppo BASSO: prova un numero più grande';
        end
      else
        begin
          LabelRisposta.Caption := 'Troppo ALTO: prova un numero più piccolo';
        end;
    end;
  EditNumero.Clear;"""
DV = "segreto := Random(100) + 1;\n  tentativi := 0;\n  LabelRisposta.Caption := 'Ho pensato un nuovo numero da 1 a 100';"


def componente(nome_lazarus, cosa, name, caption=None, extra=None):
    p = [("LAZARUS", "Nella tavolozza Standard clicca " + nome_lazarus + " (" + cosa + "). Poi clicca su un punto vuoto della Form.", "", "Sulla Form c'è il nuovo componente, selezionato.", ""),
         ("LAZARUS", "Nell'Ispettore a sinistra, alla riga Name, clicca il valore. Premi il bottone giallo, poi Ctrl + V e Invio.", name, "Alla riga Name c'è scritto " + name + ".", "Non vedi l'Ispettore? Menu Finestra → Ispettore oggetti.")]
    if caption:
        p.append(("LAZARUS", "Alla riga Caption clicca il valore. Premi il bottone giallo, poi Ctrl + V e Invio.", caption, "Sul componente c'è scritto " + caption + ".", ""))
    if extra:
        p.append(extra)
    return p


ESERCIZI["2inf-indovina"] = {
    "titolo": "Recupero — Indovina il numero (if annidati)",
    "classe": "Classe 2 · Lazarus",
    "domande": ["Perché servono due if, uno dentro l'altro?",
                "Cosa fa la riga segreto := Random(100) + 1?",
                "Cosa succede se metti il ; prima di else?"],
    "parti": [
        ("A — La Form", nuovo_progetto("indovina")
         + componente("TEdit", "la casella di testo", "EditNumero", extra=("LAZARUS", "Alla riga Text cancella tutto e premi Invio.", "", "La casella sulla Form è vuota.", ""))
         + componente("TButton", "il bottone", "ButtonProva", "Prova")
         + componente("TButton", "il bottone", "ButtonNuova", "Nuova partita")
         + componente("TLabel", "l'icona con la A", "LabelRisposta")),
        ("B — Il codice", [
            ("LAZARUS", "Premi F12.", "", "Il codice.", "Vedi ancora la Form? Premi di nuovo F12."),
            ("LAZARUS", "Cerca la riga Form1: TForm1; (in alto, sotto var). Clicca alla FINE di quella riga.", "", "Il cursore lampeggia dopo il ;", ""),
            ("LAZARUS", "Premi Invio. Poi premi il bottone giallo e in Lazarus Ctrl + V.", AV, "Sotto Form1: TForm1; ci sono le 3 righe nuove.", ""),
            ("LAZARUS", "Premi F12 per tornare alla Form.", "", "La Form con i componenti.", ""),
            ("LAZARUS", "Fai doppio clic su un punto VUOTO della Form (non sui componenti).", "", "Il codice di FormCreate. Il cursore è tra begin ed end.", "Si è aperto il codice di un bottone? Premi Ctrl + Z, F12 e riprova su un punto vuoto."),
            ("LAZARUS", "Premi il bottone giallo, poi in Lazarus Ctrl + V.", BV, "Le 3 righe dentro FormCreate.", ""),
            ("LAZARUS", "Premi F12. Fai doppio clic sul bottone Prova.", "", "Il codice di ButtonProvaClick. Il cursore è tra begin ed end.", ""),
            ("LAZARUS", "Premi il bottone giallo, poi in Lazarus Ctrl + V.", CV, "Il cuore del gioco: un if dentro un altro if.", ""),
            ("LAZARUS", "Premi F12. Fai doppio clic sul bottone Nuova partita.", "", "Il codice di ButtonNuovaClick. Il cursore è tra begin ed end.", ""),
            ("LAZARUS", "Premi il bottone giallo, poi in Lazarus Ctrl + V.", DV, "Le 3 righe dentro ButtonNuovaClick.", ""),
            ("LAZARUS", "Premi F9.", "", "Il gioco parte.", "Errore su else? Guarda l'end subito prima: NON deve avere il ;. " + APPDATA),
            ("PROGRAMMA", "Scrivi un numero da 1 a 100 e premi Prova. Continua finché vedi Troppo BASSO, Troppo ALTO e Indovinato.", "", "FATTO: hai fatto un gioco!", ""),
            ("LAZARUS", "Fallo tuo: chiudi il gioco e cambia le frasi tra gli apici con frasi TUE. Poi F9 e prova.", "", "Il gioco con le tue frasi.", ""),
            ("LAZARUS", "In alto clicca il menu File, poi Salva tutto.", "", "Il gioco è salvato.", ""),
        ]),
        ("C — Su GitHub", su_github("indovina", "indovina")),
        ("D — Spiegalo", [("PROF", "Chiama il prof e spiegagli con parole tue perché ci sono due if.", "", "Il prof ti fa 3 domande. FATTO: recupero completato!", "")]),
    ],
}

ESERCIZI["3inf-sito"] = {
    "titolo": "Recupero — Il mio sito: fallo tuo e README",
    "classe": "Classe 3 · HTML",
    "domande": ["Cosa fa il tag <li>? E <h2>?",
                "Dove si cambia il colore: nel file HTML o nel CSS?",
                "Cosa succede al sito quando premi Commit changes?"],
    "parti": [
        ("A — Fallo tuo", [
            ("BROWSER", "Apri una scheda nuova con Ctrl + T. Premi il bottone giallo, poi Ctrl + V e Invio.", "github.com", "GitHub. In alto a destra c'è il tuo tondino.", "Non sei entrato con il tuo account? Chiama il prof."),
            ("GITHUB", "A sinistra, nell'elenco dei tuoi repository, clicca quello del sito.", "", "I file del sito: index.html e style.css.", "Non lo trovi? In alto a destra clicca il tondino → Your repositories."),
            ("GITHUB", "Clicca il file index.html.", "", "Il codice della pagina.", ""),
            ("GITHUB", "In alto a destra del file clicca la matita.", "", "Puoi scrivere nel codice.", ""),
            ("GITHUB", "Cerca le righe con <li>. Cambia Calcio, Videogiochi, Musica con 3 passioni TUE.", "", "Tre righe <li> con le tue passioni.", "Hai cancellato < o >? Ogni riga deve essere <li>...</li>."),
            ("GITHUB", "Sotto Il mio sogno cambia la frase con il TUO sogno.", "", "<p>il tuo sogno</p>", ""),
            ("GITHUB", "Clicca il bottone VERDE Commit changes. Nella finestrella clicca di nuovo Commit changes.", "", "Il file index.html con le tue parole.", ""),
        ]),
        ("B — README", [
            ("GITHUB", "Torna alla pagina del repository: clicca il suo nome in alto.", "", "L'elenco dei file.", ""),
            ("GITHUB", "Clicca Add file, poi Create new file (se il README c'è già, clicca README.md e poi la matita).", "", "Una pagina per scrivere un file.", ""),
            ("GITHUB", "Nella casella del nome premi il bottone giallo, poi Ctrl + V.", "README.md", "Il nome del file è README.md.", ""),
            ("GITHUB", "Scrivi 3 righe tue: cosa ho fatto, cosa non avevo fatto la prima volta, cosa ho imparato.", "", "Le tue 3 righe.", ""),
            ("GITHUB", "Clicca il bottone VERDE Commit changes. Nella finestrella clicca di nuovo Commit changes.", "", "Il README nell'elenco dei file.", ""),
            ("BROWSER", "Apri il tuo sito (il tuo indirizzo .github.io) e premi Ctrl + F5.", "", "Il sito con le tue passioni e il tuo sogno. Può servire 1 minuto.", "Vedi ancora quelle vecchie? Aspetta 1 minuto e premi di nuovo Ctrl + F5."),
        ]),
        ("C — Spiegalo", [("PROF", "Chiama il prof e mostragli il sito: spiegagli cosa hai cambiato.", "", "Il prof ti fa 3 domande. FATTO: recupero completato!", "")]),
    ],
}

PAGINA = """<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><title>%(titolo)s</title>
<style>
:root{--blu:#12467a;--bg:#f4f7fb;--txt:#1a2330}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font-family:"Segoe UI",Arial,sans-serif}
.w{max-width:820px;margin:0 auto;padding:14px 16px 60px}h1{color:var(--blu);font-size:24px;margin:6px 0 2px}.sub{color:#556;margin-bottom:10px}
.lingue{font-size:15px;color:#334;background:#fff;border-radius:10px;padding:8px 12px;margin:8px 0}.ar{direction:rtl;text-align:right}
.parti{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}.parti button{font-size:14px;padding:6px 10px;border:2px solid #9cc0e4;background:#fff;color:var(--blu);border-radius:8px;cursor:pointer}
.parti button.on{background:var(--blu);color:#fff;border-color:var(--blu)}
.card{background:#fff;border-radius:16px;padding:18px;box-shadow:0 1px 5px rgba(0,0,0,.1)}
.top{display:flex;align-items:center;gap:12px;flex-wrap:wrap}.n{font-size:44px;font-weight:900;color:var(--blu);min-width:70px}
.app{color:#fff;font-weight:800;font-size:18px;padding:6px 14px;border-radius:999px;letter-spacing:1px}
.parte{color:#556;font-size:14px}.testo{font-size:22px;line-height:1.45;margin:14px 0}
.vedi{background:#eafaf0;border-left:6px solid #2f9e57;padding:10px 12px;border-radius:8px;font-size:18px;margin:10px 0}
.vedi b{color:#1e7a43}.copia{display:block;width:100%%;background:#ffd23f;color:#222;font-size:19px;font-weight:800;border:0;border-radius:12px;padding:12px;margin:8px 0;cursor:pointer}
pre{white-space:pre-wrap;background:#f6f6f6;border-radius:8px;padding:8px;font-size:14px;margin:4px 0}
details{margin:8px 0;font-size:17px}summary{cursor:pointer;color:#c0392b;font-weight:800}
.bar{height:12px;background:#e3e9f0;border-radius:6px;overflow:hidden;margin:10px 0}.bar div{height:100%%;background:#2f9e57}
.nav{display:flex;gap:8px;margin-top:12px}.nav button{flex:1;font-size:20px;font-weight:800;border:0;border-radius:12px;padding:14px;cursor:pointer}
.fatto{background:#2f9e57;color:#fff}.indietro{background:#dfe6ee;color:#223}
.tutti{margin-top:18px;font-size:14px}.tutti button{background:none;border:0;color:var(--blu);text-decoration:underline;cursor:pointer;font-size:14px}
#elenco{display:none}#elenco.on{display:block}#elenco ol{padding-left:24px}#elenco li{margin:6px 0}
.ver{color:#889;font-size:12px;margin-top:16px}
@media print{.card,.nav,.parti,.tutti button{display:none}#elenco{display:block}}
</style></head><body><div class="w">
<h1>%(titolo)s</h1><div class="sub">%(classe)s · il prof è accanto a te · un passo alla volta</div>
<div class="lingue">Leggi il passo, fallo, guarda se vedi quello che è scritto in verde, poi premi FATTO.
<div class="ar">اقرأ الخطوة، نفّذها، تحقّق من الجملة الخضراء، ثم اضغط FATTO. الأستاذ بجانبك.</div>
<div>读一步,做一步,看绿色的句子是否一样,然后点 FATTO。老师在你旁边。</div></div>
<div class="parti" id="parti"></div>
<div class="card"><div class="top"><span class="n" id="num"></span><span class="app" id="app"></span><span class="parte" id="parte"></span></div>
<div class="bar"><div id="bar"></div></div>
<div class="testo" id="testo"></div><div id="cp"></div>
<div class="vedi"><b>ADESSO DEVI VEDERE:</b> <span id="vedi"></span></div>
<details id="aiuto"><summary>NON MI TORNA</summary><div id="aiutot"></div></details>
<div class="nav"><button class="indietro" onclick="vai(-1)">&larr; indietro</button><button class="fatto" onclick="vai(1)">FATTO &rarr;</button></div></div>
<div class="tutti"><button onclick="document.getElementById('elenco').classList.toggle('on')">Tutti i passi (per il prof · stampa)</button></div>
<div id="elenco"></div>
<div class="ver">Versione %(vers)s</div>
</div>
<script>
var P=%(passi)s,COL=%(col)s,K="recupero-%(slug)s",i=0;
try{i=parseInt(localStorage.getItem(K)||"0")||0}catch(e){}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function mostra(){if(i<0)i=0;if(i>=P.length)i=P.length-1;var p=P[i];
 document.getElementById("num").textContent=(i+1)+"/"+P.length;
 var a=document.getElementById("app");a.textContent=p.app;a.style.background=COL[p.app]||"#333";
 document.getElementById("parte").textContent="Parte "+p.parte;
 document.getElementById("bar").style.width=Math.round(100*(i+1)/P.length)+"%%";
 document.getElementById("testo").textContent=p.t;
 document.getElementById("cp").innerHTML=p.c?'<button class="copia" onclick="copia()">COPIA (bottone giallo)</button><pre>'+esc(p.c)+'</pre>':"";
 document.getElementById("vedi").textContent=p.v;
 var h=document.getElementById("aiuto");h.style.display=p.h?"block":"none";h.open=false;document.getElementById("aiutot").textContent=p.h;
 document.querySelectorAll("#parti button").forEach(function(b){b.classList.toggle("on",b.dataset.p==p.parte)});
 try{localStorage.setItem(K,i)}catch(e){}}
function vai(d){i+=d;mostra();window.scrollTo(0,0)}
function copia(){var t=P[i].c;try{navigator.clipboard.writeText(t).then(function(){alert("Copiato! Ora Ctrl + V")})}catch(e){var x=document.createElement("textarea");x.value=t;document.body.appendChild(x);x.select();document.execCommand("copy");x.remove();alert("Copiato! Ora Ctrl + V")}}
var parti=[],h="";P.forEach(function(p,k){if(parti.indexOf(p.parte)<0){parti.push(p.parte);h+='<button data-p="'+p.parte+'" onclick="i='+k+';mostra()">Parte '+esc(p.parte)+'</button>'}});
document.getElementById("parti").innerHTML=h;
var e="<h2>Tutti i passi</h2>",cur="";P.forEach(function(p,k){if(p.parte!=cur){if(cur)e+="</ol>";cur=p.parte;e+="<h3>Parte "+esc(cur)+"</h3><ol start='"+(k+1)+"'>"}
 e+="<li><b>["+p.app+"]</b> "+esc(p.t)+(p.c?"<pre>"+esc(p.c)+"</pre>":"")+"<br><i>Devi vedere:</i> "+esc(p.v)+"</li>"});
document.getElementById("elenco").innerHTML=e+"</ol><h3>Domande del prof (prova del nove)</h3><ol>%(domande)s</ol>";
mostra();
</script></body></html>"""


def genera():
    os.makedirs(DOCS, exist_ok=True)
    righe = []
    for slug, ex in ESERCIZI.items():
        passi = [{"parte": nome, "app": a, "t": t, "c": c, "v": v, "h": h} for nome, lista in ex["parti"] for a, t, c, v, h in lista]
        d = os.path.join(DOCS, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(PAGINA % {
            "titolo": html.escape(ex["titolo"]), "classe": html.escape(ex["classe"]), "slug": slug, "vers": VERS,
            "passi": json.dumps(passi, ensure_ascii=False), "col": json.dumps(APP),
            "domande": "".join("<li>%s</li>" % html.escape(q) for q in ex["domande"])})
        righe.append((slug, ex["titolo"], len(passi)))
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(
        "<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Recupero a fianco</title>"
        "<style>body{font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#1a2330;max-width:760px;margin:0 auto;padding:16px}"
        "a{display:block;background:#fff;border-radius:12px;padding:14px;margin:10px 0;font-size:20px;color:#12467a;text-decoration:none;box-shadow:0 1px 4px rgba(0,0,0,.08)}</style>"
        "<h1>Recupero a fianco</h1><p>Rifai l'esercizio con il prof accanto, un passo alla volta.</p>"
        + "".join("<a href='%s/'>%s <small>(%d passi)</small></a>" % (s, html.escape(t), n) for s, t, n in righe))
    for r in righe:
        print("%-15s %-50s %d passi" % r)


if __name__ == "__main__":
    genera()
