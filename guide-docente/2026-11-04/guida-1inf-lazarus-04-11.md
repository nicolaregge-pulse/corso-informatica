# Guida del docente: 1INF Lazarus, mercoledì 04/11/2026

**Versione 1.0** — 04/11/2026. Laboratorio 8:00-11:00. Stringhe e interi: convertitore, calcolatrice, cassiere. Nessun nome di allievo (repository pubblico).

> **Nota:** Come si usa questa guida: la tabella a minuti di ogni ora è il copione. Le frasi tra virgolette sono da dire così, brevi. Le parole in grassetto sono da scrivere o far notare. Tutto ciò che non ho potuto provare è scritto «da verificare».

## 00 In una pagina

| Ora | Orario | Si fa | Vittoria entro 10 minuti | Si consegna |
|---|---|---|---|---|
| 1 | 8:00-9:00 | Convertitore di misure (percorso A: prima il recupero Sicurezza) | Form con bottone e scritta cambiata | unit1.pas + screenshot |
| 2 | 9:00-10:00 | Calcolatrice a 4 bottoni | Bottone + che scrive «7 più 5 fa 12» | unit1.pas + screenshot |
| 3 | 10:00-11:00 | Il cassiere: resto, banconote, scontrino | Il resto (dati meno prezzo) | unit1.pas + screenshot |

1. **Ogni ora:** firma il registro all'inizio dell'ora, non dopo (limite 14:05 per tutte le ore del giorno).
2. **Ogni cambio di attività:** ricorda il quaderno («Ricopiate sul quaderno il riquadro giallo»).
3. **Regola 31:** si apre una ora per volta. Ora 2 e ora 3 sono «in arrivo» finché non lo dici a Claude in chat («sblocca ora 2»).
4. **Domande dei ragazzi:** vanno alla casella dell'assistente, non a te. Tu guardi il cruscotto e aiuti di persona chi è bloccato.

> **Attenzione:** Una svista da correggere prima di entrare: nella pagina dell'ora 3 il passo 4 scrive su Label1, ma il passo 3 non dice di mettere una TLabel. Chi segue la pagina alla lettera avrà l'errore Identifier not found Label1. Soluzione a voce: «Mettete anche una Label sotto le caselle». Ho segnalato il difetto a Claude.

## 01 Prima di entrare (7:30-8:00)

1. **Sul PC del docente, schede del browser aperte:**
   1. La pagina dei ragazzi, ora 1: `https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lazarus-04-11/modulo-1.html`
   2. Il tuo cruscotto: `https://nicolaregge-pulse.github.io/corso-informatica/anteprima/1inf-lazarus-04-11/cruscotto.html`
   3. Il monitor della lezione: `https://nicolaregge-pulse.github.io/corso-informatica/1inf-monitor/`
   4. Veyon aperto (gli screenshot vanno al monitor pubblico, regola di autoregolazione).
2. **La lavagna:** apri `lavagna-1inf-04-11.pdf` (20 pagine, una idea per pagina) con SumatraPDF sul proiettore, a schermo intero (F11 in Sumatra). Pagine: 1-9 ora 1, 10-15 ora 2, 16-20 ora 3.
3. **Il tuo Lazarus pronto:** apri Lazarus e prepara il convertitore già finito (codice in `docs/anteprima/1inf-lazarus-04-11/codice/ora1_unit1.pas`). Servirà per mostrare il risultato in un minuto.
   > **Da confermare:** Il codice delle tre ore è controllato da un programma automatico ma non è mai stato provato in un Lazarus vero. Fai TU la prova prima (progetto nuovo, scrivi, F9). Se un punto non gira, lo dici a Claude.
4. **Presenze e registro:** manda le presenze a Claude quando le hai (restano nel riservato). Il registro: firma ogni ora all'inizio, con il testo corto (sezione 06).
5. **Classroom:** i post dell'ora 1 (testo pronto in `POST-CLASSROOM-04-11.md` del riservato). Un solo «pubblica» a Claude basta per tutto il giorno; ora 2 e 3 escono una alla volta.
6. **Chi è A:** i ragazzi del recupero Sicurezza sono nel piano riservato (`PIANO-1INF-04-11.md`, punto 3). Dillo a voce, per nome, con tono normale: «Voi due fate prima un ripasso breve, poi Lazarus». Non è una punizione: è un percorso con meno fretta.
7. **Carta e penna sul banco:** tutti hanno un quaderno per il riquadro giallo (regola 23).

## 02 I concetti, spiegati a te

