# Libro di testo — Informatica Classe 1

**Versione 1.3** — 30/10/2026
*Il libro di testo della Classe 1: raccoglie in un unico posto gli appunti, la
teoria e le esercitazioni svolte in classe. Cresce a ogni lezione. Due formati:
il PDF (`libro-classe1-vX.Y.pdf`) per leggere e stampare; questo MD è la fonte
versionata, da dare ai ragazzi per la loro AI (NotebookLM/Gemini), così l'AI
spiega e traduce nella loro lingua. La forma segue le regole di formattazione del
corso; la lingua è l'italiano (l'AI fa da ponte per arabo e cinese).*

---

## 0. Come lavoriamo (leggere per prime)
1. Ogni lezione: **carta e penna sul banco** per appunti e schemi a mano.
2. Si lavora **un passo alla volta**, con un risultato concreto da vedere subito.
3. Consegne e materiali stanno su **Google Classroom**; i documenti si scrivono
   con **Google Documenti**.
4. **L'AI aiuta a capire, non a saltare il pensiero**: la prova che hai capito è
   **saperlo spiegare a voce** con parole tue.
5. Chi scrive meglio nella propria lingua può scrivere in **arabo/cinese** e poi
   tradurre in italiano con Google Traduttore.

## 1. Che cos'è l'informatica
1. L'informatica è la scienza che studia come **trattare le informazioni** con
   strumenti automatici: il computer riceve dati (input), li elabora e restituisce
   risultati (output).
2. Il computer da solo non "capisce": esegue **istruzioni** precise che gli diamo.
3. Impareremo a usare bene gli strumenti (computer, Google, Git) e, più avanti, a
   creare noi qualcosa (siti, giochi).

## 2. Il computer e le sue parti
1. **CPU (processore):** il "cervello", esegue tutti i calcoli.
2. **RAM (memoria):** memoria di lavoro, veloce ma **temporanea** (si svuota allo
   spegnimento).
3. **Hard Disk / SSD:** dove si salvano i file in modo **permanente** (restano
   anche da spento).
4. **Scheda madre:** la base che collega e fa comunicare tutti i pezzi.
5. **Scheda video (GPU):** disegna la grafica (immagini, video, giochi).
6. **Alimentatore:** porta la corrente a tutti i pezzi.
7. **Case:** la scatola che contiene e protegge tutto.

### 2.1 Come si assembla (dove va ogni pezzo)
1. La **scheda madre** si fissa alla parete di fondo del **case**.
2. La **CPU** va nello zoccolo (socket) al centro-alto della scheda madre; sopra
   il dissipatore con la ventola.
3. La **RAM** entra negli slot lunghi accanto alla CPU (fino al "clic").
4. La **scheda video** va nello slot PCIe, in basso sulla scheda madre.
5. L'**Hard Disk/SSD** nel vano del case, collegato con un cavo alla scheda madre.
6. L'**alimentatore** in basso nel case; dà corrente a tutti.

### 2.2 Scegliere i pezzi (compatibilità e budget)
1. Con il sito `it.pcpartpicker.com/list/` (modalità **Builder**) si sceglie un
   pezzo per ogni categoria.
2. Il sito **controlla la compatibilità** (avvisa in rosso se due pezzi non vanno
   insieme) e **somma il prezzo totale**.
3. Obiettivo: montare un PC che funzioni **entro un budget** (es. 700 €).

### 2.3 Standard e compatibilità (form factor, PCIe, socket, RAM)
1. **Standard** = misure e forme comuni, decise da tutti, perché i pezzi
   **combacino**. I quattro principali:
2. **Form factor (grandezza della scheda madre e del case):** `ATX` (305×244 mm),
   `microATX` (244×244), `Mini-ITX` (170×170); `AT` è il vecchio standard. Più
   grande = più slot.
3. **Slot PCIe (schede aggiuntive):** `x1, x4, x8, x16` (lunghezze crescenti); nel
   `x16` va la **scheda video**. Versioni `3.0/4.0/5.0` (velocità); `M.2` per gli
   SSD NVMe.
4. **Socket (dove si appoggia la CPU):** Intel = `LGA` (pin nel socket, es.
   `LGA1700`); AMD = `PGA` (pin sulla CPU, es. `AM4`) o `LGA` (`AM5`). CPU e
   scheda madre si comprano **in coppia**.
5. **Processori per marca:** Intel Core `i3/i5/i7/i9`; AMD Ryzen `3/5/7/9`.
6. **RAM (memorie):** `DDR3/DDR4/DDR5`, con la **tacca in posizione diversa** (non
   si scambiano); `DIMM` (desktop) vs `SO-DIMM` (portatili).
7. **Cosa deve combaciare:** case↔scheda madre (form factor), scheda madre↔CPU
   (socket), scheda madre↔RAM (generazione), scheda video↔slot `PCIe x16`.

> [GIALLO] È il "perché" dei controlli che fa PCPartPicker quando si monta il PC.
> Materiale: scheda `standard-hardware` (teoria trilingue con i disegni in scala).

### 2.4 Lo storage: i 5 livelli (dove si salvano i file)

![I 5 livelli dello storage digitale](immagini/20260924_Storage-5-Livelli.jpg)

1. **Livello 1 — Tecnologia:** l'**HDD** (meccanico) ha un piatto che gira e una
   testina che si muove; l'**SSD** (elettrico) usa **celle NAND Flash**, senza
   parti in movimento (più veloce e resistente).
2. **Livello 2 — Tipo e velocità:** HDD meccanico ~160 MB/s; **SSD SATA** (2,5")
   ~560 MB/s; **SSD NVMe** molto più veloce (Gen3 ~3.500, Gen4 ~7.500, Gen5
   ~12.000+ MB/s).
3. **Livello 3 — Logica di controllo (il "linguaggio"):** **AHCI** (vecchio):
   seriale, una sola coda, va bene per l'HDD; **NVMe** (moderno): in parallelo,
   fino a 65.535 code, perfetto per i chip dell'SSD.
4. **Livello 4 — Connettore fisico:** **SATA** (con cavo, robusto) oppure **M.2**
   (a incastro diretto sulla scheda madre, piccolo). Attenzione: **M.2 è solo una
   FORMA** del connettore (può essere SATA o NVMe).
5. **Livello 5 — Interfaccia (la "strada" sulla scheda madre):** il **bus SATA**
   è lento e passa da un controller; il **bus PCIe** è velocissimo ed è collegato
   direttamente alla **CPU** (le "corsie" x4).

> [GIALLO] Da ricordare, le tre cose diverse: **M.2** = la forma del connettore ·
> **NVMe/AHCI** = il linguaggio · **PCIe/SATA** = la strada. Il disco più veloce
> oggi è un **SSD NVMe su M.2 collegato via PCIe**.

#### 2.4.1 In parole semplici — la storia dello storage

1. Una volta c'erano solo gli **HDD**: dischi che **girano**, con una **testina**
   che legge e scrive, un po' come la puntina di un giradischi. Funzionano, ma
   sono **lenti** e delicati, perché hanno **parti in movimento**.
2. Poi sono arrivati gli **SSD**: **niente parti in movimento**, salvano tutto in
   **chip di memoria** (NAND Flash), come una chiavetta USB molto evoluta. Sono
   più **veloci**, silenziosi e resistenti agli urti.
3. Ma non tutti gli SSD sono uguali. Un **SSD SATA** usa la **vecchia strada**
   dell'hard disk: è veloce, ma ha un limite (~560 MB/s). Un **SSD NVMe** usa una
   **strada nuova e larghissima**, il **PCIe** (la stessa della scheda video e
   della CPU), e va **molto** più veloce.
4. Tre parole da **non confondere**:
   1. la **FORMA** — `M.2`, il "bastoncino" che si incastra sulla scheda madre;
   2. il **LINGUAGGIO** — `NVMe` o `AHCI`, cioè come il computer "parla" col disco;
   3. la **STRADA** — `PCIe` (autostrada) o `SATA` (strada normale), per dove
      passano i dati.
5. **In pratica:** per far "volare" un computer, la prima cosa da fare è mettere
   un **SSD** (meglio se **NVMe**): è il salto di velocità che si sente di più,
   più ancora che cambiare processore.

> [GIALLO] Immagine mentale: pensa a una **consegna di pacchi**. La **forma** è il
> tipo di furgone, il **linguaggio** è la lingua con cui parli al corriere, la
> **strada** è l'autostrada o la stradina di campagna. Per andare veloce servono
> tutte e tre giuste: furgone adatto (M.2), lingua moderna (NVMe), autostrada (PCIe).

## 3. Utenze e aree di lavoro
1. **Account e password:** ognuno ha il proprio account della scuola; la password
   va tenuta al sicuro e robusta (lunga, con lettere, numeri e simboli).
2. **Le aree:** cartella personale in rete + spazio su **Google Drive**; i file si
   organizzano in **cartelle e sottocartelle** (area logica).
3. **Chiudere bene il computer:** quando hai finito, blocca o disconnetti con
   `Ctrl + Alt + Canc`; non lasciare il PC aperto e incustodito.

## 4. Google Suite e Classroom
1. **Google Documenti:** il programma per scrivere i testi (si salva da solo).
2. **Consegnare un compito su Classroom:** aprire il corso → "Lavori del corso" →
   il compito → "Aggiungi o crea" → "Documenti Google" → scrivere → "Consegna".
3. **Il voto:** l'allievo vede il voto **solo dopo** che il docente clicca
   "Restituisci".

## 5. GitHub e i repository
1. **GitHub** è un sito dove i programmatori **salvano e condividono** il codice
   dei loro progetti e collaborano.
2. **Repository (repo):** la "cartella-progetto" digitale che contiene tutti i
   file **e la storia di ogni modifica** fatta nel tempo.
3. A cosa serve la storia delle modifiche: si può **tornare a una versione
   precedente** se qualcosa va storto, e si capisce chi ha cambiato cosa e quando.
4. **Git** è il sistema che tiene traccia delle modifiche; **GitHub** è il sito
   che ospita i progetti online.

### 5.1 La storia del nostro gioco: versioni, rami, fork e merge (09/10/2026)
1. **Versione (commit):** ogni salvataggio pubblicato del gioco. Nel grafo è un pallino: v0.3, v1.1, v2.0.
2. **Ramo (branch):** una linea del grafo; il gioco cresce lungo il ramo, da sinistra a destra.
3. **Fork (copia):** la 1INF ha copiato il «Treno blindato» della 2INF (versione v0.11) e lo fa crescere per conto suo (v1.0, v1.1).
4. **Pull Request (proposta di modifica):** il Documento consegnato su Classroom («il mio cattivo si chiama Hidra…»): il prof lo legge, lo accetta e lo mette nel gioco.
5. **Merge (unione):** un ramo di lavoro rientra nel ramo principale. Il prof ha provato le «immagini della classe» su un ramo a parte, per non rompere il gioco; quando funzionavano le ha unite al ramo della 1INF.
6. **I numeri delle versioni:**
   6.1 v0.x = le prove, prima della versione stabile;
   6.2 1.0 = la prima versione «vera» del ramo;
   6.3 1.1, 1.2 = versioni **minor**: piccole aggiunte (un cattivo, un cielo);
   6.4 2.0 = versione **major**: cambia una cosa grossa. Il nostro gioco è stato rifatto con **Godot** (motore per videogiochi): per questo è la v2.0 e non la v1.2.
7. **Ponte da Lazarus:** Lazarus **reagisce** (aspetta un clic), Godot **pulsa** (`_process` gira da solo circa 60 volte al secondo).
8. Lezione completa (in italiano, arabo e cinese) e grafo: `classe-1/lezione-versioni-treno/` e la pagina `docs/lezione-versioni/`.

### 5.2 La lavagna del 09/10/2026: numeri delle versioni, fork, Pull Request

![La lavagna del 09/10: versioning, changelog, fork, Pull Request accettata e rifiutata](immagini/20261009_lavagna-versioning.jpg)

1. **I numeri delle versioni** (in blu): 16.0.2.31 · 7.0.3 · 2.01. Il primo numero è la **major** (cambio grosso), il secondo la **minor** (aggiunte), il terzo la **patch** (piccole correzioni di errori), il quarto, se c'è, la **build** (numero di compilazione). Esempio: 16.0.2.31 = major 16, minor 0, patch 2, build 31.
2. **Il ramo principale** (in rosso): v0.8 → v0.9 → v1.0. Il cerchio grande è la v1.0, la prima versione stabile che si pubblica (**release**).
3. **Il changelog** (riquadro verde tra v0.9 e v1.0): la lista di tutto quello che è cambiato da una versione all'altra.
4. **Il fork** (in blu): dalla v0.9 qualcuno copia il progetto e lavora per conto suo.
5. **La Pull Request**: dal fork si propone la modifica al progetto principale; se va bene → **accept ✓** e **merge**, la modifica entra nel ramo rosso e nasce una versione nuova.
6. **Refuse ✗**: una proposta che non va bene non entra nel progetto, ma resta nella storia e si può correggere e riproporre.

## 6. Sicurezza e regole di laboratorio
1. **Password robuste** e mai condivise; attenzione a e-mail sospette (phishing).
2. **Regole "quando hai finito"**: niente giochi, niente YouTube, niente cose che
   fanno rumore; resti al tuo posto; blocca/esci col `Ctrl + Alt + Canc`.
3. **Se hai finito**: ripassa, fai lo schema a mano sul quaderno, aiuta un
   compagno, prova a spiegare a voce cosa hai capito.

### 6.1 Sicurezza 1: pericolo, danno, rischio (22/10)
1. **Pericolo:** una cosa che **può** fare male (il coltello, l'olio bollente, la presa rotta, il pavimento bagnato, il cavo per terra). Domanda magica: «Che cosa qui mi può fare male?».
2. **Danno:** il male che **succede davvero** (un taglio, una bruciatura, una caviglia storta, gli occhi stanchi dopo ore di schermo).
3. **Rischio:** quanto è **facile** che il danno succeda e quanto è **grave**. Lo stesso pericolo ha un rischio diverso a seconda di come lo usi: motorino con il casco allacciato (basso) o senza casco, veloce, con il telefono in mano (alto); telefono in carica sul tavolo (basso) o sotto il cuscino tutta la notte (alto).
4. **«Per un pelo» (quasi incidente):** non ti sei fatto niente, ma il pericolo c'era: lo dici subito, così il prossimo non si fa male.
5. La prossima volta: **prevenzione** (il danno succede meno spesso) e **protezione** (il danno è meno grave). Documento completo: `classe-1/sicurezza-1ora/1inf-sicurezza-1ora.md`.

## 7. Esercitazioni svolte
1. **Io e la mia famiglia** — presentazione di sé e della famiglia con Google
   Documenti, consegna su Classroom (anche scrivendo nella propria lingua +
   traduzione).
2. **Ricerca: cos'è GitHub e cos'è un repository** — piccola ricerca in rete,
   scritta in un documento e consegnata su Classroom.
3. **I componenti del PC** — per ogni componente spiegare a cosa serve con parole
   proprie + due domande personali.
4. **Costruisci il tuo PC** — montare un PC compatibile a budget con PCPartPicker
   (Builder) e scrivere la lista con il prezzo totale.
5. **Documento sulla configurazione del PC** — spiegare con parole proprie gli
   standard (form factor, PCIe, socket, processori per marca, memorie) e inserire
   immagini dal web descrivendo la tipologia; consegna su Classroom.

### 7.1 Quanto pesa un file e quanto va veloce la rete (20 e 21/10)

1. **Bit e byte:** il bit vale 0 oppure 1; 8 bit fanno 1 byte, cioè una lettera. Il bit si scrive con la **b** piccola, il byte con la **B** grande.
2. **Le unità:** ogni gradino è circa 1000 volte più grande: KB, MB, GB, TB. Una foto pesa circa 3 MB, un film circa 2 GB.
3. **Il conto:** prima si porta tutto nella stessa unità, poi si divide. Esempio: 64 GB = 64000 MB; 64000 : 3 = circa 21000 foto.
4. **La velocità della rete** si misura in **Mbps** (megabit al secondo): 100 Mbps = 12,5 MB al secondo.
5. **Il controllo dei dati (CRC):** chi spedisce aggiunge un numero di controllo, chi riceve rifà il conto; se non torna, un bit si è rovinato e il pacchetto si chiede di nuovo.
6. **Nel cavo i bit sono corrente:** 5 volt = 1, 0 volt = 0.

![La lavagna del 20/10: bit, byte, Mbps e il controllo dei dati](immagini/20261020_lavagna-bit-byte-crc_slide.jpg)

![La lavagna del 20/10: il byte diventa corrente nel cavo](immagini/20261020_lavagna-segnale-0V-5V_slide.jpg)

7. **Il laboratorio del gamer (21/10):** il **ping** è il tempo di andata e ritorno verso il server (sotto 30 ms ottimo); il **jitter** è quanto il ping cambia; il **lag** è il ritardo che si sente giocando. Gli **FPS** sono le immagini al secondo prodotte dalla scheda video; gli **Hz** sono quante volte al secondo il monitor ridisegna l'immagine. I cavi video: VGA (vecchio, analogico), HDMI (porta anche l'audio), DisplayPort (monitor da gaming). Documento completo: `classe-1/gamer/1inf-gamer.md`.

## 8. Lazarus: il mio primo programma (28/10)

*Programmazione · Informatica, laboratorio · 28/10/2026 · la prima finestra con una casella (TEdit) e un bottone (TButton): scrivi il nome, premi e compare «Ciao» con il tuo nome; i file del progetto; consegna su Classroom. Dispensa completa in tre lingue (italiano, arabo, cinese): `classe-1/lazarus-ciao/20261028_Classe-1_v1.0_Lazarus-Primo-Programma_IT.md` (e `_AR`, `_ZH`).*

### 8.1 Che cos'è Lazarus

**Lazarus** è un programma che serve a **creare altri programmi**, con le finestre e i bottoni, come quelli che usi ogni giorno. Funziona come i **mattoncini**: prendi un pezzo già pronto (un bottone, una casella), lo metti nella finestra e poi scrivi **che cosa deve fare**. Il linguaggio si chiama **Pascal**.

Oggi facciamo il primo programma di tutti i programmatori: il **«Ciao»**. Scrivi il tuo nome in una casella, premi un bottone e il programma ti saluta: **Ciao Ahmed**.

Per aprire Lazarus: doppio clic sull'icona di Lazarus (il prof vi mostra dove si trova). Poi vai al capitolo 02: lì prepari il progetto nuovo e la tua cartella.

### 8.2 Partenza pulita: nuovo progetto e cartella nuova

Prima di mettere i pezzi nella finestra prepariamo il posto giusto. **Un progetto = una cartella sola**: tutti i file del tuo programma stanno insieme, nella tua cartella. Così nessun file si perde e nessun file si mescola con quelli di un altro.

Fai un passo alla volta. Dopo ogni passo guarda lo schermo.

**1.** In alto a sinistra in Lazarus clicca il menu «File».

**2.** Nel menu clicca «Chiudi tutto». Così si chiudono i file rimasti aperti.

**3.** Se Lazarus chiede di salvare un progetto vecchio, clicca «No».

**4.** In alto clicca il menu «Progetto».

**5.** Nel menu clicca «Chiudi progetto». Se la voce è grigia, non si può cliccare: va bene così, vai al passo 6.

**6.** Ora fai il progetto nuovo. In alto clicca il menu «Progetto».

**7.** Nel menu clicca «Nuovo progetto…». Si apre una finestra con un elenco.

**8.** Nell'elenco a sinistra clicca «Applicazione».

**9.** In basso nella finestra clicca «OK». Al centro compare la finestra vuota **Form1**.

**10.** SUBITO si salva. In alto clicca il menu «Progetto».

**11.** Nel menu clicca «Salva progetto con nome…». Si apre la finestra per salvare.

**12.** In alto nella finestra clicca il bottone «Nuova cartella». (Non lo vedi? Clic con il tasto destro su un punto vuoto della finestra → «Nuovo» → «Cartella».)

**13.** Scrivi il nome della cartella e premi `Invio`:

```
ciao
```

**14.** Fai **doppio clic** sulla cartella `ciao` per entrarci. In alto ora c'è scritto `ciao`.

**15.** In basso, nella casella «Nome file», scrivi il nome del progetto:

```
ciao.lpi
```

**16.** In basso a destra clicca «Salva».

**17.** Lazarus apre una seconda finestra: chiede il nome della **unit** (il file del codice). Nella casella «Nome file» lascia o scrivi:

```
unit1.pas
```

**18.** In basso a destra clicca «Salva».

**19.** Controlla: guarda in alto, nella barra del titolo di Lazarus. C'è scritto `ciao`. FATTO: il tuo progetto ha la sua cartella!

### 8.3 Le finestre di Lazarus

Quando apri un progetto nuovo vedi più finestre. Ognuna ha un lavoro:

| Dove | Si chiama | A che cosa serve |
|---|---|---|
| in alto | **menu** e **palette dei componenti** | i comandi («File», «Progetto», «Esegui»…) e, sotto, i pezzi da mettere nella finestra, divisi in linguette |
| a sinistra | **Ispettore oggetti** | le **proprietà** del pezzo selezionato (il testo, il nome, il colore) e i suoi **eventi** (che cosa succede quando lo clicchi) |
| al centro | **Form1**, con i puntini | la **finestra del tuo programma**: qui metti i pezzi |
| dietro la Form | **Editor del codice** (unit1.pas) | qui scrivi **che cosa fa** il programma |
| in basso | **Messaggi** | Lazarus ti dice se è andato tutto bene o dove c'è un errore |

Per passare dalla Form al codice e ritorno: tasto `F12`.

**Da ricopiare sul quaderno**

```
+--------------------------------------------------+
| MENU:  File  Progetto  Esegui ...                |
| PALETTE: [Standard]  [OK] [abc] [A] ...          |
+------------+-------------------------------------+
| ISPETTORE  |                                     |
| OGGETTI    |   FORM1  (la mia finestra)          |
|            |    +-----------------+              |
| Proprieta  |    | Edit1           |  <- TEdit    |
|  Caption   |    +-----------------+              |
|  Text      |       [ Saluta ]       <- TButton   |
| Eventi     |                                     |
|  OnClick   |   (F12 = vado al codice)            |
+------------+-------------------------------------+
| MESSAGGI: errori e avvisi                        |
+--------------------------------------------------+
```

![Foto della lavagna: la lavagna del 28/10/2026: le finestre di Lazarus. In alto la palette con gli oggetti (i componenti); a sinistra l'Object Inspector (l'Ispettore oggetti) con le proprietà e i metodi (gli eventi); a destra la Form e, sotto, il codice.](immagini/20261028_lavagna-finestre-lazarus.jpg)

### 8.4 La palette: come scegliere il pezzo giusto

La **palette dei componenti** è la fila di icone in alto, sotto il menu. I pezzi di oggi sono nella linguetta «Standard». Per scegliere, chiediti: **che cosa deve fare chi usa il programma?**

| Deve… | Pezzo (componente) | Icona nella palette | Proprietà che conta |
|---|---|---|---|
| **scrivere** qualcosa | **TEdit** (casella di testo) | una casella bianca con «abc» o «ab\|» | `Text` = quello che c'è scritto dentro |
| **premere** per far succedere una cosa | **TButton** (bottone) | un bottone con «OK» | `Caption` = la scritta sul bottone |
| **leggere** un testo (solo guardare) | **TLabel** (etichetta) | una «A» | `Caption` = il testo che si vede |

Per metterlo nella finestra: **un clic** sull'icona nella palette, poi **un clic** sulla Form1, nel punto dove lo vuoi. Lazarus gli dà un nome da solo: `Edit1`, `Button1`. Il **nome** (`Name`) è quello che userai nel codice.

### 8.5 Esercitazione: il mio «Ciao»

Un passo alla volta. Dopo ogni passo guarda lo schermo: deve essere uguale.

**1.** Nella palette, linguetta «Standard», clicca **TEdit**, poi clicca nella Form1, in alto a sinistra. Compare una casella con scritto `Edit1`.

**2.** Con la casella selezionata, nell'Ispettore oggetti trova la proprietà `Text` e cancella la scritta «Edit1»: la casella resta vuota.

**3.** Nella palette clicca **TButton**, poi clicca nella Form1 sotto la casella. Compare `Button1`.

**4.** Con il bottone selezionato, nell'Ispettore oggetti cambia `Caption` in `Saluta`. FATTO: la finestra è pronta!

**5.** Fai **doppio clic sul bottone**. Si apre il codice, con il cursore qui:

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  // qui scrivi la tua riga
end;
```

**6.** Tra `begin` e `end;` scrivi questa riga:

```
ShowMessage('Ciao ' + Edit1.Text);
```

Che cosa vuol dire, pezzo per pezzo:

| Pezzo | Vuol dire |
|---|---|
| `ShowMessage( … )` | apre una **finestrella** con un messaggio e il bottone **OK**. Quello che c'è tra le parentesi è il messaggio |
| `Edit1.Text` | il testo scritto dentro la casella Edit1 (il nome) |
| `'Ciao '` | una scritta fissa. Va tra apici. Lo **spazio** dopo Ciao serve per non avere «CiaoAhmed» |
| `+` | attacca due scritte una dopo l'altra |
| `;` | fine dell'istruzione (come il punto alla fine di una frase) |

Tutto insieme: **«apri una finestrella con scritto Ciao e il nome che c'è nella casella»**. Come alla lavagna: scrivi MARIO, premi Saluta, compare **Ciao MARIO** con il bottone OK. È la funzione che risponde al **clic** del bottone: si chiama `Button1Click`.

**Da ricopiare sul quaderno**

```
scrivo MARIO -> clic su [Saluta] -> OnClick -> Button1Click
   -> ShowMessage('Ciao ' + Edit1.Text) -> | Ciao MARIO  [OK] |
```

![Foto della lavagna: la lavagna del 28/10/2026. In alto la finestra con la casella (MARIO) e il bottone Saluta; il clic apre la finestrella «Ciao MARIO» con il bottone OK. Sotto: 1) chiudere tutti i file; 2) creare la cartella e salvare tutti i file lì dentro.](immagini/20261028_lavagna-lazarus-ciao.jpg)

### 8.6 Salva e fai partire

La cartella `ciao` l'hai già fatta nel capitolo 02. Adesso basta poco.

1. Premi `Ctrl` + `S`: Lazarus salva tutto nella tua cartella.
2. Premi `F9` (oppure la freccia verde ▶ in alto). Lazarus prepara il programma e lo fa partire: si apre la TUA finestra.
3. Clicca nella casella e scrivi il tuo nome.
4. Clicca il bottone **Saluta**. Si apre una finestrella con **Ciao** e il tuo nome.
5. Clicca **OK**. Ce l'hai fatta: hai scritto il tuo primo programma!

> [GIALLO] **Errore? È normale, succede a tutti i programmatori.** Guarda la finestra «Messaggi» in basso: dice la riga. I più comuni: manca il `;`; hai scritto `=` invece di `:=`; manca un apice `'`; la riga è fuori da begin … end.

### 8.7 I file del progetto, uno per uno

Dopo `F9` apri la cartella `ciao` con Esplora file. Lazarus ha creato tanti file. L'**estensione** sono le lettere dopo il punto nel nome del file: dice **che tipo di file è**. Non vedi le estensioni? In Esplora file, in alto: «Visualizza» → «Mostra» → «Estensioni nomi file».

**Gruppo 1. Il progetto**

| File | Che cos'è | Che cosa c'è dentro | Si può cancellare? |
|---|---|---|---|
| `ciao.lpi` | informazioni del progetto (**L**azarus **P**roject **I**nformation)<br>*Come: la scheda del progetto, con l'elenco dei pezzi e le istruzioni per montarli* | un testo in formato **XML** (testo con le etichette tra < e >): quali file fanno parte del progetto e le **opzioni** del progetto e del compilatore, quelle che si cambiano dal menu «Progetto» → «Opzioni progetto…». Con doppio clic su questo file riapri il progetto | **NO** |
| `ciao.lpr` | programma principale (**L**azarus **PR**ogram)<br>*Come: il fischio di inizio della partita: fa partire tutto* | le poche righe in Pascal che fanno partire tutto e aprono Form1. Non si tocca | **NO** |
| `ciao.lps` | sessione (**L**azarus **P**roject **S**ession)<br>*Come: un segnalibro: la memoria di dove eri rimasto* | quali file erano aperti nell'editor, in che ordine erano le linguette, dov'era il cursore. **Non contiene il programma**: se la cancelli, il tuo lavoro c'è ancora tutto | sì: Lazarus la rifà |
| `ciao.res` | risorse (**RES**ource)<br>*Come: lo zaino con le cose da portare dentro l'exe: icona e versione* | l'icona e la versione del programma, pronte da mettere dentro l'exe | sì: Lazarus la rifà |
| `ciao.ico` | icona (**ICO**n)<br>*Come: la foto profilo del programma* | il disegnino del programma, quello che vedi sulla barra di Windows | sì: Lazarus la rifà |

**Gruppo 2. La finestra e il codice**

| File | Che cos'è | Che cosa c'è dentro | Si può cancellare? |
|---|---|---|---|
| `unit1.lfm` | la form (**L**azarus **F**or**M**)<br>*Come: la piantina di una stanza: dove stanno i mobili* | **com'è fatta la finestra**: quali pezzi ci sono, dove stanno, quanto sono grandi, Caption e Text | **NO** |
| `unit1.pas` | la unit (un file di codice in **Pas**cal)<br>*Come: la ricetta: le istruzioni che hai scritto tu* | il **TUO codice**: la procedura `Button1Click` con la riga del Ciao. Una unit può avere anche l'estensione `.pp` | **NO** |

**Gruppo 3. Il programma finito**

| File | Che cos'è | Che cosa c'è dentro | Si può cancellare? |
|---|---|---|---|
| `ciao.exe` | eseguibile (**EXE**cutable), nella cartella del progetto<br>*Come: la torta già cotta: si mangia anche senza la ricetta* | il **programma finito**, creato con F9. Si apre anche senza Lazarus | sì: si rifà con F9 |

**Gruppo 4. File di lavoro del compilatore** (il **compilatore** è il programma che trasforma il Pascal in un programma che il computer sa eseguire)

