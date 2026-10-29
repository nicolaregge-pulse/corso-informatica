#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2INF · Sicurezza sul lavoro (Regione), 5ª ora: rischio infortuni (30/10/2026). Solo italiano (2INF).
# Scrive: docs/verifica/banche/2inf-sicurezza-5ora.js, docs/verifica/stato/2inf-sicurezza-5ora.json
# e (nel riservato) il comando del ponte che crea il quiz su Moduli con gli stessi 20 casi.
# Nessun link al sito della Regione (#136): teoria nelle schede, quiz solo nostro su Google Moduli.
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
R = '/home/user/corso-informatica-riservato/'

SCHEDE = [
 ("1. Ripasso in un minuto", "Nelle prime 4 ore hai visto: <b>pericolo</b> (la cosa che può fare male), <b>rischio</b> (quanto è probabile che faccia male e quanto male), <b>danno</b> (il male che succede). <b>Prevenzione</b> = il danno succede meno spesso; <b>protezione</b> = fa meno male. Poi la squadra della sicurezza e i diritti e doveri.<br><br>Oggi comincia la <b>formazione specifica</b>: la 5ª ora è il <b>rischio infortuni</b>."),
 ("2. Che cos'è un infortunio", "Un <b>infortunio sul lavoro</b> è un evento <b>improvviso e violento</b> che succede <b>mentre lavori</b> e ti fa male: un taglio, una caduta, una scossa.<br><br>La <b>malattia professionale</b> invece arriva <b>piano piano</b>, in mesi o anni (per esempio la schiena rovinata o l'udito perso per il rumore).<br><br><b>Infortunio = in un attimo. Malattia professionale = piano piano.</b>"),
 ("3. Infortunio, incidente, quasi infortunio", "<b>Incidente</b>: succede qualcosa che non doveva succedere (cade uno scatolone).<br><b>Infortunio</b>: l'incidente fa male a una persona (lo scatolone cade su un piede).<br><b>Quasi infortunio</b> (in inglese <i>near miss</i>, «mancato di poco»): poteva farti male, ma per fortuna no (lo scatolone cade a un metro da te).<br><br>Il quasi infortunio è un <b>avviso gratis</b>: va sempre <b>segnalato</b>, perché la volta dopo può andare peggio."),
 ("4. Infortunio in itinere", "<b>In itinere</b> vuol dire «durante il viaggio». È l'infortunio che succede sulla strada <b>da casa al lavoro</b> o <b>dal lavoro a casa</b>, sul percorso normale.<br><br>Anche questo è un infortunio sul lavoro: l'assicurazione lo copre. Per questo anche la strada è sicurezza: casco, cintura, niente telefono alla guida."),
 ("5. Come succedono gli infortuni", "Gli infortuni più frequenti: <b>cadute e scivolamenti</b> (pavimento bagnato, scale, cavi per terra), <b>urti e colpi</b>, <b>tagli</b>, <b>schiacciamenti</b> (mani nelle macchine), <b>oggetti che cadono</b>, <b>incidenti stradali</b>.<br><br>Le parti del corpo più colpite sono le <b>mani</b>. In informatica? Cavi per terra, scale per i cavi di rete, prese e ciabatte sovraccariche, scatoloni pesanti dei PC."),
 ("6. Le cause: cose, organizzazione, persone", "Un infortunio ha quasi sempre più cause insieme:<br><b>1. Le cose</b>: una macchina senza protezione, una scala rotta.<br><b>2. L'organizzazione</b>: troppa fretta, nessuno ha spiegato come si fa, turni troppo lunghi.<br><b>3. Le persone</b>: distrazione, telefono, abitudine («l'ho sempre fatto così»), DPI non usati, scherzi.<br><br>L'<b>abitudine</b> è pericolosa: quando una cosa sembra facile si smette di stare attenti."),
 ("7. Se succede: che cosa fai", "<b>1.</b> Metti al sicuro te e gli altri, senza rischiare (se c'è corrente, non toccare il ferito).<br><b>2.</b> Chiama l'<b>addetto al primo soccorso</b> o il <b>112</b>.<br><b>3.</b> Non spostare il ferito, salvo pericolo grave.<br><b>4.</b> <b>Avvisa subito</b> il preposto o il datore di lavoro, anche se ti sembra una cosa piccola: senza avviso l'infortunio può non essere riconosciuto.<br><b>5.</b> Vai dal medico: il <b>certificato</b> serve per l'assicurazione."),
 ("8. L'assicurazione: l'INAIL", "In Italia i lavoratori sono assicurati contro gli infortuni dall'<b>INAIL</b> (Istituto Nazionale per l'Assicurazione contro gli Infortuni sul Lavoro).<br><br>L'assicurazione è <b>obbligatoria</b> e la paga il <b>datore di lavoro</b>, non il lavoratore. Copre anche gli studenti in laboratorio e in stage.<br><br>Il datore di lavoro <b>denuncia</b> l'infortunio all'INAIL; tu devi solo <b>avvisarlo subito</b> e portare il certificato."),
]
TEMI = {"ripasso": 1, "infortunio": 2, "quasi": 3, "itinere": 4, "come": 5, "cause": 6, "succede": 7, "inail": 8}

