# Versioning e Agile

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 12/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 12/10/2026, 3 ore, Laboratorio.
2. **Argomenti:** Il Documento come ramo dell'albero delle versioni; come si chiede una modifica (Pull Request PR1, PR2…); Manifesto Agile e 10 regole; backlog Agile.

### La teoria e l'esercitazione

Testo per la tua AI: chiedile di spiegarti ogni parola nella tua lingua.

#### 01 I link della lezione

1. Il grafo delle versioni (clicca i pallini)

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/grafo/
```

2. Tutte le versioni del vostro treno, giocabili

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-blindato/versioni/
```

3. Il changelog del treno (la lista dei cambiamenti)

```
https://github.com/nicolaregge-pulse/corso-informatica/blob/main/docs/giochi/treno-blindato/CHANGELOG.md
```

4. La storia dei commit del ramo treno-2inf

```
https://github.com/nicolaregge-pulse/corso-informatica/commits/treno-2inf
```

5. Il grafo vero di Git su GitHub (Network)

```
https://github.com/nicolaregge-pulse/corso-informatica/network
```

6. Il fork della 3INF: il loro treno

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf/
```

7. La versione 2.0 su Godot

```
https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-godot/
```

#### 02 Le 10 parole, con il nostro gioco

1. **Versione.** Una «fotografia» del progetto in un momento preciso, con un numero. Il vostro treno è passato da v0.0 (prima idea, finestrino laterale) a v0.11 (i punteggi si salvano sempre): 12 versioni in un giorno.

   1.2 Prova: Apri «Tutte le versioni» e gioca la v0.0 e la v0.11: cosa è cambiato?
2. **Git e GitHub.** Git è il programma che ricorda TUTTA la storia del progetto: chi ha cambiato cosa, quando e perché. GitHub è il sito dove il progetto (il repository) sta online. Il nostro repository si chiama corso-informatica.

   2.2 Prova: Apri «La storia dei commit»: ogni riga è un salvataggio.
3. **Commit.** Un salvataggio nella storia di Git, con un messaggio che spiega il cambiamento. Esempio vero di ieri: 7724900 «Treno blindato v0.11: i punteggi si salvano sempre». Il numero strano (7724900) è il codice del commit.

   3.2 Prova: Trova nella storia il commit della v0.5 (la Pull Request #104).
4. **Branch (ramo).** Una linea di lavoro separata. Si apre un ramo per provare una cosa nuova senza rompere il gioco che funziona. Il vostro gioco sta nel ramo treno-2inf; il prof ha provato le «immagini della classe» su un ramo a parte.

   4.2 Prova: Nel grafo: quante linee (rami) vedi?
5. **Fork (copia).** La copia di un progetto intero che cresce per conto suo. Ieri la 3INF ha fatto il fork del vostro treno alla v0.11 e lo ha portato alla v1.4 (montagna, Black Panter, Nash…); anche la 1INF.

   5.2 Prova: Nel grafo: da quale vostra versione parte la linea verde della 3INF?
6. **Push.** Mandare i propri commit dal PC al repository online (GitHub). Ieri, dopo ogni versione, il prof ha fatto il push: per questo il gioco sul sito cambiava da solo.

   6.2 Prova: Perché il gioco sul telefono cambiava senza scaricare niente?
7. **Pull.** Il contrario del push: prendere da GitHub l'ultima versione e portarla sul proprio PC. La v0.11 del treno «chiede sempre alla rete la versione nuova»: è un pull automatico.

   7.2 Prova: Quando fai un pull, cosa ricevi?
8. **Pull Request (proposta di modifica).** «Ho fatto una modifica: la vuoi nel progetto?». Qualcuno la controlla e, se va bene, fa il MERGE (la unisce). Ieri le vostre richieste su Classroom erano Pull Request: la #104 della squadra MOTORE FISICA è diventata la v0.5.

   8.2 Prova: Chi decide se una Pull Request entra nel gioco?
9. **Changelog (registro dei cambiamenti).** La lista, versione per versione, di cosa è cambiato e perché. Il treno ha il suo CHANGELOG.md: chi gioca sa cosa c'è di nuovo, chi programma sa dove cercare un errore.

   9.2 Prova: Apri il changelog: qual è la novità della v0.7?
10. **Numeri delle versioni (major.minor).** v0.x = prove; 1.0 = prima versione stabile (il fork della 3INF parte da 1.0); 1.1, 1.2 = piccole aggiunte (minor); 2.0 = cambio grosso (major): il gioco rifatto con Godot è la v2.0.

   10.2 Prova: Perché la versione Godot non si chiama v1.5?

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
