# -*- coding: utf-8 -*-
"""2INF — riquadro 'IL GIOCO PASSO PASSO' (Indovina il numero in Lazarus) nella pagina docs/2inf-if/.
Un passo alla volta, bottone FATTO, bottoni gialli per copiare nomi e codice. Si rigenera: python3 gen_passo_passo.py"""
import json, html, os, re
HUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "docs", "2inf-if", "index.html")
A = "  segreto: Integer;     // il numero pensato dal computer\n  tentativi: Integer;   // quante prove hai fatto"
B = "  Randomize;                     // mescola i numeri a caso\n  segreto := Random(100) + 1;    // un numero da 1 a 100\n  tentativi := 0;"
C = """procedure TForm1.ButtonProvaClick(Sender: TObject);
var
  numero: Integer;
begin
  numero := StrToInt(EditNumero.Text);
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
  EditNumero.Clear;
end;"""
D = """procedure TForm1.ButtonNuovaClick(Sender: TObject);
begin
  segreto := Random(100) + 1;
  tentativi := 0;
  LabelRisposta.Caption := 'Ho pensato un nuovo numero da 1 a 100';
end;"""
A = "  segreto: Integer;     // il numero pensato dal computer\n  tentativi: Integer;   // quante prove hai fatto"
B = "  Randomize;                     // mescola i numeri a caso\n  segreto := Random(100) + 1;    // un numero da 1 a 100\n  tentativi := 0;"
C = """procedure TForm1.ButtonProvaClick(Sender: TObject);
var
  numero: Integer;
begin
  numero := StrToInt(EditNumero.Text);
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
  EditNumero.Clear;
end;"""
D = """procedure TForm1.ButtonNuovaClick(Sender: TObject);
begin
  segreto := Random(100) + 1;
  tentativi := 0;
  LabelRisposta.Caption := 'Ho pensato un nuovo numero da 1 a 100';
end;"""
COPIE2 = {"k1": "indovina", "k2": "Ho pensato un numero da 1 a 100. Quale?", "k3": "EditNumero", "k4": "ButtonProva", "k5": "Prova",
         "k6": "ButtonNuova", "k7": "Nuova partita", "k8": "LabelRisposta", "cA": A, "cB": B, "cC": C, "cD": D}
LAB2 = {"k1": "COPIA IL NOME: indovina", "k2": "COPIA LA FRASE", "k3": "COPIA: EditNumero", "k4": "COPIA: ButtonProva", "k5": "COPIA: Prova",
       "k6": "COPIA: ButtonNuova", "k7": "COPIA: Nuova partita", "k8": "COPIA: LabelRisposta", "cA": "COPIA IL CODICE A (2 righe)",
       "cB": "COPIA IL CODICE B (FormCreate)", "cC": "COPIA IL CODICE C (bottone Prova)", "cD": "COPIA IL CODICE D (Nuova partita)"}