1. **String e Integer: testo e numero.**
   1. Un **String** è testo: lettere, cifre, spazi, tutto. Un **Integer** è un numero intero (senza virgola) con cui puoi fare i conti.
   2. Esempio: il numero sulla maglia di un calciatore è un testo. '10' è solo il disegno di un 1 e di uno 0. Per questo '5' + '3' fa '53' (due testi attaccati) e 5 + 3 fa 8.
   3. **Edit1.Text è sempre testo**, anche se il ragazzo scrive 5. Per fare i conti serve trasformarlo in numero.
2. **StrToInt e IntToStr: i due traduttori.**
   1. **StrToInt** = da testo a numero. **IntToStr** = da numero a testo. Il nome si legge «String To Integer» e «Integer To String».
   2. Immagine: la dogana. Il testo '5' entra nella dogana e ne esce come numero 5. Prima di scrivere il risultato su un Label, il numero deve rifare la dogana al contrario, perché Caption accetta solo testo.
3. **Perché StrToInt può dare errore.**
   1. Non tutti i testi sono numeri. Se la casella è vuota, o c'è scritto «ciao», o «3,5» (con la virgola), il traduttore non sa che numero uscirne e il programma si ferma con un messaggio.
   2. Il messaggio (da verificare nel testo esatto): `Project convertitore raised exception class 'EConvertError' with message: "ciao" is an invalid integer`. Vuol dire: «ciao non è un numero valido».
   3. **StrToIntDef(testo, 0)** = «se non riesci, usa 0». Il programma non si ferma. Attenzione: «3,5» diventa 0, non 3: i ragazzi si stupiranno.
4. **div e mod: la divisione fatta con i sacchetti.**
   1. 17 caramelle, 5 per sacchetto. **17 div 5 = 3**: i sacchetti PIENI. **17 mod 5 = 2**: le caramelle che AVANZANO.
   2. div = «quante volte ci sta». mod = «quanto avanza». Entrambi danno sempre un numero intero.
   3. Uso vero: 135 minuti. 135 div 60 = 2 ore. 135 mod 60 = 15 minuti. Cioè 2 ore e 15 minuti. Stesso trucco per il cassiere: quante banconote da 10 (div), quanto resta da pagare (mod).
   4. Un uso per il futuro: **n mod 2** vale 0 se n è pari, 1 se è dispari.
5. **Perché C * 9 div 5 + 32 dà 98 e non 98,6 con 37 gradi.**
   1. Con i numeri interi div butta via la virgola: 37 * 9 = 333, 333 div 5 = 66 (non 66,6), più 32 = 98. È normale: Integer non ha decimali.
   2. Pascal fa prima * e div (da sinistra a destra), poi + e meno. Quindi la formula è corretta senza parentesi.
6. **Il + tra testi.** Con i testi il segno + non somma: unisce. **'Cliente: ' + Edit1.Text** diventa «Cliente: Maria». Si chiama concatenare (unire in fila).
7. **Evento OnClick, il ponte con quello che sanno.** Doppio clic sul bottone: Lazarus scrive già `procedure ... Button1Click`, `begin`, `end;`. Il ragazzo scrive solo dentro. È lo stesso che facevano nella calcolatrice vecchia: nuovo è solo StrToInt e div/mod.
8. **Integer ha un limite.** In Lazarus (modalità objfpc) arriva a circa 2 miliardi. Oltre, il numero «gira» senza avvisare. Non serve dirlo ai ragazzi oggi (da verificare sulle vostre impostazioni).

## 03 Ora 1 (8:00-9:00): il convertitore di misure

**Obiettivo in una frase:** «Oggi i numeri lavorano per noi: scriviamo un numero e il programma lo converte.»

**Vittoria rapida:** entro 10 minuti ogni ragazzo ha la finestra con bottone che cambia scritta (passi 1-5 della pagina: li conoscono già). Entro le 8:30 il primo bottone dà «5000 metri» con F9.

| Minuti | Tu | Loro |
|---|---|---|
| 8:00-8:05 | Presenze a Claude. Firma l'ora. Dividi A e B. | Aprono la pagina da Classroom, scrivono nome e cognome |
| 8:05-8:10 | Lavagna p.1-3. Mostra il tuo convertitore che gira: «Questo lo fate in 20 minuti». | Guardano, scelgono A o B |
| 8:10-8:20 | Lavagna p.4. Giri tra i banchi mentre fanno i passi 1-5. | Progetto, salva in Documenti, Edit, Label, bottone |
| 8:20-8:30 | Lavagna p.5: il primo bottone, riga per riga. | Doppio clic, scrivono il codice, F9, provano 5 |
| 8:30-8:35 | «Quiz di 4 minuti, poi si torna a Lazarus.» | Quiz 5+3 su Moduli (8 domande, servono 6) |
| 8:35-8:45 | Mostra come si copia un bottone e si cambia il numero. | Ore in minuti, euro in centesimi |
| 8:45-8:52 | Lavagna p.6-8: caramelle, poi 135 minuti. | Celsius, poi minuti in ore e minuti |
| 8:52-8:58 | Lavagna p.9: quaderno. «Fallo tuo». | Fallo tuo, quaderno, Ctrl+S, screenshot |
| 8:58-9:00 | Controlla il cruscotto. | Premono «Manda al prof» |

