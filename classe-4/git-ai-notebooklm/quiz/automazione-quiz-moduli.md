# Automazione dei quiz su Google Moduli

**Nota tecnica · Versione 1.0 · 29/09/2026**

*Come creiamo i quiz di verifica in modo automatico, senza costruirli a mano uno
per uno. Documento scritto da Claude, l'assistente IA del corso, per Massimo Fubini.*

---

## 1. Il problema
1. Un quiz di verifica su Google Moduli, fatto a mano, richiede tempo: creare ogni domanda, incollare le risposte, impostare quella giusta, assegnare i punti. Per 12 domande sono molti clic ripetitivi.
2. Ogni volta che cambia un argomento, bisognerebbe rifare tutto da capo.

## 2. La soluzione: un piccolo script
1. Google Moduli offre un linguaggio di automazione, **Apps Script** (basato su JavaScript). Con poche righe si puo dire al Modulo: "crea queste domande, con queste opzioni, con questa risposta giusta e questi punti".
2. Noi scriviamo il quiz **una volta sola** come lista di domande, poi lo script lo trasforma in un vero Modulo-quiz **in un clic**, con il punteggio automatico gia impostato.

## 3. Come funziona, in pratica
1. Si apre `script.google.com` e si crea un nuovo progetto.
2. Si incolla il nostro file di script (per esempio `crea-quiz-versioning.gs`).
3. Si preme "Esegui" e si autorizza con l'account della scuola.
4. Lo script crea il Modulo, imposta le domande a risposta multipla, segna la risposta corretta e i punti, e restituisce **due link**: uno per modificarlo e uno da dare agli allievi.
5. Il link si allega come **Compito su Classroom**. Il Modulo si **autocorregge** e assegna il voto da solo.

## 4. Perche e utile (didatticamente e non)
1. **Velocita**: da un elenco di domande a un quiz pronto in meno di un minuto.
2. **Zero errori di copia**: le risposte giuste sono definite una volta e non si sbagliano a impostarle a mano.
3. **Riuso**: cambiare argomento vuol dire cambiare solo la lista delle domande; la struttura resta.
4. **Correzione automatica**: il punteggio e immediato, il docente risparmia tempo e lo dedica agli allievi.
5. **Scalabilita**: lo stesso metodo vale per qualunque materia e per tutte le classi.

## 5. Il legame con l'IA
1. Le domande si possono **far generare a un'IA** (per esempio Gemini o NotebookLM sul documento della lezione) e poi rifinire a mano: l'IA propone, il docente controlla e decide.
2. Cosi si uniscono due automazioni: l'IA che **propone i contenuti** e lo script che **costruisce lo strumento**. Il docente resta al centro delle decisioni.

> In allegato trovi un esempio reale: lo script `crea-quiz-versioning.gs` che crea il quiz su Git e versioning presente in questo pacchetto.
