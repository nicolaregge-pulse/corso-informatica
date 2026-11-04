# Guida del docente: 3INF Mastermind in rete v4.0, mercoledì 04/11/2026

**Versione 1.0** — 04/11/2026. Laboratorio 11:00-13:00 (2 ore). Il protocollo, il client diviso in UnitInterfaccia e UnitRete, la partita di classe, il commit su GitHub, il quiz sulla rete. Nessun nome di allievo (repository pubblico).

> **Nota:** Orario confermato dal registro: 3INF 11:00-13:00. Nel file REGISTRO-TESTI-04-11 del riservato le ore sono scritte 12-13 e 13-14: è un errore, da correggere (ho avvisato Claude). Il testo da firmare resta valido.

## 00 In una pagina

| Ora | Orario | Si fa | Vittoria entro 10 minuti | KPI |
|---|---|---|---|---|
| 1 | 11:00-12:00 | Animazione alla lavagna, schede, «Il Prof finto» | Le 5 risposte del server scoperte nella pagina | (preparazione) |
| 2 | 12:00-13:00 | Client v4 in Lazarus, collegamento, partita di classe, GitHub, quiz | «Collegato! Ciao» nel client | Collegato +15, commit chiaro +15, quiz 8/12 +10 |

1. Voto da 40 a 80. Il cruscotto mostra per primi: Prof finto, client collegato, commit chiaro, quiz. I KPI sono proposti, vanno da te confermati.
2. **Regola 31:** l'ora 2 resta «in arrivo» finché non scrivi a Claude «sblocca ora 2».
3. Una scheda in bangla c'è solo per l'allievo del PC 14, sotto ogni frase. L'ho scritta io: fallo controllare da chi la legge.
4. Firma ogni ora all'inizio. Limite 14:05.

## 01 Prima di entrare: il Server sul PC del docente

Il server è un programma tuo, nella cartella `Server` del progetto. Farlo PARTIRE per tempo è la cosa più importante di oggi.

1. **Scarica e apri il progetto.** Estrai `mastermind-bello-v4.0.zip` (lo stesso dei ragazzi) in Documenti. Apri con Lazarus `Server\ServerMastermind.lpi`.
2. **Premi F9.** La prima volta Lazarus compila: ci vuole un po'. Compare la finestra «Mastermind bello - il SERVER del prof».
3. **Premi «Avvia server».** La porta è 5050: non toccarla.
4. **Windows chiede il permesso (firewall).** Clicca **Consenti accesso**. Se ti fa scegliere il tipo di rete, spunta anche quella della scuola (privata o di dominio; se non sai, spunta tutte).
   > **Attenzione:** Se rispondi Annulla, il firewall blocca i ragazzi e nessuno si collega. Per rimediare: Pannello di controllo, Windows Defender Firewall, «Consenti app», trova ServerMastermind e spunta le reti. Può servire l'amministratore (da verificare in aula).
5. **Trova l'IP.** Il server lo scrive in alto: «IP di questo PC: ...». Copialo.
6. **Scrivi l'IP in grande alla lavagna.** Poi dillo a Claude in chat: può metterlo anche nella pagina dei ragazzi (campo `server_ip`).
7. **Prova da solo.** Apri anche il client (`Client\ClientMastermind.lpi`, F9), nella casella IP scrivi `127.0.0.1` (significa: questo stesso computer) e premi Connetti: deve comparire «Collegato! Ciao ...». Prova solo che il server funziona, non il firewall.
8. **Test vero del firewall.** Appena il primo ragazzo ha il client aperto (ora 2), il suo Connetti con il tuo IP è la prova. Se non va, vai alla tabella errori.
9. **Lavagna e animazione.** Apri `animazione-protocollo.html` nel browser (25 passi, bottoni Avanti, Indietro, Riparti; anche freccia destra) e `lavagna-3inf-04-11.pdf` (15 pagine) in SumatraPDF.
10. **Altre schede:** pagina ora 1 `https://nicolaregge-pulse.github.io/corso-informatica/anteprima/3inf-protocollo-04-11/index.html`, il tuo cruscotto (`cruscotto.html` della stessa cartella), il monitor `https://nicolaregge-pulse.github.io/corso-informatica/3inf-monitor/`, Veyon.

