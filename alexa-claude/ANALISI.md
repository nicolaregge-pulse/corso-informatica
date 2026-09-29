# Analisi: parlare a voce con Claude (anche tramite Alexa)

**Versione 0.1** (29/09/2026). Da leggere con calma. In fondo c'è la lista
"cosa fare domattina".

## 01 Risposta breve

Ci sono tre strade. In ordine di semplicità:

1. **Strada A: app Claude sul telefono, modalità vocale.** Funziona **subito**,
   stasera. Usa il tuo abbonamento claude.ai. Non serve chiave API, non serve
   credito, non serve codice.
2. **Strada B: come la A, ma la voce esce dall'Echo.** Colleghi il telefono
   all'Echo via Bluetooth: tu parli al telefono, Claude risponde dall'altoparlante
   dell'Echo. Anche questa funziona subito, zero codice.
3. **Strada C: skill Alexa vera ("Alexa, apri mio assistente").** È il codice di
   questo progetto. Non serve il telefono. Richiede però una chiave API con credito
   (quella di Claude te la deve dare Guido), oppure la chiave gratuita di Gemini
   per iniziare.

Il consiglio è di usare **subito la A o la B** e costruire **con calma la C**.

## 02 Strada A: modalità vocale dell'app Claude

1. Apri l'app **Claude** sul telefono (è quella che già usi).
2. Nuova chat.
3. In basso, accanto al campo di scrittura, tocca l'icona della **voce** (onde
   sonore / cuffie; non il microfono della tastiera, che serve solo a dettare).
4. Parla normalmente: Claude risponde a voce e la conversazione continua da sola.

Vantaggi: è Claude "vero", con tutta la memoria delle chat, risposte lunghe
quanto vuoi, nessun costo in più. Limite: serve il telefono.

## 03 Strada B: telefono + altoparlante Echo

1. Di' all'Echo: "Alexa, associa Bluetooth".
2. Sul telefono: Impostazioni → Bluetooth → scegli il tuo Echo.
3. Apri l'app Claude in modalità vocale (strada A).
4. Parli verso il telefono (sul comodino), la risposta esce dall'Echo.
5. Per staccare: "Alexa, disconnetti Bluetooth".

## 04 Strada C: la skill Alexa (il codice)

### 04.1 Perché serve una chiave API

1. Alexa non può "entrare" nel tuo account claude.ai: l'abbonamento Pro/Max vale
   solo per le app di Anthropic.
2. Un programma esterno (la skill) parla con Claude solo tramite l'**API**, che si
   paga a consumo con una **chiave** creata su console.anthropic.com.
3. Tu non hai credito sulla Console; nel riepilogo della chat di Pulse risultano
   "chiavi" tra le cose in sospeso a carico di Guido. Quindi:
   1. o **Guido** crea una chiave dedicata nella sua organizzazione (consigliato:
      nome "alexa-nicola", con un limite di spesa basso);
   2. o apri una **tua** organizzazione sulla Console e carichi pochi euro.
4. Nel frattempo la skill funziona con **Gemini**, la cui chiave è gratuita
   (aistudio.google.com). Cambiare da Gemini a Claude è una riga di configurazione.

### 04.2 Quanto costa con Claude

Una domanda a voce con risposta breve costa indicativamente circa un centesimo
con il modello predefinito del codice (claude-opus-5-5: $4 per milione di token,
cioè pezzetti di parola, in ingresso e $20 in uscita). Cento domande al mese:
circa un euro. Con il limite di spesa impostato sulla Console
non ci sono sorprese.

### 04.3 Come funziona il codice

1. Tu parli: "Alexa, apri mio assistente", poi "dimmi ...".
2. Alexa trasforma la voce in testo e lo manda a `lambda/index.js`.
3. `index.js` passa la domanda (più le ultime domande della conversazione) a
   `lambda/ia.js`.
4. `ia.js` chiama Gemini o Claude, con istruzioni "rispondi breve, parlato, in
   italiano", e ripulisce la risposta da simboli che Alexa leggerebbe male.
5. Alexa legge la risposta e resta in ascolto per la domanda successiva.

### 04.4 Limiti di Alexa (non dipendono da noi)

1. **Circa 8 secondi** per rispondere: il codice si ferma a 7 e, se l'IA è lenta,
   Alexa dice "ci sto mettendo troppo". Per questo le risposte sono brevi e il
   modello è impostato su "sforzo basso" (più veloce).
2. **Parola d'aggancio obbligatoria**: la domanda deve iniziare con "dimmi",
   "spiegami", "chiedi", "voglio sapere", "perché", "come"... Alexa non accetta
   frasi totalmente libere.
3. **Memoria corta**: la skill ricorda solo la conversazione in corso (ultime sei
   domande); chiusa la skill, riparte da zero. La strada A invece ricorda tutto.
4. **Solo il tuo account**: la skill resta in "sviluppo", non va nello Store; è
   un vantaggio (privata, gratuita, nessuna approvazione di Amazon).

### 04.5 Stato del codice

1. Scritto e collaudato con una **simulazione** di Alexa: avvio, domanda,
   seconda domanda con memoria, stop, messaggio di attesa troppo lunga, sia con
   Gemini sia con Claude.
2. **Non ancora provato** su un Echo vero né con chiavi vere: è il collaudo di
   domattina.

## 05 Cosa fare domattina (in ordine)

1. Prova la **strada A** (2 minuti). Se ti basta, il problema è già risolto.
2. Se vuoi Alexa senza telefono, **strada C**:
   1. manda a Guido la richiesta della chiave (testo pronto in chat);
   2. crea intanto la chiave gratuita di Gemini su aistudio.google.com;
   3. scrivimi "avanti skill": ti guido clic per clic nella Alexa Developer
      Console (developer.amazon.com), dove si incollano i file di questo progetto.
3. Quando arriva la chiave di Guido: la metti in `config.js` e cambi
   `MODELLO: 'gemini'` in `MODELLO: 'claude'`.

## CHANGELOG

1. v0.1: prima stesura dell'analisi (tre strade, costi, limiti, piano per domattina).
