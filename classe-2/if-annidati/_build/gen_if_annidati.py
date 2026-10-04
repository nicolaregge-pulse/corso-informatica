# -*- coding: utf-8 -*-
"""Classe 2 — if / then / else e if ANNIDATI in Lazarus + il gioco "Indovina il numero".

Regola di indentazione (RIFERIMENTI §2.27, voluta da Nicola): if ed else sullo stesso rientro,
begin ed end sullo stesso rientro, tutto il resto indentato. Nel corso si usa SEMPRE begin...end
dopo then e dopo else, anche per una riga sola (stile della scheda Convertitore: begin un gradino
dentro rispetto all'if).

Genera: Dispensa (teoria + riscaldamento + gioco a 4 livelli + sfide), Compito, in classe-2/if-annidati/.
Uso:  python3 classe-2/if-annidati/_build/gen_if_annidati.py
"""
import html, os, re, subprocess, glob

VER = "1.0"
DATA = "05/10/2026"
PREF = "20261005_Classe-2-PerTutti"
QUI = os.path.dirname(os.path.abspath(__file__))
CART = os.path.dirname(QUI)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
E = html.escape

COL = ["#12467a", "#1e7a44", "#7030a0", "#c0392b", "#d9731a", "#1f6fa5"]   # colore per profondità


def pascal(code, coppie=True):
    """Colora il Pascal: if/then/else in rosso; ogni coppia begin/end con lo stesso colore e numero."""
    out, pila, n = [], [], 0
    for riga in code.strip("\n").split("\n"):
        r = E(riga)
        r = re.sub(r"(//.*)$", r"<span class='cm'>\1</span>", r)
        r = re.sub(r"\b(if|then|else|var|procedure|mod)\b", r"<span class='kw'>\1</span>", r)
        if coppie:
            def bg(m):
                nonlocal n
                n += 1; pila.append(n); c = COL[(len(pila) - 1) % len(COL)]
                return "<span class='be' style='color:%s'><i style='background:%s'>%d</i>begin</span>" % (c, c, n)
            def en(m):
                k = pila.pop() if pila else 0; c = COL[len(pila) % len(COL)]
                return "<span class='be' style='color:%s'><i style='background:%s'>%d</i>end</span>" % (c, c, k)
            r = re.sub(r"\bbegin\b", bg, r)
            r = re.sub(r"\bend\b", en, r)
        out.append(r)
    return "<pre class='pas'>%s</pre>" % "\n".join(out)


