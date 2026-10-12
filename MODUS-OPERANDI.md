# Modus operandi del corso

**Versione 1.3** — 12/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano. Area Docente.

Raccoglie in un solo posto il modo di lavorare deciso con il docente tra venerdì 09/10 e lunedì 12/10/2026. Le regole vengono dalle lezioni vere di quei giorni (1INF, 2INF, 3INF) e dagli errori segnati nel registro degli errori (dal #41 al #54). Quando c'è un dubbio, valgono questo documento e CLAUDE.md.

## 00 Le cinque regole che vengono prima di tutto

1. **Prima di proporre qualcosa ai ragazzi si chiede: «Pubblico o vuoi vederlo prima?».** Si pubblica solo dopo la parola «pubblica» o un sì esplicito. Un orario detto prima non vale come via (#41).
2. **Ordine fisso di ogni lezione:** prima si guarda insieme la teoria, poi il compito, poi si pubblica.
3. **Decide il docente.** Se il docente ragiona ad alta voce o scrive considerazioni, Claude non decide al suo posto: se non è chiaro, fa una domanda sola (#54). Se il docente dice «fai tu», Claude decide con le regole di questo documento e avvisa di ogni cosa fatta.
4. **Prima i fatti, poi le parole:** si dice «fatto» solo dopo un controllo vero (pagina provata nel browser, controllo automatico passato, file pubblicato).
5. **Tutto versionato:** ogni file va nel repository, con commit e push; i dati con i nomi dei ragazzi solo nel repository riservato.

## 01 Il compito della lezione

1. **Un solo compito su Classroom**, con un link fisso a una pagina che si aggiorna da sola.
2. La pagina si costruisce come dice `REGOLE-COSTRUZIONE-TEORIA.md`: titolo, il percorso di oggi in alto, FASE 1 la teoria (solo da leggere), FASE 2 i bottoni verdi del lavoro. I link si aprono in una scheda nuova.
3. **Il compito lo devono poter iniziare tutti:** frasi da quinta elementare, una per riga; il primo passo è una risposta che tutti sanno dare (#43).
4. **Tutto al computer:** niente foto, niente telefono, niente carta e penna, se il docente non lo chiede (#44, #45).
5. **Ogni attività si controlla dalla pagina del prof**, senza passare banco per banco.

## 02 Le lingue di ogni classe

| Classe | Lingue delle pagine per i ragazzi |
|---|---|
| 1INF | italiano, arabo, cinese |
| 2INF | solo italiano |
| 3INF | italiano e bengalese |

1. Per una classe solo italiano ogni pagina passa da `strumenti/solo_italiano.py`: toglie le altre lingue e, se ne resta anche un carattere, blocca la pubblicazione (#49).
2. Una pagina non si copia da un'altra classe senza rifare il controllo delle lingue.

## 03 Le consegne

1. **Modulo «Consegna» generico**, lo stesso per tutte le classi: si può inviare tutte le volte che si vuole, senza ritirare niente su Classroom (#42).
   1. «Cosa consegni?»: testo, file, commento, PR1, PR2…
   2. «Il tuo testo, commento o proposta di modifica»: casella grande (paragrafo); per una PR: Titolo · Cosa cambia · Dove · Perché.
   3. «Carica i tuoi file»: facoltativo.
2. **Modulo Feedback sulla teoria**, uno per classe e per lezione.
3. **Lo script «Consegne Classroom → Git»** gira ogni minuto; i Moduli collegati arrivano su Git appena un ragazzo preme «Invia».

## 04 Il giro delle Pull Request

Il metodo completo sta in `GIRO-PULL-REQUEST.md`. In breve:

1. Ogni PR entra nel **backlog** con riepilogo, **peso** (Fibonacci: 1 testo o colore, 2 un numero, 3 un personaggio, 5 un ambiente o un oggetto, 8 una regola nuova, 13 una parte grande) e motivo.
2. **Ordine:** peso più basso prima; a parità di peso, chi è arrivato prima.
3. **Una PR = una versione nuova del gioco**, con changelog (chi l'ha chiesta, cosa cambia, peso, dove nel codice), versione ferma giocabile, grafo aggiornato.
4. **Stato nel backlog:** FATTO in verde con la versione; NO in rosso con il motivo (foto di una persona vera, diritti d'autore, non dice cosa e dove, doppione o copiata, c'è già).
5. Il **sì o no** su una PR lo dà il docente; con «fai tu» lo dà Claude con queste regole.
6. Nei giochi di scuola niente sangue: si propone un'alternativa.

## 05 La sezione dei bottoni nella pagina del compito

In alto nella pagina del compito, sotto «Il tuo percorso di oggi», c'è un riquadro con i bottoni. Il docente li ritrova sempre aprendo il lavoro della classe su Classroom.

| Bottone | Cosa mostra | Chi lo vede |
|---|---|---|
| I voti | voto, PR inviate, PR nel gioco, Feedback, perché | tutta la classe (nome e iniziale) |
| Il backlog | tutte le PR, con peso e stato | tutta la classe |
| Il monitor della lezione | i giri Veyon: cosa c'era su ogni schermo, fuori compito in rosso | tutta la classe (nome e iniziale) |
| Cosa è cambiato oggi nel gioco | il changelog del giorno, con il link per giocare ogni versione | tutta la classe |
| La classifica | prima le PR pubblicate nel gioco, a parità le PR inviate; sotto ogni nome tutte le sue PR | tutta la classe |
| Valutazione dei singoli (solo prof) | la valutazione per allievo, pagina cifrata: COGNOME Nome, in ordine alfabetico del cognome | solo il docente, con la password dell'area docente |

## 06 I voti

1. **Proposta calcolata, voto deciso dal docente.**
2. Regole del 12/10: nessuna PR 40; da 1 a 4 PR da 45 a 54; almeno 5 PR 60; oltre 70 serve almeno una PR messa nel gioco; contano anche le PR scritte bene e il Feedback; non contano doppioni, richieste vuote, foto di persone vere.
3. **Le decisioni del docente vincono sul calcolo.** Nella pagina pubblica il motivo è solo «decisione del prof»; il motivo vero resta nel riservato.
4. A fine lezione i voti si **congelano** all'ora detta dal docente e il docente riceve il **PDF della valutazione per allievo** (una pagina per ragazzo).
5. Gli assenti non hanno voto.

## 07 Il monitor (Veyon)

1. Il docente manda in chat la schermata di Veyon; Claude la trascrive subito nel monitor.
2. **Solo fatti:** cosa c'era sullo schermo, senza giudizi; fuori compito in rosso.
3. Nome e iniziale nella pagina pubblica; il collegamento computer → nome sta nelle impostazioni della lezione, nel riservato.

## 08 Come Claude dà le istruzioni al docente

1. Ogni passo dice prima **dove** e poi **cosa**: account (PERSONALE o PIAMARTA) → finestra → programma → zona della pagina → azione.
2. Ogni testo da scrivere è già nel messaggio, in un riquadro da copiare, **subito dopo** il passo che lo usa (#46).
3. **La memoria del copia e incolla si considera vuota:** prima si apre la pagina dove si incolla, poi si copia, poi si incolla (#50).
4. **Formato atomico:** più passi in un messaggio, ognuno completo; ogni gruppo di passi finisce con «Dopo devi vedere: …» (#47). Niente screenshot a ogni passo.
5. **Mappa vera dello schermo:** i campi si indicano per posizione; prima di guidare un programma mai visto, una schermata sola, salvata come mappa (#51).
6. **Niente parole in più:** se togliendo una parola il senso resta uguale, si toglie (#53).
7. **Solo il prossimo passo:** non si ripetono i passi già fatti.
8. **Un flusso unico, sempre da zero:** le istruzioni partono sempre dall'inizio e funzionano senza condizioni; niente «se», niente «salta», niente domande dentro i passi (#55).
9. **Durante le ore di lezione il docente viene interrotto di continuo dai ragazzi:** in quelle ore si mandano solo messaggi brevi, con una o due azioni al massimo, che si possono riprendere anche dopo un'interruzione. Tutto quello che ha molti passi (script, Moduli, impostazioni) si fa il lunedì e il mercoledì pomeriggio, quando il docente è a scuola senza classe (fino alle 17:30).

## 09 Lo script di Google

1. Il codice si copia **sempre** dal link pubblico, nella finestra PIAMARTA (il repository riservato lì dà 404, #48):

```
https://raw.githubusercontent.com/nicolaregge-pulse/corso-informatica/main/strumenti/automazione-corso.gs
```

2. Il progetto si apre da `script.google.com/home` → «Consegne Classroom → Git». Ha 5 file: il codice va in **automazione-corso.gs**, non in «Codice.gs» che si apre per primo (#51).
3. Dopo aver incollato: Ctrl+S, poi «Esegui» su `attivaAutomatico` e su `attivaInvioModuli`.

## 10 Il registro (DIDAweb)

1. Firma **subito in classe**, entro le 14:05, con il programma previsto; a fine giornata si sistemano gli argomenti.
2. Il bottone «FIRMA ✓» c'è anche sulle ore già firmate: da una schermata non si dice mai che un'ora non è firmata. Se il docente dice «firmate», è così (#52).
3. Testo del registro corto: una frase, al massimo circa 40 caratteri.

## 11 File, password e privacy

1. I file per il docente (PDF, immagini) si mandano **scaricabili in chat**, non come link da aprire.
2. **Le password non si scrivono mai in chat.** Il docente le trova nel repository riservato, dall'account PERSONALE.
3. Mai foto di persone vere nei giochi; nelle pagine pubbliche solo nome e iniziale; nomi completi, voti dettagliati, note e file dei ragazzi solo nel riservato.
4. Un fatto personale di un ragazzo (per esempio una chiamata dalla tutor) non va mai nelle pagine pubbliche.

## 12 L'automazione di Claude durante la lezione

1. **Un solo processo scrive su Git** (`generatori/lezione_pr.py <lezione> giro`): più processi insieme bloccano il repository.
2. Il giro automatico dura **oltre la fine della lezione**, non meno.
3. Ogni versione nuova del gioco passa dal controllo automatico; se fallisce, non si pubblica niente.
4. Le impostazioni di ogni lezione stanno in un file solo (`config/lezioni/<AAAAMMGG>_<CLASSE>.json`, nel riservato): per una lezione nuova si copia quello di una lezione vecchia.

## 13 Documenti collegati

| Documento | Cosa contiene |
|---|---|
| `CLAUDE.md` | le regole operative di Claude, lette per prime |
| `GIRO-PULL-REQUEST.md` | il giro delle PR in classe, passo per passo |
| `REGOLE-COSTRUZIONE-TEORIA.md` | come si costruisce la pagina della lezione |
| `METODOLOGIA-CORSO.md` | la metodologia del corso, da stampare |
| `REGISTRO-ERRORI-CLAUDE.md` | gli errori, con la regola nata da ognuno |
| `RIFERIMENTI-E-DECISIONI.md` | le decisioni, numerate |

## 14 Registro delle versioni

4. **v1.3 (12/10/2026)**: capitolo 08 punto 8, flusso unico sempre da zero, senza «se».
3. **v1.2 (12/10/2026)**: capitolo 08 punto 8, in classe solo messaggi brevi; i lavori lunghi il lunedì e il mercoledì pomeriggio.
2. **v1.1 (12/10/2026)**: valutazione dei singoli con COGNOME Nome, in ordine alfabetico.
1. **v1.0 (12/10/2026)**: prima versione, con le decisioni del 09/10 e del 12/10/2026.
