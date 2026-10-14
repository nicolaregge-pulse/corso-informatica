# Il framework della lezione: tutto quello che deve esserci SEMPRE

**Versione 1.0** — 14/10/2026

Prof. Nicola Regge, Laboratorio di Informatica. Area Docente, documento interno (non per i ragazzi).

Lo scheletro fisso di ogni lezione, per tutte le classi, da spuntare insieme (docente e Claude). Raccoglie in un solo posto le regole di `CLAUDE.md` (regole operative 6-12, AUTOREGOLAZIONE, motore «Vinci subito · Fallo tuo · Mostralo», lingue), di `MODUS-OPERANDI.md`, `REGOLE-COSTRUZIONE-TEORIA.md`, `VERIFICA-COME-SI-FA.md`, `GIRO-PULL-REQUEST.md` e degli errori del 13 e 14/10/2026 (registro degli errori, dal #60 al #79). I numeri tra parentesi, per esempio (#78), rimandano al registro degli errori.

> [GIALLO] **Nota:** il motore resta sempre lo stesso. Vinci subito (il primo passo non si può sbagliare), Fallo tuo (ognuno sceglie qualcosa di suo), Mostralo (ogni pezzo si gioca e si fa vedere). La leva è l'autoregolazione: gli strumenti per regolarsi stanno sempre nelle mani dei ragazzi.

## 01 Prima della lezione (il giorno prima o la mattina presto)

1. **Pagine standard del giorno, per ogni classe in orario.** I sei bottoni passano al lavoro di oggi: I voti, Il backlog, Il monitor della lezione, Le versioni del gioco (Cosa è cambiato oggi), La classifica, La situazione della classe (#71, #77).
2. **Pagine del docente del giorno:** il pannello del prof (`docs/<classe>-prof/`) e il cruscotto cifrato, con la password dell'area docente.
3. **Casella «Chiedi aiuto all'assistente del Prof Regge»** in ogni pagina per i ragazzi, nelle lingue della classe, con un solo bottone «Manda» (mai «Scrivi a Claude»).
4. **Le pagine di ieri** restano in un file «di ieri», raggiungibile con un link; non si mescolano con quelle di oggi (#71).
5. **Strumenti veri controllati prima di disegnare il percorso:** postazioni (niente webcam), permessi degli account dei ragazzi, servizi già attivi (applicazione web dello script, Modulo «Consegna»). Se una cosa non è sicura, la strada principale è quella che funziona già (#72).
6. **Lezione provata come un ragazzo, clic per clic, sul sito vero:** indirizzo del sito, file compressi, ricarica senza memoria (Ctrl+F5), telefono; gioco con le versioni giuste, verifica e recupero con `strumenti/prova_verifica.js` fino a «Tutto a posto» (#70, #78).
7. **Audit di tutte le pagine, anche quelle del docente, bottone per bottone:** ogni bottone si apre e mostra dati di oggi. Un bottone che oggi non può funzionare non si mostra (#75, #77).
8. **Nessuna pagina per i ragazzi è pubblica prima della parola «pubblica».** Claude dà il link dell'anteprima e chiede «Pubblico o vuoi vederlo prima?». Un orario detto prima non vale come via (#41). Ordine fisso: prima la teoria, poi il compito, poi si pubblica.
9. **Un link si dà solo dopo che il sito è pubblicato:** dopo il push si lancia lo script di attesa e il link va al docente solo dopo «PUBBLICATO». Una pagina per i ragazzi si pubblica almeno 3 minuti prima di dare il link a voce (#78, #79).

```
bash strumenti/aspetta_pubblicazione.sh
```

> [BLU] **Da confermare:** la casella «Chiedi aiuto» funziona solo con l'applicazione web dello script attiva (i 13 passi una tantum di `VERIFICA-COME-SI-FA.md`, capitolo 06). Finché non è attiva, la casella non si mette: una casella fragile fa più danno che niente (§2.53).

## 02 La pagina della lezione

1. **Un solo percorso, dall'alto in basso, con un solo link fisso** per lezione (`docs/compito/<classe>-<data>-<argomento>/`). Niente menu, niente schede, niente «scegli tu».
2. **Le cose nuove si aggiungono IN FONDO,** come passo successivo, mai in cima (#78).
3. **Ogni passo apre una finestra nuova e il ragazzo torna alla pagina:** vicino al bottone c'è scritto «si apre in una finestra nuova, poi torna qui».
4. **Il passo da fare ha il bordo blu; il passo fatto diventa verde con «✓ Fatto» e il suo bottone si spegne.**
5. **Una azione per passo,** frasi da bambino di 10 anni, una per riga. Se serve una spiegazione lunga si cambia il procedimento, non si allunga la spiegazione (#62).
6. **I sei bottoni** stanno nella pagina (riquadro «Come sta andando la classe»), con il proprio andamento: personaggi nel gioco, richieste mandate, voto della lezione (#60).
7. **Nelle pagine pubbliche solo «Nome I.»,** anche per i maggiorenni; nei giochi pubblici mai foto di persone vere (#69).

I passi fissi, in quest'ordine (modelli: `docs/compito/3inf-20261014-merge/` e `docs/compito/1inf-talpa-percorso/`):

| Passo | Che cosa | A che cosa serve |
|---|---|---|
| 1 | Il tuo nome: scrivi nome e cognome e premi OK | la prima vittoria, impossibile da sbagliare |
| 2 | La teoria: frasi corte, disegni, parole nuove; alla fine «Ho letto» | capire, solo da leggere |
| 3 | «Spiegalo in 30 secondi»: 4 frasi da dire al compagno e 4 domande rapide corrette subito | la prova del nove: saperlo spiegare (#76) |
| 4 | L'attività: giocare, trovare, scegliere qualcosa di proprio | Fallo tuo, Mostralo |
| 5 | La consegna: una sola strada, letta da Claude in tempo reale | niente lavoro perso (#68) |
| 6 | Ripasso, poi Verifica (la apre il prof) | fissare e misurare |
| 7 | La tua valutazione e il recupero | sapere dove si è e cosa fare dopo |

Le lingue di ogni classe:

| Classe | Lingue delle pagine per i ragazzi |
|---|---|
| 1INF | italiano, arabo (a destra, font Amiri), cinese (WenQuanYi Zen Hei) |
| 2INF | solo italiano, controllato con `strumenti/solo_italiano.py` |
| 3INF | italiano, con una riga di aiuto in bengalese sotto ogni frase |
| 4TI | italiano |

> [BLU] **Da confermare:** per la 2INF la richiesta di questo documento indicava italiano e cinese (decisione §2.49 dell'08/10), ma la decisione più recente (12/10, `MODUS-OPERANDI.md` capitolo 02 ed errore #49) dice «solo italiano». Qui vale la più recente finché il docente non decide.

## 03 Durante la lezione

1. **In classe non si cambia il giro:** si correggono solo errori. Ogni idea nuova va nell'elenco dei lavori aperti per la lezione dopo (#78).
2. **Ogni schermata di Veyon va subito nel monitor pubblico e nel cruscotto,** senza aspettare la domanda del docente: solo fatti, fuori compito in rosso, chi gioca da più giri (#60, #73).
3. **Le note del docente** (dal Modulo «Note del prof» o scritte in chat) entrano nel monitor come fatti, senza giudizi. Per ciò che sa solo il docente si usa la strada più corta per lui: scriverlo in chat (#74).
4. **Firma del registro in aula, entro le 14:05,** con il programma previsto. Il titolo è una voce dell'Allegato A di quella classe e della materia di quell'ora, al massimo circa 40 caratteri, uno per ora, ognuno nel suo riquadro da copiare. Da una schermata non si dice mai che un'ora non è firmata (#52).
5. **La situazione in un posto solo:** il sesto bottone «La situazione della classe» e il cruscotto dicono chi è sul compito, chi gioca, chi è fuori compito, richieste mandate e in attesa, voti, cosa fa adesso ciascuno.
6. **Al docente, in classe, solo messaggi brevi:** una o due azioni, ogni testo da scrivere già pronto in un riquadro da copiare, subito dopo il passo che lo usa. I lavori lunghi il lunedì e il mercoledì pomeriggio.
7. **La verifica si apre** quando più della metà ha finito il ripasso e la classe comincia a parlare, dopo che il docente scrive «attiva».

## 04 Valutazione

1. **Voto proposto da regole chiare e pubbliche,** scritte nella pagina «I voti» (per le PR: nessuna 40, da 1 a 4 da 45 a 54, almeno 5 60, oltre 70 serve una PR entrata nel gioco). Gli assenti non hanno voto.
2. **Ripasso, poi verifica, poi recupero** con il motore unico `docs/verifica/`: ripasso con allenamento corretto subito; verifica con consegna con un clic; recupero personale con la teoria mirata sui propri errori, poi la riverifica.
3. **Rapporto personale di fine lezione per ogni ragazzo:** PR mandate ed entrate nel gioco, comprensione («Spiegalo in 30 secondi» e verifica), che cosa dice il monitor, voto proposto, che cosa fare dopo. Il PDF arriva al docente, una pagina per ragazzo.
4. **Il voto lo decide il docente.** La decisione del docente vince sul calcolo; nella pagina pubblica il motivo è solo «decisione del prof», il motivo vero resta nel riservato.
5. **Prima di pubblicare i voti** si chiede «Pubblico i voti o vuoi vederli prima?».

## 05 Dopo la lezione

1. **Argomenti svolti:** si chiedono al docente e si scrivono in `ARGOMENTI-SVOLTI-2026-27.md`, senza nomi; si corregge il titolo del registro se serve.
2. **Libro di testo:** la lezione diventa un documento MD e PDF versionato e si aggiunge al libro della classe (versione nuova e voce nel changelog).
3. **Registro degli errori:** ogni correzione del docente diventa una voce del registro con la sua regola, e la regola entra nei documenti del metodo.
4. **Retrospettiva a fine argomento:** revisione e retrospettiva fra docente e Claude (`AGILE-CERIMONIE.md`), riassunto senza nomi in `RETROSPETTIVE.md`; la giornata entra nella demo, senza nomi.
5. **Archivio:** comandi eseguiti e compiti chiusi vanno in `archivio/`; le pagine di oggi diventano le pagine «di ieri».

## 06 Che cosa NON si fa

1. Cambiare il giro durante la lezione (#78).
2. Aggiungere un passo in cima al percorso (#78).
3. Mettere un bottone che porta a una pagina vuota o «in attesa» (#77).
4. Dare un link prima di «PUBBLICATO» (#79).
5. Usare un menu a tendina per abbinare i nomi al posto del nome scritto dal docente in chat (#74).
6. Chiedere al docente di scrivere a mano un testo: ogni testo va già pronto in un riquadro da copiare.
7. Dare due strade per consegnare (#68), o una consegna fatta di cinque passi (#62).
8. Dire «fatto» o «tutto a posto» senza la prova: pagina aperta dal sito vero, controllo passato (#63, #75).

## 07 Spunta prima di entrare in classe

| N. | Cosa | Chi | Fatto |
|---|---|---|---|
| 1 | Sei bottoni con i dati di oggi, pagine di ieri nel file «di ieri» | Claude | [ ] |
| 2 | Pannello e cruscotto del prof del giorno, provati come li usa il docente | Claude | [ ] |
| 3 | Casella «Chiedi aiuto all'assistente del Prof Regge» (se l'applicazione web è attiva) | Claude | [ ] |
| 4 | Percorso unico: nome, teoria, Spiegalo in 30 secondi, attività, consegna, ripasso, verifica, valutazione | Claude | [ ] |
| 5 | Lingue giuste per la classe, solo «Nome I.», niente foto di persone vere | Claude | [ ] |
| 6 | Lezione provata come un ragazzo sul sito vero, anche sul telefono e dopo Ctrl+F5 | Claude | [ ] |
| 7 | Verifica e recupero provati fino a «Tutto a posto» | Claude | [ ] |
| 8 | Consegna provata: arriva entro un minuto | Claude | [ ] |
| 9 | Teoria e compito visti dal docente; detto «pubblica» | Docente | [ ] |
| 10 | Link dato solo dopo «PUBBLICATO» | Claude | [ ] |
| 11 | Testi del registro pronti (voce dell'Allegato A, circa 40 caratteri) e firma entro le 14:05 | Docente | [ ] |

## 08 Registro delle versioni

1. **v1.0 (14/10/2026):** prima versione, dopo le lezioni del 13 e del 14/10/2026 (errori dal #60 al #79).
