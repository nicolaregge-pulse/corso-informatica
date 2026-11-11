# fabbrica
Richieste per lo script Fabbrica del docente (testo codificato, nessun nome di allievo). Non modificare a mano.

## TIPOLOGIA LEZIONE (11/11/2026)
Le 4 TIPOLOGIE LEZIONE: Esercitazione Lazarus, Quiz su Moduli, Versioning su GitHub, Teoria a schede.
Nei lavori di `indice.json` il campo e `tipologia_lezione` (`quiz` o `teoria`); i nomi vecchi `tipologia` e `tipo` sono ancora accettati.
Se manca: un id che comincia per `scheda-` e teoria, tutto il resto e quiz. Un lavoro gia creato non si ricrea mai (conta solo l'id).
Il motore (v2.8) scrive la scheda `Tipologie lezione` (classi x TIPOLOGIA LEZIONE) nel foglio Fabbrica.

## Intestazioni dei quiz (motore v2.10, 11/11/2026)
Nelle schede `Situazione <CLASSE>` e `Sicurezza <CLASSE>` ogni colonna quiz ha l'intestazione in 3 righe: ora e argomento breve (per esempio `Sic. ora 5 · infortuni`), data, id del quiz. Ricavate dal titolo, mai troncate; se due coincidono si aggiunge l'id. Prova con finti servizi: `test_situazione_v2_10.js` nel riservato (report/2026-11-11).

## Situazione per classe (motore v2.9, 11/11/2026)
Il motore scrive nel foglio Fabbrica le schede `Situazione 1INF`, `Situazione 2INF`, `Situazione 3INF`, `Situazione 4TI` (solo docente, con COGNOME Nome, mai da pubblicare): una riga per allievo, una colonna per quiz di `indice.json` (tipologia quiz), cella = miglior % (punti/totale) o MANCA, colonne Fatti/totali, Media e NON HA FATTO. Elenco allievi dalle schede `Email <CLASSE>` o `Consegne <CLASSE>`.

## Indice, ordine e colori delle schede (motore v2.11, 11/11/2026)
Prima scheda `Indice`: una riga per scheda (nome con link al gid, tipo, classe, ultimo aggiornamento, visibile o nascosta). Ordine fisso a ogni giro: Indice, Situazione, Sicurezza, Esiti e Quiz, Tipologie lezione, Utenti/Consegne/Git/Email/Corsi, altre, poi le `Ris <id>`. Le `Ris <id>` il cui id non e piu nei `lavori` di `indice.json` sono NASCOSTE (mai cancellate; se l'id torna, si rimostrano). Colori: Ris per classe (1INF blu, 2INF verde, 3INF arancio, 4TI viola, orfane grigie), Situazione e Sicurezza colori propri. Se `indice.json` non si legge, non si nasconde nulla. Prova con finti servizi: `test_indice_v2_11.js` nel riservato (report/2026-11-11).

## Indice con colonne di testo e Pannello (motore v2.12, 11/11/2026)
La scheda `Indice` ha ora 9 colonne: Scheda, Tipo, Classe, Ultimo aggiornamento, Stato, **URL** (testo: `https://docs.google.com/spreadsheets/d/<id>/edit#gid=<gid>`), **Titolo**, **Link ragazzi** (solo il viewform pubblico dei Moduli, preso da Esiti colonna D; mai il link di modifica), **Tipologia lezione**. In fondo una riga `Quiz` per ogni lavoro di `indice.json` con link valido. Nessun cognome e nessuna email. Serve alla pagina pubblica `docs/pannello/` (https://nicolaregge-pulse.github.io/corso-informatica/pannello/), che legge il CSV pubblicato della scheda Indice: il link va in `docs/pannello/config.json` (campo `indice`, vuoto finche non e pubblicato; oppure `?config=1` per questo browser). Prova con finti servizi: `test_indice_v2_12.js` nel riservato (report/2026-11-11).

## Indice senza formule (motore v2.13, 11/11/2026)
Correzione: nelle schede `Indice` (colonna A) e `Quiz` (colonna G) il motore non scrive piu formule `=HYPERLINK(...)` (il foglio e in italiano e le rifiutava: `#ERROR!`). Scrive TESTO semplice e aggiunge il link cliccabile con RichTextValue (`setLinkUrl`); l'URL completo resta in colonna F. Le righe `Quiz` dell'Indice hanno Titolo e Link ragazzi (viewform, mai link di modifica) da Esiti colonna D. Provato solo con finti servizi (`test_indice_v2_13.js` nel riservato).

## Indice solo con i quiz attuali (motore v2.14, 11/11/2026)
Nella scheda `Indice` le righe `Quiz` sono solo quelle degli id correnti di `indice.json` (una riga per id, Stato `Attivo`). Gli id vecchi che restano in `Esiti` (Moduli creati e poi sostituiti) diventano righe `Quiz (vecchio)` con Stato `Nascosta` e senza Link ragazzi, cosi il Pannello non le mostra. Provato solo con finti servizi (`test_indice_v2_14.js` nel riservato).

## Situazione con elenco da Utenti e abbinamento email (motore v2.15, 11/11/2026)
Nella scheda `Situazione <CLASSE>` l'elenco allievi viene, in ordine, da `Email <CLASSE>`, da `Consegne <CLASSE>`, da `Utenti <CLASSE>` (colonna C Allievo, COGNOME Nome). Con `Utenti` chi non ha risposto a nessun quiz compare con MANCA su ogni quiz. Le email delle risposte si abbinano agli allievi per nome.cognome (cognome.nome, nome_cognome, cognomenome; un abbinamento ambiguo o con la sola iniziale non vale). La riga 4 dice quanti allievi sono abbinati, quanti no e quante risposte hanno email non abbinata, con il gesto da fare (account PIAMARTA, un passo: scheda `Email <CLASSE>`, A email, B allievo). Se manca tutto, la riga 4 dice quale scheda manca e il gesto. Provato solo con finti servizi (`test_situazione_v2_15.js`, `test_indice_v2_15.js` nel riservato).