> **Nota:** Ora 1 è lunga: non tutti arriveranno ai 5 bottoni. Va bene. L'importante è il primo bottone (km in metri) e il quiz. Gli altri sono copia-modifica per chi va veloce.

**Percorso A (recupero Sicurezza):** A1 ripasso (quaderno: pericolo, danno, prevenzione, protezione, RLS) → A2 quiz Sicurezza B (8 domande, servono 6) → A3 poi Lazarus. Tempo previsto: 15-20 minuti, poi primo bottone entro le 8:40. Il quiz 5+3 lo fanno all'inizio dell'ora 2. Il voto di Lazarus non cambia.

**Cosa dire (frasi brevi):**

1. «Il computer legge una cifra scritta come un disegno. Per fare i conti deve capire che è un numero.»
2. «StrToInt è la dogana: il testo entra, il numero esce.»
3. «div: quanti sacchetti pieni. mod: quante caramelle avanzano.»
4. «Se il programma si ferma con un messaggio rosso, non avete rotto il computer. Succede anche ai professionisti.»

**Domande al volo (prova del nove).** Segna OK o KO, senza commentare davanti agli altri.

| Domanda | Risposta attesa |
|---|---|
| Quanto fa '5' + '3'? E 5 + 3? | 53 (testo attaccato). 8 (numero). |
| Cosa fa StrToInt? | Da testo a numero. |
| 17 div 5? 17 mod 5? | 3 e 2. |
| 135 minuti sono quante ore e minuti? | 2 ore e 15 minuti. |
| Perché Label1.Caption vuole IntToStr? | Perché Caption vuole testo, non numero. |

**Errori tipici ora 1:**

| Cosa vedono | Cosa significa | Cosa fare |
|---|---|---|
| `Identifier not found "Edit1"` | Il nome non esiste: Edit cancellato o rinominato. | Ispettore oggetti, proprietà Name: deve essere Edit1. |
| `Identifier not found "km"` | Variabile non dichiarata o scritta diversa. | Controllare la riga `var` e la scrittura (maiuscole ok, lettere uguali). |
| `Incompatible types: got "AnsiString" expected "LongInt"` | Un testo dove va un numero: manca StrToInt. | Scrivere `StrToInt(Edit1.Text)`. |
| `Incompatible types ... expected "AnsiString"` oppure `Operator is not overloaded` | Un numero dove va un testo: manca IntToStr. | `Label1.Caption := IntToStr(metri) + ' metri'`. |
| `Syntax error, ";" expected` | Manca il punto e virgola alla riga prima. | Guardare la riga sopra a quella segnata. |
| `Unterminated string` | Manca l'apice di chiusura. | Chiudere il testo con '. |
| Finestra «raised exception class EConvertError» | Casella vuota o non numero. | «Scrivete un numero intero» e premere Continua (o Stop, il quadrato rosso). |
| Il bottone non fa niente | Doppio clic non fatto, o codice nel bottone sbagliato. | Riaprire con doppio clic sul bottone giusto. |
| F9 non riparte | Il programma di prima è ancora aperto. | Chiudere la finestra del programma, poi F9. |
| Non trovo il file | Salvato altrove. | Cercare in Documenti, cartella convertitore. |

> **Da confermare:** I testi esatti degli errori del compilatore dipendono dalla versione di Free Pascal: sono quelli tipici, non provati sui PC della scuola.

**Cruscotto: cosa guardare.** Chi è fermo da più di 5 minuti. Chi ha il percorso A e a che passo. La colonna «ora 1» (spunta quando unit1.pas supera il controllo automatico). Veyon: fuori compito in rosso. Il quiz 5+3.

**Sblocco ora 2:** alle 9:00, se il primo bottone gira per la maggior parte. Scrivi a Claude: «sblocca ora 2». Chi non ha finito continua l'ora 1 (la pagina resta aperta, da verificare nel cruscotto).

