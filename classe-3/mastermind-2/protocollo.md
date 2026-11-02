# Mastermind 2.0 - il protocollo (spiegato semplice)

Versione 1.0 - 02/11/2026 - 3INF - Lazarus / Free Pascal

Un solo codice segreto per tutta la classe. Il PC del prof è il SERVER: pensa il codice e tiene la classifica. I PC dei ragazzi sono i CLIENT: provano a indovinare e vedono la loro posizione.

## 1. Le regole del gioco

1. Il codice è di 4 cifre, ognuna da 1 a 6 (anche cifre uguali, come 1123).
2. Esatte = cifra giusta al posto giusto. Spostate = cifra giusta al posto sbagliato (stesso conteggio del Mastermind normale).
3. Il prof preme **V** (Via!): prima del Via ogni tentativo riceve la risposta WAIT.
4. Si vince indovinando il codice. La classifica è per numero di tentativi (meno è meglio); a parità, vince chi ci ha messo meno secondi dal Via. Stessi tentativi e stessi secondi = stessa posizione (pari merito).
5. Dopo che hai indovinato, altri tentativi non contano: resti col tuo risultato.

## 2. Due modi per parlare con il server

| Modo | Come funziona | Quando |
|---|---|---|
| **B - FILE (predefinito)** | si scrivono righe in una cartella condivisa o in un repository GitHub | sempre disponibile, non chiede permessi di rete |
| **A - RETE (TCP, facoltativo)** | il client si collega all'IP del PC del prof, porta 5050 | veloce (risposta subito), ma il firewall del PC del prof può chiedere «Consenti accesso» |

