#!/usr/bin/env python3
"""Genera la «Mini guida: smontare, rimontare e installare Windows 10» (MD + PDF versionati).

Uso:  python3 strumenti/genera_dispensa_pc.py --versione 1.0 [--nota "che cosa cambia"] [--rifai]

Scrive (V = versione):
  1. classe-2/dispense/MINI-GUIDA-PC-vV.md + .pdf        ragazzi, solo italiano, capitoli 00-08 (2INF, vale anche per la 3INF)
  2. classe-3/dispense/MINI-GUIDA-PC-BN-vV.md + .pdf     3INF: + una riga in bangla sotto ogni passo (allievo del PC 14),
                                                         come fa genera_lezione_pc.py (una riga per passo, non per frase)
  3. riservato report/2026-11-05/DISPENSA-DOCENTE-PC-vV.md + .pdf   = ragazzi + capitolo 09 «Creazione guasti»
  4. riservato report/2026-11-05/FOTO-DA-INSERIRE.md     elenco dei segnaposto (ID, passo, che cosa deve mostrare la foto)
Immagini: classe-2/dispense/img-mini-guida-pc/FOTO-CC-NN.png (schemi dichiarati, dagli SVG di genera_lezione_pc.py).
Le foto vere del docente si mettono con strumenti/inserisci_foto_dispensa.py (scrive FOTO-CC-NN.jpg e foto.json,
poi rilancia questo script con una versione nuova). Una versione già scritta non si riscrive (R11) senza --rifai.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import sys
import tempfile
from html import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_svg_pc as S  # noqa: E402
import genera_lezione_pc as G  # noqa: E402

PUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RIS = '/home/user/corso-informatica-riservato'
D2 = os.path.join(PUB, 'classe-2/dispense')
D3 = os.path.join(PUB, 'classe-3/dispense')
DR = os.path.join(RIS, 'report/2026-11-05')
IMG = os.path.join(D2, 'img-mini-guida-pc')
IMG_R = os.path.join(DR, 'img-dispensa-pc')
FOTO_JSON = os.path.join(IMG, 'foto.json')
STORICO = os.path.join(IMG, 'storico.json')
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
RETE = json.load(open(os.path.join(PUB, 'docs/anteprima/2inf-pc-05-11/config.json'), encoding='utf-8'))['rete']
N_BANCHI = 9

# ------------------------------------------------------------------ schemi in più (oltre a quelli della lezione)
f = S.finestra


def disegni_extra():
    ip = RETE['prefisso'] + str(RETE['primo'] + 3)
    return {
        'w-start.svg': f('Start', [
            ('v', 40, 70, 300, 'Esplora file', False), ('v', 40, 110, 300, 'Impostazioni (ingranaggio)', True),
            ('v', 40, 150, 300, 'Arresta il sistema', False), ('a', 470, 125, 350, 125), ('t', 480, 130, 'clic qui', 17, True)]),
        'w-imp-home.svg': f('Impostazioni di Windows', [
            ('v', 40, 80, 190, 'Sistema', False), ('v', 260, 80, 190, 'Dispositivi', False), ('v', 480, 80, 190, 'Rete e Internet', False),
            ('v', 40, 140, 190, 'App', False), ('v', 260, 140, 190, 'Account', True), ('v', 480, 140, 190, 'Ora e lingua', False),
            ('n', 40, 260, 'Account = utenti. App = app predefinite (capitolo 07).')]),
        'u-info.svg': f('Account Microsoft', [
            ('t', 50, 90, 'In che modo accederà questa persona?', 18, True), ('c', 50, 110, 500, 'Email o telefono', ''),
            ('v', 50, 190, 520, 'Non ho le informazioni di accesso di questa persona', True), ('a', 640, 205, 580, 205)]),
        'u-senza-ms.svg': f('Crea account', [
            ('t', 50, 90, 'Crea un account', 18, True), ('c', 50, 110, 500, 'Email', ''),
            ('v', 50, 180, 520, 'Ottieni un nuovo indirizzo email', False),
            ('v', 50, 230, 520, 'Aggiungi un utente senza account Microsoft', True), ('a', 640, 245, 580, 245)]),
        'u-admin.svg': f('Crea un utente per questo PC', [
            ('c', 50, 90, 400, 'Chi userà questo PC?', 'admin'), ('c', 50, 160, 400, 'Password', '••••••'),
            ('c', 50, 230, 400, 'Immetti di nuovo la password', '••••••'), ('b', 540, 320, 130, 'Avanti', True)]),
        'u-user1.svg': f('Crea un utente per questo PC', [
            ('c', 50, 90, 400, 'Chi userà questo PC?', 'user1'), ('c', 50, 160, 400, 'Password', '••••••'),
            ('c', 50, 230, 400, 'Immetti di nuovo la password', '••••••'), ('b', 540, 320, 130, 'Avanti', True)]),
        'u-elenco.svg': f('Impostazioni · Account · Famiglia e altri utenti', [
            ('t', 50, 90, 'Altri utenti', 18, True), ('v', 50, 105, 400, 'admin   ·   Account locale', True),
            ('b', 70, 150, 260, 'Cambia tipo di account', True), ('b', 350, 150, 120, 'Rimuovi', False),
            ('v', 50, 210, 400, 'user1   ·   Account locale', False), ('n', 50, 300, 'Clic su admin, poi «Cambia tipo di account».')]),
        'u-tipo-admin.svg': f('Cambia tipo di account', [
            ('t', 50, 90, 'admin', 19, True), ('t', 50, 130, 'Tipo di account'),
            ('v', 50, 145, 300, 'Utente standard', False), ('v', 50, 180, 300, 'Amministratore', True),
            ('a', 470, 195, 360, 195), ('b', 400, 320, 130, 'OK', True)]),
        'u-controllo.svg': f('Impostazioni · Account · Famiglia e altri utenti', [
            ('t', 50, 90, 'Altri utenti', 18, True),
            ('v', 50, 105, 520, 'admin   ·   Amministratore   ·   Account locale', True),
            ('v', 50, 150, 520, 'user1   ·   Account locale   (= Utente standard)', True),
            ('t', 50, 260, 'admin = Amministratore: può cambiare tutto.', 17, True),
            ('t', 50, 295, 'user1 = Utente standard: usa il PC, non cambia le cose importanti.', 17, True)]),
        'w-esegui.svg': f('Esegui', [
            ('t', 50, 100, 'Windows + R apre questa finestra.', 17, True), ('c', 50, 140, 420, 'Apri:', 'ncpa.cpl'),
            ('b', 400, 320, 120, 'OK', True), ('b', 540, 320, 130, 'Annulla', False)]),
        'w-cmd.svg': f('Cerca', [
            ('c', 50, 90, 420, 'Scrivi qui per eseguire la ricerca', 'cmd'),
            ('v', 50, 170, 420, 'Prompt dei comandi  (App)', True), ('a', 600, 185, 480, 185), ('t', 520, 230, 'Invio', 17, True)]),
        'ip-ipconfig.svg': f('Prompt dei comandi', [('r', 22, 52, 676, 326, '#0c0c0c')], barra='#333').replace('</svg>', '')
        + S.t(40, 90, 'C:\\Users\\tecnico> ipconfig', 17, '#f0f0f0')
        + S.t(40, 130, 'Indirizzo IPv4. . . . . : ' + ip, 17, '#7ee787')
        + S.t(40, 160, 'Subnet mask . . . . . . : ' + RETE['maschera'], 17, '#7ee787')
        + S.t(40, 190, 'Gateway predefinito . . : ' + RETE['gateway'], 17, '#7ee787')
        + S.t(40, 250, 'ipconfig fa vedere l\'IP che il PC sta usando.', 18, '#ffd33d', True) + '</svg>\n',
    }


# ------------------------------------------------------------------ il contenuto
# Ogni passo: (titolo, testo, schema, riga bangla, che cosa deve mostrare la foto). Un'azione per passo.
CAPITOLI = []


def cap(num, titolo, intro, passi, box=()):
    CAPITOLI.append({'n': num, 'titolo': titolo, 'intro': intro, 'passi': passi, 'box': list(box)})


cap(1, 'Sicurezza', 'Prima di tutto la sicurezza: così non si fa male nessuno e non si rompe niente.', [
    ('Spegni il PC', 'Clicca Start, poi Arresta il sistema. Aspetta che lo schermo e le ventole si fermino.', 'spina.svg',
     'Start > Arresta চাপো। স্ক্রিন আর ফ্যান থামা পর্যন্ত অপেক্ষা করো।', 'il tasto Start e la voce «Arresta il sistema» sullo schermo del laboratorio'),
    ('Togli la spina', 'Togli la spina dalla presa della corrente. Solo dopo si apre il case.', 'spina.svg',
     'প্লাগ খুলে ফেলো। তারপরই কেস খোলো।', 'una mano che sfila la spina del PC dalla ciabatta'),
    ('Scarica l\'elettricità statica', 'Tocca con la mano il metallo del case. Se c\'è il braccialetto antistatico, mettilo e attacca la pinza al metallo.', 'esd.svg',
     'কেসের ধাতু হাত দিয়ে ছোঁও, অথবা অ্যান্টিস্ট্যাটিক ব্রেসলেট পরো।', 'la mano sul metallo del case (o il braccialetto con la pinza attaccata)'),
    ('Prepara la scatola delle viti', 'Metti una scatola vicino al PC. Ogni vite che togli va subito nella scatola.', 'viti.svg',
     'স্ক্রুর বাক্স কাছে রাখো। প্রতিটি স্ক্রু সঙ্গে সঙ্গে বাক্সে রাখো।', 'la scatola delle viti accanto al PC, con il cacciavite a stella'),
], box=[('GIALLO', 'CPU e dissipatore oggi non si smontano. Non si tocca mai l\'interno dell\'alimentatore.'),
        ('GIALLO', 'Si lavora a coppie. MANI smonta e monta. OCCHI legge il passo e controlla. A ogni capitolo vi scambiate.')])

cap(2, 'Smontare il PC', 'Si smonta in quest\'ordine: cavi di alimentazione, cavi SATA (i cavi del disco), scheda video, RAM, disco.', [
    ('Svita le viti del pannello', 'Gira il PC. Dietro, svita con il cacciavite a stella le 2 viti del pannello laterale.', 'apri-case.svg',
     'PC ঘোরাও। পেছনের ২টি স্ক্রু খোলো।', 'il retro del case con le 2 viti del pannello laterale indicate'),
    ('Togli il pannello', 'Fai scorrere il pannello verso il retro e appoggialo sul tavolo.', 'apri-case.svg',
     'প্যানেল পেছনের দিকে সরিয়ে খুলে টেবিলে রাখো।', 'il pannello che scorre verso il retro, case aperto'),
    ('Guarda l\'ordine', 'Leggi lo schema: si smonta da sinistra a destra. CPU e dissipatore restano al loro posto.', 'ordine-smontaggio.svg',
     'বাঁ থেকে ডানে খোলো। CPU আর কুলার আজ খুলবে না।', 'l\'interno del case dall\'alto, con i pezzi numerati nell\'ordine di smontaggio'),
    ('Riconosci i componenti', 'Trova nel tuo PC le 8 parti dello schema, da A a H. Tocca ogni parte con il dito.', 'componenti.svg',
     'ছবির A থেকে H পর্যন্ত ৮টি অংশ তোমার PC-তে খুঁজে আঙুল দিয়ে ছোঁও।', 'l\'interno del PC del laboratorio con le lettere A-H sui componenti'),
    ('Guarda dove sono i cavi', 'OCCHI guarda dove è attaccato ogni cavo, prima che MANI lo stacchi.', 'mappa-cavi.svg',
     'তার খোলার আগে OCCHI দেখে নেয় কোথায় লাগানো আছে।', 'la scheda madre con i punti dei cavi: 24 pin, CPU 4/8 pin, SATA'),
    ('Stacca il cavo 24 pin', 'Premi il gancio della spina grande della scheda madre e tira dritto. Tira dalla spina, mai dal filo.', 'mappa-cavi.svg',
     'বড় ২৪ পিন প্লাগের হুক চেপে সোজা টানো। তার ধরে নয়।', 'il pollice che preme il gancio del connettore 24 pin'),
    ('Stacca il cavo CPU 4/8 pin', 'Premi il gancio della spina vicino alla CPU, in alto, e tira dritto.', 'mappa-cavi.svg',
     'CPU-র কাছের ৪/৮ পিন প্লাগের হুক চেপে সোজা টানো।', 'il connettore CPU 4/8 pin in alto a sinistra della scheda madre'),
    ('Stacca i cavi SATA', 'Stacca dal disco il cavo SATA dati (sottile) e il cavo SATA di alimentazione (largo).', 'mappa-cavi.svg',
     'ডিস্ক থেকে সরু SATA ডেটা তার আর চওড়া SATA পাওয়ার তার খোলো।', 'il retro del disco con i due cavi SATA: sottile (dati) e largo (corrente)'),
    ('Togli la scheda video, se c\'è', 'Togli la vite della scheda video. Premi il gancio dello slot e tirala dritta verso l\'alto.', 'ordine-smontaggio.svg',
     'গ্রাফিক্স কার্ড থাকলে স্ক্রু খোলো, স্লটের হুক চেপে সোজা উপরে টানো।', 'la scheda video con la sua vite e il gancio dello slot PCIe'),
    ('Apri i ganci della RAM', 'Spingi in fuori i due ganci ai lati del banco di RAM. Il banco si alza da solo.', 'ram.svg',
     'RAM-এর দুই পাশের হুক বাইরে ঠেলো। RAM নিজেই উঠে আসবে।', 'i due ganci aperti ai lati del banco di RAM'),
    ('Togli la RAM', 'Prendi il banco dai bordi e sfilalo. Non toccare i contatti dorati.', 'ram.svg',
     'RAM কিনারা ধরে বের করো। সোনালি অংশ ছোঁবে না।', 'due dita che tengono la RAM dai bordi corti'),
    ('Togli il disco', 'Svita le viti del disco (o apri la slitta) e sfilalo. Leggi l\'etichetta: SSD o HDD? Quanti GB?', 'componenti.svg',
     'ডিস্কের স্ক্রু খুলে বের করো। লেবেল পড়ো: SSD না HDD? কত GB?', 'il disco tolto, con l\'etichetta leggibile'),
    ('Metti i pezzi in fila', 'Metti i pezzi sul tavolo, da sinistra a destra, nell\'ordine in cui li hai tolti.', 'ordine-smontaggio.svg',
     'যে ক্রমে খুলেছ সেই ক্রমে টুকরোগুলো বাঁ থেকে ডানে সাজাও।', 'i pezzi in fila sul tavolo: cavi, scheda video, RAM, disco'),
])

cap(3, 'Rimontare il PC', 'Si rimonta al contrario: disco, RAM, scheda video, cavi SATA, cavi di alimentazione. Adesso chi era OCCHI diventa MANI.', [
    ('Guarda l\'ordine inverso', 'Leggi lo schema: si rimonta nell\'ordine contrario a quello dello smontaggio.', 'ordine-montaggio.svg',
     'খোলার উল্টো ক্রমে জোড়া দাও।', 'i pezzi in fila sul tavolo, con le frecce nell\'ordine del rimontaggio'),
    ('Rimetti il disco', 'Infila il disco nel suo posto e rimetti le sue viti (o chiudi la slitta).', 'componenti.svg',
     'ডিস্ক জায়গায় বসিয়ে স্ক্রু লাগাও।', 'il disco al suo posto con le viti avvitate'),
    ('Rimetti la RAM', 'Fai combaciare la tacca della RAM con il dentino dello slot. Spingi dritto con due pollici fino al «clic».', 'ram.svg',
     'RAM-এর খাঁজ আর স্লটের দাঁত মেলাও। দুই বুড়ো আঙুলে সোজা চাপো, «ক্লিক» পর্যন্ত।', 'i due pollici sulla RAM e i ganci che si chiudono'),
    ('Rimetti la scheda video, se c\'era', 'Spingi la scheda video dritta nello slot fino al clic. Rimetti la sua vite.', 'ordine-montaggio.svg',
     'গ্রাফিক্স কার্ড সোজা স্লটে চাপো, তারপর স্ক্রু লাগাও।', 'la scheda video inserita nello slot e la vite rimessa'),
    ('Attacca i cavi SATA', 'Attacca al disco il cavo SATA dati e il cavo SATA di alimentazione. Ogni spina entra in un solo verso: non forzare.', 'mappa-cavi.svg',
     'ডিস্কে SATA ডেটা আর পাওয়ার তার লাগাও। জোর করবে না।', 'i due connettori SATA attaccati al disco, con la forma a L visibile'),
    ('Attacca il cavo 24 pin', 'Spingi la spina grande nella scheda madre fino al clic del gancio.', 'mappa-cavi.svg',
     'বড় ২৪ পিন প্লাগ «ক্লিক» পর্যন্ত চাপো।', 'il connettore 24 pin inserito, gancio agganciato'),
    ('Attacca il cavo CPU 4/8 pin', 'Spingi la spina 4/8 pin vicino alla CPU fino al clic.', 'mappa-cavi.svg',
     'CPU-র কাছে ৪/৮ পিন প্লাগ «ক্লিক» পর্যন্ত চাপো।', 'il connettore CPU 4/8 pin inserito'),
    ('Fai i 5 controlli', 'OCCHI legge, MANI controlla: RAM con i ganci chiusi, 24 pin, CPU 4/8 pin, cavi SATA, nessuna vite libera.', 'checklist.svg',
     'চালু করার আগে ৫টি জিনিস দেখো। কোনোটা না হলে আগে ঠিক করো।', 'il case aperto e completo, pronto per i 5 controlli'),
    ('Chiudi il case', 'Rimetti il pannello laterale e le sue 2 viti.', 'apri-case.svg',
     'প্যানেল লাগিয়ে ২টি স্ক্রু দাও।', 'il pannello rimesso e le 2 viti avvitate'),
    ('Collega i cavi esterni', 'Collega monitor, tastiera, mouse e cavo di rete. La spina della corrente va per ultima.', 'collega.svg',
     'মনিটর, কীবোর্ড, মাউস আর নেটওয়ার্ক লাগাও। বিদ্যুৎ সবার শেষে।', 'il retro del PC con monitor, tastiera, mouse, rete e corrente collegati'),
], box=[('ROSSO', 'Un controllo è NO? Non accendere: sistema prima.')])

cap(4, 'Accensione e BIOS', 'Il BIOS (Basic Input Output System: il programma che parte per primo, nei PC nuovi si chiama UEFI) dice al PC da dove partire. Oggi si parte dalla chiavetta USB.', [
    ('Metti la chiavetta', 'Metti la chiavetta di Windows 10 in una porta USB dietro il PC.', 'collega.svg',
     'Windows 10-এর USB পেছনের একটা USB পোর্টে লাগাও।', 'la chiavetta di Windows 10 infilata in una porta USB dietro il PC'),
    ('Entra nel BIOS', 'Premi il tasto di accensione. Subito, più volte, premi Canc (o F2). Lo schermo all\'avvio dice il tasto giusto.', 'tasti-bios.svg',
     'চালু করে সঙ্গে সঙ্গে বারবার Canc (বা F2) চাপো।', 'lo schermo all\'avvio con la scritta del tasto per entrare nel BIOS'),
    ('Leggi CPU, RAM e disco', 'Nella prima schermata leggi il nome della CPU, quanta RAM c\'è e il nome del disco.', 'bios-info.svg',
     'প্রথম পাতায় CPU-র নাম, RAM কত আর ডিস্কের নাম পড়ো।', 'la prima schermata del BIOS dei PC del laboratorio'),
    ('Vai nella scheda Boot', 'Con le frecce vai nella scheda Boot (Avvio).', 'bios-boot.svg',
     'তীর চিহ্ন দিয়ে Boot ট্যাবে যাও।', 'la scheda Boot del BIOS dei PC del laboratorio'),
    ('Metti USB per prima', 'Porta USB al primo posto nell\'ordine di avvio (Boot Option #1).', 'bios-boot.svg',
     'Boot Option #1-এ USB রাখো।', 'la riga Boot Option #1 con la chiavetta USB'),
    ('Salva ed esci', 'Premi F10 e conferma con Sì (Yes). Il PC riparte dalla chiavetta.', 'bios-boot.svg',
     'F10 চেপে Yes দাও। PC USB থেকে চালু হবে।', 'la finestra «Save and Exit» con Yes'),
    ('Piano B: il menu F12', 'Non trovi l\'ordine di avvio? Spegni, accendi e premi F12 (o Esc). Scegli la riga con USB e premi Invio.', 'menu-avvio.svg',
     'না পেলে: চালু করে F12 চাপো, USB বেছে Enter চাপো।', 'il menu di avvio F12 dei PC del laboratorio con la riga USB'),
])

cap(5, 'Installare Windows 10 da chiavetta', 'Il PC del banco si può cancellare tutto: è fatto per imparare. Si crea un account locale: nome e password stanno solo su questo PC.', [
    ('Parti dalla chiavetta', 'Se compare «Premi un tasto per avviare da CD o DVD», premi un tasto qualsiasi.', 'w-avvio.svg',
     '«Premi un tasto…» দেখালে যেকোনো কী চাপো।', 'lo schermo nero con il logo di Windows o la scritta «Premi un tasto»'),
    ('Lascia la lingua italiana', 'Lascia Italiano nelle tre caselle e premi Avanti.', 'w-lingua.svg',
     'তিনটি ঘরে Italiano রেখে Avanti চাপো।', 'la finestra della lingua con le tre caselle in Italiano'),
    ('Premi Installa', 'Premi il bottone grande Installa.', 'w-lingua.svg',
     'বড় Installa বাটন চাপো।', 'il bottone «Installa» al centro dello schermo'),
    ('Non ho un codice Product Key', 'In basso clicca la scritta Non ho un codice Product Key.', 'w-key.svg',
     'নিচে «Non ho un codice Product Key» চাপো।', 'la finestra «Attiva Windows» con la scritta in basso'),
    ('Scegli l\'edizione', 'Scegli Windows 10 Pro (o quella che dice il Professore) e premi Avanti.', 'w-key.svg',
     'Windows 10 Pro বেছে Avanti চাপো।', 'l\'elenco delle edizioni con Windows 10 Pro selezionato'),
    ('Accetta la licenza', 'Spunta Accetto le condizioni di licenza e premi Avanti.', 'w-tipo.svg',
     'লাইসেন্সে টিক দিয়ে Avanti চাপো।', 'la casella «Accetto le condizioni di licenza» spuntata'),
    ('Scegli Personalizzata', 'Clicca Personalizzata: installa solo Windows.', 'w-tipo.svg',
     '«Personalizzata» বেছে নাও।', 'le due scelte, con «Personalizzata» evidenziata'),
    ('Elimina le partizioni', 'Seleziona una partizione e premi Elimina. Rifallo finché resta solo «Spazio non allocato».', 'w-disco.svg',
     'প্রতিটি পার্টিশন বেছে Elimina চাপো, শুধু «Spazio non allocato» থাকবে।', 'la finestra dei dischi con il bottone «Elimina»'),
    ('Scegli lo spazio non allocato', 'Seleziona Unità 0 Spazio non allocato e premi Avanti.', 'w-disco.svg',
     '«Unità 0 Spazio non allocato» বেছে Avanti চাপো।', 'la riga «Spazio non allocato» selezionata'),
    ('Aspetta la copia', 'Windows copia i file e riavvia da solo (15-25 minuti). Non toccare niente.', 'w-copia.svg',
     'Windows নিজে ফাইল কপি করে রিস্টার্ট হয় (১৫-২৫ মিনিট)। কিছু ছোঁবে না।', 'la finestra «Installazione di Windows» con la percentuale'),
    ('Scegli Italia', 'Al primo avvio scegli Italia e premi Sì.', 'w-regione.svg',
     'Italia বেছে Sì চাপো।', 'l\'elenco dei paesi con Italia selezionata'),
    ('Scegli la tastiera', 'Scegli la tastiera Italiano e premi Sì. Alla seconda tastiera premi Ignora.', 'w-regione.svg',
     'কীবোর্ড Italiano, Sì। দ্বিতীয় কীবোর্ডে Ignora।', 'la schermata della tastiera con «Italiano»'),
    ('Non ho Internet', 'In basso a sinistra clicca Non ho Internet.', 'w-rete.svg',
     'নিচে বাঁয়ে «Non ho Internet» চাপো।', 'la schermata «Connettiamoti a una rete» con la scritta in basso a sinistra'),
    ('Configurazione limitata', 'Clicca Continua con configurazione limitata.', 'w-rete.svg',
     '«Continua con configurazione limitata» চাপো।', 'il bottone «Continua con configurazione limitata»'),
    ('Scrivi il nome del primo utente', 'Scrivi tecnico e premi Avanti. Questo primo utente è amministratore.', 'w-account.svg',
     'নাম tecnico লিখে Avanti চাপো। এটা অ্যাডমিন।', 'la schermata «Chi userà questo PC?» con il nome scritto'),
    ('Scrivi la password', 'Scrivi la password che dice il Professore, due volte. Poi scegli 3 domande di sicurezza.', 'w-account.svg',
     'প্রফেসরের বলা পাসওয়ার্ড দুবার লেখো। তারপর ৩টি নিরাপত্তা প্রশ্ন।', 'la casella della password (senza la password scritta)'),
    ('Privacy: tutto No', 'Metti No a tutte le voci e premi Accetta. Poi aspetta il desktop.', 'w-privacy.svg',
     'সব No করে Accetta চাপো। ডেস্কটপের জন্য অপেক্ষা করো।', 'la schermata della privacy con le voci su No'),
], box=[('GIALLO', 'Windows 10 Pro a volte chiede «Configura per uso personale», poi «Account offline» e «Esperienza limitata»: sono la stessa strada senza Internet.'),
        ('ROSSO', 'Si installano solo i PC del banco, mai le postazioni della classe.')])

cap(6, 'Creare gli utenti admin e user1', 'Due utenti nuovi: admin (amministratore: può cambiare tutto) e user1 (utente standard: usa il PC ma non cambia le cose importanti). Si lavora di solito con l\'utente standard: è più sicuro.', [
    ('Apri Impostazioni', 'Clicca Start, poi l\'ingranaggio Impostazioni.', 'w-start.svg',
     'Start, তারপর গিয়ার Impostazioni চাপো।', 'il menu Start aperto con l\'ingranaggio Impostazioni'),
    ('Apri Account', 'Clicca Account.', 'w-imp-home.svg',
     'Account চাপো।', 'la pagina iniziale di Impostazioni con il riquadro Account'),
    ('Apri Famiglia e altri utenti', 'A sinistra clicca Famiglia e altri utenti.', 'w-utenti.svg',
     'বাঁয়ে «Famiglia e altri utenti» চাপো।', 'la colonna a sinistra con «Famiglia e altri utenti» (nella Pro: «Altri utenti»)'),
    ('Aggiungi un altro utente', 'Clicca Aggiungi un altro utente a questo PC.', 'w-utenti.svg',
     '«Aggiungi un altro utente a questo PC» চাপো।', 'il bottone con il più: «Aggiungi un altro utente a questo PC»'),
    ('Non ho le informazioni di accesso', 'Clicca Non ho le informazioni di accesso di questa persona.', 'u-info.svg',
     '«Non ho le informazioni di accesso di questa persona» চাপো।', 'la finestra blu dell\'account Microsoft con la scritta in basso'),
    ('Utente senza account Microsoft', 'Clicca Aggiungi un utente senza account Microsoft.', 'u-senza-ms.svg',
     '«Aggiungi un utente senza account Microsoft» চাপো।', 'la finestra «Crea account» con la scritta in basso'),
    ('Crea admin', 'Scrivi admin come nome. Scrivi la password del Professore due volte, poi le 3 domande. Premi Avanti.', 'u-admin.svg',
     'নাম admin, পাসওয়ার্ড দুবার, ৩টি প্রশ্ন, তারপর Avanti।', 'la finestra «Crea un utente per questo PC» con il nome admin (senza la password)'),
    ('Crea user1', 'Rifai i passi 4, 5 e 6. Scrivi user1 come nome, la password e le domande. Premi Avanti.', 'u-user1.svg',
     'ধাপ ৪, ৫, ৬ আবার করো। নাম user1, পাসওয়ার্ড, প্রশ্ন, Avanti।', 'la stessa finestra con il nome user1'),
    ('Cambia il tipo di admin', 'Clicca admin, poi Cambia tipo di account.', 'u-elenco.svg',
     'admin-এ ক্লিক করো, তারপর «Cambia tipo di account»।', 'l\'elenco «Altri utenti» con admin aperto e il bottone «Cambia tipo di account»'),
    ('Scegli Amministratore', 'Nella casella Tipo di account scegli Amministratore e premi OK.', 'u-tipo-admin.svg',
     'Tipo di account-এ Amministratore বেছে OK চাপো।', 'la finestra «Cambia tipo di account» con Amministratore'),
    ('Controlla i due utenti', 'Guarda l\'elenco: sotto admin c\'è scritto Amministratore. user1 resta Utente standard.', 'u-controllo.svg',
     'admin = Amministratore, user1 = Utente standard। মিলিয়ে দেখো।', 'l\'elenco «Altri utenti» con admin Amministratore e user1'),
], box=[('GIALLO', 'Nell\'edizione Pro la voce a sinistra si può chiamare «Altri utenti»: è lo stesso posto.')])

cap(7, 'Impostazioni di base', 'Un tecnico sceglie il browser e vede sempre il tipo di ogni file: .txt è testo, .jpg è una foto, .exe è un programma. Un file «foto.jpg.exe» è un programma travestito: attenzione!', [
    ('Chrome c\'è?', 'Clicca Start e scrivi Chrome. Se non compare, il Professore lo installa quando c\'è Internet.', 'w-chrome.svg',
     'Start-এ Chrome লেখো। না থাকলে ইন্টারনেট এলে প্রফেসর ইনস্টল করবেন।', 'il menu Start con «Chrome» scritto nella ricerca'),
    ('Apri le app predefinite', 'Start, Impostazioni, App, poi a sinistra App predefinite.', 'w-predefinite.svg',
     'Impostazioni > App > App predefinite।', 'la pagina «App predefinite» di Impostazioni'),
    ('Scegli Chrome', 'Sotto Web browser clicca il browser che c\'è e scegli Google Chrome. Se chiede conferma: Cambia comunque.', 'w-predefinite.svg',
     'Web browser-এ ক্লিক করে Google Chrome বেছে নাও।', 'la voce «Web browser» con Google Chrome scelto'),
    ('Apri Esplora file', 'Premi insieme i tasti Windows ed E. In alto clicca la scheda Visualizza.', 'w-estensioni.svg',
     'Windows + E চাপো। উপরে Visualizza ট্যাব চাপো।', 'Esplora file aperto con la scheda Visualizza'),
    ('Mostra le estensioni', 'Spunta la casella Estensioni nomi file.', 'w-estensioni.svg',
     '«Estensioni nomi file»-এ টিক দাও।', 'la casella «Estensioni nomi file» spuntata'),
    ('Prova con un file', 'In Documenti fai tasto destro, Nuovo, Documento di testo. Il nome finisce con .txt? Fatto!', 'w-prova.svg',
     'Documenti-এ নতুন টেক্সট ফাইল বানাও। শেষে .txt দেখা যায়? হয়ে গেছে!', 'il file «Nuovo documento di testo.txt» con l\'estensione visibile'),
])

cap(8, 'IP fisso e prova con il PC accanto', 'Ogni PC in rete ha un indirizzo IP (Internet Protocol: il «numero civico» del PC). Nella stessa rete le prime 3 parti sono uguali, l\'ultima è diversa. Il vostro IP dipende dal numero del banco: guardate la tabella.', [
    ('Trova il tuo IP', 'Cerca il numero del tuo banco nella tabella qui sopra. Leggi il tuo IP e quello del PC accanto.', 'rete-schema.svg',
     'ওপরের টেবিলে তোমার বেঞ্চ নম্বর খোঁজো। তোমার আর পাশের PC-র IP পড়ো।', 'il numero del banco scritto sul case'),
    ('Apri le connessioni di rete', 'Premi insieme Windows e R. Scrivi ncpa.cpl e premi Invio.', 'w-esegui.svg',
     'Windows + R চাপো, ncpa.cpl লিখে Enter।', 'la finestra Esegui con ncpa.cpl scritto'),
    ('Apri Ethernet', 'Tasto destro su Ethernet, poi Proprietà.', 'w-ncpa.svg',
     'Ethernet-এ ডান ক্লিক, তারপর Proprietà।', 'la finestra «Connessioni di rete» con il menu di Ethernet aperto'),
    ('Apri IPv4', 'Doppio clic su Protocollo Internet versione 4 (TCP/IPv4).', 'w-ipv4.svg',
     '«Protocollo Internet versione 4 (TCP/IPv4)»-এ ডাবল ক্লিক।', 'l\'elenco delle Proprietà di Ethernet con la riga IPv4'),
    ('Scrivi i 4 valori', 'Scegli Utilizza il seguente indirizzo IP. Scrivi indirizzo IP, subnet mask, gateway e DNS della tabella. Premi OK, poi OK.', 'w-ipv4.svg',
     '«Utilizza il seguente indirizzo IP» বেছে টেবিলের ৪টি মান লেখো। OK, OK।', 'la finestra IPv4 compilata con i valori del banco'),
    ('Lascia passare il ping', 'Start, scrivi Windows Defender Firewall con sicurezza avanzata. Regole connessioni in entrata: tasto destro su ogni riga «Richiesta echo - ICMPv4 in entrata», Abilita regola.', 'w-firewall.svg',
     'Firewall > Regole in entrata > «Richiesta echo - ICMPv4» > Abilita regola।', 'le righe «Richiesta echo - ICMPv4 in entrata» con «Abilita regola»'),
    ('Collega il cavo allo switch', 'Quando il Professore lo dice, collega il cavo di rete del PC allo switch.', 'collega.svg',
     'প্রফেসর বললে নেটওয়ার্ক তার সুইচে লাগাও।', 'il cavo di rete dal PC allo switch del laboratorio'),
    ('Controlla il tuo IP', 'Start, scrivi cmd, Invio. Scrivi ipconfig e premi Invio. Leggi Indirizzo IPv4: è il tuo?', 'ip-ipconfig.svg',
     'cmd খোলো, ipconfig লিখে Enter। Indirizzo IPv4 তোমারটা কি না দেখো।', 'il Prompt dei comandi con il risultato di ipconfig'),
    ('Mostralo: ping al PC accanto', 'Scrivi ping, uno spazio e l\'IP del PC accanto. Premi Invio. «Risposta da…» vuol dire che la rete funziona!', 'ping.svg',
     'ping আর পাশের PC-র IP লিখে Enter। «Risposta da…» = কাজ করছে!', 'il Prompt dei comandi con le righe «Risposta da…»'),
], box=[('GIALLO', '«Richiesta scaduta»? Controlla l\'IP, il cavo e il firewall, poi riprova.')])

for c in CAPITOLI:
    c['passi'] = [{'id': f'FOTO-{c["n"]:02d}-{i:02d}', 'n': i, 'titolo': p[0], 'testo': p[1], 'svg': p[2], 'bn': p[3], 'foto': p[4]}
                  for i, p in enumerate(c['passi'], 1)]
TUTTI_PASSI = [p for c in CAPITOLI for p in c['passi']]


def tabella_ip():
    righe = ['| Banco | Indirizzo IP | Subnet mask | Gateway | DNS |', '|---|---|---|---|---|']
    for b in range(1, N_BANCHI + 1):
        righe.append(f'| {b} | `{RETE["prefisso"]}{RETE["primo"] + b}` | `{RETE["maschera"]}` | `{RETE["gateway"]}` | `{RETE["dns"]}` |')
    return '\n'.join(righe)


# ------------------------------------------------------------------ capitolo 09 (solo docente)
GUASTI_MD = r'''## 09 Creazione guasti (solo docente)

Questo capitolo c'è solo nella versione per il docente. I ragazzi trovano il guasto con la scheda «Caccia al guasto» sulla pagina `anteprima/2inf-pc-05-11/guasti.html`, chiusa finché non la sblocchi (09.8).

> [BLU] Non provato sui PC del laboratorio: i messaggi esatti cambiano con il modello del BIOS. Prova ogni guasto su un PC prima della lezione e correggi qui il sintomo.

### 09.1 Regole per tutti i guasti

1. Ogni guasto si crea a PC SPENTO e con la spina STACCATA, dopo aver toccato il metallo del case.
2. Un guasto alla volta per PC. Annota banco e guasto nel cartellino (09.9) prima di girarti.
3. I ragazzi guardano altrove mentre crei il guasto. Il guasto si cerca con le 4 mosse: sintomo, ipotesi, prova, soluzione.
4. Le domande-guida si fanno una alla volta, senza dare la soluzione. Si passa alla domanda dopo solo se la coppia è ferma da qualche minuto.
5. Prima di aprire il case, la coppia spegne e stacca la spina: se non lo fa, si ferma il gioco.
6. Mai creare guasti che toccano CPU, dissipatore, alimentatore aperto, pulsanti del pannello frontale (pin piccoli e fragili) o impostazioni del BIOS diverse dall'ordine di avvio.

### 09.2 Guasto 1: RAM tolta o non agganciata

1. **Come crearlo:** togli tutti i banchi di RAM e mettili nella scatola delle viti del banco. Variante «non agganciata»: banco appoggiato dritto nello slot, ganci aperti, senza clic.
2. **Sintomo che vedranno:** le ventole girano ma lo schermo resta nero; su alcuni PC dei beep ripetuti o un LED «DRAM» acceso sulla scheda madre. Molti PC non hanno il cicalino: solo schermo nero.
3. **Domande-guida:**
   1. Le ventole girano? Allora la corrente arriva?
   2. Che cosa serve al PC per lavorare appena acceso?
   3. Nello schema A-H, quali pezzi potete controllare senza attrezzi?
4. **Soluzione:** rimettere la RAM con la tacca al posto giusto, spingere fino al clic dei ganci.
5. **Rischio e attenzioni:** basso. Scarica statica prima di toccare la RAM; RAM presa dai bordi; mai a PC acceso. La variante «non agganciata» solo con il banco dritto: un banco storto può fare un contatto sbagliato. Nel dubbio, toglila del tutto.

### 09.3 Guasto 2: cavo SATA dati del disco staccato

1. **Come crearlo:** stacca solo il cavo SATA dati (quello sottile) dal disco; lascia attaccato il cavo SATA di alimentazione.
2. **Sintomo che vedranno:** con Windows già installato, «Reboot and Select proper Boot device», «No bootable device» o il PC che entra da solo nel BIOS. Nel BIOS il disco non compare. Durante l'installazione: nessuna unità nella finestra dei dischi.
3. **Domande-guida:**
   1. Il BIOS vede il disco? In quale schermata lo avete letto all'ora 2?
   2. Quanti cavi ha un disco, e a che cosa serve ognuno?
   3. Che cosa cambia tra il disco «che gira» e il disco «che parla con la scheda madre»?
4. **Soluzione:** riattaccare il cavo SATA dati al disco (e controllare che sia attaccato anche alla scheda madre).
5. **Rischio e attenzioni:** basso. Il connettore a L è fragile: non piegarlo e non tirare il filo. Se il cavo ha il gancio metallico, va premuto.

### 09.4 Guasto 3: alimentazione 24 pin o CPU 4/8 pin staccata

1. **Come crearlo:** variante A, stacca il connettore 24 pin dalla scheda madre. Variante B, stacca solo il connettore CPU 4/8 pin in alto.
2. **Sintomo che vedranno:**
   1. variante A (24 pin): premendo il tasto non succede niente, nessuna ventola, nessuna luce;
   2. variante B (CPU 4/8 pin): le ventole partono ma non c'è immagine; su alcuni PC si spegne e riprova da solo.
3. **Domande-guida:**
   1. Si accende qualcosa? Una luce, una ventola?
   2. La spina è nella presa? L'interruttore dietro l'alimentatore è su I?
   3. Quali cavi portano la corrente dall'alimentatore alla scheda madre? Guardate la mappa dei cavi.
4. **Soluzione:** rimettere il connettore staccato fino al clic del gancio.
5. **Rischio e attenzioni:** medio. Solo a spina staccata. I connettori sono duri: si preme il gancio, non si tirano i fili. Il CPU 8 pin e l'8 pin PCIe della scheda video si assomigliano: non forzare mai una spina che non entra.

### 09.5 Guasto 4: ordine di avvio sbagliato nel BIOS

1. **Come crearlo:** nel BIOS, scheda Boot, metti il disco (o la rete, «PXE») prima della USB. Salva con F10. Non serve aprire il case.
2. **Sintomo che vedranno:** con la chiavetta inserita il PC non parte dalla USB: parte Windows già installato, oppure (disco vuoto) «No bootable device» o la scritta «Start PXE over IPv4».
3. **Domande-guida:**
   1. Chi decide da dove parte il PC?
   2. Dove lo avete cambiato all'ora 2?
   3. C'è un modo per scegliere la USB solo per questa volta, senza cambiare il BIOS?
4. **Soluzione:** BIOS, Boot, USB al primo posto, F10; oppure il menu F12.
5. **Rischio e attenzioni:** nessun rischio per i pezzi. Non cambiare altre voci: Secure Boot o la modalità del disco (AHCI, RAID) possono impedire a Windows di partire. Scrivi nel cartellino che cosa hai cambiato.

### 09.6 Guasto 5: rete, cavo staccato o IP sbagliato

1. **Come crearlo:** a PC acceso dopo il capitolo 08, una variante alla volta, solo sulla rete separata dello switch del laboratorio:
   1. variante A, cavo di rete staccato dallo switch;
   2. variante B, IP uguale a quello del PC accanto;
   3. variante C, terza parte dell'IP diversa (per esempio `192.168.11.x`) oppure subnet mask sbagliata.
2. **Sintomo che vedranno:**
   1. variante A: icona della rete con la X, ping con «Host di destinazione non raggiungibile» o «Errore generale»;
   2. variante B: avviso di Windows «conflitto di indirizzi IP»; `ipconfig` mostra «(Duplicato)» o un indirizzo `169.254.x.x`; il ping non risponde o risponde il PC sbagliato;
   3. variante C: il ping al PC accanto non risponde.
3. **Domande-guida:**
   1. Che cosa dice l'icona della rete in basso a destra?
   2. Che IP ha il vostro PC adesso? Usate `ipconfig`.
   3. Le prime 3 parti sono uguali a quelle del PC accanto? L'ultima è diversa?
4. **Soluzione:** riattaccare il cavo; rimettere l'IP della tabella del banco e la subnet mask `255.255.255.0`.
5. **Rischio e attenzioni:** nessun rischio per i pezzi. Mai sulla rete della scuola: un IP doppio disturba un altro PC. Un ping che non risponde può dipendere anche dal firewall (regola «Richiesta echo»): è un buon «falso guasto» da far scoprire.

### 09.7 Guasto 6: monitor sulla scheda video sbagliata

1. **Come crearlo:** solo nei PC con scheda video dedicata. Collega il cavo del monitor alla porta video della scheda madre (in alto, vicino alle USB) invece che a quella della scheda video (in basso, orizzontale).
2. **Sintomo che vedranno:** il PC è acceso (ventole, luci, Bloc Num che si accende) ma il monitor dice «Nessun segnale» e resta nero.
3. **Domande-guida:**
   1. Il PC è acceso? Come fate a saperlo senza schermo?
   2. Dietro il PC, quante porte video ci sono? In quali punti?
   3. Che cosa avete smontato all'ora 1 che ha anche lui delle porte video?
4. **Soluzione:** collegare il monitor alla porta della scheda video dedicata.
5. **Rischio e attenzioni:** nessuno. Per i cavi VGA e DVI si stacca a PC spento e si avvitano bene. Nei PC senza scheda video, variante: ingresso del monitor sbagliato (tasto Input o Source).

### 09.8 La scheda «Caccia al guasto» per i ragazzi

1. Si compila a coppie sulla pagina `anteprima/2inf-pc-05-11/guasti.html`, niente carta: per ogni guasto (fino a 3) sintomo, ipotesi, prova, soluzione, risolto sì o no. Si consegna con il bottone «Manda al prof».
2. La pagina è chiusa. Per aprirla, nel terminale del repository pubblico:

```
python3 strumenti/sblocca_ora.py 2inf-pc-05-11 guasti
```

3. Per richiuderla:

```
python3 strumenti/sblocca_ora.py 2inf-pc-05-11 guasti-chiudi
```

4. Dopo lo sblocco: `bash strumenti/aspetta_pubblicazione.sh`; la pagina aperta se ne accorge da sola entro 30 secondi.

| Colonna della scheda | Che cosa scrivono i ragazzi | Esempio |
|---|---|---|
| Sintomo | che cosa vedono, scelto da un elenco | Ventole girano ma schermo nero |
| Ipotesi | che cosa può essere | La RAM non è dentro |
| Prova | che cosa controllano, una cosa per volta | Spina staccata, case aperto: la RAM manca |
| Soluzione | che cosa hanno fatto | RAM rimessa fino al clic, ora parte |
| Risolto | sì o no | sì |

### 09.9 Cartellino del docente (da tenere in tasca)

| Banco | Guasto creato (1-6, variante) | Ora | Risolto | Note |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |

> [ROSSO] A fine giro ogni PC torna a posto: RAM, cavi 24 pin, CPU e SATA attaccati, ordine di avvio rimesso, IP della tabella. Controlla il cartellino riga per riga.
'''


# ------------------------------------------------------------------ MD
def foto_vere():
    try:
        return json.load(open(FOTO_JSON, encoding='utf-8'))
    except Exception:
        return {}


def storico(versione, nota):
    try:
        st = json.load(open(STORICO, encoding='utf-8'))
    except Exception:
        st = []
    if not any(x['v'] == versione for x in st):
        st.append({'v': versione, 'data': datetime.date.today().strftime('%d/%m/%Y'), 'nota': nota})
        os.makedirs(IMG, exist_ok=True)
        json.dump(st, open(STORICO, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return [x for x in st if tuple(map(int, x['v'].split('.'))) <= tuple(map(int, versione.split('.')))]


def scrivi_md(tipo, versione, rel_img, st):
    """tipo: 'ragazzi', 'bn', 'docente'."""
    fv = foto_vere()
    titolo = 'Mini guida: smontare, rimontare e installare Windows 10'
    chi = {'ragazzi': '2INF e 3INF', 'bn': '3INF (con la riga in bangla, PC 14)', 'docente': 'versione DOCENTE (2INF e 3INF)'}[tipo]
    L = [f'# {titolo}', '',
         f'**Versione {versione}** — 05/11/2026 · {chi} · solo italiano' + (' + bangla' if tipo == 'bn' else ''), '']
    if tipo == 'docente':
        L += ['> [ROSSO] RISERVATO: non pubblicare. È la dispensa dei ragazzi, identica, più il capitolo 09 «Creazione guasti».', '']
    L += ['| Macro-argomento | Argomento | Materia | Data | Orario | Contenuto |', '|---|---|---|---|---|---|',
          '| Hardware e sistemi operativi | Smontare, rimontare e installare un PC | Laboratorio | giovedì 05/11/2026 | 2INF 8-11, 3INF 11-13 | sicurezza, smontaggio, rimontaggio, BIOS, Windows 10, utenti, impostazioni, rete |', '',
          '## 00 Come si usa questa guida', '',
          '1. Si lavora a coppie, un PC per coppia. MANI fa, OCCHI legge e controlla.',
          '2. Ogni passo ha un numero, una sola cosa da fare e una figura.',
          '3. Le figure per ora sono schemi disegnati. Ogni schema ha un codice (per esempio FOTO-02-03): verrà sostituito dalla foto del docente.',
          '4. Sei bloccato? Scrivi la domanda all\'assistente della pagina della lezione. Il Professore serve se il PC non funziona, se un pezzo si rompe o se qualcuno si fa male.', '',
          '> [GIALLO] Parole da sapere. PC (Personal Computer). CPU (Central Processing Unit: il processore). RAM (Random Access Memory: la memoria di lavoro). SATA (Serial ATA: il cavo del disco). SSD (Solid State Drive: disco senza parti che girano). HDD (Hard Disk Drive: disco con un piatto che gira). USB (Universal Serial Bus: la porta della chiavetta).', '']
    for c in CAPITOLI:
        L += [f'## {c["n"]:02d} {c["titolo"]}', '', c['intro'], '']
        if c['n'] == 8:
            L += [tabella_ip(), '']
        for col, testo in c['box']:
            L += [f'> [{col}] {testo}', '']
        for p in c['passi']:
            L += [f'### {c["n"]:02d}.{p["n"]:02d} {p["titolo"]}', '', p['testo'], '']
            if tipo == 'bn':
                L += [f'> [BN] {p["bn"]}', '']
            vera = fv.get(p['id'])
            file = vera or (p['id'] + '.png')
            L += [f'![{p["id"]}]({rel_img}/{file})', '']
            L += [f'*{p["id"]} · ' + ('foto del docente*' if vera else 'schema: verrà sostituito dalla foto del docente*'), '']
    if tipo == 'docente':
        L += [GUASTI_MD.strip(), '']
    L += [f'## {10 if tipo == "docente" else 9:02d} Registro delle versioni', '']
    for i, x in enumerate(st, 1):
        L.append(f'{i}. v{x["v"]} ({x["data"]}): {x["nota"]}')
    L.append('')
    return '\n'.join(L)


# ------------------------------------------------------------------ MD -> HTML -> PDF
BOX = {'ROSSO': ('#fdecea', '#c0392b', 'ATTENZIONE'), 'BLU': ('#e8f1fb', '#1f6feb', 'DA CONFERMARE'),
       'GIALLO': ('#fff8db', '#d4a72c', 'NOTA'), 'BN': ('#f3f4f6', '#8c959f', '')}


def inline(s):
    s = escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def md_html(md, base):
    out, lista, passo, i = [], [], False, 0
    righe = md.split('\n')

    def chiudi_liste(n=0):
        while len(lista) > n:
            out.append('</li></ol>')
            lista.pop()

    def chiudi_passo():
        nonlocal passo
        if passo:
            out.append('</section>')
            passo = False

    while i < len(righe):
        ln = righe[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith('```'):
            chiudi_liste()
            j = i + 1
            buf = []
            while j < len(righe) and not righe[j].startswith('```'):
                buf.append(escape(righe[j]))
                j += 1
            out.append('<pre>' + '\n'.join(buf) + '</pre>')
            i = j + 1
            continue
        m = re.match(r'^(#{1,3}) (.*)$', ln)
        if m:
            chiudi_liste()
            chiudi_passo()
            lv = len(m.group(1))
            if lv == 3:
                out.append('<section class="passo">')
                passo = True
            cl = ' class="nuovo"' if lv == 2 and re.match(r'\d\d ', m.group(2)) and not m.group(2).startswith('00 ') and 'Registro' not in m.group(2) else ''
            out.append(f'<h{lv}{cl}>{inline(m.group(2))}</h{lv}>')
            i += 1
            continue
        m = re.match(r'^> \[(ROSSO|BLU|GIALLO|BN)\] (.*)$', ln)
        if m:
            chiudi_liste()
            bg, bd, et = BOX[m.group(1)]
            if m.group(1) == 'BN':
                out.append(f'<p class="bn" lang="bn">{inline(m.group(2))}</p>')
            else:
                out.append(f'<div class="box" style="background:{bg};border-left-color:{bd}"><b>{et}.</b> {inline(m.group(2))}</div>')
            i += 1
            continue
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', ln)
        if m:
            src = 'file://' + os.path.abspath(os.path.join(base, m.group(2)))
            cap_ = ''
            if i + 2 < len(righe) and righe[i + 2].startswith('*'):
                cap_ = righe[i + 2].strip('*')
                i += 2
            out.append(f'<figure><img src="{src}" alt="{escape(m.group(1))}"><figcaption>{inline(cap_)}</figcaption></figure>')
            i += 1
            continue
        if ln.startswith('|'):
            chiudi_liste()
            rows = []
            while i < len(righe) and righe[i].startswith('|'):
                rows.append([x.strip() for x in righe[i].strip().strip('|').split('|')])
                i += 1
            h = '<table><tr>' + ''.join(f'<th>{inline(x)}</th>' for x in rows[0]) + '</tr>'
            for r in rows[2:]:
                h += '<tr>' + ''.join(f'<td>{inline(x)}</td>' for x in r) + '</tr>'
            out.append(h + '</table>')
            continue
        m = re.match(r'^( *)(\d+)\. (.*)$', ln)
        if m:
            lv = len(m.group(1)) // 3 + 1
            if lv > len(lista):
                while len(lista) < lv:
                    out.append(f'<ol start="{m.group(2)}">')
                    lista.append(1)
            else:
                chiudi_liste(lv)
                out.append('</li>')
            out.append('<li>' + inline(m.group(3)))
            i += 1
            continue
        chiudi_liste()
        out.append(f'<p>{inline(ln)}</p>')
        i += 1
    chiudi_liste()
    chiudi_passo()
    return '\n'.join(out)


CSS = '''*{box-sizing:border-box}body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1a2330;font-size:11.5pt;line-height:1.45;margin:0}
h1{color:#12467a;font-size:19pt;margin:0 0 3mm;border-bottom:3px solid #2b7cc4;padding-bottom:2mm}
h2{color:#12467a;font-size:15pt;margin:6mm 0 2mm;background:#eef4fb;border-left:5px solid #2b7cc4;padding:2mm 3mm;break-after:avoid}
h2.nuovo{break-before:page}
h3{color:#1a5a94;font-size:12.5pt;margin:0 0 1.5mm;break-after:avoid}
.passo{break-inside:avoid;margin:4mm 0 5mm;padding:2mm 3mm;border:1px solid #d5e0ec;border-radius:6px}
.passo p{margin:1mm 0}
figure{margin:2mm 0 0;text-align:center}figure img{max-width:100%;max-height:50mm;border:1px solid #cfdae6;border-radius:4px}
figcaption{font-size:8.5pt;color:#57606a;font-style:italic;margin-top:1mm}
.bn{font-family:"Noto Sans Bengali","DejaVu Sans",sans-serif;font-size:11pt;color:#33475b;background:#f3f4f6;border-left:4px solid #8c959f;padding:1mm 3mm;margin:1.5mm 0}
.box{border-left:6px solid;border-radius:5px;padding:2.5mm 4mm;margin:3mm 0;break-inside:avoid}
ol{margin:1mm 0 2mm;padding-left:7mm}li{margin:1mm 0}
code{font-family:"DejaVu Sans Mono",monospace;background:#eef3f8;border:1px solid #d5e0ec;border-radius:3px;padding:0 3px;font-size:9.5pt}
pre{font-family:"DejaVu Sans Mono",monospace;background:#0c0c0c;color:#f0f0f0;padding:3mm;border-radius:5px;font-size:10pt;break-inside:avoid}
table{border-collapse:collapse;width:100%;margin:3mm 0;font-size:9.5pt;break-inside:avoid}
th{background:#12467a;color:#fff;text-align:left;padding:1.8mm 2.5mm;border:1px solid #12467a}
td{border:1px solid #cfdae6;padding:1.6mm 2.5mm;vertical-align:top}'''


def pdf(md_path, pdf_path, testa_sx, testa_dx, piede_sx):
    md = open(md_path, encoding='utf-8').read()
    corpo = md_html(md, os.path.dirname(md_path))
    doc = f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{corpo}</body></html>'
    from playwright.sync_api import sync_playwright
    tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8')
    tmp.write(doc)
    tmp.close()
    col = '#8a2a1c' if piede_sx.startswith('RISERVATO') else '#12467a'
    hd = (f'<div style="font-size:8px;width:100%;padding:0 15mm;color:#12467a;display:flex;justify-content:space-between">'
          f'<span>{escape(testa_sx)}</span><span>{escape(testa_dx)}</span></div>')
    ft = (f'<div style="font-size:8px;width:100%;padding:0 15mm;color:{col};display:flex;justify-content:space-between">'
          f'<span>{escape(piede_sx)}</span><span>pag. <span class="pageNumber"></span> di <span class="totalPages"></span></span></div>')
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        pg = b.new_page()
        pg.goto('file://' + tmp.name, wait_until='networkidle')
        pg.pdf(path=pdf_path, format='A4', print_background=True, display_header_footer=True, header_template=hd,
               footer_template=ft, margin={'top': '18mm', 'bottom': '16mm', 'left': '15mm', 'right': '15mm'})
        b.close()
    os.unlink(tmp.name)


def schemi_png():
    """Rende in PNG gli schemi SVG (uno per nome) e li copia come FOTO-CC-NN.png (uno per passo)."""
    conf = json.load(open(os.path.join(PUB, 'docs/anteprima/2inf-pc-05-11/config.json'), encoding='utf-8'))
    svg = dict(G.disegni(conf))
    svg.update(disegni_extra())
    os.makedirs(IMG, exist_ok=True)
    nomi = sorted({p['svg'] for p in TUTTI_PASSI})
    manca = [n for n in nomi if n not in svg]
    if manca:
        sys.exit('MANCANO schemi: ' + ', '.join(manca))
    from playwright.sync_api import sync_playwright
    tmpd = tempfile.mkdtemp()
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        pg = b.new_page(viewport={'width': 720, 'height': 400}, device_scale_factor=1.5)
        for n in nomi:
            pg.set_content('<html><body style="margin:0">' + svg[n] + '</body></html>')
            pg.screenshot(path=os.path.join(tmpd, n + '.png'), clip={'x': 0, 'y': 0, 'width': 720, 'height': 400})
        b.close()
    for p in TUTTI_PASSI:
        shutil.copyfile(os.path.join(tmpd, p['svg'] + '.png'), os.path.join(IMG, p['id'] + '.png'))
    shutil.rmtree(tmpd)
    return svg


def foto_da_inserire(versione):
    fv = foto_vere()
    L = ['# FOTO DA INSERIRE nella Mini guida PC', '',
         f'**Versione {versione}** — 05/11/2026 · RISERVATO · elenco generato da `strumenti/genera_dispensa_pc.py`', '',
         '## 01 Come si usano', '',
         '1. Il docente manda le foto nella chat con l\'ID (per esempio «FOTO-02-06»).',
         '2. Claude le inserisce con `strumenti/inserisci_foto_dispensa.py`: raddrizza, ritaglia se serve, porta a massimo 1600 px, toglie i dati EXIF (posizione, telefono), rigenera i PDF con una versione nuova.',
         '3. Le foto vanno anche nella dispensa pubblica dei ragazzi: niente volti, niente nomi, niente schermi con password.', '',
         '```', 'python3 strumenti/inserisci_foto_dispensa.py --versione 1.1 FOTO-02-06=/percorso/foto.jpg FOTO-03-03=/percorso/altra.jpg@0,200,3000,2000', '```', '',
         '## 02 Elenco dei segnaposto', '',
         '| ID | Passo | Che cosa deve mostrare la foto | Stato |', '|---|---|---|---|']
    for c in CAPITOLI:
        for p in c['passi']:
            L.append(f'| {p["id"]} | {c["n"]:02d}.{p["n"]:02d} {p["titolo"]} | {p["foto"]} | {"foto inserita" if p["id"] in fv else "schema"} |')
    L += ['', f'Totale: {len(TUTTI_PASSI)} segnaposto, {sum(1 for p in TUTTI_PASSI if p["id"] in fv)} con la foto vera.', '']
    return '\n'.join(L)


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--versione', required=True)
    a.add_argument('--nota', default='prima versione: capitoli 01-08 per i ragazzi, 09 «Creazione guasti» solo docente; schemi al posto delle foto')
    a.add_argument('--rifai', action='store_true', help='riscrive una versione già esistente (solo prima del commit)')
    a = a.parse_args()
    V = a.versione
    if not re.match(r'^\d+\.\d+$', V):
        sys.exit('Versione nel formato 1.0')
    usc = {'ragazzi': os.path.join(D2, f'MINI-GUIDA-PC-v{V}.md'), 'bn': os.path.join(D3, f'MINI-GUIDA-PC-BN-v{V}.md'),
           'docente': os.path.join(DR, f'DISPENSA-DOCENTE-PC-v{V}.md')}
    if not a.rifai and any(os.path.exists(x) for x in usc.values()):
        sys.exit(f'La versione {V} esiste già: non si riusa un numero (R11). Usa una versione nuova.')
    for d in (D2, D3, DR):
        os.makedirs(d, exist_ok=True)
    schemi_png()
    st = storico(V, a.nota)
    # immagini per il riservato (copia)
    os.makedirs(IMG_R, exist_ok=True)
    for nome in os.listdir(IMG):
        if re.match(r'^FOTO-\d\d-\d\d\.(png|jpg)$', nome):
            shutil.copyfile(os.path.join(IMG, nome), os.path.join(IMG_R, nome))
    rel = {'ragazzi': 'img-mini-guida-pc', 'bn': '../../classe-2/dispense/img-mini-guida-pc', 'docente': 'img-dispensa-pc'}
    testa = {'ragazzi': ('Mini guida PC v' + V, '2INF e 3INF · a.s. 2026/27', 'Corso di Informatica · Laboratorio · 05/11/2026'),
             'bn': ('Mini guida PC v' + V + ' (bangla)', '3INF · a.s. 2026/27', 'Corso di Informatica · Laboratorio · 05/11/2026'),
             'docente': ('Dispensa docente PC v' + V, '2INF e 3INF · a.s. 2026/27', 'RISERVATO — non pubblicare · Dispensa docente PC')}
    for tipo, mdp in usc.items():
        open(mdp, 'w', encoding='utf-8').write(scrivi_md(tipo, V, rel[tipo], st))
        pdf(mdp, mdp[:-3] + '.pdf', *testa[tipo])
        print('OK', mdp[:-3] + '.pdf')
    open(os.path.join(DR, 'FOTO-DA-INSERIRE.md'), 'w', encoding='utf-8').write(foto_da_inserire(V))
    print(f'{len(TUTTI_PASSI)} passi, {len(foto_vere())} foto vere. FOTO-DA-INSERIRE.md aggiornato.')


if __name__ == '__main__':
    main()