CSS = """
@page{size:A4;margin:13mm 13mm 12mm}*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;color:#1a2330;line-height:1.45;font-size:10.5pt;font-family:"DejaVu Sans",Arial,sans-serif}
.cover{background:linear-gradient(160deg,#134a6e,#2c86b8);color:#fff;border-radius:12px;padding:9mm 10mm;margin-bottom:5mm;position:relative}
.cover h1{font-size:20pt;margin:0;line-height:1.25}.cover .s{font-size:10.5pt;opacity:.93;margin-top:2mm}
.ver{position:absolute;top:4mm;right:5mm;background:#fff;color:#134a6e;font-weight:bold;font-size:10pt;padding:1mm 3mm;border-radius:12px}
h2{color:#12467a;font-size:14pt;margin:6mm 0 2mm;background:#eef4fb;border-left:6px solid #2b7cc4;padding:2mm 4mm;border-radius:4px;page-break-after:avoid}
h3{color:#12467a;font-size:12pt;margin:4mm 0 1.5mm;page-break-after:avoid}
p{margin:1.5mm 0}ol{margin:1mm 0 2mm;padding-left:7mm}li{margin:1.4mm 0}
code,.t{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 4px;font-size:9.4pt}
pre.pas{background:#f5f8fc;border:1px solid #cfdbe8;color:#1a2330;border-radius:8px;padding:3mm 4mm 3mm 8mm;font-family:"DejaVu Sans Mono",monospace;font-size:9pt;line-height:1.45;white-space:pre-wrap;margin:2mm 0;page-break-inside:avoid}
.kw{color:#c0392b;font-weight:bold}.cm{color:#7a8794;font-style:italic}
.be{font-weight:bold}.be i{font-style:normal;color:#fff;border-radius:50%;display:inline-block;width:4.2mm;height:4.2mm;line-height:4.2mm;text-align:center;font-size:7pt;margin-left:-5mm;margin-right:.8mm;vertical-align:1px}
.box{border-radius:6px;padding:2.5mm 4mm;margin:3mm 0;page-break-inside:avoid}
.novita{background:#eafaf0;border-left:5px solid #2f9e57}.attn{background:#fdecea;border-left:5px solid #c0392b}
.nota{background:#fff8e6;border-left:5px solid #d0a516}.tuo{background:#f2ebf7;border-left:5px solid #8e44ad}
.carta{background:#eef4fb;border:1px dashed #9cc0e4;color:#22405e}
.lv{border:1px solid #cfdae6;border-radius:8px;margin:3mm 0;page-break-inside:avoid}.lv.l4{page-break-inside:auto}.pz{page-break-inside:avoid}
.lv .h{padding:1.8mm 3.5mm;font-weight:bold;color:#fff}.lv .b{padding:2mm 4mm}
.l1 .h{background:#2f9e57}.l2 .h{background:#1f6fa5}.l3 .h{background:#d9731a}.l4 .h{background:#7030a0}
table{border-collapse:collapse;width:100%;margin:2mm 0;page-break-inside:avoid}
th,td{border:1px solid #cfdbe8;padding:1.5mm 2.5mm;text-align:left;vertical-align:top;font-size:9.8pt}th{background:#12467a;color:#fff}
.form{border:2px solid #8aa0b6;border-radius:6px;width:95mm;margin:2mm auto;background:#f0f0f0;font-size:9pt;page-break-inside:avoid}
.form .tb{background:#2c86b8;color:#fff;padding:1mm 3mm;font-weight:bold}.form .in{padding:3mm}
.form .ed{display:inline-block;background:#fff;border:1px solid #888;width:30mm;padding:.5mm 2mm}
.form .bt{display:inline-block;background:#e1e1e1;border:1px solid #888;border-radius:3px;padding:.5mm 3mm}
.cap{font-size:8.8pt;color:#667;text-align:center;margin:0 0 2mm}
.flow{display:flex;gap:2mm;align-items:center;justify-content:center;flex-wrap:wrap;margin:2mm 0;font-size:9.4pt}
.flow div{border:2px solid #12467a;border-radius:6px;padding:1.5mm 3mm;text-align:center;background:#fff}
.flow .q{border-color:#c0392b;background:#fdecea}.flow .ok{border-color:#2f9e57;background:#eafaf0}
.foot{margin-top:5mm;font-size:8.6pt;color:#778;border-top:1px solid #dde4ec;padding-top:1.5mm}
"""


def doc(titolo, corpo):
    return "<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>%s</body></html>" % (E(titolo), CSS, corpo)


def box(cls, t):
    return "<div class='box %s'>%s</div>" % (cls, t)


def livelli(l1, l2, l3, l4):
    s = ""
    for k, (tit, cont) in enumerate([("Livello 1 — Cosa deve fare", l1), ("Livello 2 — Un aiuto", l2),
                                     ("Livello 3 — I pezzi sulla Form", l3), ("Livello 4 — Il codice completo", l4)], 1):
        s += "<div class='lv l%d'><div class='h'>%s</div><div class='b'>%s</div></div>" % (k, tit, cont)
    return s


# ---------------------------------------------------------------- codice del gioco
GIOCO_VAR = """var
  Form1: TForm1;
  segreto: Integer;     // il numero pensato dal computer
  tentativi: Integer;   // quante prove hai fatto"""

