# alexa-claude

**Versione 0.1**

Skill Alexa personale: fai una domanda a voce all'Echo e risponde un'IA
(Gemini con chiave gratuita, oppure Claude con la chiave dell'organizzazione).
La skill resta in modalità "sviluppo": funziona solo sui dispositivi del tuo
account Amazon e non compare nello Store.

## 01 Come si usa (a voce)

1. "Alexa, apri mio assistente"
2. "Dimmi perché il cielo è blu" (oppure: spiegami..., chiedi..., voglio sapere...)
3. Alexa risponde e resta in ascolto: puoi fare un'altra domanda, e si ricorda
   le ultime sei domande della conversazione.
4. "Stop" per chiudere.

## 02 Cosa c'è nel progetto

1. `lambda/index.js`: riceve le richieste di Alexa e decide cosa rispondere.
2. `lambda/ia.js`: manda la domanda a Gemini o a Claude e ripulisce la risposta per la voce.
3. `lambda/config.example.js`: modello del file delle chiavi (le chiavi vere NON vanno su GitHub).
4. `lambda/package.json`: le librerie usate.
5. `skill-package/interactionModels/custom/it-IT.json`: il "modello vocale", cioè le frasi che Alexa riconosce.

## 03 Messa in funzione (riassunto; la guida clic per clic la fa Claude in chat)

1. Crea la chiave gratuita di Gemini su aistudio.google.com.
2. Su developer.amazon.com, nella Alexa Developer Console, crea una skill:
   1. lingua Italiano, modello "Custom", hosting "Alexa-hosted (Node.js)";
   2. nella scheda Build, nel JSON Editor, incolla `it-IT.json`, poi Save e Build;
   3. nella scheda Code incolla `index.js`, `ia.js`, `package.json`;
   4. sempre nella scheda Code crea `config.js` partendo da `config.example.js` e inserisci la chiave;
   5. Save e Deploy.
3. Nella scheda Test attiva "Development" e prova scrivendo o parlando.
4. Da quel momento funziona su tutti gli Echo del tuo account.

## 04 Passare da Gemini a Claude

Nel file `config.js` (solo nella console Alexa):

1. inserisci la chiave Claude in `CLAUDE_API_KEY`;
2. cambia `MODELLO: 'gemini'` in `MODELLO: 'claude'`;
3. Save e Deploy.

## 05 Limiti da sapere

1. Alexa aspetta circa 8 secondi: il codice si ferma a 7 e, se l'IA è lenta,
   Alexa lo dice ("ci sto mettendo troppo"). Per questo le risposte sono brevi.
2. Per iniziare una domanda serve una parola "d'aggancio" (dimmi, spiegami, chiedi...):
   è un limite di Alexa sulle frasi libere.
3. La memoria della conversazione dura solo finché la skill resta aperta.

## CHANGELOG

1. v0.1: prima versione. Domanda e risposta a voce, memoria breve di sessione,
   scelta Gemini/Claude da configurazione, gestione tempi di attesa e rifiuti.
