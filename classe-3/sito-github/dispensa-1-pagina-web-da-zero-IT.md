<!-- generato da dispensa-1-pagina-web-da-zero-IT.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 1 — La mia pagina web da zero

Classe 3 · Informatica · 05/10/2026 · HTML + CSS in due file separati · italiano

**Cosa ottieni oggi:** una cartella **mio-sito** con **due file** : **index.html** (il **contenuto** : i testi) e **style.css** (l'**aspetto** : i colori). Doppio clic e la tua pagina si apre nel browser. Nella Dispensa 2 la mettiamo **su internet**.

# Ciao, sono Leo

Questo è il mio primo sito web.

### Chi sono

Studio informatica e mi piace creare cose nuove.

### Le mie passioni

  * Calcio
  * Videogiochi
  * Musica

### Il mio sogno

Lavorare con i computer.

Sito creato da me - 2026

Ecco come sarà (poi la fai tua)

Desktop > mio-sito

index.html style.css  
  
index.html = CONTENUTO  
style.css = ASPETTO

La cartella: esattamente due file

**Carta e penna:** disegna sul quaderno la cartella **mio-sito** con dentro i due file. Fai una freccia da index.html a style.css e scrivici sopra **< link>**. Scrivi: **HTML = contenuto, CSS = aspetto**.

**Il tuo sito diventerà PUBBLICO** (lo vedrà chiunque su internet). Quindi scrivi **solo il nome o un soprannome**. **MAI** cognome, telefono, email, indirizzo, foto del viso.

## 1\. Il codice (uguale per tutti — poi lo fai tuo)

**Il modo più sicuro per copiare:** apri la pagina del corso (il link è nel compito su Classroom) e premi il bottone **Copia** sopra il codice. Poi nel Blocco note premi Ctrl \+ V. Copiare dal PDF a volte rovina gli spazi.

RIQUADRO 1 — file index.html (il contenuto)
    
    
    <!DOCTYPE html>
    <html lang="it">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Il mio primo sito</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <h1>Ciao, sono Leo</h1>
      <p class="sotto">Questo è il mio primo sito web.</p>
    
      <div class="scheda">
        <h2>Chi sono</h2>
        <p>Studio informatica e mi piace creare cose nuove.</p>
    
        <h2>Le mie passioni</h2>
        <ul>
          <li>Calcio</li>
          <li>Videogiochi</li>
          <li>Musica</li>
        </ul>
    
        <h2>Il mio sogno</h2>
        <p>Lavorare con i computer.</p>
      </div>
    
      <p class="piede">Sito creato da me - 2026</p>
    </body>
    </html>
    

RIQUADRO 2 — file style.css (l'aspetto)
    
    
    body {
      background: lightblue;
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
    }
    
    h1 {
      color: darkblue;
    }
    
    .sotto {
      color: gray;
    }
    
    .scheda {
      background: white;
      max-width: 500px;
      margin: 20px auto;
      padding: 20px;
      border-radius: 12px;
      text-align: left;
    }
    
    h2 {
      color: teal;
    }
    
    .piede {
      font-size: 12px;
      color: gray;
    }
    

## 2\. I passi, uno alla volta

1Crea la cartella

Sul **Desktop** , in un punto vuoto: clic con il tasto **DESTRO** del mouse -> **Nuovo** -> **Cartella**. Scrivi il nome mio-sito e premi Invio.

2Fai vedere la fine dei nomi (consigliato)

Apri la cartella **mio-sito**. In alto clic su **Visualizza** -> **Mostra** -> **Estensioni nomi file** (compare la spunta). Così vedi se un file finisce con **.html** o, per errore, con **.txt**.

3Apri il Blocco note

In basso a sinistra clic su **Start** , scrivi Blocco note e clicca sul programma **Blocco note**.

4Incolla il codice HTML

Copia **tutto** il **RIQUADRO 1** e incollalo nel Blocco note (Ctrl \+ V).

5Fallo tuo

Cambia **Leo** con il tuo nome o un soprannome. Cambia **Chi sono** , **le passioni** e **il sogno** con cose tue. Non toccare le parole tra < e >: cambia solo il testo in mezzo.

6Salva come index.html

In alto a sinistra **File** -> **Salva con nome**. A sinistra scegli **Desktop** e apri **mio-sito**. In basso: **Salva come** -> **Tutti i file** ; **Nome file** : index.html; **Codifica** : **UTF-8**. Clic su **Salva**.

Salva con nome

Cartella: **Desktop > mio-sito**

Nome file: index.html

Salva come: Tutti i file (*.*)

Codifica: UTF-8   Salva

7Un foglio nuovo per il CSS

Nel Blocco note: **File** -> **Nuovo** (si apre un foglio vuoto). Copia **tutto** il **RIQUADRO 2** e incollalo.

8Salva come style.css

Come prima: **File** -> **Salva con nome** , **stessa cartella mio-sito** , **Tutti i file** , nome style.css, **UTF-8** , **Salva**.

9Controlla la cartella

Dentro **mio-sito** ci devono essere **due file** : index.html e style.css. Nomi tutti **minuscoli** , senza spazi, senza **.txt** alla fine.

10Apri la tua pagina

Doppio clic su **index.html** : si apre nel browser, **con i colori**. **FATTO! Hai creato la tua pagina web.**

11Cambia i colori (il CSS)

Clic **destro** su **style.css** -> **Apri con** -> **Blocco note**. Cambia lightblue con un colore che ti piace. Salva (Ctrl \+ S) e nel browser premi F5: il colore cambia!

Colore| Scrivi| Colore| Scrivi| Colore| Scrivi  
---|---|---|---|---|---  
| pink| | lightgreen| | gold  
| orange| | lavender| | coral  
| khaki| | turquoise| | salmon  
  
## 3\. Cosa fa ogni pezzo

Pezzo di codice| Cosa fa  
---|---  
<head> ... </head>| istruzioni per il browser (non si vedono)  
<link rel="stylesheet" href="style.css">| **collega** l'HTML al file style.css  
<body> ... </body>| tutto quello che si vede nella pagina  
<h1> <h2>| titolo grande, titolo più piccolo  
<p>| un paragrafo di testo  
<ul> <li>| un elenco e le sue voci  
<div class="scheda">| una scatola; il nome **scheda** lo usa il CSS  
.scheda { background: white; }| CSS: **chi** { **proprietà** : **valore** ; }  
  
## 4\. Se qualcosa non va (succede a tutti, anche ai professionisti)

Problema| Soluzione  
---|---  
Vedo il **codice** invece della pagina| Il file è stato salvato come **.txt** : risalva con **Tutti i file**.  
La pagina è **senza colori**|  style.css non è nella stessa cartella, o ha un nome diverso (es. **Style.css** , **stile.css** , **style.css.txt**).  
Al posto di **è** vedo simboli strani| Risalva index.html scegliendo **Codifica: UTF-8**.  
Ho cambiato ma non vedo niente| Hai salvato? (Ctrl+S) Poi nel browser F5.  
  
**Hai già fatto la pagina del 30/09?** Benissimo: puoi riusare i tuoi testi. Ma per il sito servono **questi nomi esatti** : **index.html** e **style.css** , e nel <link> deve esserci **style.css**.

**Prossimo passo:** Dispensa 2 — mettiamo il tuo sito **su internet** , con un indirizzo da aprire anche sul telefono.

Classe 3 · Dispensa 1 · v1.0 · Tutti i dati negli esempi sono inventati.