ALLEN = [  # (scheda, domanda, [giusta, sbagliate...], spiegazione)
 (1, "La PREVENZIONE fa sì che il danno…", ["succeda meno spesso", "faccia meno male", "sia pagato dall'assicurazione"], "Prevenzione = meno spesso."),
 (2, "Un infortunio sul lavoro è…", ["un evento improvviso che ti fa male mentre lavori", "una malattia che arriva piano piano", "un giorno di ferie"], "Infortunio = in un attimo."),
 (2, "Perdi l'udito dopo 20 anni in un capannone rumoroso. È…", ["una malattia professionale", "un infortunio", "un quasi infortunio"], "Arriva piano piano: malattia professionale."),
 (3, "Uno scatolone cade a un metro da te e non ti tocca. È…", ["un quasi infortunio", "un infortunio", "niente di importante"], "Poteva farti male: quasi infortunio."),
 (3, "Il quasi infortunio…", ["si segnala sempre", "si tiene segreto", "non conta"], "È un avviso gratis."),
 (4, "Ti fai male in motorino andando al lavoro. È un infortunio…", ["in itinere", "in vacanza", "che non conta"], "Sulla strada casa-lavoro: in itinere."),
 (5, "Le parti del corpo più colpite negli infortuni sono…", ["le mani", "le orecchie", "i capelli"], "Le mani."),
 (6, "«L'ho sempre fatto così» è un rischio perché…", ["con l'abitudine si smette di stare attenti", "è vietato dalla legge", "fa perdere tempo"], "L'abitudine abbassa l'attenzione."),
 (7, "Ti tagli un dito, poco. Che cosa fai?", ["avviso subito il preposto", "non dico niente", "lo dico la settimana dopo"], "Si avvisa subito, anche per le cose piccole."),
 (8, "L'assicurazione INAIL la paga…", ["il datore di lavoro", "il lavoratore", "lo studente"], "La paga il datore di lavoro."),
]

