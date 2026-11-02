#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Compiti di mercoledì 04/11/2026 in coda come BOZZA invisibile (stesso meccanismo di martedì), UN compito per ora.
# I link dei Moduli sono segnaposto __QUIZ1__ / __QUIZ2__ / __QUIZ3__: li riempie strumenti/riempi_link_04_11.py quando il ponte ha creato i Moduli.
# 3INF ora 1: il compito del client lo ha creato a mano il docente (non modificabile): NON si accoda, il testo pronto sta nel piano B.
import json, os
R = '/home/user/corso-informatica-riservato/coda/'
U = 'https://nicolaregge-pulse.github.io/corso-informatica/anteprima/'
NOTA = ("04/11/2026 preparazione: BOZZA (DRAFT) invisibile ai ragazzi, con scadenza di una settimana perche il ponte la richiede (regola 27 dice senza scadenza: la si toglie a mano). "
        "Si mostra con classroom.mostra solo quando il docente lo dice, UN'ORA PER VOLTA (regola 31). Prima di creare/mostrare: strumenti/prima_di_pubblicare.sh (regola 34). Il Modulo e creato dal ponte e solo collegato nel testo.")
F5 = "La pagina viene aggiornata spesso durante la lezione: premi F5 per vedere la versione nuova."
AIUTO = "Hai una domanda? Scrivila nella casella dell'assistente, in fondo alla pagina di oggi."
COMP = [
 ('1INF_ora1-convertitore', '1INF', '4/11 Ora 1: Convertitore di misure (Lazarus)', '1inf-0411-ora1',
  "OGGI 4/11, ORA 1: il convertitore di misure in Lazarus (km in metri, ore in minuti, euro in centesimi, Celsius in Fahrenheit, minuti in ore e minuti).\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "1inf-lab-04-11/modulo-1.html <<<\n" + F5 + "\nLa pagina è in italiano, arabo e cinese · الصفحة بالإيطالية والعربية والصينية · 页面有意大利语、阿拉伯语和中文。\n\nPASSO 1: quiz breve su Moduli (testo contro numero):\n__QUIZ1__\nPASSI 2-12: il convertitore, un bottone alla volta.\nA FINE ORA: consegna unit1.pas e lo screenshot con il bottone «Manda al prof» e ricopia sul quaderno il riquadro giallo.\n\nA che punto sono:\n" + U + "1inf-lab-04-11/cruscotto-ragazzi.html\n\n" + AIUTO),
 ('1INF_ora2-calcolatrice', '1INF', '4/11 Ora 2: Calcolatrice a 4 bottoni (Lazarus)', '1inf-0411-ora2',
  "OGGI 4/11, ORA 2: la calcolatrice a 4 bottoni in Lazarus (con StrToIntDef e il risultato scritto come frase).\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "1inf-lab-04-11/modulo-2.html <<<\n" + F5 + "\n\nA FINE ORA: consegna unit1.pas e lo screenshot con il bottone «Manda al prof» e ricopia sul quaderno il riquadro giallo.\n\nA che punto sono:\n" + U + "1inf-lab-04-11/cruscotto-ragazzi.html\n\n" + AIUTO),
 ('1INF_ora3-cassiere', '1INF', '4/11 Ora 3: Il cassiere (Lazarus)', '1inf-0411-ora3',
  "OGGI 4/11, ORA 3: il cassiere in Lazarus (il resto, banconote e monete con div e mod, lo scontrino con il nome del cliente).\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "1inf-lab-04-11/modulo-3.html <<<\n" + F5 + "\n\nA FINE ORA: consegna unit1.pas e lo screenshot con il bottone «Manda al prof» e ricopia sul quaderno il riquadro giallo.\n\nA che punto sono:\n" + U + "1inf-lab-04-11/cruscotto-ragazzi.html\n\n" + AIUTO),
 ('2INF_sicurezza-6ora', '2INF', '4/11 Sicurezza, 6ª ora: macchine e corrente', '2inf-0411-sicurezza6',
  "OGGI 4/11, SICUREZZA, 6ª ORA: i rischi meccanici ed elettrici generali.\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "2inf-sicurezza-04-11/ <<<\n" + F5 + "\n\nPASSO 1: leggi le 8 schede.\nPASSO 2: il ripasso (6 domande).\nPASSO 3: il quiz su Moduli, 20 casi, 5 punti l'uno (massimo 100):\n__QUIZ2__\n\nA che punto sono:\n" + U + "2inf-sicurezza-04-11/cruscotto-ragazzi.html\n\n" + AIUTO),
 ('3INF_ora2-partita-github-quiz', '3INF', '4/11 Ora 2: partita di classe, GitHub e quiz (Mastermind in rete)', '3inf-0411-ora2',
  "OGGI 4/11, ORA 2: la partita di classe del Mastermind in rete, il progetto su GitHub con un commit dal messaggio chiaro e il quiz.\nApri questa pagina: c'è tutto, passo per passo.\n>>> " + U + "3inf-mastermind-04-11/ora2.html <<<\n" + F5 + "\n\nA che punto sono:\n" + U + "3inf-mastermind-04-11/cruscotto-ragazzi.html\n\n" + AIUTO),
]
if __name__ == '__main__':
    for nome, classe, titolo, cart, desc in COMP:
        f = R + '2026-11-04_%s.json' % nome
        if os.path.exists(f): print('esiste già', nome); continue
        json.dump({"stato": "da-pubblicare", "bozza": True, "nota": NOTA, "classe": classe, "titolo": titolo, "cartella": cart,
                   "cartella_drive": "%s - %s" % (classe, cart), "base_url": "", "pdf": [], "descrizione": desc, "scadenza_iso": "2026-11-10T22:59:00Z"},
                  open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('creato', nome)
