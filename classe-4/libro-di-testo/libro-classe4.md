# Libro di testo — Informatica Classe 4

**Versione 1.0** — 29/10/2026
*Il libro di testo della 4TI: raccoglie in un unico posto la teoria e le esercitazioni svolte in classe, lezione per lezione. Cresce a ogni lezione. Il PDF (libro-classe4-vX.Y.pdf) serve per leggere e stampare; questo MD è la fonte versionata, da dare alla tua AI (NotebookLM, Gemini) perché ti spieghi ogni parte con parole semplici. Ogni lezione ha anche il suo libro parziale nella cartella lezioni.*

---

## 0 Come lavoriamo (leggere per prime)
1. Si lavora un passo alla volta, con un risultato concreto da vedere subito.
2. Consegne e materiali stanno su Google Classroom; i progetti stanno su GitHub, ognuno nel suo repository.
3. Ogni lezione ha la sua pagina con le schede di teoria, il ripasso e la verifica: leggi le schede prima di rispondere.
4. Se ti blocchi, chiedi all'assistente nella casella della pagina: risponde subito.
5. L'AI aiuta a capire, non a saltare il pensiero: la prova che hai capito è saperlo spiegare a voce con parole tue.
6. Il progetto individuale di stage è il filo dell'anno: ogni lezione ci aggiunge un pezzo.

## 1 Le lezioni una per una
*In ordine di data: che cosa abbiamo fatto, la teoria e l'esercitazione di ogni lezione.*

<!-- LEZIONI:INIZIO -->
### L01 22/09/2026 — Presentazione del corso e lo stage

*Libro parziale: lezioni/2026-09-22_presentazione-stage.md*

#### Che cosa abbiamo fatto

1. **Quando:** 22/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Presentazione del corso; lo stage e il progetto individuale.

#### La teoria e l'esercitazione

Questa lezione è stata di organizzazione e di avvio: non ha una dispensa scritta. Gli argomenti sono quelli elencati sopra.

### L02 29/09/2026 — Organizzazione del corso, Git e IA

*Libro parziale: lezioni/2026-09-29_git-ai-notebooklm.md*

#### Che cosa abbiamo fatto

1. **Quando:** 29/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Organizzazione del corso; Git, GitHub e l'intelligenza artificiale (NotebookLM) per studiare.

#### La teoria e l'esercitazione

*Documento di teoria per l'allievo, in versione testo (.md). E la stessa dispensa
in formato testo puro: puoi darla a Gemini per farti spiegare o tradurre le parti
difficili, o caricarla come fonte. I disegni (i grafi dei rami) qui sono descritti
a parole. Regola d'oro del corso: l'IA serve a CAPIRE meglio, non a copiare; la
prova del nove e saperlo spiegare a parole tue.*

---

##### 1. I tre strumenti e come si legano
1. Usiamo tre ambienti diversi, ognuno con un compito preciso:
   1. **Git e GitHub**: il magazzino ordinato del lavoro, dove ogni versione resta salvata e condivisibile.
   2. **Gemini**: l'IA (Intelligenza Artificiale) generativa a cui si parla; le si da un testo (anche un file .md) e ti spiega, traduce, riassume.
   3. **NotebookLM**: un tutor che risponde SOLO sui documenti che carichi (per esempio un PDF), quindi resta fedele alla fonte.
2. Idea da tenere a mente: **Git conserva**, **Gemini spiega**, **NotebookLM ripassa sulla fonte**. Non sono concorrenti: si usano insieme.

##### 2. Git e GitHub
1. **Git** e un sistema di **versionamento**: tiene la storia del lavoro, cosi ogni salvataggio importante resta e si puo tornare indietro.
2. **GitHub** e il sito in rete dove il lavoro versionato vive e si condivide: e "Git su internet". Attenzione a non confonderli: **Git** e lo strumento (il motore), **GitHub** e il servizio online (il garage online).

###### 2.1 GitHub: un'azienda e un servizio
1. E un'**azienda** (GitHub, Inc., dal 2018 di Microsoft): come ogni azienda deve mantenersi.
2. E un **servizio** online: un sito dove metti i progetti in rete, li tieni al sicuro e ci lavori in gruppo, tutto da browser.

###### 2.2 Il repository, il commit, il branch
1. Un **repository** (o "repo") e la cartella-progetto con dentro i file e tutta la loro storia.
2. Un **commit** e un salvataggio con etichetta: fotografa il progetto in quel momento e gli mette un messaggio ("cosa ho cambiato"). Tanti commit in fila fanno la **storia**.
3. Un **branch** (ramo) e una strada di lavoro parallela, per provare senza rovinare la versione principale (il **main**); riunire un ramo al main si chiama **merge**.
4. La **Pull Request** (PR) e la proposta di unire il proprio ramo nella versione principale, dopo che qualcuno l'ha controllata.

###### 2.3 Che tipo di servizio: PaaS e Freemium
1. **PaaS** (Platform as a Service: piattaforma come servizio): qualcuno ti mette online una piattaforma gia pronta e tu la usi senza costruirti server e computer. Fa parte della famiglia "…aaS" (IaaS = server nudi, PaaS = piattaforma pronta, SaaS = software pronto nel browser).
2. **Freemium** (free + premium): le funzioni di base sono gratis; per le funzioni avanzate si paga. A te studente basta la parte gratis.

##### 3. Il versioning: le versioni 1.2.3
1. Quando un progetto raggiunge un punto "buono", gli si da un numero di versione di tre cifre `1.2.3`:
   1. **major** (la prima cifra): aumenta quando cambi tutto in modo grosso, magari incompatibile col vecchio.
   2. **minor** (la seconda): aumenta quando aggiungi una funzione nuova, ma il resto funziona ancora.
   3. **patch** (la terza): aumenta quando correggi solo un bug, niente di nuovo.
2. Esempio: `v1.0.0` prima versione giocabile, aggiungi i suoni `v1.1.0`, correggi un bug `v1.1.1`, rifai tutto da capo `v2.0.0`.
3. Una versione pubblicata (**release**) e "congelata".

