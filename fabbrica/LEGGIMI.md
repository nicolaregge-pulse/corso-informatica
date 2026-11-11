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
