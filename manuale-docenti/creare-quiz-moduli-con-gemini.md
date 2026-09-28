# Creare quiz autocorreggenti su Google Moduli con l'aiuto di Gemini

**Guida per il docente** — Anno formativo 2026/27

*Come farsi generare da **Gemini** uno "script" (Apps Script) che crea in un clic un
**quiz su Google Moduli** già impostato con le risposte giuste e il **punteggio
automatico**. Non serve saper programmare: si incolla un prompt, si copia il codice
che Gemini restituisce, lo si esegue una volta e il quiz è pronto da allegare su
Classroom.*

---

## 1. A cosa serve

1. Crei un **quiz autocorreggente** (Google Moduli assegna il voto da solo).
2. Non lo costruisci a mano domanda per domanda: lo genera un piccolo **script**.
3. Lo script te lo scrive **Gemini**, se gli dai le istruzioni giuste (sono qui sotto).

## 2. Cosa ti serve

1. Il tuo **account Google della scuola** (per creare il Modulo).
2. Un **browser** (niente da installare).
3. **Gemini** (gemini.google.com) per generare il codice.
4. **script.google.com** (Apps Script) per eseguire il codice: è gratis e già incluso
   nell'account Google.

## 3. Il prompt da dare a Gemini (copia-incolla)

Apri **gemini.google.com**, incolla il testo qui sotto e **personalizza** le tre righe
tra parentesi quadre (argomento, numero di domande, lingua). Poi invia.

```
Sei un esperto di Google Apps Script. Scrivimi UNO script completo per Google Moduli
che crei un QUIZ autocorreggente. Requisiti OBBLIGATORI, rispettali tutti:

1. Una sola funzione chiamata creaQuiz().
2. Usa FormApp.create(...) con .setIsQuiz(true).
3. Come PRIMA domanda aggiungi un campo di testo "Nome e Cognome" OBBLIGATORIO
   (addTextItem().setTitle('Nome e Cognome').setRequired(true)).
4. Attiva la raccolta dell'email: form.setCollectEmail(true).
5. Tutte le domande devono essere a SCELTA MULTIPLA (addMultipleChoiceItem), con
   UNA sola risposta giusta, usando item.createChoice(testo, true/false).
6. Ogni domanda vale 5 punti: item.setPoints(5).setRequired(true).
7. Alla fine stampa i due link con Logger.log: form.getEditUrl() (per il docente)
   e form.getPublishedUrl() (per gli allievi).
8. NIENTE domande aperte (Moduli non le corregge da solo).
9. Rispondimi SOLO con il codice, in un unico blocco, senza spiegazioni.

Argomento del quiz: [SCRIVI QUI L'ARGOMENTO, es. "I tipi di file: estensioni,
testo/binario, formati, compressione, percorso"].
Numero di domande: [SCRIVI QUI, es. 20].
Lingua delle domande: [SCRIVI QUI, es. "italiano"].
Inventa tu domande e risposte corrette, corrette e adatte a studenti di istituto
professionale (semplici e chiare).
```

> Variante: se hai GIA' le domande e le risposte, invece dell'ultima frase scrivi
> "Usa queste domande e segna la risposta giusta:" e incolla il tuo elenco.

## 4. Come eseguire il codice che Gemini ti ha dato

1. Copia **tutto** il codice che Gemini ha scritto (il blocco).
2. Vai su **script.google.com** e clicca **"Nuovo progetto"**.
3. **Cancella** il codice di esempio e **incolla** quello di Gemini.
4. In alto, nel menu delle funzioni, scegli **creaQuiz** e premi **"Esegui"**.
5. La prima volta chiede l'**autorizzazione**: accetta con l'**account scuola**.
6. In basso, nel pannello **"Esecuzioni"** (o "Log"), compaiono **due link**.

## 5. I due link (attenzione a non confonderli)

1. Link che finisce con **/edit** → è **tuo**: apre il Modulo per **controllare e
   modificare** le domande.
2. Link che finisce con **/viewform** → è quello **per gli allievi**: è il quiz da
   **allegare come Compito su Google Classroom**.

## 6. Consigli e trappole da evitare

1. **Auto-correzione = solo scelta multipla** (o caselle). Le domande aperte Moduli
   NON le corregge da solo: se ti servono, mettine poche e le correggi a mano.
2. **Controlla sempre** il Modulo generato prima di darlo: apri il link /edit e
   verifica che le risposte segnate come giuste siano davvero giuste.
3. Usa **l'account scuola** in Gemini, in Apps Script e in Classroom: devono essere
   lo stesso.
4. Se Gemini aggiunge spiegazioni o testo fuori dal codice, **cancellale**: incolla
   in Apps Script **solo** la parte di codice (da `function creaQuiz()` in giù).
5. Se al primo tentativo dà errore, rimanda a Gemini il **messaggio d'errore**
   scrivendo "Ho ricevuto questo errore, correggi il codice:" e incolla l'errore.
6. **Nome e Cognome obbligatorio**: è già nel prompt, così sai sempre chi ha risposto.

## 7. Esempio pratico (già provato)

Con l'argomento "I tipi di file", 20 domande, italiano, lo script genera un quiz da
**100 punti** (20 × 5) con Nome e Cognome obbligatorio, pronto da allegare su
Classroom. È esattamente il metodo usato per il quiz della Classe 2.