> [GIALLO] Regola d'oro del versioning: una versione gia pubblicata non si riusa mai. Se cambi anche una sola cosa, prima aumenti il numero e poi pubblichi.

##### 4. Casi d'uso di Git (i grafi, descritti a parole)
1. **Sviluppo lineare**: un solo autore, nessun ramo. I commit vanno in fila, la storia e una linea dritta. Se qualcosa si rompe, torni indietro di un commit.
2. **Una funzione su un branch, poi merge**: provi una funzione su un ramo separato mentre il main resta sano; quando e pronta la unisci (merge).
3. **Due funzioni in parallelo**: due rami partono insieme e si fondono in tempi diversi; il main raccoglie i pezzi man mano.
4. **Hotfix urgente**: durante una funzione lunga esce un bug grave; apri un ramo hotfix corto, lo correggi e lo unisci subito, poi torni alla tua funzione.
5. **Le release**: ogni tanto pubblichi una versione (bandierina sul main): v1.0, v1.1, v1.2… fino a un cambiamento grosso v2.0. Ogni release e congelata.
6. **Ramo abbandonato**: provi un'idea su un ramo e non la unisci mai; il main non ne risente. Nessun danno.
7. **Ramo da un altro ramo**: una funzione grande stacca un sotto-ramo; prima rientra il sotto-ramo nel ramo, poi il ramo nel main (scatole dentro scatole).
8. **Grande integrazione (gruppo)**: ognuno ha il suo ramo (grafica, movimenti, audio, menu) e alla fine confluiscono tutti nel main con le Pull Request: nasce la v1.0.
9. **Ramo di manutenzione**: il main va verso la v2.0, ma per chi usa ancora la v1 tieni un ramo parallelo con solo i fix (v1.1, v1.2).
10. **Revert**: un commit ha introdotto un problema; non cancelli la storia, aggiungi un nuovo commit che annulla quello sbagliato (revert), lasciando traccia onesta.
11. **Conflitto di merge**: due rami cambiano la stessa riga in modo diverso; Git si ferma e una persona sceglie cosa tenere, chiudendo con un commit di risoluzione.
12. **Squadra a 5 rami con due release**: sul main si pubblicano v1.0 e v2.0 mentre quattro rami lavorano in parallelo e rientrano in momenti diversi.
13. **Rami annidati a 5 livelli**: un lavoro grande si divide in rami dentro rami, fino a cinque livelli; ogni livello rientra nel precedente, come le matriosche.
14. **Due major insieme**: dopo la v1.0 il main punta alla v2.0, ma restano vivi due rami di manutenzione (v1.x e poi v2.x).
15. **Storia realistica**: tutto insieme — release, feature con sotto-ramo, hotfix, revert e un merge con conflitto: la fotografia di un progetto vero.

> [GIALLO] Come si legge un grafo: ogni pallino e un commit, la linea orizzontale in alto e il main, le linee colorate che si staccano sono branch, quando due linee si riuniscono e un merge, le bandierine gialle sono le release.

##### 5. I file Markdown (.md)
1. Un file **Markdown** (estensione **.md**) e **testo puro** con pochi simboli:
   1. `#` a inizio riga fa un titolo;
   2. `**parola**` mette in grassetto;
   3. una riga con `1.` fa un elenco numerato.
2. Si legge ovunque e non contiene immagini pesanti: solo contenuto. Per questo l'IA lo legge molto bene: nel corso diamo le dispense anche in .md proprio per darle a Gemini.

##### 6. Gemini: l'IA generativa, e come usarla con un file .md
1. **Gemini** e un'IA **generativa**: le scrivi una richiesta (un "prompt") e genera una risposta: spiega, traduce, riassume, fa domande di ripasso.
2. L'IA puo **sbagliare o inventare** (allucinazioni): quello che dice va controllato, soprattutto date, numeri e fonti.

###### 6.1 Passi per usare Gemini con un file .md
1. Nel browser vai su questo indirizzo, con l'account della scuola:

```
gemini.google.com
```

2. Apri il file .md, **seleziona tutto** e **copialo**; torna su Gemini e **incolla** (oppure allega il file).
3. Scrivi la richiesta, per esempio:

```
Spiegami con parole semplici la parte che non capisco: [incolla la frase].
```

###### 6.2 Quale versione di Gemini scegliere
1. In alto Gemini ha un menu per la **versione del modello**. I nomi/numeri cambiano; conta a cosa serve ciascuna:
   1. **Flash** (veloce): risposte rapide per cose semplici (spiegazioni, traduzioni, riassunti brevi). La scelta di tutti i giorni.
   2. **Pro** (per esempio "3.1 Pro", piu potente): per compiti complessi e testi lunghi. Piu lenta ma piu capace.
   3. **Ragionamento** (per esempio "3.6 ragionamento", che "pensa" prima di rispondere): per problemi difficili, passo per passo. La piu lenta ma la piu accurata.
2. Regola pratica: parti da **Flash**; se la risposta e complessa o ti sembra sbagliata, passa a **Pro** o **Ragionamento** e richiedi.
3. Guarda a **cosa serve** la versione (veloce / potente / ragiona), non solo al numero.

> [GIALLO] Le versioni piu potenti o di "ragionamento", con l'account gratuito, possono avere un limite giornaliero: usale quando servono davvero, per il resto va bene Flash.

##### 7. NotebookLM: il tutor sulle fonti, e come usarlo con un PDF
1. **NotebookLM** risponde **solo** sui documenti che carichi: se carichi un PDF, ti risponde usando quel PDF e non inventa fuori da li.
2. E ottimo per **studiare e ripassare** su una fonte precisa (una dispensa, un capitolo): resta fedele al testo.

###### 7.1 Passi per usare NotebookLM con un PDF
1. Nel browser vai su questo indirizzo, con l'account della scuola:

```
notebooklm.google.com
```

2. Clicca `Crea nuovo`, poi `Carica`, e scegli un file **PDF**; aspetta che la fonte compaia a sinistra.
3. Nel riquadro della chat scrivi, per esempio:

```
Fammi un riassunto semplice di questo documento.
```

