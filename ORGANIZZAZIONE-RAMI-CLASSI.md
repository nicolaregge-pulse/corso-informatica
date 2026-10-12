# Il ramo del prof e i rami delle classi

**Versione 1.0** — 12/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano. Area Docente.

Come si organizza il lavoro sul gioco della classe da martedì 13/10/2026: un solo gioco di base, sul ramo del prof, da cui partono tutte le classi. Mette insieme il meglio della lezione di venerdì 09/10 (1INF) e di quella di lunedì 12/10 (2INF e 3INF). Il giro delle Pull Request in classe resta quello di `GIRO-PULL-REQUEST.md`; le regole di lavoro restano quelle di `MODUS-OPERANDI.md`.

## 00 L'idea in breve

1. Il gioco «Il treno blindato» passa su **Godot**: il codice lo scrive Claude, i ragazzi non toccano Godot. Le loro Pull Request (PR) arrivano dal Modulo «Consegna», come lunedì.
2. Esiste **un ramo del prof**, `prof-nicola-regge`: è la **base** comune. La versione v1.0 è il treno della 2INF (v0.31) portato su Godot, con il vetro che si crepa dai bordi verso il centro.
3. **Ogni classe ha il suo ramo**, che parte dalla base: `classe-1inf`, `classe-2inf`, `classe-3inf`, `classe-4ti`. Le PR di una classe cambiano solo il ramo di quella classe.
4. Quando il prof migliora la base (un difetto corretto, una regola nuova per tutti), la modifica **si unisce (merge)** nei rami delle classi. È il modo in cui lavorano i progetti veri: una base comune e tante copie che la seguono.

> **Da confermare:** la base è «neutra»: niente facce né nomi di una classe. Ogni classe aggiunge sul suo ramo le sue facce, i suoi cattivi e i suoi nomi.

## 01 I rami e i numeri di versione

| Ramo | Di chi | Numeri | Esempio |
|---|---|---|---|
| `prof-nicola-regge` | del prof: la base | PROF v1.0, v1.1, v1.2… | PROF v1.1 «vetro più resistente per tutti» |
| `classe-1inf` | della 1INF | 1INF v1.0.1, v1.0.2… | 1INF v1.0.3 «il cattivo con il casco rosso» |
| `classe-2inf` | della 2INF | 2INF v1.0.1, v1.0.2… | |
| `classe-3inf` | della 3INF | 3INF v1.0.1, v1.0.2… | |
| `classe-4ti` | della 4TI | 4TI v1.0.1, v1.0.2… | |

1. Il numero di una classe dice da quale base parte: 1INF **v1.0**.3 è la terza versione della 1INF costruita sulla base PROF v1.0.
2. Quando la base passa a v1.1 e si unisce nel ramo della classe, la classe ricomincia da v1.1.1. Così i ragazzi vedono da soli che cosa vuol dire «portare dentro gli aggiornamenti».
3. Ogni versione resta giocabile nella sua cartella ferma, come oggi; il grafo delle versioni mostra tutti i rami con i loro colori.

## 02 Il meglio di venerdì 09/10 (1INF)

1. **La storia nel grafo:** versioni, rami, fork, merge, minor e major spiegati sul gioco della classe, con i pallini veri da cliccare. Funziona: si tiene come teoria per ogni classe nuova.
2. **Fallo tuo:** le facce e i cattivi consegnati dai ragazzi entrano nel gioco con il loro nome. È il gancio più forte: sul ramo della classe si rifà.
3. **Una domanda alla volta con «Avanti»** nel compito trilingue: chi legge poco l'italiano non si perde.
4. **Da non rifare** (registro errori #41-#45): pubblicare senza chiedere; un primo passo che chiede la foto o il telefono; attività a mano che fanno perdere metà lezione.

## 03 Il meglio di lunedì 12/10 (2INF e 3INF)

1. **Il Modulo «Consegna» unico** per tutte le PR, con le quattro parti: Titolo, Cosa cambia, Dove, Perché.
2. **Il backlog con i pesi di Fibonacci**, pubblico: ognuno vede la sua richiesta in coda e poi FATTO con la versione, oppure NO con il motivo.
3. **Una PR = una versione** con il suo changelog e il nome di chi l'ha chiesta: 20 versioni in tre ore.
4. **I voti pubblici durante la lezione:** dopo la pubblicazione delle 13:22 un allievo è passato da 40 a 62 in pochi minuti. Si pubblicano **a metà lezione**, non solo alla fine.
5. **I bottoni in alto nella pagina del compito:** voti, backlog, monitor, novità, classifica, valutazione dei singoli (solo prof).
6. **Il monitor Veyon** con i soli fatti; i voti congelati all'ora decisa dal docente; il PDF della valutazione per allievo.
7. **Da non rifare** (registro errori #49-#59): una pagina copiata da un'altra classe con un'altra lingua; più processi che scrivono su Git insieme; lo script fermato dal limite di GitHub; una richiesta del docente lasciata indietro.

## 04 La giornata con il ramo della classe

| Quando | Chi | Cosa |
|---|---|---|
| La sera prima | Claude | crea il ramo della classe dalla base (se non c'è), prepara la pagina del compito con i bottoni, il file delle impostazioni della lezione e il Modulo Feedback; manda il link al docente |
| La sera prima | Docente | guarda la pagina e dice «pubblica» |
| Inizio lezione | Docente | firma il registro con il programma previsto (entro le 14:05) |
| FASE 1, 20-30 minuti | Ragazzi | leggono la teoria; chi è nuovo gioca la versione della sua classe |
| FASE 2 | Ragazzi | Feedback, poi le PR dal Modulo «Consegna» |
| Durante | Claude | un solo giro automatico che scrive su Git; mette nel gioco le PR in ordine di backlog: modifica il codice Godot, esporta per il browser, controlla, pubblica la versione |
| Metà lezione | Claude | pubblica i voti e la classifica |
| Giri Veyon | Docente e Claude | il docente manda la schermata, Claude la trascrive nel monitor |
| Fine lezione | Docente | dice a che ora si congelano i voti |
| Fine lezione | Claude | voti congelati, PDF per allievo, argomenti svolti aggiornati |

## 05 Martedì 13/10: cosa si prepara

1. **Ramo `prof-nicola-regge` con la base PROF v1.0 su Godot**, provata nel browser e sul telefono. Il docente la prova e dice se va bene.
2. **Una o due versioni del prof** questa sera, per vedere il giro completo sul ramo nuovo.
3. **1INF (8-10)**: ramo `classe-1inf` dalla base, con le facce della classe già consegnate venerdì; pagina del compito in italiano, arabo e cinese.
4. **4TI (10-13)**: ramo `classe-4ti` dalla base; da decidere con il docente se la 4TI fa il giro delle PR o continua con le reti.
5. **La revisione di tutte le versioni** (una riga positiva e una negativa per versione) per l'analisi in classe, vista prima dal docente.

## 06 Domande aperte per il docente

1. La base resta neutra (niente facce e nomi di una classe) e ogni classe aggiunge i suoi?
2. La 4TI entra nel giro del treno o resta sulle reti?
3. I rami delle classi si creano tutti domani mattina o ognuno il giorno della sua lezione?

## 07 Registro delle versioni

1. **v1.0 (12/10/2026)**: prima versione, dopo la richiesta del docente di un ramo base del prof su Godot da cui partono tutte le classi.
