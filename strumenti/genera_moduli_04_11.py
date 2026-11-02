#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Moduli (quiz) di mercoledì 04/11/2026: SOLO creazione col ponte (forms.crea_quiz), nessun allegato a Classroom.
# Scrive in riservato comandi/2026-11-04_MODULO-*.json (stato da-eseguire). Nessun nome di ragazzi.
import json, os
R = '/home/user/corso-informatica-riservato/comandi/'

def quiz(titolo, descr, punti, dom):
    return {"titolo": titolo, "descrizione": descr, "punti": punti, "mescola": True, "versioni": ["A"],
            "domande": [{"A": ["%d) %s" % (i + 1, q), g, w, ""]} for i, (q, g, w) in enumerate(dom)]}

Q1 = [  # 1INF, ora 1: testo contro numero (it / ar / zh nella domanda)
 ("Che cosa mostra  Label1.Caption := '5' + '3';\nماذا يعرض هذا السطر؟\n这一行会显示什么？", "53", ["8", "errore"]),
 ("a := 5; b := 3;  Label1.Caption := IntToStr(a + b);  Che cosa mostra?\nماذا يعرض؟\n会显示什么？", "8", ["53", "5 + 3"]),
 ("Che cosa mostra  Label1.Caption := '10' + '20';\nماذا يعرض؟\n会显示什么？", "1020", ["30", "errore"]),
 ("Quale istruzione trasforma il testo della casella in numero?\nأي تعليمة تحوّل نص الخانة إلى رقم؟\n哪个指令把输入框的文字变成数字？", "StrToInt", ["IntToStr", "Caption"]),
 ("Quale istruzione trasforma un numero in testo da mettere nella Label?\nأي تعليمة تحوّل الرقم إلى نص؟\n哪个指令把数字变成文字放进 Label？", "IntToStr", ["StrToInt", "Edit1.Text"]),
 ("17 div 5 fa…\n17 div 5 يساوي…\n17 div 5 等于…", "3", ["3,4", "2"]),
 ("17 mod 5 fa…\n17 mod 5 يساوي…\n17 mod 5 等于…", "2", ["3", "12"]),
 ("Celsius in Fahrenheit con 20 gradi: 20 * 9 div 5 + 32 fa…\n20 * 9 div 5 + 32 يساوي…\n20 * 9 div 5 + 32 等于…", "68", ["52", "36"]),
]
Q2 = [  # 2INF, Sicurezza 6ª ora: rischi meccanici ed elettrici generali (20 casi, 5 punti l'uno)
 ("Un organo meccanico in movimento è…", "una parte della macchina che si muove (ingranaggio, cinghia, lama)", ["il motore spento", "il quadro elettrico", "il cartello di sicurezza"]),
 ("C'è rischio di schiacciamento quando…", "una parte del corpo resta stretta tra due parti che si avvicinano", ["la macchina fa rumore", "la macchina è spenta", "si usa il casco"]),
 ("Perché non si portano sciarpe, cravatte e braccialetti vicino a una macchina che gira?", "possono impigliarsi e trascinare la mano o il corpo", ["si sporcano", "danno fastidio al capo", "non c'è un motivo"]),
 ("Hai i capelli lunghi e usi un trapano a colonna. Che cosa fai?", "li lego e li raccolgo", ["li lascio sciolti", "li taglio ogni volta", "non c'è rischio"]),
 ("Un riparo fisso su una macchina serve a…", "impedire di toccare le parti pericolose", ["abbellire la macchina", "farla andare più veloce", "fare meno rumore soltanto"]),
 ("Il riparo con interblocco…", "ferma la macchina se lo apri", ["si toglie senza fermare la macchina", "serve solo per il rumore", "accende la macchina da solo"]),
 ("Il pulsante di emergenza (fungo rosso) serve a…", "fermare subito la macchina", ["accendere la macchina", "regolare la velocità", "cambiare l'utensile"]),
 ("La protezione di una macchina è rotta. Che cosa fai?", "fermo la macchina e avviso subito il preposto", ["la uso lo stesso con attenzione", "tolgo la protezione", "aspetto che qualcuno se ne accorga"]),
 ("Prima di pulire o riparare una macchina bisogna…", "fermarla, staccare l'energia e metterla in sicurezza", ["pulirla mentre gira piano", "farla tenere accesa da un compagno", "mettere solo un guanto"]),
 ("Il cartello «Non azionare, lavori in corso» sull'interruttore serve a…", "evitare che qualcuno riaccenda la macchina mentre ci lavori", ["decorare il quadro", "dire che la macchina è nuova", "segnalare uno sciopero"]),
 ("Il rischio elettrico è…", "il rischio che la corrente passi nel corpo e faccia male", ["il rischio che si rompa il computer", "il rischio di inciampare nei cavi", "un rischio che esiste solo nelle fabbriche"]),
 ("Contatto diretto significa…", "toccare una parte che è normalmente in tensione (per esempio un filo scoperto)", ["toccare un cavo spento", "guardare un cavo da lontano", "toccare una parte che era in tensione per un guasto"]),
 ("Contatto indiretto significa…", "toccare una parte che di solito non è in tensione ma lo è diventata per un guasto (per esempio una carcassa)", ["toccare un filo scoperto", "toccare una pila da 1,5 volt", "usare un telecomando"]),
 ("Quanto è pericolosa la corrente dipende da…", "intensità, tempo di passaggio e percorso nel corpo", ["solo dal colore del cavo", "solo dall'ora del giorno", "solo dal tipo di spina"]),
 ("Le mani bagnate vicino a una presa…", "aumentano molto il rischio elettrico", ["non cambiano niente", "diminuiscono il rischio", "proteggono dalla scossa"]),
 ("Il salvavita (interruttore differenziale) serve a…", "staccare la corrente se una parte si disperde, per esempio nel corpo", ["far costare meno la bolletta", "aumentare la tensione", "proteggere dai ladri"]),
 ("La messa a terra serve a…", "mandare nel terreno la corrente in caso di guasto", ["aumentare la potenza", "far andare più veloce il PC", "tenere ferma la spina"]),
 ("Un cavo con la guaina rovinata e il filo visibile…", "non si usa: si toglie l'alimentazione e si segnala al preposto", ["si ripara con il nastro adesivo e si continua", "si usa ma senza toccarlo", "si bagna per raffreddarlo"]),
 ("Un collega prende la scossa e resta attaccato al cavo. Prima di tutto…", "tolgo la corrente (interruttore o spina) senza toccarlo, poi chiamo il 112", ["lo tiro via con le mani", "gli butto addosso dell'acqua", "aspetto dieci minuti"]),
 ("Una ciabatta con altre ciabatte attaccate una dopo l'altra…", "può surriscaldarsi e causare un incendio", ["è sempre sicura", "fa risparmiare energia", "non cambia niente"]),
]
Q3 = [  # 3INF: Mastermind in rete (8 domande)
 ("Nel Mastermind in rete, che cosa fa il CLIENT?", "è il programma con cui ogni giocatore prova i codici e che si collega al server", ["pensa il codice segreto per tutta la classe", "è il cavo di rete", "è la classifica stampata"]),
 ("Che cosa fa il SERVER?", "pensa il codice segreto, controlla i tentativi e tiene la classifica", ["è il programma con cui si prova il codice", "serve solo a stampare", "spegne i client"]),
 ("Per collegare il client al server servono…", "l'indirizzo IP e la porta del server", ["solo il tuo nome", "solo la password del Wi-Fi", "il numero del banco"]),
 ("Qual è la porta del nostro server?", "5050", ["80", "443", "21"]),
 ("Nel risultato di un tentativo il piolo NERO vuol dire…", "colore giusto al posto giusto", ["colore giusto al posto sbagliato", "colore sbagliato", "hai perso un turno"]),
 ("Il piolo BIANCO vuol dire…", "colore giusto al posto sbagliato", ["colore giusto al posto giusto", "colore sbagliato", "tentativo finito"]),
 ("Perché i PC si vedano in rete devono stare…", "nella stessa rete (stessa maschera, per esempio 255.255.255.0)", ["in due reti diverse senza router", "spenti", "collegati solo con il Bluetooth"]),
 ("Se il server è spento e premi Connetti, che cosa succede?", "compare un errore di connessione (rifiutata o nessuna risposta)", ["il programma indovina il codice da solo", "la partita parte lo stesso", "il PC si spegne"]),
]
MOD = {
 '1inf-lab-0411-testo-numero': ("Quiz — Testo contro numero (1INF, 04/11)", "8 domande su String e Integer: '5' + '3' contro 5 + 3.\n8 أسئلة عن String و Integer.\n8 道关于 String 和 Integer 的题。", 1, Q1, "1INF ora 1 del 04/11: quiz breve su testo contro numero. 8 domande, 1 punto l'una."),
 '2inf-sicurezza-6ora': ("Quiz — Sicurezza 6ª ora: rischi meccanici ed elettrici (2INF)", "20 casi. Ogni risposta giusta vale 5 punti: massimo 100 punti. Rispondi a tutte e premi «Invia».", 5, Q2, "2INF Sicurezza 6ª ora (rischi meccanici ed elettrici generali): 20 casi, 5 punti l'uno, massimo 100."),
 '3inf-mastermind-rete': ("Quiz — Mastermind in rete: client, server, IP e porta (3INF)", "8 domande sul Mastermind in rete. Ogni risposta giusta vale 1 punto.", 1, Q3, "3INF ora 2 del 04/11: quiz sul Mastermind in rete, 8 domande."),
}
if __name__ == '__main__':
    for k, (tit, desc, pt, dom, nota) in MOD.items():
        f = R + '2026-11-04_MODULO-%s-quiz.json' % k
        if os.path.exists(f):
            print('esiste già', f); continue
        json.dump({"stato": "da-eseguire", "nota": "04/11/2026 preparazione: " + nota + " SOLO creazione: nessun allegato a Classroom, non visibile ai ragazzi finche il link non viene messo in una pagina aperta.",
                   "azioni": [{"tipo": "forms.crea_quiz", "quiz": quiz(tit, desc, pt, dom)}]},
                  open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('creato', os.path.basename(f), len(dom), 'domande')