> **Da confermare:** Non è provato che la rete della scuola faccia parlare tra loro due PC del laboratorio (alcune reti isolano i computer). Piano B se non si collegano: tutti usano «Gioca da solo» e fai vedere le righe sul Registro del TUO server con un solo client (o con la pagina «Prof finto»). La lezione sul protocollo si regge comunque.

## 02 I concetti, spiegati a te

1. **Client e server.**
   1. Il **client** chiede, il **server** risponde. Come in un bar: il cliente ordina, il barista risponde.
   2. Qui: il client è il programma di ogni ragazzo, il server è il tuo (il barista), e i ragazzi sono tanti clienti.
2. **IP e porta.**
   1. L'**indirizzo IP** dice QUALE computer: come il numero civico di un palazzo.
   2. La **porta** dice QUALE programma dentro quel computer: come il citofono di un palazzo. Il nostro è il 5050.
   3. Gli indirizzi tipo 192.168.x.x, 10.x.x.x, 172.16-31.x.x sono indirizzi interni (privati): vanno bene dentro la scuola, non da internet. Per parlarsi i PC devono stare sulla stessa rete (da verificare per la scuola).
   4. Le porte basse (80 per le pagine web, 21, 22...) sono riservate a servizi noti. 5050 è un numero alto, di solito libero. Se il server dice che la porta è occupata, prova 5051 e dillo ai ragazzi (da verificare se in aula serve).
3. **Una riga che va, una riga che torna.**
   1. Il client apre la connessione, scrive UNA riga di testo, aspetta UNA riga di risposta, chiude. Come una telefonata brevissima: «Pronto, come va?», «Bene», riattacco.
   2. Per questo ogni 3 secondi il client richiama per sapere lo STATO: ogni volta è una telefonata nuova.
   3. Sotto c'è TCP (da verificare se vuoi andare in profondità): garantisce che le righe arrivino complete e in ordine. A noi basta sapere che esiste.
4. **Il protocollo.**
   1. È l'accordo sul linguaggio: come si scrive una domanda, quali risposte esistono. Senza accordo i due programmi non si capiscono.
   2. Qui: il client fa DUE domande, **STATO;nome** e **GUESS;nome;1234**. Il server dà CINQUE risposte: **STATO, WAIT, RESULT, WIN, ERR**.
   3. Una riga è fatta di **campi separati da punto e virgola**. Il primo campo (numero 0) dice che cosa è la riga. Chi legge conta i campi: è come una riga di Excel.
