# INDICE DEI DOCUMENTI DEL CORSO

**Versione 1.0** — 21/10/2026 · Area Docente

*Spostato qui da `CLAUDE.md` il 21/10/2026 per alleggerire le chat (ogni chat rilegge CLAUDE.md a ogni avvio). Quando un documento cambia si bumpa la versione nella sua intestazione e si aggiorna la sua riga qui. Le sezioni «Prossimi passi» e «Struttura cartella godot/» sono la storia dell'inizio del corso.*

## 🗺️ Prossimi passi (roadmap immediata)

**Sessione dedicata al LIBRO DI TESTO** (richiesta da Nicola):
1. **Agganciare `corso-godot` a questa sessione** (add_repo — serve OK esplicito di Nicola).
2. **Spostare** manuale + eserciziario + template + `immagini/` dentro `corso-godot`.
3. **Nicola carica le immagini** in `manuale/immagini/` e fa push (GitHub Desktop
   o upload da browser). Divisione: Nicola droppa i file, **Claude impagina**.
4. **Claude genera il PDF impaginato definitivo** con le immagini incluse.

**Poi:** invitare la classe · primo giro **branch → Pull Request** (browser) ·
prima **Release** per i ragazzi.

## Struttura cartella `godot/`

```
godot/   (spazio di authoring dentro shiftmanager-web → poi migra nel repo corso-godot)
├── CLAUDE.md                 ← questo file (preferenze corso)
├── README.md                 ← panoramica + concetti base
├── manuale/
│   ├── manuale.md            ← LIBRO DI TESTO (teoria; fonte versionata → PDF)
│   ├── eserciziario.md       ← ESERCIZI a 4 livelli (fonte versionata → PDF)
│   ├── quaderno-studente-TEMPLATE.md ← portfolio personale dei ragazzi (MD+PDF)
│   └── immagini/             ← screenshot richiamati dal manuale
├── chirurgo-pasticcione/     ← primo gioco (backup del progetto vivo)
└── acchiappa-le-stelle/      ← mini-esempio di riferimento

Repo del corso (nicolaregge-pulse/corso-godot) — layout OBIETTIVO:
  main = area autore  ·  Release vX.Y = versione stabile per i ragazzi
  ├── manuale/           (libro di testo + eserciziario + immagini + quaderno template)
  ├── esercizi/          (Fase 1: una sottocartella per esercizio)
  └── progetto-gruppo/   (Fase 2: progetto che evolve con branch/PR/release)
```

## ⭐ Elenco documenti e versioni (indice, aggiornato 04/10/2026)

Ogni documento del corso porta un **numero di versione** nella propria
intestazione (`**Versione X.Y**`). Questo è l'indice di riferimento: quando un
documento cambia si bumpa la versione nella sua intestazione **e** si aggiorna la
riga qui sotto. La fonte di verità della singola versione resta sempre
l'intestazione del file.

