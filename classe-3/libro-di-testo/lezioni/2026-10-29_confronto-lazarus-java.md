# Lazarus e Java a confronto

**Versione 1.0** — 29/10/2026
*Libro parziale della 3INF: la lezione del 29/10/2026. Fa parte del libro di testo della classe (libro-classe3). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 29/10/2026, 2 ore, Laboratorio.
2. **Argomenti:** Percorso guidato «Lazarus e Java a confronto» (Eclipse portabile, Hello World in Java accanto a quello in Lazarus) e Documento valutato su Classroom; per chi non è riuscito a far girare Java, un Documento con le perplessità e il confronto.

### La teoria e l'esercitazione

Pagina per i ragazzi (indirizzo fisso): `https://nicolaregge-pulse.github.io/corso-informatica/3inf-confronto/` (con `?pc=14` compare la riga in bangla).

#### 00 Che cosa si fa oggi

1. Parte 1: si finisce Hello World in Eclipse, ognuno dal punto in cui è arrivato il 28/10 (passi 1-3; percorso facilitato di 3 passi per chi deve ancora scompattare o aprire Eclipse).
2. Parte 2: si completa il Documento del compito di ieri su Classroom «Hello World in Lazarus e in Java» (sezioni 2 e 4) e si aggiungono la tabella del confronto (sezione 6) e 3 frasi (sezione 7) (passi 4-10).
3. Ogni passo si chiude con «✓ Fatto» e una prova breve, che arriva al prof (riservato `dati/verifiche/3inf-confronto/arrivi/`): il cruscotto sa a che passo è ognuno.
4. Consegna su Classroom entro le 13:00.

#### 01 Come viene valutato

Il Documento del confronto viene valutato. Il voto parte da 40 (massimo 80):

1. +10 lo screenshot di Hello World in Lazarus (sezione 2)
2. +10 lo screenshot di Hello World in Eclipse/Java (sezione 4)
3. +10 la tabella del confronto completa (sezione 6): righe scritte con parole tue, non copiate dall'esempio
4. +10 le 3 frasi finali (sezione 7)
5. Consegnato entro le 13:00; dopo le 13 si valuta lo stesso, ma il ritardo viene segnato.

> [GIALLO] Protezione dagli abusi: righe vuote, copiate dall'esempio o testo senza senso non contano; gli screenshot si contano solo nel PDF della consegna vera. Il voto del cruscotto è provvisorio: decide il prof.

#### 02 Il Documento alla fine

1. Il mio codice Lazarus — di ieri
2. Il mio programma Lazarus che funziona (screenshot) — oggi: +10
3. Il mio codice Java — di ieri
4. Il mio programma Java che funziona (screenshot) — oggi: +10, lo screenshot di Eclipse
5. Con parole mie — di ieri
6. Lazarus e Java a confronto (la tabella) — nuova: +10
7. In 3 frasi: che cosa cambia e che cosa resta uguale — nuova: +10

#### 03 La tabella del confronto (sezione 6)

| # | Riga | Lazarus | Java | Domanda che aiuta |
|---|---|---|---|---|
| 1 | Ambiente | Lazarus | Eclipse | Esempio già scritto: copialo così. |
| 2 | Linguaggio | … | … | Come si chiama la lingua del codice in Lazarus? E in Eclipse? |
| 3 | Dove si scrive il codice | … | … | In quale file e in quale parte della finestra scrivi le istruzioni? |
| 4 | Come si avvia | … | … | Quale tasto premi in Lazarus? Quale bottone in Eclipse? |
| 5 | La finestra e il bottone | … | … | Come si chiamano in Lazarus? E nel codice Java (guarda le righe con new)? |
| 6 | Il punto e virgola e le parentesi | … | … | Dove metti il ; in tutti e due? Che virgolette usa ShowMessage e che virgolette usa Java? |
| 7 | begin…end contro { } | … | … | Con che cosa apri e chiudi un blocco di istruzioni in Lazarus? E in Java? |
| 8 | File del progetto | … | … | Quali file ha il progetto Lazarus (.lpi .pas .lfm)? E quello Java (.java, e dopo il Run .class)? |

