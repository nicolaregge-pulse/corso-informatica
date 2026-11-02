#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2INF 11-12 Sicurezza (6ª ora: rischi meccanici ed elettrici generali) e 3INF 12-14 Mastermind in rete, mercoledì 04/11/2026.
# Voci Allegato A (PFP_2 Comp. 14, II anno; PFP_3 Comp. 16 e Comp. 12, III anno). Tutto CHIUSO (ore_sbloccate 0). Nessun nome di ragazzi.
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_pagine_lezione import *

SRC = SLUGDIR + '1inf-deepfake-03-11/ore.js'

def conf(d, nota, extra=None):
    c = {"invio": INVIO, "attivo": True, "ore_sbloccate": 0, "_nota": nota, "_ore": "0 = tutta chiusa; il docente alza di UNA ora alla volta (regola 31): strumenti/sblocca_ora.py"}
    if extra: c.update(extra)
    json.dump(c, open(d + 'config.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    shutil.copy(SRC, d + 'ore.js')

def P(t, x, img, alt='', code=None, extra=None, bn=None, bnt=None):
    return dict(t=t, x=x, img=img, alt=alt, code=code, extra=extra, xl={'bn': bn} if bn else {}, tl={'bn': bnt} if bnt else {})

# ======================= 2INF =======================
S2 = '2inf-sicurezza-04-11'; D2 = SLUGDIR + S2 + '/'; os.makedirs(D2 + 'img', exist_ok=True)
svg(D2 + 'img/schede.svg', 'Le 8 schede', [('box', '8 schede: leggile in ordine\n1 ripasso · 2-5 macchine · 6-8 corrente', 80, 90, 640, 100), ('btn', 'Apri la scheda 1', 160, 240, 480)], (0,), 'Clicca il titolo di ogni scheda per aprirla')
svg(D2 + 'img/ripasso.svg', 'Ripasso', [('box', 'Prima pensa la risposta,\npoi clicca per vedere quella giusta', 80, 90, 640, 100), ('btn', 'Vedi la risposta', 160, 240, 480)], (1,), '6 domande, niente voto')
svg(D2 + 'img/quiz.svg', 'Quiz su Google Moduli', [('box', '20 casi · 5 punti l\'uno\nrispondi a tutte e premi Invia', 80, 90, 640, 100), ('btn', 'Apri il quiz', 160, 240, 480)], (1,), 'Il quiz è la prova: lavoro tuo')
svg(D2 + 'img/fine.svg', 'Chi ha finito', [('box', 'Rileggi le schede che\nhai sbagliato nel quiz', 80, 90, 640, 100), ('box', 'Poi guarda il tuo andamento', 80, 230, 640, 60)], (0,), 'Aspetta il Prof senza uscire')
SCHEDE = [
 ("1. Ripasso in un minuto (5ª ora)", "<b>Infortunio</b>: un evento improvviso che ti fa male mentre lavori. <b>Quasi infortunio</b>: poteva farti male ma non è successo (si segnala sempre). <b>In itinere</b>: sulla strada da casa al lavoro. <b>INAIL</b>: l'assicurazione degli infortuni, la paga il datore di lavoro."),
 ("2. Che cos'è un rischio meccanico", "Il <b>rischio meccanico</b> nasce dalle parti di una macchina che si muovono: ingranaggi, cinghie, lame, rulli, pistoni. Succede anche vicino a noi: le ventole di un PC, le stampanti, le porte automatiche, i carrelli."),
 ("3. Come ci si fa male con le macchine", "<b>Schiacciamento</b>: resti stretto tra due parti che si avvicinano. <b>Taglio</b>: una lama ti taglia. <b>Trascinamento e impigliamento</b>: sciarpe, cravatte, braccialetti e capelli lunghi finiscono dentro. <b>Cesoiamento</b>: due parti si incrociano come le forbici. <b>Proiezione</b>: schegge e pezzi che volano via."),
 ("4. Le protezioni delle macchine", "<b>Riparo fisso</b>: una protezione avvitata che non si toglie. <b>Riparo con interblocco</b>: se lo apri la macchina si ferma. <b>Sensori</b> (per esempio le fotocellule): fermano la macchina se passi. <b>Pulsante di emergenza</b>: il fungo rosso, ferma subito tutto. <b>Mai</b> togliere o bloccare una protezione."),
 ("5. Prima di pulire o riparare", "1. <b>Fermo</b> la macchina. 2. <b>Stacco</b> l'energia (corrente o aria compressa). 3. Metto il cartello «Non azionare, lavori in corso» sull'interruttore. 4. <b>Controllo</b> che sia davvero ferma. Solo dopo ci metto le mani. Se la protezione è rotta, non uso la macchina e avviso il preposto."),
 ("6. Il rischio elettrico", "<b>Contatto diretto</b>: tocchi una parte che è normalmente in tensione, per esempio un filo scoperto. <b>Contatto indiretto</b>: tocchi una parte che di solito non è in tensione ma lo è diventata per un guasto, per esempio la carcassa di un apparecchio. La corrente delle prese (230 volt) è pericolosa."),
 ("7. Che cosa fa la corrente al corpo", "Dipende da <b>quanta</b> corrente passa, per <b>quanto tempo</b> e da <b>dove</b> passa (mano-mano o mano-piede è peggio perché attraversa il cuore). Può far contrarre i muscoli (non riesci a staccarti), fare ustioni e fermare il cuore. Le <b>mani bagnate</b> o l'acqua aumentano molto il rischio."),
 ("8. Come ci si protegge e che cosa si fa se succede", "<b>Isolamento</b> dei cavi, <b>messa a terra</b>, <b>salvavita</b> (interruttore differenziale). Non uso cavi rovinati, non attacco ciabatte una all'altra, non tocco prese con le mani bagnate. <b>Se succede</b>: tolgo la corrente (interruttore o spina) <b>senza toccare</b> il collega, chiamo il <b>112</b>, avviso il preposto."),
]
RIP = [("Che cos'è un rischio meccanico?", "Il rischio che nasce dalle parti di una macchina che si muovono."),
       ("Perché sciarpe e cravatte sono pericolose vicino a una macchina che gira?", "Si impigliano e trascinano la mano o il corpo."),
       ("A che serve il riparo con interblocco?", "Se lo apri, la macchina si ferma."),
       ("Prima di riparare una macchina che cosa fai?", "La fermo, stacco l'energia, metto il cartello e controllo che sia ferma."),
       ("Che differenza c'è tra contatto diretto e indiretto?", "Diretto: tocchi una parte in tensione (filo scoperto). Indiretto: tocchi una parte diventata in tensione per un guasto (carcassa)."),
       ("Un collega è attaccato a un cavo elettrico. Che cosa fai?", "Tolgo la corrente senza toccarlo e chiamo il 112.")]
det = lambda t, x: '<details class="card"><summary>%s</summary><p>%s</p></details>' % (t, x)
sc = ''.join(det(t, x) for t, x in SCHEDE)
rp = ''.join(det(q, a) for q, a in RIP)
PASSI2 = [
    P('Leggi le 8 schede', 'Clicca il titolo di ogni scheda e leggila. Quando hai letto tutte e 8, premi «Ho fatto!». Non serve correre: il quiz viene dopo.', 'schede.svg', 'Schede', extra=sc),
    P('Ripasso: 6 domande', 'Pensa la risposta, poi clicca la domanda per vedere quella giusta. Non conta per il voto: serve per prepararti.', 'ripasso.svg', 'Ripasso', extra=rp),
    P('Il quiz su Google Moduli', 'Premi il bottone verde: sono <b>20 casi</b>, 5 punti l\'uno, massimo 100. Rispondi a tutti e premi <b>Invia</b>. Il quiz è la tua prova: lavoro tuo, senza aiuto dei compagni.', 'quiz.svg', 'Quiz Moduli',
      extra='<a class="bt v" href="__QUIZ2__" target="_blank" rel="noopener">Apri il quiz di sicurezza</a>'),
    P('Hai finito prima degli altri?', 'Rileggi le schede delle domande che hai sbagliato. Poi aspetta il Prof senza uscire dall\'aula.', 'fine.svg', 'Rileggi'),
]
conf(D2, "2INF 04/11/2026, Sicurezza 6a ora (rischi meccanici ed elettrici generali; Allegato A PFP_2 Comp. 14, II anno). Pagina CHIUSA finche il docente non sblocca (regola 31).")
h = pagina(S2, '2INF', 'Sicurezza sul lavoro · 6ª ora: macchine e corrente', '2INF · Sicurezza · mercoledì 04/11/2026 · formazione specifica, 6ª ora', 1, PASSI2, (), 'it', avz='2inf-sicurezza-0411')
open(D2 + 'index.html', 'w', encoding='utf-8').write(h)
shutil.copy(SLUGDIR + '1inf-deepfake-03-11/cruscotto.css', D2 + 'cruscotto.css'); shutil.copy(SLUGDIR + '1inf-deepfake-03-11/cruscotto-vista.js', D2 + 'cruscotto-vista.js')
open(D2 + 'cruscotto-ragazzi.html', 'w', encoding='utf-8').write(open(SLUGDIR + '1inf-deepfake-03-11/cruscotto-ragazzi.html', encoding='utf-8').read().replace('1INF', '2INF').replace('03/11', '04/11'))
open(D2 + 'cruscotto-ragazzi.json', 'w', encoding='utf-8').write(json.dumps({"titolo": "2INF 04/11", "generato": "", "ora": "-", "fonte": "dati non ancora letti", "righe": []}, ensure_ascii=False, indent=1))

# ======================= 3INF =======================
S3 = '3inf-mastermind-04-11'; D3 = SLUGDIR + S3 + '/'; os.makedirs(D3 + 'img', exist_ok=True)
def s3(n, t, items, hl=(), nota=''): svg(D3 + 'img/' + n, t, items, hl, nota)
s3('apri-progetto.svg', 'Lazarus: apri il progetto', [('menu', ['File  ▸', 'Apri progetto…'], 40, 70), ('box', 'Documenti ▸ mastermind-client\nfile: mastermind.lpi  → Apri', 380, 90, 360, 100)], (0, 1), 'File → Apri progetto… → mastermind.lpi')
s3('f9.svg', 'Premi F9', [('box', 'F9\n(oppure il triangolo verde)', 160, 100, 480, 100), ('box', 'Compare la finestra\nMastermind 2.0', 160, 240, 480, 100)], (0,), 'Se Lazarus chiede di salvare: Salva')
s3('ip-nome.svg', 'IP e nome', [('lbl', 'IP del server', 40, 100), ('edit', '192.168.38.70', 40, 120, 300), ('lbl', 'Il tuo nome', 400, 100), ('edit', 'Nome Cognome', 400, 120, 300), ('box', 'L\'IP è quello del riquadro\ngrande in alto nella pagina', 40, 220, 660, 90)], (1, 3), 'La porta 5050 c\'è già')
s3('connetti.svg', 'Connetti', [('btn', 'Connetti', 40, 100, 260), ('lbl', 'Collegato!', 340, 130), ('lbl', 'ATTESA: aspetta il Via del Prof', 40, 220)], (0, 1), 'Collegato! = tutto bene')
s3('gioca.svg', 'Gioca', [('lbl', 'GIOCO', 40, 90), ('edit', '1234', 40, 120, 240), ('btn', 'Prova', 300, 120, 160), ('box', 'Esatte = cifre giuste al posto giusto\nSpostate = giuste ma al posto sbagliato', 40, 210, 720, 100)], (0, 2), '4 cifre da 1 a 6')
s3('screenshot.svg', 'Screenshot', [('box', 'Win + Shift + S\nseleziona la finestra del gioco', 120, 100, 560, 100), ('box', 'Ctrl + S: salva in\nDocumenti ▸ mastermind-client', 120, 230, 560, 100)], (0,), 'Nome file: client_screenshot.png')
s3('consegna.svg', 'Consegna', [('btn', 'Manda al prof', 160, 130, 480), ('box', 'Scegli unit1.pas e lo screenshot', 160, 220, 480, 60)], (0,), 'Poi premi Manda al prof')
s3('github-upload.svg', 'GitHub: carica i file', [('box', 'github.com ▸ il tuo repository', 40, 70, 720, 60), ('btn', 'Add file ▸ Upload files', 40, 150, 360), ('box', 'Trascina i file di mastermind-client:\nmastermind.lpi · mastermind.lpr\nunit1.pas · unit1.lfm', 40, 230, 720, 130)], (1,), 'Trascina i file dentro la pagina')
s3('commit-msg.svg', 'GitHub: messaggio del commit', [('lbl', 'Commit changes', 40, 90), ('edit', 'Mastermind client collegato al server', 40, 120, 700), ('btn', 'Commit changes', 40, 190, 300), ('box', 'Il messaggio dice COSA hai fatto', 40, 270, 700, 60)], (1, 2), 'Scrivi il messaggio, poi Commit changes')
s3('link-commit.svg', 'Il link del commit', [('box', 'Nel repository clicca il commit\nin alto (la riga con il tuo messaggio)', 40, 70, 720, 90), ('edit', 'https://github.com/…/commit/…', 40, 190, 720), ('box', 'Copia questo indirizzo dalla barra del browser', 40, 260, 720, 60)], (1,), 'Indirizzo = link del commit')
s3('partita.svg', 'La partita di classe', [('box', 'Il Prof dice «Via»:\ngiocano tutti insieme', 80, 90, 640, 100), ('box', 'A destra: il migliore, il peggiore\ne il tuo posto', 80, 230, 640, 80)], (0,), 'Gioca finché indovini')
s3('quiz.svg', 'Quiz su Google Moduli', [('box', '8 domande sul Mastermind in rete', 80, 90, 640, 80), ('btn', 'Apri il quiz', 160, 220, 480)], (1,), 'Rispondi e premi Invia')

NOM = lambda: ''
PASSI31 = [
    P('Apri il tuo progetto', 'In Lazarus: menu <b>File</b> → <b>Apri progetto…</b> → <b>Documenti</b> → cartella <code>mastermind-client</code> → file <code>mastermind.lpi</code> → <b>Apri</b>. FATTO!', 'apri-progetto.svg', 'Apri progetto', bn='Lazarus: File → Apri progetto… → Documenti → mastermind-client → mastermind.lpi → Apri।'),
    P('Fai partire il programma', 'Premi <b>F9</b>. Dopo qualche secondo compare la finestra <b>Mastermind 2.0</b>. Se Lazarus chiede di salvare, clicca <b>Salva</b>.', 'f9.svg', 'F9', bn='F9 চাপো। Mastermind 2.0 জানালা খুলবে। Lazarus সেভ করতে বললে Salva চাপো।'),
    P('Scrivi IP e nome', 'Nella prima casella scrivi l\'<b>IP</b> del riquadro grande in alto in questa pagina (la porta c\'è già). Nella casella <b>Il tuo nome</b> scrivi nome e cognome.', 'ip-nome.svg', 'IP e nome', bn='প্রথম ঘরে পেজের উপরের বড় বাক্সের IP লেখো। দ্বিতীয় ঘরে নিজের নাম লেখো।'),
    P('Premi Connetti', 'Clicca <b>Connetti</b>. Se va bene, in alto compare <b>Collegato!</b> e sotto <b>ATTESA: aspetta il Via del Prof</b>.', 'connetti.svg', 'Connetti', bn='Connetti বাটন চাপো। «Collegato!» দেখা যাবে।'),
    P('Quando il Prof dice «Via», gioca', 'La scritta grande diventa <b>GIOCO</b>. Scrivi 4 cifre da 1 a 6 (per esempio <code>1234</code>) e clicca <b>Prova</b>. <b>Esatte</b> = giuste al posto giusto; <b>Spostate</b> = giuste ma al posto sbagliato. Riprova finché indovini.', 'gioca.svg', 'Gioco', bn='প্রফেসর «Via» বললে ১ থেকে ৬-এর ৪টি সংখ্যা লিখে Prova চাপো।'),
    P('Fai lo screenshot', 'Premi <b>Win + Shift + S</b>, seleziona la finestra del gioco, incolla in Paint e salva in <b>Documenti</b> → <code>mastermind-client</code> con il nome <code>client_screenshot.png</code>.', 'screenshot.svg', 'Screenshot', bn='Win + Shift + S চাপো, স্ক্রিনশট নাও।'),
    P('Consegna', 'Premi il bottone: scegli <code>unit1.pas</code> e lo screenshot e premi «Manda al prof». FATTO!', 'consegna.svg', 'Consegna', extra='<a class="bt v" href="consegna.html">Manda al prof</a>', bn='প্রফেসরকে ছবি আর unit1.pas পাঠাও।'),
]
MID1 = '<details class="card"><summary>Non hai la cartella mastermind-client (non c\'eri lunedì)?</summary><p>Costruisci il client con la pagina di lunedì, poi torna qui.</p><a class="bt b" href="../3inf-client-lazarus-02-11/">Apri la pagina di lunedì</a><p class="bn" lang="bn">সোমবারের পেজ খুলে ক্লায়েন্ট বানাও, তারপর এখানে ফিরে এসো।</p></details>'
conf(D3, "3INF 04/11/2026, Mastermind in rete, ore 12-14 (Allegato A PFP_3 Comp. 16 Reti locali e Comp. 12 Sviluppo collaborativo, III anno). Ora 1 = index.html, ora 2 = ora2.html. CHIUSE finche il docente non sblocca (regola 31). server_ip = SOLO indirizzo, senza porta.", {"server_ip": "192.168.38.70"})
h1 = pagina(S3, '3INF', 'Mastermind in rete · ora 1: il tuo client si collega', '3INF · progetto <code>mastermind-client</code> · mercoledì 04/11/2026', 1, PASSI31, ('bn',), 'it', extra_mid=MID1, ip=True, avz='3inf-mastermind-0411-ora1')
open(D3 + 'index.html', 'w', encoding='utf-8').write(h1)

MSG = 'Mastermind client collegato al server 192.168.38.70 porta 5050'
FORM = ('<div class="card"><h2>Manda il link del commit</h2><input type="text" id="urlcommit" placeholder="https://github.com/…/commit/…"><button class="bt v" id="mandacommit">Manda al prof</button><p class="msg" id="msgcommit"></p></div>'
        '<script>(function(){var C={};function $(i){return document.getElementById(i)}fetch("config.json?t="+Date.now()).then(function(r){return r.json()}).then(function(c){C=c||{}}).catch(function(){});'
        '$("mandacommit").onclick=function(){var u=$("urlcommit").value.trim(),n="";try{n=JSON.parse(localStorage.getItem("nome-0411")||"\\"\\"")}catch(x){}'
        'if(!/^https:\\/\\/github\\.com\\/.+\\/commit\\/[0-9a-f]{7,}/i.test(u)){$("msgcommit").textContent="Il link deve cominciare con https://github.com/ e contenere /commit/. Controlla di aver cliccato il commit.";return}'
        'if(!n||n.split(" ").length<2){$("msgcommit").textContent="Scrivi prima nome e cognome nella casella «Chi sei?» in alto.";return}'
        'var d={id:"3inf-commit-0411",modo:"verifica",classe:"3INF",nome:n,cosa:"commit",url:u,quando:new Date().toISOString()};'
        'if(!C.attivo||!C.invio){$("msgcommit").textContent="ANTEPRIMA: invio spento.";return}'
        'var f=document.createElement("form");f.method="POST";f.action=C.invio;f.target="_blank";f.acceptCharset="UTF-8";var i=document.createElement("input");i.type="hidden";i.name="d";i.value=JSON.stringify(d);f.appendChild(i);document.body.appendChild(f);f.submit();f.remove();'
        '$("msgcommit").textContent="Mandato! Si è aperta una scheda con scritto «Consegna arrivata al prof»."}})();</script>')
PASSI32 = [
    P('Collegati di nuovo', 'Tieni aperto il programma dell\'ora 1 e premi <b>Connetti</b>. Devi vedere <b>Collegato!</b>. FATTO!', 'connetti.svg', 'Connetti', bn='Connetti চাপো। «Collegato!» দেখা যাবে।'),
    P('Partita di classe', 'Quando il Prof dice <b>Via</b> giocano tutti insieme: stesso codice per tutta la classe. Guarda a destra il migliore, il peggiore e il <b>tuo posto</b>. Gioca finché indovini.', 'partita.svg', 'Partita', bn='প্রফেসর «Via» বললে সবাই একসাথে খেলে। ডানদিকে নিজের অবস্থান দেখো।'),
    P('Carica il progetto su GitHub', 'Apri <b>github.com</b> → il tuo repository → <b>Add file</b> → <b>Upload files</b>. Trascina dentro i file della cartella <code>mastermind-client</code>: <code>mastermind.lpi</code>, <code>mastermind.lpr</code>, <code>unit1.pas</code>, <code>unit1.lfm</code>.', 'github-upload.svg', 'Upload files', bn='github.com → নিজের repository → Add file → Upload files। mastermind-client ফোল্ডারের ফাইলগুলো টেনে আনো।'),
    P('Scrivi il messaggio del commit', 'Nella casella <b>Commit changes</b> scrivi un messaggio che dice <b>che cosa hai fatto</b>, poi premi <b>Commit changes</b> (bottone verde).', 'commit-msg.svg', 'Messaggio', code=MSG, bn='Commit changes ঘরে কী করেছ লেখো, তারপর সবুজ Commit changes বাটন চাপো।'),
    P('Manda il link del commit', 'Nel repository clicca il commit in alto (la riga con il tuo messaggio). Copia l\'indirizzo dalla barra del browser, scrivilo qui sotto e premi «Manda al prof».', 'link-commit.svg', 'Link commit', extra=FORM, bn='commit-এর লিংক কপি করে নিচে লিখে Manda al prof চাপো।'),
    P('Quiz sul Mastermind in rete', '8 domande su client, server, IP e porta. Premi il bottone verde, rispondi e premi <b>Invia</b>.', 'quiz.svg', 'Quiz Moduli', extra='<a class="bt v" href="__QUIZ3__" target="_blank" rel="noopener">Apri il quiz</a>', bn='৮টি প্রশ্নের Moduli কুইজ করো।'),
]
h2 = pagina(S3, '3INF', 'Mastermind in rete · ora 2: partita, GitHub e quiz', '3INF · progetto <code>mastermind-client</code> · mercoledì 04/11/2026 · ora 2', 2, PASSI32, ('bn',), 'it', ip=True, avz='3inf-mastermind-0411-ora2')
open(D3 + 'ora2.html', 'w', encoding='utf-8').write(h2)
c = open(SLUGDIR + '3inf-client-lazarus-02-11/consegna.html', encoding='utf-8').read()
c = c.replace('mm0211-pc14', 'pc14').replace('mm0211-nome', 'nome-0411').replace('3inf-client-0211', '3inf-client-0411').replace('mm0211', 'mm0411').replace('3INF 02/11/2026', '3INF 04/11/2026')
assert '3inf-client-0411' in c
open(D3 + 'consegna.html', 'w', encoding='utf-8').write(c)
for f in os.listdir(SLUGDIR + '3inf-client-lazarus-02-11/img'): pass
shutil.copy(SLUGDIR + '1inf-deepfake-03-11/cruscotto.css', D3 + 'cruscotto.css'); shutil.copy(SLUGDIR + '1inf-deepfake-03-11/cruscotto-vista.js', D3 + 'cruscotto-vista.js')
open(D3 + 'cruscotto-ragazzi.html', 'w', encoding='utf-8').write(open(SLUGDIR + '1inf-deepfake-03-11/cruscotto-ragazzi.html', encoding='utf-8').read().replace('1INF', '3INF').replace('03/11', '04/11'))
open(D3 + 'cruscotto-ragazzi.json', 'w', encoding='utf-8').write(json.dumps({"titolo": "3INF 04/11", "generato": "", "ora": "-", "fonte": "dati non ancora letti", "righe": []}, ensure_ascii=False, indent=1))
print('2inf e 3inf ok')
