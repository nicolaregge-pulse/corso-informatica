# Il Framework LAVAGNA: domande con disegni, controllo automatico e raccolta dei lavori

**Versione 1.0** — 12/11/2026 — Prof. Nicola Regge, Laboratorio di Informatica. Area Docente, documento interno (non per i ragazzi).

Una sola pagina, `docs/lavagna/index.html`, mostra un compito di disegno scritto in un file JSON (la «spec»). Il ragazzo disegna, la pagina controlla da sola quello che può controllare, il lavoro finisce in una cartella Drive e l'assistente lo raccoglie. Il prototipo (v0.1, biblioteca, 4 compiti «cerchia») è diventato il compito `biblioteca-1inf-ora6`.

> [GIALLO] **Stato (12/11/2026):** pagina, spec, controlli e raccolta sono provati in Chromium con una web app simulata. Il collegamento a Google (la web app Apps Script «Lavagna») è scritto e NON attivo: serve un gesto del docente (riservato, `report/2026-11-12/LAVAGNA-ATTIVAZIONE-v1.0.md`). Finché `docs/lavagna/config.json` ha il campo `invio` vuoto la pagina lavora in modalità PROVA.

## 01 A che cosa serve

1. Domande in cui il ragazzo risponde **disegnando o toccando** un'immagine: cerchiare una parte, toccarla, trascinare etichette, tracciare una freccia, disegnare a mano.
2. Il controllo automatico c'è per i tipi con un bersaglio; il disegno libero lo guarda l'assistente dopo la consegna (campo «da guardare»).
3. Ogni ragazzo vede da solo che cosa ha fatto e che cosa gli manca (R9): i segnalini in alto (verde fatto, rosso da rifare, blu da guardare) e un bottone per il passo dopo.
4. Il lavoro arriva all'assistente, che lo raccoglie per allievo e lo porta nel cruscotto (R8).
5. Indirizzi: elenco dei compiti `https://nicolaregge-pulse.github.io/corso-informatica/lavagna/`, un compito `…/lavagna/?id=<id della spec>`.

## 02 I tipi di domanda

| Tipo | Che cosa fa il ragazzo | Controllo automatico |
|---|---|---|
| `cerchia` | fa un cerchio con la penna | sì, vedi la regola qui sotto |
| `scegli` | tocca una zona tra più zone | sì: la zona toccata è quella giusta |
| `collega` | trascina le etichette sulle parti del disegno | sì: ogni etichetta sulla sua zona |
| `freccia` | traccia una freccia da una zona a un'altra (la punta si disegna da sola) | sì: parte dalla zona «da» e arriva nella zona «a» (margine 24 px) |
| `disegna` | disegna a mano libera | no: esito «da guardare», lo valuta l'assistente |

**Regola di giudizio del tipo `cerchia` (12/11/2026).** Per ogni zona dell'immagine (tutte, non solo il bersaglio) si calcola la copertura = area(rettangolo del disegno ∩ zona) / area(zona). Il passo è **giusto** se:

1. la zona del passo ha copertura almeno 0,6;
2. la sua copertura è la più alta di tutte, con margine di almeno 0,15 sulla seconda;
3. l'area del disegno non supera 6 volte quella della zona.

Messaggi: copertura sotto 0,3 «Il cerchio è lontano da…»; tra 0,3 e 0,6 «Quasi…»; un'altra zona coperta quasi quanto la giusta «Hai circondato anche X: prendi solo la parte giusta»; disegno troppo grande «Il cerchio è troppo grande». Un cerchio che sfora un po' è giusto: non lo si punisce.

Dopo 3 tentativi sbagliati compare «Vai avanti lo stesso» (il passo resta «da rifare»; il numero si cambia con `tentativi_max`).

I testi dell'interfaccia (bottoni, messaggi) in italiano stanno nella pagina; quelli in arabo, cinese e bangla stanno in `docs/lavagna/lingue/<lingua>.json` e si scaricano solo se la spec usa quella lingua: una pagina della 2INF non contiene né scarica nessun carattere arabo o cinese (R6). Il bangla (3INF, solo PC 14) si aggiunge con `&bn=1` all'indirizzo.