P2 = [
    ('Apri <b>Lazarus</b>. In alto, menu <b>Progetto</b> &rarr; <b>Nuovo progetto</b> &rarr; scegli <b>Applicazione</b> &rarr; <b>OK</b>. Compare una Form vuota.', ''),
    ('Salva subito: menu <b>File</b> &rarr; <b>Salva tutto</b>. Nella finestra, nel pannello <b>a sinistra</b>, clicca <b>Documenti</b> (NON la cartella di Lazarus o Programmi). Lì crea una cartella nuova con il nome qui sotto (bottone giallo, poi Ctrl + V), entra nella cartella e premi <b>Salva</b> due volte (unit1 e project1).', 'k1'),
    ("In alto, nella tavolozza <b>Standard</b>, clicca il componente <b>TLabel</b> (l'icona con la A), poi clicca sulla Form in alto. Nell'<b>Ispettore</b> a sinistra, alla voce <b>Caption</b>, incolla questa frase:", 'k2'),
    ("Metti sulla Form una <b>TEdit</b> (la casella di testo). Nell'Ispettore, alla voce <b>Name</b>, incolla il nome qui sotto. Poi alla voce <b>Text</b> cancella tutto.", 'k3'),
    ("Metti un <b>TButton</b>. Nell'Ispettore, alla voce <b>Name</b>, incolla:", 'k4'),
    ('Sempre su questo bottone, alla voce <b>Caption</b> incolla:', 'k5'),
    ('Metti un secondo <b>TButton</b>. Alla voce <b>Name</b> incolla:', 'k6'),
    ('Sempre sul secondo bottone, alla voce <b>Caption</b> incolla:', 'k7'),
    ('Metti una seconda <b>TLabel</b>, sotto i bottoni. Alla voce <b>Name</b> incolla il nome qui sotto. Poi alla voce <b>Font</b> (tre puntini) scegli un carattere <b>grande</b> e un colore che ti piace.', 'k8'),
    ('Premi <b>F12</b>: vedi il codice. Cerca la riga <b>Form1: TForm1;</b> (in alto, sotto <b>var</b>). Clicca alla fine di quella riga, premi <b>Invio</b> e incolla queste 2 righe:', 'cA'),
    ('Premi <b>F12</b> per tornare alla Form. Fai <b>doppio clic su un punto VUOTO</b> della Form: nasce <b>FormCreate</b> con begin ed end. Clicca nella riga vuota tra <b>begin</b> ed <b>end</b> e incolla:', 'cB'),
    ("Torna alla Form (F12) e fai <b>doppio clic sul bottone Prova</b>. Lazarus scrive la procedura vuota <b>ButtonProvaClick</b>. Seleziona tutta la procedura, dalla riga <b>procedure</b> fino al suo <b>end;</b>, e incolla al suo posto questa (il cuore del gioco, con l'<b>if annidato</b>):", 'cC'),
    ('Torna alla Form (F12) e fai <b>doppio clic sul bottone Nuova partita</b>. Seleziona la procedura vuota <b>ButtonNuovaClick</b> (da procedure a end;) e incolla al suo posto:', 'cD'),
    ("Premi <b>F9</b>: il gioco parte! Scrivi un numero e premi Prova, finché vedi <b>Troppo BASSO</b>, <b>Troppo ALTO</b> e <b>Indovinato</b>. <b>FATTO: hai fatto un gioco!</b> Errore su <b>else</b>? Guarda l'end subito prima: NON deve avere il <b>;</b>.", ''),
    ('<b>Fallo tuo</b>: cambia la Caption della Form (il titolo della finestra), le frasi tra apici (anche spiritose) e i colori. Poi fallo provare a un compagno: chi indovina con meno tentativi?', ''),
    ("<b>Salva il gioco su GitHub, in un repository NUOVO.</b> In Lazarus: <b>File</b> &rarr; <b>Salva tutto</b>. Su github.com: in alto a destra <b>+</b> &rarr; <b>New repository</b>; nel riquadro <b>Repository name</b> incolla il nome qui sotto; <b>Add README</b> su <b>On</b>; verde <b>Create repository</b>.", "k1"),
    ("Nel repository <b>indovina</b> clicca <b>Add file</b> &rarr; <b>Upload files</b> &rarr; la scritta blu <b>choose your files</b>.", ""),
    ("Nella finestra, a sinistra <b>Documenti</b>, doppio clic sulla cartella <b>indovina</b>, premi <b>Ctrl + A</b> e clicca <b>Apri</b>. In fondo alla pagina verde <b>Commit changes</b>. Il primo programma resta intatto nel repository <b>lazarus</b>.", ""),
    ("Su <b>Classroom</b> apri il compito <b>Lazarus — Indovina il numero con gli if annidati</b>: nel Documento metti 3 screenshot (Troppo BASSO, Troppo ALTO, Indovinato), perché serve un if dentro un altro if, cosa non hai capito. Poi <b>Consegna</b>.", ""),
]
# 05/10 ore 11:45 (Nicola): obiettivo di oggi = PUBBLICARE SU GITHUB. Programma semplicissimo da copiare; gli if annidati dopo.
FRASE = "  Label1.Caption := 'Ciao! Questo è il mio primo programma su GitHub';"
COPIE = {"cF": FRASE, "kR": "lazarus", "kU": "unit1.pas", "kF": '"unit1.pas" "unit1.lfm" "project1.lpi" "project1.lpr"'}
COPIE.update(COPIE2)
LAB = {"cF": "COPIA IL CODICE (1 riga)", "kR": "COPIA IL NOME: lazarus", "kU": "COPIA IL NOME: unit1.pas", "kF": "COPIA I NOMI DEI 4 FILE"}
LAB.update(LAB2)
P = [
    ("<b>PARTE 1 — IL PROGRAMMA (5 minuti).</b> Apri <b>Lazarus</b>. In alto, menu <b>Progetto</b> &rarr; <b>Nuovo progetto</b> &rarr; <b>Applicazione</b> &rarr; <b>OK</b>. Poi SUBITO menu <b>File</b> &rarr; <b>Salva tutto</b>: nella finestra, a sinistra, clicca <b>Documenti</b>; in alto clicca <b>Nuova cartella</b> e incolla il nome qui sotto (bottone giallo, poi Ctrl + V); entra nella cartella con doppio clic e premi <b>Salva</b> due volte.", "kR"),
    ("In alto, nella tavolozza <b>Standard</b>, clicca il componente <b>TButton</b> (il bottone). Poi clicca sulla Form: compare il bottone.", ""),
    ("Nella tavolozza <b>Standard</b> clicca il componente <b>TLabel</b> (l'icona con la A). Poi clicca sulla Form, sotto il bottone.", ""),
    ("Fai <b>doppio clic sul bottone</b>. Si apre il codice: il cursore è tra <b>begin</b> ed <b>end</b>.", ""),
    ("Premi il bottone giallo qui sotto. Poi in Lazarus, nella riga vuota tra <b>begin</b> ed <b>end</b>, premi <b>Ctrl + V</b>.", "cF"),
    ("Premi <b>F9</b>: il programma parte. Clicca il bottone: compare la frase. <b>FATTO: il tuo primo programma!</b> Chiudi la finestra del programma. <br><small><b>Se compare &quot;Impossibile creare la cartella ... AppData&quot;:</b> premi Annulla; menu <b>Strumenti</b> &rarr; <b>Opzioni</b> &rarr; a sinistra <b>Ambiente</b> &rarr; alla riga <b>Cartella per costruire progetti di test</b> clicca il bottone <b>...</b> a destra &rarr; scegli <b>Documenti</b> &rarr; <b>Seleziona cartella</b> &rarr; <b>Ok</b>. Poi di nuovo F9.</small>", ""),
    ("<b>Fallo tuo:</b> nel codice cambia la frase tra gli apici con una <b>TUA</b> (per esempio con il tuo nome). Premi F9 e prova.", ""),
    ("<b>PARTE 2 — SU GITHUB.</b> In Lazarus: menu <b>File</b> &rarr; <b>Salva tutto</b>. Così i file del programma sono salvati nei tuoi <b>Documenti</b>.", ""),
    ("Apri una scheda nuova del browser (<b>Ctrl + T</b>), vai su <b>github.com</b> ed entra con il <b>TUO</b> account. Non ce l'hai? <b>Alza la mano</b>.", ""),
    ("<b>In alto a destra</b> clicca il simbolo <b>+</b> (più), poi <b>New repository</b>.", ""),
    ("Premi il bottone giallo qui sotto. Poi clicca nel riquadro <b>Repository name</b> e premi <b>Ctrl + V</b>.", "kR"),
    ("Metti <b>Add README</b> su <b>On</b>. In fondo clicca il bottone <b>VERDE</b> <b>Create repository</b>.", ""),
    ("Nel tuo repository, sopra l'elenco dei file, clicca <b>Add file</b> e poi <b>Upload files</b> (carica file).", ""),
    ("Nella pagina c'è un grande riquadro tratteggiato. Clicca la scritta blu <b>choose your files</b> (scegli i file): si apre la finestra per scegliere i file del computer.", ""),
    ("Nella finestra, a sinistra, clicca <b>Documenti</b> e fai doppio clic sulla cartella <b>lazarus</b>. Premi <b>Ctrl + A</b> (seleziona tutti i file del tuo programma) e clicca <b>Apri</b>. Va bene anche se i file hanno nomi diversi da project1.", ""),
    ("Aspetta che i 4 file compaiano nell'elenco. In fondo alla pagina clicca il bottone <b>VERDE</b> <b>Commit changes</b>. <b>FATTO: il tuo programma è su GitHub!</b>", ""),
    ("Ultimo passo: clicca il file <b>README.md</b>, poi la <b>matita</b> in alto a destra. Scrivi con parole tue: cosa ho fatto oggi, cosa non ho capito. Poi verde <b>Commit changes</b> (2 volte).", ""),
    ("Su <b>Classroom</b>, nel compito <b>Lazarus — Il mio primo programma pubblicato su GitHub</b>, premi il bottone blu <b>Consegna</b>. Il codice lo prende il professore da GitHub. <b>FINE DEL COMPITO 1!</b> Premi FATTO per il compito 2.", ""),
]
P[len(P):] = [("<b>COMPITO 2 — INDOVINA IL NUMERO (if annidati)</b>, per chi ha finito il compito 1. " + P2[0][0], P2[0][1])] + P2[1:]
pre = "".join("<pre id='%s' hidden>%s</pre>" % (k, html.escape(v)) for k, v in COPIE.items())
BOX = ("<!--PASSO-->"
       "<div class='box mia' style='border:3px solid #1f6fa5'><h2 style='color:#1f6fa5'>OGGI: IL MIO PRIMO PROGRAMMA SU GITHUB — un passo alla volta</h2>"
       "<p>Leggi il passo, fallo, poi premi il bottone verde <b>FATTO</b>. Nomi e codice si copiano con i bottoni gialli: niente da scrivere a mano.</p>"
       "<style>#pn{font-size:20px;font-weight:800;color:#12467a}.barra{height:12px;background:#e3e9f0;border-radius:6px;overflow:hidden;margin:6px 0}.barra div{height:100%;background:#2f9e57}"
       "#pt{font-size:22px;line-height:1.5;background:#f4f9ff;border:3px solid #1f6fa5;border-radius:14px;padding:16px;margin:8px 0}"
       ".cpb{background:#ffd34d;color:#1a2330;font-size:20px;font-weight:800;border:0;border-radius:12px;padding:14px;width:100%;margin-top:8px;cursor:pointer}"
       ".av{background:#2f9e57;color:#fff;font-size:22px;font-weight:700;border:0;border-radius:12px;padding:14px 18px;cursor:pointer}.ind{background:#7a8794;color:#fff;font-size:16px;border:0;border-radius:10px;padding:10px 14px;cursor:pointer}"
       "#pcod{background:#1e1e1e;color:#e6e6e6;font-family:Consolas,monospace;font-size:14px;border-radius:10px;padding:10px;white-space:pre;overflow:auto;margin-top:8px}</style>"
       "<div id='pn'></div><div class='barra'><div id='pb'></div></div><div id='pt'></div><div id='pc'></div><pre id='pcod' hidden></pre>"
       "<button class='av' onclick='mv(1)'>FATTO &rarr; passo dopo</button> <button class='ind' onclick='mv(-1)'>&larr; passo prima</button> <button class='ind' onclick='mv(-99)'>ricomincia</button>"
       + pre +
       "<script>var PS=__PS__,LB=__LB__,P=0;try{var n=localStorage.getItem('passo-2inf-github'),o=localStorage.getItem('passo-2inf-indovina');"
       "if(n===null&&o!==null&&parseInt(o)>0){P=18+Math.min(parseInt(o),14);localStorage.setItem('passo-2inf-github',P)}else P=parseInt(n||'0')||0}catch(e){}"
       "function dis(){var t=PS[P];document.getElementById('pn').textContent='Passo '+(P+1)+' di '+PS.length;document.getElementById('pb').style.width=Math.round((P+1)*100/PS.length)+'%';"
       "document.getElementById('pt').innerHTML=t[0];var c=document.getElementById('pc'),k=document.getElementById('pcod');"
       "if(t[1]){c.innerHTML='<button class=\"cpb\" onclick=\"cp(\\''+t[1]+'\\',this)\">'+LB[t[1]]+'</button>';if(t[1][0]=='c'){k.hidden=false;k.textContent=document.getElementById(t[1]).textContent}else k.hidden=true}else{c.innerHTML='';k.hidden=true}}"
       "function mv(d){P=Math.max(0,Math.min(PS.length-1,d==-99?0:P+d));try{localStorage.setItem('passo-2inf-github',P)}catch(e){}dis()}"
       "function cp(id,b){var t=document.getElementById(id).textContent;function ok(){b.textContent='COPIATO! Ora clicca dove serve e premi Ctrl + V'}"
       "if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){fb(t);ok()})}else{fb(t);ok()}}"
       "function fb(t){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}dis();</script></div>"
       "<!--/PASSO-->").replace("__PS__", json.dumps(P, ensure_ascii=False)).replace("__LB__", json.dumps(LAB, ensure_ascii=False))
s = open(HUB, encoding="utf-8").read()
s = re.sub(r"<!--PASSO-->.*?<!--/PASSO-->", "", s, flags=re.S)
s = s.replace('<span class="ver">v1.0</span>', '<span class="ver">v1.1</span>')
a = '<div class="box b1"><h2>1. Dispensa'
s = s.replace("<!--IFDOPO", BOX + "<!--IFDOPO", 1) if "<!--IFDOPO" in s else s.replace(a, BOX + a, 1)
i = s.find(a); j = s.find('<!--DOPO')
if i > 0 and j > i and '<!--IFDOPO' not in s:      # gli if annidati si fanno dopo: oggi nascosti
    s = s[:i] + '<!--IFDOPO\n' + s[i:j].replace('-->', '--&gt;') + '\n-->' + s[j:]
open(HUB, "w", encoding="utf-8").write(s)
print("ok", len(P), "passi")
