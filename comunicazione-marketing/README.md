# Comunicazione e marketing

**Versione 0.4** — 13/10/2026 — Il laboratorio di informatica secondo le idee di Nicola Regge. Area Docente.

La parte del corso che raccoglie i materiali per chi sta fuori dall'aula: possibili acquirenti e altre scuole, genitori, ragazzi, e chi non capisce niente di informatica. Nasce il 13/10/2026, dopo il racconto «Cinque giorni da azienda».

## 00 La pagina pubblica

1. Un solo indirizzo, da dare a chi serve. Non è collegato da nessun'altra pagina e i motori di ricerca non lo indicizzano (`noindex`).
```
https://nicolaregge-pulse.github.io/corso-informatica/cm-qma7yay4q5/
```
2. Limite da sapere: il repository del corso è pubblico. Chi lo sfoglia su GitHub vede anche questa cartella. Per un pubblico generico basta; per qualcosa di riservato si usa la demo con l'accesso via email.
3. Sorgente: `docs/cm-qma7yay4q5/` (pagina, racconto, PDF).

## 01 I due assi

1. **Per chi è:**
   1. chi vuole solo capire, anche senza saper usare un computer (la prova: la mamma del prof, 92 anni);
   2. genitori;
   3. scuole e aziende, cioè possibili acquirenti;
   4. ragazzi.
2. **In che forma:**
   1. PDF, da stampare o allegare;
   2. percorsi guidati da guardare, con la voce, che vanno avanti da soli;
   3. demo vere, da provare con le mani.

## 02 Che cosa c'è (inventario)

| N. | Contenuto | Per chi | Forma | Versione | Dove |
|---|---|---|---|---|---|
| 1 | Racconto «Cinque giorni da azienda» (9-13/10) | chi vuole capire, genitori, ragazzi | percorso guidato con voce | 1.0 | `docs/cm-qma7yay4q5/racconto/` |
| 2 | Brochure «La scuola come un'azienda di software» | scuole e aziende | PDF | 1.2 | `presentazione-demo/` |
| 3 | Presentazione della lezione del 12/10 (2INF) | scuole e aziende | PDF | 1.0 | `presentazione-demo/` |
| 4 | Demo con accesso via email: giornate del 12 e 13/10, «Prova come un allievo» | scuole e aziende | demo | 1.0 | `docs/demo/`, script `strumenti/demo-accesso.gs` |
| 5 | Il progetto del treno, 9-13/10 | genitori, ragazzi | PDF | 1.0 | `presentazione-demo/progetto-treno-09-13-ottobre.md` |
| 6 | Guida per docenti con alunni non italofoni (tolta dalla pagina pubblica: nomina molti prodotti di altre aziende; da riscrivere) | scuole | PDF | 0.1 | `guida-docenti-alunni-non-italofoni/` |
| 7 | Il parco del corso: mappa illustrata e cliccabile, senza le pagine del docente | scuole e aziende | HTML e PDF con link | 1.0 | `docs/cm-qma7yay4q5/parco/`, generatore `strumenti/gen_atlante.py` (l'Atlante completo resta interno) |

## 02b La mappa disegnata da Gemini

1. La mappa del parco è disegnata da Claude con forme semplici. Per un'illustrazione vera si può far disegnare a Gemini con questo testo, poi la si mette in cima all'Atlante:
```
Disegna la mappa illustrata di un parco divertimenti a tema informatica, vista dall'alto in stile cartoon colorato come le mappe illustrate dei grandi parchi divertimenti, formato orizzontale. Un trenino rosso gira tutto intorno al parco su un binario. Al centro un laghetto e una grande stazione ferroviaria rossa chiamata "Stazione del Treno blindato". Intorno, collegate da vialetti color sabbia e alberi: tre quartieri di casette colorate chiamati "Quartiere 1INF" (arancione), "Quartiere 2INF" (blu), "Quartiere 3INF" (verde); una torre viola "Torre del Grafo" con rami e pallini luminosi come un albero di versioni; una torre rosa "Torre delle Verifiche"; un'officina blu petrolio con ingranaggi "Laboratorio dello Stage"; una sala di controllo grigia con schermi "Sala di controllo"; una sala giochi viola con joystick "Sala giochi"; una biblioteca verde con un libro aperto "Biblioteca"; una cassaforte scura con un lucchetto dorato "Cassaforte". In basso al centro un grande arco d'ingresso arancione con la scritta "Il laboratorio raccontato". Ragazzi sorridenti di diverse origini camminano nei vialetti. Scritte in italiano grandi e leggibili, colori caldi, atmosfera allegra.
```

## 03 Regole

1. **Niente nomi dei ragazzi**, mai: nei testi, nelle schermate (si tagliano le righe con i nomi), nei PDF. Si controlla con l'elenco della classe prima di pubblicare.
2. **Parole semplici**: niente gergo; se serve una parola tecnica si dice prima in italiano («proposta di modifica», poi, se serve, «Pull Request»).
3. **Il test della mamma**: un contenuto per «chi vuole capire» deve funzionare con un solo bottone, scritte grandi, una voce che legge e il testo sotto.
4. **Ogni giornata importante produce il suo pezzo di comunicazione** (come il racconto del 13/10), e si aggiunge qui e nella pagina pubblica.
5. Ogni contenuto ha il suo numero di versione; quando cambia si sale di versione e si aggiorna l'inventario.
6. Prima di dare un contenuto nuovo a qualcuno: «Pubblico o vuoi vederlo prima?».
7. **Niente marchi di altri e niente cose non nostre:** nessun nome di scuola, prodotto o azienda nei testi (si dice «classe virtuale», «modulo online», «archivio delle versioni», «motore di videogiochi», «assistente di intelligenza artificiale»); nessuna immagine o personaggio che non abbiamo fatto noi (copertine, facce prese dal web). Gli indirizzi dei siti restano, perché servono a raggiungere le pagine.

## 04 Registro delle versioni

1. **v0.4 (13/10/2026):** niente marchi di altri e niente immagini non nostre: brochure v1.4, presentazione v1.2, progetto treno v1.2, racconto con un'immagine del gioco disegnato da noi, «Il parco del corso» al posto dell'Atlante completo, guida per i docenti tolta dalla pagina.
2. **v0.3 (13/10/2026):** tolto ogni riferimento alla scuola: i materiali portano il nome «Il laboratorio di informatica secondo le idee di Nicola Regge» (serve un'autorizzazione per usare il nome della scuola).
2. **v0.2 (13/10/2026):** aggiunti il parco del corso (mappa cliccabile + Atlante v1.0) nella pagina pubblica e il testo per far disegnare la mappa a Gemini.
2. **v0.1 (13/10/2026):** prima versione: impianto, pagina pubblica non collegata, inventario di sei contenuti, regole.