5. **Leggere una risposta.**
   1. **RESULT;1;2;1;0;1;6;6** = tipo, neri, bianchi, tentativi, posto, finiti, migliore, peggiore. Quindi 1 nero e 2 bianchi.
   2. Nero = colore giusto al posto giusto. Bianco = colore giusto al posto sbagliato. Con segreto 1413 e tentativo 1234: 1 nero (l'1 al primo posto) e 2 bianchi (il 3 e il 4 ci sono nel segreto, ma in altre posizioni).
   3. WAIT = «aspetta il Via». ERR = errore, con il motivo. WIN = hai vinto, con nome, tentativi e secondi.
   4. Colori: 1 rosso, 2 giallo, 3 verde, 4 blu, 5 arancio, 6 porpora.
6. **Perché il client è diviso in due unit.**
   1. **UnitInterfaccia** = la finestra (disegni, bottoni, pioli). **UnitRete** = la rete (collegarsi, scrivere e leggere una riga, capire il protocollo).
   2. UnitRete NON conosce la finestra: nel suo `uses` non c'è Forms. Così si prova da sola e chi disegna non tocca la rete.
   3. Come parla alla finestra? Con un **evento**, come OnClick: `Rete.OnRisultato := @ReteRisultato` vuol dire «quando arriva RESULT, chiama la mia procedura». È un OnClick lanciato dalla rete invece che dal mouse.
7. **Il commit.** È una fotografia del progetto con un messaggio. «Add files via upload» non dice niente. «Mastermind v4: provato il protocollo, titolo con il mio nome» dice cosa e perché.

## 03 Ora 1 (11:00-12:00): il protocollo

**Obiettivo:** «Capire come parlano il client e il server: una riga va, una riga torna.»

**Vittoria rapida:** entro 10 minuti ogni ragazzo ha fatto comparire nel «Prof finto» la prima risposta (STATO). Entro la fine, tutte e 5 (segno verde per ciascuna).

| Minuti | Tu | Loro |
|---|---|---|
| 11:00-11:05 | Firma. Dì dove siamo: «Oggi i vostri Mastermind parlano con il mio». Mostra il server acceso. | Aprono la pagina ora 1, scrivono nome |
| 11:05-11:25 | Animazione, 25 passi: ferma ai passi chiave e chiedi «Cosa risponde il server adesso?» | Guardano, rispondono a voce |
| 11:25-11:35 | Lavagna p.4-8 (righe, campi, due domande, cinque risposte, RESULT letto). Scrivi alla lavagna RESULT;1;2 e cerchia i campi. | Leggono le 7 schede (hanno il disegno) |
| 11:35-11:55 | Missione 1: il Prof finto. Giri. | Scoprono STATO, WAIT, RESULT, WIN, ERR |
| 11:55-12:00 | Missione 2: spiegare una riga a un compagno. Lavagna p.9 (le due unit). | Spiegano a voce |

**Cosa dire:**

1. «Il vostro programma non gioca: manda una riga al mio e riceve una riga.»
2. «Una riga è come una riga di Excel: i campi sono le colonne, e il separatore è il punto e virgola.»
3. «WAIT vuol dire solo: aspetta, il Prof non ha ancora premuto Via.»
4. «Il client ha DUE domande, il server CINQUE risposte. Il protocollo è questo elenco.»

**Cosa disegnare alla lavagna (PDF p.2-8):** due scatole CLIENT e SERVER con una freccia che va e una che torna; il numero 5050 sul server; la riga RESULT;1;2 spezzata in campi.

**Domande al volo (prova del nove).** Segna OK/KO.

| Domanda | Risposta attesa |
|---|---|
| Su che porta ascolta il server? | 5050. |
| Cosa manda il client per sapere come va? | STATO;nome. |
| Il Prof non ha premuto Via: cosa risponde il server a un tentativo? | WAIT. |
| In RESULT;2;1;4;0;3;3;7 quanti neri e bianchi? | 2 neri e 1 bianco. |
| Qual è la differenza tra IP e porta? | IP = quale computer, porta = quale programma. |
| Perché UnitRete non ha bisogno della finestra? | Perché avvisa con eventi: non sa chi ascolta. |

**Errori tipici ora 1:**

| Problema | Causa | Cosa fare |
|---|---|---|
| Il «Prof finto» non risponde | Scheda non aggiornata | F5, scrivere il nome e riprovare |
| Non capiscono «campo» | Parola nuova | Esempio: la riga di Excel |
| L'animazione va troppo veloce | 25 passi | Ferma con Indietro, chiedi a un ragazzo di dire cosa succede |

**Sblocco ora 2:** alle 12:00, quando la maggior parte ha le 5 risposte. Scrivi a Claude: «sblocca ora 2».

## 04 Ora 2 (12:00-13:00): il client vero, la partita, GitHub, il quiz

**Obiettivo:** «Il vostro client parla davvero con il mio server: gioca la partita di classe.»

**Vittoria rapida:** entro 10 minuti il client apre e «Gioca da solo» funziona (anche senza rete). Entro le 12:20 «Collegato! Ciao ...».

| Minuti | Tu | Loro |
|---|---|---|
| 12:00-12:05 | Firma. «sblocca ora 2». IP alla lavagna (grande). Server acceso. | Scaricano lo zip, Estrai tutto |
| 12:05-12:15 | Giri. Lavagna p.11. | Apri progetto Client, F9 (la prima volta è lenta), Gioca da solo |
| 12:15-12:25 | Lavagna p.12. Controlla il tuo server: «Collegati: N». | IP + nome, Connetti, «Collegato!» |
| 12:25-12:35 | Preme Via!. Lavagna p.13. Proietta Classifica e Registro del server. | Partita di classe: stesso codice per tutti |
| 12:35-12:42 | «Cercate PORTA_SERVER e Elabora» | Ctrl+F: PORTA_SERVER, Elabora in UnitRete.pas |
| 12:42-12:50 | «Il titolo con il vostro nome» | TITOLO_FORM in UnitInterfaccia.pas, F9 |
| 12:50-12:58 | Lavagna p.14: commit. Mostra un buon messaggio. | GitHub: Add file, Upload files, messaggio, Commit changes, manda il link |
| 12:58-13:00 | Lavagna p.15. | Quiz sulla rete (12 domande, servono 8) |

> **Nota:** Il tempo è molto stretto: partita, commit e quiz in 60 minuti. Se serve, il quiz si fa all'inizio della prossima lezione. Priorità: collegato, poi commit chiaro, poi quiz.

**Cosa dire:**

1. «Ora il programma è quello vero. Apritelo e premete F9: la prima volta Lazarus ci mette un po'.»
2. «Nella casella IP scrivete i numeri alla lavagna, senza spazi. Poi il vostro nome, poi Connetti.»
3. «Guardate il Registro del mio server: ogni riga che arriva è una domanda di un vostro client.»
4. «Il messaggio del commit deve dire COSA avete fatto. Non: aggiunti file.»

**Cosa mostrare dal server (proiettato):** Collegati, Classifica, Registro (le righe che passano). È la prova viva che «una riga va, una riga torna».

**Domande al volo:**

| Domanda | Risposta attesa |
|---|---|
| Cosa significa «Collegato! Ciao»? | Il server ha risposto alla mia riga STATO. |
| Dove si trova la porta nel codice? | PORTA_SERVER in UnitRete.pas, vale 5050. |
| Che cosa fa Elabora? | Legge il primo campo e sceglie l'evento giusto. |
| Che messaggio di commit è buono? | Uno che dice cosa e perché. |
| Cosa succede se cambio la porta del client? | Non trova il server. |

**Errori tipici ora 2 (rete):**

| Messaggio nel client | Significa | Cosa fare |
|---|---|---|
| «Scrivi l'IP del server...» | Casella IP vuota | Scrivere l'IP della lavagna |
| «Connessione rifiutata: il server non e' acceso oppure la porta e' sbagliata.» | Server non avviato o porta diversa | Controlla sul server: «ACCESO (porta 5050)». Premi Avvia server |
| «Il server non risponde: controlla l'IP ... e il firewall.» | IP sbagliato o firewall | 1) IP uguale alla lavagna? 2) Firewall sul PC del Prof: Consenti accesso 3) stessa rete? |
| «L'IP non e' scritto bene: deve avere 4 numeri separati da punti.» | Errore di battitura | Riscrivere: niente spazi, punti al posto delle virgole |
| «Il server non ha risposto. Riprova tra un attimo.» | Server occupato | Premere di nuovo Connetti |
| «Il server non risponde piu'...» | Il server si è fermato | Controlla il server e premi Connetti |

| Problema | Causa | Cosa fare |
|---|---|---|
| Server: «Non riesco ad aprire la porta 5050» | Un altro server è già acceso, o la porta è bloccata | Chiudere il vecchio server. Se serve, porta 5051 (e dire ai ragazzi: IP:5051, il client accetta anche IP:porta) |
| IP sbagliato nel server | Più schede di rete (VPN, macchine virtuali) | Scegliere l'IP che inizia come quello dei PC dei ragazzi. Da verificare in aula |
| F9 non parte | Il .lpi è fuori dalla cartella estratta | Estrarre TUTTA la cartella (Estrai tutto), non aprire dallo zip |
| Lazarus: unit non trovata | Cartella Comune spostata | Il progetto legge `../Comune/DisegnoMastermind.inc`: non spostare le cartelle |
| Nessuno si collega | Rete della scuola isola i PC (da verificare) | Piano B (sezione 01) |
| Il nome è già preso o non valido | Il server risponde ERR;nome non valido | Scrivere un nome senza spazi o simboli strani |
| GitHub: «Add files via upload» | Messaggio non cambiato | Riscrivere il messaggio nel riquadro |
| Commit: non trovano il link | Pagina sbagliata | Aprire il commit (riga con il messaggio) e copiare l'indirizzo dalla barra |

**Cruscotto: cosa guardare.** Colonna Prof finto (ora 1), client collegato (spunta quando il server lo vede o con «Sono collegato», da confermare col server), commit chiaro (link ricevuto più messaggio che non sia «Add files via upload»), quiz. Fermo da più di 5 minuti.

**Consegna:** link del commit con il bottone «Manda al prof»; quiz su Moduli (link nel compito).

**Quiz sulla rete:** 12 domande su Moduli, soglia 8 su 12. La prova resta valida come traccia per la Regione solo se è il Modulo allegato al compito su Classroom (regola 33).

## 05 Chi è indietro, chi si stufa, chi finisce prima

1. **Chi è indietro.**
   1. Parti da quello che ha già: «Il tuo Gioca da solo funziona? Bene, già vedi il client».
   2. Un compagno vicino può collegarsi per primo: «Guarda cosa succede nel Registro del server quando premi Connetti».
   3. Nessuno viene escluso dalla partita: chi non si collega gioca da solo e fa lo stesso quiz.
2. **Chi si stufa.**
   1. Cambia lo scopo: sfida a chi indovina prima, classifica sulla lavagna.
   2. Dagli un compito vero: «Trova nel codice dove si decide il colore del piolo».
3. **Chi finisce prima.**
   1. Bonus: cambia il titolo con una frase, i colori, o `MOSTRA_CODICE_NEL_TITOLO` (da leggere nel LEGGIMI).
   2. Spiega a un compagno perché UnitRete non ha Forms.
   3. Legge il Registro del server e capisce un GUESS di un altro.
4. **Allievo del PC 14 (bangla):** sotto ogni frase della pagina c'è la riga in bangla. Se qualcosa non torna, chiedi a lui di dirtelo con parole sue.

## 06 Fine ora, registro, firma

1. **Fine ora 2:** chiedi a tre ragazzi «Cosa manda il client? Cosa risponde il server?». Segna 70 OK / 50 KO.
2. **Testi per il registro (corti):**

Ora 1:

```
Master Mind: il protocollo di rete
```

Ora 2:

```
Master Mind in rete: client e server
```

3. **Voce dell'Allegato A:** nel Word PFP_3 la voce che c'è è Competenza 8, II Anno, «Creazioni di applicazioni con Lazarus», «Esercizi: Master Mind e Slide Show». «Protocolli di rete» e «TCP/IP porte» (Comp. 16) NON risultano nel Word del 02/11.
   > **Attenzione:** È una criticità aperta: la voce «Protocolli di rete: il protocollo del Mastermind e le porte TCP/IP» va aggiunta. Se ne occupa Claude con te.
4. **Firma:** all'inizio di ciascuna ora. «FIRMA» in verde = firmata. Limite 14:05.