La riga 1 è l'esempio già scritto: non conta per il voto.

#### 04 I passi

##### Passo 1 · Dove sei arrivato?

Guarda il tuo PC e scegli la frase giusta. Non ci sono risposte sbagliate: serve a sapere da dove ripartire.

Prova: Dove sei arrivato con Eclipse? Scelte: Hello World in Eclipse funziona già · Eclipse si apre, ma il programma non funziona · Non ho ancora scompattato o aperto Eclipse

##### Passo 2 · Eclipse aperto, con Main.java

Percorso facilitato (3 passi):

1. **Scompatta lo ZIP in una cartella corta.** Fai clic destro sul file eclipse-java-2026-09-R-win32-x86_64.zip e scegli «Estrai tutto…». Nella casella del percorso premi Ctrl + A, scrivi il percorso qui sotto, clicca «Estrai» e aspetta che la finestra si chiuda da sola.

```
C:\Users\Public\ec
```

2. **Apri Eclipse e crea il progetto.** Apri la cartella C:\Users\Public\ec\eclipse e fai doppio clic su eclipse.exe. Clicca «Launch», poi «Later». A sinistra clicca «Create a Java project», scrivi il nome qui sotto, togli la spunta «Create module-info.java» e clicca «Finish».

```
HelloWorld
```

3. **Incolla la classe Main e premi Run.** Clicca «Copia» sul codice qui sotto. A sinistra apri HelloWorld e clicca una volta su src. Premi Ctrl + V: Eclipse crea da solo Main.java. Poi in alto clicca il cerchio verde (Run).

```
import javax.swing.*;
import java.awt.FlowLayout;

public class Main {

    public static void main(String[] args) {
        JFrame finestra = new JFrame("Il mio primo programma");
        JButton bottone = new JButton("Premi");

        bottone.addActionListener(e -> JOptionPane.showMessageDialog(finestra, "Hello World"));

        finestra.setLayout(new FlowLayout());
        finestra.add(bottone);
        finestra.setSize(300, 150);
        finestra.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        finestra.setVisible(true);
    }

}
```

Chi ha già Eclipse aperto riparte dalla guida `docs/3inf-eclipse-guida/`:

1. Eclipse non si apre o dà un errore: guida, passi 1-6
2. Eclipse è aperto ma non c'è il progetto HelloWorld: guida, passi 9-12
3. C'è il progetto ma non c'è Main.java: guida, passi 13-17
4. Main.java c'è, ma il codice è vecchio o ha la X rossa: guida, passi 18-22, poi «Errori comuni» in fondo

Prova: Scrivi il nome della linguetta aperta al centro di Eclipse, sopra il codice.

##### Passo 3 · Run: la finestrella Hello World

1. In alto clicca il cerchio verde con il triangolo bianco: è «Run» (Esegui), come F9 in Lazarus.
2. Si apre la finestra con il bottone Premi: cliccalo.

> [GIALLO] Non vedi la finestra? È dietro Eclipse: cercala nella barra in basso dello schermo.

Prova: Che cosa c'è scritto nella finestrella che si apre?

##### Passo 4 · Apri il tuo Documento

1. Clicca il bottone qui sotto: si apre il compito su Classroom «Hello World in Lazarus e in Java».
2. A destra, nel riquadro «Il tuo lavoro», clicca il Documento con il tuo nome.

Link: https://classroom.google.com/c/MjUzMjQ1NzQ2NDBa/a/MjU1MTAyOTQzNjBa/details

> [GIALLO] Hai già consegnato ieri? In alto a destra clicca «Annulla consegna»: così puoi modificare il Documento. Alla fine lo consegni di nuovo (passo 10).