| File | Che cos'è | Che cosa c'è dentro | Si può cancellare? |
|---|---|---|---|
| `lib\x86_64-win64\` | cartella<br>*Come: il tavolo della cucina dove si preparano i pezzi* | i pezzi intermedi che servono per fare l'exe (qui sotto) | sì: Lazarus la rifà |
| `.o` | file oggetto (**O**bject)<br>*Come: un ingrediente già cotto, uno solo* | il codice macchina di **una sola** unit, per esempio `unit1.o` | sì |
| `.ppu` | unit compilata di Free Pascal (**P**ascal **P**recompiled **U**nit)<br>*Come: un pezzo già montato, con l'etichetta che dice che cosa sa fare* | le informazioni sulla unit già tradotta, per esempio `unit1.ppu` | sì |
| `.compiled` | promemoria della compilazione<br>*Come: lo scontrino: ricorda com'è andata l'ultima volta* | come è stato compilato il progetto l'ultima volta: così Lazarus sa se deve rifare tutto | sì |
| `.or` | risorse compilate<br>*Come: lo zaino del .res già chiuso, pronto da caricare* | il file `.res` già pronto da attaccare all'exe | sì |
| `backup\` | cartella delle copie di sicurezza<br>*Come: la fotocopia del compito prima di correggerlo* | quando salvi un file che esisteva già, Lazarus mette qui la versione di prima. Le copie dei file del progetto hanno **lo stesso nome** dell'originale (`unit1.pas`, `unit1.lfm`, `ciao.lpi`…); un file che non fa parte del progetto prende in più `.bak` (per esempio `prova.pas.bak`). La cartella compare dal secondo salvataggio | sì |

Con le impostazioni normali di Lazarus 4, fuori dalla cartella `backup` non trovi copie con `~` o `.bak`. Se le vedi, qualcuno ha cambiato le impostazioni delle copie (menu «Strumenti» → «Opzioni…», pagina «Backup»).

Regola da ricordare: i **4 file da tenere**, da consegnare e da mettere su GitHub sono `.lpi` `.lpr` `.pas` `.lfm`. Tutto il resto Lazarus lo rifà da solo.

**Da ricopiare sul quaderno**

```
ciao\                       <- UNA cartella = UN progetto
 |- ciao.lpi    progetto (+ opzioni)      TENERE
 |- ciao.lpr    programma principale      TENERE
 |- unit1.pas   il mio codice             TENERE
 |- unit1.lfm   com'e' fatta la finestra  TENERE
 |- ciao.lps    sessione                  si rifa'
 |- ciao.res    risorse (icona)           si rifa'
 |- ciao.ico    icona                     si rifa'
 |- ciao.exe    programma finito (F9)     si rifa'
 |- lib\x86_64-win64\
 |     .o .ppu .compiled .or (compilatore) si rifa'
 |- backup\     copie di sicurezza        si butta
```

![Foto della lavagna: la lavagna del 28/10/2026: i 4 file da tenere, con un progetto che si chiama PIPPO. PIPPO.LPI è il progetto; PIPPO.LPR è il Lazarus Program (il programma principale); UNIT1.PAS è il codice in Object Pascal; UNIT1.LFM è la Lazarus Form (com'è fatta la finestra).](immagini/20261028_lavagna-file-progetto.jpg)

### 8.8 Fallo tuo

Il programma funziona? Adesso rendilo **tuo**. Scegli almeno una cosa:

1. Il saluto nella **tua lingua**: al posto di `'Ciao '` scrivi `'Hello '`, `'مرحبا '`, `'你好 '`, `'Hola '`…
2. Il **titolo** della finestra: clicca su un punto vuoto della Form1, nell'Ispettore oggetti cambia `Caption` (per esempio «Il saluto di Ahmed»).
3. Il **colore**: sempre sulla Form1, proprietà `Color`, scegli un colore dalla tendina.
4. Per i più veloci: aggiungi una TLabel e una seconda riga, `Label1.Caption := 'Ciao ' + Edit1.Text;`: il saluto resta scritto anche nella finestra.

Poi **spiegalo in 30 secondi** al compagno: «Ho messo una TEdit e un TButton; quando clicco, la funzione Button1Click apre una finestrella con Ciao e il nome».

### 8.9 Consegna

Su Classroom c'è il compito **«Il mio primo programma: Ciao in Lazarus»**. Dentro c'è un **Documento Google** già pronto, solo tuo. Aprilo e fai 3 cose:

1. **Il codice.** In Lazarus seleziona con il mouse la tua procedura, da `procedure TForm1.Button1Click` fino a `end;`, premi `Ctrl` + `C`; nel Documento clicca sotto «1. Il mio codice» e premi `Ctrl` + `V`.
2. **Lo screenshot.** Fai partire il programma (`F9`), scrivi il tuo nome e premi Saluta. Poi premi `Win` + `Shift` + `S` e trascina un rettangolo intorno alla tua finestra. Nel Documento clicca sotto «2. Il mio programma che funziona» e premi `Ctrl` + `V`.
3. **Con parole tue.** Sotto «3» scrivi in una o due frasi che cosa fa la riga `ShowMessage('Ciao ' + Edit1.Text);`. Puoi scrivere anche nella tua lingua.

Poi in Classroom premi «Consegna» (il bottone blu in alto a destra nel compito).


## 9. Le lezioni una per una
*In ordine di data: che cosa abbiamo fatto, in breve nelle tre lingue (italiano, arabo, cinese), la teoria e l'esercitazione di ogni lezione. Ogni lezione ha anche il suo libro parziale nella cartella lezioni.*

<!-- LEZIONI:INIZIO -->
### L01 15/09/2026 — Ulisse, la curiosità e l'informatica

*Libro parziale: lezioni/2026-09-15_ulisse-informatica.md*

#### Che cosa abbiamo fatto

1. **Quando:** 15/09/2026, 1 ora, Tecnologia.
2. **Argomenti:** Prima lezione: accoglienza, il viaggio di Ulisse come esempio di curiosità, che cos'è l'informatica.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">L&#x27;informatica tratta le informazioni con il computer: dati in entrata, elaborazione, risultati in uscita.</p><p lang="ar" dir="rtl">المعلوماتية تعالج المعلومات بالحاسوب: بيانات تدخل، معالجة، ونتائج تخرج.</p><p lang="zh">信息学用电脑处理信息：输入数据，处理，输出结果。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **L'informatica come viaggio:** come Ulisse parte per **curiosità** di conoscere, così noi useremo la curiosità come motore per imparare.
2. **Cosa studieremo quest'anno:** il computer e le sue parti, internet, saper usare bene gli strumenti digitali e l'intelligenza artificiale, un po' di programmazione.
3. **Il metodo del corso:** passi piccoli, un risultato concreto a ogni tappa; provare **senza paura di sbagliare** (l'errore è normale); **mostrare** quello che si fa.
4. **Carta e penna sul banco sempre:** appunti e schemi a mano aiutano a capire e a ricordare.

##### Il compito
1. Lezione introduttiva: ascoltare, prendere **appunti a mano**, e dire con parole proprie cosa ci si aspetta dal corso.
2. Nessuna consegna individuale.

##### Criteri di valutazione
1. **Partecipazione**: ascolto e attenzione.
2. **Appunti**: presa di appunti a mano sul quaderno.

### L02 16/09/2026 — Regolamento di laboratorio, utente e password

*Libro parziale: lezioni/2026-09-16_regolamento-user-password.md*

#### Che cosa abbiamo fatto

1. **Quando:** 16/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Regolamento di laboratorio e regolamento sugli strumenti digitali e l'IA; laboratorio 1: utenze e aree di lavoro, login di Windows, account Google e Drive, prova della password.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il laboratorio ha regole precise. Ognuno ha il suo utente e una password segreta, da non dare a nessuno.</p><p lang="ar" dir="rtl">للمختبر قواعد واضحة. لكل طالب اسم مستخدم وكلمة سر لا يعطيها لأحد.</p><p lang="zh">机房有明确的规则。每个人都有自己的用户名和密码，密码不能告诉别人。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Le regole del laboratorio:** come si usano i computer della scuola, rispetto delle postazioni, non installare programmi, non lasciare il proprio account aperto.
2. **Uso corretto di internet e dei servizi digitali** e attenzione alla **privacy** (propria e degli altri).
3. **Regola d'uso dell'Intelligenza Artificiale:** l'IA aiuta a **capire**, non a fare il lavoro **al posto tuo**. Chi capisce e sa spiegare, vince.
4. **Quando hai finito:** niente giochi/YouTube, si resta al posto, si fa qualcosa di utile e si aspetta l'indicazione del docente.

##### Il compito
1. Leggere il **regolamento** e firmarne la **presa visione/accettazione** (modulo).
2. Capire perché ogni regola esiste (non è un capriccio: serve a lavorare bene tutti).

##### Criteri di valutazione
1. **Presa visione**: modulo letto e firmato.
2. **Comprensione**: sa spiegare almeno due regole con parole proprie.

##### Teoria
1. **Account (utente) e password:** l'account è la tua identità sul computer; la password la protegge. Servono per entrare e ritrovare le tue cose.
2. **Login e logout a Windows** e **blocco schermo** con `Ctrl + Alt + Canc` (bloccare quando ci si alza).
3. **Account Google della scuola** e **Google Drive** (lo spazio dove salvare i file online).
4. **Una password sicura:** lunga, non banale (non 1234), non condivisa; e si **tiene al sicuro** (non attaccata al monitor).

##### Il compito
1. Accedere al computer e all'**account Google**; **provare** la password.
2. Compilare a penna la scheda **"Le mie utenze e password"** e tenerla al sicuro.
3. Provare a **bloccare e sbloccare** lo schermo con `Ctrl + Alt + Canc`.

##### Criteri di valutazione
1. **Accesso**: sa accedere e uscire, e bloccare lo schermo.
2. **Password**: ne gestisce una in modo sicuro.

### L03 17/09/2026 — Prova account e «Io e la mia famiglia»

*Libro parziale: lezioni/2026-09-17_account-famiglia.md*

#### Che cosa abbiamo fatto

1. **Quando:** 17/09/2026, 2 ore, Tecnologia e Sicurezza.
2. **Argomenti:** Prova dell'account; laboratorio 2: cartelle ad albero, giro della Google Suite, iscrizione a Classroom; primo documento «Io e la mia famiglia» con Google Documenti e Google Traduttore, consegnato su Classroom.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Primo documento con Google Documenti, aiutandosi con Google Traduttore, e prima consegna su Classroom.</p><p lang="ar" dir="rtl">أول مستند في مستندات Google بمساعدة مترجم Google، وأول تسليم في Classroom.</p><p lang="zh">用 Google 文档写第一份文件，用 Google 翻译帮忙，第一次在 Classroom 上交作业。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Ripasso:** accedere ai propri account (Windows, Google) e **verificare** che tutto funzioni.
2. **Se non si riesce ad accedere:** cosa fare (password sbagliata o dimenticata, maiuscole accese, chiedere aiuto).
3. **Google Classroom:** il luogo dove il docente mette i compiti e dove si **consegna** il proprio lavoro; come **iscriversi** al corso.

##### Il compito
1. **Provare l'accesso** ai propri account e verificare l'**ingresso a Google Classroom**.
2. Segnare quali account funzionano e quali no.

##### Criteri di valutazione
1. **Accesso riuscito**: entra nei propri account.
2. **Classroom**: iscritto al corso.

##### Teoria
1. **Google Documenti:** un programma per scrivere testi che funziona nel browser e si salva da solo.
2. **Presentarsi per iscritto:** scrivere di sé e della propria famiglia (chi sono, da dove vengo, la mia storia).
3. **Google Traduttore** (`translate.google.com`): chi non scrive ancora bene in italiano scrive nella propria lingua e traduce.
4. **Privacy:** un lavoro personale si condivide solo con il docente o la classe, non si pubblica su internet.

##### Il compito
1. Creare un documento in **Google Documenti** che presenta te stesso/a e la tua famiglia.
2. Se serve, scrivere prima nella propria lingua e **tradurre** in italiano.
3. **Fallo tuo:** aggiungere una foto o un colore che ti rappresenta.
4. **Consegnare** su Google Classroom.

##### Criteri di valutazione
1. **Contenuto**: si presenta con alcune frasi.
2. **Lingua**: testo comprensibile in italiano.
3. **Personalizzazione**: un dettaglio proprio.
4. **Consegna**: su Classroom.

### L04 18/09/2026 — GitHub e i repository

*Libro parziale: lezioni/2026-09-18_github-repository.md*

#### Che cosa abbiamo fatto

1. **Quando:** 18/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Ricerca «che cos'è GitHub e che cos'è un repository» in Google Documenti; creazione dell'account GitHub.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">GitHub conserva i progetti e la loro storia. Un repository è la cartella del progetto, con tutte le versioni.</p><p lang="ar" dir="rtl">يحفظ GitHub المشاريع وتاريخها. المستودع (repository) هو مجلد المشروع مع كل نسخه.</p><p lang="zh">GitHub 保存项目和它们的历史。仓库（repository）就是项目的文件夹，里面有所有版本。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **GitHub:** un sito dove si **conservano e condividono** progetti (documenti, codice, siti).
2. **Repository (repo):** una "cartella di progetto" online, con dentro i file e la loro **storia** (chi ha cambiato cosa e quando).
3. **A cosa serve:** salvare il lavoro al sicuro, vederne le **versioni**, poter **collaborare** in più persone.
4. Con GitHub un domani potremo **pubblicare** i nostri lavori (siti, giochi) su internet.

##### Il compito
1. Fare una **piccola ricerca**: "cos'è GitHub e cos'è un repository", guardando il sito e cercando in rete.
2. Scrivere in **Google Documenti** e **consegnare** su Classroom.
3. (Passo successivo) **Creare l'account GitHub** con l'email della scuola.

##### Criteri di valutazione
1. **Comprensione**: spiega cos'è GitHub e cos'è un repository.
2. **Consegna**: documento consegnato su Classroom.

### L05 21/09/2026 — Ripasso hardware, regole e il versioning

*Libro parziale: lezioni/2026-09-21_hardware-regole-versioning.md*

#### Che cosa abbiamo fatto

1. **Quando:** 21/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Ripasso dei pezzi del PC; regole e modalità di lavoro; che cos'è il versioning (le versioni di un lavoro); quiz «Regole + Versioning».

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Ogni lavoro cresce per versioni: 1.0, 1.1, 2.0. Così si vede che cosa è cambiato e si può tornare indietro.</p><p lang="ar" dir="rtl">كل عمل يكبر بنسخ: 1.0 ثم 1.1 ثم 2.0. هكذا نرى ما تغيّر ونستطيع الرجوع.</p><p lang="zh">每个作品按版本成长：1.0、1.1、2.0。这样能看到改了什么，也能回到以前。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Ripasso delle parti del PC:** CPU (il cervello), RAM (il tavolo di lavoro), SSD (il magazzino), scheda madre (la base), scheda video (le immagini), alimentatore (la corrente), case (la scatola), dissipatore (il raffreddamento).
2. **A cosa serve ciascuno** e come i pezzi lavorano insieme.
3. Fare uno **schema a mano** delle parti aiuta a fissarle.

##### Il compito
1. **Ripasso a voce** e **schema a mano** sul quaderno delle parti del PC e della loro funzione.
2. Nessuna consegna online (attività in classe).

##### Criteri di valutazione
1. **Conoscenza**: sa nominare le parti e spiegarne la funzione.
2. **Schema**: schema a mano sul quaderno.

##### Teoria
1. **Come si lavora in laboratorio:** un obiettivo alla volta, si segue l'indicazione, si prende appunti.
2. **Come si consegna:** i compiti si trovano e si consegnano su **Google Classroom**.
3. **Comportamento in classe:** si alza la **mano ben alta** e si aspetta il cenno del docente; attenzione durante il lavoro.
4. **Quando hai finito o non hai nulla da fare:** niente giochi/YouTube, si resta al posto, si fa qualcosa di utile.

##### Il compito
1. Comprendere e **applicare** le regole e le modalità di lavoro.
2. Nessuna consegna online (attività in classe).

##### Criteri di valutazione
1. **Rispetto delle modalità**: segue le regole di lavoro e di consegna.

##### Teoria
1. **Versioning:** dare un **numero** alle versioni di un lavoro (v1.0, v1.1, v2.0) per sapere qual è l'**ultima** e tenere la **storia**.
2. **Major e minor:** se cambia **molto** sale il **primo** numero (2.0); se è una **piccola** correzione sale il **secondo** (1.1).
3. **Ripartenza:** a una nuova versione principale si riparte da .0 (es. 2.0).
4. **Perché serve:** non perdere il lavoro, poter **tornare indietro**, sapere **cosa è cambiato**. È l'idea alla base di Git.

##### Il compito
1. Attività sul versioning: leggere la **scheda delle versioni** e svolgere il **quiz**.
2. Saper dire, dato un cambiamento, se è **major** o **minor**.

##### Criteri di valutazione
1. **Comprensione**: distingue major e minor e spiega a cosa serve il versioning.
2. **Quiz**: quiz completato.

### L06 22/09/2026 — Controllo degli account

*Libro parziale: lezioni/2026-09-22_controllo-account.md*

#### Che cosa abbiamo fatto

1. **Quando:** 22/09/2026, 1 ora, Tecnologia.
2. **Argomenti:** Controllo che ognuno entri nei suoi account (Windows, Google, Classroom, GitHub).

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Controlliamo che ognuno entri da solo in tutti i suoi account.</p><p lang="ar" dir="rtl">نتأكد أن كل طالب يدخل وحده إلى كل حساباته.</p><p lang="zh">检查每个人都能自己登录所有账号。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Mettere in ordine gli account:** email della scuola, Google, GitHub; controllare di **poter accedere** a tutto.
2. **Sicurezza:** non condividere le password; riconoscere **email sospette** (phishing) e non cliccare link strani.
3. Tenere una **scheda** con le proprie utenze, al sicuro.

##### Il compito
1. **Controllare** i propri account e segnare quali funzionano e quali no.
2. Sistemare eventuali problemi di accesso con l'aiuto del docente.

##### Criteri di valutazione
1. **Account in ordine**: accede a scuola/Google/GitHub.
2. **Sicurezza**: sa riconoscere una password debole e un'email sospetta.

### L07 23/09/2026 — L'hardware del PC

*Libro parziale: lezioni/2026-09-23_hardware.md*

#### Che cosa abbiamo fatto

1. **Quando:** 23/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** I componenti del PC: scheda madre, processore, RAM, memoria di massa, alimentatore, scheda video.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il PC è fatto di pezzi: scheda madre, processore (CPU), RAM, disco, alimentatore, scheda video.</p><p lang="ar" dir="rtl">يتكوّن الحاسوب من قطع: اللوحة الأم، المعالج، الذاكرة RAM، القرص، مزوّد الطاقة، بطاقة الرسوم.</p><p lang="zh">电脑由零件组成：主板、处理器（CPU）、内存（RAM）、硬盘、电源、显卡。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Approfondimento hardware:** i componenti e le loro **caratteristiche** (velocità, capacità).
2. **Compatibilità:** i pezzi devono "andare d'accordo" (es. CPU e scheda madre stesso socket).
3. **Standard:** form factor (ATX/microATX/Mini-ITX), **socket** della CPU, memorie **RAM DDR3/DDR4/DDR5**.
4. Prepararsi a **configurare** un PC scegliendo pezzi compatibili.

##### Il compito
1. Attività pratica: **riconoscere** i componenti e le loro caratteristiche.
2. Nessuna consegna online (attività in classe, preparazione alla configurazione).

##### Criteri di valutazione
1. **Riconoscimento**: identifica i componenti e le compatibilità principali.

### L08 24/09/2026 — Configurazione di un PC: standard hardware

*Libro parziale: lezioni/2026-09-24_configurazione-pc.md*

#### Che cosa abbiamo fatto

1. **Quando:** 24/09/2026, 3 ore, Tecnologia e Sicurezza.
2. **Argomenti:** Standard hardware: form factor (ATX, microATX, Mini-ITX), slot PCIe, socket Intel e AMD, RAM DDR3/4/5; documento con teoria e immagini consegnato su Classroom; correzione dei compiti.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">I pezzi del PC devono essere compatibili: la stessa misura (form factor), lo stesso socket, lo stesso tipo di RAM.</p><p lang="ar" dir="rtl">يجب أن تكون قطع الحاسوب متوافقة: نفس المقاس، نفس المقبس (socket)، نفس نوع الذاكرة RAM.</p><p lang="zh">电脑零件必须兼容：同样的尺寸（form factor）、同样的插座（socket）、同样类型的内存。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. **Form factor:** grandezza della scheda madre — ATX (grande), microATX (media), Mini-ITX (piccola).
2. **Slot PCIe:** attacchi (x1, x4, x8, x16); il **x16** serve per la **scheda video**.
3. **Socket CPU:** **Intel = LGA** (es. LGA1700), **AMD = AM** (es. AM5); CPU e scheda madre stesso socket.
4. **Processori per marca:** Intel Core **i3/i5/i7/i9**, AMD Ryzen **3/5/7/9**.
5. **Memorie RAM:** **DDR3/DDR4/DDR5**, non intercambiabili (tacca diversa).

##### Il compito
1. Creare un documento in **Google Documenti** che spiega **con parole proprie** i 5 argomenti.
2. Inserire **immagini prese dal web** (almeno una per argomento).
3. **Consegnare** su Google Classroom.

##### Criteri di valutazione
1. **Completezza teoria**: spiegati tutti e 5 gli argomenti.
2. **Parole proprie**: spiegazione personale (prova del nove a voce).
3. **Immagini**: almeno una per argomento.
4. **Consegna**: su Classroom.

##### Teoria
1. **Rivedere insieme gli errori tipici** della configurazione: componenti dimenticati (spesso l'alimentatore), doppioni di RAM/SSD, totale non calcolato.
2. **Come si corregge un lavoro:** si guarda cosa manca, si aggiunge, si ricontrolla il totale.
3. **Migliorare è normale:** un lavoro si consegna, si riceve un riscontro e si migliora — come fanno i professionisti.

##### Il compito
1. Correggere e **completare** il proprio documento di configurazione con le indicazioni ricevute.
2. Ricontrollare compatibilità, presenza di tutti i componenti e totale.

##### Criteri di valutazione
1. **Correzione**: sistema gli errori segnalati.
2. **Completezza**: il lavoro finale ha tutti i componenti e il totale.

*Classe 1 — Informatica. Scheda docente + appunti per i ragazzi sugli standard
hardware: form factor (AT/ATX/microATX/Mini-ITX), slot PCIe (x1/x4/x8/x16),
socket della CPU (Intel LGA vs AMD PGA/AM5), tipi di RAM (DDR3/DDR4/DDR5, DIMM
vs SO-DIMM). I PDF (`20260924_Classe-1-PerTutti_v1.0_Standard-Configurazione-PC_IT/AR/ZH.pdf`)
contengono i disegni con le forme in proporzione reale, nelle 3 lingue; questo
`.md` è la fonte versionata e serve anche all'AI dei ragazzi per spiegare/tradurre.*

> Nota: i disegni (Fig. 1–4) sono nei file `standard-hardware-it/ar/zh.html` → PDF. Qui
> sono descritti a parole così che l'AI possa spiegarli in un'altra lingua.

---

##### Idea guida

Dentro un computer i pezzi devono **combaciare**: una scheda madre entra solo in
certi case, una CPU entra solo in un certo socket, una RAM entra solo nel suo
slot. Per farli combaciare, nel mondo ci si è messi d'accordo su **misure e forme
comuni**: sono gli **standard**. Ne vediamo quattro: form factor, slot PCIe,
socket, tipi di RAM.

> [BLU] Carta e penna: prima di guardare lo schermo, ognuno disegna a mano un
> rettangolo "scheda madre" e ci segna dove va la CPU (socket), dove le RAM (slot
> lunghi e stretti) e dove la scheda video (slot PCIe x16). Poi confronta con
> quello vero.

##### 1. Form factor — la taglia della scheda madre

**Form factor** = la misura standard della scheda madre. Decide anche quale
**case** ("cassone") serve: una scheda grande non entra in un case piccolo.

1. **ATX** — 305 × 244 mm. Il più diffuso: PC desktop e da gioco (schede "ATX"
   ASUS, MSI, Gigabyte, ASRock). Ha più slot (fino a 4 RAM, più PCIe).
2. **microATX (mATX)** — 244 × 244 mm. PC compatti ed economici, uffici.
3. **Mini-ITX** — 170 × 170 mm. Mini-PC, PC da salotto (HTPC): pochi slot.
4. **E-ATX** — 305 × 330 mm. Workstation e fascia alta, moltissimi slot.
5. **AT / Baby-AT** — storico (anni '80–'90, IBM): non più in commercio, solo
   cultura generale.

> [GIALLO] Da ricordare: ATX è lo standard "normale"; le altre sono variazioni.
> Più piccola = meno spazio = meno slot.

##### 2. Slot PCIe — dove si infilano le schede aggiuntive

**PCIe** (PCI Express) è lo slot per le **schede di espansione**, prima fra tutte
la **scheda video** (GPU). Il numero dice quante "corsie" (linee di dati) ha: più
corsie = più veloce. Una scheda corta entra anche in uno slot più lungo.
Lunghezze reali:

1. **PCIe x16** — 89 mm, 16 corsie: **scheda video** (NVIDIA GeForce, AMD Radeon).
2. **PCIe x8** — 56 mm, 8 corsie: RAID, schede di rete veloci, seconda GPU.
3. **PCIe x4** — 39 mm, 4 corsie: adattatori per SSD **NVMe**, controller.
4. **PCIe x1** — 25 mm, 1 corsia: schede di rete, audio, USB, acquisizione video.

> [BLU] Versioni PCIe: oltre alla lunghezza c'è la generazione 3.0 → 4.0 → 5.0.
> Ad ogni salto la banda raddoppia, ma la forma dello slot resta uguale
> (compatibili). **M.2** è invece un piccolo slot dedicato agli SSD NVMe: usa le
> corsie PCIe ma ha una forma tutta sua.

##### 3. Socket — dove si appoggia la CPU

Il **socket** è lo "zoccolo" sulla scheda madre dove si mette la **CPU**. Ogni
socket ha un nome e accetta solo certe CPU. Due famiglie, con una differenza
fisica:

1. **Intel — LGA** (Land Grid Array): i **pin sono nel socket**; la CPU ha
   contatti piatti.
2. **AMD — PGA** (Pin Grid Array): i **pin sono sulla CPU**. (Attenzione: **AM5**
   di AMD è invece **LGA**, come Intel.)

Nomi (socket → CPU che accetta):

1. **Intel LGA1700** — Intel Core 12ª · 13ª · 14ª gen (i3/i5/i7/i9).
2. **Intel LGA1851** — Intel Core Ultra (serie 2).
3. **AMD AM4** (PGA) — Ryzen serie 1000 → 5000.
4. **AMD AM5** (LGA) — Ryzen serie 7000 e 9000.
5. **Intel LGA4677 / AMD SP5** — server e workstation (Xeon, EPYC).

> [ROSSO] Attenzione: il numero nel nome (1700, 1851, AM4…) è legato ai
> **contatti**, non è "quanto è potente". CPU e scheda madre si comprano **sempre
> in coppia**, controllando che il socket sia lo stesso. Il triangolino "pin 1"
> in un angolo indica il verso giusto di inserimento.

##### 4. Tipi di RAM — DDR3, DDR4, DDR5

La **RAM** è la memoria di lavoro: le "bacchette" (moduli) negli slot lunghi
vicino alla CPU. Ogni generazione ha la **tacca (chiave) in una posizione
diversa**: così è impossibile metterla nello slot sbagliato. La scheda madre
supporta **una** sola generazione.

1. **DDR3** — 240 pin, 1,5 V. Es. DDR3-1600 (PC3-12800). PC vecchi.
2. **DDR4** — 288 pin, 1,2 V. Es. DDR4-3200 (PC4-25600). Standard recente.
3. **DDR5** — 288 pin, 1,1 V. Es. DDR5-5600 / 6000. Attuale (Corsair Vengeance,
   Kingston Fury, Crucial).
4. **SO-DIMM** — più corta: è la RAM dei **portatili** (stessa sigla + "SO-DIMM").

> [GIALLO] DDR4 e DDR5 hanno tutte e due 288 pin, ma la tacca è in un punto
> diverso e la scheda madre ne supporta una sola: non sono intercambiabili. La
> RAM da desktop (DIMM, lunga) è diversa da quella del portatile (SO-DIMM, corta).

##### 5. Riepilogo — cosa deve combaciare con cosa

1. **Case ⟷ scheda madre**: stesso form factor (ATX, microATX, Mini-ITX).
2. **Scheda madre ⟷ CPU**: stesso socket (LGA1700, AM5…).
3. **Scheda madre ⟷ RAM**: stessa generazione (DDR4 con DDR4, DDR5 con DDR5).
4. **Scheda video ⟷ scheda madre**: slot PCIe x16.

> [BLU] La prova del nove (saperlo spiegare): ogni ragazzo racconta a voce, con
> parole sue, "Perché non posso mettere una CPU AMD su una scheda Intel? Perché
> una DDR5 non entra in uno slot DDR4?". Se lo sa spiegare, ha capito davvero.

> [GIALLO] Collegamento al compito: questi standard sono i controlli che fa
> PCPartPicker quando montiamo il PC (attività "Costruisci il PC"): avvisa se
> socket, RAM o form factor non combaciano. Ora sappiamo perché lo fa.

##### Schema alla lavagna (fatto in classe)

Lo stesso contenuto è stato disegnato a mano alla lavagna durante la lezione del
24/09/2026 (metodo "carta e penna"): SLOT schede (PCIe con la tacca), SLOT RAM
(piedini + tacca), SOCKET CPU (il processore che si ribalta + i pin sotto),
GRANDEZZA MB/CASE → AT, ATX, mini-ATX. Foto: `immagini/20260924_Classe-1-PerTutti_Lavagna-Configurazione-PC.jpg`.


### L09 30/09/2026 — Configura un PC e cattura lo schermo

*Libro parziale: lezioni/2026-09-30_configura-pc-cattura.md*

#### Che cosa abbiamo fatto

1. **Quando:** 30/09/2026, 3 ore, Laboratorio.
2. **Argomenti:** Configurazione di un PC con PCPartPicker; cattura dello schermo, copia e incolla, trascrizione con l'AI.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Scegliamo i pezzi di un PC con PCPartPicker e impariamo a catturare lo schermo per consegnare il lavoro.</p><p lang="ar" dir="rtl">نختار قطع حاسوب بموقع PCPartPicker ونتعلّم التقاط صورة الشاشة لتسليم العمل.</p><p lang="zh">用 PCPartPicker 选择电脑零件，学习截屏来交作业。</p></div>

#### La teoria e l'esercitazione

##### Teoria
1. Un computer è fatto di **8 componenti principali**: CPU (cervello), dissipatore (raffredda), scheda madre (base), RAM (tavolo di lavoro), SSD (magazzino), scheda video (immagini), case (scatola), **alimentatore** (corrente — senza, il PC non si accende).
2. I pezzi devono essere **compatibili**; il configuratore lo controlla da solo.
3. **Restare nel budget** e avere un **totale** realistico.

##### Il compito
1. Con **it.pcpartpicker.com** (Builder) scegliere un componente per ogni categoria, compatibili ed entro budget.
2. In **Google Documenti** scrivere la **lista**, il **prezzo totale** e **2-3 righe sul perché**.
3. **Consegnare** su Classroom.

##### Criteri di valutazione
1. **Completezza**: tutti gli 8 componenti.
2. **Prezzi e totale**: presenti e calcolati.
3. **Scelte sensate**: coerenti, senza doppioni.
4. **Cura e personalizzazione**: ordinata, con motivazione.
5. **Originalità (anti-plagio)**: autentico.

##### Teoria
1. **Screenshot (cattura schermo):** una "foto" dello schermo. Solo una parte: `Windows + Maiusc + S`; tutto lo schermo: `Windows + Stamp`.
2. **Copia-incolla:** `Ctrl + C` per copiare, `Ctrl + V` per incollare.
3. **Trascrivere con Gemini** (`gemini.google.com`): si incolla un'immagine con del testo e si chiede "Trascrivi il testo di questa immagine".
4. **Google Lens:** su Chrome legge il testo dentro un'immagine (clic destro → Cerca immagine con Google → Testo).

##### Il compito
1. Fare uno **screenshot** di una pagina **con del testo**.
2. **Incollarlo in Gemini** e farsi **trascrivere** il testo.
3. **Copiare** il testo in un documento di **Google Documenti** e **consegnare** su Classroom.
4. **Riflessione finale OBBLIGATORIA:** cosa non sono riuscito a fare e perché, cosa non ho capito.

##### Criteri di valutazione
1. **Screenshot**: presente e corretto.
2. **Trascrizione**: fatta con Gemini.
3. **Copia-incolla**: testo nel documento.
4. **Consegna**: su Classroom.
5. **Riflessione**: presenti le due parti (la più importante).

### L10 01/10/2026 — Bit, byte e numeri binari

*Libro parziale: lezioni/2026-10-01_bit-byte-binario.md*

#### Che cosa abbiamo fatto

1. **Quando:** 01/10/2026, 2 ore, Tecnologia.
2. **Argomenti:** Sistema decimale e binario, il bit, il byte (8 bit), conversione da binario a decimale con il metodo delle caselle (128…1), multipli KB, MB, GB; esercitazione di 16 esercizi consegnata su Classroom.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il computer usa solo 0 e 1 (bit). 8 bit fanno un byte. Per passare da binario a decimale si sommano i valori delle caselle con 1.</p><p lang="ar" dir="rtl">الحاسوب يستعمل 0 و1 فقط (بِت). ٨ بِت = بايت واحد. للتحويل من الثنائي إلى العشري نجمع قيم الخانات التي فيها 1.</p><p lang="zh">电脑只用 0 和 1（比特）。8 个比特是一个字节。二进制转十进制：把有 1 的格子的数值加起来。</p></div>

#### La teoria e l'esercitazione

Classe 1 · spiegazione base · italiano · solo binario→decimale

**In questa lezione facciamo UNA direzione: dal BINARIO al DECIMALE** (da 0 e 1 al numero di tutti i giorni).

##### 1. I numeri di tutti i giorni

Noi contiamo con **dieci cifre**: 0 1 2 3 4 5 6 7 8 9. Con queste dieci cifre scriviamo
**qualsiasi** numero. Questo si chiama **sistema decimale** («deci» vuol dire dieci).

##### 2. Dentro il computer: acceso o spento

Il computer è fatto di **tantissimi piccoli interruttori**. Un interruttore può stare solo
in **due modi**: acceso o spento. Il computer usa questi due stati: **acceso = 1**, **spento = 0**.

##### 3. Il bit

Un **bit** è la cosa più piccola: **una sola cifra, 0 oppure 1**. La parola "bit"
viene dall'inglese **Binary Digit** = **cifra binaria**. Tutto, dentro il computer, è fatto di bit.

##### 4. Contare con solo 0 e 1 (il binario)

Con due cifre si conta così: 0, 1… poi le cifre finiscono, quindi si scrive **10, 11, 100, 101,
110, 111…** È come il **contachilometri** dell'auto: quando una rotella arriva in fondo, gira quella accanto.

##### 5. Il byte

Mettiamo insieme **8 bit**: questo si chiama **byte**. Un byte ha **8 caselle**, ognuna
con uno 0 o un 1. Una **lettera** scritta nel computer occupa **1 byte**.

##### 6. Da binario a decimale (il metodo delle caselle)

Ogni casella ha un **valore**. Da destra verso sinistra: **1, 2, 4, 8, 16, 32, 64, 128**
(ogni volta il doppio). Per trovare il numero: guarda dove c'è un **1** e **somma** i valori.

**Esempio (come alla lavagna):**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |

Ci sono gli **1** sotto 64, 8, 4, 2 → **64 + 8 + 4 + 2 = 78**. Quindi `01001110 = 78`.

La lavagna della nostra lezione: BIT, Byte = 8 bit e la conversione 01001110 = 64+8+4+2 = 78.

**Trucco con le dita:** ogni dito è un bit (alzato = 1, abbassato = 0). Con
**una mano** conti fino a **31**, con **due mani** fino a **1023**!

##### 7. Quanto «pesa» (i multipli)

1 byte = 8 bit. Poi: **1 KB = 1024 byte**, **1 MB = 1024 KB**, **1 GB = 1024 MB**.
Una foto pesa qualche **MB**; un film qualche **GB**.

##### Tanti esempi: byte → decimale

Dato il byte, somma i valori dove c'è un 1: trovi il numero. Gli 1 sono evidenziati.

`00000011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