Il client prova prima la rete se esiste `server.txt`; se il server non risponde passa da solo ai file (se c'è `cartella.txt`).

## 3. Modo A - RETE (TCP)

Una connessione per ogni richiesta: il client manda UNA riga, il server risponde con UNA riga, poi la connessione si chiude. Ogni riga finisce con "a capo" (codice 10). I campi sono separati da punto e virgola `;`. Il nome non può contenere `;`.

### 3.1 Messaggi del client

| Riga | Significato |
|---|---|
| `GUESS;NOME;1234` | tentativo: il nome e le 4 cifre |
| `STATO;NOME` | voglio solo aggiornare la console (nessun tentativo) |

### 3.2 Risposte del server

| Riga | Significato |
|---|---|
| `RESULT;esatte;spostate;tentativi;posizione;totale;migliore;peggiore` | tentativo sbagliato |
| `WIN;NOME;tentativi;secondi;posizione;totale;migliore;peggiore` | hai indovinato (anche se riprovi dopo: resta lo stesso) |
| `WAIT` | il prof non ha ancora dato il Via |
| `STATO;ATTESA` o `STATO;GIOCO` seguito da `;tentativi;posizione;totale;migliore;peggiore` | risposta a STATO |
| `ERR;motivo` | riga sbagliata (codice non valido, nome mancante, comando sconosciuto) |

Significato dei numeri:

1. **tentativi** = i tuoi tentativi finora.
2. **posizione** = il tuo posto tra chi ha finito (0 = non hai ancora indovinato).
3. **totale** = quanti hanno indovinato finora.
4. **migliore** = tentativi del migliore tra chi ha finito (0 se nessuno).
5. **peggiore** = tentativi del peggiore tra chi ha finito.
6. **secondi** = secondi dal Via alla tua vittoria, misurati dal server.

Nota: quando indovini il server risponde con `WIN` al posto di `RESULT` (è un'unica riga, così il client legge sempre una sola riga).

### 3.3 Esempi

```
client  ->  GUESS;Sara M.;1234
server  ->  RESULT;1;2;1;0;0;0;0

client  ->  GUESS;Sara M.;4162
server  ->  WIN;Sara M.;2;85;3;5;1;4

client  ->  GUESS;Sara M.;1111          (prima del Via)
server  ->  WAIT
```

### 3.4 IP e nomi (facoltativo)

Se accanto al server c'è `ip-nomi.txt` (una riga per PC, `IP;NOME`), il server prende il nome dall'IP di chi si collega: nessuno può scrivere un nome falso e in classifica compaiono i nomi veri. Per un IP non presente vale il nome scritto dal client. Il pannello del server mostra chi non ha ancora provato.

## 4. Modo B - FILE

Cartella condivisa (cartella di rete, oppure repository GitHub clonato e sincronizzato con GitHub Desktop):

```
cartella/
  partita.txt          scritto dal SERVER
  ranking.txt          scritto dal SERVER
  comando.txt          (facoltativo) il prof scrive VIA, NUOVA o FINE
  giocatori/
    NOME.txt           scritto da OGNI studente, solo il suo
```

### 4.1 partita.txt (il server lo riscrive a ogni Via e a ogni nuova partita)

Prima del Via (il seme NON c'è, così il codice non si può ricavare):

```
PARTITA;P3x64719;0;ATTESA
```

Dopo il Via (il seme permette al client di ricavare lo stesso codice del server; l'ultimo numero è l'ora del Via secondo l'orologio del server, in secondi):

```
PARTITA;P3x64719;424242;GIOCO;4002345678
```

### 4.2 giocatori/NOME.txt (una riga per tentativo, aggiunta in fondo)

```
id;NOME;1234;secondi
P3x64719;Sara M.;1234;17
P3x64719;Sara M.;4162;85
```

1. `id` = l'id della partita letto da partita.txt (le righe di partite vecchie vengono ignorate).
2. `secondi` = secondi dal Via, calcolati dal PC dello studente.
3. Il server NON si fida del risultato: rifà lui il conteggio con il suo codice. Una riga che finisce senza "a capo" è considerata a metà e viene letta al giro dopo.
4. Ogni studente scrive solo nel proprio file: in Git non ci sono conflitti.

### 4.3 ranking.txt (scritto dal server, letto da tutti i client)

```
PARTITA;P3x64719
STATO;GIOCO
TOTALE;4
MIGLIORE;1
PEGGIORE;3
R;1;Bruno;1;20;S
R;2;Anna;2;10;S
R;2;Dino;2;10;S
R;4;Carla;3;30;S
R;0;Fabio;1;0;N
```

Le righe `R` sono: `R;posizione;nome;tentativi;secondi;S o N` (S = ha indovinato, N = sta ancora provando, posizione 0). Il server rilegge la cartella ogni 2 secondi e riscrive i due file quando cambia qualcosa.

### 4.4 I limiti, detti chiaramente

1. Con una **cartella di rete** il ritardo è di pochi secondi: va bene per giocare dal vivo.
2. Con **GitHub** serve: lo studente fa Commit e Push, il PC del prof fa Pull, il server aggiorna, il prof fa Commit e Push di `ranking.txt`, lo studente fa Pull. Il ritardo è di **almeno un minuto**: va bene come piano di riserva, NON per giocare dal vivo.
3. Nel modo file il codice si ricava dal seme: un ragazzo bravo potrebbe leggerlo dal programma. Il server però ricalcola tutto e conta i tentativi veri; è un gioco di fiducia, non una verifica.
4. I tempi nel modo file dipendono dagli orologi dei PC: se sono sballati di più di qualche secondo conta il numero di tentativi.

## 5. File di configurazione accanto al programma dello studente

| File | Contenuto | Esempio |
|---|---|---|
| `server.txt` | una riga: IP:PORTA del PC del prof | `192.168.10.5:5050` |
| `cartella.txt` | una riga: percorso della cartella condivisa | `Z:\mastermind` |

Se ci sono tutti e due, il client prova la rete e, se non risponde, usa i file.

## 6. File del progetto

| File | A cosa serve |
|---|---|
| `mm_logica.pas` | il cervello: codice, esatte/spostate, tabella, classifica, protocollo (nessuna finestra, nessuna rete) |
| `mm_file.pas` | trasporto B: file |
| `mm_tcp.pas` | trasporto A: TCP con `ssockets` (unità di Free Pascal, niente da installare) |
| `client_unit.pas` | la parte dello studente |
| `unit1_client.pas` + `unit1_client.lfm` | la finestra dello studente: indirizzo server, nome, Connetti, tentativo, Prova, storia, classifica e posizione |
| `server_mastermind.pas` | il server a console del prof |
| `test/` | le prove automatiche |