GIOCO_CREATE = """procedure TForm1.FormCreate(Sender: TObject);
begin
  Randomize;                     // mescola i numeri a caso
  segreto := Random(100) + 1;    // un numero da 1 a 100
  tentativi := 0;
end;"""

GIOCO_PROVA = """procedure TForm1.ButtonProvaClick(Sender: TObject);
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

GIOCO_NUOVA = """procedure TForm1.ButtonNuovaClick(Sender: TObject);
begin
  segreto := Random(100) + 1;
  tentativi := 0;
  LabelRisposta.Caption := 'Ho pensato un nuovo numero da 1 a 100';
end;"""


def dispensa():
    c = "<div class='cover'><span class='ver'>v%s</span><h1>Le decisioni: if / then / else<br>e gli if uno dentro l'altro</h1>" % VER
    c += "<div class='s'>Classe 2 · Informatica · Lazarus · %s · e alla fine il gioco <b>Indovina il numero</b></div></div>" % DATA
    c += box("novita", "<b>Cosa impari oggi:</b> a far <b>decidere</b> il programma (<b>if</b> = se, <b>then</b> = allora, <b>else</b> = altrimenti) "
             "e a mettere un if <b>dentro</b> un altro if (si dice <b>if annidati</b>: come una scatola dentro una scatola). "
             "Alla fine costruisci un <b>gioco vero</b>: il computer pensa un numero e tu lo devi indovinare.")
    c += "<h2>1. Ripasso: if / then / else</h2>"
    c += "<p>Si legge come in italiano: <b>SE</b> la condizione è vera <b>ALLORA</b> fai questo, <b>ALTRIMENTI</b> fai quest'altro.</p>"
    c += "<div class='flow'><div class='q'>numero pari?</div><div class='ok'>SÌ &rarr; scrivi PARI</div><div>NO &rarr; scrivi DISPARI</div></div>"
    c += pascal("""numero := StrToInt(Edit1.Text);
if numero mod 2 = 0 then
  begin
    Label1.Caption := 'PARI';
  end
else
  begin
    Label1.Caption := 'DISPARI';
  end;""")
    c += "<p><code>mod</code> = il <b>resto</b> della divisione: se diviso 2 il resto è 0, il numero è pari. I confronti: "
    c += "<code>=</code> uguale · <code>&lt;&gt;</code> diverso · <code>&lt;</code> minore · <code>&gt;</code> maggiore · <code>&lt;=</code> · <code>&gt;=</code>.</p>"

    c += "<h2>2. La regola dei rientri (si fa sempre così)</h2>"
    c += "<table><tr><th>Regola</th><th>Perché</th></tr>"
    c += "<tr><td><b>if</b> ed <b>else</b> sullo <b>stesso rientro</b> (stessa colonna)</td><td>si vede subito quale else appartiene a quale if</td></tr>"
    c += "<tr><td><b>begin</b> ed <b>end</b> sullo <b>stesso rientro</b>, con lo stesso numero e colore</td><td>ogni begin ha il suo end, come una parentesi che si apre e si chiude</td></tr>"
    c += "<tr><td>tutto quello che sta <b>dentro</b> va <b>un gradino più a destra</b> (2 spazi)</td><td>si vede a colpo d'occhio chi sta dentro a chi</td></tr>"
    c += "<tr><td>dopo <b>then</b> e dopo <b>else</b> mettiamo <b>sempre</b> begin ... end, anche per una riga sola</td><td>il codice resta sempre ordinato e puoi aggiungere righe senza errori</td></tr></table>"
    c += box("attn", "<b>L'errore che fanno tutti (anche i professionisti):</b> il <b>;</b> prima di <b>else</b>. "
             "L'<b>end</b> che sta subito prima di <b>else</b> va <b>senza</b> punto e virgola. Il <b>;</b> si mette solo all'<b>end</b> finale dell'if.")
    c += box("nota", "<b>Trucco per non perdere le coppie:</b> appena scrivi <b>begin</b>, scrivi subito sotto il suo <b>end</b> allo stesso rientro. Poi riempi in mezzo.")

    c += "<h2>3. Un if dentro un altro if (if annidati)</h2>"
    c += "<p>Con un solo if hai <b>2 strade</b>. Se dentro l'else metti un altro if, le strade diventano <b>3</b>. Esempio: positivo, negativo o zero?</p>"
    c += "<div class='flow'><div class='q'>numero &gt; 0 ?</div><div>SÌ &rarr; <b>POSITIVO</b></div><div>NO &rarr;</div><div class='q'>numero &lt; 0 ?</div><div>SÌ &rarr; <b>NEGATIVO</b></div><div>NO &rarr; <b>ZERO</b></div></div>"
    c += pascal("""numero := StrToInt(Edit1.Text);