**Consegna:** `unit1.pas` e lo screenshot, bottone «Manda al prof».

**Quaderno da ricopiare (lavagna p.9):**

```
String = testo   '53'
Integer = numero   53
div = senza virgola   17 div 5 = 3
mod = quello che avanza   17 mod 5 = 2
C * 9 div 5 + 32 = Fahrenheit
```

## 04 Ora 2 (9:00-10:00): la calcolatrice a 4 bottoni

**Obiettivo:** «Due caselle, quattro bottoni, il risultato scritto come una frase.»

**Vittoria rapida:** entro 10 minuti il bottone + scrive «7 più 5 fa 12». Hanno già fatto il progetto: è più veloce di ora 1.

| Minuti | Tu | Loro |
|---|---|---|
| 9:00-9:03 | Firma l'ora. «sblocca ora 2» a Claude. Chi riprende il quiz 5+3 lo fa ora. | Aprono la pagina ora 2 |
| 9:03-9:08 | Lavagna p.10-11: come sarà il programma. | Nuovo progetto, salvano in cartella calcolatrice |
| 9:08-9:20 | Lavagna p.12-13: la casella vuota e StrToIntDef. | Edit, Edit, 4 bottoni, Label. Bottone +. F9: 7 più 5 |
| 9:20-9:40 | Giri. | Meno, per, diviso |
| 9:40-9:50 | Lavagna p.14: if b = 0. Bonus per chi arriva. | Fallo tuo, quaderno |
| 9:50-10:00 | Controllo cruscotto. | Ctrl+S, screenshot, Manda al prof |

**Cosa dire:**

1. «Il bottone più lo conoscete. Cambia solo che ora le caselle sono testi e devono diventare numeri.»
2. «StrToIntDef: Def vuol dire Default, se non riesci usa questo. Casella vuota? Fa 0 e non si blocca.»
3. «Il risultato lo scriviamo come una frase: testo, numero tradotto, testo.»

**Domande al volo:**

| Domanda | Risposta attesa |
|---|---|
| Cosa succede con StrToInt se la casella è vuota? | Errore, il programma si ferma. |
| E con StrToIntDef(testo, 0)? | Usa 0 e va avanti. |
| Quanto fa 7 div 2? Perché? | 3, perché div butta via la virgola. |
| Perché dividere per zero non si può? | Non esiste un risultato: il programma darebbe errore. |

**Errori tipici ora 2:**

| Cosa vedono | Cosa significa | Cosa fare |
|---|---|---|
| Funziona solo l'ultimo bottone | Hanno incollato tutti i codici nello stesso bottone (la pagina mostra sempre Button1Click). | Ogni bottone ha il suo doppio clic: il meno va in Button2Click, e così via. |
| 3,5 + 2 fa 2 | StrToIntDef non legge la virgola e usa 0. | «Qui solo numeri interi, senza virgola.» |
| `EDivByZero` («Division by zero», da verificare il testo) | Diviso 0. | Aggiungere l'if del bonus. |
| `Incompatible types` con `/` | Il segno / dà risultato con virgola. | Usare `div`. |
| Il risultato non si vede | Label1 troppo piccola o dietro un altro componente. | Ingrandire la Label. |

**Quaderno (lavagna p.15):**

```
StrToIntDef(testo, 0) = se non riesci, 0
'ciao ' + 'Anna' = 'ciao Anna'
if b = 0 then ... else ...
a div b non si fa se b = 0
```

**Sblocco ora 3:** alle 10:00 con la stessa regola. «sblocca ora 3» a Claude.

## 05 Ora 3 (10:00-11:00): il cassiere

**Obiettivo:** «Un cassiere fa il resto: quante banconote e monete servono?»

**Vittoria rapida:** entro 10 minuti il resto: soldi dati meno prezzo, scritto su una Label.

| Minuti | Tu | Loro |
|---|---|---|
| 10:00-10:03 | Firma l'ora. Lavagna p.16-17: il resto (37 meno 12 fa 25). | Aprono ora 3, nuovo progetto, salvano in cassiere |
| 10:03-10:15 | Giri. Ricorda la Label (vedi 00). | 3 Edit, bottone, Memo, Label. Codice del resto. F9 |
| 10:15-10:35 | Lavagna p.18: banconote a gradini. Disegna 25 euro: 2 da 10, 1 da 5. | div e mod a gradini |
| 10:35-10:48 | Lavagna p.19: lo scontrino col nome. | Memo, Add, nome del cliente |
| 10:48-10:56 | Lavagna p.20: quaderno. Fallo tuo: il nome del negozio. | Ricopiano, Ctrl+S, screenshot |
| 10:56-11:00 | Cruscotto. «Saperlo spiegare» a voce. | Manda al prof |

