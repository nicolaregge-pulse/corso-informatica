# 00 Passi notturni obbligatori della Chat del giorno

**Versione 1.0** — 28/10/2026 — documento interno di Claude

La Chat del giorno (attività programmata, lunedì-venerdì) li esegue TUTTI, in quest'ordine, dopo aver riletto le regole e prima del messaggio del mattino al docente. Ogni passo nasce da voci del registro degli errori (numero tra parentesi); la mappa completa è `MAPPA-REGOLE-CONTROLLI.md`. Nel messaggio del mattino va solo ciò che resta ROSSO e blocca la lezione.

## 01 Controlli con un comando

1. Audit delle regole (coda, ponte, annunci, pagine, versioni, firme; #49 #81 #84 #85 #93 #97 #107 #114 #118 #125 #129 #136): stampa VERDE o ROSSO con il file dei dettagli; ciò che è ROSSO si sistema prima della lezione.

```
python3 /home/user/corso-informatica-riservato/generatori/audit_regole.py
```

2. Prove dei controlli automatici (hook): devono stampare «N/N»; se no, lo si dice al docente nella prima riga.

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_messaggio.py
```

```
python3 /home/user/corso-informatica/.claude/hooks/prove/prova_limite.py
```

3. Sito pubblicato (#79): dalla cartella del pubblico; scrive anche il timbro che l'hook usa prima di accettare un link al sito.

```
cd /home/user/corso-informatica && bash strumenti/aspetta_pubblicazione.sh
```

4. Per ogni classe in orario oggi, dopo aver messo il compito in bozza programmata (#94 #105 #120 #128): GIALLO «DRAFT programmato» va bene di notte; ROSSO si sistema.

```
python3 /home/user/corso-informatica-riservato/generatori/verifica_lezione.py 1INF
```

## 02 Controlli sulla lezione di oggi (si scrive sì o no per ognuno nel diario del giorno)

1. Storia della classe riletta: annunci e compiti degli ultimi giorni, `ARGOMENTI-SVOLTI-2026-27.md`; la lezione non è già stata fatta (#99; 01/10 n. 11).
2. Il compito lo possono iniziare TUTTI: passo 1 = contare, scegliere o copiare; ogni passo un'azione che si vede sullo schermo, per un dodicenne; niente foto, telefono o lavoro a mano non chiesto (#43 #44 #45 #123).
3. Versione facile di massimo 3 passi pronta e data a tutti; la versione completa è per chi finisce (#126).
4. Il primo risultato visibile nel controllo automatico arriva entro 10 minuti; i controlli danno punti anche ai passi intermedi (#110 #38).
5. Durate stimate dal contenuto: circa 1 minuto per domanda a crocette, 2-3 per livello di un gioco (#102).
6. Riquadro «Spiegalo in 30 secondi» nella pagina, dopo la teoria e prima del compito (#76).
7. Una sola strada di consegna, con UN bottone, provata come un ragazzo fino all'arrivo nel riservato (#68 #81 #62 #42).
8. Ogni pagina che produce un risultato lo fa arrivare al docente, non solo sul PC del ragazzo (#103).
9. La pagina della classe mostra solo il lavoro di oggi (05/10 n. 10).
10. Sei bottoni, cruscotto e pagine del docente con la DATA DI OGGI, ogni bottone aperto mostra dati di oggi (#71 #75 #77 #80 #60).
11. Lingue della classe controllate anche sul testo del compito della coda (1INF italiano, arabo, cinese; 2INF solo italiano; 3INF italiano + bangla per il PC 14; 4TI italiano) (#49 #82 #119).
12. Scadenza detta dal docente; se non l'ha detta, la campanella dell'ultima ora della classe, scritta nel messaggio del mattino (#97 #122).
13. Quiz e Moduli già creati con il loro link; niente «arriva tra poco» (#129).
14. `FIRME-REGISTRO-2026-27.md`: aggiungere la sezione di oggi con le ore della giornata «da firmare» (le segna «firmata» chi riceve la conferma) (#137).

## 03 Promemoria a orario (strumento send_later, uno per riga, orari di Roma convertiti in UTC)

1. Alle 13:30 di ogni giorno di lezione: «Leggi FIRME-REGISTRO-2026-27.md: se un'ora di oggi non risulta firmata, scrivi al docente UNA riga da sola, in cima: FIRMA <classe> <ore> entro le 14:05» (#137, CLAUDE.md regola 4).
2. 10 minuti prima della prima ora di ogni classe: «Lancia verifica_lezione.py <CLASSE>; dai al docente il testo dell'annuncio per Classroom in un riquadro (piano B) e, alla campanella, se il compito non è PUBLISHED scrivi PIANO B in cima» (#131 #128 #104).
3. 10 minuti prima della fine di ogni classe: «Consegna al docente quello che c'è (bozza segnata come bozza); poi ferma i giri automatici di questa classe e fai il push del riservato» (05/10 n. 35, #86, #112).
4. Alle 14:10: «Chiedi al docente gli argomenti realmente svolti e aggiorna ARGOMENTI-SVOLTI-2026-27.md» (CLAUDE.md regola 4).

## Changelog

1. v1.0 (28/10/2026): prima versione, dalla mappa regole-controlli.

15. Regola 28: per ogni classe del giorno controlla che cruscotto docente e pagina dei ragazzi mostrino per ogni presente avanzamento, consegna letta, mancanze, minuti da fermo, Veyon, voto con il conto; prova con 2 allievi veri; se manca qualcosa, sistemalo prima della campanella.

16. Regola 24, SEMPRE (Nicola 28/10): durante la giornata, alla fine di ogni ora di lezione, lancia nel riservato `python3 generatori/report_ore.py --giorno <oggi> --immagini <cartella delle immagini della chat> --config config/report-ore-<AAAAMMGG>.json` (prepara il config del giorno al mattino) e manda a Nicola in chat il PDF dell'ora: screenshot Veyon a piena risoluzione, note personali del registro, presenze, fuori compito, consegne. A fine giornata rigenera tutti i PDF del giorno e mandali.
