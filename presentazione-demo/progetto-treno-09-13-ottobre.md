# Il progetto del treno, da venerdì a oggi

**Versione 1.0** — 13/10/2026 — Prof. Nicola Regge, Laboratorio di Informatica, Piamarta Milano.

Che cosa hanno fatto la prima, la seconda e la terza (1INF, 2INF, 3INF) con il gioco «Il treno blindato», da venerdì 9 a martedì 13 ottobre 2026. In classe si lavora come in un'azienda di software: i ragazzi chiedono le modifiche, l'intelligenza artificiale (Claude) scrive il codice, il prof decide, Git tiene tutte le versioni.

## 00 In breve

| Giorno | Classi | Che cosa |
|---|---|---|
| Venerdì 09/10 | 1INF e 2INF | la storia del gioco letta nel grafo di Git: versioni, rami, copie, unioni |
| Lunedì 12/10 | 2INF e 3INF | l'azienda in classe: richieste di modifica, coda dei lavori, 20 versioni del gioco in tre ore |
| Martedì 13/10 | 2INF | si chiude l'argomento: ripasso, verifica, recupero e retrospettiva; il gioco passa su Godot |

## 01 Venerdì 09/10: la storia nel grafo

1. Il gioco ha una storia: ogni versione ha un numero (v1.0, v1.1, v2.0) e una riga che dice che cosa cambia.
2. I ragazzi leggono questa storia nel **grafo di Git**, con i pallini da cliccare: **versione**, **ramo** (una strada parallela di lavoro), **fork** (la copia di un'altra classe), **merge** (due rami che si uniscono), cambio piccolo (minor) e grande (major).
3. Il treno della 1INF passa su **Godot**, un motore di gioco vero: è una versione major, la v2.0.
4. Il compito è in tre lingue (italiano, arabo, cinese), una domanda alla volta.

## 02 Lunedì 12/10: l'azienda in classe

1. **Teoria breve:** come lavorano le aziende di software, il Manifesto Agile e le 10 regole del nostro treno.
2. **La richiesta di modifica (Pull Request):** ogni ragazzo scrive nel Modulo «Consegna» un'idea per il gioco, in quattro parti: Titolo, Cosa cambia, Dove, Perché.
3. **Il backlog (la coda dei lavori):** ogni richiesta ha un peso (1 un colore, 2 un numero, 3 un personaggio, 5 un ambiente, 8 una regola nuova); prima si fanno le più leggere.
4. **Claude scrive il codice**, lo prova e pubblica la versione nuova; il prof decide che cosa entra. Ogni versione dice chi l'ha chiesta.
5. **Il risultato in 2INF:** 17 ragazzi, 129 richieste, **20 versioni nuove del gioco in tre ore**, tutte giocabili.
6. **Tutto è pubblico e si aggiorna da solo:** coda dei lavori, voti, classifica, monitor della lezione, «cosa è cambiato oggi nel gioco».

## 03 Martedì 13/10: si chiude l'argomento

1. **Ripasso, verifica, recupero**, in un'unica pagina: prima una vittoria facile, poi le schede con le risposte corrette subito, poi la verifica che il prof apre quando più della metà ha finito il ripasso.
2. **Autoregolazione:** ogni ragazzo vede sempre il suo andamento, il monitor della lezione e i risultati, e si regola da solo.
3. **Recupero personale:** prima i propri errori spiegati, poi una verifica solo sui punti sbagliati.
4. **Retrospettiva Agile** alla fine della verifica: che cosa fare di più, di meno, che cosa cominciare e che cosa smettere. I ragazzi chiedono di imparare a scrivere il codice da soli e di fare anche hardware.
5. **Il gioco passa su Godot per tutte le classi:** una base comune del prof, da cui partirà un ramo per ogni classe.

## 04 E la 4INF

1. Lo stesso modo di lavorare vale per i progetti di stage: un deposito su GitHub per ogni progetto, le modifiche come Pull Request, la pagina della Pull Request come chat tra ragazzo, prof e Claude, un diario che cresce tappa dopo tappa.
2. Il primo progetto (un automa che legge la temperatura vera di Milano, la salva e la mostra in una pagina web) è partito il 13/10 e in un'ora ha fatto la sua prima lettura automatica.

## 05 Dove si vede

1. La demo, con la giornata vera della 2INF senza i nomi dei ragazzi (si entra con la propria email e un codice che arriva per posta, valido 24 ore):
```
https://script.google.com/macros/s/AKfycbyhkWr44IWarPFRvcyP0Ku1pI-XbFaeBVJA4I0iEITq_4U4XvD5rqiPci77-p2FLory/exec
```
2. Il gioco, versione base su Godot:
```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-prof/
```
3. Il grafo delle versioni:
```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/
```
