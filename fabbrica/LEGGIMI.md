# fabbrica
Richieste per lo script Fabbrica del docente (testo codificato, nessun nome di allievo). Non modificare a mano.

## TIPOLOGIA LEZIONE (11/11/2026)
Le 4 TIPOLOGIE LEZIONE: Esercitazione Lazarus, Quiz su Moduli, Versioning su GitHub, Teoria a schede.
Nei lavori di `indice.json` il campo e `tipologia_lezione` (`quiz` o `teoria`); i nomi vecchi `tipologia` e `tipo` sono ancora accettati.
Se manca: un id che comincia per `scheda-` e teoria, tutto il resto e quiz. Un lavoro gia creato non si ricrea mai (conta solo l'id).
Il motore (v2.8) scrive la scheda `Tipologie lezione` (classi x TIPOLOGIA LEZIONE) nel foglio Fabbrica.