Le sezioni del Documento sono nella sezione 02.

Prova: Come si chiama la sezione 2 del tuo Documento? Scelte: Il mio codice Java · Il mio programma Lazarus che funziona (screenshot) · Con parole mie (giusta: «Il mio programma Lazarus che funziona (screenshot)»)

##### Passo 5 · Sezione 2: lo screenshot di Lazarus

1. Apri Lazarus e il tuo progetto di ieri. Premi F9 e poi il bottone: compare il saluto.
2. Premi Windows + Maiusc + S e trascina il mouse sopra la finestra del programma.
3. Nel Documento clicca nella riga vuota sotto il titolo «2.» e premi Ctrl + V.

> [GIALLO] Non trovi il progetto di ieri? Fanne uno nuovo: «File», «Nuovo», «Applicazione»; metti un bottone; doppio clic sul bottone; scrivi ShowMessage('Hello World'); e premi F9.

Prova: Che cosa scrive il tuo programma Lazarus quando premi il bottone?

##### Passo 6 · Sezione 4: lo screenshot di Eclipse

1. Torna in Eclipse, premi Run e poi il bottone Premi: si apre la finestrella Hello World.
2. Premi Windows + Maiusc + S e prendi la finestra con la finestrella.
3. Nel Documento clicca nella riga vuota sotto il titolo «4.» e premi Ctrl + V.

Prova: Quante immagini ci sono adesso nel tuo Documento? Scrivi il numero.

##### Passo 7 · Sezione 6: la tabella, prima metà

1. Nel Documento premi Ctrl + Fine: vai in fondo.
2. Scrivi il titolo:

```
6. Lazarus e Java a confronto
```

Sotto, scrivi la riga di esempio:

```
Ambiente: Lazarus - Eclipse
```

Poi scrivi le righe da 2 a 5 della tabella qui sotto, una per riga, con parole tue: il nome della riga, i due punti, Lazarus, un trattino, Java. La domanda accanto ti aiuta.

Righe 1-5 della tabella (sezione 03).

Prova: Scrivi qui la tua riga «Come si avvia», uguale a quella del Documento.

##### Passo 8 · Sezione 6: la tabella, seconda metà

Sotto le righe di prima scrivi le righe da 6 a 8, sempre una per riga e con parole tue.

Righe 6-8 della tabella (sezione 03).

> [GIALLO] Le righe vuote, copiate dall'esempio o senza senso non contano per il voto.

Prova: Scrivi qui la tua riga «File del progetto», uguale a quella del Documento.

##### Passo 9 · Sezione 7: in 3 frasi

1. Sotto la tabella scrivi il titolo:

```
7. In 3 frasi: che cosa cambia e che cosa resta uguale
```

Poi scrivi 3 frasi tue, una per riga. Puoi cominciare così:

1. In tutti e due i programmi resta uguale che …
2. In Java invece cambia che …
3. Secondo me il più facile è … perché …

Prova: Scrivi qui la tua prima frase, uguale a quella del Documento.

##### Passo 10 · Consegna su Classroom

1. Torna nella scheda di Classroom del compito.
2. In alto a destra clicca il bottone blu «Consegna», poi ancora «Consegna» nella finestrella.

> [GIALLO] Entro le 13:00. Dopo le 13 il Documento si valuta lo stesso, ma il ritardo viene segnato.

Prova: Che cosa c'è scritto adesso sul bottone in alto a destra? Scelte: Consegna · Annulla consegna · Aggiungi o crea (giusta: «Annulla consegna»)

#### 05 Per il docente: che cosa vede il cruscotto

1. Colonna Percorso: passo raggiunto (1-10) e da quanti minuti il ragazzo è fermo.
2. Colonna Documento: consegnato sì/no e a che ora; sezioni compilate (lette dal Documento); dopo la consegna le immagini contate dal PDF.
3. Voto 40-80 con il conto, provvisorio: decide il prof. Tutti i presenti.

## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
