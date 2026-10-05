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
COPIE = {"k1": "indovina", "k2": "Ho pensato un numero da 1 a 100. Quale?", "k3": "EditNumero", "k4": "ButtonProva", "k5": "Prova",
         "k6": "ButtonNuova", "k7": "Nuova partita", "k8": "LabelRisposta", "cA": A, "cB": B, "cC": C, "cD": D}
LAB = {"k1": "COPIA IL NOME DELLA CARTELLA", "k2": "COPIA LA FRASE", "k3": "COPIA: EditNumero", "k4": "COPIA: ButtonProva", "k5": "COPIA: Prova",
       "k6": "COPIA: ButtonNuova", "k7": "COPIA: Nuova partita", "k8": "COPIA: LabelRisposta", "cA": "COPIA IL CODICE A (2 righe)",
       "cB": "COPIA IL CODICE B (FormCreate)", "cC": "COPIA IL CODICE C (bottone Prova)", "cD": "COPIA IL CODICE D (Nuova partita)"}
P = [
    ("Apri <b>Lazarus</b>. In alto, menu <b>Progetto</b> &rarr; <b>Nuovo progetto</b> &rarr; scegli <b>Applicazione</b> &rarr; <b>OK</b>. Compare una Form vuota.", ""),
    ("Salva subito: menu <b>File</b> &rarr; <b>Salva tutto</b>. Nella finestra crea una cartella nuova con il nome qui sotto (bottone giallo, poi Ctrl + V), entra nella cartella e premi <b>Salva</b> due volte (unit1 e project1).", "k1"),
    ("In alto, nella tavolozza <b>Standard</b>, clicca il componente <b>TLabel</b> (l'icona con la A), poi clicca sulla Form in alto. Nell'<b>Ispettore</b> a sinistra, alla voce <b>Caption</b>, incolla questa frase:", "k2"),
    ("Metti sulla Form una <b>TEdit</b> (la casella di testo). Nell'Ispettore, alla voce <b>Name</b>, incolla il nome qui sotto. Poi alla voce <b>Text</b> cancella tutto.", "k3"),
    ("Metti un <b>TButton</b>. Nell'Ispettore, alla voce <b>Name</b>, incolla:", "k4"),
    ("Sempre su questo bottone, alla voce <b>Caption</b> incolla:", "k5"),
    ("Metti un secondo <b>TButton</b>. Alla voce <b>Name</b> incolla:", "k6"),
    ("Sempre sul secondo bottone, alla voce <b>Caption</b> incolla:", "k7"),
    ("Metti una seconda <b>TLabel</b>, sotto i bottoni. Alla voce <b>Name</b> incolla il nome qui sotto. Poi alla voce <b>Font</b> (tre puntini) scegli un carattere <b>grande</b> e un colore che ti piace.", "k8"),
    ("Premi <b>F12</b>: vedi il codice. Cerca la riga <b>Form1: TForm1;</b> (in alto, sotto <b>var</b>). Clicca alla fine di quella riga, premi <b>Invio</b> e incolla queste 2 righe:", "cA"),
    ("Premi <b>F12</b> per tornare alla Form. Fai <b>doppio clic su un punto VUOTO</b> della Form: nasce <b>FormCreate</b> con begin ed end. Clicca nella riga vuota tra <b>begin</b> ed <b>end</b> e incolla:", "cB"),
    ("Torna alla Form (F12) e fai <b>doppio clic sul bottone Prova</b>. Lazarus scrive la procedura vuota <b>ButtonProvaClick</b>. Seleziona tutta la procedura, dalla riga <b>procedure</b> fino al suo <b>end;</b>, e incolla al suo posto questa (il cuore del gioco, con l'<b>if annidato</b>):", "cC"),
    ("Torna alla Form (F12) e fai <b>doppio clic sul bottone Nuova partita</b>. Seleziona la procedura vuota <b>ButtonNuovaClick</b> (da procedure a end;) e incolla al suo posto:", "cD"),
    ("Premi <b>F9</b>: il gioco parte! Scrivi un numero e premi Prova, finché vedi <b>Troppo BASSO</b>, <b>Troppo ALTO</b> e <b>Indovinato</b>. <b>FATTO: hai fatto un gioco!</b> Errore su <b>else</b>? Guarda l'end subito prima: NON deve avere il <b>;</b>.", ""),
    ("<b>Fallo tuo</b>: cambia la Caption della Form (il titolo della finestra), le frasi tra apici (anche spiritose) e i colori. Poi fallo provare a un compagno: chi indovina con meno tentativi?", ""),
    ("Gli screenshot: con il gioco aperto premi <b>Win + Shift + S</b> e seleziona la finestra. Incolla nel Documento del compito, parte 1. Ne servono <b>3</b>: Troppo BASSO, Troppo ALTO, Indovinato.", ""),
    ("Il codice: in Lazarus seleziona tutta la procedura <b>ButtonProvaClick</b> (da procedure al suo end;), Ctrl + C, e incollala nel Documento, parte 2. I rientri devono restare.", ""),
    ("Nel Documento, parte 3: spiega con parole tue <b>perché serve un if dentro un altro if</b>. Parte 4: cosa non sei riuscito a fare, cosa non hai capito.", ""),
    ("Su <b>Classroom</b>, nel compito, premi il bottone blu <b>Consegna</b>. Poi il professore ti fa qualche domanda sul tuo gioco.", ""),
]
pre = "".join("<pre id='%s' hidden>%s</pre>" % (k, html.escape(v)) for k, v in COPIE.items())
BOX = ("<!--PASSO-->"
       "<div class='box mia' style='border:3px solid #1f6fa5'><h2 style='color:#1f6fa5'>IL GIOCO PASSO PASSO: un passo alla volta</h2>"
       "<p>Leggi il passo, fallo, poi premi il bottone verde <b>FATTO</b>. Nomi e codice si copiano con i bottoni gialli: niente da scrivere a mano.</p>"
       "<style>#pn{font-size:20px;font-weight:800;color:#12467a}.barra{height:12px;background:#e3e9f0;border-radius:6px;overflow:hidden;margin:6px 0}.barra div{height:100%;background:#2f9e57}"
       "#pt{font-size:22px;line-height:1.5;background:#f4f9ff;border:3px solid #1f6fa5;border-radius:14px;padding:16px;margin:8px 0}"
       ".cpb{background:#ffd34d;color:#1a2330;font-size:20px;font-weight:800;border:0;border-radius:12px;padding:14px;width:100%;margin-top:8px;cursor:pointer}"
       ".av{background:#2f9e57;color:#fff;font-size:22px;font-weight:700;border:0;border-radius:12px;padding:14px 18px;cursor:pointer}.ind{background:#7a8794;color:#fff;font-size:16px;border:0;border-radius:10px;padding:10px 14px;cursor:pointer}"
       "#pcod{background:#1e1e1e;color:#e6e6e6;font-family:Consolas,monospace;font-size:14px;border-radius:10px;padding:10px;white-space:pre;overflow:auto;margin-top:8px}</style>"
       "<div id='pn'></div><div class='barra'><div id='pb'></div></div><div id='pt'></div><div id='pc'></div><pre id='pcod' hidden></pre>"
       "<button class='av' onclick='mv(1)'>FATTO &rarr; passo dopo</button> <button class='ind' onclick='mv(-1)'>&larr; passo prima</button> <button class='ind' onclick='mv(-99)'>ricomincia</button>"
       + pre +
       "<script>var PS=__PS__,LB=__LB__,P=0;try{P=parseInt(localStorage.getItem('passo-2inf-indovina')||'0')||0}catch(e){}"
       "function dis(){var t=PS[P];document.getElementById('pn').textContent='Passo '+(P+1)+' di '+PS.length;document.getElementById('pb').style.width=Math.round((P+1)*100/PS.length)+'%';"
       "document.getElementById('pt').innerHTML=t[0];var c=document.getElementById('pc'),k=document.getElementById('pcod');"
       "if(t[1]){c.innerHTML='<button class=\"cpb\" onclick=\"cp(\\''+t[1]+'\\',this)\">'+LB[t[1]]+'</button>';if(t[1][0]=='c'){k.hidden=false;k.textContent=document.getElementById(t[1]).textContent}else k.hidden=true}else{c.innerHTML='';k.hidden=true}}"
       "function mv(d){P=Math.max(0,Math.min(PS.length-1,d==-99?0:P+d));try{localStorage.setItem('passo-2inf-indovina',P)}catch(e){}dis()}"
       "function cp(id,b){var t=document.getElementById(id).textContent;function ok(){b.textContent='COPIATO! Ora Ctrl + V in Lazarus'}"
       "if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){fb(t);ok()})}else{fb(t);ok()}}"
       "function fb(t){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}dis();</script></div>"
       "<!--/PASSO-->").replace("__PS__", json.dumps(P, ensure_ascii=False)).replace("__LB__", json.dumps(LAB, ensure_ascii=False))
s = open(HUB, encoding="utf-8").read()
s = re.sub(r"<!--PASSO-->.*?<!--/PASSO-->", "", s, flags=re.S)
s = s.replace('<span class="ver">v1.0</span>', '<span class="ver">v1.1</span>')
a = '<div class="box b1"><h2>1. Dispensa'
s = s.replace(a, BOX + a, 1)
open(HUB, "w", encoding="utf-8").write(s)
print("ok", len(P), "passi")