### 1. Riferimento e stato
1. `00-STATO-DEL-CORSO.md` — v2.3 (fonte di verità: decisioni e stato)
2. `CORSO-INFORMATICA.md` — v1.17 (super-guida / indice generale)
3. `PROMEMORIA-NICOLA.md` — v0.7 (+ PDF v0.7; cose da fare di Nicola + roadmap cose da sviluppare con Claude)
4. `01-GLOSSARIO.md` — v1.1
5. `REGOLE-NOSTRE-CLAUDE-NICOLA.md` — v2.7 (v2.7 = tolti gli ultimi due nomi veri negli esempi dei nomi dei file; v2.6 = regola d’oro 7: PRI prioritario senza output, PPP in background; v2.5 = PPP: «fammeli» vince, se fermo vado avanti; PDF `20261004_Docente_v2.4_...`; v2.4 = tolti i nomi veri di allievi; convenzioni interne Nicola↔Claude: PPP, schema nomi file cronologia/cosa/chi + aree Comune/Docente/Regione, nome deterministico col percorso, conservazione integrale; NON sono le regole per i ragazzi)
5c. `sbobinature/README.md` (+ `TEMPLATE-sbobinatura.md`) — v0.1 (trascrizioni lezioni: conservazione integrale + versione lavorata; alimenta libro di testo, argomenti svolti e note dei ragazzi; nomi solo in scratchpad)
5d. `strumenti/nome-albero.py` (+ `README.md`) — v0.1 (script: nomi file deterministici col percorso nel nome, espandi/collassa l'albero — regola 2.13)
5e. `ATLANTE.md` (generatore `strumenti/gen_atlante.py` → pagina `docs/atlante-k4x9w2/` solo con il link + `20261013_Atlante_Docente_v1.8.pdf` con i link cliccabili; versione pubblica senza testo interno «Il parco del corso» v1.2 in `docs/cm-qma7yay4q5/parco/`) — v1.8 (v1.8 l'ufficio informazioni: zona nella mappa e capitolo 06, 21/10; v1.7 il cruscotto dal vivo, 19/10; v1.6 i tre framework e il monitor dal vivo, giro automatico, script v7.9, lezioni 15-19/10 nella mappa; v1.5 nella zona della quarta la pagina «Progetti della quarta» senza nomi; v1.4 «I documenti del prof»: punto di partenza per tutto; v1.3 leggibile sul telefono, numero di edizione in alto; v1.2 senza nomi di prodotti nelle zone; v1.1 senza il nome della scuola; 13/10: MAPPA ILLUSTRATA e cliccabile del corso «come un parco» con 12 zone; Atlante riscritto: principi, due repository, giornata di lezione, i sei bottoni, gioco e versioni, verifica, stage 4TI, automazione, materiali, libri, parole da dire a Claude, comunicazione, glossario)
5f. `CATALOGO.md` (+ `20261021_Catalogo_Docente_v1.2.pdf`) — v1.2 (21/10/2026: capitolo 02 DIDAweb e Classroom; v1.1 capitolo 01 «I tre framework»; v1.0 elenco completo di tutto quello che è stato prodotto, pagine, giochi, strumenti, script, automatismi e cartelle del riservato; separato dall'Atlante, che resta la vetrina)
5g. `docs/orientamento/` — test di orientamento per i ragazzi di terza media, pagina v1.0 + banca `banca-orientamento-v1.0.js` (21/10/2026: un'ora tutto al PC, logica, matematica, informatica pratica con il robot a blocchi, motivazione; risultati per area, profilo e valutazione A4 da stampare con la firma del docente; il nome resta solo nella pagina). Scheda del docente con la chiave nel riservato: `materiale-docente/orientamento/SCHEDA-ORIENTAMENTO.md` v1.1
5g. `METODOLOGIA-CORSO.md` (→ `METODOLOGIA-CORSO-v1.3.pdf`, generatore `strumenti/gen_metodologia.py`) — v1.3 (capitolo 09b giro delle Pull Request e come si rifà; sintesi da stampare: missione, motore, come si scrive per i ragazzi, giornata di lezione, compito, valutazione, Chiudi classe, documentazione Regione, automazione Git↔script↔Classroom, comandi, dove sta cosa, approvato/da provare)
5j. `MODUS-OPERANDI.md` (→ `20261012_Modus-Operandi_Docente_v1.5.pdf`) — v1.5 (il modo di lavorare deciso il 09/10 e il 12/10: le cinque regole prime, compito, lingue, consegne, giro delle PR, sezione dei bottoni, voti, monitor, istruzioni al docente, script, registro, privacy, automazione)
5q. `RIPARTENZA.md` — v1.5 (28/10/2026: punto 04.5, compito del mattino SENZA scadenza, regola 27; v1.4 28/10/2026 audit: punto 08.3, Chat del giorno a mezzanotte; v1.3 28/10/2026 audit: punto 08.2.4, controllore dei controlli `strumenti/controlla_controlli.py`; v1.2 28/10/2026 sera: punto 08.2.3, la Chat del giorno esegue tutti i passi di `.claude/passi-notturni.md`; v1.1 28/10/2026: sezione 08 «Stato al 28/10/2026 sera»: script v8.4 con la leva del ritmo, controlli automatici, «Chat del giorno» alle 6:47, regole 23-24, lezioni del 28/10, cose aperte; v1.0 21/10: da qui riparte ogni chat nuova)
5p. `CRUSCOTTO-DAL-VIVO.md` (→ `20261021_Cruscotto-Dal-Vivo_Docente_v1.1.pdf`; PDF della v1.2 da rigenerare) — v1.2 (29/10: cruscotto unico `docs/cruscotto/`, vista «Tutte le classi» del Piano del giorno `?tab=piano&classe=tutte`, bottoni «Scelgo questa» e «Pubblica» sempre visibili, barra fissa) · prima v1.1 (21/10: cruscotto UNICO della lezione con domande orali, Veyon e note, storico; 19/10: il framework del cruscotto del docente nato con la 3INF: righe complete, 🏁, «manca», miniature dei siti, Veyon dentro, domande con risposta, voto proposto 40-80, ordine dal più bravo, dati cifrati; strumenti `strumenti/giro_veyon.py`, `strumenti/thumb_siti.py`, `strumenti/cifra_json.py`; nel riservato `generatori/voto_3inf_oggi.py`, `correggi_3inf_portfolio.py`, `didaweb_3inf_20261019.py`)
5o. `MANIFESTO.md` — v1.2 (§9.9-9.12: cruscotto, voto proposto, pubblicazione, battito dello script) · prima v1.1 (patto Claude↔Nicola: pubblico io, verifica end-to-end, flusso che funziona, §9 il monitoraggio decide i tempi, §9.5 lezione tracciabile, §9.6 prova automatica prima del link, §9.7 monitor dal vivo, §9.8 i tre framework e i sei bottoni) + `AUDIT-MONITORAGGIO-DAL-VIVO.md` — v1.0 (18/10: perché il monitor non andava e la soluzione: script v7.9 con `AUTO_live` e `MONITOR_TOKEN`, monitor `docs/avanzamento/` ogni 5 s, relay `generatori/relay_prova.py` nel riservato)
5n. `VERIFICA-COME-SI-FA.md` (→ `20261013_Verifica-Come-Si-Fa_Docente_v1.0.pdf`) — v1.0 (13/10: come si rifà ripasso, verifica e recupero per ogni classe: pagine, prova come un ragazzo `strumenti/prova_verifica.js`, quando aprire, consegna con un clic via applicazione web dello script v7.4, correzione con fascia del docente, recupero mirato, retrospettiva, tempi per domanda nel cruscotto; passi una tantum per il docente)
5m. `AGILE-CERIMONIE.md` (→ `20261013_Agile-Cerimonie_Docente_v1.2.pdf`) + `RETROSPETTIVE.md` — v1.2 (13/10: docente e Claude lavorano in Agile; una sola sessione a fine argomento con revisione e retrospettiva, prima volta il 13/10 chiusura Treno e versioning; Definition of Done; le retrospettive restano come storia)
5l. `PROVE-METODO.md` (generatore `strumenti/prove_metodo.py`; versione con i nomi nel riservato `prove-metodo/`) — v0.1 (le prove che il metodo funziona, lezione per lezione: partecipazione, produzione, ritmo, prima e dopo i voti pubblici, recuperi, attenzione dal monitor, qualità; senza nomi, Allievo NN come nella demo)
5k. `ORGANIZZAZIONE-RAMI-CLASSI.md` (→ `20261012_Organizzazione-Rami-Classi_Docente_v1.1.pdf`) — v1.1 (4TI fuori dal treno; dal 13/10: il gioco su Godot, ramo base `prof-nicola-regge` e un ramo per classe; numeri di versione; il meglio di venerdì 09/10 e di lunedì 12/10; la giornata con il ramo della classe; cosa si prepara per martedì)
5i. `GIRO-PULL-REQUEST.md` (→ `20261012_Giro-Pull-Request_Docente_v1.0.pdf`) — v1.0 (il giro delle PR in classe, replicabile: impostazioni per lezione, cosa fa il docente, cosa fa Claude, regole di backlog e voto, script, privacy, errori del 12/10)
5h. `REGOLE-COSTRUZIONE-TEORIA.md` (+ PDF `20261009_Regole-Costruzione-Teoria_Docente_v1.2.pdf`) — v1.2 (prova del percorso come un ragazzo, nessun vicolo cieco; link esterni sempre in scheda nuova; come si costruisce la pagina di una lezione: link fisso, titolo + 2 traduzioni, percorso in alto con immagine del bottone, FASE 1 teoria solo da leggere, FASE 2 bottone verde del compito; lingue, tabelle, niente carta e penna; modello approvato `docs/compito/1inf-20261009-versioni/`)
5f. `RIFERIMENTI-E-DECISIONI.md` — v2.35 (§2.54.8 progetti dei ragazzi: solo iniziali, fuori solo la presentazione, link vero su richiesta; §2.54 comunicazione e marketing: pagina pubblica solo con il link; §2.53 casella «Chiedi aiuto all'assistente del Prof Regge» in ogni pagina, un solo bottone; §2.52 AUTOREGOLAZIONE: strumenti per regolarsi sempre nelle mani dei ragazzi, cruscotto cifrato del docente; §2.51 ordine fisso: teoria, poi compito, poi approvazione; §2.50 prima di proporre ai ragazzi: «Pubblico o vuoi vederlo prima?»; §2.49 lingue 2INF: SOLO ITALIANO (12/10 e 15/10); §2.48 modo di lavorare: pubblica, istruzioni personalizzate «Il mio punto», segui, traccia Veyon; §2.46 chi ha finito: altre materie o informatica; §2.47 media tecnica separata, non consegnati a 40; §2.45 tutta la suite Google in automatico: coda + ponte `comandi/`, automazione v5; §2.44 voti DIDAweb: materia per argomento trattato, minimo 40; §2.43 lista standard valutazioni per il docente / Valutazione complessiva della classe; §2.42 recupero a fianco: pagine semplificate docs/recupero + elenco docente riservato; §2.41 solo strumenti provati e approvati da Nicola + flusso completo fino all'archivio prove; §2.40 controllo GitHub con ricerca + git clone; §2.39 un solo compito aperto alla volta; §2.38 su Classroom solo il lavoro del giorno; §2.30.4-5 chiusura in pagina privata con un clic, ordine fisso; §2.35 assenti esclusi, §2.36 fuori compito tracciato, §2.37 controlli senza API; §2.34 consegna dei lavori GitHub generata da Claude; §2.33 in classe solo testo compito + link docente; §2.32 Veyon: solo fatti; §2.31 non cancellare PDF in docs/ durante le lezioni; §2.30 comando "Chiudi classe"; §2.28 ogni correzione → registro errori + regola, §2.29 testi Classroom impaginati; §1.10 campanelle, §2.25 registro corto, §2.26 solo il metodo del docente, §2.27 rientri Lazarus; contatti, convenzioni durature, tassonomia libri, dove stanno le cose, aperte; anti-compattamento; NIENTE nomi)

### 2. Pianificazione didattica
1. `MAPPA-ARGOMENTI.md` — v1.5 (aggiunto Google Takeout in Produttività digitale)
2. `MENU-CONTENITORI.md` — v0.1 (menu dei contenitori per i ragazzi: cosa possiamo fare + percorso a imbuto sui 4 anni)
3. `GRIGLIA-ARGOMENTI.md` — v1.17 (argomenti per anno + colonna competenze; Godot: assaggio dopo Lazarus 1ª/2ª, sviluppo 3ª-4ª)
4. `PIANO-ORE-LEZIONE.md` — v0.4 (piano ora-per-ora, 4 anni)

### 3. Regole, standard e organizzazione
1. `REGOLE-FORMATTAZIONE.md` — v1.4
2. `REGOLE-LABORATORIO.md` — v0.1
3. `REGOLAMENTO-STRUMENTI-DIGITALI-IA.md` — v0.2 (v0.2: vietato registrare la voce senza permesso e fare deepfake di voce/volto; regolamento + modulo presa visione/accettazione: strumenti informatici, servizi digitali, IA generativa)
4. `RUOLI-CLASSE.md` — v0.4
5. `STRUTTURA-REPOSITORY.md` — v1.2
5b. `STRUTTURA-REGISTRI-CLASSI.md` — v0.1 (struttura logica delle 4 classi: un Excel per classe con Allievi/Registro voti/Assenze/Allegato A; dati coi nomi solo fuori dal repo; flusso Allegato A)
6. `ORGANIZZAZIONE-GIT-ALLIEVI.md` — v0.4 (repository allievi via Classroom 50)
7. `GUIDA-NOTEBOOKLM-CLASSROOM.md` (→ `GUIDA-NOTEBOOKLM-CLASSROOM-v0.1.pdf`) — v0.1 (guida operativa docente: NotebookLM + creare un compito su Classroom, passo-passo; cosa caricare, cosa far abilitare)
8. `SCHEDA-NOTEBOOKLM-SUBITO.md` (→ `SCHEDA-NOTEBOOKLM-SUBITO-v0.1.pdf`) — v0.1 (scheda pronta "ricetta": solo i passi, la prima volta con NotebookLM, senza spiegazioni)
9. `SCHEDA-DUE-MONDI-CLASSROOM-GITHUB.md` (→ `SCHEDA-DUE-MONDI-CLASSROOM-GITHUB-v0.1.pdf`) — v0.1 (scheda chiara: Classroom vs GitHub vs NotebookLM, chi mette cosa, l'unico ponte a mano)
10. `SCHEDA-TRIADE-NOTEBOOKLM-CLASSROOM-GIT.md` (→ `SCHEDA-TRIADE-NOTEBOOKLM-CLASSROOM-GIT-v0.1.pdf`) — v0.1 (scheda triade: come gestire e lavorare al meglio con i tre; giro completo + esempio concreto)
11. `guida-docenti-alunni-non-italofoni/GUIDA-DOCENTI-ALUNNI-NON-ITALOFONI.md` (+ `guida-docenti.html` → `Guida-Docenti-Alunni-Non-Italofoni-v0.1.pdf`) — v0.1 (guida per gli altri docenti: come gestire le lezioni con alunni che non parlano italiano; principi + pratiche concrete che stiamo facendo + strumenti; esempio del quiz trilingue su Moduli con lo script e come si gestisce)
12. `manuale-docenti/generazione-modulo-google-via-script.md` (+ `.html` → `20260923_Generazione-Modulo-Google-via-Script_IT_v0.2.pdf`) — v0.2 (capitolo manuale docenti: creare un quiz su Google Moduli con uno script Apps Script; esecuzione passo-passo provata in classe, allega su Classroom, come cambiare le domande, errori da evitare)
13. `manuale-docenti/strumenti-didaweb-google/strumenti-didaweb-google.md` (sito `docs/docenti/` con indice e caselle Copia, generatore `gen_sito.py` → `20261007_Strumenti-DIDAweb-Google_Docente_v1.3.pdf`) — v1.3 (segnalibri DIDAweb: Copia HTML, Copia funzioni, Voti v1, Voti AUTO v2, Firma registro v1.2; script «Consegne Classroom → Git»: coda, raccolta, ponte, moduli, voti; pagine collegate; giro della lezione)
14. `INVENTARIO-STRUMENTI-AUTOMAZIONE.md` (→ `20261007_Inventario-Strumenti-e-Automazione_Docente_v1.0.pdf`, con `strumenti/md2pdf.py`) — v1.0 (piattaforme, modalità di lavoro, giro della lezione, automatico / semiautomatico / a mano, lezioni imparate, prossimi passi)
15. `manuale-docenti/gioco-della-classe/guida-docente-gioco-della-classe.md` (→ `20261008_Gioco-Della-Classe_Guida-Docente_v1.1.pdf`) — v1.1 (lezione di ingegneria del software: gioco «Assalto dei mostri» a pezzi, fork, Pull Request, controllo automatico, merge, conflitto, release, grafico Network; il gioco sta in `docs/giochi/assalto-dei-mostri/` del repository del corso)

### 4. Programmi per classe e documenti per la Regione
1. `classe-1/programma.md` — v0.4
2. `classe-2/programma.md` — v0.3
3. `classe-3/programma.md` — v0.2
4. `classe-4/programma.md` — v0.2
5. `PROGRAMMA-PREVENTIVO-2026-27.md` — v0.5 (parti da incollare in Allegato A; v0.5 con le voci delle lezioni fino al 12/10)
5b. `programmi-ufficiali/2026-27/` (script unico `programmi-ufficiali/_build/aggiorna_allegati.py` + `allegati_comune.py`; fonte `PROGRAMMI-DI-MASSIMA-2026-27.md` v1.0; procedura `COME-SI-AGGIORNA-ALLEGATO-A.md` v1.2) — v1.0 (14/10: i quattro Allegati A veri della scuola con la parte di Regge solo nelle aree Digitale e Tecnico-professionali, voci tecniche con sotto-voci; rosa = 2026/27, verde = anni scorsi, giallo/bianco = altri docenti; si parte SEMPRE dal file più recente della scuola, `--verifica` dopo il caricamento; originali in `originali-20261014/`, ultimi pronti in `consegna/`; consegna entro il 30/10)
6. `MIE-PARTI-ALLEGATO-A.md` — v0.2 (parti di Regge estratte dai PFP)
7. `ARGOMENTI-SVOLTI.md` — v0.3 (svolto 2025/26, nomenclatura 26/27)
7b. `ARGOMENTI-SVOLTI-2026-27.md` — v0.9 (registro attività svolte 2026/27, agganciato all'Allegato A; si aggiorna a ogni lezione)
7c. `allegato-a-stato/allegato-a-stato.md` (+ `allegato-a-stato.html` → `Allegato-A-Stato-v0.3.pdf`) — v0.3 (Allegato A stato fatto/da fare, da fare in giallo; Classi 1-4; 2/3/4 generate da MIE-PARTI con build_allegato.py)
7d. `allegato-a-2026-27/allegato-a-classe-{1,2,3,4}.md` (→ `allegato-a-classe-N-v0.1.pdf`) — v0.1 (le mie parti Regge mappate per competenza/area, pronte da incollare negli Argomenti del PFP ufficiale; sorgente per compilare poi il docx ufficiale in `programmi-ufficiali/`; generati da `gen_allegati.py`)
8. `programma-svolto/README.md` — v1.0
9. `programma-svolto/_fonti-registro-2025-26/README.md` — v1.0
10. `programmi-ufficiali/README.md` — v0.6

### 5. Manuale (libro di testo + eserciziario)
1. `manuale/manuale.md` — v0.20 (libro di testo)
2. `manuale/eserciziario.md` — v0.15 (esercizi a 4 livelli)
3. `manuale/quaderno-studente-TEMPLATE.md` — v1.0
4. `manuale/immagini/README.md` — v1.0
5. `manuale/_build/README.md` — v1.0

### 6. Materiali della Classe 1
1. `classe-1/README.md` — v1.0
2. `classe-1/MATERIALE-PRONTO.md` — v1.5 (aggiornato con i materiali di settembre 2026)
3. `classe-1/scheda-configuratore-pc.md` — v0.3
4. `classe-1/bussola-mondo-del-lavoro.md` — v0.2
5. `classe-1/da-far-fare-assolutamente.md` — v0.2
6. `classe-1/laboratorio-01-utenze-e-aree.md` — v0.1 (primo lab: login Windows + cartella in rete e account Google + Drive, prova password)
7. `classe-1/laboratorio-02-area-logica-google-classroom.md` — v0.1 (secondo lab: area logica/cartelle ad albero, giro Google Suite, iscrizione a Classroom; ripasso sicurezza)
8. `classe-1/glossario-l2/glossario-l2.md` (+ `glossario.html` → `Glossario-L2-v1.0.pdf`) — v1.0 (glossario multilingue IT · EN · cinese semplificato caratteri+pinyin · arabo; PDF da HTML per i font CJK/arabo)
8b. `classe-1/attivita-blocchi/attivita-blocchi.md` (+ `attivita-blocchi.html` → `attivita-blocchi-v0.1.pdf`) — v0.1 (attività jolly "tempo libero": primo gioco con i blocchi / Ora del Codice; trilingue IT/AR/ZH, a prova di errore, browser)
8c. `classe-1/github-crea-account/github-crea-account.md` (+ `github-crea-account.html` → `20260917_Classe-1-PerTutti_v0.2_Crea-Account-GitHub_multilingua.pdf`) — v0.2 (prima lezione Git: crea account GitHub con email scuola ed entra; trilingue IT/AR/ZH; bottoni per posizione/colore, indirizzi marcati; nota "provare prima i permessi/posta esterna")
8d. `classe-1/consegna-senza-tastiera/consegna-senza-tastiera.md` (+ `.html` → `consegna-senza-tastiera-v0.1.pdf`) — v0.1 (supporto per allievo senza tastiera / che non scrive in italiano: via sicura foglio+foto, via digitale scrittura a mano col mouse; cinese+italiano con disegni; nessun nome di allievo per privacy)
8e. `classe-1/ricerca-github/ricerca-github.md` (+ HTML IT/AR/ZH → `Ricerca-GitHub-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna: piccola ricerca "cos'è GitHub e cos'è un repository", guardando il sito e cercando in rete; si scrive in Google Documenti e si consegna su Classroom; attività di avvicinamento prima di creare gli account; niente login necessario; 3 file monolingui)
8f. `classe-1/costruisci-pc/costruisci-pc.md` (+ HTML IT/AR/ZH → `Costruisci-PC-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna: montare un PC con it.pcpartpicker.com in modalità Builder, componenti compatibili a budget; lista+prezzo in Google Documenti, consegna su Classroom; 3 file monolingui)
8g. `classe-1/componenti-pc-compito/componenti-pc.md` (+ HTML IT/AR/ZH → `Componenti-PC-IT/AR/ZH-v1.0.pdf`) — v1.0 (consegna dopo i componenti fisici: spiegare a cosa serve ogni pezzo con parole proprie + domande personali anti copia/AI; consegna su Classroom o foto; 3 file monolingui)
8h. `classe-1/regole-fine-lavoro/regole-fine.md` (+ HTML IT/AR/ZH → `Regole-Fine-Lavoro-IT/AR/ZH-v1.0.pdf`) — v1.0 (regole di laboratorio 'quando hai finito o non hai niente da fare': no giochi/YouTube/rumore, resti al posto, blocca/esci col Ctrl+Alt+Canc, + cosa fare di utile; 3 file monolingui da caricare su Classroom)
8i. `classe-1/libro-di-testo/libro-classe1.md` (+ `_build/libro-classe1.html` → `libro-classe1-v0.9.pdf`, 22 pagine) — v0.9 (v0.9: capitolo 8 «Lazarus: il mio primo programma» del 28/10, con le tre foto della lavagna; glossario e changelog diventano 9 e 10; v0.8: 6.1 Sicurezza 1, pericolo, danno, rischio; v0.7: 7.1 bit, byte, Mbps, CRC, segnale 0V/5V, laboratorio del gamer, foto della lavagna del 20/10; v0.6: 5.2 lavagna del 09/10, numeri major.minor.patch.build; v0.5: 5.1 versioni, rami, fork, merge del Treno blindato; LIBRO DI TESTO Classe 1: raccoglie appunti/teoria/esercitazioni; cresce a ogni lezione; PDF per leggere, MD per l'AI dei ragazzi)
8i2. `classe-1/utenze-password/utenze-password.html` (→ `20260923_Le-Mie-Utenze-Password_Classe-1-PerTutti_multilingua_v1.0.pdf`) — v1.0 (scheda da compilare a penna: utenze e password di computer scuola/Google/GitHub; trilingue IT/AR/ZH, una pagina, con nota di sicurezza "tienila al sicuro")
8j. `classe-1/accesso-blocco-schermo/accesso-blocco-schermo.md` (+ `.html` → `Accesso-Blocco-Schermo-v1.0.pdf`) — v1.0 (scheda UNICA trilingue: Ctrl+Alt+Canc — login/logout, blocca/sblocca schermo; spiega tutte le voci del menu; con disegno della schermata; separata dalle Regole)
8k. `classe-1/regole-classe/regole-classe.md` (+ `.html` → `Regole-Classe-v1.1.pdf`) — v1.1 (scheda UNICA trilingue: regole di comportamento in classe — alzare la mano ben alta + cenno del docente; attenzione/lavoro con l orologio sulla lavagna, niente YouTube, si aspetta l esercitazione su Classroom)
8l. `classe-1/versioning/versioning.md` (+ `.html` → `Versioning-v2.3.pdf`) — v2.3 (scheda UNICA trilingue: flusso completo delle versioni, major/minor, ripartenza da .0 con nuova linea a ogni release principale; pagine con alberi eterogenei; grafo complesso stile Git a 4 rami paralleli con branch/merge, che termina in 2 versioni principali v1.x e v2.0)
8m. `classe-1/quiz-regole-versioning/` — v1.1 (md v1.1, PDF ancora v1.0; quiz per Google Moduli su Regole della classe + Versioning; `crea-modulo.gs` = script Apps Script che crea il Modulo-quiz in 1 clic, 12 domande trilingui IT/AR/ZH con punteggio automatico; `quiz-regole-versioning.md` + `.html` → `Quiz-Regole-Versioning-v1.0.pdf` = istruzioni passo-passo + chiave risposte per il docente; si allega come Compito su Classroom)
8n. `classe-1/lezione-versioni-treno/lezione-versioni-treno.md` (generatore `_build/gen_lezione_versioni.py` → pagina `docs/lezione-versioni/` + `20261009_Lezione-Versioni-Treno_Classe-1-2-PerTutti_multilingua_v1.0.pdf`) — v1.0 (09/10, 1INF e 2INF: la storia del Treno blindato nel grafo di Git — versione, ramo, fork, Pull Request, merge, minor/major, release; trilingue IT/AR/ZH; la storia si legge dai versioni.json dei giochi)
8p. `treno-prof-godot/` (export web `docs/giochi/treno-prof/`, ramo Git `prof-nicola-regge`) — v1.0 (BASE DEL PROF su Godot 4.7, da cui partono i rami delle classi: il treno della 2INF v0.31 portato su Godot, neutro (niente facce né nomi di una classe), vetro che si crepa dai bordi verso il centro; dati in `dati/*.json`, dopo ogni modifica si riesporta; `strumenti/congela_versione.py` per le versioni ferme)
8o. `treno-blindato-godot/` (export web `docs/giochi/treno-godot/`, ramo Git `treno-godot`) — v2.0 (il Treno della 1INF v1.1 rifatto con Godot 4.7: versione major; dati in `dati/*.json`; grafo `docs/giochi/grafo/` con fork, ramo «immagini» + merge e v2.0)
9. `classe-1/esercizio-presentazione-famiglia/` — v1.2 (esercizio "Io e la mia famiglia": presentazione di sé/famiglia con Google Documenti + consegna su Classroom; passo-passo "a prova di errore" con spiegazione dei 2 link + nota su indirizzi/bottoni nelle 3 lingue. Fonte `esercizio-presentazione-famiglia.md`; **3 file monolingui** `...-IT/AR/ZH-v1.2.pdf` + versione unica trilingue `...-v1.2.pdf` + **versione ILLUSTRATA** `...-IMMAGINI-v1.2.pdf` (disegni con frecce + QR per Classroom, per chi non legge italiano; `esercizio-immagini.html`))
10. `classe-1/negozio-online/GUIDA-RAGAZZI.md` — v1.5
11. `classe-1/negozio-online/PIANO-LEZIONE.md` — v1.1
12. `classe-1/negozio-online/README.md` — v1.0

### 6b. Materiali della Classe 2
1. `classe-2/condizioni-if-then.md` — v0.1 (condizioni SE/ALLORA: IFTTT, funzione SE di Google Fogli, social, Lazarus if/then/else)
2. `classe-2/if-annidati/` (generatori `_build/gen_if_annidati.py`, `gen_cinema.py`; pagina unica `docs/2inf-if/`) — v1.0 (05/10: dispensa if/then/else e if annidati con la regola dei rientri §2.27, riscaldamento R1-R4, gioco Indovina il numero a 4 livelli + compito; 08/10: Il cassiere del cinema, 3 if annidati, or, CheckBox, tabella di prova + compito)
3. `classe-2/lazarus-convertitore/` — v1.0-2.2 (convertitori mph/km/h e temperature, 29/09-01/10) · `classe-2/sicurezza-1ora-rischio-danno/quiz/` — v1.0 · `classe-2/sicurezza-phishing/` — v1.0 (Email sicura o truffa)

### 6c. Materiale trasversale (tutti gli anni)
1. `INTELLIGENZA-ARTIFICIALE.md` — v0.1 (IA: Gem vs Agenti autonomi; con Gemini)
1b. `corso-docente-ai/corso-agenti-gem.md` (→ `20260923_Corso-Agenti-e-GEM_Docente_v1.0.pdf`) — v1.0 (CORSO PER IL DOCENTE su Agenti e GEM: i tre livelli chat/GEM/agente, creare un Gem in Gemini passo-passo, "simulare un professionista", ricettario di 5 Gem pronti da copiare, cenni sugli agenti, regole/privacy, piano in 3 passi; area Docente)
2. `INVALSI-GRADO10-2025-26.md` — v1.1 (analisi dati INVALSI grado 10 2INFSPE; area Sicurezza = solo 4.1/4.2 + mappa 22 quesiti)
3. `RECUPERO-INVALSI.md` — v0.2 (piano recupero lacune DigComp: sicurezza 4.1/4.2 sui 5 temi misurati + comunicazione area 2)
4. `RECUPERO-INVALSI-esercizi.md` — v0.1 (schede + esercizi a scenario + laboratorio pratico: finta mail phishing, wi-fi non sicuro, cookie)
6. `sicurezza-deepfake/` (generatore `_build/gen_deepfake.py`; pagina `docs/sicurezza-deepfake/`, quiz `docs/quiz/?b=sicurezza-deepfake`; PDF IT/AR/ZH; `SCHEDA-DOCENTE-deepfake-v1.0.pdf`; modello di compito Classroom nel riservato `coda/modelli/`) — v1.0 (voci e volti falsi: cos'è, segnali d'allarme, parola d'ordine di famiglia, regole della scuola, cosa fare; tutte le classi)
5. `quiz-recupero-invalsi/index.html` + `README.md` — v1.0 (quiz HTML autocorreggente, 18 scenari; pubblicabile su GitHub Pages)

### 7. Materiali della Classe 3
1. `classe-3/reti-teoria.md` — v0.2
2. `classe-3/esercizi/01-cablaggio-rj45.md` — v0.1
3. `classe-3/troubleshooting-guasti.md` — v0.1 (kit diagnosi guasti: teoria a crocette + guasti fisici) — Panaccione
4. `classe-3/corso-html-css.md` — v0.1 (corso base HTML5/CSS, con pubblicazione su Pages) — Panaccione
5. `classe-3/comunicazione-digitale/comunicazione-digitale.md` (+ `.html` → `Comunicazione-Digitale-v0.1.pdf`) — v0.1 (contenitore "Addetto alla comunicazione digitale" per la terza, nato dai bisogni delle aziende di stage: contenuti/siti/social/Facebook; profilo + competenze + 6 moduli + progetto finale, strumenti browser, legami con e-commerce/HTML-CSS/stage; bozza da confermare)
6. `classe-3/sito-github/` (generatori `_build/gen_sito_github.py` e `gen_sito_github_2.py` → PDF IT e IT-BN; la chiave DOCENTE va nel repo riservato `materiale-docente/`; pagina unica `docs/3inf-sito/` con bottoni Copia ed esempio vivo) — v1.0 (05/10: Dispensa 1 pagina web da zero con index.html + style.css separati, Dispensa 2 pubblicazione su GitHub Pages, Compito primo sito pubblico; 07/10: Dispensa 3 modifica su GitHub, commit e History + Compito 3; 08/10: Dispensa 4 seconda pagina e menu + Compito 4)
7. `classe-3/pagina-html-locale/` — v1.0 (30/09: pagina HTML locale, CSS separato, mini-compiti, sfida finale; IT e IT-BN) · `classe-3/cosa-e-git/` — v1.0-2.1 (Git, versioning; il file IT-BN è `20260925_Classe-3-PerTutti_v1.3_Compito-Git-Versioning_IT-BN.pdf`)
8. `classe-3/sito-github/` 08/10 (generatori `_build/gen_competenze_3inf.py`, `gen_squadra_3inf.py`) — v1.0 (Dispensa 5 + Compito «Il mio portfolio: cosa so fare», rimandato; Dispensa 6 + Compito 4 «Lavoriamo come un'azienda»: il gioco della classe con fork, Pull Request, merge, versioni; IT e IT-BN)

### 7b. Materiali della Classe 4
1. `classe-4/reti-iso-osi/` (generatore `_build/gen_iso_osi.py`; pagina unica `docs/4ti-iso-osi/` con la pagina interattiva Il viaggio di un pacchetto) — v1.0 (06/10: scheda dei 7 livelli + compito Il viaggio del mio messaggio + quiz personale)
2. `classe-4/git-ai-notebooklm/` — v1.0-1.1 (29/09: Git e AI con NotebookLM; la chiave del quiz versioning sta nel repo riservato)
3. `docs/4ti-app/` — v1.0 (06/10: pagina «App di reti» con elenco estendibile; prima app `viaggio-iso-osi.html` «Il viaggio di un messaggio»: teoria dei 7 livelli, simulazione PC A → switch → router → server con byte reali (Ethernet, IP, TCP, FCS calcolati), vista per livello con comunicazione virtuale e percorso reale; un solo file, nessuna libreria; l'esempio usa l'indirizzo vero del sito del corso)

### 7c. Settimana, quiz e pagine del sito
1. `orario/settimana-2026-10-19.md` — v1.0 (orario 19-23/10, dal registro) · `orario/settimana-2026-10-05.md` — v1.0 (orario 5-9/10) · `orario/piano-settimana-2026-10-05.md` (→ `Piano-Settimana-2026-10-05-v1.0.pdf`) — v1.0 (lezione per lezione: materiali, compiti in coda, testi registro ≤40 caratteri)
2. `docs/quiz/` — v1.0 (motore unico del quiz personale: `?b=banca&n=compito&timer=1`; banche in `docs/quiz/banche/`: `4ti-iso-osi`, `2inf-if`, `1inf-sicurezza-1`; uscita da incollare nel Documento, raccolta automatica)
2c. `docs/verifica/` — v1.0 (13/10: motore unico di RIPASSO → VERIFICA → RECUPERO in HTML, riutilizzabile per tutte le classi: `?b=<banca>` ripasso con schede e allenamento corretto subito; `&modo=verifica` e `&modo=recupero` si aprono solo quando il prof dice «attiva» (file `docs/verifica/stato/<banca>.json`); crocette in ordine personale, domande personali con le PR vere del ragazzo, scale 1-5, grafico dei dati; antiplagio: niente incolla, uscite dalla pagina, tempo di scrittura; voto = giudizio complessivo del prof; pagina pubblica `risultati.html?b=` da `risultati/<banca>.json`; `&anteprima` per il prof; banche in `docs/verifica/banche/`, prima: `2inf-versioning`)
2d. Lezioni del 19/10 nel motore `docs/verifica/`: banche `3inf-portfolio` (sito personale → portfolio, scheda 11 collaboratori per il lavoro in coppia del 21/10; regia per il docente `classe-3/sito-github/20261019_Classe-3_Regia-Portfolio_Docente_v1.0.pdf`; controllo dei siti `generatori/portfolio_3inf.py` → «Il mio punto») e `2inf-for2` (ciclo FOR seconda parte); domanda «incolla qui» (`incolla: true`) unica dove si può incollare; prova `strumenti/prova_verifica.js` — v1.0
2e. Lezioni del 21/10 (un compito + un annuncio per classe, quiz su Google Moduli, verifiche delle pagine chiuse): `1inf-gamer` (+ `classe-1/gamer/`), `2inf-sicurezza-3ora` (+ `classe-2/sicurezza-3ora/`, v1.1 del 28/10/2026: tolto il link al sito della Regione), `3inf-grafica-pr` (+ `classe-3/sito-github/grafica-pr/`) e la pagina `docs/3inf-albero/` «L'albero del mio sito» (struttura letta da GitHub: una chiamata con ETag, riserva jsDelivr, attesa 30 s; controlla file richiesti, nomi, cartella img, collegamenti rotti, sfondo e animazione). Documento MD+PDF di ogni lezione generato dalla banca con `strumenti/banca2md.py` — v1.0
2f. Lezione del 22/10 della 2INF nel motore `docs/verifica/`: banca `2inf-salvadanaio` «Il mio salvadanaio» (FOR + WHILE, sfida con mod; incipit del codice con i punti // QUI, FATTO! a ogni pezzo, consegna del codice nella domanda «incolla qui»; circa 2 ore) + `classe-2/salvadanaio/` (MD + PDF dalla banca); soluzione e griglia per il docente nel riservato — v1.0
2g. Lezione del 22/10 della 1INF nel motore `docs/verifica/`: banca `1inf-sicurezza-1ora` «Sicurezza 1: pericolo, danno, rischio» (prima ora del corso sulla sicurezza; solo casi della vita dei ragazzi, niente leggi; italiano con arabo e cinese; 8 schede, 13 domande di ripasso, 20 casi uguali al quiz su Moduli), documento `classe-1/sicurezza-1ora/` MD+PDF v1.0 e ossatura della 2ª lezione (prevenzione e protezione) `classe-1/sicurezza-1ora/ossatura-2a-lezione.md` v0.1; libro della Classe 1 v0.8. `banca2md.py`: le righe in arabo e cinese diventano paragrafi a parte; `md2pdf.py`: paragrafi con direzione automatica (arabo a destra)
2b. `docs/recupero/` (generatore `strumenti/gen_recupero.py`) — v1.0 (recupero a fianco: pagine semplificate un'azione per passo per 2inf-github, 2inf-indovina, 3inf-sito; senza nomi)
3. `docs/1inf-conversione/` — v1.0 (decimale → binario interattivo, numeri personali, timer) · `docs/1inf-divisioni/` — v1.0 · `docs/1inf-decimale-binario/` (teoria e compiti v1.2-1.4, trilingue)
4. `REGISTRO-ERRORI-CLAUDE.md` — v2.88 (#139: un ROSSO non si liquida come atteso; v2.87 cognomi sostituiti dalle iniziali) · `MAPPA-REGOLE-CONTROLLI.md` — v1.2 (29/10/2026: regola 30, bottone «Serve te» del cruscotto) · prima v1.1 (28/10/2026 audit: stato della notte e controllore dei controlli; v1.0 28/10/2026: tutte le 168 voci del registro con schema e controllo che le copre, A automatico / B notturno / C superata / D scoperta; conteggi e perché delle scoperte) · `.claude/hooks/LEGGIMI-controlli.md` — v1.2 (i controlli automatici, con le prove) · `.claude/passi-notturni.md` — v1.4 (passi obbligatori della Chat del giorno; v1.4: 04.1 scelta con il bottone «Scelgo questa» del cruscotto, si pubblica solo dopo «pubblica»; v1.3: 04.1 anche la 4TI il martedì; v1.2: 02.12 compito SENZA scadenza, regola 27) · `CHECKLIST-LEZIONE.md` — v1.5 (v1.5: 02.3 compito del mattino SENZA scadenza, regola 27; tutti gli errori come controlli prima, durante e dopo la lezione; 02.6 verifica_lezione.py prima di dire «pubblicato»; v1.4 rimando alla mappa e ai passi notturni; rimanda ai controlli automatici in `.claude/hooks/LEGGIMI-controlli.md`; PDF `20261026_Checklist-Lezione_v1.0.pdf`) · `REGISTRO-ORE-2026-27.md` — v1.1 · `INDICE-GENERALE.md` — v1.0 · `AUDIT-REPOSITORY-2026-10-02.md` — v1.0 · `RETROSPETTIVA-25-09-2026.md` — v1.0 · `SCHEMA-CLASSI-TIPOLOGIE.md` — v1.1 (4TI = classe articolata di 2 gruppi; il gruppo 4INF di Nicola è di 9)

### 8. Altri materiali e prototipi
00. `comunicazione-marketing/README.md` — v0.7 + `EDIZIONI.md` v1.4 (EDIZIONE 1.4 del 19/10: «Una mattina con la terza» e la demo del cruscotto senza nomi `docs/demo/cruscotto/`; EDIZIONE 1.2: «Progetti della quarta» senza nomi, link vero su richiesta) (EDIZIONE 1.0 del 13/10, controllo `strumenti/controlla_edizione.py --browser`, commit bd2a58004f; 13/10: NIENTE MARCHI DI ALTRI né immagini non nostre; NIENTE NOME DELLA SCUOLA nei materiali per l'esterno, si chiama «Il laboratorio di informatica secondo le idee di Nicola Regge»; con il parco del corso (mappa + Atlante) e il testo per Gemini; COMUNICAZIONE E MARKETING, i materiali per scuole e aziende, genitori, ragazzi e chi non capisce di informatica: PDF, percorsi guidati con voce, demo; pagina pubblica solo con il link `docs/cm-qma7yay4q5/` con il racconto «Cinque giorni da azienda» e i PDF; inventario e regole)
0. `presentazione-demo/` (generatori `gen_brochure.py`, `gen_presentazione.py`; demo in `docs/demo/` con `strumenti/gen_demo.py` e lo script `strumenti/demo-accesso.gs` nell'account PERSONALE) — v1.0 (materiale promozionale del metodo: brochure commerciale A4 con le schermate vere, nomi sostituiti; demo con accesso via email e codice 24 ore e notifica di ogni pagina; «Prova il sistema come un allievo» `docs/demo/prova/`; la giornata della 2INF del 12/10 senza nomi `docs/demo/giornata/`)
1. `README.md` (radice) — v1.0
2. `battaglia-navale-3d/README.md` — v1.0

### 9. Libro combinato (generato)
1. `LIBRO-COMPLETO.md` / `LIBRO-COMPLETO-vX.Y.pdf` — v1.74 (assemblato in automatico da `classe-1/_build/`; la versione è `LIBRO_VERSION`; copertina/footer "classi 1,2,3,4" + frontespizio per ogni Parte-classe; include ora il Libro di Testo Classe 1).

### 10. Attestati (non testuali)
1. `attestati/ATTESTATO-RUOLI.html` → `ATTESTATO-RUOLI-v0.4.pdf` (unico PDF, 4 pagine, con logo Piamarta).


### 11. Dispense Classe 1 (una per lingua)
1. `classe-1/byte-velocita/dispensa-rete-gamer/20261023_Classe-1-Dispensa_v1.0_Rete-Gamer_{IT,ZH}.md/.pdf` e `..._v1.1_Rete-Gamer_AR.md/.pdf` — IT/ZH v1.0, AR v1.1 (28/10/2026: font Amiri completo, parentesi non più invertite; changelog in coda; la pagina docs/1inf-misure punta alla v1.1 araba). v1.0 (23/10/2026: ping, jitter, TCP/UDP, FPS/Hz, pixel, monitor, scheda video, cavi video; foto lavagna, esempi, «Prova tu»; generatore `_build/genera.py` + `_build/pdf.js`).
2. `classe-1/byte-velocita/dispensa-rete-gamer/20261023_Classe-1-Linee-Guida_v1.0_Documento-Rete-Gamer_{IT,ZH}.md/.pdf` e `..._v1.1_Documento-Rete-Gamer_AR.md/.pdf` — IT/ZH v1.0, AR v1.1 (28/10/2026: font Amiri completo, parentesi giuste, changelog in coda). v1.0 (23/10/2026: linee guida del compito su Google Documenti, almeno 1500 parole, 13 capitoli personali, creare/contare parole/consegnare, regole antiplagio; `python3 _build/genera.py linee` + `node _build/pdf.js Linee-Guida`).
3. `classe-1/lazarus-ciao/20261028_Classe-1_v1.0_File-Lazarus-Lavagna_Docente.md/.pdf/.html` — v1.0 (28/10/2026, documento per il docente, solo italiano: i file di un progetto Lazarus 4 «ciao» spiegati per estensione, .lpi .lpr .pas/.pp .lfm .lps .res .ico .exe, cartelle lib\x86_64-win64\ e backup\; tabella «tenere o si rifà» e schema da scrivere alla lavagna; 4 pagine).
4. `classe-1/lazarus-ciao/20261028_Classe-1_v1.0_Lazarus-Primo-Programma_{IT,AR,ZH}.md/.pdf/.html` — v1.0 (28/10/2026, dispensa per gli allievi, una per lingua, traduzione completa: che cos'è Lazarus, partenza pulita con progetto e cartella nuova, le finestre, la palette, l'esercitazione «Ciao» con `ShowMessage('Ciao ' + Edit1.Text);`, salva e fai partire, i file del progetto uno per uno, fallo tuo, consegna su Classroom; schemi da ricopiare sul quaderno e tre foto della lavagna; IT 11 pagine, AR 14, ZH 11; generatore `_build-dispensa/genera.py` + `node _build-dispensa/pdf.js`; Amiri completo in `strumenti/render-pdf/fonts/Amiri-*.ttf` perché il sottoinsieme woff2 sbagliava le parentesi nell'arabo).
5. Dispense arabe rifatte il 28/10/2026 con il font Amiri completo (`strumenti/render-pdf/fonts/`; prima le parentesi uscivano invertite), changelog in arabo in coda, dall'HTML monolingue già nel repo: `classe-1/bit-e-byte/Dispensa-Bit-Byte-AR-v1.2.pdf` (era v1.1), `classe-1/decimale-binario/Dispensa-Decimale-Binario-AR-v1.3.pdf` (era v1.2; link aggiornato in `docs/1inf-decimale-binario/`), `classe-1/decimale-binario/Dispensa-Facilissima-Binario-AR-v1.2.pdf` (era v1.1), `classe-1/nome-e-colori/Dispensa-Nome-Colori-AR-v1.2.pdf` (era v1.1; link aggiornato in `docs/1inf-nome-colori/`). Restano col vecchio font (da rifare se servono di nuovo): compiti, schede e documenti multilingua di settembre-ottobre.

### 12. Classe 3
1. `classe-3/pascal-vs-java/20261026_Classe-3-Teoria_v1.0_Object-Pascal-e-Java_IT.md/.pdf` — v1.0 (26/10/2026, solo italiano: in 3INF non servono arabo e cinese; Hello World, variabili senza new, finestra con un bottone, riassunto; `python3 _build/genera.py teoria` + `node _build/pdf.js Object-Pascal`).
2. `classe-3/eclipse-java/20261028_Classe-3_v1.1_Eclipse-Hello-World.md/.pdf/.html` — v1.1 (28/10/2026, aggiunti due errori comuni con schermata: «Unresolved compilation problem» con la X rossa su import javax.swing e «A package name must be specified for a module», soluzione cancellare module-info.java; riquadro rosso al passo della spunta module-info; 21 pagine). Precedente: v1.0 (28/10/2026, guida per gli allievi IT + riga in bangla, con 15 schermate reali di Eclipse 2026-09: ZIP in cartella corta, primo avvio, progetto HelloWorld, classe Main, codice Swing con `JOptionPane.showMessageDialog`, Lazarus e Java a confronto, codice riga per riga, errori comuni; 23 passi, 18 pagine; pagina con spunte `docs/3inf-eclipse-guida/`, collegata dalla lezione `docs/verifica/?b=3inf-eclipse-java`; `python3 _build/guida.py` + `node _build/pdf.js`).