QUIZ = [  # (domanda, giusta, sbagliate, tema)
 ("Un magazziniere scivola sul pavimento bagnato e si rompe un polso. È…", "un infortunio sul lavoro", ["una malattia professionale", "un quasi infortunio", "un incidente senza conseguenze"], "infortunio"),
 ("Un tecnico, dopo 15 anni al computer senza pause, ha mal di schiena cronico. È…", "una malattia professionale", ["un infortunio", "un quasi infortunio", "un infortunio in itinere"], "infortunio"),
 ("La differenza tra infortunio e malattia professionale è…", "l'infortunio è improvviso, la malattia arriva piano piano", ["l'infortunio è più grave", "la malattia succede solo fuori dal lavoro", "non c'è differenza"], "infortunio"),
 ("Una scala si rompe mentre nessuno ci sta sopra. È…", "un incidente", ["un infortunio", "una malattia professionale", "un infortunio in itinere"], "quasi"),
 ("Un trapano ti scivola di mano e cade a 20 cm dal piede. È…", "un quasi infortunio", ["un infortunio", "una malattia professionale", "niente"], "quasi"),
 ("Perché si segnala un quasi infortunio?", "perché la volta dopo può andare peggio e si può rimediare prima", ["per prendere una multa", "non si segnala mai", "per avere un giorno libero"], "quasi"),
 ("Torni a casa dal lavoro in bici, sul percorso di sempre, e cadi. È un infortunio…", "in itinere, coperto dall'assicurazione", ["che non conta perché eri fuori dal lavoro", "solo se c'era un testimone", "di cui non si parla"], "itinere"),
 ("In un ufficio di informatica, il rischio di caduta più comune è…", "inciampare nei cavi lasciati per terra", ["cadere dal tetto", "scivolare sul ghiaccio in ufficio", "nessuno"], "come"),
 ("Le parti del corpo più colpite negli infortuni sul lavoro sono…", "le mani", ["gli occhi", "le orecchie", "i piedi"], "come"),
 ("Una ciabatta con 6 prese ha attaccate altre ciabatte. Che rischio c'è?", "surriscaldamento e incendio", ["nessuno", "solo che si spegne il PC", "che si consuma il cavo di rete"], "come"),
 ("Una macchina senza la protezione sulle parti che girano è una causa…", "tecnica (le cose)", ["organizzativa", "di comportamento", "di malattia"], "cause"),
 ("Il capo dice «fai in fretta, salta i controlli». È una causa…", "organizzativa", ["tecnica", "fortunata", "di nessun tipo"], "cause"),
 ("Un operaio scrive al telefono mentre porta un carrello. È una causa…", "di comportamento (la persona)", ["tecnica", "organizzativa", "meteorologica"], "cause"),
 ("Perché l'abitudine è pericolosa?", "perché quando una cosa sembra facile si smette di stare attenti", ["perché fa lavorare piano", "non è pericolosa", "perché costa di più"], "cause"),
 ("Un collega prende la scossa ed è ancora attaccato al cavo. Prima di tutto…", "stacco la corrente, senza toccarlo", ["lo tiro via con le mani", "gli butto dell'acqua", "aspetto che si stacchi"], "succede"),
 ("Un collega cade dalla scala e non si muove. Che cosa fai?", "chiamo il 112 o l'addetto al primo soccorso e non lo sposto", ["lo metto subito in piedi", "gli do da bere", "torno a lavorare"], "succede"),
 ("Ti fai un piccolo taglio al lavoro. Quando avvisi il preposto?", "subito, anche se è piccolo", ["mai, è piccolo", "a fine mese", "solo se sanguina tanto"], "succede"),
 ("Che cos'è l'INAIL?", "l'istituto che assicura i lavoratori contro gli infortuni", ["il sindacato dei lavoratori", "la polizia del lavoro", "un'azienda di trasporti"], "inail"),
 ("Chi paga l'assicurazione contro gli infortuni?", "il datore di lavoro", ["il lavoratore", "il cliente", "nessuno, è facoltativa"], "inail"),
 ("Sei in stage e ti fai male in officina. Sei assicurato?", "sì, anche gli studenti in stage e in laboratorio", ["no, solo i dipendenti", "solo se paghi tu", "solo dopo 18 anni"], "inail"),
]

def C(area, q, o, spiega, tema=''):
    return {"tipo": "c", "area": area, "tema": tema, "q": q, "o": o, "a": 0, "spiega": spiega}