Colori: penna rossa, blu, nera e gomma. Esiti: verde (fatto), rosso (da rifare), blu (informazione).

## 03 Come si scrive una spec

File `docs/lavagna/spec/<id>.json`, con l'id uguale al nome del file (solo lettere minuscole, numeri e trattini).

| Campo | Significato |
|---|---|
| `id`, `versione`, `classe` | `1INF`, `2INF`, `3INF` o `4TI` |
| `lingue` | `["it","ar","zh"]` per la 1INF, `["it"]` per le altre (R6). Ogni testo della spec porta tutte le lingue della classe |
| `titolo` | testo per lingua |
| `sfondo`, `dimensioni` | immagine di partenza in `img/` (con `?v=N` in fondo) e misura (1200 x 700) |
| `penne`, `tentativi_max` | opzionali |
| `ordine` | `fisso` (default) oppure `casuale`: ogni ragazzo ha i passi in un ordine diverso, deciso da un seme legato al suo account (sempre lo stesso a ogni apertura) |
| `passi` | elenco dei passi |

Ogni passo ha `id`, `tipo`, `testo` (per lingua), `sfondo` (facoltativo: cambia immagine) e `penna`. In più:

1. **`zone`**: elenco di `{id, rett:[x0,y0,x1,y1], nome:{it,ar,zh}}` con **tutte** le parti dell'immagine (anche quelle che non sono il bersaglio). Le zone non devono stare una dentro l'altra: i particolari (la lampada, i libri) fanno parte della zona dell'oggetto.
2. `cerchia`: `bersaglio` = id della zona giusta; facoltativi `copertura_min` (0,6), `margine` (0,15), `dimensione_max` (6). Vecchia forma ancora valida: `bersaglio:{rett,nome}` senza `zone`.
3. `scegli`: `giusta` = id della zona giusta.
4. `collega`: `etichette:[{id, zona, testo}]`; le zone sono i posti.
5. `freccia`: `da` e `a` = `{rett, nome}`.
6. `disegna`: `criteri` (solo per l'assistente, non si mostra) con che cosa deve esserci nel disegno.

**Immagini.** Si disegnano con PIL (mai prese da internet), senza nomi di allievi. Le zone si **calcolano dallo script che disegna**, mai a mano. Nell'indirizzo c'è sempre `?v=N`: se si cambia un'immagine si aumenta N, così il browser non mostra la copia vecchia (la pagina aggiunge anche `?v=<versione della spec>` quando manca).

**Strumenti.**

1. `python3 strumenti/genera_lavagna_bibpc.py` — disegna le 8 immagini «biblioteca e PC» (`img/bibpc-01..08.png`), l'immagine `img/biblioteca.png`, scrive le spec `biblioteca-pc-1inf-ora6` e `biblioteca-1inf-ora6` e copia gli originali nel riservato. Controlla che le zone non si sovrappongano e che i tavoli stiano a 40 px o più dagli scaffali.
2. `python3 strumenti/genera_lavagna_prove.py` — immagini e spec di prova (`prova-scegli`, `prova-disegna`, `prova-collega-freccia`).
3. `python3 strumenti/controlla_lavagna_spec.py --indice` — controlla campi, immagini, rettangoli, zone, **lingue per classe (R6)** e **cognomi (R1)**, e riscrive `spec/indice.json` (l'elenco che la pagina mostra senza `?id=`). Va lanciato prima di ogni commit.

**Regole di disegno delle scene di biblioteca** (feedback del docente, 12/11/2026): il tavolo di lettura ha legno chiaro, 2-3 sedie, libri aperti e lampada; il banco prestiti è un bancone alto grigio-azzurro con pannello frontale, cartello, scanner e schermo, senza sedie. I due non devono mai sembrare uguali.

## 04 Come si consegna e come si raccoglie

1. **Consegna.** A fine compito il ragazzo preme Consegna. La pagina prepara:
   1. un **PNG** a «foglio» con tutti i passi (immagine, segni, intestazione con id ed esito);
   2. il **risultato** `{specId, versione, nonce, ora, durata, lingue, ordine, passi, esiti}`; ogni passo ha esito (`giusto`, `da_rifare`, `da_valutare`, `non_fatto`), tentativi, dati (rettangolo del disegno, coperture) e i tratti in vettori.
2. **Invio.** Con `invio` pieno in `docs/lavagna/config.json`, POST a una web app Apps Script (`fabbrica/lavagna-webapp.gs`, «esegui come me, accesso: chiunque nel dominio»), che legge l'email dalla sessione Google (mai dalla pagina), salva `Lavagna/<specId>/<email>_<data>.png` e `.json` su Drive e aggiunge una riga alla scheda «Lavagna» del foglio Fabbrica. Limiti: PNG 2,5 MB, risultato 400 KB, 30 invii per ragazzo e compito, lo stesso `nonce` non si salva due volte.
3. **Ricevuta.** La pagina scrive «Consegnato alle HH:MM» **solo** dopo aver letto dalla web app la ricevuta (R7); senza ricevuta scrive in rosso che non riesce a confermare e lascia il bottone Consegna attivo. La ricevuta non contiene l'email e vale solo per chi ha spedito.
4. **Ordine casuale.** Il seme lo dà la web app (hash di email, sale segreto e compito: non si risale all'email). Senza web app il seme è casuale e resta nel browser; il risultato dice da dove viene (`seme_origine`).
5. **Modalità PROVA.** Con `invio` vuoto non parte niente: banner «PROVA, non inviato», link per scaricare il PNG, risultato visibile.
6. **Raccolta (assistente).** Nel riservato `generatori/raccogli_lavagna.py` legge i file scaricati dalla cartella Drive (e, se c'è, la scheda «Lavagna» esportata in CSV) e scrive `LAVAGNA-<specId>-<data>.json` e `.md` con, per ogni allievo (COGNOME Nome, solo riservato), l'esito di ogni passo, i campi di valutazione dei disegni liberi e la riga «consegnati N su N presenti»; e un file `-pubblico.json` con solo «Nome I.» e i conteggi, per il cruscotto. Una valutazione già scritta si conserva se si rilancia.

## 05 Privacy

1. Nelle spec, nelle pagine e nelle immagini non c'è nessun nome di allievo (controllo automatico di `controlla_lavagna_spec.py`).
2. La pagina non chiede il nome e non manda email: chi è il ragazzo lo dice solo la sessione Google della web app.
3. I PNG e i risultati stanno nel Drive del docente (account PIAMARTA) e nel riservato. Nel pubblico passano solo «Nome I.» e i conteggi.
4. La web app non scrive nessuna email nelle sue risposte.

## 06 Limiti noti

1. Il collegamento a Google non è provato: la pagina e il codice della web app sono provati solo con servizi finti. Un browser che blocca i cookie di terze parti, o un ragazzo non entrato con l'account della scuola, fa arrivare il lavoro come «anonimo» (la pagina lo dice) o non lo fa arrivare (la pagina non scrive «consegnato»).
2. Il controllo del cerchio guarda **dove** sta il segno (il rettangolo che lo contiene), non se il cerchio è chiuso: un segno a zig-zag nella zona giusta passa. Per questo il PNG va comunque all'assistente.
3. Le traduzioni in arabo, cinese e bangla sono scritte dall'assistente e vanno fatte rivedere.
4. Il tipo `freccia` controlla l'inizio e la fine del tratto, non la forma.
5. Le zone sono rettangoli: gli oggetti molto obliqui hanno rettangoli un po' larghi.
6. Con le ricevute la pagina aspetta fino a circa 20 secondi prima di dire «non riesco a confermare».
