<!-- generato da dispensa-3-migliora-sito-github-IT.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 3 — Migliora il tuo sito direttamente su GitHub

Classe 3 · Informatica · 07/10/2026 · la matita, il commit, la storia delle versioni · italiano

**Cosa ottieni oggi:** nel tuo sito compaiono due **bottoni-link** che cambiano colore quando ci passi sopra, e la scheda ha un'**ombra**. Modifichi i file **direttamente su GitHub** , senza scaricare niente: ogni modifica è un **commit** , cioè una nuova **versione** salvata nella storia.

**Il sito è pubblico:** anche oggi solo nome o soprannome, niente dati personali.

## 1\. Il codice nuovo

Il codice si copia dalla **pagina del corso** con il bottone **Copia** (link nel compito su Classroom).

RIQUADRO 3 — da aggiungere in index.html (prima di </div>)
    
    
        <h2>I miei siti preferiti</h2>
        <p>
          <a class="bottone" href="https://it.wikipedia.org/wiki/HTML" target="_blank">Cos'è l'HTML</a>
          <a class="bottone" href="https://www.w3schools.com/css/" target="_blank">Imparo il CSS</a>
        </p>
    

RIQUADRO 4 — da aggiungere in fondo a style.css
    
    
    .scheda {
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    .bottone {
      display: inline-block;
      background: darkblue;
      color: white;
      padding: 8px 14px;
      border-radius: 8px;
      text-decoration: none;
      margin: 4px;
    }
    
    .bottone:hover {
      background: orange;
    }
    

## 2\. I passi, uno alla volta

1Apri il tuo repository

Vai su github.com, entra (Sign in) e apri il repository **mio-sito** (in alto a sinistra, o dal tuo profilo).

2Apri index.html e premi la matita

Nell'elenco dei file clic su **index.html**. In alto a destra del codice clic sulla **matita** ✎ (Modifica).

github.com/tuonome/mio-sito/blob/main/index.html

**mio-sito / index.html**

Raw ✎ <- matita ⋮

3Incolla il RIQUADRO 3

Trova la riga <p>Lavorare con i computer.</p> (o il tuo sogno). Clic alla fine della riga, premi Invio e incolla il RIQUADRO 3 (Ctrl \+ V). Deve stare **prima** di </div>.

4Salva: Commit changes

In alto a destra bottone **verde** **Commit changes...** -> si apre una finestrella -> di nuovo **Commit changes** (verde).

Cancel changes Commit changes... <- 1

**Commit changes**

Commit message: Update index.html

Commit changes <- 2

5Ora style.css

Torna al repository (clic su **mio-sito** in alto), clic su **style.css** -> **matita**. Vai **in fondo** , premi Invio e incolla il RIQUADRO 4. Poi **Commit changes...** -> **Commit changes**.

6Guarda il sito

Aspetta 1 minuto, apri il tuo sito (https://tuonome.github.io/mio-sito/) e premi Ctrl \+ F5. Passa con il mouse sui bottoni: diventano arancioni! **FATTO!**

7La storia delle versioni

Nel repository clic sul file **index.html** -> in alto a destra **History** (Cronologia, icona con l'orologio). Vedi la lista dei tuoi **commit** : ogni riga è una versione del file, con data e messaggio. Fai uno **screenshot** : serve per il compito.

8Fallo tuo

Cambia i link con **due siti utili che piacciono a te** (niente social, niente siti vietati) e i colori dei bottoni. Ogni volta: matita -> Commit.

## 3\. Cosa fa ogni pezzo

Pezzo| Cosa fa  
---|---  
<a href="...">testo</a>| un **link** : **href** è l'indirizzo dove porta  
target="_blank"| apre il link in una scheda nuova  
class="bottone"| il nome che usa il CSS per dare l'aspetto  
.bottone:hover| lo stile quando il mouse **passa sopra**  
box-shadow| l'ombra della scatola  
commit| una versione salvata, con data e messaggio  
  
**Non vedi i cambiamenti?** Aspetta ancora un minuto e premi Ctrl \+ F5 (ricarica forzata). Se il sito si rompe: apri **History** , guardi la versione di prima e la ricopi. Con Git **niente si perde**.

**Carta e penna:** disegna una linea del tempo con i tuoi commit (pallino = versione) e scrivi sotto cosa hai cambiato in ognuno.

Classe 3 · Dispensa 3 · v1.0