if numero > 0 then
  begin
    Label1.Caption := 'POSITIVO';
  end
else
  begin
    if numero < 0 then
      begin
        Label1.Caption := 'NEGATIVO';
      end
    else
      begin
        Label1.Caption := 'ZERO';
      end;
  end;""")
    c += box("carta", "<b>Carta e penna:</b> ricopia questo codice sul quaderno e traccia una <b>graffa</b> da ogni begin al suo end (stesso numero). "
             "Poi disegna lo schema a frecce: due domande, tre risposte.")

    c += "<h2>4. Riscaldamento (Form: Edit1, Button1, Label1)</h2>"
    c += ("<p>Stessa Form per tutti e tre: una casella <b>Edit1</b>, un bottone <b>Button1</b> (Caption: <b>Controlla</b>), una scritta <b>Label1</b>. "
         "Doppio clic sul bottone e scrivi il codice tra begin ed end. Ricordati <code>var numero: Integer;</code> sopra il begin.</p>")
    c += "<table><tr><th style='width:9mm'>N.</th><th>Esercizio</th><th>Quante strade</th></tr>"
    c += "<tr><td>R1</td><td><b>Pari o dispari</b>: copia l'esempio del punto 1 e provalo con 4, 7, 0.</td><td>2 (un if)</td></tr>"
    c += "<tr><td>R2</td><td><b>Positivo, negativo o zero</b>: copia l'esempio del punto 3 e provalo con 5, -3, 0.</td><td>3 (if annidati)</td></tr>"
    c += "<tr><td>R3</td><td><b>Il voto</b> (fallo tu!): se il voto è minore di 6 scrivi <b>Insufficiente</b>; altrimenti, se è minore di 8 scrivi <b>Sufficiente</b>; altrimenti <b>Ottimo!</b>. Prova con 4, 6, 7, 9.</td><td>3 (if annidati)</td></tr>"
    c += "<tr><td>R4</td><td><b>Maggiorenne?</b> (fallo tu!): età minore di 14 &rarr; <b>Bambino</b>; minore di 18 &rarr; <b>Ragazzo</b>; altrimenti <b>Maggiorenne</b>.</td><td>3 (if annidati)</td></tr></table>"
    c += box("nota", "<b>Aiuto per R3:</b> è identico a R2: cambia solo le condizioni (<code>voto &lt; 6</code>, <code>voto &lt; 8</code>) e le scritte.")

    c += "<h2>5. Il gioco: Indovina il numero</h2>"
    c += "<div class='form'><div class='tb'>Indovina il numero</div><div class='in'>Ho pensato un numero da 1 a 100. Quale?<br><br>"
    c += "<span class='ed'>50</span> &nbsp; <span class='bt'>Prova</span> &nbsp; <span class='bt'>Nuova partita</span><br><br>"
    c += "<b style='color:#c0392b'>Troppo ALTO: prova un numero più piccolo</b></div></div><div class='cap'>Ecco come sarà il tuo gioco (titolo e colori li scegli tu)</div>"
    c += livelli(
        "<p>All'avvio il computer pensa un numero <b>segreto</b> da 1 a 100. Tu scrivi un numero e premi <b>Prova</b>. "
        "Il programma risponde: <b>Troppo BASSO</b>, <b>Troppo ALTO</b> oppure <b>BRAVO! Indovinato</b> (con il numero di tentativi). "
        "Il bottone <b>Nuova partita</b> pensa un altro numero.</p>",
        "<p>Ti servono 2 variabili che <b>durano per tutta la partita</b> (segreto e tentativi): vanno in alto, sotto <code>Form1: TForm1;</code>. "
        "Il numero segreto si crea con <code>Random(100) + 1</code>, all'avvio (evento <b>OnCreate</b> della Form: doppio clic su un punto vuoto della Form). "
        "Nel bottone Prova usa un <b>if annidato</b>: prima chiedi \"è uguale?\", nell'else chiedi \"è più piccolo?\".</p>",
        "<table><tr><th>Pezzo</th><th>Name</th><th>Proprietà</th></tr>"
        "<tr><td>Form</td><td>Form1</td><td>Caption = Indovina il numero</td></tr>"
        "<tr><td>Label</td><td>Label1</td><td>Caption = Ho pensato un numero da 1 a 100. Quale?</td></tr>"
        "<tr><td>Edit</td><td>EditNumero</td><td>Text = (vuoto)</td></tr>"
        "<tr><td>Button</td><td>ButtonProva</td><td>Caption = Prova</td></tr>"
        "<tr><td>Button</td><td>ButtonNuova</td><td>Caption = Nuova partita</td></tr>"
        "<tr><td>Label</td><td>LabelRisposta</td><td>Caption = (vuoto) · Font: grande e colorato, a tuo gusto</td></tr></table>",
        "<div class='pz'><p><b>A) In alto nel codice</b>, sotto <code>Form1: TForm1;</code>, aggiungi le due variabili:</p>" + pascal(GIOCO_VAR, False) + "</div>" +
        "<div class='pz'><p><b>B) Doppio clic su un punto vuoto della Form</b> &rarr; nasce <b>FormCreate</b>:</p>" + pascal(GIOCO_CREATE) + "</div>" +
        "<div class='pz'><p><b>C) Doppio clic su Prova</b> &rarr; il cuore del gioco, con l'<b>if annidato</b>:</p>" + pascal(GIOCO_PROVA) + "</div>" +
        "<div class='pz'><p><b>D) Doppio clic su Nuova partita</b>:</p>" + pascal(GIOCO_NUOVA) + "</div>")
    c += box("attn", "<b>Se Lazarus dà errore su else:</b> guarda l'end subito prima: non deve avere il <b>;</b>. "
             "<b>Se dà errore appena premi Prova con la casella vuota:</b> è normale, StrToInt vuole un numero (vedi sfida 3).")
    c += box("tuo", "<b>Fallo tuo:</b> cambia il titolo della finestra, i colori, le frasi (anche spiritose) e il nome del gioco. Poi fallo provare a un compagno: chi indovina con meno tentativi?")

    c += "<h2>6. Sfide per chi ha finito (sempre con gli if)</h2>"
    c += ("<ol><li><b>Ci sei quasi!</b> Dentro \"troppo alto\" e \"troppo basso\" aggiungi un altro if: se la differenza è al massimo 5, scrivi <b>Ci sei quasi!</b> "
         "(aiuto: <code>if Abs(numero - segreto) &lt;= 5 then</code>).</li>"
         "<li><b>Massimo 7 tentativi:</b> se tentativi arriva a 7 e non hai indovinato, scrivi <b>Hai perso! Il numero era</b> ... (aiuto: <code>IntToStr(segreto)</code>).</li>"
         "<li><b>Fuori campo:</b> se il numero è minore di 1 o maggiore di 100 scrivi <b>Solo numeri da 1 a 100!</b> e non contare il tentativo "
         "(aiuto: <code>if (numero &lt; 1) or (numero &gt; 100) then</code>).</li>"
         "<li><b>Livelli:</b> aggiungi tre bottoni <b>Facile</b> (1-10), <b>Medio</b> (1-100), <b>Difficile</b> (1-1000).</li></ol>")
    c += "<div class='foot'>Classe 2 · Dispensa if / then / else e if annidati · v%s · Non si consegna: si consegna il foglio del COMPITO.</div>" % VER
    return doc("Dispensa — if annidati e Indovina il numero", c)


def compito():
    c = "<div class='cover'><span class='ver'>v%s</span><h1>Compito — Indovina il numero</h1>" % VER
    c += "<div class='s'>Classe 2 · Informatica · Lazarus · %s · si consegna su Classroom</div></div>" % DATA
    c += box("novita", "<b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom (c'è già il tuo nome), con <b>4 parti</b>.")
    c += "<h2>Le 4 parti del Documento</h2><ol>"
    c += ("<li><b>Gli screenshot del gioco che funziona</b>: tre immagini, una con <b>Troppo BASSO</b>, una con <b>Troppo ALTO</b>, una con <b>BRAVO! Indovinato</b>. "
         "(Premi <span class='t'>Win</span> + <span class='t'>Shift</span> + <span class='t'>S</span>, seleziona la finestra del gioco, poi nel Documento <span class='t'>Ctrl</span> + <span class='t'>V</span>.)</li>")
    c += "<li><b>Il codice del bottone Prova</b>: in Lazarus seleziona tutta la procedura <b>ButtonProvaClick</b>, da <b>procedure</b> fino al suo <b>end;</b>, copia e incolla. I rientri devono restare: if ed else allineati, begin ed end allineati.</li>"
    c += "<li><b>Spiegalo con parole tue</b>: a) perché qui serve un if <b>dentro</b> un altro if? b) cosa succede se scrivi il <b>;</b> prima di else?</li>"
    c += "<li><b>Riflessione</b>: cosa NON sono riuscito a fare e perché; cosa NON ho capito.</li></ol>"
    c += "<h2>Come viene valutato (voto in decimi)</h2><table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in [("Il gioco funziona: i tre casi negli screenshot", "3"), ("If annidato corretto (uguale / più piccolo / più grande)", "2"),
                 ("Rientri in ordine: if/else allineati, begin/end allineati, il resto indentato", "2"),
                 ("Il gioco è tuo: titolo, frasi, colori", "1"), ("Spiegazione con parole tue", "1,5"), ("Riflessione", "0,5")]:
        c += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += "<tr><td><b>Totale</b> (+1 bonus per ogni sfida della dispensa fatta bene, fino a 10)</td><td style='text-align:center'><b>10</b></td></tr></table>"
    c += box("nota", "<b>Non hai finito?</b> Consegna lo stesso quello che hai fatto e scrivilo nella riflessione: conta anche il pezzo fatto. Il bug è normale, succede a tutti i programmatori.")
    c += box("carta", "<b>Carta e penna:</b> sul quaderno disegna lo schema a frecce del bottone Prova (2 domande, 3 risposte) prima di scrivere il codice.")
    c += "<div class='foot'>Classe 2 · Compito Indovina il numero · v%s</div>" % VER
    return doc("Compito — Indovina il numero", c)


def pdf(h, nome_html, nome_pdf):
    hp = os.path.join(CART, nome_html); open(hp, "w", encoding="utf-8").write(h)
    out = os.path.join(CART, nome_pdf)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + out, "file://" + hp], check=True, capture_output=True)
    print(nome_pdf)


if __name__ == "__main__":
    for v in glob.glob(os.path.join(CART, "*.pdf")):
        os.remove(v)
    pdf(dispensa(), "dispensa-if-annidati.html", "%s_v%s_Dispensa-If-Annidati-Indovina-il-Numero_IT.pdf" % (PREF, VER))
    pdf(compito(), "compito-indovina-numero.html", "%s_v%s_Compito-Indovina-il-Numero_IT.pdf" % (PREF, VER))