= 2 + 1 = **3**

`00000101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

= 4 + 1 = **5**

`00001010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |

= 8 + 2 = **10**

`00001101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |

= 8 + 4 + 1 = **13**

`00010011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |

= 16 + 2 + 1 = **19**

`00011011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |

= 16 + 8 + 2 + 1 = **27**

`00101010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

= 32 + 8 + 2 = **42**

`00110010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |

= 32 + 16 + 2 = **50**

`01000000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

= 64 = **64**

`01001110`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |

= 64 + 8 + 4 + 2 = **78**

`01010101`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

= 64 + 16 + 4 + 1 = **85**

`01100100`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |

= 64 + 32 + 4 = **100**

`01111000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |

= 64 + 32 + 16 + 8 = **120**

`01111111`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

= 64 + 32 + 16 + 8 + 4 + 2 + 1 = **127**

`10000010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

= 128 + 2 = **130**

`10010110`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |

= 128 + 16 + 4 + 2 = **150**

`10101010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

= 128 + 32 + 8 + 2 = **170**

`11001000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |

= 128 + 64 + 8 = **200**

`11010010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |

= 128 + 64 + 16 + 2 = **210**

`11100001`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 |

= 128 + 64 + 32 + 1 = **225**

`11110000`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

= 128 + 64 + 32 + 16 = **240**

`11111010`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |

= 128 + 64 + 32 + 16 + 8 + 2 = **250**

`11111111`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = **255**

`01100011`

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |

= 64 + 32 + 2 + 1 = **99**

### L11 02/10/2026 — Divisioni per 2: da decimale a binario

*Libro parziale: lezioni/2026-10-02_divisioni-decimale-binario.md*

#### Che cosa abbiamo fatto

1. **Quando:** 02/10/2026, 3 ore, Laboratorio e Sicurezza.
2. **Argomenti:** La divisione per 2 con il resto e la conversione da decimale a binario con il metodo della lavagna; compiti con il timer.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Da decimale a binario: si divide per 2 tante volte e si leggono i resti dal basso verso l&#x27;alto.</p><p lang="ar" dir="rtl">من العشري إلى الثنائي: نقسم على 2 مرات كثيرة ونقرأ البواقي من الأسفل إلى الأعلى.</p><p lang="zh">十进制转二进制：一直除以 2，然后从下往上读余数。</p></div>

#### La teoria e l'esercitazione

v1.4

#### La divisione per 2 con il resto

Classe 1 · scheda di aiuto · sul foglio · italiano

##### 1. Dividere per 2 = fare 2 parti uguali

Hai delle caramelle e le dividi tra **2 amici**: ognuno ne prende lo stesso numero. Quella che **avanza** (in rosso) è il **RESTO**.

6 caramelle → 3 a testa, non avanza niente.

6 : 2 = 3 resto 0

7 caramelle → 3 a testa, ne avanza 1.

7 : 2 = 3 resto 1

##### 2. La regola (una riga sola)

**Numero PARI** (finisce con 0, 2, 4, 6, 8) → fai la **metà**, resto **0**.
**Numero DISPARI** (finisce con 1, 3, 5, 7, 9) → **togli 1** (è il resto), poi fai la **metà**.

Esempio: **37** è dispari → tolgo 1 → 36 → metà = **18**. Quindi **37 : 2 = 18 resto 1**.

##### 3. La tabella delle metà (guardala quando serve)

| numero | : 2 | resto |
| --- | --- | --- |
| **1** | 0 | 1 |
| **2** | 1 | 0 |
| **3** | 1 | 1 |
| **4** | 2 | 0 |
| **5** | 2 | 1 |
| **6** | 3 | 0 |
| **7** | 3 | 1 |
| **8** | 4 | 0 |
| **9** | 4 | 1 |
| **10** | 5 | 0 |

| numero | : 2 | resto |
| --- | --- | --- |
| **11** | 5 | 1 |
| **12** | 6 | 0 |
| **13** | 6 | 1 |
| **14** | 7 | 0 |
| **15** | 7 | 1 |
| **16** | 8 | 0 |
| **17** | 8 | 1 |
| **18** | 9 | 0 |
| **19** | 9 | 1 |
| **20** | 10 | 0 |

| numero | : 2 | resto |
| --- | --- | --- |
| **21** | 10 | 1 |
| **22** | 11 | 0 |
| **23** | 11 | 1 |
| **24** | 12 | 0 |
| **25** | 12 | 1 |
| **26** | 13 | 0 |
| **27** | 13 | 1 |
| **28** | 14 | 0 |
| **29** | 14 | 1 |
| **30** | 15 | 0 |

| numero | : 2 | resto |
| --- | --- | --- |
| **31** | 15 | 1 |
| **32** | 16 | 0 |
| **33** | 16 | 1 |
| **34** | 17 | 0 |
| **35** | 17 | 1 |
| **36** | 18 | 0 |
| **37** | 18 | 1 |
| **38** | 19 | 0 |
| **39** | 19 | 1 |
| **40** | 20 | 0 |

##### 4. Esercizi

##### Livello 1 — dividi le caramelle in coppie (colora quella che avanza)

1.4 : 2 = \_\_\_\_ resto \_\_\_\_

2.5 : 2 = \_\_\_\_ resto \_\_\_\_

3.8 : 2 = \_\_\_\_ resto \_\_\_\_

4.9 : 2 = \_\_\_\_ resto \_\_\_\_

##### Livello 2 — pari o dispari? poi dividi

5.10 : 2 = \_\_\_\_ resto \_\_\_\_

6.11 : 2 = \_\_\_\_ resto \_\_\_\_

7.14 : 2 = \_\_\_\_ resto \_\_\_\_

8.15 : 2 = \_\_\_\_ resto \_\_\_\_

9.20 : 2 = \_\_\_\_ resto \_\_\_\_

10.21 : 2 = \_\_\_\_ resto \_\_\_\_

##### Livello 3 — divisioni a catena

La prima riga è già fatta: 37 : 2 = 18 resto 1. Il **18** passa nella riga sotto e lo dividi. Fai così ogni volta: il risultato va nella riga sotto. Ti fermi quando il risultato è **0**.

1.37 : 2 = 18 resto 1(già fatto)

2.18 : 2 = \_\_\_\_ resto \_\_\_\_← il risultato della riga sopra

3.\_\_\_\_ : 2 = \_\_\_\_ resto \_\_\_\_← il risultato della riga sopra

4.\_\_\_\_ : 2 = \_\_\_\_ resto \_\_\_\_← il risultato della riga sopra

5.\_\_\_\_ : 2 = \_\_\_\_ resto \_\_\_\_← il risultato della riga sopra

6.\_\_\_\_ : 2 = \_\_\_\_ resto \_\_\_\_← il risultato della riga sopra

FATTO! Ora sai fare la divisione per 2 con il resto.

v1.2

#### Da decimale a binario

Classe 1 · spiegazione · italiano · 02/10/2026

**Ieri** abbiamo fatto la strada da 0 e 1 al numero (binario → decimale).
**Oggi facciamo la strada al contrario:** dal numero di tutti i giorni a 0 e 1 (decimale → binario).

##### 1. Ripasso in 30 secondi

1. Un **bit** è una sola cifra: **0** oppure **1**.
2. Un **byte** sono **8 bit**: 8 caselle.
3. Le caselle valgono, da destra: **1, 2, 4, 8, 16, 32, 64, 128** (ogni volta il doppio).

##### 2. Il metodo delle divisioni per 2 (come alla lavagna)

1. Scrivi il **numero** in alto a sinistra e tira una **linea** verticale.
2. **Dividi per 2**: il **risultato** va sotto, a sinistra; il **resto** (0 oppure 1) va a destra della linea.
3. **Continua** a dividere il nuovo numero, finché arrivi a **1**. L'ultimo 1 passa a destra così com'è.
4. **Leggi i resti dal basso verso l'alto**: quello è il numero in binario.

**Trucco:** il resto è facilissimo. **Numero pari → resto 0**, **numero dispari → resto 1**.
Non serve nemmeno fare la divisione col resto: basta guardare se il numero è pari o dispari.

##### 3. L'esempio della lavagna: 37

÷ 2resto37118091402011

37 diviso 2 fa 18, resto **1**. 18 diviso 2 fa 9, resto **0**. 9 diviso 2 fa 4, resto **1**.
4 diviso 2 fa 2, resto **0**. 2 diviso 2 fa 1, resto **0**. Il 1 finale passa a destra: **1**.

Leggo i resti **dal basso verso l'alto**: `100101`.

**La prova con le caselle:** dove c'è un 1 sommo il valore: **32 + 4 + 1 = 37**. Giusto!

**byte (8 cifre):**

128064032116080412011

##### 4. Il byte: gli zeri davanti

Un byte ha sempre **8 caselle**. Se il numero binario ha meno cifre, si aggiungono degli
**zeri a SINISTRA** (davanti). Gli zeri davanti **non cambiano il valore**, come `007` che vale 7.

`100101` ha 6 cifre → aggiungo 2 zeri davanti → `00100101` (gli zeri aggiunti sono in rosso).

![](data:image/jpeg;base64,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)

La lavagna della nostra lezione: 37 diviso per 2 più volte, i resti letti dal basso verso l'alto (100101), la prova 32 + 4 + 1 = 37 e il byte 00100101.

![](data:image/jpeg;base64,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bdJSmkpiQUhpaaaTAjmG6Nh7VgXUXUVvztsjY+1YczlmOaykaRM54dvOahZfar8luTyDVZ4yucjpUllc0mKeR6000AIKUUlLQAo60o602lHBpAOpc4puaUGmA8GlzTAeaUGkA+l700GlzzQAtJilpaAGEUhFPIpNtAERFIak200rQBGRSU/FJigBvak7U40lMBopRSClBoQB1oo6UUAAzR3o5o4zQAUlLQKACgUYoFABmijINJQAooooz3oAKTpS0UAHWj2ooBoAKTFLSHigAo6UdKKACiiigAooxxSUAFL2yaT60UALmikoNAC5pKKKACig0UAFFHaigBKKU0lFwFFFIKXNABRRR9aQBRRRTAKXNFJQAUdaKKACjFFLjNIBKDRRTAbjFJTjTGNAilq7EQqvYmsbitfWOYU+tZPFJgWLnlQK9K8LjZo8CnrivM7ngivS9GkEem2xPTYK6EZM16KQmkzQxCk02gmmyOEUselIaM3V7nYnlg81mwzbyFPWl1W4WWXjPFR6cPMkJ7CsmaItkH0qrMnUk1ckbbxVOfJ5oGVHAFRHippBxUJNIYnFFBFJ0oAcKAaSlzSAWlBpuaM0APFKDTM4pc0APBpc0wGl9qAJAaXNRing80APpMULzQ7pGAXYKDwMmgBDTSKkwKaRxQBFim4qUimEGgBntTT1p9NNADR1ope1JTADRRRQAUGk7UtABiiik9aAFpDxS9RSUAKKSgCigAo70UUAHel70UmKACjrR0ozQAuRSUd6MUABo+tGaDQAdaO1JRQAo6Ugoo6UwDvRmijPrSASloooEFHej6UlACmikpcUAFFBooGBpKBQaQB3oopaYBRRRQAUYo6UUAHJopaSgA70dKKO9AAaBS0lAg70UUUAIaYRzTzTD1pAUNY/1C/WskdK19Xb9yB71kAmhgS3RyyivR7f9zpkIHQItebzj98vPUivRbtvL0hSOyLXQjJmtb3CzRqfapdwrmtOvHaHbk5JrRSZ0Xlqm47GnkVRvLofcBphvDgjNZ8s534Iz70mykiC7QMdxNO0rAdxVadyznnIqbT3EcpLcAioKLl420iq0jDHJp9/MkqAKeRVAn1NACyPxgVEaViOlNJoGITR2opKQCilpuaXNIBRyKM0naloAUGjNIKKYDs07NNooAeDxSimCleWOCNpJWCqoySe1AEu9YkLyMFV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)

La prova della classe alla lavagna: 17 diviso 2 più volte; i resti letti dal basso danno 10001. Nel byte diventa 00010001.

##### 5. Errori da evitare

1. **Leggere i resti dall'alto in basso.** Per 37 verrebbe `101001` = 41: sbagliato. Si legge **dal basso**.
2. **Dimenticare l'ultimo 1** (quello in fondo alla tabella).
3. **Mettere gli zeri a destra** invece che a sinistra: `10010100` = 148, un altro numero.

**Carta e penna:** rifai a mano la tabella del 37 sul tuo foglio, senza guardare. Se ti torna 100101, hai capito il metodo.

##### 6. Il riassunto in 4 parole

**Dividi** per 2 · scrivi il **resto** · leggi **dal basso** · metti gli **zeri davanti** fino a 8.

##### 7. Altri esempi svolti

Guarda come si fa con altri numeri. Copre la parte destra con la mano e prova da solo!

÷ 2resto603111

6

binario:

`110`

byte (8 cifre):

128064032016080412110

prova con le caselle: 4 + 2 = 6

÷ 2resto131603111

13

binario:

`1101`

byte (8 cifre):

128064032016081412011

prova con le caselle: 8 + 4 + 1 = 13

÷ 2resto251120603111

25

binario:

`11001`

byte (8 cifre):

128064032016181402011

prova con le caselle: 16 + 8 + 1 = 25

÷ 2resto500251120603111

50

binario:

`110010`

byte (8 cifre):

128064032116180402110

prova con le caselle: 32 + 16 + 2 = 50

÷ 2resto1000500251120603111

100

binario:

`1100100`

byte (8 cifre):

128064132116080412010

prova con le caselle: 64 + 32 + 4 = 100

÷ 2resto20001000500251120603111

200

binario:

`11001000`

byte (8 cifre):

128164132016081402010

prova con le caselle: 128 + 64 + 8 = 200

**Sfida per chi va veloce:** scrivi in binario la **tua età** e il **giorno** in cui sei nato.
Poi prova 255: viene `11111111`, tutto pieno. È il numero più grande che sta in un byte!

Corso Informatica — Classe 1 · Da decimale a binario · v1.2

### L12 08/10/2026 — Il treno blindato: le prime Pull Request

*Libro parziale: lezioni/2026-10-08_treno-pull-request.md*

#### Che cosa abbiamo fatto

1. **Quando:** 08/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Progetto del treno blindato: richieste al gioco con le Pull Request PR-1 (il mio cattivo), PR-2 (il mio paesaggio), PR-3 (un difetto), PR-4 (revisione).

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Una Pull Request è una richiesta di modifica: proponi un&#x27;idea per il gioco e chi lo cura decide se farla entrare.</p><p lang="ar" dir="rtl">طلب السحب (Pull Request) هو طلب تعديل: تقترح فكرة للعبة ومن يدير اللعبة يقرّر إدخالها.</p><p lang="zh">Pull Request 是修改请求：你给游戏提一个想法，负责人决定要不要加进去。</p></div>

#### La teoria e l'esercitazione

##### 00 A che cosa serve

*لماذا هذا الدليل · 这份指南有什么用*

1. Oggi il tuo personaggio entra nel gioco della classe. Ti serve la tua foto (solo la testa) e una frase su come vuoi il personaggio: il personaggio cartoonesco lo crea il prof.
   اليوم تدخل شخصيتك لعبة الصف. تحتاج صورتك (الرأس فقط) وجملة عن الشخصية التي تريدها: الأستاذ يصنع الشخصية الكرتونية.
   今天你的角色要进入全班的游戏。你需要你的照片（只要头）和一句话说明你想要什么样的角色：卡通角色由老师来做。

2. Usa solo una foto tua. Mai foto dei compagni o di altre persone.
   استعمل صورتك أنت فقط. لا تستعمل أبدًا صور زملائك أو أشخاص آخرين.
   只用你自己的照片。绝不用同学或别人的照片。

##### 01a Ritagliare la foto: dal telefono

*قصّ الصورة: من الهاتف · 裁剪照片：用手机*

1. Apri l'app delle foto: «Galleria» sui telefoni Android, «Foto» sull'iPhone.
   افتح تطبيق الصور: «Galleria» (المعرض) في هواتف أندرويد، «Foto» (الصور) في آيفون.
   打开相册应用：安卓手机是「Galleria」（图库），苹果手机是「Foto」（照片）。

2. Tocca la tua foto per aprirla.
   المس صورتك لفتحها.
   点你的照片，打开它。

3. In basso tocca la matita «Modifica».
   في الأسفل المس القلم «Modifica» (تعديل).
   在下面点铅笔图标「Modifica」（编辑）。

4. Tocca l'icona del ritaglio: un quadrato con le frecce agli angoli.
   المس أيقونة القص: مربع بأسهم في الزوايا.
   点裁剪图标：一个四角有箭头的方框。

5. Scegli la forma quadrata: «1:1» oppure «Quadrato».
   اختر الشكل المربع: «1:1» أو «Quadrato» (مربع).
   选正方形：「1:1」或「Quadrato」（正方形）。

6. Trascina gli angoli finché nel quadrato resta solo la tua testa.
   اسحب الزوايا حتى يبقى رأسك فقط داخل المربع.
   拖动四个角，直到方框里只剩下你的头。

7. In alto tocca «Salva copia» (o «Salva»). Fatto: la foto ritagliata è in Galleria.
   في الأعلى المس «Salva copia» (حفظ نسخة) أو «Salva» (حفظ). تمّ: الصورة المقصوصة في المعرض.
   在上面点「Salva copia」（另存一份）或「Salva」（保存）。好了：裁好的照片在相册里。

##### 01b Ritagliare la foto: dal PC della scuola

*قصّ الصورة: من حاسوب المدرسة · 裁剪照片：用学校的电脑*

1. Apri la tua foto sullo schermo: per esempio la foto del tuo profilo social, nel browser.
   افتح صورتك على الشاشة: مثلًا صورة حسابك في وسائل التواصل، داخل المتصفح.
   在屏幕上打开你的照片：比如在浏览器里打开你社交账号的头像。

2. Premi insieme tre tasti: Windows, Maiusc e S.
   اضغط معًا ثلاثة مفاتيح: Windows و Shift (Maiusc) و S.
   同时按三个键：Windows、Shift（Maiusc）和 S。

   ```
   Windows + Maiusc + S
   ```

3. Lo schermo diventa più scuro. Tieni premuto il tasto sinistro del mouse e disegna un quadrato intorno alla tua testa.
   تصبح الشاشة أغمق. اضغط زر الفأرة الأيسر باستمرار وارسم مربعًا حول رأسك.
   屏幕变暗。按住鼠标左键，在你的头周围画一个方框。

4. Lascia il mouse. In basso a destra compare un riquadro «Strumento di cattura»: cliccalo. La foto ritagliata si apre.
   اترك الفأرة. في الأسفل على اليمين يظهر مربع «Strumento di cattura» (أداة القص): انقر عليه. تُفتح الصورة المقصوصة.
   松开鼠标。右下角出现「Strumento di cattura」（截图工具）的小窗口：点它。裁好的照片就打开了。

##### 02 Salvare con il nome giusto

*الحفظ بالاسم الصحيح · 用正确的名字保存*

1. Il nome giusto è: classe, cognome e nome, che cosa è. Senza spazi e senza accenti. Per la foto:
   الاسم الصحيح هو: الصف، اسم العائلة والاسم، ما هي. بدون فراغات وبدون علامات. للصورة:
   正确的名字是：班级、姓和名、是什么。不要空格，不要重音符号。照片这样写：

   ```
   1INF_cognome-nome_foto.png
   ```

2. Al posto di «cognome-nome» scrivi i tuoi, per esempio 1INF_rossi-mario_foto.png.
   مكان «cognome-nome» اكتب اسمك، مثلًا 1INF_rossi-mario_foto.png.
   把「cognome-nome」换成你的姓和名，比如 1INF_rossi-mario_foto.png。

3. Sul PC: nella finestra «Strumento di cattura», in alto a destra clicca il dischetto «Salva».
   على الحاسوب: في نافذة «Strumento di cattura»، في الأعلى على اليمين انقر على القرص «Salva» (حفظ).
   在电脑上：在「Strumento di cattura」窗口里，点右上角的软盘图标「Salva」（保存）。

4. A sinistra clicca la cartella «Immagini».
   على اليسار انقر على مجلد «Immagini» (الصور).
   在左边点文件夹「Immagini」（图片）。

5. In basso clicca nella casella «Nome file», cancella e scrivi il nome giusto.
   في الأسفل انقر في خانة «Nome file» (اسم الملف)، امسح واكتب الاسم الصحيح.
   在下面点「Nome file」（文件名）框，删掉原来的，写正确的名字。

6. Clicca il bottone «Salva».
   انقر على زر «Salva» (حفظ).
   点「Salva」（保存）按钮。

7. Sul telefono il nome lo sceglie il telefono: va bene così.
   في الهاتف، الهاتف يختار الاسم: لا مشكلة.
   在手机上，名字由手机自己起：这样也可以。

##### 03 In alternativa: caricare la foto sul Modulo della consegna

*بديل: رفع الصورة إلى نموذج التسليم · 备选：把照片上传到交作业的表单*

1. Apri il compito su Classroom e clicca il Modulo «Consegna». Oppure apri questo indirizzo (scrivilo esattamente così):
   افتح الواجب في Classroom وانقر على النموذج «Consegna» (التسليم). أو افتح هذا العنوان (اكتبه تمامًا هكذا):
   在 Classroom 打开作业，点表单「Consegna」（提交）。或者打开这个网址（照原样输入）：

   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform
   ```

2. Se te lo chiede, entra con l'account della scuola.
   إذا طُلب منك، ادخل بحساب المدرسة.
   如果要求登录，用学校的账号登录。

3. Prima casella «Cosa consegni?»: scrivi foto.
   الخانة الأولى «Cosa consegni?» (ماذا تسلّم؟): اكتب foto.
   第一个框「Cosa consegni?」（你交什么？）：写 foto。

   ```
   foto
   ```

4. Seconda casella: scrivi il mio personaggio.
   الخانة الثانية: اكتب il mio personaggio.
   第二个框：写 il mio personaggio。

   ```
   il mio personaggio
   ```

5. Clicca il bottone «Aggiungi file» (ha una freccia in su).
   انقر على زر «Aggiungi file» (إضافة ملف)، عليه سهم إلى الأعلى.
   点「Aggiungi file」（添加文件）按钮，上面有一个向上的箭头。

6. Nella finestra che si apre clicca il bottone blu «Sfoglia».
   في النافذة التي تُفتح انقر على الزر الأزرق «Sfoglia» (تصفّح).
   在打开的窗口里点蓝色按钮「Sfoglia」（浏览）。

7. Scegli il tuo file (1INF_cognome-nome_foto.png) e clicca «Apri».
   اختر ملفك (1INF_cognome-nome_foto.png) وانقر «Apri» (فتح).
   选你的文件（1INF_cognome-nome_foto.png），点「Apri」（打开）。

8. Se compare, clicca «Carica».
   إذا ظهر، انقر «Carica» (رفع).
   如果出现，点「Carica」（上传）。

9. In basso clicca il bottone viola «Invia». Compare «Ricevuto»: fatto!
   في الأسفل انقر على الزر البنفسجي «Invia» (إرسال). يظهر «Ricevuto» (تم الاستلام): تمّ!
   在下面点紫色按钮「Invia」（发送）。出现「Ricevuto」（收到了）：完成！

### L13 09/10/2026 — Versioni e Git: la storia del nostro gioco

*Libro parziale: lezioni/2026-10-09_versioni-git-treno.md*

#### Che cosa abbiamo fatto

1. **Quando:** 09/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** La storia del gioco del treno: numeri delle versioni, rami, fork, merge e changelog; quiz «Versioni e Git» e compito unico.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il numero di versione dice quanto è cambiato il gioco. Un ramo è una strada di lavoro; il merge unisce i rami.</p><p lang="ar" dir="rtl">رقم النسخة يقول كم تغيّرت اللعبة. الفرع طريق عمل، والدمج (merge) يجمع الفروع.</p><p lang="zh">版本号说明游戏改了多少。分支是一条工作路线，合并（merge）把分支合在一起。</p></div>

#### La teoria e l'esercitazione

Testo per la tua AI: chiedile di spiegarti ogni parte nella tua lingua.

##### 01 Che cosa facciamo oggi

1. Carta e penna sul banco: oggi si disegna il grafo a mano.
   1.1 العربية: ضع الورقة والقلم على الطاولة: اليوم نرسم الرسم البياني باليد.
   1.2 中文：桌上放好纸和笔：今天我们用手画版本图。
2. VINCI SUBITO (5 minuti). Apri il grafo, clicca il primo pallino BLU (v0.0) e premi il bottone verde «Apri questa versione»: gioca 30 secondi. Poi torna al grafo, clicca il pallino VIOLA (v2.0) e gioca ancora. Sul foglio scrivi 2 cose che sono cambiate.
   2.1 العربية: اربح فوراً: افتح الرسم البياني، اضغط أول دائرة زرقاء (v0.0) ثم الزر الأخضر، والعب 30 ثانية. ثم اضغط الدائرة البنفسجية (v2.0) والعب. اكتب على الورقة شيئين تغيّرا.
   2.2 中文：马上赢：打开版本图，点第一个蓝色圆点（v0.0），按绿色按钮，玩30秒。再点紫色圆点（v2.0）再玩。在纸上写两样改变了的东西。
3. Leggi le 8 parole del grafo (tabella qui sotto) e copiale sul foglio con la traduzione nella tua lingua.
   3.1 العربية: اقرأ الكلمات الثماني (الجدول أدناه) وانسخها على الورقة مع الترجمة بلغتك.
   3.2 中文：读下面表格里的8个词，把它们和你的语言的翻译一起抄在纸上。
4. Clicca i pallini del TUO ramo (arancione per la 1INF, blu per la 2INF): leggi «Cosa è cambiato e perché». Trova la versione dove c'è una cosa fatta dalla tua classe.
   4.1 العربية: اضغط دوائر فرعك (برتقالي لـ 1INF، أزرق لـ 2INF) واقرأ ماذا تغيّر ولماذا. ابحث عن النسخة التي فيها شيء صنعه صفك.
   4.2 中文：点你们分支的圆点（1INF 是橙色，2INF 是蓝色），读「改变了什么，为什么」。找到有你们班做的东西的版本。
5. SCHEMA A MANO: disegna sul foglio un grafo con 3 colori: il ramo principale, un fork e un ramo di lavoro che rientra con un merge. Sotto ogni pallino scrivi il numero di versione.
   5.1 العربية: ارسم باليد رسماً بثلاثة ألوان: الفرع الرئيسي، نسخة fork، وفرع عمل يعود بـ merge. اكتب رقم النسخة تحت كل دائرة.
   5.2 中文：手画图：用三种颜色画：主分支、一个 fork、一个用 merge 合并回来的工作分支。在每个圆点下写版本号。
6. PROVA DEL NOVE: spiega a voce al compagno, con parole tue, cos'è un merge e perché la versione Godot si chiama 2.0 e non 1.2.
   6.1 العربية: اشرح لزميلك بكلماتك: ما هو merge، ولماذا نسخة Godot اسمها 2.0 وليس 1.2.
   6.2 中文：用你自己的话给同学讲：什么是 merge，为什么 Godot 版本叫 2.0 而不是 1.2。

