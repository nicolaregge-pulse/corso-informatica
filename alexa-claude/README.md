# alexa-claude — "Amichetto Claudio"

**Versione 0.2** (05/10/2026)

Skill Alexa personale: fai una domanda a voce all'Echo e risponde un'IA
(oggi Gemini con chiave gratuita; Claude appena arriva la chiave API).
La skill non è pubblicata nello Store: è in **Beta test** privato.

## 01 Stato attuale (funzionante)

1. Nome pubblico: **Amichetto Claudio**; nome di invocazione: `amichetto claudio`.
2. Provata con successo il 05/10/2026 dal simulatore della console e dall'app Alexa
   dell'account di famiglia (domanda e risposta corrette).
3. Modello in uso: Gemini `gemini-flash-lite-latest` (il modello "flash" normale
   superava gli 8 secondi di Alexa).
4. Account usati:
   1. Amazon Developer: account `libero.it` (proprietario della skill);
   2. Echo e app Alexa: account di famiglia, invitato come **beta tester**
      (accesso valido fino al **03/01/2027**, poi si rinnova dalla console).
5. Codice ospitato da Amazon (Alexa-hosted, Node.js 16, regione EU-Irlanda).

## 02 Come si usa (a voce)

1. "Alexa, apri amichetto claudio"
2. "Dimmi perché il cielo è blu" (oppure: spiegami..., chiedi..., voglio sapere...)
3. Alexa risponde e resta in ascolto: puoi fare un'altra domanda, e si ricorda
   le ultime sei domande della conversazione.
4. "Stop" per chiudere.

## 03 Cosa c'è nel progetto

1. `lambda/index.js`: riceve le richieste di Alexa e decide cosa rispondere.
2. `lambda/ia.js`: manda la domanda a Gemini o a Claude (modulo `https` di Node.js,
   senza librerie esterne, compatibile con Node.js 16) e ripulisce la risposta per la voce.
3. `lambda/config.example.js`: modello del file delle chiavi (le chiavi vere NON vanno su GitHub).
4. `lambda/package.json`: le librerie usate (solo l'SDK di Alexa).
5. `skill-package/interactionModels/custom/it-IT.json`: il "modello vocale", cioè le frasi che Alexa riconosce.
6. `icone/`: icone della skill (108 e 512 px) e la loro sorgente HTML.
7. `guida-chiave-guido/`: guida per Guido per creare la chiave API Claude.

## 04 Messa in funzione (come è stata fatta)

1. Chiave Gemini su aistudio.google.com (progetto importato, chiave gratuita).
2. Alexa Developer Console: skill "Custom", "Alexa-hosted (Node.js)", Italiano, EU (Ireland).
3. Build → JSON Editor: incollato `it-IT.json` → Save → Build skill.
4. Code: sostituito `index.js`, creati `ia.js` e `config.js` → Save → Deploy.
5. Distribution: descrizioni, frasi di esempio, categoria, icone, privacy.
6. Availability → Beta Test: aggiunta l'email dell'account di famiglia, accettato
   l'invito dall'app Alexa (con "Copy link" mandato via WhatsApp).

## 05 Passare da Gemini a Claude

Nel file `config.js` (solo nella console Alexa):

1. inserisci la chiave Claude in `CLAUDE_API_KEY`;
2. cambia `MODELLO: 'gemini'` in `MODELLO: 'claude'`;
3. Save e Deploy.

## 06 Da fare

1. Sostituire la chiave Gemini (quella attuale è comparsa in uno screenshot).
2. Ricevere da Guido la chiave Claude e passare a `MODELLO: 'claude'`.
3. Provare la skill a voce sull'Echo di casa.
4. Rinnovare il Beta test prima del 03/01/2027.

## 07 Limiti da sapere

1. Alexa aspetta circa 8 secondi: il codice si ferma a 7 e, se l'IA è lenta,
   Alexa lo dice ("ci sto mettendo troppo"). Per questo le risposte sono brevi.
2. Per iniziare una domanda serve una parola "d'aggancio" (dimmi, spiegami, chiedi...):
   è un limite di Alexa sulle frasi libere.
3. La memoria della conversazione dura solo finché la skill resta aperta.
4. Il nome di invocazione deve avere almeno 2 parole e non somigliare ai comandi
   di Alexa ("mio assistente" non veniva riconosciuto).

## CHANGELOG

1. v0.2: skill funzionante. Nome "Amichetto Claudio"; chiamate HTTP native per
   Node.js 16; modello Gemini flash-lite; icone; Beta test sull'account di famiglia.
2. v0.1: prima versione. Domanda e risposta a voce, memoria breve di sessione,
   scelta Gemini/Claude da configurazione, gestione tempi di attesa e rifiuti.
