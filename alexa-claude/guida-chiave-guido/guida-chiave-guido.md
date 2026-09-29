# Chiave API Claude per la skill Alexa di Nicola

**Versione 1.0** (29/09/2026) · Guida per Guido · tempo richiesto: circa 5 minuti

## 01 Cosa serve e perché

Nicola ha una skill Alexa personale (progetto `alexa-claude`) che manda le
domande dette a voce a Claude e fa leggere la risposta all'Echo. Per parlare con
Claude un programma esterno usa l'API di Anthropic, che si paga a consumo e
richiede una chiave API. Nicola non ha credito sulla Console; la tua
organizzazione sì.

1. Consumo previsto: circa un centesimo di dollaro a domanda (stima; risposte
   brevi, modello `claude-opus-5-5` a sforzo basso). Cento domande al mese: circa
   un dollaro.
2. Uso: solo personale, un solo account Amazon, skill non pubblicata.

## 02 Passi sulla Console Anthropic

1. Apri console.anthropic.com ed entra nella tua organizzazione.
2. Consigliato: crea un workspace dedicato, così il consumo è separato da Pulse.
   1. Menu Settings, voce Workspaces, bottone "Create Workspace".
   2. Nome: `alexa-nicola`.
   3. Nelle impostazioni del workspace imposta un limite di spesa mensile basso
      (per esempio 5 dollari).
3. Crea la chiave.
   1. Menu Settings, voce API Keys, bottone "Create Key".
   2. Nome: `alexa-nicola`.
   3. Workspace: `alexa-nicola` (quello appena creato).
   4. Copia la chiave (inizia con `sk-ant-`): la Console la mostra una volta sola.

## 03 Come consegnarla a Nicola (importante)

1. La chiave **non va messa nel repository** su GitHub, né in chiaro in chat di
   gruppo: chi la vede può spendere il credito.
2. Mandala a Nicola **in privato**, preferibilmente con un link a scadenza
   (per esempio Bitwarden Send, che usate già) oppure in un messaggio diretto che
   poi cancellate.
3. Nicola la inserisce lui nel file `config.js`, che esiste
   **solo dentro la Alexa Developer Console** (codice ospitato da Amazon) ed è escluso da Git
   tramite `.gitignore`. Nel repository c'è solo `config.example.js`, senza chiavi.

## 04 Cosa succede dopo, lato Nicola

1. In `config.js` mette la chiave in `CLAUDE_API_KEY`.
2. Cambia `MODELLO: 'gemini'` in `MODELLO: 'claude'`.
3. Clicca Save e Deploy nella Alexa Developer Console.

## 05 Se vuoi controllare il codice

Il codice è nel repository `nicolaregge-pulse/corso-informatica`, ramo
`claude/alexa-claude`, cartella `alexa-claude/`. La chiamata all'API è in
`lambda/ia.js`: SDK ufficiale `@anthropic-ai/sdk`, `effort: low`, `max_tokens`
2000, timeout 7 secondi senza nuovi tentativi, `fallbacks: "default"` in caso di
rifiuto.

## 06 Per bloccare tutto in qualsiasi momento

Console, menu Settings, voce API Keys: disattiva o elimina la chiave
`alexa-nicola`. La skill smette subito di usare Claude, senza toccare nient'altro.

## CHANGELOG

1. v1.0: prima versione.