Indirizzo del grafo (scrivilo esattamente così):

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/
```

![Il grafo delle versioni](../../docs/lezione-versioni/grafo-20261009.png)

##### 02 Le 8 parole del grafo

| Italiano | العربية | 中文 | Nel nostro gioco |
|---|---|---|---|
| versione (commit) | نسخة (حفظ commit) | 版本（提交 commit） | Ogni pallino del grafo: v0.3, v1.1, v2.0… |
| ramo (branch) | فرع (branch) | 分支（branch） | Una linea del grafo: il gioco cresce lungo il ramo. |
| fork (copia) | نسخة مستقلة (fork) | 复刻（fork，复制） | La 1INF copia il gioco della 2INF e lo fa crescere per conto suo. |
| Pull Request (proposta di modifica) | اقتراح تعديل (Pull Request) | 修改建议（Pull Request） | Il vostro Documento su Classroom: «il mio cattivo si chiama…». |
| merge (unione) | دمج (merge) | 合并（merge） | Il ramo «immagini» rientra nel ramo della 1INF. |
| versione minor (1.1, 1.2…) | إصدار صغير (1.1، 1.2…) | 小版本（1.1、1.2……） | Piccole aggiunte: un cattivo nuovo, un cielo nuovo. |
| versione major (2.0) | إصدار كبير (2.0) | 大版本（2.0） | Cambia una cosa grossa: il motore diventa Godot. |
| release (versione pubblicata) | إصدار منشور (release) | 发布（release） | La versione che tutti possono giocare con un link. |

##### 03 Perché

1. **Perché i numeri cambiano così.** v0.x = le prove, prima della versione stabile (la 2INF ha fatto 12 prove: v0.0 → v0.11). 1.0 = la prima versione «vera» di un ramo (il fork della 1INF e della 3INF). 1.1, 1.2 = versioni MINOR: piccole aggiunte (un cattivo, un cielo). 2.0 = versione MAJOR: cambia una cosa grossa (il motore Godot), il primo numero sale e il secondo riparte da 0.
   1.1 العربية: v0.x = تجارب. 1.0 = أول نسخة حقيقية. 1.1، 1.2 = إضافات صغيرة (minor). 2.0 = تغيير كبير (major): الرقم الأول يزيد والثاني يعود إلى 0.
   1.2 中文：v0.x = 试验。1.0 = 第一个真正的版本。1.1、1.2 = 小的增加（minor）。2.0 = 大的改变（major）：第一个数字加一，第二个数字回到 0。
2. **Perché si fanno i rami.** Per provare una cosa nuova SENZA rompere il gioco che funziona. Il prof ha fatto la funzione «immagini della classe» su un ramo a parte; quando funzionava l'ha unita (merge) al ramo della 1INF. Nelle aziende si lavora sempre così: ognuno sul suo ramo, poi Pull Request, controllo e merge.
   2.1 العربية: لنجرّب شيئاً جديداً دون أن نكسر اللعبة التي تعمل. في الشركات يعمل كل واحد على فرعه، ثم Pull Request، ثم مراجعة، ثم merge.
   2.2 中文：为了试新东西而不弄坏能玩的游戏。在公司里大家都这样工作：每人在自己的分支上，然后 Pull Request、检查、合并（merge）。
3. **Perché Godot (v2.0).** Godot è un motore vero per videogiochi, gratis e portabile (non si installa), usato anche nel lavoro. I vostri cattivi ci sono ancora: stanno nei file di dati (cattivi.json), uguali a prima. Ponte da Lazarus: Lazarus REAGISCE (aspetta un clic), Godot PULSA (_process gira da solo circa 60 volte al secondo).
   3.1 العربية: Godot محرك حقيقي للألعاب، مجاني ولا يحتاج تثبيت. أشراركم ما زالوا موجودين في ملف البيانات cattivi.json. Lazarus ينتظر النقرة، Godot ينبض 60 مرة في الثانية.
   3.2 中文：Godot 是真正的游戏引擎，免费、不用安装。你们的坏人还在数据文件 cattivi.json 里。Lazarus 等待点击，Godot 每秒跳动约60次。

##### 04 La storia, ramo per ramo

1. **2INF — Il treno blindato (HTML), il ramo principale** — العربية: ١٢ نسخة من v0.0 إلى v0.11: من الفكرة الأولى إلى اللعبة الكاملة. · 中文：从 v0.0 到 v0.11 共12个版本：从第一个想法到完整的游戏。
   1.1 **v0.0 — Prima idea: il finestrino laterale.** Il treno visto dal finestrino di lato: paesaggio che scorre, cattivi che sbucano da dietro alberi e case, vetro da 5 colpi. Poi la classe ha disegnato alla lavagna la vista dalla cabina.
   1.2 **v0.1-alfa — Demo del prof sul progetto della lavagna.** Vista dalla cabina lungo i binari (progetto della classe), cattivi da finestre, alberi e barili, facce della classe e copertina disegnata con l'IA, tachimetro, installabile come app. Da qui la classe corregge il tiro.
   1.3 **v0.2 — I personaggi della squadra PERSONAGGI.** Quattro personaggi disegnati con l'IA (tre agenti e il Boss dei cattivi), bottone «I personaggi», le loro facce nel gioco. Prima modifica arrivata dalla classe.
   1.4 **v0.3 — Più lento: richiesta della squadra TEST QUALITÀ.** Prima richiesta di modifica consegnata su Classroom dalla Triade: «il gioco va troppo veloce». Velocità del treno da 1 a 0,7.
   1.5 **v0.4 — Audit degli investitori: personaggi nascosti che escono.** Il cattivo è un personaggio intero nascosto dietro gli oggetti che esce di lato, più grande; treno al minimo (0,5); tolte 2 foto senza faccia.
   1.6 **v0.5 — Le regole della squadra MOTORE FISICA (Pull Request #104).** Prima Pull Request vera (#104) del capo MOTORE FISICA: cattivi sparano dopo 3 secondi, 100 punti per cattivo, velocità 0,5. Corretto 0,5 → 0.5 (in JSON i decimali vogliono il punto).
   1.7 **v0.6 — Il bosco bruciato della squadra SCENARI.** Richiesta SCENARI: cielo rosso cupo, alberi bruciati e rottami fumanti vicino ai binari. Richiesta PERSONAGGI: il cattivo dice «Hahahahaha, perdente!» quando spara.
   1.8 **v0.7 — Omini interi che escono dal nascondiglio.** Indicazione del prof: omini interi (testa, busto, braccia, gambe, arma) al posto dei cerchietti; si alzano da dietro il nascondiglio ed escono di lato con un «!»; quando li colpisci cadono.
   1.9 **v0.8 — Mimetica, facce senza cerchio e il fucile d'assalto.** Indicazioni del prof: facce senza cerchio (solo la faccia), barretta del tempo sopra la testa, omini in mimetica, l'Agente Speciale con il fucile d'assalto.
   1.10 **v0.9 — Teste in proporzione.** Indicazione del prof: la testa degli omini lontani era troppo grossa (misura minima fissa); ora è sempre in proporzione al corpo.
   1.11 **v0.10 — I migliori punteggi.** Indicazione del prof: classifica dei primi 10 con soprannome a fine partita, mostrata nella schermata iniziale; record della classe da record-classe.json.
   1.12 **v0.11 — I punteggi si salvano sempre.** Difetto segnalato dal prof: il punteggio ora si salva da solo a fine partita, il soprannome si conferma anche con Invio; il gioco chiede sempre alla rete la versione nuova.
2. **3INF — fork (copia) del gioco della 2INF** — العربية: صف 3INF نسخ لعبة 2INF (fork) وأضاف أشراراً ومناظر جديدة. · 中文：3INF 班复制（fork）了 2INF 的游戏，并加入了新的坏人和风景。
   2.1 **v1.0 — Il fork della 3INF: traversine di legno e nuvole.** La 3INF fa la sua copia (fork) del gioco della 2INF (v0.11). Traversine di legno con venature e nodi, nuvole nel cielo.
   2.2 **v1.1 — Black Panter (PR #1 e #2, SCENARI).** Pull Request #1 (PC 18) e #2 (PC 17) dalla consegna su Classroom: il cattivo Black Panter con la mimetica nera e argento, esce da una porta, dice «Yahuu!».
   2.3 **v1.2 — Montagna, tempo che peggiora, Travor.** PR #4 Dani e #5 Ale (SCENARI): si parte dalla montagna, cielo sereno, il tempo peggiora a ogni livello. PR #6 Tomas (PERSONAGGI): il cattivo Travor, mimetica grigia.
   2.4 **v1.3 — Cespugli, greggi, armi diverse, nuovi cattivi.** PR #8 Mirko: cespugli e armi diverse; #13 Dani e #14 Ale: greggi in montagna; #10 Ariel D. e #11 Tomas: Travor e il protagonista Nash; #12 Eric: Franciscos.
   2.5 **v1.4 — Treno più veloce, Nash, Dylan, cielo che cambia subito.** PR #17 Noah: velocità 2; #15 Ariel D.: Nash; #19 Emmanuel: Dylan; #18 Eric: Franciscos azzurro e bianco; #20 Dani e #21 Ale: difetto del cielo sistemato.
3. **1INF — fork (copia) del gioco della 2INF** — العربية: صفكم 1INF نسخ اللعبة وأضاف أشراركم وألوان السماء. · 中文：你们 1INF 班复制了游戏，加入了你们的坏人和天空的颜色。
   3.1 **v1.0 — Il fork della 1INF.** Copia (fork) del gioco della 2INF alla versione v0.11. Da qui partono le Pull Request della 1INF.
   3.2 **v1.1 — I primi cattivi e i cieli della 1INF.** Pull Request accettate: cattivi Hidra (Giexther A.), EI (Yinlin L.), Mister Bar Berry (Matteo A.); cielo arancione in montagna (Giexther A.), cielo di guerra nel bosco (Yinlin L.), cielo viola in città (Wesley J.).
4. **Ramo di lavoro del prof: «immagini della classe» → merge nella 1INF** — العربية: الأستاذ جرّب ميزة جديدة في فرع منفصل، ثم دمجها (merge) في فرع 1INF. · 中文：老师在一个单独的分支上试了新功能，然后把它合并（merge）到 1INF 的分支。
   4.1 **immagini — Nuova funzione su un ramo separato.** Il prof prova una cosa nuova su un RAMO a parte, così il gioco che funziona non si rompe: cartelle per le immagini (cattivi, paesaggi, difetti, revisioni), galleria con i nomi, foto prese da sole dalle consegne di Classroom. Quando funziona: MERGE (unione) nel ramo della 1INF.
5. **1INF su Godot — versione 2.0 (major)** — العربية: نفس اللعبة لكن بمحرك Godot: تغيير كبير، لذلك الرقم يصبح 2.0. · 中文：同一个游戏，但是用 Godot 引擎做的：大变化，所以版本号变成 2.0。
   5.1 **v2.0 — Il treno su Godot.** Stesso gioco della 1INF v1.1 (cattivi Hidra, EI, Mister Bar Berry e i cieli della 1INF), ma rifatto con il motore Godot 4.7 ed esportato per il browser. È cambiato il motore, cioè una cosa grossa: per questo il numero passa da 1.x a 2.0 (versione major).

### L14 13/10/2026 — La mia prima Pull Request

*Libro parziale: lezioni/2026-10-13_prima-pull-request.md*

#### Che cosa abbiamo fatto

1. **Quando:** 13/10/2026, Laboratorio.
2. **Argomenti:** Pull Request al gioco del treno (versioni v2.x): le richieste che entrano nel gioco.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Ognuno manda la sua prima Pull Request: la richiesta accettata entra nella nuova versione del gioco.</p><p lang="ar" dir="rtl">يرسل كل طالب أول طلب سحب له: الطلب المقبول يدخل في النسخة الجديدة من اللعبة.</p><p lang="zh">每个人提交第一个 Pull Request：被接受的请求会进入游戏的新版本。</p></div>

#### La teoria e l'esercitazione

أول Pull Request لي

我的第一个 Pull Request

1INF · 13/10/2026

Come sta andando la lezione · كيف يسير الدرس · 课堂进展

I votiالعلامات · 分数Il backlogقائمة الاقتراحات · 建议列表Il monitor della lezioneمراقبة الدرس · 课堂监控Cosa è cambiato oggi nel giocoما الجديد في اللعبة · 游戏里的新变化La classificaالترتيب · 排行榜Valutazione dei singoli (solo prof)تقييم كل طالب (للأستاذ) · 个人评价（老师）

Hai scritto la Pull Request nel Documento? Mandami il Documento:

1. Premi il bottone verde.

   اضغط الزر الأخضر.

   按绿色按钮。

   Manda il tuo Documento
2. Prima casella: scrivi **file**.

   الخانة الأولى: اكتب file.

   第一个格子：写 file。
3. Seconda casella: scrivi **file**.

   الخانة الثانية: اكتب file.

   第二个格子：写 file。
4. Premi «Aggiungi file» e scegli il tuo Documento.

   اضغط «Aggiungi file» (إضافة ملف) واختر مستندك.

   按「Aggiungi file」（添加文件），选择你的文档。
5. Premi «Invia».

   اضغط «Invia» (إرسال).

   按「Invia」（发送）。

##### Domanda in più · solo per Yinlin L. (PC 24)

**Yinlin，这是 Nicola 老师只问你的一个问题。不是作业，不打分。**

早上你进学校的时候，在院子里推着自行车走。你为什么这样做？为什么不一直骑到自行车停车的地方？

1. 按绿色按钮。
2. 回答 · Rispondi
3. 第一个格子写：`domanda`
4. 第二个格子写你的回答。可以用中文写。
5. 按紫色按钮「Invia」（发送）。

Per Yinlin: al mattino entri a scuola spingendo la bici nel cortile. Perché? Perché non arrivi pedalando fino al parcheggio delle bici? Domanda del prof, non è un compito e non ha voto.

##### Passo 1 · Gioca

1. Premi il bottone verde.

   اضغط الزر الأخضر.

   按绿色按钮。
2. Gioca il treno
3. Gioca 3 minuti.

   العب 3 دقائق.

   玩3分钟。
4. Chiudi la scheda del gioco.

   أغلق صفحة اللعبة.

   关掉游戏的标签页。

##### Passo 2 · Il fork

1. Il prof ha copiato il vostro treno.

   الأستاذ نسخ قطاركم.

   老师复制了你们的火车游戏。
2. La copia si chiama **fork**.

   النسخة تسمى **fork**.

   副本叫做 **fork**。
3. Il treno vero resta al sicuro.

   القطار الأصلي يبقى بأمان.

   原来的火车是安全的。

Treno v2.1.3→fork 1INF

##### Passo 3 · Scegli una riga

1. Leggi la tabella.

   اقرأ الجدول.

   读这个表格。
2. Scegli **una** riga da cambiare.

   اختر سطراً **واحداً** لتغييره.

   选**一**行来改。

| Riga · السطر · 行 | Adesso · الآن · 现在 |
| --- | --- |
| Colpi che il vetro regge عدد الضربات التي يتحملها الزجاج  玻璃能挨几下 | 5 |
| Velocità del treno سرعة القطار  火车的速度 | 0.5 |
| Secondi prima che il cattivo spari الثواني قبل أن يطلق الشرير النار  坏人开枪前的秒数 | 3 |
| Cattivi in ogni livello عدد الأشرار في كل مستوى  每一关的坏人数量 | 10 |
| Punti per ogni cattivo النقاط لكل شرير  每个坏人的分数 | 100 |
| Frase del cattivo جملة الشرير  坏人说的话 | Hahahahaha, perdente! |
| Frase quando vinci جملة عندما تفوز  你赢的时候的话 | Grande! Hai portato il treno in salvo. |

##### Passo 4 · Pensa la tua Pull Request

1. Pensa il valore nuovo.

   فكّر في القيمة الجديدة.

   想一个新的值。
2. Pensa perché.

   فكّر لماذا.

   想一想为什么。

Esempio · مثال · 例子

|  |  |
| --- | --- |
| Riga السطر  行 | Colpi che il vetro regge |
| Valore nuovo القيمة الجديدة  新的值 | 8 |
| Perché لماذا  为什么 | Così il gioco dura di più. هكذا تدوم اللعبة أكثر.  这样游戏更久。 |

Una Pull Request è una proposta. Il prof dice SÌ o NO. · Pull Request هو اقتراح. الأستاذ يقول نعم أو لا. · Pull Request 就是一个建议。老师说是或不。

##### Passo 5 · Manda

1. Premi il bottone verde.

   اضغط الزر الأخضر.

   按绿色按钮。
2. Scrivi la tua Pull Request
3. Nella prima casella scrivi:

   في الخانة الأولى اكتب بالحروف اللاتينية:

   在第一个格子里用拉丁字母写：
4. `pull request`
5. Nella seconda casella scrivi: la riga, il valore nuovo, perché.

   في الخانة الثانية اكتب: السطر، القيمة الجديدة، لماذا.

   在第二个格子里写：哪一行、新的值、为什么。
6. Puoi scrivere nella tua lingua.

   يمكنك الكتابة بلغتك.

   你可以用你的语言写。
7. Premi il bottone viola «Invia».

   اضغط الزر البنفسجي «Invia» (إرسال).

   按紫色按钮「Invia」（发送）。

Fatto! La tua idea arriva al prof.

تم! فكرتك تصل إلى الأستاذ.

完成！你的想法会送到老师那里。

Hai un'altra idea? Torna al Passo 5. · عندك فكرة أخرى؟ ارجع إلى الخطوة 5. · 还有别的想法？回到第5步。

### L15 14/10/2026 — La talpa e il mio personaggio

*Libro parziale: lezioni/2026-10-14_talpa.md*

#### Che cosa abbiamo fatto

1. **Quando:** 14/10/2026, Laboratorio.
2. **Argomenti:** Il gioco della talpa e la classifica; il proprio personaggio (foto e descrizione); Pull Request e merge spiegati con parole proprie.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Creiamo il nostro personaggio e lo mandiamo nel gioco della talpa con una richiesta.</p><p lang="ar" dir="rtl">نصنع شخصيتنا ونرسلها إلى لعبة الخُلد بطلب.</p><p lang="zh">我们创造自己的角色，并通过请求把它加入打地鼠游戏。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Un'app di tutta la classe

<div class="scheda">Tutta la classe lavora su <b>un solo programma</b>: il gioco della talpa. Ognuno porta un pezzo: il suo personaggio. Regola: <b>si aggiunge, non si cancella</b> il lavoro degli altri.<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em">كل الصف يعمل على <b>برنامج واحد</b>: لعبة الخُلد. كل واحد يجلب قطعة: شخصيته. القاعدة: <b>نضيف ولا نمسح</b> عمل الآخرين.</div><div style="color:#5d6878">全班一起做<b>同一个程序</b>：打地鼠游戏。每个人带来一部分：自己的角色。规则：<b>只添加，不删除</b>别人的成果。</div></div>

##### 2. Pull Request e Merge

<div class="scheda">La <b>Pull Request</b> è una <b>richiesta</b>: «ecco il mio personaggio, mettilo nel gioco». Il prof la controlla e la unisce al gioco: questo si chiama <b>merge</b> (unione).<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em"><b>Pull Request</b> هو <b>طلب</b>: «هذه شخصيتي، ضعها في اللعبة». الأستاذ يتحقق ويدمجها في اللعبة: اسمه <b>merge</b> (دمج).</div><div style="color:#5d6878"><b>Pull Request</b> 是一个<b>请求</b>：「这是我的角色，把它放进游戏」。老师检查后把它合并进游戏：这叫 <b>merge</b>（合并）。</div></div>

##### 3. Versioni, backlog, changelog

<div class="scheda">Ogni modifica fa nascere una <b>versione nuova</b>: v1.1, v1.2… Il <b>backlog</b> è la fila delle richieste. Il <b>changelog</b> è il diario: che cosa è cambiato in ogni versione e chi l'ha chiesto.<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em">كل تعديل يصنع <b>نسخة جديدة</b>: v1.1، v1.2… <b>backlog</b> هو قائمة الطلبات. <b>changelog</b> هو المذكرة: ما الذي تغيّر في كل نسخة ومن طلبه.</div><div style="color:#5d6878">每个修改产生一个<b>新版本</b>：v1.1、v1.2……<b>backlog</b> 是请求的队列。<b>changelog</b> 是日记：每个版本改了什么、是谁要求的。</div></div>

##### 4. Ritagliare e copiare una foto

<div class="scheda"><b>Ritagliare</b> = tenere solo la parte che serve (la testa). Sul PC: <b>Windows + Maiusc + S</b> e disegni un quadrato. <b>Copiare</b> un'immagine: tasto destro → «Copia immagine». <b>Incollare</b>: <b>Ctrl + V</b>.<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em"><b>القص</b> = نحتفظ بالجزء المهم فقط (الرأس). في الحاسوب: <b>Windows + Shift + S</b> وترسم مربعًا. <b>نسخ</b> صورة: الزر الأيمن ← «Copia immagine». <b>اللصق</b>: <b>Ctrl + V</b>.</div><div style="color:#5d6878"><b>裁剪</b>＝只留下需要的部分（头）。在电脑上：<b>Windows + Shift + S</b>，然后画一个方框。<b>复制</b>图片：右键 →「Copia immagine」。<b>粘贴</b>：<b>Ctrl + V</b>。</div></div>

##### 5. Salvare e caricare

<div class="scheda"><b>Salvare con nome</b>: scegli la cartella (Immagini) e un nome chiaro, senza spazi: 1INF_cognome-nome_foto.png. <b>Caricare</b> sul Modulo: «Aggiungi file» → «Sfoglia» → scegli il file → «Apri» → «Invia».<div dir="rtl" style="color:#5d6878;font-family:Amiri,serif;font-size:1.05em"><b>الحفظ باسم</b>: اختر المجلد (الصور) واسمًا واضحًا بدون فراغات: 1INF_cognome-nome_foto.png. <b>الرفع</b> إلى النموذج: «Aggiungi file» ← «Sfoglia» ← اختر الملف ← «Apri» ← «Invia».</div><div style="color:#5d6878"><b>另存为</b>：选文件夹（图片）和一个清楚、没有空格的名字：1INF_cognome-nome_foto.png。<b>上传</b>到表单：「Aggiungi file」→「Sfoglia」→ 选文件 →「Apri」→「Invia」。</div></div>


### L16 15/10/2026 — Verifica: versioni e changelog

*Libro parziale: lezioni/2026-10-15_verifica-versioni.md*

#### Che cosa abbiamo fatto

1. **Quando:** 15/10/2026, 1 ora.
2. **Argomenti:** Verifica «Versioni e changelog» (versioni, changelog, Pull Request, merge), consegnata online.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Ripasso e verifica: versioni, changelog (l&#x27;elenco delle novità), Pull Request e merge.</p><p lang="ar" dir="rtl">مراجعة واختبار: النسخ، سجل التغييرات (changelog)، طلب السحب والدمج.</p><p lang="zh">复习和测验：版本、更新日志（changelog）、Pull Request 和合并。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Che cos'è una versione

<div class="scheda">Una <b>versione</b> è un salvataggio del programma con un <b>numero</b> e una riga che dice <b>cosa cambia</b>. Così si sa sempre quale versione si sta usando, e se una modifica rompe tutto si può tornare a una versione di prima.</div>

##### 2. Major e minor

<div class="scheda">Se cambia il numero <b>dopo il punto</b> (v0.30 → v0.31, oppure v1.4 → v1.5) è un passo <b>piccolo</b>: <b>minor</b>. Se cambia il <b>primo numero</b> (v1.9 → v2.0) è un cambio <b>grande</b>: <b>major</b>, per esempio un motore nuovo. Dopo un major si riparte dallo zero (v2.0, v2.1…).</div>

##### 3. Il changelog

<div class="scheda">Il <b>changelog</b> è il <b>registro di tutte le modifiche</b>, versione per versione: per ognuna c'è il numero e cosa è cambiato. Serve a ricordare la storia del programma e a far capire agli altri cosa è stato fatto.</div>


### L17 16/10/2026 — Monta il PC: assemblaggio in laboratorio

*Libro parziale: lezioni/2026-10-16_assemblaggio-pc.md*

#### Che cosa abbiamo fatto

1. **Quando:** 16/10/2026, Laboratorio.
2. **Argomenti:** Montaggio del PC e sistema operativo: la gara di assemblaggio, la sfida lampo sui pezzi e il test di ripasso.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Si monta il PC in ordine: processore, RAM, scheda madre nel case, alimentatore, disco, poi il sistema operativo.</p><p lang="ar" dir="rtl">نركّب الحاسوب بالترتيب: المعالج، الذاكرة، اللوحة الأم في الصندوق، مزوّد الطاقة، القرص، ثم نظام التشغيل.</p><p lang="zh">按顺序装电脑：处理器、内存、主板装进机箱、电源、硬盘，然后装操作系统。</p></div>

#### La teoria e l'esercitazione

Bozza da rivedere col docente (FASE 1: teoria). Linguaggio semplice, legato al fare.

---

##### 1. Che cosa facciamo oggi

1. Apriamo un PC, togliamo i pezzi e li rimettiamo: capiamo **dove va ogni cosa**.
2. Mettiamo il **sistema operativo** (Windows 10) da una chiavetta: facciamo «nascere» il PC.
3. Creiamo **due utenti** e guardiamo gli **strumenti** per gestire il computer.

##### 2. Sicurezza prima di tutto (hardware)

1. Spegni e **togli il cavo della corrente** prima di aprire.
2. **Tocca il metallo** del case: così scarichi l'elettricità del tuo corpo, che potrebbe rovinare i pezzi.
3. Non forzare: se un pezzo non entra, è nel **verso sbagliato**.
4. Le **viti** stanno tutte in una ciotola, così non si perdono.

##### 3. I pezzi e l'ordine di montaggio

Già sappiamo a cosa serve ogni componente (l'abbiamo visto col preventivo). Oggi conta **l'ordine**:

1. **Alimentatore** (dà la corrente a tutto).
2. **Scheda madre** (la base dove si attacca tutto).
3. **CPU** e il suo **dissipatore** (il cervello e la sua ventola).
4. **RAM** (la memoria di lavoro): si inserisce fino al «clic».
5. **Disco** SSD o hard disk (dove restano i dati).
6. **Cavi**: corrente ai pezzi, pulsante di accensione, dati del disco.

Alla fine: si chiude, si attacca corrente, monitor, tastiera e mouse, e si accende.

##### 4. Il sistema operativo: far «nascere» il PC

1. Un PC appena montato è «vuoto»: non sa fare niente senza un **sistema operativo**.
2. Il **sistema operativo** (Windows, ma anche Linux) è il programma che fa funzionare tutto: schermo, file, programmi.
3. La **chiavetta avviabile** contiene Windows pronto da installare.
4. All'accensione diciamo al PC di **partire dalla chiavetta** (menu di avvio), poi seguiamo i passi sullo schermo.
5. Alla fine il PC parte da solo con Windows: è «nato».

##### 5. Due utenti: amministratore e utente normale

1. Un **utente** è un profilo con il suo nome e le sue cose.
2. L'**amministratore** può cambiare tutto (installare, cancellare, creare altri utenti): è «il capo».
3. L'**utente normale** usa il PC ma non può toccare le cose importanti: così non combina guai.
4. Creiamo **due utenti**: uno amministratore e uno normale, con un nome scelto da loro.

##### 6. Gli strumenti per gestire il computer

Guardiamo a cosa servono (senza cambiare niente di pericoloso):

1. **Gestione dispositivi**: l'elenco dei pezzi che Windows riconosce (se un pezzo ha un problema, qui si vede).
2. **Gestione disco**: lo spazio del disco e come è diviso.
3. **Gestione attività** (Ctrl+Shift+Esc): i programmi aperti e quanto «lavorano».
4. **Account utente**: dove si creano e si gestiscono gli utenti.

##### 7. Saperlo spiegare (la prova del nove)

Con parole tue, sai dire:

1. Perché si tocca il metallo del case prima di montare?
2. A cosa serve il sistema operativo?
3. Che differenza c'è tra amministratore e utente normale?
</content>

#### Le schede della lezione

##### 1. Il cervello e la memoria

<div class="scheda">La <b>CPU</b> (processore) è il <b>cervello</b>: fa i calcoli. La <b>RAM</b> è la <b>memoria veloce di lavoro</b>: si infila negli slot lunghi della scheda madre. L'<b>hard disk</b> (o SSD) <b>conserva i tuoi file</b> (foto, giochi): non si cancella quando spegni.</div>

##### 2. Corrente e raffreddamento

<div class="scheda">L'<b>alimentatore</b> dà la <b>corrente</b> a tutti i pezzi. La CPU si scalda, quindi sopra ha il <b>dissipatore</b> + la <b>ventola</b> che la <b>raffreddano</b> buttando fuori l'aria calda.</div>

##### 3. Dove si monta e come si collega

<div class="scheda">La <b>scheda madre</b> è la base dove si <b>montano tutti i pezzi</b>. Il <b>lettore DVD</b> e l'<b>hard disk</b> stanno sulla <b>slitta</b> e si collegano alla scheda madre col <b>cavo SATA</b>.</div>


### L18 20/10/2026 — Quanto pesa un file, quanto va veloce la rete

*Libro parziale: lezioni/2026-10-20_byte-velocita.md*

#### Che cosa abbiamo fatto

1. **Quando:** 20/10/2026, 1 ora, Tecnologia.
2. **Argomenti:** Bit e byte, KB, MB, GB, TB; la velocità in Mbps, b piccola (bit) e B grande (byte); tempo di download, streaming, Wi-Fi o cavo.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">La rete si misura in Mbps (megabit al secondo). 1 byte = 8 bit, quindi 100 Mbps = 12,5 MB al secondo.</p><p lang="ar" dir="rtl">تُقاس الشبكة بـ Mbps (ميغابِت في الثانية). ١ بايت = ٨ بِت، إذن 100 Mbps = 12.5 ميغابايت في الثانية.</p><p lang="zh">网速用 Mbps（每秒兆比特）表示。1 字节 = 8 比特，所以 100 Mbps = 每秒 12.5 MB。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Il bit: 0 oppure 1 · ١. البِت: صفر أو واحد · 1. 比特：0 或 1

<div class="scheda">Il computer capisce solo <b>due cose</b>: corrente <b>sì</b> o corrente <b>no</b>, come una lampadina accesa o spenta. Le scriviamo <b>1</b> e <b>0</b>.<br>Un solo 0 o 1 si chiama <b>bit</b>. È il pezzo più piccolo di informazione. Lo avete già visto con il <b>binario</b>: 1010 sono 4 bit.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الحاسوب يفهم شيئين فقط: 1 أو 0، مثل مصباح مضاء أو مطفأ. الرقم الواحد اسمه «بِت».</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">电脑只懂两种状态：1 或 0，就像灯开或关。一个 0 或 1 叫做“比特”（bit）。</span></div>

##### 2. Il byte: 8 bit insieme · ٢. البايت: ٨ بِت معًا · 2. 字节：8 个比特

<div class="scheda">Un bit da solo dice poco. <b>8 bit insieme</b> fanno un <b>byte</b>. Con un byte il computer scrive <b>una lettera</b>: la A è 01000001.<br>Quindi: <b>1 byte = 8 bit = una lettera</b>.<br>Il bit si scrive con la <b>b piccola</b>, il byte con la <b>B grande</b>. Ricordatelo: serve dopo, per la velocità.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">٨ بِت = ١ بايت = حرف واحد. البِت يُكتب b صغيرة، والبايت B كبيرة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">8 个比特 = 1 个字节 = 一个字母。比特写小写 b，字节写大写 B。</span></div>

##### 3. Le unità: KB, MB, GB, TB · ٣. الوحدات: KB، MB، GB، TB · 3. 单位：KB、MB、GB、TB

<div class="scheda">I file sono fatti di tantissimi byte. Per non scrivere numeri lunghi usiamo i <b>multipli</b>, ogni gradino è <b>circa 1000 volte</b> più grande:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nome</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Si scrive</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Quanto è</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">kilobyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">KB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 byte</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">megabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">MB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 KB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">gigabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 MB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">terabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 GB</td></tr></table>Come i metri: 1000 metri = 1 chilometro. (Il computer, per essere precisi, usa 1024 invece di 1000: per i nostri conti va bene 1000.)<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">كل درجة أكبر بنحو ١٠٠٠ مرة: ١٠٠٠ بايت = KB، ١٠٠٠ KB = MB، ١٠٠٠ MB = GB.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">每一级大约大 1000 倍：1000 字节 = 1 KB，1000 KB = 1 MB，1000 MB = 1 GB。</span></div>

##### 4. Quanto pesa? · ٤. كم يزن؟ · 4. 有多大？

<div class="scheda">Numeri tondi da ricordare:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Quanto pesa (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un messaggio di testo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1 KB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">una foto del telefono</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3 MB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">una canzone</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4 MB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un video di 1 minuto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">100 MB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un film</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 GB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">la memoria di un telefono</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">128 GB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il disco del PC che avete montato</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">500 GB o 1 TB</td></tr></table>La <b>RAM</b> si misura nello stesso modo: 8 GB, 16 GB.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">صورة ≈ ٣ MB، أغنية ≈ ٤ MB، فيلم ≈ ٢ GB، ذاكرة الهاتف ≈ ١٢٨ GB.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">一张照片约 3 MB，一首歌约 4 MB，一部电影约 2 GB，手机存储约 128 GB。</span></div>

##### 5. Il conto: quante foto ci stanno? · ٥. الحساب: كم صورة تتسع؟ · 5. 计算：能放多少张照片？

<div class="scheda">Il telefono ha <b>64 GB</b> liberi. Quante foto da 3 MB ci stanno?<br>1) Porto tutto in MB: 64 GB = 64 × 1000 = <b>64000 MB</b>.<br>2) Divido per il peso di una foto: 64000 : 3 = circa <b>21000 foto</b>.<br>Regola: <b>prima porto tutto nella stessa unità, poi divido</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">أولًا نحوّل كل شيء إلى نفس الوحدة، ثم نقسم: ٦٤ GB = ٦٤٠٠٠ MB، ٦٤٠٠٠ ÷ ٣ ≈ ٢١٠٠٠ صورة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">先换成同一个单位，再做除法：64 GB = 64000 MB，64000 ÷ 3 ≈ 21000 张照片。</span></div>

##### 6. La velocità della rete: bit al secondo · ٦. سرعة الشبكة: بِت في الثانية · 6. 网速：每秒多少比特

<div class="scheda">La velocità di Internet si misura in <b>bit al secondo</b>. Si usa il <b>Mbps</b> = megabit al secondo (milioni di bit ogni secondo).<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Connessione</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Velocità (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ADSL vecchia</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">10 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4G del telefono</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">5G</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">300 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fibra</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 Mbps = 1 Gbps</td></tr></table>Più Mbps = scarichi più in fretta, i video non si bloccano, il gioco online non va a scatti.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">سرعة الإنترنت تُقاس بالبِت في الثانية: Mbps = ميغابِت في الثانية. الألياف ≈ ١٠٠٠ Mbps.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">网速用“每秒比特”来量：Mbps = 每秒兆比特。光纤约 1000 Mbps。</span></div>

##### 7. Attenzione: b piccola e B grande · ٧. انتبه: b صغيرة و B كبيرة · 7. 注意：小写 b 和大写 B

<div class="scheda">La rete si misura in <b>Mb</b> (megabit, b piccola). I file si misurano in <b>MB</b> (megabyte, B grande).<br>Siccome 1 byte = 8 bit, per passare dalla velocità della rete ai MB al secondo <b>divido per 8</b>:<br>100 Mbps : 8 = <b>12,5 MB al secondo</b>.<br>Per questo, con una linea da 100 «mega», il download non va a 100 MB al secondo ma a circa 12.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الشبكة بالميغابِت (b صغيرة) والملفات بالميغابايت (B كبيرة). نقسم على ٨: ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB في الثانية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">网速用兆比特（小写 b），文件用兆字节（大写 B）。除以 8：100 Mbps ÷ 8 = 每秒 12.5 MB。</span></div>

##### 8. Quanto ci metto a scaricare? · ٨. كم أحتاج من الوقت للتنزيل؟ · 8. 下载需要多长时间？

<div class="scheda">Voglio scaricare un film da <b>2 GB</b> con una linea da <b>100 Mbps</b>.<br>1) Il film in MB: 2 GB = <b>2000 MB</b>.<br>2) La velocità in MB al secondo: 100 : 8 = <b>12,5 MB/s</b>.<br>3) Divido: 2000 : 12,5 = <b>160 secondi</b>, meno di 3 minuti.<br>Con il 4G a 30 Mbps: 30 : 8 ≈ 4 MB/s → 2000 : 4 = 500 secondi, più di 8 minuti.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">فيلم ٢ GB = ٢٠٠٠ MB. سرعة ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB/ث. ٢٠٠٠ ÷ ١٢٫٥ = ١٦٠ ثانية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">电影 2 GB = 2000 MB。100 Mbps ÷ 8 = 每秒 12.5 MB。2000 ÷ 12.5 = 160 秒。</span></div>

##### 9. Lo streaming: quanta velocità serve? · ٩. البثّ المباشر: كم سرعة نحتاج؟ · 9. 在线播放：需要多快的网速？

<div class="scheda"><b>Streaming</b> vuol dire guardare o ascoltare <b>mentre scarica</b>, senza salvare il file (YouTube, Netflix, Spotify, le dirette). Servono almeno:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Velocità minima (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">musica</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">0,3 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">videochiamata</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">video HD</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">5 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">video 4K</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">25 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">gioco online</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">10 Mbps, ma conta il <b>ping</b>: il tempo di risposta, sotto 50 ms</td></tr></table>Se in casa 3 persone guardano video HD insieme: 3 × 5 = 15 Mbps.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">البثّ = نشاهد أثناء التنزيل. فيديو HD ≈ ٥ Mbps، فيديو 4K ≈ ٢٥ Mbps.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">在线播放 = 边下载边看。高清视频约 5 Mbps，4K 视频约 25 Mbps。</span></div>

##### 10. Wi-Fi o cavo? · ١٠. واي فاي أم كابل؟ · 10. 无线还是网线？

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"></th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cavo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Velocità</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">alta e sempre uguale</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cala con la distanza e i muri</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Stabilità</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ottima, ping basso</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dipende: microonde, tanti dispositivi</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Comodità</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">devi stare vicino alla presa</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ti muovi dove vuoi</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Meglio per</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">PC fisso, console, lavoro</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">telefono, tablet, portatile</td></tr></table><b>Tipi di Wi-Fi</b> (il numero più alto è il più nuovo):<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nome</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Anno</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Velocità massima (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi 4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2009</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">600 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi 5</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2014</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">3500 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi 6 / 6E</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2019-2020</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">9600 Mbps</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi 7</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2024</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">oltre 40000 Mbps</td></tr></table>Due «strade» (bande): <b>2,4 GHz</b> arriva più lontano ma è più lenta; <b>5 GHz</b> è più veloce ma passa peggio i muri. Le velocità massime sono teoriche: a casa sono molto meno.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الكابل أسرع وأكثر ثباتًا، والواي فاي أكثر راحة. الواي فاي ٤ و٥ و٦ و٧: الرقم الأكبر هو الأحدث. ٢٫٤ GHz يصل أبعد، ٥ GHz أسرع.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">网线更快更稳定，无线更方便。Wi-Fi 4、5、6、7：数字越大越新。2.4 GHz 传得更远，5 GHz 更快。</span></div>

##### 11. I tipi di cavo · ١١. أنواع الكابلات · 11. 网线的种类

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cavo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Com'è</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Velocità (circa)</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Dove si usa</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">rame <b>Cat 5e</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">cavo di rete con la spina <b>RJ45</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 Mbps</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">casa, scuola</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">rame <b>Cat 6 / 6A</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">come il 5e, più schermato</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fino a 10000 Mbps</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">uffici, laboratori</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>fibra ottica</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un filo di vetro: passa la <b>luce</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">migliaia di Mbps, anche chilometri</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dalla centrale a casa, tra palazzi</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">coassiale</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il cavo dell'antenna TV</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">basse</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TV, vecchie reti</td></tr></table>Il cavo di rete di rame arriva al massimo a <b>100 metri</b>; la fibra va molto più lontano e non sente i disturbi elettrici.<br>Nel laboratorio, il cavo che va dal PC alla presa nel muro è un <b>Cat 5e o Cat 6 con RJ45</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">كابل النحاس (Cat 5e / Cat 6) بقابس RJ45 حتى ١٠٠ متر. الألياف البصرية تنقل الضوء وتصل إلى مسافات بعيدة جدًا.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">铜网线（Cat 5e / Cat 6）用 RJ45 插头，最长 100 米。光纤传输光，可以传很远。</span></div>


### L19 21/10/2026 — Il laboratorio del gamer: quante ce ne stanno?

*Libro parziale: lezioni/2026-10-21_gamer-quante.md*

#### Che cosa abbiamo fatto

1. **Quando:** 21/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Quanto pesa un file e quante ne stanno, tempo di download, streaming e buffering; percorso «Quante ce ne stanno?», giochi dei byte, quiz su Moduli, domande orali.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Calcoliamo quante foto e film stanno in una memoria e quanto tempo serve a scaricarli.</p><p lang="ar" dir="rtl">نحسب كم صورة وفيلمًا تتسع لها الذاكرة وكم من الوقت يلزم لتنزيلها.</p><p lang="zh">计算一个存储器能放多少照片和电影，以及下载需要多长时间。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Ripasso: Mbps e MB · مراجعة · 复习

<div class="scheda">La rete si misura in <b>Mbps</b> (megabit al secondo). 1 byte = 8 bit, quindi 100 Mbps = 12,5 MB al secondo. Per i giochi però la velocità non basta: conta anche <b>quanto in fretta</b> arriva la risposta.</div>

##### 2. Il ping · البينغ · 延迟(ping)

<div class="scheda">Il <b>ping</b> è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in <b>millisecondi (ms)</b>: 1000 ms = 1 secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Ping</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come si gioca</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sotto 30 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ottimo</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30-60 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">buono</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60-100 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">si sente un po'</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">oltre 150 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">lag: i colpi arrivano in ritardo</td></tr></table>Il ping dipende soprattutto dalla <b>distanza</b> dal server, non dai Mbps. <a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>: prova il gioco dei bersagli con ping 20 e con ping 200.</div>

##### 3. Il jitter · التذبذب · 抖动

<div class="scheda">Il <b>jitter</b> è quanto il ping <b>cambia</b> da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping.</div>

##### 4. Lag, scatti e pacchetti persi · التأخير والتقطع · 卡顿和丢包

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Parola</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Che cosa vuol dire</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Da dove viene</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>lag</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">il gioco risponde in ritardo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ping alto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>scatti</b> di rete</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">movimenti a salti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">jitter alto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>pacchetti persi</b> (packet loss)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">pezzi di informazione che non arrivano</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Wi-Fi debole, rete piena</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>scatti</b> del PC (FPS bassi)</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">l'immagine va a scatti anche offline</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">scheda video troppo lenta</td></tr></table>Il cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo.</div>

##### 5. Gli FPS · الإطارات في الثانية · 帧率(FPS)

<div class="scheda">Un video o un gioco è fatto di tante <b>immagini ferme</b> mostrate una dopo l'altra. <b>FPS</b> = frame per second, immagini al secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">FPS</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come appare</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">15</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a scatti</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">accettabile, film e console vecchie</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fluido</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">144 e più</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">molto fluido, giochi veloci</td></tr></table>Gli FPS li produce la <b>scheda video</b>. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS.</div>

##### 6. Gli Hz del monitor · الهرتز · 刷新率(Hz)

<div class="scheda">Gli <b>Hz</b> (hertz) dicono quante volte al secondo il <b>monitor</b> ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.<br>Regola: <b>FPS della scheda video e Hz del monitor devono andare d'accordo</b>. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando.</div>

##### 7. I tipi di monitor · أنواع الشاشات · 显示器类型

<div class="scheda"><table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Tipo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Pregio</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Difetto</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>TN</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">velocissimo, economico</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">colori spenti, angolo di visione stretto</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>IPS</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">colori belli, si vede bene di lato</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">un po' più lento</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>VA</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">neri profondi, buon contrasto</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a volte scie nelle scene veloci</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>OLED</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">neri perfetti, velocissimo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">costoso</td></tr></table>Il <b>tempo di risposta</b> (1-5 ms) dice quanto in fretta un pixel cambia colore: più basso, meno scie.</div>

##### 8. La scheda video · بطاقة الرسوميات · 显卡

<div class="scheda">La <b>scheda video</b> (GPU) disegna le immagini del gioco.<br><b>Integrata</b>: dentro il processore, consuma poco, va bene per scuola e video.<br><b>Dedicata</b>: una scheda a parte con la sua memoria (<b>VRAM</b>, per esempio 8 GB), serve per i giochi pesanti.<br>Più la risoluzione è alta (4K) e più gli FPS che vuoi, più la scheda video deve essere potente.</div>

##### 9. Quanto pesano immagini e film · حجم الصور والأفلام · 图片和电影有多大

<div class="scheda">Un'immagine è fatta di <b>pixel</b>; ogni pixel ha un colore di <b>3 byte</b> (rosso, verde, blu). Una foto Full HD: 1920 × 1080 pixel × 3 byte ≈ <b>6 MB</b> senza compressione. Il formato <b>JPG</b> la comprime a circa 0,5-1 MB.<br>Un <b>film</b> è un'immagine ripetuta 24-30 volte al secondo: 2 ore senza compressione sarebbero più di 1000 GB! Grazie alla compressione (MP4) diventa circa 2 GB. Per questo lo streaming funziona anche con pochi Mbps.</div>

##### 10. Il cavo video e la banda · كابل الفيديو · 视频线

<div class="scheda">Il PC si collega al monitor con un cavo video: <b>VGA</b> (vecchio, analogico, connettore blu a 15 piedini, immagine meno nitida), <b>DVI</b> (digitale, bianco), <b>HDMI</b> (digitale, porta anche l'audio, il più diffuso), <b>DisplayPort</b> (digitale, per i monitor da gaming). Dalla scheda video al monitor passano tantissimi dati. Il conto: <b>pixel × 3 byte di colore × Hz</b>. Full HD a 60 Hz: 1920 × 1080 × 24 bit × 60 ≈ <b>3 Gbit al secondo</b>.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cavo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Banda massima (circa)</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 1.4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">10 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 2.0</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">18 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DisplayPort 1.4</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">32 Gbit/s</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI 2.1</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">48 Gbit/s</td></tr></table>Per un monitor 4K a 144 Hz serve un cavo nuovo. <a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>, parte 3: calcola la banda del tuo monitor ideale.</div>

##### 11. Il mio setup da gamer · إعدادي · 我的游戏设备

<div class="scheda">Ultima prova: scegli il tuo <b>gioco preferito</b> e il setup giusto per giocarlo: cavo o Wi-Fi, quanti Hz, che monitor, che scheda video, che cavo video. Lo scrivi nella verifica con le tue parole e i tuoi numeri.</div>


### L20 22/10/2026 — Sicurezza 1: pericolo, danno, rischio

*Libro parziale: lezioni/2026-10-22_sicurezza-1.md*

#### Che cosa abbiamo fatto

1. **Quando:** 22/10/2026, 1 ora, Sicurezza.
2. **Argomenti:** Rischio e danno, pericolo, prevenzione e protezione, con casi della vita di tutti i giorni; quiz su Moduli.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Il pericolo è ciò che può fare male; il rischio è quanto è probabile che succeda; il danno è il male che succede davvero.</p><p lang="ar" dir="rtl">الخطر هو ما قد يؤذي؛ والمخاطرة هي احتمال حدوثه؛ والضرر هو الأذى الذي يحدث فعلاً.</p><p lang="zh">危险是可能伤人的东西；风险是发生的可能性；伤害是真正发生的损害。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Oggi: tre parole · ١. اليوم: ثلاث كلمات · 1. 今天：三个词

<div class="scheda">Oggi comincia il corso sulla <b>sicurezza</b>. Serve a una cosa sola: <b>non farsi male</b>, a scuola, a casa, per strada e al lavoro.<br>Oggi impari tre parole:<br><b>PERICOLO</b>: una cosa che <b>può</b> fare male.<br><b>DANNO</b>: il male che <b>succede davvero</b>.<br><b>RISCHIO</b>: <b>quanto è facile</b> che il danno succeda, e <b>quanto è grave</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">اليوم نتعلم ثلاث كلمات: الخطر = شيء يمكن أن يؤذي. الضرر = الأذى الذي يحدث فعلاً. المخاطرة = مدى سهولة حدوث الضرر ومدى خطورته.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">今天学三个词：危险源 = 可能伤人的东西。伤害 = 真的发生的伤。风险 = 伤害发生的可能性有多大、有多严重。</span></div>

##### 2. Il pericolo · ٢. الخطر · 2. 危险源

<div class="scheda">Il <b>pericolo</b> è una cosa (o una situazione) che <b>può</b> fare male. Non ti ha ancora fatto niente: <b>potrebbe</b>.<br>Esempi: il <b>coltello</b>, l'<b>olio bollente</b> nella padella, la <b>presa</b> con i fili che si vedono, il <b>pavimento bagnato</b>, la <b>strada</b> piena di macchine.<br>Domanda magica: <b>«Che cosa qui mi può fare male?»</b> La risposta è il pericolo.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الخطر = شيء يمكن أن يؤذي، لكنه لم يؤذك بعد. أمثلة: السكين، الزيت المغلي، المقبس بأسلاك ظاهرة، الأرض المبللة، الشارع.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">危险源 = 可能伤人的东西，但还没有伤到你。例如：刀、热油、露出电线的插座、湿的地板、马路。</span></div>

##### 3. I pericoli sono dappertutto · ٣. الأخطار في كل مكان · 3. 危险源到处都有

<div class="scheda"><b>In aula di informatica:</b> cavi per terra, zaini nel passaggio, una presa rotta, la sedia che dondola, lo schermo troppo vicino.<br><b>A casa, in cucina:</b> il fornello acceso, la pentola che bolle, il coltello, il ferro da stiro.<br><b>In strada:</b> il motorino, la bici di sera senza luci, il telefono in mano mentre attraversi.<br><b>Nello sport e in palestra:</b> il pallone lasciato a terra, il pavimento bagnato, gli attrezzi.<br><b>Nei lavoretti:</b> la scala, il trapano, la sedia con le ruote usata come scala.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">في قاعة الحاسوب: أسلاك على الأرض، حقائب في الممر، مقبس مكسور. في المطبخ: الموقد، القدر الذي يغلي، السكين. في الشارع: الدراجة النارية، الدراجة بلا أضواء. في الرياضة: كرة على الأرض، أرض مبللة. في الأعمال الصغيرة: السلّم، المثقاب.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">电脑教室：地上的电线、过道里的书包、坏插座。厨房：炉子、开水锅、刀。马路：摩托车、晚上没灯的自行车。运动：地上的球、湿地板。打零工：梯子、电钻。</span></div>

##### 4. Il danno · ٤. الضرر · 4. 伤害

<div class="scheda">Il <b>danno</b> è il male che <b>succede davvero</b>.<br>Esempi: un <b>taglio</b> al dito, una <b>bruciatura</b> alla mano, una <b>caviglia storta</b>, una <b>frattura</b> (un osso rotto), la <b>scossa</b> elettrica, il <b>mal di schiena</b>, gli <b>occhi stanchi</b> e il mal di testa dopo ore di schermo.<br>Il danno può essere piccolo (un graffio) o grande (un osso rotto). Si può rompere anche una cosa: il telefono, il PC.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الضرر = الأذى الذي يحدث فعلاً: جرح، حرق، التواء الكاحل، كسر، صدمة كهربائية، ألم الظهر، تعب العينين. يمكن أن يكون صغيراً أو كبيراً.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">伤害 = 真的发生的伤：割伤、烫伤、扭伤脚踝、骨折、触电、腰疼、眼睛累。伤害可以小，也可以大。</span></div>

##### 5. Il rischio · ٥. المخاطرة · 5. 风险

<div class="scheda">Il <b>rischio</b> risponde a due domande:<br>1) <b>Succede facilmente?</b> (spesso o quasi mai)<br>2) <b>Quanto male fa?</b> (poco o tanto)<br>Lo stesso pericolo può avere un rischio diverso. Il <b>coltello</b>: se tagli sul tagliere con le dita lontane, il rischio è <b>basso</b>. Se tagli il pane tenendolo in mano, verso la mano, il rischio è <b>alto</b>.<br>Il pericolo è la cosa. Il rischio dipende da <b>come</b> la usi.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">المخاطرة تجيب عن سؤالين: هل يحدث الضرر بسهولة؟ وكم يؤذي؟ نفس السكين: على لوح التقطيع والأصابع بعيدة = مخاطرة منخفضة؛ نحو اليد = مخاطرة عالية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">风险回答两个问题：伤害容易发生吗？伤得有多重？同一把刀：在砧板上、手指离得远 = 低风险；朝着手切 = 高风险。</span></div>

##### 6. Rischio alto, rischio basso · ٦. مخاطرة عالية، مخاطرة منخفضة · 6. 高风险、低风险

<div class="scheda">Guardiamo il <b>motorino</b>:<br><b>Rischio basso:</b> casco allacciato, piano, strada che conosci, di giorno.<br><b>Rischio alto:</b> senza casco, veloce, di notte, con il telefono in mano.<br>Guardiamo il <b>telefono in carica</b>:<br><b>Rischio basso:</b> caricatore originale, sul tavolo, di giorno.<br><b>Rischio alto:</b> caricatore con il filo spellato, sotto il cuscino, tutta la notte: si scalda tanto e può prendere fuoco.<br>Il rischio è più alto quando il danno è <b>più facile</b> e <b>più grave</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الدراجة النارية: خوذة مربوطة وسرعة بطيئة = مخاطرة منخفضة؛ بلا خوذة وبسرعة ومع الهاتف في اليد = مخاطرة عالية. الهاتف في الشحن تحت الوسادة طوال الليل = مخاطرة عالية: يسخن وقد يحترق.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">摩托车：系好头盔、慢慢开 = 低风险；不戴头盔、开得快、手拿手机 = 高风险。手机整夜在枕头下充电 = 高风险：会很烫，可能着火。</span></div>

##### 7. Tutte e tre insieme · ٧. الثلاثة معاً · 7. 三个词一起看

<div class="scheda"><b>La padella in cucina.</b><br>Pericolo: l'<b>olio bollente</b>.<br>Danno: una <b>bruciatura</b> alla mano o al braccio.<br>Rischio: <b>alto</b> se il manico sporge fuori dal fornello e passa un bambino; <b>basso</b> se il manico è girato verso dentro e stai attento.<br><b>La sedia in aula.</b><br>Pericolo: la sedia che <b>dondola</b> su due gambe.<br>Danno: cadi all'indietro e <b>batti la testa</b>.<br>Rischio: <b>alto</b> se ti dondoli spesso; <b>basso</b> se stai seduto con quattro gambe a terra.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">المقلاة: الخطر = الزيت المغلي؛ الضرر = حرق؛ المخاطرة عالية إذا كان المقبض خارج الموقد. الكرسي: الخطر = التأرجح؛ الضرر = السقوط وضرب الرأس.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">平底锅：危险源 = 热油；伤害 = 烫伤；锅柄朝外时风险高。椅子：危险源 = 摇椅子；伤害 = 向后摔倒、撞到头。</span></div>

##### 8. «Per un pelo!» · ٨. «نجوت بأعجوبة!» · 8. “差一点！”

<div class="scheda">Scivoli sul pavimento bagnato ma ti tieni al banco: <b>non ti fai niente</b>. Questo è un <b>quasi incidente</b>: il danno non c'è stato, ma il pericolo c'era davvero.<br>Che cosa fai? <b>Lo dici subito</b> (al prof, in palestra all'allenatore, al lavoro al capo), così la prossima persona non cade.<br>Chi fa sicurezza dice: <b>prima di un incidente vero ci sono tanti «per un pelo»</b>. Se li ascolti, eviti il danno.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">تنزلق على الأرض المبللة لكنك تمسك بالطاولة ولا تتأذى: هذا «حادث وشيك». أخبر فوراً المعلم أو المدرب أو المسؤول، حتى لا يسقط الشخص التالي.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">在湿地板上滑了一下，但扶住了桌子，没受伤：这是“险些发生的事故”。马上告诉老师、教练或老板，这样下一个人就不会摔倒。</span></div>


### L21 23/10/2026 — Rete e gamer: ping, jitter, FPS e monitor

*Libro parziale: lezioni/2026-10-23_rete-gamer.md*

#### Che cosa abbiamo fatto

1. **Quando:** 23/10/2026, 4 ore, Tecnologia e Laboratorio.
2. **Argomenti:** Ping, jitter, TCP e UDP, FPS e Hz, pannelli TN, VA e OLED, pixel e risoluzione; app «Le misure del mio PC» con le prove di ping, download e schermo; Documento personale; quiz su Moduli.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Nei giochi conta il ping (il tempo di risposta) più della velocità. Gli FPS sono le immagini al secondo, gli Hz quante volte il monitor si aggiorna.</p><p lang="ar" dir="rtl">في الألعاب يهمّ زمن الاستجابة (ping) أكثر من السرعة. FPS هي عدد الصور في الثانية، وHz عدد مرات تحديث الشاشة.</p><p lang="zh">玩游戏时 ping（响应时间）比网速更重要。FPS 是每秒画面数，Hz 是显示器每秒刷新的次数。</p></div>

#### La teoria e l'esercitazione

Ping, jitter, TCP e UDP, FPS e Hz, pixel, monitor, scheda video, cavi video

Classe 1 · lezione del 23/10/2026 · Versione 1.0

Questa dispensa raccoglie la lezione: le slide, le foto della lavagna e tanti esempi con i conti fatti. In fondo trovi gli esercizi «Prova tu» con le soluzioni.

##### 01 Il ping

Il **ping** è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e a tornare indietro. Si misura in **millisecondi (ms)**: 1000 ms = 1 secondo.

| Ping | Come si gioca |
|---|---|
| sotto 30 ms | ottimo |
| 30-60 ms | buono |
| 60-100 ms | si sente un po' |
| oltre 150 ms | lag: i colpi arrivano in ritardo |

Il ping dipende soprattutto dalla **distanza** dal server, non dai Mbps.

> **Esempio.** Giochi su un server a Milano: ping 15 ms. Lo stesso gioco su un server in America: ping 120 ms. La tua linea è la stessa (100 Mbps): cambia solo la strada che fa il messaggio. Con 120 ms premi «spara» e il server lo riceve 60 ms dopo (metà del viaggio): intanto l'avversario si è già spostato.

![La lavagna della lezione](../byte-velocita/immagini/lavagna-20261023/01_streaming-ftp-ping-jitter_doc.jpg)

*La lavagna della lezione: In alto: streaming senza ritrasmissione e FTP con ritrasmissione (capitolo 03). Al centro: il grafico del ping, con tempi di 23, 30 e 40 ms e un picco molto più alto. In basso: le onde del jitter.*

##### 02 Il jitter

Il **jitter** è quanto il ping **cambia** da un momento all'altro.

> **Esempio.** Ping misurati: 40, 41, 39, 40 ms. Cambiano di 1-2 ms: jitter **basso**, il gioco è regolare.  
> Ping misurati: 20, 120, 30, 110 ms. Cambiano di circa 100 ms: jitter **alto**, il personaggio salta e a volte si teletrasporta.

Sulla lavagna: le onde grandi sono una connessione a scatti (jitter alto); la riga quasi piatta in fondo è una connessione stabile (jitter basso).

> **Nota.** Meglio un ping di 50 ms sempre uguale che un ping che salta tra 20 e 120 ms.

##### 03 Con o senza ritrasmissione: TCP e UDP

In rete i dati viaggiano a **pacchetti**, cioè piccoli pezzi. A volte un pacchetto si perde per strada. Per spedire ci sono due regole, che si chiamano **protocolli**:

| Protocollo | Se un pacchetto si perde | Pregio | Si usa per |
|---|---|---|---|
| TCP | viene rimandato (con ritrasmissione, in inglese «retry») | arriva tutto, in ordine | file (FTP), pagine web, email, download |
| UDP | non viene rimandato (senza ritrasmissione) | più veloce, meno ritardo | streaming, videochiamate, giochi online |

> **Esempio.** Scarichi un file con FTP: se manca anche un solo pacchetto il file è rotto, quindi TCP lo rimanda. In una partita online un pacchetto perso diventa solo un piccolo scatto: aspettarlo bloccherebbe il gioco, quindi si usa UDP.

> **Nota.** Per ricordarlo: TCP è una raccomandata con ricevuta di ritorno; UDP è un volantino nella cassetta della posta: arriva prima, ma se si perde nessuno lo rimanda. TCP/IP è il nome di tutta la famiglia di regole di Internet.

##### 04 Lag, scatti e pacchetti persi

| Parola | Che cosa vuol dire | Da dove viene |
|---|---|---|
| lag | il gioco risponde in ritardo | ping alto |
| scatti di rete | movimenti a salti | jitter alto |
| pacchetti persi | pezzi di informazione che non arrivano | Wi-Fi debole, rete piena |
| scatti del PC | l'immagine va a scatti anche senza Internet | scheda video troppo lenta (FPS bassi) |

> **Esempio.** Il gioco va a scatti anche quando giochi senza Internet: la colpa non è della rete ma della scheda video. Se invece va a scatti solo online, controlla ping e jitter e prova il cavo al posto del Wi-Fi.

> **Nota.** Il cavo di rete dà ping e jitter più bassi del Wi-Fi: per questo i gamer usano il cavo.

##### 05 Gli FPS

Un video o un gioco è fatto di tante **immagini ferme** mostrate una dopo l'altra, come un cartone animato. **FPS** vuol dire «frame per second», cioè immagini al secondo. Gli FPS li prepara la **scheda video**.

| FPS | Come appare |
|---|---|
| 15 | a scatti |
| 30 | accettabile: film e console vecchie |
| 60 | fluido |
| 144 e più | molto fluido, per i giochi veloci |

> **Esempio.** A 60 FPS ogni immagine resta sullo schermo 1000 : 60 ≈ 17 ms. A 30 FPS resta 1000 : 30 ≈ 33 ms, il doppio: si vede meno fluido. A 144 FPS resta circa 7 ms.

##### 06 Gli Hz del monitor

Gli **Hz** (hertz) dicono quante volte al secondo il **monitor** ridisegna lo schermo. In inglese si dice «refresh rate», frequenza di aggiornamento.

> **Nota.** Regola: gli FPS della scheda video e gli Hz del monitor devono andare d'accordo.

> **Esempio.** Scheda video a 30 FPS, monitor a 120 Hz: il monitor ridisegna 120 volte al secondo ma ha solo 30 immagini nuove. Ogni immagine viene mostrata 4 volte (120 : 30 = 4): il monitor veloce è sprecato.  
> Scheda video a 200 FPS, monitor a 60 Hz: vedi comunque solo 60 immagini al secondo: la scheda video è sprecata.  
> Scheda video a 144 FPS, monitor a 144 Hz: tutto d'accordo, massima fluidità.

![La lavagna della lezione](../byte-velocita/immagini/lavagna-20261023/02_tcp-udp-fps-hz_doc.jpg)

*La lavagna della lezione: In alto: TCP/IP e UDP. Al centro: le immagini in fila (da 15 a 240 al secondo). In basso: 30 FPS su un monitor a 120 Hz, ogni immagine ripetuta 4 volte.*

##### 07 Pixel e risoluzione

Lo schermo è una griglia di quadratini colorati: ogni quadratino è un **pixel**. La **risoluzione** dice quanti pixel ci sono in larghezza e in altezza.

| Nome | Larghezza × altezza | Pixel in tutto (circa) |
|---|---|---|
| HD | 1280 × 720 | 0,9 milioni |
| Full HD | 1920 × 1080 | 2 milioni |
| 2K (QHD) | 2560 × 1440 | 3,7 milioni |
| 4K | 3840 × 2160 | 8,3 milioni |

> **Esempio.** 1920 × 1080 = 2.073.600, cioè circa 2 milioni di pixel.  
> Il 4K ha il doppio dei pixel in larghezza e il doppio in altezza: 2 × 2 = 4 volte il Full HD. Per questo serve una scheda video più potente.

![La lavagna della lezione](../byte-velocita/immagini/lavagna-20261023/04_pixel-risoluzione_doc.jpg)

*La lavagna della lezione: La griglia dei pixel e il conto 1920 × 1080 ≈ 2 milioni.*

##### 08 I tipi di monitor

Lo schermo può essere fatto in modi diversi: si chiamano **pannelli**. L'**angolo di visione** dice da quanto di lato vedi ancora bene i colori.

| Pannello | Angolo (lavagna) | Pregio | Difetto |
|---|---|---|---|
| TN | circa 90° | velocissimo (tanti Hz), economico | colori spenti, angolo stretto |
| IPS | 120° | colori belli, si vede bene di lato | un po' più lento |
| VA | 160° | neri profondi, buon contrasto | scia dietro le cose che si muovono |
| OLED | molto ampio | neri perfetti, velocissimo | costa tanto |

Sul VA la pallina che si muove lascia una scia, soprattutto nelle scene scure: si chiama **ghosting**, «immagine fantasma». Il **tempo di risposta** (1-5 ms) dice quanto in fretta un pixel cambia colore: più è basso, meno scie.

> **Esempio.** Chi gioca a sparatutto veloci e ha pochi soldi: TN o IPS veloce. Chi guarda film al buio: VA o OLED. Chi vuole il massimo e può spendere: OLED.

> **Nota.** Oggi i pannelli IPS e VA arrivano quasi a 178° e ci sono anche IPS a 144-240 Hz: i numeri della lavagna servono a capire la differenza tra i pannelli.

![La lavagna della lezione](../byte-velocita/immagini/lavagna-20261023/03_pannelli-tn-va-oled_doc.jpg)

*La lavagna della lezione: Gli angoli di visione (90°, 120°, 160°), la scia del VA, l'OLED che costa tanto.*

##### 09 La scheda video

La **scheda video** (in inglese GPU) disegna le immagini del gioco. **Integrata**: è dentro il processore, consuma poco, va bene per la scuola e i video. **Dedicata**: è una scheda a parte con la sua memoria (**VRAM**, per esempio 8 GB) e serve per i giochi pesanti.

> **Esempio.** Per scuola, video e Classroom basta la scheda integrata. Per un gioco 3D in Full HD a 144 FPS serve una scheda dedicata con almeno 8 GB di VRAM.

##### 10 Quanto pesano immagini e film

Ogni pixel ha un colore fatto di **3 byte**: rosso, verde, blu.

> **Esempio.** Una foto Full HD: 2.073.600 pixel × 3 byte = 6.220.800 byte, circa **6 MB**. Il formato JPG la comprime (la rende più piccola) a circa 0,5-1 MB.  
> Un film di 2 ore mostra 24 immagini al secondo: 6 MB × 24 = 144 MB ogni secondo; 2 ore sono 7200 secondi; 144 × 7200 = 1.036.800 MB, circa **1000 GB**. Con la compressione MP4 diventa circa 2 GB: 500 volte più piccolo. Per questo lo streaming funziona anche con pochi Mbps.

##### 11 Il cavo video e la banda

Il PC si collega al monitor con un **cavo video**: **VGA** (vecchio, connettore blu a 15 piedini, immagine meno nitida), **DVI** (digitale, bianco), **HDMI** (digitale, porta anche l'audio, il più diffuso), **DisplayPort** (digitale, per i monitor da gaming). La **banda** è quanti dati passano nel cavo ogni secondo: pixel × 24 bit di colore × Hz.

| Cavo | Banda massima (circa) |
|---|---|
| HDMI 1.4 | 10 Gbit/s |
| HDMI 2.0 | 18 Gbit/s |
| DisplayPort 1.4 | 32 Gbit/s |
| HDMI 2.1 | 48 Gbit/s |

> **Esempio.** Full HD a 60 Hz: 1920 × 1080 × 24 × 60 = 2.985.984.000 bit al secondo, circa **3 Gbit/s**: va bene anche HDMI 1.4.  
> 4K a 144 Hz: 3840 × 2160 × 24 × 144 = circa **28,7 Gbit/s**: HDMI 2.0 (18) non basta, serve DisplayPort 1.4 (32) o HDMI 2.1 (48).

##### 12 Esempio completo: il mio setup da gamer

Ecco un setup scelto per un gioco veloce, con i conti. Poi tocca a te, con il tuo gioco preferito.

| Che cosa | Scelta | Perché |
|---|---|---|
| gioco | uno sparatutto online | serve rapidità |
| rete | cavo, ping sotto 30 ms | ping e jitter bassi |
| monitor | IPS, Full HD, 144 Hz | veloce e con bei colori |
| scheda video | dedicata, 8 GB di VRAM | fa 144 FPS in Full HD |
| cavo video | DisplayPort 1.4 | 1920 × 1080 × 24 × 144 ≈ 7,2 Gbit/s: basta anche HDMI 2.0 |

##### 13 Prova tu

1. Ping misurati: 35, 36, 34, 35 ms. Il jitter è alto o basso?
2. Scheda video a 60 FPS, monitor a 240 Hz: quante volte viene mostrata ogni immagine?
3. Quanti pixel ha uno schermo 1280 × 720?
4. Scarichi un aggiornamento del gioco: TCP o UDP? E per la voce nella chat della squadra?
5. Il gioco va a scatti anche senza Internet: colpa della rete o della scheda video?
6. Un monitor 2K (2560 × 1440) a 60 Hz: basta un cavo HDMI 1.4?

###### Soluzioni

1. Basso: cambia solo di 1-2 ms.
2. 4 volte: 240 : 60 = 4.
3. 1280 × 720 = 921.600 pixel.
4. L'aggiornamento con TCP: il file deve arrivare intero. La voce con UDP: meglio un piccolo salto che un ritardo.
5. Della scheda video (FPS bassi).
6. 2560 × 1440 × 24 × 60 ≈ 5,3 Gbit/s: sì, HDMI 1.4 arriva a 10.

##### 14 Parole nuove

| Parola | Che cosa vuol dire |
|---|---|
| ping | tempo di andata e ritorno di un messaggio, in ms |
| jitter | quanto cambia il ping |
| lag | ritardo nel gioco |
| pacchetto | piccolo pezzo di dati che viaggia in rete |
| protocollo | regola per spedire i dati (TCP, UDP) |
| FPS | immagini al secondo preparate dalla scheda video |
| Hz | volte al secondo che il monitor ridisegna lo schermo |
| pixel | quadratino colorato dello schermo |
| risoluzione | pixel in larghezza × pixel in altezza |
| pannello | il tipo di schermo: TN, IPS, VA, OLED |
| VRAM | la memoria della scheda video |
| banda | quanti dati passano ogni secondo |

### L22 27/10/2026 — Ripasso e schede video, uscite e cavi

*Libro parziale: lezioni/2026-10-27_ripasso-video-cavi.md*

#### Che cosa abbiamo fatto

1. **Quando:** 27/10/2026, Laboratorio.
2. **Argomenti:** Ripasso di bit, byte, Mbps, ping, jitter, FPS e Hz con il quiz su Moduli; GPU integrata e dedicata, VRAM, uscite video VGA, DVI, HDMI, DisplayPort, USB-C e adattatori.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">La scheda video crea le immagini; il cavo (HDMI, DisplayPort, VGA) le porta al monitor.</p><p lang="ar" dir="rtl">بطاقة الرسوم تصنع الصور، والكابل (HDMI أو DisplayPort أو VGA) ينقلها إلى الشاشة.</p><p lang="zh">显卡生成画面；线缆（HDMI、DisplayPort、VGA）把画面送到显示器。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Il bit: 0 oppure 1 · ١. البِت: صفر أو واحد · 1. 比特：0 或 1

<div class="scheda">Il computer capisce solo <b>due cose</b>: corrente <b>sì</b> o corrente <b>no</b>, come una lampadina accesa o spenta. Le scriviamo <b>1</b> e <b>0</b>.<br>Un solo 0 o 1 si chiama <b>bit</b>. È il pezzo più piccolo di informazione. Lo avete già visto con il <b>binario</b>: 1010 sono 4 bit.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الحاسوب يفهم شيئين فقط: 1 أو 0، مثل مصباح مضاء أو مطفأ. الرقم الواحد اسمه «بِت».</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">电脑只懂两种状态：1 或 0，就像灯开或关。一个 0 或 1 叫做“比特”（bit）。</span></div>

##### 2. Il byte: 8 bit insieme · ٢. البايت: ٨ بِت معًا · 2. 字节：8 个比特

<div class="scheda">Un bit da solo dice poco. <b>8 bit insieme</b> fanno un <b>byte</b>. Con un byte il computer scrive <b>una lettera</b>: la A è 01000001.<br>Quindi: <b>1 byte = 8 bit = una lettera</b>.<br>Il bit si scrive con la <b>b piccola</b>, il byte con la <b>B grande</b>. Ricordatelo: serve dopo, per la velocità.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">٨ بِت = ١ بايت = حرف واحد. البِت يُكتب b صغيرة، والبايت B كبيرة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">8 个比特 = 1 个字节 = 一个字母。比特写小写 b，字节写大写 B。</span></div>

##### 3. Le unità: KB, MB, GB, TB · ٣. الوحدات: KB، MB، GB، TB · 3. 单位：KB、MB、GB、TB

<div class="scheda">I file sono fatti di tantissimi byte. Per non scrivere numeri lunghi usiamo i <b>multipli</b>, ogni gradino è <b>circa 1000 volte</b> più grande:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Nome</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Si scrive</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Quanto è</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">kilobyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">KB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 byte</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">megabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">MB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 KB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">gigabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 MB</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">terabyte</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">1000 GB</td></tr></table>Come i metri: 1000 metri = 1 chilometro. (Il computer, per essere precisi, usa 1024 invece di 1000: per i nostri conti va bene 1000.)<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">كل درجة أكبر بنحو ١٠٠٠ مرة: ١٠٠٠ بايت = KB، ١٠٠٠ KB = MB، ١٠٠٠ MB = GB.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">每一级大约大 1000 倍：1000 字节 = 1 KB，1000 KB = 1 MB，1000 MB = 1 GB。</span></div>

##### 4. Attenzione: b piccola e B grande · ٧. انتبه: b صغيرة و B كبيرة · 7. 注意：小写 b 和大写 B

<div class="scheda">La rete si misura in <b>Mb</b> (megabit, b piccola). I file si misurano in <b>MB</b> (megabyte, B grande).<br>Siccome 1 byte = 8 bit, per passare dalla velocità della rete ai MB al secondo <b>divido per 8</b>:<br>100 Mbps : 8 = <b>12,5 MB al secondo</b>.<br>Per questo, con una linea da 100 «mega», il download non va a 100 MB al secondo ma a circa 12.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الشبكة بالميغابِت (b صغيرة) والملفات بالميغابايت (B كبيرة). نقسم على ٨: ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB في الثانية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">网速用兆比特（小写 b），文件用兆字节（大写 B）。除以 8：100 Mbps ÷ 8 = 每秒 12.5 MB。</span></div>

##### 5. Il ping · البينغ · 延迟(ping)

<div class="scheda">Il <b>ping</b> è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in <b>millisecondi (ms)</b>: 1000 ms = 1 secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Ping</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come si gioca</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sotto 30 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">ottimo</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30-60 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">buono</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60-100 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">si sente un po'</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">oltre 150 ms</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">lag: i colpi arrivano in ritardo</td></tr></table>Il ping dipende soprattutto dalla <b>distanza</b> dal server, non dai Mbps. <a href="../1inf-gamer/" target="_blank" rel="noopener"><b>Apri il Laboratorio del gamer</b></a>: prova il gioco dei bersagli con ping 20 e con ping 200.</div>

##### 6. Il jitter · التذبذب · 抖动

<div class="scheda">Il <b>jitter</b> è quanto il ping <b>cambia</b> da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping.</div>

##### 7. Gli FPS · الإطارات في الثانية · 帧率(FPS)

<div class="scheda">Un video o un gioco è fatto di tante <b>immagini ferme</b> mostrate una dopo l'altra. <b>FPS</b> = frame per second, immagini al secondo.<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">FPS</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Come appare</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">15</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">a scatti</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">30</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">accettabile, film e console vecchie</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">60</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fluido</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">144 e più</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">molto fluido, giochi veloci</td></tr></table>Gli FPS li produce la <b>scheda video</b>. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS.</div>

##### 8. Gli Hz del monitor · الهرتز · 刷新率(Hz)

<div class="scheda">Gli <b>Hz</b> (hertz) dicono quante volte al secondo il <b>monitor</b> ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.<br>Regola: <b>FPS della scheda video e Hz del monitor devono andare d'accordo</b>. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando.<div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE DEL RIPASSO · نهاية المراجعة · 复习结束</b></p><p><a href="https://docs.google.com/forms/d/e/1FAIpQLSfGk_SZIFZ5pJ6bxXXmSQkSHMlKuKH54Jlpebvdn2WtvmAD8g/viewform" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">QUIZ di ripasso · اختبار المراجعة · 复习测验</a></p><p>Poi la teoria nuova · ثم الدرس الجديد · 然后新课: <a href="./?b=1inf-video-cavi">la scheda video e i cavi video</a></p></div></div>


#### Le schede della lezione

##### 1. La GPU: il cervello delle immagini · ١. معالج الرسوميات: عقل الصور · 1. GPU：图像的大脑

<div class="scheda">Il 21/10 avete visto che gli <b>FPS</b> (immagini al secondo) li prepara la <b>scheda video</b>. Oggi la guardiamo da vicino.<br>Dentro la scheda video c'è la <b>GPU</b>: è il <b>cervello delle immagini</b>. Il processore (CPU) pensa a tutto il resto; la GPU disegna lo schermo, migliaia di pixel insieme.<br>Ci sono due tipi:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"></th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Integrata</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Dedicata</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Dove sta</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">dentro il processore</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">una scheda a parte, infilata nello <b>slot PCIe</b> della scheda madre</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Com'è</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">non si vede</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">grande, con <b>1, 2 o 3 ventole</b></td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Potenza</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">bassa: scuola, video, Internet</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">alta: giochi, montaggio video, 3D</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Prezzo</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">compresa nel processore</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">da 150 a oltre 1000 euro</td></tr></table>I PC del laboratorio di solito hanno la scheda video <b>integrata</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">GPU هو عقل الصور. المدمجة داخل المعالج، والمنفصلة بطاقة مستقلة في منفذ PCIe ولها مراوح.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">GPU 是图像的大脑。集成显卡在处理器里面；独立显卡是单独的一块卡，插在 PCIe 插槽上，有风扇。</span></div>

##### 2. La VRAM e la corrente · ٢. ذاكرة الفيديو والكهرباء · 2. 显存和电源

<div class="scheda">La scheda dedicata ha una <b>sua memoria</b>: la <b>VRAM</b> (video RAM). Lì tiene le immagini, i colori e i disegni del gioco. Si misura in <b>GB</b>, come la RAM:<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">VRAM</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Va bene per</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4 GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">giochi leggeri in Full HD</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">8 GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">quasi tutti i giochi in Full HD</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">12-16 GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">giochi in 2K e 4K, montaggio video 4K</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">24 GB</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4K al massimo, grafica 3D, intelligenza artificiale</td></tr></table>La scheda integrata non ha VRAM sua: <b>prende in prestito un pezzo della RAM</b> del PC.<br>La scheda dedicata <b>consuma tanta corrente</b>: da 75 a 450 watt (una lampadina LED ne consuma 10). Per questo ha un cavo che arriva <b>direttamente dall'alimentatore</b>, e serve un alimentatore più forte (600-850 watt). Scalda tanto: per questo ha le ventole.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">VRAM هي ذاكرة بطاقة الرسوميات وتُقاس بـ GB (مثلًا ٨ GB). البطاقة المنفصلة تستهلك كهرباء كثيرة (٧٥-٤٥٠ واط) وتحتاج كابلًا من مزوّد الطاقة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">VRAM 是显卡自己的内存，用 GB 来量（比如 8 GB）。独立显卡很耗电（75-450 瓦），需要电源直接接线。</span></div>

##### 3. Le uscite video: riconoscerle a vista · ٣. منافذ الفيديو: كيف نعرفها بالنظر · 3. 视频接口：一眼认出来

<div class="scheda">Dietro al PC ci sono tante <b>prese</b> (uscite). Quelle per il monitor si riconoscono da <b>forma</b>, <b>colore</b> e <b>piedini</b> (i pin, i contatti di metallo):<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Uscita</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Forma</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Colore</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Piedini</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>VGA</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">trapezio con 2 viti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">blu</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">15 buchini in 3 file</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>DVI</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">rettangolo lungo con 2 viti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">bianco</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">fino a 24 buchini + una crocetta</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>HDMI</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">trapezio piatto, senza viti</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">nero</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">19 contatti dentro</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>DisplayPort</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">rettangolo con <b>un angolo tagliato</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">nero</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">20 contatti dentro</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>USB-C</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">piccolo ovale, entra nei due versi</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">nero o grigio</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">24 contatti dentro</td></tr></table>Attenzione: se il PC ha una scheda <b>dedicata</b>, le sue uscite sono <b>più in basso</b>, in fila orizzontale. Il monitor va attaccato <b>lì</b>, non alle uscite in alto vicino alle USB (quelle sono della scheda integrata).<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">نعرف المنافذ من الشكل واللون وعدد الدبابيس: VGA أزرق ١٥ ثقبًا، DVI أبيض كبير، HDMI مسطّح، DisplayPort له زاوية مقطوعة، USB-C صغير بيضاوي.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">看形状、颜色和针脚就能认出：VGA 蓝色 15 孔，DVI 白色很大，HDMI 扁平，DisplayPort 有一个切角，USB-C 小小的椭圆形。</span></div>

##### 4. I cavi video a confronto · ٤. مقارنة كابلات الفيديو · 4. 视频线比较

<div class="scheda">Ogni uscita ha il suo cavo. Ecco la tabella da ricordare (numeri tondi):<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Cavo</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Com'è</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Audio</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Massimo (circa)</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Dove si trova</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>VGA</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">vecchio, <b>analogico</b>, blu</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">no, solo immagine</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Full HD a 60 Hz, meno nitido</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">PC e proiettori vecchi</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>DVI</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">digitale, bianco, grande</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">di solito no</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">2560 × 1600 a 60 Hz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">PC e monitor di 10-15 anni fa</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>HDMI 1.4</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">digitale, il più comune</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4K a 30 Hz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TV, PC, proiettori</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>HDMI 2.0</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">uguale fuori</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4K a 60 Hz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">TV, console, PC</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>HDMI 2.1</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">uguale fuori</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4K a 120 Hz, 8K a 60 Hz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">console nuove, TV nuove</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>DisplayPort 1.4</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">digitale, angolo tagliato</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">4K a 120 Hz e oltre</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">PC e monitor da gioco</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left"><b>USB-C</b></td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">piccolo, entra nei due versi</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">di solito 4K a 60 Hz</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">telefoni, portatili, tablet</td></tr></table><b>Analogico</b> = il segnale è un'onda, si rovina un po'. <b>Digitale</b> = il segnale è fatto di 0 e 1, arriva pulito.<br>I cavi HDMI fuori sono tutti uguali: la versione (2.0, 2.1) è scritta sulla confezione o sul cavo.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">VGA قديم وتناظري، بدون صوت. HDMI الأكثر انتشارًا، صورة وصوت. DisplayPort لشاشات الألعاب. USB-C للهواتف والحواسيب المحمولة. HDMI 2.0: 4K بـ ٦٠ Hz. HDMI 2.1 و DisplayPort 1.4: 4K بـ ١٢٠ Hz.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">VGA 是旧的模拟线，没有声音。HDMI 最常见，有图像和声音。DisplayPort 用于游戏显示器。USB-C 用于手机和笔记本。HDMI 2.0：4K 60 Hz。HDMI 2.1 和 DisplayPort 1.4：4K 120 Hz。</span></div>

##### 5. Gli adattatori e il cavo giusto · ٥. المحوّلات والكابل المناسب · 5. 转接头和合适的线

<div class="scheda">Se il PC e il monitor hanno prese diverse si usa un <b>adattatore</b> (un pezzo che cambia la forma della spina):<table style="border-collapse:collapse;width:100%;font-size:15px;margin:8px 0"><tr><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Adattatore</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Funziona?</th><th style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">Attenzione</th></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">HDMI → VGA</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">trasforma il digitale in analogico; l'<b>audio si perde</b></td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DVI → HDMI</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì, facile</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">di solito senza audio</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">DisplayPort → HDMI</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì, facile</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">va bene per i PC con solo DisplayPort</td></tr><tr><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">USB-C → HDMI</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">sì</td><td style="border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left">solo se il telefono o il portatile manda il video dalla USB-C</td></tr></table><b>Il cavo giusto:</b><br>Per una <b>console</b> (PlayStation, Xbox, Switch): sempre <b>HDMI</b>, perché porta immagine e audio alla TV.<br>Per il <b>monitor della scuola</b>: guardi le prese dietro al PC e dietro al monitor e scegli quella <b>uguale e più nuova</b> (meglio HDMI o DisplayPort che VGA).<br>Per un <b>monitor da gioco a 144 Hz</b>: DisplayPort, o HDMI 2.1.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">المحوّل يغيّر شكل القابس: HDMI إلى VGA (يضيع الصوت). للكونسول نستعمل دائمًا HDMI. لشاشة المدرسة نختار المنفذ المتشابه والأحدث.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">转接头改变插头的形状：HDMI 转 VGA（没有声音）。游戏机永远用 HDMI。学校的显示器：选两边都有的、最新的接口。</span></div>

##### 6. Prova al banco: che uscite vedi? · ٦. تجربة على الطاولة: ما المنافذ التي تراها؟ · 6. 动手看看：你看到哪些接口？

<div class="scheda">Adesso tocca a te, al tuo posto, senza smontare niente e senza staccare cavi.<br>1) Guarda <b>dietro al PC</b> del laboratorio. Cerca le prese della tabella della scheda 3. Conta: quante VGA? quante HDMI? quante DisplayPort? quante DVI?<br>2) Guarda <b>dietro al monitor</b>. Che prese ha?<br>3) Segui il cavo che va dal PC al monitor: <b>che cavo è</b>? Di che colore è la spina?<br>4) Il PC ha una scheda <b>dedicata</b> (uscite in basso, in fila) o solo <b>integrata</b> (uscite in alto, vicino alle USB)?<br>Scrivi quello che vedi nella casella «Prepara la tua storia» qui sotto: servirà nella verifica.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">انظر خلف الحاسوب وخلف الشاشة، بدون فصل أي كابل. عُدّ المنافذ: VGA، HDMI، DisplayPort، DVI. أي كابل يصل الحاسوب بالشاشة؟ اكتب ما تراه.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">看看电脑和显示器的背面，不要拔线。数一数：VGA、HDMI、DisplayPort、DVI 各有几个？电脑和显示器用的是哪种线？把你看到的写下来。</span></div>

##### 7. Spiegalo in 30 secondi · ٧. اشرحه في ٣٠ ثانية · 7. 30 秒讲清楚

<div class="scheda">Girati verso il compagno e digli queste frasi con parole tue. Se le sai dire, hai capito davvero:<br>1) «La <b>GPU</b> è il cervello che disegna le immagini; la VRAM è la sua memoria.»<br>2) «La scheda <b>integrata</b> sta nel processore; quella <b>dedicata</b> è una scheda a parte, con le ventole, per i giochi.»<br>3) «<b>VGA</b> è vecchio e porta solo l'immagine; <b>HDMI</b> porta immagine e audio; <b>DisplayPort</b> è per i monitor da gioco.»<br>4) «Se le prese sono diverse, uso un <b>adattatore</b>.»<br>Poi scambiatevi: adesso spiega lui a te.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">قل لزميلك: GPU عقل الصور. المدمجة في المعالج والمنفصلة بطاقة بمراوح. VGA قديم، HDMI صورة وصوت، DisplayPort لشاشات الألعاب.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">对同学说：GPU 是图像的大脑。集成显卡在处理器里，独立显卡是带风扇的卡。VGA 很旧，HDMI 有图像和声音，DisplayPort 用于游戏显示器。</span><!--QUIZNUOVO--><div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE · النهاية · 结束</b></p><p><a href="https://docs.google.com/forms/d/e/1FAIpQLSf0b-qU-RPEeoKmoufXEb02NTJKqKB-3F6u52nMeKcBdJQHzw/viewform" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">QUIZ sulla lezione nuova · اختبار الدرس الجديد · 新课测验</a></p></div><!--/QUIZNUOVO--></div>


### L23 28/10/2026 — Lazarus: il mio primo programma «Ciao»

*Libro parziale: lezioni/2026-10-28_lazarus-ciao.md*

#### Che cosa abbiamo fatto

1. **Quando:** 28/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Progetto nuovo in una cartella (Documenti\Lazarus), la palette, TEdit e TButton, ShowMessage «Ciao», i file del progetto per estensione; consegna del Documento su Classroom.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Con Lazarus costruiamo una finestra con una casella (TEdit) e un bottone (TButton): al clic compare «Ciao» e il nome.</p><p lang="ar" dir="rtl">مع Lazarus نبني نافذة فيها خانة نص (TEdit) وزر (TButton): عند النقر تظهر «Ciao» مع الاسم.</p><p lang="zh">用 Lazarus 做一个窗口，有文本框（TEdit）和按钮（TButton）：点击后出现“Ciao”和名字。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Che cos'è Lazarus · ١. ما هو Lazarus · 1. Lazarus 是什么

<div class="scheda"><div style="background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 6px"><b>Questa pagina cambia durante la lezione: ogni tanto premi F5 per vedere la versione nuova.</b></p><p lang="ar" dir="rtl" style="color:#5b6573"><b>هذه الصفحة تتغيّر أثناء الدرس: اضغط F5 من وقت لآخر لترى النسخة الجديدة.</b></p><p lang="zh" style="color:#5b6573"><b>这个页面在上课时会变化：时不时按 F5，看最新的版本。</b></p></div><div style="background:#fdf2e6;border:2px solid #b45309;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 8px"><a href="../1inf-oggi/" target="_blank" rel="noopener" style="display:block;text-align:center;background:#b45309;color:#fff;font-weight:bold;font-size:18px;padding:14px 12px;border-radius:10px;text-decoration:none">Il mio cruscotto: voto, che cosa ho fatto e che cosa manca</a></p><p style="margin:0 0 6px">Guardalo ogni tanto: ti dice a che punto sei e che cosa ti manca per consegnare.</p><p lang="ar" dir="rtl" style="color:#5b6573">انظر إليه من وقت لآخر: يقول لك أين وصلت وماذا ينقصك لكي تسلّم.</p><p lang="zh" style="color:#5b6573">时不时看一看：它告诉你做到哪里了，还差什么才能提交。</p></div><p><b>Lazarus</b> è un programma che serve a <b>creare altri programmi</b>, con le finestre e i bottoni, come quelli che usi ogni giorno. Funziona come i <b>mattoncini</b>: prendi un pezzo già pronto (un bottone, una casella), lo metti nella finestra e poi scrivi <b>che cosa deve fare</b>. Il linguaggio si chiama <b>Pascal</b>.</p><p>Oggi facciamo il primo programma di tutti i programmatori: il <b>«Ciao»</b>. Scrivi il tuo nome in una casella, premi un bottone e il programma ti saluta: <b>Ciao Ahmed</b>.</p><p>Per aprire Lazarus: doppio clic sull'icona di Lazarus (il prof vi mostra dove si trova). Poi vai alla scheda 2: lì prepari il progetto nuovo e la tua cartella.</p><p lang="ar" dir="rtl" style="color:#5b6573">Lazarus برنامج نصنع به برامج أخرى بنوافذ وأزرار. نأخذ قطعة جاهزة (زر، خانة) ونضعها في النافذة، ثم نكتب ماذا تفعل. اللغة اسمها Pascal. اليوم نصنع برنامج «Ciao» (مرحبًا): تكتب اسمك، تضغط الزر، فيقول لك البرنامج مرحبًا.</p><p lang="zh" style="color:#5b6573">Lazarus 是用来做其他程序的软件，可以做有窗口和按钮的程序。像搭积木一样：拿一个现成的零件（按钮、输入框），放进窗口，再写它要做什么。语言叫 Pascal。今天做第一个程序「Ciao」（你好）：写名字，按按钮，程序就跟你打招呼。</p></div>

##### 2. Partenza pulita: nuovo progetto e cartella nuova · ٢. بداية نظيفة: مشروع جديد ومجلد جديد · 2. 干净的开始：新项目和新文件夹

<div class="scheda"><p><a href="../1inf-howto-progetto/" target="_blank" rel="noopener" style="display:block;text-align:center;background:#0b6e99;color:#fff;font-weight:bold;font-size:18px;padding:14px 12px;border-radius:10px;text-decoration:none">Come si crea un progetto nuovo (vale per tutti i progetti) · كيف أنشئ مشروعًا جديدًا · 怎么新建项目</a></p><p>Prima di mettere i pezzi nella finestra prepariamo il posto giusto. Nel tuo PC c'è la cartella <b>Documenti → Lazarus</b>: lì dentro stanno <b>TUTTI</b> i tuoi progetti Lazarus dell'anno. Ogni progetto ha la <b>sua cartella</b>: <b>un progetto = una cartella sola</b>. Così nessun file si perde e nessun file si mescola con quelli di un altro progetto. Oggi il progetto si chiama <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao</code>.</p><p><b>Da ricopiare sul quaderno</b></p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">Documenti\   Lazarus\          &lt;- TUTTI i miei progetti     Ciao\           &lt;- UN progetto = UNA cartella     (prossimo)\</pre><p>Fai un passo alla volta. Dopo ogni passo guarda lo schermo.</p><p><b>1.</b> In alto a sinistra in Lazarus clicca il menu <b>File</b>.</p><p><b>2.</b> Nel menu clicca <b>Chiudi tutto</b>. Così si chiudono i file rimasti aperti.</p><p><b>3.</b> Se Lazarus chiede di salvare un progetto vecchio, clicca <b>No</b>.</p><p><b>4.</b> In alto clicca il menu <b>Progetto</b>.</p><p><b>5.</b> Nel menu clicca <b>Chiudi progetto</b>. Se la voce è grigia, non si può cliccare: va bene così, vai al passo 6.</p><p><b>6.</b> Ora fai il progetto nuovo. In alto clicca il menu <b>Progetto</b>.</p><p><b>7.</b> Nel menu clicca <b>Nuovo progetto…</b>. Si apre una finestra con un elenco.</p><p><b>8.</b> Nell'elenco a sinistra clicca <b>Applicazione</b>.</p><p><b>9.</b> In basso nella finestra clicca <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.</p><p><b>10.</b> SUBITO si salva. In alto clicca il menu <b>Progetto</b>.</p><p><b>11.</b> Nel menu clicca <b>Salva progetto con nome…</b>. Si apre la finestra per salvare.</p><p><b>12.</b> Nel pannello a sinistra della finestra clicca <b>Documenti</b>.</p><p><b>13.</b> Fai <b>doppio clic</b> sulla cartella <b>Lazarus</b>. In alto, nella barra del percorso, ora c'è scritto <b>Questo PC › Documenti › Lazarus</b>.</p><p><b>14.</b> In alto nella finestra clicca il bottone <b>Nuova cartella</b>.</p><p><b>15.</b> Scrivi il nome del progetto, con la C maiuscola e senza spazi, e premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Invio</code>:</p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">Ciao</pre><p><b>16.</b> Fai <b>doppio clic</b> sulla cartella <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao</code> per entrarci. In alto ora c'è scritto <b>Documenti › Lazarus › Ciao</b>.</p><p><b>17.</b> In basso, nella casella <b>Nome file</b>, scrivi il nome del progetto (lo stesso della cartella):</p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">Ciao.lpi</pre><p><b>18.</b> In basso a destra clicca <b>Salva</b>.</p><p><b>19.</b> Lazarus apre una seconda finestra: chiede il nome della <b>unit</b> (il file del codice). Nella casella <b>Nome file</b> lascia o scrivi:</p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">unit1.pas</pre><p><b>20.</b> In basso a destra clicca <b>Salva</b>.</p><p><b>21.</b> Controlla: guarda in alto, nella barra del titolo di Lazarus. C'è scritto <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao</code> e, tra parentesi, il percorso che finisce con <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Documents\Lazarus\Ciao</code> (Windows scrive <b>Documents</b>, in inglese: è la stessa cartella Documenti). FATTO: il tuo progetto ha la sua cartella!</p><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-6.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p style="margin-top:-4px;font-style:italic">Lo schermo del prof: la finestra per salvare il progetto. In alto il percorso Questo PC › Documenti › Lazarus; sotto, il bottone «Nuova cartella»; nell'elenco, la cartella Ciao appena creata.</p><p lang="ar" dir="rtl" style="color:#5b6573">شاشة الأستاذ: نافذة حفظ المشروع. في الأعلى المسار Documenti › Lazarus، وتحته زر «Nuova cartella» (مجلد جديد)، وفي القائمة المجلد Ciao.</p><p lang="zh" style="color:#5b6573">老师的屏幕：保存项目的窗口。上面是路径 Documenti › Lazarus，下面是「Nuova cartella」（新建文件夹）按钮，列表里是刚建好的文件夹 Ciao。</p><p lang="ar" dir="rtl" style="color:#5b6573">قبل أن نبدأ نجهّز المكان الصحيح. في حاسوبك يوجد المجلد «Documenti» ثم «Lazarus»: فيه كل مشاريعك. لكل مشروع مجلده: مشروع واحد = مجلد واحد، فلا يضيع أي ملف. ١) قائمة «File» ثم «Chiudi tutto» (إغلاق الكل)؛ إذا سأل عن حفظ مشروع قديم اضغط «No». ٢) قائمة «Progetto» ثم «Chiudi progetto» إذا كان الأمر متاحًا. ٣) قائمة «Progetto» ثم «Nuovo progetto» ثم «Applicazione» ثم OK. ٤) فورًا: قائمة «Progetto» ثم «Salva progetto con nome». ٥) على اليسار اضغط «Documenti»، ثم انقر مرتين على المجلد Lazarus. ٦) اضغط زر «Nuova cartella» (مجلد جديد) واكتب Ciao واضغط Invio، ثم انقر مرتين للدخول. ٧) احفظ المشروع باسم Ciao.lpi، ثم الوحدة باسم unit1.pas واضغط «Salva». ٨) تحقّق: في أعلى نافذة Lazarus يظهر الاسم Ciao والمسار Documents\Lazarus\Ciao.</p><p lang="zh" style="color:#5b6573">开始之前先准备好地方。你的电脑里有文件夹「Documenti」→「Lazarus」：你所有的项目都放在这里。每个项目有自己的文件夹：一个项目 = 一个文件夹，这样文件不会丢。1）菜单 File →「Chiudi tutto」（全部关闭）；如果问要不要保存旧项目，点「No」。2）菜单 Progetto →「Chiudi progetto」（如果能点）。3）菜单 Progetto →「Nuovo progetto」→「Applicazione」→ OK。4）马上保存：菜单 Progetto →「Salva progetto con nome」。5）在左边点「Documenti」，再双击文件夹 Lazarus。6）点「Nuova cartella」（新建文件夹），写 Ciao，按 Invio，再双击进去。7）项目存为 Ciao.lpi，然后单元存为 unit1.pas，点「Salva」。8）检查：Lazarus 最上面的标题栏里有 Ciao 和路径 Documents\Lazarus\Ciao。</p></div>

##### 3. Le finestre di Lazarus · ٣. نوافذ Lazarus · 3. Lazarus 的窗口

<div class="scheda"><p>Quando apri un progetto nuovo vedi più finestre. Ognuna ha un lavoro:</p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Dove</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Si chiama</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">A che cosa serve</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">in alto</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>menu</b> e <b>palette dei componenti</b></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">i comandi (File, Progetto, Esegui…) e, sotto, i pezzi da mettere nella finestra, divisi in linguette</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">a sinistra</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>Ispettore oggetti</b></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">le <b>proprietà</b> del pezzo selezionato (il testo, il nome, il colore) e i suoi <b>eventi</b> (che cosa succede quando lo clicchi)</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">al centro</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>Form1</b>, con i puntini</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">la <b>finestra del tuo programma</b>: qui metti i pezzi</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">dietro la Form</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>Editor del codice</b> (unit1.pas)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">qui scrivi <b>che cosa fa</b> il programma</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">in basso</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>Messaggi</b></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">Lazarus ti dice se è andato tutto bene o dove c'è un errore</td></tr></table></div><p>Per passare dalla Form al codice e ritorno: tasto <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">F12</code>.</p><p><b>Da ricopiare sul quaderno</b></p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">+--------------------------------------------------+ | MENU:  File  Progetto  Esegui ...                | | PALETTE: [Standard]  [OK] [abc] [A] ...          | +------------+-------------------------------------+ | ISPETTORE  |                                     | | OGGETTI    |   FORM1  (la mia finestra)          | |            |    +-----------------+              | | Proprieta  |    | Edit1           |  &lt;- TEdit    | |  Caption   |    +-----------------+              | |  Text      |       [ Saluta ]       &lt;- TButton   | | Eventi     |                                     | |  OnClick   |   (F12 = vado al codice)            | +------------+-------------------------------------+ | MESSAGGI: errori e avvisi                        | +--------------------------------------------------+</pre><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-2.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p style="margin-top:-4px;font-style:italic">Alla lavagna: in alto la palette con gli oggetti; a sinistra l'Object Inspector (Ispettore oggetti) con le proprietà e, nella linguetta Eventi, i metodi che rispondono ai clic; al centro la Form; dietro, il codice.</p><p lang="ar" dir="rtl" style="color:#5b6573">في الأعلى: القوائم ولوحة المكوّنات. على اليسار: «مفتش الكائنات» (الخصائص والأحداث). في الوسط: Form1 وهي نافذة برنامجك. خلفها: محرر الكود. في الأسفل: الرسائل والأخطاء. للتنقل بين النافذة والكود: F12.</p><p lang="zh" style="color:#5b6573">上面：菜单和组件面板。左边：对象检查器（属性和事件）。中间：Form1，就是你的程序窗口。后面：代码编辑器。下面：消息（错误会写在这里）。窗口和代码之间切换：按 F12。</p></div>

##### 4. La palette: come scegliere il pezzo giusto · ٤. لوحة المكوّنات: كيف نختار القطعة · 4. 组件面板：怎么选零件

<div class="scheda"><p>La <b>palette dei componenti</b> è la fila di icone in alto, sotto il menu. I pezzi di oggi sono nella linguetta <b>Standard</b>. Per scegliere, chiediti: <b>che cosa deve fare chi usa il programma?</b></p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Deve…</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Pezzo (componente)</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Icona nella palette</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Proprietà che conta</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>scrivere</b> qualcosa</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>TEdit</b> (casella di testo)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">una casella bianca con «abc» o «ab|»</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Text</code> = quello che c'è scritto dentro</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>premere</b> per far succedere una cosa</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>TButton</b> (bottone)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">un bottone con «OK»</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Caption</code> = la scritta sul bottone</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>leggere</b> un testo (solo guardare)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>TLabel</b> (etichetta)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">una «A»</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Caption</code> = il testo che si vede</td></tr></table></div><p>Per metterlo nella finestra: <b>un clic</b> sull'icona nella palette, poi <b>un clic</b> sulla Form1, nel punto dove lo vuoi. Lazarus gli dà un nome da solo: <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Edit1</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Button1</code>. Il <b>nome</b> (<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Name</code>) è quello che userai nel codice.</p><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-4.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p style="margin-top:-4px;font-style:italic">Lo schermo del prof: in rosso la linguetta Standard; sottolineati TButton (il bottone con Ok) e TEdit (la casella con abc).</p><p lang="ar" dir="rtl" style="color:#5b6573">شاشة الأستاذ: باللون الأحمر اللسان Standard؛ وتحتهما خط: TButton (الزر المكتوب عليه Ok) وTEdit (الخانة المكتوب فيها abc).</p><p lang="zh" style="color:#5b6573">老师的屏幕：红圈是 Standard 标签；画线的是 TButton（写着 Ok 的按钮）和 TEdit（写着 abc 的输入框）。</p><p lang="ar" dir="rtl" style="color:#5b6573">لوحة المكوّنات هي صف الأيقونات في الأعلى، اللسان «Standard». اسأل نفسك: ماذا يفعل المستخدم؟ يكتب ← TEdit (خانة نص، الخاصية Text). يضغط ← TButton (زر، الخاصية Caption). يقرأ فقط ← TLabel. نقرة على الأيقونة ثم نقرة على Form1.</p><p lang="zh" style="color:#5b6573">组件面板是上面一排图标，在 Standard 标签里。问自己：用户要做什么？要写字 → TEdit（输入框，属性 Text）。要按 → TButton（按钮，属性 Caption）。只看文字 → TLabel。点一下图标，再点一下 Form1。</p></div>

##### 5. Esercitazione: il mio «Ciao» · ٥. التمرين: برنامج «Ciao» · 5. 练习：我的「Ciao」

<div class="scheda"><p>Un passo alla volta. Dopo ogni passo guarda lo schermo: deve essere uguale.</p><p><b>1.</b> Nella palette, linguetta <b>Standard</b>, clicca <b>TEdit</b>, poi clicca nella Form1, in alto a sinistra. Compare una casella con scritto <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Edit1</code>.</p><p><b>2.</b> Con la casella selezionata, nell'Ispettore oggetti trova la proprietà <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Text</code> e cancella la scritta «Edit1»: la casella resta vuota.</p><p><b>3.</b> Nella palette clicca <b>TButton</b>, poi clicca nella Form1 sotto la casella. Compare <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Button1</code>.</p><p><b>4.</b> Con il bottone selezionato, nell'Ispettore oggetti cambia <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Caption</code> in <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Saluta</code>. FATTO: la finestra è pronta!</p><p><b>5.</b> Fai <b>doppio clic sul bottone</b>. Si apre il codice, con il cursore qui:</p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">procedure TForm1.Button1Click(Sender: TObject); begin   <span style="color:#7ee787">// qui scrivi la tua riga</span> end;</pre><p><b>6.</b> Tra <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">begin</code> e <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">end;</code> scrivi questa riga:</p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">ShowMessage('Ciao ' + Edit1.Text);</pre><p>Che cosa vuol dire, pezzo per pezzo:</p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Pezzo</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Vuol dire</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">ShowMessage( … )</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">apre una <b>finestrella</b> con un messaggio e il bottone <b>OK</b>. Quello che c'è tra le parentesi è il messaggio</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Edit1.Text</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il testo scritto dentro la casella Edit1 (il nome)</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'Ciao '</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">una scritta fissa. Va tra apici. Lo <b>spazio</b> dopo Ciao serve per non avere «CiaoAhmed»</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">+</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">attacca due scritte una dopo l'altra</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">;</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">fine dell'istruzione (come il punto alla fine di una frase)</td></tr></table></div><p>Tutto insieme: <b>«apri una finestrella con scritto Ciao e il nome che c'è nella casella»</b>. Come alla lavagna: scrivi MARIO, premi Saluta, compare <b>Ciao MARIO</b> con il bottone OK. È la funzione che risponde al <b>clic</b> del bottone: si chiama <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Button1Click</code>.</p><p><b>Da ricopiare sul quaderno</b></p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">scrivo MARIO -&gt; clic su [Saluta] -&gt; OnClick -&gt; Button1Click    -&gt; ShowMessage('Ciao ' + Edit1.Text) -&gt; | Ciao MARIO  [OK] |</pre><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-1.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-5.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p style="margin-top:-4px;font-style:italic">Lo schermo del prof. A sinistra, linguetta Eventi: OnClick è collegato a Button1Click (si collega da solo con il doppio clic sul bottone). Nella casella il prof ha scritto «Scrivi il tuo nome» nella proprietà Text. Nel codice il prof ha messo il nome prima: ShowMessage(Edit1.Text + ' ciao'); va bene lo stesso: cambia solo l'ordine delle scritte unite con il +.</p><p lang="ar" dir="rtl" style="color:#5b6573">شاشة الأستاذ: في لسان «Eventi» الحدث OnClick مربوط بـ Button1Click (يُربط وحده بالنقر مرتين على الزر). الأستاذ وضع الاسم أولًا: ShowMessage(Edit1.Text + ' ciao'); وهذا صحيح أيضًا، يتغيّر فقط ترتيب الكلمات.</p><p lang="zh" style="color:#5b6573">老师的屏幕：在 Eventi 标签里，OnClick 连着 Button1Click（双击按钮就会自动连上）。老师把名字放在前面：ShowMessage(Edit1.Text + ' ciao'); 这样也对，只是用 + 连起来的文字顺序不同。</p><p lang="ar" dir="rtl" style="color:#5b6573">١) ضع TEdit في النافذة وامسح نص «Edit1» من الخاصية Text. ٢) ضع TButton واجعل Caption = Saluta. ٣) انقر مرتين على الزر، يُفتح الكود. ٤) بين begin و end اكتب: ShowMessage('Ciao ' + Edit1.Text); المعنى: تفتح نافذة صغيرة فيها «Ciao» + الاسم وزر OK.</p><p lang="zh" style="color:#5b6573">1）放一个 TEdit，在 Text 属性里删掉「Edit1」。2）放一个 TButton，Caption 改成 Saluta。3）双击按钮，打开代码。4）在 begin 和 end 中间写：ShowMessage('Ciao ' + Edit1.Text); 意思：打开一个小窗口，写着「Ciao」加上名字，还有 OK 按钮。</p></div>

##### 6. Salva e fai partire · ٦. احفظ وشغّل · 6. 保存并运行

<div class="scheda"><p>La cartella <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao</code> l'hai già fatta nella scheda 2. Adesso basta poco.</p><p><b>1.</b> Premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ctrl</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">S</code>: Lazarus salva tutto nella tua cartella.</p><p><b>2.</b> Premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">F9</code> (oppure la freccia verde ▶ in alto). Lazarus prepara il programma e lo fa partire: si apre la TUA finestra.</p><p><b>3.</b> Clicca nella casella e scrivi il tuo nome.</p><p><b>4.</b> Clicca il bottone <b>Saluta</b>. Si apre una finestrella con <b>Ciao</b> e il tuo nome.</p><p><b>5.</b> Clicca <b>OK</b>. Ce l'hai fatta: hai scritto il tuo primo programma!</p><p><b>Errore? È normale, succede a tutti i programmatori.</b> Guarda la finestra Messaggi in basso: dice la riga. I più comuni: manca il <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">;</code>; hai scritto <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">=</code> invece di <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">:=</code>; manca un apice <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'</code>; la riga è fuori da begin … end.</p><p lang="ar" dir="rtl" style="color:#5b6573">١) اضغط Ctrl+S للحفظ. ٢) اضغط F9 للتشغيل: تفتح نافذتك. ٣) اكتب اسمك. ٤) اضغط الزر «Saluta». ٥) اضغط OK. خطأ؟ هذا طبيعي: انظر إلى «Messaggi» في الأسفل، فهي تذكر رقم السطر (ينقص ; أو ينقص ' ).</p><p lang="zh" style="color:#5b6573">1）按 Ctrl+S 保存。2）按 F9 运行：你的窗口就打开了。3）写你的名字。4）点「Saluta」按钮。5）点 OK。出错了？很正常：看下面的 Messaggi，它会告诉你是哪一行（少了 ; 或者少了 ' ）。</p></div>

##### 7. I file del progetto, uno per uno · ٧. ملفات المشروع · 7. 项目的文件

<div class="scheda"><p>Dopo <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">F9</code> apri la cartella <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao</code> con Esplora file. Lazarus ha creato tanti file. L'<b>estensione</b> sono le lettere dopo il punto nel nome del file: dice <b>che tipo di file è</b>. Non vedi le estensioni? In Esplora file, in alto: <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>.</p><p><b>Gruppo 1. Il progetto</b></p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">File</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cos'è</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cosa c'è dentro</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Si può cancellare?</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.lpi</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">informazioni del progetto (<b>L</b>azarus <b>P</b>roject <b>I</b>nformation)<br><i>Come: la scheda del progetto, con l'elenco dei pezzi e le istruzioni per montarli</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">un testo in formato <b>XML</b> (testo con le etichette tra &lt; e &gt;): quali file fanno parte del progetto e le <b>opzioni</b> del progetto e del compilatore, quelle che si cambiano dal menu <b>Progetto</b> → <b>Opzioni progetto…</b>. Con doppio clic su questo file riapri il progetto</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>NO</b></td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.lpr</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">programma principale (<b>L</b>azarus <b>PR</b>ogram)<br><i>Come: il fischio di inizio della partita: fa partire tutto</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">le poche righe in Pascal che fanno partire tutto e aprono Form1. Non si tocca</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>NO</b></td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.lps</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sessione (<b>L</b>azarus <b>P</b>roject <b>S</b>ession)<br><i>Come: un <b>segnalibro</b>: la memoria di dove eri rimasto</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">quali file erano aperti nell'editor, in che ordine erano le linguette, dov'era il cursore. <b>Non contiene il programma</b>: se la cancelli, il tuo lavoro c'è ancora tutto</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì: Lazarus la rifà</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.res</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">risorse (<b>RES</b>ource)<br><i>Come: lo zaino con le cose da portare dentro l'exe: icona e versione</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">l'icona e la versione del programma, pronte da mettere dentro l'exe</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì: Lazarus la rifà</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.ico</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">icona (<b>ICO</b>n)<br><i>Come: la foto profilo del programma</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il disegnino del programma, quello che vedi sulla barra di Windows</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì: Lazarus la rifà</td></tr></table></div><p><b>Gruppo 2. La finestra e il codice</b></p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">File</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cos'è</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cosa c'è dentro</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Si può cancellare?</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.lfm</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">la form (<b>L</b>azarus <b>F</b>or<b>M</b>)<br><i>Come: la piantina di una stanza: dove stanno i mobili</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>com'è fatta la finestra</b>: quali pezzi ci sono, dove stanno, quanto sono grandi, Caption e Text</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>NO</b></td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.pas</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">la unit (un file di codice in <b>Pas</b>cal)<br><i>Come: la ricetta: le istruzioni che hai scritto tu</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il <b>TUO codice</b>: la procedura <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Button1Click</code> con la riga del Ciao. Una unit può avere anche l'estensione <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.pp</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><b>NO</b></td></tr></table></div><p><b>Gruppo 3. Il programma finito</b></p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">File</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cos'è</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cosa c'è dentro</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Si può cancellare?</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.exe</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">eseguibile (<b>EXE</b>cutable), nella cartella del progetto<br><i>Come: la torta già cotta: si mangia anche senza la ricetta</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il <b>programma finito</b>, creato con F9. Si apre anche senza Lazarus</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì: si rifà con F9</td></tr></table></div><p><b>Gruppo 4. File di lavoro del compilatore</b> (il <b>compilatore</b> è il programma che trasforma il Pascal in un programma che il computer sa eseguire)</p><div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">File</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cos'è</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Che cosa c'è dentro</th><th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">Si può cancellare?</th></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">lib\x86_64-win64\</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">cartella<br><i>Come: il tavolo della cucina dove si preparano i pezzi</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">i pezzi intermedi che servono per fare l'exe (qui sotto)</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì: Lazarus la rifà</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.o</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">file oggetto (<b>O</b>bject)<br><i>Come: un ingrediente già cotto, uno solo</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il codice macchina di <b>una sola</b> unit, per esempio <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.o</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.ppu</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">unit compilata di Free Pascal (<b>P</b>ascal <b>P</b>recompiled <b>U</b>nit)<br><i>Come: un pezzo già montato, con l'etichetta che dice che cosa sa fare</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">le informazioni sulla unit già tradotta, per esempio <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.ppu</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.compiled</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">promemoria della compilazione<br><i>Come: lo scontrino: ricorda com'è andata l'ultima volta</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">come è stato compilato il progetto l'ultima volta: così Lazarus sa se deve rifare tutto</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.or</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">risorse compilate<br><i>Come: lo zaino del .res già chiuso, pronto da caricare</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">il file <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.res</code> già pronto da attaccare all'exe</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì</td></tr><tr><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top"><code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">backup\</code></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">cartella delle copie di sicurezza<br><i>Come: la fotocopia del compito prima di correggerlo</i></td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">quando salvi un file che esisteva già, Lazarus mette qui la versione di prima. Le copie dei file del progetto hanno <b>lo stesso nome</b> dell'originale (<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.pas</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">unit1.lfm</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ciao.lpi</code>…); un file che non fa parte del progetto prende in più <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.bak</code> (per esempio <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">prova.pas.bak</code>). La cartella compare dal secondo salvataggio</td><td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">sì</td></tr></table></div><p>Con le impostazioni normali di Lazarus 4, fuori dalla cartella <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">backup</code> non trovi copie con <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">~</code> o <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.bak</code>. Se le vedi, qualcuno ha cambiato le impostazioni delle copie (menu <b>Strumenti</b> → <b>Opzioni…</b>, pagina <b>Backup</b>).</p><p>Regola da ricordare: i <b>4 file da tenere</b>, da consegnare e da mettere su GitHub sono <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.lpi</code> <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.lpr</code> <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.pas</code> <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">.lfm</code>. Tutto il resto Lazarus lo rifà da solo.</p><p><b>Da ricopiare sul quaderno</b></p><pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">Ciao\                       &lt;- UNA cartella = UN progetto  |- Ciao.lpi    progetto (+ opzioni)      TENERE  |- Ciao.lpr    programma principale      TENERE  |- unit1.pas   il mio codice             TENERE  |- unit1.lfm   com'e' fatta la finestra  TENERE  |- Ciao.lps    sessione                  si rifa'  |- Ciao.res    risorse (icona)           si rifa'  |- Ciao.ico    icona                     si rifa'  |- Ciao.exe    programma finito (F9)     si rifa'  |- lib\x86_64-win64\  |     .o .ppu .compiled .or (compilatore) si rifa'  |- backup\     copie di sicurezza        si butta</pre><p><img src="../../docs/verifica/foto/1inf-lazarus-ciao-3.jpg" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p><p style="margin-top:-4px;font-style:italic">Alla lavagna: il nome del progetto (qui PIPPO) è quello che scegli tu; la unit si chiama UNIT1 se non la rinomini. Il codice è scritto in Object Pascal.</p><p lang="ar" dir="rtl" style="color:#5b6573">الامتداد هو الحروف بعد النقطة في اسم الملف، ويقول نوع الملف (لإظهاره في مستكشف الملفات: Visualizza ثم Mostra ثم Estensioni nomi file). المجموعة ١، المشروع: .lpi (معلومات المشروع وخياراته بصيغة XML، مثل بطاقة المشروع؛ ننقر عليه مرتين لنكمل العمل)، .lpr (البرنامج الرئيسي)، .lps (الجلسة: مثل علامة الكتاب، تتذكر أين توقفت: الملفات المفتوحة في المحرر وترتيبها ومكان المؤشر؛ لا تحتوي البرنامج، يمكن حذفها وLazarus يصنعها من جديد)، .res (الموارد)، .ico (الأيقونة). المجموعة ٢، النافذة والكود: .lfm (شكل النافذة، مثل مخطط الغرفة)، .pas (كودك، مثل الوصفة؛ وقد يكون امتداده أيضًا .pp). المجموعة ٣، البرنامج الجاهز: .exe (مثل الكعكة الجاهزة، تعمل بدون Lazarus). المجموعة ٤، ملفات عمل المترجم: المجلد lib\x86_64-win64 فيه .o (كود الآلة لوحدة واحدة) و.ppu (وحدة مترجمة) و.compiled (تذكير بطريقة الترجمة) و.or (موارد مترجمة)؛ والمجلد backup فيه نسخ احتياطية بنفس الاسم. القاعدة: نحتفظ بأربعة ملفات ونسلّمها ونضعها على GitHub: .lpi .lpr .pas .lfm، والباقي يصنعه Lazarus وحده.</p><p lang="zh" style="color:#5b6573">扩展名是文件名里点后面的字母，表示文件的类型（在文件资源管理器里显示：Visualizza → Mostra → Estensioni nomi file）。第 1 组，项目：.lpi（项目信息和选项，XML 格式，像项目卡片；双击它继续工作）、.lpr（主程序）、.lps（会话：像书签，记住你停在哪里：编辑器里打开了哪些文件、顺序、光标位置；里面没有程序，可以删掉，Lazarus 会再做一个）、.res（资源）、.ico（图标）。第 2 组，窗口和代码：.lfm（窗口的样子，像房间的平面图）、.pas（你的代码，像菜谱；单元也可以是 .pp）。第 3 组，做好的程序：.exe（像做好的蛋糕，没有 Lazarus 也能打开）。第 4 组，编译器的工作文件：lib\x86_64-win64 文件夹里有 .o（一个单元的机器码）、.ppu（编译好的单元）、.compiled（怎么编译的记录）、.or（编译好的资源）；backup 文件夹里是同名的备份。规则：要保留、提交、放到 GitHub 上的是 4 个文件：.lpi .lpr .pas .lfm，其他的 Lazarus 会自己再做。</p></div>

##### 8. Fallo tuo · ٨. اجعله خاصًا بك · 8. 做成你自己的

<div class="scheda"><p>Il programma funziona? Adesso rendilo <b>tuo</b>. Scegli almeno una cosa:</p><p><b>1.</b> Il saluto nella <b>tua lingua</b>: al posto di <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'Ciao '</code> scrivi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'Hello '</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'مرحبا '</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'你好 '</code>, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">'Hola '</code>…</p><p><b>2.</b> Il <b>titolo</b> della finestra: clicca su un punto vuoto della Form1, nell'Ispettore oggetti cambia <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Caption</code> (per esempio «Il saluto di Ahmed»).</p><p><b>3.</b> Il <b>colore</b>: sempre sulla Form1, proprietà <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Color</code>, scegli un colore dalla tendina.</p><p><b>4.</b> Per i più veloci: aggiungi una TLabel e una seconda riga, <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Label1.Caption := 'Ciao ' + Edit1.Text;</code>: il saluto resta scritto anche nella finestra.</p><p>Poi <b>spiegalo in 30 secondi</b> al compagno: «Ho messo una TEdit e un TButton; quando clicco, la funzione Button1Click apre una finestrella con Ciao e il nome».</p><p lang="ar" dir="rtl" style="color:#5b6573">غيّر التحية إلى لغتك (مرحبا، 你好، Hello)، غيّر عنوان النافذة (Caption في Form1) ولونها (Color). ثم اشرح لزميلك في 30 ثانية ماذا يفعل برنامجك.</p><p lang="zh" style="color:#5b6573">把问候改成你的语言（你好、مرحبا、Hello），改窗口的标题（Form1 的 Caption）和颜色（Color）。然后用 30 秒跟同学讲你的程序做什么。</p></div>

##### 9. Consegna · ٩. التسليم · 9. 提交

<div class="scheda"><p>Su Classroom c'è il compito <b>«Il mio primo programma: Ciao in Lazarus»</b>. Dentro c'è un <b>Documento Google</b> già pronto, solo tuo. Aprilo e fai 3 cose:</p><p><b>1. Il codice.</b> In Lazarus seleziona con il mouse la tua procedura, da <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">procedure TForm1.Button1Click</code> fino a <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">end;</code>, premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ctrl</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">C</code>; nel Documento clicca sotto «1. Il mio codice» e premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ctrl</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">V</code>.</p><p><b>2. Lo screenshot.</b> Fai partire il programma (<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">F9</code>), scrivi il tuo nome e premi Saluta. Poi premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Win</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Shift</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">S</code> e trascina un rettangolo intorno alla tua finestra. Nel Documento clicca sotto «2. Il mio programma che funziona» e premi <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">Ctrl</code> + <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">V</code>.</p><p><b>3. Con parole tue.</b> Sotto «3» scrivi in una o due frasi che cosa fa la riga <code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">ShowMessage('Ciao ' + Edit1.Text);</code>. Puoi scrivere anche nella tua lingua.</p><p>Poi in Classroom premi <b>Consegna</b> (il bottone blu in alto a destra nel compito).</p><p lang="ar" dir="rtl" style="color:#5b6573">في Classroom الواجب «Il mio primo programma». داخله مستند Google خاص بك. ١) انسخ الكود من procedure إلى end; (Ctrl+C) والصقه (Ctrl+V). ٢) شغّل البرنامج، اكتب اسمك، اضغط Saluta، ثم Win+Shift+S وحدد نافذتك، والصق في المستند. ٣) اكتب بكلماتك ماذا يفعل السطر. ثم اضغط «Consegna» (الزر الأزرق).</p><p lang="zh" style="color:#5b6573">Classroom 里有作业「Il mio primo programma」，里面有一份你自己的 Google 文档。1）复制代码，从 procedure 到 end;（Ctrl+C），粘贴（Ctrl+V）。2）运行程序，写名字，按 Saluta，然后按 Win+Shift+S 框住你的窗口，粘贴到文档里。3）用你自己的话写这一行做什么。然后按「Consegna」（蓝色按钮）提交。</p></div>


### L24 29/10/2026 — Sicurezza 2 e 3: prevenzione, protezione e prevenzione aziendale

*Libro parziale: lezioni/2026-10-29_sicurezza-2-3.md*

#### Che cosa abbiamo fatto

1. **Quando:** 29/10/2026, 1 ora, Sicurezza.
2. **Argomenti:** Sicurezza sul lavoro (Regione), 2ª ora: prevenzione e protezione, con schede, ripasso e quiz su Moduli; su richiesta del docente anche la 3ª ora: l'organizzazione della prevenzione in azienda, con schede e quiz su Moduli.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">La prevenzione evita che il danno succeda; la protezione riduce il danno se succede. In azienda ognuno ha un compito per la sicurezza.</p><p lang="ar" dir="rtl">الوقاية تمنع حدوث الضرر؛ والحماية تقلّل الضرر إذا حدث. في الشركة لكل شخص دور في السلامة.</p><p lang="zh">预防是不让伤害发生；防护是在发生时减少伤害。在公司里每个人都有安全方面的任务。</p></div>

#### La teoria e l'esercitazione

#### Le schede della lezione

##### 1. Ripasso in un minuto · ١. مراجعة في دقيقة · 1. 一分钟复习

<div class="scheda">Ripasso della volta scorsa:<br><b>PERICOLO</b> = una cosa che <b>può</b> fare male.<br><b>DANNO</b> = il male che <b>succede davvero</b>.<br><b>RISCHIO</b> = <b>quanto è facile</b> che il danno succeda e <b>quanto è grave</b>.<br>Oggi impari come si <b>abbassa</b> il rischio.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">مراجعة: الخطر = شيء يمكن أن يؤذي. الضرر = الأذى الذي يحدث فعلاً. المخاطرة = مدى سهولة حدوث الضرر ومدى خطورته. اليوم نتعلم كيف نخفّض المخاطرة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">复习：危险源 = 可能伤人的东西。伤害 = 真的发生的伤。风险 = 伤害发生的可能性有多大、有多严重。今天学习怎样降低风险。</span></div>

##### 2. Due modi: prevenzione e protezione · ٢. طريقتان: الوقاية والحماية · 2. 两种方法：预防和防护

<div class="scheda">Ci sono <b>due modi</b> per abbassare il rischio.<br><b>PREVENZIONE</b>: il danno succede <b>meno spesso</b> (o mai). Agisci <b>prima</b>.<br><b>PROTEZIONE</b>: se il danno succede, fa <b>meno male</b>. Ti difende <b>durante</b>.<br>Esempio, il motorino: andare <b>piano</b> è prevenzione (cadi meno spesso); il <b>casco</b> è protezione (se cadi, ti fai meno male).<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">هناك طريقتان لتخفيض المخاطرة. الوقاية: الضرر يحدث أقل (أو لا يحدث أبداً)، نعمل قبل. الحماية: إذا حدث الضرر يكون أقل أذى. مثال الدراجة النارية: القيادة ببطء = وقاية؛ الخوذة = حماية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">降低风险有两种方法。预防：让伤害少发生（或不发生），在事前行动。防护：如果伤害发生了，伤得轻一些。例如摩托车：开慢一点 = 预防；头盔 = 防护。</span></div>

##### 3. La prevenzione a casa e in aula · ٣. الوقاية في البيت وفي القاعة · 3. 家里和教室里的预防

<div class="scheda"><b>A casa:</b> il manico della padella girato <b>verso dentro</b>; il telefono in carica <b>sul tavolo</b>, non sotto il cuscino; il pavimento bagnato asciugato <b>subito</b>.<br><b>In aula:</b> i cavi <b>lungo il muro</b>, gli zaini <b>sotto il banco</b>, la sedia con <b>quattro gambe a terra</b>, una presa rotta <b>detta subito</b> al prof.<br>Sono tutte <b>prevenzione</b>: il pericolo non arriva a farti male.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">في البيت: مقبض المقلاة نحو الداخل؛ الهاتف يُشحن على الطاولة لا تحت الوسادة؛ نجفف الأرض المبللة فوراً. في القاعة: الأسلاك بجانب الحائط، الحقائب تحت الطاولة، الكرسي على أرجله الأربع، نخبر المعلم فوراً عن المقبس المكسور. كل هذا وقاية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">在家：锅柄朝里；手机放在桌上充电，不放在枕头下；湿地板马上擦干。在教室：电线沿着墙，书包放在桌子下面，椅子四条腿着地，插座坏了马上告诉老师。这些都是预防。</span></div>

##### 4. La prevenzione in strada e nello sport · ٤. الوقاية في الشارع وفي الرياضة · 4. 马路上和运动中的预防

<div class="scheda"><b>In strada:</b> le <b>luci</b> della bici accese di sera, <b>rallentare</b> sul bagnato, il telefono <b>in tasca</b> mentre guidi o attraversi.<br><b>Nello sport:</b> il <b>riscaldamento</b> prima della partita, il pavimento della palestra <b>asciutto</b>, il pallone <b>rimesso a posto</b>.<br>Anche queste sono <b>prevenzione</b>: il danno succede meno spesso.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">في الشارع: أضواء الدراجة مضاءة في المساء، نبطئ على الأرض المبللة، الهاتف في الجيب أثناء القيادة أو عبور الطريق. في الرياضة: الإحماء قبل المباراة، أرض الصالة جافة، نعيد الكرة إلى مكانها. هذه أيضاً وقاية.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">在马路上：晚上开自行车灯，路湿时减速，骑车或过马路时手机放口袋里。运动时：比赛前热身，体育馆地板保持干燥，球放回原处。这些也是预防。</span></div>

##### 5. La protezione · ٥. الحماية · 5. 防护

<div class="scheda">La <b>protezione</b> non toglie il pericolo: fa sì che il danno sia <b>meno grave</b>.<br>Esempi: il <b>casco</b> del motorino e della bici, i <b>guanti da forno</b>, i <b>parastinchi</b> nel calcio, le <b>ginocchiere</b>, gli <b>occhiali</b> quando usi il trapano, le <b>scarpe antinfortunistiche</b> al lavoro.<br>Al lavoro queste cose si chiamano <b>DPI</b>: dispositivi di protezione individuale.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الحماية لا تزيل الخطر: تجعل الضرر أقل خطورة. أمثلة: خوذة الدراجة النارية والدراجة، قفازات الفرن، واقي الساق في كرة القدم، واقي الركبة، النظارات عند استعمال المثقاب، أحذية السلامة في العمل. في العمل تُسمّى معدات الحماية الشخصية (DPI).</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">防护不能去掉危险源：它让伤害不那么严重。例如：摩托车和自行车的头盔、烤箱手套、踢足球的护腿板、护膝、用电钻时戴的护目镜、工作时穿的安全鞋。在工作中这些叫个人防护装备（DPI）。</span></div>

##### 6. Protezione per tutti, protezione per me · ٦. حماية للجميع، حماية لي · 6. 保护所有人，保护我自己

<div class="scheda">Alcune protezioni proteggono <b>tutti</b>: il <b>salvavita</b> di casa (stacca la corrente se c'è un guasto), la <b>ciabatta con l'interruttore</b>, la <b>ringhiera</b> delle scale.<br>Altre proteggono <b>solo chi le indossa</b>: il casco, i guanti, gli occhiali.<br>Quelle per tutti funzionano anche se qualcuno si dimentica; quelle per me funzionano <b>solo se le metto</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">بعض وسائل الحماية تحمي الجميع: قاطع الكهرباء الآلي في البيت (يقطع الكهرباء عند العطل)، المشترك الكهربائي بزر، درابزين الدرج. وبعضها يحمي فقط من يلبسها: الخوذة، القفازات، النظارات. الحماية للجميع تعمل حتى لو نسي أحد؛ الحماية الشخصية تعمل فقط إذا لبستها.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">有些防护保护所有人：家里的漏电保护开关（出故障时自动断电）、带开关的插线板、楼梯扶手。有些只保护戴着它的人：头盔、手套、护目镜。保护所有人的防护即使有人忘了也有效；个人防护只有戴上才有效。</span></div>

##### 7. Prima la prevenzione, poi la protezione · ٧. أولاً الوقاية، ثم الحماية · 7. 先预防，再防护

<div class="scheda">La regola d'oro: <b>prima</b> provo a <b>togliere</b> il pericolo (prevenzione). Se <b>non posso</b> toglierlo, <b>mi proteggo</b> (protezione).<br>Esempio: il cavo per terra in aula. Prima lo <b>sposto lungo il muro</b>: il pericolo sparisce.<br>Esempio: l'olio bollente. Non posso cucinare senza: allora giro il manico verso dentro e uso i <b>guanti da forno</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">القاعدة الذهبية: أولاً أحاول إزالة الخطر (وقاية). إذا لم أستطع إزالته، أحمي نفسي (حماية). مثال: السلك على أرض القاعة: أولاً أنقله بجانب الحائط فيختفي الخطر. مثال: الزيت المغلي: لا أستطيع الطبخ بدونه، فأدير المقبض نحو الداخل وأستعمل قفازات الفرن.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">黄金法则：先想办法去掉危险源（预防）。如果去不掉，就保护自己（防护）。例如：教室地上的电线，先把它移到墙边，危险就没了。例如：热油，做饭离不开它，那就把锅柄朝里，并戴烤箱手套。</span></div>

##### 8. Lo schermo e la sedia · ٨. الشاشة والكرسي · 8. 屏幕和椅子

<div class="scheda">Al computer il pericolo è <b>piccolo ma tutti i giorni</b>: occhi stanchi, mal di schiena, mal di collo.<br>Prevenzione facile: una <b>pausa</b> breve ogni ora (guarda lontano), lo schermo alla <b>distanza di un braccio</b>, la <b>schiena appoggiata</b>, i piedi a terra, la sedia con <b>quattro gambe a terra</b>.<br>Lo puoi fare <b>adesso</b>, qui in aula.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">أمام الحاسوب الخطر صغير لكنه كل يوم: تعب العينين، ألم الظهر، ألم الرقبة. وقاية سهلة: استراحة قصيرة كل ساعة (انظر بعيداً)، الشاشة على بعد ذراع، الظهر مسنود، القدمان على الأرض، الكرسي على أرجله الأربع. تستطيع أن تفعل هذا الآن هنا في القاعة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">在电脑前，危险很小但每天都有：眼睛累、腰疼、脖子疼。简单的预防：每小时短暂休息一下（看远处），屏幕离你一臂远，后背靠着椅背，双脚着地，椅子四条腿着地。你现在就可以在教室里做到。</span><!--QUIZNUOVO--><div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE DELLE SCHEDE · نهاية البطاقات · 卡片结束</b></p><p>Fai il ripasso qui sotto, poi il quiz su Moduli (20 casi, 5 punti l'uno, massimo 100). · راجِع ثم أجب عن الاختبار. · 先复习，再做测验。</p><p><a href="https://docs.google.com/forms/d/e/1FAIpQLSfNVtYELVo5gTJbKZTcUMYCiWeHF_uy42Rbls1sFBPgQG9mBQ/viewform" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">QUIZ su Moduli · اختبار · 测验</a></p><p><b>Sul quaderno ricopia:</b> PREVENZIONE = il danno succede meno spesso. PROTEZIONE = se il danno succede, fa meno male. Regola d'oro: prima togli il pericolo, poi proteggiti. · انسخ في الدفتر. · 抄在本子上。</p></div><!--/QUIZNUOVO--></div>


#### Le schede della lezione

##### 1. Ripasso in un minuto · مراجعة في دقيقة · 1. 一分钟复习

<div class="scheda">Ripasso della volta scorsa:<br><b>PREVENZIONE</b> = il danno succede <b>meno spesso</b>.<br><b>PROTEZIONE</b> = se il danno succede, fa <b>meno male</b>.<br>Regola d'oro: <b>prima</b> togli il pericolo, <b>poi</b> proteggiti.<br>Oggi impari <b>chi</b> si occupa della sicurezza al lavoro.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">مراجعة: الوقاية = الضرر يحدث أقل. الحماية = إذا حدث الضرر يؤذي أقل. القاعدة الذهبية: أزل الخطر أولاً، ثم احمِ نفسك. اليوم تتعلم من يهتم بالسلامة في العمل.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">复习：预防 = 伤害发生得更少。防护 = 伤害发生时伤得更轻。黄金法则：先去掉危险，再保护自己。今天学习：在工作中谁负责安全。</span></div>

##### 2. La sicurezza è una squadra · السلامة فريق · 2. 安全是一个团队

<div class="scheda">In una squadra di calcio ognuno ha il suo <b>ruolo</b>: l'allenatore, il capitano, il medico, i giocatori.<br>Al lavoro è uguale: la sicurezza la fa una <b>squadra</b>, e ognuno ha il suo compito.<br>Anche <b>tu</b>, lavoratore o studente in <b>stage</b>, fai parte della squadra.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">في فريق كرة القدم لكل واحد دوره: المدرب، القائد، الطبيب، اللاعبون. في العمل الأمر نفسه: السلامة يصنعها فريق، ولكل واحد مهمته. وأنت أيضاً، عاملاً أو طالباً في التدريب، جزء من الفريق.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">足球队里每个人都有自己的角色：教练、队长、队医、球员。工作中也一样：安全由一个团队来做，每个人都有自己的任务。你也是团队的一员，不管你是工人还是实习学生。</span></div>

##### 3. Il datore di lavoro e il preposto · صاحب العمل والمشرف · 3. 雇主和班组长

<div class="scheda">Il <b>DATORE DI LAVORO</b> è il capo dell'azienda: <b>decide</b>, paga le cose per la sicurezza e <b>risponde</b> se qualcosa va male.<br>Il <b>PREPOSTO</b> è il capo-reparto: sta <b>sul campo</b> con i lavoratori e <b>controlla</b> che usino le protezioni. Se vede un pericolo, ferma il lavoro.<br>In laboratorio, a scuola, il prof fa un po' da preposto.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">صاحب العمل هو رئيس الشركة: يقرّر، ويدفع ثمن أشياء السلامة، ويتحمّل المسؤولية إذا حدث خطأ. المشرف (preposto) هو رئيس القسم: يكون في الميدان مع العمال ويراقب أنهم يستعملون وسائل الحماية. إذا رأى خطراً يوقف العمل. في مختبر المدرسة، المعلم يقوم قليلاً بدور المشرف.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">雇主（datore di lavoro）是公司的老板：他做决定，为安全花钱，出了问题要负责。班组长（preposto）是部门负责人：他在现场和工人在一起，检查大家是否使用防护。看到危险时，他会停止工作。在学校实验室里，老师有点像班组长。</span></div>

##### 4. Gli esperti: RSPP e medico · الخبراء: RSPP والطبيب · 4. 专家：RSPP 和医生

<div class="scheda">L'<b>RSPP</b> è l'<b>esperto</b> della sicurezza: studia i rischi di ogni lavoro e <b>propone</b> le soluzioni al capo.<br>Il <b>MEDICO COMPETENTE</b> è il medico dell'azienda: fa le <b>visite</b> ai lavoratori e dice se uno può fare quel lavoro.<br>La visita è <b>gratis</b> e si fa in orario di lavoro.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الـ RSPP هو خبير السلامة: يدرس مخاطر كل عمل ويقترح الحلول على صاحب العمل. الطبيب المختص هو طبيب الشركة: يفحص العمال ويقول إن كان الشخص يستطيع القيام بذلك العمل. الفحص مجاني ويتم في وقت العمل.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">RSPP 是安全专家：他研究每项工作的风险，并向老板提出解决办法。职业医生（medico competente）是公司的医生：他给工人做体检，并判断一个人能不能做这项工作。体检免费，在工作时间内进行。</span></div>

##### 5. L'RLS: la voce dei lavoratori · الـ RLS: صوت العمال · 5. RLS：工人的声音

<div class="scheda">L'<b>RLS</b> è un <b>lavoratore</b> come gli altri, <b>eletto dai colleghi</b>.<br>È la loro <b>voce</b>: porta al capo i problemi di sicurezza, controlla e fa domande.<br>Se vedi un pericolo e hai paura di dirlo al capo, puoi dirlo all'<b>RLS</b>.<br>A scuola è come il <b>rappresentante di classe</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الـ RLS عامل مثل الآخرين، ينتخبه زملاؤه. هو صوتهم: ينقل إلى صاحب العمل مشاكل السلامة، يراقب ويسأل. إذا رأيت خطراً وخفت أن تقوله للرئيس، تستطيع أن تقوله للـ RLS. في المدرسة هو مثل ممثّل الصف.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">RLS 是一名普通工人，由同事选出来。他是工人们的声音：把安全问题告诉老板，检查并提问。如果你看到危险，又不敢告诉老板，可以告诉 RLS。在学校里，他就像班级代表。</span></div>

##### 6. Il DVR: il quaderno dei rischi · الـ DVR: دفتر المخاطر · 6. DVR：风险本子

<div class="scheda">Il <b>DVR</b> (Documento di Valutazione dei Rischi) è il <b>quaderno dei rischi</b> dell'azienda.<br>Dentro c'è scritto <b>quali rischi</b> ci sono in ogni lavoro e <b>che cosa si fa</b> per abbassarli.<br>Lo fa il datore di lavoro, con l'RSPP e il medico. Si <b>aggiorna</b> quando cambia qualcosa: una macchina nuova, un reparto nuovo, dopo un infortunio.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الـ DVR (وثيقة تقييم المخاطر) هو دفتر المخاطر في الشركة. مكتوب فيه ما هي المخاطر في كل عمل وماذا نفعل لتخفيضها. يكتبه صاحب العمل مع الـ RSPP والطبيب. يُحدَّث عندما يتغير شيء: آلة جديدة، قسم جديد، بعد إصابة.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">DVR（风险评估文件）是公司的“风险本子”。里面写着每项工作有哪些风险，以及做什么来降低风险。由雇主和 RSPP、医生一起完成。有变化时要更新：新机器、新部门、发生工伤以后。</span></div>

##### 7. Le emergenze · حالات الطوارئ · 7. 紧急情况

<div class="scheda">In ogni azienda (e a scuola) ci sono gli <b>addetti alle emergenze</b>: quelli dell'<b>antincendio</b> (usano l'estintore) e quelli del <b>primo soccorso</b> (aiutano chi si fa male e chiamano il <b>112</b>).<br>Se suona l'allarme: segui il cartello <b>verde</b> dell'uscita e vai al <b>punto di raccolta</b>.<br><b>Niente ascensore, non correre, non tornare indietro</b> a prendere le cose.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">في كل شركة (وفي المدرسة) يوجد مسؤولو الطوارئ: مسؤولو مكافحة الحريق (يستعملون طفاية الحريق) ومسؤولو الإسعافات الأولية (يساعدون المصاب ويتصلون بالرقم 112). إذا رنّ الإنذار: اتبع اللافتة الخضراء للمخرج واذهب إلى نقطة التجمع. لا مصعد، لا ركض، لا تعد إلى الخلف لتأخذ أغراضك.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">每个公司（和学校）都有应急人员：消防员（会用灭火器）和急救员（帮助受伤的人，并拨打 112）。警报响了：跟着绿色的出口标志走，到集合点去。不坐电梯，不跑，不回去拿东西。</span></div>

##### 8. Informazione, formazione, addestramento · الإعلام، التكوين، التدريب العملي · 8. 告知、培训、实操训练

<div class="scheda"><b>INFORMAZIONE</b>: ti dicono quali rischi ci sono e chi sono le persone della sicurezza.<br><b>FORMAZIONE</b>: un corso per capire, come questo.<br><b>ADDESTRAMENTO</b>: provi davvero, con le mani, l'attrezzo o il DPI, con qualcuno che ti guarda.<br>Sono <b>gratis</b>, in orario di lavoro, anche per lo studente in <b>stage</b>.<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px">الإعلام: يقولون لك ما هي المخاطر ومن هم أشخاص السلامة. التكوين: دورة لتفهم، مثل هذه. التدريب العملي: تجرّب فعلاً بيديك الأداة أو وسيلة الحماية، وشخص يراقبك. كلها مجانية، في وقت العمل، وأيضاً للطالب في التدريب.</span><span lang="zh" style="display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px">告知：告诉你有哪些风险，谁是负责安全的人。培训：一门帮你理解的课，就像这门课。实操训练：在别人看着的情况下，你亲手试用工具或防护装备。这些都免费，在工作时间内进行，实习学生也一样。</span><!--QUIZNUOVO--><div style="margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px"><p><b>FINE DELLE SCHEDE · نهاية البطاقات · 卡片结束</b></p><p>Fai il ripasso qui sotto, poi il quiz su Moduli (20 casi, 5 punti l'uno, massimo 100). · راجِع ثم أجب عن الاختبار. · 先复习，再做测验。</p><p><a href="https://docs.google.com/forms/d/e/1FAIpQLSd6-FoHcINBi9ieRm4Bzv58jjb1o89T0DhM4xqB9kiUGemdTQ/viewform" target="_blank" rel="noopener" style="display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px">QUIZ su Moduli · اختبار · 测验</a></p><p><b>Sul quaderno ricopia:</b> RLS = il lavoratore eletto dai colleghi: è la loro voce. DVR = il documento con tutti i rischi e che cosa si fa per abbassarli. REGOLA D'ORO: allarme = niente ascensore, non correre, vai al punto di raccolta.</p><p lang="ar" dir="rtl">انسخ في الدفتر: RLS = العامل الذي ينتخبه زملاؤه، هو صوتهم. DVR = الوثيقة التي فيها كل المخاطر وما نفعله لتخفيضها. القاعدة الذهبية: إنذار = لا مصعد، لا ركض، اذهب إلى نقطة التجمع.</p><p lang="zh">抄在本子上：RLS = 同事选出的工人，是大家的声音。DVR = 写着所有风险以及如何降低风险的文件。黄金法则：警报 = 不坐电梯，不跑，去集合点。</p></div><!--/QUIZNUOVO--></div>


### L25 30/10/2026 — Unicode e codice ASCII

*Libro parziale: lezioni/2026-10-30_unicode-ascii.md*

#### Che cosa abbiamo fatto

1. **Quando:** 30/10/2026, ora 8-9, Informatica.
2. **Argomenti:** Il codice ASCII (A 65 01000001, B 66 01000010), solo 256 caratteri con 8 bit; Unicode, una tabella per tutte le lingue; interi e stringhe.

#### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">Ogni lettera ha un numero: A = 65 = 01000001. Con 8 bit ci stanno solo 256 caratteri: per tutte le lingue del mondo è nato Unicode.</p><p lang="ar" dir="rtl">لكل حرف رقم: A = 65 = 01000001. مع 8 بت لا يتسع إلا 256 رمزاً: لكل لغات العالم وُلد Unicode.</p><p lang="zh">每个字母都有一个数字：A = 65 = 01000001。8 个比特只能放 256 个字符：为了世界上所有的语言，有了 Unicode。</p></div>

#### La teoria e l'esercitazione

##### La lavagna del 30/10

![La lavagna del 30/10: Unicode, interi e stringhe, codice ASCII, solo 256 caratteri](../unicode/immagini/20261030_lavagna-unicode-ascii.jpg)

1. Oggi: 1) **Unicode** · 2) **Interi e stringhe**.
2. Il computer conosce solo 0 e 1: 0101010101010.
3. **Codice ASCII:** ogni lettera ha un numero. **A** = 65 = 01000001; **B** = 66 = 01000010.
4. In rosso: **solo 256 caratteri**, da 00000000 a 11111111.

<div class="scheda"><p lang="it">Perché 256? Con 8 bit ci sono 256 combinazioni: da 00000000 a 11111111. Il primissimo ASCII usava 7 bit, cioè 128 caratteri; la versione a 8 bit ne ha 256. Per tutte le lingue del mondo 256 non bastano: per questo è nato <b>Unicode</b>.</p><p lang="ar" dir="rtl">لماذا 256؟ مع 8 بت توجد 256 تركيبة: من 00000000 إلى 11111111. أول ASCII كان يستعمل 7 بت، أي 128 رمزاً؛ ونسخة 8 بت فيها 256. لكل لغات العالم 256 لا تكفي: لهذا وُلد Unicode.</p><p lang="zh">为什么是 256？8 个比特有 256 种组合：从 00000000 到 11111111。最早的 ASCII 用 7 个比特，也就是 128 个字符；8 比特的版本有 256 个。世界上所有的语言，256 个远远不够：所以有了 Unicode。</p></div>

##### La lavagna 2: Unicode e le cifre esadecimali

![La lavagna 2 del 30/10: Unicode, A U+0041, arabo U+0628, cinese U+4E2D, le cifre esadecimali](../unicode/immagini/20261030_lavagna-unicode-esadecimale.jpg)

1. Italiano/inglese: **A** = U+0041.
2. Arabo: **ب** = U+0628.
3. Cinese: **中** = U+4E2D.
4. **Cifre esadecimali:** 0 1 2 3 4 5 6 7 8 9 A B C D E F, con A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.
5. In alto a destra: ABC e lettere di altri alfabeti.

<div class="scheda"><p lang="it">In Unicode ogni carattere ha un numero, scritto con U+ e 4 cifre esadecimali. Le cifre esadecimali sono 16: dopo il 9 vengono le lettere da A (10) a F (15).</p><p lang="ar" dir="rtl">في Unicode لكل رمز رقم، يُكتب بـ U+ و4 أرقام سداسية عشرية. الأرقام السداسية العشرية 16: بعد 9 تأتي الحروف من A (10) إلى F (15). الإنكليزية/الإيطالية: A = U+0041 · العربية: ب = U+0628 · الصينية: 中 = U+4E2D.</p><p lang="zh">在 Unicode 里每个字符都有一个数字，用 U+ 和 4 位十六进制数字来写。十六进制数字有 16 个：9 后面是字母 A（10）到 F（15）。意大利文/英文：A = U+0041 · 阿拉伯文：ب = U+0628 · 中文：中 = U+4E2D。</p></div>

##### La lavagna 3: stringhe e interi

![La lavagna 3 del 30/10: stringhe e interi, '12' + '15' = '1215' e 12 + 15 = 27](../unicode/immagini/20261030_lavagna-stringhe-interi.jpg)

Due colonne: a sinistra **STRINGHE**, a destra **INTERI**.

1. 1 → 1.
2. 123 → 123: cerchiato, **NUMERI**.
3. '123' ← '123': cerchiato, **CARATTERI**.
4. 'Ciao' ← 'Ciao': **CARATTERI**.
5. '12' + '15' = '1215'.
6. 12 + 15 = 27.

<div class="scheda"><p lang="it">Con gli apici è una <b>stringa</b> (caratteri): il + attacca i testi uno dopo l'altro, quindi '12' + '15' = '1215'. Senza apici è un <b>intero</b> (numero): il + fa la somma, quindi 12 + 15 = 27.</p><p lang="ar" dir="rtl">مع علامات الاقتباس هو نص (String، رموز): علامة + تلصق النصوص واحداً بعد الآخر، إذن '12' + '15' = '1215'. بدون علامات الاقتباس هو عدد صحيح (Integer): علامة + تجمع، إذن 12 + 15 = 27.</p><p lang="zh">有引号的是字符串（String，字符）：+ 把文字一个接一个连起来，所以 '12' + '15' = '1215'。没有引号的是整数（Integer，数字）：+ 做加法，所以 12 + 15 = 27。</p></div>
<!-- LEZIONI:FINE -->

## 10. Glossario (essenziale)
1. **CPU:** processore, il "cervello" del PC.
2. **RAM:** memoria di lavoro veloce e temporanea.
3. **SSD/Hard Disk:** memoria permanente dove si salvano i file.
4. **Repository:** cartella-progetto con i file e la storia delle modifiche.
5. **Commit:** un salvataggio (una "fotografia") delle modifiche fatte.
6. **Compatibilità:** quando due pezzi funzionano bene insieme.
7. **Lazarus:** il programma con cui si creano altri programmi con finestre e bottoni; il linguaggio è il Pascal.
8. **Compilatore:** il programma che trasforma il codice Pascal in un programma che il computer sa eseguire (il file .exe).
9. **Estensione:** le lettere dopo il punto nel nome di un file (.pas, .lpi, .exe): dicono che tipo di file è.
(Il glossario completo multilingue è nel documento `glossario-l2`.)

## 11. Changelog
13. **v1.3 (30/10/2026)**: lezione L25: le lavagne 2 (Unicode e cifre esadecimali) e 3 (stringhe e interi) del 30/10, con foto e trascrizione
12. **v1.2 (30/10/2026)**: aggiunta la lezione L25 del 30/10 «Unicode e codice ASCII» con la foto della lavagna e la trascrizione.
11. **v1.1 (29/10/2026)**: lezione del 29/10/2026 (audit della giornata)
10. **v1.0 (29/10/2026)**: aggiunto il capitolo 9 «Le lezioni una per una»: le 23 lezioni dal 15/09 al 28/10, ognuna con «In breve» in italiano, arabo e cinese, la teoria e l'esercitazione (binario, Pull Request del treno, talpa, assemblaggio, rete e gamer, schede video e cavi, Lazarus); ogni lezione ha anche il suo libro parziale nella cartella lezioni.
9. **v0.9 (28/10/2026)**: aggiunto il capitolo 8 "Lazarus: il mio primo programma" (Lazarus e le sue finestre, la palette, l'esercitazione «Ciao» con ShowMessage, salva e fai partire, i file del progetto spiegati uno per uno, fallo tuo, consegna su Classroom; tre foto della lavagna del 28/10 e gli schemi da ricopiare sul quaderno); glossario e changelog diventano i capitoli 9 e 10; nel glossario Lazarus, compilatore, estensione.
8. **v0.8 (22/10/2026)**: aggiunta 6.1 "Sicurezza 1: pericolo, danno, rischio" (prima lezione del corso sulla sicurezza, con casi della vita di tutti i giorni).
7. **v0.7 (21/10/2026)**: aggiunta 7.1 "Quanto pesa un file e quanto va veloce la rete" (bit, byte, unità, Mbps, CRC, segnale 0V/5V, laboratorio del gamer) con le due foto della lavagna del 20/10.
6. **v0.6 (09/10/2026)**: aggiunta 5.2 "La lavagna del 09/10" (numeri major.minor.patch.build, ramo principale, changelog, fork, Pull Request accettata e rifiutata) con la foto.
5. **v0.5 (09/10/2026)**: aggiunta 5.1 "La storia del nostro gioco: versioni, rami, fork e merge" (grafo del Treno blindato, versioni minor e major, Godot v2.0).
4. **v0.4 (24/09/2026)**: aggiunta 2.4.1 "In parole semplici — la storia dello storage" (paginetta descrittiva con analogia).
3. **v0.3 (24/09/2026)**: aggiunta 2.4 "Lo storage: i 5 livelli" (HDD/SSD, SATA/NVMe, AHCI/NVMe, connettori SATA/M.2, interfaccia PCIe) con infografica.
2. **v0.2 (24/09/2026)**: aggiunta 2.3 "Standard e compatibilità" (form factor,
   PCIe, socket, processori per marca, RAM) e l'esercitazione "Documento sulla
   configurazione del PC".
1. **v0.1 (21/09/2026)**: prima versione. Come lavoriamo; cos'è l'informatica; il
   computer e le sue parti (+ assemblaggio + scelta pezzi); utenze e aree; Google
   Suite e Classroom; GitHub e repository; sicurezza e regole di laboratorio;
   elenco esercitazioni svolte; glossario essenziale.
