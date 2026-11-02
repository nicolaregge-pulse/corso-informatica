#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2INF lunedì 02/11/2026 · due banche per il motore docs/verifica/: «reti» (teoria a 6 schede + quiz di chiusura) e «phishing» (schede + quiz con messaggi nuovi).
# Solo italiano (2INF). Marchi e domini INVENTATI (.example). La verifica resta CHIUSA finché il prof non la apre (stato/*.json).
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')

def C(area, q, o, tema='', spiega=''):
    return {"tipo": "c", "area": area, "tema": tema, "q": q, "o": o, "a": 0, "spiega": spiega}

def scrivi(nome, banca, commento):
    js = "// " + commento + "\n// Generata da classe-2/phishing-0211/_build/gen_banche.py. Solo italiano (2INF). Marchi e domini inventati (.example).\nwindow.BANCA = " + json.dumps(banca, ensure_ascii=False, indent=1) + ";\n"
    open(P + 'docs/verifica/banche/%s.js' % nome, 'w', encoding='utf-8').write(js)

def vuoto(nome, titolo):
    json.dump({"titolo": titolo, "classe": "2INF", "aggiornato": "—", "come": "<b>Come si legge.</b> Le crocette si correggono da sole; le risposte scritte le legge l'assistente. Per ora nessun risultato pubblicato.", "allievi": []}, open(P + 'docs/verifica/risultati/%s.json' % nome, 'w', encoding='utf-8'), ensure_ascii=False)

