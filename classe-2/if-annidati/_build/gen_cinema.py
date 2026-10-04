# -*- coding: utf-8 -*-
"""Classe 2 — giovedì 08/10/2026: esercitazione valutata "Il cassiere del cinema" (if annidati, 3 livelli + or).
Stessa grafica e stessa regola dei rientri della dispensa if annidati (gen_if_annidati.py).
Uso:  python3 classe-2/if-annidati/_build/gen_cinema.py
"""
import os, sys, glob, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_if_annidati as G
from gen_if_annidati import pascal, doc, box, livelli

VER = "1.0"
DATA = "08/10/2026"
PREF = "20261008_Classe-2-PerTutti"
CART = G.CART
DOCS = os.path.join(os.path.dirname(os.path.dirname(CART)), "docs", "2inf-if")

CODICE = """procedure TForm1.ButtonPrezzoClick(Sender: TObject);
var
  eta: Integer;
begin
  eta := StrToInt(EditEta.Text);
  if eta < 6 then
    begin
      LabelPrezzo.Caption := 'Gratis!';
    end
  else
    begin
      if (eta < 14) or (eta >= 65) then
        begin
          LabelPrezzo.Caption := 'Ridotto: 5 euro';
        end
      else
        begin
          if CheckBoxMercoledi.Checked then
            begin
              LabelPrezzo.Caption := 'Mercoledì: 6 euro';
            end
          else
            begin
              LabelPrezzo.Caption := 'Intero: 8 euro';
            end;
        end;
    end;
end;"""


def scheda():
    c = "<style>.lv.l4{page-break-inside:avoid}pre.pas{font-size:8.6pt;line-height:1.35}</style>"
    c += "<div class='cover'><span class='ver'>v%s</span><h1>Il cassiere del cinema</h1>" % VER
    c += "<div class='s'>Classe 2 · Informatica · Lazarus · %s · if annidati su 3 livelli · esercitazione valutata</div></div>" % DATA
    c += box("novita", "<b>La missione:</b> il cinema ti assume come programmatore. Devi fare l'app della cassa: il cliente scrive l'<b>età</b>, "
             "spunta se oggi è <b>mercoledì</b>, preme <b>Prezzo</b> e l'app dice quanto paga. È un vero programma da lavoro, fatto tutto con gli <b>if</b>.")
    c += "<h2>1. Le regole del cinema</h2><table><tr><th>Chi</th><th>Quanto paga</th></tr>"
    c += "<tr><td>meno di 6 anni</td><td><b>Gratis!</b></td></tr><tr><td>da 6 a 13 anni, oppure 65 anni e più</td><td><b>Ridotto: 5 euro</b></td></tr>"
    c += "<tr><td>tutti gli altri, di mercoledì</td><td><b>Mercoledì: 6 euro</b></td></tr><tr><td>tutti gli altri</td><td><b>Intero: 8 euro</b></td></tr></table>"
    c += "<div class='flow'><div class='q'>età &lt; 6 ?</div><div>SÌ &rarr; <b>Gratis</b></div><div>NO &rarr;</div><div class='q'>età &lt; 14 <u>oppure</u> età &ge; 65 ?</div>"
    c += "<div>SÌ &rarr; <b>5 euro</b></div><div>NO &rarr;</div><div class='q'>mercoledì ?</div><div>SÌ &rarr; <b>6 euro</b></div><div>NO &rarr; <b>8 euro</b></div></div>"
    c += box("carta", "<b>Carta e penna, PRIMA del computer:</b> ricopia lo schema a frecce: 3 domande, 4 risposte. Ogni domanda è un <b>if</b>; ogni NO porta al prossimo if, dentro l'<b>else</b>.")
    c += "<h2>2. Parola nuova: or (oppure)</h2><p><code>(eta &lt; 14) or (eta &gt;= 65)</code> è vero se <b>almeno una</b> delle due condizioni è vera. "
    c += "Le condizioni vanno <b>tra parentesi</b>. Componente nuovo: la <b>CheckBox</b> (casella da spuntare): <code>CheckBoxMercoledi.Checked</code> è vero se è spuntata.</p>"
    c += "<div class='form'><div class='tb'>Cinema Stella — Cassa</div><div class='in'>Quanti anni hai? <span class='ed'>15</span><br><br>"
    c += "&#9745; Oggi è mercoledì &nbsp; <span class='bt'>Prezzo</span><br><br><b style='color:#c0392b'>Mercoledì: 6 euro</b></div></div><div class='cap'>La tua app (il nome del cinema lo scegli tu)</div>"
    c += "<h2>3. Costruisci l'app</h2>"
    c += livelli(
        "<p>Una casella per l'età, una casella da spuntare per il mercoledì, un bottone <b>Prezzo</b>, una scritta che mostra il prezzo secondo le regole del punto 1.</p>",
        "<p>Tre if uno dentro l'altro, nell'ordine dello schema: prima \"età &lt; 6\", nell'else \"età &lt; 14 or età &ge; 65\", nell'else \"mercoledì?\". "
        "Scrivi <b>prima tutte le coppie begin/end</b>, poi riempi.</p>",
        "<table><tr><th>Pezzo</th><th>Name</th><th>Proprietà</th></tr>"
        "<tr><td>Form</td><td>Form1</td><td>Caption = il nome del TUO cinema</td></tr>"
        "<tr><td>Label</td><td>Label1</td><td>Caption = Quanti anni hai?</td></tr>"
        "<tr><td>Edit</td><td>EditEta</td><td>Text = (vuoto)</td></tr>"
        "<tr><td>CheckBox</td><td>CheckBoxMercoledi</td><td>Caption = Oggi è mercoledì (gruppo Standard, icona con la spunta)</td></tr>"
        "<tr><td>Button</td><td>ButtonPrezzo</td><td>Caption = Prezzo</td></tr>"
        "<tr><td>Label</td><td>LabelPrezzo</td><td>Caption = (vuoto) · Font grande e colorato</td></tr></table>",
        "<div class='pz'><p>Doppio clic su <b>Prezzo</b> e scrivi:</p>" + pascal(CODICE) + "</div>")
    c += "<h2>4. Collaudo: la tabella di prova</h2>"
    c += "<p>I programmatori veri <b>provano</b> ogni strada prima di consegnare. Prova questi casi e scrivi cosa esce:</p>"
    c += "<table><tr><th>Età</th><th>Mercoledì?</th><th>Deve uscire</th><th>È uscito (scrivi tu)</th></tr>"
    for e, m, r in [("4", "no", "Gratis!"), ("10", "sì", "Ridotto: 5 euro"), ("70", "no", "Ridotto: 5 euro"), ("16", "sì", "Mercoledì: 6 euro"), ("30", "no", "Intero: 8 euro"), ("14", "no", "Intero: 8 euro")]:
        c += "<tr><td>%s</td><td>%s</td><td>%s</td><td></td></tr>" % (e, m, r)
    c += "</table>"
    c += box("tuo", "<b>Fallo tuo:</b> nome del cinema, colori, il titolo del film di oggi in una Label. Puoi cambiare i prezzi: ma allora cambia anche la tabella di prova.")
    c += "<h2>5. Sfide per chi ha finito</h2><ol>"
    c += "<li><b>Popcorn:</b> aggiungi la CheckBox <b>Popcorn (+3 euro)</b>. Aiuto: usa una variabile <code>prezzo: Integer</code>, calcola il prezzo con gli if, poi <code>if CheckBoxPopcorn.Checked then prezzo := prezzo + 3;</code> e alla fine scrivi <code>IntToStr(prezzo) + ' euro'</code>.</li>"
    c += "<li><b>Età impossibile:</b> se l'età è minore di 0 o maggiore di 120 scrivi <b>Età non valida</b> (un if in più, prima di tutti gli altri).</li>"
    c += "<li><b>Biglietti per la famiglia:</b> una casella <b>Quanti biglietti?</b> e il totale da pagare.</li></ol>"
    c += "<div class='foot'>Classe 2 · Il cassiere del cinema · v%s</div>" % VER
    return doc("Il cassiere del cinema", c)