> [GIALLO] Se non hai un PDF sul computer: su github.com entra nella cartella del documento, clicca sul PDF e poi sull'icona di download (freccia in giu) in alto a destra.

##### 8. Il flusso completo: i tre ambienti insieme
1. Il materiale del corso sta su **Git/GitHub** (versionato).
2. Da li si **scarica** il PDF (per leggere/stampare) o il file **.md** (per l'IA).
3. Il **.md** si da a **Gemini** per farsi spiegare o tradurre.
4. Il **PDF** si carica su **NotebookLM** per interrogarlo e ripassare restando sulla fonte.
5. Il lavoro finito si **consegna su Classroom**.

| Strumento | A cosa serve | Cosa gli dai |
|---|---|---|
| Git / GitHub | Conservare e condividere il lavoro versionato | I file del progetto |
| Gemini | Spiegare, tradurre, riassumere | Un testo o un file .md |
| NotebookLM | Ripassare restando fedele alla fonte | Un documento (per esempio un PDF) |

##### 9. Uso responsabile dell'IA
1. **Capire, non copiare**: l'IA e un aiuto per imparare, non un modo per saltare il lavoro. La prova del nove: saperlo spiegare a parole proprie.
2. **Controllare sempre**: l'IA puo sbagliare o inventare; verifica quello che dice.
3. **Privacy e dati**: non inserire dati personali, di compagni o di famiglia negli assistenti.

##### 10. Prendi appunti a mano
1. Prima di usare gli strumenti, disegna sul quaderno tre riquadri (Git, Gemini, NotebookLM) e, per ognuno, a cosa serve e cosa gli dai.
2. Gli appunti a mano confluiscono nel tuo quaderno personale: aiutano a fissare i concetti e servono per la prova del nove.


*Compito unico in tre parti. Provi le tre cose viste in classe: capire e usare
Git/GitHub, usare Gemini con un file .md, usare NotebookLM con un PDF. Puoi
tenere aperta la dispensa di teoria. Si lavora tutto da browser, senza installare
nulla. Alla fine consegni su Classroom.*

---

##### 1. Come si consegna
1. Scrivi le risposte in un documento di **Google Documenti** (uno solo per tutto il compito).
2. Intitola il documento con **Cognome e Nome** e **"Compito Git e AI"**.
3. Dove chiesto, incolla uno **screenshot** (cattura schermo) come prova.
4. Alla fine **consegni** il documento nel compito su **Classroom**.

> [GIALLO] Come si fa uno screenshot (Windows 10 e 11): premi insieme i tasti `Windows` + `Maiusc` + `S`, seleziona la parte di schermo, poi incolla nel documento con `Ctrl` + `V`.

##### 2. Parte 1 — Git e GitHub

###### 2.1 Domande (rispondi a parole tue)
1. Con parole tue, che differenza c'e tra **Git** e **GitHub**?
2. Che cos'e un **repository**?
3. Che cos'e un **commit** e a cosa serve avere la storia dei commit?
4. A cosa serve un **branch** e cosa propone una **Pull Request**?

###### 2.2 Azione pratica
1. Nel browser entra su questo indirizzo con il tuo account:

```
github.com
```

2. Apri un **repository** del corso (quello indicato dal docente) e guarda l'elenco dei file.
3. Apri la sezione dei **commit** (la storia) e osserva gli ultimi salvataggi.
4. Fai uno **screenshot** della storia dei commit e incollalo nel documento.
5. Scrivi due righe: **cosa** mostra quella schermata (che cosa e cambiato nell'ultimo commit).

##### 3. Parte 2 — Gemini con un file .md

###### 3.1 Esercitazione
1. Nel browser entra su questo indirizzo con l'account della scuola:

```
gemini.google.com
```

2. In alto scegli la versione **Flash** (quella veloce): per questo compito basta.
3. Apri il file **.md** indicato dal docente (per esempio la dispensa di teoria in formato .md), **seleziona tutto** e **copialo**.
4. **Incolla** il testo in Gemini e chiedi, con parole tue, di spiegarti una parte. Puoi partire da qui:

```
Spiegami con parole semplici cosa sono i file Markdown e perche sono comodi per l'IA.
```

5. Poi chiedi a Gemini di verificarti:

```
Fammi 3 domande per controllare se ho capito, poi correggimi le risposte.
```

###### 3.2 Cosa consegni della Parte 2
1. Uno **screenshot** della risposta di Gemini.
2. Con parole tue: **cosa** ti ha spiegato e se hai dovuto **correggere** qualcosa (ricorda: l'IA puo sbagliare).
3. Scrivi quale **versione** hai usato (Flash / Pro / ragionamento) e perche.

##### 4. Parte 3 — NotebookLM con un PDF

###### 4.1 Esercitazione
1. Nel browser entra su questo indirizzo con l'account della scuola:

```
notebooklm.google.com
```

2. Clicca `Crea nuovo`, poi `Carica`, e scegli il **PDF** indicato dal docente (per esempio la dispensa di teoria in PDF).
3. Aspetta che la fonte compaia a sinistra: e pronta.
4. Nel riquadro della chat scrivi:

```
Fammi un riassunto semplice di questo documento.
```

5. Poi chiedi:

```
Fammi 3 domande a risposta multipla su questo documento.
```

###### 4.2 Cosa consegni della Parte 3
1. Uno **screenshot** del riassunto e delle domande generate.
2. Con parole tue: qual e la **differenza** che hai notato tra chiedere a **Gemini** e chiedere a **NotebookLM**?

##### 5. Domanda finale (fa la differenza)
1. In tre righe, spiega il **flusso completo**: dove sta il materiale, cosa dai a Gemini, cosa carichi su NotebookLM, dove consegni. Usa parole tue.

##### 6. Come sarai valutato (per sapere cosa conta)
1. **Parte 1 — Git/GitHub (30%)**: risposte corrette a parole tue e screenshot della storia dei commit.
2. **Parte 2 — Gemini con .md (25%)**: esercitazione svolta, screenshot, e hai indicato la versione usata.
3. **Parte 3 — NotebookLM con PDF (25%)**: esercitazione svolta, screenshot, e hai colto la differenza con Gemini.
4. **Domanda finale + parole tue (20%)**: sai spiegare il flusso completo con parole tue (la prova del nove).

> [GIALLO] Conta piu il "saperlo spiegare a parole tue" che il copia-incolla: se sai raccontare cosa hai fatto, hai imparato davvero.


### L03 06/10/2026 — Il progetto individuale e il modello ISO/OSI

*Libro parziale: lezioni/2026-10-06_progetto-iso-osi.md*

#### Che cosa abbiamo fatto

1. **Quando:** 06/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Progetto individuale (idea di gioco o applicazione, prima versione); modello ISO/OSI con quiz.

#### La teoria e l'esercitazione

**Perché ci serve:** ogni messaggio che parte dal tuo PC attraversa **7 livelli**. Se sai a quale livello sta un problema, sai **dove cercare il guasto**: è il lavoro del tecnico di rete ed è la base dell'esame con **Packet Tracer**.

##### 1. L'idea: come spedire un pacco

Tu scrivi il biglietto, lo metti in una scatola, il negozio scrive l'indirizzo, il corriere sceglie la strada, il furgone lo porta. Ognuno fa **un solo lavoro** e si fida di quello sotto. Una rete funziona allo stesso modo: **7 livelli**, ognuno con il suo compito.

##### 2. La tabella dei 7 livelli

| Livello | Cosa fa | Esempi |
| 
7 Applicazione
 | i programmi che usi: dove nasce il messaggio | HTTP, HTTPS, DNS, SMTP |
| 
6 Presentazione
 | traduce in un formato comune, cifra e comprime | TLS (lucchetto), JPEG, ASCII |
| 
5 Sessione
 | apre, tiene aperta e chiude la conversazione | sessioni, login |
| 
4 Trasporto
 | spezza in pezzi, numera, controlla che arrivino tutti | TCP, UDP, porte (80, 443) |
| 
3 Rete
 | indirizzo IP e scelta della strada tra reti | IP, ICMP (ping) |
| 
2 Collegamento dati
 | indirizzo MAC, consegna nella rete locale | Ethernet, Wi-Fi (MAC) |
| 
1 Fisico
 | i bit come segnali: corrente, luce, onde radio | RJ45, fibra, Wi-Fi |

##### 3. Come ricordarli

1. Dal basso (1) all'alto (7): **F**isico, **C**ollegamento, **R**ete, **T**rasporto, **S**essione, **P**resentazione, **A**pplicazione.
1. Frase per ricordare le iniziali F-C-R-T-S-P-A: **«Fiori Colorati Rendono Tutti Sereni, Perfino gli Arrabbiati»**.
1. In inglese (Physical, Data link, Network, Transport, Session, Presentation, Application): «Please Do Not Throw Sausage Pizza Away».

##### 4. Guarda il viaggio

Apri la pagina interattiva **Il viaggio di un pacchetto** (è nella pagina della classe): fai scendere il messaggio dal 7 all'1 e guardalo risalire dall'altra parte.

**Carta e penna:** disegna la pila dei 7 livelli, dal 7 in alto all'1 in basso, ognuno con il suo colore. Ti serve per l'Esercitazione 1.

##### 1. L'incapsulamento: le buste

Chi spedisce, scendendo dal 7 all'1, **aggiunge** a ogni livello un'intestazione (una busta). Chi riceve, salendo dall'1 al 7, le **toglie** nell'ordine inverso.

MAC

IP

TCP

Ciao prof!

coda MAC

Il frame che viaggia sul cavo: il messaggio dentro tre buste

##### 2. Come si chiama il pezzo di dati (PDU)

| Livello | Nome del pezzo (PDU) |
| 7 · 6 · 5 | dati |
| 4 Trasporto | segmento |
| 3 Rete | pacchetto |
| 2 Collegamento | frame (trama) |
| 1 Fisico | bit |

**PDU** = Protocol Data Unit, unità di dati del protocollo: il nome del pezzo di dati a quel livello.

##### 3. Due indirizzi diversi: MAC e IP

|  | Indirizzo MAC (livello 2) | Indirizzo IP (livello 3) |
| Cos'è | il «nome e cognome» della scheda di rete, scritto in fabbrica | l'«indirizzo di casa», dato dalla rete in cui sei |
| Esempio | `3C:52:82:1A:7F:09` | `192.168.1.23` |
| Dove vale | solo dentro la rete locale | anche tra reti diverse, fino a Internet |
| Chi lo usa | lo switch | il router |

##### 4. I dispositivi e il loro livello

| Dispositivo | Livello | Cosa fa |
| cavo, antenna, hub | 1 | trasporta i bit; l'hub ripete tutto a tutte le porte |
| scheda di rete | 1-2 | trasforma i dati in segnali; ha il MAC |
| switch, access point Wi-Fi | 2 | consegna il frame solo al dispositivo giusto, usando il MAC |
| router | 3 | collega reti diverse e sceglie la strada, usando l'IP |
| firewall | 3-4 e oltre | decide cosa può passare (indirizzi, porte) |

Il «modem» di casa di solito è **più dispositivi in uno**: router + switch + access point Wi-Fi.

##### 5. Trasporto: TCP o UDP

| TCP | UDP |
| come una **raccomandata con ricevuta**: controlla che arrivi tutto, in ordine | come una **cartolina**: veloce, ma se un pezzo si perde va avanti |
| download, siti web, email | videochiamate, giochi online, dirette |

Le **porte** dicono a quale programma va il segmento: 80 = web (HTTP), 443 = web sicuro (HTTPS), 53 = DNS.

**Carta e penna:** disegna le buste di un messaggio (MAC · IP · TCP · dati · coda) e scrivi sotto ogni busta il suo livello.

##### 1. ISO/OSI e TCP/IP

ISO/OSI è il modello per **ragionare**; Internet usa il modello **TCP/IP**, che ha 4 livelli e raggruppa quelli OSI così:

| TCP/IP (4 livelli) | Livelli ISO/OSI |
| Applicazione | 7 · 6 · 5 |
| Trasporto | 4 |
| Internet | 3 |
| Accesso alla rete | 2 · 1 |

##### 2. Il metodo: dal basso verso l'alto

Quando «Internet non va», il tecnico controlla **prima i livelli bassi**: se il cavo è staccato, è inutile cercare il problema nel browser.

| Livello | Cosa controllo | Come |
| 1 Fisico | cavo collegato, lucine accese, Wi-Fi attivo | guardo e tocco: lucina della scheda di rete, icona della rete |
| 2 Collegamento | switch o access point acceso, porta funzionante | cambio porta o cavo; mi ricollego al Wi-Fi |
| 3 Rete | il PC ha un IP giusto? il router risponde? | `ipconfig`: se l'IP inizia con 169.254 non l'ha ricevuto; `ping` al router |
| 4-7 | il servizio e il nome del sito funzionano? | `ping 8.8.8.8` va ma il sito no → problema di DNS |

**ipconfig** mostra l'indirizzo IP del PC; **ping** manda un piccolo messaggio e aspetta la risposta (protocollo ICMP, livello 3). **DNS** traduce il nome del sito (www.google.it) in un indirizzo IP.

##### 3. Tre casi svolti

| Sintomo | Livello | Cosa faccio |
| L'icona della rete ha una X: «cavo di rete scollegato» | 1 | ricollego il cavo o lo cambio |
| `ipconfig` mostra 169.254.10.5 | 3 | il PC non ha ricevuto l'IP dal router: riavvio la scheda di rete, controllo il router |
| `ping 8.8.8.8` risponde ma www.google.it non si apre | 7 (DNS) | il collegamento c'è, manca la traduzione dei nomi: controllo il DNS |

**Carta e penna:** scrivi i 4 controlli in ordine, dal livello 1 in su. È la scaletta che userai anche in Packet Tracer.

### L04 13/10/2026 — I progetti di stage su GitHub

*Libro parziale: lezioni/2026-10-13_progetti-stage.md*

#### Che cosa abbiamo fatto

1. **Quando:** 13/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Avvio dei progetti di stage individuali su GitHub (per esempio un automa meteo in Python, un router-firewall virtuale): prima capire, poi scrivere il codice.

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Che cos'è un automa

<div class="scheda">Un <b>automa</b> è un programma che fa da solo un lavoro che si ripete: legge un dato, lo salva, lo mostra, poi aspetta e ricomincia. I sistemi di controllo delle fabbriche e dei laboratori (come <b>EPICS</b>) sono fatti così, in grande: <b>sorgente dei dati → automa → storico → pannello di controllo</b>. Il tuo progetto ha gli stessi quattro blocchi.</div>

##### 2. API REST e JSON

<div class="scheda">Una <b>API REST</b> è un indirizzo web che invece di una pagina restituisce <b>dati</b>. Open-Meteo risponde in <b>JSON</b>: testo con parentesi graffe, fatto di coppie <i>nome: valore</i>, una dentro l'altra come cassetti in un armadio. In Python <code>json.loads()</code> trasforma quel testo in un dizionario, e <code>dati["current_weather"]["temperature"]</code> apre il cassetto «current_weather» e prende «temperature».</div>

##### 3. Funzioni, return e None

<div class="scheda">Una <b>funzione</b> (<code>def</code>) è un pezzo di programma con un nome, che si richiama quando serve. Con <code>return</code> restituisce un risultato a chi l'ha chiamata. I <b>parametri</b>, tra le parentesi, sono i dati che riceve: <code>vento=None</code> vuol dire «se non me lo dai, vale None». <b>None</b> vuol dire «niente»: lo si usa quando un dato manca, per esempio se Internet non risponde (<code>try</code> / <code>except</code>).</div>

##### 4. Lo storico: file CSV

<div class="scheda">Un <b>CSV</b> è un file di testo a tabella: una riga per lettura, le colonne separate da <code>;</code>. Si apre con Excel. Aprendo il file in modalità <code>"a"</code> (append) si aggiunge in fondo senza cancellare. In Excel italiano i decimali vogliono la <b>virgola</b>: con il punto, 18.9 diventa testo e non si può fare la media.</div>

##### 5. Il ciclo e il tempo

<div class="scheda"><code>while True:</code> ripete per sempre; <code>time.sleep(60)</code> aspetta 60 secondi. Il computer che esegue il programma può avere un altro fuso orario: con <code>ZoneInfo("Europe/Rome")</code> si usa l'ora italiana.</div>

##### 6. La dashboard: Python scrive una pagina web

<div class="scheda">Una pagina web è solo testo HTML. Python la costruisce con una <b>f-string</b> (<code>f"...{temperatura}..."</code>), che mette i valori al posto giusto, e la scrive in <code>index.html</code>. <code>&lt;meta charset="utf-8"&gt;</code> serve perché simboli come «°» si vedano bene.</div>

##### 7. GitHub Actions e Pages

<div class="scheda"><b>GitHub Actions</b> esegue il tuo programma da solo, agli orari scritti nel file <code>.github/workflows/automa.yml</code> (ogni 30 minuti), anche a computer spento, e salva i risultati con un commit. <b>GitHub Pages</b> pubblica la cartella <code>docs</code> come sito: la dashboard si apre anche dal telefono.</div>

##### 8. LA PRATICA: costruisci il tuo automa

<div class="scheda">La pratica è il <b>percorso a tappe</b> nel tuo deposito: scrivi l'automa da zero, nella cartella <code>mio-automa/</code>, un pezzo alla volta, con gli aiuti a livelli e senza codice da copiare. Ogni tappa: funziona + commit + la sai spiegare nella chat del progetto.<br><a href="https://github.com/chasedeleon/automa-meteo-python/blob/main/documenti/PERCORSO.md" target="_blank"><b>Apri il percorso a tappe</b></a> · <a href="https://colab.research.google.com" target="_blank">Apri Google Colab</a> · <a href="https://github.com/chasedeleon/automa-meteo-python/pulls" target="_blank">La chat del progetto</a></div>


### L05 20/10/2026 — Ripasso ISO/OSI e verifica

*Libro parziale: lezioni/2026-10-20_iso-osi-ripasso.md*

#### Che cosa abbiamo fatto

1. **Quando:** 20/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Ripasso del modello ISO/OSI (i 7 livelli, l'incapsulamento, i dispositivi), verifica e descrizione del progetto; quiz su Moduli.

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. I sette livelli: come spedire un pacco

<div class="scheda">Quando mandi un messaggio, non lo fa un solo programma: lo fanno <b>sette livelli</b>, uno sopra l'altro, come in una ditta di spedizioni. Ognuno fa il suo lavoro e passa il pacco al livello sotto.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">N.</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa fa</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Esempio</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Applicazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il programma che usi</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">browser, WhatsApp, e-mail</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">6</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Presentazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">traduce, comprime, cifra</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">JPG, MP3, HTTPS</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">5</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Sessione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">apre e chiude la conversazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">login, videochiamata</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Trasporto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">divide in pezzi e controlla che arrivino</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TCP, UDP, porte</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sceglie la strada tra reti diverse</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">indirizzo IP, router</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">consegna dentro la stessa rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">indirizzo MAC, switch</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Fisico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">manda i bit sul mezzo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cavo, Wi-Fi, fibra</td></tr></table></div>

##### 2. Come ricordarli

<div class="scheda">Dal basso verso l'alto: <b>F</b>isico, <b>C</b>ollegamento, <b>R</b>ete, <b>T</b>rasporto, <b>S</b>essione, <b>P</b>resentazione, <b>A</b>pplicazione.<br><br>Una frase per ricordare le iniziali F-C-R-T-S-P-A: <b>«Fate Come Ragazzi Tranquilli: Studiate Prima, Applicatevi»</b>.<br><br>Due regole d'oro:<br>1. <b>In basso</b> ci sono le cose che tocchi (cavi, schede, switch); <b>in alto</b> i programmi che usi.<br>2. Chi spedisce scende dal 7 all'1; chi riceve sale dall'1 al 7.</div>

##### 3. L'incapsulamento: le buste

<div class="scheda">Scendendo, ogni livello mette i dati dentro una <b>busta</b> e ci scrive sopra le sue informazioni (l'<b>intestazione</b>). Chi riceve apre le buste al contrario.<br><br>Il pezzo di dati cambia nome a ogni livello (si chiama <b>PDU</b>):<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nome del pezzo</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7, 6, 5</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dati</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4 Trasporto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">segmento</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 Rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">pacchetto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">frame (trama)</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1 Fisico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">bit</td></tr></table>Per ricordarlo: <b>D-S-P-F-B</b>, «Dati Spediti Per Fare Bene».</div>

##### 4. Due indirizzi: MAC e IP

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"></th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">MAC</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">IP</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 Rete</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cos'è</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il «numero di telaio» della scheda di rete, scritto in fabbrica</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'«indirizzo di casa», dato dalla rete in cui sei</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cambia?</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">no, resta sempre lo stesso</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì, se cambi rete cambia</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Esempio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3C-52-82-1A-7F-09</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">192.168.1.25</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Chi lo usa</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">lo switch</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il router</td></tr></table>Il MAC serve per l'ultimo tratto, dentro la stessa rete. L'IP serve per trovare la strada da una rete all'altra.</div>

##### 5. I dispositivi e il loro livello

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Dispositivo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa guarda</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cavo, hub, ripetitore</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">solo i bit, non capisce niente</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">switch, access point</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo MAC: manda il frame solo al PC giusto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">router</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo IP: sceglie la strada tra reti diverse</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">firewall</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3-4 (e oltre)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">IP e porte: decide chi passa e chi no</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">PC, server</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">da 1 a 7</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">tutti i livelli</td></tr></table>Trucco: più il dispositivo «capisce», più sta in alto.</div>

##### 6. Trasporto: TCP o UDP

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"></th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TCP</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">UDP</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come lavora</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">controlla che tutto arrivi, in ordine; se manca un pezzo lo rimanda</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">manda e basta, senza controllare</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Pregio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">affidabile</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">veloce</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Si usa per</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">pagine web, e-mail, file</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">videochiamate, giochi online, dirette</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Paragone</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">raccomandata con ricevuta</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">volantino nella cassetta</td></tr></table>La <b>porta</b> dice a quale programma va il segmento: 80 e 443 sito web, 53 DNS, 25 e-mail.</div>

##### 7. Il metodo del tecnico: dal basso verso l'alto

<div class="scheda">Quando «Internet non va», il tecnico controlla i livelli <b>dal basso</b>, uno alla volta:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa controllo</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1 Fisico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cavo collegato, lucine accese, Wi-Fi attivo</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">switch o access point acceso, porta che funziona</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 Rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il PC ha un IP giusto? se comincia con 169.254 non l'ha ricevuto; il router risponde?</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4-7</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il servizio funziona? se l'IP 8.8.8.8 risponde ma il sito no, è il DNS</td></tr></table>È il metodo che userai in stage: prima i cavi, poi i programmi.</div>

##### 8. Il mio progetto: perché scrivere la descrizione

<div class="scheda">Ognuno di voi ha un progetto di stage (un gioco, un programma, una rete). In un'azienda vera, prima di scrivere codice si scrive <b>la descrizione</b>: due minuti di lettura che spiegano a chiunque che cosa farai.<br><br>Serve a tre cose:<br>1. a <b>te</b>, per avere chiaro dove vai;<br>2. al <b>prof</b> e al <b>tutor dello stage</b>, per aiutarti;<br>3. a <b>un'azienda</b>, che la legge come un biglietto da visita.<br><br>Regola d'oro: la <b>prima versione (v0.1)</b> è la cosa più piccola che funziona. Meglio piccola e finita che grande e a metà.</div>

##### 9. Com'è fatta una descrizione (il README)

<div class="scheda">Su GitHub la descrizione sta nel file <b>README.md</b>, la prima pagina del repository. Oggi la scrivi qui nella verifica; poi diventa il README del tuo progetto. Lo schema:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap"># Nome del mio progetto  ## Che cosa fa Due o tre frasi: che cosa fa il mio programma, gioco o rete.  ## Per chi è Chi lo usa: un'azienda, un giocatore, un tecnico, la mia classe.  ## Come si usa I passi di chi lo usa: apro, clicco, scrivo, vedo.  ## Con che cosa lo faccio Godot, Lazarus, Python, Packet Tracer, GitHub…  ## La prima versione (v0.1) La cosa più piccola che funziona e che posso mostrare.  ## Le versioni dopo v0.2: …  v0.3: …  ## Chi sono Nome (o soprannome), classe 4ª, indirizzo informatico.</pre>Scrivila con parole tue: non serve che sia lunga, serve che sia vera e chiara.</div>

##### 10. Il ponte verso la prossima lezione: l'indirizzo IP

<div class="scheda">Al livello 3 c'è l'<b>indirizzo IP</b>. La prossima volta impariamo a leggerlo davvero: indirizzo, maschera, gateway e DNS.<br><br>Prova già adesso, senza riga di comando: <b>Impostazioni → Rete e Internet → Ethernet</b> (o Wi-Fi) <b>→ Proprietà</b>. Cerca la riga «Indirizzo IPv4»: è il numero del tuo PC nella rete della scuola.</div>


### L06 27/10/2026 — LAN, Internet, protocolli e dispositivi

*Libro parziale: lezioni/2026-10-27_reti-dispositivi.md*

#### Che cosa abbiamo fatto

1. **Quando:** 27/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** LAN e Internet, i protocolli, i dispositivi della rete; schede di teoria, ripasso e quiz su Moduli; poi il progetto dell'anno.

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Ripasso: i 7 livelli in una pagina

<div class="scheda">Lo hai già studiato: un messaggio viaggia attraverso <b>sette livelli</b>, come un pacco in una ditta di spedizioni. Chi spedisce scende dal 7 all'1, chi riceve sale dall'1 al 7. Ogni livello mette una <b>busta</b> (incapsulamento).<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">N.</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Parola chiave</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Chi ci lavora</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Applicazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il programma</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">browser, HTTP, DNS</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Trasporto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">pezzi e porte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TCP, UDP</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">indirizzo IP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">router</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">indirizzo MAC</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">switch, access point</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Fisico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">i bit</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cavo, onde del Wi-Fi</td></tr></table>Oggi usiamo questa tabella come una <b>mappa</b>: per ogni dispositivo nuovo ci chiediamo «a che livello lavora?».</div>

##### 2. La rete di casa, la rete della scuola, Internet

<div class="scheda">Una <b>rete</b> è un gruppo di dispositivi collegati che si parlano. Ce ne sono di grandezze diverse, come le strade:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nome</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cos'è</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Paragone</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">LAN (rete locale)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">i dispositivi di una casa, di un'aula, di un ufficio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">le strade dentro il tuo quartiere</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">WAN (rete geografica)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">collega reti lontane: città, sedi di un'azienda</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'autostrada tra due città</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Internet</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la rete di tutte le reti del mondo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">tutte le strade del mondo insieme</td></tr></table><b>A casa:</b> telefono, PC e TV sono una piccola LAN; il modem-router la collega a Internet.<br><b>A scuola:</b> i PC del laboratorio sono una LAN più grande, con molti switch e access point; un router la collega a Internet.</div>

##### 3. I protocolli: le lingue comuni

<div class="scheda">Un <b>protocollo</b> è un insieme di regole per parlarsi, come una lingua comune. Se due dispositivi usano lo stesso protocollo, si capiscono, anche se sono di marche diverse.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Protocollo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">A che cosa serve</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nella vita reale</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">IP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dà un indirizzo e trova la strada</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 Rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo sulla busta</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TCP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">consegna sicura, in ordine</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4 Trasporto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la raccomandata con ricevuta</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">UDP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">consegna veloce, senza controllo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4 Trasporto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il volantino nella cassetta</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HTTP / HTTPS</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">apre le pagine web (HTTPS è cifrato, col lucchetto)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7 Applicazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">chiedere un libro in biblioteca</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DNS</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">traduce il nome (google.it) in indirizzo IP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7 Applicazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la rubrica del telefono</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DHCP</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dà in automatico l'IP a chi entra nella rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">7 Applicazione</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la reception dell'hotel che ti dà la stanza</td></tr></table></div>

##### 4. Lo switch (e il vecchio hub)

<div class="scheda">Lo <b>switch</b> è la «ciabatta» della rete: ha tante prese (porte) dove infili i cavi dei PC. Lavora al <b>livello 2</b> e guarda l'<b>indirizzo MAC</b>.<br><br>Lo switch impara chi è collegato a ogni porta e lo scrive nella sua <b>tabella degli indirizzi MAC</b>:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Porta</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Indirizzo MAC che ha visto</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3C-52-82-1A-7F-09 (PC del prof)</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">A4-BB-6D-10-22-3E (PC 2)</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">F0-1F-AF-55-90-0C (stampante)</td></tr></table>Così manda ogni frame <b>solo</b> al PC giusto.<br><br>L'<b>hub</b> (livello 1) invece non capisce gli indirizzi: ripete tutto a tutti.<br><b>Paragone:</b> l'hub è chi grida in corridoio; lo switch è il postino che porta la lettera alla porta giusta.</div>

##### 5. Il router: la porta verso le altre reti

<div class="scheda">Il <b>router</b> lavora al <b>livello 3</b> e guarda l'<b>indirizzo IP</b>. Collega reti diverse e sceglie la strada, come un navigatore.<br><br>Il <b>gateway predefinito</b> è l'indirizzo del router della tua rete: è la «porta d'uscita». Quando il PC deve parlare con qualcuno fuori dalla LAN, manda il pacchetto lì.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"></th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Switch</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Router</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Livello</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 Collegamento</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 Rete</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Guarda</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo MAC</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo IP</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Lavora</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dentro la stessa rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">tra reti diverse</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Paragone</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il postino del condominio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'ufficio postale che smista tra città</td></tr></table><b>NAT in parole semplici:</b> a casa tutti i dispositivi hanno un IP privato (192.168…). Verso Internet il router li fa uscire tutti con <b>un solo</b> IP pubblico, e poi ricorda a chi riportare le risposte. Come il centralino di un'azienda: un solo numero fuori, tanti interni dentro.</div>

##### 6. L'access point e il Wi-Fi

<div class="scheda">L'<b>access point</b> (punto di accesso) collega i dispositivi senza fili alla rete con il cavo. È come uno switch, ma via radio: lavora ai livelli <b>1 e 2</b>.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Parola</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa vuol dire</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">SSID</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il nome della rete Wi-Fi che vedi sul telefono</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Password WPA2 / WPA3</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la chiave che cifra il Wi-Fi; WPA3 è la più nuova e sicura</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2,4 GHz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">arriva più lontano e passa meglio i muri, ma è più lento</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">5 GHz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">più veloce, ma arriva meno lontano</td></tr></table><b>Access point o router di casa?</b> Il «router» di casa è in realtà <b>tante scatole in una</b>: router + switch + access point + modem (+ firewall). A scuola invece sono apparecchi separati: tanti access point sui soffitti, collegati a switch, e un router solo.</div>

##### 7. Il firewall: il buttafuori della rete

<div class="scheda">Il <b>firewall</b> controlla tutto quello che entra ed esce e decide chi passa, seguendo delle <b>regole</b>. È come il buttafuori di una discoteca con la lista.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Regola (esempio)</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa succede</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">porta 443 (HTTPS): aperta</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">i siti web sicuri funzionano</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">porta 80 (HTTP): aperta</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">i siti web normali funzionano</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">porte dei giochi online: chiuse</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a scuola il gioco non si collega</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">siti di scommesse o violenti: bloccati</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il browser mostra «pagina bloccata»</td></tr></table>Una <b>porta</b> è come il numero dell'interno di un ufficio: dice a quale programma va il messaggio. <b>Aperta</b> = si può entrare; <b>chiusa</b> = non si passa.<br>La scuola usa un firewall per proteggere i PC dai virus e per bloccare certi siti: non è un dispetto, è sicurezza.</div>

##### 8. Leggere la configurazione del tuo PC: ipconfig

<div class="scheda">Ora guardi i numeri veri del tuo PC. <b>Non servono diritti di amministratore.</b><br>1. Premi il tasto <b>Windows</b> sulla tastiera.<br>2. Scrivi <b>cmd</b> e premi <b>Invio</b>: si apre una finestra nera (il Prompt dei comandi).<br>3. Scrivi <b>ipconfig</b> e premi <b>Invio</b>.<br>4. Cerca il blocco della tua scheda (Ethernet se hai il cavo, Wi-Fi se sei senza fili). Vedi qualcosa così:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap">Scheda Ethernet Ethernet:     Indirizzo IPv4. . . . . . . . . : 192.168.10.37    Subnet mask . . . . . . . . . . : 255.255.255.0    Gateway predefinito . . . . . . : 192.168.10.1</pre><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Riga</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa vuol dire</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Indirizzo IPv4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il numero del tuo PC nella rete (l'indirizzo di casa)</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Subnet mask (maschera)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dice quanto è grande il «quartiere»: chi è nella tua stessa rete</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Gateway predefinito</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'indirizzo del router, la porta d'uscita</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Server DNS</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">chi traduce i nomi in IP; lo vedi con <b>ipconfig /all</b></td></tr></table>Se l'IP comincia con <b>169.254</b>, il PC non ha ricevuto l'indirizzo dal DHCP: guarda il cavo e chiedi all'assistente.</div>

##### 9. Che cosa faremo quest'anno

<div class="scheda">Questa è la strada del laboratorio di quest'anno. Sono competenze che chiedono davvero le aziende:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Tappa</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa fai</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa sai fare alla fine</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1. Cablaggio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">prepari un cavo di rete e lo provi</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">collegare una postazione</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2. Packet Tracer</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">costruisci una rete al computer, con PC, switch e router</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">progettare una rete senza comprare niente</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3. Configurare</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dai gli indirizzi, configuri switch, router e access point</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">far parlare due reti</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4. Sicurezza</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">password Wi-Fi, regole del firewall, aggiornamenti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">proteggere una piccola rete</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">5. Progetto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il tuo progetto, che mostri alla classe e allo stage</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un lavoro da mettere nel curriculum</td></tr></table>Packet Tracer è un programma gratuito che simula la rete: puoi sbagliare quanto vuoi, non si rompe niente.</div>

##### 10. Il mio progetto: definirlo bene

<div class="scheda">Il 20/10 hai scritto la prima descrizione del tuo progetto. Oggi la <b>aggiorni</b> con quello che hai imparato sulle reti. In un'azienda vera la descrizione sta nel file <b>README.md</b>, la prima pagina del repository. Lo schema:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.45;white-space:pre-wrap"># Nome del mio progetto  ## Che cosa fa Due o tre frasi: che cosa fa il mio programma, gioco o rete.  ## Per chi è Chi lo usa: un'azienda, un giocatore, un tecnico, la mia classe.  ## Come si usa I passi di chi lo usa: apro, clicco, scrivo, vedo.  ## Con che cosa lo faccio Godot, Lazarus, Python, Packet Tracer, GitHub…  ## Che cosa c'entra la rete Quali dispositivi o protocolli usa (o potrebbe usare): switch, router, Wi-Fi, HTTP, DNS…  ## La prima versione (v0.1) La cosa più piccola che funziona e che posso mostrare.  ## Le versioni dopo v0.2: …  v0.3: …  ## Chi sono Nome (o soprannome), classe 4ª, indirizzo informatico.</pre>Regola d'oro: la <b>prima versione (v0.1)</b> è la cosa più piccola che funziona. Meglio piccola e finita che grande e a metà.<br>Il nuovo punto «Che cosa c'entra la rete» ti aiuta a collegare il tuo progetto a quello che faremo quest'anno.</div>

<!-- LEZIONI:FINE -->

## 2 Changelog
1. **v1.0 (29/10/2026)**: prima versione completa: le 6 lezioni dal 22/09 al 27/10, ognuna con la teoria e l'esercitazione.
