<!-- generato da dispensa-4-seconda-pagina-menu-IT.html con html2md.py: non modificare a mano, si rigenera -->

v1.0

# Dispensa 4 — La seconda pagina e il menu

Classe 3 · Informatica · 08/10/2026 · un sito vero ha più pagine collegate · italiano

**Cosa ottieni oggi:** il tuo sito ha **due pagine** (Home e La mia passione) e un **menu** in alto per passare dall'una all'altra, come i siti veri. Le due pagine usano lo **stesso style.css** : cambi un colore e cambia in tutto il sito.

## 1\. Il codice nuovo

RIQUADRO 5 — file nuovo passione.html (la seconda pagina)
    
    
    <!DOCTYPE html>
    <html lang="it">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>La mia passione</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <nav class="menu">
        <a href="index.html">Home</a>
        <a href="passione.html">La mia passione</a>
      </nav>
    
      <h1>La mia passione: il calcio</h1>
    
      <div class="scheda">
        <h2>Perché mi piace</h2>
        <p>Mi piace giocare in squadra e allenarmi con gli amici.</p>
    
        <h2>Tre cose che so fare</h2>
        <ol>
          <li>Passare la palla con precisione</li>
          <li>Correre veloce</li>
          <li>Parare un rigore</li>
        </ol>
    
        <h2>Lo sapevi che...</h2>
        <p>Il primo mondiale di calcio si è giocato nel 1930.</p>
      </div>
    
      <p class="piede">Sito creato da me - 2026</p>
    </body>
    </html>
    

RIQUADRO 6 — il menu: da mettere in index.html, subito dopo <body>
    
    
      <nav class="menu">
        <a href="index.html">Home</a>
        <a href="passione.html">La mia passione</a>
      </nav>
    

RIQUADRO 7 — in fondo a style.css
    
    
    .menu {
      background: darkblue;
      padding: 10px;
      border-radius: 10px;
    }
    
    .menu a {
      color: white;
      text-decoration: none;
      font-weight: bold;
      margin: 0 12px;
    }
    
    .menu a:hover {
      color: orange;
    }
    

## 2\. I passi, uno alla volta

1Crea il file nuovo

Nel repository **mio-sito** : bottone **Add file** (grigio) -> **Create new file** (Crea nuovo file). In alto, nel campo del nome, scrivi passione.html.

github.com/tuonome/mio-sito/new/main

mio-sito / passione.html

Enter file contents here

2Incolla la seconda pagina

Nel riquadro grande incolla il RIQUADRO 5. Poi **Commit changes...** -> **Commit changes**.

3Fallo tuo

Con la **matita** cambia la pagina: la **tua** passione (sport, musica, cucina, un videogioco, un paese...), perché ti piace, tre cose che sai fare, una curiosità. Poi Commit.

4Il menu anche nella Home

Apri **index.html** -> **matita**. Subito dopo la riga <body> incolla il RIQUADRO 6. Commit.

5Lo stile del menu

Apri **style.css** -> **matita** -> in fondo incolla il RIQUADRO 7. Commit.

6Prova il menu

Aspetta 1 minuto, apri il sito, Ctrl \+ F5. Clic su **La mia passione** , poi su **Home** : passi da una pagina all'altra. **FATTO! Hai un sito a due pagine.**

7Mostralo

L'indirizzo della seconda pagina è https://tuonome.github.io/mio-sito/passione.html. Aprila sul telefono e falla vedere a un compagno.

## 3\. Se qualcosa non va

Problema| Soluzione  
---|---  
Clic su **La mia passione** e vedo **404**|  Il file deve chiamarsi esattamente **passione.html** (minuscolo), come nel menu.  
La seconda pagina è **senza colori**|  Manca la riga <link rel="stylesheet" href="style.css"> nel <head>.  
Il menu c'è ma è **senza stile**|  Il RIQUADRO 7 non è in style.css, oppure aspetta un minuto e Ctrl \+ F5.  
  
**Carta e penna:** disegna la **mappa del sito** : due rettangoli (index.html e passione.html) con le frecce del menu, e una freccia da ciascuno verso style.css.

Classe 3 · Dispensa 4 · v1.0