def stato(nome, nota):
    json.dump({"verifica": "chiusa", "recupero": "chiuso", "recupero_per": [], "_nota": nota}, open(P + 'docs/verifica/stato/%s.json' % nome, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

STRUM = [{"t": "Il mio andamento di oggi", "u": "../anteprima/2inf-reti-02-11/cruscotto-ragazzi.html", "c": "#b45309"},
         {"t": "Torna alla pagina di oggi", "u": "../anteprima/2inf-reti-02-11/", "c": "#0b6e99"}]

# ============ RETI: IP, MAC, gateway, DNS, DHCP ============
S_RETI = [
 ("1. Che cos'è una rete", "Una <b>rete</b> è un gruppo di dispositivi collegati per parlarsi: PC, telefoni, stampanti.<br>Si collegano con un <b>cavo</b> o con il <b>Wi-Fi</b> (la rete senza fili).<br><br>Una rete piccola, come quella del laboratorio o di casa tua, si chiama <b>LAN</b> (in inglese «Local Area Network», cioè rete locale).<br><br><b>Per parlarsi, ogni dispositivo ha bisogno di un nome che gli altri capiscono: un indirizzo.</b>"),
 ("2. L'indirizzo IP: l'indirizzo di casa del PC", "L'<b>indirizzo IP</b> è l'indirizzo di casa del tuo PC nella rete. Per esempio: <b>192.168.1.25</b>.<br><br>Sono <b>quattro numeri</b> separati da punti. Ogni numero va da 0 a 255.<br>Due PC nella stessa rete <b>non possono avere lo stesso IP</b>, come due case non possono avere lo stesso numero civico nella stessa via.<br><br>L'IP può <b>cambiare</b>: se porti il telefono da casa a scuola, ha un IP diverso."),
 ("3. L'indirizzo MAC: il numero di serie della scheda di rete", "Il <b>MAC</b> è il numero di serie della <b>scheda di rete</b> (la parte del PC che si collega alla rete). Per esempio: <b>5C-BA-EF-12-34-56</b>.<br><br>Sono <b>sei coppie</b> di numeri e lettere. Lo scrive la fabbrica e <b>non cambia</b>.<br><br><b>IP = indirizzo di casa (può cambiare). MAC = numero di serie (resta sempre quello).</b>"),
 ("4. Il gateway: la porta di casa verso Internet", "Il <b>gateway</b> (in italiano «porta d'uscita») è la <b>porta della rete verso Internet</b>. Di solito è il <b>router</b>, quella scatola con le lucine. Il suo indirizzo è spesso come <b>192.168.1.1</b>.<br><br>Quando il tuo PC vuole parlare con qualcuno <b>fuori dalla rete</b> (un sito, per esempio), manda tutto al gateway, e il gateway lo porta fuori.<br><br>Senza gateway puoi parlare con i PC vicini, ma <b>non vai su Internet</b>."),
 ("5. Il DNS: la rubrica di Internet", "Per i computer un sito è un numero (un IP), ma per noi è più facile ricordare un nome, come <b>example.org</b>.<br><br>Il <b>DNS</b> è la <b>rubrica</b> che traduce il nome in numero: il tuo PC chiede «qual è il numero di questo nome?» e il DNS risponde.<br><br>Se il DNS non funziona, i siti non si aprono con il nome, anche se la rete c'è."),
 ("6. Il DHCP: chi distribuisce gli indirizzi", "Chi dà un indirizzo IP al tuo PC? Di solito <b>lo fa il router da solo</b>, con un servizio che si chiama <b>DHCP</b>.<br><br>Appena ti colleghi, il DHCP ti dà in un attimo: l'<b>IP</b>, il <b>gateway</b> e il <b>DNS</b>. Come il portiere di un albergo che ti consegna la chiave e ti dice dov'è l'uscita.<br><br>Per questo di solito non devi scrivere niente a mano: è tutto <b>automatico</b>."),
]
T_RETI = {"rete": 1, "ip": 2, "mac": 3, "gateway": 4, "dns": 5, "dhcp": 6}
AL_RETI = [
 (1, "LAN vuol dire…", ["rete locale (piccola, come quella del laboratorio)", "il nome di un sito", "un tipo di cavo elettrico"], "Local Area Network: rete locale."),
 (1, "Quale di questi si può collegare a una rete?", ["un telefono, un PC e una stampante", "solo i PC", "solo i telefoni"], "Anche telefoni e stampanti."),
 (2, "Un indirizzo IP come 192.168.1.25 è fatto da…", ["quattro numeri separati da punti", "sei coppie di lettere e numeri", "una sola parola"], "Quattro numeri con i punti."),
 (2, "Due PC nella stessa rete possono avere lo stesso IP?", ["no, ognuno ha il suo", "sì, sempre", "solo se sono dello stesso colore"], "Come due case con lo stesso numero civico: non va."),
 (3, "Il MAC è…", ["il numero di serie della scheda di rete", "l'indirizzo di casa del PC", "il nome del router"], "Numero di serie: lo scrive la fabbrica."),
 (3, "Quale tra IP e MAC può cambiare quando cambi rete?", ["l'IP", "il MAC", "tutti e due non cambiano mai"], "L'IP cambia, il MAC resta."),
 (4, "Il gateway serve per…", ["uscire dalla rete e andare su Internet", "stampare", "dare l'IP ai telefoni"], "È la porta verso Internet."),
 (5, "Il DNS fa…", ["da rubrica: traduce un nome in un numero", "da stampante", "da antivirus"], "Nome → numero."),
 (6, "Il DHCP serve a…", ["dare in automatico l'IP, il gateway e il DNS", "spegnere il router", "scaricare i giochi"], "Distribuisce gli indirizzi da solo."),
]
QZ_RETI = [  # (domanda, giusta, sbagliate, tema)
 ("Una rete piccola, come quella di casa o del laboratorio, si chiama…", "LAN", ["WAN", "USB", "HDMI"], "rete"),
 ("Il tuo PC ha l'indirizzo 192.168.1.25. Questo numero è…", "un indirizzo IP", ["un indirizzo MAC", "un numero di telefono", "il nome di un sito"], "ip"),
 ("Quale di questi può essere un indirizzo IP?", "192.168.1.40", ["5C-BA-EF-12-34-56", "www.example.org", "192.168"], "ip"),
 ("Perché due PC non possono avere lo stesso IP nella stessa rete?", "perché la rete non saprebbe a quale dei due mandare i messaggi", ["perché si rompono", "perché si spegne il router", "non è vero: possono"], "ip"),
 ("Il numero 5C-BA-EF-12-34-56 è…", "un indirizzo MAC", ["un indirizzo IP", "un gateway", "un DNS"], "mac"),
 ("Il MAC lo decide…", "la fabbrica che ha costruito la scheda di rete", ["il router ogni volta", "il professore", "il sito che visiti"], "mac"),
 ("Quale frase è giusta?", "l'IP può cambiare, il MAC di solito resta quello", ["il MAC cambia ogni giorno", "l'IP e il MAC sono la stessa cosa", "l'IP non cambia mai"], "mac"),
 ("Il gateway di una rete di casa è di solito…", "il router", ["la stampante", "il monitor", "la tastiera"], "gateway"),
 ("Se il gateway non funziona, che cosa succede?", "puoi parlare con i PC vicini ma non vai su Internet", ["il PC si spegne", "non puoi più scrivere", "si cancellano i file"], "gateway"),
 ("Scrivi «example.org» e il sito si apre. Chi ha tradotto il nome in numero?", "il DNS", ["il DHCP", "il MAC", "la stampante"], "dns"),
 ("Hai la rete ma nessun sito si apre con il nome. Quale servizio sospetti?", "il DNS", ["il MAC", "la tastiera", "lo schermo"], "dns"),
 ("Chi dà l'IP al PC in automatico quando ti colleghi?", "il DHCP", ["il DNS", "il MAC", "il monitor"], "dhcp"),
]
DATI_RETI = [
 {"tipo": "n", "area": "rete", "tema": "ip", "q": "Da quanti numeri è fatto un indirizzo IP come 192.168.1.25? Scrivi solo il numero.", "giusto": 4, "spiega": "Quattro numeri con i punti."},
 {"tipo": "n", "area": "rete", "tema": "mac", "q": "Quante coppie di numeri e lettere ha un indirizzo MAC come 5C-BA-EF-12-34-56? Scrivi solo il numero.", "giusto": 6, "spiega": "Sei coppie."},
]
banca_reti = {
 "id": "2inf-reti-ip-v1", "classe": "2INF", "titolo": "Come parla il mio PC in rete: IP, MAC, gateway, DNS",
 "sotto": "2INF · 02/11/2026 · prima le 6 schede, poi il ripasso, poi il quiz di chiusura",
 "stato": "stato/2inf-reti-ip.json", "risultati": "risultati.html?b=2inf-reti-ip", "minuti": 15, "anteprima": "1166576373",
 "aree": {"rete": {"nome": "Come parla il PC in rete", "peso": 80}, "mia": {"nome": "Con parole tue", "peso": 20}, "parere": {"nome": "Il tuo parere (non conta per il voto)", "peso": 0}},
 "schede_temi": T_RETI, "schede": [{"titolo": t, "testo": x} for t, x in S_RETI], "strumenti": STRUM,
 "via": C("rete", "Quale di questi si può collegare a una rete?", ["un telefono, un PC e una stampante", "solo i PC", "solo i telefoni"], "rete", "Anche telefoni e stampanti."),
 "prepara": [
  {"q": "Prova a dire con parole tue: a cosa serve l'indirizzo IP? Scrivi una frase.", "aiuto": "Pensa all'indirizzo di casa."},
  {"q": "Che cosa è più facile ricordare: un nome come example.org o un numero? Perché serve il DNS?", "aiuto": "Pensa alla rubrica del telefono."}],
 "allenamento": [dict(C("rete", q, o, "", s), scheda=n) for n, q, o, s in AL_RETI],
 "crocette": [C("rete", q, [g] + w, t) for q, g, w, t in QZ_RETI],
 "dati": DATI_RETI,
 "scale": [{"area": "parere", "q": "Quanto ti senti sicuro a leggere l'IP del tuo PC da solo?", "basso": "per niente", "alto": "moltissimo", "ultima": True}],
 "aperte": [
  {"area": "mia", "tema": "gateway", "q": "A COSA SERVE IL GATEWAY. Spiega con parole tue, come a un compagno, a cosa serve il gateway. Puoi fare un esempio con la porta di casa.", "criteri": "porta verso Internet, router, senza gateway niente Internet"},
  {"area": "mia", "tema": "dns", "q": "A COSA SERVE IL DNS. Spiega con parole tue che cosa fa il DNS e che cosa succede se non funziona.", "criteri": "traduce i nomi in numeri (rubrica); senza DNS i siti non si aprono con il nome"}],
 "recupero": [C("rete", q, o, "", "") for n, q, o, s in AL_RETI[:8]],
}
for i, r in enumerate(banca_reti["recupero"]): r["tema"] = list(T_RETI)[min(AL_RETI[i][0] - 1, 5)]
scrivi("2inf-reti-ip", banca_reti, "2INF · Reti: IP, MAC, gateway, DNS, DHCP (02/11/2026).")
vuoto("2inf-reti-ip", "Come parla il mio PC in rete"); stato("2inf-reti-ip", "2INF 02/11: schede e ripasso aperti; il quiz di chiusura resta chiuso finché il prof non lo apre.")

# ============ PHISHING ============
S_PH = [
 ("1. Che cos'è il phishing", "<b>Phishing</b> si legge «fìscing» e viene da «fishing», che in inglese vuol dire <b>pescare</b>.<br>Il truffatore ti manda un messaggio che è l'<b>esca</b> (una mail, un SMS, un messaggio su WhatsApp). Se ci caschi, ti prende <b>password, dati della carta o soldi</b>.<br><br>Si chiama anche <b>ingegneria sociale</b>: non ingannano il computer, ingannano <b>te</b>. Possono farlo anche con un messaggio scritto benissimo."),
 ("2. Chi scrive: guarda l'indirizzo, non il nome", "Sotto il nome c'è l'<b>indirizzo</b> di chi scrive, per esempio <b>assistenza@bancanova.example</b>. La parte dopo la chiocciola (<b>bancanova.example</b>) è il <b>dominio</b>: è il vero «cognome» del mittente.<br><br>Il <b>nome</b> lo può scrivere chiunque. Il dominio no.<br>I truffatori usano domini <b>quasi uguali</b>: una «rn» al posto della «m» (postaprirna), un «1» al posto della «i», un trattino in più (bancanova-<b>sicurezza</b>).<br><br>Prova: se il dominio non è <b>esattamente</b> quello vero, non ti fidare."),
 ("3. Fretta e paura", "Chi ti truffa vuole che tu <b>non abbia il tempo di pensare</b>.<br>Per questo scrive: «subito», «entro 24 ore», «il conto sarà chiuso», «hai vinto!».<br><br>Una mail vera di solito è <b>calma</b>. Se ti mette <b>fretta</b> o ti fa <b>paura</b>, fermati: è proprio il momento di <b>non cliccare</b>."),
 ("4. Il saluto e gli errori", "«<b>Gentile cliente</b>», «<b>Caro utente</b>»: un saluto generico può voler dire che la mail è stata mandata a mille persone.<br>Anche gli <b>errori di scrittura</b> e le frasi strane sono un indizio.<br><br><b>Attenzione:</b> i truffatori più bravi scrivono bene e usano il tuo nome. Gli indizi vanno guardati <b>tutti insieme</b>, e l'indirizzo e il link contano più degli altri."),
 ("5. Il link e gli allegati", "Un bottone può <b>nascondere</b> un altro indirizzo. Prima di cliccare, <b>passa il mouse sopra</b> senza premere: in basso a sinistra il programma mostra dove porta davvero.<br><br>Se il sito è diverso da quello del mittente, <b>non cliccare</b>.<br>Gli <b>allegati</b> che non aspetti (specialmente <b>.zip</b> e <b>.exe</b>) possono contenere virus: non aprirli."),
 ("6. Che cosa fai se ricevi una mail strana", "<b>1.</b> <b>Non cliccare</b> e non aprire gli allegati.<br><b>2.</b> <b>Non rispondere</b> e non scrivere password o dati.<br><b>3.</b> Per controllare, vai al sito o all'app <b>scrivendo tu l'indirizzo</b> (non dal link della mail), oppure chiedi a un adulto o al prof.<br><b>4.</b> <b>Segnala</b> e <b>cancella</b> la mail.<br><br><b>Se hai già cliccato o scritto la password:</b> cambia subito la password e avvisa un adulto o il prof. Succede anche ai professionisti: l'importante è dirlo subito.<br><br><b>Una password non te la chiede mai nessuno</b>: né la banca, né la scuola, né un amico."),
]
T_PH = {"phishing": 1, "mittente": 2, "fretta": 3, "saluto": 4, "link": 5, "cosa": 6}
AL_PH = [
 (1, "Il «phishing» è…", ["un messaggio che cerca di farti dare password, dati o soldi", "un tipo di videogioco", "un programma per fare foto"], "È l'esca per «pescare» i tuoi dati."),
 (2, "Di una mail guardi per prima cosa…", ["l'indirizzo di chi scrive, dopo la chiocciola", "il colore del bottone", "l'ora di arrivo"], "Il dominio non si può inventare uguale a quello vero."),
 (2, "Il vero dominio della banca è bancanova.example. Quale indirizzo è sospetto?", ["assistenza@bancanova-sicurezza.example", "avvisi@bancanova.example", "info@bancanova.example"], "C'è «-sicurezza» in più: dominio diverso."),
 (2, "Quale dominio è fatto per ingannare chi legge di fretta?", ["postaprirna.example (al posto di postaprima.example)", "postaprima.example", "www.postaprima.example"], "«rn» sembra una «m»."),
 (3, "«Conferma subito o il conto sarà chiuso in 12 ore!» Questa frase è…", ["un segnale di pericolo: mette fretta", "normale, vuol dire che è urgente davvero", "un regalo"], "Fretta e paura: tipico del phishing."),
 (4, "«Gentile cliente» senza il tuo nome è un indizio?", ["sì, ma da solo non basta", "no, mai", "sì, e basta per essere certi"], "Va guardato insieme agli altri indizi."),
 (5, "Prima di cliccare un bottone in una mail, cosa puoi fare?", ["passarci sopra con il mouse e leggere dove porta", "cliccare in fretta", "stampare la mail"], "In basso a sinistra vedi l'indirizzo vero."),
 (6, "Un messaggio ti chiede la password. Che cosa fai?", ["non la do e controllo sul sito vero scrivendo io l'indirizzo", "la scrivo, è urgente", "la mando a un amico"], "La password non si dà a nessuno."),
 (6, "Hai cliccato per sbaglio e scritto la password. Che cosa fai?", ["cambio subito la password e avviso un adulto o il prof", "aspetto e spero", "non lo dico a nessuno"], "Si dice subito: così si rimedia in fretta."),
]
def sms(testo, da):
    return ('<div style="background:#eef3f8;border:1px solid #9fb2c6;border-radius:12px;padding:10px 14px;margin:8px 0;font-size:.95em">'
            '<div style="color:#4a5563;font-size:.85em">%s</div>%s</div>' % (da, testo))
M = [  # messaggi nuovi per il quiz: (testo, da, giusto='phishing'|'sicuro', indizio giusto, sbagliati)
 (sms("Corrierexpress: il tuo pacco è bloccato. Sblocca subito qui: http://sblocca-pacco-corriere.example/x1", "SMS da numero sconosciuto, 03:20"), "phishing",
  "il link e la fretta, e non c'è nessun nome né numero di spedizione", ["il messaggio è troppo lungo", "il messaggio è scritto in italiano", "arriva di notte, ed è normale"], "link"),
 (sms("Ciao mamma, ho rotto il telefono e questo è il mio numero nuovo. Puoi fare un bonifico urgente? Ti spiego dopo!", "Messaggio WhatsApp da numero nuovo"), "phishing",
  "un numero nuovo che chiede soldi con urgenza: prima si chiama il numero vero", ["il messaggio parla di un telefono", "ha il saluto «ciao»", "non ci sono indizi"], "fretta"),
 (sms("BancaNova: il codice per il tuo acquisto è 482915. Non dirlo a nessuno: BancaNova non te lo chiederà mai.", "SMS da «BancaNova», dopo che hai pagato tu online"), "sicuro",
  "è un codice che ti serve per un acquisto fatto proprio da te e non c'è nessun link", ["ha dei numeri, quindi è phishing", "nomina la banca, quindi è phishing", "dice «non dirlo a nessuno»"], "link"),
 (sms("Istituto Orizzonti: domani la lezione inizia alle 9:00 invece che alle 8:00. Buona serata!", "SMS dalla scuola, numero già salvato in rubrica"), "sicuro",
  "è un avviso senza link e senza richieste, da un numero che conosci", ["la scuola non scrive mai SMS", "dice «buona serata»", "contiene un orario"], "saluto"),
]
QZ_PH = []
for i, (t, g, ind, sb, tema) in enumerate(M, 1):
    QZ_PH.append(C("ph", "<b>Messaggio %d.</b> Leggi con calma.%s Questo messaggio è…" % (i, t), ["un messaggio sicuro" if g == "sicuro" else "phishing (una truffa)", "phishing (una truffa)" if g == "sicuro" else "un messaggio sicuro"], tema))
    QZ_PH.append(C("ph", "<b>Messaggio %d.</b> Qual è l'indizio più importante per decidere?" % i, [ind] + sb, tema))
QZ_PH += [
 C("ph", "Il vero dominio di PostaPrima è postaprima.example. Quale mittente è quello vero?", ["notifiche@postaprima.example", "notifiche@postaprirna.example", "notifiche@posta-prima-spedizioni.example", "notifiche@postaprima-tracking.example"], "mittente"),
 C("ph", "Una mail dice «la tua password scade oggi, scrivi la password attuale nel modulo». Che cosa fai?", ["non scrivo niente: nessuno deve chiedermi la password", "la scrivo, così non la perdo", "la scrivo ma poi la cambio"], "cosa"),
 C("ph", "Ricevi una mail con un allegato .zip da un mittente che non conosci. Che cosa fai?", ["non lo apro e cancello la mail", "lo apro per vedere cosa c'è", "lo inoltro ai compagni"], "link"),
 C("ph", "Il phishing è difficile da riconoscere perché…", ["i truffatori possono scrivere bene e usare il tuo nome", "è sempre scritto male", "arriva solo la notte"], "phishing"),
]
banca_ph = {
 "id": "2inf-phishing-v1", "classe": "2INF", "titolo": "Phishing: riconosco la truffa",
 "sotto": "2INF · 02/11/2026 · sicurezza informatica · prima le schede, poi il ripasso, poi il quiz (messaggi nuovi)",
 "stato": "stato/2inf-phishing.json", "risultati": "risultati.html?b=2inf-phishing", "minuti": 15, "anteprima": "1294333367",
 "aree": {"ph": {"nome": "Riconosco il phishing", "peso": 80}, "mia": {"nome": "Con parole tue", "peso": 20}, "parere": {"nome": "Il tuo parere (non conta per il voto)", "peso": 0}},
 "schede_temi": T_PH, "schede": [{"titolo": t, "testo": x} for t, x in S_PH], "strumenti": STRUM,
 "via": C("ph", "Il «phishing» è…", ["un messaggio che cerca di farti dare password, dati o soldi", "un tipo di videogioco", "un programma per fare foto"], "phishing", "È l'esca per «pescare» i tuoi dati."),
 "prepara": [
  {"q": "Hai mai ricevuto un messaggio strano (mail, SMS, WhatsApp)? Racconta in due righe che cosa diceva, senza nomi.", "aiuto": "Anche un messaggio che ti ha insospettito va bene."},
  {"q": "Come fai a capire se una mail è vera? Scrivi due cose che controlli.", "aiuto": "Pensa all'indirizzo e al link."}],
 "allenamento": [dict(C("ph", q, o, "", s), scheda=n) for n, q, o, s in AL_PH],
 "crocette": QZ_PH,
 "scale": [{"area": "parere", "q": "Quanto ti senti sicuro a riconoscere un messaggio di phishing?", "basso": "per niente", "alto": "moltissimo", "ultima": True}],
 "aperte": [
  {"area": "mia", "tema": "cosa", "q": "CHE COSA FAI. Ti arriva un messaggio che dice che il tuo account sta per essere chiuso. Scrivi con parole tue che cosa fai, passo per passo.", "criteri": "non cliccare, non dare dati, controllare dal sito vero scrivendo l'indirizzo, chiedere a un adulto o al prof, segnalare"},
  {"area": "mia", "tema": "mittente", "q": "COME CONTROLLI IL MITTENTE. Spiega a un compagno come si controlla chi ti ha scritto davvero.", "criteri": "guardare l'indirizzo dopo la chiocciola (dominio), confrontarlo con quello vero, attenzione a lettere cambiate"}],
 "recupero": [C("ph", q, o, "", "") for n, q, o, s in AL_PH],
}
for i, r in enumerate(banca_ph["recupero"]): r["tema"] = list(T_PH)[min(AL_PH[i][0] - 1, 5)]
scrivi("2inf-phishing", banca_ph, "2INF · Phishing: riconosco la truffa (02/11/2026).")
vuoto("2inf-phishing", "Phishing: riconosco la truffa"); stato("2inf-phishing", "2INF 02/11: schede e ripasso aperti; il quiz resta chiuso finché il prof non lo apre.")
print('banche ok')