banca = {
 "id": "2inf-sicurezza-5ora-v1", "classe": "2INF",
 "titolo": "Sicurezza sul lavoro — 5ª ora: il rischio infortuni",
 "sotto": "2INF · 30/10/2026 · formazione specifica, 5ª ora · prima le schede, poi il ripasso, poi il quiz su Moduli",
 "stato": "stato/2inf-sicurezza-5ora.json", "risultati": "risultati.html?b=2inf-sicurezza-5ora",
 "minuti": 20, "anteprima": "868848605",
 "aree": {"sic": {"nome": "Rischio infortuni", "peso": 80}, "mia": {"nome": "Nella mia vita (parole tue)", "peso": 20}, "parere": {"nome": "Il tuo parere (non conta per il voto)", "peso": 0}},
 "schede_temi": TEMI,
 "schede": [{"titolo": t, "testo": x} for t, x in SCHEDE],
 "strumenti": [{"t": "La situazione dei quiz di sicurezza", "u": "../avanzamento/2inf-sicurezza-oggi.html", "c": "#b45309"}],
 "via": C("sic", "Uno scatolone cade vicino a te e non ti tocca. È…", ["un quasi infortunio", "un infortunio", "una malattia professionale"], "Quasi infortunio: si segnala.", "quasi"),
 "prepara": [
  {"q": "Spiegalo in 30 secondi: scrivi con parole tue la differenza tra infortunio e quasi infortunio.", "aiuto": "Un esempio vale più di una definizione."},
  {"q": "Pensa al laboratorio dove sei adesso. Scrivi UN pericolo che può causare un infortunio e come lo togli.", "aiuto": "Cavi, prese, sedie, zaini per terra…"}],
 "allenamento": [dict(C("sic", q, o, s), scheda=n) for n, q, o, s in ALLEN],
 "crocette": [C("sic", q, [g] + w, "", t) for q, g, w, t in QUIZ],
 "scale": [{"area": "parere", "q": "Quanto ti senti pronto, adesso, se succede un infortunio vicino a te?", "basso": "per niente", "alto": "moltissimo", "ultima": True}],
 "aperte": [
  {"area": "mia", "tema": "quasi", "q": "IL QUASI INFORTUNIO. Racconta un quasi infortunio che hai visto o che ti è successo (a casa, a scuola, per strada). Che cosa si poteva fare prima?", "criteri": "quasi infortunio riconosciuto e una prevenzione sensata"},
  {"area": "mia", "tema": "succede", "q": "SE SUCCEDE. Un compagno si taglia con la lamiera di un case del PC. Scrivi che cosa fai, passo per passo.", "criteri": "sicurezza propria, primo soccorso o 112, avvisare subito il preposto"}],
 "recupero": [C("sic", q, o, "", "") for n, q, o, s in ALLEN[:8]],
}
js = ("// 2INF · Sicurezza sul lavoro, 5ª ora (Regione, formazione specifica): il rischio infortuni (30/10/2026).\n"
      "// Generata da classe-2/sicurezza-5ora/_build/gen.py. Solo italiano (2INF). Nessun link al sito della Regione (#136).\n"
      "window.BANCA = " + json.dumps(banca, ensure_ascii=False, indent=1) + ";\n")
open(P + 'docs/verifica/banche/2inf-sicurezza-5ora.js', 'w', encoding='utf-8').write(js)
json.dump({"verifica": "chiusa", "recupero": "chiuso", "recupero_per": [], "_nota": "2INF 30/10: schede e ripasso aperti; il quiz è su Google Moduli (20 casi, massimo 100)."},
          open(P + 'docs/verifica/stato/2inf-sicurezza-5ora.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
cmd = {"stato": "da-eseguire",
       "nota": "29/10 sera (preparazione del 30/10): quiz su Moduli della 5ª ora di sicurezza della 2INF (rischio infortuni), 20 casi = le crocette della banca 2inf-sicurezza-5ora, 5 punti l'uno, massimo 100. Si crea ADESSO, prima della lezione (#129).",
       "azioni": [{"tipo": "forms.crea_quiz", "quiz": {
           "titolo": "Quiz — Sicurezza 5ª ora: il rischio infortuni (2INF)",
           "descrizione": "20 casi. Ogni risposta giusta vale 5 punti: massimo 100 punti. Rispondi a tutte e premi «Invia».",
           "punti": 5, "mescola": True, "versioni": ["A"],
           "domande": [{"A": ["%d) %s" % (i + 1, q), g, w]} for i, (q, g, w, t) in enumerate(QUIZ)]}}]}
f = R + 'comandi/2026-10-30_quiz-2inf-sicurezza-5ora.json'
if not os.path.exists(f):
    json.dump(cmd, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