**Cosa dire:**

1. «Il resto è una sottrazione. Per le banconote: quante da 10? div. Quanto avanza? mod. Poi si ricomincia con quel che avanza.»
2. «Con 37 euro: 3 da 10, avanzano 7; 1 da 5, avanzano 2; 1 moneta da 2, avanzano 0.»
3. «Lo scontrino unisce testi con il più: 'Cliente: ' + il nome.»

**Domande al volo:**

| Domanda | Risposta attesa |
|---|---|
| Resto di 37 euro: quante banconote da 10? | 3 (37 div 10). |
| Quanto avanza? | 7 (37 mod 10). |
| Cosa fa il + tra due testi? | Li unisce. |
| Perché ripartiamo da resto mod 10 e non da 37? | Perché le banconote da 10 sono già state tolte. |

**Errori tipici ora 3:**

| Cosa vedono | Cosa significa | Cosa fare |
|---|---|---|
| `Identifier not found "Label1"` | Nella pagina manca la Label. | Mettere una TLabel (Standard), nome Label1. |
| Banconote sbagliate | Dimenticato `resto := resto mod 10`. | Controllare che dopo ogni div ci sia il mod. |
| Resto negativo con strani numeri | Soldi dati meno del prezzo. | Bonus: if dati < prezzo, scrivere «Mancano soldi» (negativi con mod: da verificare provando). |
| Lo scontrino si allunga a ogni clic | Manca `Memo1.Clear`. | Metterlo prima di Add. |
| Nome del cliente vuoto | Edit1 vuota. | Scrivere un nome. |

**Quaderno (lavagna p.20):**

```
resto = dati - prezzo
div = quante volte ci sta
mod = quanto avanza
'Cliente: ' + nome = testo unito
```

## 06 Chi è indietro, chi si stufa, chi finisce prima

1. **Chi è indietro.**
   1. Non dire mai «sei indietro». Dì: «Sei al passo 5. Il prossimo è uno solo».
   2. Percorso facilitato: ora 2 solo il bottone +; ora 3 solo il resto. Contano come un risultato vero.
   3. Mostragli il suo risultato più piccolo, vero: «Guarda, qui funziona».
   4. Mai correggere davanti agli altri. Chinati al suo livello e leggi con lui l'errore: le parole dell'errore dicono cosa controllare.
2. **Chi si stufa.**
   1. Cambia il gioco, non la fatica: «Fallo tuo, cambia il colore e il titolo».
   2. Dagli un compito di aiuto vero: «Quando il tuo gira, spiegami come l'hai fatto». Rotazione, mai sempre gli stessi.
   3. Ricorda la frase: «Provarci qui conviene: non c'è vergogna, solo bug».
3. **Chi finisce prima.**
   1. Ora 1: metri in km e metri (2500 metri = 2 km e 500 m) con div e mod.
   2. Ora 2: bottone «pari o dispari» con `a mod 2 = 0`.
   3. Ora 3: sconto 10 per cento sul prezzo, o banconote da 20 e 50.
   4. Poi: spiega la tua soluzione a un compagno (prova del nove).
4. **Chi non c'è o è fuori dall'aula:** se un ragazzo esce e dopo 5 minuti non è rientrato, dillo a Claude.

## 07 Fine ora, registro, firma

1. **Ogni fine ora:** chiedi a tre ragazzi, a voce: «Cosa fa div?». Segna 70 OK / 50 KO nel cruscotto o dillo a Claude.
2. **Testi per il registro (corti, già pronti):**

Ora 1:

```
Lazarus: Caption e OnClick, convertitore
```

Ora 2:

```
Lazarus: Caption e OnClick, calcolatrice
```

Ora 3:

```
Lazarus: OnClick, il cassiere
```

3. **Voce dell'Allegato A:** PFP_1, Competenza 15, I anno: «Programmazione a eventi con Lazarus (Free Pascal): form, componenti, proprietà, gestori di evento».
   > **Attenzione:** String, Integer, StrToInt, div e mod NON sono nelle sotto-voci dell'Allegato A 1INF. La lezione si regge su TEdit, Caption, OnClick, ma resta una voce da aggiungere (criticità aperta, ne parla Claude).
4. **Firma:** all'inizio di ogni ora. «FIRMA» scritta in verde vuol dire già firmata. Scadenza assoluta 14:05: le ore non firmate si perdono.
5. **A fine giornata:** Claude ti chiede gli argomenti realmente svolti e li registra.