def compito():
    c = "<div class='cover'><span class='ver'>v%s</span><h1>Compito — Il cassiere del cinema</h1>" % VER
    c += "<div class='s'>Classe 2 · Informatica · Lazarus · %s · si consegna su Classroom</div></div>" % DATA
    c += box("novita", "<b>Cosa consegni:</b> il <b>Documento</b> già pronto nel compito su Classroom (c'è già il tuo nome), con <b>5 parti</b>.")
    c += "<ol><li><b>Lo schema a frecce</b> fatto a mano sul quaderno: una <b>foto</b>.</li>"
    c += "<li><b>4 screenshot</b> dell'app: Gratis, Ridotto, Mercoledì, Intero (" + "<span class='t'>Win</span> + <span class='t'>Shift</span> + <span class='t'>S</span>).</li>"
    c += "<li><b>La tabella di prova</b> completata (i 6 casi con cosa è uscito).</li>"
    c += "<li><b>Il codice</b> del bottone Prezzo, con i rientri in ordine.</li>"
    c += "<li><b>Spiegalo con parole tue:</b> a) cosa fa <b>or</b>? b) perché il controllo \"età &lt; 6\" viene <b>per primo</b>? c) cosa NON hai capito?</li></ol>"
    c += "<h2>Come viene valutato (voto in decimi)</h2><table><tr><th>Cosa guardo</th><th style='width:16mm'>Punti</th></tr>"
    for a, p in [("L'app funziona: i 4 prezzi negli screenshot", "3"), ("Tabella di prova completa e onesta", "2"),
                 ("Codice con if annidati e rientri in ordine", "2"), ("Schema a mano", "1"), ("Spiegazione con parole tue", "2")]:
        c += "<tr><td>%s</td><td style='text-align:center'><b>%s</b></td></tr>" % (a, p)
    c += "<tr><td><b>Totale</b> (+1 per ogni sfida fatta bene, fino a 10)</td><td style='text-align:center'><b>10</b></td></tr></table>"
    c += box("nota", "<b>Non funziona tutto?</b> Consegna lo stesso e scrivi nella tabella di prova cosa è uscito davvero: trovare un errore con il collaudo è già un lavoro da programmatore.")
    return doc("Compito — Il cassiere del cinema", c)


if __name__ == "__main__":
    for v in glob.glob(os.path.join(CART, PREF + "_*.pdf")): os.remove(v)
    s = "%s_v%s_Scheda-Cassiere-Cinema_IT.pdf" % (PREF, VER); c = "%s_v%s_Compito-Cassiere-Cinema_IT.pdf" % (PREF, VER)
    G.pdf(scheda(), "scheda-cassiere-cinema.html", s); G.pdf(compito(), "compito-cassiere-cinema.html", c)
    shutil.copy(os.path.join(CART, s), os.path.join(DOCS, "Scheda-Cassiere-Cinema-v%s.pdf" % VER))
    shutil.copy(os.path.join(CART, c), os.path.join(DOCS, "Compito-Cassiere-Cinema-v%s.pdf" % VER))
