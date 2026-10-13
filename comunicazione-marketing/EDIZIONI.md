# Le edizioni della comunicazione e dell'Atlante

**Versione 1.1** — 13/10/2026 — Il laboratorio di informatica secondo le idee di Nicola Regge. Area Docente.

Come si numera l'insieme dei materiali (Atlante, mappa, racconto, PDF) e come si controlla che sia tutto giusto.

## 00 L'idea in breve

1. **Ogni parte ha la sua versione**, scritta dentro la parte stessa: l'Atlante può essere alla 1.3 mentre il racconto resta alla 1.0.
2. **L'edizione è la fotografia dell'insieme:** dice quali parti, e in quale versione, stanno insieme. Si scrive in `comunicazione-marketing/EDIZIONE.json`.
3. **Se cambia anche una sola parte, si sale di edizione** (1.0, poi 1.1, poi 1.2). Un cambio grande dell'insieme (per esempio una parte nuova importante) fa salire il primo numero (2.0).
4. **L'impronta** è un codice di 10 caratteri calcolato da tutti i file delle parti. Se un file cambia, cambia l'impronta. Così dal numero dell'edizione e dall'impronta si capisce se quello che c'è è proprio l'edizione controllata.
5. **Su Git l'edizione è legata a un commit** (scritto nel registro del capitolo 03): si può sempre tornare a quella fotografia esatta. Le etichette (tag) Git da qui non si possono pubblicare.

## 01 Come si legge

1. In alto nell'Atlante c'è scritto, per esempio, «versione 1.3 · edizione 1.0»: l'Atlante è alla 1.3 e fa parte dell'edizione 1.0.
2. La composizione completa di ogni edizione è nella tabella del capitolo 03.

## 02 Come si controlla

1. Il comando che controlla tutto:
```
python3 strumenti/controlla_edizione.py --browser
```
2. Che cosa controlla:
   1. ogni parte ha nel sorgente la stessa versione scritta nell'edizione, e i suoi file ci sono;
   2. tutti i link, partendo dall'Atlante, dalla mappa, dalla pagina e dal racconto, portano a una pagina che esiste (anche quelli dentro i PDF);
   3. nelle parti pubbliche non ci sono nomi di ragazzi, nome della scuola o della città, marchi di altri;
   4. ogni pagina si apre senza errori sul telefono e sul computer, senza uscire dai bordi;
   5. il racconto arriva fino in fondo con la voce (simulata nel controllo);
   6. l'impronta è uguale a quella dell'edizione.
3. Se tutto va bene scrive «TUTTO A POSTO · edizione X · impronta Y». Altrimenti scrive l'elenco «DA SISTEMARE».
4. I link verso servizi esterni (la demo con l'accesso via email) dal computer di controllo non si raggiungono: si provano a mano.

## 03 Registro delle edizioni

| Edizione | Data | Composizione | Impronta |
|---|---|---|---|
| 1.1 | 13/10/2026 · commit c50b78018f | Atlante 1.4 · Il parco del corso 1.0 · Pagina «Il laboratorio raccontato» 1.0 · Racconto 1.0 · Brochure 1.4 · Presentazione 1.2 · Progetto del treno 1.2 · Indice della comunicazione 0.5 | fce06e3c08 |
| 1.0 | 13/10/2026 · commit bd2a58004f | Atlante 1.3 · Il parco del corso 1.0 · Pagina «Il laboratorio raccontato» 1.0 · Racconto 1.0 · Brochure 1.4 · Presentazione 1.2 · Progetto del treno 1.2 · Indice della comunicazione 0.5 | 63d129690e |

## 04 Come si fa un'edizione nuova

1. Si cambia la parte e si sale la sua versione (nel suo sorgente).
2. Si aggiorna la versione della parte e il numero dell'edizione in `EDIZIONE.json`.
3. Si rigenerano le pagine e i PDF.
4. Si lancia il controllo; quando dice «TUTTO A POSTO» si fissa l'impronta:
```
python3 strumenti/controlla_edizione.py --browser --fissa
```
5. Si aggiunge una riga al registro del capitolo 03 e si scrive nel registro il commit dell'edizione.

## 05 Registro delle versioni di questo documento

1. **v1.1 (13/10/2026):** edizione 1.1 nel registro (in alto la più nuova).
2. **v1.0 (13/10/2026):** prima versione, con l'edizione 1.0.
